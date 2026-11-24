"""Three sourced mock case stories, composed as a reversible paper-card deck."""
import json
from pathlib import Path
from html import escape as esc
B=Path(__file__).resolve().parent

def render_hero_deck():
 cars=json.loads((B/'dist/cars.json').read_text())['cars'];by_id={c['id']:c for c in cars}
 cases=[
 {'id':'swift','category':'Mileage','title':'This Swift has two different readings.','copy':'The last service invoice says 72,000 km. The seller declares 58,000 km. Ask to compare the original documents.','label':'Mileage to verify','value':'14,000','unit':'km','image':'swift-archive.webp','anchor':'mileage','short':'Swift'},
 {'id':'creta','category':'Finance','title':'This Creta needs a lender follow-up.','copy':'The lender entry is active and closure documents have not been provided. Check both before arranging a transfer.','label':'Lender entry','value':'Active','unit':'','image':'creta-archive.webp','anchor':'finance','short':'Creta'},
 {'id':'brezza','category':'Challans','title':'This Brezza has an unpaid entry.','copy':'An unpaid challan totals ₹1,500 in the records. Verify the current payment status with the seller.','label':'Unpaid challan','value':'₹1,500','unit':'','image':'brezza-archive.webp','anchor':'challans','short':'Brezza'}]
 # Facts are checked against the same report fixtures rather than invented for the animation.
 assert by_id['swift']['services'][-1]['km']-by_id['swift']['declaredKm']==14000
 assert by_id['creta']['lenderActive'] and not by_id['creta']['closureDocument']
 assert sum(r['amount'] for r in by_id['brezza']['challans'])==1500
 cards='';controls=''
 for i,item in enumerate(cases):
  c=by_id[item['id']];url=f'sample-{c["id"]}.html#{item["anchor"]}';item['url']=url;item['name']=c['name']
  cards+=f'''<article class="case-card" data-case="{i}"><div class="case-front"><div class="case-kicker"><span>Vehicle history</span><span>0{i+1} / {item['short']}</span></div><img class="case-art" src="assets/{item['image']}" width="900" height="600" alt="Blue ink illustration of a {c['year']} {esc(c['name'])} with archive papers"><div class="case-identity"><h2>{esc(c['name'])}</h2><p>{c['year']} · {esc(c['fuel'])} · {esc(c['transmission'])}</p></div><div class="case-finding"><span>{item['label']}</span><strong>{item['value']} <small>{item['unit']}</small></strong></div><div class="case-mobile-detail"><p>{item['copy']}</p><a href="{url}">Read this {item['short']}’s report</a></div></div><div class="case-back" aria-hidden="true"><span>VIB</span><i></i><small>Vehicle history</small></div></article>'''
  controls+=f'<button type="button" class="case-selector" data-select-case="{i}" aria-label="Show {item["short"]} {item["category"].lower()} example" aria-pressed="{str(i==0).lower()}"><span>0{i+1}</span>{item["short"]}</button>'
 first=cases[0]
 html=f'''<div class="hero-stage"><div class="wrap minimal-hero case-hero-layout"><div class="hero-copy"><p class="eyebrow">THE CAR’S PAPER TRAIL</p><h1>A car’s past.<br>In black <br>and <em>white.</em></h1><div class="hero-case-copy"><p id="case-category">01 / Mileage</p><h2 id="case-title">{first['title']}</h2><p id="case-description">{first['copy']}</p></div><a id="case-report-action" class="button gold" href="{first['url']}">View this Swift’s report</a></div><div class="case-deck-region" role="region" aria-roledescription="carousel" aria-label="Three vehicle record examples"><div class="case-deck">{cards}</div><div class="case-selectors" role="group" aria-label="Choose a vehicle example">{controls}</div><p class="case-scroll-hint">Scroll to turn the next file</p><p class="visually-hidden" id="case-announcement" aria-live="polite"></p></div></div></div><script id="hero-case-data" type="application/json">{json.dumps(cases,ensure_ascii=False)}</script><noscript><style>.case-selectors,.case-scroll-hint{{display:none}}.case-mobile-detail{{display:block!important}}</style></noscript>'''
 return html
