"""Content integrity across variable record counts and issue-led chapter orders."""
from pathlib import Path
from bs4 import BeautifulSoup as Soup
import json,hashlib,subprocess
from build_issue_reports import STORIES
from datetime import date
B=Path(__file__).resolve().parent;D=B/'dist';cars=json.loads((D/'cars.json').read_text())['cars']
old=json.loads(subprocess.check_output(['git','show','ae392bdf419e2da18f14eeb9284443aa3f0db830:dist/cars.json'],cwd=B));assert json.loads((D/'cars.json').read_text())==old
for c in cars:
 s=Soup((D/f'sample-{c["id"]}.html').read_text(),'html.parser');payload=json.loads(s.select_one('#swift-report-data').string);txt=s.get_text(' ',strip=True);n=len(c['services']);r=payload['readings']
 assert len(s.select('.photo-thumb'))==4 and len(s.select('.service-invoices li'))==n
 assert len(r)==n+1 and int(s.select_one('#reading-range')['max'])==n
 assert s.select_one('#journey-position').text==f'{n+1} of {n+1}'
 assert [p['src'] for p in payload['photos']]==[p['src'] for p in c['photos']]
 assert [(a['date'],a['km']) for a in r]==[(a['date'],a['km']) for a in c['services']]+[(c['sellerDate'],c['declaredKm'])]
 assert all(56<=a['x']<=650 and 25<=a['y']<=274 for a in r)
 assert c['reportId'] in txt and c['registration'] in txt and int(s.select_one('.condition-value strong').text)==c['score']['value']
 assert ('First owner' if c['owners']==1 else 'Second owner') in s.select_one('.cover-facts').get_text()
 ids=[e['id'] for e in s.select('.photo-chapter,.swift-chapter')];assert len(ids)==len(set(ids))==8
 assert [a['href'][1:] for a in s.select('.chapter-nav a')]==ids
 assert len(s.select('.seller-prompt'))==7
 assert len({a.get_text(' ',strip=True) for a in s.select('.priority-findings>a')})==3
 assert '1 owners recorded' not in txt
 if c['id'] in STORIES:
  story=STORIES[c['id']];assert ids[1]==story[1] and story[4] in s.select_one('#'+story[1]+' .seller-prompt').get_text()
  assert payload['vehicleName']==c['name']+' '+c['variant']
 if not c['claim']:assert 'No claim entry in available records' in txt and not s.select('.claim-feature') and 'Read the policy.' in s.select_one('#claims h2').text
 if c['id']=='venue':assert 'closure document is available' in txt.lower() and 'Closure proof is missing' not in txt and '14 Oct 2026' not in txt
 if c['id']=='i20':assert 'No service invoice after July 2024' in txt and 'Last service · 8 Jul 2024' in txt and r[-2]['km']==45300 and r[-1]['km']==81500
 if c['id']=='nexon':assert n==2 and '2021' not in s.select_one('.journey-years').text
 for p in c['photos']:assert hashlib.sha256((D/p['src']).read_bytes()).hexdigest()==p['sha256']
 dates=[t['datetime'] for t in s.select('.swift-timeline time')];assert dates==sorted(dates)
 assert '2025-02-12' not in dates and '2026-10-14' not in dates
 assert 'histories, amounts and outcomes are fictional' in txt and 'model-matched reference car' in txt
base=json.loads((B/'data/all-reports-baseline-2026-11-25.json').read_text());allowed={'motion.js','scroll-stories.js','guide.html','guide-mileage.html','guide-finance.html','guide-inspection.html','sample-router.js','index.html','sample.html','swift-report.css','swift-report.js','hero-deck.css','hero-deck.js',*('sample-'+c['id']+'.html' for c in cars)}
for file,h in base.items():
 if file not in allowed:assert hashlib.sha256((D/file).read_bytes()).hexdigest()==h,file
print('PASS: all ten reports; exact fixtures/photos/scores; own story/question; variable reading counts/date bounds; no invented transfer/closure dates; no-claim/closure/gap branches; protected assets and dataset.')
