"""Lesson gm12-u4-10e (10E Matrix inverse, the determinant and matrix equations) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/10E slides.html      Run: python3 tools/deck/gm12-u4-10e/build.py      Screenshots: python3 tools/deck/gm12-u4-10e/shoot.py
Matrices drawn with tools/deck/mx.py.

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- No CFAT this lesson (CFAT 3.10.1 opened 10D; CFAT 3.10.2 opens 10F-10G).
- Do Now: VCAA 2025 Exam 1 Q26 (C, 84%) · VCAA 2026 Exam 1 Q1 (stem plot retyped; C; 2026 report not yet released: no %) ·
          VCAA 2023 Exam 2 Q9 stem + Q9b (t = 1.25; average 0.5/1 = 50%) · VCAA 2025 Exam 2 Q6 stem + Q6a (plot cropped; average 1.1/2 = 55%).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4D #11 (p. 291) and 4E #12 (p. 292) (solutions worked for 12MAG) ·
       VCAA 2017 Further Exam 2 Matrices Q1ci as reprinted in Edrolo U1&2 5F Q15 (p. 302; $3.80; 56% as quoted by Edrolo; card said 60).
- Learn: Cambridge U3&4 10E pp. 513-520 (own words) · Edrolo U3&4 7D pp. 451-453 · Edrolo U1&2 5F pp. 296-297.
- Worked examples: Cambridge U3&4 Examples 24-27 (pp. 513-520). CAS: Cambridge 10E CAS 4 (pp. 516-518), steps from planner/cas-skills.json 'matrix-det-inverse'.
  You trys: YT-10E-24 (written, planner/written-youtrys.json), Edrolo U3&4 7D WE1a (p. 451), 7D WE2 (p. 453), 7D WE1b (CAS, p. 452),
            Edrolo U1&2 5F WE1 (pp. 296-297) and 5F WE2 (p. 297; the card's spare, used because Example 27 is mostly AX = B).
- Exit 1: VCAA 2018 Further Exam 1 Matrices Q1 (= Edrolo U3&4 7D Q15), D, 78%.
- Exit 2: VCAA 2020 Further Exam 2 Matrices Q2 (= Edrolo U3&4 7D Q16), a 37%, b 71%, c 51%.
- Exit 3: VCAA 2016 Further Exam 1 Matrices Q3 (= Edrolo U3&4 7D Q17), E, 63%. (% as quoted by Edrolo from the examiner reports.)
"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat, cells
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-10e')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def FRc(n,d): return f'<span style="display:inline-flex;flex-direction:column;align-items:center;line-height:1.05;vertical-align:middle;margin:0 4px"><span>{n}</span><span style="border-top:1.5px solid currentColor;padding:0 3px">{d}</span></span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
S=['<style>.sm .L .q{font-size:17px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}</style>']
# ================= opening
t=title('10E','Matrix inverse, the determinant and matrix equations',f'{CAM} · 10E Matrix inverse, the determinant and matrix equations','10E')
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills + one VCAA question','var(--apk)'),
  ('Inverses · Example 24','→ You try',None),('Determinant · Example 25','→ You try',None),('Inverse of a 2 × 2 · Example 26','→ You try',None),
  ('CAS: det and inverse','→ You try',None),('Matrix equations · Example 27','→ You try ×2',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Identity matrix <i>I</i>','1s on the leading diagonal, 0s elsewhere: <i>AI</i> = <i>IA</i> = <i>A</i>',mat([[1,0],[0,1]],fs=15)),
  ('Inverse <i>A</i><sup>−1</sup>','<i>AA</i><sup>−1</sup> = <i>A</i><sup>−1</sup><i>A</i> = <i>I</i> (square matrices only)'),
  ('Determinant','a number worked out from a square matrix: det(<i>A</i>)'),
  ('Singular matrix','det = 0: NO inverse')],
  [('Determinant',F('det',mat([['a','b'],['c','d']],fs=15),' = <i>ad</i> − <i>bc</i>'),'2 × 2 only by hand'),
   ('Inverse',F('<i>A</i><sup>−1</sup> = ',FRc(1,'<i>ad</i> − <i>bc</i>'),mat([['d','−b'],['−c','a']],fs=15)),'swap a, d; negate b, c'),
   ('AX = B',F('<i>X</i> = <i>A</i><sup>−1</sup><i>B</i>'),'pre-multiply'),
   ('XA = B',F('<i>X</i> = <i>BA</i><sup>−1</sup>'),'post-multiply')],
  f'{CAM}, 10E pp. 513–520; Study Design: inverse of a matrix, its determinant, and the condition for a matrix to have an inverse'))

# ================= Do Now 1: VCAA 2025 E1 Q26 (10D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q26','Review of 10D (last lesson)',
  '<div style="font-size:26px;margin-top:30px">Consider the matrices <i>A</i>, <i>B</i> and <i>C</i> where'+C(EQ('<i>A</i> =',mat([[2,0],[1,6]],fs=26,tid='d1a')),EQ('<i>B</i> =',mat([[3],[5]],fs=26,tid='d1b')),'and <i>C</i> = <i>AB</i>.',gap=16)
  +'The calculation that correctly determines element <i>c</i><sub>21</sub> is</div>',
  [('c21','row 2 of <i>A</i> × column 1 of <i>B</i>','data-hi="#d1a|c1_0,c1_1|hy;#d1b|c0_0,c1_0|hy"'),('Multiply and add','1 × 3 + 6 × 5')],
  '1 × 3 + 6 × 5: <b>C</b>.','VCAA 2025 General Mathematics Exam 1 Q26 (examiner report: 84% correct)',
  mc=['2 × 3 + 0 × 5','2 × 5 + 3 × 0','1 × 3 + 6 × 5','1 × 5 + 6 × 3'],key='C',dis=('A','row 1 of <i>A</i> gives <i>c</i><sub>11</sub>, not <i>c</i><sub>21</sub>'),stat=('mc',84)))
# ================= Do Now 2: VCAA 2026 E1 Q1 (1F)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q1','Review of 1F (last term)',
  '<div style="font-size:20px">The stem plot below shows the <em class="v">points scored</em> by a National Rugby League team in each of the 25 games it played in the 2025 season.'
  +C(stem('d2',[('0','88'),('1','024444'),('1','56688'),('2','002'),('2','666'),('3','024'),('3','66'),('4','0')],'key: 1|6 = 16 &nbsp;&nbsp; <i>n</i> = 25',fs=22))
  +'The median of <em class="v">points scored</em> is</div>',
  [('Position','<i>n</i> = 25: median is the (25 + 1) ÷ 2 = 13th value'),('Count','0|8 8 → 2 values, 1|0 2 4 4 4 4 → 8 values, then 15, 16, 16, 18, <b>18</b> → 13th')],
  '18: <b>C</b>.','VCAA 2026 General Mathematics Exam 1 Q1 (2026 examiner report not yet released)',
  mc=['16','17','18','20'],key='C'))
# ================= Do Now 3: VCAA 2023 E2 Q9b (10D)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q9b','Review of 10D (last lesson)',
  '<div style="font-size:19px">The circus is held at five different locations, <i>E</i>, <i>F</i>, <i>G</i>, <i>H</i> and <i>I</i>.<br>The table below shows the total revenue for the ticket sales, rounded to the nearest hundred dollars, for the last 20 performances held at each of the five locations.'
  '<table class="t tight" style="font-size:17px;margin:8px auto"><tr><th>Location</th><th><i>E</i></th><th><i>F</i></th><th><i>G</i></th><th><i>H</i></th><th><i>I</i></th></tr><tr><th>Ticket sales</th><td>$960 000</td><td>$990 500</td><td>$940 100</td><td>$920 800</td><td>$901 300</td></tr></table>'
  'The ticket sales information is presented in matrix <i>R</i> below.'+C(EQ('<i>R</i> =',mat([['960 000','990 500','940 100','920 800','901 300']],fs=19)))
  +'The circus would like to increase its total revenue from the ticket sales from all five locations.<br>The circus will use the following matrix calculation to target the next 20 performances.'
  +C(EQ('[<i>t</i>] × <i>R</i> ×',mat([[1],[1],[1],[1],[1]],fs=15)))
  +'b. <b>Determine</b> the value of <i>t</i> if the circus would like to increase its revenue from ticket sales by 25%. <span class="muted">(1 mark)</span></div>',
  [('Summing','<i>R</i> × column of 1s = total revenue from all five locations'),('Increase 25%','100% + 25% = 125% of the total, so multiply by 1.25')],
  '<i>t</i> = <b>1.25</b>','VCAA 2023 General Mathematics Exam 2 Q9 stem and Q9b (examiner report: average 0.5/1)',
  stat=('mark',50),cmd=('Determine',None,'increase by 25% → × 1.25')))
sm()
# ================= Do Now 4: VCAA 2025 E2 Q6a (5A)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 Exam 2 Q6a','Review of 5A (last term)',
  ('<div style="font-size:19px">The time series plot below shows the number of homes sold in a town each month over a four-year period.<br>Month 1 is January 2016 and month 48 is December 2019.</div>',
   IMG('dn4_ts.png',560),
   '<div style="font-size:19px">a. Excluding any possible outliers, <b>identify</b> <b>two</b> qualitative features of the time series plot. <span class="muted">(2 marks)</span></div>'),
  [('Repeating pattern','peaks early in each year, lowest about month 9, 21, 33, 45: every 12 months → seasonality'),('Long-term direction','the peaks and troughs stay at about the same level → no trend')],
  'The time series shows <b>seasonality</b> and <b>no (clear) trend</b>.','VCAA 2025 General Mathematics Exam 2 Q6 stem and Q6a (examiner report: average 1.1/2)',
  stat=('mark',55),cmd=('identify',2,'trend, seasonality, cycles, irregular')))
sm()

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4D #11','The identity matrix',
  '<div style="font-size:34px;margin-top:60px">Construct an identity matrix of size 3×3.</div>',
  [('Square','3 rows and 3 columns'),('Diagonal','1s on the leading diagonal (top left to bottom right), 0s everywhere else')],
  '<i>I</i> = '+mat([[1,0,0],[0,1,0],[0,0,1]],fs=22),f'{CAM12} · Ch 4 review skills checklist 4D #11 (p. 291) · solution worked for 12MAG',cmd=('Construct',None,'1s on the diagonal')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4E #12','Finding an inverse',
  '<div style="font-size:34px;margin-top:60px">Find the inverse of the matrix'+C(mat([[7,2],[-1,3]],fs=34))+'</div>',
  [('Determinant','7 × 3 − 2 × (−1) = 21 + 2 = 23'),('Swap and negate','swap 7 and 3, negate 2 and −1: '+mat([[3,-2],[1,7]],fs=17)),('Divide','multiply by 1/23')],
  FRc(1,23)+' '+mat([[3,-2],[1,7]],fs=20)+' = '+mat([[FRc(3,23),FRc('−2',23)],[FRc(1,23),FRc(7,23)]],fs=20),f'{CAM12} · Ch 4 review skills checklist 4E #12 (p. 292) · solution worked for 12MAG',cmd=('Find',None,'det, swap, negate, divide')))
S.append(qslide('apk','APK · VCAA 2017 Exam 2 Q1ci','Solving a matrix equation (Year 11)',
  '<div style="font-size:26px;margin-top:30px">Consider the matrix equation'+C(EQ(mat([[35,24,60],[28,32,43],[32,30,56]],fs=26),'×',mat([['a'],['b'],['c']],fs=26),'=',mat([['491.55'],['428.00'],['487.60']],fs=26)))
  +'where <i>a</i> = cost of one pie, <i>b</i> = cost of one roll and <i>c</i> = cost of one sandwich.<br>What is the cost of one sandwich? <span class="muted">(1 mark)</span></div>',
  [('Form','<i>MX</i> = <i>B</i>, so <i>X</i> = <i>M</i><sup>−1</sup><i>B</i>'),('CAS','type the inverse of the 3 × 3 matrix × the answer matrix → <i>a</i> = 4.65, <i>b</i> = 4.20, <i>c</i> = 3.80')],
  'One sandwich costs <b>$3.80</b>','VCAA 2017 Further Mathematics Exam 2 Matrices Q1ci (56% correct, quoted by Edrolo) · Edrolo U1&amp;2 5F Q15',stat=('mark',56)))

# ================= Learn 1: identity + inverse
S.append(learn('Learn · 10E','The inverse matrix',
  '<h4>Matrices can’t be divided: we multiply by an inverse</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>the <b>identity matrix</b> <i>I</i> acts like the number 1: <i>AI</i> = <i>IA</i> = <i>A</i></li>'
  '<li><i>A</i> and <i>B</i> are <b>inverses</b> if <i>AB</i> = <i>I</i> and <i>BA</i> = <i>I</i>; we write <i>B</i> = <i>A</i><sup>−1</sup></li>'
  '<li>to show two matrices are inverses: multiply both ways and get <i>I</i> each time</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ(mat([[2,3],[3,5]],fs=24),mat([[5,-3],[-3,2]],fs=24),'=',mat([[1,0],[0,1]],fs=24))+'</div>'
  '<div class="frag">'+EQ(mat([[5,-3],[-3,2]],fs=24),mat([[2,3],[3,5]],fs=24),'=',mat([[1,0],[0,1]],fs=24))+'</div>'
  '<div class="frag">both products are <i>I</i> → inverses ✓</div></div>',
  'Check BOTH orders: AB = I and BA = I.',f'{CAM}, 10E pp. 513–514 (own words) · {EDR}, 7D p. 452',
  cards=(kcard('Inverse',F('<i>AA</i><sup>−1</sup> = <i>A</i><sup>−1</sup><i>A</i> = <i>I</i>')),kcard('Identity',F('<i>AI</i> = <i>IA</i> = <i>A</i>')))))
# ================= Ex 24 / YT-10E-24
S.append(qslide('we','Worked example 24 · 10E','Demonstrating that two matrices are inverses',
  '<div style="font-size:30px;margin-top:40px">Show that the matrices '+EQ('<i>A</i> =',mat([[2,3],[3,5]],fs=30))+' and '+EQ('<i>B</i> =',mat([[5,-3],[-3,2]],fs=30))+' are inverses.</div>',
  [('AB',mat([['2 × 5 + 3 × (−3)','2 × (−3) + 3 × 2'],['3 × 5 + 5 × (−3)','3 × (−3) + 5 × 2']],fs=16)+' = '+mat([[1,0],[0,1]],fs=16)),
   ('BA',mat([['5 × 2 + (−3) × 3','5 × 3 + (−3) × 5'],['(−3) × 2 + 2 × 3','(−3) × 3 + 2 × 5']],fs=16)+' = '+mat([[1,0],[0,1]],fs=16))],
  'Because <i>AB</i> = <i>I</i> and <i>BA</i> = <i>I</i>, <i>A</i> and <i>B</i> are inverses.',f'{CAM} · Example 24 (pp. 513–514)',video='Cambridge GO · Example 24 (10E Resources)',cmd=('Show',None,'multiply both ways')))
S.append(qslide('yt','You try · written for 12MAG','Demonstrating that two matrices are inverses',
  '<div style="font-size:30px;margin-top:40px">Show that the matrices '+EQ('<i>A</i> =',mat([[3,5],[1,2]],fs=30))+' and '+EQ('<i>B</i> =',mat([[2,-5],[-1,3]],fs=30))+' are inverses.</div>',
  [('AB',mat([['3 × 2 + 5 × (−1)','3 × (−5) + 5 × 3'],['1 × 2 + 2 × (−1)','1 × (−5) + 2 × 3']],fs=16)+' = '+mat([[1,0],[0,1]],fs=16)),
   ('BA',mat([['2 × 3 + (−5) × 1','2 × 5 + (−5) × 2'],['−1 × 3 + 3 × 1','−1 × 5 + 3 × 2']],fs=16)+' = '+mat([[1,0],[0,1]],fs=16))],
  'Because <i>AB</i> = <i>I</i> and <i>BA</i> = <i>I</i>, <i>A</i> and <i>B</i> are inverses.','Written for 12MAG (modelled on Cambridge Example 24; no Edrolo match) · planner/written-youtrys.json YT-10E-24',cmd=('Show',None,'multiply both ways')))

# ================= Learn 2: determinant
S.append(learn('Learn · 10E','The determinant of a 2 × 2 matrix',
  '<h4>One number that tells you if an inverse exists</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>det(<i>A</i>) = <i>ad</i> − <i>bc</i>: leading diagonal product minus the other diagonal product</li>'
  '<li>it can be positive, negative or zero</li>'
  '<li>det = 0 → <b>singular</b>: no inverse</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">det'+mat([['<b style="color:#1565c0">a</b>','<b style="color:#c62828">b</b>'],['<b style="color:#c62828">c</b>','<b style="color:#1565c0">d</b>']],fs=26)+' = <b style="color:#1565c0">ad</b> − <b style="color:#c62828">bc</b></div>'
  '<div class="frag">det'+mat([[2,3],[2,3]],fs=26)+' = 6 − 6 = 0 → no inverse</div></div>',
  'Down-right first, then subtract down-left.',f'{CAM}, 10E pp. 514–515 (own words) · {EDR}, 7D p. 451',
  cards=(kcard('Determinant',F('det(<i>A</i>) = <i>ad</i> − <i>bc</i>')),kcard('Singular',F('det = 0 → no inverse')))))
# ================= Ex 25 / YT 7D WE1a
S.append(qslide('we','Worked example 25 · 10E','Finding the determinant of a 2 × 2 matrix',
  '<div style="font-size:30px;margin-top:30px">Find the determinant of the matrices:'+plist([('a','<i>A</i> = '+mat([[2,3],[3,5]],fs=28)),('b','<i>B</i> = '+mat([[2,3],[2,3]],fs=28)),('c','<i>C</i> = '+mat([[2,4],[2,3]],fs=28))])+'</div>',
  [('Rule','det = <i>a</i> × <i>d</i> − <i>b</i> × <i>c</i>'),('a','2 × 5 − 3 × 3'),('b','2 × 3 − 2 × 3'),('c','2 × 3 − 2 × 4')],
  '',f'{CAM} · Example 25 (p. 515)',video='Cambridge GO · Example 25 (10E Resources)',
  parts=[('a','det(<i>A</i>) = 1'),('b','det(<i>B</i>) = 0'),('c','det(<i>C</i>) = −2')]))
S.append(qslide('yt','You try · Edrolo 7D WE1a','Calculating the determinant of a matrix',
  '<div style="font-size:30px;margin-top:40px">'+C(EQ('<i>A</i> =',mat([[4,2,13],[6,0,0],[0,0,3]],fs=28)),EQ('<i>B</i> =',mat([[2,2],[3,1]],fs=28)))+'a. Find the determinant of <i>B</i>.</div>',
  [('Rule','det(<i>B</i>) = <i>ad</i> − <i>bc</i>'),('Substitute','2 × 1 − 2 × 3 = 2 − 6')],
  'det(<i>B</i>) = <b>−4</b>',f'{EDR} · 7D Worked example 1a (p. 451)',cmd=('Find',None,'ad − bc')))

# ================= Learn 3: inverse rule
S.append(learn('Learn · 10E','The inverse of a 2 × 2 matrix',
  '<h4>det, swap, negate, divide</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>find det(<i>A</i>) first: if it is 0, stop (no inverse)</li>'
  '<li><b>swap</b> <i>a</i> and <i>d</i>, <b>negate</b> <i>b</i> and <i>c</i></li>'
  '<li>multiply by 1 ÷ det(<i>A</i>)</li><li>bigger matrices: use CAS</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ('<i>A</i> =',mat([['a','b'],['c','d']],fs=26))+'</div>'
  '<div class="frag">'+EQ('<i>A</i><sup>−1</sup> =',FRc(1,'<i>ad</i> − <i>bc</i>'),mat([['d','−b'],['−c','a']],fs=26))+'</div>'
  '<div class="frag">provided <i>ad</i> − <i>bc</i> ≠ 0</div></div>',
  'Check: A × A⁻¹ should give I.',f'{CAM}, 10E pp. 515–516 (own words) · {EDR}, 7D p. 452',
  cards=(kcard('Inverse',F('<i>A</i><sup>−1</sup> = ',FRc(1,'det(<i>A</i>)'),mat([['d','−b'],['−c','a']],fs=14))),kcard('Exists if',F('det(<i>A</i>) ≠ 0')))))
# ================= Ex 26 / YT 7D WE2
S.append(qslide('we','Worked example 26 · 10E','Using the rule to find the inverse of a 2 × 2 matrix',
  '<div style="font-size:30px;margin-top:40px">Find the inverse of the following matrices.'+plist([('a','<i>A</i> = '+mat([[2,2],[3,4]],fs=28)),('b','<i>B</i> = '+mat([[2,3],[2,3]],fs=28))])+'</div>',
  [('a det','2 × 4 − 3 × 2 = 2'),('a inverse',EQ(FRc(1,2),mat([[4,-2],[-3,2]],fs=17))),('b det','2 × 3 − 2 × 3 = 0')],
  '',f'{CAM} · Example 26 (p. 516)',video='Cambridge GO · Example 26 (10E Resources)',
  parts=[('a','<i>A</i><sup>−1</sup> = '+mat([[2,-1],[-1.5,1]],fs=18)),('b','det(<i>B</i>) = 0, so <i>B</i> does not have an inverse.')]))
S.append(qslide('yt','You try · Edrolo 7D WE2','Calculating the inverse of a matrix',
  '<div style="font-size:30px;margin-top:40px">'+C(EQ('<i>A</i> =',mat([[7,5],[2,3]],fs=30)))+plist([('a','Does the inverse of <i>A</i> exist?'),('b','Calculate <i>A</i><sup>−1</sup>.')])+'</div>',
  [('a','det(<i>A</i>) = 7 × 3 − 5 × 2 = 21 − 10 = 11 ≠ 0'),('b',EQ(FRc(1,'7 × 3 − 5 × 2'),mat([[3,-5],[-2,7]],fs=17),'=',FRc(1,11),mat([[3,-5],[-2,7]],fs=17)))],
  '',f'{EDR} · 7D Worked example 2 (p. 453)',
  parts=[('a','Yes: det(<i>A</i>) ≠ 0, so the inverse is defined.'),('b','<i>A</i><sup>−1</sup> = '+mat([[FRc(3,11),FRc('−5',11)],[FRc('−2',11),FRc(7,11)]],fs=17))]))

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-det-inverse']
S.append(cas('CAS · 10E','Determinant and inverse of an n × n matrix',
  '<div style="font-size:24px">If</div>'+C(EQ('<i>A</i> =',mat([[1,2,3],[4,1,0],[2,0,2]],fs=26)))+'<div style="font-size:24px">find det(<i>A</i>) and <i>A</i><sup>−1</sup>.</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'],CS['classpad'],'det(<i>A</i>) = −20 · <i>A</i><sup>−1</sup> = '+mat([[FRc('−1',10),FRc(1,5),FRc(3,20)],[FRc(2,5),FRc(1,5),FRc('−3',5)],[FRc(1,10),FRc('−1',5),FRc(7,20)]],fs=13),
  f'{CAM} · 10E CAS 4 (pp. 516–518) · Steps: CAS guide (planner)'))
S.append(qslide('yt','You try · Edrolo 7D WE1b','Determinant on CAS',
  '<div style="font-size:30px;margin-top:40px">'+C(EQ('<i>A</i> =',mat([[4,2,13],[6,0,0],[0,0,3]],fs=28)),EQ('<i>B</i> =',mat([[2,2],[3,1]],fs=28)))+'b. Use a CAS to find the determinant of <i>A</i>.</div>',
  [('TI-Nspire','Menu › 7: Matrix &amp; Vector › 3: Determinant, enter <i>A</i>, enter'),('ClassPad','Action › Matrix › Calculation › det, enter <i>A</i>, EXE')],
  'det(<i>A</i>) = <b>−36</b>',f'{EDR} · 7D Worked example 1b (p. 452)',cmd=('Use',None,'3 × 3: CAS only')))

# ================= Learn 4: matrix equations
S.append(learn('Learn · 10E','Solving matrix equations',
  '<h4>Undo a matrix by multiplying by its inverse, on the SAME side</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><i>B</i> + <i>X</i> = <i>C</i> → <i>X</i> = <i>C</i> − <i>B</i></li>'
  '<li><i>BX</i> = <i>C</i> (<i>B</i> on the left) → pre-multiply: <i>X</i> = <i>B</i><sup>−1</sup><i>C</i></li>'
  '<li><i>XB</i> = <i>C</i> (<i>B</i> on the right) → post-multiply: <i>X</i> = <i>CB</i><sup>−1</sup></li>'
  '<li>order matters: <i>B</i><sup>−1</sup><i>C</i> ≠ <i>CB</i><sup>−1</sup> in general</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:14px;align-items:center;font-size:26px">'
  '<div class="frag"><i>BX</i> = <i>C</i></div><div class="frag"><b style="color:#c62828">B</b><sup style="color:#c62828">−1</sup><i>BX</i> = <b style="color:#c62828">B</b><sup style="color:#c62828">−1</sup><i>C</i></div>'
  '<div class="frag"><i>IX</i> = <i>B</i><sup>−1</sup><i>C</i></div><div class="frag"><i>X</i> = <i>B</i><sup>−1</sup><i>C</i></div></div>',
  'Write the order of X first: it tells you if the product is defined.',f'{CAM}, 10E pp. 518–520 (own words) · {EDR12}, 5F p. 296',
  cards=(kcard('AX = B',F('<i>X</i> = <i>A</i><sup>−1</sup><i>B</i>')),kcard('XA = B',F('<i>X</i> = <i>BA</i><sup>−1</sup>')))))
# ================= Ex 27 / YT 5F WE1, WE2
G27=C(EQ('Let <i>A</i> =',mat([[1,2,1],[2,1,3],[1,1,1]],fs=20)),EQ('<i>B</i> =',mat([[2,1],[3,2]],fs=20)),EQ('<i>C</i> =',mat([[8,-1],[4,6]],fs=20)),EQ('<i>D</i> =',mat([[2],[3]],fs=20)),EQ('and <i>E</i> =',mat([[2],[3],[1]],fs=20)),gap=14)
QL=[('a','<i>B</i> + <i>X</i> = <i>C</i>'),('b','<i>BX</i> = <i>C</i>'),('c','<i>XB</i> = <i>C</i>'),('d','<i>BX</i> = <i>D</i>'),('e','<i>AX</i> = <i>E</i>'),('f',EQ('<i>BX</i> +',mat([[4],[5]],fs=18),'= <i>D</i>'))]
BI=('B inverse','det(<i>B</i>) = 4 − 3 = 1, <i>B</i><sup>−1</sup> = '+mat([[2,-1],[-3,2]],fs=15))
for half,(lo,hi_),steps,parts_ in ((1,(0,3),[('a','<i>X</i> = <i>C</i> − <i>B</i>'),BI,('b','pre-multiply: <i>X</i> = <i>B</i><sup>−1</sup><i>C</i>'),('c','post-multiply: <i>X</i> = <i>CB</i><sup>−1</sup>')],
                                    [('a','<i>X</i> = '+mat([[6,-2],[1,4]],fs=17)),('b','<i>X</i> = '+mat([[12,-8],[-16,15]],fs=17)),('c','<i>X</i> = '+mat([[19,-10],[-10,8]],fs=17))]),
                                   (2,(3,6),[BI,('d','pre-multiply: <i>X</i> = <i>B</i><sup>−1</sup><i>D</i>'),('e','<i>X</i> = <i>A</i><sup>−1</sup><i>E</i> (CAS for the 3 × 3)'),('f','<i>BX</i> = <i>D</i> − '+mat([[4],[5]],fs=14)+', so <i>X</i> = <i>B</i><sup>−1</sup>'+mat([[-2],[-2]],fs=14))],
                                    [('d','<i>X</i> = '+mat([[1],[0]],fs=17)),('e','<i>X</i> = '+mat([[-2],[1],[2]],fs=17)),('f','<i>X</i> = '+mat([[-2],[2]],fs=17))])):
    S.append(qslide('we',f'Worked example 27 ({"a–c" if half==1 else "d–f"}) · 10E','Solving matrix equations',
      '<div style="font-size:22px">'+G27+'Solve each of the following matrix equations for <i>X</i>'+plist(QL[lo:hi_])+'</div>',
      steps,'',f'{CAM} · Example 27 (pp. 518–520)',video='Cambridge GO · Example 27 (10E Resources)',parts=parts_))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5F WE1','Solving matrix equations',
  '<div style="font-size:30px;margin-top:40px">If '+EQ('<i>A</i> =',mat([[5,-3],[4,2]],fs=28))+' and '+EQ('<i>B</i> =',mat([[5,2],[6,10]],fs=28))+', solve the following matrix equations for <i>X</i>.'
  +plist([('a','<i>A</i> + <i>X</i> = <i>B</i>'),('b','3<i>X</i> = <i>A</i>')])+'</div>',
  [('a','<i>X</i> = <i>B</i> − <i>A</i> = '+mat([['5 − 5','2 − (−3)'],['6 − 4','10 − 2']],fs=16)),('b','<i>X</i> = '+FRc(1,3)+'<i>A</i>')],
  '',f'{EDR12} · 5F Worked example 1 (pp. 296–297)',
  parts=[('a','<i>X</i> = '+mat([[0,5],[2,8]],fs=17)),('b','<i>X</i> = '+mat([[FRc(5,3),-1],[FRc(4,3),FRc(2,3)]],fs=17))]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5F WE2','Solving AX = B',
  '<div style="font-size:30px;margin-top:40px">Consider the matrix equation <i>AX</i> = <i>B</i>.<br>If '+EQ('<i>A</i> =',mat([[4,-1],[2,3]],fs=28))+' and '+EQ('<i>B</i> =',mat([[18],[16]],fs=28))+', solve for matrix <i>X</i>.</div>',
  [('Rearrange','pre-multiply both sides by <i>A</i><sup>−1</sup>: <i>X</i> = <i>A</i><sup>−1</sup><i>B</i>'),('Substitute',EQ('<i>X</i> =',mat([[4,-1],[2,3]],fs=17,sup='−1'),mat([[18],[16]],fs=17))),('Inverse','det = 14: '+FRc(1,14)+mat([[3,1],[-2,4]],fs=15))],
  '<i>X</i> = '+mat([[5],[2]],fs=20),f'{EDR12} · 5F Worked example 2 (p. 297)',cmd=('solve',None,'pre-multiply by the inverse')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 1 Q1','Show what you know',
  '<div style="font-size:26px;margin-top:30px">Which of the following matrices has a determinant of zero?</div>',
  [('Rule','det = <i>ad</i> − <i>bc</i>'),('Check','A: −1 · B: 1 · C: 6 + 6 = 12 · D: 12 − 12 = 0 · E: −8')],
  mat([[3,6],[2,4]],fs=18)+': <b>D</b>.','VCAA 2018 Further Mathematics Exam 1 Matrices Q1 (78% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7D Q15',
  mc=[mat([[0,1],[1,0]],fs=20),mat([[1,0],[0,1]],fs=20),mat([[1,2],[-3,6]],fs=20),mat([[3,6],[2,4]],fs=20),mat([[4,0],[0,-2]],fs=20)],key='D',stat=('mc',78)))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2020 Exam 2 Q2','Show what you know',
  '<div style="font-size:22px;margin-top:10px">The preferred number of cafes (<i>x</i>) and sandwich bars (<i>y</i>) in Grandmall’s food court can be determined by solving the following equations written in matrix form.'
  +C(EQ(mat([[5,-9],[4,-7]],fs=24),mat([['x'],['y']],fs=24),'=',mat([[7],[6]],fs=24)))
  +plist([('a','The value of the determinant of the 2 × 2 matrix is 1.<br><b>Use</b> this information to <b>explain</b> why this matrix has an inverse. <span class="muted">(1 mark)</span>'),
          ('b','<b>Write</b> the three missing values of the inverse matrix that can be used to solve these equations. <span class="muted">(1 mark)</span> '+mat([['',9],['','']],fs=18)),
          ('c','<b>Determine</b> the preferred number of sandwich bars for Grandmall’s food court. <span class="muted">(1 mark)</span>')])+'</div>',
  [('a','an inverse exists when det ≠ 0'),('b',EQ(FRc(1,1),mat([[-7,9],[-4,5]],fs=15))),('c',mat([[-7,9],[-4,5]],fs=15)+mat([[7],[6]],fs=15)+' = '+mat([['−49 + 54'],['−28 + 30']],fs=15))],
  '',f'VCAA 2020 Further Mathematics Exam 2 Matrices Q2 (a 37%, b 71%, c 51% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7D Q16',
  cmd=('explain',None,'det ≠ 0'),
  parts=[('a','The determinant is not zero (it is 1), so the matrix has an inverse.'),('b',mat([[-7,9],[-4,5]],fs=17)),('c','<i>y</i> = 2: two sandwich bars')]))
sm()
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2016 Exam 1 Q3','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The following matrix equation represents a pair of simultaneous linear equations.'+C(EQ(mat([[12,9],['m',3]],fs=26),mat([['x'],['y']],fs=26),'=',mat([[6],[6]],fs=26)))
  +'These simultaneous linear equations have no unique solution when <i>m</i> is equal to</div>',
  [('No unique solution','the matrix has no inverse: det = 0'),('Solve','12 × 3 − 9 × <i>m</i> = 0 → 36 = 9<i>m</i> → <i>m</i> = 4')],
  '<i>m</i> = 4: <b>E</b>.','VCAA 2016 Further Mathematics Exam 1 Matrices Q3 (63% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7D Q17',
  mc=['−4','−3','0','3','4'],key='E',dis=('A','sign slip: 36 + 9m = 0'),stat=('mc',63)))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 10 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='10E' and v.get('url')]))
n=assemble(S,'12MAG · 10E · Inverse, determinant and matrix equations',os.path.join(ROOT,'lessons','10E slides.html'))
print(n-1,'slides')
