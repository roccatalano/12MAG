"""Lesson gm12-u3-l42 (8F Using a finance solver to find interest rates, time taken and regular payments) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8F slides.html     Run: python3 tools/deck/gm12-u3-l42/build.py     Screenshots: python3 tools/deck/gm12-u3-l42/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2025 NHT Exam 1 Q19 (C $10 774.16; scanned paper read as image; NHT report: answers only) ·
          VCAA 2026 Exam 1 Q12 (C: b = 0.836 x 0.930/6.86 = 0.1133, a = -2.71; graphs cropped from p. 8) ·
          VCAA 2026 NHT Exam 2 Q7 (12 222.56 / 12 222.56 / 0 / 252 011.45, NHT report) ·
          VCAA 2026 Exam 2 Q6 (time series plot cropped from p. 11). 2026 reports not yet published: no %.
- APK: Cambridge U1&2 Ch 3 skills checklist 3I #26 (Rohan; interest in 5th year = 100 000 x 1.035^4 x 0.035 = 4016.33).
       The card's second APK (Edrolo U1&2 3E Q11 = VCAA 2017 Exam 2 Q6a) was already burnt as the l34 exit (VCAA 2017 E2 Q6), and every other
       Edrolo U1&2 Ch 3 exam question is burnt too, so this lesson has one APK (Decisions log, 16 Nov).
- Learn: Cambridge U3&4 8F pp. 432-436 (own words).  CAS: planner/cas-skills.json 'finance-solver' (solve for I%, N, PMT), task = Cambridge Ex 21 setup.
- Worked examples: Cambridge U3&4 Examples 21-24 (8F, pp. 432-436). Ex 23 FV after 60 = -0.2897 (final 203.05).
  You trys: written for 12MAG (planner/written-youtrys.json YT-8F-21..24; Edrolo has no WE solving for I%, N or PMT). Answers checked with a TVM solver.
- Exits: VCAA 2018 Exam 2 Q6 stem + bi (Edrolo U3&4 6D Q18; report 48% scored the mark; $2800) ·
         VCAA 2017 Exam 2 Q7 stem + b (Edrolo U3&4 6F Q19; report 26% full marks, avg 0.6/2; $805.65) ·
         VCAA 2021 Exam 2 Q9a-b (Edrolo U3&4 6D Q20; report a 21% full marks, b 8%; $151 925.59, $7039.20).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l42')
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

def solver(N,I,PV,PMT,FV,P,solve):
    return FS(N,I,PV,PMT,FV,P,solve)
S=[]
S.append(title(42,'Using a finance solver to find interest rates, time taken and regular payments',f'{CAM} · 8F Using a finance solver to find interest rates, time taken and regular payments','L42',
               flow=('Do Now','APK','Learn','CAS','Worked examples','You try','Exit tasks')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill','var(--apk)'),
  ('8F Solve for I%, N or PMT','',None),('CAS','· solving for the unknown','var(--muted)'),('Worked examples 21–24','→ You try each',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('N','the total number of payments'),('I(%)','the annual interest rate'),('PV / FV','the present (start) value / future (end) value'),
  ('PMT','the amount of each regular payment'),('Total cost','the sum of all repayments of a loan')],
  [('Unknown',F('enter 6 values'),'solve for the 7th: I%, N or PMT'),
   ('Time taken',F('N → whole payments'),'investment: round up · annuity: round down for regular payments'),
   ('Total interest',F('total repaid − principal'),'loan: total repaid = regular × (N − 1) + final'),
   ('Final payment',F('loan: regular − FV'),'annuity: regular + FV (FV is what is left over or still owed)')],
  f'{CAM}, 8F pp. 432–436; Study Design: use of technology with financial modelling functionality to solve problems involving reducing balance loans and annuities'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 NHT Exam 1 Q19','Review of 8E (last lesson)',
  '<div style="font-size:22px;margin-top:6px">Aisha took out a reducing balance loan of $500 000 with interest calculated quarterly.<br>The balance of the loan, in dollars, after <i>n</i> quarters, <i>A<sub>n</sub></i>, can be modelled by the recurrence relation<br><br>&nbsp; &nbsp; <i>A</i><sub>0</sub> = 500 000, &nbsp; &nbsp; <i>A</i><sub><i>n</i>+1</sub> = 1.015<i>A<sub>n</sub></i> − <i>d</i><br><br>With regular quarterly payments, Aisha repays the loan in full in 20 years.<br>The value of <i>d</i> is closest to</div>',
  [('Rate','R = 1.015: 1.5% per quarter × 4 = 6% p.a.'),('Finance solver',FS('80','6','500 000','?','0',4,'PMT')),('Solve','PMT = −10 774.16: d = 10 774.16')],
  '<i>d</i> ≈ <b>$10 774.16</b>: <b>C</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q19 (NHT report gives answers only)',
  stat=('nht',),mc=['$7598.52','$9923.26','$10 774.16','$19 790.92'],key='C'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q12','Review of 3A (last term)',
  ('<div style="font-size:17px">A class investigated whether there was, for 20 countries, a linear association between <i>life expectancy</i>, in years, and a <i>happiness index</i> on a scale of 1−10. Students were given the following table of summary statistics.</div>'+AT([['Mean','73.8','5.65'],['Standard deviation','6.86','0.930'],['Correlation coefficient (<i>r</i>)','0.836','']],['','<i>Life expectancy</i>','<i>Happiness index</i>'],fs=13),
   img('dn2_row.png',640),
   '<div style="font-size:17px">Options A, B, C and D show four different attempts to fit the calculated least squares line to a scatterplot of the original data. Which one of these attempts is closest to being correct?</div>'),
  [('Slope','b = r × s<sub>y</sub> ÷ s<sub>x</sub> = 0.836 × 0.930 ÷ 6.86 = 0.1133'),('Intercept','a = 5.65 − 0.1133 × 73.8 = −2.71'),
   ('Check','x = 60 → 4.09; x = 85 → 6.92: only C runs from about 4.1 to 6.9')],
  'The line in <b>C</b> is closest.','VCAA 2026 General Mathematics Exam 1 Q12 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['graph A','graph B','graph C','graph D'],key='C',made=img('dn2_options.png',380)))
NHT=['Payment number','Payment ($)','Interest ($)','Principal reduction ($)','Balance ($)']
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q7','Review of 8C (this chapter)',
  '<div style="font-size:21px">Timmy took out a further reducing balance loan with interest compounding annually. He makes annual repayments. Two lines of the amortisation table for Timmy’s loan are shown below.</div>'
  +AT([['0','0.00','0.00','0.00','260 000.00'],['1','20 598.55','12 610.00','7988.55','252 011.45'],['2','','','','']],NHT)
  +'<div style="font-size:21px">After one year, Timmy changes to making interest-only repayments.<br><b>Complete</b> the next line in the amortisation table, rounding all values to the nearest cent. <span class="muted">(2 marks)</span></div>',
  [('Rate','12 610 ÷ 260 000 × 100 = 4.85% p.a.'),('Interest','0.0485 × 252 011.45 = 12 222.555… ≈ 12 222.56'),('Interest only','payment = interest, so principal reduction = 0 and the balance stays 252 011.45')],
  'Line 2: payment <b>12 222.56</b>, interest <b>12 222.56</b>, principal reduction <b>0.00</b>, balance <b>252 011.45</b>.',
  'VCAA 2026 (NHT) General Mathematics Exam 2 Q7 (NHT report gives answers only)',stat=('nht',),cmd=('Complete',2,'all four cells, nearest cent')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q6','Review of 5A (last term)',
  ('<div style="font-size:20px">A time series plot of monthly values of the <i>happiness index</i> in one country over four years is shown below.</div>',
   img('dn4_ts.png',600),
   '<div style="font-size:20px"><b>Identify</b> <b>three</b> qualitative features of this time series plot. <span class="muted">(2 marks)</span></div>'),
  [('Trend','the index rises over the four years: increasing trend'),('Seasonality','peaks and troughs repeat about every 12 months'),('Irregular','small ups and downs that do not repeat')],
  'Increasing trend, seasonality (12-month cycle) and irregular fluctuations; no outliers.','VCAA 2026 General Mathematics Exam 2 Q6 (2026 examiner report not yet published: no %)',
  stat=('new',),cmd=('Identify',2,'three features, named')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3I #26','Using a rule to analyse an investment',
  '<div style="font-size:28px;margin-top:50px">I can use a rule to analyse an investment.<br><br>e.g. Rohan invests $100 000 in an account earning compound interest at the rate of 3.5% per annum. <b>Find</b> the amount of interest earned in the fifth year of the investment.</div>',
  [('Rule','<i>V<sub>n</sub></i> = 1.035<sup><i>n</i></sup> × 100 000'),('Start and end of year 5','<i>V</i><sub>4</sub> = 114 752.30, &nbsp;<i>V</i><sub>5</sub> = 118 768.63'),('Interest','118 768.63 − 114 752.30 = 4016.33')],
  'Rohan earns <b>$4016.33</b> interest in the fifth year.',f'{CAM12} · Ch 3 skills checklist 3I #26',cmd=('Find',None,'V5 − V4')))

# ================= Learn
S.append(learn('Learn · 8F','Solving for I%, N or PMT',
  '<h4>Leave one box empty</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>enter the six values you know, with the usual signs</li>'
  '<li>solve for the one you want: <b>I%</b>, <b>N</b> or <b>PMT</b></li>'
  '<li>always check the rounding by putting the rounded value back in</li></ul>',
  '<table style="border-collapse:collapse;font-size:21px;margin:24px auto;background:#fff;color:#111">'+'<tr>'+''.join(f'<th style="border:1.5px solid #556;padding:6px 14px;background:#e8eef9">{h}</th>' for h in ('Solving for','Round','Why'))+'</tr>'
  +''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:6px 14px">{c}</td>' for c in r)+'</tr>' for r in
     [['PMT (investment)','up','so the target is reached'],['N (investment)','up','the target is reached in that month'],['N (annuity)','down','count only the full regular payments'],['PMT (loan)','nearest cent','then fix the final payment']])+'</table>',
  'Total interest = total paid − amount borrowed.',f'{CAM}, 8F pp. 432–436 (own words)',
  cards=(kcard('Final payment','loan: regular − FV · annuity: regular + FV'),)))
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['finance-solver']
S.append(cas('CAS · 8F','Solving for the interest rate',
  '<p style="font-size:21px">Mingjia puts $20 000 into a compound interest investment where interest compounds monthly. She adds $50 per month. She wants her investment to reach $40 000 in 10 years. Find the annual interest rate.</p>'
  +AT([['N','120'],['I(%)','(solve)'],['PV','−20 000'],['PMT','−50'],['FV','40 000'],['PpY','12'],['CpY','12']],['Input','Value'],fs=18,w='background:#fff;color:#111')
  +'<p class="muted" style="font-size:19px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'I = 4.8076…: <b>4.81%</b> per annum',
  f'{CAM} · Example 21 (p. 432) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

WY=f'Written for 12MAG (modelled on {CAM} Example'
# ================= Ex 21
S.append(qslide('we','Worked example 21 · 8F','Finding the interest rate for an investment with additional payments',
  '<div style="font-size:30px;margin-top:70px">Mingjia puts $20 000 into a compound interest investment where interest compounds monthly. She adds $50 per month. She wants her investment to reach $40 000 in 10 years. Find the annual interest rate required for this to occur. Round your answer to two decimal places.</div>',
  [('Signs','PV and PMT go to the bank: negative; FV comes back: positive'),('Enter',FS('120','?','−20 000','−50','40 000',12,'I')),('Solve','I = 4.807 676…')],
  'Mingjia would require an interest rate of <b>4.81%</b> per annum.',f'{CAM} · Example 21 (p. 432)',video='Cambridge GO · Example 21 (8F Resources)',cmd=('Find',None,'I%, 2 d.p.')))
S.append(qslide('yt','You try · written for 12MAG','Finding the interest rate for an investment with additional payments',
  '<div style="font-size:30px;margin-top:70px">Lena puts $10 000 into a compound interest investment where interest compounds monthly. She adds $100 per month. She wants her investment to reach $30 000 in 10 years. Find the annual interest rate required for this to occur. Round your answer to two decimal places.</div>',
  [('Signs','PV −, PMT −, FV +'),('Enter',FS('120','?','−10 000','−100','30 000',12,'I')),('Solve','I = 4.1609…')],
  'Lena would require an interest rate of <b>4.16%</b> per annum.',f'{WY} 21) · YT-8F-21',cmd=('Find',None,'I%, 2 d.p.')))

# ================= Ex 22
S.append(qslide('we','Worked example 22 · 8F','Regular payment and time taken for an investment with additions',
  '<div style="font-size:24px;margin-top:20px">Winston puts $20 000 into an investment, paying 5.1% interest per annum, compounding monthly.</div>'
  +plist([('a','If Winston wants his investment to be worth at least $40 000 in 5 years, what is the minimum he will need to add each month?'),('b','If Winston invests $1000 each month immediately after interest is calculated, what is the minimum number of months required for his investment to at least triple in value?')]),
  [('a · Enter',FS('60','5.1','−20 000','?','40 000',12,'PMT')),('a · Solve','PMT = −208.3416…: $208.34 only reaches $39 999.89, so round up'),
   ('b · Enter',FS('?','5.1','−20 000','−1000','60 000',12,'N')),('b · Solve','N = 34.32…: 34 months gives $59 598.15, so round up to 35')],
  '',f'{CAM} · Example 22 (p. 433)',video='Cambridge GO · Example 22 (8F Resources)',cmd=('what',None,'PMT, then N (round up)'),
  parts=[('a','Winston will add <b>$208.35</b> each month.'),('b','The investment will take <b>35 months</b> to triple.')]))
S.append(qslide('yt','You try · written for 12MAG','Regular payment and time taken for an investment with additions',
  '<div style="font-size:24px;margin-top:20px">Omar puts $15 000 into an investment, paying 4.8% interest per annum, compounding monthly.</div>'
  +plist([('a','If Omar wants his investment to be worth at least $30 000 in 6 years, what is the minimum he will need to add each month?'),('b','If Omar invests $800 each month immediately after interest is calculated, what is the minimum number of months required for his investment to at least triple in value?')]),
  [('a · Enter',FS('72','4.8','−15 000','?','30 000',12,'PMT')),('a · Solve','PMT = −120.1848…: $120.18 falls just short, so round up'),
   ('b · Enter',FS('?','4.8','−15 000','−800','45 000',12,'N')),('b · Solve','N = 32.72…: round up to 33')],
  '',f'{WY} 22) · YT-8F-22',cmd=('what',None,'PMT, then N (round up)'),
  parts=[('a','Omar needs to add at least <b>$120.19</b> each month.'),('b','It takes <b>33 months</b> to triple.')]))

# ================= Ex 23
S.append(qslide('we','Worked example 23 · 8F','Payment, total repaid and total interest for a loan',
  '<div style="font-size:21px;margin-top:6px">Sipho borrows $10 000 to be repaid in 59 equal monthly payments followed by a 60th payment of less than one dollar more than the regular payment. Interest is charged at the rate of 8% per annum, compounding monthly.</div>'
  +plist([('a','Find the regular monthly payment amount. Round your answer to the nearest cent.'),('b','Find the final payment. Round your answer to the nearest cent.'),
          ('c','Find the total of the repayments on the loan. Round your answer to the nearest cent.'),('d','Find the total amount of interest paid. Round your answer to the nearest cent.')]),
  [('a · Enter',FS('60','8','10 000','?','0',12,'PMT')),('a · Solve','PMT = −202.7639…'),
   ('b · Check',FS('60','8','10 000','−202.76','?',12,'FV')+': FV = −0.2897…, still owing 29 cents'),
   ('c · Total','59 × 202.76 + 203.05'),('d · Interest','12 165.89 − 10 000')],
  '',f'{CAM} · Example 23 (pp. 434–435)',video='Cambridge GO · Example 23 (8F Resources)',cmd=('Find',None,'PMT, final, total, interest'),
  parts=[('a','Sipho repays <b>$202.76</b> as the regular payment.'),('b','Final payment = 202.76 + 0.29 = <b>$203.05</b>.'),('c','Total of repayments = <b>$12 165.89</b>.'),('d','Interest paid = <b>$2165.89</b>.')]))
S.append(qslide('yt','You try · written for 12MAG','Payment, total repaid and total interest for a loan',
  '<div style="font-size:21px;margin-top:6px">Priya borrows $15 000 to be repaid in 47 equal monthly payments followed by a 48th payment of less than one dollar more than the regular payment. Interest is charged at the rate of 7% per annum, compounding monthly.</div>'
  +plist([('a','Find the regular monthly payment amount. Round your answer to the nearest cent.'),('b','Find the final payment. Round your answer to the nearest cent.'),
          ('c','Find the total of the repayments on the loan. Round your answer to the nearest cent.'),('d','Find the total amount of interest paid. Round your answer to the nearest cent.')]),
  [('a · Enter',FS('48','7','15 000','?','0',12,'PMT')),('a · Solve','PMT = −359.1936…'),
   ('b · Check',FS('48','7','15 000','−359.19','?',12,'FV')+': FV = −0.2026…, still owing 20 cents'),
   ('c · Total','47 × 359.19 + 359.39'),('d · Interest','17 241.32 − 15 000')],
  '',f'{WY} 23) · YT-8F-23',cmd=('Find',None,'PMT, final, total, interest'),
  parts=[('a','The regular payment is <b>$359.19</b>.'),('b','Final payment = 359.19 + 0.20 = <b>$359.39</b>.'),('c','Total of repayments = <b>$17 241.32</b>.'),('d','Interest paid = <b>$2241.32</b>.')]))

# ================= Ex 24
S.append(qslide('we','Worked example 24 · 8F','Interest rate, time taken and regular payment for an annuity',
  '<div style="font-size:19px;margin-top:0">Joe invests $200 000 into an annuity, with interest compounding monthly.</div>'
  +plist([('a','What interest rate would allow Joe to withdraw $2500 each month for 10 years? Round your answer to one decimal place.'),
          ('b','Assume the interest rate is 5% per annum and that Joe receives a regular monthly payment of $3000. For how many months will Joe receive a regular payment?'),
          ('c','Assume that the interest rate is 5% per annum and that Joe wishes to be paid monthly payments for 10 years. How much will he regularly receive each month?'),
          ('d','If Joe receives the regular monthly payment found in part c for 119 months, what will his final payment be? Round your answer to the nearest cent.')]),
  [('a',FS('120','?','−200 000','2500','0',12,'I')+' → I = 8.689…'),('b',FS('?','5','−200 000','3000','0',12,'N')+' → N = 78.26…: round down'),
   ('c',FS('120','5','−200 000','?','0',12,'PMT')+' → PMT = 2121.3103…'),('d','PMT = 2121.31, solve FV = +0.047…: still owed to Joe, add it')],
  '',f'{CAM} · Example 24 (pp. 435–436)',video='Cambridge GO · Example 24 (8F Resources)',cmd=('What',None,'I%, N, PMT, final'),
  parts=[('a','<b>8.7%</b> per annum.'),('b','<b>78 months</b> of regular payments.'),('c','<b>$2121.31</b> each month.'),('d','Final payment = 2121.31 + 0.05 = <b>$2121.36</b>.')]))
S.append(qslide('yt','You try · written for 12MAG','Interest rate, time taken and regular payment for an annuity',
  '<div style="font-size:19px;margin-top:0">Kate invests $250 000 into an annuity, with interest compounding monthly.</div>'
  +plist([('a','What interest rate would allow Kate to withdraw $3000 each month for 10 years? Round your answer to one decimal place.'),
          ('b','Assume the interest rate is 4.5% per annum and that Kate receives a regular monthly payment of $3500. For how many months will Kate receive a regular payment?'),
          ('c','Assume that the interest rate is 4.5% per annum and that Kate wishes to be paid monthly payments for 15 years. How much will she regularly receive each month?'),
          ('d','If Kate receives the regular monthly payment found in part c for 179 months, what will her final payment be? Round your answer to the nearest cent.')]),
  [('a',FS('120','?','−250 000','3000','0',12,'I')+' → I = 7.748…'),('b',FS('?','4.5','−250 000','3500','0',12,'N')+' → N = 83.30…: round down'),
   ('c',FS('180','4.5','−250 000','?','0',12,'PMT')+' → PMT = 1912.4832…'),('d','PMT = 1912.48, solve FV = +0.826…: add it')],
  '',f'{WY} 24) · YT-8F-24',cmd=('What',None,'I%, N, PMT, final'),
  parts=[('a','<b>7.7%</b> per annum.'),('b','<b>83 months</b> of regular payments.'),('c','<b>$1912.48</b> each month.'),('d','Final payment = 1912.48 + 0.83 = <b>$1913.31</b>.')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 2 Q6bi','Show what you know',
  '<div style="font-size:26px;margin-top:50px">Julie has retired from work and has received a superannuation payment of $492 800.<br><b>Option 2</b><br>Julie could invest the $492 800 in an annuity, instead of a perpetuity.<br>The annuity earns interest at the rate of 4.32% per annum, compounding monthly.<br>The balance of Julie’s annuity at the end of the first year of investment would be $480 242.25<br><br>b. i. What monthly payment, in dollars, would Julie receive? <span class="muted">(1 mark)</span></div>',
  [('Enter',FS('12','4.32','−492 800','?','480 242.25',12,'PMT')),('Solve','PMT = 2800.000…')],
  'Julie would receive <b>$2800</b> each month.',f'VCAA 2018 Further Mathematics Exam 2 Q6 (Option 2) bi (examiner report) · {EDR} 6D Q18',
  stat=('mark',48),cmd=('What',None,'PMT')))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2017 Exam 2 Q7b','Show what you know',
  '<div style="font-size:20px;margin-top:0">Alex sold his mechanics’ business for $360 000 and invested this amount in a perpetuity.<br>The perpetuity earns interest at the rate of 5.2% per annum.<br>Interest is calculated and paid monthly.<br><br>b. Later, Alex converts the perpetuity to an annuity investment.<br>This annuity investment earns interest at the rate of 3.8% per annum, compounding monthly.<br>For the first four years Alex makes a further payment each month of $500 to his investment.<br>This monthly payment is made immediately after the interest is added.<br>After four years of these regular monthly payments, Alex increases the monthly payment.<br>This new monthly payment gives Alex a balance of $500 000 in his annuity after a further two years.<br><br>What is the value of Alex’s new monthly payment?<br>Round your answer to the nearest cent. <span class="muted">(2 marks)</span></div>',
  [('First 4 years',FS('48','3.8','−360 000','−500','?',12,'FV')),('Balance','FV = 444 872.94…'),('Next 2 years',FS('24','3.8','−444 872.94','?','500 000',12,'PMT')),('Solve','PMT = −805.65…')],
  'Alex’s new monthly payment is <b>$805.65</b>.',f'VCAA 2017 Further Mathematics Exam 2 Q7b (stem and part b; examiner report) · {EDR} 6F Q19',
  stat=('mark',26),cmd=('What',2,'two finance-solver steps')))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2021 Exam 2 Q9','Show what you know',
  '<div style="font-size:19px">Sienna invests $152 431 into an annuity from which she will receive a regular monthly payment of $900 for 25 years. The interest rate for this annuity is 5.1% per annum, compounding monthly.</div>'
  +plist([('a','Let <i>V<sub>n</sub></i> be the balance of the annuity after <i>n</i> monthly payments. A recurrence relation written in terms of <i>V</i><sub>0</sub>, <i>V</i><sub><i>n</i>+1</sub> and <i>V<sub>n</sub></i> can model the value of this annuity from month to month. Showing recursive calculations, determine the value of the annuity after two months. Round your answer to the nearest cent. (2 marks)'),
          ('b','After two years, the interest rate for this annuity will fall to 4.6%. To ensure that she will still receive the same number of $900 monthly payments, Sienna will add an extra one-off amount into the annuity at this time. Determine the value of this extra amount that Sienna will add. Round your answer to the nearest cent. (1 mark)')]),
  [('a · R','1 + 5.1 ÷ 1200 = 1.00425'),('a · Recursion','<i>V</i><sub>1</sub> = 1.00425 × 152 431 − 900 = 152 178.83; <i>V</i><sub>2</sub> = 1.00425 × 152 178.83 − 900'),
   ('b · After 2 years',FS('24','5.1','−152 431','900','?',12,'FV')+' → 146 073.74'),('b · Needed',FS('276','4.6','?','900','0',12,'PV')+' → 153 112.94'),('b · Extra','153 112.94 − 146 073.74')],
  '',f'VCAA 2021 Further Mathematics Exam 2 Q9 (examiner report: a 21% full marks, b 8%) · {EDR} 6D Q20',
  stat=('mark',8),cmd=('determine',None,'recursion, then two solver steps'),
  parts=[('a','<i>V</i><sub>2</sub> = <b>$151 925.59</b>'),('b','Sienna adds <b>$7039.20</b>.')]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8F' and v.get('url')]))
n=assemble(S,'12MAG · L42 · Using a finance solver to find interest rates, time taken and regular payments',os.path.join(ROOT,'lessons','8F slides.html'))
print(n-1,'slides')
