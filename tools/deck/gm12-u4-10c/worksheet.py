"""Lesson gm12-u4-10c (10C) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 skills checklist 4B #3, 4C #6 (solutions worked for 12MAG); VCAA 2021 Exam 2 Matrices Q1b (original wording; Edrolo U1&2 5B Q15 adapted).
Examples 11-16 = Cambridge U3&4 Examples 11-16 (pp. 491-496).
You trys = Edrolo U1&2 5B WE3, 5B WE2, Edrolo U3&4 7B WE1a-b, 7B WE2, YT-10C-15 (written), YT-10C-16 (written).
Exits = VCAA 2019 Exam 1 Matrices Q1 (Edrolo U3&4 7B Q13), VCAA 2016 Exam 1 Matrices Q1 (Edrolo 7B Q14).
Output: lessons/10C worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-10c/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join(xs) + '</div>'

P = [title('10C', 'Matrix arithmetic: addition, subtraction and scalar multiplication')]
P.append(lis(['To be able to establish when two matrices are equal.', 'To be able to recognise when matrix addition and subtraction are defined and to perform these operations.',
              'To be able to undertake scalar multiplication.', 'To be able to identify zero matrices.',
              'To be able to undertake addition, subtraction and multiplication by a scalar with a CAS calculator.',
              'To be able to use the operations of addition, subtraction and scalar multiplication of matrices in practical situations.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Complete the following matrix addition.') + row(M([[2, 4], [5, 1]]), '+', M([[9, 8], [9, -1]]), '=') + space(12, M([[11, 12], [14, 0]]))))
P.append(box('Question 2', Q('If <i>A</i> = ' + M([[5, 3], [-2, 0]]) + ' and <i>B</i> = ' + M([[2, -1], [0, 1]]) + ', then find 2<i>A</i> + 3<i>B</i>.')
  + space(16, '2A + 3B = ' + M([[10, 6], [-4, 0]]) + ' + ' + M([[6, -3], [0, 3]]) + ' = ' + M([[16, 3], [-4, 3]]))))
P.append(box('Question 3 · VCAA 2021 Exam 2 Q1b', q('Elena imports three brands of olive oil: Carmani (<i>C</i>), Linelli (<i>L</i>) and Ohana (<i>O</i>).<br>The number of 1 litre bottles of these oils sold in January 2021 is shown in matrix <i>J</i> below.')
  + row('<i>J</i> = ' + M([[2800], [1700], [2400]], rl='CLO', side=True))
  + q('b. Elena expected that in February 2021 the sales of all three brands of olive oil would increase by 5%.<br>She multiplied matrix <i>J</i> by a scalar value, <i>k</i>, to determine the expected volume of sales for February.<br>Write down the value of the scalar <i>k</i>.')
  + space(8, 'k = 1.05 (100% + 5%)'), '1 mark'))

P.append(sect('10C Matrix arithmetic', 'Example, then you try'))
P.append(exyt('Example 11 · Equality of two matrices',
  q('Given that') + row(M([[2, '<i>a</i>'], [8, '<i>b</i> + 1']]), '=', M([[2, 10], [20, 7]])) + q('find the value of <i>a</i> and the value of <i>b</i>.')
  + q('<i>a</i> = ' + A('10') + ' &nbsp; <i>b</i> + 1 = ' + A('7') + ', so <i>b</i> = ' + A('6')),
  'You try 11', q('Consider the following matrix equation.') + row(M([[1, '<i>a</i>'], [-3, 7]]), '+', M([[6, 3], [5, 8]]), '=', M([[7, 1], [2, 15]]))
  + q('What is the value of <i>a</i>?') + space(14, 'a + 3 = 1, so a = −2')))
A12 = [[2, 3, 0], [1, 4, 2]]; B12 = [[1, 2, 3], [2, -2, 1]]
P.append(exyt('Example 12 · Adding two matrices',
  row(M(A12, name='A'), M(B12, name='B')) + q('Find <i>A</i> + <i>B</i>.')
  + row('<span><i>A</i> + <i>B</i> = ' + M([['&nbsp;&nbsp;&nbsp;'] * 3] * 2) + ' = ' + A(M([[3, 5, 3], [3, 2, 3]])) + '</span>'),
  'You try 12', Q('If <i>A</i> = ' + M([[2, 0], [0, 4], [6, 7]]) + ' and <i>B</i> = ' + M([[8, 3], [2, 9], [4, 2]]) + ', find <i>A</i> + <i>B</i>.')
  + space(18, M([[10, 3], [2, 13], [10, 9]]))))
P.append(exyt('Example 13 · Subtracting two matrices',
  row(M(A12, name='A'), M(B12, name='B')) + q('Find <i>A</i> − <i>B</i>.')
  + row('<span><i>A</i> − <i>B</i> = ' + M([['&nbsp;&nbsp;&nbsp;'] * 3] * 2) + ' = ' + A(M([[1, 1, -3], [-1, 6, 1]])) + '</span>'),
  'You try 13', Q('Consider the matrices <i>A</i> = ' + M([[2, 2], [1, 4], [5, 3]]) + ' and <i>B</i> = ' + M([[4, 1], [0, 2], [4, 5]]) + '.')
  + parts([('a', 'Is <i>A</i> + <i>B</i> defined?', 'Yes: both are 3 × 2 (same order)', 8), ('b', 'If possible, calculate <i>A</i> − <i>B</i>.', M([[-2, 1], [1, 2], [1, -2]]), 18)])))
C14 = [[4, -4], [-2, 6]]
P.append(exyt('Example 14 · Scalar multiplication',
  row(M(A12, name='A'), M(C14, name='C')) + q('Find 3<i>A</i> and 0.5<i>C</i>.')
  + row('<span>3<i>A</i> = ' + A(M([[6, 9, 0], [3, 12, 6]])) + '</span>', '<span>0.5<i>C</i> = ' + A(M([[2, -2], [-1, 3]])) + '</span>') + space(6, ''),
  'You try 14', Q('Given that <i>C</i> = ' + M([[2, 1, 3], [4, 5, 2], [1, 0, 4]]) + ', calculate 3<i>C</i>.') + space(18, M([[6, 3, 9], [12, 15, 6], [3, 0, 12]]))))
P.append(exyt('Example 15 · The zero matrix',
  row(M([[6, 0], [-4, 2]], name='G'), M([[9, 0], [-6, 3]], name='H')) + q('Show that 3<i>G</i> − 2<i>H</i> = <i>O</i>.')
  + row('<span>3<i>G</i> − 2<i>H</i> = ' + M([['&nbsp;&nbsp;&nbsp;'] * 2] * 2) + ' − ' + M([['&nbsp;&nbsp;&nbsp;'] * 2] * 2) + ' = ' + A(M([[0, 0], [0, 0]])) + '</span>')
  + q(A('18 − 18 = 0, 0 − 0 = 0, −12 − (−12) = 0, 6 − 6 = 0, so 3G − 2H = O')),
  'You try 15', Q('<i>G</i> = ' + M([[4, 0], [-2, 6]]) + ', <i>H</i> = ' + M([[6, 0], [-3, 9]]) + '. Show that 3<i>G</i> − 2<i>H</i> = <i>O</i>.')
  + space(20, M([[12, 0], [-6, 18]]) + ' − ' + M([[12, 0], [-6, 18]]) + ' = ' + M([[0, 0], [0, 0]]) + ', so 3G − 2H = O')))
def sales(names, a, b, ya, yb):
    t = [['', ya, '', '', yb, '', ''], [f'<i>{names[0]}</i>'] + [f'<i>{s}</i>' for s in names[1]] * 2]
    t += [[n] + [str(v) for v in ra + rb] for n, ra, rb in zip(names[2], a, b)]
    return table(t, cls='t tiny')
A16 = [[24, 32, 11], [32, 34, 9]]; B16 = [[26, 38, 16], [35, 41, 12]]
A16y = [[18, 25, 9], [27, 22, 14]]; B16y = [[22, 30, 12], [28, 26, 16]]
P.append(exyt('Example 16 · Processing data using addition, subtraction and scalar multiplication',
  q('The sales data for two used car dealers, Honest Joe’s and Super Deals, are displayed below.') + sales(('Car sales', ('Small', 'Medium', 'Large'), ('Honest Joe’s', 'Super Deals')), A16, B16, '2014', '2015')
  + parts([('a', 'Construct two matrices, <i>A</i> and <i>B</i>, to represent the sales data for 2014 and 2015 separately.', 'A = ' + M(A16) + ' &nbsp; B = ' + M(B16), 14),
           ('b', 'Construct a new matrix <i>C</i> = <i>A</i> + <i>B</i>. What does this matrix represent?', 'C = ' + M([[50, 70, 27], [67, 75, 21]]) + ': total sales for 2014 and 2015 for the two dealers.', 14),
           ('c', 'Construct a new matrix, <i>D</i> = <i>B</i> − <i>A</i>. What does this matrix represent?', 'D = ' + M([[2, 6, 5], [3, 7, 3]]) + ': the increase in sales from 2014 to 2015 for the two dealers.', 14),
           ('d', 'Both dealers want to increase their 2015 sales by 50% by 2016. Construct a new matrix <i>E</i> = 1.5<i>B</i>. Explain why this matrix represents the planned sales figures for 2016.',
            'E = ' + M([[39, 57, 24], [52.5, 61.5, 18]]) + ': multiplying each element by 1.5 increases each value by 50%.', 16)]),
  'You try 16', q('The bread sales (small, medium, large loaves) for two bakeries are displayed below.') + sales(('Bread sales', ('Small', 'Medium', 'Large'), ('Corner Bake', 'Daily Loaf')), A16y, B16y, '2024', '2025')
  + parts([('a', 'Construct two matrices, <i>A</i> and <i>B</i>, to represent the sales data for 2024 and 2025 separately.', 'A = ' + M(A16y) + ' &nbsp; B = ' + M(B16y), 14),
           ('b', 'Construct a new matrix <i>C</i> = <i>A</i> + <i>B</i>. What does this matrix represent?', 'C = ' + M([[40, 55, 21], [55, 48, 30]]) + ': total sales for 2024 and 2025 for the two bakeries.', 16),
           ('c', 'Construct a new matrix, <i>D</i> = <i>B</i> − <i>A</i>. What does this matrix represent?', 'D = ' + M([[4, 5, 3], [1, 4, 2]]) + ': the increase in sales from 2024 to 2025 for the two bakeries.', 16),
           ('d', 'Both bakeries want to increase their 2025 sales by 50% by 2026. Construct a new matrix <i>E</i> = 1.5<i>B</i>. Explain why this matrix represents the planned sales figures for 2026.',
            'E = ' + M([[33, 45, 18], [42, 39, 24]]) + ': each 2025 figure × 1.5 (a 50% increase) gives the planned 2026 sales.', 18)])))

P.append(sect('Exit tasks', 'Show what you know'))
X1 = [M([[8], [12]]) + ' + ' + M([[4], [2]]), M([[8], [12]]) + ' + ' + M([[4, 0], [0, 2]]), M([[8, 0], [12, 0]]) + ' + ' + M([[4], [2]]), M([[8, 0], [12, 0]]) + ' + ' + M([[4, 0], [0, 2]])]
P.append(box('Exit task 1 · VCAA 2019 Exam 1 Q1', q('Consider the following four matrix expressions.') + row(*X1) + q('How many of these four matrix expressions are defined?')
  + mc(['0', '1', '2', '3', '4'], 'C', cols=5) + why('only the first (2 × 1 + 2 × 1) and the last (2 × 2 + 2 × 2) have matching orders'), '1 mark'))
OP14 = [[[13, 19, 8], [2, 7, 10]], [[10, 7, 2], [8, 19, 13]], [[2, 13], [7, 19], [10, 8]], [[13, 2], [19, 7], [8, 10]], [[8, 10], [19, 7], [13, 2]]]
P.append(box('Exit task 2 · VCAA 2016 Exam 1 Q1', Q('The transpose of ' + M([[2, 7, 10], [13, 19, 8]]) + ' is')
  + mc([M(o) for o in OP14], 'C', cols=5) + why('rows become columns: row 1 (2, 7, 10) becomes column 1'), '1 mark'))
SC = ['I can recognise when two matrices are equal and use this to solve problems.', 'I can add two matrices of the same order together.',
      'I can subtract one matrix from another when they have the same order.', 'I can multiply a matrix by a scalar.',
      'I recognise the role of the zero matrix and can undertake operations using the zero matrix.', 'I can use addition, subtraction and scalar multiplication to process data.']
P.append(close(SC, [('10C', 'Q1–11')], ['10C']))
build('gm12-u4-10c', '10C', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-10c-worksheet', '10C worksheet'), ('gm12-u4-10c-worksheet-solutions', '10C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
