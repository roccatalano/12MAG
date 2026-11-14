"""Sample deck: one slide of each template, using the 1G (Lesson 4) content. Output: tools/deck/tpl/sample.html"""
import os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
B=['box','med','wl','wu','out']
S=[]
S.append(title(4,'The five-number summary and the boxplot','Cambridge General Mathematics Units 3&amp;4 · 1G','S4'))
SC=['I can construct a boxplot from a five-number summary.','I can construct a boxplot with outliers from data using the CAS calculator.','I can read values from a boxplot.','I can estimate percentages from a boxplot.']
S.append(today(['To be able to construct the boxplot for displaying the distribution of a numerical data.','To be able to define and identify outliers.','To be able to use a CAS calculator to construct a boxplot.'],SC,
  [('Do Now','· four current VCAA questions','#00838F'),('APK','· Year 11 boxplots','var(--apk)'),('Five-number summary and the boxplot','→ WE 22',None),('Outliers and fences','· CAS',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([('Five-number summary','minimum, Q<sub>1</sub>, median, Q<sub>3</sub>, maximum'),('Boxplot','a picture of the five-number summary; the box holds the middle 50% of the data'),('Outlier','a value below the lower fence or above the upper fence'),('Whiskers','run to the smallest and largest values that are not outliers')],
  [('Median position',F('median position = ',FR(['<i>n</i> + 1'],['2']))),('Median, n even',F('M = ',FR(['first middle value + second middle value'],['2']))),('Interquartile range',F('IQR = Q<sub>3</sub> − Q<sub>1</sub>')),('Lower fence',F('Q<sub>1</sub> − 1.5 × IQR')),('Upper fence',F('Q<sub>3</sub> + 1.5 × IQR'))],
  'Cambridge General Mathematics Units 3&amp;4, 1F p. 44 and 1G pp. 61–64'))
# --- Do Now, multiple choice
runners=[134]*3+[135]*8+[136]*11+[137]*6+[138]*4+[139]*2+[140]*2+[141,142,143,146]
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q1','Review of 1F',
  ('The dot plot below shows the times, in seconds, of 40 runners in the qualifying heats of their 800 m club championship.',
   dot("t1d",{"min":134,"max":146,"vals":runners,"xl":"time (seconds)","W":900,"h":380,"r":12}),'The median time, in seconds, of these runners is'),
  [('Count','n = 40 runners.'),
   fx('Median position',None,F(FR([V('<i>n</i>','40'),' + 1'],['2'])),'20.5th'),
   ('Locate','between the 20th and 21st times: 3 + 8 = 11 up to 135 s, 11 + 11 = 22 up to 136 s. Both are 136.','data-dotmark="#t1d|19,20"'),
   fx('Median, n even',None,F(FR([V('20th','136'),' + ',V('21st','136')],['2'])),'136')],
  'The median time of these runners is <b>136 seconds</b>.','VCAA 2023 General Mathematics Exam 1 Q1 (examiner report)',
  stat=('mc',90),mc=['135.5','136','136.5','137','137.5'],key='B',dist=[1,90,6,2,1],
  dis=('C','136.5 averages 136 and 137. Count the dots: the 20th and 21st are both in the 136 column.'),cmd=('Multiple choice',1)))
# --- Do Now, short answer (Exam 2)
apt=['350 000','490 000','500 000','620 000','720 000','830 000','875 000','995 000','1 100 000','1 520 000']
hou=['800 000','840 000','920 000','920 000','1 010 000','1 263 000','1 398 000','1 460 000','1 540 000','1 540 000']
tb=lambda rows:'<table class="t" style="font-size:15px"><tr><th>Price ($)</th><th>Type</th></tr>'+''.join(f'<tr><td style="text-align:right">{p}</td><td>{t}</td></tr>' for p,t in rows)+'</table>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q1a','Review of 1F',
  ('Table 1, below, shows the prices in dollars, <em class="v">price</em>, for a sample of 20 homes sold in an inner Melbourne suburb during 2017. The type of home sold is either an apartment or a house.',
   f'<div class="tbl1" style="justify-content:center">{tb([(p,"apartment") for p in apt])}{tb([(p,"house") for p in hou])}</div>',
   '<b>a.</b> Find the median, in dollars, of the variable <em class="v">price</em>. <span class="muted">(1 mark)</span>'),
  [('Count','n = 20 homes.'),
   fx('Median position',None,F(FR([V('<i>n</i>','20'),' + 1'],['2'])),'10.5th'),
   ('Order','350 000, 490 000, 500 000, 620 000, 720 000, 800 000, 830 000, 840 000, 875 000, <b>920 000</b>, <b>920 000</b>, …'),
   fx('Median, n even',None,F(FR([V('10th','920 000'),' + ',V('11th','920 000')],['2'])),'920 000')],
  'The median price is <b>$920 000</b>.','VCAA 2025 General Mathematics Exam 2 Q1a (examiner report) · Data: Adapted from &lt;www.kaggle.com/datasets/anthonypino/melbourne-housing-market&gt;',
  stat=('mark',84),cmd=('Find',1,'the value, with working')))
# --- APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2H #15','Outliers from the fences',
  'The ages of a group of people at a party:<div class="data" style="font-size:21px">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>'
  'Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).',
  [('Quartiles','In order: 17 19 19 19 20 <b>20</b> 21 21 22 23 | 26 27 28 29 34 <b>34</b> 37 45 56 66 → Q<sub>1</sub> = 20, Q<sub>3</sub> = 34'),
   fx('Interquartile range',None,F(V('Q<sub>3</sub>','34'),' − ',V('Q<sub>1</sub>','20')),'14'),
   fx('Lower fence',None,F(V('Q<sub>1</sub>','20'),' − 1.5 × ',V('IQR','14')),'−1'),
   fx('Upper fence',None,F(V('Q<sub>3</sub>','34'),' + 1.5 × ',V('IQR','14')),'55','data-bx="#t3b|box,med,wl,wu,out"')],
  'The outliers are <b>56 and 66</b>: both are above the upper fence of 55.','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #15 (teacher solution)',
  cmd=('Calculate',2,'working for each fence'),
  made=box('t3b',{"min":15,"max":70,"step":5,"lw":17,"q1":20,"m":24.5,"q3":34,"uw":45,"out":[56,66],"xl":"age (years)","hide":B,"W":800,"fs":20,"top":20})))
# --- Learn
marks=[28,21,21,3,22,31,35,26,27,33,43,31,30,34,48,36,35,23,24]
S.append(learn('Learn · 1G','Outliers: the 1.5 × IQR fences',
  '<h4>Outlier</h4><p>A value more than 1.5 IQRs below Q<sub>1</sub> or above Q<sub>3</sub>. &nbsp; lower fence = Q<sub>1</sub> − 1.5 × IQR &nbsp;·&nbsp; upper fence = Q<sub>3</sub> + 1.5 × IQR</p>',
  box('t4b',{"min":0,"max":55,"step":1,"lab":5,"lw":21,"q1":23,"m":30,"q3":35,"uw":48,"out":[3],"hide":["wl","wu","out"],"W":1300,"fs":20,"top":70,"bh":60,
     "bands":[{"p":"iqr","a":23,"b":35,"t":"IQR = 35 − 23 = 12","col":"rgba(106,63,199,.15)","sc":"#6a3fc7","tc":"#5b33b0"}],
     "fences":[{"p":"fl","x":5,"t":"lower fence 23 − 18 = 5"},{"p":"fu","x":53,"t":"upper fence 35 + 18 = 53","left":True}]}),
  '<b>Whiskers stop at the last value inside the fences:</b> here 21 (not the outlier, 3) and 48.',
  'Cambridge General Mathematics Units 3&amp;4, 1G pp. 63–64 · Data: CAS 4 (p. 64)',
  frags='<span class="frag" data-bx="#t4b|iqr"></span><span class="frag" data-bx="#t4b|fl,fu"></span><span class="frag" data-bx="#t4b|out"></span><span class="frag" data-bx="#t4b|wl,wu"></span>'))
# --- Worked example + You try (identical shape)
life=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
five='<table class="t" style="font-size:17px;white-space:nowrap"><tr><td class="l">minimum</td><td>52</td></tr><tr><td class="l">first quartile (Q<sub>1</sub>)</td><td>66</td></tr><tr><td class="l">median (M)</td><td>73</td></tr><tr><td class="l">third quartile (Q<sub>3</sub>)</td><td>75</td></tr><tr><td class="l">maximum</td><td>77</td></tr></table>'
S.append(qslide('we','Worked example 22 · 1G','Constructing a boxplot from a five-number summary',
  ('The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:',
   f'<div class="row" style="gap:30px;justify-content:center">{stem("t5s",life,"Key: 5|2 = 52 years",20)}{five}</div>','Use the five-number summary to construct a boxplot.'),
  [('Number line','labelled and scaled to cover the full range of values.'),
   ('Box','from Q<sub>1</sub> = 66 to Q<sub>3</sub> = 75.','data-bx="#t5b|box"'),
   ('Median','a vertical line at M = 73.','data-bx="#t5b|med"'),
   ('Whiskers','out to the minimum (52) and maximum (77).','data-bx="#t5b|wl,wu"')],
  'The finished boxplot is above.',f'{CAM} · Example 22',cmd=('Construct',None,'scaled axis, box, median, whiskers'),video='Cambridge GO · Example 22 (1G Resources)',
  made=box('t5b',{"min":50,"max":80,"step":1,"lab":5,"lw":52,"q1":66,"m":73,"q3":75,"uw":77,"xl":"Life expectancy (years)","hide":B,"W":800,"fs":20,"top":20})))
w4=[('0',[1,2,3,5,5,9]),('1',[0,0,1,5,8,9]),('2',[1,2,3,3,5]),('3',[3,7,9])]
S.append(qslide('yt','You try · Edrolo 1E WE4','Constructing a boxplot from a five-number summary',
  ('The five-number summary for the following stem plot is: <b>1, 7, 16.5, 23, 39</b>',stem("t6s",w4,"Key: 1 | 2 = 12",22),'Construct a boxplot using the data.'),
  [('Outliers?','IQR = 23 − 7 = 16 · fences −17 and 47 → none.'),
   ('Box','from Q<sub>1</sub> = 7 to Q<sub>3</sub> = 23.','data-bx="#t6b|box"'),
   ('Median','a vertical line at 16.5.','data-bx="#t6b|med"'),
   ('Whiskers','out to the minimum (1) and maximum (39).','data-bx="#t6b|wl,wu"')],
  'The finished boxplot is above.',f'{EDR} · 1E Worked example 4',
  made=box('t6b',{"min":0,"max":40,"step":1,"lab":5,"lw":1,"q1":7,"m":16.5,"q3":23,"uw":39,"hide":B,"W":800,"fs":20,"top":20})))
# --- CAS
S.append(cas('CAS · 1G','Boxplot with outliers on CAS',
  'Display the following set of 19 marks in the form of a boxplot with outliers.<div class="data" style="font-size:22px">28 21 21 3 22 31 35 26 27 33<br>43 31 30 34 48 36 35 23 24</div>',
  ['New document → <b>Lists &amp; Spreadsheet</b>; list <b>marks</b>.','Add <b>Data &amp; Statistics</b>; x-axis → marks.','Menu › Plot Type › <b>Box Plot</b>.','Menu › Analyze › <b>Graph Trace</b> to read values.'],
  ['<b>Statistics</b> app; list <b>marks</b>.','SetGraph: Type <b>MedBox</b>, XList main\\marks.','Tick <b>Show Outliers</b>; Set; plot.','<b>Trace</b> to read values.'],
  'min = 3 (outlier) · Q<sub>1</sub> = 23 · M = 30 · Q<sub>3</sub> = 35 · max = 48','Cambridge General Mathematics Units 3&amp;4, 1G pp. 64–66 (CAS 4)'))
# --- Exit
hep=[(1,'1.76','15.34','41.22'),(2,'1.79','16.96','42.41'),(3,'1.83','13.87','46.53'),(4,'1.82','14.23','40.53'),(5,'1.87','13.78','40.62'),(6,'1.73','14.50','45.62'),(7,'1.68','15.08','42.33'),(8,'1.82','13.13','40.88'),(9,'1.83','14.22','39.22'),(10,'1.87','13.62','42.51'),(11,'1.87','12.01','42.75'),(12,'1.80','12.88','38.12'),(13,'1.83','12.68','42.65'),(14,'1.87','12.45','41.32'),(15,'1.78','11.31','42.88')]
ht='<table class="t tight" style="font-size:13px;line-height:1.12"><tr><th>athlete number</th><th>high jump (metres)</th><th>shot-put (metres)</th><th>javelin (metres)</th></tr>'+''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in hep)+'</table>'
S.append(qslide('ex','Exit task 1 of 2 · Edrolo 1E Q20 · VCAA 2021 Exam 2 Q1e','Show what you know',
  ('<span style="font-size:16px;line-height:1.3">In the sport of heptathlon, athletes compete in seven events. These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump. Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games. Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table. The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.</span>',
   f'<div class="row" style="gap:14px;align-items:center">{ht}<div style="flex:1">'+box("t8b",{"min":1.68,"max":1.88,"step":0.01,"lab":0.04,"dec":2,"lw":1.68,"q1":1.78,"m":1.82,"q3":1.87,"uw":1.87,"caps":True,"xl":"high jump","W":600,"fs":22,"top":14,"bh":44})+'</div></div>',
   'Explain why the boxplot has no whisker at its upper end. <span class="muted">(1 mark)</span>'),
  [('Read','Q<sub>3</sub> = 1.87 m and the maximum = 1.87 m.'),('Why','Four of the 15 athletes jumped 1.87 m, the highest height.')],
  'Q<sub>3</sub> is equal to the maximum value, so there is no distance for an upper whisker to cover.',
  f'{EDR} · 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e (examiner report)',stat=('avg',50),cmd=('Explain',1,'a reason, using values')))
S.append(checkin(SC))
S.append(coursework([('Cambridge · Exercise 1G (part 1)',[('Five-number summary from a dot or stem plot','Q1–2'),('Boxplot from a five-number summary','Q3–6')]),
                     ('Cambridge · Exercise 1G (part 2)',[('Reading percentages from a boxplot','Q11–13'),('Exam 1 style questions','Q17–20')])],'The <b>1G</b> section'))
n=assemble(S,'12MAG · Slide templates (sample)',os.path.join(os.path.dirname(os.path.abspath(__file__)),'sample.html'))
print('slides',n)
