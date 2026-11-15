"""Lesson l11 (3C) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/3C slides.html
Run: python3 tools/deck/l11/build.py      Screenshots: python3 tools/deck/l11/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- CFAT 1.3.1 slide first (as planned on the card).
- Do Now: VCAA 2023 Exam 1 Q9 (B, 59%; A 9 B 59 C 18 D 10 E 3) · VCAA 2026 NHT Exam 1 Q9 (B; NHT report: answers only) ·
          VCAA 2024 Exam 2 Q3 stem + Q3e (54% full marks; Table 2 and scatterplot shared with l07 Do Now 3) · VCAA 2023 Exam 2 Q1 stem + Q1cii (27%; 9.53).
- APK: Cambridge U1&2 Ch 5 skills checklist 5A #1 ($110) and 5E #8 (y-intercept −7, slope 2) ·
       VCAA 2017 Further Exam 1 Q8 (= Edrolo U1&2 6D Q14, which changes the variables; original wording; B, 43%; A 3 B 43 C 6 D 39 E 9) ·
       VCAA 2016 Further Exam 2 Q3bii (= Edrolo U1&2 6D Q15; Edrolo's adapted wording: the original refers to the line found in part bi; 28%).
- Learn: Cambridge Units 3&4 3B pp. 184-188 and 3C pp. 195-196 (own words).
- Worked examples: Cambridge U3&4 Examples 6 (p. 184), 7 (pp. 186-187; the book's solution labels plot D as 'Plot B' twice: shown as D), 8 (p. 188).
  You trys: Edrolo U3&4 3C Worked example 2 (pp. 181-183), Worked example 3 (p. 185) · YT-3B-8 (planner/written-youtrys.json, written for 12MAG).
- CAS: planner/cas-skills.json 'residuals', 'regression-analysis'; data = Cambridge 3C CAS 2 (birth rate, life expectancy, pp. 195-196).
- Exits: Edrolo U3&4 3C Q11 = VCAA 2018 Further Exam 2 Q2e (original wording; 59%; 85%) · 3C Q13 = VCAA 2019 Further Exam 2 Q5fi, fii
  (original wording; 41%, 36%) · 3C Q14 = VCAA 2021 Further Exam 2 Q3b (original wording, the card lists Edrolo's adaptation; 19%; −0.938).
- Videos: videos.json (3B, 3C: links still blank).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l11')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13):
    return f'<table class="t tight" style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def sm(cls): S[-1]=S[-1].replace('" data-cfu',' '+cls+'" data-cfu',1)

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}.rp4{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px}.rp4 b{display:block;text-align:center;font-size:15px}.casxs .cas2 li,.casxs .cas2 ol{font-size:14.5px!important;line-height:1.3!important}.casxs .wk .ans{font-size:15px!important}</style>']
# ================= opening
S.append(title(11,'Residual analysis and regression analysis',f'{CAM} · 3B (residuals, reporting) and 3C Conducting a regression analysis using data','L11').replace('font-size:84px','font-size:60px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items'] if not x.startswith('No learning')]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.3.1','· about 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· four Year 11 questions','var(--apk)'),
  ('Residuals, residual plots, reports','',None),('Worked examples 6–8','→ You try',None),('CAS: residual plot and full regression analysis','',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.3.1','Fitting and interpreting the least squares line','3A–3B',15,'Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))
S.append(keys([
  ('Residual','the vertical distance from the least squares line to a data point'),
  ('Residual plot','residuals (vertical axis) plotted against the EV (horizontal axis)'),
  ('Random scatter','no clear pattern around 0: supports the linearity assumption'),
  ('Clear pattern','e.g. a curve: the association is not linear')],
  [('Residual',F('actual − predicted'),'above the line: + · below: − · on it: 0'),
   ('Prediction',F('RV = <i>a</i> + <i>b</i> × (EV value)'),'substitute the EV value'),
   ('Coefficient of determination',F('<i>r</i>² × 100%'),'% of variation in the RV explained by the EV'),
   ('Correlation from r²',F('<i>r</i> = ±√<i>r</i>²'),'sign = sign of the slope')],
  f'{CAM}, 3B pp. 184–188'))

# ================= Do Now 1: VCAA 2023 E1 Q9 (3B)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q9','Review of 3A–3B',
  '<div style="font-size:20px">A least squares line can be used to model the birth rate (children per 1000 population) in a country from the average daily food energy intake (megajoules) in that country.<br>'
  'When a least squares line is fitted to data from a selection of countries it is found that:<ul class="bul" style="margin:6px 0 6px 24px"><li>for a country with an average daily food energy intake of 8.53 megajoules, the birth rate will be 32.2 children per 1000 population</li>'
  '<li>for a country with an average daily food energy intake of 14.9 megajoules, the birth rate will be 9.9 children per 1000 population.</li></ul>The slope of this least squares line is closest to</div>',
  [('Two points on the line','(8.53, 32.2) and (14.9, 9.9): EV = energy intake, RV = birth rate'),
   fx('Slope','<i>b</i>',F(FR([V('y₂','9.9'),' − ',V('y₁','32.2')],[V('x₂','14.9'),' − ',V('x₁','8.53')])),'−22.3 ÷ 6.37 = −3.5')],
  'Slope ≈ −3.5: <b>B</b>.','VCAA 2023 General Mathematics Exam 1 Q9 (examiner report)',
  mc=['−4.7','−3.5','−0.29','2.7','25'],key='B',dist=[9,59,18,10,3],
  dis=('C','18% divided the other way round (run ÷ rise): 6.37 ÷ −22.3 = −0.29.')))
# ================= Do Now 2: VCAA 2026 NHT E1 Q9 (2F)
MW,MH=420,250
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 NHT Exam 1 Q9','Review of 2F',
  G('The <em class="v">minimum temperature</em>, in degrees Celsius, is recorded as a whole number for five consecutive days. The data is shown in the graph below.',
    W_(380,ts(MINT,(0,6),(0,12),1,1,'day','minimum temperature (°C)',W=MW,H=MH,r=4.5,fs=12)),
    'The value of Pearson’s correlation coefficient, <i>r</i>, between <em class="v">minimum temperature</em> and <em class="v">day</em>, is closest to'),
  [('Read the data','day 1–5: 8, 10, 7, 9, 8'),('CAS','enter day and minimum temperature in two lists; Linear Reg (a+bx) gives <i>r</i>'),
   ('Read off','<i>r</i> = −0.1387: very weak, negative')],
  '<i>r</i> ≈ −0.139: <b>B</b>.','VCAA 2026 (NHT) General Mathematics Exam 1 Q9 (NHT report: answer only, no %; graph redrawn)',
  mc=['−0.019','−0.139','0.019','0.039'],key='B',stat=('nht',)))
# ================= Do Now 3: VCAA 2024 E2 Q3e (3B)
WT='<table class="t tight" style="font-size:12px"><tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y in WYR)+'</tr><tr><th><i>Wgold</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WGOLD)+'</tr><tr><th><i>Wbest</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WBEST)+'</tr></table>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q3e','Review of 3B',
  '<div style="font-size:15.5px">The Olympic gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, is often lower than the best height achieved in other international women’s high jump competitions in that same year.<br>Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.</div>'
  f'<div style="margin:5px 0">{WT}</div><div style="display:flex;gap:10px;align-items:center"><div style="flex:none;width:280px">'+SC(list(zip(WGOLD,WBEST)),(1.90,2.08),(1.92,2.10),0.02,0.02,'Wgold (m)','Wbest (m)',W=400,H=260,r=4.5,fs=11,tl=((1.90,0.300+0.860*1.90),(2.08,0.300+0.860*2.08)),tl_hid=False)+'</div>'
  '<div style="font-size:15.5px">When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em><br>'
  'e. Referring to the equation of the least squares line, interpret the value of the slope in terms of the variables <em class="v">Wbest</em> and <em class="v">Wgold</em>. <span class="muted">(1 mark)</span></div></div>',
  [('EV and RV','EV <em>Wgold</em> · RV <em>Wbest</em>'),('Slope','<i>b</i> = 0.860 (rounded: 0.86): change in <em>Wbest</em> for each 1 m increase in <em>Wgold</em>')],
  'On average, for each 1 metre increase in <em>Wgold</em>, <em>Wbest</em> increases by 0.86 metres.',
  'VCAA 2024 General Mathematics Exam 2 Q3 stem and Q3e (examiner report: students did not always reference the change in both variables; scatterplot redrawn)',stat=('mark',54),cmd=('Interpret',1,'both variables change')))
sm('sm')
# ================= Do Now 4: VCAA 2023 E2 Q1cii (3B)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q1cii','Review of 3B',
  '<div style="font-size:21px">c. When a least squares line is used to model the association between oyster weight and volume, the equation is:'
  '<div style="text-align:center;margin:10px 0"><em>volume</em> = 0.780 + 0.953 × <em>weight</em></div>'
  'ii. Complete the following sentence by filling in the box provided. <span class="muted">(1 mark)</span><br><br>'
  'This equation predicts that, on average, each 10 g increase in the weight of an oyster is associated with a <span style="display:inline-block;width:110px;height:30px;border:2px solid #333;vertical-align:middle"></span> cm³ increase in its volume.</div>',
  [('Slope','0.953: the increase in volume for each <b>1 g</b> increase in weight'),fx('For 10 g','increase',F(V('b','0.953'),' × 10'),'9.53')],
  '… associated with a <b>9.53</b> cm³ increase in its volume.',
  'VCAA 2023 General Mathematics Exam 2 Q1c stem and Q1cii (examiner report: not answered well; a frequent response was 0.953)',stat=('mark',27),cmd=('Complete',1,'10 × the slope')))

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 5A #1','Substituting into a linear formula',
  '<div style="font-size:26px">The cost, <i>C</i>, of hiring a trailer is <i>C</i> = 10<i>t</i> + 50, where <i>t</i> is the time in hours.<br><br>How much will it cost to hire the trailer for 6 hours?</div>',
  [fx('Substitute','<i>C</i>',F('10 × ',V('t','6'),' + 50'),'110')],
  'It will cost <b>$110</b>.',f'{CAM12} · Ch 5 skills checklist 5A #1 (answer p. 820)',cmd=('substitute',None,'replace t with 6')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 5E #8','Intercept and slope from an equation',
  '<div style="font-size:26px">What is the <i>y</i>-intercept and the slope of the straight line <i>y</i> = −7 + 2<i>x</i>?</div>',
  [('Form','<i>y</i> = <i>a</i> + <i>bx</i>: <i>a</i> is the intercept, <i>b</i> is the slope'),('Match','<i>a</i> = −7 · <i>b</i> = 2')],
  '<i>y</i>-intercept = −7, slope = 2',f'{CAM12} · Ch 5 skills checklist 5E #8 (answer p. 820)',cmd=('What',None,'match to y = a + bx')))
S.append(qslide('apk','APK · Year 11 · VCAA 2017 Exam 1 Q8','Equation from a line on a scatterplot',
  G('The scatterplot below shows the <em class="v">wrist</em> circumference and <em class="v">ankle</em> circumference, both in centimetres, of 13 people. A least squares line has been fitted to the scatterplot with <em class="v">ankle</em> circumference as the explanatory variable.',
    W_(330,SC(WRIST,(21,26),(16,20),1,1,'ankle circumference (cm)','wrist circumference (cm)',W=420,H=270,r=4.5,fs=11,tl=((21,10.2+0.342*21),(26,10.2+0.342*26)),tl_hid=False)),
    'The equation of the least squares line is closest to'),
  [('Which variable is y?','ankle is the EV, so the equation is <em>wrist</em> = … (A, C ✗)'),
   ('Slope','the line rises from about 17.4 (ankle 21) to 19.1 (ankle 26): 1.7 ÷ 5 ≈ 0.34 (E ✗)'),
   ('Intercept','the axis starts at 21, not 0: 17.4 is not the intercept; 17.4 − 0.342 × 21 ≈ 10.2')],
  '<em>wrist</em> = 10.2 + 0.342 × <em>ankle</em>: <b>B</b>.',
  f'{EDR12} · 6D Q14 (adapted by Edrolo) · VCAA 2017 Further Mathematics Exam 1 Q8 (examiner report; original wording; scatterplot redrawn)',
  mc=['<em>ankle</em> = 10.2 + 0.342 × <em>wrist</em>','<em>wrist</em> = 10.2 + 0.342 × <em>ankle</em>','<em>ankle</em> = 17.4 + 0.342 × <em>wrist</em>','<em>wrist</em> = 17.4 + 0.342 × <em>ankle</em>','<em>wrist</em> = 17.4 + 0.731 × <em>ankle</em>'],
  key='B',dist=[3,43,6,39,9],dis=('D','39% read 17.4 off the vertical axis, but that axis is at ankle = 21 cm, not 0.')))
sm('xs')
S.append(qslide('apk','APK · Year 11 · VCAA 2016 Exam 2 Q3bii (adapted)','Interpreting the intercept',
  G('The data in the following scatterplot shows a sample of actual temperatures and apparent temperatures recorded at a weather station.',
    W_(340,SC(list(zip(ACT,APP)),(20,29),(16,26),1,1,'actual temperature (°C)','apparent temperature (°C)',W=420,H=260,r=4.5,fs=11)),
    'A line of good fit has the equation<div style="text-align:center"><em>apparent temperature</em> = −1.7 + 0.94 × <em>actual temperature</em></div>'
    'Interpret the intercept of the line of good fit in terms of the variables <em class="v">apparent temperature</em> and <em class="v">actual temperature</em>. <span class="muted">(1 mark)</span>'),
  [('EV and RV','EV actual temperature · RV apparent temperature'),('Intercept','<i>a</i> = −1.7: the RV when the EV = 0')],
  'On average, when the actual temperature is 0 °C, the apparent temperature is −1.7 °C.',
  f'{EDR12} · 6D Q15 · adapted (by Edrolo) from VCAA 2016 Further Mathematics Exam 2 Core Q3bii: the original uses the line found in part bi (examiner report; scatterplot redrawn)',
  stat=('mark',28),cmd=('Interpret',1,'RV when EV = 0')))
sm('sm')

# ================= Learn
cx,cy=zip(*CARS); ca,cb=lsq(cx,cy); CRES=[(x,y-(ca+cb*x)) for x,y in CARS]
S.append(learn('Learn · 3B','Residuals',
  '<h4>Residual = actual − predicted</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>the vertical distance from the line to a data point</li><li>point above the line: <b>positive</b> · below: <b>negative</b> · on it: <b>zero</b></li>'
  '<li>the residuals always have a mean of 0</li></ul>',
  '<div style="display:flex;gap:14px;align-items:center">'+W_(380,SC(CARS,(0,10),(0,40000),1,5000,'Age (years)','Price (dollars)',W=440,H=250,r=4.5,fs=11,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False))+
  '<div style="font-size:20px;line-height:1.8"><div class="frag">6-year-old car: actual $6500</div><div class="frag">predicted = 35 100 − 3940 × 6 = $11 460</div><div class="frag"><b>residual = 6500 − 11 460 = −$4960</b></div><div class="frag muted">below the line → negative</div></div></div>',
  'Always actual minus predicted, never the other way round.',f'{CAM}, 3B p. 184 (scatterplot redrawn)',
  cards=(kcard('Residual','actual − predicted'),)))
S.append(learn('Learn · 3B','Reading a residual plot',
  '<h4>Residual plot: residuals against the EV</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>random scatter</b> around 0, no clear pattern → the linearity assumption is supported</li>'
  '<li><b>clear pattern</b> (e.g. a curve) → the association is not linear</li></ul>',
  '<div class="rp4" style="max-width:760px;margin:auto"><div class="frag"><b>random → linear ✓</b>'+resid(EW3['b'],(0,10),(-4,4),2,2,'x','residual',W=360,H=200,r=4.5,fs=11)+'</div>'
  '<div class="frag"><b>curved pattern → not linear ✗</b>'+resid(EW3['a'],(0,8),(-4,4),2,2,'x','residual',W=360,H=200,r=4.5,fs=11)+'</div></div>',
  'Answer the exam question in two parts: the pattern you see, then what it means for linearity.',f'{CAM}, 3B pp. 185–186 · plots: {EDR} 3C Worked example 3 (redrawn)',
  cards=(kcard('Random scatter','supports linearity'),kcard('Clear pattern','not linear'))))
S.append(learn('Learn · 3B–3C','A full regression analysis',
  '<h4>Steps (then write the report)</h4><ol style="font-size:17px;margin-left:24px;line-height:1.45"><li>EV and RV; scatterplot: direction, form, strength, outliers</li><li><i>r</i> (strength)</li>'
  '<li>least squares line <i>y</i> = <i>a</i> + <i>bx</i></li><li>interpret <i>a</i> and <i>b</i></li><li><i>r</i>² in words</li><li>predictions</li><li>residual plot: linearity check</li></ol>',
  '<div style="font-size:18px;line-height:1.6;background:#f5f7fb;padding:10px 16px;border-radius:10px">'
  '<div class="frag">strong negative linear association, <i>r</i> = −0.964, no obvious outliers</div><div class="frag"><em>price</em> = 35 100 − 3940 × <em>age</em></div>'
  '<div class="frag">slope: on average, price decreased by $3940 each year</div><div class="frag">intercept: on average, price when new was $35 100</div>'
  '<div class="frag">93% of the variation in price is explained by the variation in age</div><div class="frag">no clear pattern in the residual plot → linear ✓</div></div>',
  'Use the variable names in every line, never x and y.',f'{CAM}, 3B pp. 187–188, 3C pp. 195–196',
  cards=(kcard('Report','DFS + outliers · equation · slope · intercept · r² · residuals'),)))

# ================= WE6 / YT Edrolo 3C WE2
S.append(qslide('we','Worked example 6 · 3B','Calculating a residual',
  G('<div style="font-size:23px">The actual price of the 6-year-old car is $6500. Calculate the residual when its price is predicted using the regression equation:<div style="text-align:center;margin:8px 0"><em>price</em> = 35100 − 3940 × <em>age</em></div></div>',
    W_(360,SC(CARS,(0,10),(0,40000),1,5000,'Age (years)','Price (dollars)',W=440,H=230,r=4,fs=10,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False))),
  [('Actual','actual price: $6500'),fx('Predicted','<em>price</em>',F('35 100 − 3940 × ',V('age','6')),'$11 460'),
   fx('Residual','residual',F(V('actual','6500'),' − ',V('predicted','11 460')),'−$4960')],
  'Residual = <b>−$4960</b>',f'{CAM} · Example 6 (p. 184)',video='Cambridge GO · Example 6 (3B Resources)',cmd=('Calculate',None,'actual − predicted')))
RT=lambda pred,res,cls='': ('<table class="t tight" style="font-size:15px"><tr><th>number of people</th>'+''.join(f'<td>{v}</td>' for v in PPL)+'</tr><tr><th>actual total cost ($)</th>'+''.join(f'<td>{v}</td>' for v in COST)+'</tr>'
   '<tr><th>predicted total cost ($)</th>'+''.join(f'<td>{v}</td>' for v in pred)+'</tr><tr><th>residual value ($)</th>'+''.join(f'<td>{v}</td>' for v in res)+'</tr></table>')
PRED=[7+29*p for p in PPL]; RES=[c-p for c,p in zip(COST,PRED)]
S.append(qslide('yt','You try · Edrolo 3C WE2','Residuals and a residual plot',
  '<div style="font-size:16px">A least squares regression equation has been used to predict the <em class="v">total cost</em> ($) of a table bill at a restaurant from the <em class="v">number of people</em> eating together on the table, such that<div style="text-align:center;margin:4px 0"><em>total cost</em> = 7 + 29 × <em>number of people</em></div></div>'
  +plist([('a','If the actual <em>total cost</em> for a table of six people is $166, calculate the residual value when the <em>total cost</em> is predicted using the regression equation.'),
          ('b','There were 8 other groups of people at the restaurant. The <em>number of people</em> at each table and the <em>total cost</em> for each group were recorded and displayed in a table.'+RT(['']*8,['']*8)+'Use the regression equation to complete the table by filling in the predicted <em>total cost</em> and residual values.'),
          ('c','Construct a residual plot for this data set.')]),
  [fx('a: predicted','<em>total cost</em>',F('7 + 29 × ',V('people','6')),'181'),fx('a: residual','residual',F(V('actual','166'),' − ',V('predicted','181')),'−15'),
   ('b: each column','predicted = 7 + 29 × people, then residual = actual − predicted (e.g. 3 people: 94, 90 − 94 = −4)'),
   ('c: axes','number of people across (0 to 7), residual value up (−10 to 10); plot each residual')],'',
  f'{EDR} · 3C Worked example 2 (pp. 181–183) · residual plot redrawn',cmd=('Calculate',None,'actual − predicted'),
  parts=[('a','−15'),('b',RT(PRED,RES)),('c',W_(330,resid(list(zip(PPL,RES)),(0,7),(-10,10),1,5,'number of people','residual value',W=400,H=170,r=4.5,fs=11)))]))
sm('xs')
# ================= WE7 / YT Edrolo 3C WE3
RP=lambda k,xr=(0,12): f'<div><b>{k}</b>'+resid(EX7[k],xr,(-1,1),2,0.5,'x','Residual',W=330,H=150,r=3.5,fs=10)+'</div>'
S.append(qslide('we','Worked example 7 · 3B','Interpreting a residual plot',
  '<div style="font-size:20px">Which of the following residual plots would call into question the assumption of linearity in a regression analysis? Give reasons for your answers.</div>'
  '<div class="rp4" style="margin-top:6px">'+RP('A')+RP('B')+RP('C')+RP('D')+'</div>',
  [('Look for','a pattern or structure in the residuals (not random scatter around 0)'),('A and C','random scatter above and below 0'),('B and D','a clear curve')],
  '<b>B and D</b> call linearity into question.<br>Plot A – residuals look random, so linearity assumption is met.<br>Plot B – there is a clear curve in the residuals, the linearity assumption is not met.<br>'
  'Plot C – residuals look random, so linearity assumption is met.<br>Plot D – there is a clear curve in the residuals, the linearity assumption is not met.',
  f'{CAM} · Example 7 (pp. 186–187; the book’s solution prints “Plot B” for D) · plots redrawn',video='Cambridge GO · Example 7 (3B Resources)',cmd=('Which',None,'pattern or random?')))
sm('xs')
S.append(qslide('yt','You try · Edrolo 3C WE3','Does the residual plot support linearity?',
  '<div style="font-size:20px">Determine if the following residual plots support the assumption of linearity.</div>'
  +plist([('a',W_(330,resid(EW3['a'],(0,8),(-4,4),2,2,'x','residual',W=380,H=170,r=4,fs=10))),('b',W_(330,resid(EW3['b'],(0,10),(-4,4),2,2,'x','residual',W=380,H=170,r=4,fs=10)))]),
  [('a','the points rise then fall: a clear curved pattern'),('b','about as many points above as below 0, randomly scattered, no pattern')],'',
  f'{EDR} · 3C Worked example 3 (p. 185) · plots redrawn',cmd=('Determine',None,'pattern or random?'),
  parts=[('a','The residual plot does not support the assumption of linearity.'),('b','The residual plot supports the assumption of linearity.')]))
sm('xs')
# ================= WE8 / YT-3B-8
CARR=resid(CRES,(0,9),(-6000,4000),1,2000,'Age (years)','Residual',W=380,H=170,r=4,fs=10)
S.append(qslide('we','Worked example 8 · 3B','Reporting the results of a regression analysis',
  '<div style="font-size:21px">Construct a report to describe the association between the price and age of secondhand cars.</div>'
  '<div class="rp4" style="margin-top:6px"><div><b>scatterplot</b>'+SC(CARS,(0,10),(0,40000),1,10000,'Age (years)','Price (dollars)',W=380,H=200,r=4,fs=10,tl=((0,35100),(8.9,35100-3940*8.9)),tl_hid=False)+'</div>'
  '<div><b>residual plot</b>'+CARR+'</div></div><div style="font-size:16px;margin-top:4px"><i>r</i> = −0.964 · <em>price</em> = 35 100 − 3940 × <em>age</em> · <i>r</i>² = 0.930</div>',
  [('Association','direction, form, strength (<i>r</i>), outliers'),('Equation and coefficients','slope and intercept in context'),('<i>r</i>² and residuals','% of variation explained; pattern in residual plot?')],
  'From the scatterplot we see that there is a strong negative, linear association between the price of a second hand car and its age, <i>r</i> = −0.964. There are no obvious outliers. '
  'The equation of the least squares regression line is: <em>price</em> = 35 100 − 3940 × <em>age</em>. The slope of the regression line predicts that, on average, the price of these second-hand cars decreased by $3940 each year. '
  'The intercept predicts that, on average, the price of these cars when new was $35 100. The coefficient of determination indicates that 93% of the variation in the price of these second-hand cars is explained by the variation in their age. '
  'The lack of a clear pattern in the residual plot confirms the assumption of a linear association between the price and the age of these second-hand cars.',
  f'{CAM} · Example 8 (p. 188) · plots redrawn from the 3B car data (p. 180)',video='Cambridge GO · Example 8 (3B Resources)',cmd=('Construct',None,'report template')))
sm('xs')
ma,mb=lsq(MAGE,MPR); MRES=[(x,y-(ma+mb*x)) for x,y in zip(MAGE,MPR)]
y8=YTW['YT-3B-8']
S.append(qslide('yt','You try · written for 12MAG (YT-3B-8)','Writing a regression report',
  '<div style="font-size:20px">Construct a report to describe the association between the price and age of secondhand motorbikes.</div>'
  +rowtab([('age (years)',*MAGE),('price ($)',*[f'{p:,}'.replace(',','&nbsp;') for p in MPR])],13).replace('<td>','<td style="white-space:nowrap">')+
  '<div class="rp4" style="margin-top:6px"><div><b>scatterplot</b>'+SC(list(zip(MAGE,MPR)),(0,9),(6000,16000),1,2000,'age (years)','price ($)',W=380,H=190,r=4,fs=10,tl=((0,ma),(9,ma+mb*9)),tl_hid=False)+'</div>'
  '<div><b>residual plot</b>'+resid(MRES,(0,9),(-600,600),1,300,'age (years)','residual',W=380,H=190,r=4,fs=10)+'</div></div>',
  [('CAS','<i>r</i> = −0.993 · <em>price</em> = 15 700 − 1070 × <em>age</em> · <i>r</i>² = 0.985'),('Residual plot','no clear pattern')],
  y8['answer'],f'Written for 12MAG (modelled on {CAM} Example 8; no Edrolo match)',cmd=('Construct',None,'same template as Example 8')))
sm('xs')

# ================= CAS
CS={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}
la,lb=lsq(BIRTH,LIFE); lr=corr(BIRTH,LIFE); LRES=[(x,y-(la+lb*x)) for x,y in zip(BIRTH,LIFE)]
DT=rowtab([('Birth rate',*BIRTH),('Life expectancy (years)',*LIFE)],13)
for cid,head,task,ans in (
  ('residuals','Drawing a residual plot',
   '<p style="font-size:19px">Life expectancy (years) and birth rate (births per 1000 people) in 10 countries:</p>'+DT+
   '<p style="font-size:19px;margin-top:8px">Fit the least squares line predicting life expectancy from birth rate, then draw the residual plot.</p>'
   +W_(330,resid(LRES,(25,45),(-10,10),5,5,'birth','residual',W=400,H=190,r=4.5,fs=11)),
   'no clear pattern in the residual plot: the linearity assumption is supported'),
  ('regression-analysis','A full regression analysis',
   '<p style="font-size:19px">Same data:</p>'+DT+'<p style="font-size:19px;margin-top:8px">Conduct a regression analysis of the association between life expectancy and birth rate.</p>'
   +W_(330,SC(list(zip(BIRTH,LIFE)),(25,45),(40,70),5,5,'birth','life',W=400,H=200,r=4.5,fs=11,tl=((25,la+lb*25),(45,la+lb*45)),tl_hid=False)),
   f'<em>life</em> = {la:.1f} − {-lb:.3f} × <em>birth</em> · <i>r</i> = {lr:.4f} · <i>r</i>² = {lr*lr:.3f}')):
    C=CS[cid]
    S.append(cas('CAS · 3C',head,task,C['ti'],C['classpad'],ans,f'{CAM} · 3C CAS 2 (pp. 195–196) · Steps: CAS guide (planner)',
      videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
    if cid=='regression-analysis': sm('casxs')

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 2 Q2e','Show what you know',
  G('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>This is called the percentage congestion level.<br>'
    'The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.',
    W_(320,SC(CONG,(35,70),(35,75),5,5,'morning congestion level (%)','evening congestion level (%)',W=400,H=230,r=4,fs=11)),
    'e. The value of the correlation coefficient <i>r</i> is 0.92<br>What percentage of the variation in the evening congestion level can be explained by the variation in the morning congestion level?<br>Round your answer to the nearest whole number. <span class="muted">(1 mark)</span>'),
  [fx('Square r','<i>r</i>²',F(V('r','0.92'),'²'),'0.8464'),('As a %','0.8464 × 100 = 84.64 → 85%')],
  '<b>85%</b> (92%, the value of <i>r</i>, was a very common wrong answer).',
  f'{EDR} · 3C Q11 · VCAA 2018 Further Mathematics Exam 2 Core Q2e (examiner report; original wording; scatterplot redrawn)',stat=('mark',59),cmd=('What',1,'square r, then %')))
sm('sm')
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2019 Exam 2 Q5f','Show what you know',
  '<div style="font-size:17px">The scatterplot shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<em class="v">pressure 3 pm</em>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<em class="v">pressure 9 am</em>) for 23 days in November 2017 at a particular weather station. '
  'The equation of the least squares line is <em>pressure 3 pm</em> = 111.4 + 0.8894 × <em>pressure 9 am</em><br>f. The residual plot associated with the least squares line is shown below.</div>'
  +W_(360,resid(PRES,(1010,1030),(-3,3),5,1,'pressure 9 am (hPa)','residual (hPa)',W=440,H=200,r=4,fs=11))
  +plist([('i','The residual plot above can be used to test one of the assumptions about the nature of the association between the atmospheric pressure at 3 pm and the atmospheric pressure at 9 am. What is this assumption? <span class="muted">(1 mark)</span>'),
          ('ii','The residual plot above does not support this assumption. Explain why. <span class="muted">(1 mark)</span>')]),
  [('i','a residual plot tests whether the association is linear'),('ii','the residuals fall then rise: a clear (curved) pattern, not random')],'',
  f'{EDR} · 3C Q13 · VCAA 2019 Further Mathematics Exam 2 Core Q5fi–ii (examiner report: 41%, 36%; many contradicted themselves; original wording; plot redrawn)',stat=('mark',36),cmd=('Explain',2,'name the pattern'),
  parts=[('i','Linearity (the association is linear).'),('ii','The residuals have a clear pattern (a curve), so they are not randomly scattered.')]))
sm('xs')
SY=(1952,2016)
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2021 Exam 2 Q3b','Show what you know',
  G('The time series plot below shows the <em class="v">winning time</em>, in seconds, for the women’s 100 m freestyle swim plotted against <em class="v">year</em>, for each year that the Olympic Games were held during the period 1956 to 2016.<br>A least squares line has been fitted to the plot to model the decreasing trend in the <em>winning time</em> over this period.',
    W_(360,ts(SWIM,SY,(52,64),8,2,'year','winning time (seconds)',W=440,H=230,r=4,fs=11,tl=((1952,357.1-0.1515*1952),(2016,357.1-0.1515*2016)),tl_hid=False)),
    'The equation of the least squares line is <em>winning time</em> = 357.1 – 0.1515 × <em>year</em><br>The coefficient of determination is 0.8794<br>b. Determine the value of the correlation coefficient (<i>r</i>).<br>Round your answer to three decimal places. <span class="muted">(1 mark)</span>'),
  [fx('Square root','√<i>r</i>²',F('√',V('r²','0.8794')),'0.9378'),('Sign','the slope is negative (−0.1515), so <i>r</i> is negative')],
  '<i>r</i> = <b>−0.938</b> (many students left off the negative sign).',
  f'{EDR} · 3C Q14 (adapted by Edrolo) · VCAA 2021 Further Mathematics Exam 2 Core Q3b (examiner report; original wording; plot redrawn)',stat=('mark',19),cmd=('Determine',1,'√r², sign of the slope')))
sm('sm')

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 3 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('3B','3C') and v.get('url')]))
n=assemble(S,'12MAG · L11 · Residual analysis and regression analysis',os.path.join(ROOT,'lessons','3C slides.html'))
print(n-1,'slides')
