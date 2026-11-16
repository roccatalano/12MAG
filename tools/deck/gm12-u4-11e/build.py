"""Lesson gm12-u4-11e (11E Leslie matrices) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/11E slides.html      Run: python3 tools/deck/gm12-u4-11e/build.py      Screenshots: python3 tools/deck/gm12-u4-11e/shoot.py
Matrices with tools/deck/mx.py; life cycle diagrams drawn with tools/deck/leslie.py (new reusable helper).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- No CFAT (CFAT 3.11.2 opens the Ch 11 test lesson).
- Do Now: VCAA 2025 NHT Exam 1 Q32 (B; NHT report: no %) · VCAA 2025 Exam 1 Q31 (B, 70%) ·
          VCAA 2023 Exam 2 Q11 stem + Q11a (average 0.3/1) · VCAA 2024 Exam 2 Q1 stem + Q1e (average 0.5/1). % from tools/vcaa_current_index.csv.
- APK: Cambridge U1&2 Ch 4 review skills checklist 4D #8, solution worked for 12MAG.
- Learn: Cambridge U3&4 11E pp. 574-577 (own words) · Edrolo U3&4 7G p. 486.
- Worked examples: Cambridge U3&4 Examples 9-13 (pp. 578-582).
- You trys: Edrolo U3&4 7G Worked example 8 (pp. 486-488) for Ex 9; YT-11E-10..13 written for 12MAG (planner/written-youtrys.json,
  answers checked with numpy 16 Nov) for Ex 10-13 (no Edrolo Leslie example matches).
- CAS: planner/cas-skills.json 'matrix-recurrence' (Lⁿ·S) on Cambridge Example 11 data.
- No exit task (card: Edrolo has no VCAA Leslie-matrix reprints).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat
from leslie import lifecycle
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-11e')
yid=lambda u:u.split('v=')[1].split('&')[0]
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:10px 0">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(x if x.lstrip().startswith(('<table','<span')) else f'<span>{x}</span>' for x in xs)+'</span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def Sn(n): return f'<i>S</i><sub>{n}</sub>'
def col(v,fs=15): return mat([[x] for x in v],fs=fs)
WR=lambda n:f'Written for 12MAG (modelled on Cambridge Example {n}; no Edrolo match) · planner/written-youtrys.json YT-11E-{n}'
S=['<style>.sm .L .q{font-size:17px}.xs ol.parts li{font-size:18px!important;line-height:1.25}</style>']

# ================= opening
t=title('11E','Leslie matrices',f'{CAM} · 11E Leslie matrices','11E',flow=('Do Now','APK','Learn','Worked examples','You try','CAS','Check-in'))
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill','var(--apk)'),
  ('Leslie matrices and life cycle diagrams · Examples 9–10','→ You try',None),('Long-term behaviour · Examples 11–13','→ You try',None),
  ('CAS','· Lⁿ × S₀',None),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Leslie matrix <i>L</i>','females only · top row = birth rates of each age group · sub-diagonal = survival rates · zeros elsewhere · columns do NOT add to 1'),
  ('Life cycle diagram','one circle per age group; birth arrows back to group 1, survival arrows to the next group',lifecycle([0,1.8,2.6,0.1],[0.2,0.4,0.3],w=300,fs=12)),
  ('Long term','the population grows, declines, stays constant or cycles (periodic)')],
  [('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>L</i> <i>S</i><sub><i>n</i></sub>'),'one time period'),
   ('nth state',F('<i>S</i><sub><i>n</i></sub> = <i>L</i><sup><i>n</i></sup><i>S</i><sub>0</sub>'),'straight to state n'),
   ('Total',F('[1 1 … 1] × <i>S</i><sub><i>n</i></sub>'),'adds every age group'),
   ('Growth rate',F('<i>S</i><sub><i>n</i>+1</sub> ÷ <i>S</i><sub><i>n</i></sub>'),'same for every age group, large n')],
  f'{CAM}, 11E pp. 574–577; Study Design: Sₙ₊₁ = LSₙ, L a Leslie matrix'))

# ================= Do Now 1: VCAA 2025 NHT E1 Q32 (11D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 NHT Exam 1 Q32','Review of 11D (last lesson)',
  '<div style="font-size:13px;line-height:1.25">A course requires students to pass two levels of study before they graduate.<br>Each level of study takes one year.<br>'
  '• Students must pass the first level (<i>L1</i>) before they move on to the second level (<i>L2</i>).<br>• Students must pass the second level before they become graduates (<i>G</i>).<br>'
  'From one year to the next, it is known that<br>• 80% of students pass the first level of study and progress to the second level of study<br>• 60% of students in the second level of study become graduates the following year.<br>'
  'Students who do not pass a level of study repeat it in the following year. No student leaves the course before graduating.<br>'
  'At the start of 2025, the numbers of students enrolled in <i>L1</i> and <i>L2</i> of the course and who have graduated from the course are given by the recurrence relation'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[1000],[0],[0]],rl=['<i>L1</i>','<i>L2</i>','<i>G</i>'],side=True,fs=14)),EQ('<i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> +',mat([['<i>k</i>'],[0],[0]],fs=14)))
  +'where<br>• <i>T</i> is the transition matrix showing the expected proportion of students moving between states <i>L1</i>, <i>L2</i> and <i>G</i> from one year to the next<br>• <i>S</i><sub><i>n</i></sub> is the state matrix <i>n</i> years after the start of 2025.<br>'
  'To ensure that there are always students studying the course, new students are enrolled into the first level every year so that the number of students studying the first level remains at 1000.<br>'
  '<i>k</i> is the number of new students enrolled at the first level each year.<br>At the start of which year will the expected number of students who have graduated from the course first exceed 5000?</div>',
  [('T',EQ('<i>T</i> =',mat([[0.2,0,0],[0.8,0.4,0],[0,0.6,1]],fs=14),'(columns = from L1, L2, G)')),
   ('k','L1 stays 1000: 0.2 × 1000 + <i>k</i> = 1000, so <i>k</i> = 800'),
   ('Step','<i>T</i> × ans + <i>B</i> on CAS: G = 0, 0, 480, 1152, 1900.8, 2680.3, 3472.1, 4268.9, <b>5067.5</b> (n = 8)'),
   ('Year','n = 8 → start of 2025 + 8 = 2033')],
  '2033: <b>B</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q32 (NHT report: answers only, no %)',
  mc=['2032','2033','2034','2035'],key='B',dis=('A','2032 is n = 7: G = 4268.9, not yet over 5000'),stat=('nht',)))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
# ================= Do Now 2: VCAA 2025 E1 Q31 (10D)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q31','Review of 10D (Ch 10)',
  '<div style="font-size:24px;margin-top:30px">Consider the following four matrices.'
  +C(EQ('<i>A</i> =',mat([[4,6],[-2,-3]],fs=22)),EQ('<i>B</i> =',mat([[4],[2],[8]],fs=22)),EQ('<i>C</i> =',mat([[5,0],[2,5],[3,1]],fs=22)),EQ('<i>D</i> =',mat([[3,-2,5]],fs=22)),gap=30)
  +'Which one of the following computations is defined?</div>',
  [('Orders','<i>A</i> 2 × 2 · <i>B</i> 3 × 1 · <i>C</i> 3 × 2 · <i>D</i> 1 × 3'),
   ('A','<i>A</i> + <i>B</i>: different orders ✗'),('B','<i>C</i><sup>T</sup>(2 × 3) × <i>B</i>(3 × 1) = 2 × 1; × <i>D</i>(1 × 3) = 2 × 3 ✓'),
   ('C, D','<i>BD</i> is 3 × 3 ≠ <i>C</i> ✗ · <i>DA</i>: 1 × 3 by 2 × 2 ✗')],
  '<i>C</i><sup>T</sup><i>BD</i> is defined: <b>B</b>.','VCAA 2025 General Mathematics Exam 1 Q31 (examiner report: 70% correct)',
  mc=['<i>D</i>(<i>A</i> + <i>B</i>)','<i>C</i><sup>T</sup><i>BD</i>','<i>C</i> + <i>BD</i>','(<i>DA</i>)<sup>T</sup> + <i>D</i>'],key='B',
  dis=('C','<i>BD</i> is defined (3 × 3), but a 3 × 3 cannot be added to the 3 × 2 matrix <i>C</i>'),stat=('mc',70)))
# ================= Do Now 3: VCAA 2023 E2 Q11a (11D)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q11a','Review of 11D (last lesson)',
  '<div style="font-size:23px">The circus requires 180 workers to put on each show.<br>From one show to the next, workers can either continue working (<i>W</i>) or they can leave the circus (<i>L</i>).<br>'
  'Once workers leave the circus, they do not return.<br>It is known that 95% of the workers continue working at the circus.<br>This situation can be modelled by the matrix recurrence relation'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[180],[0]],fs=22)),EQ(', <i>S</i><sub><i>n</i>+1</sub> = <i>TS</i><sub><i>n</i></sub> + <i>B</i>'))
  +'a. Write down matrix <i>T</i>, the transition matrix, for this recurrence relation. <span class="muted">(1 mark)</span></div>',
  [('W column','95% of workers stay (W → W = 0.95), so 5% leave (W → L = 0.05)'),('L column','once left, they do not return: L → W = 0, L → L = 1')],
  EQ('<i>T</i> =',mat([[0.95,0],[0.05,1]],cl=['<i>W</i>','<i>L</i>'],rl=['<i>W</i>','<i>L</i>'],side=True,fs=18)),
  'VCAA 2023 General Mathematics Exam 2 Q11a (examiner report: average 0.3/1)',stat=('mark',30),cmd=('Write down',None,'each column adds to 1')))
# ================= Do Now 4: VCAA 2024 E2 Q1e (2G)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q1e','Review of 2G (last term)',
  '<div style="font-size:24px;margin-top:40px">Table 1 lists the Olympic year, <i>year</i>, and the gold medal-winning height for the men’s high jump, <i>Mgold</i>, in metres, for each Olympic Games held from 1928 to 2020. No Olympic Games were held in 1940 or 1944, and the 2020 Olympic Games were held in 2021.<br><br>'
  '<span class="muted">(Table 1 and parts a–d not shown.)</span><br><br>e. The coefficient of determination is 0.857<br>Interpret the coefficient of determination in terms of <i>Mgold</i> and <i>year</i>. <span class="muted">(1 mark)</span></div>',
  [('Template','<i>r</i><sup>2</sup> × 100% of the variation in the response variable can be explained by the variation in the explanatory variable'),
   ('Variables','response = <i>Mgold</i> · explanatory = <i>year</i>'),('Value','0.857 → 85.7%')],
  '<b>85.7%</b> of the variation in <i>Mgold</i> can be explained by the variation in <i>year</i>.','VCAA 2024 General Mathematics Exam 2 Q1e (examiner report: average 0.5/1)',
  stat=('mark',50),cmd=('Interpret',None,'the r² template, in context')))

# ================= APK
S.append(qslide('apk','APK 1 · Year 11 · Cambridge U1&amp;2 4D #8','The order of a matrix product',
  '<div style="font-size:28px;margin-top:40px">Determine the order of the answer matrix for the following matrix multiplication:'
  +C(EQ(mat([[9,-11],[8,3]],fs=28),mat([[7,-6,2,-2],[4,-3,1,5]],fs=28)))+'</div>',
  [('Orders','2 × <b>2</b> and <b>2</b> × 4'),('Check','inner numbers match (2 = 2), so the product is defined'),('Order','outer numbers: 2 × 4')],
  'The answer matrix has order <b>2 × 4</b>.',f'{CAM12} · Ch 4 review skills checklist 4D #8 · solution worked for 12MAG',cmd=('Determine',None,'outer numbers')))

# ================= Learn 1: Leslie matrices
L9=[[0,'1.8','2.6','0.1'],['0.2',0,0,0],[0,'0.4',0,0],[0,0,'0.3',0]]
S.append(learn('Learn · 11E','A Leslie matrix models an age-structured population',
  '<h4>Reading a Leslie matrix</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>females only, split into age groups of equal length</li>'
  '<li><b style="color:#c62828">top row</b> = birth rates <i>b</i><sub>1</sub>, <i>b</i><sub>2</sub> …: average daughters per female in each group</li>'
  '<li><b style="color:#1565c0">sub-diagonal</b> = survival rates <i>s</i><sub>1</sub>, <i>s</i><sub>2</sub> …: proportion that live into the next group</li>'
  '<li>zeros everywhere else · columns do NOT add to 1</li>'
  '<li><i>S</i><sub><i>n</i>+1</sub> = <i>LS</i><sub><i>n</i></sub>, so <i>S</i><sub><i>n</i></sub> = <i>L</i><sup><i>n</i></sup><i>S</i><sub>0</sub></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:12px;align-items:center;font-size:22px">'
  +EQ('<i>L</i> =',mat(L9,fs=22))
  +'<div class="frag">'+lifecycle([0,1.8,2.6,0.1],[0.2,0.4,0.3],w=520)+'</div></div>',
  'Birth arrows always go back to group 1; survival arrows only go one step forward.',f'{CAM}, 11E pp. 574–577 (own words) · {EDR}, 7G p. 486',
  cards=(kcard('Next state',F('<i>S</i><sub><i>n</i>+1</sub> = <i>LS</i><sub><i>n</i></sub>')),kcard('nth state',F('<i>S</i><sub><i>n</i></sub> = <i>L</i><sup><i>n</i></sup><i>S</i><sub>0</sub>')))))

# ================= Ex 9 / You try 7G WE8
S.append(qslide('we','Worked example 9 · 11E','Determining state matrices and life cycle diagrams',
  '<div style="font-size:18px">Use the Leslie matrix and initial state matrix below to answer the following questions.'
  +C(EQ('<i>L</i> =',mat(L9,fs=17,cl=['1','2','3','4'],rl=['1','2','3','4'],side=True)),EQ('<i>S</i><sub>0</sub> =',col([1000,0,0,0],17)),gap=40)
  +plist([('a','Write down <b>i</b> the birth rate for age group 2 &nbsp; <b>ii</b> the survival rate for age group 3'),('b','Complete a life cycle diagram for this Leslie matrix.'),
          ('c','Evaluate the following population state matrices. <i>S</i><sub>1</sub>, <i>S</i><sub>5</sub> and <i>S</i><sub>20</sub>'),
          ('d',EQ('Given that <i>S</i><sub>16</sub> =',col(['9.53','2.42','1.22','0.16'],14),', determine <i>S</i><sub>17</sub>'))])+'</div>',
  [],'',f'{CAM} · Example 9 (pp. 578–579)',video='Cambridge GO · Example 9 (11E Resources)',
  parts=[('a','i birth rate for age group 2 = <b>1.8</b> (row 1, column 2) · ii survival rate for age group 3 = <b>0.3</b> (row 4, column 3)'),
         ('b',lifecycle([0,1.8,2.6,0.1],[0.2,0.4,0.3],w=330,fs=13)),
         ('c',EQ(Sn(1),'=',col([0,200,0,0],13),Sn(5),'=',col(['149.76','26.4','16.64','8.64'],13),Sn(20),'=',col(['3.84','0.97','0.49','0.19'],13))),
         ('d',EQ(Sn(17),'= <i>L</i>',Sn(16),'=',col(['7.54','1.91','0.97','0.37'],13),' · the population keeps decreasing'))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
L8=[['0.05','0.80','0.90'],['0.85',0,0],[0,'0.75',0]]
S.append(qslide('yt','You try 1 · Edrolo 7G WE8','Determining state matrices',
  '<div style="font-size:18px">Scientists have collected the yearly fertility and survival rates for siamese fighting fish. A small sample of the species is under observation. The following Leslie matrix for the survival rate of siamese fighting fish can be used to model the growth of the sample population.'
  +C(EQ('<i>L</i> =',mat(L8,cl=['0','1','2'],fs=17)),EQ('<i>S</i><sub>0</sub> =',mat([[50],[40],[30]],rl=['0','1','2'],side=True,fs=17)),gap=40)
  +'The initial state matrix represents the female population of the sample being observed at the start of the study (columns and rows = age).'
  +plist([('a','Interpret the element in row 2 and column 1 of the Leslie matrix.'),('b','Interpret the element in row 1 and column 3 of the Leslie matrix.'),
          ('c','What is the estimated total number of female siamese fighting fish after two years?'),('d','Determine <i>S</i><sub>8</sub>, the expected female population in the study after 8 years. Round the matrix elements to the nearest whole number.')])+'</div>',
  [],'',f'{EDR} · 7G Worked example 8 (pp. 486–488)',
  parts=[('a','85% of the female population that is less than 1 year old will survive into the next year.'),('b','On average, there will be 0.90 females born to each 2-year-old female.'),
         ('c',EQ(Sn(2),'= <i>L</i><sup>2</sup>',Sn(0),'=',col(['64.075','52.275','31.875'],13),'≈',col([64,52,32],13),': <b>148</b> female fish')),
         ('d',EQ(Sn(8),'= <i>L</i><sup>8</sup>',Sn(0),'≈',col([128,97,66],13)))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)

# ================= Ex 10 / YT 10
def tab(head,rows,fs=17):
    th=''.join(f'<td style="border:1px solid #999;padding:3px 9px;text-align:center">{h}</td>' for h in head)
    return f'<table style="border-collapse:collapse;font-size:{fs}px;margin:8px auto"><tr><th style="border:1px solid #999;padding:3px 9px;text-align:left;color:#0a7a8a">Age group (years)</th>{th}</tr>'+''.join(f'<tr><th style="border:1px solid #999;padding:3px 9px;text-align:left;color:#0a7a8a">{r[0]}</th>'+''.join(f'<td style="border:1px solid #999;padding:3px 9px;text-align:center">{x}</td>' for x in r[1:])+'</tr>' for r in rows)+'</table>'
EX10Q=lambda an:plist([('a','Write down the initial population state matrix, <i>S</i><sub>0</sub>.'),('b',f'Using the information in the table above, write down a Leslie matrix to describe the change in population of female {an}.'),
                    ('c','Construct a life cycle transition diagram for this Leslie matrix.'),('d',f'Determine the number of 3 − 4 year old female {an} in the population after 3 years. Round your answer to the nearest whole number.')])
S.append(qslide('we','Worked example 10 · 11E','Entering information in a Leslie matrix and state matrix',
  '<div style="font-size:18px">Information about a population of female goats is given in the following table.'
  +tab(['0 − 1','1 − 2','2 − 3','3 − 4','4 − 5'],[['Initial population',10,25,40,20,15],['Birth rates',0,0.2,0.9,0,0],['Survival rates',0.6,0.7,0.5,0.2,0]])+EX10Q('goats')+'</div>',
  [],'',f'{CAM} · Example 10 (pp. 579–580)',video='Cambridge GO · Example 10 (11E Resources)',cmd=('Construct',None,'one circle per age group'),
  parts=[('a',EQ(Sn(0),'=',col([10,25,40,20,15],12))),
         ('b',EQ('<i>L</i> =',mat([[0,0.2,0.9,0,0],[0.6,0,0,0,0],[0,0.7,0,0,0],[0,0,0.5,0,0],[0,0,0,0.2,0]],fs=12))),
         ('c',lifecycle([0,0.2,0.9,0,0],[0.6,0.7,0.5,0.2],w=360,fs=12)),
         ('d',EQ(Sn(3),'= <i>L</i><sup>3</sup>',Sn(0),'=',col(['8.7','10.17','17.22','2.1','1.75'],12),': there are <b>two goats</b> in the 3–4 year old age group'))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
S.append(qslide('yt','You try 2 · written for 12MAG','Entering information in a Leslie matrix and state matrix',
  '<div style="font-size:18px">Information about a population of female rabbits is given in the following table.'
  +tab(['0 − 1','1 − 2','2 − 3','3 − 4'],[['Initial population',20,30,15,10],['Birth rates',0,1.2,0.8,0],['Survival rates',0.5,0.6,0.3,0]])+EX10Q('rabbits')+'</div>',
  [],'',WR(10),cmd=('Construct',None,'one circle per age group'),
  parts=[('a',EQ(Sn(0),'=',col([20,30,15,10],12))),('b',EQ('<i>L</i> =',mat([[0,1.2,0.8,0],[0.5,0,0,0],[0,0.6,0,0],[0,0,0.3,0]],fs=12))),
         ('c',lifecycle([0,1.2,0.8,0],[0.5,0.6,0.3],w=330,fs=12)),
         ('d',EQ(Sn(3),'= <i>L</i><sup>3</sup>',Sn(0),'=',col(['33.6','13.2','14.4','1.8'],12),': about <b>2 rabbits</b> aged 3–4'))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)

# ================= Learn 2: long term
S.append(learn('Learn · 11E','Long-term (limiting) behaviour',
  '<h4>What happens in the long run?</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>find <i>S</i><sub><i>n</i></sub> = <i>L</i><sup><i>n</i></sup><i>S</i><sub>0</sub> for larger and larger <i>n</i></li>'
  '<li>total population: premultiply by [1 1 … 1]</li>'
  '<li>often, after a while, every age group grows by the same factor <i>k</i>: <i>LS</i><sub><i>n</i></sub> = <i>kS</i><sub><i>n</i></sub></li>'
  '<li><i>k</i> = <i>S</i><sub><i>n</i>+1</sub> ÷ <i>S</i><sub><i>n</i></sub> (any age group): <i>k</i> &gt; 1 grows, <i>k</i> &lt; 1 declines</li>'
  '<li>not always: some populations cycle (periodic)</li></ul>',
  '<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;font-size:20px;width:100%">'
  +''.join(f'<div class="frag kf" style="display:block"><b>{a}</b><br><span class="muted">{b}</span></div>' for a,b in [('Increasing','k &gt; 1, e.g. 1.19 = +19% per period'),('Decreasing','k &lt; 1, numbers head to 0'),('Constant','k = 1, the numbers stop changing'),('Periodic','the states repeat, e.g. L³ = I')])+'</div>',
  'The growth rate depends mostly on L, not on S₀.',f'{CAM}, 11E pp. 580–582 (own words)',
  cards=(kcard('Total',F('[1 1 … 1] × <i>S</i><sub><i>n</i></sub>')),kcard('Growth rate',F('<i>k</i> = <i>S</i><sub><i>n</i>+1</sub> ÷ <i>S</i><sub><i>n</i></sub>')))))

# ================= Ex 11 / YT 11
EX11Q=lambda r:plist([('a','Find <b>i</b> <i>S</i><sub>5</sub> &nbsp; <b>ii</b> <i>S</i><sub>10</sub> &nbsp; <b>iii</b> <i>S</i><sub>50</sub><br>Premultiply each of these state matrices by [1 1 1] to calculate the total populations at each of these stages and comment.'),
                      ('b',f'Determine <i>S</i><sub>25</sub> and <i>S</i><sub>26</sub>. Divide each age group population for <i>S</i><sub>26</sub> by the corresponding age group population for <i>S</i><sub>25</sub> and show that <i>S</i><sub>26</sub> ≈ {r}<i>S</i><sub>25</sub> and comment.')])
S.append(qslide('we','Worked example 11 · 11E','Limiting behaviour for Leslie matrices',
  '<div style="font-size:19px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,4,4],[0.25,0,0],[0,0.5,0]],fs=19)),'and',EQ('<i>S</i><sub>0</sub> =',col([1000,0,0],19)))+EX11Q('1.1915')+'</div>',
  [],'',f'{CAM} · Example 11 (pp. 580–581)',video='Cambridge GO · Example 11 (11E Resources)',cmd=('Determine',None,'Lⁿ × S₀ on CAS'),
  parts=[('a',EQ(Sn(5),'=',col([1000,250,'62.5'],12),'total 1312.5 ·',Sn(10),'=',col([2500,'531.25','218.75'],12),'total 3250 ·',Sn(50),'=',col(['2 777 063','582 688.05','244 521.18'],12),'total ≈ 3 604 272: the population <b>increases without bound</b>')),
         ('b',EQ(Sn(25),'=',col(['34 781.25','7297.85','3062.50'],12),Sn(26),'=',col(['41 441.41','8695.31','3648.93'],12),': each ratio ≈ 1.1915, so the population grows by about <b>19%</b> each time period'))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)
S.append(qslide('yt','You try 3 · written for 12MAG','Limiting behaviour for Leslie matrices',
  '<div style="font-size:19px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,3,3],[0.3,0,0],[0,0.5,0]],fs=19)),'and',EQ('<i>S</i><sub>0</sub> =',col([1000,0,0],19)))+EX11Q('1.1381')+'</div>',
  [],'',WR(11),cmd=('Determine',None,'Lⁿ × S₀ on CAS'),
  parts=[('a',EQ(Sn(5),'=',col([810,243,'67.5'],12),'total ≈ 1121 ·',Sn(10),'≈',col([1575,421,180],12),'total ≈ 2176 ·',Sn(50),'≈',col(['280 035','73 813','32 427'],12),'total ≈ 386 275: the population <b>keeps increasing</b>')),
         ('b',EQ(Sn(25),'≈',col(['11 022','2905','1276'],12),Sn(26),'≈',col(['12 544','3307','1453'],12),': each ratio ≈ 1.1381, so every age group grows by about <b>13.8%</b> each year'))]))
sm(); S[-1]=S[-1].replace('slide T sm ','slide T sm xs ',1)

# ================= Ex 12 / YT 12
EX12Q=lambda r:plist([('a','Determine <b>i</b> <i>S</i><sub>10</sub> &nbsp; <b>ii</b> <i>S</i><sub>14</sub> &nbsp; <b>iii</b> <i>S</i><sub>15</sub>'),
  ('b','The rate of increase of the population is a constant and each of the age group populations increase in the same way. Find this rate by comparing <i>S</i><sub>14</sub> and <i>S</i><sub>15</sub>.'),
  ('c',f'Confirm the ratio of the age group populations stays constant for <i>S</i><sub>0</sub>, <i>S</i><sub>1</sub> and <i>S</i><sub>10</sub> at {r}')])
S.append(qslide('we','Worked example 12 · 11E','A Leslie matrix and state matrix with constant rate of increase',
  '<div style="font-size:19px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,2.3,0.4],[0.6,0,0],[0,0.3,0]],fs=19)),'and',EQ('<i>S</i><sub>0</sub> =',col([1600,800,200],19)))+EX12Q('8 : 4 : 1')+'</div>',
  [],'',f'{CAM} · Example 12 (pp. 581–582)',video='Cambridge GO · Example 12 (11E Resources)',
  parts=[('a',EQ(Sn(10),'=',col(['9906.78','4953.39','1238.35'],12),Sn(14),'=',col(['20 542.70','10 271.35','2567.84'],12),Sn(15),'=',col(['24 651.24','12 325.62','3081.4043'],12))),
         ('b','24 651.24 ÷ 20 542.70 = 12 325.62 ÷ 10 271.35 = 3081.4043 ÷ 2567.84 ≈ 1.2: the growth rate is <b>1.2</b>'),
         ('c','8 : 4 : 1 = 1600 : 800 : 200 ≈ 9906.78 : 4953.39 : 1238.35')]))
sm()
S.append(qslide('yt','You try 4 · written for 12MAG','A Leslie matrix and state matrix with constant rate of increase',
  '<div style="font-size:19px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,2,1],[0.6,0,0],[0,0.48,0]],fs=19)),'and',EQ('<i>S</i><sub>0</sub> =',col([1000,500,200],19)))+EX12Q('10 : 5 : 2')+'</div>',
  [],'',WR(12),
  parts=[('a',EQ(Sn(10),'≈',col([6192,3096,1238],12),Sn(14),'≈',col(['12 839','6420','2568'],12),Sn(15),'≈',col(['15 407','7704','3081'],12))),
         ('b','15 407 ÷ 12 839 ≈ 7704 ÷ 6420 ≈ 3081 ÷ 2568 ≈ 1.2: a <b>20%</b> increase each period'),
         ('c','1000 : 500 : 200 = 1200 : 600 : 240 (<i>S</i><sub>1</sub>) ≈ 6192 : 3096 : 1238 (<i>S</i><sub>10</sub>) = 10 : 5 : 2')]))
sm()

# ================= Ex 13 / YT 13
S.append(qslide('we','Worked example 13 · 11E','Periodic, increasing and decreasing rates of change',
  '<div style="font-size:22px;margin-top:20px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,0,'<i>b</i><sub>3</sub>'],[0.25,0,0],[0,0.5,0]],fs=22)),'and',EQ('<i>S</i><sub>0</sub> =',col([1000,0,0],22)))
  +'Investigate the long-term behaviour of the population if:'+plist([('a','<i>b</i><sub>3</sub> = 8'),('b','<i>b</i><sub>3</sub> = 4'),('c','<i>b</i><sub>3</sub> = 10')])+'</div>',
  [],'',f'{CAM} · Example 13 (p. 582)',video='Cambridge GO · Example 13 (11E Resources)',
  parts=[('a',EQ(Sn(1),'=',col([0,250,0],12),Sn(2),'=',col([0,0,125],12),Sn(3),'=',col([1000,0,0],12),': the population <b>cycles</b> through these three states (<i>L</i><sup>3</sup> = <i>I</i>)')),
         ('b',EQ(Sn(1),'=',col([0,250,0],12),Sn(5),'=',col([0,0,'62.5'],12),Sn(50),'=',col([0,0,'0.0019'],12),': the population <b>decreases</b>')),
         ('c',EQ(Sn(1),'=',col([0,250,0],12),Sn(5),'=',col([0,0,'156.25'],12),Sn(50),'=',col([0,0,'4440.89'],12),': the population <b>increases</b>'))]))
sm()
S.append(qslide('yt','You try 5 · written for 12MAG','Periodic, increasing and decreasing rates of change',
  '<div style="font-size:22px;margin-top:20px">Consider the following Leslie matrix <i>L</i> and initial population matrix <i>S</i><sub>0</sub>:'
  +C(EQ('<i>L</i> =',mat([[0,0,'<i>b</i><sub>3</sub>'],[0.4,0,0],[0,0.5,0]],fs=22)),'and',EQ('<i>S</i><sub>0</sub> =',col([500,0,0],22)))
  +'Investigate the long-term behaviour of the population if:'+plist([('a','<i>b</i><sub>3</sub> = 5'),('b','<i>b</i><sub>3</sub> = 3'),('c','<i>b</i><sub>3</sub> = 8')])+'</div>',
  [('Every time',EQ(Sn(1),'=',col([0,200,0],12),Sn(2),'=',col([0,0,100],12),Sn(3),'=',col(['100<i>b</i><sub>3</sub>',0,0],12)))],'',WR(13),
  parts=[('a',EQ(Sn(3),'=',Sn(6),'=',Sn(9),'=',col([500,0,0],12),': <b>periodic</b>, repeats every 3 years')),
         ('b',EQ(Sn(3),'=',col([300,0,0],12),Sn(6),'=',col([180,0,0],12),Sn(9),'=',col([108,0,0],12),': <b>decreasing</b> (× 0.6 every 3 years)')),
         ('c',EQ(Sn(3),'=',col([800,0,0],12),Sn(6),'=',col([1280,0,0],12),Sn(9),'=',col([2048,0,0],12),': <b>increasing</b> (× 1.6 every 3 years)'))]))
sm()

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-recurrence']
S.append(cas('CAS · 11E','Leslie matrices on CAS: Lⁿ × S₀',
  '<div style="font-size:24px">Example 11 on CAS:</div>'+C(EQ('<i>L</i> =',mat([[0,4,4],[0.25,0,0],[0,0.5,0]],fs=20)),EQ('<i>S</i><sub>0</sub> =',col([1000,0,0],20)))
  +'<div style="font-size:24px">Find <i>S</i><sub>5</sub>, <i>S</i><sub>10</sub> and the total population after 10 periods.</div>'
  '<p class="muted" style="font-size:17px">Total: multiply by the row matrix [1 1 1] first, e.g. [1 1 1]·l^10·s.</p>',
  [CS['ti'][0],CS['ti'][1]],[CS['classpad'][0],CS['classpad'][1]],
  EQ(Sn(5),'=',col([1000,250,'62.5'],16),' · ',Sn(10),'=',col([2500,'531.25','218.75'],16),' · total = 3250'),
  f'{CAM} · Example 11 (pp. 580–581) · Steps: CAS guide (planner)'))

# ================= closing (no exit task: no VCAA Leslie reprints in Edrolo)
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 11 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='11E' and v.get('url')]))
n=assemble(S,'12MAG · 11E · Leslie matrices',os.path.join(ROOT,'lessons','11E slides.html'))
print(n-1,'slides')
