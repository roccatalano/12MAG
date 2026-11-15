"""Lesson gm12-u3-l31 (7A, sequences and recurrence relations) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as tools/deck/gm12-u3-l31/build.py (Do Now is not on the worksheet, as in l16-l22; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 3 skills checklist 3A #2, VCAA 2015 Exam 1 Number patterns Q1 (Edrolo U1&2 3A Q12).
Example 1 / You try 1 = Cambridge U3&4 Example 1 (p. 334) / written for 12MAG YT-7A-1.
Example 2 / You try 2 = Cambridge Example 2 (p. 335) / written for 12MAG YT-7A-2.
Example 3 / You try 3 = Cambridge Example 3 (pp. 335-336) / Edrolo U3&4 5A WE5 (pp. 299-300).
Example 4 / You try 4 = Cambridge Example 4 (p. 337) / Edrolo 5A WE4a (p. 299).
Example 5 / You try 5 = Cambridge Example 5 (p. 337) / Edrolo 5A WE4b (p. 299).
Example 6 / You try 6 = Cambridge Example 6 (p. 338) / Edrolo U1&2 3B WE1 (p. 133).
Exits = VCAA 2017 Exam 1 Q18 (Edrolo 5A Q17), VCAA 2021 Exam 1 Q17 (5A Q19), VCAA 2019 Exam 1 Q17 (5A Q20; original wording).
Output: lessons/7A worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u3-l31/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
RR = lambda v0, rule, L='V': f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
def T(vals, names):
    return table([[str(v) for v in vals], [f'<b>{n}</b>' for n in names]], head=False, cls='t tiny')

P = [title('7A', 'Sequences and recurrence relations')]
P.append(lis(['To be able to generate a sequence of terms recursively.', 'To be able to generate a sequence of numbers from a worded description using a calculator.',
              'To be able to generate a sequence from a recurrence relation.', 'To be able to generate a sequence of numbers from a recurrence relation using a calculator.',
              'To be able to number and name terms in a sequence.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Look for a pattern or rule in the following sequence, and hence find the next number:<br>3, 7, 11, 15, 19, ...') + space(14, 'Rule: add 4 to each term. Next number = 19 + 4 = 23'), ''))
P.append(box('Question 2 · VCAA 2015 Exam 1 Q1', q('The first four terms in a geometric sequence are: 5, 10, 20, 40, ...<br>The fifth term in this sequence is')
  + mc(['45', '50', '60', '80', '100'], 'D', cols=5) + why('rule: multiply by 2; 40 × 2 = 80'), ''))
P.append(sect('7A Sequences and recurrence relations', 'Example, then you try'))
P.append(exyt('Example 1 · Generating a sequence of terms recursively (1)',
  q('Write down the first five terms of the sequence with a starting value of 6 and the rule ‘add 4 to the previous term’.')
  + q('Start: ' + A('6')) + q('Next terms: ' + A('6 + 4 = 10, 14, 18, 22')) + q('The first five terms are ' + A('6, 10, 14, 18, 22')),
  'You try 1', q('Write down the first five terms of the sequence with a starting value of 9 and the rule ‘add 7 to the previous term’.') + space(26, '9, 16, 23, 30, 37')))
P.append(exyt('Example 2 · Generating a sequence of terms recursively (2)',
  q('Write down the first five terms of the sequence with a starting value of 5 and the rule ‘double the number and then subtract 3’.')
  + q('Start: ' + A('5')) + q('Next term: 5 × 2 − 3 = ' + A('7')) + q('Three more: ' + A('11, 19, 35')) + q('The first five terms are ' + A('5, 7, 11, 19, 35')),
  'You try 2', q('Write down the first five terms of the sequence with a starting value of 4 and the rule ‘triple the number and then subtract 5’.') + space(30, '4 × 3 − 5 = 7, 7 × 3 − 5 = 16, 43, 124<br>4, 7, 16, 43, 124')))
P.append(exyt('Example 3 · Generating a sequence of numbers with a calculator',
  q('Use a calculator to generate the first five terms of the sequence with a starting value of 5 and the rule ‘double and then subtract 3’.')
  + q('Type the starting value: ' + A('5') + ', then the rule: ' + A('× 2 − 3')) + q('The first five terms are ' + A('5, 7, 11, 19, 35')),
  'You try 3', q('Use a calculator to find the first five terms of the sequence given by the following geometric recurrence relation, correct to two decimal places.<br>'
  + RR('2.12', '−3.76 × <i>B<sub>n</sub></i>', 'B')) + space(26, '2.12, −7.97, 29.97, −112.69, 423.73')))
P.append(exyt('Example 4 · Generating a sequence from a recurrence relation',
  q('Write down the first five terms of the sequence defined by the recurrence relation<br>' + RR('29', '<i>V<sub>n</sub></i> − 4'))
  + q('<i>V</i><sub>0</sub> = ' + A('29')) + q('<i>V</i><sub>1</sub> = <i>V</i><sub>0</sub> − 4 = ' + A('29 − 4 = 25'))
  + q('<i>V</i><sub>2</sub> = ' + A('21') + ' &nbsp; <i>V</i><sub>3</sub> = ' + A('17') + ' &nbsp; <i>V</i><sub>4</sub> = ' + A('13')) + q('The first five terms are ' + A('29, 25, 21, 17, 13')),
  'You try 4', q('Find the first five terms of the sequence given by the following recurrence relations.') + parts([('a', RR('42', '<i>H<sub>n</sub></i> − 3.5', 'H'), '42, 38.5, 35, 31.5, 28', 26)])))
P.append(exyt('Example 5 · Using a calculator to generate sequences from recurrence relations',
  q('A sequence is generated by the recurrence relation<br>' + RR('300', '0.5<i>V<sub>n</sub></i> − 9') + '<br>Use your calculator to generate this sequence and determine how many terms at the start of the sequence are positive.')
  + q('Terms: ' + A('300, 141, 61.5, 21.75, 1.875, −8.625')) + q('Number of positive terms at the start: ' + A('5')),
  'You try 5', q('Find the first five terms of the sequence given by the following recurrence relations.') + parts([('b', RR('2', '4<i>Y<sub>n</sub></i> − 3', 'Y'), '2, 5, 17, 65, 257', 26)])))
P.append(exyt('Example 6 · Naming terms in a sequence',
  q('Consider the recurrence relation<br>' + RR('3', '<i>V<sub>n</sub></i> + 6') + '<br>State the values of:')
  + T([A('3'), A('9'), A('15'), A('21'), A('27'), A('33')], ['V₀', 'V₁', 'V₂', 'V₃', 'V₄', 'V₅'])
  + q('a &nbsp;<i>V</i><sub>1</sub> = ' + A('9') + ' &nbsp;&nbsp; b &nbsp;<i>V</i><sub>4</sub> = ' + A('27') + ' &nbsp;&nbsp; c &nbsp;<i>V</i><sub>5</sub> = ' + A('33')),
  'You try 6', q('Consider the following recurrence relation.<br>' + RR('3', '<i>u<sub>n</sub></i> + 6', 'u') + '<br>Calculate the value of <i>u</i><sub>3</sub>.')
  + space(26, 'u₁ = 3 + 6 = 9, u₂ = 9 + 6 = 15, u₃ = 15 + 6 = 21')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q18', q('The first five terms of a sequence are 2, 6, 22, 86, 342 …<br>The recurrence relation that generates this sequence could be')
  + mc([RR('2', '<i>P<sub>n</sub></i> + 4', 'P'), RR('2', '2<i>P<sub>n</sub></i> + 2', 'P'), RR('2', '3<i>P<sub>n</sub></i>', 'P'), RR('2', '4<i>P<sub>n</sub></i> − 2', 'P'), RR('2', '5<i>P<sub>n</sub></i> − 4', 'P')], 'D', cols=3)
  + why('4 × 2 − 2 = 6, 4 × 6 − 2 = 22, 4 × 22 − 2 = 86 ✓'), ''))
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q17', q('The following recurrence relation can generate a sequence of numbers.<br>' + RR('37', '<i>L<sub>n</sub></i> + <i>C</i>', 'L') + '<br>The value of <i>L</i><sub>2</sub> is 25.<br>The value of <i>C</i> is')
  + mc(['–6', '–4', '4', '6', '37'], 'A', cols=5) + why('L₂ = 37 + 2C = 25 → C = −6'), ''))
P.append(box('Exit task 3 · VCAA 2019 Exam 1 Q17', q('Consider the recurrence relation shown below.<br>' + RR('3', '2<i>A<sub>n</sub></i> + 4', 'A') + '<br>The value of <i>A</i><sub>3</sub> in the sequence generated by this recurrence relation is given by')
  + mc(['2 × 3 + 4', '2 × 4 + 4', '2 × 10 + 4', '2 × 24 + 4', '2 × 52 + 4'], 'D', cols=5) + why('A₁ = 10, A₂ = 24, so A₃ = 2 × 24 + 4 (A = 2 × 3 + 4 is only A₁)'), ''))
SC = ['I can generate a sequence of terms recursively.', 'I can generate a sequence of numbers with a calculator.', 'I can generate a sequence from a recurrence relation.',
      'I can use a calculator to generate sequences from recurrence relations.', 'I can name terms in a sequence.']
P.append(close(SC, [('7A', 'Q1–13')], ['7A']))
build('l31', '7A', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l31-worksheet', '7A worksheet'), ('l31-worksheet-solutions', '7A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
