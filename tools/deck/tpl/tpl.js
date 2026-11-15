/* ---------- tpl: formula substitution ---------- */
/* hidden items revealed step by step (Lesson 2): elements with class hid0 start hidden (dot3 charts with cfg.hid: every dot);
   data-show="#id|i,j;#id2|k" reveals the [data-i] items listed */
function tplHide(s){s.querySelectorAll('[data-chart="dot3"]').forEach(b=>{let c={};try{c=JSON.parse(b.dataset.cfg)}catch(e){}if(c.hid)b.querySelectorAll('circle.d3').forEach(d=>d.classList.add('hid0'))});s.querySelectorAll('.hid0').forEach(e=>e.classList.add('hid'))}
function tplShow(s,f){if(f.dataset.show)f.dataset.show.split(';').forEach(sp=>{const [sel,ks]=sp.split('|');const box=s.querySelector(sel);if(!box)return;ks.split(',').forEach(k=>box.querySelectorAll('[data-i="'+k+'"]').forEach(e=>e.classList.remove('hid')))})}

/* dot plot: a dashed line between two neighbouring dots (e.g. the 20.5th position) */
function dotSplit(spec){const [sel,i,lab]=spec.split('|');const box=document.querySelector(sel);if(!box)return;const svg=box.querySelector('svg');
  const a=svg.querySelector('circle[data-i="'+i+'"]'),b=svg.querySelector('circle[data-i="'+(+i+1)+'"]');if(!a||!b)return;
  const ax=+a.getAttribute('cx'),ay=+a.getAttribute('cy'),bx=+b.getAttribute('cx'),by=+b.getAttribute('cy'),r=+a.getAttribute('r');
  const g=el('g',{class:'dsplit'});
  if(Math.abs(ax-bx)<1){const y=(ay+by)/2;g.append(el('line',{x1:ax-r*2.6,x2:ax+r*2.6,y1:y,y2:y,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'7 5'}),el('text',{x:ax+r*3,y:y+7,'font-size':22,'font-weight':800,fill:'#b0263a'},lab||''))}
  else{const x=(ax+bx)/2;g.append(el('line',{x1:x,x2:x,y1:Math.min(ay,by)-r*2,y2:Math.max(ay,by)+r,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'7 5'}),el('text',{x:x+6,y:Math.min(ay,by)-r*2,'font-size':22,'font-weight':800,fill:'#b0263a'},lab||''))}
  svg.append(g)}
function tplapply(s,f){normApply(f);tplShow(s,f);if(f.dataset.dsplit)dotSplit(f.dataset.dsplit);if(f.dataset.fx==='sub'){const x=f.closest('.fx');if(x)x.classList.add('sub')}if(f.dataset.pk!=null){const k=+f.dataset.pk;s.querySelectorAll('[data-pks]').forEach(e=>e.classList.toggle('dim',!e.dataset.pks.split(',').includes(String(k))));s.querySelectorAll('.L ol.parts li').forEach((li,i)=>li.classList.toggle('dim',i!==k));s.querySelectorAll('.pa').forEach((p,i)=>p.classList.toggle('dim',i<k))}
if(f.dataset.tmpl){const [w,k]=f.dataset.tmpl.split(':');if(w==='on')f.closest('.tmpl').classList.add('on');else{const t=s.querySelector('.tmpl[data-tk="'+k+'"]');t.classList.add('done');const all=s.querySelectorAll('.tmpl');if(all[all.length-1]===t&&!s.querySelector('[data-pall]'))s.querySelectorAll('.hc,.hv,.hy,.hb,.hg').forEach(e=>e.classList.remove('hc','hv','hy','hb','hg'))}}
if(f.dataset.hi)f.dataset.hi.split(';').forEach(sp=>{const [sel,ks,c]=sp.split('|');const box=s.querySelector(sel);if(!box)return;box.querySelectorAll('.hc,.hv,.hy,.hb,.hg').forEach(e=>e.classList.remove('hc','hv','hy','hb','hg'));if(ks)ks.split(',').forEach(k=>box.querySelectorAll('[data-i="'+k+'"]').forEach(e=>e.classList.add(c||'hy')))});
if(f.dataset.grow)f.dataset.grow.split(';').forEach(g=>{const [sel,i]=g.split('|');const ch=s.querySelector(sel);if(ch){grow(ch.querySelectorAll('rect.grow')[+i]);if(f.dataset.lg!=null)ch.classList.remove('hidelg')}});
if(f.dataset.ax){s.querySelectorAll(f.dataset.ax).forEach(c=>c.classList.remove('noax'))}
if(f.dataset.pall){s.querySelectorAll('.hc,.hv,.hy,.hb,.hg').forEach(e=>e.classList.remove('hc','hv','hy','hb','hg'));s.querySelectorAll('[data-pks].dim').forEach(e=>e.classList.remove('dim'));s.querySelectorAll('.L ol.parts li.dim,.pa.dim').forEach(e=>e.classList.remove('dim'))}}
function tplreset(s){tplHide(s);s.querySelectorAll('.hx').forEach(e=>e.classList.remove('hx'));s.querySelectorAll('[data-axhide]').forEach(c=>c.classList.add('noax'));s.querySelectorAll('.tmpl').forEach(e=>e.classList.remove('on','done'));s.querySelectorAll('.hc,.hv,.hy,.hb,.hg').forEach(e=>e.classList.remove('hc','hv','hy','hb','hg'));s.querySelectorAll('[data-pks].dim').forEach(e=>e.classList.remove('dim'));s.querySelectorAll('ol.parts li.dim,.pa.dim').forEach(e=>e.classList.remove('dim'));normReset(s);s.querySelectorAll('g.dsplit').forEach(g=>g.remove());s.querySelectorAll('.fx.sub').forEach(x=>x.classList.remove('sub'))}
/* ---------- tpl: normal curve (68–95–99.7%) ----------
   cfg: m (mean) · s (SD) · rows ['x','z'] axis rows · hide ['x','z','pct'] hidden until shown · xl axis title · W h fs · dec · sh [[a,b,col,label]] always shaded
   frags: data-nclear="#id" (clear earlier shading/marks) · data-nshade="#id|a,b|col|label" (z units; spaces separate several) · data-nshow="#id|x,z,pct" · data-nmark="#id|z|label|col" */
const NPDF=z=>Math.exp(-z*z/2);
function normGeo(c){const W=c.W||900,rows=c.rows||['z'],fs=c.fs||18,T=c.T||52,B=rows.length*30+(c.xl?30:10),H=c.h||330,base=H-B,L=24,R=24,pw=W-L-R,
  sx=z=>L+(z+3.6)/7.2*pw,sy=z=>base-NPDF(z)*(base-T);return {W,H,rows,fs,T,B,base,L,R,pw,sx,sy}}
function normPath(g,a,b){a=Math.max(a,-3.6);b=Math.min(b,3.6);let d=`M${g.sx(a)},${g.base}`;for(let k=0;k<=80;k++){const z=a+(b-a)*k/80;d+=` L${g.sx(z).toFixed(1)},${g.sy(z).toFixed(1)}`}return d+` L${g.sx(b)},${g.base} Z`}
function nfmt(v,d){return (d!=null?(+v).toFixed(d):String(+(+v).toFixed(6))).replace('-','−')}
function drawNorm(box,c){const g=normGeo(c),s=el('svg',{viewBox:`0 0 ${g.W} ${g.H}`,width:'100%'});box._g=g;
  s.append(el('g',{class:'nsh'}));
  (c.sh||[]).forEach(r=>normShade(s,g,r));
  for(let z=-3;z<=3;z++)s.append(el('line',{x1:g.sx(z),x2:g.sx(z),y1:g.base,y2:g.sy(z),stroke:'#8a93a6','stroke-width':z?1.2:2,'stroke-dasharray':z?'5 4':''}));
  let d='';for(let k=0;k<=200;k++){const z=-3.6+7.2*k/200;d+=(k?' L':'M')+g.sx(z).toFixed(1)+','+g.sy(z).toFixed(1)}
  s.append(el('path',{d,fill:'none',stroke:'#1f4fb0','stroke-width':3}));
  s.append(el('line',{x1:g.L-6,x2:g.W-g.R+6,y1:g.base,y2:g.base,stroke:'#333','stroke-width':2}));
  const pg=el('g',{class:'npct'});[[.5,'34%'],[1.5,'13.5%'],[2.5,'2.35%'],[3.3,'0.15%']].forEach(([z,t])=>[-z,z].forEach(zz=>{
    const y=Math.min(g.sy(zz)-8,g.base-(Math.abs(zz)>3?16:Math.abs(zz)>2?30:0));pg.append(el('text',{x:g.sx(zz),y,'text-anchor':'middle','font-size':g.fs-2,'font-weight':700,fill:'#5b33b0'},t))}));s.append(pg);
  g.rows.forEach((r,k)=>{const rg=el('g',{class:'n'+r}),y=g.base+24+k*30;
    for(let z=-3;z<=3;z++){let t;if(r==='z')t='z = '+nfmt(z);else t=nfmt(c.m+z*c.s,c.dec);
      rg.append(el('text',{x:g.sx(z),y,'text-anchor':'middle','font-size':g.fs,'font-weight':r==='z'?600:400,fill:r==='z'?'#5b33b0':'#222'},t))}
    if(r==='x'&&c.xl)rg.append(el('text',{x:g.L+g.pw/2,y:g.H-6,'text-anchor':'middle','font-size':g.fs+1,'font-weight':600,'font-style':'italic'},c.xl));
    s.append(rg)});
  s.append(el('g',{class:'nmk'}));box.append(s);normHide(box,c)}
function normHide(box,c){const h=c.hide||[];['x','z','pct'].forEach(k=>{const e=box.querySelector('g.n'+k);if(e)e.style.opacity=h.includes(k)?0:1})}
function normShade(s,g,r,dyn){const [a,b,col,lab]=r;const dc=dyn?' dyn':'';const grp=s.querySelector('g.nsh');
  const p=el('path',{d:normPath(g,a,b),fill:col||'rgba(79,132,230,.45)',stroke:'none',class:'nsp'+dc});grp.append(p);
  if(lab){const zc=(Math.max(a,-3.6)+Math.min(b,3.6))/2,w=Math.min(b,3.6)-Math.max(a,-3.6),y=w>1.2?g.base-(g.base-g.sy(zc))*.4:g.sy(zc)-34;
    grp.append(el('text',{x:g.sx(zc),y,'text-anchor':'middle','font-size':g.fs+4,'font-weight':800,fill:'#0b2a6b',class:'nsl'+dc},lab.replace(/_/g,' ')))}}
function normApply(f){
  if(f.dataset.nclear)f.dataset.nclear.split(' ').forEach(sel=>document.querySelectorAll(sel+' g.nsh .dyn,'+sel+' g.nmk > *').forEach(e=>e.remove()));
  if(f.dataset.nshade)f.dataset.nshade.split(' ').forEach(sp=>{const [sel,ab,col,lab]=sp.split('|');const box=document.querySelector(sel);if(!box)return;
    const [a,b]=ab.split(',').map(Number);normShade(box.querySelector('svg'),box._g,[a,b,col,lab],1)});
  if(f.dataset.nshow)f.dataset.nshow.split(' ').forEach(sp=>{const [sel,ks]=sp.split('|');ks.split(',').forEach(k=>{const e=document.querySelector(sel+' g.n'+k);if(e)e.style.opacity=1})});
  if(f.dataset.nmark)f.dataset.nmark.split(' ').forEach(sp=>{const [sel,z,lab,col]=sp.split('|');const box=document.querySelector(sel);if(!box)return;const g=box._g,x=g.sx(+z),m=box.querySelector('g.nmk'),cl=col||'#d2475b';
    m.append(el('line',{x1:x,x2:x,y1:g.T-30,y2:g.base,stroke:cl,'stroke-width':3.5}),el('text',{x,y:g.T-36,'text-anchor':'middle','font-size':g.fs+2,'font-weight':800,fill:cl},(lab||'').replace(/_/g,' ')))})}
function normReset(s){s.querySelectorAll('[data-chart="norm"]').forEach(b=>{const c=JSON.parse(b.dataset.cfg);b.querySelectorAll('g.nsh .dyn').forEach(e=>e.remove());
  b.querySelectorAll('g.nmk > *').forEach(e=>e.remove());normHide(b,c)})}
/* fixed shades are drawn first; mark them so reset keeps them */
document.querySelectorAll('[data-chart="norm"]').forEach(b=>drawNorm(b,JSON.parse(b.dataset.cfg)));
/* histogram: labels centred under each column (discrete values), cfg.clab */
document.querySelectorAll('[data-chart="hist"]').forEach(b=>{const c=JSON.parse(b.dataset.cfg);if(!c.clab)return;const W=c.W||640,H=c.h||400,L=c.L||74,B=c.xl?76:44,T=16,R=24,ph=H-T-B,pw=W-L-R,fs=c.fs||19;
  const x0=c.xmin!=null?c.xmin:c.start,x1=c.xmax!=null?c.xmax:c.start+c.w*c.v.length,sx=x=>L+(x-x0)/(x1-x0)*pw,svg=b.querySelector('svg');
  c.clab.forEach((t,i)=>svg.append(el('text',{x:sx(c.start+(i+.5)*c.w),y:T+ph+29,'text-anchor':'middle','font-size':fs},t)))});
