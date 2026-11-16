"""Build a combined chapter workbook from the lesson guided worksheets.

    python3 tools/deck/chapter_workbook.py 1 S1 S2 S3 S4 S5

Writes lessons/Ch<n>-workbook.pdf (student) and lessons/Ch<n>-workbook-solutions.pdf:
a cover page with a contents table, then each lesson's worksheet PDF in order.
Each lesson starts on an odd page (a blank page is added after a lesson with an odd
page count) so the workbook prints double-sided with every lesson on a fresh sheet.
Rebuild the lesson worksheets first (tools/deck/s#/worksheet.py).
"""
import asyncio, html, io, re, sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[2]
AOS = {1: 'AoS 1 · Data analysis'}


def lesson_info(s):
    h = (ROOT / f'lessons/{s}-worksheet.html').read_text(encoding='utf-8')
    code = re.search(r'<div class="code">(.*?)</div>', h).group(1)
    title = re.sub(r'<span class="solmark">.*?</span>', '', re.search(r'<div class="title">.*?<h1>(.*?)</h1>', h, re.S).group(1))
    return re.sub('<[^>]+>', '', code).strip(), re.sub('<[^>]+>', '', title).strip()


def cover_html(ch, rows, sol):
    tr = ''.join(f'<tr><td>Lesson {s[1:]}</td><td>{html.escape(c)}</td><td>{html.escape(t)}</td><td class="p">{p}</td></tr>' for s, c, t, p in rows)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}body{{margin:0;font-family:Arial,Helvetica,sans-serif}}
.pg{{width:210mm;height:297mm;box-sizing:border-box;padding:18mm 18mm;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;font-size:10pt;border-bottom:1.5px solid #000;padding-bottom:2mm}}
h1{{font-size:30pt;margin:40mm 0 4mm}}h2{{font-size:16pt;font-weight:normal;margin:0 0 14mm;color:#333}}
.sol{{color:#c00;font-weight:bold}}
table{{border-collapse:collapse;width:100%;font-size:11pt}}th,td{{border:1px solid #000;padding:3mm 3mm;text-align:left}}th{{background:#eee}}td.p,th.p{{text-align:center;width:18mm}}
.name{{margin-top:auto;font-size:12pt;display:flex;gap:10mm}}.name span{{flex:1;border-bottom:1px solid #000;padding-bottom:1mm}}
</style></head><body><div class="pg"><div class="top"><span>VCE General Maths 3&amp;4</span><span>{AOS.get(ch, '')}</span></div>
<h1>Chapter {ch} workbook{' <span class="sol">· SOLUTIONS</span>' if sol else ''}</h1><h2>Guided worksheets for every lesson, in lesson order</h2>
<table><tr><th>Lesson</th><th>Subchapters</th><th>Title</th><th class="p">Page</th></tr>{tr}</table>
<div class="name"><span>Name:</span><span>Class:</span></div></div></body></html>'''


async def render(htmls):
    from playwright.async_api import async_playwright
    out = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        for h in htmls:
            await pg.set_content(h)
            out.append(await pg.pdf(prefer_css_page_size=True, print_background=True))
        await b.close()
    return out


def build(ch, lessons):
    info = [(s, *lesson_info(s)) for s in lessons]
    for sol in (False, True):
        suf = '-solutions' if sol else ''
        parts = [PdfReader(ROOT / f'lessons/{s}-worksheet{suf}.pdf') for s in lessons]
        # cover = page 1, blank page 2, lessons start on odd pages
        rows, page = [], 3
        for (s, c, t), r in zip(info, parts):
            rows.append((s, c, t, page))
            n = len(r.pages)
            page += n + (n % 2)
        cover = asyncio.run(render([cover_html(ch, rows, sol)]))[0]
        w = PdfWriter()
        w.append(PdfReader(io.BytesIO(cover)))
        w.add_blank_page(width=w.pages[0].mediabox.width, height=w.pages[0].mediabox.height)
        for r in parts:
            w.append(r)
            if len(r.pages) % 2:
                w.add_blank_page(width=w.pages[0].mediabox.width, height=w.pages[0].mediabox.height)
        w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
        out = ROOT / f'lessons/Ch{ch}-workbook{suf}.pdf'
        with open(out, 'wb') as f:
            w.write(f)
        print('built', out.name, len(w.pages), 'pages')


if __name__ == '__main__':
    build(int(sys.argv[1]), sys.argv[2:] or ['S1', 'S2', 'S3', 'S4', 'S5'])
