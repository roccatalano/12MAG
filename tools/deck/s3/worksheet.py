"""Lesson 3 (1F) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py; model tools/deck/s1/worksheet.py).
Questions verbatim from the approved deck tools/deck/z10/s3_build.py (lessons/S3-slides.html), same order and numbering. No CAS steps, no key ideas, no guess-% boxes.
Sources (not printed, Rocco 15 Nov: only exam questions show their source): APK 1a/1b = Cambridge U1&2 Ch 2 skills checklist 2E #10, 2F #11;
APK 2 = VCAA 2017 Exam 2 Q1ai (via Edrolo U1&2 1D Q18); Examples 14-21 = Cambridge U3&4 1F Examples 14-21 (pp. 45-50);
You try 14 = Edrolo U3&4 1E WE1 data (adapted: median only); You try 15 = 1F WE2a; You try 16 = 1F WE3a; You try (five-number summary) = 1E WE1;
You try 17 = 1E WE2a; You try 18 = 1E WE2b; You try 20 = 1F WE1a; You try 21 = 1G WE1; exam practice = VCAA 2024 Exam 1 Q3 and Q14;
CAS examples = Cambridge U3&4 1F pp. 53-54 and Example 15 data; You try (CAS) = Edrolo U3&4 1G WE2;
exit = Edrolo U3&4 1G Q11 (adapted from VCAA 2020 Exam 2 Q4aii).
Run: python3 tools/deck/s3/worksheet.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *

def stemw(rows, key, cap='', ncol=None):
    """Stem plot, large and neat: one fixed-width cell per leaf so the columns line up."""
    ncol = ncol or max(len(lv) for _, lv in rows)
    td = 'style="width:5.2mm;text-align:center;padding:0"'
    tr = ''.join(f'<tr><td style="text-align:right;border-right:1.5px solid #000;padding:0 2.5mm 0 1mm;font-weight:bold">{s}</td><td style="width:2mm;padding:0"></td>'
                 + ''.join(f'<td {td}>{lv[i] if i < len(lv) else ""}</td>' for i in range(ncol)) + '</tr>' for s, lv in rows)
    c = f'<b>{cap}</b> &nbsp;' if cap else ''
    return (f'<div style="display:flex;justify-content:center"><div><div style="font-size:8.5pt">{c}{key}</div>'
            f'<table style="font-family:Courier New,monospace;font-size:12pt;line-height:1.35;border-collapse:collapse;margin:1mm 0">{tr}</table></div></div>')
def dotw(vals, lo, hi, xl='', mm=110, r=5):
    W = 440; L = 20; pw = W - 40; sx = lambda x: L + (x - lo) / (hi - lo) * pw
    cnt = {}
    for v in vals: cnt[v] = cnt.get(v, 0) + 1
    top = max(cnt.values()) * (2 * r + 2) + 10; H = top + (40 if xl else 24)
    o = [f'<circle cx="{sx(v):.1f}" cy="{top - k*(2*r+2) - r - 3}" r="{r}" fill="#000"/>' for v in cnt for k in range(cnt[v])]
    ax = f'<line x1="{L-8}" x2="{W-L+8}" y1="{top}" y2="{top}" stroke="#000"/>' + ''.join(f'<line x1="{sx(x):.1f}" x2="{sx(x):.1f}" y1="{top}" y2="{top+4}" stroke="#000"/><text x="{sx(x):.1f}" y="{top+15}" font-size="10" text-anchor="middle">{x}</text>' for x in range(lo, hi + 1))
    if xl: ax += f'<text x="{W/2}" y="{top+32}" font-size="11" text-anchor="middle" font-style="italic">{xl}</text>'
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{ax}{"".join(o)}</svg>'
def histw(start, w, v, ymax, ystep, xl='', yl='Frequency', mm=80, lab=None):
    W, H, L, B, T = 300, 170, 34, 34, 8; n = len(v); pw = W - L - 10; ph = H - B - T
    sx = lambda i: L + i * pw / n; sy = lambda y: T + ph - y / ymax * ph
    o = [f'<line x1="{L}" x2="{L}" y1="{T}" y2="{T+ph}" stroke="#000"/><line x1="{L}" x2="{W-10}" y1="{T+ph}" y2="{T+ph}" stroke="#000"/>']
    for y in range(0, ymax + 1, ystep): o.append(f'<text x="{L-4}" y="{sy(y)+3}" font-size="9" text-anchor="end">{y}</text><line x1="{L-3}" x2="{L}" y1="{sy(y)}" y2="{sy(y)}" stroke="#000"/>')
    for i, f in enumerate(v):
        if f: o.append(f'<rect x="{sx(i):.1f}" y="{sy(f):.1f}" width="{pw/n:.1f}" height="{ph-(sy(f)-T):.1f}" fill="#ddd" stroke="#000"/>')
    for i in range(0, n + 1, lab or 1): o.append(f'<text x="{sx(i):.1f}" y="{T+ph+12}" font-size="9" text-anchor="middle">{round(start+i*w, 6):g}</text>')
    o.append(f'<text x="{L+pw/2}" y="{H-4}" font-size="10" text-anchor="middle" font-style="italic">{xl}</text><text transform="translate(10 {T+ph/2}) rotate(-90)" font-size="10" text-anchor="middle">{yl}</text>')
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{"".join(o)}</svg>'
def side(left, fig, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{fig}</div></div>'

P = [title('1F', 'Measures of centre and spread')]
P.append(lis(['To be able to understand the mean and the median as measures of centre.', 'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
  'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.', 'To be able to use a CAS calculator to calculate these summary statistics.']))

# ---------------------------------------------------------------- APK (deck: APK 1 of 3 = part a, 2 of 3 = part b, 3 of 3 = VCAA)
P.append(sect('Activating prior knowledge', 'Year 11'))
PARTY = [('1', [7, 9, 9, 9]), ('2', [0, 0, 1, 1, 2, 3, 6, 7, 8, 9]), ('3', [4, 4, 7]), ('4', [5]), ('5', [6]), ('6', [6])]
P.append(box('Question 1', side(q('The ages of a group of people at a party:') + '<div class="data">19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29</div>'
  + parts([('a', 'Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?', 'x̄ = 583 ÷ 20 = 29.15 · n = 20: M = (23 + 26) ÷ 2 = 24.5<br>x̄ = 29.15, M = 24.5: the <b>median</b> is preferred (outliers 56, 66 and a skewed shape pull the mean up).', 24),
           ('b', 'Determine the quartiles and hence the IQR of the ages of the people at the party.', 'Q<sub>1</sub> = (20 + 20) ÷ 2 = 20, Q<sub>3</sub> = (34 + 34) ÷ 2 = 34<br>Q<sub>1</sub> = 20, Q<sub>3</sub> = 34, IQR = 14', 18)]),
  stemw(PARTY, 'Key: 1 | 7 = 17'), 62)))
EGG = '<table class="t"><tr><th rowspan="2"><i>number of eggs</i></th>' + ''.join(f'<td>{x}</td>' for x in [172, 192, 159, 125, 197, 135]) + '</tr><tr>' + ''.join(f'<td>{x}</td>' for x in [140, 140, 138, 166, 136, 131]) + '</tr></table>'
P.append(box('Question 2 · VCAA 2017 Exam 2 Q1ai', q('The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.') + EGG
  + q('From the information given, determine the range.') + space(12, 'range = 197 − 125 = 72 eggs'), '1 mark'))

# ---------------------------------------------------------------- 1F
P.append(sect('1F Measures of centre and spread', 'Example, then you try'))
P.append(exyt('Example 14 · Finding the median value in a data set', q('Order each of the following data sets, locate the median, and then write down its value.')
    + parts([('a', '<span class="data">2 9 1 8 3 5 3 8 1</span>', '1 1 2 3 <b>3</b> 5 8 8 9 · n = 9, (9 + 1) ÷ 2 = 5th value · M = 3', 16),
             ('b', '<span class="data">10 1 3 4 8 6 10 1 2 9</span>', '1 1 2 3 <b>4 6</b> 8 9 10 10 · n = 10, 5.5th: average the 5th and 6th · M = (4 + 6) ÷ 2 = 5', 16)]),
  'You try 14', q('Order the following data set, locate the median, and then write down its value.') + '<div class="data">3 5 1 10 8 9 6 3 8 6</div>'
    + space(30, '1 3 3 5 <b>6 6</b> 8 8 9 10 · n = 10, (10 + 1) ÷ 2 = 5.5th: average the 5th and 6th<br>M = (6 + 6) ÷ 2 = 6', grow=True)))
CRIC = [18, 18, 19, 19, 22, 22, 22, 22, 23, 23, 24, 25, 29]
ED2 = [23] + [24] * 2 + [25] * 4 + [26] * 4 + [27] * 7 + [28] * 5 + [29] * 3 + [30, 31]
P.append(exyt('Example 15 · Finding the median value from a dot plot', q('The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team. Determine the median age of these cricketers and mark its location on the dot plot.')
    + dotw(CRIC, 17, 30, 'Age (years)', mm=80) + space(16, 'n = 13: (13 + 1) ÷ 2 = 7th value · the median age is 22 years (marked on the plot)'),
  'You try 15', q('Consider the dot plot.') + dotw(ED2, 22, 31, mm=80) + parts([('a.', 'Determine the median.', 'n = 28: (28 + 1) ÷ 2 = 14.5th · M = (27 + 27) ÷ 2 = 27', 22)])))
W16 = [('1', [8, 9, 9]), ('2', [0, 2, 5, 7, 8, 9, 9]), ('3', [1, 3])]
E3 = [('40', [7]), ('41', []), ('42', []), ('43', []), ('44', [4, 6]), ('45', [1, 3, 3]), ('46', [2, 6, 7]), ('47', [4, 7, 8, 9]), ('48', [0, 0, 4, 5, 6, 8]), ('49', [1, 2, 5, 5, 5, 9]), ('50', [3, 4, 4, 7, 8, 8, 9, 9])]
P.append(exyt('Example 16 · Finding the median value from a stem plot', q('The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the median maximum temperature for these 12 days.')
    + stemw(W16, 'Key: 0 | 8 = 8°C') + space(16, '(12 + 1) ÷ 2 = 6.5th: average the 6th and 7th, 25 and 27 · M = (25 + 27) ÷ 2 = 26°C'),
  'You try 16', q('Consider the stem plot.') + stemw(E3, 'Key: 40 | 7 = 407') + parts([('a.', 'Calculate the median.', 'n = 33: (33 + 1) ÷ 2 = 17th value · M = 485', 16)])))
P.append(box('You try · Five-number summary', side(q('Construct a five-number summary for the following data.') + '<div class="data">3 5 1 10 8 9 6 3 8 6</div>',
  space(26, '1 3 <b>3</b> 5 6 | 6 8 <b>8</b> 9 10 · min = 1, max = 10<br>M = (6 + 6) ÷ 2 = 6 · Q<sub>1</sub> = 3rd value of the lower half = 3 · Q<sub>3</sub> = 3rd value of the upper half = 8<br><b>1, 3, 6, 8, 10</b> (min, Q<sub>1</sub>, M, Q<sub>3</sub>, max)'), 108)))
NET = [('2', [2, 3, 5, 7, 9]), ('3', [0, 1, 3, 5, 7, 7, 8]), ('4', [0, 1, 2, 2])]
NETQ = q('The following stem plot displays the number of goals scored by 16 netball teams over a season.') + stemw(NET, 'Key: 2 | 2 = 22 goals')
P.append(exyt('Example 17 · Finding the range from a stem plot', q('The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the temperature range over these 12 days.')
    + stemw(W16, 'Key: 0 | 8 = 8°C') + space(14, 'Lowest = 18, highest = 33 · R = 33 − 18 = 15°C'),
  'You try 17', NETQ + parts([('a.', 'Calculate the range of goals scored.', 'Lowest = 22, highest = 42 · R = 42 − 22 = 20 goals', 14)])))
CATS = [('1', [9]), ('2', [1, 3, 5, 8]), ('3', [0, 0, 4, 9, 9]), ('4', [0, 4, 5, 8]), ('5', [0, 3]), ('6', [3, 4])]
P.append(exyt('Example 18 · Finding the IQR from an ordered stem plot when n is even', q('Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.')
    + stemw(CATS, '1 | 2 represents 1.2 kg', 'Weight (kg)') + space(24, 'Nine in each half · lower half: 5th value, Q<sub>1</sub> = 2.8 · upper half: 5th value, Q<sub>3</sub> = 4.8<br>IQR = 4.8 − 2.8 = 2.0 kg'),
  'You try 18', NETQ + parts([('b.', 'Calculate the IQR of goals scored.', 'Eight in each half · Q<sub>1</sub> = (27 + 29) ÷ 2 = 28, Q<sub>3</sub> = (38 + 40) ÷ 2 = 39<br>IQR = 39 − 28 = 11 goals', 26)])))
LIFE = [('5', [2]), ('5', [5, 6]), ('6', [4]), ('6', [6, 6, 7, 9]), ('7', [1, 2, 2, 3, 3, 4, 4, 4, 4]), ('7', [5, 5, 6, 6, 7, 7])]
P.append(box('Example 19 · Finding the IQR from an ordered stem plot when n is odd', side(q('The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.')
  + space(30, 'n = 23: median = 12th value = 73 · n is odd: leave the median out, 11 values below and 11 above<br>Q<sub>1</sub> = middle (6th) of the bottom 11 = 66 · Q<sub>3</sub> = middle (6th) of the top 11 = 75<br>IQR = 75 − 66 = 9 years'),
  stemw(LIFE, 'Stem: 5 | 2 = 52 years'), 66)))
P.append(exyt('Example 20 · Finding the median and quartiles from a histogram', q('The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.')
    + histw(10, 10, [1, 0, 0, 2, 4, 5, 3, 6, 2], 7, 1, 'internet hours per week') + space(22, 'Median = 12th value: 60–70 hours · Q<sub>1</sub> = 6th from the bottom: 50–60 hours · Q<sub>3</sub> = 6th from the top: 80–90 hours'),
  'You try 20', q('Consider the histogram.') + histw(1, 1, [3, 15, 12, 13, 9, 5, 2], 16, 4, '', 'frequency')
    + parts([('a.', 'Estimate the median.', 'n = 59: 30th value · running totals 3, 18, 30: the 3–&lt;4 interval · M ≈ (3 + 4) ÷ 2 = 3.5', 24)])))
LOG = 'log<tspan baseline-shift="sub" font-size="7">10</tspan> (population density)'
P.append(box('Exam practice · VCAA 2024 Exam 1 Q3', side(q('The histogram below displays the population density, in people per km<sup>2</sup>, of the 27 countries in the European Union in 2021. The histogram has a logarithmic (base 10) scale.')
  + q('The median value occurs in a column with a frequency of') + mc(['2', '3', '6', '9'], 'D', cols=4)
  + why('n = 27: median = 14th value; running totals 2, 4, 6, 12, 21, so the 14th is in the 2.0–2.2 column (frequency 9).'),
  histw(1.0, 0.2, [0, 2, 2, 2, 6, 9, 3, 1, 1, 0, 0, 1, 0], 10, 2, LOG, 'frequency', mm=78, lab=2), 80), '1 mark'))
P.append(exyt('Example 21 · Calculating the mean from the formula', q('The following is a set of reaction times (in milliseconds). Write down the values of the following, correct to one decimal place.') + '<div class="data">38 36 35 43 46 64 48 25</div>'
    + parts([('a', '<i>n</i>', 'n = 8', 'L'), ('b', 'Σ<i>x</i>', 'Σx = 335', 'L'), ('c', '<i>x̄</i>', 'x̄ = 335 ÷ 8 = 41.875 → 41.9', 'L')], cols=3),
  'You try 21', q('The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.')
    + '<div class="data">11.60 55.50 7.95 42.15 17.10 2.00 82.55 26.85 5.40 21.90</div>' + space(20, 'Σx = 273, n = 10 · x̄ = 273 ÷ 10 = 27.3<br>The mean amount spent is $27.30.', grow=True)))
YR = list(range(2011, 2023)); NEW = [14, 11, 7, 6, 11, 13, 12, 6, 10, 15, 12, 10]
STAFF = ('<table class="t" style="font-size:8.8pt"><tr><th><i>year</i></th>' + ''.join(f'<td>{y}</td>' for y in YR) + '</tr><tr><th><i>new</i></th>' + ''.join(f'<td>{x}</td>' for x in NEW) + '</tr></table>'
         '<div style="font-size:8pt;text-align:center">(values read off the time series plot)</div>')
P.append(box('Exam practice · VCAA 2024 Exam 1 Q14', q('A school runs an orientation program for new staff each January. The time series plot below shows the number of new staff, <i>new</i>, for each year, <i>year</i>, from 2011 to 2022 (inclusive).') + STAFF
  + q('The number of new staff in 2023 is added to the total number of new staff from the previous 12 years. For these 13 years, the mean number of new staff is 11.') + q('The number of new staff in 2023 is')
  + mc(['11', '16', '17', '19'], 'B', cols=4) + why('Total for 13 years = 11 × 13 = 143; total for 12 years = 127; 2023 = 143 − 127 = 16.'), '1 mark'))
HTS = '<div class="data">176 160 163 157 168 172 173 169</div>'
FT = '<table class="t"><tr><th>age</th>' + ''.join(f'<td>{x}</td>' for x in [18, 19, 22, 23, 24, 25, 29]) + '</tr><tr><th>freq</th>' + ''.join(f'<td>{x}</td>' for x in [2, 2, 4, 2, 1, 1, 1]) + '</tr></table>'
P.append(exyt('CAS example · Mean and standard deviation from a list', q('The following are the heights (in cm) of a group of women.') + HTS
    + q('Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.') + space(14, 'n = 8 · x̄ = 167.25 cm, s<sub>x</sub> = 6.67 cm')
    + QSEP + '<b>Summary statistics from a frequency table</b>' + q('When values repeat (a dot plot or frequency table), enter each value once and its frequency in a second list. Check with the cricket team from Example 15:') + FT
    + space(12, 'n = 13 · x̄ = 22, median = 22 · s<sub>x</sub> = 3.08'),
  'You try', q('The weight, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ weight, rounded to two decimal places.')
    + '<div class="data">80 95 85 91 102 93 87 78 84 90</div>' + space(24, 'n = 10 · x̄ = 88.5 → 88.50 · s<sub>x</sub> = 7.230… → 7.23<br>mean = 88.50 kg, standard deviation = 7.23 kg', grow=True)))

# ---------------------------------------------------------------- exit
P.append(sect('Exit task', 'Show what you know'))
DENS = ['1.07', '1.07', '1.08', '1.08', '1.03', '1.05', '1.07', '1.06', '1.07', '1.09', '1.02', '1.09']
WT = ['70.1', '90.4', '73.2', '85.0', '84.3', '95.6', '71.7', '95.0', '80.2', '87.4', '94.9', '65.3']
P.append(box('Exit task · VCAA 2020 Exam 2 Q4aii (adapted)', q('The body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 orangutans are shown in the table.')
  + table([['body density (kg/litre)'] + DENS, ['weight (kg)'] + WT], head=False, style='font-size:8.5pt')
  + q('For these 12 orangutans, determine the mean of their body density, in kilograms per litre.') + space(14, 'Use only the body density row · Σx = 12.78 · x̄ = 12.78 ÷ 12 = 1.065 kg/litre (not rounded)'), '1 mark'))

P.append(close(['I can find the median value in a data set.', 'I can find the median value from a dot plot.', 'I can find the median value from a stem plot.', 'I can find the range from a stem plot.',
  'I can find the IQR from a stem plot when n is even.', 'I can find the IQR from a stem plot when n is odd.', 'I can calculate the mean using the formula.', 'I can calculate the mean and standard deviation using the CAS calculator.'],
  [('1F', 'Q1–26')], ['1F']).replace('>Revision booklet<', '>Practice booklet<'))  # deck coursework slide: Cambridge Exercise 1F Q1–26 · Practice booklet 1F section
build('S3', '1F', 'AoS 1 · Data analysis', P)
