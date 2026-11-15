"""Lesson gm12-u4-10d (10D) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now and CFAT not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4D #7, #9 (p. 291; solutions worked for 12MAG); VCAA 2020 Exam 1 Matrices Q2 (Edrolo U1&2 5C Q16).
Examples 17-23 = Cambridge U3&4 Examples 17-23 (pp. 500-508).
You trys = Edrolo U3&4 7C WE1, Edrolo U1&2 5C WE1, YT-10D-19 (written), Edrolo U3&4 7C WE2, 7C WE3, Edrolo U1&2 5D WE1, Edrolo U3&4 7C WE4.
Exits = VCAA 2017 Exam 2 Matrices Q1a (Edrolo U3&4 7C Q17), VCAA 2018 Exam 1 Matrices Q2 (Edrolo 7C Q18).
Output: lessons/10D worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-10d/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join(xs) + '</div>'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-10d')

P = [title('10D', 'Matrix arithmetic: the product of two matrices')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', Q('State whether it is possible to find <i>AB</i> or <i>BA</i> for the following matrices:') + row(M([[3], [-2]], name='A'), M([[7, 5], [-3, 9]], name='B'))
  + space(14, 'AB: (2 × 1)(2 × 2), 1 ≠ 2: not possible. BA: (2 × 2)(2 × 1): possible, BA = ' + M([[11], [-27]]))))
P.append(box('Question 2', q('Calculate the following matrix multiplication by hand:') + row(M([[5, 2], [-1, 0], [1, 4]]) + M([[3, 1, 9], [-4, -5, 0]]))
  + space(20, M([[7, -5, 45], [-3, -1, -9], [-13, -19, 9]]))))
P.append(box('Question 3 · VCAA 2020 Exam 1 Q2', row('Matrix <i>A</i> = ' + M([[1, 2], [0, 3], [1, 0], [4, 5]]), 'and matrix <i>B</i> = ' + M([[2, 0, 3, 1], [4, 5, 2, 0]]) + '.')
  + q('Matrix <i>Q</i> = <i>A</i> × <i>B</i>.<br>The element in row <i>i</i> and column <i>j</i> of matrix <i>Q</i> is <i>q<sub>ij</sub></i>.<br>Element <i>q</i><sub>41</sub> is determined by the calculation')
  + mc(['0 × 0 + 3 × 5', '1 × 1 + 2 × 0', '1 × 2 + 2 × 4', '4 × 1 + 5 × 0', '4 × 2 + 5 × 4'], 'E', cols=5) + why('row 4 of A × column 1 of B'), '1 mark'))

P.append(sect('10D The product of two matrices', 'Example, then you try'))
G17 = row(M([[6, 0], [-4, 2]], name='A'), M([[3, 1]], name='B'), M([[1], [-1]], name='C'))
P.append(exyt('Example 17 · Is a matrix product defined?',
  G17 + q('Which of the following matrix products are defined?')
  + q('a <i>AB</i>: (2 × 2)(1 × 2) → ' + A('not defined') + '<br>b <i>BC</i>: (1 × 2)(2 × 1) → ' + A('defined') + '<br>c <i>AC</i>: (2 × 2)(2 × 1) → ' + A('defined')),
  'You try 17', q('Determine whether the following matrix products are defined. If defined, determine its order.') + row(M([[3, -2], [0, 5]], name='K'), M([[-1], [3]], name='L'))
  + parts([('a', '<i>KL</i>', 'defined; order 2 × 1', 10), ('b', '<i>LK</i>', 'not defined', 10)])))
P.append(exyt('Example 18 · Determining the order of a matrix product',
  G17 + q('The following matrix products are defined. What is their order?')
  + q('a <i>BA</i>: (1 × 2)(2 × 2) → ' + A('1 × 2') + '<br>b <i>BC</i>: (1 × 2)(2 × 1) → ' + A('1 × 1') + '<br>c <i>AC</i>: (2 × 2)(2 × 1) → ' + A('2 × 1')),
  'You try 18', q('Determine whether the following matrix products are defined. If defined, determine its order.')
  + row(M([[3, -12], [9, 4], [-7, 6]], name='P'), M([[2, 3, -11], [4, 0, -5], [3, -2, 7], [2, -5, 0], [1, 1, 6]], name='Q'))
  + parts([('a', '<i>PQ</i>', 'not defined (3 × 2)(5 × 3)', 8), ('b', '<i>QP</i>', 'defined; order 5 × 2', 8)])))
P.append(exyt('Example 19 · Multiplying a row matrix by a column matrix (by hand)',
  Q('Evaluate the matrix product <i>AB</i>, where <i>A</i> = ' + M([[1, 3, 2]]) + ' and <i>B</i> = ' + M([[2], [4], [1]]) + '.')
  + q('Order: (1 × 3)(3 × 1) → defined, ' + A('1 × 1')) + q('<i>AB</i> = [1 × 2 + 3 × 4 + 2 × 1] = ' + A('[16]')),
  'You try 19', Q('Evaluate the matrix product <i>AB</i>, where <i>A</i> = ' + M([[2, 1, 3]]) + ' and <i>B</i> = ' + M([[5], [2], [4]]) + '.')
  + space(20, '(1 × 3)(3 × 1): defined, 1 × 1. AB = [2 × 5 + 1 × 2 + 3 × 4] = [24]')))
P.append(exyt('Example 20 · Multiplying a rectangular matrix by a column matrix (by hand)',
  Q('Evaluate the matrix product <i>AB</i>, where <i>A</i> = ' + M([[1, 0], [2, 3]]) + ' and <i>B</i> = ' + M([[2], [3]]) + '.')
  + q('Order: (2 × 2)(2 × 1) → defined, ' + A('2 × 1'))
  + row('<i>AB</i> = ' + M([['1 × 2 + 0 × 3'], ['2 × 2 + 3 × 3']]) + ' = ' + A(M([[2], [13]]))),
  'You try 20', q('Consider the following matrices.') + row(M([[-1, 3], [0, 5]], name='P'), M([[2], [4]], name='Q')) + q('Evaluate the matrix product <i>PQ</i>.')
  + space(18, 'PQ = ' + M([['−1 × 2 + 3 × 4'], ['0 × 2 + 5 × 4']]) + ' = ' + M([[10], [20]]))))
M21 = [[1, 3, 0], [2, 6, 7], [3, 0, 1]]; N21 = [[2, 5, -1, -3, 4], [0, 6, 2, -2, 3]]; S7 = [[-1, 0, 6], [2, -3, 4]]
P.append(exyt('Example 21 · Using matrix multiplication to sum the rows and columns of a matrix',
  q('Use matrix multiplication to generate a matrix that:')
  + Q('a i displays row sums of the matrix ' + M(M21)) + row(M(M21) + M([[1], [1], [1]]) + ' = ' + A(M([[4], [15], [4]])))
  + Q('a ii displays column sums of the matrix ' + M(M21)) + row(M([[1, 1, 1]]) + M(M21) + ' = ' + A(M([[6, 9, 8]])))
  + Q('b displays the column sums of the matrix ' + M(N21) + '.') + row(M([[1, 1]]) + M(N21) + ' = ' + A(M([[2, 11, 1, -5, 7]]))),
  'You try 21', row(M(S7, name='S')) + q('Use an appropriate summing matrix to')
  + parts([('a', 'sum the rows of matrix <i>S</i>.', M(S7) + M([[1], [1], [1]]) + ' = ' + M([[5], [3]]), 18), ('b', 'sum the columns of matrix <i>S</i>.', M([[1, 1]]) + M(S7) + ' = ' + M([[1, -3, 10]]), 18)])))
P.append(exyt('Example 22 · A practical application of matrix multiplication',
  row('<i>E</i> = ' + M([[25], [40]], rl=['<i>Walk</i>', '<i>Run</i>'], side=True)) + q('Matrix <i>E</i> gives the energy in kilojoules consumed per minute when walking and running.')
  + row('<i>T</i> = ' + M([[20, 40]], cl=['<i>Walk</i>', '<i>Run</i>'])) + q('Matrix <i>T</i> gives the times (in minutes) a person spent walking and running in a training session.')
  + q('Compute the matrix product <i>TE</i> and show that it gives the total energy consumed during the training session.')
  + q('<i>T</i> × <i>E</i> = [20 × 25 + 40 × 40] = ' + A('[2100]')) + q('20 min × 25 kJ/min + 40 min × 40 kJ/min = ' + A('2100 kJ, the value given by <i>TE</i>.')),
  'You try 22', q('Jaiden (J) and Nick (N) both sell the same types of fish. They both sell trout (T) for $40, cod (C) for $30 and mackerel (M) for $20. The number of each fish sold by Jaiden and Nick can be found in matrix <i>F</i>.')
  + row('<i>F</i> = ' + M([[10, 19, 13], [11, 9, 16]], cl=['T', 'C', 'M'], rl=['J', 'N'], side=True))
  + parts([('a', 'Construct <i>P</i>, a matrix which contains the prices of each type of fish, as a column matrix.', 'P = ' + M([[40], [30], [20]], rl=['T', 'C', 'M'], side=True), 18),
           ('b', 'Using a matrix product, calculate the revenue made from Jaiden and Nick.', 'F × P = ' + M([[1230], [1030]], rl=['J', 'N'], side=True) + ': Jaiden $1230, Nick $1030', 18)])))
P.append(exyt('Example 23 · Evaluating matrix expressions involving powers',
  Q('If <i>A</i> = ' + M([[1, 0], [2, -1]]) + ', <i>B</i> = ' + M([[-1, 1], [2, 1]]) + ' and <i>C</i> = ' + M([[0, 1], [1, 1]]) + ', determine:')
  + Q('a 2<i>A</i> + <i>B</i><sup>2</sup> − 2<i>C</i> = ' + A(M([[5, -2], [2, -1]])))
  + Q('b (2<i>A</i> − <i>B</i>)<sup>2</sup> − <i>C</i><sup>2</sup> = ' + A(M([[6, -1], [-1, 5]])))
  + Q('c <i>AB</i><sup>2</sup> − 3<i>C</i><sup>2</sup> = ' + A(M([[0, -3], [3, -9]]))),
  'You try 23', q('Consider the following matrices.') + row(M([[1], [2], [3]], name='A'), M([[2, 1], [8, 9]], name='B'), M([[2, 3, 5]], name='C'))
  + parts([('a', 'Calculate <i>B</i><sup>2</sup>.', 'B² = ' + M([[12, 11], [88, 89]]), 18), ('b', 'Determine whether (<i>AC</i>)<sup>2</sup> is defined.', 'AC is (3 × 1)(1 × 3) = 3 × 3, square: (AC)² is defined', 14)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 2 Q1a', q('A school canteen sells pies (<i>P</i>), rolls (<i>R</i>) and sandwiches (<i>S</i>).<br>The number of each item sold over three school weeks is shown in matrix <i>M</i>.')
  + row('<i>M</i> = ' + M([[35, 24, 60], [28, 32, 43], [32, 30, 56]], cl=['P', 'R', 'S'], rl=['week 1', 'week 2', 'week 3'], side=True))
  + q('a. In total, how many sandwiches were sold in these three weeks?') + space(10, '60 + 43 + 56 = 159'), '1 mark'))
X2 = [M([[144]]), M([[16], [24], [0]]), '4 × ' + M([[1, 2, 0]]) + ' × ' + M([[1], [12], [8]]), '2 × ' + M([[2, 1, 0]]) + ' × ' + M([[2], [6], [4]]), '4 × ' + M([[2, 1, 0]]) + ' × ' + M([[2], [6], [4]])]
P.append(box('Exit task 2 · VCAA 2018 Exam 1 Q2', Q('The matrix product ' + M([[4, 2, 0]]) + ' × ' + M([[4], [12], [8]]) + ' is equal to')
  + mc(X2, 'E', cols=5) + why('4 × 4 + 2 × 12 + 0 × 8 = 40, and 4 × (2 × 2 + 1 × 6 + 0 × 4) = 40'), '1 mark'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('10D', 'Q1–20')], ['10D']))
build('gm12-u4-10d', '10D', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-10d-worksheet', '10D worksheet'), ('gm12-u4-10d-worksheet-solutions', '10D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
