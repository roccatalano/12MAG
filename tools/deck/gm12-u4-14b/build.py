"""Lesson gm12-u4-14b (14B Matching and allocation problems) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/14B slides.html      Run: python3 tools/deck/gm12-u4-14b/build.py      Screenshots: python3 tools/deck/gm12-u4-14b/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; VCAA figures cropped from the papers, fig/*.png):
- Do Now: VCAA 2025 Exam 1 Q36 (+ shared stem for Q36-37; A, 77%) · VCAA 2025 Exam 1 Q20 (A, 55%) ·
          VCAA 2024 Exam 2 Q14 stem + Q14a (46; average 0.8/1, 78%) · VCAA 2025 Exam 2 Q4 stem + Q4a (distance from city centre; 94%).
- APK: Cambridge U1&2 Ch 8 skills checklist #5 (p. 540; graph = checklist #1 graph; answer worked out: no printed answer) ·
       VCAA 2017 Exam 1 N&DM Q3 (original wording; = Edrolo U1&2 7B Q16, adapted there; A, 92% from the 2017 E1 report).
- Learn: Cambridge U3&4 14B pp. 674-678 (own words) · Edrolo U3&4 8G pp. 596-599.
- Worked examples: Cambridge U3&4 Example 6 (pp. 674-675); the Hungarian algorithm as worked in Cambridge's text (pp. 676-678,
  Wendy/Xenefon/Yolanda/Zelda; Cambridge has no numbered Example for it).
  You trys: Edrolo U3&4 8G Worked examples 1 (pp. 596-597), 2 (pp. 598-599, by inspection: no Cambridge Example), 3 (pp. 599-600).
- No CAS (card: none).
- Exits: VCAA 2016 Exam 1 N&DM Q1 (= Edrolo 8G Q10; B, 97%) · VCAA 2020 Exam 2 N&DM Q2 (= Edrolo 8G Q11; 57%) ·
         VCAA 2018 Exam 1 N&DM Q8 (= Edrolo 8G Q13; C, 24%). % from the examiner reports (2016 E1, 2020 E2, 2018 E1).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
from net import amat
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-14b')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'

# data
EX6_L = ['Nick', 'Maria', 'David', 'Subitha']; EX6_R = ['Greece', 'Malaysia', 'France', 'Brazil']
EX6_E = [('Nick', 'Greece'), ('Nick', 'Malaysia'), ('Nick', 'Brazil'), ('Maria', 'Greece'), ('Maria', 'France'), ('David', 'Malaysia'), ('Subitha', 'Malaysia'), ('Subitha', 'Brazil')]
EX6_A = {('Nick', 'Greece'), ('Maria', 'France'), ('David', 'Malaysia'), ('Subitha', 'Brazil')}
WE1_L = ['James', 'Alice', 'Harry', 'Nathan']; WE1_R = ['basketball', 'soccer', 'tennis', 'football']
WE1_E = [('James', 'basketball'), ('James', 'soccer'), ('James', 'tennis'), ('Alice', 'football'), ('Harry', 'soccer'), ('Harry', 'tennis'),
         ('Nathan', 'soccer'), ('Nathan', 'tennis'), ('Nathan', 'football')]
EMP = ['Wendy', 'Xenefon', 'Yolanda', 'Zelda']; MAC = ['A', 'B', 'C', 'D']
C0 = [[30, 40, 50, 60], [70, 30, 40, 70], [60, 50, 60, 30], [20, 80, 50, 70]]
C1 = [[0, 10, 20, 30], [40, 0, 10, 40], [30, 20, 30, 0], [0, 60, 30, 50]]
C2 = [[0, 10, 10, 30], [40, 0, 0, 40], [30, 20, 20, 0], [0, 60, 20, 50]]
C3 = [[0, 0, 0, 30], [50, 0, 0, 50], [30, 10, 10, 0], [0, 50, 10, 50]]
def R(names, M): return list(zip(names, M))
ACT = ['activity A', 'activity B', 'activity C', 'activity D']; PPL = ['Amy', 'Bryce', 'Cherry', 'Dinnith']
W0 = [[4, 4, 2, 4], [4, 3, 4, 5], [2, 5, 6, 3], [8, 7, 4, 6]]
W1 = [[2, 2, 0, 2], [1, 0, 1, 2], [0, 3, 4, 1], [4, 3, 0, 2]]
W2 = [[2, 2, 0, 1], [1, 0, 1, 1], [0, 3, 4, 0], [4, 3, 0, 1]]
W3 = [[1, 1, 0, 0], [1, 0, 2, 1], [0, 3, 5, 0], [3, 2, 0, 0]]
WE2 = [('Bryan', [1, 4, 7, 5]), ('Mason', [4, 5, 3, 7]), ('Lily', [2, 2, 3, 7]), ('Carmen', [8, 7, 6, 4])]
STG = ['planning', 'researching', 'writing', 'editing']

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.cmx td,.cmx th{line-height:1.25}'
     '.xs .R .wk li{font-size:15px}.L .q ul li{font-size:inherit!important;line-height:1.3!important}</style>']
S.append(title('14B', 'Matching and allocation problems', f'{CAM} · 14B Matching and allocation problems', 'gm12-u4-14b'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 14B', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>14B')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· two Year 11 questions', 'var(--apk)'),
  ('Bipartite graphs', '', None), ('Worked example 6', '→ You try', None), ('Allocation by inspection', '→ You try', None),
  ('The Hungarian algorithm', '', None), ('Worked example', '→ You try', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'),
  ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Bipartite graph', 'two groups of vertices; every edge joins one group to the other'), ('Allocation problem', 'match each person or machine to exactly one task'),
  ('Cost matrix', 'rows = people, columns = tasks, entries = cost (time, money …)'), ('By inspection', 'try the possible allocations; choose the smallest total'),
  ('Hungarian algorithm', 'row and column reductions, cover the zeros, adjust, allocate on the zeros'), ('Minimum cost', 'add the ORIGINAL costs of the allocation')],
  [('Lines = allocations', 'fewest lines to cover all zeros = number of rows → allocate', 'fewer lines → adjust'),
   ('Adjust', 'smallest uncovered value k: − k uncovered, + k covered twice', 'once-covered values stay'),
   ('Maximise', 'largest total wanted (scores)', 'check every allocation, or by inspection')],
  f'{CAM}, 14B pp. 674–678; {EDR}, 8G pp. 596–599; Study Design: use of a bipartite graph and its tabular or matrix form to represent a matching problem; '
  'determination of the optimum assignment(s) of people or machines to tasks by inspection or by use of the Hungarian algorithm'))

# ================= Do Now
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2025 Exam 1 Q36', 'Review of 14A (cut capacity)',
  ('<div style="font-size:20px">The network below shows the flow of water, in litres per minute, in a system of pipes connecting the source to the sink.</div>',
   Wd(460, img('dn1.png')), '<div style="font-size:20px">What is the capacity of Cut 1?</div>'),
  [('Cut edges', 'Cut 1 crosses 6 edges'), ('Direction', 'the 4 (pointing up) and the 6 (pointing down-left) flow back to the source side: count 0'),
   ('Add', '7 + 3 + 5 + 12 = 27')],
  'The capacity of Cut 1 is 27: <b>A</b>.', 'VCAA 2025 General Mathematics Exam 1 Q36 (examiner report: 77% correct)', mc=['27', '31', '33', '37'], key='A', stat=('mc', 77),
  dis=('C', '33 adds the backward 6: edges flowing towards the source count 0.')))
sm()
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2025 Exam 1 Q20', 'Review of 8C (unit cost depreciation)',
  '<div style="font-size:22px">Steve owns gardening equipment that had an initial value of $12 000.<br>He will use the unit cost method to depreciate the value of this equipment per hour used.<br>'
  'Steve uses the gardening equipment for 960 hours per year.<br>The value of the gardening equipment is $7680 after two years.<br>By what amount does the gardening equipment depreciate per hour used?</div>',
  [('Loss of value', '$12 000 − $7680 = $4320'), ('Hours used', '960 × 2 = 1920'), ('Per hour', '$4320 ÷ 1920 = $2.25')],
  'It depreciates by $2.25 per hour: <b>A</b>.', 'VCAA 2025 General Mathematics Exam 1 Q20 (examiner report: 55% correct)', mc=['$2.25', '$4.00', '$4.17', '$4.50'], key='A', stat=('mc', 55),
  dis=('D', '$4.50 divides the loss by 960 hours only: the value fell over TWO years.')))
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2024 Exam 2 Q14a', 'Review of 14A (cut capacity)',
  ('<div style="font-size:18px">A manufacturer (<i>M</i>) makes deliveries to the supermarket (<i>S</i>) via a number of storage warehouses, <i>L</i>, <i>N</i>, <i>O</i>, <i>P</i>, <i>Q</i> and <i>R</i>. These eight locations are represented as vertices in the network below.<br>'
   'The numbers on the edges represent the maximum number of deliveries that can be made between these locations each day.</div>', Wd(520, img('dn3.png')),
   '<div style="font-size:18px">a. When considering the possible flow of deliveries through this network, many different cuts can be made.<br><b>Determine</b> the capacity of Cut 1, shown above. <span class="muted">(1 mark)</span></div>'),
  [('Cut edges', '13, 7, 18, 6, 9'), ('Direction', 'the 7 runs from Q back to O: count 0'), ('Add', '13 + 18 + 6 + 9 = 46')],
  'The capacity of Cut 1 is <b>46</b>.', 'VCAA 2024 General Mathematics Exam 2 Q14 stem and Q14a (examiner report: average 0.8/1)', stat=('avg', 78), cmd=('Determine', 1, 'source → sink edges only')))
sm()
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2025 Exam 2 Q4a', 'Review of 3A (explanatory variable)',
  ('<div style="font-size:17px">The scatterplot below shows the sale price of a home, in dollars, against the distance of the home from the city centre of Melbourne, in kilometres, <i>distance from city centre</i>.<br>'
   'The sample consists of three-bedroom homes sold between 2016 and 2018.</div>', Wd(470, img('dn4.png')),
   '<div style="font-size:17px">The equation of the least squares line for the data in the scatterplot is<div style="text-align:center"><i>sale price</i> = 1 765 353 – 35 054 × <i>distance from city centre</i></div>'
   'The coefficient of determination is 0.0806<br>a. <b>Identify</b> the explanatory variable in the least squares equation. <span class="muted">(1 mark)</span></div>'),
  [('Equation', '<i>response</i> = <i>a</i> + <i>b</i> × <i>explanatory</i>'), ('Read off', 'the variable multiplied by the slope')],
  'The explanatory variable is <b>distance from city centre</b>.', 'VCAA 2025 General Mathematics Exam 2 Q4 stem and Q4a (examiner report: average 1.0/1)', stat=('avg', 94), cmd=('Identify', 1, 'name the variable')))
sm(extra='sm xs')

# ================= APK
AM = [[0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 1]]
S.append(qslide('apk', 'APK · Year 11 · Cambridge U1&amp;2 Ch 8 checklist #5', 'Adjacency matrices (Year 11)',
  ('<div style="font-size:22px"><b>Complete</b> the following matrix to represent the graph below.</div>', Wd(300, img('apk1.png')),
   amat(list('ABCDE'), [[''] * 5] * 5, fs=20)),
  [('Rows', 'one row and one column per vertex'), ('Edges', '<i>AB</i>, <i>AE</i>, <i>BE</i>, <i>BD</i>, <i>ED</i>, <i>DC</i>: a 1 in both matching cells'),
   ('Loops', 'loops at <i>C</i> and <i>E</i>: 1 on the diagonal')],
  '', f'{CAM12} · Ch 8 skills checklist #5, p. 540 (graph from checklist #1) · answer worked out (no printed answer)', cmd=('Complete', None, 'one entry per pair of vertices'),
  afig=amat(list('ABCDE'), AM, fs=20)))
S.append(qslide('apk', 'APK · VCAA 2017 Exam 1 Q3', 'Adjacency matrices (Year 11)',
  ('<div style="font-size:19px">Consider the following graph.</div>', Wd(250, img('apk2.png')),
   '<div style="font-size:17px">The adjacency matrix for this graph, with some elements missing, is shown below.'
   + amat(list('WXYZ'), [[1, '_', '_', '_'], ['_', 0, '_', '_'], ['_', '_', 0, '_'], ['_', '_', '_', 1]], fs=17)
   + 'This adjacency matrix contains 16 elements when complete.<br>Of the 12 missing elements</div>'),
  [('Count edges', 'W–X 2, W–Y 2, W–Z 1, X–Y 1, X–Z 1, Y–Z 1'), ('Twice each', 'every pair fills two cells: four 2s and eight 1s')],
  'Eight are ‘1’ and four are ‘2’: <b>A</b>.', f'VCAA 2017 Further Mathematics Exam 1 Networks and decision mathematics Q3 (examiner report: 92% correct) · {EDR12} 7B Q16 (adapted there)',
  mc=['eight are ‘1’ and four are ‘2’.', 'four are ‘1’ and eight are ‘2’.', 'six are ‘1’ and six are ‘2’.', 'two are ‘0’, six are ‘1’ and four are ‘2’.', 'four are ‘0’, four are ‘1’ and four are ‘2’.'],
  key='A', stat=('mc', 92)))
sm(extra='sm xs')

# ================= Learn 1: bipartite graphs
S.append(learn('Learn · 14B', 'Bipartite graphs and allocation',
  '<h4>Two groups, one match each</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a <b>bipartite graph</b> has two groups of vertices (e.g. people and tasks)</li><li>each edge joins a vertex in one group to a vertex in the other</li>'
  '<li><b>allocation</b>: match each person to exactly one task</li><li>start with a vertex that has only <b>one</b> edge: that match is forced</li></ul>',
  '<div style="display:flex;gap:26px;align-items:center;justify-content:center">' + Wd(380, bip([f'employee {i}' for i in range(1, 5)], [f'machine {i}' for i in range(1, 5)],
     [(f'employee {i}', f'machine {k}') for i in range(1, 5) for k in range(1, 5)], lw=105, rw=100, W=380)) + '<div style="width:340px">'
  + frag('Every employee can use every machine: a <b>complete</b> bipartite graph') + frag('Too many edges to weigh: put the costs in a table (cost matrix)') + '</div></div>',
  'Highlight the forced matches first, then cross out what they rule out.', f'{CAM}, 14B pp. 674–676 (own words; Cambridge’s employee–machine graph) · {EDR}, 8G p. 596',
  cards=(kcard('Bipartite graph', 'two groups; edges go across'), kcard('Allocation', 'one task each'))))
EXQ = ('<div style="font-size:18px">Nick, Maria, David and Subitha are presenters on a TV travel show. Each presenter will be assigned a story to film about one country that they have visited before.'
  '<ul style="margin-left:24px"><li>Nick has visited Greece, Malaysia and Brazil</li><li>Maria has visited Greece and France</li><li>Subitha has visited Malaysia and Brazil</li><li>David has visited Malaysia</li></ul>'
  '<b>Construct</b> a bipartite graph of the information above and use it to decide on the assignment of each presenter to one country.</div>')
S.append(qslide('we', 'Worked example 6 · 14B', 'Bipartite graphs and allocation', EXQ,
  [('Graph', 'presenters in one column, countries in the other; join each presenter to each country visited (picture)'),
   ('Forced', 'David has visited only Malaysia → David–Malaysia · only Maria has visited France → Maria–France'),
   ('Eliminate', 'Maria is used, so Greece → Nick · Subitha is left with Brazil')],
  'Nick: Greece · Maria: France · David: Malaysia · Subitha: Brazil.', f'{CAM} · Example 6 (pp. 674–675)', video='Cambridge GO · Example 6 (14B Resources)',
  made=Wd(300, bip(EX6_L, EX6_R, EX6_E, W=330, lw=80, rw=80)), afig=Wd(260, bip(EX6_L, EX6_R, EX6_E, hl=EX6_A, W=330, lw=80, rw=80)), cmd=('Construct', None, 'a vertex for each, an edge for each visit')))
sm()
S.append(qslide('yt', 'You try · Edrolo 8G WE1', 'Constructing a bipartite graph',
  '<div style="font-size:21px">A random survey of individuals’ sports preferences was conducted.<br>The results of 4 random individuals from the survey are shown in the following table. Use the information from the table to <b>construct</b> a bipartite graph.'
  '<table class="t" style="margin:10px auto;font-size:19px"><tr><th>individual</th><th>preferences</th></tr><tr><td>James</td><td>basketball, soccer, tennis</td></tr>'
  '<tr><td>Alice</td><td>football</td></tr><tr><td>Harry</td><td>soccer, tennis</td></tr><tr><td>Nathan</td><td>soccer, tennis, football</td></tr></table></div>',
  [('Two groups', '4 individuals in one column, 4 sports in the other'), ('Edges', 'one edge for each preference: 3 + 1 + 2 + 3 = 9 edges')],
  '', f'{EDR} · 8G Worked example 1 (pp. 596–597)', cmd=('construct', None, 'two columns, one edge per preference'),
  afig=Wd(330, bip(WE1_L, WE1_R, WE1_E, W=330, lw=75, rw=100))))

# ================= inspection
S.append(learn('Learn · 14B', 'Allocation by inspection',
  '<h4>Small problems: look for the best total</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>the <b>cost matrix</b>: rows = people, columns = tasks</li><li>find the cheapest person for each task</li>'
  '<li>if two tasks want the same person, give that person the task where they save the most</li><li>minimum cost = sum of the chosen entries</li></ul>',
  Wd(520, cm(MAC, R(EMP, C0), fs=19)) + frag('Cost matrix: minutes for each employee on each machine (Cambridge)'),
  'Small table (3 × 3): check every allocation. Bigger: use the Hungarian algorithm.', f'{CAM}, 14B p. 676 (own words) · {EDR}, 8G p. 597',
  cards=(kcard('By inspection', 'try the allocations'), kcard('Minimum cost', 'add the original costs'))))
S.append(qslide('yt', 'You try · Edrolo 8G WE2', 'Allocation by inspection (no Cambridge Example)',
  '<div style="font-size:20px">A university group assignment details a writing task on a research topic. The members in the group decide to split up the work based on which member was the most efficient at each task. '
  'Using inspection, <b>find</b> the minimum cost of the following cost matrix. The cost values are in hours.' + cm(STG, WE2, fs=19) + '</div>',
  [('Best per stage', 'planning: Bryan 1 · researching: Lily 2 · writing: Mason or Lily 3 · editing: Carmen 4'),
   ('Clash', 'Lily is best at researching, so Mason takes writing'), ('Add', '1 + 2 + 3 + 4 = 10')],
  'Bryan: planning, Lily: researching, Mason: writing, Carmen: editing. Minimum cost <b>10 hours</b>.', f'{EDR} · 8G Worked example 2 (pp. 598–599)',
  made=cm(STG, WE2, circ={(0, 0), (2, 1), (1, 2), (3, 3)}, fs=15), cmd=('find', None, 'cheapest for each task, then add')))
sm()

# ================= Hungarian
S.append(learn('Learn · 14B', 'The Hungarian algorithm',
  '<h4>Make zeros, then allocate on them</h4><ol style="font-size:17px;line-height:1.45;margin-left:24px">'
  '<li>subtract each <b>row</b>’s smallest value from that row</li><li>cover all zeros with the fewest lines: lines = rows? go to 6</li>'
  '<li>subtract each <b>column</b>’s smallest value (columns with no zero)</li><li>cover the zeros again: lines = rows? go to 6</li>'
  '<li>smallest uncovered value <i>k</i>: subtract <i>k</i> from uncovered, add <i>k</i> to values covered twice; repeat 4</li>'
  '<li>draw a bipartite graph of the zeros; allocate; add the <b>original</b> costs</li></ol>',
  '<div style="display:flex;gap:14px;align-items:center;justify-content:center">' + cm(MAC, R(EMP, C1), cover_c={0, 1, 3}, fs=17)
  + '<div style="width:260px">' + frag('Shaded = a covering line') + frag('3 lines but 4 allocations: not yet') + '</div></div>',
  'Lines go along whole rows or columns, never diagonally.', f'{CAM}, 14B pp. 676–678 (own words) · {EDR}, 8G pp. 597–598',
  cards=(kcard('Lines = allocations', 'then allocate'), kcard('Adjust', '− k uncovered, + k twice'))))
HQ = ('<div style="font-size:16px">The table shows the four employees: Wendy, Xenefon, Yolanda and Zelda. The machines in a factory are represented by the letters A, B, C and D.<br>'
      'The numbers in the table are the times, in minutes, it takes each employee to finish the task on each machine.' + cm(MAC, R(EMP, C0), fs=18)
      + 'The cost matrix can be used to determine the best way to allocate an employee to a machine so that the overall cost, in terms of the time taken to finish the work, is minimised. The Hungarian algorithm is used to do this.</div>')
S.append(qslide('we', 'Worked example · 14B (Cambridge text)', 'The Hungarian algorithm (part 1)', HQ,
  [('Step 1 · rows', 'subtract 30, 30, 30, 20' + cm(MAC, R(EMP, C1), fs=13)),
   ('Step 2 · lines', '3 lines cover the zeros; 4 needed' + cm(MAC, R(EMP, C1), cover_c={0, 1, 3}, fs=13)),
   ('Step 3 · columns', 'column C has no zero: subtract 10' + cm(MAC, R(EMP, C2), fs=13))],
  '', f'{CAM} · 14B pp. 676–677 (the Hungarian algorithm, worked in the text: no numbered Example)', video='Cambridge GO · 14B Resources'))
sm(extra='sm xs')
S.append(qslide('we', 'Worked example · 14B (Cambridge text)', 'The Hungarian algorithm (part 2)', HQ,
  [('Step 4 · lines', 'still 3 lines' + cm(MAC, R(EMP, C2), cover_r={1}, cover_c={0, 3}, fs=13)),
   ('Step 5 · adjust', 'smallest uncovered 10: −10 uncovered, +10 at Xenefon–A and Xenefon–D' + cm(MAC, R(EMP, C3), cover_r={0, 1}, cover_c={0, 3}, fs=13)),
   ('Step 6 · allocate', 'Zelda–A, Yolanda–D forced; Wendy and Xenefon share B and C')],
  'Zelda: A, Yolanda: D, Wendy: B or C, Xenefon: the other. Minimum time 20 + 30 + 50 + 30 = <b>130 minutes</b> (both allocations).',
  f'{CAM} · 14B pp. 677–678 (the Hungarian algorithm, worked in the text: no numbered Example)', video='Cambridge GO · 14B Resources'))
sm(extra='sm xs')
WQ = ('<div style="font-size:20px">Using the Hungarian algorithm, <b>find</b> the minimum cost of the following cost matrix. The cost values are in hours.'
      + cm(ACT, R(PPL, W0), fs=19) + '</div>')
S.append(qslide('yt', 'You try · Edrolo 8G WE3', 'Using the Hungarian algorithm (part 1)', WQ,
  [('Step 1 · rows', 'subtract 2, 3, 2, 4' + cm(['A', 'B', 'C', 'D'], R(PPL, W1), fs=13)),
   ('Step 2 · lines', '3 lines; 4 needed' + cm(['A', 'B', 'C', 'D'], R(PPL, W1), cover_c={0, 1, 2}, fs=13)),
   ('Step 3 · columns', 'column D: subtract 1' + cm(['A', 'B', 'C', 'D'], R(PPL, W2), fs=13))],
  '', f'{EDR} · 8G Worked example 3 (pp. 599–600)', cmd=('find', None, 'Hungarian algorithm, then add original costs')))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8G WE3', 'Using the Hungarian algorithm (part 2)', WQ,
  [('Step 4 · lines', 'still 3 lines' + cm(['A', 'B', 'C', 'D'], R(PPL, W2), cover_r={1, 2}, cover_c={2}, fs=13)),
   ('Step 5 · adjust', 'smallest uncovered 1: −1 uncovered, +1 covered twice; now 4 lines' + cm(['A', 'B', 'C', 'D'], R(PPL, W3), cover_r={1, 2}, cover_c={2, 3}, fs=13)),
   ('Allocate', 'Cherry: A · Bryce: B · Amy and Dinnith: C and D either way'),
   ('Original costs', '2 + 3 + 2 + 6 = 13 or 2 + 3 + 4 + 4 = 13')],
  'Minimum cost <b>13 hours</b>.', f'{EDR} · 8G Worked example 3 (pp. 599–600)', cmd=('find', None, 'Hungarian algorithm, then add original costs')))
sm(extra='sm xs')

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2016 Exam 1 Q1', 'Show what you know',
  ('<div style="font-size:20px">Lee, Mandy, Nola, Oscar and Pieter are each to be allocated one particular task at work.<br>The bipartite graph below shows which task(s), 1–5, each person is able to complete.</div>',
   Wd(400, img('q10.png')), '<div style="font-size:20px">Each person completes a different task.<br>Task 4 must be completed by</div>'),
  [('Forced', 'Oscar → Task 3 only · Pieter → Task 5 only'), ('Then', 'Nola: Tasks 2, 5 → Task 2 · Mandy: Task 4 only'), ('Left', 'Lee → Task 1')],
  'Mandy: <b>B</b>.', f'VCAA 2016 Further Mathematics Exam 1 Networks and decision mathematics Q1 (examiner report: 97% correct) · {EDR} 8G Q10',
  mc=['Lee.', 'Mandy.', 'Nola.', 'Oscar.', 'Pieter.'], key='B', stat=('mc', 97)))
sm()
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2020 Exam 2 Q2', 'Show what you know',
  '<div style="font-size:19px">A cricket team has 11 players who are each assigned to a batting position.<br>Three of the new players, Alex, Bo and Cameron, can bat in position 1, 2 or 3.<br>'
  'The table below shows the average scores, in runs, for each player for the batting positions 1, 2 and 3.' + cm(['1', '2', '3'], [('Alex', [22, 24, 24]), ('Bo', [25, 25, 21]), ('Cameron', [24, 25, 19])], fs=19)
  + 'Each player will be assigned to one batting position.<br>To which position should each player be assigned to <b>maximise</b> the team’s score? Write your answer in the table below. <span class="muted">(1 mark)</span>'
  '<table class="t" style="margin:6px auto;font-size:17px"><tr><th>Player</th><th>Batting position</th></tr><tr><td>Alex</td><td></td></tr><tr><td>Bo</td><td></td></tr><tr><td>Cameron</td><td></td></tr></table></div>',
  [('Maximise', 'largest total, not the Hungarian minimum'), ('Position 3', 'Alex 24 is far better than 21 or 19: Alex → 3'), ('Positions 1, 2', 'Bo 1 + Cameron 2 = 50 (Bo 2 + Cameron 1 = 49)'),
   ('Total', '24 + 25 + 25 = 74')],
  'Alex: <b>3</b> · Bo: <b>1</b> · Cameron: <b>2</b>.', f'VCAA 2020 Further Mathematics Exam 2 Networks and decision mathematics Q2 (examiner report: average 0.6/1) · {EDR} 8G Q11',
  stat=('avg', 57), cmd=('maximise', 1, 'largest total score')))
sm(extra='sm xs')
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2018 Exam 1 Q8', 'Show what you know',
  '<div style="font-size:15px">Annie, Buddhi, Chuck and Dorothy work in a factory.<br>Today each worker will complete one of four tasks, 1, 2, 3 and 4.<br>The usual completion times for Annie, Chuck and Dorothy are shown in the table below.'
  + cm(['Task 1', 'Task 2', 'Task 3', 'Task 4'], [('Annie', [7, 3, 8, 2]), ('Buddhi', ['<i>k</i>', '<i>k</i>', 3, '<i>k</i>']), ('Chuck', [5, 6, 9, 2]), ('Dorothy', [4, 8, 5, 3])], fs=16)
  + 'Buddhi takes 3 minutes for Task 3.<br>He takes <i>k</i> minutes for each other task.<br>Today the factory supervisor allocates the tasks as follows:'
  '<ul style="margin-left:24px;font-size:15px;columns:2"><li>Task 1 to Dorothy</li><li>Task 2 to Annie</li><li>Task 3 to Buddhi</li><li>Task 4 to Chuck</li></ul>'
  'This allocation will achieve the minimum total completion time if the value of <i>k</i> is at least</div>',
  [('Supervisor', '4 + 3 + 3 + 2 = 12 minutes'), ('Rival', 'Buddhi: Task 1 (<i>k</i>), Annie: 2 (3), Dorothy: 3 (5), Chuck: 4 (2) = <i>k</i> + 10'),
   ('Need', '<i>k</i> + 10 ≥ 12 → <i>k</i> ≥ 2 (other allocations cost more)')],
  '<i>k</i> is at least 2: <b>C</b>.', f'VCAA 2018 Further Mathematics Exam 1 Networks and decision mathematics Q8 (examiner report: 24% correct) · {EDR} 8G Q13',
  mc=['0', '1', '2', '3', '4'], key='C', stat=('mc', 24), dis=('E', '34% chose E: k = 4 works, but the question asks for the SMALLEST k that still makes this allocation minimal.')))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 14 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '14B' and v.get('url')]))
n = assemble(S, '12MAG · 14B · Matching and allocation problems', os.path.join(ROOT, 'lessons', '14B slides.html'))
print(n - 1, 'slides')
