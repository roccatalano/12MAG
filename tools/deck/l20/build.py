"""Lesson l20 (5D, seasonal indices: interpreting and using) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5D seasonal indices slides.html
Run: python3 tools/deck/l20/build.py      Screenshots: python3 tools/deck/l20/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- CFAT 1.5.1 (5A-5C) at the start (planner card).
- Do Now: VCAA 2023 Exam 1 Q13-14 stem + Q13 (C, 68%; A 4 B 12 C 68 D 13 E 3) ·
          VCAA 2026 NHT Exam 1 Q2-3 stem + Q3 (D; NHT report: answers only) ·
          VCAA 2024 Exam 2 Q4 stem + Q4a (55% scored the mark) ·
          VCAA 2023 Exam 2 Q3 stem + Q3d (43% scored the mark; scatterplot not needed for part d, not shown).
- APK: Cambridge U1&2 Ch 1 skills checklist 1B #6 (replaces 1A #2, burnt in l03) and 1D #11 (answers worked for 12MAG) ·
       VCAA 2018 Further Exam 2 Q2 stem + Q2a (41% full marks; medians 52%, 56%) = Edrolo U1&2 1D Q19 (original wording).
- Learn: Cambridge U3&4 5D pp. 283-286 (own words; unemployment table p. 284). Study Design dot point.
- Worked examples: Cambridge U3&4 Examples 14, 15, 16 (pp. 284-286).
  You trys: Edrolo U3&4 4D Worked example 1b (p. 269; part a's table and answer 0.53 given as context), Worked example 5 (p. 271), Worked example 4 (p. 271).
- No CAS on the card.
- Exits: Edrolo U3&4 4D Q19 = VCAA 2017 Further Exam 1 Q16 (A, 32%; A 32 B 11 C 22 D 27 E 6) ·
         4D Q17 = VCAA 2020 Further Exam 1 Q17-18 stem (Table 4) + Q17 (B, 88%; A 2 B 88 C 4 D 3 E 3). Original VCAA wording.
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l20')
yid=lambda u:u.split('v=')[1].split('&')[0]
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def stab(heads,rows,fs=18,tid='',lead=None):
    """seasons across the top; rows = [(row label or None, values)]; cells data-i c{r}_{k}"""
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px;margin:8px auto">'
    t+='<tr>'+(f'<th>{lead}</th>' if lead is not None else '')+''.join(f'<th>{h}</th>' for h in heads)+'</tr>'
    for r,(lab,vals) in enumerate(rows):
        t+='<tr>'+(f'<th>{lab}</th>' if lab is not None else '')+''.join(f'<td data-i="c{r}_{k}">{v}</td>' for k,v in enumerate(vals))+'</tr>'
    return t+'</table>'
pk=lambda ks:','.join(f'p{k}' for k in ks)
SEAS=['Summer','Autumn','Winter','Spring']

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:3px 10px!important;text-align:center}</style>']
# ================= opening
S.append(title(20,'Seasonal indices',f'{CAM} · 5D Seasonal indices (interpreting and using)','L20',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 1.5.1','· 5A–5C · 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills + one VCAA question','var(--apk)'),
  ('What a seasonal index means','',None),('Deseasonalise · reseasonalise · correct','',None),('Worked examples 14–16','→ You try',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Seasonal index (SI)','compares a season with the average season: 1 (100%) = an average season'),
  ('SI above 1','that season is typically higher than average (1.2 → 20% higher)'),
  ('SI below 1','that season is typically lower than average (0.9 → 10% lower)'),
  ('Sum of the SIs','= the number of seasons (4 quarters → 4, 12 months → 12); their mean is 1'),
  ('Deseasonalise','remove the seasonal effect so the trend is clearer'),
  ('Reseasonalise','put the seasonal effect back in: get the actual value')],
  [('Deseasonalise',F('deseasonalised = ',FR(['actual'],['SI'])),'divide by the SI'),
   ('Reseasonalise',F('actual = deseasonalised × SI'),'multiply by the SI'),
   ('Correct for seasonality',F('multiply by ',FR(['1'],['SI'])),'1.25 → increase 25% · 0.8 → decrease 20%')],
  f'{CAM}, 5D pp. 283–286; Study Design: seasonal adjustment including the use and interpretation of seasonal indices'))
S.append(cfat('CFAT 1.5.1','Time series plots and smoothing','5A–5C',14,'CFAT 1.5.1 (5A–5C) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now 1: VCAA 2023 E1 Q13 (5C)
D1=tsm(W800,[None]*6+[116.8]+[None]*16,xs=W800_X,yr=(114,119),yt=1,xl='year',yl='winning time (seconds)',W=560,H=250,fs=12,xr=(2000,2022),xtick=2,sid='d1',r=3.5)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q13','Review of 5C (last lesson)',
  ('<div style="font-size:18px">The following graph shows a selection of winning times, in seconds, for the women’s 800 m track event from various athletic events worldwide. The graph shows one winning time for each calendar year from 2000 to 2022.</div>',
   Wd(560,D1),'<div style="font-size:18px">The time series is smoothed using seven-median smoothing.<br>The smoothed value for the winning time in 2006, in seconds, is closest to</div>'),
  [('Seven points','2006 and three each side: 2003 to 2009','data-hi="#d1|'+pk(range(3,10))+'|hy"'),
   ('Order','116.0, 116.0, 116.4, <b>116.8</b>, 117.2, 117.6, 117.9: 4th value'),
   ('Mark','cross at (2006, 116.8)','data-show="#d1|g6,m6"')],
  '116.8: <b>C</b>.','VCAA 2023 General Mathematics Exam 1 Q13–14 stem and Q13 (examiner report; plot redrawn, values read off)',
  mc=['116.0','116.4','116.8','117.2','117.6'],key='C',dist=[4,12,68,13,3],dis=('D','13%: 117.2 is the 2006 value itself, not the median of the seven values around it.')))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2026 NHT E1 Q3 (1F)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 NHT Exam 1 Q3','Review of 1F (last term)',
  ('<div style="font-size:19px">The <em class="v">shoe size</em> of a group of 46 adults was recorded.<br>The results are shown in the dot plot below.</div>',
   Wd(520,dot('d2d',{"min":5,"max":13,"vals":SHOE,"xl":"shoe size","W":520,"h":230,"r":6,"fs":14})),
   '<div style="font-size:19px">The person with a <em class="v">shoe size</em> of 13 is removed from the data set.<br>For the variable <em class="v">shoe size</em>, this would cause</div>'),
  [('Mean','13 is the largest value: removing it makes the total smaller → the mean <b>decreases</b>'),
   ('Standard deviation','13 is the value furthest from the mean: removing it makes the data less spread → the standard deviation <b>decreases</b>')],
  'Both decrease: <b>D</b>.','VCAA 2026 NHT General Mathematics Exam 1 Q2–3 stem and Q3 (NHT report gives the answer only; dot plot redrawn)',
  mc=['the mean to increase and the standard deviation to increase.','the mean to increase and the standard deviation to decrease.',
      'the mean to decrease and the standard deviation to increase.','the mean to decrease and the standard deviation to decrease.'],key='D',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 3: VCAA 2024 E2 Q4a (5C)
G5=mmed(WG,5)
D3=tsm(WG,G5,xs=OLY,yr=(1.60,2.05),yt=0.05,xl='year',yl='Wgold (m)',W=540,H=260,fs=12,xr=(1952,1988),xtick=4,sid='d3',r=4)
D3=D3.replace('<path data-i="ml" class="hid0"','<path data-i="ml" class="hid0" stroke-dasharray="7 5"')
for k in (2,3):   # the two crosses printed in the question: visible, black
    i=D3.index(f'<g data-i="m{k}" class="hid0">'); j=D3.index('</g>',i)
    D3=D3[:i]+D3[i:j].replace(' class="hid0"','').replace('#d2475b','#222')+D3[j:]
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q4a','Review of 5C (last lesson)',
  ('<div style="font-size:18px">The time series plot below shows the gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, in metres, for each Olympic year, <em class="v">year</em>, from 1952 to 1988.</div>',
   Wd(540,D3),
   '<div style="font-size:18px">A five-median smoothing process will be used to smooth the time series plot above.<br>The first two points have been placed on the graph with crosses (X) and joined by a dashed line (- - -).<br>'
   'a. <b>Complete</b> the five-median smoothing by marking smoothed values with crosses (X) joined by a dashed line (- - -) on the time series plot above. <span class="muted">(1 mark)</span></div>'),
  [('1968','1960 to 1976: 1.85, 1.90, 1.82, 1.92, 1.93 → middle value 1.90','data-hi="#d3|'+pk(range(2,7))+'|hy" data-show="#d3|g4,m4"'),
   ('1972','1964 to 1980: 1.90, 1.82, 1.92, 1.93, 1.97 → 1.92','data-hi="#d3|'+pk(range(3,8))+'|hy" data-show="#d3|g5,m5"'),
   ('1976','1968 to 1984: 1.82, 1.92, 1.93, 1.97, 2.02 → 1.93','data-hi="#d3|'+pk(range(4,9))+'|hy" data-show="#d3|g6,m6"'),
   ('1980','1972 to 1988: 1.92, 1.93, 1.97, 2.02, 2.01 → 1.97 (last one: 1984, 1988 have no value)','data-hi="#d3|'+pk(range(5,10))+'|hy" data-show="#d3|g7,m7"'),
   ('Join','join all six crosses with a dashed line','data-hi="#d3||hy" data-show="#d3|ml"')],
  'Crosses at (1968, 1.90), (1972, 1.92), (1976, 1.93), (1980, 1.97), joined by a dashed line from 1960.',
  'VCAA 2024 General Mathematics Exam 2 Q4 stem and Q4a (examiner report; plot redrawn, values read off)',
  stat=('mark',55),cmd=('Complete',1,'five at a time from the original points')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2023 E2 Q3d (3B)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q3d','Review of 3B (last term)',
  '<div style="font-size:22px">The scatterplot below plots the average monthly ice cream consumption, in litres/person, against average monthly temperature, in °C. The data for the graph was recorded in the Northern Hemisphere.<br>'
  '<span class="muted" style="font-size:17px">(scatterplot not needed for this part)</span><br><br>When a least squares line is fitted to the scatterplot, the equation is found to be:'
  '<div style="text-align:center;margin:12px 0"><em>consumption</em> = 0.1404 + 0.0024 × <em>temperature</em></div>The coefficient of determination is 0.7212<br><br>'
  'd. Referring to the equation of the least squares line, <b>interpret</b> the value of the intercept in terms of the variables <em class="v">consumption</em> and <em class="v">temperature</em>. <span class="muted">(1 mark)</span></div>',
  [('Intercept','0.1404: the predicted <em>consumption</em> when <em>temperature</em> = 0'),
   ('Template','On average, when <em>EV</em> = 0, the <em>RV</em> is predicted to be <i>a</i>.'),
   ('Only the intercept','no slope, no horizontal intercept (examiner report)')],
  'On average, when the <em>temperature</em> is 0 °C, ice cream <em>consumption</em> per person is predicted to be <b>0.1404 litres</b>.',
  'VCAA 2023 General Mathematics Exam 2 Q3 stem and Q3d (examiner report; scatterplot not shown: not needed for part d)',
  stat=('mark',43),cmd=('interpret',1,'intercept only, in context')))

# ================= APK 1: Cambridge U1&2 1B #6 (replaces 1A #2, burnt in l03)
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1B #6','Increase or decrease by a percentage',
  '<div style="font-size:30px;margin-top:40px">Decrease $150 by 20%.</div>',
  [('Multiplier','decrease by 20% → keep 100% − 20% = 80% = 0.8'),fx('Result','new value',F(V('value','150'),' × ',V('multiplier','0.8')),'120')],
  '$150 decreased by 20% is <b>$120</b>.',f'{CAM12} · Ch 1 skills checklist 1B #6 · solution worked for 12MAG · replaces 1A #2 (already used in l03)',cmd=('Decrease',None,'multiply by 0.8')))
# ================= APK 2: Cambridge U1&2 1D #11
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1D #11','Express quantities as a ratio',
  '<div style="font-size:30px;margin-top:40px">In a class there are ten students who are 16 years old and twenty students who are 17 years old. Express the ratio of the number of 16-year-olds to 17-year-olds.</div>',
  [('In order','16-year-olds : 17-year-olds = 10 : 20'),('Simplify','divide both by 10 → 1 : 2')],
  'The ratio of 16-year-olds to 17-year-olds is <b>1 : 2</b>.',f'{CAM12} · Ch 1 skills checklist 1D #11 · solution worked for 12MAG',cmd=('Express',None,'in the order asked, then simplify')))
# ================= APK 3: VCAA 2018 E2 Q2a
A3=scat(CONG,(35,70),(35,75),5,5,'morning congestion level (%)','evening congestion level (%)',W=420,H=320,r=4.5,fs=12,sid='a3s')
S.append(qslide('apk','APK · VCAA 2018 Exam 2 Q2a','Medians from a scatterplot',
  ('<div style="font-size:17px">The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>'
   'This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.</div>',
   Wd(380,A3),
   '<div style="font-size:17px">a. <b>Determine</b> the median percentage congestion level for the morning peak period and the evening peak period. <span class="muted">(2 marks)</span></div>'),
  [('19 values','median = the 10th value, counted from the left (morning) or from the bottom (evening)'),
   ('Morning','count 10 points from the left → 52%','data-hi="#a3s|p9|hy"'),
   ('Evening','count 10 points from the bottom → 56% (a different point!)','data-hi="#a3s|p11|hb"')],
  'Median morning congestion level = <b>52%</b> · median evening congestion level = <b>56%</b>',
  'VCAA 2018 Further Mathematics Exam 2 Q2 stem and Q2a (examiner report: don’t read the evening value off the morning median’s point; scatterplot redrawn) · Edrolo General Mathematics Units 1&amp;2 1D Q19',
  stat=('mark',41),cmd=('Determine',2,'10th value each way')))

# ================= Learn 1: what a seasonal index means
UT='<table class="t tight" style="font-size:22px;margin:10px auto"><tr>'+''.join(f'<th>{m}</th>' for m in UMON)+'<th>Total</th></tr><tr>'+''.join(f'<td data-i="c0_{k}">{v:g}</td>' for k,v in enumerate(UNEMP))+'<td data-i="c0_12"><b>12.0</b></td></tr></table>'
S.append(learn('Learn · 5D','What a seasonal index means',
  '<h4>Compare a season with the average season</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>the average season has SI = <b>1</b> (100%)</li>'
  '<li>SI × 100% → how big the season is <b>compared with average</b></li><li>SI − 1 → how much <b>higher</b> (+) or <b>lower</b> (−)</li><li>the SIs add up to the <b>number of seasons</b></li></ul>',
  '<div id="lu" style="width:900px;max-width:100%;margin:0 auto">'+UT+'<div style="font-size:24px;line-height:1.7;margin-top:14px">'
  '<div class="frag" data-hi="#lu|c0_1|hy">Feb: SI = 1.2 = 120% → unemployment is typically <b>20% higher</b> than the monthly average.</div>'
  '<div class="frag" data-hi="#lu|c0_7|hb">Aug: SI = 0.90 = 90% → typically <b>10% lower</b> than the monthly average.</div>'
  '<div class="frag" data-hi="#lu|c0_12|hg">Total = 12.0: twelve months → the SIs add to 12 (mean 1).</div></div></div>',
  'Write the % and the word “average season” (or “monthly average”) in every interpretation.',f'{CAM}, 5D pp. 283–284 (own words; table p. 284)',
  cards=(kcard('Seasonal index','compares a season with the average season'),kcard('Sum of the SIs','= number of seasons'))))
# ================= Learn 2: deseasonalise / reseasonalise / correct
S.append(learn('Learn · 5D','Seasonally adjusting data',
  '<h4>Divide to remove · multiply to put back</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li><b>deseasonalise</b>: actual ÷ SI (removes the seasonal effect)</li>'
  '<li><b>reseasonalise</b>: deseasonalised × SI (gives the actual value)</li><li><b>correct for seasonality</b>: multiply by 1 ÷ SI, then write it as a % change</li></ul>',
  '<div style="font-size:26px;line-height:1.8;width:1000px;max-width:100%;margin:0 auto">'
  '<div class="frag">SI = 1.25: a busy season → deseasonalised = actual ÷ 1.25 → smaller (the extra is removed)</div>'
  '<div class="frag">SI = 0.8: a quiet season → deseasonalised = actual ÷ 0.8 → bigger</div>'
  '<div class="frag">1 ÷ 0.8 = 1.25 = 125% → <b>increase by 25%</b> · 1 ÷ 1.25 = 0.8 = 80% → <b>decrease by 20%</b></div></div>',
  'Correcting for seasonality: the % change comes from 1 ÷ SI, not from the SI itself (0.8 is NOT “increase by 20%”).',f'{CAM}, 5D pp. 285–286 (own words)',
  cards=(kcard('Deseasonalise',F(FR(['actual'],['SI']))),kcard('Reseasonalise','deseasonalised × SI'))))

# ================= Ex 14 / YT WE1b
S.append(qslide('we','Worked example 14 · 5D','Interpreting seasonal indices',
  '<div style="font-size:21px">Suppose that the seasonal indices (SI) for electricity usage in Esse’s home are as shown in the table:'
  +stab(SEAS,[(None,['1.16','0.94','1.26','0.64'])],22,'e14')+'</div>'
  +plist([('a','What does the seasonal index for Winter tell us?'),('b','What does the seasonal index for Spring tell us?')]),
  [('a','Winter SI = 1.26 = 126% → 26% above average','data-hi="#e14|c0_2|hy"'),('b','Spring SI = 0.64 = 64% → 100% − 64% = 36% below average','data-hi="#e14|c0_3|hy"')],
  '',f'{CAM} · Example 14 (p. 284)',video='Cambridge GO · Example 14 (5D Resources)',cmd=('What',None,'% above or below the average season'),
  parts=[('a','The seasonal index for Winter is 1.26. This tells us that Esse’s electricity usage in Winter is typically <b>26% higher</b> than the average season.'),
         ('b','The seasonal index for Spring is 0.64. This tells us that Esse’s electricity usage in Spring is typically <b>36% lower</b> than the average season.')]))
S.append(qslide('yt','You try · Edrolo 4D WE1b','Interpreting a seasonal index',
  '<div style="font-size:21px">Consider the following table.'
  +stab(['summer','autumn','winter','spring'],[('umbrella sales',[205,377,528,442])],22,'y1',lead='')+
  '<span class="muted" style="font-size:18px">Part a: the seasonal index for umbrella sales in summer, correct to two decimal places, is 0.53.</span><br><br>'
  'b. What does the rounded seasonal index for summer mean in terms of the <em class="v">umbrella sales</em> in summer compared to the average season?</div>',
  [('Percentage','0.53 = 53%','data-hi="#y1|c0_0|hy"'),('Below 100%','100% − 53% = 47% less than the average season')],
  'On average, the number of umbrella sales in summer is <b>53% of</b>, or <b>47% less than</b>, the average season.',f'{EDR} · 4D Worked example 1b (p. 269; part a’s table and answer given as context)',
  cmd=('What',None,'SI as a %, compared with average')))

# ================= Ex 15 / YT WE5
S.append(qslide('we','Worked example 15 · 5D','Using seasonal indices',
  '<div style="font-size:20px">The seasonal indices (SI) for cold drink sales for Imogen’s kiosk are as shown in the table:'
  +stab(SEAS,[(None,['1.75','0.66','0.46','1.13'])],22,'e15')+'</div>'
  +plist([('a','If the actual cold drink sales last summer totalled $21 653, what is the deseasonalised sales figure for that time period?'),
          ('b','If the deseasonalised cold drink sales last spring totalled $10 870, what were the actual sales for that time period?')]),
  [fx('a','deseasonalised',F(FR([V('actual','21 653')],[V('SI','1.75')])),'12 373.14','data-hi="#e15|c0_0|hy"'),
   fx('b','actual',F(V('deseasonalised','10 870'),' × ',V('SI','1.13')),'12 283.10','data-hi="#e15|c0_3|hy"')],
  '',f'{CAM} · Example 15 (p. 285)',video='Cambridge GO · Example 15 (5D Resources)',cmd=('what',None,'divide to deseasonalise, multiply to reseasonalise'),
  parts=[('a','Deseasonalised sales = <b>$12 373.14</b>'),('b','Actual sales = <b>$12 283.10</b>')]))
S.append(qslide('yt','You try · Edrolo 4D WE5','Reseasonalising',
  '<div style="font-size:26px;margin-top:30px">The seasonal index for Australian <em class="v">Oodie sales</em> in January is 0.65.<br>Last January, a store in Sydney sold a deseasonalised number of 540 Oodies.<br><br>How many Oodies did the store actually sell in January?</div>',
  [('Values','seasonal index = 0.65 · deseasonalised value = 540'),fx('Reseasonalise','actual value',F(V('SI','0.65'),' × ',V('deseasonalised','540')),'351')],
  'The store actually sold <b>351 Oodies</b> in January.',f'{EDR} · 4D Worked example 5 (p. 271)',cmd=('How many',None,'actual = SI × deseasonalised')))

# ================= Ex 16 / YT WE4
S.append(qslide('we','Worked example 16 · 5D','Percentage change to correct for seasonality',
  '<div style="font-size:19px">Consider the table below which gives the seasonal indices for heater sales at a discount store:'
  +stab(SEAS,[(None,['0.65','1.25','1.35','0.75'])],21,'e16')+'</div>'
  +plist([('a','By what percentage should the sales in summer be increased or decreased in order to deseasonalise the data? Give your answer as a percentage rounded to one decimal place.'),
          ('b','By what percentage should the sales in winter be increased or decreased in order to deseasonalise the data? Give your answer as a percentage rounded to one decimal place.')]),
  [('a · rule','deseasonalised sales = actual sales ÷ 0.65 = (1 ÷ 0.65) × actual sales','data-hi="#e16|c0_0|hy"'),
   ('a · multiplier','1 ÷ 0.65 = 1.538 = 153.8% → increase by 53.8%'),
   ('b · rule','deseasonalised sales = actual sales ÷ 1.35 = (1 ÷ 1.35) × actual sales','data-hi="#e16|c0_2|hy"'),
   ('b · multiplier','1 ÷ 1.35 = 0.741 = 74.1% → decrease by 100% − 74.1% = 25.9%')],
  '',f'{CAM} · Example 16 (p. 286)',video='Cambridge GO · Example 16 (5D Resources)',cmd=('By what percentage',None,'1 ÷ SI, then the % change'),
  parts=[('a','To correct for seasonality, the actual sales should be <b>increased by 53.8%</b>.'),('b','To correct for seasonality, the actual sales should be <b>decreased by 25.9%</b>.')]))
S.append(qslide('yt','You try · Edrolo 4D WE4','Correcting for seasonality',
  '<div style="font-size:28px;margin-top:40px">The seasonal index for January is 0.8. How should data for this season be adjusted to correct for seasonality?</div>',
  [('Seasonal index','seasonal index = 0.8'),('Reciprocal','1 ÷ 0.8 = 1.25'),('Interpret','1.25 = 125%: deseasonalised values are 125% of the actual value → increase by 25%')],
  'The data from January should be <b>increased by 25%</b> to correct for seasonality.',f'{EDR} · 4D Worked example 4 (p. 271)',cmd=('How',None,'1 ÷ SI → % change')))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2017 Exam 1 Q16','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The seasonal index for the sales of cold drinks in a shop in January is 1.6<br><br>To correct the January sales of cold drinks for seasonality, the actual sales should be</div>',
  [('Reciprocal','1 ÷ 1.6 = 0.625 = 62.5%'),('% change','100% − 62.5% = 37.5% → reduce by 37.5%')],
  'Reduced by 37.5%: <b>A</b>.','VCAA 2017 Further Mathematics Exam 1 Q16 (examiner report) · Edrolo General Mathematics Units 3&amp;4 4D Q19',
  mc=['reduced by 37.5%','reduced by 40%','reduced by 62.5%','increased by 60%','increased by 62.5%'],key='A',dist=[32,11,22,27,6],
  dis=('D','27%: read the SI straight off (1.6 → 60%) instead of using 1 ÷ 1.6; a busy season must be reduced, not increased.')))
def _rt(ks,r0):
    return ('<table class="t tight" style="font-size:16px;margin:6px auto"><tr><th></th>'+''.join(f'<th>{RMON[k]}</th>' for k in ks)+'</tr>'
            '<tr><th>Monthly rainfall (mm)</th>'+''.join(f'<td data-i="c{r0}_{k}">{RAIN[k]:.1f}</td>' for k in ks)+'</tr>'
            '<tr><th>Seasonal index</th>'+''.join(f'<td data-i="c{r0+1}_{k}">{RSI[k]:.3f}</td>' for k in ks)+'</tr></table>')
RT='<div id="x2t">'+_rt(range(6),0)+_rt(range(6,12),2)+'</div>'
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2020 Exam 1 Q17','Show what you know',
  '<div style="font-size:19px">Table 4 below shows the monthly rainfall for 2019, in millimetres, recorded at a weather station, and the associated long-term seasonal indices for each month of the year.'
  '<div style="font-size:15px;margin-top:8px"><b>Table 4</b></div>'+RT+'<br>The deseasonalised rainfall for May 2019 is closest to</div>',
  [('May','rainfall 92.6 mm · SI = 1.222','data-hi="#x2t|c0_4,c1_4|hy"'),fx('Deseasonalise','deseasonalised',F(FR([V('actual','92.6')],[V('SI','1.222')])),'75.78')],
  '75.8 mm: <b>B</b>.','VCAA 2020 Further Mathematics Exam 1 Q17–18 stem (Table 4, shown in two halves) and Q17 (examiner report) · Edrolo General Mathematics Units 3&amp;4 4D Q17',
  mc=['71.3 mm','75.8 mm','86.1 mm','88.1 mm','113.0 mm'],key='B',dist=[2,88,4,3,3]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5D',) and v.get('url')]))
n=assemble(S,'12MAG · L20 · Seasonal indices',os.path.join(ROOT,'lessons','5D seasonal indices slides.html'))
print(n-1,'slides')
