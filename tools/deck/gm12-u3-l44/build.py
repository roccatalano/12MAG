"""Lesson gm12-u3-l44 (8H Interest-only loans) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/8H slides.html     Run: python3 tools/deck/gm12-u3-l44/build.py     Screenshots: python3 tools/deck/gm12-u3-l44/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2025 Exam 1 Q24 (A 19; report 52%; replaces the card's 2026 E1 Q23, which is interest-only = today's 8H content) ·
          VCAA 2026 Exam 1 Q14 (C 0.64) · VCAA 2026 Exam 2 Q11 ($1404.83, 602; no 2026 report yet) · VCAA 2026 NHT Exam 2 Q1e (not an outlier; NHT report).
- APK: VCAA 2020 Exam 2 Q7a, original wording (report 94%). Edrolo U1&2 3B Q15 adapts Q7a+b, but Q7b is burnt (l32 exit), so only part a is used.
       The card's other APK (Cambridge U1&2 1B checklist #6) was already burnt in l20: dropped (Decisions log, 16 Nov).
- Learn: Cambridge U3&4 8H pp. 446-447 (own words; D = 40/50/60 table from p. 447). CAS: planner/cas-skills.json 'finance-solver', task = Cambridge Ex 27.
- Worked examples: Cambridge U3&4 Examples 27-29 (pp. 448-449). You trys: Edrolo U3&4 6C WE1a (p. 375) · YT-8H-28 · YT-8H-29 (planner/written-youtrys.json).
- Exit: VCAA 2021 Exam 1 Q24 (Edrolo U3&4 6C Q13; report B 33%: A 9, B 33, C 25, D 15, E 16). Answers checked with a TVM solver.
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l44')
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

def MT(rows):
    c=[rows[k:k+5] for k in range(0,len(rows),5)]
    th=''.join('<th style="border:1px solid #556;padding:2px 8px;background:#e8eef9">Mammal</th><th style="border:1px solid #556;padding:2px 8px;background:#e8eef9">kg</th>' for _ in c)
    tr=''.join('<tr>'+''.join((f'<td style="border:1px solid #556;padding:1px 8px;white-space:nowrap">{col[r][0]}</td><td style="border:1px solid #556;padding:1px 8px;text-align:right">{col[r][1]}</td>' if r<len(col) else '<td style="border:1px solid #556"></td><td style="border:1px solid #556"></td>') for col in c)+'</tr>' for r in range(5))
    return f'<table style="border-collapse:collapse;font-size:14px;margin:4px auto;background:#fff;color:#111"><tr>{th}</tr>{tr}</table>'
def solver(N,I,PV,PMT,FV,P,solve):
    return FS(N,I,PV,PMT,FV,P,solve)
S=[]
S.append(title(44,'Interest-only loans',f'{CAM} · 8H Interest-only loans','L44',
               flow=('Do Now','APK','Learn','CAS','Worked examples','You try','Exit task')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one VCAA question (Year 11)','var(--apk)'),
  ('8H Interest-only loans','',None),('CAS','· one period, FV = −PV','var(--muted)'),('Worked examples 27–29','→ You try each',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Interest-only loan','each payment equals the interest charged, so the balance never goes down'),('Principal','the amount borrowed, V₀'),
  ('Growth multiplier','R = 1 + r ÷ (100 × p)'),('Use','common for investments (shares, property): the loan is repaid in full at the end')],
  [('Recurrence',F('V₀ = principal, Vₙ₊₁ = RVₙ − D'),'the balance stays at V₀'),
   ('Payment',F('D = r ÷ (100 × p) × V₀'),'r = annual rate, p = periods per year'),
   ('Finance solver',F('N = 1, FV = −PV'),'solve for PMT'),
   ('Rearranged',F('V₀ = D ÷ (r ÷ (100p)) · r = 100p × D ÷ V₀'),'for the principal or the rate')],
  f'{CAM}, 8H pp. 446–447'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q24','Review of 8F–8G (last week)',
  '<div style="font-size:24px;margin-top:20px">Dennis invests $800 000 in an annuity.<br>The annuity earns interest at 4.8% per annum, compounding monthly.<br>After the interest is credited to the annuity, Dennis receives a monthly payment of $6000.<br>After some years, the balance of the annuity is $521 118.96<br>For the remainder of the annuity, Dennis receives a monthly payment of $4767.66<br>The total number of years for which Dennis receives payments is closest to</div>',
  [('Stage 1',FS('?','4.8','−800 000','6000','521 118.96',12,'N')+' → N = 84'),
   ('Stage 2',FS('?','4.8','−521 118.96','4767.66','0',12,'N')+' → N = 144'),('Years','(84 + 144) ÷ 12 = 19')],
  'Dennis receives payments for <b>19 years</b>: <b>A</b>.','VCAA 2025 General Mathematics Exam 1 Q24 (examiner report)',
  stat=('mc',52),mc=['19','20','21','22'],key='A'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q14','Review of 5D (last term)',
  '<div style="font-size:26px;margin-top:40px">To correct for seasonality, the number of cold drinks sold in a shop in July is increased by 56.25%.<br>The seasonal index for the sales of cold drinks in July is closest to</div>',
  [('Deseasonalise','deseasonalised = actual ÷ SI'),('Increase by 56.25%','actual ÷ SI = 1.5625 × actual'),('Solve','SI = 1 ÷ 1.5625 = 0.64')],
  'The seasonal index for July is <b>0.64</b>: <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q14 (2026 examiner report not yet published: no %)',
  stat=('new',),mc=['0.178','0.4375','0.64','0.79'],key='C'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 Exam 2 Q11','Review of 8G (last lesson)',
  '<div style="font-size:22px;margin-top:10px">Hunter takes out a reducing balance loan of $500 000.<br>The interest rate for Hunter’s loan is 4.66% per annum, compounding fortnightly.<br>Hunter makes scheduled repayments of $1303.02 per fortnight.<br>After reducing the loan by $97 764.34, Hunter makes a larger repayment of a fixed amount each fortnight.<br>These larger repayments enable him to pay off the loan with 48 fewer repayments than originally scheduled.<br>Assume there are exactly 26 fortnights in one year.<br>What is the value of the larger fortnightly repayment, rounded to the nearest cent, and how many fortnightly repayments, in total, will Hunter make over the life of the loan? <span class="muted">(2 marks)</span></div>',
  [('Scheduled',FS('?','4.66','500 000','−1303.02','0',26,'N')+' → N = 650'),
   ('Balance','500 000 − 97 764.34 = 402 235.66 owed'),
   ('When',FS('?','4.66','500 000','−1303.02','−402 235.66',26,'N')+' → N = 200'),
   ('Larger',FS('402','4.66','402 235.66','?','0',26,'PMT')+' (650 − 48 − 200 = 402) → −1404.826…'),
   ('Total','200 + 402 = 602')],
  'Larger repayment = <b>$1404.83</b>; total number of repayments = <b>602</b>.','VCAA 2026 General Mathematics Exam 2 Q11 (2026 examiner report not yet published: no %)',
  stat=('new',),cmd=('What',2,'PMT and N')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 NHT Exam 2 Q1e','Review of 1G (last term)',
  ('<div style="font-size:16px">The table below displays the typical body weight, in kilograms, for a sample of 19 different mammals.</div>',
   '<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:100%">'+MT([('okapi','250'),('gorilla','210'),('pig','190'),('Brazilian tapir','160'),('jaguar','100'),('grey seal','85'),('giant armadillo','60'),('sheep','56'),('chimpanzee','52'),('kangaroo','35'),('goat','28'),('roedeer','15'),('baboon','11'),('rhesus monkey','6.8'),('raccoon','4.3'),('red fox','4.2'),('cat','3.3'),('echidna','3.0'),('rabbit','2.5')])
   +'<table style="border-collapse:collapse;font-size:14px;margin:6px auto;background:#fff;color:#111"><tr>'+''.join(f'<th style="border:1px solid #556;padding:2px 10px;background:#e8eef9">{h}</th>' for h in ('Minimum','Q1','Median','Q3','Maximum'))+'</tr><tr>'+''.join(f'<td style="border:1px solid #556;padding:2px 10px;text-align:center">{c}</td>' for c in ('','4.3','','100','250'))+'</tr></table></div>',
   '<div style="font-size:17px">e. The body weight of the okapi is removed from the data set. A new mammal with a typical body weight of 240 kg is added to the data set.<br><b>Explain</b> whether or not the typical body weight value of the new mammal is an outlier. Include a relevant calculation in your answer. <span class="muted">(2 marks)</span></div>'),
  [('Quartiles','240 is still the largest value, so Q1 = 4.3 and Q3 = 100 stay the same'),('IQR','100 − 4.3 = 95.7'),('Upper fence','UF = 100 + 1.5 × 95.7 = 243.55')],
  'As 240 &lt; 243.55 = UF, the new mammal’s body weight is <b>not an outlier</b>.','VCAA 2026 (NHT) General Mathematics Exam 2 Q1e (NHT report gives answers only)',
  stat=('nht',),cmd=('Explain',2,'upper fence calculation')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · VCAA 2020 Exam 2 Q7a','Flat rate depreciation (Year 11)',
  '<div style="font-size:28px;margin-top:60px">Samuel owns a printing machine.<br>The printing machine is depreciated in value by Samuel using flat rate depreciation.<br>The value of the machine, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation<br><br>&nbsp; &nbsp; <i>V</i><sub>0</sub> = 120 000, &nbsp; &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − 15 000<br><br>a. By what amount, in dollars, does the value of the machine decrease each year? <span class="muted">(1 mark)</span></div>',
  [('Read the rule','Vₙ₊₁ = Vₙ − 15 000: the same amount comes off every year'),('Today’s link','interest-only: Vₙ₊₁ = RVₙ − D, and the balance stays the same')],
  'The value decreases by <b>$15 000</b> each year.',f'VCAA 2020 Further Mathematics Exam 2 Q7a (examiner report) · {EDR12} 3B Q15 (adapted there with part b; part b is already used)',
  stat=('mark',94),cmd=('By what amount',None,'d in the rule')))

# ================= Learn
S.append(learn('Learn · 8H','When the payment equals the interest',
  '<h4>Interest-only loan</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>each period the interest added is <b>r ÷ (100p) × V₀</b></li>'
  '<li>pay exactly that: the balance stays at V₀</li>'
  '<li>pay less: the balance grows · pay more: it falls</li>'
  '<li>the principal is still owed at the end</li></ul>',
  '<table style="border-collapse:collapse;font-size:19px;margin:20px auto;background:#fff;color:#111">'+'<tr>'+''.join(f'<th style="border:1.5px solid #556;padding:5px 12px;background:#e8eef9">{h}</th>' for h in ('n','D = 40','D = 50','D = 60'))+'</tr>'
  +''.join('<tr>'+''.join(f'<td style="border:1.5px solid #556;padding:5px 12px;text-align:right">{c}</td>' for c in r)+'</tr>' for r in
     [['0','1000','1000','1000'],['1','1010','1000','990'],['2','1020.50','1000','979.50'],['3','1031.525','1000','968.475'],['4','1043.101…','1000','956.898…'],['','grows','<b>stays the same</b>','falls']])+'</table>'
  +'<p class="muted" style="font-size:16px;text-align:center">V₀ = 1000, Vₙ₊₁ = 1.05Vₙ − D (Cambridge 8H, p. 447)</p>',
  'Finance solver: one period is enough (N = 1, FV = −PV).',f'{CAM}, 8H pp. 446–447 (own words)',
  cards=(kcard('Payment','D = r ÷ (100 × p) × V₀'),)))
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['finance-solver']
S.append(cas('CAS · 8H','Interest-only payment on the finance solver',
  '<p style="font-size:20px">Jane borrows $50 000 on an interest-only loan at 9% p.a., compounding monthly. Monthly payment?</p>'
  +AT([['N','1','one compounding period'],['I(%)','9','annual rate'],['PV','50 000','received'],['PMT','(solve)',''],['FV','−50 000','still owed after one payment'],['PpY = CpY','12','monthly']],['Input','Value','Why'],fs=17,w='background:#fff;color:#111'),
  C['ti'],C['classpad'],'PMT = −375: <b>$375 a month</b>',
  f'{CAM} · Example 27 (p. 448) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Ex 27
S.append(qslide('we','Worked example 27 · 8H','Finding the regular payment for an interest-only loan',
  '<div style="font-size:28px;margin-top:70px">Jane borrows $50 000 to buy some shares. Jane negotiates an interest-only loan at an interest rate of 9% per annum, compounding monthly. <b>What</b> is the monthly amount Jane will be required to pay?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),
   ('Substitute','D = 9 ÷ (100 × 12) × 50 000 = 375'),('Check on CAS',FS('1','9','50 000','?','−50 000',12,'PMT')+' → −375')],
  'Jane will need to repay <b>$375</b> every month on this interest-only loan.',f'{CAM} · Example 27 (p. 448)',video='Cambridge GO · 8H Resources',cmd=('What',None,'D, by rule or CAS')))
S.append(qslide('yt','You try · Edrolo 6C Worked example 1a','Finding the regular payment for an interest-only loan',
  '<div style="font-size:28px;margin-top:70px">Brock borrows $8000 in an interest-only loan at 3% per annum, compounding monthly.<br><br>a. <b>What</b> is the monthly amount that he will be required to pay?</div>',
  [('Principal and rate','V₀ = 8000, r = 3, p = 12'),('Substitute','d = 3 ÷ (12 × 100) × 8000 = 3 ÷ 1200 × 8000'),('Evaluate','d = 20')],
  'Brock will be required to pay <b>$20</b> each month.',f'{EDR} · 6C Worked example 1a (p. 375)',cmd=('What',None,'d = r ÷ (100p) × V₀')))

# ================= Ex 28
S.append(qslide('we','Worked example 28 · 8H','Finding the amount borrowed for an interest-only loan',
  '<div style="font-size:28px;margin-top:80px">A loan at 6% per annum, compounding monthly, requires payments of $440 each month.<br>If the loan is an interest-only loan, <b>what</b> is the principal?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','440 = 6 ÷ (100 × 12) × V₀ = 0.005 × V₀'),('Solve','V₀ = 440 ÷ 0.005 = 88 000')],
  'The principal is <b>$88 000</b>.',f'{CAM} · Example 28 (p. 449)',video='Cambridge GO · 8H Resources',cmd=('what',None,'solve for V₀')))
S.append(qslide('yt','You try · written for 12MAG','Finding the amount borrowed for an interest-only loan',
  '<div style="font-size:28px;margin-top:80px">A loan at 4.8% per annum, compounding monthly, requires payments of $600 each month. If the loan is an interest-only loan, <b>what</b> is the principal?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','600 = 4.8 ÷ (100 × 12) × V₀ = 0.004 × V₀'),('Solve','V₀ = 600 ÷ 0.004 = 150 000')],
  'The principal is <b>$150 000</b>.','Written for 12MAG (modelled on '+CAM+' Example 28) · YT-8H-28',cmd=('what',None,'solve for V₀')))

# ================= Ex 29
S.append(qslide('we','Worked example 29 · 8H','Finding the interest rate for an interest-only loan',
  '<div style="font-size:28px;margin-top:80px">An interest-only loan of $1 000 000 requires quarterly payments of $4000.<br><b>What</b> is the annual interest rate on the loan?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','4000 = r ÷ (100 × 4) × 1 000 000'),('Solve','r = 4000 × 400 ÷ 1 000 000 = 1.6')],
  'The annual interest rate is <b>1.6%</b>.',f'{CAM} · Example 29 (p. 449)',video='Cambridge GO · 8H Resources',cmd=('What',None,'solve for r')))
S.append(qslide('yt','You try · written for 12MAG','Finding the interest rate for an interest-only loan',
  '<div style="font-size:28px;margin-top:80px">An interest-only loan of $500 000 requires quarterly payments of $6250. <b>What</b> is the annual interest rate on the loan?</div>',
  [('Formula','D = r ÷ (100 × p) × V₀'),('Substitute','6250 = r ÷ (100 × 4) × 500 000'),('Solve','r = 6250 × 400 ÷ 500 000 = 5')],
  'The annual interest rate is <b>5%</b> per annum.','Written for 12MAG (modelled on '+CAM+' Example 29) · YT-8H-29',cmd=('What',None,'solve for r')))

# ================= Exit
S.append(qslide('ex','Exit task · VCAA 2021 Exam 1 Q24','Show what you know',
  '<div style="font-size:23px;margin-top:20px">Bob borrowed $400 000 to buy an apartment.<br>The interest rate for this loan was 3.14% per annum, compounding monthly.<br>A scheduled monthly repayment that allowed Bob to fully repay the loan in 20 years was determined.<br>Bob decided, however, to make interest-only repayments for the first two years.<br>After these two years the interest rate changed. Bob was still able to pay off the loan in the 20 years by repaying the scheduled amount each month.<br>The interest rate, per annum, for the final 18 years of the loan was closest to</div>',
  [('Scheduled',FS('240','3.14','400 000','?','0',12,'PMT')+' → −2246.528…'),
   ('After 2 years','interest-only: Bob still owes $400 000'),
   ('Final 18 years',FS('216','?','400 000','−2246.528…','0',12,'I')+' → I = 2.2116…')],
  'The new rate is about <b>2.21%</b> per annum: <b>B</b>.',f'VCAA 2021 Further Mathematics Exam 1 Q24 (examiner report) · {EDR} 6C Q13',
  stat=('mc',33),mc=['1.85%','2.21%','2.79%','3.14%','4.07%'],key='B',dist=[9,33,25,15,16]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8H' and v.get('url')]))
n=assemble(S,'12MAG · L44 · Interest-only loans',os.path.join(ROOT,'lessons','8H slides.html'))
print(n-1,'slides')
