"""Lesson gm12-u3-l41 (8E using a finance solver to find the balance and final payment) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l41/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3I #25; Edrolo U1&2 3B Q16 (adapted by Edrolo from VCAA 2020 Exam 1 Q21).
Examples 18-20 = Cambridge U3&4 pp. 425-429. You trys = Edrolo U3&4 6F WE3a, 6B WE3a, 6D WE3a.
Exits = VCAA 2021 Exam 1 Q19 (Edrolo 6D Q19), VCAA 2021 Exam 2 Q8b (Edrolo 6B Q21).
Output: lessons/8E worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l41/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
HL = ['Payment number', 'Payment', 'Interest', 'Principal reduction', 'Balance of investment']
def T(rows, head=HL): return table([head] + rows, style='width:100%;font-size:8.5pt')
def fs(N, I, PV, PMT, FV, P): return f'N = {N}, I = {I}, PV = {PV}, PMT = {PMT}, FV = {FV}, PpY = CpY = {P}'
def solver(v=None):
    """Example scaffold: blank finance solver table (filled in red on the solutions copy)."""
    v = v or ['', '', '', '', '', '', '']
    return table([['N', 'I(%)', 'PV', 'PMT', 'FV', 'PpY', 'CpY'], [a(x) for x in v]], style='width:100%;font-size:9pt')

P = [title('8E', 'Using a finance solver to find the balance and final payment')]
P.append(lis(['To be able to use the finance solver to find the value of a compounding interest investment with additional payments.',
              'To be able to use the finance solver to find the balance and final payment of a reducing balance loan.',
              'To be able to use the finance solver to find the balance of an annuity.']))
P.append(sect('Activating prior knowledge', 'Year 11 skill and a VCAA question'))
P.append(box('Question 1', q('Adrian invests $250 000 in an account earning compound interest at the rate of 6% per annum. Use a rule to find the value of the investment after 15 years.')
  + space(14, '<i>V</i><sub>15</sub> = 1.06<sup>15</sup> × 250 000 = $599 139.55'), ''))
P.append(box('Question 2 · VCAA 2020 Exam 1 Q21 (adapted)', q('The following recurrence relation can generate a sequence of numbers. &nbsp;<i>S</i><sub>0</sub> = 7, &nbsp;<i>S</i><sub><i>n</i>+1</sub> = <i>S<sub>n</sub></i> + 4')
  + q('The number 11 appears in this sequence as') + mc(['<i>S</i><sub>1</sub>', '<i>S</i><sub>2</sub>', '<i>S</i><sub>3</sub>', '<i>S</i><sub>10</sub>', '<i>S</i><sub>11</sub>'], 'A', cols=5)
  + why('S₁ = 7 + 4 = 11'), ''))

P.append(sect('8E Investment with regular additions', 'Example, then you try'))
P.append(exyt('Example 18 · Value of an investment with regular additions',
  q('Lars invests $500 000 at 5.5% per annum, compounding monthly. He makes a regular deposit of $500 per month into the account. What is the value of his investment after 5 years? Round your answer to the nearest cent.')
  + solver(['60', '5.5', '−500 000', '−500', '692 292.297…', '12', '12']) + space(10, 'After 5 years, Lars’ investment will be worth $692 292.30.'),
  'You try 1', q('Steve is saving up for a cruise holiday by investing $10 000 in an account that earns interest at a rate of 3.90% per annum, compounding monthly. He deposits $500 at the end of each month.')
  + q('a. After 5 years, how much is in Steve’s account?') + space(30, fs(60, 3.90, '−10 000', '−500', '?', 12) + '<br>FV = 45 214.925… → $45 214.93')))

P.append(sect('8E Balance and final payment of a loan', 'Example, then you try'))
P.append(exyt('Example 19 · Balance and final payment of a reducing balance loan',
  q('Andrew borrows $20 000 at an interest rate of 7.25% per annum, compounding monthly. This loan will be repaid over 4 years with regular payments of $481.25 each month for 47 months followed by a final payment to fully repay the loan.')
  + parts([('a', 'How much does Andrew owe after 3 years? Round your answer to the nearest cent.', fs(36, 7.25, '20 000', '−481.25', '?', 12) + '<br>FV = −5554.36 → Andrew owes $5554.36', 14),
           ('b', 'What is the final payment amount that Andrew must make to fully repay the loan within 4 years (48 months)? Round your answer to the nearest cent.', 'N = 48 → FV = +0.11 (overpaid)<br>Final payment = 481.25 − 0.11 = $481.14', 14)]),
  'You try 2', q('Cilian takes out a reducing balance loan of $35 000 with a bank that charges an interest rate of 5.9% per annum, compounding monthly. He makes a payment of $1000 each month to pay off the loan.')
  + q('a. How much does Cilian still owe after 21 months?') + space(30, fs(21, 5.9, '35 000', '−1000', '?', 12) + '<br>FV = −16 731.708… → Cilian owes $16 731.71')))

P.append(sect('8E Balance of an annuity', 'Example, then you try'))
P.append(exyt('Example 20 · Balance and final payment of an annuity',
  q('Charlie invests $300 000 into an annuity, paying 5% interest per annum, compounding monthly. Over the next ten years, Charlie receives a payment of $3182 per month from the annuity for each month except the final month.')
  + parts([('a', 'Find the value of the annuity after five years. Round your answer to the nearest cent.', fs(60, 5, '−300 000', '3182', '?', 12) + '<br>FV = $168 612.25', 14),
           ('b', 'Find the final payment from the annuity. Round your answer to the nearest cent.', 'N = 120 → FV = −5.36<br>Final payment = 3182 − 5.36 = $3176.64', 14)]),
  'You try 3', q('Chuck invests $400 000 in an annuity with a bank who offers an interest rate of 4% per annum, compounding monthly. The annuity pays out $5000 per month.')
  + q('a. What will the annuity be worth after 6 months?') + space(30, fs(6, 4, '−400 000', '5000', '?', 12) + '<br>FV = 377 815.849… → $377 815.85')))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2021 Exam 1 Q19', q('Deepa invests $500 000 in an annuity that provides an annual payment of $44 970.55. Interest is calculated annually. The first five lines of the amortisation table are shown.')
  + T([['0', '0.00', '0.00', '0.00', '500 000.00'], ['1', '44 970.55', '20 000.00', '24 970.55', '475 029.45'], ['2', '44 970.55', '19 001.18', '25 969.37', '449 060.08'], ['3', '44 970.55', '17 962.40', '27 008.15', '422 051.93'], ['4', '44 970.55', '16 882.08', '28 088.47', '393 963.46']])
  + q('The number of years, in total, for which Deepa will receive the regular payment of $44 970.55 is closest to') + mc(['12', '15', '16', '18', '20'], 'B', cols=5)
  + why('I = 20 000/500 000 = 4%; N = ?, PV = −500 000, PMT = 44 970.55, FV = 0, PpY = 1 → N = 15'), ''))
P.append(box('Exit task 2 · VCAA 2021 Exam 2 Q8b', q('For renovations to her coffee shop, Sienne took out a reducing balance loan of $570 000, with interest calculated fortnightly. The balance of the loan, in dollars, after <i>n</i> fortnights, <i>S<sub>n</sub></i>, can be modelled by the recurrence relation &nbsp;<i>S</i><sub>0</sub> = 570 000, &nbsp;<i>S</i><sub><i>n</i>+1</sub> = 1.001 × <i>S<sub>n</sub></i> − 1193')
  + q('Show that the compound interest rate for this loan is 2.6% per annum. (1 mark)') + space(14, '(1.001 − 1) × 26 × 100 = 2.6% per annum'), ''))
SC = ['I can determine the value of an investment with regular additions made to the principal using a financial solver.',
      'I can determine the balance and final payment of a reducing balance loan after a given number of payments.', 'I can determine the balance of an annuity using a finance solver.']
P.append(close(SC, [('8E', 'Q1–12')], ['8E']))
build('l41', '8E', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l41-worksheet', '8E worksheet'), ('l41-worksheet-solutions', '8E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
