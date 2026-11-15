import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
import math
EDR12='Edrolo General Mathematics Units 1&amp;2'
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l13')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13):
    return f'<table class="t tight" style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def stats(cols,rows,fs=20):
    return (f'<table class="t" style="font-size:{fs}px;margin:10px 0"><tr><th></th>'+''.join(f'<th>{c}</th>' for c in cols)+'</tr>'+
            ''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>')

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}.xs ol.parts>li,.xs ol.parts>li *{font-size:15px!important;line-height:1.3!important}'
   '.tight td,.tight th{padding:2px 5px!important}.c4 .cas2 li{font-size:15px;line-height:1.3}.c4 .ytrow .ytf{height:110px!important;padding:0!important;aspect-ratio:auto!important}</style>']
def cls(c): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide '+c+' T ',1)
import re
# ================= opening
S.append(title(13,'The log transformation',f'{CAM} · 4B The log transformation','L13',
               flow=('Do Now','APK','Learn','Worked examples','You try','CAS','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('Taking the log of one axis','',None),('Worked examples 3–4','→ You try',None),('CAS: log, then fit the line','',None),('Exit tasks','· two VCAA questions','var(--ex)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('log transformation','replace x by log x (or y by log y); log means log<sub>10</sub>'),
  ('log x','compresses the high x-values; y-values unchanged'),
  ('log y','compresses the high y-values; x-values unchanged'),
  ('Undo a log','if log y = k, then y = 10<sup>k</sup>')],
  [('log x line',F('<i>y</i> = <i>a</i> + <i>b</i> × log <i>x</i>'),'the “x” on the CAS is log x'),
   ('log y line',F('log <i>y</i> = <i>a</i> + <i>b</i> × <i>x</i>'),'the “y” on the CAS is log y'),
   ('Undo log y',F('<i>y</i> = 10<sup>log <i>y</i></sup>'),'work out log y first')],
  f'{CAM}, 4B pp. 221–223'))

# ================= Do Now 1: VCAA 2024 NHT E1 Q11 (4A)
BR=[27.18,26.78,25.21,26.44,26.14,20.60,17.55,18.24,15.69,11.35,8.15,7.72]; INC=[2460,5211,9846,12706,15176,16304,17402,20463,20615,23285,23926,24364]
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q11','Review of 4A',
  G('The table below shows the birth rate, in number of births per 1000 people, and the average annual income, in dollars per person, for a sample of 12 countries.<br>A scatterplot displaying the data is also shown.',
    '<div style="display:flex;gap:14px;align-items:center">'+'<table class="t tight" style="font-size:11.5px"><tr><th>birth rate</th><th>income</th><th>birth rate</th><th>income</th></tr>'+''.join(f'<tr><td>{BR[k]}</td><td>{INC[k]:,}</td><td>{BR[k+6]}</td><td>{INC[k+6]:,}</td></tr>'.replace(',',' ') for k in range(6))+'</table>'
    +W_(300,SC(list(zip(INC,BR)),(0,25000),(0,30),5000,5,'income (dollars)','birth rate',W=380,H=220,r=4,fs=10))+'</div>',
    'A squared transformation applied to the variable <em class="v">birth rate</em> can be used to linearise the scatterplot.<br>The equation of the least squares line is<div style="text-align:center">(<em>birth rate</em>)² = 953 − 0.0333 × <em>income</em></div>'
    'Using this equation, the predicted birth rate, in number of births per 1000 people, for a country with an average annual income of $18 500 is closest to'),
  [fx('Substitute','(<em>birth rate</em>)²',F('953 − 0.0333 × ',V('income','18 500')),'336.95'),('Undo the square','<em>birth rate</em> = √336.95 = 18.36…')],
  'The predicted birth rate is about 18.4 births per 1000 people: <b>C</b>.','VCAA 2024 (NHT) General Mathematics Exam 1 Q11–12 stem and Q11 (NHT report: answer only; scatterplot redrawn from the table)',
  mc=['17.7','18.0','18.4','337','113 535'],key='C',stat=('nht',),dis=('D','337 is (birth rate)²: the square root was not taken.')))
cls('xs')
# ================= Do Now 2: VCAA 2024 NHT E1 Q9 (3A)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 NHT Exam 1 Q9','Review of 3A',
  G('The scatterplot below shows the average annual <em class="v">income</em>, in dollars, plotted against <em class="v">life expectancy</em>, in years, for 42 countries in 2020.<br>A least squares line has been fitted to the scatterplot.<br>The coefficient of determination is 0.306.',
    W_(470,SC(LIFE,(55,75),(0,14000),2,2000,'life expectancy (years)','income (dollars)',W=600,H=260,r=4,fs=12,tl=LIFE_TL,tl_hid=False)),
    'The equation of the least squares line is closest to'),
  [('Two points on the line','(55, ≈ 870) and (75, ≈ 8380)'),('Slope','(8380 − 870) ÷ (75 − 55) ≈ 375'),('Check D','−19 750 + 375 × 55 = 875 ✓')],
  'Slope ≈ 375 and the line passes through (55, 875): <b>D</b>.','VCAA 2024 (NHT) General Mathematics Exam 1 Q9–10 stem and Q9 (NHT report: answer only; scatterplot redrawn)',
  mc=['<em>income</em> = −19 000 + 345 × <em>life expectancy</em>','<em>income</em> = −19 250 + 355 × <em>life expectancy</em>','<em>income</em> = −19 500 + 365 × <em>life expectancy</em>',
      '<em>income</em> = −19 750 + 375 × <em>life expectancy</em>','<em>income</em> = −20 000 + 385 × <em>life expectancy</em>'],key='D',stat=('nht',)))
cls('xs')
# ================= Do Now 3: VCAA 2024 NHT E2 Q4a (3A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 NHT Exam 2 Q4a','Review of 3A',
  G('In another study, the heights, in metres, of the highest high tide (<em class="v">HHT</em>) for that day and the lowest low tide (<em class="v">LLT</em>) for that day were recorded in Sydney Harbour for the 31 days of July 2021.<br>A scatterplot of this data is shown below.',
    W_(420,SC(TIDE,(0.2,0.64),(1.2,2.1),0.04,0.1,'LLT (m)','HHT (m)',W=560,H=240,r=4,fs=11)),
    'When a least squares line is fitted to the scatterplot, the equation is found to be:<div style="text-align:center"><em>HHT</em> = 2.19 − 1.08 × <em>LLT</em></div>The coefficient of determination is 0.4709<br>'
    'a. Draw the graph of the least squares line on the scatterplot above. <span class="muted">(1 mark)</span>'),
  [fx('Left end','<em>HHT</em>',F('2.19 − 1.08 × ',V('LLT','0.20')),'1.974'),fx('Right end','<em>HHT</em>',F('2.19 − 1.08 × ',V('LLT','0.64')),'1.499'),('Join','plot (0.20, 1.974) and (0.64, 1.499), rule a line across the data')],
  'Line from (0.20, 1.97) to (0.64, 1.50):'+W_(300,SC(TIDE,(0.2,0.64),(1.2,2.1),0.08,0.2,'LLT','HHT',W=360,H=160,r=3,fs=10,tl=((0.2,1.974),(0.64,1.4988)),tl_hid=False)),
  'VCAA 2024 (NHT) General Mathematics Exam 2 Q4 stem and Q4a (NHT report: no %; scatterplot redrawn)',stat=('nht',),cmd=('Draw',1,'two points from the equation, far apart')))
cls('sm')
# ================= Do Now 4: VCAA 2023 E2 Q1d (3A)
IV=[5.1,4.8,6.5,2.9,3.7,5.7,4.0,2.7,5.5,5.0,3.9,4.1,5.3,3.5,5.3]; VOL=[13.0,11.7,17.4,7.2,10.1,15.6,9.9,7.5,12.7,12.7,10.5,10.8,13.1,8.5,14.2]; WT=[12.9,11.4,17.4,6.8,9.6,15.5,9.7,7.0,12.6,12.5,10.1,10.6,13.0,8.1,14.1]
SZ='large medium large small medium large small small medium medium medium medium large small large'.split()
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q1d','Review of 3A',
  '<div style="font-size:15px">Data was collected to investigate the use of electronic images to automate the sizing of oysters for sale. … The data collected for a sample of 15 oysters is displayed in Table 1.</div>'
  '<b style="font-size:14px">Table 1</b><table class="t tight" id="d4t" style="font-size:11.5px"><tr><th>ID</th><th>Weight (g)</th><th>Volume (cm³)</th><th>Image size (megapixels)</th><th>Size</th></tr>'
  +''.join(f'<tr><td>{i+1}</td><td>{w}</td><td>{v}</td><td>{s}</td><td>{z}</td></tr>' for i,(w,v,s,z) in enumerate(zip(WT,VOL,IV,SZ)))+'</table>'
  '<div style="font-size:15.5px;margin-top:4px">d. A least squares line can also be used to model the association between an oyster’s volume, in cm³, and its electronic image size, in megapixels. In this model, image size is the explanatory variable.<br>'
  'Using data from Table 1, determine the equation of this least squares line. Use the template below to write your answer. Round the values of the intercept and slope to four significant figures. <span class="muted">(2 marks)</span><br>'
  '<div style="text-align:center;margin-top:4px">______ = ______ + ______ × ______</div></div>',
  [('EV and RV','EV: image size (x) · RV: volume (y)','data-hi="#d4t|c2,c3|hy"'),('CAS','Linear Reg: XList image, YList volume'),('Read off','a = 0.002 857… · b = 2.571 4…'),('4 s.f.','0.002 857 (leading zeros don’t count) · 2.571')],
  '<em>volume</em> = <b>0.002 857</b> + <b>2.571</b> × <em>image size</em>','VCAA 2023 General Mathematics Exam 2 Q1 (Table 1; variable list omitted) and Q1d (examiner report: average 1.0/2)',stat=('avg',50),cmd=('determine',2,'EV = x; 4 significant figures')))

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9D #9','Undoing a logarithm',
  '<div style="font-size:28px">Find the number whose logarithm is 2.1567 to one decimal place.</div>',
  [('If log x = k','then x = 10<sup>k</sup>'),('Calculator','10<sup>2.1567</sup> = 143.4…'),('Check','log 143.4 = 2.1565… ✓')],
  'The number is <b>143.4</b>',f'{CAM12} · Ch 9 skills checklist 9D #9 · solution worked for 12MAG',cmd=('Find',None,'10 to the power')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9D #10','The log transformation',
  '<div style="font-size:26px">Complete the following table giving a log<sub>10</sub>(<i>x</i>) transformation, and check that this linearises the data.</div>'
  '<div style="margin:18px 0">'+rowtab([('<i>x</i>','10','100','1000'),('log<sub>10</sub>(<i>x</i>)','','',''),('<i>y</i>','3','6','9')],26).replace('<table','<table id="a2t"')+'</div>',
  [('Take logs','log 10 = 1 · log 100 = 2 · log 1000 = 3','data-hi="#a2t|r1|hy"'),('Slope','each step of 1 in log x adds 3 to y'),('Same slope','the points (log x, y) lie on one line')],
  'log<sub>10</sub>(<i>x</i>) = 1, 2, 3. The slope is 3 each time, so <b>y against log x is linear</b> (<i>y</i> = 3 log<sub>10</sub> <i>x</i>).',f'{CAM12} · Ch 9 skills checklist 9D #10 · solution worked for 12MAG',cmd=('Complete',None,'log each x, then check')))
S.append(qslide('apk','APK · VCAA 2017 Exam 1 Q4 (adapted)','Reading a log scale',
  G('<div style="font-size:24px">The following histogram shows the distribution of log<sub>10</sub>(<em>population</em>) of 12 towns.</div>',
    '<div style="width:440px">'+hist('a3h',{"start":0,"w":1,"v":POPF,"ymax":3,"ystep":1,"tick":1,"xl":"log10(population)","yl":"frequency","h":250,"W":520,"fs":16})+'</div>',
    '<div style="font-size:24px">The median population of these towns is between</div>'),
  [('Median position','12 towns: between the 6th and 7th values'),('Count up','1 + 3 = 4, then 4 + 3 = 7: both are in the 2–3 column'),('Undo the log','10² = 100 and 10³ = 1000')],
  'The median population is between 100 and 1000: <b>C</b>.',f'{EDR12} · 8D Q14 (p. 473), adapted by Edrolo from VCAA 2017 Exam 1 Data analysis Q4 (62% answered the original correctly)',
  mc=['2 and 3','3 and 4','100 and 1000','1000 and 10 000','10 000 and 100 000'],key='C',dis=('A','2 and 3 are log values: undo the log (10²,10³).')))

# ================= Learn
def mini(kind):
    P=[(x,math.log10(x)*0.9+0.05) for x in [1+i*0.9 for i in range(11)]] if kind=='x' else [(x,10**(x)/10.5) for x in [i/10 for i in range(11)]]
    xr=(0,10) if kind=='x' else (0,1); yr=(0,1.05)
    T=[(math.log10(x),y) for x,y in P] if kind=='x' else [(x,math.log10(y*10.5)) for x,y in P]
    a=W_(230,SC(P,xr,yr,(xr[1]-xr[0])/4,0.25,'x','y',W=260,H=190,r=4,fs=10,ticks=False))
    b=W_(230,SC(T,(0,1),(0,1.05),0.25,0.25,*(('log x','y') if kind=='x' else ('x','log y')),W=260,H=190,r=4,fs=10,ticks=False))
    return f'<div style="display:flex;align-items:center;gap:8px">{a}<span class="frag" style="font-size:34px">→</span><div class="frag">{b}</div></div>'
S.append(learn('Learn · 4B','Taking the log of one axis straightens a curve',
  '<h4>The log transformation</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>it <b>compresses</b> the upper end of one axis</li>'
  '<li><b>log x</b>: squeezes the high x-values (y unchanged)</li><li><b>log y</b>: squeezes the high y-values (x unchanged)</li><li>log means log<sub>10</sub></li></ul>',
  '<div style="display:flex;flex-direction:column;gap:6px;align-items:center"><div><b>log x</b> straightens</div>'+mini('x')+'<div class="frag"><b>log y</b> straightens</div><div class="frag">'+mini('y')+'</div></div>',
  'Squared stretches the top of an axis; log squeezes it.',f'{CAM}, 4B p. 221 (diagrams redrawn)',
  cards=(kcard('log x','compresses the high x-values'),kcard('log y','compresses the high y-values'))))
S.append(learn('Learn · 4B','Fitting and using the line',
  '<h4>Same four steps as 4A</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Make a new column: log <i>x</i> (or log <i>y</i>)</li><li>Plot and check it is now linear</li>'
  '<li>Fit the least squares line to the transformed data</li><li>Write it in the variable names, then substitute to predict</li></ol>',
  '<div style="font-size:24px;text-align:center;line-height:2.1"><div class="frag"><em>lifespan</em> = 54.3 + 5.59 × <span style="background:#fff3c4;padding:2px 8px;border-radius:6px">log(<em>GDP</em>)</span></div>'
  '<div class="frag"><span style="background:#bbdefb;padding:2px 8px;border-radius:6px">log(<em>cases</em>)</span> = 1.046 + 0.227 × <em>day</em></div>'
  '<div class="frag" style="font-size:21px">log y on the left? Work out log y, then <b>10<sup>log y</sup></b></div></div>',
  'The x (or y) on the CAS screen is the transformed variable: write log x (or log y) in your equation.',f'{CAM}, 4B pp. 222–223',
  cards=(kcard('log x line','<i>y</i> = <i>a</i> + <i>b</i> log <i>x</i>'),kcard('log y line','log <i>y</i> = <i>a</i> + <i>b x</i>'))))

# ================= WE3 / YT Edrolo 3E WE1b
la,lb=lsq([lg(g) for g in GDP],LIFESPAN)
S.append(qslide('we','Worked example 3 · 4B','Applying the log x transformation',
  G('The general wealth of a country, often measured by its Gross Domestic Product (GDP), is one of several variables associated with lifespan in different countries. However, the association is not linear, as can be seen in the scatterplot below which plots lifespan (in years) against GDP per person (in dollars) for 13 different countries.',
    W_(380,SC(list(zip(GDP,LIFESPAN)),(0,50000),(67,83),10000,2,'GDP','Lifespan (years)',W=480,H=210,r=4,fs=11)),
    'The scatterplot shows that there is a strong positive association between the lifespan and GDP.<br>'
    'a. Apply a log transformation to the variable GDP, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict the lifespan of a country with a GDP of $20 000 per person, giving your answer rounded to one decimal place.'),
  [('Transform','change the x-axis to log(GDP)'),
   ('Check',W_(320,SC([(lg(g),l) for g,l in zip(GDP,LIFESPAN)],(2.5,4.75),(67,83),0.5,2,'log (GDP)','lifespan',W=400,H=170,r=4,fs=10,tl=((2.5,la+2.5*lb),(4.75,la+4.75*lb)),tl_hid=False))+'lifespan against log(GDP) is now linear'),
   ('a','<em>lifespan</em> = 54.3 + 5.59 × log(<em>GDP</em>)'),
   fx('b','<em>lifespan</em>',F('54.3 + 5.59 × log ',V('GDP','20 000')),'78.3')],
  '<b>a</b> <em>lifespan</em> = 54.3 + 5.59 × log(<em>GDP</em>) &nbsp; <b>b</b> 78.3 years',f'{CAM} · Example 3 (pp. 221–222; scatterplots redrawn from the 4B CAS 2 table)',video='Cambridge GO · Example 3 (4B Resources)',cmd=('Apply',None,'log x, then fit the line')))
cls('sm')
S.append(qslide('yt','You try · Edrolo 3E WE1b','Applying the log x transformation',
  G('<div style="font-size:20px">Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <em class="v">distance</em>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.</div>'
    +'<div style="margin:6px 0">'+rowtab([('<i>week</i>',*WEEK),('<i>distance</i> (km)',*DIST)],15)+'</div>',
    W_(330,SC(list(zip(WEEK,DIST)),(0,10),(0,8),1,1,'week','distance (km)',W=420,H=180,r=4,fs=10)),
    '<div style="font-size:20px">b. Apply a log transformation to the variable <em class="v">week</em> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.</div>'),
  [('EV and RV','EV: log<sub>10</sub>(week) · RV: distance'),('CAS','new column logweek = log(week); Linear Reg: XList logweek, YList dist'),('Read off','<i>a</i> = 0.997 · <i>b</i> = 6.971')],
  '<b><em>distance</em> = 0.997 + 6.971 × log<sub>10</sub>(<em>week</em>)</b>',f'{EDR} · 3E Worked example 1b (pp. 208–209)',cmd=('calculate',None,'3 d.p.')))
cls('sm')
# ================= WE4 / YT-4B-4 (written)
ca,cb=lsq(DAY,LCASES)
S.append(qslide('we','Worked example 4 · 4B','Applying the log y transformation',
  G('The numbers of cases of a very infectious disease were recorded over a 12 day period. The association is not linear, as can be seen in the scatterplot below which plots cases against days.',
    W_(360,SC(list(zip(DAY,CASES)),(0,12),(0,7000),2,1000,'day','cases',W=440,H=200,r=4,fs=11)),
    'The scatterplot shows that there is a strong positive association between the number of case and day.<br>'
    'a. Apply a log transformation to the variable cases, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict the cases on day 13.'),
  [('Transform','change the y-axis to log(cases)'),
   ('Check',W_(300,SC(list(zip(DAY,LCASES)),(0,12),(1,4),2,1,'day','log(cases)',W=380,H=160,r=4,fs=10,tl=((0,ca),(12,ca+12*cb)),tl_hid=False))+'log(cases) against day is now linear'),
   ('a','log(<em>cases</em>) = 1.046 + 0.227 × <em>day</em>'),
   fx('b','log(<em>cases</em>)',F('1.046 + 0.227 × ',V('day','13')),'3.997'),('Undo the log','<em>cases</em> = 10<sup>3.997</sup> = 9931')],
  '<b>a</b> log(<em>cases</em>) = 1.046 + 0.227 × <em>day</em> &nbsp; <b>b</b> 9931 cases',f'{CAM} · Example 4 (pp. 222–223; scatterplots redrawn, points approximate)',video='Cambridge GO · Example 4 (4B Resources)',cmd=('Apply',None,'log y, fit, then 10^')))
cls('sm')
S.append(qslide('yt','You try · written for 12MAG (YT-4B-4)','Applying the log y transformation',
  '<div style="font-size:22px">The number of followers of a new social media account was recorded over a 10 week period. The association is not linear.</div><div style="margin:14px 0">'
  +rowtab([('<i>week</i>',*FWEEK),('<i>followers</i>',*FOLL)],20)+'</div>'
  '<div style="font-size:22px">a. Apply a log transformation to the variable followers, and determine the least squares regression line for the transformed data.<br>b. Use the least squares equation to predict the followers in week 11.</div>',
  [('Transform','new column lfoll = log(followers)'),('CAS','Linear Reg: XList week, YList lfoll'),('a','log(<em>followers</em>) = 0.989 + 0.183 × <em>week</em>'),
   fx('b','log(<em>followers</em>)',F('0.989 + 0.183 × ',V('week','11')),'3.002'),('Undo the log','10<sup>3.002</sup> = 1005')],
  '<b>a</b> log(<em>followers</em>) = 0.989 + 0.183 × <em>week</em> &nbsp; <b>b</b> 1005 followers','Written for 12MAG, modelled on Cambridge Example 4 (planner/written-youtrys.json YT-4B-4)',cmd=('Apply',None,'log y, fit, then 10^')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['transformed-lsrl']
S.append(cas('CAS · 4B','Take the log, then fit the least squares line',
  '<p style="font-size:18px">The table shows the lifespan (in years) and GDP (in dollars) of people in 12 countries. The association is non-linear.</p>'
  +rowtab([('Lifespan',*LIFESPAN),('GDP',*[f'{g:,}'.replace(',',' ') for g in GDP])],11.5)+
  '<p style="font-size:17px;margin-top:8px">Using the log x transformation:<br>• linearise the data, and fit a regression line to the transformed data (GDP is the EV)<br>• write its equation in terms of the variables lifespan and GDP rounded to three significant figures.<br>'
  '• use the equation of the regression line to predict the lifespan in a country with a GDP of $20 000, rounded to one decimal place.</p>',
  C['ti'],C['classpad'],'<b><em>lifespan</em> = 54.3 + 5.59 × log(<em>GDP</em>)</b> · $20 000: <b>78.3 years</b>',
  f'{CAM} · 4B CAS 2 (pp. 224–226) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
S[-1]=S[-1].replace('<section class="slide T kcas"','<section class="slide T kcas c4"',1)

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2020 Exam 1 Q14','The log transformation',
  '<div style="font-size:24px">In a study, the association between the <em class="v">number of tasks</em> completed on a test and the <em class="v">time</em> allowed for the test, in hours, was found to be non-linear.<br>'
  'The data can be linearised using a log<sub>10</sub> transformation applied to the variable <em class="v">number of tasks</em>.<br>The equation of the least squares line for the transformed data is'
  '<div style="text-align:center;margin:12px 0">log<sub>10</sub>(<em>number of tasks</em>) = 1.160 + 0.03617 × <em>time</em></div>'
  'This equation predicts that the <em class="v">number of tasks</em> completed when the <em class="v">time</em> allowed for the test is three hours is closest to</div>',
  [fx('Substitute','log(<em>tasks</em>)',F('1.160 + 0.03617 × ',V('time','3')),'1.2685'),('Undo the log','<em>tasks</em> = 10<sup>1.2685</sup> = 18.56…')],
  'About 19 tasks: <b>C</b>.',f'{EDR} · 3E Q10 (p. 217) · VCAA 2020 Exam 1 Q14 (examiner report)',
  mc=['13','16','19','25','26'],key='C',dist=[14,6,74,4,2]))
cls('sm')
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2017 Exam 2 Q4b, Q4ci','The log transformation',
  '<div style="font-size:16px">The following time series plot shows the total area, in hectares, of forest eaten by the caterpillars in a rural area during the period 1900 to 1980. The data used to generate this plot is also given.</div>'
  +W_(330,SC(list(zip(YEAR,AREA)),(1890,1990),(0,400),20,50,'year','area (hectares)',W=440,H=170,r=4,fs=10))
  +rowtab([('year',*YEAR),('area (hectares)',*AREA)],12)+
  '<div style="font-size:16px;margin-top:4px">The association between <em class="v">area</em> of forest eaten by the caterpillars and <em class="v">year</em> is non-linear.<br>A log<sub>10</sub> transformation can be applied to the variable <em class="v">area</em> to linearise the data.</div>'
  +plist([('a','Perform the log<sub>10</sub> transformation to the variable <em>area</em> and determine the equation of the least squares line that can be used to predict log<sub>10</sub>(<em>area</em>) from <em>year</em>. Round the values of the intercept and slope to three significant figures. <span class="muted">(2 marks)</span>'),
         ('b','The least squares line predicts that the log<sub>10</sub>(<em>area</em>) of forest eaten by the caterpillars by the year 2020 will be approximately 2.85. Using this value of 2.85, calculate the expected area of forest that will be eaten by the caterpillars by the year 2020. Round your answer to the nearest hectare. <span class="muted">(1 mark)</span>')]),
  [('a: CAS','new column larea = log(area); Linear Reg: XList year, YList larea'),('a: 3 s.f.','a = −14.396… ≈ −14.4 · b = 0.008 538… ≈ 0.00854'),('b: undo the log','10<sup>2.85</sup> = 707.9…')],'',
  f'{EDR} · 3E Q12a–b (p. 218) · VCAA 2017 Exam 2 Q4b (average 0.9/2) and Q4ci (29% correct) (examiner report); Q4cii was the l09 APK',stat=('avg',45),cmd=('determine',3,'year as given; 3 s.f.; then 10^'),
  parts=[('a','log<sub>10</sub>(<em>area</em>) = −14.4 + 0.00854 × <em>year</em>'),('b','<b>708 hectares</b>')]))
cls('xs')

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 4 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('4B',) and v.get('url')]))
n=assemble(S,'12MAG · L13 · The log transformation',os.path.join(ROOT,'lessons','4B slides.html'))
print(n-1,'slides')
