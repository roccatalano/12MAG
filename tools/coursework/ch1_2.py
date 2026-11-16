"""Chapters 1 + 2 coursework check (card gm12-u3-ch2-test, 'Coursework check'). Double-sided A4.
Front: students tick the coursework they have (guided worksheets, bound reference entries, CFATs 1.1.1-1.2.3,
Cambridge exercises 1A-2I with the Q numbers from each lesson card's coursework, revision booklet sections); teacher signs off.
Back: success criteria from the lesson cards (gm12-u3-s1..s5, l03..l08) with a Test Q column:
C1 = lessons/Ch1 test.html (Mathspace Ch 1, renumbered Q1-19), C2 = lessons/Ch2 test.html (Mathspace Ch 2, Q1-20).
A dash = no test question checks this criterion (teacher judges it from the CFATs / coursework).
CSS copied from lessons/Ch1-coursework-check.html (14 Nov).
Run: python3 tools/coursework/ch1_2.py  -> lessons/Ch1-2 coursework check.html/.pdf
"""
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
LES = ['gm12-u3-s1', 'gm12-u3-s2', 'gm12-u3-s3', 'gm12-u3-s4', 'gm12-u3-s5',
       'gm12-u3-l03', 'gm12-u3-l04', 'gm12-u3-l05', 'gm12-u3-l06', 'gm12-u3-l07', 'gm12-u3-l08']
SUBS = ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1I', '2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H', '2I']
CFATS = [('CFAT 1.1.1', '1A–1E'), ('CFAT 1.1.2', '1F–1G'), ('CFAT 1.1.3', '1F–1I'),
         ('CFAT 1.2.1', '2A–2B'), ('CFAT 1.2.2', '2C–2D'), ('CFAT 1.2.3', '2E–2H')]
BOOK1 = ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H']           # Ch1 booklet sections (no 1I)
BOOK2 = ['2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H', '2I']     # Ch2 booklet sections

# Test Q mapping (C1 = Chapter 1 test, C2 = Chapter 2 test), by success criterion
TQ = {
 'I can identify types of data.': 'C1 Q1',
 'I can construct a bar chart from a frequency table.': 'C1 Q8, Q11',
 'I can describe the features of a distribution from a histogram.': 'C1 Q3',
 'I can construct a stem plot.': 'C2 Q11',
 'I can interpret a histogram with a log scale.': 'C1 Q4',
 'I can find the median value in a data set.': 'C1 Q19a',
 'I can find the median value from a dot plot.': 'C1 Q2',
 'I can find the median value from a stem plot.': 'C2 Q20',
 'I can find the range from a stem plot.': 'C1 Q12',
 'I can calculate the mean using the formula.': 'C1 Q5, Q15',
 'I can calculate the mean and standard deviation using the CAS calculator.': 'C2 Q17c',
 'I can read values from a boxplot.': 'C1 Q7',
 'I can use boxplots to describe a distribution with outliers.': 'C1 Q19b–c',
 'I can use boxplots to answer statistical questions.': 'C1 Q19d',
 'I can apply the 68-95-99.7% rule.': 'C1 Q10, Q14, Q17a',
 'I can calculate standardised scores.': 'C1 Q9, Q16a–b, Q18b',
 'I can use standardised scores to make comparisons.': 'C1 Q16c',
 'I can use standard scores to determine percentages.': 'C1 Q17b–c, Q18c',
 'I can convert standardised scores into actual scores.': 'C1 Q13',
 'I can solve for the values of the mean and standard deviation.': 'C1 Q18a',
 'I can identify explanatory and response variables.': 'C2 Q1, Q9, Q14a, Q16a',
 'I can percentage a two-way frequency table.': 'C2 Q10, Q16b–c, e',
 'I can describe an association from a percentaged two-way frequency table.': 'C2 Q16d',
 'I can describe an association from a percentaged segmented bar chart.': 'C2 Q2',
 'I can use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable.': 'C2 Q3, Q11, Q20',
 'I can use parallel boxplots to display and describe the association between a numerical variable and a categorical variable.': 'C2 Q4, Q15',
 'I can classify the direction, form and strength of an association from a scatterplot.': 'C2 Q5, Q12, Q14b, Q17b',
 'I can use technology to determine the value of the correlation coefficient r.': 'C2 Q17a',
 'I can classify the strength of a linear association as weak, moderate or strong based on the value of the correlation coefficient r.': 'C2 Q6, Q18a',
 'I can calculate the value of the coefficient of determination.': 'C2 Q7, Q14c, Q18b',
 'I can use the coefficient of determination to assess the strength of the association in terms of the the explained variation.': 'C2 Q14c, Q18b',
 'I understand that correlation does not imply causation.': 'C2 Q8, Q13, Q17d, Q19',
 'I can identify the explanatory and response variables.': 'C2 Q1, Q9',
}

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

css = open(os.path.join(L, 'Ch1-coursework-check.html')).read()
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
.c9 > div { padding:1.2mm 1.1mm; } .c9 .k { gap:1mm; white-space:nowrap; font-size:7.2pt; } .c9 .k span { gap:.5mm; }
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

front = ('<div class="title"><div class="code">Ch<br>1+2</div><h1>Chapters 1 + 2 coursework check'
         '<div style="font-size:10pt;font-weight:normal;margin-top:1mm">Bring every item. Tick what you have; your teacher checks and signs. Coursework counts towards your S.</div></h1>'
         '<div class="who"><div>Name <i></i></div><div>Class <i style="width:30mm"></i></div></div></div>')
ws = []
for lid in LES:
    c = cards[lid]; subs = c['subchapters']
    lab = f'{subs[0]}–{subs[-1]}' if len(subs) > 1 else subs[0]
    ws.append(cell(lab, '', ('Have', 'T ✓')))
ws.append('')
front += '<div class="secthd">Guided worksheets<span>One per lesson, completed and corrected</span></div>' + grid('c11', ws)
front += '<div class="secthd">Bound reference entries<span>One per subchapter, stuck in, with your own notes on the double page</span></div>'
front += grid('c9', [cell(s, '', ('Have', 'T ✓')) for s in SUBS])
front += '<div class="secthd">CFATs<span>Completed, then corrected in a different colour</span></div>'
front += grid('c6', [cell(i, s, ('Have', 'T ✓')) for i, s in CFATS])
front += '<div class="secthd">Cambridge exercises<span>Your own textbook: questions set on each lesson’s coursework slide</span></div>'
front += grid('c9', [cell(s, q, ('Have', 'T ✓')) for s, q in EXC])
front += '<div class="secthd">Revision booklets<span>One section per subchapter, marked and corrected</span></div>'
front += '<div class="sub2">Chapter 1 booklet (1A–1H) and Chapter 2 booklet (2A–2I)</div>'
front += grid('c9', [cell(s, '', ('Have', 'T ✓')) for s in BOOK1] + ['<div></div>'] + [cell(s, '', ('Have', 'T ✓')) for s in BOOK2])
front += ('<div class="catch"><div class="hd">What I will do to catch up<span>by the date below</span></div>'
          '<div class="ln"></div><div class="ln"></div></div>')
front += ('<div class="endrow"><div class="lines2">'
          '<div>Student signature <i></i> Date <i class="d"></i></div>'
          '<div>Parent signature <i></i> Date <i class="d"></i></div>'
          '<div>Catch-up due <i></i> Teacher <i class="d"></i></div></div>'
          '<div class="stamp">Teacher stamp</div></div>')

back = ('<div class="brk"></div><div class="secthd">Chapters 1 + 2 tests · success criteria<span>Teacher ticks when marking the tests</span></div>'
        '<p class="keyline">Test Q: <b>C1</b> = Chapter 1 test, <b>C2</b> = Chapter 2 test. ✓ = shown on the test · ✗ = not yet (revise before the SAC). '
        '— = not on the tests (check it in your CFATs and coursework).</p>'
        '<table class="ck scx"><tr><th style="width:11mm">Sub</th><th>Success criterion</th><th>Test Q</th><th class="b">✓</th><th class="b">✗</th></tr>')
n = 0; tested = 0
for lid in LES:
    for g in cards[lid]['card']['successCriteria']:
        its = g['items']
        for i, t in enumerate(its):
            n += 1; q = re.sub(r', Q', ', ', TQ.get(t, '—')); tested += q != '—'
            sc = f'<td rowspan="{len(its)}" style="font-weight:bold;text-align:center;background:#f4f4f4">{g["sub"]}</td>' if i == 0 else ''
            back += f'<tr>{sc}<td>{t}</td><td class="q">{q}</td><td class="b"><span class="bx"></span></td><td class="b"><span class="bx"></span></td></tr>'
back += ('</table><div class="tot">Chapter 1 test <span>/37</span> Chapter 2 test <span>/41</span> '
         f'Success criteria shown <span>/{tested}</span></div>')
unused = [k for k in TQ if k not in {t for lid in LES for g in cards[lid]['card']['successCriteria'] for t in g['items']}]
assert not unused, unused
html = f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Ch1-2 coursework check</title><style>{css}</style></head><body>{front}{back}</body></html>'
out = os.path.join(L, 'Ch1-2 coursework check.html'); open(out, 'w').write(html)
if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + out); pg.wait_for_timeout(500)
        pg.pdf(path=out[:-5] + '.pdf', prefer_css_page_size=True, print_background=True); b.close()
    print(out, n, 'criteria,', tested, 'tested')
