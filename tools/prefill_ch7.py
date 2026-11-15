"""Prefill the Chapter 7 lesson cards (gm12-u3-l31..l34) - queue task AoS2 #1, 16 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 7 (learning intentions, Examples 1-32, Exercises 7A-7F headings,
Ch 7 skills checklist), Edrolo U3&4 2023 Ch 5 worked examples (5A WE1-5, 5B WE1-4, 5C WE1-2, 5D WE1-3,
5E WE1-2, 5F WE1-2, 5G WE1-2) and exam practice (5A-5G), Edrolo U1&2 2023 Ch 3 worked examples
(3B-3F) and exam practice, tools/y11_cambridge_skills_checklist.csv, tools/vcaa_current_index.csv,
tools/ledger*.csv (burnt; read from origin 16 Nov 01:40).
No Edrolo (U3&4 or U1&2) WE matches Cambridge Ex 1, 2 (sequence from a worded rule, by hand) or
Ex 26, 27 (solve for n / r on CAS) -> written You trys YT-7A-1, YT-7A-2, YT-7E-26, YT-7E-27.
Duplicate VCAA originals across books were avoided (e.g. 2020 E1 Q21 = Edrolo U3&4 5A Q18 = U1&2 3B Q16).
"""
import json, csv, math
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for a in d['aos']:
    for ch in a['chapters']:
        for l in ch['lessons']: L[l['id']]=l
SD=json.load(open('tools/sd.json'))

def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
def we(n,sub,title,yt): return {'n':n,'sub':sub,'title':title,'youTry':yt,'video':f'Cambridge GO · {sub} Resources'}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
def lo(sub,items): return {'sub':sub,'items':items}

C={}
C['gm12-u3-l31']=dict(
 learningObjectives=[lo('7A',['To be able to generate a sequence of terms recursively.',
   'To be able to generate a sequence of numbers from a worded description using a calculator.',
   'To be able to generate a sequence from a recurrence relation.',
   'To be able to generate a sequence of numbers from a recurrence relation using a calculator.',
   'To be able to number and name terms in a sequence.'])],
 successCriteria=[lo('7A',['I can generate a sequence of terms recursively.','I can generate a sequence of numbers with a calculator.',
   'I can generate a sequence from a recurrence relation.','I can use a calculator to generate sequences from recurrence relations.',
   'I can name terms in a sequence.'])],
 studyDesign=[SD['RF-1.1']],
 keyVocab=['Sequence: a list of numbers in order (terms)','Recurrence relation: a starting value + a rule that gives the next term from the current term',
   'V₀ is the starting value (term 0); Vₙ₊₁ is the term after Vₙ'],
 weDo=[we(1,'7A','Generating a sequence of terms recursively (1)','Written (modelled on Cambridge Ex 1) · YT-7A-1'),
   we(2,'7A','Generating a sequence of terms recursively (2)','Written (modelled on Cambridge Ex 2) · YT-7A-2'),
   we(3,'7A','Generating a sequence of numbers with a calculator','Edrolo 5A WE5a'),
   we(4,'7A','Generating a sequence from a recurrence relation','Edrolo 5A WE4'),
   we(5,'7A','Using a calculator to generate sequences from recurrence relations','Edrolo 5A WE5b–c'),
   we(6,'7A','Naming terms in a sequence','Edrolo U1&2 3B WE1')],
 apk=[{'kind':'Skill','ref':'Cambridge U1&2 3A checklist #2','text':'Determine a simple rule for a sequence of numbers'},
   {'kind':'Exam','ref':'Edrolo U1&2 3A Q12','text':'VCAA 2015 Exam 1 Q1 (Number patterns; no report %)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q14','5A'),('Exam 1','VCAA 2024 Exam 1 Q3','1F'),
   ('Exam 2','VCAA 2024 Exam 2 Q2ci','1G'),('Exam 2','VCAA 2023 Exam 2 Q4b','5D')),
 exit=[{'ref':'Edrolo U3&4 5A Q17','src':'VCAA 2017 Exam 1 Q18'},{'ref':'Edrolo U3&4 5A Q19','src':'VCAA 2021 Exam 1 Q17'},
   {'ref':'Edrolo U3&4 5A Q20','src':'VCAA 2019 Exam 1 Q17'}],
 cas=['recursion-sequence'], casYouTry='Edrolo 5A WE5 (sequence on CAS)',
 hw=[hw('7A',[('Generating a sequence recursively','Q1–6'),('Generating sequences using recurrence relations','Q7–8'),
   ('Exploring sequences with a calculator','Q9–10'),('Exam 1 style questions','Q11–13')])],
 note='Edrolo 5A WE1–3 (recurrence relation ↔ words / sequence) are spare You trys for Exercise 7A Q7–8.')

C['gm12-u3-l32']=dict(
 learningObjectives=[lo('7B',['To be able to graph the terms of a linear growth/decay sequence.',
   'To be able to model simple interest loans and investments using recurrence relations.',
   'To be able to use a recurrence relation to analyse a simple interest investment.',
   'To be able to model and analyse flat rate depreciation using a recurrence relation.',
   'To be able to model and analyse unit cost depreciation using a recurrence relation.']),
  lo('7D',['To be able to graph the terms of a geometric sequence.','To be able to model compound interest with a recurrence relation.',
   'To be able to model reducing balance depreciation with recurrence relations.','To be able to use reducing balance depreciation with recurrence relations.'])],
 successCriteria=[lo('7B',['I can graph the terms of a linear growth/decay sequence.','I can model simple interest loans and investments with a recurrence relation.',
   'I can use a recurrence relation to analyse a simple interest investment.','I can model flat rate depreciation using a recurrence relation.',
   'I can use a recurrence relation to analyse flat rate depreciation.','I can model unit cost depreciation with a recurrence relation.']),
  lo('7D',['I can graph the terms in a geometric sequence.','I can model compound interest with a recurrence relation.',
   'I can model reducing balance depreciation with recurrence relations.','I can use reducing balance depreciation with recurrence relations.'])],
 studyDesign=[SD['RF-1.2'],SD['RF-2.1'],SD['RF-2.2']],
 keyVocab=['Linear growth/decay: add or subtract the same amount D each step (Vₙ₊₁ = Vₙ ± D): points lie on a straight line',
   'Simple interest: D = (r/100) × V₀ added each year; flat rate depreciation: D = (r/100) × V₀ subtracted each year',
   'Unit cost depreciation: subtract the cost per unit of use (per km, per hour, per use)',
   'Geometric growth/decay: multiply by R each step (Vₙ₊₁ = R × Vₙ): points lie on a curve',
   'Compound interest R = 1 + r/100; reducing balance depreciation R = 1 − r/100'],
 weDo=[we(7,'7B','Graphing the terms of linear growth/decay sequence','Edrolo 5B WE3b'),
   we(8,'7B','Modelling simple interest investments with a recurrence relation','Edrolo 5E WE1a'),
   we(9,'7B','Using a recurrence relation to analyse a simple interest investment','Edrolo 5E WE1b–c'),
   we(10,'7B','Modelling flat rate depreciation with a recurrence relation','Edrolo 5B WE1'),
   we(11,'7B','Using a recurrence relation to analyse flat rate depreciation','Edrolo 5B WE3a'),
   we(12,'7B','Modelling unit cost depreciation with a recurrence relation','Edrolo 5B WE2'),
   we(19,'7D','Graphing the terms in a geometric sequence','Edrolo U1&2 3D WE2'),
   we(20,'7D','Modelling compound interest with a recurrence relation','Edrolo U1&2 3E WE1'),
   we(21,'7D','Modelling reducing balance depreciation with recurrence relations','Edrolo 5C WE1'),
   we(22,'7D','Using reducing balance depreciation with recurrence relations','Edrolo 5C WE2a')],
 apk=[{'kind':'Skill','ref':'Cambridge U1&2 1A checklist #5','text':'Find a percentage of a quantity'},
   {'kind':'Skill','ref':'Cambridge U1&2 1A checklist #4','text':'Convert percentages to decimals'},
   {'kind':'Exam','ref':'Edrolo U1&2 3D Q14','text':'VCAA 2016 Exam 2 Q5a'}],
 doNow=dn(('Exam 1','VCAA 2025 NHT Exam 1 Q17','7A'),('Exam 1','VCAA 2025 Exam 1 Q9','3A'),
   ('Exam 2','VCAA 2025 Exam 2 Q2b','1G'),('Exam 2','VCAA 2023 Exam 2 Q3e','3B')),
 exit=[{'ref':'Edrolo U3&4 5B Q14','src':'VCAA 2019 Exam 1 Q19'},{'ref':'Edrolo U3&4 5B Q15','src':'VCAA 2020 Exam 2 Q7b'},
   {'ref':'Edrolo U3&4 5C Q13','src':'VCAA 2019 Exam 2 Q7a'}],
 cas=['recursion-sequence'],
 hw=[hw('7B',[('Modelling linear growth and decay using recurrence relations','Q1–2'),('Modelling and analysing simple interest with recurrence relations','Q3–6'),
   ('Modelling flat-rate depreciation with recurrence relations','Q7–11'),('Modelling unit-cost depreciation with recurrence relations','Q12–15'),('Exam 1 style questions','Q16–18')]),
  hw('7D',[('Graphing geometric sequences','Q1'),('Modelling compound interest with recurrence relations','Q2–5'),
   ('Modelling reducing balance depreciation with recurrence relations','Q6–10'),('Exam 1 style questions','Q11–14')])],
 note='Big lesson (10 Examples): split it into 7B and 7D on the planner if it runs over. Edrolo 5B WE4 (unit cost: uses until a value) is a spare You try for Example 12; Edrolo U1&2 3C WE3 (flat rate fridge) a spare for Example 10.')

C['gm12-u3-l33']=dict(
 learningObjectives=[lo('7C',['To be able to convert a recurrence relation to an explicit rule.','To be able to model a simple interest investment using an explicit rule.',
   'To be able to use a rule to determine the value of a simple interest loan or investment.','To be able to model flat rate depreciation of an asset using an explicit rule.',
   'To be able to use a rule for the flat rate depreciation of an asset.','To be able to use an explicit rule for unit cost depreciation.']),
  lo('7E',['To be able to write explicit rules for geometric growth and decay.','To be able to use an explicit rule to find the value of an investment after n years.',
   'To be able to calculate the value and total depreciation of an asset after a period of reducing balance depreciation.',
   'To be able to use a calculator to solve geometric growth and decay problems.'])],
 successCriteria=[lo('7C',['I can convert a recurrence relation to an explicit rule.','I can model a simple interest investment using an explicit rule.',
   'I can use a rule to determine the value of a simple interest investment.','I can model flat rate depreciation of an asset with an explicit rule.',
   'I can use a rule for the flat rate depreciation of an asset.','I can use an explicit rule for unit cost depreciation.']),
  lo('7E',['I can write explicit rules for geometric growth and decay.','I can use a rule to find the value of an investment after n years.',
   'I can calculate the value and total depreciation of an asset after a period of reducing balance depreciation.',
   'I can use a calculator to solve geometric growth and decay problems.'])],
 studyDesign=[SD['RF-1.3'],SD['RF-2.4']],
 keyVocab=['Linear rule: Vₙ = V₀ + n × D (growth) or Vₙ = V₀ − n × D (decay)',
   'Geometric rule: Vₙ = Rⁿ × V₀','Interest earned = Vₙ − V₀; total depreciation = V₀ − Vₙ',
   'Solve for n or r on CAS; round n UP to a whole number of periods'],
 weDo=[we(13,'7C','Converting a recurrence relation to an explicit rule','Edrolo U1&2 3F WE1'),
   we(14,'7C','Modelling simple interest investments','Edrolo 5E WE2'),
   we(15,'7C','Using a rule to determine the value of a simple interest investment','Edrolo U1&2 3F WE2'),
   we(16,'7C','Modelling flat rate depreciation of an asset using an explicit rule','Edrolo 5D WE1a'),
   we(17,'7C','Using a rule for the flat rate depreciation of an asset','Edrolo 5D WE1b'),
   we(18,'7C','Using an explicit rule for unit cost depreciation','Edrolo 5D WE2'),
   we(23,'7E','Writing explicit rules for geometric growth and decay','Edrolo U1&2 3F WE3'),
   we(24,'7E','Using a rule to find the value of an investment after n years','Edrolo 5F WE2'),
   we(25,'7E','Calculating the value and total depreciation of an asset after a period of reducing balance depreciation','Edrolo 5C WE2b–c'),
   we(26,'7E','Using a calculator to solve geometric growth and decay problems to find n','Written (modelled on Cambridge Ex 26) · YT-7E-26'),
   we(27,'7E','Using a calculator to solve geometric growth and decay problems to find r','Written (modelled on Cambridge Ex 27) · YT-7E-27')],
 apk=[{'kind':'Skill','ref':'Cambridge U1&2 3D checklist #10','text':'Find the nth term to solve problems involving arithmetic sequences'},
   {'kind':'Skill','ref':'Cambridge U1&2 3G checklist #21','text':'Find the nth term in a geometric sequence using a recurrence relation'},
   {'kind':'Exam','ref':'Edrolo U1&2 3F Q12','text':'VCAA 2018 Exam 2 Q4c'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q20','7B'),('Exam 1','VCAA 2024 Exam 1 Q19','7D'),
   ('Exam 2','VCAA 2025 Exam 2 Q8ai','7B'),('Exam 2','VCAA 2024 NHT Exam 2 Q8c','7D')),
 exit=[{'ref':'Edrolo U3&4 5D Q17','src':'VCAA 2020 Exam 1 Q29'},{'ref':'Edrolo U3&4 5D Q18','src':'VCAA 2021 Exam 1 Q20'},
   {'ref':'Edrolo U3&4 5E Q16','src':'VCAA 2012 Exam 1 Q2 (no report %)'}],
 cas=['solve-n-r'],
 hw=[hw('7C',[('Writing an explicit rule from a linear recurrence relation','Q1–2'),('Using a rule for simple interest loans and investments','Q3–5'),
   ('Using a rule for flat rate depreciation of assets','Q6–9'),('Using a rule for unit cost depreciation of assets','Q10–12'),('Exam 1 style questions','Q13–14')]),
  hw('7E',[('Writing explicit rules for geometric recurrence relations','Q1–2'),('Using a rule for compound interest loans and investments','Q3–5'),
   ('Using a rule for reducing balance depreciation','Q6–7'),('Using a CAS calculator to solve geometric growth and decay problems','Q8–12'),('Exam 1 style questions','Q13–14')])],
 note='Big lesson (11 Examples): split it into 7C and 7E on the planner if it runs over. Edrolo 5D WE3 (reducing balance rule) is a spare You try for Example 23/25.')

C['gm12-u3-l34']=dict(
 learningObjectives=[lo('7F',['To be able to convert nominal (annual) interest rates to compounding period interest rates.',
   'To be able to model loans with different compounding periods using recurrence relations.',
   'To be able to model investments with different compounding periods using recurrence relations.',
   'To be able to compare loans and investments using effective interest rates.','To be able to calculate effective interest rates using a CAS calculator.'])],
 successCriteria=[lo('7F',['I can convert nominal (annual) interest rates to compounding period interest rates.',
   'I can use recurrence relations to model loans with different compounding periods.','I can model an investment that compounds monthly using recurrence relations.',
   'I can compare loans and investments using effective interest rates.','I can calculate effective interest rates using a CAS calculator.'])],
 studyDesign=[SD['RF-2.3'],SD['RF-2.2']],
 keyVocab=['Nominal rate: the stated annual rate; rate per period = nominal rate ÷ periods per year (12, 26, 52, 4)',
   'Effective interest rate: the actual % increase over one year once compounding is included',
   'Compare loans/investments by their effective rates (lower for a loan, higher for an investment)'],
 weDo=[we(28,'7F','Converting nominal interest rates to compounding period interest rates','Edrolo U1&2 3E WE3a'),
   we(29,'7F','Recurrence relations with different compounding periods','Edrolo 5F WE1a'),
   we(30,'7F','Modelling an investment that compounds monthly using recurrence relations','Edrolo 5F WE1b–c'),
   we(31,'7F','Comparing loans and investments with effective interest rates','Edrolo 5G WE2'),
   we(32,'7F','Calculating effective interest rates using a CAS calculator','Edrolo 5G WE1')],
 apk=[{'kind':'Skill','ref':'Cambridge U1&2 3H checklist #23','text':'Write a recurrence relation to model a loan that compounds with a different compounding period'},
   {'kind':'Exam','ref':'Edrolo U1&2 3F Q14','text':'VCAA 2020 Exam 1 Q26'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q18','7C'),('Exam 1','VCAA 2025 NHT Exam 1 Q21','7E'),
   ('Exam 2','VCAA 2024 Exam 2 Q5a','7C'),('Exam 2','VCAA 2026 Exam 2 Q8c','7E')),
 exit=[{'ref':'Edrolo U3&4 5F Q17','src':'VCAA 2020 Exam 1 Q24'},{'ref':'Edrolo U3&4 5G Q11','src':'VCAA 2020 Exam 1 Q28'},
   {'ref':'Edrolo U3&4 5F Q18','src':'VCAA 2017 Exam 2 Q6'}],
 cas=['effective-rate'], casYouTry='Edrolo 5G WE1 (effective rate on CAS)',
 hw=[hw('7F',[('Interest rate conversions','Q1–2'),('Recurrence relations with different compounding periods','Q3–7'),
   ('Comparing loans and investments with effective interest rates','Q8–11'),('Calculating effective interest rates using the CAS','Q12–13'),('Exam 1 style questions','Q14–17')])])

for i,c in C.items():
    card=L[i]['card']
    for k in ['learningObjectives','successCriteria','studyDesign','keyVocab','weDo','apk','doNow','exit','cas']:
        card[k]=c[k]
    if 'casYouTry' in c: card['casYouTry']=c['casYouTry']
    if 'note' in c: card['note']=c['note']
    subs=L[i]['subchapters']
    card['homework']={'source':'prefill','sets':c['hw']+[{'title':'Revision book','items':[],'note':'The '+', '.join(subs)+' section'+('s' if len(subs)>1 else '')}]}
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# written You trys
n26=math.log(12000/8000)/math.log(1.05)
r27=(1-(9000/42000)**(1/8))*100
W='planner/written-youtrys.json'; w=json.load(open(W))
lab=lambda n:f'Written for 12MAG (Claude, modelled on Cambridge Example {n})'
new=[
 {'id':'YT-7A-1','pairs':'Cambridge U3&4 Example 1','sub':'7A','label':lab(1),
  'text':'Write down the first five terms of the sequence with a starting value of 9 and the rule ‘add 7 to the previous term’.',
  'answer':'The first five terms are 9, 16, 23, 30, 37.'},
 {'id':'YT-7A-2','pairs':'Cambridge U3&4 Example 2','sub':'7A','label':lab(2),
  'text':'Write down the first five terms of the sequence with a starting value of 4 and the rule ‘triple the number and then subtract 5’.',
  'answer':'The first five terms are 4, 7, 16, 43, 124.'},
 {'id':'YT-7E-26','pairs':'Cambridge U3&4 Example 26','sub':'7E','label':lab(26),
  'text':'How many years will it take for an investment of $8000, paying compound interest at 5% per annum, to grow above $12 000? Write your answer correct to the nearest year.',
  'answer':f'12 000 = 1.05ⁿ × 8000 gives n = {n26:.4f}. Rounding up (interest is paid at the end of the year), the investment grows above $12 000 after 9 years. After 8 years the value is ${8000*1.05**8:,.2f}.'.replace(',',' ')},
 {'id':'YT-7E-27','pairs':'Cambridge U3&4 Example 27','sub':'7E','label':lab(27),
  'text':'A bakery purchased a new oven at a cost of $42 000. It has an estimated value of $9000 after 8 years of operation. If the value of the oven is depreciated using a reducing balance method, what is the annual rate of depreciation? Write your answer correct to one decimal place.',
  'answer':f'9000 = (1 − r/100)⁸ × 42 000 gives r = {r27:.4f} (the other solution, r > 100, is not sensible). The annual rate of depreciation is {r27:.1f}%.'},
]
ids={x['id'] for x in w['items']}
w['items']+=[x for x in new if x['id'] not in ids]
json.dump(w,open(W,'w'),indent=1,ensure_ascii=False)

# CAS skills (new for Ch 7; Draft)
CS='planner/cas-skills.json'; cs=json.load(open(CS)); S=cs['skills']
have={k['id'] for k in S}
NEW=[
 {'id':'recursion-sequence','skill':'Generating a sequence from a recurrence relation','subs':['7A','7B','7D'],
  'ti':['Calculator page: type the starting value (e.g. 300) and press enter.',
        'Type the rule using the previous answer, e.g. ×0.5 − 9 (the calculator shows ans·0.5−9), and press enter.',
        'Keep pressing enter: each press gives the next term (V₁, V₂, V₃ …). Count the presses to name the term.'],
  'classpad':['Main application: type the starting value (e.g. 300) and press EXE.',
        'Type the rule using ans, e.g. ans × 0.5 − 9, and press EXE.',
        'Keep pressing EXE: each press gives the next term (V₁, V₂, V₃ …). Count the presses to name the term.'],
  'tip':'The starting value is V₀, so the first press of enter/EXE after typing the rule gives V₁.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 7A Examples 3, 5 + Edrolo 5A WE5 (Draft, check against 02 Sources\\CAS guides)'},
 {'id':'solve-n-r','skill':'Solving a geometric growth/decay rule for n or r','subs':['7E'],
  'ti':['Calculator page: Menu › Algebra › Solve.',
        'Enter the rule with the known values, e.g. solve(8000 = 1.06^n × 5000, n) or solve(15000 = (1 − r/100)^10 × 56000, r), and press enter.',
        'n: round UP to the next whole period. r: keep the sensible solution (between 0 and 100) and round as asked.'],
  'classpad':['Main application: Action › Advanced › solve (or type solve( from the keyboard).',
        'Enter the rule with the known values, e.g. solve(8000 = 1.06^n × 5000, n) or solve(15000 = (1 − r/100)^10 × 56000, r), and press EXE.',
        'n: round UP to the next whole period. r: keep the sensible solution (between 0 and 100) and round as asked.'],
  'tip':'Write the rule Vₙ = Rⁿ × V₀ first, then substitute; there are often two solutions for r.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 7E Examples 26, 27 (Draft, check against 02 Sources\\CAS guides)'},
 {'id':'effective-rate','skill':'Effective interest rate','subs':['7F'],
  'ti':['Calculator page: Menu › Finance › Interest Conversion › Effective Interest Rate (pastes eff( ).',
        'Enter eff(nominal rate, compounding periods per year), e.g. eff(4.5, 12), and press enter.',
        'Write the effective rate as a percentage, rounded as asked (e.g. 4.594%).'],
  'classpad':['Main application: Interactive › Financial › Interest Conversion › convEff.',
        'Enter the compounding periods per year (e.g. 12) and the nominal rate (e.g. 4.5); OK.',
        'Write the effective rate as a percentage, rounded as asked (e.g. 4.594%).'],
  'tip':'The effective rate is always higher than the nominal rate when interest compounds more than once a year.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 7F Example 32 + Edrolo 5G WE1 (Draft, check against 02 Sources\\CAS guides)'},
]
S+=[k for k in NEW if k['id'] not in have]
json.dump(cs,open(CS,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('7A','Sequences and recurrence relations'),('7B','Linear growth and decay: simple interest, flat rate and unit cost depreciation'),
            ('7C','Rules for linear growth and decay'),('7D','Geometric growth and decay: compound interest and reducing balance depreciation'),
            ('7E','Rules for geometric growth and decay'),('7F','Nominal and effective interest rates')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

# reserve exam items (ledger_manual.csv): Do Now + exits (+ APK exam items and Cambridge APK skills)
rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((x['src'].split(' (')[0].replace('Exam ','E'),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((x['text'].split(' (')[0].replace('Exam ','E'),x['ref'],'APK',i))
        else:
            sec,num=x['ref'].split()[2],x['ref'].split()[-1]
            rows.append((f'Cambridge U1&2 skills checklist {sec} {num}','','APK',i))
M='tools/ledger_manual.csv'
old=open(M).read()
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if f'{item},' in old: print('already in ledger:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS2 prefill'])
print('ok', len(rows))
