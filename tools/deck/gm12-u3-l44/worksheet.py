"""Lesson gm12-u3-l44 (8H Interest-only loans) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l44/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = VCAA 2020 Exam 2 Q7a (Edrolo U1&2 3B Q15 adapts Q7a+b; Q7b burnt). Examples 27-29 = Cambridge U3&4 pp. 448-449.
You trys = Edrolo U3&4 6C WE1a, YT-8H-28, YT-8H-29 (planner/written-youtrys.json). Exit = VCAA 2021 Exam 1 Q24 (Edrolo U3&4 6C Q13).
Output: lessons/8H worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l44/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
def fs(N, I, PV, PMT, FV, P): return f'N = {N}, I = {I}, PV = {PV}, PMT = {PMT}, FV = {FV}, PpY = CpY = {P}'

P = [title('8H', 'Interest-only loans')]
P.append(lis(['To be able to find the regular payment amount for an interest-only loan with and without a financial solver.',
              'To be able to find the amount borrowed for an interest-only loan.',
              'To be able to find the interest rate for an interest-only loan.']))
P.append(sect('Activating prior knowledge', 'Year 11 exam question'))
P.append(box('Question 1 · VCAA 2020 Exam 2 Q7a', q('Samuel owns a printing machine. The printing machine is depreciated in value by Samuel using flat rate depreciation. The value of the machine, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation')
  + q('<i>V</i><sub>0</sub> = 120 000, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − 15 000')
  + q('a. By what amount, in dollars, does the value of the machine decrease each year? (1 mark)')
  + space(12, '$15 000 each year'), ''))

P.append(sect('8H Finding the regular payment', 'Example, then you try'))
P.append(exyt('Example 27 · Finding the regular payment for an interest-only loan',
  q('Jane borrows $50 000 to buy some shares. Jane negotiates an interest-only loan at an interest rate of 9% per annum, compounding monthly. What is the monthly amount Jane will be required to pay?')
  + q('<i>D</i> = <i>r</i> ÷ (100 × <i>p</i>) × <i>V</i><sub>0</sub> = ______ ÷ (100 × ______) × ______')
  + space(10, 'D = 9 ÷ (100 × 12) × 50 000 = 375<br>Finance solver: ' + fs(1, 9, '50 000', '?', '−50 000', 12) + ' → −375<br>Jane will need to repay $375 every month.'),
  'You try 1', q('Brock borrows $8000 in an interest-only loan at 3% per annum, compounding monthly.')
  + q('a. What is the monthly amount that he will be required to pay?')
  + space(30, 'd = 3 ÷ (12 × 100) × 8000 = 20<br>$20 each month')))

P.append(sect('8H Finding the amount borrowed', 'Example, then you try'))
P.append(exyt('Example 28 · Finding the amount borrowed for an interest-only loan',
  q('A loan at 6% per annum, compounding monthly, requires payments of $440 each month. If the loan is an interest-only loan, what is the principal?')
  + q('______ = ______ ÷ (100 × ______) × <i>V</i><sub>0</sub>')
  + space(10, '440 = 6 ÷ (100 × 12) × V₀ = 0.005 × V₀<br>V₀ = 440 ÷ 0.005 = 88 000: the principal is $88 000'),
  'You try 2', q('A loan at 4.8% per annum, compounding monthly, requires payments of $600 each month. If the loan is an interest-only loan, what is the principal?')
  + space(30, '600 = 4.8 ÷ (100 × 12) × V₀ = 0.004 × V₀<br>V₀ = 600 ÷ 0.004 = $150 000')))

P.append(sect('8H Finding the interest rate', 'Example, then you try'))
P.append(exyt('Example 29 · Finding the interest rate for an interest-only loan',
  q('An interest-only loan of $1 000 000 requires quarterly payments of $4000. What is the annual interest rate on the loan?')
  + q('______ = <i>r</i> ÷ (100 × ______) × ______')
  + space(10, '4000 = r ÷ (100 × 4) × 1 000 000<br>r = 4000 × 400 ÷ 1 000 000 = 1.6: the annual interest rate is 1.6%'),
  'You try 3', q('An interest-only loan of $500 000 requires quarterly payments of $6250. What is the annual interest rate on the loan?')
  + space(30, '6250 = r ÷ (100 × 4) × 500 000<br>r = 6250 × 400 ÷ 500 000 = 5: 5% per annum')))

P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2021 Exam 1 Q24', q('Bob borrowed $400 000 to buy an apartment. The interest rate for this loan was 3.14% per annum, compounding monthly. A scheduled monthly repayment that allowed Bob to fully repay the loan in 20 years was determined. Bob decided, however, to make interest-only repayments for the first two years.')
  + q('After these two years the interest rate changed. Bob was still able to pay off the loan in the 20 years by repaying the scheduled amount each month.')
  + q('The interest rate, per annum, for the final 18 years of the loan was closest to')
  + mc(['1.85%', '2.21%', '2.79%', '3.14%', '4.07%'], 'B') + why('Interest-only keeps $400 000 owing for 2 years; the scheduled payment then repays it over 216 months at 2.21%.')
  + space(16, fs(240, 3.14, '400 000', '?', 0, 12) + ' → −2246.528…<br>' + fs(216, '?', '400 000', '−2246.528…', 0, 12) + ' → I = 2.2116…'), ''))
SC = ['I can find the repayment amount for an interest-only loan with and without finance solver.',
      'I can find the amount borrowed for an interest-only loan.',
      'I can find the interest rate for an interest-only loan.']
P.append(close(SC, [('8H', 'Q1–17')], ['8H']))
build('l44', '8H', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l44-worksheet', '8H worksheet'), ('l44-worksheet-solutions', '8H worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
