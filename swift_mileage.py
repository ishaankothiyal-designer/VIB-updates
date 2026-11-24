"""Native, dated mileage journey. Smooth monotone service path; separate declaration event."""
from datetime import date
from html import escape

def smooth_path(points):
 """C1 monotone cubic Hermite interpolation, no overshoot between rising readings."""
 if len(points)<2:return ''
 h=[b[0]-a[0] for a,b in zip(points,points[1:])]
 slopes=[(b[1]-a[1])/dx for a,b,dx in zip(points,points[1:],h)]
 tangent=[slopes[0]]
 for i in range(1,len(points)-1):
  a,b=slopes[i-1],slopes[i]
  if a*b<=0:tangent.append(0)
  else:
   w1=2*h[i]+h[i-1];w2=h[i]+2*h[i-1]
   tangent.append((w1+w2)/(w1/a+w2/b))
 tangent.append(slopes[-1]);path=f'M{points[0][0]:.3f} {points[0][1]:.3f}'
 for i,((x0,y0),(x1,y1)) in enumerate(zip(points,points[1:])):
  dx=h[i]/3;path+=f'C{x0+dx:.3f} {y0+tangent[i]*dx:.3f} {x1-dx:.3f} {y1-tangent[i+1]*dx:.3f} {x1:.3f} {y1:.3f}'
 return path

def render_mileage(c):
 services=[dict(r,source='Service invoice') for r in c['services']]
 readings=services+[{'date':c['sellerDate'],'km':c['declaredKm'],'source':'Seller declaration'}]
 start=date.fromisoformat(readings[0]['date']);end=date.fromisoformat(readings[-1]['date']);duration=(end-start).days
 points=[]
 for i,r in enumerate(readings):
  x=56+594*(date.fromisoformat(r['date'])-start).days/duration;y=274-r['km']/80000*240
  r.update(x=round(x,3),y=round(y,3),displayDate=date.fromisoformat(r['date']).strftime('%-d %b %Y'))
  points.append((x,y))
 service_points=points[:-1];path=smooth_path(service_points);sx,sy=points[-2];dx,dy=points[-1];difference=services[-1]['km']-c['declaredKm']
 grid=''.join(f'<path d="M56 {274-v/80000*240:.1f}H650"/><text x="9" y="{279-v/80000*240:.1f}">{int(v/1000)}k</text>' for v in [0,20000,40000,60000,80000])
 years=''.join(f'<text x="{56+594*(date(y,7,8)-start).days/duration:.1f}" y="314">{y}</text>' for y in [2021,2023,2025])
 years+=f'<text x="{dx:.1f}" y="314" text-anchor="end">Nov 2026</text>'
 dots=''.join(f'<circle class="journey-dot" data-record-dot="{i}" cx="{x:.3f}" cy="{y:.3f}" r="4.5"/>' for i,(x,y) in enumerate(service_points))
 hits=''.join(f'<circle class="journey-hit" data-record-index="{i}" cx="{x:.3f}" cy="{y:.3f}" r="19"/>' for i,(x,y) in enumerate(points))
 graph=f'''<div class="mileage-experience" data-selected-kind="seller"><div class="journey-readout"><div><span id="journey-source">Seller declaration</span><time id="journey-date" datetime="{c['sellerDate']}">{readings[-1]['displayDate']}</time><div class="journey-odometer"><strong id="journey-km">{c['declaredKm']:,}</strong><span>km</span></div><p id="journey-insight">{difference:,} km below the last service record</p></div><img src="assets/odometer-study.webp" width="240" height="160" alt="" class="odometer-illustration"></div><div class="journey-plot"><svg viewBox="0 0 720 340" role="img" aria-labelledby="mileage-chart-title mileage-chart-desc"><title id="mileage-chart-title">Swift mileage — dated records</title><desc id="mileage-chart-desc">Six service readings vary in yearly distance, increasing from {services[0]['km']:,} km in 2021 to {services[-1]['km']:,} km in July 2026. The November seller declaration is {c['declaredKm']:,} km, {difference:,} km lower. The smooth line guides the eye between actual dated records; intermediate readings are not known.</desc><defs><linearGradient id="journey-area" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#739fb9" stop-opacity=".26"/><stop offset="100%" stop-color="#739fb9" stop-opacity=".015"/></linearGradient></defs><g class="journey-grid">{grid}</g><rect class="declaration-window" x="{sx:.3f}" y="30" width="{dx-sx+15:.3f}" height="244" rx="8"/><path class="journey-area" d="{path}V274H56Z"/><path class="swift-mileage-path journey-service-line" d="{path}"/><path class="last-reading-guide" d="M{sx:.3f} {sy:.3f}H680"/>{dots}<path class="seller-diamond" d="M{dx:.3f} {dy-6:.3f}l6 6-6 6-6-6Z"/><path class="difference-bracket" d="M674 {sy:.3f}h6V{dy:.3f}h-6"/><g class="journey-years">{years}</g><g class="journey-cursor"><line id="journey-crosshair" x1="{dx:.3f}" y1="26" x2="{dx:.3f}" y2="274"/><circle id="journey-halo" cx="{dx:.3f}" cy="{dy:.3f}" r="11"/><circle id="journey-focus" cx="{dx:.3f}" cy="{dy:.3f}" r="4.5"/></g><g aria-hidden="true">{hits}</g></svg></div><div class="journey-controls"><div class="journey-control-label"><label for="reading-range">Explore the dated readings</label><span id="journey-position">7 of 7</span></div><div class="journey-scrubber"><button type="button" id="reading-previous" aria-label="Previous mileage reading"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="m12 4-6 6 6 6"/></svg></button><input id="reading-range" type="range" min="0" max="6" step="1" value="6" aria-label="Mileage readings" aria-valuetext="{readings[-1]['displayDate']}, seller declaration, {c['declaredKm']:,} kilometres"><button type="button" id="reading-next" aria-label="Next mileage reading"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="m8 4 6 6-6 6"/></svg></button></div></div><div class="journey-key"><span><i></i>Service invoices</span><span><i></i>Seller declaration</span><span class="curve-note">Curve connects recorded points</span></div><div class="journey-comparison"><div><span>Last service · 8 Jul 2026</span><strong>{services[-1]['km']:,} <small>km</small></strong></div><div><span>Seller · 20 Nov 2026</span><strong>{c['declaredKm']:,} <small>km</small></strong></div><div class="journey-gap"><span>Difference to verify</span><strong>{difference:,} <small>km</small></strong></div></div><p class="journey-caution">The cause of the difference is not established.</p><p id="mileage-announcement" class="visually-hidden" aria-live="polite"></p></div>'''
 return graph,readings
