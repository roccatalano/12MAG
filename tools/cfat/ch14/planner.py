"""Add CFAT 4.14.1-4.14.3 to the planner cards (unit-plan.json) and reserve their items in tools/ledger_manual.csv."""
import json, sys, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import CFATS
P = os.path.join(R, 'planner/unit-plan.json'); d = json.load(open(P))
L = {l['id']: l for ch in d['aos'][3]['chapters'] for l in ch['lessons']}
where = {'CFAT 4.14.1': ('gm12-u4-14c', 'Start of the 14C lesson.'), 'CFAT 4.14.2': ('gm12-u4-14e', 'Start of the 14E lesson.'), 'CFAT 4.14.3': ('gm12-ch14-test', 'Start of the Ch 14 test lesson.')}
rows = []
for c in CFATS:
    lid, plan = where[c['id']]; card = L[lid].setdefault('card', {})
    mcm = len(c['mc']); sam = sum(p[2] for q in c['sa'] for p in q['parts']); base = f"lessons/{c['id']} ({c['subs']})"
    srcs = [q['src'].replace('Edrolo ', '') for q in c['mc'] + c['sa']]
    card['cfats'] = [x for x in card.get('cfats', []) if x.get('id') != c['id']]
    card['cfats'].insert(0, dict(id=c['id'], title=c['title'], covers=[c['subs']], format='About 20 min · individual · CAS and single bound reference allowed', status='Draft', plan=plan,
                                 marks=mcm + sam, mcMarks=mcm, saMarks=sam, file=base + '.html', sources=['Edrolo GM U3&4 2023 exercise questions only (rule 8): ' + ', '.join(srcs)]))
    card['materials'] = [m for m in card.get('materials', []) if m.get('kind') != c['id']]
    card['materials'].insert(0, dict(kind=c['id'], desc='Worksheet style, about 20 min, CAS and bound reference allowed.', status='draft',
                                     copies=[dict(label='Student copy', file=base + '.html', pdf=base + '.pdf'), dict(label='Solutions', file=base + ' solutions.html', pdf=base + ' solutions.pdf')]))
    for q in c['mc'] + c['sa']:
        rows.append(f"Edrolo U3&4 {q['src'].replace('Edrolo ', '').split(' (')[0]},,CFAT,yes,{c['id']},2026-11-16,CFAT exercise question")
json.dump(d, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
LM = os.path.join(R, 'tools/ledger_manual.csv'); led = open(LM).read()
new = [r for r in rows if '\n' + r.split(',')[0] + ',' not in led]
open(LM, 'a').write(('' if led.endswith('\n') else '\n') + '\n'.join(new) + '\n'); print(len(new), 'ledger rows')
