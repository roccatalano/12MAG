"""Lesson l19 (5C, moving medians) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5C slides.html
Run: python3 tools/deck/l19/build.py      Screenshots: python3 tools/deck/l19/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- Do Now: VCAA 2024 NHT Exam 1 Q14 (B; NHT: answers only) · VCAA 2024 NHT Exam 1 Q5 (B; NHT: answers only) ·
          VCAA 2025 Exam 2 Q4 stem + Q4d (27% scored the mark; extrapolation; scatterplot as in l18) ·
          VCAA 2024 Exam 2 Q3 stem + Table 2 + Q3b (51% scored the mark; draw the least squares line; scatterplot as in l11).
- APK: VCAA 2020 Further Exam 2 Q3 table + Q3b (89%; IQR = 2.6) = Edrolo U1&2 1D Q17 (adapted by Edrolo: ORIGINAL used; boxplots not shown, table is enough).
  Card's Cambridge U1&2 2E checklist #10 is burnt (S3) -> dropped, as in l17/l18.
- Learn: Cambridge U3&4 5C p. 278 (locating medians graphically; own words). Study Design dot point.
- Worked examples: Cambridge U3&4 Examples 12, 13 (pp. 278-280; births plot values read off).
  You trys: Edrolo U3&4 4C Worked example 1 a-c (pp. 254-256), Worked example 2 a-d (pp. 257-259).
- No CAS on the card (moving medians are graphical).
- Exits: Edrolo U3&4 4C Q13 = VCAA 2021 Further Exam 1 Q13 (C, 53%; A 4 B 8 C 53 D 24 E 11) ·
         4C Q14 = VCAA 2016 Further Exam 2 Q4a (35% full marks, average 1/2) ·
         4C Q15 = VCAA 2019 Further Exam 1 Q13-14 stem + Q13 (E, 45%; A 18 B 10 C 15 D 12 E 45). Original VCAA wording.
"""
import os, sys, json, re
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
_s=__import__('importlib.util').util.spec_from_file_location('f18',os.path.join(H,'..','l18','figs.py')); _f18=__import__('importlib.util').util.module_from_spec(_s); _s.loader.exec_module(_f18)
HOUSE=_f18.HOUSE
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l19')
yid=lambda u:u.split('v=')[1].split('&')[0]
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def htab(rows,fs=14,tid='',key='c'):
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'
    for r,(h,cells) in enumerate(rows):
        t+='<tr><th>'+h+'</th>'+''.join(f'<td data-i="{key}{r}_{k}">{v}</td>' for k,v in enumerate(cells))+'</tr>'
    return t+'</table>'
def win(r,ks): return ','.join(f'c{r}_{k}' for k in ks)
pk=lambda ks:','.join(f'p{k}' for k in ks)
ylab=lambda svg:re.sub(r'x="15"( y="[^"]*" text-anchor="middle"[^>]*rotate\(-90) 15',r'x="-38"\1 -38',svg.replace('viewBox="0 0 400 200"','viewBox="-52 0 452 200"'))
ylab0=lambda svg:re.sub(r'(text-anchor="end"[^>]*>)(\d+)<',lambda m:m.group(1)+f'{int(m.group(2))*100000:,}'.replace(',',' ')+'<',svg)
MONL={k+1:m for k,m in enumerate(MON)}
# Cambridge Examples 12-13 plot (values read off p. 278; its 3- and 5-median answers agree)
EX12=[10,12.5,6,5,22,19.5,14,7.5,8.5,10,8,15]
M3=mmed(EX12,3); M5=mmed(EX12,5)
def sh(sid,ks,pre='m'): return f'data-show="#{sid}|'+','.join(f'{pre}{k}' for k in ks)+'"'

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:2px 6px!important;text-align:center}</style>']
# ================= opening
S.append(title(19,'Smoothing with moving medians',f'{CAM} · 5C Smoothing a time series plot using moving medians','L19',
               flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 12 question','var(--apk)'),
  ('Locating a median on a graph','',None),('Worked examples 12–13','→ You try',None),
  ('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Moving median smoothing','replace each value by the median of it and its neighbours; done straight onto the graph'),
  ('Odd number of points','3, 5, 7, 9 … points: the middle time of the group gets the smoothed value'),
  ('Median point','middle point across (time) and middle point up (value): mark it with a cross ×'),
  ('Lost points','an <i>n</i>-median has no value for the first and last (<i>n</i> − 1) ÷ 2 points'),
  ('Why medians?','they ignore one-off spikes (outliers), so large fluctuations are smoothed out')],
  [('Middle value',F('the ',FR(['<i>n</i> + 1'],['2']),'th value from smallest'),'3 points → 2nd · 5 → 3rd · 9 → 5th'),
   ('Lost points',F(FR(['<i>n</i> − 1'],['2']),' at each end'),'3-median → 1 · 5-median → 2')],
  f'{CAM}, 5C pp. 278–280; Study Design: moving medians, odd number of points only'))

# ================= Do Now 1: VCAA 2024 NHT E1 Q14 (5B)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q14','Review of 5B (last lesson)',
  '<div style="font-size:19px">The number of fruit drinks sold by a fast-food shop each day for 14 consecutive days was recorded.<br>These results are shown in the table below.<div style="margin:10px 0">'
  +htab([('Day',list(range(1,15))),('Number',DRINK)],14,'d1t')+'</div>The six-mean smoothed value with centring for day 8 is</div>',
  [('Seven values','days 5 to 11: 129, 187, 179, 71, 89, 131, 147','data-hi="#d1t|'+win(1,range(4,11))+'|hy"'),
   ('Mean 1','days 5–10: 786 ÷ 6 = 131'),('Mean 2','days 6–11: 804 ÷ 6 = 134'),
   ('Centred','(131 + 134) ÷ 2 = 132.5')],
  '132.5: <b>B</b>.','VCAA 2024 NHT General Mathematics Exam 1 Q14 (NHT report gives the answer only)',
  mc=['132','132.5','133','133.5','134'],key='B',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2024 NHT E1 Q5 (1H)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 NHT Exam 1 Q5','Review of 1H (last term)',
  '<div style="font-size:21px">The heights of a group of Year 9 students were measured and the standard deviation was found to be 12.25 cm.<br><br>'
  'One student with a height of 174.6 cm had a standardised score of <i>z</i> = 0.45<br><br>The mean height of this group of students, in centimetres, was closest to</div>',
  [fx('z-score','<i>z</i>',F(FR([V('x','174.6'),' − <i>x̄</i>'],[V('s','12.25')])),'0.45'),
   ('Rearrange','<i>x̄</i> = 174.6 − 0.45 × 12.25'),('Result','<i>x̄</i> = 174.6 − 5.5125 = 169.0875')],
  '169.1: <b>B</b>.','VCAA 2024 NHT General Mathematics Exam 1 Q5 (NHT report gives the answer only)',
  mc=['161.9','169.1','180.1','186.4','187.3'],key='B',stat=('nht',)))
# ================= Do Now 3: VCAA 2025 E2 Q4d (3A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q4d','Review of 3A',
  ('The scatterplot below shows the <em class="v">sale price</em> of a home, in dollars, against the distance of the home from the city centre of Melbourne, in kilometres, <em class="v">distance from city centre</em>.<br>The sample consists of three-bedroom homes sold between 2016 and 2018.',
   Wd(400,ylab(ylab0(SC([(x,y/100000) for x,y in HOUSE],(0,16),(0,25),1,5,'distance from city centre (km)','sale price ($)',W=400,H=200,r=4,fs=14,sid='d3s')))),
   'The equation of the least squares line for the data in the scatterplot is<div style="text-align:center"><em>sale price</em> = 1 765 353 – 35 054 × <em>distance from city centre</em></div>'
   'd. Jocelyn wants to sell her three-bedroom home located two kilometres from the city centre of Melbourne.<br>Would the predicted <em class="v">sale price</em> be an example of interpolation or extrapolation?<br>Briefly <b>explain</b> your answer. <span class="muted">(1 mark)</span>'),
  [('Data range (EV)','<em>distance</em> runs from about 5 km to 15.5 km','data-hi="#d3s|p|hy"'),
   ('2 km','2 km is outside that range (the EV), so it is extrapolation')],
  '<b>Extrapolation</b>, as 2 km lies outside the range of the <em>distance from city centre</em> data (the explanatory variable).',
  'VCAA 2025 General Mathematics Exam 2 Q4 stem and Q4d (examiner report: refer to the EV, not the sale price; scatterplot redrawn, values read off)',
  stat=('mark',27),cmd=('explain',1,'name it, then why')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2024 E2 Q3b (3A)
WT='<table class="t tight" style="font-size:11px"><tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y in WYR)+'</tr><tr><th><i>Wgold</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WGOLD)+'</tr><tr><th><i>Wbest</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WBEST)+'</tr></table>'
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q3b','Review of 3A',
  '<div style="font-size:15px">Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.</div>'
  f'<div style="margin:5px 0">{WT}</div><div style="display:flex;gap:10px;align-items:center"><div style="flex:none;width:300px">'
  +SC(list(zip(WGOLD,WBEST)),(1.90,2.08),(1.92,2.10),0.02,0.02,'Wgold (m)','Wbest (m)',W=400,H=270,r=4.5,fs=11,tl=((1.90,0.300+0.860*1.90),(2.08,0.300+0.860*2.08)),sid='d4s')+'</div>'
  '<div style="font-size:15.5px">When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em><br>The correlation coefficient is 0.9318<br><br>'
  'b. <b>Draw</b> the least squares line on the scatterplot. <span class="muted">(1 mark)</span></div></div>',
  [fx('Point 1','<em>Wbest</em>',F('0.300 + 0.860 × ',V('Wgold','1.90')),'1.934'),
   fx('Point 2','<em>Wbest</em>',F('0.300 + 0.860 × ',V('Wgold','2.08')),'2.0888'),
   ('Draw','plot (1.90, 1.934) and (2.08, 2.089), rule a line across the whole plot','data-show="#d4s|tl"')],
  'Line through (1.90, 1.934) and (2.08, 2.089), drawn across the scatterplot.',
  'VCAA 2024 General Mathematics Exam 2 Q3 stem, Table 2 and Q3b (examiner report: calculate two points, don’t draw by eye; scatterplot redrawn)',
  stat=('mark',51),cmd=('Draw',1,'two points from the equation')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK: VCAA 2020 E2 Q3b
S.append(qslide('apk','APK · VCAA 2020 Exam 2 Q3b','Medians and quartiles',
  '<div style="font-size:19px">In a study of the association between BMI and neck size, 250 men were grouped by neck size (below average, average and above average) and their BMI recorded.<br>'
  'Five-number summaries describing the distribution of BMI for each group are displayed in the table below along with the group size.<div style="margin:12px 0">'
  '<table class="t tight" id="a1t" style="font-size:16px"><tr><th>Neck size</th><th>Group size</th><th>Min.</th><th>Q<sub>1</sub></th><th>Median</th><th>Q<sub>3</sub></th><th>Max.</th></tr>'
  +''.join('<tr>'+''.join(f'<td data-i="c{r}_{k}">{v}</td>' for k,v in enumerate(row))+'</tr>' for r,row in enumerate(BMI))+'</table></div>'
  'b. What is the interquartile range (IQR) of BMI for the men with an average neck size? <span class="muted">(1 mark)</span></div>',
  [('Row','average neck size: Q<sub>1</sub> = 23.4, Q<sub>3</sub> = 26.0','data-hi="#a1t|c1_3,c1_5|hy"'),
   fx('IQR','IQR',F(V('Q3','26.0'),' − ',V('Q1','23.4')),'2.6')],
  'IQR = <b>2.6</b> kg/m²','VCAA 2020 Further Mathematics Exam 2 Q3 table and Q3b (examiner report; original wording; boxplots not shown) · = Edrolo General Mathematics Units 1&amp;2 1D Q17, adapted by Edrolo',
  stat=('mark',89),cmd=('What',1,'Q3 − Q1')))

# ================= Learn 1: locating a median graphically
LOC=tsm(LOC_Y,[None,3,None],xs=LOC_X,yr=(0,5),yt=1,xl='x',yl='y',W=380,H=260,fs=14,xr=(0,5),r=5,sid='lp1',hidline=True)
S.append(learn('Learn · 5C','Locating a median on a graph',
  '<h4>Three points → one median point</h4><ol style="font-size:19px;line-height:1.5;margin-left:26px"><li>find the <b>middle point across</b> (x): draw a vertical line through it</li>'
  '<li>find the <b>middle point up</b> (y): draw a horizontal line through it</li><li>the median is where the lines cross: mark it with a <b style="color:#d2475b">×</b></li></ol>'
  '<p style="font-size:17px">The cross need not sit on a data point.</p>',
  Wd(380,LOC),'Points (1, 3), (3, 1), (4, 4): middle x = 3, middle y = 3 → median point (3, 3).',f'{CAM}, 5C p. 278 (own words)',
  frags='<span class="frag" data-show="#lp1|g1"></span><span class="frag" data-show="#lp1|m1"></span>'))
# ================= Learn 2: moving median smoothing
L2=tsm(EX12,M3,yr=(0,25),yt=5,xl='month',yl='number of births',W=560,H=240,fs=12,xlab=MONL,sid='lp2',r=3,guides=False)
S.append(learn('Learn · 5C','Moving median smoothing',
  '<h4>Smooth straight onto the graph</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>three-median: median of each point and <b>one</b> each side</li>'
  '<li>five-median: <b>two</b> each side; nine-median: <b>four</b> each side</li><li>always use the <b>original</b> points, never the crosses</li>'
  '<li>join the crosses: the trend shows through</li><li>odd numbers of points only (no centring)</li></ul>',
  Wd(560,L2),'More points in each median → a smoother plot, but more points lost at the ends.',f'{CAM}, 5C pp. 278–280 (plot: Example 12)',
  frags=f'<span class="frag" {sh("lp2",range(1,11))}></span><span class="frag" data-show="#lp2|ml"></span>',
  cards=(kcard('Lost points',F(FR(['<i>n</i> − 1'],['2']),' at each end')),)))

# ================= WE12 / YT WE1
def P12(sid,meds): return tsm(EX12,meds,yr=(0,25),yt=5,xl='month',yl='number of births',W=430,H=230,fs=12,xlab=MONL,sid=sid,r=3)
S.append(qslide('we','Worked example 12 · 5C','Three-moving median smoothing using a graphical approach',
  ('<div style="font-size:20px">Construct a three-median smoothed plot of the time series plot shown below.</div>',Wd(430,P12('e12',M3)),''),
  [('Jan, Feb, Mar','middle month = Feb; middle number = 10 → cross at (Feb, 10)','data-hi="#e12|p0,p1,p2|hy" data-show="#e12|g1,m1"'),
   ('Feb, Mar, Apr','middle month = Mar; middle number = 6 → cross at (Mar, 6)','data-hi="#e12|p1,p2,p3|hy" data-show="#e12|g2,m2"'),
   ('Keep going','one month along each time, until Oct, Nov, Dec','data-hi="#e12||hy" '+sh('e12',range(3,11))),
   ('Join','join the crosses with line segments','data-show="#e12|ml"')],
  'Three-median smoothed plot drawn: Feb 10, Mar 6, Apr 6, May 19.5, Jun 19.5, Jul 14, Aug 8.5, Sep 8.5, Oct 8.5, Nov 10.',f'{CAM} · Example 12 (pp. 278–279; plot redrawn, values read off)',
  video='Cambridge GO · Example 12 (5C Resources)',cmd=('Construct',None,'cross, slide one along, join')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
WE1=mmed(SCREEN,3)
S.append(qslide('yt','You try · Edrolo 4C WE1','Three-median smoothing',
  ('<div style="font-size:18px">Bailey recorded their screen time, in minutes, on their phone over the past week. Their data is presented in the following time series plot.</div>',
   Wd(400,tsm(SCREEN,WE1,yr=(40,120),yt=10,xl='day',yl='screen time (mins)',W=400,H=220,fs=12,sid='y1',r=4)),
   plist([('a','Determine the three-median smoothed <i>screen time</i> for day 5.'),('b','Construct a three-median smoothed plot for the entire time series.'),('c','What, if any, trend can be seen from the three-median smoothed time series?')])),
  [('a','days 4, 5, 6: 107, 81, 102 → middle value 102','data-hi="#y1|p3,p4,p5|hy" data-show="#y1|g4,m4"'),
   ('b','day 2: 82, 55, 70 → 70; day 3: 55, 70, 107 → 70; day 4: 70, 107, 81 → 81; day 6: 81, 102, 113 → 102','data-hi="#y1||hy" '+sh('y1',(1,2,3,5))),
   ('b · join','join the crosses (days 2 to 6)','data-show="#y1|ml"'),
   ('c','the crosses rise from left to right')],
  '',f'{EDR} · 4C Worked example 1 (pp. 254–256; plot redrawn)',cmd=('Determine',None,'middle point of each group'),
  parts=[('a','<b>102 minutes</b>'),('b','Crosses at 70, 70, 81, 102, 102 (days 2–6), joined.'),('c','The three-median smoothed data shows an <b>increasing trend</b> in Bailey’s screen time over the week.')]))
S[-1]=S[-1].replace('<section class="slide T yt mp"','<section class="slide T yt mp sm"',1)
# ================= WE13 / YT WE2
S.append(qslide('we','Worked example 13 · 5C','Five-moving median smoothing using a graphical approach',
  ('<div style="font-size:20px">Construct a five-median smoothed plot of the time series plot shown below.</div>',Wd(430,P12('e13',M5)),''),
  [('Jan to May','middle month = Mar; middle number = 10 (3rd of 5) → cross at (Mar, 10)','data-hi="#e13|p0,p1,p2,p3,p4|hy" data-show="#e13|g2,m2"'),
   ('Feb to Jun','middle month = Apr; middle number = 12.5 → cross at (Apr, 12.5)','data-hi="#e13|p1,p2,p3,p4,p5|hy" data-show="#e13|g3,m3"'),
   ('Keep going','one month along each time, until Aug to Dec','data-hi="#e13||hy" '+sh('e13',range(4,10))),
   ('Join','join the crosses with line segments','data-show="#e13|ml"')],
  'Five-median smoothed plot drawn (Mar to Oct). It is much smoother than the three-median plot.',f'{CAM} · Example 13 (pp. 279–280; plot redrawn, values read off)',
  video='Cambridge GO · Example 13 (5C Resources)',cmd=('Construct',None,'five at a time, cross, join')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
WE2=mmed(GOALS,5)
S.append(qslide('yt','You try · Edrolo 4C WE2','Five- and nine-median smoothing',
  ('<div style="font-size:17px">Emanuel is the goalkeeper for his soccer team and has recorded the <i>number of goals saved</i> each month for the past ten months. His data has been presented in the following time series plot.</div>',
   Wd(400,tsm(GOALS,WE2,yr=(0,30),yt=5,xl='month',yl='number of goals saved',W=400,H=210,fs=12,sid='y2',r=4)),
   plist([('a','Determine the five-median smoothed <i>number of goals saved</i> for month 8.'),('b','Determine the nine-median smoothed <i>number of goals saved</i> for month 5.'),
          ('c','Construct a five-median smoothed plot for the entire time series.'),('d','What, if any, trend can be seen from the five-median smoothed time series?')])),
  [('a','months 6 to 10: 13, 11, 15, 7, 12 → 3rd value = 12','data-hi="#y2|'+pk(range(5,10))+'|hy" data-show="#y2|g7,m7"'),
   ('b','months 1 to 9 → order: 7, 10, 11, 13, <b>15</b>, 17, 18, 18, 25 → 5th value = 15','data-hi="#y2|'+pk(range(0,9))+'|hb"'),
   ('c','month 3: 18; month 4: 17; then 17, 15, 13, 12 (months 5–8)','data-hi="#y2||hy" '+sh('y2',(2,3,4,5,6))),
   ('c · join','join the crosses (months 3 to 8)','data-show="#y2|ml"'),
   ('d','the crosses fall from left to right')],
  '',f'{EDR} · 4C Worked example 2 (pp. 257–259; plot redrawn)',cmd=('Determine',None,'middle of 5 (or 9) values'),
  parts=[('a','<b>12</b> goals saved'),('b','<b>15</b> goals saved'),('c','Crosses at 18, 17, 17, 15, 13, 12 (months 3–8), joined.'),('d','The five-median smoothed data shows a <b>decreasing trend</b> in number of goals saved.')]))
S[-1]=S[-1].replace('<section class="slide T yt mp"','<section class="slide T yt mp sm"',1)

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2021 Exam 1 Q13','Show what you know',
  ('<div style="font-size:19px">The time series plot below shows the <em class="v">points scored</em> by a basketball team over 40 games.</div>',
   Wd(560,tsm(PTS,[None]*9+[110]+[None]*30,yr=(90,150),yt=10,xl='game number',yl='points scored',W=560,H=240,fs=12,sid='x1',r=3,xr=(0,40),xtick=5)),
   '<div style="font-size:19px">The nine-median smoothed <em class="v">points scored</em> for game number 10 is closest to</div>'),
  [('Nine points','game 10 and four each side: games 6 to 14','data-hi="#x1|'+pk(range(5,14))+'|hy"'),
   ('Order','96.5, 102, 108.5, 109.5, <b>110</b>, 112, 118, 118, 134: 5th value'),
   ('Mark','cross at (10, 110)','data-show="#x1|g9,m9"')],
  '110: <b>C</b>.','VCAA 2021 Further Mathematics Exam 1 Q13 (examiner report; plot redrawn, values read off) · Edrolo General Mathematics Units 3&amp;4 4C Q13',
  mc=['102','108','110','112','117'],key='C',dist=[4,8,53,24,11],dis=('D','24%: probably used games 6–14 but miscounted the middle (6th value 112), or included game 15. Nine points → 5th value.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide sm"',1)
RM=mmed(RMIN,5)
X2=tsm(RMIN,RM,yr=(0,100),yt=10,xl='month number',yl='minimum rainfall (mm)',W=480,H=230,fs=12,sid='x2',r=4,xr=(0,13))
for k in (2,3,4,5):  # the four crosses printed in the question: visible, in the plot colour
    i=X2.index(f'<g data-i="m{k}" class="hid0">'); j=X2.index('</g>',i)
    X2=X2[:i]+X2[i:j].replace(' class="hid0"','').replace('#d2475b','#1f4fb0')+X2[j:]
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2016 Exam 2 Q4a','Show what you know',
  ('<div style="font-size:17px">The time series plot below shows the <em class="v">minimum rainfall</em> recorded at the weather station each month plotted against the <em class="v">month number</em> (1 = January, 2 = February, and so on).<br>Rainfall is recorded in millimetres.<br>The data was collected over a period of one year.</div>',
   Wd(480,X2),
   '<div style="font-size:17px">Five-median smoothing has been used to smooth the time series plot above.<br>The first four smoothed points are shown as crosses (×).<br>Complete the five-median smoothing by marking smoothed values with crosses (×) on the time series plot above. <span class="muted">(2 marks)</span></div>'),
  [('Month 7','months 5 to 9: 95, 50, 83, 61, 74 → 3rd value = 74','data-hi="#x2|'+pk(range(4,9))+'|hy" data-show="#x2|g6,m6"'),
   ('Month 8','months 6 to 10: 50, 83, 61, 74, 48 → 61','data-hi="#x2|'+pk(range(5,10))+'|hy" data-show="#x2|g7,m7"'),
   ('Month 9','months 7 to 11: 83, 61, 74, 48, 67 → 67','data-hi="#x2|'+pk(range(6,11))+'|hy" data-show="#x2|g8,m8"'),
   ('Month 10','months 8 to 12: 61, 74, 48, 67, 53 → 61 (last one: months 11, 12 have no value)','data-hi="#x2|'+pk(range(7,12))+'|hy" data-show="#x2|g9,m9"')],
  'Crosses at (7, 74), (8, 61), (9, 67), (10, 61).','VCAA 2016 Further Mathematics Exam 2 Q4a (examiner report: place the crosses graphically; plot redrawn, values read off) · Edrolo General Mathematics Units 3&amp;4 4C Q14',
  stat=('mark',35),cmd=('Complete',2,'five at a time from the original points')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)
L3=mmed(LIV,3); L5=mmed(LIV,5)
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2019 Exam 1 Q13','Show what you know',
  ('<div style="font-size:18px">The time, in minutes, that Liv ran each day was recorded for nine days.<br>These times are shown in the table below.<div style="margin:8px 0">'
   +htab([('Day number',list(range(1,10))),('Time (minutes)',LIV)],15,'x3t')+'</div>The time series plot below was generated from this data.</div>',
   Wd(330,tsm(LIV,[None]*6+[37]+[None]*2,yr=(0,70),yt=10,xl='day number',yl='time (minutes)',W=380,H=215,fs=12,sid='x3',r=4,xr=(0,10))),
   '<div style="font-size:18px">Both three-median smoothing and five-median smoothing are being considered for this data.<br>Both of these methods result in the same smoothed value on <em class="v">day number</em></div>'),
  [('Three-median','days 2–8: 28, 40, 28, 51, 33, 37, 37','data-hi="#x3t|'+win(1,range(9))+'|hy"'),
   ('Five-median','days 3–7: 28, 40, 33, 37, 37'),
   ('Compare','day 3: 40 vs 28 · day 4: 28 vs 40 · day 5: 51 vs 33 · day 6: 33 vs 37 · <b>day 7: 37 and 37</b>','data-show="#x3|g6,m6"')],
  'Day 7: <b>E</b>.','VCAA 2019 Further Mathematics Exam 1 Q13–14 stem and Q13 (examiner report; plot redrawn) · Edrolo General Mathematics Units 3&amp;4 4C Q15',
  mc=['3','4','5','6','7'],key='E',dist=[18,10,15,12,45],dis=('A','18%: day 3 is the first day with BOTH smoothed values, but they differ (40 vs 28). Check every day.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5C',) and v.get('url')]))
n=assemble(S,'12MAG · L19 · Smoothing with moving medians',os.path.join(ROOT,'lessons','5C slides.html'))
print(n-1,'slides')
