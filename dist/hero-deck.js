/* Three automatic paper-file turns; links and evidence always stay together. */
(()=>{
 'use strict';const payload=document.getElementById('hero-case-data');if(!payload)return;
 const cases=JSON.parse(payload.textContent),region=document.querySelector('.case-deck-region'),cards=[...document.querySelectorAll('.case-card')],pause=document.querySelector('.case-pause'),next=document.querySelector('.case-next'),progress=document.querySelector('.case-progress span'),G=window.gsap;
 let current=0,turn=null,sequence=0,timer=0,progressTween=null,userPaused=false,inView=false,hovered=false,focused=false;
 const reduced=()=>document.documentElement.dataset.motion==='reduced'||matchMedia('(prefers-reduced-motion: reduce)').matches;
 region.classList.add('deck-enhanced');
 function arrange(index){cards.forEach((card,i)=>{const depth=(i-index+cards.length)%cards.length;const pose={x:0,y:depth?-depth*9:0,z:depth?-depth*18:1,rotationY:0,rotationZ:reduced()?0:depth?(depth===1?-4:4):1.3,scale:1-depth*.025,zIndex:cards.length-depth,autoAlpha:1};if(G)G.set(card,pose);else{card.style.visibility=i===index?'visible':'hidden';card.style.zIndex=String(pose.zIndex);}card.classList.toggle('is-current',i===index);card.setAttribute('aria-hidden',String(i!==index));card.inert=i!==index;});}
 function updateCopy(index,announce){const c=cases[index],link=document.getElementById('case-report-action');link.href=c.url;link.textContent='View '+c.short+'’s report';document.querySelector('.case-position').textContent='0'+(index+1)+' / 03';region.dataset.activeCase=c.id;if(announce)document.getElementById('case-announcement').textContent=c.name+'. '+c.title;}
 function select(index,animate=true,announce=false){index=(index+cases.length)%cases.length;if(index===current){updateCopy(index,announce);return;}const old=current;current=index;sequence++;const run=sequence;turn?.kill();if(G)G.killTweensOf(cards);arrange(old);updateCopy(index,announce);cards.forEach((card,i)=>{card.classList.toggle('is-current',i===index);card.setAttribute('aria-hidden',String(i!==index));card.inert=i!==index;});
  if(!G||reduced()||!animate){arrange(index);return;}
  G.set(cards[index],{x:26,y:7,z:70,rotationY:88,rotationZ:1.3,scale:.985,autoAlpha:1,zIndex:5});G.set(cards[old],{zIndex:4});turn=G.timeline({onComplete:()=>{if(run===sequence)arrange(index);}}).to(cards[old],{x:-28,y:18,z:-55,rotationY:-112,rotationZ:-4,scale:.95,duration:.42,ease:'power2.in'},0).to(cards[index],{x:0,y:0,z:1,rotationY:0,rotationZ:1.3,scale:1,duration:.65,ease:'power3.out'},.12);
 }
 function stop(){clearTimeout(timer);timer=0;progressTween?.kill();progress.style.transform='scaleX(0)';}
 function schedule(){stop();const playing=!userPaused&&!reduced();pause.setAttribute('aria-label',playing?'Pause car animation':'Play car animation');pause.dataset.paused=String(!playing);pause.hidden=reduced();region.dataset.autoplay=playing?'enabled':'paused';if(!playing||!inView||hovered||focused||document.hidden)return;progressTween=G?.fromTo(progress,{scaleX:0},{scaleX:1,duration:6,ease:'none'});timer=setTimeout(()=>{select(current+1);schedule();},6000);}
 pause.addEventListener('click',()=>{userPaused=!userPaused;schedule();});next.addEventListener('click',()=>{select(current+1,true,true);schedule();});
 region.addEventListener('pointerenter',event=>{if(event.pointerType==='mouse'){hovered=true;schedule();}});region.addEventListener('pointerleave',()=>{hovered=false;schedule();});region.addEventListener('focusin',()=>{focused=true;schedule();});region.addEventListener('focusout',event=>{if(!region.contains(event.relatedTarget)){focused=false;schedule();}});
 document.addEventListener('visibilitychange',schedule);new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;schedule();},{threshold:.25}).observe(region);
 new MutationObserver(()=>{turn?.kill();if(G)G.killTweensOf(cards);arrange(current);schedule();}).observe(document.documentElement,{attributes:true,attributeFilter:['data-motion']});matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',()=>{arrange(current);schedule();});
 arrange(0);updateCopy(0,false);schedule();
})();
