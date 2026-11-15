"""Lesson gm12-u4-10a10b (10A What is a matrix? · 10B Using matrices to represent information) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/10A-10B slides.html      Run: python3 tools/deck/gm12-u4-10a10b/build.py      Screenshots: python3 tools/deck/gm12-u4-10a10b/shoot.py
Matrices drawn with tools/deck/mx.py (new reusable helper for AoS 3).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- Do Now: VCAA 2025 Exam 1 Q2 (stem + histogram cropped from the paper; D, 76%) ·
          VCAA 2024 Exam 1 Q15 (C, 70%) ·
          VCAA 2024 Exam 2 Q2a (boxplot cropped; average 0.9/1 = 90%) ·
          VCAA 2026 Exam 2 Q3 stem + Q3a (2026 report not yet released; 13.5% worked for 12MAG).
- APK: Cambridge U1&2 Ch 4 skills checklist 4A #1 and #2 (matrices from tools/y11_cambridge_skills_checklist.csv: the checklist PDF is not on G:; solutions worked for 12MAG) ·
       VCAA 2020 Further Exam 1 Matrices Q6 (ORIGINAL wording m_ij = 3i + 2j; Edrolo U1&2 5A Q13 adapts it to s_ij = 2i + j). Answer B.
       No 2020 Exam 1 examiner report on G: (Edrolo quotes 73% 'for this type'): % left blank.
- Learn: Cambridge U3&4 10A pp. 473-480, 10B pp. 485-487 (own words) · Edrolo U3&4 7A pp. 419-423.
- Worked examples: Cambridge U3&4 Examples 1-10 (pp. 474-487). Ex 9 network drawn from the book; Ex 10 network cropped from p. 487.
  You trys: Edrolo U3&4 7A WE1a, 7B WE3, Edrolo U1&2 5A WE2, Edrolo U3&4 7A WE2a-e, 7A WE1b, 7A WE4, 7A WE3a-b,
            YT-10B-8 (written, planner/written-youtrys.json), Edrolo U1&2 5D WE3a, YT-10B-10 (written).
- CAS: planner/cas-skills.json 'matrix-entry' (task = Cambridge Example 4 symmetric matrix, as the card says: CAS 1 with the Example 4 matrices).
- Exit 1: VCAA 2018 Further Exam 2 Matrices Q1a-c (= Edrolo U3&4 7A Q12). Parts a, b original; part c original asks for M in M × C (10D content):
          Edrolo's wording 'Construct a row matrix that shows this' used, labelled adapted. Report: a 99%, b 94%, c 66%.
- Exit 2: VCAA 2017 Further Exam 1 Matrices Q6 (= Edrolo U3&4 7B Q15). D; report: A 6, B 13, C 12, D 58, E 10.
          Needs A + B (10C): kept, the step is 'add matching elements' (decision logged in docs/QUEUE.md).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-10a10b')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def lab(l,x): return f'<span style="display:inline-flex;align-items:center;gap:8px"><b>{l}</b>{x}</span>'
def stab(heads,rows,fs=18,tid='',lead=''):
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px;margin:8px auto"><tr><th>{lead}</th>'+''.join(f'<th>{h}</th>' for h in heads)+'</tr>'
    for r,(l,vals) in enumerate(rows): t+=f'<tr><th>{l}</th>'+''.join(f'<td data-i="c{r}_{k}">{v}</td>' for k,v in enumerate(vals))+'</tr>'
    return t+'</table>'

S=['<style>.sm .L .q{font-size:17px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}'
   '.mxg{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:8px}.mxg>div{background:#fff;border:3px solid var(--learn);border-radius:14px;padding:10px;text-align:center;font-size:18px}.mxg b{display:block;font-size:20px;margin-bottom:6px}</style>']
# ================= opening
t=title('10A–10B','What is a matrix? Using matrices to represent information',f'{CAM} · 10A What is a matrix? · 10B Using matrices to represent information','10A-10B')
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('Learn: what is a matrix?','',None),('Worked examples 1–6','→ You try',None),('CAS: entering a matrix','',None),
  ('Learn: matrices from tables and networks','',None),('Worked examples 7–10','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Matrix','a rectangular array of numbers (elements) in rows and columns',mat([[1,2],[3,4],[5,6]],fs=15)),
  ('Order','rows × columns: the matrix above is 3 × 2'),
  ('Row / column / square','one row · one column · rows = columns'),
  ('Leading diagonal','top left to bottom right of a square matrix'),
  ('Diagonal · identity (I)','zeros off the leading diagonal · and 1s on it'),
  ('Symmetric','equal to its own transpose (mirror image across the leading diagonal)'),
  ('Upper / lower triangular','zeros below / above the leading diagonal')],
  [('Order',F('rows × columns'),'number of elements = rows × columns'),
   ('Element',F('<i>a</i><sub><i>ij</i></sub> = row <i>i</i>, column <i>j</i>'),'row first, then column'),
   ('Transpose',F('<i>A</i><sup>T</sup>: rows become columns'),'an m × n matrix becomes n × m'),
   ('Network matrix',F('1 = joined · 0 = not joined'),'or the number of connections')],
  f'{CAM}, 10A pp. 473–480, 10B pp. 485–487; Study Design: matrix arithmetic (order, types, transpose) and matrices representing tables and rules'))

# ================= Do Now 1: VCAA 2025 E1 Q2 (1F)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q2','Review of AoS 1 (last term)',
  ('<div style="font-size:20px">At a fruit shop, customers can buy avocados in bags.<br>The <em class="v">bag size</em> ranges from one to six avocados per bag.<br>The histogram below shows the number of customers who bought each <em class="v">bag size</em> on a particular day.</div>',
   IMG('dn1_hist.png',360),'<div style="font-size:20px">The total number of avocados sold in bags was</div>'),
  [('Read','frequencies: 4, 11, 3, 9, 5, 7 customers'),('Multiply','avocados = bag size × customers: 4 + 22 + 9 + 36 + 25 + 42'),('Add','total = 138')],
  '138 avocados: <b>D</b>.','VCAA 2025 General Mathematics Exam 1 Q1–2 stem and Q2 (examiner report: 76% correct)',
  mc=['39','134','136','138'],key='D',stat=('mc',76)))
# ================= Do Now 2: VCAA 2024 E1 Q15 (5B)
CANS=[316,321,365,306,254,308,354,357,381,355,365,324]
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q15','Review of 5B (last term)',
  '<div style="font-size:21px">The table below shows the total number of cans of soft drink sold each month at a suburban cafe in 2023.'
  +''.join(f'<table class="t tight" id="d2{h}" style="font-size:18px;margin:8px auto"><tr><th>Month</th>'+''.join(f'<td>{k+1}</td>' for k in range(6*i,6*i+6))+'</tr><tr><th>Cans sold</th>'+''.join(f'<td data-i="c{k}">{CANS[k]}</td>' for k in range(6*i,6*i+6))+'</tr></table>' for i,h in enumerate('ab'))
  +'The six-mean smoothed value of the number of cans sold, with centring, for month 5 is closest to</div>',
  [fx('Mean 1','months 2–7',F(FR([V('sum','1908')],[V('n','6')])),'318','data-hi="#d2a|c1,c2,c3,c4,c5|hy;#d2b|c6|hy"'),
   fx('Mean 2','months 3–8',F(FR([V('sum','1944')],[V('n','6')])),'324','data-hi="#d2a|c2,c3,c4,c5|hb;#d2b|c6,c7|hb"'),
   fx('Centre','month 5',F(FR([V('318 + 324','642')],[V('','2')])),'321','data-hi="#d2a|c4|hg;#d2b||"')],
  '321: <b>C</b>.','VCAA 2024 General Mathematics Exam 1 Q15 (examiner report: 70% correct)',
  mc=['315','318','321','324'],key='C',stat=('mc',70)))
# ================= Do Now 3: VCAA 2024 E2 Q2a (1C)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q2a','Review of 1C (last term)',
  ('<div style="font-size:20px">The boxplot below displays the distribution of all gold medal-winning heights for the women’s high jump, <em class="v">Wgold</em>, in metres, for the 19 Olympic Games held from 1948 to 2020.</div>',
   IMG('dn3_box.png',560),'<div style="font-size:21px">a. <b>Describe</b> the shape of this data distribution. <span class="muted">(1 mark)</span></div>'),
  [('Look','the long whisker and the longer box section are on the LEFT (low values)'),('Tail','tail to the left = negative skew')],
  'The distribution is <b>negatively skewed</b>.','VCAA 2024 General Mathematics Exam 2 Q2 stem and Q2a (examiner report: average 0.9/1)',
  stat=('mark',90),cmd=('Describe',1,'shape only: name the skew')))
# ================= Do Now 4: VCAA 2026 E2 Q3a (1H)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q3a','Review of 1H (last term)',
  '<div style="font-size:24px;margin-top:20px">The <em class="v">happiness level</em> scores for a group of 2000 students are collected as a data set. The data set is modelled by a normal distribution with a mean of 72 and a standard deviation of 8.0<br><br>'
  'a. Using the 68–95–99.7% rule, <b>find</b> the expected percentage of students in this group with a <em class="v">happiness level</em> score between 80 and 88. <span class="muted">(1 mark)</span></div>',
  [fx('z for 80','<i>z</i>',F(FR([V('x − mean','80 − 72')],[V('sd','8')])),'1'),fx('z for 88','<i>z</i>',F(FR([V('x − mean','88 − 72')],[V('sd','8')])),'2'),
   ('Rule','between z = 1 and z = 2: 47.5% − 34% = 13.5%')],
  '<b>13.5%</b> of the students.','VCAA 2026 General Mathematics Exam 2 Q3 stem and Q3a (2026 report not yet released)',
  stat=('new',),cmd=('find',1,'z-scores, then the 68–95–99.7% rule')))

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4A #1','The order of a matrix',
  '<div style="font-size:30px;margin-top:40px">State the order of the following matrix:'+C(mat([[7,-2,5],[10,0,4]],fs=32,tid='a1'))+'</div>',
  [('Rows','2 rows','data-hi="#a1|'+cells(0,2,0,1)+'|hy"'),('Columns','3 columns','data-hi="#a1|'+cells(0,1,0,3)+'|hb"')],
  'Order <b>2 × 3</b> (rows × columns).',f'{CAM12} · Ch 4 skills checklist 4A #1 · solution worked for 12MAG',cmd=('State',None,'rows × columns')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4A #2','The location of an element',
  '<div style="font-size:30px;margin-top:40px">Considering the following matrix, <i>B</i>, state the value of the element in <i>b</i><sub>23</sub>.'+C(mat([[57,63,19],[48,54,6]],name='B',fs=32,tid='a2'))+'</div>',
  [('Row','<i>b</i><sub>23</sub>: row 2','data-hi="#a2|'+cells(1,2,0,3)+'|hy"'),('Column','column 3','data-hi="#a2|c1_2|hg"')],
  '<i>b</i><sub>23</sub> = <b>6</b>',f'{CAM12} · Ch 4 skills checklist 4A #2 · solution worked for 12MAG',cmd=('state',None,'row first, then column')))
def M3(r): return mat(r,fs=17)
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q6','Constructing a matrix from a rule',
  '<div style="font-size:24px;margin-top:20px">The element in row <i>i</i> and column <i>j</i> of matrix <i>M</i> is <i>m<sub>ij</sub></i>.<br><i>M</i> is a 3 × 3 matrix. It is constructed using the rule <i>m<sub>ij</sub></i> = 3<i>i</i> + 2<i>j</i>.<br><i>M</i> is</div>',
  [('Row 1','<i>i</i> = 1: 3 + 2 = 5, 3 + 4 = 7, 3 + 6 = 9'),('Row 2','<i>i</i> = 2: 8, 10, 12'),('Row 3','<i>i</i> = 3: 11, 13, 15')],
  mat([[5,7,9],[8,10,12],[11,13,15]],fs=18)+' : <b>B</b>.','VCAA 2020 Further Mathematics Exam 1 Matrices Q6 (original wording; no 2020 Exam 1 examiner report on file) · Edrolo U1&amp;2 5A Q13 (adapted)',
  mc=[M3([[5,7,9],[7,9,11],[11,13,15]]),M3([[5,7,9],[8,10,12],[11,13,15]]),M3([[5,7,10],[8,10,13],[11,13,16]]),M3([[5,8,11],[7,10,13],[9,12,15]]),M3([[5,8,11],[8,11,14],[11,14,17]])],key='B'))
S[-1]=S[-1].replace('<div class="mc"','<div class="mc" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px"',1)

# ================= Learn 1: what is a matrix?
EXM=[[1,4,4,5],[4,3,4,6],[4,3,2,1]]
S.append(learn('Learn · 10A','What is a matrix?',
  '<h4>Rows × columns</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a matrix is a rectangular array of numbers (<b>elements</b>)</li><li><b>order</b> = rows × columns (rows first)</li>'
  '<li><i>a<sub>ij</sub></i> = element in row <i>i</i>, column <i>j</i></li><li><b>row</b> matrix: 1 row · <b>column</b> matrix: 1 column · <b>square</b>: rows = columns</li>'
  '<li><b>transpose</b> <i>A</i><sup>T</sup>: rows become columns</li></ul>',
  '<div style="display:flex;gap:40px;justify-content:center;align-items:center;margin-top:6px">'+mat(EXM,name='A',fs=24,tid='l1')+
  '<div style="font-size:21px"><div class="frag" data-hi="#l1|'+cells(0,3,0,4)+'|hy">3 rows, 4 columns: order <b>3 × 4</b> · 12 elements</div>'
  '<div class="frag" data-hi="#l1|c1_2|hg" style="margin-top:8px"><i>a</i><sub>23</sub> = row 2, column 3 = <b>4</b></div>'
  '<div class="frag" style="margin-top:8px;display:flex;gap:10px;align-items:center">Transpose: '+mat([[1,2],[3,4],[5,6]],fs=18,sup='T')+' = '+mat([[1,3,5],[2,4,6]],fs=18)+'</div></div></div>',
  'Order is always rows first: a 2 × 3 matrix has 2 rows, not 2 columns.',f'{CAM}, 10A pp. 473–476 (own words) · {EDR}, 7A pp. 419–420',
  cards=(kcard('Order',F('rows × columns')),kcard('Element',F('<i>a</i><sub><i>ij</i></sub>: row <i>i</i>, column <i>j</i>')))))

# ================= Ex 1 / YT 7A WE1a
EX1={'a':[[1,5],[3,0],[7,6]],'b':[[1,5,8,9,0]],'c':[[1],[4],[4],[9]],'d':[[1,4,4,5],[4,3,4,6],[4,3,2,1],[9,1,0,7]]}
S.append(qslide('we','Worked example 1 · 10A','The order of a matrix',
  '<div style="font-size:24px">State the order of each of the following matrices.'+C(*[lab(k,mat(v,fs=22)) for k,v in EX1.items()])+'</div>',
  [('a','3 rows and 2 columns'),('b','1 row and 5 columns'),('c','4 rows and 1 column'),('d','4 rows and 4 columns')],
  '','f',cmd=('State',None,'rows × columns'),video='Cambridge GO · Example 1 (10A Resources)',
  parts=[('a','Order is <b>3 × 2</b>'),('b','Order is <b>1 × 5</b>'),('c','Order is <b>4 × 1</b>'),('d','Order is <b>4 × 4</b>')]).replace('<div class="src">f</div>',f'<div class="src">{CAM} · Example 1 (p. 474)</div>'))
WE1=[[101,2,85],[41,56,73]]
S.append(qslide('yt','You try · Edrolo 7A WE1a','The order of a matrix',
  '<div style="font-size:28px;margin-top:30px">Matrix <i>A</i> contains a list of multiple elements.'+C(mat(WE1,name='A',fs=30,tid='y1'))+'a. What is the order of matrix <i>A</i>?</div>',
  [('Rows','The matrix has 2 rows.','data-hi="#y1|'+cells(0,2,0,1)+'|hy"'),('Columns','The matrix has 3 columns.','data-hi="#y1|'+cells(0,1,0,3)+'|hb"')],
  '<b>2 × 3</b>',f'{EDR} · 7A Worked example 1a (p. 420)'))
# ================= Ex 2 / YT 7B WE3
S.append(qslide('we','Worked example 2 · 10A','The transpose of a matrix',
  '<div style="font-size:24px">'+plist([('a','Write down the transpose of '+mat([[7,4],[8,1]],fs=22)+'.'),('b','Write down the matrix '+mat([[0,1,2],[3,2,5]],fs=22,sup='T')+'.'),('c','If <i>A</i> = '+mat([[2,0,1]],fs=22)+', write down the matrix <i>A</i><sup>T</sup>.')])+'</div>',
  [('Rule','switch rows and columns: row 1 becomes column 1, row 2 becomes column 2'),('Order','a 2 × 3 matrix becomes 3 × 2; a row matrix becomes a column matrix')],
  '',f'{CAM} · Example 2 (p. 475)',video='Cambridge GO · Example 2 (10A Resources)',cmd=('Write down',None,'rows become columns'),
  parts=[('a',mat([[7,8],[4,1]],fs=20)),('b',mat([[0,3],[1,2],[2,5]],fs=20)),('c','<i>A</i><sup>T</sup> = '+mat([[2],[0],[1]],fs=20))]))
S.append(qslide('yt','You try · Edrolo 7B WE3','The transpose of a matrix',
  '<div style="font-size:30px;margin-top:40px">If <i>D</i> = '+mat([[1,0,9],[5,2,3]],fs=30,tid='y2')+', <b>determine</b> <i>D</i><sup>T</sup>.</div>',
  [('Order','<i>D</i> is 2 × 3, so <i>D</i><sup>T</sup> will be 3 × 2'),('Row 1','first row of <i>D</i> → first column of <i>D</i><sup>T</sup>: 1, 0, 9','data-hi="#y2|'+cells(0,1,0,3)+'|hy"'),
   ('Row 2','second row → second column: 5, 2, 3','data-hi="#y2|'+cells(1,2,0,3)+'|hb"')],
  '<i>D</i><sup>T</sup> = '+mat([[1,5],[0,2],[9,3]],fs=22),f'{EDR} · 7B Worked example 3 (p. 432)',cmd=('determine',None,'rows become columns')))
# ================= Ex 3 / YT U1&2 5A WE2
S.append(qslide('we','Worked example 3 · 10A','Matrix facts',
  '<div style="font-size:23px">For each of the matrices below, write down its type, order and the number of elements.'
  +C(mat([[1,5,1],[2,2,4],[2,-1,6]],name='A',fs=22),mat([[1],[0],[1]],name='B',fs=22),mat([[3,1,0,5,-3,1]],name='C',fs=22))+'</div>',
  [('A','rows = columns: 3 rows, 3 cols · 3 × 3 = 9'),('B','single column: 3 rows, 1 col · 3 × 1 = 3'),('C','single row: 1 row, 6 cols · 1 × 6 = 6')],
  '',f'{CAM} · Example 3 (p. 476)',video='Cambridge GO · Example 3 (10A Resources)',cmd=('write down',None,'type · order · elements'),
  parts=[('A','<b>Square</b> matrix · <b>3 × 3</b> · <b>9</b> elements'),('B','<b>Column</b> matrix · <b>3 × 1</b> · <b>3</b> elements'),('C','<b>Row</b> matrix · <b>1 × 6</b> · <b>6</b> elements')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5A WE2','Matrix facts',
  '<div style="font-size:24px">Classify the following matrices as either a row, column, square, zero or identity matrix. There may be more than one answer.'
  +plist([('a','<i>B</i> = '+mat([[12,23,42,7]],fs=22)),('b','<i>C</i> = '+mat([[0,0,0,0],[0,0,0,0]],fs=22)),('c','<i>D</i> = '+mat([[1,0,0],[0,1,0],[0,0,1]],fs=22))])+'</div>',
  [('a','one row and four columns'),('b','all of the elements are zero'),('c','3 rows and 3 columns; leading diagonal all 1, all other elements 0')],
  '',f'{EDR12} · 5A Worked example 2 (p. 254)',cmd=('Classify',None,'look at the shape, then the elements'),
  parts=[('a','<b>Row</b> matrix'),('b','<b>Zero</b> matrix'),('c','<b>Square</b> and <b>identity</b> matrix')]))

# ================= Learn 2: special square matrices
def sq(t,m,frag=True): return f'<div class="{"frag" if frag else ""}"><b>{t}</b>{m}</div>'
S.append(learn('Learn · 10A','Types of square matrices',
  '<h4>Look at the leading diagonal</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>leading diagonal</b>: top left → bottom right</li><li><b>diagonal</b>: zeros everywhere off it</li><li><b>identity</b> <i>I</i>: diagonal with all 1s</li>'
  '<li><b>symmetric</b>: mirror image across it (<i>A</i><sup>T</sup> = <i>A</i>)</li><li><b>upper / lower triangular</b>: zeros below / above it</li></ul>',
  '<div class="mxg">'+sq('Diagonal',mat([[2,0,0],[0,6,0],[0,0,3]],fs=20))+sq('Identity',mat([[1,0,0],[0,1,0],[0,0,1]],fs=20))+sq('Symmetric',mat([[1,2,4],[2,3,5],[4,5,3]],fs=20))
  +sq('Upper triangular',mat([[1,2,3],[0,4,5],[0,0,6]],fs=20))+sq('Lower triangular',mat([[3,0,0],[6,5,0],[9,8,7]],fs=20))+'</div>'
  '<div class="frag" style="font-size:22px;text-align:center;margin-top:16px">A matrix can be more than one type: <i>I</i> is diagonal, symmetric, upper AND lower triangular.</div>',
  'Only square matrices can be diagonal, identity, symmetric or triangular.',f'{CAM}, 10A pp. 476–478 (own words; matrices adapted from the book’s examples) · {EDR}, 7A pp. 420–421',
  cards=(kcard('Symmetric',F('<i>A</i><sup>T</sup> = <i>A</i>')),)))
# ================= Ex 4 / YT 7A WE2
E4=[[[1,0],[0,1]],[[1,2],[0,3]],[[1,0,0],[0,4,0],[0,0,3]],[[1,3,5],[3,4,7],[5,7,2]]]
S.append(qslide('we','Worked example 4 · 10A','Types of matrices',
  '<div style="font-size:23px">Consider the following square matrices.'+C(*[mat(m,fs=20,tid=f'e4{k}') for k,m in enumerate(E4)])+'Write down:'
  +plist([('a','the upper triangular matrices'),('b','the identity matrix'),('c','the diagonal matrices'),('d','the symmetric matrices.')])+'</div>',
  [('a','all elements below the leading diagonal are 0'),('b','leading diagonal all 1, other elements 0'),('c','all elements other than the leading diagonal are zero'),('d','the matrix must be its own transpose')],
  '',f'{CAM} · Example 4 (p. 478)',video='Cambridge GO · Example 4 (10A Resources)',cmd=('Write down',None,'check each matrix against the definition'),
  parts=[('a',mat(E4[1],fs=16)+', '+mat(E4[0],fs=16)+' and '+mat(E4[2],fs=16)),('b',mat(E4[0],fs=16)),('c',mat(E4[0],fs=16)+', '+mat(E4[2],fs=16)),('d',mat(E4[3],fs=16)+', '+mat(E4[0],fs=16)+' and '+mat(E4[2],fs=16))]))
S[-1]=S[-1].replace('<section class="slide T we','<section class="slide T we sm',1)
W2={'P':[[6,5,2],[0,5,6],[0,0,5]],'Q':[[1,0,5],[0,0,2],[5,2,3]],'R':[[1,0,0],[0,1,0],[0,0,1]],'S':[[5,0,0],[0,4,0],[0,0,7]],'T':[[0,0,0],[11,2,0],[2,5,8]]}
S.append(qslide('yt','You try · Edrolo 7A WE2','Types of matrices',
  '<div style="font-size:19px">Matrices <i>P</i>, <i>Q</i>, <i>R</i>, <i>S</i> and <i>T</i> are all 3 × 3 matrices. Each of the following matrices fall into one or more classifications, namely diagonal, identity, symmetric, upper triangular, and lower triangular.'
  +C(*[mat(v,name=k,fs=18) for k,v in W2.items()],gap=18)
  +plist([(k.lower() if False else 'abcde'[i],f'How can matrix <i>{k}</i> be classified?') for i,k in enumerate(W2)])+'</div>',
  [('P','all elements below the main diagonal are 0'),('Q','each element is symmetric across the leading diagonal'),('R','1s on the leading diagonal, 0 elsewhere'),('S','0s off the leading diagonal'),('T','all elements above the main diagonal are 0')],
  '',f'{EDR} · 7A Worked example 2a–e (pp. 420–422)',cmd=('classified',None,'check every type'),
  parts=[('a','Upper triangular'),('b','Symmetric'),('c','Symmetric, diagonal, identity, upper triangular, lower triangular'),('d','Symmetric, diagonal, upper triangular, lower triangular'),('e','Lower triangular')]))
S[-1]=S[-1].replace('<section class="slide T yt','<section class="slide T yt sm',1)
# ================= Ex 5 / YT 7A WE1b
S.append(qslide('we','Worked example 5 · 10A','Identifying the elements in a matrix',
  '<div style="font-size:24px">For the matrices <i>A</i> and <i>B</i>, opposite, write down the values of:'+C(mat([[1,5,3],[-1,0,4],[2,-2,6]],name='A',fs=26,tid='e5a'),mat([[3],[2],[1]],name='B',fs=26,tid='e5b'))
  +plist([('a','<i>a</i><sub>12</sub>'),('b','<i>a</i><sub>21</sub>'),('c','<i>a</i><sub>33</sub>'),('d','<i>b</i><sub>31</sub>')])+'</div>',
  [('a','first row, second column of <i>A</i>','data-hi="#e5a|c0_1|hy"'),('b','second row, first column of <i>A</i>','data-hi="#e5a|c1_0|hy"'),
   ('c','third row, third column of <i>A</i>','data-hi="#e5a|c2_2|hy"'),('d','third row, first column of <i>B</i>','data-hi="#e5b|c2_0|hy"')],
  '',f'{CAM} · Example 5 (p. 479)',video='Cambridge GO · Example 5 (10A Resources)',cmd=('write down',None,'row first, then column'),
  parts=[('a','<i>a</i><sub>12</sub> = <b>5</b>'),('b','<i>a</i><sub>21</sub> = <b>−1</b>'),('c','<i>a</i><sub>33</sub> = <b>6</b>'),('d','<i>b</i><sub>31</sub> = <b>1</b>')]))
S.append(qslide('yt','You try · Edrolo 7A WE1b','Identifying the elements in a matrix',
  '<div style="font-size:28px;margin-top:30px">Matrix <i>A</i> contains a list of multiple elements.'+C(mat(WE1,name='A',fs=30,tid='y5'))+'b. What is element <i>a</i><sub>21</sub>?</div>',
  [('Row','the 2 in <i>a</i><sub>21</sub> refers to the second row','data-hi="#y5|'+cells(1,2,0,3)+'|hy"'),('Column','the 1 refers to the first column','data-hi="#y5|c1_0|hg"')],
  '<i>a</i><sub>21</sub> = <b>41</b>',f'{EDR} · 7A Worked example 1b (p. 420)'))
# ================= Ex 6 / YT 7A WE4
S.append(qslide('we','Worked example 6 · 10A','Constructing a matrix given a rule for its <i>ij</i>th term',
  '<div style="font-size:26px;margin-top:30px"><i>A</i> is a 3 × 2 matrix. The element in row <i>i</i> and column <i>j</i> is given by <i>a<sub>ij</sub></i> = <i>i</i> + <i>j</i>.<br><b>Construct</b> the matrix.</div>',
  [('Form','<i>A</i> = '+mat([['a<sub>11</sub>','a<sub>12</sub>'],['a<sub>21</sub>','a<sub>22</sub>'],['a<sub>31</sub>','a<sub>32</sub>']],fs=18)),
   ('Row 1','<i>a</i><sub>11</sub> = 1 + 1 = 2 · <i>a</i><sub>12</sub> = 1 + 2 = 3'),('Row 2','<i>a</i><sub>21</sub> = 2 + 1 = 3 · <i>a</i><sub>22</sub> = 2 + 2 = 4'),('Row 3','<i>a</i><sub>31</sub> = 3 + 1 = 4 · <i>a</i><sub>32</sub> = 3 + 2 = 5')],
  '<i>A</i> = '+mat([[2,3],[3,4],[4,5]],fs=22),f'{CAM} · Example 6 (p. 479)',video='Cambridge GO · Example 6 (10A Resources)',cmd=('Construct',None,'write the form, then use the rule')))
S.append(qslide('yt','You try · Edrolo 7A WE4','Constructing a matrix given a rule',
  '<div style="font-size:26px;margin-top:30px">Matrix <i>C</i> is a matrix with an order of 3 × 2.<br><b>Construct</b> matrix <i>C</i>, with the element rule <i>c<sub>ij</sub></i> = <i>i</i> × <i>j</i>, where <i>c<sub>ij</sub></i> refers to the entry in the <i>i</i><sup>th</sup> row and <i>j</i><sup>th</sup> column.</div>',
  [('Form','<i>C</i> = '+mat([['c<sub>11</sub>','c<sub>12</sub>'],['c<sub>21</sub>','c<sub>22</sub>'],['c<sub>31</sub>','c<sub>32</sub>']],fs=18)),
   ('Elements',mat([['1 × 1','1 × 2'],['2 × 1','2 × 2'],['3 × 1','3 × 2']],fs=18))],
  '<i>C</i> = '+mat([[1,2],[2,4],[3,6]],fs=22),f'{EDR} · 7A Worked example 4 (p. 423)',cmd=('Construct',None,'write the form, then use the rule')))

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-entry']
S.append(cas('CAS · 10A','Entering a matrix',
  '<p style="font-size:21px">Enter this matrix from Example 4, store it as <i>A</i>, then find its transpose.</p>'+C(mat(E4[3],name='A',fs=28))+
  '<p style="font-size:20px">Is <i>A</i> symmetric?</p><p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'],CS['classpad'],'<i>A</i><sup>T</sup> = '+mat(E4[3],fs=16)+' = <i>A</i>, so <i>A</i> is <b>symmetric</b>.',
  f'{CAM} · 10A CAS 1 (p. 480), Example 4 matrix · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in CS['videos']['ti'][:1]+CS['videos']['classpad'][:1]]))

# ================= Learn 3: 10B
GYM=stab(['Weights','Aerobics','Fitness'],[('Males',[16,104,86]),('Females',[75,34,94])],18,'',lead='Gender')
S.append(learn('Learn · 10B','Matrices from tables and networks',
  '<h4>Same layout, numbers only</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>table → matrix</b>: copy the numbers row by row, keep the labels</li><li><b>network → matrix</b>: one row and one column per point</li>'
  '<li>element = 1 if joined, 0 if not (or the number of lines)</li><li>no loops → leading diagonal all 0; two-way lines → symmetric</li></ul>',
  '<div style="display:flex;gap:30px;justify-content:center;align-items:center">'
  '<div class="frag">'+GYM+'</div><div class="frag" style="font-size:30px">→ '+mat([[16,104,86],[75,34,94]],fs=22,rl=['M','F'],cl=['W','A','F'])+'</div></div>'
  '<div style="display:flex;gap:30px;justify-content:center;align-items:center;margin-top:10px"><div class="frag">'+IMG('ex9_net.png',160)+'</div>'
  '<div class="frag" style="font-size:30px">→ '+mat([[0,1,0,1],[1,0,1,1],[0,1,0,0],[1,1,0,0]],fs=20,rl='ABCD',cl='ABCD')+'</div></div>',
  'Rows and columns of a network matrix list the points in the SAME order.',f'{CAM}, 10B pp. 485–487 (own words; Examples 7 and 9) · {EDR}, 7A p. 422',
  cards=(kcard('Network matrix',F('1 = joined · 0 = not')),)))
# ================= Ex 7 / YT 7A WE3a-b
S.append(qslide('we','Worked example 7 · 10B','Representing information in a table by a matrix',
  '<div style="font-size:24px">The table opposite shows the three types of membership of a local gym and the number of males and females enrolled in each. <b>Construct</b> a matrix to display the numerical information in the table.'
  +stab(['Weights','Aerobics','Fitness'],[('Males',[16,104,86]),('Females',[75,34,94])],22,'e7',lead='Gender')+'</div>',
  [('Blank','draw a blank 2 × 3 matrix: rows <i>M</i>, <i>F</i> · columns <i>W</i>, <i>A</i>, <i>F</i>'),('Row 1','males: 16, 104, 86','data-hi="#e7|'+cells(0,1,0,3)+'|hy"'),('Row 2','females: 75, 34, 94','data-hi="#e7|'+cells(1,2,0,3)+'|hb"')],
  mat([[16,104,86],[75,34,94]],fs=22,rl=['M','F'],cl=['W','A','F']),f'{CAM} · Example 7 (p. 485; table on the opposite side in the book)',video='Cambridge GO · Example 7 (10B Resources)',cmd=('Construct',None,'row by row from the top left')))
FR_=stab(['banana','dragon fruit','kiwi fruit'],[('adult',[14,19,16]),('child',[23,11,17])],20,'y7',lead='')
S.append(qslide('yt','You try · Edrolo 7A WE3a, b','Representing information in a table by a matrix',
  '<div style="font-size:22px">A group of 100 people were surveyed about their favourite fruit. Their results are shown in the table.'+FR_.replace('<tr><th></th>','<tr><th></th><th colspan="3" style="font-style:italic">favourite fruit</th></tr><tr><th></th>',1)
  +plist([('a','<b>Construct</b> matrix <i>F</i>, to represent the information in the table.'),('b','<b>Construct</b> a row matrix to represent the favourite fruit of adults surveyed.')])+'</div>',
  [('a · set up','2 rows (A, C) and 3 columns (B, D, K): order 2 × 3'),('a · fill','row 1 = adults: 14, 19, 16 · row 2 = children: 23, 11, 17','data-hi="#y7|'+cells(0,2,0,3)+'|hy"'),
   ('b','the first row of the table: one row, three columns','data-hi="#y7|'+cells(0,1,0,3)+'|hb"')],
  '',f'{EDR} · 7A Worked example 3a, b (pp. 422–423)',cmd=('Construct',None,'label rows and columns first'),
  parts=[('a','<i>F</i> = '+mat([[14,19,16],[23,11,17]],fs=20,rl='AC',cl='BDK',side=True)),('b',mat([[14,19,16]],fs=20))]))
# ================= Ex 8 / YT-10B-8
S.append(qslide('we','Worked example 8 · 10B','Entering a credit card number into a matrix',
  '<div style="font-size:28px;margin-top:40px">Convert the 16-digit credit card number: 4454 8178 1029 3161 into a 2 × 8 matrix, listing the digits in pairs, one under the other. Ignore the spaces.</div>',
  [('Write out','4454 8178 1029 3161 (groups of four help you keep track)'),('Pairs','44 · 54 · 81 · 78 · 10 · 29 · 31 · 61: first digit on top, second underneath')],
  mat([[4,5,8,7,1,2,3,6],[4,4,1,8,0,9,1,1]],fs=24),f'{CAM} · Example 8 (pp. 485–486)',video='Cambridge GO · Example 8 (10B Resources)',cmd=('Convert',None,'pairs go down the columns')))
YT=json.load(open(os.path.join(ROOT,'planner','written-youtrys.json'))); YT=YT if isinstance(YT,list) else YT.get('items',list(YT.values()))
YT={y['id']:y for y in YT}
S.append(qslide('yt','You try · written for 12MAG','Entering a credit card number into a matrix',
  '<div style="font-size:28px;margin-top:40px">'+YT['YT-10B-8']['text']+'</div>',
  [('Pairs','52 · 13 · 70 · 46 · 93 · 81 · 27 · 50: first digit on top, second underneath')],
  mat([[5,1,7,4,9,8,2,5],[2,3,0,6,3,1,7,0]],fs=24),'Written for 12MAG (modelled on Cambridge Example 8; no Edrolo match) · planner/written-youtrys.json YT-10B-8',cmd=('Convert',None,'pairs go down the columns')))
# ================= Ex 9 / YT U1&2 5D WE3a
S.append(qslide('we','Worked example 9 · 10B','Representing a network diagram by a matrix',
  ('<div style="font-size:23px">Represent the network diagram shown opposite as a 4 × 4 matrix <i>M</i>, where the:<ul class="bul" style="margin-left:24px"><li>matrix element = 1 if the two points are joined by a line</li><li>matrix element = 0 if the two points are not connected.</li></ul></div>',
   IMG('ex9_net.png',230),''),
  [('Blank','4 × 4 matrix, rows and columns labelled A, B, C, D'),('Row A','<i>m</i><sub>11</sub> = 0 (no loop) · <i>m</i><sub>12</sub> = 1 (A–B) · <i>m</i><sub>13</sub> = 0 · <i>m</i><sub>14</sub> = 1 (A–D)'),
   ('Rows B–D','and so on until the matrix is complete'),('Check','no loops → leading diagonal all 0')],
  '<i>M</i> = '+mat([[0,1,0,1],[1,0,1,1],[0,1,0,0],[1,1,0,0]],fs=20,rl='ABCD',cl='ABCD'),f'{CAM} · Example 9 (p. 486)',video='Cambridge GO · Example 9 (10B Resources)',cmd=('Represent',None,'row by row: 1 = joined')))
S.append(qslide('yt','You try · Edrolo U1&amp;2 5D WE3a','Representing a network by a matrix',
  '<div style="font-size:23px;margin-top:10px">Lucas (L), Mayoi (M), Omar (O) and Seb (S) are pen pals and are trying to communicate with one another through letters.<ul class="bul" style="margin-left:24px">'
  '<li>Lucas can send letters directly to Mayoi and Omar.</li><li>Mayoi can send letters directly to Lucas, Omar and Seb.</li><li>Omar can send letters directly to Lucas, Mayoi and Seb.</li><li>Seb can send letters directly to Mayoi and Omar.</li></ul>'
  'a. <b>Construct</b> a communication matrix, <i>C</i>, that represents the direct connections between the four pen pals.</div>',
  [('Set up','four people: a 4 × 4 matrix · rows = from, columns = to'),('Row L','Lucas → Mayoi, Omar: 0 1 1 0'),('Rows M–S','M: 1 0 1 1 · O: 1 1 0 1 · S: 0 1 1 0')],
  '<i>C</i> = '+mat([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]],fs=20,rl='LMOS',cl='LMOS'),f'{EDR12} · 5D Worked example 3a (pp. 281–282)',cmd=('Construct',None,'rows = from, columns = to')))
# ================= Ex 10 / YT-10B-10
M10=[[0,1,0,0],[1,0,2,1],[0,2,0,3],[0,1,3,0]]
S.append(qslide('we','Worked example 10 · 10B','Interpreting a matrix representing a network diagram',
  '<div style="font-size:17px">The diagram opposite shows the roads connecting four towns: town A, town B, town C, and town D. This diagram has been represented by a 4 × 4 matrix, <i>M</i>. The elements show the number of roads between each pair of towns.'
  +C(IMG('ex10_net.png',200),'<i>M</i> = '+mat(M10,fs=18,rl='ABCD',cl='ABCD',tid='e10'),gap=20)
  +plist([('a','In the matrix <i>M</i>, <i>m</i><sub>24</sub> = 1. What does this tell us?'),('b','In the matrix <i>M</i>, <i>m</i><sub>34</sub> = 3. What does this tell us?'),('c','In the matrix <i>M</i>, <i>m</i><sub>41</sub> = 0. What does this tell us?'),
          ('d','What is the sum of the elements in row 3 of matrix <i>M</i> and what does this tell us?'),('e','What is the sum of all the elements of matrix <i>M</i> and what does this tell us?')])+'</div>',
  [('a','row B, column D','data-hi="#e10|c1_3|hy"'),('b','row C, column D','data-hi="#e10|c2_3|hy"'),('c','row D, column A','data-hi="#e10|c3_0|hy"'),
   ('d','0 + 2 + 0 + 3 = 5','data-hi="#e10|'+cells(2,3,0,4)+'|hb"'),('e','1 + 4 + 5 + 4 = 14 (each road counted both ways)','data-hi="#e10|'+cells(0,4,0,4)+'|hg"')],
  '',f'{CAM} · Example 10 (p. 487; network cropped from the book)',video='Cambridge GO · Example 10 (10B Resources)',cmd=('What',None,'row = from town, column = to town'),
  parts=[('a','There is one road between town B and town D.'),('b','There are three roads between town D and town C.'),('c','There is no road between town D and town A.'),
         ('d','5: the total number of roads between town C and the other towns in the network.'),('e','14: the total number of different ways you can travel between towns.')]))
S[-1]=S[-1].replace('<section class="slide T we','<section class="slide T we sm',1)
M10y=[[0,2,1,0],[2,0,0,1],[1,0,0,3],[0,1,3,0]]
S.append(qslide('yt','You try · written for 12MAG','Interpreting a matrix representing a network diagram',
  '<div style="font-size:19px">The roads connecting four towns, town P, town Q, town R and town S, have been represented by a 4 × 4 matrix, <i>M</i>. The elements show the number of roads between each pair of towns.'
  +C('<i>M</i> = '+mat(M10y,fs=20,rl='PQRS',cl='PQRS',tid='y10'))
  +plist([('a','In the matrix <i>M</i>, <i>m</i><sub>14</sub> = 0. What does this tell us?'),('b','In the matrix <i>M</i>, <i>m</i><sub>34</sub> = 3. What does this tell us?'),
          ('c','What is the sum of the elements in row 2 of matrix <i>M</i> and what does this tell us?'),('d','What is the sum of all the elements of matrix <i>M</i> and what does this tell us?')])+'</div>',
  [('a','row P, column S','data-hi="#y10|c0_3|hy"'),('b','row R, column S','data-hi="#y10|c2_3|hy"'),('c','2 + 0 + 0 + 1 = 3','data-hi="#y10|'+cells(1,2,0,4)+'|hb"'),('d','3 + 3 + 4 + 4 = 14','data-hi="#y10|'+cells(0,4,0,4)+'|hg"')],
  '','Written for 12MAG (modelled on Cambridge Example 10; no Edrolo match) · planner/written-youtrys.json YT-10B-10',cmd=('What',None,'row = from town, column = to town'),
  parts=[('a','There is no road between town P and town S.'),('b','There are three roads between town R and town S.'),('c','3: the total number of roads between town Q and the other towns in the network.'),('d','14: the total number of different ways you can travel between towns.')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2018 Exam 2 Q1a–c','Show what you know',
  '<div style="font-size:22px">A toll road is divided into three sections, <i>E</i>, <i>F</i> and <i>G</i>.<br>The cost, in dollars, to drive one journey on each section is shown in matrix <i>C</i> below.'
  +C('<i>C</i> = '+mat([[3.58],[2.22],[2.87]],fs=24,rl='EFG',side=True,tid='x1'))
  +plist([('a','What is the cost of one journey on section <i>G</i>? <span class="muted">(1 mark)</span>'),('b','<b>Write down</b> the order of matrix <i>C</i>. <span class="muted">(1 mark)</span>'),
          ('c','One day Kim travels once on section <i>E</i> and twice on section <i>G</i>. <b>Construct</b> a row matrix that shows this. <span class="muted">(1 mark; adapted by Edrolo: the original asks for <i>M</i> in <i>M</i> × <i>C</i>)</span>')])+'</div>',
  [('a','row G','data-hi="#x1|c2_0|hy"'),('b','3 rows, 1 column'),('c','one row, a column for each section E, F, G: once, none, twice')],
  '','VCAA 2018 Further Mathematics Exam 2 Matrices Q1 (examiner report: a 99%, b 94%, c 66%) · Edrolo U3&amp;4 7A Q12 (part c adapted)',
  stat=('mark',66),cmd=('Construct',3,'row matrix = one row'),
  parts=[('a','<b>$2.87</b>'),('b','<b>3 × 1</b>'),('c',mat([[1,0,2]],fs=20)+' <span class="muted" style="font-size:15px">(not a column matrix)</span>')]))
A17=[[3,4,5],[5,6,7],[7,8,9]]; B17=[[0,-1,-2],[1,0,-1],[2,1,0]]
OPT=[[[5,7,9],[8,10,12],[11,13,15]],[[5,8,11],[7,10,13],[9,12,15]],[[3,6,9],[3,6,9],[3,6,9]],[[3,3,3],[6,6,6],[9,9,9]],[[3,6,3],[6,3,9],[3,9,3]]]
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2017 Exam 1 Q6','Show what you know',
  '<div style="font-size:19px">The table below shows information about two matrices, <i>A</i> and <i>B</i>.'
  '<table class="t tight" style="font-size:18px;margin:6px auto"><tr><th>Matrix</th><th>Order</th><th>Rule</th></tr><tr><td><i>A</i></td><td>3 × 3</td><td><i>a<sub>ij</sub></i> = 2<i>i</i> + <i>j</i></td></tr><tr><td><i>B</i></td><td>3 × 3</td><td><i>b<sub>ij</sub></i> = <i>i</i> – <i>j</i></td></tr></table>'
  'The element in row <i>i</i> and column <i>j</i> of matrix <i>A</i> is <i>a<sub>ij</sub></i>.<br>The element in row <i>i</i> and column <i>j</i> of matrix <i>B</i> is <i>b<sub>ij</sub></i>.<br>The sum <i>A</i> + <i>B</i> is</div>',
  [('A','<i>A</i> = '+mat(A17,fs=16)),('B','<i>B</i> = '+mat(B17,fs=16)),('Add','add matching elements (10C): row 1 = 3 3 3, row 2 = 6 6 6, row 3 = 9 9 9')],
  mat(OPT[3],fs=16)+' : <b>D</b>.','VCAA 2017 Further Mathematics Exam 1 Matrices Q6 (examiner report) · Edrolo U3&amp;4 7B Q15',
  mc=[mat(o,fs=14) for o in OPT],key='D',stat=('mc',58),dist=[6,13,12,58,10],dis=('C','rows and columns swapped: the sum is 3<i>i</i>, so each ROW is constant, not each column.')))
S[-1]=S[-1].replace('<div class="mc"','<div class="mc" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px"',1).replace('<section class="slide T ex','<section class="slide T ex sm',1)

# ================= closing
S.append(checkin(SC_).replace('<section class="slide T "','<section class="slide T ci10"',1)); S[0]+='<style>.ci10 .tick li{font-size:17px!important;margin:1px 0!important;padding-top:2px!important;padding-bottom:2px!important}</style>'
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 10 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('10A','10B') and v.get('url')]))
n=assemble(S,'12MAG · 10A-10B · What is a matrix?',os.path.join(ROOT,'lessons','10A-10B slides.html'))
print(n-1,'slides')
