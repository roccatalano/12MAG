"""Lesson gm12-u4-11c (11C) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now and CFAT not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4D #10 (p. 291), 4H #18 (p. 293) (solutions worked for 12MAG); VCAA 2021 E2 Matrices Q3a (Edrolo U1&2 5G Q12).
Examples 4-7 = Cambridge U3&4 pp. 561-566. You trys = Edrolo U3&4 7G WE5 (pp. 484-485), 7G WE7 (p. 485), 7G WE6 (p. 485), 7H WE1 (p. 497).
Exits = VCAA 2016 E2 Matrices Q3a (Edrolo 7G Q19), 2017 E2 Matrices Q3 (7G Q20), 2018 E1 Matrices Q8 (7H Q12), 2020 E2 Matrices Q3d (7H Q14).
Output: lessons/11C worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-11c/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:6mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def LT(m, top, side): return f'<span style="display:inline-flex;flex-direction:column;align-items:center"><i style="font-size:9pt">{top}</i>{m}</span><i style="font-size:9pt">{side}</i>'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-11c')
S_ = lambda n: f'<span style="white-space:nowrap"><i>S</i><sub>{n}</sub></span>'
P = [title('11C', 'Transition matrices: using recursion')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Calculate the following matrix multiplication using a CAS calculator:')
  + row(M([[6, -11, 3, 7], [0, 8, -2, 8]]) + M([[12, -3], [1, 5], [4, -6], [10, -2]]))
  + space(14, M([[143, -105], [80, 36]]))))
P.append(box('Question 2', q('Consider the following matrices: one defining the initial populations in Geelong and Ballarat and the other, a transition matrix defining the proportion of the population moving between the two cities each year. Assume Geelong is listed first.')
  + row(S_(0) + ' = ' + M([['250 000'], ['110 000']]), '<i>T</i> = ' + M([[0.9, 0.15], [0.1, 0.85]]))
  + q('How many people are expected to be in Geelong after five years?')
  + space(16, S_(5) + ' = <i>T</i><sup>5</sup>' + S_(0) + ' = (224 068.4…, 135 931.6…): about 224 068 people')))
P.append(box('Question 3 · VCAA 2021 Exam 2 Q3a', q('A market research study of shoppers showed that the buying preferences for the three olive oils, Carmani (<i>C</i>), Linelli (<i>L</i>) and Ohana (<i>O</i>), change from month to month according to the transition matrix <i>T</i> below.')
  + row('<span><i>T</i> =</span> ' + LT(M([['0.85', '0.10', '0.05'], ['0.05', '0.80', '0.05'], ['0.10', '0.10', '0.90']], cl=['C', 'L', 'O'], rl=['C', 'L', 'O'], side=True), 'this month', 'next month'))
  + q('The initial state matrix ' + S_(0) + ' below shows the number of shoppers who bought each brand of olive oil in July 2021.')
  + row(S_(0) + ' = ' + M([[3200], [2000], [2800]], rl=['C', 'L', 'O'], side=True))
  + q('Let ' + S_('<i>n</i>') + ' represent the state matrix describing the number of shoppers buying each brand <i>n</i> months after July 2021.<br>a. How many of these 8000 shoppers bought a different brand of olive oil in August 2021 from the brand bought in July 2021?')
  + space(14, '0.15 × 3200 + 0.20 × 2000 + 0.10 × 2800 = 480 + 400 + 280 = 1160'), '1 mark'))

P.append(sect('11C Transition matrices – using recursion', 'Example, then you try'))
T4 = M([[0.85, 0.05], [0.15, 0.95]]); S04 = M([[80], [20]])
EX = (Q('The factory has a large number of machines. The machines can be in one of two states: operating (<i>O</i>) or broken (<i>B</i>). Broken machines are repaired and come back into operation and vice versa.<br>At the start, 80 machines are operating and 20 are broken.<br>Use the recursion relation')
  + row(S_(0) + ' = intial value, ' + S_('<i>n</i>+1') + ' = <i>T</i>' + S_('<i>n</i>')) + Q('where') + row(S_(0) + ' = ' + S04, 'and <i>T</i> = ' + T4)
  + Q('to determine the number of operational and broken machines after 1 day and after 3 days.')
  + space(40, S_(1) + ' = <i>T</i>' + S_(0) + ' = (69, 31): after 1 day, 69 operational and 31 broken.<br>' + S_(2) + ' = <i>T</i>' + S_(1) + ' = (60.2, 39.8); ' + S_(3) + ' = <i>T</i>' + S_(2) + ' = (53.16, 46.84): after 3 days, 53 operating and 47 broken.'))
YT = (Q('Every night, a colony of seals can settle on either island A or island B. On Sunday, there were 130 seals on island A and 180 seals on island B.<br>The initial state and transition matrices are provided.')
  + row(S_(0) + ' = ' + M([[130], [180]], rl=['A', 'B'], side=True), '<i>T</i> = ' + LT(M([[0.2, 0.6], [0.8, 0.4]], cl=['A', 'B'], rl=['A', 'B'], side=True), 'today', 'tomorrow'))
  + parts([('a', 'Determine the matrix recurrence relation that can be used to calculate the number of seals on each island every day.', S_(0) + ' = (130, 180), ' + S_('<i>n</i>+1') + ' = ' + M([[0.2, 0.6], [0.8, 0.4]]) + ' × ' + S_('<i>n</i>'), 'L'),
           ('b', 'Use recursion to calculate the number of seals on each island on Tuesday, rounded to the nearest whole number.', S_(1) + ' = (134, 176), ' + S_(2) + ' = (132.4, 177.6): A 132 seals, B 178 seals', 'L')]))
P.append(exyt('Example 4 · State matrices step by step', EX, 'You try 1', YT))
EX = (Q('The factory has a large number of machines. The machines can be in one of two states: operating (<i>O</i>) or broken (<i>B</i>). Broken machines are repaired and come back into operation and vice versa.<br>Initially, 80 machines are operating and 20 are broken, so:')
  + row(S_(0) + ' = ' + S04, 'and <i>T</i> = ' + T4) + Q('Determine the number of operational and broken machines after 10 days.')
  + space(28, S_(10) + ' = <i>T</i><sup>10</sup>' + S_(0) + ' = (30.9056, 69.0944): after 10 days, 31 operational and 69 broken.'))
YT = (Q('Consider the following initial state matrix and transition matrix.') + row(S_(0) + ' = ' + M([[213], [142]]), '<i>T</i> = ' + M([[0.3, 0.9], [0.7, 0.1]]))
  + Q('Determine ' + S_(10) + ', rounding the matrix elements to the nearest whole number.')
  + space(28, S_(10) + ' = <i>T</i><sup>10</sup> × ' + S_(0) + ' = (199.76…, 155.23…) → ' + M([[200], [155]])))
P.append(exyt('Example 5 · The nth state: S<sub>n</sub> = T<sup>n</sup>S<sub>0</sub>', EX, 'You try 2', YT))
EX = (Q('We have a transition matrix') + row('<span><i>T</i> =</span> ' + M([[0.6, 0.3], [0.4, 0.7]])) + Q('and we know that the state matrix') + row(S_(4) + ' = ' + M([['25 587'], ['34 413']]))
  + Q('Determine ' + S_(3) + ' and ' + S_(2) + '.')
  + space(30, S_(3) + ' = <i>T</i><sup>−1</sup>' + S_(4) + ' = (25 290, 34 710); ' + S_(2) + ' = <i>T</i><sup>−1</sup>' + S_(3) + ' = (24 300, 35 700)'))
YT = (Q('Consider the following state matrix after 3 periods, ' + S_(3) + ', and transition matrix, <i>T</i>.') + row(S_(3) + ' = ' + M([[120], [150]]), '<i>T</i> = ' + M([[0.84, 0.21], [0.16, 0.79]]))
  + Q('Determine ' + S_(2) + ', rounding the matrix elements to the nearest whole number.')
  + space(30, S_(2) + ' = <i>T</i><sup>−1</sup> × ' + S_(3) + ' = (100.47…, 169.52…) → ' + M([[100], [170]])))
P.append(exyt('Example 6 · Using the inverse of a transition matrix', EX, 'You try 3', YT))
EX = (Q('For the car rental problem:') + row(S_(0) + ' = ' + M([[50], [40]]), 'and <i>T</i> = ' + M([[0.8, 0.1], [0.2, 0.9]]))
  + Q('Estimate the steady-state solution by calculating ' + S_('<i>n</i>') + ' for <i>n</i> = 10, 15, 17 and 18.')
  + space(30, S_(10) + ' = (30.6, 59.4), ' + S_(15) + ' = (30.1, 59.9), ' + S_(17) + ' = (30.0, 60.0), ' + S_(18) + ' = (30.0, 60.0): steady state 30 cars in Bendigo, 60 in Colac'))
YT = (Q('If ' + S_(0) + ' = ' + M([[29], [32]]) + ' and <i>T</i> = ' + M([[0.7, 0.2], [0.3, 0.8]]) + ', calculate the equilibrium state matrix.')
  + space(30, S_(30) + ' = <i>T</i><sup>30</sup>' + S_(0) + ' = (24.4, 36.6) and ' + S_(31) + ' = (24.4, 36.6): equilibrium ' + M([[24.4], [36.6]])))
P.append(exyt('Example 7 · Estimating the steady-state solution', EX, 'You try 4', YT))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 2 Q3a', q('The travel company is studying the choice between air (<i>A</i>), land (<i>L</i>), sea (<i>S</i>) or no (<i>N</i>) travel by some of its customers each year.<br>Matrix <i>T</i>, shown below, contains the percentages of customers who are expected to change their choice of travel from year to year.')
  + row('<span><i>T</i> =</span> ' + LT(M([['0.65', '0.25', '0.25', '0.50'], ['0.15', '0.60', '0.20', '0.15'], ['0.05', '0.10', '0.25', '0.20'], ['0.15', '0.05', '0.30', '0.15']], cl=list('ALSN'), rl=list('ALSN'), side=True), 'this year', 'next year'))
  + q('Let ' + S_('<i>n</i>') + ' be the matrix that shows the number of customers who choose each type of travel <i>n</i> years after 2014.<br>Matrix ' + S_(0) + ' below shows the number of customers who chose each type of travel in 2014.')
  + row(S_(0) + ' = ' + M([[520], [320], [80], [80]], rl=list('ALSN'), side=True))
  + q('Matrix ' + S_(1) + ' below shows the number of customers who chose each type of travel in 2015.')
  + row(S_(1) + ' = <i>T</i>' + S_(0) + ' = ' + M([[478], ['<i>d</i>'], ['<i>e</i>'], ['<i>f</i>']], rl=list('ALSN'), side=True))
  + q('a. Write the values missing from matrix ' + S_(1) + ' (<i>d</i>, <i>e</i>, <i>f</i>) in the boxes provided below.')
  + row('<i>d</i> = ☐', '<i>e</i> = ☐', '<i>f</i> = ☐') + space(10, '<i>d</i> = 298, <i>e</i> = 94, <i>f</i> = 130'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2017 Exam 2 Q3', q('Senior students at this school will also choose one elective activity in each of the four terms in 2018.<br>Their choices are communication (<i>C</i>), investigation (<i>I</i>), problem-solving (<i>P</i>) and service (<i>S</i>).<br>The transition matrix <i>T</i> shows the way in which senior students are expected to change their choice of elective activity from term to term.')
  + row('<span><i>T</i> =</span> ' + LT(M([[0.4, 0.2, 0.3, 0.1], [0.2, 0.4, 0.1, 0.3], [0.2, 0.3, 0.3, 0.4], [0.2, 0.1, 0.3, 0.2]], cl=list('CIPS'), rl=list('CIPS'), side=True), 'this term', 'next term'))
  + q('Let ' + S_('<i>n</i>') + ' be the state matrix for the number of senior students expected to choose each elective activity in Term <i>n</i>.<br>For the given matrix ' + S_(1) + ', a matrix rule that can be used to predict the number of senior students in each elective activity in Terms 2, 3 and 4 is')
  + row(S_(1) + ' = ' + M([[300], [200], [200], [300]]) + ',', S_('<i>n</i>+1') + ' = <i>T</i>' + S_('<i>n</i>'))
  + parts([('a', 'How many senior students will <b>not</b> change their elective activity from Term 1 to Term 2? (1 mark)', '0.4 × 300 + 0.4 × 200 + 0.3 × 200 + 0.2 × 300 = 320', 'L'),
           ('b', 'Complete ' + S_(2) + ', the state matrix for Term 2, below. (1 mark)' + row(S_(2) + ' = ' + M([['____'], ['____'], ['____'], ['____']], rl=list('CIPS'), side=True)), S_(2) + ' = (250, 250, 300, 200)', 4),
           ('c', 'Of the senior students expected to choose investigation (<i>I</i>) in Term 3, what percentage chose service (<i>S</i>) in Term 2? (2 marks)', S_(3) + ' = (260, 240, 295, 205); 0.3 × 200 = 60; 60 ÷ 240 = 25%', 'L'),
           ('d', 'What is the maximum number of senior students expected in investigation (<i>I</i>) at any time during 2018? (1 mark)', '250 (Term 2)', 'L')]), '5 marks'))
P.append(box('Exit task 3 · VCAA 2018 Exam 1 Q8', q('A public library organised 500 of its members into five categories according to the number of books each member borrows each month.<br>These categories are<br>'
  '&emsp;<i>J</i> = no books borrowed per month<br>&emsp;<i>K</i> = one book borrowed per month<br>&emsp;<i>L</i> = two books borrowed per month<br>&emsp;<i>M</i> = three books borrowed per month<br>&emsp;<i>N</i> = four or more books borrowed per month<br>'
  'The transition matrix, <i>T</i>, below shows how the number of books borrowed per month by the members is expected to change from month to month.')
  + row('<span><i>T</i> =</span> ' + LT(M([[0.1, 0.2, 0.2, 0, 0], [0.5, 0.2, 0.3, 0.1, 0], [0.3, 0.3, 0.4, 0.1, 0.2], [0.1, 0.2, 0.1, 0.6, 0.3], [0, 0.1, 0, 0.2, 0.5]], cl=list('JKLMN'), rl=list('JKLMN'), side=True), 'this month', 'next month'))
  + q('In the long term, which category is expected to have approximately 96 members each month?')
  + mc(['<i>J</i>', '<i>K</i>', '<i>L</i>', '<i>M</i>', '<i>N</i>'], 'B', cols=5) + space(12, 'steady state with 500 members (e.g. 100 in each): (49, 96, 124, 151, 80), so K'), '1 mark'))
P.append(box('Exit task 4 · VCAA 2020 Exam 2 Q3d', q('An offer to buy the Westmall shopping centre was made by a competitor.<br>One market research project suggested that if the Westmall shopping centre were sold, each of the three centres (Westmall, Grandmall and Eastmall) would continue to have regular shoppers but would attract and lose shoppers on a weekly basis.<br>Let ' + S_('<i>n</i>') + ' be the state matrix that shows the expected number of shoppers at each of the three centres <i>n</i> weeks after Westmall is sold.<br>A matrix recurrence relation that generates values of ' + S_('<i>n</i>') + ' is')
  + row(S_('<i>n</i>+1') + ' = <i>T</i> × ' + S_('<i>n</i>'))
  + row('where <i>T</i> = ' + LT(M([['0.80', '0.09', '0.10'], ['0.12', '0.79', '0.10'], ['0.08', '0.12', '0.80']], cl=list('WGE'), rl=list('WGE'), side=True), 'this week', 'next week'), S_(0) + ' = ' + M([['250 000'], ['230 000'], ['200 000']], rl=list('WGE'), side=True))
  + q('d. In the long term, what is the expected weekly number of shoppers at Westmall?<br>Round your answer to the nearest whole number.')
  + space(14, '<i>T</i><sup>100</sup>' + S_(0) + ' = (218 884.1…, 233 476.4…, 227 639.5…): 218 884 shoppers'), '1 mark'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('11C', 'Q1–11')], ['11C']))
build('gm12-u4-11c', '11C', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-11c-worksheet', '11C worksheet'), ('gm12-u4-11c-worksheet-solutions', '11C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
