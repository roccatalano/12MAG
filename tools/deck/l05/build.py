"""Lesson l05 (2D, 2E) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2D-2E slides.html
Run: python3 tools/deck/l05/build.py      Screenshots: python3 tools/deck/l05/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn from the source figures, values read off them):
- Do Now: VCAA 2025 NHT Exam 1 Q11 (answer B; NHT report gives no %) · VCAA 2025 NHT Exam 1 Q5 (answer C; no %)
          VCAA 2025 Exam 2 Q1d (report: 89% scored 1) · VCAA 2023 Exam 2 Q1bii (report: 39% scored 1, answer 14.1)
- APK (planner card): Cambridge U1&2 Ch 7 skills checklist 7B #3 (p. 457; uses the height/foot-length data of #2; checklist has no answer:
  solution written for 12MAG, r = 0.66 checked on CAS → moderate) · VCAA 2020 Further Exam 2 Core Q4bi (= Edrolo U1&2 6A Q16, 'adapted';
  original VCAA wording used; report: 78% scored 1, answer weight)
- Learn: Cambridge Units 3&4 2D pp. 130-133 (scatterplot, participation-rate data) and 2E pp. 134-138 (direction, form, strength)
- Worked examples: Cambridge Units 3&4 Examples 13, 14, 15 (pp. 135-138). Example 15 point clouds redrawn approximately.
- You try (planner card): Edrolo U1&2 6B WE3 (p. 329, burger patties; scatterplot approximate) · Edrolo U1&2 6B WE1 (p. 327; approximate)
  · Edrolo U3&4 2C WE4 (p. 136, sleep and errors) · CAS You try: Edrolo U3&4 2C WE3 (p. 133, cross-country times).
- Exits: Edrolo U3&4 2C Q15 = VCAA 2018 Further Exam 2 Core Q2b (report: 90% scored 1; original wording used, scatterplot redrawn)
         Edrolo U3&4 2C Q16 = VCAA 2016 Further Exam 2 Core Q3a (report: 78% scored 1; original wording incl. n = 13, r² = 0.97)
- CAS: planner/cas-skills.json 'scatterplot'; task data = Cambridge 2D CAS 1 (test scores).
- Videos: videos.json (2D MaffsGuru link, draft; 2E link still blank).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,os.path.join(H,'..','l04')); sys.path.insert(0,H)
from tpl import *
import tpl as TPL
from figs import *
from figs import scat as SC
import importlib.util
_s=importlib.util.spec_from_file_location('f4',os.path.join(H,'..','l04','figs.py')); F4=importlib.util.module_from_spec(_s); _s.loader.exec_module(F4)
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'

def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:8px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'):
    return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def table(head,rows,fs=19,rid='',extra=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td><span data-i="{i}">{c}</span></td>' for j,c in enumerate(r))+'</tr>' for i,r in enumerate(rows))
    return f'<table class="t"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}"><tr>{th}</tr>{tr}</table>'
DFS=[('D','Direction','#2f6fdf'),('F','Form','#1f9e74'),('S','Strength','#7b3fbf'),('O','Outliers','#c0632b')]
def dfs(pre,lines,fs=17,concl=None):
    """Describe-an-association template: Direction, Form, Strength, Outliers (None = skip); filled by data-fill="<pre>1..4", sentence <pre>5."""
    rows=''
    for k,((l,n,c),t) in enumerate(zip(DFS,lines)):
        if t is None: continue
        rows+=f'<div class="socsr"><span class="socsl" style="background:{c}">{l}</span><span class="socsn" style="color:{c}">{n}</span><span class="socst">{B(pre+str(k+1),t,"…")}</span></div>'
    if concl: rows+=f'<div class="socsr"><span class="socsl" style="background:#333">✓</span><span class="socsn">Sentence</span><span class="socst">{B(pre+"5",concl,"in context")}</span></div>'
    return f'<div class="socs report" style="font-size:{fs}px">{rows}</div>'

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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l05')
yid=lambda u:u.split('v=')[1].split('&')[0]

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.T .mc>div{padding-right:54px}'
   '.trio{display:flex;gap:10px;justify-content:center}.trio>div{flex:1;text-align:center;font-weight:700}</style>']
# ================= opening
S.append(title(5,'Investigating associations between two numerical variables · How to interpret a scatterplot',
  f'{CAM} · 2D Investigating associations between two numerical variables · 2E How to interpret a scatterplot','L05',
  flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')).replace('font-size:84px','font-size:60px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills','var(--apk)'),
  ('The scatterplot','',None),('CAS: scatterplots','→ You try',None),('Direction','→ WE 13',None),('Form','→ WE 14',None),('Strength','→ WE 15',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mk=lambda pts,xr,yr:W_(170,SC(pts,xr,yr,100,100,W=200,H=140,r=4,grid=False,ticks=False))
S.append(keys([
  ('Scatterplot','a plot of paired numerical data: EV on the horizontal (x) axis, RV on the vertical (y) axis; one point per case',mk(PART,(0,60),(30,55))),
  ('Direction','positive (RV tends to increase as EV increases), negative (RV tends to decrease) or none'),
  ('Form','linear (points follow a straight line) or non-linear (a curve)'),
  ('Strength','strong, moderate or weak: how tightly the points cluster about a trend line'),
  ('Outlier','a point that does not fit the pattern of the rest')],
  [('Describe an association',F('Direction · Form · Strength'),'+ any outliers, then a sentence in context'),
   ('Sentence template',F('There is a <i>strong, positive, linear</i> association between RV and EV'),'e.g. ‘taller players tend to be heavier’')],
  f'{CAM}, 2D pp. 130–131, 2E pp. 134–138'))

# ================= Do Now 1: VCAA 2025 NHT E1 Q11 (2C)
BX=[('1896',(153,160,162,165.2,171.8),[]),('1946',(159.5,166.7,168.8,170.9,177.9),[]),('1996',(159.8,167.2,171.1,175,182.7),[])]
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 NHT Exam 1 Q11','Review of 2C',
  G('The graph below shows parallel boxplots for the average heights of adult males, in centimetres, in 208 countries in 1896, 1946 and 1996.',
    W_(600,F4.pbox(BX,150,185,5,'average height (cm)',W=700,rowH=50,fs=15,lab=60).replace('<svg','<svg id="d1b"',1)),'Which one of the following statements can be concluded from the boxplots?'),
  [('Test B','1996 median ≈ 171 cm > 170 cm: half of 208 = 104 countries are above it ✓','data-hi="#d1b|2m|hy"'),
   ('Check A, C, D','A: range 1946 ≈ 18 &lt; 1996 ≈ 23 ✗ · C: 1896 max ≈ 172 &gt; 1996 median ≈ 171 ✗ · D: 1896 min ≈ 153 &lt; 155 ✗','data-hi="#d1b|0w,1w,2w|hb"')],
  'More than 100 countries had an average above 170 cm in 1996: <b>B</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q11 (examiner report: answer only, no %; boxplots redrawn horizontally)',
  mc=['The range of the average heights for males in the 208 countries was greater in 1946 than in 1996.','The average adult male height was greater than 170 cm in 1996 for more than 100 of the countries observed.',
      'The largest average adult male height observed in 1896 was less than the median of the average male heights observed in 1996.','No countries out of any of the 208 countries observed had an average adult male height less than 155 cm in 1896.'],key='B'))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2025 NHT E1 Q5 (1C)
HG=[4,6,8,10,8,5,4,2,1,1,1]
def histo(fr,W=560,Hh=270):
    L,B_,T=50,46,10; pw=W-L-14; ph=Hh-T-B_; bw=pw/11
    s=f'<svg id="d2h" viewBox="0 0 {W} {Hh}" width="100%" style="display:block">'
    for y in range(0,13,2): s+=f'<line x1="{L}" x2="{L+pw}" y1="{T+ph-y/12*ph:.1f}" y2="{T+ph-y/12*ph:.1f}" stroke="#e3e6ee"/><text x="{L-6}" y="{T+ph-y/12*ph+5:.1f}" text-anchor="end" font-size="14">{y}</text>'
    for i,f in enumerate(fr): s+=f'<rect data-i="b{i}" x="{L+i*bw:.1f}" y="{T+ph-f/12*ph:.1f}" width="{bw:.1f}" height="{f/12*ph:.1f}" fill="#c9cdd6" stroke="#333"/>'
    for i in range(12): s+=f'<text x="{L+i*bw:.1f}" y="{T+ph+18}" text-anchor="middle" font-size="13">{95+5*i}</text>'
    s+=f'<line x1="{L}" x2="{L+pw}" y1="{T+ph}" y2="{T+ph}" stroke="#333" stroke-width="2"/><text x="{L+pw/2}" y="{Hh-6}" text-anchor="middle" font-size="15" font-style="italic">systolic blood pressure</text>'
    s+=f'<text x="13" y="{T+ph/2}" text-anchor="middle" font-size="14" transform="rotate(-90 13 {T+ph/2})">frequency</text></svg>'
    return s
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 NHT Exam 1 Q5','Review of 1C',
  G('The <em class="v">systolic blood pressure</em> of 50 people was recorded. The results are summarised in the histogram below.',W_(470,histo(HG)),
    'The percentage of these people with a <em class="v">systolic blood pressure</em> less than 120 is closest to'),
  [('Count','bars below 120: 4 + 6 + 8 + 10 + 8 = 36','data-hi="#d2h|b0,b1,b2,b3,b4|hy"'),
   fx('Percentage','%',F(FR([V('below 120','36')],[V('total','50')]),' × 100%'),'72%')],
  '36 of the 50 people: <b>C</b>, 72%.','VCAA 2025 (NHT) General Mathematics Exam 1 Q5 (examiner report: answer only, no %; histogram redrawn)',
  mc=['36%','41%','72%','82%'],key='C'))
# ================= Do Now 3: VCAA 2025 E2 Q1d (2B)
T1=[('350 000','apartment'),('490 000','apartment'),('500 000','apartment'),('620 000','apartment'),('720 000','apartment'),('830 000','apartment'),('875 000','apartment'),('995 000','apartment'),('1 100 000','apartment'),('1 520 000','apartment'),
    ('800 000','house'),('840 000','house'),('920 000','house'),('920 000','house'),('1 010 000','house'),('1 263 000','house'),('1 398 000','house'),('1 460 000','house'),('1 540 000','house'),('1 540 000','house')]
def t1(rows,off,rid):
    return (f'<table class="t" id="{rid}" style="font-size:12px;margin-top:3px"><tr><th><i>Price</i> ($)</th>'+''.join(f'<td style="padding:2px 4px"><span data-i="{off+i}">{p}</span></td>' for i,(p,t) in enumerate(rows))+'</tr>'
            f'<tr><th><i>Type</i></th><td colspan="{len(rows)}" style="padding:2px 4px">{rows[0][1]}</td></tr></table>')
T3=('<table class="t" style="font-size:14px"><tr><th rowspan="2">Price range ($)</th><th colspan="2">Type of home</th></tr><tr><th>House (%)</th><th>Apartment (%)</th></tr>'
    f'<tr><td>less than 600 000</td><td>{B("d3h d31","0")}</td><td>{B("d3a d32","30")}</td></tr><tr><td>from 600 000 to 1 000 000</td><td>40</td><td>{B("d3a d33","50")}</td></tr>'
    f'<tr><td>more than 1 000 000</td><td>{B("d3h d34","60")}</td><td>{B("d3a d35","20")}</td></tr><tr><td><b>Total</b></td><td>100</td><td>100</td></tr></table>')
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q1d','Review of 2B',
  '<div style="font-size:16px">Table 1, below, shows the prices in dollars, <em class="v">price</em>, for a sample of 20 homes sold in an inner Melbourne suburb during 2017. The <em class="v">type</em> of home sold is either an apartment or a house.</div>'
  '<div style="font-weight:700;font-size:13px;margin-top:4px">Table 1 <span class="muted" style="font-weight:400">(arranged across the page)</span></div>'+t1(T1[:10],0,'d3a')+t1(T1[10:],10,'d3h')+
  '<div style="font-size:16px;margin-top:6px">Table 3, below, shows the percentage of houses and apartments with prices in the given ranges. Some information is missing.<br>Use the data from Table 1 to complete Table 3. <span class="muted">(1 mark)</span></div>'
  '<div style="font-weight:700;font-size:13px;margin-top:4px">Table 3</div>'+T3.replace(B("d3h d31","0"),'&nbsp;').replace(B("d3a d32","30"),'&nbsp;').replace(B("d3a d33","50"),'&nbsp;').replace(B("d3h d34","60"),'&nbsp;').replace(B("d3a d35","20"),'&nbsp;'),
  [('Houses','10 houses: none below 600 000 → 0% · 4 in the middle (given 40%) · 6 above 1 000 000 → 60%','data-hi="#d3h|10,11,12,13,14,15,16,17,18,19|hb" data-fill="d3h"'),
   ('Apartments','10 apartments: 3 below 600 000 → 30% · 5 from 600 000 to 1 000 000 → 50% · 2 above → 20%','data-hi="#d3a|0,1,2|hy;#d3h||" data-fill="d3a"'),
   ('TMPL',T3,'','data-stat="89"')],
  '','VCAA 2025 General Mathematics Exam 2 Q1d (examiner report)',stat=('mark',89),cmd=('complete',1,'every missing cell')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2023 E2 Q1bii (1F)
OY=[(1,12.9,13.0,5.1,'large'),(2,11.4,11.7,4.8,'medium'),(3,17.4,17.4,6.5,'large'),(4,6.8,7.2,2.9,'small'),(5,9.6,10.1,3.7,'medium'),(6,15.5,15.6,5.7,'large'),(7,9.7,9.9,4.0,'small'),(8,7.0,7.5,2.7,'small'),
    (9,12.6,12.7,5.5,'medium'),(10,12.5,12.7,5.0,'medium'),(11,10.1,10.5,3.9,'medium'),(12,10.6,10.8,4.1,'medium'),(13,13.0,13.1,5.3,'large'),(14,8.1,8.5,3.5,'small'),(15,14.1,14.2,5.3,'large')]
OT=table(['<i>ID</i>','<i>Weight</i><br>(g)','<i>Volume</i><br>(cm³)','<i>Image size</i><br>(megapixels)','<i>Size</i>'],[[str(a),f'{b:.1f}',f'{c:.1f}',f'{d:.1f}',e] for a,b,c,d,e in OY],fs=13,rid='d4t')
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q1bii','Review of 1F',
  '<div style="display:flex;gap:14px;align-items:flex-start"><div style="flex:1;font-size:17px">Data was collected to investigate the use of electronic images to automate the sizing of oysters for sale.<br>The data collected for a sample of 15 oysters is displayed in Table 1.'
  '<div style="margin-top:14px">Determine, in grams:</div><div>ii. the median <em class="v">weight</em> of the large oysters in this sample. <span class="muted">(1 mark)</span></div></div><div><div style="font-weight:700;font-size:14px">Table 1</div>'+OT+'</div></div>',
  [('Large only','IDs 1, 3, 6, 13, 15: weights 12.9, 17.4, 15.5, 13.0, 14.1','data-hi="#d4t|0,2,5,12,14|hy"'),
   ('Order','12.9, 13.0, <b>14.1</b>, 15.5, 17.4: 5 values, the median is the 3rd')],
  'median = <b>14.1</b> g','VCAA 2023 General Mathematics Exam 2 Q1bii (examiner report: many gave 11.4, the median of the whole data set)',stat=('mark',39),cmd=('Determine',1,'large oysters only')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK 1: Cambridge U1&2 checklist 7B #3
FT=f'<table class="t" style="font-size:12px"><tr><th>height</th><th>foot length</th><th>height</th><th>foot length</th></tr>'+''.join(f'<tr><td>{FOOT[i][0]}</td><td>{FOOT[i][1]}</td><td>{FOOT[i+8][0]}</td><td>{FOOT[i+8][1]}</td></tr>' for i in range(8))+'</table>'
FS=SC(FOOT,(150,190),(15,45),5,5,'height (cm)','foot length (cm)',W=460,H=330,r=5,fs=14,tl=((152,20.5),(186,33.5)),sid='a1s')
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7B #3','Describing an association from a scatterplot',
  '<div>In order to predict the length of a person’s foot from their height, a group of 16 students collected the following data set, which gives height (<em class="v">height</em>) and the length of their foot (<em class="v">foot length</em>) in centimetres.</div>'
  '<div style="display:flex;gap:10px;align-items:center;margin:8px 0">'+FT+W_(300,FS)+'</div>'
  '<div>Describe the association in the previous scatterplot between height and foot length in terms of direction, form and strength.</div>',
  [('Direction','points trend upwards left to right → positive','data-show="#a1s|tl" data-fill="a11"'),
   ('Form','scattered about a straight line → linear','data-fill="a12"'),
   ('Strength','broadly clustered about the line → moderate','data-fill="a13"'),
   ('Outlier','(185, 40) sits well above the pattern','data-hi="#a1s|p14|hc" data-fill="a14"'),
   ('TMPL',dfs('a1',['positive','linear','moderate','possible outlier: height 185 cm, foot length 40 cm'],fs=16,concl='There is a moderate, positive, linear association between foot length and height: taller students tend to have longer feet.'),'','data-fill="a15"')],
  '',f'{CAM12} · Ch 7 skills checklist 7B #3 (data from #2, p. 457; scatterplot drawn for 12MAG) · solution written for 12MAG',cmd=('Describe',None,'direction, form, strength')))
S[-1]=S[-1].replace('<section class="slide T apk"','<section class="slide T apk sm"',1)
# ================= APK 2: VCAA 2020 E2 Q4bi
BT=table(['<i>Age</i><br>(years)','<i>Body density</i><br>(kg/litre)','<i>Weight</i><br>(kg)'],[[str(a),f'{b:.2f}',f'{c:.1f}'] for a,b,c in V20],fs=14)
S.append(qslide('apk','APK · Year 11 · VCAA 2020 Exam 2 Q4bi','Explanatory and response variables',
  '<div style="display:flex;gap:16px;align-items:flex-start"><div style="flex:1">The age, in years, body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 men aged 23 to 25 years are shown in the table below.'
  '<div style="margin-top:16px">A least squares line is to be fitted to the data with the aim of predicting body density from weight.</div><div style="margin-top:10px">i. Name the explanatory variable for this least squares line. <span class="muted">(1 mark)</span></div></div><div>'+BT+'</div></div>',
  [('Predicting … from …','we predict the RV (body density) <b>from</b> the EV'),('EV','the variable we predict from: weight')],
  'The explanatory variable is <em class="v">weight</em>.',f'{EDR12} · 6A Q16 · VCAA 2020 Further Mathematics Exam 2 Core Q4bi (examiner report; original wording)',stat=('mark',78),cmd=('Name',1,'one variable')))

# ================= Learn 2D: the scatterplot
PS=SC(PART,(0,60),(30,55),10,5,'Participation rate (%)','Hours worked',W=520,H=330,r=6,fs=14,hid=True,sid='lps')
ord_=','.join(f'p{k}' for k in range(1,9))
S.append(learn('Learn · 2D','The scatterplot',
  '<h4>Two numerical variables → scatterplot</h4><ul class="bul" style="font-size:19px;line-height:1.55;margin-left:22px"><li>each point is <b>one case</b> (here, one country)</li>'
  '<li>EV on the <b>horizontal (x) axis</b>, RV on the <b>vertical (y) axis</b></li></ul>'
  f'<table class="t" style="font-size:14px;margin-top:8px"><tr><th>Participation rate (%)</th>{"".join(f"<td>{x}</td>" for x,_ in PART)}</tr><tr><th>Hours worked</th>{"".join(f"<td>{y}</td>" for _,y in PART)}</tr></table>',
  W_(470,PS),'Read the question: the variable you predict FROM is the EV and goes on the x-axis.',f'{CAM}, 2D pp. 130–131 (9 countries)',
  frags='<span class="frag" data-show="#lps|p0" data-hi="#lps|p0|hy"></span><span class="frag" data-show="#lps|'+ord_+'" data-hi="#lps||"></span>',
  cards=(kcard('Scatterplot','one point per case, EV across, RV up'),)))
# ================= CAS (2D)
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['scatterplot']
TS=SC(list(zip(TEST1,TEST2)),(4,20),(4,22),2,2,'test1','test2',W=440,H=290,r=5,fs=13)
S.append(cas('CAS · 2D','Constructing a scatterplot',
  '<p style="font-size:21px">Construct a scatterplot for the set of test scores given below. Treat test 1 as the explanatory (i.e. x) variable.</p>'
  f'<table class="t" style="font-size:17px;margin:10px 0"><tr><th>Test 1</th>{"".join(f"<td>{x}</td>" for x in TEST1)}</tr><tr><th>Test 2</th>{"".join(f"<td>{x}</td>" for x in TEST2)}</tr></table>'+W_(380,TS),
  C['ti'],C['classpad'],'test1 on the x-axis, test2 on the y-axis: 9 points, a positive association.',
  f'{CAM} · 2D CAS 1 (pp. 131–132) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
# ================= You try (CAS): Edrolo 2C WE3
CS=SC(CROSS,(680,940),(0,11),40,1,'time (seconds)','points',W=470,H=300,r=5,fs=13)
S.append(qslide('yt','You try · Edrolo 2C WE3','Constructing a scatterplot on CAS',
  G('10 students were competing in the school cross-country. Each student’s house would be awarded <em class="v">points</em> based on their placing in the race. The <em class="v">time</em> that it took each student to complete the race and the number of house <em class="v">points</em> they received were recorded.',
    table(['<i>time</i> (s)']+[str(t) for t,_ in CROSS],[['<i>points</i>']+[str(p) for _,p in CROSS]],fs=13),'With a calculator, use the data in the table to construct a scatterplot.'),
  [('Lists','name a list ‘time’ and another list ‘points’ and enter the data'),
   ('RV and EV','points are awarded based on time: RV <em>points</em>, EV <em>time</em>'),
   ('Plot','Data &amp; Statistics (TI) or StatGraph Scatter (ClassPad): EV on the x-axis')],
  'Scatterplot of <em>points</em> (y) against <em>time</em> (x):',f'{EDR} · 2C Worked example 3 (pp. 133–134)',cmd=('construct',None,'EV across, RV up'),afig=W_(330,CS)))

# ================= Learn 2E: direction
FB=SC([(173,68),(174,75),(175,71),(176,73),(176,76),(178,68),(178,73),(179,77),(180,79),(181,81),(182,78),(183,85),(184,80),(185,87),(185,89),(186,78),(187,75),(188,83),(191,87),(192,80),(193,86),(194,83),(195,85),(195,90),(196,83),(197,92),(201,96),(206,100)],(170,210),(60,100),10,10,'Height (cm)','Weight (kg)',W=330,H=250,r=4,fs=12,tl=((172,70),(206,98)),sid='ld1')
HW=SC([(0,49),(4,51),(6,48),(7,48.5),(20,42),(21,39),(22,42.5),(26,39),(27,38.5),(27,35),(27,34.5),(31,40),(36,38.5),(37,36.5),(55,35)],(0,60),(30,50),10,5,'Participation rate (%)','Hours worked',W=330,H=250,r=4,fs=12,tl=((0,49.5),(56,34)),sid='ld2')
S.append(learn('Learn · 2E','Direction of an association',
  '<h4>First: is there a clear pattern?</h4><p style="font-size:19px">No pattern (a random scatter) → <b>no association</b>. A clear pattern → describe its <b>direction</b>:</p>'
  '<ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li><b>positive</b>: points trend <b>upwards</b> left to right (RV tends to increase as EV increases)</li><li><b>negative</b>: points trend <b>downwards</b> left to right</li></ul>',
  '<div class="trio"><div>'+W_(300,FB)+'positive</div><div>'+W_(300,HW)+'negative</div></div>',
  'Always say what the direction means in context: ‘taller players tend to be heavier’.',f'{CAM}, 2E pp. 134–135 (footballers; 15 countries)',
  frags='<span class="frag" data-show="#ld1|tl"></span><span class="frag" data-show="#ld2|tl"></span>',cards=(kcard('Direction','positive · negative · none'),)))
# ================= WE13
p13=lambda pts,xr,yr,xt,yt,xl,yl,sid,tl=None:W_(250,SC(pts,xr,yr,xt,yt,xl,yl,W=300,H=240,r=4,fs=12,tl=tl,sid=sid))
S.append(qslide('we','Worked example 13 · 2E','Direction of association',
  'Classify each of the following scatterplots as exhibiting positive, negative or no association. Where there is an association, describe the direction of the association in terms of the variables in the scatterplot and what it means in terms of the variables involved.'
  '<div class="trio" style="margin-top:10px"><div>a'+p13(E13A,(0,6),(0,70),1,10,'Dose (mg)','Reaction time (min)','w13a',((0,62),(5.5,8)))+'</div><div>b'+p13(E13B,(20,36),(0,25),2,5,'Age (years)','Diameter (cm)','w13b')+'</div><div>c'+p13(E13C,(145,180),(145,180),5,5,'Height mother','Height daughter','w13c',((148,156),(178,180)))+'</div></div>',
  [],'',f'{CAM} · Example 13 (pp. 135–136; scatterplots redrawn)',video='Cambridge GO · Example 13 (2E Resources)',cmd=('Classify',None,'direction, then what it means'),
  parts=[('a','The points trend downwards from left to right. The direction of the association is negative. Reaction times tend to decrease as the drug dose increases.','data-show="#w13a|tl" data-hi="#w13a|p|hy"'),
         ('b','There is no pattern in the scatterplot of diameter against age. There is no association between diameter and age.','data-hi="#w13b|p|hy"'),
         ('c','The points trend upwards from left to right. The direction of the association is positive. Taller mothers tend to have taller daughters.','data-show="#w13c|tl" data-hi="#w13c|p|hy"')]))
# ================= You try: Edrolo U1&2 6B WE3
S.append(qslide('yt','You try · Edrolo U1&amp;2 6B WE3','Interpreting the direction of an association',
  G('The relationship between customer satisfaction and burger patty size at a fast food restaurant is shown in the following scatterplot.',
    W_(430,SC(W3,(0,20),(0,20),5,5,'burger patty diameter (cm)','customer satisfaction level (0–20)',W=470,H=320,r=4,fs=13,tl=((0,1),(19,20.2)),sid='y1s')),
    'Interpret the correlation between <em class="v">burger patty diameter</em> and <em class="v">customer satisfaction level</em>.'),
  [('Direction','the values follow an upward trend from left to right: positive','data-show="#y1s|tl"'),
   ('In context','an increase in the EV goes with an increase in the RV')],
  'An increase in <em class="v">burger patty diameter</em> is associated with an increase in <em class="v">customer satisfaction level</em>.',f'{EDR12} · 6B Worked example 3 (p. 329; scatterplot redrawn)',cmd=('Interpret',None,'direction, in context')))

# ================= Learn 2E: form
PF=[(x,round(5*(1-2.718**(-x/2.2)),2)) for x in [0.3,0.8,1.2,1.8,2.4,3,3.6,4.4,5,6,7,8,9,10]]
VEL=SC([(0,1),(0.5,3.5),(1,5.5),(1.5,8),(2,11),(2.5,13),(3,15.5),(3.5,17),(4,21),(4.5,22),(5,25.5)],(0,5),(0,30),1,5,'Time (s)','Velocity (m/s)',W=320,H=240,r=4,fs=12,tl=((0,1),(5,25.5)),sid='lf1')
PER=SC(PF,(0,10),(0,5),2,1,'Time spent practising','Performance level',W=320,H=240,r=4,fs=12,curve=[(x/4,5*(1-2.718**(-x/8.8))) for x in range(0,41)],sid='lf2')
S.append(learn('Learn · 2E','Form of an association',
  '<h4>Linear or non-linear?</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li><b>linear</b>: the points tend to follow a <b>straight line</b></li><li><b>non-linear</b>: the points tend to follow a <b>curved line</b></li></ul>'
  '<p style="font-size:17px;margin-top:6px">For now we analyse linear associations; non-linear data can often be made linear (Chapter 4).</p>',
  '<div class="trio"><div>'+W_(290,VEL)+'linear</div><div>'+W_(290,PER)+'non-linear</div></div>',
  'Imagine a line through the points: if a curve fits better, the form is non-linear.',f'{CAM}, 2E pp. 136–137',
  frags='<span class="frag" data-show="#lf1|tl"></span><span class="frag" data-show="#lf2|tl"></span>',cards=(kcard('Form','linear · non-linear'),)))
# ================= WE14
S.append(qslide('we','Worked example 14 · 2E','Form of an association',
  'Classify the form of the association in each of scatterplot as linear or non-linear.'
  '<div class="trio" style="margin-top:14px"><div>a'+W_(330,SC(E13C,(145,180),(145,180),5,5,'Height mother','Height daughter',W=340,H=270,r=4,fs=12,tl=((148,156),(178,180)),sid='w14a'))+'</div>'
  '<div>b'+W_(330,SC(E14B,(1,7),(0,14),1,2,'Number of weeks on a diet','Weight loss (kg)',W=340,H=270,r=4,fs=12,curve=[(1.8+k*0.13,12.6*(1-2.718**(-(1.8+k*0.13-1.75)/1.9))) for k in range(40)],sid='w14b'))+'</div></div>',
  [],'',f'{CAM} · Example 14 (p. 137; scatterplots redrawn)',video='Cambridge GO · Example 14 (2E Resources)',cmd=('Classify',None,'linear or non-linear'),
  parts=[('a','There is a clear pattern. The points can be imagined to be scattered around a straight line. The association is linear.','data-show="#w14a|tl"'),
         ('b','There is a clear pattern. The points can be imagined to be scattered around a curved line rather than a straight line. The association is non-linear.','data-show="#w14b|tl"')]))
# ================= You try: Edrolo U1&2 6B WE1
S.append(qslide('yt','You try · Edrolo U1&amp;2 6B WE1','Describing strength, direction and form',
  G('Consider the following scatterplot.',W_(470,SC(W1,(0,11.5),(0,15),2,2,'<tspan font-style="italic">x</tspan>','y',W=520,H=330,r=5,fs=13,tl=((0,1.5),(11.2,13.5)),sid='y2s')),
    'Describe the relationship in terms of strength, direction and form.'),
  [('Strength','a distinct trend, but the points are more spread out: moderate','data-fill="y23"'),
   ('Direction','<i>y</i> tends to increase as <i>x</i> increases: positive','data-fill="y21"'),
   ('Form','the trend resembles a straight line: linear','data-show="#y2s|tl" data-fill="y22"'),
   ('TMPL',dfs('y2',['positive','linear','moderate',None],fs=17,concl='Moderate, positive, linear relationship'),'','data-fill="y25"')],
  '',f'{EDR12} · 6B Worked example 1 (p. 327; scatterplot redrawn)',cmd=('Describe',None,'strength, direction, form')))

# ================= Learn 2E: strength
import random as _R
def cloud(sd,seed,neg=False):
    r=_R.Random(seed); return [(x,(10-x if neg else x)+r.gauss(0,sd)) for x in [r.uniform(0.5,9.5) for _ in range(16)]]
mini=lambda pts:SC(pts,(0,10),(-3,13),20,20,W=200,H=170,r=4,grid=False,ticks=False)
rows=[('Strong',0.5),('Moderate',1.5),('Weak',3)]
grid_='<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px;font-size:15px;text-align:center">'+''.join(
  f'<div class="frag">{mini(cloud(sd,k*7+(3 if ng else 1),ng))}<b>{n.lower()} {"negative" if ng else "positive"}</b></div>' for k,(n,sd) in enumerate(rows) for ng in (False,True))+'</div>'
S.append(learn('Learn · 2E','Strength of an association',
  '<h4>How much scatter?</h4><ul class="bul" style="font-size:18px;line-height:1.45;margin-left:22px"><li><b>strong</b>: tightly clustered about a trend line</li><li><b>moderate</b>: broadly clustered about a trend line</li>'
  '<li><b>weak</b>: loosely clustered about a trend line</li><li>no pattern: <b>no association</b></li></ul>',grid_,
  'Describe in the order direction, form, strength, then outliers: ‘a strong, negative, linear association’.',f'{CAM}, 2E pp. 137–138 (example plots redrawn)',cards=(kcard('Strength','strong · moderate · weak'),)))
# ================= WE15
S.append(qslide('we','Worked example 15 · 2E','Strength of an association',
  'Classify the <span style="font-weight:700">strength</span> of the association in each of the following scatterplots.'
  '<div class="trio" style="margin-top:14px"><div>a'+W_(320,SC(E15A,(5,25),(5,45),5,10,'X','Y',W=340,H=270,r=3.5,fs=12,sid='w15a'))+'</div>'
  '<div>b'+W_(320,SC(E15B,(0,20),(5,25),5,5,'X','Y',W=340,H=270,r=3.5,fs=12,tl=((2,6.9),(20,24)),sid='w15b'))+'</div></div>',
  [],'',f'{CAM} · Example 15 (p. 138; scatterplots redrawn, points approximate)',video='Cambridge GO · Example 15 (2E Resources)',cmd=('Classify',None,'weak, moderate or strong'),
  parts=[('a','The points are loosely clustered. The association is weak.','data-hi="#w15a|p|hy"'),('b','The points are tightly clustered. The association is strong.','data-show="#w15b|tl" data-hi="#w15b|p|hy"')]))
# ================= You try: Edrolo U3&4 2C WE4
S.append(qslide('yt','You try · Edrolo 2C WE4','Strength, direction, form and outliers',
  G('An investigation into the association between sleep and work performance was conducted. The following scatterplot displays the collected data.',
    W_(450,SC(SLEEP,(0,10),(0,12),2,2,'amount of sleep (hours)','number of basic errors',W=480,H=320,r=6,fs=13,tl=((0,10.8),(10,0.3)),sid='y3s')),
    'Describe the relationship in terms of strength, direction, form and potential outliers.'),
  [('Strength','all points appear very close to the underlying trend: strong','data-fill="y33"'),
   ('Direction','as the EV increases, the RV decreases: negative','data-fill="y31"'),
   ('Form','the data best resembles a straight line: linear','data-show="#y3s|tl" data-fill="y32"'),
   ('Outliers','no points clearly lie outside the trend','data-fill="y34"'),
   ('TMPL',dfs('y3',['negative','linear','strong','none visible'],fs=17,concl='The scatterplot displays a strong, negative, linear relationship, with no visible outliers.'),'','data-fill="y35"')],
  '',f'{EDR} · 2C Worked example 4 (p. 136; scatterplot redrawn)',cmd=('Describe',None,'strength, direction, form, outliers')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2018 Exam 2 Q2b','Show what you know',
  G('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.',
    W_(370,SC(V18,(35,70),(35,75),5,5,'morning congestion level (%)','evening congestion level (%)',W=420,H=290,r=4.5,fs=12)),
    'A least squares line is to be fitted to the data with the aim of predicting evening congestion level from morning congestion level.<br>The equation of this line is'
    '<p style="text-align:center;margin:6px 0"><em>evening congestion level</em> = 8.48 + 0.922 × <em>morning congestion level</em></p>Name the response variable in this equation. <span class="muted">(1 mark)</span>'),
  [('Predicting … from …','we predict evening congestion level from morning congestion level'),('Left-hand side','the RV is the one being predicted: on the left of the equation, on the y-axis')],
  'The response variable is <em class="v">evening congestion level</em>.',f'{EDR} · 2C Q15 · VCAA 2018 Further Mathematics Exam 2 Core Q2b (examiner report; original wording; scatterplot redrawn)',stat=('mark',90),cmd=('Name',1,'one variable')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)
TT=('<table class="t" style="font-size:11px"><tr><th>Apparent temperature (°C)</th>'+''.join(f'<td style="padding:2px 3px">{b}</td>' for a,b in V16)+'</tr><tr><th>Actual temperature (°C)</th>'+''.join(f'<td style="padding:2px 3px">{a}</td>' for a,b in V16)+'</tr></table>')
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2016 Exam 2 Q3a','Show what you know',
  '<div style="font-size:16px">The data in the table below shows a sample of actual temperatures and apparent temperatures recorded at the weather station. A scatterplot of the data is also shown.<br>The data will be used to investigate the association between the variables <em class="v">apparent temperature</em> and <em class="v">actual temperature</em>.</div>'
  '<div style="margin:6px 0">'+TT+'</div><div style="display:flex;gap:10px;align-items:center"><div style="width:330px;position:relative">'+SC(V16,(20,29),(16,26),1,1,'actual temperature (°C)','apparent temperature (°C)',W=400,H=280,r=4.5,fs=12,sid='x2s')+
  '<div style="position:absolute;right:24px;bottom:70px;font-size:13px"><i>n</i> = 13<br><i>r</i>² = 0.97</div></div>'
  '<div style="flex:1;font-size:16px">a. Use the scatterplot to describe the association between <em class="v">apparent temperature</em> and <em class="v">actual temperature</em> in terms of strength, direction and form. <span class="muted">(1 mark)</span></div></div>',
  [('Strength','points tightly clustered: strong'),('Direction','trend upwards: positive'),('Form','follows a straight line: linear')],
  'The association is <b>strong, positive and linear</b>.',f'{EDR} · 2C Q16 · VCAA 2016 Further Mathematics Exam 2 Core Q3a (examiner report: common error ‘positively skewed’; original wording)',stat=('mark',78),cmd=('describe',1,'strength, direction, form')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 2 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in('2D','2E') and v.get('url')]))
n=assemble(S,'12MAG · L05 · Scatterplots',os.path.join(ROOT,'lessons','2D-2E slides.html'))
print(n-1,'slides')
