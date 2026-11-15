"""Lesson gm12-u4-13a13b (13A graphs and networks, 13B adjacency matrices) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/13A-13B slides.html      Run: python3 tools/deck/gm12-u4-13a13b/build.py      Screenshots: python3 tools/deck/gm12-u4-13a13b/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; graphs redrawn with tools/deck/tpl/net.py, same vertices and edges):
- Do Now: VCAA 2024 Exam 1 Q30 (B, 78%) · VCAA 2026 Exam 1 Q6 (2026 report not yet released; answer C worked) ·
          VCAA 2025 Exam 2 Q12 stem + Q12a (average 0.6/1) · VCAA 2024 Exam 2 Q7 stem + Q7c (3.6%, average 0.6/1).
- APK: Cambridge U1&2 Ch 8 skills checklist #2 (graph from #1) and #8 (graph from #6), pp. 540-541; answers from the
       Skills Checklist answers (p. 833) · VCAA 2017 Exam 1 Networks and decision mathematics Q2 (= Edrolo U1&2 7A Q13; C, 83%).
- Learn: Cambridge U3&4 13A pp. 609-615, 13B pp. 619-620 (own words) · Edrolo U3&4 8A pp. 518-525, 8B pp. 532-535.
- Worked examples: Cambridge U3&4 Examples 1-6 (pp. 612-620).
  You trys: Edrolo U3&4 8A Worked example 1 (pp. 520-521), WE2a (pp. 523-524), WE3a, WE3b (pp. 524-525); 8B WE2 (pp. 534-535), WE1 (pp. 532-533).
- No CAS (Cambridge prints none for 13A/13B).
- Exits: VCAA 2021 Exam 2 N&DM Q1 stem, Q1a, Q1b (= Edrolo U3&4 8A Q18; average 1.9/2) · VCAA 2021 Exam 1 N&DM Q3 (= Edrolo 8A Q20; C, 34%) ·
         VCAA 2019 Exam 1 N&DM Q6 (= Edrolo 8B Q15; A, 39%). Floor plan and road map cropped from the papers (fig/).
- % correct: VCAA examiner reports (via tools/y12_edrolo_exam_practice.csv and tools/vcaa_current_index.csv).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
CAM = 'Cambridge General Mathematics Units 3&amp;4'; EDR = 'Edrolo General Mathematics Units 3&amp;4'; CAM12 = 'Cambridge General Mathematics Units 1&amp;2'
def _card(o, i):
    if isinstance(o, dict):
        if o.get('id') == i: return o['card']
        for v in o.values():
            r = _card(v, i)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = _card(v, i)
            if r: return r
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-13a13b')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
L5 = list('ABCDE')
def mtx(rows, labels=None, fs=15, cols=None):  # small plain matrix for MC options
    return amat(labels or [''] * len(rows), rows, fs=fs, cols=cols or [''] * len(rows[0]))
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def cells(r0, r1, c0, c1): return ','.join(f'c{r}_{k}' for r in range(r0, r1) for k in range(c0, c1))
def row(r, n=5): return ','.join(f'c{r}_{k}' for k in range(n))
def vals(r, n=5): return ','.join(f'v{r}_{k}' for k in range(n))

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.mcm .mc{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px}'
     '.mcm .mc>div{align-items:center}.mcm .amat{margin:0}.tiles4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:6px}'
     '.tiles4>div{background:#fff;border:3px solid var(--learn);border-radius:14px;padding:8px 10px;font-size:17px;text-align:center}.tiles4 b{display:block;font-size:19px;margin-bottom:2px}'
     '.mini{width:100%;max-width:190px;margin:0 auto}.mc3 .mc{grid-template-columns:1fr 1fr 1fr!important}</style>']
# ================= opening
S.append(title('13A–13B', 'Graphs, networks and adjacency matrices', f'{CAM} · 13A Graphs and networks · 13B Adjacency matrices', 'gm12-u4-13a13b'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 13A–13B', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>13A–13B')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· three Year 11 questions', 'var(--apk)'),
  ('Graphs: vertices, edges, loops, degree', '', None), ('Worked example 1', '→ You try', None), ('Describing graphs · planar graphs', '', None),
  ('Worked example 2', '→ You try', None), ('Euler’s formula', '', None), ('Worked examples 3–4', '→ You try', None),
  ('Adjacency matrices', '', None), ('Worked examples 5–6', '→ You try', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'), ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Graph', 'vertices (dots) joined by edges (lines)', Wd(110, net({'A': (15, 15, 'w'), 'B': (85, 15, 'e'), 'C': (50, 65, 's')}, [('A', 'B'), ('B', 'C'), ('A', 'C')], W=100, H=80, fs=14, pad=4))),
  ('Loop', 'an edge from a vertex back to itself', Wd(90, net({'A': (20, 40, 'w')}, [('A', 'A', {'loop': 0, 'size': 15})], W=80, H=60, fs=14, pad=4))),
  ('Degree', 'deg(A) = number of edges at A; a loop adds 2'),
  ('Planar graph', 'can be drawn with no edges crossing; the regions (faces) include the outside'),
  ('Isomorphic', 'same vertices and same connections, drawn differently'),
  ('Adjacency matrix', 'row <i>i</i>, column <i>j</i> = number of edges joining <i>i</i> and <i>j</i>; a loop counts as 1')],
  [('Sum of degrees', F('sum of degrees = 2 × number of edges'), 'each edge has two ends'),
   ('Euler’s formula', F('<i>v</i> + <i>f</i> = <i>e</i> + 2'), 'connected planar graphs (Edrolo writes v − e + f = 2)')],
  f'{CAM}, 13A pp. 609–615, 13B pp. 619–620; Study Design: conventions, terminology, properties and types of graphs; use of matrices to represent graphs'))

# ================= Do Now 1: VCAA 2024 E1 Q30 (11E)
LT = ('<table class="t tight" id="d1" style="font-size:16px;margin:6px auto"><tr><th></th><th colspan="3">Age group (years)</th></tr><tr><th></th><th>0–2</th><th>2–4</th><th>4–6</th></tr>'
      '<tr><th>Initial population</th><td data-i="c0_0">2100</td><td data-i="c0_1">6400</td><td data-i="c0_2">4260</td></tr>'
      '<tr><th>Birth rate</th><td data-i="c1_0">0</td><td data-i="c1_1">1.8</td><td data-i="c1_2">1.2</td></tr>'
      '<tr><th>Survival rate</th><td data-i="c2_0">0.7</td><td data-i="c2_1">0.6</td><td data-i="c2_2">0</td></tr></table>')
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2024 Exam 1 Q30', 'Review of 11E (Leslie matrices)',
  '<div style="font-size:18px">Data has been collected on the female population of a species of mammal located on a remote island.<br>'
  'The female population has been divided into three age groups, with the initial population (at the time of data collection), the birth rate, and the survival rate of each age group shown in the table below.'
  + LT + 'The Leslie matrix (<i>L</i>) that may be used to model this particular population is</div>',
  [('Row 1', 'birth rates across the top: 0 1.8 1.2', 'data-hi="#d1|c1_0,c1_1,c1_2|hy"'),
   ('Sub-diagonal', 'survival rates 0.7, 0.6 under the leading diagonal; everything else 0', 'data-hi="#d1|c2_0,c2_1|hb"'),
   ('Not used', 'the initial population goes in the state matrix, not in <i>L</i>')],
  'Birth rates in row 1, survival rates on the sub-diagonal: <b>B</b>.', 'VCAA 2024 General Mathematics Exam 1 Q30 (examiner report: 78% correct)',
  mc=['<i>L</i> = ' + mtx(o) for o in DN1_OPTS], key='B', stat=('mc', 78), dist=[5, 78, 7, 10]))
sm(extra='sm mcm')
# ================= Do Now 2: VCAA 2026 E1 Q6 (1H)
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2026 Exam 1 Q6', 'Review of 1H (the normal distribution)',
  '<div style="font-size:22px;margin-top:10px">The heights, in centimetres (cm), of adult males are modelled by a normal distribution.<br>For these height values, it is known that:'
  '<ul style="margin:6px 0 6px 26px"><li>0.15% of these values are expected to be less than 160.8 cm</li><li>the standard deviation is 5.6 cm.</li></ul>'
  'Consider a sample of 4000 adult males.<br>Using the 68–95–99.7% rule, it is expected that 100 of these males will have a height, in centimetres, greater than</div>',
  [('0.15% below', '160.8 is 3 standard deviations below the mean'),
   fx('Mean', 'mean', F('160.8 + 3 × ', V('s', '5.6')), '177.6'),
   ('100 of 4000', '100 ÷ 4000 = 2.5% → 2 standard deviations above the mean'),
   fx('Height', 'height', F(V('mean', '177.6'), ' + 2 × ', V('s', '5.6')), '188.8')],
  '188.8 cm: <b>C</b>.', 'VCAA 2026 General Mathematics Exam 1 Q6 (2026 report not yet released)',
  mc=['172.0', '183.2', '188.8', '194.4'], key='C', stat=('new',)))
# ================= Do Now 3: VCAA 2025 E2 Q12a (11D)
M12 = amat(['N', 'T', 'P', 'L'], [['0.25', '0', '0', '0'], ['0.625', '0.25', '0', '0'], ['0', '0.625', '0.1', '0'], ['0.125', '0.125', '0.9', '1']], fs=15, tid='d3m')
S12 = amat(['N', 'T', 'P', 'L'], [['4'], ['15'], ['15'], ['27']], fs=15, cols=[''])
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2025 Exam 2 Q12a', 'Review of 11D (transition matrices)',
  '<div style="font-size:16px">The early learning centre contains three rooms, Nursery (<i>N</i>), Toddler (<i>T</i>) and Pre-kinder (<i>P</i>).<br>'
  'From one year to the next, children can move between rooms, stay in the same room, or may leave (<i>L</i>) the centre. The following transition matrix, <i>M</i>, shows the expected proportion of children who will move between categories or stay in the same category from one year to the next.'
  '<div style="display:flex;align-items:center;justify-content:center;gap:8px"><i>M</i> = ' + M12 + '<span class="muted">(columns: this year · rows: next year)</span></div>'
  'a. The number of children expected to be in each of the four categories, from one year to the next, can be calculated using the matrix recurrence relation <i>S</i><sub><i>n</i>+1</sub> = <i>MS</i><sub><i>n</i></sub><br>'
  'where <i>S<sub>n</sub></i> represents the expected number of children in each of the four categories at the start of year <i>n</i>.<br>The state matrix <i>S</i><sub>2024</sub>, shown below, gives the number of children in each category at the start of 2024.'
  '<div style="display:flex;align-items:center;justify-content:center;gap:8px"><i>S</i><sub>2024</sub> = ' + S12 + '</div><b>Find</b> <i>S</i><sub>2023</sub>. <span class="muted">(1 mark)</span></div>',
  [('Backwards', '<i>S</i><sub>2024</sub> = <i>M</i> <i>S</i><sub>2023</sub> → <i>S</i><sub>2023</sub> = <i>M</i><sup>−1</sup> <i>S</i><sub>2024</sub>'),
   ('CAS', 'enter <i>M</i> and <i>S</i><sub>2024</sub>, then <i>M</i><sup>−1</sup> × <i>S</i><sub>2024</sub>'),
   ('Check', 'N: 0.25 × 16 = 4 ✓')],
  '<i>S</i><sub>2023</sub> = <b>[16, 20, 25, 0]</b><sup>T</sup> (N = 16, T = 20, P = 25, L = 0)', 'VCAA 2025 General Mathematics Exam 2 Q12 stem and Q12a (examiner report: average 0.6/1)',
  stat=('avg', 60), cmd=('Find', 1, 'go back a year: M⁻¹ × S')))
sm(extra='sm xs')
# ================= Do Now 4: VCAA 2024 E2 Q7c (8F)
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2024 Exam 2 Q7c', 'Review of 8F (annuities)',
  '<div style="font-size:24px;margin-top:20px">Emi decides to invest a $300 000 inheritance into an annuity.<br>Let <i>E<sub>n</sub></i> be the balance of Emi’s annuity after <i>n</i> months.<br>'
  'A recurrence relation that can model the value of this balance from month to month is<div style="text-align:center;margin:12px 0"><i>E</i><sub>0</sub> = 300 000, &nbsp;&nbsp; <i>E</i><sub><i>n</i>+1</sub> = 1.003<i>E<sub>n</sub></i> − 2159.41</div>'
  'c. <b>Calculate</b> the annual compound interest rate for this annuity. <span class="muted">(1 mark)</span></div>',
  [('Monthly rate', '1.003 = 1 + <i>r</i> ÷ 100 → <i>r</i> = 0.3% per month'),
   fx('Annual', 'annual rate', F(V('monthly', '0.3%'), ' × 12'), '3.6%')],
  'The annual interest rate is <b>3.6%</b>.', 'VCAA 2024 General Mathematics Exam 2 Q7 stem and Q7c (examiner report: average 0.6/1)',
  stat=('avg', 60), cmd=('Calculate', 1, 'monthly rate × 12')))

# ================= APK 1: checklist #2
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #2', 'Degree of a vertex',
  ('<div style="font-size:24px">Determine the degree of each vertex in the graph above and the sum of degrees of the graph.</div>',
   Wd(420, net(K1_V, K1_E, sid='k1', W=290, H=200, pad=14)), ''),
  [('deg(A)', 'A–B, A–E → <b>2</b>', 'data-hi="#k1|ab,ae|hy"'), ('deg(B)', 'B–A, B–E, B–D → <b>3</b>', 'data-hi="#k1|ab,be,bd|hy"'),
   ('deg(C)', 'C–D + loop (2) → <b>3</b>', 'data-hi="#k1|dc,cl|hy"'), ('deg(D)', 'D–B, D–E, D–C → <b>3</b>', 'data-hi="#k1|bd,ed,dc|hy"'),
   ('deg(E)', 'E–A, E–B, E–D + loop (2) → <b>5</b>', 'data-hi="#k1|ae,be,ed,el|hy"'),
   fx('Sum', 'sum', F('2 + 3 + 3 + 3 + 5'), '16', 'data-hi="#k1||"')],
  'deg(A) = 2, deg(B) = 3, deg(C) = 3, deg(D) = 3, deg(E) = 5; sum of degrees = <b>16</b> (= 2 × 8 edges).',
  f'{CAM12} · Ch 8 skills checklist #2 (graph from #1), p. 540 · answer from the Skills Checklist answers', cmd=('Determine', None, 'count edge ends; a loop adds 2')))
# ================= APK 2: checklist #8
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #8', 'Verifying Euler’s formula',
  ('<div style="font-size:24px">Verify Euler’s formula for the graph above.</div>', Wd(430, net(K2_V, K2_E, sid='k2', W=330, H=240, pad=12)), ''),
  [('Count', '<i>v</i> = 3 · <i>e</i> = 5 · <i>f</i> = 4 (the crossing can be removed: the graph is planar)'),
   fx('Euler', '<i>v</i> + <i>f</i>', F(V('v', '3'), ' + ', V('f', '4')), '7'), fx('Check', '<i>e</i> + 2', F(V('e', '5'), ' + 2'), '7')],
  '<i>v</i> + <i>f</i> = <i>e</i> + 2: 3 + 4 = 5 + 2, 7 = 7 ✓ <b>Euler’s formula is verified.</b>',
  f'{CAM12} · Ch 8 skills checklist #8 (graph from #6), p. 541 · answer from the Skills Checklist answers', cmd=('Verify', None, 'count v, e, f; both sides equal')))
# ================= APK 3: VCAA 2017 E1 N&DM Q2
S.append(qslide('apk', 'APK · VCAA 2017 Exam 1 Q2', 'Sum of degrees',
  ('<div style="font-size:22px">Two graphs, labelled Graph 1 and Graph 2, are shown below.</div>', apk3(),
   '<div style="font-size:22px">The sum of the degrees of the vertices of Graph 1 is</div>'),
  [('Graph 1', '6 edges → sum of degrees = 2 × 6 = 12'), ('Graph 2', '6 edges → sum of degrees = 2 × 6 = 12')],
  'equal to the sum of the degrees of the vertices of Graph 2: <b>C</b>.', f'VCAA 2017 Further Mathematics Exam 1 Networks and decision mathematics Q2 (examiner report: 83%) · Edrolo General Mathematics Units 1&amp;2 7A Q13',
  mc=['two less than the sum of the degrees of the vertices of Graph 2.', 'one less than the sum of the degrees of the vertices of Graph 2.', 'equal to the sum of the degrees of the vertices of Graph 2.',
      'one more than the sum of the degrees of the vertices of Graph 2.', 'two more than the sum of the degrees of the vertices of Graph 2.'], key='C', stat=('mc', 83), dist=[9, 1, 83, 4, 3]))
sm()

# ================= Learn 1: graphs, degree, loops
S.append(learn('Learn · 13A', 'Graphs: vertices, edges and degree',
  '<h4>A graph shows connections</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>vertex</b> = a dot (a person, town, room …)</li><li><b>edge</b> = a line joining two vertices</li>'
  '<li><b>degree</b> deg(A) = number of edges at A</li><li><b>loop</b> = an edge from a vertex to itself: adds <b>2</b> to the degree</li></ul>',
  Wd(430, soc('lsoc')) +
  '<div class="frag" style="font-size:17px;text-align:center;line-height:1.25" data-hi="#lsoc|ab,ae,af|hy">Anna is a friend of Brett, Ethan and Frances: deg(<i>A</i>) = 3 (odd)</div>'
  '<div class="frag" style="font-size:17px;text-align:center;line-height:1.25" data-hi="#lsoc|cd,fd|hb">Dario: deg(<i>D</i>) = 2 (even)</div>'
  '<div class="frag" style="font-size:17px;text-align:center;line-height:1.25" data-show="#lsoc|el" data-hi="#lsoc|ae,ce,el|hc">Ethan adds himself: a loop. deg(<i>E</i>) = 2 + 2 = 4</div>',
  'Count edge ENDS at the vertex: a loop has two ends there. Sum of degrees = 2 × number of edges.', f'{CAM}, 13A pp. 609–610 (own words; Cambridge’s social media graph) · {EDR}, 8A pp. 518–519',
  cards=(kcard('Sum of degrees', F('2 × number of edges')),)))

# ================= Ex 1 / YT WE1
S.append(qslide('we', 'Worked example 1 · 13A', 'Graphs',
  '<div style="font-size:19px">A connected graph is shown on the right.' + Wd(420, ex1('e1')) + '</div>'
  + plist([('a', 'What is the degree of vertex <i>C</i>?'), ('b', 'Which vertices have a loop?'), ('c', 'What is the degree of vertex <i>F</i>?'),
           ('d', 'A bridge exists between two vertices. Which vertices are they?'), ('e', 'Draw a subgraph of this graph that involves only vertices <i>A</i>, <i>B</i> and <i>C</i>.')]),
  [('a', 'edges at C: C–A, C–D, C–E, C–F', 'data-hi="#e1|ac,cd,ce,cf|hy"'), ('b', 'an edge from a vertex back to itself', 'data-hi="#e1|bl,fl|hc"'),
   ('c', 'F–C, F–D, F–E + loop (2)', 'data-hi="#e1|cf,df,ef,fl|hy"'), ('d', 'remove A–C: the graph splits in two', 'data-hi="#e1|ac|hc"'),
   ('e', 'keep only edges that join A, B and C (there are other answers)', 'data-hi="#e1||"')],
  '', f'{CAM} · Example 1 (p. 612)', video='Cambridge GO · Example 1 (13A Resources)',
  parts=[('a', 'deg(<i>C</i>) = <b>4</b>'), ('b', 'Vertex <b><i>B</i></b> and vertex <b><i>F</i></b> have loops.'), ('c', 'deg(<i>F</i>) = <b>5</b>'),
         ('d', 'A bridge exists between vertex <b><i>A</i></b> and vertex <b><i>C</i></b>.'), ('e', '<div style="width:170px">' + ex1sub() + '</div>')]))
sm(extra='sm mp')
S.append(qslide('yt', 'You try · Edrolo 8A WE1', 'Graphs',
  '<div style="font-size:19px">Consider the graph.' + Wd(400, y1('y1', faces=True)) + '</div>'
  + plist([('a', 'How many edges are in this graph?'), ('b', 'How many faces are in this graph?'), ('c', 'How many vertices are in this graph?'),
           ('d', 'Which vertex has a loop?'), ('e', '<b>Determine</b> the degree of vertex C.'), ('f', 'Between which vertices can a bridge be found?')]),
  [('a', 'count every line, including the loop', 'data-hi="#y1|ab,ac,bc,cl,cd,de,df,ef|hy"'), ('b', 'no edges cross: count regions + the outside', 'data-show="#y1|f1,f2,f3,f4" data-hi="#y1||"'),
   ('c', 'count the dots'), ('d', 'edge back to itself', 'data-hi="#y1|cl|hc"'), ('e', 'C–A, C–B, C–D + loop (2)', 'data-hi="#y1|ac,bc,cd,cl|hy"'),
   ('f', 'remove C–D: A, B, C can’t reach D, E, F', 'data-hi="#y1|cd|hc"')],
  '', f'{EDR} · 8A Worked example 1 (pp. 520–521)', cmd=('Determine', None, 'a loop adds 2'),
  parts=[('a', '<b>8</b> edges'), ('b', '<b>4</b> faces'), ('c', '<b>6</b> vertices'), ('d', '<b>C</b>'), ('e', 'deg(C) = <b>5</b>'), ('f', '<b>C and D</b>')]))
sm(extra='sm xs')

# ================= Learn 2: describing graphs
def mini(V, E, extra=''): return '<div style="width:150px;margin:2px auto">' + net(V, E, W=150, H=95, fs=13, r=4, pad=6, lw=2.2) + '</div>' + extra
T4 = ('<div class="tiles4">'
  + '<div class="frag"><b>Simple</b>no loops, no multiple edges' + mini({'A': (15, 50, 'w'), 'B': (75, 15, 'n'), 'C': (135, 50, 'e'), 'D': (75, 85, 's')}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D'), ('B', 'D')]) + '</div>'
  + '<div class="frag"><b>Isolated vertex</b>joined to nothing (E)' + mini({'A': (15, 50, 'w'), 'B': (65, 15, 'n'), 'C': (110, 50, 'n'), 'E': (125, 85, 'e')}, [('A', 'B'), ('B', 'C'), ('A', 'C', {'bend': -10})]) + '</div>'
  + '<div class="frag"><b>Degenerate</b>all vertices isolated (no edges)' + mini({'A': (20, 40, 'n'), 'B': (75, 20, 'n'), 'C': (60, 80, 's'), 'D': (125, 60, 'n')}, []) + '</div>'
  + '<div class="frag"><b>Complete</b>every pair joined by an edge' + mini({'A': (20, 85, 'w'), 'B': (40, 15, 'n'), 'C': (130, 15, 'n'), 'D': (110, 85, 'e')}, [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]) + '</div>'
  + '<div class="frag"><b>Connected · bridge</b>remove the bridge (D–E) → two pieces' + mini({'A': (10, 50, 'w'), 'B': (35, 15, 'n'), 'C': (35, 85, 's'), 'D': (65, 50, 's'), 'E': (100, 30, 'n'), 'F': (125, 80, 's'), 'G': (145, 30, 'n')},
        [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E', {'col': '#d2475b'}), ('E', 'F'), ('F', 'G'), ('E', 'G')]) + '</div>'
  + '<div class="frag"><b>Subgraph</b>part of a graph: every edge and vertex is in the original' + mini({'A': (15, 55, 'w'), 'B': (70, 15, 'n'), 'F': (100, 85, 's')}, [('A', 'B', {'bend': -8}), ('B', 'F', {'bend': -8})]) + '</div>'
  + '<div class="frag"><b>Multiple edges</b>two or more edges join the same pair' + mini({'A': (20, 50, 'w'), 'B': (130, 50, 'e')}, [('A', 'B', {'bend': 14}), ('A', 'B', {'bend': -14})]) + '</div>'
  + '<div class="frag"><b>Isomorphic</b>same connections, drawn differently<div style="display:flex">'
  + mini({'A': (30, 20, 'n'), 'B': (120, 20, 'n'), 'C': (120, 80, 's'), 'D': (30, 80, 's')}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
  + mini({'A': (20, 50, 'w'), 'C': (130, 50, 'e'), 'B': (75, 12, 'n'), 'D': (75, 88, 's')}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]) + '</div></div>'
  + '</div>')
S.append(learn('Learn · 13A', 'Describing graphs',
  '<h4>Words that describe a graph</h4><p style="font-size:19px;margin:4px 0">Exam questions use these words exactly: learn each one with its picture.</p>', T4,
  'Connected ≠ complete: connected = you can get from any vertex to any other; complete = every pair is joined DIRECTLY.',
  f'{CAM}, 13A pp. 610–612 (own words; pictures redrawn) · {EDR}, 8A pp. 521–523'))
# ================= Learn 3: planar graphs
S.append(learn('Learn · 13A', 'Planar graphs and faces',
  '<h4>Can it be drawn with no edges crossing?</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>edges that cross are NOT joined (no vertex at the crossing)</li><li><b>planar</b>: it can be redrawn with no crossings (same connections)</li>'
  '<li><b>faces</b>: the regions a planar graph makes, <b>including the outside</b></li></ul>',
  Wd(560, ex2('lp')) + '<span class="frag" data-hi="#lp|ce|hc"></span><span class="frag" data-show="#lp|ce2" data-hi="#lp|ce|hx"></span>'
  '<div class="frag" style="font-size:21px;text-align:center">Move C–E round the outside: no crossings → the graph is planar.</div>',
  'Count faces only on a planar drawing; the outside region is always a face.', f'{CAM}, 13A pp. 613–614 (own words) · {EDR}, 8A pp. 522–523',
  cards=(kcard('Isomorphic', 'same connections, different drawing'),)))
# ================= Ex 2 / YT WE2a
S.append(qslide('we', 'Worked example 2 · 13A', 'Redrawing a graph in planar form',
  ('<div style="font-size:24px">Show that this graph is planar by redrawing it so that no edges cross.</div>', Wd(500, ex2('e2')), ''),
  [('Choose', 'an edge that crosses another: C–E crosses A–D', 'data-hi="#e2|ce|hc"'), ('Remove', 'take C–E out for now', 'data-hi="#e2|ce|hc"'),
   ('Redraw', 'join C to E round the outside, crossing nothing', 'data-show="#e2|ce2" data-hi="#e2|ce|hx"')],
  'No edges cross, so the graph is <b>planar</b> (green edge = C–E redrawn).', f'{CAM} · Example 2 (p. 613)', video='Cambridge GO · Example 2 (13A Resources)',
  cmd=('Show', None, 'redraw so no edges cross')))
S.append(qslide('yt', 'You try · Edrolo 8A WE2a', 'Redrawing a graph in planar form',
  ('<div style="font-size:24px">Consider the following graph.</div>', Wd(520, y2('y2')), '<div style="font-size:24px">a. Redraw the graph in planar form.</div>'),
  [('Find crossings', 'A–C crosses B–E · A–D crosses B–E and C–E', 'data-hi="#y2|ac,ad,be,ce|hy"'), ('Redraw A–D', 'round the outside (under E)', 'data-hi="#y2|ad|hc"'),
   ('Redraw A–C', 'round the outside (over B)', 'data-hi="#y2|ac,ad|hx"')],
  'One planar form (others are possible):', f'{EDR} · 8A Worked example 2a (pp. 523–524)', cmd=('Redraw', None, 'move crossing edges to the outside'),
  afig=Wd(420, y2('y2a', planar=True))))
# ================= Learn 4: Euler's formula
S.append(learn('Learn · 13A', 'Euler’s formula',
  '<h4>For any connected planar graph</h4><p style="font-size:24px;text-align:center;margin:6px 0"><b><i>v</i> + <i>f</i> = <i>e</i> + 2</b></p>'
  '<ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li><i>v</i> vertices · <i>e</i> edges · <i>f</i> faces (include the outside)</li>'
  '<li><b>verify</b>: count v, e, f; show both sides are equal</li><li><b>use</b>: substitute two values, solve for the third</li></ul>',
  Wd(420, ex4('le')) + '<div class="frag" style="font-size:22px;text-align:center">6 vertices, 9 edges, 5 faces: 6 + 5 = 9 + 2 = 11 ✓</div>',
  'Euler’s formula only works on a planar drawing: redraw first, then count faces.', f'{CAM}, 13A p. 614 (own words; graph from Example 4) · {EDR}, 8A p. 524 (writes it as v − e + f = 2)',
  cards=(kcard('Euler’s formula', F('<i>v</i> + <i>f</i> = <i>e</i> + 2')),)))
# ================= Ex 3 / YT WE3a
S.append(qslide('we', 'Worked example 3 · 13A', 'Verifying Euler’s formula',
  ('<div style="font-size:24px">For the graph shown on the right:</div>', Wd(440, ex3('e3', faces=True)),
   plist([('a', 'redraw the graph into planar form'), ('b', 'verify Euler’s formula for this graph.')])),
  [('a', 'remove A–C (it crosses B–D) and redraw it round the outside', 'data-hi="#e3|ac|hx" data-show="#e3|ac2"'),
   ('b · count', '<i>v</i> = 5 · <i>e</i> = 7 · <i>f</i> = 4', 'data-show="#e3|f1,f2,f3,f4"'),
   fx('b · Euler', '<i>v</i> + <i>f</i>', F(V('v', '5'), ' + ', V('f', '4')), '9'), fx('b · check', '<i>e</i> + 2', F(V('e', '7'), ' + 2'), '9')],
  '', f'{CAM} · Example 3 (pp. 614–615)', video='Cambridge GO · Example 3 (13A Resources)', cmd=('verify', None, 'count v, e, f; both sides equal'),
  parts=[('a', 'A–C redrawn round the outside (green): no edges cross.'), ('b', '5 + 4 = 7 + 2, 9 = 9: <b>Euler’s formula is verified.</b>')]))
S.append(qslide('yt', 'You try · Edrolo 8A WE3a', 'Verifying Euler’s formula',
  ('<div style="font-size:24px">Use Euler’s rule to solve the following questions.<br>a. <b>Show</b> that the graph is a connected planar graph.</div>', Wd(330, y3('y3', faces=True)), ''),
  [('Count', '<i>v</i> = 4 · <i>e</i> = 5 · <i>f</i> = 3', 'data-show="#y3|f1,f2,f3"'),
   fx('Euler', '<i>v</i> − <i>e</i> + <i>f</i>', F(V('v', '4'), ' − ', V('e', '5'), ' + ', V('f', '3')), '2')],
  '<i>v</i> − <i>e</i> + <i>f</i> = 4 − 5 + 3 = 2, so Euler’s rule holds: the graph is a <b>connected planar graph</b>.', f'{EDR} · 8A Worked example 3a (pp. 524–525)',
  cmd=('Show', None, 'count, substitute, = 2')))
# ================= Ex 4 / YT WE3b
S.append(qslide('we', 'Worked example 4 · 13A', 'Using Euler’s formula',
  '<div style="font-size:26px;margin-top:30px">A connected planar graph has six vertices and nine edges. How many faces does the graph have? Draw a connected planar graph with six vertices and nine edges.</div>',
  [('Known', '<i>v</i> = 6 · <i>e</i> = 9'), fx('Euler', '6 + <i>f</i>', F(V('e', '9'), ' + 2'), '11'), fx('Solve', '<i>f</i>', F('11 − ', V('v', '6')), '5')],
  'This graph has <b>5 faces</b>. One graph (there are others):', f'{CAM} · Example 4 (p. 615)', video='Cambridge GO · Example 4 (13A Resources)',
  cmd=('How many', None, 'substitute into v + f = e + 2'), afig=Wd(330, ex4())))
S.append(qslide('yt', 'You try · Edrolo 8A WE3b', 'Using Euler’s formula',
  '<div style="font-size:26px;margin-top:30px">b. If a connected planar graph has five vertices and five faces, how many edges does the graph have?</div>',
  [('Known', '<i>v</i> = 5 · <i>f</i> = 5'), ('Substitute', '<i>v</i> − <i>e</i> + <i>f</i> = 2 → 5 − <i>e</i> + 5 = 2'), ('Simplify', '10 − <i>e</i> = 2'),
   ('Solve', '<i>e</i> = 8')],
  'The graph has <b>8 edges</b>.', f'{EDR} · 8A Worked example 3b (p. 525)', cmd=('how many', None, 'substitute, solve for e')))

# ================= Learn 5: adjacency matrices
S.append(learn('Learn · 13B', 'Adjacency matrices',
  '<h4>A matrix that records the connections</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>one row and one column per vertex (square)</li><li>entry = number of edges joining the row vertex and the column vertex</li>'
  '<li>a <b>loop</b> counts as <b>1</b> (on the leading diagonal)</li><li>an undirected graph gives a symmetric matrix</li></ul>',
  '<div style="display:flex;gap:30px;align-items:center;justify-content:center">' + Wd(300, net(LB_V, LB_E, sid='lb', W=330, H=215, pad=10)) + amat(L5, LB_M, fs=20, tid='lbm') + '</div>'
  '<div class="frag" style="font-size:18px;text-align:center" data-hi="#lb|ab|hy;#lbm|c0_1|hy">row A, column B = 1: one edge joins A and B</div>'
  '<div class="frag" style="font-size:18px;text-align:center" data-hi="#lb|bc1,bc2|hb;#lbm|c2_1|hb">row C, column B = 2: two edges join C and B</div>'
  '<div class="frag" style="font-size:18px;text-align:center" data-hi="#lbm|c0_3,c0_0|hc;#lb||">row A, column D = 0 (no edge) · row A, column A = 0 (no loop)</div>',
  'Row sums give the degrees, except that a loop adds 2 to the degree but only 1 to the matrix.', f'{CAM}, 13B pp. 619–620 (own words; Cambridge’s graph and matrix) · {EDR}, 8B pp. 532–534',
  cards=(kcard('Adjacency matrix', 'entry = number of edges joining <i>i</i> and <i>j</i>; loop = 1'),)))
# ================= Ex 5 / YT WE2 (matrix -> graph)
S.append(qslide('we', 'Worked example 5 · 13B', 'Drawing a graph from an adjacency matrix',
  '<div style="font-size:24px">Draw the graph that is represented by the following adjacency matrix.</div>' + amat(L5, EX5_M, fs=24, tid='m5'),
  [('Vertices', 'one dot for each of A to E'), ('Row A', 'A–C twice, A–E once', 'data-hi="#m5|' + row(0) + '|hy" data-show="#e5|ac1,ac2,ae"'),
   ('Row B', 'B–C twice, B–D once', 'data-hi="#m5|' + row(1) + '|hy" data-show="#e5|bc1,bc2,bd"'),
   ('Row C', 'C–D once (C–A, C–B already drawn)', 'data-hi="#m5|' + row(2) + '|hy" data-show="#e5|cd"'),
   ('Row D', 'the 1 at row D, column D = a loop at D', 'data-hi="#m5|c3_3|hc" data-show="#e5|dl"'), ('Rows D, E', 'nothing new to add', 'data-hi="#m5||"')],
  'The graph (drawn planar here, which is not required):', f'{CAM} · Example 5 (pp. 619–620)', video='Cambridge GO · Example 5 (13B Resources)',
  afig=Wd(380, ex5('e5'))))
S.append(qslide('yt', 'You try · Edrolo 8B WE2', 'Drawing a graph from an adjacency matrix',
  '<div style="font-size:24px"><b>Construct</b> a graph from the following adjacency matrix.</div>' + amat(L5, Y5_M, fs=24, tid='m6'),
  [('Vertices', 'the matrix is 5 × 5: five vertices A to E'), ('Row A', 'A–B once, A–C twice, A–E once', 'data-hi="#m6|' + row(0) + '|hy"'),
   ('Row B', 'B–D once (B–A already drawn)', 'data-hi="#m6|' + row(1) + '|hy"'), ('Row C', 'loop at C, C–D once', 'data-hi="#m6|' + row(2) + '|hy"'),
   ('Row D', 'loop at D, D–E twice', 'data-hi="#m6|' + row(3) + '|hy"'), ('Row E', 'all already drawn', 'data-hi="#m6||"')],
  'A correct graph (it may look different: it must have all these edges):', f'{EDR} · 8B Worked example 2 (pp. 534–535)', cmd=('Construct', None, 'row by row; diagonal = loop'),
  afig=Wd(360, y5())))
# ================= Ex 6 / YT WE1 (graph -> matrix)
S.append(qslide('we', 'Worked example 6 · 13B', 'Constructing an adjacency matrix',
  ('<div style="font-size:21px">Construct an adjacency matrix that can be used to represent the graph opposite. This graph represents the ways that three houses <i>A</i>, <i>B</i> and <i>C</i> are connected to three utility outlets, gas (<i>G</i>), water (<i>W</i>) and electricity (<i>E</i>).</div>',
   Wd(460, net(EX6_V, EX6_E, sid='e6', W=380, H=190, pad=12)), ''),
  [('Label', 'rows and columns A, B, C, G, W, E (6 × 6)'), ('Houses', 'each house joins G, W and E once; houses don’t join houses', 'data-hi="#e6|AG,AW,AE|hy"'),
   ('Utilities', 'each utility joins A, B and C once', 'data-hi="#e6|AG,BG,CG|hb"'), ('Diagonal', 'no loops → 0s', 'data-hi="#e6||"')],
  amat(['A', 'B', 'C', 'G', 'W', 'E'], EX6_M, fs=17), f'{CAM} · Example 6 (p. 620)', video='Cambridge GO · Example 6 (13B Resources)', cmd=('Construct', None, 'count edges between each pair')))
S.append(qslide('yt', 'You try · Edrolo 8B WE1', 'Constructing an adjacency matrix',
  ('<div style="font-size:24px"><b>Construct</b> an adjacency matrix from the following graph.</div>', Wd(430, net(Y6_V, Y6_E, sid='y6', W=320, H=225, pad=12)), ''),
  [('Order', 'five vertices → 5 × 5, rows and columns A to E'),
   ('Row A', 'loop (1), A–B twice, A–C once → 1 2 1 0 0', 'data-hi="#y6|al,ab1,ab2,ac|hy"'),
   ('Row B', 'B–A twice, B–C once, B–D once → 2 0 1 1 0', 'data-hi="#y6|ab1,ab2,bc,bd|hy"'),
   ('Rows C–E', 'C: 1 1 0 1 0 · D: 0 1 1 0 1 · E: 0 0 0 1 0', 'data-hi="#y6||"')],
  amat(L5, Y6_M, fs=18), f'{EDR} · 8B Worked example 1 (pp. 532–533)', cmd=('Construct', None, 'row by row; loop = 1')))

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2021 Exam 2 Q1a, b', 'Show what you know',
  '<div style="font-size:15px">Maggie’s house has five rooms, <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i>, and eight doors. The floor plan of these rooms and doors is shown below. The outside area, <i>F</i>, is shown shaded on the floor plan.'
  '<div style="display:flex;gap:14px;align-items:center"><div style="width:44%">' + img('vcaa2021e2_floorplan.png') + '</div><div style="width:52%">' + x1('x1') + '</div></div>'
  'The floor plan is represented by the graph above. On this graph, vertices represent the rooms and the outside area. Edges represent direct access to the rooms through the doors. One edge is missing from the graph.</div>'
  + plist([('a', 'On the <b>graph above</b>, draw the missing edge. <span class="muted">(1 mark)</span>'), ('b', 'What is the degree of vertex <i>E</i>? <span class="muted">(1 mark)</span>')]),
  [('a', '8 doors, only 7 edges: the door between rooms A and B has no edge', 'data-show="#x1|miss"'), ('b', 'E has doors to B and D', 'data-hi="#x1|e5,e6|hy"')],
  '', 'VCAA 2021 Further Mathematics Exam 2 Networks and decision mathematics Q1 stem, Q1a, Q1b (examiner report: average 1.9/2) · ' + EDR + ' 8A Q18',
  stat=('avg', 95), parts=[('a', 'Edge <b><i>A</i>–<i>B</i></b> (red)'), ('b', 'deg(<i>E</i>) = <b>2</b>')]))
sm(extra='sm xs')
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2021 Exam 1 Q3', 'Show what you know',
  ('<div style="font-size:24px">Consider the graph below.</div>', Wd(420, net(X2_V, X2_E, sid='x2', W=320, H=190, pad=16, faces=X2_F)), '<div style="font-size:24px">The number of faces is</div>'),
  [('Planar?', 'two edges cross: redraw one round the outside', 'data-hi="#x2|x13|hc" data-show="#x2|r13"'),
   ('Count', 'four faces (three inside + the outside)', 'data-show="#x2|f1,f2,f3,f4" data-hi="#x2|x13|hx"'),
   ('Check', '<i>v</i> + <i>f</i> = <i>e</i> + 2: 4 + 4 = 6 + 2 ✓')],
  '4 faces: <b>C</b>.', 'VCAA 2021 Further Mathematics Exam 1 Networks and decision mathematics Q3 (examiner report: 34% correct) · ' + EDR + ' 8A Q20',
  mc=['2', '3', '4', '5', '6'], key='C', stat=('mc', 34), dist=[1, 2, 34, 61, 1],
  dis=('D', '5 faces (61% chose it): counting the regions of the drawing as it is. The crossing is not a vertex, so redraw it planar first.')))
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2019 Exam 1 Q6', 'Show what you know',
  '<div style="font-size:16px">The map below shows all the road connections between five towns, <i>P</i>, <i>Q</i>, <i>R</i>, <i>S</i> and <i>T</i>.'
  + Wd(260, img('vcaa2019e1q6_map.png')) + 'The road connections could be represented by the adjacency matrix</div>',
  [('Loop', 'a road leaves P and comes back to P without passing another town → row P, column P = 1'),
   ('P–Q', 'three different roads join P and Q without passing another town → 3'),
   ('Match', 'only A has 1 at P–P and 3 at P–Q')],
  'Matrix <b>A</b>.', 'VCAA 2019 Further Mathematics Exam 1 Networks and decision mathematics Q6 (examiner report: 39% correct) · ' + EDR + ' 8B Q15',
  mc=[mtx(o, list('PQRST'), fs=12, cols=list('PQRST')) for o in X3_OPTS], key='A', stat=('mc', 39), dist=[39, 31, 14, 11, 4],
  dis=('B', '31% chose B: it has only 2 roads between P and Q (the road through the junction was missed).')))
sm(extra='sm mcm mc3')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 13 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] in ('13A', '13B') and v.get('url')]))
n = assemble(S, '12MAG · 13A-13B · Graphs, networks and adjacency matrices', os.path.join(ROOT, 'lessons', '13A-13B slides.html'))
print(n - 1, 'slides')
