# Chapter 13 revision booklet: Insight GM1 Unit 4 (MC) + GM2 Unit 4 (SA), section 'Networks and decision mathematics—
# Undirected graphs and networks: travelling and connecting problems' (GM1 Q1-22, printed pp.18-23 = pdf 19-24;
# GM2 Q1-8, printed pp.21-28 = pdf 22-29), plus GM1 directed-graphs section Q4 (shortest path, p.24).
# Questions are scans of the Insight pages (crop.py -> crops/*.png), so they are verbatim. Answers from Insight's
# explanatory notes / worked solutions (GM1 pp.40-44, GM2 pp.47-50). Insight is never burnt.
# Left out (Chapter 14): GM1 Q19 (Hungarian allocation) and the rest of the directed section (flow, matching, critical path).
G1 = 'Insight GM1 Unit 4'
G2 = 'Insight GM2 Unit 4'


def MC(n, sub, page, key, a, why):
    return dict(kind='mc', n=n, sub=sub, stem=f'[[{key}]]', opts=None, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}')


def SA(n, sub, page, parts, why=None, note=None, stem=None):
    stem = f'[[g2q{n}]]' if stem is None else stem
    ps = [('', f'[[{k}]]', ans, sp, mk) for k, ans, sp, mk in parts]
    return dict(long=False, kind='sa', n=n, sub=sub, marks=sum(p[4] for p in ps), stem=stem, parts=ps, why=why, note=note, src=f'{G2} p.{page} Q{n}')


SUBS = [('13A', 'Graphs and networks'), ('13B', 'Adjacency matrices'), ('13C', 'Exploring and travelling'),
        ('13D', 'Weighted graphs and networks'), ('13E', 'Dijkstra’s algorithm'), ('13F', 'Trees and minimum connector problems')]
EMPTY = {}

Q = [
 # 13A
 MC(4, '13A', 19, 'g1q4', 'D', 'A simple graph has no loops or multiple edges: A and C have a loop, B and E have multiple edges.'),
 MC(6, '13A', 20, 'g1q6', 'C', 'Euler’s formula v − e + f = 2: v − 21 + 17 = 2, so v = 6.'),
 MC(9, '13A', 20, 'g1q9', 'D', 'v − e + f = 2: 4 − 6 + 4 = 2 (the other options do not give 2).'),
 MC(10, '13A', 20, 'g1q10', 'C', 'A planar graph can be redrawn with no edges crossing; this cannot be done for C.'),
 MC(12, '13A', 21, 'g1q12', 'A', 'Removing a bridge leaves the graph no longer connected: the middle edge in A.'),
 MC(15, '13A', 21, 'g1q15', 'C', 'v + f − e = 2: v + 5 − 7 = 2, so v = 4.'),
 MC(20, '13A', 23, 'g1q20', 'B', 'Removing BC leaves vertex C unconnected to the rest of the graph.'),
 MC(22, '13A', 23, 'g1q22', 'C', 'Complete graph: edges = n(n − 1)/2 = 7 × 6/2 = 21.'),
 # 13B
 MC(5, '13B', 19, 'g1q5', 'D', 'Multiple edges are counted (not only 1s and 0s), no loops so the diagonal is all 0s, and the C–E edge must be there: D.'),
 MC(18, '13B', 22, 'g1q18', 'A', 'B misses the loop at A; C misses one of the three A–D edges; D misses both; E has only one B–D edge.'),
 SA(8, '13B', 28, stem='', parts=[('g2q8', 'Add the three missing edges: D–H, D–R and a second W–R edge (W–R = 2 in the matrix).', 10, 1)]),
 # 13C
 MC(1, '13C', 18, 'g1q1', 'A', 'A trail is a walk with no repeated edges; this walk repeats a vertex but no edge.'),
 MC(2, '13C', 18, 'g1q2', 'E', 'A and E have odd degree (3); an edge between them makes every degree even, so an Eulerian circuit exists.'),
 MC(7, '13C', 20, 'g1q7', 'D', 'A–F–E–C–D–B–A uses an edge for every step and visits each vertex once (A: no A–C edge; B: no D–E; C: no E–B; E: no A–C).'),
 MC(11, '13C', 20, 'g1q11', 'E', 'A, B, E, F are odd (degree 3). An edge between two of them leaves exactly two odd vertices (trail possible); an edge B–G makes G odd: 3 odd vertices, still no trail.'),
 MC(13, '13C', 21, 'g1q13', 'C', 'Adding AB makes every degree even (Euler circuit); an Euler trail needs exactly two odd vertices.'),
 MC(16, '13C', 22, 'g1q16', 'B', 'ABDECF visits every vertex once. A: no C–D edge; C, D repeat vertices; E returns to A (a cycle).'),
 MC(17, '13C', 22, 'g1q17', 'E', 'Not true: the sum of the degrees is 28 (= 2 × 14 edges), not 26. A–D are true.'),
 MC(21, '13C', 23, 'g1q21', 'A', 'F–B–A–E–D–F–B–F–C–D–C repeats edge FB and uses F–C, which is not an edge.'),
 SA(3, '13C', 23, [('g2q3a', '4 (Filter 1, D, C and E)', 5, 1),
                   ('g2q3b', 'Between any two of the four odd vertices (Filter 1, D, C, E): Filter 1 to D, Filter 1 to E, Filter 1 to C, D to C, D to E or E to C.', 6, 1),
                   ('g2q3c', 'Any path that passes through each vertex exactly once (other solutions exist; Insight GM2 p.48 draws one).', 3, 1)]),
 SA(5, '13C', 25, [('g2q5a', 'fruit products and soft drinks', 5, 1),
                   ('g2q5bi', 'An Eulerian cycle needs every vertex to have even degree; the chocolaterie and the olive grove have degree 3.', 6, 1),
                   ('g2q5bii', 'Between the chocolaterie and the olive grove.', 5, 1),
                   ('g2q5biii', 'A Hamiltonian cycle: starts and ends at the tour company office and visits each food location exactly once (Insight GM2 p.49 draws one).', 2, 1)]),
 # 13D
 SA(1, '13D', 21, [('g2q1a', 'A – F – E (1400 + 750 = 2150 m; A–C–F–E 2600, A–D–E 2200, A–B–D–E 2850)', 6, 1),
                   ('g2q1b', 'B – A – C – F – E – D – B (or B – D – E – F – C – A – B)', 5, 1),
                   ('g2q1c', 'Every vertex must have even degree for an Eulerian circuit; F and D have degree 3 (odd).', 6, 1),
                   ('g2q1d', 'Start at D and finish at F (or start at F, finish at D): the two odd vertices.', 5, 1)]),
 # 13E
 MC(4, '13E', 24, 'g1d4', 'C', 'Dijkstra from A: F = 45 (A–F), C = 47, B = 67, then D = 45 + 38 = 83 (A–F–D).'),
 # 13F
 MC(3, '13F', 19, 'g1q3', 'D', 'Prim’s algorithm gives the minimum spanning tree shown in Insight’s solution; C–G (72 m) is not used.'),
 MC(8, '13F', 20, 'g1q8', 'A', 'Prim’s algorithm: 15 + 6 + 13 + 9 + 7 + 8 + 12 + 8 = 78.'),
 MC(14, '13F', 21, 'g1q14', 'D', '10 vertices so a spanning tree has 9 edges and no circuit: B and E contain a circuit; A and C miss a vertex.'),
 SA(2, '13F', 22, [('g2q2a', 'e.g. C – B – A – D – H – G – F – E – C, total 5250 m (or C – G – H – D – A – B – F – E – C, 6925 m). Any circuit through every vertex once, with its correct total.', 7, 2),
                   ('g2q2b', 'An Euler trail needs exactly 0 or 2 odd vertices; this network has more than 2 vertices of odd degree.', 6, 1),
                   ('g2q2c', 'Minimum spanning tree with edges 525, 850, 475, 750, 350, 625 and 300 m (Insight GM2 p.47 draws it).', 2, 1),
                   ('g2q2cii', '525 + 850 + 475 + 750 + 350 + 625 + 300 = 3875 m', 4, 1)]),
 SA(4, '13F', 24, [('g2q4a', 'Filter 1 – B – E – Filter 2 (4 + 3 + 5 = 12 s)', 5, 1),
                   ('g2q4b', 'Minimum spanning tree reaching every filter (Insight GM2 p.48 draws it).', 2, 1)]),
 SA(6, '13F', 26, [('g2q6a', '3 roads: gate – park, and houses – tennis court – villas', 5, 1),
                   ('g2q6b', '2 roads between gate – park and houses – villas (or a combination of those 4 locations): gate has degree 1, park, houses and villas degree 3.', 5, 1),
                   ('g2q6c', 'gate – park – townhouses – playground – houses: 50 + 170 + 260 + 280 = 760 m', 2, 1),
                   ('g2q6d', 'Edges not in the minimum spanning tree: 180 + 170 + 160 + 260 + 280 + 230 = 1280 m saved', 5, 1)]),
 SA(7, '13F', 27, [('g2q7a', '8 faces (including the space around the outside)', 4, 1),
                   ('g2q7b', 'Depot – D – F – J – I – H – G – E – B – A – C – Depot (or the reverse)', 5, 1),
                   ('g2q7c', 'A – D – Depot – I – H = 25 km', 4, 1),
                   ('g2q7d', '58 km', 5, 1)]),
]
