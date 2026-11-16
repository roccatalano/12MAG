"""Lesson gm12-u4-11c (11C Transition matrices: using recursion) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/11C slides.html      Run: python3 tools/deck/gm12-u4-11c/build.py      Screenshots: python3 tools/deck/gm12-u4-11c/shoot.py
Matrices with tools/deck/mx.py (no figures needed: every question here is matrices or a table).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- CFAT 3.11.1 (11A-11B) opens the lesson.
- Do Now: VCAA 2024 Exam 1 Q25 (B, 79%; replaces the card's 2023 E1 Q27, which asks for the long-term state = today's new content) ·
          VCAA 2024 Exam 1 Q27 (B, 50%) · VCAA 2025 Exam 2 Q13 stem + Q13a (average 0.7/1) · VCAA 2025 Exam 2 Q5 stem + Q5a (average 1/2).
          % from tools/vcaa_current_index.csv (examiner reports).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4D #10 (p. 291) and 4H #18 (p. 293), solutions worked for 12MAG ·
       VCAA 2021 Exam 2 Matrices Q3 stem + Q3a (original wording; = Edrolo U1&2 5G Q12); 28% from the 2021 E2 report (card said 30).
- Learn: Cambridge U3&4 11C pp. 560-566 (own words) · Edrolo U3&4 7G p. 484, 7H p. 497.
- Worked examples: Cambridge U3&4 Examples 4-7 (pp. 561-566). You trys: Edrolo U3&4 7G WE5 (pp. 484-485), 7G WE7 (p. 485),
  7G WE6 (p. 485), 7H WE1 (p. 497).
- CAS: planner/cas-skills.json 'matrix-recurrence' on Cambridge Example 5 data (S10 = T^10 S0).
- Exits (original VCAA wording; Edrolo U3&4 7G Q19, 7G Q20, 7H Q12, 7H Q14):
  VCAA 2016 Further Exam 2 Matrices Q3 stem + Q3a (85%) · VCAA 2017 Further Exam 2 Matrices Q3a-d (47, 73, 12 (full marks), 43%) ·
  VCAA 2018 Further Exam 1 Matrices Q8 (B, 46%) · VCAA 2020 Further Exam 2 Matrices Q3 stem + Q3d (39%; graph for b, c left out).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-11c')
yid=lambda u:u.split('v=')[1].split('&')[0]
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def LT(m,top,side):
    return f'<span style="display:inline-flex;align-items:center;gap:8px"><span style="display:inline-flex;flex-direction:column;align-items:center"><i style="color:#0a7a8a">{top}</i>{m}</span><i style="color:#0a7a8a">{side}</i></span>'
def Sn(n): return f'<i>S</i><sub>{n}</sub>'
S=['<style>.sm .L .q{font-size:17px}.xs ol.parts li{font-size:18px!important;line-height:1.25}</style>']
# ================= opening
t=title('11C','Transition matrices: using recursion',f'{CAM} · 11C Transition matrices – using recursion','11C',flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks'))
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 3.11.1','· 11A–11B, 20 min','#00838F'),('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 skills','var(--apk)'),
  ('Step by step and Sₙ = TⁿS₀ · Examples 4, 5','→ You try ×2',None),('Going back a step · Example 6','→ You try',None),('Steady state · Example 7','→ You try',None),
  ('Exit tasks','· four VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('State matrix <i>S</i><sub><i>n</i></sub>','column matrix: how many (or what proportion) are in each state after <i>n</i> steps'),
  ('Recurrence relation','<i>S</i><sub>0</sub> = initial state, <i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub>: the next state = <i>T</i> × the current state'),
  ('Steady state (equilibrium)','the state matrix stops changing: <i>S</i><sub><i>n</i>+1</sub> ≈ <i>S</i><sub><i>n</i></sub> for large <i>n</i>')],
  [('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>T</i> <i>S</i><sub><i>n</i></sub>'),'one step at a time'),
   ('nth state',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup> <i>S</i><sub>0</sub>'),'jump straight to step n'),
   ('Step back',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup> <i>S</i><sub><i>n</i>+1</sub>'),'go back one step'),
   ('Steady state',F('<i>T</i><sup>50</sup><i>S</i><sub>0</sub> ≈ <i>T</i><sup>51</sup><i>S</i><sub>0</sub>'),'large n, two in a row agree')],
  f'{CAM}, 11C pp. 560–566; Study Design: matrix recurrence relations and the equilibrium state matrix'))
S.append(cfat('CFAT 3.11.1','Transition matrices and transition diagrams','11A–11B',13,'CFAT 3.11.1 (11A–11B) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now 1: VCAA 2024 E1 Q25 (10D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q25','Review of 10D (Ch 10)',
  '<div style="font-size:30px;margin-top:50px">Matrix <i>J</i> is a 2 × 3 matrix.<br>Matrix <i>K</i> is a 3 × 1 matrix.<br>Matrix <i>L</i> is added to the product <i>JK</i>.<br>The order of matrix <i>L</i> is</div>',
  [('Product JK','(2 × <b>3</b>)(<b>3</b> × 1): inner numbers match, so <i>JK</i> is 2 × 1'),('Adding','only matrices of the same order can be added, so <i>L</i> is 2 × 1')],
  '2 × 1: <b>B</b>.','VCAA 2024 General Mathematics Exam 1 Q25 (examiner report: 79% correct)',
  mc=['1 × 3','2 × 1','2 × 3','3 × 2'],key='B',stat=('mc',79)))
# ================= Do Now 2: VCAA 2024 E1 Q27 (10E)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q27','Review of 10E (Ch 10)',
  '<div style="font-size:30px;margin-top:50px">Consider the following matrix, where <i>h</i> ≠ 0.'+C(mat([[4,'<i>g</i>'],[8,'<i>h</i>']],fs=32))+
  'The inverse of this matrix does <b>not</b> exist when <i>g</i> is equal to</div>',
  [('No inverse','when the determinant = 0'),('det','4<i>h</i> − 8<i>g</i> = 0'),('Solve','8<i>g</i> = 4<i>h</i>, so <i>g</i> = <i>h</i>/2')],
  '<i>g</i> = <i>h</i>/2: <b>B</b>.','VCAA 2024 General Mathematics Exam 1 Q27 (examiner report: 50% correct)',
  mc=['−2<i>h</i>','<i>h</i>/2','<i>h</i>','2<i>h</i>'],key='B',dis=('D','2h comes from 8h − 4g = 0: the diagonals multiplied the wrong way'),stat=('mc',50)))
# ================= Do Now 3: VCAA 2025 E2 Q13a (11B)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q13a','Review of 11B (last lesson)',
  '<div style="font-size:24px;margin-top:20px">The early learning centre also offers a 10-week activity program for four-year-old children. There are 27 children enrolled in the program. They participate in three different activities over the 10 weeks. The activities are cooking (<i>C</i>), gardening (<i>G</i>) and music (<i>M</i>).<br>'
  'The transition matrix <i>K</i>, shown below, gives the expected proportion of children in the program who will change activities from one week to the next.'
  +C(EQ('<i>K</i> =',LT(mat([[0,0.76,0.36],[0.55,0,0.64],[0.45,0.24,0]],cl=['C','G','M'],rl=['C','G','M'],side=True,fs=24,tid='d3'),'this week','next week')))
  +'a. What do the values on the leading diagonal in matrix <i>K</i> indicate? <span class="muted">(1 mark)</span></div>',
  [('Leading diagonal','top left to bottom right: C → C, G → G, M → M (stay in the same activity)','data-hi="#d3|c0_0,c1_1,c2_2|hy"'),('Values','all 0')],
  'No child is expected to do the same activity two weeks in a row: every child changes activity each week.','VCAA 2025 General Mathematics Exam 2 Q13a (examiner report: average 0.7/1)',stat=('mark',70)))
# ================= Do Now 4: VCAA 2025 E2 Q5a (3A)
TB='<table class="dt" style="border-collapse:collapse;font-size:15px;margin:4px 0">'+'<tr><th style="border:1px solid #333;padding:2px 14px"><i>Sale price ($)</i></th><th style="border:1px solid #333;padding:2px 14px"><i>Days</i></th></tr>'+''.join(
  f'<tr><td style="border:1px solid #333;padding:1px 14px;text-align:center">{p}</td><td style="border:1px solid #333;padding:1px 14px;text-align:center">{d}</td></tr>' for p,d in
  [('950 000',15),('925 000',18),('900 000',23),('900 000',24),('905 000',26),('750 000',28),('680 000',31),('800 000',35),('590 000',46),('600 000',65)])+'</table>'
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 Exam 2 Q5a','Review of 3A (last term)',
  '<div style="font-size:19px">The table below shows <i>sale price</i> and the number of days on the market before sale, <i>days</i>, for a sample of 10 apartments sold in a particular suburb.'
  +C(TB)+'a. Use the data in the table above to find the equation of the least squares line.<br>Write your answers in the boxes below, rounding both values to four significant figures. <span class="muted">(2 marks)</span>'
  +C('<i>sale price</i> = ☐ + ☐ × <i>days</i>',gap=8)+'</div>',
  [('Variables','EV = <i>days</i> (x) · RV = <i>sale price</i> (y)'),('CAS','linear regression (a + bx): <i>a</i> = 1 050 360.6…, <i>b</i> = −8050.18…'),('Round','4 significant figures: 1 050 000 and −8050')],
  '<i>sale price</i> = <b>1 050 000</b> + (<b>−8050</b>) × <i>days</i>','VCAA 2025 General Mathematics Exam 2 Q5a (examiner report: average 1/2)',stat=('mark',50),cmd=('Use',None,'CAS regression, 4 s.f.')))
sm()

# ================= APK
A10=mat([[6,-11,3,7],[0,8,-2,8]],fs=26); B10=mat([[12,-3],[1,5],[4,-6],[10,-2]],fs=26)
S.append(qslide('apk','APK 1 · Year 11 · Cambridge U1&amp;2 4D #10','Matrix multiplication on CAS',
  '<div style="font-size:28px;margin-top:40px">Calculate the following matrix multiplication using a CAS calculator:'+C(EQ(A10,B10))+'</div>',
  [('Order','(2 × <b>4</b>)(<b>4</b> × 2): possible, answer is 2 × 2'),('CAS','store the matrices, multiply with ×')],
  mat([[143,-105],[80,36]],fs=26),f'{CAM12} · Ch 4 review skills checklist 4D #10 (p. 291) · solution worked for 12MAG'))
S.append(qslide('apk','APK 2 · Year 11 · Cambridge U1&amp;2 4H #18','Recursion with a state matrix',
  '<div style="font-size:28px;margin-top:40px">Consider the following matrices: one defining the initial populations in Geelong and Ballarat and the other, a transition matrix defining the proportion of the population moving between the two cities each year. Assume Geelong is listed first.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([['250 000'],['110 000']],fs=26)),EQ('<i>T</i> =',mat([[0.9,0.15],[0.1,0.85]],fs=26)))+'How many people are expected to be in Geelong after five years?</div>',
  [('Rule','<i>S</i><sub>5</sub> = <i>T</i><sup>5</sup><i>S</i><sub>0</sub> (or <i>TS</i><sub>0</sub>, then <i>T</i> × answer, five times)'),('CAS','<i>T</i><sup>5</sup><i>S</i><sub>0</sub> = '+mat([['224 068.4…'],['135 931.6…']],fs=20)),('Read','Geelong = row 1')],
  'About <b>224 068 people</b> in Geelong after five years.',f'{CAM12} · Ch 4 review skills checklist 4H #18 (p. 293) · solution worked for 12MAG'))
S.append(qslide('apk','APK 3 · VCAA 2021 Exam 2 Matrices Q3a','Reading a transition matrix',
  '<div style="font-size:22px">A market research study of shoppers showed that the buying preferences for the three olive oils, Carmani (<i>C</i>), Linelli (<i>L</i>) and Ohana (<i>O</i>), change from month to month according to the transition matrix <i>T</i> below.'
  +C(EQ('<i>T</i> =',LT(mat([['0.85','0.10','0.05'],['0.05','0.80','0.05'],['0.10','0.10','0.90']],cl=['C','L','O'],rl=['C','L','O'],side=True,fs=22,tid='a3'),'this month','next month')),
     EQ('<i>S</i><sub>0</sub> =',mat([[3200],[2000],[2800]],rl=['C','L','O'],side=True,fs=22)))
  +'The initial state matrix <i>S</i><sub>0</sub> above shows the number of shoppers who bought each brand of olive oil in July 2021.<br>Let <i>S</i><sub><i>n</i></sub> represent the state matrix describing the number of shoppers buying each brand <i>n</i> months after July 2021.<br>'
  'a. How many of these 8000 shoppers bought a different brand of olive oil in August 2021 from the brand bought in July 2021? <span class="muted">(1 mark)</span></div>',
  [('Change brand','everything OFF the leading diagonal: 1 − stay','data-hi="#a3|c1_0,c2_0,c0_1,c2_1,c0_2,c1_2|hy"'),
   ('Each column','C: 0.15 × 3200 = 480 · L: 0.20 × 2000 = 400 · O: 0.10 × 2800 = 280'),('Add','480 + 400 + 280 = 1160')],
  '<b>1160 shoppers</b> changed brand.','VCAA 2021 Further Mathematics Exam 2 Matrices Q3a (examiner report: 28%) · Edrolo U1&amp;2 5G Q12',stat=('mark',28)))
sm()

# ================= Learn 1: recursion step by step and S_n = T^n S_0
TL=mat([[0.8,0.1],[0.2,0.9]],fs=22); S0L=mat([[50],[40]],fs=22)
S.append(learn('Learn · 11C','Generating state matrices',
  '<h4>Start with S₀, then multiply by T again and again</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><i>S</i><sub>0</sub> = the starting numbers (a column matrix)</li>'
  '<li><i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub>, <i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub>, … always <i>T</i> on the LEFT</li>'
  '<li>a big jump: <i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub> on CAS</li>'
  '<li>the total stays the same every step (each column of <i>T</i> adds to 1)</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:12px;align-items:center;font-size:22px">'
  +EQ('<i>T</i> =',TL,'&nbsp; <i>S</i><sub>0</sub> =',S0L,'<span class="muted">(cars: Bendigo, Colac)</span>')
  +'<div class="frag">'+EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> =',TL,S0L,'=',mat([['0.8 × 50 + 0.1 × 40'],['0.2 × 50 + 0.9 × 40']],fs=20),'=',mat([[44],[46]],fs=22))+'</div>'
  +'<div class="frag">'+EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub> =',TL,mat([[44],[46]],fs=22),'=',mat([[39.8],[50.2]],fs=22))+'</div>'
  +'<div class="frag">'+EQ('<i>S</i><sub>10</sub> = <i>T</i><sup>10</sup><i>S</i><sub>0</sub> =',mat([[30.6],[59.4]],fs=22),'<span class="muted">(CAS)</span>')+'</div></div>',
  'Write T × S (T first). S × T does not even multiply for a 2 × 2 and a 2 × 1.',f'{CAM}, 11C pp. 560–563 (own words) · {EDR}, 7G p. 484',
  cards=(kcard('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub>')),kcard('nth state',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub>')))))

# ================= Ex 4 / You try 7G WE5
T4=mat([[0.85,0.05],[0.15,0.95]],fs=24); S04=mat([[80],[20]],fs=24)
S.append(qslide('we','Worked example 4 · 11C','Calculating state matrices step by step',
  '<div style="font-size:24px;margin-top:20px">The factory has a large number of machines. The machines can be in one of two states: operating (<i>O</i>) or broken (<i>B</i>). Broken machines are repaired and come back into operation and vice versa.<br>'
  'At the start, 80 machines are operating and 20 are broken.<br>Use the recursion relation'+C('<i>S</i><sub>0</sub> = intial value, <i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub>')+'where'
  +C(EQ('<i>S</i><sub>0</sub> =',S04,'and <i>T</i> =',T4))+'to determine the number of operational and broken machines after 1 day and after 3 days.</div>',
  [('S₁',EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> =',mat([[0.85,0.05],[0.15,0.95]],fs=17),mat([[80],[20]],fs=17),'=',mat([[69],[31]],fs=17))),
   ('ANS','After 1 day, 69 machines are operational and 31 are broken.'),
   ('S₂',EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub> =',mat([[0.85,0.05],[0.15,0.95]],fs=17),mat([[69],[31]],fs=17),'=',mat([[60.2],[39.8]],fs=17))),
   ('S₃',EQ('<i>S</i><sub>3</sub> = <i>TS</i><sub>2</sub> =',mat([[0.85,0.05],[0.15,0.95]],fs=17),mat([[60.2],[39.8]],fs=17),'=',mat([[53.16],[46.84]],fs=17))),
   ('ANS','After 3 days, 53 machines are operating and 47 are broken.')],
  '',f'{CAM} · Example 4 (p. 561)',video='Cambridge GO · Example 4 (11C Resources)'))
S.append(qslide('yt','You try 1 · Edrolo 7G WE5','Calculating state matrices step by step',
  '<div style="font-size:24px;margin-top:20px">Every night, a colony of seals can settle on either island A or island B. On Sunday, there were 130 seals on island A and 180 seals on island B.<br>The initial state and transition matrices are provided.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[130],[180]],rl=['A','B'],side=True,fs=24)),EQ('<i>T</i> =',LT(mat([[0.2,0.6],[0.8,0.4]],cl=['A','B'],rl=['A','B'],side=True,fs=24),'today','tomorrow')))
  +plist([('a','Determine the matrix recurrence relation that can be used to calculate the number of seals on each island every day.'),
          ('b','Use recursion to calculate the number of seals on each island on Tuesday, rounded to the nearest whole number.')])+'</div>',
  [('a','substitute <i>S</i><sub>0</sub> and <i>T</i> into <i>S</i><sub>0</sub> = initial state, <i>S</i><sub><i>n</i>+1</sub> = <i>T</i> × <i>S</i><sub><i>n</i></sub>'),
   ('b: Monday',EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> =',mat([[134],[176]],fs=17))),('b: Tuesday',EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub> =',mat([[132.4],[177.6]],fs=17)))],
  '',f'{EDR} · 7G Worked example 5 (pp. 484–485)',
  parts=[('a',EQ('<i>S</i><sub>0</sub> =',mat([[130],[180]],fs=17),', <i>S</i><sub><i>n</i>+1</sub> =',mat([[0.2,0.6],[0.8,0.4]],fs=17),'× <i>S</i><sub><i>n</i></sub>')),('b','Island A: <b>132 seals</b> · Island B: <b>178 seals</b>')]))

# ================= Ex 5 / CAS / You try 7G WE7
S.append(qslide('we','Worked example 5 · 11C','The nth state: Sₙ = TⁿS₀',
  '<div style="font-size:26px;margin-top:30px">The factory has a large number of machines. The machines can be in one of two states: operating (<i>O</i>) or broken (<i>B</i>). Broken machines are repaired and come back into operation and vice versa.<br>'
  'Initially, 80 machines are operating and 20 are broken, so:'+C(EQ('<i>S</i><sub>0</sub> =',S04,'and <i>T</i> =',T4))+'Determine the number of operational and broken machines after 10 days.</div>',
  [('Rule','<i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub>, so <i>S</i><sub>10</sub> = <i>T</i><sup>10</sup><i>S</i><sub>0</sub>'),
   ('CAS','store <i>T</i> → t and <i>S</i><sub>0</sub> → s, then t<sup>10</sup> · s = '+mat([['30.9056'],['69.0944']],fs=18)),
   ('Round',EQ('<i>S</i><sub>10</sub> =',mat([[30.9],[69.1]],fs=18)))],
  'After 10 days, <b>31 machines</b> will be operational and <b>69 broken</b>.',f'{CAM} · Example 5 (p. 563)',video='Cambridge GO · Example 5 (11C Resources)'))
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-recurrence']
S.append(cas('CAS · 11C','State matrices on CAS: Sₙ = TⁿS₀ and the steady state',
  '<div style="font-size:24px">Example 5 on CAS:</div>'+C(EQ('<i>T</i> =',T4),EQ('<i>S</i><sub>0</sub> =',S04))+'<div style="font-size:24px">Find <i>S</i><sub>10</sub>, then <i>S</i><sub>50</sub> and <i>S</i><sub>51</sub>.</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'][:4],CS['classpad'][:4],EQ('<i>S</i><sub>10</sub> =',mat([[30.9],[69.1]],fs=16),' · <i>S</i><sub>50</sub> = <i>S</i><sub>51</sub> =',mat([[25.0],[75.0]],fs=16),'(steady state)'),
  f'{CAM} · Example 5 (p. 563) · Steps: CAS guide (planner)'))
S.append(qslide('yt','You try 2 · Edrolo 7G WE7','The nth state: Sₙ = TⁿS₀',
  '<div style="font-size:30px;margin-top:50px">Consider the following initial state matrix and transition matrix.'+C(EQ('<i>S</i><sub>0</sub> =',mat([[213],[142]],fs=30)),EQ('<i>T</i> =',mat([[0.3,0.9],[0.7,0.1]],fs=30)))
  +'Determine <i>S</i><sub>10</sub>, rounding the matrix elements to the nearest whole number.</div>',
  [('Rule','<i>S</i><sub>10</sub> = <i>T</i><sup>10</sup> × <i>S</i><sub>0</sub>'),('CAS',EQ(mat([[0.3,0.9],[0.7,0.1]],fs=17),'<sup>10</sup> ×',mat([[213],[142]],fs=17),'=',mat([['199.76…'],['155.23…']],fs=17)))],
  EQ('<i>S</i><sub>10</sub> =',mat([[200],[155]],fs=22)),f'{EDR} · 7G Worked example 7 (p. 485)'))

# ================= Ex 6 / You try 7G WE6 (inverse)
S.append(learn('Learn · 11C','Going back a step: the inverse',
  '<h4>Undo T by multiplying by T⁻¹ (on the left)</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> → <i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup><i>S</i><sub><i>n</i>+1</sub></li>'
  '<li>two steps back: (<i>T</i><sup>−1</sup>)<sup>2</sup></li><li><i>T</i><sup>−1</sup> is NOT a transition matrix (it can have negatives)</li></ul>',
  '<div style="text-align:center;font-size:30px">'+Sn(0)+' → '+Sn(1)+' → '+Sn(2)+' → … → '+Sn('<i>n</i>')+' → '+Sn('<i>n</i>+1')+'</div>'
  '<div class="frag" style="text-align:center;font-size:22px;margin-top:14px">× <i>T</i> moves right · × <i>T</i><sup>−1</sup> moves left</div>',
  'Pre-multiply: T⁻¹ goes on the LEFT of the state matrix.',f'{CAM}, 11C p. 563 (own words) · {EDR}, 7G p. 484',
  cards=(kcard('Step back',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup><i>S</i><sub><i>n</i>+1</sub>')),)))
T6=mat([[0.6,0.3],[0.4,0.7]],fs=24)
TI6=mat([['7/3',-1],['−4/3',2]],fs=17)
S.append(qslide('we','Worked example 6 · 11C','Using the inverse of a transition matrix',
  '<div style="font-size:30px;margin-top:50px">We have a transition matrix'+C(EQ('<i>T</i> =',T6))+'and we know that the state matrix'+C(EQ('<i>S</i><sub>4</sub> =',mat([['25 587'],['34 413']],fs=28)))+'Determine <i>S</i><sub>3</sub> and <i>S</i><sub>2</sub>.</div>',
  [('Rearrange','<i>S</i><sub>4</sub> = <i>TS</i><sub>3</sub>, so <i>S</i><sub>3</sub> = <i>T</i><sup>−1</sup><i>S</i><sub>4</sub>'),
   ('T⁻¹',EQ('<i>T</i><sup>−1</sup> =',TI6,'<span class="muted">(hold it in CAS)</span>')),
   ('S₃',EQ('<i>S</i><sub>3</sub> = <i>T</i><sup>−1</sup>',mat([['25 587'],['34 413']],fs=17),'=',mat([['25 290'],['34 710']],fs=17))),
   ('S₂',EQ('<i>S</i><sub>2</sub> = <i>T</i><sup>−1</sup>',mat([['25 290'],['34 710']],fs=17),'=',mat([['24 300'],['35 700']],fs=17)))],
  EQ('<i>S</i><sub>3</sub> =',mat([['25 290'],['34 710']],fs=20),', <i>S</i><sub>2</sub> =',mat([['24 300'],['35 700']],fs=20)),f'{CAM} · Example 6 (p. 564)',video='Cambridge GO · Example 6 (11C Resources)'))
S.append(qslide('yt','You try 3 · Edrolo 7G WE6','Using the inverse of a transition matrix',
  '<div style="font-size:30px;margin-top:50px">Consider the following state matrix after 3 periods, <i>S</i><sub>3</sub>, and transition matrix, <i>T</i>.'
  +C(EQ('<i>S</i><sub>3</sub> =',mat([[120],[150]],fs=30)),EQ('<i>T</i> =',mat([[0.84,0.21],[0.16,0.79]],fs=30)))+'Determine <i>S</i><sub>2</sub>, rounding the matrix elements to the nearest whole number.</div>',
  [('Rearrange','<i>S</i><sub>3</sub> = <i>T</i> × <i>S</i><sub>2</sub>; pre-multiply both sides by <i>T</i><sup>−1</sup>: <i>S</i><sub>2</sub> = <i>T</i><sup>−1</sup> × <i>S</i><sub>3</sub>'),
   ('CAS',EQ(mat([[0.84,0.21],[0.16,0.79]],fs=17),'<sup>−1</sup> ×',mat([[120],[150]],fs=17),'=',mat([['100.47…'],['169.52…']],fs=17)))],
  EQ('<i>S</i><sub>2</sub> =',mat([[100],[170]],fs=22)),f'{EDR} · 7G Worked example 6 (p. 485)'))

# ================= Learn 3 + Ex 7 / You try 7H WE1 (steady state)
ROWS=[('0',50,40),('1',44,46),('2',39.8,50.2),('3',36.9,53.1),('…','…','…'),('12',30.3,59.7),('13',30.2,59.8),('14',30.1,59.9),('15',30.1,59.9)]
TBL='<table style="border-collapse:collapse;font-size:19px">'+'<tr><th style="border:1px solid #999;padding:4px 8px">Week</th>'+''.join(f'<td style="border:1px solid #999;padding:4px 8px;text-align:center">{w}</td>' for w,_,_ in ROWS)+'</tr><tr><th style="border:1px solid #999;padding:4px 8px">State</th>'+''.join(f'<td style="border:1px solid #999;padding:4px 6px">{mat([[a],[b]],fs=16) if a!="…" else "…"}</td>' for _,a,b in ROWS)+'</tr></table>'
S.append(learn('Learn · 11C','The steady-state solution',
  '<h4>For large n the state matrix stops changing</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>find <i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub> for a large <i>n</i> (e.g. 50)</li>'
  '<li>check the next one (51): if they agree (to the accuracy asked), that is the steady state</li>'
  '<li>‘in the long term’ = steady state</li></ul>',
  '<div style="display:flex;flex-direction:column;align-items:center;gap:10px">'+TBL+'<div class="frag" style="font-size:22px">rental cars (Bendigo, Colac): settles at about <b>30</b> and <b>60</b></div></div>',
  'Two successive state matrices must agree before you call it the steady state.',f'{CAM}, 11C pp. 564–566 (own words; table p. 564) · {EDR}, 7H p. 497',
  cards=(kcard('Steady state',F('<i>S</i><sub><i>n</i>+1</sub> ≈ <i>S</i><sub><i>n</i></sub>')),)))
S.append(qslide('we','Worked example 7 · 11C','Estimating the steady-state solution',
  '<div style="font-size:30px;margin-top:50px">For the car rental problem:'+C(EQ('<i>S</i><sub>0</sub> =',mat([[50],[40]],fs=30),'and <i>T</i> =',mat([[0.8,0.1],[0.2,0.9]],fs=30)))
  +'Estimate the steady-state solution by calculating <i>S</i><sub><i>n</i></sub> for <i>n</i> = 10, 15, 17 and 18.</div>',
  [('Rule','<i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub>'),
   ('CAS',EQ('<i>T</i><sup>10</sup><i>S</i><sub>0</sub> =',mat([['30.565'],['59.435']],fs=16),' <i>T</i><sup>15</sup><i>S</i><sub>0</sub> =',mat([['30.095'],['59.905']],fs=16))),
   ('CAS',EQ('<i>T</i><sup>17</sup><i>S</i><sub>0</sub> =',mat([['30.047'],['59.953']],fs=16),' <i>T</i><sup>18</sup><i>S</i><sub>0</sub> =',mat([['30.033'],['59.967']],fs=16))),
   ('Round (1 d.p.)',EQ('<i>S</i><sub>15</sub> =',mat([[30.1],[59.9]],fs=16),', <i>S</i><sub>17</sub> =',mat([['30.0'],['60.0']],fs=16),', <i>S</i><sub>18</sub> =',mat([['30.0'],['60.0']],fs=16)))],
  'The estimated steady-state solution is <b>30 cars</b> based in Bendigo and <b>60 cars</b> based in Colac.',f'{CAM} · Example 7 (p. 566)',video='Cambridge GO · Example 7 (11C Resources)'))
S.append(qslide('yt','You try 4 · Edrolo 7H WE1','Estimating the steady-state solution',
  '<div style="font-size:30px;margin-top:60px">If '+EQ('<i>S</i><sub>0</sub> =',mat([[29],[32]],fs=30),'and <i>T</i> =',mat([[0.7,0.2],[0.3,0.8]],fs=30))+', calculate the equilibrium state matrix.</div>',
  [('Large n',EQ('<i>S</i><sub>30</sub> = <i>T</i><sup>30</sup> × <i>S</i><sub>0</sub> =',mat([[24.4],[36.6]],fs=17))),
   ('Check',EQ('<i>S</i><sub>31</sub> = <i>T</i><sup>31</sup> × <i>S</i><sub>0</sub> =',mat([[24.4],[36.6]],fs=17),': equal, so this is the equilibrium'))],
  EQ('Equilibrium state matrix =',mat([[24.4],[36.6]],fs=22)),f'{EDR} · 7H Worked example 1 (p. 497)'))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 4 · VCAA 2016 Exam 2 Q3a','Show what you know',
  '<div style="font-size:17px">The travel company is studying the choice between air (<i>A</i>), land (<i>L</i>), sea (<i>S</i>) or no (<i>N</i>) travel by some of its customers each year.<br>'
  'Matrix <i>T</i>, shown below, contains the percentages of customers who are expected to change their choice of travel from year to year.'
  +C(EQ('<i>T</i> =',LT(mat([['0.65','0.25','0.25','0.50'],['0.15','0.60','0.20','0.15'],['0.05','0.10','0.25','0.20'],['0.15','0.05','0.30','0.15']],cl=['A','L','S','N'],rl=['A','L','S','N'],side=True,fs=16,tid='x1'),'this year','next year')))
  +'Let <i>S</i><sub><i>n</i></sub> be the matrix that shows the number of customers who choose each type of travel <i>n</i> years after 2014.<br>Matrix <i>S</i><sub>0</sub> below shows the number of customers who chose each type of travel in 2014.<br>'
  'Matrix <i>S</i><sub>1</sub> below shows the number of customers who chose each type of travel in 2015.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[520],[320],[80],[80]],rl=['A','L','S','N'],side=True,fs=15)),EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> =',mat([[478],['<i>d</i>'],['<i>e</i>'],['<i>f</i>']],rl=['A','L','S','N'],side=True,fs=15)),gap=60)
  +'a. Write the values missing from matrix <i>S</i><sub>1</sub> (<i>d</i>, <i>e</i>, <i>f</i>) in the boxes provided below. <span class="muted">(1 mark)</span></div>',
  [('d (row L)','0.15 × 520 + 0.60 × 320 + 0.20 × 80 + 0.15 × 80 = 298','data-hi="#x1|c1_0,c1_1,c1_2,c1_3|hy"'),
   ('e (row S)','0.05 × 520 + 0.10 × 320 + 0.25 × 80 + 0.20 × 80 = 94','data-hi="#x1|c2_0,c2_1,c2_2,c2_3|hb"'),
   ('f (row N)','0.15 × 520 + 0.05 × 320 + 0.30 × 80 + 0.15 × 80 = 130','data-hi="#x1|c3_0,c3_1,c3_2,c3_3|hg"')],
  '<i>d</i> = <b>298</b>, <i>e</i> = <b>94</b>, <i>f</i> = <b>130</b>','VCAA 2016 Further Mathematics Exam 2 Matrices Q3a (examiner report: 85%) · Edrolo U3&amp;4 7G Q19',stat=('mark',85),cmd=('Write',None,'three values')))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
T17=lambda tid:mat([[0.4,0.2,0.3,0.1],[0.2,0.4,0.1,0.3],[0.2,0.3,0.3,0.4],[0.2,0.1,0.3,0.2]],cl=['C','I','P','S'],rl=['C','I','P','S'],side=True,fs=17,tid=tid)
X2=lambda tid,pl:('<div style="font-size:18px">Senior students at this school will also choose one elective activity in each of the four terms in 2018.<br>Their choices are communication (<i>C</i>), investigation (<i>I</i>), problem-solving (<i>P</i>) and service (<i>S</i>).<br>'
  'The transition matrix <i>T</i> shows the way in which senior students are expected to change their choice of elective activity from term to term.'
  +'<br>Let <i>S</i><sub><i>n</i></sub> be the state matrix for the number of senior students expected to choose each elective activity in Term <i>n</i>.<br>For the given matrix <i>S</i><sub>1</sub>, a matrix rule that can be used to predict the number of senior students in each elective activity in Terms 2, 3 and 4 is'
  +C(EQ('<i>T</i> =',LT(T17(tid),'this term','next term')),EQ('<i>S</i><sub>1</sub> =',mat([[300],[200],[200],[300]],fs=14),', &nbsp; <i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub>'),gap=30)+plist(pl)+'</div>')
SRC17='VCAA 2017 Further Mathematics Exam 2 Matrices Q3 (examiner report: a 47%, b 73%, c 12% full marks, d 43%) · Edrolo U3&amp;4 7G Q20'
S.append(qslide('ex','Exit task 2 of 4 (a, b) · VCAA 2017 Exam 2 Q3','Show what you know',
  X2('x2',[('a','How many senior students will <b>not</b> change their elective activity from Term 1 to Term 2? <span class="muted">(1 mark)</span>'),
          ('b','Complete <i>S</i><sub>2</sub>, the state matrix for Term 2, below. <span class="muted">(1 mark)</span>')]),
  [('a: diagonal','stay = leading diagonal × each column total','data-hi="#x2|c0_0,c1_1,c2_2,c3_3|hy"'),
   ('b',EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub>: row C = 0.4 × 300 + 0.2 × 200 + 0.3 × 200 + 0.1 × 300 = 250, …'))],
  '',SRC17,
  parts=[('a','0.4 × 300 + 0.4 × 200 + 0.3 × 200 + 0.2 × 300 = <b>320</b>'),('b',EQ('<i>S</i><sub>2</sub> =',mat([[250],[250],[300],[200]],rl=['C','I','P','S'],side=True,fs=15)))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
S.append(qslide('ex','Exit task 2 of 4 (c, d) · VCAA 2017 Exam 2 Q3','Show what you know',
  X2('x2b',[('c','Of the senior students expected to choose investigation (<i>I</i>) in Term 3, what percentage chose service (<i>S</i>) in Term 2? <span class="muted">(2 marks)</span>'),
          ('d','What is the maximum number of senior students expected in investigation (<i>I</i>) at any time during 2018? <span class="muted">(1 mark)</span>')]),
  [('c',EQ('<i>S</i><sub>3</sub> = <i>TS</i><sub>2</sub> =',mat([[260],[240],[295],[205]],fs=14),': 240 in <i>I</i>; from <i>S</i>: 0.3 × 200 = 60'),'data-hi="#x2b|c1_3|hy"'),
   ('d','<i>I</i>: Term 1 200, Term 2 250, Term 3 240, Term 4 239 (the steady state, 239, is not the maximum)')],
  '',SRC17,parts=[('c','60 ÷ 240 = <b>25%</b>'),('d','<b>250</b> (Term 2)')]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
S.append(qslide('ex','Exit task 3 of 4 · VCAA 2018 Exam 1 Q8','Show what you know',
  '<div style="font-size:16px">A public library organised 500 of its members into five categories according to the number of books each member borrows each month.<br>These categories are<br>'
  '<span style="margin-left:40px"><i>J</i> = no books borrowed per month</span><br><span style="margin-left:40px"><i>K</i> = one book borrowed per month</span><br><span style="margin-left:40px"><i>L</i> = two books borrowed per month</span><br>'
  '<span style="margin-left:40px"><i>M</i> = three books borrowed per month</span><br><span style="margin-left:40px"><i>N</i> = four or more books borrowed per month</span><br>'
  'The transition matrix, <i>T</i>, below shows how the number of books borrowed per month by the members is expected to change from month to month.'
  +C(EQ('<i>T</i> =',LT(mat([[0.1,0.2,0.2,0,0],[0.5,0.2,0.3,0.1,0],[0.3,0.3,0.4,0.1,0.2],[0.1,0.2,0.1,0.6,0.3],[0,0.1,0,0.2,0.5]],cl=list('JKLMN'),rl=list('JKLMN'),side=True,fs=14),'this month','next month')))
  +'In the long term, which category is expected to have approximately 96 members each month?</div>',
  [('Long term','= steady state: <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub> for large <i>n</i>'),
   ('S₀','not given: any start with 500 members works (e.g. 100 in each)'),
   ('CAS','<i>T</i><sup>50</sup><i>S</i><sub>0</sub> = <i>T</i><sup>51</sup><i>S</i><sub>0</sub> ≈ '+mat([[49],[96],[124],[151],[80]],rl=list('JKLMN'),side=True,fs=14))],
  'Category <i>K</i> (about 96 members): <b>B</b>.','VCAA 2018 Further Mathematics Exam 1 Matrices Q8 (examiner report: 46% correct) · Edrolo U3&amp;4 7H Q12',
  mc=['<i>J</i>','<i>K</i>','<i>L</i>','<i>M</i>','<i>N</i>'],key='B',stat=('mc',46)))
sm()
S.append(qslide('ex','Exit task 4 of 4 · VCAA 2020 Exam 2 Q3d','Show what you know',
  '<div style="font-size:16px">An offer to buy the Westmall shopping centre was made by a competitor.<br>One market research project suggested that if the Westmall shopping centre were sold, each of the three centres (Westmall, Grandmall and Eastmall) would continue to have regular shoppers but would attract and lose shoppers on a weekly basis.<br>'
  'Let <i>S</i><sub><i>n</i></sub> be the state matrix that shows the expected number of shoppers at each of the three centres <i>n</i> weeks after Westmall is sold.<br>A matrix recurrence relation that generates values of <i>S</i><sub><i>n</i></sub> is'
  +C('<i>S</i><sub><i>n</i>+1</sub> = <i>T</i> × <i>S</i><sub><i>n</i></sub>')
  +C(EQ('where <i>T</i> =',LT(mat([['0.80','0.09','0.10'],['0.12','0.79','0.10'],['0.08','0.12','0.80']],cl=['W','G','E'],rl=['W','G','E'],side=True,fs=16),'this week','next week')),EQ('<i>S</i><sub>0</sub> =',mat([['250 000'],['230 000'],['200 000']],rl=['W','G','E'],side=True,fs=16)),gap=20)
  +'d. In the long term, what is the expected weekly number of shoppers at Westmall?<br>Round your answer to the nearest whole number. <span class="muted">(1 mark)</span></div>',
  [('Long term','steady state: try a large <i>n</i>'),('CAS',EQ('<i>T</i><sup>100</sup><i>S</i><sub>0</sub> = <i>T</i><sup>101</sup><i>S</i><sub>0</sub> =',mat([['218 884.1…'],['233 476.4…'],['227 639.5…']],fs=15))),('Round','Westmall = row 1 → 218 884')],
  '<b>218 884</b> shoppers per week at Westmall in the long term.','VCAA 2020 Further Mathematics Exam 2 Matrices Q3d (examiner report: 39%) · Edrolo U3&amp;4 7H Q14',stat=('mark',39),cmd=('Round',None,'nearest whole number')))
sm()

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 11 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='11C' and v.get('url')]))
n=assemble(S,'12MAG · 11C · Transition matrices: using recursion',os.path.join(ROOT,'lessons','11C slides.html'))
print(n-1,'slides')
