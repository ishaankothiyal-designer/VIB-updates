"""Check records across the report story, derived totals and photograph provenance."""
from pathlib import Path
from datetime import date
import json,hashlib
from bs4 import BeautifulSoup
B=Path(__file__).resolve().parent;D=B/'dist';data=json.loads((D/'cars.json').read_text());cars=data['cars'];assert len(cars)==10
assert len({c['id'] for c in cars})==10
assert len(data['homepageIds'])==5
for c in cars:
 s=BeautifulSoup((D/f'sample-{c["id"]}.html').read_text(),'html.parser');text=s.get_text(' ',strip=True)
 assert c['name'] in s.h1.text
 assert len(s.select('.photo-open'))==len(c['photos'])==4
 assert len(s.select('.report-section:not(.gaps)'))==8
 assert not s.select('.vehicle-picker')
 assert c['score']['mode']=='preset-sample' and 0<=c['score']['value']<=100
 assert not any(x in text.lower() for x in ['illustrative','synthetic','sample lender','dummy'])
 for r in c['services']:
  assert c['registeredOn']<=r['date']<=c['reportDate']
  assert f'{r["km"]:,} km' in text
 assert all(a['km']<=b['km'] for a,b in zip(c['services'],c['services'][1:]))
 if c['claim']:assert c['registeredOn']<=c['claim']['date']<=c['reportDate']
 for p in c['photos']:
  assert p['sourceListing'].endswith(c['sourceListingId']+'/')
  assert p['isReferencePhoto'] and p['relatedRecordId'] is None
  assert hashlib.sha256((D/p['src']).read_bytes()).hexdigest()==p['sha256']
 if c['challans']:assert f'₹{sum(r["amount"] for r in c["challans"]):,}' in text
home=BeautifulSoup((D/'index.html').read_text(),'html.parser')
assert not home.select('.car-file,.car-files,.hero-baseline')
assert len(home.select('#report-contents .story-step'))==6 and len(home.select('#process .story-step'))==3
assert 'illustrative' not in str(home).lower()
assert cars[0]['claim']['date']=='2023-08-16' and sum(x['amount'] for x in cars[0]['challans'])==3000
print('PASS: 10 distinct car histories; 40 matched photo hashes; dates, mileage, chapter/hidden-dataset counts, challan totals and homepage consistency.')
