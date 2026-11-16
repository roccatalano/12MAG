window.addEventListener('load',()=>{
 const rng=s=>{const o=[];(s||'').split(',').forEach(p=>{if(p==='')return;if(p.includes('-')&&!p.startsWith('-')){const [a,b]=p.split('-').map(Number);for(let i=a;i<=b;i++)o.push(i)}else o.push(+p)});return o};
 function x2(sl){sl.querySelectorAll('.zkey.zkh.on').forEach(e=>e.classList.remove('on'));sl.querySelectorAll('.xon').forEach(e=>e.classList.remove('xon'));sl.querySelectorAll('.xm').forEach(e=>e.classList.remove('xm'));sl.querySelectorAll('table.s2lt tr.on').forEach(e=>e.classList.remove('on'));
  sl.querySelectorAll('.st[data-do].show').forEach(s=>s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');const el=document.getElementById(id);if(!el)return;
   if(op==='xb')rng(x).forEach(i=>el.querySelector(`rect.b[data-i="${i}"]`)?.classList.add('xon'));
   if(op==='xd')rng(x).forEach(k=>el.querySelector(`.dot[data-k="${k}"]`)?.classList.add('xon'));
   if(op==='xm')rng(x).forEach(k=>el.querySelector(`.dot[data-k="${k}"]`)?.classList.add('xm'));
   if(op==='xl'){const L=[...el.querySelectorAll('.lv')];rng(x).forEach(k=>L[k]?.classList.add('xon'))}
   if(op==='xs')el.querySelectorAll('tr')[+x]?.classList.add('on');
   if(op==='sk')el.querySelector('.zkey')?.classList.add('on');
   if(op==='bf')rng(x).forEach(k=>el.querySelectorAll(`[data-b="${k}"]`).forEach(e=>e.classList.add('xon')));
   if(op==='bok')el.classList.add('xon');
  }))}
 document.querySelectorAll('.slide.z').forEach(x2);
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);x2(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
});
