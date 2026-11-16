"""Lesson gm12-u3-l41 (8E Using a finance solver to find the balance and final payment) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8E slides.html     Run: python3 tools/deck/gm12-u3-l41/build.py     Screenshots: python3 tools/deck/gm12-u3-l41/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2026 Exam 1 Q22 (B: I = 2170/620 000 x 1200 = 4.2%, N = 216 months = 18 years) · VCAA 2026 Exam 1 Q9 (C: CAS regression
          points against = 371.33 - 0.666 x points for; 7 positive residuals) · VCAA 2026 NHT Exam 2 Q6 stem + Q6a ($42 500; NHT report: answers only) ·
          VCAA 2026 Exam 2 Q5 stem + Q5a (line drawn through (0, 4.36) and (250 000, 8.21); scatterplot cropped from p. 8). 2026 reports not yet published: no %.
- APK: Cambridge U1&2 Ch 3 skills checklist 3I #25 (skill + its example; V15 = 1.06^15 x 250 000) ·
       Edrolo U1&2 3B Q16 = adapted (by Edrolo) from VCAA 2020 Exam 1 Recursion Q21 (85%, index y11_edrolo_exam_practice.csv).
- Learn: Cambridge U3&4 8E pp. 422-428 (own words: sign convention boxes) · Edrolo U3&4 6A.
- CAS (card casYouTry): Edrolo U3&4 6A Worked example 2 (p. 356-357); steps from planner/cas-skills.json 'finance-solver'.
- Worked examples: Cambridge U3&4 Examples 18-20 (8E, pp. 425-429).
  You trys (planner card): Ex 18 = Edrolo U3&4 6F WE3a (p. 409) · Ex 19 = Edrolo 6B WE3a (p. 366) · Ex 20 = Edrolo 6D WE3a (pp. 385-386).
- Exits: VCAA 2021 Exam 1 Q19 (Edrolo U3&4 6D Q19; 2021 E1 report 44% B; 24/44/10/15/6) ·
         VCAA 2021 Exam 2 Q8b (Edrolo U3&4 6B Q21; 2021 E2 report 27% scored the mark; answer (1.001 - 1) x 26 x 100).
"""
import os, sys, json, base64
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l41')
yid=lambda u:u.split('v=')[1].split('&')[0]
def AT(rows,head,fs=16,w=''):
    st=f'border-collapse:collapse;font-size:{fs}px;margin:8px 0;{w}'
    th=''.join(f'<th style="border:1.5px solid #556;padding:3px 8px;background:#e8eef9;font-size:{fs-2}px;line-height:1.15">{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:2px 10px;text-align:{"center" if j==0 else "right"};white-space:nowrap">{c}</td>' for j,c in enumerate(r))+'</tr>' for r in rows)
    return f'<table style="{st}"><tr>{th}</tr>{tr}</table>'
def img(p,w):
    b=base64.b64encode(open(os.path.join(H,'img',p),'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w}px;max-width:100%;display:block;margin:auto;background:#fff">'
def FS(N,I,PV,PMT,FV,P,solve='FV'):
    """finance solver entries as one compact line; the unknown is shown as ?"""
    d=dict(N=N,I=I,PV=PV,PMT=PMT,FV=FV)
    return ' · '.join(f'{k} = <b>?</b>' if k==solve else f'{k} = {v}' for k,v in d.items())+f' · PpY = CpY = {P}'

S=[]
S.append(title(41,'Using a finance solver to find the balance and final payment',f'{CAM} · 8E Using a finance solver to find the balance and final payment','L41',
               flow=('Do Now','APK','Learn','CAS','Worked examples','You try','Exit tasks')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('8E The finance solver and its signs','',None),('CAS','· entering a loan','var(--muted)'),('Worked example 18','→ You try',None),
  ('Worked example 19','→ You try',None),('Worked example 20','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('N','the total number of payments'),('I(%)','the annual interest rate'),('PV / FV','the present (start) value / future (end) value'),
  ('PMT','the amount of each regular payment'),('PpY = CpY','payments per year = compounding periods per year')],
  [('Sign rule',F('money you receive: +'),'money you pay out: −'),
   ('Loan',F('PV +, PMT −'),'FV − = still owing'),
   ('Annuity',F('PV −, PMT +'),'FV + = still in the account'),
   ('Investment with additions',F('PV −, PMT −'),'FV + = what you will get')],
  f'{CAM}, 8E pp. 422–428; Study Design: use of technology with financial modelling functionality to solve problems involving reducing balance loans and annuities'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 Exam 1 Q22','Review of 8D (last lesson)',
  '<div style="font-size:21px">Three lines of the amortisation table for Brian’s annuity investment are shown below.<br>Interest is calculated monthly and Brian receives monthly payments.</div>'
  +AT([['0','0.00','0.00','0.00','620 000.00'],['1','4095.58','2170.00','1925.58','618 074.42'],['2','4095.58','2163.26','1932.32','616 142.10']],
      ['Payment number','Payment ($)','Interest ($)','Principal reduction ($)','Balance ($)'])
  +'<div style="font-size:21px">The number of years that Brian will receive monthly payments of $4095.58 is closest to</div>',
  [('Rate','2170 ÷ 620 000 × 12 × 100 = 4.2% p.a.'),('Finance solver',FS('?','4.2','−620 000','4095.58','0',12,'N')),('Solve','N = 216 months ÷ 12 = 18 years')],
  'Brian is paid for about <b>18 years</b>: <b>B</b>.','VCAA 2026 General Mathematics Exam 1 Q22 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['16','18','20','24'],key='B'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q9','Review of 3C (last term)',
  '<div style="font-size:18px">Twelve teams played in a competition. The total points scored by each team, <i>points for</i>, and the total points scored against each team, <i>points against</i>, are shown in the table below.</div>'
  +'<div style="display:flex;gap:18px;align-items:flex-start">'
  +AT([[a,b] for a,b in zip(['285','325','258','186','217','171'],['187','165','209','207','188','194'])],['<i>Points for</i>','<i>Points against</i>'],fs=15)
  +AT([[a,b] for a,b in zip(['202','194','162','164','183','135'],['253','213','310','247','321','309'])],['<i>Points for</i>','<i>Points against</i>'],fs=15)+'</div>'
  +'<div style="font-size:18px">A least squares line is fitted to the data to enable a prediction of <i>points against</i> from <i>points for</i> scored by each team.<br>The number of times that the predicted value of a team’s <i>points against</i> is less than the actual value of a team’s <i>points against</i> is</div>',
  [('CAS','linear regression: x = points for, y = points against'),('Line','points against = 371.33 − 0.6660 × points for'),
   ('Residuals','predicted &lt; actual ⇔ residual &gt; 0: count the positive residuals = 7')],
  '7 teams were under-predicted: <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q9 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['5','6','7','8'],key='C'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q6a','Review of 7B (earlier this term)',
  '<div style="font-size:27px;margin-top:60px">Timmy’s car was valued at $60 000 when new. The value of the car is depreciated by 35 cents for each kilometre travelled. Assume he travels 25 000 km each year.<br><br>a. What will be the value of Timmy’s car, in dollars, after two years of driving? <span class="muted">(1 mark)</span></div>',
  [('Kilometres','2 × 25 000 = 50 000 km'),('Depreciation','0.35 × 50 000 = 17 500'),('Value','60 000 − 17 500 = 42 500')],
  'After two years the car is worth <b>$42 500</b>.','VCAA 2026 (NHT) General Mathematics Exam 2 Q6 stem and Q6a (NHT report gives answers only)',stat=('nht',)))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q5a','Review of 3A (last term)',
  ('<div style="font-size:18px">The <i>happiness index</i>, a score from 0 to 10, and the average annual <i>income</i>, in dollars per person, were collected for 40 different countries. The data is shown in the scatterplot below.</div>',
   img('dn4_scatter.png',520),
   '<div style="font-size:18px">a. A least squares line with <i>happiness index</i> as the response variable is fitted to this data set. The equation of the least squares line is<br>&nbsp; &nbsp; <i>happiness index</i> = 4.36 + 0.0000154 × <i>income</i><br><b>Draw</b> this least squares line on the scatterplot above. <span class="muted">(1 mark)</span></div>'),
  [('Start','income = 0 → 4.36: point (0, 4.36)'),('End','income = 250 000 → 4.36 + 0.0000154 × 250 000 = 8.21: point (250 000, 8.21)'),('Rule','join the two points with a ruler across the whole graph')],
  'The line runs from (0, 4.36) to (250 000, 8.21).','VCAA 2026 General Mathematics Exam 2 Q5 stem and Q5a (2026 examiner report not yet published: no %)',
  stat=('new',),cmd=('Draw',None,'two points far apart, ruler'),afig=img('dn4_line.png',430)))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3I #25','Compound interest by rule',
  '<div style="font-size:28px;margin-top:50px">I can use the rule for determining the value of an investment with compounding interest or an asset with reducing-balance depreciation after a certain length of time.<br><br>e.g. Adrian invests $250 000 in an account earning compound interest at the rate of 6% per annum. <b>Use</b> a rule to find the value of the investment after 15 years.</div>',
  [('Rule','<i>V<sub>n</sub></i> = <i>R</i><sup><i>n</i></sup> × <i>V</i><sub>0</sub>, &nbsp; <i>R</i> = 1 + 6/100 = 1.06'),('Substitute','<i>V</i><sub>15</sub> = 1.06<sup>15</sup> × 250 000'),('Evaluate','= 599 139.548…')],
  'After 15 years the investment is worth <b>$599 139.55</b>.',f'{CAM12} · Ch 3 skills checklist 3I #25',cmd=('Use',None,'Vn = Rⁿ × V0')))
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q21 (adapted)','Terms of a recurrence relation',
  '<div style="font-size:30px;margin-top:70px">The following recurrence relation can generate a sequence of numbers.<br><br>&nbsp; &nbsp; <i>S</i><sub>0</sub> = 7, &nbsp; <i>S</i><sub><i>n</i>+1</sub> = <i>S<sub>n</sub></i> + 4<br><br>The number 11 appears in this sequence as</div>',
  [('S₀','7'),('S₁','7 + 4 = 11')],
  '11 is the first term after <i>S</i><sub>0</sub>: <b>A</b>.',f'Adapted (by Edrolo) from VCAA 2020 Further Mathematics Exam 1 Recursion and financial modelling Q21 · {EDR12} 3B Q16',
  stat=('mc',85),mc=['<i>S</i><sub>1</sub>','<i>S</i><sub>2</sub>','<i>S</i><sub>3</sub>','<i>S</i><sub>10</sub>','<i>S</i><sub>11</sub>'],key='A'))

# ================= Learn: the finance solver
S.append(learn('Learn · 8E','The finance solver and its signs',
  '<h4>Follow the money</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>money you <b>receive</b> (or are owed) is <b>positive</b>; money you <b>pay out</b> (or owe) is <b>negative</b></li>'
  '<li>enter six of N, I(%), PV, PMT, FV, PpY = CpY; solve for the one left</li>'
  '<li>N counts <b>payments</b> (months, quarters…), not years</li></ul>',
  '<table style="border-collapse:collapse;font-size:22px;margin:30px auto;background:#fff;color:#111">'+'<tr>'+''.join(f'<th style="border:1.5px solid #556;padding:6px 16px;background:#e8eef9">{h}</th>' for h in ('','PV','PMT','FV'))+'</tr>'
  +''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:6px 16px;text-align:{"left" if j==0 else "center"}">{c}</td>' for j,c in enumerate(r))+'</tr>' for r in
     [['Loan','+','−','− still owing · 0 repaid'],['Annuity','−','+','+ still left · 0 paid out'],['Investment + additions','−','−','+ you get it']])+'</table>',
  'Read the sign of FV: it tells you who owes whom.',f'{CAM}, 8E pp. 425–428 (own words) · {EDR}, 6A',
  cards=(kcard('Sign rule','receive +, pay out −'),)))
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['finance-solver']
S.append(cas('CAS · 8E','Entering a loan in the finance solver',
  '<p style="font-size:22px">Isabelle takes out an interest-free loan of $30 000. She makes repayments of $1000 per week to pay off the loan. Isabelle wants to know how much she owes the bank 10 weeks after establishing the loan.</p>'
  +AT([['N','10'],['I(%)','0'],['PV','30 000'],['PMT','−1000'],['FV','(solve)'],['PpY','52'],['CpY','52']],['Input','Value'],fs=18,w='background:#fff;color:#111')
  +'<p class="muted" style="font-size:19px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'FV = −20 000: Isabelle still owes <b>$20 000</b>',
  f'{EDR} · 6A Worked example 2 (pp. 356–357) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Ex 18 investment
S.append(qslide('we','Worked example 18 · 8E','Value of an investment with regular additions',
  '<div style="font-size:30px;margin-top:80px">Lars invests $500 000 at 5.5% per annum, compounding monthly. He makes a regular deposit of $500 per month into the account. What is the value of his investment after 5 years? Round your answer to the nearest cent.</div>',
  [('Signs','PV and PMT are paid to the bank: negative'),('Enter',FS('60','5.5','−500 000','−500','?',12)),('Solve','FV = 692 292.297…: positive, the bank gives it to Lars')],
  'After 5 years, Lars’ investment will be worth <b>$692 292.30</b>.',f'{CAM} · Example 18 (p. 425)',video='Cambridge GO · Example 18 (8E Resources)',cmd=('What',None,'FV, nearest cent')))
S.append(qslide('yt','You try · Edrolo 6F WE3a','Value of an investment with regular additions',
  '<div style="font-size:30px;margin-top:80px">Steve is saving up for a cruise holiday by investing $10 000 in an account that earns interest at a rate of 3.90% per annum, compounding monthly. He deposits $500 at the end of each month.<br><br>a. After 5 years, how much is in Steve’s account?</div>',
  [('Signs','PV and PMT go into the account: negative'),('Enter',FS('60','3.90','−10 000','−500','?',12)),('Solve','FV = 45 214.925…')],
  'After 5 years Steve has <b>$45 214.93</b>.',f'{EDR} · 6F Worked example 3a (p. 409)',cmd=('How much',None,'FV')))

# ================= Ex 19 loan
S.append(qslide('we','Worked example 19 · 8E','Balance and final payment of a reducing balance loan',
  '<div style="font-size:24px;margin-top:30px">Andrew borrows $20 000 at an interest rate of 7.25% per annum, compounding monthly. This loan will be repaid over 4 years with regular payments of $481.25 each month for 47 months followed by a final payment to fully repay the loan.</div>'
  +plist([('a','How much does Andrew owe after 3 years? Round your answer to the nearest cent.'),('b','What is the final payment amount that Andrew must make to fully repay the loan within 4 years (48 months)? Round your answer to the nearest cent.')]),
  [('a · Enter',FS('36','7.25','20 000','−481.25','?',12)),('a · Solve','FV = −5554.3626…: negative, Andrew still owes'),
   ('b · Enter',FS('48','7.25','20 000','−481.25','?',12)),('b · Solve','FV = +0.1079… ≈ 11 cents: overpaid, so the last payment is 11 cents less')],
  '',f'{CAM} · Example 19 (pp. 426–427)',video='Cambridge GO · Example 19 (8E Resources)',cmd=('How much',None,'FV after 36, then after 48'),
  parts=[('a','Andrew owes <b>$5554.36</b>.'),('b','Final payment = 481.25 − 0.11 = <b>$481.14</b>.')]))
S.append(qslide('yt','You try · Edrolo 6B WE3a','Balance of a reducing balance loan',
  '<div style="font-size:30px;margin-top:80px">Cilian takes out a reducing balance loan of $35 000 with a bank that charges an interest rate of 5.9% per annum, compounding monthly. He makes a payment of $1000 each month to pay off the loan.<br><br>a. How much does Cilian still owe after 21 months?</div>',
  [('Signs','loan received: PV +; payments: PMT −'),('Enter',FS('21','5.9','35 000','−1000','?',12)),('Solve','FV = −16 731.708…: negative, he still owes')],
  'Cilian still owes <b>$16 731.71</b>.',f'{EDR} · 6B Worked example 3a (p. 366)',cmd=('How much',None,'FV')))

# ================= Ex 20 annuity
S.append(qslide('we','Worked example 20 · 8E','Balance and final payment of an annuity',
  '<div style="font-size:24px;margin-top:30px">Charlie invests $300 000 into an annuity, paying 5% interest per annum, compounding monthly. Over the next ten years, Charlie receives a payment of $3182 per month from the annuity for each month except the final month.</div>'
  +plist([('a','Find the value of the annuity after five years. Round your answer to the nearest cent.'),('b','Find the final payment from the annuity. Round your answer to the nearest cent.')]),
  [('a · Enter',FS('60','5','−300 000','3182','?',12)),('a · Solve','FV = 168 612.24795…: positive, still owed to Charlie'),
   ('b · Enter',FS('120','5','−300 000','3182','?',12)),('b · Solve','FV = −5.36: Charlie has been overpaid by $5.36')],
  '',f'{CAM} · Example 20 (pp. 428–429)',video='Cambridge GO · Example 20 (8E Resources)',cmd=('Find',None,'FV after 60, then after 120'),
  parts=[('a','The balance of the annuity is <b>$168 612.25</b>.'),('b','Final payment = 3182 − 5.36 = <b>$3176.64</b>.')]))
S.append(qslide('yt','You try · Edrolo 6D WE3a','Balance of an annuity',
  '<div style="font-size:30px;margin-top:80px">Chuck invests $400 000 in an annuity with a bank who offers an interest rate of 4% per annum, compounding monthly. The annuity pays out $5000 per month.<br><br>a. What will the annuity be worth after 6 months?</div>',
  [('Signs','invested: PV −; paid to Chuck: PMT +'),('Enter',FS('6','4','−400 000','5000','?',12)),('Solve','FV = 377 815.849…')],
  'After 6 months the annuity is worth <b>$377 815.85</b>.',f'{EDR} · 6D Worked example 3a (pp. 385–386)',cmd=('What',None,'FV')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2021 Exam 1 Q19','Show what you know',
  '<div style="font-size:20px">Deepa invests $500 000 in an annuity that provides an annual payment of $44 970.55. Interest is calculated annually.<br>The first five lines of the amortisation table are shown.</div>'
  +AT([['0','0.00','0.00','0.00','500 000.00'],['1','44 970.55','20 000.00','24 970.55','475 029.45'],['2','44 970.55','19 001.18','25 969.37','449 060.08'],['3','44 970.55','17 962.40','27 008.15','422 051.93'],['4','44 970.55','16 882.08','28 088.47','393 963.46']],
      ['Payment number','Payment','Interest','Principal reduction','Balance of investment'],fs=15)
  +'<div style="font-size:20px">The number of years, in total, for which Deepa will receive the regular payment of $44 970.55 is closest to</div>',
  [('Rate','20 000 ÷ 500 000 × 100 = 4% p.a.'),('Finance solver',FS('?','4','−500 000','44 970.55','0',1,'N')),('Solve','N = 15.000…')],
  'Deepa is paid for <b>15 years</b>: <b>B</b>.',f'VCAA 2021 Further Mathematics Exam 1 Q19 (examiner report) · {EDR} 6D Q19',
  stat=('mc',44),mc=['12','15','16','18','20'],key='B',dist=[24,44,10,15,6],dis=('A','ignores the interest: 500 000 ÷ 44 970.55 ≈ 11.1, so about 12 payments')))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 2 Q8b','Show what you know',
  '<div style="font-size:28px;margin-top:60px">For renovations to her coffee shop, Sienne took out a reducing balance loan of $570 000, with interest calculated fortnightly.<br>The balance of the loan, in dollars, after <i>n</i> fortnights, <i>S<sub>n</sub></i>, can be modelled by the recurrence relation<br><br>&nbsp; &nbsp; <i>S</i><sub>0</sub> = 570 000, &nbsp; <i>S</i><sub><i>n</i>+1</sub> = 1.001 × <i>S<sub>n</sub></i> − 1193<br><br><b>Show</b> that the compound interest rate for this loan is 2.6% per annum. <span class="muted">(1 mark)</span></div>',
  [('Rate per fortnight','1.001 − 1 = 0.001 = 0.1%'),('Per year','26 fortnights: (1.001 − 1) × 26 × 100 = 2.6')],
  '(1.001 − 1) × 26 × 100 = <b>2.6% per annum</b>. Start from 1.001, not from 2.6%.',f'VCAA 2021 Further Mathematics Exam 2 Recursion and financial modelling Q8b (examiner report) · {EDR} 6B Q21',
  stat=('mark',27),cmd=('Show',None,'start from R = 1.001; no CAS syntax')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8E' and v.get('url')]))
n=assemble(S,'12MAG · L41 · Using a finance solver to find the balance and final payment',os.path.join(ROOT,'lessons','8E slides.html'))
print(n-1,'slides')
