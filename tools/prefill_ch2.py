"""Prefill the Chapter 2 lesson cards (l03-l08) - queue task 1, 15 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 2 (Examples 1-21, Exercises 2A-2I, Skills checklist p.157),
Cambridge solutions (exercise Q numbers), Edrolo U3&4 2023 (2A-2D and 3C worked examples),
tools/vcaa_current_index.csv (Do Now), tools/ledger.csv (burnt), Cambridge CAS 1/CAS 2 boxes.
"""
import json
P='planner/unit-plan.json'; d=json.load(open(P))
L={l['id']:l for l in d['aos'][0]['chapters'][1]['lessons']}
def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
DN={
'gm12-u3-l03':dn(('Exam 1','VCAA 2024 Exam 1 Q7','1H'),('Exam 1','VCAA 2023 Exam 1 Q5','1H'),('Exam 2','VCAA 2024 Exam 2 Q1ai','1F'),('Exam 2','VCAA 2024 Exam 2 Q1b','1H')),
'gm12-u3-l04':dn(('Exam 1','VCAA 2026 NHT Exam 1 Q5','2B'),('Exam 1','VCAA 2024 Exam 1 Q6','1G'),('Exam 2','VCAA 2023 Exam 2 Q1ci','2A'),('Exam 2','VCAA 2023 Exam 2 Q2bi','2B')),
'gm12-u3-l05':dn(('Exam 1','VCAA 2025 NHT Exam 1 Q11','2C'),('Exam 1','VCAA 2025 NHT Exam 1 Q5','1C'),('Exam 2','VCAA 2025 Exam 2 Q1d','2B'),('Exam 2','VCAA 2023 Exam 2 Q1bii','1F')),
'gm12-u3-l06':dn(('Exam 1','VCAA 2024 Exam 1 Q10','2E'),('Exam 1','VCAA 2024 Exam 1 Q5','1G'),('Exam 2','VCAA 2023 Exam 2 Q3c','2E'),('Exam 2','VCAA 2024 NHT Exam 2 Q1c','1G')),
'gm12-u3-l07':dn(('Exam 1','VCAA 2024 Exam 1 Q9','2F'),('Exam 1','VCAA 2024 NHT Exam 1 Q6','1H'),('Exam 2','VCAA 2025 NHT Exam 2 Q4g','2F'),('Exam 2','VCAA 2024 Exam 2 Q1aii','1F')),
'gm12-u3-l08':dn(('Exam 1','VCAA 2023 Exam 1 Q10','2H'),('Exam 1','VCAA 2026 Exam 1 Q5','1H'),('Exam 2','VCAA 2024 Exam 2 Q3c','2G'),('Exam 2','VCAA 2024 NHT Exam 2 Q2b','2B')),
}
YT={1:'Edrolo U1&2 1A WE1',2:'Edrolo 2C WE1',3:'Edrolo 2C WE2',4:'Edrolo 2A WE1',5:'Edrolo 2A WE4',6:'Edrolo 2A WE2',7:'Edrolo 2A WE3',8:'Edrolo 2A WE5',
    9:'Edrolo 2B WE2',10:'Edrolo 2B WE1',11:'Edrolo 2B WE3',12:'Edrolo 2B WE4',13:'Edrolo U1&2 6B WE3',14:'Edrolo U1&2 6B WE1',15:'Edrolo 2C WE4',16:'Edrolo 2D WE1',
    17:'Edrolo 3C WE1a',18:'Edrolo 3C WE1b',19:None,20:None,21:None}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
HW={
'gm12-u3-l03':[hw('2A',[('Categorical or numerical variables','Q1'),('Explanatory and response variables','Q2–3'),('Exam 1 style questions','Q4–6')]),
               hw('2B',[('Two-way frequency table','Q1'),('Percentaged two-way tables and associations','Q2–5'),('Segmented bar charts','Q6–9'),('Exam 1 style questions','Q10–12')])],
'gm12-u3-l04':[hw('2C',[('Parallel dot plots','Q1'),('Back-to-back stem plots','Q2–3'),('Parallel boxplots','Q4–6'),('Exam 1 style questions','Q7–10')])],
'gm12-u3-l05':[hw('2D',[('Reading a scatterplot','Q1'),('Scatterplots on CAS','Q2–5'),('Exam 1 style questions','Q6')]),
               hw('2E',[('Direction from the variables','Q1'),('Direction, form and strength from a scatterplot','Q2')])],
'gm12-u3-l06':[hw('2F',[('Basic ideas','Q1'),('r using the formula (optional)','Q2'),('r on CAS','Q3'),('Classifying strength from r','Q4')])],
'gm12-u3-l07':[hw('2G',[('r² from r','Q1'),('Calculating and interpreting r²','Q2–3'),('Exam 1 style questions','Q4–8')]),
               hw('2H',[('Correlation and causation','Q1–7'),('Exam 1 style questions','Q8')])],
'gm12-u3-l08':[hw('2I',[('Choosing the graph','Q1–2'),('Exam 1 style questions','Q3')])],
}
CAS={'gm12-u3-l04':['parallel-boxplots'],'gm12-u3-l05':['scatterplot'],'gm12-u3-l06':['correlation-r'],'gm12-u3-l07':['r-and-r2']}
for i,l in L.items():
    if i not in DN: continue
    c=l['card']; c['doNow']=DN[i]
    for w in c.get('weDo',[]): w['youTry']=YT.get(w['n'])
    rb={'title':'Revision book','items':[],'note':'The '+', '.join(l['subchapters'])+' sections'}
    c['homework']={'source':'prefill','sets':HW[i]+[rb]}
    if i in CAS: c['cas']=CAS[i]
c=L['gm12-u3-l05']['card']; c['casYouTry']='Edrolo 2C WE3 (scatterplot on CAS)'
c=L['gm12-u3-l07']['card']; c['note']='2H has no Cambridge Example: Edrolo 2D WE2 (third variable, causation) can be a 2H You try if Rocco wants one.'
L['gm12-u3-l08']['card']['exit']=[]  # Rocco 15 Nov: 2I has no exits
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False); print('ok')
