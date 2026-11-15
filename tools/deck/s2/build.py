"""Lesson 2 (1C-1E) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S2-slides.html
Run: python3 tools/deck/s2/build.py

Sources (all checked against the PDFs on G: 15 Nov 2026):
- Do Now: VCAA 2024 NHT Exam 1 Q2 (NHT report: answer B only) · VCAA 2024 Exam 1 Q1 (report: B 78%, A 18, C 3, D 1)
          VCAA 2023 Exam 2 Q1a (report: 50% scored 1) · VCAA 2023 Exam 2 Q2ai (report: 95% scored 1)
- APK (the planner card's list): Cambridge Units 1&2 Chapter 2 skills checklist 2C #6 + 2D #7 (AFL games), 2D #9 (party ages); Chapter 9 checklist 9D #6, #7 (logs);
  Edrolo Units 1&2 1C Q17 (adapted from VCAA 2016 Exam 2 Q1d: report 52% scored 2/2) and 1C Q15 (adapted from VCAA 2017 Exam 2 Q2b: report 87%). Edrolo's adapted text is used verbatim
  (the originals need the decimal rainfall dot plot / a back-to-back stem plot); goal values read off Edrolo's dot plot (p. 26).
- Describing: SOCS template (tpl.socs). CAS dot plot: TI-Nspire only (ClassPad can't make dot plots: Rocco, 15 Nov).
- Learn: Cambridge Units 3&4 1C pp. 14-23, 1D pp. 28-31, 1E pp. 34-36; Edrolo Units 3&4 1C pp. 20-21 (dot plot / stem plot theory figures)
- Worked examples: Cambridge Units 3&4 Examples 6-13 (pp. 14-38). CAS: Cambridge 1C CAS 1 (27 marks); steps from planner/cas-skills.json
- You try: Edrolo Units 3&4 1C WE4, WE5 (frequency table, histogram), 1C WE1 (dot plot), 1C WE2 (stem plot), 1D WE1 (logs), 1D WE3 (log histogram)
  No Edrolo match for Examples 6 and 9, so no You try there.
- Exits: Edrolo U3&4 1C Q16 = VCAA 2020 Exam 2 Q2a (93% scored 1) · Edrolo 1C Q18 = VCAA 2016 Exam 1 Q3 (A 87%, B 9, C 1, D 2, E 1)
         Edrolo 1D Q13 = VCAA 2019 Exam 1 Q3 (D 71%, A 7, B 6, C 7, E 9). Question text = the original VCAA wording.
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
import tpl as TPL
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'

# ---------------- helpers (as in s1/build.py) ----------------
def table(head,rows,fs=19,extra='',rid=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td{" class=\"l\"" if j==0 else ""}>{c}</td>' for j,c in enumerate(r))+'</tr>' for r in rows)
    return f'<table class="t"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}"><tr>{th}</tr>{tr}</table>'
def seg(rid,cfg,stepped=False,ax=False): return f'<div class="chart{" noax" if ax else ""}" id="{rid}" data-chart="seg" data-cfg=\'{J(cfg)}\'{" data-stepped=\"1\"" if stepped else ""}{" data-axhide" if ax else ""}></div>'
def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:14px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'):
    return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def fttab(var,rows,total,rid='',pct=True,fs=19,pcth='Percentage',numh='Number'):
    """frequency table; rows/total may hold B(...) blanks. Each row carries data-i so steps can highlight it."""
    h=f'<tr><th rowspan="2">{var}</th><th colspan="{2 if pct else 1}">Frequency</th></tr><tr><th>{numh}</th>'+(f'<th>{pcth}</th>' if pct else '')+'</tr>'
    tr=''.join(f'<tr><td class="l"><span data-i="{i}">{a}</span></td><td><span data-i="{i}">{b}</span></td>'+(f'<td><span data-i="{i}">{c}</span></td>' if pct else '')+'</tr>' for i,(a,b,c) in enumerate(rows))
    k=len(rows)
    return (f'<table class="t" id="{rid}" style="font-size:{fs}px"><thead>{h}</thead>{tr}<tr><td class="l"><b><span data-i="{k}">Total</span></b></td><td><b><span data-i="{k}">{total[0]}</span></b></td>'
            +(f'<td><b><span data-i="{k}">{total[1]}</span></b></td>' if pct else '')+'</tr></table>')
def tab2(h1,h2,rows,total,rid,fs=19):
    """two-column table (interval | frequency), rows highlightable by data-i"""
    tr=''.join(f'<tr><td class="l"><span data-i="{i}">{a}</span></td><td><span data-i="{i}">{b}</span></td></tr>' for i,(a,b) in enumerate(rows))
    return f'<table class="t" id="{rid}" style="font-size:{fs}px"><tr><th>{h1}</th><th>{h2}</th></tr>{tr}<tr><td class="l"><b>Total</b></td><td><b>{total}</b></td></tr></table>'
def dl(rid,vals,cols,fs=22):
    """a data list (numbers or words) laid out in a grid; each value has data-i (its position in the list) for highlighting"""
    return f'<div class="dlist" id="{rid}" style="grid-template-columns:repeat({cols},auto);font-size:{fs}px">'+''.join(f'<span data-i="{i}">{v}</span>' for i,v in enumerate(vals))+'</div>'
def idx(vals,test): return ','.join(str(i) for i,v in enumerate(vals) if test(v))
def stemB(rid,rows,key,fs=24,hid=True,var='',cap=True):
    """stem plot whose leaves can start hidden (class hid0) and be revealed with data-show="#rid|i,j".
    rows: [(stem, [leaves])]. Returns (html, [[leaf data-i for each row]])."""
    i=0; tr=''; ix=[]
    for st,lv in rows:
        sp=''; r=[]
        for l in lv: sp+=f'<span class="lf2{" hid0" if hid else ""}" data-i="{i}">{l}</span>'; r.append(i); i+=1
        tr+=f'<tr><td class="st">{st}</td><td class="lv">{sp}</td></tr>'; ix.append(r)
    capx=f'<div class="stemcap">{var}{" &nbsp; " if var else ""}{key}</div>' if cap else ''
    return f'<div>{capx}<table class="stem3" id="{rid}" style="font-size:{fs}px">{tr}</table></div>', ix
def J2(xs): return ','.join(str(x) for x in xs)
def growix(v):
    """index of each non-empty bin among the drawn bars (empty bins draw no rect)"""
    out={};k=0
    for i,x in enumerate(v):
        if x>0: out[i]=k; k+=1
    return out
def dix(vals,test): return ','.join(str(i) for i,v in enumerate(sorted(vals)) if test(v))
def nl(n): return ''.join('<span class="frag"></span>' for _ in range(n))
CS={x['id']:x for x in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills']}
yid=lambda u:u.split('v=')[1].split('&')[0]

S=[]
# ================= opening
S.append(title(2,'Displaying and describing numerical data',
  'Cambridge General Mathematics Units 3&amp;4 · 1C Displaying and describing numerical data · 1D Dot plots and stem plots · 1E Using a logarithmic (base 10) scale to display data','S2'))
LI=['To be able to construct frequency tables for discrete numerical data.','To be able to construct frequency tables for grouped numerical data (discrete and continuous).',
    'To be able to construct a histogram from a frequency table for numerical data.','To be able to construct a histogram from numerical data using a CAS calculator.',
    'To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.',
    'To be able to construct a dot plot for numerical data.','To be able to construct a stem plot for numerical data.',
    'To be able to revise the concept of log<sub>10</sub> <i>x</i>.','To be able to investigate the effect of the logarithmic scale on the features of a distribution.']
SC=['I can construct a frequency table for discrete numerical data.','I can construct a grouped frequency table.','I can construct a histogram from a grouped frequency table.',
    'I can describe the features of a distribution from a histogram.','I can construct a dot plot.','I can construct a stem plot.',
    'I can use a CAS calculator to find logs.','I can interpret a histogram with a log scale.']
TD=today(LI,SC,[('Do Now','· four VCAA questions on 1A–1B','#00838F'),('APK','· Year 11 skills and two VCAA questions','var(--apk)'),
  ('Frequency tables','→ WE 6, 7',None),('Histograms','→ WE 8 · CAS',None),('Describing: SOCS','→ WE 9',None),
  ('Dot plots and stem plots','→ WE 10, 11',None),('Logs and log scales','→ WE 12 · CAS · WE 13',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')])
S.append(TD.replace('<div class="col3">','<style>.li9 .card3:first-child li{font-size:17px!important;padding-top:4px!important;padding-bottom:4px!important;line-height:1.3}</style><div class="col3 li9">',1))
FPCT=F('percentage frequency = ',FR(['number of values in the interval'],['total number of values']),' × 100%')
FLOG=F('log<sub>10</sub> <i>x</i> = <i>b</i> &nbsp;⇔&nbsp; 10<sup><i>b</i></sup> = <i>x</i>')
FNUM=F('number = 10<sup>its log</sup>')
S.append(keys([
  ('Histogram','columns that touch; each column is an interval, its height the frequency',hist('kh',{"start":0,"w":1,"v":[2,5,8,6,3,1],"ymax":8,"ystep":4,"nox":True,"noy":True,"h":110,"W":220,"L":12})),
  ('Dot plot','a number line with a dot for each value; equal values stack',dot('kd',{"min":1,"max":5,"vals":[1,2,2,3,3,3,4,5],"h":140,"W":260,"r":8,"fs":14})),
  ('Stem plot','stem = leading digits, leaf = last digit; always a key','<table class="stem3" style="font-size:14px"><tr><td class="st">1</td><td class="lv" style="min-width:0">2 4 9</td></tr><tr><td class="st">2</td><td class="lv" style="min-width:0">1 1 6</td></tr></table>'),
  ('Shape','symmetric, positively skewed (long upper tail) or negatively skewed (long lower tail)'),
  ('Log scale','an axis in powers of 10, for data ranging over several orders of magnitude')],
  [('Percentage frequency',FPCT),('Log of a number',FLOG,'log<sub>10</sub>(100) = 2, since 10<sup>2</sup> = 100'),('Number from its log',FNUM,'log = 3.4 → number = 10<sup>3.4</sup>')],
  'Cambridge General Mathematics Units 3&amp;4, 1C pp. 14–16, 1D pp. 28–29, 1E pp. 34–36 · Charts: teacher illustrations'))

# ================= Do Now 1: VCAA 2024 NHT E1 Q2 (1A)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q2','Review of 1A',
  'The variables <em class="v">exercise type</em> (aerobic, boxing, circuit) and <em class="v">recovery time</em> (short, medium, long) are',
  [('Exercise type','aerobic, boxing, circuit only name a group: nominal.'),('Recovery time','short, medium, long have a natural order: ordinal.')],
  '<em class="v">exercise type</em> is <b>nominal</b> and <em class="v">recovery time</em> is <b>ordinal</b>.',
  'VCAA 2024 NHT General Mathematics Exam 1 Q2 (NHT report: answers only)',stat=('nht',),
  mc=['a nominal variable and a numerical variable respectively.','a nominal variable and an ordinal variable respectively.','an ordinal variable and a nominal variable respectively.','both ordinal variables.','both nominal variables.'],key='B'))
# ================= Do Now 2: VCAA 2024 E1 Q1 (1B)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q1','Review of 1B',
  ('A group of students were asked to name their favourite colour.<br>The results are displayed in the percentage segmented bar chart below.',
   '<div style="width:380px">'+seg('d2s',{"bars":[{"v":[35,21,18,14,12]}],"names":["pink","green","blue","yellow","red"],"legendTop":["red","yellow","blue","green","pink"],"yl":"percentage (%)","ticks":10,"h":330})+'</div>',
   'The percentage of students who named blue as their favourite colour is closest to'),
  [('Read','the blue segment runs from 56% up to 74%.'),('Subtract','74 − 56 = 18')],
  '<b>18%</b> of students named blue.','VCAA 2024 General Mathematics Exam 1 Q1 (examiner report)',stat=('mc',78),
  mc=['14%','18%','26%','74%'],key='B',dist=[18,78,3,1],
  dis=('A','18% chose this: 14% is the size of the yellow segment (74% to 88%), the one above blue.')))
# ================= Do Now 3: VCAA 2023 E2 Q1a (1A)
OY=[(1,'12.9','13.0','5.1','large'),(2,'11.4','11.7','4.8','medium'),(3,'17.4','17.4','6.5','large'),(4,'6.8','7.2','2.9','small'),(5,'9.6','10.1','3.7','medium'),
    (6,'15.5','15.6','5.7','large'),(7,'9.7','9.9','4.0','small'),(8,'7.0','7.5','2.7','small'),(9,'12.6','12.7','5.5','medium'),(10,'12.5','12.7','5.0','medium'),
    (11,'10.1','10.5','3.9','medium'),(12,'10.6','10.8','4.1','medium'),(13,'13.0','13.1','5.3','large'),(14,'8.1','8.5','3.5','small'),(15,'14.1','14.2','5.3','large')]
def oyt(rows): return table(['ID','Weight<br>(g)','Volume<br>(cm<sup>3</sup>)','Image size<br>(megapixels)','Size'],[list(r) for r in rows],fs=13,extra='line-height:1').replace('<td','<td style="padding:1px 6px"').replace('<th>','<th style="padding:2px 5px">')
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q1a','Review of 1A',
  ('<span style="font-size:17px;line-height:1.3;display:block">Data was collected to investigate the use of electronic images to automate the sizing of oysters for sale.<br>The variables in this study were:'
   '<br>• <em class="v">ID</em>: identity number of the oyster<br>• <em class="v">weight</em>: weight of the oyster in grams (g)<br>• <em class="v">volume</em>: volume of the oyster in cubic centimetres (cm<sup>3</sup>)'
   '<br>• <em class="v">image size</em>: oyster size determined from its electronic image (in megapixels)<br>• <em class="v">size</em>: oyster size when offered for sale: small, medium or large'
   '<br>The data collected for a sample of 15 oysters is displayed in Table 1.</span>',
   f'<div class="row" style="gap:10px;justify-content:center">{oyt(OY[:8])}{oyt(OY[8:])}</div>',
   'Write down the number of categorical variables in Table 1. <span class="muted">(1 mark)</span>'),
  [('ID','identity numbers are labels, not quantities: categorical.'),('Size','small, medium or large: categorical.'),('Others','weight, volume and image size are measured: numerical.')],
  'There are <b>2</b> categorical variables (<em class="v">ID</em> and <em class="v">size</em>).','VCAA 2023 General Mathematics Exam 2 Q1a (examiner report: a number of students didn’t answer; no need to name the variables)',
  stat=('mark',50),cmd=('Write',1,'just the number')))
# ================= Do Now 4: VCAA 2023 E2 Q2ai (1B)
OZ='small small large medium medium medium large small medium medium small medium small small medium medium medium medium small large'.split()
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q2ai','Review of 1B',
  G('The following data shows the sizes of a sample of 20 oysters rated as small, medium or large.',dl('d4d',OZ,5,20),
    'Use the data above to complete the following frequency table. <span class="muted">(1 mark)</span>'),
  [('Count small','7',f'data-hi="#d4d|{idx(OZ,lambda v:v=="small")}|hy" data-fill="o1"'),('Count medium','10',f'data-hi="#d4d|{idx(OZ,lambda v:v=="medium")}|hb" data-fill="o2"'),
   ('Count large','3',f'data-hi="#d4d|{idx(OZ,lambda v:v=="large")}|hg" data-fill="o3"'),('Total','7 + 10 + 3 = 20 · check: 7/20 × 100 = 35%','data-hi="#d4d||" data-fill="o4"'),
   ('TMPL','<div style="font-size:15px;font-weight:700;margin-bottom:4px">Table 2</div>'+fttab('Size',[('small',B('o1',7),'35'),('medium',B('o2',10),'50'),('large',B('o3',3),'15')],(B('o4',20),'100'),pcth='Percentage (%)',fs=18),'','data-stat="95"')],
  '','VCAA 2023 General Mathematics Exam 2 Q2ai (examiner report: some students left out the total or wrote tally marks: not accepted)',stat=('mark',95),cmd=('Complete',1,'numbers and the total')))

# ================= APK 1: Cambridge U1&2 2C #6 + 2D #7 (AFL games)
AFL=[266,259,238,227,210,160,160,159,155,145,133,99,91,80,80,75,73,58,42,36,32,25,32,25,25,21,17,13,10,9,9,4,2]
AV=[7,7,2,2,4,0,1,3,2,0,1,2,1,1]
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2C #6, 2D #7','What do you remember?',
  G('The following data gives the number of games played in total by each member of an AFL club:',dl('a1d',AFL,11,20),
    plist([('a','Use a CAS calculator to construct a histogram starting at 0 with column width 20.'),('b','Describe the shape of the histogram of the number of games played (above).')])),
  [('CAS','enter the list, Histogram, width 20, start (alignment) 0.','data-pk="0"'),
   ('ANS','<b>a</b><div style="width:430px">'+hist('a1h',{"start":0,"w":20,"v":AV,"ymax":8,"ystep":2,"tick":40,"xl":"number of games played","yl":"frequency","h":250,"W":620,"fs":17})+'</div>'),
   ('Tail','most players have under 100 games; a long tail runs out to the right.','data-pk="1"'),('ANS','<b>b</b> &nbsp;Positively skewed.')],
  '',f'{CAM12} · Chapter 2 skills checklist, 2C #6 and 2D #7 (teacher solution)',cmd=('Describe',None,'the shape')))
# ================= APK: Edrolo U1&2 1C Q17 (adapted from VCAA 2016 E2 Q1d) — histogram from a dot plot
GL=[0]*16+[0.3,0.6,1.2,1.6,1.6,2.2,2.6,3.2,6.4,7.2,7.8,12.4,16.8,17.8]
GB=[21,3,0,3,0,0,1,0,2]; gi=growix(GB)
S.append(qslide('apk','APK · VCAA 2016 Exam 2 Q1d (adapted)','A real VCAA question you can already do',
  G('The following dot plot shows the average number of goals scored per season by each player within a soccer club.',
    '<div style="width:100%">'+dot('a4d',{"min":0,"max":19,"vals":GL,"xl":"average goals scored","W":900,"h":400,"r":6,"fs":17})+'</div>',
    'Use the grid to construct a histogram that displays the distribution of the average number of goals scored per season at the soccer club. Use interval widths of two with the first interval starting at 0. <span class="muted">(2 marks)</span>'),
  [('Axes','<em>average goals scored</em> across, 0 to 18 in twos; frequency up, to 22.','data-ax="#a4h"'),
   ('0–&lt;2','16 dots at 0 and 5 more below 2: 21',f'data-hi="#a4d|{dix(GL,lambda v:v<2)}|hy" data-grow="#a4h|{gi[0]}"'),
   ('2–&lt;4','3',f'data-hi="#a4d|{dix(GL,lambda v:2<=v<4)}|hy" data-grow="#a4h|{gi[1]}"'),
   ('6–&lt;8','3 (nothing from 4 to 6)',f'data-hi="#a4d|{dix(GL,lambda v:6<=v<8)}|hy" data-grow="#a4h|{gi[3]}"'),
   ('12–&lt;14, 16–&lt;18','1 · 2 · check: 21 + 3 + 3 + 1 + 2 = 30',f'data-hi="#a4d|{dix(GL,lambda v:v>=12)}|hy" data-grow="#a4h|{gi[6]};#a4h|{gi[8]}"'),
   ('TMPL','<div style="width:440px">'+hist('a4h',{"start":0,"w":2,"v":GB,"xmin":0,"xmax":18,"ymax":22,"ystep":2,"tick":2,"xl":"average goals scored","yl":"frequency","h":320,"W":600,"fs":15},'data-stepped="1" data-axhide').replace('class="chart"','class="chart noax"')+'</div>','','data-stat="52"')],
  '','Edrolo General Mathematics Units 1&amp;2 · 1C Q17 · Adapted from VCAA 2016 Exam 2 Data analysis Q1d (examiner report: many drew interval widths of one)',stat=('mark',52),cmd=('Construct',2,'intervals of width 2, from 0')))
# ================= APK 2: Cambridge U1&2 2D #9 (party ages)
PA=[19,21,22,56,34,19,27,28,34,17,66,37,20,20,21,45,26,19,23,29]
prow=[(s,sorted(v%10 for v in PA if v//10==s)) for s in range(1,7)]
ph,pix=stemB('a2s',prow,'Key: 1 | 7 = 17',24,var='<em>age</em> (years)')
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2D #9','And a stem plot',
  G('Construct a stem plot of the ages of a group of people at a party:',dl('a2d',PA,10,24)),
  [('Stems','ages run from 17 to 66: stems 1 to 6, and a key.')]+
  [(f'Stem {s}',' '.join(map(str,lv)) or '(none)',f'data-hi="#a2d|{idx(PA,lambda v,s=s:v//10==s)}|hy" data-show="#a2s|{J2(pix[k])}"') for k,(s,lv) in enumerate(prow) if s in (1,2,3)]+
  [('Stems 4–6','45 · 56 · 66',f'data-hi="#a2d|{idx(PA,lambda v:v>=40)}|hy" data-show="#a2s|{J2(pix[3]+pix[4]+pix[5])}"'),
   ('TMPL',ph)],
  '',f'{CAM12} · Chapter 2 skills checklist, 2D #9 (teacher solution)',cmd=('Construct',None,'ordered leaves and a key')))
# ================= APK: Edrolo U1&2 1C Q15 (adapted from VCAA 2017 E2 Q2b) — mode from a stem plot
MR=[(1,[8]),(2,[2,2,4,4,4]),(2,[5,5,9]),(3,[0,0,1,2,3,4]),(3,[6,8]),(4,[0,3])]
mh_,mix=stemB('a5s',MR,'Key: 1 | 2 = 12',24,hid=False,var='<em>wingspan</em> (mm)')
S.append(qslide('apk','APK · VCAA 2017 Exam 2 Q2b (adapted)','And another',
  G('The following stem plot displays the <em class="v">wingspan</em>, in millimetres, of 19 moths that were captured.',mh_,
    'Write down the modal <em class="v">wingspan</em>, in millimetres, of the moths captured. <span class="muted">(1 mark)</span>'),
  [('Most leaves','leaf 4 appears three times on the first 2 stem; no other value appears more than twice.',f'data-hi="#a5s|{J2(mix[1][2:])}|hy"'),('Key','2 | 4 = 24 mm')],
  'The modal wingspan is <b>24 mm</b>.','Edrolo General Mathematics Units 1&amp;2 · 1C Q15 · Adapted from VCAA 2017 Exam 2 Data analysis Q2b (examiner report, original question)',
  stat=('mark',87),cmd=('Write',1,'one value, in mm')))
# ================= APK 3: Cambridge U1&2 9D #6, #7 (logs)
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9D #6, #7','Logs and powers of ten',
  plist([('a','Find the log of 592 to two decimal places.'),('b','What is the order of magnitude of 478 000?')]),
  [],'',f'{CAM12} · Chapter 9 skills checklist, 9D #6 and #7 (teacher solutions)',cmd=('Find',None,'two decimal places'),
  parts=[('a','log<sub>10</sub>(592) = 2.772… → <b>2.77</b>'),('b','478 000 = 4.78 × 10<sup>5</sup> → order of magnitude <b>5</b>')]))

# ================= Learn 1C: frequency tables for numerical data
S.append(learn('Learn · 1C','Frequency tables for numerical data',
  '<h4>Two cases</h4><p><b>Few values (discrete):</b> one row for every value from the minimum to the maximum, as for categorical data.<br><b>Many values, or continuous:</b> group the data into intervals: a <b>grouped frequency table</b>.</p>',
  '<div class="row" style="gap:26px;align-items:stretch"><div class="key frag" style="flex:1"><h4>Choosing the intervals</h4><ul class="bul" style="font-size:21px;line-height:1.55;margin-left:26px">'
  '<li>every data value is in an interval</li><li>intervals don’t overlap, and there are no gaps</li><li>about 5 to 15 intervals</li><li>easy widths: 10, 100, 1000 …</li><li>start each interval on an exact value: 0–49, 50–99, 100–149</li></ul></div>'
  '<div class="key frag" style="flex:.8"><h4>Reading an interval</h4><p style="font-size:24px;margin-top:8px"><b>30–&lt;40</b><br>at least 30 but less than 40</p><p style="font-size:24px;margin-top:10px"><b>30.0–34.9</b><br>30.0 up to 34.9</p></div></div>',
  'Percentages may add to 99.9% or 100.1%: that’s rounding, and it’s fine.','Cambridge General Mathematics Units 3&amp;4, 1C pp. 14–15',
  cards=[kcard('Percentage frequency',FPCT)]))
# ================= WE6: Cambridge Example 6
BED=[2,3,4,3,3,4,3,4,4,1,3,2,1,2,2,2,4,5,3,4,4,5,3,4]
bc={v:BED.count(v) for v in range(1,6)}
CL={1:'hy',2:'hb',3:'hg',4:'hc',5:'hy'}
S.append(qslide('we','Worked example 6 · 1C','Frequency table for discrete numerical data',
  G('The number of bedrooms in each of the 24 properties sold in a certain area over a one month period are as follows:',dl('w6d',BED,12,24),
    'Construct a table for these data showing both frequency and percentage frequency, giving the values of the percentage frequency rounded to one decimal place.'),
  [('Min and max','minimum 1, maximum 5: one row for each of 1, 2, 3, 4, 5.','data-fill="b0"')]+
  [('Count 1s and 2s','2 · 5',f'data-hi="#w6d|{idx(BED,lambda x:x<=2)}|hy" data-fill="b1"'),
   ('Count 3s, 4s, 5s','7 · 8 · 2 · total 2 + 5 + 7 + 8 + 2 = 24',f'data-hi="#w6d|{idx(BED,lambda x:x>=3)}|hb" data-fill="b3"')]+
  [
   fx('Percentage frequency','% of 1s',F(FR([V('number','2')],[V('total','24')]),' × 100%'),'8.3%',ra='data-hi="#w6d||" data-fill="p1"'),
   ('Other %','5/24 → 20.8 · 7/24 → 29.2 · 8/24 → 33.3 · 2/24 → 8.3 · total 99.9 (rounding)','data-fill="p2"'),
   ('TMPL',fttab('Number of bedrooms',[(B('b0',v),B('b1' if v<=2 else 'b3',bc[v]),B('p1' if v==1 else 'p2',p)) for v,p in zip(range(1,6),['8.3','20.8','29.2','33.3','8.3'])],(B('b3',24),B('p2','99.9')),pcth='%',fs=16).replace('class="t"','class="t cmp"'))],
  '',f'{CAM} · Example 6 (p. 14)',video='Cambridge GO · Example 6 (1C Resources)',cmd=('Construct',None,'number and % columns, total row')))
# ================= WE7: Cambridge Example 7
HRS=[35.0,48.0,45.0,43.0,38.2,50.0,39.8,40.7,40.0,50.0,35.4,38.8,40.2,45.0,45.0,40.0,43.0,48.8,43.3,53.1,35.6,44.1,34.8]
HI=['30.0−34.9','35.0−39.9','40.0−44.9','45.0−49.9','50.0−54.9']; HN=[1,6,8,5,3]; HP=['4.3','26.1','34.8','21.7','13.0']
hk=lambda v:int((v-30)//5)
S.append(qslide('we','Worked example 7 · 1C','Constructing a grouped frequency table',
  G('The data below give the average hours worked per week in 23 countries.',dl('w7d',[f'{v:.1f}' for v in HRS],8,22),'Construct a grouped frequency table with five intervals.'),
  [('Set up','five intervals, ascending: 30.0–34.9 to 50.0–54.9','data-fill="h0"')]+
  [('Count 30.0–34.9, 35.0–39.9','1 · 6',f'data-hi="#w7d|{idx(HRS,lambda v:hk(v)<=1)}|hy" data-fill="h1"'),
   ('Count 40.0–44.9 to 50.0–54.9','8 · 5 · 3 · total 23',f'data-hi="#w7d|{idx(HRS,lambda v:hk(v)>=2)}|hb" data-fill="h3"'),
   fx('Percentage frequency','first interval',F(FR([V('number','1')],[V('total','23')]),' × 100%'),'4.3%',ra='data-fill="q1"'),
   ('Other %','26.1 · 34.8 · 21.7 · 13.0 · total 99.9','data-fill="q2"'),
   ('TMPL',fttab('Average hours worked',[(B('h0',HI[k]),B('h1' if k<=1 else 'h3',HN[k]),B('q1' if k==0 else 'q2',HP[k])) for k in range(5)],(B('h3',23),B('q2','99.9')),fs=16).replace('class="t"','class="t cmp"'))],
  '',f'{CAM} · Example 7 (p. 15)',video='Cambridge GO · Example 7 (1C Resources)',cmd=('Construct',None,'five intervals, number and %')))
# ================= You try: Edrolo 1C WE4
PL=[32.0,40.2,40.5,45.1,47.0,49.1,50.1,53.7,54.2,55.3,56.9,57.2,58.2,67.2,68.9,69.0,72.3,77.6,82.1,88.5]
PI=['30−&lt;40','40−&lt;50','50−&lt;60','60−&lt;70','70−&lt;80','80−&lt;90']; PN=[1,5,7,3,2,2]; PP=['5','25','35','15','10','10']
pk=lambda v:int((v-30)//10)
S.append(qslide('yt','You try · Edrolo 1C WE4','Constructing a grouped frequency table',
  G('The <em class="v">height</em> (cm) of 20 plants in a Year 6 science experiment were recorded.',dl('y7d',[f'{v:.1f}' for v in PL],7,22),'Construct a grouped frequency table with intervals of 10.'),
  [('How many intervals?','min 32.0 → start at 30 · max 88.5 → end at 90 · six intervals','data-fill="g0"')]+
  [('Count 30–&lt;40 to 50–&lt;60','1 · 5 · 7',f'data-hi="#y7d|{idx(PL,lambda v:pk(v)<=2)}|hy" data-fill="g1"'),
   ('Count 60–&lt;70 to 80–&lt;90','3 · 2 · 2 · total 20',f'data-hi="#y7d|{idx(PL,lambda v:pk(v)>=3)}|hb" data-fill="g3"'),
   ('Percentages','1/20 × 100 = 5 · then 25, 35, 15, 10, 10','data-hi="#y7d||" data-fill="g4"'),
   ('TMPL',fttab('<em>height</em> (cm)',[(B('g0',PI[k]),B('g1' if k<=2 else 'g3',PN[k]),B('g4',PP[k])) for k in range(6)],(B('g3',20),B('g4',100)),pcth='%',numh='number',fs=15).replace('Frequency','frequency').replace('Total','total'))],
  '',f'{EDR} · 1C Worked example 4 (pp. 23–24)',cmd=('Construct',None,'intervals of 10, number and %')))

# ================= Learn 1C: the histogram (data -> grouped frequency table -> histogram), CAS 1 marks
MK=[16,11,4,25,15,7,14,13,14,12,15,13,16,14,15,12,18,22,17,18,23,15,13,17,18,22,23]
MI=['2–&lt;6','6–&lt;10','10–&lt;14','14–&lt;18','18–&lt;22','22–&lt;26']; MN=[1,1,6,11,3,5]
mk=lambda v:(v-2)//4
MCOL=['hy','hb','hg','hc','hy','hb']
mtab=('<table class="t" style="font-size:19px"><tr><th><em>marks</em></th><th>Frequency</th></tr>'+''.join(f'<tr><td class="l">{B("m0",MI[k])}</td><td>{B(f"m{k+1}",MN[k])}</td></tr>' for k in range(6))+f'<tr><td class="l"><b>Total</b></td><td><b>{B("m7",27)}</b></td></tr></table>')
def card(n,t,b,a,extra=''): return f'<div class="sc"><div class="n">{n}</div><div class="frag" {a}><div class="st">{t}</div><div class="sb">{b}</div></div>{extra}</div>'
cnt=''.join(f'<span class="frag" data-hi="#lhd|{idx(MK,lambda v,k=k:mk(v)==k)}|{MCOL[k]}" data-fill="m{k+1}"></span>' for k in range(1,6))
bars=''.join(f'<span class="frag" data-hi="#lhh|{k}|hy" data-grow="#lhh|{k}"></span>' for k in range(1,6))
body=('<div class="row" style="gap:26px;align-items:stretch"><div class="key" style="flex:.9"><h4>Data: 27 marks</h4>'+dl('lhd',MK,9,22)+'<div style="display:flex;justify-content:center;margin-top:12px">'+mtab+'</div></div>'
  '<div class="key" style="flex:1.1"><h4>Grouped frequency table → histogram</h4>'+
  hist('lhh',{"start":2,"w":4,"v":MN,"xmin":2,"xmax":26,"ymax":12,"ystep":2,"tick":4,"xl":"marks","yl":"frequency","h":380,"W":620},'data-stepped="1" data-axhide').replace('class="chart"','class="chart noax"')+
  '<ul class="bul" style="font-size:19px;margin:6px 0 0 24px"><li>bars <b>touch</b>: the scale is continuous</li><li>each bar is one interval; its height is the frequency</li></ul></div></div>'
  '<div class="stepsH">'+card(1,'Intervals','width 4, starting at 2: 2–&lt;6, 6–&lt;10, …','data-fill="m0"')+
  card(2,'Count','one interval at a time',f'data-hi="#lhd|{idx(MK,lambda v:mk(v)==0)}|hy" data-fill="m1"',cnt)+
  card(3,'Total','1 + 1 + 6 + 11 + 3 + 5 = 27','data-hi="#lhd||" data-fill="m7"')+
  card(4,'Axes','marks across (2 to 26), frequency up (to 12)','data-ax="#lhh"')+
  card(5,'Bars','one bar per interval, height = frequency','data-hi="#lhh|0|hy" data-grow="#lhh|0"',bars+'<span class="frag" data-hi="#lhh||"></span>')+'</div>')
S.append(TPL._frame('learn','Learn · 1C','The histogram: data → grouped frequency table → graph',body,'Cambridge General Mathematics Units 3&amp;4, 1C pp. 15–16 (27 marks, CAS 1, p. 16)',cfu='disc'))
# ================= WE8: Cambridge Example 8
HV=[1,6,8,5,3]
S.append(qslide('we','Worked example 8 · 1C','Constructing a histogram from a frequency table',
  G('Construct a histogram for the frequency table opposite.',tab2('Average hours worked','Frequency',list(zip(['30.0–34.9','35.0–39.9','40.0–44.9','45.0–49.9','50.0–54.9'],HV)),23,'w8t',20)),
  [('Axes','horizontal: <em>Average hours worked</em>, marked at the start of each interval (30, 35, …) · vertical: <em>Frequency</em>, scaled for the maximum, 8.','data-ax="#w8h"')]+
  [(f'Bar {a}',f'height {v}',f'data-hi="#w8t|{k}|hy" data-grow="#w8h|{k}"') for k,(a,v) in enumerate(zip(['30.0–34.9','35.0–39.9','40.0–44.9','45.0–49.9','50.0–54.9'],HV))]+
  [('TMPL','<div style="width:400px">'+hist('w8h',{"start":30,"w":5,"v":HV,"xmin":25,"xmax":60,"ymax":9,"ystep":1,"tick":5,"xl":"Average hours worked","yl":"Frequency","h":330,"W":620,"fs":17},'data-stepped="1" data-axhide').replace('class="chart"','class="chart noax"')+'</div>')],
  '',f'{CAM} · Example 8 (p. 16)',video='Cambridge GO · Example 8 (1C Resources)',cmd=('Construct',None,'labelled axes, bars that touch')))
# ================= You try: Edrolo 1C WE5
PT=fttab('<em>height</em> (cm)',list(zip(PI,PN,PP)),(20,100),rid='y8t',pcth='%',numh='number',fs=17).replace('Frequency','frequency').replace('Total','total')
S.append(qslide('yt','You try · Edrolo 1C WE5','Constructing a histogram from a frequency table',
  'The <em class="v">height</em> (cm) of 20 plants in a Year 6 science experiment was recorded in the following grouped frequency table.'+f'<div style="margin:10px 0;display:flex;justify-content:center">{PT}</div>'+
  plist([('a.','Construct a histogram to display this data.'),('b.','What percentage of plants were shorter than 60 cm?')]),
  [('Axes','<em>height</em> (cm) across, 30 to 90; frequency up, to 8.','data-pk="0" data-ax="#y8h"'),
   ('Bars 30–&lt;60','heights 1, 5, 7','data-pk="0" data-hi="#y8t|0,1,2|hy" data-grow="#y8h|0;#y8h|1;#y8h|2"'),
   ('Bars 60–&lt;90','heights 3, 2, 2','data-pk="0" data-hi="#y8t|3,4,5|hy" data-grow="#y8h|3;#y8h|4;#y8h|5"'),
   ('TMPL','<b>a.</b><div style="width:460px">'+hist('y8h',{"start":30,"w":10,"v":PN,"ymax":8,"ystep":1,"tick":10,"xl":"height (cm)","yl":"frequency","h":250,"W":620,"fs":17},'data-stepped="1" data-axhide').replace('class="chart"','class="chart noax"')+'</div>'),
   ('Shorter than 60','the first three intervals: 5 + 25 + 35','data-pk="1" data-hi="#y8t|0,1,2|hg"'),('ANS','<b>b.</b> &nbsp;<b>65%</b> of plants were shorter than 60 cm.')],
  '',f'{EDR} · 1C Worked example 5 (pp. 25–26)',cmd=('Construct',None,'labelled axes, bars that touch')))
# ================= CAS: histogram (planner/cas-skills.json: histogram)
C=CS['histogram']
S.append(cas('CAS · 1C','Constructing a histogram from raw data',
  '<p>Display the following set of 27 marks in the form of a histogram.</p>'+dl('cmd',MK,9,22)+
  '<p style="margin-top:14px">Enter the data into a list named <b>marks</b>, then change the column (bin) width to <b>4</b> and the starting point to <b>2</b>.</p>'
  '<div style="width:420px;margin:8px auto 0">'+hist('cmh',{"start":2,"w":4,"v":MN,"xmin":2,"xmax":26,"ymax":12,"ystep":2,"tick":4,"xl":"marks","yl":"frequency","h":250,"W":560,"fs":16})+'</div>',
  C['ti'],C['classpad'],'Hover over (TI) or trace (ClassPad) each column: 2–&lt;6 has 1, 6–&lt;10 has 1, 10–&lt;14 has 6, 14–&lt;18 has 11, 18–&lt;22 has 3, 22–&lt;26 has 5.',
  'Cambridge General Mathematics Units 3&amp;4, 1C pp. 16–20 (CAS 1) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Learn 1C: shape
def mh(v,col='#4f84e6',vline=None,h=150,W=280):
    c={"start":0,"w":1,"v":v,"ymax":10,"ystep":5,"nox":True,"noy":True,"h":h,"W":W,"L":12,"col":col}
    if vline is not None: c['vline']=vline
    return hist('',c)
SH=[('Symmetric','tails off evenly on either side of the peak',[1,2,4,7,9,7,4,2,1]),('Positively skewed','long <b>upper</b> tail, to the right',[3,9,8,6,4,3,2,1,1]),
    ('Negatively skewed','long <b>lower</b> tail, to the left',[1,1,2,3,4,6,8,9,3]),('Bimodal','two peaks: often two groups mixed',[1,4,8,5,2,5,8,4,1])]
pic='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">'+''.join(f'<div class="key frag" style="text-align:center"><h4>{a}</h4>{mh(v)}<p style="font-size:19px;margin-top:4px">{b}</p></div>' for a,b,v in SH)+'</div>'
S.append(learn('Learn · 1C','Shape: what to look for',
  '<h4>Shape</h4><p>Is the histogram single-peaked? Does it tail off <b>evenly</b> (symmetric) or mostly in <b>one direction</b> (skewed)?</p>',pic,
  'The tail names the skew. Salaries and house prices: positively skewed. Age at death: negatively skewed.','Cambridge General Mathematics Units 3&amp;4, 1C p. 21 (shapes: teacher illustrations)'))
# ================= Learn 1C: SOCS (Rocco's paradigm for describing numerical data)
SC4=[('S','Shape','#2f6fdf','symmetric · positively skewed · negatively skewed',mh([1,2,4,7,9,7,4,2,1],h=95)),
     ('O','Outliers','#c0632b','present or not present: they go with the shape',mh([1,0,0,0,3,7,9,6,2],h=95)),
     ('C','Centre','#1f9e74','mean · median · mode<br><b>median</b> is unaffected by outliers',mh([1,5,9,6,4,3,2,1,1],vline=3.1,h=95)),
     ('S','Spread','#7b3fbf','range · IQR<br><b>IQR</b> is unaffected by outliers',mh([0,0,1,3,10,3,1,0,0],h=95))]
pic=('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">'+''.join(f'<div class="key frag" style="text-align:center;border-color:{c}"><h4 style="color:{c}"><span style="background:{c};color:#fff;border-radius:6px;padding:0 8px;margin-right:6px">{l}</span>{n}</h4>{h}<p style="font-size:18px;margin-top:4px">{t}</p></div>' for l,n,c,t,h in SC4)+'</div>'
     '<div class="frag" style="margin-top:12px">'+socs('ls')+'</div>')
S.append(learn('Learn · 1C','Describing a distribution: SOCS',
  '<h4>SOCS, like a sock</h4><p>Describe numerical data in this order, one sentence each: <b>S</b>hape · <b>O</b>utliers · <b>C</b>entre · <b>S</b>pread.</p>',pic,
  'Skewed, or outliers? Give the <b>median</b> for the centre and the <b>IQR</b> for the spread: outliers don’t affect them. From a histogram, centre and spread are only estimates.',
  'Cambridge General Mathematics Units 3&amp;4, 1C pp. 21–23 (SOCS order: class convention; charts: teacher illustrations)'))
# ================= WE9: Cambridge Example 9 (report template)
GV=[2,2,2,2,2,2,2,4,6,10,16,34,95,233,300,207,86,4]
WSOCS=socs('r','negatively skewed','are possible outliers below 34 weeks',('around 38–39 weeks','median (the line that halves the area)'),('range','17 weeks (25 to 42 weeks)'),most='36 and 41 weeks',fs=17)
S.append(qslide('we','Worked example 9 · 1C','Describing the features of a distribution from a histogram',
  G('The histogram shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year.',
    '<div style="width:100%">'+hist('w9h',{"start":25,"w":1,"v":GV,"xmin":25,"xmax":44,"ymax":300,"ystep":100,"tick":1,"xl":"Gestation period (weeks)","yl":"Frequency","h":360,"W":760,"fs":15,"L":64})+'</div>',
    'Describe this histogram in terms of shape, centre, spread and outliers.'),
  [('Shape','the bars tail off to the left: a long lower tail.','data-hi="#w9h|0,1,2,3,4,5,6,7,8,9,10|hy" data-fill="r1"'),
   ('Outliers','values below 34 weeks look small compared with the rest, but a histogram can’t tell us which are outliers.','data-hi="#w9h|0,1,2,3,4,5,6,7,8|hc" data-fill="r2"'),
   ('Centre','the line that halves the area is between 38 and 39.','data-hi="#w9h|13,14|hb" data-fill="r3"'),
   ('Spread','25 to 42 weeks; most values 36–41.','data-hi="#w9h|11,12,13,14,15,16|hg" data-fill="r4"'),('TMPL',WSOCS)],
  '',f'{CAM} · Example 9 (pp. 23–24; Cambridge’s solution set out in SOCS order; histogram redrawn)',video='Cambridge GO · Example 9 (1C Resources)',cmd=('Describe',None,'SOCS: shape, outliers, centre, spread')))

# ================= Learn 1D: dot plots and stem plots
DP=dot('ldp',{"min":2,"max":7,"vals":[2,3,3,4,4,4,4,5,5,6,7],"xl":"board games owned","h":190,"W":520,"r":11})
SP,_=stemB('lsp',[(4,[3,5,5,5,7]),(5,[1,3,6,8]),(6,[7,9]),(7,[1]),(8,[0,1,3,9,9]),(9,[1,4])],'Key: 4 | 3 = 43',22,hid=False)
S.append(learn('Learn · 1D','Dot plots and stem plots',
  '<h4>Two quick, by-hand displays for small data sets</h4><p>Both show every data value, so you can still read the data off the plot.</p>',
  f'<div class="row" style="gap:26px;align-items:stretch"><div class="key frag" style="flex:1.1"><h4>Dot plot</h4><p style="font-size:20px">A number line with each data value marked by a dot. Equal values <b>stack</b>. Best for small, discrete data sets.</p>{DP}</div>'
  f'<div class="key frag" style="flex:1"><h4>Stem plot</h4><p style="font-size:20px">Each value splits into a <b>stem</b> (leading digits) and a <b>leaf</b> (last digit).</p><div class="row" style="gap:22px;align-items:center">{SP}'
  '<ul class="bul" style="font-size:19px;margin-left:22px;line-height:1.5"><li>always add a key</li><li>leaves in order</li><li>include empty stems</li><li>bunched up? split the stems</li></ul></div></div></div>',
  'Spaces matter: line the leaves up in columns so the rows can be compared like bars.','Cambridge General Mathematics Units 3&amp;4, 1D pp. 28–31 · Edrolo General Mathematics Units 3&amp;4, 1C pp. 20–21 (example plots)'))
# ================= WE10: Cambridge Example 10 (dot plot)
CR=[22,19,18,19,23,25,22,29,18,22,23,24,22]
srt=sorted(CR)
S.append(qslide('we','Worked example 10 · 1D','Constructing a dot plot',
  G('The ages (in years) of the 13 members of a cricket team are:',dl('w10d',CR,7,26),'Construct a dot plot.'),
  [('Number line','scaled to include all data values (17 to 30); label it <em>Age (years)</em>.','data-ax="#w10p"'),
   ('18 and 19','two dots each, stacked',f'data-hi="#w10d|{idx(CR,lambda v:v in (18,19))}|hy" data-show="#w10p|{dix(CR,lambda v:v in (18,19))}"'),
   ('22','four dots, stacked',f'data-hi="#w10d|{idx(CR,lambda v:v==22)}|hb" data-show="#w10p|{dix(CR,lambda v:v==22)}"'),
   ('23, 24, 25','two dots on 23, one each on 24 and 25',f'data-hi="#w10d|{idx(CR,lambda v:v in (23,24,25))}|hg" data-show="#w10p|{dix(CR,lambda v:v in (23,24,25))}"'),
   ('29','one dot · check: 13 dots',f'data-hi="#w10d|{idx(CR,lambda v:v==29)}|hc" data-show="#w10p|{dix(CR,lambda v:v==29)}"'),
   ('TMPL','<div style="width:520px">'+f'<div class="chart noax" id="w10p" data-chart="dot3" data-axhide data-cfg=\'{J({"min":17,"max":30,"vals":CR,"xl":"Age (years)","h":230,"W":760,"r":14,"fs":20,"hid":True})}\'></div></div>')],
  '',f'{CAM} · Example 10 (p. 29)',video='Cambridge GO · Example 10 (1D Resources)',cmd=('Construct',None,'scaled, labelled number line')))
# ================= You try: Edrolo 1C WE1 (dot plot)
PET=[3,2,0,1,1,3,0,5,2,1,1,2]
S.append(qslide('yt','You try · Edrolo 1C WE1','Constructing a dot plot',
  G('Sophie surveyed 12 of the families living on her street.<br>She asked for the number of pets each of them owned and the results were recorded.',dl('y10d',PET,12,26),
    plist([('a.','Construct a dot plot to display this data.'),('b.','What was the modal number of pets owned by families that Sophie surveyed?')])),
  [('Order','0 0 1 1 1 1 2 2 2 3 3 5 · lowest 0, highest 5','data-pk="0"'),('Number line','scale 0 to 5; label it <em>number of pets</em>.','data-pk="0" data-ax="#y10p"'),
   ('0, 1, 2','2 dots · 4 dots · 3 dots',f'data-pk="0" data-hi="#y10d|{idx(PET,lambda v:v<=2)}|hy" data-show="#y10p|{dix(PET,lambda v:v<=2)}"'),
   ('3, 5','2 dots · 1 dot',f'data-pk="0" data-hi="#y10d|{idx(PET,lambda v:v>2)}|hb" data-show="#y10p|{dix(PET,lambda v:v>2)}"'),
   ('TMPL','<b>a.</b><div style="width:470px">'+f'<div class="chart noax" id="y10p" data-chart="dot3" data-axhide data-cfg=\'{J({"min":0,"max":5,"vals":PET,"xl":"number of pets","h":230,"W":700,"r":14,"fs":20,"hid":True})}\'></div></div>'),
   ('Mode','the most dots: 4 families own 1 pet.',f'data-pk="1" data-hi="#y10p|{dix(PET,lambda v:v==1)}|hg"'),('ANS','<b>b.</b> &nbsp;<b>1 pet</b>')],
  '',f'{EDR} · 1C Worked example 1 (pp. 20–21)',cmd=('Construct',None,'scaled, labelled number line')))
# ================= CAS: dot plot (TI-Nspire only: ClassPad has no dot plot)
C=CS['dotplot']
S.append(cas('CAS · 1D','Constructing a dot plot (TI-Nspire)',
  '<p>The ages (in years) of the 13 members of a cricket team are:</p>'+dl('cdd',CR,7,24)+'<p style="margin-top:12px">Enter the ages into a list named <b>age</b> and display them as a dot plot.</p>',
  C['ti'],['<b>No dot plot on the ClassPad.</b> Draw dot plots by hand.'],'Each dot is one cricketer: 22 has four dots, the most of any age.',
  'Cambridge General Mathematics Units 3&amp;4, Example 10 data (p. 29) · Steps: CAS guide (planner)',videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:2]]))
# ================= WE11: Cambridge Example 11 (stem plot: unordered, then ordered)
UR=[26,3,12,20,36,1,25,26,13,9,26,27,15,21,7,8,22,3,37,17,55,30,1]
urow=[(s,[v%10 for v in UR if v//10==s]) for s in range(6)]
orow=[(s,sorted(l)) for s,l in urow]
uh,uix=stemB('w11u',urow,'',22,cap=False); oh,oix=stemB('w11o',orow,'Key: 1|2 = 12',22,var='<em>rate</em> (%)')
S.append(qslide('we','Worked example 11 · 1D','Constructing a stem plot',
  G('University participation rates (%) in 23 countries are given below.',dl('w11d',UR,12,26),'Display the data in the form of a stem plot.'),
  [('Stems','values in the units, tens, twenties, … fifties: stems 0 to 5.'),
   ('Stems 0 and 1','first come first: 26 → stem 2, leaf 6 …',f'data-hi="#w11d|{idx(UR,lambda v:v<20)}|hy" data-show="#w11u|{J2(uix[0]+uix[1])}"'),
   ('Stem 2','6 0 5 6 6 7 1 2',f'data-hi="#w11d|{idx(UR,lambda v:v//10==2)}|hb" data-show="#w11u|{J2(uix[2])}"'),
   ('Stems 3 to 5','6 7 0 · (none) · 5',f'data-hi="#w11d|{idx(UR,lambda v:v>=30)}|hg" data-show="#w11u|{J2(uix[3]+uix[4]+uix[5])}"'),
   ('Order','leaves on each stem in ascending order; add the variable name and a key: 1|2 = 12',f'data-hi="#w11d||" data-show="#w11o|{J2(sum(oix,[]))}"'),
   ('TMPL','<div class="row" style="gap:26px;align-items:flex-start"><div><div style="font-size:16px;font-weight:700">Unordered</div>'+uh+'</div><div><div style="font-size:16px;font-weight:700">Ordered</div>'+oh+'</div></div>')],
  '',f'{CAM} · Example 11 (p. 30)',video='Cambridge GO · Example 11 (1D Resources)',cmd=('Display',None,'stems, ordered leaves, key')))
# ================= You try: Edrolo 1C WE2 (stem plot)
EX=[55,68,76,90,83,89,75,66,59,84,48,62,58,95,80,77,61,92,99,63,84,65,70,81,96]
erow=[(s,sorted(v%10 for v in EX if v//10==s)) for s in range(4,10)]
eh,eix=stemB('y11s',erow,'Key: 4 | 8 = 48%',22)
above=[i for s,(st,lv) in enumerate(erow) for i,l in zip(eix[s],lv) if st*10+l>70]
S.append(qslide('yt','You try · Edrolo 1C WE2','Constructing a stem plot',
  G('Ms Smyth’s maths class of 25 students sat their end-of-year exam. Their results (%) were recorded.',dl('y11d',EX,13,24),
    plist([('a.','Construct a stem plot to display this data.'),('b.','How many students scored above 70% on the exam?')])),
  [('Stems','two-digit values from 48 to 99: stems 4 to 9 (tens), leaves = ones; add a key.','data-pk="0"'),
   ('Stems 4 to 6','8 · 5 8 9 · 1 2 3 5 6 8',f'data-pk="0" data-hi="#y11d|{idx(EX,lambda v:v<70)}|hy" data-show="#y11s|{J2(eix[0]+eix[1]+eix[2])}"'),
   ('Stems 7 to 9','0 5 6 7 · 0 1 3 4 4 9 · 0 2 5 6 9',f'data-pk="0" data-hi="#y11d|{idx(EX,lambda v:v>=70)}|hb" data-show="#y11s|{J2(eix[3]+eix[4]+eix[5])}"'),
   ('TMPL','<b>a.</b>'+eh),
   ('Above 70','leaves greater than 0 on stem 7, and every leaf on stems 8 and 9: 3 + 6 + 5',f'data-pk="1" data-hi="#y11s|{J2(above)}|hg"'),('ANS','<b>b.</b> &nbsp;<b>14 students</b>')],
  '',f'{EDR} · 1C Worked example 2 (pp. 21–22)',cmd=('Construct',None,'stems, ordered leaves, key')))

# ================= Learn 1E: logs are powers of 10
LT=('<table class="t" style="font-size:24px;margin:0 auto"><tr><th class="l">number</th>'+''.join(f'<td>{x}</td>' for x in ['0.01','0.1','1','10','100','1000','1 000 000'])+'</tr>'
    '<tr class="frag"><th class="l">power of 10</th>'+''.join(f'<td>10<sup>{p}</sup></td>' for p in ['−2','−1','0','1','2','3','6'])+'</tr>'
    '<tr class="frag"><th class="l">log</th>'+''.join(f'<td><b>{p}</b></td>' for p in ['−2','−1','0','1','2','3','6'])+'</tr></table>')
S.append(learn('Learn · 1E','Logs are just powers of 10',
  '<h4>log<sub>10</sub> <i>x</i></h4><p>The log of a number is the power of 10 that makes it: log<sub>10</sub>(1000) = 3, since 10<sup>3</sup> = 1000.</p>',
  LT+'<div class="key frag" style="margin-top:18px;font-size:21px"><h4>Properties</h4>number greater than 1 → log greater than 0 &nbsp;·&nbsp; between 0 and 1 → log negative &nbsp;·&nbsp; zero → log undefined</div>',
  'Each step of 1 on a log scale multiplies the number by 10.','Cambridge General Mathematics Units 3&amp;4, 1E pp. 34–35',cards=[kcard('Log of a number',FLOG)]))
# ================= Learn 1E: why a log scale?
NUMS=[0.01,0.1,1,10,100,1000,10000,100000,1000000]
def nline(xs,labs,lo,hi,title,W=1080,h=96):
    sx=lambda x:40+(x-lo)/(hi-lo)*(W-80)
    s=f'<svg viewBox="0 0 {W} {h}" width="100%"><line x1="30" x2="{W-30}" y1="40" y2="40" stroke="#333" stroke-width="2"/>'
    for t,l in labs: s+=f'<line x1="{sx(t)}" x2="{sx(t)}" y1="40" y2="48" stroke="#333" stroke-width="1.5"/><text x="{sx(t)}" y="72" text-anchor="middle" font-size="19">{l}</text>'
    for x in xs: s+=f'<circle cx="{sx(x)}" cy="28" r="9" fill="#2f6fdf"/>'
    return s+f'<text x="{W/2}" y="{h-2}" text-anchor="middle" font-size="19" font-style="italic" font-weight="600">{title}</text></svg>'
import math
L1=nline(NUMS,[(0,'0'),(300000,'300 000'),(600000,'600 000'),(900000,'900 000')],0,1000000,'number')
L2=nline([math.log10(x) for x in NUMS],[(k,str(k).replace('-','−')) for k in range(-2,7)],-2.3,6.3,'log(number)')
S.append(learn('Learn · 1E','Why use a log scale?',
  '<h4>Data over several orders of magnitude</h4><p>0.01, 0.1, 1, 10, 100, 1000, 10 000, 100 000, 1 000 000 plotted on an ordinary scale, then as their logs.</p>',
  f'<div class="key frag"><h4>Ordinary scale: eight numbers bunch up at 0, one million sits alone</h4>{L1}</div><div class="key frag" style="margin-top:14px"><h4>Log scale: evenly spread</h4>{L2}</div>',
  'A positively skewed histogram often becomes roughly symmetric on a log scale.','Cambridge General Mathematics Units 3&amp;4, 1E pp. 35–36'))
# ================= WE12: Cambridge Example 12
S.append(qslide('we','Worked example 12 · 1E','Using a CAS calculator to find logs',
  plist([('a','Find the log of 45, correct to two significant figures.'),('b','Find the number with log equal to 2.7125, correct to the nearest whole number.')]),
  [('Calculator','type log(45): log 45 = 1.65…','data-pk="0"'),('ANS','<b>a</b> &nbsp;log 45 = 1.65… = <b>1.7</b> (to 2 sig. figs)'),
   ('Undo the log','if the log of a number is 2.7125, the number is 10<sup>2.7125</sup>: type 10^2.7125.','data-pk="1"'),('ANS','<b>b</b> &nbsp;10<sup>2.7125</sup> = 515.82… = <b>516</b> (to the nearest whole number)')],
  '',f'{CAM} · Example 12 (pp. 36–37)',video='Cambridge GO · Example 12 (1E Resources)',cmd=('Find',None,'rounded as asked')))
# ================= CAS: logs
C=CS['logs']
S.append(cas('CAS · 1E','Finding a log, and undoing it',
  '<p>a Find the log of 45, correct to two significant figures.</p><p>b Find the number with log equal to 2.7125, correct to the nearest whole number.</p>'
  '<div class="key" style="margin-top:14px;font-size:21px"><h4>On the screen</h4>log(45) → 1.65321…<br>10^2.7125 → 515.822…</div>',
  C['ti'],C['classpad'],'a 1.7 &nbsp;·&nbsp; b 516','Cambridge General Mathematics Units 3&amp;4, 1E Example 12 (p. 37) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti']+C['videos']['classpad']]))
# ================= You try: Edrolo 1D WE1
S.append(qslide('yt','You try · Edrolo 1D WE1','Using a CAS calculator to find logs',
  'Use log<sub>10</sub> for the following calculations.'+plist([('a.','Calculate the log of 23, correct to two decimal places.'),('b.','If the log of a number is 5, what is the number?')]),
  [],'',f'{EDR} · 1D Worked example 1 (pp. 37–38)',cmd=('Calculate',None,'two decimal places'),
  parts=[('a.','log<sub>10</sub>(23) = 1.361… → <b>1.36</b>'),('b.','log<sub>10</sub>(<i>x</i>) = 5, so <i>x</i> = 10<sup>5</sup> = <b>100 000</b>')]))
# ================= WE13: Cambridge Example 13
AW=[3.7,7.4,18.5,25.9,25.9,11.1,7.4]
S.append(qslide('we','Worked example 13 · 1E','Interpreting a histogram with a log scale',
  ('The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.',
   '<div style="width:470px">'+hist('w13h',{"start":-2,"w":1,"v":AW,"xmin":-2,"xmax":6,"ymax":28,"ystep":4,"pct":True,"tick":1,"xl":"log(body weight)","yl":"Percentage","h":300,"W":600,"fs":16})+'</div>',
   plist([('a','What body weight (in kg) is represented by the number 4 on the log scale?'),('b','How many of these animals have body weights more than 10 000 kg?'),
          ('c','The weight of a cat is 3.3 kg. Use your calculator to determine the log of its weight correct to two significant figures.'),
          ('d','Determine the weight (in kg) of the animal with a log(<em class="v">body weight</em>) of 3.4 (the elephant). Write your answer correct to the nearest whole number.')])),
  [('Log 4','the number is 10<sup>4</sup>.','data-pk="0"'),('ANS','<b>a</b> &nbsp;10<sup>4</sup> = <b>10 000 kg</b>'),
   ('Above 4','10 000 is 4 on the log scale; one bar above 4: 7.4% of 27 animals.','data-pk="1" data-hi="#w13h|6|hy"'),('ANS','<b>b</b> &nbsp;<b>Two animals</b>'),
   ('Cat','log 3.3 = 0.518…','data-pk="2" data-hi="#w13h||"'),('ANS','<b>c</b> &nbsp;<b>0.52</b> (to 2 sig. figs)'),
   ('Elephant','10<sup>3.4</sup> = 2511.88…','data-pk="3"'),('ANS','<b>d</b> &nbsp;<b>2512 kg</b>')],
  '',f'{CAM} · Example 13 (pp. 37–38; histogram redrawn from the CAS 2 data, p. 38)',video='Cambridge GO · Example 13 (1E Resources)',cmd=('Determine',None,'rounded as asked')))
# ================= You try: Edrolo 1D WE3
DV=[2,3,3,5,6,1]
S.append(qslide('yt','You try · Edrolo 1D WE3','Interpreting a histogram with a log scale',
  ('A class of twenty students were asked about the <em class="v">distance</em>, in kilometres, from their home to the school.<br>The results were summarised in a histogram using a log<sub>10</sub> scale.',
   '<div style="width:440px">'+hist('y13h',{"start":-1,"w":0.5,"v":DV,"ymax":8,"ystep":2,"tick":0.5,"dec":1,"xl":"log₁₀(distance)","yl":"frequency","h":300,"W":560,"fs":17})+'</div>',
   plist([('a.','Jane was away the day of the survey. It is known that she lives 9.5 km away from school. Which interval on the histogram reflects this?'),('b.','How many students live more than 10 km away from school?')])),
  [('Log of 9.5','log<sub>10</sub>(9.5) = 0.9777…: between 0.5 and 1.0','data-pk="0" data-hi="#y13h|3|hy"'),('ANS','<b>a.</b> &nbsp;<b>0.5–&lt;1.0</b>'),
   ('Log of 10','log<sub>10</sub>(10) = 1: count the columns above 1','data-pk="1" data-hi="#y13h|4,5|hg"'),('ANS','<b>b.</b> &nbsp;6 + 1 = <b>7 students</b>')],
  '',f'{EDR} · 1D Worked example 3 (pp. 40–41)',cmd=('Which',None,'an interval')))

# ================= Exits
neck={31:1,32:1,33:3,34:11,35:19,36:32,37:34,38:48,39:39,40:18,41:28,42:12,43:3,44:1}
nv=[k for k,f in neck.items() for _ in range(f)]
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2020 Exam 2 Q2a','Show what you know',
  ('The <em class="v">neck size</em>, in centimetres, of 250 men was recorded and displayed in the dot plot below.',
   dot('e1d',{"min":30,"max":45,"vals":nv,"xl":"neck size (cm)","W":900,"h":560,"r":4.2,"fs":20}),
   'Write down the modal <em class="v">neck size</em>, in centimetres, for these 250 men. <span class="muted">(1 mark)</span>'),
  [('Mode','the value with the tallest column of dots: 48 dots at 38.',f'data-hi="#e1d|{dix(nv,lambda v:v==38)}|hy"')],
  'The modal neck size is <b>38 cm</b>.',f'{EDR} · 1C Q16 · VCAA 2020 Exam 2 Data analysis Q2a (examiner report)',stat=('mark',93),cmd=('Write',1,'one value')))
TR=[(2,[2,4,4]),(2,[5,7,8,8,8,8,8,8,9,9,9,9]),(3,[1,2,3,3,4,4,4]),(3,[5,6,7,7,7,7]),(4,[1])]
TR=[(2,[2,2,4,4]),(2,[5,7,8,8,8,8,8,8,9,9,9,9]),(3,[1,2,3,3,4,4,4]),(3,[5,6,7,7,7,7]),(4,[1])]
th,tix=stemB('e2s',TR,'key: 2|2 = 2.2 °C',24,hid=False,var='<em>temperature</em>')
e8=[i for i,l in zip(tix[1],TR[1][1]) if l==8]; e9=[i for i,l in zip(tix[1],TR[1][1]) if l==9]; e7=[i for i,l in zip(tix[3],TR[3][1]) if l==7]
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2016 Exam 1 Q3','Show what you know',
  ('The stem plot below displays 30 temperatures recorded at a weather station.',th,'The modal temperature is'),
  [('Most leaves','2 | 8 has six leaves: the most of any value.',f'data-hi="#e2s|{J2(e8)}|hy"'),('Read the key','2 | 8 = 2.8 °C')],
  'The modal temperature is <b>2.8 °C</b>.',f'{EDR} · 1C Q18 · VCAA 2016 Exam 1 Data analysis Q3 (examiner report)',stat=('mc',87),
  mc=['2.8 °C','2.9 °C','3.7 °C','8.0 °C','9.0 °C'],key='A',dist=[87,9,1,2,1],
  dis=('B','9% chose this: 2 | 9 has four leaves, but 2 | 8 has six.')))
PV=[0,0,1,0,7,5,21,13,1,0]
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2019 Exam 1 Q3','Show what you know',
  ('The histogram below shows the population size for these 48 countries plotted on a log<sub>10</sub> scale.',
   '<div style="width:470px">'+hist('e3h',{"start":0,"w":1,"v":PV,"ymax":25,"ystep":5,"tick":1,"xl":"log₁₀ (population size)","yl":"frequency","h":320,"W":600,"fs":17})+'<div class="muted" style="font-size:13px;text-align:right;margin-top:8px">Data: Worldometers, &lt;www.worldometers.info/&gt;</div></div>',
   'Based on this histogram, the number of countries with a population size that is less than 100 000 people is'),
  [('Convert','100 000 = 10<sup>5</sup>, which is 5 on the log scale.'),('Count','columns below 5: 1 + 7','data-hi="#e3h|2,4|hy"')],
  '<b>8</b> countries have a population of less than 100 000.',f'{EDR} · 1D Q13 · VCAA 2019 Exam 1 Data analysis Q3 (examiner report)',stat=('mc',71),
  mc=['1','5','7','8','48'],key='D',dist=[7,6,7,71,9],dis=('E','9% chose this: 48 is every country in the data set, not the ones below 5 on the log scale.')))

# ================= closing
S.append(checkin(SC))
def _card(o):
    if isinstance(o,dict):
        if o.get('id')=='gm12-u3-s2': return o['card']
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
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V if v['sub'] in ('1C','1D','1E')]))
n=assemble(S,'12MAG · S2 · Displaying and describing numerical data',os.path.join(ROOT,'lessons','S2-slides.html'))
print(n,'slides')
