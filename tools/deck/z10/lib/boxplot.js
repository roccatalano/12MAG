function bxApply(sl){const V=new Map();sl.querySelectorAll('svg.zbx').forEach(sv=>V.set(sv.id,{s:new Set(),o:false}));
  sl.querySelectorAll('svg.zbd circle').forEach(c=>c.classList.remove('on'));
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const one={};s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');const v=V.get(id);
    if(op==='bdx'){sl.querySelectorAll('#'+id+' circle[data-e]').forEach(c=>c.classList.add('on'));return}
    if(!v)return;if(op==='bx')x.split(',').forEach(p=>v.s.add(p));if(op==='bxo')v.o=true;
    if(op==='bx1'){(v.b1||[]).forEach(p=>v.s.delete(p));v.b1=x.split(',');v.b1.forEach(p=>v.s.add(p))}})});
  V.forEach((v,id)=>{const sv=document.getElementById(id);const H=new Set((sv.dataset.hide||'').split(',').filter(Boolean));
    sv.querySelectorAll('[data-p]').forEach(g=>g.style.opacity=(!H.has(g.dataset.p)||v.s.has(g.dataset.p))?1:0);
    sv.querySelectorAll('.bo').forEach(c=>c.classList.toggle('on',v.o))})}
document.querySelectorAll('.slide').forEach(bxApply);
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)){seen.add(sl);bxApply(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
