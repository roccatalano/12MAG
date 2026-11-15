"""Lesson l03 (2A, 2B) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/2A-2B slides.html
Run: python3 tools/deck/l03/build.py      Screenshots: python3 tools/deck/l03/shoot.py

Sources (all read from the PDFs on G: 15 Nov 2026; question text verbatim):
- Do Now: VCAA 2024 Exam 1 Q7 (report: C 82%, A 5, B 9, D 4) · VCAA 2023 Exam 1 Q5 (report: B 84%, A 4, C 6, D 4, E 1)
          VCAA 2024 Exam 2 Q1ai (report: 96% scored 1) · VCAA 2024 Exam 2 Q1b (report: 84% scored 1)
- APK (planner card): Cambridge Units 1&2 Chapter 2 skills checklist 2A #2 (canteen ratings) · Chapter 1 checklist 1A #2 (0.67 as a %)
- Learn: Cambridge Units 3&4 2A pp. 104-106, 2B pp. 108-117 (gun control, mobile phones, smoking tables; report wording)
- Worked examples: Cambridge Units 3&4 Examples 1-8 (pp. 105-117)
- You try (planner card): Edrolo Units 1&2 1A WE1 (p. 2) · Edrolo Units 3&4 2C WE1, WE2 (p. 132) · 2A WE1 (pp. 106-107), WE4 (p. 110),
  WE2 (pp. 107-108, grouped bar chart), WE3 (p. 109), WE5 (pp. 110-111)
- Exits: Edrolo U3&4 2A Q11 = VCAA 2018 Exam 2 (Further) Core Q1d (report: 94% scored 2/2, average 1.9)
         Edrolo U3&4 2A Q13 = VCAA 2021 Exam 1 (Further) Core Q3 (report: A 50%, B 13, C 28, D 1, E 8). Question text = the original VCAA wording.
- Videos: MaffsGuru 2B (YouTube title checked 15 Nov); the 2A MaffsGuru video is locked (paid), so that card stays blank.
"""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
import tpl as TPL
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'

def table(head,rows,fs=19,extra='',rid=''):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td{" class=\"l\"" if j==0 else ""}><span data-i="{i}">{c}</span></td>' for j,c in enumerate(r))+'</tr>' for i,r in enumerate(rows))
    return f'<table class="t"{f" id={chr(34)}{rid}{chr(34)}" if rid else ""} style="font-size:{fs}px;{extra}"><tr>{th}</tr>{tr}</table>'
def seg(rid,cfg,stepped=False,ax=False): return f'<div class="chart{" noax" if ax else ""}" id="{rid}" data-chart="seg" data-cfg=\'{J(cfg)}\'{" data-stepped=\"1\"" if stepped else ""}{" data-axhide" if ax else ""}></div>'
def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:12px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'):
    return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def tw(rid,rv,ev,cats,rows,total=None,fs=18,totcol=None,extra=''):
    """two-way table: EV labels the columns, RV the rows. rows [(rv category, [cells])]; cells may be B() blanks.
    Each cell has data-i = 10*row + column (total row = 90 + column) so steps can highlight it."""
    nc=len(cats)+(1 if totcol else 0)
    h=(f'<tr><th style="background:none;border:none"></th><th colspan="{len(cats)}"><em>{ev}</em></th>'+('<th style="background:none;border:none"></th>' if totcol else '')+'</tr>'
       f'<tr><th class="l"><em>{rv}</em></th>'+''.join(f'<th>{c}</th>' for c in cats)+('<th>Total</th>' if totcol else '')+'</tr>')
    tr=''
    for r,(lab,cells) in enumerate(rows):
        cc=cells+([totcol[r]] if totcol else [])
        tr+=f'<tr><td class="l">{lab}</td>'+''.join(f'<td><span data-i="{10*r+c}">{x}</span></td>' for c,x in enumerate(cc))+'</tr>'
    if total:
        tr+='<tr><td class="l"><b>Total</b></td>'+''.join(f'<td><b><span data-i="{90+c}">{x}</span></b></td>' for c,x in enumerate(total))+'</tr>'
    return f'<table class="t cmp" id="{rid}" style="font-size:{fs}px;{extra}">{h}{tr}</table>'
def report(parts,fs=20):
    out=''
    for hl,bc,toks in parts:
        out+=f'<span class="{hl}">'+''.join(t if isinstance(t,str) else B(bc,t[1],t[0]) for t in toks)+'</span> '
    return f'<div class="report"><p class="tpl" style="font-size:{fs}px;line-height:1.8;margin:0">{out}</p></div>'
def gbar(rid,cats,names,vals,ymax,ystep,xl,yl,W=560,Hh=330):
    """grouped bar chart (one group per EV category, one bar per RV category). rect.grow order: group by group."""
    PAL=['#9db8f0','#4f84e6','#1f4fb0']; L=60;B_=62;T=14;R=150;pw=W-L-R;ph=Hh-T-B_
    s=f'<svg viewBox="0 0 {W} {Hh}" width="100%">'
    for y in range(0,ymax+1,ystep):
        yy=T+ph-y/ymax*ph; s+=f'<line x1="{L}" x2="{L+pw}" y1="{yy}" y2="{yy}" stroke="#e3e6ee"/><text x="{L-8}" y="{yy+5}" text-anchor="end" font-size="15" fill="#555">{y}</text>'
    gw=pw/len(cats); bw=gw*0.8/len(names)
    for i,c in enumerate(cats):
        for j in range(len(names)):
            v=vals[j][i]; hh=v/ymax*ph; x=L+i*gw+gw*0.1+j*bw; yv=T+ph-hh
            s+=f'<rect class="grow" x="{x:.1f}" width="{bw:.1f}" y="{yv:.1f}" height="{hh:.1f}" data-y="{yv:.1f}" data-h="{hh:.1f}" fill="{PAL[j]}"/>'
        s+=f'<text x="{L+i*gw+gw/2}" y="{T+ph+22}" text-anchor="middle" font-size="15">{c}</text>'
    s+=(f'<line x1="{L}" x2="{L+pw}" y1="{T+ph}" y2="{T+ph}" stroke="#333" stroke-width="2"/><line x1="{L}" x2="{L}" y1="{T}" y2="{T+ph}" stroke="#333" stroke-width="2"/>'
        f'<text x="{L+pw/2}" y="{Hh-12}" text-anchor="middle" font-size="16" font-weight="600" font-style="italic">{xl}</text>'
        f'<text x="16" y="{T+ph/2}" text-anchor="middle" font-size="16" font-weight="600" transform="rotate(-90 16 {T+ph/2})">{yl}</text><g class="lg">')
    for j,n in enumerate(names): s+=f'<rect x="{L+pw+18}" y="{T+10+j*30}" width="20" height="20" fill="{PAL[j]}"/><text x="{L+pw+46}" y="{T+26+j*30}" font-size="16" font-weight="600">{n}</text>'
    return f'<div class="chart noax" id="{rid}" data-chart="gbar" data-stepped="1" data-axhide>{s}</g></svg></div>'
def scat(pts):
    W,Hh,L,B_,T,R=420,330,64,52,12,16; pw=W-L-R; ph=Hh-T-B_
    sx=lambda x:L+x/10*pw; sy=lambda y:T+ph-y/200*ph
    s=f'<svg viewBox="0 0 {W} {Hh}" width="100%">'
    for y in range(0,201,50): s+=f'<line x1="{L}" x2="{L+pw}" y1="{sy(y)}" y2="{sy(y)}" stroke="#e3e6ee"/><text x="{L-8}" y="{sy(y)+5}" text-anchor="end" font-size="14">{y}</text>'
    for x in range(0,11,2): s+=f'<line x1="{sx(x)}" x2="{sx(x)}" y1="{T}" y2="{T+ph}" stroke="#e3e6ee"/><text x="{sx(x)}" y="{T+ph+20}" text-anchor="middle" font-size="14">{x}</text>'
    s+=''.join(f'<circle cx="{sx(x)}" cy="{sy(y)}" r="5" fill="#2f6fdf"/>' for x,y in pts)
    s+=(f'<line x1="{L}" x2="{L+pw}" y1="{T+ph}" y2="{T+ph}" stroke="#333" stroke-width="2"/><line x1="{L}" x2="{L}" y1="{T}" y2="{T+ph}" stroke="#333" stroke-width="2"/>'
        f'<text x="{L+pw/2}" y="{Hh-6}" text-anchor="middle" font-size="14" font-weight="600" font-style="italic">number of soft drinks consumed per week</text>'
        f'<text x="14" y="{T+ph/2}" text-anchor="middle" font-size="14" font-weight="600" font-style="italic" transform="rotate(-90 14 {T+ph/2})">daily sugar intake (g)</text></svg>')
    return s
def cells(r,cs): return ','.join(str(10*r+c) for c in cs)
yid=lambda u:u.split('v=')[1].split('&')[0]

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
CARD=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))),'gm12-u3-l03')

S=[]
# ================= opening
S.append(title(3,'Investigating associations between two categorical variables',
  'Cambridge General Mathematics Units 3&amp;4 · 2A Bivariate data – Classifying the variables · 2B Investigating associations between categorical variables','L03',
  flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=[x for g in CARD['learningObjectives'] for x in g['items']]
SC=[x for g in CARD['successCriteria'] for x in g['items']]
S.append(today(LI,SC,[('Do Now','· four VCAA questions on Chapter 1','#00838F'),('APK','· two Year 11 skills','var(--apk)'),
  ('Bivariate data','→ WE 1',None),('Explanatory and response variables','→ WE 2, 3',None),('Two-way frequency tables','→ WE 4',None),
  ('Percentaged tables and associations','→ WE 5, 6',None),('Segmented bar charts','→ WE 7, 8',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
FPC=F('column % = ',FR(['cell frequency'],['column total']),' × 100%')
S.append(keys([
  ('Bivariate data','two variables recorded for each individual (subject)'),
  ('Explanatory variable (EV)','the variable we expect to explain or predict the other one'),
  ('Response variable (RV)','the variable whose value we explain or predict'),
  ('Two-way frequency table','counts for two categorical variables: EV labels the columns, RV labels the rows',
   '<table class="t" style="font-size:12px"><tr><th></th><th>EV 1</th><th>EV 2</th></tr><tr><td class="l">RV a</td><td>32</td><td>30</td></tr><tr><td class="l">RV b</td><td>26</td><td>12</td></tr></table>'),
  ('Association','the percentages differ across the EV categories: knowing the EV helps predict the RV'),
  ('Segmented bar chart','one 100% bar per EV category, split into segments for the RV',
   '<div style="width:240px">'+seg('ks',{"bars":[{"v":[55,45]},{"v":[71,29]}],"names":["For","Against"],"yl":"%","h":150,"ticks":50})+'</div>')],
  [('Column percentage',FPC,'percentage down each column of the EV: each column totals 100%'),
   ('Placing the variables',F('EV → columns (horizontal axis) · RV → rows (segments)'))],
  f'{CAM}, 2A pp. 105–106, 2B pp. 109–116'))

# ================= Do Now 1: VCAA 2024 E1 Q7 (1H)
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2024 Exam 1 Q7','Review of 1H',
  'Fiona plays nine holes of golf each week, and records her <em class="v">score</em>.<br>Her mean <em class="v">score</em> for all rounds in 2024 is 55.7<br>In one round, when she recorded a <em class="v">score</em> of 48, her standardised score was <i>z</i> = −1.75<br>The standard deviation for <em class="v">score</em> in 2024 is',
  [fx('z-score',' <i>z</i>',F(FR([V('x','48'),' − ',V('x̄','55.7')],[V('s','s')])),'−1.75'),
   ('Solve','−7.7 ÷ <i>s</i> = −1.75, so <i>s</i> = 7.7 ÷ 1.75 = 4.4')],
  'The standard deviation is <b>4.4</b>.','VCAA 2024 General Mathematics Exam 1 Q7 (examiner report)',stat=('mc',82),
  mc=['1.1','2.3','4.4','6.95'],key='C',dist=[5,9,82,4]))
# ================= Do Now 2: VCAA 2023 E1 Q5 (1H)
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2023 Exam 1 Q5','Review of 1H',
  'The heights of a group of Year 8 students have a mean of 163.56 cm and a standard deviation of 8.14 cm.<br>One student’s height has a standardised <i>z</i>-score of −0.85.<br>This student’s height, in centimetres, is closest to',
  [('Rearrange','<i>x</i> = <i>x̄</i> + <i>z</i> × <i>s</i>'),('Substitute','163.56 + (−0.85) × 8.14 = 163.56 − 6.919 = 156.64')],
  'The student’s height is closest to <b>156.6 cm</b>.','VCAA 2023 General Mathematics Exam 1 Q5 (examiner report)',stat=('mc',84),
  mc=['155.4','156.6','162.7','170.5','171.7'],key='B',dist=[4,84,6,4,1]))
# ================= Do Now 3 & 4: VCAA 2024 E2 Q1ai, Q1b
MG=[(1928,'1.94'),(1932,'1.97'),(1936,'2.03'),(1948,'1.98'),(1952,'2.04'),(1956,'2.12'),(1960,'2.16'),(1964,'2.18'),(1968,'2.24'),(1972,'2.23'),(1976,'2.25'),
    (1980,'2.36'),(1984,'2.35'),(1988,'2.38'),(1992,'2.34'),(1996,'2.39'),(2000,'2.35'),(2004,'2.36'),(2008,'2.36'),(2012,'2.33'),(2016,'2.38'),(2020,'2.37')]
def mgt(rid,rows,off): return ('<table class="t tight" id="'+rid+'" style="font-size:17px;line-height:1"><tr><th><em>year</em></th><th><em>Mgold</em> (m)</th></tr>'+
    ''.join(f'<tr><td style="padding:1px 8px"><span data-i="{off+i}">{y}</span></td><td style="padding:1px 8px"><span data-i="{off+i}">{v}</span></td></tr>' for i,(y,v) in enumerate(rows))+'</table>')
MGT=f'<div class="row" style="gap:12px;justify-content:center">{mgt("d3a",MG[:11],0)}{mgt("d3b",MG[11:],11)}</div>'
MGI='Table 1 lists the Olympic year, <em class="v">year</em>, and the gold medal-winning height for the men’s high jump, <em class="v">Mgold</em>, in metres, for each Olympic Games held from 1928 to 2020. No Olympic Games were held in 1940 or 1944, and the 2020 Olympic Games were held in 2021.'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2024 Exam 2 Q1ai','Review of 1F',
  G(f'<span style="font-size:18px">{MGI}</span>',MGT.replace('d3a','d3a1').replace('d3b','d3b1'),'For the data in Table 1, determine:<br>i. the maximum <em class="v">Mgold</em> in metres <span class="muted">(1 mark)</span>'),
  [('Scan','the largest value in the <em>Mgold</em> column: 2.39 (1996)','data-hi="#d3b1|15|hy"')],
  'The maximum <em class="v">Mgold</em> is <b>2.39 m</b>.','VCAA 2024 General Mathematics Exam 2 Q1ai (examiner report)',stat=('mark',96),cmd=('determine',1,'one value, in metres')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2024 Exam 2 Q1b','Review of 1H',
  'The mean of these <em class="v">Mgold</em> values is 2.23 m, and the standard deviation is 0.15 m.<br>Calculate the standardised <i>z</i>-score for the 2000 <em class="v">Mgold</em> of 2.35 m. <span class="muted">(1 mark)</span>',
  [fx('z-score',' <i>z</i>',F(FR([V('x','2.35'),' − ',V('x̄','2.23')],[V('s','0.15')])),'0.8')],
  'The <i>z</i>-score is <b>0.8</b>.','VCAA 2024 General Mathematics Exam 2 Q1b (examiner report)',stat=('mark',84),cmd=('Calculate',1,'the z-score')))

# ================= APK 1: Cambridge U1&2 2A #2
CN='bad, bad, ok, ok, good, bad, good, ok, ok, ok, bad, ok, bad, good, good, good, good, bad, ok, ok'.split(', ')
def dl(rid,vals,cols,fs=22):
    return f'<div class="dlist" id="{rid}" style="grid-template-columns:repeat({cols},auto);font-size:{fs}px">'+''.join(f'<span data-i="{i}">{v}</span>' for i,v in enumerate(vals))+'</div>'
ix=lambda w:','.join(str(i) for i,v in enumerate(CN) if v==w)
ct=('<table class="t cmp" style="font-size:19px"><tr><th class="l"><em>Rating</em></th><th>Frequency</th><th>%</th></tr>'+
    ''.join(f'<tr><td class="l">{a}</td><td>{B(f"c{k}",n)}</td><td>{B("cp",p)}</td></tr>' for k,(a,n,p) in enumerate([('bad',6,'30'),('ok',8,'40'),('good',6,'30')]))+
    f'<tr><td class="l"><b>Total</b></td><td><b>{B("c3",20)}</b></td><td><b>{B("cp",100)}</b></td></tr></table>')
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2A #2','What do you remember?',
  G('Twenty students rated their school canteen as bad, ok or good, giving the following data:',dl('a1d',CN,5,22),'Construct a percentage frequency table.'),
  [('Count bad','6',f'data-hi="#a1d|{ix("bad")}|hy" data-fill="c0"'),('Count ok','8',f'data-hi="#a1d|{ix("ok")}|hb" data-fill="c1"'),
   ('Count good','6',f'data-hi="#a1d|{ix("good")}|hg" data-fill="c2"'),('Total','20','data-hi="#a1d||" data-fill="c3"'),
   fx('Percentage frequency','bad',F(FR([V('count','6')],[V('total','20')]),' × 100%'),'30%',ra='data-fill="cp"'),
   ('TMPL',ct)],
  '',f'{CAM12} · Chapter 2 skills checklist, 2A #2 (teacher solution)',cmd=('Construct',None,'frequency, % and a total')))
# ================= APK 2: Cambridge U1&2 1A #2
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 1A #2','Decimals to percentages',
  '<p style="font-size:34px;margin-top:40px">What is 0.67 as a percentage?</p>',
  [('Multiply by 100','0.67 × 100 = 67')],'0.67 = <b>67%</b>',f'{CAM12} · Chapter 1 skills checklist, 1A #2 (teacher solution)',cmd=('What',None,'a percentage')))

# ================= Learn 2A: bivariate data, three kinds of investigation
S.append(learn('Learn · 2A','Bivariate data: what kind of association?',
  '<h4>Bivariate data</h4><p>Two variables are recorded for each person or thing, so we can ask whether they <b>vary together</b> (are associated). First step: classify each variable as categorical or numerical.</p>',
  '<div class="row" style="gap:18px;align-items:stretch">'
  '<div class="key frag" style="flex:1"><h4>Categorical + numerical</h4><p style="font-size:20px">Does the new headache treatment work more quickly than the old one?<br><span class="muted"><em>type of treatment</em> (new, old) · <em>time taken</em> (minutes)</span></p></div>'
  '<div class="key frag" style="flex:1"><h4>Two categorical</h4><p style="font-size:20px">Are city voters more likely to vote Greens than country voters?<br><span class="muted"><em>place of residence</em> (city, country) · <em>vote for the Greens</em> (yes, no)</span></p></div>'
  '<div class="key frag" style="flex:1"><h4>Two numerical</h4><p style="font-size:20px">Can we predict a test score (%) from hours spent studying?<br><span class="muted"><em>test score</em> · <em>time spent studying</em></span></p></div></div>',
  'A variable with number codes (1 = light, 2 = moderate …) or a postcode is still categorical: the numbers are labels.',f'{CAM}, 2A pp. 104–105',
  cards=[kcard('Bivariate data','two variables recorded for each individual')]))
# ================= WE1: Cambridge Example 1
S.append(qslide('we','Worked example 1 · 2A','Identifying associations as categorical or numerical',
  'For each of the following questions, determine if they involve investigating associations between<br>■ one numerical variable and one categorical variable or<br>■ two categorical variables or<br>■ two numerical variables.'+
  plist([('a','Are younger people (age measured in years) more likely to believe in astrology (measured as ‘yes’ or ‘no’) than older people?'),
         ('b','Do people who weigh more (weight measured in kg) tend to have higher blood pressure (blood pressure measured in mmHg)?'),
         ('c','Are people who have a driver’s licence (measured as ‘yes’ or ‘no’) more likely to be in favour of lowering the driving age (measured as ‘yes’ or ‘no’)?')]),
  [],'',f'{CAM} · Example 1 (p. 105)',video='Cambridge GO · Example 1 (2A Resources)',cmd=('determine',None,'name both variables and their types'),
  parts=[('a','<em>age</em> in years: numerical · <em>belief in astrology</em> yes/no: categorical → <b>one numerical variable and one categorical variable</b>'),
         ('b','<em>weight</em> (kg) and <em>blood pressure</em> (mmHg) are both measured → <b>two numerical variables</b>'),
         ('c','<em>have a driver’s licence</em> and <em>support for lowering the driving age</em> are both yes/no → <b>two categorical variables</b>')]))
# ================= You try: Edrolo U1&2 1A WE1
S.append(qslide('yt','You try · Edrolo U1&amp;2 1A WE1','Categorical or numerical?',
  '<p style="font-size:30px;margin-top:40px">Is the variable <em class="v">hair colour</em> an example of categorical or numerical data?</p>',
  [('Count or measure?','hair colour can’t be counted or measured; it is sorted into groups (brown, black, red …).')],
  '<em class="v">hair colour</em> is <b>categorical</b>.',f'{EDR12} · 1A Worked example 1 (p. 2)',cmd=('Is',None,'categorical or numerical')))
# ================= Learn 2A: EV and RV
S.append(learn('Learn · 2A','Explanatory and response variables',
  '<h4>Which variable explains the other?</h4><p>The <b>explanatory variable (EV)</b> is the one we expect to explain or predict the value of the <b>response variable (RV)</b>.</p>',
  '<div class="row" style="gap:22px;align-items:stretch"><div class="key frag" style="flex:1"><h4>‘Are city voters more likely to vote Greens than country voters?’</h4>'
  '<p style="font-size:22px">Knowing where someone lives might help explain how they vote, not the other way round.</p><p style="font-size:24px;margin-top:10px"><b>EV:</b> <em>place of residence</em><br><b>RV:</b> <em>vote for the Greens</em></p></div>'
  '<div class="key frag" style="flex:1"><h4>Read the question</h4><p style="font-size:22px">‘Can we predict <b>RV</b> from <b>EV</b>?’ · ‘Does <b>RV</b> depend on <b>EV</b>?’</p>'
  '<p style="font-size:22px;margin-top:10px">If there is no obvious EV, the way the question is asked decides.</p><p class="muted" style="font-size:19px;margin-top:10px">Also called the independent (IV) and dependent (DV) variables.</p></div></div>',
  'On a graph or table the EV goes on the horizontal axis / across the columns.',f'{CAM}, 2A pp. 105–106',
  cards=[kcard('Explanatory variable (EV)','explains or predicts'),kcard('Response variable (RV)','responds; is predicted')]))
# ================= WE2 / You try / WE3 / You try
S.append(qslide('we','Worked example 2 · 2A','Identifying the response and explanatory variables',
  'We wish to investigate the question, ‘Does the time it takes a student to get to school depend on their mode of transport?’ The variables here are <em class="v">time</em> and <em class="v">mode of transport</em>. Which is the response variable (RV) and which is the explanatory variable (EV)?',
  [('Read the question','‘does the <em>time</em> … depend on their <em>mode of transport</em>?’'),('Explain','a student’s mode of transport might explain the differences in the time it takes to get to school.')],
  'EV: <em class="v">mode of transport</em><br>RV: <em class="v">time</em>',f'{CAM} · Example 2 (p. 106)',video='Cambridge GO · Example 2 (2A Resources)',cmd=('Which',None,'name the EV and the RV')))
S.append(qslide('yt','You try · Edrolo 2C WE1','Identifying the response and explanatory variables',
  'The following question was posed: ‘Can the <em class="v">number of ice creams sold</em> be predicted from the <em class="v">temperature</em>?’<br>Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.',
  [('Predicted?','the number of ice creams sold is being predicted from changes in temperature.')],
  'RV: <em class="v">number of ice creams sold</em><br>EV: <em class="v">temperature</em>',f'{EDR} · 2C Worked example 1 (p. 132)',cmd=('Identify',None,'name the RV and the EV')))
S.append(qslide('we','Worked example 3 · 2A','Identifying the response and explanatory variables',
  'Can we predict people’s height (in cm) from their wrist measurement? The variables in this investigation are <em class="v">height</em> and <em class="v">wrist measurement</em>. Which is the response variable (RV) and which is the explanatory variable (EV)?',
  [('Read the question','‘predict … <em>height</em> from their <em>wrist measurement</em>’'),('Explain','we use wrist measurement as the predictor (explanatory) variable; height is then the response.')],
  'EV: <em class="v">wrist measurement</em><br>RV: <em class="v">height</em>',f'{CAM} · Example 3 (p. 106)',video='Cambridge GO · Example 3 (2A Resources)',cmd=('Which',None,'name the EV and the RV')))
SP=[(0,98),(1,90),(2,110),(3,122),(4,125),(5,130),(6,137),(7,145),(8,166),(9,192),(10,188)]
S.append(qslide('yt','You try · Edrolo 2C WE2','Identifying the response and explanatory variables',
  G('A study was conducted on the association between <em class="v">daily sugar intake</em> and the <em class="v">number of soft drinks consumed per week</em>. The following scatterplot displays the data that was collected.',
    '<div style="width:400px">'+scat(SP)+'</div>','Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.'),
  [('Axes','on a scatterplot the RV is on the vertical axis and the EV on the horizontal axis.')],
  'RV: <em class="v">daily sugar intake</em><br>EV: <em class="v">number of soft drinks consumed per week</em>',f'{EDR} · 2C Worked example 2 (p. 132; scatterplot redrawn)',cmd=('Identify',None,'name the RV and the EV')))

# ================= Learn 2B: the two-way frequency table
GT=tw('lgt','Attitude to gun control','Residence',['Country','City'],[('For',[B('g1',32),B('g1',30)]),('Against',[B('g2',26),B('g2',12)])],
      total=[B('g4',58),B('g4',42),B('g4',100)],totcol=[B('g3',62),B('g3',38)],fs=22)
body=('<div class="row" style="gap:26px;align-items:stretch"><div class="key" style="flex:1"><h4>100 people: residence and attitude to gun control</h4>'
  '<ul class="bul" style="font-size:20px;line-height:1.6;margin-left:24px"><li>32 country people are for gun control</li><li>30 city people are for gun control</li><li>26 country people are against gun control</li><li>12 city people are against gun control</li></ul>'
  '<p class="frag" style="font-size:21px;margin-top:12px"><b>EV:</b> <em>residence</em> → labels the <b>columns</b><br><b>RV:</b> <em>attitude to gun control</em> → labels the <b>rows</b></p></div>'
  f'<div class="key" style="flex:1.1"><h4>Two-way frequency table</h4><div style="display:flex;justify-content:center;margin-top:10px">{GT}</div>'
  '<p class="frag" style="font-size:20px;margin-top:14px">Row sums and column sums complete the table; the four counts inside are the <b>cells</b>.</p></div></div>'
  '<span class="frag" data-fill="g1"></span><span class="frag" data-fill="g2"></span><span class="frag" data-fill="g3"></span><span class="frag" data-fill="g4"></span>'
  '<div class="tip frag" style="margin-top:14px">Check: row totals and column totals both add to the sample size (62 + 38 = 58 + 42 = 100).</div>')
S.append(TPL._frame('learn','Learn · 2B','Constructing a two-way frequency table',body,f'{CAM}, 2B pp. 109–110',cfu='disc'))
# ================= WE4: Cambridge Example 4
ST=[('Female','Yes'),('Male','Yes'),('Female','No'),('Female','Yes'),('Male','No'),('Male','Yes'),('Female','Yes'),('Male','No'),('Female','No'),('Female','Yes')]
sti=lambda g,u=None:','.join(str(i) for i,(a,b) in enumerate(ST) if a==g and (u is None or b==u))
def stt(rid,rng): return ('<table class="t tight" id="'+rid+'" style="font-size:17px"><tr><th>Student</th><th><em>Gender</em></th><th><em>University</em></th></tr>'+
    ''.join(f'<tr><td><span data-i="{i}">{i+1}</span></td><td><span data-i="{i}">{ST[i][0]}</span></td><td><span data-i="{i}">{ST[i][1]}</span></td></tr>' for i in rng)+'</table>')
STT=f'<div class="row" style="gap:12px;justify-content:center" id="w4d">{stt("w4a",range(5))}{stt("w4b",range(5,10))}</div>'
W4=tw('w4t','University','Gender',['Male','Female'],[('Yes',[B('u1',2),B('u2',4)]),('No',[B('u1',2),B('u2',2)])],total=[B('u3',4),B('u3',6),B('u3',10)],totcol=[B('u3',6),B('u3',4)],fs=20)
S.append(qslide('we','Worked example 4 · 2B','Constructing a two-way frequency table',
  G('The following data were obtained when a sample of ten Year 9 students were asked if they intended to go to university (<em class="v">university</em>). The gender of the student was also recorded.',STT,'Create a two-way frequency table from these data.'),
  [('EV and RV','intention to go to university may depend on gender, not the other way round: <em>gender</em> = EV (columns), <em>university</em> = RV (rows).'),
   ('Males','Yes: 2 · No: 2',f'data-hi="#w4a|{sti("Male")}|hb;#w4b|{sti("Male")}|hb" data-fill="u1"'),
   ('Females','Yes: 4 · No: 2',f'data-hi="#w4a|{sti("Female")}|hg;#w4b|{sti("Female")}|hg" data-fill="u2"'),
   ('Sums','row sums 6, 4 · column sums 4, 6 · total 10 = the number of students','data-hi="#w4a||;#w4b||" data-fill="u3"'),
   ('TMPL',W4)],
  '',f'{CAM} · Example 4 (pp. 110–111)',video='Cambridge GO · Example 4 (2B Resources)',cmd=('Create',None,'EV across the columns, row and column sums')))
# ================= You try: Edrolo 2A WE1
E1=tw('y1t','opinion','studying status',['studying','','not studying',''],
      [('for',['20',B('s1','55.56%'),'5',B('s2','25.00%')]),('against',['16',B('s1','44.44%'),'15',B('s2','75.00%')])],total=['<b>36</b>','<b>100%</b>','<b>20</b>','<b>100%</b>'],fs=20)
S.append(qslide('yt','You try · Edrolo 2A WE1','Completing a percentaged two-way table',
  'A group of people were surveyed on their opinion towards offering a student discount for public transport. Their <em class="v">studying status</em> was recorded as ‘studying’ or ‘not studying’ along with their <em class="v">opinion</em> ‘for’ or ‘against’ the student discount.<br>Complete the percentage frequency table by filling out the missing columns with the percentage frequency of each category, rounded to two decimal places.',
  [fx('Column percentage','studying, for',F(FR([V('cell','20')],[V('column total','36')]),' × 100'),'55.56%',ra=f'data-hi="#y1t|{cells(0,[0])},90|hy"'),
   ('Studying, against','16/36 × 100 = 44.44% · column adds to 100%',f'data-hi="#y1t|{cells(1,[0])},90|hy" data-fill="s1"'),
   ('Not studying','5/20 × 100 = 25.00% · 15/20 × 100 = 75.00%',f'data-hi="#y1t|{cells(0,[2])},{cells(1,[2])},92|hb" data-fill="s2"'),
   ('TMPL',E1)],
  '',f'{EDR} · 2A Worked example 1 (pp. 106–107)',cmd=('Complete',None,'two decimal places, each column 100%')))

# ================= Learn 2B: percentaged tables and associations
PT=tw('lpt','Attitude to gun control','Residence',['Country','City'],[('For',[B('q1','55.2%'),B('q2','71.4%')]),('Against',[B('q1','44.8%'),B('q2','28.6%')])],total=['100.0%','100.0%'],fs=21)
LREP=report([('hl1','r1',['In this sample of 100 people, a higher percentage of ',('category','city people'),' were for gun control than ',('category','country people'),': ',('%','71.4%'),' to ',('%','55.2%'),'.']),
  ('hl2','r2',['This indicates that a person’s ',('RV','attitude to gun control'),' ',('is / is not','is'),' associated with their ',('EV','place of residence'),'.'])],fs=19)
body=('<div class="row" style="gap:22px;align-items:stretch"><div class="key" style="flex:.9"><h4>Why percentages?</h4><p style="font-size:20px">More country people (32) than city people (30) are for gun control, but there are more country people in the sample. Compare <b>percentages</b> within each EV category.</p>'
  f'<div style="display:flex;justify-content:center;margin-top:10px">{PT}</div>'
  '<p class="frag" style="font-size:19px;margin-top:10px"><b>Associated</b> if the % in one row differ clearly across the columns. <b>Not associated</b> if they are about the same (Year 10 vs Year 12 ban phones: 87.9% vs 86.8%).</p></div>'
  f'<div style="flex:1.1;display:flex;flex-direction:column;gap:12px"><div class="key"><h4>A report has</h4><p style="font-size:20px;line-height:1.7"><span class="hl1">1 · the context and the two % compared, from one row</span><br><span class="hl2">2 · the conclusion: associated or not</span></p></div>{LREP}</div></div>'
  '<span class="frag" data-fill="q1" data-hi="#lpt|0,10|hy"></span><span class="frag" data-fill="q2" data-hi="#lpt|1,11|hb"></span><span class="frag" data-fill="r1" data-hi="#lpt|0,1|hg"></span><span class="frag" data-fill="r2" data-hi="#lpt||"></span>')
S.append(TPL._frame('learn','Learn · 2B','Percentaged two-way tables: is there an association?',body,f'{CAM}, 2B pp. 112–113 (column %s and both reports)',cfu='disc'))
# ================= WE5: Cambridge Example 5
W5=tw('w5t','University','Gender',['Male','Female'],[('Yes',['50','54']),('No',['55','41'])],total=['105','95','200'],totcol=['104','96'],fs=19)
W5P=tw('w5p','University','Gender',['Male','Female'],[('Yes',[B('m1','47.6%'),B('m2','56.8%')]),('No',[B('m1','52.4%'),B('m2','43.2%')])],total=['100.0%','100.0%'],fs=18)
W5R=report([('hl1','v1',['In this sample of 200 Year 9 students, a greater proportion of ',('category','females'),' than ',('category','males'),' (',('%','56.8%'),' compared with ',('%','47.6%'),') were intending to go to university.']),
  ('hl2','v1',['There ',('is / is not','is'),' an association between ',('EV','gender'),' and ',('RV','intention to go to university'),'.'])],fs=17)
S.append(qslide('we','Worked example 5 · 2B','Describing an association from a percentaged table (2 × 2)',
  G('Are males and females in Year 9 equally likely to indicate an intention to go to university? Data from interviews with 200 Year 9 students are summarised in the following table. Write a brief report addressing this question and quoting appropriate percentages.',W5),
  [fx('Column percentage','male, yes',F(FR([V('cell','50')],[V('column total','105')]),' × 100%'),'47.6%',ra=f'data-hi="#w5t|0,90|hy" data-fill="m1"'),
   ('Female column','54/95 → 56.8% · 41/95 → 43.2%','data-hi="#w5t|1,91|hb" data-fill="m2"'),('TMPL',W5P),
   ('Compare one row','Yes: 56.8% of females vs 47.6% of males: clearly different, so associated.','data-hi="#w5p|0,1|hy" data-fill="v1"'),
   ('TMPL',W5R)],
  '',f'{CAM} · Example 5 (p. 114, report verbatim)',video='Cambridge GO · Example 5 (2B Resources)',cmd=('Write',None,'a report quoting %')))
# ================= You try: Edrolo 2A WE4
Y4=tw('y4t','preference','age',['under 20','','20 and over',''],[('hardcopy',['20','56%','15','75%']),('digital',['16','44%','5','25%'])],total=['<b>36</b>','<b>100%</b>','<b>20</b>','<b>100%</b>'],fs=19)
Y4R=report([('hl1','x1',['Yes, there is an association between ',('EV, RV','<em>preference</em> and <em>age</em>'),'.']),
  ('hl2','x2',['The percentage of people that prefer hardcopy books differs depending on their age, since only ',('%','56%'),' of those ',('category','under 20'),' prefer it while ',('%','75%'),' of those ',('category','aged 20 years and over'),' do.'])],fs=18)
S.append(qslide('yt','You try · Edrolo 2A WE4','Describing an association from a percentaged two-way table',
  G('A group of people were surveyed on their <em class="v">preference</em> towards reading hardcopy or digital books. Their <em class="v">age</em> (under 20, 20 and over) was recorded along with their book <em class="v">preference</em> (hardcopy, digital).<br>The results were displayed in a two-way percentage frequency table.',Y4,
    'Is there an association between <em class="v">age</em> and <em class="v">preference</em>? Justify your answer by quoting appropriate percentages.'),
  [('Compare one row','hardcopy: 56% (under 20) vs 75% (20 and over): a 19% difference.','data-hi="#y4t|1,3|hy" data-fill="x1"'),
   ('Quote the %','both percentages, with their categories','data-fill="x2"'),('TMPL',Y4R)],
  '',f'{EDR} · 2A Worked example 4 (p. 110)',cmd=('Justify',None,'quote a % for each category')))
# ================= WE6: Cambridge Example 6
W6=tw('w6t','Interest in sport','Age group (%)',['Under 18<br>years','19–25<br>years','26–35<br>years','36–50<br>years'],
      [('High',['56.5','50.2','40.7','35.0']),('Medium',['30.1','34.4','36.8','44.7']),('Low',['13.4','15.4','22.5','20.3'])],total=['100.0']*4,fs=17)
W6R=report([('hl1','z1',['There is an association between the level of interest in sport and age. ']),
  ('hl2','z2',['A high level of interest in sport is seen to decrease steadily across the age categories from ',('%','56.5%'),' for under 18 years, ',('%','50.2%'),' for 19–25 years, ',('%','40.7%'),' for 26–35 years to, at its lowest, ',('%','35%'),' for 36–50 years.'])],fs=17)
S.append(qslide('we','Worked example 6 · 2B','Describing associations from a percentaged table (3 × 3)',
  G('A survey was conducted with 1000 males under 50 years old. As part of this survey, they were asked to rate their interest in sport as ‘high’, ‘medium’, or ‘low’. Their age group was also recorded as ‘under 18’, ‘19–25’, ‘26–35’ and ‘36–50’. The results are displayed in the table.',W6,
    plist([('a','Which is the explanatory variable, <em class="v">interest in sport</em> or <em class="v">age group</em>?'),('b','Is there an association between <em class="v">interest in sport</em> and <em class="v">age group</em>? Write a brief response quoting appropriate percentages.')])),
  [('Which explains?','age could explain interest in sport, but interest in sport cannot explain age.','data-pk="0"'),('ANS','<b>a</b> &nbsp;<em class="v">Age group</em> is the EV.'),
   ('Look across the rows','the % differ for each age group in every row: associated.','data-pk="1" data-fill="z1"'),
   ('Choose one row','High: 56.5 → 50.2 → 40.7 → 35.0, a steady decrease.',f'data-pk="1" data-hi="#w6t|{cells(0,[0,1,2,3])}|hy" data-fill="z2"'),('TMPL','<b>b</b> '+W6R)],
  '',f'{CAM} · Example 6 (pp. 115–116)',video='Cambridge GO · Example 6 (2B Resources)',cmd=('Write',None,'a response quoting %')))
# ================= You try: Edrolo 2A WE2 (grouped bar chart)
CF=[[22,16,10,2],[5,10,14,17],[3,4,6,11]]
CT=tw('y2t','caffeine intake','age',['20–29','30–39','40–49','50–59'],[('low',[str(x) for x in CF[0]]),('medium',[str(x) for x in CF[1]]),('high',[str(x) for x in CF[2]])],fs=17)
S.append(qslide('yt','You try · Edrolo 2A WE2','Constructing a grouped bar chart',
  G('A group of individuals between the ages of 20 and 59 were asked how much coffee they drink a day. Their <em class="v">caffeine intake</em> was categorised as ‘low’, ‘medium’ and ‘high’. Their <em class="v">age</em> was also recorded and grouped as ‘20–29’, ‘30–39’, ‘40–49’ and ‘50–59’. The results are displayed in a two-way frequency table.',CT,
    'Use the frequency table to construct a grouped bar chart.'),
  [('EV','<em>age</em> is more likely to dictate <em>caffeine intake</em>: age goes on the horizontal axis.'),
   ('Axes','frequency up, to at least 22 (the largest value); the four age groups across.','data-ax="#y2g"'),
   ('20–29','bars 22, 5, 3 (low, medium, high)',f'data-hi="#y2t|{cells(0,[0])},{cells(1,[0])},{cells(2,[0])}|hy" data-grow="#y2g|0;#y2g|1;#y2g|2"'),
   ('30–39','16, 10, 4',f'data-hi="#y2t|{cells(0,[1])},{cells(1,[1])},{cells(2,[1])}|hy" data-grow="#y2g|3;#y2g|4;#y2g|5"'),
   ('40–49, 50–59','10, 14, 6 · 2, 17, 11; add a legend',f'data-hi="#y2t|{cells(0,[2,3])},{cells(1,[2,3])},{cells(2,[2,3])}|hy" data-grow="#y2g|6;#y2g|7;#y2g|8;#y2g|9;#y2g|10;#y2g|11"'),
   ('TMPL','<div style="width:470px">'+gbar('y2g',['20–29','30–39','40–49','50–59'],['low','medium','high'],CF,25,5,'age','frequency',Hh=300)+'</div>')],
  '',f'{EDR} · 2A Worked example 2 (pp. 107–108)',cmd=('construct',None,'axes, a bar for each RV category, legend')))

# ================= Learn 2B: the segmented bar chart
SM=tw('lsm','Smoking status','Education level (%)',['Year 9<br>or less','Year 10<br>or 11','Year 12','University'],
      [('Smoker',['34.0','31.7','26.5','18.4']),('Past smoker',['36.0','33.8','30.9','28.0']),('Never smoked',['30.0','34.5','42.6','53.6'])],total=['100.0']*4,fs=16)
smg=seg('lsg',{"bars":[{"v":[34.0,36.0,30.0],"label":"Yr 9 or less"},{"v":[31.7,33.8,34.5],"label":"Yr 10 or 11"},{"v":[26.5,30.9,42.6],"label":"Yr 12"},{"v":[18.4,28.0,53.6],"label":"University"}],
     "names":["Smoker","Past smoker","Never smoked"],"legendTop":["Never smoked","Past smoker","Smoker"],"yl":"Percentage","xl":"Level of education","ticks":20,"h":380},True,True)
grow=lambda b:';'.join(f'#lsg|{3*b+j}' for j in range(3))
body=('<div class="row" style="gap:22px;align-items:stretch"><div class="key" style="flex:1"><h4>Percentaged two-way table</h4><div style="display:flex;justify-content:center">'+SM+'</div>'
  '<ul class="bul" style="font-size:19px;line-height:1.5;margin:12px 0 0 24px"><li>one bar for each <b>EV</b> category (each column of the table)</li><li>each bar is 100%, split into <b>RV</b> segments</li><li>same colour for the same RV category in every bar, plus a key</li></ul></div>'
  f'<div class="key" style="flex:1.1"><h4>Percentage segmented bar chart</h4>{smg}</div></div>'
  '<span class="frag" data-ax="#lsg"></span>'+''.join(f'<span class="frag" data-hi="#lsm|{b},{10+b},{20+b},{90+b}|hy" data-grow="{grow(b)}"{" data-lg" if b==3 else ""}></span>' for b in range(4))+
  '<span class="frag" data-hi="#lsm||"></span><div class="tip frag" style="margin-top:12px">Look across one segment: smokers fall from 34.0% to 18.4% as education level rises, so smoking status is associated with education level.</div>')
S.append(TPL._frame('learn','Learn · 2B','The segmented bar chart: table → bars',body,f'{CAM}, 2B pp. 115–116 (smoking table and chart)',cfu='disc'))
# ================= WE7: Cambridge Example 7
W7=W6.replace('id="w6t"','id="w7t"')
w7g=seg('w7g',{"bars":[{"v":[56.5,30.1,13.4],"label":"under 18"},{"v":[50.2,34.4,15.4],"label":"19–25"},{"v":[40.7,36.8,22.5],"label":"26–35"},{"v":[35.0,44.7,20.3],"label":"36–50"}],
     "names":["High","Medium","Low"],"legendTop":["Low","Medium","High"],"yl":"Interest in sport (%)","xl":"Age group (years)","ticks":10,"h":340},True,True)
S.append(qslide('we','Worked example 7 · 2B','Constructing a segmented bar chart',
  G('Construct a segmented bar chart to display the association <em class="v">interest in sport</em> and <em class="v">age group</em> displayed in the table in Example 6.',W7),
  [('Axes','<em>age group</em> is the EV: horizontal axis. Vertical axis 0% to 100%, in intervals of 10%.','data-ax="#w7g"'),
   ('under 18','High to 56.5 · Medium to 86.6 · Low to 100',f'data-hi="#w7t|0,10,20|hy" data-grow="#w7g|0;#w7g|1;#w7g|2"'),
   ('19–25','50.2 · 84.6 · 100',f'data-hi="#w7t|1,11,21|hy" data-grow="#w7g|3;#w7g|4;#w7g|5"'),
   ('26–35, 36–50','40.7 · 77.5 · 100 &nbsp;|&nbsp; 35.0 · 79.7 · 100; add the key',f'data-hi="#w7t|2,12,22,3,13,23|hy" data-grow="#w7g|6;#w7g|7;#w7g|8;#w7g|9;#w7g|10;#w7g|11" data-lg'),
   ('TMPL','<div style="width:540px">'+w7g+'</div>')],
  '',f'{CAM} · Example 7 (pp. 116–117)',video='Cambridge GO · Example 7 (2B Resources)',cmd=('Construct',None,'EV across, 100% bars, key')))
# ================= You try: Edrolo 2A WE3
HT_=tw('y3t','height','year level',['Year 11','Year 12'],[('short',['15%','20%']),('average',['20%','30%']),('tall',['65%','50%'])],total=['<b>100%</b>','<b>100%</b>'],fs=19)
y3g=seg('y3g',{"bars":[{"v":[15,20,65],"label":"Year 11"},{"v":[20,30,50],"label":"Year 12"}],"names":["short","average","tall"],"legendTop":["short","average","tall"],"yl":"frequency (%)","xl":"year level","ticks":10,"h":320},True,True)
S.append(qslide('yt','You try · Edrolo 2A WE3','Constructing a percentage segmented bar chart',
  G('A group of students in Year 11 and Year 12 were asked to describe their <em class="v">height</em> as ‘short’, ‘average’ or ‘tall’. Their responses, as well as their <em class="v">year level</em>, were recorded in the following percentage frequency table.',HT_,
    'Use the frequency table to construct a percentage segmented bar chart.'),
  [('EV','<em>year level</em> is more likely to dictate <em>height</em>: horizontal axis. Vertical axis 0 to 100%.','data-ax="#y3g"'),
   ('Year 11','short ends at 15 · average at 15 + 20 = 35 · tall at 35 + 65 = 100','data-hi="#y3t|0,10,20|hy" data-grow="#y3g|0;#y3g|1;#y3g|2"'),
   ('Year 12','20 · 20 + 30 = 50 · 50 + 50 = 100; add a legend','data-hi="#y3t|1,11,21|hy" data-grow="#y3g|3;#y3g|4;#y3g|5" data-lg'),
   ('TMPL','<div style="width:520px">'+y3g+'</div>')],
  '',f'{EDR} · 2A Worked example 3 (p. 109)',cmd=('construct',None,'EV across, 100% bars, legend')))
# ================= WE8: Cambridge Example 8
w8g=seg('w8g',{"bars":[{"v":[75,25],"label":"under 40"},{"v":[60,40],"label":"40 and over"}],"names":["coast","country"],"legendTop":["country","coast"],"yl":"Preferred holiday (%)","xl":"Age group","ticks":10,"h":330})
W8R=report([('hl1','w1',['There ',('is / is not','is'),' an association between the ',('RV','holiday preference'),' and ',('EV','age'),'. ']),
  ('hl2','w2',['Those aged under forty are more likely to choose a coastal holiday (',('%','75%'),') than those aged forty or over (',('%','60%'),').'])],fs=19)
S.append(qslide('we','Worked example 8 · 2B','Identifying and describing associations from a segmented bar chart',
  G('The percentaged segmented bar chart below shows the association between <em class="v">preferred holiday</em> (country or coast) and <em class="v">age group</em> (under 40, 40 or over) for a sample of 800 visitors to a travel website.',
    '<div style="width:560px">'+w8g+'</div>','Does the percentaged segmented bar chart support the contention there is an association between <em class="v">preferred holiday</em> and <em class="v">age group</em>?'),
  [('Look across','the segment heights (percentages) differ for each age group: associated.','data-fill="w1"'),
   ('Choose one segment','coast: 75% (under 40) vs 60% (40 and over)','data-hi="#w8g|0|hy" data-fill="w2"'),('TMPL',W8R)],
  '',f'{CAM} · Example 8 (p. 117)',video='Cambridge GO · Example 8 (2B Resources)',cmd=('Does',None,'yes/no, quoting two %')))
# ================= You try: Edrolo 2A WE5
y5g=seg('y5g',{"bars":[{"v":[40,60],"label":"18–21"},{"v":[75,25],"label":"22–25"}],"names":["employed","unemployed"],"legendTop":["unemployed","employed"],"yl":"frequency (%)","xl":"age","ticks":10,"h":320})
Y5R=report([('hl1','e1',['Yes, there is an association between ',('RV','<em>employment status</em>'),' and ',('EV','<em>age</em>'),'. ']),
  ('hl2','e2',['The percentage of people that are employed tends to increase with age, with ',('%','40%'),' of 18–21 year olds employed and ',('%','75%'),' of 22–25 year olds employed.'])],fs=19)
S.append(qslide('yt','You try · Edrolo 2A WE5','Describing an association from a percentage segmented bar chart',
  G('A large group of people between the ages of 18 and 25 were asked what their current <em class="v">employment status</em> was. They were classified as either ‘employed’ or ‘unemployed’. Their <em class="v">age</em> was also recorded and classified as ‘18–21’ or ‘22–25’.<br>The results have been displayed in a percentage segmented bar chart.',
    '<div style="width:540px">'+y5g+'</div>','Is there an association between <em class="v">employment status</em> and <em class="v">age</em>? Justify your answer by quoting appropriate percentages.'),
  [('Compare one segment','employed: 40% (18–21) vs 75% (22–25): a 35% difference.','data-hi="#y5g|0,2|hy" data-fill="e1"'),
   ('Quote the %','both percentages, with their age groups','data-fill="e2"'),('TMPL',Y5R)],
  '',f'{EDR} · 2A Worked example 5 (pp. 110–111)',cmd=('Justify',None,'quote a % for each category')))

# ================= Exits
UK=[('Belfast','high','small',52),('Edinburgh','high','small',43),('London','high','large',40),('Manchester','high','large',44),('Brighton and Hove','high','small',35),('Bournemouth','high','small',36),
    ('Sheffield','medium','small',36),('Hull','medium','small',40),('Bristol','medium','small',39),('Newcastle-Sunderland','medium','large',34),('Leicester','medium','small',36),('Liverpool','medium','large',29),
    ('Swansea','low','small',30),('Glasgow','low','large',34),('Cardiff','low','small',31),('Nottingham','low','small',31),('Birmingham-Wolverhampton','low','large',29),('Leeds-Bradford','low','large',31),
    ('Portsmouth','low','small',27),('Southampton','low','small',30),('Reading','low','small',31),('Coventry','low','small',30),('Stoke-on-Trent','low','small',29)]
def ukt(rid,rng): return ('<table class="t tight" id="'+rid+'" style="font-size:13px;line-height:1"><tr><th><em>City</em></th><th><em>Congestion level</em></th><th><em>Size</em></th><th><em>Increase in travel time</em><br>(minutes per day)</th></tr>'+
    ''.join(f'<tr><td class="l" style="padding:1px 5px"><span data-i="{i}">{UK[i][0]}</span></td><td style="padding:1px 5px"><span data-i="{i}">{UK[i][1]}</span></td><td style="padding:1px 5px"><span data-i="{i}">{UK[i][2]}</span></td><td style="padding:1px 5px"><span data-i="{i}">{UK[i][3]}</span></td></tr>' for i in rng)+'</table>')
uki=lambda c,s:','.join(str(i) for i,u in enumerate(UK) if u[1]==c and u[2]==s)
EX1=tw('x1t','Congestion level','City size',['Small','Large'],[('high',['4',B('k1',2)]),('medium',[B('k2',4),B('k2',2)]),('low',[B('k3',8),B('k3',3)])],total=['16',B('k4',7)],fs=19)
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2018 Exam 2 Q1d','Show what you know',
  G('<span style="font-size:16px;line-height:1.25;display:block">The data in Table 1 relates to the impact of traffic congestion in 2016 on travel times in 23 cities in the United Kingdom (UK).<br>The four variables in this data set are: <em class="v">city</em> – name of city · <em class="v">congestion level</em> – traffic congestion level (high, medium, low) · <em class="v">size</em> – size of city (large, small) · <em class="v">increase in travel time</em> – increase in travel time due to traffic congestion (minutes per day).</span>',
    f'<div class="row" style="gap:8px;justify-content:center;align-items:flex-start">{ukt("x1a",range(12))}{ukt("x1b",range(12,23))}</div>',
    'Use the data in Table 1 to complete the following two-way frequency table, Table 2. <span class="muted">(2 marks)</span>'),
  [('High, large','London, Manchester: 2',f'data-hi="#x1a|{uki("high","large")}|hy" data-fill="k1"'),
   ('Medium','small: 4 · large: 2',f'data-hi="#x1a|{uki("medium","small")}|hb;#x1b|{uki("medium","small")}|hb" data-fill="k2"'),
   ('Low','small: 8 · large: 3',f'data-hi="#x1b|{uki("low","small")}|hg" data-fill="k3"'),
   ('Total large','2 + 2 + 3 = 7 · check: 16 + 7 = 23 cities','data-hi="#x1a||;#x1b||" data-fill="k4"'),
   ('TMPL','<div style="font-size:15px;font-weight:700;margin-bottom:4px">Table 2</div>'+EX1,'','data-stat="94"')],
  '',f'{EDR} · 2A Q11 · VCAA 2018 Further Mathematics Exam 2 Core Q1d (examiner report: average 1.9 out of 2)',stat=('mark',94),cmd=('complete',2,'every cell and the total')))
c21=seg('x2g',{"bars":[{"v":[35,65],"label":"under 55 years"},{"v":[55,45],"label":"55 years and over"}],"names":["international","domestic"],"legendTop":["domestic","international"],"yl":"percentage","xl":"age (years)","ticks":10,"h":300})
def ot(d,i,t): return (f'<table class="t tight" style="font-size:12px;line-height:1;display:inline-table;vertical-align:top"><tr><th class="l" style="padding:1px 4px"></th><th style="padding:1px 4px">Under 55</th><th style="padding:1px 4px">55 and over</th></tr>'
    f'<tr><td class="l" style="padding:1px 4px">domestic</td><td>{d[0]}</td><td>{d[1]}</td></tr><tr><td class="l" style="padding:1px 4px">international</td><td>{i[0]}</td><td>{i[1]}</td></tr><tr><td class="l" style="padding:1px 4px"><b>Total</b></td><td>{t[0]}</td><td>{t[1]}</td></tr></table>')
OPTS=[ot((91,90),(49,110),(140,200)),ot((65,35),(45,55),(110,90)),ot((35,55),(65,45),(100,100)),ot((50,70),(100,50),(150,120)),ot((71,39),(29,61),(100,100))]
x2=qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 1 Q3','Show what you know',
  G('<span style="font-size:17px">The percentaged segmented bar chart below shows the <em class="v">age</em> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <em class="v">preferred travel destination</em> (domestic, international).</span>',
    '<div style="width:320px">'+c21+'</div>','<span style="font-size:17px">The results could also be summarised in a two-way frequency table.<br>Which one of the following frequency tables could match the percentaged segmented bar chart?</span>'),
  [('Read the chart','under 55: 65% domestic, 35% international · 55 and over: 45% domestic, 55% international'),
   ('Test each table','work out column %s: A: 91/140 = 65%, 49/140 = 35%, 90/200 = 45%, 110/200 = 55% ✓')],
  'Table <b>A</b> matches the chart.',f'{EDR} · 2A Q13 · VCAA 2021 Further Mathematics Exam 1 Core Q3 (examiner report)',stat=('mc',50),
  mc=OPTS,key='A',dist=[50,13,28,1,8],dis=('C','28% chose this: its domestic and international rows are swapped (35% domestic under 55), so they read the key the wrong way round.'))
x2=x2.replace('<section class="slide T ex mcslide"','<section class="slide T ex mcslide x2"',1)
S.append('<style>.x2 .L .mc{display:grid;grid-template-columns:1fr 1fr;gap:2px 8px}.x2 .L .mc>div{padding:1px 50px 1px 6px;display:flex;gap:6px;align-items:flex-start}.x2 .L .q{font-size:17px}.x2 .L .q>div{margin:4px 0!important}</style>'+x2)

# ================= closing
S.append(checkin(SC))
CW=CARD['homework']['sets']
S.append(coursework([(st['title'].replace('Revision book','Chapter 2 revision booklet'),st.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st['items']]) for st in CW]))
V=json.load(open(os.path.join(ROOT,'planner','videos.json'))); V=V if isinstance(V,list) else V.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V if v['sub'] in ('2A','2B') and v.get('url')]))
n=assemble(S,'12MAG · L03 · Associations between two categorical variables',os.path.join(ROOT,'lessons','2A-2B slides.html'))
print(n,'slides')
