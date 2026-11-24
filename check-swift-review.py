"""Bounded Swift review: content integrity, gallery contract and dated scope preservation."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,hashlib
B=Path(__file__).resolve().parent;D=B/'dist'
c=next(c for c in json.loads((D/'cars.json').read_text())['cars'] if c['id']=='swift')
s=BeautifulSoup((D/'sample-swift.html').read_text(),'html.parser');text=s.get_text(' ',strip=True)
expected=['photos','mileage','ownership','finance','claims','challans','valuation','timeline']
assert [el['id'] for el in s.select('.photo-chapter,.swift-chapter')]==expected
assert len(s.select('.photo-thumb'))==len(c['photos'])==4
assert len(s.select('.service-invoices li'))==len(c['services'])==6
assert int(s.select_one('#reading-range')['max'])==len(c['services'])
assert len(s.select('.seller-prompt'))==7
assert int(s.select_one('.condition-value strong').text)==c['score']['value']
config=json.loads(s.select_one('#swift-report-data').string)
assert [r['km'] for r in config['readings']]==[r['km'] for r in c['services']]+[c['declaredKm']]
assert [p['src'] for p in config['photos']]==[p['src'] for p in c['photos']]
for p in c['photos']:assert hashlib.sha256((D/p['src']).read_bytes()).hexdigest()==p['sha256']
assert f'{c["services"][-1]["km"]-c["declaredKm"]:,} km lower' in text
for r in c['services']:assert r['id'] in text and f'{r["km"]:,} km' in text
for r in c['challans']:assert r['id'] in text and r['offence'] in text
assert c['claim']['part'] in text and '₹42,000' in text and '₹3,000' in text
assert '₹3.4–3.8' in text and '₹4,40,000' in text and '₹4,00,000' in text
assert len(s.select('noscript a'))==4
assert not s.select('.vehicle-picker,.car-files')
baseline=json.loads((B/'data/swift-review-baseline-2026-11-24.json').read_text())
allowed_changes={'cars.json','sample.html','index.html'}
for name,h in baseline.items():
 if name in allowed_changes:continue
 assert (D/name).is_file() and hashlib.sha256((D/name).read_bytes()).hexdigest()==h,f'Changed outside Swift scope: {name}'
print(f'PASS: Swift eight chapters, four original photos, six invoices, seven reading states, fixed financial/mileage facts and {len(baseline)-len(allowed_changes)} protected byte-identical existing non-Swift files.')
