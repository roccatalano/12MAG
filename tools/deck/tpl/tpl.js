/* ---------- tpl: formula substitution ---------- */
/* dot plot: a dashed line between two neighbouring dots (e.g. the 20.5th position) */
function dotSplit(spec){const [sel,i,lab]=spec.split('|');const box=document.querySelector(sel);if(!box)return;const svg=box.querySelector('svg');
  const a=svg.querySelector('circle[data-i="'+i+'"]'),b=svg.querySelector('circle[data-i="'+(+i+1)+'"]');if(!a||!b)return;
  const ax=+a.getAttribute('cx'),ay=+a.getAttribute('cy'),bx=+b.getAttribute('cx'),by=+b.getAttribute('cy'),r=+a.getAttribute('r');
  const g=el('g',{class:'dsplit'});
  if(Math.abs(ax-bx)<1){const y=(ay+by)/2;g.append(el('line',{x1:ax-r*2.6,x2:ax+r*2.6,y1:y,y2:y,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'7 5'}),el('text',{x:ax+r*3,y:y+7,'font-size':22,'font-weight':800,fill:'#b0263a'},lab||''))}
  else{const x=(ax+bx)/2;g.append(el('line',{x1:x,x2:x,y1:Math.min(ay,by)-r*2,y2:Math.max(ay,by)+r,stroke:'#d2475b','stroke-width':4,'stroke-dasharray':'7 5'}),el('text',{x:x+6,y:Math.min(ay,by)-r*2,'font-size':22,'font-weight':800,fill:'#b0263a'},lab||''))}
  svg.append(g)}
function tplapply(s,f){if(f.dataset.dsplit)dotSplit(f.dataset.dsplit);if(f.dataset.fx==='sub'){const x=f.closest('.fx');if(x)x.classList.add('sub')}}
function tplreset(s){s.querySelectorAll('g.dsplit').forEach(g=>g.remove());s.querySelectorAll('.fx.sub').forEach(x=>x.classList.remove('sub'))}
