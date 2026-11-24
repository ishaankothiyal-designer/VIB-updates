import vm from 'node:vm';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const source=fs.readFileSync(new URL('./dist/sample-router.js',import.meta.url),'utf8');
const cars=JSON.parse(fs.readFileSync(new URL('./dist/cars.json',import.meta.url),'utf8')).cars;
const allowed=new Set(cars.map(c=>'sample-'+c.id+'.html'));let state=null;
const storage={getItem:()=>state,setItem:(key,value)=>{state=value}};
function run(path='/sample.html',sessionStorage=storage){const result={};const events={};const ctx={Math,JSON,URL,sessionStorage,location:{pathname:path,origin:'https://vib.example',href:'https://vib.example'+path,hash:'#mileage',replace:url=>result.redirect=url,assign:url=>result.navigation=url},document:{addEventListener:(name,fn)=>events[name]=fn}};vm.runInNewContext(source,ctx);return {...result,events,result};}
const picks=Array.from({length:20},()=>run().redirect.replace('#mileage',''));
assert.equal(new Set(picks.slice(0,10)).size,10);assert.equal(new Set(picks.slice(10)).size,10);assert.notEqual(picks[9],picks[10]);assert(picks.every(p=>allowed.has(p)));
const denied={getItem(){throw Error('Storage unavailable')},setItem(){throw Error('Storage unavailable')}};assert(allowed.has(run('/sample.html',denied).redirect.replace('#mileage','')));
const page=run('/index.html');let prevented=false;page.events.click({target:{closest:()=>({href:'https://vib.example/sample.html#mileage',hasAttribute:()=>false})},button:0,preventDefault(){prevented=true}});assert(prevented);assert(page.result.navigation.endsWith('#mileage'));assert(allowed.has(page.result.navigation.replace('#mileage','')));
console.log('PASS: two complete no-repeat report cycles, boundary repeat prevention, storage-denied fallback and contextual sample-link navigation.');
