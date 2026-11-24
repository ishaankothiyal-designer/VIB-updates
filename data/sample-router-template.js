/* Pick from the background fixture collection. No network lookup or catalogue UI. */
(()=>{
 'use strict';const ids=__VEHICLE_IDS__;const key='vib-sample-cycle-v1';
 function nextReport(){
  let queue=[];let last='';
  try{const saved=JSON.parse(sessionStorage.getItem(key)||'{}');queue=Array.isArray(saved.queue)?saved.queue.filter(id=>ids.includes(id)):[];last=saved.last||'';}catch{}
  if(!queue.length){queue=[...ids];for(let i=queue.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[queue[i],queue[j]]=[queue[j],queue[i]];}if(queue[0]===last&&queue.length>1)[queue[0],queue[1]]=[queue[1],queue[0]];}
  const id=queue.shift();try{sessionStorage.setItem(key,JSON.stringify({queue,last:id}));}catch{}
  return 'sample-'+id+'.html';
 }
 if(/\/sample(?:\.html)?$/.test(location.pathname)){location.replace(nextReport()+location.hash);return;}
 document.addEventListener('click',event=>{const link=event.target.closest('a');if(!link||event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey||link.target==='_blank'||link.hasAttribute('download'))return;const url=new URL(link.href,location.href);if(url.origin===location.origin&&/\/sample(?:\.html)?$/.test(url.pathname)){event.preventDefault();location.assign(nextReport()+url.hash);}});
})();
