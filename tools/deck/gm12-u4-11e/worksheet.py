"""Lesson gm12-u4-11e (11E Leslie matrices) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from mx.py,
life cycle diagrams from tools/deck/leslie.py. Same items and order as build.py (Do Now not on the worksheet; no CAS steps; no exit task).
Sources (not printed): APK = Cambridge U1&2 Ch 4 checklist 4D #8. Examples 9-13 = Cambridge U3&4 pp. 578-582.
You try 1 = Edrolo U3&4 7G WE8 (pp. 486-488); You try 2-5 = written for 12MAG (planner/written-youtrys.json YT-11E-10..13).
Output: lessons/11E worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-11e/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
from leslie import lifecycle
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def V(v): return M([[x] for x in v])
def row(*xs): return '<div style="display:flex;gap:6mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-11e')
S_ = lambda n: f'<i>S</i><sub>{n}</sub>'
LC = lambda b, s: f'<div style="width:62mm;margin:0 auto">{lifecycle(b, s, w=330, fs=13, color=("#c00", "#c00"))}</div>'
def tab(head, rows):
    td = 'style="border:1px solid #999;padding:0.5mm 2mm;text-align:center"'
    return ('<table style="border-collapse:collapse;font-size:9pt;margin:1.5mm auto"><tr><th ' + td + '>Age group (years)</th>' + ''.join(f'<td {td}>{h}</td>' for h in head) + '</tr>'
            + ''.join(f'<tr><th {td}>{r[0]}</th>' + ''.join(f'<td {td}>{x}</td>' for x in r[1:]) + '</tr>' for r in rows) + '</table>')
P = [title('11E', 'Leslie matrices')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skill'))
P.append(box('Question 1', q('Determine the order of the answer matrix for the following matrix multiplication:')
  + row(M([[9, -11], [8, 3]]) + M([[7, -6, 2, -2], [4, -3, 1, 5]])) + space(12, '2 × 2 by 2 × 4: inner numbers match, so the answer matrix is 2 × 4')))

P.append(sect('11E Leslie matrices', 'Examples, then you try'))
L9 = [[0, '1.8', '2.6', '0.1'], ['0.2', 0, 0, 0], [0, '0.4', 0, 0], [0, 0, '0.3', 0]]
EX = (q('Use the Leslie matrix and initial state matrix below to answer the following questions.')
  + row('<i>L</i> = ' + M(L9), S_(0) + ' = ' + V([1000, 0, 0, 0]))
  + parts([('a', 'Write down i the birth rate for age group 2 &nbsp; ii the survival rate for age group 3', 'i 1.8 &nbsp; ii 0.3', 12),
           ('b', 'Complete a life cycle diagram for this Leslie matrix.', LC([0, 1.8, 2.6, 0.1], [0.2, 0.4, 0.3]), 30),
           ('c', 'Evaluate the following population state matrices. ' + S_(1) + ', ' + S_(5) + ' and ' + S_(20), S_(1) + ' = (0, 200, 0, 0), ' + S_(5) + ' = (149.76, 26.4, 16.64, 8.64), ' + S_(20) + ' = (3.84, 0.97, 0.49, 0.19)', 16),
           ('d', 'Given that ' + S_(16) + ' = ' + V(['9.53', '2.42', '1.22', '0.16']) + ', determine ' + S_(17), S_(17) + ' = <i>L</i>' + S_(16) + ' = (7.54, 1.91, 0.97, 0.37)', 14)]))
YT = (q('Scientists have collected the yearly fertility and survival rates for siamese fighting fish. A small sample of the species is under observation. The following Leslie matrix for the survival rate of siamese fighting fish can be used to model the growth of the sample population.')
  + row('<i>L</i> = ' + M([['0.05', '0.80', '0.90'], ['0.85', 0, 0], [0, '0.75', 0]], cl=['0', '1', '2']))
  + q('The following initial state matrix represents the female population of the sample being observed at the start of the study.') + row(S_(0) + ' = ' + M([[50], [40], [30]], rl=['0', '1', '2'], side=True))
  + parts([('a', 'Interpret the element in row 2 and column 1 of the Leslie matrix.', '85% of the female population that is less than 1 year old will survive into the next year.', 14),
           ('b', 'Interpret the element in row 1 and column 3 of the Leslie matrix.', 'On average, there will be 0.90 females born to each 2-year-old female.', 14),
           ('c', 'What is the estimated total number of female siamese fighting fish after two years?', S_(2) + ' = (64.075, 52.275, 31.875) ≈ (64, 52, 32): 148 female fish', 16),
           ('d', 'Determine ' + S_(8) + ', the expected female population in the study after 8 years. Round the matrix elements to the nearest whole number.', S_(8) + ' = <i>L</i><sup>8</sup>' + S_(0) + ' ≈ (128, 97, 66)', 14)]))
P.append(exyt('Example 9 · state matrices and life cycle diagrams', EX, 'You try 1', YT))

def ex10(an, hd, rows, Lm, b, s, s3, d):
    return (q(f'Information about a population of female {an} is given in the following table.') + tab(hd, rows)
      + parts([('a', 'Write down the initial population state matrix, ' + S_(0) + '.', S_(0) + ' = ' + V(rows[0][1:]), 20),
               ('b', f'Using the information in the table above, write down a Leslie matrix to describe the change in population of female {an}.', '<i>L</i> = ' + M(Lm), 22),
               ('c', 'Construct a life cycle transition diagram for this Leslie matrix.', LC(b, s), 30),
               ('d', f'Determine the number of 3 − 4 year old female {an} in the population after 3 years. Round your answer to the nearest whole number.', S_(3) + ' = <i>L</i><sup>3</sup>' + S_(0) + ' = ' + s3 + ': ' + d, 16)]))
EX = ex10('goats', ['0 − 1', '1 − 2', '2 − 3', '3 − 4', '4 − 5'], [['Initial population', 10, 25, 40, 20, 15], ['Birth rates', 0, 0.2, 0.9, 0, 0], ['Survival rates', 0.6, 0.7, 0.5, 0.2, 0]],
          [[0, 0.2, 0.9, 0, 0], [0.6, 0, 0, 0, 0], [0, 0.7, 0, 0, 0], [0, 0, 0.5, 0, 0], [0, 0, 0, 0.2, 0]], [0, 0.2, 0.9, 0, 0], [0.6, 0.7, 0.5, 0.2], '(8.7, 10.17, 17.22, 2.1, 1.75)', 'two goats')
YT = ex10('rabbits', ['0 − 1', '1 − 2', '2 − 3', '3 − 4'], [['Initial population', 20, 30, 15, 10], ['Birth rates', 0, 1.2, 0.8, 0], ['Survival rates', 0.5, 0.6, 0.3, 0]],
          [[0, 1.2, 0.8, 0], [0.5, 0, 0, 0], [0, 0.6, 0, 0], [0, 0, 0.3, 0]], [0, 1.2, 0.8, 0], [0.5, 0.6, 0.3], '(33.6, 13.2, 14.4, 1.8)', 'about 2 rabbits')
P.append(exyt('Example 10 · entering a Leslie matrix', EX, 'You try 2', YT))

def ex11(Lm, r, a, b):
    return (q('Consider the following Leslie matrix <i>L</i> and initial population matrix ' + S_(0) + ':') + row('<i>L</i> = ' + M(Lm), S_(0) + ' = ' + V([1000, 0, 0]))
      + parts([('a', 'Find i ' + S_(5) + ' ii ' + S_(10) + ' iii ' + S_(50) + '<br>Premultiply each of these state matrices by [1 1 1] to calculate the total populations at each of these stages and comment.', a, 26),
               ('b', 'Determine ' + S_(25) + ' and ' + S_(26) + '. Divide each age group population for ' + S_(26) + ' by the corresponding age group population for ' + S_(25) + f' and show that {S_(26)} ≈ {r}{S_(25)} and comment.', b, 22)]))
EX = ex11([[0, 4, 4], [0.25, 0, 0], [0, 0.5, 0]], '1.1915', S_(5) + ' = (1000, 250, 62.5), total 1312.5; ' + S_(10) + ' = (2500, 531.25, 218.75), total 3250; ' + S_(50) + ' = (2 777 063, 582 688.05, 244 521.18), total ≈ 3 604 272: increases without bound',
          S_(25) + ' = (34 781.25, 7297.85, 3062.50), ' + S_(26) + ' = (41 441.41, 8695.31, 3648.93); each ratio ≈ 1.1915: grows by about 19% each period')
YT = ex11([[0, 3, 3], [0.3, 0, 0], [0, 0.5, 0]], '1.1381', S_(5) + ' = (810, 243, 67.5), total ≈ 1121; ' + S_(10) + ' ≈ (1575, 421, 180), total ≈ 2176; ' + S_(50) + ' ≈ (280 035, 73 813, 32 427), total ≈ 386 275: keeps increasing',
          S_(25) + ' ≈ (11 022, 2905, 1276), ' + S_(26) + ' ≈ (12 544, 3307, 1453); each ratio ≈ 1.1381: grows by about 13.8% each year')
P.append(exyt('Example 11 · limiting behaviour', EX, 'You try 3', YT))

def ex12(Lm, s0, r, a, b, c):
    return (q('Consider the following Leslie matrix <i>L</i> and initial population matrix ' + S_(0) + ':') + row('<i>L</i> = ' + M(Lm), S_(0) + ' = ' + V(s0))
      + parts([('a', 'Determine i ' + S_(10) + ' ii ' + S_(14) + ' iii ' + S_(15), a, 18),
               ('b', 'The rate of increase of the population is a constant and each of the age group populations increase in the same way. Find this rate by comparing ' + S_(14) + ' and ' + S_(15) + '.', b, 16),
               ('c', 'Confirm the ratio of the age group populations stays constant for ' + S_(0) + ', ' + S_(1) + ' and ' + S_(10) + f' at {r}', c, 14)]))
EX = ex12([[0, 2.3, 0.4], [0.6, 0, 0], [0, 0.3, 0]], [1600, 800, 200], '8 : 4 : 1', S_(10) + ' = (9906.78, 4953.39, 1238.35), ' + S_(14) + ' = (20 542.70, 10 271.35, 2567.84), ' + S_(15) + ' = (24 651.24, 12 325.62, 3081.4043)',
          '24 651.24 ÷ 20 542.70 ≈ 1.2 (same for each group): growth rate 1.2', '8 : 4 : 1 = 1600 : 800 : 200 ≈ 9906.78 : 4953.39 : 1238.35')
YT = ex12([[0, 2, 1], [0.6, 0, 0], [0, 0.48, 0]], [1000, 500, 200], '10 : 5 : 2', S_(10) + ' ≈ (6192, 3096, 1238), ' + S_(14) + ' ≈ (12 839, 6420, 2568), ' + S_(15) + ' ≈ (15 407, 7704, 3081)',
          '15 407 ÷ 12 839 ≈ 1.2 (same for each group): a 20% increase each period', '1000 : 500 : 200 = 1200 : 600 : 240 ≈ 6192 : 3096 : 1238 = 10 : 5 : 2')
P.append(exyt('Example 12 · constant rate of increase', EX, 'You try 4', YT))

def ex13(s, s0, bs, ans):
    return (q('Consider the following Leslie matrix <i>L</i> and initial population matrix ' + S_(0) + ':') + row('<i>L</i> = ' + M([[0, 0, '<i>b</i><sub>3</sub>'], [s, 0, 0], [0, 0.5, 0]]), S_(0) + ' = ' + V([s0, 0, 0]))
      + q('Investigate the long-term behaviour of the population if:') + parts([(l, '<i>b</i><sub>3</sub> = ' + str(b), a, 16) for l, b, a in zip('abc', bs, ans)]))
EX = ex13(0.25, 1000, [8, 4, 10], [S_(1) + ' = (0, 250, 0), ' + S_(2) + ' = (0, 0, 125), ' + S_(3) + ' = (1000, 0, 0): cycles through these three states',
                                   S_(5) + ' = (0, 0, 62.5), ' + S_(50) + ' = (0, 0, 0.0019): decreases', S_(5) + ' = (0, 0, 156.25), ' + S_(50) + ' = (0, 0, 4440.89): increases'])
YT = ex13(0.4, 500, [5, 3, 8], [S_(3) + ' = ' + S_(6) + ' = (500, 0, 0): periodic, repeats every 3 years', S_(3) + ' = (300, 0, 0), ' + S_(6) + ' = (180, 0, 0): decreasing (× 0.6 every 3 years)',
                                S_(3) + ' = (800, 0, 0), ' + S_(6) + ' = (1280, 0, 0): increasing (× 1.6 every 3 years)'])
P.append(exyt('Example 13 · periodic, increasing, decreasing', EX, 'You try 5', YT))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('11E', 'Q1–13')], ['11E']))
build('gm12-u4-11e', '11E', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-11e-worksheet', '11E worksheet'), ('gm12-u4-11e-worksheet-solutions', '11E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
