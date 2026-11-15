"""Lesson gm12-u3-l34 (7F Interest rates over different time periods and effective interest rates) slides,
built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/7F slides.html     Run: python3 tools/deck/gm12-u3-l34/build.py     Screenshots: python3 tools/deck/gm12-u3-l34/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- No CFAT this lesson (CFAT 2.7.2 sits at the start of l36).
- Do Now: VCAA 2023 Exam 1 Q18 (stem of Q18-19; report 60% C, 33/2/60/4/1) ·
          VCAA 2025 NHT Exam 1 Q21 (scanned paper read from the page image; answer A; NHT report gives no %) ·
          VCAA 2024 Exam 2 Q5a (scanned paper read from the page image; stem of Q5; report avg 0.9/1 = 90%) ·
          VCAA 2026 Exam 2 Q8c (stem of Q8; 2026 report not out yet: no %).
- APK: Cambridge U1&2 Ch 3 skills checklist 3H #23 (solution worked for 12MAG) ·
       VCAA 2020 Further Exam 1 Q26 (= Edrolo U1&2 3F Q14; report 20% E, 5/18/6/51/20).
- Learn: Cambridge U3&4 7F pp. 373-377 (own words) · Edrolo U3&4 5F, 5G.
- Worked examples: Cambridge U3&4 Examples 28-32 (7F, pp. 373-377).
  You trys (planner card): Ex 28 = Edrolo U1&2 3E WE3a (p. 157ff) · Ex 29 = Edrolo U3&4 5F WE1a (p. 339) · Ex 30 = 5F WE1b-c (pp. 339-340) ·
  Ex 31 = Edrolo U3&4 5G WE2 (pp. 348-349) · Ex 32 = 5G WE1 (pp. 347-348).
- CAS: planner/cas-skills.json 'effective-rate' (task = Cambridge Example 32).
- Exits: VCAA 2020 Further Exam 1 Q24 (Edrolo U3&4 5F Q17; report 80% D, 3/8/5/80/3) ·
         VCAA 2020 Further Exam 1 Q28 (5G Q11; report 58% C, 13/5/58/9/14) ·
         VCAA 2017 Further Exam 2 Q6 (5F Q18; report a 61%, b 39% full marks, c 26%).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l34')
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
S.append(title(34,'Interest rates over different time periods and effective interest rates',f'{CAM} · 7F Interest rates over different time periods and effective interest rates','L34').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('7F Interest rate conversions','',None),('Worked examples 28–30','→ You try',None),('7F Effective interest rates','',None),
  ('Worked examples 31–32','→ You try',None),('CAS: effective interest rate','',None),('Exit tasks','· three VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Nominal interest rate','the quoted annual rate (per annum)'),
  ('Compounding period','how often interest is calculated and added: yearly, quarterly, monthly, fortnightly, weekly, daily'),
  ('Periods per year','12 months · 4 quarters · 26 fortnights · 52 weeks · 365 days'),
  ('Effective interest rate','the actual % the value grows in ONE year once compounding is included'),
  ('Comparing','loan: choose the LOWER effective rate · investment: choose the HIGHER')],
  [('Rate per period',F('<i>r</i> ÷ <i>p</i>'),'<i>p</i> = compounding periods per year'),
   ('Growth multiplier',F('<i>R</i> = 1 + <i>r</i>/(100 × <i>p</i>)'),'<i>n</i> then counts periods, not years'),
   ('Effective rate',F(REFF),'here <i>n</i> = compounding periods per year (VCAA formula sheet)')],
  f'{CAM}, 7F pp. 373–377; Study Design: nominal and effective interest rates, compound interest with different compounding periods'))

# ================= Do Now (retrieval)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q18','Review of 7C (last lesson)',
  '<div style="font-size:21px">Gus purchases a coffee machine for $15 000 and depreciates its value using the unit cost method.<br>The rate of depreciation is $0.04 per cup of coffee made.<br>A recurrence relation that models the year-to-year value <i>G<sub>n</sub></i>, in dollars, of the machine is<br><br>'
  +RR('15000','<i>G<sub>n</sub></i> − 1314','G')+'<br><br>A rule for <i>G<sub>n</sub></i>, the value of the machine after <i>n</i> years is</div>',
  [('V0','<i>G</i><sub>0</sub> = 15 000'),('D','the recurrence relation drops 1314 each YEAR'),('Rule','<i>G<sub>n</sub></i> = <i>G</i><sub>0</sub> − <i>nD</i>')],
  '<i>G<sub>n</sub></i> = <b>15 000 − 1314<i>n</i></b>: <b>C</b>.','VCAA 2023 General Mathematics Exam 1 Q18–19 stem and Q18 (examiner report)',
  mc=['<i>G<sub>n</sub></i> = 15 000 − 0.04<i>n</i>','<i>G<sub>n</sub></i> = 15 000 + 0.04<i>n</i>','<i>G<sub>n</sub></i> = 15 000 − 1314<i>n</i>','<i>G<sub>n</sub></i> = 1314 − 0.04<i>n</i>','<i>G<sub>n</sub></i> = 1314 + 0.04<i>n</i>'],key='C',dist=[33,2,60,4,1],
  dis=('A','0.04 is per CUP; <i>n</i> counts YEARS, so use the yearly drop of 1314')))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2025 NHT Exam 1 Q21','Review of 7E (last lesson)',
  '<div style="font-size:30px;margin-top:60px">Nina invests $2000 at 9.25% per annum compounding annually.<br><br>After how many years will Nina’s investment first be more than double its initial value?</div>',
  [('Equation','4000 = 1.0925<sup><i>n</i></sup> × 2000'),('CAS','<i>n</i> = 7.83…'),('Round UP','interest is added at the END of each year')],
  'After <b>8 years</b>: <b>A</b>.','VCAA 2025 (NHT) General Mathematics Exam 1 Q21 (NHT examiner report gives no % statistics)',
  mc=['8 years','9 years','10 years','11 years'],key='A'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q5a','Review of 7C (last lesson)',
  '<div style="font-size:26px;margin-top:30px">Emi operates a mobile dog-grooming business.<br>The value of her grooming equipment will depreciate.<br>Based on average usage, a rule for the value, in dollars, of the equipment, <i>V<sub>n</sub></i>, after <i>n</i> weeks is<br><br>'
  '<i>V<sub>n</sub></i> = 15 000 − 60<i>n</i><br><br>Assume that there are exactly 52 weeks in a year.<br>a. By what amount, in dollars, does the value of the grooming equipment depreciate each week? <span class="muted">(1 mark)</span></div>',
  [('Rule','<i>V<sub>n</sub></i> = <i>V</i><sub>0</sub> − <i>nD</i>: <i>D</i> is the number with <i>n</i>'),('n','<i>n</i> counts weeks, so <i>D</i> is per week')],
  '<b>$60</b> each week','VCAA 2024 General Mathematics Exam 2 Q5 stem and Q5a (examiner report: average 0.9 / 1 = 90%)',
  stat=('mark',90),cmd=('By what amount',1,'D = the coefficient of n')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q8c','Review of 7E (last lesson)',
  '<div style="font-size:26px;margin-top:30px">Hunter is a mobile mechanic. He bought a new van for $60 000 and will depreciate its value using the reducing balance method.<br>The value of the van, <i>V<sub>n</sub></i>, in dollars, after <i>n</i> years is modelled by the recurrence relation shown below.<br><br>'
  +RR('60 000','0.85<i>V<sub>n</sub></i>')+'<br><br>c. The value of the van, <i>V<sub>n</sub></i>, in dollars, after <i>n</i> years can also be modelled by a rule.<br><b>Write</b> the rule for <i>V<sub>n</sub></i> in terms of <i>n</i>. <span class="muted">(1 mark)</span></div>',
  [('Read off','<i>V</i><sub>0</sub> = 60 000 · <i>R</i> = 0.85'),('Rule','<i>V<sub>n</sub></i> = <i>R<sup>n</sup></i> × <i>V</i><sub>0</sub>')],
  '<i>V<sub>n</sub></i> = <b>0.85<sup><i>n</i></sup> × 60 000</b>','VCAA 2026 General Mathematics Exam 2 Q8 stem and Q8c (2026 examiner report not yet published: no %)',
  cmd=('Write',1,'R to the power n, times V₀')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3H #23','Recurrence relation for a loan with a different compounding period',
  '<div style="font-size:30px;margin-top:50px">Jack borrows $2000. He will pay interest at the rate of 4.2% per annum. Write down a recurrence relation to model the value of Jack’s loan if interest is compounded quarterly.</div>',
  [('Per quarter','4.2 ÷ 4 = 1.05% per quarter'),fx('R','<i>R</i>',F('1 + ',FR([V('r','1.05')],['100'])),'1.0105')],
  RR('2000','1.0105<i>V<sub>n</sub></i>')+' (<i>n</i> in quarters)',f'{CAM12} · Ch 3 skills checklist 3H #23 · solution worked for 12MAG',cmd=('Write down',None,'rate per quarter, then R')))
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q26','A rule when interest compounds quarterly',
  '<div style="font-size:28px;margin-top:40px">Ray deposited $5000 in an investment account earning interest at the rate of 3% per annum, compounding quarterly.<br><br>A rule for the balance, <i>R<sub>n</sub></i>, in dollars, after <i>n</i> years is given by</div>',
  [('Per quarter','3 ÷ 4 = 0.75% → <i>R</i> = 1.0075'),('n is YEARS','4 quarters every year: 4<i>n</i> compounding periods')],
  '<i>R<sub>n</sub></i> = <b>5000 × 1.0075<sup>4<i>n</i></sup></b>: <b>E</b>.',f'VCAA 2020 Further Mathematics Exam 1 Recursion and financial modelling Q26 (examiner report) · {EDR12} 3F Q14',
  mc=['<i>R<sub>n</sub></i> = 5000 × 0.03<sup><i>n</i></sup>','<i>R<sub>n</sub></i> = 5000 × 1.03<sup><i>n</i></sup>','<i>R<sub>n</sub></i> = 5000 × 0.03<sup>4<i>n</i></sup>','<i>R<sub>n</sub></i> = 5000 × 1.0075<sup><i>n</i></sup>','<i>R<sub>n</sub></i> = 5000 × 1.0075<sup>4<i>n</i></sup>'],key='E',dist=[5,18,6,51,20],
  dis=('D','1.0075 is right, but <i>n</i> counts YEARS: the power must be the number of QUARTERS, 4<i>n</i>')))

# ================= 7F Learn: conversions
S.append(learn('Learn · 7F','Converting a nominal rate to a rate per compounding period',
  '<h4>Divide the annual rate by the number of periods in a year</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>banks quote an annual (nominal) rate, but may add interest monthly, quarterly, …</li><li>rate per period = <i>r</i> ÷ <i>p</i>: <i>p</i> = 12, 4, 26, 52 or 365</li>'
  '<li><i>R</i> = 1 + <i>r</i>/(100 × <i>p</i>), and <i>n</i> now counts periods (months, quarters, …)</li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">$5000 loan at 4.5% p.a.</span><br>'
  '<span class="frag">yearly: <i>R</i> = 1.045 · quarterly: <i>R</i> = 1 + 4.5/400 = 1.011 25</span><br>'
  '<span class="frag">monthly: <i>R</i> = 1 + 4.5/1200 = 1.003 75 → <b>'+RR('5000','1.00375<i>V<sub>n</sub></i>')+'</b></span></div>',
  'Say what <i>n</i> counts: “after <i>n</i> months” needs <i>n</i> = 48 for 4 years.',f'{CAM}, 7F pp. 373–374 (own words) · {EDR}, 5F',
  cards=(kcard('Growth multiplier','<i>R</i> = 1 + <i>r</i>/(100<i>p</i>)','<i>p</i> = periods per year'),)))
S.append(qslide('we','Worked example 28 · 7F','Converting nominal interest rates to compounding period interest rates',
  '<div style="font-size:28px;margin-top:30px">An investment account will pay interest at the rate of 4.68% per annum. Convert this interest rate to each of the following rates:</div>'
  +plist([('a','monthly'),('b','fortnightly'),('c','quarterly')]),
  [('a','divide by <i>p</i> = 12'),('b','divide by <i>p</i> = 26'),('c','divide by <i>p</i> = 4')],
  '',f'{CAM} · Example 28 (p. 373)',video='Cambridge GO · Example 28 (7F Resources)',cmd=('Convert',None,'÷ periods per year'),
  parts=[('a','4.68 ÷ 12 = <b>0.39%</b> per month'),('b','4.68 ÷ 26 = <b>0.18%</b> per fortnight'),('c','4.68 ÷ 4 = <b>1.17%</b> per quarter')]))
S.append(qslide('yt','You try · Edrolo U1&amp;2 3E WE3a','Interest rate per compounding period',
  '<div style="font-size:30px;margin-top:60px">Tully invests $5000 in a savings account that earns interest at a rate of 4.6% p.a., compounding monthly.<br><br>a. <b>Calculate</b> the interest rate, as a percentage, per compounding period. Round to two decimal places.</div>',
  [('p','compounding monthly: 12 periods'),fx('r','<i>r</i>','4.6 ÷ 12','0.38…')],
  '<b>0.38%</b> per compounding period',f'{EDR12} · 3E Worked example 3a',cmd=('Calculate',None,'÷ 12 for monthly')))
S.append(qslide('we','Worked example 29 · 7F','Recurrence relations with different compounding periods',
  '<div style="font-size:24px">Brian borrows $5000 from a bank. He will pay interest at the rate of 4.5% per annum.<br>Let <i>V<sub>n</sub></i> be the value of the loan after <i>n</i> compounding periods.<br><b>Write down</b> a recurrence relation to model the value of Brian’s loan if interest is compounded:</div>'
  +plist([('a','yearly'),('b','quarterly'),('c','monthly')]),
  [('a','<i>p</i> = 1: <i>R</i> = 1 + 4.5/(100 × 1) = 1.045 · <i>n</i> in years'),('b','<i>p</i> = 4: <i>R</i> = 1 + 4.5/(100 × 4) = 1.011 25 · <i>n</i> in quarters'),('c','<i>p</i> = 12: <i>R</i> = 1 + 4.5/(100 × 12) = 1.003 75 · <i>n</i> in months')],
  '',f'{CAM} · Example 29 (p. 374)',video='Cambridge GO · Example 29 (7F Resources)',cmd=('Write down',None,'R = 1 + r/(100p)'),
  parts=[('a',RR('5000','1.045<i>V<sub>n</sub></i>')),('b',RR('5000','1.01125<i>V<sub>n</sub></i>')),('c',RR('5000','1.00375<i>V<sub>n</sub></i>'))]))
S.append(qslide('yt','You try · Edrolo 5F WE1a','Recurrence relation for fortnightly compounding',
  '<div style="font-size:28px;margin-top:50px">Duncan has an investment of $10 000 that is earning interest at a rate of 8% per annum, compounding fortnightly.<br><br>a. <b>Construct</b> a recurrence relation that can be used to calculate value of the investment, <i>V<sub>n</sub></i>, after <i>n</i> fortnights.<br><span style="font-size:22px">Round to three decimal places where necessary.</span></div>',
  [('Per fortnight','8 ÷ 26 = 0.307…%'),fx('R','<i>R</i>',F('1 + ',FR([V('r','0.307…')],['100'])),'1.003')],
  RR('10 000','1.003 × <i>V<sub>n</sub></i>'),f'{EDR} · 5F Worked example 1a (p. 339)',cmd=('Construct',None,'÷ 26 for fortnightly')))
S.append(qslide('we','Worked example 30 · 7F','Modelling an investment that compounds monthly using recurrence relations',
  '<div style="font-size:23px">A principal value of $10 000 is invested in an account earning compound interest monthly at the rate of 9% per annum.<br>Let <i>V<sub>n</sub></i> be the value of the investment after <i>n</i> months.</div>'
  +plist([('a','Calculate the growth multiplier, <i>R</i>.'),('b','Write down a recurrence relation for the value of the investment after <i>n</i> months.'),('c','Write down a rule for the value of the investment after <i>n</i> months.'),('d','Use this rule to find the value of the investment after 4 years.')]),
  [('a','monthly: <i>p</i> = 12 → <i>R</i> = 1 + 9/(100 × 12)'),('b','<i>V</i><sub>0</sub> = 10 000 and <i>R</i>'),('c','<i>V<sub>n</sub></i> = <i>R<sup>n</sup></i> × <i>V</i><sub>0</sub>'),('d','4 years = 48 months: <i>V</i><sub>48</sub> = 1.0075<sup>48</sup> × 10 000')],
  '',f'{CAM} · Example 30 (p. 375)',video='Cambridge GO · Example 30 (7F Resources)',cmd=('Use',None,'d: n = 48 months'),
  parts=[('a','<i>R</i> = <b>1.0075</b>'),('b',RR('10 000','1.0075<i>V<sub>n</sub></i>')),('c','<i>V<sub>n</sub></i> = 1.0075<sup><i>n</i></sup> × 10 000'),('d','<b>$14 314.05</b>')]))
S.append(qslide('yt','You try · Edrolo 5F WE1b–c','Using the recurrence relation step by step',
  '<div style="font-size:22px">Duncan has an investment of $10 000 that is earning interest at a rate of 8% per annum, compounding fortnightly.<br><span class="muted">(Part a: '+RR('10 000','1.003 × <i>V<sub>n</sub></i>')+')</span></div>'
  +plist([('b','Calculate the value of Duncan’s investment after 4 fortnights.'),('c','Plot the value of the investment for the first four fortnights on the set of axes shown.')])
  +plot([10000]*5,10000,10150,50,W=320,Hh=170,col='transparent'),
  [('b','<i>V</i><sub>1</sub> = 10 030 · <i>V</i><sub>2</sub> = 10 060.09 · <i>V</i><sub>3</sub> = 10 090.27… · <i>V</i><sub>4</sub> = 10 120.54…'),('c','plot (0, 10 000), (1, 10 030), (2, 10 060.09), (3, 10 090.27), (4, 10 120.54)')],
  '',f'{EDR} · 5F Worked example 1b–c (pp. 339–340)',cmd=('Calculate',None,'× 1.003 four times'),
  parts=[('b','<b>$10 120.54</b>'),('c',plot([10000,10030,10060.09,10090.27,10120.54],10000,10150,50,W=360,Hh=200))]))

# ================= 7F Learn: effective rates
S.append(learn('Learn · 7F','Effective interest rates',
  '<h4>Compare loans and investments by the interest earned in ONE year</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>effective rate = interest in one year ÷ principal × 100%</li><li>'+REFF+' (<i>n</i> = periods per year)</li>'
  '<li>more compounding periods → higher effective rate · loan: pick the LOWEST · investment: pick the HIGHEST</li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">$5000 at 4.8% p.a.</span><br>'
  '<span class="frag">quarterly: value after 1 year $5244.35 → 244.35 ÷ 5000 = <b>4.89%</b></span><br>'
  '<span class="frag">monthly: value after 1 year $5245.35 → 245.35 ÷ 5000 = <b>4.91%</b></span></div>',
  'The nominal rate is the same; the effective rate shows which one really pays more.',f'{CAM}, 7F pp. 375–376 (own words) · {EDR}, 5G',
  cards=(kcard('Effective rate',REFF),)))
S.append(qslide('we','Worked example 31 · 7F','Comparing loans and investments with effective interest rates',
  '<div style="font-size:24px">Brooke would like to borrow $20 000 that she will repay entirely after one year. She is deciding between two loan options:<br>&nbsp;&nbsp;option A: 5.95% per annum, compounding weekly<br>&nbsp;&nbsp;option B: 6% per annum, compounding quarterly.</div>'
  +plist([('a','Calculate the effective interest rate for each investment.'),('b','Which investment option is the best and why?')]),
  [('a','A: <i>r</i> = 5.95, <i>n</i> = 52 → ((1 + 5.95/5200)<sup>52</sup> − 1) × 100% · B: <i>r</i> = 6, <i>n</i> = 4 → ((1 + 6/400)<sup>4</sup> − 1) × 100%'),('b','a LOAN: the lower effective rate costs less')],
  '',f'{CAM} · Example 31 (p. 376)',video='Cambridge GO · Example 31 (7F Resources)',cmd=('Calculate',None,'then compare: loan → lowest'),
  parts=[('a','A: <b>6.13%</b> · B: <b>6.14%</b>'),('b','<b>Option A</b>: it has the lower effective rate, so Brooke pays less interest')]))
S.append(qslide('yt','You try · Edrolo 5G WE2','Choosing an investment by effective rate',
  '<div style="font-size:28px;margin-top:40px">Pete is saving up money for schoolies and is considering investing his savings into either of two accounts with the following interest rates:<br>• Superior Saver: 4.5% per annum, compounding quarterly<br>• Supreme Saver: 4.4% per annum, compounding weekly<br><br>Which account should Pete choose?</div>',
  [('Superior','<i>r</i> = 4.5, <i>n</i> = 4 → <i>r</i><sub>eff</sub> = 4.5765…%'),('Supreme','<i>r</i> = 4.4, <i>n</i> = 52 → <i>r</i><sub>eff</sub> = 4.4962…%'),('Compare','an INVESTMENT: pick the higher effective rate')],
  'Pete should choose <b>Superior Saver</b> (higher effective rate).',f'{EDR} · 5G Worked example 2 (pp. 348–349)',cmd=('Which',None,'investment → highest')))
S.append(qslide('we','Worked example 32 · 7F','Calculating effective interest rates using a CAS calculator',
  '<div style="font-size:30px;margin-top:60px">Marissa has $10 000 to invest. She chooses an account that will earn compounding interest at the rate of 4.5% per annum, compounding monthly.<br><br><b>Use</b> a CAS calculator to find the effective interest rate for this investment, correct to three decimal places.</div>',
  [('Values','nominal rate 4.5 · 12 compounding periods per year'),('TI-Nspire','eff(4.5, 12)'),('ClassPad','convEff: 12, 4.5')],
  'The effective interest rate is <b>4.594%</b>.',f'{CAM} · Example 32 (p. 377)',video='Cambridge GO · Example 32 (7F Resources)',cmd=('Use',None,'eff(rate, periods per year)')))
S.append(qslide('yt','You try · Edrolo 5G WE1','Converting to an effective interest rate',
  '<div style="font-size:30px;margin-top:60px"><b>Convert</b> an interest rate of 12.7% per annum, compounding monthly, to an effective interest rate, correct to two decimal places.</div>',
  [('Values','<i>r</i> = 12.7, <i>n</i> = 12'),('By hand','((1 + 12.7/1200)<sup>12</sup> − 1) × 100 = 13.465…'),('CAS','eff(12.7, 12)')],
  'The effective interest rate is <b>13.47%</b>.',f'{EDR} · 5G Worked example 1 (pp. 347–348)',cmd=('Convert',None,'by hand or eff( )')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['effective-rate']
S.append(cas('CAS · 7F','Effective interest rate',
  '<p style="font-size:24px">Marissa invests at 4.5% per annum, compounding monthly. Find the effective interest rate, correct to three decimal places.</p><p style="font-size:28px;text-align:center">eff(4.5, 12)</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'Effective interest rate = <b>4.594%</b>',
  f'{CAM} · Example 32 (p. 377) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 3 · VCAA 2020 Exam 1 Q24','Show what you know',
  '<div style="font-size:22px">Manu invests $3000 in an account that pays interest compounding monthly.<br>The balance of his investment after <i>n</i> months, <i>B<sub>n</sub></i>, can be determined using the recurrence relation<br><br>'
  +RR('3000','1.0048 × <i>B<sub>n</sub></i>','B')+'<br><br>The total interest earned by Manu’s investment after the first five months is closest to</div>',
  [fx('B5','<i>B</i><sub>5</sub>',F('1.0048<sup>5</sup> × ',V('V0','3000')),'3072.69'),('Interest','3072.69 − 3000 = 72.69')],
  'Total interest <b>$72.69</b>: <b>D</b>.',f'VCAA 2020 Further Mathematics Exam 1 Recursion and financial modelling Q24 (examiner report) · {EDR} 5F Q17',
  mc=['$57.60','$58.02','$72.00','$72.69','$87.44'],key='D',dist=[3,8,5,80,3],dis=('C','$72.00 is 5 × 0.48% × 3000: simple interest, no compounding')))
S.append(qslide('ex','Exit task 2 of 3 · VCAA 2020 Exam 1 Q28','Show what you know',
  '<div style="font-size:24px">The nominal interest rate for a loan is 8% per annum.<br>When rounded to two decimal places, the effective interest rate for this loan is <b>not</b></div>',
  [('Check each','eff(8, 365) = 8.33 · eff(8, 52) = 8.32 · eff(8, 26) = 8.315… → 8.32 · eff(8, 12) = 8.30 · eff(8, 4) = 8.24'),('Odd one out','fortnightly rounds to 8.32%, not 8.31%')],
  '<b>C</b>: fortnightly gives 8.32%, not 8.31%.',f'VCAA 2020 Further Mathematics Exam 1 Recursion and financial modelling Q28 (examiner report) · {EDR} 5G Q11',
  mc=['8.33% per annum when interest is charged daily.','8.32% per annum when interest is charged weekly.','8.31% per annum when interest is charged fortnightly.','8.30% per annum when interest is charged monthly.','8.24% per annum when interest is charged quarterly.'],key='C',dist=[13,5,58,9,14]))
S[-1]=S[-1].replace('<section class="slide T ex','<section id="x2" class="slide T ex sm',1).replace('</section>','<style>#x2 .mc>div{font-size:18px!important;padding-right:52px!important}</style></section>')
S.append(qslide('ex','Exit task 3 of 3 · VCAA 2017 Exam 2 Q6','Show what you know',
  '<div style="font-size:17px">Alex sends a bill to his customers after repairs are completed.<br>If a customer does not pay the bill by the due date, interest is charged.<br>Alex charges interest after the due date at the rate of 1.5% per month on the amount of an unpaid bill.<br>The interest on this amount will compound monthly.</div>'
  +plist([('a','Alex sent Marcus a bill of $200 for repairs to his car.<br>Marcus paid the full amount one month after the due date.<br>How much did Marcus pay? <span class="muted">(1 mark)</span>'),
          ('b','Alex sent Lily a bill of $428 for repairs to her car. Lily did not pay the bill by the due date. Let <i>A<sub>n</sub></i> be the amount of this bill <i>n</i> months after the due date.<br><b>Write down</b> a recurrence relation, in terms of <i>A</i><sub>0</sub>, <i>A</i><sub><i>n</i>+1</sub> and <i>A<sub>n</sub></i>, that models the amount of the bill. <span class="muted">(2 marks)</span>'),
          ('c','Lily paid the full amount of her bill four months after the due date.<br>How much interest was Lily charged?<br>Round your answer to the nearest cent. <span class="muted">(1 mark)</span>')]),
  [('a','1.5% is already PER MONTH: 1.015 × 200'),('b','<i>R</i> = 1 + 1.5/100 = 1.015'),('c','<i>A</i><sub>4</sub> = 1.015<sup>4</sup> × 428 = 454.26… → minus 428')],
  '',f'VCAA 2017 Further Mathematics Exam 2 Q6 (examiner report: a 61%, b 39%, c 26% full marks) · {EDR} 5F Q18',
  stat=('mark',39),cmd=('Write down',None,'the rate is already monthly'),
  parts=[('a','<b>$203</b>'),('b',RR('428','1.015<i>A<sub>n</sub></i>','A')),('c','<b>$26.26</b> (interest only, not $454.26)')]))
S[-1]=S[-1].replace('<section class="slide T ex','<section id="x3" class="slide T ex sm',1).replace('</section>','<style>#x3 .q .parts li,#x3 .q .parts{font-size:18px!important;line-height:1.3!important}</style></section>')

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 7 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='7F' and v.get('url')]))
n=assemble(S,'12MAG · L34 · Interest rates over different time periods and effective interest rates',os.path.join(ROOT,'lessons','7F slides.html'))
print(n-1,'slides')
