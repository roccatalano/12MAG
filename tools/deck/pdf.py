"""Static PDF of a slide deck (Rocco, 15 Nov):
question slides (Do Now, APK, worked example, you try, exit, CAS) -> 2 pages: the question as it first appears, then the final frame;
every other slide (title, Learn, key ideas, check-in, coursework, videos) -> 1 page: the final frame.
Run: python3 tools/deck/pdf.py lessons/S1-slides.html lessons/S1-slides.pdf   (needs playwright + /usr/bin/google-chrome)"""
import asyncio, sys, os, tempfile
from playwright.async_api import async_playwright
from PIL import Image
Q={'dn','apk','we','yt','ex'}  # slide classes that get a question-only page first
async def main(src,out):
    tmp=tempfile.mkdtemp(); pages=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1600,'height':900},device_scale_factor=1.5)
        await pg.goto('file://'+os.path.abspath(src)); await pg.wait_for_timeout(2500)
        await pg.add_style_tag(content='.vid,.cfu,.ytf iframe{visibility:hidden}')  # no buttons / embedded players in print
        n=await pg.evaluate('slides.length')
        for k in range(n):
            cls=set((await pg.evaluate(f'slides[{k}].className')).split())
            shots=([False] if cls&Q else [])+[True]
            for end in shots:
                await pg.evaluate(f'show({k},{str(end).lower()})'); await pg.wait_for_timeout(4200 if end else 900)
                f=f'{tmp}/{len(pages):03d}.png'; await pg.screenshot(path=f); pages.append(f)
        await b.close()
    ims=[Image.open(f).convert('RGB') for f in pages]
    ims[0].save(out,save_all=True,append_images=ims[1:],resolution=144)
    print(len(pages),'pages ->',out)
asyncio.run(main(sys.argv[1],sys.argv[2]))
