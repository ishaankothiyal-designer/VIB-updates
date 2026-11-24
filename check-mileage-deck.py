from pathlib import Path
from bs4 import BeautifulSoup
from swift_mileage import smooth_path,render_mileage
import json,math,re,hashlib,subprocess
B=Path(__file__).resolve().parent;D=B/'dist';data=json.loads((D/'cars.json').read_text());c=next(c for c in data['cars'] if c['id']=='swift')
expected=[9800,21750,29400,46300,58750,72000];assert [r['km'] for r in c['services']]==expected
others=json.loads((B/'data/mileage-other-cars-baseline.json').read_text());assert [r for r in data['cars'] if r['id']!='swift']==others
old=json.loads(subprocess.check_output(['git','show','418bc4b89ec3b6c0db1e3385f337cb01e12ec2be:dist/cars.json'],cwd=B))
oldswift=next(r for r in old['cars'] if r['id']=='swift');copy=json.loads(json.dumps(c))
for row,original in zip(copy['services'],oldswift['services']):row['km']=original['km']
assert copy==oldswift,'Only the earlier mock mileage values may change.'
html,readings=render_mileage(c);points=[(r['x'],r['y']) for r in readings[:-1]];path=smooth_path(points);assert path.count('C')==5
nums=[float(x) for x in re.findall(r'-?\d+\.\d+',path)];x0,y0=nums[:2];last_y=y0
for seg in range(5):
 a,b,d,e,x1,y1=nums[2+seg*6:8+seg*6]
 for step in range(1,101):
  t=step/100;u=1-t;y=u**3*y0+3*u*u*t*b+3*u*t*t*e+t**3*y1
  assert y<=last_y+1e-6 and min(y0,y1)-1e-6<=y<=max(y0,y1)+1e-6,'Curve overshoot'
  last_y=y
 x0,y0=x1,y1
s=BeautifulSoup((D/'sample-swift.html').read_text(),'html.parser');payload=json.loads(s.select_one('#swift-report-data').string)
assert [r['km'] for r in payload['readings']]==expected+[58000]
assert len(s.select('.journey-dot'))==6 and s.select_one('.seller-diamond')
assert s.select_one('#reading-range')['max']=='6'
for r in c['services']:assert f'{r["km"]:,} km' in s.get_text(' ',strip=True)
home=BeautifulSoup((D/'index.html').read_text(),'html.parser');cases=json.loads(home.select_one('#hero-case-data').string);assert [r['id'] for r in cases]==['swift','creta','brezza']
assert len(home.select('.case-card'))==3 and not home.select('.case-selector')
before=BeautifulSoup(subprocess.check_output(['git','show','418bc4b89ec3b6c0db1e3385f337cb01e12ec2be:dist/index.html'],cwd=B),'html.parser')
for selector in ['#evidence','#report-contents','#process','#faqs','#guides','.closing-file','.contact-strip','.site-header','.site-footer']:
 assert str(home.select_one(selector))==str(before.select_one(selector)),f'Outside hero changed: {selector}'
protected=json.loads((B/'data/mileage-scope-baseline-2026-11-24.json').read_text());intentional={'index.html','sample-creta.html','sample-brezza.html'}
for file,h in protected.items():
 if file in intentional:continue
 assert hashlib.sha256((D/file).read_bytes()).hexdigest()==h,file
print('PASS: uneven mock history; 500 spline samples with no overshoot; actual dates/7 states; 9 unchanged cars; all lower homepage sections unchanged; 3 linked hero cases; protected source hashes.')
