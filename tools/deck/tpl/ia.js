/* ---------- ia: interactive features (16 Nov, ideas from the 10MA deck, 12MAG look) ----------
   Every feature is driven by data attributes on reveal steps (frags), so the click-reveal, back() and the PDF (final frame) all work.
   Widgets the teacher touches (sliders, card sort) carry class "ia": a click on them never advances the slide.
   IA.fast = 1 while the engine replays steps (show(n,true), back()): no delays, so the final frame is reached at once.
   1 tiles      data-tsort="#t" · data-tcross="#t|a|b" · data-tmid="#t|a|b|cls|label" · data-thalves="#t"   (a, b = positions in the ORDERED list; blank = all)
   2 sliders    data-fset="#id|value" (fences / box plot / z / log sliders: animate to a value) · data-shset="#id|skew" (shape slider, −1…1)
   3 card sort  data-sreveal="#id|1" (correct level-1 buckets) · data-slevel="#id|2" (open the sub-buckets) · data-sreveal="#id|2"
   4 stem       data-leaf="#id|0-5" or "#id|0,3,7" or "#id|all" (leaves fly in from the data list) · data-lsort="#id" (order each row)
     tally      data-ftally="#chips|#table|i" (light the values in class i and count them into row i) · data-ftot="#table" · data-fgrow="#hist|i" */
const IA={T:[],fast:0};
function iaLater(fn,ms){if(IA.fast||!ms)fn();else IA.T.push(setTimeout(fn,ms))}
const iaS=()=>(stage.getBoundingClientRect().width/1600)||1;
const iaNum=v=>String(+(+v).toFixed(6)).replace('-','−');
const iaEach=(spec,fn)=>{if(spec)spec.split(';').forEach(sp=>{const p=sp.split('|');const b=document.querySelector(p[0]);if(b)fn(b,p.slice(1))})};
/* quartiles, VCAA/CAS method: n odd leaves the median out of both halves */
function iaMed(a){const n=a.length;return n%2?a[(n-1)/2]:(a[n/2-1]+a[n/2])/2}
function iaFive(v){const a=v.slice().sort((x,y)=>x-y),n=a.length,h=Math.floor(n/2);return {a,min:a[0],max:a[n-1],m:iaMed(a),q1:iaMed(a.slice(0,h)),q3:iaMed(a.slice(n-h))}}

/* ===== 1. data tiles ===== */
function tlInit(b){const t=[...b.querySelectorAll('.i-t')];b._n=t.length;
  const ord=t.map((e,k)=>[+e.dataset.v,k]).sort((x,y)=>x[0]-y[0]||x[1]-y[1]).map(p=>p[1]);b._rank=[];b._at=[];ord.forEach((k,j)=>{b._rank[k]=j;b._at[j]=t[k]});tlReset(b)}
function tlPos(b,sorted){b.querySelectorAll('.i-t').forEach((e,k)=>{const j=sorted?b._rank[k]:k;e.style.left=`calc(${j} * 100% / ${b._n} + 4px)`})}
function tlClr(b){b.querySelectorAll('.i-t').forEach(e=>{e.classList.remove('t-x','t-mid','t-q','t-lo','t-hi');e.style.transitionDelay=''})}
function tlReset(b){tlPos(b,0);tlClr(b);b.querySelectorAll('.i-tlab,.i-tsplit').forEach(e=>e.remove())}
function tlRange(b,p){const a=p[0]!==undefined&&p[0]!==''?+p[0]:0,c=p[1]!==undefined&&p[1]!==''?+p[1]:b._n-1;return [a,c]}
function tlCross(b,a,c){let i=a,j=c,k=0;while(j-i>=2){[i,j].forEach(q=>{const e=b._at[q];e.style.transitionDelay=IA.fast?'':(k*.38)+'s';e.classList.add('t-x')});i++;j--;k++}return k}
function tlMid(b,a,c,cls,lab,delay){cls=cls||'mid';const n=c-a+1,m=a+Math.floor((n-1)/2);(n%2?[m]:[m,m+1]).forEach(q=>{const e=b._at[q];e.classList.remove('t-x');e.style.transitionDelay=IA.fast?'':delay+'s';e.classList.add('t-'+cls)});
  if(lab){const L=document.createElement('div');L.className='i-tlab l-'+cls;L.style.left=`calc(${(a+c+1)/2} * 100% / ${b._n})`;L.innerHTML=lab;if(!IA.fast)L.style.transitionDelay=delay+'s';b.append(L);
    if(IA.fast)L.classList.add('on');else requestAnimationFrame(()=>requestAnimationFrame(()=>L.classList.add('on')))}}
function tlSplit(b,pos){const d=document.createElement('div');d.className='i-tsplit';d.style.left=`calc(${pos} * 100% / ${b._n})`;b.append(d)}
function tlApply(f){
  iaEach(f.dataset.tsort,(b)=>{tlPos(b,1);b._sorted=1});
  const crossed={};
  iaEach(f.dataset.tcross,(b,p)=>{const [a,c]=tlRange(b,p);crossed[b.id+'|'+a+'|'+c]=tlCross(b,a,c)});
  iaEach(f.dataset.tmid,(b,p)=>{const [a,c]=tlRange(b,p);const k=crossed[b.id+'|'+a+'|'+c];tlMid(b,a,c,p[2],p[3],k!=null?k*.38+.15:0)});
  iaEach(f.dataset.thalves,(b)=>{const n=b._n,h=Math.floor(n/2);b.querySelectorAll('.i-t').forEach(e=>{e.classList.remove('t-x','t-q');if(n%2===0)e.classList.remove('t-mid');e.style.transitionDelay=''});
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
/* fences + box plot slider. cfg: data, k (index of the moving value), min, max, step, tick, lab (label every), lo/hi (slider limits), xl, dec, mode 'fences' | 'box' */
function fsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,L=40,R=40,box_=c.mode==='box',H=box_?300:310,ay=box_?190:200,sx=x=>L+(x-c.min)/(c.max-c.min)*(W-L-R),xs=X=>c.min+(X-L)/(W-L-R)*(c.max-c.min);
  const svg=slSvg(W,H),dec=c.dec!=null?c.dec:2;box.innerHTML='';box.append(svg);
  const rd=document.createElement('div');rd.className='i-read';box.append(rd);
  const f=x=>iaNum((+x).toFixed(dec));
  box._set=(x,moving)=>{x=moving?+x:slSnap(c,x);box._v=x;const v=c.data.slice();v[c.k]=x;const F=iaFive(v),iqr=F.q3-F.q1,lf=F.q1-1.5*iqr,uf=F.q3+1.5*iqr;
    svg.innerHTML='';
    /* outlier zones */
    const zt=24,zb=ay;if(lf>c.min)svg.append(el('rect',{x:sx(c.min),y:zt,width:sx(Math.max(c.min,lf))-sx(c.min),height:zb-zt,fill:'#fde3e7'}));
    if(uf<c.max)svg.append(el('rect',{x:sx(Math.min(c.max,uf)),y:zt,width:sx(c.max)-sx(Math.min(c.max,uf)),height:zb-zt,fill:'#fde3e7'}));
    /* axis */
    svg.append(el('line',{x1:L-14,x2:W-R+14,y1:ay,y2:ay,stroke:'#333','stroke-width':2}));const tk=c.tick||c.step||1,lb=c.lab||tk;
    for(let t=c.min;t<=c.max+1e-9;t+=tk){const big=Math.abs((t-c.min)/lb-Math.round((t-c.min)/lb))<1e-6;svg.append(el('line',{x1:sx(t),x2:sx(t),y1:ay,y2:ay+(big?10:6),stroke:'#333','stroke-width':big?2:1.2}));
      if(big)svg.append(el('text',{x:sx(t),y:ay+34,'text-anchor':'middle','font-size':19},iaNum(+t.toFixed(6))))}
    if(c.xl)svg.append(el('text',{x:(L+W-R)/2,y:ay+(box_?68:84),'text-anchor':'middle','font-size':20,'font-weight':600,'font-style':'italic'},c.xl));
    const out=x=>x<lf-1e-9||x>uf+1e-9,isOut=out(x);
    if(box_){const cy=100,bh=56,inl=F.a.filter(v=>!out(v)),lw=inl[0],uw=inl[inl.length-1],sc='#1b1f2a';
      svg.append(el('line',{x1:sx(lw),x2:sx(F.q1),y1:cy,y2:cy,stroke:sc,'stroke-width':2.5}),el('line',{x1:sx(F.q3),x2:sx(uw),y1:cy,y2:cy,stroke:sc,'stroke-width':2.5}),
        el('rect',{x:sx(F.q1),y:cy-bh/2,width:sx(F.q3)-sx(F.q1),height:bh,fill:'#cfe0fb',stroke:sc,'stroke-width':2.5}),el('line',{x1:sx(F.m),x2:sx(F.m),y1:cy-bh/2,y2:cy+bh/2,stroke:sc,'stroke-width':3.5}));
      F.a.filter(out).forEach(o=>svg.append(el('circle',{cx:sx(o),cy,r:9,fill:'#fff',stroke:'#d2475b','stroke-width':3})));
      /* the moving value: a handle under the axis */
      const hx=sx(x),hc=isOut?'#d2475b':'#d98a1f';svg.append(el('line',{x1:hx,x2:hx,y1:cy+(isOut?12:0),y2:ay-26,stroke:hc,'stroke-width':2,'stroke-dasharray':'4 4'}),
        el('path',{d:`M${hx},${ay-2} l-13,-24 h26 z`,fill:hc,class:'i-handle'}),el('text',{x:hx,y:cy-bh/2-12,'text-anchor':'middle','font-size':20,'font-weight':800,fill:hc},'x = '+f(x)))}
    else{const cnt={},r=11;F.a.forEach(v=>{cnt[v]=(cnt[v]||0)+1});const seen={};let mv=false;
      v.forEach((d,j)=>{seen[d]=(seen[d]||0)+1;const cy=ay-r-5-(seen[d]-1)*(2*r+3),me=j===c.k;
        svg.append(el('circle',{cx:sx(d),cy,r:me?r+3:r,fill:me?(isOut?'#d2475b':'#d98a1f'):(out(d)?'#d2475b':'#1f4fb0'),stroke:me?'#fff':'none','stroke-width':2,class:me?'i-handle':''}));
        if(me)svg.append(el('text',{x:sx(d),y:cy-24,'text-anchor':'middle','font-size':20,'font-weight':800,fill:isOut?'#d2475b':'#9a5a00'},'x = '+f(d)))});
      [[F.q1,'Q₁'],[F.q3,'Q₃']].forEach(([q,t])=>svg.append(el('line',{x1:sx(q),x2:sx(q),y1:ay-8,y2:ay+8,stroke:'#1f9e74','stroke-width':4}),el('text',{x:sx(q),y:ay+56,'text-anchor':'middle','font-size':17,'font-weight':800,fill:'#137a59'},t)))}
    [[lf,'LF'],[uf,'UF']].forEach(([q,t])=>{if(q<c.min||q>c.max)return;svg.append(el('line',{x1:sx(q),x2:sx(q),y1:zt,y2:ay,stroke:'#2f6fdf','stroke-width':3,'stroke-dasharray':'8 6'}),
      el('text',{x:sx(q),y:zt-4,'text-anchor':'middle','font-size':18,'font-weight':800,fill:'#1f4fb0'},t+' = '+f(q)))});
    const st=x>uf+1e-9?`<b class="no"><i>x</i> = ${f(x)} &gt; UF = ${f(uf)} → <i>x</i> is an outlier</b>`:x<lf-1e-9?`<b class="no"><i>x</i> = ${f(x)} &lt; LF = ${f(lf)} → <i>x</i> is an outlier</b>`
      :`<b class="ok">LF ≤ <i>x</i> = ${f(x)} ≤ UF → not an outlier</b>`;
    rd.innerHTML=`<div>Q<sub>1</sub> = <b>${f(F.q1)}</b> · Q<sub>3</sub> = <b>${f(F.q3)}</b> · IQR = Q<sub>3</sub> − Q<sub>1</sub> = <b>${f(iqr)}</b>${box_?` · M = <b>${f(F.m)}</b>`:''}</div>`+
      `<div>LF = Q<sub>1</sub> − 1.5 × IQR = <b>${f(lf)}</b> · UF = Q<sub>3</sub> + 1.5 × IQR = <b>${f(uf)}</b></div><div>${st}</div>`+
      (box_?`<div class="i-sm">Whiskers end at the last values that are not outliers: ${f(F.a.filter(v=>!out(v))[0])} and ${f(F.a.filter(v=>!out(v)).slice(-1)[0])}.</div>`:'')};
  slDrag(box,svg,X=>slSnap(c,xs(X)));box._v0=c.data[c.k];box._set(box._v0)}
/* normal-curve z slider. cfg: m, s, step (default s/2), xl, dec, W */
const IAPCT={'-3':0.15,'-2':2.5,'-1':16,'0':50,'1':84,'2':97.5,'3':99.85};
function zsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=330,L=30,R=30,T=40,base=230,sx=z=>L+(z+3.6)/7.2*(W-L-R),sy=z=>base-Math.exp(-z*z/2)*(base-T),dec=c.dec!=null?c.dec:2;
  c.min=c.m-3.5*c.s;c.max=c.m+3.5*c.s;c.lo=c.m-3*c.s;c.hi=c.m+3*c.s;c.step=c.step||c.s/2;const svg=slSvg(W,H);box.innerHTML='';box.append(svg);const rd=document.createElement('div');rd.className='i-read';box.append(rd);
  const f=x=>iaNum((+x).toFixed(dec));
  box._set=(x,moving)=>{x=moving?+x:slSnap(c,x);box._v=x;const z=(x-c.m)/c.s;svg.innerHTML='';
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
function lsBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=230,L=60,R=60,sx=p=>L+(p-c.lo)/(c.hi-c.lo)*(W-L-R),y1=70,y2=170;box.innerHTML='';const svg=slSvg(W,H);box.append(svg);
  const rd=document.createElement('div');rd.className='i-read';box.append(rd);c.min=c.lo;c.max=c.hi;c.step=c.step||0.01;
  const sp=x=>x>=1e4?Math.round(x).toLocaleString('en-AU').replace(/,/g,' '):String(+x.toPrecision(3));
  box._set=(p)=>{p=Math.max(c.lo,Math.min(c.hi,+p));box._v=p;const x=Math.pow(10,p);svg.innerHTML='';
    svg.append(el('text',{x:10,y:y1-34,'font-size':18,'font-weight':800,fill:'#5b33b0'},'log₁₀(x)'),el('text',{x:10,y:y2+56,'font-size':18,'font-weight':800,fill:'#1f4fb0'},c.xl||'x'));
    [y1,y2].forEach(y=>svg.append(el('line',{x1:L-10,x2:W-R+10,y1:y,y2:y,stroke:'#333','stroke-width':2})));
    for(let k=Math.ceil(c.lo);k<=c.hi;k++){svg.append(el('line',{x1:sx(k),x2:sx(k),y1:y1-8,y2:y2+8,stroke:'#e3e6ee','stroke-width':1.5}),
      el('text',{x:sx(k),y:y1-14,'text-anchor':'middle','font-size':19,'font-weight':600,fill:'#5b33b0'},k),el('text',{x:sx(k),y:y2+30,'text-anchor':'middle','font-size':18,fill:'#1f4fb0'},sp(Math.pow(10,k))));
      for(let m=2;m<10&&k+Math.log10(m)<=c.hi;m++)svg.append(el('line',{x1:sx(k+Math.log10(m)),x2:sx(k+Math.log10(m)),y1:y2,y2:y2+7,stroke:'#555','stroke-width':1}))}
    const hx=sx(p);svg.append(el('line',{x1:hx,x2:hx,y1:y1,y2:y2,stroke:'#d98a1f','stroke-width':4}),el('circle',{cx:hx,cy:y1,r:10,fill:'#d98a1f',class:'i-handle'}),el('circle',{cx:hx,cy:y2,r:10,fill:'#d98a1f',class:'i-handle'}));
    rd.innerHTML=`<div><i>x</i> = <b>${sp(x)}</b> &nbsp;⟷&nbsp; log<sub>10</sub>(${sp(x)}) = <b>${p.toFixed(2)}</b> &nbsp;·&nbsp; 10<sup>${p.toFixed(2)}</sup> = ${sp(x)}</div><div class="i-sm">Each step of 1 on the log scale multiplies <i>x</i> by 10.</div>`};
  slDrag(box,svg,X=>Math.round((c.lo+(X-L)/(W-L-R)*(c.hi-c.lo))/c.step)*c.step);box._v0=c.x0!=null?Math.log10(c.x0):(c.lo+c.hi)/2;box._set(box._v0)}
/* shape slider: drag left/right to skew a histogram; mean (dashed) and median (solid) follow. cfg: v0 (−1…1), W */
function shBuild(box){const c=JSON.parse(box.dataset.cfg),W=c.W||1000,H=320,L=40,R=40,B=44,T=30,N=11,w=(W-L-R)/N;box.innerHTML='';const svg=slSvg(W,H);box.append(svg);
  const rd=document.createElement('div');rd.className='i-read';box.append(rd);
  box._set=(a,moving)=>{a=Math.max(-1,Math.min(1,+a));if(!moving)a=Math.round(a*20)/20;box._v=a;
    let fr=[...Array(N).keys()].map(k=>{const x=(k+.5)/N,p=3+9*Math.max(0,-a),q=3+9*Math.max(0,a);return Math.pow(x,p-1)*Math.pow(1-x,q-1)});const mx=Math.max(...fr);fr=fr.map(v=>Math.round(v/mx*12));
    const n=fr.reduce((s,v)=>s+v,0),mean=fr.reduce((s,v,k)=>s+v*k,0)/n;let cu=0,med=0;for(let k=0;k<N;k++){if(cu+fr[k]>=n/2){med=k-.5+(n/2-cu)/fr[k];break}cu+=fr[k]}
    const X=v=>L+(v+.5)*w,Y=v=>H-B-v/12*(H-B-T);svg.innerHTML='';
    fr.forEach((v,k)=>svg.append(el('rect',{x:L+k*w,y:Y(v),width:w,height:H-B-Y(v),fill:'#4f84e6',stroke:'#1f4fb0','stroke-width':1.5})));
    svg.append(el('line',{x1:L,x2:W-R,y1:H-B,y2:H-B,stroke:'#333','stroke-width':2}),el('line',{x1:X(med),x2:X(med),y1:T-10,y2:H-B,stroke:'#1f9e74','stroke-width':4}),
      el('line',{x1:X(mean),x2:X(mean),y1:T-10,y2:H-B,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'10 6'}));
    const sym=Math.abs(a)<.12;if(!sym){const y0=T+30,x1=a>0?X(med)+30:X(med)-30,x2=a>0?W-R-8:L+8;svg.append(el('line',{x1,x2,y1:y0,y2:y0,stroke:'#d98a1f','stroke-width':4}),
      el('path',{d:a>0?`M${x2},${y0} l-14,-9 v18 z`:`M${x2},${y0} l14,-9 v18 z`,fill:'#d98a1f'}),el('text',{x:(x1+x2)/2,y:y0-10,'text-anchor':'middle','font-size':19,'font-weight':800,fill:'#9a5a00'},'tail'))}
    const nm=sym?'symmetric':a>0?'positively skewed':'negatively skewed';
    rd.innerHTML=`<div>The distribution is <b>${nm}</b>.</div><div><span style="color:#1f9e74;font-weight:800">median ${med.toFixed(1)}</span> · <span style="color:#d2475b;font-weight:800">mean ${mean.toFixed(1)}</span> · `+
      (sym?'mean ≈ median':a>0?'the tail pulls the mean <b>above</b> the median':'the tail pulls the mean <b>below</b> the median')+'</div>'};
  slDrag(box,svg,X=>((X-L)/(W-L-R))*2-1);box._v0=c.v0||0;box._set(box._v0)}

/* ===== 3. card sort ===== */
function csHome(cs){return cs.closest('.i-sort').querySelector('.i-pool')}
function csTray(b,path){return b.querySelector(`.i-bk[data-b="${path}"] > .i-tray`)}
function csMove(card,tray){const r0=card.getBoundingClientRect(),sc=iaS();tray.append(card);if(IA.fast)return;const r1=card.getBoundingClientRect();
  card.style.transition='none';card.style.transform=`translate(${(r0.left-r1.left)/sc}px,${(r0.top-r1.top)/sc}px)`;void card.offsetWidth;card.style.transition='';card.style.transform=''}
function csInit(b){b.querySelectorAll('.i-cs').forEach((cs,k)=>{cs.dataset.k=k;let d=null;
  cs.addEventListener('pointerdown',e=>{d={x:e.clientX,y:e.clientY,on:false};cs.setPointerCapture(e.pointerId);e.stopPropagation()});
  cs.addEventListener('pointermove',e=>{if(!d)return;const dx=e.clientX-d.x,dy=e.clientY-d.y;if(!d.on&&Math.hypot(dx,dy)>6){d.on=true;cs.classList.add('drag')}
    if(d.on){const sc=iaS();cs.style.transition='none';cs.style.transform=`translate(${dx/sc}px,${dy/sc}px)`}});
  cs.addEventListener('pointerup',e=>{if(!d)return;const was=d.on;d=null;cs.classList.remove('drag');cs.style.transform='';cs.style.transition='';
    if(!was){const s=cs.classList.contains('sel');b.querySelectorAll('.i-cs.sel').forEach(x=>x.classList.remove('sel'));if(!s)cs.classList.add('sel');return}
    cs.style.visibility='hidden';const t=document.elementFromPoint(e.clientX,e.clientY);cs.style.visibility='';
    const bk=t&&t.closest('.i-bk'),pool=t&&t.closest('.i-pool');if(bk&&b.contains(bk))csMove(cs,bk.querySelector(':scope > .i-tray'));else if(pool)csMove(cs,pool);cs.classList.remove('ok','no')})});
  b.querySelectorAll('.i-bk').forEach(bk=>bk.addEventListener('click',e=>{if(e.target.closest('.i-cs'))return;e.stopPropagation();const cs=b.querySelector('.i-cs.sel');if(!cs)return;
    const own=e.target.closest('.i-bk');csMove(cs,own.querySelector(':scope > .i-tray'));cs.classList.remove('sel','ok','no')}));
  b.querySelector('.i-pool').addEventListener('click',e=>{if(e.target.closest('.i-cs'))return;const cs=b.querySelector('.i-cs.sel');if(cs){csMove(cs,b.querySelector('.i-pool'));cs.classList.remove('sel','ok','no')}});
  b._order=[...b.querySelectorAll('.i-cs')];b.addEventListener('click',e=>e.stopPropagation())}
function csReset(b){const pool=b.querySelector('.i-pool');b._order.forEach(cs=>{pool.append(cs);cs.classList.remove('sel','ok','no');cs.style.transform=''});b.classList.remove('lv2');b.querySelector('.i-score').innerHTML=''}
function csReveal(b,lv){let ok=0;const all=b._order;all.forEach(cs=>{const ans=cs.dataset.a.split('/'),L=Math.min(lv,ans.length),want=ans.slice(0,L).join('/'),bk=cs.closest('.i-bk'),got=bk?bk.dataset.b.split('/'):null;
    cs.classList.remove('sel');const placed=got&&got.length>=L,right=placed&&got.slice(0,L).join('/')===want;
    if(placed){cs.classList.remove('ok','no');cs.classList.add(right?'ok':'no')}if(right)ok++;
    if(!right){const t=csTray(b,want);if(t)csMove(cs,t)}});
  b.querySelector('.i-score').innerHTML=`Step ${lv}: <b>${ok}</b> of ${all.length} placed correctly before the reveal`}

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
  iaEach(d.slevel,(b,p)=>{if(+p[0]>=2)b.classList.add('lv2')});
  iaEach(d.sreveal,(b,p)=>{if(+p[0]>=2)b.classList.add('lv2');csReveal(b,+p[0]||1)});
  iaEach(d.leaf,(b,p)=>{const n=b.querySelectorAll('.i-lf').length;iaIdx(p[0],n).forEach((k,j)=>sfFly(b,k,j*180))});
  iaEach(d.lsort,(b)=>sfSort(b));
  if(d.ftally){const [c,t,i]=d.ftally.split('|');const ch=document.querySelector(c),tb=document.querySelector(t);if(ch&&tb)ftTally(ch,tb,i)}
  iaEach(d.ftot,(t)=>{const c=t.querySelector('td.i-ftot');if(c){c.textContent=[...t.querySelectorAll('td.i-fq')].reduce((a,x)=>a+(+x.dataset.n||0),0);c.classList.add('on')}
    t.querySelectorAll('tr.hy').forEach(r=>r.classList.remove('hy'));document.querySelectorAll('.i-dch.on').forEach(x=>{x.classList.remove('on');x.classList.add('done')})});
  iaEach(d.fgrow,(ch,p)=>p[0].split(',').forEach(i=>{const r=ch.querySelector(`rect.grow[data-i="${i}"]`);if(r)grow(r)}))}
function iareset(s){IA.T.splice(0).forEach(clearTimeout);
  s.querySelectorAll('.i-tiles').forEach(tlReset);
  s.querySelectorAll('.i-slider').forEach(b=>{b._an=(b._an||0)+1;b._v=null;if(b._set)b._set(b._v0)});
  s.querySelectorAll('.i-sort').forEach(csReset);
  s.querySelectorAll('.i-stem').forEach(sfReset);
  s.querySelectorAll('.i-ftab').forEach(ftReset);s.querySelectorAll('td.i-ftot').forEach(c=>{c.textContent='';c.classList.remove('on')});
  s.querySelectorAll('.i-dch').forEach(x=>x.classList.remove('on','done'))}
document.querySelectorAll('.i-tiles').forEach(tlInit);
document.querySelectorAll('.i-slider').forEach(b=>({fences:fsBuild,box:fsBuild,z:zsBuild,log:lsBuild,shape:shBuild})[b.dataset.kind](b));
document.querySelectorAll('.i-sort').forEach(csInit);
document.querySelectorAll('.i-stem').forEach(sfReset);
