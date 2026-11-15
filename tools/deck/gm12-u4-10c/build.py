"""Lesson gm12-u4-10c (10C Matrix arithmetic: addition, subtraction and scalar multiplication) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/10C slides.html      Run: python3 tools/deck/gm12-u4-10c/build.py      Screenshots: python3 tools/deck/gm12-u4-10c/shoot.py
Matrices drawn with tools/deck/mx.py.

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- Do Now: VCAA 2023 Exam 1 Q29 (E, 62%) · VCAA 2025 Exam 1 Q7-8 stem + Q8 (D, 79%) ·
          VCAA 2024 Exam 2 Q9 stem + Q9a (average 0.9/1 = 90%) · VCAA 2025 Exam 2 Q4 stem + Q4e (scatterplot cropped; average 1.5/2 = 75%).
- APK: Cambridge U1&2 Ch 4 skills checklist 4B #3 and 4C #6 (from tools/y11_cambridge_skills_checklist.csv; solutions worked for 12MAG) ·
       VCAA 2021 Further Exam 2 Matrices Q1 stem + Q1b in ORIGINAL wording (5%, k = 1.05; Edrolo U1&2 5B Q15 adapts it to 10%).
       2021 Exam 2 report: 48% scored 1 (the card's '50%' corrected).
- Learn: Cambridge U3&4 10C pp. 491-496 (own words) · Edrolo U3&4 7B pp. 429-431.
- Worked examples: Cambridge U3&4 Examples 11-16 (pp. 491-496).
  You trys: Edrolo U1&2 5B WE3 (p. 263), 5B WE2 (p. 262), Edrolo U3&4 7B WE1a-b (pp. 429-430), 7B WE2 (p. 431),
            YT-10C-15 and YT-10C-16 (written, planner/written-youtrys.json).
- CAS: planner/cas-skills.json 'matrix-operations'; task = Cambridge 10C CAS 2 (p. 494).
- Exit 1: VCAA 2019 Further Exam 1 Matrices Q1 (= Edrolo U3&4 7B Q13), C, 87%.
- Exit 2: VCAA 2016 Further Exam 1 Matrices Q1 (= Edrolo U3&4 7B Q14), C, 81%. (% as quoted by Edrolo from the examiner reports.)
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-10c')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def Mx(r,**k): return mat(r,**k)
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def grid(slide,cols=3,gap=4): return slide.replace('<div class="mc"',f'<div class="mc" style="display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px"',1)

S=['<style>.sm .L .q{font-size:17px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}</style>']
# ================= opening
t=title('10C','Matrix arithmetic: addition, subtraction and scalar multiplication',f'{CAM} · 10C Matrix arithmetic: addition, subtraction and scalar multiplication','10C')
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('Learn: equal matrices, adding and subtracting','',None),('Worked examples 11–13','→ You try',None),('Learn: scalar multiplication and the zero matrix','',None),
  ('Worked examples 14–15','→ You try',None),('CAS: matrix arithmetic','',None),('Worked example 16','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Equal matrices','same order AND every corresponding element equal'),
  ('Sum / difference','add or subtract corresponding elements; only defined for matrices of the same order'),
  ('Scalar multiplication','multiply every element by the number (the scalar)'),
  ('Zero matrix (O)','every element is 0',mat([[0,0],[0,0]],fs=15)),
  ('Not defined','different orders: you cannot add or subtract')],
  [('Sum',F('<i>A</i> + <i>B</i>: <i>a<sub>ij</sub></i> + <i>b<sub>ij</sub></i>'),'same order only'),
   ('Difference',F('<i>A</i> − <i>B</i>: <i>a<sub>ij</sub></i> − <i>b<sub>ij</sub></i>'),'same order only'),
   ('Scalar multiple',F('<i>kA</i>: <i>k</i> × <i>a<sub>ij</sub></i>'),'order does not change'),
   ('Zero matrix',F('<i>A</i> − <i>A</i> = <i>O</i>'),'and A + O = A')],
  f'{CAM}, 10C pp. 491–496; Study Design: elementary matrix operations (sum, difference, multiplication of a scalar)'))

# ================= Do Now 1: VCAA 2023 E1 Q29 (10A)
def M3(r): return mat(r,fs=20)
S.append(grid(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q29','Review of 10A (last lesson)',
  '<div style="font-size:24px;margin-top:20px">Matrix <i>K</i> is a 3 × 2 matrix.<br>The elements of <i>K</i> are determined by the rule <i>k<sub>ij</sub></i> = (<i>i</i> − <i>j</i>)<sup>2</sup>.<br>Matrix <i>K</i> is</div>',
  [('Order','3 × 2: three rows, two columns'),('Row 1','(1 − 1)<sup>2</sup> = 0 · (1 − 2)<sup>2</sup> = 1'),('Row 2','(2 − 1)<sup>2</sup> = 1 · (2 − 2)<sup>2</sup> = 0'),('Row 3','(3 − 1)<sup>2</sup> = 4 · (3 − 2)<sup>2</sup> = 1')],
  mat([[0,1],[1,0],[4,1]],fs=18)+' : <b>E</b>.','VCAA 2023 General Mathematics Exam 1 Q29 (examiner report: 62% correct)',
  mc=[M3([[0,1,-2],[1,0,-1]]),M3([[0,1,4],[1,0,1]]),M3([[0,-1],[1,0],[4,1]]),M3([[0,1],[1,0],[2,1]]),M3([[0,1],[1,0],[4,1]])],key='E',stat=('mc',62))))
# ================= Do Now 2: VCAA 2025 E1 Q8 (2I)
CAR='<table class="t tight" style="font-size:19px;margin:8px auto"><tr><th></th><th colspan="3"><i>Preferred car colour</i></th></tr><tr><th></th><th>Black</th><th>Silver</th><th>White</th></tr><tr><th>Female</th><td>28</td><td>42</td><td>35</td></tr><tr><th>Male</th><td>55</td><td>32</td><td>42</td></tr></table>'
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q8','Review of 2I (last term)',
  '<div style="font-size:21px">The data in the table below shows the <em class="v">preferred car colour</em> for a sample of female and male car buyers.'+CAR
  +'Which one of the following is the most appropriate way to graphically display the data shown in the table above?</div>',
  [('Variables','<i>sex</i> and <i>preferred car colour</i>: both categorical'),('Display','two categorical variables in a two-way table → segmented bar chart')],
  'a segmented bar chart: <b>D</b>.','VCAA 2025 General Mathematics Exam 1 Q7–8 stem and Q8 (examiner report: 79% correct)',
  mc=['a histogram','a back-to-back stem plot','parallel boxplots','a segmented bar chart'],key='D',stat=('mc',79)))
# ================= Do Now 3: VCAA 2024 E2 Q9a (10A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q9a','Review of 10A (last lesson)',
  '<div style="font-size:22px">Vince works on a construction site.<br>The amount Vince gets paid depends on the type of shift he works, as shown in the table below.'
  '<table class="t tight" id="d3t" style="font-size:20px;margin:10px auto"><tr><th>Shift type</th><th>Normal</th><th>Overtime</th><th>Weekend</th></tr><tr><th>Hourly rate of pay ($ per hour)</th><td>36</td><td>54</td><td>72</td></tr></table>'
  'This information is shown in matrix <i>R</i> below.'+C('<i>R</i> = '+mat([[36,54,72]],fs=22,tid='d3'))
  +'a. Matrix <i>R</i><sup><i>T</i></sup> is the transpose of matrix <i>R</i>.<br><b>Write down</b> matrix <i>R</i><sup><i>T</i></sup> in the space below. <span class="muted">(1 mark)</span></div>',
  [('Order','<i>R</i> is 1 × 3, so <i>R</i><sup><i>T</i></sup> is 3 × 1'),('Rows → columns','the row 36, 54, 72 becomes a column','data-hi="#d3|c0_0,c0_1,c0_2|hy"')],
  '<i>R</i><sup><i>T</i></sup> = '+mat([[36],[54],[72]],fs=20),'VCAA 2024 General Mathematics Exam 2 Q9 stem and Q9a (examiner report: average 0.9/1)',
  stat=('mark',90),cmd=('Write down',1,'rows become columns')))
# ================= Do Now 4: VCAA 2025 E2 Q4e (2E)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 Exam 2 Q4e','Review of 2E–2G (last term)',
  ('<div style="font-size:17px">The scatterplot below shows the <em class="v">sale price</em> of a home, in dollars, against the distance of the home from the city centre of Melbourne, in kilometres, <em class="v">distance from city centre</em>. The sample consists of three-bedroom homes sold between 2016 and 2018.</div>',
   '<div style="display:flex;align-items:center;gap:6px"><span style="font-size:14px;font-style:italic">sale price ($)</span>'+IMG('dn4_scatter.png',540)+'</div>',
   '<div style="font-size:17px">The equation of the least squares line for the data in the scatterplot is<br>&nbsp;&nbsp;<em class="v">sale price</em> = 1 765 353 – 35 054 × <em class="v">distance from city centre</em><br>The coefficient of determination is 0.0806<br>'
   'e. <b>Describe</b> the linear association between <em class="v">sale price</em> and <em class="v">distance from city centre</em> in terms of its strength and direction. Answer in the table below. <span class="muted">(2 marks)</span></div>'),
  [('Direction','slope −35 054 is negative → negative association'),fx('r','<i>r</i>',F('−√',V('r²','0.0806')),'−0.284'),('Strength','0.1 ≤ |<i>r</i>| &lt; 0.3 → weak')],
  '<table class="t tight" style="font-size:18px;margin:0"><tr><th>strength</th><td><b>weak</b></td></tr><tr><th>direction</th><td><b>negative</b></td></tr></table>',
  'VCAA 2025 General Mathematics Exam 2 Q4 stem and Q4e (examiner report: average 1.5/2)',stat=('avg',75),cmd=('Describe',2,'strength and direction')))

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4B #3','Adding matrices',
  '<div style="font-size:30px;margin-top:40px">Complete the following matrix addition.'+C(EQ(mat([[2,4],[5,1]],fs=32,tid='a1'),'+',mat([[9,8],[9,-1]],fs=32,tid='a1b')))+'</div>',
  [('Same order','both 2 × 2, so they can be added'),('Add','2 + 9 · 4 + 8 · 5 + 9 · 1 + (−1)','data-hi="#a1|c0_0|hy;#a1b|c0_0|hy"')],
  mat([[11,12],[14,0]],fs=24),f'{CAM12} · Ch 4 skills checklist 4B #3 · solution worked for 12MAG',cmd=('Complete',None,'add matching elements')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4C #6','Scalar multiplication with addition',
  '<div style="font-size:30px;margin-top:40px">If '+EQ('<i>A</i> =',mat([[5,3],[-2,0]],fs=30))+' and '+EQ('<i>B</i> =',mat([[2,-1],[0,1]],fs=30))+', then <b>find</b> 2<i>A</i> + 3<i>B</i>.</div>',
  [('2A','2<i>A</i> = '+mat([[10,6],[-4,0]],fs=18)),('3B','3<i>B</i> = '+mat([[6,-3],[0,3]],fs=18)),('Add','10 + 6 · 6 + (−3) · −4 + 0 · 0 + 3')],
  '2<i>A</i> + 3<i>B</i> = '+mat([[16,3],[-4,3]],fs=22),f'{CAM12} · Ch 4 skills checklist 4C #6 · solution worked for 12MAG',cmd=('find',None,'multiply first, then add')))
S.append(qslide('apk','APK · VCAA 2021 Exam 2 Q1b','Finding a scalar',
  '<div style="font-size:24px;margin-top:10px">Elena imports three brands of olive oil: Carmani (<i>C</i>), Linelli (<i>L</i>) and Ohana (<i>O</i>).<br>The number of 1 litre bottles of these oils sold in January 2021 is shown in matrix <i>J</i> below.'
  +C('<i>J</i> = '+mat([[2800],[1700],[2400]],fs=24,rl='CLO',side=True))
  +'b. Elena expected that in February 2021 the sales of all three brands of olive oil would increase by 5%.<br>She multiplied matrix <i>J</i> by a scalar value, <i>k</i>, to determine the expected volume of sales for February.<br><b>Write down</b> the value of the scalar <i>k</i>. <span class="muted">(1 mark)</span></div>',
  [('Increase','new sales = 100% + 5% = 105% of January'),('Scalar','105% = 1.05 (not 0.05: that is only the increase)')],
  '<i>k</i> = <b>1.05</b>','VCAA 2021 Further Mathematics Exam 2 Matrices Q1 stem and Q1b (examiner report: 48% scored 1) · Edrolo U1&amp;2 5B Q15 (adapted)',
  stat=('mark',48),cmd=('Write down',1,'the multiplier, not the increase')))

# ================= Learn 1: equal matrices, adding and subtracting
S.append(learn('Learn · 10C','Equal matrices, adding and subtracting',
  '<h4>Same order, match the positions</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>equal</b>: same order and every corresponding element equal</li><li>same numbers in different places are NOT equal</li>'
  '<li><b>add / subtract</b>: combine the elements in the same position</li><li>different orders → <b>not defined</b></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:16px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ(mat([[1,2],[3,4]],fs=26),'=',mat([[1,2],[3,4]],fs=26),' ✓ &nbsp;&nbsp;&nbsp; ',mat([[1,2],[3,4]],fs=26),'≠',mat([[4,3],[2,1]],fs=26),' ✗')+'</div>'
  '<div class="frag">'+EQ(mat([['a','b'],['c','d']],fs=26),'+',mat([['e','f'],['g','h']],fs=26),'=',mat([['a + e','b + f'],['c + g','d + h']],fs=26))+'</div>'
  '<div class="frag">'+EQ(mat([[1],[2]],fs=26),'+',mat([[1,2]],fs=26),': 2 × 1 and 1 × 2 → <b>not defined</b>')+'</div></div>',
  'Check the orders FIRST: if they are different, the answer is “not defined”.',f'{CAM}, 10C pp. 491–492 (own words; examples from the book) · {EDR}, 7B p. 429',
  cards=(kcard('Sum',F('<i>a<sub>ij</sub></i> + <i>b<sub>ij</sub></i>')),kcard('Difference',F('<i>a<sub>ij</sub></i> − <i>b<sub>ij</sub></i>')))))

# ================= Ex 11 / YT U1&2 5B WE3
S.append(qslide('we','Worked example 11 · 10C','Equality of two matrices',
  '<div style="font-size:28px;margin-top:30px">Given that'+C(EQ(mat([[2,'<i>a</i>'],[8,'<i>b</i> + 1']],fs=30,tid='e11'),'=',mat([[2,10],[20,7]],fs=30,tid='e11b')))+'find the value of <i>a</i> and the value of <i>b</i>.</div>',
  [('a','corresponding elements: <i>a</i> = 10','data-hi="#e11|c0_1|hy;#e11b|c0_1|hy"'),('b','<i>b</i> + 1 = 7, so <i>b</i> = 6','data-hi="#e11|c1_1|hb;#e11b|c1_1|hb"')],
  '<i>a</i> = <b>10</b> and <i>b</i> = <b>6</b>',f'{CAM} · Example 11 (p. 491)',video='Cambridge GO · Example 11 (10C Resources)',cmd=('find',None,'match the positions')))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5B WE3','Equality of two matrices',
  '<div style="font-size:28px;margin-top:30px">Consider the following matrix equation.'+C(EQ(mat([[1,'<i>a</i>'],[-3,7]],fs=30,tid='y11'),'+',mat([[6,3],[5,8]],fs=30,tid='y11b'),'=',mat([[7,1],[2,15]],fs=30,tid='y11c')))+'What is the value of <i>a</i>?</div>',
  [('Position','<i>a</i> is in the first row and second column','data-hi="#y11|c0_1|hy"'),('Match','same position in the second and final matrices: 3 and 1','data-hi="#y11b|c0_1|hy;#y11c|c0_1|hy"'),('Solve','<i>a</i> + 3 = 1, so <i>a</i> = 1 − 3')],
  '<i>a</i> = <b>−2</b>',f'{EDR12} · 5B Worked example 3 (p. 263)'))
# ================= Ex 12 / YT U1&2 5B WE2
A12=[[2,3,0],[1,4,2]]; B12=[[1,2,3],[2,-2,1]]
S.append(qslide('we','Worked example 12 · 10C','Adding two matrices',
  '<div style="font-size:28px;margin-top:30px">'+C(mat(A12,name='A',fs=30),mat(B12,name='B',fs=30))+'<b>Find</b> <i>A</i> + <i>B</i>.</div>',
  [('Order','both 2 × 3, so they can be added'),('Add','add corresponding elements: '+mat([['2 + 1','3 + 2','0 + 3'],['1 + 2','4 + (−2)','2 + 1']],fs=20))],
  '<i>A</i> + <i>B</i> = '+mat([[3,5,3],[3,2,3]],fs=22),f'{CAM} · Example 12 (p. 492)',video='Cambridge GO · Example 12 (10C Resources)',cmd=('Find',None,'same order? then add')))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5B WE2','Adding two matrices',
  '<div style="font-size:28px;margin-top:30px">If '+EQ('<i>A</i> =',mat([[2,0],[0,4],[6,7]],fs=30))+' and '+EQ('<i>B</i> =',mat([[8,3],[2,9],[4,2]],fs=30))+', <b>find</b> <i>A</i> + <i>B</i>.</div>',
  [('Write','write the calculation (both 3 × 2)'),('Add','add the elements in the same position: '+mat([['2 + 8','0 + 3'],['0 + 2','4 + 9'],['6 + 4','7 + 2']],fs=20))],
  mat([[10,3],[2,13],[10,9]],fs=22),f'{EDR12} · 5B Worked example 2 (p. 262)',cmd=('find',None,'same order? then add')))
# ================= Ex 13 / YT 7B WE1
S.append(qslide('we','Worked example 13 · 10C','Subtracting two matrices',
  '<div style="font-size:28px;margin-top:30px">'+C(mat(A12,name='A',fs=30),mat(B12,name='B',fs=30))+'<b>Find</b> <i>A</i> − <i>B</i>.</div>',
  [('Order','both 2 × 3, so they can be subtracted'),('Subtract','subtract corresponding elements: '+mat([['2 − 1','3 − 2','0 − 3'],['1 − 2','4 − (−2)','2 − 1']],fs=20))],
  '<i>A</i> − <i>B</i> = '+mat([[1,1,-3],[-1,6,1]],fs=22),f'{CAM} · Example 13 (p. 492)',video='Cambridge GO · Example 13 (10C Resources)',cmd=('Find',None,'same order? then subtract')))
S.append(qslide('yt','You try · Edrolo 7B WE1','Adding and subtracting matrices',
  '<div style="font-size:26px;margin-top:20px">Consider the matrices '+EQ('<i>A</i> =',mat([[2,2],[1,4],[5,3]],fs=28))+' and '+EQ('<i>B</i> =',mat([[4,1],[0,2],[4,5]],fs=28))+'.'
  +plist([('a','Is <i>A</i> + <i>B</i> defined?'),('b','If possible, calculate <i>A</i> − <i>B</i>.')])+'</div>',
  [('a','<i>A</i> has three rows and two columns: 3 × 2. <i>B</i> is also 3 × 2: the same order'),('b','subtract each element of <i>B</i> from its corresponding element of <i>A</i>: '+mat([['2 − 4','2 − 1'],['1 − 0','4 − 2'],['5 − 4','3 − 5']],fs=20))],
  '',f'{EDR} · 7B Worked example 1a–b (pp. 429–430)',cmd=('calculate',None,'check the orders first'),
  parts=[('a','Yes: the matrix sum is defined.'),('b','<i>A</i> − <i>B</i> = '+mat([[-2,1],[1,2],[1,-2]],fs=20))]))

# ================= Learn 2: scalar multiplication and the zero matrix
S.append(learn('Learn · 10C','Scalar multiplication and the zero matrix',
  '<h4>Multiply every element</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>scalar multiplication</b> <i>kA</i>: multiply EVERY element by <i>k</i></li><li>2<i>A</i> doubles every element; 0.5<i>A</i> halves them</li>'
  '<li>a % increase: multiply by 1 + rate (e.g. 1.5 for +50%)</li><li><b>zero matrix</b> <i>O</i>: all elements 0 (any order)</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:16px;align-items:center;font-size:26px">'
  '<div class="frag">'+EQ('3',mat([['a','b'],['c','d']],fs=26),'=',mat([['3a','3b'],['3c','3d']],fs=26))+'</div>'
  '<div class="frag">'+EQ(mat([[1,2],[3,4]],fs=26),'−',mat([[1,2],[3,4]],fs=26),'=',mat([[0,0],[0,0]],fs=26),'= <i>O</i>')+'</div>'
  '<div class="frag">'+EQ('<i>O</i> = [0],',mat([[0,0],[0,0]],fs=24),',',mat([[0],[0],[0]],fs=24),',',mat([[0,0],[0,0],[0,0]],fs=24))+'</div></div>',
  'Multiply the WHOLE matrix: every element, not just the first row.',f'{CAM}, 10C pp. 492–493 (own words; examples from the book) · {EDR}, 7B p. 431',
  cards=(kcard('Scalar multiple',F('<i>k</i> × <i>a<sub>ij</sub></i>')),kcard('Zero matrix',F('<i>A</i> − <i>A</i> = <i>O</i>')))))
# ================= Ex 14 / YT 7B WE2
C14=[[4,-4],[-2,6]]
S.append(qslide('we','Worked example 14 · 10C','Scalar multiplication',
  '<div style="font-size:28px;margin-top:30px">'+C(mat(A12,name='A',fs=30),mat(C14,name='C',fs=30))+'<b>Find</b> 3<i>A</i> and 0.5<i>C</i>.</div>',
  [('3A','multiply each element of <i>A</i> by 3'),('0.5C','multiply each element of <i>C</i> by 0.5')],
  '',f'{CAM} · Example 14 (p. 493)',video='Cambridge GO · Example 14 (10C Resources)',cmd=('Find',None,'multiply every element'),
  parts=[('3A','3'+mat(A12,fs=18)+' = '+mat([[6,9,0],[3,12,6]],fs=18)),('0.5C','0.5'+mat(C14,fs=18)+' = '+mat([[2,-2],[-1,3]],fs=18))]))
C2=[[2,1,3],[4,5,2],[1,0,4]]
S.append(qslide('yt','You try · Edrolo 7B WE2','Scalar multiplication',
  '<div style="font-size:30px;margin-top:40px">Given that '+EQ('<i>C</i> =',mat(C2,fs=30))+', <b>calculate</b> 3<i>C</i>.</div>',
  [('Multiply','multiply each individual element by 3: '+mat([['3 × 2','3 × 1','3 × 3'],['3 × 4','3 × 5','3 × 2'],['3 × 1','3 × 0','3 × 4']],fs=20))],
  mat([[6,3,9],[12,15,6],[3,0,12]],fs=22),f'{EDR} · 7B Worked example 2 (p. 431)',cmd=('calculate',None,'multiply every element')))
# ================= Ex 15 / YT-10C-15
S.append(qslide('we','Worked example 15 · 10C','The zero matrix',
  '<div style="font-size:30px;margin-top:40px">'+C(mat([[6,0],[-4,2]],name='G',fs=30),mat([[9,0],[-6,3]],name='H',fs=30))+'<b>Show</b> that 3<i>G</i> − 2<i>H</i> = <i>O</i>.</div>',
  [('Multiply','3<i>G</i> − 2<i>H</i> = '+mat([[18,0],[-12,6]],fs=20)+' − '+mat([[18,0],[-12,6]],fs=20)),('Subtract',mat([['18 − 18','0 − 0'],['−12 − (−12)','6 − 6']],fs=20)+' = '+mat([[0,0],[0,0]],fs=20))],
  '∴ 3<i>G</i> − 2<i>H</i> = <i>O</i>',f'{CAM} · Example 15 (p. 493)',video='Cambridge GO · Example 15 (10C Resources)',cmd=('Show',None,'every element ends up 0')))
YT=json.load(open(os.path.join(ROOT,'planner','written-youtrys.json'))); YT=YT if isinstance(YT,list) else YT.get('items',list(YT.values()))
YT={y['id']:y for y in YT}
S.append(qslide('yt','You try · written for 12MAG','The zero matrix',
  '<div style="font-size:30px;margin-top:40px">'+C(mat([[4,0],[-2,6]],name='G',fs=30),mat([[6,0],[-3,9]],name='H',fs=30))+'<b>Show</b> that 3<i>G</i> − 2<i>H</i> = <i>O</i>.</div>',
  [('Multiply','3<i>G</i> − 2<i>H</i> = '+mat([[12,0],[-6,18]],fs=20)+' − '+mat([[12,0],[-6,18]],fs=20)),('Subtract',mat([['12 − 12','0 − 0'],['−6 − (−6)','18 − 18']],fs=20)+' = '+mat([[0,0],[0,0]],fs=20))],
  '∴ 3<i>G</i> − 2<i>H</i> = <i>O</i>','Written for 12MAG (modelled on Cambridge Example 15; no Edrolo match) · planner/written-youtrys.json YT-10C-15',cmd=('Show',None,'every element ends up 0')))

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-operations']
AC=[[2,3,0],[1,4,2]]; BC=[[1,0,3],[2,-2,1]]
S.append(cas('CAS · 10C','Adding, subtracting and scalar multiplying',
  '<div style="font-size:22px">If</div>'+C(mat(AC,name='A',fs=24),mat(BC,name='B',fs=24))+'<div style="font-size:22px">find:</div>'
  '<p style="font-size:22px">a &nbsp;<i>A</i> + <i>B</i> &nbsp;&nbsp;&nbsp; b &nbsp;<i>A</i> − <i>B</i> &nbsp;&nbsp;&nbsp; c &nbsp;3<i>A</i> − 2<i>B</i></p><p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'],CS['classpad'],'a '+mat([[3,3,3],[3,2,3]],fs=15)+' &nbsp; b '+mat([[1,3,-3],[-1,6,1]],fs=15)+' &nbsp; c '+mat([[4,9,-6],[-1,16,4]],fs=15),
  f'{CAM} · 10C CAS 2 (pp. 494–495) · Steps: CAS guide (planner)'))

# ================= Ex 16 / YT-10C-16
def sales(names,a,b,ya,yb,tid,fs=18):
    t=(f'<table class="t tight" id="{tid}" style="font-size:{fs}px;margin:6px auto"><tr><th></th><th colspan="3">{ya}</th><th colspan="3">{yb}</th></tr>'
       f'<tr><th><i>{names[0]}</i></th>'+''.join(f'<th><i>{s}</i></th>' for s in names[1])*2+'</tr>')
    for r,(n,ra,rb) in enumerate(zip(names[2],a,b)): t+=f'<tr><th>{n}</th>'+''.join(f'<td data-i="c{r}_{k}">{v}</td>' for k,v in enumerate(ra+rb))+'</tr>'
    return t+'</table>'
A16=[[24,32,11],[32,34,9]]; B16=[[26,38,16],[35,41,12]]
S.append(qslide('we','Worked example 16 · 10C','Processing data using addition, subtraction and scalar multiplication',
  '<div style="font-size:18px">The sales data for two used car dealers, Honest Joe’s and Super Deals, are displayed below.'
  +sales(('Car sales',('Small','Medium','Large'),('Honest Joe’s','Super Deals')),A16,B16,'2014','2015','e16')
  +plist([('a','<b>Construct</b> two matrices, <i>A</i> and <i>B</i>, to represent the sales data for 2014 and 2015 separately.'),('b','<b>Construct</b> a new matrix <i>C</i> = <i>A</i> + <i>B</i>. What does this matrix represent?'),
          ('c','<b>Construct</b> a new matrix, <i>D</i> = <i>B</i> − <i>A</i>. What does this matrix represent?'),('d','Both dealers want to increase their 2015 sales by 50% by 2016. <b>Construct</b> a new matrix <i>E</i> = 1.5<i>B</i>. <b>Explain</b> why this matrix represents the planned sales figures for 2016.')])+'</div>',
  [('a','2014 columns → <i>A</i>, 2015 columns → <i>B</i>','data-hi="#e16|'+cells(0,2,0,3)+'|hy"'),('b','add corresponding elements','data-hi="#e16|'+cells(0,2,0,6)+'|hb"'),('c','subtract corresponding elements'),('d','1.5 × each element of <i>B</i>')],
  '',f'{CAM} · Example 16 (pp. 495–496)',video='Cambridge GO · Example 16 (10C Resources)',cmd=('Construct',None,'one matrix per year'),
  parts=[('a','<i>A</i> = '+mat(A16,fs=17)+' &nbsp; <i>B</i> = '+mat(B16,fs=17)),('b','<i>C</i> = '+mat([[50,70,27],[67,75,21]],fs=17)+': the total sales for 2014 and 2015 for the two dealers.'),
         ('c','<i>D</i> = '+mat([[2,6,5],[3,7,3]],fs=17)+': the increase in sales from 2014 to 2015 for the two dealers.'),
         ('d','<i>E</i> = '+mat([[39,57,24],[52.5,61.5,18]],fs=17)+': forming 1.5<i>B</i> multiplies each element by 1.5, which increases each value by 50%.')]))
S[-1]=S[-1].replace('<section class="slide T we','<section class="slide T we sm',1)
A16y=[[18,25,9],[27,22,14]]; B16y=[[22,30,12],[28,26,16]]
S.append(qslide('yt','You try · written for 12MAG','Processing data using matrix arithmetic',
  '<div style="font-size:18px">The bread sales (small, medium, large loaves) for two bakeries are displayed below.'
  +sales(('Bread sales',('Small','Medium','Large'),('Corner Bake','Daily Loaf')),A16y,B16y,'2024','2025','y16')
  +plist([('a','<b>Construct</b> two matrices, <i>A</i> and <i>B</i>, to represent the sales data for 2024 and 2025 separately.'),('b','<b>Construct</b> a new matrix <i>C</i> = <i>A</i> + <i>B</i>. What does this matrix represent?'),
          ('c','<b>Construct</b> a new matrix, <i>D</i> = <i>B</i> − <i>A</i>. What does this matrix represent?'),('d','Both bakeries want to increase their 2025 sales by 50% by 2026. <b>Construct</b> a new matrix <i>E</i> = 1.5<i>B</i>. <b>Explain</b> why this matrix represents the planned sales figures for 2026.')])+'</div>',
  [('a','2024 columns → <i>A</i>, 2025 columns → <i>B</i>','data-hi="#y16|'+cells(0,2,0,3)+'|hy"'),('b','add corresponding elements','data-hi="#y16|'+cells(0,2,0,6)+'|hb"'),('c','subtract corresponding elements'),('d','1.5 × each element of <i>B</i>')],
  '','Written for 12MAG (modelled on Cambridge Example 16; no Edrolo match) · planner/written-youtrys.json YT-10C-16',cmd=('Construct',None,'one matrix per year'),
  parts=[('a','<i>A</i> = '+mat(A16y,fs=17)+' &nbsp; <i>B</i> = '+mat(B16y,fs=17)),('b','<i>C</i> = '+mat([[40,55,21],[55,48,30]],fs=17)+': the total sales for 2024 and 2025 for the two bakeries.'),
         ('c','<i>D</i> = '+mat([[4,5,3],[1,4,2]],fs=17)+': the increase in sales from 2024 to 2025 for the two bakeries.'),
         ('d','<i>E</i> = '+mat([[33,45,18],[42,39,24]],fs=17)+': each 2025 figure is multiplied by 1.5, a 50% increase, giving the planned 2026 sales.')]))
S[-1]=S[-1].replace('<section class="slide T yt','<section class="slide T yt sm',1)

# ================= Exits
X1=[EQ(mat([[8],[12]],fs=20),'+',mat([[4],[2]],fs=20)),EQ(mat([[8],[12]],fs=20),'+',mat([[4,0],[0,2]],fs=20)),EQ(mat([[8,0],[12,0]],fs=20),'+',mat([[4],[2]],fs=20)),EQ(mat([[8,0],[12,0]],fs=20),'+',mat([[4,0],[0,2]],fs=20))]
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2019 Exam 1 Q1','Show what you know',
  '<div style="font-size:24px">Consider the following four matrix expressions.'+C(*X1,gap=26)+'How many of these four matrix expressions are defined?</div>',
  [('Orders','2 × 1 + 2 × 1 · 2 × 1 + 2 × 2 · 2 × 2 + 2 × 1 · 2 × 2 + 2 × 2'),('Same order?','only the first and the last have matching orders')],
  '2 are defined: <b>C</b>.','VCAA 2019 Further Mathematics Exam 1 Matrices Q1 (87% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7B Q13',
  mc=['0','1','2','3','4'],key='C',stat=('mc',87)))
T14=[[2,7,10],[13,19,8]]
OP14=[[[13,19,8],[2,7,10]],[[10,7,2],[8,19,13]],[[2,13],[7,19],[10,8]],[[13,2],[19,7],[8,10]],[[8,10],[19,7],[13,2]]]
S.append(grid(qslide('ex','Exit task 2 of 2 · VCAA 2016 Exam 1 Q1','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The transpose of '+mat(T14,fs=26,tid='x2')+' is</div>',
  [('Order','2 × 3 becomes 3 × 2'),('Rows → columns','row 1 (2, 7, 10) becomes column 1; row 2 (13, 19, 8) becomes column 2','data-hi="#x2|c0_0,c0_1,c0_2|hy"')],
  mat(OP14[2],fs=16)+' : <b>C</b>.','VCAA 2016 Further Mathematics Exam 1 Matrices Q1 (81% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7B Q14',
  mc=[mat(o,fs=15) for o in OP14],key='C',stat=('mc',81))))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 10 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='10C' and v.get('url')]))
n=assemble(S,'12MAG · 10C · Matrix arithmetic',os.path.join(ROOT,'lessons','10C slides.html'))
print(n-1,'slides')
