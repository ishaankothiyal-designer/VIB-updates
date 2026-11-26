/* Local preview only: no network calls, storage or invented vehicle results. */
(() => {
 'use strict';
 function registrationState(input){
  const raw=String(input).trim();const value=raw.replace(/[ -]/g,'').toUpperCase();
  return {valid:/^[a-z\d -]+$/i.test(raw)&&/^[A-Z\d]{6,12}$/.test(value)&&/[A-Z]/.test(value)&&/\d/.test(value),value};
 }
 if(typeof module!=='undefined')module.exports={registrationState};
 if(typeof document==='undefined')return;
 const form=document.querySelector('#vehicle-check form');if(!form)return;
 const input=form.querySelector('input');const control=input.closest('.registration-control');const button=form.querySelector('button');const feedback=document.querySelector('#vehicle-feedback');
 button.disabled=false;
 input.addEventListener('input',()=>{input.removeAttribute('aria-invalid');input.removeAttribute('aria-errormessage');control.classList.remove('is-invalid');feedback.textContent='';delete feedback.dataset.state;});
 form.addEventListener('submit',event=>{
  event.preventDefault();const state=registrationState(input.value);
  if(!state.valid){input.setAttribute('aria-invalid','true');input.setAttribute('aria-errormessage','vehicle-feedback');control.classList.add('is-invalid');feedback.dataset.state='error';feedback.textContent='Enter the registration using letters and numbers, for example DL 03 AB 1234.';input.focus();return;}
  input.value=state.value;input.removeAttribute('aria-invalid');input.removeAttribute('aria-errormessage');control.classList.remove('is-invalid');feedback.dataset.state='demo';
  feedback.textContent=`No vehicle check was run. Explore a sample report to see the records and questions to consider.`;
 });
 document.querySelectorAll('a[href="#vehicle-check"]').forEach(link=>link.addEventListener('click',()=>{input.focus({preventScroll:true});}));
})();
