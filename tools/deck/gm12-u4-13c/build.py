"""Lesson gm12-u4-13c (13C exploring and travelling) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/13C slides.html      Run: python3 tools/deck/gm12-u4-13c/build.py      Screenshots: python3 tools/deck/gm12-u4-13c/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; graphs redrawn with tools/deck/tpl/net.py, same vertices and edges):
- Do Now: VCAA 2024 Exam 1 Q33 (C, 75%) · VCAA 2025 Exam 1 Q29 (A, 84%; life-cycle diagram cropped) ·
          VCAA 2024 Exam 2 Q13 stem + Q13a (average 0.9/1; floor plan cropped) · VCAA 2025 Exam 2 Q7 stem + Q7b (average 0.7/1).
- APK: Cambridge U1&2 Ch 8 skills checklist #3 (graph from #1, p. 540) and #9 (p. 541); answers from the Skills Checklist answers (p. 833) ·
       Edrolo U1&2 7D Q11 (adapted from VCAA 2019 Exam 2 N&DM Q1bii; 93%).
- Learn: Cambridge U3&4 13C pp. 624-628 (own words; Cambridge's house-shaped graph) · Edrolo U3&4 8C pp. 548-553.
- Worked examples: Cambridge U3&4 Examples 7 (p. 626) and 8 (p. 628; road map cropped).
  You trys: Edrolo U3&4 8C Worked example 1 (pp. 549-550), WE2 (pp. 551-552), WE3 (pp. 553-554).
- No CAS (Cambridge prints none for 13C).
- Exits: VCAA 2019 Exam 2 N&DM Q1 stem + Q1bi (= Edrolo U3&4 8C Q14; 70%) · VCAA 2019 Exam 1 N&DM Q2 (= Edrolo 8C Q15; C, 64%) ·
         VCAA 2018 Exam 2 N&DM Q2 stem + Q2c (= Edrolo 8C Q16; 62%).
- % correct: VCAA examiner reports (via tools/y12_edrolo_exam_practice.csv, tools/y11_edrolo_exam_practice.csv and tools/vcaa_current_index.csv;
  2019 Exam 1 option split from the 2019 Exam 1 report).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
CAM = 'Cambridge General Mathematics Units 3&amp;4'; EDR = 'Edrolo General Mathematics Units 3&amp;4'; CAM12 = 'Cambridge General Mathematics Units 1&amp;2'
EDR12 = 'Edrolo General Mathematics Units 1&amp;2'
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-13c')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def mtx(rows, fs=15): return amat([''] * len(rows), rows, fs=fs, cols=[''] * len(rows[0]))
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def lab(t, s): return f'<div style="font-weight:700;font-size:15px;margin-bottom:-4px">{t}</div>{s}'
def quad(f, keys='abcd', px=230):
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px 14px">' + ''.join(f'<div>{lab(k, Wd(px, f(k)))}</div>' for k in keys) + '</div>'

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.mcm .mc{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px}'
     '.mcm .mc>div{align-items:center}.mcm .amat{margin:0}.tiles5{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:6px}'
     '.tiles5>div{background:#fff;border:3px solid var(--learn);border-radius:14px;padding:6px 8px;font-size:16px;text-align:center}.tiles5 b{display:block;font-size:19px;margin-bottom:2px}'
     '.wt{border-collapse:collapse;margin:8px auto;font-size:19px}.wt td,.wt th{border:2px solid #c9d3e6;padding:4px 12px;text-align:center}.wt th{background:#eef3fb}'
     '.amt{border-collapse:collapse;font-size:15px;margin:6px auto}.amt td,.amt th{border:1px solid #999;padding:2px 8px;text-align:right;white-space:nowrap}.amt th{white-space:normal}</style>']
# ================= opening
S.append(title('13C', 'Exploring and travelling', f'{CAM} · 13C Exploring and travelling', 'gm12-u4-13c'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 13C', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>13C')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('CFAT 4.13.1', '· 13A–13B, 20 min', '#00838F'), ('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· three Year 11 questions', 'var(--apk)'),
  ('Walks, trails, paths, circuits, cycles', '', None), ('Worked example 7', '→ You try', None), ('Eulerian trails and circuits', '', None),
  ('Hamiltonian paths and cycles', '', None), ('Worked example 8', '→ You try ×2', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'), ('Check-in and coursework', '', 'var(--muted)')]))
S.append(cfat('CFAT 4.13.1', 'Graphs, Euler’s rule and adjacency matrices', '13A–13B', 13, 'Edrolo U3&amp;4 8A–8B exercise questions · lessons/CFAT 4.13.1 (13A-13B)'))
S.append(keys([
  ('Walk', 'any sequence of edges from vertex to vertex'), ('Trail', 'a walk with no repeated edges'), ('Path', 'no repeated edges and no repeated vertices'),
  ('Circuit · cycle', 'a trail · a path that ends where it starts'),
  ('Eulerian', 'every edge exactly once (trail; circuit if it returns to the start)'), ('Hamiltonian', 'every vertex exactly once (path; cycle if it returns to the start)')],
  [('Eulerian circuit', 'connected + <b>all</b> vertices even', 'start anywhere'),
   ('Eulerian trail', 'connected + exactly <b>two</b> odd vertices', 'start at one odd vertex, finish at the other'),
   ('Neither', 'more than two odd vertices', 'Hamiltonian: no rule, find one by inspection')],
  f'{CAM}, 13C pp. 624–628; Study Design: the exploring and travelling problem, walks, trails, paths, Eulerian trails and circuits, and Hamiltonian paths and cycles'))

# ================= Do Now 1: VCAA 2024 E1 Q33 (13A)
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2024 Exam 1 Q33', 'Review of 13A (degree of a vertex)',
  ('<div style="font-size:24px">Consider the following graph.</div>', Wd(380, net(D1_V, D1_E, sid='d1', W=200, H=130, pad=16)), '<div style="font-size:24px">The sum of the degrees of the vertices is</div>'),
  [('Count edges', '5 edges + 1 loop = 6 edges (the isolated vertex has degree 0)', 'data-hi="#d1|lt,tm,tr,mb,br,rl|hy"'),
   fx('Sum', 'sum of degrees', F('2 × ', V('edges', '6')), '12', 'data-hi="#d1||"')],
  'Sum of degrees = 2 × 6 = 12: <b>C</b>.', 'VCAA 2024 General Mathematics Exam 1 Q33 (examiner report: 75% correct)',
  mc=['10', '11', '12', '13'], key='C', stat=('mc', 75)))
# ================= Do Now 2: VCAA 2025 E1 Q29 (11E)
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2025 Exam 1 Q29', 'Review of 11E (Leslie matrices)',
  '<div style="font-size:16px">The female population of an animal species has been divided into four age groups (1, 2, 3 and 4), with age group 1 being the youngest.<br>'
  'The age groups, birth rates and survival rates are presented in the life-cycle diagram below.' + Wd(440, img('vcaa2025e1q29_lifecycle.png'))
  + 'Which one of the following is a Leslie matrix that corresponds with this life-cycle diagram?</div>',
  [('Row 1', 'birth rates (arrows back to 1): 0, 2.1, 4.6, 1.8'), ('Sub-diagonal', 'survival rates 0.9, 0.7, 0.2 under the leading diagonal')],
  'Birth rates in row 1, survival rates on the sub-diagonal: <b>A</b>.', 'VCAA 2025 General Mathematics Exam 1 Q29 (examiner report: 84% correct)',
  mc=[mtx(o) for o in [[['0', '2.1', '4.6', '1.8'], ['0.9', '0', '0', '0'], ['0', '0.7', '0', '0'], ['0', '0', '0.2', '0']],
                        [['0', '0.9', '0.7', '0.2'], ['2.1', '0', '0', '0'], ['0', '4.6', '0', '0'], ['0', '0', '1.8', '0']],
                        [['2.1', '4.6', '1.8', '0'], ['0.9', '0', '0', '0'], ['0', '0.7', '0', '0'], ['0', '0', '0.2', '0']],
                        [['2.1', '4.6', '1.8', '0.8'], ['0', '0.9', '0', '0'], ['0', '0', '0.7', '0'], ['0', '0', '0', '0.2']]]], key='A', stat=('mc', 84)))
sm(extra='sm mcm')
# ================= Do Now 3: VCAA 2024 E2 Q13a (13A)
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2024 Exam 2 Q13a', 'Review of 13A (graphs from a floor plan)',
  '<div style="font-size:16px">A supermarket has five departments, with areas allocated as shown on the floorplan below.' + Wd(400, img('vcaa2024e2q13_floorplan.png'))
  + 'The floorplan is represented by the graph below.<br>On this graph, vertices represent departments and edges represent boundaries between two departments.<br>This graph is incomplete.'
  + Wd(300, d3('d3')) + 'a. <b>Draw</b> the missing vertex and missing edges on the graph above. Include a label. <span class="muted">(1 mark)</span></div>',
  [('Missing vertex', 'Promotional (<i>P</i>) has no vertex', 'data-show="#d3|vP,tP"'),
   ('Its boundaries', '<i>P</i> shares a wall with General (<i>G</i>) and Fresh produce (<i>F</i>), not with Bakery', 'data-show="#d3|pg,pf"')],
  'Vertex <b><i>P</i></b> joined to <b><i>G</i></b> and <b><i>F</i></b> (red).', 'VCAA 2024 General Mathematics Exam 2 Q13 stem and Q13a (examiner report: average 0.9/1)',
  stat=('avg', 90), cmd=('Draw', 1, 'vertex, label and edges')))
sm()
# ================= Do Now 4: VCAA 2025 E2 Q7b (8C)
AMT = ('<table class="amt"><tr><th>Payment number</th><th>Payment ($)</th><th>Interest ($)</th><th>Principal reduction ($)</th><th>Balance ($)</th></tr>'
       '<tr><td>0</td><td>0.00</td><td>0.00</td><td>0.00</td><td>850 000.00</td></tr><tr><td>1</td><td>15 730.88</td><td>2975.00</td><td>12 755.88</td><td>837 244.12</td></tr>'
       '<tr><td>2</td><td>15 730.88</td><td>2930.35</td><td>12 800.53</td><td>824 443.59</td></tr></table>')
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2025 Exam 2 Q7b', 'Review of 8C (amortisation tables)',
  '<div style="font-size:20px">Declan is a filmmaker and content creator.<br>He has taken out a reducing balance loan to fund a new production.<br>'
  'Interest is calculated monthly and Declan makes monthly repayments.<br>Three rows of the amortisation table for Declan’s loan are shown below.' + AMT
  + 'b. Why is the interest associated with payment 2 lower than the interest associated with payment 1? <span class="muted">(1 mark)</span></div>',
  [('Interest', 'interest each month = monthly rate × the balance owing'), ('Balance', 'payment 1 reduced the balance from $850 000.00 to $837 244.12')],
  'The balance owing is lower before payment 2, so <b>less interest</b> is charged on it.', 'VCAA 2025 General Mathematics Exam 2 Q7 stem and Q7b (examiner report: average 0.7/1)',
  stat=('avg', 70), cmd=('Why', 1, 'a reason that refers to the balance')))

# ================= APK 1: checklist #3
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #3', 'Connected graphs and bridges',
  ('<div style="font-size:24px">Give a reason why the graph above would be considered connected. Are there any bridges present? If yes, identify the two vertices the bridge(s) exist between.</div>',
   Wd(420, net(K1_V, K1_E, sid='k1', W=290, H=200, pad=14)), ''),
  [('Connected', 'every vertex can be reached from every other vertex', 'data-hi="#k1|ab,ae,be,bd,ed,dc|hb"'),
   ('Bridge?', 'remove an edge: does the graph fall into two pieces? Only C–D does', 'data-hi="#k1|dc|hc"')],
  'Connected: there is a path between each pair of vertices. <b>Yes</b>: one bridge, between <b>C and D</b>.',
  f'{CAM12} · Ch 8 skills checklist #3 (graph from #1), p. 540 · answer from the Skills Checklist answers', cmd=('Give a reason', None, 'path between every pair')))
# ================= APK 2: checklist #9
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #9', 'Classifying a walk',
  ('<div style="font-size:24px">For the graph below, is the walk <i>S</i>-<i>R</i>-<i>Q</i>-<i>P</i>-<i>O</i>-<i>N</i>-<i>M</i>-<i>S</i> considered a trail, path, circuit or cycle?</div>',
   Wd(430, net(K9_V, K9_E, sid='k9', W=285, H=170, pad=14)), ''),
  [('Trace it', 'S–R, R–Q, Q–P, P–O, O–N, N–M, M–S', 'data-hi="#k9|rs,qr,pq,op,no,mn,ms|hy"'), ('Repeats?', 'no edge or vertex repeated (except S at both ends)'),
   ('Ends', 'starts and ends at S → circuit or cycle')],
  'No repeated edges or vertices and it returns to <i>S</i>: a <b>cycle</b>.', f'{CAM12} · Ch 8 skills checklist #9, p. 541 · answer from the Skills Checklist answers'))
# ================= APK 3: Edrolo U1&2 7D Q11 (adapted VCAA 2019 E2 Q1bii)
HKA = walk(['Mount Cockatoo', 'Snake Point', 'Point Kangaroo', 'Sunset Lookout', 'Waterfall Way', 'Feather Mountain', 'Mount Cockatoo'], pre='h', hid=True, bend=8)
S.append(qslide('apk', 'APK · VCAA 2019 Exam 2 Q1bii (adapted)', 'Visiting every vertex once',
  ('<div style="font-size:20px">A hiking trail has six lookout points. The following network shows these lookout points represented by vertices. The edges of the network represent the paths between the lookout points.</div>',
   Wd(560, hike('hk', extra=HKA)), '<div style="font-size:20px">A hiking tour starts and finishes at Mount Cockatoo, visiting each lookout only once.<br><b>Draw</b> a possible route for this tour. <span class="muted">(1 mark)</span></div>'),
  [('Start', 'Mount Cockatoo → Snake Point → Point Kangaroo', 'data-show="#hk|h1,h2"'), ('Continue', '→ Sunset Lookout → Waterfall Way → Feather Mountain', 'data-show="#hk|h3,h4,h5"'),
   ('Finish', '→ back to Mount Cockatoo: every lookout once', 'data-show="#hk|h6"')],
  'Cockatoo – Snake – Kangaroo – Sunset – Waterfall – Feather – Cockatoo (or the reverse).',
  f'Adapted from VCAA 2019 Further Mathematics Exam 2 Networks and decision mathematics Q1bii (93% answered this type of question correctly) · {EDR12} 7D Q11',
  stat=('mc', 93), cmd=('Draw', 1, 'a route through every vertex once')))
sm(extra='sm xs')

# ================= Learn 1: walks, trails, paths
def frag(t, a=''): return f'<div class="frag" style="font-size:22px;text-align:center;line-height:1.3" {a}>{t}</div>'
S.append(learn('Learn · 13C', 'Walks, trails and paths',
  '<h4>Ways of travelling through a graph</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>walk</b>: any sequence of edges (repeats allowed)</li><li><b>trail</b>: a walk with <b>no repeated edges</b></li>'
  '<li><b>path</b>: no repeated edges <b>and no repeated vertices</b></li><li>write a walk as its vertices in order: A–C–A–D–G</li></ul>',
  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">'
  + ''.join(f'<div class="frag">{lab(t, Wd(260, house("l" + k, k)))}<div style="font-size:16px;text-align:center">{d}</div></div>'
            for k, t, d in [('walk', 'Walk · A–C–A–D–G', 'edge A–C used twice'), ('trail', 'Trail · B–E–F–C–B–A', 'no repeated edge; B repeated'),
                            ('path', 'Path · A–D–C–F–E–B', 'nothing repeated')]) + '</div>',
  'Trail = no repeated EDGES. Path = no repeated edges or VERTICES. Every path is a trail; every trail is a walk.',
  f'{CAM}, 13C pp. 624–625 (own words; Cambridge’s graph and walks) · {EDR}, 8C p. 548', cards=(kcard('Trail', 'no repeated edges'), kcard('Path', 'no repeated vertices'))))
# ================= Learn 2: circuits and cycles + decision table
S.append(learn('Learn · 13C', 'Circuits and cycles',
  '<h4>Walks that end where they start</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>circuit</b>: a trail that starts and ends at the same vertex</li><li><b>cycle</b>: a path that starts and ends at the same vertex</li>'
  '<li>the start/end vertex does not count as a repeat</li></ul>',
  '<div style="display:flex;gap:20px;align-items:center;justify-content:center">'
  + ''.join(f'<div class="frag" style="width:260px">{lab(t, house("m" + k, k))}<div style="font-size:16px;text-align:center">{d}</div></div>'
            for k, t, d in [('circuit', 'Circuit · A–C–F–G–D–C–B–A', 'no repeated edge; C repeated'), ('cycle', 'Cycle · F–E–B–C–F', 'nothing repeated')])
  + '<table class="wt frag"><tr><th></th><th>open</th><th>closed (same start/end)</th></tr><tr><th>edges repeat</th><td>walk</td><td>walk</td></tr>'
    '<tr><th>no repeated edges</th><td>trail</td><td>circuit</td></tr><tr><th>no repeated vertices</th><td>path</td><td>cycle</td></tr></table></div>',
  'Ask two questions: same start and end? Then what repeats: an edge, a vertex, or nothing?', f'{CAM}, 13C pp. 625–626 (own words) · {EDR}, 8C pp. 548–549',
  cards=(kcard('Circuit', 'closed trail'), kcard('Cycle', 'closed path'))))
# ================= Ex 7 / YT WE1
S.append(qslide('we', 'Worked example 7 · 13C', 'Identifying types of walks',
  '<div style="font-size:19px"><b>Identify</b> the walk in each of graphs below as a trail, path, circuit, cycle or walk only.</div>'
  + quad(lambda k: ex7(k) + f'<div style="font-size:14px;text-align:center">start {E7_SE[k][0]} · end {E7_SE[k][1]}</div>', px=225),
  [('a', 'D–B–C–A–E–C–D: same start and end; C twice, no edge twice'), ('b', 'A–E–C–D–B–A: same start and end; nothing repeated'),
   ('c', 'B–C–A–B–D–F: different ends; B twice, no edge twice'), ('d', 'D–E–C–A–E–C–B: C, E and the edge C–E repeated')],
  '', f'{CAM} · Example 7 (p. 626)', video='Cambridge GO · Example 7 (13C Resources)', cmd=('Identify', None, 'same start/end? what repeats?'),
  parts=[('a', '<b>circuit</b>'), ('b', '<b>cycle</b>'), ('c', '<b>trail</b>'), ('d', '<b>walk</b> only')]))
sm(extra='sm mp')
S.append(qslide('yt', 'You try · Edrolo 8C WE1', 'Identifying types of walks',
  '<div style="font-size:19px"><b>Determine</b> if the walk in each graph is a trail, path, circuit, cycle, or just a walk.</div>'
  + quad(lambda k: ey1(k) + f'<div style="font-size:14px;text-align:center">start {Y1_W[k][0]} · end {Y1_W[k][-1]}</div>', px=225),
  [('a', 'F–E–C–D–A–F: starts and ends at F; nothing repeated'), ('b', 'A–E–D–B–C: different ends; nothing repeated'),
   ('c', 'D–A–F–E–D–B–C: different ends; no repeated edge, D repeated'), ('d', 'B–C–E–D–A–D–B: starts and ends at B; edge A–D repeated')],
  '', f'{EDR} · 8C Worked example 1 (pp. 549–550)', cmd=('Determine', None, 'same start/end? what repeats?'),
  parts=[('a', '<b>Cycle</b>'), ('b', '<b>Path</b>'), ('c', '<b>Trail</b>'), ('d', '<b>Walk</b>')]))
sm(extra='sm mp')

# ================= Learn 3: Eulerian
EUL_V = {'A': (20, 110, 'w'), 'B': (80, 20, 'n'), 'C': (150, 95, 'e'), 'D': (200, 15, 'n'), 'E': (265, 150, 'e')}
EUL_E = [('A', 'B', {'i': 'ab'}), ('B', 'C', {'i': 'bc'}), ('A', 'C', {'i': 'ac1', 'bend': -6}), ('A', 'C', {'i': 'ac2', 'bend': 18}), ('C', 'D', {'i': 'cd'}), ('D', 'E', {'i': 'de'})]
S.append(learn('Learn · 13C', 'Eulerian trails and circuits',
  '<h4>Every Edge exactly once</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>Eulerian circuit</b>: connected and <b>every</b> vertex has even degree; start anywhere</li>'
  '<li><b>Eulerian trail</b>: connected and exactly <b>two</b> odd vertices; start at one odd vertex, finish at the other</li>'
  '<li>more than two odd vertices: neither</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(380, net(EUL_V, EUL_E + walk('ACABCDE', pre='u', hid=True, bend=7), sid='eu', W=285, H=170, pad=16)) + '<div style="width:420px">'
  + frag('Count degrees: A 3 · B 2 · C 4 · D 2 · E 1', 'data-hi="#eu|ac1,ac2,ab|hy"')
  + frag('Exactly two odd vertices (A and E) → an Eulerian trail from A to E', 'data-hi="#eu||"')
  + frag('A–C–A–B–C–D–E uses every edge once', 'data-show="#eu|u1,u2,u3,u4,u5,u6"') + '</div></div>',
  'Cambridge counts a circuit as a special trail (zero odd vertices). Edrolo and most exam questions say “Eulerian trail” only when there are exactly two odd vertices: answer the question that is asked.',
  f'{CAM}, 13C pp. 626–627 (own words) · {EDR}, 8C pp. 550–551 (Edrolo’s example graph)', cards=(kcard('Eulerian circuit', 'all even'), kcard('Eulerian trail', 'exactly two odd'))))
# ================= Learn 4: Hamiltonian
S.append(learn('Learn · 13C', 'Hamiltonian paths and cycles',
  '<h4>Every vertex exactly once</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>Hamiltonian path</b>: visits every vertex once (it need not use every edge)</li>'
  '<li><b>Hamiltonian cycle</b>: a Hamiltonian path that returns to its start</li><li>no rule: find one by <b>inspection</b> (trial)</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(380, net(HS_V, HS_E + walk('ABEFGDCA', pre='hm', hid=True, bend=7), sid='hm', W=330, H=195, pad=14)) + '<div style="width:400px">'
  + frag('Start at A and visit B, E, F, G, D, C once each', 'data-show="#hm|hm1,hm2,hm3,hm4,hm5,hm6"')
  + frag('A–B–E–F–G–D–C is a Hamiltonian path') + frag('Add C–A: A–B–E–F–G–D–C–A is a Hamiltonian cycle', 'data-show="#hm|hm7"') + '</div></div>',
  'Eulerian = Edges (both start with E). Hamiltonian = vertices: don’t repeat a vertex, and you may skip edges.',
  f'{CAM}, 13C pp. 627–628 (own words; Cambridge’s house graph) · {EDR}, 8C pp. 552–553', cards=(kcard('Hamiltonian', 'every vertex once'),)))
# ================= Ex 8
TS = towns('tw', hid=True)
S.append(qslide('we', 'Worked example 8 · 13C', 'Eulerian and Hamiltonian travel',
  '<div style="display:flex;gap:10px;align-items:center;font-size:14px"><div style="flex:1">A map showing the towns of St Andrews, Kinglake, Yarra Glen, Toolangi and Healesville is shown on the right. Consider only the yellow routes in your answer. '
  'St Andrews and Yarra Glen are considered connected, although this route is not fully shown in the image.</div><div style="flex:0 0 250px">' + img('cam_ex8_map.png', '250px') + '</div></div>'
  + plist([('a', '<b>Draw</b> a graph with a vertex representing each of these towns and edges representing the direct road connections between the towns.'),
           ('b', '<b>Explain</b> why an Eulerian trail, but not an Eulerian circuit, is possible through this graph.'),
           ('c', '<b>Write down</b> an Eulerian trail that begins at Toolangi.'), ('d', '<b>Write down</b> a Hamiltonian cycle that begins at Healesville.')]),
  [('a', 'one vertex per town; an edge for each direct road (7 roads)', 'data-show="#tw|sk,sy,ky,kt,yt,yh,ht"'),
   ('b', 'degrees: St Andrews 2, Kinglake 3, Yarra Glen 4, Toolangi 3, Healesville 2', 'data-hi="#tw|kt,ky,sk,yt,ht|hy"'),
   ('c', 'start at an odd vertex (Toolangi), finish at the other (Kinglake)', 'data-hi="#tw||"'), ('d', 'visit each town once, return to Healesville')],
  '', f'{CAM} · Example 8 (p. 628; map from the textbook)', video='Cambridge GO · Example 8 (13C Resources)',
  parts=[('a', Wd(300, TS.replace(' class="hid0"', ''))), ('b', 'Exactly two odd-degree vertices (Toolangi, Kinglake): an Eulerian trail exists, but not an Eulerian circuit.'),
         ('c', 'Toolangi–Healesville–Yarra Glen–Toolangi–Kinglake–Yarra Glen–St Andrews–Kinglake'),
         ('d', 'Healesville–Yarra Glen–St Andrews–Kinglake–Toolangi–Healesville')]))
sm(extra='sm mp xs')
# ================= YT WE2 (Eulerian)
DRA = walk('BEABCDAB', pre='c', hid=True, bend=8)
S.append(qslide('yt', 'You try · Edrolo 8C WE2', 'Eulerian trails and circuits',
  '<div style="font-size:20px">The following graph represents a map of a walking track in the Dandenong Ranges.<br>The vertices represent lookout points.'
  + Wd(400, dandy('dr', extra=DRA)) + '</div>'
  + plist([('a', 'Is an Eulerian trail possible in this graph?'), ('b', 'Is an Eulerian circuit possible in this graph?'), ('c', '<b>Write down</b> an Eulerian circuit starting from lookout B.')]),
  [('a, b', 'connected · degrees: A 4, B 4, C 2, D 2, E 2 (all even)', 'data-hi="#dr|ab1,ab2,ae,ad|hy"'),
   ('a', 'Edrolo’s rule: a trail needs exactly two odd vertices: none here', 'data-hi="#dr||"'), ('b', 'all even → a circuit'),
   ('c', 'from B, use every edge once, back to B', 'data-show="#dr|c1,c2,c3,c4,c5,c6,c7"')],
  '', f'{EDR} · 8C Worked example 2 (pp. 551–552)', cmd=('Write down', None, 'every edge once, back to B'),
  parts=[('a', '<b>Not possible</b> (Edrolo; all vertices are even)'), ('b', '<b>Possible</b>'), ('c', '<b>B–E–A–B–C–D–A–B</b> (others are possible)')]))
sm(extra='sm mp')
# ================= YT WE3 (Hamiltonian)
MXA = walk(['PO', '1', '2', '4', '3', '6', '5'], pre='p', hid=True, bend=8) + walk(['PO', '2', '4', '3', '6', '5', '1', 'PO'], pre='q', hid=True, bend=-8, col='#1f9e74')
S.append(qslide('yt', 'You try · Edrolo 8C WE3', 'Hamiltonian paths and cycles',
  '<div style="font-size:20px">Max the mailman is doing his morning delivery run and has to deliver packages to six houses. These houses and the post office where the packages are stored are shown in the graph.'
  + Wd(400, maxg('mx', extra=MXA)) + '</div>'
  + plist([('a', '<b>Write down</b> a Hamiltonian path that allows Max to deliver all of his packages.'),
           ('b', '<b>Write down</b> a Hamiltonian cycle that allows Max to deliver all of his packages before returning to the post office.')]),
  [('a', 'start at PO, visit every house once, end anywhere', 'data-show="#mx|p1,p2,p3,p4,p5,p6"'),
   ('b', 'start and end at PO, every house once', 'data-show="#mx|q1,q2,q3,q4,q5,q6,q7" data-hi="#mx|p1|hx"')],
  '', f'{EDR} · 8C Worked example 3 (pp. 553–554)', cmd=('Write down', None, 'every vertex once'),
  parts=[('a', '<b>PO–1–2–4–3–6–5</b> (others are possible)'), ('b', '<b>PO–2–4–3–6–5–1–PO</b> (others are possible)')]))
sm(extra='sm mp')

# ================= Exits
FHA = walk(['office', 'science laboratories', 'mathematics classrooms', 'library', 'computer rooms', 'gymnasium', 'office'], pre='f', hid=True, bend=8)
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2019 Exam 2 Q1bi', 'Show what you know',
  ('<div style="font-size:20px">Fencedale High School has six buildings. The network shows these buildings represented by vertices.<br>The edges represent the paths between the buildings.</div>',
   Wd(600, fence('fh', extra=FHA)),
   '<div style="font-size:20px">A school tour is to start and finish at the office, visiting each building only once.<br>What is the mathematical term for this route? <span class="muted">(1 mark)</span></div>'),
  [('Every vertex', 'each building visited once → Hamiltonian', 'data-show="#fh|f1,f2,f3,f4,f5,f6"'), ('Closed', 'starts and finishes at the office → cycle')],
  'A <b>Hamiltonian cycle</b>.', 'VCAA 2019 Further Mathematics Exam 2 Networks and decision mathematics Q1 stem and Q1bi (examiner report: 70%) · ' + EDR + ' 8C Q14',
  stat=('mc', 70), cmd=('What is', 1, 'the full name')))
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2019 Exam 1 Q2', 'Show what you know',
  ('<div style="font-size:22px">Consider the following graph.</div>', Wd(420, net(X2_V, X2_E + [('_1', '_2', {'i': 'n1', 'hid': True, 'col': RED, 'dash': True, 'bend': 14}),
                                                                                          ('_3', '_5', {'i': 'n2', 'hid': True, 'col': RED, 'dash': True, 'bend': 14})], sid='x2', W=240, H=130, pad=12)),
   '<div style="font-size:22px">The minimum number of extra edges that are required so that an Eulerian circuit is possible in this graph is</div>'),
  [('Degrees', 'four odd vertices (3, 3, 3, 5) and two even'), ('Pair them', 'each new edge makes two odd vertices even: 4 odd ÷ 2 = 2 edges', 'data-show="#x2|n1,n2"')],
  '2 extra edges: <b>C</b>.', 'VCAA 2019 Further Mathematics Exam 1 Networks and decision mathematics Q2 (examiner report: 64% correct) · ' + EDR + ' 8C Q15',
  mc=['0', '1', '2', '3', '4'], key='C', stat=('mc', 64), dist=[6, 11, 64, 12, 7]))
ZNA = walk('FEHIJGDABC', pre='z', hid=True, bend=0)
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2018 Exam 2 Q2c', 'Show what you know',
  '<div style="font-size:19px">In one area of the town of Zenith, a postal worker delivers mail to 10 houses labelled as vertices A to J on the following graph.'
  + '<div style="display:flex;gap:16px;align-items:flex-start"><div style="flex:1">' + zen() + '</div><div style="flex:1.3;font-size:19px">The postal worker has delivered the mail at F and will continue her deliveries by following a Hamiltonian path from F.<br>'
  '<b>Draw</b> in a possible Hamiltonian path for the postal worker on the following diagram. <span class="muted">(1 mark)</span></div></div>' + Wd(250, zen('zn', dash=True, extra=ZNA)) + '</div>',
  [('Start', 'F → E → H → I → J', 'data-show="#zn|z1,z2,z3,z4"'), ('Continue', '→ G → D → A → B → C: all 10 houses, once each', 'data-show="#zn|z5,z6,z7,z8,z9"')],
  '<b>F–E–H–I–J–G–D–A–B–C</b> (others are possible).', 'VCAA 2018 Further Mathematics Exam 2 Networks and decision mathematics Q2 stem and Q2c (examiner report: 62%) · ' + EDR + ' 8C Q16',
  stat=('mc', 62), cmd=('Draw', 1, 'every vertex once from F')))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 13 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '13C' and v.get('url')]))
n = assemble(S, '12MAG · 13C · Exploring and travelling', os.path.join(ROOT, 'lessons', '13C slides.html'))
print(n - 1, 'slides')
