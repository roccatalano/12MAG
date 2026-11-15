"""AoS3 #12: plan Chapter 11 (Transition matrices and Leslie matrices) lessons in planner/unit-plan.json.
Split kept as the Cambridge sample planner: 11A · 11B · 11C · 11D · 11E (5 lessons; 13 Examples).
Learning intentions = Cambridge U3&4 (2023) subchapter 'Learning intentions' (pp. 552-600);
success criteria = Cambridge Chapter 11 skills checklist (items 1-12);
coursework = Cambridge exercises by section heading."""
import json
P='planner/unit-plan.json'
LI={
'11A':["To be able to set up a transition matrix from a diagram or written information."],
'11B':["To be able to interpret a transition matrix and a transition diagram."],
'11C':["To be able to use a matrix recurrence relation: S0 = initial state matrix, Sn+1 = TSn, to generate a sequence of state matrices.","To be able to informally identify the equilibrium state or steady-state matrix in the case of regular state matrices."],
'11D':["To be able to use a matrix recurrence relation S0 = initial state matrix, Sn+1 = TSn + B to model systems that include external additions or reductions at each step of the process."],
'11E':["To use and interpret Leslie matrices to analyse changes in population over time."]}
SC={
'11A':["I can set up a transition matrix from a diagram.","I can set up a transition matrix from written information."],
'11B':["I can interpret a transition matrix and a transition diagram."],
'11C':["I can use a recurrence relation to calculate state matrices step by step.","I can use a recurrence relation Sn = TⁿS0 to determine the nth state.","I can use the inverse of a transition matrix.","I can estimate the steady-state solution for suitable transition matrices."],
'11D':["I can use the matrix recurrence relation S0 = initial state matrix, Sn+1 = TSn + B."],
'11E':["I can determine state matrices and construct life cycle diagrams in situations modelled by Leslie matrices.","I can enter information into a Leslie matrix from written information.","I can use numerical techniques to consider the limiting behaviour of Leslie matrices.","I can identify the properties of a Leslie matrix and the state matrices when there is a constant rate."]}
CW={
'11A':[("Setting up a transition matrix from a transition diagram","Q1–3"),("Exam 1 style questions","Q4")],
'11B':[("Interpreting transition matrices","Q1–4"),("Exam 1 style questions","Q5–6")],
'11C':[("Calculating state matrices step-by-step and by rule","Q1–5"),("Practical applications of transition matrices","Q6–8"),("Exam 1 style questions","Q9–11")],
'11D':[("Using a recurrence rule to calculate state matrices","Q1"),("Practical application","Q2"),("Exam 1 style questions","Q3–4")],
'11E':[("Determining state matrices and life cycle diagrams","Q1–3"),("Entering information in a Leslie matrix and state matrix","Q4–5"),("Limiting behaviour for Leslie matrices","Q6–10"),("Exam 1 style questions","Q11–13")]}
SD={'11A':["MX-2.3","MX-S2"],'11B':["MX-2.3","MX-S2"],'11C':["MX-2.1","MX-2.2","MX-S1"],'11D':["MX-2.4","MX-S4"],'11E':["MX-2.1","MX-2.3"]}
LESSONS=[('gm12-u4-11a',['11A'],'Transition matrices: setting up a transition matrix'),
 ('gm12-u4-11b',['11B'],'Interpreting transition matrices'),
 ('gm12-u4-11c',['11C'],'Transition matrices: using recursion and the steady state'),
 ('gm12-u4-11d',['11D'],'Transition matrices: using the rule Sn+1 = TSn + B'),
 ('gm12-u4-11e',['11E'],'Leslie matrices')]
sd=json.load(open('tools/sd.json'))
d=json.load(open(P))
ch=[c for A in d['aos'] for c in A['chapters'] if c['n']==11][0]
check=[l for l in ch['lessons'] if l['kind']=='check']
new=[]
for lid,subs,title in LESSONS:
  sdp=[]
  for s in subs:
    for k in SD[s]:
      if sd[k] not in sdp: sdp.append(sd[k])
  sets=[{"title":f"Cambridge · Exercise {s}","items":[{"skill":a,"q":b} for a,b in CW[s]],"note":""} for s in subs]
  sets.append({"title":"Revision book","items":[],"note":"The "+" and ".join(subs)+" section"+("s" if len(subs)>1 else "")})
  new.append({"id":lid,"kind":"lesson","subchapters":subs,"title":title,"card":{
    "learningObjectives":[{"sub":s,"items":LI[s]} for s in subs],
    "successCriteria":[{"sub":s,"items":SC[s]} for s in subs],
    "studyDesign":sdp,
    "homework":{"source":"prefill","sets":sets}}})
for c in check: c.pop('shell',None)
ch['lessons']=new+check
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
