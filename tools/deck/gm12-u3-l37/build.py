"""Lesson gm12-u3-l37 (8A Compound interest investments with regular additions) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/8A slides.html     Run: python3 tools/deck/gm12-u3-l37/build.py     Screenshots: python3 tools/deck/gm12-u3-l37/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- No CFAT this lesson (CFAT 2.8.1 sits at the start of l40).
- Do Now: VCAA 2026 Exam 1 Q17 (answer D) · VCAA 2026 Exam 1 Q2 (stem of Q1-2; IQR 14, B) · VCAA 2026 Exam 2 Q8a · VCAA 2026 Exam 2 Q1a
          (2026 examiner reports not yet published: no %).
- APK: Cambridge U1&2 Ch 3 skills checklist 3H #22 (skill; illustrated with Fred's $5000 at 4% from Cambridge U3&4 8A p. 393) ·
       VCAA 2017 Further Exam 2 Q5c (= Edrolo U1&2 3E Q12; report 58% full marks, answer 5.7%).
- Learn: Cambridge U3&4 8A pp. 392-396 (own words) · Edrolo U3&4 6F.
- Worked examples: Cambridge U3&4 Examples 1-5 (8A, pp. 392-396). Example 5 prints 1.005Vn / 1.012Vn (typo) - shown with An / Wn, noted on the slide.
  You trys (planner card): Ex 1, 2, 5 = written YT-8A-1, -2, -5 (planner/written-youtrys.json) · Ex 3 = Edrolo U3&4 6F WE1a (p. 405) · Ex 4 = 6F WE1b (pp. 405-406).
- CAS: planner/cas-skills.json 'recursion-sequence' (task = Cambridge Example 4c).
- Exits: VCAA 2018 Further Exam 1 Q17 + Q18 (Edrolo U3&4 6F Q16a-b; report Q17 79% D, 1/3/5/79/11; Q18 61% C, 5/17/61/11/5) ·
         VCAA 2021 Exam 1 Q22 (6F Q17; report 56% B, 5/56/10/23/5).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l37')
yid=lambda u:u.split('v=')[1].split('&')[0]
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
REFF='<i>r</i><sub>eff</sub> = ((1 + <i>r</i>/(100<i>n</i>))<sup><i>n</i></sup> − 1) × 100%'
def plot(vals,y0,y1,ystep,L='V',W=380,Hh=230,col='#1565C0'):
    l,b,t,r=66,30,12,14; pw=W-l-r; ph=Hh-b-t; nx=len(vals)
    X=lambda n:l+pw*(n+0.5)/nx; Y=lambda v:t+ph*(1-(v-y0)/(y1-y0))
    o=[f'<line x1="{l}" y1="{Y(y0)}" x2="{W-r}" y2="{Y(y0)}" stroke="#333" stroke-width="1.5"/>',f'<line x1="{l}" y1="{t}" x2="{l}" y2="{Y(y0)}" stroke="#333" stroke-width="1.5"/>']
    y=y0
    while y<=y1+1e-9:
        o.append(f'<line x1="{l}" y1="{Y(y)}" x2="{W-r}" y2="{Y(y)}" stroke="#ddd"/><text x="{l-6}" y="{Y(y)+5}" text-anchor="end" font-size="13">{y:,.10g}</text>'.replace(',',' '))
        y+=ystep
    for n,v in enumerate(vals):
        o.append(f'<text x="{X(n)}" y="{Y(y0)+18}" text-anchor="middle" font-size="13">{n}</text><circle cx="{X(n)}" cy="{Y(v)}" r="5.5" fill="{col}"/>')
    o.append(f'<text x="{W-r}" y="{Y(y0)+18}" font-size="14" font-style="italic" text-anchor="end">n</text><text x="{l+6}" y="{t+8}" font-size="14" font-style="italic">{L}ₙ</text>')
    return f'<svg viewBox="0 0 {W} {Hh}" width="{W}" style="max-width:100%;display:block;margin:4px auto;background:#fff;border-radius:8px">{"".join(o)}</svg>'

S=[]
S.append(title(37,'Compound interest investments with regular additions',f'{CAM} · 8A Combining linear and geometric growth or decay to model compound interest investments with additions to the principal','L37').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('8A Combining geometric and linear growth','',None),('Worked examples 1–3','→ You try',None),('8A Analysing annuity investments','',None),
  ('Worked examples 4–5','→ You try',None),('CAS: generating the sequence','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Annuity investment','a compound interest investment with regular, equal additions to the principal'),
  ('Regular addition, <i>D</i>','the amount added each period, straight after the interest is added'),
  ('Growth multiplier, <i>R</i>','grows the balance by the interest each period'),
  ('Periods per year, <i>p</i>','12 months · 4 quarters · 26 fortnights · 52 weeks · 365 days')],
  [('Recurrence relation',F(RR('the principal','<i>RV<sub>n</sub></i> + <i>D</i>')),'times <i>R</i> (interest), then add <i>D</i>'),
   ('Growth multiplier',F('<i>R</i> = 1 + <i>r</i>/(100 × <i>p</i>)'),'<i>r</i> = annual interest rate'),
   ('Annual rate from <i>R</i>',F('<i>r</i> = (<i>R</i> − 1) × 100 × <i>p</i>'),'rate per period × periods per year')],
  f'{CAM}, 8A pp. 392–396; Study Design: first-order linear recurrence relations u<sub><i>n</i>+1</sub> = Ru<sub><i>n</i></sub> + d; annuity investments'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2026 Exam 1 Q17','Review of 7F (last lesson)',
  '<div style="font-size:30px;margin-top:60px">Cassandra invests a sum of money in an account earning compound interest.<br>The nominal interest rate and the effective interest rate for the investment are both 3.95% per annum.<br><br>For Cassandra’s investment, the compounding period is</div>',
  [('Effective','the effective rate includes the extra interest from compounding during the year'),('Equal','nominal = effective only when interest is added ONCE a year')],
  'The compounding period is <b>annually</b>: <b>D</b>.','VCAA 2026 General Mathematics Exam 1 Q17 (2026 examiner report not yet published: no %)',
  mc=['daily.','weekly.','monthly.','annually.'],key='D'))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q2','Review of 1F (last term)',
  '<div style="font-size:19px">The stem plot below shows the points scored by a National Rugby League team in each of the 25 games it played in the 2025 season.</div>'
  '<div style="font-family:monospace;font-size:19px;line-height:1.35;margin:6px 0 6px 40px;white-space:pre">key: 1|6 = 16   n = 25\n0 | 8 8\n1 | 0 2 4 4 4 4\n1 | 5 6 6 8 8\n2 | 0 0 2\n2 | 6 6 6\n3 | 0 2 4\n3 | 6 6\n4 | 0</div>'
  '<div style="font-size:12px" class="muted">Data: Rugby League Tables &lt;afltables.com/rl/seas/2025.html&gt;</div><div style="font-size:21px">The interquartile range (IQR) of points scored is</div>',
  [('CAS','one-variable stats on the 25 values'),('Q₁, Q₃','Q₁ = 14 · Q₃ = 28'),fx('IQR','IQR',F(V('q3','28'),' − ',V('q1','14')),'14')],
  'IQR = <b>14</b>: <b>B</b>.','VCAA 2026 General Mathematics Exam 1 stem of Q1–2 and Q2 (2026 examiner report not yet published: no %)',
  mc=['12','14','16','20'],key='B'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 Exam 2 Q8a','Review of 7D (last week)',
  '<div style="font-size:26px;margin-top:30px">Hunter is a mobile mechanic. He bought a new van for $60 000 and will depreciate its value using the reducing balance method.<br>The value of the van, <i>V<sub>n</sub></i>, in dollars, after <i>n</i> years is modelled by the recurrence relation shown below.<br><br>'
  +RR('60 000','0.85<i>V<sub>n</sub></i>')+'<br><br>a. <b>Showing recursive calculations</b>, determine the value of the van, in dollars, after two years. <span class="muted">(1 mark)</span></div>',
  [('V1','<i>V</i><sub>1</sub> = 0.85 × 60 000 = 51 000'),('V2','<i>V</i><sub>2</sub> = 0.85 × 51 000 = 43 350')],
  'After two years the van is worth <b>$43 350</b>.','VCAA 2026 General Mathematics Exam 2 Q8 stem and Q8a (2026 examiner report not yet published: no %)',
  cmd=('Showing recursive calculations',1,'write V₁ then V₂')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q1a','Review of 1F (last term)',
  '<div style="font-size:19px">The happiness index for a country is a score ranging from 0 to 10. It represents the level of happiness for people in that country. A higher score represents happier people.<br>The happiness index scores for 12 countries in 2022 are given in the table below.</div>'
  '<table style="font-size:16px;margin:4px 0 4px 40px;border-collapse:collapse">'+''.join(f'<tr><td style="padding:0 30px 0 0">{c}</td><td>{v}</td></tr>' for c,v in [('Finland','7.82'),('Denmark','7.64'),('Iceland','7.56'),('Switzerland','7.51'),('Netherlands','7.42'),('Luxembourg','7.40'),('Sweden','7.38'),('Norway','7.37'),('Israel','7.36'),('New Zealand','7.20'),('Austria','7.16'),('Australia','7.16')])+'</table>'
  '<div style="font-size:19px">a. <b>Calculate</b> the range of the happiness index for the data in the table. <span class="muted">(1 mark)</span></div>',
  [('Max, min','max = 7.82 (Finland) · min = 7.16'),fx('Range','range',F(V('mx','7.82'),' − ',V('mn','7.16')),'0.66')],
  'range = <b>0.66</b>','VCAA 2026 General Mathematics Exam 2 Q1 stem and Q1a (2026 examiner report not yet published: no %)',
  cmd=('Calculate',1,'largest − smallest')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3H #22','Recurrence relation for compound interest',
  '<div style="font-size:30px;margin-top:50px">Use a recurrence relation to model compound interest for investments or loans.<br><br><span style="font-size:24px" class="muted">e.g. $5000 invested at 4% per annum, compounding annually (Cambridge U3&amp;4 8A, p. 393)</span></div>',
  [('V0','<i>V</i><sub>0</sub> = 5000'),fx('R','<i>R</i>',F('1 + ',FR([V('r','4')],['100 × 1'])),'1.04')],
  RR('5000','1.04<i>V<sub>n</sub></i>'),f'{CAM12} · Ch 3 skills checklist 3H #22 · example from {CAM} 8A p. 393',cmd=('Use',None,'V₀, then R')))
S.append(qslide('apk','APK · VCAA 2017 Exam 2 Q5c','Reading the rate from R',
  '<div style="font-size:28px;margin-top:40px">Alex is a mobile mechanic. He uses a van to travel to his customers to repair their cars.<br>The value of Alex’s van is depreciated using the reducing balance method of depreciation.<br>The value of the van, in dollars, after <i>n</i> years, <i>R<sub>n</sub></i>, can be modelled by the following recurrence relation.<br><br>'
  +RR('75 000','0.943<i>R<sub>n</sub></i>','R')+'<br><br>At what annual percentage rate is the value of the van depreciated each year? <span class="muted">(1 mark)</span></div>',
  [('R','<i>R</i> = 0.943 = 1 − 0.057'),('Rate','0.057 × 100 = 5.7%')],
  '<b>5.7%</b> per year',f'VCAA 2017 Further Mathematics Exam 2 Q5c (examiner report: average 0.6 / 1 = 58% full marks) · {EDR12} 3E Q12',
  stat=('mark',58),cmd=('At what annual percentage rate',None,'(1 − R) × 100')))

# ================= Learn 1
S.append(learn('Learn · 8A','Combining geometric and linear growth',
  '<h4>Multiply by <i>R</i>, then add (or subtract) <i>D</i></h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>'+RR('starting value','<i>R</i> × <i>V<sub>n</sub></i> ± <i>D</i>')+'</li><li>× <i>R</i> is geometric growth (interest); + <i>D</i> is linear growth (a regular addition)</li>'
  '<li>an <b>annuity investment</b> adds <i>D</i> every period: '+RR('the principal','<i>RV<sub>n</sub></i> + <i>D</i>')+'</li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">Fred: $5000 at 4% p.a., compounding yearly</span><br>'
  '<span class="frag">no additions: '+RR('5000','1.04<i>V<sub>n</sub></i>')+'</span><br>'
  '<span class="frag">plus $1000 a year: <b>'+RR('5000','1.04<i>V<sub>n</sub></i> + 1000')+'</b></span></div>',
  '<i>D</i> and <i>R</i> must use the SAME period: monthly additions need a monthly <i>R</i>.',f'{CAM}, 8A pp. 392–394 (own words) · {EDR}, 6F',
  cards=(kcard('Growth multiplier','<i>R</i> = 1 + <i>r</i>/(100<i>p</i>)','<i>p</i> = periods per year'),)))
S.append(qslide('we','Worked example 1 · 8A','Generating a sequence from a recurrence relation of the form V<sub><i>n</i>+1</sub> = R × V<sub><i>n</i></sub> ± D',
  '<div style="font-size:30px;margin-top:60px"><b>Write down</b> the first five terms of the sequence generated by the recurrence relation<br><br>'+RR('3','4<i>V<sub>n</sub></i> − 1')+'</div>',
  [('Start','3'),('Rule','× 4, then − 1'),('Terms','3 × 4 − 1 = 11 · 11 × 4 − 1 = 43 · 43 × 4 − 1 = 171 · 171 × 4 − 1 = 683')],
  'The first five terms are <b>3, 11, 43, 171, 683</b>.',f'{CAM} · Example 1 (p. 392)',video='Cambridge GO · Example 1 (8A Resources)',cmd=('Write down',None,'start value + four more')))
S.append(qslide('yt','You try · written for 12MAG (YT-8A-1)','Generating a sequence',
  '<div style="font-size:30px;margin-top:60px"><b>Write down</b> the first five terms of the sequence generated by the recurrence relation<br><br>'+RR('2','3<i>V<sub>n</sub></i> + 1')+'</div>',
  [('Start','2'),('Terms','2 × 3 + 1 = 7 · 7 × 3 + 1 = 22 · 22 × 3 + 1 = 67 · 67 × 3 + 1 = 202')],
  'The first five terms are <b>2, 7, 22, 67, 202</b>.','Written for 12MAG (modelled on Cambridge Example 1) · planner/written-youtrys.json',cmd=('Write down',None,'× 3, then + 1')))
S.append(qslide('we','Worked example 2 · 8A','Modelling compound interest investments with additions to the principal (1)',
  '<div style="font-size:28px;margin-top:40px">Fred has saved $5000 and invests this in a compound interest account paying 4% per annum, compounding yearly. He also adds an extra $1000 each year.<br><br><b>Model</b> this investment using a recurrence relation of the form<br>'+RR('the principal','<i>RV<sub>n</sub></i> + <i>D</i>')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 5000 and <i>D</i> = 1000'),fx('R','<i>R</i>',F('1 + ',FR([V('r','4')],['100 × 1'])),'1.04')],
  RR('5000','1.04<i>V<sub>n</sub></i> + 1000'),f'{CAM} · Example 2 (p. 393)',video='Cambridge GO · Example 2 (8A Resources)',cmd=('Model',None,'V₀, D, then R')))
S.append(qslide('yt','You try · written for 12MAG (YT-8A-2)','Modelling an investment with yearly additions',
  '<div style="font-size:28px;margin-top:40px">Maya has saved $4000 and invests this in a compound interest account paying 5% per annum, compounding yearly. She also adds an extra $800 each year.<br><br><b>Model</b> this investment using a recurrence relation of the form<br>'+RR('the principal','<i>RV<sub>n</sub></i> + <i>D</i>')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> years.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 4000 and <i>D</i> = 800'),fx('R','<i>R</i>',F('1 + ',FR([V('r','5')],['100'])),'1.05')],
  RR('4000','1.05<i>V<sub>n</sub></i> + 800'),'Written for 12MAG (modelled on Cambridge Example 2) · planner/written-youtrys.json',cmd=('Model',None,'V₀, D, then R')))
S.append(qslide('we','Worked example 3 · 8A','Modelling compound interest investments with additions to the principal (2)',
  '<div style="font-size:28px;margin-top:40px">Nor invests $1200 and plans to add an extra $50 each month. The account pays interest at a rate of 3% per annum, compounding monthly.<br><br><b>Model</b> this investment using a recurrence relation of the form<br>'+RR('the principal','<i>RV<sub>n</sub></i> + <i>D</i>')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> months.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 1200 and <i>D</i> = 50'),fx('R','<i>R</i>',F('1 + ',FR([V('r','3')],['100 × 12'])),'1.0025')],
  RR('1200','1.0025<i>V<sub>n</sub></i> + 50'),f'{CAM} · Example 3 (p. 394)',video='Cambridge GO · Example 3 (8A Resources)',cmd=('Model',None,'p = 12 for monthly')))
S.append(qslide('yt','You try · Edrolo 6F WE1a','Recurrence relation for an annuity investment',
  '<div style="font-size:28px;margin-top:50px">An annuity investment currently has a balance of $3600 and earns interest at a rate of 3.6% per annum, compounding monthly. The investor adds an additional $500 into the account at the end of each month.<br><br>a. <b>Construct</b> a recurrence relation that can be used to model the value of the investment, <i>V<sub>n</sub></i>, after <i>n</i> months.</div>',
  [('V0, d','<i>V</i><sub>0</sub> = 3600 · <i>d</i> = 500'),fx('R','<i>R</i>',F('1 + ',FR([V('r','3.6')],['12 × 100'])),'1.003')],
  RR('3600','1.003 × <i>V<sub>n</sub></i> + 500'),f'{EDR} · 6F Worked example 1a (p. 405)',cmd=('Construct',None,'p = 12 for monthly')))

# ================= Learn 2
S.append(learn('Learn · 8A','Analysing an annuity investment',
  '<h4>Apply the rule one period at a time</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li><i>V</i><sub>1</sub> = <i>R</i> × <i>V</i><sub>0</sub> + <i>D</i>, then <i>V</i><sub>2</sub> = <i>R</i> × <i>V</i><sub>1</sub> + <i>D</i>, …</li>'
  '<li>“after 3 extra payments” = after 3 periods = <i>V</i><sub>3</sub>; plot (<i>n</i>, <i>V<sub>n</sub></i>): a slight upward curve</li>'
  '<li>annual rate from <i>R</i>: rate per period = (<i>R</i> − 1) × 100, then × <i>p</i></li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">'+RR('400','1.005<i>V<sub>n</sub></i> + 30')+' (monthly)</span><br>'
  '<span class="frag"><i>V</i><sub>1</sub> = 432 · <i>V</i><sub>2</sub> = 464.16 · <i>V</i><sub>3</sub> = 496.48</span><br>'
  '<span class="frag"><i>R</i> = 1.005 → 0.5% per month → <b>6% per annum</b></span></div>',
  'Early additions earn interest for longer, so the investment grows faster.',f'{CAM}, 8A pp. 394–396 (own words) · {EDR}, 6F',
  cards=(kcard('Annual rate','<i>r</i> = (<i>R</i> − 1) × 100 × <i>p</i>'),)))
S.append(qslide('we','Worked example 4 · 8A','Using a recurrence relation to analyse compound interest investments with additions to the principal',
  '<div style="font-size:21px">Albert has an investment that can be modelled by the recurrence relation<br>'+RR('400','1.005<i>V<sub>n</sub></i> + 30')+'<br>where <i>V<sub>n</sub></i> is the value of the investment after <i>n</i> months.</div>'
  +plist([('a','State the value of the initial investment.'),('b','Determine the value of the investment after Albert has made three extra payments. Round your answer to the nearest cent.'),('c','What will be the value of his investment after 6 months? Round your answer to the nearest cent.'),('d','Plot the points for the value of the investment after 0, 1, 2 and 3 months on a graph.')]),
  [('a','<i>V</i><sub>0</sub> = 400'),('b','<i>V</i><sub>1</sub> = 1.005 × 400 + 30 = 432 · <i>V</i><sub>2</sub> = 464.16 · <i>V</i><sub>3</sub> = 496.48'),('c','CAS: 400, then × 1.005 + 30 six times: 528.96, 561.61, 594.42'),('d','plot (0, 400), (1, 432), (2, 464.16), (3, 496.48)')],
  '',f'{CAM} · Example 4 (p. 395)',video='Cambridge GO · Example 4 (8A Resources)',cmd=('Determine',None,'one period at a time'),
  parts=[('a','The initial investment was <b>$400</b>.'),('b','<b>$496.48</b>'),('c','<b>$594.42</b>'),('d',plot([400,432,464.16,496.48],0,500,100,W=360,Hh=200))]))
S.append(qslide('yt','You try · Edrolo 6F WE1b','Value after three months',
  '<div style="font-size:28px;margin-top:50px">An annuity investment currently has a balance of $3600 and earns interest at a rate of 3.6% per annum, compounding monthly. The investor adds an additional $500 into the account at the end of each month.<br><span class="muted" style="font-size:22px">(Part a: '+RR('3600','1.003 × <i>V<sub>n</sub></i> + 500')+')</span><br><br>b. How much will the account be worth after three months?</div>',
  [('V1','1.003 × 3600 + 500 = 4110.80'),('V2','1.003 × 4110.80 + 500 = 4623.132…'),('V3','1.003 × 4623.132… + 500 = 5137.001…')],
  'The account will be worth <b>$5137.00</b>.',f'{EDR} · 6F Worked example 1b (pp. 405–406)',cmd=('How much',None,'three periods')))
S.append(qslide('we','Worked example 5 · 8A','Determining the annual interest rate from a recurrence relation',
  '<div style="font-size:24px"><b>Determine</b> the annual interest rates for each of the following investments.</div>'
  +plist([('a','Consider an investment given by the recurrence relation '+RR('400','1.005<i>A<sub>n</sub></i> + 30','A')+' where <i>A<sub>n</sub></i> is the value of the investment after <i>n</i> months.'),('b','Consider an investment given by the recurrence relation '+RR('2000','1.012<i>W<sub>n</sub></i> + 500','W')+' where <i>W<sub>n</sub></i> is the value of the investment after <i>n</i> quarters.')]),
  [('a','solve 1.005 = 1 + <i>r</i>/(100 × 12)'),('b','solve 1.012 = 1 + <i>r</i>/(100 × 4)')],
  '',f'{CAM} · Example 5 (p. 396; the book prints “1.005<i>V<sub>n</sub></i>”, “1.012<i>V<sub>n</sub></i>”: corrected to <i>A<sub>n</sub></i>, <i>W<sub>n</sub></i>)',video='Cambridge GO · Example 5 (8A Resources)',cmd=('Determine',None,'p = 12 months, p = 4 quarters'),
  parts=[('a','<i>r</i> = 6: the annual interest rate is <b>6%</b>.'),('b','<i>r</i> = 4.8: the annual interest rate is <b>4.8%</b>.')]))
S.append(qslide('yt','You try · written for 12MAG (YT-8A-5)','Annual rate from a recurrence relation',
  '<div style="font-size:24px"><b>Determine</b> the annual interest rates for each of the following investments.</div>'
  +plist([('a','Consider an investment given by the recurrence relation '+RR('600','1.004<i>A<sub>n</sub></i> + 40','A')+' where <i>A<sub>n</sub></i> is the value of the investment after <i>n</i> months.'),('b','Consider an investment given by the recurrence relation '+RR('3000','1.015<i>W<sub>n</sub></i> + 200','W')+' where <i>W<sub>n</sub></i> is the value of the investment after <i>n</i> quarters.')]),
  [('a','0.4% per month × 12'),('b','1.5% per quarter × 4')],
  '','Written for 12MAG (modelled on Cambridge Example 5) · planner/written-youtrys.json',cmd=('Determine',None,'rate per period × p'),
  parts=[('a','<b>4.8%</b> per annum'),('b','<b>6%</b> per annum')]))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['recursion-sequence']
S.append(cas('CAS · 8A','Generating the sequence',
  '<p style="font-size:24px">Albert: '+RR('400','1.005<i>V<sub>n</sub></i> + 30')+'. Find the value after 6 months.</p><p style="font-size:28px;text-align:center">400 ↵ &nbsp; × 1.005 + 30 ↵ ↵ ↵ ↵ ↵ ↵</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'<i>V</i><sub>6</sub> = <b>$594.42</b>',
  f'{CAM} · Example 4c (p. 395) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
EX1='<div style="font-size:24px">The value of an annuity investment, in dollars, after <i>n</i> years, <i>V<sub>n</sub></i>, can be modelled by the recurrence relation shown below.<br><br>'+RR('46 000','1.0034 × <i>V<sub>n</sub></i> + 500')+'<br><br>'
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2018 Exam 1 Q17','Show what you know',
  EX1+'What is the value of the regular payment added to the principal of this annuity investment?</div>',
  [('Form','<i>V</i><sub><i>n</i>+1</sub> = <i>R</i> × <i>V<sub>n</sub></i> + <i>D</i>'),('D','the number added: 500')],
  '<b>$500.00</b>: <b>D</b>.',f'VCAA 2018 Further Mathematics Exam 1 Recursion and financial modelling Q17 (examiner report) · {EDR} 6F Q16a',
  mc=['$34.00','$156.40','$466.00','$500.00','$656.40'],key='D',dist=[1,3,5,79,11],dis=('E','$656.40 is the first year’s interest PLUS the payment, not the payment')))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2018 Exam 1 Q18','Show what you know',
  EX1+'Between the second and third years, the increase in the value of this investment is closest to</div>',
  [('V1, V2','<i>V</i><sub>1</sub> = 46 656.40 · <i>V</i><sub>2</sub> = 47 315.03'),('V3','<i>V</i><sub>3</sub> = 1.0034 × 47 315.03 + 500 = 47 975.90'),('Increase','47 975.90 − 47 315.03 = 660.87')],
  'Increase ≈ <b>$661</b>: <b>C</b>.',f'VCAA 2018 Further Mathematics Exam 1 Recursion and financial modelling Q18 (examiner report) · {EDR} 6F Q16b',
  mc=['$656','$658','$661','$1315','$1975'],key='C',dist=[5,17,61,11,5],dis=('B','$658 is the increase between years 1 and 2, one year too early')))
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2021 Exam 1 Q22','Show what you know',
  '<div style="font-size:26px;margin-top:30px">Joanna deposited $12 000 in an investment account earning interest at the rate of 2.8% per annum, compounding monthly.<br>She would like this account to reach a balance of $25 000 after five years.<br>To achieve this balance, she will make an extra payment into the account each month, immediately after the interest is calculated.<br><br>The minimum value of this payment is closest to</div>',
  [('Model',RR('12 000','(1 + 2.8/1200)<i>V<sub>n</sub></i> + <i>D</i>')+', 60 months'),('Solve','find <i>D</i> so that <i>V</i><sub>60</sub> = 25 000 (CAS, or try each option)'),('D','<i>D</i> = 174.106…')],
  '<b>$174.11</b>: <b>B</b>.',f'VCAA 2021 Exam 1 Recursion and financial modelling Q22 (examiner report) · {EDR} 6F Q17',
  mc=['$113.85','$174.11','$580.16','$603.22','$615.47'],key='B',dist=[5,56,10,23,5]))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8A' and v.get('url')]))
n=assemble(S,'12MAG · L37 · Compound interest investments with regular additions',os.path.join(ROOT,'lessons','8A slides.html'))
print(n-1,'slides')
