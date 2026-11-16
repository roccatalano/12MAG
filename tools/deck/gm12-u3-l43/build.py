"""Lesson gm12-u3-l43 (8G Solving harder financial problems) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8G slides.html     Run: python3 tools/deck/gm12-u3-l43/build.py     Screenshots: python3 tools/deck/gm12-u3-l43/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2025 Exam 1 Q22 (A 8.4%; report 68%) · VCAA 2026 Exam 1 Q13 (C; medians 44,40,34,40,42,42,43,40,37; graphs cropped from p. 9) ·
          VCAA 2026 NHT Exam 2 Q8ai (12 years; NHT report answers only) · VCAA 2026 Exam 2 Q7 (5.59; no 2026 report yet).
- APK: VCAA 2016 Exam 2 Q6c adapted (Edrolo U1&2 3C Q19, p. 154; $0.75 per km; report 29% on the original).
       The card's other APK (Cambridge U1&2 1B checklist #7) was already burnt in l21, so it is dropped (Decisions log, 16 Nov).
- Learn: Cambridge U3&4 8G pp. 440-442 (own words). CAS: planner/cas-skills.json 'finance-solver', task = Cambridge Ex 25.
- Worked examples: Cambridge U3&4 Examples 25-26. You trys: YT-8G-25 (planner/written-youtrys.json) · Edrolo U3&4 6B WE3 (a + b, pp. 366-367).
- Exit: VCAA 2016 Exam 2 Q7b (Edrolo U3&4 6B Q22; report 8% full marks, avg 0.2; $28 204). Answers checked with a TVM solver.
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l43')
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
S.append(title(43,'Solving harder financial problems',f'{CAM} · 8G Solving harder financial problems','L43',
               flow=('Do Now','APK','Learn','CAS','Worked examples','You try','Exit task')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one VCAA question (Year 11)','var(--apk)'),
  ('8G Two-stage problems','',None),('CAS','· carrying FV across','var(--muted)'),('Worked examples 25–26','→ You try each',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Stage','a stretch of time where the rate and payment stay the same'),('Change','a new interest rate or a new regular payment part-way through'),
  ('Lump sum','a one-off extra payment that reduces a loan balance'),('Unrounded','keep every in-between value in full until the final answer')],
  [('Two stages',F('FV of stage 1 → PV of stage 2'),'keep the sign: an investment stays negative, a loan stays positive'),
   ('N per stage',F('N = years × PpY'),'stage 2 only counts the payments left'),
   ('Final payment',F('loan: regular + FV'),'FV positive (overpaid) → final is smaller'),
   ('Lump sum',F('balance now − PV needed'),'PV needed = what the rest of the payments can repay')],
  f'{CAM}, 8G pp. 440–442; Study Design: impact of a change in interest rate on repayment amount, time to repay, total interest and total cost'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q22','Review of 8F (last lesson)',
  '<div style="font-size:24px;margin-top:20px">Rita opens a savings account with an initial deposit of $4000.<br>The account earns interest compounding weekly. After the interest is added each week, Rita deposits an additional $50 into the account.<br>Assume there are exactly 52 weeks in one year.<br>The annual interest rate, compounding weekly, that is required to achieve a balance of $14 000 after three years is closest to</div>',
  [('Signs','deposits go in: PV and PMT negative; FV comes back: positive'),('Finance solver',FS('156','?','−4000','−50','14 000',52,'I')),('Solve','I = 8.3723…')],
  'The rate is about <b>8.4%</b>: <b>A</b>.','VCAA 2025 General Mathematics Exam 1 Q22 (examiner report)',
  stat=('mc',68),mc=['8.4%','14.2%','14.6%','17.2%'],key='A'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q13','Review of 5C (last term)',
  ('<div style="font-size:19px">The time series plot below shows the <i>points scored</i> by a football team in each <i>game</i> during a recent season.</div>',
   img('dn2_ts.png',430),
   '<div style="font-size:19px">When smoothed, using three-median smoothing, the time series plot will look most like</div>'),
  [('Read the points','50, 44, 34, 40, 33, 42, 45, 40, 43, 34, 37'),('Medians of three','games 2–10: 44, 40, 34, 40, 42, 42, 43, 40, 37'),
   ('Match','the dip is at game 4 and the peak at game 8: only C')],
  'The smoothed plot is <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q13 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['graph A','graph B','graph C','graph D'],key='C',made=img('dn2_options.png',470)))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q8ai','Review of 8F (last lesson)',
  '<div style="font-size:24px;margin-top:30px">Timmy makes an annuity investment. The value of the annuity, <i>A<sub>n</sub></i>, after <i>n</i> monthly payments have been made to Timmy can be determined using the recurrence relation shown below.<br><br>&nbsp; &nbsp; <i>A</i><sub>0</sub> = 225 000, &nbsp; &nbsp; <i>A</i><sub><i>n</i>+1</sub> = 1.0025<i>A<sub>n</sub></i> − 1862.53<br><br>i. For how many years is Timmy expected to receive a monthly payment? <span class="muted">(1 mark)</span></div>',
  [('Rate','R = 1.0025: 0.25% per month × 12 = 3% p.a.'),('Finance solver',FS('?','3','−225 000','1862.53','0',12,'N')),('Solve','N = 143.999… ≈ 144 months = 144 ÷ 12')],
  'Timmy receives payments for <b>12 years</b>.','VCAA 2026 (NHT) General Mathematics Exam 2 Q8ai (NHT report gives answers only)',
  stat=('nht',),cmd=('how many',None,'N, then years')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q7','Review of 5B (last term)',
  ('<div style="font-size:16px">The happiness index for a particular country is recorded each month for one year, as shown in the table below. The happiness index values for September and October have not been provided.</div>',
   AT([['January','6.72'],['February','6.23'],['March','5.97'],['April','5.81'],['May','5.26'],['June','4.99'],['July','4.85'],['August','5.04'],['September',''],['October',''],['November','6.36'],['December','6.91']],['Month','Happiness index'],fs=12),
   '<div style="font-size:16px">The total of the 10 values given in the table is 58.14<br>Based on this one year of data, seasonal indices for each month are calculated.<br>The total of the 11 seasonal indices for the happiness index relating to all months in the year except December is 10.813<br>The seasonal index for September is 0.961<br><b>Calculate</b> the three-mean smoothed value of the happiness index for September. Round your answer to two decimal places. <span class="muted">(2 marks)</span></div>'),
  [('December SI','12 − 10.813 = 1.187'),('Monthly mean','6.91 ÷ 1.187 = 5.8214…'),('September','0.961 × 5.8214… = 5.5944…'),
   ('October','12 × 5.8214… − 58.14 − 5.5944… = 6.1224…'),('Three-mean','(5.04 + 5.5944… + 6.1224…) ÷ 3 = 5.5856…')],
  'The smoothed value for September is <b>5.59</b>.','VCAA 2026 General Mathematics Exam 2 Q7 (2026 examiner report not yet published: no %)',
  stat=('new',),cmd=('Calculate',2,'2 d.p.')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · VCAA 2016 Exam 2 Q6c (adapted)','Unit cost depreciation (Year 11)',
  '<div style="font-size:28px;margin-top:50px">Anton is a musician, and he purchases a minivan for $64 000 to transport equipment.<br>After four years, the value of the minivan is $40 000.<br>The minivan travelled an average of 8000 km in each of the four years since it was purchased.<br>Assume that the value of the minivan has been depreciated using the unit cost method of depreciation.<br>By how much is the value of the minivan reduced per kilometre travelled? <span class="muted">(1 mark)</span></div>',
  [('Total drop','64 000 − 40 000 = 24 000'),('Total km','4 × 8000 = 32 000 km'),('Per km','24 000 ÷ 32 000 = 0.75')],
  'The value drops by <b>$0.75</b> per kilometre.',f'Adapted from VCAA 2016 Further Mathematics Exam 2 Q6c (examiner report, original question) · {EDR12} 3C Q19',
  stat=('mark',29),cmd=('By how much',None,'drop ÷ total km')))

# ================= Learn
S.append(learn('Learn · 8G','When the conditions change',
  '<h4>Split it into stages</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><b>stage 1:</b> the time before the change: solve for FV</li>'
  '<li><b>stage 2:</b> FV becomes the new PV; change N, I% or PMT</li>'
  '<li>do not round in between: banks only round at the end</li></ul>',
  '<table style="border-collapse:collapse;font-size:20px;margin:24px auto;background:#fff;color:#111">'+'<tr>'+''.join(f'<th style="border:1.5px solid #556;padding:6px 14px;background:#e8eef9">{h}</th>' for h in ('Change','Same payment','To keep the same end date'))+'</tr>'
  +''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:6px 14px">{c}</td>' for c in r)+'</tr>' for r in
     [['Loan rate rises','takes longer, more interest','pay more each month'],['Loan rate falls','repaid sooner, less interest','pay less each month'],['Annuity rate falls','runs out sooner','take less, or add a lump sum'],['Investment payment rises','grows faster','reach the target sooner']])+'</table>',
  'Use the unrounded FV (copy it, don’t retype it).',f'{CAM}, 8G pp. 440–442 (own words)',
  cards=(kcard('Two stages','FV of stage 1 → PV of stage 2'),)))
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['finance-solver']
S.append(cas('CAS · 8G','Carrying the balance into stage 2',
  '<p style="font-size:20px">Derek invests $50 000 at 6.1% p.a., compounding annually, adding $8000 a year; after five years he adds $10 000 a year. Value after twelve years?</p>'
  +AT([['N','5','7'],['I(%)','6.1','6.1'],['PV','−50 000','−112 414.364…'],['PMT','−8000','−10 000'],['FV','(solve)','(solve)'],['PpY = CpY','1','1']],['Input','Stage 1','Stage 2'],fs=17,w='background:#fff;color:#111')
  +'<p class="muted" style="font-size:18px">Stage 1 FV = 112 414.364… comes out positive: type it back in as a negative PV (it is still Derek’s money in the bank).</p>',
  C['ti'],C['classpad'],'FV = 254 343.797…: <b>$254 343.80</b>',
  f'{CAM} · Example 25 (pp. 440–441) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Ex 25
S.append(qslide('we','Worked example 25 · 8G','Finding the value of an investment when the regular payment changes',
  '<div style="font-size:28px;margin-top:60px">Derek invests $50 000 into a compound interest investment paying 6.1% per annum, compounding annually. Derek invests an additional $8000 per year immediately after interest is calculated.<br>After five years, Derek increases his additional investment to $10 000 per year.<br><b>Calculate</b> the value of Derek’s investment after twelve years (in total).</div>',
  [('Stage 1',FS('5','6.1','−50 000','−8000','?',1,'FV')),('Solve','FV = 112 414.364… (5 years before the change)'),
   ('Stage 2',FS('7','6.1','−112 414.364…','−10 000','?',1,'FV')),('Solve','FV = 254 343.797… (7 years after the change)')],
  'The value of Derek’s investment is <b>$254 343.80</b>.',f'{CAM} · Example 25 (pp. 440–441)',video='Cambridge GO · Example 25 (8G Resources)',cmd=('Calculate',None,'two stages')))
S.append(qslide('yt','You try · written for 12MAG','Finding the value of an investment when the regular payment changes',
  '<div style="font-size:28px;margin-top:60px">Ella invests $40 000 into a compound interest investment paying 5.4% per annum, compounding annually. Ella invests an additional $6000 per year immediately after interest is calculated. After four years, Ella increases her additional investment to $9000 per year. <b>Calculate</b> the value of Ella’s investment after ten years (in total).</div>',
  [('Stage 1',FS('4','5.4','−40 000','−6000','?',1,'FV')),('Solve','FV = 75 380.303…'),
   ('Stage 2',FS('6','5.4','−75 380.303…','−9000','?',1,'FV')),('Solve','FV = 165 184.474…')],
  'After ten years Ella’s investment is worth <b>$165 184.47</b>.','Written for 12MAG (modelled on '+CAM+' Example 25) · YT-8G-25',cmd=('Calculate',None,'two stages')))

# ================= Ex 26
S.append(qslide('we','Worked example 26 · 8G','Final payment of a loan when the interest rate changes',
  '<div style="font-size:25px;margin-top:30px">Adrian borrows $150 000 for 25 years at an interest rate of 6.8% per annum, compounding monthly.<br>For the first three years, Adrian repays $1041.11 each month.<br>After 3 years, the interest rate rises to 7.2% per annum. Adrian still wishes to pay off the loan in 25 years so makes 263 monthly payments of $1076.18 followed by a final payment.<br><b>Calculate</b> the final payment to ensure the loan is fully repaid at the end of 25 years. Round your answer to the nearest cent.</div>',
  [('Stage 1',FS('36','6.8','150 000','−1041.11','?',12,'FV')),('Solve','FV = −142 391.835… (still owed after 3 years)'),
   ('Stage 2',FS('264','7.2','142 391.835…','−1076.18','?',12,'FV')),('Solve','FV = 0.1173…: overpaid by 12 cents'),
   ('Final','1076.18 − 0.12')],
  'The final payment is <b>$1076.06</b> (rounding early gives the wrong $1076.08).',f'{CAM} · Example 26 (pp. 441–442)',video='Cambridge GO · Example 26 (8G Resources)',cmd=('Calculate',None,'nearest cent')))
S.append(qslide('yt','You try · Edrolo 6B Worked example 3','Finding the final payment when the interest rate changes',
  '<div style="font-size:21px;margin-top:4px">Cilian takes out a reducing balance loan of $35 000 with a bank that charges an interest rate of 5.9% per annum, compounding monthly. He makes a payment of $1000 each month to pay off the loan.</div>'
  +plist([('a','How much does Cilian still owe after 21 months?'),
          ('b','The bank changes the interest rate for Cilian’s loan after 21 months to 6.4% per annum compounding monthly. Cilian’s monthly payments remain unchanged. To ensure the loan is fully repaid, the final repayment will be lower. If Cilian manages to pay off the rest of the loan, how much interest will he pay in total? Use the rounded value found in part a.')]),
  [('a',FS('21','5.9','35 000','−1000','?',12,'FV')+' → FV = −16 731.708…'),
   ('b · N',FS('?','6.4','16 731.71','−1000','0',12,'N')+' → N = 17.57…: 17 full payments + 1 final'),
   ('b · Left',FS('17','6.4','16 731.71','−1000','?',12,'FV')+' → −570.161…'),
   ('b · Final','N = 1, PV = 570.161…, FV = 0 → PMT = −573.20'),
   ('b · Interest','21 × 1000 + 17 × 1000 + 573.20 − 35 000')],
  '',f'{EDR} · 6B Worked example 3 (pp. 366–367)',cmd=('How much',None,'two stages, then the final payment'),
  parts=[('a','Cilian still owes <b>$16 731.71</b>.'),('b','Total paid $38 573.20, so interest = <b>$3573.20</b>.')]))

# ================= Exit
S.append(qslide('ex','Exit task · VCAA 2016 Exam 2 Q7b','Show what you know',
  '<div style="font-size:23px;margin-top:20px">Ken has borrowed $70 000 to buy a new caravan.<br>He will be charged interest at a rate of 6.9% per annum, compounding monthly.<br>Ken will make monthly repayments of $800.<br><br>After three years, Ken will make a lump sum payment of $<i>L</i> in order to reduce the balance of his loan.<br>This lump sum payment will ensure that Ken’s loan is fully repaid in a further three years.<br>Ken’s repayment amount and interest remains the same.<br>What is the value of Ken’s lump sum payment, $<i>L</i>? Round to the nearest dollar. <span class="muted">(2 marks)</span></div>',
  [('Balance after 3 years',FS('36','6.9','70 000','−800','?',12,'FV')+' → −54 151.599…'),
   ('What 3 more years can repay',FS('36','6.9','?','−800','0',12,'PV')+' → 25 947.576…'),
   ('Lump sum','54 151.599… − 25 947.576… = 28 204.02…')],
  'Ken’s lump sum payment is <b>$28 204</b>.',f'VCAA 2016 Further Mathematics Exam 2 Q7b (examiner report: 8% full marks, average 0.2/2) · {EDR} 6B Q22',
  stat=('mark',8),cmd=('What',2,'balance − PV needed')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8G' and v.get('url')]))
n=assemble(S,'12MAG · L43 · Solving harder financial problems',os.path.join(ROOT,'lessons','8G slides.html'))
print(n-1,'slides')
