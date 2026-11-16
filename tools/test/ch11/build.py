"""Chapter 11 test (11A-11D, transition matrices) + solutions, HTML + PDF in the CFAT 1.x layout. Model: tools/test/ch10/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4 'Chapter 7 - Matrices' topic assessment Q9, Q17, Q18 (the transition items the Ch10 test left), topped up (QUEUE notes)
with Mathspace question worksheets 7.10 Q5, Q12; 7.11 Q8; 7.12 Q5, Q6 (8 Qs, /25). No Leslie (11E) item: the only Mathspace one (7.12 Q10) needs its life-cycle diagram.
Answers = Mathspace answer keys, checked with numpy (S1, S3, steady states, S_n+1 = T S_n + B).
Run: python3 tools/test/ch11/build.py lessons -> 'Ch11 test.html/.pdf' + 'Ch11 test solutions.html/.pdf'
"""
import sys, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, '../../cfat/ch2/cfat.css')).read() + """
body{font-size:9.6pt;line-height:1.25}
.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:3mm} .qgrid .box{margin-bottom:0}
.mcl div{margin:.6mm 0} .mcl b{display:inline-block;width:5mm}
.mc2{display:grid;grid-template-columns:1fr 1fr;gap:.5mm 3mm}
.ans{color:#c00;display:none;white-space:pre-wrap} .sol .ans{display:block}
.ok{color:#c00;font-weight:bold;display:none} .sol .ok{display:inline}
.part{border-top:1px dashed #000;padding:1mm 0 0;margin-top:1mm} .part .pq b{margin-right:2mm}
.sp{min-height:var(--h)} .mk{color:#555;font-size:8.5pt}
table.t{border-collapse:collapse;margin:1mm 0} table.t td,table.t th{border:1px solid #000;padding:.5mm 2mm;text-align:center}
.cite{font-size:7.5pt;color:#555;margin-top:1mm}
.stem3 td{border:none!important;padding:0 2mm!important;font-family:monospace;font-size:10pt} .stem3 td.s{border-left:1px solid #000!important;border-right:1px solid #000!important}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.9em;line-height:1.05}.fr span:first-child{border-bottom:1px solid #000;padding:0 1px}
.mc2 b{display:inline-block;width:5mm}
.blk{display:inline-block;min-width:9mm;height:4mm;text-align:center;line-height:4mm;border:1px solid #000;vertical-align:middle}
.secthd{font-weight:bold;border-bottom:2px solid #000;margin:2mm 0;display:flex;justify-content:space-between}
"""
E = html.escape
import base64
sys.path.insert(0, os.path.join(HERE, '../../deck')); from mx import mat
def IMG(f, w=150): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(HERE, f), "rb").read()).decode()}" style="width:{w}mm;display:block;margin:1mm 0">'
def T(rows, head=False):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{c}</th>' if (head and i == 0) else f'<td>{c}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
TA = 'Mathspace Ch 7 (matrices) topic assessment'
M = lambda r, n=None, **k: mat(r, name=n, **k)
TA = 'Mathspace Ch 7 (matrices) topic assessment'
W10 = 'Mathspace 7.10 Transition matrices question worksheet'
W11 = 'Mathspace 7.11 Long-term transitions question worksheet'
W12 = 'Mathspace 7.12 Transition matrices with regular change question worksheet'
M = lambda r, n=None, **k: mat(r, name=n, **k)
R = lambda r, n=None: mat(r, name=n, col='#c00')
C = lambda x: f'<div style="text-align:center;margin:1mm 0">{x}</div>'
MC = [
 (TA + ' Q9 · 7.10', 'A transition matrix must have columns that:', ['Each sum to 1.', 'Each sum to 0.', 'Contain only 0s and 1s.', 'Each sum to the number of states.'], 0),
]
SA = [
 (W10 + ' Q5 · 7.10', 'The chance of the weather being rainy (<i>R</i>) or fine (<i>F</i>) tomorrow, given it was rainy or fine today, is displayed in the table.'
  + C(T([['', 'Today(<i>R</i>)', 'Today(<i>F</i>)'], ['Tomorrow(<i>R</i>)', '0.8', '0.25'], ['Tomorrow(<i>F</i>)', '0.2', '0.75']])) + 'Construct an appropriate transition matrix for this information.',
  [('', '', 1, R([[0.8, 0.25], [0.2, 0.75]], 'T'), 20)]),
 (W10 + ' Q12 · 7.10', 'Two car rental agencies, a city agency (C) and an airport agency (A), exchange cars each week based on one-way rentals. The city agency keeps 70% of its cars, while 30% are returned to the airport agency. The airport agency keeps 90% of its cars, while 10% are returned to the city agency. Initially, both agencies have 100 cars each:',
  [('a', 'Construct the transition matrix <i>T</i> (with the city agency as the first column or row) and the initial state matrix <i>S</i><sub>0</sub>.', 1, R([[0.7, 0.1], [0.3, 0.9]], 'T') + '  ' + R([[100], [100]], 'S<sub>0</sub>'), 22),
   ('b', 'Calculate the number of cars at each agency after 10 weeks, rounded to the nearest whole number.', 1, 'City agency: 50, airport agency: 150', 18)]),
 (W11 + ' Q8 · 7.11', 'Two rival coffee shops, Shop D and Shop B, compete for customers in a small town:<ul style="margin:.5mm 0"><li>Each week, Shop D keeps 85% of its customers, while 15% switch to Shop B.</li><li>Each week, Shop B keeps 75% of its customers, while 25% switch to Shop D.</li></ul>Initially, Shop D has 400 customers and Shop B has 300 customers:',
  [('a', 'Construct the transition matrix <i>T</i> to represent this situation. Use Shop D as the first row or column.', 1, R([[0.85, 0.25], [0.15, 0.75]], 'T'), 20),
   ('b', 'Identify the initial state matrix <i>S</i><sub>0</sub>.', 1, R([[400], [300]], 'S<sub>0</sub>'), 18),
   ('c', 'Using the rule <i>S<sub>n</sub></i> = <i>T<sup>n</sup>S</i><sub>0</sub>, calculate the number of customers for each shop after 4 weeks. Round the answers to the nearest whole number.', 1, '433 customers at Shop D, 267 customers at Shop B.', 18),
   ('d', 'Calculate the steady state matrix to determine the long-term number of customers for each shop. (Note: Leave the answer as an exact decimal).', 1, '437.5 customers at Shop D, 262.5 customers at Shop B.', 18)]),
 (TA + ' Q17 · 7.11', 'A Melbourne bike-share scheme has 600 bikes, which are left at three stations: Carlton (<i>C</i>), Docklands (<i>D</i>) and Richmond (<i>R</i>). The movement of bikes from one morning to the next is modelled by the transition matrix below, with columns showing the station a bike is at one morning (from) and rows showing the station it is at the next morning (to), both in the order <i>C</i>, <i>D</i>, <i>R</i>.'
  + C(M([[0.6, 0.2, 0.1], [0.3, 0.7, 0.3], [0.1, 0.1, 0.6]], 'T')) + 'On Monday morning there are 240 bikes at Carlton, 180 at Docklands and 180 at Richmond, so ' + M([[240], [180], [180]], 'S<sub>0</sub>') + '.',
  [('a', 'What percentage of the bikes at Richmond one morning are at Docklands the next morning?', 1, '30%', 10),
   ('b', 'Calculate <i>S</i><sub>1</sub>.', 1, R([[198], [252], [150]], 'S<sub>1</sub>'), 22),
   ('c', 'Determine the number of bikes at Docklands after 3 days, rounded to the nearest whole number.', 1, '292', 16),
   ('d', 'Use technology to find the steady-state number of bikes at each station.', 1, 'Carlton 180, Docklands 300, Richmond 120', 16),
   ('e', 'Explain why this steady state does not depend on the numbers of bikes at each station on Monday morning.', 1, '<i>T</i> is a regular transition matrix (it has no zero elements), so the system approaches the same steady state from any initial state of 600 bikes.', 16),
   ('f', 'The operator plans to reduce the Docklands station to 280 docking bays. Decide whether this is enough in the long term. Give a reason.', 1, 'No. In the long term about 300 bikes are at Docklands each morning, which is more than 280 bays.', 16)]),
 (W12 + ' Q5 · 7.12', 'A city manages two public gardens, a Rose Garden (<i>R</i>) and a Botanical Garden (<i>B</i>). The city employs a team of 300 gardeners:<ul style="margin:.5mm 0"><li>Each year, 0.75 of gardeners at the Rose Garden stay, while 0.25 are reassigned to the Botanical Garden.</li><li>Each year, 0.8 of gardeners at the Botanical Garden stay, while 0.2 are reassigned to the Rose Garden.</li></ul>Initially, there are 100 gardeners at the Rose Garden and 200 at the Botanical Garden. Due to budget cuts, 10 positions are removed from the Rose Garden and 15 positions are removed from the Botanical Garden each year:',
  [('a', 'Define the transition matrix <i>T</i>. Let the first row or column represent the Rose Garden.', 1, R([[0.75, 0.2], [0.25, 0.8]], 'T'), 20),
   ('b', 'Define the initial state matrix <i>S</i><sub>0</sub>.', 1, R([[100], [200]], 'S<sub>0</sub>'), 18),
   ('c', 'Define the culling matrix <i>B</i>.', 1, R([[-10], [-15]], 'B'), 18)]),
 (W12 + ' Q6 · 7.12', 'Two political parties, the Progressives (P) and the Traditionalists (T), are tracking voter preferences. The transition matrix <i>T</i>, initial state matrix <i>S</i><sub>0</sub>, and the matrix representing new registrations and withdrawals <i>B</i> are given by:'
  + C(M([[0.7, 0.2], [0.3, 0.8]], 'T') + ',  ' + M([[2000], [3000]], 'S<sub>0</sub>') + ',  ' + M([[100], [-50]], 'B')),
  [('a', 'Calculate the number of voters for each party after one month (<i>S</i><sub>1</sub>).', 1, R([[2100], [2950]], 'S<sub>1</sub>'), 22),
   ('b', 'Calculate the number of voters for each party after two months (<i>S</i><sub>2</sub>).', 1, R([[2160], [2940]], 'S<sub>2</sub>'), 22)]),
 (TA + ' Q18 · 7.12', 'At a Bendigo sports centre, every member belongs to either the swimming club (<i>S</i>) or the cycling club (<i>C</i>). Each month, 20% of swimming members switch to cycling and 15% of cycling members switch to swimming; the rest stay in their club. In addition, 20 new members join swimming and 40 new members join cycling each month, and no members leave the centre.<br>The numbers of members after <i>n</i> months are modelled by <i>S</i><sub><i>n</i>+1</sub> = <i>TS<sub>n</sub></i> + <i>B</i>, where '
  + M([[0.80, 0.15], [0.20, 0.85]], 'T') + ' and ' + M([[400], [500]], 'S<sub>0</sub>') + ', with rows in the order <i>S</i>, <i>C</i>.',
  [('a', 'Write the matrix <i>B</i>.', 1, R([[20], [40]], 'B'), 18),
   ('b', 'Calculate <i>S</i><sub>1</sub>.', 1, R([[415], [545]], 'S<sub>1</sub>'), 20),
   ('c', 'Calculate <i>S</i><sub>2</sub>, rounding each element to the nearest whole number.', 1, R([[434], [586]], 'S<sub>2</sub>'), 20),
   ('d', 'Let <i>M<sub>n</sub></i> be the total number of members after <i>n</i> months. Write a recurrence relation for <i>M<sub>n</sub></i>, and state the type of growth it models.', 1, '<i>M</i><sub>0</sub> = 900, <i>M</i><sub><i>n</i>+1</sub> = <i>M<sub>n</sub></i> + 60; linear growth', 14),
   ('e', 'Find the total number of members after 12 months.', 1, '1620', 12),
   ('f', 'The centre claims that the cycling club will have more than 650 members after 4 months. Decide whether the claim is correct. Give a reason.', 1, 'The claim is correct. <i>S</i><sub>4</sub> gives about 662 cycling members, which is more than 650.', 16)]),
]
def mk(n): return f'{n} mark{"s" if n > 1 else ""}'
def mcbox(n, q):
    les, stem, opts, a = q
    o = ''.join(f'<div><b>{"ABCD"[i]}</b>{x} {"<span class=ok>✓</span>" if i == a else ""}</div>' for i, x in enumerate(opts))
    cls = 'mc2' if max(map(len, opts)) < 25 or all('<table' in x for x in opts) else 'mcl'
    return f'<div class="box"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><div class="q">{stem}</div><div class="{cls}">{o}</div><div class="cite">{les}</div></div></div>'
def sabox(n, q):
    les, stem, parts = q
    tot = sum(p[2] for p in parts)
    ps = ''
    for lab, txt, m, ans, h in parts:
        head = f'<div class="pq"><b>{lab}</b>{txt} <span class="mk">({mk(m)})</span></div>' if lab else ''
        ps += f'<div class="part">{head}<div class="sp" style="--h:{h}mm"><div class="ans">{ans}</div></div></div>'
    return f'<div class="box"><div class="hd">Question {n}<span>{mk(tot)}</span></div><div class="bd"><div class="q">{stem}</div>{ps}<div class="cite">{les}</div></div></div>'

def page(sol):
    tot = len(MC) + sum(p[2] for q in SA for p in q[2])
    out = [f'<div class="title"><div class="code">Ch 11<br>test</div><h1>Transition matrices<div style="font-size:10pt;font-weight:normal;margin-top:1mm">11A–11D · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch11 test' + (' solutions' if sol else '')
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{t}</title><style>{CSS}</style>'
            f'<script src="a4view.js"></script><script src="paged.polyfill.min.js"></script></head><body class="{"sol" if sol else ""}">\n' + '\n'.join(out) + '\n</body></html>'), t

if __name__ == '__main__':
    od = sys.argv[1]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for sol in (False, True):
            h, t = page(sol); f = os.path.join(od, t + '.html'); open(f, 'w').write(h)
            pg = b.new_page(); pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(2500)
            pg.pdf(path=os.path.join(od, t + '.pdf'), prefer_css_page_size=True, print_background=True); pg.close(); print(t)
        b.close()
