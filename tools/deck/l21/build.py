"""Lesson l21 (5D, calculating seasonal indices and deseasonalising) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5D deseasonalising slides.html
Run: python3 tools/deck/l21/build.py      Screenshots: python3 tools/deck/l21/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- Do Now: VCAA 2023 Exam 1 Q16 (D, 43%; A 5 B 39 C 9 D 43 E 4) ·
          VCAA 2024 NHT Exam 1 Q13 (C; NHT report: answers only; plot redrawn, grid 0.2 s) ·
          VCAA 2026 NHT Exam 2 Q4 stem + Q4bi (197.7; NHT report: answer only; sunspot plot not needed for part b, not shown) ·
          VCAA 2024 Exam 2 Q3 equation + part f + Q3gi (47% scored the mark; Table 2 / scatterplot not needed for part g, not shown; residual plot redrawn from the line).
- APK: Cambridge U1&2 Ch 1 skills checklist 1B #7 (replaces the card's 1B #6, burnt in l20) and 1F #14 (answers worked for 12MAG).
- Learn: Cambridge U3&4 5D pp. 287-291 (own words; 'Why deseasonalise?' plots p. 291 redrawn from Examples 18/19). Edrolo 4D theory p. 268.
- Worked examples: Cambridge U3&4 Examples 17, 18, 19 (pp. 287-290).
  You trys: Edrolo U3&4 4D Worked example 1a (p. 268), Worked example 2 (pp. 269-270), Worked example 3 (p. 270).
- No CAS on the card.
- Exit: Edrolo U3&4 4D Q18 = VCAA 2019 Further Exam 2 Q6a,b (6a: 32% full marks, average 0.9/2; 6b: 58%). Original VCAA wording.
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l21')
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
col=lambda r0,r1,k:','.join(f'c{r}_{k}' for r in range(r0,r1))
row=lambda r,n:','.join(f'c{r}_{k}' for k in range(n))

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:3px 10px!important;text-align:center;white-space:nowrap}.xs ol.parts li,.xs ol.parts li span{font-size:15px!important;line-height:1.3!important}.wrapth th{white-space:normal!important}</style>']
# ================= opening
S.append(title(21,'Calculating seasonal indices and deseasonalising',f'{CAM} · 5D Seasonal indices (calculating and deseasonalising)','L21'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills','var(--apk)'),
  ('Calculating seasonal indices','',None),('Why deseasonalise?','',None),('Worked examples 17–19','→ You try',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Seasonal index (SI)','compares a season with the average season'),
  ('Seasonal average','the mean of all the seasons in one cycle (one year)'),
  ('Several years','find each year’s SIs, then average each season’s SIs'),
  ('Check','the SIs add up to the number of seasons'),
  ('Deseasonalise','remove the seasonal effect so the trend is clearer')],
  [('Seasonal index',F('SI = ',FR(['value for season'],['seasonal average'])),'one year’s data'),
   ('Deseasonalise',F('deseasonalised = ',FR(['actual'],['SI'])),'divide by the SI'),
   ('Reseasonalise',F('actual = deseasonalised × SI'),'multiply by the SI')],
  f'{CAM}, 5D pp. 287–291; Study Design: seasonal indices and their calculation using seasonal and yearly means'))

# ================= Do Now 1: VCAA 2023 E1 Q16 (5D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q16','Review of 5D (last lesson)',
  '<div style="font-size:26px;margin-top:30px">The number of visitors each month to a zoo is seasonal.<br>To correct the number of visitors in January for seasonality, the actual number of visitors, to the nearest percent, is increased by 35%.<br><br>The seasonal index for that month is closest to</div>',
  [('Correcting','correct for seasonality = multiply by 1 ÷ SI'),('Increase 35%','1 ÷ SI = 1.35'),fx('SI','SI',F(FR(['1'],[V('1 ÷ SI','1.35')])),'0.741')],
  '0.74: <b>D</b>.','VCAA 2023 General Mathematics Exam 1 Q16 (examiner report)',
  mc=['0.61','0.65','0.69','0.74','0.77'],key='D',dist=[5,39,9,43,4],dis=('B','39%: took 100% − 35% = 65% → 0.65; the % change comes from 1 ÷ SI, not from the SI.')))
# ================= Do Now 2: VCAA 2024 NHT E1 Q13 (5C)
D2=tsm(M15,[None]*5+[209.4]+[None]*7,xs=M15_X,yr=(206,212),yt=1,xl='year',yl='winning time (seconds)',W=560,H=260,fs=12,xr=(2004,2016),xtick=2,sid='d2',r=3.5)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 NHT Exam 1 Q13','Review of 5C (two lessons ago)',
  ('<div style="font-size:18px">The following graph shows the <em class="v">winning time</em>, in seconds, for each <em class="v">year</em> from 2004 to 2016 for a men’s 1500 m track event.</div>',
   Wd(560,D2),'<div style="font-size:18px">The time series is smoothed using nine-median smoothing.<br>The smoothed value for the <em class="v">winning time</em> in 2009, in seconds, is closest to</div>'),
  [('Nine points','2009 and four each side: 2005 to 2013','data-hi="#d2|'+pk(range(1,10))+'|hy"'),
   ('Order','207.8, 208.8, 209.0, 209.2, <b>209.4</b>, 210.0, 210.4, 210.6, 211.4: 5th value'),
   ('Mark','cross at (2009, 209.4)','data-show="#d2|g5,m5"')],
  '209.4: <b>C</b>.','VCAA 2024 NHT General Mathematics Exam 1 Q13 (NHT report gives the answer only; plot redrawn, values read off)',
  mc=['209.0','209.2','209.4','210.0','210.4'],key='C',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 3: VCAA 2026 NHT E2 Q4bi (5B)
def _sun(ks,r0):
    return ('<table class="t tight" style="font-size:17px;margin:6px auto"><tr><th>Month</th>'+''.join(f'<td data-i="c{r0}_{k}"><b>{k+1}</b></td>' for k in ks)+'</tr>'
            '<tr><th>Number</th>'+''.join(f'<td data-i="c{r0+1}_{k}">{SUN[k]:.1f}</td>' for k in ks)+'</tr></table>')
ST='<div id="d3t">'+_sun(range(6),0)+_sun(range(6,12),2)+_sun(range(12,18),4)+'</div>'
win=','.join([f'c1_{k}' for k in range(2,6)]+[f'c3_{k}' for k in range(6,12)]+[f'c5_{k}' for k in range(12,15)])
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q4bi','Review of 5B (last week)',
  '<div style="font-size:19px">Sunspots are dark areas on the surface of the Sun. <span class="muted" style="font-size:16px">(time series plot not needed for this part)</span><br>'
  'b. Astronomers who monitor sunspot numbers use 13-point smoothing to display the underlying trend in the data.<br>'
  'The table below shows the mean monthly sunspot numbers for 18 consecutive months starting in March 1990 for the time series plot displayed on page 8.<br>'
  'In this table, month 1 is March 1990 and month 18 is August 1991.'+ST+
  'i. <b>Find</b> the 13-point mean smoothed value, rounded to one decimal place, for month 9 (November 1990). <span class="muted">(1 mark)</span></div>',
  [('13 points','month 9 and six each side: months 3 to 15','data-hi="#d3t|'+win+'|hy"'),
   fx('Mean','smoothed value',F(FR([V('sum','2569.8')],[V('n','13')])),'197.68')],
  'The 13-point mean smoothed value for month 9 is <b>197.7</b>.','VCAA 2026 NHT General Mathematics Exam 2 Q4 stem and Q4bi (NHT report gives the answer only; sunspot plot not shown: not needed for part b)',
  stat=('nht',),cmd=('Find',1,'six each side, then the mean')))
# ================= Do Now 4: VCAA 2024 E2 Q3gi (3C)
def resplot(sid,show=False):
    W,Hh,xr,yr=520,300,(1.90,2.08),(-0.02,0.04)
    s=scat(RES,xr,yr,0.02,0.01,'Wgold (m)','residual',W=W,H=Hh,r=4.5,fs=12,sid=sid,ink='#222')
    L,R,T,B=58,16,12,50; pw,ph=W-L-R,Hh-T-B
    X=lambda x:L+(x-xr[0])/(xr[1]-xr[0])*pw; Y=lambda y:T+ph-(y-yr[0])/(yr[1]-yr[0])*ph
    x0,y0=X(2.02),Y(0.0328); c='' if show else ' class="hid0"'
    add=(f'<line x1="{L}" x2="{L+pw}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" stroke="#333" stroke-width="1.5"/>'
         f'<g data-i="m"{c}><path d="M{x0-7:.1f},{y0-7:.1f}L{x0+7:.1f},{y0+7:.1f}M{x0-7:.1f},{y0+7:.1f}L{x0+7:.1f},{y0-7:.1f}" stroke="#d2475b" stroke-width="3.5"/></g>')
    return s.replace('</svg>',add+'</svg>')
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q3gi','Review of 3C (last term)',
  ('<div style="font-size:17px">When a least squares line is fitted to the scatterplot, the equation is found to be: &nbsp;<em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em><br>'
   'f. In 1984, the <em class="v">Wbest</em> value was 2.07 m for a <em class="v">Wgold</em> value of 2.02 m.<br>Show that when this least squares line is fitted to the scatterplot, the residual value for this point is 0.0328<br>'
   'g. The residual plot obtained when the least squares line was fitted to the data is shown below. The residual value from <b>part f</b> is missing from the residual plot.</div>',
   Wd(460,resplot('d4')),
   '<div style="font-size:17px">i. <b>Complete</b> the residual plot by adding the residual value from <b>part f</b>, drawn as a cross (X), to the residual plot above. <span class="muted">(1 mark)</span></div>'),
  [('Point','x = <em>Wgold</em> = 2.02 · residual = 0.0328 (from part f)'),
   ('Scale','0.0328 is just above 0.03 (each grid line = 0.005)'),
   ('Plot','cross at (2.02, 0.0328)','data-show="#d4|m"')],
  'A cross (X) at <em>Wgold</em> = 2.02 m, residual = 0.0328.','VCAA 2024 General Mathematics Exam 2 Q3 (equation, part f) and Q3gi (examiner report; Table 2 and scatterplot not shown: not needed for part g; residual plot redrawn)',
  stat=('mark',47),cmd=('Complete',1,'x = Wgold, y = residual')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK 1: Cambridge U1&2 1B #7 (replaces 1B #6, burnt in l20)
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1B #7','Percentage increase or decrease',
  '<div style="font-size:30px;margin-top:40px">A kg of bananas rose in value from $4.50 to $7.00. What was the % increase?</div>',
  [('Increase','$7.00 − $4.50 = $2.50'),fx('% increase','% increase',F(FR([V('increase','2.50')],[V('original','4.50')]),' × 100%'),'55.6%')],
  'The price increased by about <b>55.6%</b>.',f'{CAM12} · Ch 1 skills checklist 1B #7 · solution worked for 12MAG · replaces 1B #6 (already used in l20)',cmd=('What',None,'increase ÷ original × 100%')))
# ================= APK 2: Cambridge U1&2 1F #14
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1F #14','The unitary method',
  '<div style="font-size:30px;margin-top:40px">If 50 items cost $2500, how much do 10 items cost?</div>',
  [('One item','$2500 ÷ 50 = $50'),('Ten items','10 × $50 = $500')],
  '10 items cost <b>$500</b>.',f'{CAM12} · Ch 1 skills checklist 1F #14 · solution worked for 12MAG',cmd=('how much',None,'find one, then multiply')))

# ================= Learn 1: calculating seasonal indices
S.append(learn('Learn · 5D','Calculating seasonal indices',
  '<h4>Compare each season with the seasonal average</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>one year</b>: seasonal average = mean of that year’s seasons; SI = season ÷ average</li>'
  '<li><b>several years</b>: do this for every year, then <b>average each season’s SIs</b></li><li>check: the SIs add to the number of seasons</li></ul>',
  '<div style="font-size:25px;line-height:1.75;width:1000px;max-width:100%;margin:0 auto">'
  '<div class="frag">1. Find the seasonal (yearly) average: add the seasons, divide by how many there are.</div>'
  '<div class="frag">2. Divide each season’s value by that average → that year’s SIs.</div>'
  '<div class="frag">3. Several years? Repeat for each year, then find the mean SI for each season.</div>'
  '<div class="frag">4. Check: 4 quarters → SIs add to 4 · 12 months → 12 · 7 days → 7.</div></div>',
  'Keep 3 decimal places until the final average, then round as asked.',f'{CAM}, 5D pp. 287–289 (own words) · {EDR}, 4D p. 268',
  cards=(kcard('Seasonal index',F(FR(['value for season'],['seasonal average']))),kcard('Check','SIs add to the number of seasons'))))
# ================= Learn 2: why deseasonalise
def qplot(ys,yr,yl,sid):
    return ts(ys,xs=list(range(1,13)),yr=yr,yt=200 if yr[1]>1500 else 100,xl='quarter',yl=yl,W=470,H=270,fs=12,xr=(0,13),xtick=1,sid=sid,r=3.5)
ACT=sum(MIK,[]); DES=sum(MDES,[])
S.append(learn('Learn · 5D','Why deseasonalise?',
  '<h4>Take the seasons out to see the trend</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>deseasonalised value = actual ÷ SI</li><li>the seasonal ups and downs are removed</li><li>the underlying <b>trend</b> is clearer</li><li>deseasonalise before fitting a trend line (5E)</li></ul>',
  '<div style="display:flex;gap:24px;justify-content:center;align-items:flex-start">'
  f'<div style="width:470px"><div style="text-align:center;font-weight:700">Actual customers</div>{qplot(ACT,(0,1600),"actual customers","w1")}</div>'
  f'<div class="frag" style="width:470px"><div style="text-align:center;font-weight:700">Deseasonalised customers</div>{qplot(DES,(600,1400),"deseasonalised","w2")}</div></div>'
  '<div class="frag" style="font-size:24px;text-align:center;margin-top:10px">Actual: hard to tell if Mikki’s shop is growing · Deseasonalised: a clear <b>increasing trend</b>.</div>',
  'Deseasonalised values are not the real numbers: reseasonalise (× SI) to get actual values back.',f'{CAM}, 5D p. 291 (own words; plots redrawn from Examples 18–19 data)',
  cards=(kcard('Deseasonalise',F(FR(['actual'],['SI']))),)))

# ================= Ex 17 / YT WE1a
S.append(qslide('we','Worked example 17 · 5D','Calculating seasonal indices (1 year’s data)',
  '<div style="font-size:22px">Mikki runs a shop and she wishes to determine quarterly seasonal indices for the number of customers to her shop based on last year’s figures which are shown in the table opposite.'
  +stab(SEAS,[(None,MIK[0])],24,'e17')+'</div>',
  [fx('Average','quarterly average',F(FR([V('total','920 + 1085 + 1241 + 446')],[V('quarters','4')])),'923','data-hi="#e17|'+row(0,4)+'|hy"'),
   ('SIs','SI = value ÷ 923: 920 ÷ 923 = 0.997 · 1085 ÷ 923 = 1.176 · 1241 ÷ 923 = 1.345 · 446 ÷ 923 = 0.483'),
   ('Check','0.997 + 1.176 + 1.345 + 0.483 = 4.001 ≈ 4 (rounding)')],
  'Seasonal indices'+stab(SEAS,[(None,['0.997','1.176','1.345','0.483'])],20),f'{CAM} · Example 17 (p. 287)',video='Cambridge GO · Example 17 (5D Resources)',
  cmd=('determine',None,'season ÷ seasonal average')))
S.append(qslide('yt','You try · Edrolo 4D WE1a','Calculating a seasonal index',
  '<div style="font-size:24px;margin-top:20px">Consider the following table.'
  +stab(['summer','autumn','winter','spring'],[('umbrella sales',[205,377,528,442])],24,'y1',lead='')+
  '<br>a. Use the table to <b>calculate</b> the seasonal index for umbrella sales in summer, correct to two decimal places.</div>',
  [fx('Mean','mean of all seasons',F(FR([V('total','205 + 377 + 528 + 442')],[V('seasons','4')])),'388','data-hi="#y1|'+row(0,4)+'|hy"'),
   fx('Summer','seasonal index',F(FR([V('summer','205')],[V('mean','388')])),'0.5283…','data-hi="#y1|c0_0|hy"')],
  'Seasonal index for summer = <b>0.53</b>',f'{EDR} · 4D Worked example 1a (p. 268)',cmd=('calculate',None,'season ÷ mean of all seasons')))

# ================= Ex 18 / YT WE2
S.append(qslide('we','Worked example 18 · 5D','Calculating seasonal indices (several years’ data)',
  '<div style="font-size:20px">Suppose that Mikki has 3 years of data, as shown. Use the data to calculate seasonal indices, rounded to two decimal places.'
  +stab(SEAS,[(y+1,MIK[y]) for y in range(3)],22,'e18',lead='Year')+'</div>',
  [('Year 1','from Example 17: 0.997, 1.176, 1.345, 0.483','data-hi="#e18|'+row(0,4)+'|hy"'),
   ('Year 2','average = 4112 ÷ 4 = 1028 → 1.007, 1.148, 1.319, 0.526','data-hi="#e18|'+row(1,4)+'|hy"'),
   ('Year 3','average = 4732 ÷ 4 = 1183 → 1.098, 1.119, 1.226, 0.557','data-hi="#e18|'+row(2,4)+'|hy"'),
   fx('Summer','SI',F(FR([V('3 summer SIs','0.997 + 1.007 + 1.098')],[V('years','3')])),'1.03','data-hi="#e18|'+col(0,3,0)+'|hb"'),
   ('Others','Autumn (1.176 + 1.148 + 1.119) ÷ 3 = 1.15 · Winter 1.30 · Spring 0.52 · check: 1.03 + 1.15 + 1.30 + 0.52 = 4.00')],
  'Seasonal indices'+stab(SEAS,[(None,['1.03','1.15','1.30','0.52'])],20),f'{CAM} · Example 18 (pp. 288–289)',video='Cambridge GO · Example 18 (5D Resources)',
  cmd=('calculate',None,'each year’s SIs, then average')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 4D WE2','Seasonal indices from several years',
  '<div style="font-size:22px">For the following table, <b>calculate</b> the seasonal indices for summer, autumn, winter, and spring, correct to two decimal places.'
  +stab(['summer','autumn','winter','spring'],[(2019+y,E2[y]) for y in range(3)],24,'y2',lead='year')+'</div>',
  [('2019','mean = 148 ÷ 4 = 37 → 1.216, 0.810, 0.594, 1.378','data-hi="#y2|'+row(0,4)+'|hy"'),
   ('2020','mean = 168 ÷ 4 = 42 → 1.261, 0.690, 0.619, 1.428','data-hi="#y2|'+row(1,4)+'|hy"'),
   ('2021','mean = 196 ÷ 4 = 49 → 1.102, 0.836, 0.591, 1.469','data-hi="#y2|'+row(2,4)+'|hy"'),
   ('Average','summer (1.216 + 1.261 + 1.102) ÷ 3 = 1.19 · autumn 0.78 · winter 0.60 · spring 1.43','data-hi="#y2|'+col(0,3,0)+'|hb"')],
  'summer: <b>1.19</b>, autumn: <b>0.78</b>, winter: <b>0.60</b>, spring: <b>1.43</b>',f'{EDR} · 4D Worked example 2 (pp. 269–270)',cmd=('calculate',None,'each year, then average')))

# ================= Ex 19 / YT WE3
S.append(qslide('we','Worked example 19 · 5D','Deseasonalising a time series',
  '<div style="font-size:19px">The quarterly sales figures for Mikki’s shop over a 3-year period are given below.'
  +stab(SEAS,[(y+1,MIK[y]) for y in range(3)],20,'e19',lead='Year')
  +'Use the seasonal indices shown to deseasonalise these sales figures. Write answers rounded to the nearest whole number.'
  +stab(SEAS,[(None,MSI)],20,'e19s')+'</div>',
  [('Rule','deseasonalised = actual ÷ SI: divide each column by its SI'),
   ('Summer','920 ÷ 1.03 = 893 · 1035 ÷ 1.03 = 1005 · 1299 ÷ 1.03 = 1261','data-hi="#e19|'+col(0,3,0)+'|hy"'),
   ('Other seasons','Autumn ÷ 1.15 · Winter ÷ 1.30 · Spring ÷ 0.52','data-hi="#e19|'+','.join(col(0,3,k) for k in (1,2,3))+'|hb"')],
  'Deseasonalised sales figures'+stab(SEAS,[(y+1,MDES[y]) for y in range(3)],18,lead='Year'),f'{CAM} · Example 19 (p. 290)',video='Cambridge GO · Example 19 (5D Resources)',
  cmd=('deseasonalise',None,'actual ÷ SI')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 4D WE3','Deseasonalising',
  '<div style="font-size:21px">Use the given seasonal indices to <b>deseasonalise</b> the following time series data. Give values correct to the nearest whole number.'
  +stab(DAYS,[('seasonal index',E3SI),('number of steps',E3N),('deseasonalised number of steps',['']*7)],15,'y3',lead='').replace('class="t tight"','class="t tight wrapth"',1)+'</div>',
  [('Monday','seasonal index = 0.70 · actual value = 7500','data-hi="#y3|c0_0,c1_0|hy"'),
   fx('Substitute','deseasonalised value',F(FR([V('actual','7500')],[V('SI','0.70')])),'≈ 10 714'),
   ('Repeat','the other days: number of steps ÷ seasonal index')],
  'Mon: 10 714, Tue: 10 370, Wed: 7500, Thu: 10 667, Fri: 10 833, Sat: 10 000, Sun: 8000',f'{EDR} · 4D Worked example 3 (p. 270)',cmd=('deseasonalise',None,'actual ÷ SI')))

# ================= Exit: VCAA 2019 E2 Q6a,b
S.append(qslide('ex','Exit task · VCAA 2019 Exam 2 Q6a, b','Show what you know',
  '<div style="font-size:16px">The total rainfall, in millimetres, for each of the four seasons in 2015 and 2016 is shown in Table 5 below.<br><b>Table 5</b>'
  +stab(SEAS,[(2015,[142,156,222,120]),(2016,[135,153,216,96])],14,'x1',lead='Year')+'</div>'
  +plist([('a','The seasonal index for winter is shown in Table 6 below. Use the values in Table 5 to <b>find</b> the seasonal indices for summer, autumn and spring. Write your answers in Table 6, rounded to two decimal places. <span class="muted">(2 marks)</span>'
             +stab(SEAS,[('Seasonal index',['','','1.41',''])],15,lead='')),
          ('b','The total rainfall for each of the four seasons in 2017 is shown in Table 7 below.'+stab(SEAS,[(2017,[141,156,262,120])],15,'x2',lead='Year')
             +'Use the appropriate seasonal index from Table 6 to <b>deseasonalise</b> the total rainfall for winter in 2017. Round your answer to the nearest whole number. <span class="muted">(1 mark)</span>')]),
  [('a · averages','2015: 640 ÷ 4 = 160 · 2016: 600 ÷ 4 = 150','data-hi="#x1|'+row(0,4)+','+row(1,4)+'|hy"'),
   ('a · summer','(142 ÷ 160 + 135 ÷ 150) ÷ 2 = (0.8875 + 0.9) ÷ 2 = 0.89'),
   ('a · autumn, spring','autumn (0.975 + 1.02) ÷ 2 = 0.9975 → 1.00 · spring (0.75 + 0.64) ÷ 2 = 0.70'),
   fx('b','deseasonalised',F(FR([V('actual','262')],[V('SI','1.41')])),'185.8','data-hi="#x2|c0_2|hy"')],
  '',f'VCAA 2019 Further Mathematics Exam 2 Q6a, b (examiner report: 6a 32% full marks, 6b 58%) · {EDR} 4D Q18',
  stat=('mark',32),cmd=('find',3,'average of each year’s SIs'),
  parts=[('a','Summer <b>0.89</b> · Autumn <b>1.00</b> · Spring <b>0.70</b> (write 1.00, not 1)'),('b','Deseasonalised winter rainfall 2017 = <b>186 mm</b>')]))
S[-1]=S[-1].replace('<section class="slide T ex ','<section class="slide T ex sm xs ',1).replace('<ol class="parts">','<ol class="parts" style="font-size:15px;line-height:1.3">',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5D',) and v.get('url')]))
n=assemble(S,'12MAG · L21 · Deseasonalising',os.path.join(ROOT,'lessons','5D deseasonalising slides.html'))
print(n-1,'slides')
