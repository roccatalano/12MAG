import re, json, html
SRC='/home/claude/teaching-dashboard-2027/lessons/gm12/S2-slides.html'
OUT='/home/claude/teaching-dashboard-2027/lessons/gm12/S3-slides.html'
CAM='Cambridge General Mathematics Units 3&amp;4'
EDR='Edrolo General Mathematics Units 3&amp;4'

def stem(rid, rows, key, cap='', fs=26, start=0):
    """rows: list of (stem, [leaves]) in display order; leaves get data-i in reading order"""
    i=start; tr=''
    for st,lv in rows:
        sp=''.join(f'<span class="lf2" data-i="{(i:=i+1)-1}">{l}</span>' for l in lv)
        tr+=f'<tr><td class="st">{st}</td><td class="lv">{sp}</td></tr>'
    c=f'<div class="stemcap">{"<b>"+cap+"</b> &nbsp; " if cap else ""}{key}</div>'
    return f'<div>{c}<table class="stem3" id="{rid}" style="font-size:{fs}px">{tr}</table></div>'

def seq(rid, vals, fs=25, gaps=()):
    out=''
    for k,v in enumerate(vals):
        if k in gaps: out+='<span class="gap"></span>'
        out+=f'<span data-i="{k}">{v}</span>'
    return f'<div class="seqrow" id="{rid}" style="font-size:{fs}px">{out}</div>'

def cards(items):
    h='<div class="stepsH">'
    for k,(t,b,attr) in enumerate(items,1):
        h+=f'<div class="sc"><div class="n">{k}</div><div class="frag" {attr}><div class="st">{t}</div><div class="sb">{b}</div></div></div>'
    return h+'</div>'

def vid(n):
    return f'<button class="vid" data-src="" data-label="Cambridge GO · Example {n} (1F Resources)">▶ Video</button>'

def hist(rid,cfg,style=''):
    return f'<div class="chart" id="{rid}" data-chart="hist" data-cfg=\'{json.dumps(cfg)}\' style="{style}"></div>'

def dot3(rid,cfg):
    return f'<div class="chart" id="{rid}" data-chart="dot3" data-cfg=\'{json.dumps(cfg)}\'></div>'

S=[]
# ---------------- 1 title
S.append('''<section class="slide s-title">
  <div class="kicker"><i></i>Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 3</div>
  <h1>Where’s the <span>middle</span>?<br>How <span>spread out</span>?</h1>
  <div class="sub">1F Measures of centre and spread: median, quartiles, IQR, mean and standard deviation</div>
  <div class="flow"><div style="border-color:#00838F">CFAT 1.1.1</div><div style="border-color:#00838F">Do Now</div><div style="border-color:var(--apk)">APK</div><div style="border-color:var(--learn)">Learn</div><div style="border-color:var(--we)">Worked examples</div><div style="border-color:var(--yt)">You try</div><div style="border-color:var(--exit)">Exit tasks</div></div>
  <div class="foot"><span>12MAG · General Mathematics 3&amp;4</span><span>S3</span></div>
</section>''')
# ---------------- 2 today's lesson
LI=['To be able to understand the mean and the median as measures of centre.',
    'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
    'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.',
    'To be able to use a CAS calculator to calculate these summary statistics.']
S.append('''<section class="slide">
  <div class="pill">Today’s lesson</div>
  <h2 style="margin-bottom:14px">Today’s lesson</h2>
  <div class="lisc" style="grid-template-columns:1.15fr 1fr"><div><h3>Learning intentions</h3><ul>'''+''.join(f'<li style="font-size:22px;padding:6px 0 6px 32px">{x}</li>' for x in LI)+'''</ul></div>
    <div><h3>Lesson sequence</h3><ol class="seq">
      <li style="--c:#00838F">CFAT 1.1.1 <small>· 20 minutes, 1A–1E</small></li>
      <li style="--c:#00838F">Do Now <small>· four current VCAA questions</small></li>
      <li style="--c:var(--apk)">APK <small>· Year 11 skills</small></li>
      <li>The median <small>→ WE 14, 15, 16</small></li>
      <li>Range, quartiles and IQR <small>→ WE 17, 18, 19, 20</small></li>
      <li>The mean <small>→ WE 21</small></li>
      <li>Mean or median? Standard deviation <small>· CAS</small></li>
      <li style="--c:var(--exit)">Exit tasks <small>· two VCAA questions</small></li>
      <li style="--c:var(--muted)">Check-in and homework</li></ol></div>
  </div>
</section>''')
SC=['I can find the median value in a data set.','I can find the median value from a dot plot.','I can find the median value from a stem plot.','I can find the range from a stem plot.',
    'I can find the IQR from a stem plot when n is even.','I can find the IQR from a stem plot when n is odd.','I can calculate the mean using the formula.','I can calculate the mean and standard deviation using the CAS calculator.']
def scgrid(): return '<div class="lisc" style="grid-template-columns:1fr 1fr"><ul>'+''.join(f'<li>{x}</li>' for x in SC[:4])+'</ul><ul>'+''.join(f'<li>{x}</li>' for x in SC[4:])+'</ul></div>'
S.append(f'''<section class="slide">
  <div class="pill">Success criteria</div>
  <h2>By the end of this lesson you’ll be able to say…</h2>
  {scgrid()}
</section>''')
# ---------------- 4 CFAT
S.append('''<section class="slide cfat" data-cfu="qw">
  <div class="pill">CFAT 1.1.1 · 1A–1E</div>
  <h2>CFAT 1.1.1: types of data, displays, log scales</h2>
  <div class="row" style="gap:40px;align-items:stretch">
    <div class="key" style="flex:1"><h4>How it runs</h4><ul class="bul" style="font-size:26px;line-height:1.6;margin-left:30px"><li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>6 multiple choice + short answer · <b>13 marks</b></li><li>Covers last week: 1A–1E</li><li>Pens down when the timer ends</li></ul></div>
    <div class="key" style="flex:.8;display:flex;flex-direction:column;justify-content:center"><h4 style="text-align:center">Time remaining</h4><div class="timer" id="cfatT">20:00</div><p class="frag muted" data-act="timer" style="text-align:center;font-size:20px">Timer running · click on when you’re ready to go</p></div>
  </div>
  <div class="src">CFAT 1.1.1 is on the teaching dashboard (lessons/gm12/CFAT-1.1.1)</div>
</section>''')
# ---------------- 5 Do Now 1: 2025 NHT E1 Q4
S.append('''<section class="slide mcslide dn" data-cfu="mc">
  <div class="pill">Do Now 1 of 4 · VCAA 2025 NHT · Exam 1</div>
  <div class="stat">VCAA: NHT report gives answers only</div>
  <h2>Review of 1C</h2>
  <div class="row" style="gap:36px"><div class="q" style="flex:1"><div class="stem">The <em class="v">systolic blood pressure</em> of 50 people was recorded. The results are summarised in the histogram below.<br><br>For this group of people, the distribution of their <em class="v">systolic blood pressure</em> is best described as</div>
  <div class="mc"><div data-o="A"><b>A.</b>symmetric.</div><div data-o="B"><b>B.</b>bell-shaped.</div><div data-o="C"><b>C.</b>positively skewed.</div><div data-o="D"><b>D.</b>negatively skewed.</div></div></div>
  <div style="flex:1">'''+hist('dn1h',{"start":95,"w":5,"v":[4,6,8,10,8,5,4,2,1,1,1],"ymax":12,"ystep":2,"tick":5,"xl":"systolic blood pressure","yl":"frequency","h":360,"W":640,"fs":17})+'''</div></div>
  <div class="mcsol"><div class="ansbox frag" data-key="C" data-s="sol"><div class="lab">Solution · C</div><p>Most values sit at the low end (100–120) and the tail stretches out to the right, towards 150: <b>positively skewed</b>.</p></div><div class="frag" data-s="sol" style="flex:1;display:flex"><div class="dbox none"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="-"><p>No % data: the NHT report gives answers only. Watch for D (the tail is on the right, so it is positive).</p></div></div></div></div>
  <div class="src">VCAA 2025 NHT General Mathematics Exam 1 Q4</div>
</section>''')
# ---------------- 6 Do Now 2: 2024 NHT E1 Q4
S.append('''<section class="slide mcslide dn" data-cfu="mc">
  <div class="pill">Do Now 2 of 4 · VCAA 2024 NHT · Exam 1</div>
  <div class="stat">VCAA: NHT report gives answers only</div>
  <h2>Review of 1E</h2>
  <div class="row" style="gap:36px"><div class="q" style="flex:1;font-size:22px"><div class="stem">The histogram below shows the distribution of the <em class="v">GDP per capita</em>, in dollars per year, for a sample of 22 countries in 2021 plotted on a logarithmic (base 10) scale.<br><br>Australia is one of these 22 countries, and its <em class="v">GDP per capita</em> value is $56 281.<br>Which one of the columns marked A, B, C, D or E would contain Australia’s value?</div>
  <div class="mc cols"><div data-o="A"><b>A.</b>A</div><div data-o="B"><b>B.</b>B</div><div data-o="C"><b>C.</b>C</div><div data-o="D"><b>D.</b>D</div><div data-o="E"><b>E.</b>E</div></div></div>
  <div style="flex:1;position:relative">'''+hist('dn2h',{"start":3.6,"w":0.2,"v":[3,4,4,3,0,3,4,1],"xmax":5.4,"ymax":6,"ystep":1,"tick":0.2,"dec":1,"xl":"log10 (GDP per capita)","yl":"frequency","h":360,"W":640,"fs":17,"col":"#3a3f4b"}).replace('data-chart','data-lab=\'[[2,"A"],[3,"B"],[5,"C"],[6,"D"],[7,"E"]]\' data-chart')+'''
    </div></div>
  <div class="mcsol"><div class="ansbox frag" data-key="C" data-s="sol"><div class="lab">Solution · C</div><p>\\(\\log_{10}(56\\,281)=4.750\\ldots\\), which falls in the column from 4.6 to 4.8: column <b>C</b>.</p></div><div class="frag" data-s="sol" style="flex:1;display:flex"><div class="dbox none"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="-"><p>No % data: the NHT report gives answers only. Watch for D: 4.75 is close to 4.8, but it is still below it.</p></div></div></div></div>
  <div class="src">VCAA 2024 NHT General Mathematics Exam 1 Q4 · Data: &lt;data.worldbank.org&gt;</div>
</section>''')
# ---------------- Do Now 3: 2026 E2 Q2b
S.append('''<section class="slide dn" data-cfu="qw">
  <div class="pill">Do Now 3 of 4 · VCAA 2026 · Exam 2</div>
  <div class="stat">VCAA: report not yet released</div>
  <h2>Review of 1C</h2>
  <div class="row" style="gap:30px">
    <div class="q" style="flex:.9;font-size:21px;padding:14px 22px">The <em class="v">happiness index</em> scores for 141 countries, based on 2024 data, are summarised in the table below.<br>All <em class="v">happiness index</em> scores range from 0 to 10 and contain two decimal places.
      <table class="t" style="font-size:17px;margin:8px 0"><tr><th>Score range</th><th>Frequency</th></tr>'''+''.join(f'<tr><td style="padding:0 12px">{a}</td><td style="padding:0 12px">{b}</td></tr>' for a,b in [('0.00–0.99',0),('1.00–1.99',1),('2.00–2.99',1),('3.00–3.99',14),('4.00–4.99',30),('5.00–5.99',38),('6.00–6.99',45),('7.00–7.99',12),('8.00–8.99',0),('9.00–10.00',0)])+'''</table>
      <p class="muted" style="font-size:13px">Data: Adapted from World Population Review &lt;worldpopulationreview.com/country-rankings/happiest-countries-in-the-world&gt;</p></div>
    <div style="flex:1.1"><div class="q" style="font-size:21px;padding:12px 22px"><b>b.</b> A histogram is used to show the distribution of <em class="v">happiness index</em> scores for all 141 countries. The incomplete histogram below has been constructed from the data in the table. Complete the histogram below by adding the missing bars. <span class="muted">(1 mark)</span></div>
      '''+hist('dn3h',{"start":0,"w":1,"v":[0,1,1,14,30,38,45,12,0,0],"ymax":50,"ystep":10,"dec":2,"xl":"happiness index","yl":"frequency","h":330,"W":640,"fs":15,"col":"#b8bcc4"}).replace('data-chart','data-miss="2,4,5,7" data-chart')+'''
      <div class="sol" style="margin-top:4px"><p class="frag" data-showbar="#dn3h|2,4,5,7">Add the bars 2.00–2.99 (1), 4.00–4.99 (30), 5.00–5.99 (38) and 7.00–7.99 (12).</p></div></div></div>
  <div class="src">VCAA 2026 General Mathematics Exam 2 Q2b (teacher solution; examiner report not yet released)</div>
</section>''')
# ---------------- 7 Do Now 3: 2024 NHT E2 Q2a
def t3row(lab,a,b):
    return f'<tr><th class="l" rowspan="2">{lab}</th>'+''.join(f'<td style="padding:2px 10px">{x}</td>' for x in a)+'</tr><tr>'+''.join(f'<td style="padding:2px 10px">{x}</td>' for x in b)+'</tr>'
S.append('''<section class="slide dn" data-cfu="qw">
  <div class="pill">Do Now 4 of 4 · VCAA 2024 NHT · Exam 2</div>
  <div class="stat">VCAA: NHT report gives answers only</div>
  <div class="row" style="margin-top:14px;gap:34px">
    <div class="q" style="flex:1.15;font-size:22px;padding:16px 24px">In the year 2021 there were 12 days where a new moon appeared in Sydney Harbour.<br>For these 12 days the occurrence of the highest high tides (HHT) and lowest low tides (LLT) occurred before, on or after the appearance of the new moon.<br>These records are displayed in the table below.
      <p style="font-size:18px;font-weight:700;margin:10px 0 4px">Table 3</p><table class="t" style="font-size:18px">'''+t3row('LLT',['on','before','before','after','after','after'],['after']*6)+t3row('HHT',['on','before','before','before','after','after'],['after','on','on','after','after','after'])+'''</table>
      <p class="muted" style="font-size:15px;margin-top:4px">Data: http://www.bom.gov.au/australia/tides/</p>
      <br><b>a.</b> Use the data from Table 3 to complete the following frequency table. <span class="muted">(2 marks)</span></div>
    <div style="flex:.8"><p style="font-size:18px;font-weight:700;margin-bottom:4px">Table 4</p><table class="t" style="font-size:24px;width:100%"><tr><th rowspan="2" class="l">Occurrence</th><th colspan="2">Frequency</th></tr><tr><th>LLT</th><th>HHT</th></tr>
      <tr><td class="l">before</td><td><span class="cell" data-c="1">2</span></td><td><span class="cell" data-c="2">3</span></td></tr>
      <tr><td class="l">on</td><td><span class="cell" data-c="1">1</span></td><td><span class="cell" data-c="2">3</span></td></tr>
      <tr><td class="l">after</td><td><span class="cell" data-c="1">9</span></td><td><span class="cell" data-c="2">6</span></td></tr>
      <tr class="tot"><td class="l">Total</td><td>12</td><td>12</td></tr></table>
      <div class="stepsH" style="margin-top:22px"><div class="sc"><div class="n">1</div><div class="frag"><div class="st">LLT</div><div class="sb">Tally both LLT rows: before 2, on 1, after 9.</div></div></div><div class="sc"><div class="n">2</div><div class="frag"><div class="st">HHT</div><div class="sb">Before 3, on 3, after 6. Each column totals 12.</div></div></div></div></div>
  </div>
  <div class="src">VCAA 2024 NHT General Mathematics Exam 2 Q2a (NHT report: answers only)</div>
</section>''')
# ---------------- 8 APK
party=[19,21,22,56,34,19,27,28,34,17,66,37,20,20,21,45,26,19,23,29]
S.append(f'''<section class="slide apk" data-cfu="qw">
  <div class="pill">APK · from Year 11</div>
  <h2 style="margin-bottom:12px">Back to the party</h2>
  <div class="row" style="gap:34px"><div class="q" style="flex:1.05;font-size:23px">The ages of a group of people at a party:
      <div class="data" style="font-size:22px">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>
      <ol class="sub"><li data-part="a"><b>a</b>Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?</li><li data-part="b"><b>b</b>Determine the quartiles and hence the IQR of the ages of the people at the party.</li></ol></div>
    <div style="flex:.95">{stem('apks',[(1,[7,9,9,9]),(2,[0,0,1,1,2,3,6,7,8,9]),(3,[4,4,7]),(4,[5]),(5,[6]),(6,[6])],'Key: 1 | 7 = 17','age (years)',24)}
      <div class="sol" style="margin-top:10px">
        <p class="frag" data-p="a" data-mark="#apks|9,10|mid">\\(\\bar x=\\tfrac{{583}}{{20}}=\\)<span class="reveal">29.15</span>; &nbsp;M \\(=\\tfrac{{23+26}}{{2}}=\\)<span class="reveal">24.5</span>. <b>Median</b>: skewed with outliers (56, 66).</p>
        <p class="frag" data-p="b" data-mark="#apks|4,5,14,15|q1m">Q<sub>1</sub> \\(=\\tfrac{{20+20}}{{2}}=20\\), Q<sub>3</sub> \\(=\\tfrac{{34+34}}{{2}}=34\\), IQR <span class="reveal">= 14</span></p></div></div></div>
  <div class="src">Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2E #10, 2F #11 (teacher solutions)</div></section>''')
eggs=[172,192,159,125,197,135,140,140,138,166,136,131]
S.append(f'''<section class="slide apk" data-cfu="qw">
  <div class="pill">APK · VCAA 2017 · Exam 2</div>
  <div class="stat">VCAA: <b>?%</b> scored 1/1</div>
  <h2>From Year 11 exam practice</h2>
  <div class="q">The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.
    <table class="t" style="font-size:22px;margin:14px 0;width:100%"><tr><th class="l"><em class="v">number of eggs</em></th>{''.join(f'<td>{x}</td>' for x in eggs)}</tr></table>
    From the information given, determine the range. <span class="muted">(1 mark)</span>
    <div class="ansbox frag" data-stat="87" style="margin-top:16px"><div class="lab">Solution</div><p>largest = 197, smallest = 125 → range \\(=197-125=\\) <b>72</b> eggs</p></div></div>
  <div class="src">Edrolo General Mathematics Units 1&amp;2 · 1D Q18 · VCAA 2017 Exam 2 Data analysis Q1ai (87% of students answered this question correctly)</div></section>''')
# ---------------- 9 Learn: centre and spread overview
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1F</div>
  <h2>Two questions about any distribution</h2>
  <div class="row" style="gap:36px">
    <div class="key frag" style="flex:1"><h4>Where is the centre?</h4><p><b style="color:#d2475b">median</b> (M): the middle value</p><p style="margin-top:6px"><b style="color:#2f6fdf">mean</b> (\\(\\bar x\\)): the balance point</p></div>
    <div class="key frag" style="flex:1.2"><h4>How spread out is it?</h4><p><b>range</b>: largest − smallest</p><p style="margin-top:6px"><b style="color:#6a3fc7">IQR</b>: spread of the middle 50%</p><p style="margin-top:6px"><b style="color:#1f9e74">standard deviation</b> (s): spread around the mean</p></div></div>
  <div class="tip frag" style="font-size:24px;margin-top:26px"><b>They come in pairs:</b> median with IQR · mean with standard deviation.</div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1F pp. 44, 50–52</div></section>''')
# ---------------- 10 Learn: median explainer
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1F</div>
  <h2 style="margin-bottom:14px">The median: the middle value</h2>
  <div class="xp" id="medx" style="height:236px"></div>
  <span class="frag" data-act="m-order"></span><span class="frag" data-act="m-count"></span><span class="frag" data-act="m-even"></span><span class="frag" data-act="m-evenmid"></span>
  <div class="key frag" style="margin-top:18px;padding:16px 28px"><h4>The median</h4><p style="font-size:24px">The median is the middle value in an ordered data set.<br>For <i>n</i> data values the median is located at the \\(\\dfrac{n+1}{2}\\)th position. When:</p><ul class="bul" style="font-size:23px;margin-top:2px"><li><i>n</i> is odd, the median will be the middle data value</li><li><i>n</i> is even, the median will be the average of the two middle data values.</li></ul></div>
  <div class="src">Key box: Cambridge General Mathematics Units 3&amp;4, 1F p. 44 · Animation data: teacher example</div></section>''')
# ---------------- 11 WE14
a=[2,9,1,8,3,5,3,8,1]; b=[10,1,3,4,8,6,10,1,2,9]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 14 · 1F</div>{vid(14)}
  <div class="wename">Finding the median value in a data set</div>
  <div class="q" style="margin-top:14px">Order each of the following data sets, locate the median, and then write down its value.
    <ol class="sub"><li data-part="a"><b>a</b><span class="data" style="font-size:24px">2 9 1 8 3 5 3 8 1</span></li><li data-part="b"><b>b</b><span class="data" style="font-size:24px">10 1 3 4 8 6 10 1 2 9</span></li></ol></div>
  <div class="row" style="gap:40px;margin-top:16px">
    <div class="sol" style="margin-top:0"><div class="frag" data-p="a" data-s="ao"><p><b>a</b> \\(n=9\\) (odd): \\(\\tfrac{{9+1}}{{2}}=5\\)th value</p>{seq('w14a',sorted(a))}</div><p class="frag" data-p="a" data-count="#w14a">Median = <span class="reveal">3</span></p></div>
    <div class="sol" style="margin-top:0"><div class="frag" data-p="b" data-s="bo"><p><b>b</b> \\(n=10\\) (even): average of the 5th and 6th</p>{seq('w14b',sorted(b))}</div><p class="frag" data-p="b" data-count="#w14b">Median \\(=\\tfrac{{4+6}}{{2}}=\\)<span class="reveal">5</span></p></div></div>
  {cards([('Order','Write the data set in order.',''),('Locate','Odd: the middle value. Even: the two middle values.',''),('Check','Equal numbers of values on each side of the median.','')])}
  <div class="src">{CAM} · Example 14</div></section>''')
# ---------------- 12 YT Edrolo 1E WE1
d=[3,5,1,10,8,9,6,3,8,6]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the median value in a data set</div>
  <div class="q" style="margin-top:16px">Construct a five-number summary for the following data.<div class="data">3 5 1 10 8 9 6 3 8 6</div></div>
  <div class="sol">
    <div class="frag" data-p="x"><p>In order (\\(n=10\\)):</p>{seq('y14',sorted(d),gaps=(5,))}</div>
    <p class="frag" data-mark="#y14|0,9|ext">minimum = 1, maximum = 10</p>
    <p class="frag" data-count="#y14">median: \\(\\tfrac{{10+1}}{{2}}=5.5\\)th position, \\(\\tfrac{{6+6}}{{2}}=6\\)</p>
    <p class="frag" data-count="#y14|0|4|q1m #y14|5|9|q1m">Q<sub>1</sub> = median of the lower half = 3 · Q<sub>3</sub> = median of the upper half = 8</p>
    <p class="frag big">Five-number summary: <span class="reveal">1, 3, 6, 8, 10</span></p></div>
  <div class="src">{EDR} · 1E Worked example 1</div></section>''')
# ---------------- 13 WE15
cric=[18,18,19,19,22,22,22,22,23,23,24,25,29]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 15 · 1F</div>{vid(15)}
  <div class="wename">Finding the median value from a dot plot</div>
  <div class="row" style="margin-top:14px;gap:36px;align-items:center">
    <div class="q" style="flex:.8">The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team.<br><br>Determine the median age of these cricketers and mark its location on the dot plot.</div>
    <div style="flex:1.2">{dot3('w15d',{"min":17,"max":30,"vals":cric,"xl":"Age (years)","W":900,"h":250,"r":13})}
      <div class="sol"><p class="frag" data-p="x">\\(n=13\\): the median is the \\(\\tfrac{{13+1}}{{2}}=7\\)th value from either end.</p><p class="frag big" data-dotmark="#w15d|6">Median = <span class="reveal">22 years</span></p></div></div></div>
  {cards([('Count','13 dots, so the 7th value is the middle.',''),('Locate','Count in from the left: 18, 18, 19, 19, 22, 22, <b>22</b>.',''),('Write','Mark it on the plot. Median = 22 years.','')])}
  <div class="src">{CAM} · Example 15</div></section>''')
# ---------------- 14 YT Edrolo 1F WE2a
ed=[23]+[24]*2+[25]*4+[26]*4+[27]*7+[28]*5+[29]*3+[30,31]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the median value from a dot plot</div>
  <div class="row" style="margin-top:14px;gap:36px;align-items:center">
    <div class="q" style="flex:.7">Consider the dot plot.<ol class="sub"><li><b>a.</b>Determine the median.</li></ol></div>
    <div style="flex:1.3">{dot3('y15d',{"min":22,"max":31,"vals":ed,"W":900,"h":300,"r":12})}</div></div>
  <div class="sol"><p class="frag">There are 28 data points: \\(\\tfrac{{28+1}}{{2}}=14.5\\), so average the 14th and 15th data points.</p><p class="frag big" data-dotmark="#y15d|13,14|#d98a1f">\\(\\tfrac{{27+27}}{{2}}=\\)<span class="reveal">27</span></p></div>
  <div class="src">{EDR} · 1F Worked example 2a</div></section>''')
# ---------------- 15 WE16
w16=[('1',[8,9,9]),('2',[0,2,5,7,8,9,9]),('3',[1,3])]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 16 · 1F</div>{vid(16)}
  <div class="wename">Finding the median value from a stem plot</div>
  <div class="row" style="margin-top:16px;gap:40px">
    <div class="q" style="flex:1">The stem plot opposite displays the maximum temperature (in °C) for 12 days in January.<br><br>Determine the median maximum temperature for these 12 days.</div>
    <div style="flex:.8;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 24px">{stem('w16s',w16,'Key: 0|8 = 8°C','',30)}
      <div class="sol"><p class="frag" data-count="#w16s">Count in from both ends: 25 and 27 are the 6th and 7th values.</p><p class="frag big">\\(M=\\tfrac{{25+27}}{{2}}=\\)<span class="reveal">26°C</span></p></div></div></div>
  {cards([('n is even','12 values: the median is the average of the two middle values.',''),('Locate','Count in 6 from each end: 25 and 27.',''),('Average','\\(\\tfrac{25+27}{2}=26\\)°C','')])}
  <div class="src">{CAM} · Example 16</div></section>''')
# ---------------- 16 YT Edrolo 1F WE3a
e3=[('40',[7]),('41',[]),('42',[]),('43',[]),('44',[4,6]),('45',[1,3,3]),('46',[2,6,7]),('47',[4,7,8,9]),('48',[0,0,4,5,6,8]),('49',[1,2,5,5,5,9]),('50',[3,4,4,7,8,8,9,9])]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the median value from a stem plot</div>
  <div class="row" style="margin-top:14px;gap:40px">
    <div class="q" style="flex:.8">Consider the stem plot.<ol class="sub"><li><b>a.</b>Calculate the median.</li></ol>
      <div class="sol"><p class="frag">There are 33 data points: \\(\\tfrac{{33+1}}{{2}}=17\\), so the median is the 17th data point.</p><p class="frag big" data-count="#y16s">Median = <span class="reveal">485</span></p></div></div>
    <div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px 24px">{stem('y16s',e3,'Key: 40 | 7 = 407','',22)}</div></div>
  <div class="src">{EDR} · 1F Worked example 3a</div></section>''')
# ---------------- 17 Learn: range, quartiles, IQR explainer
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1F</div>
  <h2 style="margin:8px 0 10px;font-size:42px">Quartiles cut the ordered data into quarters</h2>
  <div class="xp" id="qx" style="height:400px"></div>
  <span class="frag" data-act="q-0-m"></span><span class="frag" data-act="q-0-q"></span><span class="frag" data-act="q-0-band"></span><span class="frag" data-act="q-1-show"></span><span class="frag" data-act="q-1-m"></span><span class="frag" data-act="q-1-q"></span><span class="frag" data-act="q-1-band"></span>
  <div class="row" style="gap:20px;margin-top:12px"><div class="key frag" style="padding:10px 20px"><p style="font-size:22px"><b>Range</b> \\(R=\\) largest − smallest</p></div><div class="key frag" style="padding:10px 20px;flex:2.4"><p style="font-size:22px">Q<sub>1</sub> = median of lower half · Q<sub>3</sub> = median of upper half · IQR = Q<sub>3</sub> − Q<sub>1</sub></p></div></div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1F pp. 46–47 · Animation data: teacher example</div></section>''')
# ---------------- 18 WE17
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 17 · 1F</div>{vid(17)}
  <div class="wename">Finding the range from a stem plot</div>
  <div class="row" style="margin-top:16px;gap:40px">
    <div class="q" style="flex:1">The stem plot opposite displays the maximum temperature (in °C) for 12 days in January.<br><br>Determine the temperature range over these 12 days.</div>
    <div style="flex:.8;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 24px">{stem('w17s',w16,'Key: 0|8 = 8°C','',30)}
      <div class="sol"><p class="frag" data-mark="#w17s|0,11|ext">Lowest = 18, highest = 33</p><p class="frag big">range \\(=33-18=\\)<span class="reveal">15°C</span></p></div></div></div>
  {cards([('Identify','The lowest and highest values in the stem plot.',''),('Substitute','\\(R=\\) largest − smallest \\(=33-18=15\\)°C','')])}
  <div class="src">{CAM} · Example 17</div></section>''')
# ---------------- 19 YT Edrolo 1E WE2a  /  20 YT 1E WE2b
net=[('2',[2,3,5,7,9]),('3',[0,1,3,5,7,7,8]),('4',[0,1,2,2])]
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the range from a stem plot</div>
  <div class="row" style="margin-top:16px;gap:40px">
    <div class="q" style="flex:1">The following stem plot displays the number of <em class="v">goals scored</em> by 16 netball teams over a season.<ol class="sub"><li><b>a.</b>Calculate the range of <em class="v">goals scored</em>.</li></ol>
      <div class="sol"><p class="frag" data-mark="#y17s|0,15|ext">minimum = 22, maximum = 42</p><p class="frag big">range \\(=42-22=\\)<span class="reveal">20 goals</span></p></div></div>
    <div style="flex:.7;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 24px">{stem('y17s',net,'Key: 2 | 2 = 22 goals','',30)}</div></div>
  <div class="src">{EDR} · 1E Worked example 2a</div></section>''')
# ---------------- WE18
cats=[('1',[9]),('2',[1,3,5,8]),('3',[0,0,4,9,9]),('4',[0,4,5,8]),('5',[0,3]),('6',[3,4])]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 18 · 1F</div>{vid(18)}
  <div class="wename">Finding the IQR from an ordered stem plot when n is even</div>
  <div class="row" style="margin-top:14px;gap:36px">
    <div class="q" style="flex:.9">Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.
      <div style="margin-top:12px">{stem('w18s',cats,'1 | 2 represents 1.2 kg','Weight (kg)',28)}</div></div>
    <div class="sol" style="flex:1.1;margin-top:0">
      <p class="frag">18 values: nine in the lower ‘half’, nine in the upper ‘half’.</p>
      <p class="frag" data-count="#w18s|0|8|q1m">Lower half: 1.9 2.1 2.3 2.5 <b>2.8</b> 3.0 3.0 3.4 3.9 → Q<sub>1</sub> = <span class="reveal">2.8</span></p>
      <p class="frag" data-count="#w18s|9|17|q1m">Upper half: 3.9 4.0 4.4 4.5 <b>4.8</b> 5.0 5.3 6.3 6.4 → Q<sub>3</sub> = <span class="reveal">4.8</span></p>
      <p class="frag big">IQR \\(=Q_3-Q_1=4.8-2.8=\\)<span class="reveal">2.0</span></p></div></div>
  {cards([('Split','18 values: 9 in each half.',''),('Q₁','5th value from the bottom.',''),('Q₃','5th value from the top.',''),('IQR','\\(Q_3-Q_1\\)','')])}
  <div class="src">{CAM} · Example 18</div></section>''')
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the IQR from an ordered stem plot when n is even</div>
  <div class="row" style="margin-top:16px;gap:40px">
    <div class="q" style="flex:1">The following stem plot displays the number of <em class="v">goals scored</em> by 16 netball teams over a season.<ol class="sub"><li><b>b.</b>Calculate the IQR of <em class="v">goals scored</em>.</li></ol>
      <div class="sol"><p class="frag">\\(n=16\\): position of median \\(=\\tfrac{{16+1}}{{2}}=8.5\\), so 8 values in each half.</p>
        <p class="frag" data-count="#y18s|0|7|q1m">Lower half: 22 23 25 27 29 30 31 33 → \\(Q_1=\\tfrac{{27+29}}{{2}}=28\\)</p>
        <p class="frag" data-count="#y18s|8|15|q1m">Upper half: 35 37 37 38 40 41 42 42 → \\(Q_3=\\tfrac{{38+40}}{{2}}=39\\)</p>
        <p class="frag big">IQR \\(=39-28=\\)<span class="reveal">11 goals</span></p></div></div>
    <div style="flex:.6;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 24px">{stem('y18s',net,'Key: 2 | 2 = 22 goals','',30)}</div></div>
  <div class="src">{EDR} · 1E Worked example 2b</div></section>''')
# ---------------- WE19 (no You try)
life=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 19 · 1F</div>{vid(19)}
  <div class="wename">Finding the IQR from an ordered stem plot when n is odd</div>
  <div class="row" style="margin-top:14px;gap:36px">
    <div class="q" style="flex:.85">The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.
      <div style="margin-top:12px">{stem('w19s',life,'Stem: 5|2 = 52 years','',28)}</div></div>
    <div class="sol" style="flex:1.15;margin-top:0">
      <p class="frag" data-count="#w19s">23 values: the median is the 12th value from either end, <b>73</b>.</p>
      <p class="frag">n is odd, so the median is left out: 11 values below it and 11 above it.</p>
      <p class="frag" data-count="#w19s|0|10|q1m">Q<sub>1</sub> = midpoint of the bottom 11 = <span class="reveal">66</span></p>
      <p class="frag" data-count="#w19s|12|22|q1m">Q<sub>3</sub> = midpoint of the top 11 = <span class="reveal">75</span></p>
      <p class="frag big">IQR \\(=Q_3-Q_1=75-66=\\)<span class="reveal">9</span></p>
      <p class="frag smallnote">Check: 52 55 56 64 66 | <b>66</b> | 67 69 71 72 72 | <b>73</b> | 73 74 74 74 74 | <b>75</b> | 75 76 76 77 77 → four groups of 5 values</p></div></div>
  <div class="src">{CAM} · Example 19 (no matching Edrolo worked example, so no You try)</div></section>''')
# ---------------- WE20
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 20 · 1F</div>{vid(20)}
  <div class="wename">Finding the median and quartiles from a histogram</div>
  <div class="row" style="margin-top:12px;gap:34px">
    <div style="flex:1"><div class="q" style="font-size:23px">The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.</div>
      <div class="sol"><p class="frag" data-cum="#w20h">Add the frequencies from left to right: 1, 3, 7, 12, …</p>
        <p class="frag" data-hlbar="#w20h|5|#d2475b">M = 12th value from the bottom: median is in the interval <span class="reveal">60–70</span></p>
        <p class="frag" data-hlbar="#w20h|4|#7b4fd6">Q<sub>1</sub> = 6th value from the bottom: <span class="reveal">50–60</span></p>
        <p class="frag" data-hlbar="#w20h|7|#7b4fd6">Q<sub>3</sub> = 6th value from the top (2 + 6): <span class="reveal">80–90</span></p></div></div>
    <div style="flex:.95">{hist('w20h',{"start":10,"w":10,"v":[1,0,0,2,4,5,3,6,2],"ymax":7,"ystep":1,"xl":"internet hours per week","yl":"Frequency","h":420,"W":640,"fs":18})}</div></div>
  <div class="src">{CAM} · Example 20</div></section>''')
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Finding the median and quartiles from a histogram</div>
  <div class="row" style="margin-top:12px;gap:34px">
    <div style="flex:1"><div class="q">Consider the histogram.<ol class="sub"><li><b>a.</b>Estimate the median.</li></ol></div>
      <div class="sol"><p class="frag">\\(3+15+12+13+9+5+2=59\\) data points; median at \\(\\tfrac{{59+1}}{{2}}=30\\)th</p>
        <p class="frag" data-cum="#y20h">Cumulative frequency: 3, 18, 30, … The 30th data point occurs in the 3–&lt;4 interval.</p>
        <p class="frag big" data-hlbar="#y20h|2|#d98a1f">\\(\\tfrac{{3+4}}{{2}}=\\)<span class="reveal">approximately 3.5</span></p></div></div>
    <div style="flex:.9">{hist('y20h',{"start":1,"w":1,"v":[3,15,12,13,9,5,2],"ymax":16,"ystep":4,"yl":"frequency","h":420,"W":620,"fs":18})}</div></div>
  <div class="src">{EDR} · 1F Worked example 1a</div></section>''')
# ---------------- Learn: mean as balance point
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1F</div>
  <h2 style="margin-bottom:10px">The mean is the balance point</h2>
  <div class="row" style="gap:30px;align-items:center"><div class="formula" style="flex:1">\\(\\bar x=\\dfrac{\\sum x}{n}\\) &nbsp;<span style="font-size:20px;color:#6b7280">\\(\\sum\\) = ‘sum of’, \\(x\\) = a data value, \\(n\\) = number of values</span></div></div>
  <div class="xp" id="balx" style="margin-top:14px"></div>
  <p id="balread" style="font-size:23px;margin-top:10px"></p>
  <span class="frag" data-act="b-8"></span>
  <div class="tip frag" style="font-size:22px"><b>Resistant:</b> the mean is affected by changing the largest data value but the median is not. <span class="muted">Drag the orange dot to try it.</span></div>
  <div class="src">Cambridge General Mathematics Units 3&amp;4, 1F pp. 50–51 (data 2 3 3 4 and 2 3 3 8)</div></section>''')
# ---------------- WE21
rt=[38,36,35,43,46,64,48,25]
S.append(f'''<section class="slide we" data-cfu="cold">
  <div class="pill">Worked example 21 · 1F</div>{vid(21)}
  <div class="wename">Calculating the mean from the formula</div>
  <div class="q" style="margin-top:16px">The following is a set of reaction times (in milliseconds): <span class="data" style="font-size:24px">38 36 35 43 46 64 48 25</span><br>Write down the values of the following, correct to one decimal place.
    <ol class="sub" style="display:flex;gap:80px"><li data-part="a"><b>a</b>\\(n\\)</li><li data-part="b"><b>b</b>\\(\\sum x\\)</li><li data-part="c"><b>c</b>\\(\\bar x\\)</li></ol></div>
  <div class="sol">
    <p class="frag big" data-p="a"><b>a</b> \\(n\\) is the number of data values: \\(n=\\)<span class="reveal">8</span></p>
    <p class="frag big" data-p="b"><b>b</b> \\(\\sum x=38+36+35+43+46+64+48+25=\\)<span class="reveal">335</span></p>
    <p class="frag big" data-p="c"><b>c</b> \\(\\bar x=\\dfrac{{\\sum x}}{{n}}=\\dfrac{{335}}{{8}}=41.875\\) → <span class="reveal">41.9</span></p></div>
  {cards([('Count','\\(n\\) = how many values.',''),('Add','\\(\\sum x\\) = the sum of the values.',''),('Divide','\\(\\bar x=\\sum x \\div n\\), then round.','')])}
  <div class="src">{CAM} · Example 21</div></section>''')
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · 1F</div>
  <div class="wename">Calculating the mean from the formula</div>
  <div class="q" style="margin-top:16px">The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.
    <div class="data">11.60 55.50 7.95 42.15 17.10 2.00 82.55 26.85 5.40 21.90</div></div>
  <div class="sol">
    <p class="frag big">\\(\\sum x=11.60+55.50+7.95+\\dots+21.90=273\\), &nbsp; \\(n=10\\)</p>
    <p class="frag big">\\(\\bar x=\\dfrac{{273}}{{10}}=27.3\\) → <span class="reveal">$27.30</span></p></div>
  <div class="src">{EDR} · 1G Worked example 1</div></section>''')
# ---------------- Learn: mean or median
S.append('''<section class="slide" data-cfu="tps">
  <div class="pill">Learn · 1F</div>
  <h2 style="margin-bottom:12px">Mean or median?</h2>
  <div class="row" style="gap:24px">
    <div class="key frag" style="flex:1"><h4>Symmetric, no outliers</h4>'''+hist('mm1',{"start":0,"w":1,"v":[1,2,4,7,9,7,4,2,1],"ymax":10,"ystep":5,"nox":True,"noy":True,"h":200,"W":520,"vline":4.5})+'''<p style="font-size:21px">mean ≈ median: <b>either</b> can be used</p></div>
    <div class="key frag" style="flex:1"><h4>Clearly skewed and/or outliers</h4>'''+hist('mm2',{"start":0,"w":1,"v":[9,8,5,3,2,1,0,0,1],"ymax":10,"ystep":5,"nox":True,"noy":True,"h":200,"W":520,"vline":2.6})+'''<p style="font-size:21px">the tail drags the mean: use the <b>median</b></p></div></div>
  <div class="key frag" style="margin-top:14px;padding:12px 24px"><h4>Choosing between the mean and the median</h4><p style="font-size:21px">The mean and the median are both measures of the centre of a distribution. If the distribution is:</p><ul class="bul" style="font-size:21px"><li>symmetric and there are no outliers, either the mean or the median can be used to indicate the centre of the distribution</li><li>clearly skewed and/or there are outliers, it is more appropriate to use the median to indicate the centre of the distribution.</li></ul></div>
  <div class="src">Key box: Cambridge General Mathematics Units 3&amp;4, 1F p. 52 · Sketches: teacher illustration (dashed line = mean)</div></section>''')
# ---------------- Learn: standard deviation explainer
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">Learn · 1F</div>
  <h2 style="margin-bottom:8px">Standard deviation: spread around the mean</h2>
  <div class="row" style="gap:24px;align-items:center"><div class="formula" style="flex:none">\\(s=\\sqrt{\\dfrac{\\sum (x-\\bar x)^2}{n-1}}\\)</div><p style="flex:1;font-size:22px;line-height:1.4">Roughly, the typical distance of the data values from the mean. On CAS it is <b>s<sub>x</sub></b>. Same mean, different spread:</p></div>
  <div class="xp" id="sdx" style="margin-top:12px"></div>
  <span class="frag" data-act="sd-a"></span><span class="frag" data-act="sd-ad"></span><span class="frag" data-act="sd-b"></span><span class="frag" data-act="sd-bd"></span><span class="frag" data-act="sd-s"></span>
  <div class="src">Formula: Cambridge General Mathematics Units 3&amp;4, 1F p. 52 · Animation data: teacher example</div></section>''')
# ---------------- CAS from a list
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">CAS · 1F</div>
  <h2 style="margin:10px 0 8px;font-size:40px">Mean and standard deviation from a list</h2>
  <p style="font-size:22px;margin-bottom:8px">The following are the heights (in cm) of a group of women. &nbsp;<span class="data" style="font-size:21px">176 160 163 157 168 172 173 169</span><br>Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.</p>
  <div class="row" style="gap:24px"><div class="cas" style="flex:1.5">
    <div class="key frag"><h4>TI-Nspire</h4><ol><li>New document → <b>Lists &amp; Spreadsheet</b>. Name a list <b>height</b>; enter the data.</li><li>Add <b>Calculator</b>.</li><li>Menu › Statistics › Stat Calculations › <b>One-Variable Statistics</b>. Num of Lists: 1.</li><li>X1 List: <b>height</b>. OK.</li><li>Read \\(\\bar x\\) and <b>sx</b> (the sample standard deviation).</li></ol></div>
    <div class="key frag"><h4>ClassPad</h4><ol><li><b>Statistics</b> app. Name a list <b>height</b>; enter the data.</li><li>Calc › <b>One-Variable</b>.</li><li>XList: main\\height · Freq: 1. OK.</li><li>Read \\(\\bar x\\) and <b>s<sub>x</sub></b>. Scroll for the median, Q<sub>1</sub>, Q<sub>3</sub>, min and max.</li></ol></div></div>
    <div class="key frag" style="flex:.6;align-self:center;text-align:center"><h4>Answer</h4><p style="font-size:30px">\\(\\bar x=167.25\\) cm</p><p style="font-size:30px">\\(s=6.67\\) cm</p></div></div>
  <div class="tip frag" style="font-size:20px"><b>Use s<sub>x</sub>, not σ<sub>x</sub>.</b> General Maths always uses the sample standard deviation.</div>
  <div class="src">Reference: Cambridge General Mathematics Units 3&amp;4, 1F pp. 53–54 (CAS 3)</div></section>''')
# ---------------- CAS from a frequency table
S.append('''<section class="slide" data-cfu="disc">
  <div class="pill">CAS · 1F</div>
  <h2 style="margin:10px 0 8px;font-size:40px">Summary statistics from a frequency table</h2>
  <p style="font-size:22px;margin-bottom:8px">When values repeat (a dot plot or frequency table), enter each value once and its frequency in a second list. Check with the cricket team from Example 15:</p>
  <div class="row" style="gap:24px"><div class="cas" style="flex:1.5">
    <div class="key frag"><h4>TI-Nspire</h4><ol><li>Lists &amp; Spreadsheet: <b>age</b> in column A, <b>freq</b> in column B.</li><li>Add Calculator › Menu › Statistics › Stat Calculations › <b>One-Variable Statistics</b>.</li><li>X1 List: <b>age</b> · Frequency List: <b>freq</b>. OK.</li><li>Read \\(\\bar x\\), <b>sx</b>, <b>n</b>, MedianX.</li></ol></div>
    <div class="key frag"><h4>ClassPad</h4><ol><li>Statistics app: <b>age</b> in list1, <b>freq</b> in list2.</li><li>Calc › <b>One-Variable</b>.</li><li>XList: main\\age · Freq: main\\freq. OK.</li><li>Read \\(\\bar x\\), <b>s<sub>x</sub></b>, <b>n</b>, Med.</li></ol></div></div>
    <div style="flex:.6"><table class="t" style="font-size:22px;width:100%"><tr><th>age</th><td>18</td><td>19</td><td>22</td><td>23</td><td>24</td><td>25</td><td>29</td></tr><tr><th>freq</th><td>2</td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>1</td></tr></table>
      <div class="key frag" style="margin-top:14px;text-align:center"><h4>Check</h4><p style="font-size:24px">\\(n=13\\) · \\(\\bar x=22\\) · \\(s_x=3.08\\) · median \\(=22\\) ✓</p></div></div></div>
  <div class="tip frag" style="font-size:20px"><b>Check n.</b> If n is not the total frequency, the frequency list was not selected.</div>
  <div class="src">Reference: ClassPad Help 402 (statistical calcs from a frequency table) · Data: Cambridge Example 15</div></section>''')
# ---------------- YT CAS Edrolo 1G WE2
S.append(f'''<section class="slide yt" data-cfu="qw">
  <div class="pill">You try · CAS</div>
  <div class="wename">Calculating the mean and standard deviation using the CAS calculator</div>
  <div class="q" style="margin-top:16px">The <em class="v">weight</em>, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ <em class="v">weight</em>, rounded to two decimal places.<div class="data">80 95 85 91 102 93 87 78 84 90</div></div>
  <div class="sol">
    <p class="frag">One-Variable Statistics on the list <b>weight</b>.</p>
    <p class="frag big">mean \\(\\bar x=\\)<span class="reveal">88.50 kg</span></p>
    <p class="frag big">standard deviation \\(s_x=7.230\\ldots\\) → <span class="reveal">7.23 kg</span></p></div>
  <div class="src">{EDR} · 1G Worked example 2</div></section>''')
# ---------------- Exit 1: Edrolo 1G Q11
dens=[1.07,1.07,1.08,1.08,1.03,1.05,1.07,1.06,1.07,1.09,1.02,1.09]; wt=[70.1,90.4,73.2,85.0,84.3,95.6,71.7,95.0,80.2,87.4,94.9,65.3]
td=lambda xs:''.join(f'<td style="padding:2px 7px">{x:.2f}</td>' for x in xs)
tw=lambda xs:''.join(f'<td style="padding:2px 7px">{x:.1f}</td>' for x in xs)
S.append(f'''<section class="slide ex" data-cfu="qw">
  <div class="pill">Exit task 1 of 2 · Edrolo 1G Q11 (adapted from VCAA 2020 Exam 2 Q4aii)</div>
  <div class="stat">VCAA: <b>?%</b> scored 1/1</div>
  <h2>Show what you know</h2>
  <div class="q" style="font-size:23px;padding:16px 24px">The <em class="v">body density</em>, in kilograms per litre, and <em class="v">weight</em>, in kilograms, of a sample of 12 orangutans are shown in the table.
    <div style="margin:12px 0"><table class="t" style="font-size:18px;width:100%"><tr><th class="l"><em class="v">body density</em> (kg/litre)</th>{td(dens)}</tr><tr><th class="l"><em class="v">weight</em> (kg)</th>{tw(wt)}</tr></table></div>
    For these 12 orangutans, determine the mean of their <em class="v">body density</em>, in kilograms per litre. <span class="muted">(1 mark)</span>
    <div class="ansbox frag" data-stat="77" style="margin-top:14px"><div class="lab">Solution</div><p>\\(\\bar x=\\dfrac{{12.78}}{{12}}=\\) <b>1.065</b> kg/litre</p><p class="muted" style="font-size:18px">Examiner: the required answer was 1.065; rounding did not apply, so 1.07 was not accepted.</p></div></div>
  <div class="src">{EDR} · 1G Q11 · Adapted from VCAA 2020 Exam 2 Data analysis Q4aii (77% of students answered this type of question correctly)</div>
</section>''')
# ---------------- Exit 2: 2026 NHT E2 Q1b, d
mam=[('okapi',250),('gorilla',210),('pig',190),('Brazilian tapir',160),('jaguar',100),('grey seal',85),('giant armadillo',60),('sheep',56),('chimpanzee',52),('kangaroo',35),('goat',28),('roedeer',15),('baboon',11),('rhesus monkey',6.8),('raccoon',4.3),('red fox',4.2),('cat',3.3),('echidna',3.0),('rabbit',2.5)]
mt=''.join(f'<tr><td class="l" style="padding:0 10px">{m}</td><td style="padding:0 10px">{w}</td></tr>' for m,w in mam)
S.append(f'''<section class="slide ex" data-cfu="qw">
  <div class="pill">Exit task 2 of 2 · VCAA 2026 NHT Exam 2 Q1b, d</div>
  <div class="stat">VCAA: NHT report gives answers only</div>
  <div class="row" style="margin-top:14px;gap:30px">
    <div class="q" style="flex:1.35;font-size:21px;padding:16px 24px">The table below displays the typical body weight, in kilograms, for a sample of 19 different mammals.
      <ol class="sub" style="margin-top:10px"><li data-part="b"><b>b.</b>Complete the five-number summary in the table below for the variable <em class="v">body weight</em>, in kilograms, by writing in the values for the minimum and the median. <span class="muted">(2 marks)</span>
        <table class="t" style="font-size:20px;margin:8px 0"><tr><th>Minimum</th><th>Q<sub>1</sub></th><th>Median</th><th>Q<sub>3</sub></th><th>Maximum</th></tr><tr><td><span class="frag reveal" data-s="exb">2.5</span></td><td>4.3</td><td><span class="frag reveal" data-s="exb">35</span></td><td>100</td><td>250</td></tr></table></li>
      <li data-part="d"><b>d.</b>The mean body weight is 67 kg, rounded to the nearest whole number.<br>Explain why the median is a better measure of the centre of the body weight data than the mean. <span class="muted">(1 mark)</span></li></ol>
      <div class="sol" style="margin-top:8px"><p class="frag" data-p="b" data-s="exb" data-mark="#ex2t|9|mid #ex2t|0|ext">b. Minimum = 2.5 (rabbit). n = 19, so the median is the \\(\\tfrac{{19+1}}{{2}}=10\\)th value: <b>35</b> (kangaroo).</p><p class="frag" data-p="d">d. The data is (positively) skewed and/or has an outlier, so the mean (67) is dragged above most values; the median is not affected.</p></div></div>
    <div style="flex:.65"><table class="t" id="ex2t" style="font-size:16px;width:100%"><tr><th class="l">Mammal</th><th>Body weight (kg)</th></tr>{''.join(f'<tr><td class="l" style="padding:0 10px">{m}</td><td style="padding:0 10px"><span data-i="{18-k}" style="padding:0 6px;border-radius:6px;border:1.5px solid transparent">{w}</span></td></tr>' for k,(m,w) in enumerate(mam))}</table>
      <p class="muted" style="font-size:12px;margin-top:2px">Data: Adapted from T Allison and DV Cicchetti, ‘Sleep in mammals: ecological and constitutional correlates’, Science, vol. 194, no. 4266, 12 November 1976, pp. 732–734 &lt;lib.stat.cmu.edu/datasets/sleep&gt;</p></div>
  </div>
  <div class="src">VCAA 2026 NHT General Mathematics Exam 2 Q1b, Q1d (NHT report: answers only)</div>
</section>''')
# ---------------- check-in / homework
S.append(f'''<section class="slide" data-cfu="tf">
  <div class="pill">Check-in</div>
  <h2>How did you go?</h2>
  {scgrid()}
  <p class="muted" style="font-size:24px;margin-top:22px">Thumbs up, sideways or down for each one, then rate it on your worksheet: ✓ got it · ~ nearly · ✗ not yet</p>
</section>''')
S.append('''<section class="slide">
  <div class="pill" style="background:#4b5563">Homework</div>
  <h2 style="margin-bottom:16px">Homework</h2>
  <div class="row" style="gap:24px">
    <div class="key hw"><h4>Cambridge · Exercise 1F (part 1)</h4><table><tr><td>Median from data</td><td>Q1–2</td></tr><tr><td>Median from a dot plot</td><td>Q3</td></tr><tr><td>Median and range from a stem plot</td><td>Q4</td></tr><tr><td>Median and quartiles from a dot plot</td><td>Q5</td></tr><tr><td>Median and quartiles from a stem plot</td><td>Q6–9</td></tr><tr><td>Median and quartiles from a histogram</td><td>Q10–11</td></tr></table></div>
    <div class="key hw"><h4>Cambridge · Exercise 1F (part 2)</h4><table><tr><td>Mean, median and mode from data</td><td>Q12–17</td></tr><tr><td>The concept of standard deviation</td><td>Q18–20</td></tr><tr><td>Mean and standard deviation on CAS</td><td>Q21–22</td></tr><tr><td>Exam 1 style questions</td><td>Q23–26</td></tr></table></div></div>
  <div class="key hw" style="margin-top:18px"><h4>Revision book</h4><p style="font-size:26px">The <b>1F</b> section</p></div>
</section>''')

h=open(SRC).read()
i=h.find('</style>'); j=h.find('<section'); k=h.rfind('</section>')+len('</section>')
head=h[:i].replace('S2 · Displaying numerical data and log scales','S3 · Centre and spread')
head=re.sub(r'<title>.*?</title>','<title>12MAG · S3 · Centre and spread: median, quartiles, IQR, mean and standard deviation</title>',head)
tail=h[k:]
tail=tail.replace('s2apply(s,f);','s2apply(s,f);s3apply(s,f);',1).replace('function reset(s){frags(s).forEach(f=>f.classList.remove(\'shown\'));s2reset(s);','function reset(s){frags(s).forEach(f=>f.classList.remove(\'shown\'));s2reset(s);s3reset(s);',1)
assert 's3apply' in tail and 's3reset' in tail
tail=tail.replace('/* ---------- reveal engine ---------- */',open('/home/claude/s3/extra.js').read()+'\ns3init();\n/* ---------- reveal engine ---------- */',1)
# morph is S2-only; drawMorph() is a no-op without #morph
out=head+open('/home/claude/s3/extra.css').read()+h[i:j]+'\n'.join(S)+tail
open(OUT,'w').write(out)
print('slides',len(S),'bytes',len(out))
