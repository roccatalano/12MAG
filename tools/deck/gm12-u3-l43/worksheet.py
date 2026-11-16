"""Lesson gm12-u3-l43 (8G Solving harder financial problems) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). DRAFT.
Questions verbatim, same items and order as tools/deck/gm12-u3-l43/build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed): APK = VCAA 2016 Exam 2 Q6c adapted (Edrolo U1&2 3C Q19). Examples 25-26 = Cambridge U3&4 pp. 440-442.
You trys = YT-8G-25 (planner/written-youtrys.json) and Edrolo U3&4 6B WE3. Exit = VCAA 2016 Exam 2 Q7b (Edrolo U3&4 6B Q22).
Output: lessons/8G worksheet(.html/.pdf) + solutions.   Run: python3 tools/deck/gm12-u3-l43/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
def fs(N, I, PV, PMT, FV, P): return f'N = {N}, I = {I}, PV = {PV}, PMT = {PMT}, FV = {FV}, PpY = CpY = {P}'
def solver(v=None):
    v = v or ['', '', '', '', '', '', '']
    return table([['N', 'I(%)', 'PV', 'PMT', 'FV', 'PpY', 'CpY'], [a(x) for x in v]], style='width:100%;font-size:9pt')

P = [title('8G', 'Solving harder financial problems')]
P.append(lis(['To be able to find the value of an investment when the regular payment changes.',
              'To be able to analyse the impact of a change in the interest rate on a reducing balance loan, an annuity and an investment.']))
P.append(sect('Activating prior knowledge', 'Year 11 exam question'))
P.append(box('Question 1 · VCAA 2016 Exam 2 Q6c (adapted)', q('Anton is a musician, and he purchases a minivan for $64 000 to transport equipment. After four years, the value of the minivan is $40 000. The minivan travelled an average of 8000 km in each of the four years since it was purchased. Assume that the value of the minivan has been depreciated using the unit cost method of depreciation.')
  + q('By how much is the value of the minivan reduced per kilometre travelled? (1 mark)')
  + space(14, '(64 000 − 40 000) ÷ (4 × 8000) = 24 000 ÷ 32 000 = $0.75 per km'), ''))

P.append(sect('8G Changing the regular payment', 'Example, then you try'))
P.append(exyt('Example 25 · Finding the value of an investment when the regular payment changes',
  q('Derek invests $50 000 into a compound interest investment paying 6.1% per annum, compounding annually. Derek invests an additional $8000 per year immediately after interest is calculated.')
  + q('After five years, Derek increases his additional investment to $10 000 per year. Calculate the value of Derek’s investment after twelve years (in total).')
  + q('Stage 1') + solver(['5', '6.1', '−50 000', '−8000', '112 414.364…', '1', '1'])
  + q('Stage 2') + solver(['7', '6.1', '−112 414.364…', '−10 000', '254 343.797…', '1', '1'])
  + space(8, 'The value of Derek’s investment is $254 343.80'),
  'You try 1', q('Ella invests $40 000 into a compound interest investment paying 5.4% per annum, compounding annually. Ella invests an additional $6000 per year immediately after interest is calculated. After four years, Ella increases her additional investment to $9000 per year. Calculate the value of Ella’s investment after ten years (in total).')
  + space(52, fs(4, 5.4, '−40 000', '−6000', '?', 1) + ' → FV = 75 380.303…<br>' + fs(6, 5.4, '−75 380.303…', '−9000', '?', 1) + ' → FV = 165 184.474…<br>After ten years: $165 184.47')))

P.append(sect('8G Changing the interest rate', 'Example, then you try'))
P.append(exyt('Example 26 · Finding the final payment of a reducing balance loan when the interest rate changes',
  q('Adrian borrows $150 000 for 25 years at an interest rate of 6.8% per annum, compounding monthly. For the first three years, Adrian repays $1041.11 each month.')
  + q('After 3 years, the interest rate rises to 7.2% per annum. Adrian still wishes to pay off the loan in 25 years so makes 263 monthly payments of $1076.18 followed by a final payment.')
  + q('Calculate the final payment to ensure the loan is fully repaid at the end of 25 years. Round your answer to the nearest cent.')
  + q('Stage 1') + solver(['36', '6.8', '150 000', '−1041.11', '−142 391.835…', '12', '12'])
  + q('Stage 2') + solver(['264', '7.2', '142 391.835…', '−1076.18', '0.1173…', '12', '12'])
  + space(8, 'FV = +0.12 (overpaid): final payment = 1076.18 − 0.12 = $1076.06'),
  'You try 2', q('Cilian takes out a reducing balance loan of $35 000 with a bank that charges an interest rate of 5.9% per annum, compounding monthly. He makes a payment of $1000 each month to pay off the loan.')
  + parts([('a', 'How much does Cilian still owe after 21 months?', fs(21, 5.9, '35 000', '−1000', '?', 12) + '<br>FV = −16 731.708…: $16 731.71', 14),
           ('b', 'The bank changes the interest rate for Cilian’s loan after 21 months to 6.4% per annum compounding monthly. Cilian’s monthly payments remain unchanged. To ensure the loan is fully repaid, the final repayment will be lower. If Cilian manages to pay off the rest of the loan, how much interest will he pay in total? Use the rounded value found in part a.',
            'N = 17.57… → 17 payments of $1000 + 1 final; after 17: owes 570.161…; final = $573.20<br>Total paid = 21 × 1000 + 17 × 1000 + 573.20 = 38 573.20; interest = 38 573.20 − 35 000 = $3573.20', 30)])))

P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 2 Q7b', q('Ken has borrowed $70 000 to buy a new caravan. He will be charged interest at a rate of 6.9% per annum, compounding monthly. Ken will make monthly repayments of $800.')
  + q('After three years, Ken will make a lump sum payment of $<i>L</i> in order to reduce the balance of his loan. This lump sum payment will ensure that Ken’s loan is fully repaid in a further three years. Ken’s repayment amount and interest remains the same.')
  + q('What is the value of Ken’s lump sum payment, $<i>L</i>? Round to the nearest dollar. (2 marks)')
  + space(24, fs(36, 6.9, '70 000', '−800', '?', 12) + ' → FV = −54 151.599…<br>' + fs(36, 6.9, '?', '−800', '0', 12) + ' → PV = 25 947.576…<br><i>L</i> = 54 151.599… − 25 947.576… = 28 204.02… ≈ $28 204'), ''))
SC = ['I can find the value of an investment when the regular payment changes.',
      'I can analyse the impact of a change in the interest rate on a reducing balance loan, an annuity and an investment.']
P.append(close(SC, [('8G', 'Q1–14')], ['8G']))
build('l43', '8G', 'AoS 2 · Recursion and financial modelling', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l43-worksheet', '8G worksheet'), ('l43-worksheet-solutions', '8G worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
