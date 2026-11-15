"""Lesson gm12-u4-13f (13F trees and minimum connector problems) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 13F).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #15 (p. 542, graph from #14) · VCAA 2017 Exam 2 N&DM Q3a (Edrolo U1&2 7F Q18).
Examples 11-13 = Cambridge U3&4 Examples 11 (pp. 641-642), 12 (pp. 643-644), 13 (pp. 644-645).
You try 11 = Edrolo U3&4 8D WE1 (p. 563) · You try 12 = 8D WE2 (pp. 564-565) · You try 13 = Edrolo U1&2 7F WE2 (pp. 419-420).
Exits = VCAA 2018 Exam 1 N&DM Q1 (Edrolo 8D Q11) · VCAA 2020 Exam 1 N&DM Q3 (Edrolo 8D Q12).
Graphs redrawn with tools/deck/tpl/net.py (same vertices, edges and weights); solutions draw the tree in red.
Output: lessons/13F worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-13f/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
import importlib.util
_s = importlib.util.spec_from_file_location('f13d', os.path.join(H, '..', 'gm12-u4-13d13e', 'figs.py')); F13D = importlib.util.module_from_spec(_s); _s.loader.exec_module(F13D)
K = '#111'
def G(svg, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{svg}</div>'
def ST(stu, sol, mm):
    """student figure / solutions figure (tree in red)"""
    return f'<div class="stuonly">{G(stu, mm)}</div><div class="solonly">{G(sol, mm)}</div>'
HS_T = ['bs', 'lc', 'ct', 'bb', 'ha', 'tm', 'ms', 'hl']
def hs_tree(): return F13D.hschool(ink=K).replace('', '')

P = [title('13F', 'Trees and minimum connector problems')]
P.append(lis([x for x in ['To be able to identify a tree.', 'To be able to find a spanning tree for a graph.',
                          'To be able to find the minimum spanning tree for a network using Prim’s algorithm.']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
hsol = F13D.net(F13D.HS_V, [(a, b, dict(o, col=RED) if o.get('i') in HS_T else o) for a, b, o in F13D.HS_E], W=730, H=270, pad=26, padx=70, fs=24, ink=K)
P.append(box('Question 1', q('For the graph below, find the minimum spanning tree and state its length.') + ST(F13D.hschool(ink=K), hsol, 95)
             + space(8, 'Length 23 (3 + 5 + 2 + 2 + 4 + 4 + 1 + 2)')))
P.append(box('Question 2 · VCAA 2017 Exam 2 Q3a', q('While on holiday, the four friends visit a theme park where there are nine rides.<br>On the graph below, the positions of the rides are indicated by the vertices.<br>'
  'The numbers on the edges represent the distances, in metres, between rides.') + G(park(ink=K), 62)
  + q('Electrical cables are required to power the rides.<br>These cables will form a connected graph.<br>The shortest total length of cable will be used.')
  + q('i. Give a mathematical term to describe a graph that represents these cables.') + space(8, 'minimum spanning tree') + '<hr class="dash">'
  + q('ii. Draw in the graph that represents these cables on the diagram below.') + ST(park(ink=K, dash=True), park(ink=K, dash=True, tree=TP_T), 62), '2 marks'))
P.append(sect('13F Trees and minimum connector problems', 'Example, then you try'))
P.append(exyt('Example 11 · Finding the weight of a spanning tree',
  q('a Draw one spanning tree for the graph shown.<br>b Calculate the weight of this spanning tree.') + G(ex11(ink=K), 66)
  + '<div class="stuonly">' + space(46) + '</div><div class="solonly">' + G(ex11(ink=K, tree=X11_KEEP), 60)
  + '<div class="ans">9 vertices, 13 edges → tree has 8 edges: remove 13 − 8 = 5.<br>Weight = 5 + 2 + 1 + 4 + 5 + 2 + 3 + 4 = 26</div></div>',
  'You try 11', q('Consider the following graph.') + G(we1(ink=K), 66)
  + q('a. Construct a spanning tree for the graph') + '<div class="stuonly">' + space(36) + '</div><div class="solonly">' + G(we1(ink=K, tree=['lb', 'bo', 'to', 'or', 'ok', 'mk', 'rm']), 56)
  + '<div class="ans">8 vertices → 7 edges; remove 2 (others possible)</div></div><hr class="dash">'
  + q('b. Calculate the weight of the spanning tree.') + space(12, '40 + 40 + 70 + 90 + 30 + 20 + 50 = 340')))
P.append(exyt('Example 12 · Finding the minimum spanning tree',
  q('Apply Prim’s algorithm to find the minimum spanning tree for the graph shown on the right. Write down the total weight of the minimum spanning tree.')
  + ST(ex12(ink=K), ex12(ink=K, tree=X12_T), 58) + space(24, 'AB 2, AD 5, DC 3, CE 5, EF 2<br>The total weight of the minimum spanning tree is 2 + 5 + 3 + 5 + 2 = 17.'),
  'You try 12', q('For the following graph:') + ST(we2(ink=K), we2(ink=K, tree=W2_T), 66)
  + q('a. Use Prim’s algorithm to find the minimum spanning tree.') + space(24, 'From A: AB 6, AC 6, CF 4 (skip the loop), FD 3, FE 6') + '<hr class="dash">'
  + q('b. Calculate the weight of the minimum spanning tree.') + space(12, '6 + 6 + 4 + 3 + 6 = 25')))
P.append(exyt('Example 13 · Solving a connector problem',
  q('Water is to be piped from a water tank to seven outlets on a property. The distances (in metres) of the outlets from the tank and from each other are shown in the network below. '
    'Starting at the tank, the aim is to find the minimum length of pipe, in metres, which will be needed to have water piped to all outlets in the property.')
  + ST(ex13(ink=K), ex13(ink=K, tree=X13_T), 78)
  + q('a On the diagram, show where the water pipes will be placed in order to minimise the length required.') + '<hr class="dash">'
  + q('b Calculate the total length, in metres, of the water pipe that is required to obtain this minimum length.') + space(16, '2 + 6 + 5 + 8 + 7 + 10 + 6 = 44 metres'),
  'You try 13', q('Use Prim’s algorithm to draw the minimum spanning tree for the following graph.') + G(u12we2(ink=K), 70)
  + '<div class="stuonly">' + space(52) + '</div><div class="solonly">' + G(u12we2(ink=K, tree=U2_T), 66)
  + '<div class="ans">AB 5, BD 2, DC 3, DG 8, GF 6, FE 4, GH 10 (total 38; other minimum spanning trees are possible)</div></div>'))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q1', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('Consider the graph with five isolated vertices shown below.') + q('To form a tree, the minimum number of edges that must be added to the graph is')
  + mc(['1', '4', '5', '6', '10'], 'B') + why('a tree with 5 vertices has 5 − 1 = 4 edges') + '</div>' + G(iso5(ink=K), 50) + '</div>', '1 mark'))
OPT = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:2mm">' + ''.join(f'<div><b>{k}.</b>{spopt(v, ink=K, fs=26)}</div>' for k, v in SP_OPT.items()) + '</div>'
P.append(box('Exit task 2 · VCAA 2020 Exam 1 Q3', G(sp(ink=K), 55) + q('Which one of the following is <b>not</b> a spanning tree for the network above?') + OPT
  + mc(['A', 'B', 'C', 'D', 'E'], 'B', cols=5) + why('B uses an edge from 3 to 5, which is not in the network'), '1 mark'))
SC = ['I can define tree, spanning tree and minimum spanning tree.', 'I can draw a minimum spanning tree using Prim’s algorithm.', 'I can solve a minimum connector problem.']
P.append(close(SC, [('13F', 'Q1–8')], ['13F']))
CSS_EXTRA = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
             'hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}</style>')
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-13f', '13F', 'AoS 4 · Networks and decision mathematics', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-13f-worksheet', '13F worksheet'), ('gm12-u4-13f-worksheet-solutions', '13F worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
