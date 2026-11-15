"""Lesson l06 (2F) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2F slides.html
Run: python3 tools/deck/l06/build.py      Screenshots: python3 tools/deck/l06/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- CFAT 1.2.2 (2C-2D) at the start (planner card: 'Start of the 2F lesson').
- Do Now: VCAA 2025 NHT Exam 1 Q9 (answer B; NHT report gives no %) — REPLACES the card's VCAA 2024 E1 Q10, which the index tagged 2E
          but is a least-squares prediction question (3B, not yet taught; see QUEUE Decisions log) ·
          VCAA 2024 Exam 1 Q5 (C, 80%; A 10 B 4 D 6) · VCAA 2023 Exam 2 Q3c (average 0.6/1 → 60%; answer strong, positive, linear) ·
          VCAA 2024 NHT Exam 2 Q1c (2 marks; NHT report gives no %; report: LF = 0.39 − 1.5 × 0.26 = 0, 0.22 > 0).
- APK (planner card): Cambridge U1&2 Ch 7 skills checklist 7C #4 and #5 (height/foot length data of 7B #2, p. 457; no printed answers:
  solutions written for 12MAG, r = 0.657 on CAS → moderate) · VCAA 2016 Further Exam 1 Q12 (= Edrolo U1&2 6B Q15 'adapted';
  original VCAA wording with 5 options; report: D 67%, A 11 B 8 C 3 E 11).
- Learn: Cambridge Units 3&4 2F pp. 140-144 (r properties, classification table, warning).
- CAS: planner/cas-skills.json 'correlation-r'; task = Cambridge 2F CAS 2 (income / CO2, 11 countries). r = 0.818 (the ClassPad page's value;
  the TI page prints 0.8342, which is a misprint: checked on the data).
- Worked example: Cambridge Units 3&4 Example 16 (p. 144). You try: Edrolo U3&4 2D Worked example 1 (pp. 146-148, grade vs lectures).
- Exit: Edrolo U3&4 2C Q17 = VCAA 2020 Further Exam 2 Core Q6b (report: average 0.5/1 → 50%; answer 'Strong negative'); original wording.
- Videos: videos.json (2F MaffsGuru link, draft).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'

def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:8px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def table(head,rows,fs=19,rid='',extra=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td><span data-i="{i}">{c}</span></td>' for c in r)+'</tr>' for i,r in enumerate(rows))
    return f'<table class="t"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}">'+(f'<tr>{th}</tr>' if head else '')+f'{tr}</table>'
STR=[('0.75 ≤ <i>r</i> ≤ 1','strong positive'),('0.5 ≤ <i>r</i> &lt; 0.75','moderate positive'),('0.25 ≤ <i>r</i> &lt; 0.5','weak positive'),('−0.25 &lt; <i>r</i> &lt; 0.25','no association'),
     ('−0.5 &lt; <i>r</i> ≤ −0.25','weak negative'),('−0.75 &lt; <i>r</i> ≤ −0.5','moderate negative'),('−1 ≤ <i>r</i> ≤ −0.75','strong negative')]
strt=lambda rid,fs=16:table(['<i>r</i>','linear association'],[[a,b] for a,b in STR],fs=fs,rid=rid)

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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l06')
yid=lambda u:u.split('v=')[1].split('&')[0]

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.T .mc>div{padding-right:54px}'
   '.tight td,.tight th{padding:2px 5px!important}#lst{font-size:15px!important;width:56%;margin:auto}#lst td,#lst th{padding:1px 10px!important;line-height:1.25}.rg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center;font-weight:700;font-size:17px}</style>']
# ================= opening
S.append(title(6,'Strength of a linear relationship: the correlation coefficient',f'{CAM} · 2F Strength of a linear relationship: the correlation coefficient','L06',
  flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')).replace('font-size:84px','font-size:64px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('CFAT 1.2.2','· 2C–2D, about 20 minutes','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 skills','var(--apk)'),
  ('What r measures','',None),('Classifying r','',None),('CAS: finding r','',None),('Worked example 16','→ You try',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mini=lambda r,s=3:W_(150,SC(rcloud(r,30,s),(-2.6,2.6),(-2.6,2.6),9,9,W=170,H=130,r=3.5,grid=False,ticks=False))
S.append(keys([
  ('Pearson’s correlation coefficient, <i>r</i>','measures the strength and direction of a <b>linear</b> association; −1 ≤ <i>r</i> ≤ 1',mini(0.8)),
  ('Sign of <i>r</i>','positive association → <i>r</i> &gt; 0 · negative association → <i>r</i> &lt; 0 · no association → <i>r</i> close to 0'),
  ('Strength from <i>r</i>','the closer <i>r</i> is to −1 or +1, the stronger the linear association'),
  ('Use <i>r</i> only if','the variables are numerical, the association is linear and there are no clear outliers')],
  [('Correlation coefficient',F('<i>r</i> = ',FR(['Σ(<i>x</i> − <i>x̄</i>)(<i>y</i> − <i>ȳ</i>)'],['(<i>n</i> − 1)<i>s<sub>x</sub></i><i>s<sub>y</sub></i>'])),'(optional: we use CAS)'),
   ('Strength guide',F('|<i>r</i>| ≥ 0.75 strong · 0.5 to 0.75 moderate'),'0.25 to 0.5 weak · below 0.25 no association')],
  f'{CAM}, 2F pp. 140–144'))
S.append(cfat('CFAT 1.2.2','Numerical vs categorical variables; scatterplots','2C–2D',16,'CFAT 1.2.2 (2C–2D) · Edrolo U3&amp;4 exercise questions'))

# ================= Do Now 1: VCAA 2025 NHT E1 Q9 (2E)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 NHT Exam 1 Q9','Review of 2E',
  G('The scatterplot below shows the <em class="v">test scores</em> and the <em class="v">study time</em> in hours for students in a class. A least squares line has been added to the scatterplot.',
    W_(470,SC(STUDY,(0,4.5),(0,100),0.5,10,'study time (hours)','test scores',W=560,H=300,r=4.5,fs=13,tl=((0,35),(4,97)),tl_hid=False,sid='d1s')),
    'From the scatterplot, it can be concluded that a'),
  [('Direction','the points trend upwards from left to right: positive','data-hi="#d1s|p|hy"'),
   ('Association, not cause','a scatterplot shows an association; it cannot show that one variable causes the other')],
  'Longer study time goes with higher test scores: <b>B</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q9 (examiner report: answer only, no %; scatterplot redrawn)',
  mc=['longer time spent studying causes a higher test score.','longer time spent studying is associated with a higher test score.',
      'shorter time spent studying is associated with a higher test score.','shorter time spent studying causes a higher test score.'],key='B',
  dis=('A','‘causes’: an association alone never shows cause and effect (more in 2H).')))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide sm"',1)
# ================= Do Now 2: VCAA 2024 E1 Q5 (1G)
sib='<table class="t" id="d2t" style="font-size:20px;margin:6px auto">'+''.join('<tr>'+''.join(f'<td style="padding:3px 12px"><span data-i="v{v}">{v}</span></td>' for v in row)+'</tr>' for row in SIB)+'</table>'
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q5','Review of 1G',
  G('The number of siblings of each member of a class of 24 students was recorded.<br>The results are displayed in the table below.',sib,
    'A boxplot was constructed to display the spread of the data.<br>Which one of the following statements about this boxplot is correct?'),
  [('Count','1 × 12 · 2 × 7 · 3 × 3 · 4 × 2 (24 values)','data-hi="#d2t|v1|hy"'),
   ('Median','between the 12th (1) and 13th (2) values: <b>1.5</b>'),
   ('Check the rest','Q1 = 1, Q3 = 2 → IQR = 1 (B ✗) · UF = 2 + 1.5 × 1 = 3.5 → the 4s are outliers (A ✗) · median 1.5 (D ✗)','data-hi="#d2t|v4|hc"')],
  'The value of the median is 1.5: <b>C</b>.','VCAA 2024 General Mathematics Exam 1 Q5 (examiner report)',
  mc=['There are no outliers.','The value of the interquartile range (IQR) is 1.5','The value of the median is 1.5','All of the five-number summary values are whole numbers.'],key='C',dist=[10,4,80,6],
  dis=('A','10% missed that 4 &gt; 3.5 = UF, so both 4s are outliers.')))
# ================= Do Now 3: VCAA 2023 E2 Q3c (2E)
T3=('<table class="t" style="font-size:14px"><tr><th>strength</th><td style="min-width:150px"><span class="blank d31"><span class="ph">&nbsp;</span><span class="fill">strong</span></span></td></tr>'
    '<tr><th>direction</th><td><span class="blank d32"><span class="ph">&nbsp;</span><span class="fill">positive</span></span></td></tr>'
    '<tr><th>form</th><td><span class="blank d33"><span class="ph">&nbsp;</span><span class="fill">linear</span></span></td></tr></table>')
T3Q='<table class="t" style="font-size:14px">'+''.join(f'<tr><th>{k}</th><td style="min-width:150px">&nbsp;</td></tr>' for k in ('strength','direction','form'))+'</table>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2023 Exam 2 Q3c','Review of 2E',
  G('The scatterplot below plots the average monthly ice cream <em class="v">consumption</em>, in litres/person, against average monthly <em class="v">temperature</em>, in °C. The data for the graph was recorded in the Northern Hemisphere.',
    W_(330,SC(ICE,(-10,25),(0.10,0.22),5,0.01,'temperature (°C)','consumption (litres/person)',W=480,H=270,r=4.5,fs=12,tl=((-10,0.1164),(25,0.2004)),sid='d3s')),
    'When a least squares line is fitted to the scatterplot, the equation is found to be:<br><span style="margin-left:40px"><em>consumption</em> = 0.1404 + 0.0024 × <em>temperature</em></span><br>The coefficient of determination is 0.7212<br>'
    'c. Describe the association between average monthly ice cream <em class="v">consumption</em> and average monthly <em class="v">temperature</em> in terms of strength, direction and form. <span class="muted">(1 mark)</span>'+T3Q),
  [('Strength','<i>r</i> = √0.7212 = 0.849 ≥ 0.75: strong (use <i>r</i>, not <i>r</i>²)','data-fill="d31"'),
   ('Direction','the points trend upwards: positive','data-fill="d32"'),
   ('Form','scattered about a straight line: linear','data-show="#d3s|tl" data-fill="d33"'),
   ('TMPL',T3,'','data-stat="60"')],
  '','VCAA 2023 General Mathematics Exam 2 Q3c (examiner report: some wrote ‘moderate’ from <i>r</i>² instead of <i>r</i>; scatterplot redrawn)',stat=('mark',60),cmd=('Describe',1,'strength, direction, form')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2024 NHT E2 Q1c (1G)
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q1c','Review of 1G',
  'Data was collected to investigate the behaviour of tides in Sydney Harbour.<br>The variables in this study were:<br>• <em class="v">Day</em>: the day number in the sample<br>• <em class="v">LLT</em>: the height of the lowest low tide for that day (in metres)<br>• <em class="v">HHT</em>: the height of the highest high tide for that day (in metres)'
  '<div style="margin-top:12px">c. The five-number summary of the <em class="v">LLT</em> data is shown in Table 2 below.</div><div style="font-weight:700;font-size:15px;margin-top:6px">Table 2</div>'
  +table(['Minimum','Q1','Median','Q3','Maximum'],[['0.22','0.39','0.52','0.65','0.73']],fs=18,rid='d4t')+
  '<div style="margin-top:10px">Show that the minimum <em class="v">LLT</em> value of 0.22 m is <b>not</b> an outlier. <span class="muted">(2 marks)</span></div>',
  [fx('IQR','IQR',F('0.65 − 0.39'),'0.26'),
   fx('Lower fence','LF',F('Q1 − 1.5 × IQR = 0.39 − 1.5 × ',V('IQR','0.26')),'0'),
   ('Compare','0.22 &gt; 0 = LF → <b>not</b> an outlier')],
  'As 0.22 &gt; 0 (the lower fence), the minimum <em class="v">LLT</em> value of 0.22 m is not an outlier.','VCAA 2024 (NHT) General Mathematics Exam 2 Q1c (NHT report: worked answer, no %)',cmd=('Show',2,'fence, then compare')))

# ================= APK 1: Cambridge U1&2 7C #4
r_foot=corr(*zip(*FOOT))
FS=SC(FOOT,(150,190),(15,45),5,5,'height (cm)','foot length (cm)',W=420,H=300,r=5,fs=13,sid='a1s')
gal='<div class="rg" style="grid-template-columns:repeat(2,1fr);font-size:14px">'+''.join(f'<div>{mini(r,7+k)}r = {r}</div>' for k,r in enumerate([0.3,0.5,0.7,0.9]))+'</div>'
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7C #4','Estimating and calculating r',
  '<div>Height (<em class="v">height</em>) and foot length (<em class="v">foot length</em>) of 16 students, in centimetres (data from 7B #2):</div>'
  '<div style="display:flex;gap:10px;align-items:center;margin:6px 0"><div style="flex:none;width:330px">'+FS+'</div>'+'<div style="flex:1">'+gal+'</div></div>'
  '<div>Estimate the value of the correlation coefficient, <i>r</i>, between height and foot length by comparing the scatterplot to those on page 420, and then use your calculator to find its exact value. Give your answer rounded to three decimal places.</div>',
  [('Estimate','positive, more scattered than r = 0.9, about like r = 0.7: <i>r</i> ≈ 0.6 to 0.7','data-hi="#a1s|p|hy"'),
   ('CAS','lists height (EV) and foot (RV) → corrMat / Linear Reg → <i>r</i> = 0.6567…')],
  f'<i>r</i> ≈ 0.7 (estimate); <i>r</i> = <b>{r_foot:.3f}</b>',f'{CAM12} · Ch 7 skills checklist 7C #4 (data from 7B #2, p. 457; plots drawn for 12MAG; ‘page 420’ = the r gallery in Cambridge U1&amp;2) · solution written for 12MAG',
  cmd=('Estimate',None,'then CAS, 3 d.p.')))
S[-1]=S[-1].replace('<section class="slide T apk"','<section class="slide T apk sm"',1)
# ================= APK 2: Cambridge U1&2 7C #5
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7C #5','Classifying the strength of r',
  G('Use the table on page 428 to classify the value of the correlation coefficient, <i>r</i>, between height and foot length as weak, moderate or strong.',strt('a2t',17),''),
  [('Locate',f'<i>r</i> = {r_foot:.3f}: 0.5 ≤ {r_foot:.3f} &lt; 0.75','data-hi="#a2t|1|hy"')],
  f'<i>r</i> = {r_foot:.3f}: a <b>moderate</b> positive linear association.',f'{CAM12} · Ch 7 skills checklist 7C #5 (‘page 428’ = the strength table, same as Cambridge U3&amp;4 p. 143) · solution written for 12MAG',cmd=('classify',None,'use the table')))
# ================= APK 3: VCAA 2016 E1 Q12
S.append(qslide('apk','APK · Year 11 · VCAA 2016 Exam 1 Q12','Interpreting an association',
  'There is a strong positive association between a country’s Human Development Index and its carbon dioxide emissions.<br>From this information, it can be concluded that',
  [('Positive','higher values of one variable go with higher values of the other'),('Not cause','an association does not tell us that changing one variable changes the other: A and B ✗')],
  'Countries with higher HDI tend to have higher CO₂ emissions: <b>D</b>.',f'{EDR12} · 6B Q15 · VCAA 2016 Further Mathematics Exam 1 Q12 (examiner report; original wording)',
  mc=['increasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.','decreasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.',
      'this association must be a chance occurrence and can be safely ignored.','countries that have higher human development indices tend to have higher levels of carbon dioxide emissions.',
      'countries that have higher human development indices tend to have lower levels of carbon dioxide emissions.'],key='D',dist=[11,8,3,67,11],
  dis=('A','11% read ‘association’ as ‘cause’.')))

# ================= Learn: what r measures
row='<div class="rg">'+''.join(f'<div class="frag">{mini(r,11+k)}<span>r = {r:+g}</span></div>'.replace('r = +0<','r = 0<') for k,r in enumerate([-1,-0.7,-0.3,0,0.5,0.9,1]))+'</div>'
row=row.replace('grid-template-columns:repeat(4,1fr)','')
S.append(learn('Learn · 2F','Pearson’s correlation coefficient, r',
  '<h4>One number for a linear association</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>−1 ≤ <i>r</i> ≤ +1</li><li><b>sign</b> = direction: positive or negative</li>'
  '<li><b>size</b> = strength: closer to ±1 → points closer to a straight line</li><li><i>r</i> = ±1: perfect · <i>r</i> ≈ 0: no linear association</li></ul>',
  row.replace('class="rg"','class="rg" style="grid-template-columns:repeat(7,1fr);font-size:16px"'),
  'Read the sign for direction, then the size for strength.',f'{CAM}, 2F pp. 140–141 (plots drawn for 12MAG)',cards=(kcard('Pearson’s <i>r</i>','strength and direction of a linear association'),)))
# ================= Learn: classifying r
S.append(learn('Learn · 2F','Classifying the strength of a linear association',
  '<h4>Use the size of r</h4><p style="font-size:19px">Find where <i>r</i> sits in the table. Watch the ends: 0.75 is <b>strong</b>, 0.5 is <b>moderate</b>, 0.25 is <b>weak</b>.</p>'
  '<h4 style="margin-top:12px">Warning: only use r when</h4><ol style="font-size:18px;margin-left:24px;line-height:1.45"><li>the variables are numerical</li><li>the association is linear</li><li>there are no outliers</li></ol>',
  strt('lst',15),'Outliers or a curve make <i>r</i> misleading: look at the scatterplot first.',f'{CAM}, 2F pp. 143–144',
  frags='<span class="frag" data-hi="#lst|0,1,2|hg"></span><span class="frag" data-hi="#lst|3|hy"></span><span class="frag" data-hi="#lst|4,5,6|hb"></span><span class="frag" data-hi="#lst||"></span>',
  cards=(kcard('Strength guide','|<i>r</i>| ≥ 0.75 strong · 0.5–0.75 moderate · 0.25–0.5 weak · &lt; 0.25 none'),)))
# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['correlation-r']
S.append(cas('CAS · 2F','Finding the correlation coefficient r',
  '<p style="font-size:20px">The following data show the per capita income (in $’000) and the per capita carbon dioxide emissions (in tonnes) of 11 countries.</p>'
  f'<table class="t tight" style="font-size:12px;margin:10px 0"><tr><th>Income ($’000)</th>{"".join(f"<td>{x}</td>" for x in INC)}</tr><tr><th>CO<sub>2</sub> (tonnes)</th>{"".join(f"<td>{x}</td>" for x in CO2)}</tr></table>'
  '<p style="font-size:20px">Determine the value of Pearson’s correlation coefficient rounded to two decimal places.</p>'+W_(330,SC(list(zip(INC,CO2)),(0,25),(0,14),5,2,'income','co2',W=380,H=240,r=4.5,fs=12)),
  C['ti'],C['classpad'],f'<i>r</i> = {corr(INC,CO2):.4f}… = <b>0.82</b> (2 d.p.): a strong positive linear association.',
  f'{CAM} · 2F CAS 2 (pp. 142–143) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
# ================= WE16
S.append(qslide('we','Worked example 16 · 2F','Classifying the strength of a linear association',
  'Classify the strength of each of the following linear associations using the previous table:'
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 30px;font-size:24px;margin:14px 0 18px 10px"><div>a <i>r</i> = 0.35</div><div>b <i>r</i> = −0.507</div><div>c <i>r</i> = 0.992</div><div>d <i>r</i> = −0.159</div></div>'+strt('w16',17),
  [],'',f'{CAM} · Example 16 (p. 144)',video='Cambridge GO · Example 16 (2F Resources)',cmd=('Classify',None,'find r in the table'),
  parts=[('a','The value 0.35 is more than 0.25 and less than 0.5. That is, 0.25 ≤ <i>r</i> &lt; 0.5: <b>weak, positive</b>','data-hi="#w16|2|hy"'),
         ('b','The value −0.507 is more than −0.75 and less than −0.5. That is, −0.75 &lt; <i>r</i> ≤ −0.5: <b>moderate, negative</b>','data-hi="#w16|5|hy"'),
         ('c','The value 0.992 is more than 0.75 and less than 1. That is, 0.75 ≤ <i>r</i> ≤ 1: <b>strong, positive</b>','data-hi="#w16|0|hy"'),
         ('d','The value −0.159 is more than −0.25 and less than 0.25. That is, −0.25 &lt; <i>r</i> &lt; 0.25: <b>no association</b>','data-hi="#w16|3|hy"')]))
# ================= You try: Edrolo 2D WE1
S.append(qslide('yt','You try · Edrolo 2D WE1','Calculating and interpreting r',
  '<div>A survey followed the study habits of a group of first-year uni students with the aim of predicting their <em class="v">grade</em>, as a percentage, from the number of <em class="v">lectures attended</em>. The results are shown in the following table.</div>'
  +'<div style="display:flex;gap:12px;align-items:center;margin:6px 0">'+table([],[['<i>grade</i> (%)']+[str(g) for g in GRADE],['<i>lectures attended</i>']+[str(l) for l in LECT]],fs=15).replace('class="t"','class="t tight"')+'<div style="flex:none;width:220px">'+(SC(list(zip(LECT,GRADE)),(0,12),(40,100),2,10,'lectures attended','grade (%)',W=360,H=220,r=4.5,fs=12,sid='y1s'))+'</div></div>'+
  plist([('a','Is the Pearson correlation coefficient, <i>r</i>, an appropriate statistic for this data set?'),('b','Determine the value of the correlation coefficient. Give the value correct to two decimal places.'),
         ('c','If possible, describe the association between the variables in terms of strength, direction, and form.')]),
  [],'',f'{EDR} · 2D Worked example 1 (pp. 146–148)',cmd=('Determine',None,'r to 2 d.p.'),
  parts=[('a','RV <i>grade</i>, EV <i>lectures attended</i>; the scatterplot shows no curve, so the data is linear and numeric. Yes, the Pearson correlation coefficient is an appropriate statistic for this data set.','data-hi="#y1s|p|hy"'),
         ('b',f'CAS (X: lectures, Y: grade): <i>r</i> = {corr(LECT,GRADE):.4f}… → <b><i>r</i> = 0.85</b>'),
         ('c','0.75 ≤ 0.85 ≤ 1 → strong; 0.85 is positive → positive. <b>Strong, positive, linear association</b>')]))

# ================= Exit
EX=('<table class="t" style="font-size:12px"><tr><th></th><th colspan="7">Age group</th></tr><tr><th></th>'+''.join(f'<th>{g}</th>' for g in AGEGRP)+'</tr>'
    '<tr><th><i>Mean age</i> (years)</th>'+''.join(f'<td>{a}</td>' for a in AGE)+'</tr><tr><th><i>Mean height</i> (cm)</th>'+''.join(f'<td>{h}</td>' for h in HT)+'</tr></table>')
S.append(qslide('ex','Exit task · VCAA 2020 Exam 2 Q6b','Show what you know',
  '<div style="font-size:16px">The table below shows the <em class="v">mean age</em>, in years, and the <em class="v">mean height</em>, in centimetres, of 648 women from seven different age groups.</div><div style="margin:5px 0">'+EX+'</div>'
  '<div style="font-size:16px">A scatterplot displaying this data shows an association between the <em class="v">mean height</em> and the <em class="v">mean age</em> of these women. In an initial analysis of the data, a line is fitted to the data by eye, as shown.</div>'
  '<div style="display:flex;justify-content:center">'+W_(380,SC(list(zip(AGE,HT)),(20,90),(155,170),10,5,'mean age (years)','mean height (cm)',W=440,H=240,r=4.5,fs=12,tl=((19,168.2),(91,155.9)),tl_hid=False,sid='x1s'))+'</div>'
  '<div style="font-size:16px">b. Describe this association in terms of strength and direction. <span class="muted">(1 mark)</span></div>',
  [('Strength','the points lie very close to the line: strong','data-hi="#x1s|p|hy"'),('Direction','mean height decreases as mean age increases: negative')],
  'The association is <b>strong</b> and <b>negative</b>.',f'{EDR} · 2C Q17 · VCAA 2020 Further Mathematics Exam 2 Core Q6b (examiner report: some added information that negated a correct answer; original wording; scatterplot redrawn)',
  stat=('mark',50),cmd=('Describe',1,'strength and direction only')))
S[-1]=S[-1].replace('<section class="slide T ex"','<section class="slide T ex sm"',1)

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 2 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='2F' and v.get('url')]))
n=assemble(S,'12MAG · L06 · Correlation coefficient',os.path.join(ROOT,'lessons','2F slides.html'))
print(n-1,'slides')
