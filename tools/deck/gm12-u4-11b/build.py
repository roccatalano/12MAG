"""Lesson gm12-u4-11b (11B Interpreting transition matrices) slides, built from tools/deck/tpl/tpl.py.
Output: lessons/11B slides.html      Run: python3 tools/deck/gm12-u4-11b/build.py      Screenshots: python3 tools/deck/gm12-u4-11b/shoot.py
Matrices with tools/deck/mx.py; the Do Now 4 answer diagram is redrawn with tools/deck/tpl/net.py; other diagrams are verbatim crops (fig/).

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- No CFAT this lesson (CFAT 3.11.1 opens 11C).
- Do Now: VCAA 2024 Exam 1 Q31 (D, 53%) · VCAA 2024 Exam 1 Q2 (A, 79%) · VCAA 2024 Exam 2 Q10a (average 0.6/1 = 60%) ·
          VCAA 2024 NHT Exam 2 Q12 stem + Q12a (diagram cropped; NHT report gives no %). % from tools/vcaa_current_index.csv (examiner reports).
- APK: Cambridge U1&2 Ch 4 review skills checklist 4G #17 (p. 293; solution worked for 12MAG).
- Learn: Cambridge U3&4 11B p. 555 (own words) · Edrolo U3&4 7G p. 482.
- Worked example: Cambridge U3&4 Example 3 (pp. 555-556; diagram cropped), split over two slides (a-b, c-d).
  You try: Edrolo U3&4 7G WE3 (p. 483).
- CAS: none on the card (interpreting only).
- Exit: VCAA 2019 Further Exam 1 Matrices Q8 (original wording; = Edrolo U3&4 7I Q16, p. 514; diagram cropped from the paper); E, 15% (2019 E1 report; A 27%).
"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..'))
from tpl import *
from mx import mat
from net import net
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u4-11b')
yid=lambda u:u.split('v=')[1].split('&')[0]
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
def C(*xs,gap=34): return f'<div style="display:flex;gap:{gap}px;justify-content:center;align-items:center;flex-wrap:wrap;margin:12px 0">'+''.join(xs)+'</div>'
def EQ(*xs): return '<span style="display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap">'+''.join(xs)+'</span>'
def sm(): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide T sm ',1)
def LT(m,top,side,fs):
    return f'<span style="display:inline-flex;align-items:center;gap:8px"><span style="display:inline-flex;flex-direction:column;align-items:center"><i style="color:#0a7a8a">{top}</i>{m}</span><i style="color:#0a7a8a">{side}</i></span>'
S=['<style>.sm .L .q{font-size:17px}.afig svg{max-height:330px!important}.ex3 ol.parts li{font-size:17px!important;line-height:1.3}</style>']
# ================= opening
t=title('11B','Interpreting transition matrices',f'{CAM} · 11B Interpreting transition matrices','11B')
S.append(t.replace('Unit 3<i></i>AOS 1 Data Analysis','Unit 4<i></i>AOS 3 Matrices'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill','var(--apk)'),
  ('Reading a transition matrix · Example 3','→ You try',None),('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Transition matrix <i>T</i>','columns = from (this period), rows = to (next period); each column adds to 1'),
  ('Leading diagonal','the proportion that STAY in the same state (the loops on the diagram)'),
  ('Transition diagram','the same information: one arrow (or loop) for each non-zero element')],
  [('Element t<sub>ij</sub>',F('t<sub><i>ij</i></sub> = proportion <b>from</b> column <i>j</i> <b>to</b> row <i>i</i>'),'column first: from → to'),
   ('Proportion → %',F('0.58 → 58%'),'× 100'),
   ('Proportion → number',F('number = t<sub><i>ij</i></sub> × number in the FROM state'),'0.8 × 50 = 40')],
  f'{CAM}, 11B p. 555; Study Design: transition diagrams and matrices to model and analyse practical situations'))

# ================= Do Now 1: VCAA 2024 E1 Q31 (10G)
D='…'
M31=mat([[0,1,0,1,0],[0,0,D,1,D],[1,D,0,1,0],[0,0,0,0,1],[1,D,1,0,0]],cl=list('HIJKL'),rl=list('HIJKL'),fs=15,tid='d1')
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q31','Review of 10G (last week)',
  '<div style="font-size:15px">The matrix below shows the results of a round-robin chess tournament between five players: <i>H, I, J, K</i> and <i>L</i>. In each game, there is a winner and a loser.<br>Two games still need to be played.'
  +C(LT(M31,'loser','',15),'<i style="color:#0a7a8a">rows: winner</i>',gap=12)
  +'A ‘1’ in the matrix shows that the player named in that row defeated the player named in that column. For example, the 1 in row 4 shows that player <i>K</i> defeated player <i>L</i>.<br>'
  'A ‘…’ in the matrix shows that the player named in that row has not yet competed against the player in that column.<br>'
  'At the end of the tournament, players will be ranked by calculating the sum of their one-step and two-step dominances.<br>'
  'The player with the highest sum will be ranked first. The player with the second-highest sum will be ranked second, and so on.<br>'
  'Which one of the following is <b>not</b> a potential outcome after the final two games have been played?</div>',
  [('Games left','<i>I</i> v <i>J</i> and <i>I</i> v <i>L</i>: four possible outcomes','data-hi="#d1|c1_2,c1_4,c2_1,c4_1|hy"'),
   ('Sums (D + D²)','J, L beat I: I = 2 (5th) · J, I beat L: J = 8 (1st) · I beats both: I = 8 (1st)'),
   ('J last?','J’s sum is 5 or more in every outcome, but K’s is 4 or less, so J can never be 5th')],
  'Player <i>J</i> will be ranked fifth: <b>D</b>.','VCAA 2024 General Mathematics Exam 1 Q31 (examiner report: 53% correct)',
  mc=['Player <i>I</i> will be ranked first.','Player <i>I</i> will be ranked fifth.','Player <i>J</i> will be ranked first.','Player <i>J</i> will be ranked fifth.'],key='D',stat=('mc',53)))
sm()
# ================= Do Now 2: VCAA 2024 E1 Q2 (1A)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q2','Review of 1A (last term)',
  '<div style="font-size:28px;margin-top:40px">Freddie organised a function at work. He surveyed the staff about their preferences.<br>'
  'He asked them about their <i>payment preference</i> (cash or electronic payment) and their <i>budget preference</i> (less than $50 or more than $50).<br>'
  'The variables in this survey, <i>payment preference</i> and <i>budget preference</i>, are</div>',
  [('Payment','cash / electronic: categories → categorical'),('Budget','‘less than $50’ / ‘more than $50’: two categories, not a measured number → categorical')],
  'both categorical variables: <b>A</b>.','VCAA 2024 General Mathematics Exam 1 Q2 (examiner report: 79% correct)',
  mc=['both categorical variables.','both numerical variables.','categorical and numerical variables, respectively.','numerical and categorical variables, respectively.'],key='A',
  dis=('C','$50 looks numerical, but the answers are groups (ordinal), not measurements'),stat=('mc',79)))
# ================= Do Now 3: VCAA 2024 E2 Q10a (10A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q10a','Review of 10A (last week)',
  '<div style="font-size:26px;margin-top:30px">To access the southern end of the construction site, Vince must enter a security code consisting of five numbers.<br>'
  'The security code is represented by the row matrix <i>W</i>.<br>The element in row <i>i</i> and column <i>j</i> of <i>W</i> is <i>w</i><sub><i>ij</i></sub>.<br>'
  'The elements of <i>W</i> are determined by the rule (<i>i</i> − <i>j</i>)<sup>2</sup> + 2<i>j</i>.<br>'
  'a. <b>Complete</b> the following matrix showing the five numbers in the security code. <span class="muted">(1 mark)</span>'
  +C(EQ('<i>W</i> =',mat([['____']*5],fs=26)))+'</div>',
  [('Row matrix','one row, so <i>i</i> = 1 every time; <i>j</i> = 1 to 5'),
   ('j = 1, 2','(1 − 1)² + 2 = 2 · (1 − 2)² + 4 = 5'),('j = 3, 4, 5','(−2)² + 6 = 10 · (−3)² + 8 = 17 · (−4)² + 10 = 26')],
  '<i>W</i> = '+mat([[2,5,10,17,26]],fs=24),'VCAA 2024 General Mathematics Exam 2 Q10a (examiner report: average 0.6/1)',stat=('mark',60),cmd=('Complete',None,'i = 1, j = 1…5')))
# ================= Do Now 4: VCAA 2024 NHT E2 Q12a (11A)
AR=lambda a,b,w,**o:(a,b,dict(arrow=True,w=w,**o))
DG=net({'C':(170,30,'nw'),'F':(40,230,'sw'),'B':(300,230,'se')},
  [AR('F','C','0.15',bend=-18),AR('C','B','0.15',bend=-18),AR('B','F','0.30',bend=-18),
   AR('C','F','0.20',bend=-18,hid=1,i='m1',col='#c62828'),AR('F','B','0.15',bend=-18,hid=1,i='m2',col='#c62828'),AR('B','C','0.25',bend=-18,hid=1,i='m3',col='#c62828'),
   ('C','C',dict(loop=-90,size=24,arrow=True,hid=1,i='l1',col='#c62828')),('F','F',dict(loop=200,size=24,arrow=True,hid=1,i='l2',col='#c62828')),('B','B',dict(loop=-20,size=24,arrow=True,hid=1,i='l3',col='#c62828'))],
  faces=[('0.65',218,4,'_f1'),('0.70',-14,276,'_f2'),('0.45',350,262,'_f3')],sid='d4',W=340,H=260,pad=34,fs=19)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q12a','Review of 11A (last lesson)',
  '<div style="font-size:14px">Three types of eggs are sold at a local supermarket: cage eggs (<i>C</i>), free-range eggs (<i>F</i>) and barn-laid eggs (<i>B</i>).<br>Each week customers purchase eggs from one of the three types.<br>'
  'The supermarket is holding a 10-week campaign to encourage more shoppers to purchase free-range eggs.<br>Let <i>S</i><sub><i>n</i></sub> be the state matrix that shows the expected proportion of customers who purchased each type of egg <i>n</i> weeks after the campaign began.<br>'
  'The proportion of customers who purchased each type of egg prior to the beginning of the 10-week campaign is shown in <i>S</i><sub>0</sub> below.'
  +C(EQ('<i>S</i><sub>0</sub> =',mat([[0.4],[0.4],[0.2]],rl=['C','F','B'],side=True,fs=13)))
  +'The recurrence relation that is used to calculate the expected proportion of customers who purchased each type of egg is given by'
  +C(EQ('<i>S</i><sub><i>n</i>+1</sub> = <i>T</i> × <i>S</i><sub><i>n</i></sub> &nbsp; where &nbsp;<i>T</i> =',LT(mat([['0.65','0.15','0.25'],['0.20','0.70','0.30'],['0.15','0.15','0.45']],cl=['C','F','B'],rl=['C','F','B'],side=True,fs=15,tid='d4t'),'this week','next week',15)))
  +'<div style="display:flex;gap:12px;align-items:center"><span>a. An incomplete transition diagram for Matrix <i>T</i> is shown below.<br><b>Complete</b> the transition diagram by adding the missing edges and the missing proportions. <span class="muted">(1 mark)</span></span>'+IMG('dn4.png',165)+'</div></div>',
  [('Check given','F → C 0.15 · C → B 0.15 · B → F 0.30 are drawn'),
   ('Missing','column C: C → F 0.20 · column F: F → B 0.15 · column B: B → C 0.25','data-hi="#d4t|c1_0,c2_1,c0_2|hy"'),
   ('Loops','leading diagonal: 0.65, 0.70, 0.45','data-hi="#d4t|c0_0,c1_1,c2_2|hb"')],
  '','VCAA 2024 (NHT) General Mathematics Exam 2 Q12 stem and Q12a (NHT examiner report gives no %)',cmd=('Complete',None,'edges + loops'),
  afig='<div style="width:430px;margin:0 auto">'+DG+'</div>',build=[('Three missing edges','data-show="#d4|m1,m2,m3"'),('Three loops (stay)','data-show="#d4|l1,l2,l3,f1,f2,f3"')]))
sm()

# ================= APK
TA=LT(mat([[0.8,0.3],[0.2,0.7]],cl=['S','H'],rl=['S','H'],side=True,fs=26,tid='ap'),'This week','Next week',26)
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 4G #17','Interpreting a transition matrix',
  '<div style="font-size:27px;margin-top:30px">The following transition matrix, <i>T</i>, can be used to describe whether customers bring their shopping bags to the supermarket (<i>S</i>) or leave them at home (<i>H</i>), based on their behaviour last week.'
  +C(EQ('<i>T</i> =',TA))+'If 150 people took their bags for their weekly shop, and 90 people left their bags at home this week, how many people do you expect to bring their own shopping bags next week?</div>',
  [('Row S','‘bring bags next week’ = row <i>S</i>','data-hi="#ap|c0_0,c0_1|hy"'),
   ('From S','0.8 × 150 = 120'),('From H','0.3 × 90 = 27'),('Add','120 + 27 = 147')],
  '<b>147 people</b> are expected to bring their own bags next week.',f'{CAM12} · Ch 4 review skills checklist 4G #17 (p. 293) · solution worked for 12MAG'))

# ================= Learn
TB=LT(mat([['0.80','0.10'],['0.20','0.90']],cl=['B','C'],rl=['B','C'],side=True,fs=26,tid='lb'),'Rented in','Returned to',22)
S.append(learn('Learn · 11B','Reading a transition matrix',
  '<h4>Find the element, then say it in words</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>column = where they are NOW (from) · row = where they go NEXT (to)</li>'
  '<li>the element is a proportion: × 100 for a %</li>'
  '<li>× the number in the FROM state for a number of people / cars</li>'
  '<li>‘not’ or ‘either … or’: add the right elements, or use 1 − …</li></ul>',
  '<div style="display:flex;gap:30px;align-items:center;justify-content:center;font-size:24px">'+EQ('<i>T</i> =',TB)+
  '<div style="display:flex;flex-direction:column;gap:12px;font-size:22px">'
  '<div class="frag">50 cars rented in Bendigo: <b>0.80 × 50 = 40</b> back to Bendigo</div>'
  '<div class="frag">and <b>0.20 × 50 = 10</b> (20%) to Colac</div>'
  '<div class="frag">40 cars rented in Colac: <b>0.10 × 40 = 4</b> to Bendigo, <b>0.90 × 40 = 36</b> stay</div></div></div>',
  'Always multiply by the number in the COLUMN (from) state, not the row.',f'{CAM}, 11B p. 555 (own words) · {EDR}, 7G p. 482',
  cards=(kcard('Element t<sub>ij</sub>',F('from column <i>j</i> → to row <i>i</i>')),kcard('Number',F('t<sub><i>ij</i></sub> × number FROM')))))

# ================= Ex 3 (two slides) / You try 7G WE3
T3=lambda tid:LT(mat([[0.7,0.05,0.12],[0.1,0.8,0.11],[0.2,0.15,0.77]],cl=['A','W','B'],rl=['A','W','B'],side=True,fs=18,tid=tid),'','Returned to',18)
EX3=lambda tid:('<div style="font-size:17px">The following transition matrix, <i>T</i>, and its transition diagram can be used to describe the weekly pattern of rental car returns in three locations: Albury, Wodonga and Benalla.'
  +C(EQ('<i>T</i> =',T3(tid)),IMG('ex3.png',270),gap=16)+'Use the transition matrix <i>T</i> and its transition diagram to answer the following questions.</div>')
S.append(qslide('we','Worked example 3 (a, b) · 11B','Interpreting a transition matrix',
  EX3('w3')+'<div class="ex3">'+plist([('a','What percentage of cars rented in Wodonga each week are predicted to be returned to:<br>i Albury? &nbsp; ii Benalla? &nbsp; iii Wodonga?'),
   ('b','Two hundred cars were rented in Albury this week. How many of these cars do we expect to be returned to:<br>i Albury? &nbsp; ii Benalla? &nbsp; iii Wodonga?')])+'</div>',
  [('a: column W','rented in Wodonga = column <i>W</i>','data-hi="#w3|c0_1,c1_1,c2_1|hy"'),
   ('b: column A','rented in Albury = column <i>A</i>; × 200','data-hi="#w3|c0_0,c1_0,c2_0|hb"')],
  '',f'{CAM} · Example 3 (pp. 555–556)',video='Cambridge GO · Example 3 (11B Resources)',
  parts=[('a','i 0.05 or <b>5%</b> &nbsp; ii 0.15 or <b>15%</b> &nbsp; iii 0.80 or <b>80%</b>'),('b','i 0.70 × 200 = <b>140 cars</b> &nbsp; ii 0.20 × 200 = <b>40 cars</b> &nbsp; iii 0.10 × 200 = <b>20 cars</b>')]))
sm()
S.append(qslide('we','Worked example 3 (c, d) · 11B','Interpreting a transition matrix',
  EX3('w3b')+'<div class="ex3">'+plist([('c','What percentage of cars rented in Benalla each week are <i>not</i> expected to be returned to Benalla?'),
   ('d','One hundred and sixty cars were rented in Albury this week. How many of these cars are expected to be returned to either Benalla or Wodonga?')])+'</div>',
  [('c: column B','not back to Benalla: the other two elements of column <i>B</i> (or 1 − 0.77)','data-hi="#w3b|c0_2,c1_2|hy"'),
   ('d: column A','to Benalla 0.2 and to Wodonga 0.1, each × 160','data-hi="#w3b|c1_0,c2_0|hb"')],
  '',f'{CAM} · Example 3 (pp. 555–556)',video='Cambridge GO · Example 3 (11B Resources)',
  parts=[('c','11 + 12 = <b>23%</b> or 100 − 77 = 23%'),('d','20% of 160 + 10% of 160 = 32 + 16 = <b>48 cars</b>')]))
sm()
TY=LT(mat([['0.68','0.34','0.58'],['0.22','0.17','0.36'],['0.10','0.49','0.06']],cl=['drive','bus','train'],rl=['drive','bus','train'],side=True,fs=26,tid='y1'),'today','tomorrow',22)
S.append(qslide('yt','You try · Edrolo 7G WE3','Interpreting a transition matrix',
  '<div style="font-size:27px;margin-top:30px">The transition matrix, <i>T</i>, is used to predict the number of people who drive, bus, or train to work on a day-to-day basis.'
  +C(EQ('<i>T</i> =',TY))+'What percentage of people who caught the train today will choose to drive tomorrow?</div>',
  [('Element','train today = column 3 · drive tomorrow = row 1','data-hi="#y1|c0_2|hy"'),('Convert','0.58 = 58%')],
  '<b>58%</b> of people who caught the train today will drive tomorrow.',f'{EDR} · 7G Worked example 3 (p. 483)'))

# ================= Exit
S.append(qslide('ex','Exit task · VCAA 2019 Exam 1 Q8','Show what you know',
  ('<div style="font-size:21px">An airline parks all of its planes at Sydney airport or Melbourne airport overnight.<br>The transition diagram below shows the change in the location of the planes from night to night.</div>',
   IMG('exit1.png',470),
   '<div style="font-size:21px">There are always <i>m</i> planes parked at Melbourne airport.<br>There are always <i>s</i> planes parked at Sydney airport.<br>'
   'Of the planes parked at Melbourne airport on Tuesday night, 12 had been parked at Sydney airport on Monday night.<br>How many planes does the airline have?</div>'),
  [('Sydney → Melbourne','0.48 × <i>s</i> = 12, so <i>s</i> = 25'),
   ('Numbers stay the same','so 12 planes also move Melbourne → Sydney: 0.2 × <i>m</i> = 12, so <i>m</i> = 60'),
   ('Total','<i>m</i> + <i>s</i> = 60 + 25 = 85')],
  '85 planes: <b>E</b>.','VCAA 2019 Further Mathematics Exam 1 Matrices Q8 (examiner report: 15% correct) · Edrolo U3&amp;4 7I Q16',
  mc=['25','37','62','65','85'],key='E',dis=('A','25 is only the Sydney planes (s); 27% chose it'),stat=('mc',15)))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 11 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='11B' and v.get('url')]))
n=assemble(S,'12MAG · 11B · Interpreting transition matrices',os.path.join(ROOT,'lessons','11B slides.html'))
print(n-1,'slides')
