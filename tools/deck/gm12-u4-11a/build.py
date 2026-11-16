"""Lesson gm12-u4-11a (11A Transition matrices: setting up a transition matrix) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/11A slides.html      Run: python3 tools/deck/gm12-u4-11a/build.py      Screenshots: python3 tools/deck/gm12-u4-11a/shoot.py
Transition matrices drawn with tools/deck/tpl/net.py amat() (cells revealed column by column); transition diagrams are verbatim crops (fig/).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- No CFAT this lesson (CFAT 3.11.1 opens 11C).
- Do Now: VCAA 2025 Exam 1 Q25 (A, 83%) · VCAA 2023 Exam 1 Q15 (C, 66%) · VCAA 2025 Exam 2 Q11 stem + Q11b (average 0.6/1 = 60%) ·
          VCAA 2024 Exam 2 Q2 stem + Q2cii (boxplot cropped from the paper; average 0.8/1 = 80%). % from tools/vcaa_current_index.csv (examiner reports).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4G #16 (p. 293; solution worked for 12MAG) ·
       VCAA 2019 Further Exam 2 Matrices Q2 stem + Q2b and Q3 stem + Q3a (original wording; = Edrolo U1&2 5G Q11, p. 311); 2b 84%, 3a 75% (2019 E2 report).
- Learn: Cambridge U3&4 11A pp. 551-553 (own words; Bendigo-Colac diagram cropped) · Edrolo U3&4 7G pp. 482-484, 7I p. 505.
- Worked examples: Cambridge U3&4 Examples 1-2 (pp. 552-553; Example 1 diagram cropped).
  You trys: Edrolo U3&4 7I WE2a (p. 505, diagram cropped) · 7G WE4 (pp. 483-484).
- CAS: planner/cas-skills.json 'matrix-entry' (card: enter and store the Example 1 matrix, check each column adds to 1).
- Exit: VCAA 2017 Further Exam 2 Matrices Q2a,b (= Edrolo U3&4 7I Q14, p. 513; diagram cropped from the paper); a 95%, b 69% (2017 E2 report).
"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat
from net import amat
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-11a')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def TM(tid,labels,rows,top,side,fs=20,name='T'):
    """transition matrix answer template: column heading (from) on top, row heading (to) on the right, cells hidden until shown column by column"""
    return (f'<div style="display:flex;align-items:center;justify-content:center;gap:10px;font-size:{fs}px"><i>{name}</i> ='
            f'<div style="text-align:center"><div style="font-style:italic;color:#0a7a8a">{top}</div>{amat(labels,rows,fs=fs,tid=tid,blank=True)}</div>'
            f'<span style="font-style:italic;color:#0a7a8a">{side}</span></div>')
def COL(tid,k,n): return f'data-show="#{tid}|'+','.join(f'v{r}_{k}' for r in range(n))+'"'
S=['<style>.T .ex17 ol.parts li{font-size:17px!important}.sm .L .q{font-size:17px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}</style>']
# ================= opening
t=title('11A','Transition matrices: setting up a transition matrix',f'{CAM} · 11A Transition matrices - setting up a transition matrix','11A')
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + two VCAA questions','var(--apk)'),
  ('From a diagram · Example 1','→ You try',None),('From written information · Example 2','→ You try',None),
  ('CAS: enter and store a transition matrix','',None),('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('State','one of the categories something can be in (e.g. a town, a machine that is operating or broken)'),
  ('Transition diagram','one point per state; arrows (and loops) show the % that move each period; the % leaving each point add to 100%',IMG('ex_intro.png',230)),
  ('Transition matrix <i>T</i>','the proportions moving between states: columns = from (this period), rows = to (next period)'),
  ('State matrix <i>S</i><sub><i>n</i></sub>','a column matrix of the numbers in each state after <i>n</i> periods')],
  [('Element t<sub>ij</sub>',F('t<sub><i>ij</i></sub> = proportion moving <b>from</b> column state <i>j</i> <b>to</b> row state <i>i</i>'),'column first: from → to'),
   ('Column sums',F('each column of <i>T</i> adds to 1'),'everyone ends up somewhere'),
   ('% → proportion',F('70% = 0.7'),'divide by 100')],
  f'{CAM}, 11A pp. 551–553; Study Design: construct a transition matrix from a transition diagram or a written description'))

# ================= Do Now 1: VCAA 2025 E1 Q25 (10F)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q25','Review of 10F (last week)',
  '<div style="font-size:28px;margin-top:40px">Consider the matrix <i>G</i> where'+C(EQ('<i>G</i> =',mat([[0,1,0],[1,0,1],[0,0,0]],fs=28,tid='d1')))
  +'Which one of the following correctly describes matrix <i>G</i>?</div>',
  [('Elements','every element is 0 or 1','data-hi="#d1|c0_0,c0_1,c0_2,c1_0,c1_1,c1_2,c2_0,c2_1,c2_2|hy"'),
   ('Rule out','not permutation (row 3 has no 1; row 2 has two) · not identity or diagonal (1s off the leading diagonal)')],
  'a binary matrix: <b>A</b>.','VCAA 2025 General Mathematics Exam 1 Q25 (examiner report: 83% correct)',
  mc=['a binary matrix','a permutation matrix','an identity matrix','a diagonal matrix'],key='A',dis=('B','permutation needs exactly one 1 in every row and column'),stat=('mc',83)))
# ================= Do Now 2: VCAA 2023 E1 Q15 (5B)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2023 Exam 1 Q15','Review of 5B (last term)',
  '<div style="font-size:21px">The number of visitors to a public library each day for 10 consecutive days was recorded.<br>These results are shown in the table below.'
  '<table class="t tight" id="d2" style="font-size:14px;margin:12px auto"><tr><th>Day number</th>'+''.join(f'<td data-i="h{i}">{i+1}</td>' for i in range(10))+'</tr><tr><th>Number of visitors</th>'
  +''.join(f'<td data-i="v{i}">{v}</td>' for i,v in enumerate([337,317,313,335,322,335,322,338,302,349]))+'</tr></table>'
  'The eight-mean smoothed number of visitors with centring for day number 6 is</div>',
  [('First 8','days 2–9: 2584 ÷ 8 = 323','data-hi="#d2|v1,v2,v3,v4,v5,v6,v7,v8|hy"'),('Next 8','days 3–10: 2616 ÷ 8 = 327','data-hi="#d2|v2,v3,v4,v5,v6,v7,v8,v9|hb"'),('Centre','(323 + 327) ÷ 2 = 325')],
  '325: <b>C</b>.','VCAA 2023 General Mathematics Exam 1 Q15 (examiner report: 66% correct)',
  mc=['323','324','325','326','327'],key='C',dis=('A','one 8-mean only (days 2–9), not centred'),stat=('mc',66)))
# ================= Do Now 3: VCAA 2025 E2 Q11b (10D)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q11b','Review of 10D (last week)',
  '<div style="font-size:19px">An early learning centre contains three rooms, Nursery (<i>N</i>), Toddler (<i>T</i>) and Pre-kinder (<i>P</i>).<br>'
  'The Nursery and Toddler rooms each have capacity for eight children and the Pre-kinder room has capacity for 20 children, as shown in matrix <i>C</i> below.'
  +C(EQ('<i>C</i> =',mat([[8],[8],[20]],rl=['N','T','P'],side=True,fs=19)))+'Matrix <i>E</i> shows enrolment numbers for each room for one week, Monday to Friday.'
  +C(EQ('<i>E</i> =',mat([[6,8,8,8,5],[7,8,7,8,6],[18,18,17,15,13]],cl=['Mon','Tue','Wed','Thu','Fri'],rl=['N','T','P'],side=True,fs=19,tid='d3')))
  +'b. The following matrix multiplication has been completed to determine a new matrix, <i>W</i>.'+C(EQ(mat([[1,1,1]],fs=19),'× <i>E</i> = <i>W</i>'))
  +'What information does matrix <i>W</i> provide regarding enrolments at the early learning centre? <span class="muted">(1 mark)</span></div>',
  [('Row of 1s','[1 1 1] × <i>E</i> adds the three rooms in each column','data-hi="#d3|c0_0,c1_0,c2_0|hy"'),('Each column','a column of <i>E</i> = one day, so <i>W</i> = [31 34 32 31 24]')],
  '<i>W</i> gives the <b>total number of children enrolled</b> at the centre on each day, Monday to Friday.','VCAA 2025 General Mathematics Exam 2 Q11 stem and Q11b (examiner report: average 0.6/1)',
  stat=('mark',60)))
sm()
# ================= Do Now 4: VCAA 2024 E2 Q2cii (1G)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q2cii','Review of 1G (last term)',
  ('<div style="font-size:19px">The boxplot below displays the distribution of all gold medal-winning heights for the women’s high jump, <i>Wgold</i>, in metres, for the 19 Olympic Games held from 1948 to 2020.</div>',
   IMG('dn4.png',560),
   '<div style="font-size:19px">c. i. Using the boxplot, show that the lower fence is 1.565 m and the upper fence is 2.325 m.<br>'
   'ii. Referring to the boxplot, the lower fence and the upper fence, <b>explain</b> why no outliers exist. <span class="muted">(1 mark)</span></div>'),
  [('Read off','minimum = 1.67 m, maximum = 2.06 m'),('Compare','1.67 &gt; 1.565 = LF and 2.06 &lt; 2.325 = UF')],
  'The minimum (1.67 m) is above the lower fence (1.565 m) and the maximum (2.06 m) is below the upper fence (2.325 m), so <b>no outliers</b> exist.',
  'VCAA 2024 General Mathematics Exam 2 Q2 stem and Q2cii (examiner report: average 0.8/1)',stat=('mark',80),cmd=('explain',1,'min and max vs the fences')))
sm()

# ================= APK
S.append(qslide('apk','APK 1 of 3 · Year 11 · Cambridge U1&amp;2 4G #16','Setting up a transition matrix',
  '<div style="font-size:28px;margin-top:40px">A charity sends out a monthly letter asking for donations. They notice that 60% of patrons who donated last month will donate this month, while 30% of patrons who did not donate last month will donate this month. Construct a transition matrix that describes how the behaviour of patrons who donate (<i>D</i>) or do not donate (<i>N</i>) changes from month to month.</div>',
  [('TMPL',TM('ap1',['D','N'],[['0.6','0.3'],['0.4','0.7']],'last month','this month',fs=24)),
   ('Column D','donated last month: 60% donate again → 0.6; the other 40% → 0.4',COL('ap1',0,2)),
   ('Column N','did not donate: 30% donate → 0.3; the other 70% → 0.7',COL('ap1',1,2))],
  '',f'{CAM12} · Ch 4 review skills checklist 4G #16 (p. 293) · solution worked for 12MAG',cmd=('Construct',None,'columns = last month')))
T19=mat([[0.1,0.2,0.1,0.2],[0.3,0.4,0.6,0.3],[0.1,0.2,0.2,0.1],[0.5,0.2,0.1,0.4]],cl=['A','F','G','W'],rl=['A','F','G','W'],side=True,fs=16,tid='a2t')
S.append(qslide('apk','APK 2 of 3 · VCAA 2019 Exam 2 Q2b','State matrices (Year 11)',
  '<div style="font-size:16px">The theme park has four locations, Air World (<i>A</i>), Food World (<i>F</i>), Ground World (<i>G</i>) and Water World (<i>W</i>). The number of visitors at each of the four locations is counted every hour.<br>'
  'Let <i>S</i><sub><i>n</i></sub> be the state matrix that shows the number of visitors expected at each location <i>n</i> hours after 10 am on Saturday.<br>The number of visitors expected at each location <i>n</i> hours after 10 am on Saturday can be determined by the matrix recurrence relation below.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[600],[600],[400],[400]],fs=16,tid='a2s')),EQ(', <i>S</i><sub><i>n</i>+1</sub> = <i>T</i> × <i>S</i><sub><i>n</i></sub> &nbsp;where&nbsp; <i>T</i> =',T19),gap=10)
  +'<div style="display:flex;gap:16px;align-items:center"><span>b. <b>Complete</b> the state matrix, <i>S</i><sub>1</sub>, below to show the number of visitors expected at each location at 11 am on Saturday. <span class="muted">(1 mark)</span></span>'
  +EQ('<i>S</i><sub>1</sub> =',mat([['&nbsp;&nbsp;&nbsp;&nbsp;'],[''],[300],['']],rl=['A','F','G','W'],side=True,fs=16))+'</div></div>',
  [('Rule','<i>S</i><sub>1</sub> = <i>T</i> × <i>S</i><sub>0</sub>: each row of <i>T</i> × the column <i>S</i><sub>0</sub>'),
   ('A','0.1 × 600 + 0.2 × 600 + 0.1 × 400 + 0.2 × 400 = 300','data-hi="#a2t|c0_0,c0_1,c0_2,c0_3|hy"'),
   ('F','0.3 × 600 + 0.4 × 600 + 0.6 × 400 + 0.3 × 400 = 780','data-hi="#a2t|c1_0,c1_1,c1_2,c1_3|hy"'),
   ('W','0.5 × 600 + 0.2 × 600 + 0.1 × 400 + 0.4 × 400 = 620','data-hi="#a2t|c3_0,c3_1,c3_2,c3_3|hy"')],
  '<i>S</i><sub>1</sub> = '+mat([[300],[780],[300],[620]],rl=['A','F','G','W'],side=True,fs=20),
  f'VCAA 2019 Further Mathematics Exam 2 Matrices Q2b (examiner report: 84%; Q2 opening stem for 2a left out, as in Edrolo’s reprint) · {EDR12} 5G Q11a (p. 311)',stat=('mark',84),cmd=('Complete',None,'row × column')))
sm()
S.append(qslide('apk','APK 3 of 3 · VCAA 2019 Exam 2 Q3a','State matrices (Year 11)',
  '<div style="font-size:16px">On Sunday, matrix <i>V</i> is used when calculating the expected number of visitors at each location every hour after 10 am. It is assumed that the park will be at its capacity of 2000 visitors for all of Sunday.<br>Let <i>L</i><sub>0</sub> be the state matrix that shows the number of visitors at each location at 10 am on Sunday.<br>The number of visitors expected at each location at 11 am on Sunday can be determined by the matrix product'
  +C(EQ('<i>V</i> × <i>L</i><sub>0</sub> &nbsp;where&nbsp; <i>L</i><sub>0</sub> =',mat([[500],[600],[500],[400]],rl=['A','F','G','W'],side=True,fs=16)),EQ('and <i>V</i> =',mat([[0.3,0.4,0.6,0.3],[0.1,0.2,0.1,0.2],[0.1,0.2,0.2,0.1],[0.5,0.2,0.1,0.4]],cl=['A','F','G','W'],rl=['A','F','G','W'],side=True,fs=16,tid='a3v')),gap=16)
  +'a. Safety restrictions require that all four locations have a maximum of 600 visitors.<br>Which location is expected to have more than 600 visitors at 11 am on Sunday? <span class="muted">(1 mark)</span></div>',
  [('A','0.3 × 500 + 0.4 × 600 + 0.6 × 500 + 0.3 × 400 = 810 &gt; 600','data-hi="#a3v|c0_0,c0_1,c0_2,c0_3|hy"'),
   ('Others','F: 300 · G: 310 · W: 580 (all ≤ 600)')],
  '<b>Air World</b> (810 visitors expected)',f'VCAA 2019 Further Mathematics Exam 2 Matrices Q3a (examiner report: 75%) · {EDR12} 5G Q11b (p. 311)',stat=('mark',75)))
sm()

# ================= Learn 1: from a diagram
S.append(learn('Learn · 11A','From a transition diagram to a transition matrix',
  '<h4>Columns are FROM, rows are TO</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>one row and one column for each state, in the same order</li>'
  '<li>fill one column at a time: every arrow (and loop) LEAVING that state</li>'
  '<li>write each % as a proportion (20% = 0.2)</li><li>each column adds to 1</li></ul>',
  '<div style="display:flex;gap:30px;align-items:center;justify-content:center">'+IMG('ex_intro.png',560)
  +'<div class="frag" style="font-size:24px">'+EQ('<i>T</i> =',mat([[0.8,0.1],[0.2,0.9]],cl=['B','C'],rl=['B','C'],side=True,fs=26))+'<div class="muted" style="font-size:16px;text-align:center">column = rented in · row = returned to</div></div></div>'
  '<div class="frag" style="font-size:20px;text-align:center;margin-top:10px">Column <i>B</i>: 80% stay (loop) + 20% to <i>C</i> = 100% ✓ &nbsp;·&nbsp; Column <i>C</i>: 10% + 90% = 100% ✓</div>',
  'A loop is the % that STAY: it goes on the leading diagonal.',f'{CAM}, 11A p. 551 (own words; diagram from p. 551) · {EDR}, 7G p. 482',
  cards=(kcard('Element t<sub>ij</sub>',F('from column <i>j</i> → to row <i>i</i>')),kcard('Column sums',F('each column adds to 1')))))
# ================= Ex 1 / YT 7I WE2a
L3=['A','W','B']
S.append(qslide('we','Worked example 1 · 11A','Setting up a transition matrix',
  ('<div style="font-size:22px">The diagram gives the weekly return rates of rental cars at three locations: Albury, Wodonga and Benalla. <b>Construct</b> a transition matrix that describes the week-by-week return rates at each of the three locations. Convert the percentages to proportions.</div>',
   IMG('ex1.png',470),''),
  [('TMPL',TM('w1',L3,[['0.7','0.05','0.12'],['0.1','0.8','0.11'],['0.2','0.15','0.77']],'Rented in','Returned to',fs=22)),
   ('Set up','3 locations → 3 × 3; columns = rented in, rows = returned to (both A, W, B)'),
   ('Column A','loop 70%, A → W 10%, A → B 20%',COL('w1',0,3)),
   ('Column W','W → A 5%, loop 80%, W → B 15%',COL('w1',1,3)),
   ('Column B','B → A 12%, B → W 11%, loop 77%',COL('w1',2,3)),
   ('Check','columns: 0.7 + 0.1 + 0.2 = 1 · 0.05 + 0.8 + 0.15 = 1 · 0.12 + 0.11 + 0.77 = 1')],
  '',f'{CAM} · Example 1 (p. 552)',video='Cambridge GO · Example 1 (11A Resources)',cmd=('Construct',None,'one column per state')))
S.append(qslide('yt','You try · Edrolo 7I WE2a','Converting a transition diagram into a transition matrix',
  ('<div style="font-size:24px">Complete the following conversions.<br>a. Convert the following transition diagram into a transition matrix.</div>',IMG('yt1.png',520),''),
  [('TMPL',TM('y1',['R','S','T'],[['0.00','0.05','0.50'],['0.80','0.20','0.00'],['0.20','0.75','0.50']],'from','to',fs=22)),
   ('Set up','3 points → 3 × 3, labelled R, S, T'),
   ('Column R','no loop (0) · R → S 80% · R → T 20%',COL('y1',0,3)),
   ('Column S','S → R 5% · loop 20% · S → T 75%',COL('y1',1,3)),
   ('Column T','T → R 50% · no T → S arrow (0) · loop 50%',COL('y1',2,3))],
  '',f'{EDR} · 7I Worked example 2a (p. 505)',cmd=('Convert',None,'no arrow → 0')))

# ================= Learn 2: from written information
S.append(learn('Learn · 11A','From written information to a transition matrix',
  '<h4>Label first, then fill each column</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>find the states and the time step (day, week, term …)</li>'
  '<li>label columns ‘start / today / this week’ and rows ‘end / tomorrow / next week’</li>'
  '<li>each sentence gives one element: ‘<b>of</b> those in X, …% move <b>to</b> Y’ → column X, row Y</li>'
  '<li>a missing value = 1 − the rest of its column</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:16px;align-items:center;font-size:27px">'
  '<div class="frag">“20% of workers at station <i>A</i> today move to station <i>B</i> tomorrow”</div>'
  '<div class="frag">'+EQ('<i>T</i> =',mat([['·','·'],['<b style="color:#c62828">0.2</b>','·']],cl=['A','B'],rl=['A','B'],side=True,fs=26),'<span class="muted" style="font-size:17px">column <i>A</i> (today), row <i>B</i> (tomorrow)</span>')+'</div>'
  '<div class="frag">so 1 − 0.2 = <b>0.8</b> of station <i>A</i> stay at <i>A</i> (row <i>A</i>, column <i>A</i>)</div></div>',
  'Words like ‘today’, ‘from’, ‘start’ name the COLUMNS.',f'{CAM}, 11A pp. 552–553 (own words) · {EDR}, 7G p. 482',
  cards=(kcard('Columns',F('from · today · start · this week')),kcard('Rows',F('to · tomorrow · end · next week')))))
# ================= Ex 2 / YT 7G WE4
S.append(qslide('we','Worked example 2 · 11A','Setting up a transition matrix',
  '<div style="font-size:24px;margin-top:10px">A factory has a large number of machines. Machines can be in one of two states: operating or broken. Broken machines are repaired and come back into operation, and vice versa. On a given day:'
  '<ul class="bul" style="margin:8px 0 8px 30px"><li>85% of machines that are operational stay operating</li><li>15% of machines that are operating break down</li><li>5% of machines that are broken are repaired and start operating again</li><li>95% of machines that are broken stay broken.</li></ul>'
  '<b>Construct</b> a transition matrix to describe this situation. Use the columns to define the situation at the ‘Start’ of the day and the rows to describe the situation at the ‘End’ of the day.</div>',
  [('TMPL',TM('w2',['O','B'],[['0.85','0.05'],['0.15','0.95']],'Start','End',fs=26)),
   ('Set up','2 states: operating (O), broken (B) → 2 × 2'),
   ('Column O','start operating: 85% stay O, 15% → B',COL('w2',0,2)),
   ('Column B','start broken: 5% → O, 95% stay B',COL('w2',1,2)),
   ('Check','0.85 + 0.15 = 1 · 0.05 + 0.95 = 1')],
  '',f'{CAM} · Example 2 (pp. 552–553)',video='Cambridge GO · Example 2 (11A Resources)',cmd=('Construct',None,'Start = columns')))
S.append(qslide('yt','You try · Edrolo 7G WE4','Constructing a transition matrix',
  '<div style="font-size:26px;margin-top:30px">Johnny is an avid fan of fish, and has two different ponds (A and B) for his Koi fish. The number of Koi fish in each pond can change on a daily basis.'
  '<ul class="bul" style="margin:8px 0 8px 30px"><li>10% of the Koi fish in pond A today will remain in pond A tomorrow.</li><li>15% of the Koi fish in pond B today will be moved to pond A tomorrow.</li></ul>'
  '<b>Construct</b> a transition matrix, <i>T</i>, to represent the movement of Koi fish in each pond from one day to the next.</div>',
  [('TMPL',TM('y2',['A','B'],[['0.10','0.15'],['0.90','0.85']],'today','tomorrow',fs=26)),
   ('Given','t<sub>11</sub> = 0.10 (A → A) · t<sub>12</sub> = 0.15 (B → A)','data-show="#y2|v0_0,v0_1"'),
   ('Columns add to 1','column A: 1 − 0.10 = 0.90 · column B: 1 − 0.15 = 0.85','data-show="#y2|v1_0,v1_1"')],
  '',f'{EDR} · 7G Worked example 4 (pp. 483–484)',cmd=('Construct',None,'missing = 1 − the rest')))

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-entry']
S.append(cas('CAS · 11A','Entering and storing a transition matrix',
  '<div style="font-size:24px">Enter and store the Example 1 transition matrix as <i>t</i>, then check each column adds to 1.</div>'
  +C(EQ('<i>T</i> =',mat([[0.7,0.05,0.12],[0.1,0.8,0.11],[0.2,0.15,0.77]],cl=['A','W','B'],rl=['A','W','B'],fs=26)))
  +'<div style="font-size:19px">Check: multiply a row of 1s by <i>T</i>: [1 1 1] × <i>t</i> should give [1 1 1].</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  [x for x in CS['ti'] if 'Transpose' not in x],[x for x in CS['classpad'] if 'Transpose' not in x],
  '[1 1 1] × <i>t</i> = [1 1 1]: every column adds to 1 ✓ · <i>t</i> is stored for 11B',
  f'Task: card ‘casYouTry’ (Example 1 matrix, {CAM} p. 552) · Steps: CAS guide (planner)'))

# ================= Exit
S.append(qslide('ex','Exit task · VCAA 2017 Exam 2 Q2a, b','Show what you know',
  '<div style="font-size:17px">Junior students at this school must choose one elective activity in each of the four terms in 2018.<br>Students can choose from the areas of performance (<i>P</i>), sport (<i>S</i>) and technology (<i>T</i>).<br>'
  'The transition diagram below shows the way in which junior students are expected to change their choice of elective activity from term to term.'
  '<div style="display:flex;gap:14px;align-items:center">'+IMG('exit1.png',340)+'<div class="ex17">'+plist([('a','Of the junior students who choose performance (<i>P</i>) in one term, what percentage are expected to choose sport (<i>S</i>) the next term? <span class="muted">(1 mark)</span>')])+'</div></div>'
  'Matrix <i>J</i><sub>1</sub> lists the number of junior students who will be in each elective activity in Term 1. &nbsp;'+EQ('<i>J</i><sub>1</sub> =',mat([[300],[240],[210]],rl=['P','S','T'],side=True,fs=17))
  +'<div class="ex17">'+plist([('b','306 junior students are expected to choose sport (<i>S</i>) in Term 2.<br><b>Complete</b> the calculation below to show this. <span class="muted">(1 mark)</span><br>300 × ☐ + 240 × ☐ + 210 × ☐ = 306')])+'</div></div>',
  [('a','arrow from <i>P</i> to <i>S</i>: 40%'),('b','into <i>S</i>: from <i>P</i> 40%, loop at <i>S</i> 60%, from <i>T</i> 20% → 120 + 144 + 42 = 306 ✓')],
  '','VCAA 2017 Further Mathematics Exam 2 Matrices Q2a, b (examiner report: a 95%, b 69%) · Edrolo U3&amp;4 7I Q14',
  cmd=('Complete',None,'proportions, not %'),parts=[('a','<b>40%</b>'),('b','300 × <b>0.4</b> + 240 × <b>0.6</b> + 210 × <b>0.2</b> = 306')]))
sm()

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 11 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='11A' and v.get('url')]))
n=assemble(S,'12MAG · 11A · Setting up a transition matrix',os.path.join(ROOT,'lessons','11A slides.html'))
print(n-1,'slides')
