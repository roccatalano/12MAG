"""Prefill the Chapter 14 lesson cards (gm12-u4-14a … 14e) - queue task AoS4 #12, 16 Nov 2026 (runner).
Learning intentions, success criteria, Study Design points and coursework were set by AoS4 #11 and are kept.
Sources checked: Cambridge U3&4 2023 Ch 14 (Examples 1-13; the Hungarian algorithm is worked in the text with no
Example number), Edrolo U3&4 2023 Ch 8 worked examples (8E WE1-3, 8G WE1-3, 8H WE1-4, 8I WE1-4, 8J WE1-2) and exam
practice (8E Q14-16, 8G Q10-13, 8H Q14-15, 8I Q15-18, 8J Q9-12), Edrolo U1&2 2023 Ch 7 exam practice, Cambridge U1&2
Ch 8 skills checklist (#1-15), tools/vcaa_current_index.csv, tools/ledger*.csv (burnt; read from origin 16 Nov 11:00).
Flow, matching and scheduling are not in Units 1&2, so APK primes the Ch 8 graph basics they rest on; 14E (crashing)
has no U1&2 prerequisite and gets no APK.
No Edrolo worked example for Cambridge Examples 4 (maximum flow, groups that stay together) and 5 (more than one
source) -> written You trys YT-14A-4, YT-14A-5 (rule 6). Edrolo 8G WE2 (allocation by inspection) and WE3 (Hungarian
algorithm) are You trys with no Cambridge Example (2H precedent).
No CAS for Ch 14 (Cambridge prints none).
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
N='Networks and decision mathematics'

C={}
C['gm12-u4-14a']=dict(
 keyVocab=['Directed graph (digraph): each edge has a direction (arrow); a flow network has a source (start) and a sink (end)',
   'Capacity: the weight of an edge = the most that can flow along it',
   'Flow along a route of edges in a row = the smallest capacity on that route',
   'Cut: a line that separates the source from the sink; its capacity = sum of the capacities of the edges it cuts that flow from the source side to the sink side (edges flowing back are not counted)',
   'Maximum flow = capacity of the minimum cut',
   'More than one source or sink: look at each sink (outlet) on its own'],
 weDo=[we(1,'14A','Calculating the maximum flow','Edrolo 8E WE1'),
   we(2,'14A','Calculating cut capacity','Edrolo 8E WE2'),
   we(3,'14A','Calculating maximum flow using cuts','Edrolo 8E WE3'),
   we(4,'14A','Calculating maximum flow','Written for 12MAG: YT-14A-4'),
   we(5,'14A','Calculating maximum flow from more than one source','Written for 12MAG: YT-14A-5')],
 apk=[sk('8A',1,'I can identify the number of vertices, edges and loops of a graph.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7A Q14','text':f'VCAA 2016 Exam 2 {N} Q1a,bi (83%, 53%)'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q33','13F'),('Exam 1','VCAA 2024 Exam 1 Q9','3A'),
   ('Exam 2','VCAA 2025 Exam 2 Q15d','13F'),('Exam 2','VCAA 2024 Exam 2 Q1c','1G')),
 exit=[ex('Edrolo U3&4 8E Q14',f'VCAA 2016 Exam 1 {N} Q2'),ex('Edrolo U3&4 8E Q15',f'VCAA 2020 Exam 2 {N} Q4b,c'),
   ex('Edrolo U3&4 8E Q16',f'VCAA 2017 Exam 1 {N} Q8')],
 cas=[],
 note='Edrolo 8E WE1 (route through a digraph and its weight) is the closest match for Example 1. No Edrolo worked example for Examples 4 and 5: You trys written (planner/written-youtrys.json).')

C['gm12-u4-14b']=dict(
 keyVocab=['Bipartite graph: two groups of vertices; every edge joins a vertex in one group to a vertex in the other',
   'Allocation (assignment) problem: match each person/machine to exactly one task',
   'Cost matrix: rows = people, columns = tasks, entries = cost (time, money, distance)',
   'By inspection: try the possible allocations and choose the smallest total',
   'Hungarian algorithm: subtract row minimums, then column minimums; cover the zeros with the fewest lines; if fewer lines than rows, add/subtract the smallest uncovered value and repeat; allocate using the zeros',
   'Minimum cost: add the ORIGINAL costs of the chosen allocation'],
 weDo=[we(6,'14B','Bipartite graphs and allocation','Edrolo 8G WE1'),
   {'n':None,'sub':'14B','title':'Allocation by inspection (no Cambridge Example)','youTry':'Edrolo 8G WE2','video':'Cambridge GO · 14B Resources'},
   {'n':None,'sub':'14B','title':'The Hungarian algorithm (no Cambridge Example: Cambridge works one in the text)','youTry':'Edrolo 8G WE3','video':'Cambridge GO · 14B Resources'}],
 apk=[sk('8B',5,'I can use an adjacency matrix to represent a graph.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7B Q16','text':f'Adapted from VCAA 2017 Exam 1 {N} Q3 (92%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q36','14A'),('Exam 1','VCAA 2025 Exam 1 Q20','7B'),
   ('Exam 2','VCAA 2024 Exam 2 Q14a','14A'),('Exam 2','VCAA 2025 Exam 2 Q4a','2A')),
 exit=[ex('Edrolo U3&4 8G Q10',f'VCAA 2016 Exam 1 {N} Q1'),ex('Edrolo U3&4 8G Q11',f'VCAA 2020 Exam 2 {N} Q2'),
   ex('Edrolo U3&4 8G Q13',f'VCAA 2018 Exam 1 {N} Q8')],
 cas=[],
 note='Spare exit (not reserved): Edrolo 8G Q12 (VCAA 2017 E2 N&DM Q2a).')

C['gm12-u4-14c']=dict(
 keyVocab=['Activity network: a directed graph where each edge is an activity (label, duration) and vertices are the points where activities start/finish',
   'Immediate predecessor: an activity that must be finished just before another can start',
   'Precedence table: lists each activity and its immediate predecessors',
   'Dummy activity: a dashed edge of duration 0, used when two activities share some, but not all, of their immediate predecessors',
   'Every network has one start and one finish vertex'],
 weDo=[we(7,'14C','Drawing an activity network from a precedence table','Edrolo 8H WE2'),
   we(8,'14C','Using a dummy activity in an activity network','Edrolo 8H WE4'),
   we(9,'14C','Creating a precedence table from an activity network','Edrolo 8H WE3')],
 apk=[{'kind':'Exam','ref':'Edrolo U1&2 7D Q12','text':f'Adapted from VCAA 2018 Exam 1 {N} Q4 (88%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q39','14B'),('Exam 1','VCAA 2024 Exam 1 Q28','10D'),
   ('Exam 2','VCAA 2024 NHT Exam 2 Q14a','14B'),('Exam 2','VCAA 2025 Exam 2 Q8b','7B')),
 exit=[ex('Edrolo U3&4 8H Q14',f'Adapted from VCAA 2017 Exam 2 {N} Q4a'),ex('Edrolo U3&4 8H Q15',f'Adapted from VCAA 2020 Exam 2 {N} Q5a')],
 cas=[],
 note='Edrolo 8H WE1 (reading a precedence table) is a spare You try. Both exits are Edrolo-adapted VCAA items (pill: adapted).')

C['gm12-u4-14d']=dict(
 keyVocab=['Earliest start time (EST): forward scan; EST = the largest (EST + duration) over its immediate predecessors',
   'Minimum completion time: the EST at the finish = the length of the longest path',
   'Latest start time (LST): backward scan from the finish; LST = the smallest LST of the following activities − its duration',
   'Float time = LST − EST: how long an activity can be delayed without delaying the project',
   'Critical path: the activities with zero float; any delay on it delays the whole project'],
 weDo=[we(10,'14D','Finding the critical path from a precedence table','Edrolo 8I WE1 (network from weighted table) + WE2 (EST)'),
   we(11,'14D','Finding the critical path','Edrolo 8I WE3 (LST) + WE4 (float, critical path)')],
 apk=[{'kind':'Exam','ref':'Edrolo U1&2 7E Q13','text':f'Adapted from VCAA 2021 Exam 2 {N} Q2a (85%)'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q38','14C'),('Exam 1','VCAA 2025 Exam 1 Q13','5C'),
   ('Exam 2','VCAA 2023 Exam 2 Q14a','14C'),('Exam 2','VCAA 2023 Exam 2 Q9d','10F')),
 exit=[ex('Edrolo U3&4 8I Q15',f'VCAA 2020 Exam 1 {N} Q6'),ex('Edrolo U3&4 8I Q16',f'VCAA 2018 Exam 2 {N} Q3a,d'),
   ex('Edrolo U3&4 8I Q17',f'VCAA 2021 Exam 1 {N} Q6')],
 cas=[],
 note='APK primes shortest path (the critical path is the longest path). Spare exit (not reserved): Edrolo 8I Q18 (VCAA 2021 E2 N&DM Q4a,b).')

C['gm12-u4-14e']=dict(
 keyVocab=['Crashing: reducing the duration of one or more activities to reduce the completion time of the project',
   'Only crashing activities on the critical path can shorten the project; once another path becomes as long, it is critical too',
   'Crashing with cost: reduce the cheapest critical activities first; stop when no further saving is possible or the budget runs out'],
 weDo=[we(12,'14E','Crashing one activity with cost','Edrolo 8J WE1'),
   we(13,'14E','Crashing multiple activities with cost','Edrolo 8J WE2')],
 apk=[],
 doNow=dn(('Exam 1','VCAA 2024 NHT Exam 1 Q40','14D'),('Exam 1','VCAA 2023 Exam 1 Q31','11E'),
   ('Exam 2','VCAA 2024 Exam 2 Q15a','14D'),('Exam 2','VCAA 2024 Exam 2 Q6a','7F')),
 exit=[ex('Edrolo U3&4 8J Q9',f'VCAA 2017 Exam 2 {N} Q4ci,ii'),ex('Edrolo U3&4 8J Q10',f'VCAA 2020 Exam 1 {N} Q10'),
   ex('Edrolo U3&4 8J Q11',f'VCAA 2021 Exam 2 {N} Q4c')],
 cas=[],
 note='No APK: crashing has no Units 1&2 prerequisite (the Do Now retrieves 14D critical path). Spare exit (not reserved): Edrolo 8J Q12 (VCAA 2019 E2 N&DM Q3e).')

for i,c in C.items():
    card=L[i]['card']
    for k in ['keyVocab','weDo','apk','doNow','exit','cas','note']: card[k]=c[k]
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# ---------- written You trys (checked with networkx max flow, 16 Nov) ----------
Wf='planner/written-youtrys.json'; w=json.load(open(Wf))
lab=lambda n:f'Written for 12MAG (Claude, modelled on Cambridge Example {n})'
new=[
 {'id':'YT-14A-4','pairs':'Cambridge U3&4 Example 4','sub':'14A','label':lab(4),
  'figure':{'type':'digraph','source':'A','sink':'G','edges':[['A','B',14],['A','D',18],['A','E',7],['B','C',9],['B','D',6],['C','G',11],['D','C',4],['D','G',10],['D','F',8],['E','F',12],['F','G',20]]},
  'text':'A wildlife park allows visitors to walk through the park along one-way tracks. The park is represented by the network below, where the direction of travel on each track is shown by an arrow. The numbers on the edges indicate the maximum number of people who are permitted to walk along each track each hour.\na Starting at A, how many people are permitted to walk to G each hour?\nb Given that one group of eight people would like to walk from A to G together as a group, list all the different routes they could take so that the entire group of eight will stay together for the duration of their walk.\nc What is the largest group of people that could walk through the wildlife park if they must stay together in a group for the entire duration of the walk?',
  'answer':'a 36 people per hour. Minimum cut: C→G 11, D→G 10, D→F 8 and A→E 7: 11 + 10 + 8 + 7 = 36.\nb A–B–C–G (smallest capacity 9), A–D–G (10), A–D–F–G (8).\nc 10 people (route A–D–G).'},
 {'id':'YT-14A-5','pairs':'Cambridge U3&4 Example 5','sub':'14A','label':lab(5),
  'figure':{'type':'digraph','sources':['Source 1','Source 2'],'sinks':['Outlet 1','Outlet 2'],'edges':[['Source 1','P',500],['Source 1','Q',300],['Source 2','Q',200],['Source 2','R',400],['P','Outlet 1',350],['P','Q',150],['Q','Outlet 1',250],['Q','R',100],['Q','Outlet 2',200],['R','Outlet 2',450]]},
  'text':'Water enters a network of pipes at either Source 1 or Source 2 and flows out at either Outlet 1 or Outlet 2.\nThe numbers next to the arrows represent the maximum rate, in kilolitres per minute, at which water can flow through each pipe.\nDetermine the maximum rate, in kilolitres per minute, at which water can flow from these pipes at Outlet 1 and at Outlet 2.',
  'answer':'Outlet 1: minimum cut through the two pipes into Outlet 1: 350 + 250 = 600 kilolitres per minute.\nOutlet 2: minimum cut through the two pipes into Outlet 2: 200 + 450 = 650 kilolitres per minute.\n(These cannot simply be added: both outlets may not reach their maximum at the same time.)'},
]
have={x['id'] for x in w['items']}
for x in new:
    if x['id'] in have: w['items']=[y for y in w['items'] if y['id']!=x['id']]
    w['items'].append(x)
json.dump(w,open(Wf,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('14A','Flow problems'),('14B','Matching and allocation problems'),('14C','Precedence tables and activity networks'),
            ('14D','Scheduling problems'),('14E','Crashing')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

def nm(s): return s.replace('Adapted from ','').replace('Exam ','E').replace(N,'Networks')
rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((nm(x['src']),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((nm(x['text'].split(' (')[0]),x['ref'],'APK',i))
        else:
            sec,num=x['ref'].split()[2],x['ref'].split()[-1].lstrip('#')
            rows.append((f'Cambridge U1&2 skills checklist {sec} {num}','','APK',i))
M='tools/ledger_manual.csv'
old=open(M).read()
items_old={r['item'] for r in csv.DictReader(open(M)) if r.get('burnt')=='yes'}
L2={r['item'] for r in csv.DictReader(open('tools/ledger.csv')) if r.get('burnt')=='yes'}
clash=[]
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if item in items_old or item in L2: clash.append(item); print('ALREADY IN LEDGER:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS4 prefill'])
print('ok', len(rows), 'clashes', clash)
