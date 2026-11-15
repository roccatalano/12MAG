"""Content for each bound reference card. size: 'half' (half A4) or 'full' (full A4).
Notes are own words (condensed from the slides); examples are Cambridge Examples, cited."""

def bars():
    # Cambridge U3&4 Example 3: cold 3, mild 14, hot 6 (frequency bar chart)
    W, H, x0, y0 = 230, 150, 34, 122
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:22em">']
    for v in range(0, 16, 5):
        y = y0 - v * 7
        s.append(f'<line x1="{x0}" y1="{y}" x2="{W-6}" y2="{y}" stroke="#e3e6ee"/><text x="{x0-5}" y="{y+3}" font-size="9" text-anchor="end">{v}</text>')
    for i, (n, v) in enumerate([('Cold', 3), ('Mild', 14), ('Hot', 6)]):
        x = x0 + 14 + i * 62
        s.append(f'<rect x="{x}" y="{y0-v*7}" width="40" height="{v*7}" fill="#2f6fdf"/><text x="{x+20}" y="{y0+12}" font-size="9" text-anchor="middle">{n}</text>')
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{W-6}" y2="{y0}" stroke="#1b1f2a" stroke-width="1.4"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="10" stroke="#1b1f2a" stroke-width="1.4"/>')
    s.append(f'<text x="{(x0+W)/2}" y="{H-2}" font-size="9" font-weight="700" text-anchor="middle">Climate type</text>')
    s.append(f'<text x="10" y="{y0/2+10}" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 10 {y0/2+10})">Frequency</text></svg>')
    return ''.join(s)

def seg():
    # Cambridge U3&4 Example 4: cold 13.0%, mild 60.9%, hot 26.1%
    H, y0, k = 150, 122, 1.1
    s = [f'<svg viewBox="0 0 170 {H}" width="100%" style="max-width:15em">']
    for v in range(0, 101, 20):
        y = y0 - v * k
        s.append(f'<text x="29" y="{y+3}" font-size="9" text-anchor="end">{v}</text><line x1="31" y1="{y}" x2="34" y2="{y}" stroke="#1b1f2a"/>')
    y = y0
    for n, v, c in [('Cold', 13.0, '#9cc0f5'), ('Mild', 60.9, '#2f6fdf'), ('Hot', 26.1, '#173f8c')]:
        s.append(f'<rect x="44" y="{y-v*k}" width="44" height="{v*k}" fill="{c}" stroke="#fff"/>')
        y -= v * k
    for i, (n, c) in enumerate([('Hot', '#173f8c'), ('Mild', '#2f6fdf'), ('Cold', '#9cc0f5')]):
        s.append(f'<rect x="100" y="{30+i*16}" width="10" height="10" fill="{c}"/><text x="114" y="{39+i*16}" font-size="9">{n}</text>')
    s.append(f'<line x1="34" y1="{y0}" x2="34" y2="10" stroke="#1b1f2a" stroke-width="1.4"/><line x1="34" y1="{y0}" x2="96" y2="{y0}" stroke="#1b1f2a" stroke-width="1.4"/>')
    s.append(f'<text x="10" y="{y0/2+8}" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 10 {y0/2+8})">Percentage</text></svg>')
    return ''.join(s)

A1 = """
<div class="tree">
 <div class="grp"><div>Categorical <span class="small mut">names a quality or group</span></div>
  <div class="two"><div class="leaf"><b>Nominal</b>names only, no order<br><span class="mut">eye colour, car brand</span></div>
  <div class="leaf"><b>Ordinal</b>names <i>and</i> a natural order<br><span class="mut">fitness level, shirt size</span></div></div></div>
 <div class="grp"><div>Numerical <span class="small mut">a quantity</span></div>
  <div class="two"><div class="leaf"><b>Discrete</b>counted: how many?<br><span class="mut">number of pets, pulse rate</span></div>
  <div class="leaf"><b>Continuous</b>measured: how much?<br><span class="mut">height, time, weight, age</span></div></div></div>
</div>
<div class="row">
 <div class="box tip" style="flex:1"><h4>Not sure? Two tests</h4>
  <b>1 · Can you average it?</b> Average weight makes sense; average house number doesn't. Numbers that are only labels are <b>categorical</b>.<br>
  <b>2 · How was it recorded?</b> Weight in kg → numerical. Weight as 'under 60 kg', '60–80 kg', 'over 80 kg' → <b>ordinal</b>.<br>
  <span class="mut">Age is continuous, even when recorded in whole years.</span></div>
 <div class="box ex" style="flex:1.25"><h4>Example 1 · classify the data</h4>
  <table class="t" style="width:100%"><tr><th>Data</th><th>Type</th></tr>
  <tr><td>number of chocolate chips in each of 10 cookies</td><td><b>discrete</b></td></tr>
  <tr><td>time for 20 students to complete a puzzle (s)</td><td><b>continuous</b></td></tr>
  <tr><td>rating of the coach, 1 = Very satisfied … 5 = Very dissatisfied</td><td><b>ordinal</b></td></tr>
  <tr><td>preferred colour, 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow</td><td><b>nominal</b></td></tr>
  <tr><td>weight as 'less than 60kg', '60kg - 80kg', 'more than 80kg'</td><td><b>ordinal</b></td></tr></table></div>
</div>
<div class="box vc"><h4>VCAA 2019 Exam 2 Q1a <span class="pc">81% correct</span></h4>
  The table shows the <b>day number</b> and the <b>minimum temperature</b>, in degrees Celsius, for 15 consecutive days in May 2017.
  <table class="t sm" style="margin:1mm 0"><tr><th>day number</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><th>minimum temperature (°C)</th><td>12.7</td><td>11.8</td><td>10.7</td><td>9.0</td><td>6.0</td><td>7.0</td><td>4.1</td><td>4.8</td><td>9.2</td><td>6.7</td><td>7.5</td><td>8.0</td><td>8.6</td><td>9.8</td><td>7.7</td></tr></table>
  <div class="row" style="align-items:baseline"><span>Which of the two variables in this data set is an ordinal variable? <span class="mut">(1 mark)</span></span>
  <span class="ans"><b>day number</b>: it labels each day in order; it isn't counted or measured.</span></div></div>
"""

import base64 as _b, os as _o
IMG='data:image/png;base64,'+_b.b64encode(open(_o.path.join(_o.path.dirname(__file__),'vcaa2017e1_q5.png'),'rb').read()).decode()

B1 = f"""
<div class="row">
 <div class="box" style="flex:1"><h4>Frequency table</h4>
  Lists each category and how often it occurs, as a <b>number</b> and a <b>percentage</b>.
  <div class="box f" style="margin:1.4mm 0"><h4>Percentage frequency</h4>
  percentage frequency =\\[\\small \\dfrac{{\\text{{number of times a value occurs}}}}{{\\text{{total number of values}}}}\\times100\\%\\]</div>
  <ol class="st"><li>One row per category, columns for number and %.</li><li>Count each category; add the total.</li>
  <li>Each % = count ÷ total × 100.</li><li>Check the % column adds to 100 <span class="mut">(99.9 or 100.1 is just rounding)</span>.</li></ol></div>
 <div class="box ex" style="flex:.9"><h4>Example 2</h4>
  11 preschool children chose chocolate (C) or vanilla (V):<br>C V V C C V C C C V V
  <table class="t" style="margin-top:1.4mm"><tr><th rowspan="2">Flavour</th><th colspan="2">Frequency</th></tr><tr><th>Number</th><th>Percentage</th></tr>
  <tr><td>Chocolate</td><td>6</td><td>54.5</td></tr><tr><td>Vanilla</td><td>5</td><td>45.5</td></tr><tr><td><b>Total</b></td><td>11</td><td>100.0</td></tr></table>
  <div class="small mut" style="margin-top:1mm">\\(\\tfrac{{6}}{{11}}\\times100\\%=54.5\\%\\)</div></div>
</div>
<div class="row">
 <div class="box" style="flex:1"><h4>Bar chart</h4>
  <ol class="st"><li>Frequency (or %) on the vertical axis.</li><li>One bar per category, <b>gaps</b> between bars, all the same width.</li>
  <li>Label both axes; use a ruler.</li><li>Ordinal data: keep the categories in order.</li></ol>
  <div class="box ex" style="margin-top:1.4mm"><h4>Example 3 · climate type of 23 countries</h4>
  <div class="row"><table class="t"><tr><th>Climate</th><th>No.</th><th>%</th></tr><tr><td>Cold</td><td>3</td><td>13.0</td></tr><tr><td>Mild</td><td>14</td><td>60.9</td></tr><tr><td>Hot</td><td>6</td><td>26.1</td></tr><tr><td><b>Total</b></td><td>23</td><td>100.0</td></tr></table>{bars()}</div>
  <span class="small">Climate type is <b>ordinal</b>: the groups have a natural order of 'warmth'.</span></div></div>
 <div class="box" style="flex:1"><h4>Percentage segmented bar chart</h4>
  One bar, 100% tall, split into one segment per category. Shows each category's <b>share of the whole</b> and makes groups easy to compare.
  <div class="box ex" style="margin-top:1.4mm"><h4>Example 4 · same data</h4>
  <div class="row">{seg()}<ol class="st small" style="flex:1"><li>Cold: 0 to 13%</li><li>Mild: 13 to 13 + 60.9 = 73.9%</li><li>Hot: 73.9 to 100%</li><li>Shade each segment; add a legend.</li></ol></div></div></div>
</div>
<div class="row">
 <div class="box" style="flex:1"><h4>Describing the distribution</h4>
  <b>Mode (modal category)</b> = the most common category: tallest bar or longest segment.
  <div class="rep" style="margin-top:1.2mm">The <span class="blank">variable</span> of <span class="blank">number</span> <span class="blank">individuals</span> were classified as <span class="blank">categories</span>. The majority / most <span class="blank">individuals</span>, <span class="blank">%</span>, were found to <span class="blank">modal category</span>. Of the remaining <span class="blank">individuals</span>, <span class="blank">%</span> were <span class="blank">category</span>, while <span class="blank">%</span> were <span class="blank">category</span>.</div>
  <div class="box tip" style="margin-top:1.4mm"><h4>Tip</h4>Say <b>'the majority'</b> only when the modal category is over 50%; otherwise say <b>'the most common'</b>. Always give the context and the %.</div></div>
 <div class="box ex" style="flex:1"><h4>Example 5 · report on climate types</h4>
  <div class="rep">The climate types of 23 countries were classified as being, ‘cold’, ‘mild’ or ‘hot’. The majority of the countries, 60.9%, were found to have a mild climate. Of the remaining countries, 26.1% were found to have a hot climate, while 13.0% were found to have a cold climate.</div></div>
</div>
<div class="box vc"><h4>VCAA 2017 Exam 1 Q5 <span class="pc">76% correct</span></h4>
 <div class="row"><img src="{IMG}" style="width:46%;align-self:center">
 <div style="flex:1">A study was conducted to investigate the association between the <i>number of moths</i> caught in a moth trap (less than 250, 250–500, more than 500) and the <i>trap type</i> (sugar, scent, light). The results are summarised in the percentaged segmented bar chart.<br>
 There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to
 <div class="mcq"><span><b>A.</b> 30</span><span><b>B.</b> 90</span><span><b>C.</b> 250</span><span><b>D.</b> 300</span><span><b>E.</b> 500</span></div>
 <div class="ans"><b>B</b>: the 'less than 250' segment for sugar reaches 30%, and 30% of 300 = 0.30 × 300 = 90.</div></div></div></div>
"""

def hist(v, start=0, w=1, xl='', yl='Frequency', ymax=None, ystep=5, W=230, H=140, col='#2f6fdf', axes=True, mw='22em', xlab=None):
    """Simple histogram SVG: bars touch; x ticks at the start of each interval."""
    ymax = ymax or max(v)
    x0, y0, x1 = (34 if axes else 4), H - (26 if axes else 4), W - 6
    bw, k = (x1 - x0) / len(v), (y0 - 10) / ymax
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mw}">']
    if axes:
        y = 0
        while y <= ymax + 1e-9:
            yy = y0 - y * k
            s.append(f'<line x1="{x0}" y1="{yy}" x2="{x1}" y2="{yy}" stroke="#e3e6ee"/><text x="{x0-4}" y="{yy+3}" font-size="9" text-anchor="end">{y:g}</text>')
            y += ystep
    for i, f in enumerate(v):
        if f: s.append(f'<rect x="{x0+i*bw:.1f}" y="{y0-f*k:.1f}" width="{bw:.1f}" height="{f*k:.1f}" fill="{col}" stroke="#fff" stroke-width=".8"/>')
    if axes:
        labs = xlab or [f'{start+i*w:g}' for i in range(len(v) + 1)]
        for i, t in enumerate(labs):
            s.append(f'<text x="{x0+i*bw:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle">{t}</text>')
        s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#1b1f2a" stroke-width="1.4"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="6" stroke="#1b1f2a" stroke-width="1.4"/>')
        s.append(f'<text x="{(x0+x1)/2}" y="{H-2}" font-size="9" font-weight="700" text-anchor="middle">{xl}</text>')
        s.append(f'<text x="10" y="{y0/2+6}" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 10 {y0/2+6})">{yl}</text>')
    else:
        s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#1b1f2a" stroke-width="1.2"/>')
    s.append('</svg>')
    return ''.join(s)

def mini(v, cap):
    return f'<div style="flex:1;text-align:center">{hist(v, axes=False, W=120, H=52, mw="100%")}<div class="small"><b>{cap[0]}</b><br><span class="mut">{cap[1]}</span></div></div>'

def dots():
    # Cambridge U3&4 Example 10: cricket team ages
    data = [22,19,18,19,23,25,22,29,18,22,23,24,22]
    W, y0 = 250, 62
    s = [f'<svg viewBox="0 0 {W} 86" width="100%" style="max-width:21em">']
    xs = lambda a: 12 + (a - 17) * 17.4
    for a in range(17, 31):
        s.append(f'<line x1="{xs(a)}" y1="{y0}" x2="{xs(a)}" y2="{y0+4}" stroke="#1b1f2a"/><text x="{xs(a)}" y="{y0+14}" font-size="8.5" text-anchor="middle">{a}</text>')
        for j in range(data.count(a)):
            s.append(f'<circle cx="{xs(a)}" cy="{y0-6-j*10}" r="4" fill="#2f6fdf"/>')
    s.append(f'<line x1="6" y1="{y0}" x2="{W-6}" y2="{y0}" stroke="#1b1f2a" stroke-width="1.4"/><text x="{W/2}" y="84" font-size="9" font-weight="700" text-anchor="middle">Age (years)</text></svg>')
    return ''.join(s)

def stem(rows, key, cap=''):
    r = ''.join(f'<tr><td class="st">{a}</td><td class="lv">{" ".join(b)}</td></tr>' for a, b in rows)
    return f'<table class="stem"><tr><td colspan="2" class="small"><b>{cap}</b> <span class="mut">Key: {key}</span></td></tr>{r}</table>'

C1 = f"""
<div class="row">
 <div class="box" style="flex:1"><h4>Frequency tables for numerical data</h4>
  <b>Discrete, few values:</b> one row for every value from the minimum to the maximum (like categorical data).<br>
  <b>Many values, or continuous:</b> group into intervals, a <b>grouped frequency table</b>.
  <ol class="st"><li>Every value fits in exactly one interval: no overlaps, no gaps.</li><li>About 5 to 15 intervals with easy widths (2, 5, 10, 100…).</li><li>Start each interval on an exact value: 0–49, 50–99.</li><li>Read <b>30–&lt;40</b> as 'at least 30 but less than 40'.</li></ol>
  <div class="box f" style="margin-top:1.2mm"><h4>Percentage frequency</h4>\\[\\small \\dfrac{{\\text{{frequency}}}}{{\\text{{total}}}}\\times100\\%\\]</div></div>
 <div class="box ex" style="flex:1.05"><h4>Examples 7 + 8 · average hours worked, 23 countries</h4>
  <div class="row"><table class="t sm"><tr><th>Hours</th><th>No.</th><th>%</th></tr><tr><td>30.0–34.9</td><td>1</td><td>4.3</td></tr><tr><td>35.0–39.9</td><td>6</td><td>26.1</td></tr><tr><td>40.0–44.9</td><td>8</td><td>34.8</td></tr><tr><td>45.0–49.9</td><td>5</td><td>21.7</td></tr><tr><td>50.0–54.9</td><td>3</td><td>13.0</td></tr><tr><td><b>Total</b></td><td>23</td><td>99.9</td></tr></table>
  {hist([1,6,8,5,3], start=30, w=5, xl='Average hours worked', ystep=2, W=200, H=130)}</div>
  <span class="small">Histogram: frequency up, variable across; one bar per interval; <b>bars touch</b>; mark the start of each interval. 99.9%: just rounding.</span></div>
</div>
<div class="row">
 <div class="box ex" style="flex:1"><h4>Example 6 · bedrooms in 24 properties sold</h4>
  2 3 4 3 3 4 3 4 4 1 3 2 1 2 2 2 4 5 3 4 4 5 3 4
  <div class="row" style="margin-top:1.2mm"><table class="t sm"><tr><th>Bedrooms</th><th>No.</th><th>%</th></tr><tr><td>1</td><td>2</td><td>8.3</td></tr><tr><td>2</td><td>5</td><td>20.8</td></tr><tr><td>3</td><td>7</td><td>29.2</td></tr><tr><td>4</td><td>8</td><td>33.3</td></tr><tr><td>5</td><td>2</td><td>8.3</td></tr><tr><td><b>Total</b></td><td>24</td><td>99.9</td></tr></table>
  <ol class="st small" style="flex:1"><li>Minimum 1, maximum 5: one row for every value 1 to 5.</li><li>Count each value; total 24.</li><li>\\(\\tfrac{{2}}{{24}}\\times100=8.3\\%\\)</li><li>Total 99.9%: rounding, that's fine.</li></ol></div></div>
 <div class="box tip" style="flex:.8"><h4>Writing a description</h4>Cover all four, in context, with numbers:<ol class="st"><li><b>Shape</b>: symmetric / positively or negatively skewed (name the tail).</li><li><b>Centre</b>: 'around …' with units.</li><li><b>Spread</b>: from min to max; where most values lie.</li><li><b>Outliers</b>: possible ones only, from a histogram.</li></ol></div>
</div>
<div class="box cas"><h4>CAS · histogram from raw data (e.g. bin width 4, starting at 2)</h4>
 <div class="row"><div style="flex:1"><b>TI-Nspire</b><ol class="st small"><li>Lists &amp; Spreadsheet: name column A (e.g. <i>marks</i>), enter the data.</li><li>Add Data &amp; Statistics; put <i>marks</i> on the x-axis.</li><li>Menu › Plot Type › Histogram.</li><li>Menu › Plot Properties › Histogram Properties › Bin Settings › Equal Bin Width: width 4, alignment 2.</li><li>Window/Zoom › Zoom-Data. Hover to read a bar.</li></ol></div>
 <div style="flex:1"><b>ClassPad</b><ol class="st small"><li>Statistics app: name list1 <i>marks</i>, enter the data.</li><li>SetGraph › Setting: Draw On, Type Histogram, XList main\\marks, Freq 1. Set.</li><li>Tap the graph icon.</li><li>Set Interval: HStart 2, HStep 4. OK.</li><li>Analysis › Trace to read each bar.</li></ol></div></div></div>
<div class="box"><h4>Describing a distribution: shape, centre, spread, outliers</h4>
 <div class="row" style="gap:3mm">{mini([1,3,6,9,6,3,1],('Symmetric','even tails either side'))}{mini([3,9,7,4,2,1,1],('Positively skewed','long tail to the right'))}{mini([1,1,2,4,7,9,3],('Negatively skewed','long tail to the left'))}{mini([2,7,4,1,4,7,2],('Bimodal','two peaks: two groups?'))}</div>
 <div class="row small" style="margin-top:1mm"><div style="flex:1"><b>Centre:</b> the middle value, where the area splits in half.</div><div style="flex:1"><b>Spread:</b> narrow peak = tightly clustered; broad = widely spread.</div><div style="flex:1"><b>Outliers:</b> values that stand out from the main body. Check them.</div></div>
 <div class="box tip" style="margin-top:1.2mm"><h4>Tip</h4>The <b>tail</b> names the skew. From a histogram you can only <b>estimate</b> the centre and spread and flag <b>possible</b> outliers.</div></div>
<div class="box ex"><h4>Example 9 · gestation period of 1000 babies</h4>
 <div class="row"><div style="flex:1">{hist([2,2,2,2,2,2,2,4,6,10,16,34,95,233,302,207,86,4], start=25, xl='Gestation period (weeks)', ymax=300, ystep=100, W=290, H=130, mw='100%', xlab=[str(25+i) if i%2==0 else '' for i in range(19)])}</div>
 <div class="rep" style="flex:1">The distribution is clearly negatively skewed, with a long lower tail. The centre of the distribution is around 38-39 weeks. The data values range from 25-42 weeks, but most of the data values are close to the centre, in the range of 36-41 weeks. Those values which are less than 34 weeks seem to be small in comparison to the rest of the data, but which values are outliers cannot be determined from the histogram.</div></div></div>
"""

IMG2='data:image/png;base64,'+_b.b64encode(open(_o.path.join(_o.path.dirname(__file__),'vcaa2020e2_q2a.png'),'rb').read()).decode()

D1 = f"""
<div class="row">
 <div class="box" style="flex:1"><h4>Dot plot</h4>A number line with a dot for each value; equal values stack. Best for <b>small, discrete</b> data sets.
  <div class="box ex" style="margin-top:1.2mm"><h4>Example 10 · ages of a cricket team</h4>22 19 18 19 23 25 22 29 18 22 23 24 22{dots()}</div></div>
 <div class="box" style="flex:1"><h4>Stem plot</h4>Each value splits into a <b>stem</b> (leading digits) and a <b>leaf</b> (last digit).
  <div class="small" style="margin-top:.6mm">Add a key and the variable name · leaves in order · include empty stems · bunched? split each stem in two (leaves 0–4, 5–9).</div>
  <div class="box ex" style="margin-top:1.2mm"><h4>Example 11 · university participation (%)</h4>
  <div class="row"><span class="small" style="flex:1">26 3 12 20 36 1 25 26 13 9 26 27 15 21 7 8 22 3 37 17 55 30 1</span>
  {stem([('0','1 1 3 3 7 8 9'.split()),('1','2 3 5 7'.split()),('2','0 1 2 5 6 6 6 7'.split()),('3','0 6 7'.split()),('4',[]),('5',['5'])],'1|2 = 12','rate (%)')}</div></div></div>
</div>
<div class="row">
 <div class="box vc" style="flex:1"><h4>VCAA 2020 Exam 2 Q2a <span class="pc">93% correct</span></h4>
  <div class="row"><img src="{IMG2}" style="width:23mm;align-self:center"><div style="flex:1">The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.<br>Write down the modal <i>neck size</i>, in centimetres, for these 250 men. <span class="mut">(1 mark)</span>
  <div class="ans" style="margin-top:1.2mm"><b>38 cm</b>: the tallest column of dots.</div></div></div></div>
 <div class="box vc" style="flex:1.1"><h4>VCAA 2016 Exam 1 Q3 <span class="pc">87% correct</span></h4>
  <div class="row"><div style="flex:1">The following stem plot displays 30 temperatures recorded at a weather station.<br>The modal temperature is
  <div class="mcq" style="flex-wrap:wrap;gap:0 3mm"><span><b>A.</b> 2.8 °C</span><span><b>B.</b> 2.9 °C</span><span><b>C.</b> 3.7 °C</span><span><b>D.</b> 8.0 °C</span><span><b>E.</b> 9.0 °C</span></div></div>
  {stem([('2','2 4 4'.split()),('2','5 7 8 8 8 8 8 8 9 9 9 9'.split()),('3','1 2 3 3 4 4 4'.split()),('3','5 6 7 7 7 7'.split()),('4',['1'])],'2|2 = 2.2 °C','temperature')}</div>
  <div class="ans" style="margin-top:1mm"><b>A</b>: leaf 8 appears six times on a 2 stem: 2.8 °C.</div></div>
</div>
"""

E1 = f"""
<div class="row">
 <div class="box" style="flex:1.2"><h4>Logs are powers of 10</h4>
  <table class="t sm" style="width:100%"><tr><th>number</th><td>0.01</td><td>0.1</td><td>1</td><td>10</td><td>100</td><td>1000</td><td>1 000 000</td></tr><tr><th>power of 10</th><td>10<sup>−2</sup></td><td>10<sup>−1</sup></td><td>10<sup>0</sup></td><td>10<sup>1</sup></td><td>10<sup>2</sup></td><td>10<sup>3</sup></td><td>10<sup>6</sup></td></tr><tr><th>log</th><td>−2</td><td>−1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>6</td></tr></table>
  <div class="box f" style="margin-top:1.2mm"><h4>Log and its inverse</h4>\\[\\small \\log_{{10}}x=b \\iff x=10^{{b}}\\]</div>
  <span class="small">number &gt; 1 → log positive · = 1 → log 0 · between 0 and 1 → log negative · 0 or negative → undefined</span></div>
 <div class="box" style="flex:1"><h4>Why a log scale?</h4>Use it when data range over several <b>orders of magnitude</b>: values spread evenly instead of bunching at 0. A positively skewed histogram often becomes <b>symmetric</b>.
  <div class="box cas" style="margin-top:1.2mm"><h4>CAS</h4>Log: type <b>log(45)</b> → 1.65… <br>Undo a log: type <b>10^2.7125</b> → 515.82…</div></div>
</div>
<div class="row">
 <div class="box ex" style="flex:1"><h4>Example 13 · weights of 27 animals</h4>
  <div class="row">{hist([3.7,7.4,18.5,25.9,25.9,11.1,7.4], start=-2, xl='log(body weight)', yl='Percentage', ymax=28, ystep=7, W=200, H=125, mw='48mm')}
  <ol class="st small" style="flex:1"><li>4 on the scale: 10<sup>4</sup> = 10 000 kg</li><li>log 3.3 = 0.518… = 0.52</li><li>log = 3.4: 10<sup>3.4</sup> = 2511.88… ≈ 2512 kg</li></ol></div></div>
 <div class="box vc" style="flex:1.15"><h4>VCAA 2019 Exam 1 Q3 <span class="pc">71% correct</span></h4>
  <div class="row"><div style="flex:1">The following histogram shows the <i>population size</i> for 48 countries plotted on a log<sub>10</sub> scale.<br>Based on this histogram, the number of countries with a <i>population size</i> that is less than 100 000 people is
  <div class="mcq"><span><b>A.</b> 1</span><span><b>B.</b> 5</span><span><b>C.</b> 7</span><span><b>D.</b> 8</span><span><b>E.</b> 48</span></div></div>
  <div style="flex:1">{hist([0,0,1,0,7,5,21,13,1,0], xl='log₁₀(population size)', ymax=25, ystep=5, W=170, H=120, mw='100%')}</div></div>
  <div class="ans" style="margin-top:1mm"><b>D</b>: 100 000 = 10<sup>5</sup>, so 5 on the scale. Bars below 5: 1 + 7 = 8.</div></div>
</div>
"""

MAM = [('okapi','250'),('gorilla','210'),('pig','190'),('Brazilian tapir','160'),('jaguar','100'),('grey seal','85'),('giant armadillo','60'),('sheep','56'),('chimpanzee','52'),('kangaroo','35'),('goat','28'),('roedeer','15'),('baboon','11'),('rhesus monkey','6.8'),('raccoon','4.3'),('red fox','4.2'),('cat','3.3'),('echidna','3.0'),('rabbit','2.5')]
def mamtab():
    h = lambda r: '<tr><th>Mammal</th>' + ''.join(f'<td>{m}</td>' for m, _ in r) + '</tr><tr><th>Body weight (kg)</th>' + ''.join(f'<td>{w}</td>' for _, w in r) + '</tr>'
    return f'<table class="t sm" style="width:100%;margin:1mm 0">{h(MAM[:10])}</table><table class="t sm" style="width:100%;margin-bottom:1mm">{h(MAM[10:])}</table>'

F1 = f"""
<div class="row">
 <div class="box" style="flex:1"><h4>Two questions about any distribution</h4>
  <table class="t" style="width:100%"><tr><th></th><th>Centre</th><th>Spread</th></tr>
  <tr><td>skewed or outliers</td><td><b>median</b> M: the middle value</td><td><b>IQR</b>: spread of the middle 50%</td></tr>
  <tr><td>symmetric, no outliers</td><td><b>mean</b> \\(\\bar x\\): the balance point</td><td><b>standard deviation</b> s: spread around the mean</td></tr></table>
  <div class="small" style="margin-top:1mm">They come in pairs: median with IQR, mean with standard deviation. <b>Range</b> = largest − smallest (uses only two values).</div>
  <div class="box tip" style="margin-top:1.2mm"><h4>Mean or median?</h4>The mean and the median are both measures of the centre of a distribution. If the distribution is <b>symmetric and there are no outliers</b>, either the mean or the median can be used to indicate the centre of the distribution. If it is <b>clearly skewed and/or there are outliers</b>, it is more appropriate to use the median. <span class="mut">The median is <b>resistant</b>: changing the largest value moves the mean but not the median.</span></div></div>
 <div class="box f" style="flex:.8"><h4>Key formulas</h4>
  <b>Median</b> at position <span class="inl">\\(\\tfrac{{n+1}}{{2}}\\)</span> in the <b>ordered</b> data <span class="small mut">(n odd: middle value; n even: average of the two middle values)</span>
  <div style="margin-top:1.2mm"><b>Q<sub>1</sub></b> = median of the lower half · <b>Q<sub>3</sub></b> = median of the upper half <span class="small mut">(n odd: leave the median out of both halves)</span></div>
  \\[\\text{{IQR}}=Q_3-Q_1 \\qquad R=\\text{{largest}}-\\text{{smallest}}\\]
  \\[\\bar x=\\dfrac{{\\sum x}}{{n}} \\qquad s=\\sqrt{{\\dfrac{{\\sum (x-\\bar x)^2}}{{n-1}}}}\\]
  <span class="small">s is roughly the typical distance of the values from the mean.</span></div>
</div>
<div class="row">
 <div class="box ex" style="flex:1"><h4>Example 14 · median</h4>
  <b>a</b> 2 9 1 8 3 5 3 8 1 → 1 1 2 3 <b>3</b> 5 8 8 9<br><span class="small">n = 9: \\(\\tfrac{{9+1}}{{2}}\\) = 5th value, M = <b>3</b></span><br>
  <b>b</b> 10 1 3 4 8 6 10 1 2 9 → 1 1 2 3 <b>4 6</b> 8 9 10 10<br><span class="small">n = 10: average of 5th and 6th, M = \\(\\tfrac{{4+6}}{{2}}\\) = <b>5</b></span></div>
 <div class="box ex" style="flex:1.25"><h4>Example 18 · IQR, n even (18 cats)</h4>
  <div class="row">{stem([('1',['9']),('2','1 3 5 8'.split()),('3','0 0 4 9 9'.split()),('4','0 4 5 8'.split()),('5','0 3'.split()),('6','3 4'.split())],'1|2 = 1.2 kg','Weight (kg)')}
  <div class="small" style="flex:1">9 values in each half.<br>Lower: 1.9 2.1 2.3 2.5 <b>2.8</b> 3.0 3.0 3.4 3.9 → Q<sub>1</sub> = 2.8<br>Upper: 3.9 4.0 4.4 4.5 <b>4.8</b> 5.0 5.3 6.3 6.4 → Q<sub>3</sub> = 4.8<br>IQR = 4.8 − 2.8 = <b>2.0</b></div></div></div>
 <div class="box ex" style="flex:.85"><h4>Example 21 · mean</h4>
  38 36 35 43 46 64 48 25 <span class="mut">(ms)</span><br>n = 8, \\(\\sum x\\) = 335<br>\\(\\bar x=\\tfrac{{335}}{{8}}=41.875\\) → <b>41.9</b></div>
</div>
<div class="box cas"><h4>CAS · mean, standard deviation and five-number summary (one-variable statistics)</h4>
 <div class="row"><div style="flex:1"><b>TI-Nspire</b><ol class="st small"><li>Lists &amp; Spreadsheet: name a list (e.g. <i>height</i>), enter the data.</li><li>Add Calculator › Menu › Statistics › Stat Calculations › One-Variable Statistics.</li><li>X1 List: <i>height</i>. OK.</li><li>Read \\(\\bar x\\), <b>sx</b>, n, MinX, Q₁X, MedianX, Q₃X, MaxX.</li></ol></div>
 <div style="flex:1"><b>ClassPad</b><ol class="st small"><li>Statistics app: name a list (e.g. <i>height</i>), enter the data.</li><li>Calc › One-Variable; XList: main\\height, Freq: 1.</li><li>Read \\(\\bar x\\), <b>sx</b>, n; scroll for minX, Q₁, Med, Q₃, maxX.</li></ol></div>
 <div style="flex:.8"><b>Frequency table?</b><div class="small">Values in one list, frequencies in another; set the Frequency List (TI) or Freq (ClassPad) to it. Check that n = total frequency.</div>
 <div class="ans small" style="margin-top:1mm">Use <b>sx</b>, not σx: General Maths always uses the sample standard deviation.</div></div></div>
</div>
<div class="row">
 <div class="box vc" style="flex:1"><h4>VCAA 2017 Exam 2 Q1ai <span class="pc">87% correct</span></h4>
  The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.
  <table class="t sm" style="margin:1mm 0"><tr><th>number of eggs</th><td>172</td><td>192</td><td>159</td><td>125</td><td>197</td><td>135</td><td>140</td><td>140</td><td>138</td><td>166</td><td>136</td><td>131</td></tr></table>
  From the information given, determine the range. <span class="mut">(1 mark)</span>
  <div class="ans" style="margin-top:1mm"><b>72 eggs</b>: 197 − 125 = 72.</div></div>
</div>
<div class="box vc"><h4>VCAA 2026 NHT Exam 2 Q1b, d <span class="pc">NHT report: answers only</span></h4>
 The table below displays the typical body weight, in kilograms, for a sample of 19 different mammals.{mamtab()}
 <div class="row"><div style="flex:1"><b>b.</b> Complete the five-number summary in the table below for the variable <i>body weight</i>, in kilograms, by writing in the values for the minimum and the median. <span class="mut">(2 marks)</span>
 <table class="t sm" style="margin-top:1mm"><tr><th>Minimum</th><th>Q<sub>1</sub></th><th>Median</th><th>Q<sub>3</sub></th><th>Maximum</th></tr><tr><td></td><td>4.3</td><td></td><td>100</td><td>250</td></tr></table></div>
 <div style="flex:1"><b>d.</b> The mean body weight is 67 kg, rounded to the nearest whole number.<br>Explain why the median is a better measure of the centre of the body weight data than the mean. <span class="mut">(1 mark)</span></div></div>
 <div class="ans" style="margin-top:1mm"><b>b</b> Minimum = <b>2.5</b>; n = 19, median = 10th value = <b>35</b>. &nbsp; <b>d</b> The data is positively skewed (and/or has outliers), so the mean is pulled above most values; the median is not affected.</div></div>
"""

def box(lo, hi, lw, q1, m, q3, uw, out=(), step=None, lab=None, xl='', W=300, H=58, fences=(), bands=False, mw='100%', col='#cfe0fb', axis=True):
    """Horizontal boxplot SVG on a scaled axis; fences = [(x, label)]."""
    x0, x1, yb, bh, ya = 12, W - 12, 22, 16, H - (22 if xl else 12)
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mw}">']
    for fx, ft in fences:
        s.append(f'<line x1="{X(fx):.1f}" y1="10" x2="{X(fx):.1f}" y2="{ya}" stroke="#d2475b" stroke-dasharray="3 2"/><text x="{X(fx):.1f}" y="8" font-size="7.5" fill="#d2475b" text-anchor="middle">{ft}</text>')
    if bands:
        for a, b in [(lw, q1), (q1, m), (m, q3), (q3, uw)]:
            s.append(f'<text x="{(X(a)+X(b))/2:.1f}" y="{yb-bh/2-3}" font-size="7.5" fill="#6b7280" text-anchor="middle">25%</text>')
    yc = yb + bh / 2
    s.append(f'<line x1="{X(lw):.1f}" y1="{yc}" x2="{X(q1):.1f}" y2="{yc}" stroke="#1b1f2a" stroke-width="1.2"/><line x1="{X(q3):.1f}" y1="{yc}" x2="{X(uw):.1f}" y2="{yc}" stroke="#1b1f2a" stroke-width="1.2"/>')
    s.append(f'<rect x="{X(q1):.1f}" y="{yb}" width="{X(q3)-X(q1):.1f}" height="{bh}" fill="{col}" stroke="#1b1f2a" stroke-width="1.2"/><line x1="{X(m):.1f}" y1="{yb}" x2="{X(m):.1f}" y2="{yb+bh}" stroke="#d2475b" stroke-width="2"/>')
    for o in out:
        s.append(f'<circle cx="{X(o):.1f}" cy="{yc}" r="2.6" fill="#fff" stroke="#1b1f2a" stroke-width="1.1"/>')
    if axis: s.append(f'<line x1="{x0}" y1="{ya}" x2="{x1}" y2="{ya}" stroke="#1b1f2a" stroke-width="1.2"/>')
    if step:
        v = lo
        while v <= hi + 1e-9:
            big = lab and abs((v - lo) / lab - round((v - lo) / lab)) < 1e-6
            s.append(f'<line x1="{X(v):.1f}" y1="{ya}" x2="{X(v):.1f}" y2="{ya+(4 if big else 2.5)}" stroke="#1b1f2a" stroke-width=".8"/>')
            if big: s.append(f'<text x="{X(v):.1f}" y="{ya+11}" font-size="8" text-anchor="middle">{v:g}</text>')
            v += step
    if xl: s.append(f'<text x="{W/2}" y="{H-1}" font-size="8.5" font-weight="700" text-anchor="middle">{xl}</text>')
    s.append('</svg>')
    return ''.join(s)

def sbox(lw, q1, m, q3, uw, out, cap):
    return f'<div style="flex:1;text-align:center">{box(0, 20, lw, q1, m, q3, uw, out, W=120, H=44, axis=False)}<div class="small"><b>{cap[0]}</b><br><span class="mut">{cap[1]}</span></div></div>'

HEP = [('1','1.76','15.34','41.22'),('2','1.79','16.96','42.41'),('3','1.83','13.87','46.53'),('4','1.82','14.23','40.53'),('5','1.87','13.78','40.62'),('6','1.73','14.50','45.62'),('7','1.68','15.08','42.33'),('8','1.82','13.13','40.88'),('9','1.83','14.22','39.22'),('10','1.87','13.62','42.51'),('11','1.87','12.01','42.75'),('12','1.80','12.88','38.12'),('13','1.83','12.68','42.65'),('14','1.87','12.45','41.32'),('15','1.78','11.31','42.88')]
def heptab():
    rows = [('athlete number', 0), ('high jump (metres)', 1), ('shot-put (metres)', 2), ('javelin (metres)', 3)]
    return '<table class="t sm" style="width:100%;margin:1mm 0">' + ''.join(f'<tr><th>{n}</th>' + ''.join(f'<td>{r[i]}</td>' for r in HEP) + '</tr>' for n, i in rows) + '</table>'

G1 = f"""
<div class="row">
 <div class="box" style="flex:1"><h4>Five-number summary and boxplot</h4>
  <b>Five-number summary:</b> minimum, Q<sub>1</sub>, median, Q<sub>3</sub>, maximum.<br>
  <b>Boxplot:</b> a picture of it. The box runs Q<sub>1</sub> to Q<sub>3</sub> (the middle 50%) with a line at the median; the <b>whiskers</b> run to the smallest and largest values that are <b>not outliers</b>.
  {box(0, 100, 12, 35, 50, 62, 95, step=5, lab=10, bands=True, H=50)}
  <span class="small">Each of the four sections holds about <b>25%</b> of the data, however long it looks: a long whisker means spread out, not more values.</span></div>
 <div class="box f" style="flex:.9"><h4>Key formulas</h4>
  \\[\\text{{IQR}}=Q_3-Q_1 \\qquad \\text{{range}}=\\max-\\min\\]
  \\[\\text{{LF}}=Q_1-1.5\\times\\text{{IQR}} \\qquad \\text{{UF}}=Q_3+1.5\\times\\text{{IQR}}\\]
  <b>Outlier:</b> x &lt; LF → outlier · x &gt; UF → outlier. Drawn as a dot; the whisker stops at the last value inside the fence.
  <div class="box ex" style="margin-top:1.2mm"><h4>CAS 4 · 19 marks</h4>Q<sub>1</sub> = 23, Q<sub>3</sub> = 35, IQR = 12<br>LF = 23 − 1.5 × 12 = 5 · UF = 35 + 1.5 × 12 = 53<br>3 &lt; 5 = LF → <b>3 is an outlier</b>; lower whisker stops at 21.
  {box(0, 55, 21, 23, 30, 35, 48, [3], step=1, lab=5, fences=[(5, 'LF = 5'), (53, 'UF = 53')], H=54)}</div></div>
</div>
<div class="box cas"><h4>CAS · boxplot with outliers (then read the five numbers with trace)</h4>
 <div class="row"><div style="flex:1"><b>TI-Nspire</b><ol class="st small"><li>Lists &amp; Spreadsheet: name a list (e.g. <i>marks</i>), enter the data.</li><li>Add Data &amp; Statistics; x-axis → <i>marks</i>.</li><li>Menu › Plot Type › Box Plot (outliers shown as dots).</li><li>Menu › Analyze › Graph Trace to read the values.</li></ol></div>
 <div style="flex:1"><b>ClassPad</b><ol class="st small"><li>Statistics app: name a list (e.g. <i>marks</i>), enter the data.</li><li>SetGraph: Draw On · Type MedBox · XList main\\marks · Freq 1.</li><li>Tick <b>Show Outliers</b>; Set; plot.</li><li>Tap Trace; move with the cursor arrows.</li></ol></div></div></div>
<div class="row">
 <div class="box ex" style="flex:1"><h4>Example 22 · boxplot from a five-number summary</h4>
  Life expectancy (years), 23 countries: <b>52, 66, 73, 75, 77</b>
  {box(50, 80, 52, 66, 73, 75, 77, step=1, lab=5, xl='Life expectancy (years)', H=56)}
  <span class="small">1 Scaled, labelled axis · 2 box Q<sub>1</sub> to Q<sub>3</sub> · 3 median line · 4 whiskers to min and max.</span></div>
 <div class="box ex" style="flex:1"><h4>Examples 23 + 24 · reading a boxplot</h4>
  {box(0, 100, 10, 30, 36, 44, 60, [4, 70, 84, 92], step=2, lab=10, fences=[(9, 'LF = 9'), (65, 'UF = 65')], H=50)}
  <span class="small">M = 36 · Q<sub>1</sub> = 30 · Q<sub>3</sub> = 44 · IQR = 14 · min 4, max 92 · outliers 4, 70, 84, 92.<br>
  <b>Percentages:</b> below Q<sub>1</sub> 25% · below M 50% · below Q<sub>3</sub> 75% · Q<sub>1</sub> to Q<sub>3</sub> 50% · Q<sub>1</sub> to max 75%.</span></div>
</div>
<div class="box"><h4>Shape from a boxplot: where is the median in the box, and which whisker is longer?</h4>
 <div class="row" style="gap:3mm">{sbox(2,7,10,13,18,[],('Symmetric','median central, equal whiskers'))}{sbox(2,4,6,10,18,[],('Positively skewed','median left, long right whisker'))}{sbox(2,10,14,16,18,[],('Negatively skewed','median right, long left whisker'))}{sbox(6,8,9,10,12,[1,18],('With outliers','dots past the whiskers'))}</div>
 <div class="row" style="margin-top:1mm"><div class="box tip" style="flex:1"><h4>Describe in this order</h4>Shape (and outliers) · centre (the median) · spread (IQR and range) · outliers by value.</div>
 <div class="rep" style="flex:2"><b>Example 26:</b> The distribution is symmetric but with outliers. The distribution is centred at 41, the median value. The spread of the distribution, as measured by the IQR, is 5.5 and, as measured by the range, 37. There are four outliers: 10, 15, 20 and 25.</div></div></div>
<div class="row">
 <div class="box vc" style="flex:1"><h4>VCAA 2020 Exam 2 Q2c <span class="pc">55% correct</span></h4>
  <div class="row"><div style="flex:1">The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.
  <table class="t sm" style="margin:1mm 0"><tr><th>minimum</th><th>first quartile (Q<sub>1</sub>)</th><th>median</th><th>third quartile (Q<sub>3</sub>)</th><th>maximum</th></tr><tr><td>31</td><td>36</td><td>38</td><td>39</td><td>44</td></tr></table>
  Use the five-number summary to construct a boxplot, showing any outliers if appropriate. <span class="mut">(2 marks)</span></div>
  <div class="ans" style="flex:1">IQR = 39 − 36 = 3 · LF = 36 − 1.5 × 3 = 31.5 · UF = 39 + 1.5 × 3 = 43.5<br>31 &lt; 31.5 = LF and 44 &gt; 43.5 = UF → <b>31 and 44 are outliers</b>; whiskers to 32 and 43.
  {box(30, 45, 32, 36, 38, 39, 43, [31, 44], step=1, lab=1, fences=[(31.5, 'LF = 31.5'), (43.5, 'UF = 43.5')], xl='neck size (cm)', H=60)}</div></div></div>
</div>
"""

CARDS = {
 '1A': dict(size='half', title='Types of data', sd='Study Design: types of data', body=A1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1A. Example: Cambridge U3&amp;4 Example 1.'),
 '1B': dict(size='full', title='Displaying and describing categorical data',
            sd='Study Design: display and description of categorical variables; using distributions to answer statistical questions', body=B1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1B. Examples: Cambridge U3&amp;4 Examples 2–5 (Example 5 report verbatim).'),

 '1C': dict(size='full', title='Displaying and describing numerical data',
            sd='Study Design: representation, display and description of the distributions of numerical variables: histograms; use of distributions to answer statistical questions', body=C1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1C. Examples: Cambridge U3&amp;4 Examples 6–9 (Example 9 report verbatim; histograms redrawn).'),
 '1D': dict(size='half', title='Dot plots and stem plots',
            sd='Study Design: representation, display and description of the distributions of numerical variables: dot plots, stem plots', body=D1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1D. Examples: Cambridge U3&amp;4 Examples 10–11.'),
 '1E': dict(size='half', title='Logarithmic scales',
            sd='Study Design: the use of a logarithmic (base 10) scale to display data ranging over several orders of magnitude and their interpretation in terms of powers of ten', body=E1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1E. Example: Cambridge U3&amp;4 Example 13 (histogram redrawn).'),

 '1F': dict(size='full', title='Measures of centre and spread',
            sd='Study Design: summary of the distributions of numerical variables; the sample mean and standard deviation and their use in comparing data distributions in terms of centre and spread', body=F1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1F ("Mean or median?" box verbatim, p. 52). Examples: Cambridge U3&amp;4 Examples 14, 18, 21.'),

 '1G': dict(size='full', title='The five-number summary and the boxplot',
            sd='Study Design: the five-number summary and boxplots (including the use of the lower fence (Q1 – 1.5 × IQR) and upper fence (Q3 + 1.5 × IQR) to identify and display possible outliers)', body=G1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1G. Examples: Cambridge U3&amp;4 Examples 22–24, 26 (Example 26 description verbatim) and CAS 4; boxplots redrawn.'),
}

LESSONS = {'1A-1B': ['1A', '1B'], '1C-1E': ['1C', '1D', '1E']}
