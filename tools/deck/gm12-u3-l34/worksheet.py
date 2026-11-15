"""Lesson gm12-u3-l34 (7F interest rates over different periods; effective rates) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l34/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = Cambridge U1&2 Ch 3 skills checklist 3H #23; VCAA 2020 Further Exam 1 Q26 (Edrolo U1&2 3F Q14).
Examples 28-32 = Cambridge U3&4 pp. 373-377. You trys = Edrolo U1&2 3E WE3a, Edrolo U3&4 5F WE1a, 5F WE1b-c, 5G WE2, 5G WE1.
Exits = VCAA 2020 Exam 1 Q24 (Edrolo 5F Q17), VCAA 2020 Exam 1 Q28 (5G Q11), VCAA 2017 Exam 2 Q6 (5F Q18).
Output: lessons/7F worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l34/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
A = lambda v: ans(v)
RR = lambda v0, rule, L='V': f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
VN = '<i>V<sub>n</sub></i>'
def axes(pts=(), col='#000'):
    W, Hh, l, b, t = 230, 120, 44, 18, 8
    X = lambda n: l + (W - l - 10) * (n + 0.5) / 5; Y = lambda v: t + (Hh - b - t) * (1 - (v - 10000) / 150)
    o = [f'<line x1="{l}" y1="{Y(10000)}" x2="{W-6}" y2="{Y(10000)}" stroke="#000"/><line x1="{l}" y1="{t}" x2="{l}" y2="{Y(10000)}" stroke="#000"/>']
    for v in (10000, 10050, 10100, 10150): o.append(f'<line x1="{l}" y1="{Y(v)}" x2="{W-6}" y2="{Y(v)}" stroke="#ccc" stroke-width=".6"/><text x="{l-3}" y="{Y(v)+3}" font-size="8" text-anchor="end">{v:,}</text>'.replace(',', ' '))
    for n in range(5): o.append(f'<text x="{X(n)}" y="{Y(10000)+11}" font-size="8" text-anchor="middle">{n}</text>')
    o.append(f'<text x="{W-6}" y="{Y(10000)+11}" font-size="8" font-style="italic">n</text><text x="{l+3}" y="{t+6}" font-size="8" font-style="italic">Vₙ</text>')
    o.append('<g class="ans">' + ''.join(f'<circle cx="{X(n)}" cy="{Y(v)}" r="2.6" fill="{col}"/>' for n, v in enumerate(pts)) + '</g>')
    return f'<svg viewBox="0 0 {W} {Hh}" style="width:62mm;display:block;margin:1mm auto">{"".join(o)}</svg>'

P = [title('7F', 'Interest rates over different time periods and effective interest rates')]
LI = ['To be able to convert nominal (annual) interest rates to compounding period interest rates.', 'To be able to model loans with different compounding periods using recurrence relations.',
      'To be able to model investments with different compounding periods using recurrence relations.', 'To be able to compare loans and investments using effective interest rates.',
      'To be able to calculate effective interest rates using a CAS calculator.']
P.append(lis(LI))
P.append(sect('Activating prior knowledge', 'Year 11 skill and a VCAA question'))
P.append(box('Question 1', q('Jack borrows $2000. He will pay interest at the rate of 4.2% per annum. Write down a recurrence relation to model the value of Jack’s loan if interest is compounded quarterly.') + space(16, 'R = 1 + 4.2/(100 × 4) = 1.0105; V₀ = 2000, Vₙ₊₁ = 1.0105Vₙ'), ''))
P.append(box('Question 2 · VCAA 2020 Exam 1 Q26', q('Ray deposited $5000 in an investment account earning interest at the rate of 3% per annum, compounding quarterly.<br>A rule for the balance, <i>R<sub>n</sub></i>, in dollars, after <i>n</i> years is given by')
  + mc(['<i>R<sub>n</sub></i> = 5000 × 0.03<sup><i>n</i></sup>', '<i>R<sub>n</sub></i> = 5000 × 1.03<sup><i>n</i></sup>', '<i>R<sub>n</sub></i> = 5000 × 0.03<sup>4<i>n</i></sup>', '<i>R<sub>n</sub></i> = 5000 × 1.0075<sup><i>n</i></sup>', '<i>R<sub>n</sub></i> = 5000 × 1.0075<sup>4<i>n</i></sup>'], 'E', cols=2)
  + why('R = 1 + 3/400 = 1.0075 per quarter; n is in years, so 4n quarters'), ''))

P.append(sect('7F Interest rate conversions and compounding periods', 'Example, then you try'))
P.append(exyt('Example 28 · Converting nominal interest rates to compounding period interest rates',
  q('An investment account will pay interest at the rate of 4.68% per annum. Convert this interest rate to each of the following rates:')
  + parts([('a', 'monthly ' + A('4.68 ÷ 12 = 0.39%'), '', 'L'), ('b', 'fortnightly ' + A('4.68 ÷ 26 = 0.18%'), '', 'L'), ('c', 'quarterly ' + A('4.68 ÷ 4 = 1.17%'), '', 'L')]),
  'You try 28', q('Tully invests $5000 in a savings account that earns interest at a rate of 4.6% p.a., compounding monthly.')
  + parts([('a', 'Calculate the interest rate, as a percentage, per compounding period. Round to two decimal places.', '4.6 ÷ 12 = 0.38% per compounding period', 20)])))
P.append(exyt('Example 29 · Recurrence relations with different compounding periods',
  q('Brian borrows $5000 from a bank. He will pay interest at the rate of 4.5% per annum. Let ' + VN + ' be the value of the loan after <i>n</i> compounding periods. Write down a recurrence relation to model the value of Brian’s loan if interest is compounded:')
  + parts([('a', 'yearly<br>' + A('R = 1.045: V₀ = 5000, Vₙ₊₁ = 1.045Vₙ'), '', 'L'), ('b', 'quarterly<br>' + A('R = 1 + 4.5/400 = 1.01125: V₀ = 5000, Vₙ₊₁ = 1.01125Vₙ'), '', 'L'),
           ('c', 'monthly<br>' + A('R = 1 + 4.5/1200 = 1.00375: V₀ = 5000, Vₙ₊₁ = 1.00375Vₙ'), '', 'L')]),
  'You try 29', q('Duncan has an investment of $10 000 that is earning interest at a rate of 8% per annum, compounding fortnightly.')
  + parts([('a', 'Construct a recurrence relation that can be used to calculate value of the investment, ' + VN + ', after <i>n</i> fortnights. Round to three decimal places where necessary.', 'r = 8 ÷ 26 = 0.307…%, R ≈ 1.003; V₀ = 10 000, Vₙ₊₁ = 1.003 × Vₙ', 26)])))
P.append(exyt('Example 30 · Modelling an investment that compounds monthly using recurrence relations',
  q('A principal value of $10 000 is invested in an account earning compound interest monthly at the rate of 9% per annum. Let ' + VN + ' be the value of the investment after <i>n</i> months.')
  + parts([('a', 'Calculate the growth multiplier, <i>R</i>. ' + A('1 + 9/1200 = 1.0075'), '', 'L'),
           ('b', 'Write down a recurrence relation for the value of the investment after <i>n</i> months. ' + A('V₀ = 10 000, Vₙ₊₁ = 1.0075Vₙ'), '', 'L'),
           ('c', 'Write down a rule for the value of the investment after <i>n</i> months. ' + A('Vₙ = 1.0075ⁿ × 10 000'), '', 'L'),
           ('d', 'Use this rule to find the value of the investment after 4 years. ' + A('V₄₈ = 1.0075⁴⁸ × 10 000 = $14 314.05'), '', 'L')]),
  'You try 30', q('Duncan has an investment of $10 000 that is earning interest at a rate of 8% per annum, compounding fortnightly. (Part a: ' + RR('10 000', '1.003 × ' + VN) + ')')
  + parts([('b', 'Calculate the value of Duncan’s investment after 4 fortnights.', 'V₁ = 10 030, V₂ = 10 060.09, V₃ = 10 090.27, V₄ = $10 120.54', 20),
           ('c', 'Plot the value of the investment for the first four fortnights on the set of axes shown.' + axes([10000, 10030, 10060.09, 10090.27, 10120.54], '#c00000'), '', 2)])))

P.append(sect('7F Effective interest rates', 'Example, then you try'))
P.append(exyt('Example 31 · Comparing loans and investments with effective interest rates',
  q('Brooke would like to borrow $20 000 that she will repay entirely after one year. She is deciding between two loan options:<br>option A: 5.95% per annum, compounding weekly<br>option B: 6% per annum, compounding quarterly.')
  + parts([('a', 'Calculate the effective interest rate for each investment.<br>A: ' + A('((1 + 5.95/5200)⁵² − 1) × 100% = 6.13%') + '<br>B: ' + A('((1 + 6/400)⁴ − 1) × 100% = 6.14%'), '', 'L'),
           ('b', 'Which investment option is the best and why?<br>' + A('Option A: a loan, so the lower effective rate means less interest'), '', 'L')]),
  'You try 31', q('Pete is saving up money for schoolies and is considering investing his savings into either of two accounts with the following interest rates:<br>• Superior Saver: 4.5% per annum, compounding quarterly<br>• Supreme Saver: 4.4% per annum, compounding weekly<br>Which account should Pete choose?')
  + space(40, 'Superior: 4.5765…%; Supreme: 4.4962…%. Investment → higher effective rate: Superior Saver')))
P.append(exyt('Example 32 · Calculating effective interest rates using a CAS calculator',
  q('Marissa has $10 000 to invest. She chooses an account that will earn compounding interest at the rate of 4.5% per annum, compounding monthly. Use a CAS calculator to find the effective interest rate for this investment, correct to three decimal places.')
  + q('Nominal rate: ' + A('4.5') + ' &nbsp; Periods per year: ' + A('12')) + q('Effective rate: ' + A('4.594%')),
  'You try 32', q('Convert an interest rate of 12.7% per annum, compounding monthly, to an effective interest rate, correct to two decimal places.')
  + space(34, '((1 + 12.7/1200)¹² − 1) × 100 = 13.465…: 13.47%')))

P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2020 Exam 1 Q24', q('Manu invests $3000 in an account that pays interest compounding monthly.<br>The balance of his investment after <i>n</i> months, <i>B<sub>n</sub></i>, can be determined using the recurrence relation<br>' + RR('3000', '1.0048 × <i>B<sub>n</sub></i>', 'B') + '<br>The total interest earned by Manu’s investment after the first five months is closest to')
  + mc(['$57.60', '$58.02', '$72.00', '$72.69', '$87.44'], 'D', cols=5) + why('B₅ = 1.0048⁵ × 3000 = 3072.69; 3072.69 − 3000 = 72.69'), ''))
P.append(box('Exit task 2 · VCAA 2020 Exam 1 Q28', q('The nominal interest rate for a loan is 8% per annum.<br>When rounded to two decimal places, the effective interest rate for this loan is <b>not</b>')
  + mc(['8.33% per annum when interest is charged daily.', '8.32% per annum when interest is charged weekly.', '8.31% per annum when interest is charged fortnightly.', '8.30% per annum when interest is charged monthly.', '8.24% per annum when interest is charged quarterly.'], 'C', cols=1)
  + why('eff(8, 26) = 8.315… → 8.32%, not 8.31%'), ''))
P.append(box('Exit task 3 · VCAA 2017 Exam 2 Q6', q('Alex sends a bill to his customers after repairs are completed.<br>If a customer does not pay the bill by the due date, interest is charged.<br>Alex charges interest after the due date at the rate of 1.5% per month on the amount of an unpaid bill.<br>The interest on this amount will compound monthly.')
  + parts([('a', 'Alex sent Marcus a bill of $200 for repairs to his car. Marcus paid the full amount one month after the due date. How much did Marcus pay?', '1.015 × 200 = $203', 14),
           ('b', 'Alex sent Lily a bill of $428 for repairs to her car. Lily did not pay the bill by the due date. Let <i>A<sub>n</sub></i> be the amount of this bill <i>n</i> months after the due date. Write down a recurrence relation, in terms of <i>A</i><sub>0</sub>, <i>A</i><sub><i>n</i>+1</sub> and <i>A<sub>n</sub></i>, that models the amount of the bill.', 'A₀ = 428, Aₙ₊₁ = 1.015Aₙ', 16),
           ('c', 'Lily paid the full amount of her bill four months after the due date. How much interest was Lily charged? Round your answer to the nearest cent.', '1.015⁴ × 428 = 454.26; 454.26 − 428 = $26.26', 16)]), ''))
SC = ['I can convert nominal (annual) interest rates to compounding period interest rates.', 'I can use recurrence relations to model loans with different compounding periods.',
      'I can model an investment that compounds monthly using recurrence relations.', 'I can compare loans and investments using effective interest rates.', 'I can calculate effective interest rates using a CAS calculator.']
P.append(close(SC, [('7F', 'Q1–17')], ['7F']))
build('l34', '7F', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l34-worksheet', '7F worksheet'), ('l34-worksheet-solutions', '7F worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
