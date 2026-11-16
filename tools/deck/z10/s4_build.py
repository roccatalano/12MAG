r"""12MAG S4 (1G The five-number summary and the boxplot) built in the 10MA slide house style.
Built on the slide library tools/deck/z10/lib (rules: tools/deck/z10/HOWTO.md).
python3 tools/deck/z10/s4_build.py  ->  lessons/S4-slides.html
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.boxplot import *
lesson('1G Boxplots')
# ---------------- slides ----------------
# S4 = 1G The five-number summary and the boxplot. Content from the planner card gm12-u3-s4 and the old deck
# tools/deck/s4/build.py, in git history (questions there are verbatim and cited). Boxplot helper + engine defined here.
CG1 = 'Cambridge General Mathematics Units 1&amp;2'
ED1 = 'Edrolo General Mathematics Units 1&amp;2'

def bigdot(id_, counts, lo, hi, xl, W=640, r=3.4, gap=7):
    """Dot plot for large n (one dot per value, stacked)."""
    mx = max(counts.values()); ay = 30 + mx * gap; px = lambda x: 30 + (x - lo) / (hi - lo) * (W - 60)
    s = f'<line x1="14" y1="{ay}" x2="{W-14}" y2="{ay}" stroke="#000" stroke-width="2"/>'
    for x in range(lo, hi + 1):
        s += f'<line x1="{px(x)}" y1="{ay-5}" x2="{px(x)}" y2="{ay+5}" stroke="#000"/><text x="{px(x)}" y="{ay+24}" font-size="17" text-anchor="middle">{x}</text>'
    first, last = min(counts), max(counts)
    for x, c in counts.items():
        for j in range(c):
            e = ' data-e="1"' if (x in (first, last)) else ''
            s += f'<circle cx="{px(x)}" cy="{ay-6-j*gap}" r="{r}" fill="#333"{e}/>'
    s += f'<text x="{W/2}" y="{ay+48}" font-size="17" text-anchor="middle">{xl}</text>'
    return f'<svg class="zbd" id="{id_}" viewBox="0 0 {W} {ay+56}">{s}</svg>'

KI_5 = r'Five-number summary: min, $Q_1$, $M$, $Q_3$, max<div class="kn">the box runs $Q_1$ to $Q_3$; line at $M$; whiskers to the ends</div>'
KI_F = r'$\text{LF} = Q_1 - 1.5 \times \text{IQR}$<br>$\text{UF} = Q_3 + 1.5 \times \text{IQR}$<div class="kn">below LF or above UF → outlier (a dot)</div>'
KI_P = r'Each of the four sections holds about <b>25%</b> of the data.<div class="kn">below $Q_1$: 25% · below $M$: 50% · below $Q_3$: 75%</div>'
KI_S = r'SOCS: <b>S</b>hape · <b>O</b>utliers · <b>C</b>entre (median) · <b>S</b>pread (IQR, range)'
SOCS = lambda s, o, c, sp: (f'The distribution is {s}.<br>There {o}.<br>The distribution is centred at {c}, the median.<br>{sp}')

title_slide('The five-number summary and the boxplot', ['1G The five-number summary and the boxplot (pp. 61–69)'])
LI = ['To be able to construct the boxplot for displaying the distribution of a numerical data.', 'To be able to define and identify outliers.',
      'To be able to construct both simple boxplots and boxplots with outliers.', 'To be able to determine the features of a distribution from a boxplot.',
      'To be able to use a CAS calculator to construct a boxplot.']
SC = ['I can construct a boxplot from a five-number summary.', 'I can construct a boxplot with outliers from data using the CAS calculator.',
      'I can read values from a boxplot.', 'I can estimate percentages from a boxplot.', 'I can use boxplots to describe a distribution without outliers.',
      'I can use boxplots to describe a distribution with outliers.', 'I can use boxplots to answer statistical questions.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'The boxplot · Example 22', 'Outliers and the fences', 'Boxplots on CAS',
       'Reading a boxplot · Examples 23–24', 'Shape from a boxplot · Examples 25–27', 'Exit tasks', 'Check-in and coursework']
overview('1G', LI, SC, SEQ, CG + ", 1G Learning intentions (p. 61); success criteria: one per worked example", cols='1.05fr 1.05fr .9fr')

# ---- APK 1 + 2: party ages (Cambridge U1&2 2H #14, #15)
PARTY = [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')]
APKQ = 'The ages of a group of people at a party:<br>19 21 22 56 34 19 27 28 34 17 66 37 20 20 21 45 26 19 23 29<br>'
S.append(qslide('apk', '1 of 3', 'Year 11 skills: five-number summary and boxplot', 'Cambridge U1&amp;2 · 2H #14',
    APKQ + 'Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).',
    KI_5, [('$n = 20$: min $= 17$, max $= 66$', 'lx:pa:0,19'),
           (r'Median position $= \dfrac{20 + 1}{2} = $ 10.5th. Count to the 10th and 11th: $M = \dfrac{23 + 26}{2} = 24.5$', 'ln:pa:0:11 lm:pa:9,10'),
           (r'Ten in each half: $Q_1 = \dfrac{20 + 20}{2} = 20$, $Q_3 = \dfrac{34 + 34}{2} = 34$', 'lm:pa:9,10 lq:pa:4,5,14,15'),
           ('Scale 15 to 70. Box from 20 to 34, line at 24.5', 'lm:pa:9,10 lq:pa:4,5,14,15 bx:pab:axis,box,med'),
           ('Whiskers out to 17 and 66', 'lm:pa:9,10 lq:pa:4,5,14,15 bx:pab:wl,wu')],
    '<b>17, 20, 24.5, 34, 66</b>; boxplot drawn', CG1 + ', Chapter 2 skills checklist 2H #14 (data in a stem plot by the teacher). Working by teacher.',
    fig=stem('pa', PARTY, 'Key: 1 | 7 = 17') + bplot('pab', 15, 70, 5, 10, (17, 20, 24.5, 34, 66), xl='age (years)', build=True), figw='1.45fr', cls='tight apkb apks'))
S.append(qslide('apk', '2 of 3', 'Year 11 skills: outliers from the fences', 'Cambridge U1&amp;2 · 2H #15',
    APKQ + 'Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).',
    KI_F, [(r'$\text{IQR} = 34 - 20 = 14$', 'lq:pb:4,5,14,15'),
           (r'$\text{LF} = 20 - 1.5 \times 14 = -1$', 'lq:pb:4,5,14,15 bx:pbb:fl'),
           (r'$\text{UF} = 34 + 1.5 \times 14 = 55$', 'lq:pb:4,5,14,15 bx:pbb:fl,fu'),
           ('$56 > 55$ and $66 > 55$: outliers. Nothing is below $-1$.', 'lq:pb:4,5,14,15 lx:pb:18,19 bx:pbb:fl,fu,out'),
           ('Upper whisker stops at 45, the largest value that is not an outlier', 'lq:pb:4,5,14,15 lx:pb:18,19 bx:pbb:fl,fu,out,wu')],
    'LF $= -1$, UF $= 55$. The outliers are <b>56 and 66</b>.', CG1 + ', Chapter 2 skills checklist 2H #15. Working by teacher.',
    fig=stem('pb', PARTY, 'Key: 1 | 7 = 17') + bplot('pbb', -5, 70, 5, 10, (17, 20, 24.5, 34, 45), out=(56, 66), xl='age (years)', hide=('out', 'wu'),
        fences=(('fl', -1, 'LF = −1'), ('fu', 55, 'UF = 55'))), figw='1.75fr', cls='tight apkb apks'))
OPTDIST['3 of 3'] = [None] * 5
S.append(qslide('apk', '3 of 3', 'A real VCAA question you can already do', 'VCAA 2017 Exam 1 Q2 (adapted)',
    'The boxplot shows the distribution of the <i>reaction time</i> (milliseconds), of 256 firefighters.'
    + bplot('fir', 0, 260, 10, 50, (122, 130, 140, 152, 179), out=(70, 90, 255), xl='reaction time (milliseconds)', caps=True,
            marks=(('m1', 70, 'min', '#d00000'), ('m2', 255, 'max', '#d00000'))) +
    'The five-number summary for the <i>reaction time</i> of these 256 firefighters is closest to',
    r'Outliers are real data values.<div class="kn">min and max are the outer dots, not the whisker ends</div>',
    [('The dots are data: smallest value $= 70$, largest $= 255$', 'bx:fir:m1,m2 bxo:fir'), ('Box: $Q_1 = 130$, $M = 140$, $Q_3 = 152$', 'bx:fir:m1,m2 bxo:fir')],
    '70, 130, 140, 152, 255',
    ED1 + ', 1F Q16 · adapted by Edrolo from VCAA 2017 Exam 1 Data analysis Q2; 58% correct (examiner report, original question). Boxplot redrawn.',
    marks=1, vcaa=58, opts=[('A', '70, 130, 140, 152, 179'), ('B', '70, 130, 140, 152, 255'), ('C', '122, 130, 140, 152, 179'), ('D', '122, 130, 140, 152, 245'), ('E', '122, 130, 140, 152, 265')],
    key='B', figw='1.15fr').replace('zmc"', 'zmc zmc1"').replace('How did students answer? Bars show the % choosing each option.', '58% chose B (examiner report). The report’s % for each other option is not in the repo.')
    .replace('pct stat:58', 'stat:58'))

# ---- Key ideas
KD = [('Five-number summary', 'minimum, $Q_1$, median, $Q_3$, maximum'), ('Boxplot', 'a picture of the five-number summary; the box holds the middle 50%'),
      ('Whiskers', 'run from the box to the smallest and largest values that are not outliers'), ('Outlier', 'a value below the lower fence or above the upper fence, drawn as a dot')]
KF = [('Median position', r'$\dfrac{n + 1}{2}$th value'), ('Interquartile range', r'$\text{IQR} = Q_3 - Q_1$'), ('Range', r'$\text{range} = \text{max} - \text{min}$'),
      ('Lower fence', r'$\text{LF} = Q_1 - 1.5 \times \text{IQR}$ &nbsp;<span class="zn">$x < \text{LF}$ → outlier</span>'),
      ('Upper fence', r'$\text{UF} = Q_3 + 1.5 \times \text{IQR}$ &nbsp;<span class="zn">$x > \text{UF}$ → outlier</span>')]
S.append(f'<section class="slide z kif">{bar("1G", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1F pp. 44–47 and 1G pp. 61–64. Fences: VCAA formula sheet.")}</section>')

# ---- NL: the boxplot
S.append(nl_slide('Five numbers, one picture',
    'A <b>boxplot</b> draws the five-number summary. <span class="hint">Click to build it.</span>',
    '<div class="zbig">' + bplot('nl1', 0, 100, 5, 10, (12, 35, 50, 62, 95), build=True, W=900,
        marks=(('k0', 12, 'min', '#8a4d00'), ('k1', 35, 'Q₁', '#1f5fbf'), ('k2', 50, 'M', '#d00000'), ('k3', 62, 'Q₃', '#1f5fbf'), ('k4', 95, 'max', '#8a4d00')),
        bands=(('p1', 12, 35, '25%'), ('p2', 35, 50, '25%'), ('p3', 50, 62, '25%'), ('p4', 62, 95, '25%'))) + '</div>'
    + '<div class="zrow3">' + st('<b>1</b> Scaled number line; mark the five numbers.', do='bx:nl1:axis,k0,k1,k2,k3,k4')
    + st('<b>2</b> Box from $Q_1$ to $Q_3$, line at the median.', do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med')
    + st('<b>3</b> Whiskers out to the min and the max.', do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med,wl,wu')
    + st('<b>Each section holds about 25% of the data</b>, however long it looks.', True, do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med,wl,wu,p1,p2,p3,p4') + '</div>',
    CG + ', 1G pp. 61–62. Boxplot: teacher illustration.'))

# ---- Example 22 / You try 22
life = [('5', '2'), ('5', '5 6'), ('6', '4'), ('6', '6 6 7 9'), ('7', '1 2 2 3 3 4 4 4 4'), ('7', '5 5 6 6 7 7')]
S.append(qslide('ex', 22, 'Constructing a boxplot from a five-number summary', 'Cambridge · Example 22',
    'The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:'
    + '<table class="ztab zinq zh5"><tr><th>minimum</th><th>first quartile ($Q_1$)</th><th>median ($M$)</th><th>third quartile ($Q_3$)</th><th>maximum</th></tr><tr><td>52</td><td>66</td><td>73</td><td>75</td><td>77</td></tr></table>'
    + 'Use the five-number summary to construct a boxplot.', KI_5,
    [('The five numbers on the stem plot: 52, 66, 73, 75, 77', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11'),
     ('Number line 50 to 80, labelled and scaled', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis'),
     ('Box from $Q_1 = 66$ to $Q_3 = 75$; line at $M = 73$', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis,box,med'),
     ('Whiskers out to 52 and 77', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis,box,med,wl,wu')],
    'Boxplot drawn (52, 66, 73, 75, 77)', CG + ', 1G Example 22',
    fig=stem('s22', life, 'Key: 5 | 2 = 52 years') + bplot('b22', 50, 80, 1, 5, (52, 66, 73, 75, 77), xl='Life expectancy (years)', build=True), figw='1.75fr', cls='tight apkb apks'))
w4 = [('0', '1 2 3 5 5 9'), ('1', '0 0 1 5 8 9'), ('2', '1 2 3 3 5'), ('3', '3 7 9')]
S.append(qslide('yt', 22, 'Constructing a boxplot from a five-number summary', 'Edrolo 1E WE4',
    'The five-number summary for the following stem plot is: 1, 7, 16.5, 23, 39<br>Construct a boxplot using the data.', KI_5,
    [('Number line 0 to 40', 'bx:b4:axis'), ('Box from 7 to 23; line at 16.5', 'bx:b4:axis,box,med'),
     (r'Check for outliers: $\text{IQR} = 16$, fences $-17$ and $47$. 1 and 39 are inside.', 'bx:b4:axis,box,med'),
     ('Whiskers out to 1 and 39', 'bx:b4:axis,box,med,wl,wu')],
    'Boxplot drawn; no outliers', ED + ', 1E Worked example 4. Working by teacher.',
    fig=stem('y22', w4, 'Key: 1 | 2 = 12') + bplot('b4', 0, 40, 1, 5, (1, 7, 16.5, 23, 39), build=True), figw='1fr', cls='tight apkb'))

# ---- NL: outliers and fences (Cambridge CAS 4 data)
S.append(nl_slide('Outliers: the 1.5 × IQR fences',
    'An <b>outlier</b> is more than 1.5 IQRs below $Q_1$ or above $Q_3$. It is drawn as a dot; the whisker stops at the last value inside the fence. <span class="hint">19 marks: $Q_1 = 23$, $M = 30$, $Q_3 = 35$.</span>',
    '<div class="zbig">' + bplot('nl2', 0, 55, 1, 5, (21, 23, 30, 35, 48), out=(3,), xl='marks', W=900, hide=('wl', 'wu', 'out'),
        bands=(('iq', 23, 35, 'IQR = 12'),), fences=(('fl', 5, 'LF = 5'), ('fu', 53, 'UF = 53'))) + '</div>'
    + '<div class="zrow3">' + st(r'<b>1</b> $\text{IQR} = 35 - 23 = 12$', do='bx:nl2:iq')
    + st(r'<b>2</b> $\text{LF} = 23 - 18 = 5$, $\text{UF} = 35 + 18 = 53$', do='bx:nl2:iq,fl,fu')
    + st('<b>3</b> $3 < 5$: <b>3 is an outlier</b> (a dot). Nothing is above 53.', do='bx:nl2:iq,fl,fu,out')
    + st('Whiskers: down to 21 (smallest non-outlier), up to 48 (the max).', True, do='bx:nl2:iq,fl,fu,out,wl,wu') + '</div>',
    CG + ', 1G pp. 63–64. Data: CAS 4 (p. 64).'))

# ---- interactive: party ages fence slider
S.append(f'<section class="slide z nl zfx">{bar("New learning", "When is an age an outlier?")}'
    '<div class="ctx">Back to the party. The oldest guest was 66. Drag the slider (or tap a button) to change that one guest’s age. The quartiles, fences and boxplot update. When does that guest become an <b>outlier</b>?</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>Party ages (years)</h2>'
    '<svg class="zfxs ix" viewBox="0 0 700 230" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>15</span><input type="range" min="15" max="90" step="1" value="66"><span>90</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-v="45">45</button><button data-v="55">55</button><button data-v="56">56</button><button data-v="66">66</button><button data-v="90">90</button></div></div>'
    '<div class="col"><h2>Live summary</h2><div class="zfxo"></div>'
    '<div class="zrule">$x$ is an outlier if $x < Q_1 - 1.5 \\times \\text{IQR}$ or $x > Q_3 + 1.5 \\times \\text{IQR}$. Exactly on a fence is <b>not</b> an outlier.</div></div></div>'
    f'{foot("Data: " + CG1 + ", Chapter 2 skills checklist 2H #14–15 (party ages). Interactive by teacher.")}</section>')

# ---- CAS
def castabs(sid):
    import json as _j
    sk = [x for x in _j.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if isinstance(x, dict) and x.get('id') == sid][0]
    return ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in sk["ti"])}</ol></div>'
            '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in sk["classpad"])}</ol></div></div>')
S.append(qslide('cas', '', 'Boxplot with outliers on CAS', 'Cambridge · 1G CAS 4',
    'Display the following set of 19 marks in the form of a boxplot with outliers.<br>28 &nbsp;21 &nbsp;21 &nbsp;3 &nbsp;22 &nbsp;31 &nbsp;35 &nbsp;26 &nbsp;27 &nbsp;33 &nbsp;43 &nbsp;31 &nbsp;30 &nbsp;34 &nbsp;48 &nbsp;36 &nbsp;35 &nbsp;23 &nbsp;24',
    r'CAS draws outliers as dots automatically.<div class="kn">Trace gives min, $Q_1$, $M$, $Q_3$, max</div>',
    ['Enter the 19 marks in one list.', 'Draw the box plot (outliers on).', 'Trace: min $= 3$ (a dot), $Q_1 = 23$, $M = 30$, $Q_3 = 35$, max $= 48$',
     ('3 shows as a dot; the whisker starts at 21', 'bx:cb:out')],
    'The boxplot has one outlier, <b>3</b>', CG + ', 1G pp. 64–66 (CAS 4). CAS steps: planner CAS guide.',
    fig=castabs('boxplot') + bplot('cb', 0, 50, 1, 10, (21, 23, 30, 35, 48), out=(3,), xl='marks', W=560), figw='1.05fr', cls='tight apkb'))
S.append(qslide('yt', '', 'Constructing a boxplot with outliers using CAS', 'Edrolo 1E WE5',
    'Construct a boxplot for the following data set.<br>2 &nbsp;4 &nbsp;4 &nbsp;5 &nbsp;5 &nbsp;5 &nbsp;7 &nbsp;6 &nbsp;5 &nbsp;4 &nbsp;6 &nbsp;5 &nbsp;6 &nbsp;7 &nbsp;8 &nbsp;12 &nbsp;3 &nbsp;5', KI_F,
    ['CAS one-variable statistics: 2, 4, 5, 6, 12', r'$\text{IQR} = 6 - 4 = 2$', r'$\text{LF} = 4 - 3 = 1$, $\text{UF} = 6 + 3 = 9$',
     ('$12 > 9$: outlier. $2 > 1$: not an outlier.', 'bx:b5:axis,box,med,fl,fu,out'), ('Whiskers to 2 and 8 (largest non-outlier)', 'bx:b5:axis,box,med,fl,fu,out,wl,wu')],
    'Boxplot drawn, with <b>12 as an outlier</b>', ED + ', 1E Worked example 5. Working by teacher.',
    fig=bplot('b5', 0, 13, 1, 1, (2, 4, 5, 6, 8), out=(12,), xl='value', build=True, fences=(('fl', 1, 'LF = 1'), ('fu', 9, 'UF = 9'))), figw='1fr'))
S.append(f'<section class="slide z cas">{bar("CAS", "Parallel boxplots on CAS")}<p class="lead zlead">Two or more groups on the same scale (used again in 2C). Steps from the planner CAS guide.</p>'
         f'<div class="zb" style="grid-template-columns:1fr;margin-top:6px"><div class="zfig">{castabs("parallel-boxplots").replace("zcas2", "zcas2 zh")}</div></div>'
         f'{foot("CAS steps: planner CAS guide (parallel-boxplots) · ClassPad Help 405")}</section>')

# ---- Example 23 / You try 23
S.append(qslide('ex', 23, 'Reading values from a boxplot', 'Cambridge · Example 23',
    'For the boxplot shown, write down the values of:', r'Fences: $Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$', [], None, CG + ', 1G Example 23',
    parts=[('a', 'the median', [], '$M = 36$', 'bx:b23:mm'),
           ('b', 'the quartiles $Q_1$ and $Q_3$', [], '$Q_1 = 30$, $Q_3 = 44$', 'bx:b23:mm,mq,mq3'),
           ('c', 'the interquartile range (IQR)', [], r'$\text{IQR} = 44 - 30 = 14$', 'bx:b23:mm,mq,mq3'),
           ('d', 'the minimum and maximum values', [], 'min $= 4$, max $= 92$', 'bx:b23:mm,mq,mq3'),
           ('e', 'the values of any possible outliers', [], '4, 70, 84 and 92', 'bx:b23:mm,mq,mq3 bxo:b23'),
           ('f', 'the smallest value in the upper end of the data set that will be classified as an outlier', [], r'$\text{UF} = 44 + 1.5 \times 14 = 65$: values above 65', 'bx:b23:mm,mq,mq3,fu bxo:b23'),
           ('g', 'the largest value in the lower end of the data set that will be classified as an outlier.', [], r'$\text{LF} = 30 - 1.5 \times 14 = 9$: values below 9', 'bx:b23:mm,mq,mq3,fu,fl bxo:b23')],
    fig=bplot('b23', 0, 100, 2, 10, (10, 30, 36, 44, 60), out=(4, 70, 84, 92), W=900,
        marks=(('mm', 36, 'M', '#d00000', 1), ('mq', 30, 'Q₁', '#1f5fbf'), ('mq3', 44, 'Q₃', '#1f5fbf')),
        fences=(('fl', 9, 'LF 9'), ('fu', 65, 'UF 65'))), stack=True, cls='tight p7'))
S.append(qslide('yt', 23, 'Reading values from a boxplot', 'Edrolo 1E WE6',
    'The <i>number of runs scored</i> by the leading batsman at a local cricket club is represented by the following boxplot. It is known that data was collected from 20 separate innings.',
    KI_P, [], None, ED + ', 1E Worked example 6. Working by teacher.',
    parts=[('a.', 'Determine the five-number summary for the data and identify any outliers.', [], '30, 50, 70, 80, 90; no outliers', None),
           ('b.', 'Between which two values does the middle 50% of data lie?', [], '50 and 80 runs', 'bx1:b6:h1'),
           ('c.', 'In approximately what percentage of innings did they score more than 80 runs?', [], '25%', 'bx1:b6:h2'),
           ('d.', 'In approximately how many innings did they score at least 50 runs, but fall short of 100?', [], r'75% of 20 $= 15$ innings', 'bx1:b6:h3')],
    fig=bplot('b6', 0, 100, 5, 10, (30, 50, 70, 80, 90), caps=True, xl='number of runs scored', W=900,
        bands=(('h1', 50, 80, 'middle 50%'), ('h2', 80, 90, '25%'), ('h3', 50, 90, '75%'))), stack=True, cls='tight'))

# ---- Example 24
S.append(qslide('ex', 24, 'Estimating percentages from a boxplot', 'Cambridge · Example 24',
    'For the boxplot shown, estimate the percentage of values:', KI_P, [], None,
    CG + ', 1G Example 24. Boxplot redrawn; the outlier dots are placed by eye from the textbook figure. No matching Edrolo worked example, so no You try.',
    parts=[('a', 'less than 54', [], '54 is $Q_1$: <b>25%</b>', 'bx1:b24:ba'), ('b', 'less than 55', [], '55 is $M$: <b>50%</b>', 'bx1:b24:bb'),
           ('c', 'less than 59', [], '59 is $Q_3$: <b>75%</b>', 'bx1:b24:bc'), ('d', 'greater than 59', [], '100% − 75% = <b>25%</b>', 'bx1:b24:bd'),
           ('e', 'between 54 and 59', [], '75% − 25% = <b>50%</b>', 'bx1:b24:be'), ('f', 'between 54 and 86.', [], '100% − 25% = <b>75%</b>', 'bx1:b24:bf')],
    fig=bplot('b24', 45, 85, 1, 5, (50, 54, 55, 59, 65), out=(70, 81), W=900,
        bands=(('ba', 50, 54, '25%'), ('bb', 50, 55, '50%'), ('bc', 50, 59, '75%'), ('bd', 59, 81, '25%'), ('be', 54, 59, '50%'), ('bf', 54, 81, '75%'))), stack=True, cls='tight'))

# ---- NL: shape
def mini(id_, f5, out=()):
    return bplot(id_, 0, 20, 1, 100, f5, out=out, W=420, T=4)
S.append(nl_slide('Reading shape from a boxplot',
    'Where does the median sit in the box? Which whisker is longer? The long side is the <b>tail</b>. <span class="hint">Click for each shape.</span>',
    '<div class="zsh4">' + st('<h3>Symmetric</h3>' + mini('h1', (2, 7, 10, 13, 18)) + 'Median near the middle; whiskers about equal.')
    + st('<h3>Positively skewed</h3>' + mini('h2', (1, 3, 4.5, 8, 19)) + 'Median to the <b>left</b> of the box; long <b>right</b> whisker.')
    + st('<h3>Negatively skewed</h3>' + mini('h3', (1, 12, 15.5, 17, 19)) + 'Median to the <b>right</b>; long <b>left</b> whisker.')
    + st('<h3>With outliers</h3>' + mini('h4', (8, 10, 11, 12, 14), out=(2, 19)) + 'Dots separated from the whiskers.') + '</div>'
    + st('<b>Describe with SOCS, like a sock:</b> Shape · Outliers · Centre (the median) · Spread (IQR and range).', True, cls='zctr'),
    CG + ', 1G pp. 68–69. Sketches: teacher illustration.'))

# ---- Example 25 / You try 25 / Examples 26, 27
S.append(qslide('ex', 25, 'Using a boxplot to describe a distribution without outliers', 'Cambridge · Example 25',
    'Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.', KI_S,
    [('<b>S</b> Median left of centre, long right whisker', 'bx:b25:mm'), ('<b>O</b> No dots', 'bx:b25:mm'),
     ('<b>C</b> $M = 10$', 'bx:b25:mm'), (r'<b>S</b> $\text{IQR} = 21 - 5 = 16$, range $= 45 - 0 = 45$', 'bx:b25:mm,q1,q3,mx')],
    SOCS('positively skewed', 'are no outliers', '10', 'The IQR is 16 and the range is 45.'),
    CG + ', 1G Example 25 (solution set out in SOCS order)',
    fig=bplot('b25', 0, 50, 1, 5, (0, 5, 10, 21, 45), W=640, col='#fde7a6',
        marks=(('mm', 10, 'M = 10', '#d00000', 1), ('q1', 5, 'Q₁ = 5', '#1f5fbf'), ('q3', 21, 'Q₃ = 21', '#1f5fbf'), ('mx', 45, 'max = 45', '#8a4d00'))), figw='1fr'))
S.append(qslide('yt', 25, 'Using a boxplot to describe a distribution without outliers', 'Edrolo 1F WE5',
    'Consider the boxplot.<br>Describe the distribution in terms of shape, centre, spread and outliers.', KI_S,
    [('<b>S</b> Median towards the right of the box; tail to the left', 'bx:b25y:mm'), ('<b>O</b> No dots', 'bx:b25y:mm'),
     ('<b>C</b> $M = 18$', 'bx:b25y:mm'), (r'<b>S</b> range $= 20 - 12 = 8$', 'bx:b25y:mm')],
    SOCS('negatively skewed', 'are no outliers', '18', 'The range is 8.'),
    ED + ', 1F Worked example 5 (solution set out in SOCS order)',
    fig=bplot('b25y', 12, 20, 0.5, 2, (12, 15, 18, 19, 20), caps=True, W=640, col='#ddd3f3', marks=(('mm', 18, 'M = 18', '#d00000'),)), figw='1fr'))
S.append(qslide('ex', 26, 'Using a boxplot to describe a distribution with outliers', 'Cambridge · Example 26',
    'Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.', KI_S,
    [('<b>S</b> Box and whiskers symmetric', 'bx:b26:mm'), ('<b>O</b> Four dots: 10, 15, 20, 25', 'bx:b26:mm bxo:b26'),
     ('<b>C</b> $M = 41$', 'bx:b26:mm bxo:b26'), (r'<b>S</b> $\text{IQR} = 44.25 - 38.75 = 5.5$, range $= 47 - 10 = 37$', 'bx:b26:mm bxo:b26')],
    SOCS('symmetric', 'are outliers at 10, 15, 20 and 25', '41', 'The IQR is 5.5 and the range is 37.'),
    CG + ', 1G Example 26 (solution set out in SOCS order). No matching Edrolo worked example, so no You try.',
    fig=bplot('b26', 0, 50, 1, 5, (34, 38.75, 41, 44.25, 47), out=(10, 15, 20, 25), W=640, col='#e9c6ea', marks=(('mm', 41, 'M = 41', '#d00000'),)), figw='1fr'))
S.append(qslide('ex', 27, 'Using a boxplot to answer statistical questions', 'Cambridge · Example 27',
    'The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.', KI_S,
    [('<b>S</b> Long tail of dots to the left', 'bx:b27:mm'), ('<b>O</b> Dots at 25 to 34 weeks', 'bx:b27:mm bxo:b27'),
     ('<b>C</b> $M = 39$ weeks', 'bx:b27:mm bxo:b27'), (r'<b>S</b> $\text{IQR} = 40 - 38 = 2$, range $= 42 - 25 = 17$', 'bx:b27:mm bxo:b27')],
    SOCS('negatively skewed', 'are outliers at 25, 26, 27, 28, 29, 30, 31, 32, 33 and 34 weeks', '39 weeks', 'The IQR is only 2 weeks, but the range is 17 weeks.'),
    CG + ', 1G Example 27 (solution set out in SOCS order). No matching Edrolo worked example, so no You try.',
    fig=bplot('b27', 25, 43, 1, 1, (35, 38, 39, 40, 42), out=tuple(range(25, 35)), xl='Gestation period (weeks)', W=640, col='#bcd6f2', marks=(('mm', 39, 'M = 39', '#d00000'),)), figw='1fr', cls='tight'))

# ---- Exit 1: VCAA 2020 E2 Q2c (Edrolo 1E Q19)
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2020 Exam 2 Q2c',
    'The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.' + bigdot('nk', neck, 30, 45, 'neck size (cm)')
    + 'The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.'
    + table_hl('nk5', [('minimum', ['31']), ('first quartile ($Q_1$)', ['36']), ('median', ['38']), ('third quartile ($Q_3$)', ['39']), ('maximum', ['44'])], 'ztab zinq zh5')
    + 'Use the five-number summary to construct a boxplot, showing any outliers if appropriate.', KI_F,
    [r'$\text{IQR} = 39 - 36 = 3$', r'$\text{LF} = 36 - 4.5 = 31.5$, $\text{UF} = 39 + 4.5 = 43.5$',
     ('$31 < 31.5$ and $44 > 43.5$: both are outliers', 'bdx:nk'), ('Whiskers stop at the last values inside the fences: 32 and 43', 'bdx:nk')],
    bplot('nkb', 30, 45, 0.5, 1, (32, 36, 38, 39, 43), out=(31, 44), xl='neck size (cm)', W=560),
    ED + ', 1E Q19 · VCAA 2020 Exam 2 Data analysis Q2c; average 1.1/2 marks (55%), examiner report. Dot plot redrawn. Working by teacher.',
    marks=2, vcaa=55, figw='1.05fr', ans_do='bdx:nk', cls='tight',
    watch='Teacher tip: the whiskers end at 32 and 43 (real values), not at the fences 31.5 and 43.5.'))
# ---- Exit 2: VCAA 2021 E2 Q1e (Edrolo 1E Q20)
hep = [('1.76', '15.34', '41.22'), ('1.79', '16.96', '42.41'), ('1.83', '13.87', '46.53'), ('1.82', '14.23', '40.53'), ('1.87', '13.78', '40.62'), ('1.73', '14.50', '45.62'),
       ('1.68', '15.08', '42.33'), ('1.82', '13.13', '40.88'), ('1.83', '14.22', '39.22'), ('1.87', '13.62', '42.51'), ('1.87', '12.01', '42.75'), ('1.80', '12.88', '38.12'),
       ('1.83', '12.68', '42.65'), ('1.87', '12.45', '41.32'), ('1.78', '11.31', '42.88')]
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2021 Exam 2 Q1e',
    'In the sport of heptathlon, athletes compete in seven events. These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump. '
    'Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games. Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.'
    + table_hl('hp', [('athlete number', [str(i) for i in range(1, 16)]), ('high jump (metres)', [h[0] for h in hep]), ('shot-put (metres)', [h[1] for h in hep]), ('javelin (metres)', [h[2] for h in hep])], 'ztab zinq zhep')
    + 'The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.'
    + bplot('hj', 1.68, 1.88, 0.01, 0.04, (1.68, 1.78, 1.82, 1.87, 1.87), caps=True, xl='high jump (metres)', dec=2, W=600, marks=(('q3', 1.87, 'Q₃ = max = 1.87', '#d00000'),))
    + 'Explain why the boxplot has no whisker at its upper end.', KI_5,
    [('Only the high jump row matters', 'dim:hp:2 dim:hp:3'),
     (r'$n = 15$: $Q_3$ is the middle (4th) of the top 7 values $= 1.87$', 'dim:hp:2 dim:hp:3 bx:hj:q3'),
     ('The largest jump is also 1.87 (four athletes)', 'dim:hp:2 dim:hp:3 bx:hj:q3 tc:hp:104,109,110,113')],
    '$Q_3$ and the maximum are both 1.87 m, so there is nothing for an upper whisker to cover.',
    ED + ', 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e; average 0.5/1 (50%), examiner report. Table transposed to fit (adapted layout); boxplot redrawn.',
    marks=1, vcaa=50, figw='1.25fr', ans_do='dim:hp:2 dim:hp:3 bx:hj:q3 tc:hp:104,109,110,113', cls='tight',
    watch='Teacher tip: name both values. “$Q_3$ = maximum = 1.87 m” is the reason; “there are no data above the box” on its own does not say why.'))

# ---- check-in, coursework
checkin(SC, "Success criteria: one per worked example")
coursework('1G', 'Coursework · Exercise 1G', [('Cambridge Exercise 1G (part 1)', 'Q1–10'), ('Cambridge Exercise 1G (part 2)', 'Q11–20'), ('Practice booklet', '1G section')],
           'Exercise 1G: The five-number summary and the boxplot', CG + ", Exercise 1G")



# ---- lesson-only CSS / JS (everything shared lives in lib/)
LESSON_CSS = r'''
.slide.apkb .zfig{flex-direction:column;gap:2px;justify-content:flex-start!important;padding-top:22px!important}.slide.apkb .zstem table{font-size:19px!important}.slide.apkb .zstem .zkey{font-size:15px;margin-top:2px}.slide.apkb .zfig svg.zbx{max-height:112px;flex:none}.slide.apkb .zcas2 .zcas{font-size:15px!important}.slide.apkb .zstem td{padding-top:0!important;padding-bottom:0!important}
.zw.c2 .zpq.brk{break-before:auto!important;border-top:2px dotted #888!important;padding-top:6px!important}.zw.c2 .zpq.brk:first-child{border-top:none!important}
.slide.tight .zw.c2{column-count:3}
.slide.tight .zw.c2 .st.zs{font-size:18px!important;margin-bottom:4px!important}.slide.tight .zw.c2 .zpq{font-size:17px;margin-bottom:2px}.slide.z .zb.stack .zfig svg.zbx{max-height:165px!important}.slide.z .zb.stack>.zfig{padding:4px 22px!important}.zw.c2 .zpq{break-after:avoid}.slide.p7 .zb.stack .zfig svg.zbx{max-height:135px!important}.slide.p7 .zw.c2 .st.zs{font-size:16px!important}.slide.p7 .zw.c2 .zpq{font-size:16px}.slide.p7 .top>.q{font-size:20px}
.zrow3{display:grid;grid-template-columns:1fr 1fr 1fr 1.3fr;gap:16px;margin-top:6px}
.zrow3 .st{font-size:21px!important;white-space:normal}
.zsh4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;margin:14px 0}
.zsh4 .st{border:2px solid #000;padding:10px;font-size:19px!important;white-space:normal;box-shadow:4px 4px 0 #bbb}
.zsh4 h3{margin:0 0 6px;font-size:22px}
.ztab.zh5{font-size:16px}.ztab.zhep{font-size:12px}.ztab.zhep th,.ztab.zhep td{padding:1px 3px}
.zmc1 .pc{display:none}
.zcas2.zh{flex-direction:row}.zcas2.zh>div{flex:1}.zcas2.zh .zcas{font-size:22px!important}
.zfxo{font-size:20px;line-height:1.55}.zfxo .ol{color:#d00000;font-weight:bold}
'''
LESSON_JS = r'''
// party ages: one guest's age changes; quartiles by the halves method (n = 20)
document.querySelectorAll('.slide.zfx').forEach(sl=>{const sv=sl.querySelector('svg.zfxs'),r=sl.querySelector('input'),O=sl.querySelector('.zfxo');
  const base=[19,21,22,56,34,19,27,28,34,17,37,20,20,21,45,26,19,23,29];
  const md=a=>{const n=a.length,h=Math.floor(n/2);return n%2?a[h]:(a[h-1]+a[h])/2};
  const draw=()=>{const X=+r.value,d=[...base,X].sort((a,b)=>a-b),n=d.length,h=Math.floor(n/2),M=md(d),Q1=md(d.slice(0,h)),Q3=md(d.slice(n-h)),I=Q3-Q1,LF=Q1-1.5*I,UF=Q3+1.5*I;
    const ins=d.filter(v=>v>=LF&&v<=UF),wl=Math.min(...ins),wu=Math.max(...ins),outs=d.filter(v=>v<LF||v>UF);
    const lo=-10,hi=100,px=v=>30+(v-lo)/(hi-lo)*640,cy=110;let s='';
    s+=`<line x1="20" y1="185" x2="690" y2="185" stroke="#000" stroke-width="2"/>`;for(let v=-10;v<=100;v+=10)s+=`<line x1="${px(v)}" y1="179" x2="${px(v)}" y2="191" stroke="#000"/><text x="${px(v)}" y="210" font-size="15" text-anchor="middle">${v<0?'−'+(-v):v}</text>`;
    [[LF,'LF'],[UF,'UF']].forEach(([v,l])=>{s+=`<line x1="${px(v)}" y1="40" x2="${px(v)}" y2="185" stroke="#1f5fbf" stroke-width="2.5" stroke-dasharray="7 5"/><text x="${px(v)}" y="32" font-size="15" font-weight="bold" fill="#1f5fbf" text-anchor="middle">${l} = ${+v.toFixed(2)}</text>`});
    s+=`<line x1="${px(wl)}" y1="${cy}" x2="${px(Q1)}" y2="${cy}" stroke="#000" stroke-width="2.5"/><line x1="${px(Q3)}" y1="${cy}" x2="${px(wu)}" y2="${cy}" stroke="#000" stroke-width="2.5"/>`;
    s+=`<rect x="${px(Q1)}" y="${cy-28}" width="${px(Q3)-px(Q1)}" height="56" fill="#fff" stroke="#000" stroke-width="2.5"/><line x1="${px(M)}" y1="${cy-28}" x2="${px(M)}" y2="${cy+28}" stroke="#000" stroke-width="4"/>`;
    outs.forEach(v=>{s+=`<circle cx="${px(v)}" cy="${cy}" r="7" fill="#fff" stroke="#000" stroke-width="2.5"/>`});
    const xo=X<LF||X>UF;s+=`<path d="M${px(X)} ${cy+38} l-8 14 h16z" fill="${xo?'#d00000':'#555'}"/><text x="${px(X)}" y="${cy+66}" font-size="14" font-weight="bold" text-anchor="middle" fill="${xo?'#d00000':'#555'}">${X}</text>`;
    sv.innerHTML=s;const f=v=>+v.toFixed(2);
    O.innerHTML=`Changed guest: <b>${X}</b><br>$Q_1$ = <b>${f(Q1)}</b>, $M$ = <b>${f(M)}</b>, $Q_3$ = <b>${f(Q3)}</b><br>IQR = <b>${f(I)}</b><br>Fences: <b>${f(LF)}</b> and <b>${f(UF)}</b><br>Outliers: <b>${outs.length?outs.join(', '):'none'}</b><br>`+
      (xo?`<span class="ol">${X} is an outlier: it is ${X>UF?'above the upper':'below the lower'} fence.</span>`:(X===UF||X===LF?`<b style="color:#a06b00">${X} is exactly on the fence: not an outlier.</b>`:`<b>${X} is inside the fences: not an outlier.</b>`));
    if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();r.value=b.dataset.v;draw()});draw()});
'''

build('S4-slides.html', '12MAG S4 · The five-number summary and the boxplot · Slides', css=LESSON_CSS, js=LESSON_JS, css_first=True)
