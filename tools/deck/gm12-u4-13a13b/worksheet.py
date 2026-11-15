"""Lesson gm12-u4-13a13b (13A graphs and networks, 13B adjacency matrices) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 13A/13B).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #2 and #8 (pp. 540-541), VCAA 2017 Exam 1 N&DM Q2 (Edrolo U1&2 7A Q13).
Example 1-6 = Cambridge U3&4 Examples 1-6 (pp. 612-620).
You try 1 = Edrolo U3&4 8A WE1 · 2 = 8A WE2a · 3 = 8A WE3a · 4 = 8A WE3b · 5 = 8B WE2 · 6 = 8B WE1.
Exits = VCAA 2021 Exam 2 N&DM Q1a, b (Edrolo 8A Q18) · VCAA 2021 Exam 1 N&DM Q3 (Edrolo 8A Q20) · VCAA 2019 Exam 1 N&DM Q6 (Edrolo 8B Q15).
Graphs redrawn with tools/deck/tpl/net.py (same vertices and edges); floor plan and road map cropped from the VCAA papers.
Output: lessons/13A-13B worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-13a13b/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
from net import net, amat
K = '#111'
def G(svg, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{svg}</div>'
def RG(svg, mm): return f'<div style="width:{mm}mm;margin:0 auto">{svg}</div>'
A = lambda v: ans(v)
L5 = list('ABCDE')
def blankmat(labels, rows, fs=11): return amat(labels, [[A(v) for v in r] for r in rows], fs=fs)
def fig_l(cap, svg, mm): return f'<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{cap}</div>{G(svg, mm)}</div>'

P = [title('13A–13B', 'Graphs, networks and adjacency matrices')]
P.append(lis(['To be able to define and identify a graph, vertex, edge and loop.', 'To be able to find the degree of a vertex and the sum of degrees.',
              'To be able to describe the features of a graph.', 'To be able to define and identify a planar graph and its faces.',
              'To be able to apply Euler’s formula and use it to verify if a graph is planar.', 'To be able to use an adjacency matrix to represent a graph.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', G(net(K1_V, K1_E, W=290, H=200, pad=14, ink=K, fs=16), 45)
  + q('Determine the degree of each vertex in the graph above and the sum of degrees of the graph.')
  + space(12, 'deg(A) = 2, deg(B) = 3, deg(C) = 3, deg(D) = 3, deg(E) = 5; sum of degrees = 16'), ''))
P.append(box('Question 2', G(net(K2_V, K2_E, W=330, H=240, pad=12, ink=K), 40) + q('Verify Euler’s formula for the graph above.')
  + space(14, 'v = 3, e = 5, f = 4; v + f = e + 2: 3 + 4 = 5 + 2, 7 = 7 ✓'), ''))
P.append(box('Question 3 · VCAA 2017 Exam 1 Q2', q('Two graphs, labelled Graph 1 and Graph 2, are shown below.') + G(apk3().replace('#1f4fb0', K), 80)
  + q('The sum of the degrees of the vertices of Graph 1 is')
  + mc(['two less than the sum of the degrees of the vertices of Graph 2.', 'one less than the sum of the degrees of the vertices of Graph 2.', 'equal to the sum of the degrees of the vertices of Graph 2.',
        'one more than the sum of the degrees of the vertices of Graph 2.', 'two more than the sum of the degrees of the vertices of Graph 2.'], 'C') + why('both have 6 edges: sum of degrees = 2 × 6 = 12'), ''))
P.append(sect('13A Graphs and networks', 'Example, then you try'))
P.append(exyt('Example 1 · Graphs',
  fig_l(q('A connected graph is shown on the right.'), ex1('', ink=K, fs=16), 46)
  + parts([('a', 'What is the degree of vertex <i>C</i>?', 'deg(C) = 4', 'L'), ('b', 'Which vertices have a loop?', 'B and F', 'L'),
           ('c', 'What is the degree of vertex <i>F</i>?', 'deg(F) = 5', 'L'), ('d', 'A bridge exists between two vertices. Which vertices are they?', 'A and C', 'L'),
           ('e', 'Draw a subgraph of this graph that involves only vertices <i>A</i>, <i>B</i> and <i>C</i>.', RG(ex1sub(ink=RED), 22), 18)]),
  'You try 1', q('Consider the graph.') + G(y1('', ink=K, fs=16), 46)
  + parts([('a', 'How many edges are in this graph?', '8', 'L'), ('b', 'How many faces are in this graph?', '4', 'L'), ('c', 'How many vertices are in this graph?', '6', 'L'),
           ('d', 'Which vertex has a loop?', 'C', 'L'), ('e', 'Determine the degree of vertex C.', '5', 'L'), ('f', 'Between which vertices can a bridge be found?', 'C and D', 'L')])))
P.append(exyt('Example 2 · Redrawing a graph in planar form',
  q('Show that this graph is planar by redrawing it so that no edges cross.') + G(ex2('', ink=K, fs=16).replace('class="hid0"', 'style="display:none"'), 50)
  + solfig(32, RG(net(EX2_V, [e for e in EX2_E if e[2:] == () or e[2].get('i') not in ('ce', 'ce2')] + [('C', 'E', {'via': [(320, 20), (375, 100), (320, 180)]})], W=390, H=200, pad=12, ink=RED, fs=16), 50)),
  'You try 2', q('Consider the following graph.') + G(y2('', ink=K, fs=16), 52) + parts([('a', 'Redraw the graph in planar form.', RG(y2('', planar=True, ink=RED, fs=16), 52), 34)])))
P.append(exyt('Example 3 · Verifying Euler’s formula',
  fig_l(q('For the graph shown on the right:'), ex3('', ink=K, fs=16).replace('class="hid0"', 'style="display:none"'), 46)
  + parts([('a', 'redraw the graph into planar form', RG(net(EX3_V, [e for e in EX3_E if e[2:] == () or e[2].get('i') not in ('ac', 'ac2')] + [('A', 'C', {'via': [(200, 205), (310, 195), (325, 100)]})], W=360, H=210, pad=12, ink=RED, fs=16), 44), 30),
           ('b', 'verify Euler’s formula for this graph.', 'v = 5, e = 7, f = 4: v + f = e + 2 → 5 + 4 = 7 + 2, 9 = 9 ✓', 12)]),
  'You try 3', q('Use Euler’s rule to solve the following questions.') + G(y3('', ink=K, fs=16), 34)
  + parts([('a', 'Show that the graph is a connected planar graph.', 'v = 4, e = 5, f = 3: v − e + f = 4 − 5 + 3 = 2 ✓ so it is a connected planar graph', 14)])))
P.append(exyt('Example 4 · Using Euler’s formula',
  q('A connected planar graph has six vertices and nine edges. How many faces does the graph have? Draw a connected planar graph with six vertices and nine edges.')
  + q('<i>v</i> = ' + A('6') + ' &nbsp; <i>e</i> = ' + A('9')) + q('<i>v</i> + <i>f</i> = <i>e</i> + 2 → ' + A('6 + f = 9 + 2 → f = 5'))
  + solfig(36, RG(ex4('', ink=RED, fs=16), 46)),
  'You try 4', parts([('b', 'If a connected planar graph has five vertices and five faces, how many edges does the graph have?', '5 − e + 5 = 2 → e = 8 edges', 18)])))
P.append(sect('13B Adjacency matrices', 'Example, then you try'))
P.append(exyt('Example 5 · Drawing a graph from an adjacency matrix',
  q('Draw the graph that is represented by the following adjacency matrix.') + amat(L5, EX5_M, fs=11)
  + solfig(40, RG(net(EX5_V, [(a, b, {k: v for k, v in o.items() if k != 'hid'}) for a, b, o in EX5_E], W=380, H=215, pad=10, ink=RED, fs=16), 52)),
  'You try 5', q('Construct a graph from the following adjacency matrix.') + amat(L5, Y5_M, fs=11) + solfig(40, RG(y5('', ink=RED, fs=16), 52))))
P.append(exyt('Example 6 · Constructing an adjacency matrix',
  q('Construct an adjacency matrix that can be used to represent the graph opposite. This graph represents the ways that three houses <i>A</i>, <i>B</i> and <i>C</i> are connected to three utility outlets, gas (<i>G</i>), water (<i>W</i>) and electricity (<i>E</i>).')
  + G(net(EX6_V, EX6_E, W=380, H=190, pad=12, ink=K, fs=16), 46) + blankmat(['A', 'B', 'C', 'G', 'W', 'E'], EX6_M),
  'You try 6', q('Construct an adjacency matrix from the following graph.') + G(net(Y6_V, Y6_E, W=320, H=225, pad=12, ink=K, fs=16), 44)
  + space(30, RG(amat(L5, Y6_M, fs=11), 40))))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2021 Exam 2 Q1a, b', q('Maggie’s house has five rooms, <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i>, and eight doors.<br>The floor plan of these rooms and doors is shown below. The outside area, <i>F</i>, is shown shaded on the floor plan.')
  + f'<div style="display:flex;gap:6mm;align-items:center;justify-content:center"><div style="width:42mm">{img("vcaa2021e2_floorplan.png")}</div><div style="width:52mm">'
  + x1('', ink=K, fs=16).replace('class="hid0"', 'class="solonly"').replace('stroke="#d2475b"', f'stroke="{RED}"') + '</div></div>'
  + q('The floor plan is represented by the graph above.<br>On this graph, vertices represent the rooms and the outside area. Edges represent direct access to the rooms through the doors.<br>One edge is missing from the graph.')
  + parts([('a', 'On the <b>graph above</b>, draw the missing edge. (Answer on the graph above.)', 'edge A–B (red)', 6), ('b', 'What is the degree of vertex <i>E</i>?', '2', 'L')]), '2 marks'))
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q3', q('Consider the graph below.') + G(net(X2_V, X2_E[:6], W=320, H=190, pad=14, ink=K), 50) + q('The number of faces is')
  + mc(['2', '3', '4', '5', '6'], 'C', cols=5) + why('redraw one crossing edge round the outside: 3 inside faces + the outside = 4; v + f = e + 2: 4 + 4 = 6 + 2'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2019 Exam 1 Q6', q('The map below shows all the road connections between five towns, <i>P</i>, <i>Q</i>, <i>R</i>, <i>S</i> and <i>T</i>.')
  + f'<div style="width:60mm;margin:0 auto">{img("vcaa2019e1q6_map.png")}</div>' + q('The road connections could be represented by the adjacency matrix')
  + mc([amat(list('PQRST'), o, fs=9.5) for o in X3_OPTS], 'A', cols=3) + why('loop at P (1) and three roads between P and Q (3): only A'), '1 mark'))
SC = [x for g_ in [['I can identify edges, vertices and loops in a graph.', 'I can determine the degree of a vertex in a graph.',
                    'I can identify simple graphs, isolated vertices, degenerate graphs, connected graphs, bridges and subgraphs.', 'I can recognise isomorphic graphs.',
                    'I can redraw graphs in planar form.', 'I can use Euler’s formula.'], ['I can write an adjacency matrix from a graph.', 'I can construct a graph from an adjacency matrix.']] for x in g_]
P.append(close(SC, [('13A', 'Q1–15'), ('13B', 'Q1–12')], ['13A', '13B']))
CSS_EXTRA = ('<style>.solonly{display:none}.sol .solonly{display:inline}.box svg{max-width:100%}.mc .amat{margin:0}'
             '.space .ans svg path{stroke:' + RED + '}.space .ans svg circle{fill:' + RED + '}.space .ans .amat{color:' + RED + '}</style>')
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-13a13b', '13A-13B', 'AoS 4 · Networks and decision mathematics', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-13a13b-worksheet', '13A-13B worksheet'), ('gm12-u4-13a13b-worksheet-solutions', '13A-13B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
