(function(){
const N=x=>Math.exp(-x*x/2),PX=z=>40+(z+3.6)/7.2*620,BASE=215,H=160,PY=z=>BASE-H*N(z);
const PCT=[[-3.3,'0.15'],[-2.5,'2.35'],[-1.5,'13.5'],[-0.5,'34'],[0.5,'34'],[1.5,'13.5'],[2.5,'2.35'],[3.3,'0.15']];
function fmt(v,d){return (+v.toFixed(d)).toFixed(d)}
function draw(sv){const c=JSON.parse(sv.dataset.cfg);let s='';
  for(let k=-3;k<=3;k++)s+=`<line x1="${PX(k)}" y1="${PY(k)}" x2="${PX(k)}" y2="${BASE}" stroke="#999" stroke-width="1.2" stroke-dasharray="4 4"/>`;
  s+='<g class="sh"></g>';let d='';for(let z=-3.6;z<=3.601;z+=0.05)d+=(d?'L':'M')+PX(z).toFixed(1)+' '+PY(z).toFixed(1);
  s+=`<path d="${d}" fill="none" stroke="#000" stroke-width="3"/><line x1="20" y1="${BASE}" x2="680" y2="${BASE}" stroke="#000" stroke-width="2"/>`;
  let y=BASE+24;
  if(c.x){s+='<g class="rx" opacity="0">';for(let k=-3;k<=3;k++)s+=`<text x="${PX(k)}" y="${y}" font-size="17" text-anchor="middle">${fmt(c.m+k*c.s,c.dec)}</text>`;s+='</g>';y+=24}
  if(c.z){s+=`<g class="rz" opacity="${c.x?0:1}">`;for(let k=-3;k<=3;k++)s+=`<text x="${PX(k)}" y="${y}" font-size="16" fill="#1f5fbf" text-anchor="middle">${k}</text>`;s+=`<text x="16" y="${y}" font-size="16" font-weight="bold" fill="#1f5fbf">z</text></g>`;y+=22}
  if(c.xl)s+=`<text x="350" y="${y+2}" font-size="16" text-anchor="middle">${c.xl}</text>`;
  s+='<g class="rp" opacity="0">'+PCT.map(([z,t])=>{const tail=Math.abs(z)>3;return `<text x="${PX(z)}" y="${tail?BASE-12:Math.max(PY(z)+((Math.abs(z)>2)?-8:30),40)}" font-size="${tail?12:16}" font-weight="bold" text-anchor="middle">${t}%</text>`}).join('')+'</g><g class="nmk"></g>';
  sv.setAttribute('viewBox','0 0 700 '+(y+12));sv.innerHTML=s}
document.querySelectorAll('svg.zn').forEach(draw);
function region(a,b,col,lab){a=+a;b=+b;let d=`M${PX(a)} ${BASE}`;for(let z=a;z<=b+1e-9;z+=0.05)d+=`L${PX(z).toFixed(1)} ${PY(z).toFixed(1)}`;d+=`L${PX(b)} ${PY(b)}L${PX(b)} ${BASE}Z`;
  const f=col==='o'?'#e8892b':'#1f5fbf';let s=`<path d="${d}" fill="${f}" fill-opacity="${col==='o'?.55:.32}"/>`;
  if(lab){const zc=Math.max(-3.2,Math.min(3.2,(Math.max(a,-3.4)+Math.min(b,3.4))/2));const yy=Math.max(22,PY(zc)-40);
    s+=`<line x1="${PX(zc)}" y1="${yy+4}" x2="${PX(zc)}" y2="${PY(zc)+12}" stroke="${col==='o'?'#a04a00':'#d00000'}" stroke-width="1.5"/><text x="${PX(zc)}" y="${yy}" font-size="22" font-weight="bold" fill="${col==='o'?'#a04a00':'#d00000'}" text-anchor="middle" stroke="#fff" stroke-width="5" paint-order="stroke">${lab}</text>`}return s}
function mark(z,col,lab){z=+z;const f={r:'#d00000',b:'#1f5fbf',g:'#1a7f1a'}[col]||'#d00000';
  return `<line x1="${PX(z)}" y1="${PY(z)-26}" x2="${PX(z)}" y2="${BASE}" stroke="${f}" stroke-width="3.5"/><circle cx="${PX(z)}" cy="${BASE}" r="6" fill="${f}"/><text x="${PX(z)}" y="${PY(z)-32}" font-size="18" font-weight="bold" fill="${f}" text-anchor="middle" stroke="#fff" stroke-width="5" paint-order="stroke">${lab}</text>`}
function apply(sl){sl.querySelectorAll('svg.zn').forEach(sv=>{sv.querySelector('.sh').innerHTML='';sv.querySelector('.nmk').innerHTML='';['rx','rp'].forEach(c=>sv.querySelector('.'+c)?.setAttribute('opacity',0));
    const c=JSON.parse(sv.dataset.cfg);if(c.x&&c.z)sv.querySelector('.rz').setAttribute('opacity',0)});
  sl.querySelectorAll('.zsmp').forEach(g=>g.style.opacity=0);
  [...sl.querySelectorAll('.st[data-do].show')].forEach(st=>st.dataset.do.split(' ').forEach(a=>{const p=a.split(':'),op=p[0];
    if(op==='smp'){sl.querySelectorAll('.zsmp').forEach(g=>g.style.opacity=1);return}
    const sv=document.getElementById(p[1]);if(!sv||!sv.classList.contains('zn'))return;
    if(op==='nx')sv.querySelector('.rx')?.setAttribute('opacity',1);
    if(op==='nz')sv.querySelector('.rz')?.setAttribute('opacity',1);
    if(op==='np')sv.querySelector('.rp').setAttribute('opacity',1);
    if(op==='ncl'){sv.querySelector('.sh').innerHTML='';sv.querySelector('.nmk').innerHTML=''}
    if(op==='ns')sv.querySelector('.sh').insertAdjacentHTML('beforeend',region(p[2],p[3],p[4],(p[5]||'').replace(/_/g,' ')));
    if(op==='nm')sv.querySelector('.nmk').insertAdjacentHTML('beforeend',mark(p[2],p[3],(p[4]||'').replace(/_/g,' ')));
  }))}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)&&sl.querySelector('svg.zn,.zsmp')){seen.add(sl);apply(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
window.ZN={PX,PY,BASE,H,N,mark,region};  // for lesson interactives (e.g. S5 two tests)
})();
