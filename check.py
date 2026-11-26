"""Check local site resources, fragment/ARIA targets and preserved V4 source."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,re
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
DIST=BASE/'dist'
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.path=path;self.ids=[];self.links=[];self.controls=[];self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  self.links.extend(a[k]for k in ('href','src')if k in a)
  self.controls.extend(a.get('aria-controls','').split())
pages={p:Page(p)for p in DIST.glob('*.html')}
for path,page in pages.items():
 assert len(page.ids)==len(set(page.ids)),f'Duplicate IDs: {path.name}'
 for target in page.controls:assert target in page.ids,f'ARIA target missing: {target}'
 for ref in page.links:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  dst=DIST/unquote(u.path)if u.path else path
  assert dst.is_file(),f'Missing local resource: {path.name}: {ref}'
  if u.fragment:assert u.fragment in pages.get(dst,Page(dst)).ids,f'Missing fragment: {ref}'
for path in DIST.glob('*.css'):
 for value in re.findall(r'url\([\"\']?([^\)\"\']+)',path.read_text()):
  if not value.startswith(('data:','http:','https:','#')):assert (DIST/value).is_file(),f'Missing CSS asset: {value}'
for _,_,image,_ in json.loads((DIST/'guides.json').read_text()).values():assert (DIST/'assets'/image).is_file(),image
# V4 belongs to the original multi-site workspace, not this standalone repository.
# Validate it only when its actual source directory is explicitly supplied.
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--v4-root',type=Path)
args=parser.parse_args()
if args.v4_root is not None:
 assert args.v4_root.is_dir(), 'Provided V4 source directory does not exist'
 preserved=json.loads((BASE/'v4-baseline-hashes.json').read_text())
 actual={str(p.relative_to(args.v4_root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in args.v4_root.rglob('*') if p.is_file()}
 assert actual==preserved,'V4 source differs from pre-V5 baseline'
 print(f'PASS: {len(preserved)} V4 files at explicit --v4-root')
print(f'PASS: {len(pages)} HTML routes, local resources, fragment/ARIA targets and CSS assets.')
