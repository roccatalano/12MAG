"""CFAT 4.14.x follow-ups (rule 8): Jacaranda Maths Quest 12 General Mathematics VCE U3&4 7th ed (2023), Topic 10 exercises
(10.2 Precedence tables and activity networks, 10.3 Critical path analysis with backward scanning and crashing,
10.4 Flow problems, 10.5 Bipartite graphs and allocation problems). Matched by the Edrolo exercise question's skill heading
(tools/y12_edrolo_exercise_questions.csv). Jacaranda has no exercise on reachability in directed graphs (closest: 10.4
Q4-5, inflow/outflow) and none on crashing with restrictions (closest: 10.3 Q19e-f). Writes a followUp list on each CFAT entry."""
import json
J='Jacaranda U3&4 (2023) '
FU={'CFAT 4.14.1':[
 'Navigating directed graphs (Edrolo 8E Q1, Q4, Q7): '+J+'10.4 Ex Q4, Q5',
 'Capacity of a cut (Edrolo 8E Q5): '+J+'10.4 Ex Q8a–b, Q11a–b',
 'Maximum flow / minimum cut (Edrolo 8E Q9): '+J+'10.4 Ex Q7, Q8c, Q9, Q11c, Q13',
 'Matching problems as a bipartite graph (Edrolo 8G Q1, Q2, Q4): '+J+'10.5 Ex Q1–5'],
'CFAT 4.14.2':[
 'Interpreting precedence tables (Edrolo 8H Q1, Q2): '+J+'10.2 Ex Q5',
 'Constructing activity networks (Edrolo 8H Q3, Q4): '+J+'10.2 Ex Q3, Q4, Q9; 10.3 Ex Q9, Q10, Q12',
 'Forward scanning: EST and minimum completion time (Edrolo 8I Q3, Q4): '+J+'10.2 Ex Q1, Q2, Q8a–b',
 'Critical path and float times (Edrolo 8I Q7, Q8): '+J+'10.2 Ex Q7; 10.3 Ex Q1, Q5, Q6, Q8, Q16, Q17'],
'CFAT 4.14.3':[
 'Crashing an activity network (Edrolo 8J Q1, Q3, Q7): '+J+'10.3 Ex Q15d, Q19e',
 'Crashing with restrictions (Edrolo 8J Q4, Q6): '+J+'10.3 Ex Q19f (nearest: no restricted-crashing exercise)']}
p='planner/unit-plan.json';d=json.load(open(p));n=0
def walk(o):
  global n
  if isinstance(o,dict):
    if o.get('id') in FU and 'covers' in o: o['followUp']=FU[o['id']]; n+=1
    for v in o.values(): walk(v)
  elif isinstance(o,list): [walk(v) for v in o]
walk(d);json.dump(d,open(p,'w'),indent=1,ensure_ascii=False);open(p,'a').write('\n');print(n)
