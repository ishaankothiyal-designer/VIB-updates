"""Build the minimal V5 homepage from the shared data and original chrome/reading room."""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape as e
B=Path(__file__).resolve().parent;D=B/'dist'
def frag(t):return BeautifulSoup(t,'html.parser')
def card(label,title,visual,caption):
 return f'<div class="evidence-card"><span class="evidence-card-label">{label}</span><h3>{title}</h3><div class="evidence-card-art">{visual}</div><p>{caption}</p></div>'
def asset(name,alt=''):
 return f'<img src="assets/{name}" alt="{alt}" width="280" height="220" loading="lazy">'
def story(id,title,description,items,reverse=False):
 steps=''
 for i,(heading,copy,mini,anchor) in enumerate(items):
  link_text={'ownership':'View registration records','mileage':'View mileage records','finance':'Review the lender entry','claims':'Review the repair record','challans':'Review challans and documents','valuation':'View the price context','photos':'View vehicle photos'}[anchor]
  # Each explanation owns its evidence. No detached visual layer or pinned scroll state.
  visual='' if reverse else f'<details class="inline-card"><summary>See sample details</summary>{mini}</details>'
  steps+=f'<article class="story-step" id="{id}-{i+1}"><div class="story-copy"><h3>{heading}</h3><p>{copy}</p><a href="sample-swift.html#{anchor}" class="story-link">{link_text}</a></div>{visual}</article>'
 return f'<section class="scroll-story {"story-reverse" if reverse else ""}" id="{id}"><div class="wrap"><div class="story-heading"><h2>{title}</h2><p>{description}</p></div><div class="story-layout"><div class="story-steps">{steps}</div></div></div></section>'

def build_home():
 s=frag((B/'data/home-template-original.html').read_text())
 # Retain the approved chrome, FAQ, guides and contact sections, rebuilding only annotated sections.
 for sel in ['.hero-baseline','.car-files']:
  for el in s.select(sel):el.decompose()
 from hero_deck import render_hero_deck
 hero=s.select_one('.hero');hero.clear();hero.append(frag(render_hero_deck()))
 evidence=s.select_one('#evidence');evidence.clear();evidence.append(frag('''<div class="wrap mileage-story"><div class="mileage-intro"><h2>What a history report<br>can help you spot.</h2><p>Example: a 2020 Swift with conflicting mileage records. The car is one example, not a limit on who this preview is for.</p></div><div class="mileage-scene"><div class="scene-orbit" aria-hidden="true"></div><article class="service-receipt"><div class="receipt-top"><span>Service invoice</span><time datetime="2026-07-08">8 Jul 2026</time></div><span class="receipt-label">Odometer recorded</span><strong>72,000 <small>km</small></strong><div class="receipt-rule"></div><span class="receipt-foot">Maruti Suzuki Swift · 2020</span></article><div class="mileage-connection"><svg viewBox="0 0 240 110" aria-hidden="true"><path class="mileage-arc" d="M8 18 C100 12 104 94 225 86" fill="none"/><path d="m213 76 13 10-14 8" fill="none"/></svg><strong>14,000 <span>km lower</span></strong></div><article class="odometer-record"><div class="odometer-top"><span>Seller declaration</span><time datetime="2026-11-20">20 Nov 2026</time></div><p>The later reading</p><div class="odometer-digits" aria-label="58,000 kilometres"><span>0</span><span>5</span><span>8</span><span>0</span><span>0</span><span>0</span></div><div class="odometer-bottom"><span>km</span><span>Needs verification</span></div></article></div><div class="mileage-question"><div><span>Your next question</span><h3>“Can we compare the service invoice with the odometer?”</h3><p>Check the original documents and the seller’s explanation. The difference alone does not establish tampering.</p></div><a class="button ink" href="sample-swift.html#mileage">View this Swift’s report</a></div></div>'''))
 items=[
 ('Identity & ownership','Start with the basics. Do the registration details match the car and the person selling it?',card('Identity & ownership','Match the details.',asset('1b4dc.webp'),'<b>First owner</b><span>Registration valid to 7 Jul 2035</span>'),'ownership'),
 ('Service & mileage','Follow the dated readings. A later, lower declaration gives you a specific question to ask.',card('Service & mileage','Two dates. One discrepancy.','<div class="mini-reading"><span>8 Jul 2026<b>72,000<small> km</small></b></span><span>20 Nov 2026<b>58,000<small> km</small></b></span></div>','Ask to see the original service invoice.'),'mileage'),
 ('Finance & transfer','An active lender entry needs a follow-up. Ask for closure documents before discussing the transfer.',card('Finance & transfer','Ask for the closure letter.',asset('030ff.webp'),'<b>Lender entry active</b><span>Loan balance unavailable</span>'),'finance'),
 ('Insurance & repairs','A claim starts a conversation about the work. Read the invoice and inspect the repair.',card('Insurance & repairs','Understand the repair.',asset('43160.webp'),'<b>₹42,000 claim recorded</b><span>16 Aug 2023 · settled</span>'),'claims'),
 ('Challans & documents','Check unpaid entries and document dates. Verify the current status with the seller.',card('Challans & documents','Clear the open questions.','<div class="mini-challans"><span>Parking violation<b>₹1,000</b></span><span>Speeding violation<b>₹2,000</b></span></div>','<b>₹3,000 in unpaid entries</b><span>Check payment before transfer</span>'),'challans'),
 ('Price context','Put the asking price beside the history and the car’s condition. A range is a starting point.',card('Price context','Bring the records to the price.','<div class="mini-price">₹3.4–3.8<span>lakh · reference range</span></div>','An estimate, not an offer.'),'valuation')]
 s.select_one('#report-contents').replace_with(frag(story('report-contents','Six parts of a car’s history.','See what each section helps you check. These details use the Swift sample; available records vary by vehicle.',items)))
 process=[
 ('Follow the evidence.','Start with the dated record and its source. Keep a seller declaration separate from a service invoice.',card('The finding','The readings conflict.','<div class="mini-reading"><span>Service invoice<b>72,000<small> km</small></b></span><span>Seller declaration<b>58,000<small> km</small></b></span></div>','Read each value with its date and source.'),'mileage'),
 ('Ask for the original.','Compare the original invoice, the vehicle details and the odometer. Ask the seller to explain the gap.',card('The document','Put the original beside it.',asset('b39dc.webp'),'“Can we check the service invoice together?”'),'mileage'),
 ('See the car today.','Use the history to focus an inspection and test drive. Check what the records cannot tell you.',card('The car today','History meets inspection.',asset('records-inspection.webp'),'Use the records. Inspect the car.'),'photos')]
 s.select_one('#process').replace_with(frag(story('process','Turn a finding into a next step.','A short checklist to take to the seller.',process,True)))
 closing=s.select_one('.closing-file');closing.clear();closing.append(frag('''<div class="wrap closing-file-inner"><div><h2>Ready to read<br>a sample report?</h2><p>Choose an example that matches your question. Each sample explains its findings, limits and what to ask next.</p><a class="button gold" href="#sample-reports">Choose a sample report</a></div><div class="closing-object"><div class="closing-object-under"></div><article class="closing-report"><span>Vehicle history report</span><img src="assets/report-folio.webp" alt="Blue ink illustration of a vehicle report folio and car key" width="900" height="600" loading="lazy"><div><h3>A closer look<br>starts here.</h3><span>Records. Photos. Next steps.</span></div></article></div></div>'''))
 # Correct all retained prototype framing in the reading sections.
 for node in list(s.find_all(string=True)):
  if node.parent.name in ['script','style']:continue
  t=str(node).replace('The sample’s 64/100 is an illustrative design value, not a calculated result. VIB’s condition-score methodology describes a relative prediction of physical condition. It is not a guarantee or a summary of every legal and financial record.','A condition score describes predicted physical condition. Read it with the supporting records and an inspection. Sample scores are preset for this preview; legal and financial findings are shown separately.').replace('What does the sample score mean?','How should I read a condition score?')
  if t!=str(node):node.replace_with(t)
 for el in s.select('link[href="home.css"]'):pass
 s.head.append(frag('<link href="minimal-home.css" rel="stylesheet"><link href="hero-deck.css" rel="stylesheet"><script src="hero-deck.js" defer></script>'))
 # Scroll story functions load before the existing preference-aware motion owner.
 motion=s.select_one('script[src="motion.js"]');s.select_one('script[src="hero-deck.js"]').extract();motion.insert_after(frag('<script src="hero-deck.js" defer></script>'))
 s.select_one('meta[name=description]')['content']='Read a car’s history one record at a time. Explore a VIB sample report with photographs, dated records and the questions to ask.'
 # The available experience is explicitly a preview, not an unconnected registration form.
 import json
 cars=json.loads((D/'cars.json').read_text())['cars']
 lead=[('swift','Mileage discrepancy','Compare conflicting readings.'),('creta','Finance before transfer','Follow up on the lender entry.'),('baleno','Read a service history','Follow dated invoices and their limits.')]
 by_id={c['id']:c for c in cars}
 choices=''.join(f'<a class="sample-choice" href="sample-{id}.html"><span class="sample-topic">{topic}</span><h3>{e(by_id[id]["name"])}</h3><p>{copy}</p><span class="sample-choice-action">Read this sample <span aria-hidden="true">→</span></span></a>' for id,topic,copy in lead)
 all_samples=''.join(f'<a href="sample-{c["id"]}.html">{e(c["name"])} <span>{c["year"]} · {e(c["fuel"])}</span></a>' for c in cars)
 chooser=f'<section id="sample-reports" class="sample-explorer"><div class="wrap"><div class="section-intro"><p class="eyebrow">EXPLORE THE PREVIEW</p><h2>Start with a question.<br>Choose an example.</h2><p>These fictional reports show how to read a car’s history. They do not establish live coverage for a make, model or registration.</p></div><div class="sample-options">{choices}</div><details class="all-samples"><summary>Browse all ten sample cars</summary><div class="sample-list">{all_samples}</div></details><p class="availability-note">Live vehicle lookup is not available in this preview. Report availability, price and delivery for your own car are not offered here.</p></div></section>'
 s.select_one('#evidence').insert_before(frag(chooser))
 faq=s.select_one('#faqs')
 first=faq.select_one('details')
 if first:first.insert_before(frag('<details><summary>Can I check my own car here?<span aria-hidden="true">+</span></summary><p>This is a preview with ten fictional reports. Live vehicle lookup is not available. The examples do not confirm coverage for your car.</p></details>'))
 (D/'index.html').write_text(str(s))
