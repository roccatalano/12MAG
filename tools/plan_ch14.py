"""Plan Chapter 14 (AoS4 #11, 16 Nov): titles, LIs (Cambridge 14A-14E, verbatim),
SCs (Cambridge Ch 14 skills checklist, verbatim), Study Design dot points (sd.json NW-4..7),
coursework by Cambridge exercise heading + Q ranges. Split kept = Cambridge sample planner (one lesson per subchapter)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parent.parent / 'planner/unit-plan.json'
sd = json.load(open(Path(__file__).parent / 'sd.json'))
T = lambda s: "To be able to " + s
PLAN = {
 'gm12-u4-14a': dict(sub='14A', title='Flow problems',
   li=[T('define and describe flow.'), T('calculate the maximum flow through a flow network by observation.'),
       T('identify cuts and calculate cut capacities.'),
       T('determine the maximum flow through a flow network by finding the capacity of the minimum cut.'),
       T('solve flow problems by finding minimum cut capacities.')],
   sc=['I can define and describe a directed graph.',
       'I can determine the maximum flow for any section of sequential edges of a directed graph.',
       'I can determine cut capacities.',
       'I can determine the maximum flow as equal to the minimum cut capacity.'],
   sd=['NW-4.1', 'NW-4.2'],
   cw=[('Directed graphs','Q1'),('Cuts','Q2–3'),('Maximum-flow','Q4'),('Minimum-cut maximum-flow','Q5'),
       ('Networks with more than one source','Q6'),('Analysis of maximum-flow problems','Q7–8'),('Exam 1 style questions','Q9–11')]),
 'gm12-u4-14b': dict(sub='14B', title='Matching and allocation problems',
   li=[T('define and describe bipartite graphs.'), T('solve assignment problems using the Hungarian Algorithm.')],
   sc=['I can draw directed and weighted bipartite graphs.',
       'I can use the Hungarian algorithm to determine an optimum allocation in order to minimise cost.'],
   sd=['NW-6.1', 'NW-6.2'],
   cw=[('Bipartite graphs','Q1–4'),('The Hungarian algorithm','Q5–10'),('Exam 1 style questions','Q11–14')]),
 'gm12-u4-14c': dict(sub='14C', title='Precedence tables and activity networks',
   li=[T('identify activities in a project.'), T('understand the precedence that some activities have over others in a project.'),
       T('identify immediate predecessors of activities from an activity network.'), T('draw an activity network from a precedence table.'),
       T('understand and explain the need for dummy activities in projects.'), T('include dummy activities in activity networks as required.')],
   sc=['I can create an activity network from a precedence table.', 'I can write down a precedence table from an activity network.',
       'I can decide when to use dummy activities in an activity network.'],
   sd=['NW-7.1'],
   cw=[('Constructing activity networks from precedence tables','Q1–2'),('Constructing precedence tables from activity networks','Q3–7'),('Exam 1 style questions','Q8–10')]),
 'gm12-u4-14d': dict(sub='14D', title='Scheduling problems and critical path analysis',
   li=[T('understand activity networks that include weights (durations) of each activity.'),
       T('determine the EST for activities using forward scanning.'), T('determine the LST for activities using backward scanning.'),
       T('calculate and understand the existence of float times for some activities.'),
       T('identify the critical path and completion time of a project.')],
   sc=['I can use forward scanning to determine the earliest starting time of activities in an activity network.',
       'I can use backward scanning to determine the latest starting time of activities in an activity network.',
       'I can determine the float time for activities in an activity network.',
       'I can determine the overall minimum completion time for a project using critical path analysis.',
       'I can determine the critical path for an activity network.'],
   sd=['NW-7.2', 'NW-7.3'],
   cw=[('Calculations from elements of an activity network','Q1–6'),('Critical path analysis from a given activity network','Q7–11'),
       ('Critical path analysis from precedence table only','Q12–13'),('Exam 1 style questions','Q14–18')]),
 'gm12-u4-14e': dict(sub='14E', title='Crashing',
   li=[T('use crashing to reduce the completion time of a project.'),
       T('minimise the cost of crashing activities to achieve the maximum reduction in completion time of a project.')],
   sc=['I can use crashing to reduce the completion time of a project.'],
   sd=['NW-7.4'],
   cw=[('Crashing','Q1–4'),('Crashing with cost','Q5–8'),('Exam 1 style questions','Q9–11')]),
}
d = json.load(open(P))
ch = next(c for a in d['aos'] for c in a['chapters'] if c['n'] == 14)
for l in ch['lessons']:
    p = PLAN.get(l['id'])
    if not p: continue
    s = p['sub']; l['title'] = p['title']; l.pop('shell', None)
    c = l['card']
    c['learningObjectives'] = [{'sub': s, 'items': p['li']}]
    c['successCriteria'] = [{'sub': s, 'items': p['sc']}]
    c['studyDesign'] = [sd[k] for k in p['sd']]
    c['homework'] = {'source': 'plan', 'sets': [
        {'title': f'Cambridge · Exercise {s}', 'items': [{'skill': k, 'q': q} for k, q in p['cw']], 'note': ''},
        {'title': 'Revision book', 'items': [], 'note': f'The {s} section'}]}
for l in ch['lessons']:
    if l['id'] == 'gm12-ch14-test': l.pop('shell', None)
json.dump(d, open(P, 'w'), ensure_ascii=False, indent=1)
