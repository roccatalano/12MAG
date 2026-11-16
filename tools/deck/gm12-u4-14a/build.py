"""Lesson gm12-u4-14a (14A Flow problems) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/14A slides.html      Run: python3 tools/deck/gm12-u4-14a/build.py      Screenshots: python3 tools/deck/gm12-u4-14a/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; figures cropped from the PDFs, fig/*.png):
- Do Now: VCAA 2023 Exam 1 Q33 (D, 56%) · VCAA 2024 Exam 1 Q9 stem + Q9 (A, 52%) · VCAA 2025 Exam 2 Q15 stem + Q15d (average 0.8/1; graph redrawn as in 13F) ·
          VCAA 2024 Exam 2 Q1 stem + Q1c (average 1.7/2; Table 1 as in l07).
- APK: Cambridge U1&2 Ch 8 skills checklist #1 (p. 540; answer worked out: no printed answer) ·
       VCAA 2016 Exam 2 N&DM Q1a, Q1bi (= Edrolo U1&2 7A Q14, p. 372; 83%, 53%; answers from Edrolo U1&2 answers).
- Learn: Cambridge U3&4 14A pp. 660-664 (own words) · Edrolo U3&4 8E pp. 573-576.
- Worked examples: Cambridge U3&4 Examples 1 (p. 662), 2 (p. 664), 3 (pp. 664-665), 4 (pp. 665-668), 5 (pp. 668-669).
  You trys: Edrolo U3&4 8E Worked examples 1 (p. 574), 2 (p. 575), 3 (pp. 576-577); YT-14A-4 and YT-14A-5 written for 12MAG
  (planner/written-youtrys.json; no Edrolo match; answers checked with networkx).
- No CAS (Cambridge prints none for 14A).
- Exits: VCAA 2016 Exam 1 N&DM Q2 (= Edrolo 8E Q14; C, 54%) · VCAA 2020 Exam 2 N&DM Q4b,c (= Edrolo 8E Q15; 69%, 32%; 52, 50) ·
         VCAA 2017 Exam 1 N&DM Q8 (= Edrolo 8E Q16; B, 44%). Answers: Edrolo U3&4 answers p. 731.
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
import importlib.util
def _mod(n, p):
    s = importlib.util.spec_from_file_location(n, os.path.join(H, '..', p)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
F13F = _mod('f13f', 'gm12-u4-13f/figs.py'); F07 = _mod('f07', 'l07/figs.py'); F04 = _mod('f04', 'l04/figs.py')
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-14a')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'
def HI(sid, ids, c='hc'): return f'data-hi="#{sid}|{",".join(ids)}|{c}"'
WR = 'Written for 12MAG (no Edrolo worked example matches; modelled on Cambridge Example {}): planner/written-youtrys.json'

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight .L .q ol.parts li,.tight .L .q ol.parts li span{font-size:16px!important;line-height:1.3!important;padding:2px 0!important}</style>']
S.append(title('14A', 'Flow problems', f'{CAM} · 14A Flow problems', 'gm12-u4-14a'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 14A', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>14A')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· two Year 11 questions', 'var(--apk)'),
  ('Directed graphs and flow', '', None), ('Worked example 1', '→ You try', None), ('Cuts and cut capacity', '', None), ('Worked examples 2–3', '→ You try', None),
  ('Tracking flow', '', None), ('Worked examples 4–5', '→ You try', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'),
  ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Directed graph', 'a graph whose edges have arrows: travel one way only'), ('Source / sink', 'where the flow starts / where it ends'),
  ('Capacity', 'the weight on an edge: the most that can flow along it'), ('Cut', 'a line that completely separates the source from the sink'),
  ('Cut capacity', 'sum of the cut edges flowing source side → sink side'), ('Minimum cut', 'the cut with the smallest capacity')],
  [('Edges in a row', 'flow = smallest capacity', 'e.g. 300 then 600 then 800 → 300'), ('Cut capacity', 'add only edges going source → sink', 'edges flowing back count 0'),
   ('Max-flow min-cut', 'maximum flow = minimum cut capacity', 'check every cut')],
  f'{CAM}, 14A pp. 660–664; {EDR}, 8E pp. 573–576; Study Design: use of networks to model flow problems: capacity, sinks and sources; the ‘maximum-flow minimum-cut’ theorem'))

# ================= Do Now
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2023 Exam 1 Q33', 'Review of 13A–13F (graph words)',
  ('<div style="font-size:21px">Consider the following graph.</div>', Wd(240, img('q33.png')),
   '<div style="font-size:19px">How many of the following five statements are true?<ul style="margin-left:24px"><li>The graph is a tree.</li><li>The graph is connected.</li>'
   '<li>The graph contains a path.</li><li>The graph contains a cycle.</li><li>The sum of the degrees of the vertices is eight.</li></ul></div>'),
  [('Tree?', '5 vertices, 4 edges, no cycle: <b>true</b>'), ('Connected? Path?', 'every vertex is joined: <b>true</b> · any walk with no repeats is a path: <b>true</b>'),
   ('Cycle?', 'a tree has no cycle: <b>false</b>'), ('Degrees', '2 × 4 edges = 8: <b>true</b>')],
  'Four statements are true: <b>D</b>.', 'VCAA 2023 General Mathematics Exam 1 Q33 (examiner report: 56% correct)', mc=['1', '2', '3', '4', '5'], key='D', stat=('mc', 56)))
sm()
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2024 Exam 1 Q9', 'Review of 3A (r from the slope)',
  '<div style="font-size:20px">The least squares equation for the relationship between the average number of male athletes per competing nation, <i>males</i>, and the number of the Summer Olympic Games, <i>number</i>, is'
  '<div style="text-align:center;margin:6px"><i>males</i> = 67.5 − 1.27 × <i>number</i></div>The summary statistics for the variables <i>number</i> and <i>males</i> are shown in the table below.'
  '<table class="t tight" style="margin:6px auto;font-size:18px"><tr><th></th><th><i>number</i></th><th><i>males</i></th></tr><tr><td>mean</td><td>15.0</td><td>48.4</td></tr>'
  '<tr><td>standard deviation</td><td>8.51</td><td>19.0</td></tr></table>'
  'The value of Pearson’s correlation coefficient, <i>r</i>, rounded to three decimal places, is closest to</div>',
  [fx('Slope rule', '<i>r</i>', F(V('b', '−1.27'), ' × ', V('s<sub>x</sub>', '8.51'), ' ÷ ', V('s<sub>y</sub>', '19.0')), '−0.569'),
   ('Sign', 'negative slope, so <i>r</i> is negative')],
  '<i>r</i> ≈ −0.569: <b>A</b>.', 'VCAA 2024 General Mathematics Exam 1 Q9 (examiner report: 52% correct)', mc=['−0.569', '−0.394', '0.394', '0.569'], key='A', stat=('mc', 52),
  dis=('B', '−0.394 comes from multiplying by 19.0 and dividing by 8.51: the standard deviations the wrong way round.')))
sm()
FT = ['cg', 'cs', 'ch', 'cp']
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2025 Exam 2 Q15d', 'Review of 13F (spanning trees)',
  ('<div style="font-size:21px">Frances lives in a housing estate.<br>On the graph below the vertices represent her favourite locations, and the edges represent the roads between them.</div>',
   Wd(420, F13F.frances('fr')), '<div style="font-size:21px">d. Using edges from the original graph, <b>construct</b> a spanning tree below. <span class="muted">(1 mark)</span></div>'),
  [('Count', '5 vertices, so the tree has 5 − 1 = 4 edges'), ('Choose', 'keep 4 edges that reach every vertex with no cycle', HI('fr', FT, 'hy'))],
  'One spanning tree: coffee shop joined to gym, supermarket, home and pet shop (other answers possible).', 'VCAA 2025 General Mathematics Exam 2 Q15 stem and Q15d (examiner report: average 0.8/1)',
  stat=('avg', 80), cmd=('construct', 1, '4 edges, every vertex, no cycle')))
MG = sorted(m for _, m in F07.MGOLD)
BP = F04.pbox([('', (1.94, 2.12, 2.29, 2.36, 2.39), [])], 1.90, 2.40, 0.05, 'Mgold (m)', W=520, rowH=46, fs=14, lab=20)
MT = ('<table class="t tight" style="font-size:13px"><tr><th><i>year</i></th>' + ''.join(f'<td>{y}</td>' for y, _ in F07.MGOLD[:11]) + '</tr><tr><th><i>Mgold</i> (m)</th>'
      + ''.join(f'<td>{m:.2f}</td>' for _, m in F07.MGOLD[:11]) + '</tr><tr><th><i>year</i></th>' + ''.join(f'<td>{y}</td>' for y, _ in F07.MGOLD[11:])
      + '</tr><tr><th><i>Mgold</i> (m)</th>' + ''.join(f'<td>{m:.2f}</td>' for _, m in F07.MGOLD[11:]) + '</tr></table>')
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2024 Exam 2 Q1c', 'Review of 1G (boxplots)',
  '<div style="font-size:15px">Table 1 lists the Olympic year, <em class="v">year</em>, and the gold medal-winning height for the men’s high jump, <em class="v">Mgold</em>, in metres, for each Olympic Games held from 1928 to 2020. '
  'No Olympic Games were held in 1940 or 1944, and the 2020 Olympic Games were held in 2021.<div style="font-weight:700;margin-top:6px">Table 1</div>' + MT
  + '<div style="font-size:18px;margin-top:8px">c. <b>Construct</b> a boxplot for the <em class="v">Mgold</em> data in Table 1 on the grid below. <span class="muted">(2 marks)</span></div></div>',
  [('CAS', 'one-variable stats on the 22 values: min 1.94, Q<sub>1</sub> 2.12, median 2.29, Q<sub>3</sub> 2.36, max 2.39'),
   fx('IQR', 'IQR', F(V('Q<sub>3</sub>', '2.36'), ' − ', V('Q<sub>1</sub>', '2.12')), '0.24'),
   ('Fences', 'LF = 2.12 − 1.5 × 0.24 = 1.76 · UF = 2.36 + 0.36 = 2.72: 1.94 > 1.76 and 2.39 < 2.72 → no outliers')],
  Wd(440, BP), 'VCAA 2024 General Mathematics Exam 2 Q1 stem and Q1c (examiner report: average 1.7/2)', stat=('avg', 85), cmd=('Construct', 2, 'five-number summary, check outliers')))
sm(extra='sm xs')

# ================= APK
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #1', 'Vertices, edges and loops (Year 11)',
  ('<div style="font-size:22px"><b>Identify</b> the number of vertices, edges and loops in the graph below.</div>', Wd(300, img('apk1.png')), ''),
  [('Vertices', '<i>A</i>, <i>B</i>, <i>C</i>, <i>D</i>, <i>E</i>: 5'), ('Edges', '<i>AB</i>, <i>AE</i>, <i>BE</i>, <i>BD</i>, <i>ED</i>, <i>DC</i> + 2 loops: 8 (a loop is an edge)'),
   ('Loops', 'at <i>C</i> and at <i>E</i>: 2')],
  '<b>5</b> vertices, <b>8</b> edges, <b>2</b> loops.', f'{CAM12} · Ch 8 skills checklist #1, p. 540 · answer worked out (no printed answer)', cmd=('Identify', None, 'three counts')))
S.append(qslide('apk', 'APK · VCAA 2016 Exam 2 Q1a, Q1bi', 'Graphs from maps (Year 11)',
  '<div style="font-size:17px">A map of the roads connecting five suburbs of a city, Alooma (A), Beachton (B), Campville (C), Dovenest (D) and Easyside (E), is shown.'
  '<div style="display:flex;gap:14px;align-items:center;justify-content:center">' + Wd(230, img('apk2map.png')) + Wd(220, img('apk2g.png')) + '</div>'
  + plist([('a.', 'Starting at Beachton, which two suburbs can be driven to using only one road? <span class="muted">(1 mark)</span>'),
           ('b.', 'A graph that represents the map of the roads is shown (right). One of the edges that connects to vertex E is missing from the graph.<br>Add the missing edge to the graph. <span class="muted">(1 mark)</span>')]) + '</div>',
  [('Map', 'two roads leave Beachton: one to Alooma, one down to Easyside'), ('Compare', 'the graph has only A–B at B: the road B–E is missing')],
  '', f'VCAA 2016 Further Mathematics Exam 2 Networks and decision mathematics Q1a, Q1bi (examiner report: 83%, 53%) · {EDR12} 7A Q14',
  stat=('avg', 53), parts=[('a.', '<b>Alooma and Easyside</b>'), ('b.', 'draw the edge <b>B–E</b>')]))
sm(extra='sm xs')

# ================= Learn 1: directed graphs and flow
S.append(learn('Learn · 14A', 'Directed graphs and flow',
  '<h4>Flow goes one way</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a <b>directed graph</b> (digraph) has arrows: you can only travel the way they point</li><li>material flows from the <b>source</b> to the <b>sink</b></li>'
  '<li>the weight on each edge is its <b>capacity</b></li><li>pipes in a row: the flow is the <b>smallest</b> capacity (the bottleneck)</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(400, img('ex1.png')) + '<div style="width:360px">'
  + frag('A → B → C → E: 300, 600, 800') + frag('Bottleneck 300: only 300 cars per hour get through') + frag('Separate routes add up') + '</div></div>',
  'Follow the arrows: an edge pointing the wrong way cannot be used.', f'{CAM}, 14A pp. 660–661 (own words; Cambridge’s Example 1 network) · {EDR}, 8E p. 573',
  cards=(kcard('Capacity', 'most that can flow'), kcard('Edges in a row', 'flow = smallest capacity'))))
S.append(qslide('we', 'Worked example 1 · 14A', 'Calculating the maximum flow',
  '<div style="font-size:17px">In the digraph shown on the right, the vertices <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i> represent towns. The edges of the graph represent roads and the weights of those edges are the maximum number of cars that can travel on the road each hour. The roads allow only one-way travel.'
  + Wd(380, img('ex1.png')) + plist([('a', '<b>Find</b> the maximum traffic flow from <i>A</i> to <i>E</i> through town <i>C</i>.'), ('b', '<b>Find</b> the maximum traffic flow from <i>A</i> to <i>E</i> overall.'),
    ('c', 'A new road is being built to allow traffic from town <i>D</i> to town <i>C</i>. This road can carry 500 cars per hour.<br>i Add this road to the digraph.<br>ii <b>Find</b> the maximum traffic flow from <i>A</i> to <i>E</i> overall after this road is built.')]) + '</div>',
  [('Through C', 'A–B–C–E: smallest of 300, 600, 800 = 300'), ('Through D', 'A–D–E: smallest of 500, 150 = 150'),
   ('New road', 'A–D–C–E carries 500 more: C–E (800) has room for 300 + 500')],
  '', f'{CAM} · Example 1 (p. 662)', video='Cambridge GO · Example 1 (14A Resources)', cmd=('Find', None, 'the bottleneck on each route'), afig=Wd(300, img('ex1c.png')),
  parts=[('a', '<b>300</b> cars per hour'), ('b', '300 + 150 = <b>450</b> cars per hour'), ('c', 'i an arrow from D to C labelled 500 · ii <b>800</b> cars per hour')]))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8E WE1', 'Navigating directed graphs',
  '<div style="font-size:19px">For the following directed graphs, <b>determine</b> if it is possible to travel from vertex A to vertex D. If so, identify a route and calculate the weight of the route.'
  '<div style="display:flex;gap:16px;justify-content:center;align-items:flex-start"><div>a.' + Wd(280, img('we1a.png')) + '</div><div>b.' + Wd(300, img('we1b.png')) + '</div></div></div>',
  [('a. From A', 'A → C is a dead end (C only leads back) · A → E → B → D works'), ('a. Weight', '4 + 7 + 5 = 16'),
   ('b. From A', 'A → B: dead end · A → G → E: E is a dead end, so D cannot be reached')],
  '', f'{EDR} · 8E Worked example 1 (p. 574)', cmd=('determine', None, 'follow the arrows'),
  parts=[('a', 'Yes: A–E–B–D, weight <b>16</b>'), ('b', '<b>No</b>')]))
sm()

# ================= Learn 2: cuts
S.append(learn('Learn · 14A', 'Cuts and the maximum-flow minimum-cut theorem',
  '<h4>Block every route</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a <b>cut</b> separates the source from the sink completely</li><li><b>cut capacity</b> = sum of the cut edges that flow from the source side to the sink side</li>'
  '<li>an edge flowing back (sink side → source side) counts 0</li><li><b>maximum flow = capacity of the minimum cut</b></li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(420, img('ex2.png')) + '<div style="width:340px">'
  + frag('<i>C</i><sub>1</sub>: 15 + 20') + frag('<i>C</i><sub>2</sub>: <i>F</i> → <i>B</i> flows back: not counted') + frag('Smallest cut = the bottleneck of the whole network') + '</div></div>',
  'Check each arrow a cut crosses: does it point towards the sink?', f'{CAM}, 14A pp. 663–664 (own words) · {EDR}, 8E pp. 575–576',
  cards=(kcard('Cut capacity', 'source → sink edges only'), kcard('Max-flow min-cut', 'max flow = min cut'))))
S.append(qslide('we', 'Worked example 2 · 14A', 'Calculating cut capacity',
  ('<div style="font-size:22px"><b>Calculate</b> the capacity of the four cuts shown in the network on the right. The source is vertex <i>S</i> and the sink is vertex <i>T</i>.</div>', Wd(520, img('ex2.png')), ''),
  [('<i>C</i><sub>1</sub>', 'both edges counted: 15 + 20'), ('<i>C</i><sub>2</sub>', 'F → B flows back: 14 + 20'), ('<i>C</i><sub>3</sub>', 'all counted: 14 + 15 + 20'),
   ('<i>C</i><sub>4</sub>', 'D → C flows back: 20 + 10')],
  '', f'{CAM} · Example 2 (p. 664)', video='Cambridge GO · Example 2 (14A Resources)', cmd=('Calculate', None, 'only source → sink edges'),
  parts=[('<i>C</i><sub>1</sub>', '<b>35</b>'), ('<i>C</i><sub>2</sub>', '<b>34</b>'), ('<i>C</i><sub>3</sub>', '<b>49</b>'), ('<i>C</i><sub>4</sub>', '<b>30</b>')]))
S.append(qslide('yt', 'You try · Edrolo 8E WE2', 'Calculating cut capacity',
  ('<div style="font-size:22px"><b>Calculate</b> the capacity of each cut in the following network.</div>', Wd(520, img('we2.png')), ''),
  [('Check direction', 'the edge with weight 12 in cut 1 flows from the sink side to the source side: not counted'), ('Cut 1', '8 + 15'), ('Cut 2', '7 + 6 + 4 + 18'), ('Cut 3', '8 + 3 + 18')],
  '', f'{EDR} · 8E Worked example 2 (p. 575)', cmd=('Calculate', None, 'only source → sink edges'),
  parts=[('Cut 1', '<b>23</b>'), ('Cut 2', '<b>35</b>'), ('Cut 3', '<b>29</b>')]))
S.append(qslide('we', 'Worked example 3 · 14A', 'Calculating maximum flow using cuts',
  ('<div style="font-size:22px"><b>Determine</b> the maximum flow from <i>S</i> to <i>T</i> for the digraph shown on the right.</div>', Wd(440, img('ex3.png')), ''),
  [('Mark the cuts', 'six cuts that separate S from T (picture)'), ('<i>C</i><sub>1</sub>–<i>C</i><sub>3</sub>', '8 + 11 = 19 · 3 + 11 = 14 · 3 + 5 + 11 = 19'),
   ('<i>C</i><sub>4</sub>–<i>C</i><sub>6</sub>', '8 + 3 + 1 = 12 · 3 + 3 + 1 = 7 · 3 + 5 + 1 = 9'), ('Smallest', '<i>C</i><sub>5</sub> = 7')],
  'The minimum cut capacity is 7, so the maximum flow from S to T is <b>7</b>.', f'{CAM} · Example 3 (pp. 664–665)', video='Cambridge GO · Example 3 (14A Resources)',
  made=Wd(330, img('ex3cuts.png')), cmd=('Determine', None, 'find the minimum cut')))
sm()
S.append(qslide('yt', 'You try · Edrolo 8E WE3', 'Determining the maximum flow',
  ('<div style="font-size:21px">The following network shows the number of cars that can travel between five different towns each second.</div>', Wd(440, img('we3.png')),
   '<div style="font-size:21px">What is the maximum number of cars that can travel from town A to town E each second?</div>'),
  [('Mark the cuts', 'seven possible cuts (picture)'), ('Cuts 1–4', '6 + 4 = 10 · 10 + 7 + 4 = 21 · 10 + 11 + 4 = 25 · 10 + 7 + 3 = 20 (C → D not counted)'),
   ('Cuts 5–7', '6 + 3 = 9 · 6 + 3 = 9 · 10 + 3 = 13'), ('Smallest', 'cuts 5 and 6: 9')],
  'The maximum flow is <b>9 cars</b> per second.', f'{EDR} · 8E Worked example 3 (pp. 576–577)', made=Wd(330, img('we3cuts.png'))))
sm()

# ================= Learn 3: tracking flow, more than one source
S.append(learn('Learn · 14A', 'Tracking flow and more than one source',
  '<h4>Push the flow through</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>edges leaving the source run full</li><li>at each vertex: flow out ≤ flow in; cross out a capacity that can’t be reached and write the real flow</li>'
  '<li>maximum flow = total arriving at the sink</li><li>two sources / outlets: look at each outlet on its own (cut off that outlet)</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(420, img('ex4.png')) + '<div style="width:340px">'
  + frag('B gets 15: 10 to C, only 5 left for D') + frag('A group must fit every edge on its route') + '</div></div>',
  'Use a minimum cut to check a tracked answer: they must agree.', f'{CAM}, 14A pp. 665–669 (own words)',
  cards=(kcard('Max-flow min-cut', 'max flow = min cut'),)))
S.append(qslide('we', 'Worked example 4 · 14A', 'Calculating maximum flow',
  '<div style="font-size:14px">The koala sanctuary in Cowes allows visitors to walk through their park. The park is represented by a network below, where each edge represents one-way tracks for visitors through the park. The direction of travel on each track is shown by an arrow. The numbers on the edges indicate the maximum number of people who are permitted to walk along each track each hour.'
  + Wd(320, img('ex4.png')) + plist([('a', 'Starting at <i>A</i>, how many people are permitted to walk to <i>G</i> each hour?'),
    ('b', 'Given that one group of nine people would like to walk from <i>A</i> to <i>G</i> together as a group, <b>list</b> all the different routes they could take so that the entire group of nine will stay together for the duration of their walk.'),
    ('c', 'What is the largest group of people that could walk through the koala sanctuary if they must stay together in a group for the entire duration of the walk?')]) + '</div>',
  [('From A', 'A → B 15, A → D 20, A → E 8 run full'), ('B', '10 to C (then 10 C → G), 5 left for B → D'), ('E, D', 'E → F 8 · D gets 25: 9 to G, 13 to F'),
   ('Into G', 'F → G gets 8 + 13 = 21: 10 + 9 + 21 = 40'), ('Group of 9', 'every edge on the route ≥ 9'), ('Largest group', '20 into D, but only 13 can leave D together')],
  '', f'{CAM} · Example 4 (pp. 665–668)', video='Cambridge GO · Example 4 (14A Resources)', cmd=('list', None, 'routes with every edge ≥ 9'),
  parts=[('a', '<b>40</b> people per hour'), ('b', 'A–B–C–G, A–D–G, A–D–F–G'), ('c', '<b>13</b> people (A–D–F–G)')]))
sm(extra='sm xs tight')
S.append(qslide('yt', 'You try · written for 12MAG (YT-14A-4)', 'Calculating maximum flow',
  '<div style="font-size:14px">A wildlife park allows visitors to walk through the park along one-way tracks. The park is represented by the network below, where the direction of travel on each track is shown by an arrow. The numbers on the edges indicate the maximum number of people who are permitted to walk along each track each hour.'
  + Wd(320, yt4('y4')) + plist([('a', 'Starting at <i>A</i>, how many people are permitted to walk to <i>G</i> each hour?'),
    ('b', 'Given that one group of eight people would like to walk from <i>A</i> to <i>G</i> together as a group, <b>list</b> all the different routes they could take so that the entire group of eight will stay together for the duration of their walk.'),
    ('c', 'What is the largest group of people that could walk through the wildlife park if they must stay together in a group for the entire duration of the walk?')]) + '</div>',
  [('Minimum cut', 'cut C → G, D → G, D → F and A → E', HI('y4', Y4_CUT, 'hy')), ('Capacity', '11 + 10 + 8 + 7 = 36'),
   ('Group of 8', 'A–B–C–G (smallest 9), A–D–G (10), A–D–F–G (8)'), ('Largest group', 'best bottleneck: A–D–G = 10')],
  '', WR.format(4), cmd=('list', None, 'routes with every edge ≥ 8'),
  parts=[('a', '<b>36</b> people per hour'), ('b', 'A–B–C–G, A–D–G, A–D–F–G'), ('c', '<b>10</b> people (A–D–G)')]))
sm(extra='sm xs tight')
S.append(qslide('we', 'Worked example 5 · 14A', 'Calculating maximum flow from more than one source',
  ('<div style="font-size:18px">Water enters a network of pipes at either Source 1 or Source 2 and flows out at either Outlet 1 or Outlet 2.<br>The numbers next to the arrows represent the maximum rate, in kilolitres per minute, at which water can flow through each pipe.</div>',
   Wd(460, img('ex5.png')), '<div style="font-size:18px"><b>Determine</b> the maximum rate, in kilolitres per minute, at which water can flow from these pipes into the ocean at Outlet 1 and Outlet 2.</div>'),
  [('Outlet 1', 'cuts 400 + 800 = 1200 · 400 + 300 = 700 · 400 + 400 = 800 · 300 + 100 + 300 = 700 · 300 + 400 = 700'),
   ('Outlet 2', 'cuts 700, 900, 900, 800, 900, 900 (the 200 pipe towards Outlet 2 must be cut)'), ('Careful', 'the two maximums may not happen at the same time: don’t just add them')],
  'Outlet 1: <b>700</b> kL/min · Outlet 2: <b>700</b> kL/min.', f'{CAM} · Example 5 (pp. 668–669)', video='Cambridge GO · Example 5 (14A Resources)',
  cmd=('Determine', None, 'one outlet at a time')))
sm()
S.append(qslide('yt', 'You try · written for 12MAG (YT-14A-5)', 'Maximum flow from more than one source',
  ('<div style="font-size:19px">Water enters a network of pipes at either Source 1 or Source 2 and flows out at either Outlet 1 or Outlet 2.<br>The numbers next to the arrows represent the maximum rate, in kilolitres per minute, at which water can flow through each pipe.</div>',
   Wd(440, yt5('y5')), '<div style="font-size:19px"><b>Determine</b> the maximum rate, in kilolitres per minute, at which water can flow from these pipes at Outlet 1 and at Outlet 2.</div>'),
  [('Outlet 1', 'cut the two pipes into Outlet 1: 350 + 250 = 600', HI('y5', ['po', 'qo'], 'hy')), ('Outlet 2', 'cut the two pipes into Outlet 2: 200 + 450 = 650', HI('y5', ['qp', 'ro'], 'hy')),
   ('Check', 'enough water reaches P, Q and R to fill those pipes')],
  'Outlet 1: <b>600</b> kL/min · Outlet 2: <b>650</b> kL/min.', WR.format(5), cmd=('Determine', None, 'one outlet at a time')))
sm()

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2016 Exam 1 Q2', 'Show what you know',
  ('<div style="font-size:22px">The following directed graph shows the flow of water, in litres per minute, in a system of pipes connecting the source to the sink.</div>', Wd(440, img('q14.png')),
   '<div style="font-size:22px">The maximum flow, in litres per minute, from the source to the sink is</div>'),
  [('Cuts', '4 + 10 + 6 = 20 · 2 + 10 + 6 = 18 · 4 + 10 + 8 = 22 · 2 + 10 + 8 = 20'), ('Minimum', '18')],
  '18 L/min: <b>C</b>.', f'VCAA 2016 Further Mathematics Exam 1 Networks and decision mathematics Q2 (examiner report: 54% correct) · {EDR} 8E Q14',
  mc=['10', '14', '18', '20', '22'], key='C', stat=('mc', 54)))
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2020 Exam 2 Q4b, c', 'Show what you know',
  '<div style="font-size:15px">A training program has a cricket team starting from exercise station S and running to exercise station O.<br>For safety reasons, the cricket coach has placed a restriction on the maximum number of people who can use the tracks in the fitness park.<br>'
  'The directed graph shows the capacity of the tracks, in number of people per minute.' + Wd(470, img('q15.png'))
  + 'When considering the possible flow of people through this network, many different cuts can be made.'
  + plist([('b.', '<b>Determine</b> the capacity of cut 1. <span class="muted">(1 mark)</span>'), ('c.', 'What is the maximum flow from S to O, in number of people per minute? <span class="muted">(1 mark)</span>')]) + '</div>',
  [('Cut 1', 'edges flowing from the S side to the O side: 20 + 12 + 20'), ('Max flow', 'minimum cut (cut B): S–M 20, T–U 10, R–Q 20 → 20 + 10 + 20 = 50')],
  '', f'VCAA 2020 Further Mathematics Exam 2 Networks and decision mathematics Q4b, Q4c (examiner report: 69%, 32%) · {EDR} 8E Q15',
  stat=('avg', 32), cmd=('Determine', 1, 'only source → sink edges'), afig=Wd(300, img('q15cuts.png')),
  parts=[('b.', '<b>52</b> people per minute'), ('c.', '<b>50</b> people per minute')]))
sm(extra='sm xs')
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2017 Exam 1 Q8', 'Show what you know',
  '<div style="font-size:17px">The flow of oil through a series of pipelines, in litres per minute, is shown in the following network.' + Wd(520, img('q16.png'))
  + 'The weightings of three of the edges are labelled <i>x</i>.<br>Five cuts labelled A–E are shown on the network.<br>The maximum flow of oil from the source to the sink, in litres per minute, is given by the capacity of</div>',
  [('Cuts', 'A: 25 + <i>x</i> · B: 23 + <i>x</i> · C: 24 + <i>x</i> · D: 32 · E: 27'), ('Eliminate', 'B is always below A and C; E is below D'),
   ('Try', '<i>x</i> = 2: B = 25 < 27 · <i>x</i> = 3: B = 26 < 27: cut B is the minimum')],
  '<b>B</b>: cut B if <i>x</i> = 2.', f'VCAA 2017 Further Mathematics Exam 1 Networks and decision mathematics Q8 (examiner report: 44% correct) · {EDR} 8E Q16',
  mc=['cut A if <i>x</i> = 1', 'cut B if <i>x</i> = 2', 'cut C if <i>x</i> = 2', 'cut D if <i>x</i> = 3', 'cut E if <i>x</i> = 3'], key='B', stat=('mc', 44),
  dis=('D', 'cut D has the greatest capacity: the maximum flow is the SMALLEST cut, not the largest.')))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 14 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '14A' and v.get('url')]))
n = assemble(S, '12MAG · 14A · Flow problems', os.path.join(ROOT, 'lessons', '14A slides.html'))
print(n - 1, 'slides')
