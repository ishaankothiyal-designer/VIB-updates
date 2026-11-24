from pathlib import Path
from bs4 import BeautifulSoup as Soup
import json,hashlib
B=Path(__file__).resolve().parent;D=B/'dist';cars=json.loads((D/'cars.json').read_text())['cars']
for id in ['creta','brezza']:
 c=next(c for c in cars if c['id']==id);s=Soup((D/f'sample-{id}.html').read_text(),'html.parser');txt=s.get_text(' ',strip=True)
 order=['photos','finance','mileage','ownership','claims','challans','valuation','timeline'] if id=='creta' else ['photos','challans','ownership','mileage','finance','claims','valuation','timeline']
 assert [r['id'] for r in s.select('.photo-chapter,.swift-chapter')]==order
 assert [a['href'][1:] for a in s.select('.chapter-nav a')]==order
 assert len(s.select('.photo-thumb'))==4 and len(s.select('.service-invoices li'))==6
 payload=json.loads(s.select_one('#swift-report-data').string)
 assert payload['vehicleName']==c['name']+' '+c['variant']
 assert [p['src'] for p in payload['photos']]==[p['src'] for p in c['photos']]
 assert [r['km'] for r in payload['readings']]==[r['km'] for r in c['services']]+[c['declaredKm']]
 assert all(25<=r['y']<=274 for r in payload['readings'])
 assert c['reportId'] in txt and c['registration'] in txt
 assert 'Maruti Suzuki Swift LXI' not in str(s)
 assert 'km below' not in txt
 assert len(s.select('.seller-prompt'))==7
 assert int(s.select_one('.condition-value strong').text)==c['score']['value']
 assert ('Closure documents' in txt and '₹96,000' in txt) if id=='creta' else ('CH-08-001' in txt and '₹1,500' in txt and 'Recorded validity has ended' in txt)
 for p in c['photos']:assert hashlib.sha256((D/p['src']).read_bytes()).hexdigest()==p['sha256']
 s.select_one('#photo-viewer')
home=Soup((D/'index.html').read_text(),'html.parser');assert not home.select('.case-selector,.case-selectors')
assert home.select_one('.case-deck-footer #case-report-action') and home.select_one('.case-pause') and home.select_one('.case-next')
allowed={'index.html','sample-creta.html','sample-brezza.html','sample-swift.html','sample.html','swift-report.css','swift-report.js','hero-deck.css','hero-deck.js'}
base=json.loads((B/'data/issue-reports-baseline-2026-11-25.json').read_text())
for file,h in base.items():
 if file not in allowed:assert hashlib.sha256((D/file).read_bytes()).hexdigest()==h,file
print('PASS: two issue-led eight-chapter reports; exact fixture readings/owners/scores; original photos; own gallery names; no false mileage rollback; hero action below deck/no tabs; protected routes and dataset unchanged.')
