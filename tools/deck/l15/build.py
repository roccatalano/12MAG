"""Lesson l15 (4D) slides: Choosing and applying the appropriate transformation. Content only; templates in tools/deck/tpl/tpl.py.
Sources (all verbatim):
- Do Now: VCAA 2023 Exam 1 Q11 (60%), VCAA 2025 Exam 1 Q11 (81%), VCAA 2026 NHT Exam 2 Q1a, VCAA 2024 NHT Exam 2 Q1ai (NHT reports: answers only).
- APK: Cambridge U1&2 Ch 9 skills checklist 9E #11 (answer y = 3x^2 + 20, printed answers) and 9B #3 (graph redrawn);
  Edrolo U1&2 9B Q22 (adapted from VCAA 2021 Exam 2 Q2a: Edrolo's numbers, so no % tile; original paper not on G:).
- Learn: Cambridge U3&4 4D pp. 239-242 (own words). Figures = crops of the Cambridge pages (circle of transformations, Example 7 plots).
- Worked example: Cambridge U3&4 Example 7 (pp. 240-242; no data table printed, so the figures are crops).
- You try: Edrolo U3&4 3E Worked example 1d (p. 210-211; stem + table from WE1; the three models from parts a-c listed as context).
- CAS: planner/cas-skills.json 'transformation-check'; data = Edrolo 3E WE1 (the You try data).
- Exits: Edrolo U3&4 3D Q14 = VCAA 2009 Exam 1 Q12 (scatterplot cropped from Edrolo p. 204; pre-2016: no report %, rule 11);
  Edrolo U3&4 3E Q13 = VCAA 2020 Further Maths Exam 2 Q6d (original wording; average 0.6/2, examiner report; residual plot redrawn from the data).
Run: python3 tools/deck/l15/build.py"""
import os, sys, json, base64
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"img",f),"rb").read()).decode()}" style="width:{w}px;display:block">'
def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:8px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l15')
yid=lambda u:u.split('v=')[1].split('&')[0]
def rowtab(rows,fs=13,tid=''):
    return f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px">'+''.join('<tr><th>'+r[0]+'</th>'+''.join(f'<td>{v}</td>' for v in r[1:])+'</tr>' for r in rows)+'</table>'
def coltab(head,rows,fs=12,tid=''):
    return f'<table class="t tight"{" id="+chr(34)+tid+chr(34) if tid else ""} style="font-size:{fs}px"><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr>'+''.join('<tr>'+''.join(f'<td>{v}</td>' for v in r)+'</tr>' for r in rows)+'</table>'

FR=lambda n,d:f'<span style="display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1.05;font-size:.9em"><span style="border-bottom:1.5px solid currentColor;padding:0 3px">{n}</span><span style="padding:0 3px">{d}</span></span>'
S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}.xs ol.parts>li,.xs ol.parts>li *{font-size:15px!important;line-height:1.3!important}'
   '.tight td,.tight th{padding:2px 5px!important}.c4 .cas2 li{font-size:15px;line-height:1.3}.c4 .ytrow .ytf{height:110px!important;padding:0!important;aspect-ratio:auto!important}</style>']
def cls(c): S[-1]=S[-1].replace('<section class="slide T ','<section class="slide '+c+' T ',1)

# ================= opening
S.append(title(15,'Choosing and applying the appropriate transformation',f'{CAM} · 4D Choosing and applying the appropriate transformation','L15',
               flow=('Do Now','APK','Learn','Worked example','You try','CAS','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('The circle of transformations','',None),('Worked example 7','→ You try',None),('CAS: compare r² and residual plots','',None),('Exit tasks','· two VCAA questions','var(--ex)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('circle of transformations','shows which transformations may straighten each of the four curve shapes'),
  ('candidates','each shape has more than one possible transformation: try them all'),
  ('residual plot','the best transformation leaves no clear pattern in the residuals'),
  ('r²','the best transformation has the highest coefficient of determination')],
  [('Squared',F('<i>x</i>² or <i>y</i>²'),'stretches the high values'),
   ('Log',F('log<sub>10</sub> <i>x</i> or log<sub>10</sub> <i>y</i>'),'compresses the high values'),
   ('Reciprocal',F('1/<i>x</i> or 1/<i>y</i>'),'compresses the high values even more')],
  f'{CAM}, 4D pp. 239–242'))

# ================= Do Now 1: VCAA 2023 E1 Q11 (4C)
AGE=[10,8,13,9,11,14,6,4,12,7,5]; HT=[9.5,8.0,9.7,9.1,9.4,9.8,6.0,3.5,9.6,7.8,4.0]
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q11','Review of 4C',
  G('The table below shows the height, in metres, and the age, in years, for 11 plantation trees.<br>A scatterplot displaying this data is also shown.',
    '<div style="display:flex;gap:14px;align-items:center">'+coltab(['age (years)','height (m)','age (years)','height (m)'],[(AGE[k],HT[k],AGE[k+6] if k<5 else '',HT[k+6] if k<5 else '') for k in range(6)],11.5)
    +W_(300,SC(list(zip(AGE,HT)),(3,15),(2,11),1,1,'age (years)','height (m)',W=380,H=210,r=4,fs=10))+'</div>',
    'A reciprocal transformation applied to the variable <em class="v">age</em> can be used to linearise the scatterplot.<br>With '+FR('1','<em>age</em>')+' as the explanatory variable, the equation of the least squares line fitted to the linearised data is closest to'),
  [('Which variable?','1/age is x, height stays as y: height = a + b × 1/age'),('CAS','new column agerec = 1/age; Linear Reg: XList agerec, YList height'),('Read off','a = 13.04 · b = −40.22')],
  '<em>height</em> = 13.04 − 40.22 × '+FR('1','<em>age</em>')+': <b>D</b>.','VCAA 2023 General Mathematics Exam 1 Q11–12 stem and Q11 (examiner report; scatterplot redrawn from the table)',
  mc=['<em>height</em> = −13.04 + 40.22 × '+FR('1','<em>age</em>'),'<em>height</em> = −10.74 + 8.30 × '+FR('1','<em>age</em>'),'<em>height</em> = 2.14 + 0.63 × '+FR('1','<em>age</em>'),'<em>height</em> = 13.04 − 40.22 × '+FR('1','<em>age</em>'),'<em>height</em> = 16.56 − 22.47 × '+FR('1','<em>age</em>')],
  key='D',stat=('mc',60),dis=('A','A has the right numbers with the signs swapped: the slope is negative because 1/x reverses the order.')))
cls('xs')
# ================= Do Now 2: VCAA 2025 E1 Q11 (4B)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q11','Review of 4B',
  G('The table below shows the life expectancy in years, <em class="v">life</em>, and the number of doctors per 1000 people, <em class="v">doctors</em>, for a sample of 10 countries in 2024. A scatterplot displaying the data is also shown.',
    '<div style="display:flex;gap:14px;align-items:center">'+'<table class="t tight" style="font-size:11.5px"><tr><th>Doctors</th><th>Life</th><th>Doctors</th><th>Life</th></tr>'+''.join(f'<tr><td>{DOC[k]}</td><td>{LIFE[k]}</td><td>{DOC[k+5]}</td><td>{LIFE[k+5]}</td></tr>' for k in range(5))+'</table>'
    +W_(300,SC(list(zip(DOC,LIFE)),(0,2.5),(60,80),0.5,4,'doctors (number per 1000 people)','life (years)',W=380,H=210,r=4,fs=10))+'</div>',
    'A logarithmic (base 10) transformation was applied to the variable <em class="v">life</em>.<br>With log<sub>10</sub> (<em>life</em>) as the response variable, the equation of the least squares line fitted to the transformed data is closest to'),
  [('Which variable?','log<sub>10</sub>(life) is y, doctors stays as x'),('CAS','new column loglife = log(life); Linear Reg: XList doctors, YList loglife'),('Read off','a = 1.788 · b = 0.0383')],
  'log<sub>10</sub>(<em>life</em>) = 1.79 + 0.0383 × <em>doctors</em>: <b>C</b>.','VCAA 2025 General Mathematics Exam 1 Q11–12 stem and Q11 (examiner report; scatterplot redrawn from the table)',
  mc=['log<sub>10</sub> (<em>life</em>) = 1.57 + 0.0123 × <em>doctors</em>','log<sub>10</sub> (<em>life</em>) = 1.63 + 0.0326 × <em>doctors</em>','log<sub>10</sub> (<em>life</em>) = 1.79 + 0.0383 × <em>doctors</em>','log<sub>10</sub> (<em>life</em>) = 1.85 + 0.0403 × <em>doctors</em>'],
  key='C',stat=('mc',81)))
cls('xs')
# ================= Do Now 3: VCAA 2026 NHT E2 Q1a (1A)
MAM=[('okapi',250),('gorilla',210),('pig',190),('Brazilian tapir',160),('jaguar',100),('grey seal',85),('giant armadillo',60),('sheep',56),('chimpanzee',52),('kangaroo',35),
     ('goat',28),('roedeer',15),('baboon',11),('rhesus monkey',6.8),('raccoon',4.3),('red fox',4.2),('cat',3.3),('echidna',3.0),('rabbit',2.5)]
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 NHT Exam 2 Q1a','Review of 1A',
  '<div style="font-size:17px">The table below displays the typical body weight, in kilograms, for a sample of 19 different mammals.</div>'
  '<div style="margin:6px 0;display:flex;justify-content:center">'+coltab(['Mammal','Body weight (kg)','Mammal','Body weight (kg)'],[(MAM[k][0],MAM[k][1])+((MAM[k+10][0],MAM[k+10][1]) if k+10<19 else ('','')) for k in range(10)],12,'d3t')+'</div>'
  '<div style="font-size:19px">a. Is the variable <em class="v">mammal</em> an ordinal variable or a nominal variable? <span class="muted">(1 mark)</span></div>',
  [('Categories','okapi, gorilla, pig … are names','data-hi="#d3t|c0|hy"'),('Order?','there is no natural order to the names of mammals')],
  '<em>mammal</em> is a <b>nominal</b> variable.','VCAA 2026 (NHT) General Mathematics Exam 2 Q1 stem and Q1a (data source omitted; NHT report gives answers only)',stat=('nht',),cmd=('Is',1,'ordinal or nominal?')))
cls('sm')
# ================= Do Now 4: VCAA 2024 NHT E2 Q1ai (1F)
LLT=[0.43,0.49,0.55,0.61,0.68,0.73,0.72,0.65,0.57,0.48,0.39,0.30,0.25,0.22]; HHT=[1.65,1.55,1.44,1.42,1.42,1.42,1.42,1.47,1.55,1.64,1.74,1.83,1.90,1.92]
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q1ai','Review of 1F',
  '<div style="font-size:16px">Data was collected to investigate the behaviour of tides in Sydney Harbour.<br>There are usually two high tides and two low tides each day.<br>The variables in this study were:<br>'
  '• <em class="v">Day</em>: the day number in the sample<br>• <em class="v">LLT</em>: the height of the lowest low tide for that day (in metres)<br>• <em class="v">HHT</em>: the height of the highest high tide for that day (in metres)<br>'
  'Table 1 displays the data collected for a sample of 14 consecutive days in February 2021.</div><b style="font-size:14px">Table 1</b>'
  +rowtab([('Day',*range(1,15)),('LLT (m)',*LLT),('HHT (m)',*HHT)],12.5,'d4t')+
  '<div style="font-size:17px;margin-top:6px">a. For the <em class="v">HHT</em> values in Table 1:<br>&nbsp;&nbsp;i. Calculate the mean, in metres.<br>&nbsp;&nbsp;&nbsp;&nbsp;Round your answer to one decimal place. <span class="muted">(1 mark)</span></div>',
  [('HHT only','use the HHT row','data-hi="#d4t|r2|hy"'),('CAS','One-Variable Statistics on HHT: x̄ = 1.5979'),('1 d.p.','1.5979 → 1.6')],
  'mean = <b>1.6 m</b>','VCAA 2024 (NHT) General Mathematics Exam 2 Q1 stem and Q1ai (data source omitted; NHT report gives answers only)',stat=('nht',),cmd=('Calculate',1,'mean, 1 decimal place')))
cls('xs')

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9E #11','Modelling with a squared transformation',
  '<div style="font-size:26px">Find a rule connecting the variables <i>x</i> and <i>y</i> if the data in the given table has undergone an <i>x</i>² transformation.</div>'
  '<div style="margin:18px 0">'+rowtab([('<i>x</i>','1','5','10','15'),('<i>x</i>²','1','25','100','225'),('<i>y</i>','23','95','320','695')],26,'a1t')+'</div>',
  [('Slope','(95 − 23) ÷ (25 − 1) = 72 ÷ 24 = 3','data-hi="#a1t|r1|hy"'),('Check','(320 − 95) ÷ (100 − 25) = 225 ÷ 75 = 3'),('Intercept','23 = 3 × 1 + c, so c = 20')],
  '<b><i>y</i> = 3<i>x</i>² + 20</b>',f'{CAM12} · Ch 9 skills checklist 9E #11',cmd=('Find',None,'y = kx² + c')))
HYP=''.join(f'{"M" if i==0 else "L"}{40+i*4},{int(200-170/(1+i*0.18))}' for i in range(60))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 9B #3','Direct or inverse variation?',
  '<div style="font-size:26px">Does the following graph show direct or inverse variation?</div>'
  '<div style="margin:14px 0;display:flex;justify-content:center"><svg viewBox="0 0 300 230" width="360"><line x1="30" y1="10" x2="30" y2="210" stroke="#333" stroke-width="2"/><line x1="30" y1="210" x2="290" y2="210" stroke="#333" stroke-width="2"/>'
  f'<text x="16" y="20" font-size="14" font-style="italic">y</text><text x="282" y="226" font-size="14" font-style="italic">x</text><text x="18" y="226" font-size="13">0</text><path d="{HYP}" fill="none" stroke="#4a3d8f" stroke-width="2.5"/></svg></div>',
  [('Direct?','direct variation is a straight line through the origin (or y = kx²): it goes up'),('This graph','as x increases, y decreases, getting close to the axes'),('Shape','this is the shape of y = k/x')],
  'The graph shows <b>inverse variation</b>.',f'{CAM12} · Ch 9 skills checklist 9B #3 (graph redrawn)',cmd=('Does',None,'direct or inverse?')))
S.append(qslide('apk','APK · Year 11 · adapted from VCAA 2021 Exam 2 Q2a','Rounding the equation of a line',
  '<div style="font-size:24px">The two running events in the heptathlon are the 200 m run and the 800 m run. The times taken by the athletes in these two events, <em class="v">time200</em> and <em class="v">time800</em>, are linearly related.<br>'
  'When a line of good fit is fitted to the data, the equation of this line is found to be<div style="text-align:center;margin:10px 0"><em>time800</em> = 0.03921 + 5.2756 × <em>time200</em></div>'
  'Round the values for the intercept and the slope to three significant figures.<br>Write your answers in the boxes provided. <span class="muted">(1 mark)</span><div style="text-align:center;margin-top:10px"><em>time800</em> = ______ + ______ × <em>time200</em></div></div>',
  [('Intercept','0.03921: first significant figure is the 3 → 0.0392'),('Slope','5.2756 → 5.28')],
  '<em>time800</em> = <b>0.0392</b> + <b>5.28</b> × <em>time200</em>',f'{EDR12} · 9B Q22 (adapted from VCAA 2021 Exam 2 Data analysis Q2a)',cmd=('Round',1,'3 significant figures')))

# ================= Learn
S.append(learn('Learn · 4D','The circle of transformations',
  '<h4>Which transformation might straighten it?</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>match the curve to one of the <b>four quarters</b> of the circle</li>'
  '<li>the labels beside that quarter are the <b>possible</b> transformations</li><li>there is <b>more than one</b> candidate each time</li><li>only for curves that keep going up or keep going down</li></ul>',
  '<div style="display:flex;justify-content:center">'+IMG('circle.png',430)+'</div>',
  'Read the labels on the same side as the curve: top left uses y², log x or 1/x.',f'{CAM}, 4D p. 239 (figure from the textbook)',
  cards=(kcard('Squared','<i>x</i>² or <i>y</i>²'),kcard('Log or reciprocal','log <i>x</i>, 1/<i>x</i>, log <i>y</i>, 1/<i>y</i>'))))
S.append(learn('Learn · 4D','Which candidate is best?',
  '<h4>Try each candidate, then compare</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Apply each possible transformation</li><li>Look at each <b>residual plot</b>: no clear pattern = linear</li>'
  '<li>Compare <b>r²</b>: the higher, the better</li><li>Close r²? Choose the one easier to interpret</li></ol>',
  '<div style="font-size:22px;text-align:center;line-height:2"><div class="frag">residual plot with a curve → <b>not linear yet</b></div><div class="frag">random scatter + highest r² → <b>best transformation</b></div></div>',
  'Write the final equation in the variable names, e.g. age = 5.098 + 0.091 × diameter².',f'{CAM}, 4D pp. 240–242',
  cards=(kcard('Residual plot','no pattern = linear'),kcard('r²','% of variation explained'))))

# ================= WE7 / YT Edrolo 3E WE1d
S.append(qslide('we','Worked example 7 · 4D','Choosing the best transformation',
  G('The scatterplot shows the age (in years) and diameter at a height of 1.5 metre (in cm) for a sample of 19 trees of the same species. Use an appropriate transformation to find a regression model which allows the age of this species of tree to be predicted from its diameter.',
    IMG('ex7.png',300)),
  [('Circle','increasing, curving up: x², 1/y or log y'),
   ('x²','<span style="display:flex;gap:10px;align-items:center">'+IMG('t_x2.png',230)+'<span>residuals: no clear pattern · r² = 92.7%</span></span>'),
   ('1/y','<span style="display:flex;gap:10px;align-items:center">'+IMG('t_1y.png',230)+'<span>residuals still curved · r² = 75.7%</span></span>'),
   ('log y','<span style="display:flex;gap:10px;align-items:center">'+IMG('t_logy.png',230)+'<span>residuals: no clear pattern · r² = 90.2%</span></span>'),
   ('Choose','x² and log y similar: diameter² is easier to interpret')],
  'x² transformation: <b><em>age</em> = 5.098 + 0.091 × <em>diameter</em>²</b>',f'{CAM} · Example 7 (pp. 240–242; figures from the textbook)',video='Cambridge GO · Example 7 (4D Resources)',cmd=('Use',None,'circle → residuals → r²')))
cls('sm')
S.append(qslide('yt','You try · Edrolo 3E WE1d','Choosing the best transformation',
  G('<div style="font-size:19px">Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <em class="v">distance</em>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.</div>'
    +'<div style="margin:6px 0">'+rowtab([('<i>week</i>',*WEEK),('<i>distance</i> (km)',*DIST)],15)+'</div>',
    W_(320,SC(list(zip(WEEK,DIST)),(0,10),(0,8),1,1,'week','distance (km)',W=420,H=170,r=4,fs=10)),
    '<div style="font-size:16px" class="muted">Parts a–c: (distance)² against week · distance against log<sub>10</sub>(week) · distance against 1/week</div>'
    '<div style="font-size:19px">d. Determine which transformation is the best fit for the data set.</div>'),
  [('r² each','use the a–c columns on CAS: r² is on the same screen as a and b'),('Compare','(distance)²: 0.9732 · log<sub>10</sub>(week): 0.9959 · 1/week: 0.9221'),('Largest','0.9959: the log transformation on week')],
  'The <b>log transformation on week</b>: <em>distance</em> = 0.997 + 6.971 × log<sub>10</sub>(<em>week</em>)',f'{EDR} · 3E Worked example 1 stem and part d (pp. 207–211)',cmd=('Determine',None,'largest r²')))
cls('sm')

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['transformation-check']
S.append(cas('CAS · 4D','Compare the candidates: r² and residual plots',
  '<p style="font-size:16px">Akin’s data (the You try):</p>'+rowtab([('week',*WEEK),('distance',*DIST)],13)+
  '<p style="font-size:17px;margin-top:8px">Make a column for each candidate (dist², log(week), 1/week), fit the least squares line to each, and compare r² and the residual plots.</p>',
  C['ti'],C['classpad'],'r² = 0.9732 (dist²) · <b>0.9959 (log week)</b> · 0.9221 (1/week)',
  f'{EDR} · 3E Worked example 1 data · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))
S[-1]=S[-1].replace('<section class="slide T kcas"','<section class="slide T kcas c4"',1)

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2009 Exam 1 Q12','Choosing a transformation',
  G('The <em class="v">mathematics achievement</em> level (TIMSS score) for grade 8 students and the general rate of <em class="v">internet use</em> (%) for 10 countries are displayed in the following scatterplot.',
    '<div style="text-align:center">'+IMG('timss.png',330)+'</div>','To linearise the data, it would be best to plot'),
  [('Shape','increasing, curving over: top-left quarter of the circle'),('Candidates','y², log x or 1/x'),('Options','only log<sub>10</sub>(internet use) is offered')],
  '<em>mathematics achievement</em> against log<sub>10</sub>(<em>internet use</em>): <b>C</b>.','Edrolo U3&amp;4 3D Q14 (VCAA 2009 Further Mathematics Exam 1 Q12; scatterplot from Edrolo; no examiner report % before 2016)',
  mc=['<em>mathematics achievement</em> against <em>internet use</em>.','log<sub>10</sub>(<em>mathematics achievement</em>) against <em>internet use</em>.','<em>mathematics achievement</em> against log<sub>10</sub>(<em>internet use</em>).','<em>mathematics achievement</em> against (<em>internet use</em>)².',FR('1','<em>mathematics achievement</em>')+' against <em>internet use</em>.'],
  key='C',dis=('D','x² is for curves bending upwards (bottom-right quarter); this curve bends over.')))
cls('sm')
MA=[26.3,35.2,45.2,55.3,65.1,74.8,83.1]; MH=[167.1,164.9,164.8,163.4,161.2,158.4,156.7]
RES=[-0.334,-0.959,0.709,1.096,0.629,-0.455,-0.687]
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2020 Exam 2 Q6d','Applying the best transformation',
  G('<div style="font-size:16px">The table below shows the mean age, in years, and the mean height, in centimetres, of 648 women from seven different age groups.</div>'
    +rowtab([('Mean age (years)',*MA),('Mean height (cm)',*MH)],13,'e2t')
    +'<div style="font-size:16px;margin-top:4px">d. In a further analysis of the data, a least squares line was fitted.<br>The associated residual plot that was generated is shown below.</div>',
    W_(320,SC(list(zip(MA,RES)),(20,90),(-1,1),10,0.5,'mean age (years)','residual',W=420,H=150,r=4,fs=10)),
    '<div style="font-size:16px">The residual plot indicates that the association between the mean height and the mean age of women is non-linear.<br>'
    'The data presented in the table … can be linearised by applying an appropriate transformation to the variable <em class="v">mean age</em>.<br>'
    'Apply an appropriate transformation to the variable <em class="v">mean age</em> to linearise the data. Fit a least squares line to the transformed data and write its equation below.<br>'
    'Round the values of the intercept and the slope to four significant figures. <span class="muted">(2 marks)</span></div>'),
  [('Shape','decreasing and curving down (residuals: − + −): top-right quarter → x² (on mean age)'),('CAS','new column age2 = age²; Linear Reg: XList age2, YList height'),('Read off','a = 167.861… · b = −0.001 621…'),('4 s.f.','167.9 and −0.001621')],
  '<em>mean height</em> = <b>167.9 − 0.001621</b> × (<em>mean age</em>)²','VCAA 2020 Further Mathematics Exam 2 Q6 table and Q6d (examiner report: average 0.6/2; residual plot redrawn from the data) · Edrolo U3&amp;4 3E Q13',stat=('avg',30),cmd=('Apply',2,'x², then 4 s.f.')))
cls('xs')

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 4 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('4D',) and v.get('url')]))
n=assemble(S,'12MAG · L15 · Choosing and applying the appropriate transformation',os.path.join(ROOT,'lessons','4D slides.html'))
print(n-1,'slides')
