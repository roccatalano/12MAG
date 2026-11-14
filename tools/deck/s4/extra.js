/* ---------- S4: boxplots (stepped build, marks, fences, % bands) ---------- */
function drawBox(box,c){const W=c.W||1000,L=c.L||34,R=c.R||34,fs=c.fs||20,bh=c.bh||56,T=c.top!=null?c.top:64,dec=c.dec||0;
  const cy=T+bh/2+10,ay=cy+bh/2+30,H=ay+(c.xl?66:42),sx=x=>L+(x-c.min)/(c.max-c.min)*(W-L-R);box._sx=sx;
  const s=el('svg',{viewBox:`0 0 ${W} ${H}`,width:'100%'});const hide=new Set(c.hide||[]);
  const g=p=>{const e=el('g',{class:'bxp','data-p':p});if(hide.has(p))e.style.opacity=0;s.append(e);return e};
  /* axis */
  s.append(el('line',{x1:L-14,x2:W-R+14,y1:ay,y2:ay,stroke:'#333','stroke-width':2}));
  const st=c.step||1,lb=c.lab||st,n=Math.round((c.max-c.min)/st);
  for(let k=0;k<=n;k++){const x=c.min+k*st,xx=sx(x),big=Math.abs(((x-c.min)/lb)-Math.round((x-c.min)/lb))<1e-6;
    s.append(el('line',{x1:xx,x2:xx,y1:ay,y2:ay+(big?10:6),stroke:'#333','stroke-width':big?2:1.2}));
    if(big)s.append(el('text',{x:xx,y:ay+34,'text-anchor':'middle','font-size':fs},(c.fmt==='k'?x.toLocaleString('en-AU').replace(/,/g,' '):x.toFixed(dec))))}
  if(c.xl)s.append(el('text',{x:(L+W-R)/2,y:H-10,'text-anchor':'middle','font-size':fs+1,'font-weight':600,'font-style':'italic'},c.xl));
  /* bands (behind the plot) */
  (c.bands||[]).forEach(b=>{const e=g(b.p);if(!hide.has(b.p)&&!b.show)e.style.opacity=0;e.dataset.h=1;e.dataset.band=1;
    e.append(el('rect',{x:sx(b.a),width:sx(b.b)-sx(b.a),y:cy-bh/2-8,height:bh+16,rx:6,fill:b.col||'rgba(217,138,31,.22)',stroke:b.sc||'#d98a1f','stroke-width':2,'stroke-dasharray':'6 4'}),
      el('text',{x:(sx(b.a)+sx(b.b))/2,y:cy-bh/2-16-(b.lv||0)*26,'text-anchor':'middle','font-size':fs,'font-weight':800,fill:b.tc||'#8a4d00'},b.t))});
  (c.rows||[c]).forEach(r=>{const col=r.col||c.col||'#cfe0fb',sc='#1b1f2a';
    const wl=g('wl');wl.append(el('line',{x1:sx(r.lw),x2:sx(r.q1),y1:cy,y2:cy,stroke:sc,'stroke-width':2.5}));if(c.caps)wl.append(el('line',{x1:sx(r.lw),x2:sx(r.lw),y1:cy-12,y2:cy+12,stroke:sc,'stroke-width':2.5}));
    const wu=g('wu');if(r.uw>r.q3){wu.append(el('line',{x1:sx(r.q3),x2:sx(r.uw),y1:cy,y2:cy,stroke:sc,'stroke-width':2.5}));if(c.caps)wu.append(el('line',{x1:sx(r.uw),x2:sx(r.uw),y1:cy-12,y2:cy+12,stroke:sc,'stroke-width':2.5}))}
    g('box').append(el('rect',{x:sx(r.q1),width:sx(r.q3)-sx(r.q1),y:cy-bh/2,height:bh,fill:col,stroke:sc,'stroke-width':2.5}));
    g('med').append(el('line',{x1:sx(r.m),x2:sx(r.m),y1:cy-bh/2,y2:cy+bh/2,stroke:sc,'stroke-width':3.5}));
    const o=g('out');(r.out||[]).forEach(v=>o.append(el('circle',{cx:sx(v),cy,r:9,fill:'#fff',stroke:sc,'stroke-width':2.5,class:'bxo'})))});
  /* fences: dashed red lines */
  (c.fences||[]).forEach(f=>{const e=g(f.p);if(!hide.has(f.p))e.style.opacity=0;e.dataset.h=1;
    e.append(el('line',{x1:sx(f.x),x2:sx(f.x),y1:T-24,y2:ay,stroke:'#d2475b','stroke-width':3,'stroke-dasharray':'9 6'}),
      el('text',{x:sx(f.x)+(f.left?-8:8),y:T-30-(f.lv||0)*28,'text-anchor':f.left?'end':'start','font-size':fs-1,'font-weight':800,fill:'#b0263a'},f.t))});
  /* marks: value guides with labels */
  (c.marks||[]).forEach(m=>{const e=g(m.p);if(!hide.has(m.p))e.style.opacity=0;e.dataset.h=1;const xx=sx(m.x),col=m.col||'#6a3fc7',ly=T-30-(m.lv||0)*28;
    e.append(el('line',{x1:xx,x2:xx,y1:ly+8,y2:ay,stroke:col,'stroke-width':2.5,'stroke-dasharray':'5 5'}),
      el('text',{x:xx+(m.dx||0),y:ly,'text-anchor':m.anchor||'middle','font-size':fs,'font-weight':800,fill:col},m.t))});
  box.append(s)}
function bxShow(spec){let [sel,ps]=spec.split('|');const b=document.querySelector(sel);if(!b)return;
  if(ps[0]==='='){ps=ps.slice(1);b.querySelectorAll('g.bxp[data-band]').forEach(e=>e.style.opacity=0)}
  ps.split(',').forEach(p=>b.querySelectorAll(`g.bxp[data-p="${p}"]`).forEach(e=>e.style.opacity=1))}
function bxOut(spec){const [sel,col]=spec.split('|');document.querySelectorAll(sel+' circle.bxo').forEach(o=>{o.setAttribute('fill',col||'#d2475b')})}
function s4apply(s,f){if(f.dataset.bx)f.dataset.bx.split(' ').forEach(bxShow);if(f.dataset.bxo)bxOut(f.dataset.bxo)}
function s4reset(s){s.querySelectorAll('[data-chart="box"]').forEach(b=>{const c=JSON.parse(b.dataset.cfg),h=new Set(c.hide||[]);
  b.querySelectorAll('g.bxp').forEach(e=>e.style.opacity=(h.has(e.dataset.p)||e.dataset.h)?0:1);b.querySelectorAll('circle.bxo').forEach(o=>o.setAttribute('fill','#fff'))})}
function s4init(){document.querySelectorAll('[data-chart="box"]').forEach(b=>drawBox(b,JSON.parse(b.dataset.cfg)));
  document.querySelectorAll('[data-hidelab]').forEach(b=>{const hs=JSON.parse(b.dataset.hidelab);b.querySelectorAll('svg text').forEach(t=>{if(hs.includes(t.textContent))t.remove()})})}
