"""Lesson gm12-u3-l38 (8B Reducing balance loans and annuities) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/8B slides.html     Run: python3 tools/deck/gm12-u3-l38/build.py     Screenshots: python3 tools/deck/gm12-u3-l38/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim). DRAFT.
- No CFAT this lesson (CFAT 2.8.1 sits at the start of l40).
- Do Now: VCAA 2025 Exam 1 Q18 (report 52% D; 14/15/19/52) · VCAA 2026 Exam 1 Q3 (boxplot: 1, 3, 4, 5.5, 6; answer A) ·
          VCAA 2026 Exam 2 Q9a (560) · VCAA 2026 Exam 2 Q2a (46). 2026 examiner reports not yet published: no %.
- APK: Cambridge U1&2 Ch 3 skills checklist 3B #5 (skill + its example) ·
       VCAA 2020 Exam 1 Q22 (= Edrolo U1&2 3F Q13; report 55% C; 35/6/55/1/3).
- Learn: Cambridge U3&4 8B pp. 400-402 (own words) · Edrolo U3&4 6B, 6D.
- Worked examples: Cambridge U3&4 Examples 6-9 (8B, pp. 400-402). Example 8b: the book's solution line prints both $0.04 and $506.23; the answer is $506.23.
  You trys (planner card): Ex 6 = written YT-8B-6 (planner/written-youtrys.json) · Ex 7 = Edrolo U3&4 6B WE1a (p. 363) · Ex 8 = 6B WE1b (p. 363) · Ex 9 = 6D WE1a-b (p. 383).
- CAS: planner/cas-skills.json 'recursion-sequence' (task = Cambridge Example 8a).
- Exits: VCAA 2017 Further Exam 1 Q17 (Edrolo U3&4 6B Q18; report 82% A; 82/9/3/2/4) ·
         VCAA 2016 Further Exam 1 Q18 (Edrolo U3&4 6D Q17; report 77% C; 7/5/77/9/2).
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l38')
yid=lambda u:u.split('v=')[1].split('&')[0]
RR=lambda v0,rule,L='V':f'<i>{L}</i><sub>0</sub> = {v0}, &nbsp; <i>{L}</i><sub><i>n</i>+1</sub> = {rule}'
VN='<i>V<sub>n</sub></i>'
FORM='<br>'+RR('the principal','<i>RV<sub>n</sub></i> − <i>D</i>')+'<br>'

S=[]
S.append(title(38,'Reducing balance loans and annuities',f'{CAM} · 8B Using recurrence relations to analyse and model reducing balance loans and annuities','L38').replace('AOS 1 Data Analysis','AOS 2 Recursion and financial modelling'))
LI=[x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_=[x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· one Year 11 skill + one VCAA question','var(--apk)'),
  ('8B Reducing balance loans','',None),('Worked examples 6–8','→ You try',None),('CAS: the loan balance','',None),('8B Annuities','',None),
  ('Worked example 9','→ You try',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Reducing balance loan','a compound interest loan repaid with regular, equal payments, so the balance goes down to zero'),
  ('Annuity','an investment that earns compound interest and pays out regular, equal amounts until it runs out'),
  ('Payment, <i>D</i>','the amount paid (loan) or received (annuity) each period, straight after the interest is added'),
  ('Periods per year, <i>p</i>','12 months · 4 quarters · 26 fortnights · 52 weeks · 365 days')],
  [('Recurrence relation',F(RR('the principal','<i>RV<sub>n</sub></i> − <i>D</i>')),'times <i>R</i> (interest), then subtract <i>D</i>'),
   ('Growth multiplier',F('<i>R</i> = 1 + <i>r</i>/(100 × <i>p</i>)'),'<i>r</i> = annual interest rate'),
   ('Annual rate from <i>R</i>',F('<i>r</i> = (<i>R</i> − 1) × 100 × <i>p</i>'),'rate per period × periods per year')],
  f'{CAM}, 8B pp. 400–402; Study Design: amortisation of a reducing balance loan and of an annuity with a first-order linear recurrence relation'))

# ================= Do Now
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q18','Review of 8A (last lesson)',
  '<div style="font-size:30px;margin-top:60px">A recurrence relation is of the form<br><br>&nbsp; &nbsp; <i>u</i><sub>0</sub> = <i>a</i>, &nbsp; <i>u</i><sub><i>n</i>+1</sub> = <i>Ru<sub>n</sub></i> + <i>d</i><br><br>If <i>a</i> &gt; 0, <i>R</i> = 0.5 and <i>d</i> = 0, the sequence generated will be</div>',
  [('d = 0','nothing added: only × <i>R</i> → geometric'),('R = 0.5','0 &lt; <i>R</i> &lt; 1 → each term is half the one before → decreasing')],
  '<b>geometric and decreasing</b>: <b>D</b>.','VCAA 2025 General Mathematics Exam 1 Q18 (examiner report)',
  stat=("mc",52),mc=['arithmetic and increasing.','arithmetic and decreasing.','geometric and increasing.','geometric and decreasing.'],key='D',dist=[14,15,19,52],dis=('C','geometric is right, but R = 0.5 shrinks the terms')))
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q3','Review of 1E (last term)',
  '<div style="font-size:21px">A standard die has six faces, numbered one to six.<br>The die was rolled 20 times.<br>The <i>number</i> displayed on the top face after each roll was recorded.<br>A summary of the results is displayed in the boxplot below.</div>'
  +box('dnb',{"min":0,"max":7,"step":1,"lw":1,"q1":3,"m":4,"q3":5.5,"uw":6,"xl":"number","W":700,"fs":18,"top":10})+
  '<div style="font-size:21px">The correct calculation for the lower fence is</div>',
  [('Q₁, Q₃','Q₁ = 3 · Q₃ = 5.5'),('IQR','IQR = 5.5 − 3'),('LF','LF = Q₁ − 1.5 × IQR = 3 − 1.5 × (5.5 − 3)')],
  'LF = <b>3 − 1.5 × (5.5 − 3)</b>: <b>A</b>.','VCAA 2026 General Mathematics Exam 1 Q3 (2026 examiner report not yet published: no %)',
  mc=['3 − 1.5 × (5.5 − 3)','3 − 1.5 × (4 − 3)','3 + 1.5 × (5.5 − 4)','5.5 − 1.5 × (4 − 3)'],key='A'))
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2026 Exam 2 Q9a','Review of 7B (last week)',
  '<div style="font-size:26px;margin-top:30px">Hunter opens two savings accounts, each earning simple interest:<br>• $4000 is invested in account A, earning 4.5% per annum.<br>• $3500 is invested in account B, earning 4.8% per annum.<br><br>a. <b>Complete</b> the following sentence by inserting an appropriate number in the box provided. <span class="muted">(1 mark)</span><br><br>After five years, the value of account A will be greater than the value of account B by &nbsp;<span style="display:inline-block;width:110px;height:34px;border:2px solid #333;vertical-align:middle"></span>&nbsp; dollars.</div>',
  [('A','4000 + 5 × 0.045 × 4000 = 4000 + 900 = 4900'),('B','3500 + 5 × 0.048 × 3500 = 3500 + 840 = 4340'),('Difference','4900 − 4340 = 560')],
  'A is greater than B by <b>560</b> dollars.','VCAA 2026 General Mathematics Exam 2 Q9 stem and Q9a (2026 examiner report not yet published: no %)',
  cmd=('Complete',None,'value of A − value of B')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2026 Exam 2 Q2a','Review of 1D (last term)',
  '<div style="font-size:19px">The happiness index scores for 141 countries, based on 2024 data, are summarised in the table below.<br>All happiness index scores range from 0 to 10 and contain two decimal places.</div>'
  '<table style="font-size:17px;margin:4px 0 4px 60px;border-collapse:collapse"><tr><th style="padding:0 40px 0 0;text-align:left">Score range</th><th>Frequency</th></tr>'+''.join(f'<tr><td style="padding:0 40px 0 0">{c}</td><td style="text-align:center">{v}</td></tr>' for c,v in [('0.00–0.99',0),('1.00–1.99',1),('2.00–2.99',1),('3.00–3.99',14),('4.00–4.99',30),('5.00–5.99',38),('6.00–6.99',45),('7.00–7.99',12),('8.00–8.99',0),('9.00–10.00',0)])+'</table>'
  '<div style="font-size:12px" class="muted">Data: Adapted from World Population Review &lt;worldpopulationreview.com/country-rankings/happiest-countries-in-the-world&gt;</div>'
  '<div style="font-size:20px">a. How many countries in this data set have a happiness index below 5.00? <span class="muted">(1 mark)</span></div>',
  [('Rows','below 5.00 = the first five rows'),('Add','0 + 1 + 1 + 14 + 30 = 46')],
  '<b>46</b> countries','VCAA 2026 General Mathematics Exam 2 Q2 stem and Q2a (2026 examiner report not yet published: no %)',
  cmd=('How many',None,'add the frequencies below 5.00')))
for k in range(-4,0): S[k]=S[k].replace('<section class="slide T dn','<section class="slide T dn sm',1)

# ================= APK
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 3B #5','Generating a sequence from a recurrence relation',
  '<div style="font-size:30px;margin-top:50px">I can generate a sequence from a recurrence relation.<br><br><b>Write down</b> the first five terms of the sequence defined by the recurrence relation: <i>t</i><sub>0</sub> = 12 and <i>t</i><sub><i>n</i>+1</sub> = <i>t<sub>n</sub></i> + 7, showing the values of the first four iterations.</div>',
  [('t0','<i>t</i><sub>0</sub> = 12'),('Iterate','<i>t</i><sub>1</sub> = 12 + 7 = 19 · <i>t</i><sub>2</sub> = 19 + 7 = 26 · <i>t</i><sub>3</sub> = 26 + 7 = 33 · <i>t</i><sub>4</sub> = 33 + 7 = 40')],
  'The first five terms are <b>12, 19, 26, 33, 40</b>.',f'{CAM12} · Ch 3 skills checklist 3B #5',cmd=('Write down',None,'start value + four iterations')))
S.append(qslide('apk','APK · VCAA 2020 Exam 1 Q22','Rule to recurrence relation',
  '<div style="font-size:28px;margin-top:40px">An asset is purchased for $2480.<br>The value of this asset after <i>n</i> time periods, <i>V<sub>n</sub></i>, can be determined using the rule<br><br>&nbsp; &nbsp; <i>V<sub>n</sub></i> = 2480 + 45<i>n</i><br><br>A recurrence relation that also models the value of this asset after <i>n</i> time periods is</div>',
  [('Start','<i>V</i><sub>0</sub> = 2480 (n = 0)'),('Each period','+45 every period (not +45<i>n</i>)')],
  RR('2480','<i>V<sub>n</sub></i> + 45')+': <b>C</b>.',f'VCAA 2020 Exam 1 Recursion and financial modelling Q22 (examiner report) · {EDR12} 3F Q13',
  stat=("mc",55),mc=[RR('2480','<i>V<sub>n</sub></i> + 45<i>n</i>'),'<i>V<sub>n</sub></i> = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + 45<i>n</i>',RR('2480','<i>V<sub>n</sub></i> + 45'),'<i>V</i><sub>1</sub> = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + 45','<i>V<sub>n</sub></i> = 2480, &nbsp; <i>V</i><sub><i>n</i>+1</sub> = <i>V<sub>n</sub></i> + 45'],
  key='C',dist=[35,6,55,1,3],dis=('A','45n is the TOTAL added after n periods; each step adds only 45')))

# ================= Learn 1
S.append(learn('Learn · 8B','Reducing balance loans',
  '<h4>Multiply by <i>R</i>, then subtract the payment <i>D</i></h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>'+RR('the principal','<i>RV<sub>n</sub></i> − <i>D</i>')+', &nbsp;<i>V<sub>n</sub></i> = balance after <i>n</i> payments</li><li>× <i>R</i> adds the interest owed; − <i>D</i> is the regular repayment</li>'
  '<li><i>R</i> and <i>D</i> must use the SAME period: monthly payments need a monthly <i>R</i></li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">Flora: borrows $8000 at 13% p.a., compounding yearly, pays $2100 a year</span><br>'
  '<span class="frag"><i>R</i> = 1 + 13/100 = 1.13</span><br>'
  '<span class="frag"><b>'+RR('8000','1.13<i>V<sub>n</sub></i> − 2100')+'</b></span></div>',
  'The payment must be bigger than the interest, or the balance never goes down.',f'{CAM}, 8B pp. 400–401 (own words) · {EDR}, 6B',
  cards=(kcard('Growth multiplier','<i>R</i> = 1 + <i>r</i>/(100<i>p</i>)','<i>p</i> = periods per year'),)))
S.append(qslide('we','Worked example 6 · 8B','Modelling a reducing balance loan with a recurrence relation (1)',
  '<div style="font-size:28px;margin-top:40px">Flora borrows $8000 at an interest rate of 13% per annum, compounding annually. She makes yearly payments of $2100.<br><br><b>Construct</b> a recurrence relation to model this loan, in the form'+FORM+'where '+VN+' is the balance of the loan after <i>n</i> years.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 8000 and <i>D</i> = 2100'),fx('R','<i>R</i>',F('1 + ',FR([V('r','13')],['100 × 1'])),'1.13')],
  RR('8000','1.13<i>V<sub>n</sub></i> − 2100'),f'{CAM} · Example 6 (p. 400)',video='Cambridge GO · Example 6 (8B Resources)',cmd=('Construct',None,'V₀, D, then R')))
S.append(qslide('yt','You try · written for 12MAG (YT-8B-6)','Modelling a yearly loan',
  '<div style="font-size:28px;margin-top:40px">Tom borrows $6000 at an interest rate of 9% per annum, compounding annually. He makes yearly payments of $1800.<br><br><b>Construct</b> a recurrence relation to model this loan, in the form'+FORM+'where '+VN+' is the balance of the loan after <i>n</i> years.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 6000 and <i>D</i> = 1800'),fx('R','<i>R</i>',F('1 + ',FR([V('r','9')],['100 × 1'])),'1.09')],
  RR('6000','1.09<i>V<sub>n</sub></i> − 1800'),'Written for 12MAG (modelled on Cambridge Example 6) · planner/written-youtrys.json',cmd=('Construct',None,'V₀, D, then R')))
S.append(qslide('we','Worked example 7 · 8B','Modelling a reducing balance loan with a recurrence relation (2)',
  '<div style="font-size:28px;margin-top:40px">Alyssa borrows $1000 at an interest rate of 15% per annum, compounding monthly. She makes monthly payments of $250.<br><br><b>Construct</b> a recurrence relation to model this loan, in the form'+FORM+'where '+VN+' is the balance of the loan after <i>n</i> months.</div>',
  [('V0, D','<i>V</i><sub>0</sub> = 1000 and <i>D</i> = 250'),fx('R','<i>R</i>',F('1 + ',FR([V('r','15')],['100 × 12'])),'1.0125')],
  RR('1000','1.0125<i>V<sub>n</sub></i> − 250'),f'{CAM} · Example 7 (p. 401)',video='Cambridge GO · Example 7 (8B Resources)',cmd=('Construct',None,'p = 12 for monthly')))
S.append(qslide('yt','You try · Edrolo 6B WE1a','Recurrence relation for a weekly loan',
  '<div style="font-size:28px;margin-top:50px">Dawn has borrowed $5000 from Barry, who charges interest at a rate of 5% per annum, compounding weekly. Dawn will make weekly $500 repayments.<br><br>a. <b>Construct</b> a recurrence relation that can be used to model '+VN+', the value of the loan after <i>n</i> weeks.<br>Round <i>R</i> to 5 decimal places.</div>',
  [('V0, d','<i>V</i><sub>0</sub> = 5000 · <i>d</i> = 500'),fx('R','<i>R</i>',F('1 + ',FR([V('r','5')],['52 × 100'])),'1.000961… ≈ 1.00096')],
  RR('5000','1.00096 × '+VN+' − 500'),f'{EDR} · 6B Worked example 1a (p. 363)',cmd=('Construct',None,'p = 52 for weekly')))
S.append(qslide('we','Worked example 8 · 8B','Using a recurrence relation to analyse a reducing balance loan',
  '<div style="font-size:24px">Alyssa’s loan can be modelled by the recurrence relation:<br>&nbsp; &nbsp; '+RR('1000','1.0125'+VN+' − 257.85')+'</div>'
  +plist([('a','Use your calculator to find the balance of the loan after four payments.'),('b','Find the balance of the loan after two payments have been made. Round your answer to the nearest cent.')]),
  [('a','CAS: 1000 ↵, then × 1.0125 − 257.85 ↵ four times: 754.65, 506.23, 254.71, 0.0449…'),('b','the second line after 1000: <i>V</i><sub>2</sub> = 506.2331…')],
  '',f'{CAM} · Example 8 (p. 401; the book’s answer line for b prints both $0.04 and $506.23: b = $506.23)',video='Cambridge GO · Example 8 (8B Resources)',cmd=('Find',None,'one payment at a time'),
  parts=[('a','After four payments the balance is <b>$0.04</b> (to the nearest cent).'),('b','After two payments the balance is <b>$506.23</b>.')]))
S.append(qslide('yt','You try · Edrolo 6B WE1b','Balance after three weeks',
  '<div style="font-size:28px;margin-top:50px">Dawn has borrowed $5000 from Barry, who charges interest at a rate of 5% per annum, compounding weekly. Dawn will make weekly $500 repayments.<br><span class="muted" style="font-size:22px">(Part a: '+RR('5000','1.00096 × '+VN+' − 500')+')</span><br><br>b. <b>Calculate</b> the amount that Dawn owes Barry after 3 weeks.</div>',
  [('V1','1.00096 × 5000 − 500 = 4504.80'),('V2','1.00096 × 4504.80 − 500 = 4009.124…'),('V3','1.00096 × 4009.124… − 500 = 3512.973…')],
  'Dawn owes Barry <b>$3512.97</b>.',f'{EDR} · 6B Worked example 1b (p. 363)',cmd=('Calculate',None,'three periods')))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['recursion-sequence']
S.append(cas('CAS · 8B','The loan balance, payment by payment',
  '<p style="font-size:24px">Alyssa: '+RR('1000','1.0125<i>V<sub>n</sub></i> − 257.85')+'. Find the balance after four payments.</p><p style="font-size:28px;text-align:center">1000 ↵ &nbsp; × 1.0125 − 257.85 ↵ ↵ ↵ ↵</p>'
  '<p class="muted" style="font-size:20px">'+C['tip']+'</p>',
  C['ti'],C['classpad'],'<i>V</i><sub>4</sub> = 0.0449… ≈ <b>$0.04</b>',
  f'{CAM} · Example 8a (p. 401) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= Learn 2
S.append(learn('Learn · 8B','Annuities',
  '<h4>Same rule, different story</h4><ul class="bul" style="font-size:20px;line-height:1.5;margin-left:22px">'
  '<li>an <b>annuity</b> earns interest and pays YOU <i>D</i> each period: '+RR('the principal','<i>RV<sub>n</sub></i> − <i>D</i>')+'</li>'
  '<li><i>V<sub>n</sub></i> = how much money is left after <i>n</i> payments</li>'
  '<li>the calculations are identical to a reducing balance loan</li></ul>',
  '<div style="font-size:23px;text-align:center;line-height:1.7"><span class="frag">Reza: $12 000 at 6% p.a. monthly, paid $2035 a month</span><br>'
  '<span class="frag"><i>R</i> = 1 + 6/1200 = 1.005</span><br>'
  '<span class="frag"><b>'+RR('12 000','1.005<i>V<sub>n</sub></i> − 2035')+'</b></span></div>',
  'Loan: you owe the balance. Annuity: the balance is yours.',f'{CAM}, 8B p. 402 (own words) · {EDR}, 6D',
  cards=(kcard('Annual rate','<i>r</i> = (<i>R</i> − 1) × 100 × <i>p</i>'),)))
S.append(qslide('we','Worked example 9 · 8B','Modelling an annuity with a recurrence relation',
  '<div style="font-size:22px">Reza invests $12 000 in an annuity that earns interest at the rate of 6% per annum, compounding monthly, providing him with a monthly income of $2035.</div>'
  +plist([('a','Model this annuity using a recurrence relation of the form '+RR('the principal','<i>RV<sub>n</sub></i> − <i>D</i>')+' where '+VN+' is the value of the annuity after <i>n</i> months.'),('b','Use your calculator to find the value of the annuity after the first four months. Round your answer to the nearest cent.')]),
  [('a','<i>V</i><sub>0</sub> = 12 000 · <i>D</i> = 2035 · <i>R</i> = 1 + 6/(100 × 12) = 1.005'),('b','CAS: 12000 ↵, × 1.005 − 2035 ↵ four times: 10 025, 8040.125, 6045.33, 4040.55')],
  '',f'{CAM} · Example 9 (p. 402)',video='Cambridge GO · Example 9 (8B Resources)',cmd=('Model',None,'V₀, D, R, then iterate'),
  parts=[('a',RR('12 000','1.005<i>V<sub>n</sub></i> − 2035')),('b','After four months the annuity is worth <b>$4040.55</b>.')]))
S.append(qslide('yt','You try · Edrolo 6D WE1','Modelling an annuity',
  '<div style="font-size:22px">Tom invests $25 000 in an annuity with an interest rate of 7% per annum, compounding monthly. This annuity will provide him with a monthly income of $2500.</div>'
  +plist([('a','Construct a recurrence relation that can be used to model '+VN+', the value of this annuity after <i>n</i> compounding periods. Round <i>R</i> to 5 decimal places.'),('b','Calculate the value of the investment after 4 months.')]),
  [('a','<i>V</i><sub>0</sub> = 25 000 · <i>d</i> = 2500 · <i>R</i> = 1 + 7/(12 × 100) = 1.00583…'),('b','22 645.75 → 20 277.77… → 17 895.99… → 15 500.327…')],
  '',f'{EDR} · 6D Worked example 1 (p. 383)',cmd=('Construct',None,'p = 12, then four periods'),
  parts=[('a',RR('25 000','1.00583 × '+VN+' − 2500')),('b','After 4 months the investment is worth <b>$15 500.33</b>.')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2017 Exam 1 Q17','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The value of a reducing balance loan, in dollars, after <i>n</i> months, '+VN+', can be modelled by the recurrence relation shown below.<br><br>&nbsp; &nbsp; '+RR('26 000','1.003 '+VN+' – 400')+'<br><br>What is the value of this loan after five months?</div>',
  [('V1–V2','25 678.00 · 25 355.03'),('V3–V4','25 031.10 · 24 706.19'),('V5','1.003 × 24 706.19 − 400 = 24 380.31')],
  '<b>$24 380.31</b>: <b>A</b>.',f'VCAA 2017 Further Mathematics Exam 1 Recursion and financial modelling Q17 (examiner report) · {EDR} 6B Q18',
  stat=("mc",82),mc=['$24 380.31','$24 706.19','$25 031.10','$25 355.03','$25 678.00'],key='A',dist=[82,9,3,2,4],dis=('B','$24 706.19 is the balance after FOUR months: one step short')))
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2016 Exam 1 Q18','Show what you know',
  '<div style="font-size:26px;margin-top:30px">The value of an annuity, '+VN+', after <i>n</i> monthly payments of $555 have been made, can be determined using the recurrence relation<br><br>&nbsp; &nbsp; '+RR('100 000','1.0025 '+VN+' – 555')+'<br><br>The value of the annuity after five payments have been made is closest to</div>',
  [('V1–V2','99 695.00 · 99 389.24'),('V3–V4','99 082.71 · 98 775.42'),('V5','1.0025 × 98 775.42 − 555 = 98 467.36')],
  '≈ <b>$98 467</b>: <b>C</b>.',f'VCAA 2016 Further Mathematics Exam 1 Recursion and financial modelling Q18 (examiner report) · {EDR} 6D Q17',
  stat=("mc",77),mc=['$97 225','$98 158','$98 467','$98 775','$110 224'],key='C',dist=[7,5,77,9,2],dis=('D','$98 775 is the value after FOUR payments')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 8 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='8B' and v.get('url')]))
n=assemble(S,'12MAG · L38 · Reducing balance loans and annuities',os.path.join(ROOT,'lessons','8B slides.html'))
print(n-1,'slides')
