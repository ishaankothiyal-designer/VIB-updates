// Report routes are static so each car works without JavaScript.
document.querySelectorAll('.fixture-chart').forEach(chart=>{
 chart.querySelectorAll('[data-value]').forEach(button=>button.addEventListener('click',()=>{
  chart.querySelectorAll('[data-value]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  chart.querySelector('.chart-readout').textContent=button.dataset.value;
 }));
});
const photoDialog=document.querySelector('.photo-dialog');let photoTrigger;
document.querySelectorAll('.photo-open').forEach(button=>button.addEventListener('click',()=>{
 photoTrigger=button;const img=photoDialog.querySelector('img');img.src=button.dataset.photo;img.alt=button.dataset.caption;
 photoDialog.querySelector('p').textContent=button.dataset.caption;photoDialog.showModal();
}));
photoDialog?.querySelector('.photo-close').addEventListener('click',()=>photoDialog.close());
photoDialog?.addEventListener('click',event=>{if(event.target===photoDialog)photoDialog.close();});
photoDialog?.addEventListener('close',()=>photoTrigger?.focus({preventScroll:true}));
