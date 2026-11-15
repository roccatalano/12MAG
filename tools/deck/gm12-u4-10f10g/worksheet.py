"""Lesson gm12-u4-10f10g (10F-10G) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py, networks from tools/deck/tpl/net.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 4 review skills checklist 4F #14, #15 (p. 292); VCAA 2019 Exam 1 Matrices Q7 adapted (Edrolo U1&2 5D Q14).
Examples 28-32 = Cambridge U3&4 pp. 523-533. You trys = Edrolo U3&4 7E WE1, 7E WE3, YT-10F-30 (written), 7F WE1, 7F WE2.
Exits = VCAA 2018 E1 Matrices Q4 (7E Q9), 2020 E1 Matrices Q3 (7E Q10), 2017 E1 Matrices Q5 (7F Q12), 2021 E2 Matrices Q2 (7F Q13).
Run: python3 tools/deck/gm12-u4-10f10g/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl'))
from ws2 import *
import ws2
from mx import mat
from net import net
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def Wd(mm, x): return f'<div style="width:{mm}mm;margin:1mm auto">{x}</div>'
def AR(a, b): return (a, b, {'arrow': True})
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-10f10g')
G31 = net({'E': (110, 10, 'e'), 'W': (110, 70, 'e'), 'Y': (30, 150, 'w'), 'K': (190, 150, 'e')}, [AR('W', 'E'), AR('E', 'W'), AR('W', 'Y'), AR('Y', 'W'), AR('W', 'K'), AR('K', 'W')], W=220, H=160, pad=14)
G32 = net({'A': (20, 70, 'w'), 'B': (150, 10, 'n'), 'C': (270, 55, 'e'), 'D': (230, 120, 's')}, [AR('A', 'B'), AR('A', 'D'), AR('B', 'C'), AR('D', 'C'), AR('D', 'B')], W=290, H=130, pad=16)
GLH = net({'B': (20, 35, 'w'), 'D': (150, 15, 'n'), 'C': (200, 85, 's'), 'A': (35, 110, 's')}, [('B', 'D'), ('D', 'C'), ('B', 'A'), ('B', 'C')], W=220, H=120, pad=16)
GJ = net({'Bruin': (140, 15, 'n'), 'Claude': (250, 45, 'e'), 'Abe': (30, 70, 'w'), 'Dan': (230, 140, 'e'), 'Eugene': (110, 160, 's')},
         [AR('Abe', 'Bruin'), AR('Abe', 'Claude'), AR('Abe', 'Dan'), AR('Bruin', 'Eugene'), AR('Claude', 'Bruin'), AR('Dan', 'Bruin'), AR('Dan', 'Claude'), AR('Eugene', 'Abe'), AR('Eugene', 'Claude'), AR('Eugene', 'Dan')], W=280, H=175, pad=22, fs=16)
GRD = net({'A': (20, 20, 'w'), 'B': (210, 15, 'n'), 'C': (190, 150, 'w'), 'D': (20, 150, 's')}, [('A', 'B'), ('A', 'D'), ('D', 'B', {'bend': 40}), ('B', 'C', {'bend': -25})], W=230, H=165, pad=16)
GABC = net({'A': (20, 110, 'w'), 'B': (160, 110, 'e'), 'C': (90, 15, 'n')}, [('A', 'B'), ('B', 'C'), ('A', 'C')], W=180, H=125, pad=16)
SOL = '<span class="ans">' + Wd(30, GABC) + '</span>'

P = [title('10F-10G', 'Binary, permutation, communication and dominance matrices')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Use a matrix to record the number of ways of travelling directly from one town to another.') + Wd(45, GRD)
  + space(22, M([[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]], rl=list('ABCD'), cl=list('ABCD')))))
P.append(box('Question 2', q('Draw a network to show the direct connections between towns <i>A</i>, <i>B</i> and <i>C</i> given in the matrix below.')
  + row(M([[0, 1, 1], [1, 0, 1], [1, 1, 0]], rl=list('ABC'), cl=list('ABC'), side=True)) + space(26, Wd(30, GABC))))
JM = [[0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [1, 1, 0, 1, 0, 0]]
P.append(box('Question 3 · VCAA 2019 Exam 1 Q7 (adapted)', q('Matrix <i>J</i> is a communication matrix showing the direct paths by which messages can be sent between two people in a group of six people, U to Z.')
  + row('<i>J</i> = ' + M(JM, rl=list('UVWXYZ'), cl=list('UVWXYZ'), side=True), '<i>sender (rows), receiver (columns)</i>')
  + q('A ‘1’ in the matrix shows that the person named in that row can send a message directly to the person named in that column. For example, the ‘1’ in row 4, column 3 shows that X can send a message directly to W.<br>In how many ways can W get a message to U by sending it directly to one other person?')
  + mc(['0', '1', '2', '3', '4'], 'D', cols=5) + why('W → V → U, W → X → U, W → Z → U'), '1 mark'))

P.append(sect('10F Binary, permutation and communication matrices', 'Example, then you try'))
P.append(exyt('Example 28 · Applying a permutation matrix',
  Q('<i>X</i> is the column matrix <i>X</i> = ' + M([['T'], ['A'], ['R']]) + '. <i>P</i> is the permutation matrix <i>P</i> = ' + M([[0, 0, 1], [0, 1, 0], [1, 0, 0]]) + '.')
  + Q('a Show that:<br>i pre-multiplying <i>X</i> by <i>P</i> changes the matrix <i>X</i> to the matrix <i>Y</i> = ' + M([['R'], ['A'], ['T']]))
  + row('<i>PX</i> = ' + A(M([['R'], ['A'], ['T']])))
  + Q('ii pre-multiplying <i>X</i> by <i>P</i><sup>2</sup> leaves the matrix <i>X</i> unchanged.') + row('<i>P</i><sup>2</sup><i>X</i> = ' + A(M([['T'], ['A'], ['R']])))
  + Q('b What can be deduced about <i>P</i><sup>2</sup> from the result in a ii?') + q(A('<i>P</i><sup>2</sup> is the identity matrix <i>I</i>.')),
  'You try 28', Q('Perform a column permutation of matrix <i>X</i> by using permutation matrix <i>P</i>.')
  + row('<i>X</i> = ' + M([['u', 'm', 'l', 'p']]), '<i>P</i> = ' + M([[0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]))
  + space(30, 'XP = ' + M([['p', 'l', 'u', 'm']]))))
P.append(exyt('Example 29 · Finding a permutation matrix',
  Q('Find a permutation matrix that takes the column matrix ' + M([['A'], ['B'], ['C'], ['D']]) + ' to the column matrix ' + M([['D'], ['C'], ['B'], ['A']]))
  + row(A(M([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])) + M([['A'], ['B'], ['C'], ['D']]) + ' = ' + M([['D'], ['C'], ['B'], ['A']])),
  'You try 29', Q('Determine the permutation matrix <i>P</i> that would be required to change')
  + row(M([[21, 17, 42], [31, 22, 27], [46, 33, 15]]), 'to', M([[31, 22, 27], [21, 17, 42], [46, 33, 15]]))
  + space(22, 'P = ' + M([[0, 1, 0], [1, 0, 0], [0, 0, 1]]))))
P.append(exyt('Example 30 · The inverse of a permutation matrix',
  Q('A 4 × 4 permutation matrix <i>P</i> = ' + M([[0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]) + ' applied to a 4 × 1 column matrix <i>A</i> gives the column matrix ' + M([['X'], ['Y'], ['Z'], ['W']]) + '. Determine the matrix <i>A</i>.')
  + row('<i>A</i> = <i>P</i><sup>−1</sup>' + M([['X'], ['Y'], ['Z'], ['W']]) + ' = <i>P</i><sup>T</sup>' + M([['X'], ['Y'], ['Z'], ['W']]) + ' = ' + A(M([['W'], ['Z'], ['X'], ['Y']]))),
  'You try 30', Q('A 4 × 4 permutation matrix <i>P</i> = ' + M([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]) + ' applied to a 4 × 1 column matrix <i>A</i> gives the column matrix ' + M([['K'], ['L'], ['M'], ['N']]) + '. Determine the matrix <i>A</i>.')
  + space(24, 'A = Pᵀ' + M([['K'], ['L'], ['M'], ['N']]) + ' = ' + M([['M'], ['K'], ['N'], ['L']]))))
P.append(exyt('Example 31 · Constructing a communication matrix',
  Q('Eva, Wong, Yumi and Kim are students who are staying in a backpacker’s hostel. Because they speak different languages they can have problems communicating. The situation they have to deal with is that: Eva speaks English only; Yumi speaks Japanese only; Kim speaks Korean only; Wong speaks English, Japanese and Korean.')
  + Wd(32, G31) + Q('Conveniently, this information can be summarised in a network diagram, as shown above. In this diagram, the arrow linking Eva and Wong indicates that they can communicate directly because they both speak English. The task is to construct a communication matrix.')
  + row('<i>Speaker</i> ' + A(M([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]], rl=list('EWYK'), cl=list('EWYK'))) + ' <i>Receiver</i> (columns)'),
  'You try 31', Q('The following network diagram shows communication lines between four lighthouses, A, B, C and D.') + Wd(36, GLH)
  + parts([('a', 'Construct an undirected communication matrix, <i>C</i>, that indicates all one-step communication links between the lighthouses.', 'C = ' + M([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]), 20),
           ('b', 'Construct a communication matrix, <i>T</i>, that indicates all one-step and two-step communication links between the lighthouses.', 'T = C + C² = ' + M([[1, 1, 1, 1], [1, 3, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2]]), 20),
           ('c', 'Using matrix <i>T</i> from part b, in how many ways can lighthouse B communicate with lighthouse D?', '2', 8),
           ('d', 'Using matrix <i>T</i> from part b, how many redundant communication links are there?', '1 + 3 + 2 + 2 = 8', 8)])))

P.append(sect('10G Dominance matrices', 'Example, then you try'))
P.append(exyt('Example 32 · Determining dominance',
  Q('Four people, <i>A</i>, <i>B</i>, <i>C</i> and <i>D</i>, have been asked to form a committee to decide on the location of a new toxic waste dump.') + Wd(45, G32)
  + Q('From previous experience, it is known that: <i>A</i> influences the decisions of <i>B</i> and <i>D</i>; <i>B</i> influences the decisions of <i>C</i>; <i>C</i> influences the decisions of no one; <i>D</i> influences the decisions of <i>C</i> and <i>B</i>.')
  + Q('a Use the graph to construct a dominance matrix that takes into account both one-step and two-step dominances.')
  + row('<i>D</i> = ' + M([[0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0]], rl=list('ABCD'), cl=list('ABCD')), '<i>D</i><sup>2</sup> = ' + M([[0, 1, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]))
  + row('<i>T</i> = <i>D</i> + <i>D</i><sup>2</sup> = ' + A(M([[0, 2, 2, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 2, 0]], rl=list('ABCD'), cl=list('ABCD'))) + ' totals ' + A('5, 1, 0, 3'))
  + Q('b From this matrix, determine who is the most influential person on the committee.') + q(A('Person <i>A</i> (total dominance score 5).')),
  'You try 32', Q('Five players participated in a round-robin jousting tournament. The results are shown in the following network. An arrow from Abe to Bruin indicates that Abe defeated Bruin.') + Wd(48, GJ)
  + parts([('a', 'Construct a dominance matrix, <i>D</i>, that indicates all one-step dominances.', 'D = ' + M([[0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [1, 0, 1, 1, 0]], rl=list('ABCDE'), cl=list('ABCDE')), 26),
           ('b', 'Rank the players from most to least dominant.', 'T = D + D² row sums 7, 4, 2, 4, 9: Eugene, Abe, Bruin/Dan (tied), Claude', 18)])))

P.append(sect('Exit tasks', 'Show what you know'))
OPT = [[[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], [[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]], [[1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]]]
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q4', q('Matrix <i>P</i> is a 4 × 4 permutation matrix.<br>Matrix <i>W</i> is another matrix such that the matrix product <i>P</i> × <i>W</i> is defined.<br>This matrix product results in the entire first and third rows of matrix <i>W</i> being swapped.<br>The permutation matrix <i>P</i> is')
  + mc([M(o) for o in OPT], 'B', cols=5) + why('1s at (1, 3) and (3, 1) swap rows 1 and 3; rows 2 and 4 stay'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2020 Exam 1 Q3', q('Matrices <i>P</i> and <i>W</i> are defined as shown.')
  + row('<i>P</i> = ' + M([[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0]]), '<i>W</i> = ' + M([['A'], ['S'], ['T'], ['O'], ['R']]))
  + row('If <i>P</i><sup><i>n</i></sup> × <i>W</i> = ' + M([['A'], ['S'], ['T'], ['O'], ['R']]) + ', the value of <i>n</i> could be')
  + mc(['1', '2', '3', '4', '5'], 'D', cols=5) + why('PW = TRSOA, P²W = SAROT, P³W = RTAOS, P⁴W = ASTOR'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2017 Exam 1 Q5', q('Four teams, A, B, C and D, competed in a round-robin competition where each team played each of the other teams once. There were no draws.<br>The results are shown in the following matrix.')
  + row(M([[0, 0, '<i>f</i>', 1], [1, 0, 0, 0], [1, '<i>g</i>', 0, 1], [0, 1, 0, '<i>h</i>']], rl=list('ABCD'), cl=list('ABCD'), side=True), '<i>winner (rows), loser (columns)</i>')
  + q('A ‘1’ in the matrix shows that the team named in that row defeated the team named in that column.<br>For example, the ‘1’ in row 2 shows that team B defeated team A.<br>In this matrix, the values of <i>f</i>, <i>g</i> and <i>h</i> are')
  + mc(['<i>f</i> = 0, <i>g</i> = 1, <i>h</i> = 0', '<i>f</i> = 0, <i>g</i> = 1, <i>h</i> = 1', '<i>f</i> = 1, <i>g</i> = 0, <i>h</i> = 0', '<i>f</i> = 1, <i>g</i> = 1, <i>h</i> = 0', '<i>f</i> = 1, <i>g</i> = 1, <i>h</i> = 1'], 'A', cols=3)
  + why('C beat A (f = 0), C beat B (g = 1), no team plays itself (h = 0)'), '1 mark'))
MM = [[0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]
P.append(box('Exit task 4 · VCAA 2021 Exam 2 Q2', q('The main computer system in Elena’s office has broken down.<br>The five staff members, Alex (A), Brie (B), Chai (C), Dex (D) and Elena (E), are having problems sending information to each other.<br>Matrix <i>M</i> shows the available communication links between the staff members.')
  + row('<i>M</i> = ' + M(MM, rl=list('ABCDE'), cl=list('ABCDE'), side=True), '<i>sender (rows), receiver (columns)</i>')
  + q('In this matrix: the ‘1’ in row A, column B indicates that Alex can send information to Brie; the ‘0’ in row D, column C indicates that Dex cannot send information to Chai.')
  + parts([('a', 'Which two staff members can send information directly to each other? (1 mark)', 'Brie and Dex', 8),
           ('b', 'Elena needs to send documents to Chai.<br>What is the sequence of communication links that will successfully get the information from Elena to Chai? (1 mark)', 'Elena → Dex → Brie → Chai', 8),
           ('c', 'Matrix <i>M</i><sup>2</sup> is the square of matrix <i>M</i> and shows the number of two-step communication links between each pair of staff members.'
            + row('<i>M</i><sup>2</sup> = ' + M([[0, 0, 1, 2, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 0]], rl=list('ABCDE'), cl=list('ABCDE'), side=True))
            + 'Only one pair of individuals has two different two-step communication links.<br>List each two-step communication link for this pair. (1 mark)', 'Alex → Brie → Dex and Alex → Elena → Dex', 10)]), '3 marks'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('10F', 'Q1–9'), ('10G', 'Q1–12')], ['10F', '10G']))
build('gm12-u4-10f10g', '10F-10G', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-10f10g-worksheet', '10F-10G worksheet'), ('gm12-u4-10f10g-worksheet-solutions', '10F-10G worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
