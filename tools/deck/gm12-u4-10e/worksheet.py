"""Lesson gm12-u4-10e (10E) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4D #11 (p. 291), 4E #12 (p. 292) (solutions worked for 12MAG); VCAA 2017 Exam 2 Matrices Q1ci (Edrolo U1&2 5F Q15).
Examples 24-27 = Cambridge U3&4 Examples 24-27 (pp. 513-520).
You trys = YT-10E-24 (written), Edrolo U3&4 7D WE1a, 7D WE2, 7D WE1b (CAS), Edrolo U1&2 5F WE1 + WE2.
Exits = VCAA 2018 Exam 1 Matrices Q1 (Edrolo 7D Q15), VCAA 2020 Exam 2 Matrices Q2 (7D Q16), VCAA 2016 Exam 1 Matrices Q3 (7D Q17).
Output: lessons/10E worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-10e/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def FR(n, d): return f'<span style="display:inline-flex;flex-direction:column;align-items:center;line-height:1.05;vertical-align:middle;margin:0 2px"><span>{n}</span><span style="border-top:1px solid currentColor;padding:0 2px">{d}</span></span>'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-10e')
I2 = M([[1, 0], [0, 1]])
P = [title('10E', 'Matrix inverse, the determinant and matrix equations')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Construct an identity matrix of size 3×3.') + space(14, M([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))))
P.append(box('Question 2', q('Find the inverse of the matrix') + row(M([[7, 2], [-1, 3]]))
  + space(18, 'det = 7 × 3 − 2 × (−1) = 23; inverse = ' + FR(1, 23) + M([[3, -2], [1, 7]]))))
P.append(box('Question 3 · VCAA 2017 Exam 2 Q1ci', q('Consider the matrix equation') + row(M([[35, 24, 60], [28, 32, 43], [32, 30, 56]]) + ' × ' + M([['a'], ['b'], ['c']]) + ' = ' + M([['491.55'], ['428.00'], ['487.60']]))
  + q('where <i>a</i> = cost of one pie, <i>b</i> = cost of one roll and <i>c</i> = cost of one sandwich.<br>What is the cost of one sandwich?')
  + space(12, 'X = M⁻¹B gives a = 4.65, b = 4.20, c = 3.80: one sandwich costs $3.80'), '1 mark'))

P.append(sect('10E Inverse, determinant and matrix equations', 'Example, then you try'))
P.append(exyt('Example 24 · Demonstrating that two matrices are inverses',
  Q('Show that the matrices <i>A</i> = ' + M([[2, 3], [3, 5]]) + ' and <i>B</i> = ' + M([[5, -3], [-3, 2]]) + ' are inverses.')
  + row('<i>AB</i> = ' + M([['2 × 5 + 3 × (−3)', '2 × (−3) + 3 × 2'], ['3 × 5 + 5 × (−3)', '3 × (−3) + 5 × 2']]) + ' = ' + A(I2))
  + row('<i>BA</i> = ' + M([['5 × 2 + (−3) × 3', '5 × 3 + (−3) × 5'], ['(−3) × 2 + 2 × 3', '(−3) × 3 + 2 × 5']]) + ' = ' + A(I2))
  + q(A('<i>AB</i> = <i>I</i> and <i>BA</i> = <i>I</i>, so <i>A</i> and <i>B</i> are inverses.')),
  'You try 24', Q('Show that the matrices <i>A</i> = ' + M([[3, 5], [1, 2]]) + ' and <i>B</i> = ' + M([[2, -5], [-1, 3]]) + ' are inverses.')
  + space(30, 'AB = ' + I2 + ' and BA = ' + I2 + ', so A and B are inverses.')))
P.append(exyt('Example 25 · Finding the determinant of a 2 × 2 matrix',
  q('Find the determinant of the matrices:')
  + Q('a <i>A</i> = ' + M([[2, 3], [3, 5]]) + ' det(<i>A</i>) = 2 × 5 − 3 × 3 = ' + A('1'))
  + Q('b <i>B</i> = ' + M([[2, 3], [2, 3]]) + ' det(<i>B</i>) = 2 × 3 − 2 × 3 = ' + A('0'))
  + Q('c <i>C</i> = ' + M([[2, 4], [2, 3]]) + ' det(<i>C</i>) = 2 × 3 − 2 × 4 = ' + A('−2')),
  'You try 25', row('<i>A</i> = ' + M([[4, 2, 13], [6, 0, 0], [0, 0, 3]]), '<i>B</i> = ' + M([[2, 2], [3, 1]]))
  + q('a. Find the determinant of <i>B</i>.') + space(16, 'det(B) = 2 × 1 − 2 × 3 = −4')))
P.append(exyt('Example 26 · Using the rule to find the inverse of a 2 × 2 matrix',
  q('Find the inverse of the following matrices.')
  + Q('a <i>A</i> = ' + M([[2, 2], [3, 4]])) + q('det(<i>A</i>) = 2 × 4 − 3 × 2 = 2')
  + row('<i>A</i><sup>−1</sup> = ' + FR(1, 2) + M([[4, -2], [-3, 2]]) + ' = ' + A(M([[2, -1], [-1.5, 1]])))
  + Q('b <i>B</i> = ' + M([[2, 3], [2, 3]])) + q('det(<i>B</i>) = 2 × 3 − 2 × 3 = 0 → ' + A('<i>B</i> does not have an inverse.')),
  'You try 26', row('<i>A</i> = ' + M([[7, 5], [2, 3]]))
  + parts([('a', 'Does the inverse of <i>A</i> exist?', 'Yes: det(A) = 21 − 10 = 11 ≠ 0', 12),
           ('b', 'Calculate <i>A</i><sup>−1</sup>.', 'A⁻¹ = ' + FR(1, 11) + M([[3, -5], [-2, 7]]), 18)])))
P.append(box('You try (CAS)', row('<i>A</i> = ' + M([[4, 2, 13], [6, 0, 0], [0, 0, 3]]), '<i>B</i> = ' + M([[2, 2], [3, 1]]))
  + q('b. Use a CAS to find the determinant of <i>A</i>.') + space(10, 'det(A) = −36')))
G27 = row('Let <i>A</i> = ' + M([[1, 2, 1], [2, 1, 3], [1, 1, 1]]), '<i>B</i> = ' + M([[2, 1], [3, 2]]), '<i>C</i> = ' + M([[8, -1], [4, 6]]), '<i>D</i> = ' + M([[2], [3]]), 'and <i>E</i> = ' + M([[2], [3], [1]]))
BI = M([[2, -1], [-3, 2]])
P.append(exyt('Example 27 · Solving matrix equations',
  G27 + q('Solve each of the following matrix equations for <i>X</i>') + row('<i>B</i><sup>−1</sup> = ' + BI + ' (det(<i>B</i>) = 1)')
  + Q('a <i>B</i> + <i>X</i> = <i>C</i> → <i>X</i> = <i>C</i> − <i>B</i> = ' + A(M([[6, -2], [1, 4]])))
  + Q('b <i>BX</i> = <i>C</i> → <i>X</i> = <i>B</i><sup>−1</sup><i>C</i> = ' + A(M([[12, -8], [-16, 15]])))
  + Q('c <i>XB</i> = <i>C</i> → <i>X</i> = <i>CB</i><sup>−1</sup> = ' + A(M([[19, -10], [-10, 8]])))
  + Q('d <i>BX</i> = <i>D</i> → <i>X</i> = <i>B</i><sup>−1</sup><i>D</i> = ' + A(M([[1], [0]])))
  + Q('e <i>AX</i> = <i>E</i> → <i>X</i> = <i>A</i><sup>−1</sup><i>E</i> = ' + A(M([[-2], [1], [2]])))
  + Q('f <i>BX</i> + ' + M([[4], [5]]) + ' = <i>D</i> → <i>X</i> = <i>B</i><sup>−1</sup>(<i>D</i> − ' + M([[4], [5]]) + ') = ' + A(M([[-2], [2]]))),
  'You try 27', Q('If <i>A</i> = ' + M([[5, -3], [4, 2]]) + ' and <i>B</i> = ' + M([[5, 2], [6, 10]]) + ', solve the following matrix equations for <i>X</i>.')
  + parts([('a', '<i>A</i> + <i>X</i> = <i>B</i>', 'X = B − A = ' + M([[0, 5], [2, 8]]), 18), ('b', '3<i>X</i> = <i>A</i>', 'X = ⅓A = ' + M([[FR(5, 3), -1], [FR(4, 3), FR(2, 3)]]), 18)])
  + '<div class="qsep"></div>' + Q('Consider the matrix equation <i>AX</i> = <i>B</i>. If <i>A</i> = ' + M([[4, -1], [2, 3]]) + ' and <i>B</i> = ' + M([[18], [16]]) + ', solve for matrix <i>X</i>.')
  + space(24, 'X = A⁻¹B = ' + FR(1, 14) + M([[3, 1], [-2, 4]]) + M([[18], [16]]) + ' = ' + M([[5], [2]]))))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q1', q('Which of the following matrices has a determinant of zero?')
  + mc([M([[0, 1], [1, 0]]), M([[1, 0], [0, 1]]), M([[1, 2], [-3, 6]]), M([[3, 6], [2, 4]]), M([[4, 0], [0, -2]])], 'D', cols=5) + why('3 × 4 − 6 × 2 = 0'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q2', q('The preferred number of cafes (<i>x</i>) and sandwich bars (<i>y</i>) in Grandmall’s food court can be determined by solving the following equations written in matrix form.')
  + row(M([[5, -9], [4, -7]]) + M([['x'], ['y']]) + ' = ' + M([[7], [6]]))
  + parts([('a', 'The value of the determinant of the 2 × 2 matrix is 1.<br>Use this information to explain why this matrix has an inverse. (1 mark)', 'The determinant is not zero, so the matrix has an inverse.', 12),
           ('b', 'Write the three missing values of the inverse matrix that can be used to solve these equations. (1 mark) ' + M([['&nbsp;&nbsp;', 9], ['&nbsp;&nbsp;', '&nbsp;&nbsp;']]), M([[-7, 9], [-4, 5]]), 12),
           ('c', 'Determine the preferred number of sandwich bars for Grandmall’s food court. (1 mark)', M([[-7, 9], [-4, 5]]) + M([[7], [6]]) + ' = ' + M([[5], [2]]) + ': 2 sandwich bars', 14)]), '3 marks'))
P.append(box('Exit task 3 · VCAA 2016 Exam 1 Q3', q('The following matrix equation represents a pair of simultaneous linear equations.')
  + row(M([[12, 9], ['m', 3]]) + M([['x'], ['y']]) + ' = ' + M([[6], [6]]))
  + q('These simultaneous linear equations have no unique solution when <i>m</i> is equal to')
  + mc(['−4', '−3', '0', '3', '4'], 'E', cols=5) + why('no unique solution → det = 0: 36 − 9m = 0, m = 4'), '1 mark'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('10E', 'Q1–14')], ['10E']))
build('gm12-u4-10e', '10E', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-10e-worksheet', '10E worksheet'), ('gm12-u4-10e-worksheet-solutions', '10E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
