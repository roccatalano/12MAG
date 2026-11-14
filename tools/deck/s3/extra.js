
/* ---------- S3: explainers (median, quartiles, balance point, standard deviation) ---------- */
const S3T=[];function later(fn,ms){S3T.push(setTimeout(fn,ms))}
function sortIdx(v){return v.map((x,i)=>[x,i]).sort((a,b)=>a[0]-b[0]||a[1]-b[1]).map(p=>p[1])}
/* --- 1. median: chips slide into order, count in from both ends --- */
const MED={base:[6,2,9,4,7,3,8],extra:5};
function medBuild(){const box=document.getElementById('medx');if(!box)return;box.innerHTML='';
  [...MED.base,MED.extra].forEach((v,k)=>{const c=document.createElement('div');c.className='chip3'+(k===MED.base.length?' new':'');c.textContent=v;c.dataset.k=k;box.append(c)});
  box.insertAdjacentHTML('beforeend','<div class="xlab c" id="medlab" style="left:50%;top:150px"></div><div class="xlab c" id="medlab2" style="left:50%;top:196px;font-size:21px;color:#6b7280"></div>');medSet({extra:0,ordered:0,dim:0,mid:0})}
function medSet(st){const box=document.getElementById('medx');if(!box)return;box._st=Object.assign(box._st||{},st);const s=box._st;
  const vals=s.extra?[...MED.base,MED.extra]:MED.base.slice(),n=vals.length,W=74,G=18,tot=n*W+(n-1)*G,x0=(box.clientWidth||1400)/2-tot/2;
  const ord=s.ordered?sortIdx(vals):vals.map((_,i)=>i);const slot={};ord.forEach((k,j)=>slot[k]=j);
  box.querySelectorAll('.chip3').forEach(c=>{const k=+c.dataset.k;if(k>=n){c.classList.add('hide');c.style.left=(x0+tot+G)+'px';c.style.top='40px';return}
    c.classList.remove('hide');const j=slot[k];c.style.left=(x0+j*(W+G))+'px';c.style.top='60px';
    c.classList.toggle('cnt',s.dim>0&&(j<s.dim||j>=n-s.dim));
    const mids=n%2?[(n-1)/2]:[n/2-1,n/2];c.classList.toggle('mid',!!s.mid&&mids.includes(j))});
  const L=document.getElementById('medlab'),L2=document.getElementById('medlab2');
  if(!s.ordered){L.innerHTML='n = '+n+' values, not in order yet';L2.textContent=''}
  else if(!s.mid){L.innerHTML='Ordered. Now count in from both ends…';L2.textContent=''}
  else if(n%2){L.innerHTML='n = 7 is odd: the median is the <span class="red">4th value</span>, &nbsp;M = <span class="red">6</span>';L2.innerHTML='3 values below it, 3 values above it'}
  else{L.innerHTML='n = 8 is even: average the <span class="red">4th and 5th values</span>, &nbsp;M = (5 + 6) ÷ 2 = <span class="red">5.5</span>';L2.innerHTML='4 values below it, 4 values above it'}}
function medCount(){const box=document.getElementById('medx');const n=box._st.extra?8:7,h=Math.floor((n-1)/2);
  for(let k=1;k<=h;k++)later(()=>medSet({dim:k}),k*420);later(()=>medSet({mid:1}),(h+1)*420)}
/* --- 2. quartiles: two rows (n odd, n even) --- */
const QX=[{v:[2,4,5,7,8,10,11,13,14,16,19],m:[5],q1:[2],q3:[8],M:'10',Q1:'5',Q3:'14'},
          {v:[2,4,5,7,8,10,11,13,14,16,19,20],m:[5,6],q1:[2,3],q3:[8,9],M:'(10 + 11) ÷ 2 = 10.5',Q1:'(5 + 7) ÷ 2 = 6',Q3:'(14 + 16) ÷ 2 = 15'}];
function qBuild(){const box=document.getElementById('qx');if(!box)return;box.innerHTML='';const W=66,G=14;box._g={W,G};
  QX.forEach((r,ri)=>{const n=r.v.length,tot=n*W+(n-1)*G,x0=700-tot/2,top=56+ri*210;r.x0=x0;r.top=top;
    box.insertAdjacentHTML('beforeend',`<div class="rowtag" style="top:${top+16}px" id="qt${ri}">n = ${n} (${n%2?'odd':'even'})</div>`);
    box.insertAdjacentHTML('beforeend',`<div class="band hide" id="qb${ri}"><b>middle 50% · IQR = 9</b></div>`);
    r.v.forEach((v,k)=>{const c=document.createElement('div');c.className='chip3';c.style.width=W+'px';c.style.height='52px';c.style.fontSize='24px';c.textContent=v;c.dataset.r=ri;c.dataset.k=k;c.style.left=(x0+k*(W+G))+'px';c.style.top=top+'px';box.append(c)});
    const cx=ks=>x0+(ks.reduce((a,b)=>a+b,0)/ks.length)*(W+G)+W/2;r.cx=cx;
    [['m',r.m,'M = '+r.M,''],['q1',r.q1,'Q<sub>1</sub> = '+r.Q1,'p'],['q3',r.q3,'Q<sub>3</sub> = '+r.Q3,'p']].forEach(([id,ks,t,p],z)=>{
      box.insertAdjacentHTML('beforeend',`<div class="mk ${p} hide" id="mk${id}${ri}" style="left:${cx(ks)}px;top:${top+60}px"></div><div class="xlab c hide" id="lb${id}${ri}" style="left:${cx(ks)}px;top:${top+78+(id==='m'?0:0)}px;font-size:${ri?18:20}px">${t}</div>`)});
    if(ri===0)box.insertAdjacentHTML('beforeend',`<div class="xlab hide" id="omit0" style="left:${cx([5])+60}px;top:${top+112}px;font-size:17px;color:#b0263a">n odd: leave the median out of both halves</div>`);
    const b=document.getElementById('qb'+ri);b.style.left=(cx(r.q1)-W/2-6)+'px';b.style.width=(cx(r.q3)-cx(r.q1)+W+12)+'px';b.style.top=(top-10)+'px';b.style.height='72px'});
  qSet(null)}
function qSet(a){const box=document.getElementById('qx');if(!box)return;box._st=box._st||[{},{}];if(a===null)box._st=[{},{show:0},];
  if(a){const [ri,k]=a;box._st[ri][k]=1}
  box._st.forEach((s,ri)=>{const r=QX[ri],show=ri===0||s.show;
    box.querySelectorAll(`.chip3[data-r="${ri}"]`).forEach(c=>{const k=+c.dataset.k;c.classList.toggle('hide',!show);c.classList.toggle('mid',!!s.m&&r.m.includes(k));c.classList.toggle('q1m',!!s.q&&(r.q1.includes(k)||r.q3.includes(k)))});
    document.getElementById('qt'+ri).classList.toggle('hide',!show);
    document.getElementById('mkm'+ri).classList.toggle('hide',!s.m);document.getElementById('lbm'+ri).classList.toggle('hide',!s.m);
    ['q1','q3'].forEach(q=>{document.getElementById('mk'+q+ri).classList.toggle('hide',!s.q);document.getElementById('lb'+q+ri).classList.toggle('hide',!s.q)});
    document.getElementById('qb'+ri).classList.toggle('hide',!s.band);if(ri===0)document.getElementById('omit0').classList.toggle('hide',!s.m)})}
/* --- 3. mean as the balance point --- */
const BAL={v:[2,3,3,4],mv:3};
function balBuild(){const box=document.getElementById('balx');if(!box)return;box.innerHTML='';const W=1400,H=330,L=110,R=1290,Y=196,sx=x=>L+x/10*(R-L);box._sx=sx;
  const s=el('svg',{viewBox:`0 0 ${W} ${H}`,width:'100%'});
  s.append(el('rect',{x:L-30,y:Y,width:R-L+60,height:10,rx:5,fill:'#1b1f2a'}));
  for(let x=0;x<=10;x++){s.append(el('line',{x1:sx(x),x2:sx(x),y1:Y+10,y2:Y+20,stroke:'#555','stroke-width':2}),el('text',{x:sx(x),y:Y+44,'text-anchor':'middle','font-size':22,fill:'#444'},x))}
  const fg=el('g',{class:'mv',id:'bfulc'});fg.append(el('path',{d:'M0,0 L-34,62 L34,62 Z',fill:'#2f6fdf',transform:`translate(0,${Y+10})`}),el('text',{id:'bmean',x:0,y:Y+102,'text-anchor':'middle','font-size':24,'font-weight':700,fill:'#2f6fdf'},''));s.append(fg);
  const mg=el('g',{class:'mv',id:'bmed'});mg.append(el('path',{d:'M-12,0 L12,0 L0,16 Z',fill:'#d2475b',transform:'translate(0,40)'}),el('text',{id:'bmedt',x:0,y:30,'text-anchor':'middle','font-size':24,'font-weight':700,fill:'#d2475b'},''));s.append(mg);
  BAL.v.forEach((v,k)=>{const g=el('g',{class:'mv'+(k===BAL.mv?' dragdot':''),id:'bd'+k});g.append(el('circle',{r:17,cx:0,cy:0,fill:k===BAL.mv?'#d98a1f':'#1f4fb0'}));s.append(g)});
  box.append(s);
  const dot=s.querySelector('#bd'+BAL.mv);let drag=false;
  const toVal=e=>{const p=s.createSVGPoint();p.x=e.clientX;p.y=e.clientY;const q=p.matrixTransform(s.getScreenCTM().inverse());return Math.max(0,Math.min(10,Math.round((q.x-L)/(R-L)*20)/2))};
  dot.addEventListener('pointerdown',e=>{drag=true;box.classList.add('drag');dot.setPointerCapture(e.pointerId);e.stopPropagation()});
  dot.addEventListener('pointermove',e=>{if(drag)balSet(toVal(e))});
  dot.addEventListener('pointerup',e=>{drag=false;box.classList.remove('drag')});
  s.addEventListener('click',e=>{if(e.target.closest('.dragdot'))e.stopPropagation()});
  balSet(4)}
function balSet(x){const box=document.getElementById('balx');if(!box)return;const sx=box._sx,Y=196,v=BAL.v.slice();v[BAL.mv]=x;box._x=x;
  const cnt={};v.forEach((a,k)=>{cnt[a]=(cnt[a]||0)+1;const g=box.querySelector('#bd'+k);g.style.transform=`translate(${sx(a)}px,${Y-19-(cnt[a]-1)*37}px)`});
  const mean=v.reduce((a,b)=>a+b,0)/v.length,sv=v.slice().sort((a,b)=>a-b),med=(sv[1]+sv[2])/2;
  box.querySelector('#bfulc').style.transform=`translate(${sx(mean)}px,0)`;box.querySelector('#bmean').textContent='mean = '+(+mean.toFixed(3));
  box.querySelector('#bmed').style.transform=`translate(${sx(med)}px,0)`;box.querySelector('#bmedt').textContent='M = '+med;
  const t=document.getElementById('balread');if(t)t.innerHTML=`Data: ${sv.join('&nbsp;&nbsp;')} &nbsp;→&nbsp; mean = ${sv.join(' + ')} ÷ 4 = <b style="color:#2f6fdf">${+mean.toFixed(3)}</b>, &nbsp;median = <b style="color:#d2475b">${med}</b>`}
/* --- 4. standard deviation: distances from the mean --- */
const SDX=[{n:'Set A',v:[3,4,5,6,7],s:'1.58'},{n:'Set B',v:[1,3,5,7,9],s:'3.16'}];
function sdBuild(){const box=document.getElementById('sdx');if(!box)return;box.innerHTML='';const W=1400,H=360,L=250,R=1250,sx=x=>L+x/10*(R-L);
  const s=el('svg',{viewBox:`0 0 ${W} ${H}`,width:'100%'});
  const defs=el('defs');const m=el('marker',{id:'arr',markerWidth:8,markerHeight:8,refX:6,refY:4,orient:'auto'});m.append(el('path',{d:'M0,0 L8,4 L0,8 Z',fill:'#d98a1f'}));defs.append(m);s.append(defs);
  SDX.forEach((d,ri)=>{const Y=130+ri*170,g=el('g',{id:'sdg'+ri});
    g.append(el('text',{x:40,y:Y+8,'font-size':26,'font-weight':800,fill:'#1b1f2a'},d.n));
    g.append(el('line',{x1:L-20,x2:R+20,y1:Y,y2:Y,stroke:'#333','stroke-width':2.5}));
    for(let x=0;x<=10;x++)g.append(el('line',{x1:sx(x),x2:sx(x),y1:Y,y2:Y+9,stroke:'#555','stroke-width':1.5}),el('text',{x:sx(x),y:Y+32,'text-anchor':'middle','font-size':19,fill:'#555'},x));
    g.append(el('line',{x1:sx(5),x2:sx(5),y1:Y-100,y2:Y,stroke:'#2f6fdf','stroke-width':3,'stroke-dasharray':'8 6'}),el('text',{x:sx(5),y:Y-106,'text-anchor':'middle','font-size':20,'font-weight':700,fill:'#2f6fdf'},'mean = 5'));
    const dv=el('g',{id:'sdd'+ri,class:'sdd'}),devs=[...new Set(d.v.map(v=>Math.abs(v-5)).filter(x=>x))].sort((a,b)=>a-b);
    d.v.forEach(v=>{if(v===5)return;const lev=devs.indexOf(Math.abs(v-5)),yy=Y-36-lev*32;dv.append(el('line',{x1:sx(5),x2:sx(v)+(v>5?-6:6),y1:yy,y2:yy,stroke:'#d98a1f','stroke-width':4,'marker-end':'url(#arr)'}),el('text',{x:(sx(5)+sx(v))/2,y:yy-7,'text-anchor':'middle','font-size':18,'font-weight':700,fill:'#9a5a00'},(v>5?'+':'−')+Math.abs(v-5)))});
    g.append(dv);d.v.forEach(v=>g.append(el('circle',{cx:sx(v),cy:Y-14,r:13,fill:'#1f4fb0'})));
    g.append(el('text',{id:'sds'+ri,x:R+40,y:Y+8,'font-size':28,'font-weight':800,fill:'#1f9e74'},'s ≈ '+d.s));s.append(g)});
  box.append(s);sdSet({})}
function sdSet(st){const box=document.getElementById('sdx');if(!box)return;box._st=Object.assign(box._st||{},st);const s=box._st;
  [0,1].forEach(ri=>{box.querySelector('#sdg'+ri).style.opacity=(ri===0?s.a:s.b)?1:0;box.querySelector('#sdd'+ri).style.opacity=(ri===0?s.ad:s.bd)?1:0;box.querySelector('#sds'+ri).style.opacity=s.s?1:0})}
/* --- stem plots / data rows: count in from both ends, mark values --- */
function idxEls(sel){return [...document.querySelectorAll(sel+' [data-i]')].sort((a,b)=>a.dataset.i-b.dataset.i)}
function countIn(spec){const [sel,lo,hi,cls]=spec.split('|');const all=idxEls(sel),a=lo?+lo:0,b=hi?+hi:all.length-1,set=all.slice(a,b+1),n=set.length,h=Math.floor((n-1)/2);
  for(let k=0;k<h;k++)later(()=>{set[k].classList.add('cnt');set[n-1-k].classList.add('cnt')},k*170+60);
  later(()=>{set.forEach(e=>e.classList.remove('cnt'));(n%2?[set[h]]:[set[h],set[h+1]]).forEach(e=>e.classList.add(cls||'mid'))},h*170+260)}
function markIdx(spec){const [sel,ks,cls]=spec.split('|');const all=idxEls(sel);ks.split(',').forEach(k=>all[+k]&&all[+k].classList.add(cls||'mid'))}
/* --- histogram running totals --- */
function cumBars(spec){const [sel,hl]=spec.split('|');const box=document.querySelector(sel),svg=box.querySelector('svg');let tot=0;
  [...svg.querySelectorAll('rect.grow')].forEach((r,k)=>{const v=+r.dataset.v;tot+=v;const t=tot;later(()=>{svg.append(el('text',{class:'cum',x:+r.getAttribute('x')+ +r.getAttribute('width')/2,y:+r.dataset.y-8,'text-anchor':'middle','font-size':18},t))},k*260)})}
function hlBar(spec){const [sel,i,col]=spec.split('|');const r=document.querySelector(sel+' rect.grow[data-i="'+i+'"]');if(r){r.setAttribute('fill',col);r.setAttribute('stroke',col)}}
/* --- dot plot with markable dots --- */
function drawDot3(box,c){const W=c.W||900,H=c.h||240,L=34,R=34,B=72,r=c.r||12,fs=c.fs||20,n=c.max-c.min,pw=W-L-R,sx=x=>L+(x-c.min)/n*pw,base=H-B;
  const s=el('svg',{viewBox:`0 0 ${W} ${H}`,width:'100%'});s.append(el('line',{x1:L-14,x2:W-R+14,y1:base,y2:base,stroke:'#333','stroke-width':2}));
  for(let x=c.min;x<=c.max;x+=(c.step||1)){const xx=sx(x);s.append(el('line',{x1:xx,x2:xx,y1:base,y2:base+8,stroke:'#333','stroke-width':1.5}),el('text',{x:xx,y:base+32,'text-anchor':'middle','font-size':fs},x))}
  if(c.xl)s.append(el('text',{x:L+pw/2,y:H-8,'text-anchor':'middle','font-size':fs+1,'font-weight':600,'font-style':'italic'},c.xl));
  const cnt={};let i=0;c.vals.slice().sort((a,b)=>a-b).forEach(v=>{cnt[v]=(cnt[v]||0)+1;s.append(el('circle',{cx:sx(v),cy:base-r-5-(cnt[v]-1)*(2*r+3),r,fill:'#1f4fb0','data-i':i++,class:'d3'}))});box.append(s)}
function markDots(spec){const [sel,ks,col]=spec.split('|');ks.split(',').forEach(k=>{const d=document.querySelector(sel+' circle[data-i="'+k+'"]');if(d){d.setAttribute('fill',col||'#d2475b');d.setAttribute('r',+d.getAttribute('r')+2)}})}
/* --- CFAT timer --- */
let TIM=null;function timerReset(){clearInterval(TIM);TIM=null;const t=document.getElementById('cfatT');if(t){t.textContent='20:00';t.classList.remove('go')}}
function timerGo(){const t=document.getElementById('cfatT');if(!t)return;clearInterval(TIM);let s=1200;t.classList.add('go');TIM=setInterval(()=>{s--;t.textContent=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');if(s<=0)clearInterval(TIM)},1000)}
function s3apply(s,f){const a=f.dataset.act;
  if(a==='m-order')medSet({ordered:1});if(a==='m-count')medCount();
  if(a==='m-even'){medSet({extra:1,ordered:0,dim:0,mid:0});later(()=>medSet({ordered:1}),500)}
  if(a==='m-evenmid')medCount();
  if(a&&a.startsWith('q-')){const [_,ri,k]=a.split('-');qSet([+ri,k])}
  if(a==='b-8')balSet(8);
  if(a&&a.startsWith('sd-'))sdSet({[a.slice(3)]:1});
  if(a==='timer')timerGo();
  if(f.dataset.count)f.dataset.count.split(' ').forEach(countIn);
  if(f.dataset.mark)f.dataset.mark.split(' ').forEach(markIdx);
  if(f.dataset.cum)cumBars(f.dataset.cum);
  if(f.dataset.hlbar)f.dataset.hlbar.split(' ').forEach(hlBar);
  if(f.dataset.showbar){const [sel,ks]=f.dataset.showbar.split('|');ks.split(',').forEach(k=>{const r=document.querySelector(sel+' rect.grow[data-i="'+k+'"]');if(r){r.style.opacity=1;r.setAttribute('fill','#d98a1f');r.setAttribute('stroke','#9a5a00');grow(r)}})}
  if(f.dataset.dotmark)markDots(f.dataset.dotmark)}
function s3reset(s){S3T.splice(0).forEach(clearTimeout);
  s.querySelectorAll('[data-i]').forEach(e=>e.classList.remove('cnt','mid','q1m','ext'));
  s.querySelectorAll('text.cum').forEach(t=>t.remove());
  s.querySelectorAll('rect.grow[data-c0]').forEach(r=>{r.setAttribute('fill',r.dataset.c0);r.setAttribute('stroke','#1f4fb0')});
  s.querySelectorAll('[data-miss]').forEach(b=>b.dataset.miss.split(',').forEach(k=>{const r=b.querySelector('rect.grow[data-i="'+k+'"]');if(r)r.style.opacity=0}));
  s.querySelectorAll('circle.d3').forEach(d=>{d.setAttribute('fill','#1f4fb0');d.setAttribute('r',d.dataset.r0||d.getAttribute('r'))});
  if(s.querySelector('#medx'))medSet({extra:0,ordered:0,dim:0,mid:0});
  if(s.querySelector('#qx'))qSet(null);
  if(s.querySelector('#balx'))balSet(4);
  if(s.querySelector('#sdx'))sdSet({a:0,ad:0,b:0,bd:0,s:0});
  if(s.querySelector('#cfatT'))timerReset()}
function s3init(){document.querySelectorAll('[data-chart="dot3"]').forEach(b=>drawDot3(b,JSON.parse(b.dataset.cfg)));
  document.querySelectorAll('circle.d3').forEach(d=>d.dataset.r0=d.getAttribute('r'));
  document.querySelectorAll('[data-chart="hist"] rect.grow').forEach(r=>{r.dataset.c0=r.getAttribute('fill')});
  document.querySelectorAll('[data-chart="hist"]').forEach(b=>{const c=JSON.parse(b.dataset.cfg);b.querySelectorAll('rect.grow').forEach(r=>r.dataset.v=c.v[+r.dataset.i])});
  document.querySelectorAll('[data-lab]').forEach(b=>{const svg=b.querySelector('svg');JSON.parse(b.dataset.lab).forEach(([i,t])=>{const r=svg.querySelector('rect.grow[data-i="'+i+'"]');svg.append(el('text',{x:+r.getAttribute('x')+ +r.getAttribute('width')/2,y:+r.dataset.y-8,'text-anchor':'middle','font-size':20,'font-weight':700},t))})});
  /* explainers need real widths: build once the slide is first shown */
  medBuild();qBuild();balBuild();sdBuild()}
