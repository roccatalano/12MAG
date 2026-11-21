// lib/assoc (Chapter 2): sl:id shows a scatterplot's line, sx:id shows its points (build=True). Table fills (tf),
// row highlights (hr), bars (ax / bg / lg) are done by lib/cat.js; cell highlights (tc) by core.js.
(function(){function za(sl){sl.querySelectorAll('svg.zsc .zsl,svg.zsc.zbuild .zsp,.zrep2 [data-f]').forEach(e=>e.classList.remove('on'));
 sl.querySelectorAll('.st[data-do].show').forEach(s=>s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');const el=document.getElementById(id);if(!el)return;
  if(op==='sl')el.querySelector('.zsl')?.classList.add('on');
  if(op==='sx')el.querySelector('.zsp')?.classList.add('on');
  if(op==='tf'&&el.classList.contains('zrep2'))x.split(',').forEach(k=>el.querySelector(`[data-f="${k}"]`)?.classList.add('on'))}))}
 document.querySelectorAll('.slide.z').forEach(za);
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);za(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});})();
