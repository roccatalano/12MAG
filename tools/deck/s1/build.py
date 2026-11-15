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
import tpl as TPL
def G(pre,fig,post=''):
    # question text, figure, question line: stacked with normal spacing (no stretched gap)
    return f'<div>{pre}</div><div style="margin:14px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'):
    # a blank in an answer template: dashed line until a step fills it (data-fill="cls")
    return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def fttab(var,rows,total,rid='',pct=True,fs=19,pcth='Percentage'):
    # frequency table; rows/total may hold B(...) blanks. Each row carries data-i so steps can highlight it.
    h=f'<tr><th rowspan="2">{var}</th><th colspan="{2 if pct else 1}">Frequency</th></tr><tr><th>Number</th>'+(f'<th>{pcth}</th>' if pct else '')+'</tr>'
    tr=''.join(f'<tr><td class="l"><span data-i="{i}">{a}</span></td><td><span data-i="{i}">{b}</span></td>'+(f'<td><span data-i="{i}">{c}</span></td>' if pct else '')+'</tr>' for i,(a,b,c) in enumerate(rows))
    k=len(rows)
    return (f'<table class="t" id="{rid}" style="font-size:{fs}px"><thead>{h}</thead>{tr}<tr><td class="l"><b><span data-i="{k}">Total</span></b></td><td><b><span data-i="{k}">{total[0]}</span></b></td>'
            +(f'<td><b><span data-i="{k}">{total[1]}</span></b></td>' if pct else '')+'</tr></table>')
def cone(flavour,letter,i):
    # ice-cream cone icon (chocolate / vanilla) with its data letter
    col={'C':('#7a4a24','#fff'),'V':('#f6e7b0','#5a4a12')}[letter]
    return (f'<span data-i="{i}" style="display:inline-flex;flex-direction:column;align-items:center;padding:4px 3px;border-radius:8px"><svg width="40" height="58" viewBox="0 0 40 58">'
            f'<path d="M8 24 L20 56 L32 24 Z" fill="#e0a85a" stroke="#a8742c" stroke-width="1.5"/><path d="M11 30 L29 30 M13 36 L27 36 M15 42 L25 42" stroke="#a8742c" stroke-width="1"/>'
            f'<circle cx="20" cy="17" r="14" fill="{col[0]}" stroke="#5c3a1c" stroke-width="1.2"/><text x="20" y="23" text-anchor="middle" font-size="16" font-weight="800" fill="{col[1]}">{letter}</text></svg></span>')
def stepsH(cards):
    # horizontal numbered step cards (engine .stepsH/.sc): (title, body, frag attrs)
    return '<div class="stepsH">'+''.join(f'<div class="sc"><div class="n">{k}</div><div class="frag" {a}><div class="st">{t}</div><div class="sb">{b}</div></div></div>' for k,(t,b,a) in enumerate(cards,1))+'</div>'
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
S.append(qslide('apk','APK · VCAA 2021 Exam 1 Q1','A real VCAA question you can already do',
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
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q10','And another',
  ('The data in the table shown was collected in a study of the association between the variables <em class="v">frequency of nightmares</em> (low, high) and <em class="v">snores</em> (no, yes).',NT,
   'The variables in this study, <em class="v">frequency of nightmares</em> (low, high) and <em class="v">snores</em> (no, yes), are'),
  [('Nightmares','low and high have a natural order: ordinal.'),('Snores','no and yes only name a group: nominal.')],
  '<em class="v">frequency of nightmares</em> is <b>ordinal</b> and <em class="v">snores</em> is <b>nominal</b>.',f'{EDR12} · 1A Q14 · VCAA 2020 Exam 1 Data analysis Q10 (examiner report)',
  stat=('mc',57),mc=['ordinal and nominal respectively.','nominal and ordinal respectively.','both numerical.','both ordinal.','both nominal.'],
  key='A',dist=[57,5,3,24,11],dis=('D','24% chose this: they treated no and yes as ordered. No and yes only name a group, so <em class="v">snores</em> is nominal.')))
# ================= Learn 1A: types of variable
W=1180;cw=(W-54)/4;cx=[cw/2+k*(cw+18) for k in range(4)];cat=(cx[0]+cx[1])/2;num=(cx[2]+cx[3])/2
def arrows(pairs,h=30):
    l=''.join(f'<line x1="{a}" y1="2" x2="{b}" y2="{h-6}" stroke="#5a6170" stroke-width="2.5" marker-end="url(#ah)"/>' for a,b in pairs)
    return f'<svg width="{W}" height="{h}" style="display:block"><defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5a6170"/></marker></defs>{l}</svg>'
TREE=(f'<div style="width:{W}px;margin:0 auto;font-size:20px;line-height:1.25;text-align:center">'
  '<div class="key" style="width:300px;margin:0 auto;padding:8px 20px"><b>Variable</b></div>'
  f'<div class="frag" data-s="t1">{arrows([(W/2,cat),(W/2,num)])}</div>'
  '<div class="frag" data-s="t1" style="display:grid;grid-template-columns:1fr 1fr;gap:18px">'
  '<div class="key" style="border-color:#1f9e74"><b>Categorical</b><br><small>names a quality or group</small></div>'
  '<div class="key" style="border-color:#2f6fdf"><b>Numerical</b><br><small>a quantity: counted or measured</small></div></div>'
  f'<div class="frag" data-s="t2">{arrows([(cat,cx[0]),(cat,cx[1]),(num,cx[2]),(num,cx[3])])}</div>'
  '<div class="frag" data-s="t2" style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px">'
  '<div class="key"><b>Nominal</b><br><small>names only · e.g. eye colour</small></div>'
  '<div class="key"><b>Ordinal</b><br><small>names <i>and</i> orders · e.g. fitness level</small></div>'
  '<div class="key"><b>Discrete</b><br><small>‘How many?’ counted · e.g. cars</small></div>'
  '<div class="key"><b>Continuous</b><br><small>‘How much?’ measured · e.g. weight</small></div></div></div>')
S.append(learn('Learn · 1A','Types of variable',
  '<h4>Two types, each with two sub-types</h4><p>Categorical data put people into groups. Numerical data are quantities you can do arithmetic with.</p>',
  TREE,
  '<b>Not sure? Two tests</b><div style="display:grid;grid-template-columns:1fr 1fr;gap:4px 30px;margin-top:4px"><div><b>1 · Does an average make sense?</b><br>average weight ✓ → numerical<br>average house number ✗ → categorical</div><div><b>2 · How was it recorded?</b><br>weight in kg → numerical<br>‘underweight’, ‘normal’, ‘overweight’ → categorical</div></div>',
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
YT1=('<div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly;font-size:23px;line-height:1.4">'+
 '<div data-pks="0,1"><p style="display:flex;gap:12px;margin:0 0 6px"><b style="min-width:22px">1</b><span>Classify the following variables as either categorical or numerical.</span></p>'+plist([('a.','<em class="v">type of pasta</em>'),('b.','<em class="v">number of candles</em>')]).replace('<ol class="parts">','<ol class="parts" style="margin-left:34px">')+'</div>'+
 '<div data-pks="2,3"><p style="display:flex;gap:12px;margin:0 0 6px"><b style="min-width:22px">2</b><span>Classify the following categorical variables as either nominal or ordinal.</span></p>'+plist([('a.','<em class="v">type of shoe</em> (runners, boots, sandals, slides)'),('b.','<em class="v">shirt size</em> (small, medium, large)')]).replace('<ol class="parts">','<ol class="parts" style="margin-left:34px">')+'</div>'+
 '<div data-pks="4,5"><p style="display:flex;gap:12px;margin:0 0 6px"><b style="min-width:22px">3</b><span>Classify the following numerical variables as either discrete or continuous.</span></p>'+plist([('a.','<em class="v">length</em> (m)'),('b.','<em class="v">number of tennis racquets</em>')]).replace('<ol class="parts">','<ol class="parts" style="margin-left:34px">')+'</div>'+'</div>')
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
# ================= Learn 1B: frequency table (the original design: tally the data into the table)
STUDY='O O C O O O C O C C C O C O O O C C C O C O C O C C C O C O C O C O O O C O C O C O O O O O O C C O C O O O C O C C C O'.split()
CHIPS='<div class="chips">'+''.join(f'<div class="chip" data-v="{v}">{"campus" if v=="C" else "online"}</div>' for v in STUDY)+'</div>'
def ftcells(fs=25,pct=True,cells=(1,2,3,4,5,6)):
    c1,c2,c3,c4,c5,c6=cells
    return (f'<table class="t ft" style="font-size:{fs}px;width:100%"><tr><th rowspan="2" class="l"><em class="v">study mode</em></th><th colspan="{2 if pct else 1}">Frequency</th></tr><tr><th>Number</th>'+('<th>%</th>' if pct else '')+'</tr>'
      f'<tr data-part="campus"><td class="l"><span class="cell" data-c="{c1}">on-campus</span></td><td><b class="cell" data-c="{c2}" id="nC"></b></td>'+(f'<td><span class="cell" data-c="{c4}">45.0</span></td>' if pct else '')+'</tr>'
      f'<tr data-part="online"><td class="l"><span class="cell" data-c="{c1}">online</span></td><td><b class="cell" data-c="{c2}" id="nO"></b></td>'+(f'<td><span class="cell" data-c="{c5}">55.0</span></td>' if pct else '')+'</tr>'
      f'<tr class="tot" data-part="total"><td class="l">Total</td><td><span class="cell" data-c="{c3}">60</span></td>'+(f'<td><span class="cell" data-c="{c6}">100.0</span></td>' if pct else '')+'</tr></table>')
body=('<p class="muted" style="font-size:22px;margin:0 0 12px">A <b>frequency table</b> lists each category and how often it occurs: as a number and as a percentage. Here: the <em class="v">study mode</em> (C = on-campus, O = online) of 60 students.</p>'
  f'<div class="row" style="gap:34px"><div style="flex:1.3">{CHIPS}</div><div style="flex:.85">{ftcells()}'
  f'<div class="kf frag" data-s="f12" style="margin-top:14px"><span class="kn">Percentage frequency</span><span class="kx" style="font-size:21px">{FPCT}</span></div></div></div>'
  +stepsH([('Set up the table','One row for each category.',''),('Count','Count each category.','data-act="tally"'),('Total','27 + 33 = 60','data-p="total"'),
           ('% on-campus','27/60 × 100% = 45.0%','data-p="campus" data-s="f12"'),('% online','33/60 × 100% = 55.0%','data-p="online"'),('Check','45.0 + 55.0 = 100%','data-p="campus online total"')]))
S.append(TPL._frame('learn','Learn · 1B','From raw data to a frequency table',body,'Cambridge General Mathematics Units 3&amp;4, 1B p. 7 (study mode of 60 students)',cfu='disc'))
# ================= WE2: Cambridge Example 2 (answer template filled step by step)
ICE='C V V C C V C C C V V'.split()
CONES='<div id="w2d" style="display:flex;gap:4px;justify-content:center;flex-wrap:wrap">'+''.join(cone('',v,i) for i,v in enumerate(ICE))+'</div>'
iC=','.join(str(i) for i,v in enumerate(ICE) if v=='C'); iV=','.join(str(i) for i,v in enumerate(ICE) if v=='V')
S.append(qslide('we','Worked example 2 · 1B','Frequency table for a categorical variable',
  G('A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):',CONES,
    'Construct a frequency table (including percentage frequencies) to display the data.'),
  [('Count chocolate','6 C cones',f'data-hi="#w2d|{iC}|hc" data-fill="c1"'),
   ('Count vanilla','5 V cones',f'data-hi="#w2d|{iV}|hv" data-fill="c2"'),
   ('Total','6 + 5 = 11','data-hi="#w2d||" data-fill="c3"'),
   fx('Percentage frequency','% chocolate',F(FR([V('number','6')],[V('total','11')]),' × 100%'),'54.5%',ra='data-fill="c4"'),
   fx('Percentage frequency','% vanilla',F(FR([V('number','5')],[V('total','11')]),' × 100%'),'45.5%',ra='data-fill="c5"'),
   ('Check','54.5 + 45.5 = 100.0','data-fill="c6"'),
   ('TMPL',fttab('Flavour',[('chocolate',B('c1',6),B('c4','54.5')),('vanilla',B('c2',5),B('c5','45.5'))],(B('c3',11),B('c6','100.0'))))],
  '',f'{CAM} · Example 2 (p. 7)',video='Cambridge GO · Example 2 (1B Resources)',cmd=('Construct',None,'numbers, percentages, totals')))
# ================= You try: Edrolo 1B WE1
TH='average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'.split()
WORDS='<div id="y2d" style="display:grid;grid-template-columns:repeat(6,auto);gap:4px 18px;font-size:20px;justify-content:center">'+''.join(f'<span data-i="{i}" style="padding:1px 5px">{v}</span>' for i,v in enumerate(TH))+'</div>'
ix=lambda w:','.join(str(i) for i,v in enumerate(TH) if v==w)
S.append(qslide('yt','You try · Edrolo 1B WE1','Constructing a frequency table',
  G('The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:',WORDS,
    'Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.'),
  [('Count short','6',f'data-hi="#y2d|{ix("short")}|hy" data-fill="s1"'),('Count average','10',f'data-hi="#y2d|{ix("average")}|hb" data-fill="s2"'),
   ('Count tall','8 · total 6 + 10 + 8 = 24',f'data-hi="#y2d|{ix("tall")}|hg" data-fill="s3"'),
   ('% short','6/24 × 100 = 25.0','data-hi="#y2d||" data-fill="p1"'),('% average','10/24 × 100 = 41.7','data-fill="p2"'),
   ('% tall','8/24 × 100 = 33.3 · check: 25.0 + 41.7 + 33.3 = 100.0','data-fill="p3"'),
   ('TMPL',fttab('teacher’s height',[('short',B('s1',6),B('p1','25.0')),('average',B('s2',10),B('p2','41.7')),('tall',B('s3',8),B('p3','33.3'))],(B('s3',24),B('p3','100.0')),pcth='%',fs=17))],
  '',f'{EDR} · 1B Worked example 1 (pp. 9–10)',cmd=('Create',None,'number and % columns, total row')))
# ================= Learn 1B: bar chart (data -> frequency table -> graph)
CH2='<div class="chips" style="grid-template-columns:repeat(12,1fr)">'+''.join(f'<div class="chip" data-v="{v}" style="font-size:12px">{"campus" if v=="C" else "online"}</div>' for v in STUDY)+'</div>'
body=('<div class="row" style="gap:28px;align-items:stretch"><div class="key" style="flex:1"><h4>Data → frequency table</h4>'+CH2+
  '<div style="margin-top:12px">'+ftcells(21,pct=False,cells=(1,1,2,0,0,0))+'</div></div>'
  '<div class="key" style="flex:1"><h4>Frequency table → bar chart</h4><div style="width:520px;margin:0 auto">'+
  bar('l4b',{"cats":["on-campus","online"],"v":[27,33],"max":35,"step":5,"xl":"Study mode","yl":"Frequency","h":320},True)+'</div></div></div>'
  +stepsH([('Count','Tally each category into the table.','data-act="tally"'),('Total','27 + 33 = 60','data-p="total"'),
           ('Axes','Study mode across, Frequency up (to 35).',''),('on-campus','A bar 27 high.','data-bar="0" data-p="campus"'),('online','A bar 33 high, with a gap.','data-bar="1" data-p="campus online total"')]))
S.append(TPL._frame('learn','Learn · 1B','The bar chart: data → frequency table → graph',body,'Cambridge General Mathematics Units 3&amp;4, 1B pp. 7–8 (study mode of 60 students)',cfu='disc'))
# ================= WE3: Cambridge Example 3
CLIMR=[('Cold',3,'13.0'),('Mild',14,'60.9'),('Hot',6,'26.1')]
S.append(qslide('we','Worked example 3 · 1B','Constructing a bar chart from a frequency table',
  'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.'+
  f'<div style="margin:12px 0">{fttab("Climate type",CLIMR,(23,"100.0"),rid="w3t")}</div>'+
  plist([('a','What is the level of measurement of the variable <em class="v">climate type</em>?'),('b','Construct a frequency bar chart to display this information.')]),
  [('Order?','cold, mild, hot can be put in a natural order of ‘warmth’.','data-pk="0"'),('ANS','<b>a</b> &nbsp;Ordinal'),
   ('Axes','<em>Climate type</em> across (three equal intervals); <em>Frequency</em> up, scaled to 15.','data-pk="1" data-hi="#w3t||"'),
   ('Cold','bar of height 3','data-pk="1" data-hi="#w3t|0|hy" data-grow="#w3b|0"'),('Mild','bar of height 14, with gaps between bars','data-pk="1" data-hi="#w3t|1|hy" data-grow="#w3b|1"'),
   ('Hot','bar of height 6','data-pk="1" data-hi="#w3t|2|hy" data-grow="#w3b|2"'),
   ('TMPL','<b>b</b><div style="width:430px;margin-top:6px">'+bar('w3b',{"cats":["Cold","Mild","Hot"],"v":[3,14,6],"max":15,"step":5,"xl":"Climate type","yl":"Frequency","h":300},True)+'</div>')],
  '',f'{CAM} · Example 3 (p. 8)',video='Cambridge GO · Example 3 (1B Resources)',cmd=('Construct',None,'labelled axes, bars with gaps')))
# ================= You try: Edrolo 1B WE2
THR=[('short',6,'25.0'),('average',10,'41.7'),('tall',8,'33.3')]
S.append(qslide('yt','You try · Edrolo 1B WE2','Constructing a bar chart',
  G('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.',
    fttab('teacher’s height',THR,(24,'100.0'),rid='y3t',pcth='%'),'Use the frequency table to construct a frequency bar chart.'),
  [('Axes','frequency up (to at least 10); <em>teacher’s height</em> across.'),('short','bar of height 6','data-hi="#y3t|0|hy" data-grow="#y3b|0"'),
   ('average','bar of height 10','data-hi="#y3t|1|hy" data-grow="#y3b|1"'),('tall','bar of height 8','data-hi="#y3t|2|hy" data-grow="#y3b|2"'),
   ('TMPL','<div style="width:430px">'+bar('y3b',{"cats":["short","average","tall"],"v":[6,10,8],"max":10,"step":2,"xl":"teacher’s height","yl":"frequency","h":300},True)+'</div>')],
  '',f'{EDR} · 1B Worked example 2 (p. 11)',cmd=('Construct',None,'labelled axes, bars with gaps')))
# ================= Learn 1B: segmented bar chart (table -> bars -> stacked -> percentage)
body=('<div class="row" style="gap:30px;align-items:stretch"><div style="flex:.8;display:flex;flex-direction:column;gap:16px">'
  f'<div class="key"><h4>Climate type of 23 countries</h4>{fttab("Climate type",CLIMR,(23,"100.0"),rid="l5t",fs=18)}</div>'
  '<div class="key frag" data-act="stack"><h4>1 · Stack the bars</h4><p style="font-size:21px">Same frequencies, one on top of the other: a <b>segmented bar chart</b>. The total height is 23.</p></div>'
  '<div class="key frag" data-act="pct"><h4>2 · Convert to percentages</h4><p style="font-size:21px">Each segment becomes its %, so the bar is exactly 100% tall: a <b>percentage segmented bar chart</b>. Segment ends: 13.0 · 13.0 + 60.9 = 73.9 · 100.</p></div></div>'
  '<div class="key" style="flex:1.2"><div class="chart" id="morph" style="height:450px;padding:0"></div></div></div>')
S.append(TPL._frame('learn','Learn · 1B','From a bar chart to a segmented bar chart',body,'Cambridge General Mathematics Units 3&amp;4, 1B pp. 8–9 (climate data, Example 3)',cfu='disc'))
# ================= WE4: Cambridge Example 4
S.append(qslide('we','Worked example 4 · 1B','Constructing a percentage segmented bar chart from a frequency table',
  G('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’.',fttab('Climate type',CLIMR,(23,'100.0'),rid='w4t'),'Construct a percentage frequency segmented bar chart to display this information.'),
  [('Axes','no label on the horizontal axis. Vertical axis: <em>Percentage</em>, 0 to 100 in tens.'),
   ('Cold','from 0 to 13.0%','data-hi="#w4t|0|hy" data-grow="#w4s|0"'),('Mild','from 13.0 to 13.0 + 60.9 = 73.9%','data-hi="#w4t|1|hy" data-grow="#w4s|1"'),
   ('Hot','from 73.9 to 100%; add the legend','data-hi="#w4t|2|hy" data-grow="#w4s|2" data-lg'),
   ('TMPL','<div style="width:400px">'+seg('w4s',{"bars":[{"v":[13.0,60.9,26.1]}],"names":["Cold","Mild","Hot"],"legendTop":["Hot","Mild","Cold"],"yl":"Percentage","ticks":10,"h":320},True)+'</div>')],
  '',f'{CAM} · Example 4 (p. 9)',video='Cambridge GO · Example 4 (1B Resources)',cmd=('Construct',None,'one 100% bar, segments, legend')))
# ================= You try: Edrolo 1B WE3
S.append(qslide('yt','You try · Edrolo 1B WE3','Constructing segmented bar charts',
  '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.'+
  f'<div style="margin:12px 0">{fttab("teacher’s height",THR,(24,"100.0"),rid="y4t",pcth="%")}</div>'+
  plist([('a.','Use the frequency table to construct a segmented bar chart.'),('b.','Use the frequency table to construct a percentage segmented bar chart.')]),
  [('short','ends at 6','data-pk="0" data-hi="#y4t|0|hy" data-grow="#y4a|0"'),('average','ends at 6 + 10 = 16','data-pk="0" data-hi="#y4t|1|hy" data-grow="#y4a|1"'),
   ('tall','ends at 16 + 8 = 24; add the legend','data-pk="0" data-hi="#y4t|2|hy" data-grow="#y4a|2" data-lg'),
   ('TMPL','<div style="display:flex;gap:14px;align-items:center"><b>a.</b><div style="width:260px">'+seg('y4a',{"bars":[{"v":[25,41.67,33.33]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency","xl":"teacher’s height","scale":24,"ticks":25,"h":185},True)+'</div></div>'),
   ('short','ends at 25%','data-pk="1" data-hi="#y4t|0|hy" data-grow="#y4b|0"'),('average','ends at 25 + 41.7 = 66.7%','data-pk="1" data-hi="#y4t|1|hy" data-grow="#y4b|1"'),
   ('tall','ends at 100%; add the legend','data-pk="1" data-hi="#y4t|2|hy" data-grow="#y4b|2" data-lg'),
   ('TMPL','<div style="display:flex;gap:14px;align-items:center"><b>b.</b><div style="width:260px">'+seg('y4b',{"bars":[{"v":[25,41.7,33.3]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency (%)","xl":"teacher’s height","ticks":20,"h":185},True)+'</div></div>')],
  '',f'{EDR} · 1B Worked example 3 (pp. 12–13)',cmd=('Construct',None,'segments, legend')))
# ================= Learn 1B: describing the distribution (report template, filled part by part)
def report(parts):
    # parts: [(highlight class, blank class, [text or (placeholder, fill)])]
    out=''
    for hl,bc,toks in parts:
        out+=f'<span class="{hl}">'+''.join(t if isinstance(t,str) else B(bc,t[1],t[0]) for t in toks)+'</span> '
    return f'<div class="report"><p class="tpl" style="font-size:21px;line-height:1.9;margin:0">{out}</p></div>'
LREP=report([('hl1','h1',['The ',('variable','study mode'),' of ',('number','60'),' ',('individuals','students'),' were classified as being ',('categories','‘on-campus’ or ‘online’'),'.']),
  ('hl2','h2',['The ',('majority / most','majority'),' of the ',('individuals','students'),', ',('%','55.0%'),', were found to ',('modal category','study online'),'.']),
  ('hl3','h3',['Of the remaining ',('individuals','students'),', ',('%','45.0%'),' were found to ',('category','study on-campus'),'.'])])
body=('<div class="row" style="gap:30px;align-items:stretch"><div class="key" style="flex:.7"><h4>The mode</h4><p style="font-size:22px">The most frequent category: the <b>tallest bar</b> or <b>longest segment</b>.</p>'
  '<h4 style="margin-top:16px">A report includes</h4><p style="font-size:22px;line-height:1.9"><span class="hl1">1 · the context and how many</span><br><span class="hl2">2 · the modal category, with its %</span><br><span class="hl3">3 · percentages for the others</span></p>'
  '<p class="muted" style="font-size:19px;margin-top:10px">‘Majority’ only when the mode is more than 50%; otherwise ‘the most common’.</p></div>'
  f'<div style="flex:1.3;display:flex;flex-direction:column;gap:14px"><div class="key"><h4>The data</h4><div style="display:flex;justify-content:center">{fttab("Study mode",[("on-campus",27,"45.0"),("online",33,"55.0")],(60,"100.0"),fs=20,pcth="%")}</div></div>'
  f'{LREP}<span class="frag" data-fill="h1"></span><span class="frag" data-fill="h2"></span><span class="frag" data-fill="h3"></span></div></div>')
S.append(TPL._frame('learn','Learn · 1B','Describing the distribution of a categorical variable',body,'Cambridge General Mathematics Units 3&amp;4, 1B pp. 9–10 (report guidelines; study mode data p. 7)',cfu='disc'))
# ================= WE5: Cambridge Example 5
WREP=report([('hl1','h1',['The ',('variable','climate types'),' of ',('number','23'),' ',('individuals','countries'),' were classified as being ',('categories','‘cold’, ‘mild’ or ‘hot’'),'.']),
  ('hl2','h2',['The ',('majority / most','majority'),' of the ',('individuals','countries'),', ',('%','60.9%'),', were found to ',('modal category','have a mild climate'),'.']),
  ('hl3','h3',['Of the remaining ',('individuals','countries'),', ',('%','26.1%'),' were found to ',('category','have a hot climate'),', while ',('%','13.0%'),' were found to ',('category','have a cold climate'),'.'])])
S.append(qslide('we','Worked example 5 · 1B','Describing the distribution of a categorical variable',
  G('In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages.',
    fttab('Climate type',CLIMR,(23,'100.0'),rid='w5t',pcth='%'),'Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.'),
  [('Context','23 countries; climate type cold, mild or hot.','data-hi="#w5t|3|hy" data-fill="h1"'),('Mode','Mild, 60.9%: more than 50%, so ‘the majority’.','data-hi="#w5t|1|hb" data-fill="h2"'),
   ('Others','hot 26.1%, cold 13.0%','data-hi="#w5t|2,0|hg" data-fill="h3"'),('TMPL',WREP)],
  '',f'{CAM} · Example 5 (pp. 10–11, report verbatim)',video='Cambridge GO · Example 5 (1B Resources)',cmd=('Write',None,'context, mode, percentages')))
# ================= You try: Edrolo 1B WE4
YREP=report([('hl1','h1',[('number','24'),' ',('individuals','prep students'),' were surveyed on ',('question','how tall they thought their teacher was'),'.']),
  ('hl2','h2',[' The ',('most common / majority','most common'),' response was ',('modal category','average'),', accounting for ',('%','41.7%'),' of responses,']),
  ('hl3','h3',[' while ',('%','25%'),' said their teacher was ',('category','short'),', and ',('%','33.3%'),' said their teacher was ',('category','tall'),'.'])])
S.append(qslide('yt','You try · Edrolo 1B WE4','Describing the distribution',
  '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.'+
  '<div style="width:340px;margin:10px auto">'+seg('y5s',{"bars":[{"v":[25,41.7,33.3]}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency (%)","xl":"teacher’s height","ticks":20,"h":270})+'</div>'+
  plist([('a.','Find the modal category of the data set.'),('b.','Describe the distribution of the data set.')]),
  [('Tallest segment','average: 41.7% (short 25%, tall 33.3%)','data-pk="0"'),('ANS','<b>a.</b> &nbsp;Average'),
   ('Context','24 prep students, asked about their teacher’s height.','data-pk="1" data-fill="h1"'),('Mode','average, 41.7%: under 50%, so ‘the most common’.','data-pk="1" data-fill="h2"'),
   ('Others','short 25%, tall 33.3%','data-pk="1" data-fill="h3"'),('TMPL','<b>b.</b>'+YREP)],
  '',f'{EDR} · 1B Worked example 4 (p. 14)',cmd=('Describe',None,'context, mode, percentages')))
# ================= Exits
DAY=list(range(1,16)); TMP=[12.7,11.8,10.7,9.0,6.0,7.0,4.1,4.8,9.2,6.7,7.5,8.0,8.6,9.8,7.7]
def tt1(ix): return ('<table class="t" style="font-size:16px;margin:4px auto"><tr><td class="l"><em>day number</em></td>'+''.join(f'<td>{DAY[i]}</td>' for i in ix)+'</tr><tr><td class="l"><em>minimum temperature</em> (°C)</td>'+''.join(f'<td>{TMP[i]}</td>' for i in ix)+'</tr></table>')
TT1='<div style="display:flex;flex-direction:column;gap:6px">'+tt1(range(8))+tt1(range(8,15))+'</div>'
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2019 Exam 2 Q1a','Show what you know',
  G('The table shows the <em class="v">day number</em> and the <em class="v">minimum temperature</em>, in degrees Celsius, for 15 consecutive days in May 2017.',TT1,
   'Which of the two variables in this data set is an ordinal variable? <span class="muted">(1 mark)</span>'),
  [('Temperature','measured in °C: numerical.'),('Day number','labels each day and puts the days in order; you wouldn’t average it: categorical, ordinal.')],
  '<em class="v">day number</em> is the ordinal variable.',f'{EDR} · 1A Q14 · VCAA 2019 Exam 2 Data analysis Q1a (examiner report)',
  stat=('mark',83),cmd=('Which',1,'name the variable')))
HEP=[(1,1.76,15.34,41.22),(2,1.79,16.96,42.41),(3,1.83,13.87,46.53),(4,1.82,14.23,40.53),(5,1.87,13.78,40.62),(6,1.73,14.50,45.62),(7,1.68,15.08,42.33),(8,1.82,13.13,40.88),
     (9,1.83,14.22,39.22),(10,1.87,13.62,42.51),(11,1.87,12.01,42.75),(12,1.80,12.88,38.12),(13,1.83,12.68,42.65),(14,1.87,12.45,41.32),(15,1.78,11.31,42.88)]
HT=lambda rows:table(['<em>athlete number</em>','<em>high jump</em> (metres)','<em>shot-put</em> (metres)','<em>javelin</em> (metres)'],[[a,f'{b:.2f}',f'{c:.2f}',f'{d:.2f}'] for a,b,c,d in rows],fs=13,extra='line-height:1').replace('<td','<td style="padding:1px 5px"').replace('<th>','<th style="padding:2px 4px">')
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2021 Exam 2 Q1a','Show what you know',
  ('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.',
   f'<div class="row" style="gap:16px;justify-content:center">{HT(HEP[:8])}{HT(HEP[8:])}</div>',
   'Write down the number of numerical variables in the table. <span class="muted">(1 mark)</span>'),
  [('Measured','<em>high jump</em>, <em>shot-put</em> and <em>javelin</em> are measured in metres: numerical.'),('Label','<em>athlete number</em> only names each athlete: categorical.')],
  'There are <b>3</b> numerical variables.',f'{EDR} · 1A Q16 · VCAA 2021 Exam 2 Data analysis Q1a (examiner report: a common error was counting the 45 values)',
  stat=('mark',52),cmd=('Write',1,'just the number')))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2017 Exam 1 Q5 (adapted)','Show what you know',
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
def _card(o):
    if isinstance(o,dict):
        if o.get('id')=='gm12-u3-s1': return o['card']
        for v in o.values():
            r=_card(v)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=_card(v)
            if r: return r
CW=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))))['homework']['sets']
S.append(coursework([(st['title'].replace('Revision book','Chapter 1 revision booklet'),st.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st['items']]) for st in CW]))
V=json.load(open(os.path.join(ROOT,'planner','videos.json'))); V=V if isinstance(V,list) else V.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V if v['sub'] in ('1A','1B')]))
n=assemble(S,'12MAG · S1 · Types of data and categorical data',os.path.join(ROOT,'lessons','S1-slides.html'))
print(n,'slides')
