/* The existing motion owner calls this only when full motion is allowed. */
window.VIBScrollStories={init(gsap,ScrollTrigger,context){
 const stories=[...document.querySelectorAll('.scroll-story')];
 stories.forEach(story=>{
  const steps=[...story.querySelectorAll('.story-step')];const panels=[...story.querySelectorAll('.stack-panel')];let current=-1;
  story.classList.add('story-enhanced');
  const select=index=>{if(current===index)return;const initial=current<0;const previous=current;current=index;story.dataset.activeStep=String(index);
   steps.forEach((step,i)=>step.classList.toggle('is-active',i===index));
   context.add(()=>panels.forEach((panel,i)=>{
    gsap.killTweensOf(panel);const depth=index-i;const pose={y:depth===0?0:-Math.min(depth,3)*9,rotation:depth===0?0:-Math.min(depth,3)*1.3,scale:1-Math.min(Math.max(depth,0),3)*.025,zIndex:i+1};
    if(i>index||depth>3){gsap.set(panel,{autoAlpha:0,y:34,rotation:3,scale:.98,zIndex:i+1});return;}
    gsap.set(panel,{autoAlpha:1});
    if(initial){gsap.set(panel,pose);return;}
    if(i===index){gsap.fromTo(panel,{y:previous<index?28:8,rotation:previous<index?2:0,scale:.985},{...pose,duration:.58,ease:'power2.out',overwrite:'auto'});}
    else gsap.to(panel,{...pose,duration:.58,ease:'power2.out',overwrite:'auto'});
   }));
  };
  select(0);
  steps.forEach((step,i)=>ScrollTrigger.create({trigger:step,start:()=>innerWidth<768?'top 72%':'top 62%',end:()=>innerWidth<768?'bottom 72%':'bottom 62%',onEnter:()=>select(i),onEnterBack:()=>select(i)}));
 });
 const hero=document.querySelector('.hero-visual');if(hero){const cards=hero.querySelectorAll('.hero-record,.hero-finding');gsap.from(cards,{y:22,rotation:0,opacity:.7,stagger:.12,duration:.58,ease:'power2.out',clearProps:'transform,opacity'});}
 const scene=document.querySelector('.mileage-scene');if(scene){gsap.from(scene.querySelectorAll('.service-receipt,.odometer-record'),{scrollTrigger:{trigger:scene,start:'top 82%',once:true},y:20,opacity:.65,stagger:.15,duration:.58,ease:'power2.out',clearProps:'transform,opacity'});const arc=scene.querySelector('.mileage-arc');if(arc){const len=arc.getTotalLength();gsap.fromTo(arc,{strokeDasharray:len,strokeDashoffset:len},{strokeDashoffset:0,duration:.65,ease:'power2.out',scrollTrigger:{trigger:scene,start:'top 75%',once:true},clearProps:'strokeDasharray,strokeDashoffset'});}}
 const close=document.querySelector('.closing-report');if(close)gsap.from(close,{scrollTrigger:{trigger:close,start:'top 90%',once:true},y:24,rotation:0,duration:.58,ease:'power2.out',clearProps:'transform'});
 return ()=>stories.forEach(story=>{story.classList.remove('story-enhanced');delete story.dataset.activeStep;story.querySelectorAll('.story-step').forEach(step=>step.classList.remove('is-active'));});
}};
