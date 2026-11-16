"""Lesson gm12-u3-l40 (8D analysing financial situations using amortisation tables) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l40/build.py (CFAT and Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3C #8; Edrolo U1&2 3D Q15 (adapted by Edrolo from VCAA 2020 Exam 2 Q9a).
Examples 15-17 = Cambridge U3&4 pp. 416-418. You trys = Edrolo U3&4 6D WE2a-b, 6D WE2c, written YT-8D-17.
Exits = VCAA 2020 Exam 1 Q25 (Edrolo 6E Q15), VCAA 2021 Exam 1 Q23 (6B Q20).
Output: lessons/8D worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l40/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
HL = ['Payment number', 'Payment', 'Interest', 'Principal reduction', 'Balance']
def T(rows, head=HL): return table([head] + rows, style='width:100%;font-size:8.5pt')

def plot(series, ymax, ystep, nmax, xl='Payment (n)', yl='Amount ($)', draw=False, W=230, Hh=125, mm=62):
    """Points on a grid. draw=False: grid only for students, points in red on the solutions copy."""
    L, Tp, B = 34, 8, 24
    o, y0, k = ws2._grid(W, Hh, L, Tp, B, ymax, ystep, yl, xl)
    sx = (W - 8 - L) / nmax
    o += [f'<text x="{L+n*sx:.1f}" y="{y0+10}" font-size="8.5" text-anchor="middle">{n}</text>' for n in range(nmax + 1)]
    g = []
    for sh, pts in series:
        for n, v in pts:
            g.append(f'<circle cx="{L+n*sx:.1f}" cy="{y0-v*k:.1f}" r="2.6" fill="{ws2.RED if not draw else "#000"}"/>' if sh == 'o' else
                     f'<rect x="{L+n*sx-2.6:.1f}" y="{y0-v*k-2.6:.1f}" width="5.2" height="5.2" fill="{ws2.RED if not draw else "#000"}"/>')
    o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(g) + '</g>')
    return ws2._svg(W, Hh, o, mm)

P = [title('8D', 'Analysing financial situations using amortisation tables')]
P.append(lis(['To be able to find the final payment in a reducing balance loan and an annuity.', 'To be able to find the total payment made/received and the total interest paid/earned.',
              'To be able to plot points using an amortisation table for a reducing balance loan, an annuity and a compound interest investment with additional payments.']))
P.append(sect('Activating prior knowledge', 'Year 11 skill and a VCAA question'))
P.append(box('Question 1', q('The sequence, 5, 8, 11, ... is an arithmetic sequence with a common difference of 3. Construct a table showing the term number, <i>n</i>, and its value, <i>t<sub>n</sub></i>, for the first four terms in the sequence. Use the table to plot the graph.')
  + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;align-items:center">'
  + table([['<i>n</i>', '0', '1', '2', '3'], ['<i>t<sub>n</sub></i>', a('5'), a('8'), a('11'), a('14')]], style='width:100%;font-size:9pt')
  + plot([('o', [(0, 5), (1, 8), (2, 11), (3, 14)])], 16, 2, 4, xl='n', yl='tₙ', mm=58) + '</div>', ''))
P.append(box('Question 2 · VCAA 2020 Exam 2 Q9a (adapted)', q('Amahle opens a savings account. Let <i>B<sub>n</sub></i> be the balance of this savings account, in dollars, <i>n</i> months after it was opened. The month-to-month value of <i>B<sub>n</sub></i> can be determined using the following recurrence relation. &nbsp;<i>B</i><sub>0</sub> = 6000, &nbsp;<i>B</i><sub><i>n</i>+1</sub> = 1.002<i>B<sub>n</sub></i>')
  + q('Write down the value of <i>B</i><sub>3</sub>, the balance of the savings account after three months. Round to the nearest cent.') + space(12, '6012 → 6024.024 → $6036.07'), ''))

P.append(sect('8D Finding the final payment', 'Example, then you try'))
MT = T([['0', '0.00', '0.00', '0.00', '5000.00'], ['1', '2010.00', '500.00', '1510.00', '3490.00'], ['2', '2010.00', '349.00', '1661.00', '1829.00'], ['3', '', '', '', '0.00']], HL[:4] + ['Balance of investment'])
MIKE = 'Mike invests $5000 in an annuity account paying interest at 10% per annum. Mike wants to receive a payment of $2010 per year. This is modelled using the following amortisation table.'
P.append(exyt('Example 15 · Finding the final payment for a reducing balance loan or annuity',
  q('Consider the following amortisation table for a reducing balance loan of $20 000 with an interest rate of 8% per annum, compounding annually. Regular payments of $5009.12 are made for the first four years as shown in the amortisation table.')
  + T([['0', '0.00', '0.00', '0.00', '20 000.00'], ['1', '5009.12', '1600.00', '3409.12', '16 590.88'], ['2', '5009.12', '1327.27', '3681.85', '12 909.03'], ['3', '5009.12', '1032.72', '3976.40', '8932.63'], ['4', '5009.12', '714.61', '4294.51', '4638.12']])
  + q('Calculate the final payment required in the fifth year to pay off the loan fully.') + space(14, 'Interest = 8/100 × 4638.12 = 371.05<br>Final payment = 4638.12 + 371.05 = $5009.17'),
  'You try 1', q(MIKE) + MT + q('Mike wants the final payment amount adjusted so that the annuity will be fully paid out after payment number 3.')
  + parts([('a', 'Calculate the missing interest for payment number 3.', '10/100 × 1829.00 = $182.90', 12), ('b', 'Calculate the final payment that Mike will receive for this annuity.', '1829.00 + 182.90 = $2011.90', 12)])))

P.append(sect('8D Total payments and total interest', 'Example, then you try'))
P.append(exyt('Example 16 · Finding the total payment made and total interest paid',
  q('Consider the following amortisation table for a reducing balance loan of $10 000 with an interest rate of 8% per annum, compounding quarterly. Three quarterly payments of $2626 are made.')
  + T([['0', '0.00', '0.00', '0.00', '10 000.00'], ['1', '2626.00', '200.00', '2426.00', '7574.00'], ['2', '2626.00', '151.48', '2474.52', '5099.48'], ['3', '2626.00', '101.99', '2524.01', '2575.47'], ['4', 'A', 'B', 'C', '0.00']])
  + parts([('a', 'Complete the amortisation table corresponding to payment four such that the final payment ensures that the balance is 0.', 'B = 8/400 × 2575.47 = 51.51 · C = 2575.47 · A = 2575.47 + 51.51 = 2626.98', 12),
           ('b', 'Calculate the total payment made for the loan.', '2626 × 3 + 2626.98 = $10 504.98', 9), ('c', 'Calculate the total interest paid on the loan.', '10 504.98 − 10 000 = $504.98', 9)]),
  'You try 2', q(MIKE) + MT + q('Mike wants the final payment amount adjusted so that the annuity will be fully paid out after payment number 3. The final payment is $2011.90.')
  + q('c. How much interest has the account earned over three years?') + space(30, '2 × 2010.00 + 2011.90 = 6031.90<br>6031.90 − 5000.00 = $1031.90')))

P.append(sect('8D Plotting from an amortisation table', 'Example, then you try'))
E17 = [('o', [(1, 12.5), (2, 9.43), (3, 6.33), (4, 3.18)]), ('s', [(1, 245.35), (2, 248.42), (3, 251.52), (4, 254.71)])]
Y17 = [('o', [(1, 8), (2, 6.03), (3, 4.04), (4, 2.03)]), ('s', [(1, 197), (2, 198.97), (3, 200.96), (4, 203.07)])]
P.append(exyt('Example 17 · Plotting from an amortisation table',
  q('Consider the following amortisation table for a reducing balance loan.')
  + T([['0', '0.00', '0.00', '0.00', '1000.00'], ['1', '257.85', '12.50', '245.35', '754.65'], ['2', '257.85', '9.43', '248.42', '506.23'], ['3', '257.85', '6.33', '251.52', '254.71'], ['4', '257.89', '3.18', '254.71', '0.00']])
  + q('Plot a graph of the interest and principal reduction on the same graph.') + plot(E17, 300, 50, 5) + q(A('● interest &nbsp; ■ principal reduction')),
  'You try 3', q('Consider the following amortisation table for a reducing balance loan.')
  + T([['0', '0.00', '0.00', '0.00', '800.00'], ['1', '205.00', '8.00', '197.00', '603.00'], ['2', '205.00', '6.03', '198.97', '404.03'], ['3', '205.00', '4.04', '200.96', '203.07'], ['4', '205.10', '2.03', '203.07', '0.00']])
  + q('Plot a graph of the interest and principal reduction on the same graph.') + space(44, plot(Y17, 250, 50, 5) + '● interest &nbsp; ■ principal reduction')))

P.append(sect('Exit tasks', 'Show what you know'))
FLAT = ('<svg viewBox="0 0 230 110" width="100%" style="max-width:55mm;display:block;margin:1mm auto"><line x1="25" y1="95" x2="25" y2="5" stroke="#000"/><line x1="25" y1="95" x2="220" y2="95" stroke="#000"/>'
        '<text x="10" y="12" font-size="10" font-style="italic">A<tspan font-size="7" dy="3">n</tspan></text><text x="222" y="98" font-size="10" font-style="italic">n</text>'
        + ''.join(f'<circle cx="{25+n*35}" cy="15" r="3" fill="#000"/><text x="{25+n*35}" y="106" font-size="9" text-anchor="middle">{n}</text>' for n in range(6)) + '</svg>')
P.append(box('Exit task 1 · VCAA 2020 Exam 1 Q25', q('The graph below represents the value of an annuity investment, <i>A<sub>n</sub></i>, in dollars, after <i>n</i> time periods.') + FLAT
  + q('A recurrence relation that could match this graphical representation is')
  + mc([f'<i>A</i><sub>0</sub> = 200 000, &nbsp;<i>A</i><sub><i>n</i>+1</sub> = {r}<i>A<sub>n</sub></i> − {d}' for r, d in (('1.015', '2500'), ('1.025', '5000'), ('1.03', '5500'), ('1.04', '6000'), ('1.05', '8000'))], 'B')
  + why('flat graph: interest = payment; 2.5% × 200 000 = 5000'), ''))
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q23', q('Bimal has a reducing balance loan. The balance, in dollars, of the loan from month to month, <i>B<sub>n</sub></i>, is modelled by the recurrence relation below. &nbsp;<i>B</i><sub>0</sub> = 450 000, &nbsp;<i>B</i><sub><i>n</i> + 1</sub> = <i>RB<sub>n</sub></i> – 2633')
  + q('Given that the loan will be fully repaid in 20 years, the value of <i>R</i> is closest to') + mc(['1.003', '1.0036', '1.03', '1.036', '1.36'], 'A', cols=5)
  + why('Finance Solver N = 240, PV = 450 000, PMT = −2633, FV = 0 → 3.6% p.a. = 0.3% per month → R = 1.003'), ''))
SC = ['I can find the final payment for a reducing balance loan or annuity.', 'I can find the total payment made and the total interest paid.', 'I can plot from an amortisation table.']
P.append(close(SC, [('8D', 'Q1–12')], ['8D']))
build('l40', '8D', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l40-worksheet', '8D worksheet'), ('l40-worksheet-solutions', '8D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
