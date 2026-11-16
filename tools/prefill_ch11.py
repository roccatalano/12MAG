"""Prefill the Chapter 11 lesson cards (gm12-u4-11a … -11e) - queue task AoS3 #13, 16 Nov 2026 (runner).
Learning intentions, success criteria, Study Design points and coursework were set by tools/plan_ch11.py (AoS3 #12) and are kept.
Sources checked: Cambridge U3&4 2023 Ch 11 (Examples 1-13, pp. 552-595), Edrolo U3&4 2023 7G (WE1-8, incl. Leslie WE8),
7H (WE1-2), 7I (WE1-3) worked examples and exam practice (7G Q19-20, 7H Q12-14, 7I Q14-16),
Edrolo U1&2 5G exam practice (Q11-12), tools/y11_cambridge_skills_checklist.csv (Cambridge U1&2 4D-4H),
tools/vcaa_current_index.csv, tools/ledger*.csv (burnt; read from origin 16 Nov 11:15).
No Edrolo (U3&4 or U1&2) WE matches Cambridge Ex 10 (Leslie matrix from a table), 11 (limiting behaviour),
12 (constant rate of increase), 13 (periodic / increasing / decreasing) -> written You trys YT-11E-10 … YT-11E-13
(answers checked with numpy).
Exits: Edrolo has no VCAA Leslie questions (Leslie matrices are new to the 2023 Study Design), so 11E has no exit task.
Do Now: current-design items only from content already taught (AoS 1, Ch 10, earlier Ch 11 subchapters); AoS 2 items left
for the AoS 2 runner.
"""
import json, csv
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for a in d['aos']:
    for ch in a['chapters']:
        for l in ch['lessons']: L[l['id']]=l

def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
def we(n,sub,title,yt): return {'n':n,'sub':sub,'title':title,'youTry':yt,'video':f'Cambridge GO · {sub} Resources'}
def sk(sec,n,text): return {'kind':'Skill','ref':f'Cambridge U1&2 {sec} checklist #{n}','text':text}
def ex(ref,src): return {'ref':ref,'src':src}
W=lambda n,sub: f'Written (modelled on Cambridge Ex {n}) · YT-{sub}-{n}'

C={}
C['gm12-u4-11a']=dict(
 keyVocab=['Transition matrix T: shows the proportions moving from each state (columns: "from", this period) to each state (rows: "to", next period)',
   'Each column of a transition matrix adds to 1 (100%)',
   'Transition diagram: one point per state; arrows (including loops) show the % moving; the % leaving each point add to 100%',
   'State matrix Sₙ: a column matrix of the numbers in each state after n periods'],
 weDo=[we(1,'11A','Setting up a transition matrix (from a diagram)','Edrolo 7I WE2a'),
   we(2,'11A','Setting up a transition matrix (from written information)','Edrolo 7G WE4')],
 apk=[sk('4G',16,'I can set up a transition matrix.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5G Q11','text':'VCAA 2019 Exam 2 Matrices Q2b,3a (90%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q25','10F'),('Exam 1','VCAA 2023 Exam 1 Q15','5B'),
   ('Exam 2','VCAA 2025 Exam 2 Q11b','10D'),('Exam 2','VCAA 2024 Exam 2 Q2cii','1G')),
 exit=[ex('Edrolo U3&4 7I Q14','VCAA 2017 Exam 2 Matrices Q2a,b')],
 cas=['matrix-entry'], casYouTry='Enter and store the Example 1 transition matrix (check each column adds to 1)',
 note='Edrolo 7G WE1–2 (reading / constructing an initial state matrix) are spare You trys for the state-matrix idea.')

C['gm12-u4-11b']=dict(
 keyVocab=['tᵢⱼ = proportion in state j (column) this period that move to state i (row) next period',
   'Leading-diagonal elements: the proportion that stay in the same state',
   'Convert proportions to % (× 100) and to numbers (× the number in the "from" state)'],
 weDo=[we(3,'11B','Interpreting a transition matrix','Edrolo 7G WE3')],
 apk=[sk('4G',17,'I can interpret a transition matrix.')],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q31','10G'),('Exam 1','VCAA 2024 Exam 1 Q2','1A'),
   ('Exam 2','VCAA 2024 Exam 2 Q10a','10A'),('Exam 2','VCAA 2024 NHT Exam 2 Q12a','11A')),
 exit=[ex('Edrolo U3&4 7I Q16','VCAA 2019 Exam 1 Matrices Q8')],
 cas=[], casYouTry='',
 note='Edrolo 7I WE1 (interpreting a transition diagram) and 7I WE2b (matrix → diagram) are spare You trys for Example 3.')

C['gm12-u4-11c']=dict(
 keyVocab=['Recurrence relation: S₀ = initial state matrix, Sₙ₊₁ = TSₙ',
   'Rule: Sₙ = TⁿS₀',
   'Going back a step: Sₙ = T⁻¹Sₙ₊₁',
   'Steady state (equilibrium) S: for large n, Sₙ₊₁ ≈ Sₙ; find it by trying large n (e.g. 50, 51) until the state stops changing'],
 weDo=[we(4,'11C','Using a recursion relation to calculate state matrices step-by-step','Edrolo 7G WE5'),
   we(5,'11C','Determining the nth state of a system using the rule Sn = TⁿS0','Edrolo 7G WE7'),
   we(6,'11C','Using the inverse of a transition matrix (going back a step)','Edrolo 7G WE6'),
   we(7,'11C','Estimating the steady-state solution','Edrolo 7H WE1')],
 apk=[sk('4H',18,'I can use recursion to generate a sequence state matrix.'),
   sk('4D',10,'I can perform matrix multiplication using a CAS calculator.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5G Q12','text':'VCAA 2021 Exam 2 Matrices Q3a (30%)'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q27','11B'),('Exam 1','VCAA 2024 Exam 1 Q27','10E'),
   ('Exam 2','VCAA 2025 Exam 2 Q13a','11B'),('Exam 2','VCAA 2025 Exam 2 Q5a','3A')),
 exit=[ex('Edrolo U3&4 7G Q19','VCAA 2016 Exam 2 Matrices Q3a'),ex('Edrolo U3&4 7G Q20','VCAA 2017 Exam 2 Matrices Q3'),
   ex('Edrolo U3&4 7H Q12','VCAA 2018 Exam 1 Matrices Q8'),ex('Edrolo U3&4 7H Q14','VCAA 2020 Exam 2 Matrices Q3d')],
 cas=['matrix-recurrence'], casYouTry='Edrolo 7G WE7 (S10 = T¹⁰S0 on CAS)',
 note='Edrolo 7H WE2 (interpreting the equilibrium state matrix) is a spare You try for Example 7. Spare exit (not reserved): Edrolo 7H Q13 (VCAA 2018 E2 Matrices Q3e, 39%).')

C['gm12-u4-11d']=dict(
 keyVocab=['Sₙ₊₁ = TSₙ + B: B is a column matrix of the numbers added (+, restocking) or removed (−, culling) in each state every step',
   'Work one step at a time: S₁ = TS₀ + B, S₂ = TS₁ + B, … (no shortcut Sₙ = TⁿS₀ + B)',
   'The columns of T still add to 1; the total changes by the sum of the elements of B each step'],
 weDo=[we(8,'11D','Determining state matrices using the rule Sn+1 = TSn + B','Edrolo 7I WE3')],
 apk=[sk('4H',19,'I can determine what happens to a sequence of state matrices in the long term.')],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q32','11C'),('Exam 1','VCAA 2025 Exam 1 Q15','5B'),
   ('Exam 2','VCAA 2024 Exam 2 Q12a','11C'),('Exam 2','VCAA 2023 Exam 2 Q10a','10F')),
 exit=[ex('Edrolo U3&4 7I Q15','VCAA 2017 Exam 1 Matrices Q7')],
 cas=['matrix-recurrence'], casYouTry='Cambridge Ex 8 on CAS (store S0, then repeat t·s+b with ans)',
 note='')

C['gm12-u4-11e']=dict(
 keyVocab=['Leslie matrix L: females only; top row = birth (fertility) rates of each age group; sub-diagonal = survival rates; zeros elsewhere',
   'The columns of a Leslie matrix do NOT add to 1',
   'Sₙ₊₁ = LSₙ, so Sₙ = LⁿS₀; total population = [1 1 … 1] × Sₙ',
   'Life cycle diagram: one circle per age group; birth arrows back to group 1, survival arrows to the next group',
   'Long term: the population grows (rate > 1), declines (< 1), stays constant or cycles (periodic); growth rate = Sₙ₊₁ ÷ Sₙ for large n'],
 weDo=[we(9,'11E','Determining state matrices and life cycle diagrams','Edrolo 7G WE8'),
   we(10,'11E','Entering information in a Leslie matrix and state matrix',W(10,'11E')),
   we(11,'11E','Limiting behaviour for Leslie matrices',W(11,'11E')),
   we(12,'11E','A Leslie matrix and state matrix with constant rate of increase',W(12,'11E')),
   we(13,'11E','Periodic, increasing and decreasing rates of change',W(13,'11E'))],
 apk=[sk('4D',8,'I can determine the order of the resulting matrix formed under matrix multiplication.')],
 doNow=dn(('Exam 1','VCAA 2025 NHT Exam 1 Q32','11D'),('Exam 1','VCAA 2025 Exam 1 Q31','10D'),
   ('Exam 2','VCAA 2023 Exam 2 Q11a','11D'),('Exam 2','VCAA 2024 Exam 2 Q1e','2G')),
 exit=[],
 cas=['matrix-recurrence'], casYouTry='Cambridge Ex 11 on CAS (L^n·s for n = 5, 10, 50)',
 note='No exit tasks: Edrolo has no VCAA Leslie-matrix questions (new to the 2023 Study Design). Current-design Leslie items (e.g. VCAA 2024 E2 Q11, 2026 E1 Q31-32) are kept for Do Now / revision.')

for i,c in C.items():
    card=L[i]['card']
    for k in ['keyVocab','weDo','apk','doNow','exit','cas']: card[k]=c[k]
    for k in ['casYouTry','note']:
        if c.get(k): card[k]=c[k]
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# written You trys
WY='planner/written-youtrys.json'; w=json.load(open(WY))
lab=lambda n:f'Written for 12MAG (Claude, modelled on Cambridge Example {n})'
new=[
 {'id':'YT-11E-10','pairs':'Cambridge U3&4 Example 10','sub':'11E','label':lab(10),
  'text':'Information about a population of female rabbits is given in the following table. Age group (years): 0−1, 1−2, 2−3, 3−4. Initial population: 20, 30, 15, 10. Birth rates: 0, 1.2, 0.8, 0. Survival rates: 0.5, 0.6, 0.3, 0. a Write down the initial population state matrix, S0. b Using the information in the table above, write down a Leslie matrix to describe the change in population of female rabbits. c Construct a life cycle transition diagram for this Leslie matrix. d Determine the number of 3 − 4 year old female rabbits in the population after 3 years. Round your answer to the nearest whole number.',
  'answer':'a S0 = [20; 30; 15; 10]. b L = [0 1.2 0.8 0; 0.5 0 0 0; 0 0.6 0 0; 0 0 0.3 0]. c Four circles 0−1 → 1−2 → 2−3 → 3−4 with survival arrows 0.5, 0.6, 0.3; birth arrows from 1−2 (1.2) and 2−3 (0.8) back to 0−1. d S3 = L³S0 = [33.6; 13.2; 14.4; 1.8]: about 2 female rabbits aged 3−4.'},
 {'id':'YT-11E-11','pairs':'Cambridge U3&4 Example 11','sub':'11E','label':lab(11),
  'text':'Consider the following Leslie matrix L and initial population matrix S0: L = [0 3 3; 0.3 0 0; 0 0.5 0] and S0 = [1000; 0; 0]. a Find i S5 ii S10 iii S50. Premultiply each of these state matrices by [1 1 1] to calculate the total populations at each of these stages and comment. b Determine S25 and S26. Divide each age group population for S26 by the corresponding age group population for S25 and show that S26 ≈ 1.1381S25 and comment.',
  'answer':'a i S5 = [810; 243; 67.5], total ≈ 1121 ii S10 ≈ [1575; 421; 180], total ≈ 2176 iii S50 ≈ [280 035; 73 813; 32 427], total ≈ 386 275: the population keeps increasing. b S25 ≈ [11 022; 2905; 1276], S26 ≈ [12 544; 3307; 1453]; each ratio ≈ 1.1381, so in the long term every age group (and the total) grows by about 13.8% each year.'},
 {'id':'YT-11E-12','pairs':'Cambridge U3&4 Example 12','sub':'11E','label':lab(12),
  'text':'Consider the following Leslie matrix L and initial population matrix S0: L = [0 2 1; 0.6 0 0; 0 0.48 0] and S0 = [1000; 500; 200]. a Determine i S10 ii S14 iii S15. b The rate of increase of the population is a constant and each of the age group populations increase in the same way. Find this rate by comparing S14 and S15. c Confirm the ratio of the age group populations stays constant for S0, S1 and S10 at 10:5:2.',
  'answer':'a i S10 ≈ [6192; 3096; 1238] ii S14 ≈ [12 839; 6420; 2568] iii S15 ≈ [15 407; 7704; 3081]. b 15 407 ÷ 12 839 ≈ 7704 ÷ 6420 ≈ 3081 ÷ 2568 ≈ 1.2: a 20% increase each period. c S0 = [1000; 500; 200], S1 = [1200; 600; 240], S10 ≈ [6192; 3096; 1238]: each is in the ratio 10:5:2.'},
 {'id':'YT-11E-13','pairs':'Cambridge U3&4 Example 13','sub':'11E','label':lab(13),
  'text':'Consider the following Leslie matrix L and initial population matrix S0: L = [0 0 b3; 0.4 0 0; 0 0.5 0] and S0 = [500; 0; 0]. Investigate the long-term behaviour of the population if: a b3 = 5 b b3 = 3 c b3 = 8',
  'answer':'S1 = [0; 200; 0], S2 = [0; 0; 100] each time, then S3 = [100b3; 0; 0]. a b3 = 5: S3 = S6 = S9 = [500; 0; 0]: periodic (repeats every 3 years). b b3 = 3: S3 = [300; 0; 0], S6 = [180; 0; 0], S9 = [108; 0; 0]: decreasing (× 0.6 every 3 years). c b3 = 8: S3 = [800; 0; 0], S6 = [1280; 0; 0], S9 = [2048; 0; 0]: increasing (× 1.6 every 3 years).'},
]
ids={x['id'] for x in w['items']}
w['items']+=[x for x in new if x['id'] not in ids]
json.dump(w,open(WY,'w'),indent=1,ensure_ascii=False)

# CAS skill (new for Ch 11; Draft)
CS='planner/cas-skills.json'; cs=json.load(open(CS)); S=cs['skills']
have={k['id'] for k in S}
NEW=[
 {'id':'matrix-recurrence','skill':'Matrix recurrence: Sₙ = TⁿS₀, steady state, Sₙ₊₁ = TSₙ + B and Leslie matrices','subs':['11C','11D','11E'],
  'ti':['Enter and store T (or L) and S₀ as t and s (see Entering and storing a matrix).',
        'nth state: type t^n·s with the value of n (e.g. t^10·s) and press enter.',
        'Steady state: try a large n (e.g. t^50·s, then t^51·s); when the answer stops changing, that is the steady state.',
        'Step back: type t^-1·s to find the previous state.',
        'With B: store b, type t·s+b and press enter; then type t·ans+b and press enter once for each further step.'],
  'classpad':['Enter and store T (or L) and S₀ as T and S (see Entering and storing a matrix).',
        'nth state: type T^n×S with the value of n (e.g. T^10×S) and press EXE.',
        'Steady state: try a large n (e.g. T^50×S, then T^51×S); when the answer stops changing, that is the steady state.',
        'Step back: type T^-1×S to find the previous state.',
        'With B: store B, type T×S+B and press EXE; then type T×ans+B and press EXE once for each further step.'],
  'tip':'TⁿS₀ only works without B: with additions or removals, step through one period at a time.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 11C-11E CAS notes + Edrolo 7G WE7, 7I WE3 (Draft, check against 02 Sources\\CAS guides)'},
]
S+=[k for k in NEW if k['id'] not in have]
json.dump(cs,open(CS,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('11A','Transition matrices: setting up a transition matrix'),('11B','Interpreting transition matrices'),
            ('11C','Transition matrices: recursion and the steady state'),('11D','Transition matrices: Sn+1 = TSn + B'),
            ('11E','Leslie matrices')]:
    if s not in have:
        v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'',
            'status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
v['videos'].sort(key=lambda x:(int(''.join(c for c in x['sub'] if c.isdigit())),x['sub']))
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

# ledger reservations
rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((x['src'].replace('Exam ','E'),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((x['text'].split(' (')[0].replace('Exam ','E'),x['ref'],'APK',i))
        else:
            sec,num=x['ref'].split()[2],x['ref'].split()[-1]
            rows.append((f'Cambridge U1&2 skills checklist {sec} {num}','','APK',i))
M='tools/ledger_manual.csv'
old=open(M).read()
items_old={l.split(',')[0] for l in old.splitlines()}
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if item in items_old: print('ALREADY IN LEDGER:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS3 prefill'])
print('ok', len(rows))
