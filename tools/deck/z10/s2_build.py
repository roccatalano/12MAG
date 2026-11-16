r"""12MAG S2 (1C-1E Displaying and describing numerical data) rebuilt in the 10MA slide house style.
Built on the slide library tools/deck/z10/lib (rules: tools/deck/z10/HOWTO.md).
python3 tools/deck/z10/s2_build.py  ->  lessons/S2-slides.html
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.num import *
lesson('1C–1E Displaying numerical data')
# S2 = 1C-1E (planner card gm12-u3-s2). Content and verbatim questions from the old deck (git history) tools/deck/s2/build.py
# (sources checked against the PDFs on G: 15 Nov 2026). Ledger: every APK/exit item is burnt by S2 only.
#   APK: Cambridge U1&2 Ch 2 skills checklist 2C #6, 2D #7, 2D #9; Ch 9 checklist 9D #6, #7;
#        Edrolo U1&2 1C Q17 (adapted from VCAA 2016 Exam 2 Q1d, report: 52%), 1C Q15 (adapted from VCAA 2017 Exam 2 Q2b, report: 87%).
#   Examples: Cambridge U3&4 Examples 6-13. You trys: Edrolo U3&4 1C WE4, WE5, WE1, WE2; 1D WE1, WE3 (none for Examples 6 and 9).
#   CAS: planner/cas-skills.json histogram, dotplot (TI-Nspire only), logs.
#   Exits: Edrolo U3&4 1C Q16 = VCAA 2020 Exam 2 Q2a (93%), 1C Q18 = VCAA 2016 Exam 1 Q3 (87/9/1/2/1),
#          1D Q13 = VCAA 2019 Exam 1 Q3 (7/6/7/71/9). Original VCAA wording.
import math

KI_PCT = r'$\text{percentage frequency} = \dfrac{\text{count}}{\text{total}} \times 100\%$'
KI_INT = 'Intervals: no gaps, no overlaps, about 5 to 15 of them, starting at an exact value.'
KI_HIST = 'Bars <b>touch</b>. Each bar is one interval; its height is the frequency.'
KI_SOCS = '<b>SOCS</b>: Shape · Outliers · Centre · Spread, one sentence each.'
KI_DOT = 'One dot per value on a scaled, labelled number line. Equal values <b>stack</b>.'
KI_STEM = 'Stem = leading digits, leaf = last digit. Order the leaves. <b>Always a key.</b>'
KI_MODE = 'Mode = the value that occurs most often (the tallest stack, the most repeated leaf).'
KI_LOG = r'$\log_{10} x = b \iff 10^{b} = x$<div class="kn">undo a log: $x = 10^{\text{log}}$</div>'
KI_LOGH = r'A value $v$ on a $\log_{10}$ scale stands for the number $10^{v}$.'

# ---- title + lesson overview
title_slide('Displaying and describing numerical data', ['1C Displaying and describing numerical data (pp. 14–27)', '1D Dot plots and stem plots (pp. 28–33)', '1E Using a logarithmic (base 10) scale to display data (pp. 34–40)'])
LI = ['To be able to construct frequency tables for discrete numerical data.', 'To be able to construct frequency tables for grouped numerical data (discrete and continuous).',
      'To be able to construct a histogram from a frequency table for numerical data.', 'To be able to construct a histogram from numerical data using a CAS calculator.',
      'To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.',
      'To be able to construct a dot plot for numerical data.', 'To be able to construct a stem plot for numerical data.',
      'To be able to revise the concept of log<sub>10</sub> <i>x</i>.', 'To be able to investigate the effect of the logarithmic scale on the features of a distribution.']
SC = ['I can construct a frequency table for discrete numerical data.', 'I can construct a grouped frequency table.', 'I can construct a histogram from a grouped frequency table.',
      'I can describe the features of a distribution from a histogram.', 'I can construct a dot plot.', 'I can construct a stem plot.',
      'I can use a CAS calculator to find logs.', 'I can interpret a histogram with a log scale.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Frequency tables · Examples 6–7', 'Histograms · Example 8 · CAS',
       'Shape and SOCS · Example 9', 'Dot plots · Example 10 · CAS', 'Stem plots · Example 11', 'Logs · Example 12 · CAS',
       'Log scales · Example 13', 'Exit tasks', 'Check-in and coursework']
overview('1C–1E', LI, SC, SEQ, CG + ", 1C, 1D, 1E Learning intentions; success criteria: one per worked example", cols='1.15fr 1fr .8fr', cls='s2li')

# ---- APK 1: Cambridge U1&2 2C #6 + 2D #7 (AFL games)
AFL = [266, 259, 238, 227, 210, 160, 160, 159, 155, 145, 133, 99, 91, 80, 80, 75, 73, 58, 42, 36, 32, 25, 32, 25, 25, 21, 17, 13, 10, 9, 9, 4, 2]
AV = [sum(1 for v in AFL if 20 * b <= v < 20 * b + 20) for b in range(14)]
nz = [i for i, f in enumerate(AV) if f]
S.append(qslide('apk', '1 of 5', 'Year 11 skills: histogram and shape', 'Cambridge U1&amp;2 · 2C #6, 2D #7',
    'The following data gives the number of games played in total by each member of an AFL club:' + dlist('afl', AFL, 11, 'ztab zdl2 zsm3'),
    KI_HIST, [], None,
    CG12 + ', Chapter 2 skills checklist 2C #6 and 2D #7. Working by teacher.',
    parts=[('a', 'Use a CAS calculator to construct a histogram starting at 0 with column width 20.',
            [('CAS: Histogram, column width 20, start 0. Copy the bars.', bars('afh', nz))], 'Histogram (left): width 20, starting at 0.', bars('afh', nz)),
           ('b', 'Describe the shape of the histogram of the number of games played (above).',
            [('Most players have under 100 games; a long tail runs out to the right.', bars('afh', nz) + ' hq:afh:0,1')],
            'The distribution is <b>positively skewed</b>.', bars('afh', nz) + ' hq:afh:0,1')],
    fig=hist('afh', 0, 20, AV, 8, 2, 'number of games played', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1fr', cls='tight'))

# ---- APK 2: Cambridge U1&2 2D #9 (party ages, stem plot)
PA = [19, 21, 22, 56, 34, 19, 27, 28, 34, 17, 66, 37, 20, 20, 21, 45, 26, 19, 23, 29]
prow, pmp = stemmap(PA, range(1, 7), True)
pst = lambda test: J2(sorted(pmp[i] for i in where(PA, test)))
S.append(qslide('apk', '2 of 5', 'Year 11 skills: a stem plot', 'Cambridge U1&amp;2 · 2D #9',
    'Construct a stem plot of the ages of a group of people at a party:' + dlist('pa', PA, 10),
    KI_STEM,
    ['Ages run from 17 to 66: the tens digits 1 to 6 are the stems.',
     ('Teens: leaves 7, 9, 9, 9', f'tc:pa:{dk(10, where(PA, lambda v: v < 20))} xl:pas:{pst(lambda v: v < 20)}'),
     ('Twenties: leaves 0 0 1 1 2 3 6 7 8 9', f'tc:pa:{dk(10, where(PA, lambda v: v < 30))} xl:pas:{pst(lambda v: v < 30)}'),
     ('Thirties to sixties: 4 4 7 · 5 · 6 · 6', f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)}'),
     ('Write the key: 1 | 7 = 17, <i>age</i> (years)', f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)} sk:pas')],
    'Ordered stem plot (left) with the key <b>1 | 7 = 17</b>.',
    CG12 + ', Chapter 2 skills checklist 2D #9. Working by teacher.',
    fig=stem('pas', prow, 'Key: 1 | 7 = 17 &nbsp; <i>age</i> (years)', build=True).replace('class="zstem"', 'class="zstem zbuild"'), figw='.9fr',
    ans_do=f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)} sk:pas', cls=''))

# ---- APK 3: Cambridge U1&2 9D #6, #7 (logs)
S.append(qslide('apk', '3 of 5', 'Year 11 skills: logs and powers of ten', 'Cambridge U1&amp;2 · 9D #6, #7',
    'Answer each part.', KI_LOG, [], None, CG12 + ', Chapter 9 skills checklist 9D #6 and #7. Working by teacher.',
    parts=[('a', 'Find the log of 592 to two decimal places.', [r'CAS: $\log_{10}(592) = 2.7723\ldots$'], r'$\boldsymbol{2.77}$'),
           ('b', 'What is the order of magnitude of 478 000?', [r'$478\,000 = 4.78 \times 10^{5}$'], 'order of magnitude <b>5</b>')]))

# ---- APK 4: Edrolo U1&2 1C Q17 (adapted from VCAA 2016 E2 Q1d)
GL = [0] * 16 + [0.3, 0.6, 1.2, 1.6, 1.6, 2.2, 2.6, 3.2, 6.4, 7.2, 7.8, 12.4, 16.8, 17.8]
GB = [sum(1 for v in GL if 2 * b <= v < 2 * b + 2) for b in range(9)]
GO = 'xb:goh:0'
S.append(qslide('apk', '4 of 5', 'A real VCAA question you can already do', 'VCAA 2016 Exam 2 Q1d (adapted)',
    'The following dot plot shows the average number of goals scored per season by each player within a soccer club.<br>'
    'Use the grid to construct a histogram that displays the distribution of the average number of goals scored per season at the soccer club. Use interval widths of two with the first interval starting at 0.',
    KI_HIST,
    [('0 to &lt;2: <b>21</b> (16 at 0, 5 more)', f'xb:goh:0'),
     ('2 to &lt;4: <b>3</b> · 4 to &lt;6: <b>0</b> · 6 to &lt;8: <b>3</b>', f'xb:goh:0,1,3'),
     ('12 to &lt;14: <b>1</b> · 16 to &lt;18: <b>2</b> · total 30 ✓', f'xb:goh:0,1,3,6,8')],
    'Histogram (left, lower): frequencies 21, 3, 0, 3, 0, 0, 1, 0, 2.',
    ED12 + ', 1C Q17 (adapted from VCAA 2016 Exam 2 Data analysis Q1d; % from the examiner report, original question). Working by teacher.',
    fig=f'<svg class="zdp" id="gd" data-v="{json.dumps(GL)}" data-lo="0" data-hi="19" data-xl="average goals scored" viewBox="0 0 640 262"></svg>'
        + hist('goh', 0, 2, GB, 22, 2, 'average goals scored', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'),
    marks=2, vcaa=52, figw='1.6fr', ans_do=f'xb:goh:0,1,3,6,8',
    watch='widths of <b>two</b> from 0: the examiners reported many students drew widths of one.'))

# ---- APK 5: Edrolo U1&2 1C Q15 (adapted from VCAA 2017 E2 Q2b)
MR = [('1', '8'), ('2', '2 2 4 4 4'), ('2', '5 5 9'), ('3', '0 0 1 2 3 4'), ('3', '6 8'), ('4', '0 3')]
S.append(qslide('apk', '5 of 5', 'And another', 'VCAA 2017 Exam 2 Q2b (adapted)',
    'The following stem plot displays the <i>wingspan</i>, in millimetres, of 19 moths that were captured.<br>Write down the modal <i>wingspan</i>, in millimetres, of the moths captured.',
    KI_MODE,
    [('Leaf 4 appears three times on the first 2 stem. No other value appears more than twice.', 'lx:mo:3,4,5'), ('Key: 2 | 4 = 24 mm', 'lx:mo:3,4,5')],
    'The modal wingspan is <b>24 mm</b>.',
    ED12 + ', 1C Q15 (adapted from VCAA 2017 Exam 2 Data analysis Q2b; % from the examiner report, original question). Working by teacher.',
    fig=stem('mo', MR, 'Key: 1 | 2 = 12 &nbsp; <i>wingspan</i> (mm)'), marks=1, vcaa=87, figw='1fr', ans_do='lx:mo:3,4,5',
    watch='the mode is the <b>value</b> (24 mm), not how many times it occurs (3). <span class="zsc">(teacher note)</span>'))

# ---- Key ideas
KD = [('Histogram', 'columns that touch; each column is an interval, its height the frequency'),
      ('Dot plot', 'a number line with a dot for each value; equal values stack'),
      ('Stem plot', 'each value split into a stem (leading digits) and a leaf (last digit), with a key'),
      ('Shape', 'symmetric, positively skewed (long upper tail) or negatively skewed (long lower tail)'),
      ('Outlier', 'a value that stands out from the rest of the data'),
      ('Log scale', 'an axis in powers of 10, for data ranging over several orders of magnitude')]
KF = [('Percentage frequency', r'$\dfrac{\text{count}}{\text{total}} \times 100\%$ &nbsp;<span class="zn">count = number of values in the interval</span>'),
      ('Log of a number', r'$\log_{10} x = b \iff 10^{b} = x$ &nbsp;<span class="zn">$\log_{10} 100 = 2$, since $10^2 = 100$</span>'),
      ('Number from its log', r'$\text{number} = 10^{\text{log}}$ &nbsp;<span class="zn">log 3.4 → $10^{3.4}$</span>'),
      ('Describe: SOCS', 'Shape · Outliers · Centre · Spread')]
S.append(f'<section class="slide z kif">{bar("1C–1E", "Key ideas")}<div class="cols" style="grid-template-columns:1.1fr .9fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1C pp. 14–23, 1D pp. 28–31, 1E pp. 34–36")}</section>')

# ---- NL: grouped frequency table (27 marks, Cambridge 1C CAS 1 data)
MK = [16, 11, 4, 25, 15, 7, 14, 13, 14, 12, 15, 13, 16, 14, 15, 12, 18, 22, 17, 18, 23, 15, 13, 17, 18, 22, 23]
MI = ['2–5', '6–9', '10–13', '14–17', '18–21', '22–25']; MN = [sum(1 for v in MK if 2 + 4 * b <= v <= 5 + 4 * b) for b in range(6)]
def mstep(b, tid, extra=''):
    ix = where(MK, lambda v: 2 <= v <= 5 + 4 * b)
    return f'tc:mk{tid}:{dk(9, ix)} ' + fills('mt' + tid, [k for r in range(b + 1) for k in rowk(r, 2)]) + extra
S.append(nl_slide('Grouped frequency tables',
    'Many different values, or continuous data? Group them into <b>intervals</b>. <span class="hint">Click to count the 27 marks into the table.</span>',
    '<div class="cols" style="grid-template-columns:1fr .75fr 1fr"><div class="col"><h2>Data: “the following set of 27 marks” (Cambridge 1C CAS 1)</h2>' + dlist('mk1', MK, 9) +
    '<ul class="zul s2rules"><li>every value in exactly one interval: no gaps, no overlaps</li><li>about 5 to 15 intervals</li><li>start on an exact value</li><li><b>2–5</b> (whole marks) = 2, 3, 4 or 5 · <b>30.0–34.9</b> = 30.0 up to 34.9</li></ul></div>'
    '<div class="col">' + ftab('mt1', ['<i>marks</i>', 'Frequency'], [(a, f) for a, f in zip(MI, MN)] + [('<b>Total</b>', '<b>27</b>')]) + '</div><div class="col">'
    + st('<b>1</b> Width 4, starting at 2: 2–5, 6–9, …, 22–25', do=fills('mt1', [r * 10 for r in range(6)]))
    + st('<b>2</b> 2–5: <b>1</b> · 6–9: <b>1</b> · 10–13: <b>6</b>', do=mstep(2, '1'))
    + st('<b>3</b> 14–17: <b>11</b> · 18–21: <b>3</b> · 22–25: <b>5</b>', do=mstep(5, '1'))
    + st('<b>4</b> Total: 1 + 1 + 6 + 11 + 3 + 5 = <b>27</b> ✓', do=mstep(5, '1', ' ' + fills('mt1', rowk(6, 2))))
    + '</div></div>', CG + ', 1C pp. 14–16 (27 marks: CAS 1, p. 16)'))

# ---- Example 6 (Cambridge)
BED = [2, 3, 4, 3, 3, 4, 3, 4, 4, 1, 3, 2, 1, 2, 2, 2, 4, 5, 3, 4, 4, 5, 3, 4]
bc = [BED.count(v) for v in range(1, 6)]; bp = [f'{100 * c / 24:.1f}' for c in bc]
B6 = [(str(v), bc[v - 1], bp[v - 1]) for v in range(1, 6)] + [('<b>Total</b>', '<b>24</b>', '<b>99.9</b>')]
F6a = fills('t6', [r * 10 for r in range(6)])
F6b = F6a + ' ' + fills('t6', [r * 10 + 1 for r in range(6)])
S.append(qslide('ex', 6, 'Constructing a frequency table for discrete numerical data', 'Cambridge · Example 6',
    'The number of bedrooms in each of the 24 properties sold in a certain area over a one month period are as follows:' + dlist('bd', BED, 12) +
    'Construct a table for these data showing both frequency and percentage frequency, giving the values of the percentage frequency rounded to one decimal place.',
    KI_PCT,
    [('Smallest 1, largest 5: one row for each of 1, 2, 3, 4, 5.', F6a),
     ('Count each value: 2, 5, 7, 8, 2 · total 24', F6b + f' tc:bd:{dk(12, range(24))}'),
     (r'Percentage for 1 bedroom: $\dfrac{2}{24} \times 100\% = 8.3\%$', F6b + ' fill:t6:2'),
     ('The rest: 20.8, 29.2, 33.3, 8.3 · total 99.9 (rounding)', F6b + ' ' + fills('t6', [r * 10 + 2 for r in range(6)]))],
    'The frequency table (left).', CG + ', 1C Example 6 (p. 14)',
    fig=ftab('t6', ['Number of bedrooms', 'Number', '%'], B6), figw='1fr', cls='tight',
    ans_do=F6b + ' ' + fills('t6', [r * 10 + 2 for r in range(6)])))

# ---- Example 7 (Cambridge)
HRS = [35.0, 48.0, 45.0, 43.0, 38.2, 50.0, 39.8, 40.7, 40.0, 50.0, 35.4, 38.8, 40.2, 45.0, 45.0, 40.0, 43.0, 48.8, 43.3, 53.1, 35.6, 44.1, 34.8]
HI = ['30.0–34.9', '35.0–39.9', '40.0–44.9', '45.0–49.9', '50.0–54.9']; hk = lambda v: int((v - 30) // 5)
HN = [sum(1 for v in HRS if hk(v) == b) for b in range(5)]; HP = [f'{100 * n / 23:.1f}' for n in HN]
F7a = fills('t7', [r * 10 for r in range(6)])
F7b = F7a + ' ' + fills('t7', [r * 10 + 1 for r in range(6)])
S.append(qslide('ex', 7, 'Constructing a grouped frequency table', 'Cambridge · Example 7',
    'The data below give the average hours worked per week in 23 countries.' + dlist('hr', [f'{v:.1f}' for v in HRS], 8) + 'Construct a grouped frequency table with five intervals.',
    KI_INT,
    [('Smallest 34.8, largest 53.1: five intervals of width 5, from 30.0–34.9 to 50.0–54.9', F7a),
     ('Count 30.0–34.9 and 35.0–39.9: 1 · 6', F7a + ' ' + fills('t7', [1, 11]) + f' tc:hr:{dk(8, where(HRS, lambda v: hk(v) <= 1))}'),
     ('Count the rest: 8 · 5 · 3 · total 23', F7b + f' tc:hr:{dk(8, range(23))}'),
     (r'Percentages: $\dfrac{1}{23} \times 100\% = 4.3\%$, then 26.1, 34.8, 21.7, 13.0', F7b + ' ' + fills('t7', [r * 10 + 2 for r in range(6)]))],
    'The grouped frequency table (left).', CG + ', 1C Example 7 (p. 15)',
    fig=ftab('t7', ['Average hours worked', 'Number', '%'], [(a, n, p) for a, n, p in zip(HI, HN, HP)] + [('<b>Total</b>', '<b>23</b>', '<b>99.9</b>')]), figw='.9fr',
    ans_do=F7b + ' ' + fills('t7', [r * 10 + 2 for r in range(6)])))

# ---- You try 7: Edrolo 1C WE4
PL = [32.0, 40.2, 40.5, 45.1, 47.0, 49.1, 50.1, 53.7, 54.2, 55.3, 56.9, 57.2, 58.2, 67.2, 68.9, 69.0, 72.3, 77.6, 82.1, 88.5]
PI = ['30.0–39.9', '40.0–49.9', '50.0–59.9', '60.0–69.9', '70.0–79.9', '80.0–89.9']; pk = lambda v: int((v - 30) // 10)
PN = [sum(1 for v in PL if pk(v) == b) for b in range(6)]; PP = [str(5 * n) for n in PN]
FYa = fills('ty7', [r * 10 for r in range(7)]); FYb = FYa + ' ' + fills('ty7', [r * 10 + 1 for r in range(7)])
S.append(qslide('yt', 7, 'Constructing a grouped frequency table', 'Edrolo 1C WE4',
    'The <i>height</i> (cm) of 20 plants in a Year 6 science experiment were recorded.' + dlist('pl', [f'{v:.1f}' for v in PL], 7) + 'Construct a grouped frequency table with intervals of 10.',
    KI_INT,
    [('Smallest 32.0 → start at 30.0 · largest 88.5 → last interval 80.0–89.9: six intervals', FYa),
     ('Count: 1 · 5 · 7 · 3 · 2 · 2 · total 20', FYb + f' tc:pl:{dk(7, range(20))}'),
     (r'Percentages: $\dfrac{1}{20} \times 100\% = 5\%$, then 25, 35, 15, 10, 10', FYb + ' ' + fills('ty7', [r * 10 + 2 for r in range(7)]))],
    'The grouped frequency table (left).', ED + ', 1C Worked example 4 (intervals written Cambridge style). Working by teacher.',
    fig=ftab('ty7', ['<i>height</i> (cm)', 'number', '%'], [(a, n, p) for a, n, p in zip(PI, PN, PP)] + [('<b>total</b>', '<b>20</b>', '<b>100</b>')]), figw='.9fr',
    ans_do=FYb + ' ' + fills('ty7', [r * 10 + 2 for r in range(7)])))

# ---- NL: the histogram (same 27 marks)
S.append(nl_slide('The histogram: table → graph',
    'A <b>histogram</b> shows a grouped frequency table. The bars <b>touch</b> because the scale is continuous. <span class="hint">Click to grow the bars.</span>',
    '<div class="cols" style="grid-template-columns:.68fr 1.1fr 1.15fr"><div class="col">' + ftab('mt2', ['<i>marks</i>', 'Frequency'], [(a, f) for a, f in zip(MI, MN)] + [('<b>Total</b>', '<b>27</b>')]).replace('zft zfill', 'zft ztab') +
    '</div><div class="col">' + hist('mh2', 2, 4, MN, 12, 2, 'marks', 'frequency').replace('class="zhg"', 'class="zhg zbuild"') + '</div><div class="col">'
    + st('<b>1</b> Axes: <i>marks</i> across (2, 6, 10, …); frequency up, to 12.')
    + ''.join(st(f'<b>{i + 2}</b> {MI[i]}: frequency {MN[i]} → bar from {2 + 4 * i} to {6 + 4 * i}, height {MN[i]}', do=f'xb:mh2:{J2(range(i + 1))} tc:mt2:{dk(10, [i * 10, i * 10 + 1])}'.replace(dk(10,[i*10,i*10+1]), f'{i*10},{i*10+1}')) for i in range(6))
    + st('<b>Check:</b> heights add to 27 ✓', True, do='xb:mh2:0,1,2,3,4,5')
    + '</div></div>', CG + ', 1C pp. 15–16 (27 marks: CAS 1, p. 16)', 's2hg'))

# ---- Example 8 (Cambridge)
HV = [1, 6, 8, 5, 3]
S.append(qslide('ex', 8, 'Constructing a histogram from a frequency table', 'Cambridge · Example 8',
    'Construct a histogram for the frequency table opposite.' + table_hl('t8', [('Average hours worked', HI), ('Frequency', [str(x) for x in HV])], 'ztab zinq'),
    KI_HIST,
    ['Axes: <i>Average hours worked</i> across (30, 35, …); <i>Frequency</i> up, to at least 8.',
     *[(f'{HI[i]}: frequency {HV[i]} → bar {30 + 5 * i} to {35 + 5 * i}, height {HV[i]}', f'xb:h8:{J2(range(i + 1))} tc:t8:{i},{100 + i}') for i in range(5)]],
    'The histogram (left): bars touch, both axes labelled.', CG + ', 1C Example 8 (p. 16)',
    fig=hist('h8', 30, 5, HV, 9, 1, 'Average hours worked', 'Frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1.1fr',
    ans_do='xb:h8:0,1,2,3,4'))

# ---- You try 8: Edrolo 1C WE5 (a and b on two slides, as Example 13)
YT8Q = ('The <i>height</i> (cm) of 20 plants in a Year 6 science experiment was recorded in the following grouped frequency table.'
    + table_hl('ty8', [('<i>height</i> (cm)', PI), ('number', [str(x) for x in PN]), ('%', PP)], 'ztab zinq zsm2'))
S.append(qslide('yt', '8 (a)', 'Constructing a histogram from a frequency table', 'Edrolo 1C WE5',
    YT8Q, KI_HIST, [], None, ED + ', 1C Worked example 5 a (intervals written Cambridge style). Working by teacher.',
    parts=[('a.', 'Construct a histogram to display this data.',
            [(f'{PI[i]}: {PN[i]} → bar {30 + 10 * i} to {40 + 10 * i}, height {PN[i]}', f'xb:yh8:{J2(range(i + 1))} tc:ty8:{i},{100 + i}') for i in range(6)],
            'Histogram (left).', 'xb:yh8:0,1,2,3,4,5')],
    fig=hist('yh8', 30, 10, PN, 8, 1, 'height (cm)', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1.1fr', cls='tight'))
S.append(qslide('yt', '8 (b)', 'Constructing a histogram from a frequency table', 'Edrolo 1C WE5',
    YT8Q.replace("'ty8'", "'ty8b'").replace('id="ty8"', 'id="ty8b"'), KI_HIST, [], None, ED + ', 1C Worked example 5 b. Working by teacher.',
    parts=[('b.', 'What percentage of plants were shorter than 60 cm?',
            [('Shorter than 60 cm: the first three intervals.', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2'),
             ('Add their percentages: 5 + 25 + 35', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2,200,201,202')],
            '<b>65%</b> of plants were shorter than 60 cm.', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2,200,201,202')],
    fig=hist('yh8b', 30, 10, PN, 8, 1, 'height (cm)', 'frequency'), figw='1.1fr', cls='tight'))

# ---- CAS: histogram (Cambridge 1C CAS 1, 27 marks)
S.append(qslide('cas', '', 'Constructing a histogram from raw data', 'Cambridge · 1C CAS 1',
    'Display the following set of 27 marks in the form of a histogram.' + dlist('mk3', MK, 14, 'ztab zdl2 zsm3') +
    'Enter the data into a list named <b>marks</b>, then change the column (bin) width to <b>4</b> and the starting point to <b>2</b>.',
    'Set the <b>width</b> and the <b>start</b> yourself: the calculator’s default bins are rarely the ones asked for.',
    ['Enter the 27 marks in a list named <i>marks</i>.', 'Draw the histogram, then set width 4, start 2.',
     'Read each bar (hover or trace): 1, 1, 6, 11, 3, 5'],
    'Same histogram as the table → graph slide: 2–5 has 1, …, 14–17 has 11, 22–25 has 5.', CG + ', 1C pp. 16–20 (CAS 1). CAS steps: planner CAS guide.',
    fig=casbox('histogram'), figw='1.15fr', cls='s2cas'))

# ---- NL: shape
def mini(id_, v, ym=10):
    return hist(id_, 0, 1, v, ym, 5, '', '').replace('class="zhg"', 'class="zhg zmini"')
SHP = [('Symmetric', 'tails off evenly on either side of the peak', [1, 2, 4, 7, 9, 7, 4, 2, 1]),
       ('Positively skewed', 'long <b>upper</b> tail, to the right', [3, 9, 8, 6, 4, 3, 2, 1, 1]),
       ('Negatively skewed', 'long <b>lower</b> tail, to the left', [1, 1, 2, 3, 4, 6, 8, 9, 3]),
       ('With an outlier', 'a value well away from the rest', [0, 3, 7, 9, 6, 2, 0, 0, 1])]
MM = ['mean ≈ median', '<b>mean &gt; median</b> (the tail pulls the mean up)', '<b>mean &lt; median</b>', 'the mean is pulled towards the outlier, and the median barely moves']
S.append(nl_slide('Shape: which way is the tail?',
    'Look at the <b>tail</b>: it names the skew. <span class="hint">Click to reveal each shape.</span>',
    '<div class="s2shp">' + ''.join(f'<div class="zpc">' + st(f'<div class="zpt">{a}</div>' + mini(f'shp{k}', v) + f'<div class="s2c">{b}</div><div style="font-size:24px;line-height:1.25;margin-top:10px;padding-top:8px;border-top:2px dotted #999">{MM[k]}</div>') + '</div>' for k, (a, b, v) in enumerate(SHP)) + '</div>'
    + st('Salaries and house prices are usually positively skewed. Age at death is negatively skewed.', True, cls='zctr'),
    CG + ', 1C p. 21 (shapes and mean/median notes by the teacher)'))

# ---- NL: SOCS
SOCSL = [('S', 'Shape', 'The distribution is symmetric / positively skewed / negatively skewed.'),
         ('O', 'Outliers', 'There are no outliers / is an outlier at … / are outliers at …'),
         ('C', 'Centre', 'The distribution is centred at <i>value</i>, the median / mean / mode.'),
         ('S', 'Spread', 'The range / IQR is <i>value</i>. Most values lie between <i>a</i> and <i>b</i>.')]
S.append(nl_slide('Describing a distribution: SOCS, like a sock',
    'Describe numerical data in this order, one sentence for each letter. <span class="hint">Click for each line.</span>',
    '<div class="s2socs">' + ''.join(st(f'<span class="s2L">{l}</span><b>{n}</b> &nbsp; {t}') for l, n, t in SOCSL) + '</div>'
    + st('Skewed, or outliers? Give the <b>median</b> and the <b>IQR</b>: outliers don’t affect them. From a histogram, the centre and spread are only estimates.', True, cls='zctr'),
    CG + ', 1C pp. 21–23 (SOCS order: class convention)'))

# ---- Example 9 (Cambridge)
GV = [2, 2, 2, 2, 2, 2, 2, 4, 6, 10, 16, 34, 95, 233, 300, 207, 86, 4]
S.append(qslide('ex', 9, 'Describing the features of a distribution from a histogram', 'Cambridge · Example 9',
    'The histogram shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe this histogram in terms of shape, centre, spread and outliers.',
    KI_SOCS,
    ['<div class="zpart s2tpl" id="tp9"><span class="zok">✓ Answer</span> The distribution is <span class="s2b" data-b="0">negatively</span> skewed. There are <span class="s2b" data-b="1">possible outliers below 34 weeks</span>. It is centred at around <span class="s2b" data-b="2">38–39 weeks</span>, the median. The values range from <span class="s2b" data-b="3">25</span> to <span class="s2b" data-b="3">42</span> weeks; most lie between <span class="s2b" data-b="3">36</span> and <span class="s2b" data-b="3">41</span> weeks.</div>',
     ('<b>S</b> The bars tail off to the left: a long lower tail.', 'bf:tp9:0 hq:h9:0,1,2,3,4,5,6,7,8,9,10'),
     ('<b>O</b> Bars below 34 weeks are tiny next to the rest.', 'bf:tp9:0,1 hq:h9:0,1,2,3,4,5,6,7,8'),
     ('<b>C</b> The middle (500th baby) falls in 38–39 weeks.', 'bf:tp9:0-2 hm:h9:13,14'),
     ('<b>S</b> Lowest bar 25, highest 42; the tall bars 36 to 41.', 'bf:tp9:0-3 hq:h9:11,12,13,14,15,16')],
    '', 
    CG + ', 1C Example 9 (pp. 23–24); Cambridge’s solution set out in SOCS order; histogram redrawn',
    fig=hist('h9', 25, 1, GV, 300, 50, 'Gestation period (weeks)', 'Frequency'), figw='1.15fr', cls='tight', ans_do='bf:tp9:0-3 hq:h9:11,12,13,14,15,16 bok:tp9').replace('<span class="zok">✓ Answer</span> </div>', '</div>').replace('class="st zs final "', 'class="st zs final s2hid"'))

# ---- NL: dot plots and stem plots
DPV = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7]
S.append(nl_slide('Dot plots and stem plots',
    'Two quick, by-hand displays for small data sets. Both show <b>every</b> data value. <span class="hint">Click for each display.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>Dot plot</h2>'
    + f'<svg class="zdp zbuild" id="nld" data-v="{json.dumps(sorted(DPV))}" data-lo="1" data-hi="8" data-xl="board games owned" viewBox="0 0 640 262"></svg>'
    + st('A number line with one dot per value. Equal values <b>stack</b>. Best for small, discrete data sets.', do='xd:nld:0-10') + '</div>'
    '<div class="col"><h2>Stem plot</h2>' + stem('nls', [('4', '3 5 5 5 7'), ('5', '1 3 6 8'), ('6', '7 9'), ('7', '1'), ('8', '0 1 3 9 9'), ('9', '1 4')], 'Key: 4 | 3 = 43', build=True).replace('class="zstem"', 'class="zstem zbuild"')
    + st('Stem = leading digits, leaf = last digit. Leaves in order, empty stems kept.', do='xl:nls:0-18') + st('<b>Always a key</b>: 4 | 3 = 43.', do='xl:nls:0-18 sk:nls') + '</div></div>',
    CG + ', 1D pp. 28–31 · ' + ED + ', 1C (example plots)'))

# ---- Example 10 (Cambridge)
CR = [22, 19, 18, 19, 23, 25, 22, 29, 18, 22, 23, 24, 22]
S.append(qslide('ex', 10, 'Constructing a dot plot', 'Cambridge · Example 10',
    'The ages (in years) of the 13 members of a cricket team are:' + dlist('cr', CR, 13) + 'Construct a dot plot.',
    KI_DOT,
    ['Draw a number line scaled to include all values (17 to 30); label it <i>Age (years)</i>.',
     ('18 and 19: two dots each, stacked', f'xd:d10:{sk(CR, lambda v: v <= 19)} tc:cr:{dk(13, where(CR, lambda v: v <= 19))}'),
     ('22: four dots · 23: two dots', f'xd:d10:{sk(CR, lambda v: v <= 23)} tc:cr:{dk(13, where(CR, lambda v: v <= 23))}'),
     ('24, 25, 29: one dot each · check: 13 dots', f'xd:d10:{sk(CR, lambda v: True)} tc:cr:{dk(13, range(13))}')],
    'The dot plot (left).', CG + ', 1D Example 10 (p. 29)',
    fig=f'<svg class="zdp zbuild" id="d10" data-v="{json.dumps(sorted(CR))}" data-lo="17" data-hi="30" data-xl="Age (years)" viewBox="0 0 640 262"></svg>', figw='1.2fr',
    ans_do=f'xd:d10:{sk(CR, lambda v: True)} tc:cr:{dk(13, range(13))}'))

# ---- You try 10: Edrolo 1C WE1
PET = [3, 2, 0, 1, 1, 3, 0, 5, 2, 1, 1, 2]
ALLP = f'xd:y10:{sk(PET, lambda v: True)} tc:pt:{dk(12, range(12))}'
S.append(qslide('yt', 10, 'Constructing a dot plot', 'Edrolo 1C WE1',
    'Sophie surveyed 12 of the families living on her street. She asked for the number of pets each of them owned and the results were recorded.' + dlist('pt', PET, 12),
    KI_DOT, [], None, ED + ', 1C Worked example 1. Working by teacher.',
    parts=[('a.', 'Construct a dot plot to display this data.',
            ['Number line 0 to 5, labelled <i>number of pets</i>.',
             ('Dots: 0→2 · 1→4 · 2→3 · 3→2 · 5→1', ALLP)], 'Dot plot (left).', ALLP),
           ('b.', 'What was the modal number of pets owned by families that Sophie surveyed?',
            [('The tallest stack: 4 families own 1 pet.', ALLP + f' xm:y10:{sk(PET, lambda v: v == 1)}')], '<b>1 pet</b>', ALLP + f' xm:y10:{sk(PET, lambda v: v == 1)}')],
    fig=f'<svg class="zdp zbuild" id="y10" data-v="{json.dumps(sorted(PET))}" data-lo="0" data-hi="6" data-xl="number of pets" viewBox="0 0 640 262"></svg>', figw='1.1fr'))

# ---- CAS: dot plot (TI-Nspire only)
S.append(qslide('cas', '', 'Constructing a dot plot (TI-Nspire)', 'Data: Cambridge Example 10',
    'The ages (in years) of the 13 members of a cricket team are: 22 &nbsp;19 &nbsp;18 &nbsp;19 &nbsp;23 &nbsp;25 &nbsp;22 &nbsp;29 &nbsp;18 &nbsp;22 &nbsp;23 &nbsp;24 &nbsp;22<br>Enter the ages into a list named <b>age</b> and display them as a dot plot.',
    'Check the number of dots equals $n$. ClassPad has no dot plot: draw it by hand.',
    ['Enter the 13 ages in a list named <i>age</i>.', 'Data &amp; Statistics: add <i>age</i> on the x-axis.', ('A dot plot appears: 13 dots', f'xd:cd:{sk(CR, lambda v: True)}')],
    'Same dot plot as Example 10: 22 has four dots, the most of any age.', 'Data: ' + CG + ', 1D Example 10 (p. 29). CAS steps: planner CAS guide (TI-Nspire only).',
    fig=casbox('dotplot') + f'<svg class="zdp zbuild" id="cd" data-v="{json.dumps(sorted(CR))}" data-lo="17" data-hi="30" data-xl="age" viewBox="0 0 640 262"></svg>', figw='1.15fr', cls='s2cas',
    ans_do=f'xd:cd:{sk(CR, lambda v: True)}'))

# ---- Example 11 (Cambridge): unordered, then ordered
UR = [26, 3, 12, 20, 36, 1, 25, 26, 13, 9, 26, 27, 15, 21, 7, 8, 22, 3, 37, 17, 55, 30, 1]
urow, ump = stemmap(UR, range(6), False); orow, omp = stemmap(UR, range(6), True)
uk = lambda ix: J2(sorted(ump[i] for i in ix))
S.append(qslide('ex', 11, 'Constructing a stem plot', 'Cambridge · Example 11',
    'University participation rates (%) in 23 countries are given below.' + dlist('ur', UR, 12) + 'Display the data in the form of a stem plot.',
    KI_STEM,
    ['Values run from 1 to 55: stems 0 to 5 (units, tens, …, fifties).',
     ('First values, in the order given: 26 → stem 2, leaf 6 · 3 → stem 0, leaf 3 …', f'xl:u11:{uk(range(8))} tc:ur:{dk(12, range(8))}'),
     ('Every value gets a leaf on its stem; stem 4 stays empty.', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))}'),
     ('Order the leaves on each stem, smallest first.', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22'),
     ('Write the key and variable: 1 | 2 = 12, <i>rate</i> (%)', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22 sk:o11')],
    'The ordered stem plot (right), key 1 | 2 = 12%.', CG + ', 1D Example 11 (p. 30)',
    fig='<div class="s2two"><div><div class="zsc">unordered</div>' + stem('u11', urow, '&nbsp;').replace('class="zstem"', 'class="zstem zbuild" data-max="30"').replace('<div class="zkey">&nbsp;</div>', '<div class="zkey" style="visibility:hidden">&nbsp;</div>')
        + '</div><div><div class="zsc">ordered</div>' + stem('o11', orow, 'Key: 1 | 2 = 12 &nbsp; <i>rate</i> (%)', build=True).replace('class="zstem"', 'class="zstem zbuild" data-max="30"') + '</div></div>',
    figw='1.15fr', ans_do=f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22 sk:o11'))

# ---- You try 11: Edrolo 1C WE2
EX = [55, 68, 76, 90, 83, 89, 75, 66, 59, 84, 48, 62, 58, 95, 80, 77, 61, 92, 99, 63, 84, 65, 70, 81, 96]
erow, emp = stemmap(EX, range(4, 10), True)
EALL = f'xl:y11:0-24 tc:ex:{dk(13, range(25))}'
above = J2(sorted(emp[i] for i in where(EX, lambda v: v > 70)))
S.append(qslide('yt', 11, 'Constructing a stem plot', 'Edrolo 1C WE2',
    'Ms Smyth’s maths class of 25 students sat their end-of-year exam. Their results (%) were recorded.' + dlist('ex', EX, 13),
    KI_STEM, [], None, ED + ', 1C Worked example 2. Working by teacher.',
    parts=[('a.', 'Construct a stem plot to display this data.',
            ['Values from 48 to 99: stems 4 to 9 (tens), leaves = ones.', ('Place each leaf, then order each stem.', EALL), ('Write the key: 4 | 8 = 48%', EALL + ' sk:y11')],
            'Ordered stem plot (left).', EALL + ' sk:y11'),
           ('b.', 'How many students scored above 70% on the exam?',
            [('Leaves 5, 6, 7 on stem 7, and stems 8 and 9: 3 + 6 + 5', EALL + f' sk:y11 lx:y11:{above}')],
            '<b>14 students</b>', EALL + f' sk:y11 lx:y11:{above}')],
    fig=stem('y11', erow, 'Key: 4 | 8 = 48%', build=True).replace('class="zstem"', 'class="zstem zbuild"'), figw='.95fr', cls='tight'))

# ---- NL: logs are powers of ten
S.append(nl_slide('Logs are just powers of 10',
    r'The log of a number is the power of 10 that makes it: $\log_{10} 1000 = 3$, since $10^3 = 1000$. <span class="hint">Click to fill the rows.</span>',
    '<table class="zft s2lt" id="lgt"><tr><th>number</th>' + ''.join(f'<td>{x}</td>' for x in ['0.01', '0.1', '1', '10', '100', '1000', '1 000 000']) + '</tr>'
    '<tr><th>power of 10</th>' + ''.join(f'<td class="s2h" data-k="1{c}">$10^{{{p}}}$</td>' for c, p in enumerate(['-2', '-1', '0', '1', '2', '3', '6'])) + '</tr>'
    '<tr><th>log</th>' + ''.join(f'<td class="s2h" data-k="2{c}"><b>{p}</b></td>' for c, p in enumerate(['−2', '−1', '0', '1', '2', '3', '6'])) + '</tr></table>'
    + st('Write each number as a power of 10.', do='xs:lgt:1')
    + st('The log is the power.', do='xs:lgt:1 xs:lgt:2')
    + st('Number above 1 → positive log · between 0 and 1 → negative log · 0 → no log. Each step of 1 on a log scale multiplies by 10.', True, do='xs:lgt:1 xs:lgt:2'),
    CG + ', 1E pp. 34–35'))

# ---- NL interactive: animal weights on a log scale (Cambridge 1E Example 13 context)
S.append(f'<section class="slide z nl logx">{bar("New learning", "Why a log scale? Animal body weights")}'
    '<div class="ctx">Animals range from a 0.02 kg mouse to a 2500 kg elephant. On an ordinary scale, almost every animal is squashed against 0. '
    'On a <b>log scale</b>, each step of 1 is ten times heavier. Drag the slider (or tap an animal) to move the white dot.</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>The same weight on two scales</h2>'
    '<svg class="zlg ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>log −2</span><input type="range" min="-200" max="400" step="1" value="52"><span>log 4</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-w="0.02">Mouse (0.02 kg)</button><button data-w="3.3">Cat (3.3 kg)</button><button data-w="70">Person (70 kg)</button><button data-w="2512">Elephant (log 3.4)</button><button data-w="10000">log 4</button></div></div>'
    '<div class="col"><h2>Live</h2><div class="zlgo"></div>'
    r'<div class="zrule">$\log_{10}(\text{weight}) = b \iff \text{weight} = 10^{b}$. A positively skewed set of weights often looks roughly symmetric on a log scale.</div></div></div>'
    f'{foot(CG + ", 1E pp. 34–38 (cat 3.3 kg, elephant log 3.4: Example 13). Mouse and person weights made up by the teacher.")}</section>')

# ---- Example 12 (Cambridge)
S.append(qslide('ex', 12, 'Using a CAS calculator to find logs', 'Cambridge · Example 12',
    'Answer each part.', KI_LOG, [], None, CG + ', 1E Example 12 (pp. 36–37)',
    parts=[('a', 'Find the log of 45, correct to two significant figures.', [r'CAS: $\log(45) = 1.653\ldots$', '2 significant figures: count from the first non-zero digit.'],
            r'$\log 45 = \boldsymbol{1.7}$'),
           ('b', 'Find the number with log equal to 2.7125, correct to the nearest whole number.', [r'Undo the log: the number is $10^{2.7125}$', r'CAS: $10^{2.7125} = 515.82\ldots$'],
            r'$\boldsymbol{516}$')]))

# ---- CAS: logs
S.append(qslide('cas', '', 'Finding a log, and undoing it', 'Cambridge · Example 12',
    'a Find the log of 45, correct to two significant figures.<br>b Find the number with log equal to 2.7125, correct to the nearest whole number.',
    'log( ) gives the power of 10. 10^ undoes it.',
    [r'Type log(45): $1.65321\ldots$', r'Type 10^2.7125: $515.822\ldots$', 'Round as each part asks.'],
    'a 1.7 &nbsp;·&nbsp; b 516', CG + ', 1E Example 12 (p. 37). CAS steps: planner CAS guide.',
    fig=casbox('logs'), figw='1fr', cls='s2cas'))

# ---- You try 12: Edrolo 1D WE1
S.append(qslide('yt', 12, 'Using a CAS calculator to find logs', 'Edrolo 1D WE1',
    'Use log<sub>10</sub> for the following calculations.', KI_LOG, [], None, ED + ', 1D Worked example 1. Working by teacher.',
    parts=[('a.', 'Calculate the log of 23, correct to two decimal places.', [r'CAS: $\log_{10}(23) = 1.3617\ldots$'], r'$\boldsymbol{1.36}$'),
           ('b.', 'If the log of a number is 5, what is the number?', [r'$\log_{10}(x) = 5$, so $x = 10^{5}$'], r'$\boldsymbol{100\,000}$')]))

# ---- Example 13 (Cambridge)
AW = [3.7, 7.4, 18.5, 25.9, 25.9, 11.1, 7.4]
H13 = lambda id_: hist(id_, -2, 1, AW, 28, 4, 'log(body weight)', 'Percentage')
S.append(qslide('ex', '13 (a, b)', 'Interpreting a histogram with a log scale', 'Cambridge · Example 13',
    'The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.', KI_LOGH, [], None,
    CG + ', 1E Example 13 a–b (pp. 37–38); histogram redrawn from the CAS 2 data (p. 38)',
    parts=[('a', 'What body weight (in kg) is represented by the number 4 on the log scale?', [r'4 on the log scale stands for $10^{4}$.'], r'$10^{4} = \boldsymbol{10\,000}$ kg'),
           ('b', 'How many of these animals have body weights more than 10 000 kg?', [('10 000 kg is 4 on the log scale. One bar above 4: 7.4% of 27 animals', 'hq:h13:6'), (r'$0.074 \times 27 = 1.998 \approx 2$', 'hq:h13:6')], '<b>Two animals</b>', 'hq:h13:6')],
    fig=H13('h13'), figw='1fr'))
S.append(qslide('ex', '13 (c, d)', 'Interpreting a histogram with a log scale', 'Cambridge · Example 13',
    'The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.', KI_LOG, [], None,
    CG + ', 1E Example 13 c–d (pp. 37–38); histogram redrawn from the CAS 2 data (p. 38)',
    parts=[('c', 'The weight of a cat is 3.3 kg. Use your calculator to determine the log of its weight correct to two significant figures.', [r'CAS: $\log(3.3) = 0.5185\ldots$'], r'$\boldsymbol{0.52}$', 'hq:h13b:2'),
           ('d', 'Determine the weight (in kg) of the animal with a log(<i>body weight</i>) of 3.4 (the elephant). Write your answer correct to the nearest whole number.', [r'Undo the log: $10^{3.4} = 2511.88\ldots$'], r'$\boldsymbol{2512}$ kg', 'hq:h13b:2,5')],
    fig=H13('h13b'), figw='.9fr'))

# ---- You try 13: Edrolo 1D WE3
DV = [2, 3, 3, 5, 6, 1]
S.append(qslide('yt', 13, 'Interpreting a histogram with a log scale', 'Edrolo 1D WE3',
    'A class of twenty students were asked about the <i>distance</i>, in kilometres, from their home to the school. The results were summarised in a histogram using a log<sub>10</sub> scale.',
    KI_LOGH, [], None, ED + ', 1D Worked example 3. Working by teacher.',
    parts=[('a.', 'Jane was away the day of the survey. It is known that she lives 9.5 km away from school. Which interval on the histogram reflects this?',
            [(r'$\log_{10}(9.5) = 0.9777\ldots$: between 0.5 and 1.0', 'hm:yh13:3')], '<b>0.5 – &lt;1.0</b>', 'hm:yh13:3'),
           ('b.', 'How many students live more than 10 km away from school?',
            [(r'$\log_{10}(10) = 1$: add the columns above 1', 'hm:yh13:3 hq:yh13:4,5')], '6 + 1 = <b>7 students</b>', 'hm:yh13:3 hq:yh13:4,5')],
    fig=hist('yh13', -1, 0.5, DV, 8, 2, 'log<tspan baseline-shift="sub" font-size="11">10</tspan>(distance)', 'frequency'), figw='1fr'))

# ---- Exit tasks
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
NV = [k for k, f in neck.items() for _ in range(f)]
S.append(qslide('exit', '1 of 3', 'Show what you know', 'VCAA 2020 Exam 2 Q2a',
    'The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the dot plot below.<br>Write down the modal <i>neck size</i>, in centimetres, for these 250 men.',
    KI_MODE, [('The tallest stack of dots: 48 dots at 38.', f'xm:e1:{sk(NV, lambda v: v == 38)}')],
    'The modal neck size is <b>38 cm</b>.', ED + ', 1C Q16 · VCAA 2020 Exam 2 Data analysis Q2a (% from the examiner report). Dot plot redrawn.',
    fig=bigdot('e1', NV, 30, 45, 'neck size (cm)', H=520), marks=1, vcaa=93, figw='1.2fr', ans_do=f'xm:e1:{sk(NV, lambda v: v == 38)}',
    watch='write the <b>value</b> (38 cm), not the number of men (48). <span class="zsc">(teacher note)</span>'))
TR = [('2', '2 2 4 4'), ('2', '5 7 8 8 8 8 8 8 9 9 9 9'), ('3', '1 2 3 3 4 4 4'), ('3', '5 6 7 7 7 7'), ('4', '1')]
OPTDIST['2 of 3'] = [87, 9, 1, 2, 1]
S.append(qslide('exit', '2 of 3', 'Show what you know', 'VCAA 2016 Exam 1 Q3',
    'The stem plot below displays 30 temperatures recorded at a weather station.<br>The modal temperature is',
    KI_MODE, [('2 | 8 has six leaves: more than any other value.', 'lx:e2:6,7,8,9,10,11'), ('Read the key: 2 | 8 = 2.8 °C', 'lx:e2:6,7,8,9,10,11')],
    '2.8 °C', ED + ', 1C Q18 · VCAA 2016 Exam 1 Data analysis Q3 (% from the examiner report)',
    fig=stem('e2', TR, 'key: 2 | 2 = 2.2 °C &nbsp; <i>temperature</i>').replace('class="zstem"', 'class="zstem zsm"'), marks=1, vcaa=87, figw='1.1fr',
    opts=[('A', '2.8 °C'), ('B', '2.9 °C'), ('C', '3.7 °C'), ('D', '8.0 °C'), ('E', '9.0 °C')], key='A'))
PV = [0, 0, 1, 0, 7, 5, 21, 13, 1, 0]
OPTDIST['3 of 3'] = [7, 6, 7, 71, 9]
S.append(qslide('exit', '3 of 3', 'Show what you know', 'VCAA 2019 Exam 1 Q3',
    'The histogram below shows the population size for these 48 countries plotted on a log<sub>10</sub> scale.<br>Based on this histogram, the number of countries with a population size that is less than 100 000 people is',
    KI_LOGH, [r'$100\,000 = 10^{5}$: that is 5 on the log scale.', ('Columns below 5: 1 + 7', 'hq:e3:2,4')],
    '8', ED + ', 1D Q13 · VCAA 2019 Exam 1 Data analysis Q3 (% from the examiner report). Histogram redrawn; data: Worldometers.',
    fig=hist('e3', 0, 1, PV, 25, 5, 'log<tspan baseline-shift="sub" font-size="11">10</tspan> (population size)', 'frequency'), marks=1, vcaa=71, figw='1.1fr',
    opts=[('A', '1'), ('B', '5'), ('C', '7'), ('D', '8'), ('E', '48')], key='D'))

# ---- check-in + coursework
checkin(SC, "Success criteria: one per worked example")
coursework('1C–1E', 'Coursework · Exercises 1C, 1D, 1E', [('Cambridge Exercise 1C', 'Q1–12'), ('Cambridge Exercise 1D', 'Q1–11'), ('Cambridge Exercise 1E', 'Q1–6'), ('Practice booklet', '1C, 1D, 1E sections')],
           'Exercise 1C: Displaying and describing numerical data', CG + ", Exercises 1C, 1D, 1E")



# ---- lesson-only CSS / JS (everything shared lives in lib/)
LESSON_CSS = r'''
.zstem.zsm table{font-size:22px!important}.s2two .zstem td.zlv{min-width:0}.s2two>div{flex:1;min-width:0}#u11,#o11{--zsf:27px!important}#o11 .zkey{white-space:nowrap}.s2two .lv{min-width:14px;margin-right:4px}.zstem.zsm .zkey{font-size:16px}
.s2two{display:flex;gap:14px;align-items:flex-start;justify-content:center}
.s2shp{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;margin:12px 0}
.s2shp .zpc .st{text-align:center;font-size:18px!important;color:#000;white-space:normal}.s2shp svg{width:100%;height:170px}
.zhg.zmini text{display:none}.s2c{font-size:18px;margin-top:4px}
.s2socs{display:flex;flex-direction:column;gap:14px;margin:18px 0;flex:1}
.s2socs .st{font-size:25px!important;border:2px solid #000;padding:12px 16px;white-space:normal;color:#000}
.s2L{display:inline-block;width:42px;height:42px;line-height:42px;text-align:center;background:#000;color:#fff;font-weight:bold;margin-right:12px}
.s2rules{font-size:17px!important;margin-top:12px!important}.s2rules li{margin-bottom:5px!important}
table.s2lt{font-size:26px;margin:22px auto}table.s2lt td.s2h{color:transparent;transition:color .3s}table.s2lt tr.on td.s2h{color:#d00000}
.slide.s2li .zul li{margin-bottom:6px;font-size:17px}.slide.s2li .zseq li{margin-bottom:5px;font-size:18px}
.slide.s2cas .zfig{flex-direction:column;justify-content:flex-start!important;gap:8px}.slide.s2cas .zfig svg{max-height:260px}
.zlgo{font-size:21px;line-height:1.6}
.zmcq svg.zbd{max-height:410px!important}
.slide.z.s2hg .col .st.zs{flex-shrink:0!important;height:auto!important;font-size:20px!important;margin:0 0 4px!important;padding:3px 8px!important;line-height:1.3!important}
.s2hg svg.zhg{width:100%!important;height:auto!important;max-height:none!important}
.s2hg .col{justify-content:flex-start!important;gap:4px!important}
.slide.z.s2hg .col .st.zs.final{margin-top:8px!important}
'''
LESSON_JS = r'''
// S2 was approved with the stem plots fitted BEFORE zfit shrinks question text: fit them first (core refits at 900 ms, same result)
document.fonts.ready.then(()=>setTimeout(zstemfit,500));
window.addEventListener('load',()=>{
 // log-scale interactive: one weight shown on an ordinary scale (0 to 10 000 kg) and on a log scale (-2 to 4)
 document.querySelectorAll('.slide.logx').forEach(sl=>{const sv=sl.querySelector('svg.zlg'),r=sl.querySelector('input'),O=sl.querySelector('.zlgo');
  const A=[['mouse',0.02],['cat',3.3],['person',70],['elephant',2512]];
  const fmt=w=>w>=100?Math.round(w).toLocaleString('en-AU'):(w>=1?w.toFixed(1):w.toPrecision(2));
  const draw=()=>{const b=+r.value/100,w=Math.pow(10,b),pl=v=>40+v/10000*620,pg=v=>40+(v+2)/6*620;
   let s='<text x="20" y="22" font-size="16" font-weight="bold">Ordinary scale (kg)</text><line x1="30" y1="80" x2="670" y2="80" stroke="#000" stroke-width="2"/>';
   for(let v=0;v<=10000;v+=2000)s+=`<line x1="${pl(v)}" y1="74" x2="${pl(v)}" y2="86" stroke="#000"/><text x="${pl(v)}" y="106" font-size="15" text-anchor="middle">${v.toLocaleString('en-AU')}</text>`;
   s+='<text x="20" y="152" font-size="16" font-weight="bold">Log scale: log₁₀(weight)</text><line x1="30" y1="210" x2="670" y2="210" stroke="#000" stroke-width="2"/>';
   for(let v=-2;v<=4;v++)s+=`<line x1="${pg(v)}" y1="204" x2="${pg(v)}" y2="216" stroke="#000"/><text x="${pg(v)}" y="236" font-size="15" text-anchor="middle">${v<0?'−'+(-v):v}</text>`;
   A.forEach(([n,v])=>{s+=`<circle cx="${pl(v)}" cy="64" r="6" fill="#555"/><circle cx="${pg(Math.log10(v))}" cy="194" r="6" fill="#555"/><text x="${pg(Math.log10(v))}" y="180" font-size="13" text-anchor="middle">${n}</text>`});
   s+=`<circle cx="${pl(w)}" cy="58" r="10" fill="#fff" stroke="#d00000" stroke-width="3"/><circle cx="${pg(b)}" cy="188" r="10" fill="#fff" stroke="#d00000" stroke-width="3"/>`;
   sv.innerHTML=s;
   O.innerHTML=`Weight = <b>${fmt(w)} kg</b><br>log₁₀(weight) = <b style="color:#d00000">${b.toFixed(2)}</b><br>Check: 10<sup>${b.toFixed(2)}</sup> = ${fmt(w)}<br><span style="font-size:17px">On the ordinary scale the mouse, cat and person all sit on top of each other at 0. On the log scale they spread out.</span>`};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(x=>x.onclick=e=>{e.stopPropagation();r.value=Math.round(Math.log10(+x.dataset.w)*100);draw()});draw()});
});
'''

build('S2-slides.html', '12MAG S2 · Displaying and describing numerical data · Slides', css=LESSON_CSS, js=LESSON_JS)
