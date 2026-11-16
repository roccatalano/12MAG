"""Lesson gm12-u3-l39 (8C amortisation tables) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l39/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3E #11; VCAA 2021 Exam 2 Q7a (Edrolo U1&2 3C Q18).
Examples 10-14 = Cambridge U3&4 pp. 408-411. You trys = Edrolo U3&4 6A WE1, written YT-8C-11, Edrolo 6B WE2, written YT-8C-13, Edrolo 6F WE2.
Exits = VCAA 2016 Exam 1 Q22 (Edrolo 6B Q19), VCAA 2017 Exam 1 Q23 (6F Q18).
Output: lessons/8C worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l39/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
HL = ['Payment number', 'Payment', 'Interest', 'Principal reduction', 'Balance']
HI = ['Payment number', 'Payment', 'Interest', 'Principal increase', 'Balance']
def T(rows, head=HL): return table([head] + rows, style='width:100%;font-size:8.5pt')

P = [title('8C', 'Amortisation tables')]
P.append(lis(['To be able to apply the amortisation process.', 'To be able to construct an amortisation table.', 'To be able to analyse an amortisation table for a reducing balance loan.',
              'To be able to read and interpret an amortisation table for an annuity to find the interest rate.', 'To be able to interpret and construct an amortisation table for a compound interest investment with additions to the principal.']))
P.append(sect('Activating prior knowledge', 'Year 11 skill and a VCAA question'))
P.append(box('Question 1', q('An investment of $2200 pays interest at the rate of 5% per annum in the form of simple interest. Find the amount of interest paid each year.') + space(12, '5/100 × 2200 = $110'), ''))
P.append(box('Question 2 · VCAA 2021 Exam 2 Q7a', q('Sienna owns a coffee shop. A coffee machine, purchased for $12 000, is depreciated in value using the unit cost method. The rate of depreciation is $0.05 per cup of coffee made. The recurrence relation that models the year-to-year value, in dollars, of the coffee machine is <i>M</i><sub>0</sub> = 12 000, &nbsp;<i>M</i><sub><i>n</i>+1</sub> = <i>M<sub>n</sub></i> – 1440')
  + q('a. Calculate the number of cups of coffee that the machine produces per year.') + space(12, '1440 ÷ 0.05 = 28 800'), ''))

P.append(sect('8C Amortisation tables for reducing balance loans', 'Example, then you try'))
P.append(exyt('Example 10 · Applying the amortisation process',
  q('Flora borrows $20 000 at an interest rate of 8% per annum, compounding annually. She makes annual payments of $2500.')
  + parts([('a', 'State the principal of the loan. ' + A('$20 000'), '', 'L'), ('b', 'Calculate the initial interest charged on the principal. ' + A('8% × 20 000 = $1600'), '', 'L'),
           ('c', 'Determine the impact of the first annual payment to find the principal reduction. ' + A('2500 − 1600 = $900'), '', 'L'), ('d', 'Calculate the new balance. ' + A('20 000 − 900 = $19 100'), '', 'L'),
           ('e', 'Complete the row in the table below with your calculations.' + T([['1', '2500.00', a('1600.00'), a('900.00'), a('19 100.00')]]), '', 4)]),
  'You try 1', q('Ella has borrowed $10 000 from her parents to pay for a trip to Europe. They have decided not to charge interest on the loan and Ella will make equal weekly repayments once she gets back from her trip. The first five lines of the amortisation table for this loan is shown. The loan balance for the third week is missing.')
  + T([['0', '0.00', '0.00', '0.00', '10 000.00'], ['1', '150.00', '0.00', '150.00', '9850.00'], ['2', '150.00', '0.00', '150.00', '9700.00'], ['3', '150.00', '0.00', '150.00', ''], ['4', '150.00', '0.00', '150.00', '9400.00']], HL[:4] + ['Balance of loan'])
  + parts([('a', 'How much is Ella paying each week?', '$150', 10), ('b', 'Calculate the loan balance after the third repayment.', '9700.00 − 150.00 = $9550', 16)])))
E = lambda n: [[str(i), '', '', '', ''] for i in range(1, n + 1)]
P.append(exyt('Example 11 · Constructing an amortisation table for a reducing balance loan',
  q('Flora borrows $20 000 at an interest rate of 8% per annum, compounding annually. She makes annual payments of $2500. Construct an amortisation table for Flora’s reducing balance loan for the first three payments.')
  + T([['0', '0.00', '0.00', '0.00', '20 000.00'], ['1', a('2500.00'), a('1600.00'), a('900.00'), a('19 100.00')], ['2', a('2500.00'), a('1528.00'), a('972.00'), a('18 128.00')], ['3', a('2500.00'), a('1450.24'), a('1049.76'), a('17 078.24')]]),
  'You try 2', q('Sam borrows $12 000 at an interest rate of 6% per annum, compounding annually. He makes annual payments of $3000. Construct an amortisation table for Sam’s reducing balance loan for the first three payments.')
  + space(34, T([['0', '0.00', '0.00', '0.00', '12 000.00'], ['1', '3000.00', '720.00', '2280.00', '9720.00'], ['2', '3000.00', '583.20', '2416.80', '7303.20'], ['3', '3000.00', '438.19', '2561.81', '4741.39']]))))
P.append(exyt('Example 12 · Analysing an amortisation table for a reducing balance loan',
  q('A business borrows $10 000 at a rate of 8% per annum, compounding quarterly. The loan is to be repaid by making quarterly payments of $2700.00. The amortisation table for this loan is shown below.')
  + T([['0', '0.00', '0.00', '0.00', '10 000.00'], ['1', '2700.00', '', '2500.00', '7500.00'], ['2', '2700.00', '150.00', '', '4950.00'], ['3', '2700.00', '99.00', '2601.00', '']])
  + parts([('a', 'Calculate the interest paid on the initial balance. ' + A('8/400 × 10 000 = $200'), '', 'L'), ('b', 'Calculate the principal reduction from the second payment. ' + A('2700 − 150 = $2550.00'), '', 'L'),
           ('c', 'Calculate the balance of the loan after payment 3 has been made. ' + A('4950 − 2601 = $2349'), '', 'L')]),
  'You try 3', q('The first four lines of an amortisation table for a reducing balance loan of $500 000 are shown. Interest is charged at a rate of 6.2% per annum, compounding quarterly. The loan is to be repaid with quarterly payments. There are a number of cells missing.')
  + T([['0', '0.00', '0.00', '0.00', '500 000.00'], ['1', '10 000.00', '7750.00', '2250.00', '497 750.00'], ['2', 'a.', '7715.13', '2284.87', '495 465.13'], ['3', '10 000.00', 'b.', 'c.', 'd.']], HL[:4] + ['Balance of loan'])
  + parts([('a', 'Calculate the missing payment value for payment number 2.', '$10 000.00', 9), ('b', 'Calculate the missing interest for payment number 3.', '6.2/400 × 495 465.13 = $7679.71', 9),
           ('c', 'Calculate the missing principal reduction for payment number 3.', '$2320.29', 9), ('d', 'Calculate the missing loan balance after payment number 3.', '$493 144.84', 9)])))

P.append(sect('8C Amortisation tables for annuities', 'Example, then you try'))
P.append(exyt('Example 13 · Analysing an amortisation table for an annuity to find the interest rate',
  q('Consider the following amortisation table for an annuity after 3 monthly payments.')
  + T([['0', '0.00', '0.00', '0.00', '12 000.00'], ['1', '2200.00', '60.00', '2140.00', '9860.00'], ['2', '2200.00', '49.30', '2150.70', '7709.30'], ['3', '2200.00', 'A', 'B', '5547.85']])
  + parts([('a', 'State the principal of the annuity and the amount of interest paid in the first month. ' + A('$12 000; $60'), '', 'L'), ('b', 'Calculate the monthly interest rate. ' + A('60 ÷ 12 000 × 100 = 0.5%'), '', 'L'),
           ('c', 'Find the value of A and B. ' + A('A = 38.55, B = 2161.45'), '', 'L')]),
  'You try 4', q('Consider the following amortisation table for an annuity after 3 monthly payments.')
  + T([['0', '0.00', '0.00', '0.00', '8000.00'], ['1', '1500.00', '40.00', '1460.00', '6540.00'], ['2', '1500.00', '32.70', '1467.30', '5072.70'], ['3', '1500.00', 'A', 'B', '3598.06']])
  + parts([('a', 'Find the annual interest rate for this annuity.', '0.5% per month × 12 = 6% p.a.', 14), ('b', 'Find the values of A and B.', 'A = $25.36, B = $1474.64', 14)])))

P.append(sect('8C Investments with additions to the principal', 'Example, then you try'))
P.append(exyt('Example 14 · Constructing an amortisation table for a compound interest investment with additional payments',
  q('Consider the following amortisation table for a compound interest investment with monthly additions to the principal. Assume that interest compounds monthly.')
  + T([['0', '0.00', '0.00', '0.00', '1200.00'], ['1', '50.00', '3.00', '53.00', '1253.00'], ['2', '50.00', '3.13', '53.13', '1306.13'], ['3', '50.00', '3.27', '53.27', '1359.40']], HI)
  + q('Complete two additional lines for the table corresponding to payment 4 and payment 5. ' + A('rate = 3 ÷ 1200 = 0.25%'))
  + T([['4', a('50.00'), a('3.40'), a('53.40'), a('1412.80')], ['5', a('50.00'), a('3.53'), a('53.53'), a('1466.33')]], HI),
  'You try 5', q('The table shown represents an annuity investment with an initial deposit of $5000 and an interest rate of 5.2% per annum, compounding quarterly. Regular deposits of $200 are made at the end of each quarter. There are a few cells missing.')
  + T([['0', '0.00', '0.00', '0.00', '5000.00'], ['1', 'a.', '65.00', '265.00', '5265.00'], ['2', '200.00', '68.45', 'b.', '5533.45'], ['3', '200.00', '71.93', '271.93', 'c.'], ['4', '200.00', 'd.', '275.47', '6080.85']], ['Payment number', 'Payment', 'Interest', 'Principal addition', 'Balance of investment'])
  + parts([('a', 'Determine the missing payment for payment number 1.', '$200', 8), ('b', 'Calculate the missing principal addition for payment number 2.', '$268.45', 8),
           ('c', 'Calculate the missing investment balance after payment number 3.', '$5805.38', 8), ('d', 'Calculate the missing interest for payment number 4.', '5.2/400 × 5805.38 = $75.47', 8)])))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 1 Q22', q('The first three lines of an amortisation table for a reducing balance home loan are shown below. The interest rate for this home loan is 4.8% per annum compounding monthly. The loan is to be repaid with monthly payments of $1500.')
  + T([['0', '0', '0.00', '0.00', '250 000.00'], ['1', '1500', '1000.00', '500.00', '249 500.00'], ['2', '1500', '', '', '']], HL[:4] + ['Balance of loan'])
  + q('The amount of payment number 2 that goes towards reducing the principal of the loan is') + mc(['$486', '$502', '$504', '$996', '$998'], 'B', cols=5) + why('interest 0.004 × 249 500 = 998; 1500 − 998 = 502'), ''))
P.append(box('Exit task 2 · VCAA 2017 Exam 1 Q23', q('Four lines of an amortisation table for an annuity investment are shown below. The interest rate for this investment remains constant, but the payment value may vary.')
  + T([['17', '100.00', '27.40', '127.40', '6977.50'], ['18', '100.00', '27.91', '127.91', '7105.41'], ['19', '100.00', '28.42', '128.42', '7233.83'], ['20', '', '', '', '7500.00']], ['Payment number', 'Payment', 'Interest', 'Principal addition', 'Balance of investment'])
  + q('The balance of the investment after payment number 20 is $7500. The value of payment number 20 is closest to') + mc(['$29', '$100', '$135', '$237', '$295'], 'D', cols=5) + why('0.4% × 7233.83 = 28.94; 7500 − 7233.83 = 266.17; 266.17 − 28.94 = 237.23'), ''))
SC = ['I can apply the amortisation process.', 'I can construct an amortisation table for a reducing balance loan.', 'I can analyse an amortisation table for a reducing balance loan.',
      'I can analyse an amortisation table for an annuity to find the interest rate.', 'I can interpret and construct an amortisation table for a compound interest investment with additional payments.']
P.append(close(SC, [('8C', 'Q1–11')], ['8C']))
build('l39', '8C', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l39-worksheet', '8C worksheet'), ('l39-worksheet-solutions', '8C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
