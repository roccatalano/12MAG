"""Make lessons/S4-slides.pdf: one page per slide fully revealed; Do Now, APK and exit slides also get a question-only page first."""
import asyncio, os, io
from playwright.async_api import async_playwright
from PIL import Image
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1600,'height':900})
        await pg.goto(f'file://{ROOT}/lessons/S4-slides.html'); await pg.wait_for_timeout(2500)
        n=await pg.evaluate('slides.length'); pages=[]
        for k in range(n):
            q=await pg.evaluate(f'(()=>{{const c=slides[{k}].classList;return c.contains("dn")||c.contains("apk")||c.contains("ex")}})()')
            if q:
                await pg.evaluate(f'show({k})'); await pg.wait_for_timeout(1500); pages.append(await pg.screenshot())
            await pg.evaluate(f'show({k},true)'); await pg.wait_for_timeout(3200); pages.append(await pg.screenshot())
        await b.close()
    ims=[Image.open(io.BytesIO(x)).convert('RGB') for x in pages]
    ims[0].save(f'{ROOT}/lessons/S4-slides.pdf',save_all=True,append_images=ims[1:],resolution=150,quality=88)
    print('pages',len(ims))
asyncio.run(main())
