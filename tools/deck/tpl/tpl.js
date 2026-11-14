/* ---------- tpl: formula substitution ---------- */
function tplapply(s,f){if(f.dataset.fx==='sub'){const x=f.closest('.fx');if(x)x.classList.add('sub')}}
function tplreset(s){s.querySelectorAll('.fx.sub').forEach(x=>x.classList.remove('sub'))}
