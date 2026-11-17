"""Build the chapter workbook (student + solutions): one booklet per chapter, printed with the copier's
booklet mode (A4 pages in reading order, 2 per A3 sheet, folded + stapled; padded to a multiple of 4 pages).

    python3 tools/deck/chapter_workbook.py 1

p. 1  cover: chapter title, Name/Class/Teacher, contents (worksheet + practice page per lesson)
p. 2  the chapter coursework check (tools/coursework/ch<n>.py: I check / Teacher check)
then each lesson's guided worksheet in its WORKBOOK edition (WS_WORKBOOK=1 in tools/deck/ws2.py: no skills
checklist / coursework box) with that lesson's practice questions (Insight, from tools/revision/ch<n>/, via
ws2.practice()) flowing on straight after its exit tasks.
Writes lessons/Ch<n>-workbook.pdf + lessons/Ch<n>-workbook-solutions.pdf. Individual worksheets are not changed.
"""
import io, os, subprocess, sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = {
    1: dict(title='Investigating data distributions', aos='AoS 1 · Data analysis',
            lessons=[('S1', '1A–1B', 'Types of data and categorical data'),
                     ('S2', '1C–1E', 'Displaying and describing numerical data'),
                     ('S3', '1F', 'Measures of centre and spread'),
                     ('S4', '1G', 'The five-number summary and the boxplot'),
                     ('S5', '1H–1I', 'The normal distribution and standardised scores')]),
}


def cover_html(ch, C, rows, sol):
    tr = ''.join(f'<tr><td class="nw">Lesson {s[1:]}</td><td>{c}</td><td>{t}</td><td class="nw">Worksheet p. {w} · Practice p. {p}</td></tr>' for s, c, t, w, p in rows)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}body{{margin:0;font-family:Arial,"Liberation Sans",Helvetica,sans-serif}}
.pg{{width:210mm;height:297mm;box-sizing:border-box;padding:18mm 18mm}}
.top{{display:flex;justify-content:space-between;font-size:10pt;border-bottom:1.5px solid #000;padding-bottom:2mm}}
.ch{{font-size:44pt;font-weight:bold;margin:22mm 0 2mm}}h1{{font-size:26pt;margin:0 0 4mm}}h2{{font-size:12.5pt;font-weight:normal;margin:0 0 12mm;color:#333}}
.sol{{color:#c00}}.name{{font-size:11pt;display:flex;gap:8mm;margin-bottom:12mm}}.name span{{flex:1;border-bottom:1px solid #000;padding-bottom:1mm}}
h3{{font-size:12pt;margin:0 0 4mm}}
table{{border-collapse:collapse;width:100%;font-size:10pt}}th,td{{border:1px solid #000;padding:2.6mm 3mm;text-align:left;vertical-align:middle}}th{{background:#eee}}.nw{{white-space:nowrap}}
.note{{font-size:9.5pt;color:#333;margin-top:3mm}}
</style></head><body><div class="pg"><div class="top"><span>VCE General Maths 3&amp;4</span><span>{C["aos"]}</span></div>
<div class="ch">Chapter {ch}{' <span class="sol">· SOLUTIONS</span>' if sol else ''}</div><h1>{C["title"]}</h1><h2>Workbook · guided worksheets, practice questions and coursework check</h2>
<div class="name"><span>Name:</span><span>Class:</span><span>Teacher:</span></div><h3>Contents</h3>
<table><tr><th>Lesson</th><th>Subchapters</th><th>Title</th><th>Pages</th></tr><tr><td>—</td><td>Ch {ch}</td><td>Coursework check</td><td>p. 2</td></tr>{tr}</table>
<p class="note">After each lesson: finish the guided worksheet, then do its practice questions and correct them in a different colour. Tick each item on the coursework check (p. 2) as you go.</p></div></body></html>'''


def render(html):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.set_content(html)
        x = pg.pdf(prefer_css_page_size=True, print_background=True); b.close(); return x


def practice_page(f):
    n = len(PdfReader(f).pages)
    return next((i for i in range(1, n + 1) if 'Practice questions' in subprocess.run(
        ['pdftotext', '-f', str(i), '-l', str(i), f, '-'], capture_output=True, text=True).stdout), n)


def build(ch):
    C = CHAPTERS[ch]
    env = dict(os.environ, WS_WORKBOOK='1')
    for s, *_ in C['lessons']:
        subprocess.run([sys.executable, str(ROOT / f'tools/deck/{s.lower()}/worksheet.py')], check=True, env=env)
    subprocess.run([sys.executable, str(ROOT / f'tools/coursework/ch{ch}.py')], check=True)
    check = PdfReader(ROOT / f'lessons/Ch{ch}-coursework-check.pdf')
    for sol in (False, True):
        suf = '-solutions' if sol else ''
        rows, page = [], 3
        for s, c, t in C['lessons']:
            f = f'/tmp/wb/{s}-worksheet{suf}.pdf'
            rows.append((s, c, t, page, page + practice_page(f) - 1)); page += len(PdfReader(f).pages)
        w = PdfWriter()
        w.append(PdfReader(io.BytesIO(render(cover_html(ch, C, rows, sol)))))
        w.append(check, pages=(0, 1))
        for s, *_ in C['lessons']: w.append(PdfReader(f'/tmp/wb/{s}-worksheet{suf}.pdf'))
        content = len(w.pages); W, H = w.pages[0].mediabox.width, w.pages[0].mediabox.height
        while len(w.pages) % 4: w.add_blank_page(width=W, height=H)
        w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
        out = ROOT / f'lessons/Ch{ch}-workbook{suf}.pdf'
        with open(out, 'wb') as fh: w.write(fh)
        print('built', out.name, len(w.pages), 'pages; content', content, rows)


if __name__ == '__main__':
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
