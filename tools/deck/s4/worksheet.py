"""Lesson 4 (1G) guided worksheet, in the S1 worksheet house style (A4, black and white, answers in red on the solutions copy).
Question text is copied verbatim from tools/deck/s4/build.py (which copied it from the sources); keep the two in step.
Run: python3 tools/deck/s4/worksheet.py  ->  lessons/S4-worksheet.html + lessons/S4-worksheet-solutions.html (PDFs: tools/deck/s4/ws_pdf.py)"""
import os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
CSS=open(os.path.join(H,'ws.css')).read()
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
RED='#c00'

# ---------------------------------------------------------------- figures (static SVG)
def _fmt(v,dec=0): return f'{v:.{dec}f}' if dec else (str(int(v)) if float(v).is_integer() else str(v))
def axis_svg(mn,mx,step,lab=None,xl='',W=340,dec=0,body='',top=26,extra_h=0):
    lab=lab or step; L,R=14,14; s=lambda v:L+(v-mn)/(mx-mn)*(W-L-R); y=top+30
    o=[f'<line x1="{L}" y1="{y}" x2="{W-R}" y2="{y}" stroke="#000" stroke-width="1"/>']
    n=round((mx-mn)/step)
    for i in range(n+1):
        v=mn+i*step; big=abs(((v-mn)/lab)-round((v-mn)/lab))<1e-6
        o.append(f'<line x1="{s(v):.1f}" y1="{y}" x2="{s(v):.1f}" y2="{y+(5 if big else 3)}" stroke="#000" stroke-width="{0.9 if big else 0.6}"/>')
        if big: o.append(f'<text x="{s(v):.1f}" y="{y+14}" text-anchor="middle" font-size="9">{_fmt(round(v,6),dec)}</text>')
    if xl: o.append(f'<text x="{W/2}" y="{y+26}" text-anchor="middle" font-size="9">{xl}</text>')
    h=y+(30 if xl else 19)+extra_h
    return f'<svg viewBox="0 0 {W} {h}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}{body(s,y) if callable(body) else body}</svg>'
def boxplot(mn,mx,step,lw,q1,m,q3,uw,out=(),lab=None,xl='',dec=0,draw=True,caps=False,fences=(),W=340):
    """draw=True: black boxplot to read from. draw=False: blank axis for students; the boxplot appears in red on the solutions copy."""
    def body(s,y):
        c='#000' if draw else RED; cls='' if draw else ' class="solfig"'; yc=y-14; bh=16
        o=[f'<g{cls} stroke="{c}" fill="none" stroke-width="1.2">',
           f'<rect x="{s(q1):.1f}" y="{yc-bh/2}" width="{s(q3)-s(q1):.1f}" height="{bh}" fill="{"#fff" if draw else "none"}"/>',
           f'<line x1="{s(m):.1f}" y1="{yc-bh/2}" x2="{s(m):.1f}" y2="{yc+bh/2}" stroke-width="1.8"/>',
           f'<line x1="{s(lw):.1f}" y1="{yc}" x2="{s(q1):.1f}" y2="{yc}"/><line x1="{s(q3):.1f}" y1="{yc}" x2="{s(uw):.1f}" y2="{yc}"/>']
        if caps: o+= [f'<line x1="{s(x):.1f}" y1="{yc-5}" x2="{s(x):.1f}" y2="{yc+5}"/>' for x in (lw,uw)]
        o+= [f'<circle cx="{s(x):.1f}" cy="{yc}" r="2.6" fill="{c}"/>' for x in out]
        for fx,t in fences: o.append(f'<line x1="{s(fx):.1f}" y1="{yc-15}" x2="{s(fx):.1f}" y2="{y}" stroke-dasharray="3 2" stroke-width=".9"/><text x="{s(fx):.1f}" y="{yc-17}" font-size="8" fill="{c}" stroke="none" text-anchor="middle">{t}</text>')
        return ''.join(o)+'</g>'
    return axis_svg(mn,mx,step,lab,xl,W,dec,body,top=30 if fences else 22)
def dotplot(mn,mx,vals,xl='',r=4,W=340,lab=1):
    from collections import Counter
    c=Counter(vals); hmax=max(c.values()); dy=2*r*0.95
    def body(s,y): return ''.join(f'<circle cx="{s(v):.1f}" cy="{y-r-1-k*dy:.1f}" r="{r}" fill="#fff" stroke="#000" stroke-width=".7"/>' for v,f in c.items() for k in range(f))
    return axis_svg(mn,mx,1,lab,xl,W,0,body,top=max(4,hmax*dy-24))
def stem(rows,key):
    return '<table class="stem">'+''.join(f'<tr><td class="st">{a}</td><td>{" ".join(map(str,b))}</td></tr>' for a,b in rows)+f'</table><div class="key">{key}</div>'

# ---------------------------------------------------------------- building blocks (S1 classes)
def ans(t,inline=False): return f'<span class="ans in">{t}</span>' if inline else f'<div class="ans">{t}</div>'
def lines(n,a=''):
    return f'<div class="lines" style="position:relative">{"<div></div>"*n}'+(f'<div class="ans" style="position:absolute;top:1.5mm;left:0;right:0;line-height:8mm;font-size:9.5pt">{a}</div>' if a else '')+'</div>'
def blank(a,w=30): return f'<span class="blank" style="min-width:{w}mm"><u>{a}</u></span>'
def five(vals=None,lab=('min','Q<sub>1</sub>','M','Q<sub>3</sub>','max')):
    v=vals or ['']*5
    return '<table class="t fill5"><tr>'+''.join(f'<th>{l}</th>' for l in lab)+'</tr><tr>'+''.join(f'<td><span class="ans in">{x}</span></td>' for x in v)+'</tr></table>'
def parts(items,cols=1):
    return f'<div class="parts" style="grid-template-columns:repeat({cols},minmax(0,1fr))">'+''.join(f'<div class="pt"><b>{k}</b><div>{q}<div class="pl">{ans(a,True)}</div></div></div>' for k,q,a in items)+'</div>'
def mc(opts,cols=1): return f'<div class="mc" style="grid-template-columns:repeat({cols},auto)">'+''.join(f'<div><b>{"ABCDE"[i]}.</b>{o}</div>' for i,o in enumerate(opts))+'</div>'
def guess(a,mcq=True):
    return (f'<div class="guess" data-a="{a}">Guess: <b>%</b> of students who got this right <span></span>'+(' &nbsp; Most common wrong answer <span class="sh"></span>' if mcq else '')+'</div>')
def cite(t): return f'<div class="cite">{t}</div>'
def q(t): return f'<p class="q">{t}</p>'
def box(hd,body,right='',cls=''): return f'<div class="box {cls}"><div class="hd">{hd}<span>{right}</span></div><div class="bd">{body}</div></div>'
def pair(h1,b1,h2,b2): return f'<div class="pair"><div class="hd">{h1}</div><div class="hd">{h2}</div><div class="bd">{b1}</div><div class="bd">{b2}</div></div>'
def item(n,body,fig='',sep=True):
    st=' style="border-top:1px dashed #bbb;padding-top:2mm;margin-top:2mm"' if sep else ''
    return f'<div class="row"{st}><div style="flex:1">{body}</div>'+(f'<div class="fig">{fig}</div>' if fig else '')+'</div>'

# ---------------------------------------------------------------- content
P=[]
P.append(f'<div class="title"><div class="code">1G</div><h1>The five-number summary and the boxplot <span class="solmark">· SOLUTIONS</span></h1><div class="pg">{CAM}<br>Chapter 1 · 1G</div></div>')
LI=['To be able to construct the boxplot for displaying the distribution of a numerical data.','To be able to define and identify outliers.',
    'To be able to construct both simple boxplots and boxplots with outliers.','To be able to determine the features of a distribution from a boxplot.',
    'To be able to use a CAS calculator to construct a boxplot.']
P.append(box('Learning intentions','<ul class="ki">'+''.join(f'<li>{x}</li>' for x in LI)+'</ul>'))
# ---- APK
PARTY='The ages of a group of people at a party:<div class="data">19 21 22 56 34 19 27 28 34 17 66 37 20 20 21 45 26 19 23 29</div>'
apk=(q(PARTY)
 +item('1',q('<b>1.</b> Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).')+five(['17','20','24.5','34','66']),
       boxplot(15,70,5,17,20,24.5,34,66,xl='age (years)',draw=False),sep=False)
 +cite('Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #14')
 +item('2',q('<b>2.</b> Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).')
       +lines(3,'IQR = 34 − 20 = 14 · LF = 20 − 1.5 × 14 = −1 · UF = 34 + 1.5 × 14 = 55<br>56 &gt; 55 = UF → outlier · 66 &gt; 55 = UF → outlier · 17 &gt; −1 = LF → no low outliers<br>The fences are −1 and 55. The outliers are 56 and 66.'))
 +cite('Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #15')
 +item('3',q('<b>3.</b> The boxplot shows the distribution of the <i>reaction time</i> (milliseconds), of 256 firefighters.')+q('The five-number summary for the <i>reaction time</i> of these 256 firefighters is closest to')
       +mc(['70, 130, 140, 152, 179','70, 130, 140, 152, 255','122, 130, 140, 152, 179','122, 130, 140, 152, 245','122, 130, 140, 152, 265'],cols=2)+ans('B: the outlier dots (70, 90, 255) are data, so min = 70 and max = 255. Distractor C (whisker ends).'),
       boxplot(0,260,10,122,130,140,152,179,out=(70,90,255),lab=50,xl='reaction time (milliseconds)',caps=True))
 +guess('58% · C')+cite('Edrolo General Mathematics Units 1&amp;2 · 1F Q16 · Adapted from VCAA 2017 Exam 1 Data analysis Q2'))
P.append(box('Activating prior knowledge',apk,'Year 11',cls='split'))

# ---- Example 22 / You try (Edrolo 1E WE4)
life=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
w4=[('0',[1,2,3,5,5,9]),('1',[0,0,1,5,8,9]),('2',[1,2,3,3,5]),('3',[3,7,9])]
P.append(pair('Example 22 · Constructing a boxplot from a five-number summary',
  q('The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:')
  +f'<div class="row" style="justify-content:center;gap:4mm;align-items:center"><div style="flex:none">{stem(life,"Key: 5|2 = 52 years")}</div>'+five(["52","66","73","75","77"]).replace('<span class="ans in">','<span>')+'</div>'
  +q('Use the five-number summary to construct a boxplot.')+boxplot(50,80,1,52,66,73,75,77,lab=5,xl='Life expectancy (years)',draw=False)+cite(f'{CAM} · Example 22'),
  'You try · Edrolo 1E WE4',
  q('The five-number summary for the following stem plot is: <b>1, 7, 16.5, 23, 39</b>')+f'<div style="display:flex;justify-content:center">{stem(w4,"Key: 1 | 2 = 12")}</div>'
  +q('Construct a boxplot using the data.')+lines(2,'IQR = 23 − 7 = 16 · LF = 7 − 1.5 × 16 = −17 · UF = 23 + 1.5 × 16 = 47<br>1 &gt; −17 = LF and 39 &lt; 47 = UF → no outliers')
  +boxplot(0,40,1,1,7,16.5,23,39,lab=5,draw=False)+cite(f'{EDR} · 1E Worked example 4')))

# ---- CAS 4 / You try (Edrolo 1E WE5, CAS)
P.append(pair('CAS 4 · Boxplot with outliers on CAS',
  q('Display the following set of 19 marks in the form of a boxplot with outliers.')+'<div class="data">28 21 21 3 22 31 35 26 27 33<br>43 31 30 34 48 36 35 23 24</div>'
  
  +'<p class="q" style="margin-top:1mm">Read from the CAS:</p>'+five(['3 (outlier)','23','30','35','48'])
  +boxplot(0,55,1,21,23,30,35,48,out=(3,),lab=5,xl='marks',draw=False)+cite(f'{CAM}, 1G pp. 64–66 (CAS 4)'),
  'You try · Edrolo 1E WE5 (CAS)',
  q('Construct a boxplot for the following data set.')+'<div class="data">2 4 4 5 5 5 7 6 5 4 6 5 6 7 8 12 3 5</div>'
  +five(['2','4','5','6','12'])
  +lines(3,'IQR = 6 − 4 = 2 · LF = 4 − 1.5 × 2 = 1 · UF = 6 + 1.5 × 2 = 9<br>12 &gt; 9 = UF → outlier · 2 &gt; 1 = LF → not an outlier<br>Upper whisker stops at 8, the last value inside the fence.')
  +boxplot(0,13,1,2,4,5,6,8,out=(12,),xl='list',draw=False,fences=((1,'LF 1'),(9,'UF 9')))+cite(f'{EDR} · 1E Worked example 5')))

# ---- Example 23 / You try (Edrolo 1E WE6)
P.append(pair('Example 23 · Reading values from a boxplot',
  q('For the boxplot shown, write down the values of:')+boxplot(0,100,2,10,30,36,44,60,out=(4,70,84,92),lab=10)
  +parts([('a','the median','36'),('b','the quartiles Q<sub>1</sub> and Q<sub>3</sub>','Q<sub>1</sub> = 30, Q<sub>3</sub> = 44'),('c','the interquartile range (IQR)','IQR = 44 − 30 = 14'),
          ('d','the minimum and maximum values','min = 4, max = 92'),('e','the values of any possible outliers','4, 70, 84 and 92'),
          ('f','the smallest value in the upper end of the data set that will be classified as an outlier','UF = 44 + 1.5 × 14 = 65: any value above 65'),
          ('g','the largest value in the lower end of the data set that will be classified as an outlier.','LF = 30 − 1.5 × 14 = 9: any value below 9')])+cite(f'{CAM} · Example 23'),
  'You try · Edrolo 1E WE6',
  q('The <i>number of runs scored</i> by the leading batsman at a local cricket club is represented by the following boxplot.<br>It is known that data was collected from 20 separate innings.')
  +boxplot(0,100,5,30,50,70,80,90,lab=10,xl='number of runs scored',caps=True)
  +parts([('a.','Determine the five-number summary for the data and identify any outliers.','30, 50, 70, 80, 90; no dots, so no outliers'),
          ('b.','Between which two values does the middle 50% of data lie?','50 and 80 runs (Q<sub>1</sub> to Q<sub>3</sub>)'),
          ('c.','In approximately what percentage of innings did they score more than 80 runs?','25% (above Q<sub>3</sub>)'),
          ('d.','In approximately how many innings did they score at least 50 runs, but fall short of 100?','75% of 20 = 0.75 × 20 = 15 innings')])+cite(f'{EDR} · 1E Worked example 6')))

# ---- Example 24 (no You try)
P.append(box('Example 24 · Estimating percentages from a boxplot',
  f'<div class="row"><div style="flex:1">{q("For the boxplot shown, estimate the percentage of values:")}{boxplot(45,85,1,50,54,55,59,65,out=(70,81),lab=5)}</div><div style="flex:1.1">'
  +parts([('a','less than 54','25% (Q<sub>1</sub>)'),('b','less than 55','50% (median)'),('c','less than 59','75% (Q<sub>3</sub>)'),('d','greater than 59','25%'),('e','between 54 and 59','50%'),('f','between 54 and 86.','75%')],cols=2)
  +'</div></div>'+cite(f'{CAM} · Example 24'),'No matching Edrolo worked example'))

# ---- Shape + Example 25 / You try (Edrolo 1F WE5)
TPL=lambda a,b,c,d,e:(f'<div class="tpl">The distribution is {blank(a,34)} with {blank(b,22)}. The distribution is centred at {blank(c,12)}, the median value. '
                      f'The spread of the distribution, as measured by the IQR, is {blank(d,12)} and, as measured by the range, {blank(e,12)}.</div>')
P.append(pair('Example 25 · Describing a distribution without outliers',
  q('Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.')+boxplot(0,50,1,0,5,10,21,45,lab=5)
  +TPL('positively skewed','no outliers','10','16','45')+cite(f'{CAM} · Example 25'),
  'You try · Edrolo 1F WE5',
  q('Consider the boxplot.')+boxplot(12,20,0.5,12,15,18,19,20,lab=2,caps=True)+q('Describe the distribution in terms of shape, centre, spread and outliers.')
  +lines(4,'The boxplot is negatively skewed with no outliers, a median of 18 and a range of 20 − 12 = 8.')+cite(f'{EDR} · 1F Worked example 5')))

# ---- Example 26 / Example 27 (no You try)
P.append(pair('Example 26 · Describing a distribution with outliers',
  q('Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.')+boxplot(0,50,1,34,38.75,41,44.25,47,out=(10,15,20,25),lab=5)
  +lines(4,'The distribution is symmetric but with outliers. The distribution is centred at 41, the median value. The spread of the distribution, as measured by the IQR, is 5.5 and, as measured by the range, 37. There are four outliers: 10, 15, 20 and 25.')
  +cite(f'{CAM} · Example 26'),
  'Example 27 · Using a boxplot to answer statistical questions',
  q('The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.')
  +boxplot(25,43,1,35,38,39,40,42,out=tuple(range(25,35)),xl='Gestation period (weeks)')
  +lines(5,'The distribution of gestational period is negatively skewed with several outliers. The distribution is centred at 39 weeks, the median value. The range of the distribution is 17 weeks, but the interquartile range is only 2 weeks. Any gestational period less than 35 weeks or less is considered unusual, with outliers at 25, 26, …, 34 weeks.')
  +cite(f'{CAM} · Example 27')))

# ---- Exit tasks
neck={31:1,32:1,33:3,34:11,35:19,36:32,37:34,38:48,39:39,40:18,41:28,42:12,43:3,44:1}
nv=[k for k,f in neck.items() for _ in range(f)]
hep=[(1,'1.76','15.34','41.22'),(2,'1.79','16.96','42.41'),(3,'1.83','13.87','46.53'),(4,'1.82','14.23','40.53'),(5,'1.87','13.78','40.62'),(6,'1.73','14.50','45.62'),(7,'1.68','15.08','42.33'),(8,'1.82','13.13','40.88'),(9,'1.83','14.22','39.22'),(10,'1.87','13.62','42.51'),(11,'1.87','12.01','42.75'),(12,'1.80','12.88','38.12'),(13,'1.83','12.68','42.65'),(14,'1.87','12.45','41.32'),(15,'1.78','11.31','42.88')]
ht='<table class="t tiny"><tr><th>athlete number</th><th>high jump (metres)</th><th>shot-put (metres)</th><th>javelin (metres)</th></tr>'+''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in hep)+'</table>'
FT='<table class="t" style="width:100%;font-size:9pt"><tr><th>minimum</th><th>first quartile (Q<sub>1</sub>)</th><th>median</th><th>third quartile (Q<sub>3</sub>)</th><th>maximum</th></tr><tr><td>31</td><td>36</td><td>38</td><td>39</td><td>44</td></tr></table>'
ex=(item('1',q('<b>1.</b> The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.')
         +q('The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.')+FT
         +q('Use the five-number summary to construct a boxplot, showing any outliers if appropriate. <i>(2 marks)</i>')
         +lines(3,'IQR = 39 − 36 = 3 · LF = 36 − 1.5 × 3 = 31.5 · UF = 39 + 1.5 × 3 = 43.5<br>31 &lt; 31.5 → outlier · 44 &gt; 43.5 → outlier · whiskers to 32 and 43'),
         dotplot(30,45,nv,'neck size (cm)',r=1.15,W=300)+boxplot(30,45,1,32,36,38,39,43,out=(31,44),xl='neck size (cm)',draw=False,W=300),sep=False)
    +guess('55% (average mark)',mcq=False)+cite(f'{EDR} · 1E Q19 · VCAA 2020 Exam 2 Data analysis Q2c')
    +item('2',q('<b>2.</b> In the sport of heptathlon, athletes compete in seven events. These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump. Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games. Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table. The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.')
          +boxplot(1.68,1.88,0.01,1.68,1.78,1.82,1.87,1.87,lab=0.04,dec=2,xl='high jump',caps=True)
          +q('Explain why the boxplot has no whisker at its upper end. <i>(1 mark)</i>')+lines(3,'Q<sub>3</sub> is equal to the maximum value (1.87 m), so there is no distance for an upper whisker to cover.'),ht)
    +guess('50% (average mark)',mcq=False)+cite(f'{EDR} · 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e'))
P.append(box('Exit tasks',ex,'Show what you know',cls='split'))

# ---- Skills checklist + coursework
SC=['I can construct a boxplot from a five-number summary.','I can construct a boxplot with outliers from data using the CAS calculator.',
    'I can read values from a boxplot.','I can estimate percentages from a boxplot.','I can use boxplots to describe a distribution without outliers.',
    'I can use boxplots to describe a distribution with outliers.','I can use boxplots to answer statistical questions.']
P.append(box('Skills checklist','<div class="scg">'+''.join(f'<div class="sc"><div class="tick"></div><div><b>{i}. {s}</b></div></div>' for i,s in enumerate(SC,1))+'</div>','Tick when you can do it'))
P.append(box('Coursework · Cambridge exercise 1G','<div class="hwg">'
  '<div><div class="hwh">Exercise 1G</div><div class="hwq">Q1–2 · Q3–6 · Q7 <i>(CAS)</i> · Q8–10<br>Q11–13 · Q14–15 · Q16<br>Q17–20 <i>(Exam 1 style)</i></div><div class="tick"></div></div>'
  '<div><div class="hwh">Revision book</div><div class="hwq">1G section</div><div class="tick"></div></div></div>'
  '<div class="sig"><div class="stamp">Teacher stamp</div><div class="lines"><div>Teacher signature <i></i> Date <i class="d"></i></div><div>Parent signature <i></i> Date <i class="d"></i></div></div></div>','Tick when done'))

JS=''.join(f'<script>{open(f"{ROOT}/lessons/{n}").read()}</script>' for n in ('a4view.js','paged.polyfill.min.js'))  # inlined so the G: copy works on its own
def page(sol,screen=True):
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>1G guided worksheet{" · solutions" if sol else ""}</title><style>{CSS}</style>{JS if screen else ""}</head><body class="{"sol" if sol else ""}">'+'\n'.join(P)+'</body></html>'
for sol,fn in ((0,'S4-worksheet.html'),(1,'S4-worksheet-solutions.html')):
    open(f'{ROOT}/lessons/{fn}','w').write(page(sol))
    open(f'/tmp/{fn}','w').write(page(sol,False))   # plain copy that ws_pdf.py prints
print('ok')
