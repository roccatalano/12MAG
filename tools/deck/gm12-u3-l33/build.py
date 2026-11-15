"""Lesson gm12-u3-l33 (7C explicit rules for linear growth and decay, 7E explicit rules for geometric growth and decay) slides,
built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/7C-7E slides.html     Run: python3 tools/deck/gm12-u3-l33/build.py     Screenshots: python3 tools/deck/gm12-u3-l33/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- CFAT 2.7.1 (7A-7B-7D) first (planner card).
- Do Now: VCAA 2023 Exam 1 Q20 (stem of Q20-21; report 82% C, 2/5/82/6/5) ·
          VCAA 2024 Exam 1 Q19 (scanned paper read from the page image; report 72% C, 4/13/72/11) ·
          VCAA 2025 Exam 2 Q8ai (graph redrawn with the same points as the paper; report 73% full marks) ·
          VCAA 2024 NHT Exam 2 Q8c (stem of Q8 + reducing balance lead-in; NHT report gives no %).
- APK: Cambridge U1&2 Ch 3 skills checklist 3D #10 and 3G #21 (solutions worked for 12MAG) ·
       VCAA 2018 Further Exam 2 Q4c i-ii (= Edrolo U1&2 3F Q12; report 78% / 65% full marks).
- Learn: Cambridge U3&4 7C pp. 350-355, 7E pp. 366-370 (own words) · Edrolo U3&4 5D, 5E, 5F.
- Worked examples: Cambridge U3&4 Examples 13-18 (7C, pp. 352-355) and 23-27 (7E, pp. 367-370).
  You trys (planner card): Ex 13 = Edrolo U1&2 3F WE1 (p. 167) · Ex 14 = Edrolo U3&4 5E WE2 (p. 335) · Ex 15 = Edrolo U1&2 3F WE2 (pp. 167-168) ·
  Ex 16 = Edrolo U3&4 5D WE1a (p. 325) · Ex 17 = 5D WE1b (p. 326; rule from part a given) · Ex 18 = 5D WE2 (pp. 326-327) ·
  Ex 23 = Edrolo U1&2 3F WE3 (p. 169) · Ex 24 = Edrolo U3&4 5F WE2 (p. 342; monthly compounding, 7F preview) ·
  Ex 25 = Edrolo U3&4 5C WE2b-c (pp. 318-319) · Ex 26, 27 = written for 12MAG (planner/written-youtrys.json YT-7E-26, YT-7E-27).
- CAS: planner/cas-skills.json 'solve-n-r' (task = Cambridge Example 26).
- Exits: VCAA 2020 Further Exam 1 Q29 (Edrolo U3&4 5D Q17; report 54% B, 14/54/14/11/7) ·
         VCAA 2021 Further Exam 1 Q20 (5D Q18; report 44% C, 3/40/44/9/4) ·
         VCAA 2012 Further Exam 1 Business-related mathematics Q2 (5E Q16; no examiner report on G:, so no %).
"""
import os, sys, json
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l33')
WY={w['id']:w for w in (lambda d:d if isinstance(d,list) else d.get('items',[]))(json.load(open(os.path.join(ROOT,'planner','written-youtrys.json'))))}
yid=lambda u:u.split('v=')[1].split('&')[0]
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
Vn=lambda L='V',n='n':f'<i>{L}</i><sub>{n}</sub>'
def plot(vals,ymax,ystep,L='V',W=380,Hh=230,col='#1565C0'):
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
S.append(title(33,'Explicit rules for linear and geometric growth and decay',f'{CAM} · 7C Using an explicit rule for linear growth or decay · 7E Using an explicit rule for geometric growth or decay','L33',
               flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')).replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('CFAT 2.7.1','· 7A, 7B, 7D · 20 min','var(--muted)'),('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills + one VCAA question','var(--apk)'),
  ('7C Linear rules','',None),('Worked examples 13–18','→ You try',None),('7E Geometric rules','',None),
  ('Worked examples 23–27','→ You try',None),('CAS: solving for n or r','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S[-1]=S[-1].replace('<section class="slide T ','<section id="tdy" class="slide T ',1).replace('</section>','<style>#tdy .card3 li{font-size:15px!important;line-height:1.22!important;padding-top:3px!important;padding-bottom:3px!important}</style></section>')
S.append(keys([
  ('Recurrence relation','gives the NEXT term from the current one: step by step'),
  ('Explicit rule','gives any term <i>V<sub>n</sub></i> straight from <i>n</i>: no stepping'),
  ('Simple interest · flat rate','linear: the same amount <i>D</i> (= <i>r</i>% of <i>V</i><sub>0</sub>) added / subtracted each year'),
  ('Unit cost','linear decay: <i>D</i> = depreciation per unit of use (per hour, per km)'),
  ('Compound interest · reducing balance','geometric: × <i>R</i> each year (<i>R</i> &gt; 1 growth, <i>R</i> &lt; 1 decay)'),
  ('Interest earned · total depreciation','<i>V<sub>n</sub></i> − <i>V</i><sub>0</sub> · <i>V</i><sub>0</sub> − <i>V<sub>n</sub></i>')],
  [('Linear rule',F('<i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> ± <i>n</i>D'),'<i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub> (simple interest, flat rate)'),
   ('Geometric rule',F('<i>V<sub>n</sub></i> = <i>R</i><sup><i>n</i></sup> × <i>V</i><sub>0</sub>'),'<i>R</i> = 1 + <i>r</i>/100 (growth) · <i>R</i> = 1 − <i>r</i>/100 (decay)'),
   ('Solving for n',F('round <i>n</i> UP'),'interest / depreciation happens at the END of each period')],
  f'{CAM}, 7C pp. 350–355 and 7E pp. 366–370; Study Design: rules for future value after <i>n</i> periods (flat rate, unit cost, reducing balance, compound interest)'))
S.append(cfat('CFAT 2.7.1','Recurrence relations: growth and decay','7A, 7B, 7D',15,'CFAT 2.7.1 (7A-7B-7D) · Edrolo General Mathematics Units 3&amp;4 exercise questions (see the CFAT for sources)'))

# ================= Do Now (retrieval)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q20','Review of 7B (last lesson)',
  '<div style="font-size:26px;margin-top:20px">For taxation purposes, Audrey depreciates the value of her $3000 computer over a four-year period. At the end of the four years, the value of the computer is $600.<br><br>If Audrey uses flat rate depreciation, the depreciation rate, per annum is</div>',
  [('Total','3000 − 600 = 2400 over 4 years'),('Per year','2400 ÷ 4 = 600 each year'),fx('Rate','<i>r</i>',F(FR([V('D','600')],[V('V0','3000')]),' × 100%'),'20%')],
  'Flat rate depreciation of <b>20%</b> per annum: <b>C</b>.','VCAA 2023 General Mathematics Exam 1 Q20–21 stem and Q20 (examiner report)',
  mc=['10%','15%','20%','25%','33%'],key='C',dist=[2,5,82,6,5]))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q19','Review of 7D (last lesson)',
  '<div style="font-size:26px;margin-top:20px">Liv bought a new car for $35 000. The value of the car will be depreciated by 18% per annum using the reducing balance method.<br>A recurrence relation that models the year-to-year value of her car is of the form<br><br>'
  +RR('35 000','<i>k</i> × <i>L<sub>n</sub></i>','L')+'<br><br>The value of <i>k</i> is</div>',
  [fx('R','<i>k</i>',F('1 − ',FR([V('r','18')],['100'])),'0.82')],
  '<i>k</i> = <b>0.82</b>: <b>C</b>.','VCAA 2024 General Mathematics Exam 1 Q19 (examiner report)',
  mc=['0.0082','0.18','0.82','1.18'],key='C',dist=[4,13,72,11],dis=('B','0.18 is the amount LOST each year; the value kept is 1 − 0.18')))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q8ai','Review of 7B (last lesson)',
  ('<div style="font-size:20px">Declan depreciates the value of his lighting equipment using flat rate depreciation.<br>The graph below shows the value, in dollars, of the lighting equipment, <i>V<sub>n</sub></i>, after <i>n</i> years.</div>',
   plot([40000,32000,24000,16000,8000],40000,8000,W=420,Hh=220),
   '<div style="font-size:20px">a. The value of the lighting equipment could be modelled by either a recurrence relation or a rule.<br>&nbsp;&nbsp;i. <b>Write</b> a <b>recurrence relation</b> in terms of <i>V</i><sub>0</sub>, <i>V</i><sub><i>n</i>+1</sub> and <i>V<sub>n</sub></i>. <span class="muted">(1 mark)</span></div>'),
  [('V0','start of the graph: <i>V</i><sub>0</sub> = 40 000'),('D','drops 8000 each year (40 000 → 32 000)')],
  RR('40 000','<i>V<sub>n</sub></i> − 8000'),'VCAA 2025 General Mathematics Exam 2 Q8 stem and Q8ai (examiner report: 73% full marks); graph redrawn with the same points',
  stat=('mark',73),cmd=('Write',1,'V₀, then the common difference')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q8c','Review of 7D (last lesson)',
  '<div style="font-size:24px;margin-top:10px">Cleo owns equipment that was purchased for $50 000.<br>Another option for Cleo is to depreciate the value of the $50 000 equipment using the reducing balance method.<br>The value of the equipment, in dollars, after <i>n</i> months, <i>V<sub>n</sub></i>, can be modelled by a recurrence relation of the form<br><br>'
  +RR('50 000','<i>RV<sub>n</sub></i>')+'<br><br>c. If the depreciation rate per month was 1.5%, what would be the value of <i>R</i> in this recurrence relation? <span class="muted">(1 mark)</span></div>',
  [fx('R','<i>R</i>',F('1 − ',FR([V('r','1.5')],['100'])),'0.985')],
  '<i>R</i> = <b>0.985</b>','VCAA 2024 (NHT) General Mathematics Exam 2 Q8 stem and Q8c (NHT examiner report gives no % statistics)',
  cmd=('what would be',1,'R = 1 − r/100')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3D #10','Finding the nth term of an arithmetic sequence',
  '<div style="font-size:30px;margin-top:50px">Consider the recurrence relation: '+RR('40','<i>t<sub>n</sub></i> − 3','t')+'. Find <i>t</i><sub>20</sub>.</div>',
  [('Pattern','each step subtracts 3: after 20 steps, 20 × 3 = 60 has gone'),fx('t20','<i>t</i><sub>20</sub>',F(V('t0','40'),' − 20 × 3'),'−20')],
  '<i>t</i><sub>20</sub> = <b>−20</b>',f'{CAM12} · Ch 3 skills checklist 3D #10 · solution worked for 12MAG',cmd=('Find',None,'start − 20 × 3')))
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3G #21','Finding the nth term of a geometric sequence',
  '<div style="font-size:30px;margin-top:50px">Find the fifth term in the geometric sequence generated by the following recurrence relation: '+RR('10','2<i>t<sub>n</sub></i>','t')+'.</div>',
  [('Terms','<i>t</i><sub>0</sub> is the first term, so the fifth term is <i>t</i><sub>4</sub>'),('Multiply','10 → 20 → 40 → 80 → 160')],
  'The fifth term is <i>t</i><sub>4</sub> = <b>160</b>.',f'{CAM12} · Ch 3 skills checklist 3G #21 · solution worked for 12MAG',cmd=('Find',None,'× 2 four times')))
S.append(qslide('apk','APK · VCAA 2018 Exam 2 Q4c','Writing a rule from a recurrence relation',
  '<div style="font-size:23px">Julie deposits some money into a savings account that will pay compound interest every month.<br>The balance of Julie’s account, in dollars, after <i>n</i> months can be modelled by the recurrence relation shown.<br>'
  +RR('12 000','1.0062 × <i>V<sub>n</sub></i>')+'<br>A rule of the form <i>V<sub>n</sub></i> = <i>a</i> × <i>b<sup>n</sup></i> can be used to determine the balance of Julie’s account after <i>n</i> months.</div>'
  +plist([('i','<b>Complete</b> this rule for Julie’s investment after <i>n</i> months by writing the appropriate numbers in the boxes provided. <span class="muted">(1 mark)</span><br>balance = ☐ × ☐<sup><i>n</i></sup>'),
          ('ii','What would be the value of <i>n</i> if Julie wanted to determine the value of her investment after three years? <span class="muted">(1 mark)</span>')]),
  [('i','<i>a</i> = <i>V</i><sub>0</sub> = 12 000 · <i>b</i> = <i>R</i> = 1.0062'),('ii','<i>n</i> counts months: 3 × 12')],
  '',f'VCAA 2018 Further Mathematics Exam 2 Q4 stem and Q4c (examiner report: i 78%, ii 65% full marks) · {EDR12} 3F Q12',
  stat=('mark',78),cmd=('Complete',1,'V₀ in the first box, R in the second'),
  parts=[('i','balance = <b>12 000</b> × <b>1.0062</b><sup><i>n</i></sup>'),('ii','<i>n</i> = <b>36</b>')]))

# ================= 7C Learn
S.append(learn('Learn · 7C','From recurrence relation to explicit rule (linear)',
  '<h4>Skip the steps: jump straight to term <i>n</i></h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>after <i>n</i> steps, <i>D</i> has been added (or subtracted) <i>n</i> times</li><li>growth: <i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> + <i>nD</i> · decay: <i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> − <i>nD</i></li>'
  '<li>simple interest and flat rate: <i>D</i> = <i>r</i>/100 × <i>V</i><sub>0</sub> · unit cost: <i>D</i> = cost per unit</li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">$2000 at 5% simple interest: '+RR('2000','<i>V<sub>n</sub></i> + 100')+'</span><br>'
  '<span class="frag"><i>V</i><sub>1</sub> = 2000 + 1 × 100 · <i>V</i><sub>2</sub> = 2000 + 2 × 100 · <i>V</i><sub>3</sub> = 2000 + 3 × 100</span><br>'
  '<span class="frag"><b><i>V<sub>n</sub></i> = 2000 + 100<i>n</i></b> &nbsp;→&nbsp; <i>V</i><sub>15</sub> = 2000 + 15 × 100 = $3500</span></div>',
  'Count the steps: the subscript tells you how many times <i>D</i> was added.',f'{CAM}, 7C pp. 350–352 (own words) · {EDR}, 5D, 5E',
  cards=(kcard('Linear rule','<i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> ± <i>nD</i>'),)))
S.append(qslide('we','Worked example 13 · 7C','Converting a recurrence relation to an explicit rule',
  '<div style="font-size:26px;margin-top:10px">Write down a rule for <i>V<sub>n</sub></i> for each of the following recurrence relations. Calculate <i>V</i><sub>10</sub> for each case.</div>'
  +plist([('a',RR('8','<i>V<sub>n</sub></i> + 3')),('b',RR('400','<i>V<sub>n</sub></i> − 12')),('c',RR('30','<i>V<sub>n</sub></i> − 7'))]),
  [('a','<i>V</i><sub>0</sub> = 8, <i>D</i> = 3 (growth)'),('b','<i>V</i><sub>0</sub> = 400, <i>D</i> = 12 (decay)'),('c','<i>V</i><sub>0</sub> = 30, <i>D</i> = 7 (decay)')],
  '',f'{CAM} · Example 13 (p. 352)',video='Cambridge GO · Example 13 (7C Resources)',cmd=('Write down',None,'V₀ and D, then substitute n = 10'),
  parts=[('a','<i>V<sub>n</sub></i> = 8 + 3<i>n</i> · <i>V</i><sub>10</sub> = <b>38</b>'),('b','<i>V<sub>n</sub></i> = 400 − 12<i>n</i> · <i>V</i><sub>10</sub> = <b>280</b>'),('c','<i>V<sub>n</sub></i> = 30 − 7<i>n</i> · <i>V</i><sub>10</sub> = <b>−40</b>')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3F WE1','Modelling a linear sequence with a rule',
  '<div style="font-size:21px">The population of kakapos in New Zealand is being monitored after the species is declared critically endangered.<br>Initially, there are 100 kakapos. Each month, the population will increase by 2 kakapos due to the introduction of a breeding program.<br>Let <i>P<sub>n</sub></i> be the kakapos population in New Zealand <i>n</i> months after the introduction of the breeding program.</div>'
  +plist([('a','Construct a rule that can be used to calculate <i>P<sub>n</sub></i>.'),('b','Determine the population of kakapos after 1 year.')]),
  [('a','<i>P</i><sub>0</sub> = 100 · <i>d</i> = 2'),('b','<i>n</i> counts months: 1 year = 12 months')],
  '',f'{EDR12} · 3F Worked example 1 (p. 167)',cmd=('Construct',None,'start value, then common difference'),
  parts=[('a','<i>P<sub>n</sub></i> = 100 + 2<i>n</i>'),('b','<i>P</i><sub>12</sub> = 100 + 2 × 12 = <b>124 kakapos</b>')]))
S.append(qslide('we','Worked example 14 · 7C','Modelling simple interest investments',
  '<div style="font-size:30px;margin-top:60px">Amie invests $3000 in a simple interest investment with interest paid at the rate of 6.5% per year.<br><br><b>Use</b> a rule to find the value of the investment after 10 years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 3000'),fx('D','<i>D</i>',F(FR([V('r','6.5')],['100']),' × 3000'),'195'),('Rule','<i>V<sub>n</sub></i> = 3000 + 195<i>n</i>'),fx('V10','<i>V</i><sub>10</sub>',F('3000 + 195 × ',V('n','10')),'4950')],
  'After 10 years the investment is worth <b>$4950</b>.',f'{CAM} · Example 14 (p. 353)',video='Cambridge GO · Example 14 (7C Resources)',cmd=('Use',None,'V₀, D, rule, substitute')))
S.append(qslide('yt','You try · Edrolo 5E WE2','Modelling simple interest using a rule',
  '<div style="font-size:26px;margin-top:30px">Joan invests $5000 in an account paying a simple interest rate of 4.5% per year.</div>'
  +plist([('a','Construct a rule that will calculate the value of the investment, <i>V<sub>n</sub></i>, after <i>n</i> years.'),('b','Use the rule to calculate the value of the investment after five years.')]),
  [('a','<i>V</i><sub>0</sub> = 5000 · <i>d</i> = 4.5/100 × 5000 = 225'),('b','substitute <i>n</i> = 5')],
  '',f'{EDR} · 5E Worked example 2 (p. 335)',cmd=('Construct',None,'V₀ and d first'),
  parts=[('a','<i>V<sub>n</sub></i> = 5000 + 225<i>n</i>'),('b','<i>V</i><sub>5</sub> = 5000 + 225 × 5 = <b>$6125.00</b>')]))
S.append(qslide('we','Worked example 15 · 7C','Using a rule to determine the value of a simple interest investment',
  '<div style="font-size:21px">The following recurrence relation can be used to model a simple interest investment:<br>'+RR('3000','<i>V<sub>n</sub></i> + 260')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.</div>'
  +plist([('a','What is the principal of the investment? How much interest is added each year?'),('b','Write down the rule for the value of the investment after <i>n</i> years.'),
          ('c','Use a rule to find the value of the investment after 15 years.'),('d','Use a rule to find when the value of the investment first exceeds $10 000.')]),
  [('a','read off the recurrence relation'),('b','<i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> + <i>nD</i>'),('c','<i>V</i><sub>15</sub> = 3000 + 260 × 15'),('d','10 000 = 3000 + 260<i>n</i> → <i>n</i> = 7000 ÷ 260 = 26.92… → round UP')],
  '',f'{CAM} · Example 15 (p. 353)',video='Cambridge GO · Example 15 (7C Resources)',cmd=('Use',None,'d: round UP to whole years'),
  parts=[('a','Principal <b>$3000</b> · interest <b>$260</b> each year'),('b','<i>V<sub>n</sub></i> = 3000 + 260<i>n</i>'),('c','<b>$6900</b>'),('d','After <b>27 years</b>')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3F WE2','Simple interest and flat rate rules',
  '<div style="font-size:20px">Consider the following scenarios.</div>'
  +plist([('a','Lep borrows $250 from his older sibling who charges simple interest at a rate of 5% per annum.<br>The value of the loan, <i>V<sub>n</sub></i>, after <i>n</i> years can be modelled by the following recurrence relation.<br>'+RR('250','<i>V<sub>n</sub></i> + 12.5')+'<br>Construct a rule that can be used to calculate the amount Lep owes after <i>n</i> years.'),
          ('b','Clove purchases an asset worth $2000. Its value depreciates using the flat rate method, at a rate of 2.5% per year.<br>The value of the asset, <i>C<sub>n</sub></i>, after <i>n</i> years can be modelled using the following rule.<br><i>C<sub>n</sub></i> = 2000 − 50<i>n</i><br>Calculate the value of the asset after 15 years.')]),
  [('a','<i>V</i><sub>0</sub> = 250 · <i>d</i> = 5/100 × 250 = 12.5'),('b','<i>n</i> = 15: <i>C</i><sub>15</sub> = 2000 − 50 × 15')],
  '',f'{EDR12} · 3F Worked example 2 (pp. 167–168)',cmd=('Construct',None,'b: substitute n = 15'),
  parts=[('a','<i>V<sub>n</sub></i> = 250 + 12.5<i>n</i>'),('b','<b>$1250</b>')]))
S.append(qslide('we','Worked example 16 · 7C','Modelling flat rate depreciation of an asset using an explicit rule',
  '<div style="font-size:30px;margin-top:60px">A photocopier costs $6000 when new. Its value depreciates at the flat rate of 17.5% per year. <b>Write</b> a rule and use this to find its value after 4 years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 6000'),fx('D','<i>D</i>',F(FR([V('r','17.5')],['100']),' × 6000'),'1050'),('Rule','<i>V<sub>n</sub></i> = 6000 − 1050<i>n</i> (linear decay)'),fx('V4','<i>V</i><sub>4</sub>',F('6000 − 1050 × ',V('n','4')),'1800')],
  'The value after 4 years is <b>$1800</b>.',f'{CAM} · Example 16 (p. 354)',video='Cambridge GO · Example 16 (7C Resources)',cmd=('Write',None,'V₀, D, rule, substitute')))
S.append(qslide('yt','You try · Edrolo 5D WE1a','Creating a rule for flat rate depreciation',
  '<div style="font-size:28px;margin-top:50px">Kwyjibo bought an apartment for $670 000 in what he thought was a high-growth suburb. Unfortunately, the growth stopped once he bought the property and it is now depreciating yearly by 1.5% of its initial value.<br><br>a. Write the rule to determine <i>V<sub>n</sub></i>, the value of the apartment after <i>n</i> years.</div>',
  [('V0','<i>V</i><sub>0</sub> = 670 000'),fx('d','<i>d</i>',F('670 000 × ',FR([V('r','1.5')],['100'])),'10 050')],
  '<i>V<sub>n</sub></i> = 670 000 − 10 050<i>n</i>',f'{EDR} · 5D Worked example 1a (p. 325)',cmd=('Write',None,'V₀, then d')))
S.append(qslide('we','Worked example 17 · 7C','Using a rule for the flat rate depreciation of an asset',
  '<div style="font-size:21px">The following recurrence relation can be used to model the flat rate of depreciation of a set of office furniture:<br>'+RR('12 000','<i>V<sub>n</sub></i> − 1200')+'<br>where <i>V<sub>n</sub></i> is the value of the furniture after <i>n</i> years.</div>'
  +plist([('a','What is the initial value of the furniture? How much does the furniture decrease by each year?'),('b','Write down the rule for the value of the furniture after <i>n</i> years.'),
          ('c','Use a rule to find the value of the furniture after 6 years.'),('d','How long does it take for the furniture’s value to decrease to zero?')]),
  [('a','read off the recurrence relation'),('b','<i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> − <i>nD</i>'),('c','<i>V</i><sub>6</sub> = 12 000 − 1200 × 6'),('d','0 = 12 000 − 1200<i>n</i> → <i>n</i> = 10')],
  '',f'{CAM} · Example 17 (p. 354)',video='Cambridge GO · Example 17 (7C Resources)',cmd=('How long',None,'d: set Vₙ = 0'),
  parts=[('a','Initial value <b>$12 000</b> · decreases <b>$1200</b> each year'),('b','<i>V<sub>n</sub></i> = 12 000 − 1200<i>n</i>'),('c','<b>$4800</b>'),('d','<b>10 years</b>')]))
S.append(qslide('yt','You try · Edrolo 5D WE1b','Using a rule for flat rate depreciation',
  '<div style="font-size:28px;margin-top:50px">Kwyjibo bought an apartment for $670 000 in what he thought was a high-growth suburb. Unfortunately, the growth stopped once he bought the property and it is now depreciating yearly by 1.5% of its initial value.<br><span class="muted" style="font-size:22px">(Part a: <i>V<sub>n</sub></i> = 670 000 − 10 050<i>n</i>)</span><br><br>b. Find the value of Kwyjibo’s apartment after 9 years.</div>',
  [fx('V9','<i>V</i><sub>9</sub>',F('670 000 − 10 050 × ',V('n','9')),'579 550')],
  'The apartment is worth <b>$579 550</b> after 9 years.',f'{EDR} · 5D Worked example 1b (p. 326)',cmd=('Find',None,'substitute n = 9')))
S.append(qslide('we','Worked example 18 · 7C','Using an explicit rule for unit cost depreciation',
  '<div style="font-size:20px">A hairdryer in a salon was purchased for $850. The value of the hairdryer depreciates by 25 cents for every hour it is in use.<br>Let <i>V<sub>n</sub></i> be the value of the hairdryer after <i>n</i> hours of use.</div>'
  +plist([('a','Write down a rule to find the value of the hairdryer after <i>n</i> hours of use.'),('b','What is the value of the hairdryer after 50 hours of use?'),
          ('c','On average, the salon will use the hairdryer for 17 hours each week. How many weeks will it take for the value of the hairdryer to halve?'),
          ('d','The hairdryer has a scrap value of $100 before it is disposed of. Find the number of hours of use before this occurs.')]),
  [('a','<i>V</i><sub>0</sub> = 850 · <i>D</i> = 0.25 per hour'),('b','<i>V</i><sub>50</sub> = 850 − 0.25 × 50'),('c','425 = 850 − 0.25<i>n</i> → <i>n</i> = 1700 hours → 1700 ÷ 17'),('d','100 = 850 − 0.25<i>n</i> → 0.25<i>n</i> = 750')],
  '',f'{CAM} · Example 18 (p. 355)',video='Cambridge GO · Example 18 (7C Resources)',cmd=('Find',None,'D is per HOUR: convert c to weeks'),
  parts=[('a','<i>V<sub>n</sub></i> = 850 − 0.25<i>n</i>'),('b','<b>$837.50</b>'),('c','<b>100 weeks</b>'),('d','<b>3000 hours</b>')]))
S[-1]=S[-1].replace('<section class="slide T we','<section class="slide T we sm',1)
S.append(qslide('yt','You try · Edrolo 5D WE2','Creating and using a rule for unit cost depreciation',
  '<div style="font-size:26px;margin-top:30px">Samson purchased a computer worth $2000. The research he did online told him that the model of computer he purchased depreciates by $0.32 for every hour of use.</div>'
  +plist([('a','Write the rule to determine <i>V<sub>n</sub></i>, the value of the computer after <i>n</i> hours of use.'),('b','What is the value of Samson’s computer after 300 hours of use?')]),
  [('a','<i>V</i><sub>0</sub> = 2000 · <i>d</i> = 0.32 per hour'),('b','<i>V</i><sub>300</sub> = 2000 − 0.32 × 300 = 2000 − 96')],
  '',f'{EDR} · 5D Worked example 2 (pp. 326–327)',cmd=('Write',None,'d = depreciation per unit of use'),
  parts=[('a','<i>V<sub>n</sub></i> = 2000 − 0.32<i>n</i>'),('b','<b>$1904</b>')]))

# ================= 7E Learn
S.append(learn('Learn · 7E','Explicit rule for geometric growth and decay',
  '<h4>Multiply by <i>R</i>, <i>n</i> times</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>V<sub>n</sub></i> = <i>R<sup>n</sup></i> × <i>V</i><sub>0</sub> (same rule for growth and decay)</li><li>compound interest: <i>R</i> = 1 + <i>r</i>/100 · reducing balance: <i>R</i> = 1 − <i>r</i>/100</li>'
  '<li>interest earned = <i>V<sub>n</sub></i> − <i>V</i><sub>0</sub> · total depreciation = <i>V</i><sub>0</sub> − <i>V<sub>n</sub></i></li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">$2000 at 5% compound interest: '+RR('2000','1.05<i>V<sub>n</sub></i>')+'</span><br>'
  '<span class="frag"><i>V</i><sub>1</sub> = 1.05 × 2000 · <i>V</i><sub>2</sub> = 1.05<sup>2</sup> × 2000 · <i>V</i><sub>3</sub> = 1.05<sup>3</sup> × 2000</span><br>'
  '<span class="frag"><b><i>V<sub>n</sub></i> = 1.05<sup><i>n</i></sup> × 2000</b> &nbsp;→&nbsp; <i>V</i><sub>18</sub> = 1.05<sup>18</sup> × 2000 = $4813.24</span></div>',
  'Interest IN one year = <i>V<sub>n</sub></i> − <i>V</i><sub><i>n</i>−1</sub>; interest OVER <i>n</i> years = <i>V<sub>n</sub></i> − <i>V</i><sub>0</sub>.',f'{CAM}, 7E pp. 366–369 (own words) · {EDR}, 5D, 5F',
  cards=(kcard('Geometric rule','<i>V<sub>n</sub></i> = <i>R<sup>n</sup></i> × <i>V</i><sub>0</sub>','<i>R</i> = 1 ± <i>r</i>/100'),)))
S.append(qslide('we','Worked example 23 · 7E','Writing explicit rules for geometric growth and decay',
  '<div style="font-size:28px;margin-top:20px">Write down a rule for the value of <i>V<sub>n</sub></i> in terms of <i>n</i> for each of the following. Use the rule to find the value of <i>V</i><sub>6</sub>.</div>'
  +plist([('a',RR('5','4<i>V<sub>n</sub></i>')),('b',RR('10','0.5<i>V<sub>n</sub></i>'))]),
  [('a','<i>V</i><sub>0</sub> = 5, <i>R</i> = 4'),('b','<i>V</i><sub>0</sub> = 10, <i>R</i> = 0.5')],
  '',f'{CAM} · Example 23 (p. 367)',video='Cambridge GO · Example 23 (7E Resources)',cmd=('Write down',None,'V₀ and R, then n = 6'),
  parts=[('a','<i>V<sub>n</sub></i> = 4<sup><i>n</i></sup> × 5 · <i>V</i><sub>6</sub> = <b>20 480</b>'),('b','<i>V<sub>n</sub></i> = 0.5<sup><i>n</i></sup> × 10 · <i>V</i><sub>6</sub> = <b>0.156 25</b>')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3F WE3','Modelling a geometric sequence with a rule',
  '<div style="font-size:24px;margin-top:20px">The number of stem cells in a live culture is being monitored as part of a drug trial.<br>Initially, there were 4 cells in the agar plate. Each hour, the number of cells doubles.</div>'
  +plist([('a','Construct a rule that can be used to model the number of stem cells, <i>S<sub>n</sub></i>, in the agar plate after <i>n</i> hours.'),('b','How many cells will there be after a full day?')]),
  [('a','<i>S</i><sub>0</sub> = 4 · <i>R</i> = 2'),('b','<i>n</i> counts hours: a day = 24 hours')],
  '',f'{EDR12} · 3F Worked example 3 (p. 169)',cmd=('Construct',None,'start value, then common ratio'),
  parts=[('a','<i>S<sub>n</sub></i> = 4 × 2<sup><i>n</i></sup>'),('b','<i>S</i><sub>24</sub> = 4 × 2<sup>24</sup> = <b>67 108 864 cells</b>')]))
S.append(qslide('we','Worked example 24 · 7E','Using a rule to find the value of an investment after n years',
  '<div style="font-size:21px">The rule for the value of the investment after <i>n</i> years, <i>V<sub>n</sub></i>, is shown below.<br><i>V<sub>n</sub></i> = 1.09<sup><i>n</i></sup> × 10 000</div>'
  +plist([('a','State how much money was initially invested.'),('b','Find the annual interest rate for this investment.'),('c','Find the value of the investment after 4 years, correct to the nearest cent.'),
          ('d','Find the amount of interest earned over the first 4 years, correct to the nearest cent.'),('e','Find the amount of interest earned in the fourth year, correct to the nearest cent.'),('f','Determine if the investor has doubled their money within 10 years.')]),
  [('a','read off <i>V</i><sub>0</sub>'),('b','<i>R</i> = 1.09 = 1 + 9/100'),('c','<i>V</i><sub>4</sub> = 1.09<sup>4</sup> × 10 000 = 14 115.816…'),('d','<i>V</i><sub>4</sub> − <i>V</i><sub>0</sub>'),
   ('e','<i>V</i><sub>3</sub> = 12 950.29 → <i>V</i><sub>4</sub> − <i>V</i><sub>3</sub>'),('f','<i>V</i><sub>10</sub> = 1.09<sup>10</sup> × 10 000 = 23 673.64 &gt; 20 000')],
  '',f'{CAM} · Example 24 (pp. 367–368)',video='Cambridge GO · Example 24 (7E Resources)',cmd=('Find',None,'over 4 years vs IN the 4th year'),
  parts=[('a','<b>$10 000</b>'),('b','<b>9%</b>'),('c','<b>$14 115.82</b>'),('d','<b>$4115.82</b>'),('e','<b>$1165.53</b>'),('f','<b>Yes</b> ($23 673.64 &gt; $20 000)')]))
S[-1]=S[-1].replace('<section class="slide T we','<section class="slide T we sm',1)
S.append(qslide('yt','You try · Edrolo 5F WE2','Modelling compound interest using a rule',
  '<div style="font-size:26px;margin-top:30px">$20 000 is invested into an account earning compound interest at a rate of 9% per annum, compounding monthly.</div>'
  +plist([('a','Construct a rule that can be used to calculate the balance of the account, <i>V<sub>n</sub></i> after <i>n</i> months.'),('b','How much interest would the account have earned after 4 years?')]),
  [('a','monthly: <i>r</i> = 9 ÷ 12 = 0.75% · <i>R</i> = 1 + 0.75/100 = 1.0075'),('b','<i>n</i> = 4 × 12 = 48 · <i>V</i><sub>48</sub> = 20 000 × 1.0075<sup>48</sup> = 28 628.106… · − 20 000')],
  '',f'{EDR} · 5F Worked example 2 (p. 342) · monthly rates come back in 7F',cmd=('Construct',None,'rate per MONTH = annual ÷ 12'),
  parts=[('a','<i>V<sub>n</sub></i> = 20 000 × 1.0075<sup><i>n</i></sup>'),('b','<b>$8628.11</b>')]))
S.append(qslide('we','Worked example 25 · 7E','Value and total depreciation after reducing balance depreciation',
  '<div style="font-size:22px">A machine costs $9500 to buy, and decreases in value with reducing balance depreciation of 20% each year. A recurrence relation that can be used to model the value of the machine after <i>n</i> years, <i>V<sub>n</sub></i>, is shown below.<br>'+RR('9500','0.8 × <i>V<sub>n</sub></i>')+'</div>'
  +plist([('a','Write down the rule for the value of the machine after <i>n</i> years.'),('b','Use the rule to find the value of the machine after 8 years. Write your answer, correct to the nearest cent.'),('c','Calculate the total depreciation of the machine after 8 years.')]),
  [('a','<i>V</i><sub>0</sub> = 9500 · <i>R</i> = 1 − 20/100 = 0.8'),('b','<i>V</i><sub>8</sub> = 0.8<sup>8</sup> × 9500 = 1593.835…'),('c','<i>V</i><sub>0</sub> − <i>V</i><sub>8</sub> = 9500 − 1593.84')],
  '',f'{CAM} · Example 25 (p. 369)',video='Cambridge GO · Example 25 (7E Resources)',cmd=('Calculate',None,'total depreciation = V₀ − Vₙ'),
  parts=[('a','<i>V<sub>n</sub></i> = 0.8<sup><i>n</i></sup> × 9500'),('b','<b>$1593.84</b>'),('c','<b>$7906.16</b>')]))
S.append(qslide('yt','You try · Edrolo 5C WE2b–c','Value and depreciation after reducing balance depreciation',
  '<div style="font-size:24px;margin-top:20px">A tablet is worth $550 and is depreciated using a reducing balance depreciation method with a rate of 4.3% per annum.<br>A recurrence relation is constructed to represent the depreciation of the tablet:<br>'+RR('550','0.957 × <i>V<sub>n</sub></i>')+'</div>'
  +plist([('b','After three years, what is the value of the tablet?'),('c','What is the amount of depreciation in the third year?')]),
  [('b','rule: <i>V</i><sub>3</sub> = 0.957<sup>3</sup> × 550 = 482.057…'),('c','<i>V</i><sub>2</sub> = 0.957<sup>2</sup> × 550 = 503.72 → 503.72 − 482.06')],
  '',f'{EDR} · 5C Worked example 2b–c (pp. 318–319); Edrolo works it by recursion, the rule gives the same values',cmd=('What is',None,'IN the third year = V₂ − V₃'),
  parts=[('b','<b>$482.06</b>'),('c','<b>$21.66</b>')]))
S.append(qslide('we','Worked example 26 · 7E','Using a calculator to find n',
  '<div style="font-size:30px;margin-top:60px">How many years will it take for an investment of $5000, paying compound interest at 6% per annum, to grow above $8000? Write your answer correct to the nearest year.</div>',
  [('Values','<i>V</i><sub>0</sub> = 5000 · <i>R</i> = 1.06 · <i>V<sub>n</sub></i> = 8000'),('Equation','8000 = 1.06<sup><i>n</i></sup> × 5000'),('CAS','solve(8000 = 1.06<sup><i>n</i></sup> × 5000, <i>n</i>) → <i>n</i> = 8.066…'),('Round UP','after 8 years only $7969.24: interest is paid at the END of the year')],
  'The investment grows above $8000 after <b>9 years</b>.',f'{CAM} · Example 26 (p. 370)',video='Cambridge GO · Example 26 (7E Resources)',cmd=('How many years',None,'solve, then round UP')))
w=WY['YT-7E-26']
S.append(qslide('yt','You try · written for 12MAG','Using a calculator to find n',
  f'<div style="font-size:30px;margin-top:60px">{w["text"]}</div>',
  [('Equation','12 000 = 1.05<sup><i>n</i></sup> × 8000'),('CAS','<i>n</i> = 8.310…'),('Round UP','after 8 years only $11 819.64')],
  'The investment grows above $12 000 after <b>9 years</b>.',f'Written for 12MAG (modelled on {CAM} Example 26): no matching Edrolo worked example',cmd=('How many years',None,'solve, then round UP')))
S.append(qslide('we','Worked example 27 · 7E','Using a calculator to find r',
  '<div style="font-size:28px;margin-top:50px">An industrial weaving company purchased a new loom at a cost of $56 000. It has an estimated value of $15 000 after 10 years of operation. If the value of the loom is depreciated using a reducing balance method, what is the annual rate of depreciation? Write your answer correct to one decimal place.</div>',
  [('Values','<i>V</i><sub>0</sub> = 56 000 · <i>V</i><sub>10</sub> = 15 000 · <i>R</i> = 1 − <i>r</i>/100'),('Equation','15 000 = (1 − <i>r</i>/100)<sup>10</sup> × 56 000'),('CAS','<i>r</i> = 12.342… or <i>r</i> = 187.66…'),('Choose','a rate over 100% makes no sense: keep 12.342…')],
  'The annual rate of depreciation is <b>12.3%</b>.',f'{CAM} · Example 27 (p. 370)',video='Cambridge GO · Example 27 (7E Resources)',cmd=('what is',None,'solve for r, keep the sensible one')))
w=WY['YT-7E-27']
S.append(qslide('yt','You try · written for 12MAG','Using a calculator to find r',
  f'<div style="font-size:28px;margin-top:50px">{w["text"]}</div>',
  [('Equation','9000 = (1 − <i>r</i>/100)<sup>8</sup> × 42 000'),('CAS','<i>r</i> = 17.515… (the other solution is over 100)')],
  'The annual rate of depreciation is <b>17.5%</b>.',f'Written for 12MAG (modelled on {CAM} Example 27): no matching Edrolo worked example',cmd=('what is',None,'solve for r')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['solve-n-r']
S.append(cas('CAS · 7E','Solving a geometric rule for n or r',
  '<p style="font-size:24px">How many years for $5000 at 6% p.a. compound interest to grow above $8000?</p><p style="font-size:28px;text-align:center">8000 = 1.06<sup><i>n</i></sup> × 5000</p>'
  '<p style="font-size:22px">For a rate, solve for <i>r</i> instead: 15 000 = (1 − <i>r</i>/100)<sup>10</sup> × 56 000.</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'<i>n</i> = 8.066… → round UP → <b>9 years</b> · <i>r</i> = 12.342… (not 187.66) → <b>12.3%</b>',
  f'{CAM} · Examples 26–27 (p. 370) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2020 Exam 1 Q29','Show what you know',
  '<div style="font-size:24px;margin-top:10px">The value of a van purchased for $45 000 is depreciated by <i>k</i>% per annum using the reducing balance method.<br>After three years of this depreciation, it is then depreciated in the fourth year under the unit cost method at the rate of 15 cents per kilometre.<br>The value of the van after it travels 30 000 km in this fourth year is $26 166.24.<br>The value of <i>k</i> is</div>',
  [('Undo unit cost','0.15 × 30 000 = 4500 → <i>V</i><sub>3</sub> = 26 166.24 + 4500 = 30 666.24'),('Equation','30 666.24 = (1 − <i>k</i>/100)<sup>3</sup> × 45 000'),('CAS','<i>k</i> = 12')],
  '<i>k</i> = <b>12</b>: <b>B</b>.',f'VCAA 2020 Further Mathematics Exam 1 Recursion and financial modelling Q29 (examiner report) · {EDR} 5D Q17',
  mc=['9','12','14','16','18'],key='B',dist=[14,54,14,11,7]))
S[-1]=S[-1].replace('<section class="slide T ex','<section class="slide T ex sm',1)
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2021 Exam 1 Q20','Show what you know',
  '<div style="font-size:28px;margin-top:40px">Sammy purchased a boat for $72 000.<br>The value of the boat is depreciated each year by 10% using the reducing balance method.<br>In the third year, the boat will depreciate in value by 10% of</div>',
  [('Third year','starts at the value after TWO years, <i>V</i><sub>2</sub>'),fx('V2','<i>V</i><sub>2</sub>',F('0.9<sup>2</sup> × ',V('V0','72 000')),'58 320')],
  '10% of <b>$58 320.00</b>: <b>C</b>.',f'VCAA 2021 Further Mathematics Exam 1 Recursion and financial modelling Q20 (examiner report) · {EDR} 5D Q18',
  mc=['$47 239.20','$52 488.00','$58 320.00','$64 800.00','$72 000.00'],key='C',dist=[3,40,44,9,4],dis=('B','$52 488 is the value at the END of the third year (<i>V</i><sub>3</sub>), not the start')))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2012 Exam 1 Q2','Show what you know',
  '<div style="font-size:30px;margin-top:60px">$3000 is invested at a simple interest rate of 6.5% per annum.<br>The total interest earned in three years is</div>',
  [fx('D','<i>D</i>',F(FR([V('r','6.5')],['100']),' × 3000'),'195'),('3 years','3 × 195 = 585')],
  'Total interest <b>$585.00</b>: <b>C</b>.',f'VCAA 2012 Further Mathematics Exam 1 Business-related mathematics Q2 (no examiner report on file: no %) · {EDR} 5E Q16',
  mc=['$195.00','$580.50','$585.00','$3623.85','$3585.00'],key='C',dis=('E','$3585 is the VALUE of the investment, not the interest earned')))

# ================= closing
S.append(checkin(SC_).replace('<ul class="tick">','<ul class="tick" style="columns:2;column-gap:36px">'))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 7 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('7C','7E') and v.get('url')]))
n=assemble(S,'12MAG · L33 · Explicit rules for linear and geometric growth and decay',os.path.join(ROOT,'lessons','7C-7E slides.html'))
print(n-1,'slides')
