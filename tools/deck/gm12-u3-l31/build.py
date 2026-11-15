"""Lesson gm12-u3-l31 (7A, sequences and recurrence relations) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/7A slides.html
Run: python3 tools/deck/gm12-u3-l31/build.py      Screenshots: python3 tools/deck/gm12-u3-l31/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim):
- Do Now: VCAA 2025 Exam 1 Q14 (stem of Q13-14 + graph; report: 85% D, 13/1/1/85) ·
          VCAA 2024 Exam 1 Q3 (stem of Q3-4 + histogram; report: 71% D, 18/5/7/71) ·
          VCAA 2024 Exam 2 Q2ci (boxplot; report: 84% full marks) ·
          VCAA 2023 Exam 2 Q4b (time series plot; report: 72% full marks). Figures cropped from the papers (img/).
- APK: Cambridge U1&2 Ch 3 skills checklist 3A #2 (solution worked for 12MAG) ·
       VCAA 2015 Exam 1 Number patterns Q1 (= Edrolo U1&2 3A Q12; no 2015 report on G:, % left blank; answer D = 80).
- Learn: Cambridge U3&4 7A pp. 334-338 (own words) · Edrolo U3&4 5A theory.
- Worked examples: Cambridge U3&4 Examples 1-6 (pp. 334-338).
  You trys: Ex 1, 2 = written for 12MAG (planner/written-youtrys.json YT-7A-1, YT-7A-2: no Edrolo match) ·
            Ex 3 = Edrolo U3&4 5A Worked example 5 (calculator, p. 299-300) · Ex 4 = Edrolo 5A WE4a (p. 299) ·
            Ex 5 = Edrolo 5A WE4b (p. 299) · Ex 6 = Edrolo U1&2 3B Worked example 1 (p. 133).
  (Card said 'WE5a' / 'WE5b-c': Edrolo WE5 has no parts, so WE5 -> Ex 3 and WE4b -> Ex 5; see QUEUE Decisions log.)
- CAS: planner/cas-skills.json 'recursion-sequence' (task = Cambridge Example 5).
- Exits: VCAA 2017 Further Exam 1 Q18 (Edrolo U3&4 5A Q17; report 92% D) · VCAA 2021 Exam 1 Q17 (5A Q19; 83% A) ·
         VCAA 2019 Exam 1 Q17 (5A Q20; 68% D; original wording 'shown below').
"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l31')
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"img",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
yid=lambda u:u.split('v=')[1].split('&')[0]
def chain(vals,op,fs=30,frag=True):
    """a sequence drawn as chips joined by the rule (one chip per click)"""
    out='<div style="display:flex;align-items:center;justify-content:center;gap:6px;flex-wrap:wrap;margin:14px 0">'
    for k,v in enumerate(vals):
        c=' class="frag"' if frag and k else ''
        if k: out+=f'<span{c} style="font-size:{fs-8}px;color:var(--learn);font-weight:700">→ {op} →</span>'
        out+=f'<span{c} style="font-size:{fs}px;font-weight:700;background:#fff;border:3px solid var(--learn);border-radius:12px;padding:4px 14px">{v}</span>'
    return out+'</div>'
def terms(vals,fs=24):
    return ('<table class="t" style="font-size:%dpx;margin:8px auto"><tr>'%fs+''.join(f'<td style="text-align:center;padding:4px 14px">{v}</td>' for v in vals)
            +'</tr><tr>'+''.join(f'<th style="padding:4px 14px">V<sub>{k}</sub></th>' for k in range(len(vals)))+'</tr></table>')
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'

S=[]
S.append(title(31,'Sequences and recurrence relations',f'{CAM} · 7A Sequences and recurrence relations','L31').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 questions','var(--apk)'),
  ('Sequences and rules','',None),('Worked examples 1–3','→ You try',None),('Recurrence relations','',None),
  ('Worked examples 4–6','→ You try',None),('CAS: generating a sequence','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Sequence','a list of numbers in order, separated by commas: 1, 3, 5, 7, …'),
  ('Term','each number in a sequence'),
  ('Recursion','generating each term by applying the same rule to the term before'),
  ('Recurrence relation','a starting value + a rule that gives the next term from the current term'),
  ('Iteration','one application of the rule')],
  [('Recurrence relation',RR('starting value','rule using <i>V<sub>n</sub></i>')),
   ('Naming terms',F('<i>V</i><sub><i>n</i></sub> = term after <i>n</i> applications of the rule'),'V₀ is the starting value (no applications yet)'),
   ('Next term',F('<i>V</i><sub><i>n</i>+1</sub> = the term after <i>V</i><sub><i>n</i></sub>'))],
  f'{CAM}, 7A pp. 334–338; Study Design: first-order linear recurrence relations u₀ = a, uₙ₊₁ = Ruₙ + d'))

# ================= Do Now (retrieval, AoS 1)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q14','Review of 5A (last term)',
  ('<div style="font-size:19px">The following time series graph shows the <i>margin</i>, in points, for a team winning all of its games in the first 18 weeks of a season. The team plays one game per week.</div>',
   IMG('dn1.png',470),'<div style="font-size:19px">Which one of the following options best describes the qualitative features of the time series graph above?</div>'),
  [('Trend','the margin goes down over the 18 weeks: decreasing trend'),('Fluctuations','up-and-down movements with no regular pattern: irregular fluctuations'),
   ('Rule out','no sudden jump or drop (no structural change); trend AND fluctuations both present')],
  'Decreasing trend with irregular fluctuations: <b>D</b>.','VCAA 2025 General Mathematics Exam 1 Q13–14 stem and Q14 (examiner report)',
  mc=['decreasing trend only','irregular fluctuations only','structural change only','decreasing trend with irregular fluctuations'],key='D',dist=[13,1,1,85]))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q3','Review of 1E (last term)',
  ('<div style="font-size:19px">The histogram below displays the population density, in people per km<sup>2</sup>, of the 27 countries in the European Union in 2021. The histogram has a logarithmic (base 10) scale.</div>',
   IMG('dn2.png',560),'<div style="font-size:19px">The median value occurs in a column with a frequency of</div>'),
  [('Position','27 values: median = 14th value'),('Count up','2, 2, 2 → 6 · + 6 → 12 · + 9 → 21'),('Column','the 14th value is in the column 2.0–2.2, frequency 9')],
  'Frequency of <b>9</b>: <b>D</b>.','VCAA 2024 General Mathematics Exam 1 Q3–4 stem and Q3 (examiner report)',
  mc=['2','3','6','9'],key='D',dist=[18,5,7,71]))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q2ci','Review of 1G (last term)',
  ('<div style="font-size:19px">The boxplot below displays the distribution of all gold medal-winning heights for the women’s high jump, <i>Wgold</i>, in metres, for the 19 Olympic Games held from 1948 to 2020.</div>',
   IMG('dn3.png',540),'<div style="font-size:19px">c. i. Using the boxplot, <b>show that</b> the lower fence is 1.565 m and the upper fence is 2.325 m. <span class="muted">(1 mark)</span></div>'),
  [('Read off','Q<sub>1</sub> = 1.85 · Q<sub>3</sub> = 2.04'),fx('IQR','IQR',F(V('Q3','2.04'),' − ',V('Q1','1.85')),'0.19'),
   fx('LF','LF',F(V('Q1','1.85'),' − 1.5 × ',V('IQR','0.19')),'1.565'),fx('UF','UF',F(V('Q3','2.04'),' + 1.5 × ',V('IQR','0.19')),'2.325')],
  'Lower fence = 1.85 − 1.5 × 0.19 = <b>1.565 m</b>; upper fence = 2.04 + 1.5 × 0.19 = <b>2.325 m</b>.','VCAA 2024 General Mathematics Exam 2 Q2 stem and Q2ci (examiner report: 84% full marks)',
  stat=('mark',84),cmd=('show that',1,'IQR, then both fences')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q4b','Review of 5C (last term)',
  ('<div style="font-size:18px">The time series plot below shows the average monthly ice cream <i>consumption</i> recorded over three years, from January 2010 to December 2012. The data for the graph was recorded in the Northern Hemisphere. In this graph, month number 1 is January 2010, month number 2 is February 2010 and so on.</div>',
   IMG('dn4.png',430),'<div style="font-size:18px">b. The long-term seasonal index for April is 1.05.<br><b>Determine</b> the deseasonalised value for average monthly ice cream <i>consumption</i> in April 2010 (month 4).<br>Round your answer to two decimal places. <span class="muted">(1 mark)</span></div>'),
  [('Read off','month 4: consumption = 0.18'),fx('Deseasonalise','deseasonalised',F(FR([V('actual','0.18')],[V('SI','1.05')])),'0.1714…')],
  'Deseasonalised consumption in April 2010 = <b>0.17</b> litres/person.','VCAA 2023 General Mathematics Exam 2 Q4 stem and Q4b (examiner report: 72% full marks)',
  stat=('mark',72),cmd=('Determine',1,'actual ÷ SI')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3A #2','Finding the rule for a sequence',
  '<div style="font-size:30px;margin-top:40px">Look for a pattern or rule in the following sequence, and hence find the next number:<br><br>3, 7, 11, 15, 19, ...</div>',
  [('Differences','7 − 3 = 4, 11 − 7 = 4, …: the same each time'),('Rule','add 4 to each term'),('Next','19 + 4 = 23')],
  'Rule: add 4. The next number is <b>23</b>.',f'{CAM12} · Ch 3 skills checklist 3A #2 · solution worked for 12MAG',cmd=('find',None,'the rule, then apply it')))
S.append(qslide('apk','APK · VCAA 2015 Exam 1 Q1','Next term of a sequence',
  '<div style="font-size:30px;margin-top:40px">The first four terms in a geometric sequence are: 5, 10, 20, 40, ...<br><br>The fifth term in this sequence is</div>',
  [('Rule','10 ÷ 5 = 2, 20 ÷ 10 = 2: multiply by 2'),('Next','40 × 2 = 80')],
  '80: <b>D</b>.',f'VCAA 2015 Further Mathematics Exam 1 Number patterns Q1 · {EDR12} 3A Q12 (no 2015 examiner report on file)',
  mc=['45','50','60','80','100'],key='D'))

# ================= Learn 1: sequences and rules
S.append(learn('Learn · 7A','Sequences and rules',
  '<h4>A starting value + a rule</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>a <b>sequence</b> is a list of numbers (<b>terms</b>) in order</li><li>‘…’ means the sequence keeps going</li>'
  '<li><b>recursion</b>: apply the same rule to each term to get the next one</li></ul>',
  '<div style="font-size:22px;text-align:center">Start with 1, rule ‘add 2 to each term’:</div>'+chain([1,3,5,7,9],'+2')+
  '<div class="frag" style="font-size:22px;text-align:center;margin-top:10px">A calculator remembers the last answer (<b>ans</b>), so it can repeat the rule for you: type the start, then the rule, then keep pressing enter.</div>',
  'Write the starting value as the first term: it counts as one of the ‘first five terms’.',f'{CAM}, 7A pp. 334–335 (own words) · {EDR}, 5A',
  cards=(kcard('Sequence','1, 3, 5, 7, 9, …'),)))

# ================= Ex 1 / YT-7A-1
S.append(qslide('we','Worked example 1 · 7A','Generating a sequence of terms recursively (1)',
  '<div style="font-size:28px;margin-top:40px">Write down the first five terms of the sequence with a starting value of 6 and the rule ‘add 4 to the previous term’.</div>',
  [('Start','6'),('Rule','6 + 4 = 10'),('Repeat','10 + 4 = 14 · 14 + 4 = 18 · 18 + 4 = 22')],
  'The first five terms are <b>6, 10, 14, 18, 22</b>.',f'{CAM} · Example 1 (p. 334)',video='Cambridge GO · Example 1 (7A Resources)',cmd=('Write down',None,'start, then apply the rule 4 times')))
S.append(qslide('yt','You try · written for 12MAG','Generating a sequence of terms recursively (1)',
  '<div style="font-size:28px;margin-top:40px">Write down the first five terms of the sequence with a starting value of 9 and the rule ‘add 7 to the previous term’.</div>',
  [('Start','9'),('Rule','9 + 7 = 16'),('Repeat','16 + 7 = 23 · 23 + 7 = 30 · 30 + 7 = 37')],
  'The first five terms are <b>9, 16, 23, 30, 37</b>.','Written for 12MAG (modelled on Cambridge Example 1; no Edrolo match) · YT-7A-1',cmd=('Write down',None,'start, then apply the rule 4 times')))
# ================= Ex 2 / YT-7A-2
S.append(qslide('we','Worked example 2 · 7A','Generating a sequence of terms recursively (2)',
  '<div style="font-size:28px;margin-top:40px">Write down the first five terms of the sequence with a starting value of 5 and the rule ‘double the number and then subtract 3’.</div>',
  [('Start','5'),('Rule','5 × 2 − 3 = 7'),('Repeat','7 × 2 − 3 = 11 · 11 × 2 − 3 = 19 · 19 × 2 − 3 = 35')],
  'The first five terms are <b>5, 7, 11, 19, 35</b>.',f'{CAM} · Example 2 (p. 335)',video='Cambridge GO · Example 2 (7A Resources)',cmd=('Write down',None,'start, then apply the rule 4 times')))
S.append(qslide('yt','You try · written for 12MAG','Generating a sequence of terms recursively (2)',
  '<div style="font-size:28px;margin-top:40px">Write down the first five terms of the sequence with a starting value of 4 and the rule ‘triple the number and then subtract 5’.</div>',
  [('Start','4'),('Rule','4 × 3 − 5 = 7'),('Repeat','7 × 3 − 5 = 16 · 16 × 3 − 5 = 43 · 43 × 3 − 5 = 124')],
  'The first five terms are <b>4, 7, 16, 43, 124</b>.','Written for 12MAG (modelled on Cambridge Example 2; no Edrolo match) · YT-7A-2',cmd=('Write down',None,'start, then apply the rule 4 times')))
# ================= Ex 3 / Edrolo WE5
S.append(qslide('we','Worked example 3 · 7A','Generating a sequence of numbers with a calculator',
  '<div style="font-size:28px;margin-top:40px">Use a calculator to generate the first five terms of the sequence with a starting value of 5 and the rule ‘double and then subtract 3’.</div>',
  [('Start','type 5, press enter (TI) / EXE (ClassPad)'),('Rule','type × 2 − 3, press enter: screen shows ‘5·2−3’ (TI) or ‘ans × 2 − 3’ (ClassPad) → 7'),
   ('Repeat','press enter 3 more times → 11, 19, 35')],
  'The first five terms are <b>5, 7, 11, 19, 35</b>.',f'{CAM} · Example 3 (pp. 335–336)',video='Cambridge GO · Example 3 (7A Resources)',cmd=('Use a calculator',None,'start, rule, then keep pressing enter')))
S.append(qslide('yt','You try · Edrolo 5A WE5','Generating a sequence with a calculator',
  '<div style="font-size:28px;margin-top:40px">Use a calculator to find the first five terms of the sequence given by the following geometric recurrence relation, correct to two decimal places.<br><br>'
  +RR('2.12','−3.76 × <i>B<sub>n</sub></i>','B')+'</div>',
  [('Read','start 2.12; rule ‘multiply by −3.76’'),('CAS','type 2.12, enter · type × −3.76, enter → −7.9712'),('Repeat','enter 3 more times → 29.9717… · −112.6936… · 423.7280…')],
  '<b>2.12, −7.97, 29.97, −112.69, 423.73</b>',f'{EDR} · 5A Worked example 5 (pp. 299–300)',cmd=('Use a calculator',None,'two decimal places')))

# ================= Learn 2: recurrence relations
S.append(learn('Learn · 7A','Recurrence relations',
  '<h4>Two parts: a starting value and a rule</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>V<sub>n</sub></i> = the term after <i>n</i> applications of the rule</li><li><i>V</i><sub>0</sub> = starting value (no applications yet)</li>'
  '<li><i>V</i><sub><i>n</i>+1</sub> = next term, worked out from the current term <i>V<sub>n</sub></i></li></ul>',
  '<table class="t" style="font-size:22px;margin:6px auto"><tr><th>In words</th><th>In symbols</th></tr><tr class="frag"><td>Starting value = 10</td><td><i>V</i><sub>0</sub> = 10</td></tr>'
  '<tr class="frag"><td>Next term = current term + 5</td><td><i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + 5</td></tr></table>'
  '<div class="frag" style="font-size:22px;text-align:center;margin-top:6px">'+RR('10','<i>V<sub>n</sub></i> + 5')+' generates</div><div class="frag">'+terms([10,15,20,25,30])+'</div>',
  'The first term is <i>V</i><sub>0</sub>, so the fifth term is <i>V</i><sub>4</sub>: count from zero.',f'{CAM}, 7A pp. 336 and 338 (own words) · {EDR}, 5A',
  cards=(kcard('Recurrence relation',RR('10','<i>V<sub>n</sub></i> + 5')),)))
# ================= Ex 4 / Edrolo WE4a
S.append(qslide('we','Worked example 4 · 7A','Generating a sequence from a recurrence relation',
  '<div style="font-size:28px;margin-top:40px">Write down the first five terms of the sequence defined by the recurrence relation<br><br>'+RR('29','<i>V<sub>n</sub></i> − 4')+'</div>',
  [('Start','<i>V</i><sub>0</sub> = 29'),fx('V1','<i>V</i><sub>1</sub>',F(V('V0','29'),' − 4'),'25'),('Repeat','<i>V</i><sub>2</sub> = 25 − 4 = 21 · <i>V</i><sub>3</sub> = 21 − 4 = 17 · <i>V</i><sub>4</sub> = 17 − 4 = 13')],
  'The first five terms are <b>29, 25, 21, 17, 13</b>.',f'{CAM} · Example 4 (p. 337)',video='Cambridge GO · Example 4 (7A Resources)',cmd=('Write down',None,'V₀ to V₄')))
S.append(qslide('yt','You try · Edrolo 5A WE4a','Generating a sequence from a recurrence relation',
  '<div style="font-size:28px;margin-top:40px">Find the first five terms of the sequence given by the following recurrence relations.<br><br>a. '+RR('42','<i>H<sub>n</sub></i> − 3.5','H')+'</div>',
  [('Start','<i>H</i><sub>0</sub> = 42'),fx('H1','<i>H</i><sub>1</sub>',F(V('H0','42'),' − 3.5'),'38.5'),('Repeat','<i>H</i><sub>2</sub> = 38.5 − 3.5 = 35 · <i>H</i><sub>3</sub> = 31.5 · <i>H</i><sub>4</sub> = 28')],
  '<b>42, 38.5, 35, 31.5, 28</b>',f'{EDR} · 5A Worked example 4a (p. 299)',cmd=('Find',None,'H₀ to H₄')))
# ================= Ex 5 / Edrolo WE4b
S.append(qslide('we','Worked example 5 · 7A','Using a calculator to generate sequences from recurrence relations',
  '<div style="font-size:26px;margin-top:30px">A sequence is generated by the recurrence relation<br><br>'+RR('300','0.5<i>V<sub>n</sub></i> − 9')+'<br><br>Use your calculator to generate this sequence and determine how many terms at the start of the sequence are positive.</div>',
  [('Start','type 300, press enter'),('Rule','type × 0.5 − 9, press enter → 141'),('Repeat','enter → 61.5 · 21.75 · 1.875 · <b>−8.625</b> (first negative term)'),('Count','300, 141, 61.5, 21.75, 1.875: five positive terms')],
  'The first <b>five</b> terms of the sequence are positive.',f'{CAM} · Example 5 (p. 337)',video='Cambridge GO · Example 5 (7A Resources)',cmd=('determine',None,'keep pressing until a term is negative')))
S.append(qslide('yt','You try · Edrolo 5A WE4b','Generating a sequence from a recurrence relation',
  '<div style="font-size:28px;margin-top:40px">Find the first five terms of the sequence given by the following recurrence relations.<br><br>b. '+RR('2','4<i>Y<sub>n</sub></i> − 3','Y')+'</div>',
  [('Start','<i>Y</i><sub>0</sub> = 2'),fx('Y1','<i>Y</i><sub>1</sub>',F('4 × ',V('Y0','2'),' − 3'),'5'),('Repeat','<i>Y</i><sub>2</sub> = 4 × 5 − 3 = 17 · <i>Y</i><sub>3</sub> = 65 · <i>Y</i><sub>4</sub> = 257 (or on CAS: 2, enter, × 4 − 3, enter …)')],
  '<b>2, 5, 17, 65, 257</b>',f'{EDR} · 5A Worked example 4b (p. 299)',cmd=('Find',None,'Y₀ to Y₄')))
# ================= Ex 6 / Edrolo U1&2 3B WE1
S.append(qslide('we','Worked example 6 · 7A','Naming terms in a sequence',
  '<div style="font-size:26px;margin-top:30px">Consider the recurrence relation<br><br>'+RR('3','<i>V<sub>n</sub></i> + 6')+'<br><br>State the values of:</div>'
  +plist([('a','<i>V</i><sub>1</sub>'),('b','<i>V</i><sub>4</sub>'),('c','<i>V</i><sub>5</sub>')]),
  [('Terms','write the sequence with each name under its value'+terms([3,9,15,21,27,33],22))],
  '',f'{CAM} · Example 6 (p. 338)',video='Cambridge GO · Example 6 (7A Resources)',cmd=('State',None,'name each term, V₀ first'),
  parts=[('a','<i>V</i><sub>1</sub> = <b>9</b>'),('b','<i>V</i><sub>4</sub> = <b>27</b>'),('c','<i>V</i><sub>5</sub> = <b>33</b>')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3B WE1','Naming terms in a sequence',
  '<div style="font-size:28px;margin-top:40px">Consider the following recurrence relation.<br><br>'+RR('3','<i>u<sub>n</sub></i> + 6','u')+'<br><br><b>Calculate</b> the value of <i>u</i><sub>3</sub>.</div>',
  [fx('u1','<i>u</i><sub>1</sub>',F(V('u0','3'),' + 6'),'9'),fx('u2','<i>u</i><sub>2</sub>',F(V('u1','9'),' + 6'),'15'),fx('u3','<i>u</i><sub>3</sub>',F(V('u2','15'),' + 6'),'21')],
  '<i>u</i><sub>3</sub> = <b>21</b>',f'{EDR12} · 3B Worked example 1 (p. 133)',cmd=('Calculate',None,'u₁, u₂, then u₃')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['recursion-sequence']
S.append(cas('CAS · 7A','Generating a sequence from a recurrence relation',
  '<p style="font-size:24px">A sequence is generated by the recurrence relation</p><p style="font-size:28px;text-align:center">'+RR('300','0.5<i>V<sub>n</sub></i> − 9')+'</p>'
  '<p style="font-size:24px">Generate the sequence on CAS and name each term: the first press after the rule gives <i>V</i><sub>1</sub>.</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'300, 141, 61.5, 21.75, 1.875, −8.625 → <i>V</i><sub>5</sub> = −8.625 is the first negative term',
  f'{CAM} · Example 5 (p. 337) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2017 Exam 1 Q18','Show what you know',
  '<div style="font-size:26px;margin-top:20px">The first five terms of a sequence are 2, 6, 22, 86, 342 …<br>The recurrence relation that generates this sequence could be</div>',
  [('Test B','2 × 2 + 2 = 6 ✓ but 2 × 6 + 2 = 14 ✗'),('Test D','4 × 2 − 2 = 6 ✓ · 4 × 6 − 2 = 22 ✓ · 4 × 22 − 2 = 86 ✓')],
  '<i>P</i><sub><i>n</i>+1</sub> = 4<i>P<sub>n</sub></i> − 2: <b>D</b>.',f'VCAA 2017 Further Mathematics Exam 1 Recursion and financial modelling Q18 (examiner report) · {EDR} 5A Q17',
  mc=[RR('2','<i>P<sub>n</sub></i> + 4','P'),RR('2','2<i>P<sub>n</sub></i> + 2','P'),RR('2','3<i>P<sub>n</sub></i>','P'),RR('2','4<i>P<sub>n</sub></i> − 2','P'),RR('2','5<i>P<sub>n</sub></i> − 4','P')],key='D',dist=[2,3,2,92,1]))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2021 Exam 1 Q17','Show what you know',
  '<div style="font-size:26px;margin-top:20px">The following recurrence relation can generate a sequence of numbers.<br><br>'+RR('37','<i>L<sub>n</sub></i> + <i>C</i>','L')+'<br><br>The value of <i>L</i><sub>2</sub> is 25.<br>The value of <i>C</i> is</div>',
  [('Terms','<i>L</i><sub>2</sub> = 37 + <i>C</i> + <i>C</i> = 37 + 2<i>C</i>'),('Solve','37 + 2<i>C</i> = 25 → 2<i>C</i> = −12 → <i>C</i> = −6')],
  '<i>C</i> = −6: <b>A</b>.',f'VCAA 2021 Further Mathematics Exam 1 Recursion and financial modelling Q17 (examiner report) · {EDR} 5A Q19',
  mc=['–6','–4','4','6','37'],key='A',dist=[83,5,4,6,2]))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2019 Exam 1 Q17','Show what you know',
  '<div style="font-size:26px;margin-top:20px">Consider the recurrence relation shown below.<br><br>'+RR('3','2<i>A<sub>n</sub></i> + 4','A')+'<br><br>The value of <i>A</i><sub>3</sub> in the sequence generated by this recurrence relation is given by</div>',
  [('A1','2 × 3 + 4 = 10'),('A2','2 × 10 + 4 = 24'),('A3','2 × 24 + 4')],
  '<i>A</i><sub>3</sub> = 2 × 24 + 4: <b>D</b>.',f'VCAA 2019 Further Mathematics Exam 1 Recursion and financial modelling Q17 (examiner report; original wording) · {EDR} 5A Q20',
  mc=['2 × 3 + 4','2 × 4 + 4','2 × 10 + 4','2 × 24 + 4','2 × 52 + 4'],key='D',dist=[16,2,7,68,6],dis=('A','2 × 3 + 4 is A₁: counting A₀ as the first application')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 7 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('7A',) and v.get('url')]))
n=assemble(S,'12MAG · L31 · Sequences and recurrence relations',os.path.join(ROOT,'lessons','7A slides.html'))
print(n-1,'slides')
