"""Lesson 1 (1A-1B) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S1-slides.html
Run: python3 tools/deck/s1/build.py
No Do Now: first lesson of the year (Rocco, 15 Nov)."""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; EDR12='Edrolo General Mathematics Units 1&amp;2'
def bar(rid,cfg,stepped=False): return f'<div class="chart" id="{rid}" data-chart="bar" data-cfg=\'{J(cfg)}\'{" data-stepped=\"1\"" if stepped else ""}></div>'
def seg(rid,cfg,stepped=False): return f'<div class="chart" id="{rid}" data-chart="seg" data-cfg=\'{J(cfg)}\'{" data-stepped=\"1\"" if stepped else ""}></div>'
def table(head,rows,fs=19,extra=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td{" class=\"l\"" if j==0 else ""}>{c}</td>' for j,c in enumerate(r))+'</tr>' for r in rows)
    return f'<table class="t" style="font-size:{fs}px;{extra}"><tr>{th}</tr>{tr}</table>'
def ftable(var,rows,total,pct=True,fs=19):
    """Cambridge-style frequency table: category | Number | Percentage"""
    h=f'<tr><th rowspan="2">{var}</th><th colspan="{2 if pct else 1}">Frequency</th></tr><tr><th>Number</th>'+('<th>Percentage</th>' if pct else '')+'</tr>'
    tr=''.join(f'<tr><td class="l">{a}</td><td>{b}</td>'+(f'<td>{c}</td>' if pct else '')+'</tr>' for a,b,c in rows)
    return f'<table class="t" style="font-size:{fs}px"><thead>{h}</thead>{tr}<tr><td class="l"><b>Total</b></td><td><b>{total[0]}</b></td>'+(f'<td><b>{total[1]}</b></td>' if pct else '')+'</tr></table>'
def letters(rid,vals,fs=24):
    return f'<div class="data" id="{rid}" style="font-size:{fs}px;letter-spacing:.06em;font-family:inherit">'+' '.join(f'<span data-i="{i}" style="padding:0 3px;border-radius:5px;border:1.5px solid transparent">{v}</span>' for i,v in enumerate(vals))+'</div>'
S=[]
# ================= opening
S.append(title(1,'Types of data and categorical data','Cambridge General Mathematics Units 3&amp;4 · 1A Types of data · 1B Displaying and describing the distributions of categorical variables','S1',
               flow=('APK','Learn','Worked examples','You try','Exit tasks')))
LI=['To be able to classify data as categorical or numerical.','To be able to further classify categorical data as nominal or ordinal.',
    'To be able to further classify numerical data as discrete or continuous.','To be able to construct frequency and percentage frequency tables for categorical data.',
    'To be able to construct bar charts and percentage bar charts from frequency tables.','To be able to interpret and describe frequency tables and bar charts.',
    'To be able to answer statistical questions about a categorical variable.']
SC=['I can identify types of data.','I can construct a frequency table for categorical data.','I can construct a bar chart from a frequency table.',
    'I can construct a percentage segmented bar chart from a frequency table.','I can describe the distribution of a categorical variable.']
S.append(today(LI,SC,[('APK','· Year 11 types of data, two VCAA questions','var(--apk)'),('Types of data','→ WE 1 · CAS set-up',None),('Frequency tables','→ WE 2',None),
  ('Bar charts','→ WE 3',None),('Segmented bar charts','→ WE 4',None),('Describing the distribution','→ WE 5',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
FPCT=F('percentage frequency = ',FR(['number of times a value occurs'],['total number of values']),' × 100%')
FCNT=F('number = ',FR(['percentage'],['100']),' × total')
FSEG=F('segment ends at previous end + its %')
S.append(keys([
  ('Categorical variable','names a quality or group: nominal (names only) or ordinal (names and orders)'),
  ('Numerical variable','a quantity: discrete (counted, ‘How many?’) or continuous (measured, ‘How much?’)'),
  ('Bar chart','one bar per category, with gaps; height = frequency',bar('kb',{"cats":["A","B","C"],"v":[3,6,4],"max":6,"step":2,"xl":"","yl":"","h":200})),
  ('Percentage segmented bar chart','one 100% bar, a segment per category, with a legend',seg('ks',{"bars":[{"v":[25,45,30]}],"names":["A","B","C"],"yl":"%","h":220,"ticks":50})),
  ('Mode (modal category)','the category that occurs most often: the tallest bar or longest segment')],
  [('Percentage frequency',FPCT),('Number from a percentage',FCNT),('Segmented bar',FSEG)],
  'Cambridge General Mathematics Units 3&amp;4, 1A pp. 2–4 and 1B pp. 7–10 · Charts: teacher illustrations'))
# ================= APK 1: Cambridge U1&2 2A #1
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2A #1','What do you remember?',
  'Classify the following data as nominal, ordinal, discrete or continuous:'+plist([('a','The time between people arriving at the coffee shop.'),('b','The number of people in the queue at the coffee shop.'),
     ('c','Customer’s coffee preference (latte, cappuccino, black).'),('d','Customer’s rating of the coffee (excellent, quite good, not that good).')]),
  [],'','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2A #1 (teacher solution)',cmd=('Classify',None,'one type for each'),
  parts=[('a','<b>Continuous</b>: time is measured.'),('b','<b>Discrete</b>: people are counted.'),('c','<b>Nominal</b>: the categories only name the coffee.'),('d','<b>Ordinal</b>: the ratings have a natural order.')]))
# ================= APK 2: Edrolo U1&2 1A Q13 = VCAA 2021 E1 Q1
S.append(qslide('apk','APK · Edrolo U1&amp;2 1A Q13','A real VCAA question you can already do',
  ('<div class="row" style="gap:12px;align-items:center"><div style="flex:1">The percentage segmented bar chart provided shows the <em class="v">age</em> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <em class="v">preferred travel destination</em> (domestic, international).</div><div style="width:300px;flex:none">'+
   seg('a2s',{"bars":[{"v":[65,35],"label":"under 55"},{"v":[45,55],"label":"55 and over"}],"names":["domestic","international"],"yl":"percentage","xl":"age","h":330,"ticks":20})+'</div></div>','',
   'The variables <em class="v">age</em> (under 55 years, 55 years and over) and <em class="v">preferred travel destination</em> (domestic, international) are'),
  [('Age','recorded in two groups (under 55, 55 and over), not as a number of years: categorical.'),('Destination','domestic or international names a group: categorical.')],
  'Both variables are <b>categorical</b>.',f'{EDR12} · 1A Q13 · VCAA 2021 Exam 1 Data analysis Q1 (examiner report)',
  stat=('mc',70),mc=['both categorical variables.','both numerical variables.','a numerical variable and a categorical variable respectively.','a categorical variable and a numerical variable respectively.','a discrete variable and a continuous variable respectively.'],
  key='A',dist=[70,3,21,4,2],dis=('C','21% chose this: they saw <em class="v">age</em> and assumed it was numerical. Here age is recorded in groups, so it is categorical.')))
# ================= APK 3: Edrolo U1&2 1A Q14 = VCAA 2020 E1 Q10
NT=('<table class="t" style="font-size:19px"><tr><th rowspan="2"></th><th colspan="2"><em>frequency of nightmares</em></th><th rowspan="2">Total</th></tr><tr><th>low</th><th>high</th></tr>'
    '<tr><td class="l" rowspan="2"><em>snores</em><br>no / yes</td><td>80</td><td>11</td><td>91</td></tr><tr><td>58</td><td>12</td><td>70</td></tr><tr><td class="l">Total</td><td>138</td><td>23</td><td>161</td></tr></table>')
NT=('<table class="t" style="font-size:19px"><tr><th></th><th colspan="2"><em>snores</em></th><th></th></tr><tr><th><em>frequency of nightmares</em></th><th>no</th><th>yes</th><th>total</th></tr>'
    '<tr><td class="l">low</td><td>80</td><td>58</td><td>138</td></tr><tr><td class="l">high</td><td>11</td><td>12</td><td>23</td></tr><tr><td class="l">total</td><td>91</td><td>70</td><td>161</td></tr></table>')
S.append(qslide('apk','APK · Edrolo U1&amp;2 1A Q14','And another',
  ('The data in the table shown was collected in a study of the association between the variables <em class="v">frequency of nightmares</em> (low, high) and <em class="v">snores</em> (no, yes).',NT,
   'The variables in this study, <em class="v">frequency of nightmares</em> (low, high) and <em class="v">snores</em> (no, yes), are'),
  [('Nightmares','low and high have a natural order: ordinal.'),('Snores','no and yes only name a group: nominal.')],
  '<em class="v">frequency of nightmares</em> is <b>ordinal</b> and <em class="v">snores</em> is <b>nominal</b>.',f'{EDR12} · 1A Q14 · VCAA 2020 Exam 1 Data analysis Q10 (examiner report)',
  stat=('mc',57),mc=['ordinal and nominal respectively.','nominal and ordinal respectively.','both numerical.','both ordinal.','both nominal.'],
  key='A',dist=[57,5,3,24,11],dis=('D','24% chose this: they treated no and yes as ordered. No and yes only name a group, so <em class="v">snores</em> is nominal.')))
# ================= Learn 1A: types of variable
TREE=('<div class="tree" style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px 18px;font-size:22px;text-align:center;width:1180px;margin:0 auto">'
  '<div class="frag key" style="grid-column:1/5;justify-self:center;padding:10px 40px"><b>Variable</b></div>'
  '<div class="frag key" style="grid-column:1/3;border-color:#1f9e74"><b>Categorical</b><br><small>names a quality or group</small></div>'
  '<div class="frag key" style="grid-column:3/5;border-color:#2f6fdf"><b>Numerical</b><br><small>a quantity: counted or measured</small></div>'
  '<div class="frag key"><b>Nominal</b><br><small>names only<br>e.g. eye colour, study mode</small></div>'
  '<div class="frag key"><b>Ordinal</b><br><small>names <i>and</i> orders<br>e.g. fitness level (1 high, 2 medium, 3 low)</small></div>'
  '<div class="frag key"><b>Discrete</b><br><small>‘How many?’ counted<br>e.g. cars in a car park</small></div>'
  '<div class="frag key"><b>Continuous</b><br><small>‘How much?’ measured<br>e.g. weight, height</small></div></div>')
S.append(learn('Learn · 1A','Types of variable',
  '<h4>Two types, each with two sub-types</h4><p>Categorical data put people into groups. Numerical data are quantities you can do arithmetic with.</p>',
  TREE,
  '<b>Not sure?</b> Can you average it? (average weight: yes · average house number: no). And check how it was recorded: weight in kg is numerical; ‘underweight, normal, overweight’ is categorical.',
  'Cambridge General Mathematics Units 3&amp;4, 1A pp. 2–4',
  cards=[kcard('Categorical','nominal (names) · ordinal (names and orders)'),kcard('Numerical','discrete (counted) · continuous (measured)')]))
# ================= WE1: Cambridge Example 1
S.append(qslide('we','Worked example 1 · 1A','Types of data',
  'Classify the following data as nominal, ordinal, discrete or continuous.'+plist([('a','The number of chocolate chips in each of 10 cookies is counted.'),
     ('b','The time taken for 20 students to complete a puzzle is recorded in seconds.'),
     ('c','Member of a football club were asked to rate how they felt about the current coach, 1 = Very satisfied, 2 = Satisfied, 3 = Indifferent, 4 = Dissatisfied, 5 = Very dissatisfied.'),
     ('d','Students are asked to each choose their preferred colour from the list 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow.'),
     ('e','Students weights were classified as ‘less than 60kg’, ‘60kg - 80kg’ or ‘more than 80kg’.')]),
  [],'',f'{CAM} · Example 1 (p. 4)',video='Cambridge GO · Example 1 (1A Resources)',cmd=('Classify',None,'one type for each'),
  parts=[('a','<b>Discrete</b>: the number of chips can only be a whole number.'),('b','<b>Continuous</b>: time can take any value, limited only by how accurately it is measured.'),
         ('c','<b>Ordinal</b>: the numbers are not quantities; they rank how much each person approves of the coach.'),
         ('d','<b>Nominal</b>: the numbers are not quantities; they just name colours.'),('e','<b>Ordinal</b>: weight was recorded in three groups that can be ordered.')]))
# ================= You try: Edrolo 1A WE1-3
YT1=('<div style="font-size:21px"><p><b>WE1</b> Classify the following variables as either categorical or numerical.</p>'+plist([('a.','<em class="v">type of pasta</em>'),('b.','<em class="v">number of candles</em>')])+
     '<p><b>WE2</b> Classify the following categorical variables as either nominal or ordinal.</p>'+plist([('a.','<em class="v">type of shoe</em> (runners, boots, sandals, slides)'),('b.','<em class="v">shirt size</em> (small, medium, large)')])+
     '<p><b>WE3</b> Classify the following numerical variables as either discrete or continuous.</p>'+plist([('a.','<em class="v">length</em> (m)'),('b.','<em class="v">number of tennis racquets</em>')])+'</div>')
S.append(qslide('yt','You try · Edrolo 1A WE1, WE2, WE3','Types of data',YT1,[],'',f'{EDR} · 1A Worked examples 1, 2 and 3 (pp. 2–4)',cmd=('Classify',None,'one type for each'),
  parts=[('1a','<b>Categorical</b>: grouped into pasta types.'),('1b','<b>Numerical</b>: candles are counted.'),('2a','<b>Nominal</b>: shoe types have no natural order.'),
         ('2b','<b>Ordinal</b>: small → medium → large.'),('3a','<b>Continuous</b>: length is measured and can be any value.'),('3b','<b>Discrete</b>: racquets are counted.')]))
# ================= CAS: setting up the statistics app (planner/cas-skills.json: stats-list)
CS=[x for x in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills'] if x['id']=='stats-list'][0]
yid=lambda u:u.split('v=')[1].split('&')[0]
SURV=table(['Height (cm)','Weight (kg)','Age (years)','Study mode','Fitness level','Pulse rate (beats/min)'],
  [[173,57,18,'C',2,86],[179,58,19,'C',2,82],[167,62,18,'C',1,96],[195,84,18,'O',1,71],[173,64,18,'C',3,90],[184,74,22,'O',3,78],[175,60,19,'O',3,88],[140,50,34,'C',3,70]],fs=17)
S.append(cas('CAS · 1A','Setting up the statistics app',
  'A university survey of eight students (Study mode: C = on-campus, O = online; Fitness level: 1 = high, 2 = medium, 3 = low).'+SURV+
  '<p>Enter the <em class="v">height</em> data into a list named <b>height</b>. Only numerical variables go into a list you calculate with.</p>',
  CS['ti'],CS['classpad'],'8 rows filled = 8 students. The list is ready for one-variable statistics (1D onwards).',
  'Cambridge General Mathematics Units 3&amp;4, 1A p. 2 (survey data) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in CS['videos']['ti']+CS['videos']['classpad']]))
# ================= Learn 1B: frequency table
STUDY='O O C O O O C O C C C O C O O O C C C O C O C O C C C O C O C O C O O O C O C O C O O O O O O C C O C O O O C O C C C O'.split()
S.append(learn('Learn · 1B','The frequency table',
  '<h4>Frequency table</h4><p>Lists each value of a variable with how often it occurs: as a number and as a percentage. It is the first step in making sense of raw data.</p>',
  letters('l3d',STUDY,22)+'<div class="frag" style="display:flex;justify-content:center;margin-top:10px">'+ftable('Study mode',[('on-campus (C)',27,'27/60 × 100 = 45.0'),('online (O)',33,'33/60 × 100 = 55.0')],(60,'100.0'))+'</div>',
  '<b>Total both columns.</b> The numbers must add to the number of values and the percentages to 100. Rounding can give 99.9 or 100.1: that is fine.',
  'Cambridge General Mathematics Units 3&amp;4, 1B p. 7 (study mode of 60 students)',
  frags=f'<span class="frag" data-mark="#l3d|{",".join(str(i) for i,v in enumerate(STUDY) if v=="C")}|q1m"></span>',
  cards=[kcard('Percentage frequency',FPCT)]))
# ================= WE2: Cambridge Example 2
ICE='C V V C C V C C C V V'.split()
S.append(qslide('we','Worked example 2 · 1B','Frequency table for a categorical variable',
  ('A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):',letters('w2d',ICE,30),
   'Construct a frequency table (including percentage frequencies) to display the data.'),
  [('Count','chocolate: 6 · vanilla: 5 · total: 6 + 5 = 11',f'data-mark="#w2d|{",".join(str(i) for i,v in enumerate(ICE) if v=="C")}|q1m"'),
   fx('Percentage frequency','% chocolate',F(FR([V('number','6')],[V('total','11')]),' × 100%'),'54.5%'),
   fx('Percentage frequency','% vanilla',F(FR([V('number','5')],[V('total','11')]),' × 100%'),'45.5%'),
   ('Check','6 + 5 = 11 and 54.5 + 45.5 = 100.0')],
  ftable('Flavour',[('chocolate',6,54.5),('vanilla',5,45.5)],(11,'100.0')),f'{CAM} · Example 2 (p. 7)',video='Cambridge GO · Example 2 (1B Resources)',cmd=('Construct',None,'numbers, percentages, totals')))
# ================= You try: Edrolo 1B WE1
TH='average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'.split()
S.append(qslide('yt','You try · Edrolo 1B WE1','Constructing a frequency table',
  ('The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:',
   '<div class="data" id="y2d" style="display:grid;grid-template-columns:repeat(6,auto);gap:2px 16px;font-size:19px;justify-content:center;font-family:inherit">'+''.join(f'<span data-i="{i}" style="padding:0 3px;border-radius:5px;border:1.5px solid transparent">{v}</span>' for i,v in enumerate(TH))+'</div>',
   'Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.'),
  [('Count','short 6 · average 10 · tall 8 · total 24',f'data-mark="#y2d|{",".join(str(i) for i,v in enumerate(TH) if v=="short")}|q1m"'),
   fx('Percentage frequency','% short',F(FR([V('number','6')],[V('total','24')]),' × 100'),'25.0'),
   fx('Percentage frequency','% average',F(FR([V('number','10')],[V('total','24')]),' × 100'),'41.7'),
   fx('Percentage frequency','% tall',F(FR([V('number','8')],[V('total','24')]),' × 100'),'33.3')],
  ftable('teacher’s height',[('short',6,'25.0'),('average',10,'41.7'),('tall',8,'33.3')],(24,'100.0')),f'{EDR} · 1B Worked example 1 (pp. 9–10)',cmd=('Create',None,'number and % columns, total row')))
# ================= Learn 1B: bar chart
S.append(learn('Learn · 1B','The bar chart',
  '<h4>Bar chart</h4><p>A picture of a frequency table, made for categorical data.</p><ul class="bul" style="font-size:20px;margin-left:24px"><li>frequency (or %) on the vertical axis</li><li>the variable on the horizontal axis</li><li>one bar per category, with gaps between them</li></ul>',
  '<div style="width:520px;margin:0 auto">'+bar('l4b',{"cats":["on-campus","online"],"v":[27,33],"max":35,"step":5,"xl":"Study mode","yl":"Frequency","h":330},True)+'</div>',
  '<b>Gaps matter.</b> They show each category is separate. A histogram (numerical data, 1C) has no gaps.',
  'Cambridge General Mathematics Units 3&amp;4, 1B p. 8 · Data: 1B p. 7',
  frags='<span class="frag" data-bar="0"></span><span class="frag" data-bar="1"></span>'))
# ================= WE3: Cambridge Example 3
CLIM=ftable('Climate type',[('Cold',3,'13.0'),('Mild',14,'60.9'),('Hot',6,'26.1')],(23,'100.0'))
S.append(qslide('we','Worked example 3 · 1B','Constructing a bar chart from a frequency table',
  'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.'+f'<div class="fig">{CLIM}</div>'+
  plist([('a','What is the level of measurement of the variable <em class="v">climate type</em>?'),('b','Construct a frequency bar chart to display this information.')]),
  [('a','the groups can be put in a natural order of ‘warmth’: cold, mild, hot. The variable is <b>ordinal</b>.')],
  '<b>b</b>',f'{CAM} · Example 3 (p. 8)',video='Cambridge GO · Example 3 (1B Resources)',cmd=('Construct',None,'labelled axes, bars with gaps'),
  afig='<div style="width:520px">'+bar('w3b',{"cats":["Cold","Mild","Hot"],"v":[3,14,6],"max":15,"step":5,"xl":"Climate type","yl":"Frequency","h":330},True)+'</div>',
  build=[('1 Horizontal axis: <em>Climate type</em>, three equal intervals. Vertical axis: <em>Frequency</em>, scaled to 15.',''),
         ('2 Cold: bar of height 3','data-bar="0"'),('3 Mild: bar of height 14 (gaps between bars)','data-bar="1"'),('4 Hot: bar of height 6','data-bar="2"')]))
# ================= You try: Edrolo 1B WE2
TT=ftable('teacher’s height',[('short',6,'25.0'),('average',10,'41.7'),('tall',8,'33.3')],(24,'100.0'))
S.append(qslide('yt','You try · Edrolo 1B WE2','Constructing a bar chart',
  ('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.',TT,
   'Use the frequency table to construct a frequency bar chart.'),
  [('Axes','frequency on the vertical axis (up to at least 10), <em>teacher’s height</em> on the horizontal axis.')],
  'The bar chart:',f'{EDR} · 1B Worked example 2 (p. 11)',cmd=('Construct',None,'labelled axes, bars with gaps'),
  afig='<div style="width:520px">'+bar('y3b',{"cats":["short","average","tall"],"v":[6,10,8],"max":10,"step":2,"xl":"teacher’s height","yl":"frequency","h":330},True)+'</div>',
  build=[('short: 6','data-bar="0"'),('average: 10','data-bar="1"'),('tall: 8','data-bar="2"')]))
# ================= Learn 1B: segmented bar chart
S.append(learn('Learn · 1B','The segmented bar chart',
  '<h4>Segmented bar chart</h4><p>The bars are stacked into one bar, a segment per category, with a legend. In a <b>percentage</b> segmented bar chart each segment is its %, so the bar is 100% tall.</p>',
  '<div class="row" style="gap:60px;justify-content:center"><div style="width:420px">'+seg('l5f',{"bars":[{"v":[12,56,24]}],"names":["Cold","Mild","Hot"],"legendTop":["Hot","Mild","Cold"],"yl":"Frequency","scale":25,"ticks":20,"h":270})+
  '</div><div class="frag" style="width:420px">'+seg('l5p',{"bars":[{"v":[13.0,60.9,26.1]}],"names":["Cold","Mild","Hot"],"legendTop":["Hot","Mild","Cold"],"yl":"Percentage","ticks":10,"h":270})+'</div></div>',
  '<b>Segment ends:</b> add the percentages as you go up: 13.0, then 13.0 + 60.9 = 73.9, then 100.',
  'Cambridge General Mathematics Units 3&amp;4, 1B p. 9 (climate data, Example 3)',cards=[kcard('Segmented bar',FSEG)]))
# ================= WE4: Cambridge Example 4
S.append(qslide('we','Worked example 4 · 1B','Constructing a percentage segmented bar chart from a frequency table',
  ('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’.',CLIM,'Construct a percentage frequency segmented bar chart to display this information.'),
  [('Axes','no label on the horizontal axis. Vertical axis: <em>Percentage</em>, 0 to 100 in tens.'),
   ('Ends','Cold ends at 13.0 · Mild ends at 13.0 + 60.9 = 73.9 · Hot ends at 100')],
  'The percentage segmented bar chart:',f'{CAM} · Example 4 (p. 9)',video='Cambridge GO · Example 4 (1B Resources)',cmd=('Construct',None,'one 100% bar, segments, legend'),
  afig='<div style="width:440px">'+seg('w4s',{"bars":[{"v":[13.0,60.9,26.1]}],"names":["Cold","Mild","Hot"],"legendTop":["Hot","Mild","Cold"],"yl":"Percentage","ticks":10,"h":330},True)+'</div>',
  build=[('Cold: 0 to 13.0','data-act="seg0"'),('Mild: 13.0 to 73.9','data-act="seg1"'),('Hot: 73.9 to 100, then the legend','data-act="seg2"')]))
# ================= You try: Edrolo 1B WE3
S.append(qslide('yt','You try · Edrolo 1B WE3','Constructing segmented bar charts',
  '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.'+f'<div class="fig">{TT}</div>'+
  plist([('a.','Use the frequency table to construct a segmented bar chart.'),('b.','Use the frequency table to construct a percentage segmented bar chart.')]),
  [],'',f'{EDR} · 1B Worked example 3 (pp. 12–13)',cmd=('Construct',None,'segments, legend'),
  parts=[('a.','Segments end at 6, 6 + 10 = 16 and 16 + 8 = 24.<div style="width:330px">'+seg('y4a',{"bars":[{"v":[25,41.67,33.33]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency","xl":"teacher’s height","scale":24,"ticks":25,"h":300})+'</div>'),
         ('b.','Segments end at 25, 25 + 41.7 = 66.7 and 100.<div style="width:330px">'+seg('y4b',{"bars":[{"v":[25,41.7,33.3]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency (%)","xl":"teacher’s height","ticks":20,"h":300})+'</div>')]))
# ================= Learn 1B: describing the distribution
S.append(learn('Learn · 1B','Describing the distribution of a categorical variable',
  '<h4>Writing a report</h4><ul class="bul" style="font-size:20px;margin-left:24px"><li>the context and how many individuals</li><li>the modal category, if there is a clear one</li><li>percentages (preferred to counts)</li><li>with many categories, you don’t need them all, but always give the mode</li></ul>',
  '<div style="width:420px;margin:0 auto">'+seg('l6p',{"bars":[{"v":[13.0,60.9,26.1]}],"names":["Cold","Mild","Hot"],"legendTop":["Hot","Mild","Cold"],"yl":"Percentage","ticks":10,"h":330})+'</div>',
  '<b>Majority</b> means more than 50%. If the mode is 50% or less, say ‘the most common’ instead.',
  'Cambridge General Mathematics Units 3&amp;4, 1B pp. 9–10',cards=[kcard('Mode','the most frequent category: tallest bar or longest segment')]))
# ================= WE5: Cambridge Example 5
CLIM5=ftable('Climate type',[('Cold',3,'13.0'),('Mild',14,'60.9'),('Hot',6,'26.1')],(23,'100.0')).replace('<th>Percentage</th>','<th>%</th>')
S.append(qslide('we','Worked example 5 · 1B','Describing the distribution of a categorical variable',
  ('In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages.',CLIM5,
   'Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.'),
  [('Context','23 countries; climate type cold, mild or hot.'),('Mode','Mild, 60.9%: more than 50%, so ‘the majority’.'),('Others','hot 26.1%, cold 13.0%')],
  'The climate types of 23 countries were classified as being ‘cold’, ‘mild’ or ‘hot’. The majority of the countries, 60.9%, were found to have a mild climate. Of the remaining countries, 26.1% were found to have a hot climate, while 13.0% were found to have a cold climate.',
  f'{CAM} · Example 5 (pp. 10–11)',video='Cambridge GO · Example 5 (1B Resources)',cmd=('Write',None,'context, mode, percentages')))
# ================= You try: Edrolo 1B WE4
S.append(qslide('yt','You try · Edrolo 1B WE4','Describing the distribution',
  '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.'+
  '<div class="fig" style="width:380px;margin:0 auto">'+seg('y5s',{"bars":[{"v":[25,41.7,33.3]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency (%)","xl":"teacher’s height","ticks":20,"h":290})+'</div>'+
  plist([('a.','Find the modal category of the data set.'),('b.','Describe the distribution of the data set.')]),
  [],'',f'{EDR} · 1B Worked example 4 (p. 14)',cmd=('Describe',None,'context, mode, percentages'),
  parts=[('a.','<b>Average</b>: the tallest segment (41.7%).'),
         ('b.','24 prep students were surveyed on how tall they thought their teacher was. The most common response was average, accounting for 41.7% of responses, while 25% said their teacher was short, and 33.3% said their teacher was tall.')]))
# ================= Exits
DAY=list(range(1,16)); TMP=[12.7,11.8,10.7,9.0,6.0,7.0,4.1,4.8,9.2,6.7,7.5,8.0,8.6,9.8,7.7]
def tt1(ix): return ('<table class="t" style="font-size:16px;margin:4px auto"><tr><td class="l"><em>day number</em></td>'+''.join(f'<td>{DAY[i]}</td>' for i in ix)+'</tr><tr><td class="l"><em>minimum temperature</em> (°C)</td>'+''.join(f'<td>{TMP[i]}</td>' for i in ix)+'</tr></table>')
TT1='<div style="display:flex;flex-direction:column;gap:6px">'+tt1(range(8))+tt1(range(8,15))+'</div>'
S.append(qslide('ex','Exit task 1 of 3 · Edrolo U3&amp;4 1A Q14','Show what you know',
  ('The table shows the <em class="v">day number</em> and the <em class="v">minimum temperature</em>, in degrees Celsius, for 15 consecutive days in May 2017.',TT1,
   'Which of the two variables in this data set is an ordinal variable? <span class="muted">(1 mark)</span>'),
  [('Temperature','measured in °C: numerical.'),('Day number','labels each day and puts the days in order; you wouldn’t average it: categorical, ordinal.')],
  '<em class="v">day number</em> is the ordinal variable.',f'{EDR} · 1A Q14 · VCAA 2019 Exam 2 Data analysis Q1a (examiner report)',
  stat=('mark',83),cmd=('Which',1,'name the variable')))
HEP=[(1,1.76,15.34,41.22),(2,1.79,16.96,42.41),(3,1.83,13.87,46.53),(4,1.82,14.23,40.53),(5,1.87,13.78,40.62),(6,1.73,14.50,45.62),(7,1.68,15.08,42.33),(8,1.82,13.13,40.88),
     (9,1.83,14.22,39.22),(10,1.87,13.62,42.51),(11,1.87,12.01,42.75),(12,1.80,12.88,38.12),(13,1.83,12.68,42.65),(14,1.87,12.45,41.32),(15,1.78,11.31,42.88)]
HT=lambda rows:table(['<em>athlete number</em>','<em>high jump</em> (metres)','<em>shot-put</em> (metres)','<em>javelin</em> (metres)'],[[a,f'{b:.2f}',f'{c:.2f}',f'{d:.2f}'] for a,b,c,d in rows],fs=13,extra='line-height:1').replace('<td','<td style="padding:1px 5px"').replace('<th>','<th style="padding:2px 4px">')
S.append(qslide('ex','Exit task 2 of 3 · Edrolo U3&amp;4 1A Q16','Show what you know',
  ('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.',
   f'<div class="row" style="gap:16px;justify-content:center">{HT(HEP[:8])}{HT(HEP[8:])}</div>',
   'Write down the number of numerical variables in the table. <span class="muted">(1 mark)</span>'),
  [('Measured','<em>high jump</em>, <em>shot-put</em> and <em>javelin</em> are measured in metres: numerical.'),('Label','<em>athlete number</em> only names each athlete: categorical.')],
  'There are <b>3</b> numerical variables.',f'{EDR} · 1A Q16 · VCAA 2021 Exam 2 Data analysis Q1a (examiner report: a common error was counting the 45 values)',
  stat=('mark',52),cmd=('Write',1,'just the number')))
S.append(qslide('ex','Exit task 3 of 3 · Edrolo U3&amp;4 1B Q13','Show what you know',
  ('A study was conducted that investigated the <em class="v">number of moths</em> caught in a sugar moth trap (less than 250, 250–500, more than 500). The results are summarised in the percentage segmented bar chart shown.',
   '<div style="width:380px;margin:0 auto">'+seg('e3s',{"bars":[{"v":[30,46,24]}],"names":["less than 250","250–500","more than 500"],"legendTop":["less than 250","250–500","more than 500"],"yl":"frequency (%)","xl":"number of moths","ticks":10,"h":250})+'</div>',
   'There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to'),
  [('Read','the ‘less than 250’ segment runs from 0 to 30%.'),
   fx('Number from a percentage',None,F(FR([V('percentage','30')],['100']),' × ',V('total','300')),'90')],
  '<b>90</b> sugar traps caught less than 250 moths.',f'{EDR} · 1B Q13 · Adapted from VCAA 2017 Exam 1 Data analysis Q5 (examiner report, original question)',
  stat=('mc',76),mc=['30','90','250','300','500'],key='B',dist=[21,76,2,1,1],
  dis=('A','21% chose this on the original: they read 30% off the chart as 30 traps, instead of finding 30% of 300.')))
# ================= closing
S.append(checkin(SC))
S.append(coursework([('1A Types of data','Cambridge Exercise 1A: Q1–6'),('1B Displaying and describing categorical data','Cambridge Exercise 1B: Q1–9')]))
V=json.load(open(os.path.join(ROOT,'planner','videos.json'))); V=V if isinstance(V,list) else V.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V if v['sub'] in ('1A','1B')]))
n=assemble(S,'12MAG · S1 · Types of data and categorical data',os.path.join(ROOT,'lessons','S1-slides.html'))
print(n,'slides')
