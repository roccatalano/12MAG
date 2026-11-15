"""Lesson gm12-u4-13c (13C exploring and travelling) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 13C).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #3 and #9 (pp. 540-541), Edrolo U1&2 7D Q11 (adapted from VCAA 2019 Exam 2 N&DM Q1bii).
Example 7-8 = Cambridge U3&4 Examples 7-8 (pp. 626-628; Example 8 road map cropped from the textbook).
You try 7 = Edrolo U3&4 8C WE1 · You try 8 = 8C WE2 + WE3.
Exits = VCAA 2019 Exam 2 N&DM Q1bi (Edrolo 8C Q14) · VCAA 2019 Exam 1 N&DM Q2 (Edrolo 8C Q15) · VCAA 2018 Exam 2 N&DM Q2c (Edrolo 8C Q16).
Graphs redrawn with tools/deck/tpl/net.py (same vertices and edges); walks given in a question are drawn as grey arrows.
Output: lessons/13C worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-13c/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
from figs import RED as WR
K = '#111'; GR = '#666'
def G(svg, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{svg}</div>'
def RG(svg, mm): return f'<div style="width:{mm}mm;margin:0 auto">{svg}</div>'
A = lambda v: ans(v)
def solonly(svg): return svg.replace('class="hid0"', 'class="solonly"').replace(f'stroke="{WR}"', f'stroke="{RED}"').replace(f'fill="{WR}"', f'fill="{RED}"')
def quad(f, keys='abcd', mm=40, se=None):
    return '<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:1mm">' + ''.join(
        f'<div><b>{k}</b>{G(f(k), mm)}<div style="text-align:center;font-size:8pt">start {se[k][0]} · end {se[k][1]}</div></div>' for k in keys) + '</div>'

P = [title('13C', 'Exploring and travelling')]
P.append(lis(['To be able to identify a walk as a trail, path, circuit or cycle.', 'To be able to identify a walk as an Eulerian trail, Eulerian circuit, Hamiltonian path or Hamiltonian cycle.',
              'To be able to use the degrees of the vertices to identify if an Eulerian trail or circuit is possible.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(pair(
  box('Question 1', G(net(K1_V, K1_E, W=290, H=200, pad=14, ink=K, fs=16), 34)
      + q('Give a reason why the graph above would be considered connected. Are there any bridges present? If yes, identify the two vertices the bridge(s) exist between.')
      + space(16, 'Connected: there is a path between each pair of vertices. Yes, one bridge, between C and D.'), ''),
  box('Question 2', q('For the graph below, is the walk <i>S</i>-<i>R</i>-<i>Q</i>-<i>P</i>-<i>O</i>-<i>N</i>-<i>M</i>-<i>S</i> considered a trail, path, circuit or cycle?')
      + G(net(K9_V, K9_E, W=285, H=170, pad=14, ink=K, fs=16), 40) + space(10, 'Cycle (no repeated edges or vertices; starts and ends at S)'), '')))
HKA = walk(['Mount Cockatoo', 'Snake Point', 'Point Kangaroo', 'Sunset Lookout', 'Waterfall Way', 'Feather Mountain', 'Mount Cockatoo'], pre='h', hid=True, bend=8)
P.append(box('Question 3 · VCAA 2019 Exam 2 Q1bii (adapted)', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('A hiking trail has six lookout points. The following network shows these lookout points represented by vertices. The edges of the network represent the paths between the lookout points.')
  + q('A hiking tour starts and finishes at Mount Cockatoo, visiting each lookout only once.') + q('Draw a possible route for this tour. (Answer on the network.)')
  + why('Mount Cockatoo – Snake Point – Point Kangaroo – Sunset Lookout – Waterfall Way – Feather Mountain – Mount Cockatoo (or the reverse)')
  + '</div>' + G(solonly(hike('', extra=HKA, ink=K)), 78) + '</div>', '1 mark'))
P.append(sect('13C Exploring and travelling', 'Example, then you try'))
P.append(exyt('Example 7 · Identifying types of walks',
  q('Identify the walk in each of graphs below as a trail, path, circuit, cycle or walk only.')
  + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1mm">' + ''.join(f'<div><b>{k}</b>{G(ex7(k, ink=K, wcol=GR), 34)}<div style="text-align:center;font-size:8pt">start {E7_SE[k][0]} · end {E7_SE[k][1]}</div>{space(7, v)}</div>'
      for k, v in zip('abcd', ['circuit', 'cycle', 'trail', 'walk only'])) + '</div>',
  'You try 7', q('Determine if the walk in each graph is a trail, path, circuit, cycle, or just a walk.')
  + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1mm">' + ''.join(f'<div><b>{k}</b>{G(ey1(k, ink=K, wcol=GR), 34)}<div style="text-align:center;font-size:8pt">start {Y1_W[k][0]} · end {Y1_W[k][-1]}</div>{space(7, v)}</div>'
      for k, v in zip('abcd', ['Cycle', 'Path', 'Trail', 'Walk'])) + '</div>'))
P.append(exyt('Example 8 · Eulerian and Hamiltonian travel',
  q('A map showing the towns of St Andrews, Kinglake, Yarra Glen, Toolangi and Healesville is shown below. Consider only the yellow routes in your answer. St Andrews and Yarra Glen are considered connected, although this route is not fully shown in the image.')
  + f'<div style="width:58mm;margin:0 auto">{img("cam_ex8_map.png")}</div>'
  + parts([('a', 'Draw a graph with a vertex representing each of these towns and edges representing the direct road connections between the towns.', RG(towns(ink=RED), 52), 30),
           ('b', 'Explain why an Eulerian trail, but not an Eulerian circuit, is possible through this graph.', 'There are exactly two odd-degree vertices (Toolangi, Kinglake): an Eulerian trail exists, but an Eulerian circuit does not.', 13),
           ('c', 'Write down an Eulerian trail that begins at Toolangi.', 'Toolangi–Healesville–Yarra Glen–Toolangi–Kinglake–Yarra Glen–St Andrews–Kinglake', 11),
           ('d', 'Write down a Hamiltonian cycle that begins at Healesville.', 'Healesville–Yarra Glen–St Andrews–Kinglake–Toolangi–Healesville', 10)]),
  'You try 8', q('The following graph represents a map of a walking track in the Dandenong Ranges.<br>The vertices represent lookout points.') + G(dandy(ink=K), 52)
  + parts([('a', 'Is an Eulerian trail possible in this graph?', 'Not possible (all vertices are even: A, B degree 4; C, D, E degree 2)', 10),
           ('b', 'Is an Eulerian circuit possible in this graph?', 'Possible (connected, all vertices even)', 9),
           ('c', 'Write down an Eulerian circuit starting from lookout B.', 'B–E–A–B–C–D–A–B', 9)])
  + QSEP + q('Max the mailman is doing his morning delivery run and has to deliver packages to six houses. These houses and the post office where the packages are stored are shown in the graph.')
  + G(maxg(ink=K), 50)
  + parts([('a', 'Write down a Hamiltonian path that allows Max to deliver all of his packages.', 'PO–1–2–4–3–6–5 (others are possible)', 9),
           ('b', 'Write down a Hamiltonian cycle that allows Max to deliver all of his packages before returning to the post office.', 'PO–2–4–3–6–5–1–PO (others are possible)', 9)])))
P.append(sect('Exit tasks', 'Show what you know'))
FHA = walk(['office', 'science laboratories', 'mathematics classrooms', 'library', 'computer rooms', 'gymnasium', 'office'], pre='f', hid=True, bend=8)
P.append(box('Exit task 1 · VCAA 2019 Exam 2 Q1bi', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('Fencedale High School has six buildings. The network shows these buildings represented by vertices.<br>The edges represent the paths between the buildings.')
  + q('A school tour is to start and finish at the office, visiting each building only once.<br>What is the mathematical term for this route?') + space(8, 'Hamiltonian cycle')
  + '</div>' + G(fence(ink=K), 72) + '</div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2019 Exam 1 Q2', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('Consider the following graph.')
  + q('The minimum number of extra edges that are required so that an Eulerian circuit is possible in this graph is') + mc(['0', '1', '2', '3', '4'], 'C', cols=5)
  + why('four odd vertices: each extra edge makes two of them even, so 2 edges') + '</div>' + G(net(X2_V, X2_E, W=240, H=130, pad=10, ink=K), 50) + '</div>', '1 mark'))
ZNA = walk('FEHIJGDABC', pre='z', hid=True, bend=0)
P.append(box('Exit task 3 · VCAA 2018 Exam 2 Q2c', q('In one area of the town of Zenith, a postal worker delivers mail to 10 houses labelled as vertices A to J on the following graph.')
  + '<div style="display:flex;gap:6mm;align-items:center">' + G(zen(ink=K), 40) + '<div style="flex:1">'
  + q('The postal worker has delivered the mail at F and will continue her deliveries by following a Hamiltonian path from F.')
  + q('Draw in a possible Hamiltonian path for the postal worker on the following diagram.') + why('F–E–H–I–J–G–D–A–B–C (others are possible)') + '</div>'
  + G(solonly(zen(dash=True, extra=ZNA, ink=K)), 40) + '</div>', '1 mark'))
SC = ['I can define walks, trails, paths, circuits and cycles through a graph.', 'I can determine whether an Eulerian trail or circuit exists in a graph.',
      'I can identify Eulerian trails and circuits through graphs.', 'I can identify Hamiltonian paths and cycles through graphs.']
P.append(close(SC, [('13C', 'Q1–14')], ['13C']))
CSS_EXTRA = ('<style>.solonly{display:none}.sol .solonly{display:inline}.box svg{max-width:100%}'
             '.space .ans svg path{stroke:' + RED + '}.space .ans svg circle{fill:' + RED + '}</style>')
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-13c', '13C', 'AoS 4 · Networks and decision mathematics', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-13c-worksheet', '13C worksheet'), ('gm12-u4-13c-worksheet-solutions', '13C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
