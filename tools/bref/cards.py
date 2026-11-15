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

CARDS = {
 '1A': dict(size='half', title='Types of data', sd='Study Design: types of data', body=A1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1A. Example: Cambridge U3&amp;4 Example 1.'),
 '1B': dict(size='full', title='Displaying and describing categorical data',
            sd='Study Design: display and description of categorical variables; using distributions to answer statistical questions', body=B1,
            cite='Notes: own words, from Cambridge General Mathematics Units 3&amp;4, 1B. Examples: Cambridge U3&amp;4 Examples 2–5 (Example 5 report verbatim).'),
}

LESSONS = {'1A-1B': ['1A', '1B']}
