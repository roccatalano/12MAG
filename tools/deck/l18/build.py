"""Lesson l18 (5B, centring) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/5B centring slides.html
Run: python3 tools/deck/l18/build.py      Screenshots: python3 tools/deck/l18/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; plots redrawn, values read off the source plots):
- Do Now: VCAA 2026 NHT Exam 1 Q13-14 stem + Q14 (C; NHT: no %; plot redrawn) [replaces the card's VCAA 2023 E1 Q15 = eight-mean WITH centring,
          i.e. today's new content, not retrieval; 2023 E1 Q15 freed] ·
          VCAA 2024 NHT Exam 1 Q11-12 stem + Q12 (E, corrected report Oct 2026; NHT: no %; scatterplot not shown, table given) ·
          VCAA 2025 Exam 2 Q4 stem + Q4c (73% scored the mark; $1 765 353; scatterplot redrawn) ·
          VCAA 2024 Exam 2 Q4 stem + Q4b (24% scored the mark; increasing trend and irregular fluctuations; plot redrawn without Q4a's median crosses).
- APK: VCAA 2020 Further Exam 2 Q4 table + Q4aii (77%; 1.065) = Edrolo U1&2 1E Q12 (adapted by Edrolo: ORIGINAL used).
  Card's Cambridge U1&2 2E checklist #10 is burnt (S3) -> dropped, as in l17.
- Learn: Cambridge U3&4 5B pp. 270-271 (own words); simplified formulas as in Edrolo U3&4 4B theory p. 239.
- Worked examples: Cambridge U3&4 Examples 9, 10, 11 (pp. 271-273). You trys: Edrolo U3&4 4B Worked example 2 a-b, c, d (pp. 240-243).
- CAS: planner/cas-skills.json 'moving-means' (centring steps from Edrolo 4B WE2b, d); data = Cambridge Example 11.
- Exits: Edrolo U3&4 4B Q16 = VCAA 2017 Further Exam 1 Q13-15 stem + Q15 (D, 64%; A 10 B 5 C 10 D 64 E 10; stem's three-week plot not shown: Q15 uses the week-2 table) ·
         4B Q18 = VCAA 2016 Further Exam 2 Q4b (48% full marks, average 1/2; M1 = 132, M2 = 182.5). Original VCAA wording.
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l18')
yid=lambda u:u.split('v=')[1].split('&')[0]
def Wd(px,inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def B(cls,val,ph='&nbsp;'): return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def htab(rows,fs=14,tid='',key='c'):
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'
    for r,(h,cells) in enumerate(rows):
        t+='<tr><th>'+h+'</th>'+''.join(f'<td data-i="{key}{r}_{k}">{v}</td>' for k,v in enumerate(cells))+'</tr>'
    return t+'</table>'
def vtab(cols,fs=14,tid='',key='c'):
    t=f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px"><tr>'+''.join(f'<th>{h}</th>' for h,_ in cols)+'</tr>'
    for k in range(len(cols[0][1])):
        t+='<tr>'+''.join(f'<td data-i="{key}{r}_{k}">{c[k]}</td>' for r,(h,c) in enumerate(cols))+'</tr>'
    return t+'</table>'
def win(r,ks): return ','.join(f'c{r}_{k}' for k in ks)
f1=lambda v:'–' if v is None else f'{v:.1f}'
def g(v): return '–' if v is None else (f'{v:.3f}'.rstrip('0').rstrip('.'))
MONL={k+1:m for k,m in enumerate(MON)}
import re
ylab=lambda svg:re.sub(r'x="15"( y="[^"]*" text-anchor="middle"[^>]*rotate\(-90) 15',r'x="-38"\1 -38',svg.replace('viewBox="0 0 400 200"','viewBox="-52 0 452 200"'))
ylab0=lambda svg:re.sub(r'(text-anchor="end"[^>]*>)(\d+)<',lambda m:m.group(1)+f'{int(m.group(2))*100000:,}'.replace(',',' ')+'<',svg)
MEAN=lambda a,b,res:F(FR([a],[b]),' = '+res)

S=['<style>.kcas .ytf{height:130px!important;padding-top:0!important}.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.tight td,.tight th{padding:2px 6px!important;text-align:center}</style>']
# ================= opening
S.append(title(18,'Moving means with centring',f'{CAM} · 5B Smoothing a time series using moving means','L18',
               flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 12 question','var(--apk)'),
  ('Centring: why and how','',None),('Worked examples 9–11','→ You try',None),('CAS: centred means in a spreadsheet','',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Centring','smoothing over an EVEN number of points puts each mean between two times; centring averages two neighbouring means so the value lines up with a real time'),
  ('Two-mean with centring','mean of (mean of the value and the one before) and (mean of the value and the one after)'),
  ('Four-mean with centring','mean of two four-means: one ending at the value + 1, one starting at the value − 1'),
  ('Lost points','an <i>n</i>-mean with centring (<i>n</i> even) has no value for the first and last <i>n</i> ÷ 2 points')],
  [('Two-mean centred',F('smoothed <i>y</i><sub>2</sub> = ',FR(['<i>y</i><sub>1</sub> + 2<i>y</i><sub>2</sub> + <i>y</i><sub>3</sub>'],['4']))),
   ('Four-mean centred',F('smoothed <i>y</i><sub>3</sub> = ',FR(['<i>y</i><sub>1</sub> + 2<i>y</i><sub>2</sub> + 2<i>y</i><sub>3</sub> + 2<i>y</i><sub>4</sub> + <i>y</i><sub>5</sub>'],['8']))),
   ('Centred mean',F(FR(['mean 1 + mean 2'],['2'])))],
  f'{CAM}, 5B pp. 270–273; simplified forms as in {EDR} 4B p. 239'))

# ================= Do Now 1: VCAA 2026 NHT E1 Q14 (5B)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 NHT Exam 1 Q14','Review of 5B (last lesson)',
  ('The daily <em class="v">closing share price</em>, in dollars, for a sports clothing company over a 10-day period is shown in the graph below.',
   Wd(440,ts(SHARE,yr=(5.4,6.6),yt=0.2,xl='day',yl='closing share price (dollars)',W=400,H=210,fs=15,xr=(0,11),r=4,sid='d1f')),
   'The daily <em class="v">closing share price</em> data for this company, given above, can also be smoothed using three-mean smoothing.<br>On which <em class="v">day</em> is the largest smoothed value obtained?'),
  [('Where to look','the biggest value is day 9 ($6.50): check the three-means that include it','data-hi="#d1f|p7,p8,p9|hy"'),
   ('Day 8','(6.20 + 5.90 + 6.50) ÷ 3 = 6.20'),
   ('Days 9 and 7','day 9: (5.90 + 6.50 + 5.60) ÷ 3 = 6.00; day 7: (6.00 + 6.20 + 5.90) ÷ 3 = 6.03')],
  '<em>day</em> 8: <b>C</b>.','VCAA 2026 NHT General Mathematics Exam 1 Q13–14 stem and Q14 (plot redrawn, values read off; NHT report gives no %)',
  mc=['6','7','8','9'],key='C',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2024 NHT E1 Q12 (4D)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 NHT Exam 1 Q12','Review of 4D',
  '<div style="font-size:17px">The table below shows the birth rate, in number of births per 1000 people, and the average annual income, in dollars per person, for a sample of 12 countries.<div style="margin:8px 0">'
  +htab([('<i>birth rate</i>',[f'{v:.2f}' for v in BIRTH[:6]]),('<i>income</i>',[f'{v:,}'.replace(',','&nbsp;') for v in INCOME[:6]])],13,'d2t')+'<div style="height:4px"></div>'+htab([('<i>birth rate</i>',[f'{v:.2f}' for v in BIRTH[6:]]),('<i>income</i>',[f'{v:,}'.replace(',','&nbsp;') for v in INCOME[6:]])],13,'d2u')+'</div>'
  'Coefficients of determination were calculated for<ul class="bul" style="margin:4px 0 4px 26px"><li><em>birth rate</em> vs <em>income</em> (coefficient 1)</li><li>(<em>birth rate</em>)<sup>2</sup> vs <em>income</em> (coefficient 2)</li><li><em>birth rate</em> vs (<em>income</em>)<sup>2</sup> (coefficient 3)</li></ul>'
  'These coefficients were ranked in order from largest to smallest.<br>The order would be</div>',
  [('CAS','make lists <em>birth rate</em>², <em>income</em>²; LinReg each pair, read <i>r</i>²','data-hi="#d2t|'+win(0,range(6))+','+win(1,range(6))+'|hy"'),
   ('Values','coefficient 1 = 0.789, coefficient 2 = 0.830, coefficient 3 = 0.911'),
   ('Rank','0.911 &gt; 0.830 &gt; 0.789')],
  'coefficient 3, coefficient 2, coefficient 1: <b>E</b>.','VCAA 2024 NHT General Mathematics Exam 1 Q11–12 stem (table; scatterplot not shown) and Q12 (report corrected Oct 2026; NHT report gives no %)',
  mc=['coefficient 1, coefficient 2, coefficient 3','coefficient 2, coefficient 3, coefficient 1','coefficient 2, coefficient 1, coefficient 3','coefficient 3, coefficient 1, coefficient 2','coefficient 3, coefficient 2, coefficient 1'],key='E',stat=('nht',)))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 3: VCAA 2025 E2 Q4c (3B)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q4c','Review of 3B',
  ('The scatterplot below shows the <em class="v">sale price</em> of a home, in dollars, against the distance of the home from the city centre of Melbourne, in kilometres, <em class="v">distance from city centre</em>.<br>The sample consists of three-bedroom homes sold between 2016 and 2018.',
   Wd(400,ylab(ylab0(scat([(x,y/100000) for x,y in HOUSE],(0,16),(0,25),1,5,'distance from city centre (km)','sale price ($)',W=400,H=200,r=4,fs=14,sid='d3s')))),
   'The equation of the least squares line for the data in the scatterplot is<div style="text-align:center"><em>sale price</em> = 1 765 353 – 35 054 × <em>distance from city centre</em></div>The coefficient of determination is 0.0806<br>'
   'c. Use the equation of the least squares line to predict the <em class="v">sale price</em> for a three-bedroom home, located <b>in the city centre of Melbourne</b>, sold between 2016 and 2018. <span class="muted">(1 mark)</span>'),
  [('In the city centre','<em>distance from city centre</em> = 0 km'),
   fx('Substitute','<em>sale price</em>',F('1 765 353 − 35 054 × ',V('distance','0')),'1 765 353')],
  'Predicted <em>sale price</em> = <b>$1 765 353</b>','VCAA 2025 General Mathematics Exam 2 Q4 stem and Q4c (examiner report; scatterplot redrawn, values read off)',
  stat=('mark',73),cmd=('predict',1,'substitute into the equation')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2024 E2 Q4b (5A)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q4b','Review of 5A',
  ('The time series plot below shows the gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, in metres, for each Olympic year, <em class="v">year</em>, from 1952 to 1988.',
   Wd(440,ts(WGOLD,xs=YEARS,yr=(1.60,2.05),yt=0.05,xl='year',yl='Wgold (m)',W=400,H=220,fs=14,xr=(1950,1990),xtick=8,r=4,sid='d4f',tls=[((1952,1.70),(1988,2.03),'t1')])),
   'b. Identify <b>two</b> qualitative features that best describe the time series plot above. <span class="muted">(1 mark)</span>'),
  [('Trend','heights go up over time','data-show="#d4f|t1"'),('Fluctuations','ups and downs that don’t repeat (e.g. 1968): irregular, no seasonality, no outlier','data-hi="#d4f|p4|hy"')],
  '<b>Increasing trend</b> and <b>irregular fluctuations</b>.','VCAA 2024 General Mathematics Exam 2 Q4 stem and Q4b (examiner report; plot redrawn, values read off)',
  stat=('mark',24),cmd=('Identify',1,'name two features')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= APK: VCAA 2020 E2 Q4aii
S.append(qslide('apk','APK · VCAA 2020 Exam 2 Q4aii','Mean with CAS',
  '<div style="font-size:18px">The age, in years, body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 men aged 23 to 25 years are shown in the table below.<div style="margin:8px 0">'
  +htab([('Age (years)',AGE),('Body density (kg/litre)',DENS),('Weight (kg)',WT)],14,'a1t')+'</div>'
  'a. For these 12 men, determine<br>&nbsp;&nbsp;ii. the mean of their body density, in kilograms per litre. <span class="muted">(1 mark)</span></div>',
  [('CAS','body density into a list → One-Variable Statistics','data-hi="#a1t|'+win(1,range(12))+'|hy"'),
   fx('Mean','<i>x̄</i>',F(FR(['sum'],[V('n','12')])),'12.78 ÷ 12 = 1.065')],
  '<i>x̄</i> = <b>1.065</b> kg/litre (no rounding asked: 1.07 was not accepted)',
  'VCAA 2020 Further Mathematics Exam 2 Q4 table and Q4aii (examiner report; original wording; = Edrolo General Mathematics Units 1&amp;2 1E Q12, adapted by Edrolo)',
  stat=('mark',77),cmd=('determine',1,'CAS one-variable stats')))

# ================= Learn 1: why centring (two-mean)
L1=('<div style="font-size:17px">'+vtab([('Day',['Monday','','Tuesday','','Wednesday']),('Temperature',['18.1','','24.8','','26.4']),
      ('Two-moving means',['',B('l1a','(18.1 + 24.8) ÷ 2 = 21.45'),'',B('l1b','(24.8 + 26.4) ÷ 2 = 25.60'),'']),
      ('With centring',['','',B('l1c','(21.45 + 25.60) ÷ 2 = 23.525'),'',''])],17,'l1t')+'</div>')
S.append(learn('Learn · 5B','Why centre? Two-mean smoothing with centring',
  '<h4>Even number of points → centring</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>the mean of an <b>even</b> number of values sits <b>between</b> two times</li>'
  '<li>take the two means either side of the time …</li><li>… and average them: the <b>centred mean</b> lines up with that time</li>'
  '<li>only needed for even smoothing: 2, 4, 6 …</li></ul>',
  Wd(600,L1),'Two-mean centred on Tuesday = (Mon + 2 × Tue + Wed) ÷ 4.',f'{CAM}, 5B pp. 270–271 (data: Example 9)',
  frags='<span class="frag" data-fill="l1a"></span><span class="frag" data-fill="l1b"></span><span class="frag" data-fill="l1c"></span>',
  cards=(kcard('Two-mean centred',F('smoothed <i>y</i><sub>2</sub> = ',FR(['<i>y</i><sub>1</sub> + 2<i>y</i><sub>2</sub> + <i>y</i><sub>3</sub>'],['4']))),)))
# ================= Learn 2: four- and six-mean with centring
c4=mmc(E8_B,4)
L2=ts(E8_B,yr=(0,25),yt=5,xl='month',yl='births',W=560,H=230,fs=12,xlab=MONL,sid='lp2',r=3,overlays=[(c4,'#d2475b','c4','')])
S.append(learn('Learn · 5B','Four- and six-mean smoothing with centring',
  '<h4>Same idea, bigger groups</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>four-mean centred: write down the <b>five</b> values centred on the time</li>'
  '<li>mean 1 = first four, mean 2 = last four, then average</li><li>six-mean centred: <b>seven</b> values, two six-means</li>'
  '<li>an <i>n</i>-mean with centring loses <b><i>n</i> ÷ 2</b> points at each end</li></ul>',
  Wd(560,L2),'Four-mean centred = (y₁ + 2y₂ + 2y₃ + 2y₄ + y₅) ÷ 8: ends count once, middle three twice.',f'{CAM}, 5B pp. 271–273 (plot: Example 11)',
  frags='<span class="frag" data-show="#lp2|c4"></span>',
  cards=(kcard('Four-mean centred',F('smoothed <i>y</i><sub>3</sub> = ',FR(['<i>y</i><sub>1</sub> + 2<i>y</i><sub>2</sub> + 2<i>y</i><sub>3</sub> + 2<i>y</i><sub>4</sub> + <i>y</i><sub>5</sub>'],['8']))),kcard('Lost points','<i>n</i> ÷ 2 at each end'))))

TEMP=htab([('Day',E7_D),('Temperature',E7_T)],15,'TID')
# ================= WE9 / YT WE2a-b
S.append(qslide('we','Worked example 9 · 5B','Two-moving mean smoothing with centring',
  '<div style="font-size:20px">The temperatures (°C) recorded at a weather station at 9 a.m. each day for a week are displayed in the table.<div style="margin:12px 0">'
  +TEMP.replace('TID','e9t')+'</div>Calculate the two-moving mean smoothed temperature with centring for Tuesday.</div>',
  [('Three values','centred on Tuesday: 18.1, 24.8, 26.4','data-hi="#e9t|'+win(1,(0,1,2))+'|hy"'),
   ('Mean 1','(18.1 + 24.8) ÷ 2 = 21.45'),('Mean 2','(24.8 + 26.4) ÷ 2 = 25.60'),
   fx('Centred','Centred mean',F(FR([V('mean 1','21.45'),' + ',V('mean 2','25.60')],['2'])),'23.525')],
  'The two-moving mean smoothed temperature for Tuesday is <b>23.5 °C</b>.',f'{CAM} · Example 9 (p. 271)',video='Cambridge GO · Example 9 (5B Resources)',
  cmd=('Calculate',None,'mean 1, mean 2, then average')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
DIST=lambda tid,extra=():htab([('month',MON),('distance run (km)',WE2_D)]+list(extra),13,tid)
DISTV=lambda tid,extra=():vtab([('month',MON),('distance run (km)',WE2_D)]+list(extra),13,tid)
S.append(qslide('yt','You try · Edrolo 4B WE2a–b','Two-mean smoothing with centring',
  '<div style="font-size:18px">Amelia recorded the distance, in km, she ran each month for a year.<div style="margin:10px 0">'
  +DISTV('w2t',[('two-mean smoothed distance run with centring (km)',['–' if v is None else B('t2',f1(v)) for v in WE2_2])])+'</div>'
  +plist([('a','Find the two-mean smoothed distance run for July.'),('b','Find the two-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.')])+'</div>',
  [('a · values','June, July, August: 35, 36, 28','data-hi="#w2t|'+win(1,(5,6,7))+'|hy"'),
   ('a · means','mean 1 = (35 + 36) ÷ 2 = 35.5; mean 2 = (36 + 28) ÷ 2 = 32'),
   ('a · centred','(35.5 + 32) ÷ 2 = 33.75'),
   ('b','CAS spreadsheet: C2 = (b1 + 2b2 + b3)/4, copied down to C11','data-fill="t2"')],
  '',f'{EDR} · 4B Worked example 2a–b (pp. 240–241)',cmd=('Find',None,'mean 1, mean 2, then average'),
  parts=[('a','<b>33.75 km</b>'),('b','–, 43.8, 41.5, 39.5, 37.5, 35.8, 33.8, 30.8, 29.5, 30.5, 34.8, –')]))
S[-1]=S[-1].replace('<section class="slide T yt mp"','<section class="slide T yt mp sm"',1)
# ================= WE10 / YT WE2c
S.append(qslide('we','Worked example 10 · 5B','Four- and six-moving mean smoothing with centring',
  '<div style="font-size:20px">The table below gives the temperature (°C) recorded at a weather station at 9.00 a.m. each day for a week.<div style="margin:12px 0">'
  +TEMP.replace('TID','e10t')+'</div>'+plist([('a','Calculate the four-moving mean smoothed temperature with centring for Thursday.'),('b','Calculate the six-moving mean smoothed temperature with centring for Thursday.')])+'</div>',
  [('a · five values','24.8, 26.4, 13.9, 12.7, 14.2','data-hi="#e10t|'+win(1,(1,2,3,4,5))+'|hy"'),
   ('a · means','mean 1 = (24.8 + 26.4 + 13.9 + 12.7) ÷ 4 = 19.45; mean 2 = (26.4 + 13.9 + 12.7 + 14.2) ÷ 4 = 16.8'),
   ('a · centred','(19.45 + 16.8) ÷ 2 = 18.125'),
   ('b · seven values','all seven days, Monday to Sunday','data-hi="#e10t|'+win(1,range(7))+'|hb"'),
   ('b · means','mean 1 = first six ÷ 6 = 18.35; mean 2 = last six ÷ 6 = 19.483…'),
   ('b · centred','(18.35 + 19.483) ÷ 2 = 18.917')],
  '',f'{CAM} · Example 10 (pp. 272–273)',video='Cambridge GO · Example 10 (5B Resources)',cmd=('Calculate',None,'n + 1 values → two means → average'),
  parts=[('a','The four-mean smoothed temperature centred on Thursday is <b>18.1 °C</b> (to 1 d.p.).'),('b','The six-mean smoothed temperature centred on Thursday is <b>18.9 °C</b> (to 1 d.p.).')]))
S[-1]=S[-1].replace('<section class="slide T we mp"','<section class="slide T we mp sm"',1)
S.append(qslide('yt','You try · Edrolo 4B WE2c','Four-mean smoothing with centring',
  '<div style="font-size:19px">Amelia recorded the distance, in km, she ran each month for a year.<div style="margin:12px 0">'+DIST('w3t')+'</div>'
  +plist([('c','Find the four-mean smoothed distance run for July.')])+'</div>',
  [('Five values','May to September: 37, 35, 36, 28, 31','data-hi="#w3t|'+win(1,(4,5,6,7,8))+'|hy"'),
   ('Mean 1','(37 + 35 + 36 + 28) ÷ 4 = 34'),('Mean 2','(35 + 36 + 28 + 31) ÷ 4 = 32.5'),
   fx('Centred','Centred mean',F(FR([V('mean 1','34'),' + ',V('mean 2','32.5')],['2'])),'33.25')],
  'The four-mean smoothed distance run for July is <b>33.25 km</b>.',f'{EDR} · 4B Worked example 2c (p. 242)',cmd=('Find',None,'five values → two means → average')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)
# ================= WE11 / YT WE2d
m4=[None if k<0 else None for k in range(12)]
NC=[None,'8.25','11.25','12.75','14.5','15','11.75','9.75','8.5','10.5',None,None]
S.append(qslide('we','Worked example 11 · 5B','Smoothing a whole time series: four-mean with centring',
  ('<div style="font-size:18px">The following table gives the number of births per month over a calendar year in a country hospital. Use the four moving mean with centring method to complete the table.</div>',
   vtab([('Month',MON),('Number of births',E8_B),('4-moving mean (between months)',['' if v is None else B('n4',v) for v in NC]),('4-moving mean with centring',['–' if v is None else B('c4',g(v)) for v in c4])],14,'e11t'),''),
  [('First four-mean','(10 + 12 + 6 + 5) ÷ 4 = 8.25 (between Feb and Mar)','data-hi="#e11t|'+win(1,(0,1,2,3))+'|hy"'),
   ('Slide','next four-means: 11.25, 12.75 … 10.5 (the last is Sep–Dec)','data-fill="n4"'),
   ('Centre','average neighbouring pairs: March (8.25 + 11.25) ÷ 2 = 9.75, April (11.25 + 12.75) ÷ 2 = 12 …','data-fill="c4"'),
   ('Lost points','no value for Jan, Feb, Nov, Dec (4 ÷ 2 = 2 at each end)')],
  'Table complete: March 9.75 … October 9.5.',f'{CAM} · Example 11 (p. 273)',video='Cambridge GO · Example 11 (5B Resources)',cmd=('complete',None,'four-means, then centre')))
S[-1]=S[-1].replace('<section class="slide T we"','<section class="slide T we sm"',1)
S.append(qslide('yt','You try · Edrolo 4B WE2d','Four-mean smoothing with centring: whole series',
  '<div style="font-size:18px">Amelia recorded the distance, in km, she ran each month for a year.<div style="margin:10px 0">'
  +DISTV('w4t',[('four-mean smoothed distance run with centring (km)',['–' if v is None else B('t4',f1(v)) for v in WE2_4])])+'</div>'
  +plist([('d','Find the four-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.')])+'</div>',
  [('First value','March: (42 + 2×47 + 2×39 + 2×41 + 37) ÷ 8 = 41.625','data-hi="#w4t|'+win(1,(0,1,2,3,4))+'|hy"'),
   ('CAS','C3 = (b1 + 2b2 + 2b3 + 2b4 + b5)/8, copied down to C10','data-fill="t4"')],
  'four-mean centred: –, –, 41.6, 39.5, 37.6, 35.6, 33.3, 31.6, 30.6, 32.1, –, –',f'{EDR} · 4B Worked example 2d (pp. 242–243)',cmd=('Find',None,'CAS spreadsheet, round at the end')))
S[-1]=S[-1].replace('<section class="slide T yt"','<section class="slide T yt sm"',1)

# ================= CAS
C={c['id']:c for c in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills']}['moving-means']
S.append(cas('CAS · 5B','Centred moving means in a spreadsheet',
  '<p style="font-size:20px">Use a spreadsheet to find the four-mean smoothed number of births with centring for each month (Example 11 data).</p>'
  +htab([('month',list(range(1,13))),('births',E8_B)],13)
  +'<div style="margin-top:14px;font-size:17px">Column A = month, column B = births, C3: =(b1+2b2+2b3+2b4+b5)/8, copied down to C10.</div>',
  [C['ti'][0],C['ti'][4],C['ti'][2]],[C['classpad'][0],C['classpad'][4],C['classpad'][2]],'C3 … C10: 9.75, 12, 13.625, 14.75, 13.375, 10.75, 9.125, 9.5 (C1, C2, C11, C12 stay blank).',
  f'{CAM} · Example 11 data · Steps: CAS guide (planner; from {EDR} 4B WE2)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos'].get('ti',[])[:1]+C['videos'].get('classpad',[])[:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2017 Exam 1 Q15','Show what you know',
  '<div style="font-size:19px">The wind speed at a city location is measured throughout the day.<br>The table below shows the daily maximum wind speed, in kilometres per hour, for the days in week 2.<div style="margin:12px 0">'
  +htab([('Day',WIND_D),('Maximum wind speed (km/h)',WIND)],16,'x1t')+'</div>A four-point moving mean with centring is used to smooth the time series data above.<br>The smoothed maximum wind speed, in kilometres per hour, for day 11 is closest to</div>',
  [('Five values','days 9 to 13: 22, 19, 22, 43, 37','data-hi="#x1t|'+win(1,(1,2,3,4,5))+'|hy"'),
   ('Means','mean 1 = (22 + 19 + 22 + 43) ÷ 4 = 26.5; mean 2 = (19 + 22 + 43 + 37) ÷ 4 = 30.25'),
   ('Centred','(26.5 + 30.25) ÷ 2 = 28.375')],
  '28: <b>D</b>.','VCAA 2017 Further Mathematics Exam 1 Q13–15 stem (plot not shown) and Q15 (examiner report) · Edrolo General Mathematics Units 3&amp;4 4B Q16',
  mc=['22','24','26','28','30'],key='D',dist=[10,5,10,64,10],dis=('A, C, E','10% each: no centring (26.5 or 30.25 → C or E) or the plain value for day 11 (A). Centre with mean 1 AND mean 2.')))
c2=mmc(RAIN16,2)
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2016 Exam 2 Q4b','Show what you know',
  ('<div style="font-size:16px">The maximum daily rainfall each month was also recorded at the weather station.<br>The table below shows the maximum daily rainfall each month for a period of one year.<div style="margin:6px 0">'
   +htab([('Month',['Jan.','Feb.','Mar.','Apr.','May','June','July','Aug.','Sep.','Oct.','Nov.','Dec.']),('Month number',list(range(1,13))),('Maximum daily rainfall (mm)',RAIN16)],12,'x2t')
   +'</div>The data in the table has been used to plot maximum daily rainfall against month number in the time series plot below.</div>',
   Wd(400,ts(RAIN16,yr=(0,250),yt=50,xl='month number',yl='maximum daily rainfall (mm)',W=400,H=190,fs=14,xr=(0,13),xtick=2,r=4,sid='x2f',overlays=[(c2,'#d2475b','c2','6 4')])),
   '<div style="font-size:16px">b. Two-mean smoothing with centring has been used to smooth the time series plot above.<br>The smoothed values are marked with crosses (×).<br>Using the data given in the table, <b>show</b> that the two-mean smoothed rainfall centred on October is 157.25 mm. <span class="muted">(2 marks)</span></div>'),
  [('Three values','September, October, November: 124, 140, 225','data-hi="#x2t|'+win(2,(8,9,10))+'|hy"'),
   ('Means','M1 = (124 + 140) ÷ 2 = 132; M2 = (140 + 225) ÷ 2 = 182.5'),
   ('Centred','(132 + 182.5) ÷ 2 = 157.25','data-show="#x2f|c2"')],
  '(132 + 182.5) ÷ 2 = <b>157.25 mm</b>, as required.','VCAA 2016 Further Mathematics Exam 2 Q4 (maximum rainfall part) and Q4b (examiner report: use the table, not the graph; plot redrawn; smoothed values drawn as squares) · Edrolo General Mathematics Units 3&amp;4 4B Q18',
  stat=('mark',48),cmd=('show',2,'both means, then the centred mean')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 5 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('5B',) and v.get('url')]))
n=assemble(S,'12MAG · L18 · Moving means with centring',os.path.join(ROOT,'lessons','5B centring slides.html'))
print(n-1,'slides')
