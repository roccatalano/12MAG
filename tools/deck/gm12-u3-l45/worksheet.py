"""Lesson gm12-u3-l45 (8I Perpetuities) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l45/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 1 skills checklist 1A #3. Examples 30-32 = Cambridge U3&4 pp. 452-454.
You trys = Edrolo U3&4 6E WE1a, YT-8I-31, YT-8I-32 (planner/written-youtrys.json).
Exits = VCAA 2016 Exam 1 Q21 (Edrolo U3&4 6E Q16; graphs cropped from Edrolo p. 402), VCAA 2021 Exam 2 Q6 (Edrolo 6E Q17).
Output: lessons/8I worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l45/worksheet.py"""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
G = '<img src="data:image/png;base64,' + base64.b64encode(open(os.path.join(H, 'img', 'q16.png'), 'rb').read()).decode() + '" style="width:100%;display:block;margin:4px 0">'

P = [title('8I', 'Perpetuities')]
P.append(lis(['To be able to calculate the regular payment from a perpetuity.',
              'To be able to calculate the investment required to establish a perpetuity.',
              'To be able to calculate the interest rate of a perpetuity.']))
P.append(sect('Activating prior knowledge', 'Year 11 skill'))
P.append(box('Question 1', q('What is 40% as a fraction?') + space(10, '40% = 40/100 = 2/5'), ''))

P.append(sect('8I Calculating the payment', 'Example, then you try'))
P.append(exyt('Example 30 · Calculating the payment from a perpetuity',
  q('Elizabeth invests her superannuation payout of $500 000 into a perpetuity that will provide a monthly income. If the interest rate for the perpetuity is 6% per annum, what monthly payment will Elizabeth receive?')
  + q('<i>D</i> = <i>r</i> ÷ (100 × <i>p</i>) × <i>V</i><sub>0</sub> = ______ ÷ (100 × ______) × ______')
  + space(10, 'D = 6 ÷ (100 × 12) × 500 000 = 2500<br>Elizabeth will receive $2500 every month.'),
  'You try 1', q('Elise invests $259 920 in a perpetuity. Her bank offers an interest rate of 4.8% per annum, compounding monthly.')
  + q('a. What is the monthly amount she will receive from the bank?')
  + space(30, 'd = 4.8 ÷ (12 × 100) × 259 920 = 1039.68<br>$1039.68 each month')))

P.append(sect('8I Calculating the investment required', 'Example, then you try'))
P.append(exyt('Example 31 · Calculating the investment required to establish a perpetuity',
  q('Calculate how much money will need to be invested in a perpetuity account, earning interest of 4.8% per annum compounding monthly, if $300 will be withdrawn every month.')
  + q('______ = ______ ÷ (100 × ______) × <i>V</i><sub>0</sub>')
  + space(10, '300 = 4.8 ÷ (100 × 12) × V₀ = 0.004 × V₀<br>V₀ = 300 ÷ 0.004 = 75 000: $75 000 must be invested'),
  'You try 2', q('Calculate how much money will need to be invested in a perpetuity account, earning interest of 3.6% per annum compounding monthly, if $450 will be withdrawn every month.')
  + space(30, '450 = 3.6 ÷ (100 × 12) × V₀ = 0.003 × V₀<br>V₀ = 450 ÷ 0.003 = $150 000')))

P.append(sect('8I Calculating the interest rate', 'Example, then you try'))
P.append(exyt('Example 32 · Calculating the interest rate of a perpetuity',
  q('A university mathematics faculty has $30 000 to invest. It intends to award an annual mathematics prize of $1500 with the interest earned from investing this money in a perpetuity. What is the minimum interest rate that will allow this prize to be awarded indefinitely?')
  + q('______ = <i>r</i> ÷ (100 × ______) × ______')
  + space(10, '1500 = r ÷ (100 × 1) × 30 000 = r × 300<br>r = 1500 ÷ 300 = 5: the minimum rate is 5% per annum'),
  'You try 3', q('A sports club has $40 000 to invest. It intends to award an annual prize of $1800 with the interest earned from investing this money in a perpetuity. What is the minimum interest rate that will allow this prize to be awarded indefinitely?')
  + space(30, '1800 = r ÷ 100 × 40 000 = r × 400<br>r = 1800 ÷ 400 = 4.5: 4.5% per annum')))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 1 Q21', q('Juanita invests $80 000 in a perpetuity that will provide $4000 per year to fund a scholarship at a university.')
  + q('The graph that shows the value of this perpetuity over a period of five years is') + G
  + mc(['A', 'B', 'C', 'D', 'E'], 'B', cols=5) + why('A perpetuity pays out only the interest, so its value stays at $80 000.'), ''))
P.append(box('Exit task 2 · VCAA 2021 Exam 2 Q6', q('Sienna invests $420 000 in a perpetuity from which she will receive a regular monthly payment of $1890. The perpetuity earns interest at the rate of 5.4% per annum.')
  + parts([('a', 'Determine the total amount, in dollars, that Sienna will receive after one year of monthly payments. (1 mark)', '12 × 1890 = $22 680', 10),
             ('b', 'Write down the value of the perpetuity after Sienna has received one year of monthly payments. (1 mark)', '$420 000', 10),
             ('c', 'Let <i>S<sub>n</sub></i> be the value of Sienna’s perpetuity after <i>n</i> months. Complete the recurrence relation, in terms of <i>S</i><sub>0</sub>, <i>S</i><sub><i>n</i> + 1</sub> and <i>S<sub>n</sub></i>, that would model the value of this perpetuity over time. (1 mark)<br><i>S</i><sub>0</sub> = ____________ , &nbsp; <i>S</i><sub><i>n</i> + 1</sub> = ____________ × <i>S<sub>n</sub></i> – 1890', 'S₀ = 420 000, Sₙ₊₁ = 1.0045 × Sₙ − 1890', 8)]), ''))
SC = ['I can calculate the payment from a perpetuity.',
      'I can calculate the investment required to establish a perpetuity.',
      'I can calculate the interest rate of a perpetuity.']
P.append(close(SC, [('8I', 'Q1–13')], ['8I']))
build('l45', '8I', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l45-worksheet', '8I worksheet'), ('l45-worksheet-solutions', '8I worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
