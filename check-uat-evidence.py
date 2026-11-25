"""Validate the retained rendered UAT observations, not a replacement for running them."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent/'docs/uat/2026-11-25-all-reports'
frames=json.loads((P/'verified-cycle-states.json').read_text())
assert {s['case'] for s in frames if s['turning']=='false'}=={'swift','creta','brezza'}
assert all(len(s['faces'])<=1 for s in frames)
assert all('sample-'+s['case']+'.html' in s['href'] for s in frames)
assert all(s['inert'] for s in frames if s['turning']=='true')
assert all(f['gap']>0 for s in frames for f in s['faces'])
routes=json.loads((P/'route-gallery-checks.json').read_text());assert len(routes)==14
assert all(s['restored'] and not s['overflow'] and not s['broken'] for s in routes)
assert all(s['visibleDates'][-1]=='Nov 2026' for s in routes)
matrix=json.loads((P/'responsive-matrix.json').read_text());assert len(matrix)==36
assert all(not s['overflow'] and not s['broken'] for s in matrix)
interruptions=json.loads((P/'interruption-states.json').read_text());assert all(s['turning']=='false' and s['visible']==1 for s in interruptions)
print(f'PASS: retained UAT observations: {len(frames)} transition frames/3directions, 14 new-gallery journeys, 36 responsive route states, 3 interruption cases. See report for other manual checks and limits.')
