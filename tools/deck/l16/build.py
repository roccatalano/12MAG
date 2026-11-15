"""Lesson l16 (5A) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5A slides.html
Run: python3 tools/deck/l16/build.py      Screenshots: python3 tools/deck/l16/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- CFAT 1.4.2 (4C-4D) at the start (planner card).
- Do Now: VCAA 2023 Exam 1 Q12 (D, 76%; A 10 B 6 C 4 D 76 E 4; stem shortened: the earlier scatterplot is not needed) ·
          VCAA 2026 Exam 1 Q11 (+ Q10-11 stem, shortened: the scatterplot and table are not needed; B; 2026 report not yet released) ·
          VCAA 2024 Exam 2 Q3 stem + Table 2 + Q3a (answer Wbest; 90% (0.9/1 average), examiner report) ·
          VCAA 2025 NHT Exam 2 Q4 stem + scatterplot + Q4c information + Q4d (NHT report gives no %; r = 0.3744: weak, positive).
- APK: Cambridge U1&2 Ch 7 skills checklist 7D #7 (REPLACES the card's 7B #3, already burnt in l05; scatterplot redrawn; solution worked for 12MAG) · Cambridge U1&2 Ch 5 checklist 5J #14 ·
  VCAA 2019 Further Mathematics Exam 1 Q9 (= Edrolo U1&2 9B Q21, which Edrolo adapted: the ORIGINAL wording and stem are used here;
  E, 67%; A 14 B 3 C 9 D 7 E 67).
- Learn: Cambridge Units 3&4 5A pp. 252-262 (own words; sketches drawn for 12MAG).
- Worked examples: Cambridge U3&4 Examples 1-6 (pp. 254-262). You trys: Edrolo U3&4 4A Worked example 1a (p. 223), Edrolo 4A Worked example 2
  (p. 227-228), YT-5A-2, YT-5A-3, YT-5A-5, YT-5A-6 (planner/written-youtrys.json, written for 12MAG).
- CAS: planner/cas-skills.json 'time-series-plot'; data = Cambridge 5A CAS 1 (pp. 255-256, birth rate 2011-2020).
- Exits: Edrolo U3&4 4A Q11 = VCAA 2018 Further Exam 2 Q3a (88% full marks, report) · 4A Q12 = VCAA 2016 Further Exam 1 Q13
  (C, 72%; A 5 B 3 C 72 D 15 E 6) · 4A Q13 = VCAA 2021 Further Exam 1 Q12 (D, 34%; A 4 B 8 C 13 D 34 E 41). Wording as reprinted by Edrolo.
- Videos: videos.json (5A MaffsGuru link still blank).
"""
import os, sys, json, math
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'
YTW={y['id']:y for y in json.load(open(os.path.join(ROOT,'planner','written-youtrys.json')))['items']}
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l16')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13,tid=''):
    return f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
ALLP=lambda n:keys_('p',n); ALLS=lambda n:keys_('s',n-1)

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.kcas .ytf{height:130px!important;padding-top:0!important}.keys .kd{padding-top:3px!important;padding-bottom:3px!important;margin-bottom:4px!important}.keys .kpic svg{max-height:34px}.tight td,.tight th{padding:2px 5px!important}.T line.hy{stroke:#d9b100!important;stroke-width:5!important}</style>']
# ================= opening
S.append(title(16,'Time series data',f'{CAM} · 5A Time series data','L16',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.4.2','· 4C–4D, 20 min','#00838F'),('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('Time series plots and their features','',None),('Worked examples 1–6','→ You try',None),('CAS: a time series plot','',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.4.2','Reciprocal transformation; choosing and applying a transformation','4C–4D',16,'Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))
mini=lambda ys,**k:ts(ys,W=170,H=44,fs=1,grid=False,r=2,lw=1.6,**k).replace('font-size="0"','font-size="0" fill="none"')
S.append(keys([
  ('Time series data','values of a variable recorded at regular time intervals; time is the EV (horizontal axis)'),
  ('Trend','a long-term increase or decrease',mini([2,3,2.6,4,3.7,5,4.6,6],yr=(0,7),yt=7)),
  ('Cycles','up-and-down movements over periods longer than a year',mini([2,5,6,3,1,4,6,5,2,1,4],yr=(0,7),yt=7)),
  ('Seasonality','a pattern that repeats each calendar period (year, month, week)',mini([3,5,2,4,3,5,2,4,3,5,2,4],yr=(0,7),yt=7)),
  ('Structural change','a sudden change in the established pattern',mini([5,5.3,5,5.4,5.1,2,2.2,1.9,2.1,2],yr=(0,7),yt=7)),
  ('Outlier','a single value that stands out from the rest',mini([3,3.4,3,3.3,6.5,3.2,3,3.4,3.1],yr=(0,7),yt=7)),
  ('Irregular fluctuations','random, unpredictable short-term changes: always present')],
  [('Describing a plot','trend · cycles · seasonality','then structural change · outliers · irregular fluctuations'),
   ('Trend line','a line that ignores the fluctuations','slopes up: increasing · down: decreasing'),
   ('Cycles vs seasonality','longer than a year → cycles','one year or less, calendar-related → seasonality')],
  f'{CAM}, 5A pp. 252–262'))

# ================= Do Now 1: VCAA 2023 E1 Q12 (4B)
lg=(8.52+3.8)/12.6
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q12','Review of 4B',
  'The scatterplot can also be linearised using a logarithm (base 10) transformation applied to the variable <em class="v">age</em>.<br>The equation of the least squares line is'
  '<div style="text-align:center;margin:10px 0"><em>height</em> = −3.8 + 12.6 × log<sub>10</sub>(<em>age</em>)</div>'
  'Using this equation, the <em class="v">age</em>, in years, of a tree with a <em class="v">height</em> of 8.52 m is closest to',
  [('Substitute','8.52 = −3.8 + 12.6 × log<sub>10</sub>(<em>age</em>)'),('Solve',f'log<sub>10</sub>(<em>age</em>) = 12.32 ÷ 12.6 = {lg:.4f}…'),
   ('Undo the log',f'<em>age</em> = 10<sup>{lg:.4f}…</sup> = {10**lg:.2f}')],
  f'<em>age</em> ≈ 9.5 years: <b>D</b>.','VCAA 2023 General Mathematics Exam 1 Q12 (examiner report; stem shortened: the earlier scatterplot is not needed)',
  mc=['7.9','8.9','9.1','9.5','9.9'],key='D',dist=[10,6,4,76,4]))
# ================= Do Now 2: VCAA 2026 E1 Q11 (4C)
v=0.0221-0.00226*5
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q11','Review of 4C',
  'A social media influencer recorded the total number of <em class="v">likes</em> she received on a recent post each <em class="v">day</em> after it had been posted.<br><br>'
  'A reciprocal transformation was applied to the variable <em class="v">likes</em>.<br>When a least squares line is fitted to the transformed data, the equation of this line is'
  '<div style="text-align:center;margin:10px 0;font-size:24px">'+F(FR(['1'],['<em>likes</em>']),' = 0.0221 − 0.00226 × <em>day</em>')+'</div>'
  'Using this equation, the predicted value of <em class="v">likes</em> when <em class="v">day</em> = 5 is closest to',
  [('Substitute',f'1 ÷ <em>likes</em> = 0.0221 − 0.00226 × 5 = {v:.4f}'),('Flip it',f'<em>likes</em> = 1 ÷ {v:.4f} = {1/v:.2f}')],
  '<em>likes</em> ≈ 93: <b>B</b>.','VCAA 2026 General Mathematics Exam 1 Q10–11 stem (shortened: scatterplot and table not needed) and Q11 (2026 report not yet released)',
  mc=['91','93','95','99'],key='B',stat=('new',)))
# ================= Do Now 3: VCAA 2024 E2 Q3a (2A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q3a','Review of 2A',
  '<div style="font-size:17px">The Olympic gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, is often lower than the best height achieved in other international women’s high jump competitions in that same year.<br>'
  'Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.<br>'
  'A scatterplot of <em class="v">Wbest</em> versus <em class="v">Wgold</em> for this data is also provided.'
  '<div style="margin:6px 0"><b>Table 2</b>'+rowtab([('<i>year</i>',*OLY_Y),('<i>Wgold</i> (m)',*WGOLD),('<i>Wbest</i> (m)',*WBEST)],12)+'</div>'
  'When a least squares line is fitted to the scatterplot, the equation is found to be:<div style="text-align:center;margin:6px 0"><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em></div>'
  'The correlation coefficient is 0.9318<br><br>a. Name the response variable in this equation. <span class="muted">(1 mark)</span></div>',
  [('Equation form','RV = <i>a</i> + <i>b</i> × EV'),('Left-hand side','<em>Wbest</em> is the variable being predicted')],
  'The response variable is <b><em>Wbest</em></b>.','VCAA 2024 General Mathematics Exam 2 Q3 stem, Table 2 and Q3a (examiner report; scatterplot not needed for part a)',stat=('mark',90),cmd=('Name',1,'the RV')))
# ================= Do Now 4: VCAA 2025 NHT E2 Q4d (2E)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 NHT Exam 2 Q4d','Review of 2E',
  ('The height of a father, <em class="v">father’s height</em>, and the height of his son, <em class="v">son’s height</em>, were recorded, for a sample of 30 father–son pairs.<br>'
   'A scatterplot of this data is shown below. All heights were measured in metres.',
   Wd(400,scat(FS,(1.60,1.90),(1.60,1.95),0.05,0.05,'father’s height (m)','son’s height (m)',W=480,H=230,r=4,fs=12,sid='d4s')),
   'When a least squares line is fitted to the scatterplot, the equation is found to be: <em>son’s height</em> = 1.10 + 0.375 × <em>father’s height</em><br>'
   'The correlation coefficient is 0.3744<br>d. Describe the association between <em class="v">son’s height</em> and <em class="v">father’s height</em> in terms of strength and direction. <span class="muted">(1 mark)</span>'),
  [('Strength','<i>r</i> = 0.3744: between 0.3 and 0.5 → weak'),('Direction','<i>r</i> &gt; 0 (slope 0.375 &gt; 0) → positive','data-hi="#d4s|p|hy"')],
  'strength: <b>weak</b> · direction: <b>positive</b>','VCAA 2025 NHT General Mathematics Exam 2 Q4 stem, Q4c information and Q4d (scatterplot redrawn; NHT report gives no %)',stat=('new',),cmd=('Describe',1,'strength + direction')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK 1: Cambridge U1&2 7D #7 (replaces 7B #3, burnt in l05)
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7D #7','A line fitted by eye',
  ('Determine the equation of the line fitted by eye to the scatterplot, below, which shows the association between the age of a group of cars, in years, (<em class="v">age of car</em>) and the number of kilometres they have travelled (<em class="v">kms</em>).',
   Wd(440,scat(CARS,(0,10),(0,80000),1,10000,'Age of car (years)','Kms',W=500,H=250,r=4,fs=12,tl=((0,10000),(10,62000)),tl_hid=False,sid='a1s')),''),
  [('Two points on the line','(0, 10 000) and (10, 62 000)','data-hi="#a1s|tl|hy"'),fx('Slope','<i>b</i>',F(FR([V('y₂','62 000'),' − ',V('y₁','10 000')],[V('x₂','10'),' − ',V('x₁','0')])),'5200'),
   ('Intercept','the line cuts the vertical axis at 10 000')],
  '<em>kms</em> = <b>10 000 + 5200 × <em>age of car</em></b>',
  f'{CAM12} · Ch 7 skills checklist 7D #7 (scatterplot redrawn) · solution worked for 12MAG · replaces 7B #3 (already used in l05)',cmd=('Determine',None,'two points → slope → intercept')))
# ================= APK 2: Cambridge U1&2 5J #14
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 5J #14','Piecewise linear graphs',
  '<div style="font-size:26px">A car park is open for 10 hours a day. The cost, <i>C</i>, for the time, <i>t</i>, is given by the following piecewise equation.'
  '<div style="margin:16px 40px;line-height:1.7"><i>C</i> = 12<i>t</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(0 ≤ <i>t</i> &lt; 4)<br><i>C</i> = 8 + 10<i>t</i> &nbsp;&nbsp;&nbsp;(4 ≤ <i>t</i> ≤ 10)</div>'
  'Find the cost for parking your car for 8 hours.</div>',
  [('Which piece?','<i>t</i> = 8 is in 4 ≤ <i>t</i> ≤ 10: use <i>C</i> = 8 + 10<i>t</i>'),fx('Substitute','<i>C</i>',F('8 + 10 × ',V('t','8')),'88')],
  'Parking for 8 hours costs <b>$88</b>.',f'{CAM12} · Ch 5 skills checklist 5J #14 · solution worked for 12MAG',cmd=('Find',None,'pick the right piece')))
# ================= APK 3: VCAA 2019 E1 Q9
S.append(qslide('apk','APK · Year 11 · VCAA 2019 Exam 1 Q9','Rounding to significant figures',
  '<div style="font-size:21px">A least squares line is used to model the relationship between the monthly <em class="v">average temperature</em> and <em class="v">latitude</em> recorded at seven different weather stations. The equation of the least squares line is found to be'
  '<div style="text-align:center;margin:10px 0"><em>average temperature</em> = 42.9842 – 0.877447 × <em>latitude</em></div>'
  'When the numbers in this equation are correctly rounded to three significant figures, the equation will be</div>',
  [('Intercept','42.9842: first three significant figures 4, 2, 9; next digit 8 → round up: 43.0'),('Slope','0.877447: 8, 7, 7; next digit 4 → stays: 0.877')],
  '<em>average temperature</em> = 43.0 – 0.877 × <em>latitude</em>: <b>E</b>.',
  'Edrolo General Mathematics Units 1&amp;2 · 9B Q21 (adapted by Edrolo) · VCAA 2019 Further Mathematics Exam 1 Q9 (examiner report; original wording)',
  mc=['<em>average temperature</em> = 42.984 – 0.877 × <em>latitude</em>','<em>average temperature</em> = 42.984 – 0.878 × <em>latitude</em>','<em>average temperature</em> = 43.0 – 0.878 × <em>latitude</em>',
      '<em>average temperature</em> = 42.9 – 0.878 × <em>latitude</em>','<em>average temperature</em> = 43.0 – 0.877 × <em>latitude</em>'],
  key='E',dist=[14,3,9,7,67],dis=('A','14% rounded to three decimal places (42.984), not three significant figures.')))
S[-1]=S[-1].replace('<section class="slide T apk mcslide"','<section class="slide T apk mcslide sm"',1)

# ================= Learn 1: what a time series plot is
BR=[1.926,1.920,1.855,1.826,1.814,1.752,1.741,1.740,1.657,1.580]
S.append(learn('Learn · 5A','Time series data and time series plots',
  '<h4>Time series plots</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>time series data: one variable recorded at regular time intervals</li>'
  '<li><b>time is always the EV</b>: it goes on the horizontal axis</li><li>plot the points as for a scatterplot, then <b>join consecutive points</b> with straight lines</li>'
  '<li>months, quarters or days can be coded 1, 2, 3 …</li></ul>',
  Wd(560,ts(BR,list(range(2011,2021)),yr=(1.5,2.0),yt=0.1,xl='year',yl='birth rate',W=560,H=250,sid='lp1',hidpts=True,hidline=True)),
  'Never join the points in order of size: join them in time order.',f'{CAM}, 5A pp. 252–255 (data: CAS 1, birth rate 2011–2020)',
  frags=f'<span class="frag" data-show="#lp1|{ALLP(10)}"></span><span class="frag" data-show="#lp1|{ALLS(10)}"></span>',
  cards=(kcard('Time series data','values recorded at regular time intervals'),)))
# ================= Learn 2: the features
def sk(ys,nm,tl=None): return f'<div style="flex:1;min-width:0"><div style="font-weight:700;font-size:17px;text-align:center">{nm}</div>'+ts(ys,W=250,H=120,fs=10,grid=False,r=2.5,lw=1.8,tls=tl or ())+'</div>'
S.append(learn('Learn · 5A','What to look for in a time series plot',
  '<h4>Six features</h4><ul class="bul" style="font-size:18px;line-height:1.45;margin-left:22px"><li><b>Trend</b>: long-term up or down (draw a trend line through the fluctuations)</li>'
  '<li><b>Cycles</b>: peaks and troughs over periods longer than a year</li><li><b>Seasonality</b>: peaks and troughs at the same time each calendar period</li>'
  '<li><b>Structural change</b>: a sudden change in the pattern · <b>Outliers</b>: single values that stand out</li><li><b>Irregular fluctuations</b>: random changes, always there</li></ul>',
  '<div class="row" style="gap:10px;flex-wrap:wrap">'
  +'<div class="frag" style="flex:1;display:flex;gap:10px">'+sk([2,2.6,2.3,3.4,3.1,4,3.7,4.8,4.4,5.4],'Trend',[((1,2.1),(10,5.3),'t')]).replace('class="hid0"','')+sk([2,4,6,5,2,1,3,6,6,3,1,2,5],'Cycles')+sk([3,6,2,4,3,6,2,4,3,6,2,4],'Seasonality')+'</div>'
  +'<div class="frag" style="flex:1;display:flex;gap:10px">'+sk([5,5.4,5,5.3,5.1,2,2.3,1.9,2.2,2],'Structural change')+sk([3,3.4,3,3.3,7,3.2,3,3.4,3.1],'Outlier')+sk([3,5,2.5,4.5,3.2,5.5,2.4,4,3],'Irregular fluctuations')+'</div></div>',
  'Seasonality needs a calendar period (year, month, week). Peaks that come every few years are cycles.',f'{CAM}, 5A pp. 257–262 (sketches drawn for 12MAG)',
  cards=(kcard('Trend','long-term increase or decrease'),kcard('Seasonality','calendar-related repeating pattern'))))

# ================= WE1 / YT Edrolo WE1a
E1F=ts(E1_T,yr=(15,40),yt=5,xl='Day',yl='Temp (°C)',xlab={k+1:d for k,d in enumerate(E1_DAYS)},W=420,H=210,sid='e1f',hidpts=True,hidline=True)
S.append(qslide('we','Worked example 1 · 5A','Constructing a time series plot',
  '<div style="font-size:22px">Maximum temperature was recorded each day for a week in a certain town. Construct a time series plot of the data.</div><div style="margin:14px 0">'
  +rowtab([('Day',*E1_DAYS),('Temperature (°C)',*E1_T)],18,'e1t')+'</div>',
  [],'Time series plot of temperature against day',f'{CAM} · Example 1 (p. 254)',video='Cambridge GO · Example 1 (5A Resources)',cmd=('Construct',None,'time on the horizontal axis'),
  afig=Wd(400,E1F),build=[('EV: day (horizontal axis) · RV: temperature (vertical axis)',''),('Scales: days Mon–Sun · temperature 15 to 40 in steps of 5',''),
       ('Plot the seven points as for a scatterplot',f'data-show="#e1f|{ALLP(7)}" data-hi="#e1t|p|hy"'),('Join consecutive points with straight lines',f'data-show="#e1f|{ALLS(7)}"')]))
W1F=ts(WE1_D,yr=(1000,2200),yt=200,xl='month',yl='deaths and serious injuries',W=520,H=230,fs=12,xtick=2,xr=(0,16),sid='y1f',hidpts=True,hidline=True)
S.append(qslide('yt','You try · Edrolo 4A WE1','Constructing a time series plot',
  '<div style="font-size:19px">The <em class="v">number of deaths and serious injuries</em> caused by road accidents in the UK for each month from October 1982 until the end of 1983 are shown in a table.</div><div style="margin:10px 0">'
  +rowtab([('month',*WE1_M),('deaths and serious injuries',*WE1_D)],11)+'</div><div style="font-size:19px">a. Use the table to construct a time series plot.</div>',
  [],'Time series plot of deaths and serious injuries against coded month',f'{EDR} · 4A Worked example 1a (p. 223; Method 1 by hand, Method 2 CAS)',cmd=('construct',None,'code the months first'),
  afig=Wd(470,W1F),build=[('Code the months: Oct 1982 = 1, Nov 1982 = 2, … Dec 1983 = 15',''),('Axes: month 0 to 16 · deaths and serious injuries 1000 to 2200',''),
       ('Plot each data point',f'data-show="#y1f|{ALLP(15)}"'),('Join the points in order with straight lines',f'data-show="#y1f|{ALLS(15)}"')]))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)
# ================= WE2 / YT-5A-2
B2=ts(BIRTH,BIRTH_Y,yr=(1.6,3.6),yt=0.4,xl='Year',yl='Birth rate',W=560,H=240,fs=12,xtick=10,xr=(1930,2000),sid='e2f',r=2.5,
      tls=[((1933,1.75),(1958,3.38),'t1'),((1956,3.6),(1972,1.68),'t2'),((1966,1.95),(1996,1.6),'t3')])
S.append(qslide('we','Worked example 2 · 5A','Identifying trends',
  ('Consider the time series plot of the Australian annual birth rates over the years from 1931 to 1990, shown below. Comment on the trend shown in the plot.',Wd(520,B2),''),
  [('Trend 1','1940 to 1961: increasing quickly (the ‘Baby Boom’, after the Second World War)','data-show="#e2f|t1"'),
   ('Trend 2','about 1962 to 1980: decreasing very rapidly (the ‘Baby Bust’)','data-show="#e2f|t2"'),
   ('Trend 3','the 1980s and beyond: decreasing slowly','data-show="#e2f|t3"')],
  'There are <b>three distinct trends</b>: a rapid increase from 1940 to 1961, a very rapid decrease from about 1962 to 1980, then a slow decrease during the 1980s and beyond.',
  f'{CAM} · Example 2 (p. 258; plot redrawn, values read off)',video='Cambridge GO · Example 2 (5A Resources)',cmd=('Comment',None,'draw trend lines, give the years')))
y2=YTW['YT-5A-2']
S.append(qslide('yt','You try · written for 12MAG (YT-5A-2)','Identifying trends',
  ('Consider the time series plot of the number of visitors (in thousands) to a national park each year from 2008 to 2022, constructed from the data below. Comment on the trend shown in the plot.',
   Wd(470,ts(YT2,list(range(2008,2023)),yr=(30,70),yt=10,xl='year',yl='visitors (’000)',W=520,H=210,fs=12,xtick=2,xr=(2007,2023),sid='y2f',
             tls=[((2008,40),(2014,62),'t1'),((2014,62),(2022,38),'t2')])),
   rowtab([('Year',*range(2008,2023)),('Visitors (’000)',*YT2)],11)),
  [('Trend 1','2008 to 2014: increasing steadily (41 000 → 62 000)','data-show="#y2f|t1"'),('Trend 2','2014 to 2022: decreasing steadily (62 000 → 38 000)','data-show="#y2f|t2"')],
  '<b>Two distinct trends</b>: from 2008 to 2014 the number of visitors increased steadily (41 000 to 62 000); from 2014 to 2022 it decreased steadily (62 000 to 38 000).',
  f'Written for 12MAG (modelled on {CAM} Example 2; no Edrolo match)',cmd=('Comment',None,'trend lines + years')))
# ================= WE3 / YT-5A-3
S.append(qslide('we','Worked example 3 · 5A','Identifying cycles',
  ('Sunspots are darker, cooler area on the surface of the sun. The following plot shows the sunspot activity for the period 1945 to 2016. Comment on the cycles shown in the plot.',
   Wd(540,ts(SUN,SUN_Y,yr=(0,200),yt=50,xl='Year',yl='Sunspots',W=560,H=240,fs=12,xtick=10,xr=(1940,2020),sid='e3f',r=2.5,
             vmarks=[(1954,''),(1964,''),(1975,''),(1986,''),(1996,''),(2008,'')])),''),
  [('Pattern','peaks and troughs that repeat, roughly every 10 to 11 years: longer than a year → cycles'),
   ('Lows','years of lowest activity: about 1954, 1964, 1975, 1986, 1996, 2008','data-show="#e3f|vm"')],
  'The plot shows <b>cycles</b>: a recurrent pattern of peaks and troughs. The years of lowest sunspot activity are approximately 1954, 1964, 1975, 1986, 1996 and 2008.',
  f'{CAM} · Example 3 (p. 259; plot redrawn, values read off)',video='Cambridge GO · Example 3 (5A Resources)',cmd=('Comment',None,'name the cycle + when')))
S.append(qslide('yt','You try · written for 12MAG (YT-5A-3)','Identifying cycles',
  ('The following plot shows the number of mice caught each year on a farm for the period 2000 to 2023, constructed from the data below. Comment on the cycles shown in the plot.',
   Wd(480,ts(YT3,list(range(2000,2024)),yr=(0,100),yt=20,xl='year',yl='mice caught',W=540,H=210,fs=12,xtick=2,xr=(1999,2024),sid='y3f',
             vmarks=[(2002,''),(2008,''),(2014,''),(2020,'')])),
   rowtab([('Year',*range(2000,2012)),('Mice',*YT3[:12]),('Year',*range(2012,2024)),('Mice',*YT3[12:])],11)),
  [('Pattern','peaks and troughs lasting longer than a year → cycles'),('Peaks','highest about 2002, 2008, 2014, 2020: every 6 years','data-show="#y3f|vm"')],
  'There is a recurrent pattern of peaks and troughs lasting longer than a year, so the plot shows <b>cycles</b>. The highest numbers are about 2002, 2008, 2014 and 2020: the cycle repeats about every 6 years.',
  f'Written for 12MAG (modelled on {CAM} Example 3; no Edrolo match)',cmd=('Comment',None,'cycle length')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)
# ================= WE4 / Edrolo WE2
jun=[k for k in range(18) if k%4==1]; dec=[k for k in range(18) if k%4==3]
S.append(qslide('we','Worked example 4 · 5A','Identifying seasonality',
  ('The plot below shows the total percentage of hotel rooms occupied in Australia by quarter, over the years 2012–2016. Comment on the seasonality shown in the plot.',
   Wd(540,ts(HOTEL,yr=(67,75),yt=1,xl='Quarter',yl='Room occupancy rate (%)',W=580,H=250,fs=11,xlab=HOTEL_LAB,sid='e4f',tls=[((1,70.3),(18,72.4),'t1')])),''),
  [('Same time each year','troughs every June quarter','data-hi="#e4f|'+','.join(f'p{k}' for k in jun)+'|hb"'),
   ('Peaks','highest in the December quarter','data-hi="#e4f|'+','.join(f'p{k}' for k in dec)+'|hy"'),
   ('Trend','the trend line slopes upward: increasing','data-show="#e4f|t1"')],
  'Regular peaks and troughs at the same time each year show <b>seasonality</b>: occupancy is lowest in the June quarter and highest in the December quarter. There is also an increasing <b>trend</b>.',
  f'{CAM} · Example 4 (pp. 259–260; plot redrawn, values read off)',video='Cambridge GO · Example 4 (5A Resources)',cmd=('Comment',None,'when are the peaks and troughs?')))
decs=[k for k in range(49) if (k+9)%12==0]
S.append(qslide('yt','You try · Edrolo 4A WE2','Seasonality and structural change',
  ('The number of <em class="v">deaths and serious injuries</em> caused by road accidents in the UK for each month over a four-year period, from September 1980 until September 1984, are shown in the time series plot.<br>Note that seat belt use became mandatory by law in the UK in February 1983.',
   Wd(540,ts(WE2,yr=(1000,2100),yt=100,xl='month',yl='deaths and serious injuries',W=580,H=240,fs=11,xtick=5,xr=(0,50),sid='y4f',r=2.5,vmarks=[(30,'Feb 1983')])),
   'Describe any patterns present in the time series plot.'),
  [('Trend','no general increase or decrease: no trend'),('Seasonality','peaks every 12 months, generally in December','data-hi="#y4f|'+','.join(f'p{k}' for k in decs)+'|hy"'),
   ('Structural change','a sudden drop from month 29 to month 31: the seat belt law (month 30)','data-show="#y4f|vm"')],
  'No obvious <b>trend</b>. <b>Seasonality</b> with a period of 12 months, peaking every December. A <b>structural change</b> between month 29 and month 31, explained by the mandatory seat belt laws of February 1983.',
  f'{EDR} · 4A Worked example 2 (pp. 227–228; plot redrawn, values read off)',cmd=('Describe',None,'trend, seasonality, change')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)
# ================= WE5 / YT-5A-5
S.append(qslide('we','Worked example 5 · 5A','Identifying structural change',
  ('The time series plot below shows the power bill for a rental house (in kWh) for the 12 months of a year. Comment on any structural change in the plot.',
   Wd(480,ts(POWER,yr=(0,350),yt=50,xl='Month',yl='Electricity use (kWh)',W=520,H=240,fs=12,xlab={k+1:m for k,m in enumerate(MONTHS)},sid='e5f',vmarks=[(6.5,'')])),''),
  [('Before','January to June: around 300 kWh per month','data-hi="#e5f|p0,p1,p2,p3,p4,p5|hb"'),('After','July to December: around 175 kWh','data-hi="#e5f|p6,p7,p8,p9,p10,p11|hy"'),
   ('When','an abrupt drop from June to July','data-show="#e5f|vm"')],
  'There is a <b>structural change</b> from June to July: monthly power use suddenly drops from around 300 kWh to around 175 kWh, probably from a change in circumstances (e.g. a family moving out and one person living alone).',
  f'{CAM} · Example 5 (pp. 260–261; plot redrawn, values read off)',video='Cambridge GO · Example 5 (5A Resources)',cmd=('Comment',None,'when, from what to what, why')))
S.append(qslide('yt','You try · written for 12MAG (YT-5A-5)','Identifying structural change',
  ('The time series plot below shows the water use for a house (in kL) for the 12 months of a year, constructed from the data below. Comment on any structural change in the plot.',
   Wd(460,ts(YT5,yr=(0,45),yt=5,xl='Month',yl='Water use (kL)',W=500,H=220,fs=12,xlab={k+1:m for k,m in enumerate(MONTHS)},sid='y5f',vmarks=[(6.5,'')])),
   rowtab([('Month',*MONTHS),('Water use (kL)',*YT5)],12)),
  [('Before','January to June: around 21 kL','data-hi="#y5f|p0,p1,p2,p3,p4,p5|hb"'),('After','July to December: around 38 kL','data-hi="#y5f|p6,p7,p8,p9,p10,p11|hy"'),('When','an abrupt increase from June to July','data-show="#y5f|vm"')],
  'An abrupt <b>structural change</b> from June to July: water use suddenly increases from around 21 kL per month to around 38 kL, probably from a change in circumstances (e.g. more people moving into the house).',
  f'Written for 12MAG (modelled on {CAM} Example 5)',cmd=('Comment',None,'when, from what to what, why')))
# ================= WE6 / YT-5A-6
S.append(qslide('we','Worked example 6 · 5A','Identifying outliers',
  ('The time series plot below shows the daily power bill for a house (in kWh) for a fortnight. Comment on any outliers in the plot.',
   Wd(460,ts(DAILY,yr=(0,12),yt=2,xl='Day',yl='Electricity use (kWh)',W=500,H=230,fs=12,xr=(0,15),sid='e6f')),''),
  [('Usual pattern','fluctuates around 10 kWh per day'),('Stands out','day 4: less than 2 kWh','data-hi="#e6f|p3|hy"')],
  'Day 4 is a clear <b>outlier</b>: less than 2 kWh was used, against about 10 kWh on other days (the house was without power for 18 hours because of a storm).',
  f'{CAM} · Example 6 (pp. 261–262; plot redrawn, values read off)',video='Cambridge GO · Example 6 (5A Resources)',cmd=('Comment',None,'which value + why')))
S.append(qslide('yt','You try · written for 12MAG (YT-5A-6)','Identifying outliers',
  ('The time series plot below shows the number of coffees sold each day at a café for a fortnight, constructed from the data below. Comment on any outliers in the plot.',
   Wd(460,ts(YT6,yr=(0,160),yt=20,xl='Day',yl='Coffees sold',W=500,H=220,fs=12,xr=(0,15),sid='y6f')),rowtab([('Day',*range(1,15)),('Coffees sold',*YT6)],12)),
  [('Usual pattern','around 80–86 coffees each day'),('Stands out','day 9: 150 coffees','data-hi="#y6f|p8|hy"')],
  'Day 9 is an <b>outlier</b>: 150 coffees were sold, against about 80–86 on other days (perhaps a special event nearby).',
  f'Written for 12MAG (modelled on {CAM} Example 6)',cmd=('Comment',None,'which value + why')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['time-series-plot']
S.append(cas('CAS · 5A','Constructing a time series plot',
  '<p style="font-size:20px">Construct a time series plot for the data presented below, which shows the birth rate in Australia (in births per woman) from 2011–2020.</p>'
  +rowtab([('year',*range(2011,2021)),('birth',*BR)],13)+'<div style="margin-top:14px">'+Wd(420,ts(BR,list(range(2011,2021)),yr=(1.5,2.0),yt=0.1,xl='year',yl='birth',W=460,H=220,fs=12))+'</div>',
  C['ti'],C['classpad'],'A connected plot of <em>birth</em> against <em>year</em>: a <b>decreasing trend</b> from 1.926 (2011) to 1.580 (2020).',
  f'{CAM} · 5A CAS 1 (pp. 255–256) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos'].get('ti',[])[:1]+C['videos'].get('classpad',[])[:1]]))

# ================= Exits
MF=ts(MEL,list(range(2008,2017)),yr=(20,45),yt=5,xl='year',yl='congestion level (%)',W=480,H=220,fs=12,xtick=1,xr=(2008,2016),sid='x1f',r=3,
      extra=[(SYD,'#5b3fa8','')],hidfrom=6)
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 2 Q3a','Show what you know',
  '<div style="font-size:18px">The following table shows the yearly average traffic congestion levels in two cities, Melbourne and Sydney, during the period 2008 to 2016. Also shown is a time series plot of the same data. The time series plot for Melbourne is incomplete.</div><div style="margin:8px 0">'
  +rowtab([('<i>year</i>',*range(2008,2017)),('Melbourne',*MEL),('Sydney',*SYD)],13,'x1t')+'</div>'
  +Wd(420,ts(MEL,list(range(2008,2017)),yr=(20,45),yt=5,xl='year',yl='congestion level (%)',W=480,H=210,fs=12,xr=(2008,2016),r=3,extra=[(SYD,'#5b3fa8','')],hidfrom=6).replace('class="hid0"','style="display:none"'))
  +'<div style="font-size:13px;color:var(--muted)">Upper line: Sydney · lower line: Melbourne (to 2013)</div>'
  '<div style="font-size:18px;margin-top:6px">Use the data in the table to complete the time series plot for Melbourne. <span class="muted">(1 mark)</span></div>',
  [],'Melbourne completed: 2014 → 28, 2015 → 29, 2016 → 33',f'{EDR} · 4A Q11 · VCAA 2018 Further Mathematics Exam 2 Core Q3a (examiner report; plot redrawn)',stat=('mark',88),cmd=('complete',1,'plot 2014–2016, then join'),
  afig=Wd(380,MF),build=[('Read 2014–2016 for Melbourne: 28, 29, 33','data-hi="#x1t|p|hy"'),('Plot the three points',f'data-show="#x1f|p6,p7,p8"'),('Join them on from 2013','data-show="#x1f|s5,s6,s7"')]))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2016 Exam 1 Q13','Show what you know',
  ('Consider the time series plot.',Wd(470,ts(TEMP16,list(range(0,49)),yr=(0,30),yt=5,xl='month number',yl='mean temperature',W=520,H=220,fs=12,xtick=12,xr=(0,48),r=2.8,sid='x2f')),
   'The pattern in the time series plot shown is best described as having'),
  [('Trend?','peaks and troughs stay about the same height: no clear trend'),('Seasonality','peaks every 12 months: a calendar period','data-hi="#x2f|p13,p26,p37,p48|hy"'),('Irregular','always present')],
  'Seasonality with irregular fluctuations: <b>C</b>.',f'{EDR} · 4A Q12 · VCAA 2016 Further Mathematics Exam 1 Q13 (examiner report; plot redrawn)',
  mc=['irregular fluctuations only.','an increasing trend with irregular fluctuations.','seasonality with irregular fluctuations.','seasonality with an increasing trend and irregular fluctuations.',
      'seasonality with a decreasing trend and irregular fluctuations.'],key='C',dist=[5,3,72,15,6],dis=('D','15% saw an increasing trend: the peaks and troughs do not keep rising.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide sm"',1)
xs21=[2010+k/4 for k in range(41)]
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2021 Exam 1 Q12','Show what you know',
  ('The time series plot shows the quarterly <em class="v">sales</em>, in thousands of dollars, of a small business for the years 2010 to 2020.',
   Wd(470,ts(SALES21,xs21,yr=(0,700),yt=100,xl='year',yl='sales ($000’s)',W=520,H=220,fs=12,xtick=2,xr=(2010,2020),r=2.8,sid='x3f',tls=[((2010,390),(2020,215),'t1')])),
   'The time series plot is best described as having'),
  [('Trend','sales drift down over the decade: decreasing trend','data-show="#x3f|t1"'),('Seasonality?','the peaks are not at the same quarter each year: no seasonality'),('Irregular','large random ups and downs')],
  'A decreasing trend with irregular fluctuations: <b>D</b>.',f'{EDR} · 4A Q13 · VCAA 2021 Further Mathematics Exam 1 Q12 (examiner report; plot redrawn)',
  mc=['seasonality only.','irregular fluctuations only.','seasonality with irregular fluctuations.','a decreasing trend with irregular fluctuations.','a decreasing trend with seasonality and irregular fluctuations.'],
  key='D',dist=[4,8,13,34,41],dis=('E','41% chose seasonality too: peaks and troughs that do not come in the same quarter each year are irregular, not seasonal.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5A',) and v.get('url')]))
n=assemble(S,'12MAG · L16 · Time series data',os.path.join(ROOT,'lessons','5A slides.html'))
print(n-1,'slides')
