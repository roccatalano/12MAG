import asyncio, sys, os, pathlib
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1280,'height':720})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto(pathlib.Path(sys.argv[1]).resolve().as_uri());await pg.wait_for_timeout(3000)
    await pg.evaluate("document.body.classList.remove('help')")
    n=await pg.evaluate("document.querySelectorAll('.slide').length");issues=[]
    for k in range(n):
      await pg.evaluate(f"show({k})");steps=await pg.evaluate(f"document.querySelectorAll('.slide')[{k}].querySelectorAll('.st').length")
      for j in range(steps+1):
        if j: await pg.evaluate("fwd()"); await pg.wait_for_timeout(120)
        r=await pg.evaluate(f"""(()=>{{const sl=document.querySelectorAll('.slide')[{k}];const o=[];
          sl.querySelectorAll('.zw,.zfig,.top>.q,.col,.zb').forEach(e=>{{if(e.scrollHeight>e.clientHeight+3||e.scrollWidth>e.clientWidth+3)o.push(e.className)}});
          sl.querySelectorAll('.st.show').forEach(e=>{{const r=e.getBoundingClientRect(),w=e.closest('.zw,.col');if(w){{const q=w.getBoundingClientRect();if(r.bottom>q.bottom+2||r.right>q.right+2)o.push('clip:'+e.textContent.slice(0,30))}}}});return o}})()""")
        if r: issues.append((k+1,j,r))
      await pg.wait_for_timeout(2200);await pg.screenshot(path=os.path.join(sys.argv[2] if len(sys.argv)>2 else '/tmp', f's{k+1:02d}.png'))
    print('errors',errs[:5]);print('issues',len(issues))
    seen=set()
    for i in issues:
      if (i[0],str(i[2])) not in seen: seen.add((i[0],str(i[2])));print(i)
    await b.close()
asyncio.run(main())
