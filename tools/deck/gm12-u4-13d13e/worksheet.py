"""Lesson gm12-u4-13d13e (13D weighted graphs, 13E Dijkstra's algorithm) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 13D/13E).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #14 (p. 542) · VCAA 2020 Exam 2 N&DM Q3a (Edrolo U1&2 7E Q14).
Example 9-10 = Cambridge U3&4 Examples 9 (p. 634) and 10 (pp. 638-639). You try 9 = Edrolo U3&4 8F WE1 (p. 585) · You try 10 = 8F WE2 (pp. 588-589).
Exits = VCAA 2018 Exam 1 N&DM Q2 (Edrolo 8F Q10) · VCAA 2017 Exam 2 N&DM Q1b (Edrolo 8F Q11).
Graphs redrawn with tools/deck/tpl/net.py (same vertices, edges and weights).
Output: lessons/13D-13E worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-13d13e/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
K = '#111'
def G(svg, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{svg}</div>'
def solonly(svg): return svg.replace('class="hid0"', 'class="solonly"')
WT = table([['', 'P', 'B', 'M', 'C', 'E'], ['G', '1', 'X', '4', '7', '9'], ['P', '1', '7', '4', '7', '9'], ['M', '1', '5', '4', '6', '9'],
            ['B', '1', '5', '4', '6', '7'], ['C', '1', '5', '4', '6', '7']], style='margin:1mm auto;font-size:9pt')

P = [title('13D–13E', 'Shortest paths and Dijkstra’s algorithm')]
P.append(lis(['To be able to analyse a weighted graph.', 'To be able to find the shortest path between two vertices for a network.',
              'To be able to use Dijkstra’s algorithm to find the shortest path between two vertices.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('For the graph below, find the length of the shortest path from Home to School.') + G(hschool(ink=K), 90)
             + space(14, '17 (Home – bottom-left vertex – middle vertex – top vertex – School: 5 + 2 + 2 + 4 + 4)')))
TP = table([['Training program number', 'Training details'], ['1', 'The team must run to exercise station <i>O</i>.'], ['2', 'The team must run along all tracks just once.'],
            ['3', 'The team must visit each exercise station and return to exercise station <i>S</i>.']], style='font-size:9pt;margin:1mm 0')
P.append(box('Question 2 · VCAA 2020 Exam 2 Q3a', q('A local fitness park has 10 exercise stations: <i>M</i> to <i>V</i>.<br>The edges on the graph below represent the tracks between the exercise stations.<br>The number on each edge represents the length, in kilometres, of each track.')
  + G(fpark(ink=K), 88) + q('The Sunny Coast cricket coach designs three different training programs, <b>all starting at exercise station <i>S</i></b>.') + TP
  + q('What is the shortest distance, in kilometres, covered in training program 1?') + space(10, '3.2 km (S–T–U–V–O: 0.6 + 1.2 + 0.6 + 0.8)'), '1 mark'))
P.append(sect('13D Weighted graphs and networks', 'Example, then you try'))
P.append(exyt('Example 9 · Finding the shortest path from one vertex to another',
  q('Find the shortest path from Bartow to Kenton in the network shown below.') + G(crog(ink=K), 72)
  + space(34, 'B–S–M–O–K: 7 + 8 + 5 + 11 = 31 km<br>B–S–M–K: 7 + 8 + 13 = 28 km<br>B–S–O–K: 7 + 9 + 11 = 27 km<br>The shortest path from Bartow to Kenton is 27 km with route B–S–O–K.'),
  'You try 9', q('The weighted graph shown displays the distance, in kilometres, between six train stations.<br>Find the length and route of the shortest path from Daylington to Eastborough by eye.')
  + G(trains(ink=K), 72) + space(30, 'D–H–E 15 · D–M–E 18 · D–M–T–E 24 · D–B–H–E 13<br>13 km, Daylington–Beachmore–Halville–Eastborough')))
P.append(sect('13E Dijkstra’s algorithm', 'Example, then you try'))
P.append(exyt('Example 10 · Using Dijkstra’s algorithm (graphical method)',
  q('Find the shortest path from <i>A</i> to <i>F</i> in the weighted graph shown below.') + G(solonly(ex10(ink=K)), 78)
  + space(22, 'Labels: A 0, B 2, C 6 → 4, E 4, D 5, F 7 (circled in that order).<br>Backtrack: 7 − 3 = 4 (E), 4 − 2 = 2 (B), 2 − 2 = 0 (A).<br>The shortest path from A to F is A–B–E–F with a length of 7.'),
  'You try 10', q('Reuben is struggling to find his way around his new school and is constantly running late. Luckily his friend in General Maths drew him a weighted graph of the school, representing the time it takes, in minutes, to walk to each class.<br>Find the time and route of the shortest path from General (G) to English (E).')
  + G(school(ink=K), 78) + space(44, WT + '7 minutes, General–Methods–Biology–English')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q2', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('Niko drives from his home to university.<br>The network below shows the distances, in kilometres, along a series of streets connecting Niko’s home to the university.<br>The vertices <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i> represent the intersection of these streets.')
  + q('The shortest path for Niko from his home to the university could be found using')
  + mc(['a minimum cut.', 'Prim’s algorithm.', 'Dijkstra’s algorithm.', 'critical path analysis.', 'the Hungarian algorithm.'], 'C')
  + why('shortest path between two vertices on a weighted graph') + '</div>' + G(niko(ink=K), 80) + '</div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2017 Exam 2 Q1b', q('Bus routes connect six towns.<br>The towns are Northend (<i>N</i>), Opera (<i>O</i>), Palmer (<i>P</i>), Quigley (<i>Q</i>), Rosebush (<i>R</i>) and Seatown (<i>S</i>).<br>'
  'The graph below gives the cost, in dollars, of bus travel along these routes.<br>Bai lives in Northend (<i>N</i>) and he will travel by bus to take a holiday in Seatown (<i>S</i>).')
  + G(bus(ink=K), 62) + q('If Bai takes the cheapest route from Northend (<i>N</i>) to Seatown (<i>S</i>), which other town(s) will he pass through?')
  + space(12, 'Quigley (Q) and Rosebush (R): N–Q–R–S costs $80'), '1 mark'))
SC = [x for x in ['I can define a weighted graph.', 'I can calculate the shortest path from one vertex to another by inspection.',
                  'I can calculate the shortest path from one vertex to another using Dijkstra’s algorithm.']]
P.append(close(SC, [('13D', 'Q1–9'), ('13E', 'Q1–2')], ['13D–13E']))
CSS_EXTRA = '<style>.solonly{display:none}.sol .solonly{display:inline}.box svg{max-width:100%}</style>'
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-13d13e', '13D–13E', 'AoS 4 · Networks and decision mathematics', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-13d13e-worksheet', '13D-13E worksheet'), ('gm12-u4-13d13e-worksheet-solutions', '13D-13E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
