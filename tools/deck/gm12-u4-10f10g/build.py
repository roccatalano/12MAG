"""Lesson gm12-u4-10f10g (10F Binary, permutation and communication matrices · 10G Dominance matrices) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/10F-10G slides.html      Run: python3 tools/deck/gm12-u4-10f10g/build.py      Screenshots: python3 tools/deck/gm12-u4-10f10g/shoot.py
Matrices drawn with tools/deck/mx.py, networks with tools/deck/tpl/net.py (redrawn with the same vertices/edges as the source).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- CFAT 3.10.2 (10D-10E) first (planner card).
- Do Now: VCAA 2025 Exam 1 Q27 (C, 76%) · VCAA 2024 Exam 1 Q13 (plot cropped from the paper; A, 72%) ·
          VCAA 2025 NHT Exam 2 Q11 stem + Q11b (m = 22.3, n = 220; NHT: no %) · VCAA 2023 Exam 2 Q1 stem (Table 1) + Q1bi (11.42 g; average 0.9/1 = 90%).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4F #14 and #15 (p. 292; solutions worked for 12MAG) ·
       VCAA 2019 Exam 1 Matrices Q7 as adapted in Edrolo U1&2 5D Q14 (p. 286; D; 54% as quoted by Edrolo).
- Learn: Cambridge U3&4 10F pp. 523-529, 10G pp. 531-533 (own words) · Edrolo U3&4 7E pp. 460-463, 7F pp. 469-473.
- Worked examples: Cambridge U3&4 Examples 28-32 (pp. 523-533).
  You trys: Edrolo U3&4 7E WE1 (p. 461-462), 7E WE3 (pp. 463-464), YT-10F-30 (written, planner/written-youtrys.json),
            Edrolo U3&4 7F WE1 (pp. 470-471; part b = the card's CAS You try 7F WE1b), 7F WE2 (pp. 473-474).
- CAS: Cambridge 10F communication matrix C, C² and T = C + C² (pp. 526-527); steps from planner/cas-skills.json 'matrix-operations'.
- Exit 1: VCAA 2018 Exam 1 Matrices Q4 (= Edrolo U3&4 7E Q9), B, 69%.   Exit 2: VCAA 2020 Exam 1 Matrices Q3 (= 7E Q10), D, 64%.
- Exit 3: VCAA 2017 Exam 1 Matrices Q5 (= 7F Q12), A, 74%.   Exit 4: VCAA 2021 Exam 2 Matrices Q2 (= 7F Q13), a 92%, b 83%, c 21%.
  (% as quoted by Edrolo from the examiner reports.)
"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat, cells
from net import net
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-10f10g')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def Wd(w,x): return f'<div style="width:{w}px;margin:4px auto">{x}</div>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def lab(t,s='font-size:15px'): return f'<span style="{s};font-style:italic;opacity:.8">{t}</span>'
def AR(a,b,**o): d={'arrow':True}; d.update(o); return (a,b,d)

# ---- networks (same vertices/edges as the sources)
G31=net({'E':(110,10,'e'),'W':(110,70,'e'),'Y':(30,150,'w'),'K':(190,150,'e')},[AR('W','E'),AR('E','W'),AR('W','Y'),AR('Y','W'),AR('W','K'),AR('K','W')],W=220,H=160,pad=14)
G32=net({'A':(20,70,'w'),'B':(150,10,'n'),'C':(270,55,'e'),'D':(230,120,'s')},[AR('A','B'),AR('A','D'),AR('B','C'),AR('D','C'),AR('D','B')],W=290,H=130,pad=16)
GLH=net({'B':(20,35,'w'),'D':(150,15,'n'),'C':(200,85,'s'),'A':(35,110,'s')},[('B','D'),('D','C'),('B','A'),('B','C')],W=220,H=120,pad=16)
GJ=net({'Bruin':(140,15,'n'),'Claude':(250,45,'e'),'Abe':(30,70,'w'),'Dan':(230,140,'e'),'Eugene':(110,160,'s')},
       [AR('Abe','Bruin'),AR('Abe','Claude'),AR('Abe','Dan'),AR('Bruin','Eugene'),AR('Claude','Bruin'),AR('Dan','Bruin'),AR('Dan','Claude'),AR('Eugene','Abe'),AR('Eugene','Claude'),AR('Eugene','Dan')],W=280,H=175,pad=22,fs=16)
GRD=net({'A':(20,20,'w'),'B':(210,15,'n'),'C':(190,150,'w'),'D':(20,150,'s')},[('A','B'),('A','D'),('D','B',{'bend':40}),('B','C',{'bend':-25})],W=230,H=165,pad=16)
GABC=net({'A':(20,110,'w'),'B':(160,110,'e'),'C':(90,15,'n')},[('A','B'),('B','C'),('A','C')],W=180,H=125,pad=16)

S=['<style>.sm .L .q{font-size:17px}.x4 .L .parts li,.x4 .L .parts li span,.x4 .L .parts li b{font-size:15px!important;line-height:1.3!important}.tight td,.tight th{padding:2px 8px!important;text-align:center;white-space:nowrap}</style>']
# ================= opening
t=title('10F-10G','Binary, permutation, communication and dominance matrices',f'{CAM} · 10F Binary, permutation and communication matrices · 10G Dominance matrices','10F-10G',
        flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks'))
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 3.10.2','· 10D–10E · 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills + one VCAA question','var(--apk)'),
  ('Permutation matrices · Examples 28–29','→ You try',None),('Inverse of a permutation matrix · Example 30','→ You try',None),
  ('Communication matrices · Example 31','→ You try',None),('CAS: C + C²','',None),('Dominance matrices · Example 32','→ You try',None),
  ('Exit tasks','· four VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Binary matrix','every element is 0 or 1',mat([[1,0,1]],fs=15)),
  ('Permutation matrix','square binary matrix with exactly one 1 in each row and column',mat([[0,1],[1,0]],fs=15)),
  ('Communication matrix','1 = a direct (one-step) link from the row to the column'),
  ('Redundant link','a link that starts and ends with the same person (leading diagonal)'),
  ('Dominance matrix','1 = row player beat (dominates) the column player')],
  [('Rearrange rows',F('<i>PX</i>'),'pre-multiply'),
   ('Rearrange columns',F('<i>XP</i>'),'post-multiply'),
   ('Undo a permutation',F('<i>P</i><sup>−1</sup> = <i>P</i><sup>T</sup>'),''),
   ('One- and two-step',F('<i>T</i> = <i>C</i> + <i>C</i><sup>2</sup>'),'D + D² for dominance: rank by row sums')],
  f'{CAM}, 10F pp. 523–529, 10G pp. 531–533; Study Design: binary, permutation, communication and dominance matrices'))
S.append(cfat('CFAT 3.10.2','Matrix products, powers, determinants and inverses','10D–10E',15,'CFAT 3.10.2 (10D–10E) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q27','Review of 10E (last lesson)',
  '<div style="font-size:26px;margin-top:30px">Consider the matrix <i>E</i> where'+C(EQ('<i>E</i> =',mat([['m',-9],[4,'n']],fs=26)))
  +'For the inverse of <i>E</i> to exist, the values of <i>m</i> and <i>n</i>, respectively, <b>cannot</b> be</div>',
  [('No inverse','det(<i>E</i>) = 0'),('Determinant','<i>mn</i> − (−9)(4) = <i>mn</i> + 36 = 0, so <i>mn</i> = −36'),('Check','3 × (−12) = −36')],
  '3 and −12: <b>C</b>.','VCAA 2025 General Mathematics Exam 1 Q27 (examiner report: 76% correct)',
  mc=['3 and 12','12 and 3','3 and −12','−3 and −12'],key='C',dis=('A','forgot the minus: mn = 36'),stat=('mc',76)))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q13','Review of 5C (last term)',
  ('<div style="font-size:19px">A school runs an orientation program for new staff each January.<br>The time series plot below shows the number of new staff, <em class="v">new</em>, for each year, <em class="v">year</em>, from 2011 to 2022 (inclusive).</div>',
   IMG('dn2_ts.png',480),
   '<div style="font-size:19px">The time series is smoothed using seven-median smoothing.<br>The smoothed value of <em class="v">new</em> for the <em class="v">year</em> 2016 is</div>'),
  [('Window','seven points centred on 2016: 2013 to 2019'),('Values','7, 6, 11, 13, 12, 6, 10'),('Order','6, 6, 7, <b>10</b>, 11, 12, 13: middle (4th) value')],
  '10: <b>A</b>.','VCAA 2024 General Mathematics Exam 1 Q13 (examiner report: 72% correct)',
  mc=['10','11','12','13'],key='A',stat=('mc',72)))
sm()
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 NHT Exam 2 Q11b','Review of 10E (last lesson)',
  '<div style="font-size:21px">At Melbourne Airport, the three friends want to exchange their Australian currency (Australian dollars) for Thai currency (Thai baht).<br>'
  'b. The following table shows how many Australian dollars each of the three friends exchanged for Thai baht.'
  '<table class="t tight" style="font-size:19px;margin:8px auto"><tr><th></th><th>Australian dollars</th><th>Thai baht</th></tr><tr><th>Teena</th><td>100</td><td>2230</td></tr><tr><th>Alison</th><td>350</td><td>7805</td></tr><tr><th>Sally</th><td><i>n</i></td><td>4906</td></tr></table>'
  'The exchange in currency can be represented by the following matrix equation:'+C(EQ('<i>m</i> ×',mat([[100],[350],['n']],fs=21),'=',mat([[2230],[7805],[4906]],fs=21)))
  +'<b>Determine</b> the values of <i>m</i> and <i>n</i>. <span class="muted">(1 mark)</span></div>',
  [('m','row 1: <i>m</i> × 100 = 2230 → <i>m</i> = 22.3 (baht per dollar)'),('n','row 3: 22.3 × <i>n</i> = 4906 → <i>n</i> = 4906 ÷ 22.3')],
  '<i>m</i> = <b>22.3</b>, <i>n</i> = <b>220</b>','VCAA 2025 NHT General Mathematics Exam 2 Q11 stem and Q11b (NHT examiner report gives no %)',
  cmd=('Determine',None,'scalar × matrix: row by row')))
sm()
OY=[(1,12.9,13.0,5.1,'large'),(2,11.4,11.7,4.8,'medium'),(3,17.4,17.4,6.5,'large'),(4,6.8,7.2,2.9,'small'),(5,9.6,10.1,3.7,'medium'),(6,15.5,15.6,5.7,'large'),(7,9.7,9.9,4.0,'small'),(8,7.0,7.5,2.7,'small'),
    (9,12.6,12.7,5.5,'medium'),(10,12.5,12.7,5.0,'medium'),(11,10.1,10.5,3.9,'medium'),(12,10.6,10.8,4.1,'medium'),(13,13.0,13.1,5.3,'large'),(14,8.1,8.5,3.5,'small'),(15,14.1,14.2,5.3,'large')]
TB=('<table class="t tight" style="font-size:12.5px;margin:4px auto"><tr><th><i>ID</i></th><th><i>Weight</i> (g)</th><th><i>Volume</i> (cm<sup>3</sup>)</th><th><i>Image size</i> (megapixels)</th><th><i>Size</i></th></tr>'
    +''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a,b,c,d,e in OY)+'</table>')
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q1bi','Review of 1F (last term)',
  '<div style="font-size:16px">Data was collected to investigate the use of electronic images to automate the sizing of oysters for sale.<br>The variables in this study were: <i>ID</i> · <i>weight</i> (g) · <i>volume</i> (cm<sup>3</sup>) · <i>image size</i> (megapixels) · <i>size</i>: small, medium or large.<br>'
  'The data collected for a sample of 15 oysters is displayed in Table 1.'+TB
  +'b. <b>Determine</b>, in grams:<br>i. the mean <em class="v">weight</em> of all the oysters in this sample <span class="muted">(1 mark)</span></div>',
  [('CAS','one-variable statistics on the 15 weights (don’t add by hand)'),('Read off','x̄ = 171.3 ÷ 15 = 11.42')],
  'mean = <b>11.42</b> g','VCAA 2023 General Mathematics Exam 2 Q1 stem (variables shortened to one line) and Q1bi (examiner report: average 0.9/1)',
  stat=('mark',90),cmd=('Determine',None,'CAS one-variable stats')))
sm()

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4F #14','Representing a road network in a matrix',
  '<div style="font-size:28px;margin-top:20px">Use a matrix to record the number of ways of travelling directly from one town to another.</div>'+Wd(330,GRD),
  [('Set up','4 towns → 4 × 4 matrix, rows and columns A, B, C, D'),('Count roads','A: to B, D · B: to A, C, D · C: to B · D: to A, B'),('Symmetric','each road goes both ways')],
  mat([[0,1,0,1],[1,0,1,1],[0,1,0,0],[1,1,0,0]],rl=list('ABCD'),cl=list('ABCD'),fs=20),f'{CAM12} · Ch 4 review skills checklist 4F #14 (p. 292) · solution worked for 12MAG',cmd=('Use',None,'one row per town')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4F #15','Summarising a network in a matrix',
  '<div style="font-size:28px;margin-top:20px">Draw a network to show the direct connections between towns <i>A</i>, <i>B</i> and <i>C</i> given in the matrix below.'
  +C(mat([[0,1,1],[1,0,1],[1,1,0]],rl=list('ABC'),cl=list('ABC'),side=True,fs=26))+'</div>',
  [('Vertices','one dot per town: A, B, C'),('Edges','each 1 = a direct connection: A–B, A–C, B–C')],
  Wd(220,GABC),f'{CAM12} · Ch 4 review skills checklist 4F #15 (p. 292) · solution worked for 12MAG',cmd=('Draw',None,'1 = an edge')))
JM=[[0,0,1,0,1,1],[1,0,0,0,1,0],[0,1,0,1,1,1],[1,0,1,0,1,0],[0,0,0,1,0,1],[1,1,0,1,0,0]]
S.append(qslide('apk','APK · VCAA 2019 Exam 1 Q7 (adapted)','Two-step links (Year 11)',
  '<div style="font-size:19px">Matrix <i>J</i> is a communication matrix showing the direct paths by which messages can be sent between two people in a group of six people, U to Z.'
  +C(EQ('<i>J</i> =',mat(JM,rl=list('UVWXYZ'),cl=list('UVWXYZ'),side=True,fs=19,tid='ak3')),lab('sender (rows) · receiver (columns)'))
  +'A ‘1’ in the matrix shows that the person named in that row can send a message directly to the person named in that column.<br>For example, the ‘1’ in row 4, column 3 shows that X can send a message directly to W.<br>'
  'In how many ways can W get a message to U by sending it directly to one other person?</div>',
  [('W sends to','row W: V, X, Y, Z','data-hi="#ak3|c2_1,c2_3,c2_4,c2_5|hy"'),('Who sends to U?','column U: V, X, Z','data-hi="#ak3|c1_0,c3_0,c5_0|hb"'),('Two-step links','W → V → U, W → X → U, W → Z → U')],
  '3 ways: <b>D</b>.',f'VCAA 2019 Further Mathematics Exam 1 Matrices Q7, adapted by Edrolo (54% correct, quoted by Edrolo) · {EDR12} 5D Q14 (p. 286)',
  mc=['0','1','2','3','4'],key='D',stat=('mc',54)))
sm()

# ================= Learn 1: binary + permutation
S.append(learn('Learn · 10F','Binary and permutation matrices',
  '<h4>A permutation matrix rearranges another matrix</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>binary</b> matrix: only 0s and 1s</li><li><b>permutation</b> matrix: square, binary, exactly one 1 in every row and every column</li>'
  '<li><i>PX</i> (P in front) rearranges the <b>rows</b> of <i>X</i>; <i>XP</i> rearranges the <b>columns</b></li>'
  '<li>a 1 in row <i>i</i>, column <i>j</i> of <i>P</i>: row <i>j</i> of <i>X</i> moves to row <i>i</i></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:18px;align-items:center;font-size:24px">'
  '<div class="frag">'+EQ(mat([[0,0,1],[0,1,0],[1,0,0]],fs=22),mat([['T'],['A'],['R']],fs=22),'=',mat([['R'],['A'],['T']],fs=22))+'</div>'
  '<div class="frag">row 1 of <i>P</i> has its 1 in column 3 → <i>R</i> goes first</div></div>',
  'An identity matrix is a permutation matrix that changes nothing.',f'{CAM}, 10F pp. 523–524 (own words) · {EDR}, 7E pp. 460–461',
  cards=(kcard('Rows',F('<i>PX</i>: pre-multiply')),kcard('Columns',F('<i>XP</i>: post-multiply')))))
# ================= Ex 28 / YT 7E WE1
S.append(qslide('we','Worked example 28 · 10F','Applying a permutation matrix',
  '<div style="font-size:26px;margin-top:20px"><i>X</i> is the column matrix '+EQ('<i>X</i> =',mat([['T'],['A'],['R']],fs=24))+'. <i>P</i> is the permutation matrix '+EQ('<i>P</i> =',mat([[0,0,1],[0,1,0],[1,0,0]],fs=24))+'.'
  +plist([('a','Show that:<br>i pre-multiplying <i>X</i> by <i>P</i> changes the matrix <i>X</i> to the matrix <i>Y</i> = '+mat([['R'],['A'],['T']],fs=20)+'<br>ii pre-multiplying <i>X</i> by <i>P</i><sup>2</sup> leaves the matrix <i>X</i> unchanged.'),
          ('b','What can be deduced about <i>P</i><sup>2</sup> from the result in a ii?')])+'</div>',
  [('a i','first entry: 0 × <i>T</i> + 0 × <i>A</i> + 1 × <i>R</i> = <i>R</i>, and so on'),('a ii',EQ('<i>P</i><sup>2</sup><i>X</i> =',mat([[0,0,1],[0,1,0],[1,0,0]],fs=15,sup='2'),mat([['T'],['A'],['R']],fs=15),'=',mat([['T'],['A'],['R']],fs=15))),('b','leaving <i>X</i> unchanged means <i>P</i><sup>2</sup> acts like <i>I</i>')],
  '',f'{CAM} · Example 28 (pp. 523–524)',video='Cambridge GO · Example 28 (10F Resources)',cmd=('Show',None,'multiply it out'),
  parts=[('a i','<i>PX</i> = '+mat([['R'],['A'],['T']],fs=16)+' = <i>Y</i>'),('a ii','<i>P</i><sup>2</sup><i>X</i> = '+mat([['T'],['A'],['R']],fs=16)+' = <i>X</i>'),('b','<i>P</i><sup>2</sup> is the identity matrix <i>I</i>.')]))
sm()
S.append(qslide('yt','You try · Edrolo 7E WE1','Performing a column permutation',
  '<div style="font-size:30px;margin-top:40px">Perform a column permutation of matrix <i>X</i> by using permutation matrix <i>P</i>.'
  +C(EQ('<i>X</i> =',mat([['u','m','l','p']],fs=28)),EQ('<i>P</i> =',mat([[0,0,1,0],[0,0,0,1],[0,1,0,0],[1,0,0,0]],fs=28,tid='y28')))+'</div>',
  [('Columns','column permutation → post-multiply: <i>XP</i>'),('Read P','<i>p</i><sub>13</sub>: column 1 → column 3 · <i>p</i><sub>24</sub>: 2 → 4 · <i>p</i><sub>32</sub>: 3 → 2 · <i>p</i><sub>41</sub>: 4 → 1','data-hi="#y28|c0_2,c1_3,c2_1,c3_0|hy"')],
  '<i>XP</i> = '+mat([['p','l','u','m']],fs=22),f'{EDR} · 7E Worked example 1 (pp. 461–462)',cmd=('Perform',None,'columns → XP')))
S.append(qslide('we','Worked example 29 · 10F','Finding a permutation matrix',
  '<div style="font-size:30px;margin-top:40px">Find a permutation matrix that takes the column matrix '+mat([['A'],['B'],['C'],['D']],fs=26)+' to the column matrix '+mat([['D'],['C'],['B'],['A']],fs=26)+'</div>',
  [('Row 1','move D from 4th to 1st: 1 in column 4 of row 1'),('Row 2','C from 3rd to 2nd: 1 in column 3 of row 2'),('Row 3','B from 2nd to 3rd: 1 in column 2 of row 3'),('Row 4','A from 1st to 4th: 1 in column 1 of row 4')],
  EQ(mat([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]],fs=20),mat([['A'],['B'],['C'],['D']],fs=20),'=',mat([['D'],['C'],['B'],['A']],fs=20)),f'{CAM} · Example 29 (p. 524)',video='Cambridge GO · Example 29 (10F Resources)',cmd=('Find',None,'new row i ← old row j: 1 at (i, j)')))
S.append(qslide('yt','You try · Edrolo 7E WE3','Constructing a permutation matrix',
  '<div style="font-size:30px;margin-top:40px">Determine the permutation matrix <i>P</i> that would be required to change'
  +C(mat([[21,17,42],[31,22,27],[46,33,15]],fs=28),'to',mat([[31,22,27],[21,17,42],[46,33,15]],fs=28))+'</div>',
  [('Type','rows stay intact and move up or down → row permutation, 3 × 3'),('Rows','row 1 → row 2: <i>p</i><sub>21</sub> · row 2 → row 1: <i>p</i><sub>12</sub> · row 3 stays: <i>p</i><sub>33</sub>')],
  '<i>P</i> = '+mat([[0,1,0],[1,0,0],[0,0,1]],fs=22),f'{EDR} · 7E Worked example 3 (pp. 463–464)',cmd=('Determine',None,'one 1 per row and column')))

# ================= Learn 2: inverse of a permutation matrix
S.append(learn('Learn · 10F','Inverse of a permutation matrix',
  '<h4>Undo a permutation with the transpose</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>every permutation matrix has an inverse</li><li><i>P</i><sup>−1</sup> = <i>P</i><sup>T</sup>: swap rows and columns</li>'
  '<li>if <i>PA</i> = <i>B</i> then <i>A</i> = <i>P</i><sup>−1</sup><i>B</i> = <i>P</i><sup>T</sup><i>B</i></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:18px;align-items:center;font-size:24px">'
  '<div class="frag">'+EQ('<i>P</i> =',mat([[0,1,0],[0,0,1],[1,0,0]],fs=22))+'</div><div class="frag">'+EQ('<i>P</i><sup>T</sup> =',mat([[0,0,1],[1,0,0],[0,1,0]],fs=22))+'</div>'
  '<div class="frag"><i>PP</i><sup>T</sup> = <i>I</i> ✓</div></div>',
  'Transpose: row 1 becomes column 1.',f'{CAM}, 10F p. 525 (own words) · {EDR}, 7E p. 462',
  cards=(kcard('Inverse',F('<i>P</i><sup>−1</sup> = <i>P</i><sup>T</sup>')),kcard('Undo',F('<i>A</i> = <i>P</i><sup>T</sup><i>B</i>')))))
P30=[[0,0,1,0],[0,0,0,1],[0,1,0,0],[1,0,0,0]]
S.append(qslide('we','Worked example 30 · 10F','The inverse of a permutation matrix',
  '<div style="font-size:28px;margin-top:30px">A 4 × 4 permutation matrix '+EQ('<i>P</i> =',mat(P30,fs=24))+' applied to a 4 × 1 column matrix <i>A</i> gives the column matrix '+mat([['X'],['Y'],['Z'],['W']],fs=24)+'. Determine the matrix <i>A</i>.</div>',
  [('Equation',EQ('<i>PA</i> =',mat([['X'],['Y'],['Z'],['W']],fs=15))),('Undo',EQ('<i>A</i> = <i>P</i><sup>−1</sup>',mat([['X'],['Y'],['Z'],['W']],fs=15),'= <i>P</i><sup>T</sup>',mat([['X'],['Y'],['Z'],['W']],fs=15))),('CAS','transpose of <i>P</i> × the column matrix')],
  '<i>A</i> = '+mat([['W'],['Z'],['X'],['Y']],fs=20),f'{CAM} · Example 30 (p. 525)',video='Cambridge GO · Example 30 (10F Resources)',cmd=('Determine',None,'A = Pᵀ × result')))
S.append(qslide('yt','You try · written for 12MAG','The inverse of a permutation matrix',
  '<div style="font-size:28px;margin-top:30px">A 4 × 4 permutation matrix '+EQ('<i>P</i> =',mat([[0,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,0]],fs=24))+' applied to a 4 × 1 column matrix <i>A</i> gives the column matrix '+mat([['K'],['L'],['M'],['N']],fs=24)+'. Determine the matrix <i>A</i>.</div>',
  [('Equation',EQ('<i>PA</i> =',mat([['K'],['L'],['M'],['N']],fs=15))),('Undo',EQ('<i>A</i> = <i>P</i><sup>T</sup>',mat([['K'],['L'],['M'],['N']],fs=15),', <i>P</i><sup>T</sup> =',mat([[0,0,1,0],[1,0,0,0],[0,0,0,1],[0,1,0,0]],fs=14)))],
  '<i>A</i> = '+mat([['M'],['K'],['N'],['L']],fs=20),'Written for 12MAG (modelled on Cambridge Example 30; no Edrolo match) · planner/written-youtrys.json YT-10F-30',cmd=('Determine',None,'A = Pᵀ × result')))

# ================= Learn 3: communication
S.append(learn('Learn · 10F','Communication matrices',
  '<h4>Rows send, columns receive</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>communication matrix</b> <i>C</i>: 1 = a one-step (direct) link from row to column</li>'
  '<li><i>C</i><sup>2</sup> counts the <b>two-step</b> links (through one other person)</li>'
  '<li>non-zero elements on the leading diagonal = <b>redundant</b> links (back to yourself)</li>'
  '<li><i>T</i> = <i>C</i> + <i>C</i><sup>2</sup>: all one- and two-step links</li></ul>',
  '<div style="display:flex;gap:16px;align-items:center;font-size:22px"><div class="frag">'+Wd(200,G31)+'</div>'
  '<div class="frag">'+mat([[0,1,0,0],[1,0,1,1],[0,1,0,0],[0,1,0,0]],rl=list('EWYK'),cl=list('EWYK'),side=True,fs=20)+'</div></div>',
  'Eva → Wong → Yumi is a two-step link.',f'{CAM}, 10F pp. 525–528 (own words) · {EDR}, 7F pp. 469–470',
  cards=(kcard('Two-step',F('<i>C</i><sup>2</sup>')),kcard('Total',F('<i>T</i> = <i>C</i> + <i>C</i><sup>2</sup>')))))
S.append(qslide('we','Worked example 31 · 10F','Constructing a communication matrix',
  ('<div style="font-size:18px">Eva, Wong, Yumi and Kim are students who are staying in a backpacker’s hostel. Because they speak different languages they can have problems communicating. The situation they have to deal with is that:'
   '<ul style="margin:4px 0 4px 22px"><li>Eva speaks English only</li><li>Yumi speaks Japanese only</li><li>Kim speaks Korean only</li><li>Wong speaks English, Japanese and Korean.</li></ul>'
   'Conveniently, this information can be summarised in a network diagram, as shown below. In this diagram, the arrow linking Eva and Wong indicates that they can communicate directly because they both speak English.</div>',
   Wd(200,G31),'<div style="font-size:18px">The task is to construct a communication matrix.</div>'),
  [('Size','four people → 4 × 4, rows and columns <i>E</i>, <i>W</i>, <i>Y</i>, <i>K</i>'),('Labels','rows ‘Speaker’, columns ‘Receiver’'),('Fill','1 if they share a language, 0 if not')],
  mat([[0,1,0,0],[1,0,1,1],[0,1,0,0],[0,1,0,0]],rl=list('EWYK'),cl=list('EWYK'),fs=20)+lab(' Speaker (rows) · Receiver (columns)'),f'{CAM} · Example 31 (p. 526)',video='Cambridge GO · Example 31 (10F Resources)',cmd=('construct',None,'rows send, columns receive')))
sm()
S.append(qslide('yt','You try · Edrolo 7F WE1','Communication links',
  '<div style="font-size:21px">The following network diagram shows communication lines between four lighthouses, A, B, C and D.'+Wd(260,GLH)
  +plist([('a','Construct an undirected communication matrix, <i>C</i>, that indicates all one-step communication links between the lighthouses.'),
          ('b','Construct a communication matrix, <i>T</i>, that indicates all one-step and two-step communication links between the lighthouses.'),
          ('c','Using matrix <i>T</i> from part b, in how many ways can lighthouse B communicate with lighthouse D?'),
          ('d','Using matrix <i>T</i> from part b, how many redundant communication links are there?')])+'</div>',
  [('a','4 × 4, A to D; a 1 for each line (two-way)'),('b','CAS: <i>T</i> = <i>C</i> + <i>C</i><sup>2</sup>'),('c','element <i>t</i><sub>24</sub> (or <i>t</i><sub>42</sub>)'),('d','sum the leading diagonal: 1 + 3 + 2 + 2')],
  '',f'{EDR} · 7F Worked example 1 (pp. 470–471)',
  parts=[('a','<i>C</i> = '+mat([[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]],fs=14)),('b','<i>T</i> = '+mat([[1,1,1,1],[1,3,2,2],[1,2,2,2],[1,2,2,2]],fs=14)),('c','2'),('d','8')]))
sm()

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['matrix-operations']
CE=[[0,1,0,0],[1,0,1,1],[0,1,0,0],[0,1,0,0]]
S.append(cas('CAS · 10F','Two-step links: C² and T = C + C²',
  '<div style="font-size:22px">Store the hostel communication matrix as <i>c</i>:</div>'+C(EQ('<i>C</i> =',mat(CE,fs=22)))+'<div style="font-size:22px">then type <b>c^2</b> and <b>c + c^2</b>.</div>'
  '<p class="muted" style="font-size:17px">'+CS['tip']+'</p>',
  CS['ti'],CS['classpad'],'<i>C</i><sup>2</sup> = '+mat([[1,0,1,1],[0,3,0,0],[1,0,1,1],[1,0,1,1]],fs=13)+' · <i>T</i> = '+mat([[1,1,1,1],[1,3,1,1],[1,1,1,1],[1,1,1,1]],fs=13),
  f'{CAM} · 10F pp. 526–527 · Steps: CAS guide (planner)'))

# ================= Learn 4: dominance
S.append(learn('Learn · 10G','Dominance matrices',
  '<h4>Who is the strongest? Add up the rows</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>dominance matrix</b> <i>D</i>: 1 = the row player beat (dominates) the column player</li>'
  '<li>row sums of <i>D</i> = one-step dominance scores</li>'
  '<li><i>D</i><sup>2</sup> = two-step dominances (beat someone who beat them)</li>'
  '<li>ties? rank by the row sums of <i>T</i> = <i>D</i> + <i>D</i><sup>2</sup></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:14px;align-items:center;font-size:20px">'
  '<div class="frag">Birgit beat Cas, Cas beat Di</div><div class="frag">→ Birgit has a <b>two-step</b> dominance over Di</div></div>',
  'In a round-robin tournament everyone plays everyone once.',f'{CAM}, 10G pp. 531–532 (own words) · {EDR}, 7F pp. 472–473',
  cards=(kcard('One-step',F('row sums of <i>D</i>')),kcard('Total',F('<i>T</i> = <i>D</i> + <i>D</i><sup>2</sup>')))))
S.append(qslide('we','Worked example 32 · 10G','Determining dominance',
  '<div style="font-size:19px">Four people, <i>A</i>, <i>B</i>, <i>C</i> and <i>D</i>, have been asked to form a committee to decide on the location of a new toxic waste dump.'+Wd(300,G32)
  +'From previous experience, it is known that:<ul style="margin:4px 0 4px 22px"><li><i>A</i> influences the decisions of <i>B</i> and <i>D</i></li><li><i>B</i> influences the decisions of <i>C</i></li><li><i>C</i> influences the decisions of no one</li><li><i>D</i> influences the decisions of <i>C</i> and <i>B</i>.</li></ul>'
  +plist([('a','Use the graph to construct a dominance matrix that takes into account both one-step and two-step dominances.'),('b','From this matrix, determine who is the most influential person on the committee.')])+'</div>',
  [('One-step','<i>D</i> = '+mat([[0,1,0,1],[0,0,1,0],[0,0,0,0],[0,1,1,0]],rl=list('ABCD'),cl=list('ABCD'),fs=13)+' row sums 2, 1, 0, 2'),
   ('Two-step','<i>D</i><sup>2</sup> = '+mat([[0,1,2,0],[0,0,0,0],[0,0,0,0],[0,0,1,0]],fs=13)+' row sums 3, 0, 0, 1'),
   ('Sum','<i>T</i> = <i>D</i> + <i>D</i><sup>2</sup>')],
  '',f'{CAM} · Example 32 (p. 533)',video='Cambridge GO · Example 32 (10G Resources)',cmd=('construct',None,'T = D + D²'),
  parts=[('a','<i>T</i> = '+mat([[0,2,2,1],[0,0,1,0],[0,0,0,0],[0,1,2,0]],rl=list('ABCD'),cl=list('ABCD'),fs=14)+' totals 5, 1, 0, 3'),('b','Person <i>A</i> is the most influential person with a total dominance score of 5.')]))
sm()
S.append(qslide('yt','You try · Edrolo 7F WE2','Ranking with a dominance matrix',
  '<div style="font-size:21px">Five players participated in a round-robin jousting tournament. The results are shown in the following network. An arrow from Abe to Bruin indicates that Abe defeated Bruin.'+Wd(330,GJ)
  +plist([('a','Construct a dominance matrix, <i>D</i>, that indicates all one-step dominances.'),('b','Rank the players from most to least dominant.')])+'</div>',
  [('a','5 × 5, rows = winner, columns = loser; Abe beat Bruin, Claude, Dan …'),('b D²','CAS: <i>D</i><sup>2</sup>, then <i>T</i> = <i>D</i> + <i>D</i><sup>2</sup>'),('b totals','row sums of <i>T</i>: A 7, B 4, C 2, D 4, E 9')],
  '',f'{EDR} · 7F Worked example 2 (pp. 473–474)',
  parts=[('a','<i>D</i> = '+mat([[0,1,1,1,0],[0,0,0,0,1],[0,1,0,0,0],[0,1,1,0,0],[1,0,1,1,0]],rl=list('ABCDE'),cl=list('ABCDE'),fs=13)),('b','Eugene, Abe, Bruin/Dan (tied), Claude')]))
sm()

# ================= Exits
OPT=[[[0,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[[0,0,1,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]],[[1,0,0,0],[0,0,0,0],[1,0,0,0],[0,0,0,0]],[[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]],[[1,0,0,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]]]
S.append(qslide('ex','Exit task 1 of 4 · VCAA 2018 Exam 1 Q4','Show what you know',
  '<div style="font-size:24px;margin-top:20px">Matrix <i>P</i> is a 4 × 4 permutation matrix.<br>Matrix <i>W</i> is another matrix such that the matrix product <i>P</i> × <i>W</i> is defined.<br>This matrix product results in the entire first and third rows of matrix <i>W</i> being swapped.<br>The permutation matrix <i>P</i> is</div>',
  [('Rows','new row 1 = old row 3: 1 at (1, 3) · new row 3 = old row 1: 1 at (3, 1)'),('Others','rows 2 and 4 stay: 1s at (2, 2) and (4, 4)')],
  mat(OPT[1],fs=16)+': <b>B</b>.','VCAA 2018 Further Mathematics Exam 1 Matrices Q4 (69% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7E Q9',
  mc=[mat(o,fs=14) for o in OPT],key='B',dis=('E','two 1s in column 1: not a permutation matrix'),stat=('mc',69)))
S[-1]=S[-1].replace('<div class="mc"','<div class="mc" style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px"',1)
S.append(qslide('ex','Exit task 2 of 4 · VCAA 2020 Exam 1 Q3','Show what you know',
  '<div style="font-size:24px;margin-top:20px">Matrices <i>P</i> and <i>W</i> are defined as shown.'+C(EQ('<i>P</i> =',mat([[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,0],[0,0,0,1,0],[1,0,0,0,0]],fs=22)),EQ('<i>W</i> =',mat([['A'],['S'],['T'],['O'],['R']],fs=22)))
  +'If <i>P</i><sup><i>n</i></sup> × <i>W</i> = '+mat([['A'],['S'],['T'],['O'],['R']],fs=20)+', the value of <i>n</i> could be</div>',
  [('Once','<i>PW</i>: row by row picks T, R, S, O, A'),('Repeat','P²W: S, A, R, O, T · P³W: R, T, A, O, S · P⁴W: A, S, T, O, R ✓')],
  '<i>n</i> = 4: <b>D</b>.','VCAA 2020 Further Mathematics Exam 1 Matrices Q3 (64% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7E Q10',
  mc=['1','2','3','4','5'],key='D',stat=('mc',64)))
S.append(qslide('ex','Exit task 3 of 4 · VCAA 2017 Exam 1 Q5','Show what you know',
  '<div style="font-size:21px">Four teams, A, B, C and D, competed in a round-robin competition where each team played each of the other teams once. There were no draws.<br>The results are shown in the following matrix.'
  +C(mat([[0,0,'<i>f</i>',1],[1,0,0,0],[1,'<i>g</i>',0,1],[0,1,0,'<i>h</i>']],rl=list('ABCD'),cl=list('ABCD'),side=True,fs=22,tid='e3'),lab('winner (rows) · loser (columns)'))
  +'A ‘1’ in the matrix shows that the team named in that row defeated the team named in that column.<br>For example, the ‘1’ in row 2 shows that team B defeated team A.<br>In this matrix, the values of <i>f</i>, <i>g</i> and <i>h</i> are</div>',
  [('f','A v C: row C, column A is 1, so C beat A → <i>f</i> = 0'),('g','B v C: row B, column C is 0, so B lost → C beat B: <i>g</i> = 1'),('h','a team can’t play itself → <i>h</i> = 0')],
  '<i>f</i> = 0, <i>g</i> = 1, <i>h</i> = 0: <b>A</b>.','VCAA 2017 Further Mathematics Exam 1 Matrices Q5 (74% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7F Q12',
  mc=['<i>f</i> = 0, <i>g</i> = 1, <i>h</i> = 0','<i>f</i> = 0, <i>g</i> = 1, <i>h</i> = 1','<i>f</i> = 1, <i>g</i> = 0, <i>h</i> = 0','<i>f</i> = 1, <i>g</i> = 1, <i>h</i> = 0','<i>f</i> = 1, <i>g</i> = 1, <i>h</i> = 1'],key='A',stat=('mc',74)))
sm()
MM=[[0,1,0,0,1],[0,0,1,1,0],[1,0,0,1,0],[0,1,0,0,0],[0,0,0,1,0]]
S.append(qslide('ex','Exit task 4 of 4 · VCAA 2021 Exam 2 Q2','Show what you know',
  '<div style="font-size:14px;line-height:1.3">The main computer system in Elena’s office has broken down.<br>The five staff members, Alex (A), Brie (B), Chai (C), Dex (D) and Elena (E), are having problems sending information to each other.<br>Matrix <i>M</i> shows the available communication links between the staff members.'
  +C(EQ('<i>M</i> =',mat(MM,rl=list('ABCDE'),cl=list('ABCDE'),side=True,fs=13,tid='e4')),EQ('<i>M</i><sup>2</sup> =',mat([[0,0,1,2,0],[0,1,0,1,0],[0,1,0,0,0],[0,0,1,1,0],[0,1,0,0,0]],rl=list('ABCDE'),cl=list('ABCDE'),side=True,fs=13,tid='e4b')),gap=18)
  +'In this matrix: the ‘1’ in row A, column B indicates that Alex can send information to Brie; the ‘0’ in row D, column C indicates that Dex cannot send information to Chai.'
  +plist([('a','Which two staff members can send information directly to each other? <span class="muted">(1 mark)</span>'),
          ('b','Elena needs to send documents to Chai.<br>What is the sequence of communication links that will successfully get the information from Elena to Chai? <span class="muted">(1 mark)</span>'),
          ('c','Matrix <i>M</i><sup>2</sup> is the square of matrix <i>M</i> and shows the number of two-step communication links between each pair of staff members. Only one pair of individuals has two different two-step communication links.<br><b>List</b> each two-step communication link for this pair. <span class="muted">(1 mark)</span>')])+'</div>',
  [('a','look for a 1 and its mirror: row B col D and row D col B','data-hi="#e4|c1_3,c3_1|hy"'),('b','E sends only to D; D sends only to B; B sends to C'),('c','the 2 in <i>M</i><sup>2</sup> is row A, column D: A → B → D and A → E → D','data-hi="#e4b|c0_3|hy"')],
  '','VCAA 2021 Further Mathematics Exam 2 Matrices Q2 (a 92%, b 83%, c 21% correct, quoted by Edrolo from the examiner report) · Edrolo U3&amp;4 7F Q13',
  cmd=('List',None,'every link, every step'),
  parts=[('a','Brie and Dex'),('b','Elena → Dex → Brie → Chai'),('c','Alex → Brie → Dex and Alex → Elena → Dex')]))
S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T x4 ',1)
sm()

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 10 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('10F','10G') and v.get('url')]))
n=assemble(S,'12MAG · 10F-10G · Binary, permutation, communication and dominance matrices',os.path.join(ROOT,'lessons','10F-10G slides.html'))
print(n-1,'slides')
