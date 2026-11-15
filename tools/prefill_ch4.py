"""Prefill the Chapter 4 lesson cards (l12-l15) - queue task Ch4 #1, 15 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 4 (Examples 1-7, CAS 1-3, Exercises 4A-4D, Skills checklist),
Edrolo U3&4 2023 3D (WE1-4: transformation wave, x^2, log x, 1/y) and 3E (WE1a-d: y^2, log x, 1/x, best r^2; WE2a-c predictions),
exam practice 3D Q14, 3E Q10-13; Edrolo U1&2 2023 8A-8D (variation, x-transformations only: no log y WE),
tools/vcaa_current_index.csv (Do Now), tools/ledger*.csv (burnt, re-read from origin), tools/y11_cambridge_skills_checklist.csv (APK).
Changes to the existing draft cards: l12 Do Now VCAA 2023 E1 Q6 (burnt, S4) -> 2024 E1 Q10 (3B, 73%);
l14 Do Now VCAA 2024 NHT E1 Q12 (tagged 4D = l15 content) -> 2025 E1 Q12 (4A, 61%); 2026 E1 Q7 sec 2H -> 2E (index tag).
Cambridge Ex 4 (log y): no Edrolo U3&4 or U1&2 WE -> written YT-4B-4.
"""
import json
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for ch in d['aos'][0]['chapters']:
    for l in ch['lessons']: L[l['id']]=l
def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
DN={
'gm12-u3-l12':dn(('Exam 1','VCAA 2024 NHT Exam 1 Q10','3C'),('Exam 1','VCAA 2024 Exam 1 Q10','3B'),('Exam 2','VCAA 2024 NHT Exam 2 Q4e','3C'),('Exam 2','VCAA 2023 Exam 2 Q2bii','2B')),
'gm12-u3-l13':dn(('Exam 1','VCAA 2024 NHT Exam 1 Q11','4A'),('Exam 1','VCAA 2026 Exam 1 Q7','2E'),('Exam 2','VCAA 2024 NHT Exam 2 Q4a','3A'),('Exam 2','VCAA 2023 Exam 2 Q1d','3A')),
'gm12-u3-l14':dn(('Exam 1','VCAA 2024 Exam 1 Q11','4B'),('Exam 1','VCAA 2025 Exam 1 Q12','4A'),('Exam 2','VCAA 2026 Exam 2 Q5g','4B'),('Exam 2','VCAA 2024 Exam 2 Q3f','3C')),
'gm12-u3-l15':dn(('Exam 1','VCAA 2023 Exam 1 Q11','4C'),('Exam 1','VCAA 2025 Exam 1 Q11','4B'),('Exam 2','VCAA 2026 NHT Exam 2 Q1a','1A'),('Exam 2','VCAA 2024 NHT Exam 2 Q1ai','1F')),
}
YT={1:'Edrolo 3D WE2',2:'Edrolo 3E WE1a',3:'Edrolo 3E WE1b',4:'Written (modelled on Cambridge Ex 4) · YT-4B-4',
    5:'Edrolo 3E WE1c',6:'Edrolo 3D WE4',7:'Edrolo 3E WE1d'}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
HW={
'gm12-u3-l12':[hw('4A',[('Prerequisite skills','Q1'),('x² transformation on CAS','Q2–3'),('y² transformation on CAS','Q4–5'),('Applications','Q6–7'),('Exam 1 style questions','Q8–10')])],
'gm12-u3-l13':[hw('4B',[('Prerequisite skills','Q1'),('log x transformation on CAS','Q2–3'),('log y transformation on CAS','Q4–5'),('Applications','Q6–7'),('Exam 1 style questions','Q8–10')])],
'gm12-u3-l14':[hw('4C',[('Prerequisite skills','Q1'),('1/x transformation on CAS','Q2'),('1/y transformation on CAS','Q3–4'),('Applications','Q5–6'),('Exam 1 style questions','Q7–9')])],
'gm12-u3-l15':[hw('4D',[('Choosing transformations (circle of transformations)','Q1'),('Choosing and applying the best transformation','Q2–4')])],
}
NOTE={
'gm12-u3-l12':'No Edrolo exam-practice questions on the squared transformation, so no exits. Spare You trys: Edrolo 3E WE2a (prediction from (distance)²). CAS You try: Cambridge CAS 1 data.',
'gm12-u3-l13':'Spare You trys: Edrolo 3D WE3 (log x, plot only), 3E WE2b (prediction). CAS You try: Cambridge CAS 2 data.',
'gm12-u3-l14':'Spare You try: Edrolo 3E WE2c (prediction from 1/week). CAS You try: Cambridge CAS 3 data.',
'gm12-u3-l15':'Spare You try: Edrolo 3D WE1 (transformation wave: which transformations could linearise).',
}
for i in DN:
    c=L[i]['card']; c['doNow']=DN[i]
    for w in c.get('weDo',[]): w['youTry']=YT.get(w['n'])
    sub=L[i]['subchapters'][0]
    c['homework']={'source':'prefill','sets':HW[i]+[{'title':'Revision book','items':[],'note':f'The {sub} section'}]}
    c['note']=NOTE[i]
# l13 APK 1 -> 9D #9 and exit 3E Q12a-b set in a follow-up edit (9D #6 burnt in S2; 2017 E2 Q4cii = l09 APK)
L['gm12-u3-l13']['card']['apk'][2]['text']='adapted from VCAA 2017 Exam 1 Q4 (log scale)'
for i,n in [('gm12-u3-l12','Cambridge 4A CAS 1 data (squared transformation)'),('gm12-u3-l13','Cambridge 4B CAS 2 data (lifespan vs log GDP)'),('gm12-u3-l14','Cambridge 4C CAS 3 data (reciprocal transformation)')]: L[i]['card']['casYouTry']=n
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

W='planner/written-youtrys.json'; w=json.load(open(W))
if not any(x['id']=='YT-4B-4' for x in w['items']):
    w['items'].append({'id':'YT-4B-4','pairs':'Cambridge U3&4 Example 4','sub':'4B','label':'Written for 12MAG (Claude, modelled on Cambridge Example 4)',
     'text':'The number of followers of a new social media account was recorded over a 10 week period. The association is not linear.\nweek: 1 2 3 4 5 6 7 8 9 10\nfollowers: 15 22 36 51 80 118 190 276 440 650\na Apply a log transformation to the variable followers, and determine the least squares regression line for the transformed data.\nb Use the least squares equation to predict the followers in week 11.',
     'answer':'a log(followers) = 0.989 + 0.183 × week (r² = 0.9996). b log(followers) = 0.989 + 0.183 × 11 = 3.002; 10^3.002 = 1005 followers (to the nearest whole number).'})
    json.dump(w,open(W,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
for s,t in [('4A','The squared transformation'),('4B','The log transformation'),('4C','The reciprocal transformation'),('4D','Choosing and applying the appropriate transformation')]:
    if not any(x['sub']==s for x in v['videos']):
        v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

C='planner/cas-skills.json'; c=json.load(open(C))
sk={x['id']:x for x in c['skills']} if isinstance(c,dict) else {x['id']:x for x in c}
t=sk['transformed-lsrl']
if not t['ti']:
    t['ti']=['Lists & Spreadsheet: enter the data in named lists (e.g. lifespan, gdp).',
      'Name a new column for the transformed variable (e.g. lgdp) and in its formula cell type =log(gdp) (or =gdp^2, =1/gdp).',
      'Add Data & Statistics: plot the RV against the transformed variable (check the plot is now linear).',
      'Menu › Analyze › Regression › Show Linear (a+bx). The x in the equation is the transformed variable.',
      'Write the equation in the variable names, e.g. lifespan = 54.3 + 5.59 × log(GDP); substitute to predict (undo a log y or 1/y at the end).']
    t['classpad']=['Statistics app: enter the data in named lists (e.g. Lifespan, GDP).',
      'Name a third list (e.g. logGDP) and in its calculation cell at the bottom type log(GDP) (or GDP^2, 1/GDP).',
      'SetGraph: Scatter, XList = transformed list, YList = RV; draw it and check the plot is linear.',
      'Calc › Regression › Linear Reg with the same lists: read a, b, r²; the x is the transformed variable.',
      'Write the equation in the variable names; substitute to predict (undo a log y or 1/y at the end).']
    t['tip']='Transform only one variable. If you transformed y, the answer from the equation is log y, y² or 1/y: undo it (10^, √, 1/) to get the prediction.'
    t['status']='draft'; t['src']='Cambridge U3&4 4A CAS 1, 4B CAS 2, 4C CAS 3 (not yet checked against 02 Sources\\CAS guides)'
t=sk['transformation-check']
if not t['ti']:
    t['ti']=['Make a column for each transformation to try (x², log x, 1/x or y², log y, 1/y) as in "Fitting a regression line to transformed data".',
      'For each one: Data & Statistics plot, Show Linear (a+bx), turn on Diagnostics to show r².',
      'Menu › Analyze › Residuals › Show Residual Plot: look for no clear pattern.',
      'Choose the transformation with the patternless residual plot and the highest r².']
    t['classpad']=['Make a list for each transformation to try (e.g. x², log x, 1/x).',
      'For each one: Calc › Regression › Linear Reg (XList = transformed list) and read r².',
      'Set Copy Residual to a list, then plot residuals against the transformed list as a scatterplot: look for no clear pattern.',
      'Choose the transformation with the patternless residual plot and the highest r².']
    t['tip']='Use the circle of transformations first to pick the candidates, then let r² and the residual plot decide.'
    t['status']='draft'; t['src']='Cambridge U3&4 4D Example 7 + 3C CAS 2 (not yet checked against 02 Sources\\CAS guides)'
json.dump(c,open(C,'w'),indent=1,ensure_ascii=False)
print('ok')
