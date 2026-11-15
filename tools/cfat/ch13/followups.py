"""CFAT 4.13.x follow-ups (rule 8): Jacaranda Maths Quest 12 General Mathematics VCE U3&4 7th ed (2023), Topic 9 exercises
(9.2 Basic concepts, 9.3 Planar graphs/Euler's formula, 9.4 Walks...circuits, 9.5 Trees). Matched by the Edrolo exercise
question's skill heading (tools/y12_edrolo_exercise_questions.csv). Writes a followUp list on each CFAT entry."""
import json
J='Jacaranda U3&4 (2023) '
FU={'CFAT 4.13.1':[
 'Identifying properties of a graph (Edrolo 8A Q1, Q3): '+J+'9.2 Ex Q1–5; 9.3 Ex Q6',
 'Identifying and constructing graphs (Edrolo 8A Q5): '+J+'9.2 Ex Q7–11',
 'Using Euler’s rule (Edrolo 8A Q11): '+J+'9.3 Ex Q9, Q13, Q15, Q17',
 'Adjacency matrix from a graph (Edrolo 8B Q1, Q2, Q4): '+J+'9.2 Ex Q16–18'],
'CFAT 4.13.2':[
 'Identifying types of walks (Edrolo 8C Q1, Q3, Q4, Q6, Q8): '+J+'9.4 Ex Q1–6, Q8, Q13–17',
 'Shortest path by inspection (Edrolo 8F Q1, Q3): '+J+'9.5 Ex Q5, Q6',
 'Dijkstra’s algorithm (Edrolo 8F Q6, Q8): '+J+'9.5 Ex Q11, Q12, Q17'],
'CFAT 4.13.3':[
 'Spanning trees and their weight (Edrolo 8D Q1–3): '+J+'9.5 Ex Q1, Q3, Q4',
 'Minimum spanning tree / Prim’s (Edrolo 8D Q5–8): '+J+'9.5 Ex Q9, Q10, Q20, Q21']}
p='planner/unit-plan.json';d=json.load(open(p));n=0
def walk(o):
  global n
  if isinstance(o,dict):
    if o.get('id') in FU and 'covers' in o: o['followUp']=FU[o['id']]; n+=1
    for v in o.values(): walk(v)
  elif isinstance(o,list): [walk(v) for v in o]
walk(d);json.dump(d,open(p,'w'),indent=1,ensure_ascii=False);open(p,'a').write('\n');print(n)
