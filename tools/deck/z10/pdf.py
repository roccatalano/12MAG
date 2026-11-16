"""Vector PDF of a z10 slide deck (the slide standard).
Question slides (Example, You try, APK, exam practice, exit, CAS example) -> 2 pages: the question as it first appears,
then every step revealed. Every other slide -> 1 page, every step revealed.

Pages are REAL vector prints (Chrome's page.pdf): sharp at any zoom, selectable text, small files.
How: the deck is loaded at a true 1280x720 viewport (so zfit/zstemfit measure the real slide size), KaTeX and fonts are
waited for, and the fit-to-window scaling is switched off (#stage: no translate/scale, pinned at 0,0). For each page
state the deck is put in that state and printed to a one-page 1280x720 px PDF; the pages are then joined with pypdf.
Fallback, per page only: if a state prints to more than one page (or the print fails), that page is a 3x PNG
screenshot instead, and it is logged.
Run: python3 tools/deck/z10/pdf.py lessons/S3-slides.html lessons/S3-slides.pdf     (needs playwright + pypdf + pillow)"""
import asyncio, io, os, sys
from playwright.async_api import async_playwright
from pypdf import PdfReader, PdfWriter
from PIL import Image

PRINT_CSS = ('html,body{width:1280px!important;height:720px!important;margin:0!important;overflow:hidden!important}'
             '#stage,.stage{transform:none!important;left:0!important;top:0!important;width:1280px!important;height:720px!important;overflow:hidden!important;contain:strict}'
             '.tb,.helpbox,.cfu,.zcfu,[data-cfu]::after{visibility:hidden!important}'
             '*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}'
             '@page{size:1280px 720px;margin:0}')
PDF_OPTS = dict(width='1280px', height='720px', print_background=True,
                margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})


async def ready(pg):
    await pg.wait_for_load_state('networkidle')
    await pg.evaluate("document.fonts.ready.then(()=>1)")
    await pg.wait_for_function("!window.katex || !!document.querySelector('.katex') || !/\\$|\\\\\\(/.test(document.body.innerText)",
                               timeout=15000)


async def main(src, out):
    pages, fell = [], []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=1)
        shot = await b.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=3)   # fallback only
        await pg.goto('file://' + os.path.abspath(src)); await ready(pg); await pg.wait_for_timeout(2500)
        await pg.evaluate("document.body.classList.remove('help')")
        await pg.add_style_tag(content=PRINT_CSS)
        await pg.evaluate("window.fit=()=>{};document.getElementById('stage').style.transform='none'")
        shot_ready = False
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
                data = None
                try:
                    await pg.evaluate("document.getElementById('stage').style.transform='none'")
                    data = await pg.pdf(**PDF_OPTS)
                    if len(PdfReader(io.BytesIO(data)).pages) != 1: data = None
                except Exception as e:
                    print('print failed', k, e)
                if data is None:                              # fallback: 3x screenshot of the same state
                    if not shot_ready:
                        await shot.goto('file://' + os.path.abspath(src)); await ready(shot); await shot.wait_for_timeout(2500)
                        await shot.evaluate("document.body.classList.remove('help')")
                        await shot.add_style_tag(content='.tb,.helpbox,.cfu,.zcfu,[data-cfu]::after{visibility:hidden!important}')
                        shot_ready = True
                    await shot.evaluate(f"show({k})"); await shot.wait_for_timeout(400)
                    for _ in range(want): await shot.evaluate("fwd()"); await shot.wait_for_timeout(60)
                    await shot.wait_for_timeout(1800 if want else 300)
                    im = Image.open(io.BytesIO(await shot.screenshot())).convert('RGB')
                    buf = io.BytesIO(); im.save(buf, 'PDF', resolution=288); data = buf.getvalue()   # 3840px/288dpi = 960pt
                    fell.append(f'slide {k + 1} ({"question" if want == 0 and len(shots) == 2 else "revealed"}), page {len(pages) + 1}')
                pages.append(data)
        await b.close()
    w = PdfWriter()
    for d in pages: w.add_page(PdfReader(io.BytesIO(d)).pages[0])
    w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    w.write(out)
    print(len(pages), 'pages ->', out, os.path.getsize(out), 'bytes;', 'PNG fallback:', ', '.join(fell) if fell else 'none')

asyncio.run(main(sys.argv[1], sys.argv[2]))
