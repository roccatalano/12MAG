"""Lesson l17 (5B, moving means) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5B moving means slides.html
Run: python3 tools/deck/l17/build.py      Screenshots: python3 tools/deck/l17/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- Do Now: VCAA 2024 Exam 1 Q11-12 stem + table + Q12 (A, 48%; A 48 B 22 C 15 D 13; scatterplot redrawn from the table) ·
          VCAA 2026 NHT Exam 1 Q10 (A; NHT: no %; plot redrawn, values read off) ·
          VCAA 2023 Exam 2 Q4 stem + Q4a (26% scored the mark, average 0.3/1; report answer 'Maximum values occur 12 months apart'; plot redrawn) ·
          VCAA 2024 NHT Exam 2 Q4 stem + Q4b (r = -0.686; NHT: no %; scatterplot redrawn, values read off).
- APK: VCAA 2017 Further Exam 1 Q3 (= Edrolo U1&2 1E Q11, which Edrolo adapted with new data: the ORIGINAL wording and data are used here;
  D, 88%; A 1 B 3 C 7 D 88 E 2). The card's Cambridge U1&2 2E checklist #10 is burnt (S3) and every other Ch 2 mean/median
  checklist item is burnt too, so it is dropped (QUEUE Decisions log).
- Learn: Cambridge U3&4 5B pp. 268-270 (own words).
- Worked examples: Cambridge U3&4 Examples 7, 8 (pp. 268-270). You trys: Edrolo U3&4 4B Worked example 1 (pp. 234-238), 4B Worked example 3 (pp. 243-245).
- CAS: planner/cas-skills.json 'moving-means' (steps from Edrolo 4B WE1 spreadsheet method); data = Cambridge Example 8.
- Exits: Edrolo U3&4 4B Q15 = VCAA 2019 Further Exam 1 Q16 (+ Q15-16 stem and plot; C, 74%; A 7 B 11 C 74 D 5 E 2) ·
         4B Q17 = VCAA 2021 Further Exam 1 Q14 (B, 48%; A 8 B 48 C 15 D 25 E 3). Original VCAA wording.
  (Card's 4B Q16 = VCAA 2017 E1 Q15 is a four-point mean WITH CENTRING = l18 content: swapped with l18's 4B Q15.)
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
import importlib.util
_s=importlib.util.spec_from_file_location('f5',os.path.join(H,'..','l05','figs.py')); _f5=importlib.util.module_from_spec(_s); _s.loader.exec_module(_f5); scat=_f5.scat
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l17')
yid=lambda u:u.split('v=')[1].split('&')[0]
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def B(cls,val,ph='&nbsp;'): return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def htab(rows,fs=14,tid='',key='c'):
    """horizontal table; rows = (header, [cells]); cell k of row r gets data-i="{key}{r}_{k}" and the whole column data-i="col{k}" """
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'
    for r,(h,cells) in enumerate(rows):
        t+='<tr><th>'+h+'</th>'+''.join(f'<td data-i="{key}{r}_{k}">{v}</td>' for k,v in enumerate(cells))+'</tr>'
    return t+'</table>'
def vtab(cols,fs=14,tid='',key='c'):
    """vertical table; cols = (header, [cells]); cell k of column r gets data-i="{key}{r}_{k}" (same keys as htab)"""
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px"><tr>'+''.join(f'<th>{h}</th>' for h,_ in cols)+'</tr>'
    for k in range(len(cols[0][1])):
        t+='<tr>'+''.join(f'<td data-i="{key}{r}_{k}">{c[k]}</td>' for r,(h,c) in enumerate(cols))+'</tr>'
    return t+'</table>'
def win(r,ks): return ','.join(f'c{r}_{k}' for k in ks)
f1=lambda v:'–' if v is None else f'{v:.1f}'

S=['<style>.kcas .ytf{height:130px!important;padding-top:0!important}.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:2px 6px!important;text-align:center}'
   '</style>']
# ================= opening
S.append(title(17,'Smoothing with moving means',f'{CAM} · 5B Smoothing a time series using moving means','L17',
               flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 question','var(--apk)'),
  ('Three- and five-moving means','',None),('Worked examples 7–8','→ You try',None),('CAS: moving means in a spreadsheet','',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mini=lambda ys,ov:ts(ys,W=170,H=44,fs=1,grid=False,r=2,lw=1.4,overlays=[(ov,'#d2475b','m','')]).replace('font-size="0"','font-size="0" fill="none"').replace('class="hid0"','')
S.append(keys([
  ('Smoothing','replacing each value by the mean of it and its neighbours: irons out irregular fluctuations so the trend shows',mini(E8_B,mm(E8_B,5))),
  ('Three-moving mean','the mean of a value and the one value on each side'),
  ('Five-moving mean','the mean of a value and the two values on each side'),
  ('Lost points','an <i>n</i>-moving mean (<i>n</i> odd) has no value for the first and last (<i>n</i> − 1) ÷ 2 points')],
  [('Three-mean',F('smoothed <i>y</i><sub>2</sub> = ',FR(['<i>y</i><sub>1</sub> + <i>y</i><sub>2</sub> + <i>y</i><sub>3</sub>'],['3']))),
   ('Five-mean',F('smoothed <i>y</i><sub>3</sub> = ',FR(['<i>y</i><sub>1</sub> + <i>y</i><sub>2</sub> + <i>y</i><sub>3</sub> + <i>y</i><sub>4</sub> + <i>y</i><sub>5</sub>'],['5']))),
   ('Number of smoothed points','<i>N</i> − (<i>n</i> − 1)','<i>N</i> data points, <i>n</i>-moving mean')],
  f'{CAM}, 5B pp. 268–270'))

# ================= Do Now 1: VCAA 2024 E1 Q12 (4D)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q12','Review of 4D',
  ('<div style="font-size:16px">The number of breeding pairs of a small parrot species has been declining over recent years.<br>The table below shows the number of breeding pairs counted, <em class="v">pairs</em>, and the year number, <em class="v">year</em>, for the last 12 years. A scatterplot of this data is also provided.<br>The association between <em class="v">pairs</em> and <em class="v">year</em> is non-linear.</div>',
   '<div style="display:block;width:100%">'+htab([('<i>year</i>',list(range(1,13))),('<i>pairs</i>',PAIRS)],13,'d1t')
   +Wd(360,scat(list(zip(range(1,13),PAIRS)),(0,12),(140,340),2,20,'year','pairs',W=420,H=190,r=4,fs=12,sid='d1s'))+'</div>',
   '<div style="font-size:16px">A reciprocal transformation applied to the variable <em class="v">pairs</em> can also be used to linearise the scatterplot.<br>When a least squares line is fitted to the plot of <span style="font-size:18px">'+F(FR(['1'],['<em>pairs</em>']))+'</span> versus <em class="v">year</em>, the largest difference between the actual value and the predicted value occurs at <em class="v">year</em></div>'),
  [('Transform','CAS: list 1/<em>pairs</em>, then LinReg of 1/<em>pairs</em> on <em>year</em>'),
   ('Residuals','CAS residuals (× 10⁻⁴): year 1 → −6.6, year 12 → −3.6, all others smaller'),
   ('Largest','year 1 is furthest from the line','data-hi="#d1s|p0|hy"')],
  '<em>year</em> 1: <b>A</b>.','VCAA 2024 General Mathematics Exam 1 Q11–12 stem, table and Q12 (examiner report; scatterplot redrawn from the table)',
  mc=['1','2','11','12'],key='A',dist=[48,22,15,13],dis=('B','22% chose year 2: the reciprocal pulls year 1 furthest from the line, so check every residual on CAS.')))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2026 NHT E1 Q10 (4D)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 NHT Exam 1 Q10','Review of 4D',
  ('A graph of annual health expenditure, <em class="v">health cost</em>, in dollars, against <em class="v">age</em>, in years, is given below.',
   Wd(420,scat(HEALTH,(0,100),(0,14000),20,2000,'age (years)','health cost (dollars)',W=480,H=230,r=4,fs=12,sid='d2s')),
   'Which one of the following transformations would be most suitable for achieving linearity in the data?'),
  [('Shape','the points curve upwards, getting steeper: like the top-right of the circle of transformations'),
   ('Options','top right → <em>x</em><sup>2</sup> or <em>y</em><sup>2</sup>; (<em>health cost</em>)<sup>2</sup> would make it curve more, so square the EV')],
  '(<em>age</em>)<sup>2</sup>: <b>A</b>.','VCAA 2026 NHT General Mathematics Exam 1 Q10 (plot redrawn, values read off; NHT report gives no %)',
  mc=['(<em>age</em>)<sup>2</sup>','log<sub>10</sub>(<em>age</em>)','<span style="font-size:18px">'+F(FR(['1'],['<em>age</em>']))+'</span>','(<em>health cost</em>)<sup>2</sup>'],key='A',stat=('nht',)))
# ================= Do Now 3: VCAA 2023 E2 Q4a (5A)
peaks=[5,17,29]
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q4a','Review of 5A',
  ('The time series plot below shows the average monthly ice cream <em class="v">consumption</em> recorded over three years, from January 2010 to December 2012.<br>The data for the graph was recorded in the Northern Hemisphere.<br>In this graph, month number 1 is January 2010, month number 2 is February 2010 and so on.',
   Wd(470,ts(ICE,yr=(0.10,0.24),yt=0.02,xl='month number',yl='consumption (litres/person)',W=520,H=230,fs=11,xtick=3,xr=(0,37),r=2.8,sid='d3f')),
   'a. Identify a feature of this plot that is consistent with this time series having a seasonal component. <span class="muted">(1 mark)</span>'),
  [('Look for a repeat','peaks at months 6, 18 and 30','data-hi="#d3f|'+','.join(f'p{k}' for k in peaks)+'|hy"'),
   ('How far apart?','18 − 6 = 12 and 30 − 18 = 12: the same time each year')],
  'Maximum values occur <b>12 months apart</b>.','VCAA 2023 General Mathematics Exam 2 Q4 stem and Q4a (examiner report; plot redrawn, values read off)',
  stat=('mark',26),cmd=('Identify',1,'a feature you can see')))
# ================= Do Now 4: VCAA 2024 NHT E2 Q4b (2G)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q4b','Review of 2G',
  ('In another study, the heights, in metres, of the highest high tide (<em class="v">HHT</em>) for that day and the lowest low tide (<em class="v">LLT</em>) for that day were recorded in Sydney Harbour for the 31 days of July 2021.<br>A scatterplot of this data is shown below.',
   Wd(400,scat(TIDE,(0.20,0.64),(1.2,2.1),0.04,0.1,'LLT (m)','HHT (m)',W=480,H=220,r=3.5,fs=11,sid='d4s')),
   'When a least squares line is fitted to the scatterplot, the equation is found to be: <em>HHT</em> = 2.19 − 1.08 × <em>LLT</em><br>The coefficient of determination is 0.4709<br>'
   'b. Determine the value of the correlation coefficient <i>r</i>.<br>Round your answer to three decimal places. <span class="muted">(1 mark)</span>'),
  [fx('Size','<i>r</i>',F('±√',V('r²','0.4709')),'±0.68622…'),('Sign','slope −1.08 &lt; 0 → negative association: <i>r</i> is negative')],
  '<i>r</i> = <b>−0.686</b>','VCAA 2024 NHT General Mathematics Exam 2 Q4 stem and Q4b (scatterplot redrawn, values read off; NHT report gives no %)',stat=('nht',),cmd=('Determine',1,'size from r², sign from the slope')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK: VCAA 2017 E1 Q3
S.append(qslide('apk','APK · Year 11 · VCAA 2017 Exam 1 Q3','Mean and standard deviation',
  '<div style="font-size:21px">The table below shows the forearm circumference, in centimetres, of a sample of 10 people selected from this group of 252 people.<div style="margin:12px 0">'
  +htab([('Circumference',ARM)],17,'a1t')+'</div>The mean, <i>x̄</i>, and the standard deviation, <i>s<sub>x</sub></i>, of the forearm circumference for this sample of people are closest to</div>',
  [('CAS','enter the 10 values in a list → One-Variable Statistics','data-hi="#a1t|'+win(0,range(10))+'|hy"'),fx('Mean','<i>x̄</i>',F(FR(['sum'],[V('n','10')])),'277.7 ÷ 10 = 27.77'),
   ('Standard deviation','CAS: <i>s<sub>x</sub></i> = 1.664…')],
  '<i>x̄</i> = 27.8, <i>s<sub>x</sub></i> = 1.66: <b>D</b>.',
  'VCAA 2017 Further Mathematics Exam 1 Q3 (examiner report; original wording and data; = Edrolo General Mathematics Units 1&amp;2 1E Q11, adapted by Edrolo)',
  mc=['<i>x̄</i> = 1.58 &nbsp; <i>s<sub>x</sub></i> = 27.8','<i>x̄</i> = 1.66 &nbsp; <i>s<sub>x</sub></i> = 27.8','<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 1.58','<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 1.66','<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 2.30'],
  key='D',dist=[1,3,7,88,2],dis=('C','7% took σ<sub>x</sub> (population, 1.58) instead of the sample <i>s<sub>x</sub></i>.')))

# ================= Learn 1: three-moving mean
L8=ts(E8_B,yr=(0,25),yt=5,xl='month',yl='births',W=560,H=240,fs=12,xlab={k+1:m for k,m in enumerate(MON)},sid='lp1',r=3,
      overlays=[(mm(E8_B,3),'#d2475b','m3','')])
S.append(learn('Learn · 5B','Smoothing with a three-moving mean',
  '<h4>Three-moving mean</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>irregular fluctuations can hide the trend: <b>smoothing</b> irons them out</li>'
  '<li>replace each value by the <b>mean of it and the one on each side</b></li><li>slide the window of three along one place at a time</li>'
  '<li>the first and last values have no neighbour on one side: <b>no smoothed value</b></li></ul>',
  Wd(560,L8),'Plot each smoothed value at the CENTRE of its window (the middle time).',f'{CAM}, 5B pp. 268–269 (data: Example 8)',
  frags='<span class="frag" data-show="#lp1|m3"></span>',cards=(kcard('Three-mean',F('smoothed <i>y</i><sub>2</sub> = ',FR(['<i>y</i><sub>1</sub> + <i>y</i><sub>2</sub> + <i>y</i><sub>3</sub>'],['3']))),)))
# ================= Learn 2: five-moving mean
L9=ts(E8_B,yr=(0,25),yt=5,xl='month',yl='births',W=560,H=240,fs=12,xlab={k+1:m for k,m in enumerate(MON)},sid='lp2',r=3,
      overlays=[(mm(E8_B,3),'#d2475b','m3','6 4'),(mm(E8_B,5),'#1b9e5a','m5','')])
S.append(learn('Learn · 5B','Five-moving means and lost points',
  '<h4>Five-moving mean</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>the mean of the value and the <b>two on each side</b></li>'
  '<li>the first two and last two values get no smoothed value</li><li>more points in the mean → <b>smoother</b> plot, but more points lost</li>'
  '<li><i>N</i> values, <i>n</i>-moving mean: <b><i>N</i> − (<i>n</i> − 1)</b> smoothed values</li></ul>',
  Wd(560,L9)+'<div style="font-size:14px;text-align:center"><span style="color:#1f4fb0">● raw data</span> &nbsp; <span style="color:#d2475b">■ 3-moving mean</span> &nbsp; <span style="color:#1b9e5a">■ 5-moving mean</span></div>',
  'Five-mean smoothing shows no clear trend, although the raw data suggest an increase.',f'{CAM}, 5B pp. 268–270 (plot: Example 8)',
  frags='<span class="frag" data-show="#lp2|m3"></span><span class="frag" data-show="#lp2|m5"></span>',
  cards=(kcard('Five-mean',F('smoothed <i>y</i><sub>3</sub> = ',FR(['<i>y</i><sub>1</sub> + … + <i>y</i><sub>5</sub>'],['5']))),kcard('Lost points','(<i>n</i> − 1) ÷ 2 at each end'))))

# ================= WE7 / YT Edrolo 4B WE1
S.append(qslide('we','Worked example 7 · 5B','Three- and five-moving mean smoothing',
  '<div style="font-size:20px">The table below gives the temperature (°C) recorded at a weather station at 9.00 a.m. each day for a week.<div style="margin:12px 0">'
  +htab([('Day',E7_D),('Temperature',E7_T)],16,'e7t')+'</div>'+plist([('a','Calculate the three-moving mean smoothed temperature for Tuesday.'),('b','Calculate the five-moving mean smoothed temperature for Thursday.')])+'</div>',
  [('a · window','the three temperatures centred on Tuesday: 18.1, 24.8, 26.4','data-hi="#e7t|'+win(1,(0,1,2))+'|hy"'),
   fx('a · mean','Mean',F(FR([V('y₁','18.1'),' + ',V('y₂','24.8'),' + ',V('y₃','26.4')],['3'])),'23.1'),
   ('b · window','the five temperatures centred on Thursday: 24.8, 26.4, 13.9, 12.7, 14.2','data-hi="#e7t|'+win(1,(1,2,3,4,5))+'|hb"'),
   fx('b · mean','Mean',F(FR(['24.8 + 26.4 + 13.9 + 12.7 + 14.2'],['5'])),'18.4')],
  '',f'{CAM} · Example 7 (pp. 268–269)',video='Cambridge GO · Example 7 (5B Resources)',cmd=('Calculate',None,'window centred on the day → mean'),
  parts=[('a','The three-moving mean smoothed temperature for Tuesday is <b>23.1 °C</b>.'),('b','The five-moving mean smoothed temperature for Thursday is <b>18.4 °C</b>.')]))
S[-1]=S[-1].replace('<section class="slide T we mp"','<section class="slide T we mp sm"',1)
r3=mm(WE1_R,3); r5=mm(WE1_R,5)
S.append(qslide('yt','You try · Edrolo 4B WE1','Three- and five-mean smoothing',
  '<div style="font-size:18px">The following table shows the daily <em class="v">rainfall</em> in Dunedin for a week.<div style="margin:10px 0">'
  +htab([('day',WE1_DAY),('rainfall (mm)',WE1_R),('three-mean smoothed rainfall',['–' if v is None else B('y3',f'{v:.1f}') for v in r3]),
         ('five-mean smoothed rainfall',['–' if v is None else B('y5',f'{v:.1f}') for v in r5])],16,'w1t')+'</div>'
  +plist([('a','Find the three-mean smoothed rainfall for Wednesday, correct to one decimal place.'),('b','Find the three-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.'),
          ('c','Find the five-mean smoothed rainfall for Wednesday.'),('d','Find the five-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.')])+'</div>',
  [('a','Wednesday and its neighbours: 3, 5, 5 → (3 + 5 + 5) ÷ 3 = 4.333…','data-hi="#w1t|'+win(1,(1,2,3))+'|hy"'),
   ('b','slide the window: Tue (2+3+5)÷3 = 3.3, Wed 4.3, Thu 3.7, Fri 2.0, Sat 1.0 (CAS spreadsheet)','data-fill="y3"'),
   ('c','2, 3, 5, 5, 1 → (2 + 3 + 5 + 5 + 1) ÷ 5 = 3.2','data-hi="#w1t|'+win(1,(0,1,2,3,4))+'|hb"'),
   ('d','Wed 3.2, Thu (3+5+5+1+0)÷5 = 2.8, Fri 2.6','data-fill="y5"')],
  '',f'{EDR} · 4B Worked example 1 (pp. 234–238)',cmd=('Find',None,'window → mean, one place at a time'),
  parts=[('a','<b>4.3 mm</b>'),('b','three-mean: – , 3.3, 4.3, 3.7, 2.0, 1.0, –'),('c','<b>3.2 mm</b>'),('d','five-mean: – , – , 3.2, 2.8, 2.6, – , –')]))
S[-1]=S[-1].replace('<section class="slide T yt mp"','<section class="slide T yt mp sm"',1)

# ================= WE8 / YT Edrolo 4B WE3
b3=mm(E8_B,3); b5=mm(E8_B,5)
E8F=ts(E8_B,yr=(0,25),yt=5,xl='',yl='births',W=520,H=190,fs=11,xlab={k+1:m for k,m in enumerate(MON)},sid='e8f',r=3,
       overlays=[(b3,'#d2475b','m3','6 4'),(b5,'#1b9e5a','m5','')])
S.append(qslide('we','Worked example 8 · 5B','Smoothing a whole time series',
  ('<div style="font-size:18px">The following table gives the number of births per month over a calendar year in a country hospital. Use the three-moving mean and the five-moving mean methods, rounded to one decimal place, to complete the table.</div>',
   vtab([('Month',MON),('Number of births',E8_B),('3-moving mean',['–' if v is None else B('e3',f1(v)) for v in b3]),('5-moving mean',['–' if v is None else B('e5',f1(v)) for v in b5])],15,'e8t'),''),
  [('3-mean, first','February: (10 + 12 + 6) ÷ 3 = 9.3','data-hi="#e8t|'+win(1,(0,1,2))+'|hy"'),
   ('3-mean, slide','March: (12 + 6 + 5) ÷ 3 = 7.7 … November: (10 + 8 + 15) ÷ 3 = 11.0','data-fill="e3"'),
   ('5-mean, first','March: (10 + 12 + 6 + 5 + 22) ÷ 5 = 11.0','data-hi="#e8t|'+win(1,(0,1,2,3,4))+'|hb"'),
   ('5-mean, slide','April: 12.6 … October: (7 + 9 + 10 + 8 + 15) ÷ 5 = 9.8','data-fill="e5"'),
   ('Plot','the smoothed values at the centre of each window','data-show="#e8f|m3,m5"')],
  'Table complete. The five-moving mean shows <b>no clear trend</b>, although the raw data suggest an increase.',f'{CAM} · Example 8 (pp. 269–270)',
  video='Cambridge GO · Example 8 (5B Resources)',cmd=('complete',None,'slide the window one month at a time'),made=Wd(440,E8F)))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
W3F=ts(WE3_T,yr=(50,120),yt=10,xl='day',yl='time taken (s)',W=520,H=200,fs=12,xr=(0,14),sid='w3f',r=3,overlays=[(WE3_S,'#d2475b','m5','')],
       tls=[((3,102),(12,83),'t1')])
S.append(qslide('yt','You try · Edrolo 4B WE3','Plotting smoothed values',
  ('<div style="font-size:16px">Tobias wants to get faster at solving his Rubik’s Cube. He solves it once a day and records the <em class="v">time taken</em> in seconds. The data taken over two weeks is shown in the following table. Tobias has also calculated the five-mean smoothed values for the data set, correct to one decimal place.</div>'
   +'<div style="margin:6px 0">'+htab([('day',list(range(1,15))),('time taken (s)',WE3_T),('five-mean smoothed time taken (s)',[f1(v) for v in WE3_S])],11,'w3t')+'</div>'
   +'<div style="font-size:16px">Tobias has constructed the following graph to display the <em class="v">time taken</em>.</div>',
   Wd(420,W3F),
   plist([('a','Plot the five-mean smoothed values onto the same graph.'),('b','What, if any, trend can be seen from the five-mean smoothed data?')])),
  [('a','no values for days 1, 2, 13, 14; plot days 3–12 and join left to right','data-show="#w3f|m5"'),
   ('b','the smoothed values gradually decrease from left to right','data-show="#w3f|t1"')],
  '',f'{EDR} · 4B Worked example 3 (pp. 243–245; graph redrawn)',cmd=('Plot',None,'centre of each window'),
  parts=[('a','Five-mean smoothed values plotted for days 3–12 and joined.'),('b','The five-mean smoothed data shows a <b>decreasing trend</b> in <em>time taken</em> (s).')]))
S[-1]=S[-1].replace('<section class="slide T yt mp"','<section class="slide T yt mp sm"',1)

# ================= CAS
C={c['id']:c for c in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills']}['moving-means']
S.append(cas('CAS · 5B','Moving means in a spreadsheet',
  '<p style="font-size:20px">Use a spreadsheet to find the three-moving mean smoothed number of births for each month (Example 8 data).</p>'
  +htab([('month',list(range(1,13))),('births',E8_B)],13)
  +'<div style="margin-top:14px;font-size:17px">Column A = month, column B = births, C2: =(b1+b2+b3)/3, copied down to C11.</div>',
  C['ti'],C['classpad'],'C2 … C11: 9.3, 7.7, 11.0, 15.0, 17.7, 12.7, 9.7, 8.7, 9.0, 11.0 (C1 and C12 stay blank).',
  f'{CAM} · Example 8 data · Steps: CAS guide (planner; from {EDR} 4B WE1)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos'].get('ti',[])[:1]+C['videos'].get('classpad',[])[:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2019 Exam 1 Q16','Show what you know',
  ('The time series plot below shows the <em class="v">monthly rainfall</em> at a weather station, in millimetres, for each <em class="v">month</em> in 2017.',
   Wd(470,ts(RAIN19,yr=(0,300),yt=50,xl='month',yl='monthly rainfall (mm)',W=520,H=230,fs=12,xlab={k+1:m for k,m in enumerate(MON)},r=3,sid='x1f',
             overlays=[(mm(RAIN19,7),'#d2475b','m7','')])),
   'If seven-mean smoothing is used to smooth this time series plot, the number of smoothed data points would be'),
  [('Lost points','seven-mean: (7 − 1) ÷ 2 = 3 lost at each end (Jan–Mar, Oct–Dec)'),
   ('Count','12 − 6 = 6 smoothed points (April to September)','data-show="#x1f|m7"')],
  '6: <b>C</b>.','VCAA 2019 Further Mathematics Exam 1 Q15–16 stem and Q16 (examiner report; plot redrawn, values read off) · Edrolo General Mathematics Units 3&amp;4 4B Q15',
  mc=['3','5','6','8','10'],key='C',dist=[7,11,74,5,2],dis=('B','11% took 12 − 7 = 5: a seven-mean loses 3 points at EACH end, 6 in total.')))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 1 Q14','Show what you know',
  '<div style="font-size:19px">A garden centre sells garden soil.<br>The table below shows the daily quantity of garden soil sold, in cubic metres, over a one-week period.<div style="margin:12px 0">'
  +htab([('Day',['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),('Quantity (m<sup>3</sup>)',['234','186','','','','346','346'])],16,'x2t')+'</div>'
  'The quantity of garden soil sold on Wednesday, Thursday and Friday is not shown.<br>The five-mean smoothed quantity of garden soil sold on Thursday is 206 m<sup>3</sup>.<br>'
  'The three-mean smoothed quantity of garden soil sold on Thursday, in cubic metres, is</div>',
  [('Five-mean, Thursday','(186 + Wed + Thu + Fri + 346) ÷ 5 = 206','data-hi="#x2t|'+win(1,(1,2,3,4,5))+'|hb"'),
   ('Missing total','Wed + Thu + Fri = 5 × 206 − 186 − 346 = 498'),
   fx('Three-mean, Thursday','smoothed',F(FR(['Wed + Thu + Fri'],['3'])),'498 ÷ 3 = 166','data-hi="#x2t|'+win(1,(2,3,4))+'|hy"')],
  '166 m<sup>3</sup>: <b>B</b>.','VCAA 2021 Further Mathematics Exam 1 Q14 (examiner report) · Edrolo General Mathematics Units 3&amp;4 4B Q17',
  mc=['143','166','206','239','403'],key='B',dist=[8,48,15,25,3]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5B',) and v.get('url')]))
n=assemble(S,'12MAG · L17 · Smoothing with moving means',os.path.join(ROOT,'lessons','5B moving means slides.html'))
print(n-1,'slides')
