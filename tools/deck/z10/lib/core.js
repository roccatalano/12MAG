
// ---- S3 engines: dot plots, histograms, stem plots driven by .st[data-do]; sliders; timer; tabs; check-in
const NS='http://www.w3.org/2000/svg';
function drawDot(sv){const v=JSON.parse(sv.dataset.v),lo=+sv.dataset.lo,hi=+sv.dataset.hi,W=640,px=x=>40+(x-lo)/(hi-lo)*(W-80),cnt={};
  let s=`<line x1="20" y1="200" x2="${W-20}" y2="200" stroke="#000" stroke-width="2"/>`;
  for(let x=lo;x<=hi;x++)s+=`<line x1="${px(x)}" y1="194" x2="${px(x)}" y2="206" stroke="#000"/><text x="${px(x)}" y="228" font-size="18" text-anchor="middle">${x}</text>`;
  const step=Math.min(26,170/Math.max(...Object.values(v.reduce((a,x)=>(a[x]=(a[x]||0)+1,a),{}))));
  v.forEach((x,k)=>{cnt[x]=(cnt[x]||0)+1;const cy=200-step*cnt[x]+step/2-4;s+=`<circle class="dot" data-k="${k}" cx="${px(x)}" cy="${cy}" r="${Math.min(11,step/2-1)}" fill="#555"/><text class="dn" data-k="${k}" x="${px(x)}" y="${cy+5}" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle" opacity="0">${k+1}</text>`});
  if(sv.dataset.xl)s+=`<text x="${W/2}" y="250" font-size="17" text-anchor="middle">${sv.dataset.xl}</text>`;
  s+=`<g class="mk"></g>`;sv.innerHTML=s;sv._px=px;sv._v=v}
function drawHist(sv){const c=JSON.parse(sv.dataset.cfg),n=c.v.length,X0=70,X1=580,Y0=280,Y1=20,bw=(X1-X0)/n,py=y=>Y0-(y/c.ymax)*(Y0-Y1);
  let s='';for(let y=0;y<=c.ymax;y+=c.ystep)s+=`<line x1="${X0}" y1="${py(y)}" x2="${X1}" y2="${py(y)}" stroke="#ddd"/><text x="${X0-8}" y="${py(y)+5}" font-size="15" text-anchor="end">${y}</text>`;
  let cum=0;c.v.forEach((f,i)=>{cum+=f;s+=`<rect class="b" data-i="${i}" x="${X0+i*bw}" y="${py(f)}" width="${bw}" height="${Y0-py(f)}" fill="#fff" stroke="#000" stroke-width="2"/>`+
    (f?`<text class="cu" data-i="${i}" x="${X0+i*bw+bw/2}" y="${py(f)-8}" font-size="17" font-weight="bold" fill="#d00000" text-anchor="middle" opacity="0">${cum}</text>`:'')});
  for(let i=0;i<=n;i++){const x=c.start+i*c.w;s+=`<text x="${X0+i*bw}" y="${Y0+20}" font-size="15" text-anchor="middle">${c.w<1?x.toFixed(1):+x.toFixed(2)}</text>`}
  s+=`<line x1="${X0}" y1="${Y0}" x2="${X1}" y2="${Y0}" stroke="#000" stroke-width="2"/><line x1="${X0}" y1="${Y0}" x2="${X0}" y2="${Y1}" stroke="#000" stroke-width="2"/>`;
  if(c.xl)s+=`<text x="${(X0+X1)/2}" y="${Y0+44}" font-size="16" text-anchor="middle">${c.xl}</text>`;
  s+=`<text transform="translate(18 ${(Y0+Y1)/2}) rotate(-90)" font-size="16" text-anchor="middle">${c.yl}</text>`;
  sv.setAttribute('viewBox','0 0 600 '+(c.xl?335:310));sv.innerHTML=s}
document.querySelectorAll('svg.zdp').forEach(drawDot);document.querySelectorAll('svg.zhg').forEach(drawHist);
function zApply(sl,anim){const tok=sl._zt=(sl._zt||0)+1;const T=f=>()=>{if(sl._zt===tok)f()};
  sl.querySelectorAll('svg.zdp').forEach(sv=>{sv.querySelectorAll('.dot').forEach(d=>{d.setAttribute('fill','#555');d.removeAttribute('stroke')});sv.querySelectorAll('.dn').forEach(t=>t.setAttribute('opacity',0));sv.querySelector('.mk').innerHTML=''});
  sl.querySelectorAll('svg.zhg').forEach(sv=>{sv.querySelectorAll('rect.b').forEach(r=>r.setAttribute('fill','#fff'));sv.querySelectorAll('.cu').forEach(t=>t.setAttribute('opacity',0))});
  sl.querySelectorAll('.lv').forEach(l=>l.className='lv');sl.querySelectorAll('.zkey.zkh').forEach(k=>k.classList.remove('on'));
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const last=s===anim;s.dataset.do.split(' ').forEach(a=>{const [op,id,x,y,c]=a.split(':');const el=document.getElementById(id);if(!el)return;
    const L=[...el.querySelectorAll('.lv')],ks=(x||'').split(',').map(Number);
    if(op==='dn'){const n=+x;for(let k=0;k<n;k++){const go=()=>{el.querySelector(`.dot[data-k="${k}"]`).setAttribute('fill','#1f5fbf');el.querySelector(`.dn[data-k="${k}"]`).setAttribute('opacity',1)};last?setTimeout(T(go),k*(1600/n)):go()}}
    if(op==='dm'){ks.forEach(k=>{const d=el.querySelector(`.dot[data-k="${k}"]`);d.setAttribute('fill','#d00000');d.setAttribute('stroke','#000');d.setAttribute('stroke-width',2)});
      const m=ks.reduce((t,k)=>t+el._v[k],0)/ks.length,X=el._px(m);el.querySelector('.mk').innerHTML=`<line x1="${X}" y1="10" x2="${X}" y2="200" stroke="#d00000" stroke-width="3" stroke-dasharray="7 5"/><text x="${X+8}" y="24" fill="#d00000" font-size="18" font-weight="bold">M = ${m}</text>`}
    if(op==='hc'){el.querySelectorAll('.cu').forEach((t,i)=>{const go=()=>t.setAttribute('opacity',1);last?setTimeout(T(go),i*260):go()})}
    if(op==='hm'||op==='hq')ks.forEach(i=>el.querySelector(`rect.b[data-i="${i}"]`).setAttribute('fill',op==='hm'?'#f6b3b3':'#b9cff3'));
    if(op==='lb')L.slice(+x,+y+1).forEach(l=>l.classList.add(c));
    if(op==='sk')el.querySelector('.zkey').classList.add('on');
    if(op==='lq')ks.forEach(k=>L[k].classList.add('q'));
    if(op==='lm')ks.forEach(k=>L[k].classList.add('mid'));
    if(op==='lx')ks.forEach(k=>L[k].classList.add('ex'));
    if(op==='lc'){let i=+x,j=+y,k=0;while(j-i>=2){[i,j].forEach(q=>{const go=()=>L[q].classList.add('x');last?setTimeout(T(go),k*140):go()});i++;j--;k++}}
  })})}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')&&t.dataset.do!==undefined){const sl=t.closest('.slide');if(!seen.has(sl)){seen.add(sl);zApply(sl,t.classList.contains('show')?t:null)}}
  else if(t.classList&&t.classList.contains('st')&&t.closest('.slide.z')){const sl=t.closest('.slide');if(sl.querySelector('[data-do]')&&!seen.has(sl)){seen.add(sl);zApply(sl,null)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// standard deviation
document.querySelectorAll('.slide.sdx').forEach(sl=>{const sv=sl.querySelector('svg.zsd'),r=sl.querySelector('input'),O=sl.querySelector('.zsdo'),D=[-1,-.75,-.45,-.15,.15,.45,.75,1];
  const draw=()=>{const k=+r.value/100*40,d=D.map(z=>50+Math.sign(z)*Math.round(Math.abs(z)*k)),m=d.reduce((s,v)=>s+v,0)/8,sd=Math.sqrt(d.reduce((s,v)=>s+(v-m)**2,0)/7),px=v=>30+v/100*640;
    let s=`<line x1="20" y1="230" x2="690" y2="230" stroke="#000" stroke-width="2"/>`;for(let v=0;v<=100;v+=10)s+=`<line x1="${px(v)}" y1="224" x2="${px(v)}" y2="236" stroke="#000"/><text x="${px(v)}" y="254" font-size="15" text-anchor="middle">${v}</text>`;
    s+=`<rect x="${px(m-sd)}" y="10" width="${px(m+sd)-px(m-sd)}" height="215" fill="#1f5fbf" fill-opacity=".08"/><line x1="${px(m)}" y1="10" x2="${px(m)}" y2="228" stroke="#d00000" stroke-width="3" stroke-dasharray="7 5"/>`;
    d.forEach((v,i)=>{const y=30+i*24;s+=`<line x1="${px(m)}" y1="${y}" x2="${px(v)}" y2="${y}" stroke="#1f5fbf" stroke-width="3"/><circle cx="${px(v)}" cy="${y}" r="8" fill="#555"/>`});
    sv.innerHTML=s;O.innerHTML=`Scores: ${d.join(', ')}<br>Mean $\\bar{x}$ = <b>${m.toFixed(1)}</b><br>Standard deviation $s$ = <b style="color:#1f5fbf">${sd.toFixed(2)}</b><br><span style="font-size:17px">Blue lines = distance of each score from the mean. Shaded band = mean ± one standard deviation.</span>`;
    if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};r.oninput=draw;draw()});

// ---- round 2: slide-level state (VCAA %, MC key/distractor/% bars, table highlights, running sums)
const CFU=__CFU__;
document.querySelectorAll('.slide[data-cfu]').forEach(sl=>{const f=sl.querySelector('.foot');if(!f)return;const w=document.createElement('span');w.className='zcfu';
  sl.dataset.cfu.split(' ').forEach(c=>{if(CFU[c])w.insertAdjacentHTML('beforeend',`<span><img src="${CFU[c][0]}" alt="">${CFU[c][1]}</span>`)});f.insertBefore(w,f.querySelector('.pg'))});
function z2(sl,anim){const tok=sl._z2=(sl._z2||0)+1;const T=f=>()=>{if(sl._z2===tok)f()};
  sl.querySelectorAll('.mtile[data-c],.lv[data-c]').forEach(t=>delete t.dataset.c);sl.querySelectorAll('.zfill td').forEach(t=>t.classList.remove('on'));sl.querySelectorAll('.zbox').forEach(b=>b.classList.remove('pa','pb2'));
  const S=sl.querySelector('.zstat');if(S){S.classList.remove('done');S.querySelector('b').textContent='?%'}
  const M=sl.querySelector('.zmc');if(M){M.classList.remove('pct');M.querySelectorAll('div[data-o]').forEach(o=>{o.classList.remove('right','dis');o.querySelector('.pb').style.width=0})}
  sl.querySelectorAll('.ztab td.hl').forEach(t=>t.classList.remove('hl'));sl.querySelectorAll('.ztab tr.dim').forEach(t=>t.classList.remove('dim'));
  sl.querySelectorAll('.zsumw').forEach(w=>{w.querySelectorAll('.zt').forEach(t=>{t.classList.remove('on');delete t.dataset.c});const b=w.querySelector('.zrun b');b.textContent='0';w.querySelector('.zrun i')?.remove()});
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const last=s===anim;s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');
    if(op==='stat'&&S){S.querySelector('b').textContent=id+'%';S.classList.add('done')}
    if(op==='key'&&M)M.querySelector(`[data-o="${id}"]`).classList.add('right');
    if(op==='dis'&&M)M.querySelector(`[data-o="${id}"]`).classList.add('dis');
    if(op==='tn'||op==='tclr'){const tt=[...sl.querySelectorAll(`.tl[data-t="${id}"] .mtile`)];if(op==='tclr'){tt.forEach(t=>delete t.dataset.c)}else{const st0=+x,K=+a.split(':')[3];for(let k=0;k<K;k++){const t=tt[st0+k];if(!t)continue;const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*(1500/K)):go()}}}
    if(op==='ln'){const L=[...document.getElementById(id).querySelectorAll('.lv')],st0=+x,K=+a.split(':')[3];for(let k=0;k<K;k++){const t=L[st0+k];if(!t)continue;const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*(1500/K)):go()}}
    if(op==='pair'||op==='pair2'){[id,x].forEach(q=>document.getElementById(q)?.classList.add(op==='pair'?'pa':'pb2'))}
    if(op==='pct'&&M){M.classList.add('pct');M.querySelectorAll('div[data-o]').forEach(o=>{o.querySelector('.pb').style.width=parseFloat(o.querySelector('.pc').textContent)+'%'})}
    const el=document.getElementById(id);if(!el)return;
    if(op==='fill')el.querySelector(`td[data-k="${x}"]`)?.classList.add('on');
    if(op==='tc')x.split(',').forEach(k=>el.querySelector(`td[data-k="${k}"]`)?.classList.add('hl'));
    if(op==='dim')el.querySelectorAll('tr')[+x].classList.add('dim');
    if(op==='cnt')el.querySelectorAll('.zt').forEach((t,k)=>{const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*180):go()});
    if(op==='sum'){const TT=[...el.querySelectorAll('.zt')],b=el.querySelector('.zrun b');let run=0;const dp=Math.max(...TT.map(t=>(t.textContent.split('.')[1]||'').length));
      TT.forEach((t,k)=>{const go=()=>{t.classList.add('on');run+=parseFloat(t.textContent);b.textContent=run.toFixed(dp)};last?setTimeout(T(go),k*(1800/TT.length)):go()})}
    if(op==='bal'){const go=()=>{el.querySelector('.zrun i')?.remove();el.querySelector('.zrun').insertAdjacentHTML('beforeend',`<i>÷ ${el.querySelectorAll('.zt').length} = <b style="display:inline;font-size:30px">${x}</b></i>`)};last?setTimeout(T(go),1900):go()}
  })})}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);z2(sl,t.classList.contains('show')?t:null)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// house prices: mean or median
document.querySelectorAll('.slide.house').forEach(sl=>{const sv=sl.querySelector('svg.zhs'),r=sl.querySelector('input'),O=sl.querySelector('.zhso');
  const md=a=>{const n=a.length,h=Math.floor(n/2);return n%2?a[h]:(a[h-1]+a[h])/2};
  const draw=()=>{const X=+r.value,base=[620,680,700,720,740,780,820],d=[...base,X].sort((a,b)=>a-b),med=md(d),q1=md(d.slice(0,4)),q3=md(d.slice(4)),iqr=q3-q1,lo=q1-1.5*iqr,hi=q3+1.5*iqr,mean=d.reduce((t,v)=>t+v,0)/8;
    const top=X>900?3000:1000,stp=top>1500?500:100,px=v=>30+v/top*640;let s=`<line x1="20" y1="190" x2="690" y2="190" stroke="#000" stroke-width="2"/>`;
    for(let v=0;v<=top;v+=stp)s+=`<line x1="${px(v)}" y1="184" x2="${px(v)}" y2="196" stroke="#000"/><text x="${px(v)}" y="216" font-size="15" text-anchor="middle">${v}</text>`;
    s+=`<rect x="${px(Math.max(lo,0))}" y="60" width="${px(hi)-px(Math.max(lo,0))}" height="125" fill="#1f5fbf" fill-opacity=".06"/>`;
    [[lo,'lower fence'],[hi,'upper fence']].forEach(([v,l],k)=>{if(v<0)return;s+=`<line x1="${px(v)}" y1="52" x2="${px(v)}" y2="190" stroke="#1f5fbf" stroke-width="2" stroke-dasharray="6 5"/><text x="${px(v)+(k?4:-4)}" y="246" font-size="13" fill="#1f5fbf" text-anchor="${k?'start':'end'}">${l} ${Math.round(v)}</text>`});
    d.forEach(v=>{const o=v<lo||v>hi,me=v===X;s+=`<circle cx="${px(v)}" cy="${me?145:170}" r="${me?11:8}" fill="${o?'#d00000':(me?'#fff':'#555')}" stroke="${me?'#d00000':'none'}" stroke-width="3"/>`});
    s+=`<line x1="${px(med)}" y1="30" x2="${px(med)}" y2="185" stroke="#000" stroke-width="4"/><text x="${px(med)}" y="22" font-size="16" font-weight="bold" text-anchor="middle">median</text>`;
    s+=`<line x1="${px(mean)}" y1="48" x2="${px(mean)}" y2="185" stroke="#d00000" stroke-width="4" stroke-dasharray="8 5"/><text x="${px(mean)+(mean>=med?8:-8)}" y="44" font-size="16" font-weight="bold" fill="#d00000" text-anchor="${mean>=med?'start':'end'}">mean</text>`;
    if(Math.abs(mean-med)>15)s+=`<line x1="${px(med)}" y1="100" x2="${px(mean)}" y2="100" stroke="#d00000" stroke-width="2.5" marker-end="url(#zar)"/>`;
    sv.innerHTML=`<defs><marker id="zar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#d00000"/></marker></defs>`+s;
    const out=X<lo||X>hi,fmt=v=>'$'+Math.round(v)+'k';
    O.innerHTML=`Changed sale: <b>${fmt(X)}</b><br><span style="border-top:4px solid #000;display:inline-block;width:28px;vertical-align:middle"></span> Median = <b>${fmt(med)}</b><br><span style="border-top:4px dashed #d00000;display:inline-block;width:28px;vertical-align:middle"></span> Mean = <b style="color:#d00000">${fmt(mean)}</b> <span style="font-size:16px">(${mean>=med?'+':'−'}${fmt(Math.abs(mean-med)).slice(1)} from the median)</span><br>`+
      `Fences: <b>${fmt(Math.max(lo,0))}</b> to <b>${fmt(hi)}</b><br>`+(out?`<span class="ol">${fmt(X)} is an outlier: use the median.</span>`:(Math.abs(mean-med)>=25?`<b style="color:#a06b00">No outlier yet, but the data are skewed and the mean is being pulled. The median is safer.</b>`:`<b>Symmetric, no outlier: mean ≈ median, either can be used.</b>`));
    O.innerHTML=O.innerHTML.replace(/\$(\d)/g,'&#36;$1')};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();r.value=b.dataset.v;draw()});draw()});


// ---- fit: working columns never overflow, tables and stem plots fit their box
function zfit(){document.querySelectorAll('.slide.z').forEach(sl=>{const was=sl.classList.contains('on');sl.classList.add('on');const hid=[...sl.querySelectorAll('.st:not(.show)')];hid.forEach(x=>x.style.opacity=0);sl.querySelectorAll('.st').forEach(x=>x.classList.add('zmeasure'));
  const ov=e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2;
  sl.querySelectorAll('.zw').forEach(w=>{let g=0;const L=[...w.querySelectorAll('.st.zs')];while(ov(w)&&g<40){g++;L.forEach(q=>{const f=parseFloat(getComputedStyle(q).fontSize);if(f>19)q.style.fontSize=(f*0.96)+'px'})}});
  sl.querySelectorAll('.zfig').forEach(fg=>{fg.querySelectorAll('table').forEach(t=>{let g=0;const fs=()=>parseFloat(getComputedStyle(t).fontSize);while(((t.offsetWidth>fg.clientWidth-8&&fs()>10)||(!fg.classList.contains('zmcq')&&fg.scrollHeight>fg.clientHeight+2&&fs()>16))&&g<60){g++;t.style.fontSize=(fs()*0.94)+'px'}})});
  sl.querySelectorAll('.zmcq').forEach(fg=>{let g=0;const q=fg.querySelector('.zq');while(fg.scrollHeight>fg.clientHeight+2&&g<20){g++;q.style.fontSize=(parseFloat(getComputedStyle(q).fontSize)*0.95)+'px';fg.querySelectorAll('svg').forEach(v=>v.style.maxHeight=(v.getBoundingClientRect().height*0.94)+'px')}});
  sl.querySelectorAll('.top>.q').forEach(q=>{q.querySelectorAll('table').forEach(t=>{let g=0;while(t.offsetWidth>q.clientWidth&&g<30){g++;t.style.fontSize=(parseFloat(getComputedStyle(t).fontSize)*0.94)+'px'}})});
  sl.querySelectorAll('.st').forEach(x=>x.classList.remove('zmeasure'));hid.forEach(x=>x.style.opacity='');if(!was)sl.classList.remove('on')})}
document.fonts.ready.then(()=>setTimeout(zfit,700));

// check-in ticks
document.querySelectorAll('.zcb').forEach(b=>b.onclick=e=>{e.stopPropagation();b.classList.toggle('s1')});
document.querySelectorAll('.zct').forEach(b=>{b.onclick=e=>{e.stopPropagation();b.textContent=+b.textContent+1};b.oncontextmenu=e=>{e.preventDefault();e.stopPropagation();b.textContent=Math.max(0,+b.textContent-1)}});
// timer
document.querySelectorAll('.ztime').forEach(t=>{let left=+t.dataset.s,h=null;const sh=()=>{t.textContent=String(Math.floor(left/60)).padStart(2,'0')+':'+String(left%60).padStart(2,'0');t.classList.toggle('low',left<=120)};
  t.parentNode.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();const a=b.dataset.a;clearInterval(h);h=null;
    if(a==='go')h=setInterval(()=>{left=Math.max(0,left-1);sh();if(!left)clearInterval(h)},1000);if(a==='reset'){left=+t.dataset.s;sh()}})});
// CAS tabs
document.querySelectorAll('.ztabs').forEach(tb=>tb.querySelectorAll('button').forEach(b=>b.onclick=e=>{e.stopPropagation();tb.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));
  tb.parentNode.querySelectorAll('.zcas').forEach(o=>o.hidden=o.dataset.c!==b.dataset.c)}));
// ---- stem plot standard: biggest font (same for stems and leaves) that fits the figure box; key scales with it
function zstemfit(){document.querySelectorAll('.st[data-do]').forEach(t=>t.dataset.do.split(' ').forEach(a=>{const [op,id]=a.split(':');if(op==='ln'){const z=document.getElementById(id);if(z&&z.classList.contains('zstem'))z.classList.add('zcnt')}}));document.querySelectorAll('.slide.z').forEach(sl=>{const st=[...sl.querySelectorAll('.zstem')];if(!st.length)return;const was=sl.classList.contains('on');sl.classList.add('on');
  st.forEach(z=>{const fg=z.closest('.zfig')||z.parentNode;let f=z.dataset.max?+z.dataset.max:48;const bx=fg.querySelector('svg.zbx');const row=getComputedStyle(fg).flexDirection==='row';const ok=()=>(!bx||(row?bx.getBoundingClientRect().width>=300:bx.getBoundingClientRect().height>=110))&&fg.scrollHeight<=fg.clientHeight+1&&z.scrollWidth<=fg.clientWidth-8&&z.offsetWidth<=fg.clientWidth-8;
    z.style.setProperty('--zsf',f+'px');while(!ok()&&f>16){f-=1;z.style.setProperty('--zsf',f+'px')}});
  if(!was)sl.classList.remove('on')})}
document.fonts.ready.then(()=>setTimeout(zstemfit,900));
