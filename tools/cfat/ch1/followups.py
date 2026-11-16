"""CFAT 1.1.1-1.1.3 follow-ups (rule 8): Jacaranda Maths Quest 12 General Mathematics VCE U3&4 7th ed (2023),
Topic 1 'Investigating data distributions' exercises 1.2-1.10 (+ 1.11 Review). Picked per CFAT question by skill.
Writes q.fu and a followUp list per CFAT (same format as Ch 7/8/10-14).
Default = dry run (prints). python3 tools/cfat/ch1/followups.py --apply  -> edits planner/unit-plan.json.
Gaps: Jacaranda Topic 1 has no 'write a report on a categorical variable' question (1.1.1 Q7a -> nearest: bar/segmented
bar charts 1.4 Q9-11), no z-score -> actual score question (1.1.3 Q5 -> scale-labelling 1.10 Q3-4) and no
'lower time is better' comparison (1.1.3 Q9b -> 1.10 Q17-18)."""
import json, sys, os
J = 'Jacaranda U3&4 (2023) '
FU = {
 'CFAT 1.1.1': {
  1: '1.2 Ex Q13, Q15', 2: '1.2 Ex Q5–7, Q14', 3: '1.4 Ex Q9, Q10 (segmented bar charts)', 4: '1.4 Ex Q7, Q8',
  5: '1.4 Ex Q12–17', 6: '1.4 Ex Q12–17', '7a': '1.4 Ex Q9–11 (nearest: no report-writing question)',
  '8a': '1.3 Ex Q10–12', '8b': '1.3 Ex Q10–12', '8c': '1.6 Ex Q7', '9a': '1.4 Ex Q18–20', '9b': '1.4 Ex Q16, Q17'},
 'CFAT 1.1.2': {
  1: '1.6 Ex Q3, Q13', 2: '1.6 Ex Q14, Q15', 3: '1.7 Ex Q13–15', 4: '1.7 Ex Q1–3', 5: '1.7 Ex Q10, Q13',
  6: '1.7 Ex Q4–6, Q10', '7a': '1.7 Ex Q13–15', '7b': '1.7 Ex Q3, Q16', '8a': '1.7 Ex Q7–9', '8b': '1.6 Ex Q3, Q12, Q13',
  '8c': '1.7 Ex Q13–15', '8d': '1.7 Ex Q11–14', '9a': '1.5 Ex Q3, Q5, Q8', '9b': '1.6 Ex Q1, Q7'},
 'CFAT 1.1.3': {
  1: '1.9 Ex Q5, Q7–11', 2: '1.10 Ex Q15, Q16, Q19', 3: '1.10 Ex Q19', 4: '1.10 Ex Q9–11', 5: '1.10 Ex Q3, Q4 (nearest: no z → actual score question)',
  6: '1.10 Ex Q15, Q16, Q19', '7a': '1.10 Ex Q9, Q10', '7b': '1.10 Ex Q12–14', '8a': '1.10 Ex Q1–4', '8b': '1.10 Ex Q9, Q10',
  '8c': '1.10 Ex Q9–11', '8d': '1.10 Ex Q12–14', '8e': '1.10 Ex Q1, Q2, Q7, Q8', '9a': '1.10 Ex Q15–19', '9b': '1.10 Ex Q17, Q18'},
}
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
p = os.path.join(R, 'planner', 'unit-plan.json'); d = json.load(open(p)); done = set()
def walk(o):
    if isinstance(o, dict):
        i = o.get('id')
        if i in FU and 'questions' in o:
            fl = []
            for q in o['questions']:
                q['fu'] = J + FU[i][q['q']]
                line = f"{q['skill']}: {q['fu']}"
                if line not in fl: fl.append(line)
            o['followUp'] = fl
            if i not in done: print(i); [print('  ', q['q'], '|', q['fu']) for q in o['questions']]; done.add(i)
        for v in o.values(): walk(v)
    elif isinstance(o, list): [walk(v) for v in o]
walk(d)
if '--apply' in sys.argv:
    json.dump(d, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n'); print('written', p)
