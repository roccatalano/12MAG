"""Lesson 4 (1G) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py; model tools/deck/s1/worksheet.py).
Questions verbatim from tools/deck/s4/build.py, in slide order: learning intentions → APK → Example/You try pairs → exits → skills checklist + coursework.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1, 2 = Cambridge U1&2 Ch 2 skills checklist 2H #14, #15; APK 3 = Edrolo U1&2 1F Q16 (adapted from VCAA 2017 Exam 1 Q2).
Examples 22-27 = Cambridge U3&4 Examples 22-27; You try 22 = Edrolo U3&4 1E WE4; You try (CAS) = Edrolo 1E WE5; You try 23 = Edrolo 1E WE6;
You try 25 = Edrolo 1F WE5 (Examples 24, 26, 27 have no Edrolo match). Exits = Edrolo U3&4 1E Q19 (VCAA 2020 E2 Q2c), 1E Q20 (VCAA 2021 E2 Q1e).
Describe answers use SOCS (CLAUDE.md). Run: python3 tools/deck/s4/worksheet.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *

# ---------------------------------------------------------------- figures (static SVG)
def _fmt(v, dec=0): return f'{v:.{dec}f}' if dec else (str(int(v)) if float(v).is_integer() else str(v))
def axis_svg(mn, mx, step, lab=None, xl='', W=340, dec=0, body='', top=26, mm=None):
    lab = lab or step; L, R = 14, 14; s = lambda v: L + (v - mn) / (mx - mn) * (W - L - R); y = top + 30
    o = [f'<line x1="{L}" y1="{y}" x2="{W-R}" y2="{y}" stroke="#000" stroke-width="1"/>']
    for i in range(round((mx - mn) / step) + 1):
        v = mn + i * step; big = abs(((v - mn) / lab) - round((v - mn) / lab)) < 1e-6
        o.append(f'<line x1="{s(v):.1f}" y1="{y}" x2="{s(v):.1f}" y2="{y+(5 if big else 3)}" stroke="#000" stroke-width="{0.9 if big else 0.6}"/>')
        if big: o.append(f'<text x="{s(v):.1f}" y="{y+14}" text-anchor="middle" font-size="9">{_fmt(round(v,6),dec)}</text>')
    if xl: o.append(f'<text x="{W/2}" y="{y+26}" text-anchor="middle" font-size="9" font-style="italic">{xl}</text>')
    h = y + (30 if xl else 19)
    return f'<svg viewBox="0 0 {W} {h}" width="100%" style="max-width:{mm or W*0.27:.0f}mm;display:block;margin:1mm auto">{"".join(o)}{body(s,y) if callable(body) else body}</svg>'
def boxplot(mn, mx, step, lw, q1, m, q3, uw, out=(), lab=None, xl='', dec=0, mode='draw', caps=False, fences=(), W=340, mm=None):
    """mode: 'draw' black boxplot to read from · 'scaffold' blank axis, boxplot in red on the solutions copy only · 'red' whole figure red (inside a You try space)."""
    def body(s, y):
        c = '#000' if mode == 'draw' else RED; cls = ' class="solfig"' if mode == 'scaffold' else ''; yc = y - 14; bh = 16
        o = [f'<g{cls} stroke="{c}" fill="none" stroke-width="1.2">',
             f'<rect x="{s(q1):.1f}" y="{yc-bh/2}" width="{s(q3)-s(q1):.1f}" height="{bh}" fill="#fff"/>',
             f'<line x1="{s(m):.1f}" y1="{yc-bh/2}" x2="{s(m):.1f}" y2="{yc+bh/2}" stroke-width="1.8"/>',
             f'<line x1="{s(lw):.1f}" y1="{yc}" x2="{s(q1):.1f}" y2="{yc}"/><line x1="{s(q3):.1f}" y1="{yc}" x2="{s(uw):.1f}" y2="{yc}"/>']
        if caps: o += [f'<line x1="{s(x):.1f}" y1="{yc-5}" x2="{s(x):.1f}" y2="{yc+5}"/>' for x in (lw, uw)]
        o += [f'<circle cx="{s(x):.1f}" cy="{yc}" r="2.6" fill="#fff"/>' for x in out]
        for fx, t in fences: o.append(f'<line x1="{s(fx):.1f}" y1="{yc-15}" x2="{s(fx):.1f}" y2="{y}" stroke-dasharray="3 2" stroke-width=".9"/><text x="{s(fx):.1f}" y="{yc-18}" font-size="8" fill="{c}" stroke="none" text-anchor="middle">{t}</text>')
        return ''.join(o) + '</g>'
    return axis_svg(mn, mx, step, lab, xl, W, dec, body, top=34 if fences else 22, mm=mm)
def dotplot(mn, mx, vals, xl='', r=4, W=340, lab=1, mm=None):
    from collections import Counter
    c = Counter(vals); dy = 2 * r * 0.95
    def body(s, y): return ''.join(f'<circle cx="{s(v):.1f}" cy="{y-r-1-k*dy:.1f}" r="{r}" fill="#fff" stroke="#000" stroke-width=".6"/>' for v, f in c.items() for k in range(f))
    return axis_svg(mn, mx, 1, lab, xl, W, 0, body, top=max(4, max(c.values()) * dy - 24), mm=mm)
def stem(rows, key):
    return ('<table style="border-collapse:collapse;font-family:\'Courier New\',monospace;font-size:10pt;margin:1mm auto">' + ''.join(
        f'<tr><td style="border-right:1.2px solid #000;padding:0 2mm;font-weight:bold">{a}</td><td style="padding:0 2mm;letter-spacing:1.5px">{" ".join(map(str,b))}</td></tr>' for a, b in rows)
        + f'</table><div style="text-align:center;font-size:8.5pt">{key}</div>')
def five(vals, blank=True):
    f = a if blank else (lambda x: x)
    return table([['minimum', 'Q<sub>1</sub>', 'median', 'Q<sub>3</sub>', 'maximum'], [f(v) for v in vals]], cls='t fill' if blank else 't')
def SOCS(sh, ou, ce, me, sp, sv):
    return report(['<b>S</b> The distribution is ', ('shape', sh), '.<br><b>O</b> There ', ('outliers', ou), '.<br><b>C</b> The distribution is centred at ', ('value', ce), ', the ', ('measure', me),
                   '.<br><b>S</b> The ', ('range / IQR', sp), ' is ', ('value', sv), '.'])
def side(left, fig, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{fig}</div></div>'

P = [title('1G', 'The five-number summary and the boxplot')]
P.append(lis(['To be able to construct the boxplot for displaying the distribution of a numerical data.', 'To be able to define and identify outliers.',
  'To be able to construct both simple boxplots and boxplots with outliers.', 'To be able to determine the features of a distribution from a boxplot.',
  'To be able to use a CAS calculator to construct a boxplot.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
PARTY = q('The ages of a group of people at a party:') + '<div class="data">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>'
P.append(pair(
  box('Question 1', PARTY + q('Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).')
      + five(['17', '20', '24.5', '34', '66']) + space(26, boxplot(15, 70, 5, 17, 20, 24.5, 34, 66, xl='age (years)', mode='red'), grow=True)),
  box('Question 2', PARTY + q('Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).')
      + space(40, 'IQR = 34 − 20 = 14<br>LF = 20 − 1.5 × 14 = −1<br>UF = 34 + 1.5 × 14 = 55<br>56 &gt; 55 = UF → outlier · 66 &gt; 55 = UF → outlier<br>17 &gt; −1 = LF → no low outliers<br>The fences are −1 and 55. The outliers are 56 and 66.', grow=True))))
P.append(box('Question 3 · VCAA 2017 Exam 1 Q2 (adapted)', side(q('The boxplot shows the distribution of the <i>reaction time</i> (milliseconds), of 256 firefighters.')
      + q('The five-number summary for the <i>reaction time</i> of these 256 firefighters is closest to')
      + mc(['70, 130, 140, 152, 179', '70, 130, 140, 152, 255', '122, 130, 140, 152, 179', '122, 130, 140, 152, 245', '122, 130, 140, 152, 265'], 'B')
      + why('The dots at 70, 90 and 255 are data: min = 70, max = 255 (C uses the whisker ends).'),
      boxplot(0, 260, 10, 122, 130, 140, 152, 179, out=(70, 90, 255), lab=50, xl='reaction time (milliseconds)', caps=True), 90), '1 mark'))

# ---------------------------------------------------------------- Examples / You trys
P.append(sect('1G The five-number summary and the boxplot', 'Example, then you try'))
life = [('5', [2]), ('5', [5, 6]), ('6', [4]), ('6', [6, 6, 7, 9]), ('7', [1, 2, 2, 3, 3, 4, 4, 4, 4]), ('7', [5, 5, 6, 6, 7, 7])]
w4 = [('0', [1, 2, 3, 5, 5, 9]), ('1', [0, 0, 1, 5, 8, 9]), ('2', [1, 2, 3, 3, 5]), ('3', [3, 7, 9])]
P.append(exyt('Example 22 · Boxplot from a five-number summary',
  q('The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:')
  + stem(life, "Key: 5|2 = 52 years") + five(["52","66","73","75","77"], blank=False)
  + q('Use the five-number summary to construct a boxplot.') + boxplot(50, 80, 1, 52, 66, 73, 75, 77, lab=5, xl='Life expectancy (years)', mode='scaffold'),
  'You try 22',
  q('The five-number summary for the following stem plot is: <b>1, 7, 16.5, 23, 39</b>') + stem(w4, 'Key: 1 | 2 = 12') + q('Construct a boxplot using the data.')
  + space(52, 'IQR = 23 − 7 = 16 · LF = 7 − 1.5 × 16 = −17 · UF = 23 + 1.5 × 16 = 47<br>1 &gt; −17 = LF and 39 &lt; 47 = UF → no outliers'
          + boxplot(-20, 50, 1, 1, 7, 16.5, 23, 39, lab=10, mode='red', fences=((-17, 'LF = −17'), (47, 'UF = 47'))), grow=True)))
P.append(box('You try · CAS', q('Construct a boxplot for the following data set.') + '<div class="data">2 4 4 5 5 5 7 6 5 4 6 5 6 7 8 12 3 5</div>'
  + space(46, '<div class="row"><div style="flex:1">CAS: min 2 · Q<sub>1</sub> 4 · M 5 · Q<sub>3</sub> 6 · max 12<br>IQR = 6 − 4 = 2 · LF = 4 − 1.5 × 2 = 1 · UF = 6 + 1.5 × 2 = 9<br>12 &gt; 9 = UF → outlier · 2 &gt; 1 = LF → not an outlier<br>Upper whisker stops at 8, the last value inside the fence.</div><div style="flex:1">'
          + boxplot(0, 13, 1, 2, 4, 5, 6, 8, out=(12,), xl='list', mode='red', fences=((1, 'LF = 1'), (9, 'UF = 9'))) + '</div></div>', grow=True)))

P.append(exyt('Example 23 · Reading values from a boxplot',
  q('For the boxplot shown, write down the values of:') + boxplot(0, 100, 2, 10, 30, 36, 44, 60, out=(4, 70, 84, 92), lab=10)
  + parts([('a', 'the median', '36', 'L'), ('b', 'the quartiles Q<sub>1</sub> and Q<sub>3</sub>', 'Q<sub>1</sub> = 30, Q<sub>3</sub> = 44', 'L'),
           ('c', 'the interquartile range (IQR)', 'IQR = 44 − 30 = 14', 'L'), ('d', 'the minimum and maximum values', 'min = 4, max = 92', 'L'),
           ('e', 'the values of any possible outliers', '4, 70, 84 and 92', 'L'),
           ('f', 'the smallest value in the upper end of the data set that will be classified as an outlier', 'UF = 44 + 1.5 × 14 = 65: any value above 65', 'L'),
           ('g', 'the largest value in the lower end of the data set that will be classified as an outlier.', 'LF = 30 − 1.5 × 14 = 9: any value below 9', 'L')]),
  'You try 23',
  q('The <i>number of runs scored</i> by the leading batsman at a local cricket club is represented by the following boxplot.<br>It is known that data was collected from 20 separate innings.')
  + boxplot(0, 100, 5, 30, 50, 70, 80, 90, lab=10, xl='number of runs scored', caps=True)
  + parts([('a.', 'Determine the five-number summary for the data and identify any outliers.', '30, 50, 70, 80, 90; no dots, so no outliers', 14),
           ('b.', 'Between which two values does the middle 50% of data lie?', '50 and 80 runs (Q<sub>1</sub> to Q<sub>3</sub>)', 12),
           ('c.', 'In approximately what percentage of innings did they score more than 80 runs?', '25% (above Q<sub>3</sub>)', 12),
           ('d.', 'In approximately how many innings did they score at least 50 runs, but fall short of 100?', '75% of 20 = 0.75 × 20 = 15 innings', 12)])))
P.append(box('Example 24 · Estimating percentages from a boxplot',
  side(q('For the boxplot shown, estimate the percentage of values:') + boxplot(45, 85, 1, 50, 54, 55, 59, 65, out=(70, 81), lab=5),
       parts([('a', 'less than 54', '25%', 'L'), ('b', 'less than 55', '50%', 'L'), ('c', 'less than 59', '75%', 'L'), ('d', 'greater than 59', '25%', 'L'),
              ('e', 'between 54 and 59', '50%', 'L'), ('f', 'between 54 and 86.', '75%', 'L')], cols=2), 92)))
P.append(exyt('Example 25 · Describing a distribution without outliers',
  q('Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.') + boxplot(0, 50, 1, 0, 5, 10, 21, 45, lab=5)
  + SOCS('positively skewed', 'are no outliers', '10', 'median', 'IQR', '16; range 45'),
  'You try 25',
  q('Consider the boxplot.') + boxplot(12, 20, 0.5, 12, 15, 18, 19, 20, lab=2, caps=True) + q('Describe the distribution in terms of shape, centre, spread and outliers.')
  + space(30, 'The distribution is negatively skewed.<br>There are no outliers.<br>The distribution is centred at 18, the median.<br>The range is 20 − 12 = 8.', grow=True)))
P.append(pair(
  box('Example 26 · Describing a distribution with outliers', q('Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.')
      + boxplot(0, 50, 1, 34, 38.75, 41, 44.25, 47, out=(10, 15, 20, 25), lab=5) + SOCS('symmetric', 'are outliers at 10, 15, 20 and 25', '41', 'median', 'IQR', '5.5; range 37')),
  box('Example 27 · Using a boxplot to answer statistical questions', q('The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.')
      + boxplot(25, 43, 1, 35, 38, 39, 40, 42, out=tuple(range(25, 35)), xl='Gestation period (weeks)')
      + SOCS('negatively skewed', 'are outliers at 25, 26, …, 34 weeks', '39 weeks', 'median', 'IQR', '2 weeks; range 17 weeks'))))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
nv = [k for k, f in neck.items() for _ in range(f)]
FT = table([['minimum', 'first quartile (Q<sub>1</sub>)', 'median', 'third quartile (Q<sub>3</sub>)', 'maximum'], ['31', '36', '38', '39', '44']], style='width:100%')
P.append(box('Exit task 1 · VCAA 2020 Exam 2 Q2c', q('The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.')
  + dotplot(30, 45, nv, 'neck size (cm)', r=1.2, W=340, mm=110)
  + q('The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.') + FT
  + q('Use the five-number summary to construct a boxplot, showing any outliers if appropriate.')
  + side(space(24, 'IQR = 39 − 36 = 3 · LF = 36 − 1.5 × 3 = 31.5 · UF = 39 + 1.5 × 3 = 43.5<br>31 &lt; 31.5 = LF → outlier · 44 &gt; 43.5 = UF → outlier<br>Whiskers stop at 32 and 43.'),
         boxplot(30, 45, 1, 32, 36, 38, 39, 43, out=(31, 44), xl='neck size (cm)', mode='scaffold', fences=((31.5, 'LF 31.5'), (43.5, 'UF 43.5'))), 95), '2 marks'))
hep = [(1, '1.76', '15.34', '41.22'), (2, '1.79', '16.96', '42.41'), (3, '1.83', '13.87', '46.53'), (4, '1.82', '14.23', '40.53'), (5, '1.87', '13.78', '40.62'), (6, '1.73', '14.50', '45.62'), (7, '1.68', '15.08', '42.33'), (8, '1.82', '13.13', '40.88'),
       (9, '1.83', '14.22', '39.22'), (10, '1.87', '13.62', '42.51'), (11, '1.87', '12.01', '42.75'), (12, '1.80', '12.88', '38.12'), (13, '1.83', '12.68', '42.65'), (14, '1.87', '12.45', '41.32'), (15, '1.78', '11.31', '42.88')]
HT = table([['athlete number', 'high jump (metres)', 'shot-put (metres)', 'javelin (metres)']] + [list(h) for h in hep], cls='t tiny')
P.append(box('Exit task 2 · VCAA 2021 Exam 2 Q1e', side(q('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.')
  + q('The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.')
  + boxplot(1.68, 1.88, 0.01, 1.68, 1.78, 1.82, 1.87, 1.87, lab=0.04, dec=2, xl='high jump', caps=True)
  + q('Explain why the boxplot has no whisker at its upper end.') + space(16, 'Q<sub>3</sub> is equal to the maximum value (1.87 m), so there is no distance for an upper whisker to cover.'), HT, 62), '1 mark'))

P.append(close(['I can construct a boxplot from a five-number summary.', 'I can construct a boxplot with outliers from data using the CAS calculator.',
  'I can read values from a boxplot.', 'I can estimate percentages from a boxplot.', 'I can use boxplots to describe a distribution without outliers.',
  'I can use boxplots to describe a distribution with outliers.', 'I can use boxplots to answer statistical questions.'],
  [('1G', 'Q1–20')], ['1G']))
build('S4', '1G', 'AoS 1 · Data analysis', P)
