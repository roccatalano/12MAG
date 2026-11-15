"""Lesson l22 (5E, fitting a trend line and forecasting) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5E slides.html
Run: python3 tools/deck/l22/build.py      Screenshots: python3 tools/deck/l22/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim):
- Do Now: VCAA 2024 NHT Exam 1 Q15 (D; NHT report: answers only) ·
          VCAA 2026 Exam 1 Q10 (stem + data table; scatterplot not shown: table is enough; 2026 report not yet released; answer D checked on CAS) ·
          VCAA 2023 Exam 2 Q4c (2 marks: 21% full marks, average 0.7; plot from the stem not needed for part c, not shown) ·
          VCAA 2026 Exam 2 Q1 stem + Q1b (25%; 2026 report not yet released).
- APK: Cambridge U1&2 Ch 5 skills checklist 5F #10 (solution worked for 12MAG); card's 7E #10 was burnt in l10 → dropped.
       VCAA 2014 Exam 1 Graphs and relations Q4 (= Edrolo U1&2 4D Q13; no 2014 report on G:, % left blank) ·
       VCAA 2016 Exam 1 Graphs and relations Q2 (= Edrolo U1&2 4E Q16; original wording: Edrolo misprints option C; 94% A).
- Learn: Cambridge U3&4 5E pp. 295-298 (own words) · Edrolo 4E theory pp. 280-282.
- Worked examples: Cambridge U3&4 Examples 20, 21, 22, 23 (pp. 295-298).
  You trys: Edrolo U3&4 4E Worked example 1a, 1b-c (pp. 280-281), Worked example 2a, 2b-c (pp. 282-284).
- CAS: planner/cas-skills.json 'trend-line' (task = Cambridge Example 22 data).
- Exit: Edrolo U3&4 4E Q12 = VCAA 2018 Further Exam 2 Q3 stem, Table 3, Q3bii, biii, d (original wording; time series plot not needed for these parts).
  Report: bii 36%, biii 74%, d 57% full marks (average 1.4).
- CFAT 1.5.2 (5D-5E) runs in the last 20 min (planner card).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l22')
yid=lambda u:u.split('v=')[1].split('&')[0]
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def stab(heads,rows,fs=18,tid='',lead=None):
    """columns across the top; rows = [(row label or None, values)]; cells data-i c{r}_{k}"""
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px;margin:8px auto">'
    t+='<tr>'+(f'<th>{lead}</th>' if lead is not None else '')+''.join(f'<th>{h}</th>' for h in heads)+'</tr>'
    for r,(lab,vals) in enumerate(rows):
        t+='<tr>'+(f'<th>{lab}</th>' if lab is not None else '')+''.join(f'<td data-i="c{r}_{k}">{v}</td>' for k,v in enumerate(vals))+'</tr>'
    return t+'</table>'
row=lambda r,n,k0=0:','.join(f'c{r}_{k}' for k in range(k0,n))
PS=lambda n:','.join([f'p{k}' for k in range(n)]+[f's{k}' for k in range(n-1)])
nn=lambda v:f'{v:,}'.replace(',',' ')

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:3px 9px!important;text-align:center;white-space:nowrap}.xs ol.parts li,.xs ol.parts li span{font-size:15px!important;line-height:1.3!important}'
   '.fl4{display:flex;gap:14px;justify-content:center;align-items:stretch;margin-top:10px}.fl4>div{flex:1;background:#fff;border:3px solid var(--learn);border-radius:14px;padding:14px;font-size:22px;text-align:center}.fl4 b{display:block;font-size:26px;margin-bottom:6px}</style>']
# ================= opening
S.append(title(22,'Fitting a trend line and forecasting',f'{CAM} · 5E Fitting a trend line and forecasting','L22'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('Trend lines and forecasting','',None),('Worked examples 20–21','→ You try',None),('Seasonal data: deseasonalise → fit → reseasonalise','',None),
  ('Worked examples 22–23','→ You try',None),('CAS: fitting a trend line','',None),('Exit task','· one VCAA question','var(--exit)'),('CFAT 1.5.2','· last 20 minutes','#00838F'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Trend line','a least squares line fitted to a time series, with time as the EV'),
  ('Forecasting','using the trend line to predict a future value'),
  ('Slope','the average change in the RV per time period'),
  ('Seasonal data','deseasonalise first; the forecast is a deseasonalised value'),
  ('Limitation','forecasts further into the future (extrapolation) are less reliable')],
  [('Trend line',F('RV = <i>a</i> + <i>b</i> × time'),'time coded 1, 2, 3 … or the year'),
   ('Deseasonalise',F('deseasonalised = ',FR(['actual'],['SI'])),'before fitting the line'),
   ('Reseasonalise',F('actual = deseasonalised × SI'),'after the forecast')],
  f'{CAM}, 5E pp. 295–298; Study Design: modelling trend by fitting a least squares line to a time series'))

# ================= Do Now 1: VCAA 2024 NHT E1 Q15 (5D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q15','Review of 5D (last lesson)',
  '<div style="font-size:26px;margin-top:30px">The sales revenue, in dollars, from the sale of chocolate eggs is seasonal.<br>To correct the sales revenue in May for seasonality, the actual sales revenue, to the nearest percent, is decreased by 17%.<br><br>The seasonal index for that month is closest to</div>',
  [('Correcting','correct for seasonality = multiply by 1 ÷ SI'),('Decrease 17%','1 ÷ SI = 1 − 0.17 = 0.83'),fx('SI','SI',F(FR(['1'],[V('1 ÷ SI','0.83')])),'1.205')],
  '1.20: <b>D</b>.','VCAA 2024 NHT General Mathematics Exam 1 Q15 (NHT report gives the answer only)',
  mc=['0.77','0.83','1.17','1.20','1.25'],key='D',stat=('nht',)))
# ================= Do Now 2: VCAA 2026 E1 Q10 (4B)
LT='<table class="t tight" style="font-size:16px;margin:6px auto"><tr><th>Day</th>'+''.join(f'<td>{k+1}</td>' for k in range(10))+'</tr><tr><th>Likes</th>'+''.join(f'<td>{v}</td>' for v in LIKES)+'</tr></table>'
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q10','Review of 4B (last week)',
  '<div style="font-size:20px">A social media influencer recorded the total number of likes she received on a recent post each day after it had been posted.<br>'
  'The scatterplot shown below is non-linear. The data used to construct the scatterplot is also shown. <span class="muted" style="font-size:16px">(scatterplot not shown: the table is enough)</span>'+LT+
  'A logarithmic (base 10) transformation was applied to the variable <em class="v">likes</em>.<br>With <em class="v">day</em> as the explanatory variable, the equation of the least squares line fitted to the transformed data is closest to</div>',
  [('Transform','new list: log10(likes)'),('CAS','Linear Reg: X = day, Y = log10(likes)'),('Read off','<i>a</i> = 1.403 · <i>b</i> = 0.1398')],
  'log<sub>10</sub>(<em>likes</em>) = 1.40 + 0.140 × <em>day</em>: <b>D</b>.','VCAA 2026 General Mathematics Exam 1 Q10 (2026 report not yet released; answer from CAS)',
  mc=['log<sub>10</sub>(likes) = 1.29 + 0.143 × day','log<sub>10</sub>(likes) = 1.33 + 0.147 × day','log<sub>10</sub>(likes) = 1.38 + 0.152 × day','log<sub>10</sub>(likes) = 1.40 + 0.140 × day'],key='D'))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 3: VCAA 2023 E2 Q4c (5D)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q4c','Review of 5D (last lesson)',
  '<div style="font-size:19px">The time series plot below shows the average monthly ice cream consumption recorded over three years, from January 2010 to December 2012. <span class="muted" style="font-size:16px">(plot not needed for part c)</span><br>'
  'c. Table 4 below shows the average monthly ice cream consumption for 2011.<br><b>Table 4</b>'
  +stab(MON[:6],[(None,ICE[:6])],17,'d3a')+stab(MON[6:],[(None,ICE[6:])],17,'d3b')+
  '<div style="text-align:center;font-size:15px" class="muted">Consumption (litres/person), 2011</div>'
  '<b>Show that</b>, when rounded to two decimal places, the seasonal index for July 2011 estimated from this data is 1.10. <span class="muted">(2 marks)</span></div>',
  [fx('Mean','monthly mean',F(FR([V('sum','2.004')],[V('months','12')])),'0.167','data-hi="#d3a|'+row(0,6)+'|hy;#d3b|'+row(0,6)+'|hy"'),
   fx('SI','seasonal index July',F(FR([V('July','0.183')],[V('mean','0.167')])),'1.0958…','data-hi="#d3b|c0_0|hb"')],
  'Seasonal index = 0.183 ÷ 0.167 = 1.0958… = <b>1.10</b> (show BOTH calculations).','VCAA 2023 General Mathematics Exam 2 Q4 stem and Q4c (examiner report: 21% full marks, average 0.7/2)',
  stat=('mark',21),cmd=('Show that',2,'mean first, then July ÷ mean')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2026 E2 Q1b (1B)
HT='<table class="t tight" id="d4" style="font-size:15px;margin:6px auto"><tr><th>Country</th><th>Happiness index</th><th>Country</th><th>Happiness index</th></tr>'+''.join(
  f'<tr><td data-i="n{k}">{HAPPY[k][0]}</td><td data-i="v{k}">{HAPPY[k][1]}</td><td data-i="n{k+6}">{HAPPY[k+6][0]}</td><td data-i="v{k+6}">{HAPPY[k+6][1]}</td></tr>' for k in range(6))+'</table>'
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q1b','Review of 1B (last term)',
  '<div style="font-size:19px">The happiness index for a country is a score ranging from 0 to 10. It represents the level of happiness for people in that country. A higher score represents happier people.<br>'
  'The happiness index scores for 12 countries in 2022 are given in the table below.'+HT+
  'b. <b>Calculate</b> the percentage of countries listed in the table on page 2 that have a happiness index greater than 7.55 <span class="muted">(1 mark)</span></div>',
  [('Count','greater than 7.55: Finland 7.82, Denmark 7.64, Iceland 7.56 → 3 countries','data-hi="#d4|n0,v0,n1,v1,n2,v2|hy"'),
   fx('Percentage','percentage',F(FR([V('count','3')],[V('total','12')]),' × 100%'),'25%')],
  '<b>25%</b> of the countries have a happiness index greater than 7.55.','VCAA 2026 General Mathematics Exam 2 Q1 stem and Q1b (2026 report not yet released)',
  cmd=('Calculate',1,'count ÷ total × 100%')))

# ================= APK 1: Cambridge U1&2 5F #10
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 5F #10','Equation of a line from two points',
  '<div style="font-size:30px;margin-top:40px">Find the equation of the line that goes through the points (3, −1) and (−2, 7).</div>',
  [fx('Slope','<i>b</i>',F(FR([V('rise','7 − (−1)')],[V('run','−2 − 3')])),'−1.6'),
   ('Intercept','−1 = <i>a</i> − 1.6 × 3 → <i>a</i> = −1 + 4.8 = 3.8')],
  '<i>y</i> = 3.8 − 1.6<i>x</i>',f'{CAM12} · Ch 5 skills checklist 5F #10 · solution worked for 12MAG',cmd=('Find',None,'slope first, then substitute a point')))
# ================= APK 2: VCAA 2014 E1 G&R Q4
S.append(qslide('apk','APK · VCAA 2014 Exam 1 Q4','Points on a line',
  '<div style="font-size:28px;margin-top:40px">A line passes through the points (−1, 1) and (3, 5). Another point that lies on this line is</div>',
  [fx('Slope','slope',F(FR([V('rise','5 − 1')],[V('run','3 − (−1)')])),'1'),('Equation','1 = <i>a</i> + 1 × (−1) → <i>a</i> = 2: <i>y</i> = 2 + <i>x</i>'),('Test','(1, 3): 2 + 1 = 3 ✓')],
  '(1, 3): <b>B</b>.',f'VCAA 2014 Further Mathematics Exam 1 Graphs and relations Q4 · Edrolo General Mathematics Units 1&amp;2 4D Q13 (no 2014 examiner report on file)',
  mc=['(0, 1)','(1, 3)','(2, 6)','(3, 4)','(4, 7)'],key='B'))
# ================= APK 3: VCAA 2016 E1 G&R Q2
S.append(qslide('apk','APK · VCAA 2016 Exam 1 Q2','Writing a linear equation',
  '<div style="font-size:24px;margin-top:30px">A phone company charges a fixed, monthly line rental fee of $28 and $0.25 per call.<br>Let <i>n</i> be the number of calls that are made in a month.<br>Let <i>C</i> be the monthly phone bill, in dollars.<br>The equation for the relationship between the monthly phone bill, in dollars, and the number of calls is</div>',
  [('Intercept','fixed fee = $28 (paid even when <i>n</i> = 0)'),('Slope','$0.25 for each call'),('Equation','<i>C</i> = 28 + 0.25<i>n</i>')],
  '<i>C</i> = 28 + 0.25<i>n</i>: <b>A</b>.',f'VCAA 2016 Further Mathematics Exam 1 Graphs and relations Q2 (examiner report) · Edrolo General Mathematics Units 1&amp;2 4E Q16',
  mc=['<i>C</i> = 28 + 0.25<i>n</i>','<i>C</i> = 28<i>n</i> + 0.25','<i>C</i> = <i>n</i> + 28.25','<i>C</i> = 28(<i>n</i> + 0.25)','<i>C</i> = 0.25(<i>n</i> + 28)'],key='A',dist=[94,2,1,2,1]))

# ================= Learn 1: trend lines and forecasting
fa,fb=-1633580,851.017
P20=ts(FEM,xs=FEM_X,yr=(75000,92000),yt=2000,xl='year',yl='number',W=640,H=290,fs=12,xr=(2009,2027),xtick=2,sid='lt',r=4,
       tls=(((2009.5,fa+fb*2009.5),(2018,fa+fb*2018),'tl'),((2018,fa+fb*2018),(2026.5,fa+fb*2026.5),'tx')))
S.append(learn('Learn · 5E','Fitting a trend line and forecasting',
  '<h4>A least squares line with time as the EV</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>check the plot: is the trend roughly <b>linear</b>?</li><li>fit the least squares line (CAS): time = EV</li>'
  '<li><b>slope</b> = average change per time period</li><li><b>forecast</b>: substitute a future time</li></ul>',
  Wd(640,P20)+'<span class="frag" data-show="#lt|tl"></span><span class="frag" data-show="#lt|tx"></span>'
  '<div class="frag" style="font-size:22px;text-align:center">Forecasting = extrapolating: the further into the future, the less reliable (the trend may not continue).</div>',
  'Forecasts beyond the data assume the trend continues: treat them with caution.',f'{CAM}, 5E pp. 295–296 (own words; plot drawn from Example 20 data) · {EDR}, 4E p. 280',
  cards=(kcard('Trend line',F('RV = <i>a</i> + <i>b</i> × time')),)))

# ================= Ex 20 / YT WE1a
S.append(qslide('we','Worked example 20 · 5E','Fitting a trend line',
  '<div style="font-size:21px">The table below shows the number of female students in Victoria enrolled in at least one subject in the Mathematics learning area at year 12 over the period 2010–18. Fit a trend line to the data, and interpret the slope.'
  +stab(FEM_X[:5],[('Number',[nn(v) for v in FEM[:5]])],19,'e20a',lead='Year')+stab(FEM_X[5:],[('Number',[nn(v) for v in FEM[5:]])],19,'e20b',lead='Year')
  +Wd(470,ts(FEM,xs=FEM_X,yr=(75000,85000),yt=2000,xl='year',yl='number',W=470,H=210,fs=11,xr=(2009,2019),xtick=1,sid='e20',r=3.5,hidpts=True,hidline=True,
             tls=(((2009.5,fa+fb*2009.5),(2018.5,fa+fb*2018.5),'tl'),)))+'</div>',
  [('Plot','time series plot: trend is approximately linear','data-show="#e20|'+PS(9)+'"'),
   ('CAS','Linear Reg: X = year, Y = number (6 significant figures)','data-show="#e20|tl"'),
   ('Equation','number of female students = −1 633 580 + 851.017 × year'),
   ('Slope','851 (nearest whole number)')],
  'Over the period 2010–2018 on average the number of female students in Victoria enrolled in at least one subject in the Mathematics learning area at year 12 <b>increased by 851 per year</b>.',f'{CAM} · Example 20 (pp. 295–296)',video='Cambridge GO · Example 20 (5E Resources)',
  cmd=('Fit',None,'time = EV; slope = change per year')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 4E WE1a','Fitting a trend line',
  '<div style="font-size:22px">A public library introduced a record collection to their catalogue. The number of visitors to the library each day following its introduction was recorded.<br>'
  'The day that the record collection was introduced is noted as day 0 and the first day after the introduction is day 1.'
  +stab(list(range(1,8)),[('number of visitors',LIB)],22,'y1',lead='day')+
  'a. <b>Determine</b> the equation of the least squares regression line for the data. Give values correct to two decimal places where necessary.</div>',
  [('CAS','Linear Reg: X = day, Y = visitors','data-hi="#y1|'+row(0,7)+'|hy"'),('Read off','<i>a</i> = 68.285… · <i>b</i> = 21.178…'),('Variables','EV = day · RV = number of visitors')],
  '<em>number of visitors</em> = <b>68.29 + 21.18 × <em>day</em></b>',f'{EDR} · 4E Worked example 1a (pp. 280–281)',cmd=('Determine',None,'CAS, then write in the variables')))
# ================= Ex 21 / YT WE1b-c
S.append(qslide('we','Worked example 21 · 5E','Forecasting',
  '<div style="font-size:24px;margin-top:20px">How many female students in Victoria do we predict being enrolled in at least one subject in the Mathematics learning area at year 12 in 2026 if the same increasing trend continues? Give your answer rounded to the nearest whole number.'
  '<div class="muted" style="font-size:19px;margin-top:14px">From Example 20: number of female students = −1 633 580 + 851.017 × year</div></div>',
  [fx('Substitute','number',F('−1 633 580 + 851.017 × ',V('year','2026')),'90 580.4'),
   ('Caution','2026 is well beyond 2010–2018: extrapolation, treat with caution')],
  'We predict <b>90 580</b> female students in 2026 (if the trend continues).',f'{CAM} · Example 21 (p. 296)',video='Cambridge GO · Example 21 (5E Resources)',
  cmd=('predict',None,'substitute the future time')))
S.append(qslide('yt','You try · Edrolo 4E WE1b, c','Forecasting',
  '<div style="font-size:21px">'+stab(list(range(1,8)),[('number of visitors',LIB)],19,'',lead='day')+
  '<div class="muted" style="font-size:18px">From part a: number of visitors = 68.29 + 21.18 × day</div></div>'
  +plist([('b','Use the rounded regression equation to <b>estimate</b> the number of visitors on the 8th day after the introduction. Round to the nearest whole number.'),
          ('c','Use the regression equation to <b>estimate</b> the number of visitors to the library on the day that the record collection was introduced. Round to the nearest whole number.')]),
  [fx('b','visitors',F('68.29 + 21.18 × ',V('day','8')),'237.73'),('c','day 0 → visitors = the intercept = 68.29')],
  '',f'{EDR} · 4E Worked example 1b, c (p. 281)',cmd=('estimate',None,'substitute the day'),
  parts=[('b','<b>238 visitors</b>'),('c','<b>68 visitors</b>')]))

# ================= Learn 2: seasonal data
S.append(learn('Learn · 5E','Forecasting with seasonal data',
  '<h4>Take the seasons out, fit, then put them back</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>a trend line through seasonal data is distorted by the ups and downs</li><li>fit the line to the <b>deseasonalised</b> data</li>'
  '<li>the forecast is a <b>deseasonalised</b> value</li><li>reseasonalise: × the SI of that season</li></ul>',
  '<div class="fl4" style="width:1100px;max-width:100%;margin:10px auto 0"><div class="frag"><b>1 · Deseasonalise</b>actual ÷ SI</div><div class="frag"><b>2 · Fit</b>least squares line, time = EV</div>'
  '<div class="frag"><b>3 · Forecast</b>substitute the time number</div><div class="frag"><b>4 · Reseasonalise</b>× SI of that season</div></div>'
  '<div class="frag" style="font-size:22px;text-align:center;margin-top:18px">Number the time periods 1, 2, 3 … : summer year 1 = quarter 1, so winter year 4 = quarter 15.</div>',
  'Forgetting to reseasonalise is the most common error: the line gives a deseasonalised value.',f'{CAM}, 5E pp. 297–298 (own words) · {EDR}, 4E p. 282',
  cards=(kcard('Deseasonalise',F(FR(['actual'],['SI']))),kcard('Reseasonalise',F('actual = deseasonalised × SI')))))

# ================= Ex 22 / YT WE2a
ma,mb=838.0,32.07
S.append(qslide('we','Worked example 22 · 5E','Fitting a trend line (seasonality)',
  '<div style="font-size:21px">The deseasonalised quarterly sales data from Mikki’s shop are shown below.'
  +stab(list(range(1,7)),[('Sales',MDS[:6])],16,'e22',lead='Quarter')+stab(list(range(7,13)),[('Sales',MDS[6:])],16,'e22b',lead='Quarter')+'Fit a trend line and interpret the slope.'
  +Wd(470,ts(MDS,yr=(800,1300),yt=100,xl='quarter',yl='sales',W=470,H=210,fs=11,xr=(0,13),xtick=1,sid='e22p',r=3.5,hidpts=True,hidline=True,
             tls=(((0.5,ma+mb*0.5),(12.5,ma+mb*12.5),'tl'),)))+'</div>',
  [('Plot','plot the time series','data-show="#e22p|'+PS(12)+'"'),('CAS','Linear Reg: X = quarter (EV), Y = sales (RV)','data-show="#e22p|tl"'),
   ('Equation','sales = 838.0 + 32.07 × quarter (4 significant figures)')],
  'Over the 3-year period, on average sales at Mikki’s shop <b>increased by 32.07 sales per quarter</b>.',f'{CAM} · Example 22 (p. 297)',video='Cambridge GO · Example 22 (5E Resources)',
  cmd=('Fit',None,'quarter = EV')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 4E WE2a','Fitting a trend line (seasonality)',
  '<div style="font-size:19px">The sales of NRL jerseys at a merchandise store are seasonal. The sales for the first six months of 2022 are shown in the following table.'
  +stab(MON[:6],[(None,JER)],17,'y2',lead='month').replace('<tr><td','<tr><th>sales</th><td',1)
  +'The long-term seasonal index for each month is also provided.'
  +stab(MON[:6],[('seasonal index',JSI[:6])],15,'y2s',lead='month')+stab(MON[6:],[('seasonal index',JSI[6:])],15,'',lead='month')+
  'a. <b>Determine</b> the equation of the least squares regression line to predict the deseasonalised sales for a month. Give values correct to one decimal place.<br><span style="font-size:16px">Note: When deseasonalising sales, round values correct to one decimal place.</span></div>',
  [('Deseasonalise','sales ÷ SI: 479 ÷ 0.55 = 870.9 · 814.3 · 805.0 · 738.8 · 720.7 · 673.9','data-hi="#y2|'+row(0,6)+'|hy;#y2s|'+row(0,6)+'|hb"'),
   ('CAS','Linear Reg: X = month (Jan = 1 … Jun = 6), Y = deseasonalised sales'),('Read off','<i>a</i> = 903.8 · <i>b</i> = −38.057…')],
  '<em>deseasonalised sales</em> = <b>903.8 − 38.1 × <em>month</em></b>',f'{EDR} · 4E Worked example 2a (pp. 282–284)',cmd=('Determine',None,'deseasonalise first')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)
# ================= Ex 23 / YT WE2b-c
S.append(qslide('we','Worked example 23 · 5E','Forecasting (seasonality)',
  '<div style="font-size:24px;margin-top:20px">What sales do we predict for Mikki’s shop in the winter of year 4? (Because many items have to be ordered well in advance, retailers often need to make such decisions.)'
  '<div class="muted" style="font-size:19px;margin-top:14px">From Example 22: deseasonalised sales = 838.0 + 32.07 × quarter</div>'
  +stab(['Summer','Autumn','Winter','Spring'],[('SI',['1.03','1.15','1.30','0.52'])],20,'e23',lead='')+'</div>',
  [('Quarter','summer year 1 = quarter 1 → winter year 4 = quarter 15'),
   fx('Forecast','deseasonalised sales',F('838.0 + 32.07 × ',V('quarter','15')),'1319.05'),
   fx('Reseasonalise','actual sales',F(V('deseasonalised','1319.05'),' × ',V('SI winter','1.30')),'1714.765','data-hi="#e23|c0_2|hy"')],
  'Predicted sales for winter of year 4 = <b>1715</b> (nearest whole number).',f'{CAM} · Example 23 (pp. 297–298); seasonal indices from Example 18',video='Cambridge GO · Example 23 (5E Resources)',
  cmd=('predict',None,'forecast, then × SI')))
S.append(qslide('yt','You try · Edrolo 4E WE2b, c','Forecasting (seasonality)',
  '<div style="font-size:19px">'+stab(MON[:6],[('seasonal index',JSI[:6])],15,'',lead='month')+stab(MON[6:],[('seasonal index',JSI[6:])],15,'y3',lead='month')+
  '<div class="muted" style="font-size:17px">From part a: deseasonalised sales = 903.8 − 38.1 × month (January 2022 = month 1)</div></div>'
  +plist([('b','Use the rounded regression equation to <b>predict</b> the sales, correct to the nearest whole number, for October 2022.'),
          ('c','<b>Interpret</b> the slope of the rounded regression line in terms of the change in deseasonalised sales each month.')]),
  [fx('b · forecast','deseasonalised sales',F('903.8 − 38.1 × ',V('month','10')),'522.8'),
   fx('b · reseasonalise','actual',F(V('deseasonalised','522.8'),' × ',V('SI Oct','0.58')),'303.224','data-hi="#y3|c0_3|hy"'),
   ('c','slope = −38.1: the average change per month')],
  '',f'{EDR} · 4E Worked example 2b, c (pp. 283–284)',cmd=('predict',None,'forecast, then × SI'),
  parts=[('b','<b>303 sales</b>'),('c','On average, deseasonalised sales <b>decrease by 38.1 each month</b>.')]))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['trend-line']
S.append(cas('CAS · 5E','Fitting a trend line',
  '<p style="font-size:20px">Mikki’s deseasonalised quarterly sales (Example 22):</p>'
  +stab(list(range(1,7)),[('Sales',MDS[:6])],14,'',lead='Quarter')+stab(list(range(7,13)),[('Sales',MDS[6:])],14,'',lead='Quarter')+
  '<p style="font-size:20px;margin-top:8px">Fit a least squares trend line with quarter as the EV, then forecast the deseasonalised sales for quarter 15.</p>',
  C['ti'],C['classpad'],'<i>a</i> = 837.98… · <i>b</i> = 32.066… → sales = 838.0 + 32.07 × quarter · quarter 15: <b>1319</b> (deseasonalised)',
  f'{CAM} · Example 22 data (p. 297) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exit: VCAA 2018 E2 Q3bii, biii, d
S.append(qslide('ex','Exit task · VCAA 2018 Exam 2 Q3bii, biii, d','Show what you know',
  '<div style="font-size:15px">Table 3 shows the yearly average traffic congestion levels in two cities, Melbourne and Sydney, during the period 2008 to 2016. <span class="muted">(time series plot not needed for these parts)</span><br><b>Table 3</b> · Congestion level (%)'
  +stab(YRS,[('Melbourne',MEL),('Sydney',SYD)],14,'x1',lead='Year')+'</div>'
  +plist([('b','A least squares line is used to model the trend in the time series plot for Sydney. The equation is <i>congestion level</i> = –2280 + 1.15 × <i>year</i><br>'
             'ii. Use the equation of the least squares line to <b>determine</b> the average rate of increase in percentage congestion level for the period 2008 to 2016 in Sydney. <span class="muted">(1 mark)</span><br>'
             'iii. Use the least squares line to <b>predict</b> when the percentage congestion level in Sydney will be 43%. <span class="muted">(1 mark)</span>'),
          ('d','Use the data in Table 4 to <b>determine</b> the equation of the least squares line that can be used to model the trend in the data for Melbourne. The variable <i>year</i> is the explanatory variable. Round both values to four significant figures. <span class="muted">(2 marks)</span>'
             '<br><span class="muted">(Table 4 repeats the Melbourne row of Table 3.)</span>')]),
  [('bii','rate of increase = slope = 1.15'),
   fx('biii','year',F(FR([V('43 + 2280','2323')],[V('slope','1.15')])),'2020'),
   ('d','CAS Linear Reg: X = year, Y = Melbourne: <i>a</i> = −1514.755… · <i>b</i> = 0.76666…','data-hi="#x1|'+row(0,9)+'|hy"')],
  '',f'VCAA 2018 Further Mathematics Exam 2 Q3 (examiner report: bii 36%, biii 74%, d 57% full marks) · {EDR} 4E Q12',
  stat=('mark',36),cmd=('determine',4,'slope = rate; solve; CAS'),
  parts=[('bii','<b>1.15</b>% per year'),('biii','<b>2020</b>'),('d','<em>congestion level</em> = <b>−1515 + 0.7667 × <em>year</em></b>')]))
S[-1]=S[-1].replace('<section class="slide T ex ','<section class="slide T ex sm xs ',1)

# ================= CFAT 1.5.2, closing
S.append(cfat('CFAT 1.5.2','Seasonal indices and forecasting','5D–5E',17,'CFAT 1.5.2 (5D–5E) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5E',) and v.get('url')]))
n=assemble(S,'12MAG · L22 · Trend lines and forecasting',os.path.join(ROOT,'lessons','5E slides.html'))
print(n-1,'slides')
