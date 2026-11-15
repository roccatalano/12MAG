"""Prefill the Chapter 3 lesson cards (l09-l11) - queue task Ch3 #1, 15 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 3 (Examples 1-8, CAS 1, CAS 2, Exercises 3A-3C, Skills checklist),
Edrolo U3&4 2023 3A-3C worked examples (3A WE1-4, 3B WE1-3, 3C WE1-3) and exam practice (3A Q13-15, 3B Q11-13, 3C Q11, Q13, Q14),
Edrolo U1&2 2023 6C/6D worked examples (only line-of-good-fit and slope interpretation: no match for Ex 2, 5, 8),
tools/vcaa_current_index.csv (Do Now), tools/ledger*.csv (burnt), tools/y11_cambridge_skills_checklist.csv (APK).
"""
import json
P='planner/unit-plan.json'; d=json.load(open(P))
L={l['id']:l for l in d['aos'][0]['chapters'][2]['lessons']}
def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
DN={
'gm12-u3-l09':dn(('Exam 1','VCAA 2024 Exam 1 Q14','1F'),('Exam 1','VCAA 2026 NHT Exam 1 Q11','2H'),('Exam 2','VCAA 2023 Exam 2 Q3b','2G'),('Exam 2','VCAA 2026 Exam 2 Q3c','1H')),
'gm12-u3-l10':dn(('Exam 1','VCAA 2023 Exam 1 Q7','3A'),('Exam 1','VCAA 2025 NHT Exam 1 Q2','1B'),('Exam 2','VCAA 2023 Exam 2 Q3a','3A'),('Exam 2','VCAA 2023 Exam 2 Q2aii','1B')),
'gm12-u3-l11':dn(('Exam 1','VCAA 2023 Exam 1 Q9','3B'),('Exam 1','VCAA 2026 NHT Exam 1 Q9','2F'),('Exam 2','VCAA 2024 Exam 2 Q3e','3B'),('Exam 2','VCAA 2023 Exam 2 Q1cii','2A')),
}
YT={1:'Edrolo 3A WE3',2:'Written (modelled on Cambridge Ex 2) · YT-3A-2',3:'Edrolo 3B WE1',4:'Edrolo 3B WE2',
    5:'Written (modelled on Cambridge Ex 5) · YT-3B-5',6:'Edrolo 3C WE2',7:'Edrolo 3C WE3',8:'Written (modelled on Cambridge Ex 8) · YT-3B-8'}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
HW={
'gm12-u3-l09':[hw('3A',[('Basic ideas','Q1–3'),('Least squares line from summary statistics','Q4–6'),('r from the slope','Q7–9'),('Least squares line on CAS','Q10–13'),('Exam 1 style questions','Q14–16')])],
'gm12-u3-l10':[hw('3B',[('Interpreting the intercept and slope','Q1–3'),('Making predictions','Q4–6'),('Comparing associations with r²','Q7')])],
'gm12-u3-l11':[hw('3B',[('Residuals','Q8–10'),('Interpreting residual plots','Q11'),('Regression analysis','Q12–15'),('Reporting a regression analysis','Q16–17'),('Exam 1 style questions','Q18–20')]),
               hw('3C',[('Regression analysis from data on CAS','Q1–3')])],
}
APK={'gm12-u3-l11':[
 {'kind':'Skill','ref':'Cambridge U1&2 5A checklist #1','text':'Substitute values into linear equations and formulas'},
 {'kind':'Skill','ref':'Cambridge U1&2 5E checklist #8','text':'Find the intercept and slope of a straight line from its equation'},
 {'kind':'Exam','ref':'Edrolo U1&2 6D Q14','text':'adapted from VCAA 2017 Exam 1 Q8'},
 {'kind':'Exam','ref':'Edrolo U1&2 6D Q15','text':'adapted from VCAA 2016 Exam 2 Q3bii'}]}
CAS={'gm12-u3-l09':['lsrl'],'gm12-u3-l10':['lsrl-predict'],'gm12-u3-l11':['residuals','regression-analysis']}
for i,l in L.items():
    if i not in DN: continue
    c=l['card']; c['doNow']=DN[i]
    for w in c.get('weDo',[]): w['youTry']=YT.get(w['n'])
    rb={'title':'Revision book','items':[],'note':'The '+', '.join(sorted({s for s in ['3A','3B','3C'] if s in json.dumps(HW[i])}))+' sections'}
    c['homework']={'source':'prefill','sets':HW[i]+[rb]}
    c['cas']=CAS[i]
    if i in APK: c['apk']=APK[i]
L['gm12-u3-l09']['card']['casYouTry']='Edrolo 3A WE1 (least squares line on CAS)'
L['gm12-u3-l09']['card']['note']='Edrolo 3A WE2 (estimate the line from a scatterplot) and WE4 (sketch the line from its equation) have no Cambridge Example: spare You trys if wanted.'
L['gm12-u3-l10']['card']['note']='Edrolo 3B WE3 (rearranging the equation to predict the EV) is a spare You try for Example 4.'
L['gm12-u3-l11']['card']['casYouTry']='Cambridge 3C CAS 2 data (no Edrolo CAS worked example for a full regression analysis)'
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False); print('ok')
