/* One visible face: outgoing edge, atomic handoff, incoming face. No crossing backs. */
(()=>{
 'use strict';const payload=document.getElementById('hero-case-data');if(!payload)return;
 const cases=JSON.parse(payload.textContent),region=document.querySelector('.case-deck-region'),cards=[...document.querySelectorAll('.case-card')],pause=document.querySelector('.case-pause'),next=document.querySelector('.case-next'),link=document.getElementById('case-report-action'),progress=document.querySelector('.case-progress span'),G=window.gsap;
 let current=0,target=0,pending=null,turn=null,timer=0,progressTween=null,userPaused=false,inView=false,hovered=false,focused=false;
 const reduced=()=>document.documentElement.dataset.motion==='reduced'||matchMedia('(prefers-reduced-motion: reduce)').matches;
 region.classList.add('deck-enhanced');
 function pose(card,visible){if(G)G.set(card,{x:0,y:0,z:0,rotationY:0,rotationZ:reduced()?0:1.3,scale:1,opacity:visible?1:0,visibility:visible?'visible':'hidden'});else{card.style.visibility=visible?'visible':'hidden';card.style.opacity=visible?'1':'0';}card.style.zIndex=visible?'2':'0';}
 function commit(index,announce=false){current=index;cards.forEach((card,i)=>{pose(card,i===index);card.classList.toggle('is-current',i===index);card.setAttribute('aria-hidden',String(i!==index));card.inert=i!==index;});const c=cases[index];link.href=c.url;link.textContent='View '+c.short+'’s report';document.querySelector('.case-position').textContent='0'+(index+1)+' / 03';region.dataset.activeCase=c.id;if(announce)document.getElementById('case-announcement').textContent=c.name+'. '+c.title;}
 function stop(){clearTimeout(timer);timer=0;progressTween?.kill();progressTween=null;if(G)G.set(progress,{scaleX:0});else progress.style.transform='scaleX(0)';}
 function settle(){const index=turn?target:current;turn?.kill();turn=null;pending=null;G?.killTweensOf(cards);commit(index);region.dataset.turning='false';region.removeAttribute('aria-busy');link.inert=false;link.removeAttribute('aria-disabled');}
 function schedule(){stop();const playing=!userPaused&&!reduced();pause.setAttribute('aria-label',playing?'Pause car animation':'Play car animation');pause.dataset.paused=String(!playing);pause.hidden=reduced();region.dataset.autoplay=playing?'enabled':'paused';if(!playing||!inView||hovered||focused||document.hidden||turn)return;progressTween=G?.fromTo(progress,{scaleX:0},{scaleX:1,duration:6,ease:'none'});timer=setTimeout(()=>select(current+1),6000);}
 function select(index,announce=false){index=(index+cases.length)%cases.length;if(turn){pending=index;return;}if(index===current){schedule();return;}stop();target=index;
  if(!G||reduced()){commit(index,announce);schedule();return;}
  const outgoing=cards[current],incoming=cards[index];region.dataset.turning='true';region.setAttribute('aria-busy','true');link.inert=true;link.setAttribute('aria-disabled','true');
  // Never render two rotating faces together; decorative backing paper stays still.
  turn=G.timeline({onComplete:()=>{turn=null;commit(index);region.dataset.turning='false';region.removeAttribute('aria-busy');link.inert=false;link.removeAttribute('aria-disabled');const queued=pending;pending=null;if(queued!==null&&queued!==current)select(queued,true);else schedule();}})
   .to(outgoing,{rotationY:-86,scale:.9,opacity:0,duration:.25,ease:'power2.in'})
   .call(()=>{commit(index,announce);G.set(incoming,{rotationY:86,scale:.9,opacity:0});})
   .to(incoming,{rotationY:0,scale:1,opacity:1,duration:.4,ease:'power3.out'});
 }
 pause.addEventListener('click',()=>{userPaused=!userPaused;if(userPaused)settle();schedule();});next.addEventListener('click',()=>select((pending??(turn?target:current))+1,true));
 region.addEventListener('pointerenter',event=>{if(event.pointerType==='mouse'){hovered=true;schedule();}});region.addEventListener('pointerleave',()=>{hovered=false;schedule();});region.addEventListener('focusin',()=>{focused=true;schedule();});region.addEventListener('focusout',event=>{if(!region.contains(event.relatedTarget)){focused=false;schedule();}});
 document.addEventListener('visibilitychange',()=>{if(document.hidden)settle();schedule();});new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;if(!inView)settle();schedule();},{threshold:.25}).observe(region);
 const preference=()=>{settle();schedule();};new MutationObserver(preference).observe(document.documentElement,{attributes:true,attributeFilter:['data-motion']});matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',preference);window.addEventListener('resize',preference,{passive:true});
 commit(0);region.dataset.turning='false';schedule();
})();
