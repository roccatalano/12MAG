import asyncio, sys, os
from playwright.async_api import async_playwright
HTML='file:///home/claude/teaching-dashboard-2027/lessons/gm12/S3-slides.html'
OUT='/home/claude/s3/shots'; os.makedirs(OUT,exist_ok=True)
which=[int(x) for x in sys.argv[1].split(',')] if len(sys.argv)>1 and sys.argv[1] else None
mid=sys.argv[2] if len(sys.argv)>2 else ''   # e.g. "10:2" = slide 10 after 2 steps
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1600,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
        await pg.goto(HTML); await pg.wait_for_timeout(2500)
        n=await pg.evaluate('slides.length')
        for k in (which or range(1,n+1)):
            await pg.evaluate(f'show({k-1},true)'); await pg.wait_for_timeout(3200)
            await pg.screenshot(path=f'{OUT}/s{k:02d}.png')
        for spec in filter(None,mid.split(',')):
            k,st=map(int,spec.split(':'))
            await pg.evaluate(f'show({k-1})')
            for _ in range(st): await pg.evaluate('next()'); await pg.wait_for_timeout(250)
            await pg.wait_for_timeout(2500); await pg.screenshot(path=f'{OUT}/m{k:02d}_{st}.png')
        # overflow check: content wider/taller than the slide
        ov=await pg.evaluate('''slides.map((s,k)=>{show(k,true);const r=s.getBoundingClientRect();let bad=[];s.querySelectorAll('*').forEach(e=>{const q=e.getBoundingClientRect();if(q.width&&(q.right>r.right+1||q.bottom>r.bottom+1))bad.push(e.className||e.tagName)});return bad.length?(k+1)+':'+bad.slice(0,4).join('|'):null}).filter(Boolean)''')
        print('overflow',ov); print('errors',errs[:5]); await b.close()
asyncio.run(main())
