"""Lesson 4 (1G) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S4-slides.html
Run: python3 tools/deck/s4/build.py"""
import os, sys
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
BUILD=['axis','box','med','wl','wu','out']
def casstep(mn,q1,m,q3,mx,note='One-variable statistics'):
    return ('CAS',f'{note} → <span class="c5">min <b>{mn}</b> · Q<sub>1</sub> <b>{q1}</b> · M <b>{m}</b> · Q<sub>3</sub> <b>{q3}</b> · max <b>{mx}</b></span>')
def ostep(lines,attrs=''): return ('Outliers?','<br>'.join(lines),attrs)
GT='&gt;'; LT='&lt;'
S=[]
# ================= opening
S.append(title(4,'The five-number summary and the boxplot','Cambridge General Mathematics Units 3&amp;4 · 1G','S4'))
LI=['To be able to construct the boxplot for displaying the distribution of a numerical data.','To be able to define and identify outliers.',
    'To be able to construct both simple boxplots and boxplots with outliers.','To be able to determine the features of a distribution from a boxplot.',
    'To be able to use a CAS calculator to construct a boxplot.']
SC=['I can construct a boxplot from a five-number summary.','I can construct a boxplot with outliers from data using the CAS calculator.',
    'I can read values from a boxplot.','I can estimate percentages from a boxplot.','I can use boxplots to describe a distribution without outliers.',
    'I can use boxplots to describe a distribution with outliers.','I can use boxplots to answer statistical questions.']
S.append(today(LI,SC,[('Do Now','· four current VCAA questions','#00838F'),('APK','· Year 11 boxplots','var(--apk)'),('Five-number summary and the boxplot','→ WE 22',None),
  ('Outliers and fences','· CAS',None),('Reading a boxplot','→ WE 23, 24',None),('Shape from a boxplot','→ WE 25, 26, 27',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mini=lambda rid,c:box(rid,dict({"min":0,"max":20,"step":1,"lab":100,"W":380,"fs":17,"top":44,"bh":26,"nolab":1},**c))
FPOS=F('position = ',FR(['<i>n</i> + 1'],['2'])); FMED=F('M = ',FR(['first middle + second middle'],['2']))
FIQR=F('IQR = Q<sub>3</sub> − Q<sub>1</sub>'); FRNG=F('range = max − min'); FLF=F('LF = Q<sub>1</sub> − 1.5 × IQR'); FUF=F('UF = Q<sub>3</sub> + 1.5 × IQR')
RLF='<i>x</i> &lt; LF → <i>x</i> is an outlier'; RUF='<i>x</i> &gt; UF → <i>x</i> is an outlier'
S.append(keys([
  ('Five-number summary','minimum, Q<sub>1</sub>, median, Q<sub>3</sub>, maximum',mini('k1',{"lw":2,"q1":6,"m":9,"q3":13,"uw":18,"marks":[{"p":"a","x":2,"t":"min","col":"#8a4d00"},{"p":"b","x":6,"t":"Q₁"},{"p":"c","x":9,"t":"M","col":"#d2475b"},{"p":"d","x":13,"t":"Q₃"},{"p":"e","x":18,"t":"max","col":"#8a4d00"}],"show":1})),
  ('Boxplot','a picture of the five-number summary: the box holds the middle 50% of the data',mini('k2',{"lw":2,"q1":6,"m":9,"q3":13,"uw":18,"bands":[{"p":"b","a":6,"b":13,"t":"50%","show":1}]})),
  ('Outlier','a value below the lower fence or above the upper fence, drawn as a dot',mini('k3',{"lw":5,"q1":7,"m":9,"q3":11,"uw":13,"out":[18]})),
  ('Whiskers','run from the box to the smallest and largest values that are not outliers',mini('k4',{"lw":5,"q1":7,"m":9,"q3":11,"uw":13,"out":[18],"marks":[{"p":"w","x":13,"t":"last non-outlier","col":"#1f4fb0","show":1}]}))],
  [('Median position',FPOS),('Median, n even',FMED),('Interquartile range',FIQR),('Range',FRNG),('Lower fence',FLF,RLF),('Upper fence',FUF,RUF)],
  'Cambridge General Mathematics Units 3&amp;4, 1F pp. 44–47 and 1G pp. 61–64 · Boxplots: teacher illustrations'))
# ================= Do Now 1: VCAA 2023 E1 Q1
runners=[134]*3+[135]*8+[136]*11+[137]*6+[138]*4+[139]*2+[140]*2+[141,142,143,146]
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q1','Review of 1F',
  ('The dot plot below shows the times, in seconds, of 40 runners in the qualifying heats of their 800 m club championship.',
   dot('d1',{"min":134,"max":146,"vals":runners,"xl":"time (seconds)","W":900,"h":380,"r":12}),'The median time, in seconds, of these runners is'),
  [('Count','n = 40 runners (40 dots).'),
   fx('Median position',None,F(FR([V('<i>n</i>','40'),' + 1'],['2'])),'20.5th',ra='data-dsplit="#d1|19|20.5th"'),
   ('Find','the 20th and 21st dots, counting from the left: both are in the 136 column.','data-dotmark="#d1|19,20"'),
   fx('Median, n even',None,F(FR([V('20th','136'),' + ',V('21st','136')],['2'])),'136')],
  'The median time is <b>136 seconds</b>.','VCAA 2023 General Mathematics Exam 1 Q1 (examiner report)',
  stat=('mc',90),mc=['135.5','136','136.5','137','137.5'],key='B',dist=[1,90,6,2,1],
  dis=('C','136.5 averages 136 and 137, as if the middle sat between two columns. The 20th and 21st dots are both in the 136 column.')))
# ================= Do Now 2: VCAA 2023 E1 Q6
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2023 Exam 1 Q6','Review of 1E',
  ('The histogram below displays the distribution of prices, in dollars, of the cars for sale in a used-car yard.<br>The histogram has a logarithm (base 10) scale.',
   hist('d2',{"start":3.0,"w":0.5,"v":[2,6,5,4,2,1,0],"xmax":6.5,"ymax":7,"ystep":1,"tick":0.5,"dec":1,"xl":"log10 (price)","yl":"frequency","h":330,"W":620,"fs":17,"col":"#a9a9a9"},'data-hidelab=\'["6.5","1","3","5","7"]\''),
   'Six of the cars in the yard have the following prices: $2450 · $3175 · $4999 · $8925 · $10 250 · $105 600<br>How many of the six car prices listed above are in the modal class interval?'),
  [('Modal class','the tallest column: log<sub>10</sub>(price) from 3.5 to 4.0.','data-hlbar="#d2|1|#d98a1f"'),
   ('Convert','log<sub>10</sub>(2450) = 3.39 · log<sub>10</sub>(3175) = <b>3.50</b> · log<sub>10</sub>(4999) = <b>3.70</b> · log<sub>10</sub>(8925) = <b>3.95</b> · log<sub>10</sub>(10 250) = 4.01 · log<sub>10</sub>(105 600) = 5.02'),
   ('Count','3.50, 3.70 and 3.95 are from 3.5 up to 4.0: three prices.')],
  'Three of the six prices ($3175, $4999, $8925) are in the modal class.','VCAA 2023 General Mathematics Exam 1 Q6 (examiner report)',
  stat=('mc',54),mc=['1','2','3','4','6'],key='C',dist=[9,11,54,13,13],
  dis=('D','$10 250 looks close, but log<sub>10</sub>(10 250) = 4.01 is just past 4.0, so it is in the next column.')))
# ================= Do Now 3 / 4: VCAA 2025 E2 Q1a, Q1b
apt=['350 000','490 000','500 000','620 000','720 000','830 000','875 000','995 000','1 100 000','1 520 000']
hou=['800 000','840 000','920 000','920 000','1 010 000','1 263 000','1 398 000','1 460 000','1 540 000','1 540 000']
RK={}
for i,v in enumerate(sorted([(int(p.replace(' ','')),k) for k,p in enumerate(apt+hou)])): RK[v[1]]=i
def t1(rid):
    tb=lambda rows,o:'<table class="t" style="font-size:15px"><tr><th>Price ($)</th><th>Type</th></tr>'+''.join(f'<tr><td style="text-align:right"><span data-i="{RK[o+k]}" style="padding:0 4px;border-radius:5px;border:1.5px solid transparent">{p}</span></td><td><span class="ty">{t}</span></td></tr>' for k,(p,t) in enumerate(rows))+'</table>'
    return f'<div class="tbl1" id="{rid}" style="justify-content:center">{tb([(p,"apartment") for p in apt],0)}{tb([(p,"house") for p in hou],10)}</div>'
INTRO='Table 1, below, shows the prices in dollars, <em class="v">price</em>, for a sample of 20 homes sold in an inner Melbourne suburb during 2017.<br>The type of home sold is either an apartment or a house.'
DSRC='Data: Adapted from &lt;www.kaggle.com/datasets/anthonypino/melbourne-housing-market&gt;'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q1a','Review of 1F',
  (INTRO,t1('d3'),'<b>a.</b> Find the median, in dollars, of the variable <em class="v">price</em>. <span class="muted">(1 mark)</span>'),
  [('Count','n = 20 homes.'),
   fx('Median position',None,F(FR([V('<i>n</i>','20'),' + 1'],['2'])),'10.5th'),
   ('Find','the 10th and 11th prices in order: both are 920 000.','data-mark="#d3|9,10|mid"'),
   fx('Median, n even',None,F(FR([V('10th','920 000'),' + ',V('11th','920 000')],['2'])),'920 000')],
  'The median price is <b>$920 000</b>.',f'VCAA 2025 General Mathematics Exam 2 Q1a (examiner report) · {DSRC}',
  stat=('mark',84),cmd=('Find',1,'the value, with working')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 Exam 2 Q1b','Review of 1A',
  (INTRO,t1('d4'),'<b>b.</b> State whether the variable <em class="v">type</em> is numerical, nominal or ordinal. <span class="muted">(1 mark)</span>'),
  [('Values','<em class="v">type</em> takes the values apartment and house: names, not numbers, so it is categorical.'),
   ('Order?','apartment and house have no natural order, so the categories are nominal.')],
  'The variable <em class="v">type</em> is <b>nominal</b>.',f'VCAA 2025 General Mathematics Exam 2 Q1b (examiner report) · {DSRC}',
  stat=('mark',77),cmd=('State',1,'just the answer')))
# ================= APK 1 / 2: party ages (Cambridge U1&2 2H #14, #15)
PARTY='The ages of a group of people at a party:<div class="data" style="font-size:21px">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>'
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2H #14','Five-number summary and boxplot',
  PARTY+'Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).',
  [('CAS','enter the 20 ages in a list. Don’t order them by hand: it is slow and error-prone.'),casstep(17,20,24.5,34,66),
   ('Scale','the ages run from 17 to 66, so an axis from 15 to 70 covers them.')],
  'Five-number summary: <b>17, 20, 24.5, 34, 66</b>','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #14 (teacher solution)',
  cmd=('Complete',None,'fill in all five values'),
  afig=box('a1b',{"min":15,"max":70,"step":5,"lw":17,"q1":20,"m":24.5,"q3":34,"uw":66,"xl":"age (years)","hide":BUILD,"W":800,"fs":20,"top":16}),
  build=[('Axis from 15 to 70','data-bx="#a1b|axis"'),('Box from Q<sub>1</sub> = 20 to Q<sub>3</sub> = 34, median at 24.5','data-bx="#a1b|box,med"'),('Whiskers to 17 and 66','data-bx="#a1b|wl,wu"')]))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2H #15','Outliers from the fences',
  PARTY+'Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).',
  [fx('Interquartile range',None,F(V('Q<sub>3</sub>','34'),' − ',V('Q<sub>1</sub>','20')),'14'),
   fx('Lower fence',None,F(V('Q<sub>1</sub>','20'),' − 1.5 × ',V('IQR','14')),'−1'),
   fx('Upper fence',None,F(V('Q<sub>3</sub>','34'),' + 1.5 × ',V('IQR','14')),'55'),
   ostep([f'56 {GT} 55 = UF → <b>outlier</b> · 66 {GT} 55 = UF → <b>outlier</b>',f'smallest age 17 {GT} −1 = LF → no low outliers'])],
  'The fences are −1 and 55. The outliers are <b>56 and 66</b>.','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #15 (teacher solution)',
  cmd=('Calculate',None,'working for each fence'),
  afig=box('a2b',{"min":-5,"max":70,"step":5,"lw":17,"q1":20,"m":24.5,"q3":34,"uw":45,"out":[56,66],"xl":"age (years)","hide":BUILD,"W":800,"fs":19,"top":62,
       "fences":[{"p":"fl","x":-1,"t":"LF = −1"},{"p":"fu","x":55,"t":"UF = 55","left":True}]}),
  build=[('Box (Q<sub>1</sub> = 20 and Q<sub>3</sub> = 34 from the CAS), median and fences','data-bx="#a2b|axis,box,med,fl,fu"'),('56 and 66 as dots; upper whisker stops at 45','data-bx="#a2b|out,wl,wu"')]))
# ================= APK 3: Edrolo U1&2 1F Q16 (adapted from VCAA 2017 E1 Q2)
S.append(qslide('apk','APK · VCAA 2017 Exam 1 Q2 (adapted)','A real VCAA question you can already do',
  ('The boxplot shows the distribution of the <em class="v">reaction time</em> (milliseconds), of 256 firefighters.',
   box('a3b',{"min":0,"max":260,"step":10,"lab":50,"lw":122,"q1":130,"m":140,"q3":152,"uw":179,"out":[70,90,255],"caps":True,"xl":"reaction time (milliseconds)","W":820,"fs":19,"top":56,"bh":46,
     "marks":[{"p":"mn","x":70,"t":"min = 70","col":"#8a4d00"},{"p":"mx","x":255,"t":"max = 255","col":"#8a4d00","anchor":"end"},{"p":"bx","x":140,"t":"130 · 140 · 152","col":"#6a3fc7"}]}),
   'The five-number summary for the <em class="v">reaction time</em> of these 256 firefighters is closest to'),
  [('Outliers are data','the dots at 70, 90 and 255 are real reaction times.','data-bxo="#a3b|#d98a1f"'),
   ('Min and max','smallest value = 70, largest value = 255 (dots, not whisker ends).','data-bx="#a3b|mn,mx"'),
   ('Box','Q<sub>1</sub> = 130, M = 140, Q<sub>3</sub> = 152.','data-bx="#a3b|bx"')],
  'The five-number summary is <b>70, 130, 140, 152, 255</b>.','Edrolo General Mathematics Units 1&amp;2 · 1F Q16 · Adapted from VCAA 2017 Exam 1 Data analysis Q2 (58%; distractor %: Edrolo U3&amp;4 1E)',
  stat=('mc',58),mc=['70, 130, 140, 152, 179','70, 130, 140, 152, 255','122, 130, 140, 152, 179','122, 130, 140, 152, 245','122, 130, 140, 152, 265'],key='B',
  dis=('C','On the original VCAA question, 38% chose this: they used the whisker ends as the minimum and maximum and ignored the outlier dots.')))
# ================= Learn 1: five numbers, one picture
S.append(learn('Learn · 1G','The five-number summary and the boxplot',
  '<h4>Boxplot</h4><p>A boxplot is a picture of the five-number summary. The box runs from Q<sub>1</sub> to Q<sub>3</sub> with a line at the median; the whiskers run out to the smallest and largest values.</p>',
  box('l1b',{"min":0,"max":100,"step":5,"lab":10,"lw":12,"q1":35,"m":50,"q3":62,"uw":95,"hide":BUILD,"W":1300,"fs":20,"bh":64,"top":66,
     "marks":[{"p":"k0","x":12,"t":"minimum","col":"#8a4d00"},{"p":"k1","x":35,"t":"Q₁","col":"#6a3fc7"},{"p":"k2","x":50,"t":"median","col":"#d2475b"},{"p":"k3","x":62,"t":"Q₃","col":"#6a3fc7"},{"p":"k4","x":95,"t":"maximum","col":"#8a4d00"}],
     "bands":[{"p":"p1","a":12,"b":35,"t":"25%"},{"p":"p2","a":35,"b":50,"t":"25%"},{"p":"p3","a":50,"b":62,"t":"25%"},{"p":"p4","a":62,"b":95,"t":"25%"}]}),
  '<b>Each section holds about 25% of the data</b>, however long it looks. A long whisker means the values are spread out, not that there are more of them.',
  'Cambridge General Mathematics Units 3&amp;4, 1G pp. 61–62 · Boxplot: teacher illustration',
  frags='<span class="frag" data-bx="#l1b|axis,k0,k1,k2,k3,k4"></span><span class="frag" data-bx="#l1b|box"></span><span class="frag" data-bx="#l1b|med"></span><span class="frag" data-bx="#l1b|wl,wu"></span><span class="frag" data-bx="#l1b|p1,p2,p3,p4"></span>',
  cards=[kcard('Five-number summary','minimum, Q<sub>1</sub>, M, Q<sub>3</sub>, maximum')]))
# ================= WE22
life=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
FIVE='<table class="t" style="font-size:17px;white-space:nowrap"><tr><td class="l">minimum</td><td>52</td></tr><tr><td class="l">first quartile (Q<sub>1</sub>)</td><td>66</td></tr><tr><td class="l">median (M)</td><td>73</td></tr><tr><td class="l">third quartile (Q<sub>3</sub>)</td><td>75</td></tr><tr><td class="l">maximum</td><td>77</td></tr></table>'
S.append(qslide('we','Worked example 22 · 1G','Constructing a boxplot from a five-number summary',
  ('The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:',
   f'<div class="row" style="gap:30px;justify-content:center">{stem("w22s",life,"Key: 5|2 = 52 years",20)}{FIVE}</div>','Use the five-number summary to construct a boxplot.'),
  [('Read','the five numbers from the table (they match the stem plot).','data-mark="#w22s|0,22|ext #w22s|5,17|q1m #w22s|11|mid"'),
   ('Scale','values run from 52 to 77, so an axis from 50 to 80 covers them.')],
  'The boxplot:',f'{CAM} · Example 22',video='Cambridge GO · Example 22 (1G Resources)',cmd=('Construct',None,'scaled axis, box, median, whiskers'),
  afig=box('w22b',{"min":50,"max":80,"step":1,"lab":5,"lw":52,"q1":66,"m":73,"q3":75,"uw":77,"xl":"Life expectancy (years)","hide":BUILD,"W":800,"fs":20,"top":16}),
  build=[('1 Number line: labelled and scaled','data-bx="#w22b|axis"'),('2 Box from Q<sub>1</sub> = 66 to Q<sub>3</sub> = 75','data-bx="#w22b|box"'),('3 Median line at M = 73','data-bx="#w22b|med"'),('4 Whiskers to 52 and 77','data-bx="#w22b|wl,wu"')]))
# ================= YT Edrolo 1E WE4
w4=[('0',[1,2,3,5,5,9]),('1',[0,0,1,5,8,9]),('2',[1,2,3,3,5]),('3',[3,7,9])]
S.append(qslide('yt','You try · Edrolo 1E WE4','Constructing a boxplot from a five-number summary',
  ('The five-number summary for the following stem plot is: <b>1, 7, 16.5, 23, 39</b>',stem('y4s',w4,'Key: 1 | 2 = 12',22),'Construct a boxplot using the data.'),
  [fx('Interquartile range',None,F(V('Q<sub>3</sub>','23'),' − ',V('Q<sub>1</sub>','7')),'16'),
   fx('Lower fence',None,F(V('Q<sub>1</sub>','7'),' − 1.5 × ',V('IQR','16')),'−17'),
   fx('Upper fence',None,F(V('Q<sub>3</sub>','23'),' + 1.5 × ',V('IQR','16')),'47'),
   ostep([f'smallest 1 {GT} −17 = LF · largest 39 {LT} 47 = UF → <b>no outliers</b>'],'data-mark="#y4s|0,19|ext"')],
  'The boxplot (no outliers):',f'{EDR} · 1E Worked example 4',cmd=('Construct',None,'scaled axis, box, median, whiskers'),
  afig=box('y4b',{"min":-20,"max":50,"step":1,"lab":10,"lw":1,"q1":7,"m":16.5,"q3":23,"uw":39,"hide":BUILD,"W":800,"fs":20,"top":62,
     "fences":[{"p":"fl","x":-17,"t":"LF = −17"},{"p":"fu","x":47,"t":"UF = 47","left":True}]}),
  build=[('Axis and fences (−17, 47)','data-bx="#y4b|axis,fl,fu"'),('Box from 7 to 23, median at 16.5','data-bx="#y4b|box,med"'),('Whiskers to 1 and 39','data-bx="#y4b|wl,wu"')]))
# ================= Learn 2: outliers and fences
marks19=[28,21,21,3,22,31,35,26,27,33,43,31,30,34,48,36,35,23,24]
S.append(learn('Learn · 1G','Outliers: the 1.5 × IQR fences',
  '<h4>Outlier</h4><p>A value more than 1.5 IQRs below Q<sub>1</sub> or above Q<sub>3</sub>. It is drawn as a dot, and the whisker stops at the last value inside the fence.</p>',
  dot('l2d',{"min":0,"max":55,"vals":marks19,"W":1300,"h":110,"r":8,"step":5})+
  box('l2b',{"min":0,"max":55,"step":1,"lab":5,"lw":21,"q1":23,"m":30,"q3":35,"uw":48,"out":[3],"hide":["wl","wu","out"],"W":1300,"fs":19,"top":64,"bh":46,
     "bands":[{"p":"iqr","a":23,"b":35,"t":"IQR = 35 − 23 = 12","col":"rgba(106,63,199,.15)","sc":"#6a3fc7","tc":"#5b33b0"}],
     "fences":[{"p":"fl","x":5,"t":"LF = 23 − 1.5 × 12 = 5"},{"p":"fu","x":53,"t":"UF = 35 + 1.5 × 12 = 53","left":True}]}),
  f'3 {LT} 5 = LF → <b>3 is an outlier</b>. Nothing is above 53, so the upper whisker runs to the largest value, 48; the lower whisker stops at 21.',
  'Cambridge General Mathematics Units 3&amp;4, 1G pp. 63–64 · Data: CAS 4 (p. 64)',
  frags='<span class="frag" data-bx="#l2b|iqr"></span><span class="frag" data-bx="#l2b|fl,fu"></span><span class="frag" data-bx="#l2b|out" data-dotmark="#l2d|0"></span><span class="frag" data-bx="#l2b|wl,wu"></span>',
  cards=[kcard('Lower fence',FLF,RLF),kcard('Upper fence',FUF,RUF)]))
# ================= CAS
S.append(cas('CAS · 1G','Boxplot with outliers on CAS',
  'Display the following set of 19 marks in the form of a boxplot with outliers.<div class="data" style="font-size:22px">28 21 21 3 22 31 35 26 27 33<br>43 31 30 34 48 36 35 23 24</div>',
  ['New document → <b>Lists &amp; Spreadsheet</b>; name a list <b>marks</b>; enter the data.','Add <b>Data &amp; Statistics</b>; x-axis → <b>marks</b>.','Menu › Plot Type › <b>Box Plot</b>.','Menu › Analyze › <b>Graph Trace</b> to read the values.'],
  ['<b>Statistics</b> app; name a list <b>marks</b>; enter the data.','SetGraph: Draw On · Type <b>MedBox</b> · XList main\\marks · Freq 1.','Tick <b>Show Outliers</b>; Set; plot.','Tap <b>Trace</b>; move with the cursor arrows.'],
  'min = 3 (outlier) · Q<sub>1</sub> = 23 · M = 30 · Q<sub>3</sub> = 35 · max = 48','Cambridge General Mathematics Units 3&amp;4, 1G pp. 64–66 (CAS 4)',
  videos=[yt('ClassPad Help 403 – Create a boxplot from a list','HBS1g3cja2g'),yt('ClassPad Help 404 – Boxplot from a frequency table','sw2xy8_x1k0'),
          yt('ClassPad Help 405 – Multiple boxplots','NCoE4Z-irZ0'),yt('TI-Nspire: Dot plots &amp; box plots','73Ymuvv-BU8')]))
# ================= YT CAS Edrolo 1E WE5
S.append(qslide('yt','You try · Edrolo 1E WE5','Constructing a boxplot with outliers using CAS',
  'Construct a boxplot for the following data set.<div class="data">2 4 4 5 5 5 7 6 5 4 6 5 6 7 8 12 3 5</div>',
  [casstep(2,4,5,6,12),
   fx('Interquartile range',None,F(V('Q<sub>3</sub>','6'),' − ',V('Q<sub>1</sub>','4')),'2'),
   fx('Lower fence',None,F(V('Q<sub>1</sub>','4'),' − 1.5 × ',V('IQR','2')),'1'),
   fx('Upper fence',None,F(V('Q<sub>3</sub>','6'),' + 1.5 × ',V('IQR','2')),'9'),
   ostep([f'12 {GT} 9 = UF → <b>outlier</b> · 2 {GT} 1 = LF → not an outlier'])],
  'The boxplot, with 12 as an outlier:',f'{EDR} · 1E Worked example 5',cmd=('Construct',None,'boxplot with any outliers'),
  afig=box('y5b',{"min":0,"max":13,"step":1,"lw":2,"q1":4,"m":5,"q3":6,"uw":8,"out":[12],"hide":BUILD,"xl":"list","W":800,"fs":19,"top":62,
     "fences":[{"p":"fl","x":1,"t":"LF = 1"},{"p":"fu","x":9,"t":"UF = 9"}]}),
  build=[('Axis, box (4 to 6), median (5) and fences (1, 9)','data-bx="#y5b|axis,box,med,fl,fu"'),('12 as a dot; whiskers to 2 and 8','data-bx="#y5b|out,wl,wu"')]))
# ================= WE23
S.append(qslide('we','Worked example 23 · 1G','Reading values from a boxplot',
  ('For the boxplot shown, write down the values of:',
   box('w23b',{"min":0,"max":100,"step":2,"lab":10,"lw":10,"q1":30,"m":36,"q3":44,"uw":60,"out":[4,70,84,92],"W":900,"fs":19,"top":96,
       "marks":[{"p":"mm","x":36,"t":"M = 36","col":"#d2475b","lv":1},{"p":"mq","x":30,"t":"Q₁ = 30","anchor":"end","dx":-4},{"p":"mq3","x":44,"t":"Q₃ = 44","anchor":"start","dx":4}],
       "fences":[{"p":"fu","x":65,"t":"UF = 65","lv":2},{"p":"fl","x":9,"t":"LF = 9","lv":2}]}),
   plist([('a','the median'),('b','the quartiles Q<sub>1</sub> and Q<sub>3</sub>'),('c','the interquartile range (IQR)'),('d','the minimum and maximum values'),('e','the values of any possible outliers'),
          ('f','the smallest value in the upper end of the data set that will be classified as an outlier'),('g','the largest value in the lower end of the data set that will be classified as an outlier.')])),
  [],'',f'{CAM} · Example 23',video='Cambridge GO · Example 23 (1G Resources)',cmd=('Write',None,'just the values'),
  parts=[('a','M = <b>36</b> (the line in the box)','data-bx="#w23b|mm"'),('b','Q<sub>1</sub> = <b>30</b>, Q<sub>3</sub> = <b>44</b> (the ends of the box)','data-bx="#w23b|mq,mq3"'),
         ('c',fx('IQR','IQR',F(V('Q<sub>3</sub>','44'),' − ',V('Q<sub>1</sub>','30')),'14')[1]),('d','min = <b>4</b>, max = <b>92</b> (the outer dots)'),
         ('e','<b>4, 70, 84 and 92</b> (the dots)','data-bxo="#w23b|#d98a1f"'),
         ('f',fx('UF','UF',F(V('Q<sub>3</sub>','44'),' + 1.5 × ',V('IQR','14')),'65',ra='data-bx="#w23b|fu"')[1]+'&nbsp;: any value above 65 is an outlier'),
         ('g',fx('LF','LF',F(V('Q<sub>1</sub>','30'),' − 1.5 × ',V('IQR','14')),'9',ra='data-bx="#w23b|fl"')[1]+'&nbsp;: any value below 9 is an outlier')]))
# ================= YT Edrolo 1E WE6
S.append(qslide('yt','You try · Edrolo 1E WE6','Reading values from a boxplot',
  ('The <em class="v">number of runs scored</em> by the leading batsman at a local cricket club is represented by the following boxplot.<br>It is known that data was collected from 20 separate innings.',
   box('y6b',{"min":0,"max":100,"step":5,"lab":10,"lw":30,"q1":50,"m":70,"q3":80,"uw":90,"caps":True,"xl":"number of runs scored","W":900,"fs":19,"top":56,
       "marks":[{"p":"m5","x":70,"t":"30 · 50 · 70 · 80 · 90","col":"#6a3fc7"}],
       "bands":[{"p":"b50","a":50,"b":80,"t":"middle 50%"},{"p":"b25","a":80,"b":90,"t":"25%","col":"rgba(47,111,223,.15)","sc":"#2f6fdf","tc":"#1f4fb0"},{"p":"b75","a":50,"b":90,"t":"75%","col":"rgba(31,158,116,.15)","sc":"#1f9e74","tc":"#137a59"}]}),
   plist([('a.','Determine the five-number summary for the data and identify any outliers.'),('b.','Between which two values does the middle 50% of data lie?'),
          ('c.','In approximately what percentage of innings did they score more than 80 runs?'),('d.','In approximately how many innings did they score at least 50 runs, but fall short of 100?')])),
  [],'',f'{EDR} · 1E Worked example 6',cmd=('Determine',None,'values read from the plot'),
  parts=[('a.','<b>30, 50, 70, 80, 90</b>; no dots, so <b>no outliers</b>','data-bx="#y6b|m5"'),('b.','from Q<sub>1</sub> to Q<sub>3</sub>: <b>50 and 80 runs</b>','data-bx="#y6b|=b50"'),
         ('c.','25% of the data is above Q<sub>3</sub> = 80: <b>25%</b>','data-bx="#y6b|=b25"'),
         ('d.','75% lies from Q<sub>1</sub> to the max: '+fx('n','innings',F('0.75 × ',V('<i>n</i>','20')),'15',ra='data-bx="#y6b|=b75"')[1])]))
# ================= WE24
S.append(qslide('we','Worked example 24 · 1G','Estimating percentages from a boxplot',
  ('For the boxplot shown, estimate the percentage of values:',
   box('w24b',{"min":45,"max":85,"step":1,"lab":5,"lw":50,"q1":54,"m":55,"q3":59,"uw":65,"out":[70,81],"W":900,"fs":19,"top":56,"bh":50,
       "bands":[{"p":"ba","a":50,"b":54,"t":"25%"},{"p":"bb","a":50,"b":55,"t":"50%"},{"p":"bc","a":50,"b":59,"t":"75%"},{"p":"bd","a":59,"b":81,"t":"25%"},{"p":"be","a":54,"b":59,"t":"50%"},{"p":"bf","a":54,"b":81,"t":"75%"}]}),
   plist([('a','less than 54'),('b','less than 55'),('c','less than 59'),('d','greater than 59'),('e','between 54 and 59'),('f','between 54 and 86.')])),
  [],'',f'{CAM} · Example 24 (boxplot as drawn in the textbook: top dot at about 81)',video='Cambridge GO · Example 24 (1G Resources)',cmd=('Estimate',None,'a percentage from the quartiles'),
  parts=[('a','54 is Q<sub>1</sub>; 25% of values are less than Q<sub>1</sub>: <b>25%</b>','data-bx="#w24b|=ba"'),('b','55 is the median; 50% are less than it: <b>50%</b>','data-bx="#w24b|=bb"'),
         ('c','59 is Q<sub>3</sub>; 75% are less than Q<sub>3</sub>: <b>75%</b>','data-bx="#w24b|=bc"'),('d','75% are less than 59, so 25% are greater: <b>25%</b>','data-bx="#w24b|=bd"'),
         ('e','75% − 25%: <b>50%</b>','data-bx="#w24b|=be"'),('f','100% are less than 86 and 25% are less than 54: <b>75%</b>','data-bx="#w24b|=bf"')]))
# ================= Learn 3: shape
sh=lambda rid,c:box(rid,dict({"min":0,"max":20,"step":1,"lab":100,"nolab":1,"W":620,"top":8,"bh":40,"fs":14},**c))
S.append(learn('Learn · 1G','Reading shape from a boxplot',
  '<h4>Shape</h4><p>Look at where the median sits in the box and which whisker is longer: the long side is the tail.</p>',
  '<div class="mini4"><div class="key frag"><h4>Symmetric</h4>'+sh('h1',{"lw":2,"q1":7,"m":10,"q3":13,"uw":18})+'<p>Median near the middle; whiskers about equal.</p></div>'
  '<div class="key frag"><h4>Positively skewed</h4>'+sh('h2',{"lw":1,"q1":3,"m":4.5,"q3":8,"uw":19})+'<p>Median to the <b>left</b>; long right whisker (tail to the right).</p></div>'
  '<div class="key frag"><h4>Negatively skewed</h4>'+sh('h3',{"lw":1,"q1":12,"m":15.5,"q3":17,"uw":19})+'<p>Median to the <b>right</b>; long left whisker (tail to the left).</p></div>'
  '<div class="key frag"><h4>With outliers</h4>'+sh('h4',{"lw":8,"q1":10,"m":11,"q3":12,"uw":14,"out":[2,19]})+'<p>Dots separated from the box and whiskers by a gap.</p></div></div>',
  '<b>Describe with SOCS, like a sock:</b> Shape · Outliers · Centre (the median) · Spread (IQR and range).',
  'Cambridge General Mathematics Units 3&amp;4, 1G pp. 68–69 · Sketches: teacher illustration',
  cards=[kcard('Range',FRNG)]))
# ================= WE25
S.append(qslide('we','Worked example 25 · 1G','Describing a distribution without outliers',
  ('Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.',
   box('w25b',{"min":0,"max":50,"step":1,"lab":5,"lw":0,"q1":5,"m":10,"q3":21,"uw":45,"W":900,"fs":19,"top":60,"col":"#fde7a6",
       "marks":[{"p":"mm","x":10,"t":"M = 10","col":"#d2475b","lv":1},{"p":"mq1","x":5,"t":"Q₁ = 5","anchor":"end","dx":-6},{"p":"mq3","x":21,"t":"Q₃ = 21"},{"p":"mx","x":45,"t":"max = 45","col":"#8a4d00"}]}),''),
  [('TMPL',socs('w25a','positively skewed','are no outliers',('10','median'),('IQR','16, and the range is 45'))),
   ('Shape','median to the left of the box, long right whisker: positively skewed.','data-fill="w25a1"'),
   ('Outliers','no dots beyond the whiskers.','data-fill="w25a2"'),
   ('Centre','the median: M = 10.','data-bx="#w25b|mm" data-fill="w25a3"'),
   fx('Interquartile range',None,F(V('Q<sub>3</sub>','21'),' − ',V('Q<sub>1</sub>','5')),'16','data-bx="#w25b|mq1,mq3"'),
   fx('Range',None,F(V('max','45'),' − ',V('min','0')),'45','data-bx="#w25b|mx" data-fill="w25a4"')],
  '',
  f'{CAM} · Example 25 (solution set out in SOCS order)',video='Cambridge GO · Example 25 (1G Resources)',cmd=('Describe',None,'shape, centre, spread with values')))
# ================= YT Edrolo 1F WE5
S.append(qslide('yt','You try · Edrolo 1F WE5','Describing a distribution without outliers',
  ('Consider the boxplot.',box('y25b',{"min":12,"max":20,"step":0.5,"lab":2,"lw":12,"q1":15,"m":18,"q3":19,"uw":20,"caps":True,"W":900,"fs":20,"top":50,"col":"#ddd3f3",
       "marks":[{"p":"mm","x":18,"t":"M = 18","col":"#d2475b"}]}),'Describe the distribution in terms of shape, centre, spread and outliers.'),
  [('TMPL',socs('y25a','negatively skewed','are no outliers',('18','median'),('range','8'))),
   ('Shape','median towards the right of the box, tail trails off to the left: negatively skewed.','data-fill="y25a1"'),('Outliers','no dots: no outliers.','data-fill="y25a2"'),
   ('Centre','median = 18.','data-bx="#y25b|mm" data-fill="y25a3"'),
   fx('Range',None,F(V('max','20'),' − ',V('min','12')),'8','data-fill="y25a4"')],
  '',f'{EDR} · 1F Worked example 5 (solution set out in SOCS order)',cmd=('Describe',None,'shape, centre, spread, outliers')))
# ================= WE26
S.append(qslide('we','Worked example 26 · 1G','Describing a distribution with outliers',
  ('Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.',
   box('w26b',{"min":0,"max":50,"step":1,"lab":5,"lw":34,"q1":38.75,"m":41,"q3":44.25,"uw":47,"out":[10,15,20,25],"W":900,"fs":19,"top":70,"col":"#e9c6ea",
       "marks":[{"p":"mm","x":41,"t":"M = 41","col":"#d2475b","lv":1}]}),''),
  [('TMPL',socs('w26a','symmetric','are outliers at 10, 15, 20 and 25',('41','median'),('IQR','5.5, and the range is 37'))),
   ('Shape','the box and whiskers are symmetric.','data-fill="w26a1"'),('Outliers','four dots: 10, 15, 20 and 25.','data-bxo="#w26b|#d98a1f" data-fill="w26a2"'),
   ('Centre','median = 41.','data-bx="#w26b|mm" data-fill="w26a3"'),
   fx('Interquartile range',None,F(V('Q<sub>3</sub>','44.25'),' − ',V('Q<sub>1</sub>','38.75')),'5.5'),
   fx('Range',None,F(V('max','47'),' − ',V('min','10')),'37','data-fill="w26a4"')],
  '',
  f'{CAM} · Example 26 (solution set out in SOCS order; no matching Edrolo worked example, so no You try)',video='Cambridge GO · Example 26 (1G Resources)',cmd=('Describe',None,'shape, outliers, centre, spread')))
# ================= WE27
S.append(qslide('we','Worked example 27 · 1G','Using a boxplot to answer statistical questions',
  ('The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.',
   box('w27b',{"min":25,"max":43,"step":1,"lw":35,"q1":38,"m":39,"q3":40,"uw":42,"out":list(range(25,35)),"xl":"Gestation period (weeks)","W":900,"fs":16,"top":40,"col":"#bcd6f2",
       "marks":[{"p":"mm","x":39,"t":"M = 39","col":"#d2475b"}]}),''),
  [('TMPL',socs('w27a','negatively skewed','are outliers at 25, 26, 27, 28, 29, 30, 31, 32, 33 and 34 weeks',('39 weeks','median'),('IQR','only 2 weeks, but the range is 17 weeks'),fs=17)),
   ('Shape','long tail of dots to the left: negatively skewed.','data-fill="w27a1"'),
   ('Outliers','any gestational period of less than 35 weeks is unusual: dots at 25, 26, …, 34 weeks.','data-bxo="#w27b|#d98a1f" data-fill="w27a2"'),
   ('Centre','median = 39 weeks.','data-bx="#w27b|mm" data-fill="w27a3"'),
   fx('Interquartile range',None,F(V('Q<sub>3</sub>','40'),' − ',V('Q<sub>1</sub>','38')),'2'),
   fx('Range',None,F(V('max','42'),' − ',V('min','25')),'17','data-fill="w27a4"')],
  '',
  f'{CAM} · Example 27 (solution set out in SOCS order; no matching Edrolo worked example, so no You try)',video='Cambridge GO · Example 27 (1G Resources)',cmd=('Describe',None,'shape, centre, spread, outliers')))
# ================= Exit 1: Edrolo 1E Q19 (VCAA 2020 E2 Q2c)
neck={31:1,32:1,33:3,34:11,35:19,36:32,37:34,38:48,39:39,40:18,41:28,42:12,43:3,44:1}
nv=[k for k,f in neck.items() for _ in range(f)]
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2020 Exam 2 Q2c','Show what you know',
  ('The <em class="v">neck size</em>, in centimetres, of 250 men was recorded and displayed in the following dot plot.',
   dot('e1d',{"min":30,"max":45,"vals":nv,"xl":"neck size (cm)","W":900,"h":560,"r":4.2,"fs":20}),
   'The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.<table class="t" style="font-size:16px;margin:4px 0;width:100%"><tr><th>minimum</th><th>first quartile (Q<sub>1</sub>)</th><th>median</th><th>third quartile (Q<sub>3</sub>)</th><th>maximum</th></tr><tr><td>31</td><td>36</td><td>38</td><td>39</td><td>44</td></tr></table>Use the five-number summary to construct a boxplot, showing any outliers if appropriate. <span class="muted">(2 marks)</span>'),
  [fx('Interquartile range',None,F(V('Q<sub>3</sub>','39'),' − ',V('Q<sub>1</sub>','36')),'3'),
   fx('Lower fence',None,F(V('Q<sub>1</sub>','36'),' − 1.5 × ',V('IQR','3')),'31.5'),
   fx('Upper fence',None,F(V('Q<sub>3</sub>','39'),' + 1.5 × ',V('IQR','3')),'43.5'),
   ostep([f'31 {LT} 31.5 = LF → <b>outlier</b> · 44 {GT} 43.5 = UF → <b>outlier</b>','whiskers stop at the last values inside the fences: 32 and 43'],'data-dotmark="#e1d|0,249"')],
  'The boxplot:',f'{EDR} · 1E Q19 · VCAA 2020 Exam 2 Data analysis Q2c (examiner report)',stat=('avg',55),cmd=('Construct',2,'boxplot with any outliers'),
  afig=box('e1b',{"min":30,"max":45,"step":1,"lw":32,"q1":36,"m":38,"q3":39,"uw":43,"out":[31,44],"hide":BUILD,"W":800,"fs":19,"top":62,"bh":40,"xl":"neck size (cm)",
     "fences":[{"p":"fl","x":31.5,"t":"LF 31.5","left":True},{"p":"fu","x":43.5,"t":"UF 43.5"}]}),
  build=[('Axis, box (36 to 39), median (38) and fences','data-bx="#e1b|axis,box,med,fl,fu"'),('31 and 44 as dots; whiskers to 32 and 43','data-bx="#e1b|out,wl,wu"')]))
# ================= Exit 2: Edrolo 1E Q20 (VCAA 2021 E2 Q1e)
hep=[(1,'1.76','15.34','41.22'),(2,'1.79','16.96','42.41'),(3,'1.83','13.87','46.53'),(4,'1.82','14.23','40.53'),(5,'1.87','13.78','40.62'),(6,'1.73','14.50','45.62'),(7,'1.68','15.08','42.33'),(8,'1.82','13.13','40.88'),(9,'1.83','14.22','39.22'),(10,'1.87','13.62','42.51'),(11,'1.87','12.01','42.75'),(12,'1.80','12.88','38.12'),(13,'1.83','12.68','42.65'),(14,'1.87','12.45','41.32'),(15,'1.78','11.31','42.88')]
hr={}
for i,(v,k) in enumerate(sorted((float(b),a) for a,b,c,d in hep)): hr[k]=i
ht='<table class="t tight" id="e2t" style="font-size:12px;line-height:1.05"><tr><th>athlete number</th><th>high jump (metres)</th><th>shot-put (metres)</th><th>javelin (metres)</th></tr>'+''.join(f'<tr><td>{a}</td><td><span data-i="{hr[a]}" style="padding:0 3px;border-radius:4px;border:1.5px solid transparent">{b}</span></td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in hep)+'</table>'
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 2 Q1e','Show what you know',
  ('<span style="font-size:15px;line-height:1.3;display:block">In the sport of heptathlon, athletes compete in seven events. These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump. Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games. Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table. The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.</span>',
   f'<div class="row" style="gap:12px;align-items:center">{ht}<div style="flex:1">'+box('e2b',{"min":1.68,"max":1.88,"step":0.01,"lab":0.04,"dec":2,"lw":1.68,"q1":1.78,"m":1.82,"q3":1.87,"uw":1.87,"caps":True,"xl":"high jump","W":600,"fs":22,"top":40,"bh":44,
       "marks":[{"p":"q3","x":1.87,"t":"Q₃ = max = 1.87","col":"#d2475b","anchor":"end"}]})+'</div></div>',
   'Explain why the boxplot has no whisker at its upper end. <span class="muted">(1 mark)</span>'),
  [('Q<sub>3</sub>','the box ends at Q<sub>3</sub> = 1.87 m.','data-bx="#e2b|q3"'),('Maximum','the highest jump in the table is 1.87 m: four athletes jumped it.','data-mark="#e2t|11,12,13,14|mid"')],
  'Q<sub>3</sub> is equal to the maximum value (1.87 m), so there is no distance for an upper whisker to cover.',
  f'{EDR} · 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e (examiner report)',stat=('avg',50),cmd=('Explain',1,'a reason, using values')))
# ================= close
S.append(checkin(SC))
import json
def _card(o):
    if isinstance(o,dict):
        if o.get('id')=='gm12-u3-s4': return o['card']
        for v in o.values():
            r=_card(v)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=_card(v)
            if r: return r
CW=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))))['homework']['sets']
S.append(coursework([(st['title'].replace('Revision book','Chapter 1 revision booklet'),st.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st['items']]) for st in CW]))
yid=lambda u:u.split('v=')[1].split('&')[0]
VJ=json.load(open(os.path.join(ROOT,'planner','videos.json'))); VJ=VJ if isinstance(VJ,list) else VJ.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in VJ if v['sub']=='1G']))
n=assemble(S,'12MAG · S4 · The five-number summary and the boxplot',f'{ROOT}/lessons/S4-slides.html')
print('slides',n)
