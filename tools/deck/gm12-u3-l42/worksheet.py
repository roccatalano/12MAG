"""Lesson gm12-u3-l42 (8F using a finance solver to find interest rates, time taken and regular payments) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l42/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3I #26. Examples 21-24 = Cambridge U3&4 pp. 432-436.
You trys = written for 12MAG (planner/written-youtrys.json YT-8F-21..24).
Exits = VCAA 2018 Exam 2 Q6bi (Edrolo 6D Q18), VCAA 2017 Exam 2 Q7b (Edrolo 6F Q19), VCAA 2021 Exam 2 Q9 (Edrolo 6D Q20).
Output: lessons/8F worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l42/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
def fs(N, I, PV, PMT, FV, P): return f'N = {N}, I = {I}, PV = {PV}, PMT = {PMT}, FV = {FV}, PpY = CpY = {P}'
def solver(v=None):
    v = v or ['', '', '', '', '', '', '']
    return table([['N', 'I(%)', 'PV', 'PMT', 'FV', 'PpY', 'CpY'], [a(x) for x in v]], style='width:100%;font-size:9pt')

P = [title('8F', 'Using a finance solver to find interest rates, time taken and regular payments')]
P.append(lis(['To be able to use the finance solver to find the interest rate or time taken for a compounding interest investment with additional payments.',
              'To be able to use the finance solver to find the regular payment for a reducing balance loan.',
              'To be able to use the finance solver to find the interest rate, time taken or regular payment for an annuity.']))
P.append(sect('Activating prior knowledge', 'Year 11 skill'))
P.append(box('Question 1', q('Rohan invests $100 000 in an account earning compound interest at the rate of 3.5% per annum. Find the amount of interest earned in the fifth year of the investment.')
  + space(16, '<i>V</i><sub>4</sub> = 1.035<sup>4</sup> × 100 000 = 114 752.30; <i>V</i><sub>5</sub> = 118 768.63<br>Interest = 118 768.63 − 114 752.30 = $4016.33'), ''))

P.append(sect('8F Interest rate for an investment', 'Example, then you try'))
P.append(exyt('Example 21 · Finding the interest rate for an investment with additional payments',
  q('Mingjia puts $20 000 into a compound interest investment where interest compounds monthly. She adds $50 per month. She wants her investment to reach $40 000 in 10 years. Find the annual interest rate required for this to occur. Round your answer to two decimal places.')
  + solver(['120', '4.807…', '−20 000', '−50', '40 000', '12', '12']) + space(10, 'Mingjia would require an interest rate of 4.81% per annum.'),
  'You try 1', q('Lena puts $10 000 into a compound interest investment where interest compounds monthly. She adds $100 per month. She wants her investment to reach $30 000 in 10 years. Find the annual interest rate required for this to occur. Round your answer to two decimal places.')
  + space(34, fs(120, '?', '−10 000', '−100', '30 000', 12) + '<br>I = 4.1609… → 4.16% per annum')))

P.append(sect('8F Regular payment and time taken', 'Example, then you try'))
P.append(exyt('Example 22 · Regular monthly payment and time taken for an investment with additions',
  q('Winston puts $20 000 into an investment, paying 5.1% interest per annum, compounding monthly.')
  + parts([('a', 'If Winston wants his investment to be worth at least $40 000 in 5 years, what is the minimum he will need to add each month?', fs(60, 5.1, '−20 000', '?', '40 000', 12) + '<br>PMT = −208.34… → round up: $208.35', 14),
           ('b', 'If Winston invests $1000 each month immediately after interest is calculated, what is the minimum number of months required for his investment to at least triple in value?', 'PMT = −1000, FV = 60 000 → N = 34.32… → 35 months', 14)]),
  'You try 2', q('Omar puts $15 000 into an investment, paying 4.8% interest per annum, compounding monthly.')
  + parts([('a', 'If Omar wants his investment to be worth at least $30 000 in 6 years, what is the minimum he will need to add each month?', fs(72, 4.8, '−15 000', '?', '30 000', 12) + '<br>PMT = −120.18… → round up: $120.19', 14),
           ('b', 'If Omar invests $800 each month immediately after interest is calculated, what is the minimum number of months required for his investment to at least triple in value?', 'PMT = −800, FV = 45 000 → N = 32.72… → 33 months', 14)])))

P.append(sect('8F Payment, total repaid and interest for a loan', 'Example, then you try'))
P.append(exyt('Example 23 · Payment amount, total repayment and total interest for a reducing balance loan',
  q('Sipho borrows $10 000 to be repaid in 59 equal monthly payments followed by a 60th payment of less than one dollar more than the regular payment. Interest is charged at the rate of 8% per annum, compounding monthly.')
  + parts([('a', 'Find the regular monthly payment amount. Round your answer to the nearest cent.', fs(60, 8, '10 000', '?', '0', 12) + '<br>PMT = −202.76…: $202.76', 15),
           ('b', 'Find the final payment. Round your answer to the nearest cent.', 'PMT = −202.76 → FV = −0.29: 202.76 + 0.29 = $203.05', 9),
           ('c', 'Find the total of the repayments on the loan. Round your answer to the nearest cent.', '59 × 202.76 + 203.05 = $12 165.89', 9),
           ('d', 'Find the total amount of interest paid. Round your answer to the nearest cent.', '12 165.89 − 10 000 = $2165.89', 9)]),
  'You try 3', q('Priya borrows $15 000 to be repaid in 47 equal monthly payments followed by a 48th payment of less than one dollar more than the regular payment. Interest is charged at the rate of 7% per annum, compounding monthly.')
  + parts([('a', 'Find the regular monthly payment amount. Round your answer to the nearest cent.', fs(48, 7, '15 000', '?', '0', 12) + '<br>PMT = −359.19…: $359.19', 15),
           ('b', 'Find the final payment. Round your answer to the nearest cent.', 'PMT = −359.19 → FV = −0.20: 359.19 + 0.20 = $359.39', 9),
           ('c', 'Find the total of the repayments on the loan. Round your answer to the nearest cent.', '47 × 359.19 + 359.39 = $17 241.32', 9),
           ('d', 'Find the total amount of interest paid. Round your answer to the nearest cent.', '17 241.32 − 15 000 = $2241.32', 9)])))

P.append(sect('8F Interest rate, time taken and payment for an annuity', 'Example, then you try'))
P.append(exyt('Example 24 · Interest rate, time taken and regular payment for an annuity',
  q('Joe invests $200 000 into an annuity, with interest compounding monthly.')
  + parts([('a', 'What interest rate would allow Joe to withdraw $2500 each month for 10 years? Round your answer to one decimal place.', fs(120, '?', '−200 000', '2500', '0', 12) + '<br>I = 8.689… → 8.7%', 15),
           ('b', 'Assume the interest rate is 5% per annum and that Joe receives a regular monthly payment of $3000. For how many months will Joe receive a regular payment?', 'N = 78.26… → round down: 78 months', 9),
           ('c', 'Assume that the interest rate is 5% per annum and that Joe wishes to be paid monthly payments for 10 years. How much will he regularly receive each month?', 'N = 120 → PMT = $2121.31', 9),
           ('d', 'If Joe receives the regular monthly payment found in part c for 119 months, what will his final payment be? Round your answer to the nearest cent.', 'PMT = 2121.31 → FV = +0.047: 2121.31 + 0.05 = $2121.36', 9)]),
  'You try 4', q('Kate invests $250 000 into an annuity, with interest compounding monthly.')
  + parts([('a', 'What interest rate would allow Kate to withdraw $3000 each month for 10 years? Round your answer to one decimal place.', fs(120, '?', '−250 000', '3000', '0', 12) + '<br>I = 7.748… → 7.7%', 15),
           ('b', 'Assume the interest rate is 4.5% per annum and that Kate receives a regular monthly payment of $3500. For how many months will Kate receive a regular payment?', 'N = 83.30… → 83 months', 9),
           ('c', 'Assume that the interest rate is 4.5% per annum and that Kate wishes to be paid monthly payments for 15 years. How much will she regularly receive each month?', 'N = 180 → PMT = $1912.48', 9),
           ('d', 'If Kate receives the regular monthly payment found in part c for 179 months, what will her final payment be? Round your answer to the nearest cent.', 'PMT = 1912.48 → FV = +0.83: 1912.48 + 0.83 = $1913.31', 9)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q6bi', q('Julie has retired from work and has received a superannuation payment of $492 800.')
  + q('<b>Option 2</b> &nbsp;Julie could invest the $492 800 in an annuity, instead of a perpetuity. The annuity earns interest at the rate of 4.32% per annum, compounding monthly. The balance of Julie’s annuity at the end of the first year of investment would be $480 242.25')
  + q('b. i. What monthly payment, in dollars, would Julie receive? (1 mark)') + space(14, fs(12, 4.32, '−492 800', '?', '480 242.25', 12) + '<br>PMT = $2800'), ''))
P.append(box('Exit task 2 · VCAA 2017 Exam 2 Q7b', q('Alex sold his mechanics’ business for $360 000 and invested this amount in a perpetuity. The perpetuity earns interest at the rate of 5.2% per annum. Interest is calculated and paid monthly.')
  + q('b. Later, Alex converts the perpetuity to an annuity investment. This annuity investment earns interest at the rate of 3.8% per annum, compounding monthly. For the first four years Alex makes a further payment each month of $500 to his investment. This monthly payment is made immediately after the interest is added. After four years of these regular monthly payments, Alex increases the monthly payment. This new monthly payment gives Alex a balance of $500 000 in his annuity after a further two years.')
  + q('What is the value of Alex’s new monthly payment? Round your answer to the nearest cent. (2 marks)')
  + space(20, fs(48, 3.8, '−360 000', '−500', '?', 12) + ' → FV = 444 872.94<br>' + fs(24, 3.8, '−444 872.94', '?', '500 000', 12) + ' → PMT = −805.65: $805.65'), ''))
P.append(box('Exit task 3 · VCAA 2021 Exam 2 Q9', q('Sienna invests $152 431 into an annuity from which she will receive a regular monthly payment of $900 for 25 years. The interest rate for this annuity is 5.1% per annum, compounding monthly.')
  + parts([('a', 'Let <i>V<sub>n</sub></i> be the balance of the annuity after <i>n</i> monthly payments. A recurrence relation written in terms of <i>V</i><sub>0</sub>, <i>V</i><sub><i>n</i>+1</sub> and <i>V<sub>n</sub></i> can model the value of this annuity from month to month. Showing recursive calculations, determine the value of the annuity after two months. Round your answer to the nearest cent. (2 marks)',
            '<i>V</i><sub>1</sub> = 1.00425 × 152 431 − 900 = 152 178.83<br><i>V</i><sub>2</sub> = 1.00425 × 152 178.83 − 900 = $151 925.59', 16),
           ('b', 'After two years, the interest rate for this annuity will fall to 4.6%. To ensure that she will still receive the same number of $900 monthly payments, Sienna will add an extra one-off amount into the annuity at this time. Determine the value of this extra amount that Sienna will add. Round your answer to the nearest cent. (1 mark)',
            'N = 24, I = 5.1 → FV = 146 073.74; N = 276, I = 4.6, PMT = 900, FV = 0 → PV = 153 112.94<br>Extra = 153 112.94 − 146 073.74 = $7039.20', 18)]), ''))
SC = ['I can find the interest rate for an investment with additional payments.',
      'I can find the regular monthly payment and the time taken for an investment with additions to the principal.',
      'I can determine the payment amount, total cost and total amount of interest paid for a reducing balance loan.',
      'I can find the interest rate, time taken and regular payment for an annuity.']
P.append(close(SC, [('8F', 'Q1–15')], ['8F']))
build('l42', '8F', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l42-worksheet', '8F worksheet'), ('l42-worksheet-solutions', '8F worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
