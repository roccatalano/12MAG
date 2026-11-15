"""CONTENT for CFAT 4.13.1 (Cambridge 13A-13B), CFAT 4.13.2 (13C-13E), CFAT 4.13.3 (13F). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no exam practice / VCAA reprints). Edrolo Ch 8 = Cambridge Ch 13
(8A -> 13A, 8B -> 13B, 8C -> 13C, 8F Q1-3 -> 13D, 8F Q4-9 -> 13E, 8D -> 13F; tools/y12_edrolo_exercise_questions.csv).
Graphs/options are CROPPED from the Edrolo PDF by crop.py (PDF pp. 533, 535, 546-547, 562-564, 574-576, 597-600 =
printed 526-593); short stems/part text typed verbatim. Answers from the Edrolo answer pages (PDF pp. 730-736, 739 =
printed 723-732). 'Answers may vary' drawings are given as edge lists. Marks set by Claude.

CFAT 4.13.1 (13 marks, start of lesson gm12-u4-13c): MC 8A Q1, 8A Q5, 8A Q11, 8B Q1; SA 8A Q3, 8B Q2, 8B Q4.
CFAT 4.13.2 (12 marks, start of lesson gm12-u4-13f): MC 8C Q1, 8C Q4, 8C Q8, 8F Q1, 8F Q6; SA 8C Q3, 8C Q6, 8F Q3, 8F Q8.
CFAT 4.13.3 (12 marks, start of the Ch 13 test lesson gm12-ch13-test): MC 8D Q1, 8D Q5; SA 8D Q2, 8D Q3, 8D Q6, 8D Q7, 8D Q8.
Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

def mc(src, fig, w, ans): return dict(src='Edrolo ' + src, fig=fig, w=w, ans=ans)

CFATS = [
 dict(id='CFAT 4.13.1', subs='13A-13B', title='Graphs, Euler’s rule and adjacency matrices',
  layout=[('full', 0), ('full', 1), ('full', 2), ('full', 3)],
  mc=[mc('8A Q1', '8A_Q1', 15, 3), mc('8A Q5', '8A_Q5', 15, 2), mc('8A Q11', '8A_Q11', 12, 2), mc('8B Q1', '8B_Q1', 11, 2)],
  sa=[
   dict(src='Edrolo 8A Q3', stem='Consider the following graph.', fig='8A_Q3', w=5,
        parts=[('a.', 'How many vertices does it contain?', 1, '6'), ('b.', 'What is the degree of vertex C?', 1, '3'),
               ('c.', 'What is the degree of vertex D?', 1, '3'), ('d.', 'What is the degree of vertex E?', 1, '5'),
               ('e.', 'How many faces are there in this graph?', 1, '6'), ('f.', 'Is there a bridge in this graph? If so, which vertices does it connect to?', 1, 'No')]),
   dict(src='Edrolo 8B Q2', stem='Construct an adjacency matrix from the following graphs.', fig='8B_Q2', w=12,
        parts=[('a.', '', 1, '    A B C D\nA [0 1 0 1]\nB [1 0 1 0]\nC [0 1 0 1]\nD [1 0 1 0]'),
               ('b.', '', 1, '    A B C D\nA [0 1 0 0]\nB [1 0 1 0]\nC [0 1 0 1]\nD [0 0 1 0]')]),
   dict(src='Edrolo 8B Q4', stem='Harry Potter can’t seem to remember how to draw the symbol of the Deathly Hallows.\nCreate an adjacency matrix that will help Harry remember which vertices are connected.', fig='8B_Q4', w=4.5,
        parts=[('', '', 1, '    A B C D\nA [0 1 1 1]\nB [1 0 1 0]\nC [1 1 1 1]\nD [1 0 1 0]')]),
  ]),
 dict(id='CFAT 4.13.2', subs='13C-13E', title='Walks, Eulerian and Hamiltonian paths, shortest paths',
  layout=[([0], [1]), ([2], [3]), ('full', 4)],
  mc=[mc('8C Q1', '8C_Q1', 9.5, 1), mc('8C Q4', '8C_Q4', 9.5, 1), mc('8C Q8', '8C_Q8', 9.5, 2), mc('8F Q1', '8F_Q1', 9.5, 0), mc('8F Q6', '8F_Q6', 10, 2)],
  sa=[
   dict(src='Edrolo 8C Q3', stem='Chelsea is going for a walk around her neighbourhood. She wants to make sure she starts and ends at her house and does not walk along any of the roads more than once. She likes her walks to be interesting, so she also does not want to visit any of the intersections more than once. What type of walk is Chelsea hoping to take?',
        parts=[('', '', 1, 'Cycle')]),
   dict(src='Edrolo 8C Q6', stem='Consider the following graph.', fig='8C_Q6', w=5.5,
        parts=[('a.', 'Add one edge to the graph to make an Eulerian circuit possible.', 1, 'Add an edge between B and G.'),
               ('b.', 'Write down a possible Eulerian circuit.', 1, 'A–B–C–D–E–A–F–G–D–B–G–A (answers may vary)')]),
   dict(src='Edrolo 8F Q3', stem='Fiona is preparing for her first day at her new school, and is planning on walking to school. The given weighted network shows the distance, in kilometres, of the roads between her house and her school. Intersections are labelled A–F.', fig='8F_Q3', w=5,
        parts=[('a.', 'Fiona decides to walk to school via the route home–A–C–D–E–school. What distance will she walk?', 1, '1.65 km'),
               ('b.', 'Find, by inspection, the shortest distance that Fiona can walk to school.', 1, '1.15 km')]),
   dict(src='Edrolo 8F Q8', stem='During an orienteering task at a school camp, students are given a map and are tasked with getting to point X in the shortest time possible. One group of students converted the map into the following weighted network diagram. Each weight represents the time, in minutes, it would take to travel down the path.', fig='8F_Q8', w=5.5,
        parts=[('a.', 'What is the shortest possible time it would take the students to get from the start to point X?', 1, '16 minutes'),
               ('b.', 'What is the route of the shortest path?', 1, 'start–C–E–H–X')]),
  ]),
 dict(id='CFAT 4.13.3', subs='13F', title='Trees, spanning trees and minimum spanning trees',
  layout=[([0], [1])],
  mc=[mc('8D Q1', '8D_Q1', 9.5, 2), mc('8D Q5', '8D_Q5', 8, 3)],
  sa=[
   dict(src='Edrolo 8D Q2', stem='Consider the following weighted graph.', fig='8D_Q2', w=4,
        parts=[('a.', 'How many vertices and edges will a spanning tree of the weighted graph contain?', 1, '5 vertices, 4 edges'),
               ('b.', 'Find a possible spanning tree within the weighted graph.', 1, 'e.g. edges 4, 3, 2 and 5 (no loop, one of the two 2s; answers may vary)'),
               ('c.', 'Calculate the weight of the spanning tree found in part a.', 1, '14 (for the tree above)')]),
   dict(src='Edrolo 8D Q3', stem='How many edges need to be removed from the following graph in order to create a spanning tree?', fig='8D_Q3', w=4.5,
        parts=[('', '', 1, '6')]),
   dict(src='Edrolo 8D Q6', stem='Draw the minimum spanning tree of the following weighted graph.', fig='8D_Q6', w=3.6,
        parts=[('', '', 1, 'Edges 9, 10, 13, 14 and 18 (total weight 64)')]),
   dict(src='Edrolo 8D Q7', stem='Calculate the weight of the minimum spanning tree for each of the following graphs.', fig='8D_Q7', w=7,
        parts=[('a.', '', 1, '10'), ('b.', '', 1, '110'), ('c.', '', 1, '35')]),
   dict(src='Edrolo 8D Q8', stem='Since transportation dust has been discovered, Dragonride Services have been going out of business. In an effort to save some gold, they have decided to cut down on some of their flight paths.', fig='8D_Q8', w=6,
        parts=[('a.', 'Draw the flight map with the shortest possible flight distance that still accesses all of the landmarks.', 1, 'Troll Village–Fairy Tree 8, Fairy Tree–Dragonstone 6, Dragonstone–Siren Bay 11, Dragonstone–Niffler cafe 9, Niffler cafe–Witch Castle 19, Fairy Tree–Elf Palace 19'),
               ('b.', 'What is the total distance of the flight map?', 1, '72 km')]),
  ]),
]
