"""Lesson gm12-u3-l38 (8B reducing balance loans and annuities) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l38/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3B #5; VCAA 2020 Exam 1 Q22 (Edrolo U1&2 3F Q13).
Examples 6-9 = Cambridge U3&4 pp. 400-402. You trys = written YT-8B-6, Edrolo U3&4 6B WE1a, 6B WE1b, 6D WE1.
Exits = VCAA 2017 Exam 1 Q17 (Edrolo 6B Q18), VCAA 2016 Exam 1 Q18 (6D Q17).
Output: lessons/8B worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l38/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
RR = lambda v0, rule, L='V': f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
VN = '<i>V<sub>n</sub></i>'
FORM = ' in the form ' + RR('the principal', '<i>RV<sub>n</sub></i> − <i>D</i>')

P = [title('8B', 'Reducing balance loans and annuities')]
LI = ['To be able to model a reducing balance loan with a recurrence relation.', 'To be able to use a recurrence relation to analyse a reducing balance loan.',
      'To be able to model an annuity with a recurrence relation.', 'To be able to use a recurrence relation to analyse an annuity.']
P.append(lis(LI))
P.append(sect('Activating prior knowledge', 'Year 11 skill and a VCAA question'))
P.append(box('Question 1', q('Write down the first five terms of the sequence defined by the recurrence relation: <i>t</i><sub>0</sub> = 12 and <i>t</i><sub><i>n</i>+1</sub> = <i>t<sub>n</sub></i> + 7, showing the values of the first four iterations.') + space(16, '12, 19, 26, 33, 40'), ''))
P.append(box('Question 2 · VCAA 2020 Exam 1 Q22', q('An asset is purchased for $2480.<br>The value of this asset after <i>n</i> time periods, ' + VN + ', can be determined using the rule <i>V<sub>n</sub></i> = 2480 + 45<i>n</i><br>A recurrence relation that also models the value of this asset after <i>n</i> time periods is')
  + mc([RR('2480', VN + ' + 45<i>n</i>'), VN + ' = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = ' + VN + ' + 45<i>n</i>', RR('2480', VN + ' + 45'), '<i>V</i><sub>1</sub> = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = ' + VN + ' + 45', VN + ' = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = ' + VN + ' + 45'], 'C', cols=1) + why('start at V₀ = 2480 and add 45 each period'), ''))

P.append(sect('8B Reducing balance loans', 'Example, then you try'))
P.append(exyt('Example 6 · Modelling a reducing balance loan with a recurrence relation (1)',
  q('Flora borrows $8000 at an interest rate of 13% per annum, compounding annually. She makes yearly payments of $2100. Construct a recurrence relation to model this loan,' + FORM + ' where ' + VN + ' is the balance of the loan after <i>n</i> years.')
  + q('<i>V</i><sub>0</sub> = ' + A('8000') + ' &nbsp; <i>D</i> = ' + A('2100') + ' &nbsp; <i>R</i> = ' + A('1.13')) + q('Recurrence relation: ' + A('V₀ = 8000, Vₙ₊₁ = 1.13Vₙ − 2100')),
  'You try 1', q('Tom borrows $6000 at an interest rate of 9% per annum, compounding annually. He makes yearly payments of $1800. Construct a recurrence relation to model this loan,' + FORM + ' where ' + VN + ' is the balance of the loan after <i>n</i> years.') + space(24, 'R = 1.09; V₀ = 6000, Vₙ₊₁ = 1.09Vₙ − 1800')))
P.append(exyt('Example 7 · Modelling a reducing balance loan with a recurrence relation (2)',
  q('Alyssa borrows $1000 at an interest rate of 15% per annum, compounding monthly. She makes monthly payments of $250. Construct a recurrence relation to model this loan,' + FORM + ' where ' + VN + ' is the balance of the loan after <i>n</i> months.')
  + q('<i>V</i><sub>0</sub> = ' + A('1000') + ' &nbsp; <i>D</i> = ' + A('250') + ' &nbsp; <i>R</i> = ' + A('1 + 15/1200 = 1.0125')) + q('Recurrence relation: ' + A('V₀ = 1000, Vₙ₊₁ = 1.0125Vₙ − 250')),
  'You try 2', q('Dawn has borrowed $5000 from Barry, who charges interest at a rate of 5% per annum, compounding weekly. Dawn will make weekly $500 repayments.')
  + parts([('a', 'Construct a recurrence relation that can be used to model ' + VN + ', the value of the loan after <i>n</i> weeks. Round <i>R</i> to 5 decimal places.', 'R = 1 + 5/5200 = 1.00096; V₀ = 5000, Vₙ₊₁ = 1.00096 × Vₙ − 500', 22)])))
P.append(exyt('Example 8 · Using a recurrence relation to analyse a reducing balance loan',
  q('Alyssa’s loan can be modelled by the recurrence relation: ' + RR('1000', '1.0125' + VN + ' − 257.85'))
  + parts([('a', 'Use your calculator to find the balance of the loan after four payments.<br>' + A('754.65, 506.23, 254.71, 0.04: $0.04'), '', 'L'),
           ('b', 'Find the balance of the loan after two payments have been made. Round your answer to the nearest cent. ' + A('$506.23'), '', 'L')]),
  'You try 3', q('(Dawn’s loan in You try 2: ' + RR('5000', '1.00096 × ' + VN + ' − 500') + ')')
  + parts([('b', 'Calculate the amount that Dawn owes Barry after 3 weeks.', 'V₁ = 4504.80, V₂ = 4009.12, V₃ = $3512.97', 34)])))

P.append(sect('8B Annuities', 'Example, then you try'))
P.append(exyt('Example 9 · Modelling an annuity with a recurrence relation',
  q('Reza invests $12 000 in an annuity that earns interest at the rate of 6% per annum, compounding monthly, providing him with a monthly income of $2035.')
  + parts([('a', 'Model this annuity using a recurrence relation of the form ' + RR('the principal', '<i>RV<sub>n</sub></i> − <i>D</i>') + ' where ' + VN + ' is the value of the annuity after <i>n</i> months.<br>' + A('R = 1.005; V₀ = 12 000, Vₙ₊₁ = 1.005Vₙ − 2035'), '', 'L'),
           ('b', 'Use your calculator to find the value of the annuity after the first four months. Round your answer to the nearest cent. ' + A('$4040.55'), '', 'L')]),
  'You try 4', q('Tom invests $25 000 in an annuity with an interest rate of 7% per annum, compounding monthly. This annuity will provide him with a monthly income of $2500.')
  + parts([('a', 'Construct a recurrence relation that can be used to model ' + VN + ', the value of this annuity after <i>n</i> compounding periods. Round <i>R</i> to 5 decimal places.', 'V₀ = 25 000, Vₙ₊₁ = 1.00583 × Vₙ − 2500', 18),
           ('b', 'Calculate the value of the investment after 4 months.', '22 645.75, 20 277.77, 17 895.99, $15 500.33', 18)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q17', q('The value of a reducing balance loan, in dollars, after <i>n</i> months, ' + VN + ', can be modelled by the recurrence relation shown below.<br>' + RR('26 000', '1.003 ' + VN + ' – 400') + '<br>What is the value of this loan after five months?')
  + mc(['$24 380.31', '$24 706.19', '$25 031.10', '$25 355.03', '$25 678.00'], 'A', cols=5) + why('iterate five times: V₅ = 24 380.31'), ''))
P.append(box('Exit task 2 · VCAA 2016 Exam 1 Q18', q('The value of an annuity, ' + VN + ', after <i>n</i> monthly payments of $555 have been made, can be determined using the recurrence relation<br>' + RR('100 000', '1.0025 ' + VN + ' – 555') + '<br>The value of the annuity after five payments have been made is closest to')
  + mc(['$97 225', '$98 158', '$98 467', '$98 775', '$110 224'], 'C', cols=5) + why('iterate five times: V₅ = 98 467.36'), ''))
SC = ['I can model a reducing balance loan with a recurrence relation.', 'I can use a recurrence relation to analyse a reducing balance loan.',
      'I can model an annuity with a recurrence relation.', 'I can use a recurrence relation to analyse an annuity.']
P.append(close(SC, [('8B', 'Q1–18')], ['8B']))
build('l38', '8B', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l38-worksheet', '8B worksheet'), ('l38-worksheet-solutions', '8B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
