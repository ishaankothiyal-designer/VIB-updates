import vm from 'node:vm';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const source=fs.readFileSync(new URL('./dist/sample-router.js',import.meta.url),'utf8');
function run(path,hash='',search='') {
 const result={};
 vm.runInNewContext(source,{location:{pathname:path,hash,search,replace:url=>result.redirect=url},document:{addEventListener(){}},JSON,Math,URL,sessionStorage:{getItem(){throw Error('Storage disabled')},setItem(){throw Error('Storage disabled')}}});
 return result;
}
for(const path of ['/sample.html','/sample','/VIB-updates/sample.html']) {
 for(let i=0;i<3;i++)assert.equal(run(path,'#mileage').redirect,'sample-swift.html#mileage');
}
assert.equal(run('/sample.html','#finance','?utm_source=local').redirect,'sample-swift.html?utm_source=local#finance');
for(const path of ['/index.html','/sample-creta.html','/guide.html'])assert.equal(run(path).redirect,undefined);
console.log('PASS: legacy sample entry is predictable, preserves chapters and project subpaths, works without storage, and never redirects explicit choices.');
