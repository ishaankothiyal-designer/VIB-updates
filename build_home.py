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
 steps='';panels=''
 for i,(heading,copy,mini,anchor) in enumerate(items):
  link_text={'ownership':'View registration records','mileage':'View mileage records','finance':'Review the lender entry','claims':'Review the repair record','challans':'Review challans and documents','valuation':'View the price context','photos':'View vehicle photos'}[anchor]
  steps+=f'<article class="story-step" id="{id}-{i+1}"><div class="story-copy"><h3>{heading}</h3><p>{copy}</p><a href="sample-swift.html#{anchor}" class="story-link">{link_text}</a></div><div class="inline-card">{mini}</div></article>'
  panels+=f'<div class="stack-panel" data-stack-index="{i}">{mini}</div>'
 return f'<section class="scroll-story {"story-reverse" if reverse else ""}" id="{id}"><div class="wrap"><div class="story-heading"><h2>{title}</h2><p>{description}</p></div><div class="story-layout"><div class="story-stage" aria-hidden="true"><div class="card-stack">{panels}</div></div><div class="story-steps">{steps}</div></div></div></section>'
def build_home():
 s=frag((B/'data/home-template-original.html').read_text())
 # Retain the approved chrome, FAQ, guides and contact sections, rebuilding only annotated sections.
 for sel in ['.hero-baseline','.car-files']:
  for el in s.select(sel):el.decompose()
 from hero_deck import render_hero_deck
 hero=s.select_one('.hero');hero.clear();hero.append(frag(render_hero_deck()))
 evidence=s.select_one('#evidence');evidence.clear();evidence.append(frag('''<div class="wrap mileage-story"><div class="mileage-intro"><h2>Let’s get into<br>the details of this Swift.</h2><p>A service invoice. A later mileage declaration. One difference worth checking.</p></div><div class="mileage-scene"><div class="scene-orbit" aria-hidden="true"></div><article class="service-receipt"><div class="receipt-top"><span>Service invoice</span><time datetime="2026-07-08">8 Jul 2026</time></div><span class="receipt-label">Odometer recorded</span><strong>72,000 <small>km</small></strong><div class="receipt-rule"></div><span class="receipt-foot">Maruti Suzuki Swift · 2020</span></article><div class="mileage-connection"><svg viewBox="0 0 240 110" aria-hidden="true"><path class="mileage-arc" d="M8 18 C100 12 104 94 225 86" fill="none"/><path d="m213 76 13 10-14 8" fill="none"/></svg><strong>14,000 <span>km lower</span></strong></div><article class="odometer-record"><div class="odometer-top"><span>Seller declaration</span><time datetime="2026-11-20">20 Nov 2026</time></div><p>The later reading</p><div class="odometer-digits" aria-label="58,000 kilometres"><span>0</span><span>5</span><span>8</span><span>0</span><span>0</span><span>0</span></div><div class="odometer-bottom"><span>km</span><span>Needs verification</span></div></article></div><div class="mileage-question"><div><span>Your next question</span><h3>“Can we compare the service invoice with the odometer?”</h3><p>Check the original documents and the seller’s explanation. The difference alone does not establish tampering.</p></div><a class="button ink" href="sample-swift.html#mileage">View this Swift’s report</a></div></div>'''))
 items=[
 ('Identity & ownership','Start with the basics. Do the registration details match the car and the person selling it?',card('Identity & ownership','Match the details.',asset('1b4dc.webp'),'<b>First owner</b><span>Registration valid to 7 Jul 2035</span>'),'ownership'),
 ('Service & mileage','Follow the dated readings. A later, lower declaration gives you a specific question to ask.',card('Service & mileage','Two dates. One discrepancy.','<div class="mini-reading"><span>8 Jul 2026<b>72,000<small> km</small></b></span><span>20 Nov 2026<b>58,000<small> km</small></b></span></div>','Ask to see the original service invoice.'),'mileage'),
 ('Finance & transfer','An active lender entry needs a follow-up. Ask for closure documents before discussing the transfer.',card('Finance & transfer','Ask for the closure letter.',asset('030ff.webp'),'<b>Lender entry active</b><span>Loan balance unavailable</span>'),'finance'),
 ('Insurance & repairs','A claim starts a conversation about the work. Read the invoice and inspect the repair.',card('Insurance & repairs','Understand the repair.',asset('43160.webp'),'<b>₹42,000 claim recorded</b><span>16 Aug 2023 · settled</span>'),'claims'),
 ('Challans & documents','Check unpaid entries and document dates. Verify the current status with the seller.',card('Challans & documents','Clear the open questions.','<div class="mini-challans"><span>Parking violation<b>₹1,000</b></span><span>Speeding violation<b>₹2,000</b></span></div>','<b>₹3,000 in unpaid entries</b><span>Check payment before transfer</span>'),'challans'),
 ('Price context','Put the asking price beside the history and the car’s condition. A range is a starting point.',card('Price context','Bring the records to the price.','<div class="mini-price">₹3.4–3.8<span>lakh · reference range</span></div>','An estimate, not an offer.'),'valuation')]
 s.select_one('#report-contents').replace_with(frag(story('report-contents','One car.<br>Read each part of its story.','The useful detail is in the records. Take them one at a time.',items)))
 process=[
 ('Follow the evidence.','Read the service invoice and seller declaration with their dates. Start with the difference you can see.',card('The finding','The readings conflict.','<div class="mini-reading"><span>Service invoice<b>72,000<small> km</small></b></span><span>Seller declaration<b>58,000<small> km</small></b></span></div>','Read each value with its date and source.'),'mileage'),
 ('Ask for the original.','Compare the original invoice, the vehicle details and the odometer. Ask the seller to explain the gap.',card('The document','Put the original beside it.',asset('b39dc.webp'),'“Can we check the service invoice together?”'),'mileage'),
 ('See the car today.','Use the history to focus an inspection and test drive. Check what the records cannot tell you.',card('The car today','History meets inspection.',asset('records-inspection.webp'),'Use the records. Inspect the car.'),'photos')]
 s.select_one('#process').replace_with(frag(story('process','A finding is the start.<br>Here’s what comes next.','From a record on the page to a question at the car.',process,True)))
 closing=s.select_one('.closing-file');closing.clear();closing.append(frag('''<div class="wrap closing-file-inner"><div><h2>See the paper trail.<br>Find your next question.</h2><p>Open a report. Read the history, look at the photos and see what needs checking.</p><a class="button gold" href="sample.html">View sample report</a></div><div class="closing-object"><div class="closing-object-under"></div><article class="closing-report"><span>Vehicle history report</span><img src="assets/report-folio.webp" alt="Blue ink illustration of a vehicle report folio and car key" width="900" height="600" loading="lazy"><div><h3>A closer look<br>starts here.</h3><span>Records. Photos. Next steps.</span></div></article></div></div>'''))
 # Correct all retained prototype framing in the reading sections.
 for node in list(s.find_all(string=True)):
  if node.parent.name in ['script','style']:continue
  t=str(node).replace('The sample’s 64/100 is an illustrative design value, not a calculated result. VIB’s condition-score methodology describes a relative prediction of physical condition. It is not a guarantee or a summary of every legal and financial record.','A condition score describes predicted physical condition. Read it with the supporting records and an inspection. Sample scores are preset for this preview; legal and financial findings are shown separately.').replace('What does the sample score mean?','How should I read a condition score?')
  if t!=str(node):node.replace_with(t)
 for el in s.select('link[href="home.css"]'):pass
 s.head.append(frag('<link href="minimal-home.css" rel="stylesheet"><link href="hero-deck.css" rel="stylesheet"><script src="hero-deck.js" defer></script>'))
 # Scroll story functions load before the existing preference-aware motion owner.
 motion=s.select_one('script[src="motion.js"]');motion.insert_before(frag('<script src="scroll-stories.js" defer></script>'));s.select_one('script[src="hero-deck.js"]').extract();motion.insert_after(frag('<script src="hero-deck.js" defer></script>'))
 s.select_one('meta[name=description]')['content']='Read a car’s history one record at a time. Explore a VIB sample report with photographs, dated records and the questions to ask.'
 (D/'index.html').write_text(str(s))
