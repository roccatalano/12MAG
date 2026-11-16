"""Lesson gm12-u4-14a (14A Flow problems) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 14A).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #1 (p. 540) · VCAA 2016 Exam 2 N&DM Q1a, Q1bi (Edrolo U1&2 7A Q14).
Examples 1-5 = Cambridge U3&4 Examples 1 (p. 662), 2 (p. 664), 3 (pp. 664-665), 4 (pp. 665-668), 5 (pp. 668-669).
You try 1-3 = Edrolo U3&4 8E WE1 (p. 574), WE2 (p. 575), WE3 (pp. 576-577) · You try 4-5 = written for 12MAG (YT-14A-4, YT-14A-5).
Exits = VCAA 2016 Exam 1 N&DM Q2 (Edrolo 8E Q14) · VCAA 2020 Exam 2 N&DM Q4b,c (8E Q15) · VCAA 2017 Exam 1 N&DM Q8 (8E Q16).
Figures cropped from the PDFs (fig/); written You trys drawn with tools/deck/tpl/net.py.
Output: lessons/14A worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-14a/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
K = '#111'
def G(html, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{html}</div>'
def I(name, mm): return G(img(name), mm)
def ST(stu, sol, mm): return f'<div class="stuonly">{G(stu, mm)}</div><div class="solonly">{G(sol, mm)}</div>'
D = '<hr class="dash">'

P = [title('14A', 'Flow problems')]
P.append(lis(['To be able to define and describe flow.', 'To be able to calculate the maximum flow through a flow network by observation.',
              'To be able to identify cuts and calculate cut capacities.', 'To be able to determine the maximum flow through a flow network by finding the capacity of the minimum cut.',
              'To be able to solve flow problems by finding minimum cut capacities.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('Identify the number of vertices, edges and loops in the graph below.')
             + space(14, '5 vertices, 8 edges (6 + 2 loops), 2 loops') + '</div>' + I('apk1.png', 45) + '</div>'))
P.append(box('Question 2 · VCAA 2016 Exam 2 Q1a, Q1bi', q('A map of the roads connecting five suburbs of a city, Alooma (A), Beachton (B), Campville (C), Dovenest (D) and Easyside (E), is shown.')
  + '<div style="display:flex;gap:6mm;justify-content:center">' + I('apk2map.png', 50) + '</div>'
  + q('a. Starting at Beachton, which two suburbs can be driven to using only one road?') + space(8, 'Alooma and Easyside') + D
  + q('b. A graph that represents the map of the roads is shown.<br>One of the edges that connects to vertex E is missing from the graph.<br>Add the missing edge to the graph.')
  + I('apk2g.png', 45) + '<div class="solonly"><div class="ans">Draw the edge B–E.</div></div>', '2 marks'))
P.append(sect('14A Flow problems', 'Example, then you try'))
P.append(exyt('Example 1 · Calculating the maximum flow',
  q('In the digraph shown on the right, the vertices A, B, C, D and E represent towns. The edges of the graph represent roads and the weights of those edges are the maximum number of cars that can travel on the road each hour. The roads allow only one-way travel.')
  + I('ex1.png', 60) + q('a Find the maximum traffic flow from A to E through town C.') + space(8, '300 cars per hour') + D
  + q('b Find the maximum traffic flow from A to E overall.') + space(8, '300 + 150 = 450 cars per hour') + D
  + q('c A new road is being built to allow traffic from town D to town C. This road can carry 500 cars per hour.<br>i Add this road to the digraph.<br>ii Find the maximum traffic flow from A to E overall after this road is built.')
  + '<div class="solonly">' + I('ex1c.png', 55) + '</div>' + space(8, 'ii 800 cars per hour'),
  'You try 1', q('For the following directed graphs, determine if it is possible to travel from vertex A to vertex D. If so, identify a route and calculate the weight of the route.')
  + q('a.') + I('we1a.png', 50) + space(14, 'Yes, A–E–B–D, 4 + 7 + 5 = 16') + D + q('b.') + I('we1b.png', 55) + space(10, 'No: from A, B is a dead end and G leads to E, a dead end')))
P.append(exyt('Example 2 · Calculating cut capacity',
  q('Calculate the capacity of the four cuts shown in the network on the right. The source is vertex S and the sink is vertex T.') + I('ex2.png', 70)
  + space(30, 'C<sub>1</sub> = 15 + 20 = 35<br>C<sub>2</sub> = 14 + 20 = 34 (F to B not counted)<br>C<sub>3</sub> = 14 + 15 + 20 = 49<br>C<sub>4</sub> = 20 + 10 = 30 (D to C not counted)'),
  'You try 2', q('Calculate the capacity of each cut in the following network.') + I('we2.png', 70)
  + space(30, 'Cut 1: 8 + 15 = 23 (12 not counted)<br>Cut 2: 7 + 6 + 4 + 18 = 35<br>Cut 3: 8 + 3 + 18 = 29')))
P.append(exyt('Example 3 · Calculating maximum flow using cuts',
  q('Determine the maximum flow from S to T for the digraph shown on the right.') + ST(img('ex3.png'), img('ex3cuts.png'), 66)
  + space(34, 'C<sub>1</sub> = 19, C<sub>2</sub> = 14, C<sub>3</sub> = 19, C<sub>4</sub> = 12, C<sub>5</sub> = 3 + 3 + 1 = 7, C<sub>6</sub> = 9<br>The minimum cut capacity is 7 so the maximum flow from S to T is 7.'),
  'You try 3', q('The following network shows the number of cars that can travel between five different towns each second.') + ST(img('we3.png'), img('we3cuts.png'), 66)
  + q('What is the maximum number of cars that can travel from town A to town E each second?')
  + space(30, 'Cuts: 10, 21, 25, 20, 9, 9, 13 (C to D, B to C not counted where they flow back)<br>Minimum cut 9: 9 cars per second')))
P.append(exyt('Example 4 · Calculating maximum flow',
  q('The koala sanctuary in Cowes allows visitors to walk through their park. The park is represented by a network below, where each edge represents one-way tracks for visitors through the park. The direction of travel on each track is shown by an arrow. The numbers on the edges indicate the maximum number of people who are permitted to walk along each track each hour.')
  + I('ex4.png', 62) + q('a Starting at A, how many people are permitted to walk to G each hour?') + space(14, '10 + 9 + 21 = 40 people') + D
  + q('b Given that one group of nine people would like to walk from A to G together as a group, list all the different routes they could take so that the entire group of nine will stay together for the duration of their walk.')
  + space(10, 'A–B–C–G, A–D–G, A–D–F–G') + D + q('c What is the largest group of people that could walk through the koala sanctuary if they must stay together in a group for the entire duration of the walk?')
  + space(8, '13 people'),
  'You try 4', q('A wildlife park allows visitors to walk through the park along one-way tracks. The park is represented by the network below, where the direction of travel on each track is shown by an arrow. The numbers on the edges indicate the maximum number of people who are permitted to walk along each track each hour.')
  + G(yt4(ink=K), 62) + q('a Starting at A, how many people are permitted to walk to G each hour?') + space(14, 'Minimum cut C→G, D→G, D→F, A→E: 11 + 10 + 8 + 7 = 36 people') + D
  + q('b Given that one group of eight people would like to walk from A to G together as a group, list all the different routes they could take so that the entire group of eight will stay together for the duration of their walk.')
  + space(10, 'A–B–C–G, A–D–G, A–D–F–G') + D + q('c What is the largest group of people that could walk through the wildlife park if they must stay together in a group for the entire duration of the walk?')
  + space(8, '10 people (A–D–G)')))
P.append(exyt('Example 5 · Calculating maximum flow from more than one source',
  q('Water enters a network of pipes at either Source 1 or Source 2 and flows out at either Outlet 1 or Outlet 2.<br>The numbers next to the arrows represent the maximum rate, in kilolitres per minute, at which water can flow through each pipe.')
  + I('ex5.png', 78) + q('Determine the maximum rate, in kilolitres per minute, at which water can flow from these pipes into the ocean at Outlet 1 and Outlet 2.')
  + '<div class="solonly">' + I('ex5o1.png', 60) + I('ex5o2.png', 60) + '</div>'
  + space(24, 'Outlet 1: cuts 1200, 700, 800, 700, 700 → 700 kL/min<br>Outlet 2: cuts 700, 900, 900, 800, 900, 900 → 700 kL/min'),
  'You try 5', q('Water enters a network of pipes at either Source 1 or Source 2 and flows out at either Outlet 1 or Outlet 2.<br>The numbers next to the arrows represent the maximum rate, in kilolitres per minute, at which water can flow through each pipe.')
  + G(yt5(ink=K), 72) + q('Determine the maximum rate, in kilolitres per minute, at which water can flow from these pipes at Outlet 1 and at Outlet 2.')
  + space(24, 'Outlet 1: 350 + 250 = 600 kL/min<br>Outlet 2: 200 + 450 = 650 kL/min')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 1 Q2', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('The following directed graph shows the flow of water, in litres per minute, in a system of pipes connecting the source to the sink.') + q('The maximum flow, in litres per minute, from the source to the sink is')
  + mc(['10', '14', '18', '20', '22'], 'C') + why('minimum cut 2 + 10 + 6 = 18') + '</div>' + I('q14.png', 70) + '</div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q4b, c', q('A training program has a cricket team starting from exercise station S and running to exercise station O.<br>For safety reasons, the cricket coach has placed a restriction on the maximum number of people who can use the tracks in the fitness park.<br>The directed graph shows the capacity of the tracks, in number of people per minute.')
  + I('q15.png', 110) + q('When considering the possible flow of people through this network, many different cuts can be made.')
  + q('b. Determine the capacity of cut 1.') + space(8, '20 + 12 + 20 = 52') + D + q('c. What is the maximum flow from S to O, in number of people per minute?') + space(10, 'minimum cut S–M, T–U, R–Q: 20 + 10 + 20 = 50'), '2 marks'))
P.append(box('Exit task 3 · VCAA 2017 Exam 1 Q8', q('The flow of oil through a series of pipelines, in litres per minute, is shown in the following network.') + I('q16.png', 115)
  + q('The weightings of three of the edges are labelled <i>x</i>.<br>Five cuts labelled A–E are shown on the network.<br>The maximum flow of oil from the source to the sink, in litres per minute, is given by the capacity of')
  + mc(['cut A if <i>x</i> = 1', 'cut B if <i>x</i> = 2', 'cut C if <i>x</i> = 2', 'cut D if <i>x</i> = 3', 'cut E if <i>x</i> = 3'], 'B')
  + why('A = 25 + x, B = 23 + x, C = 24 + x, D = 32, E = 27: with x = 2, cut B (25) is the minimum'), '1 mark'))
SC = ['I can define and describe a directed graph.', 'I can determine the maximum flow for any section of sequential edges of a directed graph.',
      'I can determine cut capacities.', 'I can determine the maximum flow as equal to the minimum cut capacity.']
P.append(close(SC, [('14A', 'Q1–11')], ['14A']))
CSS_EXTRA = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
             'hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}</style>')
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-14a', '14A', 'AoS 4 · Networks and decision mathematics', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-14a-worksheet', '14A worksheet'), ('gm12-u4-14a-worksheet-solutions', '14A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
