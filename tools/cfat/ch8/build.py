"""CONTENT for CFAT 2.8.1 (Cambridge 8A, 8B, 8C: annuity investments, reducing balance loans, amortisation tables) and
CFAT 2.8.2 (Cambridge 8E, 8H, 8I: financial solver set-up, interest-only loans, perpetuities). Output: build_html.py.

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no VCAA reprints / exam practice). Map from
tools/y12_edrolo_exercise_questions.csv: 6F->8A, 6B Q1-5/6D Q1-5->8B, 6A Q1-3/6B Q6-14/6D Q6-12->8C, 6A Q4-6->8E,
6C->8H, 6E->8I. 8D, 8F and 8G have no Edrolo exercise questions (gap, not covered).
Wording copied verbatim from Edrolo PDF pp. 365-367, 375-378, 386-387, 406-407, 417-420 (printed = pdf - 7);
subscripts typed as Unicode. Answers from the Edrolo answer pages (PDF pp. 705-712), checked by calculation.
Marks for parts set by Claude (Edrolo prints none).

CFAT 2.8.1 (14 marks, start of l40 = the lesson after 8A-8B-8C): MC Edrolo 6F Q5, 6F Q9, 6A Q1b, 6B Q6b, 6B Q6c, 6B Q11;
  SA 6F Q4a-c, 6B Q2a-c, 6B Q10 (6B Q3 dropped: 3rd page).
CFAT 2.8.2 (15 marks, start of l46 = the Chapter 8 check lesson, after 8H-8I): MC Edrolo 6A Q4, 6C Q7, 6E Q7;
  SA 6A Q5a-c, 6C Q3a-b, 6C Q4a-b, 6E Q3a-c, 6E Q4a-b.
Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')
AH = ['payment number', 'payment', 'interest', 'principal reduction', 'balance of loan']
T6B6 = [AH, ['0','0.00','0.00','0.00','94 000.00'], ['1','5600.00','455.54','5144.46','88 855.54'],
        ['2','5600.00','430.61','5169.39','83 686.15'], ['3','5600.00','405.56','5194.44','78 491.71']]
S6B6 = 'The first four lines of an amortisation table for a reducing balance loan are shown. Interest is compounded on a fortnightly basis.'

CFATS = [
 dict(id='CFAT 2.8.1', subs='8A-8B-8C', title='Annuity investments, reducing balance loans and amortisation tables',
  layout=[([0],[1]),([2],[3]),([4],[5])],
  mc=[
   dict(src='Edrolo 6F Q5', stem='The following table can be used to model the value of an annuity investment over a period of five months.',
        table=[['payment number','payment','interest','principal addition','balance of investment'],
               ['0','0.00','0.00','0.00','15 000.00'],['1','1000.00','65.00','1065.00','16 065.00'],
               ['2','1000.00','69.62','','17 134.62'],['3','1000.00','74.25','1074.25','18 208.87'],
               ['4','1000.00','78.91','1078.91','19 287.78'],['5','1000.00','83.58','1083.58','20 371.36']],
        stem2='The principal addition after the second payment is', opts=['$0.00','$1065.00','$1069.62','$1074.25'], ans=2),
   dict(src='Edrolo 6F Q9', stem='Mariana invests $55 000 in an annuity investment which earns interest at a rate of 3.9% per annum, compounding monthly. She deposits a further $450 per month.\nAfter 6 months, the value of the annuity is closest to',
        opts=['$53 359.21','$53 359.22','$58 803.28','$58 803.29'], ans=2),
   dict(src='Edrolo 6A Q1b', stem='Stephanie takes out a loan of $50 000 with her bank who doesn’t charge interest for the first three months. She makes monthly repayments of $1200 towards the loan.\nShe has set up an amortisation table to model the amortisation of her loan. There are a few cells missing.',
        table=[AH,['0','1200.00','0.00','0.00','50 000.00'],['1','1200.00','0.00','1200.00','48 800.00'],
               ['2','1200.00','0.00','1200.00','47 600.00'],['3','1200.00','','','']],
        stem2='What is the balance of Stephanie’s loan after 3 months?', opts=['$40 000','$46 400','$48 800','$50 000'], ans=1),
   dict(src='Edrolo 6B Q6b', stem=S6B6, table=T6B6, stem2='The principal reduction after payment number 2 is',
        opts=['$0.00','$5144.46','$5169.39','$5194.44'], ans=2),
   dict(src='Edrolo 6B Q6c', stem=S6B6, table=T6B6, stem2='The interest rate, per annum, is closest to',
        opts=['0.48%','1.26%','4.80%','12.60%'], ans=3),
   dict(src='Edrolo 6B Q11', stem='Jasmine takes out a loan of $560 000 to pay for her mortgage. She makes monthly repayments of $3006.20 and will pay off the loan after 30 years.\nThe annual interest rate is closest to',
        opts=['4% p.a.','5% p.a.','10% p.a.','15% p.a.'], ans=1),
  ],
  sa=[
   dict(src='Edrolo 6F Q4', stem='Phil wants to predict how much money he will have in his savings account each month. He uses the following recurrence relation to model his account balance from month to month.\nV₀ = 8000, Vₙ₊₁ = 1.0025 × Vₙ + 230',
        parts=[('a.','Calculate the annual interest rate for this annuity investment.',1,'0.0025 × 100 × 12 = 3% per annum'),
               ('b.','How much would Phil have in his savings account after two months?',1,'V₁ = 8250, V₂ = 1.0025 × 8250 + 230 = $8500.63'),
               ('c.','How many months will it take for Phil’s account balance to first reach $9000?',1,'V₃ = 8751.88, V₄ = 9003.76 → 4 months')]),
   dict(src='Edrolo 6B Q2', stem='Skyla took out a loan that can be modelled by the following recurrence relation, where Vₙ represents the value of the loan after n months.\nV₀ = 10 000, Vₙ₊₁ = 1.004 × Vₙ − 600',
        parts=[('a.','How much did Skyla borrow?',1,'$10 000'),
               ('b.','How much does Skyla pay the lender each month?',1,'$600'),
               ('c.','What is the annual interest rate of Skyla’s loan?',1,'0.004 × 100 × 12 = 4.8% p.a.')]),
   dict(src='Edrolo 6B Q10', stem='Joan has agreed to a loan of $3000 with her bank. The loan has an interest rate of 4% per annum, compounding monthly. Joan makes monthly payments of $500 towards the loan.\nFill out the amortisation table for the first three payments.',
        parts=[('','',2,'1 | 500.00 | 10.00 | 490.00 | 2510.00\n2 | 500.00 | 8.37 | 491.63 | 2018.37\n3 | 500.00 | 6.73 | 493.27 | 1525.10',
                [AH,['0','0.00','0.00','0.00','3000.00'],['1','','','',''],['2','','','',''],['3','','','','']])]),
  ]),
 dict(id='CFAT 2.8.2', subs='8E-8H-8I', title='Financial solver, interest-only loans and perpetuities',
  layout=[([0],[1]),('full',2)],
  mc=[
   dict(src='Edrolo 6A Q4', stem='Alo has established a loan of $15 000 to pay for her car.\nShe will be charged interest at a rate of 15% per annum, compounding twice a month, with repayments of $100 every half-month.\nIf she wants to know how much she still owes after one year, the value of N will be',
        opts=['1','12','24','26'], ans=2),
   dict(src='Edrolo 6C Q7', stem='What is the annual interest rate required to establish an interest-only loan of $4500, with monthly repayments of $9? Interest compounds on a monthly basis.',
        opts=['1.2% p.a.','2.0% p.a.','2.3% p.a.','2.4% p.a.'], ans=3),
   dict(src='Edrolo 6E Q7', stem='The annual interest rate required to establish a perpetuity with a balance of $64 482 and fortnightly payments of $128.96 is closest to',
        opts=['0.2% p.a.','2.0% p.a.','5.2% p.a.','6.7% p.a.'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 6A Q5', stem='In 2003, Zo opened up a savings account and put $215 into it.\nHer bank offered an interest rate of 1.5% per annum, compounding monthly. However, she has since forgotten about the account.\nIn 2023, she discovers a document that contains details about this account and finally remembers it. She wants to know how much it is worth and uses a financial solver to help her.\nIdentify the value of the following:',
        parts=[('a.','I(%)',1,'1.5'),('b.','PV',1,'−215'),('c.','PMT',1,'0')]),
   dict(src='Edrolo 6C Q3', stem='Calculate the regular repayment amount required for each of the following interest-only loans. Round to the nearest cent.',
        parts=[('a.','A $12 000 loan with 2.8% interest per month, compounding monthly. Payments are made monthly.',1,'0.028 × 12 000 = $336.00'),
               ('b.','A $22 000 loan with 14% interest per annum, compounding annually. Payments are made annually.',1,'0.14 × 22 000 = $3080.00')]),
   dict(src='Edrolo 6C Q4', stem='Terry has taken out an interest-only loan. Every month, he makes a payment of $465. The interest rate is 24% per annum and interest is compounded monthly.',
        parts=[('a.','What is the principal of the loan?',1,'r = 24 ÷ 12 = 2% per month\n465 ÷ 0.02 = $23 250'),
               ('b.','Construct a recurrence relation that can be used to model Vₙ, the value of the loan after n months.',1,'V₀ = 23 250, Vₙ₊₁ = 1.02 × Vₙ − 465')]),
   dict(src='Edrolo 6E Q3', stem='The following recurrence relation models the value of a perpetuity, Vₙ, after n months.\nV₀ = 168 429, Vₙ₊₁ = 1.005 × Vₙ − 842.15',
        parts=[('a.','How much does the investor receive each month?',1,'$842.15'),
               ('b.','Calculate the annual interest rate.',1,'0.005 × 100 × 12 = 6% p.a.'),
               ('c.','What is the value of the perpetuity after 100 months?',1,'Perpetuity: the balance never changes → $168 429')]),
   dict(src='Edrolo 6E Q4', stem='Answer the following questions without using a financial solver. Round to two decimal places where necessary.',
        parts=[('a.','A perpetuity with an initial investment of $80 000 has an interest rate of 3.5% per annum, compounding monthly. How much are the monthly payments?',1,'80 000 × 0.035 ÷ 12 = $233.33'),
               ('b.','A perpetuity with an initial investment of $250 000 has an interest rate of 2.8% per annum, compounding quarterly. How much are the quarterly payments?',1,'250 000 × 0.028 ÷ 4 = $1750.00')]),
  ]),
]
