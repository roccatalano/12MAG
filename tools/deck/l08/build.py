"""Lesson l08 (2I) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2I slides.html
Run: python3 tools/deck/l08/build.py      Screenshots: python3 tools/deck/l08/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values from the source tables):
- Do Now (planner card): VCAA 2023 Exam 1 Q10 (A, 59%; B 9 C 5 D 22 E 4) · VCAA 2026 Exam 1 Q5 (B; 2026 report not yet released) ·
          VCAA 2024 Exam 2 Q3c (86.8%; 57% full marks; Table 2 + scatterplot shared with l07 Do Now 3) ·
          VCAA 2024 NHT Exam 2 Q2b (Table 3/4; NHT report gives the answer only, no %).
- APK: none on the planner card. Exits: none (Rocco, 15 Nov: Q2).
- Learn: Cambridge Units 3&4 2I p. 155 (guideline table; own words; flowchart drawn for 12MAG).
  Learning intentions / success criteria: written for 12MAG (the textbook prints none for 2I).
- Coursework: planner card (Cambridge Exercise 2I Q1-3 + revision booklet).
- Videos: videos.json (2I MaffsGuru link still blank).
"""
import os, sys, json, importlib.util
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
_s=importlib.util.spec_from_file_location('f7',os.path.join(H,'..','l07','figs.py')); f7=importlib.util.module_from_spec(_s); _s.loader.exec_module(f7)
SC,W_,WYR,WGOLD,WBEST=f7.scat,f7.W_,f7.WYR,f7.WGOLD,f7.WBEST
CAM='Cambridge General Mathematics Units 3&amp;4'

def _card(o,i):
    if isinstance(o,dict):
        if o.get('id')==i: return o['card']
        for v in o.values():
            r=_card(v,i)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=_card(v,i)
            if r: return r
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l08')
yid=lambda u:u.split('v=')[1].split('&')[0]
LI=[x.split(' (written')[0]+'.' if '(written' in x else x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x for g in CARD['successCriteria'] for x in g['items']]

S=['<style>.sm .L .q{font-size:17px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}'
   '.fc{display:flex;flex-direction:column;align-items:center;gap:10px;font-size:22px}.fc .nd{border:2px solid var(--ink);border-radius:10px;padding:8px 16px;background:#fff;font-weight:700;text-align:center}'
   '.fc .row{display:flex;gap:14px;align-items:flex-start;justify-content:center}.fc .br{display:flex;flex-direction:column;align-items:center;gap:8px;width:360px}'
   '.fc .lab{font-size:17px;color:var(--muted)}.fc .gr{background:#c8e6c9}.fc .q2{background:#fff3c4}</style>']
# ================= opening
S.append(title(8,'Which graph?',f'{CAM} · 2I Which graph?','L08',flow=('Do Now','Learn','Check-in','Coursework')))
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('Types of variables','',None),('Which graph?','· the guidelines',None),
  ('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Categorical variable','data that are labels or groups (e.g. sex, school type, yes/no)'),
  ('Numerical variable','data that are counts or measurements (e.g. height, income)'),
  ('Explanatory variable (EV)','the variable we expect to explain or predict the RV'),
  ('Response variable (RV)','the variable that responds: the one we want to predict')],
  [('Two categorical','segmented bar chart','from a percentaged two-way table'),
   ('Numerical RV, categorical EV','parallel boxplots · parallel dot plots','two categories: back-to-back stem plot too'),
   ('Two numerical','scatterplot','EV on the horizontal axis')],
  f'{CAM}, 2I p. 155'))

# ================= Do Now 1: VCAA 2023 E1 Q10 (2H)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2023 Exam 1 Q10','Review of 2G–2H',
  '<div style="font-size:22px">A study of Year 10 students shows that there is a negative association between the scores of topic tests and the time spent on social media. The coefficient of determination is 0.72<br>From this information it can be concluded that</div>',
  [('Direction','negative: as one goes down, the other goes up (C, E ✗)'),
   ('Association, not cause','an observational study shows association only: never “causes” (B, D ✗)')],
  'Less time on social media is associated with higher test scores: <b>A</b>.','VCAA 2023 General Mathematics Exam 1 Q10 (examiner report)',
  mc=['a decreased time spent on social media is associated with an increased topic test score.','less time spent on social media causes an increase in topic test performance.',
      'an increased time spent on social media is associated with an increased topic test score.','too much time spent on social media causes a reduction in topic test performance.',
      'a decreased time spent on social media is associated with a decreased topic test score.'],key='A',dist=[59,9,5,22,4],
  dis=('D','22% chose “causes”: a correlation (or r²) can never show cause.')))
# ================= Do Now 2: VCAA 2026 E1 Q5 (1H)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2026 Exam 1 Q5','Review of 1H',
  '<div style="font-size:21px">Students at a large secondary college completed two tests: test A and test B.<br>The marks for these two tests were both modelled by a normal distribution:<ul class="bul" style="margin-left:22px"><li>For test A, the mean mark was 68.</li><li>For test B, the mean mark was 64.</li></ul>'
  'A student, Jared, scored 55 on both tests.<br>The standardised score (<i>z</i>-score) of Jared’s mark for test B was 1.0 greater than the standardised score (<i>z</i>-score) of Jared’s mark for test A.<br>The standard deviation of the marks for test A was 5.5<br>The standard deviation of the marks for test B was closest to</div>',
  [fx('z-score, test A','<i>z</i>',F(FR(F(V('x','55'),' − ',V('x̄','68')),V('s','5.5'))),'−2.364'),
   ('z-score, test B','−2.364 + 1.0 = −1.364'),
   fx('Solve for s','<i>s</i>',F(FR(F(V('x','55'),' − ',V('x̄','64')),V('z','−1.364'))),'6.6')],
  'The standard deviation for test B ≈ 6.6: <b>B</b>.','VCAA 2026 General Mathematics Exam 1 Q5 (2026 examiner report not yet released)',
  mc=['6.2','6.6','6.9','7.3'],key='B',stat=('new',)))
# ================= Do Now 3: VCAA 2024 E2 Q3c (2G)
WT='<table class="t tight" style="font-size:12px"><tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y in WYR)+'</tr><tr><th><i>Wgold</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WGOLD)+'</tr><tr><th><i>Wbest</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WBEST)+'</tr></table>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q3c','Review of 2G',
  '<div style="font-size:15.5px">The Olympic gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, is often lower than the best height achieved in other international women’s high jump competitions in that same year.<br>Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.</div>'
  f'<div style="margin:5px 0">{WT}</div><div style="display:flex;gap:10px;align-items:center"><div style="flex:none;width:300px">'+SC(list(zip(WGOLD,WBEST)),(1.90,2.08),(1.92,2.10),0.02,0.02,'Wgold (m)','Wbest (m)',W=400,H=260,r=4.5,fs=11)+'</div>'
  '<div style="font-size:15.5px">When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em><br><span id="d3r">The correlation coefficient is 0.9318</span><br>'
  'c. Determine the value of the coefficient of determination as a percentage.<br>Round your answer to one decimal place. <span class="muted">(1 mark)</span></div></div>',
  [fx('Coefficient of determination','<i>r</i>²',F(V('r','0.9318'),'²'),'0.86825…'),('Percentage','0.86825 × 100 = 86.825… → 86.8% (1 d.p.)')],
  '<i>r</i>² = <b>86.8%</b>','VCAA 2024 General Mathematics Exam 2 Q3c (examiner report; scatterplot redrawn)',stat=('mark',57),cmd=('Determine',1,'square r, then %')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2024 NHT E2 Q2b (2B)
LLT=['on','before','before','after','after','after','after','after','after','after','after','after']
HHT=['on','before','before','before','after','after','after','on','on','after','after','after']
def t3(name,vals,k):
    return (f'<table class="t tight" id="t3{k}" style="font-size:14px;margin-bottom:6px"><tr><th rowspan="2" style="width:60px"><i>{name}</i></th>'+''.join(f'<td><span data-i="{v}">{v}</span></td>' for v in vals[:6])+'</tr><tr>'+
            ''.join(f'<td><span data-i="{v}">{v}</span></td>' for v in vals[6:])+'</tr></table>')
B=lambda c,v:f'<span class="blank {c}"><span class="ph">&nbsp;</span><span class="fill">{v}</span></span>'
T4Q=('<table class="t tight" style="font-size:14px"><tr><th>Occurrence</th><th><i>LLT</i></th><th><i>HHT</i></th></tr>'
     +''.join(f'<tr><th>{o}</th><td style="min-width:70px">&nbsp;</td><td style="min-width:70px">&nbsp;</td></tr>' for o in ('before','on','after'))+'<tr><th>Total</th><td>12</td><td>12</td></tr></table>')
T4=('<table class="t" style="font-size:16px"><tr><th>Occurrence</th><th><i>LLT</i></th><th><i>HHT</i></th></tr>'
    f'<tr><th>before</th><td>{B("f1","2 (16.7%)")}</td><td>3</td></tr><tr><th>on</th><td>{B("f2","1 (8.3%)")}</td><td>3</td></tr>'
    f'<tr><th>after</th><td>{B("f3","9 (75%)")}</td><td>6</td></tr><tr><th>Total</th><td>12</td><td>12</td></tr></table>')
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 NHT Exam 2 Q2b','Review of 2B',
  '<div style="font-size:15px">In the year 2021 there were 12 days where a new moon appeared in Sydney Harbour.<br>For these 12 days the occurrence of the highest high tides (<em class="v">HHT</em>) and lowest low tides (<em class="v">LLT</em>) occurred before, on or after the appearance of the new moon.<br>These records are displayed in the table below.</div>'
  f'<div style="font-weight:700;font-size:14px;margin-top:4px">Table 3</div>{t3("LLT",LLT,"a")}{t3("HHT",HHT,"b")}'
  f'<div style="display:flex;gap:14px;align-items:center"><div><div style="font-weight:700;font-size:14px">Table 4</div>{T4Q}</div>'
  '<div style="font-size:15px">b. Does the data in Table 4 support the contention that the occurrence of the <em class="v">LLT</em> is associated with the appearance of the new moon?<br>Explain your conclusion by comparing the values of appropriate percentages. <span class="muted">(2 marks)</span></div></div>',
  [('TMPL',T4),
   ('LLT before','2 of 12 = 16.7%','data-hi="#t3a|before|hy" data-fill="f1"'),
   ('LLT on','1 of 12 = 8.3%','data-hi="#t3a|on|hc" data-fill="f2"'),
   ('LLT after','9 of 12 = 75%','data-hi="#t3a|after|hg" data-fill="f3"'),
   ('Compare','the percentages differ a lot across before / on / after → association')],
  'Yes. The <em>LLT</em> occurred after the new moon on 75% of the days, compared with 8.3% on the new moon and 16.7% before it. The percentages differ, so the data support an association.',
  'VCAA 2024 (NHT) General Mathematics Exam 2 Q2b (NHT report: answer only, no %)',stat=('nht',),cmd=('Explain',2,'compare %')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)

# ================= Learn: two questions
S.append(learn('Learn · 2I','Before you draw: two questions',
  '<h4>Ask first</h4><ol style="font-size:20px;margin-left:24px;line-height:1.6"><li>Is each variable <b>categorical</b> or <b>numerical</b>?</li><li>Which is the <b>RV</b> and which is the <b>EV</b>?</li></ol>',
  '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;font-size:22px">'
  '<div class="key frag"><h4>Both categorical</h4>vegetarian (yes, no) and sex (male, female)</div>'
  '<div class="key frag"><h4>One of each</h4>hours at the beach and state of residence</div>'
  '<div class="key frag"><h4>Both numerical</h4>test mark and hours spent studying</div></div>',
  'The type of variable, not the topic, decides the graph.',f'{CAM}, 2I p. 155 (examples from Exercise 2I Q1 variable pairs)',
  cards=(kcard('Categorical','labels or groups'),kcard('Numerical','counts or measurements'))))
# ================= Learn: which graph (flowchart, top-down one branch at a time)
FC=('<div class="fc"><div class="nd frag q2">What types are the RV and EV?</div><div class="row">'
    '<div class="br"><div class="lab frag">both categorical</div><div class="nd gr frag">Segmented bar chart</div><div class="lab frag">from a percentaged two-way table</div></div>'
    '<div class="br"><div class="lab frag">RV numerical · EV categorical</div><div class="nd frag q2">How many categories?</div>'
    '<div class="lab frag">two</div><div class="nd gr frag">Back-to-back stem plot, parallel dot plots or parallel boxplots</div>'
    '<div class="lab frag">three or more</div><div class="nd gr frag">Parallel boxplots, parallel dot plots</div></div>'
    '<div class="br"><div class="lab frag">both numerical</div><div class="nd gr frag">Scatterplot</div><div class="lab frag">EV on the horizontal axis</div></div></div></div>')
S.append(learn('Learn · 2I','Which graph?',
  '<h4>The guidelines</h4><p style="font-size:19px">Match the graph to the types of variables. They are guidelines only: sometimes more than one graph is suitable.</p>',
  FC,'A histogram, a single dot plot or a single stem plot shows ONE variable: never the answer for an association.',f'{CAM}, 2I p. 155 (table redrawn as a flowchart)'))
# ================= Learn: summary table
TB=('<table class="t" style="font-size:19px;margin:auto"><tr><th>Response variable</th><th>Explanatory variable</th><th>Graph</th></tr>'
    '<tr class="frag"><td>Categorical</td><td>Categorical</td><td>Segmented bar chart</td></tr>'
    '<tr class="frag"><td>Numerical</td><td>Categorical</td><td>Parallel boxplots, parallel dot plots</td></tr>'
    '<tr class="frag"><td>Numerical</td><td>Categorical (two categories only)</td><td>Back-to-back stem plot, parallel dot plots or parallel boxplots</td></tr>'
    '<tr class="frag"><td>Numerical</td><td>Numerical</td><td>Scatterplot</td></tr></table>')
S.append(learn('Learn · 2I','Summary: type of variables → graph',
  '<h4>Chapter 2 in one table</h4><p style="font-size:19px">Every display from 2A–2F fits one row.</p>',TB,
  'Exam tip: back-to-back stem plots need exactly two categories (e.g. sex, licence type).',f'{CAM}, 2I p. 155'))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 2 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub']=='2I' and v.get('url')]))
n=assemble(S,'12MAG · L08 · Which graph?',os.path.join(ROOT,'lessons','2I slides.html'))
print(n-1,'slides')
