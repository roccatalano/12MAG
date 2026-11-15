"""Guided worksheet library, CFAT / revision-booklet style (Rocco, 15 Nov 2026).
Questions in boxes, blank working space (no ruled lines), answers in red on the solutions copy (same layout, same page count).
Running header: 'VCE General Maths 3&4' left, AoS right; page number at the bottom. No textbook references: exam questions name the VCAA source only.
Used by tools/deck/<s#>/worksheet.py (model: tools/deck/s1/worksheet.py)."""
import os, asyncio
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RED = '#c00'

def css(aos):
    return f"""
@page {{ size:A4; margin:13mm 12mm 12mm 12mm;
  @top-left {{ content:"VCE General Maths 3&4"; font:9pt Arial, sans-serif; color:#444; }}
  @top-right {{ content:"{aos}"; font:9pt Arial, sans-serif; color:#444; }}
  @bottom-center {{ content:"Page " counter(page) " of " counter(pages); font:8.5pt Arial, sans-serif; color:#444; }} }}
* {{ box-sizing:border-box; }}
body {{ font-family:Arial,"Liberation Sans",Helvetica,sans-serif; font-size:10pt; line-height:1.32; color:#000; margin:0; }}
.title {{ display:flex; align-items:center; gap:4mm; border:2px solid #000; padding:2mm 4mm; margin-bottom:3mm; }}
.title .code {{ font-size:16pt; font-weight:bold; border-right:2px solid #000; padding-right:4mm; white-space:nowrap; }}
.title h1 {{ font-size:15pt; margin:0; flex:1; }}
.solmark {{ display:none; color:{RED}; }} .sol .solmark {{ display:inline; }}
.secthd {{ font-weight:bold; text-transform:uppercase; letter-spacing:.4px; font-size:10.5pt; margin:2mm 0 1.2mm; display:flex; justify-content:space-between; break-after:avoid; }}
.secthd span {{ text-transform:none; letter-spacing:0; font-weight:normal; font-size:9pt; }}
.box {{ border:1.2px solid #000; margin-bottom:2mm; break-inside:avoid; display:flex; flex-direction:column; }}
.box > .hd {{ font-weight:bold; font-size:10pt; text-transform:uppercase; letter-spacing:.3px; border-bottom:1.2px solid #000; padding:1mm 3mm; background:#eee; display:flex; justify-content:space-between; gap:3mm; }}
.box > .hd span {{ text-transform:none; font-weight:normal; letter-spacing:0; font-size:9pt; }}
.box > .bd {{ padding:2mm 3mm; flex:1; display:flex; flex-direction:column; }}
.pair {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:2.5mm; margin-bottom:2.5mm; break-inside:avoid; }}
.pair > .box {{ margin-bottom:0; }}
.q {{ margin:0 0 1.5mm; }}
.row {{ display:flex; gap:3mm; align-items:flex-start; }} .row > * {{ min-width:0; }}
.fig {{ text-align:center; flex:none; }}
.space {{ position:relative; flex:none; }}
.space.grow {{ flex:1; }}
.ans {{ visibility:hidden; color:{RED}; font-size:9.3pt; }}
.sol .ans {{ visibility:visible; }}
.space > .ans {{ position:absolute; left:0; right:0; top:.5mm; }}
.pt {{ display:flex; gap:2mm; padding:.5mm 6mm .5mm 3mm; margin:0 -3mm; border-bottom:1px dashed #bbb; }} .parts > .pt.nb {{ border-bottom:none; }}
.parts > .pt.vr {{ border-right:1px dashed #bbb; margin-right:0; }} .parts > .pt.cl:not(.c0) {{ margin-left:0; padding-left:3mm; }} .pt > b {{ min-width:4mm; flex:none; }} .pt > div {{ flex:1; }}
.parts {{ display:grid; gap:0; }}
.mc {{ display:grid; gap:.4mm 4mm; margin:1mm 0; }} .mc b {{ display:inline-block; width:5mm; }}
.mc .ok {{ display:none; color:{RED}; font-weight:bold; }} .sol .mc .right .ok {{ display:inline; }} .sol .mc .right span {{ color:{RED}; }}
.why {{ visibility:hidden; color:{RED}; font-size:8.6pt; line-height:1.2; }} .sol .why {{ visibility:visible; }}
.wl {{ border-bottom:1px solid #777; height:8mm; margin:.5mm 0 1mm; display:flex; align-items:flex-end; padding-bottom:.6mm; }}
.ey .eyh {{ display:grid; grid-template-columns:1fr 1fr; border-bottom:1.2px solid #000; background:#eee; font-weight:bold; font-size:8.8pt; text-transform:uppercase; letter-spacing:.3px; }}
.ey .eyh > div {{ padding:1mm 3mm; }} .ey .eyh > div:first-child, .ey .eyb > div:first-child {{ border-right:1.2px solid #000; }}
.ey .eyb {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); flex:1; }}
.ey .eyb > .bd {{ padding:2mm 3mm; display:flex; flex-direction:column; }}
.space .ans svg line, .space .ans svg rect {{ stroke:{RED}; }} .space .ans svg text {{ fill:{RED}; }} .space .ans svg rect {{ fill-opacity:.25; }}
.pg {{ height:271mm; display:flex; flex-direction:column; break-after:page; overflow:hidden; }} .pg:last-child {{ break-after:auto; }}
.pg > .box, .pg > .pair {{ flex:1 1 auto; }} .pg > .title, .pg > .secthd, .pg > .box.lisbox {{ flex:none; }}
.pg > .pair > .box {{ height:100%; }}
.qsep {{ border-top:1.2px solid #000; margin:1.5mm -3mm 1.5mm; }}
.src {{ font-size:8pt; font-style:italic; color:#444; text-align:right; margin-top:auto; padding-top:1mm; }}
.guess {{ font-size:9pt; margin-top:1mm; padding:.6mm 2mm; border:1px dashed #000; display:flex; align-items:flex-end; gap:1.5mm; flex-wrap:wrap; }}
.guess i {{ display:inline-block; width:14mm; border-bottom:1px solid #000; height:4mm; }}
.sol .guess::after {{ content:attr(data-a); color:{RED}; font-weight:bold; margin-left:2mm; }}
table.t {{ border-collapse:collapse; font-size:9.3pt; margin:1mm auto; }}
table.t th, table.t td {{ border:1px solid #000; padding:.4mm 2.2mm; text-align:center; }}
table.t th {{ background:#eee; }} table.t td.l, table.t th.l {{ text-align:left; }}
table.t.fill td {{ height:6mm; min-width:15mm; }}
table.t.tiny {{ font-size:7.2pt; margin:0; }} table.t.tiny th, table.t.tiny td {{ padding:.1mm .8mm; }} table.t.tiny th {{ font-weight:normal; }}
table.t .a {{ color:{RED}; visibility:hidden; }} .sol table.t .a {{ visibility:visible; }}
.data {{ font-family:"Courier New",monospace; font-size:10pt; letter-spacing:.4px; margin:1mm 0 1.5mm; text-align:center; }}
.tpl {{ line-height:2.05; margin:1mm 0; }}
.bx {{ display:inline-block; border-bottom:1px solid #000; min-width:20mm; height:5.6mm; line-height:5.2mm; padding:0 1.5mm; vertical-align:middle; text-align:center; position:relative; }}
.bx i {{ position:absolute; left:0; right:0; top:100%; font-size:6.5pt; font-style:normal; color:#666; line-height:1.1; white-space:nowrap; }}
.bx u {{ text-decoration:none; color:{RED}; visibility:hidden; font-size:9pt; white-space:nowrap; }} .sol .bx u {{ visibility:visible; }}
.solfig {{ visibility:hidden; }} .sol .solfig {{ visibility:visible; }}
.scg {{ display:grid; grid-template-columns:1fr; }}
.sc {{ display:grid; grid-template-columns:6mm 1fr; gap:1mm 2mm; padding:1mm 2mm; border-bottom:1px solid #000; }} .sc:last-child {{ border-bottom:none; }}
.tick {{ width:4.6mm; height:4.6mm; border:1.2px solid #000; }}
.hwg {{ display:grid; border:1px solid #000; }}
.hwg > div {{ border-right:1px solid #000; padding:1.5mm; text-align:center; display:flex; flex-direction:column; align-items:center; gap:1mm; }} .hwg > div:last-child {{ border-right:none; }}
.hwh {{ font-weight:bold; text-transform:uppercase; font-size:9pt; }}
.sig {{ display:flex; gap:4mm; margin-top:2mm; }}
.stamp {{ width:30mm; height:15mm; border:1.2px dashed #000; font-size:8pt; color:#555; display:flex; align-items:flex-end; justify-content:center; flex:none; }}
.sig .ln {{ flex:1; display:flex; flex-direction:column; justify-content:space-around; font-size:9pt; }}
.sig .ln div {{ display:flex; gap:2mm; align-items:flex-end; }} .sig .ln span {{ white-space:nowrap; }} .sig .ln i {{ flex:1; min-width:15mm; border-bottom:1px solid #000; height:6mm; }} .sig .ln i.d {{ flex:none; width:18mm; min-width:0; }}
.lis {{ column-count:2; column-gap:6mm; margin:0; padding-left:4mm; font-size:8.8pt; line-height:1.2; }} .lis li {{ margin:0; }} .lis li {{ break-inside:avoid; }}
"""

# ---------------------------------------------------------------- building blocks
PAGE = '<!--PAGE-->'   # put between groups in P: each group fills exactly one A4 page (boxes stretch to use the room)
def title(code, t): return f'<div class="title"><div class="code">{code}</div><h1>{t} <span class="solmark">· SOLUTIONS</span></h1></div>'
def sect(t, right=''): return f'<div class="secthd">{t}<span>{right}</span></div>'
def box(hd, body, right=''): return f'<div class="box"><div class="hd">{hd}<span>{right}</span></div><div class="bd">{body}</div></div>'
def pair(a, b): return f'<div class="pair">{a}{b}</div>'
def q(t): return f'<p class="q">{t}</p>'
def src(t): return f'<div class="src">{t}</div>'
def space(mm, a='', grow=False): return f'<div class="space{" grow" if grow else ""}" style="min-height:{mm}mm"><div class="ans">{a}</div></div>'
def ans(a): return f'<span class="ans">{a}</span>'
def wline(a=''):
    """Blank space for a one-word / one-line answer (CFAT style: no ruled line; red on the solutions copy)."""
    return space(8, a)
def parts(items, cols=1):
    """items: (label, text, answer, mm of blank space under the part; 'L' = one writing line)"""
    return f'<div class="parts" style="grid-template-columns:repeat({cols},minmax(0,1fr))">' + ''.join(
        f'<div class="pt{" nb" if j >= len(items) - ((len(items) - 1) % cols + 1) else ""}{(" c0" if j % cols == 0 else "") + (" cl" if j % cols == cols - 1 else " vr") if cols > 1 else ""}"><b>{k}</b><div>{t}{space(7, a) if mm == "L" else space(mm, a)}</div></div>' for j, (k, t, a, mm) in enumerate(items)) + '</div>'
QSEP = '<div class="qsep"></div>'   # solid line between separate questions (1, 2, 3) inside one box; dashed lines stay between parts a, b
def exyt(eh, eb, yh, yb):
    """Example and You try in ONE box, split down the middle."""
    return (f'<div class="box ey"><div class="eyh"><div>{eh}</div><div>{yh}</div></div>'
            f'<div class="eyb"><div class="bd">{eb}</div><div class="bd">{yb}</div></div></div>')
def solfig(mm, fig):
    """Blank space for students; the answer figure drawn in red on the solutions copy."""
    return space(mm, fig)
def mc(opts, key, cols=1):
    return f'<div class="mc" style="grid-template-columns:repeat({cols},auto)">' + ''.join(
        f'<div class="{"right" if "ABCDE"[i] == key else ""}"><b>{"ABCDE"[i]}.</b><span>{o}</span><span class="ok">&nbsp;✓</span></div>' for i, o in enumerate(opts)) + '</div>'
def why(t): return f'<div class="why">{t}</div>'
def guess(a, mcq=True):
    return ''  # Rocco, 15 Nov: 'guess the %' boxes removed from worksheets (clutter)
    return f'<div class="guess" data-a="{a}">Guess the % of students who got this right <i></i>' + (' &nbsp; Most common wrong answer <i style="width:9mm"></i>' if mcq else '') + '</div>'
def table(rows, head=True, cls='t', style=''):
    out = f'<table class="{cls}" style="{style}">'
    for i, r in enumerate(rows):
        tag = 'th' if head and i == 0 else 'td'
        out += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in r) + '</tr>'
    return out + '</table>'
def a(x): return f'<span class="a">{x}</span>'
def ftab(var, rows, total, blank=True, pcth='Percentage (%)'):
    """Frequency table. blank=True: number and % cells empty for students, red on the solutions copy."""
    f = a if blank else (lambda x: x)
    return table([[var, 'Number', pcth]] + [[r[0], f(r[1]), f(r[2])] for r in rows] + [['<b>Total</b>', f(f'<b>{total[0]}</b>'), f(f'<b>{total[1]}</b>')]], cls='t fill' if blank else 't')
def report(toks):
    """Report template: text with boxed blanks (small label under each box; filled in red on the solutions copy)."""
    return '<p class="tpl">' + ''.join(t if isinstance(t, str) else f'<span class="bx"><u>{t[1]}</u><i>{t[0]}</i></span>' for t in toks) + '</p>'
def lis(L): return box('Learning intentions', '<ul class="lis">' + ''.join(f'<li>{x}</li>' for x in L) + '</ul>').replace('class="box"', 'class="box lisbox"', 1)
def close(SC, cols, rev):
    ck = box('Skills checklist', '<div class="scg">' + ''.join(f'<div class="sc"><div class="tick"></div><div><b>{i}.</b> {s}</div></div>' for i, s in enumerate(SC, 1)) + '</div>', 'Tick when you can')
    cw = box('Coursework · Cambridge exercises', f'<div class="hwg" style="grid-template-columns:repeat({len(cols)+1},1fr)">' + ''.join(f'<div><div class="hwh">{h}</div><div>{t}</div><div class="tick"></div></div>' for h, t in cols)
             + f'<div><div class="hwh">Revision booklet</div><div>{rev}</div><div class="tick"></div></div></div>'
             '<div class="sig"><div class="stamp">Teacher stamp</div><div class="ln"><div><span>Student signature</span><i></i></div><div><span>Parent signature</span><i></i></div><div><span>Date</span><i></i></div></div></div>', 'Tick when done')
    return f'<div class="pair" style="grid-template-columns:.85fr 1.15fr">{ck}{cw}</div>'

# ---------------------------------------------------------------- figures (static SVG)
SHADE = ['#fff', '#bbb', '#555']
def _grid(W, H, L, T, B, ymax, ystep, yl, xl):
    y0 = H - B; k = (H - T - B) / ymax; o = []; y = 0
    while y <= ymax + 1e-9:
        yy = y0 - y * k
        o.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{W-8}" y2="{yy:.1f}" stroke="#ccc" stroke-width=".5"/><text x="{L-4}" y="{yy+3:.1f}" font-size="8.5" text-anchor="end">{y:g}</text>')
        y += ystep
    o.append(f'<line x1="{L}" y1="{y0}" x2="{W-8}" y2="{y0}" stroke="#000"/><line x1="{L}" y1="{y0}" x2="{L}" y2="{T-2}" stroke="#000"/>')
    if xl: o.append(f'<text x="{(L+W-8)/2}" y="{H-3}" font-size="9" text-anchor="middle">{xl}</text>')
    if yl: o.append(f'<text x="9" y="{(T+y0)/2}" font-size="9" text-anchor="middle" transform="rotate(-90 9 {(T+y0)/2})">{yl}</text>')
    return o, y0, k
def _svg(W, H, o, mm): return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{"".join(o)}</svg>'
def barchart(cats, v, ymax, ystep, xl, yl, draw=True, W=260, H=125, mm=68):
    """Bar chart. draw=False: grid for students; bars and category labels in red on the solutions copy."""
    L, T, B = 34, 8, 30
    o, y0, k = _grid(W, H, L, T, B, ymax, ystep, yl, xl)
    n = len(cats); slot = (W - 8 - L) / n; bw = slot * .6
    c = '#000' if draw else RED
    g = [f'<rect x="{L+i*slot+(slot-bw)/2:.1f}" y="{y0-f*k:.1f}" width="{bw:.1f}" height="{f*k:.1f}" fill="{"#d9d9d9" if draw else "none"}" stroke="{c}"/>' for i, f in enumerate(v)]
    g += [f'<text x="{L+(i+.5)*slot:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle" fill="{c}">{t}</text>' for i, t in enumerate(cats)]
    o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(g) + '</g>')
    return _svg(W, H, o, mm)
def segbar(v, names, ymax, ystep, yl, xl='', draw=True, W=210, H=140, mm=56, bars=None):
    """Segmented bar(s) + legend. bars: [(label, values)] for several bars. draw=False: grid only; segments in red on the solutions copy."""
    L, T, B = 34, 8, 24 if xl or bars else 14
    o, y0, k = _grid(W, H, L, T, B, ymax, ystep, yl, xl)
    bars = bars or [('', v)]; bw = 40 if len(bars) > 1 else 46; c = '#000' if draw else RED; g = []
    for j, (lab, vals) in enumerate(bars):
        x = L + 12 + j * (bw + 18); s = 0
        for i, f in enumerate(vals):
            g.append(f'<rect x="{x}" y="{y0-(s+f)*k:.1f}" width="{bw}" height="{f*k:.1f}" fill="{SHADE[i] if draw else "none"}" stroke="{c}"/>')
            if not draw: g.append(f'<text x="{x+bw/2}" y="{y0-(s+f/2)*k+3:.1f}" font-size="8" text-anchor="middle" fill="{RED}">{names[i]}</text>')
            s += f
        if lab: o.append(f'<text x="{x+bw/2}" y="{y0+10}" font-size="8" text-anchor="middle">{lab}</text>')
    if draw:
        lx = L + 12 + len(bars) * (bw + 18) - 4
        for j, i in enumerate(reversed(range(len(names)))):
            ly = T + 4 + j * 13
            g.append(f'<rect x="{lx}" y="{ly}" width="9" height="9" fill="{SHADE[i]}" stroke="#000"/><text x="{lx+12}" y="{ly+8}" font-size="8">{names[i]}</text>')
    o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(g) + '</g>')
    return _svg(W, H, o, mm)

# ---------------------------------------------------------------- build
def build(name, page_title, aos, P):
    """Writes lessons/<name>-worksheet(.html/.pdf) and lessons/<name>-worksheet-solutions(.html/.pdf)."""
    JS = ''.join(f'<script>{open(f"{ROOT}/lessons/{n}").read()}</script>' for n in ('a4view.js', 'paged.polyfill.min.js'))
    C = css(aos)
    def page(sol, screen=True):
        return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{page_title} guided worksheet{" · solutions" if sol else ""}</title><style>{C}</style>{JS if screen else ""}</head>'
                f'<body class="{"sol" if sol else ""}">' + pages(P) + '</body></html>')
    def pages(P):
        if PAGE not in P: return '\n'.join(P)
        out, cur = [], []
        for x in P + [PAGE]:
            if x == PAGE:
                if cur: out.append('<div class="pg">' + '\n'.join(cur) + '</div>')
                cur = []
            else: cur.append(x)
        return '\n'.join(out)
    fns = (f'{name}-worksheet', f'{name}-worksheet-solutions')
    for sol, fn in enumerate(fns):
        open(f'{ROOT}/lessons/{fn}.html', 'w').write(page(sol))
        open(f'/tmp/{fn}.html', 'w').write(page(sol, False))
    from playwright.async_api import async_playwright
    async def pdf():
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox']); pg = await b.new_page()
            for fn in fns:
                await pg.goto(f'file:///tmp/{fn}.html'); await pg.wait_for_timeout(500)
                await pg.emulate_media(media='print'); await pg.set_viewport_size({'width': int(186 * 3.78), 'height': 1100})
                over = await pg.evaluate("[...document.querySelectorAll('.pg')].map((p,i)=>p.scrollHeight>p.clientHeight+2?i+1:0).filter(x=>x)")
                if over: print('WARNING', fn, 'content cut off on page(s)', over)
                await pg.pdf(path=f'{ROOT}/lessons/{fn}.pdf', prefer_css_page_size=True, print_background=True)
            await b.close()
    asyncio.run(pdf())
    from pypdf import PdfReader
    print('built', name, [len(PdfReader(f'{ROOT}/lessons/{fn}.pdf').pages) for fn in fns], 'pages')
