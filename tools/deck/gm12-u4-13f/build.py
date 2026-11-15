"""Lesson gm12-u4-13f (13F Trees and minimum connector problems) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/13F slides.html      Run: python3 tools/deck/gm12-u4-13f/build.py      Screenshots: python3 tools/deck/gm12-u4-13f/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; graphs redrawn with tools/deck/tpl/net.py, same vertices, edges and weights):
- Do Now: VCAA 2024 Exam 1 Q34 (C, 85%) · VCAA 2025 Exam 1 Q38 (A, 47%) · VCAA 2025 Exam 2 Q15 stem + Q15b (average 0.9/1) ·
          VCAA 2026 NHT Exam 2 Q4 stem + Q4c (sunspot plot cropped from the paper; answer 420 worked out; NHT reports give no %).
- APK: Cambridge U1&2 Ch 8 skills checklist #15 (p. 542; uses the #14 Home/School graph; answer 23 worked out with Prim's: no printed answer found) ·
       VCAA 2017 Exam 2 N&DM Q3 stem + Q3a i-ii in the original wording (= Edrolo U1&2 7F Q18 = Edrolo U3&4 8D Q13; card: 53%).
- Learn: Cambridge U3&4 13F pp. 640-644 (own words; Cambridge's seven-vertex tree) · Edrolo U3&4 8D pp. 563-564 (Prim's steps).
- Worked examples: Cambridge U3&4 Examples 11 (pp. 641-642), 12 (pp. 643-644), 13 (pp. 644-645).
  You trys: Edrolo U3&4 8D Worked example 1 (p. 563), Worked example 2 (pp. 564-565), Edrolo U1&2 7F Worked example 2 (pp. 419-420).
- No CAS (Cambridge prints none for 13F).
- Exits: VCAA 2018 Exam 1 N&DM Q1 (= Edrolo 8D Q11; B, 92%) · VCAA 2020 Exam 1 N&DM Q3 (= Edrolo 8D Q12; B, 81%).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
import importlib.util
_s = importlib.util.spec_from_file_location('f13d', os.path.join(H, '..', 'gm12-u4-13d13e', 'figs.py')); F13D = importlib.util.module_from_spec(_s); _s.loader.exec_module(F13D)
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-13f')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'
def HI(sid, ids, c='hc'): return f'data-hi="#{sid}|{",".join(ids)}|{c}"'
def prim(sid, order):
    """cumulative highlight attrs for Prim steps: order = [edge ids in the order chosen]"""
    return [HI(sid, order[:k + 1]) for k in range(len(order))]

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}'
     '.opts{display:grid;grid-template-columns:repeat(3,1fr);gap:4px 10px}.opts>div{display:flex;align-items:flex-start;gap:4px}.opts b{font-size:18px}</style>']
# ================= opening
S.append(title('13F', 'Trees and minimum connector problems', f'{CAM} · 13F Trees and minimum connector problems', 'gm12-u4-13f'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 13F', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>13F')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('CFAT 4.13.2', '· 13C–13E', 'var(--muted)'), ('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· two Year 11 questions', 'var(--apk)'),
  ('Trees and spanning trees', '', None), ('Worked example 11', '→ You try', None), ('Prim’s algorithm', '', None), ('Worked example 12', '→ You try', None),
  ('Minimum connector problems', '', None), ('Worked example 13', '→ You try', None), ('Exit tasks', '· two VCAA questions', 'var(--exit)'),
  ('Check-in and coursework', '', 'var(--muted)')]))
S.append(cfat('CFAT 4.13.2', 'Walks, Eulerian and Hamiltonian paths, shortest paths', '13C–13E', 12, 'Edrolo U3&amp;4 8C, 8F exercise questions · lessons/CFAT 4.13.2 (13C-13E)'))
S.append(keys([
  ('Tree', 'a connected graph with no loops, multiple edges or cycles'), ('Spanning tree', 'a tree that connects every vertex of a graph'),
  ('Weight of a tree', 'the sum of the weights of its edges'), ('Minimum spanning tree', 'the spanning tree with the smallest total weight'),
  ('Prim’s algorithm', 'grow the tree one cheapest new edge at a time'), ('Connector problem', 'join every location as cheaply as possible = minimum spanning tree')],
  [('Edges in a tree', '<i>e</i> = <i>v</i> − 1', 'e.g. 9 vertices → 8 edges'), ('Edges to remove', 'edges in graph − (<i>v</i> − 1)', 'e.g. 13 − 8 = 5'),
   ('Prim · next edge', 'cheapest edge from the tree to a NEW vertex', 'never close a cycle')],
  f'{CAM}, 13F pp. 640–644; {EDR}, 8D pp. 563–564; Study Design: the minimum connector problem, trees, spanning trees and minimum spanning trees and Prim’s algorithm'))

# ================= Do Now 1: VCAA 2024 E1 Q34 (13C)
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2024 Exam 1 Q34', 'Review of 13C (Eulerian trails)',
  ('<div style="font-size:24px">Consider the following graph.</div>', Wd(300, q34('q34')), '<div style="font-size:24px">A Eulerian trail through this graph could be</div>'),
  [('Odd vertices', '<i>B</i> and <i>F</i> have degree 3: the trail starts at one and ends at the other', 'data-hi="#q34|vB,vF|hy"'),
   ('Every edge once', '9 edges, so the trail lists 10 vertices: only C and D are long enough'),
   ('Check C', 'BA, AC, CB, BD, DC, CF, FD, DE, EF: all 9 edges, none repeated', HI('q34', ['ab', 'ac', 'bc', 'bd', 'cd', 'cf', 'df', 'de', 'ef'], 'hy'))],
  'BACBDCFDEF: <b>C</b>.', 'VCAA 2024 General Mathematics Exam 1 Q34 (examiner report: 85% correct)', mc=['ABCDEF', 'ACBDCFDEF', 'BACBDCFDEF', 'BDCABCDFCDEF'], key='C', stat=('mc', 85)))
# ================= Do Now 2: VCAA 2025 E1 Q38 (13D/13E)
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2025 Exam 1 Q38', 'Review of 13D–13E (shortest path)',
  ('<div style="font-size:20px">The diagram below shows the network of roads that Sofia can use to travel between home and school.<br>The numbers on the roads show the length, in metres, of each section of road.</div>',
   Wd(560, sofia('sf')), '<div style="font-size:20px">Using this network of roads, the shortest distance that Sofia can take to travel from home to school, in metres, is</div>'),
  [('To the middle', 'direct 1900 · over the top 1500 + 500 = 2000 · lower 900 + 500 + 400 = <b>1800</b>', HI('sf', ['hl', 'lk', 'km'], 'hy')),
   ('Middle to school', 'direct 3300 · 800 + 1100 = <b>1900</b> · 800 + 900 + 300 = 2000', HI('sf', ['hl', 'lk', 'km', 'mb', 'bs'], 'hy')),
   ('Compare', '1800 + 1900 = 3700 · top road 1500 + 1600 + 700 = 3800 · bottom 1200 + 1600 + 1100 = 3900')],
  '3700 m: <b>A</b>.', 'VCAA 2025 General Mathematics Exam 1 Q38 (examiner report: 47% correct)', mc=['3700', '3800', '3900', '5100'], key='A', stat=('mc', 47),
  dis=('B', '3800 is the top road (1500 + 1600 + 700): the route with fewest edges is not always shortest.')))
sm()
# ================= Do Now 3: VCAA 2025 E2 Q15b (13A)
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2025 Exam 2 Q15b', 'Review of 13A (Euler’s formula)',
  ('<div style="font-size:21px">Frances lives in a housing estate.<br>On the graph below the vertices represent her favourite locations, and the edges represent the roads between them.</div>',
   Wd(420, frances('fr')),
   '<div style="font-size:21px">b. Euler’s formula, <i>v</i> + <i>f</i> = <i>e</i> + 2, holds for this graph.<br><b>Complete</b> the formula by writing the appropriate numbers in the boxes below. <span class="muted">(1 mark)</span>'
   '<div style="font-size:24px;text-align:center;margin-top:6px">☐ + ☐ = ☐ + 2<br><span style="font-size:16px">&nbsp;<i>v</i>&emsp;&emsp;&nbsp;<i>f</i>&emsp;&emsp;&nbsp;<i>e</i>&emsp;&emsp;&emsp;</span></div></div>'),
  [('Vertices', '<i>v</i> = 5'), ('Edges', '<i>e</i> = 7', HI('fr', ['cg', 'gp', 'cp', 'cs', 'ch', 'ph', 'sh'], 'hy')),
   fx('Faces', '<i>f</i>', F(V('e', '7'), ' + 2 − ', V('v', '5')), '4', 'data-hi="#fr||"')],
  '<b>5 + 4 = 7 + 2</b>', 'VCAA 2025 General Mathematics Exam 2 Q15 stem and Q15b (examiner report: average 0.9/1)', stat=('avg', 90), cmd=('Complete', 1, 'v, f, e in the boxes')))
# ================= Do Now 4: VCAA 2026 NHT E2 Q4c (5B)
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2026 NHT Exam 2 Q4c', 'Review of 5B (smoothing)',
  '<div style="font-size:18px">Sunspots are dark areas on the surface of the Sun.<br>The time series plot below shows mean monthly sunspot numbers for the period from January 1975 to December 2010.'
  + Wd(470, img('vcaa2026nhte2q4_sunspots.png')) + 'Astronomers who monitor sunspot numbers use 13-point smoothing to display the underlying trend in the data.<br>'
  'c. How many points would there be in the smoothed plot if 13-point smoothing was applied to the entire data set from January 1975 to December 2010? <span class="muted">(1 mark)</span></div>',
  [('Data points', '36 years × 12 months = 432 months'), ('Lost at the ends', '13-point: 6 lost at each end, 12 in total'), ('Smoothed points', '432 − 12 = 420')],
  'There would be <b>420</b> points.', 'VCAA 2026 (NHT) General Mathematics Exam 2 Q4 stem and Q4c (NHT examiner reports give no % correct); plot from the paper'))
sm()

# ================= APK 1: Cambridge U1&2 checklist #15
HS = ['bs', 'lc', 'ct', 'bb', 'ha', 'tm', 'ms', 'hl']
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #15', 'Minimum spanning tree (Year 11)',
  ('<div style="font-size:22px">For the graph below, <b>find</b> the minimum spanning tree and state its length.</div>', Wd(640, F13D.hschool('hs')), ''),
  [('Start at Home', 'cheapest edge 3', HI('hs', ['ha'])), ('Grow', 'next cheapest to a new vertex: 5 (to the bottom-left), then 2, 2', HI('hs', ['ha', 'hl', 'lc', 'ct'])),
   ('Grow', '4, 4 (to School), then 1, 2', HI('hs', HS)), ('Check', '9 vertices → 8 edges: 3 + 5 + 2 + 2 + 4 + 4 + 1 + 2')],
  'The minimum spanning tree has length <b>23</b>.', f'{CAM12} · Ch 8 skills checklist #15, p. 542 (graph from #14) · answer worked with Prim’s algorithm',
  cmd=('Find', None, 'the tree and its length')))
# ================= APK 2: VCAA 2017 E2 Q3a
S.append(qslide('apk', 'APK · VCAA 2017 Exam 2 Q3a', 'Minimum spanning tree (Year 11)',
  '<div style="font-size:17px">While on holiday, the four friends visit a theme park where there are nine rides.<br>On the graph below, the positions of the rides are indicated by the vertices.<br>'
  'The numbers on the edges represent the distances, in metres, between rides.' + Wd(380, park('pk'))
  + 'a. Electrical cables are required to power the rides.<br>These cables will form a connected graph.<br>The shortest total length of cable will be used.'
  + plist([('i.', 'Give a mathematical term to describe a graph that represents these cables. <span class="muted">(1 mark)</span>'),
           ('ii.', '<b>Draw</b> in the graph that represents these cables on the diagram below. <span class="muted">(1 mark)</span>')]) + '</div>',
  [('Connected + shortest', 'every ride joined, least total length: a minimum spanning tree'),
   ('Prim', 'start 50, then 100, 100 (150 would close a cycle)', HI('pk', ['p6', 'p5', 'p4'])),
   ('Prim', '200 down, 150, then 300 to the top-left ride', HI('pk', ['p6', 'p5', 'p4', 'p10', 'p14', 'p3'])),
   ('Prim', '400 to the right ride, then 200: 9 vertices, 8 edges', HI('pk', TP_T))],
  '', f'VCAA 2017 Further Mathematics Exam 2 Networks and decision mathematics Q3 stem and Q3a (examiner report: Q3a 53%) · {EDR12} 7F Q18 · {EDR} 8D Q13',
  stat=('avg', 53), parts=[('i.', 'a <b>minimum spanning tree</b>'), ('ii.', 'the 8 orange edges (total 1500 m)')]))
sm(extra='sm xs')

# ================= Learn 1: trees and spanning trees
S.append(learn('Learn · 13F', 'Trees and spanning trees',
  '<h4>As few edges as possible</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a <b>tree</b> is connected and has no loops, multiple edges or cycles</li><li><i>n</i> vertices → <i>n</i> − 1 edges</li>'
  '<li>a <b>spanning tree</b> is a tree inside a graph that reaches every vertex</li><li>its <b>weight</b> is the sum of its edge weights</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(380, tree7('tr')) + '<div style="width:380px">'
  + frag('7 vertices, 6 edges', 'data-hi="#tr|ab,bf,fg,ac,ce,cd|hy"') + frag('Add any edge → a cycle appears: no longer a tree')
  + frag('Remove any edge → disconnected: no longer a tree') + '</div></div>',
  'A graph usually has many spanning trees. Count first: you must keep exactly v − 1 edges.',
  f'{CAM}, 13F p. 641 (own words; Cambridge’s tree) · {EDR}, 8D p. 563', cards=(kcard('Tree', 'e = v − 1, no cycles'), kcard('Spanning tree', 'reaches every vertex'))))
# ================= Ex 11
S.append(qslide('we', 'Worked example 11 · 13F', 'Finding the weight of a spanning tree',
  ('<div style="font-size:22px">a <b>Draw</b> one spanning tree for the graph shown.<br>b <b>Calculate</b> the weight of this spanning tree.</div>', Wd(520, ex11('x11')), ''),
  [('Count', '9 vertices and 13 edges'), ('Tree size', 'the spanning tree will have 9 − 1 = 8 edges'),
   ('Remove', '13 − 8 = 5 edges, keeping every vertex connected', HI('x11', X11_DROP, 'hv')),
   ('Add', '5 + 2 + 1 + 4 + 5 + 2 + 3 + 4 = 26', HI('x11', X11_KEEP, 'hy'))],
  '', f'{CAM} · Example 11 (pp. 641–642)', video='Cambridge GO · Example 11 (13F Resources)', cmd=('Draw', None, 'and calculate'),
  parts=[('a', 'the 8 yellow edges (one of many spanning trees)'), ('b', 'Weight = <b>26</b>')]))
S.append(qslide('yt', 'You try · Edrolo 8D WE1', 'Finding the weight of a spanning tree',
  ('<div style="font-size:22px">Consider the following graph.</div>', Wd(500, we1('w1')),
   plist([('a.', '<b>Construct</b> a spanning tree for the graph'), ('b.', '<b>Calculate</b> the weight of the spanning tree.')])),
  [('Count', '8 vertices, so <i>e</i> = 8 − 1 = 7 edges'), ('Remove', 'the graph has 9 edges, so remove 2 (keep every vertex connected)', HI('w1', W1_DROP, 'hv')),
   ('Add', '40 + 40 + 70 + 90 + 30 + 20 + 50', HI('w1', ['lb', 'bo', 'to', 'or', 'ok', 'mk', 'rm'], 'hy'))],
  '', f'{EDR} · 8D Worked example 1 (p. 563)', cmd=('Construct', None, 'and calculate'),
  parts=[('a', 'the 7 yellow edges (other spanning trees are possible)'), ('b', '<b>340</b>')]))

# ================= Learn 2: Prim
S.append(learn('Learn · 13F', 'Prim’s algorithm',
  '<h4>Grow the cheapest tree</h4><ol style="font-size:18px;line-height:1.45;margin-left:24px"><li>start at any vertex</li>'
  '<li>take the cheapest edge from it</li><li>look at every edge leaving the tree so far; take the cheapest one that reaches a <b>new</b> vertex</li>'
  '<li>skip edges that would make a cycle, loop or double edge</li><li>repeat until every vertex is joined (<i>v</i> − 1 edges); add the weights</li></ol>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(250, ex12('pl')) + '<div style="width:380px">'
  + frag('Start at <i>A</i>: 2 to <i>B</i>', HI('pl', ['ab'])) + frag('From <i>A</i> or <i>B</i>: 5 to <i>D</i>', HI('pl', ['ab', 'ad']))
  + frag('Ties? Either edge is fine.') + '</div></div>',
  'Write the edges in the order you choose them: it is your working.',
  f'{CAM}, 13F p. 642 (own words) · {EDR}, 8D p. 564', cards=(kcard('Minimum spanning tree', 'smallest total weight'), kcard('Prim', 'cheapest edge to a new vertex'))))
# ================= Ex 12
P12 = prim('x12', X12_T)
S.append(qslide('we', 'Worked example 12 · 13F', 'Finding the minimum spanning tree',
  ('<div style="font-size:22px"><b>Apply</b> Prim’s algorithm to find the minimum spanning tree for the graph shown on the right. <b>Write down</b> the total weight of the minimum spanning tree.</div>', Wd(440, ex12('x12')), ''),
  [('Start at <i>A</i>', 'smallest edge from <i>A</i>: <i>AB</i> = 2', P12[0]), ('<i>A</i>, <i>B</i>', 'smallest from either: <i>AD</i> = 5', P12[1]),
   ('<i>A</i>, <i>B</i>, <i>D</i>', 'smallest: <i>DC</i> = 3', P12[2]), ('<i>A</i>, <i>B</i>, <i>D</i>, <i>C</i>', 'smallest: <i>CE</i> = 5', P12[3]),
   ('… <i>E</i>', 'smallest: <i>EF</i> = 2; all vertices joined', P12[4])],
  'The total weight of the minimum spanning tree is 2 + 5 + 3 + 5 + 2 = <b>17</b>.', f'{CAM} · Example 12 (pp. 643–644)',
  video='Cambridge GO · Example 12 (13F Resources)', cmd=('Apply', None, 'Prim’s algorithm')))
sm()
PW2 = prim('w2', W2_T)
S.append(qslide('yt', 'You try · Edrolo 8D WE2', 'Finding the minimum spanning tree',
  ('<div style="font-size:22px">For the following graph:</div>', Wd(470, we2('w2')),
   plist([('a.', '<b>Use</b> Prim’s algorithm to find the minimum spanning tree.'), ('b.', '<b>Calculate</b> the weight of the minimum spanning tree.')])),
  [('Start at <i>A</i>', 'both edges are 6: choose <i>AB</i>', PW2[0]), ('<i>A</i>, <i>B</i>', 'lowest: <i>AC</i> = 6', PW2[1]),
   ('<i>A</i>, <i>B</i>, <i>C</i>', 'the loop (1) joins no new vertex: skip it · <i>CF</i> = 4', PW2[2]), ('Continue', '<i>FD</i> = 3', PW2[3]), ('Continue', '<i>FE</i> = 6', PW2[4])],
  '', f'{EDR} · 8D Worked example 2 (pp. 564–565)', cmd=('Use', None, 'Prim’s algorithm'),
  parts=[('a', 'edges <i>AB</i>, <i>AC</i>, <i>CF</i>, <i>DF</i>, <i>EF</i>'), ('b', '6 + 6 + 4 + 3 + 6 = <b>25</b>')]))
sm()

# ================= Learn 3: connector problems
S.append(learn('Learn · 13F', 'Minimum connector problems',
  '<h4>Connect everything, cheapest</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>pipes, cables, roads that must reach every location</li><li>the cheapest way = the <b>minimum spanning tree</b></li>'
  '<li>answer = the tree drawn + its total weight (with units)</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(500, ex13('cl')) + '<div style="width:360px">'
  + frag('Gas pipes to towns, cables to rides, water to outlets') + frag('Start Prim at the source (here the tank)', 'data-hi="#cl|ct|hc"') + '</div></div>',
  'Key words: “connect all”, “minimum length of cable / pipe”, “least cost to join”.',
  f'{CAM}, 13F p. 644 (own words) · {EDR}, 8D p. 564', cards=(kcard('Connector problem', 'minimum spanning tree'),)))
# ================= Ex 13
P13 = prim('x13', X13_T)
S.append(qslide('we', 'Worked example 13 · 13F', 'Solving a connector problem',
  '<div style="font-size:17px">Water is to be piped from a water tank to seven outlets on a property. The distances (in metres) of the outlets from the tank and from each other are shown in the network below. '
  'Starting at the tank, the aim is to find the minimum length of pipe, in metres, which will be needed to have water piped to all outlets in the property.' + Wd(500, ex13('x13'))
  + plist([('a', 'On the diagram, <b>show</b> where the water pipes will be placed in order to minimise the length required.'),
           ('b', '<b>Calculate</b> the total length, in metres, of the water pipe that is required to obtain this minimum length.')]) + '</div>',
  [('Tank', 'cheapest edge from the tank: 2 to <i>C</i>', P13[0]), ('Prim', '5 to <i>D</i>, 6 to <i>B</i>', P13[2]), ('Prim', '8 to <i>E</i>, 7 to <i>F</i>', P13[4]),
   ('Prim', '10 to <i>G</i>, 6 to <i>A</i>: all 7 outlets joined', P13[6])],
  '', f'{CAM} · Example 13 (pp. 644–645)', video='Cambridge GO · Example 13 (13F Resources)', cmd=('Calculate', None, 'pipe length'),
  parts=[('a', 'pipes on the 7 orange edges (the minimum spanning tree)'), ('b', '2 + 6 + 5 + 8 + 7 + 10 + 6 = <b>44 metres</b>')]))
sm(extra='sm xs')
PU = prim('u2', U2_T)
S.append(qslide('yt', 'You try · Edrolo U1&amp;2 7F WE2', 'Prim’s algorithm',
  ('<div style="font-size:22px"><b>Use</b> Prim’s algorithm to draw the minimum spanning tree for the following graph.</div>', Wd(520, u12we2('u2')), ''),
  [('Start at <i>A</i>', '7 or 5: <i>AB</i> = 5', PU[0]), ('<i>A</i>, <i>B</i>', '<i>BD</i> = 2', PU[1]), ('<i>A</i>, <i>B</i>, <i>D</i>', '<i>DC</i> = 3', PU[2]),
   ('Skip <i>AC</i>', 'it would make a cycle · 8 (two edges): choose <i>DG</i>', PU[3]), ('Continue', '<i>GF</i> = 6, then <i>FE</i> = 4', PU[5]),
   ('Last', '<i>H</i>: 10 either way, choose <i>GH</i>', PU[6])],
  'Minimum spanning tree <i>AB</i>, <i>BD</i>, <i>DC</i>, <i>DG</i>, <i>GF</i>, <i>FE</i>, <i>GH</i>: total weight <b>38</b>.', f'{EDR12} · 7F Worked example 2 (pp. 419–420)',
  cmd=('Use', None, 'Prim’s algorithm')))
sm()

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 2 · VCAA 2018 Exam 1 Q1', 'Show what you know',
  ('<div style="font-size:24px">Consider the graph with five isolated vertices shown below.</div>', Wd(340, iso5('i5', add=True)),
   '<div style="font-size:24px">To form a tree, the minimum number of edges that must be added to the graph is</div>'),
  [('Tree', '<i>e</i> = <i>v</i> − 1 = 5 − 1 = 4', 'data-show="#i5|t0,t1,t2,t3"')],
  '4 edges: <b>B</b>.', f'VCAA 2018 Further Mathematics Exam 1 Networks and decision mathematics Q1 (examiner report: 92% correct) · {EDR} 8D Q11',
  mc=['1', '4', '5', '6', '10'], key='B', stat=('mc', 92)))
OPT = '<div class="opts">' + ''.join(f'<div><b>{k}.</b>{spopt(v)}</div>' for k, v in SP_OPT.items()) + '</div>'
S.append(qslide('ex', 'Exit task 2 of 2 · VCAA 2020 Exam 1 Q3', 'Show what you know',
  '<div style="font-size:18px">' + Wd(300, sp('sp')) + 'Which one of the following is <b>not</b> a spanning tree for the network above?' + OPT + '</div>',
  [('Spanning tree', 'only edges of the network, every vertex, 5 edges, no cycle'),
   ('Check edges', 'B uses an edge from 3 to 5: the network has no edge 3–5')],
  '<b>B</b>: it uses an edge that is not in the network.', f'VCAA 2020 Further Mathematics Exam 1 Networks and decision mathematics Q3 (examiner report: 81% correct) · {EDR} 8D Q12',
  stat=('mc', 81)))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 13 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '13F' and v.get('url')]))
n = assemble(S, '12MAG · 13F · Trees and minimum connector problems', os.path.join(ROOT, 'lessons', '13F slides.html'))
print(n - 1, 'slides')
