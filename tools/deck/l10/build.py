"""Lesson l10 (3B) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/3B slides.html
Run: python3 tools/deck/l10/build.py      Screenshots: python3 tools/deck/l10/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- Do Now: VCAA 2023 Exam 1 Q7 (+ Q7-8 stem; A, 60%; A 60 B 15 C 6 D 7 E 12) · VCAA 2025 NHT Exam 1 Q2 (C; NHT report: answers only) ·
          VCAA 2023 Exam 2 Q3 stem + Q3a (40% full marks) · VCAA 2023 Exam 2 Q2a stem + Q2aii (84% full marks; the report, not the index's 80%).
- APK: Cambridge U1&2 Ch 7 skills checklist 7E #9 and #10 (data: 7A #2 height/foot length, as l09 APK 1; solutions worked for 12MAG) ·
       VCAA 2018 Further Exam 1 Q8 (= Edrolo U1&2 6D Q12; original wording; D, 46%; A 16 B 25 C 8 D 46 E 5) ·
       VCAA 2019 Further Exam 2 Q5a (= Edrolo U1&2 6D Q13; original wording; 44%).
- Learn: Cambridge Units 3&4 3B pp. 179-184 (own words).
- Worked examples: Cambridge U3&4 Examples 3, 4 (pp. 181-182), 5 (pp. 183-184). You trys: Edrolo U3&4 3B Worked example 1 (p. 169-170),
  Worked example 2 (p. 171) · YT-3B-5 (planner/written-youtrys.json, written for 12MAG).
- CAS: planner/cas-skills.json 'lsrl-predict'; data = Cambridge 3B car ages and prices (p. 180), prediction from Example 4.
- Exits: Edrolo U3&4 3B Q11 = VCAA 2019 Further Exam 2 Q5c (Edrolo's adapted wording: the original refers to part b, so the 1025 hPa
  prediction is written into the question; 87%) · 3B Q12 = VCAA 2018 Further Exam 2 Q2c (original wording; 78%; 63.8%) ·
  3B Q13 = VCAA 2017 Further Exam 2 Q3bii (original wording; 39%).
- Videos: videos.json (3B).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
YTW={y['id']:y for y in json.load(open(os.path.join(ROOT,'planner','written-youtrys.json')))['items']}
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l10')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13):
    return f'<table class="t tight" style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def seg(rid,cfg,stepped=False,ax=False): return f'<div class="chart{" noax" if ax else ""}" id="{rid}" data-chart="seg" data-cfg=\'{J(cfg)}\'{" data-stepped=\"1\"" if stepped else ""}{" data-axhide" if ax else ""}></div>'

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}</style>']
# ================= opening
S.append(title(10,'Interpreting and using the least squares line',f'{CAM} · 3B Using the least squares regression line to model a relationship','L10').replace('font-size:84px','font-size:64px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· four Year 11 questions','var(--apk)'),
  ('Slope, intercept, predictions, r²','',None),('Worked examples 3–5','→ You try',None),('CAS: predicting from the line','',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Slope (b)','on average, the RV changes by <i>b</i> for each one-unit increase in the EV'),
  ('Intercept (a)','on average, the value of the RV when the EV is 0 (can be meaningless if 0 is far outside the data)'),
  ('Interpolation','predicting inside the range of the EV data: reliable'),
  ('Extrapolation','predicting outside the range of the EV data: unreliable')],
  [('Least squares line',F('<i>y</i> = <i>a</i> + <i>b</i><i>x</i>'),'a = intercept · b = slope'),
   ('Prediction',F('RV = <i>a</i> + <i>b</i> × (EV value)'),'substitute, then check the data range'),
   ('Coefficient of determination',F('<i>r</i>² × 100%'),'% of variation in the RV explained by the EV'),
   ('Predictive power','<i>r</i>² &gt; 30%: good','Cambridge guide')],
  f'{CAM}, 3B pp. 180–183'))

# ================= Do Now 1: VCAA 2023 E1 Q7 (3A)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q7','Review of 3A',
  G('A teacher analysed the class marks of 15 students who sat two tests.<br>The <em class="v">test 1 mark</em> and <em class="v">test 2 mark</em>, all whole number values, are shown in the scatterplot below.<br>A least squares line has been fitted to the scatterplot.',
    W_(400,SC(TESTS,(14,38),(14,50),2,4,'test 1 mark','test 2 mark',W=500,H=290,r=4.5,fs=12,tl=((14,-6.83+1.55*14),(36.6,-6.83+1.55*36.6)),tl_hid=False,sid='d1s')),
    'The equation of the least squares line is closest to'),
  [('Two points on the line','(16, 18) and (36, 49): both sit on the line','data-hi="#d1s|p0,p14|hy"'),
   fx('Slope','<i>b</i>',F(FR([V('y₂','49'),' − ',V('y₁','18')],[V('x₂','36'),' − ',V('x₁','16')])),'31 ÷ 20 = 1.55'),
   fx('Intercept','<i>a</i>',F(V('y','18'),' − ',V('b','1.55'),' × ',V('x','16')),'−6.8')],
  '<em>test 2 mark</em> = −6.83 + 1.55 × <em>test 1 mark</em>: <b>A</b>.','VCAA 2023 General Mathematics Exam 1 Q7–8 stem and Q7 (examiner report; scatterplot redrawn)',
  mc=['<em>test 2 mark</em> = −6.83 + 1.55 × <em>test 1 mark</em>','<em>test 2 mark</em> = 15.05 + 0.645 × <em>test 1 mark</em>','<em>test 2 mark</em> = −6.78 + 0.645 × <em>test 1 mark</em>',
      '<em>test 2 mark</em> = 1.36 + 1.55 × <em>test 1 mark</em>','<em>test 2 mark</em> = 6.83 + 1.55 × <em>test 1 mark</em>'],key='A',dist=[60,15,6,7,12],
  dis=('E','12% dropped the negative sign on the intercept: the line crosses x = 0 below zero.')))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide xs"',1)
# ================= Do Now 2: VCAA 2025 NHT E1 Q2 (1B)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 NHT Exam 1 Q2','Review of 1B',
  G('Passengers on a tram were surveyed for reasons why they travelled by tram. Each reason, along with the percentage of surveyed passengers who gave that reason, is displayed in the segmented bar chart below.',
    '<div style="width:380px">'+seg('d2g',{"bars":[{"v":[22,26,20,14,18]}],"names":["less stress","lower cost","parking problems","no car","near tram stop"],"legendTop":["near tram stop","no car","parking problems","lower cost","less stress"],"yl":"percentage","ticks":20,"h":230})+'</div>',
    'The combined percentage of surveyed passengers who gave the reason ‘lower cost’ or ‘no car’ is closest to'),
  [('lower cost','from 22 to 48: 48 − 22 = 26%'),('no car','from 68 to 82: 82 − 68 = 14%'),('Combined','26 + 14 = 40%')],
  '40%: <b>C</b>.','VCAA 2025 NHT General Mathematics Exam 1 Q2 (NHT report: answers only; chart redrawn, segment heights read off the grid)',
  mc=['14%','26%','40%','66%'],key='C',stat=('nht',)))
# ================= Do Now 3: VCAA 2023 E2 Q3a (3A)
ia,ib=0.1404,0.0024
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q3a','Review of 3A',
  G('The scatterplot below plots the average monthly ice cream <em class="v">consumption</em>, in litres/person, against average monthly <em class="v">temperature</em>, in °C. The data for the graph was recorded in the Northern Hemisphere.',
    W_(400,SC(ICE,(-10,25),(0.10,0.22),5,0.02,'temperature (°C)','consumption (litres/person)',W=520,H=250,r=4.5,fs=12)),
    'When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>consumption</em> = 0.1404 + 0.0024 × <em>temperature</em><br>The coefficient of determination is 0.7212<br>'
    'a. Draw the least squares line on the scatterplot graph above. <span class="muted">(1 mark)</span>'),
  [fx('Left end','<i>y</i>',F('0.1404 + 0.0024 × ',V('x','−10')),'0.1164'),fx('Right end','<i>y</i>',F('0.1404 + 0.0024 × ',V('x','25')),'0.2004'),
   ('Rule','plot (−10, 0.1164) and (25, 0.2004) and rule a line across the whole graph')],
  'Line from (−10, 0.116) to (25, 0.200):'+W_(330,SC(ICE,(-10,25),(0.10,0.22),5,0.02,'','',W=420,H=190,r=4,fs=10,tl=((-10,ia-10*ib),(25,ia+25*ib)),tl_hid=False)),
  'VCAA 2023 General Mathematics Exam 2 Q3 stem and Q3a (examiner report: many students plotted correct points but the line was not accurate; scatterplot redrawn)',stat=('mark',40),cmd=('Draw',1,'two points far apart')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2023 E2 Q2aii (1B)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q2aii','Review of 1B',
  '<div style="font-size:21px">a. The following data shows the sizes of a sample of 20 oysters rated as small, medium or large.</div>'
  '<div style="margin:6px 0">'+rowtab([('','small','small','large','medium','medium'),('','medium','large','small','medium','medium'),('','small','medium','small','small','medium'),('','medium','medium','medium','small','large')],14).replace('<th></th>','')+'</div>'
  '<div style="font-size:19px">Table 2</div>'+'<table class="t tight" style="font-size:15px"><tr><th>Size</th><th>Number</th><th>Percentage (%)</th></tr><tr><td>small</td><td>7</td><td>35</td></tr><tr><td>medium</td><td>10</td><td>50</td></tr><tr><td>large</td><td>3</td><td>15</td></tr><tr><td>Total</td><td>20</td><td>100</td></tr></table>'
  '<div style="font-size:21px;margin-top:6px">ii. Use the percentages in Table 2 to construct a percentage segmented bar chart below. A key has been provided. <span class="muted">(1 mark)</span></div>',
  [('Bottom segment','small: 0 to 35'),('Middle segment','medium: 35 to 35 + 50 = 85'),('Top segment','large: 85 to 100')],
  'One bar, segments at 35 and 85:<div style="width:380px;margin:4px auto">'+seg('d4g',{"bars":[{"v":[35,50,15],"label":"size"}],"names":["small","medium","large"],"legendTop":["large","medium","small"],"yl":"percentage (%)","ticks":10,"h":300})+'</div>',
  'VCAA 2023 General Mathematics Exam 2 Q2a stem and Q2aii (examiner report: well done; Table 2 shown with the Number column completed, as after part i)',stat=('mark',84),cmd=('construct',1,'stack the percentages')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK
fa,fb=lsq([p[0] for p in FOOT],[p[1] for p in FOOT])
FT='<table class="t tight" style="font-size:13px"><tr><th><i>height</i></th>'+''.join(f'<td>{h}</td>' for h,_ in FOOT)+'</tr><tr><th><i>foot length</i></th>'+''.join(f'<td>{f}</td>' for _,f in FOOT)+'</tr></table>'
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7E #9','Interpreting slope and intercept',
  f'<div style="font-size:21px">Height (<em class="v">height</em>) and foot length (<em class="v">foot length</em>) of 16 students, in centimetres:</div><div style="margin:10px 0">{FT}</div>'
  f'<div style="font-size:21px">Least squares line: <em>foot length</em> = {fa:.2f} + {fb:.2f} × <em>height</em><br><br>Interpret the intercept and slope of the regression line relating height and foot length in terms of these variables.</div>',
  [('EV and RV','EV height, RV foot length'),('Slope',f'<i>b</i> = {fb:.2f}: change in foot length per 1 cm of height'),
   ('Intercept',f'<i>a</i> = {fa:.2f}: foot length when height = 0 cm, far outside the data (153–185 cm)')],
  f'<b>Slope:</b> on average, foot length increases by {fb:.2f} cm for each 1 cm increase in height.<br><b>Intercept:</b> on average, a person of height 0 cm would have a foot length of {fa:.2f} cm: this has no practical meaning.',
  f'{CAM12} · Ch 7 skills checklist 7E #9 (data: 7A #2; least squares line from 7D #8) · solution worked for 12MAG',cmd=('Interpret',None,'both variables, “on average”')))
S[-1]=S[-1].replace('<section class="slide T apk"','<section class="slide T apk sm"',1)
p160,p100=fa+fb*160,fa+fb*100
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7E #10','Interpolation and extrapolation',
  f'<div style="font-size:23px"><em>foot length</em> = {fa:.2f} + {fb:.2f} × <em>height</em> (heights in the data: 153 cm to 185 cm)<br><br>'
  'Use the linear model line relating height and foot length to predict the foot length of people with the following heights, indicating in each whether you are interpolating or extrapolating. Give your answers rounded to one decimal place.'
  '<div style="margin-top:12px">a&nbsp;&nbsp; 160 cm tall &nbsp;&nbsp;&nbsp;&nbsp; b&nbsp;&nbsp; 100 cm tall</div></div>',
  [fx('a','<em>foot length</em>',F(f'{fa:.2f} + {fb:.2f} × ',V('height','160')),f'{p160:.1f} cm'),('a: in range?','160 is inside 153–185: interpolation'),
   fx('b','<em>foot length</em>',F(f'{fa:.2f} + {fb:.2f} × ',V('height','100')),f'{p100:.1f} cm'),('b: in range?','100 is outside 153–185: extrapolation')],
  f'a {p160:.1f} cm, interpolating · b {p100:.1f} cm, extrapolating',
  f'{CAM12} · Ch 7 skills checklist 7E #10 (data: 7A #2) · solution worked for 12MAG (full-precision line)',cmd=('predict',None,'substitute, then check range')))
S.append(qslide('apk','APK · Year 11 · VCAA 2018 Exam 1 Q8','Equation from a line on a scatterplot',
  G('The scatterplot below displays the <em class="v">resting pulse rate</em>, in beats per minute, and the <em class="v">time spent exercising</em>, in hours per week, of 16 students. A least squares line has been fitted to the data.',
    W_(360,SC(PULSE,(1,11),(56,68),1,1,'time spent exercising (hours per week)','resting pulse rate',W=460,H=270,r=4.5,fs=11,tl=((1,68.3-1.1),(11,68.3-11.0)),tl_hid=False,sid='a3s')),
    'The equation of this least squares line is closest to'),
  [('Direction','the line slopes down: negative slope (E ✗)'),('Slope','line falls 11 beats (67.2 → 56.2) as time goes from 1 to 11 hours: −11 ÷ 10 = −1.10'),
   ('Intercept','the axis starts at 1, not 0: at 0 hours the line is at 67.2 + 1.10 = 68.3')],
  '<em>resting pulse rate</em> = 68.3 − 1.10 × <em>time spent exercising</em>: <b>D</b>.',
  f'{EDR12} · 6D Q12 · VCAA 2018 Further Mathematics Exam 1 Q8 (examiner report; original wording; scatterplot redrawn)',
  mc=['<em>resting pulse rate</em> = 67.2 – 0.91 × <em>time spent exercising</em>','<em>resting pulse rate</em> = 67.2 – 1.10 × <em>time spent exercising</em>','<em>resting pulse rate</em> = 68.3 – 0.91 × <em>time spent exercising</em>',
      '<em>resting pulse rate</em> = 68.3 – 1.10 × <em>time spent exercising</em>','<em>resting pulse rate</em> = 67.2 + 1.10 × <em>time spent exercising</em>'],key='D',dist=[16,25,8,46,5],
  dis=('B','25% read the intercept where the line meets the vertical axis, but that axis is at 1 hour, not 0.')))
S[-1]=S[-1].replace('<section class="slide T apk mcslide"','<section class="slide T apk mcslide xs"',1)
S.append(qslide('apk','APK · Year 11 · VCAA 2019 Exam 2 Q5a','Interpreting the slope',
  G('The scatterplot below shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<em class="v">pressure 3 pm</em>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<em class="v">pressure 9 am</em>) for 23 days in November 2017 at a particular weather station.',
    W_(330,SC(PRESS,(1010,1030),(1010,1030),5,5,'pressure 9 am (hPa)','pressure 3 pm (hPa)',W=400,H=250,r=4,fs=11,tl=((1010.4,111.4+0.8894*1010.4),(1030,111.4+0.8894*1030)),tl_hid=False)),
    'A least squares line has been fitted to the scatterplot as shown.<br>The equation of this line is <em>pressure 3 pm</em> = 111.4 + 0.8894 × <em>pressure 9 am</em><br>'
    'a. Interpret the slope of this least squares line in terms of the atmospheric pressure at this weather station at 9 am and at 3 pm. <span class="muted">(1 mark)</span>'),
  [('EV and RV','EV pressure 9 am · RV pressure 3 pm'),('Slope','<i>b</i> = 0.8894: change in RV for each <b>one-unit</b> increase in EV')],
  'On average, pressure at 3 pm increases by 0.8894 hPa for each one unit (hPa) increase in pressure at 9 am.',
  f'{EDR12} · 6D Q13 · VCAA 2019 Further Mathematics Exam 2 Core Q5a (examiner report: many left out the one-unit increase; original wording; scatterplot redrawn)',stat=('mark',44),cmd=('Interpret',1,'“on average … for each one-unit increase”')))
S[-1]=S[-1].replace('<section class="slide T apk"','<section class="slide T apk sm"',1)

# ================= Learn
CARP=W_(420,SC(CARS,(0,10),(0,40000),1,5000,'Age (years)','Price (dollars)',W=520,H=280,r=4.5,fs=11,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False))
S.append(learn('Learn · 3B','Interpreting the slope and intercept',
  '<h4>For <i>y</i> = <i>a</i> + <i>bx</i></h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>slope b</b>: on average, <i>y</i> increases/decreases by <i>b</i> for each one-unit increase in <i>x</i></li>'
  '<li><b>intercept a</b>: on average, the value of <i>y</i> when <i>x</i> = 0</li><li>the intercept can be meaningless if <i>x</i> = 0 is outside the data</li></ul>'
  '<p style="font-size:18px">Cars: <em>price</em> = 35 100 − 3940 × <em>age</em></p>',
  CARP,'Always say “on average” and use both variable names with their units.',f'{CAM}, 3B pp. 179–181 (scatterplot redrawn)',
  cards=(kcard('Slope (b)','change in RV per 1-unit increase in EV'),kcard('Intercept (a)','RV when EV = 0'))))
S.append(learn('Learn · 3B','Predictions: interpolation and extrapolation',
  '<h4>Making a prediction</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Substitute the EV value into the equation</li><li>Check: is the EV value inside the data range?</li></ol>'
  '<ul class="bul" style="font-size:18px;margin-left:22px"><li>inside → <b>interpolation</b>: reliable</li><li>outside → <b>extrapolation</b>: unreliable (assumes the trend continues)</li></ul>',
  '<table class="t" style="font-size:20px"><tr><th>Car age</th><th>Predicted price</th><th>Type</th></tr>'
  '<tr class="frag"><td>2 years</td><td>35 100 − 3940 × 2 = $27 220</td><td>interpolation</td></tr>'
  '<tr class="frag"><td>7 years</td><td>35 100 − 3940 × 7 = $7520</td><td>interpolation</td></tr>'
  '<tr class="frag"><td>12 years</td><td>35 100 − 3940 × 12 = −$12 180</td><td><b>extrapolation</b>: a negative price!</td></tr></table>',
  'Data range = smallest to largest value of the <b>EV</b> (here 1 to 8 years).',f'{CAM}, 3B pp. 182–183',
  cards=(kcard('Interpolation','inside the EV data range'),kcard('Extrapolation','outside the EV data range'))))
S.append(learn('Learn · 3B','The coefficient of determination',
  '<h4>r² in a regression</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li><i>r</i>² × 100% = % of the variation in the RV explained by the variation in the EV</li>'
  '<li>a measure of the line’s <b>predictive power</b></li><li>guide: <i>r</i>² &gt; 30% → good predictive power</li><li>to compare two EVs: the bigger <i>r</i>² explains more</li></ul>',
  '<div style="font-size:26px;text-align:center;line-height:1.9"><div class="frag"><i>r</i> = −0.9643</div><div class="frag"><i>r</i>² = (−0.9643)² = 0.930 = <b>93.0%</b></div>'
  '<div class="frag" style="font-size:21px;background:#e8f5e9;padding:8px 14px;border-radius:8px">93% of the variation in <em>price</em> of the second-hand cars can be explained by the variation in their <em>age</em>.</div></div>',
  'Square r first, then turn it into a percentage; a negative r still gives a positive r².',f'{CAM}, 3B p. 183',
  cards=(kcard('Coefficient of determination','<i>r</i>² × 100%'),)))

# ================= WE3 / YT Edrolo WE1
S.append(qslide('we','Worked example 3 · 3B','Interpreting the slope and intercept of a regression line',
  G('<div style="font-size:21px">The equation of a regression line that enables the price of a second-hand car to be predicted from its age is:<div style="text-align:center;margin:6px 0"><em>price</em> = 35 100 − 3940 × <em>age</em></div></div>',
    W_(330,SC([],(0,10),(0,45000),1,5000,'Age (years)','Price (dollars)',W=420,H=210,r=4,fs=10,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False)))
  +plist([('a','Interpret the slope in terms of the variables price and age.'),('b','Interpret the intercept in terms of the variables price and age.')]),
  [('Slope','<i>b</i> = −3940: change in price for each 1-year increase in age; negative → decrease'),('Intercept','<i>a</i> = 35 100: price when age = 0, i.e. when the car is new')],'',
  f'{CAM} · Example 3 (p. 181)',video='Cambridge GO · Example 3 (3B Resources)',cmd=('Interpret',None,'slope, then intercept'),
  parts=[('a','On average, for each additional year of age the price of these cars decreases by $3940.'),('b','On average, the price of these cars when new was $35 100.')]))
S.append(qslide('yt','You try · Edrolo 3B WE1','Interpreting the slope and intercept',
  G('<div style="font-size:20px">The heights of a group of children aged between one and six years old were measured.<br>The scatterplot and regression equation show the relationship between <em class="v">height</em> (cm) and <em class="v">age</em> (years).<br>Based on the regression equation, <em>height</em> = 58.22 + 10.46 × <em>age</em></div>',
    W_(330,SC(KIDS,(0,7),(50,130),1,10,'age (years)','height (cm)',W=420,H=210,r=4,fs=10,tl=((0,58.22),(6.9,58.22+10.46*6.9)),tl_hid=False)))
  +plist([('a','How much on average does a child grow each year, correct to two decimal places?'),('b','Interpret the <i>y</i>-intercept in this regression equation.')]),
  [('a: which part?','growth per year = change in height per 1-year increase in age: the slope, <i>b</i> = 10.46'),('b: intercept','<i>a</i> = 58.22: height when age = 0, i.e. at birth')],'',
  f'{EDR} · 3B Worked example 1 (pp. 169–170) · scatterplot redrawn',cmd=('Interpret',None,'which coefficient?'),
  parts=[('a','On average, a child grows 10.46 cm each year.'),('b','On average, the height of children when they are born is 58.22 cm.')]))
# ================= WE4 / YT Edrolo WE2
S.append(qslide('we','Worked example 4 · 3B','Using the regression line to make predictions',
  G('<div style="font-size:22px">The equation of a regression line that enables the price of a second-hand car to be predicted from its age is:<div style="text-align:center;margin:8px 0"><em>price</em> = 35 100 − 3940 × <em>age</em></div>Use this equation to predict the price of a car that is 5.5 years old.</div>',
    W_(360,SC([],(0,10),(0,40000),1,5000,'Age (years)','Price (dollars)',W=440,H=230,r=4,fs=10,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False))),
  [('By eye','up from age = 5.5 to the line, across to the price axis: about $14 000'),
   fx('More accurate','<em>price</em>',F('35 100 − 3940 × ',V('age','5.5')),'$13 430')],
  'The predicted price is <b>$13 430</b>.',f'{CAM} · Example 4 (pp. 181–182)',video='Cambridge GO · Example 4 (3B Resources)',cmd=('predict',None,'substitute the EV')))
S.append(qslide('yt','You try · Edrolo 3B WE2','Predicting from a regression line',
  G('<div style="font-size:19px">A ski hire shop has recorded the daily <em class="v">snowfall</em> (cm) and the corresponding <em class="v">number of customers</em> that hire from them. The relationship between <em>number of customers</em> and <em>snowfall</em> is displayed on the scatterplot.</div>',
    W_(360,SC(SKI,(0,10),(0,90),1,10,'snowfall (cm)','number of customers',W=440,H=220,r=4,fs=10,tl=((0,14),(10,87)),tl_hid=False,sid='y4s')))
  +plist([('a','What is the predicted <em>number of customers</em> when there is 5 cm of <em>snowfall</em>? Is this interpolation or extrapolation?'),('b','How many customers are expected to hire from the ski hire shop when there is no snowfall?')]),
  [('a: range','snowfall in the data: 1 to 9 cm; 5 is inside: interpolation'),('a: read off','up from 5 to the line, across: 50 customers'),
   ('b: snowfall = 0','the <i>y</i>-intercept, just below 15 (outside the data: extrapolation)')],'',
  f'{EDR} · 3B Worked example 2 (p. 171) · scatterplot redrawn',cmd=('predict',None,'read off the line'),
  parts=[('a','50 customers; interpolation'),('b','About 14 customers')]))
# ================= WE5 / YT-3B-5
S.append(qslide('we','Worked example 5 · 3B','Using the coefficient of determination to compare associations',
  '<div style="font-size:22px">In a recent study across a number of countries the correlation between educational attainment and the amount spent on education was found to be 0.26, whilst the correlation between educational attainment and the student : teacher ratio was found to be −0.38.</div>'
  +plist([('a','Find the values of the coefficient of determination between educational attainment and the amount spent on education, and student : teacher ratio respectively.'),
          ('b','Which of the variables, amount spent on education or student : teacher ratio is more important in explaining the variation in educational attainment?')]),
  [fx('Amount spent','<i>r</i>²',F(V('r','0.26'),'²'),'6.8%'),fx('Student : teacher ratio','<i>r</i>²',F('(',V('r','−0.38'),')²'),'14.4%'),('Compare','14.4% &gt; 6.8%')],'',
  f'{CAM} · Example 5 (pp. 183–184)',video='Cambridge GO · Example 5 (3B Resources)',cmd=('Find',None,'square r, then compare'),
  parts=[('a','amount spent on education: <i>r</i>² = 0.26² = 6.8% · student : teacher ratio: <i>r</i>² = (−0.38)² = 14.4%'),
         ('b','The variable student : teacher ratio explains 14.4% of the variation in educational attainment, making it a more important explanatory variable than the amount spent on education which explains only 6.8%.')]))
y5=YTW['YT-3B-5']
S.append(qslide('yt','You try · written for 12MAG (YT-3B-5)','Comparing associations with r²',
  '<div style="font-size:22px">In a recent study of a group of schools the correlation between Year 12 study score and hours of paid work per week was found to be −0.45, whilst the correlation between Year 12 study score and hours of sleep per night was found to be 0.31.</div>'
  +plist([('a','Find the values of the coefficient of determination between Year 12 study score and hours of paid work per week, and hours of sleep per night respectively.'),
          ('b','Which of the variables, hours of paid work per week or hours of sleep per night, is more important in explaining the variation in Year 12 study score?')]),
  [fx('Paid work','<i>r</i>²',F('(',V('r','−0.45'),')²'),'20.3%'),fx('Sleep','<i>r</i>²',F(V('r','0.31'),'²'),'9.6%'),('Compare','20.3% &gt; 9.6%')],'',
  f'Written for 12MAG (modelled on {CAM} Example 5; no Edrolo match)',cmd=('Find',None,'square r, then compare'),
  parts=[('a','hours of paid work: <i>r</i>² = (−0.45)² = 20.3% · hours of sleep: <i>r</i>² = 0.31² = 9.6%'),
         ('b','Hours of paid work per week, because it explains a larger percentage of the variation in Year 12 study score (20.3% compared with 9.6%).')]))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['lsrl-predict']
ca,cb=lsq(*zip(*CARS))
S.append(cas('CAS · 3B','Predicting from the least squares line',
  '<p style="font-size:20px">The age (in years) and price (in dollars) of 15 second-hand cars of the same brand and model:</p>'
  +rowtab([('Age (years)',*[a for a,_ in CARS]),('Price ($)',*[f'{p:,}'.replace(',',' ') for _,p in CARS])],12)+
  '<p style="font-size:20px;margin-top:8px">Find the least squares line that predicts price from age, then use it to predict the price of a car that is 5.5 years old.</p>'
  +W_(320,SC(CARS,(0,10),(0,40000),1,5000,'age','price',W=380,H=200,r=4,fs=10,tl=((0,ca),(8.9,ca+cb*8.9)),tl_hid=False)),
  C['ti'],C['classpad'],f'<i>a</i> = {ca:.1f}… · <i>b</i> = {cb:.1f}… → f1(5.5) = <b>${ca+cb*5.5:,.0f}</b> (the rounded equation gives $13 430)'.replace(',',' '),
  f'{CAM} · 3B data (p. 180) and Example 4 · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2019 Exam 2 Q5c (adapted)','Show what you know',
  G('The scatterplot provided shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<em class="v">pressure 3 pm</em>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<em class="v">pressure 9 am</em>) for 23 days in November 2017 at a particular weather station.<br>A least squares line has been fitted to the scatterplot as shown.',
    W_(330,SC(PRESS,(1010,1030),(1010,1030),5,5,'pressure 9 am (hPa)','pressure 3 pm (hPa)',W=400,H=240,r=4,fs=11,tl=((1010.4,111.4+0.8894*1010.4),(1030,111.4+0.8894*1030)),tl_hid=False,sid='x1s')),
    'The equation of this line is <em>pressure 3 pm</em> = 111.4 + 0.8894 × <em>pressure 9 am</em><br>The equation of the least squares line is used to predict the atmospheric pressure at 3 pm when the atmospheric pressure at 9 am is 1025 hPa.<br>'
    'Is this prediction an example of extrapolation or interpolation? <span class="muted">(1 mark)</span>'),
  [('EV range','pressure 9 am in the data: about 1013 to 1027 hPa','data-hi="#x1s|p0,p22|hy"'),('1025 hPa','inside the range')],
  '<b>Interpolation</b> (1025 hPa is within the range of the pressure 9 am data).',
  f'{EDR} · 3B Q11 · adapted (by Edrolo) from VCAA 2019 Further Mathematics Exam 2 Core Q5c: the original refers to the prediction in part b (examiner report; scatterplot redrawn)',stat=('mark',87)))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2018 Exam 2 Q2c','Show what you know',
  G('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>This is called the percentage congestion level.<br>'
    'The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.',
    W_(320,SC(CONG,(35,70),(35,75),5,5,'morning congestion level (%)','evening congestion level (%)',W=400,H=230,r=4,fs=11)),
    'A least squares line is to be fitted to the data with the aim of predicting evening congestion level from morning congestion level.<br>The equation of this line is<div style="text-align:center"><em>evening congestion level</em> = 8.48 + 0.922 × <em>morning congestion level</em></div>'
    'c. Use the equation of the least squares line to predict the evening congestion level when the morning congestion level is 60%. <span class="muted">(1 mark)</span>'),
  [fx('Substitute','<em>evening</em>',F('8.48 + 0.922 × ',V('morning','60')),'63.8')],
  'Predicted evening congestion level = <b>63.8%</b> (rounding does not apply: 64% was not accepted).',
  f'{EDR} · 3B Q12 · VCAA 2018 Further Mathematics Exam 2 Core Q2c (examiner report; original wording; scatterplot redrawn)',stat=('mark',78),cmd=('Use',1,'substitute, no rounding')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex xs"',1)
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2017 Exam 2 Q3bii','Show what you know',
  G('The <em class="v">number of female moths</em> caught in a trap set in a forest and the <em class="v">egg density</em> (eggs per square metre) in the forest can also be examined. A scatterplot of the data is shown below.',
    W_(360,SC(FEM,(10,60),(0,2500),5,500,'number of female moths','egg density',W=440,H=230,r=4.5,fs=11)),
    'The equation of the least squares line is <em>egg density</em> = 191 + 31.3 × <em>number of female moths</em><br>'
    'ii. Interpret the slope of the regression line in terms of the variables egg density and number of female moths caught in the trap. <span class="muted">(1 mark)</span>'),
  [('EV and RV','EV number of female moths · RV egg density'),('Slope','31.3: change in egg density for each <b>one</b> extra female moth')],
  'On average, egg density increases by 31.3 eggs/m² for each additional female moth caught.',
  f'{EDR} · 3B Q13 · VCAA 2017 Further Mathematics Exam 2 Core Q3bii (examiner report: both variables must show a change; original wording; scatterplot redrawn)',stat=('mark',39),cmd=('Interpret',1,'both variables change')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 3 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('3B',) and v.get('url')]))
n=assemble(S,'12MAG · L10 · Interpreting the least squares line',os.path.join(ROOT,'lessons','3B slides.html'))
print(n-1,'slides')
