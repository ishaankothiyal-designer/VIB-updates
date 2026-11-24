/* Swift-only gallery, reading explorer and preference-aware evidence arrival. */
(()=>{
 'use strict';const config=JSON.parse(document.getElementById('swift-report-data').textContent);
 const photos=config.photos;let selected=0;let returnFocus=null;
 const main=document.getElementById('selected-photo'),caption=document.getElementById('selected-photo-caption'),count=document.getElementById('selected-photo-count'),open=document.querySelector('.gallery-open'),thumbs=[...document.querySelectorAll('.photo-thumb')];
 const dialog=document.getElementById('photo-viewer'),viewer=document.getElementById('viewer-photo');
 const friendly=photo=>'Maruti Suzuki Swift LXI — '+photo.label.toLowerCase()+' view';
 function selectPhoto(index){selected=(index+photos.length)%photos.length;const photo=photos[selected];main.src=photo.src;main.alt=friendly(photo);caption.textContent=photo.label;count.textContent=(selected+1)+' of '+photos.length;open.setAttribute('aria-label','Open '+photo.label.toLowerCase()+' photo in full screen');thumbs.forEach((button,i)=>button.setAttribute('aria-pressed',String(i===selected)));if(dialog.open)updateViewer();}
 function updateViewer(){const photo=photos[selected];viewer.src=photo.src;viewer.alt=friendly(photo);document.getElementById('viewer-caption').textContent=photo.label;document.getElementById('viewer-position').textContent=(selected+1)+' of '+photos.length;}
 thumbs.forEach((button,i)=>{button.addEventListener('click',()=>selectPhoto(i));button.addEventListener('keydown',event=>{let next;if(event.key==='ArrowRight')next=(i+1)%photos.length;else if(event.key==='ArrowLeft')next=(i+photos.length-1)%photos.length;else if(event.key==='Home')next=0;else if(event.key==='End')next=photos.length-1;if(next!==undefined){event.preventDefault();selectPhoto(next);thumbs[next].focus();}});});
 open.addEventListener('click',()=>{returnFocus=document.activeElement;updateViewer();dialog.showModal();document.body.classList.add('photo-viewer-open');dialog.querySelector('.viewer-close').focus();});
 dialog.querySelector('.viewer-close').addEventListener('click',()=>dialog.close());
 dialog.querySelector('.viewer-previous').addEventListener('click',()=>selectPhoto(selected-1));
 dialog.querySelector('.viewer-next').addEventListener('click',()=>selectPhoto(selected+1));
 dialog.addEventListener('keydown',event=>{if(event.key==='Tab'){const first=dialog.querySelector('.viewer-close'),last=dialog.querySelector('.viewer-next');if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}}if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();selectPhoto(selected+(event.key==='ArrowRight'?1:-1));}});
 dialog.addEventListener('click',event=>{if(event.target===dialog){const b=dialog.getBoundingClientRect();if(event.clientX<b.left||event.clientX>b.right||event.clientY<b.top||event.clientY>b.bottom)dialog.close();}});
 dialog.addEventListener('close',()=>{document.body.classList.remove('photo-viewer-open');returnFocus?.focus({preventScroll:true});});
 const range=document.getElementById('reading-range'),experience=document.querySelector('.mileage-experience'),plot=document.querySelector('.journey-plot');let readingIndex=config.readings.length-1;
 const number=document.getElementById('journey-km');
 function selectReading(index,announce=false){
  index=Math.max(0,Math.min(config.readings.length-1,index));const changed=index!==readingIndex;readingIndex=index;const r=config.readings[index],last=config.readings[config.readings.length-2];const seller=index===config.readings.length-1;
  range.value=String(index);experience.dataset.selectedKind=seller?'seller':'service';
  document.getElementById('journey-source').textContent=r.source;const when=document.getElementById('journey-date');when.textContent=r.displayDate;when.dateTime=r.date;
  number.textContent=r.km.toLocaleString('en-IN');document.getElementById('journey-position').textContent=(index+1)+' of '+config.readings.length;
  document.getElementById('journey-insight').textContent=seller?(last.km-r.km).toLocaleString('en-IN')+' km below the last service record':index===0?'First available service invoice':(r.km-config.readings[index-1].km).toLocaleString('en-IN')+' km since the previous invoice';
  const spoken=r.displayDate+', '+r.source+', '+r.km.toLocaleString('en-IN')+' kilometres';range.setAttribute('aria-valuetext',spoken);if(announce)document.getElementById('mileage-announcement').textContent=spoken;
  document.getElementById('reading-previous').disabled=index===0;document.getElementById('reading-next').disabled=index===config.readings.length-1;
  const line=document.getElementById('journey-crosshair'),halo=document.getElementById('journey-halo'),focus=document.getElementById('journey-focus');
  const smooth=window.gsap&&document.documentElement.dataset.motion!=='reduced';
  if(smooth){window.gsap.to(line,{attr:{x1:r.x,x2:r.x},duration:.22,ease:'power2.out',overwrite:true});window.gsap.to([halo,focus],{attr:{cx:r.x,cy:r.y},duration:.22,ease:'power2.out',overwrite:true});if(changed)window.gsap.fromTo(number,{y:4,opacity:.7},{y:0,opacity:1,duration:.22,ease:'power2.out',clearProps:'transform,opacity',overwrite:true});}
  else{window.gsap?.killTweensOf([line,halo,focus,number]);number.style.removeProperty('transform');number.style.removeProperty('opacity');line.setAttribute('x1',r.x);line.setAttribute('x2',r.x);[halo,focus].forEach(point=>{point.setAttribute('cx',r.x);point.setAttribute('cy',r.y);});}
 }
 range.addEventListener('input',()=>selectReading(Number(range.value),true));document.getElementById('reading-previous').addEventListener('click',()=>selectReading(readingIndex-1,true));document.getElementById('reading-next').addEventListener('click',()=>selectReading(readingIndex+1,true));
 const nearest=event=>{const box=plot.querySelector('svg').getBoundingClientRect();const x=(event.clientX-box.left)/box.width*720;let best=0;config.readings.forEach((r,i)=>{if(Math.abs(r.x-x)<Math.abs(config.readings[best].x-x))best=i;});return best;};
 plot.addEventListener('pointermove',event=>{if(event.pointerType==='mouse')selectReading(nearest(event));});plot.addEventListener('click',event=>selectReading(nearest(event),true));selectReading(readingIndex);
 new MutationObserver(()=>selectReading(readingIndex)).observe(document.documentElement,{attributes:true,attributeFilter:['data-motion']});
 document.querySelector('.chapter-menu')?.addEventListener('click',event=>{if(event.target.closest('a'))event.currentTarget.open=false;});
 const printExpanded=[];window.addEventListener('beforeprint',()=>{document.querySelectorAll('.service-invoices,.record-disclosure').forEach(detail=>{if(!detail.open){printExpanded.push(detail);detail.open=true;}});});window.addEventListener('afterprint',()=>{printExpanded.splice(0).forEach(detail=>detail.open=false);});
 // Keep chapter progress separate from motion so navigation works with reduced motion.
 const chapterLinks=[...document.querySelectorAll('.chapter-nav a')];const chapterObserver=new IntersectionObserver(entries=>{entries.filter(entry=>entry.isIntersecting).forEach(entry=>{chapterLinks.forEach(a=>{if(a.getAttribute('href')==='#'+entry.target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});});},{rootMargin:'-15% 0px -55% 0px',threshold:0});document.querySelectorAll('.swift-chapter,.photo-chapter').forEach(section=>chapterObserver.observe(section));
 if(!window.gsap||!window.ScrollTrigger)return;
 const gsap=window.gsap;const media=gsap.matchMedia();media.add({reduced:'(prefers-reduced-motion: reduce)',desktop:'(min-width:768px)',mobile:'(max-width:767px)'},context=>{if(context.conditions.reduced||document.documentElement.dataset.motion==='reduced')return;
  document.querySelectorAll('[data-swift-reveal]').forEach(surface=>gsap.from(surface,{scrollTrigger:{trigger:surface,start:'top 92%',once:true},y:10,opacity:.82,duration:.4,ease:'power2.out',clearProps:'transform,opacity'}));
  const path=document.querySelector('.swift-mileage-path');if(path){const length=path.getTotalLength();gsap.fromTo(path,{strokeDasharray:length,strokeDashoffset:length},{scrollTrigger:{trigger:path.closest('figure'),start:'top 90%',once:true},strokeDashoffset:0,duration:.65,ease:'power2.out',clearProps:'strokeDasharray,strokeDashoffset'});}
 });
})();
