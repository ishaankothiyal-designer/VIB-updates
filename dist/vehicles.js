// Report routes are static so each car works without JavaScript.
document.querySelector('.vehicle-picker')?.addEventListener('submit', event => {
 event.preventDefault(); const select=event.currentTarget.querySelector('select');
 if ([...select.options].some(option=>option.value===select.value)) location.assign(select.value);
});
document.querySelectorAll('.fixture-chart').forEach(chart=>{
 chart.querySelectorAll('[data-value]').forEach(button=>button.addEventListener('click',()=>{
  chart.querySelectorAll('[data-value]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  chart.querySelector('.chart-readout').textContent=button.dataset.value;
 }));
});
let fileGroup=0;
document.querySelector('.refresh-files')?.addEventListener('click',event=>{
 fileGroup=1-fileGroup;
 document.querySelectorAll('[data-file-group]').forEach(card=>{card.hidden=Number(card.dataset.fileGroup)!==fileGroup;});
 document.querySelector('.file-page-state').textContent=fileGroup?'Showing cars 6–10 of 10':'Showing cars 1–5 of 10';
 event.currentTarget.textContent=fileGroup?'Show the first five cars':'Show five more cars';
});
const photoDialog=document.querySelector('.photo-dialog');let photoTrigger;
document.querySelectorAll('.photo-open').forEach(button=>button.addEventListener('click',()=>{
 photoTrigger=button;const img=photoDialog.querySelector('img');img.src=button.dataset.photo;img.alt=button.dataset.caption;
 photoDialog.querySelector('p').textContent=button.dataset.caption;photoDialog.showModal();
}));
photoDialog?.querySelector('.photo-close').addEventListener('click',()=>photoDialog.close());
photoDialog?.addEventListener('click',event=>{if(event.target===photoDialog)photoDialog.close();});
photoDialog?.addEventListener('close',()=>photoTrigger?.focus({preventScroll:true}));
