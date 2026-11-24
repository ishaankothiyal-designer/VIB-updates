/* Three files, three questions. Scroll-led on spacious desktop, manual everywhere. */
(()=>{
 'use strict';const payload=document.getElementById('hero-case-data');if(!payload)return;
 const cases=JSON.parse(payload.textContent),hero=document.querySelector('.hero'),region=document.querySelector('.case-deck-region'),cards=[...document.querySelectorAll('.case-card')],buttons=[...document.querySelectorAll('.case-selector')];let current=0,turn=null,scroll=null,sequence=0,lockedCase=null,lockTimer=0;
 const reduced=()=>document.documentElement.dataset.motion==='reduced'||matchMedia('(prefers-reduced-motion: reduce)').matches;
 const G=window.gsap;region.classList.add('deck-enhanced');
 function arrange(index){cards.forEach((card,i)=>{const depth=(i-index+cards.length)%cards.length;const pose={x:0,y:depth?-depth*9:0,z:depth?-depth*18:1,rotationY:0,rotationZ:reduced()?0:depth?(depth===1?-4:4):1.3,scale:1-depth*.025,zIndex:cards.length-depth,autoAlpha:1};if(G)G.set(card,pose);else{card.style.visibility=i===index?'visible':'hidden';card.style.zIndex=String(pose.zIndex);}card.classList.toggle('is-current',i===index);card.setAttribute('aria-hidden',String(i!==index));card.inert=i!==index;});}
 function updateCopy(index,announce){const c=cases[index];document.getElementById('case-category').textContent='0'+(index+1)+' / '+c.category;document.getElementById('case-title').textContent=c.title;document.getElementById('case-description').textContent=c.copy;const link=document.getElementById('case-report-action');link.href=c.url;link.textContent='View this '+c.short+'’s report';buttons.forEach((b,i)=>b.setAttribute('aria-pressed',String(i===index)));region.dataset.activeCase=c.id;if(announce)document.getElementById('case-announcement').textContent=c.name+'. '+c.title;}
 function select(index,animate=true,announce=false){index=Math.max(0,Math.min(cases.length-1,index));if(index===current){updateCopy(index,announce);return;}const old=current;current=index;sequence++;const run=sequence;turn?.kill();if(G)G.killTweensOf(cards);arrange(old);updateCopy(index,announce);
  cards.forEach((card,i)=>{card.classList.toggle('is-current',i===index);card.setAttribute('aria-hidden',String(i!==index));card.inert=i!==index;});
  if(!G||reduced()||!animate){arrange(index);return;}
  G.set(cards[index],{x:26,y:7,z:70,rotationY:88,rotationZ:1.3,scale:.985,autoAlpha:1,zIndex:5});G.set(cards[old],{zIndex:4});
  turn=G.timeline({onComplete:()=>{if(run===sequence)arrange(index);}}).to(cards[old],{x:-28,y:18,z:-55,rotationY:-112,rotationZ:-4,scale:.95,duration:.42,ease:'power2.in'},0).to(cards[index],{x:0,y:0,z:1,rotationY:0,rotationZ:1.3,scale:1,duration:.65,ease:'power3.out'},.12);
  G.fromTo(document.querySelector('.hero-case-copy'),{y:5,opacity:.7},{y:0,opacity:1,duration:.3,ease:'power2.out',clearProps:'transform,opacity',overwrite:true});
 }
 buttons.forEach((button,i)=>button.addEventListener('click',()=>{if(scroll&&hero.classList.contains('flip-scroll')&&!reduced()){lockedCase=i;clearTimeout(lockTimer);lockTimer=setTimeout(()=>{lockedCase=null;},1000);window.scrollTo({top:scroll.start+(i+.15)/cases.length*(scroll.end-scroll.start),behavior:'smooth'});select(i,true,true);}else select(i,true,true);}));
 arrange(0);updateCopy(0,false);window.addEventListener('wheel',()=>{lockedCase=null;clearTimeout(lockTimer);},{passive:true});
 if(G&&window.ScrollTrigger){const media=G.matchMedia();media.add({desktop:'(min-width:1000px) and (min-height:720px)',small:'(max-width:999px), (max-height:719px)',reduce:'(prefers-reduced-motion: reduce)'},context=>{
   if(!context.conditions.desktop||context.conditions.reduce||reduced())return;
   hero.classList.add('flip-scroll');scroll=ScrollTrigger.create({trigger:hero,start:'top top',end:'bottom bottom',onUpdate:self=>{const i=Math.min(2,Math.floor(self.progress*3));if(lockedCase!==null&&i!==lockedCase)return;if(lockedCase===i){lockedCase=null;clearTimeout(lockTimer);}select(i,true,false);}});
   return()=>{clearTimeout(lockTimer);lockedCase=null;scroll?.kill();scroll=null;hero.classList.remove('flip-scroll');turn?.kill();arrange(current);};
  });}
 new MutationObserver(()=>{turn?.kill();if(G)G.killTweensOf(cards);arrange(current);}).observe(document.documentElement,{attributes:true,attributeFilter:['data-motion']});
})();
