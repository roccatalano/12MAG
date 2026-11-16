"""CFAT 3.11.x follow-ups (rule 8): Jacaranda Maths Quest 12 General Mathematics VCE U3&4 7th ed (2023), 8.7 Transition
matrices and Leslie matrices exercise (Q1-22). Matched by each CFAT question's skill heading (Edrolo exercise index).
Jacaranda has only one Leslie matrix exercise question (8.7 Q20). Writes q.fu on every question + a followUp list per CFAT."""
import json
J='Jacaranda 8.7 '
FU={'Interpreting and constructing state matrices':J+'Q5b, Q7b, Q20a',
'Constructing and interpreting transition diagrams':J+'Q3a, Q4a, Q9c',
'Interpreting and constructing transition matrices':J+'Q3b, Q4b, Q6, Q7a, Q10a',
'Calculating state matrices':J+'Q5b–c, Q8, Q10b i–ii, Q18a',
'Calculating the equilibrium state matrix':J+'Q7c–d, Q10b iii, Q18b, Q19',
'Interpreting the equilibrium state matrix':J+'Q9b, Q18c, Q22',
'Using transition matrices to model culling and restocking':J+'Q11–17, Q21',
'Using Leslie matrices in applied scenarios':J+'Q20 (only Leslie exercise Q)'}
p='planner/unit-plan.json';d=json.load(open(p));n=0
def walk(o):
  global n
  if isinstance(o,dict):
    if str(o.get('id','')).startswith('CFAT 3.11') and 'questions' in o:
      L={}
      for q in o['questions']:
        q['fu']=FU[q['skill']]; n+=1
        L.setdefault(q['skill'],[]).append(q['src'])
      o['followUp']=[f"{s} ({', '.join(v)}): Jacaranda U3&4 (2023) {FU[s][len('Jacaranda '):]}" for s,v in L.items()]
    for v in o.values(): walk(v)
  elif isinstance(o,list): [walk(v) for v in o]
walk(d);json.dump(d,open(p,'w'),indent=1,ensure_ascii=False);open(p,'a').write('\n');print(n)
