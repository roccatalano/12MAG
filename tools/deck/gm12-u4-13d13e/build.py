"""Lesson gm12-u4-13d13e (13D weighted graphs and networks, 13E Dijkstra's algorithm) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/13D-13E slides.html      Run: python3 tools/deck/gm12-u4-13d13e/build.py      Screenshots: python3 tools/deck/gm12-u4-13d13e/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; graphs redrawn with tools/deck/tpl/net.py, same vertices, edges and weights):
- Do Now: VCAA 2025 Exam 1 Q34 (C, 85%) · VCAA 2026 NHT Exam 1 Q39 (B; NHT report gives no %) ·
          VCAA 2024 Exam 2 Q13 stem + Q13bi (average 0.9/1; floor plan cropped, as in 13C) · VCAA 2023 Exam 2 Q12 stem + Q12bi (average 0.9/1).
- APK: Cambridge U1&2 Ch 8 skills checklist #14 (p. 542; answer 17 from the Skills Checklist answers) ·
       VCAA 2020 Exam 2 N&DM Q3 stem + Q3a in the original wording (= Edrolo U1&2 7E Q14; average 0.6/1).
- Learn: Cambridge U3&4 13D pp. 633-634 and 13E pp. 637-639 (own words; Cambridge's Croghon network) · Edrolo U3&4 8F pp. 585-587 (table method, Edrolo's A-E example).
- Worked examples: Cambridge U3&4 Example 9 (p. 634), Example 10 (pp. 638-639, graphical method).
  You trys: Edrolo U3&4 8F Worked example 1 (p. 585), Worked example 2 (pp. 588-589, table method).
- No CAS (Cambridge prints none for 13D/13E).
- Exits: VCAA 2018 Exam 1 N&DM Q2 in the original wording (= Edrolo U3&4 8F Q10, adapted there; C 68%, option split from the 2018 Exam 1 report) ·
         VCAA 2017 Exam 2 N&DM Q1 stem + Q1b (= Edrolo 8F Q11; average 0.8/1).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
import importlib.util
_s = importlib.util.spec_from_file_location('f13c', os.path.join(H, '..', 'gm12-u4-13c', 'figs.py')); F13C = importlib.util.module_from_spec(_s); _s.loader.exec_module(F13C)
D13C = os.path.join(H, '..', 'gm12-u4-13c')
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-13d13e')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}'
     '.wt{border-collapse:collapse;margin:6px auto;font-size:18px}.wt td,.wt th{border:2px solid #c9d3e6;padding:3px 10px;text-align:center}.wt th{background:#eef3fb}'
     '.tp{border-collapse:collapse;margin:6px auto;font-size:16px}.tp td,.tp th{border:1px solid #333;padding:4px 8px;text-align:left}.tp th{text-align:center}</style>']
# ================= opening
S.append(title('13D–13E', 'Shortest paths and Dijkstra’s algorithm', f'{CAM} · 13D Weighted graphs and networks · 13E Dijkstra’s algorithm', 'gm12-u4-13d13e'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 13D–13E', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>13D–13E')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· two Year 11 questions', 'var(--apk)'),
  ('Weighted graphs and networks', '', None), ('Shortest path by inspection', '', None), ('Worked example 9', '→ You try', None),
  ('Dijkstra’s algorithm', '· graph and table methods', None), ('Worked example 10', '→ You try', None), ('Exit tasks', '· two VCAA questions', 'var(--exit)'),
  ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Weighted graph', 'a graph with a number (weight) on each edge'), ('Network', 'a weighted graph whose weights are physical quantities: distance, time, cost'),
  ('Shortest path', 'the route between two vertices with the smallest total weight'), ('By inspection', 'list the possible routes and add their weights'),
  ('Dijkstra’s algorithm', 'a step-by-step method that finds the shortest path from a starting vertex')],
  [('Length of a route', 'add the weights of its edges', 'e.g. 7 + 9 + 11 = 27 km'),
   ('Dijkstra · update', 'new label = circled label + edge weight', 'keep the smaller of the new and old label'),
   ('Dijkstra · next', 'circle the smallest uncircled label', 'stop when the destination is circled'),
   ('Backtrack', 'destination label − edge weight = previous circled label', 'gives the route')],
  f'{CAM}, 13D pp. 633–634 and 13E pp. 637–639; {EDR}, 8F pp. 585–587; Study Design: shortest path by inspection; the shortest path problem and Dijkstra’s algorithm'))

# ================= Do Now 1: VCAA 2025 E1 Q34 (13C bridges)
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2025 Exam 1 Q34', 'Review of 13C (bridges)',
  ('<div style="font-size:24px">Consider the following graph.</div>', Wd(380, net(B1_V, B1_E, sid='b1', W=320, H=230, pad=12)), '<div style="font-size:24px">The number of bridges in this graph is</div>'),
  [('Bridge', 'an edge whose removal disconnects the graph'), ('Triangles', 'edges in a triangle (a cycle) are never bridges'),
   ('The chain', 'the three edges joining the left triangles to the right triangle', 'data-hi="#b1|b12,b23,b34|hc"')],
  '3 bridges: <b>C</b>.', 'VCAA 2025 General Mathematics Exam 1 Q34 (examiner report: 85% correct)', mc=['1', '2', '3', '4'], key='C', stat=('mc', 85)))
# ================= Do Now 2: VCAA 2026 NHT E1 Q39 (13B/13C)
M39 = amat(['Q', 'R', 'S', 'T', 'U'], [['1', '1', '1', '0', '0'], ['1', '0', '2', '1', '1'], ['1', '2', '0', '0', '1'], ['0', '1', '0', '0', '2'], ['0', '1', '1', '2', '0']], fs=20, tid='m39')
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2026 NHT Exam 1 Q39', 'Review of 13B–13C (adjacency matrices, Eulerian circuits)',
  ('<div style="font-size:21px">A graph consists of five vertices: <i>Q</i>, <i>R</i>, <i>S</i>, <i>T</i> and <i>U</i>.<br>An adjacency matrix for the graph is shown below.</div>', M39,
   '<div style="font-size:21px">For this graph, which one of the following statements is <b>not</b> true?</div>'),
  [('Loop', 'row Q, column Q = 1: a loop at Q (D is true)', 'data-hi="#m39|c0_0|hy"'),
   ('Degree of R', '1 + 0 + 2 + 1 + 1 = 5: odd', 'data-hi="#m39|c1_0,c1_1,c1_2,c1_3,c1_4|hc"'),
   ('Eulerian circuit?', 'needs every vertex even: R is odd, so no Eulerian circuit')],
  'B is not true: <b>B</b>.', 'VCAA 2026 (NHT) General Mathematics Exam 1 Q39 (NHT examiner reports give no % correct)',
  mc=['The graph contains a Hamiltonian cycle.', 'The graph contains an Eulerian circuit.', 'The graph contains a spanning tree with four edges.', 'The graph has a loop.'], key='B'))
sm()
# ================= Do Now 3: VCAA 2024 E2 Q13bi (13C)
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2024 Exam 2 Q13bi', 'Review of 13C (Hamiltonian paths)',
  '<div style="font-size:16px">A supermarket has five departments, with areas allocated as shown on the floorplan below.' + Wd(360, img('vcaa2024e2q13_floorplan.png', d=D13C))
  + 'The floorplan is represented by the graph below.<br>On this graph, vertices represent departments and edges represent boundaries between two departments.'
  + Wd(260, F13C.d3('d3').replace(' class="hid0"', '').replace(F13C.RED, '#1f4fb0')) + 'Karla is standing in the Promotional department.<br>She wants to visit each department in the supermarket once only.<br>'
  'b. i. In which department will she finish? <span class="muted">(1 mark)</span></div>',
  [('Once only', 'every vertex once: a Hamiltonian path from <i>P</i>'), ('Degree 1', 'Bakery (<i>B</i>) joins only <i>G</i>: once you reach <i>B</i> you cannot leave', 'data-hi="#d3|e3|hy"'),
   ('Route', '<i>P</i>–<i>F</i>–<i>D</i>–<i>G</i>–<i>B</i>', 'data-hi="#d3||"')],
  'She will finish in the <b>Bakery</b> (<i>B</i>).', 'VCAA 2024 General Mathematics Exam 2 Q13 stem and Q13bi (examiner report: average 0.9/1); floor plan from the paper',
  stat=('avg', 90)))
sm()
# ================= Do Now 4: VCAA 2023 E2 Q12bi (13A)
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2023 Exam 2 Q12bi', 'Review of 13A (Euler’s formula)',
  ('<div style="font-size:21px">A country has five states, <i>A, B, C, D</i> and <i>E</i>.<br>A graph can be drawn with vertices to represent each of the states.<br>Edges represent a border shared between two states.</div>',
   Wd(330, net(ST_V, ST_E, sid='st', W=280, H=150, pad=16)),
   '<div style="font-size:21px">b. Euler’s formula, <i>v</i> + <i>f</i> = <i>e</i> + 2, holds for this graph.<br>i. <b>Complete</b> the formula by writing the appropriate numbers in the boxes provided below. <span class="muted">(1 mark)</span>'
   '<div style="font-size:24px;text-align:center;margin-top:6px">☐ + ☐ = ☐ + 2<br><span style="font-size:16px">&nbsp;<i>v</i>&emsp;&emsp;&nbsp;<i>f</i>&emsp;&emsp;&nbsp;<i>e</i>&emsp;&emsp;&emsp;</span></div></div>'),
  [('Vertices', '<i>v</i> = 5'), ('Edges', '<i>e</i> = 7 (A–B, A–C, B–C, B–D, C–D, C–E, D–E)', 'data-hi="#st|e0,e1,e2,e3,e4,e5,e6|hy"'),
   fx('Faces', '<i>f</i>', F(V('e', '7'), ' + 2 − ', V('v', '5')), '4', 'data-hi="#st||"')],
  '<b>5 + 4 = 7 + 2</b>', 'VCAA 2023 General Mathematics Exam 2 Q12 stem and Q12bi (examiner report: average 0.9/1)', stat=('avg', 90), cmd=('Complete', 1, 'v, f, e in the boxes')))

# ================= APK 1: Cambridge U1&2 checklist #14
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #14', 'Shortest path (Year 11)',
  ('<div style="font-size:24px">For the graph below, find the length of the shortest path from Home to School.</div>', Wd(640, hschool('hs')), ''),
  [('Middle vertex', 'Home → middle: 3 + 5 = 8, 8, or 5 + 2 = <b>7</b>', 'data-hi="#hs|hl,lc|hy"'),
   ('Top vertex', 'middle → top: 7 + 2 = <b>9</b> (direct 3 + 7 = 10)', 'data-hi="#hs|hl,lc,ct|hy"'),
   ('To School', 'over the top: 9 + 4 + 4 = <b>17</b> · along the bottom: 9 + 6 + 2 + 1 = 18, or 5 + 13 + 2 + 1 = 21', 'data-hi="#hs|hl,lc,ct,tm,ms|hy"')],
  'The shortest path from Home to School has length <b>17</b>.', f'{CAM12} · Ch 8 skills checklist #14, p. 542 · answer from the Skills Checklist answers'))
# ================= APK 2: VCAA 2020 E2 Q3a (Edrolo U1&2 7E Q14)
TP = ('<table class="tp"><tr><th>Training program number</th><th>Training details</th></tr><tr><td style="text-align:center">1</td><td>The team must run to exercise station <i>O</i>.</td></tr>'
      '<tr><td style="text-align:center">2</td><td>The team must run along all tracks just once.</td></tr><tr><td style="text-align:center">3</td><td>The team must visit each exercise station and return to exercise station <i>S</i>.</td></tr></table>')
S.append(qslide('apk', 'APK · VCAA 2020 Exam 2 Q3a', 'Shortest distance on a network',
  '<div style="font-size:16px">A local fitness park has 10 exercise stations: <i>M</i> to <i>V</i>.<br>The edges on the graph below represent the tracks between the exercise stations.<br>The number on each edge represents the length, in kilometres, of each track.'
  + Wd(470, fpark('fp')) + 'The Sunny Coast cricket coach designs three different training programs, <b>all starting at exercise station <i>S</i></b>.' + TP
  + 'a. What is the shortest distance, in kilometres, covered in training program 1? <span class="muted">(1 mark)</span></div>',
  [('Over the top', '<i>S</i>–<i>M</i>–<i>O</i>: 1.8 + 1.5 = 3.3', 'data-hi="#fp|sm,mo|hc"'),
   ('Through <i>U</i>, <i>N</i>', '<i>S</i>–<i>T</i>–<i>U</i>–<i>N</i>–<i>O</i>: 0.6 + 1.2 + 0.7 + 0.9 = 3.4', 'data-hi="#fp|st,tu,un,no|hb"'),
   ('Through <i>U</i>, <i>V</i>', '<i>S</i>–<i>T</i>–<i>U</i>–<i>V</i>–<i>O</i>: 0.6 + 1.2 + 0.6 + 0.8 = <b>3.2</b>', 'data-hi="#fp|st,tu,uv,vo|hy"'),
   ('Lower routes', 'via <i>R</i> and <i>Q</i> start with 1.0 + 1.2 = 2.2 already: all longer')],
  'The shortest distance is <b>3.2 km</b> (<i>S</i>–<i>T</i>–<i>U</i>–<i>V</i>–<i>O</i>).',
  f'VCAA 2020 Further Mathematics Exam 2 Networks and decision mathematics Q3 stem and Q3a (examiner report: average 0.6/1) · {EDR12} 7E Q14', stat=('avg', 60)))
sm(extra='sm xs')

# ================= Learn 1: weighted graphs
S.append(learn('Learn · 13D', 'Weighted graphs and networks',
  '<h4>Numbers on the edges</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>weighted graph</b>: each edge carries a number, its <b>weight</b></li><li>weights can be distances, times or costs</li>'
  '<li>when the weights are physical quantities, the weighted graph is a <b>network</b></li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(520, crog('cw')) + '<div style="width:380px">'
  + frag('Vertices = towns, edges = roads, weights = distances (km)')
  + frag('Bartow to Croghon is 12 km', 'data-hi="#cw|bc|hy"') + frag('Bartow → Stratmoore → Osburn: 7 + 9 = 16 km', 'data-hi="#cw|bs,so|hb"') + '</div></div>',
  'The drawing is not to scale: a long edge can have a small weight. Use the numbers, not the picture.',
  f'{CAM}, 13D p. 633 (own words; Cambridge’s network)', cards=(kcard('Weighted graph', 'a weight on every edge'), kcard('Network', 'weights are distance, time or cost'))))
# ================= Learn 2: shortest path by inspection
S.append(learn('Learn · 13D', 'Shortest path by inspection',
  '<h4>List, add, compare</h4><ol style="font-size:19px;line-height:1.5;margin-left:24px"><li>list the sensible routes from start to finish</li>'
  '<li>add the weights along each route</li><li>the smallest total is the <b>shortest path</b>: give its length and its route</li></ol>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(500, trains('il')) + '<div style="width:400px">'
  + frag('Ignore routes that are obviously long (they go the wrong way)') + frag('Watch for a short first step that pays off later', 'data-hi="#il|db|hy"') + '</div></div>',
  'Shortest path = length AND route. Write both: “13 km, D–B–H–E”.',
  f'{CAM}, 13D p. 634 (own words) · {EDR}, 8F p. 585', cards=(kcard('Shortest path', 'smallest total weight'),)))
# ================= Ex 9
S.append(qslide('we', 'Worked example 9 · 13D', 'Finding the shortest path from one vertex to another',
  ('<div style="font-size:24px"><b>Find</b> the shortest path from Bartow to Kenton in the network shown below.</div>', Wd(560, crog('c9')), ''),
  [('List', 'B–S–M–O–K · B–S–M–K · B–S–O–K'), ('Add', 'B–S–M–O–K: 7 + 8 + 5 + 11 = 31 km', 'data-hi="#c9|bs,ms,mo,ok|hc"'),
   ('Add', 'B–S–M–K: 7 + 8 + 13 = 28 km', 'data-hi="#c9|bs,ms,mk|hb"'), ('Add', 'B–S–O–K: 7 + 9 + 11 = 27 km', 'data-hi="#c9|bs,so,ok|hy"')],
  'The shortest path from Bartow to Kenton is <b>27 km</b> with route <b><i>B</i>–<i>S</i>–<i>O</i>–<i>K</i></b>.', f'{CAM} · Example 9 (p. 634)',
  video='Cambridge GO · Example 9 (13D Resources)', cmd=('Find', None, 'length and route')))
S.append(qslide('yt', 'You try · Edrolo 8F WE1', 'Shortest path by inspection',
  ('<div style="font-size:22px">The weighted graph shown displays the distance, in kilometres, between six train stations.<br><b>Find</b> the length and route of the shortest path from Daylington to Eastborough by eye.</div>',
   Wd(560, trains('t1')), ''),
  [('List', 'D–H–E, D–M–E, D–M–T–E, D–B–H–E'), ('D–H–E', '11 + 4 = 15', 'data-hi="#t1|dh,he|hc"'), ('D–M–E', '8 + 10 = 18', 'data-hi="#t1|dm,me|hb"'),
   ('D–M–T–E', '8 + 9 + 7 = 24', 'data-hi="#t1|dm,mt,te|hg"'), ('D–B–H–E', '3 + 6 + 4 = 13', 'data-hi="#t1|db,bh,he|hy"')],
  '<b>13 km</b>, Daylington–Beachmore–Halville–Eastborough.', f'{EDR} · 8F Worked example 1 (p. 585)', cmd=('Find', None, 'length and route')))

# ================= Learn 3: Dijkstra (graphical, Cambridge)
S.append(learn('Learn · 13E', 'Dijkstra’s algorithm',
  '<h4>Grow the shortest paths out from the start</h4><ol style="font-size:17px;line-height:1.4;margin-left:24px">'
  '<li>label the start 0 and circle it</li><li>from the vertex just circled, label each neighbour: circled label + edge weight (keep the smaller if it already has one)</li>'
  '<li>circle the smallest uncircled label</li><li>repeat 2–3 until the destination is circled: its label is the shortest length</li>'
  '<li>backtrack: label − edge weight = the circled vertex before it</li></ol>',
  '<div style="display:flex;gap:20px;align-items:center;justify-content:center">' + Wd(430, etheory('et')) + '<div style="width:440px">'
  + dtable('etb', ['A', 'C', 'B'], ['B', 'C', 'D', 'E'], [['8', '4', 'X', 'X'], ['8', '4', '19', '20'], ['8', '4', '16', '20']], hidden=False, fs=18)
  + frag('Same steps in a table (Edrolo): one row per circled vertex; a box = circled', 'data-hi="#etb|r0_1,r1_1,r1_0,r2_1,r2_0,r2_2|hy"')
  + frag('A to D = 16, route A–B–D', 'data-hi="#et|ab,bd|hy"') + '</div></div>',
  'A circled label never changes. Once the destination is circled, stop: you do not need to label every vertex.',
  f'{CAM}, 13E pp. 637–638 (own words) · {EDR}, 8F pp. 586–587 (table method and its A–E example)',
  cards=(kcard('Update', 'circled label + edge weight'), kcard('Next', 'smallest uncircled label'))))
sm(extra='sm')
# ================= Ex 10 (graphical)
K = lambda *xs: 'data-show="#x10|' + ','.join(xs) + '"'
S.append(qslide('we', 'Worked example 10 · 13E', 'Using Dijkstra’s algorithm: graphical method',
  ('<div style="font-size:24px"><b>Find</b> the shortest path from <i>A</i> to <i>F</i> in the weighted graph shown below.</div>', Wd(560, ex10('x10')), ''),
  [('Step 1', '<i>A</i> = 0, circled', K('lA', 'kA')), ('Step 2', 'from <i>A</i>: <i>B</i> = 2, <i>C</i> = 6 · circle <i>B</i> (2)', K('lB', 'lC6', 'kB')),
   ('Step 3', 'from <i>B</i>: <i>E</i> = 2 + 2 = 4, <i>D</i> = 2 + 3 = 5, <i>C</i> = 2 + 2 = 4 &lt; 6 · circle <i>C</i> (4)', K('lE', 'lD', 'lC6x', 'lC4', 'kC')),
   ('Step 4', 'from <i>C</i>: <i>D</i> = 4 + 1 = 5 (no better) · circle <i>E</i> (4) · from <i>E</i>: <i>F</i> = 4 + 3 = 7 · circle <i>D</i> (5): <i>F</i> = 5 + 5 = 10 &gt; 7 · circle <i>F</i> (7)', K('kE', 'lF', 'kD', 'kF')),
   ('Step 5', 'backtrack: 7 − 3 = 4 (<i>E</i>), 4 − 2 = 2 (<i>B</i>), 2 − 2 = 0 (<i>A</i>)', 'data-hi="#x10|ef,be,ab|hy"')],
  'The shortest path from <i>A</i> to <i>F</i> is <b><i>A</i>–<i>B</i>–<i>E</i>–<i>F</i></b> with a length of <b>7</b>.', f'{CAM} · Example 10 (pp. 638–639)',
  video='Cambridge GO · Example 10 (13E Resources)', cmd=('Find', None, 'length and route')))
sm()
# ================= YT Edrolo WE2 (table)
WV = [['1', 'X', '4', '7', '9'], ['1', '7', '4', '7', '9'], ['1', '5', '4', '6', '9'], ['1', '5', '4', '6', '7'], ['1', '5', '4', '6', '7']]
BOX = [[0], [0, 2], [0, 2, 1], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
def rows_(n): return ','.join(f's{n}_{k}' for k in range(5))
def boxes(upto, extra=()): return ','.join([f'r{i}_{k}' for i in range(upto) for k in BOX[i]] + list(extra))
DT = dtable('wt2', ['G', 'P', 'M', 'B', 'C'], ['P', 'B', 'M', 'C', 'E'], WV, fs=15)
S.append(qslide('yt', 'You try · Edrolo 8F WE2', 'Using Dijkstra’s algorithm: table method',
  '<div style="font-size:16px">Reuben is struggling to f<span></span>ind his way around his new school and is constantly running late. Luckily his friend in General Maths drew him a weighted graph of the school, representing the time it takes, in minutes, to walk to each class.<br>'
  '<b>Find</b> the time and route of the shortest path from General (G) to English (E).</div>' + Wd(470, school('sc')),
  [('TMPL', DT),
   ('Row G', 'edges from G: P 1, M 4, C 7, E 9; B: X', f'data-show="#wt2|{rows_(0)}"'),
   ('Row P', 'box 1 (P) · B = 1 + 6 = 7', f'data-show="#wt2|{rows_(1)}" data-hi="#wt2|{boxes(1)}|hy"'),
   ('Row M', 'box 4 (M) · B = 5, C = 6, E: 9 (no better)', f'data-show="#wt2|{rows_(2)}" data-hi="#wt2|{boxes(2)}|hy"'),
   ('Row B', 'box 5 (B) · E = 5 + 2 = 7', f'data-show="#wt2|{rows_(3)}" data-hi="#wt2|{boxes(3)}|hy"'),
   ('Row C', 'box 6 (C) · E: 9 &gt; 7, keep 7 · box 7', f'data-show="#wt2|{rows_(4)}" data-hi="#wt2|{boxes(5)}|hy"'),
   ('Route', 'back up: E 7 (row B) → B 5 (row M) → M 4 (row G)', 'data-hi="#sc|gm,mb,eb|hy"')],
  '<b>7 minutes</b>, General–Methods–Biology–English.', f'{EDR} · 8F Worked example 2 (pp. 588–589)', cmd=('Find', None, 'time and route')))
sm(extra='sm xs')

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 2 · VCAA 2018 Exam 1 Q2', 'Show what you know',
  ('<div style="font-size:20px">Niko drives from his home to university.<br>The network below shows the distances, in kilometres, along a series of streets connecting Niko’s home to the university.<br>'
   'The vertices <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i> represent the intersection of these streets.</div>', Wd(470, niko('nk')),
   '<div style="font-size:20px">The shortest path for Niko from his home to the university could be found using</div>'),
  [('Which tool?', 'shortest path between two vertices on a weighted graph → Dijkstra’s algorithm')],
  '<b>C</b>: Dijkstra’s algorithm.', f'VCAA 2018 Further Mathematics Exam 1 Networks and decision mathematics Q2 (examiner report: 68% correct) · {EDR} 8F Q10 (adapted there)',
  mc=['a minimum cut.', 'Prim’s algorithm.', 'Dijkstra’s algorithm.', 'critical path analysis.', 'the Hungarian algorithm.'], key='C', stat=('mc', 68), dist=[5, 10, 68, 15, 2],
  dis=('D', 'critical path analysis finds the longest path through a project network, not the shortest route between two places.')))
sm()
S.append(qslide('ex', 'Exit task 2 of 2 · VCAA 2017 Exam 2 Q1b', 'Show what you know',
  '<div style="font-size:18px">Bus routes connect six towns.<br>The towns are Northend (<i>N</i>), Opera (<i>O</i>), Palmer (<i>P</i>), Quigley (<i>Q</i>), Rosebush (<i>R</i>) and Seatown (<i>S</i>).<br>'
  'The graph below gives the cost, in dollars, of bus travel along these routes.<br>Bai lives in Northend (<i>N</i>) and he will travel by bus to take a holiday in Seatown (<i>S</i>).'
  + Wd(470, bus('bu')) + 'b. If Bai takes the cheapest route from Northend (<i>N</i>) to Seatown (<i>S</i>), which other town(s) will he pass through? <span class="muted">(1 mark)</span></div>',
  [('Via <i>O</i>', 'N–O–S: 15 + 105 = $120 · N–O–P–R–S: 15 + 20 + 40 + 30 = $105', 'data-hi="#bu|no,os|hc"'),
   ('Via <i>P</i>', 'N–P–R–S: 30 + 40 + 30 = $100', 'data-hi="#bu|np,pr,rs|hb"'),
   ('Via <i>Q</i>', 'N–Q–S: 30 + 60 = $90 · N–Q–R–S: 30 + 20 + 30 = <b>$80</b>', 'data-hi="#bu|nq,qr,rs|hy"')],
  'Cheapest route N–Q–R–S ($80): he passes through <b>Quigley (<i>Q</i>) and Rosebush (<i>R</i>)</b>.',
  f'VCAA 2017 Further Mathematics Exam 2 Networks and decision mathematics Q1 stem and Q1b (examiner report: average 0.8/1) · {EDR} 8F Q11', stat=('avg', 80)))
sm()

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 13 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] in ('13D', '13E') and v.get('url')]))
n = assemble(S, '12MAG · 13D–13E · Shortest paths and Dijkstra’s algorithm', os.path.join(ROOT, 'lessons', '13D-13E slides.html'))
print(n - 1, 'slides')
