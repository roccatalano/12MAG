(function(){function zs1(sl){sl.querySelectorAll('svg.zch:not(.full) .cax,svg.zch:not(.full) .cbr,svg.zch:not(.full) .clg,[data-f]').forEach(e=>e.classList.remove('on'));
 sl.querySelectorAll('.zc').forEach(c=>c.classList.remove('hb','hy','hg'));sl.querySelectorAll('tr.hl').forEach(r=>r.classList.remove('hl'));
 sl.querySelectorAll('.st[data-do].show').forEach(s=>s.dataset.do.split(' ').forEach(a=>{const [op,id,x,y]=a.split(':');const el=document.getElementById(id);if(!el)return;
  if(op==='ax')el.querySelector('.cax')?.classList.add('on');if(op==='lg')el.querySelector('.clg')?.classList.add('on');
  if(op==='bg')x.split(',').forEach(i=>el.querySelector(`.cbr[data-i="${i}"]`)?.classList.add('on'));
  if(op==='tf')x.split(',').forEach(k=>el.querySelector(`[data-f="${k}"]`)?.classList.add('on'));
  if(op==='hv')el.querySelectorAll(`.zc[data-v="${x}"]`).forEach(c=>c.classList.add(y));
  if(op==='hr')x.split(',').forEach(r=>el.querySelector(`tr[data-r="${r}"]`)?.classList.add('hl'))}))}
 document.querySelectorAll('.slide.z').forEach(zs1);
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);zs1(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});})();
// bar chart -> one stacked bar -> 100% bar (morph_svg). Stage = highest mo:id:k among shown steps
// (0 bars, 1 stacked, 2 percentage axis, 3 legend). Values, axis max come from the svg's data-v / data-ymax.
(function(){
 const cfg=sv=>{if(!sv._c){const V=sv.dataset.v.split(',').map(Number),T=V.reduce((a,b)=>a+b,0);sv._c={V,Y:+sv.dataset.ymax,P:V.map(v=>v/T*100),LP:V.map(v=>(v/T*100).toFixed(1)+'%')}}return sv._c};
 function geom(sv,s){const {V,Y,P}=cfg(sv);const [X0,Y0,Y1,XE]=sv.dataset.g.split(',').map(Number),H=Y0-Y1,bw=110;const g=[];
  if(s===0){const sl=(XE-X0)/V.length;V.forEach((v,i)=>g.push({x:X0+sl*(i+.5)-bw/2,y:Y0-v/Y*H,h:v/Y*H}))}
  else{const xc=X0+(XE-X0)/2-bw/2;let b=0;const u=s===1?V.map(v=>v/Y*H):P.map(p=>p/100*H);u.forEach(h=>{g.push({x:xc,y:Y0-b-h,h});b+=h})}
  return {g,bw}}
 function draw(sv,G,s){const {V,LP}=cfg(sv);sv.querySelectorAll('.mor').forEach((r,i)=>{const q=G.g[i];r.setAttribute('x',q.x);r.setAttribute('y',q.y);r.setAttribute('width',G.bw);r.setAttribute('height',Math.max(0,q.h))});
  sv.querySelectorAll('.mol').forEach((t,i)=>{const q=G.g[i];t.setAttribute('x',q.x+G.bw/2);t.setAttribute('y',q.y+q.h/2+8);t.textContent=s>=2?LP[i]:V[i];if(s===0){t.setAttribute('y',q.y-10)}});
  sv.querySelectorAll('.moc').forEach((t,i)=>{const q=G.g[i];t.setAttribute('x',q.x+G.bw/2)})}
 function set(sv,s){const from=sv._s??0;sv._s=s;const A=geom(sv,from),B=geom(sv,s);
  sv.querySelector('.mof').style.opacity=s>=2?0:1;sv.querySelector('.mop').style.opacity=s>=2?1:0;sv.querySelector('.molg').style.opacity=s>=3?1:0;
  sv.querySelector('.mocat').style.opacity=s===0?1:0;sv.querySelector('.moxl').style.opacity=s===0?1:0;
  if(sv._raf)cancelAnimationFrame(sv._raf);if(from===s){draw(sv,B,s);return}
  const t0=performance.now(),D=1100,e=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
  const step=now=>{const k=e(Math.min(1,(now-t0)/D));const G={bw:B.bw,g:A.g.map((a,i)=>({x:a.x+(B.g[i].x-a.x)*k,y:a.y+(B.g[i].y-a.y)*k,h:a.h+(B.g[i].h-a.h)*k}))};
   draw(sv,G,k<1?Math.min(from,s)+(k>.5&&s>from?s-from:0):s);if(k<1)sv._raf=requestAnimationFrame(step)};sv._raf=requestAnimationFrame(step)}
 function upd(sl){sl.querySelectorAll('svg.zmorph').forEach(sv=>{let s=0;sl.querySelectorAll('.st.show[data-do]').forEach(st=>st.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');if(op==='mo'&&id===sv.id)s=Math.max(s,+x)}));if(s!==sv._s)set(sv,s)})}
 document.querySelectorAll('svg.zmorph').forEach(sv=>{sv._s=0;set(sv,0)});
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)&&sl.querySelector('svg.zmorph')){seen.add(sl);upd(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});})();
