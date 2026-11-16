"""Lesson gm12-u3-l45 (8I Perpetuities) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8I slides.html     Run: python3 tools/deck/gm12-u3-l45/build.py     Screenshots: python3 tools/deck/gm12-u3-l45/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2026 NHT Exam 1 Q24 (B 118; NHT report: answers only) · VCAA 2026 Exam 1 Q15 (C 1.4; no 2026 report yet) ·
          VCAA 2025 Exam 2 Q7a ($850 000; report 93%) · VCAA 2026 NHT Exam 2 Q2a (8.07 + 0.0876 x brain weight; NHT report: answers only).
- APK: Cambridge U1&2 Ch 1 skills checklist 1A #3 (40% as a fraction). The card's other APK (1F #14) was already burnt in l21: dropped (Decisions log, 16 Nov).
- Learn: Cambridge U3&4 8I p. 452 (own words) · Edrolo U3&4 6E pp. 395, 397 (graph idea; finance solver signs).
- CAS (card casYouTry): Edrolo U3&4 6E Worked example 3a (p. 397); steps from planner/cas-skills.json 'finance-solver'.
- Worked examples: Cambridge U3&4 Examples 30-32 (pp. 452-454). You trys: Edrolo U3&4 6E WE1a (p. 396) · YT-8I-31 · YT-8I-32 (planner/written-youtrys.json).
- Exits: VCAA 2016 Exam 1 Q21 (Edrolo 6E Q16; graphs cropped from Edrolo p. 402; report B 50%: A 2, B 50, C 4, D 24, E 19) ·
         VCAA 2021 Exam 2 Q6a-c (Edrolo 6E Q17; report 59% / 47% / 38%).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l45')
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
S.append(title(45,'Perpetuities',f'{CAM} · 8I Perpetuities','L45',
               flow=('Do Now','APK','Learn','CAS','Worked examples','You try','Exit tasks')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill','var(--apk)'),
  ('8I Perpetuities','',None),('CAS','· one period, FV = −PV','var(--muted)'),('Worked examples 30–32','→ You try each',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Perpetuity','an annuity that pays out exactly the interest earned each period, so it lasts forever'),('Principal','the amount invested, V₀: it never changes'),
  ('Growth multiplier','R = 1 + r ÷ (100 × p)'),('Link','perpetuity is to annuity as interest-only loan is to reducing balance loan')],
  [('Recurrence',F('V₀ = principal, Vₙ₊₁ = RVₙ − D'),'the value stays at V₀'),
   ('Payment',F('D = r ÷ (100 × p) × V₀'),'r = annual rate, p = periods per year'),
   ('Finance solver',F('N = 1, PV = −V₀, FV = +V₀'),'solve for PMT or I(%)'),
   ('Rearranged',F('V₀ = D ÷ (r ÷ (100p)) · r = 100p × D ÷ V₀'),'for the principal or the rate')],
  f'{CAM}, 8I p. 452'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 NHT Exam 1 Q24','Review of 8G (last week)',
  '<div style="font-size:18px;margin-top:0">Pauline has a reducing balance loan with a per annum interest rate, compounding quarterly.<br>She makes quarterly repayments.<br>Let <i>P<sub>n</sub></i> be the balance of Pauline’s loan after <i>n</i> quarters.<br>A recurrence relation that can model this balance from quarter to quarter is<br>&nbsp; &nbsp; <i>P</i><sub>0</sub> = 360 000, &nbsp; <i>P</i><sub><i>n</i> + 1</sub> = 1.011<i>P<sub>n</sub></i> − 6789.90<br>After five years, Pauline restructures her loan.<br>The new repayments are $3077.53 per month.<br>The new interest rate is 4.2% per annum, compounding monthly.<br>After the restructure, the number of monthly repayments required to fully repay the loan is</div>',
  [('Rate','R = 1.011 → I = 0.011 × 4 × 100 = 4.4% p.a.'),
   ('After 5 years',FS('20','4.4','360 000','−6789.90','?',4,'FV')+' → −297 078.24'),
   ('Restructure',FS('?','4.2','297 078.24','−3077.53','0',12,'N')+' → N = 117.99…')],
  'Pauline needs <b>118</b> monthly repayments: <b>B</b>.','VCAA 2026 (NHT) General Mathematics Exam 1 Q24 (NHT report gives answers only)',
  stat=('nht',),mc=['97','118','150','151'],key='B'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q15','Review of 5D (last term)',
  '<div style="font-size:26px;margin-top:40px">A small business calculates the seasonal indices of its sales based on the four seasons: summer, autumn, winter and spring.<br>The seasonal index for winter is 0.6<br>The seasonal index for autumn is two-thirds of the seasonal index for spring.<br>The seasonal index for spring is double the seasonal index for winter.<br>The seasonal index for summer is</div>',
  [('Spring','2 × 0.6 = 1.2'),('Autumn','⅔ × 1.2 = 0.8'),('Sum to 4','summer = 4 − (0.6 + 1.2 + 0.8) = 1.4')],
  'The seasonal index for summer is <b>1.4</b>: <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q15 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['0.8','1.2','1.4','1.6'],key='C'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q7a','Review of 8C (last week)',
  '<div style="font-size:22px;margin-top:20px">Declan is a filmmaker and content creator.<br>He has taken out a reducing balance loan to fund a new production.<br>Interest is calculated monthly and Declan makes monthly repayments.<br>Three rows of the amortisation table for Declan’s loan are shown below.</div>'
  +AT([['0','0.00','0.00','0.00','850 000.00'],['1','15 730.88','2975.00','12 755.88','837 244.12'],['2','15 730.88','2930.35','12 800.53','824 443.59']],
      ['Payment number','Payment ($)','Interest ($)','Principal reduction ($)','Balance ($)'],fs=17,w='background:#fff;color:#111')
  +'<div style="font-size:22px">a. <b>What</b> amount, in dollars, did Declan borrow? <span class="muted">(1 mark)</span></div>',
  [('Read the table','payment number 0 = the start of the loan'),('Balance at 0','850 000.00')],
  'Declan borrowed <b>$850 000</b>.','VCAA 2025 General Mathematics Exam 2 Q7a (examiner report)',
  stat=('mark',93),cmd=('What',1,'balance at payment 0')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 NHT Exam 2 Q2a','Review of 3A (last term)',
  ('<div style="font-size:16px">The association between life expectancy, in years, and typical brain weight, in grams, for 12 different mammals was investigated. The life expectancy and brain weight values are shown in the table below.</div>',
   AT([[a,b] for a,b in zip(['7.0','9.8','16','16','17','20','27','30','39','40','41','50'],['81','50','56','120','98','120','180','170','410','420','320','440'])],['Life expectancy (years)','Brain weight (g)'],fs=13,w='background:#fff;color:#111;margin:auto'),
   '<div style="font-size:17px">a. A least squares line with life expectancy as the response variable is fitted to this data.<br><b>Use</b> the data in the table above to find the equation of this least squares line in terms of the variables brain weight and life expectancy. Round the numbers representing the intercept and slope to three significant figures. <span class="muted">(2 marks)</span><br>life expectancy = ______ + ______ × brain weight</div>'),
  [('Variables','explanatory (x) = brain weight · response (y) = life expectancy'),('CAS','linear regression: a = 8.0715…, b = 0.087603…'),('3 sig. figs','8.07 and 0.0876')],
  'life expectancy = <b>8.07</b> + <b>0.0876</b> × brain weight','VCAA 2026 (NHT) General Mathematics Exam 2 Q2a (NHT report gives answers only)',
  stat=('nht',),cmd=('Use',2,'x = brain weight')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Cambridge U1&2 skills checklist 1A','Percentages as fractions (Year 11)',
  '<div style="font-size:30px;margin-top:80px">I can convert percentages to fractions.<br><br>e.g. <b>What</b> is 40% as a fraction?</div>',
  [('Per cent = out of 100','40% = 40 ÷ 100'),('Simplify','40/100 = 2/5'),('Today’s link','r% per period → r ÷ 100 of the balance is paid out')],
  '40% = <b>2/5</b>',f'{CAM12} · Ch 1 skills checklist 1A #3',cmd=('What',None,'divide by 100')))

# ================= Learn
S.append(learn('Learn · 8I','An annuity that never runs out',
  '<h4>Perpetuity</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>each period the interest earned is <b>r ÷ (100p) × V₀</b></li>'
  '<li>withdraw exactly that: the balance stays at V₀ forever</li>'
  '<li>withdraw less: it grows · withdraw more: it runs out (an ordinary annuity)</li>'
  '<li>N doesn’t matter on the finance solver: use N = 1</li></ul>',
  '<table style="border-collapse:collapse;font-size:19px;margin:20px auto;background:#fff;color:#111">'+'<tr>'+''.join(f'<th style="border:1.5px solid #556;padding:5px 12px;background:#e8eef9">{h}</th>' for h in ('n','payment','interest','principal reduction','balance'))+'</tr>'
  +''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:5px 12px;text-align:right">{c}</td>' for c in r)+'</tr>' for r in
     [['0','0','0','0','100 000'],['1','4200','4200','0','100 000'],['2','4200','4200','0','100 000'],['3','4200','4200','0','100 000']])+'</table>'
  +'<p class="muted" style="font-size:16px;text-align:center">V₀ = 100 000, Vₙ₊₁ = 1.042Vₙ − 4200: the graph of Vₙ is a flat line</p>',
  'Finance solver signs: PV negative (you invest), PMT and FV positive (paid to you).',f'{CAM}, 8I p. 452 · {EDR} 6E pp. 395, 397 (own words; table from Edrolo’s 4.2% example)',
  cards=(kcard('Payment','D = r ÷ (100 × p) × V₀'),)))
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['finance-solver']
S.append(cas('CAS · 8I','Perpetuity payment on the finance solver',
  '<p style="font-size:20px">May invests $123 201 in a perpetuity. Her bank offers an interest rate of 1.3% per annum, compounding fortnightly. How much will May receive each fortnight?</p>'
  +AT([['N','1','any value: the balance is unchanged'],['I(%)','1.3','annual rate'],['PV','−123 201','invested with the bank'],['PMT','(solve)','paid to May'],['FV','123 201','paid back to May if she closes it'],['PpY = CpY','26','fortnightly']],['Input','Value','Why'],fs=17,w='background:#fff;color:#111'),
  C['ti'],C['classpad'],'PMT = 61.60: <b>$61.60 a fortnight</b>',
  f'{EDR} · 6E Worked example 3a (p. 397) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Ex 30
S.append(qslide('we','Worked example 30 · 8I','Calculating the payment from a perpetuity',
  '<div style="font-size:28px;margin-top:70px">Elizabeth invests her superannuation payout of $500 000 into a perpetuity that will provide a monthly income.<br>If the interest rate for the perpetuity is 6% per annum, <b>what</b> monthly payment will Elizabeth receive?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','D = 6 ÷ (100 × 12) × 500 000'),('Evaluate','D = 2500')],
  'Elizabeth will receive <b>$2500</b> every month from her investment.',f'{CAM} · Example 30 (p. 452)',video='Cambridge GO · 8I Resources',cmd=('what',None,'D = r ÷ (100p) × V₀')))
S.append(qslide('yt','You try · Edrolo 6E Worked example 1a','Calculating the payment from a perpetuity',
  '<div style="font-size:28px;margin-top:70px">Elise invests $259 920 in a perpetuity. Her bank offers an interest rate of 4.8% per annum, compounding monthly.<br><br>a. <b>What</b> is the monthly amount she will receive from the bank?</div>',
  [('Principal and rate','V₀ = 259 920, r = 4.8 ÷ 12 % per compounding period'),('Substitute','d = 4.8 ÷ (12 × 100) × 259 920 = 4.8 ÷ 1200 × 259 920'),('Evaluate','d = 1039.68')],
  'Elise receives <b>$1039.68</b> each month.',f'{EDR} · 6E Worked example 1a (p. 396)',cmd=('What',None,'d = r ÷ (100p) × V₀')))

# ================= Ex 31
S.append(qslide('we','Worked example 31 · 8I','Calculating the investment required to establish a perpetuity',
  '<div style="font-size:28px;margin-top:80px"><b>Calculate</b> how much money will need to be invested in a perpetuity account, earning interest of 4.8% per annum compounding monthly, if $300 will be withdrawn every month.</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','300 = 4.8 ÷ (100 × 12) × V₀ = 0.004 × V₀'),('Solve','V₀ = 300 ÷ 0.004 = 75 000')],
  '<b>$75 000</b> will need to be invested to establish the perpetuity investment.',f'{CAM} · Example 31 (pp. 452–453)',video='Cambridge GO · 8I Resources',cmd=('Calculate',None,'solve for V₀')))
S.append(qslide('yt','You try · written for 12MAG','Calculating the investment required to establish a perpetuity',
  '<div style="font-size:28px;margin-top:80px"><b>Calculate</b> how much money will need to be invested in a perpetuity account, earning interest of 3.6% per annum compounding monthly, if $450 will be withdrawn every month.</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','450 = 3.6 ÷ (100 × 12) × V₀ = 0.003 × V₀'),('Solve','V₀ = 450 ÷ 0.003 = 150 000')],
  '<b>$150 000</b> will need to be invested.','Written for 12MAG (modelled on '+CAM+' Example 31) · YT-8I-31',cmd=('Calculate',None,'solve for V₀')))

# ================= Ex 32
S.append(qslide('we','Worked example 32 · 8I','Calculating the interest rate of a perpetuity',
  '<div style="font-size:28px;margin-top:70px">A university mathematics faculty has $30 000 to invest. It intends to award an annual mathematics prize of $1500 with the interest earned from investing this money in a perpetuity.<br><b>What</b> is the minimum interest rate that will allow this prize to be awarded indefinitely?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀, p = 1'),('Substitute','1500 = r ÷ (100 × 1) × 30 000 = r × 300'),('Solve','r = 1500 ÷ 300 = 5'),('Check on CAS',FS('1','?','−30 000','1500','30 000',1,'I')+' → 5')],
  'The minimum annual interest rate to award this prize indefinitely is <b>5%</b>.',f'{CAM} · Example 32 (pp. 453–454)',video='Cambridge GO · 8I Resources',cmd=('What',None,'solve for r')))
S.append(qslide('yt','You try · written for 12MAG','Calculating the interest rate of a perpetuity',
  '<div style="font-size:28px;margin-top:70px">A sports club has $40 000 to invest. It intends to award an annual prize of $1800 with the interest earned from investing this money in a perpetuity. <b>What</b> is the minimum interest rate that will allow this prize to be awarded indefinitely?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀, p = 1'),('Substitute','1800 = r ÷ 100 × 40 000 = r × 400'),('Solve','r = 1800 ÷ 400 = 4.5')],
  'The minimum interest rate is <b>4.5%</b> per annum.','Written for 12MAG (modelled on '+CAM+' Example 32) · YT-8I-32',cmd=('What',None,'solve for r')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2016 Exam 1 Q21','Show what you know',
  ('<div style="font-size:17px">Juanita invests $80 000 in a perpetuity that will provide $4000 per year to fund a scholarship at a university.<br>The graph that shows the value of this perpetuity over a period of five years is</div>',
   img('q16.png',560),''),
  [('Perpetuity','the payment equals the interest: 5% of 80 000 = 4000'),('Value','stays at $80 000 every year: a flat line at 80 000')],
  'The value stays at $80 000: <b>B</b>.',f'VCAA 2016 Further Mathematics Exam 1 Q21 (examiner report) · {EDR} 6E Q16 (graphs from p. 402)',
  stat=('mc',50),mc=['A','B','C','D','E'],key='B',dist=[2,50,4,24,19]))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 2 Q6','Show what you know',
  '<div style="font-size:22px">Sienna invests $420 000 in a perpetuity from which she will receive a regular monthly payment of $1890.<br>The perpetuity earns interest at the rate of 5.4% per annum.</div>'
  +plist([('a','<b>Determine</b> the total amount, in dollars, that Sienna will receive after one year of monthly payments. (1 mark)'),
          ('b','<b>Write down</b> the value of the perpetuity after Sienna has received one year of monthly payments. (1 mark)'),
          ('c','Let <i>S<sub>n</sub></i> be the value of Sienna’s perpetuity after <i>n</i> months.<br><b>Complete</b> the recurrence relation, in terms of <i>S</i><sub>0</sub>, <i>S</i><sub><i>n</i> + 1</sub> and <i>S<sub>n</sub></i>, that would model the value of this perpetuity over time. (1 mark)<br><i>S</i><sub>0</sub> = ______ , &nbsp; <i>S</i><sub><i>n</i> + 1</sub> = ______ × <i>S<sub>n</sub></i> – 1890')]),
  [('a · 12 payments','12 × 1890'),('b · Perpetuity','the value never changes'),('c · R','1 + 5.4 ÷ (100 × 12) = 1.0045')],
  '',f'VCAA 2021 Further Mathematics Exam 2 Q6 (examiner report: a 59%, b 47%, c 38%) · {EDR} 6E Q17',
  stat=('avg',48),cmd=('Determine',3,'a · b · c'),
  parts=[('a','<b>$22 680</b>'),('b','<b>$420 000</b>'),('c','<i>S</i><sub>0</sub> = <b>420 000</b>, &nbsp; <i>S</i><sub><i>n</i> + 1</sub> = <b>1.0045</b> × <i>S<sub>n</sub></i> − 1890')]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8I' and v.get('url')]))
n=assemble(S,'12MAG · L45 · Perpetuities',os.path.join(ROOT,'lessons','8I slides.html'))
print(n-1,'slides')
