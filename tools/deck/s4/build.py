"""Build lessons/S4-slides.html (1G five-number summary, boxplots, outliers).
Template = lessons/S3-slides.html (its CSS, chart code and reveal engine) + s4 extra.css/extra.js.
Run from anywhere:  python3 tools/deck/s4/build.py"""
import re, json, os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=f'{ROOT}/lessons/S3-slides.html'
OUT=f'{ROOT}/lessons/S4-slides.html'
CAM='Cambridge General Mathematics Units 3&amp;4'
EDR='Edrolo General Mathematics Units 3&amp;4'

def J(o): return json.dumps(o).replace("'","&#39;")
def box(rid,cfg,style=''): return f'<div class="chart" id="{rid}" data-chart="box" data-cfg=\'{J(cfg)}\' style="{style}"></div>'
def hist(rid,cfg,style='',extra=''): return f'<div class="chart" id="{rid}" data-chart="hist" data-cfg=\'{J(cfg)}\' {extra} style="{style}"></div>'
def dot3(rid,cfg): return f'<div class="chart" id="{rid}" data-chart="dot3" data-cfg=\'{J(cfg)}\'></div>'
def vid(n): return f'<button class="vid" data-src="" data-label="Cambridge GO · Example {n} (1G Resources)">▶ Video</button>'
def stem(rid, rows, key, cap='', fs=26):
    i=0; tr=''
    for st,lv in rows:
        sp=''
        for l in lv: sp+=f'<span class="lf2" data-i="{i}">{l}</span>'; i+=1
        tr+=f'<tr><td class="st">{st}</td><td class="lv">{sp}</td></tr>'
    c=f'<div class="stemcap">{"<b>"+cap+"</b> &nbsp; " if cap else ""}{key}</div>'
    return f'<div>{c}<table class="stem3" id="{rid}" style="font-size:{fs}px">{tr}</table></div>'
def cards(items):
    h='<div class="stepsH">'
    for k,(t,b) in enumerate(items,1):
        h+=f'<div class="sc"><div class="n">{k}</div><div class="frag"><div class="st">{t}</div><div class="sb">{b}</div></div></div>'
    return h+'</div>'
BUILD=['box','med','wl','wu','out']

S=[]
# ================= 1 title
S.append('''<section class="slide s-title">
  <div class="kicker"><i></i>Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 4</div>
  <h1><span>Five numbers</span>, <br>one <span>picture</span></h1>
  <div class="sub">1G The five-number summary and the boxplot: outliers, reading boxplots and describing distributions</div>
  <div class="flow"><div style="border-color:#00838F">Do Now</div><div style="border-color:var(--apk)">APK</div><div style="border-color:var(--learn)">Learn</div><div style="border-color:var(--we)">Worked examples</div><div style="border-color:var(--yt)">You try</div><div style="border-color:var(--exit)">Exit tasks</div></div>
  <div class="foot"><span>12MAG · General Mathematics 3&amp;4</span><span>S4</span></div>
</section>''')
# ================= 2 today's lesson
LI=['To be able to construct the boxplot for displaying the distribution of a numerical data.',
    'To be able to define and identify outliers.',
    'To be able to construct both simple boxplots and boxplots with outliers.',
    'To be able to determine the features of a distribution from a boxplot.',
    'To be able to use a CAS calculator to construct a boxplot.']
S.append('''<section class="slide">
  <div class="pill">Today’s lesson</div>
  <h2 style="margin-bottom:14px">Today’s lesson</h2>
  <div class="lisc" style="grid-template-columns:1.15fr 1fr"><div><h3>Learning intentions</h3><ul>'''+''.join(f'<li style="font-size:22px;padding:6px 0 6px 32px">{x}</li>' for x in LI)+'''</ul></div>
    <div><h3>Lesson sequence</h3><ol class="seq">
      <li style="--c:#00838F">Do Now <small>· four current VCAA questions</small></li>
      <li style="--c:var(--apk)">APK <small>· Year 11 boxplots</small></li>
      <li>Five-number summary and the boxplot <small>→ WE 22</small></li>
      <li>Outliers and fences <small>· CAS</small></li>
      <li>Reading a boxplot <small>→ WE 23, 24</small></li>
      <li>Shape from a boxplot <small>→ WE 25, 26, 27</small></li>
      <li style="--c:var(--exit)">Exit tasks <small>· two VCAA questions</small></li>
      <li style="--c:var(--muted)">Check-in and coursework</li></ol></div>
  </div>
</section>''')
# ================= 3 success criteria
SC=['I can construct a boxplot from a five-number summary.','I can construct a boxplot with outliers from data using the CAS calculator.',
    'I can read values from a boxplot.','I can estimate percentages from a boxplot.',
    'I can use boxplots to describe a distribution without outliers.','I can use boxplots to describe a distribution with outliers.',
    'I can use boxplots to answer statistical questions.']
def scgrid(): return '<div class="lisc" style="grid-template-columns:1fr 1fr"><ul>'+''.join(f'<li>{x}</li>' for x in SC[:4])+'</ul><ul>'+''.join(f'<li>{x}</li>' for x in SC[4:])+'</ul></div>'
S.append(f'''<section class="slide">
  <div class="pill">Success criteria</div>
  <h2>By the end of this lesson you’ll be able to say…</h2>
  {scgrid()}
</section>''')
# ================= 4 Do Now 1: VCAA 2023 E1 Q1
runners=[134]*3+[135]*8+[136]*11+[137]*6+[138]*4+[139]*2+[140]*2+[141,142,143,146]
S.append(f'''<section class="slide mcslide dn" data-cfu="mc">
  <div class="pill">Do Now 1 of 4 · VCAA 2023 · Exam 1</div>
  <div class="stat">VCAA: <b>?%</b> of students answered correctly</div>
  <h2>Review of 1F</h2>
  <div class="row" style="gap:36px"><div class="q" style="flex:.8"><div class="stem">The dot plot below shows the times, in seconds, of 40 runners in the qualifying heats of their 800 m club championship.<br><br>The median time, in seconds, of these runners is</div>
  <div class="mc" data-dist="1,90,6,2,1"><div data-o="A"><b>A.</b>135.5</div><div data-o="B"><b>B.</b>136</div><div data-o="C"><b>C.</b>136.5</div><div data-o="D"><b>D.</b>137</div><div data-o="E"><b>E.</b>137.5</div></div></div>
  <div style="flex:1.2">{dot3('dn1d',{"min":134,"max":146,"vals":runners,"xl":"time (seconds)","W":900,"h":400,"r":12})}</div></div>
  <div class="mcsol"><div class="ansbox frag" data-key="B" data-stat="90" data-s="sol" data-dotmark="#dn1d|19,20"><div class="lab">Solution · B</div><p>n = 40, so the median is the average of the 20th and 21st times. Count up: 3 + 8 = 11 by 135 s, then 11 + 11 = 22 by 136 s. Both are <b>136</b>.</p></div><div class="frag" data-s="sol" style="flex:1;display:flex"><div class="dbox"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="C"><div class="lab2">Distractor · C</div><p>136.5 averages 136 and 137, as if the middle sat between two columns. Count the dots: the 20th and 21st are both in the 136 column.</p></div></div></div></div><span class="frag" data-pct="1"></span>
  <div class="src">VCAA 2023 General Mathematics Exam 1 Q1 (90% of students answered correctly)</div>
</section>''')
# ================= 5 Do Now 2: VCAA 2023 E1 Q6
S.append('''<section class="slide mcslide dn" data-cfu="mc">
  <div class="pill">Do Now 2 of 4 · VCAA 2023 · Exam 1</div>
  <div class="stat">VCAA: <b>?%</b> of students answered correctly</div>
  <h2>Review of 1E</h2>
  <div class="row" style="gap:36px"><div class="q" style="flex:1.1;font-size:22px"><div class="stem">The histogram below displays the distribution of prices, in dollars, of the cars for sale in a used-car yard.<br>The histogram has a logarithm (base 10) scale.<br>Six of the cars in the yard have the following prices: &nbsp;$2450 · $3175 · $4999 · $8925 · $10 250 · $105 600<br>How many of the six car prices listed above are in the modal class interval?</div>
  <div class="mc cols" data-dist="9,11,54,13,13"><div data-o="A"><b>A.</b>1</div><div data-o="B"><b>B.</b>2</div><div data-o="C"><b>C.</b>3</div><div data-o="D"><b>D.</b>4</div><div data-o="E"><b>E.</b>6</div></div></div>
  <div style="flex:.9">'''+hist('dn2h',{"start":3.0,"w":0.5,"v":[2,6,5,4,2,1,0],"xmax":6.5,"ymax":7,"ystep":1,"tick":0.5,"dec":1,"xl":"log10 (price)","yl":"frequency","h":380,"W":600,"fs":17,"col":"#a9a9a9"},extra='data-hidelab=\'["6.5","1","3","5","7"]\'')+'''</div></div>
  <div class="mcsol"><div class="ansbox frag" data-key="C" data-stat="54" data-s="sol" data-hlbar="#dn2h|1|#d98a1f"><div class="lab">Solution · C</div><p>Modal class: 3.5–4.0. Take log<sub>10</sub> of each price: 3.39, <b>3.50</b>, <b>3.70</b>, <b>3.95</b>, 4.01, 5.02. Three prices ($3175, $4999, $8925) are in it.</p></div><div class="frag" data-s="sol" style="flex:1;display:flex"><div class="dbox"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="D"><div class="lab2">Distractor · D</div><p>$10 250 looks close, but log<sub>10</sub>(10 250) = 4.01, just past 4.0, so it is in the next interval.</p></div></div></div></div><span class="frag" data-pct="1"></span>
  <div class="src">VCAA 2023 General Mathematics Exam 1 Q6 (54% of students answered correctly)</div>
</section>''')
# ================= 6–7 Do Now 3/4: VCAA 2025 E2 Q1a, Q1b
apt=['350 000','490 000','500 000','620 000','720 000','830 000','875 000','995 000','1 100 000','1 520 000']
hou=['800 000','840 000','920 000','920 000','1 010 000','1 263 000','1 398 000','1 460 000','1 540 000','1 540 000']
def t1(fs=17):
    tb=lambda rows:'<table class="t" style="font-size:%dpx"><tr><th>Price ($)</th><th>Type</th></tr>'%fs+''.join(f'<tr><td style="text-align:right">{p}</td><td>{t}</td></tr>' for p,t in rows)+'</table>'
    return ('<p style="font-size:17px;font-weight:700;margin:6px 0 2px">Table 1</p><div class="tbl1">'+tb([(p,'apartment') for p in apt])+tb([(p,'house') for p in hou])+'</div>'
            '<p class="muted" style="font-size:13px;margin-top:2px">Data: Adapted from &lt;www.kaggle.com/datasets/anthonypino/melbourne-housing-market&gt;</p>')
INTRO='Table 1, below, shows the prices in dollars, <em class="v">price</em>, for a sample of 20 homes sold in an inner Melbourne suburb during 2017.<br>The type of home sold is either an apartment or a house.'
S.append(f'''<section class="slide dn" data-cfu="qw">
  <div class="pill">Do Now 3 of 4 · VCAA 2025 · Exam 2</div>
  <div class="stat">VCAA: <b>?%</b> scored 1/1</div>
  <h2>Review of 1F</h2>
  <div class="row" style="gap:30px">
    <div class="q" style="flex:1.1;font-size:21px;padding:14px 22px">{INTRO}{t1()}</div>
    <div style="flex:.9"><div class="q" style="font-size:23px"><b>a.</b> Find the median, in dollars, of the variable <em class="v">price</em>. <span class="muted">(1 mark)</span></div>
      <div class="sol"><p class="frag">n = 20, so the median is the average of the 10th and 11th prices in order.</p>
        <p class="frag">In order: 350 000, 490 000, 500 000, 620 000, 720 000, 800 000, 830 000, 840 000, 875 000, <b>920 000</b>, <b>920 000</b>, 995 000, …</p>
        <div class="ansbox frag" data-stat="84"><div class="lab">Solution</div><p>median = (920 000 + 920 000) ÷ 2 = <b>$920 000</b></p></div></div></div></div>
  <div class="src">VCAA 2025 General Mathematics Exam 2 Q1a (84% of students scored 1/1)</div>
</section>''')
S.append(f'''<section class="slide dn" data-cfu="qw">
  <div class="pill">Do Now 4 of 4 · VCAA 2025 · Exam 2</div>
  <div class="stat">VCAA: <b>?%</b> scored 1/1</div>
  <h2>Review of 1A</h2>
  <div class="row" style="gap:30px">
    <div class="q" style="flex:1.1;font-size:21px;padding:14px 22px">{INTRO}{t1()}</div>
    <div style="flex:.9"><div class="q" style="font-size:23px"><b>b.</b> State whether the variable <em class="v">type</em> is numerical, nominal or ordinal. <span class="muted">(1 mark)</span></div>
      <div class="sol"><p class="frag">The values are apartment and house: names of groups, with no natural order.</p>
        <div class="ansbox frag" data-stat="77"><div class="lab">Solution</div><p><b>Nominal</b></p></div></div></div></div>
  <div class="src">VCAA 2025 General Mathematics Exam 2 Q1b (77% of students scored 1/1)</div>
</section>''')
# ================= 8 APK: party ages (Cambridge U1&2 2H #14, #15)
S.append(f'''<section class="slide apk" data-cfu="qw">
  <div class="pill">APK · from Year 11</div>
  <h2 style="margin-bottom:10px">Back to the party: boxplots</h2>
  <div class="row" style="gap:30px"><div class="q" style="flex:1;font-size:22px">The ages of a group of people at a party:
      <div class="data" style="font-size:21px">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>
      <ol class="sub"><li data-part="a"><b>a</b>Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).</li><li data-part="b"><b>b</b>Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).</li></ol></div>
    <div style="flex:1">
      <div class="sol" style="margin-top:0"><p class="frag" data-p="a">In order: 17 19 19 19 20 <b>20</b> 21 21 22 23 | 26 27 28 29 34 <b>34</b> 37 45 56 66</p>
        <p class="frag big" data-p="a" data-bx="#apkb|{','.join(BUILD)}">17, 20, 24.5, 34, 66</p></div>
      {box('apkb',{"min":15,"max":70,"step":5,"lw":17,"q1":20,"m":24.5,"q3":34,"uw":66,"xl":"age (years)","hide":BUILD,"W":800,"fs":20,"top":40})}
      <div class="sol"><p class="frag" data-p="b">IQR = 34 − 20 = 14 &nbsp;·&nbsp; 1.5 × 14 = 21</p>
        <p class="frag" data-p="b">lower fence = 20 − 21 = <b>−1</b> &nbsp;·&nbsp; upper fence = 34 + 21 = <b>55</b></p>
        <p class="frag big" data-p="b">Outliers: <span class="reveal">56 and 66</span> (above 55)</p></div></div></div>
  <div class="src">Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2H #14, #15 (teacher solutions)</div></section>''')
# ================= 9 APK: Edrolo U1&2 1F Q16 (adapted from VCAA 2017 E1 Q2)
S.append(f'''<section class="slide mcslide apk" data-cfu="mc cold">
  <div class="pill">APK · Edrolo U1&amp;2 1F Q16</div>
  <div class="stat">VCAA: <b>?%</b> of students answered correctly</div>
  <h2>A real VCAA question you can already do</h2>
  <div class="row" style="gap:30px"><div class="q" style="flex:1"><div class="stem">The boxplot shows the distribution of the <em class="v">reaction time</em> (milliseconds), of 256 firefighters.<br><br>The five-number summary for the <em class="v">reaction time</em> of these 256 firefighters is closest to</div>
    <div class="mc"><div data-o="A"><b>A.</b>70, 130, 140, 152, 179</div><div data-o="B"><b>B.</b>70, 130, 140, 152, 255</div><div data-o="C"><b>C.</b>122, 130, 140, 152, 179</div><div data-o="D"><b>D.</b>122, 130, 140, 152, 245</div><div data-o="E"><b>E.</b>122, 130, 140, 152, 265</div></div></div>
    <div style="flex:1.1;align-self:center">{box('apk2',{"min":0,"max":260,"step":10,"lab":50,"lw":122,"q1":130,"m":140,"q3":152,"uw":179,"out":[70,90,255],"caps":True,"xl":"reaction time (milliseconds)","W":820,"fs":19,"top":20,"bh":46})}</div></div>
  <div class="mcsol"><div class="ansbox frag" data-key="B" data-stat="58" data-s="sol" data-bxo="#apk2|#d98a1f"><div class="lab">Solution · B</div><p>The outliers are still data values: minimum = <b>70</b> and maximum = <b>255</b> (the dots). Box: 130, 140, 152.</p></div><div class="frag" data-s="sol" style="flex:1;display:flex"><div class="dbox"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="C"><div class="lab2">Distractor · C</div><p>On the original VCAA question, 38% chose this option: they ignored the outlier points and used the whisker ends as the minimum and maximum.</p></div></div></div></div>
  <div class="src">Edrolo General Mathematics Units 1&amp;2 · 1F Q16 · Adapted from VCAA 2017 Exam 1 Data analysis Q2 (58%; distractor %: Edrolo U3&amp;4 1E)</div>
</section>''')
# ================= 10 Learn: five-number summary and the boxplot
S.append(f'''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1G</div>
  <h2 style="margin-bottom:10px">Five numbers, one picture</h2>
  <div class="key frag" style="padding:12px 26px"><h4>Five-number summary</h4><p style="font-size:24px">minimum, Q<sub>1</sub>, median, Q<sub>3</sub>, maximum: the centre, the spread of the middle half, and both ends.</p></div>
  <div style="margin-top:6px">{box('lb1',{"min":0,"max":100,"step":5,"lab":10,"lw":12,"q1":35,"m":50,"q3":62,"uw":95,"hide":BUILD,"W":1400,"fs":20,"bh":70,"top":70,
     "marks":[{"p":"k0","x":12,"t":"minimum","col":"#8a4d00"},{"p":"k1","x":35,"t":"Q₁","col":"#6a3fc7"},{"p":"k2","x":50,"t":"median","col":"#d2475b"},{"p":"k3","x":62,"t":"Q₃","col":"#6a3fc7"},{"p":"k4","x":95,"t":"maximum","col":"#8a4d00"}],
     "bands":[{"p":"p1","a":12,"b":35,"t":"25%"},{"p":"p2","a":35,"b":50,"t":"25%"},{"p":"p3","a":50,"b":62,"t":"25%"},{"p":"p4","a":62,"b":95,"t":"25%"}]})}</div>
  <span class="frag" data-bx="#lb1|k0,k1,k2,k3,k4"></span><span class="frag" data-bx="#lb1|box"></span><span class="frag" data-bx="#lb1|med"></span><span class="frag" data-bx="#lb1|wl,wu"></span><span class="frag" data-bx="#lb1|p1,p2,p3,p4"></span>
  <div class="tip frag" style="font-size:22px">The <b>box</b> holds the middle 50% (Q<sub>1</sub> to Q<sub>3</sub>); the <b>whiskers</b> run out to the smallest and largest values. Each of the four sections holds about 25% of the data, however long it is.</div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1G pp. 61–62 · Boxplot: teacher illustration</div></section>''')
# ================= 11 WE22
life=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 22 · 1G</div>{vid(22)}
  <div class="wename">Constructing a boxplot from a five-number summary</div>
  <div class="row" style="margin-top:12px;gap:34px">
    <div class="q" style="flex:1;font-size:20px;padding:12px 20px">The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:
      <div class="row" style="gap:24px;margin-top:8px;align-items:flex-start">{stem('w22s',life,'Key: 5|2 = 52 years','',20)}
      <table class="t" style="font-size:18px;white-space:nowrap"><tr><td class="l">minimum</td><td>52</td></tr><tr><td class="l">first quartile (Q<sub>1</sub>)</td><td>66</td></tr><tr><td class="l">median (M)</td><td>73</td></tr><tr><td class="l">third quartile (Q<sub>3</sub>)</td><td>75</td></tr><tr><td class="l">maximum</td><td>77</td></tr></table></div>
      <p style="margin-top:4px">Use the five-number summary to construct a boxplot.</p></div>
    <div style="flex:1;align-self:center">{box('w22b',{"min":50,"max":80,"step":1,"lab":5,"lw":52,"q1":66,"m":73,"q3":75,"uw":77,"xl":"Life expectancy (years)","hide":BUILD,"W":900,"fs":20})}</div></div>
  <div class="stepsH"><div class="sc"><div class="n">1</div><div class="frag"><div class="st">Number line</div><div class="sb">Labelled and scaled to cover the full range of values.</div></div></div>
    <div class="sc"><div class="n">2</div><div class="frag" data-bx="#w22b|box"><div class="st">Box</div><div class="sb">From Q<sub>1</sub> = 66 to Q<sub>3</sub> = 75.</div></div></div>
    <div class="sc"><div class="n">3</div><div class="frag" data-bx="#w22b|med"><div class="st">Median</div><div class="sb">A vertical line at M = 73.</div></div></div>
    <div class="sc"><div class="n">4</div><div class="frag" data-bx="#w22b|wl,wu"><div class="st">Whiskers</div><div class="sb">Out to the minimum (52) and maximum (77).</div></div></div></div>
  <div class="src">{CAM} · Example 22</div></section>''')
# ================= 12 YT Edrolo 1E WE4
w4=[('0',[1,2,3,5,5,9]),('1',[0,0,1,5,8,9]),('2',[1,2,3,3,5]),('3',[3,7,9])]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1G</div>
  <div class="wename">Constructing a boxplot from a five-number summary</div>
  <div class="row" style="margin-top:12px;gap:34px">
    <div class="q" style="flex:.75">The five-number summary for the following stem plot is:<div class="data" style="font-size:24px">1, 7, 16.5, 23, 39</div>
      {stem('y4s',w4,'Key: 1 | 2 = 12','',24)}<p style="margin-top:8px">Construct a boxplot using the data.</p></div>
    <div style="flex:1.25"><div class="sol" style="margin-top:0">
      <p class="frag">Check for outliers: IQR = 23 − 7 = 16</p>
      <p class="frag">lower fence = 7 − (1.5 × 16) = −17 · upper fence = 23 + (1.5 × 16) = 47 → <b>no outliers</b></p>
      <p class="frag" data-bx="#y4b|box">Box from Q<sub>1</sub> = 7 to Q<sub>3</sub> = 23</p>
      <p class="frag" data-bx="#y4b|med">Median line at 16.5</p>
      <p class="frag" data-bx="#y4b|wl,wu">Whiskers to the minimum (1) and maximum (39)</p></div>
      {box('y4b',{"min":0,"max":40,"step":1,"lab":5,"lw":1,"q1":7,"m":16.5,"q3":23,"uw":39,"hide":BUILD,"W":900,"fs":20,"top":30})}</div></div>
  <div class="src">{EDR} · 1E Worked example 4</div></section>''')
# ================= 13 Learn: outliers and fences (CAS 4 data)
marks19=[28,21,21,3,22,31,35,26,27,33,43,31,30,34,48,36,35,23,24]
S.append(f'''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1G</div>
  <h2 style="margin-bottom:6px">Outliers: the 1.5 × IQR fences</h2>
  <div class="row" style="gap:26px;align-items:flex-start">
    <div class="key frag" style="flex:1;padding:12px 22px"><h4>Outlier</h4><p style="font-size:21px">A value more than 1.5 IQRs below Q<sub>1</sub> or above Q<sub>3</sub>.</p>
      <p style="font-size:21px;margin-top:6px">lower fence = Q<sub>1</sub> − 1.5 × IQR<br>upper fence = Q<sub>3</sub> + 1.5 × IQR</p>
      <p style="font-size:21px;margin-top:6px">Outliers are drawn as <b>dots</b>; the whiskers stop at the last value <b>inside</b> the fences.</p></div>
    <div style="flex:1.7"><p style="font-size:20px;margin-bottom:2px">19 marks: <span class="data" style="font-size:19px">28 21 21 3 22 31 35 26 27 33 43 31 30 34 48 36 35 23 24</span></p>
      {dot3('lo3',{"min":0,"max":55,"vals":marks19,"W":1000,"h":150,"r":8,"step":5})}
      {box('lo3b',{"min":0,"max":55,"step":1,"lab":5,"lw":21,"q1":23,"m":30,"q3":35,"uw":48,"out":[3],"hide":["wl","wu","out"],"W":1000,"fs":19,"top":60,"bh":50,
         "bands":[{"p":"iqr","a":23,"b":35,"t":"IQR = 35 − 23 = 12","col":"rgba(106,63,199,.15)","sc":"#6a3fc7","tc":"#5b33b0"}],
         "fences":[{"p":"fl","x":5,"t":"lower fence 23 − 18 = 5"},{"p":"fu","x":53,"t":"upper fence 35 + 18 = 53","left":True}]})}</div></div>
  <span class="frag" data-bx="#lo3b|iqr"></span><span class="frag" data-bx="#lo3b|fl,fu"></span><span class="frag" data-bx="#lo3b|out" data-dotmark="#lo3|0"></span><span class="frag" data-bx="#lo3b|wl,wu"></span>
  <div class="tip frag" style="font-size:21px">3 is below the lower fence (5), so it is an <b>outlier</b>. The lower whisker stops at <b>21</b>, the smallest value that is not an outlier. Nothing is above 53, so the upper whisker runs to 48.</div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1G pp. 63–64 · Data: CAS 4 (p. 64)</div></section>''')
# ================= 14 CAS: boxplot with outliers
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">CAS · 1G</div>
  <h2 style="margin:10px 0 8px;font-size:40px">Boxplot with outliers on CAS</h2>
  <p style="font-size:22px;margin-bottom:8px">Display the following set of 19 marks in the form of a boxplot with outliers. &nbsp;<span class="data" style="font-size:20px">28 21 21 3 22 31 35 26 27 33 43 31 30 34 48 36 35 23 24</span></p>
  <div class="row" style="gap:24px"><div class="cas" style="flex:1.5">
    <div class="key frag"><h4>TI-Nspire</h4><ol><li>New document → <b>Lists &amp; Spreadsheet</b>. Name a list <b>marks</b>; enter the data.</li><li>Add <b>Data &amp; Statistics</b>.</li><li>Click to add variable on the x-axis → <b>marks</b> (a dot plot appears).</li><li>Menu › Plot Type › <b>Box Plot</b>.</li><li>Read values: hover, or Menu › Analyze › <b>Graph Trace</b>.</li></ol></div>
    <div class="key frag"><h4>ClassPad</h4><ol><li><b>Statistics</b> app. Name a list <b>marks</b>; enter the data.</li><li>Tap the SetGraph icon. Draw: On · Type: <b>MedBox</b> · XList: main\\marks · Freq: 1.</li><li>Tick <b>Show Outliers</b>. Set, then plot.</li><li>Tap <b>Trace</b>; move with the cursor arrows to read the values.</li></ol></div></div>
    <div class="key frag" style="flex:.6;align-self:center;text-align:center"><h4>Read off</h4><p style="font-size:24px;line-height:1.5">min = 3 <span class="muted">(outlier)</span><br>Q<sub>1</sub> = 23 · M = 30<br>Q<sub>3</sub> = 35 · max = 48</p></div></div>
  <div class="tip frag" style="font-size:20px"><b>Check the outlier setting.</b> A whisker running all the way to 3 means outliers are switched off (ClassPad: tick Show Outliers).</div>
  <div class="src">Reference: Cambridge General Mathematics Units 3&amp;4, 1G pp. 64–66 (CAS 4)</div></section>''')
# ================= 15 YT CAS Edrolo 1E WE5
w5=[2,4,4,5,5,5,7,6,5,4,6,5,6,7,8,12,3,5]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · CAS</div>
  <div class="wename">Constructing a boxplot with outliers using the CAS calculator</div>
  <div class="q" style="margin-top:14px">Construct a boxplot for the following data set.<div class="data">2 4 4 5 5 5 7 6 5 4 6 5 6 7 8 12 3 5</div></div>
  <div class="row" style="gap:30px;margin-top:6px"><div class="sol" style="flex:1;margin-top:0">
    <p class="frag">Enter the data in a list; plot a boxplot (ClassPad: MedBox, Show Outliers ticked).</p>
    <p class="frag" data-bx="#y5b|box,med">Q<sub>1</sub> = 4, median = 5, Q<sub>3</sub> = 6</p>
    <p class="frag" data-bx="#y5b|out">IQR = 2, upper fence = 6 + 3 = 9: <b>12 is an outlier</b></p>
    <p class="frag" data-bx="#y5b|wl,wu">Whiskers from 2 to 8</p></div>
    <div style="flex:1.2">{box('y5b',{"min":1,"max":12,"step":1,"lw":2,"q1":4,"m":5,"q3":6,"uw":8,"out":[12],"hide":BUILD,"xl":"list","W":900,"fs":20,"top":30})}</div></div>
  <div class="src">{EDR} · 1E Worked example 5</div></section>''')
# ================= 16 WE23
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 23 · 1G</div>{vid(23)}
  <div class="wename">Reading values from a boxplot</div>
  <div class="row" style="margin-top:8px;gap:30px">
    <div class="q" style="flex:.85;font-size:21px">For the boxplot shown, write down the values of:
      <ol class="sub" style="font-size:20px"><li data-part="a"><b>a</b>the median</li><li data-part="b"><b>b</b>the quartiles Q<sub>1</sub> and Q<sub>3</sub></li><li data-part="c"><b>c</b>the interquartile range (IQR)</li><li data-part="d"><b>d</b>the minimum and maximum values</li><li data-part="e"><b>e</b>the values of any possible outliers</li><li data-part="f"><b>f</b>the smallest value in the upper end of the data set that will be classified as an outlier</li><li data-part="g"><b>g</b>the largest value in the lower end of the data set that will be classified as an outlier.</li></ol></div>
    <div style="flex:1.15">{box('w23b',{"min":0,"max":100,"step":2,"lab":10,"lw":10,"q1":30,"m":36,"q3":44,"uw":60,"out":[4,70,84,92],"W":900,"fs":19,"top":112,
       "marks":[{"p":"mm","x":36,"t":"M = 36","col":"#d2475b","lv":1},{"p":"mq","x":30,"t":"Q₁ = 30","anchor":"end","dx":-4},{"p":"mq3","x":44,"t":"Q₃ = 44","anchor":"start","dx":4}],
       "fences":[{"p":"fu","x":65,"t":"upper fence 65","lv":2},{"p":"fl","x":9,"t":"lower fence 9","lv":2}]})}
      <div class="sol" style="font-size:21px">
        <p class="frag" data-p="a" data-bx="#w23b|mm"><b>a</b> M = <span class="reveal">36</span></p>
        <p class="frag" data-p="b" data-bx="#w23b|mq,mq3"><b>b</b> Q<sub>1</sub> = <span class="reveal">30</span>, Q<sub>3</sub> = <span class="reveal">44</span></p>
        <p class="frag" data-p="c"><b>c</b> IQR = Q<sub>3</sub> − Q<sub>1</sub> = 44 − 30 = <span class="reveal">14</span></p>
        <p class="frag" data-p="d"><b>d</b> Min = <span class="reveal">4</span>, Max = <span class="reveal">92</span></p>
        <p class="frag" data-p="e" data-bxo="#w23b|#d98a1f"><b>e</b> <span class="reveal">4, 70, 84 and 92</span> are possible outliers</p>
        <p class="frag" data-p="f" data-bx="#w23b|fu"><b>f</b> Upper fence = Q<sub>3</sub> + 1.5 × IQR = 44 + 1.5 × 14 = <span class="reveal">65</span>: any value above 65 is an outlier.</p>
        <p class="frag" data-p="g" data-bx="#w23b|fl"><b>g</b> Lower fence = Q<sub>1</sub> − 1.5 × IQR = 30 − 1.5 × 14 = <span class="reveal">9</span>: any value below 9 is an outlier.</p></div></div></div>
  <div class="src">{CAM} · Example 23</div></section>''')
# ================= 17 YT Edrolo 1E WE6
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1G</div>
  <div class="wename">Reading values from a boxplot</div>
  <div class="row" style="margin-top:8px;gap:30px">
    <div class="q" style="flex:1;font-size:21px">The <em class="v">number of runs scored</em> by the leading batsman at a local cricket club is represented by the following boxplot.<br>It is known that data was collected from 20 separate innings.
      <ol class="sub" style="font-size:20px"><li data-part="a"><b>a.</b>Determine the five-number summary for the data and identify any outliers.</li><li data-part="b"><b>b.</b>Between which two values does the middle 50% of data lie?</li><li data-part="c"><b>c.</b>In approximately what percentage of innings did they score more than 80 runs?</li><li data-part="d"><b>d.</b>In approximately how many innings did they score at least 50 runs, but fall short of 100?</li></ol></div>
    <div style="flex:1">{box('y6b',{"min":0,"max":100,"step":5,"lab":10,"lw":30,"q1":50,"m":70,"q3":80,"uw":90,"caps":True,"xl":"number of runs scored","W":900,"fs":19,"top":56,
       "bands":[{"p":"b50","a":50,"b":80,"t":"middle 50%"},{"p":"b25","a":80,"b":90,"t":"25%","col":"rgba(47,111,223,.15)","sc":"#2f6fdf","tc":"#1f4fb0"},{"p":"b75","a":50,"b":90,"t":"75%","col":"rgba(31,158,116,.15)","sc":"#1f9e74","tc":"#137a59"}]})}
      <div class="sol" style="font-size:21px">
        <p class="frag" data-p="a"><b>a.</b> No dots, so no outliers. <span class="reveal">30, 50, 70, 80, 90</span>; there are no outliers.</p>
        <p class="frag" data-p="b" data-bx="#y6b|=b50"><b>b.</b> Between Q<sub>1</sub> and Q<sub>3</sub>: <span class="reveal">50 and 80 runs</span></p>
        <p class="frag" data-p="c" data-bx="#y6b|=b25"><b>c.</b> Q<sub>3</sub> = 80, and 25% of data is greater than Q<sub>3</sub>: <span class="reveal">25%</span></p>
        <p class="frag" data-p="d" data-bx="#y6b|=b75"><b>d.</b> 75% lies between Q<sub>1</sub> (50) and the maximum (90); 0.75 × 20 = <span class="reveal">15 innings</span></p></div></div></div>
  <div class="src">{EDR} · 1E Worked example 6</div></section>''')
# ================= 18 WE24
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 24 · 1G</div>{vid(24)}
  <div class="wename">Estimating percentages from a boxplot</div>
  <div class="row" style="margin-top:8px;gap:30px">
    <div class="q" style="flex:.7;font-size:22px">For the boxplot shown, estimate the percentage of values:
      <ol class="sub" style="font-size:21px"><li data-part="a"><b>a</b>less than 54</li><li data-part="b"><b>b</b>less than 55</li><li data-part="c"><b>c</b>less than 59</li><li data-part="d"><b>d</b>greater than 59</li><li data-part="e"><b>e</b>between 54 and 59</li><li data-part="f"><b>f</b>between 54 and 86.</li></ol></div>
    <div style="flex:1.3">{box('w24b',{"min":45,"max":85,"step":1,"lab":5,"lw":50,"q1":54,"m":55,"q3":59,"uw":65,"out":[70,81],"W":900,"fs":19,"top":56,"bh":50,
       "bands":[{"p":"ba","a":50,"b":54,"t":"25%"},{"p":"bb","a":50,"b":55,"t":"50%"},{"p":"bc","a":50,"b":59,"t":"75%"},{"p":"bd","a":59,"b":81,"t":"25%"},{"p":"be","a":54,"b":59,"t":"50%"},{"p":"bf","a":54,"b":81,"t":"75%"}]})}
      <div class="sol" style="font-size:21px">
        <p class="frag" data-p="a" data-bx="#w24b|=ba"><b>a</b> 54 is Q<sub>1</sub>; 25% of values are less than Q<sub>1</sub>: <span class="reveal">25%</span></p>
        <p class="frag" data-p="b" data-bx="#w24b|=bb"><b>b</b> 55 is the median; 50% of values are less than it: <span class="reveal">50%</span></p>
        <p class="frag" data-p="c" data-bx="#w24b|=bc"><b>c</b> 59 is Q<sub>3</sub>; 75% of values are less than Q<sub>3</sub>: <span class="reveal">75%</span></p>
        <p class="frag" data-p="d" data-bx="#w24b|=bd"><b>d</b> 75% are less than 59, so 25% are greater: <span class="reveal">25%</span></p>
        <p class="frag" data-p="e" data-bx="#w24b|=be"><b>e</b> 75% − 25%: <span class="reveal">50%</span></p>
        <p class="frag" data-p="f" data-bx="#w24b|=bf"><b>f</b> 100% are less than 86 and 25% are less than 54: <span class="reveal">75%</span></p></div></div></div>
  <div class="src">{CAM} · Example 24 (boxplot as drawn in the textbook: top dot at about 81)</div></section>''')
# ================= 19 Learn: shape from a boxplot + describing
S.append(f'''<section class="slide" data-cfu="tps">
  <div class="pill">Learn · 1G</div>
  <h2 style="margin-bottom:8px">Reading shape from a boxplot</h2>
  <div class="mini4">
    <div class="key frag"><h4>Symmetric</h4>{box('sh1',{"min":0,"max":20,"step":1,"lab":100,"lw":2,"q1":7,"m":10,"q3":13,"uw":18,"W":620,"top":8,"bh":40,"fs":14})}<p>Median near the middle of the box; whiskers about equal.</p></div>
    <div class="key frag"><h4>Positively skewed</h4>{box('sh2',{"min":0,"max":20,"step":1,"lab":100,"lw":1,"q1":3,"m":4.5,"q3":8,"uw":19,"W":620,"top":8,"bh":40,"fs":14})}<p>Median to the <b>left</b> of the box; short left whisker, long right whisker (tail to the right).</p></div>
    <div class="key frag"><h4>Negatively skewed</h4>{box('sh3',{"min":0,"max":20,"step":1,"lab":100,"lw":1,"q1":12,"m":15.5,"q3":17,"uw":19,"W":620,"top":8,"bh":40,"fs":14})}<p>Median to the <b>right</b> of the box; long left whisker (tail to the left).</p></div>
    <div class="key frag"><h4>With outliers</h4>{box('sh4',{"min":0,"max":20,"step":1,"lab":100,"lw":8,"q1":10,"m":11,"q3":12,"uw":14,"out":[2,19],"W":620,"top":8,"bh":40,"fs":14})}<p>Dots separated from the box and whiskers by a gap.</p></div></div>
  <div class="scos frag"><div><b>Shape</b>symmetric or skewed (+/−)</div><div><b>Centre</b>the median</div><div><b>Spread</b>IQR (and range)</div><div><b>Outliers</b>name their values</div></div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1G pp. 68–69 · Sketches: teacher illustration</div></section>''')
# ================= 20 WE25
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 25 · 1G</div>{vid(25)}
  <div class="wename">Using a boxplot to describe the features of distribution without outliers</div>
  <div class="q" style="margin-top:12px">Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.</div>
  {box('w25b',{"min":0,"max":50,"step":1,"lab":5,"lw":0,"q1":5,"m":10,"q3":21,"uw":45,"W":1400,"fs":20,"top":60,"col":"#fde7a6",
     "marks":[{"p":"mm","x":10,"t":"M = 10","col":"#d2475b"},{"p":"mq1","x":5,"t":"Q₁ = 5","anchor":"end","dx":-6},{"p":"mq3","x":21,"t":"Q₃ = 21"}]})}
  <div class="scos" style="margin-top:4px"><div class="frag"><b>Shape</b>median to the left of the box, long right whisker: positively skewed, no outliers</div><div class="frag" data-bx="#w25b|mm"><b>Centre</b>median = 10</div><div class="frag" data-bx="#w25b|mq1,mq3"><b>Spread</b>IQR = 21 − 5 = 16; range = 45 − 0 = 45</div><div class="frag"><b>Write it</b>in one or two sentences</div></div>
  <div class="ansbox frag" style="margin-top:12px"><div class="lab">Solution</div><p>The distribution is positively skewed with no outliers. The distribution is centred at 10, the median value. The spread of the distribution, as measured by the IQR, is 16 and, as measured by the range, 45.</p></div>
  <div class="src">{CAM} · Example 25</div></section>''')
# ================= 21 YT Edrolo 1F WE5
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1G</div>
  <div class="wename">Using a boxplot to describe the features of distribution without outliers</div>
  <div class="row" style="margin-top:14px;gap:34px">
    <div class="q" style="flex:.8">Consider the boxplot.<br>Describe the distribution in terms of shape, centre, spread and outliers.</div>
    <div style="flex:1.2">{box('y25b',{"min":12,"max":20,"step":0.5,"lab":2,"lw":12,"q1":15,"m":18,"q3":19,"uw":20,"caps":True,"W":900,"fs":20,"top":30,"col":"#ddd3f3"})}</div></div>
  <div class="sol">
    <p class="frag">Shape: the median is towards the right of the box and the tail trails off in the negative direction: <b>negatively skewed</b>.</p>
    <p class="frag">Centre: median = 18 · Spread: range = 20 − 12 = 8 · Outliers: none</p>
    <p class="frag big">The boxplot is negatively skewed with no outliers, a median of 18 and a range of 8.</p></div>
  <div class="src">{EDR} · 1F Worked example 5</div></section>''')
# ================= 22 WE26
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 26 · 1G</div>{vid(26)}
  <div class="wename">Using a boxplot to describe the features of a distribution with outliers</div>
  <div class="q" style="margin-top:12px">Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.</div>
  {box('w26b',{"min":0,"max":50,"step":1,"lab":5,"lw":34,"q1":38.75,"m":41,"q3":44.25,"uw":47,"out":[10,15,20,25],"W":1400,"fs":20,"top":92,"col":"#e9c6ea",
     "marks":[{"p":"mm","x":41,"t":"M = 41","col":"#d2475b","lv":1}]})}
  <div class="scos" style="margin-top:4px"><div class="frag"><b>Shape</b>box and whiskers symmetric, but with outliers</div><div class="frag" data-bxo="#w26b|#d98a1f"><b>Outliers</b>10, 15, 20 and 25</div><div class="frag" data-bx="#w26b|mm"><b>Centre</b>median = 41</div><div class="frag"><b>Spread</b>IQR = 5.5; range = 47 − 10 = 37</div></div>
  <div class="ansbox frag" style="margin-top:12px"><div class="lab">Solution</div><p>The distribution is symmetric but with outliers. The distribution is centred at 41, the median value. The spread of the distribution, as measured by the IQR, is 5.5 and, as measured by the range, 37. There are four outliers: 10, 15, 20 and 25.</p></div>
  <div class="src">{CAM} · Example 26 (no matching Edrolo worked example, so no You try)</div></section>''')
# ================= 23 WE27
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 27 · 1G</div>{vid(27)}
  <div class="wename">Using a boxplot to answer statistical questions</div>
  <div class="q" style="margin-top:12px">The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.</div>
  {box('w27b',{"min":25,"max":43,"step":1,"lw":35,"q1":38,"m":39,"q3":40,"uw":42,"out":list(range(25,35)),"xl":"Gestation period (weeks)","W":1400,"fs":20,"top":30,"col":"#bcd6f2"})}
  <div class="scos" style="margin-top:4px"><div class="frag"><b>Shape</b>long tail to the left: negatively skewed, several outliers</div><div class="frag"><b>Centre</b>median = 39 weeks</div><div class="frag"><b>Spread</b>range = 42 − 25 = 17 weeks; IQR = 40 − 38 = 2 weeks</div><div class="frag" data-bxo="#w27b|#d98a1f"><b>Outliers</b>25, 26, …, 34 weeks</div></div>
  <div class="ansbox frag" style="margin-top:12px;font-size:21px"><div class="lab">Solution</div><p>The distribution of gestational period is negatively skewed with several outliers. The distribution is centred at 39 weeks, the median value. The range of the distribution is 17 weeks, but the interquartile range is only 2 weeks. Any gestational period less than 35 weeks or less is considered unusual, with outliers at 25, 26, 27, 28, 29, 30, 31, 32, 33 and 34 weeks.</p></div>
  <div class="src">{CAM} · Example 27 (no matching Edrolo worked example, so no You try)</div></section>''')
# ================= 24 Exit 1: Edrolo 1E Q19 (VCAA 2020 E2 Q2c)
neck={31:1,32:1,33:3,34:11,35:19,36:32,37:34,38:48,39:39,40:18,41:28,42:12,43:3,44:1}
nv=[k for k,f in neck.items() for _ in range(f)]
S.append(f'''<section class="slide ex" data-cfu="qw">
  <div class="pill">Exit task 1 of 2 · Edrolo 1E Q19 · VCAA 2020 Exam 2 Q2c</div>
  <div class="stat">VCAA: average <b>?%</b> of the marks</div>
  <div class="row" style="margin-top:12px;gap:28px">
    <div style="flex:1.05"><div class="q" style="font-size:21px;padding:14px 22px">The <em class="v">neck size</em>, in centimetres, of 250 men was recorded and displayed in the following dot plot.<br>The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.
      <table class="t" style="font-size:19px;margin:8px 0;width:100%"><tr><th>minimum</th><th>first quartile (Q<sub>1</sub>)</th><th>median</th><th>third quartile (Q<sub>3</sub>)</th><th>maximum</th></tr><tr><td>31</td><td>36</td><td>38</td><td>39</td><td>44</td></tr></table>
      Use the five-number summary to construct a boxplot, showing any outliers if appropriate. <span class="muted">(2 marks)</span></div>
      <div class="sol" style="font-size:20px"><p class="frag" data-bx="#ex1b|box,med">IQR = 39 − 36 = 3 · 1.5 × 3 = 4.5</p><p class="frag" data-bx="#ex1b|out">lower fence = 36 − 4.5 = 31.5 · upper fence = 39 + 4.5 = 43.5 → <b>31 and 44 are outliers</b></p><p class="frag" data-bx="#ex1b|wl,wu">Whiskers end at the last values inside the fences: <b>32</b> and <b>43</b> (read from the dot plot).</p></div></div>
    <div style="flex:.95">{dot3('ex1d',{"min":30,"max":45,"vals":nv,"xl":"neck size (cm)","W":900,"h":600,"r":4.2,"fs":20})}
      {box('ex1b',{"min":30,"max":45,"step":1,"lw":32,"q1":36,"m":38,"q3":39,"uw":43,"out":[31,44],"hide":BUILD,"W":900,"fs":20,"top":10,"bh":44})}</div></div>
  <span class="frag" data-stat="55"></span>
  <div class="src">{EDR} · 1E Q19 · VCAA 2020 Exam 2 Data analysis Q2c (average mark 1.1 out of 2, 55%)</div>
</section>''')
# ================= 25 Exit 2: Edrolo 1E Q20 (VCAA 2021 E2 Q1e)
hep=[(1,'1.76','15.34','41.22'),(2,'1.79','16.96','42.41'),(3,'1.83','13.87','46.53'),(4,'1.82','14.23','40.53'),(5,'1.87','13.78','40.62'),(6,'1.73','14.50','45.62'),(7,'1.68','15.08','42.33'),(8,'1.82','13.13','40.88'),(9,'1.83','14.22','39.22'),(10,'1.87','13.62','42.51'),(11,'1.87','12.01','42.75'),(12,'1.80','12.88','38.12'),(13,'1.83','12.68','42.65'),(14,'1.87','12.45','41.32'),(15,'1.78','11.31','42.88')]
ht=''.join(f'<tr><td>{a}</td><td><span class="{"hj87" if b=="1.87" else ""}">{b}</span></td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in hep)
S.append(f'''<section class="slide ex" data-cfu="qw">
  <div class="pill">Exit task 2 of 2 · Edrolo 1E Q20 · VCAA 2021 Exam 2 Q1e</div>
  <div class="stat">VCAA: <b>?%</b> scored 1/1</div>
  <div class="row" style="margin-top:12px;gap:28px">
    <div style="flex:1.3"><div class="q" style="font-size:20px;padding:14px 22px">In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.<br>The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.
      {box('ex2b',{"min":1.68,"max":1.88,"step":0.01,"lab":0.04,"dec":2,"lw":1.68,"q1":1.78,"m":1.82,"q3":1.87,"uw":1.87,"caps":True,"xl":"high jump","W":800,"fs":18,"top":14,"bh":44})}
      Explain why the boxplot has no whisker at its upper end. <span class="muted">(1 mark)</span></div>
      <div class="sol" style="font-size:21px"><p class="frag">Q<sub>3</sub> = 1.87 m and the maximum = 1.87 m: four athletes jumped 1.87 m, the highest height.</p>
        <div class="ansbox frag" data-stat="50"><div class="lab">Solution</div><p>The third quartile (Q<sub>3</sub>) is equal to the maximum value (1.87 m), so there is no distance for an upper whisker to cover.</p></div></div></div>
    <div style="flex:.7"><table class="t" style="font-size:16px;width:100%"><tr><th>athlete number</th><th>high jump (metres)</th><th>shot-put (metres)</th><th>javelin (metres)</th></tr>{ht}</table></div></div>
  <div class="src">{EDR} · 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e (average mark 0.5 out of 1, 50%)</div>
</section>''')
# ================= 26 check-in / 27 coursework
S.append(f'''<section class="slide" data-cfu="tf">
  <div class="pill">Check-in</div>
  <h2>How did you go?</h2>
  {scgrid()}
  <p class="muted" style="font-size:24px;margin-top:22px">Thumbs up, sideways or down for each one, then rate it on your worksheet: ✓ got it · ~ nearly · ✗ not yet</p>
</section>''')
S.append('''<section class="slide">
  <div class="pill" style="background:#4b5563">Coursework</div>
  <h2 style="margin-bottom:16px">Coursework</h2>
  <div class="row" style="gap:24px">
    <div class="key hw"><h4>Cambridge · Exercise 1G (part 1)</h4><table><tr><td>Five-number summary from a dot or stem plot</td><td>Q1–2</td></tr><tr><td>Boxplot from a five-number summary</td><td>Q3–6</td></tr><tr><td>Boxplot using a CAS calculator</td><td>Q7</td></tr><tr><td>Reading values from a boxplot</td><td>Q8–10</td></tr></table></div>
    <div class="key hw"><h4>Cambridge · Exercise 1G (part 2)</h4><table><tr><td>Reading percentages from a boxplot</td><td>Q11–13</td></tr><tr><td>Describing a distribution from a boxplot</td><td>Q14–15</td></tr><tr><td>Using a boxplot to answer statistical questions</td><td>Q16</td></tr><tr><td>Exam 1 style questions</td><td>Q17–20</td></tr></table></div></div>
  <div class="key hw" style="margin-top:18px"><h4>Revision book</h4><p style="font-size:26px">The <b>1G</b> section</p></div>
</section>''')

h=open(SRC,encoding='utf-8').read()
i=h.find('</style>'); j=h.find('<section'); k=h.rfind('</section>')+len('</section>')
head=h[:i]
head=re.sub(r'<title>.*?</title>','<title>12MAG · S4 · The five-number summary and the boxplot</title>',head)
head=head.replace('S3 · Centre and spread','S4 · Five-number summary and boxplots')
tail=h[k:]
for a,b in [('s3apply(s,f);','s3apply(s,f);s4apply(s,f);'),('s3reset(s);','s3reset(s);s4reset(s);'),('s3init();','s3init();s4init();')]:
    assert tail.count(a)==1,a; tail=tail.replace(a,b)
tail=tail.replace('/* ---------- reveal engine ---------- */',open(f'{HERE}/extra.js',encoding='utf-8').read()+'\n/* ---------- reveal engine ---------- */',1)
assert 'function s4apply' in tail
css=open(f'{HERE}/extra.css',encoding='utf-8').read()+'.hj87{transition:all .3s}\n'
out=head+css+h[i:j]+'\n'.join(S)+tail
open(OUT,'w',encoding='utf-8').write(out)
print('slides',len(S),'bytes',len(out))
