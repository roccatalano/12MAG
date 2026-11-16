"""Lesson 2 (1C-1E) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py; model tools/deck/s1/worksheet.py).
Questions verbatim from tools/deck/s2/build.py (which copied them from the sources, checked 15 Nov).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
  APK 1 = Cambridge U1&2 Ch 2 skills checklist 2C #6 + 2D #7 · APK 2 = Edrolo U1&2 1C Q17 (adapted from VCAA 2016 E2 Q1d) · APK 3 = Cambridge U1&2 2D #9
  APK 4 = Edrolo U1&2 1C Q15 (adapted from VCAA 2017 E2 Q2b) · APK 5 = Cambridge U1&2 Ch 9 skills checklist 9D #6, #7
  Examples 6-13 = Cambridge U3&4 Examples 6-13 · You trys = Edrolo U3&4 1C WE4, WE5, WE1, WE2, 1D WE1, WE3 (none for Examples 6 and 9)
  Exits = Edrolo U3&4 1C Q16 (VCAA 2020 E2 Q2a), 1C Q18 (VCAA 2016 E1 Q3), 1D Q13 (VCAA 2019 E1 Q3).
No CAS steps, no key ideas (they live in the bound reference). Run: python3 tools/deck/s2/worksheet.py"""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *

# ---------------------------------------------------------------- local figures (static SVG; ws2 has bar/segment charts only)
def _yl(o, T, y0, yl):
    if yl: o.append(f'<text x="9" y="{(T+y0)/2}" font-size="9" text-anchor="middle" transform="rotate(-90 9 {(T+y0)/2})">{yl}</text>')
def hist(start, w, v, ymax, ystep, xl, yl='frequency', draw=True, W=280, H=140, mm=70, lab=1, dec=None, pct=False):
    """Histogram on a grid. draw=True: black bars (given). draw=False: empty grid for students; bars in red on the solutions copy.
    draw=None: grid only (no answer)."""
    L, R, T, B = 34, 8, 8, 30; n = len(v); bw = (W - L - R) / n; k = (H - T - B) / ymax; y0 = H - B; o = []; y = 0
    while y <= ymax + 1e-9:
        yy = y0 - y * k
        o.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{W-R}" y2="{yy:.1f}" stroke="#ccc" stroke-width=".5"/><text x="{L-4}" y="{yy+3:.1f}" font-size="8.5" text-anchor="end">{y:g}{"%" if pct else ""}</text>')
        y += ystep
    for i in range(n + 1):
        if i % lab == 0:
            t = start + i * w; t = f'{t:.{dec}f}' if dec is not None else f'{t:g}'
            o.append(f'<text x="{L+i*bw:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle">{t.replace("-", "−")}</text>')
    if draw is not None:
        c = '#000' if draw else RED
        o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(f'<rect x="{L+i*bw:.1f}" y="{y0-f*k:.1f}" width="{bw:.1f}" height="{f*k:.1f}" fill="{"#d9d9d9" if draw else "none"}" stroke="{c}"/>' for i, f in enumerate(v) if f) + '</g>')
    o.append(f'<line x1="{L}" y1="{y0}" x2="{W-R}" y2="{y0}" stroke="#000"/><line x1="{L}" y1="{y0}" x2="{L}" y2="{T-2}" stroke="#000"/>')
    if xl: o.append(f'<text x="{(L+W-R)/2}" y="{H-3}" font-size="9" text-anchor="middle">{xl}</text>')
    _yl(o, T, y0, yl)
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{"".join(o)}</svg>'
def dotplot(mn, mx, vals, xl, draw=True, step=1, lab=1, r=3.6, W=280, mm=70, rows=None):
    """Dot plot. draw=False: number line only for students; dots in red on the solutions copy."""
    L, R = 14, 14; s = lambda x: L + (x - mn) / (mx - mn) * (W - L - R); c = Counter(vals); dy = 2 * r * .95
    top = (rows or max(c.values())) * dy + 6; y = top; o = [f'<line x1="{L-6}" y1="{y}" x2="{W-R+6}" y2="{y}" stroke="#000"/>']
    i = 0
    while mn + i * step <= mx + 1e-9:
        t = mn + i * step; big = i % lab == 0
        o.append(f'<line x1="{s(t):.1f}" y1="{y}" x2="{s(t):.1f}" y2="{y+(4 if big else 2.5)}" stroke="#000" stroke-width=".8"/>')
        if big: o.append(f'<text x="{s(t):.1f}" y="{y+13}" font-size="8.5" text-anchor="middle">{t:g}</text>')
        i += 1
    col = '#000' if draw else RED
    o.append(f'<g{"" if draw else " class=solfig"}>' + ''.join(f'<circle cx="{s(x):.1f}" cy="{y-r-1-j*dy:.1f}" r="{r}" fill="{"#555" if draw else "none"}" stroke="{col}" stroke-width=".7"/>' for x, f in c.items() for j in range(f)) + '</g>')
    o.append(f'<text x="{W/2}" y="{y+25}" font-size="9" text-anchor="middle" font-style="italic">{xl}</text>')
    return f'<svg viewBox="0 0 {W} {y+29}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{"".join(o)}</svg>'
def stem(rows, key, cap='', blank=False):
    """Stem plot. blank=True: stems printed, leaves empty for students and red on the solutions copy."""
    lv = lambda b: f'<span class="a">{" ".join(map(str, b))}</span>' if blank else ' '.join(map(str, b))
    r = ''.join(f'<tr><td class="st">{a}</td><td class="lv">{lv(b)}</td></tr>' for a, b in rows)
    return f'<div class="stemw"><div class="stemk">{cap}{" &nbsp; " if cap else ""}{key}</div><table class="stem{" sf" if blank else ""}">{r}</table></div>'
CSS = ('<style>.stemw{display:inline-block;margin:1mm auto;text-align:left}.stemk{font-size:8.5pt;margin-bottom:.5mm}'
       'table.stem{border-collapse:collapse;font-family:"Courier New",monospace;font-size:10pt}table.stem td{padding:.2mm 2mm}table.stem td.st{border-right:1.4px solid #000;text-align:right;font-weight:bold}'
       'table.stem td.lv{min-width:40mm;letter-spacing:.5px}table.stem.sf td{height:6.4mm}table.stem.sf td.lv{border-bottom:1px dotted #bbb}'
       '.stem .a{color:#c00;visibility:hidden}.sol .stem .a{visibility:visible}.cen{text-align:center}</style>')
def cen(x): return f'<div class="cen">{x}</div>'
def side(left, fig, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{fig}</div></div>'
def ftab2(var, rows, total, blank=True, numh='Number', pcth='Percentage'):
    """Frequency table, Cambridge layout. blank=True: the whole body is red/blank (students fill every cell, incl. the values column)."""
    f = a if blank else (lambda x: x)
    return table([[var, numh, pcth]] + [[f(r[0]), f(r[1]), f(r[2])] for r in rows] + [['<b>Total</b>' if numh == 'Number' else '<b>total</b>', f(f'<b>{total[0]}</b>'), f(f'<b>{total[1]}</b>')]], cls='t fill' if blank else 't')
SOCS_ = lambda s, o, c1, c2, sp1, sp2, most='': report(['<b>S</b> &nbsp;The distribution is ', ('symmetric / positively / negatively skewed', s), '.<br><b>O</b> &nbsp;There ', ('no outliers / an outlier at … / outliers at …', o),
    '.<br><b>C</b> &nbsp;The distribution is centred at ', ('value', c1), ', the ', ('median / mean / mode', c2), '.<br><b>S</b> &nbsp;The ', ('range / IQR', sp1), ' is ', ('value', sp2), '.'] + ([' Most values lie between ', ('a and b', most), '.'] if most else []))

def SOCS(*x): return SOCS_(*x).replace('<p class="tpl">', '<p class="tpl" style="line-height:2.5">')
P = [CSS, title('1C–1E', 'Displaying and describing numerical data; log scales')]
P.append(lis(['To be able to construct frequency tables for discrete numerical data.', 'To be able to construct frequency tables for grouped numerical data (discrete and continuous).',
  'To be able to construct a histogram from a frequency table for numerical data.', 'To be able to construct a histogram from numerical data using a CAS calculator.',
  'To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.',
  'To be able to construct a dot plot for numerical data.', 'To be able to construct a stem plot for numerical data.',
  'To be able to revise the concept of log<sub>10</sub> <i>x</i>.', 'To be able to investigate the effect of the logarithmic scale on the features of a distribution.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
AFL = '266 259 238 227 210 160 160 159 155 145 133<br>99 91 80 80 75 73 58 42 36 32 25<br>32 25 25 21 17 13 10 9 9 4 2'
P.append(box('Question 1', side(q('The following data gives the number of games played in total by each member of an AFL club:') + f'<div class="data" style="font-size:9pt">{AFL}</div>'
  + parts([('a', 'Use a CAS calculator to construct a histogram starting at 0 with column width 20.', '', 0),
           ('b', 'Describe the shape of the histogram of the number of games played (above).', 'Positively skewed: most players have played fewer than 100 games; the tail runs out to the right.', 14)]),
  hist(0, 20, [7, 7, 2, 2, 4, 0, 1, 3, 2, 0, 1, 2, 1, 1], 8, 2, 'number of games played', draw=False, lab=2, W=300, H=150, mm=88), 88)))
GL = [0] * 16 + [0.3, 0.6, 1.2, 1.6, 1.6, 2.2, 2.6, 3.2, 6.4, 7.2, 7.8, 12.4, 16.8, 17.8]
P.append(box('Question 2 · VCAA 2016 Exam 2 Q1d (adapted)', q('The following dot plot shows the average number of goals scored per season by each player within a soccer club.')
  + q('Use the grid to construct a histogram that displays the distribution of the average number of goals scored per season at the soccer club. Use interval widths of two with the first interval starting at 0.')
  + '<div class="row" style="align-items:center"><div style="flex:1">' + dotplot(0, 19, [round(x, 1) for x in GL], 'average goals scored', r=2.2, W=300, mm=88) + '</div><div style="flex:1">'
  + hist(0, 2, [21, 3, 0, 3, 0, 0, 1, 0, 2], 22, 2, 'average goals scored', draw=False, W=300, H=170, mm=88) + '</div></div>', '2 marks'))
PARTY = '19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29'
MOTH = [('1', [8]), ('2', [2, 2, 4, 4, 4]), ('2', [5, 5, 9]), ('3', [0, 0, 1, 2, 3, 4]), ('3', [6, 8]), ('4', [0, 3])]
P.append(pair(box('Question 3', q('Construct a stem plot of the ages of a group of people at a party:') + f'<div class="data">{PARTY}</div>'
      + space(52, stem([('1', [7, 9, 9, 9]), ('2', [0, 0, 1, 1, 2, 3, 6, 7, 8, 9]), ('3', [4, 4, 7]), ('4', [5]), ('5', [6]), ('6', [6])], 'Key: 1 | 7 = 17', '<i>age</i> (years)'), grow=True)),
  box('Question 4 · VCAA 2017 Exam 2 Q2b (adapted)', q('The following stem plot displays the <i>wingspan</i>, in millimetres, of 19 moths that were captured.')
      + cen(stem(MOTH, 'Key: 1 | 2 = 12', '<i>wingspan</i> (mm)')) + q('Write down the modal <i>wingspan</i>, in millimetres, of the moths captured.') + wline('24 mm (leaf 4 appears three times on the first 2 stem)'), '1 mark')))
P.append(box('Question 5', parts([('a', 'Find the log of 592 to two decimal places.', 'log<sub>10</sub>(592) = 2.772… → 2.77', 'L'),
                                  ('b', 'What is the order of magnitude of 478 000?', '478 000 = 4.78 × 10<sup>5</sup> → 5', 'L')], cols=2)))

# ---------------------------------------------------------------- 1C frequency tables and histograms
P.append(sect('1C Displaying and describing numerical data', 'Example, then you try'))
P.append(box('Example 6 · Frequency table for discrete numerical data', side(
  q('The number of bedrooms in each of the 24 properties sold in a certain area over a one month period are as follows:') + '<div class="data">2 3 4 3 3 4 3 4 4 1 3 2<br>1 2 2 2 4 5 3 4 4 5 3 4</div>'
  + q('Construct a table for these data showing both frequency and percentage frequency, giving the values of the percentage frequency rounded to one decimal place.'),
  ftab2('Number of bedrooms', [('1', 2, '8.3'), ('2', 5, '20.8'), ('3', 7, '29.2'), ('4', 8, '33.3'), ('5', 2, '8.3')], (24, '99.9'), pcth='%'), 80)))
HRS = '35.0 48.0 45.0 43.0 38.2 50.0 39.8 40.7<br>40.0 50.0 35.4 38.8 40.2 45.0 45.0 40.0<br>43.0 48.8 43.3 53.1 35.6 44.1 34.8'
PLANT_A = table([['<i>height</i> (cm)', 'number', '%']] + [list(r) for r in [('30−&lt;40', 1, 5), ('40−&lt;50', 5, 25), ('50−&lt;60', 7, 35), ('60−&lt;70', 3, 15), ('70−&lt;80', 2, 10), ('80−&lt;90', 2, 10)]] + [['<b>total</b>', '<b>20</b>', '<b>100</b>']])
P.append(exyt('Example 7 · Constructing a grouped frequency table', q('The data below give the average hours worked per week in 23 countries.') + f'<div class="data" style="font-size:9pt">{HRS}</div>'
      + q('Construct a grouped frequency table with five intervals.')
      + ftab2('Average hours worked', [('30.0−34.9', 1, '4.3'), ('35.0−39.9', 6, '26.1'), ('40.0−44.9', 8, '34.8'), ('45.0−49.9', 5, '21.7'), ('50.0−54.9', 3, '13.0')], (23, '99.9')),
  'You try 7', q('The <i>height</i> (cm) of 20 plants in a Year 6 science experiment were recorded.') + '<div class="data" style="font-size:9pt">32.0 40.2 40.5 45.1 47.0 49.1 50.1<br>53.7 54.2 55.3 56.9 57.2 58.2 67.2<br>68.9 69.0 72.3 77.6 82.1 88.5</div>'
      + q('Construct a grouped frequency table with intervals of 10.') + space(50, PLANT_A, grow=True)))
P.append(exyt('Example 8 · Constructing a histogram from a frequency table', q('Construct a histogram for the frequency table opposite.')
      + table([['Average hours worked', 'Frequency'], ['30.0–34.9', 1], ['35.0–39.9', 6], ['40.0–44.9', 8], ['45.0–49.9', 5], ['50.0–54.9', 3], ['<b>Total</b>', '<b>23</b>']])
      + hist(25, 5, [0, 1, 6, 8, 5, 3, 0], 9, 1, 'Average hours worked', 'Frequency', draw=False, H=150),
  'You try 8', q('The <i>height</i> (cm) of 20 plants in a Year 6 science experiment was recorded in the following grouped frequency table.') + PLANT_A
      + parts([('a.', 'Construct a histogram to display this data.', hist(30, 10, [1, 5, 7, 3, 2, 2], 8, 1, 'height (cm)', H=150, mm=72), 52),
               ('b.', 'What percentage of plants were shorter than 60 cm?', '5 + 25 + 35 = 65%', 'L')])))
GV = [2, 2, 2, 2, 2, 2, 2, 4, 6, 10, 16, 34, 95, 233, 300, 207, 86, 4]
P.append(box('Example 9 · Describing the features of a distribution from a histogram', side(
  q('The histogram shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year.') + q('Describe this histogram in terms of shape, centre, spread and outliers.')
  + SOCS('negatively skewed', 'are possible outliers below 34 weeks', 'around 38–39 weeks', 'median', 'range', '17 weeks (25 to 42)', '36 and 41 weeks'),
  hist(25, 1, GV, 300, 100, 'Gestation period (weeks)', 'Frequency', lab=2, W=280, H=160), 82)))

# ---------------------------------------------------------------- 1D dot plots and stem plots
P.append(sect('1D Dot plots and stem plots', 'Example, then you try'))
CR = [22, 19, 18, 19, 23, 25, 22, 29, 18, 22, 23, 24, 22]; PET = [3, 2, 0, 1, 1, 3, 0, 5, 2, 1, 1, 2]
P.append(exyt('Example 10 · Constructing a dot plot', q('The ages (in years) of the 13 members of a cricket team are:') + '<div class="data">22 19 18 19 23 25 22 29 18 22 23 24 22</div>' + q('Construct a dot plot.')
      + dotplot(17, 30, CR, 'Age (years)', draw=False, rows=5, W=220, mm=80),
  'You try 10', q('Sophie surveyed 12 of the families living on her street.<br>She asked for the number of pets each of them owned and the results were recorded.') + '<div class="data">3 2 0 1 1 3 0 5 2 1 1 2</div>'
      + parts([('a.', 'Construct a dot plot to display this data.', dotplot(0, 5, PET, 'number of pets', draw=False, rows=4, W=200, mm=70), 40),
               ('b.', 'What was the modal number of pets owned by families that Sophie surveyed?', '1 pet (the most dots: 4 families)', 'L')])))
EX = '55 68 76 90 83 89 75 66 59 84 48 62 58<br>95 80 77 61 92 99 63 84 65 70 81 96'
P.append(exyt('Example 11 · Constructing a stem plot', q('University participation rates (%) in 23 countries are given below.') + '<div class="data">26 3 12 20 36 1 25 26 13 9 26 27<br>15 21 7 8 22 3 37 17 55 30 1</div>'
      + q('Display the data in the form of a stem plot.')
      + cen(stem([('0', [1, 1, 3, 3, 7, 8, 9]), ('1', [2, 3, 5, 7]), ('2', [0, 1, 2, 5, 6, 6, 6, 7]), ('3', [0, 6, 7]), ('4', []), ('5', [5])], 'Key: 1 | 2 = 12', '<i>rate</i> (%)', blank=True)),
  'You try 11', q('Ms Smyth’s maths class of 25 students sat their end-of-year exam. Their results (%) were recorded.') + f'<div class="data">{EX}</div>'
      + parts([('a.', 'Construct a stem plot to display this data.', stem([('4', [8]), ('5', [5, 8, 9]), ('6', [1, 2, 3, 5, 6, 8]), ('7', [0, 5, 6, 7]), ('8', [0, 1, 3, 4, 4, 9]), ('9', [0, 2, 5, 6, 9])], 'Key: 4 | 8 = 48%'), 50),
               ('b.', 'How many students scored above 70% on the exam?', '3 + 6 + 5 = 14 students', 'L')])))

# ---------------------------------------------------------------- 1E logs
P.append(sect('1E Using a logarithmic (base 10) scale to display data', 'Example, then you try'))
P.append(exyt('Example 12 · Using a CAS calculator to find logs',
  parts([('a', 'Find the log of 45, correct to two significant figures.', 'log 45 = 1.65… = 1.7', 'L'), ('b', 'Find the number with log equal to 2.7125, correct to the nearest whole number.', '10<sup>2.7125</sup> = 515.82… = 516', 'L')]),
  'You try 12', q('Use log<sub>10</sub> for the following calculations.')
      + parts([('a.', 'Calculate the log of 23, correct to two decimal places.', 'log<sub>10</sub>(23) = 1.361… → 1.36', 'L'), ('b.', 'If the log of a number is 5, what is the number?', '10<sup>5</sup> = 100 000', 'L')])))
P.append(exyt('Example 13 · Interpreting a histogram with a log scale', q('The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.')
      + hist(-2, 1, [3.7, 7.4, 18.5, 25.9, 25.9, 11.1, 7.4], 28, 4, 'log(body weight)', 'Percentage', pct=True, H=130, mm=62)
      + parts([('a', 'What body weight (in kg) is represented by the number 4 on the log scale?', '10<sup>4</sup> = 10 000 kg', 'L'),
               ('b', 'How many of these animals have body weights more than 10 000 kg?', 'one bar above 4: 7.4% of 27 = 2 animals', 'L'),
               ('c', 'The weight of a cat is 3.3 kg. Use your calculator to determine the log of its weight correct to two significant figures.', 'log 3.3 = 0.518… = 0.52', 'L'),
               ('d', 'Determine the weight (in kg) of the animal with a log(<i>body weight</i>) of 3.4 (the elephant). Write your answer correct to the nearest whole number.', '10<sup>3.4</sup> = 2511.88… = 2512 kg', 'L')]),
  'You try 13', q('A class of twenty students were asked about the <i>distance</i>, in kilometres, from their home to the school.<br>The results were summarised in a histogram using a log<sub>10</sub> scale.')
      + hist(-1, .5, [2, 3, 3, 5, 6, 1], 8, 2, 'log₁₀(distance)', dec=1, H=130, mm=62)
      + parts([('a.', 'Jane was away the day of the survey. It is known that she lives 9.5 km away from school. Which interval on the histogram reflects this?', 'log<sub>10</sub>(9.5) = 0.977… → 0.5–&lt;1.0', 14),
               ('b.', 'How many students live more than 10 km away from school?', 'log<sub>10</sub>(10) = 1; columns above 1: 6 + 1 = 7 students', 14)])))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
P.append(box('Exit task 1 · VCAA 2020 Exam 2 Q2a', side(q('The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the dot plot below.')
  + q('Write down the modal <i>neck size</i>, in centimetres, for these 250 men.') + wline('38 cm (the tallest column: 48 dots)'),
  dotplot(30, 45, [k for k, f in neck.items() for _ in range(f)], 'neck size (cm)', r=1.15, W=300, mm=95), 95), '1 mark'))
TEMP = [('2', [2, 2, 4, 4]), ('2', [5, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]), ('3', [1, 2, 3, 3, 4, 4, 4]), ('3', [5, 6, 7, 7, 7, 7]), ('4', [1])]
P.append(pair(box('Exit task 2 · VCAA 2016 Exam 1 Q3', q('The stem plot below displays 30 temperatures recorded at a weather station.') + cen(stem(TEMP, 'key: 2|2 = 2.2 °C', '<i>temperature</i>'))
      + q('The modal temperature is') + mc(['2.8 °C', '2.9 °C', '3.7 °C', '8.0 °C', '9.0 °C'], 'A', cols=3) + why('2 | 8 has six leaves, the most of any value: 2.8 °C.'), '1 mark'),
  box('Exit task 3 · VCAA 2019 Exam 1 Q3', q('The histogram below shows the population size for these 48 countries plotted on a log<sub>10</sub> scale.')
      + hist(0, 1, [0, 0, 1, 0, 7, 5, 21, 13, 1, 0], 25, 5, 'log₁₀ (population size)', H=125, mm=62)
      + q('Based on this histogram, the number of countries with a population size that is less than 100 000 people is') + mc(['1', '5', '7', '8', '48'], 'D', cols=5)
      + why('100 000 = 10<sup>5</sup> = 5 on the log scale; columns below 5: 1 + 7 = 8.'), '1 mark')))

P.append(close(['I can construct a frequency table for discrete numerical data.', 'I can construct a grouped frequency table.', 'I can construct a histogram from a grouped frequency table.',
  'I can describe the features of a distribution from a histogram.', 'I can construct a dot plot.', 'I can construct a stem plot.', 'I can use a CAS calculator to find logs.', 'I can interpret a histogram with a log scale.'],
  [('1C', 'Q1–12'), ('1D', 'Q1–11'), ('1E', 'Q1–6')], ['1C', '1D', '1E']))
build('S2', '1C–1E', 'AoS 1 · Data analysis', P)
