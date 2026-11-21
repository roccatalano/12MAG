"""Chapter 2 coursework check: page 2 of the Chapter 2 workbook (tools/deck/chapter_workbook.py 2). Copied from ch1.py (21 Nov):
same layout, Chapter 2 lessons (gm12-u3-l03 to l08), subchapters 2A-2I, CFATs 1.2.1-1.2.3, practice rows for the sections that have
practice questions in the workbook (Insight + Cambridge skill sheets; 2A and 2E have none). Back page (test success criteria) not built.
Run: python3 tools/coursework/ch2.py  -> lessons/Ch2-coursework-check.html/.pdf"""
import json, os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
L = os.path.join(R, 'lessons')
d = json.load(open(os.path.join(R, 'planner', 'unit-plan.json')))
cards = {}
def walk(o):
    if isinstance(o, dict):
        if 'card' in o and 'id' in o: cards[o['id']] = o
        for v in o.values(): walk(v)
    elif isinstance(o, list): [walk(v) for v in o]
walk(d)
LES = ['gm12-u3-l03', 'gm12-u3-l04', 'gm12-u3-l05', 'gm12-u3-l06', 'gm12-u3-l07', 'gm12-u3-l08']
SUBS = ['2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H', '2I']
CFATS = [('CFAT 1.2.1', '2A–2B'), ('CFAT 1.2.2', '2C–2D'), ('CFAT 1.2.3', '2E–2H')]
BOOK1 = ['2B', '2C', '2D', '2F', '2G', '2H', '2I']   # practice sections in the workbook (2A, 2E have none)
BOOK2 = []     # Ch2 booklet sections

# Test Q mapping (C1 = Chapter 1 test, C2 = Chapter 2 test), by success criterion
TQ = {}

def qrange(items):
    ns = [int(x) for i in items for x in re.findall(r'\d+', i['q'])]
    return f'Q{min(ns)}–{max(ns)}' if ns and min(ns) != max(ns) else (f'Q{ns[0]}' if ns else '')

# Cambridge exercises from the lesson cards' coursework
EX = {}
for lid in LES:
    for s in cards[lid]['card']['homework']['sets']:
        m = re.match(r'Cambridge · Exercise (\d[A-I])', s['title'])
        if m: EX.setdefault(m.group(1), []).extend(s['items'])
EXC = []
for sub in SUBS:
    it = EX.get(sub, [])
    EXC.append((sub, qrange(it) if it else 'Cambridge GO only'))

css = open(os.path.join(L, 'Ch1-coursework-check.html')).read()  # same styles as Ch 1
css = css[css.index('<style>') + 7:css.index('</style>')]
css += """
body { font-size:9.8pt; }
@page { size:A4; margin:9mm 11mm 9mm 11mm; }
.cg { display:grid; border-left:1px solid #000; border-top:1px solid #000; margin-bottom:3mm; }
.cg > div { border-right:1px solid #000; border-bottom:1px solid #000; padding:1.2mm 1.6mm; display:flex; flex-direction:column; gap:1mm; min-height:11mm; }
.cg .l { font-weight:bold; font-size:9.6pt; line-height:1.15; } .cg .s { font-size:8.3pt; color:#333; line-height:1.15; }
.cg .k { margin-top:auto; display:flex; gap:2.5mm; font-size:7.6pt; color:#333; align-items:center; }
.cg .k span { display:flex; align-items:center; gap:.8mm; }
.cg .bx { width:4mm; height:4mm; }
.c6 { grid-template-columns:repeat(6,1fr); } .c9 { grid-template-columns:repeat(9,1fr); } .c11 { grid-template-columns:repeat(11,1fr); } .c11 > div { padding:1.2mm 1.1mm; } .c11 .k { gap:1.2mm; flex-direction:column; align-items:flex-start; }
.c9 > div { padding:1.2mm 1.1mm; } .c9 .k { gap:1mm; white-space:nowrap; font-size:6.5pt; } .c9 .k span { gap:.5mm; } .cg .k { flex-direction:column; align-items:flex-start; gap:1mm; } .cg > div { min-width:0; }
.sub2 { font-size:8.8pt; color:#333; margin:-1mm 0 1.5mm; }
.endrow { display:flex; gap:4mm; align-items:stretch; margin-top:1mm; }
.endrow .lines2 { flex:1; display:flex; flex-direction:column; justify-content:space-between; gap:2mm; }
.endrow .lines2 > div { display:flex; align-items:flex-end; gap:2mm; font-size:9.6pt; }
.endrow .lines2 i { flex:1; border-bottom:1px solid #000; height:6mm; } .endrow .lines2 i.d { flex:none; width:24mm; }
.catch { border:1.2px solid #000; margin:0 0 3mm; } .catch .hd { font-weight:bold; font-size:10pt; text-transform:uppercase; background:#eee; border-bottom:1.2px solid #000; padding:1mm 3mm; display:flex; justify-content:space-between; }
.catch .hd span { text-transform:none; font-weight:normal; font-size:9pt; } .catch .ln { height:7.5mm; border-bottom:1px solid #999; margin:0 3mm; } .catch .ln:last-child { border-bottom:none; }
table.ck.scx td { padding:.25mm 1.6mm; font-size:8.6pt; line-height:1.15; } table.ck td.q { width:31mm; font-size:8.4pt; } table.ck.scx .bx { width:3.6mm; height:3.6mm; } table.ck.scx td.b { width:9mm; } .scx th { padding:.6mm 1.6mm !important; }
.keyline { font-size:8.6pt; margin:0 0 1mm; } .tot { margin-top:1.5mm; } .tot span { height:7mm; }
"""

def cell(label, sub='', who=('I have it', 'Teacher ✓')):
    s = f'<div class="s">{sub}</div>' if sub else ''
    k = ''.join(f'<span><i class="bx"></i>{w}</span>' for w in who)
    return f'<div><div class="l">{label}</div>{s}<div class="k">{k}</div></div>'

def grid(cls, cells): return f'<div class="cg {cls}">' + ''.join(cells) + '</div>'

front = ('<div class="title"><div class="code">Ch<br>2</div><h1>Chapter 2 coursework check'
         '</h1>'
         '<div class="who"><div>Name <i></i></div><div>Class <i style="width:30mm"></i></div></div></div>')
ws = []
for lid in LES:
    c = cards[lid]; subs = c['subchapters']
    lab = f'{subs[0]}–{subs[-1]}' if len(subs) > 1 else subs[0]
    ws.append(cell(lab, '', ('I check', 'Teacher check')))
front += '<div class="secthd">Guided worksheets<span>One per lesson, completed and corrected</span></div>' + grid('c6', ws)
front += '<div class="secthd">Bound reference entries<span>One per subchapter, stuck in, with your own notes on the double page</span></div>'
front += grid('c9', [cell(s, '', ('I check', 'Teacher check')) for s in SUBS])
front += '<div class="secthd">CFATs<span>Completed, then corrected in a different colour</span></div>'
front += grid('c6', [cell(i, s, ('I check', 'Teacher check')) for i, s in CFATS])
front += '<div class="secthd">Cambridge exercises<span>Your own textbook: questions set on each lesson’s coursework slide</span></div>'
front += grid('c9', [cell(s, q, ('I check', 'Teacher check')) for s, q in EXC])
front += '<div class="secthd">Practice questions<span>In this workbook, after each guided worksheet: marked and corrected</span></div>'
front += grid('c9', [cell(s, '', ('I check', 'Teacher check')) for s in BOOK1] )
front += '<div class="secthd">Chapter 2 review<span>Your own textbook: the review questions at the end of Chapter 2</span></div>'
front += grid('c6', [cell('Ch 2 review', 'Multiple-choice', ('I check', 'Teacher check')), cell('Ch 2 review', 'Written-response', ('I check', 'Teacher check'))])
front += ('<div class="catch"><div class="hd">What I will do to catch up<span>by the date below</span></div>'
          '<div class="ln"></div><div class="ln"></div></div>')
front += ('<div class="endrow"><div class="lines2">'
          '<div>Student signature <i></i> Date <i class="d"></i></div>'
          '<div>Parent signature <i></i> Date <i class="d"></i></div>'
          '<div>Catch-up due <i></i> Teacher <i class="d"></i></div></div>'
          '<div class="stamp">Teacher stamp</div></div>')

back = ''; n = tested = 0

html = f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Ch2 coursework check</title><style>{css}</style></head><body>{front}{back}</body></html>'
out = os.path.join(L, 'Ch2-coursework-check.html'); open(out, 'w').write(html)
if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + out); pg.wait_for_timeout(500)
        pg.pdf(path=out[:-5] + '.pdf', prefer_css_page_size=True, print_background=True); b.close()
    print(out, n, 'criteria,', tested, 'tested')
