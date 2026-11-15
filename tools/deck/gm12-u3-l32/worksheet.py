"""Lesson gm12-u3-l32 (7B linear growth and decay, 7D geometric growth and decay) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l32/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 1 skills checklist 1A #5, #4; VCAA 2016 Further Exam 2 Q5a (Edrolo U1&2 3D Q14).
Examples 7-12, 19-22 = Cambridge U3&4 pp. 341-346, 359-362. You trys = Edrolo U3&4 5B WE3b, 5E WE1a, 5E WE1b-c, 5B WE1, 5B WE3a, 5B WE2,
Edrolo U1&2 3D WE2, 3E WE1, Edrolo U3&4 5C WE1, 5C WE2a (graphs redrawn with the source's points).
Exits = VCAA 2019 Exam 1 Q19 (Edrolo 5B Q14), VCAA 2020 Exam 2 Q7b (5B Q15), VCAA 2019 Exam 2 Q7a (5C Q13).
Output: lessons/7B-7D worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l32/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
RR = lambda v0, rule, L='V': f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
def gplot(vals, ymax, ystep, draw=True, L='V', mm=52, n=None):
    """graph of terms: grid with n = 0, 1, 2 …; draw=True: dots in black (given), False: dots in red on the solutions copy only"""
    W, Hh, Lf, T, B = 200, 110, 34, 8, 18
    o, y0, k = ws2._grid(W, Hh, Lf, T, B, ymax, ystep, f'{L}ₙ', '')
    n = n or len(vals); slot = (W - 8 - Lf) / n
    o += [f'<text x="{Lf+(i+.5)*slot:.1f}" y="{y0+10}" font-size="8.5" text-anchor="middle">{i}</text>' for i in range(n)]
    c = '#000' if draw else RED
    o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(f'<circle cx="{Lf+(i+.5)*slot:.1f}" cy="{y0-v*k:.1f}" r="2.6" fill="{c}"/>' for i, v in enumerate(vals)) + '</g>')
    return ws2._svg(W, Hh, o, mm)

P = [title('7B, 7D', 'Linear and geometric growth and decay')]
LI = ['To be able to graph the terms of a linear growth/decay sequence.', 'To be able to model simple interest loans and investments using recurrence relations.',
      'To be able to use a recurrence relation to analyse a simple interest investment.', 'To be able to model and analyse flat rate depreciation using a recurrence relation.',
      'To be able to model and analyse unit cost depreciation using a recurrence relation.', 'To be able to graph the terms of a geometric sequence.',
      'To be able to model compound interest with a recurrence relation.', 'To be able to model reducing balance depreciation with recurrence relations.',
      'To be able to use reducing balance depreciation with recurrence relations.']
P.append(lis(LI))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('What is 30% of $50?') + space(10, '0.3 × 50 = $15'), ''))
P.append(box('Question 2', q('What is 85% as a decimal?') + space(10, '85 ÷ 100 = 0.85'), ''))
P.append(box('Question 3 · VCAA 2016 Exam 2 Q5a', q('Ken has opened a savings account to save money to buy a new caravan.<br>The amount of money in the savings account after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation shown below.<br>'
  + RR('15 000', '1.04 × <i>V<sub>n</sub></i>')) + parts([('a', 'How much money did Ken initially deposit into the savings account?', '$15 000 (V₀)', 10)]), ''))

P.append(sect('7B Modelling linear growth and decay', 'Example, then you try'))
P.append(exyt('Example 7 · Graphing the terms of linear growth/decay sequence',
  q('For each of the following recurrence relations, list the first four terms and graph the corresponding points.')
  + parts([('a', RR('2', '<i>V<sub>n</sub></i> + 5') + '<br>Terms: ' + A('2, 7, 12, 17') + gplot([2, 7, 12, 17], 20, 5, False, mm=46), '', 'L'),
           ('b', RR('20', '<i>W<sub>n</sub></i> − 3', 'W') + '<br>Terms: ' + A('20, 17, 14, 11') + gplot([20, 17, 14, 11], 25, 5, False, 'W', mm=46), '', 'L')]),
  'You try 7', q('The value of a brand new laptop, <i>V<sub>n</sub></i> after <i>n</i> years, is depreciated using flat rate depreciation. This is represented by the following recurrence relation.<br>'
  + RR('2100', '<i>V<sub>n</sub></i> − 350')) + parts([('b', 'Graph the value of the laptop over the first five years.', '2100, 1750, 1400, 1050, 700, 350' + gplot([2100, 1750, 1400, 1050, 700, 350], 2100, 350, False, mm=50), 62)])))
P.append(exyt('Example 8 · Modelling simple interest investments with a recurrence relation',
  q('Cheryl invests $5000 in an investment account that pays 4.8% per annum simple interest. Model this simple investment using a recurrence relation of the form: <i>V</i><sub>0</sub> = the principal, <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + <i>D</i>, where <i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub>. Let <i>V<sub>n</sub></i> be the value of the investment after <i>n</i> years.')
  + q('<i>V</i><sub>0</sub> = ' + A('5000')) + q('<i>D</i> = ' + A('4.8/100 × 5000 = 240')) + q('Recurrence relation: ' + A(RR('5000', '<i>V<sub>n</sub></i> + 240'))),
  'You try 8', q('Sally borrows $300 000 where simple interest is charged at a rate of 0.5% per year.') + parts([('a', 'Construct a recurrence relation to model the value of this loan, <i>V<sub>n</sub></i> after <i>n</i> years.', 'd = 0.5/100 × 300 000 = 1500<br>' + RR('300 000', 'V<sub>n</sub> + 1500'), 24)])))
P.append(exyt('Example 9 · Using a recurrence relation to analyse a simple interest investment',
  q('Cheryl’s simple interest investment is modelled by ' + RR('5000', '<i>V<sub>n</sub></i> + 240') + ' where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.')
  + parts([('a', 'Use the recurrence relation to show that the value of Cheryl’s investment after 3 years is $5720.<br>' + A('V₁ = 5000 + 240 = 5240<br>V₂ = 5240 + 240 = 5480<br>V₃ = 5480 + 240 = 5720'), '', 'L'),
           ('b', 'When will Cheryl’s investment first exceed $6000, and what will its value be then?<br>' + A('5960 → 6200: after 5 years; $6200'), '', 'L')]),
  'You try 9', q('Sally borrows $300 000 where simple interest is charged at a rate of 0.5% per year. (' + RR('300 000', '<i>V<sub>n</sub></i> + 1500') + ')')
  + parts([('b', 'What is the value of the loan after three years?', '301 500, 303 000, 304 500: $304 500.00', 22), ('c', 'How much interest has been charged after three years?', '304 500 − 300 000 = $4500.00', 16)])))
P.append(exyt('Example 10 · Modelling flat rate depreciation with a recurrence relation',
  q('A new car was purchased for $24 000 in 2014. The car depreciates by 20% of its purchase price each year. Model the depreciating value of this car using a recurrence relation of the form: <i>V</i><sub>0</sub> = initial value, <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − <i>D</i>, where <i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub>. Let <i>V<sub>n</sub></i> be the value of the car after <i>n</i> years depreciation.')
  + q('<i>V</i><sub>0</sub> = ' + A('24 000')) + q('<i>D</i> = ' + A('20/100 × 24 000 = 4800')) + q('Recurrence relation: ' + A(RR('24 000', '<i>V<sub>n</sub></i> − 4800'))),
  'You try 10', q('Determine the recurrence relation that models the value of the assets, <i>V<sub>n</sub></i>, after <i>n</i> years, in each of the scenarios.')
  + parts([('a', 'Karl does not believe in banks. Instead of investing his money, he buries his $20 000 in his backyard. Unfortunately for Karl, inflation causes his buried cash to depreciate at a constant amount per year, equal to 3% of the amount of money that he buried.', 'd = 3/100 × 20 000 = 600; V₀ = 20 000, Vₙ₊₁ = Vₙ − 600', 14),
           ('b', 'The graph shows the value of a car, purchased for $24 000, over a period of four years.' + gplot([24000, 22000, 20000, 18000, 16000], 24000, 4000, True, mm=46), 'V₀ = 24 000, Vₙ₊₁ = Vₙ − 2000', 12)])))
P.append(exyt('Example 11 · Using a recurrence relation to analyse flat rate depreciation',
  q('The flat rate depreciation of a car is modelled by ' + RR('24 000', '<i>V<sub>n</sub></i> − 4800') + ' where <i>V<sub>n</sub></i> is the value of the car after <i>n</i> years.')
  + parts([('a', 'Use the model to determine the value of the car after 2 years.<br>' + A('24 000 → 19 200 → 14 400: $14 400'), '', 'L'),
           ('b', 'If the car was purchased in 2023, in what year will the car’s value depreciate to zero?<br>' + A('0 after 5 years: 2028'), '', 'L'),
           ('c', 'What was the percentage depreciation rate?<br>' + A('4800 ÷ 24 000 × 100% = 20%'), '', 'L')]),
  'You try 11', q('The value of a brand new laptop, <i>V<sub>n</sub></i> after <i>n</i> years, is depreciated using flat rate depreciation. This is represented by the following recurrence relation.<br>' + RR('2100', '<i>V<sub>n</sub></i> − 350'))
  + parts([('a', 'What is the value of the laptop two years after it is purchased?', 'V₁ = 2100 − 350 = 1750, V₂ = 1750 − 350 = 1400: $1400', 24)])))
P.append(exyt('Example 12 · Modelling unit cost depreciation with a recurrence relation',
  q('A professional gardener purchased a lawn mower for $270. The mower depreciates in value by $3.50 each time it is used.')
  + parts([('a', 'Model the depreciating value of this mower using a recurrence relation of the form: <i>V</i><sub>0</sub> = initial value, <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − <i>D</i>, where <i>D</i> is the depreciation in value per use and <i>V<sub>n</sub></i> is the value of the mower after being used to mow <i>n</i> lawns.<br>' + A(RR('270', '<i>V<sub>n</sub></i> − 3.50')), '', 'L'),
           ('b', 'Use the model to determine the value of the mower after it has been used three times.<br>' + A('270 → 266.50 → 263 → 259.50: $259.50'), '', 'L'),
           ('c', 'How many times can the mower be used until its depreciated value is first less than $250?<br>' + A('… 256, 252.50, 249: after six mows'), '', 'L')]),
  'You try 12', q('Determine the recurrence relation that models the value of the assets, <i>V<sub>n</sub></i> after <i>n</i> units of use, in each of the following scenarios.')
  + parts([('a', 'David spends $33 on a disposable underwater camera and estimates that it will depreciate by $1.50 for each photo that he takes.', 'V₀ = 33, Vₙ₊₁ = Vₙ − 1.5', 14),
           ('b', 'Chloe purchases a book for $30. The book depreciates each time it is read. The value of the book is shown in the graph.' + gplot([30, 27, 24, 21, 18], 30, 6, True, mm=46), 'V₀ = 30, Vₙ₊₁ = Vₙ − 3', 12)])))

P.append(sect('7D Modelling geometric growth and decay', 'Example, then you try'))
P.append(exyt('Example 19 · Graphing the terms in a geometric sequence',
  q('For each recurrence relation, state the rule, find the first 6 terms and then plot each point on a graph.')
  + parts([('a', RR('1', '3<i>V<sub>n</sub></i>') + '<br>Rule: ' + A('next = 3 × current') + '<br>Terms: ' + A('1, 3, 9, 27, 81, 243') + gplot([1, 3, 9, 27, 81, 243], 250, 50, False, mm=46), '', 'L'),
           ('b', RR('8', '0.5<i>V<sub>n</sub></i>') + '<br>Rule: ' + A('next = 0.5 × current') + '<br>Terms: ' + A('8, 4, 2, 1, 0.5, 0.25') + gplot([8, 4, 2, 1, 0.5, 0.25], 10, 2, False, mm=46), '', 'L')]),
  'You try 19', q('Consider the following recurrence relation.<br>' + RR('45', '0.6<i>u<sub>n</sub></i>', 'u') + '<br>Calculate the value of the first five terms in the sequence.') + space(30, '45, 27, 16.2, 9.72, 5.832')))
P.append(exyt('Example 20 · Modelling compound interest with a recurrence relation',
  q('The following recurrence relation can be used to model a compound interest investment of $2000 paying interest at the rate of 7.5% per annum. ' + RR('2000', '1.075 × <i>V<sub>n</sub></i>') + ' In the recurrence relation, <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.')
  + parts([('a', 'Use the recurrence relation to show that the value of the investment after 3 years is $2484.59.<br>' + A('V₁ = 1.075 × 2000 = 2150<br>V₂ = 1.075 × 2150 = 2311.25<br>V₃ = 1.075 × 2311.25 = 2484.59'), '', 'L'),
           ('b', 'Determine when the value of the investment will first exceed $2500.<br>' + A('2484.59 → 2670.94: after 4 years'), '', 'L')]),
  'You try 20', q('In an environment where locusts were destroying farmers’ crops, a species of frog was introduced to eliminate the pests. Initially, 200 frogs were let out into the crops. Over the next few years, the farmers realised that the frog population was increasing, with 4 times as many frogs each year than in the previous year.')
  + parts([('a', 'Model the scenario using a recurrence relation, where <i>f</i><sub>0</sub> represents the number of frogs let out into the crops initially.', 'f₀ = 200, fₙ₊₁ = 4fₙ', 14),
           ('b', 'How many frogs will there be in 4 years after their introduction, if nothing is done to stop their growth?', '200, 800, 3200, 12 800, 51 200: 51 200 frogs', 16)])))
P.append(exyt('Example 21 · Modelling reducing balance depreciation with recurrence relations',
  q('A sofa was purchased for $7500 and is depreciating at a reducing balance rate of 8.4% per annum. Write down a recurrence relation where <i>V<sub>n</sub></i> is the value of the sofa after <i>n</i> years.')
  + q('<i>V</i><sub>0</sub> = ' + A('7500')) + q('<i>R</i> = ' + A('1 − 8.4/100 = 0.916')) + q('Recurrence relation: ' + A(RR('7500', '0.916 × <i>V<sub>n</sub></i>'))),
  'You try 21', q('Determine the recurrence relation that models the depreciation in each of the following scenarios.')
  + parts([('a', 'A tablet is worth $550 and is depreciated using a reducing balance depreciation method with a rate of 4.3% per annum.', 'R = 1 − 4.3/100 = 0.957; V₀ = 550, Vₙ₊₁ = 0.957 × Vₙ', 14),
           ('b', 'The graph shows the value of a boat, purchased for $60 000, over a period of four years.<br>(0, 60 000) (1, 48 000) (2, 38 400) (3, 30 720) (4, 24 576) (5, 19 661)' + gplot([60000, 48000, 38400, 30720, 24576, 19661], 60000, 10000, True, mm=46), 'R = 48 000 ÷ 60 000 = 0.8; V₀ = 60 000, Vₙ₊₁ = 0.8 × Vₙ', 12)])))
P.append(exyt('Example 22 · Using reducing balance depreciation with recurrence relations',
  q('The following recurrence relation can be used to model the value of office furniture with a purchase price of $9600, depreciating at a reducing-balance rate of 7% per annum. ' + RR('9600', '0.93 × <i>V<sub>n</sub></i>') + ' In the recurrence relation, <i>V<sub>n</sub></i> is the value of the office furniture after <i>n</i> years.')
  + parts([('a', 'Use the recurrence relation to find the value of the office furniture, correct to the nearest cent, after 1, 2 and 3 years.<br>' + A('V₁ = $8928.00, V₂ = $8303.04, V₃ = $7721.83'), '', 'L'),
           ('b', 'If the office furniture was initially purchased in 2023, at the end of which year will the value of the furniture first be less than $7000?<br>' + A('7181.30 → 6678.71 after 5 years: end of 2028'), '', 'L')]),
  'You try 22', q('A tablet is worth $550 and is depreciated using a reducing balance depreciation method with a rate of 4.3% per annum. A recurrence relation is constructed to represent the depreciation of the tablet: ' + RR('550', '0.957 × <i>V<sub>n</sub></i>'))
  + parts([('a', 'After how many years will the value of the tablet drop below $505?', 'V₁ = 526.35, V₂ = 503.72 &lt; 505: 2 years', 26)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 1 Q19', q('Geoff purchased a computer for $4500. He will depreciate the value of his computer by a flat rate of 10% of the purchase price per annum.<br>A recurrence relation that Geoff can use to determine the value of the computer after <i>n</i> years, <i>V<sub>n</sub></i>, is')
  + mc([RR('4500', '<i>V<sub>n</sub></i> – 450'), RR('4500', '<i>V<sub>n</sub></i> + 450'), RR('4500', '0.9 <i>V<sub>n</sub></i>'), RR('4500', '1.1 <i>V<sub>n</sub></i>'), RR('4500', '0.1 (<i>V<sub>n</sub></i> – 450)')], 'A', cols=2)
  + why('flat rate: subtract 10% of 4500 = 450 each year (C is reducing balance)'), ''))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q7b', q('Samuel owns a printing machine.<br>The printing machine is depreciated in value by Samuel using flat rate depreciation.<br>The value of the machine, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation ' + RR('120 000', '<i>V<sub>n</sub></i> – 15 000'))
  + parts([('b', 'Showing recursive calculations, determine the value of the machine, in dollars, after two years.', 'V₁ = 120 000 – 15 000 = 105 000<br>V₂ = 105 000 – 15 000 = 90 000', 18)]), ''))
P.append(box('Exit task 3 · VCAA 2019 Exam 2 Q7a', q('Phil is a builder who has purchased a large set of tools.<br>The value of Phil’s tools is depreciated using the reducing balance method.<br>The value of the tools, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation shown below. ' + RR('60 000', '0.9 <i>V<sub>n</sub></i>'))
  + parts([('a', 'Use recursion to show that the value of the tools after two years, <i>V</i><sub>2</sub>, is $48 600.', 'V₁ = 0.9 × 60 000 = 54 000<br>V₂ = 0.9 × 54 000 = 48 600', 18)]), ''))
SC = ['I can graph the terms of a linear growth/decay sequence.', 'I can model simple interest loans and investments with a recurrence relation.', 'I can use a recurrence relation to analyse a simple interest investment.',
      'I can model flat rate depreciation using a recurrence relation.', 'I can use a recurrence relation to analyse flat rate depreciation.', 'I can model unit cost depreciation with a recurrence relation.',
      'I can graph the terms in a geometric sequence.', 'I can model compound interest with a recurrence relation.', 'I can model reducing balance depreciation with recurrence relations.', 'I can use reducing balance depreciation with recurrence relations.']
P.append(close(SC, [('7B', 'Q1–18'), ('7D', 'Q1–14')], ['7B', '7D']))
build('l32', '7B-7D', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l32-worksheet', '7B-7D worksheet'), ('l32-worksheet-solutions', '7B-7D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
