"""Lesson gm12-u3-l39 (8C Amortisation tables) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/8C slides.html     Run: python3 tools/deck/gm12-u3-l39/build.py     Screenshots: python3 tools/deck/gm12-u3-l39/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- No CFAT this lesson (CFAT 2.8.1 sits at the start of l40).
- Do Now: VCAA 2026 NHT Exam 1 Q22 (answer C; NHT report: answers only) · VCAA 2026 Exam 1 Q4 (B) ·
          VCAA 2026 Exam 2 Q10 stem + Q10a (no: differences 950, 953.80 …) · VCAA 2026 Exam 2 Q3 stem + Q3b (320). 2026 reports not yet published: no %.
- APK: Cambridge U1&2 Ch 3 skills checklist 3E #11 (skill + its example) ·
       VCAA 2021 Exam 2 Q7 stem + Q7a (= Edrolo U1&2 3C Q18; report 54% scored the mark; answer 28 800).
- Learn: Cambridge U3&4 8C pp. 407-411 (own words) · Edrolo U3&4 6A, 6B, 6F.
- Worked examples: Cambridge U3&4 Examples 10-14 (8C, pp. 408-411).
  You trys (planner card): Ex 10 = Edrolo U3&4 6A WE1 (p. 355) · Ex 11 = written YT-8C-11 (planner/written-youtrys.json) ·
  Ex 12 = Edrolo 6B WE2 (pp. 364-365; Edrolo's step 1 prints 490 465.13 for 495 465.13, answer unaffected) · Ex 13 = written YT-8C-13 · Ex 14 = Edrolo 6F WE2 (pp. 406-407).
- CAS: none on the card (tables are by hand this lesson).
- Exits: VCAA 2016 Further Exam 1 Q22 (Edrolo U3&4 6B Q19; report 54% B; 9/54/19/7/10) ·
         VCAA 2017 Further Exam 1 Q23 (Edrolo U3&4 6F Q18; report 38% D; 3/35/15/38/7).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
def _card(o,i):
    if isinstance(o,dict):
        if o.get('id')==i: return o['card']
        for v in o.values():
            r=_card(v,i)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=_card(v,i)
            if r: return r
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l39')
yid=lambda u:u.split('v=')[1].split('&')[0]
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
VN='<i>V<sub>n</sub></i>'
def B(cls,val,ph='&nbsp;'): return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
HL=['Payment number','Payment','Interest','Principal reduction','Balance']
HI=['Payment number','Payment','Interest','Principal increase','Balance']
def AT(rows,head=HL,fs=17,w=''):
    st=f'border-collapse:collapse;font-size:{fs}px;margin:8px 0;{w}'
    th=''.join(f'<th style="border:1.5px solid #556;padding:3px 8px;background:#e8eef9;font-size:{fs-2}px;line-height:1.15">{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:3px 10px;text-align:{"center" if j==0 else "right"};white-space:nowrap">{c}</td>' for j,c in enumerate(r))+'</tr>' for r in rows)
    return f'<table style="{st}"><tr>{th}</tr>{tr}</table>'
def ATW(rows,head=HL,fs=16): return AT(rows,head,fs,'background:#fff;color:#111')

S=[]
S.append(title(39,'Amortisation tables',f'{CAM} · 8C Amortisation tables','L39').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('8C The amortisation process','',None),('Worked examples 10–12','→ You try',None),('8C Annuity tables','',None),('Worked example 13','→ You try',None),
  ('8C Investments with additions','',None),('Worked example 14','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Amortisation table','a table that shows, payment by payment, the payment, the interest, the principal reduction and the balance'),
  ('Principal reduction','the part of a payment that actually reduces the balance (payment − interest)'),
  ('Payment 0 line','the starting balance (the principal), before any payment is made'),
  ('Principal increase','investment with additions: interest + payment, added to the balance')],
  [('Interest',F('<i>r</i>/(100 × <i>p</i>) × previous balance'),'rate per period × previous balance'),
   ('Principal reduction',F('payment − interest'),'loans and annuities'),
   ('New balance',F('previous balance − principal reduction'),'investment: + principal increase'),
   ('Rate per period',F('interest ÷ previous balance × 100'),'× <i>p</i> for the annual rate')],
  f'{CAM}, 8C pp. 407–411; Study Design: use of a table to investigate and analyse the amortisation of a reducing balance loan and of an annuity'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 NHT Exam 1 Q22','Review of 8B (last lesson)',
  '<div style="font-size:26px;margin-top:50px">Cath invests $400 000 in an annuity from which she receives a regular monthly payment of $4021.35<br>The interest rate for this annuity is 3.85% per annum, compounding monthly.<br>Within the first five months, which one of the following is not a monthly balance of the annuity, rounded to the nearest dollar?</div>',
  [('R','<i>R</i> = 1 + 3.85/1200 = 1.003208…'),('Iterate','× <i>R</i> − 4021.35, five times'),('Balances','397 262 · 394 515 · 391 760 · 388 995 · 386 222')],
  '$391 762 is <b>not</b> a balance (it is $391 760): <b>C</b>.','VCAA 2026 (NHT) General Mathematics Exam 1 Q22 (NHT report gives answers only)',
  stat=('nht',),mc=['$397 262','$394 515','$391 762','$388 995'],key='C'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q4','Review of 1F (last term)',
  '<div style="font-size:22px;margin-top:10px">A random sample of 100 whole numbers was generated for a class exercise.<br>For this sample, Jasmine calculated a mean value of 5.00<br>For the same sample, Tina calculated a mean value of 5.05<br>Tina entered all 100 values correctly into her calculator.<br>Jasmine incorrectly entered one of the 100 values into her calculator.<br>Instead of entering the correct value of 8, what number did Jasmine incorrectly enter?</div>',
  [('Totals','Tina: 100 × 5.05 = 505 · Jasmine: 100 × 5.00 = 500'),('Short by','505 − 500 = 5'),('Entered','8 − 5 = 3')],
  'Jasmine entered <b>3</b>: <b>B</b>.','VCAA 2026 General Mathematics Exam 1 Q4 (2026 examiner report not yet published: no %)',
  mc=['2','3','4','5'],key='B'))
PTS=[(0,250000.00),(1,249050.00),(2,248096.20),(3,247138.58),(4,246177.14)]
def gfig():
    W,Hh,L,T=640,250,90,20; x=lambda m:L+m*95; y=lambda v:T+(250100-v)/4200*190
    s=f'<svg viewBox="0 0 {W} {Hh}" width="{W}" style="display:block;margin:auto"><line x1="{L}" y1="{T-10}" x2="{L}" y2="{T+205}" stroke="#333" stroke-width="2"/><line x1="{L}" y1="{T+205}" x2="{W-20}" y2="{T+205}" stroke="#333" stroke-width="2"/>'
    s+=f'<text x="{L-8}" y="{T-2}" font-size="15" text-anchor="end">value ($)</text><text x="{W-20}" y="{T+228}" font-size="15" text-anchor="end">month</text>'
    for m,v in PTS: s+=f'<circle cx="{x(m)}" cy="{y(v)}" r="6" fill="#1f4fb0"/><text x="{x(m)+8}" y="{y(v)-10}" font-size="14">({m}, {format(v,",.2f").replace(","," ")})</text>'
    return s+'</svg>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 Exam 2 Q10a','Review of 8B (last lesson)',
  ('<div style="font-size:20px">Hunter receives a regular monthly payment of $1950 from an annuity.<br>The month-to-month value of the annuity, <i>A<sub>n</sub></i>, in dollars, can be described by a recurrence relation.<br>The graph below shows the initial value and the value after each of the first four months, rounded to the nearest cent.</div>',
   gfig(),'<div style="font-size:20px">a. Do the points on the graph above lie on a straight line? <b>Explain</b> your answer using mathematical calculations. <span class="muted">(1 mark)</span></div>'),
  [('Differences','250 000 − 249 050 = 950 · 249 050 − 248 096.20 = 953.80'),('Compare','950 ≠ 953.80: the drop is not the same each month')],
  '<b>No.</b> The value falls by $950 in month 1 but by $953.80 in month 2, so the points do not lie on a straight line.','VCAA 2026 General Mathematics Exam 2 Q10 stem and Q10a (2026 examiner report not yet published: no %)',
  cmd=('Explain',None,'calculations: compare the differences')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q3b','Review of 1H (last term)',
  '<div style="font-size:26px;margin-top:50px">The happiness level scores for a group of 2000 students are collected as a data set. The data set is modelled by a normal distribution with a mean of 72 and a standard deviation of 8.0<br><br>b. Using the 68−95−99.7% rule, <b>find</b> the expected number of students in this group with a happiness level score below 64. <span class="muted">(1 mark)</span></div>',
  [('z','64 = 72 − 8 → one standard deviation below the mean'),('%','below <i>z</i> = −1: 16%'),('Number','16% × 2000 = 320')],
  '<b>320</b> students','VCAA 2026 General Mathematics Exam 2 Q3 stem and Q3b (2026 examiner report not yet published: no %)',
  cmd=('find',None,'percentage, then × 2000')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3E #11','The amount of simple interest each year',
  '<div style="font-size:30px;margin-top:60px">I can find the amount of simple interest each year.<br><br>An investment of $2200 pays interest at the rate of 5% per annum in the form of simple interest. <b>Find</b> the amount of interest paid each year.</div>',
  [('Rate','5% = 5/100'),('Interest','5/100 × 2200 = 110')],
  'The interest paid each year is <b>$110</b>.',f'{CAM12} · Ch 3 skills checklist 3E #11',cmd=('Find',None,'rate × principal')))
S.append(qslide('apk','APK · VCAA 2021 Exam 2 Q7a','Per-unit amounts from a recurrence relation',
  '<div style="font-size:27px;margin-top:40px">Sienna owns a coffee shop.<br>A coffee machine, purchased for $12 000, is depreciated in value using the unit cost method.<br>The rate of depreciation is $0.05 per cup of coffee made.<br>The recurrence relation that models the year-to-year value, in dollars, of the coffee machine is<br><br>&nbsp; &nbsp; <i>M</i><sub>0</sub> = 12 000, &nbsp; <i>M</i><sub><i>n</i> + 1</sub> = <i>M<sub>n</sub></i> – 1440<br><br>a. <b>Calculate</b> the number of cups of coffee that the machine produces per year. <span class="muted">(1 mark)</span></div>',
  [('Per year','the value drops $1440 each year'),('Cups','1440 ÷ 0.05 = 28 800')],
  'The machine makes <b>28 800</b> cups of coffee per year.',f'VCAA 2021 Further Mathematics Exam 2 Core Q7 stem and Q7a (examiner report) · {EDR12} 3C Q18',
  stat=('mark',54),cmd=('Calculate',None,'yearly drop ÷ cost per cup')))

# ================= Learn 1
S.append(learn('Learn · 8C','The amortisation process',
  '<h4>Each payment: add interest, pay interest, reduce the principal</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><b>Interest</b> = <i>r</i>/(100<i>p</i>) × previous balance</li><li><b>Principal reduction</b> = payment − interest</li>'
  '<li><b>New balance</b> = previous balance − principal reduction</li><li>row 0 shows only the starting balance; round every cell to the cent</li></ul>',
  '<div style="font-size:22px;text-align:center;line-height:1.7"><span class="frag">Alyssa: $1000 at 15% p.a. monthly, pays $250 a month</span><br>'
  '<span class="frag">Interest = 15/1200 × 1000 = $12.50</span><br><span class="frag">Principal reduction = 250 − 12.50 = $237.50</span><br>'
  '<span class="frag">New balance = 1000 − 237.50 = <b>$762.50</b></span></div>',
  'Only the principal reduction lowers the balance, not the whole payment.',f'{CAM}, 8C pp. 407–409 (own words) · {EDR}, 6A, 6B',
  cards=(kcard('Interest','<i>r</i>/(100<i>p</i>) × previous balance'),kcard('Principal reduction','payment − interest'))))
S.append(qslide('we','Worked example 10 · 8C','Applying the amortisation process',
  '<div style="font-size:21px">Flora borrows $20 000 at an interest rate of 8% per annum, compounding annually. She makes annual payments of $2500.</div>'
  +plist([('a','State the principal of the loan.'),('b','Calculate the initial interest charged on the principal.'),('c','Determine the impact of the first annual payment to find the principal reduction.'),('d','Calculate the new balance.'),('e','Complete the row in the table below with your calculations.'+AT([['1','2500.00','','','']],fs=15))]),
  [],'',f'{CAM} · Example 10 (p. 408)',video='Cambridge GO · Example 10 (8C Resources)',cmd=('Calculate',None,'interest → reduction → balance'),
  parts=[('a','The principal is <b>$20 000</b>.'),('b','Interest = 8% of $20 000 = <b>$1600</b>'),('c','Principal reduction = 2500 − 1600 = <b>$900</b>'),('d','New balance = 20 000 − 900 = <b>$19 100</b>'),
         ('e',ATW([['1','2500.00','1600.00','900.00','19 100.00']],fs=15))]))
S.append(qslide('yt','You try · Edrolo 6A WE1','Reading an interest-free loan table',
  '<div style="font-size:20px">Ella has borrowed $10 000 from her parents to pay for a trip to Europe.<br>They have decided not to charge interest on the loan and Ella will make equal weekly repayments once she gets back from her trip.<br>The first five lines of the amortisation table for this loan is shown.<br>The loan balance for the third week is missing.</div>'
  +AT([['0','0.00','0.00','0.00','10 000.00'],['1','150.00','0.00','150.00','9850.00'],['2','150.00','0.00','150.00','9700.00'],['3','150.00','0.00','150.00',''],['4','150.00','0.00','150.00','9400.00']],HL[:4]+['Balance of loan'],fs=16)
  +plist([('a','How much is Ella paying each week?'),('b','Calculate the loan balance after the third repayment.')]),
  [],'',f'{EDR} · 6A Worked example 1 (p. 355)',cmd=('Calculate',None,'previous balance − principal reduction'),
  parts=[('a','The repayments are <b>$150</b> each week.'),('b','9700.00 − 150.00 = <b>$9550</b>')]))
# Example 11: template table filled row by row
def tmpl(pre,rows,head=HL):
    out=[]
    for r,row in enumerate(rows):
        out.append([row[0]]+[c if isinstance(c,str) else B(f'{pre}{r}',c[0]) for c in row[1:]])
    return ATW(out,head,15)
E11=[['0','0.00','0.00','0.00','20 000.00'],['1',('2500.00',),('1600.00',),('900.00',),('19 100.00',)],['2',('2500.00',),('1528.00',),('972.00',),('18 128.00',)],['3',('2500.00',),('1450.24',),('1049.76',),('17 078.24',)]]
S.append(qslide('we','Worked example 11 · 8C','Constructing an amortisation table for a reducing balance loan',
  '<div style="font-size:27px;margin-top:50px">Flora borrows $20 000 at an interest rate of 8% per annum, compounding annually. She makes annual payments of $2500.<br><br><b>Construct</b> an amortisation table for Flora’s reducing balance loan for the first three payments.</div>',
  [('Payment 1','8% × 20 000 = 1600 · 2500 − 1600 = 900 · 20 000 − 900 = 19 100','data-fill="e111"'),
   ('Payment 2','8% × 19 100 = 1528 · 2500 − 1528 = 972 · 19 100 − 972 = 18 128','data-fill="e112"'),
   ('Payment 3','8% × 18 128 = 1450.24 · 2500 − 1450.24 = 1049.76 · 18 128 − 1049.76 = 17 078.24','data-fill="e113"'),
   ('TMPL',tmpl('e11',E11))],
  '',f'{CAM} · Example 11 (p. 409)',video='Cambridge GO · Example 11 (8C Resources)',cmd=('Construct',None,'one row per payment')))
Y11=[['0','0.00','0.00','0.00','12 000.00'],['1',('3000.00',),('720.00',),('2280.00',),('9720.00',)],['2',('3000.00',),('583.20',),('2416.80',),('7303.20',)],['3',('3000.00',),('438.19',),('2561.81',),('4741.39',)]]
S.append(qslide('yt','You try · written for 12MAG (YT-8C-11)','Constructing a loan table',
  '<div style="font-size:27px;margin-top:50px">Sam borrows $12 000 at an interest rate of 6% per annum, compounding annually. He makes annual payments of $3000.<br><br><b>Construct</b> an amortisation table for Sam’s reducing balance loan for the first three payments.</div>',
  [('Payment 1','6% × 12 000 = 720 · 3000 − 720 = 2280 · 12 000 − 2280 = 9720','data-fill="y111"'),
   ('Payment 2','6% × 9720 = 583.20 · 3000 − 583.20 = 2416.80 · 9720 − 2416.80 = 7303.20','data-fill="y112"'),
   ('Payment 3','6% × 7303.20 = 438.19 · 3000 − 438.19 = 2561.81 · 7303.20 − 2561.81 = 4741.39','data-fill="y113"'),
   ('TMPL',tmpl('y11',Y11))],
  '','Written for 12MAG (modelled on Cambridge Example 11) · planner/written-youtrys.json',cmd=('Construct',None,'one row per payment')))
S.append(qslide('we','Worked example 12 · 8C','Analysing an amortisation table for a reducing balance loan',
  '<div style="font-size:19px">A business borrows $10 000 at a rate of 8% per annum, compounding quarterly. The loan is to be repaid by making quarterly payments of $2700.00. The amortisation table for this loan is shown below.</div>'
  +AT([['0','0.00','0.00','0.00','10 000.00'],['1','2700.00','','2500.00','7500.00'],['2','2700.00','150.00','','4950.00'],['3','2700.00','99.00','2601.00','']],fs=15)
  +plist([('a','Calculate the interest paid on the initial balance.'),('b','Calculate the principal reduction from the second payment.'),('c','Calculate the balance of the loan after payment 3 has been made.')]),
  [],'',f'{CAM} · Example 12 (pp. 409–410)',video='Cambridge GO · Example 12 (8C Resources)',cmd=('Calculate',None,'use the three rules'),
  parts=[('a','8/(100 × 4) × 10 000 = <b>$200</b> &nbsp;(or 2700 − 2500)'),('b','2700.00 − 150.00 = <b>$2550.00</b>'),('c','4950 − 2601 = <b>$2349</b>')]))
S.append(qslide('yt','You try · Edrolo 6B WE2','Missing cells in a loan table',
  '<div style="font-size:18px">The first four lines of an amortisation table for a reducing balance loan of $500 000 are shown. Interest is charged at a rate of 6.2% per annum, compounding quarterly. The loan is to be repaid with quarterly payments. There are a number of cells missing.</div>'
  +AT([['0','0.00','0.00','0.00','500 000.00'],['1','10 000.00','7750.00','2250.00','497 750.00'],['2','a.','7715.13','2284.87','495 465.13'],['3','10 000.00','b.','c.','d.']],HL[:4]+['Balance of loan'],fs=15)
  +plist([('a','Calculate the missing payment value for payment number 2.'),('b','Calculate the missing interest for payment number 3.'),('c','Calculate the missing principal reduction for payment number 3.'),('d','Calculate the missing loan balance after payment number 3.')]),
  [],'',f'{EDR} · 6B Worked example 2 (pp. 364–365)',cmd=('Calculate',None,'use the three rules'),
  parts=[('a','7715.13 + 2284.87 = <b>$10 000.00</b>'),('b','6.2/400 × 495 465.13 ≈ <b>$7679.71</b>'),('c','10 000.00 − 7679.71 = <b>$2320.29</b>'),('d','495 465.13 − 2320.29 = <b>$493 144.84</b>')]))

# ================= Learn 2
S.append(learn('Learn · 8C','Amortisation tables for annuities',
  '<h4>Same columns, same rules: the payment comes to you</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>the balance is what is left in the annuity</li><li><b>rate per period</b> = interest ÷ previous balance × 100</li>'
  '<li><b>annual rate</b> = rate per period × <i>p</i></li></ul>',
  '<div style="font-size:22px;text-align:center;line-height:1.7"><span class="frag">Row 1: interest $60 on a balance of $12 000</span><br>'
  '<span class="frag">60 ÷ 12 000 × 100 = 0.5% per month</span><br><span class="frag">0.5 × 12 = <b>6% per annum</b></span></div>',
  'Use the first row: the interest there is on the principal.',f'{CAM}, 8C p. 410 (own words) · {EDR}, 6D',
  cards=(kcard('Rate per period','interest ÷ previous balance × 100'),)))
S.append(qslide('we','Worked example 13 · 8C','Analysing an amortisation table for an annuity to find the interest rate',
  '<div style="font-size:20px">Consider the following amortisation table for an annuity after 3 monthly payments.</div>'
  +AT([['0','0.00','0.00','0.00','12 000.00'],['1','2200.00','60.00','2140.00','9860.00'],['2','2200.00','49.30','2150.70','7709.30'],['3','2200.00','A','B','5547.85']],fs=16)
  +plist([('a','State the principal of the annuity and the amount of interest paid in the first month.'),('b','Calculate the monthly interest rate.'),('c','Find the value of A and B.')]),
  [],'',f'{CAM} · Example 13 (p. 410)',video='Cambridge GO · Example 13 (8C Resources)',cmd=('Calculate',None,'interest ÷ principal × 100'),
  parts=[('a','Principal: <b>$12 000</b>, interest: <b>$60</b>'),('b','60 ÷ 12 000 × 100 = <b>0.5% per month</b>'),('c','A = 0.5/100 × 7709.30 = <b>38.55</b> · B = 2200 − 38.55 = <b>2161.45</b>')]))
S.append(qslide('yt','You try · written for 12MAG (YT-8C-13)','Finding the rate of an annuity',
  '<div style="font-size:20px">Consider the following amortisation table for an annuity after 3 monthly payments.</div>'
  +AT([['0','0.00','0.00','0.00','8000.00'],['1','1500.00','40.00','1460.00','6540.00'],['2','1500.00','32.70','1467.30','5072.70'],['3','1500.00','A','B','3598.06']],fs=16)
  +plist([('a','Find the annual interest rate for this annuity.'),('b','Find the values of A and B.')]),
  [],'','Written for 12MAG (modelled on Cambridge Example 13) · planner/written-youtrys.json',cmd=('Find',None,'monthly rate, then × 12'),
  parts=[('a','40 ÷ 8000 × 100 = 0.5% per month → 0.5 × 12 = <b>6% per annum</b>'),('b','A = 0.005 × 5072.70 = <b>$25.36</b> · B = 1500 − 25.36 = <b>$1474.64</b>')]))

# ================= Learn 3
S.append(learn('Learn · 8C','Investments with additions to the principal',
  '<h4>The payment goes IN, so the balance grows</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><b>Interest</b> = rate per period × previous balance</li><li><b>Principal increase</b> = payment + interest</li>'
  '<li><b>New balance</b> = previous balance + principal increase</li></ul>',
  '<div style="font-size:22px;text-align:center;line-height:1.7"><span class="frag">$1359.40 at 0.25% per month, + $50 a month</span><br>'
  '<span class="frag">Interest = 0.25% × 1359.40 = $3.40</span><br><span class="frag">Increase = 3.40 + 50 = $53.40</span><br>'
  '<span class="frag">New balance = <b>$1412.80</b></span></div>',
  'Loan or annuity: subtract. Investment with additions: add.',f'{CAM}, 8C p. 411 (own words) · {EDR}, 6F',
  cards=(kcard('Principal increase','payment + interest'),)))
E14=[['4',('50.00',),('3.40',),('53.40',),('1412.80',)],['5',('50.00',),('3.53',),('53.53',),('1466.33',)]]
S.append(qslide('we','Worked example 14 · 8C','Interpreting and constructing an amortisation table for a compound interest investment',
  '<div style="font-size:21px">Consider the following amortisation table for a compound interest investment with monthly additions to the principal. Assume that interest compounds monthly.</div>'
  +AT([['0','0.00','0.00','0.00','1200.00'],['1','50.00','3.00','53.00','1253.00'],['2','50.00','3.13','53.13','1306.13'],['3','50.00','3.27','53.27','1359.40']],HI,fs=16)
  +'<div style="font-size:21px"><b>Complete</b> two additional lines for the table corresponding to payment 4 and payment 5.</div>',
  [('Rate','3 ÷ 1200 × 100 = 0.25% per month'),
   ('Payment 4','0.25% × 1359.40 = 3.40 · 3.40 + 50 = 53.40 · 1359.40 + 53.40 = 1412.80','data-fill="e140"'),
   ('Payment 5','0.25% × 1412.80 = 3.53 · 3.53 + 50 = 53.53 · 1412.80 + 53.53 = 1466.33','data-fill="e141"'),
   ('TMPL',tmpl('e14',E14,HI))],
  '',f'{CAM} · Example 14 (p. 411)',video='Cambridge GO · Example 14 (8C Resources)',cmd=('Complete',None,'rate first, then two rows')))
S.append(qslide('yt','You try · Edrolo 6F WE2','Missing cells in an investment table',
  '<div style="font-size:18px">The table shown represents an annuity investment with an initial deposit of $5000 and an interest rate of 5.2% per annum, compounding quarterly. Regular deposits of $200 are made at the end of each quarter. There are a few cells missing.</div>'
  +AT([['0','0.00','0.00','0.00','5000.00'],['1','a.','65.00','265.00','5265.00'],['2','200.00','68.45','b.','5533.45'],['3','200.00','71.93','271.93','c.'],['4','200.00','d.','275.47','6080.85']],['Payment number','Payment','Interest','Principal addition','Balance of investment'],fs=15)
  
  +plist([('a','Determine the missing payment for payment number 1.'),('b','Calculate the missing principal addition for payment number 2.'),('c','Calculate the missing investment balance after payment number 3.'),('d','Calculate the missing interest for payment number 4.')]),
  [],'',f'{EDR} · 6F Worked example 2 (pp. 406–407)',cmd=('Calculate',None,'addition = payment + interest'),
  parts=[('a','Deposits are $200 each quarter: <b>$200</b>'),('b','200.00 + 68.45 = <b>$268.45</b>'),('c','5533.45 + 271.93 = <b>$5805.38</b>'),('d','5.2/400 × 5805.38 = 75.469… ≈ <b>$75.47</b>')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2016 Exam 1 Q22','Show what you know',
  '<div style="font-size:21px">The first three lines of an amortisation table for a reducing balance home loan are shown below.<br>The interest rate for this home loan is 4.8% per annum compounding monthly.<br>The loan is to be repaid with monthly payments of $1500.</div>'
  +AT([['0','0','0.00','0.00','250 000.00'],['1','1500','1000.00','500.00','249 500.00'],['2','1500','','','']],HL[:4]+['Balance of loan'],fs=16)
  +'<div style="font-size:21px">The amount of payment number 2 that goes towards reducing the principal of the loan is</div>',
  [('Interest','4.8/1200 × 249 500 = 998'),('Reduction','1500 − 998 = 502')],
  '<b>$502</b>: <b>B</b>.',f'VCAA 2016 Further Mathematics Exam 1 Recursion and financial modelling Q22 (examiner report) · {EDR} 6B Q19',
  stat=('mc',54),mc=['$486','$502','$504','$996','$998'],key='B',dist=[9,54,19,7,10],dis=('E','$998 is the INTEREST part of payment 2, not the principal reduction')))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2017 Exam 1 Q23','Show what you know',
  '<div style="font-size:21px">Four lines of an amortisation table for an annuity investment are shown below.<br>The interest rate for this investment remains constant, but the payment value may vary.</div>'
  +AT([['17','100.00','27.40','127.40','6977.50'],['18','100.00','27.91','127.91','7105.41'],['19','100.00','28.42','128.42','7233.83'],['20','','','','7500.00']],['Payment number','Payment','Interest','Principal addition','Balance of investment'],fs=16)
  +'<div style="font-size:21px">The balance of the investment after payment number 20 is $7500.<br>The value of payment number 20 is closest to</div>',
  [('Rate','28.42 ÷ 7105.41 × 100 = 0.4% per payment'),('Interest','0.004 × 7233.83 = 28.94'),('Addition','7500 − 7233.83 = 266.17'),('Payment','266.17 − 28.94 = 237.23')],
  '≈ <b>$237</b>: <b>D</b>.',f'VCAA 2017 Further Mathematics Exam 1 Recursion and financial modelling Q23 (examiner report) · {EDR} 6F Q18',
  stat=('mc',38),mc=['$29','$100','$135','$237','$295'],key='D',dist=[3,35,15,38,7],dis=('B','the payment is NOT always $100: the question says it may vary')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8C' and v.get('url')]))
n=assemble(S,'12MAG · L39 · Amortisation tables',os.path.join(ROOT,'lessons','8C slides.html'))
print(n-1,'slides')
