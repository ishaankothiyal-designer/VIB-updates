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
 cards=''
 for i,item in enumerate(cases):
  c=by_id[item['id']];url=f'sample-{c["id"]}.html#{item["anchor"]}';item['url']=url;item['name']=c['name']
  cards+=f'''<article class="case-card" data-case="{i}"><div class="case-front"><div class="case-kicker"><span>Vehicle history</span><span>0{i+1} / {item['short']}</span></div><img class="case-art" src="assets/{item['image']}" width="900" height="600" alt="Blue ink illustration of a {c['year']} {esc(c['name'])} with archive papers"><div class="case-identity"><h2>{esc(c['name'])}</h2><p>{c['year']} · {esc(c['fuel'])} · {esc(c['transmission'])}</p></div><div class="case-finding"><span>{item['label']}</span><strong>{item['value']} <small>{item['unit']}</small></strong></div><div class="case-mobile-detail"><p>{item['copy']}</p><noscript><a href="{url}">View {item['short']}’s report</a></noscript></div></div><div class="case-back" aria-hidden="true"><span>VIB</span><i></i><small>Vehicle history</small></div></article>'''

 first=cases[0]
 html=f'''<div class="hero-stage"><div class="wrap minimal-hero case-hero-layout"><div class="hero-copy"><p class="eyebrow">THE CAR’S PAPER TRAIL</p><h1>A car’s past.<br>In black <br>and <em>white.</em></h1><p class="hero-intro">Follow the service, ownership and finance records. See what needs checking before you buy.</p></div><div class="case-deck-region" role="region" aria-roledescription="carousel" aria-label="Three vehicle record examples"><div class="case-deck">{cards}</div><div class="case-deck-footer"><a id="case-report-action" class="button gold" href="{first['url']}">View Swift’s report</a><div class="case-playback"><span class="case-position" aria-hidden="true">01 / 03</span><button type="button" class="case-pause" aria-label="Pause car animation"><svg class="pause-icon" viewBox="0 0 20 20" aria-hidden="true"><path d="M7 5v10M13 5v10"/></svg><svg class="play-icon" viewBox="0 0 20 20" aria-hidden="true"><path d="m7 5 8 5-8 5Z"/></svg></button><button type="button" class="case-next" aria-label="Show next car"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="m7 5 5 5-5 5"/></svg></button></div></div><div class="case-progress" aria-hidden="true"><span></span></div><p class="visually-hidden" id="case-announcement" aria-live="polite"></p></div></div></div><script id="hero-case-data" type="application/json">{json.dumps(cases,ensure_ascii=False)}</script><noscript><style>.case-playback,.case-progress,#case-report-action{{display:none}}.case-mobile-detail{{display:block!important}}</style></noscript>'''
 return html
