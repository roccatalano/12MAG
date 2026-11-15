"""Lesson l14 (4C) slides: The reciprocal transformation. Content only; templates in tools/deck/tpl/tpl.py.
Sources (all verbatim; figures redrawn from the printed data):
- Do Now: VCAA 2024 Exam 1 Q11 (59%), VCAA 2025 Exam 1 Q12 (61%), VCAA 2026 Exam 2 Q5g (report not yet released), VCAA 2024 Exam 2 Q3f (average 1/2).
- APK: Cambridge U1&2 Ch 9 skills checklist 9C #5 and 9A #2 (no printed answers: solutions worked for 12MAG).
- Learn: Cambridge U3&4 4C pp. 230-231 (own words; diagrams redrawn).
- Worked examples: Cambridge U3&4 Example 5 (p. 231-232; points read off the plot, close approximation), Example 6 (pp. 232-233; data = CAS 3 table).
- You trys: Edrolo U3&4 3E Worked example 1c (p. 210) · Edrolo U3&4 3D Worked example 4 (pp. 198-199).
- CAS: planner/cas-skills.json 'transformed-lsrl'; data = Cambridge 4C CAS 3 (pp. 233-235).
- Exit: Edrolo U3&4 3E Q11 (p. 217) = VCAA 2018 Further Mathematics Exam 1 Q11 (original wording; 58% correct, examiner report).
Run: python3 tools/deck/l14/build.py"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'
def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:8px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l14')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13,tid=''):
    return f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
FR=lambda n,d:f'<span style="display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1.05;font-size:.9em"><span style="border-bottom:1.5px solid currentColor;padding:0 3px">{n}</span><span style="padding:0 3px">{d}</span></span>'

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}.xs ol.parts>li,.xs ol.parts>li *{font-size:15px!important;line-height:1.3!important}'
   '.tight td,.tight th{padding:2px 5px!important}.c4 .cas2 li{font-size:15px;line-height:1.3}.c4 .ytrow .ytf{height:110px!important;padding:0!important;aspect-ratio:auto!important}</style>']
def cls(c): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide '+c+' T ',1)

# ================= opening
S.append(title(14,'The reciprocal transformation',f'{CAM} · 4C The reciprocal transformation','L14',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','CAS','Exit task')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.4.1','· 4A–4B, about 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 questions','var(--apk)'),
  ('Taking 1 over one axis','',None),('Worked examples 5–6','→ You try',None),('CAS: 1/y, then fit the line','',None),('Exit task','· one VCAA question','var(--ex)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('reciprocal','1 divided by the number: the reciprocal of 4 is 1/4 = 0.25'),
  ('1/x','compresses the high x-values (more than log x); y-values unchanged'),
  ('1/y','compresses the high y-values; x-values unchanged'),
  ('Order reverses','big values become small: 1/2 = 0.5 but 1/10 = 0.1')],
  [('1/x line',F('<i>y</i> = <i>a</i> + <i>b</i> × '+FR('1','<i>x</i>')),'the “x” on the CAS is 1/x'),
   ('1/y line',F(FR('1','<i>y</i>')+' = <i>a</i> + <i>b</i> × <i>x</i>'),'the “y” on the CAS is 1/y'),
   ('Undo 1/y',F('<i>y</i> = 1 ÷ (1/<i>y</i>)'),'work out 1/y first')],
  f'{CAM}, 4C pp. 230–231'))

# ================= Do Now 1: VCAA 2024 E1 Q11 (4B)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q11','Review of 4B',
  G('The number of breeding pairs of a small parrot species has been declining over recent years.<br>The table below shows the number of breeding pairs counted, <em class="v">pairs</em>, and the year number, <em class="v">year</em>, for the last 12 years. A scatterplot of this data is also provided.<br>The association between <em class="v">pairs</em> and <em class="v">year</em> is non-linear.',
    '<div style="display:flex;gap:14px;align-items:center">'+'<table class="t tight" style="font-size:11.5px"><tr><th>year</th><th>pairs</th><th>year</th><th>pairs</th></tr>'+''.join(f'<tr><td>{YR[k]}</td><td>{PAIRS[k]}</td><td>{YR[k+6]}</td><td>{PAIRS[k+6]}</td></tr>' for k in range(6))+'</table>'
    +W_(300,SC(list(zip(YR,PAIRS)),(0,12),(140,340),2,20,'year','pairs',W=380,H=220,r=4,fs=10))+'</div>',
    'The scatterplot can be linearised using a logarithmic (base 10) transformation applied to the explanatory variable.<br>The least squares equation calculated from the transformed data is closest to'),
  [('Which variable?','explanatory variable = <em>year</em>, so the x becomes log<sub>10</sub>(<em>year</em>)'),('Keep pairs','<em>pairs</em> = <i>a</i> + <i>b</i> × log<sub>10</sub>(<em>year</em>): only C or D'),('CAS','Linear Reg: XList log(year), YList pairs → a = 303.4, b = −150.8')],
  '<em>pairs</em> = 303 − 151 × log<sub>10</sub>(<em>year</em>): <b>D</b>.','VCAA 2024 General Mathematics Exam 1 Q11–12 stem and Q11 (examiner report; scatterplot redrawn from the table)',
  mc=['log<sub>10</sub>(<em>pairs</em>) = 2.44 − 0.0257 × <em>year</em>','log<sub>10</sub>(<em>pairs</em>) = 151 − 303 × <em>year</em>','<em>pairs</em> = 274 − 12.3 × log<sub>10</sub>(<em>year</em>)','<em>pairs</em> = 303 − 151 × log<sub>10</sub>(<em>year</em>)'],
  key='D',stat=('mc',59),dis=('A','A applies the log to pairs, the response variable, not to year.')))
cls('xs')
# ================= Do Now 2: VCAA 2025 E1 Q12 (4A)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q12','Review of 4A',
  G('The table below shows the life expectancy in years, <em class="v">life</em>, and the number of doctors per 1000 people, <em class="v">doctors</em>, for a sample of 10 countries in 2024. A scatterplot displaying the data is also shown.',
    '<div style="display:flex;gap:14px;align-items:center">'+'<table class="t tight" style="font-size:11.5px"><tr><th>Doctors</th><th>Life</th><th>Doctors</th><th>Life</th></tr>'+''.join(f'<tr><td>{DOC[k]}</td><td>{LIFE[k]}</td><td>{DOC[k+5]}</td><td>{LIFE[k+5]}</td></tr>' for k in range(5))+'</table>'
    +W_(300,SC(list(zip(DOC,LIFE)),(0,2.5),(60,80),0.5,4,'doctors (number per 1000 people)','life (years)',W=380,H=220,r=4,fs=10))+'</div>',
    'A squared transformation was applied to the variable <em class="v">doctors</em>.<br>The equation of the least squares line fitted to this transformed data is of the form <em>life</em> = <i>a</i> + <i>b</i> × (<em>doctors</em>)².<br>Using this equation, the predicted <em class="v">life</em>, in years, for a country with two <em class="v">doctors</em> per 1000 people is closest to'),
  [('CAS','new column doc2 = doctors²; Linear Reg: XList doc2, YList life'),('Read off','a = 63.12 · b = 2.842'),fx('Substitute','<em>life</em>',F('63.12 + 2.842 × ',V('doctors²','2²')),'74.48')],
  'The predicted life expectancy is about 74.5 years: <b>C</b>.','VCAA 2025 General Mathematics Exam 1 Q11–12 stem and Q12 (examiner report; scatterplot redrawn from the table)',
  mc=['73.6','74.0','74.5','74.9'],key='C',stat=('mc',61)))
cls('xs')
# ================= Do Now 3: VCAA 2026 E2 Q5g (4B)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 Exam 2 Q5g','Review of 4B',
  '<div style="font-size:17px">g. In order to linearise the data relating <em class="v">happiness index</em> and average annual <em class="v">income</em> per person in a country, a logarithmic (base 10) transformation is applied to the <em class="v">income</em> data.<br>'
  'A new data set with values of the <em class="v">happiness index</em> and log<sub>10</sub>(<em>income</em>), per person, for 10 countries is given in the table below.</div>'
  '<div style="margin:6px 0">'+rowtab([('Happiness index',*HAP),('log<sub>10</sub>(<em>income</em>)',*LINC)],14,'d3t')+'</div>'
  '<div style="font-size:17px">A least squares line with <em class="v">happiness index</em> as the response variable and log<sub>10</sub>(<em>income</em>) as the explanatory variable is fitted to this new data set.<br>'
  'Use the data in the table above to find the equation of this least squares line in terms of the variables <em class="v">happiness index</em> and log<sub>10</sub>(<em>income</em>).<br>'
  'Write your answers in the appropriate boxes provided below. Round the numbers representing the intercept and the slope to four significant figures. <span class="muted">(2 marks)</span>'
  '<div style="text-align:center;margin-top:6px"><em>happiness index</em> = ______ + ______ × log<sub>10</sub>(<em>income</em>)</div></div>',
  [('EV and RV','EV: log<sub>10</sub>(income) (x) · RV: happiness index (y)','data-hi="#d3t|r1|hy"'),('CAS','the log is already done: Linear Reg: XList lincome, YList happy'),('Read off','a = −4.069 08… · b = 2.698 90…'),('4 s.f.','−4.069 and 2.699')],
  '<em>happiness index</em> = <b>−4.069</b> + <b>2.699</b> × log<sub>10</sub>(<em>income</em>)','VCAA 2026 General Mathematics Exam 2 Q5g (Q5 stem omitted; 2026 report not yet released)',stat=('new',),cmd=('find',2,'EV = x; 4 significant figures')))
cls('sm')
# ================= Do Now 4: VCAA 2024 E2 Q3f (3C)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q3f','Review of 3C',
  '<div style="font-size:16px">The Olympic gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, is often lower than the best height achieved in other international women’s high jump competitions in that same year.<br>'
  'Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.</div>'
  '<b style="font-size:14px">Table 2</b>'+rowtab([('year',*OYR),('Wgold (m)',*WGOLD),('Wbest (m)',*WBEST)],11.5,'d4t')+
  '<div style="font-size:16px;margin-top:6px">When a least squares line is fitted to the scatterplot, the equation is found to be:<div style="text-align:center"><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em></div>'
  'f. In 1984, the <em class="v">Wbest</em> value was 2.07 m for a <em class="v">Wgold</em> value of 2.02 m.<br>Show that when this least squares line is fitted to the scatterplot, the residual value for this point is 0.0328 <span class="muted">(2 marks)</span></div>',
  [('Find 1984','Wgold = 2.02, Wbest = 2.07','data-hi="#d4t|c4|hy"'),fx('Predicted','<em>Wbest</em>',F('0.300 + 0.860 × ',V('Wgold','2.02')),'2.0372'),('Residual','actual − predicted = 2.07 − 2.0372')],
  'Residual = 2.07 − 2.0372 = <b>0.0328</b>','VCAA 2024 General Mathematics Exam 2 Q3 stem (Table 2; scatterplot and data source omitted) and Q3f (examiner report: average 1.0/2)',stat=('avg',50),cmd=('Show',2,'predicted, then actual − predicted')))
cls('xs')

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9C #5','The 1/x transformation',
  '<div style="font-size:26px">Complete the following table giving a '+FR('1','<i>x</i>')+' transformation, and check that this linearises the data.</div>'
  '<div style="margin:18px 0">'+rowtab([('<i>x</i>','0.5','0.2','0.1'),(FR('1','<i>x</i>'),'','',''),('<i>y</i>','5','35','85')],26,'a1t')+'</div>',
  [('Take 1 over x','1 ÷ 0.5 = 2 · 1 ÷ 0.2 = 5 · 1 ÷ 0.1 = 10','data-hi="#a1t|r1|hy"'),('Slope 1st pair','(35 − 5) ÷ (5 − 2) = 30 ÷ 3 = 10'),('Slope 2nd pair','(85 − 35) ÷ (10 − 5) = 50 ÷ 5 = 10'),('Same slope','the points (1/x, y) lie on one straight line')],
  '1/<i>x</i> = 2, 5, 10. The slope is 10 each time, so <b>y against 1/x is linear</b> (<i>y</i> = −15 + 10 × 1/<i>x</i>).',f'{CAM12} · Ch 9 skills checklist 9C #5 · solution worked for 12MAG',cmd=('Complete',None,'1 ÷ each x, then check')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9A #2','Inverse variation',
  '<div style="font-size:26px">If <i>F</i> is inversely proportional to <i>d</i>, use the following table to find the constant of variation.</div>'
  '<div style="margin:18px 0">'+rowtab([('<i>d</i>','10','20','50'),('<i>F</i>','10','5','2')],26)+'</div>',
  [('Inverse variation','<i>F</i> = <i>k</i> × 1/<i>d</i>, so <i>k</i> = <i>F</i> × <i>d</i>'),('Check','10 × 10 = 5 × 20 = 2 × 50 = 100'),('Link to 4C','F against 1/d is a straight line through the origin')],
  '<i>k</i> = <b>100</b> (<i>F</i> = 100/<i>d</i>)',f'{CAM12} · Ch 9 skills checklist 9A #2 · solution worked for 12MAG',cmd=('find',None,'k = F × d')))

# ================= Learn
def mini(kind):
    if kind=='x':
        P=[(x,1.1-0.9/x) for x in [1+i*0.9 for i in range(11)]]; T=[(1/x,y) for x,y in P]; xr,tx=(0,10),(0,1.05); lab=('1/x','y')
    else:
        P=[(x,1/(1.05-x)/20) for x in [i/12 for i in range(12)]]; T=[(x,1/y/20) for x,y in P]; xr,tx=(0,1),(0,1); lab=('x','1/y')
    yr=(0,1.05) if kind=='x' else (0,max(p[1] for p in P)*1.05); ty=(0,1.05) if kind=='x' else (0,max(p[1] for p in T)*1.05)
    a=W_(230,SC(P,xr,yr,(xr[1]-xr[0])/4,(yr[1])/4,'x','y',W=260,H=190,r=4,fs=10,ticks=False))
    b=W_(230,SC(T,tx,ty,(tx[1])/4,ty[1]/4,*lab,W=260,H=190,r=4,fs=10,ticks=False))
    return f'<div style="display:flex;align-items:center;gap:8px">{a}<span class="frag" style="font-size:34px">→</span><div class="frag">{b}</div></div>'
S.append(learn('Learn · 4C','Taking 1 over one axis straightens a curve',
  '<h4>The reciprocal transformation</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>it <b>compresses</b> the upper end of one axis, even more than log</li>'
  '<li><b>1/x</b>: squeezes the high x-values (y unchanged)</li><li><b>1/y</b>: squeezes the high y-values (x unchanged)</li><li>the <b>order reverses</b>: the biggest value becomes the smallest</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:6px;align-items:center"><div><b>1/x</b> straightens</div>'+mini('x')+'<div class="frag"><b>1/y</b> straightens</div><div class="frag">'+mini('y')+'</div></div>',
  'Because the order reverses, the slope changes sign: a curve going down can become a line going up.',f'{CAM}, 4C pp. 230–231 (diagrams redrawn)',
  cards=(kcard('1/x','compresses the high x-values'),kcard('1/y','compresses the high y-values'))))
S.append(learn('Learn · 4C','Fitting and using the line',
  '<h4>Same four steps as 4A and 4B</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Make a new column: 1/<i>x</i> (or 1/<i>y</i>)</li><li>Plot and check it is now linear</li>'
  '<li>Fit the least squares line to the transformed data</li><li>Write it in the variable names, then substitute to predict</li></ol>',
  '<div style="font-size:24px;text-align:center;line-height:2.1"><div class="frag"><em>weight loss</em> = 0.13 + 5.09 × <span style="background:#fff3c4;padding:2px 8px;border-radius:6px">'+FR('1','<em>length of diet</em>')+'</span></div>'
  '<div class="frag"><span style="background:#bbdefb;padding:2px 8px;border-radius:6px">1/<em>width</em></span> = 0.015 + 0.086 × <em>length</em></div>'
  '<div class="frag" style="font-size:21px">1/y on the left? Work out 1/y, then <b>y = 1 ÷ that</b></div></div>',
  'The x (or y) on the CAS screen is the transformed variable: write 1/x (or 1/y) in your equation.',f'{CAM}, 4C pp. 231–233',
  cards=(kcard('1/x line','<i>y</i> = <i>a</i> + <i>b</i> × 1/<i>x</i>'),kcard('1/y line','1/<i>y</i> = <i>a</i> + <i>b x</i>'))))

# ================= WE5 / YT Edrolo 3E WE1c
S.append(qslide('we','Worked example 5 · 4C','Applying the reciprocal (1/x) transformation',
  G('After embarking on a new healthy eating and exercise plan, Ben recorded his weekly weight loss over a 10 week. The association is not linear, as can be seen in the scatterplot below which plots <em>weekly weight loss</em> in kg against <em>length of diet</em> in weeks.',
    W_(360,SC(list(zip(BWK,LOSS)),(0,10),(0,6),2,1,'length of diet (weeks)','weekly weight loss (kg)',W=440,H=200,r=4,fs=11)),
    'The scatterplot shows that there is a strong negative association between <em>weekly weight loss</em> and <em>length of diet</em>.<br>'
    'a. Apply a reciprocal transformation to the variable <em>length of diet</em>, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict the <em>weekly weight loss</em> in week 11, giving your answer to one decimal place.'),
  [('Transform','change the x-axis to 1/(length of diet)'),
   ('Check',W_(300,SC([(1/w,l) for w,l in zip(BWK,LOSS)],(0,1),(0,6),0.2,1,'1/(length of diet)','weight loss',W=380,H=160,r=4,fs=10,tl=((0.1,0.13+0.509),(1,5.22)),tl_hid=False))+'weight loss against 1/(length of diet) is now linear'),
   ('a','<em>weekly weight loss</em> = 0.13 + 5.09 × 1/<em>length of diet</em>'),
   fx('b','<em>weekly weight loss</em>',F('0.13 + 5.09 ÷ ',V('length','11')),'0.6')],
  '<b>a</b> <em>weekly weight loss</em> = 0.13 + '+FR('5.09','<em>length of diet</em>')+' &nbsp; <b>b</b> 0.6 kg',f'{CAM} · Example 5 (pp. 231–232; scatterplots redrawn, points approximate)',video='Cambridge GO · Example 5 (4C Resources)',cmd=('Apply',None,'1/x, then fit the line')))
cls('sm')
S.append(qslide('yt','You try · Edrolo 3E WE1c','Applying the reciprocal (1/x) transformation',
  G('<div style="font-size:20px">Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <em class="v">distance</em>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.</div>'
    +'<div style="margin:6px 0">'+rowtab([('<i>week</i>',*WEEK),('<i>distance</i> (km)',*DIST)],15)+'</div>',
    W_(330,SC(list(zip(WEEK,DIST)),(0,10),(0,8),1,1,'week','distance (km)',W=420,H=180,r=4,fs=10)),
    '<div style="font-size:20px">c. Apply a reciprocal transformation to the variable <em class="v">week</em> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.</div>'),
  [('EV and RV','EV: 1/week · RV: distance'),('CAS','new column weekrec = 1/week; Linear Reg: XList weekrec, YList dist'),('Read off','<i>a</i> = 7.826 · <i>b</i> = −7.701')],
  '<b><em>distance</em> = 7.826 − 7.701 × '+FR('1','<em>week</em>')+'</b>',f'{EDR} · 3E Worked example 1c (p. 210)',cmd=('calculate',None,'3 d.p.')))
cls('sm')
# ================= WE6 / YT Edrolo 3D WE4
S.append(qslide('we','Worked example 6 · 4C','Applying the reciprocal (1/y) transformation',
  G('A homeware company makes rectangular sticky labels with a variety of lengths and widths.<br>The scatterplot below displays the width (in cm) and length (in cm) of eight of the sticky labels.',
    W_(340,SC(list(zip(LEN,WID)),(3.5,7),(1.5,3.5),0.5,0.5,'Length (cm)','Width (cm)',W=420,H=190,r=4,fs=11)),
    'The scatterplot shows that there is a strong negative association between the width of the sticky labels and their lengths, but it is clearly non-linear.<br>'
    'a. Apply a reciprocal transformation to the variable width, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict the width of a sticky label which is 5 cm long, giving your answer to two decimal places.'),
  [('Transform','change the y-axis to 1/width'),
   ('Check',W_(300,SC([(l,1/w) for l,w in zip(LEN,WID)],(3.5,7),(0.2,0.6),0.5,0.1,'Length (cm)','1/width',W=380,H=160,r=4,fs=10,tl=((3.5,0.015+0.086*3.5),(7,0.015+0.086*7)),tl_hid=False))+'1/width against length is now linear'),
   ('a','1/<em>width</em> = 0.015 + 0.086 × <em>length</em>'),
   fx('b','1/<em>width</em>',F('0.015 + 0.086 × ',V('length','5')),'0.445'),('Undo 1/y','<em>width</em> = 1 ÷ 0.445 = 2.25 cm')],
  '<b>a</b> 1/<em>width</em> = 0.015 + 0.086 × <em>length</em> &nbsp; <b>b</b> 2.25 cm',f'{CAM} · Example 6 (pp. 232–233; scatterplots redrawn from the 4C CAS 3 table)',video='Cambridge GO · Example 6 (4C Resources)',cmd=('Apply',None,'1/y, fit, then 1 ÷')))
cls('sm')
S.append(qslide('yt','You try · Edrolo 3D WE4','Applying the reciprocal (1/y) transformation',
  '<div style="font-size:22px">A class of ten students recorded the time they spent studying for their psychology test. The number of questions they got incorrect are shown in the table.</div><div style="margin:14px 0">'
  +rowtab([('<i>hours studied</i>',*HRS),('<i>questions incorrect</i>',*QI)],20)+'</div>'
  '<div style="font-size:22px">Apply a <i>y</i>-reciprocal transformation ('+FR('1','<i>y</i>')+') and plot the transformed data.</div>',
  [('New column','quesrec = 1/ques'),('Values','0.016, 0.031, 0.043, 0.059, 0.063, 0.071, 0.125, 0.143, 0.2, 0.2'),('Plot','XList hours, YList quesrec (scatter)')],
  'The transformed data is close to linear:'+W_(300,SC([(h,1/q) for h,q in zip(HRS,QI)],(0,7.5),(0,0.22),1,0.06,'hours','quesrec',W=360,H=170,r=4,fs=10)),
  f'{EDR} · 3D Worked example 4 (pp. 198–199)',cmd=('Apply',None,'1 ÷ each y, then plot')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['transformed-lsrl']
S.append(cas('CAS · 4C','Take 1 over y, then fit the least squares line',
  '<p style="font-size:16px">The table shows the length (in cm) and width (in cm) of eight sizes of sticky labels.</p>'
  +rowtab([('Length',*LEN),('Width',*WID)],14)+
  '<p style="font-size:17px;margin-top:8px">Using the 1/y transformation:<br>• linearise the data, and fit a regression line to the transformed data (length is the EV)<br>• write its equation in terms of the variables length and width<br>'
  '• use the equation to predict the width of a sticky label with a length of 5 cm.</p>',
  C['ti'],C['classpad'],'1/<em>width</em> = 0.015 + 0.086 × <em>length</em> · <b>width = 2.25 cm</b>',
  f'{CAM} · 4C CAS 3 (pp. 233–235) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
S[-1]=S[-1].replace('<section class="slide T kcas"','<section class="slide T kcas c4"',1)

# ================= Exit
S.append(qslide('ex','Exit task 1 of 1 · VCAA 2018 Exam 1 Q11','The reciprocal transformation',
  G('<div style="font-size:19px">Freya uses the following data to generate the scatterplot below.</div>'+'<div style="margin:6px 0">'+rowtab([('<i>x</i>',*FX),('<i>y</i>',*FY)],15)+'</div>',
    W_(300,SC(list(zip(FX,FY)),(0,10),(0,120),1,20,'x','y',W=380,H=170,r=4,fs=10)),
    '<div style="font-size:19px">The scatterplot shows that the data is non-linear.<br>To linearise the data, Freya applies a reciprocal transformation to the variable <i>y</i>.<br>She then fits a least squares line to the transformed data.<br>'
    'With <i>x</i> as the explanatory variable, the equation of this least squares line is closest to</div>'),
  [('Which variable?','1/y on the left, x on the right: A, B or C'),('CAS','new column yrec = 1/y; Linear Reg: XList x, YList yrec'),('Read off','a = −0.003 95 · b = 0.0118')],
  '1/<i>y</i> = −0.0039 + 0.012<i>x</i>: <b>A</b>.',f'{EDR} · 3E Q11 (p. 217) · VCAA 2018 Further Mathematics Exam 1 Q11 (original wording; examiner report)',
  mc=[FR('1','<i>y</i>')+' = −0.0039 + 0.012<i>x</i>',FR('1','<i>y</i>')+' = −0.025 + 1.1<i>x</i>',FR('1','<i>y</i>')+' = 7.8 − 0.082<i>x</i>','<i>y</i> = 45.3 + 59.7 × '+FR('1','<i>x</i>'),'<i>y</i> = 59.7 + 45.3 × '+FR('1','<i>x</i>')],key='A',dist=[58,11,21,6,4]))
cls('sm')

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 4 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('4C',) and v.get('url')]))
n=assemble(S,'12MAG · L14 · The reciprocal transformation',os.path.join(ROOT,'lessons','4C slides.html'))
print(n-1,'slides')
