"""Lesson gm12-u4-11d (11D Transition matrices: using the rule Sn+1 = TSn + B) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/11D slides.html      Run: python3 tools/deck/gm12-u4-11d/build.py      Screenshots: python3 tools/deck/gm12-u4-11d/shoot.py
Matrices with tools/deck/mx.py; transition diagrams cropped verbatim from the VCAA papers (fig/).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- No CFAT (CFAT 3.11.2 opens the Ch 11 test lesson).
- Do Now: VCAA 2023 Exam 1 Q32 (C, 18%; replaces the card's 2024 E1 Q32, which uses Sn+1 = TSn + A = today's new content) ·
          VCAA 2025 Exam 1 Q15 (B, 81%) · VCAA 2024 Exam 2 Q12 stem + Q12a (average 0.3/1) · VCAA 2023 Exam 2 Q10 stem + Q10a (average 0.7/1).
          % from tools/vcaa_current_index.csv (examiner reports).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4H #19 (p. 293; uses the 4H #18 matrices), solution worked for 12MAG.
- Learn: Cambridge U3&4 11D pp. 570-571 (own words) · Edrolo U3&4 7I p. 506.
- Worked example: Cambridge U3&4 Example 8 (pp. 570-571). You try: Edrolo U3&4 7I Worked example 3 (pp. 506-507).
- CAS: planner/cas-skills.json 'matrix-recurrence' (with B) on Cambridge Example 8 data.
- Exit (original VCAA wording; Edrolo U3&4 7I Q15): VCAA 2017 Further Exam 1 Matrices Q7 (A, 36% from the 2017 E1 report).
"""
import os, sys, json, base64
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-11d')
yid=lambda u:u.split('v=')[1].split('&')[0]
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def LT(m,top,side):
    return f'<span style="display:inline-flex;align-items:center;gap:8px"><span style="display:inline-flex;flex-direction:column;align-items:center"><i style="color:#0a7a8a">{top}</i>{m}</span><i style="color:#0a7a8a">{side}</i></span>'
def Sn(n): return f'<i>S</i><sub>{n}</sub>'
S=['<style>.sm .L .q{font-size:17px}.xs ol.parts li{font-size:18px!important;line-height:1.25}</style>']
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
B_=lambda n:f'<i>S</i><sub>{n}</sub>'
# ================= opening
t=title('11D','Transition matrices: using the rule Sₙ₊₁ = TSₙ + B',f'{CAM} · 11D Transition matrices – using the rule Sn+1 = TSn + B','11D',flow=('Do Now','APK','Learn','Worked example','You try','CAS','Exit task'))
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill','var(--apk)'),
  ('Adding and removing each step · Example 8','→ You try',None),('CAS','· T × ans + B',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Matrix <i>B</i>','column matrix (same order as <i>S</i><sub><i>n</i></sub>): the number added (+, restocking) or removed (−, culling) in each state every step'),
  ('Culling','removing animals from a population: negative elements in <i>B</i>'),
  ('Restocking','adding to a population: positive elements in <i>B</i>')],
  [('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>T</i> <i>S</i><sub><i>n</i></sub> + <i>B</i>'),'one step at a time'),
   ('Step back',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup>(<i>S</i><sub><i>n</i>+1</sub> − <i>B</i>)'),'take B away first'),
   ('No shortcut',F('<i>S</i><sub><i>n</i></sub> ≠ <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub> + <i>B</i>'),'work step by step')],
  f'{CAM}, 11D pp. 570–571; Study Design: S₀ = initial state matrix, Sₙ₊₁ = TSₙ + B, culling and restocking'))

# ================= Do Now 1: VCAA 2023 E1 Q32 (11C)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q32','Review of 11C (last lesson)',
  '<div style="font-size:15px;display:flex;gap:14px;align-items:center"><div style="flex:1">For one particular week in a school year, students at Phyllis Island Primary School can spend their lunch break at the playground (<i>P</i>), basketball courts (<i>B</i>), oval (<i>O</i>) or the library (<i>L</i>).<br>'
  'Students stay at the same location for the entire lunch break.<br>The transition diagram below shows the proportion of students who change location from one day to the next.<br>'
  'The transition diagram is incomplete.<br>On the Monday, 150 students spent their lunch break at the playground, 50 students spent it at the basketball courts, 220 students spent it at the oval, and 40 students spent it in the library.<br>'
  'Of the students expected to spend their lunch break on the oval on the Wednesday, the percentage of these students who also spent their lunch break on the oval on Tuesday is closest to</div>'+IMG('dn1.png',250)+'</div>',
  [('Complete','O → O = 1 − (0.30 + 0.10 + 0.30) = 0.30 (P, B, L loops too)'),
   ('Tuesday','O: 0.40 × 150 + 0.20 × 50 + 0.30 × 220 + 0.10 × 40 = 140'),
   ('Wednesday',EQ(B_(2)+' = <i>T</i>'+B_(1)+': O = 0.40 × 132 + 0.20 × 134 + 0.30 × 140 + 0.10 × 54 = 127')),
   ('Stayed on O','0.30 × 140 = 42, and 42 ÷ 127 = 33.1%')],
  '33%: <b>C</b>.','VCAA 2023 General Mathematics Exam 1 Q32 (examiner report: 18% correct)',
  mc=['27%','30%','33%','47%','52%'],key='C',dis=('B','30% is the O → O proportion: it ignores who else arrives on the oval on Wednesday'),stat=('mc',18)))
sm()
# ================= Do Now 2: VCAA 2025 E1 Q15 (5B)
DR=[146,98,120,176,145,78,187,106,166,124]
TBD='<table style="border-collapse:collapse;font-size:22px;margin:8px auto"><tr><th style="border:1px solid #333;padding:4px 10px">Day</th>'+''.join(f'<td id="dd{i}" style="border:1px solid #333;padding:4px 10px;text-align:center">{i+1}</td>' for i in range(10))+'</tr><tr><th style="border:1px solid #333;padding:4px 10px">Drinks</th>'+''.join(f'<td style="border:1px solid #333;padding:4px 10px;text-align:center">{d}</td>' for d in DR)+'</tr></table>'
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q15','Review of 5B (last term)',
  '<div style="font-size:26px;margin-top:40px">The number of drinks sold daily by a juice bar, <i>drinks</i>, over a 10-day period is shown in the table below.'+TBD+'The four-mean smoothed number of drinks, with centring, sold on day 8 is closest to</div>',
  [('Mean 1','days 6–9: (78 + 187 + 106 + 166) ÷ 4 = 134.25'),('Mean 2','days 7–10: (187 + 106 + 166 + 124) ÷ 4 = 145.75'),('Centre','(134.25 + 145.75) ÷ 2 = 140.0')],
  '140.0: <b>B</b>.','VCAA 2025 General Mathematics Exam 1 Q15 (examiner report: 81% correct)',
  mc=['134.25','140.0','142.75','145.75'],key='B',dis=('A','134.25 is only the first of the two four-mean values: no centring'),stat=('mc',81)))
# ================= Do Now 3: VCAA 2024 E2 Q12a (11C)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q12a','Review of 11C (last lesson)',
  '<div style="font-size:16px">When the construction company established the construction site at the beginning of 2023, it employed 390 staff to work on the site.<br>'
  'The staff comprised 330 construction workers (<i>C</i>), 50 foremen (<i>F</i>) and 10 managers (<i>M</i>).<br>At the beginning of each year, staff can choose to stay in the same job, move to a different job on the site, or leave the site (<i>L</i>) and not return.<br>'
  'The transition diagram below shows the proportion of staff who are expected to change their job at the site each year.'
  +'<div style="display:flex;gap:16px;align-items:center">'+IMG('dn3.png',330)+'<div style="flex:1">This situation can be modelled by the recurrence relation<br><i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub>, where'
  +C(EQ('<i>T</i> is the transitional matrix, <i>S</i><sub>0</sub> =',mat([[330],[50],[10],[0]],rl=list('CFML'),side=True,fs=14)))+'and <i>n</i> is the number of years after 2023.</div></div>'
  +'a. Calculate the predicted percentage decrease in the number of foremen (<i>F</i>) on the site from 2023 to 2025. <span class="muted">(1 mark)</span></div>',
  [('2024','F: 0.2 × 330 + 0.2 × 50 + 0.4 × 10 = 80 (C: 109, M: 13)'),('2025','F: 0.2 × 109 + 0.2 × 80 + 0.4 × 13 = 43'),('% change','(50 − 43) ÷ 50 × 100 = 14%')],
  'The number of foremen is predicted to decrease by <b>14%</b>.','VCAA 2024 General Mathematics Exam 2 Q12a (examiner report: average 0.3/1)',stat=('mark',30),cmd=('Calculate',None,'2 steps, then %')))
sm()
# ================= Do Now 4: VCAA 2023 E2 Q10a (10F)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q10a','Review of 10F (Ch 10)',
  '<div style="font-size:19px">Within the circus, there are different types of employees: directors (<i>D</i>), managers (<i>M</i>), performers (<i>P</i>) and sales staff (<i>S</i>). Customers (<i>C</i>) attend the circus.<br>'
  'Communication between the five groups depends on whether they are customers or employees, and on what type of employee they are.<br>Matrix <i>G</i> below shows the communication links between the five groups.'
  +'<div style="display:flex;gap:18px;align-items:center;margin:8px 0">'+EQ('<i>G</i> = <i>sender</i>',LT(mat([[0,1,1,1,1],[1,0,1,1,1],[0,1,0,0,0],[0,1,0,0,1],[0,0,0,1,0]],cl=list('DMPSC'),rl=list('DMPSC'),side=True,fs=17,tid='g4'),'receiver',''))
  +'<div style="flex:1">In this matrix:<br>• The ‘1’ in row <i>D</i>, column <i>M</i> indicates that the directors can communicate directly with the managers.<br>• The ‘0’ in row <i>P</i>, column <i>D</i> indicates that the performers cannot communicate directly with the directors.</div></div>'
  'a. A customer wants to make a complaint to a director.<br>What is the shortest communication sequence that will successfully get this complaint to a director? <span class="muted">(1 mark)</span></div>',
  [('Row C','customers can only send to S','data-hi="#g4|c4_3|hy"'),('Row S','sales staff send to M (and C), not D','data-hi="#g4|c3_1|hb"'),('Row M','managers send to D','data-hi="#g4|c1_0|hg"')],
  '<i>C</i> → <i>S</i> → <i>M</i> → <i>D</i>','VCAA 2023 General Mathematics Exam 2 Q10a (examiner report: average 0.7/1)',stat=('mark',70)))
sm()

# ================= APK
S.append(qslide('apk','APK 1 · Year 11 · Cambridge U1&amp;2 4H #19','The long term (steady state)',
  '<div style="font-size:26px;margin-top:30px">Consider the following matrices: one defining the initial populations in Geelong and Ballarat and the other, a transition matrix defining the proportion of the population moving between the two cities each year. Assume Geelong is listed first.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([['250 000'],['110 000']],fs=26)),EQ('<i>T</i> =',mat([[0.9,0.15],[0.1,0.85]],fs=26)))
  +'In the example of Geelong and Ballarat above, how many people are expected to be in Geelong in the long term?</div>',
  [('Long term','= steady state: <i>S</i><sub><i>n</i></sub> = <i>T</i><sup><i>n</i></sup><i>S</i><sub>0</sub> for a large <i>n</i>'),
   ('CAS',EQ('<i>T</i><sup>50</sup><i>S</i><sub>0</sub> = <i>T</i><sup>51</sup><i>S</i><sub>0</sub> =',mat([['216 000'],['144 000']],fs=20))),('Read','Geelong = row 1')],
  'About <b>216 000 people</b> in Geelong in the long term.',f'{CAM12} · Ch 4 review skills checklist 4H #19 (p. 293) · solution worked for 12MAG'))

# ================= Learn
TL=mat([[0.8,0.1],[0.2,0.9]],fs=20)
S.append(learn('Learn · 11D','Adding or removing at every step: Sₙ₊₁ = TSₙ + B',
  '<h4>Move with T, then add B</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> only works when the total never changes</li>'
  '<li><i>B</i> = a column matrix: + is added (restocking), − is removed (culling), in each state, every step</li>'
  '<li>the total changes by the sum of <i>B</i> each step</li>'
  '<li>no <i>T</i><sup><i>n</i></sup> shortcut: <i>S</i><sub>1</sub>, then <i>S</i><sub>2</sub>, then <i>S</i><sub>3</sub> …</li>'
  '<li>going back: <i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup>(<i>S</i><sub><i>n</i>+1</sub> − <i>B</i>)</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:14px;align-items:center;font-size:22px">'
  +EQ('<i>B</i> =',mat([[-5],[0],[10]],rl=['cows','goats','sheep'],side=True,fs=22))
  +'<div class="frag" style="font-size:20px">5 cows culled, no goats added or removed, 10 sheep restocked: every month</div>'
  +'<div class="frag">'+EQ(Sn(0),'→ × <i>T</i> → + <i>B</i> →',Sn(1),'→ × <i>T</i> → + <i>B</i> →',Sn(2),'→ …')+'</div></div>',
  'Multiply by T first, then add B. Adding B before multiplying gives a different (wrong) answer.',f'{CAM}, 11D pp. 570–571 (own words) · {EDR}, 7I p. 506 (matrix B example)',
  cards=(kcard('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> + <i>B</i>')),kcard('Step back',F('<i>S</i><sub><i>n</i></sub> = <i>T</i><sup>−1</sup>(<i>S</i><sub><i>n</i>+1</sub> − <i>B</i>)')))))

# ================= Ex 8 / You try 7I WE3
S.append(qslide('we','Worked example 8 · 11D','Determining state matrices using Sₙ₊₁ = TSₙ + B',
  '<div style="font-size:19px">A rental starts with 90 cars, 50 located at Bendigo and 40 located at Colac.<br>Cars are usually rented and returned in the same town. However, a small percentage of cars rented in Bendigo are returned in Colac and vice versa. The transition diagram opposite gives these percentages.'+IMG('ex8.png',260)
  +'To increase the number of cars, two extra cars are added to the rental fleet at each location each week. The recurrence relation that can be used to model this situation is:'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[50],[40]],fs=20),', <i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> + <i>B</i> where <i>T</i> =',TL,'and <i>B</i> =',mat([[2],[2]],fs=20)))
  +'Determine the number of cars at Bendigo and Colac after:'+plist([('a','1 week'),('b','2 weeks.')])+'</div>',
  [('a',EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> + <i>B</i> =',mat([[0.8,0.1],[0.2,0.9]],fs=16),mat([[50],[40]],fs=16),'+',mat([[2],[2]],fs=16),'=',mat([[44],[46]],fs=16),'+',mat([[2],[2]],fs=16),'=',mat([[46],[48]],fs=16))),
   ('b',EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub> + <i>B</i> =',mat([[0.8,0.1],[0.2,0.9]],fs=16),mat([[46],[48]],fs=16),'+',mat([[2],[2]],fs=16),'=',mat([[41.6],[52.4]],fs=16),'+',mat([[2],[2]],fs=16),'=',mat([[43.6],[54.4]],fs=16)))],
  '',f'{CAM} · Example 8 (pp. 570–571)',video='Cambridge GO · Example 8 (11D Resources)',
  parts=[('a','We predict <b>46 cars</b> in Bendigo and <b>48 cars</b> in Colac.'),('b','We predict <b>43.6 cars</b> in Bendigo and <b>54.4 cars</b> in Colac.')]))
sm()
T3=[['0.73','0.07','0.11','0'],['0.10','0.71','0.04','0'],['0.06','0.08','0.72','0'],['0.11','0.14','0.13','1']]
S.append(qslide('yt','You try 1 · Edrolo 7I WE3','Determining state matrices using Sₙ₊₁ = TSₙ + B',
  '<div style="font-size:19px">Eddortsford High School runs an optional extra-curricular arts program. Each year, students can choose from Music (<i>M</i>), Drama (<i>D</i>), Visual Arts (<i>V</i>), or to opt out (<i>O</i>) of the program. The movement of students from one year to the next is summarised in the transition matrix, <i>T</i>.'
  +C(EQ('<i>T</i> =',LT(mat(T3,cl=list('MDVO'),rl=list('MDVO'),side=True,fs=17),'this year','next year')),EQ('<i>S</i><sub>0</sub> =',mat([[73],[36],[52],[0]],rl=list('MDVO'),side=True,fs=17)),gap=40)
  +'The matrix <i>S</i><sub>0</sub> represents the number of students enrolled in each course at the beginning of 2023.<br>As the program expands, 30 new students are added to the program each year. 13 of these students are expected to be added to the music course, 6 to the drama course and 11 to the visual arts course.'
  +plist([('a','Construct matrix <i>B</i> to represent the predicted new enrolments and their preferences.'),('b','How many students are expected to be enrolled in the music course at the beginning of 2025? Round to the nearest whole number.')])+'</div>',
  [('a','<i>B</i> has the same order as <i>S</i><sub>0</sub> (4 × 1): 13 M, 6 D, 11 V, 0 O'),
   ('b: 2024',EQ('<i>S</i><sub>1</sub> = <i>TS</i><sub>0</sub> + <i>B</i> =',mat([['74.53'],['40.94'],['55.70'],['19.83']],fs=15))),
   ('b: 2025',EQ('<i>S</i><sub>2</sub> = <i>TS</i><sub>1</sub> + <i>B</i> =',mat([['76.3997'],['44.7484'],['58.8510'],['41.0009']],fs=15),'· music = row 1'))],
  '',f'{EDR} · 7I Worked example 3 (pp. 506–507)',
  parts=[('a',EQ('<i>B</i> =',mat([[13],[6],[11],[0]],rl=list('MDVO'),side=True,fs=15))),('b','<b>76 students</b> in music at the beginning of 2025')]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-recurrence']
S.append(cas('CAS · 11D','Sₙ₊₁ = TSₙ + B on CAS: T × ans + B',
  '<div style="font-size:24px">Example 8 on CAS:</div>'+C(EQ('<i>T</i> =',TL),EQ('<i>S</i><sub>0</sub> =',mat([[50],[40]],fs=20)),EQ('<i>B</i> =',mat([[2],[2]],fs=20)))+'<div style="font-size:24px">Find <i>S</i><sub>1</sub>, <i>S</i><sub>2</sub> and <i>S</i><sub>3</sub>.</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  [CS['ti'][0],CS['ti'][4]],[CS['classpad'][0],CS['classpad'][4]],
  EQ(Sn(1),'=',mat([[46],[48]],fs=16),' · ',Sn(2),'=',mat([[43.6],[54.4]],fs=16),' · ',Sn(3),'=',mat([[42.32],[59.68]],fs=16)),
  f'{CAM} · Example 8 (pp. 570–571) · Steps: CAS guide (planner)'))

# ================= Exit
S.append(qslide('ex','Exit task 1 of 1 · VCAA 2017 Exam 1 Q7','Show what you know',
  '<div style="font-size:16px">At a fish farm:<br>• young fish (<i>Y</i>) may eventually grow into juveniles (<i>J</i>) or they may die (<i>D</i>)<br>• juveniles (<i>J</i>) may eventually grow into adults (<i>A</i>) or they may die (<i>D</i>)<br>• adults (<i>A</i>) eventually die (<i>D</i>).<br>'
  'The initial state of this population, <i>F</i><sub>0</sub>, is shown below.'
  +'<br>Every month, fish are either sold or bought so that the number of young, juvenile and adult fish in the farm remains constant.<br>The population of fish in the fish farm after <i>n</i> months, <i>F</i><sub><i>n</i></sub>, can be determined by the recurrence rule'
  +C(EQ('<i>F</i><sub>0</sub> =',mat([['50 000'],['10 000'],['7 000'],['0']],rl=list('YJAD'),side=True,fs=14)),EQ('<i>F</i><sub><i>n</i>+1</sub> =',mat([['0.65',0,0,0],['0.25','0.75',0,0],[0,'0.20','0.95',0],['0.10','0.05','0.05',1]],fs=14,tid='x1'),'<i>F</i><sub><i>n</i></sub> + <i>B</i>'),gap=40)
  +'where <i>B</i> is a column matrix that shows the number of young, juvenile and adult fish bought or sold each month and the number of dead fish that are removed.<br>Each month, the fish farm will</div>',
  [('Constant','numbers stay the same, so <i>F</i><sub>1</sub> = <i>F</i><sub>0</sub>: <i>F</i><sub>0</sub> = <i>TF</i><sub>0</sub> + <i>B</i>'),
   ('Rearrange','<i>B</i> = <i>F</i><sub>0</sub> − <i>TF</i><sub>0</sub>'),
   ('TF₀',EQ('<i>TF</i><sub>0</sub> =',mat([['32 500'],['20 000'],['8 650'],['5 850']],rl=list('YJAD'),side=True,fs=14),'so <i>B</i> =',mat([['17 500'],['−10 000'],['−1 650'],['−5 850']],rl=list('YJAD'),side=True,fs=14))),
   ('Read','A: −1650, a negative = removed = sold')],
  'Sell 1650 adult fish: <b>A</b>.','VCAA 2017 Further Mathematics Exam 1 Matrices Q7 (examiner report: 36% correct) · Edrolo U3&amp;4 7I Q15',
  mc=['sell 1650 adult fish.','buy 1750 adult fish.','sell 17 500 young fish.','buy 50 000 young fish.','buy 10 000 juvenile fish.'],key='A',
  dis=('C','17 500 is the young-fish element of B but it is positive: young fish are bought, not sold'),stat=('mc',36)))
sm()

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 11 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='11D' and v.get('url')]))
n=assemble(S,'12MAG · 11D · Transition matrices: using the rule Sn+1 = TSn + B',os.path.join(ROOT,'lessons','11D slides.html'))
print(n-1,'slides')
