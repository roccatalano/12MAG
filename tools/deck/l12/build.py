"""Lesson l12 (4A) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/4A slides.html
Run: python3 tools/deck/l12/build.py      Screenshots: python3 tools/deck/l12/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- CFAT 1.3.2 (3B-3C) at the start (planner card).
- Do Now: VCAA 2024 NHT Exam 1 Q9-10 stem + Q10 (E; NHT report: answers only) · VCAA 2024 Exam 1 Q9-10 stem + Q10 (C, 73%; A 6 B 11 C 73 D 10) ·
          VCAA 2024 NHT Exam 2 Q4 stem + Q4e (NHT report: no %) · VCAA 2023 Exam 2 Q2 Table 3 stem + Q2bii (average 1.3/2 = 65%; report answer 21% vs 14%).
- APK: Cambridge U1&2 Ch 9 skills checklist 9C #4 (no printed answer: solution worked for 12MAG) · 9A #1 (solution worked for 12MAG).
- Learn: Cambridge Units 3&4 4A pp. 212-214 (own words; diagrams redrawn).
- Worked examples: Cambridge U3&4 Example 1 (pp. 212-213), Example 2 (pp. 213-214; scatterplot points are a close approximation read off the plot).
  You trys: Edrolo U3&4 3D Worked example 2 (p. 193) · Edrolo U3&4 3E Worked example 1a (p. 207).
- CAS: planner/cas-skills.json 'transformed-lsrl'; data = Cambridge 4A CAS 1 (pp. 214-217): height = 1560 - 4.90 x time^2.
- Exits: none (no Edrolo U3&4 exam-practice questions on the squared transformation; planner card note).
- Videos: videos.json (4A MaffsGuru link still blank).
"""
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l12')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13):
    return f'<table class="t tight" style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def stats(cols,rows,fs=20):
    return (f'<table class="t" style="font-size:{fs}px;margin:10px 0"><tr><th></th>'+''.join(f'<th>{c}</th>' for c in cols)+'</tr>'+
            ''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>')

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}.c4 .cas2 li{font-size:15px;line-height:1.3}.c4 .ytrow .ytf{height:110px!important;padding:0!important;aspect-ratio:auto!important}</style>']
# ================= opening
S.append(title(12,'The squared transformation',f'{CAM} · 4A The squared transformation','L12',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','CAS')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.3.2','· 3B–3C, 20 min','#00838F'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 questions','var(--apk)'),
  ('Squaring one axis','',None),('Worked examples 1–2','→ You try',None),('CAS: transform, then fit the line','',None),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.3.2','Residuals and regression analysis','3B–3C',15,'Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))
S.append(keys([
  ('Data transformation','applying a function to one axis (x or y, never both) to straighten (linearise) a curved scatterplot'),
  ('x² transformation','spreads out the high x-values; y-values unchanged'),
  ('y² transformation','spreads out the high y-values; x-values unchanged'),
  ('Prediction','substitute into the transformed line; if y was squared, take the positive square root at the end')],
  [('x² line',F('<i>y</i> = <i>a</i> + <i>b</i> × <i>x</i>²'),'the “x” on the CAS is x²'),
   ('y² line',F('<i>y</i>² = <i>a</i> + <i>b</i> × <i>x</i>'),'the “y” on the CAS is y²'),
   ('Undo y²',F('<i>y</i> = √(<i>y</i>²)'),'keep the positive root')],
  f'{CAM}, 4A pp. 212–214'))

# ================= Do Now 1: VCAA 2024 NHT E1 Q10 (3C)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q10','Review of 2G–3C',
  G('The scatterplot below shows the average annual <em class="v">income</em>, in dollars, plotted against <em class="v">life expectancy</em>, in years, for 42 countries in 2020.<br>A least squares line has been fitted to the scatterplot.<br>The coefficient of determination is 0.306.',
    W_(470,SC(LIFE,(55,75),(0,14000),2,2000,'life expectancy (years)','income (dollars)',W=600,H=260,r=4,fs=12,tl=LIFE_TL,tl_hid=False,sid='d1s')),
    'Which one of the following statements is true?'),
  [('A','0.306 is r², not r: ✗'),('B, C','more points sit below the line · 30.6% IS explained: ✗'),('D','the longest life expectancy (≈ 74.7) is below the line: negative residual ✗','data-hi="#d1s|p|hy"'),
   ('E','54 years is below the smallest life expectancy in the data (≈ 55.5): extrapolation ✓')],
  'Predicting for 54 years is extrapolation: <b>E</b>.','VCAA 2024 (NHT) General Mathematics Exam 1 Q9–10 stem and Q10 (NHT report: answer only; scatterplot redrawn)',
  mc=['The value of the correlation coefficient is 0.306','There are more data points above the least squares line than below.','30.6% of the variation in annual income is not explained by the variation in life expectancy.',
      'The country with the longest life expectancy has a positive residual associated with it.','Using the least squares line to predict the annual income of a country whose citizens have a life expectancy of 54 years is an example of extrapolation.'],key='E',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide xs"',1)
# ================= Do Now 2: VCAA 2024 E1 Q10 (3B)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q10','Review of 3A–3B',
  '<div style="font-size:24px">The least squares equation for the relationship between the average number of male athletes per competing nation, <em class="v">males</em>, and the number of the Summer Olympic Games, <em class="v">number</em>, is'
  '<div style="text-align:center;margin:14px 0"><em>males</em> = 67.5 − 1.27 × <em>number</em></div>'
  'At which Summer Olympic Games will the predicted average number of <em class="v">males</em> be closest to 25.6?</div>',
  [('Substitute','25.6 = 67.5 − 1.27 × <em>number</em>'),('Solve','<em>number</em> = (67.5 − 25.6) ÷ 1.27 = 32.99…'),('Round','closest Games: the 33rd')],
  'The 33rd Summer Olympic Games: <b>C</b>.','VCAA 2024 General Mathematics Exam 1 Q9–10 stem and Q10 (examiner report)',
  mc=['31st','32nd','33rd','34th'],key='C',dist=[6,11,73,10],dis=('B','11% truncated 32.99… to 32 instead of rounding to the closest Games.')))
# ================= Do Now 3: VCAA 2024 NHT E2 Q4e (3B/3C)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 NHT Exam 2 Q4e','Review of 3B',
  G('In another study, the heights, in metres, of the highest high tide (<em class="v">HHT</em>) for that day and the lowest low tide (<em class="v">LLT</em>) for that day were recorded in Sydney Harbour for the 31 days of July 2021.<br>A scatterplot of this data is shown below.',
    W_(420,SC(TIDE,(0.2,0.64),(1.2,2.1),0.04,0.1,'LLT (m)','HHT (m)',W=560,H=240,r=4,fs=11,sid='d3s')),
    'When a least squares line is fitted to the scatterplot, the equation is found to be: <em>HHT</em> = 2.19 − 1.08 × <em>LLT</em><br>'
    'e. In this investigation, the <em class="v">HHT</em> value was 1.81 m for an <em class="v">LLT</em> value of 0.40 m.<br>Show that when this least squares line is fitted to the scatterplot, the residual for this point is 0.052 <span class="muted">(2 marks)</span>'),
  [fx('Predicted','<em>HHT</em>',F('2.19 − 1.08 × ',V('LLT','0.40')),'1.758'),fx('Residual','residual',F(V('actual','1.81'),' − ',V('predicted','1.758')),'0.052')],
  'Residual = 1.81 − 1.758 = <b>0.052</b>','VCAA 2024 (NHT) General Mathematics Exam 2 Q4 stem and Q4e (NHT report: no %; scatterplot redrawn)',stat=('nht',),cmd=('Show',2,'predicted, then actual − predicted')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2023 E2 Q2bii (2B)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q2bii','Review of 2B',
  '<div style="font-size:18px">An oyster farmer has two farms, A and B.<br>She takes a random sample of oysters from each of the farms and has the oysters classified as small, medium or large.<br>The number of oysters of each size is displayed in the two-way table below.</div>'
  '<div style="margin:10px 0"><b>Table 3</b><table class="t" id="d4t" style="font-size:19px"><tr><th>Oyster size</th><th>Farm A</th><th>Farm B</th></tr><tr><td>small</td><td>42</td><td>114</td></tr>'
  '<tr><td>medium</td><td>124</td><td>160</td></tr><tr><td>large</td><td>44</td><td>46</td></tr><tr><th>Total</th><th>210</th><th>320</th></tr></table></div>'
  '<div style="font-size:18px">ii. The farmer believes that farm A has a greater capacity to grow larger oysters than farm B.<br>Does the information in Table 3 support the farmer’s belief? Explain your conclusion by comparing the values of two appropriate percentages.<br>Round these percentages to the nearest whole number. <span class="muted">(2 marks)</span></div>',
  [('Farm A large','44 ÷ 210 × 100 = 20.9… ≈ 21%'),('Farm B large','46 ÷ 320 × 100 = 14.3… ≈ 14%'),('Compare','21% &gt; 14%')],
  '<b>Yes.</b> The percentage of large oysters at farm A (21%) is greater than the percentage of large oysters at farm B (14%).',
  'VCAA 2023 General Mathematics Exam 2 Q2 (Table 3) and Q2bii (examiner report)',stat=('avg',65),cmd=('Explain',2,'compare two %')))

# ================= APK 1: Cambridge U1&2 9C #4
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9C #4','The squared transformation',
  '<div style="font-size:26px">Complete the following table giving an <i>x</i>² transformation, and check that this linearises the data.</div>'
  '<div style="margin:18px 0">'+rowtab([('<i>x</i>','1','2','5'),('<i>x</i>²','','',''),('<i>y</i>','12','27','132')],26).replace('<table','<table id="a1t"')+'</div>',
  [('Square each x','1² = 1 · 2² = 4 · 5² = 25','data-hi="#a1t|r1|hy"'),('Slope 1st pair','(27 − 12) ÷ (4 − 1) = 15 ÷ 3 = 5'),('Slope 2nd pair','(132 − 27) ÷ (25 − 4) = 105 ÷ 21 = 5'),
   ('Same slope','the points (x², y) lie on one straight line')],
  '<i>x</i>² = 1, 4, 25. The slope is 5 each time, so <b>y against x² is linear</b> (<i>y</i> = 7 + 5<i>x</i>²).',f'{CAM12} · Ch 9 skills checklist 9C #4 · solution worked for 12MAG',cmd=('Complete',None,'square x, then check')))
# ================= APK 2: Cambridge U1&2 9A #1
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9A #1','Direct variation',
  '<div style="font-size:26px">The distance (<i>d</i>) travelled by a vehicle is directly proportional to the time (<i>t</i>) taken. Using the information in the following table, find the constant of variation.</div>'
  '<div style="margin:18px 0">'+rowtab([('Time (<i>t</i>)','1','2','3'),('Distance (<i>d</i>)','95','190','285')],26)+'</div>',
  [('Direct variation','<i>d</i> = <i>k</i> × <i>t</i>, so <i>k</i> = <i>d</i> ÷ <i>t</i>'),('Check','95 ÷ 1 = 190 ÷ 2 = 285 ÷ 3 = 95')],
  '<i>k</i> = <b>95</b> (<i>d</i> = 95<i>t</i>)',f'{CAM12} · Ch 9 skills checklist 9A #1 · solution worked for 12MAG',cmd=('find',None,'k = d ÷ t')))

# ================= Learn
def curve(kind):
    import math
    if kind=='x': pts=[(x,1-(x)**2*0.8) for x in [i/10 for i in range(11)]]
    else: pts=[(x,math.sqrt(x)*0.9+0.05) for x in [i/10 for i in range(11)]]
    return pts
def mini(kind,lab):
    P=curve(kind); sq=[(x*x,y) for x,y in P] if kind=='x' else [(x,y*y) for x,y in P]
    a=W_(230,SC(P,(0,1),(0,1.05),0.25,0.25,'x','y',W=260,H=190,r=4,fs=10,ticks=False))
    b=W_(230,SC(sq,(0,1),(0,1.05),0.25,0.25,lab[0],lab[1],W=260,H=190,r=4,fs=10,ticks=False))
    return f'<div style="display:flex;align-items:center;gap:8px">{a}<span class="frag" style="font-size:34px">→</span><div class="frag">{b}</div></div>'
S.append(learn('Learn · 4A','Squaring one axis straightens a curve',
  '<h4>The squared transformation</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>it <b>stretches</b> the upper end of one axis</li>'
  '<li><b>x²</b>: spreads out the high x-values (y unchanged)</li><li><b>y²</b>: spreads out the high y-values (x unchanged)</li><li>use the one that turns the curve into a straight line</li></ul>',
  '<div style="display:flex;flex-direction:column;gap:6px;align-items:center"><div><b>x²</b> straightens</div>'+mini('x',('x²','y'))+'<div class="frag"><b>y²</b> straightens</div><div class="frag">'+mini('y',('x','y²'))+'</div></div>',
  'Transform one axis only: x² or y², never both.',f'{CAM}, 4A p. 212 (diagrams redrawn)',
  cards=(kcard('x² transformation','spreads out the high x-values'),kcard('y² transformation','spreads out the high y-values'))))
S.append(learn('Learn · 4A','Fitting and using the line',
  '<h4>Four steps</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Make a new column: <i>x</i>² (or <i>y</i>²)</li><li>Plot and check it is now linear</li>'
  '<li>Fit the least squares line to the transformed data</li><li>Write it in the variable names, then substitute to predict</li></ol>',
  '<div style="font-size:26px;text-align:center;line-height:2.1"><div class="frag"><em>height</em> = 1560 − 4.90 × <span style="background:#fff3c4;padding:2px 8px;border-radius:6px"><em>time</em>²</span></div>'
  '<div class="frag"><span style="background:#bbdefb;padding:2px 8px;border-radius:6px"><em>yield</em>²</span> = 4.45 + 2.29 × <em>fertiliser</em></div>'
  '<div class="frag" style="font-size:22px">y² on the left? Work out y², then <b>√</b> (keep the positive value)</div></div>',
  'The x (or y) on the CAS screen is the transformed variable: write x² (or y²) in your equation.',f'{CAM}, 4A pp. 213–214',
  cards=(kcard('x² line','<i>y</i> = <i>a</i> + <i>b x</i>²'),kcard('y² line','<i>y</i>² = <i>a</i> + <i>b x</i>'))))

# ================= WE1 / YT Edrolo 3D WE2
ja,jb=lsq([t*t for t in TIME],JUMP)
S.append(qslide('we','Worked example 1 · 4A','Applying the x-squared transformation',
  G('A base jumper leaps from the top of a cliff, 1560 metres above the valley floor. The scatterplot below shows the height (in metres) of the base jumper above the valley floor every second, for the first 10 seconds of the jump.',
    W_(400,SC(list(zip(TIME,JUMP)),(0,10),(1000,1600),1,100,'Time (seconds)','Height (metres)',W=500,H=220,r=4,fs=11,sid='w1s')),
    'A scatterplot shows that there is a strong negative association between the height of the base jumper above the ground and time.<br>'
    'a. Apply a squared transformation to the variable time, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict to the nearest metre the height of the base jumper after 3.4 seconds.'),
  [('Transform','change the time axis to time²: 0, 1, 4, 9, … 100'),
   ('Check',W_(330,SC([(t*t,h) for t,h in zip(TIME,JUMP)],(0,100),(1000,1600),10,100,'time²','height',W=400,H=170,r=4,fs=10,tl=((0,ja),(100,ja+100*jb)),tl_hid=False))+'height against time² is now linear'),
   ('a','<em>height</em> = 1560 − 4.90 × <em>time</em>²'),
   fx('b','<em>height</em>',F('1560 − 4.90 × ',V('time','3.4'),'²'),'1503.4…')],
  '<b>a</b> <em>height</em> = 1560 − 4.90 × <em>time</em>² &nbsp; <b>b</b> 1503 m',f'{CAM} · Example 1 (pp. 212–213; scatterplots redrawn from the CAS 1 data)',video='Cambridge GO · Example 1 (4A Resources)',cmd=('Apply',None,'x², then fit the line')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 3D WE2','Applying the x-squared transformation',
  '<div style="font-size:24px">A scatterplot was constructed from the following data.</div><div style="margin:14px 0">'+rowtab([('<i>x</i>',*EX),('<i>y</i>',*EY)],24).replace('<table','<table id="y1t"')+'</div>'
  '<div style="font-size:24px">Apply an <i>x</i>-squared transformation and plot the transformed data.</div>',
  [('Square each x','9, 16, 25, 36, 49','data-hi="#y1t|r0|hy"'),('Axes','horizontal x² from 0 to 50 · vertical y from 0 to at least 52')],
  'Plot (9, 8), (16, 17), (25, 24), (36, 33), (49, 52):'+W_(300,SC([(x*x,y) for x,y in zip(EX,EY)],(0,50),(0,60),10,10,'x²','y',W=360,H=170,r=4,fs=10)),
  f'{EDR} · 3D Worked example 2 (p. 193)',cmd=('Apply',None,'square x, then plot')))
# ================= WE2 / YT Edrolo 3E WE1a
fa,fb=lsq(FERT,YLD2)
S.append(qslide('we','Worked example 2 · 4A','Applying the y-squared transformation',
  G('In a study of the effectiveness of fertiliser on the yield of strawberry plants, differing amounts of liquid fertiliser (in mL) were given to groups of plants, and their average yield (in kg) measured.',
    W_(360,SC(list(zip(FERT,YLD)),(0,10),(2,6),2,1,'fertiliser (ml)','yield (kg)',W=440,H=200,r=4,fs=11)),
    'A scatterplot shows that there is a strong positive association between the fertiliser and yield.<br>'
    'a. Apply a squared transformation to the variable yield, and determine the least squares regression line for the transformed data.<br>'
    'b. Use the least squares equation to predict the yield of a plant given 6.5 mL of fertiliser, giving your answer to 1 decimal place.'),
  [('Transform','change the y-axis to yield²'),
   ('Check',W_(300,SC(list(zip(FERT,YLD2)),(0,10),(0,30),2,10,'fertiliser','yield²',W=380,H=160,r=4,fs=10,tl=((0,fa),(10,fa+10*fb)),tl_hid=False))+'yield² against fertiliser is now linear'),
   ('a','<em>yield</em>² = 4.45 + 2.29 × <em>fertiliser</em>'),
   fx('b','<em>yield</em>²',F('4.45 + 2.29 × ',V('fertiliser','6.5')),'19.34'),('Undo the square','<em>yield</em> = √19.34 = ±4.4: only the positive value makes sense')],
  '<b>a</b> <em>yield</em>² = 4.45 + 2.29 × <em>fertiliser</em> &nbsp; <b>b</b> 4.4 kg',f'{CAM} · Example 2 (pp. 213–214; scatterplots redrawn, points approximate)',video='Cambridge GO · Example 2 (4A Resources)',cmd=('Apply',None,'y², fit, then √')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
wa,wb=lsq(WEEK,[d*d for d in DIST])
S.append(qslide('yt','You try · Edrolo 3E WE1a','Applying the y-squared transformation',
  G('<div style="font-size:20px">Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <em class="v">distance</em>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.</div>'
    +'<div style="margin:6px 0">'+rowtab([('<i>week</i>',*WEEK),('<i>distance</i> (km)',*DIST)],15)+'</div>',
    W_(330,SC(list(zip(WEEK,DIST)),(0,10),(0,8),1,1,'week','distance (km)',W=420,H=180,r=4,fs=10)),
    '<div style="font-size:20px">a. Apply a squared transformation to the variable <em class="v">distance</em> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.</div>'),
  [('EV and RV','EV: week · RV: (distance)²'),('CAS','new column distsq = dist^2; Linear Reg: XList week, YList distsq'),('Read off',f'<i>a</i> = {wa:.3f} · <i>b</i> = {wb:.3f}')],
  '<b>(<em>distance</em>)² = −1.361 + 6.697 × <em>week</em></b>',f'{EDR} · 3E Worked example 1a (p. 207)',cmd=('calculate',None,'3 d.p.')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['transformed-lsrl']
S.append(cas('CAS · 4A','Transform, then fit the least squares line',
  '<p style="font-size:20px">The table shows the height (in m) of a base jumper for the first 10 seconds of her jump.</p>'
  +rowtab([('Time',*TIME),('Height',*JUMP)],13)+
  '<p style="font-size:19px;margin-top:8px">a Construct a scatterplot displaying height (the RV) against time (the EV).<br>b Apply an x-squared transformation and fit a least squares line to the transformed data.<br>c Use the regression line to predict the height of the base jumper after 3.4 seconds.</p>'
  ,
  C['ti'],C['classpad'],'<b><em>height</em> = 1560 − 4.90 × <em>time</em>²</b> · 3.4 s: <b>1503 m</b>',
  f'{CAM} · 4A CAS 1 (pp. 214–217) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
S[-1]=S[-1].replace('<section class="slide T kcas"','<section class="slide T kcas c4"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 4 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('4A',) and v.get('url')]))
n=assemble(S,'12MAG · L12 · The squared transformation',os.path.join(ROOT,'lessons','4A slides.html'))
print(n-1,'slides')
