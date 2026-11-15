"""Lesson l07 (2G-2H) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2G-2H slides.html
Run: python3 tools/deck/l07/build.py      Screenshots: python3 tools/deck/l07/shoot.py

Sources (read from the PDFs on G: 15 Nov 2026; question text verbatim; figures redrawn, values read off the source figures):
- Do Now: VCAA 2025 Exam 1 Q10 (+ shared Q9-10 stem and scatterplot; D, 63%; A 22 B 7 C 8) — REPLACES the card's VCAA 2024 E1 Q9,
          which needs r = b·s_y/s_x from a least squares equation (3A, not yet taught; see QUEUE Decisions log) ·
          VCAA 2024 NHT Exam 1 Q6 (D; NHT report gives no %) ·
          VCAA 2024 Exam 2 Q3d (strong, positive; 78% full marks) — REPLACES the card's VCAA 2025 NHT E2 Q4g, which compares
          r² with r (2G: today's new content, so not retrieval; re-tagged 2G in the index, freed) ·
          VCAA 2024 Exam 2 Q1aii (50%; 77% full marks; report: 54.54% came from including 2.25).
- APK (planner card): Cambridge U1&2 Ch 7 skills checklist 7C #6 (umbrellas; no printed answer: solution written for 12MAG) ·
  VCAA 2019 Further Exam 2 Q4a (= Edrolo U1&2 6A Q15 'adapted'; original VCAA wording; report: 84% full marks; humidity 9 am).
- Learn: Cambridge Units 3&4 2G pp. 146-148, 2H pp. 151-154 (own words; diagrams redrawn).
- CAS: planner/cas-skills.json 'r-and-r2'; data = Cambridge 2F CAS 2 (income / CO2, same as l06): r = 0.818, r² = 0.669.
- Worked examples: Cambridge U3&4 Examples 17-21 (pp. 146-148; Example 21 scatterplot drawn for 12MAG with r = −0.7218).
  You trys: Edrolo U3&4 3C Worked example 1a, 1b (p. 179) · YT-2G-19/20/21 (planner/written-youtrys.json, written for 12MAG) ·
  2H: Edrolo U3&4 2D Worked example 2 (p. 148, no Cambridge Example).
- Exits: Edrolo U3&4 2D Q13 = VCAA 2017 Further Exam 1 Q12 (D, 81%; A 2 B 6 C 10 E 2) · Edrolo 2D Q14 = VCAA 2019 Further Exam 2 Q4c
  (r = 0.871; 76% full marks). Original wording.
- Videos: videos.json (2H MaffsGuru link, draft; 2G link still blank).
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl')); sys.path.insert(0,H)
from tpl import *
from figs import *
SC=scat
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
YTW={y['id']:y for y in json.load(open(os.path.join(ROOT,'planner','written-youtrys.json')))['items']}

def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:8px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def table(head,rows,fs=19,rid='',extra='',cls='t'):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td><span data-i="{i}">{c}</span></td>' for c in r)+'</tr>' for i,r in enumerate(rows))
    return f'<table class="{cls}"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}">'+(f'<tr>{th}</tr>' if head else '')+f'{tr}</table>'
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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l07')
yid=lambda u:u.split('v=')[1].split('&')[0]
def bar(pct,rid,lab1,lab2):
    """100% bar: explained (green) | not explained (grey), grown on frags"""
    return (f'<div id="{rid}" style="width:620px;margin:10px auto;font-size:18px"><div style="display:flex;height:54px;border:2px solid var(--ink);border-radius:8px;overflow:hidden">'
            f'<div class="frag" style="width:{pct}%;background:#2e7d32;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700">{pct}%</div>'
            f'<div class="frag" style="flex:1;background:#cfd8dc;display:flex;align-items:center;justify-content:center;font-weight:700">{100-pct}%</div></div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:6px"><span>{lab1}</span><span>{lab2}</span></div></div>')
def tri(third,a,b,lab='causes',q=''):
    """third variable → two variables, observed association between them; drawn top-down"""
    box=lambda t,c='':f'<div style="border:2px solid var(--ink);border-radius:8px;padding:6px 12px;background:{c or "#fff"};text-align:center;font-weight:700">{t}</div>'
    return (f'<div style="display:grid;grid-template-columns:1fr 70px 1fr;grid-template-rows:auto auto;gap:8px 0;align-items:center;font-size:16px;width:430px;margin:auto">'
            f'<div class="frag" style="grid-row:1/3">{box(third,"#fff3c4")}</div>'
            f'<div class="frag" style="text-align:center">{lab}{q} →</div><div class="frag">{box(a)}</div>'
            f'<div class="frag" style="text-align:center">{lab}{q} →</div><div class="frag">{box(b)}</div></div>'
            '<div class="frag" style="text-align:right;width:430px;margin:4px auto;font-size:15px;color:var(--muted)">↕ observed association</div>')

S=['<style>.sm .L .q{font-size:17px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.T .mc>div{padding-right:54px}.xs .L .q{font-size:15.5px}.xs .L .mc>div{font-size:14.5px;padding-top:0;padding-bottom:0}'
   '.tight td,.tight th{padding:2px 5px!important}</style>']
# ================= opening
S.append(title(7,'The coefficient of determination · Correlation and causality',f'{CAM} · 2G The coefficient of determination · 2H Correlation and causality','L07').replace('font-size:84px','font-size:58px'))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC_=[x.replace('the the','the') for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC_,[('Do Now','· four VCAA questions','#00838F'),('APK','· two Year 11 skills','var(--apk)'),
  ('What r² tells us','',None),('CAS: finding r²','',None),('Worked examples 17–21','→ You try',None),('Correlation and causality','',None),('You try','· a third variable',None),
  ('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
mini=lambda r,s=3:W_(150,SC(rcloud(r,30,s),(-2.6,2.6),(-2.6,2.6),9,9,W=170,H=130,r=3.5,grid=False,ticks=False))
S.append(keys([
  ('Coefficient of determination, <i>r</i>²','the percentage of the variation in the RV that is explained by the variation in the EV'),
  ('Causation','one variable directly causes a change in the other: only an <b>experiment</b> can show it'),
  ('Common response','both variables respond to a third variable (e.g. temperature → sunscreen and fainting)'),
  ('Confounding variable','another possible cause whose effect can’t be separated from the EV’s'),
  ('Coincidence','an association that happens by chance')],
  [('Coefficient of determination',F('<i>r</i>² = (<i>r</i>)²'),'0 ≤ <i>r</i>² ≤ 1 · write as a %'),
   ('Interpretation',F('<i>r</i>² × 100 % of the variation in <b>RV</b> is explained by the variation in <b>EV</b>'),'the rest (100 − <i>r</i>²%) is NOT explained'),
   ('Back to r',F('<i>r</i> = ±√<i>r</i>²'),'sign from the scatterplot (direction)')],
  f'{CAM}, 2G pp. 146–148, 2H pp. 151–154'))

# ================= Do Now 1: VCAA 2025 E1 Q10 (2F)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q10','Review of 2F',
  G('In the scatterplot below, the <em class="v">games won</em> are plotted against the <em class="v">goals against</em> for each of the 12 Australian A-League men’s teams after 27 games of the 2022–2023 season. A least squares line has been fitted to the data.',
    W_(470,SC(GOALS,(24,50),(5,17),2,1,'goals against','games won',W=600,H=250,r=4.5,fs=12,tl=((24,12.5),(50,8.0)),tl_hid=False,sid='d1s')),
    'The correlation coefficient between <em class="v">games won</em> and <em class="v">goals against</em> is <i>r</i> = −0.466<br>Based on the correlation coefficient, it can be concluded that'),
  [('Sign of r','<i>r</i> &lt; 0: negative: more goals against goes with fewer wins','data-hi="#d1s|p|hy"'),
   ('Association, not cause','<i>r</i> measures an association; it cannot show cause (B, C ✗)')],
  'More goals against is associated with fewer wins: <b>D</b>.','VCAA 2025 General Mathematics Exam 1 Q9–10 stem and Q10 (examiner report; scatterplot redrawn)',
  mc=['fewer goals scored against is associated with a smaller number of wins.','fewer goals scored against causes a smaller number of wins.',
      'more goals scored against causes a smaller number of wins.','more goals scored against is associated with a smaller number of wins.'],key='D',dist=[22,7,8,63],
  dis=('A','22% read the direction wrong: a negative <i>r</i> means as one goes up, the other goes down.')))
S[-1]=S[-1].replace('<section class="slide T dn mcslide"','<section class="slide T dn mcslide xs"',1)
# ================= Do Now 2: VCAA 2024 NHT E1 Q6 (1H)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 NHT Exam 1 Q6','Review of 1H',
  'The weights of cans of fish on a production line are approximately normally distributed with a mean of 126.4 grams and a standard deviation of 2.4 grams.<br>13 600 cans of fish will be produced today.<br>Using the 68–95–99.7% rule, the number of these cans that are expected to weigh between 121.6 and 128.8 grams is',
  [('Locate the values','121.6 = 126.4 − 2 × 2.4 (<i>z</i> = −2) · 128.8 = 126.4 + 2.4 (<i>z</i> = 1)'),
   ('Percentage','<i>z</i> = −2 to 0: 47.5% · 0 to 1: 34% → 81.5%'),
   ('Number','0.815 × 13 600 = 11 084')],
  '11 084 cans: <b>D</b>.','VCAA 2024 (NHT) General Mathematics Exam 1 Q6 (NHT report: answer only, no %)',
  mc=['6460','9248','10 812','11 084','12 920'],key='D',stat=('nht',)))
# ================= Do Now 3: VCAA 2024 E2 Q3d (2E)
T3=('<table class="t" style="font-size:15px"><tr><th>strength</th><td style="min-width:150px"><span class="blank d31"><span class="ph">&nbsp;</span><span class="fill">strong</span></span></td></tr>'
    '<tr><th>direction</th><td><span class="blank d32"><span class="ph">&nbsp;</span><span class="fill">positive</span></span></td></tr></table>')
T3Q='<table class="t" style="font-size:15px">'+''.join(f'<tr><th>{k}</th><td style="min-width:150px">&nbsp;</td></tr>' for k in ('strength','direction'))+'</table>'
WT='<table class="t tight" style="font-size:12px"><tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y in WYR)+'</tr><tr><th><i>Wgold</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WGOLD)+'</tr><tr><th><i>Wbest</i> (m)</th>'+''.join(f'<td>{v:.2f}</td>' for v in WBEST)+'</tr></table>'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q3d','Review of 2E–2F',
  '<div style="font-size:15.5px">The Olympic gold medal-winning height for the women’s high jump, <em class="v">Wgold</em>, is often lower than the best height achieved in other international women’s high jump competitions in that same year.<br>Table 2 lists the Olympic year, <em class="v">year</em>, the gold medal-winning height, <em class="v">Wgold</em>, in metres, and the best height achieved in all international women’s high jump competitions in that same year, <em class="v">Wbest</em>, in metres, for each Olympic year from 1972 to 2020.</div>'
  f'<div style="margin:5px 0">{WT}</div><div style="display:flex;gap:10px;align-items:center"><div style="flex:none;width:300px">'+SC(list(zip(WGOLD,WBEST)),(1.90,2.08),(1.92,2.10),0.02,0.02,'Wgold (m)','Wbest (m)',W=400,H=260,r=4.5,fs=11,sid='d3s')+'</div>'
  '<div style="font-size:15.5px">When a least squares line is fitted to the scatterplot, the equation is found to be:<br><em>Wbest</em> = 0.300 + 0.860 × <em>Wgold</em><br>The correlation coefficient is 0.9318<br>'
  'd. Describe the association between <em class="v">Wbest</em> and <em class="v">Wgold</em> in terms of strength and direction. <span class="muted">(1 mark)</span>'+T3Q+'</div></div>',
  [('Strength','<i>r</i> = 0.9318 ≥ 0.75: strong','data-fill="d31"'),
   ('Direction','<i>r</i> &gt; 0 and the points trend upwards: positive','data-hi="#d3s|p|hy" data-fill="d32"'),
   ('TMPL',T3,'','data-stat="78"')],
  '','VCAA 2024 General Mathematics Exam 2 Q3d (examiner report; scatterplot redrawn)',stat=('mark',78),cmd=('Describe',1,'strength and direction')))
S[-1]=S[-1].replace('<section class="slide T dn"','<section class="slide T dn sm"',1)
# ================= Do Now 4: VCAA 2024 E2 Q1aii (1F)
MT='<table class="t tight" id="d4t" style="font-size:13px">'+''.join('<tr>'+''.join(f'<td><span data-i="{"g" if m>2.25 else ("e" if m==2.25 else "n")}">{y}</span></td><td><span data-i="{"g" if m>2.25 else ("e" if m==2.25 else "n")}">{m:.2f}</span></td>' for y,m in MGOLD[k:k+11])+'</tr>' for k in (0,11))+'</table>'
MT='<table class="t tight" id="d4t" style="font-size:13px"><tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y,_ in MGOLD[:11])+'</tr><tr><th><i>Mgold</i> (m)</th>'+''.join(f'<td><span data-i="{"g" if m>2.25 else ("e" if m==2.25 else "n")}">{m:.2f}</span></td>' for _,m in MGOLD[:11])+'</tr>'\
   '<tr><th><i>year</i></th>'+''.join(f'<td>{y}</td>' for y,_ in MGOLD[11:])+'</tr><tr><th><i>Mgold</i> (m)</th>'+''.join(f'<td><span data-i="{"g" if m>2.25 else ("e" if m==2.25 else "n")}">{m:.2f}</span></td>' for _,m in MGOLD[11:])+'</tr></table>'
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q1aii','Review of 1F',
  'Table 1 lists the Olympic year, <em class="v">year</em>, and the gold medal-winning height for the men’s high jump, <em class="v">Mgold</em>, in metres, for each Olympic Games held from 1928 to 2020. No Olympic Games were held in 1940 or 1944, and the 2020 Olympic Games were held in 2021.'
  f'<div style="font-weight:700;font-size:15px;margin-top:8px">Table 1</div>{MT}<div style="margin-top:10px">a. For the data in Table 1, determine:<br>ii. the percentage of <em class="v">Mgold</em> values greater than 2.25 m. <span class="muted">(1 mark)</span></div>',
  [('Count','22 values; greater than 2.25: 11 (2.25 itself is <b>not</b> greater)','data-hi="#d4t|g|hy"'),
   ('Watch out','1976: 2.25 is not &gt; 2.25','data-hi="#d4t|e|hc"'),
   ('Percentage','11 ÷ 22 × 100 = 50%')],
  '50%','VCAA 2024 General Mathematics Exam 2 Q1aii (examiner report: 54.54% was the most common wrong answer, from including 2.25)',stat=('mark',77),cmd=('Determine',1,'count, then %')))

# ================= APK 1: Cambridge U1&2 7C #6
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 7C #6','Correlation does not imply causation',
  '<div style="font-size:24px">There is a strong positive correlation between sales of umbrellas and traffic accidents. Can we conclude that decreasing the sales of umbrellas will help decrease the number of traffic accidents?</div>',
  [('Association only','a correlation shows the variables move together, not that one causes the other'),
   ('Third variable','rain: on rainy days more umbrellas are sold <b>and</b> roads are wet, so there are more accidents')],
  'No. The association is most likely a common response to rain; it does not show that umbrella sales cause traffic accidents.',
  f'{CAM12} · Ch 7 skills checklist 7C #6 · solution written for 12MAG',cmd=('conclude',None,'yes or no, and why')))
# ================= APK 2: VCAA 2019 E2 Q4a
HT='<table class="t tight" id="a2t" style="font-size:14px"><tr><th rowspan="2">Relative humidity (%)</th><th>9 am</th>'+''.join(f'<td>{v}</td>' for v in H9)+'</tr><tr><th>3 pm</th>'+''.join(f'<td>{v}</td>' for v in H3)+'</tr></table>'
S.append(qslide('apk','APK · Year 11 · VCAA 2019 Exam 2 Q4a','Explanatory and response variables',
  f'The relative humidity (%) at 9 am and 3 pm on 14 days in November 2017 is shown in Table 3 below.<div style="font-weight:700;font-size:15px;margin-top:8px">Table 3</div>{HT}'
  '<div style="font-size:13px;color:var(--muted)">Data: Australian Government, Bureau of Meteorology, &lt;www.bom.gov.au/&gt;</div>'
  '<div style="margin-top:10px">A least squares line is to be fitted to the data with the aim of predicting the relative humidity at 3 pm (<em class="v">humidity 3 pm</em>) from the relative humidity at 9 am (<em class="v">humidity 9 am</em>).<br>a. Name the explanatory variable. <span class="muted">(1 mark)</span></div>',
  [('Predict … from …','we predict <em>humidity 3 pm</em> (RV) <b>from</b> <em>humidity 9 am</em> (EV)')],
  '<em>humidity 9 am</em>',f'{EDR12} · 6A Q15 · VCAA 2019 Further Mathematics Exam 2 Core Q4a (examiner report; original wording)',stat=('mark',84),cmd=('Name',1,'the EV')))

# ================= Learn: r²
S.append(learn('Learn · 2G','The coefficient of determination, r²',
  '<h4>Square r</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px"><li>coefficient of determination = <i>r</i>²</li><li>0 ≤ <i>r</i>² ≤ 1: write it as a percentage</li>'
  '<li>it tells us how well the EV <b>predicts</b> the RV</li><li><i>r</i> = 1: exact prediction · <i>r</i> ≈ 0: no better than guessing</li></ul>',
  '<div style="font-size:20px;text-align:center">Weight (RV) and height (EV): <i>r</i> = 0.8 → <i>r</i>² = 0.64 = 64%</div>'+bar(64,'lb1','explained by the variation in height','NOT explained: diet, lifestyle, build …'),
  '<i>r</i>² is always positive: it has no direction. Square <i>r</i>, don’t square the percentage.',f'{CAM}, 2G pp. 146–147 (bar drawn for 12MAG)',
  cards=(kcard('Coefficient of determination','<i>r</i>² = (<i>r</i>)²'),kcard('Interpretation','<i>r</i>²% of the variation in the RV is explained by the variation in the EV'))))
# ================= Learn: interpreting r² (sentence template)
TPL=('<div style="font-size:24px;line-height:1.9;text-align:center;border:2px dashed var(--ink);border-radius:10px;padding:14px">'
     '<span class="frag" style="background:#c8e6c9;padding:2px 8px;border-radius:6px"><b>__ %</b></span> of the variation in '
     '<span class="frag" style="background:#bbdefb;padding:2px 8px;border-radius:6px"><b>the RV</b></span><br>can be explained by the variation in '
     '<span class="frag" style="background:#fff3c4;padding:2px 8px;border-radius:6px"><b>the EV</b></span></div>')
S.append(learn('Learn · 2G','Interpreting the coefficient of determination',
  '<h4>Three steps</h4><ol style="font-size:19px;margin-left:24px;line-height:1.5"><li>Square <i>r</i>; write it as a % (1 d.p.)</li><li>Decide which variable is the RV and which is the EV</li><li>Fill in the sentence, in context</li></ol>',
  TPL,'Name the variables in context: never write ‘the RV’ or ‘x’ and ‘y’ in an answer.',f'{CAM}, 2G pp. 146–148'))

# ================= CAS
C={c['id']:c for c in (lambda d:d if isinstance(d,list) else d.get('skills',d))(json.load(open(os.path.join(ROOT,'planner','cas-skills.json'))))}['r-and-r2']
r=corr(INC,CO2)
S.append(cas('CAS · 2G','Finding r and r²',
  '<p style="font-size:20px">The following data show the per capita income (in $’000) and the per capita carbon dioxide emissions (in tonnes) of 11 countries.</p>'
  f'<table class="t tight" style="font-size:12px;margin:10px 0"><tr><th>Income ($’000)</th>{"".join(f"<td>{x}</td>" for x in INC)}</tr><tr><th>CO<sub>2</sub> (tonnes)</th>{"".join(f"<td>{x}</td>" for x in CO2)}</tr></table>'
  '<p style="font-size:20px">Find <i>r</i> and the coefficient of determination, <i>r</i>², with income as the EV.</p>'+W_(330,SC(list(zip(INC,CO2)),(0,25),(0,14),5,2,'income','co2',W=380,H=240,r=4.5,fs=12)),
  C['ti'],C['classpad'],f'<i>r</i> = {r:.4f}… · <i>r</i>² = {r*r:.4f}… → <b>66.9%</b> of the variation in CO<sub>2</sub> emissions is explained by the variation in income.',
  f'{CAM} · 2F CAS 2 data (pp. 142–143) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in C['videos']['ti'][:1]+C['videos']['classpad'][:1]]))

# ================= WE17 / YT 3C WE1a
S.append(qslide('we','Worked example 17 · 2G','Calculating the coefficient of determination',
  '<div style="font-size:26px">If the correlation between weight and height is <i>r</i> = 0.8, find the value of the coefficient of determination. Express your answer as a percentage.</div>',
  [fx('Coefficient of determination','<i>r</i>²',F(V('r','0.8'),'²'),'0.64'),('Percentage','0.64 × 100 = 64%')],
  'The coefficient of determination = <i>r</i>² = 0.8² = 0.64 = <b>64%</b>',f'{CAM} · Example 17 (p. 146)',video='Cambridge GO · Example 17 (2G Resources)',cmd=('Find',None,'square r, then %')))
S.append(qslide('yt','You try · Edrolo 3C WE1a','Calculating the coefficient of determination',
  '<div style="font-size:24px">A study was conducted to explore the effect of the time in minutes spent playing <em class="v">video games</em> on time spent <em class="v">studying</em> in minutes. It was determined that the correlation coefficient, <i>r</i>, for the data collected during the study is 0.6584.</div>'
  '<div style="font-size:24px;margin-top:14px">a. Determine the coefficient of determination, <i>r</i>², correct to four decimal places.</div>',
  [fx('Coefficient of determination','<i>r</i>²',F(V('r','0.6584'),'²'),'0.43349…')],
  '<i>r</i>² = <b>0.4335</b>',f'{EDR} · 3C Worked example 1a (p. 179)',cmd=('Determine',None,'4 d.p.')))
# ================= WE18 / YT 3C WE1b
S.append(qslide('we','Worked example 18 · 2G','Interpreting the coefficient of determination',
  '<div style="font-size:26px">In the previous example we found the coefficient of determination between height and weight to be 0.64 (or 64%). Interpret this value in terms of the variables weight and height.</div>'+TPL.replace('class="frag" ','').replace('__ %','64%').replace('the RV','people’s weight').replace('the EV','their height'),
  [('RV and EV','weight depends on height: RV weight, EV height'),('Fill the sentence','64% · weight · height')],
  'The coefficient of determination tells us that <b>64%</b> of the variation in people’s weight is explained by the variation in their height.',f'{CAM} · Example 18 (p. 147)',video='Cambridge GO · Example 18 (2G Resources)',cmd=('Interpret',None,'in context')))
S[-1]=S[-1].replace(TPL.replace('class="frag" ','').replace('__ %','64%').replace('the RV','people’s weight').replace('the EV','their height'),'')
S.append(qslide('yt','You try · Edrolo 3C WE1b','Interpreting the coefficient of determination',
  '<div style="font-size:24px">A study was conducted to explore the effect of the time in minutes spent playing <em class="v">video games</em> on time spent <em class="v">studying</em> in minutes. It was determined that the correlation coefficient, <i>r</i>, for the data collected during the study is 0.6584.</div>'
  '<div style="font-size:24px;margin-top:14px">b. Interpret the coefficient of determination in terms of time spent studying and time spent playing video games.</div>',
  [('EV and RV','studying is affected by video games: EV video games, RV studying'),('Percentage','0.4335 × 100 = 43.35')],
  '43.35% of the variation in the time spent studying can be explained by the variation in the time spent playing video games.',f'{EDR} · 3C Worked example 1b (p. 179)',cmd=('Interpret',None,'in context')))
# ================= WE19 / YT-2G-19, WE20 / YT-2G-20
def we_interp(n,text,r_,rv,ev,ans,video=True):
    return qslide('we',f'Worked example {n} · 2G','Calculating and interpreting the coefficient of determination',f'<div style="font-size:25px">{text}</div>',
      [fx('Coefficient of determination','<i>r</i>²',F('(',V('r',r_),')²'),f'{float(r_)**2:.4f}'),('Percentage',f'{float(r_)**2:.4f} × 100 = {ans[0]}% (1 d.p.)'),('RV and EV',f'RV {rv} · EV {ev}')],
      ans[1],f'{CAM} · Example {n} (pp. 147–148)',video=f'Cambridge GO · Example {n} (2G Resources)',cmd=('Determine',None,'then interpret'))
def yt_w(id_,r_,rv,ev):
    y=YTW[id_]; a=y['answer'].split('; ',1)
    return qslide('yt',f'You try · written for 12MAG ({id_})','Calculating and interpreting the coefficient of determination',f'<div style="font-size:25px">{y["text"].replace("r = ","<i>r</i> = ")}</div>',
      [fx('Coefficient of determination','<i>r</i>²',F('(',V('r',r_),')²'),f'{float(r_)**2:.4f}'),('RV and EV',f'RV {rv} · EV {ev}')],
      a[0].replace('r² = ','<i>r</i>² = ')+'<br>'+a[1][0].upper()+a[1][1:],f'Written for 12MAG (modelled on {CAM} Example {id_[-2:]}; no Edrolo match)',cmd=('Determine',None,'then interpret'))
S.append(we_interp(19,'The level of carbon monoxide (CO) in the air measured at the roadside, and the traffic volume at the same location are linearly related, with <i>r</i> = +0.985. Determine the value of the coefficient of determination, write it in percentage terms and interpret. In this relationship, traffic volume is the explanatory variable.',
  '0.985','carbon monoxide level','traffic volume',('97.0','Therefore, <b>97.0%</b> of the variation in carbon monoxide levels in the air can be explained by the variation in traffic volume.')))
S.append(yt_w('YT-2G-19','0.912','bottles of sunscreen sold','daily maximum temperature'))
S.append(we_interp(20,'Scores on tests of verbal and mathematical ability are linearly related with correlation coefficient <i>r</i> = +0.275. Determine the value of the coefficient of determination, write it in percentage terms, and interpret. In this relationship, verbal ability is the explanatory variable.',
  '0.275','mathematical ability score','verbal ability score',('7.6','Therefore, only <b>7.6%</b> of the variation observed in scores on the mathematical ability test can be explained by the variation in scores obtained on the verbal ability test.')))
S.append(yt_w('YT-2G-20','0.342','spelling ability score','reading speed score'))
# ================= WE21 / YT-2G-21
def we21(pill,kind,r2,rr,seed,src,cm,head='Calculating the correlation coefficient from the coefficient of determination',vid=None):
    neg=rr<0
    sp=W_(380,SC(rcloud(rr,26,seed),(-2.6,2.6),(-2.6,2.6),9,9,W=420,H=270,r=4.5,grid=False,ticks=False,sid=f's{seed}'))
    return qslide(kind,pill,head,G(f'<div style="font-size:24px">For the relationship described by this scatterplot, the coefficient of determination = {r2}.<br>Determine the value of the correlation coefficient, <i>r</i>, rounded to four decimal places.</div>',sp),
      [fx('Back to r','<i>r</i>',F('±√',V('r²',r2)),f'±{abs(rr):.4f}'),('Direction',('the points trend downwards: negative' if neg else 'the points trend upwards: positive'),f'data-hi="#s{seed}|p|hy"')],
      f'∴ <i>r</i> = <b>{rr:+.4f}</b>'.replace('+','+' if not neg else ''),src,video=vid,cmd=('Determine',None,'sign from the plot'))
S.append(we21('Worked example 21 · 2G','we','0.5210',-0.7218,21,f'{CAM} · Example 21 (p. 148; scatterplot drawn for 12MAG)','',vid='Cambridge GO · Example 21 (2G Resources)'))
S.append(we21('You try · written for 12MAG (YT-2G-21)','yt','0.6384',0.7990,24,f'Written for 12MAG (modelled on {CAM} Example 21; no Edrolo match)',''))

# ================= Learn 2H: correlation and causality
S.append(learn('Learn · 2H','Correlation does not imply causality',
  '<h4>Association ≠ cause</h4><p style="font-size:19px">A correlation tells you the <b>strength</b> of an association, but nothing about its <b>cause</b>. Countries with more IKEA stores win more Nobel prizes (<i>r</i> = 0.82): building IKEAs won’t win prizes.</p>'
  '<h4 style="margin-top:10px">To show cause: an experiment</h4><p style="font-size:19px">Change the EV on purpose, keep every other variable the same (random groups, same conditions), then measure the RV.</p>',
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;font-size:18px"><div class="key frag"><h4>Observation</h4>record data as it happens<br>→ shows an <b>association</b> only</div><div class="key frag"><h4>Experiment</h4>EV controlled, everything else constant<br>→ can show <b>causation</b></div></div>',
  'However strong the association, observational data alone never proves cause.',f'{CAM}, 2H pp. 151–152',cards=(kcard('Causation','only an experiment can show it'),)))
S.append(learn('Learn · 2H','Possible non-causal explanations',
  '<h4>Three explanations</h4><ul class="bul" style="font-size:18px;line-height:1.45;margin-left:22px"><li><b>Common response:</b> both respond to a third variable</li><li><b>Confounding:</b> another possible cause, can’t be separated</li><li><b>Coincidence:</b> chance (margarine and divorce in Maine, <i>r</i> = 0.99)</li></ul>',
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div style="text-align:center;font-weight:700;margin-bottom:4px">Common response</div>'+tri('Temperature','Sunscreen','Fainting')+'</div>'
  '<div><div style="text-align:center;font-weight:700;margin-bottom:4px">Confounding</div>'+tri('Economy','Unemployment','Crime',q=' ?')+'</div></div>',
  'In an answer: name the third variable and say how it affects <b>both</b> variables.',f'{CAM}, 2H pp. 153–154 (diagrams redrawn)'))
# ================= You try 2H: Edrolo 2D WE2
S.append(qslide('yt','You try · Edrolo 2D WE2','Correlation and causation',
  '<div style="font-size:22px">Gunther runs a cafe and collects data throughout the year on the daily number of <em class="v">hot chocolates purchased</em>. He finds that there is a negative association between the daily number of <em class="v">hot chocolates purchased</em> and the number of <em class="v">daylight hours</em> on a particular day.</div>'+
  plist([('a','Identify a potential third variable that could have caused this association.'),('b','Has Gunther conducted an appropriate experiment to determine causation? Why or why not?')]),
  [],'',f'{EDR} · 2D Worked example 2 (p. 148; no Cambridge Example for 2H)',cmd=('Identify',None,'a third variable'),
  parts=[('a','Colder seasons: fewer daylight hours <b>and</b> more hot chocolates. A potential third variable is the <b>season</b>.'),
         ('b','No. The variable <b>season</b> does not remain constant across the experiment (all external variables must stay constant to determine causation).')]))

# ================= Exits
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2017 Exam 1 Q12','Show what you know',
  'Data collected over a period of 10 years indicated a strong, positive association between the number of stray cats and the number of stray dogs reported each year (<i>r</i> = 0.87) in a large, regional city.<br>A positive association was also found between the population of the city and both the number of stray cats (<i>r</i> = 0.61) and the number of stray dogs (<i>r</i> = 0.72).<br>During the time that the data was collected, the population of the city grew from 34 564 to 51 055.<br>From this information, we can conclude that',
  [('Third variable','population is associated with both cats and dogs'),('Common response','population growth → more stray cats and more stray dogs')],
  'A common response to the growing population: <b>D</b>.',f'{EDR} · 2D Q13 · VCAA 2017 Further Mathematics Exam 1 Q12 (examiner report; original wording)',
  mc=['if cat owners paid more attention to keeping dogs off their property, the number of stray cats reported would decrease.','the association between the number of stray cats and stray dogs reported cannot be causal because only a correlation of +1 or –1 shows causal relationships.',
      'there is no logical explanation for the association between the number of stray cats and stray dogs reported in the city so it must be a chance occurrence.',
      'because larger populations tend to have both a larger number of stray cats and stray dogs, the association between the number of stray cats and the number of stray dogs can be explained by a common response to a third variable, which is the increasing population size of the city.',
      'more stray cats were reported because people are no longer as careful about keeping their cats properly contained on their property as they were in the past.'],key='D',dist=[2,6,10,81,2],
  dis=('C','10% chose coincidence, but population explains the association.')))
S[-1]=S[-1].replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide xs"',1)
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2019 Exam 2 Q4c','Show what you know',
  f'The relative humidity (%) at 9 am and 3 pm on 14 days in November 2017 is shown in Table 3 below.<div style="font-weight:700;font-size:15px;margin-top:8px">Table 3</div>{HT.replace("a2t","x2t")}'
  '<div style="font-size:13px;color:var(--muted)">Data: Australian Government, Bureau of Meteorology, &lt;www.bom.gov.au/&gt;</div>'
  '<div style="margin-top:10px">A least squares line is to be fitted to the data with the aim of predicting the relative humidity at 3 pm (<em class="v">humidity 3 pm</em>) from the relative humidity at 9 am (<em class="v">humidity 9 am</em>).<br>c. Determine the value of the correlation coefficient for this data set.<br>Round your answer to three decimal places. <span class="muted">(1 mark)</span></div>',
  [('CAS','X: humidity 9 am (EV), Y: humidity 3 pm (RV) → Linear Reg'),('Read off',f'<i>r</i> = {corr(H9,H3):.4f}…')],
  '<i>r</i> = <b>0.871</b>',f'{EDR} · 2D Q14 · VCAA 2019 Further Mathematics Exam 2 Core Q4c (examiner report; original wording)',stat=('mark',76),cmd=('Determine',1,'3 d.p.')))

# ================= closing
S.append(checkin(SC_))
CW=CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book','Chapter 2 revision booklet'),st_.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st_['items']]) for st_ in CW]))
Vd=json.load(open(os.path.join(ROOT,'planner','videos.json'))); Vd=Vd if isinstance(Vd,list) else Vd.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in Vd if v['sub'] in ('2G','2H') and v.get('url')]))
n=assemble(S,'12MAG · L07 · Coefficient of determination; causation',os.path.join(ROOT,'lessons','2G-2H slides.html'))
print(n-1,'slides')
