/* Decorative desktop companion. Original evidence remains beside its topic in HTML. */
(() => {
 'use strict';
 function chooseStep(rects,anchor){
  if(!rects.length)return -1;
  const found=rects.findIndex(rect=>anchor>=rect.top&&anchor<rect.bottom);
  if(found>=0)return found;
  return rects.reduce((best,rect,i)=>Math.abs((rect.top+rect.bottom)/2-anchor)<Math.abs((rects[best].top+rects[best].bottom)/2-anchor)?i:best,0);
 }
 if(typeof module!=='undefined')module.exports={chooseStep};
 if(typeof window==='undefined')return;
 window.VIBScrollStories={init(gsap,ScrollTrigger){
  const media=gsap.matchMedia();
  media.add('(min-width: 1024px) and (min-height: 720px)',()=>{
   const cleanups=[];
   document.querySelectorAll('#report-contents').forEach(story=>{
    const steps=[...story.querySelectorAll('.story-step')];
    if(!steps.length||steps.some(step=>!step.querySelector('.story-copy h3')||!step.querySelector('.evidence-card')))return;
    const stage=document.createElement('div');stage.className='story-stage';stage.setAttribute('aria-hidden','true');stage.inert=true;
    const stack=document.createElement('div');stack.className='card-stack';stage.append(stack);
    const panels=steps.map(step=>{
     const panel=step.querySelector('.evidence-card').cloneNode(true);panel.classList.add('stack-panel');
     panel.querySelectorAll('[id]').forEach(el=>el.removeAttribute('id'));stack.append(panel);return panel;
    });
    const progress=document.createElement('p');progress.className='story-progress';stage.append(progress);
    story.querySelector('.story-layout').append(stage);story.classList.add('story-enhanced');let current=-1;
    const select=()=>{
     // The card switches when the next text block reaches the same reading line as the sticky card.
     const index=chooseStep(steps.map(step=>step.querySelector('.story-copy').getBoundingClientRect()),innerHeight*.47);
     if(index===current)return;const first=current<0;current=index;story.dataset.activeStep=String(index);
     steps.forEach((step,i)=>step.classList.toggle('is-active',i===index));
     panels.forEach((panel,i)=>{
      gsap.killTweensOf(panel);panel.style.visibility=i===index?'visible':'hidden';
      if(i===index){
       gsap.set(panel,{opacity:1,y:0,rotation:0,scale:1});
       if(!first)gsap.fromTo(panel,{y:12,opacity:.78},{y:0,opacity:1,duration:.24,ease:'power2.out',overwrite:true});
      }
     });
     progress.textContent=`${String(index+1).padStart(2,'0')} / ${String(steps.length).padStart(2,'0')} · ${steps[index].querySelector('.story-copy h3').textContent}`;
    };
    select();
    const trigger=ScrollTrigger.create({trigger:story,start:'top bottom',end:'bottom top',onUpdate:select,onRefresh:select});
    cleanups.push(()=>{trigger.kill();panels.forEach(panel=>gsap.killTweensOf(panel));stage.remove();story.classList.remove('story-enhanced');delete story.dataset.activeStep;steps.forEach(step=>step.classList.remove('is-active'));});
   });
   return()=>cleanups.forEach(fn=>fn());
  });
  return()=>media.revert();
 }};
})();
