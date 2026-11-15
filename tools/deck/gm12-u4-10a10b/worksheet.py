"""Lesson gm12-u4-10a10b (10A-10B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 skills checklist 4A #1, #2 (solutions worked for 12MAG); VCAA 2020 Exam 1 Matrices Q6 (original wording; Edrolo U1&2 5A Q13).
Examples 1-10 = Cambridge U3&4 Examples 1-10 (pp. 474-487).
You trys = Edrolo U3&4 7A WE1a, 7B WE3, Edrolo U1&2 5A WE2, Edrolo U3&4 7A WE2a-e, 7A WE1b, 7A WE4, 7A WE3a-b, YT-10B-8 (written),
           Edrolo U1&2 5D WE3a, YT-10B-10 (written).
Exits = VCAA 2018 Exam 2 Matrices Q1a-c (Edrolo U3&4 7A Q12; part c Edrolo's adapted wording), VCAA 2017 Exam 1 Matrices Q6 (Edrolo 7B Q15).
Output: lessons/10A-10B worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-10a10b/worksheet.py"""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def IMG(f, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{mm}mm;display:block;margin:1mm auto">'
def row(*xs): return '<div style="display:flex;gap:6mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join(xs) + '</div>'
def L(l, x): return f'<span style="display:inline-flex;gap:2mm;align-items:center"><b>{l}</b>{x}</span>'

P = [title('10A–10B', 'What is a matrix? Using matrices to represent information')]
P.append(lis(['To be able to state the order of a given matrix.', 'To be able to describe the location of an element in a matrix.', 'To be able to determine the transpose of a matrix.',
              'To be able to define and recognise diagonal, symmetric and triangular matrices.', 'To be able to define and recognise identity matrices.',
              'To be able to represent data given in a table by a matrix.', 'To be able to represent a network diagram with a matrix.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('State the order of the following matrix:') + row(M([[7, -2, 5], [10, 0, 4]])) + space(8, '2 rows, 3 columns: order 2 × 3')))
P.append(box('Question 2', q('Considering the following matrix, <i>B</i>, state the value of the element in <i>b</i><sub>23</sub>.') + row(M([[57, 63, 19], [48, 54, 6]], name='B')) + space(8, 'row 2, column 3: b<sub>23</sub> = 6')))
OP = [[[5,7,9],[7,9,11],[11,13,15]],[[5,7,9],[8,10,12],[11,13,15]],[[5,7,10],[8,10,13],[11,13,16]],[[5,8,11],[7,10,13],[9,12,15]],[[5,8,11],[8,11,14],[11,14,17]]]
P.append(box('Question 3 · VCAA 2020 Exam 1 Q6', q('The element in row <i>i</i> and column <i>j</i> of matrix <i>M</i> is <i>m<sub>ij</sub></i>.<br><i>M</i> is a 3 × 3 matrix. It is constructed using the rule <i>m<sub>ij</sub></i> = 3<i>i</i> + 2<i>j</i>.<br><i>M</i> is')
  + mc([M(o) for o in OP], 'B', cols=5) + why('row 1: 3 + 2, 3 + 4, 3 + 6 = 5, 7, 9; row 2: 8, 10, 12; row 3: 11, 13, 15')))

P.append(sect('10A What is a matrix?', 'Example, then you try'))
EX1 = {'a': [[1,5],[3,0],[7,6]], 'b': [[1,5,8,9,0]], 'c': [[1],[4],[4],[9]], 'd': [[1,4,4,5],[4,3,4,6],[4,3,2,1],[9,1,0,7]]}
P.append(exyt('Example 1 · The order of a matrix',
  q('State the order of each of the following matrices.') + row(*[L(k, M(v)) for k, v in EX1.items()])
  + q('a ' + A('3 × 2') + ' &nbsp; b ' + A('1 × 5') + ' &nbsp; c ' + A('4 × 1') + ' &nbsp; d ' + A('4 × 4')),
  'You try 1', q('Matrix <i>A</i> contains a list of multiple elements.') + row(M([[101, 2, 85], [41, 56, 73]], name='A'))
  + parts([('a', 'What is the order of matrix <i>A</i>?', '2 rows, 3 columns: 2 × 3', 'L')])))
P.append(exyt('Example 2 · The transpose of a matrix',
  parts([('a', 'Write down the transpose of ' + M([[7, 4], [8, 1]]) + '.', M([[7, 8], [4, 1]]), 12),
         ('b', 'Write down the matrix ' + M([[0, 1, 2], [3, 2, 5]], sup='T') + '.', M([[0, 3], [1, 2], [2, 5]]), 15),
         ('c', 'If <i>A</i> = ' + M([[2, 0, 1]]) + ', write down the matrix <i>A</i><sup>T</sup>.', M([[2], [0], [1]]), 15)]),
  'You try 2', '<div class="q">If <i>D</i> = ' + M([[1, 0, 9], [5, 2, 3]]) + ', determine <i>D</i><sup>T</sup>.</div>' + space(22, 'D<sup>T</sup> = ' + M([[1, 5], [0, 2], [9, 3]]))))
P.append(exyt('Example 3 · Matrix facts',
  q('For each of the matrices below, write down its type, order and the number of elements.')
  + row(M([[1, 5, 1], [2, 2, 4], [2, -1, 6]], name='A'), M([[1], [0], [1]], name='B')) + row(M([[3, 1, 0, 5, -3, 1]], name='C'))
  + table([['Matrix', 'Type', 'Order', 'No. of elements'], ['<i>A</i>', a('square'), a('3 × 3'), a('9')], ['<i>B</i>', a('column'), a('3 × 1'), a('3')], ['<i>C</i>', a('row'), a('1 × 6'), a('6')]], cls='t tiny'),
  'You try 3', q('Classify the following matrices as either a row, column, square, zero or identity matrix. There may be more than one answer.')
  + parts([('a', '<i>B</i> = ' + M([[12, 23, 42, 7]]), 'Row matrix', 'L'), ('b', '<i>C</i> = ' + M([[0, 0, 0, 0], [0, 0, 0, 0]]), 'Zero matrix', 'L'),
           ('c', '<i>D</i> = ' + M([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 'Square and identity matrix', 'L')])))
E4 = [[[1, 0], [0, 1]], [[1, 2], [0, 3]], [[1, 0, 0], [0, 4, 0], [0, 0, 3]], [[1, 3, 5], [3, 4, 7], [5, 7, 2]]]
W2 = {'P': [[6,5,2],[0,5,6],[0,0,5]], 'Q': [[1,0,5],[0,0,2],[5,2,3]], 'R': [[1,0,0],[0,1,0],[0,0,1]], 'S': [[5,0,0],[0,4,0],[0,0,7]], 'T': [[0,0,0],[11,2,0],[2,5,8]]}
W2a = ['Upper triangular', 'Symmetric', 'Symmetric, diagonal, identity, upper and lower triangular', 'Symmetric, diagonal, upper and lower triangular', 'Lower triangular']
P.append(exyt('Example 4 · Types of matrices',
  q('Consider the following square matrices.') + row(*[M(m) for m in E4]) + q('Write down:')
  + parts([('a', 'the upper triangular matrices', 'the 2nd, 1st and 3rd matrices (zeros below the leading diagonal)', 'L'), ('b', 'the identity matrix', 'the 1st matrix', 'L'),
           ('c', 'the diagonal matrices', 'the 1st and 3rd matrices', 'L'), ('d', 'the symmetric matrices.', 'the 4th, 1st and 3rd matrices', 'L')]),
  'You try 4', q('Matrices <i>P</i>, <i>Q</i>, <i>R</i>, <i>S</i> and <i>T</i> are all 3 × 3 matrices. Each of the following matrices fall into one or more classifications, namely diagonal, identity, symmetric, upper triangular, and lower triangular.')
  + row(*[M(v, name=k) for k, v in W2.items()])
  + parts([('abcde'[i], f'How can matrix <i>{k}</i> be classified?', W2a[i], 'L') for i, k in enumerate(W2)])))
P.append(exyt('Example 5 · Identifying the elements in a matrix',
  q('For the matrices <i>A</i> and <i>B</i>, opposite, write down the values of:') + row(M([[1, 5, 3], [-1, 0, 4], [2, -2, 6]], name='A'), M([[3], [2], [1]], name='B'))
  + q('a <i>a</i><sub>12</sub> = ' + A('5') + ' &nbsp; b <i>a</i><sub>21</sub> = ' + A('−1') + ' &nbsp; c <i>a</i><sub>33</sub> = ' + A('6') + ' &nbsp; d <i>b</i><sub>31</sub> = ' + A('1')),
  'You try 5', q('Matrix <i>A</i> contains a list of multiple elements.') + row(M([[101, 2, 85], [41, 56, 73]], name='A'))
  + parts([('b', 'What is element <i>a</i><sub>21</sub>?', 'row 2, column 1: 41', 'L')])))
P.append(exyt('Example 6 · Constructing a matrix given a rule for its <i>ij</i>th term',
  q('<i>A</i> is a 3 × 2 matrix. The element in row <i>i</i> and column <i>j</i> is given by <i>a<sub>ij</sub></i> = <i>i</i> + <i>j</i>.<br>Construct the matrix.')
  + row('<i>A</i> = ' + M([['a<sub>11</sub>', 'a<sub>12</sub>'], ['a<sub>21</sub>', 'a<sub>22</sub>'], ['a<sub>31</sub>', 'a<sub>32</sub>']]), '<i>A</i> = ' + M([[a('2'), a('3')], [a('3'), a('4')], [a('4'), a('5')]])),
  'You try 6', q('Matrix <i>C</i> is a matrix with an order of 3 × 2.<br>Construct matrix <i>C</i>, with the element rule <i>c<sub>ij</sub></i> = <i>i</i> × <i>j</i>, where <i>c<sub>ij</sub></i> refers to the entry in the <i>i</i><sup>th</sup> row and <i>j</i><sup>th</sup> column.')
  + space(20, 'C = ' + M([[1, 2], [2, 4], [3, 6]]))))

P.append(sect('10B Using matrices to represent information', 'Example, then you try'))
GYM = table([['Gender', 'Weights', 'Aerobics', 'Fitness'], ['Males', '16', '104', '86'], ['Females', '75', '34', '94']], cls='t tiny')
FRT = table([['', 'banana', 'dragon fruit', 'kiwi fruit'], ['adult', '14', '19', '16'], ['child', '23', '11', '17']], cls='t tiny')
P.append(exyt('Example 7 · Representing information in a table by a matrix',
  q('The table opposite shows the three types of membership of a local gym and the number of males and females enrolled in each. Construct a matrix to display the numerical information in the table.') + GYM
  + row(M([['', '', ''], ['', '', '']], rl=['M', 'F'], cl=['W', 'A', 'F']) + ' &nbsp; ' + A(M([[16, 104, 86], [75, 34, 94]], rl=['M', 'F'], cl=['W', 'A', 'F']))),
  'You try 7', q('A group of 100 people were surveyed about their favourite fruit. Their results are shown in the table.') + FRT
  + parts([('a', 'Construct matrix <i>F</i>, to represent the information in the table.', 'F = ' + M([[14, 19, 16], [23, 11, 17]], rl='AC', cl='BDK', side=True), 16),
           ('b', 'Construct a row matrix to represent the favourite fruit of adults surveyed.', M([[14, 19, 16]]), 8)])))
P.append(exyt('Example 8 · Entering a credit card number into a matrix',
  q('Convert the 16-digit credit card number: 4454 8178 1029 3161 into a 2 × 8 matrix, listing the digits in pairs, one under the other. Ignore the spaces.')
  + row(M([['&nbsp;'] * 8, ['&nbsp;'] * 8]) + ' &nbsp; ' + A(M([[4, 5, 8, 7, 1, 2, 3, 6], [4, 4, 1, 8, 0, 9, 1, 1]]))),
  'You try 8', q('Convert the 16-digit credit card number: 5213 7046 9381 2750 into a 2 × 8 matrix, listing the digits in pairs, one under the other. Ignore the spaces.')
  + space(12, M([[5, 1, 7, 4, 9, 8, 2, 5], [2, 3, 0, 6, 3, 1, 7, 0]]))))
P.append(exyt('Example 9 · Representing a network diagram by a matrix',
  q('Represent the network diagram shown opposite as a 4 × 4 matrix <i>M</i>, where the:<br>• matrix element = 1 if the two points are joined by a line<br>• matrix element = 0 if the two points are not connected.')
  + row(IMG('ex9_net.png', 26), M([['&nbsp;'] * 4] * 4, rl='ABCD', cl='ABCD'), A(M([[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]], rl='ABCD', cl='ABCD'))),
  'You try 9', q('Lucas (L), Mayoi (M), Omar (O) and Seb (S) are pen pals and are trying to communicate with one another through letters.<br>• Lucas can send letters directly to Mayoi and Omar.<br>• Mayoi can send letters directly to Lucas, Omar and Seb.<br>• Omar can send letters directly to Lucas, Mayoi and Seb.<br>• Seb can send letters directly to Mayoi and Omar.')
  + parts([('a', 'Construct a communication matrix, <i>C</i>, that represents the direct connections between the four pen pals.', 'C = ' + M([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]], rl='LMOS', cl='LMOS') + ' (rows = from, columns = to)', 22)])))
P.append(exyt('Example 10 · Interpreting a matrix representing a network diagram',
  q('The diagram opposite shows the roads connecting four towns: town A, town B, town C, and town D. This diagram has been represented by a 4 × 4 matrix, <i>M</i>. The elements show the number of roads between each pair of towns.')
  + row(IMG('ex10_net.png', 30), '<i>M</i> = ' + M([[0, 1, 0, 0], [1, 0, 2, 1], [0, 2, 0, 3], [0, 1, 3, 0]], rl='ABCD', cl='ABCD'))
  + parts([('a', 'In the matrix <i>M</i>, <i>m</i><sub>24</sub> = 1. What does this tell us?', 'There is one road between town B and town D.', 'L'),
           ('b', 'In the matrix <i>M</i>, <i>m</i><sub>34</sub> = 3. What does this tell us?', 'There are three roads between town D and town C.', 'L'),
           ('c', 'In the matrix <i>M</i>, <i>m</i><sub>41</sub> = 0. What does this tell us?', 'There is no road between town D and town A.', 'L'),
           ('d', 'What is the sum of the elements in row 3 of matrix <i>M</i> and what does this tell us?', '5: the total number of roads between town C and the other towns.', 8),
           ('e', 'What is the sum of all the elements of matrix <i>M</i> and what does this tell us?', '14: the total number of different ways you can travel between towns.', 8)]),
  'You try 10', q('The roads connecting four towns, town P, town Q, town R and town S, have been represented by a 4 × 4 matrix, <i>M</i>. The elements show the number of roads between each pair of towns.')
  + row('<i>M</i> = ' + M([[0, 2, 1, 0], [2, 0, 0, 1], [1, 0, 0, 3], [0, 1, 3, 0]], rl='PQRS', cl='PQRS'))
  + parts([('a', 'In the matrix <i>M</i>, <i>m</i><sub>14</sub> = 0. What does this tell us?', 'There is no road between town P and town S.', 8),
           ('b', 'In the matrix <i>M</i>, <i>m</i><sub>34</sub> = 3. What does this tell us?', 'There are three roads between town R and town S.', 8),
           ('c', 'What is the sum of the elements in row 2 of matrix <i>M</i> and what does this tell us?', '3: the total number of roads between town Q and the other towns.', 10),
           ('d', 'What is the sum of all the elements of matrix <i>M</i> and what does this tell us?', '14: the total number of different ways you can travel between towns.', 10)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q1a–c', q('A toll road is divided into three sections, <i>E</i>, <i>F</i> and <i>G</i>.<br>The cost, in dollars, to drive one journey on each section is shown in matrix <i>C</i> below.')
  + row('<i>C</i> = ' + M([[3.58], [2.22], [2.87]], rl='EFG', side=True))
  + parts([('a', 'What is the cost of one journey on section <i>G</i>?', '$2.87', 'L'), ('b', 'Write down the order of matrix <i>C</i>.', '3 × 1', 'L'),
           ('c', 'One day Kim travels once on section <i>E</i> and twice on section <i>G</i>. Construct a row matrix that shows this. (adapted)', M([[1, 0, 2]]), 10)]), '3 marks'))
A17 = [[[5,7,9],[8,10,12],[11,13,15]],[[5,8,11],[7,10,13],[9,12,15]],[[3,6,9],[3,6,9],[3,6,9]],[[3,3,3],[6,6,6],[9,9,9]],[[3,6,3],[6,3,9],[3,9,3]]]
P.append(box('Exit task 2 · VCAA 2017 Exam 1 Q6', q('The table below shows information about two matrices, <i>A</i> and <i>B</i>.')
  + table([['Matrix', 'Order', 'Rule'], ['<i>A</i>', '3 × 3', '<i>a<sub>ij</sub></i> = 2<i>i</i> + <i>j</i>'], ['<i>B</i>', '3 × 3', '<i>b<sub>ij</sub></i> = <i>i</i> – <i>j</i>']], cls='t tiny')
  + q('The element in row <i>i</i> and column <i>j</i> of matrix <i>A</i> is <i>a<sub>ij</sub></i>.<br>The element in row <i>i</i> and column <i>j</i> of matrix <i>B</i> is <i>b<sub>ij</sub></i>.<br>The sum <i>A</i> + <i>B</i> is')
  + mc([M(o) for o in A17], 'D', cols=5) + space(16, '') + why('A = [3 4 5; 5 6 7; 7 8 9], B = [0 −1 −2; 1 0 −1; 2 1 0]; add matching elements: rows 3 3 3, 6 6 6, 9 9 9'), '1 mark'))
SC = ['I can state the order of a given matrix.', 'I can find the transpose of a matrix.', 'I can identify a matrix as being a square, column or row matrix.',
      'I can identify a square matrix as being an identity or diagonal or symmetric or upper/lower triangular matrix.', 'I can identify the a<sub>ij</sub> term in a matrix A.',
      'I can construct a matrix given a rule for a<sub>ij</sub>.', 'I can enter a matrix into a CAS calculator.', 'I can enter information from a table into a matrix.',
      'I can represent a network diagram by a matrix.', 'I can interpret a matrix representing a network diagram.']
P.append(close(SC, [('10A', 'Q1–19'), ('10B', 'Q1–12')], ['10A', '10B']))
build('gm12-u4-10a10b', '10A-10B', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-10a10b-worksheet', '10A-10B worksheet'), ('gm12-u4-10a10b-worksheet-solutions', '10A-10B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
