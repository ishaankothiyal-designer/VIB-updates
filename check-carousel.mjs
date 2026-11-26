import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
class Node {
 constructor(){this.dataset={};this.style={};this.attrs={};this.events={};this.classList={add(){},toggle(){}};this.inert=false;}
 addEventListener(name,fn){(this.events[name]??=[]).push(fn);}
 emit(name,event={}){for(const fn of this.events[name]??[])fn(event);}
 setAttribute(name,value){this.attrs[name]=value;}
 removeAttribute(name){delete this.attrs[name];}
 contains(value){return value===this;}
}
function setup(){
 const selectors=['.case-deck-region','.case-pause','.case-next','#case-report-action','.case-progress span','.case-position','#case-announcement'];
 const nodes=Object.fromEntries(selectors.map(key=>[key,new Node()]));
 const root=new Node();root.dataset.motion='full';const cards=[new Node(),new Node(),new Node(),new Node()];const buttons=cards.map(()=>new Node());const timers=new Map();let id=0;
 const payload={textContent:JSON.stringify([{id:'overview',category:'Overview',name:'Report',title:'Report',url:'#sample-reports',action:'Explore sample reports'},{id:'swift',short:'Swift',name:'Swift',title:'Mileage',url:'sample-swift.html#mileage'},{id:'creta',short:'Creta',name:'Creta',title:'Finance',url:'sample-creta.html#finance'},{id:'brezza',short:'Brezza',name:'Brezza',title:'Challans',url:'sample-brezza.html#challans'}])};
 const doc=new Node();Object.assign(doc,{documentElement:root,hidden:false,getElementById:key=>key==='hero-case-data'?payload:nodes['#'+key],querySelector:key=>nodes[key],querySelectorAll:key=>key==='.case-card'?cards:buttons});
 const context={document:doc,window:{addEventListener(){}},matchMedia:()=>({matches:false,addEventListener(){}}),IntersectionObserver:class{constructor(fn){this.fn=fn;}observe(){this.fn([{isIntersecting:true}]);}},MutationObserver:class{observe(){}},setTimeout:fn=>{timers.set(++id,fn);return id;},clearTimeout:key=>timers.delete(key)};
 vm.runInNewContext(fs.readFileSync('dist/hero-deck.js','utf8'),context);
 return {nodes,root,timers,doc,buttons,tick(){const fn=timers.values().next().value;assert.ok(fn,'Playback must schedule a transition');timers.clear();fn();}};
}
const t=setup(),region=t.nodes['.case-deck-region'],play=t.nodes['.case-pause'],next=t.nodes['.case-next'],link=t.nodes['#case-report-action'];
assert.equal(t.timers.size,0,'No autoplay before request');
region.emit('pointerenter',{pointerType:'mouse'});region.emit('focusin');play.emit('click');
t.tick();assert.equal(region.dataset.activeCase,'swift');assert.equal(link.href,'sample-swift.html#mileage');
next.emit('click');assert.equal(region.dataset.activeCase,'creta');
region.emit('pointerleave');region.emit('pointerenter',{pointerType:'mouse'});
assert.ok(t.timers.size,'Returning the pointer must not cancel explicit Play');
region.emit('focusin');assert.ok(t.timers.size,'Refocusing controls preserves explicit Play');
assert.equal(play.attrs['aria-label'],'Pause car animation','Running UI offers Pause');
next.emit('click');assert.equal(region.dataset.activeCase,'brezza');assert.equal(link.href,'sample-brezza.html#challans');
next.emit('click');assert.equal(region.dataset.activeCase,'overview');assert.equal(link.href,'#sample-reports');
play.emit('click');assert.equal(t.timers.size,0,'Pause cancels pending playback');
next.emit('click');assert.equal(region.dataset.activeCase,'swift','Manual next works while paused');assert.equal(t.timers.size,0);
console.log('PASS: explicit Play while hovered/focused, Pause, manual Next/wrap and matching report URL without GSAP.');

t.buttons[3].emit('click');assert.equal(region.dataset.activeCase,'brezza');assert.equal(t.buttons[3].attrs['aria-pressed'],'true');assert.equal(t.timers.size,0);
