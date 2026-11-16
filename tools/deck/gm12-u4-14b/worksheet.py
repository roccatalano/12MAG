"""Lesson gm12-u4-14b (14B Matching and allocation problems) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet, as in earlier lessons; no CAS for 14B).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 8 skills checklist #5 (p. 540) · VCAA 2017 Exam 1 N&DM Q3 (Edrolo U1&2 7B Q16).
Example 6 = Cambridge U3&4 Example 6 (pp. 674-675) · Example (unnumbered) = the Hungarian algorithm worked in Cambridge's text (pp. 676-678).
You try 1-3 = Edrolo U3&4 8G WE1 (pp. 596-597), WE2 (pp. 598-599, inspection: no Cambridge Example, so a You try on its own), WE3 (pp. 599-600).
Exits = VCAA 2016 Exam 1 N&DM Q1 (Edrolo 8G Q10) · VCAA 2020 Exam 2 N&DM Q2 (8G Q11) · VCAA 2018 Exam 1 N&DM Q8 (8G Q13).
Output: lessons/14B worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-14b/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
import figs as Fg
from figs import img, bip
from net import amat
K = '#111'
def G(html, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{html}</div>'
def I(name, mm): return G(img(name), mm)
def ST(stu, sol, mm): return f'<div class="stuonly">{G(stu, mm)}</div><div class="solonly">{G(sol, mm)}</div>'
def cm(*a, **k): k.setdefault('fs', 11); return Fg.cm(*a, **k)
D = '<hr class="dash">'

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
def R(n, M): return list(zip(n, M))
ACT = ['activity A', 'activity B', 'activity C', 'activity D']; PPL = ['Amy', 'Bryce', 'Cherry', 'Dinnith']; AB = list('ABCD')
W0 = [[4, 4, 2, 4], [4, 3, 4, 5], [2, 5, 6, 3], [8, 7, 4, 6]]
W1 = [[2, 2, 0, 2], [1, 0, 1, 2], [0, 3, 4, 1], [4, 3, 0, 2]]
W2 = [[2, 2, 0, 1], [1, 0, 1, 1], [0, 3, 4, 0], [4, 3, 0, 1]]
W3 = [[1, 1, 0, 0], [1, 0, 2, 1], [0, 3, 5, 0], [3, 2, 0, 0]]
WE2 = [('Bryan', [1, 4, 7, 5]), ('Mason', [4, 5, 3, 7]), ('Lily', [2, 2, 3, 7]), ('Carmen', [8, 7, 6, 4])]
STG = ['planning', 'researching', 'writing', 'editing']
AM = [[0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 1]]
def sol(html): return f'<div class="solonly">{html}</div>'
def row(*cells): return '<div style="display:flex;gap:3mm;justify-content:center;align-items:flex-start;flex-wrap:wrap">' + ''.join(cells) + '</div>'

P = [title('14B', 'Matching and allocation problems')]
P.append(lis(['To be able to define and describe bipartite graphs.', 'To be able to solve assignment problems using the Hungarian Algorithm.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('Complete the following matrix to represent the graph below.')
             + ST(amat(list('ABCDE'), [[''] * 5] * 5, fs=14), amat(list('ABCDE'), AM, fs=14).replace('<table', '<table style="color:#c00"', 1), 45) + '</div>' + I('apk1.png', 45) + '</div>'))
P.append(box('Question 2 · VCAA 2017 Exam 1 Q3', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('Consider the following graph.')
  + q('The adjacency matrix for this graph, with some elements missing, is shown below.')
  + amat(list('WXYZ'), [[1, '_', '_', '_'], ['_', 0, '_', '_'], ['_', '_', 0, '_'], ['_', '_', '_', 1]], fs=13)
  + q('This adjacency matrix contains 16 elements when complete.<br>Of the 12 missing elements')
  + mc(['eight are ‘1’ and four are ‘2’.', 'four are ‘1’ and eight are ‘2’.', 'six are ‘1’ and six are ‘2’.', 'two are ‘0’, six are ‘1’ and four are ‘2’.', 'four are ‘0’, four are ‘1’ and four are ‘2’.'], 'A')
  + why('W–X 2, W–Y 2, W–Z 1, X–Y 1, X–Z 1, Y–Z 1, each filling two cells: eight 1s, four 2s') + '</div>' + I('apk2.png', 48) + '</div>', '1 mark'))
P.append(sect('14B Matching and allocation problems', 'Example, then you try'))
P.append(exyt('Example 6 · Bipartite graphs and allocation',
  q('Nick, Maria, David and Subitha are presenters on a TV travel show. Each presenter will be assigned a story to film about one country that they have visited before.')
  + q('• Nick has visited Greece, Malaysia and Brazil<br>• Maria has visited Greece and France<br>• Subitha has visited Malaysia and Brazil<br>• David has visited Malaysia')
  + q('Construct a bipartite graph of the information above and use it to decide on the assignment of each presenter to one country.')
  + ST(bip(EX6_L, ['Greece', 'Malaysia', 'France', 'Brazil'], [], W=300, lw=75, rw=80, ink=K),
       bip(EX6_L, EX6_R, EX6_E, hl=EX6_A, W=300, lw=75, rw=80, ink=K, hcol='#c00'), 58)
  + space(16, 'David has only visited Malaysia; only Maria has visited France, so Nick gets Greece and Subitha Brazil.<br>Nick: Greece, Maria: France, David: Malaysia, Subitha: Brazil'),
  'You try 1', q('A random survey of individuals’ sports preferences was conducted.<br>The results of 4 random individuals from the survey are shown in the following table. Use the information from the table to construct a bipartite graph.')
  + table([['individual', 'preferences'], ['James', 'basketball, soccer, tennis'], ['Alice', 'football'], ['Harry', 'soccer, tennis'], ['Nathan', 'soccer, tennis, football']])
  + '<div class="stuonly"><div style="min-height:42mm"></div></div>' + sol(G(bip(WE1_L, WE1_R, WE1_E, W=300, lw=70, rw=95, ink='#c00'), 58))))
P.append(box('You try 2 · Allocation by inspection', q('A university group assignment details a writing task on a research topic. The members in the group decide to split up the work based on which member was the most efficient at each task. Using inspection, find the minimum cost of the following cost matrix. The cost values are in hours.')
  + ST(cm(STG, WE2, fs=12), cm(STG, WE2, circ={(0, 0), (2, 1), (1, 2), (3, 3)}, fs=12), 110)
  + space(22, 'Bryan: planning (1), Lily: researching (2), Mason: writing (3), Carmen: editing (4)<br>Minimum cost = 1 + 2 + 3 + 4 = 10 hours')))
P.append(exyt('Example · The Hungarian algorithm (Cambridge 14B text)',
  q('The table shows the four employees: Wendy, Xenefon, Yolanda and Zelda. The machines in a factory are represented by the letters A, B, C and D.<br>The numbers in the table are the times, in minutes, it takes each employee to finish the task on each machine.')
  + cm(MAC, R(EMP, C0)) + q('The cost matrix can be used to determine the best way to allocate an employee to a machine so that the overall cost, in terms of the time taken to finish the work, is minimised. The Hungarian algorithm is used to do this.')
  + q('Step 1 · rows') + ST(cm(MAC, R(EMP, [[''] * 4] * 4)), cm(MAC, R(EMP, C1), cover_c={0, 1, 3}), 40)
  + q('Step 3 · columns, then cover the zeros') + ST(cm(MAC, R(EMP, [[''] * 4] * 4)), cm(MAC, R(EMP, C2), cover_r={1}, cover_c={0, 3}), 40)
  + q('Step 5 · adjust, then cover the zeros') + ST(cm(MAC, R(EMP, [[''] * 4] * 4)), cm(MAC, R(EMP, C3), cover_r={0, 1}, cover_c={0, 3}), 40)
  + space(18, 'Zelda: A (20), Yolanda: D (30), Wendy and Xenefon: B and C either way<br>Minimum time = 20 + 30 + 50 + 30 = 130 minutes'),
  'You try 3', q('Using the Hungarian algorithm, find the minimum cost of the following cost matrix. The cost values are in hours.') + cm(ACT, R(PPL, W0))
  + '<div class="stuonly"><div style="min-height:92mm"></div></div>'
  + sol(cm(AB, R(PPL, W1), cover_c={0, 1, 2}) + cm(AB, R(PPL, W2), cover_r={1, 2}, cover_c={2}) + cm(AB, R(PPL, W3), cover_r={1, 2}, cover_c={2, 3}))
  + space(14, 'Cherry: A, Bryce: B, Amy and Dinnith: C and D either way<br>2 + 3 + 2 + 6 = 13 (or 2 + 3 + 4 + 4 = 13): 13 hours')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 1 Q1', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('Lee, Mandy, Nola, Oscar and Pieter are each to be allocated one particular task at work.<br>The bipartite graph below shows which task(s), 1–5, each person is able to complete.')
  + q('Each person completes a different task.<br>Task 4 must be completed by') + mc(['Lee.', 'Mandy.', 'Nola.', 'Oscar.', 'Pieter.'], 'B')
  + why('Oscar: Task 3, Pieter: Task 5, so Nola: Task 2 and Mandy (Task 4 only) must do Task 4') + '</div>' + I('q10.png', 75) + '</div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q2', q('A cricket team has 11 players who are each assigned to a batting position.<br>Three of the new players, Alex, Bo and Cameron, can bat in position 1, 2 or 3.<br>The table below shows the average scores, in runs, for each player for the batting positions 1, 2 and 3.')
  + cm(['1', '2', '3'], [('Alex', [22, 24, 24]), ('Bo', [25, 25, 21]), ('Cameron', [24, 25, 19])], fs=12)
  + q('Each player will be assigned to one batting position.<br>To which position should each player be assigned to maximise the team’s score? Write your answer in the table below.')
  + table([['Player', 'Batting position'], ['Alex', a('3')], ['Bo', a('1')], ['Cameron', a('2')]]) + why('total 24 + 25 + 25 = 74 is the largest possible'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2018 Exam 1 Q8', q('Annie, Buddhi, Chuck and Dorothy work in a factory.<br>Today each worker will complete one of four tasks, 1, 2, 3 and 4.<br>The usual completion times for Annie, Chuck and Dorothy are shown in the table below.')
  + cm(['Task 1', 'Task 2', 'Task 3', 'Task 4'], [('Annie', [7, 3, 8, 2]), ('Buddhi', ['<i>k</i>', '<i>k</i>', 3, '<i>k</i>']), ('Chuck', [5, 6, 9, 2]), ('Dorothy', [4, 8, 5, 3])], fs=12)
  + q('Buddhi takes 3 minutes for Task 3.<br>He takes <i>k</i> minutes for each other task.<br>Today the factory supervisor allocates the tasks as follows:<br>• Task 1 to Dorothy<br>• Task 2 to Annie<br>• Task 3 to Buddhi<br>• Task 4 to Chuck')
  + q('This allocation will achieve the minimum total completion time if the value of <i>k</i> is at least') + mc(['0', '1', '2', '3', '4'], 'C', cols=5)
  + why('supervisor: 4 + 3 + 3 + 2 = 12; Buddhi on Task 1 instead: k + 3 + 5 + 2 = k + 10 ≥ 12 → k ≥ 2'), '1 mark'))
SC = ['I can draw directed and weighted bipartite graphs.', 'I can use the Hungarian algorithm to determine an optimum allocation in order to minimise cost.']
P.append(close(SC, [('14B', 'Q1–14')], ['14B']))
CSS_EXTRA = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
             'hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}.cmx{margin:1mm auto!important}</style>')
P[0] = CSS_EXTRA + P[0]
build('gm12-u4-14b', '14B', 'AoS 4 · Networks and decision mathematics', P)
RD = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-14b-worksheet', '14B worksheet'), ('gm12-u4-14b-worksheet-solutions', '14B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{RD}/{x}{ext}', f'{RD}/{y}{ext}')
