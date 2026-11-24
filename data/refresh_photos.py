"""Refresh source photographs only; preserve authored mock histories and event dates."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,re,json,io,hashlib
from datetime import date
from PIL import Image
B=Path(__file__).resolve().parents[1];D=B/'dist';path=D/'cars.json';data=json.loads(path.read_text())
def refresh(c):
 url=c['photos'][0]['sourceListing'];html=requests.get(url,timeout=40).text.replace('\\"','"').replace('\\/','/')
 candidates=re.findall(r'"label":"([^"\n]+)","category":"([^"\n]+)","image":"(https://media.cars24.com/[^"\n]+)"',html)
 for p in c['photos']:
  found=next((x for x in candidates if x[0]==p['view'] and 'gpt' not in x[2].lower()),None)
  if not found:continue
  r=requests.get(found[2],timeout=40);r.raise_for_status();im=Image.open(io.BytesIO(r.content)).convert('RGB');im.thumbnail((1200,900));out=D/p['src'];im.save(out,'WEBP',quality=84)
  p.update(sourceUrl=found[2],retrievedOn=date.today().isoformat(),sha256=hashlib.sha256(out.read_bytes()).hexdigest())
 return c
with ThreadPoolExecutor(max_workers=5) as pool:data['cars']=list(pool.map(refresh,data['cars']))
path.write_text(json.dumps(data,indent=2));print('Photograph sources refreshed; mock histories preserved. Run build_reports.py next.')
