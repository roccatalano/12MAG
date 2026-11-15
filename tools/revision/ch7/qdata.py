# Chapter 7 revision booklet: Insight GM1 (MC) + GM2 (SA), Unit 3 Recursion and Financial Modelling, first section
# "Recurrence relations, modelling linear and geometric growth and decay, simple interest and flat rate, unit cost
# depreciation, compound interest investments and loans, reducing balance depreciation"
# (GM1 Q1-14, printed pp.4-6 = pdf 7-9; GM2 Q1-9, printed pp.4-10 = pdf 7-13). Text verbatim from Insight (scanned books;
# read off the page images). Answers from Insight's explanatory notes / worked solutions (GM1 pp.15-17, GM2 pp.19-23).
# Figures are crops of the Insight pages (crop.py). Insight is never burnt.
# Print glitches: GM1 Q4 prints '´' for × (restored as ×, as Insight's own solution reads). GM1 Q10-11 say 'a lounge suite'
# but the purchase price and rate are missing from the question: added from Insight's worked solution (labelled adapted).
# The second section of the Insight books (reducing balance loans, annuities, perpetuities) is Chapter 8: not used here.
# Insight has no effective interest rate question in this section, so 7F has none (listed on the cover).
G1 = 'Insight GM1 U3 Recursion and Financial Modelling'
G2 = 'Insight GM2 U3 Recursion and Financial Modelling'


def P(t): return f'<p class="q">{t}</p>'
def C(t): return f'<p class="q" style="text-align:center">{t}</p>'
def S(t): return f'<sub>{t}</sub>'


def MC(n, sub, page, stem_, opts, a, why, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)


def SA(n, sub, page, stem_, parts, why=None, note=None, long=False):
    return dict(long=long, kind='sa', n=n, sub=sub, marks=sum(p[4] for p in parts), stem=stem_, parts=parts, why=why, note=note, src=f'{G2} p.{page} Q{n}')


LOUNGE = ('<span style="color:#555">[Adapted: Insight’s question does not give the lounge suite’s details; they are taken from Insight’s worked solution.] '
          'A lounge suite is bought for $4500 and depreciates on a reducing balance basis at 9.4% per annum.</span>')

Q = [
 # ---- 7A: sequences and recurrence relations
 MC(3, '7A', 4, P('Consider the following recurrence relation.') + C('<i>A</i>' + S('0') + ' = 3, &nbsp;&nbsp;&nbsp; <i>A</i>' + S('<i>n</i>+1') + ' = −2<i>A</i>' + S('<i>n</i>') + ' + 3')
    + P('The first four terms of this recurrence relation are'),
    ['−3, 9, −15, 33, …', '3, −3, 9, −15, …', '3, −12, 18, −42, …', '−12, 18, −42, 78, …', '3, −3, 21, 45, …'],
    'B', 'A<sub>1</sub> = −2 × 3 + 3 = −3; A<sub>2</sub> = −2 × −3 + 3 = 9; A<sub>3</sub> = −2 × 9 + 3 = −15'),
 MC(6, '7A', 5, P('Consider the following recurrence relation') + C('<i>R</i>' + S('0') + ' = −1, &nbsp;&nbsp;&nbsp; <i>R</i>' + S('<i>n</i>+1') + ' = 0.25<i>R</i>' + S('<i>n</i>') + ' + 2')
    + P('The first five terms of the sequence created by this relation, correct to two decimal places, are'),
    ['1.75, 2.44, 2.61, 2.65, 2.66', '−1, 1.75, 2.43, 2.61, 2.65', '−1, 1.75, 2.44, 2.60, 2.66', '1.75, 2.43, 2.60, 2.65, 2.66', '−1, 1.75, 2.44, 2.61, 2.65'],
    'E', 'R<sub>0</sub> = −1 is the first term. CAS: 1.75, 2.4375, 2.60938, 2.65234 → −1, 1.75, 2.44, 2.61, 2.65 (careful with the rounding).'),
 MC(13, '7A', 6, P('The following recurrence relation generates a sequence of numbers.') + C('<i>T</i>' + S('0') + ' = 6, &nbsp;&nbsp;&nbsp; <i>T</i>' + S('<i>n</i>+1') + ' = 3<i>T</i>' + S('<i>n</i>'))
    + P('<i>T</i>' + S('5') + ' is equal to'),
    ['18', '216', '486', '729', '1458'], 'E', '6 → 18 → 54 → 162 → 486 → 1458 (T<sub>5</sub> is the sixth term).'),
 # ---- 7B: linear growth and decay (simple interest, flat rate and unit cost depreciation)
 MC(2, '7B', 4, P('A printer was purchased for $1200. After three years, the printer has a value of $765.') + P('On average, 1740 pages were printed every year.')
    + P('The value of the printer was depreciated using a unit cost method of depreciation.') + P('The depreciation in the value of the printer, per page printed, is closest to'),
    ['5 cents.', '6 cents.', '7 cents.', '8 cents.', '9 cents.'], 'D', '1200 − 765 = 435 over three years = 145 per year; 145 ÷ 1740 = $0.0833 ≈ 8 cents per page.'),
 MC(8, '7B', 5, P('Five years after a car was purchased, it is worth $26&#8239;000. On average, it travels 22&#8239;000 kilometres per year.')
    + P('If it depreciates on a unit cost basis at 14 cents per kilometre, its purchase price was closest to'),
    ['$10&#8239;600', '$29&#8239;080', '$41&#8239;400', '$56&#8239;000', '$136&#8239;000'], 'C', '22&#8239;000 × 0.14 × 5 = $15&#8239;400 depreciation; 26&#8239;000 + 15&#8239;400 = $41&#8239;400.'),
 MC(12, '7B', 6, P('The graph below shows the value of an asset that was purchased for $6000. Its value decreases on a flat rate basis each year.') + '[[g1q12]]'
    + P('How much had the asset depreciated by after four years?'),
    ['$3800', '$2200', '$1650', '$550', '$412.50'], 'B', 'After three years: 6000 − 4350 = $1650, which is $550 per year. Four years × 550 = $2200.'),
 # ---- 7C: rules for linear growth and decay
 MC(1, '7C', 4, P('A motorbike was purchased for $23&#8239;200.') + P('After three years the motorbike has a value of $16&#8239;990.')
    + P('On average, the motorbike travelled 22&#8239;500 kilometres every year during those three years.')
    + P('The value of the motorbike was depreciated using a unit cost method of depreciation.')
    + P('The value of the motorbike, in dollars, after <i>n</i> kilometres are travelled, <i>V</i>' + S('<i>n</i>') + ', can be modelled by the rule'),
    ['<i>V</i><sub><i>n</i>+1</sub> = <i>V</i><sub><i>n</i></sub> − 0.092<i>n</i>', '<i>V</i><sub><i>n</i>+1</sub> = 23&#8239;200 − 0.092<i>V</i><sub><i>n</i></sub>',
     '<i>V</i><sub><i>n</i></sub> = 23&#8239;200 − 0.092<i>n</i>', '<i>V</i><sub><i>n</i></sub> = 23&#8239;200 − 6200<i>n</i>', '<i>V</i><sub><i>n</i>+1</sub> = 23&#8239;200 − 0.092<i>n</i>'],
    'C', '23&#8239;200 − 16&#8239;990 = 6210; 6210 ÷ (22&#8239;500 × 3) = 0.092 per km. Rule V<sub>n</sub> = V<sub>0</sub> − nD = 23&#8239;200 − 0.092n.'),
 MC(14, '7C', 6, P('An appliance is purchased for $486. It depreciates using the rule shown below, where <i>n</i> represents the number of time periods.')
    + C('<i>V</i>' + S('<i>n</i>') + ' = 486 − 14<i>n</i>') + P('This model of depreciation shown is'),
    ['reducing balance depreciation, at a rate of depreciation of 14% per time period.', 'flat rate depreciation, at a rate of depreciation of $14 per time period.',
     'reducing balance loan, at a rate of depreciation of 14% per time period.', 'reducing balance depreciation, at a rate of depreciation of $14 per time period.',
     'flat rate depreciation, at a rate of depreciation of 14% per time period.'],
    'B', 'V<sub>n</sub> = V<sub>0</sub> − Dn is flat rate, with D the dollar amount ($14). Reducing balance rules have the form V<sub>n</sub> = R<sup>n</sup> × V<sub>0</sub>.'),
 # ---- 7D: geometric growth and decay (compound interest, reducing balance depreciation)
 MC(4, '7D', 4, P('Which of the following recurrence relations represents geometric decay?'),
    ['<i>C</i><sub>0</sub> = 100, &nbsp; <i>C</i><sub><i>n</i>+1</sub> = 0.84 × <i>C</i><sub><i>n</i></sub> + 100', '<i>C</i><sub>0</sub> = 100, &nbsp; <i>C</i><sub><i>n</i>+1</sub> = 1.684 × <i>C</i><sub><i>n</i></sub>',
     '<i>C</i><sub>0</sub> = 100, &nbsp; <i>C</i><sub><i>n</i>+1</sub> = 0.684 × <i>C</i><sub><i>n</i></sub>', '<i>C</i><sub>0</sub> = 100, &nbsp; <i>C</i><sub><i>n</i>+1</sub> = 1.684 × <i>C</i><sub><i>n</i></sub> + 25',
     '<i>C</i><sub>0</sub> = 100, &nbsp; <i>C</i><sub><i>n</i>+1</sub> = <i>C</i><sub><i>n</i></sub> + 345'],
    'C', 'Multiplying by a number less than 1 (and adding nothing) is geometric decay. A mixes geometric decay with arithmetic growth; B is geometric growth; D mixes geometric and arithmetic growth; E is arithmetic growth.'),
 MC(5, '7D', 4, P('Consider the following graph.') + '[[g1q5]]' + P('Which of the following could be modelled by the graph?'),
    ['a reducing balance loan with regular payments', 'a flat rate loan with regular payments', 'a compound interest account', 'an interest only loan', 'a simple interest investment with regular payments'],
    'C', 'The value increases, so it is an investment (not A, B, D). It increases by slightly more each month (not by the same amount, as E would): compounding interest.'),
 MC(7, '7D', 5, P('The graph below shows the value, <i>V</i>' + S('<i>n</i>') + ', of an investment as it increases over eight years.') + '[[g1q7]]'
    + P('Which one of the following investments does this graph best represent?'),
    ['a simple interest investment earning interest at a rate of 10% per annum', 'a compound interest investment earning interest at a rate of 10% per annum, with a yearly payment',
     'a perpetuity earning interest at a rate of 103% per annum.', 'an annuity investment earning interest at a rate of 10% per annum, with a yearly withdrawal.',
     'a compound interest investment earning interest at a rate of 10% per annum, with a yearly withdrawal'],
    'B', 'The balance does not increase by the same amount each year (not A or C). It keeps increasing, so no withdrawals are being taken (not D or E).'),
 MC(11, '7D', 5, P(LOUNGE) + P('When using recursion, which one of the following calculations determines the value of the lounge suite at the end of the third year?'),
    ['0.906 × 4077 = 3693.76', '3690 − 405 = 3285', '1.09 × 4905 = 5346.45', '0.906 × 3693.76 = 3346.55', '1.09 × 5346.45 = 5827.63'],
    'D', 'V<sub>0</sub> = 4500, V<sub>n+1</sub> = 0.906V<sub>n</sub>: 4077, 3693.76, then 0.906 × 3693.76 = 3346.55. A is the end of the second year; B is flat rate; C and E are growth.'),
 # ---- 7E: rules for geometric growth and decay
 MC(9, '7E', 5, P('An asset was purchased for $124&#8239;000. It depreciates on a reducing balance basis at a rate of 5.6% per annum.')
    + P('The value of the asset after 6 years is shown by the rule'),
    ['<i>V</i><sub>6</sub> = 124&#8239;000 × (0.944 × 6)', '<i>V</i><sub>6</sub> = 124&#8239;000 − (1.056 × 6)', '<i>V</i><sub>6</sub> = 124&#8239;000 − (0.944 × 6)',
     '<i>V</i><sub>6</sub> = 124&#8239;000 − (0.056)<sup>6</sup>', '<i>V</i><sub>6</sub> = 124&#8239;000 × (0.944)<sup>6</sup>'],
    'E', 'V<sub>n</sub> = V<sub>0</sub> × (1 − r/100)<sup>n</sup> = 124&#8239;000 × (1 − 5.6/100)<sup>6</sup> = 124&#8239;000 × 0.944<sup>6</sup>'),
 MC(10, '7E', 5, P(LOUNGE) + P('A rule for the value of a lounge suite after <i>n</i> years is'),
    ['<i>V</i><sub><i>n</i></sub> = 1.094 × 4500', '<i>V</i><sub><i>n</i>+1</sub> = 0.906<i>V</i><sub><i>n</i></sub>', '<i>V</i><sub><i>n</i>+1</sub> = 0.906<sup><i>n</i></sup> × 4500',
     '<i>V</i><sub><i>n</i></sub> = 0.906<sup><i>n</i></sup> × 4500', '<i>V</i><sub><i>n</i></sub> = 1.094<sup><i>n</i></sup> × 4500'],
    'D', 'V<sub>n</sub> = (1 − 9.4/100)<sup>n</sup> × 4500 = 0.906<sup>n</sup> × 4500. B and C use V<sub>n+1</sub> (recurrence notation, not a rule); A and E use 1 + 9.4/100 (growth).'),
 # ================= short answer (each in the section of the last subchapter it needs)
 SA(1, '7C', 4, P('Casey’s first motorbike had a purchase price of $37&#8239;000.') + P('After five years, the value of the motorbike was $29&#8239;600.'),
    [('a', 'Let <i>C</i><sub><i>n</i></sub> be the value of the motorbike <i>n</i> years after it was purchased.<br>Assume that the value of the motorbike has depreciated using the <b>flat rate</b> method of depreciation.<br>'
      'Write a recurrence relation, in terms of <i>C</i><sub><i>n</i></sub> and <i>C</i><sub><i>n</i>+1</sub>, that models the value of the motorbike.',
      '(37&#8239;000 − 29&#8239;600) ÷ 5 = 1480 per year. C<sub>0</sub> = 37&#8239;000, &nbsp; C<sub>n+1</sub> = C<sub>n</sub> − 1480', 12, 2),
     ('b', 'The motorbike has travelled an average of 4000 km in each of the five years since it was purchased.<br>Assume that the value of the motorbike has been depreciated using the <b>unit cost</b> method of depreciation.<br>'
      'By how much is the value of the motorbike reduced per kilometre travelled?',
      'Rule V<sub>n</sub> = V<sub>0</sub> − nD: 35&#8239;520 = 37&#8239;000 − 4000 × D (one year) → D = $0.37: 37 cents per kilometre (a unit is required).', 10, 1)]),
 SA(9, '7C', 10, P('Saskia invests $3050 in an account earning 12% per annum on a flat rate basis.'),
    [('a i', 'Write a calculation that shows that the interest earned each year is $366.', '0.12 × 3050 = 366 (or 12/100 × 3050)', 5, 1),
     ('ii', 'Write the rule that gives the balance of the investment, <i>B</i><sub><i>n</i></sub>, in dollars after <i>n</i> years.', 'B<sub>n</sub> = 3050 + 366n', 5, 1),
     ('iii', 'How long until the balance is $7076?', '7076 = 3050 + 366n → n = 11 years', 6, 1)]),
 SA(2, '7D', '4–5', P('Jonathan purchased a car for $24&#8239;990.') + P('The value of Jonathan’s car was depreciated using the unit cost method of depreciation.')
    + P('The value of the car, in dollars, after <i>n</i> kilometres, <i>V</i><sub><i>n</i></sub>, can be modelled by the rule shown below.')
    + C('<i>V</i><sub>0</sub> = 24&#8239;990, &nbsp;&nbsp;&nbsp; <i>V</i><sub><i>n</i></sub> = 24&#8239;990 − 0.0015<i>n</i>'),
    [('a', 'Show that the value of the car after 20&#8239;000 kilometres is $24&#8239;960.', 'V<sub>n</sub> = 24&#8239;990 − 0.0015 × 20&#8239;000 = 24&#8239;960', 8, 2),
     ('b', 'What is the cost, in cents per kilometre, that Jonathan’s car is being depreciated?', '0.0015 × 100 = 0.15 cents per kilometre', 5, 1),
     ('c', 'If Jonathan were to use the flat rate method of depreciation, it would take him 3 years to depreciate the car to $23&#8239;191.<br>'
      'Find the annual flat rate of depreciation. Give your answer as a percentage. Round your answer to one decimal place.',
      '24&#8239;990 − 23&#8239;191 = 1799; 1799 ÷ 3 = 599.67 per year; 599.67 ÷ 24&#8239;990 × 100 = 2.39964% ≈ 2.4%', 8, 1),
     ('d', 'It was suggested to Jonathan that a reducing balance method of depreciation may be more appropriate to depreciate the value of his car.<br>'
      'If the car is depreciated at a reducing balance rate of 5.8% per annum, write down a recurrence relation, in terms of <i>A</i><sub>0</sub>, <i>A</i><sub><i>n</i>+1</sub> and <i>A</i><sub><i>n</i></sub>, for the value of Jonathan’s car, in dollars, after <i>n</i> years.',
      'R = 1 − 5.8/100 = 0.942. &nbsp; A<sub>0</sub> = 24&#8239;990, &nbsp; A<sub>n+1</sub> = 0.942 × A<sub>n</sub>', 12, 2)], long=True),
 SA(4, '7D', '6–7', P('Casey has opened a simple interest savings account in order to save money to buy a new motorbike. Interest is paid monthly into this account. '
      'The amount of money in the savings account after <i>n</i> years, <i>V</i><sub><i>n</i></sub>, can be modelled by the recurrence relation shown below.')
    + C('<i>V</i><sub>0</sub> = 6000, &nbsp;&nbsp;&nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V</i><sub><i>n</i></sub> + 216'),
    [('a', 'How much money did Casey initially deposit in his savings account?', '$6000 (V<sub>0</sub>)', 4, 1),
     ('b', 'What is the annual percentage interest rate for this savings account?', '216 ÷ 6000 × 100 = 3.6% p.a.', 7, 2),
     ('c i', 'The amount of money in the account after <i>n</i> years, <i>V</i><sub><i>n</i></sub>, can also be determined using a rule.<br>Complete the rule by writing the appropriate numbers in the boxes provided below.'
      '<div class="fillin" style="text-align:center"><i>V</i><sub><i>n</i></sub> = <span class="bx"><u>6000</u></span> + <span class="bx"><u>216</u></span> × <i>n</i></div>', '', 2, 1),
     ('ii', 'How much money will be in Casey’s savings account after 5 years?', 'V<sub>5</sub> = 6000 + 216 × 5 = $7080', 6, 1),
     ('d', 'Casey decides to compare a compound interest savings account to his savings in the simple interest account. He invests $6000 at an interest rate of 5.4% compounding annually. '
      'The amount of money in the savings account after <i>n</i> years, <i>V</i><sub><i>n</i></sub>, can be modelled by the recurrence relation shown below.'
      '<div style="text-align:center"><i>V</i><sub>0</sub> = 6000, &nbsp;&nbsp;&nbsp; <i>V</i><sub><i>n</i>+1</sub> = 1.054 × <i>V</i><sub><i>n</i></sub></div>'
      'Use recursion to write down calculations that show that the amount of money in Casey’s compound interest savings account after 2 years, <i>V</i><sub>2</sub>, will be $6665.50.',
      'V<sub>1</sub> = 1.054 × 6000 = 6324; &nbsp; V<sub>2</sub> = 1.054 × 6324 = 6665.496 ≈ $6665.50', 9, 1)], long=True),
 SA(6, '7D', 8, P('Jason is a personal trainer who has purchased a large piece of equipment for his home gym.') + P('The value of Jason’s equipment is depreciated using the reducing balance method.')
    + P('The value of the equipment, in dollars, after <i>n</i> years, <i>V</i><sub><i>n</i></sub>, can be modelled by the recurrence relation shown below.')
    + C('<i>V</i><sub>0</sub> = 12&#8239;000, &nbsp;&nbsp;&nbsp; <i>V</i><sub><i>n</i>+1</sub> = 0.92<i>V</i><sub><i>n</i></sub>'),
    [('a', 'Write down a calculation, using the value of the equipment after 4 years, to show that the value of Jason’s equipment after 5 years, <i>V</i><sub>5</sub>, is $7908.98.',
      'CAS recursion: V<sub>4</sub> = 8596.72. &nbsp; V<sub>5</sub> = 0.92 × 8596.72 = 7908.98', 7, 1),
     ('b', 'After how many years will the value of Jason’s equipment first fall below $7500?', 'V<sub>5</sub> = 7908.98, V<sub>6</sub> = 7276.26: after 6 years', 5, 1),
     ('c i', 'Jason has another option for depreciation of his equipment.<br>He can depreciate the value of his equipment using unit cost depreciation, where a ‘unit’ is counted each time the equipment is used for a workout.<br>'
      'In the first two years, Jason completed 1400 workouts.<br>The value of his equipment after this time was $10&#8239;850.<br>What is the unit cost of depreciation for Jason’s equipment?<br>Give your answer to the nearest cent.',
      '12&#8239;000 − 10&#8239;850 = 1150; 1150 ÷ 1400 = $0.82 (82 cents)', 6, 1),
     ('ii', 'Let <i>V</i><sub><i>n</i></sub> be the value of the equipment after <i>n</i> workouts, in dollars.<br>Write down a rule in terms of <i>V</i><sub><i>n</i></sub> that could be used to model the value of the equipment using this unit cost depreciation.',
      'V<sub>n</sub> = 12&#8239;000 − 0.82n', 5, 1)], long=True),
 SA(8, '7D', '9–10', P('Saskia buys a commercial washing machine for her laundromat business. The value of the washing machine after <i>n</i> years is shown by the equations below:')
    + C('<i>V</i><sub>0</sub> = 3875 &nbsp;&nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V</i><sub><i>n</i></sub> − 410'),
    [('a i', 'Showing recursive calculations, determine the value of the washing machine after two years.', 'V<sub>1</sub> = 3875 − 410 = 3465; &nbsp; V<sub>2</sub> = 3465 − 410 = $3055', 8, 1),
     ('ii', 'What is the annual flat rate of depreciation?<br>Write your answer as a percentage rounded to two decimal places.', '410 ÷ 3875 × 100 = 10.58%', 5, 1),
     ('b', 'An alternative model of depreciation is that the machine depreciates by $800 immediately upon purchase, then depreciates at 6% per year on a reducing balance basis.<br>'
      'What is the value of the machine after three years using this method?<br>Round your answer to the nearest dollar.',
      '3875 − 800 = 3075; 3075 × 0.94<sup>3</sup> = 2554.05 ≈ $2554 (or recursion V<sub>0</sub> = 3075, V<sub>n+1</sub> = 0.94V<sub>n</sub>)', 6, 1)]),
 SA(3, '7E', '5–6', P('Alison withdraws $5000 from her account to purchase a new photocopier for her business. The value of the photocopier will be depreciated using the reducing balance method. '
      'The value of Alison’s photocopier, in dollars, after <i>n</i> years, <i>C</i><sub><i>n</i></sub>, can be modelled by the recurrence relation shown below.')
    + C('<i>C</i><sub>0</sub> = 5000, &nbsp;&nbsp;&nbsp; <i>C</i><sub><i>n</i>+1</sub> = <i>R</i> × <i>C</i><sub><i>n</i></sub>'),
    [('a', 'The annual rate of depreciation for this photocopier is 18%.<br>What is the value of <i>R</i> in the recurrence relation?', 'R = 1 − 18/100 = 0.82', 6, 1),
     ('b', 'How much has the photocopier depreciated in value after five years of use?', '5000 × 0.82<sup>5</sup> = 1853.70; 5000 − 1853.70 = $3146.30', 7, 1),
     ('c', 'The value of the photocopier after one year of use is $4100. Alison’s company prints approximately 35&#8239;000 pages per month on this photocopier. Alison chooses to calculate the depreciation of her photocopier using unit cost depreciation.<br>'
      'By how much does the photocopier depreciate per page, using this method?<br>Give your answer in cents to one decimal place.',
      '900 depreciation in one year; 35&#8239;000 × 12 = 420&#8239;000 pages; 900 ÷ 420&#8239;000 = $0.002143 = 0.2 cents per page', 8, 1)]),
 SA(5, '7E', '7–8', P('Alison invests her money into a savings account that will pay compound interest every month. The balance of Alison’s account, after <i>n</i> months, <i>V</i><sub><i>n</i></sub>, can be modelled by the recurrence relation shown below.')
    + C('<i>V</i><sub>0</sub> = 8000, &nbsp;&nbsp;&nbsp; <i>V</i><sub><i>n</i>+1</sub> = 1.00225 <i>V</i><sub><i>n</i></sub>'),
    [('a', 'What is the annual interest rate for Alison’s savings account?', 'Solve 1.00225 = 1 + (r/12)/100 → r = 2.7% per annum', 6, 1),
     ('b i', 'Recursion can be used to calculate the balance of the account after each month.<br>Write down a calculation to show that the balance in the account after two months, <i>V</i><sub>2</sub>, is $8036.04.',
      'V<sub>1</sub> = 1.00225 × 8000 = 8018; &nbsp; V<sub>2</sub> = 1.00225 × 8018 = 8036.04', 7, 1),
     ('ii', 'After how many months will the balance of Alison’s account first exceed $8500?', 'CAS recursion: after 27 months', 5, 1),
     ('c', 'A rule of the form <i>V</i><sub><i>n</i></sub> = <i>a</i> × <i>b</i><sup><i>n</i></sup> can be used to determine the balance of Alison’s account after <i>n</i> months.<br>Write the rule for Alison’s investment below.',
      'V<sub>n</sub> = 8000 × 1.00225<sup>n</sup>', 6, 1),
     ('d', 'The value of Alison’s investment after 12 months is $8219 when rounded to the nearest dollar.<br>What is the equivalent flat rate interest rate, per annum, for Alison’s investment?<br>Round your answer to two decimal places.',
      'Interest = 8219 − 8000 = 219; 219 = 8000 × r × 1 ÷ 100 → r = 219 ÷ 8000 × 100 = 2.74%', 7, 1)], long=True),
 SA(7, '7E', 9, P('Jo invests $80&#8239;000 at a simple interest rate of 3.4% per annum.') + P('Her brother Anthony invests the same amount of money in an account earning 3.25% per annum, compounding annually.'),
    [('a', 'How much interest does Jo earn each year?', '0.034 × 80&#8239;000 = $2720', 4, 1),
     ('b', 'Write a recurrence relation to model the value of Anthony’s investment in terms of <i>V</i><sub>0</sub>, <i>V</i><sub>n+1</sub> and <i>V</i><sub>n</sub>.', 'V<sub>0</sub> = 80&#8239;000, &nbsp; V<sub>n+1</sub> = 1.0325V<sub>n</sub>', 6, 1),
     ('c', 'What is the value of Anthony’s investment after eight years?', 'V<sub>8</sub> = 1.0325<sup>8</sup> × 80&#8239;000 = $103&#8239;326.20 (or Finance Solver)', 6, 1),
     ('d', 'After how many years will Anthony’s investment be larger than Jo’s?',
      'Jo: 80&#8239;000, 82&#8239;720, 85&#8239;440, 88&#8239;160, 90&#8239;880. Anthony: 80&#8239;000, 82&#8239;600, 85&#8239;284.50, 88&#8239;056.25, 90&#8239;918.07. After four years.', 7, 1)], long=True),
]

SUBS = [('7A', 'Sequences and recurrence relations'), ('7B', 'Linear growth and decay: simple interest, flat rate and unit cost depreciation'),
        ('7C', 'Rules for the <i>n</i>th term of linear growth and decay'), ('7D', 'Geometric growth and decay: compound interest and reducing balance depreciation'),
        ('7E', 'Rules for the <i>n</i>th term of geometric growth and decay'), ('7F', 'Interest rates over different periods; effective interest rates')]
EMPTY = {'7F': 'No Insight question in this section: practise with the Cambridge 7F exercises.'}
