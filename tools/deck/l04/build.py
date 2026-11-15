"""Lesson l04 (2C) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2C slides.html
Run: python3 tools/deck/l04/build.py      Screenshots: python3 tools/deck/l04/shoot.py

Sources (all read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn from the source figures, values read off them):
- Do Now: VCAA 2026 NHT Exam 1 Q5 (answer D; NHT report gives no %) · VCAA 2024 Exam 1 Q6 (report: C 53%, A 17, B 19, D 11)
          VCAA 2023 Exam 2 Q1ci (report: 88% scored 1) · VCAA 2023 Exam 2 Q2bi (report: 87% scored 1)
- APK (planner card): Cambridge U1&2 Ch 2 skills checklist 2I #16 ('See Example 27 and Example 28'): its Now try this 27 (p. 114; Example 27
  itself is the same life-expectancy plot as U3&4 Example 10, so the Now try is used). Solution written for 12MAG in the Example 27 pattern.
  VCAA 2019 Further Exam 2 Core Q2aii (= Edrolo U1&2 1H Q16; report: 87% scored 1, answer 10)
  VCAA 2021 Further Exam 1 Core Q4 (= Edrolo U1&2 1H Q17, 'adapted'; original VCAA wording used; report: B 60%, A 4, C 10, D 11, E 15)
- Learn: Cambridge Units 3&4 2C pp. 123-126
- Worked examples: Cambridge Units 3&4 Examples 9-12 (pp. 123-127). Reports set out in SOCS order (Shape, Outliers, Centre, Spread), then the conclusion.
- You try (planner card): Edrolo Units 3&4 2B WE2 (pp. 121-122, parallel dot plots), WE1 (pp. 120-121, back-to-back stem plot),
  WE3 (pp. 122-123, parallel boxplots), WE4 (p. 124, report).
- Exits: Edrolo U3&4 2B Q11 = VCAA 2016 Further Exam 1 Core Q8 (report: C 45%, A 4, B 21, D 4, E 25)
         Edrolo U3&4 2B Q12 = VCAA 2019 Further Exam 2 Core Q3 (report: 36% scored 2/2, average 1.0; original has vertical boxplots, redrawn horizontally)
         Edrolo U3&4 2B Q13 = VCAA 2017 Further Exam 2 Core Q2e (report: 43% scored 2/2, average 1)
- CAS: planner/cas-skills.json 'parallel-boxplots'.
- Videos: the 2C MaffsGuru link in videos.json is still blank (draft), so the videos slide has blank cards.
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
import tpl as TPL
from figs import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'

def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:10px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'):
    return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def table(head,rows,fs=19,rid='',extra=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td{" class=\"l\"" if j==0 else ""}><span data-i="{i}">{c}</span></td>' for j,c in enumerate(r))+'</tr>' for i,r in enumerate(rows))
    return f'<table class="t"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}"><tr>{th}</tr>{tr}</table>'
SOC=[('S','Shape','#2f6fdf'),('O','Outliers','#c0632b'),('C','Centre','#1f9e74'),('S','Spread','#7b3fbf')]
def csocs(pre,lines,concl,fs=17):
    """SOCS comparison template: lines = [shape, outliers, centre, spread] texts (None = skip that letter), filled by data-fill="<pre>1..4"; conclusion <pre>5."""
    rows=''
    for k,((l,n,c),t) in enumerate(zip(SOC,lines)):
        if t is None: continue
        rows+=f'<div class="socsr"><span class="socsl" style="background:{c}">{l}</span><span class="socsn" style="color:{c}">{n}</span><span class="socst">{B(pre+str(k+1),t,"compare the groups")}</span></div>'
    rows+=f'<div class="socsr"><span class="socsl" style="background:#333">✓</span><span class="socsn">Conclude</span><span class="socst">{B(pre+"5",concl,"associated or not")}</span></div>'
    return f'<div class="socs report" style="font-size:{fs}px">{rows}</div>'
def W(px,inner): return f'<div style="width:{px}px;max-width:100%">{inner}</div>'

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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l04')
yid=lambda u:u.split('v=')[1].split('&')[0]

S=[BBCSS+'<style>.T .mc>div{padding-right:54px}.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.ex .L .q table.t td,.ex .L .q table.t th{padding:2px 6px}</style>']
# ================= opening
S.append(title(4,'Investigating the association between a numerical and a categorical variable',
  f'{CAM} · 2C Investigating the association between a numerical and a categorical variable','L04',
  flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC,[('CFAT 1.2.1','· 2A–2B, about 20 minutes','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 skills','var(--apk)'),
  ('Comparing groups: SOCS','',None),('Parallel dot plots','→ WE 9',None),('Back-to-back stem plots','→ WE 10',None),
  ('Parallel boxplots','→ WE 11, 12',None),('CAS: parallel boxplots','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mini_b=W(230,pbox([('A',(2,4,5,7,9),[]),('B',(4,6,8,9,10),[])],0,12,2,'',W=300,rowH=34,fs=13,lab=30,sw=1.8))
mini_d=W(230,pdot([('A',[2,3,3,4,5]),('B',[4,5,5,6,7])],1,8,1,'',W=300,gh=44,fs=13,r=5))
mini_s=bbstem('kst',[1,2,3],[['5','2'],['8','1'],['0']],[['4'],['3','6','9'],['2','7']],'A','B',fs=13)
S.append(keys([
  ('Parallel dot plots','a dot plot for each group, one above the other, on the same scale',mini_d),
  ('Back-to-back stem plot','two groups share one stem: leaves to the left for one group, to the right for the other',mini_s),
  ('Parallel boxplots','a boxplot for each group on the same scale (any number of groups)',mini_b),
  ('Association (numerical + categorical)','the distribution of the numerical variable (RV) changes from group to group of the categorical variable (EV)')],
  [('Compare with SOCS',F('Shape · Outliers · Centre (median) · Spread (IQR)'),'quote the value for EVERY group'),
   ('Interquartile range',F('IQR = Q<sub>3</sub> − Q<sub>1</sub>')),
   ('Outlier fences',F('x &lt; Q<sub>1</sub> − 1.5 × IQR → outlier · x &gt; Q<sub>3</sub> + 1.5 × IQR → outlier'))],
  f'{CAM}, 2C pp. 123–126'))

# ================= Do Now 1: VCAA 2026 NHT E1 Q5 (2B)
CD=table(['Gender','Likes<br>only cats','Likes<br>only dogs','Likes both<br>cats and dogs','Likes neither<br>cats nor dogs','Total'],
         [['male','5','8','15','4','32'],['female','11','9','14','4','38']],fs=18,rid='d1t')
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 NHT Exam 1 Q5','Review of 2B',
  G('In a survey, 70 adults were asked their opinions about cats and dogs.<br>The results are shown in the table below.',CD,'Based on the survey, which one of the following is correct?'),
  [('Test D','males who like dogs: only dogs + both = 8 + 15 = 23 · 23 ÷ 32 × 100 = 71.875% ✓','data-hi="#d1t|0|hy"'),
   ('Check A–C','A: females who like cats = (11 + 14) ÷ 38 = 65.8% ✗ · B: 5 ÷ 16 = 31.25% ✗ · C: 4 ÷ 8 = 50% ✗')],
  'Of the males surveyed, 71.875% like dogs: <b>D</b>.','VCAA 2026 (NHT) General Mathematics Exam 1 Q5 (examiner report: answer only, no %)',
  mc=['Of the females surveyed, 78.125% like cats.','Of those adults who like only cats, 15.625% are male.','Of those adults who like neither cats nor dogs, 12.5% are male.','Of the males surveyed, 71.875% like dogs.'],key='D'))
# ================= Do Now 2: VCAA 2024 E1 Q6 (1G)
FN=table(['Minimum','First quartile','Median','Third quartile','Maximum'],[['2','5','11','48','613']],fs=20,rid='d2t')
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q6','Review of 1G',
  G('More than 11 000 athletes from more than 200 countries competed in the Tokyo Summer Olympic Games.<br>An analysis of the number of athletes per country produced the following five-number summary.',FN,
    'The smallest number of athletes per country that would display as an outlier on a boxplot of this data is'),
  [fx('IQR',' IQR',F(V('Q₃','48'),' − ',V('Q₁','5')),'43'),
   fx('Upper fence',' UF',F(V('Q₃','48'),' + 1.5 × ',V('IQR','43')),'112.5'),
   ('Smallest outlier','a whole number of athletes above 112.5 → 113')],
  'The smallest outlier would be <b>113</b>.','VCAA 2024 General Mathematics Exam 1 Q6 (examiner report)',stat=('mc',53),
  mc=['49','112','113','613'],key='C',dist=[17,19,53,11],dis=('B','19% chose this: 112.5 rounded down. 112 is below the upper fence, so it is not an outlier.')))
# ================= Do Now 3: VCAA 2023 E2 Q1ci (2A)
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q1ci','Review of 2A',
  'Data was collected to investigate the use of electronic images to automate the sizing of oysters for sale.<br>When a least squares line is used to model the association between oyster weight and volume, the equation is:'
  '<p style="text-align:center;font-size:26px;margin:22px 0"><em class="v">volume</em> = 0.780 + 0.953 × <em class="v">weight</em></p>Name the response variable in this equation. <span class="muted">(1 mark)</span>',
  [('Left-hand side','the response variable is the one being predicted: it sits on the left of the equation.')],
  'The response variable is <em class="v">volume</em>.','VCAA 2023 General Mathematics Exam 2 Q1ci (examiner report)',stat=('mark',88),cmd=('Name',1,'one variable')))
# ================= Do Now 4: VCAA 2023 E2 Q2bi (2B)
OY=table(['Oyster size','Farm A','Farm B'],[['small','42','114'],['medium','124','160'],['large','44','46'],['<b>Total</b>','<b>210</b>','<b>320</b>']],fs=20,rid='d4t')
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q2bi','Review of 2B',
  G('An oyster farmer has two farms, A and B.<br>She takes a random sample of oysters from each of the farms and has the oysters classified as small, medium or large.<br>The number of oysters of each size is displayed in the two-way table below.',
    '<div><div style="font-weight:700;font-size:16px">Table 3</div>'+OY+'</div>','Calculate the percentage of the total number of oysters graded as ‘large’ in this investigation.<br>Round the percentage to the nearest whole number. <span class="muted">(1 mark)</span>'),
  [('Large','44 + 46 = 90','data-hi="#d4t|2|hy"'),('Total','210 + 320 = 530','data-hi="#d4t|3|hb"'),
   fx('Percentage','large',F(FR([V('large','90')],[V('total','530')]),' × 100%'),'16.98…%')],
  '<b>17%</b> of the oysters were graded as ‘large’.','VCAA 2023 General Mathematics Exam 2 Q2bi (examiner report)',stat=('mark',87),cmd=('Calculate',1,'a %, nearest whole number')))

# ================= APK 1: Cambridge U1&2 Now try this 27 (checklist 2I #16)
st,l,r=NT27
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2I #16','Comparing two groups with a stem plot',
  G('The following back-to-back stem plot displays the distributions of the number of hours per week spent relaxing by a group of 17 males and 16 females.',
    '<div>'+bbstem('a1s',st,l,r,'Males','Females','1|2 = 21 hours','1|6 = 16 hours','Number of hours per week spent relaxing',fs=22)+
    '<div style="display:flex;justify-content:space-around;font-size:18px;margin-top:6px"><span>M = 30 hours<br>IQR = 14.5 hours</span><span>M = 24.5 hours<br>IQR = 19 hours</span></div></div>',
    'Use the back-to-back stem plot and the summary statistics provided to compare these distributions in terms of centre and spread, and draw an appropriate conclusion.'),
  [('Centre','compare the medians: males 30 hours, females 24.5 hours'),('Spread','compare the IQRs: males 14.5 hours, females 19 hours'),
   ('ANS','The median time spent relaxing for males (M = 30 hours) was higher than for females (M = 24.5 hours). The spread for males (IQR = 14.5 hours) was lower than for females (IQR = 19 hours). In conclusion, the males spent more time relaxing than the females, and their times were less variable.')],
  '',f'{CAM12} · 2I Now try this 27 (p. 114), for skills checklist 2I #16 · solution written for 12MAG in the Example 27 pattern',cmd=('compare',None,'centre and spread, then a conclusion')))
# ================= APK 2: VCAA 2019 E2 Q2aii
S.append(qslide('apk','APK · Year 11 · VCAA 2019 Exam 2 Q2aii','Reading parallel boxplots',
  G('The parallel boxplots below show the <em class="v">maximum daily temperature</em> and <em class="v">minimum daily temperature</em>, in degrees Celsius, for 30 days in November 2017.',
    W(720,pbox([('',V19Q2[0][1],V19Q2[0][2])],6,30,2,'maximum daily temperature (°C)',W=760,rowH=62,fs=17,lab=20).replace('<g data-i="0"','<g data-i="max"')+
          pbox([('',V19Q2[1][1],V19Q2[1][2])],6,30,2,'minimum daily temperature (°C)',W=760,rowH=62,fs=17,lab=20).replace('<g data-i="0"','<g data-i="min"').replace('data-i="0m"','data-i="minm"')),
    'Use the information in the boxplots to complete the following sentence.<br>For November 2017<br>ii. the median value for <em class="v">maximum daily temperature</em> was ☐ °C higher than the median value for <em class="v">minimum daily temperature</em> <span class="muted">(1 mark)</span>'),
  [('Median, maximum','the line inside the top box: 25 °C'),('Median, minimum','the line inside the bottom box: 15 °C'),('Subtract','25 − 15 = 10')],
  'The median <em class="v">maximum daily temperature</em> was <b>10 °C</b> higher.',f'Edrolo General Mathematics Units 1&amp;2 · 1H Q16 · VCAA 2019 Further Mathematics Exam 2 Core Q2aii (examiner report; boxplots redrawn)',stat=('mark',87),cmd=('complete',1,'one number')))
# ================= APK 3: VCAA 2021 E1 Q4
S.append(qslide('apk','APK · Year 11 · VCAA 2021 Exam 1 Q4','Reading parallel boxplots',
  G('The boxplots below show the distribution of the length of fish caught in two different ponds, Pond A and Pond B.',
    W(420,pbox(V21Q4,0,12,0.5,'length',W=600,rowH=56,fs=17,lab=90,ticks=False,grid=True)),
    'Based on the boxplots above, it can be said that'),
  [('Key idea','each whisker and each half of the box holds 25% of the data'),
   ('Test B','Pond B median is to the right of Pond A’s maximum: the top 50% of B are longer than every fish in A ✓','data-hi="#apk3|1m,0w|hy"')],
  '<b>B</b>: 50% of the fish caught in Pond B are longer than all of the fish caught in Pond A.','Edrolo General Mathematics Units 1&amp;2 · 1H Q17 · VCAA 2021 Further Mathematics Exam 1 Core Q4 (examiner report; original wording; boxplots redrawn)',stat=('mc',60),
  mc=['50% of the fish caught in Pond A are the same length as the fish caught in Pond B.','50% of the fish caught in Pond B are longer than all of the fish caught in Pond A.','50% of the fish caught in Pond B are shorter than all of the fish caught in Pond A.',
      '75% of the fish caught in Pond A are shorter than all of the fish caught in Pond B.','75% of the fish caught in Pond B are longer than all of the fish caught in Pond A.'],
  key='B',dist=[4,60,10,11,15],dis=('E','15% chose this: Pond B’s Q<sub>1</sub> is not past the end of Pond A’s top whisker, and that whisker holds the top 25% of Pond A.')))
S[-1]=S[-1].replace('<svg viewBox="0 0 600','<svg id="apk3" viewBox="0 0 600',1).replace('<section class="slide T apk mcslide"','<section class="slide T apk mcslide sm"',1)

# ================= Learn 2C: comparing groups
body=('<div class="row" style="gap:20px;align-items:stretch"><div class="key" style="flex:1"><h4>Numerical RV, categorical EV</h4>'
  '<p style="font-size:20px">Does <em>test score</em> (numerical) depend on <em>attended revision class</em> (yes / no, categorical)? Draw one display per group <b>on the same scale</b>, then compare.</p>'
  '<ul class="bul" style="font-size:19px;line-height:1.55;margin:10px 0 0 24px"><li class="frag">small data sets: <b>parallel dot plots</b> or a <b>back-to-back stem plot</b></li>'
  '<li class="frag">any size, two or more groups: <b>parallel boxplots</b></li></ul></div>'
  '<div class="key" style="flex:1.15"><h4>Compare the groups with SOCS</h4>'
  '<div class="socs report" style="font-size:19px">'+''.join(f'<div class="socsr frag"><span class="socsl" style="background:{c}">{l}</span><span class="socsn" style="color:{c}">{n}</span><span class="socst">{t}</span></div>' for (l,n,c),t in zip(SOC,
   ['symmetric / skewed, for each group (hard to see in small data sets)','any outliers, and where','<b>medians</b>: higher or lower?','<b>IQRs</b>: more or less variable?']))+
  '<div class="socsr frag"><span class="socsl" style="background:#333">✓</span><span class="socsn">Conclude</span><span class="socst">noticeably different → the variables <b>are associated</b>; much the same → <b>no association</b></span></div></div></div></div>'
  '<div class="tip frag" style="margin-top:12px">Quote the value for every group (‘M = 26 before, M = 32 after’). Use medians and IQRs, not means: they are not affected by outliers.</div>')
S.append(TPL._frame('learn','Learn · 2C','Comparing a numerical variable across groups',body,f'{CAM}, 2C pp. 123–125 (SOCS order for 12MAG)',cfu='disc'))

# ================= WE9: Cambridge Example 9 (parallel dot plots)
srt=lambda g:sorted(EX9[g][1])
S.append(qslide('we','Worked example 9 · 2C','Using a parallel dot plot to identify and describe associations',
  G('The parallel dot plots below display the distribution of the number of sit-ups performed by 15 people before and after they had completed a gym program.',
    W(860,pdot([('Number of sit-ups before gym program',EX9[0][1]),('Number of sit-ups after gym program',EX9[1][1])],22,54,2,'',W=640,gh=86,fs=16,r=7).replace('<svg','<svg id="w9d"',1)),
    'Do the parallel dot plots support the contention that the number of sit-ups performed is associated with completing the gym program? Write a brief explanation that compares the distributions.'),
  [('RV and EV','RV: <em>sit-ups</em> (numerical) · EV: <em>gym program</em> (before, after)'),
   ('Centre','15 values: the median is the 8th dot. Before M = 26, after M = 32','data-hi="#w9d|0.7,1.7|hy" data-fill="w93"'),
   ('Spread','Q₁ = 4th, Q₃ = 12th dot. Before IQR = 30 − 24 = 6; after IQR = 36 − 26 = 10','data-hi="#w9d|0.3,0.11,1.3,1.11|hb" data-fill="w94"'),
   ('Conclude','reasonable differences in both median and IQR','data-hi="#w9d||" data-fill="w95"'),
   ('TMPL',csocs('w9',[None,None,'The median number of sit-ups performed after attending the gym program (M = 32) is higher than the median number of sit-ups performed before attending the gym program (M = 26).',
      'The variability in the number of sit-ups has also increased from IQR = 6 to IQR = 10.'],'Thus we can conclude that the number of sit-ups performed is associated with completing the gym program.',fs=16))],
  '',f'{CAM} · Example 9 (pp. 123–124; dot plots redrawn; report in SOCS order)',video='Cambridge GO · Example 9 (2C Resources)',cmd=('Write',None,'compare medians and IQRs, then conclude')))
# ================= You try: Edrolo 2B WE2 (construct parallel dot plots)
g5,g6=YT2
DK=lambda g:pdot_keys(g,12)
S.append(qslide('yt','You try · Edrolo 2B WE2','Constructing parallel dot plots',
  'A grade 5/6 class took a maths test on fractions. The <em class="v">number of marks</em>, by grade, was recorded.'
  '<p style="font-size:24px;margin:16px 0 4px">Grade 5: &nbsp;2 &nbsp;4 &nbsp;5 &nbsp;5 &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;9</p><p style="font-size:24px;margin:0 0 16px">Grade 6: &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;9 &nbsp;9 &nbsp;9 &nbsp;10</p>'+
  plist([('a','Construct parallel dot plots to display this data.'),('b','Which grade has a larger range of <em class="v">number of marks</em>?')]),
  [('Scale','data runs from 2 to 10: two identical axes, 2 to 10, one tick per mark','data-pk="0"'),
   ('Grade 5','a dot for each value, stacking repeats','data-pk="0" data-show="#y2d|'+DK(0)+'"'),
   ('Grade 6','same axis, vertically aligned','data-pk="0" data-show="#y2d|'+DK(1)+'"'),
   ('TMPL',W(520,pdot([('Grade 5',g5[1]),('Grade 6',g6[1])],2,10,1,'number of marks',W=560,gh=92,fs=16,r=7,hid=True).replace('<svg','<svg id="y2d"',1))),
   ('Range','Grade 5: 9 − 2 = 7 marks · Grade 6: 10 − 5 = 5 marks','data-pk="1" data-hi="#y2d|0.0,0.11,1.0,1.11|hy"'),
   ('ANS','<b>b</b> &nbsp;Grade 5 has the larger range.')],
  '',f'{EDR} · 2B Worked example 2 (pp. 121–122)',cmd=('Construct',None,'same scale, one plot per group')))

# ================= WE10: Cambridge Example 10 (back-to-back stem plot)
st,l,r=EX10
S.append(qslide('we','Worked example 10 · 2C','Using a back-to-back stem plot to identify and describe associations',
  G('The back-to-back stem plot below displays the distribution of life expectancy (in years) for the same 13 countries in 1970 and 2010.',
    bbstem('w10s',st,l,r,'1970','2010','2|5 = 52 years','6|7 = 67 years',fs=24),
    'Do the back-to-back stem plots support the contention that life expectancy has changed between these two time periods?'),
  [('RV and EV','RV: <em>life expectancy</em> · EV: <em>year</em> (only two values, so treated as categorical)'),
   ('Centre','13 values: the median is the 7th. 1970: M = 67 · 2010: M = 76','data-hi="#w10s|L3.4,R4.4|hy" data-fill="w103"'),
   ('Spread','quartiles → IQR = 12.5 years (1970), 8 years (2010)','data-hi="#w10s||" data-fill="w104"'),
   ('Conclude','differences in median and IQR are large enough: associated','data-fill="w105"'),
   ('TMPL',csocs('w10',[None,None,'The median life expectancy has increased between 1970 and 2010, from M = 67 years to M = 76 years.',
      'Over the same period life expectancy has also become less variable (IQR in 1970 = 12.5 years; IQR in 2010 = 8 years).'],'There is an association between year and life expectancy.',fs=16))],
  '',f'{CAM} · Example 10 (pp. 124–125; report in SOCS order)',video='Cambridge GO · Example 10 (2C Resources)',cmd=('Do',None,'compare medians and IQRs')))
# ================= You try: Edrolo 2B WE1 (construct back-to-back stem plot)
st,l,r=YT1
allk=lambda side,xs:','.join(f'{side}{i}.{k}' for i,x in enumerate(xs) for k in range(len(x)))
S.append(qslide('yt','You try · Edrolo 2B WE1','Constructing a back-to-back stem plot',
  'The ‘Abbotsford Avengers’ soccer team beat the ‘East Melbourne Eagles’ in the final. In order for the ‘East Melbourne Eagles’ to see what they needed to improve on, they collected the <em class="v">successful passes</em> (%) for each member of both teams.'
  '<p style="font-size:21px;margin:12px 0 2px">Abbotsford Avengers: &nbsp;64 &nbsp;68 &nbsp;70 &nbsp;53 &nbsp;57 &nbsp;62 &nbsp;74 &nbsp;77 &nbsp;36 &nbsp;41 &nbsp;66</p><p style="font-size:21px;margin:0 0 12px">East Melbourne Eagles: &nbsp;59 &nbsp;90 &nbsp;83 &nbsp;87 &nbsp;88 &nbsp;76 &nbsp;82 &nbsp;83 &nbsp;91 &nbsp;78 &nbsp;75</p>'+
  plist([('a','Construct a back-to-back stem plot to display this data, with the ‘Abbotsford Avengers’ on the left.'),('b','Which team had a higher median <em class="v">successful passes</em>?')]),
  [('Stems','two-digit data from 36 to 91: stems 3 to 9 (tens), leaves = ones','data-pk="0"'),
   ('Left leaves','Avengers: increase moving away from the stem','data-pk="0" data-show="#y1s|'+allk('L',l)+'"'),
   ('Right leaves','Eagles; then add the key 5 | 9 = 59%','data-pk="0" data-show="#y1s|'+allk('R',r)+'"'),
   ('TMPL',bbstem('y1s',st,l,r,'Abbotsford Avengers','East Melbourne Eagles','Key: 5 | 9 = 59%','',fs=17,hid=True)),
   ('Medians','11 players: the 6th value. Avengers 64% · Eagles 83%','data-pk="1" data-hi="#y1s|L3.2,R5.1|hy"'),
   ('ANS','<b>b</b> &nbsp;East Melbourne Eagles.')],
  '',f'{EDR} · 2B Worked example 1 (pp. 120–121)',cmd=('Construct',None,'stems, both sets of leaves, a key')))

# ================= Learn 2C: parallel boxplots
LB=W(620,pbox(EX11,40,120,10,'Resting pulse rate',W=680,rowH=70,fs=16,lab=80,minor=5).replace('<svg','<svg id="lbx"',1))
body=('<div class="row" style="gap:20px;align-items:stretch"><div class="key" style="flex:1"><h4>Parallel boxplots</h4>'
  '<p style="font-size:20px">One boxplot for each category of the EV, all on the <b>same axis</b>. The most common tool for a numerical RV and a categorical EV.</p>'
  f'<div style="margin-top:8px">{LB}</div></div>'
  '<div class="key" style="flex:.9"><h4>Read off each group</h4><ul class="bul" style="font-size:19px;line-height:1.6;margin-left:24px">'
  '<li class="frag" data-hi="#lbx|0m,1m|hy"><b>centre</b>: the median line</li><li class="frag" data-hi="#lbx|0b,1b|hb"><b>spread</b>: box length = IQR</li>'
  '<li class="frag" data-hi="#lbx|0w,1w|hg"><b>shape</b>: whiskers and median position</li><li class="frag" data-hi="#lbx|1o|hc"><b>outliers</b>: the separate dots</li></ul>'
  '<p class="frag" style="font-size:19px;margin-top:10px" data-hi="#lbx||">Each section (whisker, half-box) holds about 25% of the group.</p></div></div>'
  '<div class="tip frag" style="margin-top:12px">Compare with SOCS, then say whether the variables are associated.</div>')
S.append(TPL._frame('learn','Learn · 2C','Using parallel boxplots to compare groups',body,f'{CAM}, 2C p. 125 (pulse-rate boxplots, Example 11)',cfu='disc'))
# ================= WE11
S.append(qslide('we','Worked example 11 · 2C','Comparing distributions across two groups using parallel boxplots',
  G('Use the following parallel boxplots to compare the pulse rates (in beats/minute) for a group of 70 male students and 90 female students.',
    W(760,pbox(EX11,40,120,5,'Resting pulse rate',W=800,rowH=74,fs=16,lab=80,tick_every=1).replace('<svg','<svg id="w11b"',1)),''),
  [('RV and EV','RV: <em>resting pulse rate</em> (numerical) · EV: <em>gender</em> (categorical)'),
   ('Shape','both approximately symmetric','data-hi="#w11b|0w,1w|hg" data-fill="w111"'),
   ('Outliers','two male outliers, at 40 and 120','data-hi="#w11b|1o|hc" data-fill="w112"'),
   ('Centre','medians: female about 72, male about 65','data-hi="#w11b|0m,1m|hy" data-fill="w113"'),
   ('Spread','IQR: female 15, male 10','data-hi="#w11b|0b,1b|hb" data-fill="w114"'),
   ('Conclude','medians and IQRs differ → associated','data-hi="#w11b||" data-fill="w115"'),
   ('TMPL',csocs('w11',['The distributions of resting pulse rates for both male and female students were approximately symmetric.','One male was found to have an extremely low pulse rate of 40, while another had an extremely high pulse rate of 120.',
     'On average, the resting pulse rate for males is lower (median: male = 65, female = 72)','and less variable than that for females (IQR: male = 10, female = 15).'],'There is an association between resting pulse rate and gender.',fs=15))],
  '',f'{CAM} · Example 11 (pp. 125–126; boxplots redrawn; report in SOCS order)',video='Cambridge GO · Example 11 (2C Resources)',cmd=('compare',None,'SOCS, every group')))
# ================= You try: Edrolo 2B WE3 (construct parallel boxplots)
sb=pbox(YT3,0,15,1,'number of people',W=620,rowH=70,fs=16,lab=95,hid=True).replace('<svg','<svg id="y3b"',1)
S.append(qslide('yt','You try · Edrolo 2B WE3','Constructing parallel boxplots',
  'Daniel went to his local cafe every Sunday for a year and counted the number of people wearing Salomon shoes and the number of people wearing Crocs. The five-number summaries for both shoe brands are recorded.'
  '<p style="font-size:24px;margin:16px 0 4px">Salomons: 2, 4, 5, 9, 15</p><p style="font-size:24px;margin:0 0 16px">Crocs: 0, 2, 4, 7, 8</p>'+
  plist([('a','Construct parallel boxplots to display this data.'),('b','For which shoe brand was the <em class="v">number of people</em> positively skewed?')]),
  [('Scale','data from 0 to 15: one axis, 0 to 15, a tick for each whole number','data-pk="0"'),
   ('Salomons','box 4 to 9, median 5, whiskers to 2 and 15 (no outliers)','data-pk="0" data-show="#y3b|0"'),
   ('Crocs','box 2 to 7, median 4, whiskers to 0 and 8','data-pk="0" data-show="#y3b|1"'),
   ('TMPL',W(560,sb)),
   ('Shape','Salomons: long right whisker, median near Q₁ → trails off to the right','data-pk="1" data-hi="#y3b|0w|hg"'),
   ('ANS','<b>b</b> &nbsp;Salomons.')],
  '',f'{EDR} · 2B Worked example 3 (pp. 122–123)',cmd=('Construct',None,'one axis, a box for each group')))
# ================= WE12
S.append(qslide('we','Worked example 12 · 2C','Comparing distributions across more than two groups using parallel boxplots',
  G('Use the parallel boxplots below to compare the salary distribution for workers in a certain industry across four different age groups: 20–29 years, 30–39 years, 40–49 years and 50–65 years.',
    W(760,pbox(EX12,40,140,10,'Salary ($’000)',W=820,rowH=56,fs=16,lab=120,minor=2).replace('<svg','<svg id="w12b"',1)),''),
  [('RV and EV','RV: <em>salary</em> · EV: <em>age group</em>'),
   ('Shape','from symmetric (20–29) to positively skewed','data-hi="#w12b|0w,3w|hg" data-fill="w121"'),
   ('Outliers','none for 20–29 and 30–39; $110 000 (40–49); $119 000, $126 000, $140 000 (50–65)','data-hi="#w12b|0o,1o|hc" data-fill="w122"'),
   ('Centre','median rises from $64 000 to $72 000','data-hi="#w12b|3m,0m|hy" data-fill="w123"'),
   ('Spread','IQR rises from about $12 000 to about $20 000','data-hi="#w12b|3b,0b|hb" data-fill="w124"'),
   ('TMPL',csocs('w12',['The shape of the distribution of salaries changes with age group, from symmetric for 20−29-year-olds, to progressively more positively skewed as age increases.',
     'There are no outliers in the 20-29 and 30-39 age group. Outliers also begin to appear at $110 000 for the 40-49 age group, and at $119 000, $126 000 and $140 000 for the 50-65 age group.',
     'The median salaries increase across the age groups, from $64 000 for 20−29 year-olds to $72 000 for 50−65 year-olds.',
     'The salaries also became more variable, with the IQR increasing from around $12 000 for 20−29-year-olds to around $20 000 for 50−65-year-olds.'],
     'In this industry there is an association between salary and age group.',fs=13),'','data-hi="#w12b||" data-fill="w125"')],
  '',f'{CAM} · Example 12 (pp. 126–127; boxplots redrawn; report in SOCS order)',video='Cambridge GO · Example 12 (2C Resources)',cmd=('compare',None,'SOCS across all four groups')))
# ================= You try: Edrolo 2B WE4
S.append(qslide('yt','You try · Edrolo 2B WE4','Writing a report from parallel boxplots',
  G('The following parallel boxplots display the distribution of prices for a 3-bedroom house in three different locations in NSW: ‘rural’, ‘outer suburbs’ and ‘inner suburbs’.',
    W(760,pbox(YT4,0,2.4,0.2,'price ($000 000’s)',W=820,rowH=62,fs=16,lab=130,minor=0.1).replace('<svg','<svg id="y4b"',1)),
    'Identify the association between <em class="v">price</em> and <em class="v">location</em>.<br>Write a report referencing shape, centre and spread.'),
  [('Shape','rural, outer suburbs: positively skewed · inner suburbs: approximately symmetric','data-hi="#y4b|0w,1w,2w|hg" data-fill="y41"'),
   ('Centre','medians: $600 000 · $1 100 000 · $1 600 000','data-hi="#y4b|0m,1m,2m|hy" data-fill="y43"'),
   ('Spread','range: $600 000 · $1 600 000 · $1 500 000 · IQR: $200 000 · $700 000 · $800 000','data-hi="#y4b|0b,1b,2b|hb" data-fill="y44"'),
   ('TMPL',csocs('y4',['In relation to shape, the distribution of price is positively skewed in locations further from a city in NSW and approximately symmetrical in the inner suburbs.',None,
     'In relation to centre, the median price increases as the location is closer to a city in NSW.','In relation to spread, the range and IQR of price tends to be larger in locations closer to a city in NSW.'],
     'The parallel boxplots show that price and location are associated. The closer a 3-bedroom house is to a city in NSW, the higher the price of the house.',fs=14),'','data-hi="#y4b||" data-fill="y45"')],
  '',f'{EDR} · 2B Worked example 4 (p. 124; boxplots redrawn; report in SOCS order)',cmd=('Write',None,'shape, centre and spread')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['parallel-boxplots']
S.append(cas('CAS · 2C','Creating parallel boxplots',
  '<p style="font-size:22px">Use your CAS to draw parallel boxplots of the sit-ups data from Worked example 9, and read off each five-number summary.</p>'
  '<p style="font-size:19px;margin-top:10px">Before: 22, 22, 23, 24, 25, 26, 26, 26, 28, 29, 29, 30, 31, 34, 46<br>After: 24, 25, 25, 26, 28, 30, 30, 32, 33, 34, 35, 36, 43, 50, 54</p>'
  '<p style="font-size:18px;margin-top:10px" class="muted">TI-Nspire: one list <b>situps</b> (all 30 values) and one list <b>program</b> (before / after). ClassPad: <b>list1</b> = before, <b>list2</b> = after.</p>'+
  W(480,pbox([('Before',(22,24,26,30,34),[46]),('After',(24,26,32,36,50),[54])],20,56,4,'number of sit-ups',W=560,rowH=56,fs=15,lab=80)),
  C['ti'],C['classpad'],'Before: 22, 24, 26, 30, 34, outlier 46 · After: 24, 26, 32, 36, 50, outlier 54',
  f'Data: {CAM} Example 9 · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2016 Exam 1 Q8','Show what you know',
  '<p style="font-size:24px;margin-top:20px">Parallel boxplots would be an appropriate graphical tool to investigate the association between the monthly median rainfall, in millimetres, and the</p>',
  [('Variable types','monthly median rainfall is numerical, so the other variable must be categorical'),('Check options','only month of the year (January, February, March, etc.) is categorical')],
  '<b>C</b>: month of the year.',f'{EDR} · 2B Q11 · VCAA 2016 Further Mathematics Exam 1 Core Q8 (examiner report)',stat=('mc',45),
  mc=['monthly median wind speed, in kilometres per hour.','monthly median temperature, in degrees Celsius.','month of the year (January, February, March, etc.).','monthly sunshine time, in hours.','annual rainfall, in millimetres.'],
  key='C',dist=[4,21,45,4,25],dis=('E','25% chose this: annual rainfall is numerical (and rainfall again). Parallel boxplots need one numerical and one categorical variable.')))
T2=table(['<em>Month</em>','Minimum','Q<sub>1</sub>','Median','Q<sub>3</sub>','Maximum'],[['February','5.9','9.5','10.9','13.9','22.2'],['May','3.3','6.0','7.5','9.8','12.7'],['July','1.6','3.7','5.0','5.9','7.7']],fs=15,rid='x2t')
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2019 Exam 2 Q3','Show what you know',
  G('The five-number summary for the distribution of <em class="v">minimum daily temperature</em> for the months of February, May and July in 2017 is shown in Table 2.<br>The associated boxplots are shown below the table.',
    '<div style="display:flex;flex-direction:column;align-items:center;gap:4px"><div style="font-size:15px;font-weight:700">Table 2. Five-number summary for <em>minimum daily temperature</em></div>'+T2+
    W(470,pbox(V19Q3,0,24,4,'minimum daily temperature (°C)',W=640,rowH=40,fs=15,lab=90).replace('<svg','<svg id="x2b"',1))+'</div>',
    'Explain why the information given above supports the contention that <em class="v">minimum daily temperature</em> is associated with the <em class="v">month</em>. Refer to the values of an appropriate statistic in your response. <span class="muted">(2 marks)</span>'),
  [('One statistic','use the median (quote it from the table, for all three months)','data-hi="#x2t|0,1,2|hy;#x2b|0m,1m,2m|hy"'),
   ('Say what changes','the median decreases from month to month: that change signals an association')],
  'The median <em class="v">minimum daily temperature</em> decreases from February (10.9 °C) to May (7.5 °C) to July (5.0 °C), so <em class="v">minimum daily temperature</em> is associated with <em class="v">month</em>.',
  f'{EDR} · 2B Q12 · VCAA 2019 Further Mathematics Exam 2 Core Q3 (examiner report: average 1.0; boxplots redrawn horizontally)',stat=('mark',36),cmd=('Explain',2,'a change in median, all three values')))
st,l,r=V17
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2017 Exam 2 Q2e','Show what you know',
  G('The back-to-back stem plot below displays the <em class="v">wingspan</em>, in millimetres, of 32 moths and their <em class="v">place of capture</em> (forest or grassland).',
    bbstem('x3s',st,l,r,'forest (<i>n</i> = 13)','grassland (<i>n</i> = 19)','key: 1|8 = 18','',title='<em>wingspan</em> (mm)',fs=21),
    'The back-to-back stem plot suggests that <em class="v">wingspan</em> is associated with <em class="v">place of capture</em>.<br>Explain why, quoting the values of an appropriate statistic. <span class="muted">(2 marks)</span>'),
  [('Forest median','13 moths: the 7th value = 21 mm','data-hi="#x3s|L1.1|hy"'),
   ('Grassland median','19 moths: the 10th value = 30 mm','data-hi="#x3s|R3.1|hb"'),
   ('Use one statistic','the median (the mean is not suitable: the forest 52 mm is an outlier)')],
  'The median <em class="v">wingspan</em> of moths captured in the grassland (30 mm) is higher than that of moths captured in the forest (21 mm). The medians differ, so <em class="v">wingspan</em> is associated with <em class="v">place of capture</em>.',
  f'{EDR} · 2B Q13 · VCAA 2017 Further Mathematics Exam 2 Core Q2e (examiner report: average 1)',stat=('mark',43),cmd=('Explain',2,'both medians, and that they differ')))

# ================= closing
S.append(checkin(SC))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 2 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='2C' and v.get('url')]))
n=assemble(S,'12MAG · L04 · Numerical and categorical variables',os.path.join(ROOT,'lessons','2C slides.html'))
print(n-1,'slides')
