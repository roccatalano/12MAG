"""Prefill the Chapter 8 lesson cards (gm12-u3-l37..l45) - queue task AoS2 #10, 16 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 8 (learning intentions, Examples 1-32, Exercises 8A-8I headings),
Cambridge Ch 8 skills checklist, Edrolo U3&4 2023 Ch 6 worked examples (6A WE1-2, 6B WE1-3, 6C WE1-3,
6D WE1-3, 6E WE1-3, 6F WE1-3) and exam practice (6B-6F), tools/y11_cambridge_skills_checklist.csv,
tools/y11_edrolo_exam_practice.csv, tools/vcaa_current_index.csv, tools/ledger*.csv (read from origin 16 Nov 10:40).
Edrolo U1&2 has no annuity/loan/finance-solver chapter, so Cambridge Examples with no Edrolo U3&4 match
get written You trys (planner/written-youtrys.json): Ex 1, 2, 5, 6, 11, 13, 17, 21, 22, 23, 24, 25, 28, 29, 31, 32.
"""
import json, csv, math, re
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for a in d['aos']:
    for ch in a['chapters']:
        for l in ch['lessons']: L[l['id']]=l
SD=json.load(open('tools/sd.json'))

def we(n,sub,title,yt): return {'n':n,'sub':sub,'title':title,'youTry':yt,'video':f'Cambridge GO · {sub} Resources'}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
def lo(sub,items): return {'sub':sub,'items':items}
def W(n,sub): return f'Written (modelled on Cambridge Ex {n}) · YT-{sub}-{n}'
def sk(sec,num,text): return {'kind':'Skill','ref':f'Cambridge U1&2 {sec} checklist #{num}','text':text}
def ex(ref,text): return {'kind':'Exam','ref':ref,'text':text}
def ex_(ref,src): return {'ref':ref,'src':src}

C={}
C['gm12-u3-l37']=dict(sub='8A',
 lo=['To be able to generate a sequence from a recurrence relation that combines both geometric and linear growth or decay.',
   'To be able to model compound interest investments with additions to the principal.',
   'To be able to use a recurrence relation to analyse compound interest investments with additions to the principal.',
   'To be able to determine the annual interest rate from a recurrence relation.'],
 sc=['I can generate a sequence from a recurrence relation that combines both geometric and linear growth or decay.',
   'I can model compound interest investments with additions to the principal.',
   'I can use a recurrence relation to analyse compound interest investments with additions to the principal.',
   'I can determine the annual interest rate from a recurrence relation.'],
 sd=['RF-1.1','RF-5.1'],
 vocab=['Vₙ₊₁ = R × Vₙ + D: grow by R (interest) then add D (regular addition) each period',
   'Annuity investment: compound interest investment with regular equal additions to the principal',
   'Rate per period = (R − 1) × 100%; annual rate = rate per period × periods per year'],
 we=[we(1,'8A','Generating a sequence from a recurrence relation of the form Vₙ₊₁ = R × Vₙ ± D',W(1,'8A')),
   we(2,'8A','Modelling compound interest investments with additions to the principal (1)',W(2,'8A')),
   we(3,'8A','Modelling compound interest investments with additions to the principal (2)','Edrolo 6F WE1a'),
   we(4,'8A','Using a recurrence relation to analyse compound interest investments with additions to the principal','Edrolo 6F WE1b'),
   we(5,'8A','Determining the annual interest rate from a recurrence relation',W(5,'8A'))],
 apk=[sk('3H',22,'Use a recurrence relation to model compound interest for investments or loans'),
   ex('Edrolo U1&2 3E Q12','VCAA 2017 Exam 2 Q5c')],
 exit=[ex_('Edrolo U3&4 6F Q16','VCAA 2018 Exam 1 Q17'),ex_('Edrolo U3&4 6F Q17','VCAA 2021 Exam 1 Q22')],
 cas=['recursion-sequence'],
 hw=[('Generating a sequence using a recurrence relation','Q1'),('Modelling compound interest investments with additions to the principal','Q2–7'),
   ('Using a recurrence relation to model and analyse an investment with additions to the principal','Q8–11'),('Exam 1 style questions','Q12–14')])
C['gm12-u3-l38']=dict(sub='8B',
 lo=['To be able to model a reducing balance loan with a recurrence relation.','To be able to use a recurrence relation to analyse a reducing balance loan.',
   'To be able to model an annuity with a recurrence relation.','To be able to use a recurrence relation to analyse an annuity.'],
 sc=['I can model a reducing balance loan with a recurrence relation.','I can use a recurrence relation to analyse a reducing balance loan.',
   'I can model an annuity with a recurrence relation.','I can use a recurrence relation to analyse an annuity.'],
 sd=['RF-3.1','RF-4.1'],
 vocab=['Reducing balance loan: interest is added each period, then a regular payment D is subtracted: Vₙ₊₁ = R × Vₙ − D',
   'Annuity: an investment that pays out a regular amount D each period until the balance runs out: Vₙ₊₁ = R × Vₙ − D',
   'R = 1 + r/(100 × periods per year)'],
 we=[we(6,'8B','Modelling a reducing balance loan with a recurrence relation (1)',W(6,'8B')),
   we(7,'8B','Modelling a reducing balance loan with a recurrence relation (2)','Edrolo 6B WE1a'),
   we(8,'8B','Using a recurrence relation to analyse a reducing balance loan','Edrolo 6B WE1b'),
   we(9,'8B','Modelling an annuity with a recurrence relation','Edrolo 6D WE1')],
 apk=[sk('3B',5,'Generate a sequence from a recurrence relation'),ex('Edrolo U1&2 3F Q13','VCAA 2020 Exam 1 Q22')],
 exit=[ex_('Edrolo U3&4 6B Q18','VCAA 2017 Exam 1 Q17'),ex_('Edrolo U3&4 6D Q17','VCAA 2016 Exam 1 Q18')],
 cas=['recursion-sequence'],
 hw=[('Modelling reducing balance loans with recurrence relations','Q1–6'),('Using a recurrence relation to analyse a reducing balance loan','Q7–8'),
   ('Modelling and analysing an annuity with a recurrence relation','Q9–15'),('Exam 1 style questions','Q16–18')])
C['gm12-u3-l39']=dict(sub='8C',
 lo=['To be able to apply the amortisation process.','To be able to construct an amortisation table.',
   'To be able to analyse an amortisation table for a reducing balance loan.',
   'To be able to read and interpret an amortisation table for an annuity to find the interest rate.',
   'To be able to interpret and construct an amortisation table for a compound interest investment with additions to the principal.'],
 sc=['I can apply the amortisation process.','I can construct an amortisation table for a reducing balance loan.',
   'I can analyse an amortisation table for a reducing balance loan.','I can analyse an amortisation table for an annuity to find the interest rate.',
   'I can interpret and construct an amortisation table for a compound interest investment with additional payments.'],
 sd=['RF-3.2','RF-4.2'],
 vocab=['Amortisation table columns: payment number · payment · interest · principal reduction · balance',
   'Interest = rate per period × previous balance; principal reduction = payment − interest; new balance = old balance − principal reduction',
   'Investment with additions: principal increase = payment + interest; new balance = old balance + principal increase'],
 we=[we(10,'8C','Applying the amortisation process','Edrolo 6A WE1'),
   we(11,'8C','Constructing an amortisation table for a reducing balance loan',W(11,'8C')),
   we(12,'8C','Analysing an amortisation table for a reducing balance loan','Edrolo 6B WE2'),
   we(13,'8C','Analysing an amortisation table for an annuity to find the interest rate',W(13,'8C')),
   we(14,'8C','Interpreting and constructing an amortisation table for a compound interest investment with additional payments','Edrolo 6F WE2')],
 apk=[sk('3E',11,'Find the amount of simple interest each year'),ex('Edrolo U1&2 3C Q18','VCAA 2021 Exam 2 Q7a')],
 exit=[ex_('Edrolo U3&4 6B Q19','VCAA 2016 Exam 1 Q22'),ex_('Edrolo U3&4 6F Q18','VCAA 2017 Exam 1 Q23')],
 cas=[],
 hw=[('Applying the amortisation process and constructing an amortisation table for a reducing balance loan','Q1–3'),
   ('Reading and interpreting an amortisation table for a reducing balance loan','Q4–6'),('Analysing an amortisation table for an annuity to find the interest rate','Q7'),
   ('Interpreting and constructing an amortisation table for a compound investment with additional payments','Q8'),('Exam 1 style questions','Q9–11')],
 note='Edrolo 6C WE2 (interest-only table) and 6E WE2 (perpetuity table) are spare table You trys.')
C['gm12-u3-l40']=dict(sub='8D',
 lo=['To be able to find the final payment in a reducing balance loan and an annuity.',
   'To be able to find the total payment made/received and the total interest paid/earned.',
   'To be able to plot points using an amortisation table for a reducing balance loan, an annuity and a compound interest investment with additional payments.'],
 sc=['I can find the final payment for a reducing balance loan or annuity.','I can find the total payment made and the total interest paid.',
   'I can plot from an amortisation table.'],
 sd=['RF-3.1','RF-3.2','RF-4.2'],
 vocab=['Final payment = balance before it × R (the balance plus one period of interest), so the balance ends at 0',
   'Total paid = sum of all payments; total interest = total paid − amount borrowed (loan)',
   'Plot balance (vertical) against payment number (horizontal): a loan/annuity curves down to 0, an investment curves up'],
 we=[we(15,'8D','Finding the final payment for a reducing balance loan or annuity','Edrolo 6D WE2b'),
   we(16,'8D','Finding the total payment made and total interest paid','Edrolo 6D WE2c'),
   we(17,'8D','Plotting from an amortisation table',W(17,'8D'))],
 apk=[sk('3C',8,'Tabulate and graph an arithmetic sequence'),ex('Edrolo U1&2 3D Q15','VCAA 2020 Exam 2 Q9a (adapted by Edrolo)')],
 exit=[ex_('Edrolo U3&4 6E Q15','VCAA 2020 Exam 1 Q25'),ex_('Edrolo U3&4 6B Q20','VCAA 2021 Exam 1 Q23')],
 cas=[],
 hw=[('Finding the final payment in a reducing balance loan and an annuity','Q1–4'),('Finding the total payment made/received and the total interest paid/earned','Q5–8'),
   ('Plotting points from an amortisation table','Q9–10'),('Exam 1 style questions','Q11–12')])
C['gm12-u3-l41']=dict(sub='8E',
 lo=['To be able to use the finance solver to find the value of a compounding interest investment with additional payments.',
   'To be able to use the finance solver to find the balance and final payment of a reducing balance loan.',
   'To be able to use the finance solver to find the balance of an annuity.'],
 sc=['I can determine the value of an investment with regular additions made to the principal using a financial solver.',
   'I can determine the balance and final payment of a reducing balance loan after a given number of payments.',
   'I can determine the balance of an annuity using a finance solver.'],
 sd=['RF-3.3','RF-4.3'],
 vocab=['Finance solver: N (number of payments), I% (annual rate), PV (present value), Pmt (payment), FV (future value), PpY = CpY (payments/compounding per year)',
   'Sign rule: money you hand over is negative, money you receive is positive',
   'Final payment of a loan = balance before it × R (or last regular payment + FV left over)'],
 we=[we(18,'8E','Determining the value of an investment with regular additions made to the principal using a financial solver','Edrolo 6F WE3a'),
   we(19,'8E','Determining the balance and final payment of a reducing balance loan after a given number of payments','Edrolo 6B WE3a'),
   we(20,'8E','Determining the balance of an annuity using a finance solver','Edrolo 6D WE3a')],
 apk=[sk('3I',25,'Use the rule for determining the value of an investment with compounding interest'),ex('Edrolo U1&2 3B Q16','VCAA 2020 Exam 1 Q21 (adapted by Edrolo)')],
 exit=[ex_('Edrolo U3&4 6D Q19','VCAA 2021 Exam 1 Q19'),ex_('Edrolo U3&4 6B Q21','VCAA 2021 Exam 2 Q8b')],
 cas=['finance-solver'], casYouTry='Edrolo 6A WE2 (finance solver inputs)',
 hw=[('Determining the value of an investment with regular additions made to the principal','Q1–2'),('Determining the balance of a reducing balance loan using a financial calculator','Q3–6'),
   ('Determining the balance of an annuity using a financial calculator','Q7–9'),('Exam 1 style questions','Q10–12')])
C['gm12-u3-l42']=dict(sub='8F',
 lo=['To be able to use the finance solver to find the interest rate or time taken for a compounding interest investment with additional payments.',
   'To be able to use the finance solver to find the regular payment for a reducing balance loan.',
   'To be able to use the finance solver to find the interest rate, time taken or regular payment for an annuity.'],
 sc=['I can find the interest rate for an investment with additional payments.','I can find the regular monthly payment and the time taken for an investment with additions to the principal.',
   'I can determine the payment amount, total cost and total amount of interest paid for a reducing balance loan.','I can find the interest rate, time taken and regular payment for an annuity.'],
 sd=['RF-3.3','RF-4.3'],
 vocab=['Leave the unknown blank in the finance solver and solve for it (I%, N or Pmt)',
   'N: round UP to a whole number of payments when asked for the time taken',
   'Total cost of a loan = total of all repayments; total interest = total cost − principal'],
 we=[we(21,'8F','Finding the interest rate for an investment with additional payments',W(21,'8F')),
   we(22,'8F','Finding the regular monthly payment and time taken for an investment with additions to the principal',W(22,'8F')),
   we(23,'8F','Determining the payment amount, total repayment and total amount of interest paid for a reducing balance loan',W(23,'8F')),
   we(24,'8F','Finding the interest rate, time taken and regular payment for an annuity',W(24,'8F'))],
 apk=[sk('3I',26,'Use a rule to analyse an investment'),ex('Edrolo U1&2 3E Q11','VCAA 2017 Exam 2 Q6a (adapted by Edrolo)')],
 exit=[ex_('Edrolo U3&4 6D Q18','VCAA 2018 Exam 2 Q6bi'),ex_('Edrolo U3&4 6F Q19','VCAA 2017 Exam 2 Q7b'),ex_('Edrolo U3&4 6D Q20','VCAA 2021 Exam 2 Q9')],
 cas=['finance-solver'],
 hw=[('Analysing an investment with additional payments using a financial calculator','Q1–3'),('Analysing a reducing balance loan using a financial calculator','Q4–9'),
   ('Analysing an annuity using a financial calculator','Q10–12'),('Exam 1 style questions','Q13–15')],
 note='Edrolo has no worked example that solves for I%, N or Pmt, so all four You trys are written (YT-8F-21…24).')
C['gm12-u3-l43']=dict(sub='8G',
 lo=['To be able to find the value of an investment when the regular payment changes.',
   'To be able to analyse the impact of a change in the interest rate on a reducing balance loan, an annuity and an investment.'],
 sc=['I can find the value of an investment when the regular payment changes.',
   'I can analyse the impact of a change in the interest rate on a reducing balance loan, an annuity and an investment.'],
 sd=['RF-3.3','RF-4.3'],
 vocab=['Two-stage problem: solve stage 1 for FV, then use that FV (sign flipped as needed) as the PV of stage 2',
   'A rate rise with the same payment makes a loan take longer (or leaves a bigger final payment)'],
 we=[we(25,'8G','Finding the value of an investment when the regular payment changes',W(25,'8G')),
   we(26,'8G','Finding the final payment of a reducing balance loan when the interest rate changes','Edrolo 6B WE3b')],
 apk=[sk('1B',7,'Find percentage increase or decrease'),ex('Edrolo U1&2 3C Q19','VCAA 2016 Exam 2 Q6c (adapted by Edrolo)')],
 exit=[ex_('Edrolo U3&4 6B Q22','VCAA 2016 Exam 2 Q7b')],
 cas=['finance-solver'],
 hw=[('Changing the regular payment','Q1–3'),('Reducing balance loans with changing conditions','Q4–6'),('Changed conditions with annuities','Q7–9'),
   ('Changed conditions on investments','Q10–11'),('Exam 1 style questions','Q12–14')],
 note='Edrolo 6D WE3b (annuity rate drops after 6 months) is a spare You try for the annuity part of Example 26 / Exercise 8G Q7–9.')
C['gm12-u3-l44']=dict(sub='8H',
 lo=['To be able to find the regular payment amount for an interest-only loan with and without a financial solver.',
   'To be able to find the amount borrowed for an interest-only loan.','To be able to find the interest rate for an interest-only loan.'],
 sc=['I can find the repayment amount for an interest-only loan with and without finance solver.',
   'I can find the amount borrowed for an interest-only loan.','I can find the interest rate for an interest-only loan.'],
 sd=['RF-3.3'],
 vocab=['Interest-only loan: each payment equals the interest, so the balance never changes: Vₙ₊₁ = R × Vₙ − D with D = r/(100 × p) × V₀',
   'In the finance solver FV = −PV (the balance at the end equals the amount borrowed)'],
 we=[we(27,'8H','Finding the regular payment for an interest-only loan','Edrolo 6C WE1a'),
   we(28,'8H','Finding the amount borrowed for an interest-only loan',W(28,'8H')),
   we(29,'8H','Finding the interest rate for an interest-only loan',W(29,'8H'))],
 apk=[sk('1B',6,'Increase or decrease a value by a percentage'),ex('Edrolo U1&2 3B Q15','VCAA 2020 Exam 2 Q7a (adapted by Edrolo)')],
 exit=[ex_('Edrolo U3&4 6C Q13','VCAA 2021 Exam 1 Q24')],
 cas=['finance-solver'],
 hw=[('Finding the regular payment for an interest-only loan','Q1–7'),('Finding the amount borrowed for an interest-only loan','Q8–10'),
   ('Finding the interest rate for an interest-only loan','Q11–14'),('Exam 1 style questions','Q15–17')],
 note='Edrolo 6C WE3a (interest-only payment on the finance solver) is a spare You try for Example 27.')
C['gm12-u3-l45']=dict(sub='8I',
 lo=['To be able to calculate the regular payment from a perpetuity.','To be able to calculate the investment required to establish a perpetuity.',
   'To be able to calculate the interest rate of a perpetuity.'],
 sc=['I can calculate the payment from a perpetuity.','I can calculate the investment required to establish a perpetuity.',
   'I can calculate the interest rate of a perpetuity.'],
 sd=['RF-4.4'],
 vocab=['Perpetuity: an annuity that pays only the interest each period, so it lasts forever',
   'D = r/(100 × p) × V₀; rearrange for V₀ = D ÷ (r/(100 × p)) or r = 100 × p × D ÷ V₀'],
 we=[we(30,'8I','Calculating the payment from a perpetuity','Edrolo 6E WE1a'),
   we(31,'8I','Calculating the investment required to establish a perpetuity',W(31,'8I')),
   we(32,'8I','Calculating the interest rate of a perpetuity',W(32,'8I'))],
 apk=[sk('1F',14,'Use the unitary method to solve problems'),sk('1A',3,'Convert percentages to fractions')],
 exit=[ex_('Edrolo U3&4 6E Q16','VCAA 2016 Exam 1 Q21'),ex_('Edrolo U3&4 6E Q17','VCAA 2021 Exam 2 Q6')],
 cas=['finance-solver'], casYouTry='Edrolo 6E WE3a (perpetuity on the finance solver)',
 hw=[('Calculating the payment from a perpetuity','Q1–3'),('Calculating the investment required to establish a perpetuity','Q4–6'),
   ('Calculating the interest rate of a perpetuity','Q7–11'),('Exam 1 style questions','Q12–13')],
 note='No Edrolo U1&2 exam question fits perpetuities (both APK items are Cambridge skills).')

# ---------- Do Now (current-design VCAA, retrieval only, not burnt) ----------
burnt=set()
for f in ['tools/ledger.csv','tools/ledger_manual.csv']:
    for r in csv.reader(open(f)):
        if r: burnt.add(r[0].strip())
idx=list(csv.DictReader(open('tools/vcaa_current_index.csv')))
def key(r): return f"VCAA {r['paper']} E{r['exam']} {r['q']}"
def qroot(r): return f"{r['paper']} E{r['exam']} {re.match(r'Q\d+',r['q']).group(0)}"
ORDER=['8A','8B','8C','8D','8E','8F','8G','8H','8I']
used=set(); usedroot=set()
def pick(exam,ok,lesson_roots):
    cands=[r for r in idx if r['exam']==exam and ok(r['subchapter']) and key(r) not in burnt and key(r) not in used
           and qroot(r) not in lesson_roots]
    # spread: prefer question roots not used anywhere yet, then newest papers
    cands.sort(key=lambda r:(qroot(r) in usedroot, -int(r['paper'][:4]), 'NHT' in r['paper'], int(re.sub(r'\D','',r['q'][:3]) or 0)))
    r=cands[0]; used.add(key(r)); usedroot.add(qroot(r)); lesson_roots.add(qroot(r)); return r
aos1=lambda s: s[0] in '12345' and len(s)==2
for i,(lid,c) in enumerate(C.items()):
    earlier=set(['7A','7B','7C','7D','7E','7F']+ORDER[:i])
    recent=set(ORDER[max(0,i-2):i]) or {'7E','7F'}
    roots=set(); dn=[]
    for exam,ok in [('1',lambda s:s in recent),('1',aos1),('2',lambda s:s in earlier),('2',aos1)]:
        try: r=pick(exam,ok,roots)
        except IndexError: r=pick(exam,lambda s:s in earlier,roots)
        dn.append({'exam':'Exam '+exam,'ref':f"VCAA {r['paper']} Exam {r['exam']} {r['q']}",'sec':r['subchapter']})
    c['doNow']=dn

for i,c in C.items():
    card=L[i]['card']; s=c['sub']
    card['learningObjectives']=[lo(s,c['lo'])]; card['successCriteria']=[lo(s,c['sc'])]
    card['studyDesign']=[SD[k] for k in c['sd']]; card['keyVocab']=c['vocab']; card['weDo']=c['we']
    card['apk']=c['apk']; card['doNow']=c['doNow']; card['exit']=c['exit']; card['cas']=c['cas']
    if 'casYouTry' in c: card['casYouTry']=c['casYouTry']
    if 'note' in c: card['note']=c['note']
    card['homework']={'source':'prefill','sets':[hw(s,c['hw']),{'title':'Revision book','items':[],'note':f'The {s} section'}]}
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# ---------- written You trys ----------
def fv(V0,R,D,n):  # V_{n+1}=R V_n + D
    for _ in range(n): V0=R*V0+D
    return V0
def solve(f,lo_,hi,it=200):
    a,b=lo_,hi
    for _ in range(it):
        m=(a+b)/2
        if (f(a)>0)==(f(m)>0): a=m
        else: b=m
    return (a+b)/2
def money(x): return f'${x:,.2f}'.replace(',',' ')
lab=lambda n:f'Written for 12MAG (Claude, modelled on Cambridge Example {n})'
# 8C Ex11 table
rows=[];B=12000
for k in range(1,4):
    I=round(B*0.06,2);PR=round(3000-I,2);B=round(B-PR,2);rows.append(f'{k}: payment $3000.00, interest {money(I)}, principal reduction {money(PR)}, balance {money(B)}')
# 8C Ex13 table
t13=[];B=8000
for k in range(1,4):
    I=round(B*0.005,2);PR=round(1500-I,2);B=round(B-PR,2);t13.append((I,PR,B))
# 8D Ex17
t17=[];B=800.0
for k in range(1,4):
    I=round(B*0.01,2);PR=round(205-I,2);B=round(B-PR,2);t17.append((I,PR,B))
fin=round(B*1.01,2)
# 8F
r21=solve(lambda r: fv(-10000,1+r/1200,-100,120)+30000,0.01,20)
p22=solve(lambda p: fv(-15000,1.004,-p,72)+30000,0,1000)
n22=next(n for n in range(1,1000) if fv(15000,1.004,800,n)>=45000)
R23=1+7/1200
p23=solve(lambda p: fv(15000,R23,-p,48),0,2000); p23=round(p23,2)
b47=fv(15000,R23,-p23,47); f23=round(b47*R23,2); tot23=round(47*p23+f23,2)
r24=solve(lambda r: fv(250000,1+r/1200,-3000,120),0.01,20)
n24=fv; nn=0;B=250000
while B>0: B=B*(1+4.5/1200)-3500; nn+=1
N24=solve(lambda n: 250000*(1+4.5/1200)**n-3500*((1+4.5/1200)**n-1)/(4.5/1200),1,1000)
p24=round(solve(lambda p: fv(250000,1+4.5/1200,-p,180),0,5000),2)
f24=round(fv(250000,1+4.5/1200,-p24,179)*(1+4.5/1200),2)
v25=fv(fv(40000,1.054,6000,4),1.054,9000,6)
new=[
 {'id':'YT-8A-1','pairs':'Cambridge U3&4 Example 1','sub':'8A','label':lab(1),
  'text':'Write down the first five terms of the sequence generated by the recurrence relation V₀ = 2, Vₙ₊₁ = 3Vₙ + 1',
  'answer':'The first five terms are 2, 7, 22, 67, 202.'},
 {'id':'YT-8A-2','pairs':'Cambridge U3&4 Example 2','sub':'8A','label':lab(2),
  'text':'Maya has saved $4000 and invests this in a compound interest account paying 5% per annum, compounding yearly. She also adds an extra $800 each year. Model this investment using a recurrence relation of the form V₀ = the principal, Vₙ₊₁ = RVₙ + D, where Vₙ is the value of the investment after n years.',
  'answer':'V₀ = 4000, D = 800, R = 1 + 5/100 = 1.05. The recurrence relation is V₀ = 4000, Vₙ₊₁ = 1.05Vₙ + 800.'},
 {'id':'YT-8A-5','pairs':'Cambridge U3&4 Example 5','sub':'8A','label':lab(5),
  'text':'Determine the annual interest rates for each of the following investments. a Consider an investment given by the recurrence relation A₀ = 600, Aₙ₊₁ = 1.004Aₙ + 40, where Aₙ is the value of the investment after n months. b Consider an investment given by the recurrence relation W₀ = 3000, Wₙ₊₁ = 1.015Wₙ + 200, where Wₙ is the value of the investment after n quarters.',
  'answer':'a R = 1.004, so the monthly rate is 0.4%; annual rate = 0.4 × 12 = 4.8% per annum. b R = 1.015, so the quarterly rate is 1.5%; annual rate = 1.5 × 4 = 6% per annum.'},
 {'id':'YT-8B-6','pairs':'Cambridge U3&4 Example 6','sub':'8B','label':lab(6),
  'text':'Tom borrows $6000 at an interest rate of 9% per annum, compounding annually. He makes yearly payments of $1800. Construct a recurrence relation to model this loan, in the form V₀ = the principal, Vₙ₊₁ = RVₙ − D, where Vₙ is the balance of the loan after n years.',
  'answer':'V₀ = 6000, D = 1800, R = 1 + 9/100 = 1.09. The recurrence relation is V₀ = 6000, Vₙ₊₁ = 1.09Vₙ − 1800.'},
 {'id':'YT-8C-11','pairs':'Cambridge U3&4 Example 11','sub':'8C','label':lab(11),
  'text':'Sam borrows $12 000 at an interest rate of 6% per annum, compounding annually. He makes annual payments of $3000. Construct an amortisation table for Sam’s reducing balance loan for the first three payments.',
  'answer':'Payment 0: balance $12 000.00. '+'; '.join(rows)+'.'},
 {'id':'YT-8C-13','pairs':'Cambridge U3&4 Example 13','sub':'8C','label':lab(13),
  'text':f'Consider the following amortisation table for an annuity after 3 monthly payments. Payment 0: balance $8000.00. Payment 1: payment $1500.00, interest $40.00, principal reduction $1460.00, balance $6540.00. Payment 2: payment $1500.00, interest $32.70, principal reduction $1467.30, balance $5072.70. Payment 3: payment $1500.00, interest A, principal reduction B, balance {money(t13[2][2])}. a Find the annual interest rate for this annuity. b Find the values of A and B.',
  'answer':f'a Monthly rate = 40 ÷ 8000 × 100 = 0.5%; annual rate = 0.5 × 12 = 6% per annum. b A = 0.005 × 5072.70 = {money(t13[2][0])}; B = 1500 − {t13[2][0]:.2f} = {money(t13[2][1])}.'},
 {'id':'YT-8D-17','pairs':'Cambridge U3&4 Example 17','sub':'8D','label':lab(17),
  'text':f'Consider the following amortisation table for a reducing balance loan. Payment 0: balance $800.00. Payment 1: payment $205.00, interest {money(t17[0][0])}, principal reduction {money(t17[0][1])}, balance {money(t17[0][2])}. Payment 2: payment $205.00, interest {money(t17[1][0])}, principal reduction {money(t17[1][1])}, balance {money(t17[1][2])}. Payment 3: payment $205.00, interest {money(t17[2][0])}, principal reduction {money(t17[2][1])}, balance {money(t17[2][2])}. Payment 4: payment {money(fin)}, interest {money(round(fin-t17[2][2],2))}, principal reduction {money(t17[2][2])}, balance $0.00. Plot the balance of the loan against the payment number.',
  'answer':f'Points (0, 800), (1, {t17[0][2]:.2f}), (2, {t17[1][2]:.2f}), (3, {t17[2][2]:.2f}), (4, 0) on axes payment number (horizontal) and balance (vertical): the points fall almost in a straight line to 0.'},
 {'id':'YT-8F-21','pairs':'Cambridge U3&4 Example 21','sub':'8F','label':lab(21),
  'text':'Lena puts $10 000 into a compound interest investment where interest compounds monthly. She adds $100 per month. She wants her investment to reach $30 000 in 10 years. Find the annual interest rate required for this to occur. Round your answer to two decimal places.',
  'answer':f'Finance solver: N = 120, PV = −10 000, Pmt = −100, FV = 30 000, PpY = CpY = 12; solve I% = {r21:.4f}. The annual interest rate is {r21:.2f}%.'},
 {'id':'YT-8F-22','pairs':'Cambridge U3&4 Example 22','sub':'8F','label':lab(22),
  'text':'Omar puts $15 000 into an investment, paying 4.8% interest per annum, compounding monthly. a If Omar wants his investment to be worth at least $30 000 in 6 years, what is the minimum he will need to add each month? b If Omar invests $800 each month immediately after interest is calculated, what is the minimum number of months required for his investment to at least triple in value?',
  'answer':f'a N = 72, I% = 4.8, PV = −15 000, FV = 30 000, PpY = CpY = 12; solve Pmt = −{p22:.4f}. Omar needs to add at least {money(math.ceil(p22*100)/100)} each month. b I% = 4.8, PV = −15 000, Pmt = −800, FV = 45 000; solve N, then round up: {n22} months.'},
 {'id':'YT-8F-23','pairs':'Cambridge U3&4 Example 23','sub':'8F','label':lab(23),
  'text':'Priya borrows $15 000 to be repaid in 47 equal monthly payments followed by a 48th payment of less than one dollar more than the regular payment. Interest is charged at the rate of 7% per annum, compounding monthly. a Find the regular monthly payment amount. Round your answer to the nearest cent. b Find the final payment. Round your answer to the nearest cent. c Find the total of the repayments on the loan. Round your answer to the nearest cent. d Find the total amount of interest paid. Round your answer to the nearest cent.',
  'answer':f'a N = 48, I% = 7, PV = 15 000, FV = 0, PpY = CpY = 12; solve Pmt: the regular payment is {money(p23)}. b Balance after 47 payments = {money(b47)}; final payment = {b47:.4f} × {R23:.6f} = {money(f23)}. c Total = 47 × {p23:.2f} + {f23:.2f} = {money(tot23)}. d Interest = {tot23:.2f} − 15 000 = {money(tot23-15000)}.'},
 {'id':'YT-8F-24','pairs':'Cambridge U3&4 Example 24','sub':'8F','label':lab(24),
  'text':'Kate invests $250 000 into an annuity, with interest compounding monthly. a What interest rate would allow Kate to withdraw $3000 each month for 10 years? Round your answer to one decimal place. b Assume the interest rate is 4.5% per annum and that Kate receives a regular monthly payment of $3500. For how many months will Kate receive a regular payment? c Assume that the interest rate is 4.5% per annum and that Kate wishes to be paid monthly payments for 15 years. How much will she regularly receive each month? d If Kate receives the regular monthly payment found in part c for 179 months, what will her final payment be? Round your answer to the nearest cent.',
  'answer':f'a N = 120, PV = −250 000, Pmt = 3000, FV = 0; I% = {r24:.3f}, so {r24:.1f}% per annum. b N = {N24:.2f}, so Kate receives {nn-1} regular payments of $3500 (then a smaller final payment). c N = 180: Pmt = {money(p24)}. d Final payment = {money(f24)}.'},
 {'id':'YT-8G-25','pairs':'Cambridge U3&4 Example 25','sub':'8G','label':lab(25),
  'text':'Ella invests $40 000 into a compound interest investment paying 5.4% per annum, compounding annually. Ella invests an additional $6000 per year immediately after interest is calculated. After four years, Ella increases her additional investment to $9000 per year. Calculate the value of Ella’s investment after ten years (in total).',
  'answer':f'Stage 1: N = 4, I% = 5.4, PV = −40 000, Pmt = −6000: FV = {money(fv(40000,1.054,6000,4))}. Stage 2: N = 6, PV = −{fv(40000,1.054,6000,4):.2f}, Pmt = −9000: FV = {money(v25)}. After ten years the investment is worth {money(v25)}.'},
 {'id':'YT-8H-28','pairs':'Cambridge U3&4 Example 28','sub':'8H','label':lab(28),
  'text':'A loan at 4.8% per annum, compounding monthly, requires payments of $600 each month. If the loan is an interest-only loan, what is the principal?',
  'answer':'600 = 4.8/(100 × 12) × V₀ = 0.004 × V₀, so V₀ = 600 ÷ 0.004 = $150 000.'},
 {'id':'YT-8H-29','pairs':'Cambridge U3&4 Example 29','sub':'8H','label':lab(29),
  'text':'An interest-only loan of $500 000 requires quarterly payments of $6250. What is the annual interest rate on the loan?',
  'answer':'6250 = r/(100 × 4) × 500 000, so r = 6250 × 400 ÷ 500 000 = 5. The annual interest rate is 5% per annum.'},
 {'id':'YT-8I-31','pairs':'Cambridge U3&4 Example 31','sub':'8I','label':lab(31),
  'text':'Calculate how much money will need to be invested in a perpetuity account, earning interest of 3.6% per annum compounding monthly, if $450 will be withdrawn every month.',
  'answer':'450 = 3.6/(100 × 12) × V₀ = 0.003 × V₀, so V₀ = 450 ÷ 0.003 = $150 000.'},
 {'id':'YT-8I-32','pairs':'Cambridge U3&4 Example 32','sub':'8I','label':lab(32),
  'text':'A sports club has $40 000 to invest. It intends to award an annual prize of $1800 with the interest earned from investing this money in a perpetuity. What is the minimum interest rate that will allow this prize to be awarded indefinitely?',
  'answer':'1800 = r/100 × 40 000, so r = 1800 × 100 ÷ 40 000 = 4.5. The minimum interest rate is 4.5% per annum.'},
]
Wf='planner/written-youtrys.json'; w=json.load(open(Wf))
ids={x['id'] for x in w['items']}
w['items']+=[x for x in new if x['id'] not in ids]
json.dump(w,open(Wf,'w'),indent=1,ensure_ascii=False)

# ---------- CAS skill: finance solver (Draft) ----------
CS='planner/cas-skills.json'; cs=json.load(open(CS)); S=cs['skills']
if 'finance-solver' not in {k['id'] for k in S}:
    S.append({'id':'finance-solver','skill':'Finance solver (TVM): loans, annuities, investments, perpetuities','subs':['8E','8F','8G','8H','8I'],
     'ti':['Calculator page: Menu › Finance › Finance Solver.',
           'Enter N (number of payments), I(%) (annual rate), PV, Pmt, FV, PpY and CpY (payments/compounding per year; tab down). Money paid out by the person is negative, money received is positive.',
           'Leave the unknown, move the cursor to it and press enter to solve. Read it off and round as asked (round N up to whole payments).'],
     'classpad':['Main menu › Financial › Compound Interest.',
           'Enter N, I%, PV, PMT, FV, P/Y and C/Y (End of period payments). Money paid out by the person is negative, money received is positive.',
           'Tap the button of the unknown (N, I%, PV, PMT or FV) to solve it. Read it off and round as asked (round N up to whole payments).'],
     'tip':'Loan: PV +, Pmt −. Investment/annuity: PV −, Pmt + (annuity) or − (additions). Interest-only loan or perpetuity: FV = −PV.',
     'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 8E–8I Examples 18–32 + Edrolo 6A WE2 (Draft, check against 02 Sources\\CAS guides)'})
json.dump(cs,open(CS,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('8A','Combining linear and geometric growth: investments with regular additions'),('8B','Reducing balance loans and annuities with recurrence relations'),
            ('8C','Amortisation tables'),('8D','Analysing amortisation tables: final payment, totals, graphs'),('8E','Finance solver: balance and final payment'),
            ('8F','Finance solver: interest rate, time and payment'),('8G','Changing conditions: payment and interest rate changes'),
            ('8H','Interest-only loans'),('8I','Perpetuities')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

# ---------- reserve in ledger ----------
rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((x['src'].split(' (')[0].replace('Exam ','E'),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((x['text'].split(' (')[0].replace('Exam ','E'),x['ref'],'APK',i))
        else:
            p=x['ref'].split(); rows.append((f'Cambridge U1&2 skills checklist {p[2]} {p[-1]}','','APK',i))
M='tools/ledger_manual.csv'; old=open(M).read()
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if f'{item},' in old: print('already in ledger:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS2 prefill'])
print('ok',len(rows))
for i,c in C.items(): print(i,[x['ref']+' '+x['sec'] for x in c['doNow']])
