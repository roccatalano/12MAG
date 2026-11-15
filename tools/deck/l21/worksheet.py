"""Lesson l21 (5D, calculating seasonal indices and deseasonalising) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as tools/deck/l21/build.py (Do Now is not on the worksheet, as in l16-l20).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 1 skills checklist 1B #7 (replaces the card's 1B #6, burnt in l20), 1F #14.
Example 17 / You try 1 = Cambridge U3&4 Example 17 (p. 287) / Edrolo U3&4 4D WE1a (p. 268).
Example 18 / You try 2 = Cambridge Example 18 (pp. 288-289) / Edrolo 4D WE2 (pp. 269-270).
Example 19 / You try 3 = Cambridge Example 19 (p. 290) / Edrolo 4D WE3 (p. 270).
Exit = Edrolo U3&4 4D Q18 (VCAA 2019 Exam 2 Q6a, b; original wording).
Output: lessons/5D deseasonalising worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/l21/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
SEAS = ['<b>Summer</b>', '<b>Autumn</b>', '<b>Winter</b>', '<b>Spring</b>']
seas = ['<b>summer</b>', '<b>autumn</b>', '<b>winter</b>', '<b>spring</b>']
A = lambda v: ans(v)

P = [title('5D', 'Calculating seasonal indices and deseasonalising')]
P.append(lis(['To be able to calculate seasonal indices from time series data.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('A kg of bananas rose in value from $4.50 to $7.00. What was the % increase?') + space(12, '2.50 ÷ 4.50 × 100% = 55.6% increase'), ''))
P.append(box('Question 2', q('If 50 items cost $2500, how much do 10 items cost?') + space(12, '2500 ÷ 50 = $50 each → 10 × 50 = $500'), ''))
P.append(sect('5D Seasonal indices', 'Example, then you try'))
P.append(exyt('Example 17 · Calculating seasonal indices (1 year’s data)',
  q('Mikki runs a shop and she wishes to determine quarterly seasonal indices for the number of customers to her shop based on last year’s figures which are shown in the table opposite.')
  + T([SEAS, MIK[0]]) + q('Quarterly average = ' + A('(920 + 1085 + 1241 + 446) ÷ 4 = 923')) + space(8, 'SI = value ÷ 923; check: sum = 4.001 ≈ 4')
  + q('Seasonal indices') + T([SEAS, [A(v) for v in ('0.997', '1.176', '1.345', '0.483')]]),
  'You try 1', q('Consider the following table.') + T([[''] + seas, ['<b>umbrella sales</b>', 205, 377, 528, 442]])
  + parts([('a', 'Use the table to calculate the seasonal index for umbrella sales in summer, correct to two decimal places.',
            'mean = (205 + 377 + 528 + 442) ÷ 4 = 388; 205 ÷ 388 = 0.5283… → 0.53', 30)])))
P.append(exyt('Example 18 · Calculating seasonal indices (several years’ data)',
  q('Suppose that Mikki has 3 years of data, as shown. Use the data to calculate seasonal indices, rounded to two decimal places.')
  + T([['<b>Year</b>'] + SEAS] + [[y + 1] + MIK[y] for y in range(3)])
  + q('Seasonal indices for each year') + T([['<b>Year</b>'] + SEAS, [1] + [A(v) for v in ('0.997', '1.176', '1.345', '0.483')],
        [2] + [A(v) for v in ('1.007', '1.148', '1.319', '0.526')], [3] + [A(v) for v in ('1.098', '1.119', '1.226', '0.557')]])
  + space(6, 'averages: year 2 = 1028, year 3 = 1183')
  + q('Final seasonal indices (average of the three years)') + T([SEAS, [A(v) for v in ('1.03', '1.15', '1.30', '0.52')]]),
  'You try 2', q('For the following table, calculate the seasonal indices for summer, autumn, winter, and spring, correct to two decimal places.')
  + T([['<b>year</b>'] + seas] + [[2019 + y] + E2[y] for y in range(3)])
  + space(52, 'means 37, 42, 49 → yearly SIs, then average:<br>summer 1.19, autumn 0.78, winter 0.60, spring 1.43')))
P.append(exyt('Example 19 · Deseasonalising a time series',
  q('The quarterly sales figures for Mikki’s shop over a 3-year period are given below.')
  + T([['<b>Year</b>'] + SEAS] + [[y + 1] + MIK[y] for y in range(3)])
  + q('Use the seasonal indices shown to deseasonalise these sales figures. Write answers rounded to the nearest whole number.')
  + T([SEAS, MSI]) + q('Deseasonalised sales figures')
  + T([['<b>Year</b>'] + SEAS] + [[y + 1] + [A(v) for v in MDES[y]] for y in range(3)]),
  'You try 3', q('Use the given seasonal indices to deseasonalise the following time series data. Give values correct to the nearest whole number.')
  + T([[''] + [f'<b>{d}</b>' for d in DAYS[:4]], ['<b>seasonal index</b>'] + E3SI[:4], ['<b>number of steps</b>'] + E3N[:4], ['<b>deseasonalised number of steps</b>'] + [A(v) for v in E3D[:4]]])
  + T([[''] + [f'<b>{d}</b>' for d in DAYS[4:]], ['<b>seasonal index</b>'] + E3SI[4:], ['<b>number of steps</b>'] + E3N[4:], ['<b>deseasonalised number of steps</b>'] + [A(v) for v in E3D[4:]]])
  + space(14, 'e.g. Mon: 7500 ÷ 0.70 ≈ 10 714')))
P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 2 Q6a, b', q('The total rainfall, in millimetres, for each of the four seasons in 2015 and 2016 is shown in Table 5 below.<br><b>Table 5</b>')
  + T([['<b>Year</b>'] + SEAS, [2015, 142, 156, 222, 120], [2016, 135, 153, 216, 96]])
  + parts([('a', 'The seasonal index for winter is shown in Table 6 below.<br>Use the values in Table 5 to find the seasonal indices for summer, autumn and spring.<br>Write your answers in Table 6, rounded to two decimal places.<br><b>Table 6</b>'
            + T([[''] + SEAS, ['<b>Seasonal index</b>', A('0.89'), A('1.00'), '1.41', A('0.70')]]), '2015 average 160, 2016 average 150; e.g. summer (0.8875 + 0.9) ÷ 2 = 0.89', 22),
           ('b', 'The total rainfall for each of the four seasons in 2017 is shown in Table 7 below.<br><b>Table 7</b>' + T([['<b>Year</b>'] + SEAS, [2017, 141, 156, 262, 120]])
            + 'Use the appropriate seasonal index from Table 6 to deseasonalise the total rainfall for winter in 2017.<br>Round your answer to the nearest whole number.', '262 ÷ 1.41 = 185.8 → 186 mm', 14)]), '3 marks'))
SC = ['I can calculate seasonal indices from 1 year of data.', 'I can calculate seasonal indices from several years of data.', 'I can use seasonal indices to deseasonalise a time series.']
P.append(close(SC, [('5D', 'Q6–12, Q16–17')], ['5D']))
build('l21', '5D', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l21-worksheet', '5D deseasonalising worksheet'), ('l21-worksheet-solutions', '5D deseasonalising worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
