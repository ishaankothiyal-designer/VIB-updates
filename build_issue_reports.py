"""Creta and Brezza: shared Swift report system, vehicle-specific evidence stories."""
from pathlib import Path
from bs4 import BeautifulSoup as Soup
from html import escape as e
import json
from build_swift_report import chapter,details,question,fmt,amount
from swift_mileage import render_mileage
B=Path(__file__).resolve().parent;D=B/'dist'
def fragment(html):return Soup(html,'html.parser')
def build_issue_reports():
 for c in json.loads((D/'cars.json').read_text())['cars']:
  if c['id'] not in ['creta','brezza']:continue
  creta=c['id']=='creta';short='Creta' if creta else 'Brezza';full=c['name']+' '+c['variant'];owners='First owner' if c['owners']==1 else 'Second owner'
  s=Soup((D/'sample-swift.html').read_text(),'html.parser')
  s.title.string=f'{c["year"]} {short} — VIB vehicle history report'
  s.select_one('meta[name=description]')['content']=f'Read this {c["year"]} {short} report: photos, '+('lender entry and closure documents' if creta else 'unpaid challan and document dates')+', service history and questions for the seller.'
  def replace(selector,html):s.select_one(selector).replace_with(fragment(html))
  replace('.cover-copy h1',f'<h1>{e(c["name"])} <span>{e(c["variant"])}</span></h1>')
  s.select_one('.cover-specs').string=f'{c["year"]} · {c["fuel"]} · {c["transmission"]}'
  replace('.cover-registration',f'<p class="cover-registration">{c["registration"]}<span>{c["region"]}</span></p>')
  covervalues=s.select('.cover-facts dd');covervalues[0].clear();covervalues[0].append(fragment(f'{c["declaredKm"]:,} <span>km</span>'));covervalues[1].string=owners;covervalues[2].string=f'{len(c["services"])} on record'
  s.select_one('.report-number').string=f'{fmt(c["reportDate"])} · {c["reportId"]}'
  labels=['Front right','Rear right','Dashboard','Front left']
  for i,button in enumerate(s.select('.photo-thumb')):button.img['src']=c['photos'][i]['src']
  for selector in ['#selected-photo','#viewer-photo']:
   s.select_one(selector)['src']=c['photos'][0]['src'];s.select_one(selector)['alt']=full+' — front right view'
  s.select_one('#photo-viewer-title').string=full
  for a,p in zip(s.select('noscript a'),c['photos']):a['href']=p['src']
  s.select_one('.condition-value strong').string=str(c['score']['value']);s.select_one('.condition-track span')['style']=f'width:{c["score"]["value"]}%';s.select_one('.condition-snapshot h2').string=c['score']['label']
  findings=[('finance','The lender entry is still active.','Closure documents have not been provided.','Documents needed'),('claims','A repair claim is on record.','Read the invoice and inspect the work.',amount(c['claim']['amount'])),('mileage','Compare the dated mileage records.','The seller declares a higher reading than the last invoice.',f'{c["declaredKm"]:,} km')] if creta else [('challans','One challan is marked unpaid.','Verify the current status and payment receipt.','₹1,500'),('challans','The PUC date has passed.','Ask for a renewed certificate.','9 Oct 2026'),('ownership','Two owners are recorded.','Match the seller’s details with the registration certificate.','Second owner')]
  replace('.priority-findings','<div class="priority-findings"><p class="report-kicker">Before you decide</p><h2 id="overview-heading">'+('Start with the lender entry.' if creta else 'Start with the open challan.')+'</h2>'+''.join(f'<a href="#{anchor}"><span><b>{title}</b><small>{copy}</small></span><strong class="finding-word">{value}</strong></a>' for anchor,title,copy,value in findings)+'</div>')
  order=['photos','finance','mileage','ownership','claims','challans','valuation','timeline'] if creta else ['photos','challans','ownership','mileage','finance','claims','valuation','timeline']
  navlabels={'photos':'Photos','finance':'Finance','mileage':'Mileage','ownership':'Ownership','claims':'Repairs','challans':'Challans & documents','valuation':'Price','timeline':'Timeline'}
  links=''.join(f'<a href="#{id}">{navlabels[id]}</a>' for id in order)
  s.select_one('.chapter-nav').clear();s.select_one('.chapter-nav').append(fragment(links));s.select_one('.chapter-menu nav').clear();s.select_one('.chapter-menu nav').append(fragment(links))
  chapters={}
  def add(id,label,title,intro,body,prompt,source):chapters[id]=chapter(id,order.index(id)+1,label,title,intro,body,prompt,source)
  if creta:
   financebody='<div class="issue-lead"><span class="record-state attention">Active lender entry</span><h3>The entry is present.<br>The closure proof is missing.</h3><p>The registration record shows a lender’s interest. The available records do not establish the loan balance or repayment status.</p></div><ol class="document-path"><li class="recorded"><span>On record</span><h4>Lender entry</h4><p>Active in the registration record.</p></li><li><span>To request</span><h4>Closure documents</h4><p>No closure document has been provided.</p></li><li><span>To verify</span><h4>Current registration</h4><p>Compare the latest record with the lender’s documents.</p></li></ol>'+details([('Lender description',c['lender']),('Loan balance','Unavailable'),('Repayment status','Unavailable')])
   add('finance','Finance & transfer','Before the transfer,<br>follow up on the lender.','This is the first question for this Creta. Ask to see the closure documents, then check the current registration entry.',financebody,question('Can we review the lender’s closure documents and the latest registration record?',link=('guide-finance.html','Understand lender entries')),'Registration finance entry')
  else:
   add('finance','Finance & transfer','Check the current<br>finance record.','No active lender entry is shown in this record set. Compare it with the current registration certificate.','<div class="issue-lead"><span class="record-state">No active entry shown</span><h3>Keep the latest record beside you.</h3><p>A missing active entry does not establish the vehicle’s full finance history.</p></div>'+details([('Active lender entry','Not shown'),('Loan balance / repayment','Unavailable')]),question('Does the latest registration certificate show the same finance status?'),'Registration finance entry')
  rows=''.join(f'<li><div><h4>{e(r["offence"])}</h4><p>{fmt(r["date"])} · {r["id"]}</p></div><div><strong>{amount(r["amount"])}</strong><span>{r["status"]}</span></div></li>' for r in c['challans'])
  if creta:docbody='<div class="issue-lead"><span class="record-state">No challans in this record set</span><h3>Check the dates as well.</h3><p>Confirm the current challan status with the seller. An empty record set is not a guarantee of no outstanding entries.</p></div>'
  else:docbody='<div class="issue-lead challan-receipt"><span class="record-state attention">One unpaid entry</span><h3>₹1,500</h3><p>Recorded as unpaid. Verify today’s status before discussing the transfer.</p></div><ul class="challan-list">'+rows+'</ul><div class="document-followup"><span>What to ask for</span><h4>A payment receipt and the current status.</h4><p>Match the receipt to challan CH-08-001. The record here does not confirm a later payment.</p></div>'
  docbody+='<div class="surface-divider"></div><div class="surface-heading"><h3>Document dates</h3></div>'+details([('Registration valid until',fmt(c['validUntil'])),('PUC valid until',fmt(c['pucUntil'])),('PUC at report date','Within recorded validity' if creta else 'Recorded validity has ended'),('Road tax','Paid in the record')])
  add('challans','Challans & documents','Clear up the challan.<br>Check the document dates.' if not creta else 'Keep the documents<br>in date.','This Brezza has one unpaid entry and a PUC date that has passed. Take both questions to the seller.' if not creta else 'Read validity dates with the current documents. Check for any entries recorded after this report.',docbody,question('Can we verify this challan’s payment and see a renewed PUC certificate?' if not creta else 'Can we check the current challan status and document dates?'),'Challan and registration record set')
  ownbody='<div class="surface-heading"><h3>Identity & ownership</h3><span class="record-state">'+owners+'</span></div>'+details([('First registered',fmt(c['registeredOn'])),('Registration region',c['region']),('Registration',c['registration']),('Owners recorded',str(c['owners'])),('Fuel / transmission',c['fuel']+' / '+c['transmission']),('Usage',c['usage']),('Modifications',c['modifications']),('Registration valid until',fmt(c['validUntil']))],'facts-grid')+'<p class="surface-footnote">Factory equipment and engine specifications have not been verified in this record set.</p>'
  add('ownership','Identity & ownership','Match the car.<br>Then match the seller.','Read the registration certificate beside the car and the seller’s documents. Confirm the recorded ownership details.',ownbody,question('Do the seller and vehicle details match the current registration certificate?'),'Registration record')
  graph,readings=render_mileage(c)
  visits=''.join(f'<li><div class="visit-meta"><time datetime="{r["date"]}">{fmt(r["date"])}</time><strong>{r["km"]:,} km</strong></div><div><h4>{r["work"]}</h4><p>{e(r["workshop"])}</p><span>{r["id"]}</span></div><b>{amount(r["amount"])}</b></li>' for r in reversed(c['services']))
  graph+=f'<details class="service-invoices" open><summary>Service invoices<span>{len(c["services"])} visits</span></summary><ol>{visits}</ol></details>'
  add('mileage','Mileage & service','Follow the readings<br>through the years.','The seller’s declaration is higher than the last service reading. Compare both with the odometer and the original invoices.',graph,question('Can we compare these invoices with the odometer today?'),'Service invoices and seller declaration')
  cl=c['claim'];claimbody=f'<div class="claim-feature"><div><span>Repair claim · {fmt(cl["date"])}</span><strong>{amount(cl["amount"])}</strong><p>{cl["part"]}</p></div><span class="record-state">{cl["status"]}</span></div>'+details([('Accident severity','Not established'),('Current repair condition','Not assessed')])+'<div class="surface-divider"></div><div class="surface-heading"><h3>Insurance policy</h3></div>'+details([('Cover type',c['policyType']),('Policy valid until',fmt(c['policyUntil']))])
  add('claims','Insurance & repairs','Understand the repair.<br>Inspect the work.','The claim records a repair and an amount. It does not establish accident severity or the quality of the work today.',claimbody,question('Can we read the repair invoice and inspect these parts?',link=('guide-inspection.html','Use records with an inspection')),'Policy and claim record set')
  low,high=c['priceRangeLakh'];listing=''.join(f'<div><time datetime="{r["date"]}">{fmt(r["date"])}</time><strong>{amount(r["amount"])}</strong><span>Asking price</span></div>' for r in c['askingPrices'])
  price=f'<span class="value-label">Reference price range</span><h3 class="price-range">₹{low:.1f}–{high:.1f} <span>lakh</span></h3><p class="price-context">{c["year"]} {short} · {c["region"]}</p><div class="price-range-line" aria-hidden="true"><span></span><span></span></div><p class="surface-footnote">A reference range for this sample, not a live valuation or an offer.</p><div class="surface-divider"></div><h4 class="subheading">Previous asking prices</h4><div class="asking-history">{listing}</div><p class="surface-footnote">Asking prices are not completed-sale prices. Comparable sales and peer ranking are unavailable.</p>'
  add('valuation','Price context','Put the history<br>beside the price.','Discuss the asking price with the records and a physical inspection in mind.',price,question('How does the asking price reflect the records and the car today?'),'Reference range and listing history')
  events=[(c['registeredOn'],'First registration',c['region'])]+[(r['date'],'Service invoice',f'{r["km"]:,} km · {r["work"]}') for r in c['services']]+[(cl['date'],'Repair claim '+cl['status'].lower(),f'{amount(cl["amount"])} · {cl["part"]}')]+[(r['date'],'Asking price recorded',amount(r['amount'])) for r in c['askingPrices']]+[(r['date'],r['offence'],f'{amount(r["amount"])} · {r["status"]}') for r in c['challans']]+[(c['sellerDate'],'Seller mileage declaration',f'{c["declaredKm"]:,} km')]
  if not creta:events.append((c['pucUntil'],'Recorded PUC validity ended','Ask for a renewed certificate.'))
  timeline='<ol class="swift-timeline">'+''.join(f'<li><time datetime="{d}">{fmt(d)}</time><div><h3>{h}</h3><p>{copy}</p></div></li>' for d,h,copy in sorted(events,key=lambda r:r[0]))+'</ol>'
  add('timeline','The complete timeline','Read the dates<br>together.','The available registration, service, repair and listing records, each with its own date.',timeline,question('Can you help me fill in the gaps between these records?'),'Combined record set')
  anchor=s.select_one('.chapter-menu')
  for el in s.select('.swift-chapter'):el.decompose()
  for id in order[1:]:
   node=fragment(chapters[id]);anchor.insert_after(node);anchor=s.select_one('#'+id)
  payload={'vehicleName':full,'photos':[{'src':p['src'],'label':label} for p,label in zip(c['photos'],labels)],'readings':readings}
  s.select_one('#swift-report-data').string=json.dumps(payload,ensure_ascii=False).replace('</','<\\/')
  s.body['data-vehicle']=c['id']
  (D/f'sample-{c["id"]}.html').write_text(str(s))
if __name__=='__main__':build_issue_reports();print('Built Creta and Brezza issue-led reports.')
