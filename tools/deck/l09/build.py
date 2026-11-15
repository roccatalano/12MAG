"""Lesson l09 (3A) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/3A slides.html
Run: python3 tools/deck/l09/build.py      Screenshots: python3 tools/deck/l09/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- CFAT 1.2.3 (2E-2H) at the start (planner card).
- Do Now: VCAA 2024 Exam 1 Q13-14 stem + Q14 (B, 68%; A 15 B 68 C 12 D 5) ·
          VCAA 2026 Exam 1 Q7 (+ Q7-8 stem and scatterplot; A; 2026 report not yet released) — REPLACES the card's VCAA 2026 NHT E1 Q11,
          which interprets a least squares line for a reciprocal-transformed variable (3B/4: not yet taught, so not retrieval; see QUEUE
          Decisions log; Q11 freed) ·
          VCAA 2023 Exam 2 Q3b (+ stem; r = 0.849; 69% full marks) · VCAA 2026 Exam 2 Q3 stem + Q3c (upper fence 93.6; report not yet released).
- APK: Cambridge U1&2 Ch 7 skills checklist 7D #8 (data from 7A #2; solution worked for 12MAG on CAS) · Cambridge U1&2 Ch 5 checklist 5E #7 ·
  Edrolo U1&2 6C Q11 (adapted from VCAA 2017 Further Exam 2 Q4cii: the original uses a log10 transformation (Ch 4), so Edrolo's adapted
  wording is used, labelled adapted; % from the 2017 report: 53%) · VCAA 2021 Further Exam 2 Q3eii (= Edrolo U1&2 6C Q12; original wording,
  stem shortened to the part e information; report 18%, answer 'Same decreasing trend continues in the future').
- Learn: Cambridge Units 3&4 3A pp. 169-172 (own words; diagram redrawn).
- Worked examples: Cambridge U3&4 Example 1 (p. 171-172), Example 2 (pp. 172-173). You trys: Edrolo U3&4 3A Worked example 3 (p. 161) ·
  YT-3A-2 (planner/written-youtrys.json, written for 12MAG).
- CAS: planner/cas-skills.json 'lsrl'; data = Cambridge 3A CAS 1 (pp. 173-175): weight = -84.8 + 0.867 x height, r^2 = 0.723.
  CAS You try: Edrolo U3&4 3A Worked example 1 (p. 157): height of son = 23.2 + 0.857 x height of father.
- Exits: Edrolo U3&4 3A Q13 = VCAA 2018 Further Exam 1 Q13 (D, 49%; A 9 B 13 C 22 D 49 E 6) · Edrolo 3A Q14 = VCAA 2021 Further Exam 1 Q11
  (D, 40%; A 14 B 29 C 11 D 40 E 5) · Edrolo 3A Q15 = VCAA 2017 Further Exam 2 Q3a, bi (a: 67% full marks; bi: 26%). Original wording.
- Videos: videos.json (3A MaffsGuru link still blank).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l09')
yid=lambda u:u.split('v=')[1].split('&')[0]
def stats(cols,rows,fs=20):
    """summary-statistics table: cols = header names; rows = (label, values...)"""
    return (f'<table class="t" style="font-size:{fs}px;margin:10px 0"><tr><th></th>'+''.join(f'<th>{c}</th>' for c in cols)+'</tr>'+
            ''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>')
def rowtab(rows,fs=13):
    return f'<table class="t tight" style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def slope(): return F(FR(['<i>r</i> × <i>s<sub>y</sub></i>'],['<i>s<sub>x</sub></i>']))

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}</style>']
# ================= opening
S.append(title(9,'Fitting a least squares regression line',f'{CAM} · 3A Fitting a least squares regression line to numerical data','L09',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')).replace('font-size:84px','font-size:64px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.2.3','· 2E–2H, 20 min','#00838F'),('Do Now','· four VCAA questions','#00838F'),('APK','· four Year 11 questions','var(--apk)'),
  ('Residuals and the least squares line','',None),('Worked examples 1–2','→ You try',None),('CAS: the least squares line','→ You try',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.2.3','Correlation, r², correlation and causation','2E–2H',15,'Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))
S.append(keys([
  ('Residual','the vertical distance from a data point to the line: actual − predicted (above the line +, below −)'),
  ('Least squares line','the line that makes the <b>sum of the squares of the residuals</b> as small as possible'),
  ('Assumptions','numerical data · linear association · no clear outliers'),
  ('EV and RV','“predict <i>y</i> from <i>x</i>”: <i>x</i> is the EV, <i>y</i> is the RV')],
  [('Least squares line',F('<i>y</i> = <i>a</i> + <i>b</i><i>x</i>'),'a = intercept · b = slope'),
   ('Slope',F('<i>b</i> = ',FR(['<i>r</i> × <i>s<sub>y</sub></i>'],['<i>s<sub>x</sub></i>'])),'x = EV, y = RV'),
   ('Intercept',F('<i>a</i> = <i>ȳ</i> − <i>b</i><i>x̄</i>'),'work out b first'),
   ('r from the slope',F('<i>r</i> = ',FR(['<i>b</i> × <i>s<sub>x</sub></i>'],['<i>s<sub>y</sub></i>'])),'same sign as b')],
  f'{CAM}, 3A pp. 169–173'))

# ================= Do Now 1: VCAA 2024 E1 Q14 (1F)
NT=rowtab([('<i>year</i>',*range(2011,2023)),('<i>new</i>',*NEWST)],14).replace('<table','<table id="d1t"')
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q14','Review of 1F',
  'A school runs an orientation program for new staff each January.<br>The time series plot below shows the number of new staff, <em class="v">new</em>, for each year, <em class="v">year</em>, from 2011 to 2022 (inclusive).'
  f'<div style="margin:8px 0">{NT}<div style="font-size:13px;color:var(--muted)">(values read off the time series plot)</div></div>'
  'The number of new staff in 2023 is added to the total number of new staff from the previous 12 years.<br>For these 13 years, the mean number of new staff is 11.<br>The number of new staff in 2023 is',
  [('Total for 13 years','mean × number = 11 × 13 = 143'),('Total for 12 years','14 + 11 + 7 + … + 10 = 127','data-hi="#d1t|p|hy"'),('2023','143 − 127 = 16')],
  '16 new staff: <b>B</b>.','VCAA 2024 General Mathematics Exam 1 Q13–14 stem and Q14 (examiner report; time series plot shown as a table of its values)',
  mc=['11','16','17','19'],key='B',dist=[15,68,12,5],dis=('A','15% chose the mean itself, 11: the new value has to pull the total up to 143.')))
# ================= Do Now 2: VCAA 2026 E1 Q7 (2E)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q7','Review of 2E–2H',
  G('A least squares line has been fitted to the scatterplot below to enable the number of television sets per 1000 people, <em class="v">TV sets</em>, to be predicted from the number of doctors per 10 000 people, <em class="v">doctors</em>, for a randomly selected sample of 20 countries.',
    W_(470,SC(DOC,(0,50),(0,450),5,50,'doctors (per 10 000 people)','TV sets (per 1000 people)',W=600,H=270,r=4.5,fs=12,tl=((0,113),(50,348)),tl_hid=False,sid='d2s')),
    'From the scatterplot above, it can be concluded that'),
  [('Direction','the line slopes up: positive: more doctors goes with more TV sets','data-hi="#d2s|p|hy"'),
   ('Association, not cause','a scatterplot shows an association; it cannot show cause (B, C ✗)')],
  'Fewer doctors is associated with fewer TV sets: <b>A</b>.','VCAA 2026 General Mathematics Exam 1 Q7–8 stem and Q7 (scatterplot redrawn; 2026 report not yet released)',
  mc=['a smaller number of <em>doctors</em> is associated with a smaller number of <em>TV sets</em>.','a smaller number of <em>doctors</em> causes a smaller number of <em>TV sets</em>.',
      'a smaller number of <em>doctors</em> causes a larger number of <em>TV sets</em>.','a larger number of <em>doctors</em> is associated with a smaller number of <em>TV sets</em>.'],key='A',stat=('new',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide xs"',1)
# ================= Do Now 3: VCAA 2023 E2 Q3b (2G)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q3b','Review of 2G',
  G('The scatterplot below plots the average monthly ice cream <em class="v">consumption</em>, in litres/person, against average monthly <em class="v">temperature</em>, in °C. The data for the graph was recorded in the Northern Hemisphere.',
    W_(400,SC(ICE,(-10,25),(0.10,0.22),5,0.02,'temperature (°C)','consumption (litres/person)',W=520,H=250,r=4.5,fs=12,sid='d3s')),
    'When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>consumption</em> = 0.1404 + 0.0024 × <em>temperature</em><br>The coefficient of determination is 0.7212<br>'
    'b. Determine the value of the correlation coefficient <i>r</i>.<br>Round your answer to three decimal places. <span class="muted">(1 mark)</span>'),
  [fx('Back to r','<i>r</i>',F('±√',V('r²','0.7212')),'±0.84923…'),('Sign','slope 0.0024 &gt; 0 (points trend upwards): positive','data-hi="#d3s|p|hy"')],
  '<i>r</i> = <b>0.849</b>','VCAA 2023 General Mathematics Exam 2 Q3b (examiner report: some students squared the coefficient of determination; scatterplot redrawn)',stat=('mark',69),cmd=('Determine',1,'3 d.p.')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2026 E2 Q3c (1H/1G)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q3c','Review of 1G–1H',
  '<div style="font-size:23px">The happiness level scores for a group of 2000 students are collected as a data set. The data set is modelled by a normal distribution with a mean of 72 and a standard deviation of 8.0<br><br>'
  'c. The standardised scores for the upper and lower quartiles of happiness level in this data set are <i>z</i> = 0.675 and <i>z</i> = −0.675 respectively.<br>Calculate the upper fence of the happiness level for this data set. <span class="muted">(2 marks)</span></div>',
  [fx('Quartile from z','<i>Q</i><sub>3</sub>',F(V('x̄','72'),' + ',V('z','0.675'),' × ',V('s','8.0')),'77.4'),
   fx('Lower quartile','<i>Q</i><sub>1</sub>',F(V('x̄','72'),' − ',V('z','0.675'),' × ',V('s','8.0')),'66.6'),
   ('IQR','77.4 − 66.6 = 10.8'),
   fx('Upper fence','UF',F(V('Q₃','77.4'),' + 1.5 × ',V('IQR','10.8')),'93.6')],
  'Upper fence = <b>93.6</b>','VCAA 2026 General Mathematics Exam 2 Q3 stem and Q3c (2026 report not yet released)',stat=('new',),cmd=('Calculate',2,'quartiles → IQR → fence')))

# ================= APK 1: Cambridge U1&2 7D #8 (data 7A #2)
a_,b_=lsq([p[0] for p in FOOT],[p[1] for p in FOOT])
FT='<table class="t tight" style="font-size:13px"><tr><th><i>height</i></th>'+''.join(f'<td>{h}</td>' for h,_ in FOOT)+'</tr><tr><th><i>foot length</i></th>'+''.join(f'<td>{f}</td>' for _,f in FOOT)+'</tr></table>'
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7D #8','Finding the least squares line on CAS',
  '<div style="font-size:21px">In order to predict the length of a person’s foot from their height, a group of 16 students collected the following data set, which gives height (<em class="v">height</em>) and the length of their foot (<em class="v">foot length</em>) in centimetres.</div>'
  f'<div style="margin:10px 0">{FT}</div><div style="font-size:21px">Find the equation of the least squares line which would enable foot length to be predicted from height. Give the values of the intercept and slope, rounded to two decimal places.</div>',
  [('EV and RV','predict foot length <b>from</b> height: EV height (<i>x</i>), RV foot length (<i>y</i>)'),('CAS','Linear Reg: XList height, YList foot length'),
   ('Read off',f'<i>a</i> = {a_:.4f}… · <i>b</i> = {b_:.4f}…')],
  f'<em>foot length</em> = <b>{a_:.2f} + {b_:.2f} × <em>height</em></b>',f'{CAM12} · Ch 7 skills checklist 7D #8 (data: 7A #2) · solution worked for 12MAG',cmd=('Find',None,'EV first, then CAS')))
# ================= APK 2: Cambridge U1&2 5E #7
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 5E #7','Slope of a straight line',
  '<div style="font-size:28px">Find the slope of the line that goes through the points (1, 8) and (4, 2).</div>',
  [fx('Slope','<i>b</i>',F(FR([V('y₂','2'),' − ',V('y₁','8')],[V('x₂','4'),' − ',V('x₁','1')])),'−6 ÷ 3 = −2')],
  'The slope is <b>−2</b>.',f'{CAM12} · Ch 5 skills checklist 5E #7',cmd=('Find',None,'rise over run')))
# ================= APK 3: Edrolo U1&2 6C Q11 (adapted)
S.append(qslide('apk','APK · Year 11 · VCAA 2017 Exam 2 Q4cii (adapted)','Limits of a prediction',
  '<div style="font-size:22px">A large colony of ants grows in size each year. The association between the <em class="v">population</em> of the colony and <em class="v">year</em> is approximately linear. The data is shown in the following table.</div>'
  '<div style="margin:10px 0">'+rowtab([('<i>year</i>',*range(2014,2023)),('<i>population</i> (mil)','18.2','19.0','19.9','20.8','22.0','22.8','23.2','23.8','25.3')],15)+'</div>'
  '<div style="font-size:22px">The line of good fit predicts that the population of the ant colony by the year 2026 will be approximately 28.5 million.<br>Give a reason why this prediction may have limited reliability. <span class="muted">(1 mark)</span></div>',
  [('Data range','the data covers 2014 to 2022'),('2026','is outside the data range: extrapolation')],
  'The prediction is an extrapolation: 2026 is beyond the range of the data (2014–2022), so the linear trend may not continue.',
  f'{EDR12} · 6C Q11 · adapted (by Edrolo) from VCAA 2017 Further Mathematics Exam 2 Core Q4cii · % from the 2017 examiner report',stat=('mark',53),cmd=('Give',1,'a reason')))
# ================= APK 4: VCAA 2021 E2 Q3eii
S.append(qslide('apk','APK · Year 11 · VCAA 2021 Exam 2 Q3eii','Assumptions behind a prediction',
  '<div style="font-size:23px">Data on the winning time, in seconds, for the women’s 100 m freestyle swim, for each year that the Olympic Games were held during the period 1956 to 2016, was used to model the decreasing trend in the winning time over this period.<br><br>'
  'e. The following equation can be used to predict the winning time for the women’s 100 m freestyle in the future.<div style="text-align:center;margin:8px 0"><em>winning time</em> = 357.1 – 0.1515 × <em>year</em></div>'
  'ii. What assumption is being made when this equation is used to predict the winning time for the women’s 100 m freestyle in 2032? <span class="muted">(1 mark)</span></div>',
  [('Extrapolation','2032 is beyond the data (1956–2016)'),('Link to the equation','the model only works if the same decreasing trend keeps going')],
  'It is assumed that the same decreasing trend in winning time continues in the future (up to 2032).',
  f'{EDR12} · 6C Q12 · VCAA 2021 Further Mathematics Exam 2 Core Q3eii (examiner report; original wording; stem shortened: plot not needed)',stat=('mark',18),cmd=('What',1,'refer to the trend')))

# ================= Learn: residuals and the least squares line
RES=('<svg viewBox="0 0 520 300" width="100%"><line x1="40" y1="260" x2="500" y2="260" stroke="#333" stroke-width="2"/><line x1="40" y1="20" x2="40" y2="260" stroke="#333" stroke-width="2"/>'
     '<line class="frag" x1="40" y1="230" x2="500" y2="60" stroke="#d2475b" stroke-width="3"/>'
     +''.join(f'<g class="frag"><line x1="{x}" y1="{230-(x-40)*170/460:.0f}" x2="{x}" y2="{y}" stroke="#2e7d32" stroke-width="3" stroke-dasharray="5 4"/><circle cx="{x}" cy="{y}" r="7" fill="#1f4fb0"/>'
              f'<text x="{x+8}" y="{(y+230-(x-40)*170/460)/2:.0f}" font-size="16" fill="#2e7d32">d{k+1}</text></g>' for k,(x,y) in enumerate([(100,240),(180,140),(270,190),(360,95),(450,120)]))
     +'<text x="270" y="290" text-anchor="middle" font-size="16" font-style="italic">x (EV)</text></svg>')
S.append(learn('Learn · 3A','Residuals and the least squares line',
  '<h4>Residuals</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>residual = vertical distance from a point to the line</li><li>above the line: positive · below: negative · on it: zero</li>'
  '<li>the <b>least squares line</b> makes d1² + d2² + … + dn² as small as possible</li><li>we square them because the residuals always add to 0</li></ul>',
  W_(470,RES),'Assumptions first: numerical data, a linear association, no clear outliers.',f'{CAM}, 3A pp. 169–170 (diagram redrawn)',
  cards=(kcard('Residual','actual − predicted'),kcard('Least squares line','minimises the sum of the squared residuals'))))
# ================= Learn: the formulas
S.append(learn('Learn · 3A','The equation of the least squares line',
  '<h4>Three steps</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Decide the EV (<i>x</i>) and RV (<i>y</i>)</li><li>Slope <i>b</i> = <i>r s<sub>y</sub></i> ÷ <i>s<sub>x</sub></i></li><li>Intercept <i>a</i> = <i>ȳ</i> − <i>b x̄</i>, then write <i>y</i> = <i>a</i> + <i>bx</i> in the variable names</li></ol>'
  '<p style="font-size:19px">Turned round: <i>r</i> = <i>b s<sub>x</sub></i> ÷ <i>s<sub>y</sub></i></p>',
  '<div style="font-size:30px;text-align:center;line-height:2"><span class="frag" style="background:#bbdefb;padding:2px 10px;border-radius:6px"><b>RV</b></span> = '
  '<span class="frag" style="background:#fff3c4;padding:2px 10px;border-radius:6px"><b>a</b> (intercept)</span> + '
  '<span class="frag" style="background:#c8e6c9;padding:2px 10px;border-radius:6px"><b>b</b> (slope)</span> × '
  '<span class="frag" style="background:#e1bee7;padding:2px 10px;border-radius:6px"><b>EV</b></span></div>',
  'Swap the EV and RV and you get a different (wrong) line: decide them before you start.',f'{CAM}, 3A pp. 170–171',
  cards=(kcard('Slope','<i>b</i> = <i>r s<sub>y</sub></i> / <i>s<sub>x</sub></i>'),kcard('Intercept','<i>a</i> = <i>ȳ</i> − <i>b x̄</i>'))))

# ================= WE1 / YT Edrolo 3A WE3
S.append(qslide('we','Worked example 1 · 3A','Least squares line from summary statistics',
  '<div style="font-size:22px">The height and weight of 11 people have been recorded, and the values of the following statistics determined:</div>'
  +stats(['height','weight'],[('mean','173.3 cm','65.45 kg'),('standard deviation','7.444 cm','7.594 kg')])+'<div style="font-size:20px;text-align:center">correlation coefficient <i>r</i> = 0.8502</div>'
  '<div style="font-size:22px;margin-top:8px">Use the formula to determine the equation of the least squares regression line that enables weight to be predicted from height. Calculate the values of the slope and intercept rounded to two decimal places.</div>',
  [('EV and RV','EV: height (<i>x</i>) · RV: weight (<i>y</i>)'),
   fx('Slope','<i>b</i>',F(FR([V('r','0.8502'),' × ',V('s<sub>y</sub>','7.594')],[V('s<sub>x</sub>','7.444')])),'0.87'),
   fx('Intercept','<i>a</i>',F(V('ȳ','65.45'),' − ',V('b','0.8673…'),' × ',V('x̄','173.3')),'−84.86')],
  '<i>y</i> = −84.86 + 0.87<i>x</i>, or <b><em>weight</em> = −84.86 + 0.87 × <em>height</em></b>',f'{CAM} · Example 1 (pp. 171–172)',video='Cambridge GO · Example 1 (3A Resources)',cmd=('determine',None,'b first, then a')))
S.append(qslide('yt','You try · Edrolo 3A WE3','Least squares line from summary statistics',
  '<div style="font-size:24px">Consider the following summary statistics for a set of bivariate data involving the variables <i>x</i> and <i>y</i>.<div style="text-align:center;margin:14px 0"><i>r</i> = 0.845, <i>x̄</i> = 11.0, <i>ȳ</i> = 29.2, <i>s<sub>x</sub></i> = 6.06, <i>s<sub>y</sub></i> = 16.8</div>'
  'Find the equation of the least squares regression line that allows <i>y</i> to be predicted from <i>x</i>. Give all values correct to three significant figures.</div>',
  [fx('Slope','<i>b</i>',F(FR([V('r','0.845'),' × ',V('s<sub>y</sub>','16.8')],[V('s<sub>x</sub>','6.06')])),'2.342…'),
   fx('Intercept','<i>a</i>',F(V('ȳ','29.2'),' − ',V('b','2.342…'),' × ',V('x̄','11.0')),'3.431…')],
  '<b><i>y</i> = 3.43 + 2.34<i>x</i></b>',f'{EDR} · 3A Worked example 3 (p. 161)',cmd=('Find',None,'3 s.f.')))
# ================= WE2 / YT-3A-2
S.append(qslide('we','Worked example 2 · 3A','The correlation coefficient from the slope',
  '<div style="font-size:23px">Use the following information to find the value of the correlation coefficient <i>r</i>, rounded to three decimal places.</div>'
  +stats(['hours studied','exam score'],[('mean','5.87','68.3'),('standard deviation','1.34','5.42')])+
  '<div style="font-size:21px;text-align:center">least squares equation: <em>exam score</em> = 52.7 + 2.45 × <em>hours studied</em></div>',
  [('EV and RV','EV: hours studied (<i>x</i>) · RV: exam score (<i>y</i>)'),('Needed','<i>b</i> = 2.45 · <i>s<sub>x</sub></i> = 1.34 · <i>s<sub>y</sub></i> = 5.42'),
   fx('r from the slope','<i>r</i>',F(FR([V('b','2.45'),' × ',V('s<sub>x</sub>','1.34')],[V('s<sub>y</sub>','5.42')])),'0.606')],
  'Correlation coefficient <i>r</i> = <b>0.606</b> (three decimal places)',f'{CAM} · Example 2 (pp. 172–173)',video='Cambridge GO · Example 2 (3A Resources)',cmd=('find',None,'r = b s<sub>x</sub> / s<sub>y</sub>')))
y2=YTW['YT-3A-2']
S.append(qslide('yt','You try · written for 12MAG (YT-3A-2)','The correlation coefficient from the slope',
  '<div style="font-size:23px">Use the following information to find the value of the correlation coefficient <i>r</i>, rounded to three decimal places.</div>'
  +stats(['hours of sleep','reaction test score'],[('mean','7.42','61.8'),('standard deviation','2.05','9.42')])+
  '<div style="font-size:21px;text-align:center">least squares equation: <em>reaction test score</em> = 38.2 + 3.18 × <em>hours of sleep</em></div>',
  [('EV and RV','EV: hours of sleep (<i>x</i>) · RV: reaction test score (<i>y</i>)'),
   fx('r from the slope','<i>r</i>',F(FR([V('b','3.18'),' × ',V('s<sub>x</sub>','2.05')],[V('s<sub>y</sub>','9.42')])),'0.692')],
  '<i>r</i> = <b>0.692</b>',f'Written for 12MAG (modelled on {CAM} Example 2; no Edrolo match)',cmd=('find',None,'r = b s<sub>x</sub> / s<sub>y</sub>')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['lsrl']
ca,cb=lsq(CH,CW); cr=corr(CH,CW)
S.append(cas('CAS · 3A','Finding the least squares line',
  '<p style="font-size:20px">The following data give the height (in cm) and weight (in kg) of 11 people.</p>'
  +rowtab([('Height (<i>x</i>)',*CH),('Weight (<i>y</i>)',*CW)],13)+
  '<p style="font-size:20px;margin-top:8px">Determine and graph the equation of the least squares regression line that will enable weight to be predicted from height. Write the intercept and slope rounded to three significant figures.</p>'
  +W_(330,SC(list(zip(CH,CW)),(160,186),(50,80),5,5,'height','weight',W=380,H=230,r=4.5,fs=12,tl=((160,ca+cb*160),(186,ca+cb*186)),tl_hid=False)),
  C['ti'],C['classpad'],f'<i>a</i> = {ca:.2f}… · <i>b</i> = {cb:.4f}… · <i>r</i>² = {cr*cr:.3f} → <b><em>weight</em> = −84.8 + 0.867 × <em>height</em></b>',
  f'{CAM} · 3A CAS 1 (pp. 173–175) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
fa,fb=lsq(FATH,SON)
S.append(qslide('yt','You try · Edrolo 3A WE1 (CAS)','Finding the least squares line on CAS',
  '<div style="font-size:22px">The following table gives the heights, in cm, of fathers and their sons when they were the same age.</div><div style="margin:12px 0">'
  +rowtab([('height of father (cm)',*FATH),('height of son (cm)',*SON)],15)+'</div>'
  '<div style="font-size:22px">Determine the equation of the least squares regression line that will allow the <em class="v">height of son</em> to be predicted from the <em class="v">height of father</em>. Give values correct to three significant figures.</div>',
  [('EV and RV','predict height of son <b>from</b> height of father: EV father, RV son'),('CAS','Linear Reg: XList father, YList son'),('Read off',f'<i>a</i> = {fa:.3f}… · <i>b</i> = {fb:.4f}…')],
  '<b><em>height of son</em> = 23.2 + 0.857 × <em>height of father</em></b>',f'{EDR} · 3A Worked example 1 (p. 157)',cmd=('Determine',None,'EV first, 3 s.f.')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 1 Q13','Show what you know',
  'The statistical analysis of a set of bivariate data involving variables <i>x</i> and <i>y</i> resulted in the information displayed in the table below.'
  +stats(['',''],[('Mean','<i>x̄</i> = 27.8','<i>ȳ</i> = 33.4'),('Standard deviation','<i>s<sub>x</sub></i> = 2.33','<i>s<sub>y</sub></i> = 3.24'),('Equation of the least squares line','<i>y</i> = –2.84 + 1.31<i>x</i>','')],17).replace('<tr><th></th><th></th><th></th></tr>','')+
  'Using this information, the value of the correlation coefficient <i>r</i> for this set of bivariate data is closest to',
  [fx('r from the slope','<i>r</i>',F(FR([V('b','1.31'),' × ',V('s<sub>x</sub>','2.33')],[V('s<sub>y</sub>','3.24')])),'0.942…')],
  '<i>r</i> ≈ 0.94: <b>D</b>.',f'{EDR} · 3A Q13 · VCAA 2018 Further Mathematics Exam 1 Q13 (examiner report; original wording)',
  mc=['0.88','0.89','0.92','0.94','0.97'],key='D',dist=[9,13,22,49,6]))
wa,wb=lsq(HTC,WT); above=[(h,w) for h,w in zip(HTC,WT) if wa+wb*h>w]
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2021 Exam 1 Q11','Show what you know',
  'The table below shows the weight, in kilograms, and the height, in centimetres, of 10 adults.<div style="margin:8px 0">'
  +rowtab([('Weight (kg)',*WT),('Height (cm)',*HTC)],15)+'</div>'
  'A least squares line is fitted to the data.<br>The least squares line enables an adult’s weight to be predicted from their height.<br>The number of times that the predicted value of an adult’s weight is greater than the actual value of their weight is',
  [('EV and RV','predict weight from height: EV height, RV weight'),('CAS',f'<em>weight</em> = {wa:.1f} + {wb:.3f} × <em>height</em>'),
   ('Compare','predicted &gt; actual means the point is <b>below</b> the line (negative residual): count them'),('Count',f'{len(above)} adults')],
  f'{len(above)} times: <b>D</b>.',f'{EDR} · 3A Q14 · VCAA 2021 Further Mathematics Exam 1 Q11 (examiner report; original wording)',
  mc=['3','4','5','6','7'],key='D',dist=[14,29,11,40,5],dis=('B','29% counted the points above the line (predicted less than actual): 4.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide sm"',1)
fe_a,fe_b=191,31.3
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2017 Exam 2 Q3a, bi','Show what you know',
  '<div style="font-size:15px">The <em class="v">number of male moths</em> caught in a trap set in a forest and the <em class="v">egg density</em> (eggs per square metre) in the forest are shown in the table below.'
  +rowtab([('<i>Number of male moths</i>',*MALE),('<i>Egg density</i> (eggs per m²)',*EGG)],13)+
  'The <em class="v">number of female moths</em> caught in a trap set in a forest and the <em class="v">egg density</em> (eggs per square metre) in the forest can also be examined. A scatterplot of the data is shown below.'
  +W_(330,SC(FEM,(10,60),(0,2500),5,500,'number of female moths','egg density',W=420,H=200,r=4.5,fs=11,sid='x3s'))+
  'The equation of the least squares line is <em>egg density</em> = 191 + 31.3 × <em>number of female moths</em></div>'+
  plist([('a','Determine the equation of the least squares line that can be used to predict the egg density in the forest from the number of male moths caught in the trap. Round your answers to one decimal place. (2 marks)'),
         ('b i','Draw the graph of this least squares line on the scatterplot. (1 mark)')]),
  [],'',f'{EDR} · 3A Q15 · VCAA 2017 Further Mathematics Exam 2 Core Q3a, bi (examiner report: a 67% full marks, bi 26%: the horizontal axis starts at 10, not 0)',stat=('avg',60),cmd=('Determine',2,'EV = male moths'),
  parts=[('a','<em>egg density</em> = <b>−46.8 + 18.9</b> × <em>number of male moths</em>'),
         ('b i','Two points from the equation: <i>x</i> = 10 → 504 · <i>x</i> = 60 → 2069; rule a line between them.'+W_(300,SC(FEM,(10,60),(0,2500),5,500,'','',W=380,H=170,r=4,fs=10,tl=((10,fe_a+fe_b*10),(60,fe_a+fe_b*60)),tl_hid=False)))]))
S[-1]=S[-1].replace('<section class="slide T ex mp"','<section class="slide T ex mp xs"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 3 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('3A',) and v.get('url')]))
n=assemble(S,'12MAG · L09 · Least squares regression line',os.path.join(ROOT,'lessons','3A slides.html'))
print(n-1,'slides')
