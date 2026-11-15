"""Lesson gm12-u3-l32 (7B linear growth and decay, 7D geometric growth and decay) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/7B-7D slides.html     Run: python3 tools/deck/gm12-u3-l32/build.py     Screenshots: python3 tools/deck/gm12-u3-l32/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- Do Now: VCAA 2025 NHT Exam 1 Q17 (7A; scanned paper read from the page image; answer C; NHT report gives no %) ·
          VCAA 2025 Exam 1 Q9 (stem of Q9-10 + scatterplot, img/dn2.png; report 66% A, 66/6/23/4) ·
          VCAA 2025 Exam 2 Q2b (boxplot, img/dn3.png; report 0.8/1 avg = 80%) ·
          VCAA 2023 Exam 2 Q3e (stem of Q3 + scatterplot, img/dn4.png; report 0.8/1 avg = 80%).
- APK: Cambridge U1&2 Ch 1 skills checklist 1A #5 and #4 (solutions worked for 12MAG) ·
       VCAA 2016 Further Exam 2 Q5a (= Edrolo U1&2 3D Q14; report 92% full marks).
- Learn: Cambridge U3&4 7B pp. 340-346, 7D pp. 359-362 (own words) · Edrolo U3&4 5B, 5C, 5E.
- Worked examples: Cambridge U3&4 Examples 7-12 (7B, pp. 341-346) and 19-22 (7D, pp. 359-362).
  You trys (planner card): Ex 7 = Edrolo U3&4 5B WE3b (p. 309) · Ex 8 = 5E WE1a (p. 334) · Ex 9 = 5E WE1b-c (p. 334) ·
  Ex 10 = 5B WE1 (p. 307) · Ex 11 = 5B WE3a (p. 309) · Ex 12 = 5B WE2 (p. 308) · Ex 19 = Edrolo U1&2 3D WE2 (p. 150) ·
  Ex 20 = Edrolo U1&2 3E WE1 (p. 158) · Ex 21 = Edrolo U3&4 5C WE1 (p. 317) · Ex 22 = 5C WE2a (p. 318).
  Graphs in Edrolo 5B WE1b, 5B WE2b and 5C WE1b are redrawn with the same points as the source.
- CAS: planner/cas-skills.json 'recursion-sequence' (task = Cambridge Example 22b).
- Exits: VCAA 2019 Further Exam 1 Q19 (Edrolo U3&4 5B Q14; report 76% A, 76/2/13/3/5) ·
         VCAA 2020 Further Exam 2 Q7b (5B Q15; report 72% full marks) · VCAA 2019 Further Exam 2 Q7a (5C Q13; report 74% full marks).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l32')
def IMG(f,w): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"img",f),"rb").read()).decode()}" style="width:{w}px;max-width:100%;display:block;margin:6px auto">'
yid=lambda u:u.split('v=')[1].split('&')[0]
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
def plot(vals,ymax,ystep,L='V',W=380,Hh=230,lab=None,col='#1565C0'):
    """points (n, V_n) on a grid: a graph of the terms of a sequence (dots, not joined)"""
    l,b,t,r=58,30,12,14; pw=W-l-r; ph=Hh-b-t; nx=len(vals)
    X=lambda n:l+pw*(n+0.5)/nx; Y=lambda v:t+ph*(1-v/ymax)
    o=[f'<line x1="{l}" y1="{Y(0)}" x2="{W-r}" y2="{Y(0)}" stroke="#333" stroke-width="1.5"/>',f'<line x1="{l}" y1="{t}" x2="{l}" y2="{Y(0)}" stroke="#333" stroke-width="1.5"/>']
    y=0
    while y<=ymax+1e-9:
        o.append(f'<line x1="{l}" y1="{Y(y)}" x2="{W-r}" y2="{Y(y)}" stroke="#ddd"/><text x="{l-6}" y="{Y(y)+5}" text-anchor="end" font-size="13">{y:,.10g}</text>'.replace(',',' '))
        y+=ystep
    for n,v in enumerate(vals):
        o.append(f'<text x="{X(n)}" y="{Y(0)+18}" text-anchor="middle" font-size="13">{n}</text><circle cx="{X(n)}" cy="{Y(v)}" r="5.5" fill="{col}"/>')
    o.append(f'<text x="{W-r}" y="{Y(0)+18}" font-size="14" font-style="italic" text-anchor="end">n</text><text x="{l+6}" y="{t+8}" font-size="14" font-style="italic">{L}ₙ</text>')
    return f'<svg viewBox="0 0 {W} {Hh}" width="{W}" style="max-width:100%;display:block;margin:4px auto;background:#fff;border-radius:8px">{"".join(o)}</svg>'

S=[]
S.append(title(32,'Linear and geometric growth and decay',f'{CAM} · 7B Modelling linear growth and decay · 7D Modelling geometric growth and decay','L32').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· three Year 11 questions','var(--apk)'),
  ('7B Linear growth and decay','',None),('Worked examples 7–12','→ You try',None),('7D Geometric growth and decay','',None),
  ('Worked examples 19–22','→ You try',None),('CAS: generating a sequence','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]).replace('<ul class="">','<ul class="" style="font-size:14.5px;line-height:1.25">').replace('<ul class="tick">','<ul class="tick" style="font-size:14.5px;line-height:1.25">'))
S[-1]=S[-1].replace('<section class="slide T ','<section id="tdy" class="slide T ',1).replace('</section>','<style>#tdy .card3 li{font-size:16px!important;line-height:1.25!important;padding-top:4px!important;padding-bottom:4px!important}</style></section>')
# (10 learning intentions + 10 success criteria: smaller text so the cards fit)
S.append(keys([
  ('Linear growth / decay','add / subtract the same amount <i>D</i> each step: the points lie on a straight line'),
  ('Simple interest','the same amount of interest (a % of the principal) is added each year'),
  ('Flat rate depreciation','the same amount (a % of the purchase price) is subtracted each year'),
  ('Unit cost depreciation','the value drops by the cost per unit of use (per km, per use …)'),
  ('Geometric growth / decay','multiply by the same <i>R</i> each step: the points lie on a curve'),
  ('Compound interest · reducing balance','interest added to / depreciation taken from the CURRENT value each year')],
  [('Linear',F(RR('principal','<i>V<sub>n</sub></i> ± <i>D</i>')),'<i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub> (simple interest, flat rate) · <i>D</i> = cost per unit (unit cost)'),
   ('Geometric',F(RR('principal','<i>R</i> × <i>V<sub>n</sub></i>')),'<i>R</i> = 1 + <i>r</i>/100 (compound interest) · <i>R</i> = 1 − <i>r</i>/100 (reducing balance)'),
   ('Rate from the model',F('<i>r</i> = <i>D</i> ÷ <i>V</i><sub>0</sub> × 100%'),'geometric: <i>r</i> = (<i>R</i> − 1) × 100%')],
  f'{CAM}, 7B pp. 340–346 and 7D pp. 359–362; Study Design: depreciation, simple and compound interest with recurrence relations'))

# ================= Do Now (retrieval)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 NHT Exam 1 Q17','Review of 7A (last lesson)',
  '<div style="font-size:26px;margin-top:30px">A sequence of numbers is generated by the recurrence relation<br><br>'+RR('30','0.5<i>T<sub>n</sub></i> − 5','T')+'<br><br>The first negative term in the sequence is</div>',
  [('T1','0.5 × 30 − 5 = 10'),('T2','0.5 × 10 − 5 = 0 (zero is not negative)'),('T3','0.5 × 0 − 5 = −5')],
  '<i>T</i><sub>3</sub> = −5 is the first negative term: <b>C</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q17 (NHT examiner report gives no % statistics)',
  mc=['<i>T</i><sub>1</sub>','<i>T</i><sub>2</sub>','<i>T</i><sub>3</sub>','<i>T</i><sub>4</sub>'],key='C',dis=('B','<i>T</i><sub>2</sub> = 0 is not negative')))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 Exam 1 Q9','Review of 3A (last term)',
  ('<div style="font-size:18px">In the scatterplot below, the <i>games won</i> are plotted against the <i>goals against</i> for each of the 12 Australian A-League men’s teams after 27 games of the 2022–2023 season. A least squares line has been fitted to the data.</div>',
   IMG('dn2.png',560),'<div style="font-size:18px">The equation for the least squares line is closest to</div>'),
  [('Two points','on the line: (27, 12) and (44, 9)'),fx('Slope','slope',F(FR(['9 − 12'],['44 − 27'])),'−0.176…'),('Intercept','12 = <i>a</i> − 0.176 × 27 → <i>a</i> ≈ 16.8')],
  '<i>games won</i> = 16.8 − 0.178 × <i>goals against</i>: <b>A</b>.','VCAA 2025 General Mathematics Exam 1 Q9–10 stem and Q9 (examiner report)',
  mc=['<i>games won</i> = 16.8 – 0.178 × <i>goals against</i>','<i>games won</i> = 14.3 – 0.193 × <i>goals against</i>','<i>games won</i> = 12.5 – 0.165 × <i>goals against</i>','<i>games won</i> = 17.4 + 0.173 × <i>goals against</i>'],
  key='A',dist=[66,6,23,4],dis=('C','12.5 is where the line crosses the vertical axis at 24, not at <i>goals against</i> = 0')))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q2b','Review of 1G (last term)',
  ('<div style="font-size:20px">A boxplot for the sale prices of a sample of 203 homes is shown.</div>',IMG('dn3.png',520),
   '<div style="font-size:20px">b. <b>Calculate</b> the upper fence for the sale price data in the boxplot. <span class="muted">(1 mark)</span></div>'),
  [('Read off','Q<sub>1</sub> = 600 000 · Q<sub>3</sub> = 900 000'),fx('IQR','IQR',F(V('Q3','900 000'),' − ',V('Q1','600 000')),'300 000'),
   fx('UF','UF',F(V('Q3','900 000'),' + 1.5 × ',V('IQR','300 000')),'1 350 000')],
  'The upper fence is <b>$1 350 000</b>.','VCAA 2025 General Mathematics Exam 2 Q2 stem and Q2b (examiner report: average 0.8/1)',
  stat=('mark',80),cmd=('Calculate',1,'IQR, then Q3 + 1.5 × IQR')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2023 Exam 2 Q3e','Review of 3B (last term)',
  ('<div style="font-size:17px">The scatterplot below plots the average monthly ice cream <i>consumption</i>, in litres/person, against average monthly <i>temperature</i>, in °C. The data for the graph was recorded in the Northern Hemisphere.</div>',
   IMG('dn4.png',330),'<div style="font-size:17px">When a least squares line is fitted to the scatterplot, the equation is found to be:<br>&nbsp;&nbsp;<i>consumption</i> = 0.1404 + 0.0024 × <i>temperature</i><br>The coefficient of determination is 0.7212<br>e. <b>Use</b> the equation of the least squares line to predict the average monthly ice cream <i>consumption</i>, in litres per person, when the monthly average <i>temperature</i> is −6 °C. <span class="muted">(1 mark)</span></div>'),
  [fx('Predict','<i>consumption</i>',F('0.1404 + 0.0024 × ',V('temperature','(−6)')),'0.126')],
  'Predicted consumption = <b>0.126</b> litres per person (don’t round to 0.13).','VCAA 2023 General Mathematics Exam 2 Q3 stem and Q3e (examiner report: average 0.8/1)',
  stat=('mark',80),cmd=('Use',1,'substitute −6 into the equation')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1A #5','Finding a percentage of a quantity',
  '<div style="font-size:34px;margin-top:60px">What is 30% of $50?</div>',
  [('Convert','30% = 30 ÷ 100 = 0.3'),fx('Multiply','30% of $50',F('0.3 × ',V('amount','50')),'15')],
  '30% of $50 is <b>$15</b>.',f'{CAM12} · Ch 1 skills checklist 1A #5 · solution worked for 12MAG',cmd=('What is',None,'÷ 100, then × the amount')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1A #4','Converting a percentage to a decimal',
  '<div style="font-size:34px;margin-top:60px">What is 85% as a decimal?</div>',
  [('Divide','85 ÷ 100 = 0.85')],
  '85% = <b>0.85</b>',f'{CAM12} · Ch 1 skills checklist 1A #4 · solution worked for 12MAG',cmd=('What is',None,'÷ 100')))
S.append(qslide('apk','APK · VCAA 2016 Exam 2 Q5a','Reading a recurrence relation',
  '<div style="font-size:28px;margin-top:30px">Ken has opened a savings account to save money to buy a new caravan.<br>The amount of money in the savings account after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation shown below.<br><br>'
  +RR('15 000','1.04 × <i>V<sub>n</sub></i>')+'<br><br>a. How much money did Ken initially deposit into the savings account? <span class="muted">(1 mark)</span></div>',
  [('Read','initially = after 0 years = <i>V</i><sub>0</sub>')],
  'Ken initially deposited <b>$15 000</b>.',f'VCAA 2016 Further Mathematics Exam 2 Q5 stem and Q5a (examiner report: 92% full marks) · {EDR12} 3D Q14',
  stat=('mark',92),cmd=('How much',1,'the starting value')))

# ================= 7B Learn 1: linear growth and decay
S.append(learn('Learn · 7B','Linear growth and decay',
  '<h4>Add or subtract the same amount each step</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + <i>D</i>: linear <b>growth</b></li><li><i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − <i>D</i>: linear <b>decay</b></li>'
  '<li><i>D</i> = the common difference; graph the terms as dots on a straight line (don’t join them)</li></ul>',
  '<div class="row" style="gap:20px;justify-content:center"><div class="frag" style="text-align:center;font-size:20px">'+RR('20','<i>P<sub>n</sub></i> + 2','P')+'<br>20, 22, 24, …'+plot([20,22,24,26,28,30],35,5,'P',W=330,Hh=200)+'</div>'
  '<div class="frag" style="text-align:center;font-size:20px">'+RR('20','<i>Q<sub>n</sub></i> − 2','Q')+'<br>20, 18, 16, …'+plot([20,18,16,14,12,10],35,5,'Q',W=330,Hh=200,col='#C62828')+'</div></div>',
  'Upward line of dots = growth; downward = decay.',f'{CAM}, 7B pp. 340–341 (own words) · {EDR}, 5B',
  cards=(kcard('Linear',RR('a','<i>V<sub>n</sub></i> ± <i>D</i>')),)))
# Ex 7 / Edrolo 5B WE3b
S.append(qslide('we','Worked example 7 · 7B','Graphing the terms of a linear growth/decay sequence',
  '<div style="font-size:26px;margin-top:20px">For each of the following recurrence relations, list the first four terms and graph the corresponding points.</div>'
  +plist([('a',RR('2','<i>V<sub>n</sub></i> + 5')),('b',RR('20','<i>W<sub>n</sub></i> − 3','W'))]),
  [('a','start 2, rule ‘add 5’: 2, 7, 12, 17'),('b','start 20, rule ‘subtract 3’: 20, 17, 14, 11')],
  '',f'{CAM} · Example 7 (pp. 341–342)',video='Cambridge GO · Example 7 (7B Resources)',cmd=('list',None,'four terms, then plot (n, term)'),
  parts=[('a','2, 7, 12, 17'+plot([2,7,12,17],20,5,W=300,Hh=150)),('b','20, 17, 14, 11'+plot([20,17,14,11],25,5,'W',W=300,Hh=150,col='#C62828'))]))
S.append(qslide('yt','You try · Edrolo 5B WE3b','Graphing the terms of a linear decay sequence',
  '<div style="font-size:26px;margin-top:30px">The value of a brand new laptop, <i>V<sub>n</sub></i> after <i>n</i> years, is depreciated using flat rate depreciation.<br>This is represented by the following recurrence relation.<br><br>'+RR('2100','<i>V<sub>n</sub></i> − 350')+'<br><br>b. Graph the value of the laptop over the first five years.</div>',
  [('Values','<i>V</i><sub>0</sub> = 2100, <i>V</i><sub>1</sub> = 1750, <i>V</i><sub>2</sub> = 1400, <i>V</i><sub>3</sub> = 1050, <i>V</i><sub>4</sub> = 700, <i>V</i><sub>5</sub> = 350'),('Plot','<i>V</i><sub>0</sub> on the vertical axis, then one dot per year')],
  'Six points, falling by 350 each year:'+plot([2100,1750,1400,1050,700,350],2100,350,W=360,Hh=200),f'{EDR} · 5B Worked example 3b (p. 309)',cmd=('Graph',None,'V₀ to V₅, then plot')))

# Learn 2: simple interest
S.append(learn('Learn · 7B','Simple interest',
  '<h4>Simple interest = linear growth</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>the <b>principal</b> (amount borrowed or invested) is <i>V</i><sub>0</sub></li><li>the same interest <i>D</i> = <i>r</i>% of the principal is added every year</li></ul>',
  '<div style="font-size:24px;text-align:center;line-height:1.8"><span class="frag">$5000 at 4.8% p.a. simple interest</span><br><span class="frag"><i>D</i> = 4.8 ÷ 100 × 5000 = 240</span><br><span class="frag">'+RR('5000','<i>V<sub>n</sub></i> + 240')+'</span><br><span class="frag">5000 → 5240 → 5480 → 5720 → …</span></div>',
  'Interest earned = current value − principal.',f'{CAM}, 7B p. 342 (own words) · {EDR}, 5E',
  cards=(kcard('Simple interest',RR('principal','<i>V<sub>n</sub></i> + <i>D</i>'),'<i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub>'),)))
S.append(qslide('we','Worked example 8 · 7B','Modelling simple interest investments with a recurrence relation',
  '<div style="font-size:24px;margin-top:20px">Cheryl invests $5000 in an investment account that pays 4.8% per annum simple interest.<br><b>Model</b> this simple investment using a recurrence relation of the form:<br><br><i>V</i><sub>0</sub> = the principal, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + <i>D</i>, &nbsp; where <i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub>.<br><br>Let <i>V<sub>n</sub></i> be the value of the investment after <i>n</i> years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 5000'),fx('D','<i>D</i>',F(FR([V('r','4.8')],['100']),' × ',V('V0','5000')),'240')],
  RR('5000','<i>V<sub>n</sub></i> + 240'),f'{CAM} · Example 8 (p. 342)',video='Cambridge GO · Example 8 (7B Resources)',cmd=('Model',None,'V₀, then D')))
S.append(qslide('yt','You try · Edrolo 5E WE1a','Modelling a simple interest loan',
  '<div style="font-size:28px;margin-top:40px">Sally borrows $300 000 where simple interest is charged at a rate of 0.5% per year.<br><br>a. <b>Construct</b> a recurrence relation to model the value of this loan, <i>V<sub>n</sub></i> after <i>n</i> years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 300 000 · <i>r</i> = 0.5'),fx('D','<i>d</i>',F(FR([V('r','0.5')],['100']),' × ',V('V0','300 000')),'1500')],
  RR('300 000','<i>V<sub>n</sub></i> + 1500'),f'{EDR} · 5E Worked example 1a (p. 334)',cmd=('Construct',None,'V₀, then the interest each year')))
S.append(qslide('we','Worked example 9 · 7B','Using a recurrence relation to analyse a simple interest investment',
  '<div style="font-size:24px;margin-top:10px">Cheryl’s simple interest investment is modelled by<br>'+RR('5000','<i>V<sub>n</sub></i> + 240')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.</div>'
  +plist([('a','Use the recurrence relation to show that the value of Cheryl’s investment after 3 years is $5720.'),('b','When will Cheryl’s investment first exceed $6000, and what will its value be then?')]),
  [('a','<i>V</i><sub>1</sub> = 5000 + 240 = 5240 · <i>V</i><sub>2</sub> = 5240 + 240 = 5480 · <i>V</i><sub>3</sub> = 5480 + 240 = 5720'),('b','CAS: 5000, enter, + 240, enter … 5240, 5480, 5720, 5960, <b>6200</b> (5 presses)')],
  '',f'{CAM} · Example 9 (p. 343)',video='Cambridge GO · Example 9 (7B Resources)',cmd=('show that',None,'write each step'),
  parts=[('a','<i>V</i><sub>3</sub> = 5480 + 240 = <b>$5720</b>'),('b','After <b>5 years</b>; value <b>$6200</b>')]))
S.append(qslide('yt','You try · Edrolo 5E WE1b–c','Analysing a simple interest loan',
  '<div style="font-size:26px;margin-top:20px">Sally borrows $300 000 where simple interest is charged at a rate of 0.5% per year.<br>('+RR('300 000','<i>V<sub>n</sub></i> + 1500')+')</div>'
  +plist([('b','What is the value of the loan after three years?'),('c','How much interest has been charged after three years?')]),
  [('b','<i>V</i><sub>1</sub> = 301 500 · <i>V</i><sub>2</sub> = 303 000 · <i>V</i><sub>3</sub> = 304 500'),('c','interest = <i>V</i><sub>3</sub> − <i>V</i><sub>0</sub> = 304 500 − 300 000')],
  '',f'{EDR} · 5E Worked example 1b–c (p. 334); recurrence relation from part a',cmd=('How much',None,'value − principal'),
  parts=[('b','<b>$304 500.00</b>'),('c','<b>$4500.00</b>')]))

# Learn 3: flat rate depreciation
S.append(learn('Learn · 7B','Flat rate depreciation',
  '<h4>Flat rate depreciation = linear decay</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>an asset loses the same amount <i>D</i> every year</li><li><i>D</i> = <i>r</i>% of the <b>purchase price</b> <i>V</i><sub>0</sub></li><li><b>scrap value</b>: the value when the asset is no longer useful</li></ul>',
  '<div style="font-size:24px;text-align:center;line-height:1.8"><span class="frag">Car $24 000, 20% of the purchase price per year</span><br><span class="frag"><i>D</i> = 20 ÷ 100 × 24 000 = 4800</span><br><span class="frag">'+RR('24 000','<i>V<sub>n</sub></i> − 4800')+'</span><br><span class="frag">24 000 → 19 200 → 14 400 → 9600 → 4800 → 0</span></div>',
  'Rate from the model: <i>r</i> = <i>D</i> ÷ <i>V</i><sub>0</sub> × 100%.',f'{CAM}, 7B pp. 343–344 (own words) · {EDR}, 5B',
  cards=(kcard('Flat rate',RR('purchase price','<i>V<sub>n</sub></i> − <i>D</i>'),'<i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub>'),)))
S.append(qslide('we','Worked example 10 · 7B','Modelling flat rate depreciation with a recurrence relation',
  '<div style="font-size:24px;margin-top:20px">A new car was purchased for $24 000 in 2014. The car depreciates by 20% of its purchase price each year. <b>Model</b> the depreciating value of this car using a recurrence relation of the form:<br><br><i>V</i><sub>0</sub> = initial value, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − <i>D</i>, &nbsp; where <i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub><br><br>Let <i>V<sub>n</sub></i> be the value of the car after <i>n</i> years depreciation.</div>',
  [('V0','<i>V</i><sub>0</sub> = 24 000 (value when new)'),fx('D','<i>D</i>',F(FR([V('r','20')],['100']),' × ',V('V0','24 000')),'4800')],
  RR('24 000','<i>V<sub>n</sub></i> − 4800'),f'{CAM} · Example 10 (p. 344)',video='Cambridge GO · Example 10 (7B Resources)',cmd=('Model',None,'V₀, then D')))
S.append(qslide('yt','You try · Edrolo 5B WE1','Modelling flat rate depreciation',
  '<div style="font-size:19px">Determine the recurrence relation that models the value of the assets, <i>V<sub>n</sub></i>, after <i>n</i> years, in each of the scenarios.</div>'
  +plist([('a','Karl does not believe in banks. Instead of investing his money, he buries his $20 000 in his backyard. Unfortunately for Karl, inflation causes his buried cash to depreciate at a constant amount per year, equal to 3% of the amount of money that he buried.'),
          ('b','The graph shows the value of a car, purchased for $24 000, over a period of four years.'+plot([24000,22000,20000,18000,16000],24000,4000,W=320,Hh=150))]),
  [('a','<i>V</i><sub>0</sub> = 20 000 · <i>d</i> = 3/100 × 20 000 = 600'),('b','<i>V</i><sub>0</sub> = 24 000 (vertical intercept) · <i>V</i><sub>1</sub> = 22 000, so <i>d</i> = 2000')],
  '',f'{EDR} · 5B Worked example 1 (p. 307); graph redrawn with the same points',cmd=('Determine',None,'V₀, then the amount lost each year'),
  parts=[('a',RR('20 000','<i>V<sub>n</sub></i> − 600')),('b',RR('24 000','<i>V<sub>n</sub></i> − 2000'))]))
S.append(qslide('we','Worked example 11 · 7B','Using a recurrence relation to analyse flat rate depreciation',
  '<div style="font-size:24px;margin-top:10px">The flat rate depreciation of a car is modelled by<br>'+RR('24 000','<i>V<sub>n</sub></i> − 4800')+'<br>where <i>V<sub>n</sub></i> is the value of the car after <i>n</i> years.</div>'
  +plist([('a','Use the model to determine the value of the car after 2 years.'),('b','If the car was purchased in 2023, in what year will the car’s value depreciate to zero?'),('c','What was the percentage depreciation rate?')]),
  [('CAS','24 000, enter, − 4800, enter … 19 200, 14 400, 9600, 4800, 0'),('b','value 0 after 5 presses: 2023 + 5'),fx('c','<i>r</i>',F(FR([V('D','4800')],[V('V0','24 000')]),' × 100%'),'20%')],
  '',f'{CAM} · Example 11 (pp. 344–345)',video='Cambridge GO · Example 11 (7B Resources)',cmd=('determine',None,'press enter, count the presses'),
  parts=[('a','<b>$14 400</b>'),('b','In <b>2028</b>'),('c','<b>20%</b>')]))
S.append(qslide('yt','You try · Edrolo 5B WE3a','Analysing flat rate depreciation',
  '<div style="font-size:28px;margin-top:40px">The value of a brand new laptop, <i>V<sub>n</sub></i> after <i>n</i> years, is depreciated using flat rate depreciation.<br>This is represented by the following recurrence relation.<br><br>'+RR('2100','<i>V<sub>n</sub></i> − 350')+'<br><br>a. What is the value of the laptop two years after it is purchased?</div>',
  [fx('V1','<i>V</i><sub>1</sub>',F(V('V0','2100'),' − 350'),'1750'),fx('V2','<i>V</i><sub>2</sub>',F(V('V1','1750'),' − 350'),'1400')],
  'The laptop is worth <b>$1400</b> after two years.',f'{EDR} · 5B Worked example 3a (p. 309)',cmd=('What is',None,'V₁, then V₂')))

# Learn 4: unit cost depreciation
S.append(learn('Learn · 7B','Unit cost depreciation',
  '<h4>Value depends on USE, not time</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>D</i> = cost per unit of use (per km, per page, per mow …)</li><li><i>V<sub>n</sub></i> = value after <i>n</i> units of use</li></ul>',
  '<div style="font-size:24px;text-align:center;line-height:1.8"><span class="frag">Mower $270, loses $3.50 each time it is used</span><br><span class="frag">'+RR('270','<i>V<sub>n</sub></i> − 3.50')+'</span><br><span class="frag">270 → 266.50 → 263 → 259.50 → …</span></div>',
  '<i>n</i> counts uses, not years: read the question for the unit.',f'{CAM}, 7B p. 345 (own words) · {EDR}, 5B',
  cards=(kcard('Unit cost',RR('purchase price','<i>V<sub>n</sub></i> − <i>D</i>'),'<i>D</i> = depreciation per unit of use'),)))
S.append(qslide('we','Worked example 12 · 7B','Modelling unit cost depreciation with a recurrence relation',
  '<div style="font-size:20px">A professional gardener purchased a lawn mower for $270. The mower depreciates in value by $3.50 each time it is used.</div>'
  +plist([('a','Model the depreciating value of this mower using a recurrence relation of the form: <i>V</i><sub>0</sub> = initial value, <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> − <i>D</i>, where <i>D</i> is the depreciation in value per use and <i>V<sub>n</sub></i> is the value of the mower after being used to mow <i>n</i> lawns.'),
          ('b','Use the model to determine the value of the mower after it has been used three times.'),('c','How many times can the mower be used until its depreciated value is first less than $250?')]),
  [('a','<i>V</i><sub>0</sub> = 270 · <i>D</i> = 3.50'),('CAS','270, enter, − 3.5, enter … 266.5, 263, 259.5, 256, 252.5, <b>249</b>')],
  '',f'{CAM} · Example 12 (pp. 345–346)',video='Cambridge GO · Example 12 (7B Resources)',cmd=('determine',None,'one press per use'),
  parts=[('a',RR('270','<i>V<sub>n</sub></i> − 3.50')),('b','<b>$259.50</b>'),('c','After <b>six</b> mows')]))
S.append(qslide('yt','You try · Edrolo 5B WE2','Modelling unit cost depreciation',
  '<div style="font-size:19px">Determine the recurrence relation that models the value of the assets, <i>V<sub>n</sub></i> after <i>n</i> units of use, in each of the following scenarios.</div>'
  +plist([('a','David spends $33 on a disposable underwater camera and estimates that it will depreciate by $1.50 for each photo that he takes.'),
          ('b','Chloe purchases a book for $30. The book depreciates each time it is read. The value of the book is shown in the graph.'+plot([30,27,24,21,18],30,6,W=320,Hh=150))]),
  [('a','<i>V</i><sub>0</sub> = 33 · <i>d</i> = 1.5 per photo'),('b','<i>V</i><sub>0</sub> = 30 · <i>V</i><sub>1</sub> = 27, so <i>d</i> = 3 per reading')],
  '',f'{EDR} · 5B Worked example 2 (p. 308); graph redrawn with the same points',cmd=('Determine',None,'V₀, then the loss per use'),
  parts=[('a',RR('33','<i>V<sub>n</sub></i> − 1.5')),('b',RR('30','<i>V<sub>n</sub></i> − 3'))]))

# ================= 7D Learn 5: geometric growth and decay
S.append(learn('Learn · 7D','Geometric growth and decay',
  '<h4>Multiply by the same <i>R</i> each step</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>V</i><sub><i>n</i>+1</sub> = <i>R</i> × <i>V<sub>n</sub></i></li><li><i>R</i> &gt; 1: geometric <b>growth</b> · <i>R</i> &lt; 1: geometric <b>decay</b></li><li>the points lie on a curve</li></ul>',
  '<div class="row" style="gap:20px;justify-content:center"><div class="frag" style="text-align:center;font-size:20px">'+RR('3','2<i>V<sub>n</sub></i>')+'<br>3, 6, 12, 24, …'+plot([3,6,12,24,48],50,10,W=330,Hh=200)+'</div>'
  '<div class="frag" style="text-align:center;font-size:20px">'+RR('48','0.5<i>V<sub>n</sub></i>')+'<br>48, 24, 12, 6, …'+plot([48,24,12,6,3],50,10,W=330,Hh=200,col='#C62828')+'</div></div>',
  'Linear: same amount each step (+/−). Geometric: same percentage each step (×).',f'{CAM}, 7D pp. 359–360 (own words) · {EDR}, 5C',
  cards=(kcard('Geometric',RR('a','<i>R</i> × <i>V<sub>n</sub></i>')),)))
S.append(qslide('we','Worked example 19 · 7D','Graphing the terms in a geometric sequence',
  '<div style="font-size:26px;margin-top:20px">For each recurrence relation, state the rule, find the first 6 terms and then plot each point on a graph.</div>'
  +plist([('a',RR('1','3<i>V<sub>n</sub></i>')),('b',RR('8','0.5<i>V<sub>n</sub></i>'))]),
  [('a','start 1, next = 3 × current: 1, 3, 9, 27, 81, 243'),('b','start 8, next = 0.5 × current: 8, 4, 2, 1, 0.5, 0.25')],
  '',f'{CAM} · Example 19 (p. 359)',video='Cambridge GO · Example 19 (7D Resources)',cmd=('state',None,'rule in words, six terms, plot'),
  parts=[('a','1, 3, 9, 27, 81, 243'+plot([1,3,9,27,81,243],250,50,W=300,Hh=150)),('b','8, 4, 2, 1, 0.5, 0.25'+plot([8,4,2,1,0.5,0.25],10,2,W=300,Hh=150,col='#C62828'))]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3D WE2','Generating the terms of a geometric sequence',
  '<div style="font-size:30px;margin-top:50px">Consider the following recurrence relation.<br><br>'+RR('45','0.6<i>u<sub>n</sub></i>','u')+'<br><br><b>Calculate</b> the value of the first five terms in the sequence.</div>',
  [('Start','CAS: type 45, enter'),('Rule','× 0.6, enter → 27'),('Repeat','enter → 16.2 · 9.72 · 5.832')],
  '<b>45, 27, 16.2, 9.72, 5.832</b>',f'{EDR12} · 3D Worked example 2 (p. 150)',cmd=('Calculate',None,'u₀ to u₄')))

# Learn 6: compound interest
S.append(learn('Learn · 7D','Compound interest',
  '<h4>Interest is added to the CURRENT value</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>interest earned is added on, then earns interest itself</li><li>next value = current + <i>r</i>% of current = <i>R</i> × current</li></ul>',
  '<div style="font-size:24px;text-align:center;line-height:1.8"><span class="frag">$5000 at 8% p.a., compounding yearly</span><br><span class="frag">next = current + 8% of current = 108% of current</span><br><span class="frag"><i>R</i> = 1 + 8/100 = 1.08</span><br><span class="frag">'+RR('5000','1.08 × <i>V<sub>n</sub></i>')+'</span></div>',
  'Growth: <i>R</i> = 1 + <i>r</i>/100 (8% → 1.08, not 0.08).',f'{CAM}, 7D p. 360 (own words) · {EDR}, 5F',
  cards=(kcard('Compound interest',RR('principal','<i>R</i> × <i>V<sub>n</sub></i>'),'<i>R</i> = 1 + <i>r</i>/100'),)))
S.append(qslide('we','Worked example 20 · 7D','Modelling compound interest with a recurrence relation',
  '<div style="font-size:23px">The following recurrence relation can be used to model a compound interest investment of $2000 paying interest at the rate of 7.5% per annum.<br>'+RR('2000','1.075 × <i>V<sub>n</sub></i>')+'<br>In the recurrence relation, <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.</div>'
  +plist([('a','Use the recurrence relation to show that the value of the investment after 3 years is $2484.59.'),('b','Determine when the value of the investment will first exceed $2500.')]),
  [('a','<i>V</i><sub>1</sub> = 1.075 × 2000 = 2150 · <i>V</i><sub>2</sub> = 1.075 × 2150 = 2311.25 · <i>V</i><sub>3</sub> = 1.075 × 2311.25 = 2484.59'),('b','CAS: 2000, enter, × 1.075, enter … 2150, 2311.25, 2484.59, <b>2670.94</b> (4 presses)')],
  '',f'{CAM} · Example 20 (p. 361)',video='Cambridge GO · Example 20 (7D Resources)',cmd=('Determine',None,'count the presses'),
  parts=[('a','<i>V</i><sub>3</sub> = 1.075 × 2311.25 = <b>$2484.59</b>'),('b','After <b>4 years</b>')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3E WE1','Modelling geometric growth',
  '<div style="font-size:20px">In an environment where locusts were destroying farmers’ crops, a species of frog was introduced to eliminate the pests. Initially, 200 frogs were let out into the crops. Over the next few years, the farmers realised that the frog population was increasing, with 4 times as many frogs each year than in the previous year.</div>'
  +plist([('a','Model the scenario using a recurrence relation, where <i>f</i><sub>0</sub> represents the number of frogs let out into the crops initially.'),('b','How many frogs will there be in 4 years after their introduction, if nothing is done to stop their growth?')]),
  [('a','<i>a</i> = 200 · <i>R</i> = 4'),('b','200 → 800 → 3200 → 12 800 → 51 200')],
  '',f'{EDR12} · 3E Worked example 1 (p. 158)',cmd=('How many',None,'four steps'),
  parts=[('a',RR('200','4<i>f<sub>n</sub></i>','f')),('b','<b>51 200</b> frogs')]))

# Learn 7: reducing balance depreciation
S.append(learn('Learn · 7D','Reducing balance depreciation',
  '<h4>Lose <i>r</i>% of the CURRENT value each year</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>the value decays geometrically</li><li>next value = current − <i>r</i>% of current = <i>R</i> × current</li></ul>',
  '<div style="font-size:24px;text-align:center;line-height:1.8"><span class="frag">Sofa $7500, reducing balance 8.4% p.a.</span><br><span class="frag"><i>R</i> = 1 − 8.4/100 = 0.916</span><br><span class="frag">'+RR('7500','0.916 × <i>V<sub>n</sub></i>')+'</span></div>',
  'Decay: <i>R</i> = 1 − <i>r</i>/100 (8.4% → 0.916, not 0.084).',f'{CAM}, 7D pp. 361–362 (own words) · {EDR}, 5C',
  cards=(kcard('Reducing balance',RR('purchase price','<i>R</i> × <i>V<sub>n</sub></i>'),'<i>R</i> = 1 − <i>r</i>/100'),)))
S.append(qslide('we','Worked example 21 · 7D','Modelling reducing balance depreciation with recurrence relations',
  '<div style="font-size:28px;margin-top:40px">A sofa was purchased for $7500 and is depreciating at a reducing balance rate of 8.4% per annum. <b>Write down</b> a recurrence relation where <i>V<sub>n</sub></i> is the value of the sofa after <i>n</i> years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 7500'),fx('R','<i>R</i>',F('1 − ',FR([V('r','8.4')],['100'])),'0.916')],
  RR('7500','0.916 × <i>V<sub>n</sub></i>'),f'{CAM} · Example 21 (p. 362)',video='Cambridge GO · Example 21 (7D Resources)',cmd=('Write down',None,'V₀, then R')))
S.append(qslide('yt','You try · Edrolo 5C WE1','Modelling reducing balance depreciation',
  '<div style="font-size:19px">Determine the recurrence relation that models the depreciation in each of the following scenarios.</div>'
  +plist([('a','A tablet is worth $550 and is depreciated using a reducing balance depreciation method with a rate of 4.3% per annum.'),
          ('b','The graph shows the value of a boat, purchased for $60 000, over a period of four years.<br><span style="font-size:15px">(0, 60 000) (1, 48 000) (2, 38 400) (3, 30 720) (4, 24 576) (5, 19 661)</span>'+plot([60000,48000,38400,30720,24576,19661],60000,10000,W=320,Hh=150))]),
  [('a','<i>V</i><sub>0</sub> = 550 · <i>R</i> = 1 − 4.3/100 = 0.957'),('b','<i>V</i><sub>0</sub> = 60 000 · <i>R</i> = 48 000 ÷ 60 000 = 0.8 (same ratio every year)')],
  '',f'{EDR} · 5C Worked example 1 (p. 317); graph redrawn with the same labelled points',cmd=('Determine',None,'V₀, then R'),
  parts=[('a',RR('550','0.957 × <i>V<sub>n</sub></i>')),('b',RR('60 000','0.8 × <i>V<sub>n</sub></i>'))]))
S.append(qslide('we','Worked example 22 · 7D','Using reducing balance depreciation with recurrence relations',
  '<div style="font-size:22px">The following recurrence relation can be used to model the value of office furniture with a purchase price of $9600, depreciating at a reducing-balance rate of 7% per annum.<br>'+RR('9600','0.93 × <i>V<sub>n</sub></i>')+'<br>In the recurrence relation, <i>V<sub>n</sub></i> is the value of the office furniture after <i>n</i> years.</div>'
  +plist([('a','Use the recurrence relation to find the value of the office furniture, correct to the nearest cent, after 1, 2 and 3 years.'),('b','If the office furniture was initially purchased in 2023, at the end of which year will the value of the furniture first be less than $7000?')]),
  [('a','<i>V</i><sub>1</sub> = 0.93 × 9600 = 8928 · <i>V</i><sub>2</sub> = 0.93 × 8928 = 8303.04 · <i>V</i><sub>3</sub> = 0.93 × 8303.04 = 7721.83'),('b','CAS: … 7721.83, 7181.30, <b>6678.71</b> (5 presses): 2023 + 5')],
  '',f'{CAM} · Example 22 (p. 362)',video='Cambridge GO · Example 22 (7D Resources)',cmd=('find',None,'nearest cent'),
  parts=[('a','<b>$8928.00</b>, <b>$8303.04</b>, <b>$7721.83</b>'),('b','At the end of <b>2028</b>')]))
S.append(qslide('yt','You try · Edrolo 5C WE2a','Using reducing balance depreciation',
  '<div style="font-size:28px;margin-top:40px">A tablet is worth $550 and is depreciated using a reducing balance depreciation method with a rate of 4.3% per annum.<br>A recurrence relation is constructed to represent the depreciation of the tablet:<br><br>'+RR('550','0.957 × <i>V<sub>n</sub></i>')+'<br><br>a. After how many years will the value of the tablet drop below $505?</div>',
  [fx('V1','<i>V</i><sub>1</sub>',F('0.957 × ',V('V0','550')),'526.35'),fx('V2','<i>V</i><sub>2</sub>',F('0.957 × ',V('V1','526.35')),'503.716…')],
  'The value drops below $505 after <b>2 years</b>.',f'{EDR} · 5C Worked example 2a (p. 318)',cmd=('After how many years',None,'until the value is below 505')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['recursion-sequence']
S.append(cas('CAS · 7B / 7D','Generating a sequence from a recurrence relation',
  '<p style="font-size:24px">The office furniture is modelled by</p><p style="font-size:28px;text-align:center">'+RR('9600','0.93 × <i>V<sub>n</sub></i>')+'</p>'
  '<p style="font-size:24px">Generate the values on CAS and count the presses until the value is first less than $7000.</p>'
  '<p style="font-size:22px">Linear rules use + or − (e.g. <b>− 4800</b>); geometric rules use × (e.g. <b>× 0.93</b>).</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'9600, 8928, 8303.04, 7721.83, 7181.30, 6678.71 → first below $7000 after 5 presses = <i>V</i><sub>5</sub>',
  f'{CAM} · Example 22 (p. 362) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2019 Exam 1 Q19','Show what you know',
  '<div style="font-size:26px;margin-top:20px">Geoff purchased a computer for $4500. He will depreciate the value of his computer by a flat rate of 10% of the purchase price per annum.<br>A recurrence relation that Geoff can use to determine the value of the computer after <i>n</i> years, <i>V<sub>n</sub></i>, is</div>',
  [('D','10% of 4500 = 450 each year'),('Rule','flat rate: subtract the same amount: <i>V<sub>n</sub></i> − 450')],
  RR('4500','<i>V<sub>n</sub></i> – 450')+': <b>A</b>.',f'VCAA 2019 Further Mathematics Exam 1 Recursion and financial modelling Q19 (examiner report) · {EDR} 5B Q14',
  mc=[RR('4500','<i>V<sub>n</sub></i> – 450'),RR('4500','<i>V<sub>n</sub></i> + 450'),RR('4500','0.9 <i>V<sub>n</sub></i>'),RR('4500','1.1 <i>V<sub>n</sub></i>'),RR('4500','0.1 (<i>V<sub>n</sub></i> – 450)')],
  key='A',dist=[76,2,13,3,5],dis=('C','0.9<i>V<sub>n</sub></i> takes 10% of the CURRENT value: that is reducing balance, not flat rate')))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2020 Exam 2 Q7b','Show what you know',
  '<div style="font-size:28px;margin-top:30px">Samuel owns a printing machine.<br>The printing machine is depreciated in value by Samuel using flat rate depreciation.<br>The value of the machine, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation<br><br>'
  +RR('120 000','<i>V<sub>n</sub></i> – 15 000')+'<br><br>b. Showing recursive calculations, <b>determine</b> the value of the machine, in dollars, after two years. <span class="muted">(1 mark)</span></div>',
  [fx('V1','<i>V</i><sub>1</sub>',F(V('V0','120 000'),' – 15 000'),'105 000'),fx('V2','<i>V</i><sub>2</sub>',F(V('V1','105 000'),' – 15 000'),'90 000')],
  'The machine is worth <b>$90 000</b> after two years (show both lines: the answer alone gets no mark).',f'VCAA 2020 Further Mathematics Exam 2 Q7 stem and Q7b (examiner report: average 0.7/1) · {EDR} 5B Q15',
  stat=('mark',72),cmd=('determine',1,'V₁ then V₂, each written out')))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2019 Exam 2 Q7a','Show what you know',
  '<div style="font-size:28px;margin-top:30px">Phil is a builder who has purchased a large set of tools.<br>The value of Phil’s tools is depreciated using the reducing balance method.<br>The value of the tools, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation shown below.<br><br>'
  +RR('60 000','0.9 <i>V<sub>n</sub></i>')+'<br><br>a. Use recursion to <b>show that</b> the value of the tools after two years, <i>V</i><sub>2</sub>, is $48 600. <span class="muted">(1 mark)</span></div>',
  [fx('V1','<i>V</i><sub>1</sub>',F('0.9 × ',V('V0','60 000')),'54 000'),fx('V2','<i>V</i><sub>2</sub>',F('0.9 × ',V('V1','54 000')),'48 600')],
  '<i>V</i><sub>1</sub> = 0.9 × 60 000 = 54 000, <i>V</i><sub>2</sub> = 0.9 × 54 000 = <b>48 600</b> ✓',f'VCAA 2019 Further Mathematics Exam 2 Q7 stem and Q7a (examiner report: 74% full marks) · {EDR} 5C Q13',
  stat=('mark',74),cmd=('show that',1,'start from V₀, write each step')))

# ================= closing
S.append(checkin(SC_).replace('<ul class="tick">','<ul class="tick" style="columns:2;column-gap:36px">'))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 7 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('7B','7D') and v.get('url')]))
n=assemble(S,'12MAG · L32 · Linear and geometric growth and decay',os.path.join(ROOT,'lessons','7B-7D slides.html'))
print(n-1,'slides')
