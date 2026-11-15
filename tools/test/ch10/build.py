"""Chapter 10 test (10A-10G, matrices) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css). Model: tools/test/ch5/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4, 'Chapter 7 - Matrices' (Mathspace's numbering; Cambridge Ch 10 + 11),
'Chapter 7 - Topic assessment.pdf' + answer key. The Ch 10 (non-transition) items only: MC Q1-8 + SA Q10-16, 19, 20 (/27). Q9, Q17, Q18 (7.10-7.12 transition) are left for the Ch 11 test.
Q16 network cropped from the PDF (q16.png). Answers = Mathspace answer key, checked by hand (2A - B, A^-1, AB, C^2, C + C^2, M^2).
Run: python3 tools/test/ch10/build.py lessons -> 'Ch10 test.html/.pdf' + 'Ch10 test solutions.html/.pdf'
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
MC = [
 (TA + ' Q1 · 7.01', 'A matrix has 3 rows and 4 columns. What is the order of this matrix?', ['3 × 3', '4 × 4', '4 × 3', '3 × 4'], 3),
 (TA + ' Q2 · 7.01', 'For the matrix ' + M([[5, -2, 7], [0, 3, -1]], 'A') + ', the element <i>a</i><sub>21</sub> is:', ['−2', '3', '0', '5'], 2),
 (TA + ' Q3 · 7.02', 'The transpose of ' + M([[1, 4], [2, 5], [3, 6]], 'B') + ' is:',
  [M([[6, 5, 4], [3, 2, 1]]), M([[1, 4], [2, 5], [3, 6]]), M([[4, 1], [5, 2], [6, 3]]), M([[1, 2, 3], [4, 5, 6]])], 3),
 (TA + ' Q4 · 7.03', 'If ' + M([[3, -1], [2, 4]], 'A') + ' and ' + M([[1, 5], [-3, 2]], 'B') + ', then <i>A</i> + <i>B</i> equals:',
  [M([[4, -6], [-1, 6]]), M([[4, 4], [-1, 6]]), M([[3, 4], [-1, 8]]), M([[2, -6], [5, 2]])], 1),
 (TA + ' Q5 · 7.03', 'If ' + M([[2, -1], [0, 3]], 'A') + ', then 3<i>A</i> equals:',
  [M([[2, -3], [0, 9]]), M([[6, -1], [0, 9]]), M([[6, -3], [0, 9]]), M([[5, 2], [3, 6]])], 2),
 (TA + ' Q6 · 7.04', 'For matrices <i>A</i> (order 2 × 3) and <i>B</i> (order 3 × 4), the product <i>AB</i> has order:', ['2 × 4', '3 × 3', '3 × 4', '2 × 3'], 0),
 (TA + ' Q7 · 7.06', 'The matrix equation <i>AX</i> = <i>B</i> can be solved by:',
  ['<i>X</i> = <i>BA</i><sup>−1</sup>', '<i>X</i> = <i>A</i><sup>−1</sup><i>B</i>', '<i>X</i> = <i>AB</i><sup>−1</sup>', '<i>X</i> = <i>B</i><sup>−1</sup><i>A</i>'], 1),
 (TA + ' Q8 · 7.09', 'Four people, <i>P</i>, <i>Q</i>, <i>R</i>, and <i>S</i>, play a round-robin tournament. The one-stage dominance matrix is '
  + M([[0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 0]], 'M') + '. The player with the most direct wins is:', ['<i>R</i>', '<i>P</i>', '<i>S</i>', '<i>Q</i>'], 0),
]
SA = [
 (TA + ' Q10 · 7.01', 'State the order of each matrix and identify the element in the given position.',
  [('a', 'State the order of ' + M([[4, -1, 0], [2, 7, 3], [-5, 1, 8]], 'C') + '.', 1, '3 × 3', 10),
   ('b', 'State the value of <i>c</i><sub>32</sub> for the matrix above.', 1, '1', 10)]),
 (TA + ' Q11 · 7.02', 'A sports club records the number of members in three age groups (Junior, Senior, Veteran) across two branches (Melbourne, Sydney) in a matrix <i>M</i>:<div style="text-align:center;margin:1mm 0">' + M([[45, 30], [80, 95], [20, 15]], 'M') + '</div>where rows represent age groups (Junior, Senior, Veteran) and columns represent branches (Melbourne, Sydney).',
  [('a', 'Write the transpose <i>M</i><sup>T</sup> and describe what the rows of <i>M</i><sup>T</sup> represent.', 1, M([[45, 80, 20], [30, 95, 15]], 'M<sup>T</sup>', col='#c00') + '  The rows of M<sup>T</sup> represent the branches (Melbourne and Sydney).', 20),
   ('b', 'The club gains 5 new Junior members and 10 new Senior members at the Melbourne branch. Write the updated matrix <i>M</i>.', 1, M([[50, 30], [90, 95], [20, 15]], 'M', col='#c00'), 20)]),
 (TA + ' Q12 · 7.03', 'Given ' + M([[3, -2], [1, 4]], 'A') + ' and ' + M([[-1, 5], [2, -3]], 'B') + ', calculate 2<i>A</i> − <i>B</i>.',
  [('', '', 2, M([[7, -9], [0, 11]], '2A − B', col='#c00'), 22)]),
 (TA + ' Q13 · 7.05', 'For the matrix ' + M([[5, 3], [4, 2]], 'A') + ', the inverse is ' + M([[-1, 1.5], [2, 'p']], 'A<sup>−1</sup>') + '. Find the value of <i>p</i>.',
  [('', '', 1, 'p = −2.5', 14)]),
 (TA + ' Q14 · 7.07', 'The column matrix ' + M([[14], [9], [21]], 'R') + ' lists the goals scored by three netball players. The permutation matrix ' + M([[0, 1, 0], [0, 0, 1], [1, 0, 0]], 'P') + ' is used to reorder the players. Find <i>PR</i>.',
  [('', '', 1, M([[9], [21], [14]], 'PR', col='#c00'), 20)]),
 (TA + ' Q15 · 7.09', 'Three players, <i>X</i>, <i>Y</i>, and <i>Z</i>, compete in a round-robin chess tournament. <i>X</i> defeats <i>Y</i>, <i>Y</i> defeats <i>Z</i>, and <i>Z</i> defeats <i>X</i>.',
  [('a', 'Construct the one-stage dominance matrix <i>M</i> for this tournament.', 1, M([[0, 1, 0], [0, 0, 1], [1, 0, 0]], 'M', col='#c00'), 22),
   ('b', 'Calculate <i>M</i><sup>2</sup> and hence determine the two-stage dominance scores for each player.', 1, M([[0, 0, 1], [1, 0, 0], [0, 1, 0]], 'M<sup>2</sup>', col='#c00') + '  Each player has a two-stage score of 1.', 22),
   ('c', 'Using <i>M</i> + <i>M</i><sup>2</sup>, determine the overall ranking of the players.', 1, M([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 'M + M<sup>2</sup>', col='#c00') + '  Each player has a row sum of 2, so all players are ranked equally.', 22)]),
 (TA + ' Q16 · 7.08', 'Four members of a Year 12 project team, Ari (<i>A</i>), Bec (<i>B</i>), Cal (<i>C</i>) and Dee (<i>D</i>), can send messages to each other only as shown in the communication network.' + IMG('q16.png', 45).replace('display:block;margin:1mm 0', 'display:block;margin:1mm auto'),
  [('a', 'Write the communication matrix <i>C</i> for this network, with rows (senders) and columns (receivers) in the order <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i>.', 1, M([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0]], 'C', col='#c00'), 26),
   ('b', 'The matrix <i>C</i><sup>2</sup>, calculated with a CAS, is shown below.<div style="text-align:center;margin:1mm 0">' + M([[0, 0, 1, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 1, 2, 0]], 'C<sup>2</sup>') + '</div>State the number of two-step communication links from Dee to Cal, and write one of them.', 1, '2, for example D → A → C (or D → B → C)', 14),
   ('c', 'Using <i>C</i> + <i>C</i><sup>2</sup>, determine which of Bec, Cal and Dee cannot send a message to Ari in two steps or fewer.', 1, 'Bec', 12),
   ('d', 'An urgent message is to be started by the person with the greatest total number of one-step and two-step communication links. Who should start the message? Give a reason.', 1, "Dee. Dee's row of C + C<sup>2</sup> sums to 5, the greatest (Ari 4, Cal 3, Bec 2).", 16)]),
 (TA + ' Q19 · 7.04', 'Calculate the matrix product <i>AB</i> where ' + M([[2, -1, 3], [0, 4, -2]], 'A') + ' and ' + M([[1, 0], [-1, 2], [3, 1]], 'B') + '.',
  [('', '', 2, M([[12, 1], [-10, 6]], 'AB', col='#c00'), 24)]),
 (TA + ' Q20 · 7.05', 'Find the determinant and inverse of ' + M([[5, 2], [3, 1]], 'A') + '.',
  [('', '', 2, 'det(A) = −1,  ' + M([[-1, 2], [3, -5]], 'A<sup>−1</sup>', col='#c00'), 26)]),
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
    out = [f'<div class="title"><div class="code">Ch 10<br>test</div><h1>Matrices<div style="font-size:10pt;font-weight:normal;margin-top:1mm">10A–10G · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch10 test' + (' solutions' if sol else '')
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
