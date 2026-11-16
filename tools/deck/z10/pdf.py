"""Static PDF of a z10 slide deck (the slide standard; replaces tools/deck/pdf.py for these decks).
Question slides (Example, You try, APK, exam practice, exit, CAS example) -> 2 pages: the question as it first appears,
then every step revealed. Every other slide -> 1 page, every step revealed.
Pages are screenshots (1.5x, so text stays sharp when projected or printed): printing the live deck with
Chrome's print engine re-fits the stage and cuts slides, so we don't.
Run: python3 tools/deck/z10/pdf.py lessons/S3-slides.html lessons/S3-slides.pdf     (needs playwright + pypdf)"""
import asyncio, os, sys, tempfile
from playwright.async_api import async_playwright
from PIL import Image


async def main(src, out):
    tmp = tempfile.mkdtemp(); pages = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=1.5)
        await pg.goto('file://' + os.path.abspath(src)); await pg.wait_for_timeout(3000)
        await pg.evaluate("document.body.classList.remove('help')")
        await pg.add_style_tag(content='.tb,.helpbox,.cfu,.zcfu,[data-cfu]::after{visibility:hidden!important}')
        n = await pg.evaluate("document.querySelectorAll('.slide').length")
        for k in range(n):
            cls = set((await pg.evaluate(f"document.querySelectorAll('.slide')[{k}].className")).split())
            steps = await pg.evaluate(f"document.querySelectorAll('.slide')[{k}].querySelectorAll('.st').length")
            await pg.evaluate(f"show({k})"); await pg.wait_for_timeout(400)
            shots = ([0] if ('ex' in cls and steps) else []) + [steps]
            done = 0
            for want in shots:
                while done < want:
                    await pg.evaluate("fwd()"); done += 1; await pg.wait_for_timeout(60)
                await pg.wait_for_timeout(1800 if want else 300)
                f = f'{tmp}/{len(pages):03d}.png'
                await pg.screenshot(path=f); pages.append(f)
        await b.close()
    im = [Image.open(f).convert('RGB') for f in pages]
    im[0].save(out, save_all=True, append_images=im[1:], resolution=144)
    print(len(pages), 'pages ->', out)

asyncio.run(main(sys.argv[1], sys.argv[2]))
