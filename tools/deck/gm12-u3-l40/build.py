"""Lesson gm12-u3-l40 (8D Analysing financial situations using amortisation tables) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8D slides.html     Run: python3 tools/deck/gm12-u3-l40/build.py     Screenshots: python3 tools/deck/gm12-u3-l40/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- CFAT 2.8.1 (8A-8B-8C) first (planner card).
- Do Now: VCAA 2026 Exam 1 Q24 (D: 1 - 0.001 x 299 368.29/850 = 64.8%) · VCAA 2026 Exam 1 Q8 (C, slope ~ 235/50 = 4.7; scatterplot cropped from p. 5) ·
          VCAA 2026 NHT Exam 2 Q5 stem + Q5a ($4215.93; NHT report: answers only) · VCAA 2026 Exam 2 Q4 stem + Q4a (7/50 = 14%). 2026 reports not yet published: no %.
- APK: Cambridge U1&2 Ch 3 skills checklist 3C #8 (skill + its example) ·
       Edrolo U1&2 3D Q15 = adapted (by Edrolo) from VCAA 2020 Exam 2 Recursion Q9a (2020 E2 report: 64% scored the mark on the ORIGINAL question).
- Learn: Cambridge U3&4 8D pp. 416-418 (own words) · Edrolo U3&4 6D.
- Worked examples: Cambridge U3&4 Examples 15-17 (8D, pp. 416-418).
  You trys (planner card): Ex 15 = Edrolo U3&4 6D WE2a-b (pp. 384-385; a is the step b needs) · Ex 16 = Edrolo 6D WE2c (p. 385) ·
  Ex 17 = written YT-8D-17 (planner/written-youtrys.json; rewritten 16 Nov to ask for the same graph as Example 17).
- CAS: none on the card.
- Exits: VCAA 2020 Further Exam 1 Q25 (Edrolo U3&4 6E Q15; report 79% B; 8/79/5/3/4; graph redrawn from the paper) ·
         VCAA 2021 Further Exam 1 Q23 (Edrolo U3&4 6B Q20; report 31% A; 31/15/11/33/9).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l40')
yid=lambda u:u.split('v=')[1].split('&')[0]
HL=['Payment number','Payment','Interest','Principal reduction','Balance']
def AT(rows,head=HL,fs=17,w=''):
    st=f'border-collapse:collapse;font-size:{fs}px;margin:8px 0;{w}'
    th=''.join(f'<th style="border:1.5px solid #556;padding:3px 8px;background:#e8eef9;font-size:{fs-2}px;line-height:1.15">{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:3px 10px;text-align:{"center" if j==0 else "right"};white-space:nowrap">{c}</td>' for j,c in enumerate(r))+'</tr>' for r in rows)
    return f'<table style="{st}"><tr>{th}</tr>{tr}</table>'
def ATW(rows,head=HL,fs=16): return AT(rows,head,fs,'background:#fff;color:#111')
def img(p,w):
    b=base64.b64encode(open(os.path.join(H,'img',p),'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w}px;max-width:100%;display:block;margin:auto;background:#fff">'
def dots(series,ymax,ystep,W=520,Hh=300,xl='Payment (n)',yl='Amount ($)',nmax=5,dark=False):
    """points plot: series = [(colour, [(n, value)], label)]"""
    L,T,B=70,(40 if len(series)>1 else 20),50; pw=W-L-20; ph=Hh-T-B
    x=lambda n:L+n/nmax*pw; y=lambda v:T+ph-v/ymax*ph
    ink='#111'
    s=[f'<svg viewBox="0 0 {W} {Hh}" width="{W}" style="max-width:100%;display:block;margin:6px auto;background:#fff;border-radius:6px">']
    v=0
    while v<=ymax+1e-9:
        s.append(f'<line x1="{L}" y1="{y(v):.1f}" x2="{L+pw}" y2="{y(v):.1f}" stroke="#ddd"/><text x="{L-6}" y="{y(v)+5:.1f}" font-size="13" text-anchor="end" fill="{ink}">{v:g}</text>'); v+=ystep
    for n in range(nmax+1): s.append(f'<text x="{x(n):.1f}" y="{T+ph+18}" font-size="13" text-anchor="middle" fill="{ink}">{n}</text>')
    s.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T+ph}" stroke="{ink}" stroke-width="2"/><line x1="{L}" y1="{T+ph}" x2="{L+pw}" y2="{T+ph}" stroke="{ink}" stroke-width="2"/>')
    s.append(f'<text x="{L+pw/2}" y="{Hh-6}" font-size="14" text-anchor="middle" fill="{ink}">{xl}</text><text x="16" y="{T+ph/2}" font-size="14" text-anchor="middle" fill="{ink}" transform="rotate(-90 16 {T+ph/2})">{yl}</text>')
    for k,(c,pts,lab) in enumerate(series):
        for n,val in pts: s.append(f'<circle cx="{x(n):.1f}" cy="{y(val):.1f}" r="6" fill="{c}"/>')
        if len(series)>1: s.append(f'<circle cx="{L+10+k*150}" cy="12" r="6" fill="{c}"/><text x="{L+22+k*150}" y="17" font-size="13" fill="{ink}">{lab}</text>')
    return ''.join(s)+'</svg>'
def flat():
    W,Hh,L,T=460,250,60,20; x=lambda n:L+n*70
    s=f'<svg viewBox="0 0 {W} {Hh}" width="{W}" style="display:block;margin:auto;background:#fff"><line x1="{L}" y1="{T+200}" x2="{L}" y2="{T}" stroke="#111" stroke-width="2"/><line x1="{L}" y1="{T+200}" x2="{W-20}" y2="{T+200}" stroke="#111" stroke-width="2"/>'
    s+=f'<text x="{L-6}" y="{T+12}" font-size="16" text-anchor="end" font-style="italic">A<tspan font-size="11" dy="4">n</tspan></text><text x="{W-12}" y="{T+205}" font-size="16" font-style="italic">n</text>'
    for n in range(6): s+=f'<circle cx="{x(n)}" cy="{T+25}" r="6" fill="#111"/><text x="{x(n)}" y="{T+222}" font-size="15" text-anchor="middle">{n}</text>'
    return s+'</svg>'

S=[]
S.append(title(40,'Analysing financial situations using amortisation tables',f'{CAM} · 8D Analysing financial situations using amortisation tables','L40',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 2.8.1','· 8A, 8B, 8C · 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('8D The final payment','',None),('Worked example 15','→ You try',None),('8D Totals: payments and interest','',None),('Worked example 16','→ You try',None),
  ('8D Plotting from a table','',None),('Worked example 17','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Final payment','the last payment, adjusted so the balance ends at exactly 0'),
  ('Total paid','all the payments added together'),
  ('Total interest','what the loan cost (or the annuity earned) on top of the principal'),
  ('Plot from a table','payment number across, the amount (interest, principal reduction or balance) up')],
  [('Final payment',F('balance + interest on it'),'= balance × <i>R</i>'),
   ('Total payments',F('regular payment × number + final payment'),''),
   ('Total interest',F('total payments − principal'),'or add the interest column')],
  f'{CAM}, 8D pp. 416–418; Study Design: use of a table to investigate and analyse the amortisation of a reducing balance loan and of an annuity'))
S.append(cfat('CFAT 2.8.1','Annuity investments, reducing balance loans and amortisation tables','8A, 8B, 8C',14,'CFAT 2.8.1 (8A-8B-8C) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 Exam 1 Q24','Review of 8C (last lesson)',
  '<div style="font-size:23px;margin-top:20px">Selma took out a reducing balance loan of $600 000.<br>Interest on the loan is calculated at the rate of 5.2% per annum, compounding weekly.<br>Selma will make weekly repayments of $850.<br>Assume there are exactly 52 weeks in a year.<br>At some future point the balance of the loan will be reduced to $299 368.29<br>After this future point, a repayment of $850 is made one week later.<br>To the nearest whole number, what percentage of this repayment will reduce the balance of the loan?</div>',
  [('Interest','5.2/5200 × 299 368.29 = 299.37'),('Reduction','850 − 299.37 = 550.63'),('Percentage','550.63 ÷ 850 × 100 = 64.8%')],
  '≈ <b>65%</b> of the repayment reduces the balance: <b>D</b>.','VCAA 2026 General Mathematics Exam 1 Q24 (2026 examiner report not yet published: no %)',
  mc=['50%','52%','58%','65%'],key='D'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q8','Review of 3A (last term)',
  ('<div style="font-size:19px">A least squares line has been fitted to the scatterplot below to enable the number of television sets per 1000 people, <i>TV sets</i>, to be predicted from the number of doctors per 10 000 people, <i>doctors</i>, for a randomly selected sample of 20 countries.</div>',
   img('dn2_scatter.png',560),'<div style="font-size:20px">The slope of the least squares line is closest to</div>'),
  [('Two points','the line passes near (0, 113) and (50, 348)'),('Slope','(348 − 113) ÷ (50 − 0) = 235 ÷ 50 = 4.7')],
  'slope ≈ <b>4.7</b>: <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q8 (2026 examiner report not yet published: no %)',
  mc=['2.7','3.7','4.7','5.7'],key='C'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q5a','Review of 8B (last week)',
  '<div style="font-size:26px;margin-top:50px">Timmy takes out a reducing balance loan with interest compounding monthly. He intends to fully repay the loan with monthly repayments.<br>The balance of the loan, <i>V<sub>n</sub></i>, in dollars, after <i>n</i> months is modelled by the recurrence relation<br><br>&nbsp; &nbsp; <i>V</i><sub>0</sub> = 600 000, &nbsp; <i>V</i><sub><i>n</i> + 1</sub> = 1.0048<i>V<sub>n</sub></i> − 4215.93<br><br>a. What amount does Timmy repay each month? <span class="muted">(1 mark)</span></div>',
  [('Read','the amount subtracted each month is the repayment')],
  'Timmy repays <b>$4215.93</b> each month.','VCAA 2026 (NHT) General Mathematics Exam 2 Q5 stem and Q5a (NHT report gives answers only)',stat=('nht',)))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q4a','Review of 2B (last term)',
  '<div style="font-size:19px">A survey of 280 participants was conducted. The participants reported their average length of sleep each night as very long, long, normal, short or very short. They also reported their happiness level as high, medium or low.<br>The results are shown in the table below.</div>'
  +AT([['very long','17','7','6'],['long','17','23','10'],['normal','42','40','38'],['short','7','27','16'],['very short','5','9','16']],['Length of sleep','High','Medium','Low'],fs=16)
  +'<div style="font-size:19px">a. Consider only the participants who reported a short length of sleep.<br><b>Calculate</b> the percentage of these participants who reported a high happiness level. <span class="muted">(1 mark)</span></div>',
  [('Short row','7 + 27 + 16 = 50'),('Percentage','7 ÷ 50 × 100 = 14%')],
  '<b>14%</b> of the short sleepers reported a high happiness level.','VCAA 2026 General Mathematics Exam 2 Q4 stem and Q4a (2026 examiner report not yet published: no %)',
  cmd=('Calculate',None,'row total first')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3C #8','Tabulating and graphing a sequence',
  '<div style="font-size:28px;margin-top:40px">I can tabulate and graph an arithmetic sequence.<br><br>The sequence, 5, 8, 11, ... is an arithmetic sequence with a common difference of 3. <b>Construct</b> a table showing the term number, <i>n</i>, and its value, <i>t<sub>n</sub></i>, for the first four terms in the sequence. Use the table to plot the graph.</div>',
  [('Table','n: 0, 1, 2, 3 → t<sub>n</sub>: 5, 8, 11, 14'),('Axes','n across, t<sub>n</sub> up'),('Plot','one point per column of the table')],
  AT([['<i>t<sub>n</sub></i>','5','8','11','14']],['<i>n</i>','0','1','2','3'],fs=16,w='background:#fff;color:#111')+dots([('#1f4fb0',[(0,5),(1,8),(2,11),(3,14)],'t<tspan dy="3" font-size="10">n</tspan>')],16,2,W=420,Hh=230,xl='n',yl='tₙ',nmax=4),
  f'{CAM12} · Ch 3 skills checklist 3C #8',cmd=('Construct',None,'table, then plot')))
S.append(qslide('apk','APK · VCAA 2020 Exam 2 Q9a (adapted)','Iterating a recurrence relation',
  '<div style="font-size:28px;margin-top:50px">Amahle opens a savings account.<br>Let <i>B<sub>n</sub></i> be the balance of this savings account, in dollars, <i>n</i> months after it was opened.<br>The month-to-month value of <i>B<sub>n</sub></i> can be determined using the following recurrence relation.<br><br>&nbsp; &nbsp; <i>B</i><sub>0</sub> = 6000, &nbsp; <i>B</i><sub><i>n</i>+1</sub> = 1.002<i>B<sub>n</sub></i><br><br>Write down the value of <i>B</i><sub>3</sub>, the balance of the savings account after three months.<br>Round to the nearest cent. <span class="muted">(1 mark)</span></div>',
  [('B₁','1.002 × 6000 = 6012'),('B₂','1.002 × 6012 = 6024.024'),('B₃','1.002 × 6024.024 = 6036.072…')],
  '<i>B</i><sub>3</sub> = <b>$6036.07</b>',f'Adapted (by Edrolo) from VCAA 2020 Further Mathematics Exam 2 Recursion and financial modelling Q9a; % = original question (2020 Exam 2 report) · {EDR12} 3D Q15',
  stat=('mark',64),cmd=('Write down',None,'iterate three times, round to the cent')))

# ================= Learn 1: final payment
S.append(learn('Learn · 8D','The final payment',
  '<h4>The last payment clears the balance exactly</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>the regular payment rarely divides the debt exactly, so the <b>last payment</b> is adjusted</li>'
  '<li><b>Final payment</b> = balance still owing + one period of interest on it</li><li>its principal reduction = the whole balance, so the new balance is 0</li></ul>',
  '<div style="font-size:22px;text-align:center;line-height:1.7"><span class="frag">Balance before the last payment: $1000 at 1% per period</span><br>'
  '<span class="frag">Interest = 1% × 1000 = $10</span><br><span class="frag">Final payment = 1000 + 10 = <b>$1010</b></span></div>',
  'Don’t just pay the balance: it earns one more period of interest first.',f'{CAM}, 8D p. 416 (own words) · {EDR}, 6D',
  cards=(kcard('Final payment','balance + interest on it'),)))
S.append(qslide('we','Worked example 15 · 8D','Finding the final payment for a reducing balance loan or annuity',
  '<div style="font-size:21px">Consider the following amortisation table for a reducing balance loan of $20 000 with an interest rate of 8% per annum, compounding annually. Regular payments of $5009.12 are made for the first four years as shown in the amortisation table.</div>'
  +AT([['0','0.00','0.00','0.00','20 000.00'],['1','5009.12','1600.00','3409.12','16 590.88'],['2','5009.12','1327.27','3681.85','12 909.03'],['3','5009.12','1032.72','3976.40','8932.63'],['4','5009.12','714.61','4294.51','4638.12']],fs=16)
  +'<div style="font-size:21px"><b>Calculate</b> the final payment required in the fifth year to pay off the loan fully.</div>',
  [('Interest','8/100 × 4638.12 = 371.05'),('Final payment','balance + interest = 4638.12 + 371.05 = 5009.17')],
  'The final payment is <b>$5009.17</b>.',f'{CAM} · Example 15 (p. 416)',video='Cambridge GO · Example 15 (8D Resources)',cmd=('Calculate',None,'interest on the last balance, then add')))
MT=AT([['0','0.00','0.00','0.00','5000.00'],['1','2010.00','500.00','1510.00','3490.00'],['2','2010.00','349.00','1661.00','1829.00'],['3','','','','0.00']],HL[:4]+['Balance of investment'],fs=16)
MIKE='<div style="font-size:20px">Mike invests $5000 in an annuity account paying interest at 10% per annum. Mike wants to receive a payment of $2010 per year. This is modelled using the following amortisation table.</div>'
S.append(qslide('yt','You try · Edrolo 6D WE2a–b','The final payment from an annuity',
  MIKE+MT+'<div style="font-size:20px">Mike wants the final payment amount adjusted so that the annuity will be fully paid out after payment number 3.</div>'
  +plist([('a','Calculate the missing interest for payment number 3.'),('b','Calculate the final payment that Mike will receive for this annuity.')]),
  [],'',f'{EDR} · 6D Worked example 2a–b (pp. 384–385)',cmd=('Calculate',None,'interest, then balance + interest'),
  parts=[('a','10/100 × 1829.00 = <b>$182.90</b>'),('b','1829.00 + 182.90 = <b>$2011.90</b>')]))

# ================= Learn 2: totals
S.append(learn('Learn · 8D','Total payments and total interest',
  '<h4>Add up the payments; the extra over the principal is interest</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><b>Total payments</b> = regular payment × how many + the final payment</li>'
  '<li><b>Total interest</b> = total payments − principal (loan or annuity)</li><li>check: add up the interest column</li></ul>',
  '<div style="font-size:22px;text-align:center;line-height:1.7"><span class="frag">3 payments of $400, then a final $410, on a $1500 loan</span><br>'
  '<span class="frag">Total paid = 3 × 400 + 410 = $1610</span><br><span class="frag">Interest = 1610 − 1500 = <b>$110</b></span></div>',
  'Use the adjusted final payment, not another regular one.',f'{CAM}, 8D p. 417 (own words) · {EDR}, 6D',
  cards=(kcard('Total interest','total payments − principal'),)))
S.append(qslide('we','Worked example 16 · 8D','Finding the total payment made and total interest paid',
  '<div style="font-size:19px">Consider the following amortisation table for a reducing balance loan of $10 000 with an interest rate of 8% per annum, compounding quarterly. Three quarterly payments of $2626 are made.</div>'
  +AT([['0','0.00','0.00','0.00','10 000.00'],['1','2626.00','200.00','2426.00','7574.00'],['2','2626.00','151.48','2474.52','5099.48'],['3','2626.00','101.99','2524.01','2575.47'],['4','A','B','C','0.00']],fs=15)
  +plist([('a','Complete the amortisation table corresponding to payment four such that the final payment ensures that the balance is 0.'),('b','Calculate the total payment made for the loan.'),('c','Calculate the total interest paid on the loan.')]),
  [],'',f'{CAM} · Example 16 (p. 417)',video='Cambridge GO · Example 16 (8D Resources)',cmd=('Calculate',None,'final row, then totals'),
  parts=[('a','B = 8/(100 × 4) × 2575.47 = <b>51.51</b> · C = <b>2575.47</b> · A = 2575.47 + 51.51 = <b>2626.98</b>'),
         ('b','2626 × 3 + 2626.98 = <b>$10 504.98</b>'),('c','10 504.98 − 10 000 = <b>$504.98</b> &nbsp;(or 200 + 151.48 + 101.99 + 51.51)')]))
S.append(qslide('yt','You try · Edrolo 6D WE2c','Interest earned by an annuity',
  MIKE+MT+'<div style="font-size:20px">Mike wants the final payment amount adjusted so that the annuity will be fully paid out after payment number 3. The final payment is $2011.90.</div>'
  +'<div style="font-size:22px;margin-top:8px">c. How much interest has the account earned over three years?</div>',
  [('Total received','2 × 2010.00 + 1 × 2011.90 = 6031.90'),('Principal','the whole $5000 is paid out'),('Interest','6031.90 − 5000.00 = 1031.90')],
  'The account earned <b>$1031.90</b> interest.',f'{EDR} · 6D Worked example 2c (p. 385; the final payment is its part b answer)',cmd=('How much',None,'total received − principal')))

# ================= Learn 3: plotting
S.append(learn('Learn · 8D','Plotting from an amortisation table',
  '<h4>One point per payment</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>payment number across, the amount ($) up</li><li><b>loan</b>: interest falls each payment, principal reduction rises (the balance is shrinking)</li>'
  '<li><b>investment with additions</b>: the interest rises each payment</li></ul>',
  dots([('#1f4fb0',[(1,12.5),(2,9.43),(3,6.33),(4,3.18)],'interest'),('#c62828',[(1,245.35),(2,248.42),(3,251.52),(4,254.71)],'principal reduction')],300,100,W=480,Hh=260),
  'Two series on one graph: use two colours and a key.',f'{CAM}, 8D p. 418 (own words; graph from Example 17)',
  cards=(kcard('Loan','interest ↓, principal reduction ↑'),)))
T17=AT([['0','0.00','0.00','0.00','1000.00'],['1','257.85','12.50','245.35','754.65'],['2','257.85','9.43','248.42','506.23'],['3','257.85','6.33','251.52','254.71'],['4','257.89','3.18','254.71','0.00']],fs=16)
S.append(qslide('we','Worked example 17 · 8D','Plotting from an amortisation table',
  '<div style="font-size:22px">Consider the following amortisation table for a reducing balance loan.</div>'+T17
  +'<div style="font-size:22px">Plot a graph of the interest and principal reduction on the same graph.</div>',
  [('Axes','payment (n) 1 to 4 across, amount ($) 0 to 300 up'),('Interest','(1, 12.50) (2, 9.43) (3, 6.33) (4, 3.18): blue'),('Principal reduction','(1, 245.35) (2, 248.42) (3, 251.52) (4, 254.71): red')],
  'Interest falls and principal reduction rises with each payment.',f'{CAM} · Example 17 (p. 418)',video='Cambridge GO · Example 17 (8D Resources)',
  afig=dots([('#1f4fb0',[(1,12.5),(2,9.43),(3,6.33),(4,3.18)],'interest'),('#c62828',[(1,245.35),(2,248.42),(3,251.52),(4,254.71)],'principal reduction')],300,100,W=440,Hh=240)))
S.append(qslide('yt','You try · written for 12MAG (YT-8D-17)','Plotting from a loan table',
  '<div style="font-size:22px">Consider the following amortisation table for a reducing balance loan.</div>'
  +AT([['0','0.00','0.00','0.00','800.00'],['1','205.00','8.00','197.00','603.00'],['2','205.00','6.03','198.97','404.03'],['3','205.00','4.04','200.96','203.07'],['4','205.10','2.03','203.07','0.00']],fs=16)
  +'<div style="font-size:22px">Plot a graph of the interest and principal reduction on the same graph.</div>',
  [('Axes','payment (n) 1 to 4 across, amount ($) 0 to 250 up'),('Interest','(1, 8.00) (2, 6.03) (3, 4.04) (4, 2.03): blue'),('Principal reduction','(1, 197.00) (2, 198.97) (3, 200.96) (4, 203.07): red')],
  'Interest falls and principal reduction rises with each payment.','Written for 12MAG (modelled on Cambridge Example 17) · planner/written-youtrys.json',
  afig=dots([('#1f4fb0',[(1,8),(2,6.03),(3,4.04),(4,2.03)],'interest'),('#c62828',[(1,197),(2,198.97),(3,200.96),(4,203.07)],'principal reduction')],250,50,W=440,Hh=240)))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2020 Exam 1 Q25','Show what you know',
  ('<div style="font-size:22px">The graph below represents the value of an annuity investment, <i>A<sub>n</sub></i>, in dollars, after <i>n</i> time periods.</div>',flat(),
   '<div style="font-size:22px">A recurrence relation that could match this graphical representation is</div>'),
  [('Flat graph','the value never changes: interest each period = payment'),('Test','B: 2.5% × 200 000 = 5000 = payment ✓')],
  'Interest = payment, so the balance stays at $200 000: <b>B</b>.',f'VCAA 2020 Further Mathematics Exam 1 Q25 (examiner report; graph redrawn from the paper) · {EDR} 6E Q15',
  stat=('mc',79),mc=['<i>A</i><sub>0</sub> = 200 000, <i>A</i><sub><i>n</i>+1</sub> = 1.015<i>A<sub>n</sub></i> − 2500','<i>A</i><sub>0</sub> = 200 000, <i>A</i><sub><i>n</i>+1</sub> = 1.025<i>A<sub>n</sub></i> − 5000',
     '<i>A</i><sub>0</sub> = 200 000, <i>A</i><sub><i>n</i>+1</sub> = 1.03<i>A<sub>n</sub></i> − 5500','<i>A</i><sub>0</sub> = 200 000, <i>A</i><sub><i>n</i>+1</sub> = 1.04<i>A<sub>n</sub></i> − 6000','<i>A</i><sub>0</sub> = 200 000, <i>A</i><sub><i>n</i>+1</sub> = 1.05<i>A<sub>n</sub></i> − 8000'],
  key='B',dist=[8,79,5,3,4]))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 1 Q23','Show what you know',
  '<div style="font-size:26px;margin-top:40px">Bimal has a reducing balance loan.<br>The balance, in dollars, of the loan from month to month, <i>B<sub>n</sub></i>, is modelled by the recurrence relation below.<br><br>&nbsp; &nbsp; <i>B</i><sub>0</sub> = 450 000, &nbsp; <i>B</i><sub><i>n</i> + 1</sub> = <i>RB<sub>n</sub></i> – 2633<br><br>Given that the loan will be fully repaid in 20 years, the value of <i>R</i> is closest to</div>',
  [('Finance Solver','N = 240, PV = 450 000, PMT = −2633, FV = 0, P/Y = C/Y = 12 → I% ≈ 3.6'),('R','R = 1 + 3.6/1200 = 1.003')],
  '<i>R</i> ≈ <b>1.003</b>: <b>A</b>.',f'VCAA 2021 Further Mathematics Exam 1 Q23 (examiner report) · {EDR} 6B Q20',
  stat=('mc',31),mc=['1.003','1.0036','1.03','1.036','1.36'],key='A',dist=[31,15,11,33,9],dis=('D','1.036 uses the ANNUAL rate (3.6%), not the monthly rate (0.3%)')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8D' and v.get('url')]))
n=assemble(S,'12MAG · L40 · Analysing financial situations using amortisation tables',os.path.join(ROOT,'lessons','8D slides.html'))
print(n-1,'slides')
