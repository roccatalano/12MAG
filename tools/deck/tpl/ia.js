/* ---------- ia: interactive features (16 Nov, ideas from the 10MA deck, 12MAG look) ----------
   Every feature is driven by data attributes on reveal steps (frags), so the click-reveal, back() and the PDF (final frame) all work.
   Widgets the teacher touches (sliders, card sort, plinko, rounder) carry class "ia": a click on them never advances the slide.
   IA.fast = 1 while the engine replays steps (show(n,true), back()): no delays, so the final frame is reached at once.
   1 tiles      data-tsort="#t" · data-tcross="#t|a|b" · data-tmid="#t|a|b|cls|label|line" · data-thalves="#t"   (a, b = positions in the ORDERED list; blank = all)
   2 sliders    data-fset="#id|value" (fences / box plot / z / log sliders: animate to a value) · data-shset="#id|skew" (shape slider, −1…1)
                every slider has a visible range control under its figure (.i-ctl); the figure handle can be dragged too
   3 card sort  (10MA 'Sort it') each card has Step 1 buttons; a right answer opens Step 2 for that group.
                data-sreveal="#id|1[|cards]" (show the right Step 1 answers) · data-sreveal="#id|2[|cards]" (Step 2) · cards = 0,3,5 (blank = all)
   4 stem       data-leaf="#id|0-5" or "#id|0,3,7" or "#id|all" (leaves fly in from the data list) · data-lsort="#id" (order each row)
     tally      data-ftally="#chips|#table|i" (light the values in class i and count them into row i) · data-ftot="#table" · data-fgrow="#hist|i"
   5 two tests  data-ztset="#id|xA|xB" (blank keeps a value)
   6 plinko     data-plk="#id|50" (drop a batch; replays/PDF add the expected binomial pile at once) · data-plk="#id|0" (reset)
   7 rounder    data-rset="#id|dp|2" or "#id|sf|3"
   8 norm       (tpl.js normal curve) % labels lifted clear of the curve · cfg.br: hooked 68/95/99.7% brackets · data-nbr="#id|1,2,3" shows hidden ones */
const IA={T:[],fast:0};
function iaLater(fn,ms){if(IA.fast||!ms)fn();else IA.T.push(setTimeout(fn,ms))}
const iaS=()=>(stage.getBoundingClientRect().width/1600)||1;
const iaNum=v=>String(+(+v).toFixed(6)).replace('-','−');
const iaEach=(spec,fn)=>{if(spec)spec.split(';').forEach(sp=>{const p=sp.split('|');const b=document.querySelector(p[0]);if(b)fn(b,p.slice(1))})};
const iaDiv=(cls,html)=>{const d=document.createElement('div');d.className=cls;if(html!=null)d.innerHTML=html;return d};
/* quartiles, VCAA/CAS method: n odd leaves the median out of both halves */
function iaMed(a){const n=a.length;return n%2?a[(n-1)/2]:(a[n/2-1]+a[n/2])/2}
function iaFive(v){const a=v.slice().sort((x,y)=>x-y),n=a.length,h=Math.floor(n/2);return {a,min:a[0],max:a[n-1],m:iaMed(a),q1:iaMed(a.slice(0,h)),q3:iaMed(a.slice(n-h))}}

/* ===== 1. data tiles ===== */
function tlInit(b){const t=[...b.querySelectorAll('.i-t')];b._n=t.length;
  const ord=t.map((e,k)=>[+e.dataset.v,k]).sort((x,y)=>x[0]-y[0]||x[1]-y[1]).map(p=>p[1]);b._rank=[];b._at=[];ord.forEach((k,j)=>{b._rank[k]=j;b._at[j]=t[k]});tlReset(b)}
function tlPos(b,sorted){b.querySelectorAll('.i-t').forEach((e,k)=>{const j=sorted?b._rank[k]:k;e.style.left=`calc(${j} * 100% / ${b._n} + 4px)`})}
function tlClr(b){b.querySelectorAll('.i-t').forEach(e=>{e.classList.remove('t-x','t-xo','t-mid','t-q','t-lo','t-hi');e.style.transitionDelay=''})}
function tlReset(b){tlPos(b,0);tlClr(b);b.querySelectorAll('.i-tlab,.i-tsplit,.i-tmline').forEach(e=>e.remove())}
function tlRange(b,p){const a=p[0]!==undefined&&p[0]!==''?+p[0]:0,c=p[1]!==undefined&&p[1]!==''?+p[1]:b._n-1;return [a,c]}
function tlCross(b,a,c){let i=a,j=c,k=0;while(j-i>=2){[i,j].forEach(q=>{const e=b._at[q];e.style.transitionDelay=IA.fast?'':(k*.38)+'s';e.classList.remove('t-xo');e.classList.add('t-x')});i++;j--;k++}return k}
function tlFade(L,delay){if(IA.fast)L.classList.add('on');else{L.style.transitionDelay=delay+'s';requestAnimationFrame(()=>requestAnimationFrame(()=>L.classList.add('on')))}}
function tlMid(b,a,c,cls,lab,delay,line){cls=cls||'mid';const n=c-a+1,m=a+Math.floor((n-1)/2);(n%2?[m]:[m,m+1]).forEach(q=>{const e=b._at[q];e.classList.remove('t-x','t-xo');e.style.transitionDelay=IA.fast?'':delay+'s';e.classList.add('t-'+cls)});
  const mid=(a+c+1)/2;
  /* even n: optional solid line between the two middle tiles (the median sits between them) */
  if(line&&n%2===0){const M=iaDiv('i-tmline l-'+cls);M.style.left=`calc(${mid} * 100% / ${b._n})`;b.append(M);tlFade(M,delay)}
  if(lab){const L=iaDiv('i-tlab l-'+cls,lab);L.style.left=`calc(${mid} * 100% / ${b._n})`;b.append(L);tlFade(L,delay)}}
function tlSplit(b,pos){if([...b.querySelectorAll('.i-tmline')].some(m=>m.style.left===`calc(${pos} * 100% / ${b._n})`))return;
  const d=iaDiv('i-tsplit');d.style.left=`calc(${pos} * 100% / ${b._n})`;b.append(d)}
function tlApply(f){
  iaEach(f.dataset.tsort,(b)=>{tlPos(b,1);b._sorted=1});
  const crossed={};
  iaEach(f.dataset.tcross,(b,p)=>{const [a,c]=tlRange(b,p);crossed[b.id+'|'+a+'|'+c]=tlCross(b,a,c)});
  iaEach(f.dataset.tmid,(b,p)=>{const [a,c]=tlRange(b,p);const k=crossed[b.id+'|'+a+'|'+c];tlMid(b,a,c,p[2],p[3],k!=null?k*.38+.15:0,p[4]==='1')});
  /* halves: the median tile(s), its label and line stay; values crossed off for the median stay marked (faded strike) */
  iaEach(f.dataset.thalves,(b)=>{const n=b._n,h=Math.floor(n/2);b.querySelectorAll('.i-t').forEach(e=>{if(e.classList.contains('t-x')){e.classList.remove('t-x');e.classList.add('t-xo')}e.classList.remove('t-q');e.style.transitionDelay=''});
    for(let j=0;j<h;j++){b._at[j].classList.add('t-lo');b._at[n-1-j].classList.add('t-hi')}
    if(n%2){tlSplit(b,h);tlSplit(b,h+1)}else tlSplit(b,h)})}

/* ===== 2. sliders: fences · box plot · normal z · log scale · shape ===== */
function slSvg(W,H){return el('svg',{viewBox:`0 0 ${W} ${H}`,width:'100%',class:'i-svg'})}
function slDrag(box,svg,toVal){let on=false;const v=e=>{const p=svg.createSVGPoint();p.x=e.clientX;p.y=e.clientY;return toVal(p.matrixTransform(svg.getScreenCTM().inverse()).x)};
  svg.addEventListener('pointerdown',e=>{on=true;svg.setPointerCapture(e.pointerId);box.classList.add('drag');box._set(v(e));e.stopPropagation()});
  svg.addEventListener('pointermove',e=>{if(on)box._set(v(e))});
  const up=()=>{on=false;box.classList.remove('drag')};svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up)}
function slSnap(c,x){const s=c.step||1;x=Math.round((x-c.min)/s)*s+c.min;return +Math.max(c.lo!=null?c.lo:c.min,Math.min(c.hi!=null?c.hi:c.max,x)).toFixed(6)}
function slAnim(box,to){if(IA.fast||box._v==null){box._set(to);return}const from=box._v,t0=performance.now();box._an=(box._an||0)+1;const me=box._an;
  (function st(t){if(box._an!==me)return;const p=Math.min(1,(t-t0)/900),q=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;box._set(from+(to-from)*q,p<1);if(p<1)requestAnimationFrame(st)})(t0)}
/* the visible slider control (10MA style): [label] left-end text ───●─── right-end text [value]
   o: min, max, step, lab (name), lt / rt (end labels), set(v) (called on input). Returns {inp, bv, show(v, text)} */
function slCtl(o){const d=iaDiv('i-ctl');
  d.innerHTML=(o.lab?`<span class="i-cl">${o.lab}</span>`:'')+(o.lt?`<span class="i-ce">${o.lt}</span>`:'')+`<input type="range" min="${o.min}" max="${o.max}" step="${o.step}">`+(o.rt?`<span class="i-ce">${o.rt}</span>`:'')+'<b class="i-cv"></b>';
  const inp=d.querySelector('input'),bv=d.querySelector('.i-cv');
  ['pointerdown','click','mousedown','touchstart'].forEach(ev=>d.addEventListener(ev,e=>e.stopPropagation()));
  inp.addEventListener('input',()=>{o.set(+inp.value)});
  return {el:d,inp,bv,show(v,t){inp.value=v;bv.innerHTML=t}}}
/* fences + box plot slider (10MA house prices / walking times). cfg: data, k (index of the moving value), min, max, step, tick, lab (label every),
   lo/hi (slider limits), xl, dec, mode 'fences' | 'box', name, lt, rt (control labels), pre/post (units on values), mm (median + mean lines), vals (value list) */
function fsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,L=40,R=40,bx=c.mode==='box',sx=x=>L+(x-c.min)/(c.max-c.min)*(W-L-R),xs=X=>c.min+(X-L)/(W-L-R)*(c.max-c.min);
  const H=bx?350:(c.xl?286:250),ay=bx?290:220,dec=c.dec!=null?c.dec:2,svg=slSvg(W,H);box.innerHTML='';box.classList.add('i-side');
  const fig=iaDiv('i-fig'),sum=iaDiv('i-sum'),vl=iaDiv('i-vals');if(c.vals===false||(bx&&!c.vals))vl.style.display='none';
  const n=x=>iaNum((+x).toFixed(dec)),f=x=>(c.pre||'')+n(x)+(c.post||'');
  const ctl=slCtl({min:c.lo!=null?c.lo:c.min,max:c.hi!=null?c.hi:c.max,step:c.step||1,lab:c.name||'',lt:c.lt||'',rt:c.rt||'',set:v=>box._set(v)});
  fig.append(vl,svg,ctl.el);box.append(fig,sum);
  box._set=(x,moving)=>{x=moving?+x:slSnap(c,x);box._v=x;const v=c.data.slice();v[c.k]=x;const F=iaFive(v),iqr=F.q3-F.q1,lf=F.q1-1.5*iqr,uf=F.q3+1.5*iqr;
    const out=y=>y<lf-1e-9||y>uf+1e-9,isOut=out(x),ol=F.a.filter(out),mean=v.reduce((s,y)=>s+y,0)/v.length;ctl.show(x,f(x));ctl.bv.classList.toggle('out',isOut);svg.innerHTML='';
    const zt=bx?150:40,zb=bx?250:ay;
    /* the 'not an outlier' zone between the fences */
    const a1=Math.max(c.min,lf),a2=Math.min(c.max,uf);if(a2>a1)svg.append(el('rect',{x:sx(a1),y:zt,width:sx(a2)-sx(a1),height:zb-zt,fill:'#2f6fdf','fill-opacity':.07}));
    /* axis */
    svg.append(el('line',{x1:L-14,x2:W-R+14,y1:ay,y2:ay,stroke:'#333','stroke-width':2}));const tk=c.tick||c.step||1,lb=c.lab||tk;
    for(let t=c.min;t<=c.max+1e-9;t+=tk){const big=Math.abs((t-c.min)/lb-Math.round((t-c.min)/lb))<1e-6;svg.append(el('line',{x1:sx(t),x2:sx(t),y1:ay,y2:ay+(big?10:6),stroke:'#333','stroke-width':big?2:1.2}));
      if(big)svg.append(el('text',{x:sx(t),y:ay+32,'text-anchor':'middle','font-size':19},iaNum(+t.toFixed(6))))}
    if(c.xl)svg.append(el('text',{x:(L+W-R)/2,y:ay+60,'text-anchor':'middle','font-size':20,'font-weight':600,'font-style':'italic'},c.xl));
    const mvc=isOut?'#d2475b':'#d98a1f';
    if(bx){/* the data as dots on top, the moving value as a ring; box plot underneath */
      const seen={};v.forEach((d,j)=>{seen[d]=(seen[d]||0)+1;const me=j===c.k,cy=112-(seen[d]-1)*20;
        svg.append(el('circle',{cx:sx(d),cy,r:me?11:8,fill:me?(isOut?mvc:'#fff'):'#8a93a6',stroke:me?mvc:'none','stroke-width':4,class:me?'i-handle':''}));
        if(me)svg.append(el('text',{x:sx(d),y:cy-20,'text-anchor':'middle','font-size':20,'font-weight':800,fill:isOut?'#b0263a':'#9a5a00'},f(d)))});
      const y=200,bh=50,inl=F.a.filter(y=>!out(y)),lw=inl[0],uw=inl[inl.length-1],sc='#1b1f2a';
      svg.append(el('line',{x1:sx(lw),x2:sx(F.q1),y1:y,y2:y,stroke:sc,'stroke-width':3}),el('line',{x1:sx(F.q3),x2:sx(uw),y1:y,y2:y,stroke:sc,'stroke-width':3}),
        el('line',{x1:sx(lw),x2:sx(lw),y1:y-13,y2:y+13,stroke:sc,'stroke-width':3}),el('line',{x1:sx(uw),x2:sx(uw),y1:y-13,y2:y+13,stroke:sc,'stroke-width':3}),
        el('rect',{x:sx(F.q1),y:y-bh/2,width:sx(F.q3)-sx(F.q1),height:bh,fill:'#cfe0fb',stroke:sc,'stroke-width':3}),el('line',{x1:sx(F.m),x2:sx(F.m),y1:y-bh/2,y2:y+bh/2,stroke:sc,'stroke-width':4}));
      ol.forEach(o=>svg.append(el('circle',{cx:sx(o),cy:y,r:9,fill:'#d2475b'})));
      [[lf,'LF'],[uf,'UF']].forEach(([q,t])=>{if(q<c.min||q>c.max)return;svg.append(el('line',{x1:sx(q),x2:sx(q),y1:zt,y2:zb,stroke:'#2f6fdf','stroke-width':2.5,'stroke-dasharray':'7 5'}),
        el('text',{x:sx(q),y:zb+18,'text-anchor':'middle','font-size':16,'font-weight':800,fill:'#1f4fb0'},t+' = '+n(q)))})}
    else{const r=11,seen={};v.forEach((d,j)=>{seen[d]=(seen[d]||0)+1;const me=j===c.k,cy=ay-r-6-(seen[d]-1)*(2*r+4);
        svg.append(el('circle',{cx:sx(d),cy,r:me?r+2:r,fill:me?(isOut?mvc:'#fff'):(out(d)?'#d2475b':'#555c6b'),stroke:me?mvc:'none','stroke-width':4,class:me?'i-handle':''}));
        if(me)svg.append(el('text',{x:sx(d),y:cy-22,'text-anchor':'middle','font-size':20,'font-weight':800,fill:isOut?'#b0263a':'#9a5a00'},f(d)))});
      if(c.mm)svg.append(el('line',{x1:sx(F.m),x2:sx(F.m),y1:zt+20,y2:ay-2,stroke:'#1b1f2a','stroke-width':3}),el('line',{x1:sx(mean),x2:sx(mean),y1:zt+20,y2:ay-2,stroke:'#d2475b','stroke-width':3,'stroke-dasharray':'5 5'}));
      [[lf,'LF','end',-6],[uf,'UF','start',6]].forEach(([q,t,an,dx])=>{if(q<c.min||q>c.max)return;svg.append(el('line',{x1:sx(q),x2:sx(q),y1:zt-10,y2:ay,stroke:'#2f6fdf','stroke-width':3,'stroke-dasharray':'8 6'}),
        el('text',{x:sx(q)+dx,y:zt-14,'text-anchor':Math.abs(sx(uf)-sx(lf))<200?an:'middle','font-size':18,'font-weight':800,fill:'#1f4fb0'},t+' = '+n(q)))})}
    /* value list (10MA): the moving value is ringed */
    vl.innerHTML='<span class="i-vh">Values</span>'+v.map((d,j)=>`<span class="i-vc${j===c.k?' mv':''}${out(d)?' out':''}">${f(d)}</span>`).join('');
    const lo=x<lf-1e-9,hi=x>uf+1e-9,kv=(k,val,cl='')=>`<div class="i-kv ${cl}"><span>${k}</span><b>${val}</b></div>`;
    sum.innerHTML=(bx?kv('Min',f(F.min))+kv('Q<sub>1</sub>',f(F.q1))+kv('Median',f(F.m))+kv('Q<sub>3</sub>',f(F.q3))+kv('Max',f(F.max)):kv('Q<sub>1</sub>',f(F.q1))+kv('Q<sub>3</sub>',f(F.q3)))+
      kv('IQR = Q<sub>3</sub> − Q<sub>1</sub>',n(iqr))+kv('LF = Q<sub>1</sub> − 1.5 × IQR',f(lf),'fz')+kv('UF = Q<sub>3</sub> + 1.5 × IQR',f(uf),'fz')+
      `<div class="i-rules"><div class="i-rule${lo?' on':''}"><i>x</i> &lt; LF → outlier</div><div class="i-rule${hi?' on':''}"><i>x</i> &gt; UF → outlier</div></div>`+
      `<div class="i-ol">Outlier: ${ol.length?'<b class="no">'+ol.map(f).join(', ')+'</b>':'<b class="ok">none</b>'}</div>`+
      (c.mm&&!bx?`<div class="i-mm"><span class="ln"></span> Median <b>${f(F.m)}</b> <span class="ln mean"></span> Mean <b>${f(+mean.toFixed(dec))}</b></div>`:'')+
      (bx?'<div class="i-sm">The whisker stops at the last value that is <b>not</b> an outlier.</div>':'')};
  slDrag(box,svg,X=>slSnap(c,xs(X)));box._v0=c.data[c.k];box._set(box._v0)}
/* normal-curve z slider. cfg: m, s, step (default s/2), xl, dec, W, name, lt, rt */
const IAPCT={'-3':0.15,'-2':2.5,'-1':16,'0':50,'1':84,'2':97.5,'3':99.85};
function zsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=310,L=30,R=30,T=40,base=230,sx=z=>L+(z+3.6)/7.2*(W-L-R),sy=z=>base-Math.exp(-z*z/2)*(base-T),dec=c.dec!=null?c.dec:2;
  c.min=c.m-3.5*c.s;c.max=c.m+3.5*c.s;c.lo=c.m-3*c.s;c.hi=c.m+3*c.s;c.step=c.step||c.s/2;const svg=slSvg(W,H);box.innerHTML='';const rd=iaDiv('i-read');
  const f=x=>iaNum((+x).toFixed(dec)),ctl=slCtl({min:c.lo,max:c.hi,step:c.step,lab:c.name||'',lt:c.lt||f(c.lo),rt:c.rt||f(c.hi),set:v=>box._set(v)});box.append(svg,ctl.el,rd);
  box._set=(x,moving)=>{x=moving?+x:slSnap(c,x);box._v=x;const z=(x-c.m)/c.s;ctl.show(x,'x = '+f(x));svg.innerHTML='';
    let d=`M${sx(-3.6)},${base}`;for(let k=0;k<=120;k++){const zz=-3.6+(z+3.6)*k/120;d+=` L${sx(zz).toFixed(1)},${sy(zz).toFixed(1)}`}svg.append(el('path',{d:d+` L${sx(z)},${base} Z`,fill:'rgba(79,132,230,.38)'}));
    for(let k=-3;k<=3;k++)svg.append(el('line',{x1:sx(k),x2:sx(k),y1:base,y2:sy(k),stroke:'#8a93a6','stroke-width':k?1.2:2,'stroke-dasharray':k?'5 4':''}));
    let p='';for(let k=0;k<=200;k++){const zz=-3.6+7.2*k/200;p+=(k?' L':'M')+sx(zz).toFixed(1)+','+sy(zz).toFixed(1)}svg.append(el('path',{d:p,fill:'none',stroke:'#1f4fb0','stroke-width':3}));
    svg.append(el('line',{x1:L,x2:W-R,y1:base,y2:base,stroke:'#333','stroke-width':2}));
    for(let k=-3;k<=3;k++){svg.append(el('text',{x:sx(k),y:base+26,'text-anchor':'middle','font-size':18},f(c.m+k*c.s)),el('text',{x:sx(k),y:base+52,'text-anchor':'middle','font-size':17,'font-weight':600,fill:'#5b33b0'},'z = '+iaNum(k)))}
    if(c.xl)svg.append(el('text',{x:W/2,y:H-4,'text-anchor':'middle','font-size':19,'font-weight':600,'font-style':'italic'},c.xl));
    const hx=sx(z);svg.append(el('line',{x1:hx,x2:hx,y1:T-14,y2:base,stroke:'#d98a1f','stroke-width':4}),el('path',{d:`M${hx},${base-2} l-12,-22 h24 z`,fill:'#d98a1f',class:'i-handle'}),
      el('text',{x:hx,y:T-20,'text-anchor':'middle','font-size':20,'font-weight':800,fill:'#9a5a00'},'x = '+f(x)));
    const zr=Math.round(z*1e6)/1e6,pc=IAPCT[String(zr)];
    rd.innerHTML=`<div><i>z</i> = <span class="i-fr"><span><i>x</i> − <i>x̄</i></span><span><i>s</i></span></span> = <span class="i-fr"><span>${f(x)} − ${f(c.m)}</span><span>${f(c.s)}</span></span> = <b>${iaNum(zr)}</b></div>`+
      (pc!=null?`<div>68–95–99.7% rule: <b>${pc}%</b> of values lie below <i>x</i> = ${f(x)}, <b>${iaNum(+(100-pc).toFixed(2))}%</b> above</div>`
        :`<div class="i-sm">${f(x)} is ${iaNum(Math.abs(zr))} standard deviations ${zr<0?'below':'above'} the mean: the 68–95–99.7% rule works only at whole numbers of standard deviations</div>`)};
  slDrag(box,svg,X=>slSnap(c,c.m+((X-L)/(W-L-R)*7.2-3.6)*c.s));box._v0=c.x0!=null?c.x0:c.m+c.s;box._set(box._v0)}
/* log slider: drag x from 10^lo to 10^hi; the log axis is even, the x axis is not. cfg: lo, hi, x0, xl, W */
const iaSp=x=>x>=1e4?Math.round(x).toLocaleString('en-AU').replace(/,/g,' '):String(+x.toPrecision(3));
function lsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=230,L=60,R=60,sx=p=>L+(p-c.lo)/(c.hi-c.lo)*(W-L-R),y1=70,y2=170;box.innerHTML='';const svg=slSvg(W,H);
  const rd=iaDiv('i-read');c.min=c.lo;c.max=c.hi;c.step=c.step||0.01;const sp=iaSp;
  const ctl=slCtl({min:c.lo,max:c.hi,step:c.step,lab:'log₁₀(x)',lt:sp(Math.pow(10,c.lo)),rt:sp(Math.pow(10,c.hi)),set:v=>box._set(v)});box.append(svg,ctl.el,rd);
  box._set=(p)=>{p=Math.max(c.lo,Math.min(c.hi,+p));box._v=p;const x=Math.pow(10,p);ctl.show(p,'x = '+sp(x));svg.innerHTML='';
    svg.append(el('text',{x:10,y:y1-34,'font-size':18,'font-weight':800,fill:'#5b33b0'},'log₁₀(x)'),el('text',{x:10,y:y2+56,'font-size':18,'font-weight':800,fill:'#1f4fb0'},c.xl||'x'));
    [y1,y2].forEach(y=>svg.append(el('line',{x1:L-10,x2:W-R+10,y1:y,y2:y,stroke:'#333','stroke-width':2})));
    for(let k=Math.ceil(c.lo);k<=c.hi;k++){svg.append(el('line',{x1:sx(k),x2:sx(k),y1:y1-8,y2:y2+8,stroke:'#e3e6ee','stroke-width':1.5}),
      el('text',{x:sx(k),y:y1-14,'text-anchor':'middle','font-size':19,'font-weight':600,fill:'#5b33b0'},k),el('text',{x:sx(k),y:y2+30,'text-anchor':'middle','font-size':18,fill:'#1f4fb0'},sp(Math.pow(10,k))));
      for(let m=2;m<10&&k+Math.log10(m)<=c.hi;m++)svg.append(el('line',{x1:sx(k+Math.log10(m)),x2:sx(k+Math.log10(m)),y1:y2,y2:y2+7,stroke:'#555','stroke-width':1}))}
    const hx=sx(p);svg.append(el('line',{x1:hx,x2:hx,y1:y1,y2:y2,stroke:'#d98a1f','stroke-width':4}),el('circle',{cx:hx,cy:y1,r:10,fill:'#d98a1f',class:'i-handle'}),el('circle',{cx:hx,cy:y2,r:10,fill:'#d98a1f',class:'i-handle'}));
    rd.innerHTML=`<div><i>x</i> = <b>${sp(x)}</b> &nbsp;⟷&nbsp; log<sub>10</sub>(${sp(x)}) = <b>${p.toFixed(2)}</b> &nbsp;·&nbsp; 10<sup>${p.toFixed(2)}</sup> = ${sp(x)}</div><div class="i-sm">Each step of 1 on the log scale multiplies <i>x</i> by 10.</div>`};
  slDrag(box,svg,X=>Math.round((c.lo+(X-L)/(W-L-R)*(c.hi-c.lo))/c.step)*c.step);box._v0=c.x0!=null?Math.log10(c.x0):(c.lo+c.hi)/2;box._set(box._v0)}
/* shape slider: drag left/right to skew a histogram; mean (dashed) and median (solid) follow. cfg: v0 (−1…1), W */
function shBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=300,L=40,R=40,B=30,T=30,N=11,w=(W-L-R)/N;box.innerHTML='';const svg=slSvg(W,H);
  const rd=iaDiv('i-read'),ctl=slCtl({min:-1,max:1,step:0.05,lt:'Tail to the left',rt:'Tail to the right',set:v=>box._set(v)});box.append(svg,ctl.el,rd);
  box._set=(a,moving)=>{a=Math.max(-1,Math.min(1,+a));if(!moving)a=Math.round(a*20)/20;box._v=a;
    let fr=[...Array(N).keys()].map(k=>{const x=(k+.5)/N,p=3+9*Math.max(0,-a),q=3+9*Math.max(0,a);return Math.pow(x,p-1)*Math.pow(1-x,q-1)});const mx=Math.max(...fr);fr=fr.map(v=>Math.round(v/mx*12));
    const n=fr.reduce((s,v)=>s+v,0),mean=fr.reduce((s,v,k)=>s+v*k,0)/n;let cu=0,med=0;for(let k=0;k<N;k++){if(cu+fr[k]>=n/2){med=k-.5+(n/2-cu)/fr[k];break}cu+=fr[k]}
    const X=v=>L+(v+.5)*w,Y=v=>H-B-v/12*(H-B-T),sym=Math.abs(a)<.12,nm=sym?'symmetric':a>0?'positively skewed':'negatively skewed';ctl.show(a,nm);svg.innerHTML='';
    fr.forEach((v,k)=>svg.append(el('rect',{x:L+k*w,y:Y(v),width:w,height:H-B-Y(v),fill:'#4f84e6',stroke:'#1f4fb0','stroke-width':1.5})));
    svg.append(el('line',{x1:L,x2:W-R,y1:H-B,y2:H-B,stroke:'#333','stroke-width':2}),el('line',{x1:X(med),x2:X(med),y1:T-10,y2:H-B,stroke:'#1f9e74','stroke-width':4}),
      el('line',{x1:X(mean),x2:X(mean),y1:T-10,y2:H-B,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'10 6'}));
    if(!sym){const y0=T+30,x1=a>0?X(med)+30:X(med)-30,x2=a>0?W-R-8:L+8;svg.append(el('line',{x1,x2,y1:y0,y2:y0,stroke:'#d98a1f','stroke-width':4}),
      el('path',{d:a>0?`M${x2},${y0} l-14,-9 v18 z`:`M${x2},${y0} l14,-9 v18 z`,fill:'#d98a1f'}),el('text',{x:(x1+x2)/2,y:y0-10,'text-anchor':'middle','font-size':19,'font-weight':800,fill:'#9a5a00'},'tail'))}
    rd.innerHTML=`<div>The distribution is <b>${nm}</b>.</div><div><span style="color:#1f9e74;font-weight:800">median ${med.toFixed(1)}</span> · <span style="color:#d2475b;font-weight:800">mean ${mean.toFixed(1)}</span> · `+
      (sym?'mean ≈ median':a>0?'the tail pulls the mean <b>above</b> the median':'the tail pulls the mean <b>below</b> the median')+'</div>'};
  slDrag(box,svg,X=>((X-L)/(W-L-R))*2-1);box._v0=c.v0||0;box._set(box._v0)}

/* ===== 3. card sort (10MA 'Sort it'): Step 1 buttons on each card; a right answer turns green and opens Step 2 for that card's group ===== */
function csInit(b){b.addEventListener('click',e=>{e.stopPropagation();const bt=e.target.closest('button');if(!bt)return;
    if(bt.classList.contains('i-reset')){csReset(b);return}const cd=bt.closest('.i-card');if(!cd)return;
    if(bt.closest('.i-r1'))csPick(b,cd,1,bt);else csPick(b,cd,2,bt)});
  b.addEventListener('pointerdown',e=>e.stopPropagation())}
function csScore(b){const all=b.querySelectorAll('.i-card'),done=b.querySelectorAll('.i-card.done').length;b.querySelector('.i-score b').textContent=done;b.querySelector('.i-score .i-of').textContent=all.length}
function csPick(b,cd,lv,bt,rev){const ans=cd.dataset.a.split('/'),row=cd.querySelector(lv===1?'.i-r1':'.i-r2'),want=ans[lv-1];
  const right=bt.dataset.v===want;
  if(lv===1){cd.querySelectorAll('.i-r1 button,.i-r2 button').forEach(x=>{x.classList.remove('ok','rv');if(!rev)x.classList.remove('no')});cd.classList.remove('s2','done');cd.style.removeProperty('--cc')}
  else row.querySelectorAll('button').forEach(x=>{x.classList.remove('ok','rv');if(!rev)x.classList.remove('no')});
  if(right){bt.classList.add(rev?'rv':'ok');
    if(lv===1){cd.style.setProperty('--cc',bt.dataset.c||'var(--yt)');if(ans.length>1){cd.classList.add('s2');cd.querySelectorAll('.i-o').forEach(o=>o.classList.toggle('on',o.dataset.g===want))}else cd.classList.add('done')}
    else cd.classList.add('done')}
  else{void bt.offsetWidth;bt.classList.add('no');if(lv===1)cd.dataset.w1=1;else cd.dataset.w2=1}
  csScore(b)}
function csReveal(b,lv,which){const cards=[...b.querySelectorAll('.i-card')];const ks=which?which.split(',').map(Number):cards.map((_,k)=>k);
  ks.forEach(k=>{const cd=cards[k];if(!cd)return;const ans=cd.dataset.a.split('/');
    if(lv===1&&!cd.querySelector('.i-r1 button.ok')){const bt=cd.querySelector(`.i-r1 button[data-v="${CSS.escape(ans[0])}"]`);if(bt)csPick(b,cd,1,bt,1)}
    if(lv>=2&&ans.length>1){if(!cd.classList.contains('s2')&&!cd.classList.contains('done'))csReveal(b,1,String(k));
      if(!cd.classList.contains('done')){const bt=cd.querySelector(`.i-o.on button[data-v="${CSS.escape(ans[1])}"]`);if(bt)csPick(b,cd,2,bt,1)}}})}
function csReset(b){b.querySelectorAll('.i-card').forEach(cd=>{cd.classList.remove('s2','done');cd.style.removeProperty('--cc');delete cd.dataset.w1;delete cd.dataset.w2;
  cd.querySelectorAll('button').forEach(x=>x.classList.remove('ok','no','rv'));cd.querySelectorAll('.i-o').forEach(o=>o.classList.remove('on'))});csScore(b)}

/* ===== 5. two tests: which result is relatively better? (z-scores) ===== cfg: A {n,m,s,x,st}, B {…}, dec, xl, W */
function ztBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||640,H=250,L=20,R=20,T=34,base=176,sx=z=>L+(z+3.6)/7.2*(W-L-R),sy=z=>base-Math.exp(-z*z/2)*(base-T),dec=c.dec!=null?c.dec:1;
  const f=x=>iaNum((+x).toFixed(dec)),zf=z=>iaNum((+z).toFixed(2));box.innerHTML='';const row=iaDiv('i-zrow'),vd=iaDiv('i-zverdict');box.append(row,vd);const P={};
  ['A','B'].forEach((k,j)=>{const t=c[k],col=j?'#7b3fbf':'#2f6fdf',pan=iaDiv('i-zpan'),svg=slSvg(W,H);t.st=t.st||t.s/10;t.lo=t.m-3.4*t.s;t.hi=t.m+3.4*t.s;
    const hd=iaDiv('i-zhd',`<b style="color:${col}">${t.n}</b> <span>mean ${f(t.m)} · SD ${f(t.s)}</span>`),rd=iaDiv('i-zrd');
    const ctl=slCtl({min:+t.lo.toFixed(6),max:+t.hi.toFixed(6),step:t.st,lab:'score',set:v=>{P[k].set(v);ztVerdict()}});pan.append(hd,svg,ctl.el,rd);row.append(pan);
    P[k]={set(x){x=Math.max(t.lo,Math.min(t.hi,+x));P[k].x=x;const z=(x-t.m)/t.s;P[k].z=z;ctl.show(x,f(x));svg.innerHTML='';
      let d=`M${sx(-3.6)},${base}`;for(let q=0;q<=100;q++){const zz=-3.6+(z+3.6)*q/100;d+=` L${sx(zz).toFixed(1)},${sy(zz).toFixed(1)}`}svg.append(el('path',{d:d+` L${sx(z)},${base} Z`,fill:col,'fill-opacity':.22}));
      let p='';for(let q=0;q<=160;q++){const zz=-3.6+7.2*q/160;p+=(q?' L':'M')+sx(zz).toFixed(1)+','+sy(zz).toFixed(1)}svg.append(el('path',{d:p,fill:'none',stroke:col,'stroke-width':3}));
      svg.append(el('line',{x1:L,x2:W-R,y1:base,y2:base,stroke:'#333','stroke-width':2}));
      for(let q=-3;q<=3;q++){svg.append(el('line',{x1:sx(q),x2:sx(q),y1:base,y2:base+6,stroke:'#333'}),el('text',{x:sx(q),y:base+24,'text-anchor':'middle','font-size':15},f(t.m+q*t.s)),
        el('text',{x:sx(q),y:base+44,'text-anchor':'middle','font-size':14,'font-weight':600,fill:'#5b33b0'},'z = '+iaNum(q)))}
      const hx=sx(Math.max(-3.6,Math.min(3.6,z)));svg.append(el('line',{x1:hx,x2:hx,y1:T-10,y2:base,stroke:'#d98a1f','stroke-width':4}),el('text',{x:hx,y:T-14,'text-anchor':'middle','font-size':17,'font-weight':800,fill:'#9a5a00'},'x = '+f(x)));
      rd.innerHTML=`<i>z</i> = <span class="i-fr"><span>${f(x)} − ${f(t.m)}</span><span>${f(t.s)}</span></span> = <b style="color:${col}">${zf(z)}</b>`}};
    slDrag({_set:v=>{P[k].set(Math.round(v/t.st)*t.st);ztVerdict()},classList:box.classList},svg,X=>t.m+((X-L)/(W-L-R)*7.2-3.6)*t.s)});
  function ztVerdict(){const a=P.A.z,b=P.B.z,A=c.A.n,B=c.B.n,d=Math.abs(a-b)<1e-9;
    vd.innerHTML=`<span><i>z</i><sub>${A}</sub> = <b>${zf(a)}</b> &nbsp; <i>z</i><sub>${B}</sub> = <b>${zf(b)}</b></span><span class="i-zv">`+(d?`Same <i>z</i>-score: equally good on both`:
      `${zf(Math.max(a,b))} &gt; ${zf(Math.min(a,b))} → relatively better on <b>${a>b?A:B}</b>`)+'</span>'}
  box._P=P;box._set2=(xa,xb)=>{if(xa!=null)P.A.set(xa);if(xb!=null)P.B.set(xb);ztVerdict()};
  box._v0=[c.A.x!=null?c.A.x:c.A.m,c.B.x!=null?c.B.x:c.B.m];box._set2(...box._v0)}
function ztAnim(box,xa,xb){const a0=box._P.A.x,b0=box._P.B.x,ta=xa!=null?xa:a0,tb=xb!=null?xb:b0;if(IA.fast){box._set2(ta,tb);return}
  const t0=performance.now();box._an=(box._an||0)+1;const me=box._an;(function st(t){if(box._an!==me)return;const p=Math.min(1,(t-t0)/900),q=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
    box._set2(a0+(ta-a0)*q,b0+(tb-b0)*q);if(p<1)requestAnimationFrame(st)})(t0)}

/* ===== 6. plinko / Galton board: balls bounce left or right at every peg and pile up in a bell shape ===== cfg: rows, W, fill (balls in the replay/PDF pile), note */
function pkBuild(box){const c=JSON.parse(box.dataset.cfg),R=c.rows||10,W=c.W||900,B=R+1,L=30,bw=(W-2*L)/B,cx=W/2,top=40,rh=c.rh||26,py=r=>top+30+r*rh,binTop=py(R)+6,binH=c.binH||250,H=binTop+binH+30;
  const per=Math.max(3,Math.floor(bw/16)),br=Math.min(7.5,bw/per/2-.6);box.innerHTML='';const fig=iaDiv('i-pkfig'),side=iaDiv('i-pkside'),svg=slSvg(W,H);fig.append(svg);box.append(fig,side);
  side.innerHTML=`<div class="i-pkbtns"><button data-n="1">Drop 1</button><button data-n="50">Drop 50</button><button data-n="0" class="i-reset">Reset</button></div>`+
    `<div class="i-pkn">Balls dropped: <b>0</b></div><div class="i-pknote">${c.note||'Most balls land near the <b>middle</b>; fewer land further out. The pile makes a <b>bell shape</b>.'}</div>`;
  side.addEventListener('click',e=>{e.stopPropagation();const bt=e.target.closest('button');if(!bt)return;const n=+bt.dataset.n;if(!n)pkReset(box);else pkDrop(box,n)});
  side.addEventListener('pointerdown',e=>e.stopPropagation());
  /* pegs */
  const pg=el('g',{});for(let r=0;r<R;r++)for(let j=0;j<=r;j++)pg.append(el('circle',{cx:cx+(j-r/2)*bw,cy:py(r),r:4.5,fill:'#555c6b'}));
  svg.append(el('path',{d:`M${cx-26},${top-26} L${cx-8},${top+10} M${cx+26},${top-26} L${cx+8},${top+10}`,stroke:'#8a93a6','stroke-width':3,fill:'none'}),pg);
  for(let k=0;k<=B;k++)svg.append(el('line',{x1:L+k*bw,x2:L+k*bw,y1:binTop,y2:binTop+binH,stroke:'#c9ced9','stroke-width':2}));
  svg.append(el('line',{x1:L,x2:W-L,y1:binTop+binH,y2:binTop+binH,stroke:'#333','stroke-width':2.5}));
  const pile=el('g',{}),lab=el('g',{}),fly=el('g',{});svg.append(pile,lab,fly);
  box._k={R,B,bw,cx,L,py,binTop,binH,per,br,pile,lab,fly,top,rh,cnt:Array(B).fill(0),fill:c.fill||200};pkDraw(box)}
function pkDraw(box){const k=box._k,tot=k.cnt.reduce((a,b)=>a+b,0),mx=Math.max(...k.cnt),cap=Math.floor(k.binH/(2*k.br))*k.per;k.pile.innerHTML='';k.lab.innerHTML='';
  const bars=mx>cap;k.cnt.forEach((n,b)=>{const x0=k.L+b*k.bw,y0=k.binTop+k.binH;
    if(bars){const h=n/mx*(k.binH-4);k.pile.append(el('rect',{x:x0+3,y:y0-h,width:k.bw-6,height:h,fill:'#4f84e6',stroke:'#1f4fb0','stroke-width':1.5}))}
    else for(let i=0;i<n;i++){const row=Math.floor(i/k.per),col=i%k.per,off=(k.bw-k.per*2*k.br)/2;k.pile.append(el('circle',{cx:x0+off+k.br+col*2*k.br,cy:y0-k.br-row*2*k.br,r:k.br-.4,fill:'#d98a1f'}))}
    k.lab.append(el('text',{x:x0+k.bw/2,y:y0+22,'text-anchor':'middle','font-size':16,'font-weight':700,fill:'#555c6b'},n))});
  const nb=box.querySelector('.i-pkn b');if(nb)nb.textContent=tot}
function pkReset(box){const k=box._k;k.gen=(k.gen||0)+1;k.cnt.fill(0);k.fly.innerHTML='';pkDraw(box)}
function pkBinom(k,n){const R=k.R,C=[1];for(let j=1;j<=R;j++)C[j]=C[j-1]*(R-j+1)/j;const e=C.map(x=>x*n/Math.pow(2,R)),f=e.map(Math.floor);let left=n-f.reduce((a,b)=>a+b,0);
  e.map((x,j)=>[x-f[j],j]).sort((a,b)=>b[0]-a[0]||Math.abs(a[1]-R/2)-Math.abs(b[1]-R/2)).forEach(([_,j])=>{if(left>0){f[j]++;left--}});return f}
function pkDrop(box,n,fast){const k=box._k;if(fast||IA.fast){pkBinom(k,n).forEach((x,j)=>k.cnt[j]+=x);pkDraw(box);return}
  const gen=k.gen||0;for(let q=0;q<n;q++){const t=setTimeout(()=>{if((k.gen||0)!==gen)return;pkBall(box,gen)},q*(n>1?70:0));IA.T.push(t)}}
function pkBall(box,gen){const k=box._k,path=[0];let r=0;for(let j=0;j<k.R;j++)path.push(path[j]+(Math.random()<.5?0:1));
  const ball=el('circle',{r:k.br,fill:'#d2475b'});k.fly.append(ball);const xr=(j,i)=>k.cx+(i-j/2)*k.bw,t0=performance.now(),dt=95;
  const P=j=>j<0?[k.cx,k.top]:[xr(j,path[j]),k.py(j)];
  (function st(t){if((k.gen||0)!==gen){ball.remove();return}const u=(t-t0)/dt,j=Math.floor(u),fr=u-j;
    if(j>k.R){ball.remove();k.cnt[path[k.R]]++;pkDraw(box);return}
    const a=P(j-1),b=P(j),x=a[0]+(b[0]-a[0])*fr,y=a[1]+(b[1]-a[1])*fr-(j<k.R?Math.sin(fr*Math.PI)*8:0)-k.br-4;
    ball.setAttribute('cx',x);ball.setAttribute('cy',y);requestAnimationFrame(st)})(t0)}

/* ===== 7. rounder: decimal places vs significant figures ===== cfg: v (the number, as a string), mode 'dp'|'sf', n */
function rdRound(str,mode,n){let neg=str.trim()[0]==='-';let s=str.trim().replace(/^[-+]/,'');if(!s.includes('.'))s+='.';let [ip,fp]=s.split('.');
  const D=(ip+fp).split('').map(Number),p=ip.length;let j;
  if(mode==='dp')j=p-1+n;else{const f=D.findIndex(d=>d>0);if(f<0)return {txt:'0',j:-1,dec:-1,up:false};j=f+n-1}
  const dec=j+1<D.length?j+1:-1,dd=dec>=0?D[dec]:0,up=dd>=5;let K=D.slice(0,Math.max(0,j+1));while(K.length<j+1)K.push(0);
  let pp=p;if(up){let q=K.length-1;while(q>=0){if(K[q]<9){K[q]++;break}K[q]=0;q--}if(q<0){K.unshift(1);pp++;j++}}
  if(j<pp-1){while(K.length<pp)K.push(0)}
  let ipart=K.slice(0,pp).join('').replace(/^0+(?=\d)/,'')||'0',fpart=K.slice(pp).join('');
  return {txt:(neg?'−':'')+ipart+(fpart?'.'+fpart:''),j:mode==='dp'?p-1+n:j-(pp-p),dec,up,dd}}
function rdBuild(box){const c=JSON.parse(box.dataset.cfg);box.innerHTML='';box._v0=[c.mode||'dp',c.n!=null?c.n:2];
  const s=String(c.v);let html='',di=0;for(const ch of s){if(/\d/.test(ch)){html+=`<span class="i-rd" data-i="${di}">${ch}</span>`;di++}else html+=`<span class="i-rp">${ch==='-'?'−':ch}</span>`}
  box.innerHTML=`<div class="i-rtop"><div class="i-rmode"><button data-m="dp">Decimal places</button><button data-m="sf">Significant figures</button></div>`+
    `<div class="i-rcount"><button data-d="-1">−</button><input type="range" min="0" max="4" step="1"><button data-d="1">+</button><b class="i-rn"></b></div></div>`+
    `<div class="i-rnum">${html}</div><div class="i-rdec"></div><div class="i-rres"></div>`;
  const inp=box.querySelector('input');['pointerdown','mousedown','touchstart'].forEach(ev=>box.addEventListener(ev,e=>e.stopPropagation()));
  box.addEventListener('click',e=>{e.stopPropagation();const b=e.target.closest('button');if(!b)return;if(b.dataset.m)box._set(b.dataset.m,box._n);else box._set(box._m,box._n+ +b.dataset.d)});
  inp.addEventListener('input',()=>box._set(box._m,+inp.value));
  box._set=(m,n)=>{n=Math.max(m==='sf'?1:0,Math.min(4,+n));box._m=m;box._n=n;inp.min=m==='sf'?1:0;inp.value=n;
    box.querySelectorAll('.i-rmode button').forEach(b=>b.classList.toggle('on',b.dataset.m===m));
    const word=m==='dp'?(n===1?'decimal place':'decimal places'):(n===1?'significant figure':'significant figures');box.querySelector('.i-rn').textContent=n+' '+word;
    const r=rdRound(s,m,n),ds=[...box.querySelectorAll('.i-rd')],first=ds.findIndex(d=>+d.textContent>0);
    ds.forEach((d,i)=>{d.className='i-rd'+(i<=r.j?(m==='sf'&&i<first?' lz':' keep'):'')+(i===r.dec?' dec':'')+(i>r.j&&i!==r.dec?' gone':'')});
    box.querySelector('.i-rdec').innerHTML=r.dec>=0?`Deciding digit: <b class="dd">${r.dd}</b> → ${r.up?'5 or more: <b>round up</b>':'less than 5: <b>keep</b> the last digit'}`
      :'No digit after the last one kept: nothing to round.';
    box.querySelector('.i-rres').innerHTML=`${s.replace('-','−')} ≈ <b>${r.txt}</b> <span>(${n} ${word})</span>`};
  box._set(...box._v0)}

/* ===== 8. normal curve (tpl.js drawNorm): lift the % labels clear of the curve · hooked 68/95/99.7% brackets ===== */
function nbFix(box){const g=box._g,s=box.querySelector('svg');if(!g||!s)return;const c=JSON.parse(box.dataset.cfg);
  s.querySelectorAll('g.npct text').forEach(t=>{const x=+t.getAttribute('x'),w=t.textContent.length*(g.fs-2)*.62/2+6,z1=(x-w-g.L)/g.pw*7.2-3.6,z2=(x+w-g.L)/g.pw*7.2-3.6;
    let top=Infinity;for(let q=0;q<=12;q++){const z=z1+(z2-z1)*q/12;top=Math.min(top,g.sy(z))}let y=Math.min(top-8,+t.getAttribute('y'));
    /* no room above (small chart): inside the band, under the curve */
    if(y<g.fs-2){const zc=(x-g.L)/g.pw*7.2-3.6;y=(g.base+g.sy(zc))/2+(g.fs-2)/3}t.setAttribute('y',y.toFixed(1))});
  if(!c.br)return;const ks=c.br===true||c.br===1?[1,2,3]:c.br,lb={1:'68%',2:'95%',3:'99.7%'},gap=30,y0=g.H+8,cl='#5b33b0';
  s.setAttribute('viewBox',`0 0 ${g.W} ${g.H+ks.length*gap+12}`);const G=el('g',{class:'nbr'});
  ks.forEach((k,j)=>{const y=y0+j*gap+14,a=g.sx(-k),b=g.sx(k),m=(a+b)/2,tw=lb[k].length*(g.fs)*.62/2+10,bk=el('g',{class:'nb'+k});
    bk.append(el('path',{d:`M${a},${y-10} V${y} H${m-tw} M${m+tw},${y} H${b} V${y-10}`,fill:'none',stroke:cl,'stroke-width':2.5}),
      el('text',{x:m,y:y+6,'text-anchor':'middle','font-size':g.fs,'font-weight':800,fill:cl},lb[k]));G.append(bk)});s.append(G);nbHide(box)}
function nbHide(box){let c={};try{c=JSON.parse(box.dataset.cfg)}catch(e){}box.querySelectorAll('g.nbr > g').forEach(e=>e.style.opacity=c.brhide?0:1)}
/* ===== 4. stem plot built leaf by leaf · tally into a frequency table ===== */
function iaIdx(s,n){if(s==='all'||s==null||s==='')return [...Array(n).keys()];const o=[];s.split(',').forEach(p=>{const m=p.split('-');if(m.length===2)for(let k=+m[0];k<=+m[1];k++)o.push(k);else o.push(+p)});return o}
function sfReset(b){b.querySelectorAll('.i-lf').forEach(l=>{l.classList.remove('on');l.style.transform='';l.style.order=l.dataset.k});b.querySelectorAll('.i-sch').forEach(c=>c.classList.remove('used'))}
function sfFly(b,k,delay){const c=b.querySelector(`.i-sch[data-k="${k}"]`),l=b.querySelector(`.i-lf[data-k="${k}"]`);if(!c||!l)return;
  iaLater(()=>{if(IA.fast){l.classList.add('on');c.classList.add('used');return}const r1=c.getBoundingClientRect(),r2=l.getBoundingClientRect(),sc=iaS();
    l.style.transition='none';l.style.transform=`translate(${(r1.left-r2.left)/sc}px,${(r1.top-r2.top)/sc}px) scale(1.2)`;l.classList.add('on','fly');c.classList.add('used');void l.offsetWidth;
    l.style.transition='';l.style.transform='';setTimeout(()=>l.classList.remove('fly'),700)},delay)}
function sfSort(b){b.querySelectorAll('.i-lvw').forEach(w=>{[...w.querySelectorAll('.i-lf')].sort((x,y)=>x.dataset.l-y.dataset.l||x.dataset.k-y.dataset.k).forEach((l,j)=>{l.style.order=j;if(!IA.fast){l.classList.add('fly');setTimeout(()=>l.classList.remove('fly'),500)}})})}
function ftReset(t){t.querySelectorAll('td.i-fq').forEach(c=>{c.textContent='';c.classList.remove('on')});t.querySelectorAll('tr').forEach(r=>r.classList.remove('hy'))}
function ftTally(ch,t,i){ch.querySelectorAll('.i-dch.on').forEach(x=>{x.classList.remove('on');x.classList.add('done')});t.querySelectorAll('tr.hy').forEach(r=>r.classList.remove('hy'));
  const xs=[...ch.querySelectorAll(`.i-dch[data-b="${i}"]`)],cell=t.querySelector(`td.i-fq[data-i="${i}"]`),row=cell&&cell.closest('tr');if(row)row.classList.add('hy');
  if(cell){cell.textContent='0';cell.classList.add('on')}xs.forEach((x,k)=>iaLater(()=>{x.classList.add('on');if(cell)cell.textContent=k+1},IA.fast?0:150+k*170));if(!xs.length&&cell)cell.textContent='0'}


/* ===== hooks: called by the engine's apply(s,f) / reset(s) ===== */
function iaapply(s,f){const d=f.dataset;
  tlApply(f);
  iaEach(d.fset,(b,p)=>slAnim(b,b.classList.contains('i-log')?Math.log10(+p[0]):+p[0]));
  iaEach(d.shset,(b,p)=>slAnim(b,+p[0]));
  iaEach(d.sreveal,(b,p)=>csReveal(b,+p[0]||1,p[1]||''));
  iaEach(d.leaf,(b,p)=>{const n=b.querySelectorAll('.i-lf').length;iaIdx(p[0],n).forEach((k,j)=>sfFly(b,k,j*180))});
  iaEach(d.lsort,(b)=>sfSort(b));
  if(d.ftally){const [c,t,i]=d.ftally.split('|');const ch=document.querySelector(c),tb=document.querySelector(t);if(ch&&tb)ftTally(ch,tb,i)}
  iaEach(d.ftot,(t)=>{const c=t.querySelector('td.i-ftot');if(c){c.textContent=[...t.querySelectorAll('td.i-fq')].reduce((a,x)=>a+(+x.dataset.n||0),0);c.classList.add('on')}
    t.querySelectorAll('tr.hy').forEach(r=>r.classList.remove('hy'));document.querySelectorAll('.i-dch.on').forEach(x=>{x.classList.remove('on');x.classList.add('done')})});
  iaEach(d.fgrow,(ch,p)=>p[0].split(',').forEach(i=>{const r=ch.querySelector(`rect.grow[data-i="${i}"]`);if(r)grow(r)}));
  iaEach(d.ztset,(b,p)=>ztAnim(b,p[0]===''||p[0]==null?null:+p[0],p[1]===''||p[1]==null?null:+p[1]));
  iaEach(d.plk,(b,p)=>{const n=+p[0];if(!n)pkReset(b);else pkDrop(b,n,p[1]==='now')});
  iaEach(d.rset,(b,p)=>b._set(p[0],+p[1]));
  iaEach(d.nbr,(b,p)=>(p[0]||'1,2,3').split(',').forEach(k=>{const g=b.querySelector('g.nbr > g.nb'+k);if(g)g.style.opacity=1}))}
function iareset(s){IA.T.splice(0).forEach(clearTimeout);
  s.querySelectorAll('.i-tiles').forEach(tlReset);
  s.querySelectorAll('.i-slider').forEach(b=>{b._an=(b._an||0)+1;b._v=null;if(b._set)b._set(b._v0)});
  s.querySelectorAll('.i-sort').forEach(csReset);
  s.querySelectorAll('.i-stem').forEach(sfReset);
  s.querySelectorAll('.i-ftab').forEach(ftReset);s.querySelectorAll('td.i-ftot').forEach(c=>{c.textContent='';c.classList.remove('on')});
  s.querySelectorAll('.i-dch').forEach(x=>x.classList.remove('on','done'));
  s.querySelectorAll('.i-ztwo').forEach(b=>{b._an=(b._an||0)+1;b._set2(...b._v0)});
  s.querySelectorAll('.i-plk').forEach(pkReset);
  s.querySelectorAll('.i-round').forEach(b=>b._set(...b._v0));
  s.querySelectorAll('[data-chart="norm"]').forEach(nbHide)}
document.querySelectorAll('.i-tiles').forEach(tlInit);
document.querySelectorAll('.i-slider').forEach(b=>({fences:fsBuild,box:fsBuild,z:zsBuild,log:lsBuild,shape:shBuild})[b.dataset.kind](b));
document.querySelectorAll('.i-sort').forEach(b=>{csInit(b);csScore(b)});
document.querySelectorAll('.i-stem').forEach(sfReset);
document.querySelectorAll('.i-ztwo').forEach(ztBuild);
document.querySelectorAll('.i-plk').forEach(pkBuild);
document.querySelectorAll('.i-round').forEach(rdBuild);
document.querySelectorAll('[data-chart="norm"]').forEach(nbFix);
