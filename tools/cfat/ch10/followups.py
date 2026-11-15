"""CFAT 3.10.x follow-ups (rule 8): Jacaranda Maths Quest 12 General Mathematics VCE U3&4 7th ed (2023), Topic 8 exercises.
Matched by the Edrolo exercise question's skill heading (tools/y12_edrolo_exercise_questions.csv). Writes q.skill, q.sub, q.fu."""
import json,csv
SK={r['edrolo_lesson']+' Q'+r['q']:(r['skill_heading'],r['cambridge_sub']) for r in csv.DictReader(open('tools/y12_edrolo_exercise_questions.csv'))}
FU={'Identifying matrix properties and types':'Jacaranda 8.2 Q1–8',
'Adding and subtracting matrices':'Jacaranda 8.3 Q1–5, 8–12',
'Determining the transpose of a matrix':'No Jacaranda exercise Q on transpose: re-read Jacaranda 8.2 (transpose notes) + Cambridge 10C',
'Defining matrix products':'Jacaranda 8.4 Q3, 7, 8, 10',
'Calculating a matrix product':'Jacaranda 8.4 Q1, 2, 4, 9, 11–13',
'Calculating a matrix power':'Jacaranda 8.4 Q20 (CAS)',
'Calculating the determinant of a matrix':'Jacaranda 8.5 Q1–4',
'Calculating the inverse of a matrix':'Jacaranda 8.5 Q5–12',
'Solving simultaneous equations using matrix equations':'Jacaranda 8.5 Q14–18 (matrix equations)',
'Applying permutations to matrices':'Jacaranda 8.4 Q5, 6, 16',
'Constructing permutation matrices':'Jacaranda 8.4 Q5, 6, 16',
'Interpreting and constructing communication matrices':'Jacaranda 8.6 Q1–7, 14–17',
'Interpreting and constructing dominance matrices':'Jacaranda 8.6 Q8–13'}
p='planner/unit-plan.json';d=json.load(open(p));n=0
def walk(o):
  global n
  if isinstance(o,dict):
    if str(o.get('id','')).startswith('CFAT 3.10') and 'questions' in o:
      for q in o['questions']:
        s,sub=SK[q['src'].replace('Edrolo ','')]
        q['skill']=q.get('skill') or s; q['sub']=q.get('sub') or sub; q['fu']=FU[s]; n+=1
    for v in o.values(): walk(v)
  elif isinstance(o,list): [walk(v) for v in o]
walk(d);json.dump(d,open(p,'w'),indent=1,ensure_ascii=False);open(p,'a').write('\n');print(n)
