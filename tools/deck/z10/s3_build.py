r"""12MAG S3 (1F Measures of centre and spread) rebuilt in the 10MA slide house style.
Built on the slide library tools/deck/z10/lib (rules: tools/deck/z10/HOWTO.md).
python3 tools/deck/z10/s3_build.py  ->  lessons/S3-slides.html
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
lesson('1F Measures of centre and spread')
# ---------------- slides ----------------
title_slide('Measures of centre and spread', ['1F Using summary statistics to describe numerical distributions (pp. 44–54)'])
LI = ['To be able to understand the mean and the median as measures of centre.',
      'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
      'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.',
      'To be able to use a CAS calculator to calculate these summary statistics.']
SC = ['I can find the median value in a data set.', 'I can find the median value from a dot plot.', 'I can find the median value from a stem plot.',
      'I can find the range from a stem plot.', 'I can find the IQR from a stem plot when n is even.', 'I can find the IQR from a stem plot when n is odd.',
      'I can calculate the mean using the formula.', 'I can calculate the mean and standard deviation using the CAS calculator.']
SEQ = ['CFAT 1.1.1 (20 minutes, 1A–1E)', 'Activating prior knowledge', 'Key ideas and formulas',
       'The median · Examples 14–16', 'Quartiles, range and IQR · Examples 17–20', 'Exam practice: median from a histogram', 'The mean · Example 21',
       'Exam practice: working back from a mean', 'Mean or median? Standard deviation', 'Mean and standard deviation on CAS', 'Exit task', 'Check-in and coursework']
overview('1F', LI, SC, SEQ, CG + ", 1F Learning intentions (p. 44); success criteria: one per worked example", cols='1.05fr 1.05fr .9fr')
S.append(f'<section class="slide z cfat">{bar("CFAT 1.1.1", "Types of data, displays, log scales")}'
         '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
         '<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · 13 marks</li>'
         '<li>Covers 1A–1E</li><li>Pens down when the timer ends</li></ul></div>'
         '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
         '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
         f'{foot("CFAT 1.1.1 (1A–1E): student copy and solutions on the planner")}</section>')

# APK 1
ages = stem('apk', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17')
APKQ = ('The ages of a group of people at a party:<br>19 21 22 56 34 19 27 28 34 17 66 37 20 20 21 45 26 19 23 29<br>')
S.append(qslide('apk', '1 of 3', 'Year 11 skills: centre', 'Cambridge U1&amp;2 · 2E #10',
    APKQ, KI_MED, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2E #10. Working by teacher.',
    parts=[('a', 'Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?',
      [r'$\bar{x} = \dfrac{583}{20} = 29.15$', (r'$n = 20$: average the 10th and 11th values', 'ln:apk:0:11 lm:apk:9,10'),
       (r'$M = \dfrac{23 + 26}{2} = 24.5$', 'ln:apk:0:11 lm:apk:9,10'), ('Outliers (56, 66) and a skewed shape pull the mean up.', 'ln:apk:0:11 lm:apk:9,10')],
      r'$\bar{x} = 29.15$, $M = 24.5$: the <b>median</b> is preferred.', 'ln:apk:0:11 lm:apk:9,10')],
    fig=stem('apk', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17'), figw='.9fr', cmd='<b>DETERMINE</b> · values, then a choice'))
S.append(qslide('apk', '2 of 3', 'Year 11 skills: spread', 'Cambridge U1&amp;2 · 2F #11',
    APKQ, KI_IQR, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2F #11. Working by teacher.',
    parts=[('b', 'Determine the quartiles and hence the IQR of the ages of the people at the party.', [('$n = 20$: ten values in each half, split on the median line', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi'),
             (r'$Q_1 = \dfrac{20 + 20}{2} = 20$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5'),
             (r'$Q_3 = \dfrac{34 + 34}{2} = 34$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5,14,15')],
    r'$Q_1 = 20$, $Q_3 = 34$, $\boldsymbol{\text{IQR} = 14}$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5,14,15')],
    fig=stem('apk2', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17'), figw='.9fr', cmd='<b>DETERMINE</b> · quartiles, then IQR'))
# APK 2 (exam short answer)
S.append(qslide('apk', '3 of 3', 'A real VCAA question you can already do', 'VCAA 2017 Exam 2 Q1ai',
    'The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.'
    + table_hl('egg', [('number of eggs', ['172', '192', '159', '125', '197', '135']), ('', ['140', '140', '138', '166', '136', '131'])], 'ztab zv zinq zbig')
    + 'From the information given, determine the range.',
    KI_RANGE, [('Scan the table for the extremes: largest = 197, smallest = 125', 'tc:egg:4,3'), (r'$\text{range} = 197 - 125$', 'tc:egg:4,3')],
    r'$\boldsymbol{\text{range} = 72 \text{ eggs}}$',
    'Edrolo General Mathematics Units 1&amp;2, 1D Q18 (VCAA 2017 Exam 2 Data analysis Q1ai). Working by teacher.',
    marks=1, cmd='<b>DETERMINE</b> · one value', vcaa=87, figw='1.1fr', ans_do='tc:egg:4,3', watch='the range is one number (72), not “125 to 197”.'))

# Key ideas
KD = [('Median ($M$)', 'the middle value of the ordered data'), (r'Mean ($\bar{x}$)', 'the sum of the values divided by $n$: the balance point'),
      ('Range', 'largest value minus smallest value'),
      ('Quartiles ($Q_1$, $Q_3$)', 'split the ordered data into four equal groups; $Q_1$ = median of the lower half, $Q_3$ = median of the upper half'),
      ('IQR', 'the spread of the middle 50% of the data'), ('Standard deviation ($s$)', 'the spread of the data around the mean; on CAS it is $s_x$')]
KF = [('Median position', r'$\text{position} = \dfrac{n + 1}{2}$'), ('Median, $n$ even', r'$M = \dfrac{\text{first middle} + \text{second middle}}{2}$'),
      ('Range', r'$\text{range} = \text{largest} - \text{smallest}$'), ('Interquartile range', r'$\text{IQR} = Q_3 - Q_1$'),
      ('Mean', r'$\bar{x} = \dfrac{\Sigma x}{n}$'), ('Standard deviation', r'$s = \sqrt{\dfrac{\Sigma (x - \bar{x})^2}{n - 1}}$ &nbsp;<span class="zn">use CAS: $s_x$, not $\sigma_x$</span>')]
S.append(f'<section class="slide z kif">{bar("1F", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1F Key ideas (pp. 44–52)")}</section>')

# NL: pairs
S.append(nl_slide('Two questions about any distribution',
    'Where is the <b>centre</b>? How <b>spread out</b> is it? <span class="hint">Click to reveal the pairs.</span>',
    r'<div class="zpair"><div class="zpc"><div class="zpt">Centre</div><div class="zbox" id="pM">median $M$<i class="zsub">the middle value</i></div><div class="zbox" id="pX">mean $\bar{x}$<i class="zsub">the balance point</i></div></div>'
    '<div class="zpm">' + st('<span class="zarr">median ⟷ IQR</span><br>resistant: outliers barely move them', do='pair:pM:pI') + st('<span class="zarr">mean ⟷ standard deviation</span><br>use when symmetric, no outliers', do='pair:pM:pI pair2:pX:pS') + '</div>'
    r'<div class="zpc"><div class="zpt">Spread</div><div class="zbox">range<i class="zsub">largest − smallest</i></div><div class="zbox" id="pI">IQR<i class="zsub">the middle 50%</i></div><div class="zbox" id="pS">standard deviation $s$<i class="zsub">spread around the mean</i></div></div></div>'
    + st('<b>They come in pairs.</b> In a SOCS answer, the C and the S lines use the same pair.', True, cls='zctr', do='pair:pM:pI pair2:pX:pS'),
    CG + ', 1F pp. 44, 50–52'))

def nl_median():
    o = [19, 3, 26, 12, 34, 1, 24, 15, 30, 21, 27]; e = [9, 3, 12, 5, 10, 2, 14, 6, 11, 4]
    col = lambda h, t, d, n, last: (f'<div class="col"><h2>{h}</h2>{tiles(t, d)}'
        f'<div class="st stp" data-act="sort:{t}"><b>Step 1</b> Write the data in order. Count them: $n = {n}$</div>'
        f'<div class="st stp" data-do="tn:{t}:0:{6}"><b>Step 2</b> Median position $= \\tfrac{{{n} + 1}}{{2}} = $ {"6th" if n == 11 else "5.5th"}. Count along to it.</div>'
        f'<div class="st stp" data-act="mid:{t}:0:{n-1}:mid">{last}</div>'
        '</div>')
    return nl_slide('The median: the middle value',
        'The <b>median</b> is the middle value in an ordered data set. <span class="hint">Click to find the median.</span>',
        '<div class="cols" style="grid-template-columns:1fr 1fr">' + col('Odd number of values', 'o', o, 11, '<b>Step 3</b> The 6th value is the median. <b>Median $= 21$</b>')
        + col('Even number of values', 'e', e, 10, '<b>Step 3</b> 5.5th: halfway between the 5th and 6th values, $6$ and $9$. <b>Median $= \\tfrac{6 + 9}{2} = 7.5$</b>') + '</div>',
        CG + ', 1F p. 44. Data and steps by teacher (as in the 10MA deck).', 'eng')
S.append(nl_median())

# Example 14 (tiles are the data)
a14 = [2, 9, 1, 8, 3, 5, 3, 8, 1]; b14 = [10, 1, 3, 4, 8, 6, 10, 1, 2, 9]
S.append(qslide('ex', 14, 'Finding the median value in a data set', 'Cambridge · Example 14',
    'Order each of the following data sets, locate the median, and then write down its value.', KI_MED, [], None,
    CG + ', 1F Example 14 (p. 45); cross-off steps by teacher',
    parts=[('a', '2 &nbsp;9 &nbsp;1 &nbsp;8 &nbsp;3 &nbsp;5 &nbsp;3 &nbsp;8 &nbsp;1', [('Order: $n = 9$ (odd)', 'sort:a'), (r'Median position $= \dfrac{9 + 1}{2} = $ 5th value', 'sort:a'),
             ('Count along to the 5th value.', 'sort:a tn:a:0:5 mid:a:0:8:mid')], r'$\boldsymbol{M = 3}$', 'sort:a tn:a:0:5 mid:a:0:8:mid'),
           ('b', '10 &nbsp;1 &nbsp;3 &nbsp;4 &nbsp;8 &nbsp;6 &nbsp;10 &nbsp;1 &nbsp;2 &nbsp;9', [('Order: $n = 10$ (even)', 'sort:b'), (r'Median position $= \dfrac{10 + 1}{2} = $ 5.5th: average the 5th and 6th', 'sort:b'),
             ('Count along to the 5th and 6th values: $4$ and $6$', 'sort:b tn:b:0:6 mid:b:0:9:mid')], r'$\boldsymbol{M = \dfrac{4 + 6}{2} = 5}$', 'sort:b tn:b:0:6 mid:b:0:9:mid')],
    fig=tilerow('a', 'a', a14) + tilerow('b', 'b', b14), cmd='<b>LOCATE</b> · order first, then count in', cls='eng', stack=True))
# You try 14: adapted, median only
y14 = [3, 5, 1, 10, 8, 9, 6, 3, 8, 6]
S.append(qslide('yt', 14, 'Finding the median value in a data set', 'Edrolo 1E WE1 data (adapted)',
    'Order the following data set, locate the median, and then write down its value.', KI_MED,
    [('Order: $n = 10$ (even)', 'sort:y'), (r'Median position $= \dfrac{10 + 1}{2} = $ 5.5th: average the 5th and 6th', 'sort:y'),
     ('Count along to the 5th and 6th values: $6$ and $6$', 'sort:y tn:y:0:6 mid:y:0:9:mid')],
    r'$\boldsymbol{M = \dfrac{6 + 6}{2} = 6}$',
    ED + ', 1E Worked example 1 data; question adapted (median only) to match Example 14. The full five-number summary comes after quartiles.',
    fig=tiles('y', y14), figw='1fr', cmd='<b>LOCATE</b> · order first, then count in', cls='eng'))

# Example 15 / You try 15: dot plots
cr = [18, 18, 19, 19, 22, 22, 22, 22, 23, 23, 24, 25, 29]
S.append(qslide('ex', 15, 'Finding the median value from a dot plot', 'Cambridge · Example 15',
    'The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team. Determine the median age of these cricketers and mark its location on the dot plot.',
    KI_MED, ['Count: $n = 13$ dots', r'Median position $= \dfrac{13 + 1}{2} = $ 7th value',
             ('Count in from the left (each column bottom to top): 18, 18, 19, 19, 22, 22, <b>22</b>', 'dn:d15:7')],
    'The median age is <b>22 years</b> (marked on the plot).', CG + ', 1F Example 15 (p. 45)',
    fig=dotplot('d15', cr, 17, 30, 'Age (years)'), figw='1.2fr', cmd='<b>DETERMINE</b> · the value, marked on the plot', ans_do='dn:d15:7 dm:d15:6'))
yd = [23, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29, 29, 30, 31]
S.append(qslide('yt', 15, 'Finding the median value from a dot plot', 'Edrolo 1F WE2a',
    'Consider the dot plot.<br><b>a.</b> Determine the median.', KI_MED,
    ['Count: $n = 28$ data points', (r'Median position $= \dfrac{28 + 1}{2} = $ 14.5th: average the 14th and 15th', 'dn:y15:15'),
     (r'$M = \dfrac{27 + 27}{2}$', 'dn:y15:15 dm:y15:13,14')],
    r'$\boldsymbol{M = 27}$', ED + ', 1F Worked example 2a. Working by teacher.',
    fig=dotplot('y15', yd, 22, 31), figw='1.2fr', cmd='<b>DETERMINE</b> · one value', ans_do='dn:y15:15 dm:y15:13,14'))

# Example 16 / You try 16: stem plots
temp = [('1', '8 9 9'), ('2', '0 2 5 7 8 9 9'), ('3', '1 3')]
S.append(qslide('ex', 16, 'Finding the median value from a stem plot', 'Cambridge · Example 16',
    'The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the median maximum temperature for these 12 days.',
    KI_MED, [r'Median position $= \dfrac{12 + 1}{2} = $ 6.5th: average the 6th and 7th',
             ('Count to the 6th and 7th values: 25 and 27', 'ln:s16:0:7 lm:s16:5,6'), (r'$M = \dfrac{25 + 27}{2}$', 'ln:s16:0:7 lm:s16:5,6')],
    r'$\boldsymbol{M = 26^\circ\text{C}}$', CG + ', 1F Example 16 (p. 46)',
    fig=stem('s16', temp, 'Key: 0 | 8 = 8°C'), figw='.85fr', cmd='<b>DETERMINE</b> · one value', ans_do='ln:s16:0:7 lm:s16:5,6'))
ed = [('40', '7'), ('41', ''), ('42', ''), ('43', ''), ('44', '4 6'), ('45', '1 3 3'), ('46', '2 6 7'), ('47', '4 7 8 9'), ('48', '0 0 4 5 6 8'), ('49', '1 2 5 5 5 9'), ('50', '3 4 4 7 8 8 9 9')]
S.append(qslide('yt', 16, 'Finding the median value from a stem plot', 'Edrolo 1F WE3a',
    'Consider the stem plot.<br><b>a.</b> Calculate the median.', KI_MED,
    ['Count: $n = 33$ data points', r'Median position $= \dfrac{33 + 1}{2} = $ 17th', ('Count along to the 17th value', 'ln:y16:0:17 lm:y16:16')],
    r'$\boldsymbol{M = 485}$', ED + ', 1F Worked example 3a. Working by teacher.',
    fig=stem('y16', ed, 'Key: 40 | 7 = 407'), figw='1.15fr', cmd='<b>CALCULATE</b> · one value', ans_do='ln:y16:0:17 lm:y16:16'))

# NL quartiles
def nl_q():
    def col(h, t, d, steps):
        return f'<div class="col"><h2>{h}</h2>{tiles(t, d)}' + ''.join(st(x, do=a or None, cls='stp').replace('st zs','st') for a, x in steps) + '</div>'
    A = [6, 2, 9, 1, 5, 7, 2, 6, 3]; B = [8, 3, 9, 2, 9, 4, 7, 3, 9, 8]
    ca = col('Odd number of values', 'a', A, [('sort:a', '<b>1</b> Order the data. $n = 9$'), ('tn:a:0:5 mid:a:0:8:mid', '<b>2</b> Median: count to the 5th value. <b>$M = 5$</b>'),
        ('tclr:a clr:a band:a:0:3:lo band:a:5:8:hi mid:a:4:4:mid', '<b>3</b> Split into halves. With an odd $n$, <b>leave the median out</b>.'),
        ('tn:a:0:3 mid:a:0:3:q', '<b>4</b> Lower half (4 values): 2.5th position. <b>$Q_1 = \\tfrac{2 + 2}{2} = 2$</b>'), ('tclr:a tn:a:5:3 mid:a:5:8:q', '<b>5</b> Upper half: 2.5th position. <b>$Q_3 = \\tfrac{6 + 7}{2} = 6.5$</b>'), ('', '<b>$\\text{IQR} = 6.5 - 2 = 4.5$</b>')])
    cb = col('Even number of values', 'b', B, [('sort:b', '<b>1</b> Order the data. $n = 10$'), ('tn:b:0:6 mid:b:0:9:mid', '<b>2</b> Median: count to the 5.5th position. <b>$M = \\tfrac{7 + 8}{2} = 7.5$</b>'),
        ('tclr:b clr:b band:b:0:4:lo band:b:5:9:hi mid:b:0:9:mid', '<b>3</b> Split into halves (5 values each), on the median line.'),
        ('tn:b:0:3 mid:b:0:4:q', '<b>4</b> Lower half (5 values): 3rd position. <b>$Q_1 = 3$</b>'), ('tclr:b tn:b:5:3 mid:b:5:9:q', '<b>5</b> Upper half: 3rd position. <b>$Q_3 = 9$</b>'), ('', '<b>$\\text{IQR} = 9 - 3 = 6$</b>')])
    return nl_slide('Quartiles cut the ordered data into quarters',
        r'Quartiles are just <b>medians of each half</b>. $\text{IQR} = Q_3 - Q_1$ is the spread of the middle 50%. <span class="hint">Click to find each quartile.</span>',
        f'<div class="cols" style="grid-template-columns:1fr 1fr">{ca}{cb}</div>', CG + ', 1F pp. 46–47. Data and steps by teacher (as in the 10MA deck).', 'eng')
S.append(nl_q())
# You try: full five-number summary (Edrolo 1E WE1), now after quartiles
S.append(qslide('yt', '', 'Five-number summary', 'Edrolo 1E WE1',
    'Construct a five-number summary for the following data.', KI_IQR,
    [('Order: $n = 10$; min $= 1$, max $= 10$', 'sort:f fill:f5:0 fill:f5:4'),
     (r'Median: 5.5th position, $M = \dfrac{6 + 6}{2} = 6$', 'sort:f tn:f:0:6 mid:f:0:9:mid fill:f5:0 fill:f5:4 fill:f5:2'),
     ('$n$ is even: five values in each half', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid fill:f5:0 fill:f5:4 fill:f5:2'),
     ('$Q_1$: 3rd value of the lower half $= 3$', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid tn:f:0:3 mid:f:0:4:q fill:f5:0 fill:f5:4 fill:f5:2 fill:f5:1'),
     ('$Q_3$: 3rd value of the upper half $= 8$', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid mid:f:0:4:q tn:f:5:3 mid:f:5:9:q fill:f5:0 fill:f5:4 fill:f5:2 fill:f5:1 fill:f5:3')],
    '<b>1, 3, 6, 8, 10</b> (min, $Q_1$, $M$, $Q_3$, max)', ED + ', 1E Worked example 1. Working by teacher.',
    fig=tiles('f', y14) + five('f5', [1, 3, 6, 8, 10]), figw='1fr', cmd='<b>CONSTRUCT</b> · min, $Q_1$, $M$, $Q_3$, max', cls='eng'))

# Example 17 / You try 17
S.append(qslide('ex', 17, 'Finding the range from a stem plot', 'Cambridge · Example 17',
    'The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the temperature range over these 12 days.',
    KI_RANGE, [('Lowest = 18, highest = 33', 'lx:s17:0,11'), (r'$R = 33 - 18$', 'lx:s17:0,11')],
    r'$\boldsymbol{R = 15^\circ\text{C}}$', CG + ', 1F Example 17 (p. 46)',
    fig=stem('s17', temp, 'Key: 0 | 8 = 8°C'), figw='.85fr', cmd='<b>DETERMINE</b> · one value with units', ans_do='lx:s17:0,11'))
nb = [('2', '2 3 5 7 9'), ('3', '0 1 3 5 7 7 8'), ('4', '0 1 2 2')]
S.append(qslide('yt', 17, 'Finding the range from a stem plot', 'Edrolo 1E WE2a',
    'The following stem plot displays the number of goals scored by 16 netball teams over a season.<br><b>a.</b> Calculate the range of goals scored.',
    KI_RANGE, [('Lowest = 22, highest = 42', 'lx:y17:0,15'), (r'$R = 42 - 22$', 'lx:y17:0,15')],
    r'$\boldsymbol{R = 20 \text{ goals}}$', ED + ', 1E Worked example 2a. Working by teacher.',
    fig=stem('y17', nb, 'Key: 2 | 2 = 22 goals'), figw='.85fr', cmd='<b>CALCULATE</b> · one value', ans_do='lx:y17:0,15'))

# Example 18 / You try 18 / Example 19
cats = [('1', '9'), ('2', '1 3 5 8'), ('3', '0 0 4 9 9'), ('4', '0 4 5 8'), ('5', '0 3'), ('6', '3 4')]
H18 = 'lm:s18:8,9 lb:s18:0:8:lo lb:s18:9:17:hi'
S.append(qslide('ex', 18, 'Finding the IQR from an ordered stem plot when n is even', 'Cambridge · Example 18',
    'Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.', KI_IQR,
    [('18 values: split on the median line, nine in each half', H18), ('Lower half: 5th value', H18 + ' lq:s18:4'),
     ('$Q_1 = 2.8$', H18 + ' lq:s18:4'), ('Upper half: 5th value', H18 + ' lq:s18:4,13'), ('$Q_3 = 4.8$', H18 + ' lq:s18:4,13'), (r'$\text{IQR} = 4.8 - 2.8$', H18 + ' lq:s18:4,13')],
    r'$\boldsymbol{\text{IQR} = 2.0 \text{ kg}}$', CG + ', 1F Example 18 (p. 47)',
    fig=stem('s18', cats, 'Weight (kg) · 1 | 2 represents 1.2 kg'), figw='.85fr', cmd='<b>FIND</b> · $Q_1$, $Q_3$, then IQR', ans_do=H18 + ' lq:s18:4,13'))
H18y = 'lm:y18:7,8 lb:y18:0:7:lo lb:y18:8:15:hi'
S.append(qslide('yt', 18, 'Finding the IQR from an ordered stem plot when n is even', 'Edrolo 1E WE2b',
    'The following stem plot displays the number of goals scored by 16 netball teams over a season.<br><b>b.</b> Calculate the IQR of goals scored.', KI_IQR,
    [('16 values: split on the median line, eight in each half', H18y), (r'$Q_1 = \dfrac{27 + 29}{2} = 28$', H18y + ' lq:y18:3,4'),
     (r'$Q_3 = \dfrac{38 + 40}{2} = 39$', H18y + ' lq:y18:3,4,11,12'), (r'$\text{IQR} = 39 - 28$', H18y + ' lq:y18:3,4,11,12')],
    r'$\boldsymbol{\text{IQR} = 11 \text{ goals}}$', ED + ', 1E Worked example 2b. Working by teacher.',
    fig=stem('y18', nb, 'Key: 2 | 2 = 22 goals'), figw='.85fr', cmd='<b>CALCULATE</b> · $Q_1$, $Q_3$, then IQR', ans_do=H18y + ' lq:y18:3,4,11,12'))
life = [('5', '2'), ('5', '5 6'), ('6', '4'), ('6', '6 6 7 9'), ('7', '1 2 2 3 3 4 4 4 4'), ('7', '5 5 6 6 7 7')]
H19 = 'lm:s19:11 lb:s19:0:10:lo lb:s19:12:22:hi'
S.append(qslide('ex', 19, 'Finding the IQR from an ordered stem plot when n is odd', 'Cambridge · Example 19',
    'The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.', KI_IQR,
    [('23 values: median position 12th. Count to it: 73', 'ln:s19:0:12 lm:s19:11'), ('$n$ is odd: leave the median out. 11 values below, 11 above.', H19),
     ('$Q_1$ = middle (6th) of the bottom 11 $= 66$', H19 + ' lq:s19:5'), ('$Q_3$ = middle (6th) of the top 11 $= 75$', H19 + ' lq:s19:5,17'),
     (r'$\text{IQR} = 75 - 66$', H19 + ' lq:s19:5,17')],
    r'$\boldsymbol{\text{IQR} = 9 \text{ years}}$', CG + ', 1F Example 19 (p. 48). No matching Edrolo worked example, so no You try.',
    fig=stem('s19', life, 'Stem: 5 | 2 = 52 years'), figw='.85fr', cmd='<b>FIND</b> · $Q_1$, $Q_3$, then IQR', ans_do=H19 + ' lq:s19:5,17'))

# Example 20 / You try 20 / exam MC
S.append(qslide('ex', 20, 'Finding the median and quartiles from a histogram', 'Cambridge · Example 20',
    'The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.', KI_MEDH,
    [r'Median position $= \dfrac{23 + 1}{2} = $ 12th value', ('Running totals from the left: 1, 3, 7, 12, …', 'hc:h20'),
     ('Median: the 12th value is in the 60–70 interval', 'hc:h20 hm:h20:5'),
     (r'$Q_1$: 11 values below the median, $\tfrac{11 + 1}{2} = $ 6th from the bottom: 50–60', 'hc:h20 hm:h20:5 hq:h20:4'),
     ('$Q_3$: 6th value from the top (2 + 6 = 8, so it is in the 80–90 interval)', 'hc:h20 hm:h20:5 hq:h20:4,7')],
    'Median 60–70 hours · $Q_1$ 50–60 hours · $Q_3$ 80–90 hours', CG + ', 1F Example 20 (p. 49)',
    fig=hist('h20', 10, 10, [1, 0, 0, 2, 4, 5, 3, 6, 2], 7, 1, 'internet hours per week'), figw='1.1fr', cmd='<b>FIND</b> · an interval for each'))
S.append(qslide('yt', 20, 'Finding the median and quartiles from a histogram', 'Edrolo 1F WE1a',
    'Consider the histogram.<br><b>a.</b> Estimate the median.', KI_MEDH,
    [r'Count: $3 + 15 + 12 + 13 + 9 + 5 + 2 = 59$', r'Median position $= \dfrac{59 + 1}{2} = $ 30th value',
     ('Running totals 3, 18, 30: the 30th value is in the 3–&lt;4 interval', 'hc:y20 hm:y20:2'), (r'Estimate the middle of the interval: $\dfrac{3 + 4}{2}$', 'hc:y20 hm:y20:2')],
    r'$\boldsymbol{M \approx 3.5}$', ED + ', 1F Worked example 1a. Working by teacher.',
    fig=hist('y20', 1, 1, [3, 15, 12, 13, 9, 5, 2], 16, 4, '', 'frequency'), figw='1.1fr', cmd='<b>ESTIMATE</b> · one value'))
OPTDIST['VCAA 2024 Exam 1 Q3'] = [18, 5, 7, 71]
S.append(qslide('exam', '', 'VCAA 2024 Exam 1 Q3', 'Median from a histogram',
    'The histogram below displays the population density, in people per km<sup>2</sup>, of the 27 countries in the European Union in 2021. The histogram has a logarithmic (base 10) scale.<br>The median value occurs in a column with a frequency of',
    KI_MEDH, [r'27 values: median position $= \dfrac{27 + 1}{2} = $ 14th value', ('Running totals: 2, 4, 6, 12, 21', 'hc:m3'),
              ('The 14th value is in the 2.0–2.2 column', 'hc:m3 hm:m3:5')],
    'frequency 9', 'VCAA 2024 General Mathematics Exam 1 Q3–4 stem and Q3; % from the examiner report. Histogram redrawn.',
    fig=hist('m3', 1.0, 0.2, [0, 2, 2, 2, 6, 9, 3, 1, 1, 0, 0, 1, 0], 10, 2, 'log<tspan baseline-shift="sub" font-size="11">10</tspan> (population density)', 'frequency'),
    figw='1.15fr', marks=1, cmd='<b>CHOOSE</b> · one option', vcaa=71, opts=[('A', '2'), ('B', '3'), ('C', '6'), ('D', '9')], key='D',
    dis=('A', '18% chose 2, the median of the <b>column heights</b> (1, 1, 1, 2, 2, 2, 3, 6, 9), not of the 27 <b>data values</b>. <span class="zsc">(likely reason: teacher comment)</span>')))

# Example 21 / You try 21 / exam MC
S.append(qslide('ex', 21, 'Calculating the mean from the formula', 'Cambridge · Example 21',
    'The following is a set of reaction times (in milliseconds). Write down the values of the following, correct to one decimal place.', KI_MEAN, [], None,
    CG + ', 1F Example 21 (p. 50)',
    parts=[('a', '$n$', [('Count the data values.', 'cnt:r21')], r'$\boldsymbol{n = 8}$', 'cnt:r21'),
           ('b', r'$\Sigma x$', [('Add them up.', 'cnt:r21 sum:r21')], r'$\boldsymbol{\Sigma x = 335}$', 'cnt:r21 sum:r21'),
           ('c', r'$\bar{x}$', [(r'$\bar{x} = \dfrac{\Sigma x}{n} = \dfrac{335}{8} = 41.875$', 'cnt:r21 sum:r21 bal:r21:41.875')], r'$\boldsymbol{\bar{x} = 41.9}$', 'cnt:r21 sum:r21 bal:r21:41.875')],
    fig=sumtiles("r21", [38, 36, 35, 43, 46, 64, 48, 25]), figw=".62fr", cmd='<b>WRITE DOWN</b> · three values', cls='tight'))
S.append(qslide('yt', 21, 'Calculating the mean from the formula', 'Edrolo 1G WE1',
    'The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.', KI_MEAN,
    [('Add the 10 amounts: $\\Sigma x = 273$', 'sum:y21'), ('Count: $n = 10$ customers', 'sum:y21 cnt:y21'), (r'$\bar{x} = \dfrac{273}{10} = 27.3$', 'sum:y21 cnt:y21 bal:y21:27.30')],
    'The mean amount spent is <b><span class="nomath">$</span>27.30</b>.', ED + ', 1G Worked example 1. Working by teacher.',
    fig=sumtiles('y21', ['11.60', '55.50', '7.95', '42.15', '17.10', '2.00', '82.55', '26.85', '5.40', '21.90']), figw='1fr',
    cmd='<b>CALCULATE</b> · one value in dollars', ans_do='sum:y21 cnt:y21 bal:y21:27.30'))
OPTDIST['VCAA 2024 Exam 1 Q14'] = [15, 68, 12, 5]
S.append(qslide('exam', '', 'VCAA 2024 Exam 1 Q14', 'Working back from a mean',
    'A school runs an orientation program for new staff each January. The time series plot below shows the number of new staff, <i>new</i>, for each year, <i>year</i>, from 2011 to 2022 (inclusive).'
    '<br>The number of new staff in 2023 is added to the total number of new staff from the previous 12 years. For these 13 years, the mean number of new staff is 11.<br>The number of new staff in 2023 is',
    KI_MEAN, [r'Total for 13 years $= 11 \times 13 = 143$', ('Total for 12 years $= 14 + 11 + 7 + \\cdots + 10 = 127$', 'tc:t14:' + ','.join(str(100 + c) for c in range(12))),
              r'2023 $= 143 - 127 = 16$'],
    '16 new staff',
    'VCAA 2024 General Mathematics Exam 1 Q13–14 stem and Q14; % and distractor from the examiner report. Time series plot shown as a table of its values (as in 12MAG 3A).',
    fig=table_hl('t14', [('<i>year</i>', [str(y) for y in range(2011, 2023)]), ('<i>new</i>', ['14', '11', '7', '6', '11', '13', '12', '6', '10', '15', '12', '10'])], 'ztab zsm2') + '<div class="zsc">(values read off the time series plot)</div>',
    figw='1.15fr', marks=1, cmd='<b>CHOOSE</b> · one option', vcaa=68, opts=[('A', '11'), ('B', '16'), ('C', '17'), ('D', '19')], key='B',
    dis=('A', '15% chose the mean itself, 11: the new value has to pull the total up to 143.')))

# NL house prices
S.append(f'<section class="slide z nl house">{bar("New learning", "Mean or median? House prices")}'
    '<div class="ctx">Eight houses sold in a suburb this year. Then one owner either <b>knocks the house down</b> and sells the empty block cheaply, '
    'or <b>builds a mansion</b> and sells it for millions. Drag the slider (or tap a button) to change that one sale price (the white dot). Which measure of centre still describes a <b>typical</b> house?</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>House sale prices ($ thousands)</h2>'
    '<svg class="zhs ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>Knocked down</span><input type="range" min="50" max="3000" step="10" value="760"><span>Mansion</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-v="120">Knock it down ($120k)</button><button data-v="760">Typical ($760k)</button><button data-v="1000">Renovated ($1m)</button><button data-v="2800">Mansion ($2.8m)</button></div></div>'
    '<div class="col"><h2>Live summary</h2><div class="zhso"></div>'
    '<div class="zrule">If the distribution is <b>symmetric and there are no outliers</b>, either the mean or the median can be used. '
    'If it is <b>clearly skewed and/or there are outliers</b>, it is more appropriate to use the <b>median</b>.</div></div></div>'
    f'{foot(CG + ", 1F p. 52 (rule). Fences: VCAA formula sheet. Prices made up by the teacher (as in the 10MA deck).")}</section>')
# NL SD
S.append(nl_slide('Standard deviation: spread around the mean',
    r'$s = \sqrt{\dfrac{\Sigma (x - \bar{x})^2}{n - 1}}$ &nbsp; roughly the typical distance of the values from the mean. <span class="hint">Drag to spread the data. The mean stays at 50.</span>',
    '<div class="cols" style="grid-template-columns:1.35fr .65fr"><div class="col"><h2>Eight test scores, mean 50</h2>'
    '<svg class="zsd ix" viewBox="0 0 700 260" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>bunched</span><input type="range" min="0" max="100" value="35"><span>spread out</span></div></div>'
    '<div class="col"><h2>Live</h2><div class="zsdo"></div></div></div>',
    CG + ', 1F p. 52 (formula). Scores made up by the teacher.', 'sdx'))

# CAS
TI = ('Lists &amp; Spreadsheet: name a list, enter the data.', 'Add Calculator › Menu › Statistics › Stat Calculations › One-Variable Statistics.',
      'Num of Lists: 1. X1 List: the list (Frequency List: 1, or the frequency column). OK.', r'Read $\bar{x}$, $s_x$, $n$, MinX, Q₁X, MedianX, Q₃X, MaxX.')
CP = ('Statistics app: name a list, enter the data.', 'Calc › One-Variable.', r'XList: main\list; Freq: 1 (or the frequency list). OK.', r'Read $\bar{x}$, $s_x$, $n$; scroll for minX, Q₁, Med, Q₃, maxX.')
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in TI)}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CP)}</ol></div></div>')
S.append(qslide('cas', '', 'Mean and standard deviation from a list', 'Cambridge · 1F CAS',
    'The following are the heights (in cm) of a group of women.<br>176 &nbsp;160 &nbsp;163 &nbsp;157 &nbsp;168 &nbsp;172 &nbsp;173 &nbsp;169<br>Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.',
    KI_CAS, ['Enter the 8 heights in one list.', 'One-Variable Statistics. Check $n = 8$.', r'$\bar{x} = 167.25$'],
    r'$\boldsymbol{\bar{x} = 167.25 \text{ cm},\ s_x = 6.67 \text{ cm}}$', CG + ', 1F pp. 53–54. CAS steps: planner CAS guide.',
    fig=TABS, figw='1fr', cmd='<b>DETERMINE</b> · two values, 2 d.p.'))
S.append(qslide('cas', '', 'Summary statistics from a frequency table', 'Data: Cambridge Example 15',
    'When values repeat (a dot plot or frequency table), enter each value once and its frequency in a second list. Check with the cricket team from Example 15:'
    '<table class="ztab z5b"><tr><th>age</th><td>18</td><td>19</td><td>22</td><td>23</td><td>24</td><td>25</td><td>29</td></tr><tr><th>freq</th><td>2</td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>1</td></tr></table>',
    KI_CAS, ['List 1: ages · list 2: frequencies', 'Select the frequency list in One-Variable Statistics.', 'Check $n = 13$ (the total frequency).', r'$\bar{x} = 22$, median $= 22$'],
    r'$\boldsymbol{s_x = 3.08}$', 'Data: ' + CG + ', 1F Example 15. CAS steps: planner CAS guide · ClassPad Help 402.',
    fig=TABS, figw='1fr', cmd='<b>CHECK</b> · $n$, $\\bar{x}$, $s_x$'))
S.append(qslide('yt', '', 'Mean and standard deviation on CAS', 'Edrolo 1G WE2',
    'The weight, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ weight, rounded to two decimal places.',
    KI_CAS, [('CAS: One-Variable Statistics on the list <i>weight</i>. Check $n = 10$.', 'cnt:rug'), (r'$\bar{x} = 88.5 \to 88.50$', 'cnt:rug sum:rug bal:rug:88.5'), r'$s_x = 7.230\ldots \to 7.23$'],
    r'mean $= \boldsymbol{88.50}$ kg, standard deviation $= \boldsymbol{7.23}$ kg', ED + ', 1G Worked example 2. Working by teacher.',
    fig=sumtiles('rug', [80, 95, 85, 91, 102, 93, 87, 78, 84, 90], '', 'check by hand: Σx'), figw='1fr', cmd='<b>DETERMINE</b> · two values, 2 d.p.'))

# Exit task: exam short answer
S.append(qslide('exit', '', 'Show what you know', 'VCAA 2020 Exam 2 Q4aii (adapted)',
    'The body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 orangutans are shown in the table.'
    + table_hl('ora', [('body density (kg/litre)', '1.07 1.07 1.08 1.08 1.03 1.05 1.07 1.06 1.07 1.09 1.02 1.09'.split()), ('weight (kg)', '70.1 90.4 73.2 85.0 84.3 95.6 71.7 95.0 80.2 87.4 94.9 65.3'.split())], 'ztab zv zora zinq')
    + 'For these 12 orangutans, determine the mean of their body density, in kilograms per litre.',
    KI_MEAN, [('Use only the <i>body density</i> row.', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1'),
              (r'CAS One-Variable Statistics, or $\Sigma x = 12.78$', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1'),
              (r'$\bar{x} = \dfrac{12.78}{12}$', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1')],
    r'$\boldsymbol{\bar{x} = 1.065 \text{ kg/litre}}$',
    ED + ', 1G Q11 · Adapted from VCAA 2020 Exam 2 Data analysis Q4aii (77% answered this type of question correctly). Working by teacher.',
    marks=1, cmd='<b>DETERMINE</b> · one value, not rounded', vcaa=77, figw='1.15fr', ans_do='tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1',
    watch='1.07 was not accepted. The examiners wanted 1.065: no rounding instruction means no rounding.'))

checkin(SC, "Success criteria: one per worked example")
coursework('1F', 'Coursework · Exercise 1F', [('Cambridge Exercise 1F', 'Q1–26'), ('Practice booklet', '1F section')],
           'Exercise 1F: Using summary statistics', CG + ", Exercise 1F")


build('S3-slides.html', '12MAG S3 · Measures of centre and spread · Slides')
