"""Prefill the Chapter 13 lesson cards (gm12-u4-13a13b, -13c, -13d13e, -13f) - queue task AoS4 #2, 16 Nov 2026 (runner).
Learning intentions, success criteria, Study Design points and coursework were set by AoS4 #1 and are kept.
Sources checked: Cambridge U3&4 2023 Ch 13 (Examples 1-13), Edrolo U3&4 2023 Ch 8 worked examples (8A WE1-3, 8B WE1-4,
8C WE1-3, 8D WE1-2, 8F WE1-2) and exam practice (8A-8D, 8F), Edrolo U1&2 2023 Ch 7 (7A-7F) worked examples and exam
practice, Cambridge U1&2 Ch 8 (Graphs and networks) skills checklist (#1-15; not in tools/y11_cambridge_skills_checklist.csv),
tools/vcaa_current_index.csv, tools/ledger*.csv (burnt; read from origin 16 Nov 01:40).
Every Cambridge Example has an Edrolo match (Ex 13 connector problem = Edrolo U1&2 7F WE2, Prim's) -> no written You trys.
Same VCAA originals in both Edrolo books are used once only (e.g. 2021 E1 N&DM Q3 = U3&4 8A Q20 = U1&2 7C Q13;
2017 E2 N&DM Q3a = U3&4 8D Q13 = U1&2 7F Q18 -> used as the 13f APK, rule 5). VCAA items cited on Edrolo U3&4 theory
pages (2019 E1 Q4, 2017 E1 Q3, 2018 E1 Q4, 2019 E1 Q5, 2021 E2 Q2a; N&DM) are left unused.
No CAS for Ch 13 (Cambridge prints none).
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
C['gm12-u4-13a13b']=dict(
 keyVocab=['Graph: vertices (dots) joined by edges (lines); a loop joins a vertex to itself',
   'Degree of a vertex: number of edges attached (a loop adds 2); sum of degrees = 2 × number of edges',
   'Simple, connected, complete graphs; isolated vertex, bridge, subgraph; isomorphic graphs (same connections, drawn differently)',
   'Planar graph: can be drawn with no edges crossing; faces = regions, including the outside',
   'Euler’s formula (connected planar graphs): v − e + f = 2',
   'Adjacency matrix: the entry in row i, column j = number of edges joining vertices i and j (a loop counts as 1)'],
 weDo=[we(1,'13A','Graphs','Edrolo 8A WE1'),
   we(2,'13A','Redrawing a graph in planar form','Edrolo 8A WE2a'),
   we(3,'13A','Verifying Euler’s formula','Edrolo 8A WE3a'),
   we(4,'13A','Using Euler’s formula','Edrolo 8A WE3b'),
   we(5,'13B','Drawing a graph from an adjacency matrix','Edrolo 8B WE2'),
   we(6,'13B','Constructing an adjacency matrix','Edrolo 8B WE1')],
 apk=[sk('8A',2,'I can determine the degree of a vertex and the sum of degrees of a graph.'),
   sk('8C',8,'I can verify Euler’s formula.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7A Q13','text':f'VCAA 2017 Exam 1 {N} Q2 (83%)'}],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q30','11E'),('Exam 1','VCAA 2026 Exam 1 Q6','1H'),
   ('Exam 2','VCAA 2025 Exam 2 Q12a','11D'),('Exam 2','VCAA 2024 Exam 2 Q7c','8F')),
 exit=[ex('Edrolo U3&4 8A Q18',f'VCAA 2021 Exam 2 {N} Q1a,b'),ex('Edrolo U3&4 8A Q20',f'VCAA 2021 Exam 1 {N} Q3'),
   ex('Edrolo U3&4 8B Q15',f'VCAA 2019 Exam 1 {N} Q6')],
 cas=[],
 note='Spare exits (not reserved): Edrolo 8A Q19 (VCAA 2020 E2 N&DM Q1b, 58%), 8B Q14 (VCAA 2020 E1 N&DM Q8, 75%), 8B Q16 (VCAA 2021 E1 N&DM Q7, 33%). Edrolo 8B WE3–WE4 (digraph ↔ adjacency matrix) are spare You trys.')

C['gm12-u4-13c']=dict(
 keyVocab=['Walk: any route along edges; trail: no repeated edges; path: no repeated vertices',
   'Circuit: a trail that starts and ends at the same vertex; cycle: a path that starts and ends at the same vertex',
   'Eulerian trail: uses every edge exactly once (connected, exactly two odd-degree vertices: start at one, end at the other)',
   'Eulerian circuit: uses every edge exactly once and returns to the start (connected, all vertices even)',
   'Hamiltonian path: visits every vertex exactly once; Hamiltonian cycle: also returns to the start'],
 weDo=[we(7,'13C','Identifying types of walks','Edrolo 8C WE1'),
   we(8,'13C','Eulerian and Hamiltonian travel','Edrolo 8C WE2 (Eulerian) + WE3 (Hamiltonian)')],
 apk=[sk('8B',3,'I can identify a connected graph and a bridge.'),
   sk('8D',9,'I can classify a walk as either a trail, path, circuit or cycle.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7D Q11','text':f'VCAA 2019 Exam 2 {N} Q1bii (93%)'}],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q33','13A'),('Exam 1','VCAA 2025 Exam 1 Q29','11E'),
   ('Exam 2','VCAA 2024 Exam 2 Q13a','13A'),('Exam 2','VCAA 2025 Exam 2 Q7b','8C')),
 exit=[ex('Edrolo U3&4 8C Q14',f'VCAA 2019 Exam 2 {N} Q1bi'),ex('Edrolo U3&4 8C Q15',f'VCAA 2019 Exam 1 {N} Q2'),
   ex('Edrolo U3&4 8C Q16',f'VCAA 2018 Exam 2 {N} Q2c')],
 cas=[],
 note='Spare exit (not reserved): Edrolo 8C Q17 (VCAA 2021 E1 N&DM Q5, 17%).')

C['gm12-u4-13d13e']=dict(
 keyVocab=['Weighted graph (network): each edge carries a number (weight), e.g. distance, time or cost',
   'Shortest path: the route between two vertices with the smallest total weight',
   'By inspection: list the possible routes and add their weights',
   'Dijkstra’s algorithm: from the start, repeatedly finalise the closest unvisited vertex, updating the running totals of its neighbours'],
 weDo=[we(9,'13D','Finding the shortest path from one vertex to another','Edrolo 8F WE1'),
   we(10,'13E','Using Dijkstra’s algorithm to find the shortest path in a network','Edrolo 8F WE2')],
 apk=[sk('8G',14,'I can find the shortest path of a weighted network.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7E Q14','text':f'VCAA 2020 Exam 2 {N} Q3a (58%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q34','13C'),('Exam 1','VCAA 2026 NHT Exam 1 Q39','13B'),
   ('Exam 2','VCAA 2024 Exam 2 Q13bi','13C'),('Exam 2','VCAA 2023 Exam 2 Q12bi','13A')),
 exit=[ex('Edrolo U3&4 8F Q10',f'VCAA 2018 Exam 1 {N} Q2'),ex('Edrolo U3&4 8F Q11',f'VCAA 2017 Exam 2 {N} Q1b')],
 cas=[],
 note='Edrolo U1&2 7E WE1–WE2 are spare You trys for Example 9. Edrolo U1&2 7E Q12 (VCAA 2017 E2 N&DM Q1a,b) overlaps exit 2 (Q1b): not used.')

C['gm12-u4-13f']=dict(
 keyVocab=['Tree: a connected graph with no cycles; a tree with n vertices has n − 1 edges',
   'Spanning tree: a subgraph that is a tree and includes every vertex of the graph',
   'Weight of a spanning tree: the sum of the weights of its edges',
   'Minimum spanning tree: the spanning tree with the smallest weight',
   'Prim’s algorithm: start anywhere; keep adding the cheapest edge that joins a new vertex to the tree (no cycles) until all vertices are joined',
   'Minimum connector problem: join all locations as cheaply as possible = find the minimum spanning tree'],
 weDo=[we(11,'13F','Finding the weight of a spanning tree','Edrolo 8D WE1'),
   we(12,'13F','Finding the minimum spanning tree','Edrolo 8D WE2'),
   we(13,'13F','Solving a connector problem','Edrolo U1&2 7F WE2')],
 apk=[sk('8H',15,'I can apply a greedy algorithm such as Prim’s or Kruskal’s algorithm to find a minimum spanning tree in a network.'),
   {'kind':'Exam','ref':'Edrolo U1&2 7F Q18','text':f'VCAA 2017 Exam 2 {N} Q3a (53%; = Edrolo U3&4 8D Q13, used here as APK: rule 5)'}],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q34','13C'),('Exam 1','VCAA 2025 Exam 1 Q38','13E'),
   ('Exam 2','VCAA 2025 Exam 2 Q15b','13A'),('Exam 2','VCAA 2026 NHT Exam 2 Q4c','5B')),
 exit=[ex('Edrolo U3&4 8D Q11',f'VCAA 2018 Exam 1 {N} Q1'),ex('Edrolo U3&4 8D Q12',f'VCAA 2020 Exam 1 {N} Q3')],
 cas=[],
 note='Edrolo U1&2 7F WE1 (draw a tree) and WE3 (Kruskal’s) are spare You trys.')

for i,c in C.items():
    card=L[i]['card']
    for k in ['keyVocab','weDo','apk','doNow','exit','cas','note']: card[k]=c[k]
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('13A','Graphs and networks'),('13B','Adjacency matrices'),('13C','Exploring and travelling'),
            ('13D','Weighted graphs and networks'),('13E','Dijkstra’s algorithm'),('13F','Trees and minimum connector problems')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((x['src'].replace('Exam ','E').replace(N,'Networks'),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((x['text'].split(' (')[0].replace('Exam ','E').replace(N,'Networks'),x['ref'],'APK',i))
        else:
            sec,num=x['ref'].split()[2],x['ref'].split()[-1]
            rows.append((f'Cambridge U1&2 skills checklist {sec} {num}','','APK',i))
M='tools/ledger_manual.csv'
old=open(M).read()
items_old={l.split(',')[0] for l in old.splitlines()}
L2=[l.split(',')[0] for l in open('tools/ledger.csv').read().splitlines()]
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if item in items_old or item in L2: print('ALREADY IN LEDGER:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS4 prefill'])
print('ok', len(rows))
