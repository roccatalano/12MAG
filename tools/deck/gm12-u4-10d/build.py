"""Lesson gm12-u4-10d (10D Matrix arithmetic: the product of two matrices) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/10D slides.html      Run: python3 tools/deck/gm12-u4-10d/build.py      Screenshots: python3 tools/deck/gm12-u4-10d/shoot.py
Matrices drawn with tools/deck/mx.py.

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- CFAT 3.10.1 (10A-10C) first (planner card).
- Do Now: VCAA 2024 Exam 1 Q26 (B, 76%) · VCAA 2024 Exam 1 Q8 (scatterplot cropped; B, 73%) ·
          VCAA 2024 Exam 2 Q9 stem + Q9c (average 0.7/1 = 70%) · VCAA 2026 Exam 2 Q5 stem + Q5b (scatterplot cropped; 2026 report not yet released: no %).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4D #7 and #9 (p. 291; solutions worked for 12MAG) ·
       VCAA 2020 Further Exam 1 Matrices Q2 (= Edrolo U1&2 5C Q16), E, 79% (card).
- Learn: Cambridge U3&4 10D pp. 499-507 (own words) · Edrolo U3&4 7C pp. 439-444.
- Worked examples: Cambridge U3&4 Examples 17-23 (pp. 500-508; Ex 23b solution printed '(2A + B)²': the question's (2A − B)² is used).
  You trys: Edrolo U3&4 7C WE1 (p. 440), Edrolo U1&2 5C WE1 (p. 270), YT-10D-19 (written, planner/written-youtrys.json),
            Edrolo U3&4 7C WE2 (p. 441), 7C WE3 (p. 443), Edrolo U1&2 5D WE1 (pp. 278-279), Edrolo U3&4 7C WE4 (p. 444).
- CAS: planner/cas-skills.json 'matrix-operations'; task = Cambridge 10D CAS 3 (p. 504).
- Exit 1: VCAA 2017 Further Exam 2 Matrices Q1 stem + Q1a (= Edrolo U3&4 7C Q17), 159, 89%.
- Exit 2: VCAA 2018 Further Exam 1 Matrices Q2 (= Edrolo U3&4 7C Q18), E, 68%. (% as quoted by Edrolo from the examiner reports.)
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-10d')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def grid(slide,cols=3,gap=4): return slide.replace('<div class="mc"',f'<div class="mc" style="display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px"',1)
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)

S=['<style>.sm .L .q{font-size:17px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}</style>']
# ================= opening
t=title('10D','Matrix arithmetic: the product of two matrices',f'{CAM} · 10D Matrix arithmetic: the product of two matrices','10D',
        flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks'))
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 3.10.1','· 10A–10C · 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills + one VCAA question','var(--apk)'),
  ('Defined? order? · Examples 17–18','→ You try',None),('Row × column · Examples 19–20','→ You try',None),('CAS: multiplying matrices','',None),
  ('Summing matrices · Examples 21–22','→ You try',None),('Powers · Example 23','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Product defined','columns of the FIRST matrix = rows of the SECOND matrix'),
  ('Order of AB','(rows of A) × (columns of B): the two outside numbers'),
  ('Row × column','multiply matching elements, then add'),
  ('Summing matrix','a row or column matrix of 1s',mat([[1],[1],[1]],fs=15)+' '+mat([[1,1]],fs=15)),
  ('Power','<i>A</i><sup>2</sup> = <i>A</i> × <i>A</i>: only square matrices')],
  [('Defined?',F('(<i>m</i> × <b><i>n</i></b>)(<b><i>n</i></b> × <i>s</i>)'),'inside numbers equal'),
   ('Order',F('<i>AB</i> is <i>m</i> × <i>s</i>'),'outside numbers'),
   ('Element',F('<i>c<sub>ij</sub></i> = row <i>i</i> of <i>A</i> · column <i>j</i> of <i>B</i>'),'multiply and add'),
   ('Order matters',F('<i>AB</i> ≠ <i>BA</i>'),'in general')],
  f'{CAM}, 10D pp. 499–507; Study Design: elementary matrix operations (product and power)'))
S.append(cfat('CFAT 3.10.1','Matrices: types, addition, scalars and transpose','10A–10C',15,'CFAT 3.10.1 (10A–10C) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now 1: VCAA 2024 E1 Q26 (10C)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q26','Review of 10C (last lesson)',
  '<div style="font-size:26px;margin-top:30px">A market stall sells three types of candles.<br>The cost of each type of candle is shown in matrix <i>C</i> below.'+C('<i>C</i> = '+mat([[25,32,43]],fs=26))
  +'Towards the end of the day, the cost of each item is discounted by 15%.<br>Which one of the following expressions can be used to determine each discounted price?</div>',
  [('Discount','the customer pays 100% − 15% = 85% of the price'),('Scalar','85% = 0.85, so multiply every element by 0.85')],
  '0.85<i>C</i>: <b>B</b>.','VCAA 2024 General Mathematics Exam 1 Q26 (examiner report: 76% correct)',
  mc=['0.15<i>C</i>','0.85<i>C</i>','8.5<i>C</i>','15<i>C</i>'],key='B',dis=('A','0.15<i>C</i> is only the discount, not the new price'),stat=('mc',76)))
# ================= Do Now 2: VCAA 2024 E1 Q8 (3A)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q8','Review of 3A (last term)',
  ('<div style="font-size:17px">The scatterplot below displays the average number of female athletes per competing nation, <em class="v">females</em>, against the number of the Summer Olympic Games, <em class="v">number</em>, from the first Olympic Games, in 1896, to the 29th Olympic Games, held in 2021.<br>A least squares line has been fitted to the scatterplot.</div>',
   IMG('dn2_scatter.png',500),
   '<div style="font-size:17px">The equation of the least squares line is closest to</div>'),
  [('Variables','<em class="v">females</em> is on the vertical axis, so the equation starts “<em class="v">females</em> =” (C, D out)'),('Intercept','the line crosses <em class="v">number</em> ≈ 3.7: extending it back, <em class="v">females</em> ≈ −3.4 at 0'),('Slope','from (5, 1.2) to (30, 24): 22.8 ÷ 25 ≈ 0.91')],
  '<em class="v">females</em> = −3.39 + 0.91 × <em class="v">number</em>: <b>B</b>.','VCAA 2024 General Mathematics Exam 1 Q8 (examiner report: 73% correct)',
  mc=['<em class="v">females</em> = −4.87 + 1.02 × <em class="v">number</em>','<em class="v">females</em> = −3.39 + 0.91 × <em class="v">number</em>','<em class="v">number</em> = −3.39 + 0.91 × <em class="v">females</em>','<em class="v">number</em> = −0.91 + 3.39 × <em class="v">females</em>'],key='B',stat=('mc',73)))
sm()
# ================= Do Now 3: VCAA 2024 E2 Q9c (10C)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q9c','Review of 10C (last lesson)',
  '<div style="font-size:22px">Vince works on a construction site.<br>The amount Vince gets paid depends on the type of shift he works, as shown in the table below.'
  '<table class="t tight" style="font-size:20px;margin:10px auto"><tr><th>Shift type</th><th>Normal</th><th>Overtime</th><th>Weekend</th></tr><tr><th>Hourly rate of pay ($ per hour)</th><td>36</td><td>54</td><td>72</td></tr></table>'
  'Vince will receive $90 per hour if he works a public holiday shift.<br>Matrix <i>Q</i>, as calculated below, can be used to show Vince’s hourly rate for each type of shift.'
  +C('<span style="line-height:2"><i>Q</i> = <i>n</i> × '+mat([[1,1.5,2,'<i>p</i>']],fs=22,tid='d3a')+'<br>&nbsp;&nbsp;&nbsp;&nbsp; = '+mat([[36,54,72,90]],fs=22,tid='d3b')+'</span>')
  +'c. <b>Write</b> the values of <i>n</i> and <i>p</i> in the boxes below. <span class="muted">(1 mark)</span></div>',
  [('n','<i>n</i> × 1 = 36, so <i>n</i> = 36','data-hi="#d3a|c0_0|hy;#d3b|c0_0|hy"'),('p','36 × <i>p</i> = 90, so <i>p</i> = 90 ÷ 36','data-hi="#d3a|c0_3|hb;#d3b|c0_3|hb"')],
  '<i>n</i> = <b>36</b> &nbsp;&nbsp; <i>p</i> = <b>2.5</b>','VCAA 2024 General Mathematics Exam 2 Q9 stem and Q9c (examiner report: average 0.7/1)',
  stat=('mark',70),cmd=('Write',1,'match the elements')))
# ================= Do Now 4: VCAA 2026 E2 Q5b (3B)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q5b','Review of 3B (last term)',
  ('<div style="font-size:17px">The <em class="v">happiness index</em>, a score from 0 to 10, and the average annual <em class="v">income</em>, in dollars per person, were collected for 40 different countries. The data is shown in the scatterplot below.</div>',
   '<div style="display:flex;align-items:center;gap:6px">'+IMG('dn4_scatter.png',520)+'</div>',
   '<div style="font-size:17px">a. A least squares line with <em class="v">happiness index</em> as the response variable is fitted to this data set.<br>The equation of the least squares line is<br>&nbsp;&nbsp;<em class="v">happiness index</em> = 4.36 + 0.0000154 × <em class="v">income</em><br>'
   'b. If the average annual <em class="v">income</em> per person in a particular country is $85 000, <b>use</b> the equation of the least squares line from <b>part a</b> to <b>predict</b> the value of the <em class="v">happiness index</em> for this country. <span class="muted">(1 mark)</span></div>'),
  [fx('h','<em class="v">happiness index</em>',F('4.36 + 0.0000154 × ',V('income','85 000')),'5.669')],
  '<em class="v">happiness index</em> ≈ <b>5.67</b>','VCAA 2026 General Mathematics Exam 2 Q5 stem, Q5a equation and Q5b (2026 examiner report not yet released)',
  cmd=('predict',1,'substitute into the equation')))
sm()

# ================= APK
A7=[[3],[-2]]; B7=[[7,5],[-3,9]]
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4D #7','Is matrix multiplication possible?',
  '<div style="font-size:30px;margin-top:40px">State whether it is possible to find <i>AB</i> or <i>BA</i> for the following matrices:'+C(mat(A7,name='A',fs=30),mat(B7,name='B',fs=30))+'</div>',
  [('Orders','<i>A</i> is 2 × 1, <i>B</i> is 2 × 2'),('AB','(2 × <b>1</b>)(<b>2</b> × 2): 1 ≠ 2 → not possible'),('BA','(2 × <b>2</b>)(<b>2</b> × 1): 2 = 2 → possible, order 2 × 1')],
  '<i>AB</i> is <b>not possible</b>; <i>BA</i> <b>is possible</b> (<i>BA</i> = '+mat([[11],[-27]],fs=20)+')',f'{CAM12} · Ch 4 review skills checklist 4D #7 (p. 291) · solution worked for 12MAG',cmd=('State',None,'check the inside numbers')))
A9=[[5,2],[-1,0],[1,4]]; B9=[[3,1,9],[-4,-5,0]]
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4D #9','Matrix multiplication by hand',
  '<div style="font-size:30px;margin-top:40px">Calculate the following matrix multiplication by hand:'+C(EQ(mat(A9,fs=30,tid='a9'),mat(B9,fs=30,tid='a9b')))+'</div>',
  [('Order','(3 × <b>2</b>)(<b>2</b> × 3): defined, answer is 3 × 3'),('Row 1','5 × 3 + 2 × (−4) = 7 · 5 × 1 + 2 × (−5) = −5 · 5 × 9 + 2 × 0 = 45','data-hi="#a9|c0_0,c0_1|hy"'),
   ('Row 2','−1 × 3 + 0 = −3 · −1 × 1 + 0 = −1 · −1 × 9 + 0 = −9','data-hi="#a9|c1_0,c1_1|hb"'),('Row 3','1 × 3 + 4 × (−4) = −13 · 1 × 1 + 4 × (−5) = −19 · 1 × 9 + 0 = 9','data-hi="#a9|c2_0,c2_1|hg"')],
  mat([[7,-5,45],[-3,-1,-9],[-13,-19,9]],fs=22),f'{CAM12} · Ch 4 review skills checklist 4D #9 (p. 291) · solution worked for 12MAG',cmd=('Calculate',None,'row × column, then add')))
A20=[[1,2],[0,3],[1,0],[4,5]]; B20=[[2,0,3,1],[4,5,2,0]]
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q2','Finding one element of a product',
  '<div style="font-size:24px;margin-top:20px">'+C(EQ('Matrix <i>A</i> =',mat(A20,fs=24,tid='p1')),EQ('and matrix <i>B</i> =',mat(B20,fs=24,tid='p1b')),gap=20)
  +'Matrix <i>Q</i> = <i>A</i> × <i>B</i>.<br>The element in row <i>i</i> and column <i>j</i> of matrix <i>Q</i> is <i>q<sub>ij</sub></i>.<br>Element <i>q</i><sub>41</sub> is determined by the calculation</div>',
  [('q41','row 4 of <i>A</i> × column 1 of <i>B</i>','data-hi="#p1|c3_0,c3_1|hy;#p1b|c0_0,c1_0|hy"'),('Multiply and add','4 × 2 + 5 × 4')],
  '4 × 2 + 5 × 4: <b>E</b>.','VCAA 2020 Further Mathematics Exam 1 Matrices Q2 (79% correct, quoted by Edrolo) · Edrolo U1&amp;2 5C Q16',
  mc=['0 × 0 + 3 × 5','1 × 1 + 2 × 0','1 × 2 + 2 × 4','4 × 1 + 5 × 0','4 × 2 + 5 × 4'],key='E',dis=('D','row 4 of <i>A</i> but row 1 of <i>B</i>: use COLUMN 1 of <i>B</i>'),stat=('mc',79)))

# ================= Learn 1: defined? order?
S.append(learn('Learn · 10D','When is a product defined? What is its order?',
  '<h4>Write the orders side by side</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>Rule 1</b>: <i>AB</i> is defined only if columns of <i>A</i> = rows of <i>B</i> (the inside numbers)</li><li><b>Rule 2</b>: <i>AB</i> has the rows of <i>A</i> and the columns of <i>B</i> (the outside numbers)</li>'
  '<li>order matters: <i>AB</i> can be defined when <i>BA</i> is not</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:22px;align-items:center;font-size:30px">'
  '<div class="frag">(2 × <b style="color:#c62828">3</b>)(<b style="color:#c62828">3</b> × 1) → inside equal → defined</div>'
  '<div class="frag">(<b style="color:#1565c0">2</b> × 3)(3 × <b style="color:#1565c0">1</b>) → order <b style="color:#1565c0">2 × 1</b></div>'
  '<div class="frag">(3 × <b>1</b>)(<b>2</b> × 2) → 1 ≠ 2 → <b>not defined</b></div></div>',
  'Write the orders under each matrix BEFORE you multiply anything.',f'{CAM}, 10D pp. 499–502 (own words) · {EDR}, 7C p. 439',
  cards=(kcard('Defined?',F('(<i>m</i> × <b><i>n</i></b>)(<b><i>n</i></b> × <i>s</i>)')),kcard('Order',F('<i>AB</i> is <i>m</i> × <i>s</i>')))))

# ================= Ex 17 / YT 7C WE1
A17=[[6,0],[-4,2]]; B17=[[3,1]]; C17=[[1],[-1]]
GIV17='<div style="font-size:28px;margin-top:30px">'+C(mat(A17,name='A',fs=28),mat(B17,name='B',fs=28),mat(C17,name='C',fs=28))
S.append(qslide('we','Worked example 17 · 10D','Is a matrix product defined?',
  GIV17+'Which of the following matrix products are defined?'+plist([('a','<i>AB</i>'),('b','<i>BC</i>'),('c','<i>AC</i>')])+'</div>',
  [('a','<i>AB</i>: (2 × <b>2</b>)(<b>1</b> × 2): 2 ≠ 1'),('b','<i>BC</i>: (1 × <b>2</b>)(<b>2</b> × 1): equal'),('c','<i>AC</i>: (2 × <b>2</b>)(<b>2</b> × 1): equal')],
  '',f'{CAM} · Example 17 (pp. 500–501)',video='Cambridge GO · Example 17 (10D Resources)',
  parts=[('a','<i>AB</i> is not defined.'),('b','<i>BC</i> is defined.'),('c','<i>AC</i> is defined.')]))
K1=[[3,-2],[0,5]]; L1=[[-1],[3]]
S.append(qslide('yt','You try · Edrolo 7C WE1','Is a matrix product defined?',
  '<div style="font-size:28px;margin-top:30px"><b>Determine</b> whether the following matrix products are defined. If defined, <b>determine</b> its order.'+C(mat(K1,name='K',fs=28),mat(L1,name='L',fs=28))
  +plist([('a','<i>KL</i>'),('b','<i>LK</i>')])+'</div>',
  [('Orders','<i>K</i> is 2 × 2, <i>L</i> is 2 × 1'),('a','<i>KL</i>: (2 × <b>2</b>)(<b>2</b> × 1): equal → order 2 × 1'),('b','<i>LK</i>: (2 × <b>1</b>)(<b>2</b> × 2): not equal')],
  '',f'{EDR} · 7C Worked example 1 (p. 440)',cmd=('Determine',None,'inside numbers, then outside numbers'),
  parts=[('a','<i>KL</i> is defined. The order of <i>KL</i> is 2 × 1.'),('b','<i>LK</i> is not defined.')]))
# ================= Ex 18 / YT U1&2 5C WE1
S.append(qslide('we','Worked example 18 · 10D','Determining the order of a matrix product',
  GIV17+'The following matrix products are defined. What is their order?'+plist([('a','<i>BA</i>'),('b','<i>BC</i>'),('c','<i>AC</i>')])+'</div>',
  [('a','<i>BA</i>: (<b>1</b> × 2)(2 × <b>2</b>)'),('b','<i>BC</i>: (<b>1</b> × 2)(2 × <b>1</b>)'),('c','<i>AC</i>: (<b>2</b> × 2)(2 × <b>1</b>)')],
  '',f'{CAM} · Example 18 (p. 502)',video='Cambridge GO · Example 18 (10D Resources)',
  parts=[('a','order of <i>BA</i> is 1 × 2'),('b','order of <i>BC</i> is 1 × 1'),('c','order of <i>AC</i> is 2 × 1')]))
P5=[[3,-12],[9,4],[-7,6]]; Q5=[[2,3,-11],[4,0,-5],[3,-2,7],[2,-5,0],[1,1,6]]
S.append(qslide('yt','You try · Edrolo U1&amp;2 5C WE1','Determining the order of a matrix product',
  '<div style="font-size:22px;margin-top:10px"><b>Determine</b> whether the following matrix products are defined. If defined, <b>determine</b> its order.'+C(mat(P5,name='P',fs=22),mat(Q5,name='Q',fs=22))
  +plist([('a','<i>PQ</i>'),('b','<i>QP</i>')])+'</div>',
  [('Orders','<i>P</i> is 3 × 2, <i>Q</i> is 5 × 3'),('a','<i>PQ</i>: (3 × <b>2</b>)(<b>5</b> × 3): not equal'),('b','<i>QP</i>: (<b>5</b> × 3)(3 × <b>2</b>): equal → 5 × 2')],
  '',f'{EDR12} · 5C Worked example 1 (p. 270)',cmd=('Determine',None,'inside numbers, then outside numbers'),
  parts=[('a','<i>PQ</i> is not defined.'),('b','<i>QP</i> is defined. The order of <i>QP</i> is 5 × 2.')]))

# ================= Learn 2: row x column
S.append(learn('Learn · 10D','Multiplying: row × column',
  '<h4>Multiply matching elements, then add</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>row matrix × column matrix: multiply 1st × 1st, 2nd × 2nd, … and add → ONE number</li>'
  '<li>for a bigger product, each element <i>c<sub>ij</sub></i> = row <i>i</i> of <i>A</i> × column <i>j</i> of <i>B</i></li>'
  '<li>a football score works the same way: goals × 6 + behinds × 1</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ(mat([[11,5]],fs=26),mat([[6],[1]],fs=26),'= [11 × 6 + 5 × 1] = [71]')+'</div>'
  '<div class="frag">'+EQ(mat([['a','b'],['c','d']],fs=26),mat([['e'],['g']],fs=26),'=',mat([['a × e + b × g'],['c × e + d × g']],fs=26))+'</div></div>',
  'Run your left finger along the row and your right finger down the column.',f'{CAM}, 10D pp. 499–504 (own words; football example from the book) · {EDR}, 7C p. 440',
  cards=(kcard('Element',F('<i>c<sub>ij</sub></i> = row <i>i</i> · column <i>j</i>')),kcard('Order',F('<i>AB</i> is <i>m</i> × <i>s</i>')))))
# ================= Ex 19 / YT-10D-19
S.append(qslide('we','Worked example 19 · 10D','Multiplying a row matrix by a column matrix (by hand)',
  '<div style="font-size:30px;margin-top:40px">Evaluate the matrix product <i>AB</i>, where '+EQ('<i>A</i> =',mat([[1,3,2]],fs=30,tid='e19'))+' and '+EQ('<i>B</i> =',mat([[2],[4],[1]],fs=30,tid='e19b'))+'.</div>',
  [('Defined?','(1 × <b>3</b>)(<b>3</b> × 1): defined, order 1 × 1'),('Multiply','1 × 2 + 3 × 4 + 2 × 1','data-hi="#e19|c0_0,c0_1,c0_2|hy;#e19b|c0_0,c1_0,c2_0|hy"'),('Add','2 + 12 + 2 = 16')],
  '∴ <i>AB</i> = [16]',f'{CAM} · Example 19 (p. 503)',video='Cambridge GO · Example 19 (10D Resources)',cmd=('Evaluate',None,'multiply, then add')))
S.append(qslide('yt','You try · written for 12MAG','Multiplying a row matrix by a column matrix (by hand)',
  '<div style="font-size:30px;margin-top:40px">Evaluate the matrix product <i>AB</i>, where '+EQ('<i>A</i> =',mat([[2,1,3]],fs=30,tid='y19'))+' and '+EQ('<i>B</i> =',mat([[5],[2],[4]],fs=30,tid='y19b'))+'.</div>',
  [('Defined?','(1 × <b>3</b>)(<b>3</b> × 1): defined, order 1 × 1'),('Multiply','2 × 5 + 1 × 2 + 3 × 4','data-hi="#y19|c0_0,c0_1,c0_2|hy;#y19b|c0_0,c1_0,c2_0|hy"'),('Add','10 + 2 + 12 = 24')],
  '∴ <i>AB</i> = [24]','Written for 12MAG (modelled on Cambridge Example 19; no Edrolo match) · planner/written-youtrys.json YT-10D-19',cmd=('Evaluate',None,'multiply, then add')))
# ================= Ex 20 / YT 7C WE2
S.append(qslide('we','Worked example 20 · 10D','Multiplying a rectangular matrix by a column matrix (by hand)',
  '<div style="font-size:30px;margin-top:40px">Evaluate the matrix product <i>AB</i>, where '+EQ('<i>A</i> =',mat([[1,0],[2,3]],fs=30,tid='e20'))+' and '+EQ('<i>B</i> =',mat([[2],[3]],fs=30,tid='e20b'))+'.</div>',
  [('Defined?','(2 × <b>2</b>)(<b>2</b> × 1): defined, order 2 × 1'),('Row 1','1 × 2 + 0 × 3 = 2','data-hi="#e20|c0_0,c0_1|hy;#e20b|c0_0,c1_0|hy"'),('Row 2','2 × 2 + 3 × 3 = 13','data-hi="#e20|c1_0,c1_1|hb;#e20b|c0_0,c1_0|hb"')],
  '∴ <i>AB</i> = '+mat([[2],[13]],fs=22),f'{CAM} · Example 20 (pp. 503–504)',video='Cambridge GO · Example 20 (10D Resources)',cmd=('Evaluate',None,'each row × the column')))
S.append(qslide('yt','You try · Edrolo 7C WE2','Evaluating a matrix product',
  '<div style="font-size:30px;margin-top:40px">Consider the following matrices.'+C(mat([[-1,3],[0,5]],name='P',fs=30,tid='y20'),mat([[2],[4]],name='Q',fs=30,tid='y20b'))+'Evaluate the matrix product <i>PQ</i>.</div>',
  [('Defined?','(2 × <b>2</b>)(<b>2</b> × 1): defined, order 2 × 1'),('Row 1','−1 × 2 + 3 × 4 = 10','data-hi="#y20|c0_0,c0_1|hy"'),('Row 2','0 × 2 + 5 × 4 = 20','data-hi="#y20|c1_0,c1_1|hb"')],
  '<i>PQ</i> = '+mat([[10],[20]],fs=22),f'{EDR} · 7C Worked example 2, Method 1 (p. 441)',cmd=('Evaluate',None,'each row × the column')))

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-operations']
S.append(cas('CAS · 10D','Multiplying two matrices',
  '<div style="font-size:24px">If</div>'+C(mat([[11,5],[10,9]],name='C',fs=26),mat([[6],[1]],name='D',fs=26))+'<div style="font-size:24px">find the matrix <i>CD</i>.</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'],CS['classpad'],'<i>CD</i> = '+mat([[71],[69]],fs=16)+' (the football scores!)',
  f'{CAM} · 10D CAS 3 (pp. 504–505) · Steps: CAS guide (planner)'))

# ================= Learn 3: summing matrices
S.append(learn('Learn · 10D','Summing matrices',
  '<h4>A matrix of 1s adds things up</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>summing matrix</b>: a row or column matrix whose elements are all 1</li>'
  '<li>sum the <b>rows</b>: <i>post</i>-multiply (on the right) by a COLUMN of 1s (<i>n</i> × 1)</li>'
  '<li>sum the <b>columns</b>: <i>pre</i>-multiply (on the left) by a ROW of 1s (1 × <i>m</i>)</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">rows: '+EQ(mat([[1,4,2],[-2,3,0]],fs=24),mat([[1],[1],[1]],fs=24),'=',mat([[7],[1]],fs=24))+'</div>'
  '<div class="frag">columns: '+EQ(mat([[1,1]],fs=24),mat([[1,4,2],[-2,3,0]],fs=24),'=',mat([[-1,7,2]],fs=24))+'</div></div>',
  'The summing matrix must make the product DEFINED: count the columns (rows) first.',f'{CAM}, 10D p. 505 (own words) · {EDR12}, 5D p. 279 (example)',
  cards=(kcard('Row sums',F('<i>A</i> × column of 1s')),kcard('Column sums',F('row of 1s × <i>A</i>')))))
# ================= Ex 21 / YT 7C WE3
M21=[[1,3,0],[2,6,7],[3,0,1]]; N21=[[2,5,-1,-3,4],[0,6,2,-2,3]]
S.append(qslide('we','Worked example 21 · 10D','Using matrix multiplication to sum the rows and columns of a matrix',
  '<div style="font-size:24px">Use matrix multiplication to generate a matrix that:'
  +plist([('a i','displays row sums of the matrix '+mat(M21,fs=22)),('a ii','displays column sums of the matrix '+mat(M21,fs=22)),('b','displays the column sums of the matrix '+mat(N21,fs=22)+'.')])+'</div>',
  [('a i','rows of a 3 × 3: post-multiply by a 3 × 1 summing matrix'),('a ii','columns of a 3 × 3: pre-multiply by a 1 × 3 summing matrix'),('b','columns of a 2 × 5: pre-multiply by a 1 × 2 summing matrix')],
  '',f'{CAM} · Example 21 (pp. 505–506)',video='Cambridge GO · Example 21 (10D Resources)',
  parts=[('a i',mat(M21,fs=17)+mat([[1],[1],[1]],fs=17)+' = '+mat([[4],[15],[4]],fs=17)),('a ii',mat([[1,1,1]],fs=17)+mat(M21,fs=17)+' = '+mat([[6,9,8]],fs=17)),
         ('b',mat([[1,1]],fs=17)+mat(N21,fs=17)+' = '+mat([[2,11,1,-5,7]],fs=17))]))
sm()
S7=[[-1,0,6],[2,-3,4]]
S.append(qslide('yt','You try · Edrolo 7C WE3','Summing matrices',
  '<div style="font-size:28px;margin-top:30px">'+C(mat(S7,name='S',fs=30))+'Use an appropriate summing matrix to'+plist([('a','sum the rows of matrix <i>S</i>.'),('b','sum the columns of matrix <i>S</i>.')])+'</div>',
  [('a','<i>S</i> has 3 columns: post-multiply by a 3 × 1 summing matrix'),('b','<i>S</i> has 2 rows: pre-multiply by a 1 × 2 summing matrix')],
  '',f'{EDR} · 7C Worked example 3 (p. 443)',
  parts=[('a',mat(S7,fs=18)+mat([[1],[1],[1]],fs=18)+' = '+mat([[5],[3]],fs=18)),('b',mat([[1,1]],fs=18)+mat(S7,fs=18)+' = '+mat([[1,-3,10]],fs=18))]))
# ================= Ex 22 / YT U1&2 5D WE1
S.append(qslide('we','Worked example 22 · 10D','A practical application of matrix multiplication',
  '<div style="font-size:24px;margin-top:20px">'+C(mat([[25],[40]],name='E',rl=['<i>Walk</i>','<i>Run</i>'],side=True,fs=26,tid='e22'),'<span style="font-size:20px;max-width:420px">Matrix <i>E</i> gives the energy in kilojoules consumed per minute when walking and running.</span>')
  +C(mat([[20,40]],name='T',cl=['<i>Walk</i>','<i>Run</i>'],fs=26,tid='e22b'),'<span style="font-size:20px;max-width:420px">Matrix <i>T</i> gives the times (in minutes) a person spent walking and running in a training session.</span>')
  +'<b>Compute</b> the matrix product <i>TE</i> and <b>show</b> that it gives the total energy consumed during the training session.</div>',
  [('Product','<i>T</i> × <i>E</i> = [20 × 25 + 40 × 40] = [2100]','data-hi="#e22b|c0_0,c0_1|hy;#e22|c0_0,c1_0|hy"'),('Meaning','20 minutes × 25 kJ/minute + 40 minutes × 40 kJ/minute = 2100 kJ')],
  '<i>TE</i> = [2100]: the total energy consumed is 2100 kJ, the value given by the matrix product <i>TE</i>.',f'{CAM} · Example 22 (p. 506)',video='Cambridge GO · Example 22 (10D Resources)',cmd=('Compute',None,'multiply, then say what it means')))
F5=[[10,19,13],[11,9,16]]
S.append(qslide('yt','You try · Edrolo U1&amp;2 5D WE1','Using matrix products in financial applications',
  '<div style="font-size:22px;margin-top:10px">Jaiden (J) and Nick (N) both sell the same types of fish. They both sell trout (T) for $40, cod (C) for $30 and mackerel (M) for $20. The number of each fish sold by Jaiden and Nick can be found in matrix <i>F</i>.'
  +C(mat(F5,name='F',cl=['T','C','M'],rl=['J','N'],side=True,fs=24))
  +plist([('a','<b>Construct</b> <i>P</i>, a matrix which contains the prices of each type of fish, as a column matrix.'),('b','Using a matrix product, <b>calculate</b> the revenue made from Jaiden and Nick.')])+'</div>',
  [('a','three types of fish → 3 × 1, in the order T, C, M'),('b','<i>F</i> × <i>P</i>: (2 × <b>3</b>)(<b>3</b> × 1) → 2 × 1'),('Jaiden','10 × 40 + 19 × 30 + 13 × 20 = 1230'),('Nick','11 × 40 + 9 × 30 + 16 × 20 = 1030')],
  '',f'{EDR12} · 5D Worked example 1 (pp. 278–279)',cmd=('calculate',None,'post-multiply by the prices'),
  parts=[('a','<i>P</i> = '+mat([[40],[30],[20]],rl=['T','C','M'],side=True,fs=17)),('b','<i>F</i> × <i>P</i> = '+mat([[1230],[1030]],rl=['J','N'],side=True,fs=17)+': Jaiden generated $1230 of revenue whereas Nick generated $1030 of revenue.')]))

# ================= Learn 4: powers
S.append(learn('Learn · 10D','Powers of a matrix',
  '<h4>A<sup>2</sup> = A × A</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><i>A</i><sup>2</sup> = <i>A</i> × <i>A</i>, <i>A</i><sup>3</sup> = <i>A</i> × <i>A</i> × <i>A</i>, …</li>'
  '<li>only <b>square</b> matrices have powers (the product must be defined)</li>'
  '<li><i>A</i><sup>2</sup> is NOT squaring each element</li><li>keep the order of operations: (<i>AB</i>)<sup>2</sup> = (<i>AB</i>)(<i>AB</i>)</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:20px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ(mat([[2,1],[8,9]],fs=24,sup='2'),'=',mat([[2,1],[8,9]],fs=24),mat([[2,1],[8,9]],fs=24),'=',mat([[12,11],[88,89]],fs=24))+'</div>'
  '<div class="frag">'+EQ(mat([[2,1],[8,9]],fs=24,sup='2'),'≠',mat([[4,1],[64,81]],fs=24),' ✗')+'</div>'
  '<div class="frag">CAS: type <b>a·b^2</b> (with the ×), not ab^2</div></div>',
  'On CAS put a × between letters: ab is read as one variable.',f'{CAM}, 10D pp. 506–508 (own words) · {EDR}, 7C pp. 443–444 (example)',
  cards=(kcard('Power',F('<i>A</i><sup>2</sup> = <i>A</i> × <i>A</i>')),kcard('Square only',F('<i>n</i> × <i>n</i>')))))
# ================= Ex 23 / YT 7C WE4
A23=[[1,0],[2,-1]]; B23=[[-1,1],[2,1]]; C23=[[0,1],[1,1]]
S.append(qslide('we','Worked example 23 · 10D','Evaluating matrix expressions involving powers',
  '<div style="font-size:28px;margin-top:30px">If '+EQ('<i>A</i> =',mat(A23,fs=28))+', '+EQ('<i>B</i> =',mat(B23,fs=28))+' and '+EQ('<i>C</i> =',mat(C23,fs=28))+', <b>determine</b>:'
  +plist([('a','2<i>A</i> + <i>B</i><sup>2</sup> − 2<i>C</i>'),('b','(2<i>A</i> − <i>B</i>)<sup>2</sup> − <i>C</i><sup>2</sup>'),('c','<i>AB</i><sup>2</sup> − 3<i>C</i><sup>2</sup>')])+'</div>',
  [('Store','enter <i>A</i>, <i>B</i> and <i>C</i> into the CAS as a, b, c'),('Type','2·a+b^2−2·c · (2·a−b)^2−c^2 · a·b^2−3·c^2')],
  '',f'{CAM} · Example 23 (pp. 507–508; solution b printed as (2A + B)²: the question’s (2A − B)² is evaluated)',video='Cambridge GO · Example 23 (10D Resources)',cmd=('determine',None,'store the matrices on CAS'),
  parts=[('a',mat([[5,-2],[2,-1]],fs=18)),('b',mat([[6,-1],[-1,5]],fs=18)),('c',mat([[0,-3],[3,-9]],fs=18))]))
S.append(qslide('yt','You try · Edrolo 7C WE4','Calculating a matrix power',
  '<div style="font-size:28px;margin-top:30px">Consider the following matrices.'+C(mat([[1],[2],[3]],name='A',fs=28),mat([[2,1],[8,9]],name='B',fs=28,tid='y23'),mat([[2,3,5]],name='C',fs=28))
  +plist([('a','<b>Calculate</b> <i>B</i><sup>2</sup>.'),('b','<b>Determine</b> whether (<i>AC</i>)<sup>2</sup> is defined.')])+'</div>',
  [('a','<i>B</i> is 2 × 2 (square): '+mat([['2 × 2 + 1 × 8','2 × 1 + 1 × 9'],['8 × 2 + 9 × 8','8 × 1 + 9 × 9']],fs=17)),('b','<i>AC</i>: (3 × <b>1</b>)(<b>1</b> × 3) → defined, order 3 × 3: square')],
  '',f'{EDR} · 7C Worked example 4 (p. 444)',cmd=('Calculate',None,'square matrices only'),
  parts=[('a','<i>B</i><sup>2</sup> = '+mat([[12,11],[88,89]],fs=18)),('b','(<i>AC</i>)<sup>2</sup> is defined.')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2017 Exam 2 Q1a','Show what you know',
  '<div style="font-size:26px;margin-top:30px">A school canteen sells pies (<i>P</i>), rolls (<i>R</i>) and sandwiches (<i>S</i>).<br>The number of each item sold over three school weeks is shown in matrix <i>M</i>.'
  +C(mat([[35,24,60],[28,32,43],[32,30,56]],name='M',cl=['P','R','S'],rl=['week 1','week 2','week 3'],side=True,fs=26,tid='x1'))
  +'a. In total, how many sandwiches were sold in these three weeks? <span class="muted">(1 mark)</span></div>',
  [('Sandwiches','column <i>S</i>','data-hi="#x1|c0_2,c1_2,c2_2|hy"'),('Add','60 + 43 + 56 (or [1 1 1] × <i>M</i> sums every column)')],
  '<b>159</b> sandwiches','VCAA 2017 Further Mathematics Exam 2 Matrices Q1 stem and Q1a (89% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7C Q17',
  stat=('mark',89)))
X2=[mat([[144]],fs=18),mat([[16],[24],[0]],fs=18),EQ('4 ×',mat([[1,2,0]],fs=18),'×',mat([[1],[12],[8]],fs=18)),EQ('2 ×',mat([[2,1,0]],fs=18),'×',mat([[2],[6],[4]],fs=18)),EQ('4 ×',mat([[2,1,0]],fs=18),'×',mat([[2],[6],[4]],fs=18))]
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2018 Exam 1 Q2','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The matrix product '+EQ(mat([[4,2,0]],fs=26),'×',mat([[4],[12],[8]],fs=26))+' is equal to</div>',
  [('Product','4 × 4 + 2 × 12 + 0 × 8 = 40, a 1 × 1 matrix: [40]'),('Options','A = 144 · D = 2 × (4 + 6 + 0) = 20 · E = 4 × (4 + 6 + 0) = 40')],
  EQ('4 ×',mat([[2,1,0]],fs=16),'×',mat([[2],[6],[4]],fs=16))+' = [40]: <b>E</b>.','VCAA 2018 Further Mathematics Exam 1 Matrices Q2 (68% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7C Q18',
  mc=X2,key='E',dis=('B','multiplying element by element is NOT a matrix product: multiply and ADD'),stat=('mc',68)))
sm()

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 10 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='10D' and v.get('url')]))
n=assemble(S,'12MAG · 10D · The product of two matrices',os.path.join(ROOT,'lessons','10D slides.html'))
print(n-1,'slides')
