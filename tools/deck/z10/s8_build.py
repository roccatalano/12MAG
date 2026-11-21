r"""12MAG S8 (2D Two numerical variables, 2E Interpreting a scatterplot) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l05/build.py (planner card gm12-u3-l05; same items, same order). Figure values: tools/deck/l05/figs.py.
python3 tools/deck/z10/s8_build.py  ->  lessons/S8-slides.html
Sources (verbatim; read from the PDFs on G: 15 Nov 2026; figures redrawn, values read off the source figures):
- APK: Cambridge U1&2 Ch 7 skills checklist 7B #3 (p. 457; data of #2; solution written for 12MAG, r = 0.66 checked on CAS -> moderate)
       VCAA 2020 Further Exam 2 Core Q4bi (Edrolo U1&2 6A Q16; original wording; report 78%, answer weight)
- New learning: Cambridge U3&4 2D pp. 130-133 (participation-rate data), 2E pp. 134-138 (direction, form, strength).
- Examples: Cambridge U3&4 Examples 13, 14, 15 (pp. 135-138); Example 15 point clouds redrawn approximately.
- You try: Edrolo U1&2 6B WE3 (p. 329; approximate), 6B WE1 (p. 327; approximate), Edrolo U3&4 2C WE4 (p. 136). CAS You try: Edrolo U3&4 2C WE3 (p. 133).
- CAS: planner/cas-skills.json 'scatterplot'; data Cambridge 2D CAS 1 (test scores).
- Exits: Edrolo U3&4 2C Q15 = VCAA 2018 Further Exam 2 Core Q2b (90%) · 2C Q16 = VCAA 2016 Further Exam 2 Core Q3a (78%; common error 'positively skewed').
"""
import os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'l05'))
from lib.deck import *
from lib.cat import *
from lib.assoc import *
from figs import V18, V16, V20, FOOT, TEST1, TEST2, PART, E13A, E13B, E13C, E14B, E15A, E15B, SLEEP, CROSS, W1, W3
lesson('2D Two numerical variables · 2E Interpreting a scatterplot')




title_slide('Investigating associations between two numerical variables',
            ['2D Investigating associations between two numerical variables (pp. 130–133)', '2E How to interpret a scatterplot (pp. 134–140)'])
LI = ['To be able to introduce the scatterplot for displaying data from two numerical variables.', 'To be able to construct a scatterplot using a CAS calculator.',
      'To be able to use a scatterplot to identify an association between two variables.',
      'From the scatterplot, be able to classify an association according to: direction, which may be positive or negative; form, which may be linear or non-linear; strength, which may be weak, moderate or strong.']
SC = ['I can construct a scatterplot using a CAS calculator.', 'I can classify the direction, form and strength of an association from a scatterplot.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'The scatterplot', 'CAS: scatterplots · You try', 'Direction · Example 13', 'Form · Example 14',
       'Strength · Example 15', 'Exit tasks', 'Check-in and coursework']
overview('2D–2E', LI, SC, SEQ, CG + ', 2D and 2E Learning intentions; success criteria from the planner card', cols='1.2fr 1fr .8fr')

# ---- APK
FT = ('<table class="ztab zsm2"><tr><th>height</th><th>foot length</th><th>height</th><th>foot length</th></tr>'
      + ''.join(f'<tr><td>{FOOT[i][0]}</td><td>{FOOT[i][1]}</td><td>{FOOT[i+8][0]}</td><td>{FOOT[i+8][1]}</td></tr>' for i in range(8)) + '</table>')
KI_DFS = '<b>D</b>irection · <b>F</b>orm · <b>S</b>trength, then <b>O</b>utliers<div class="kn">finish with a sentence in context</div>'
S.append(qslide('apk', '1 of 2', 'Describing an association from a scatterplot', 'Cambridge U1&amp;2 · 7B #3',
    'In order to predict the length of a person’s foot from their height, a group of 16 students collected the following data set, which gives height (<i>height</i>) and the length of their foot (<i>foot length</i>) in centimetres.<br>'
    'Describe the association in the previous scatterplot between height and foot length in terms of direction, form and strength.',
    KI_DFS, [('Direction: points trend upwards left to right → positive', 'sl:a1s'), 'Form: scattered about a straight line → linear',
             'Strength: broadly clustered about the line → moderate', 'Outlier: (185, 40), height 185 cm, foot length 40 cm, sits well above the pattern'],
    'There is a moderate, positive, linear association between foot length and height: taller students tend to have longer feet.', CG12 + ', Chapter 7 skills checklist 7B #3 (data from #2, p. 457; scatterplot drawn for 12MAG). Working by teacher.',
    fig='<div class="zrowc" style="align-items:flex-start">' + FT + '<div class="zfigc" style="flex:1">'
        + scat('a1s', FOOT, (150, 190, 10), (15, 45, 5), 'height (cm)', 'foot length (cm)', seg=((152, 20.5), (186, 33.5)), w=440, h=300)
        + '</div></div>',
    figw='1.6fr', cls='tight'))
BT = '<table class="ztab zsm2"><tr><th><i>Age</i> (years)</th><th><i>Body density</i> (kg/litre)</th><th><i>Weight</i> (kg)</th></tr>' + ''.join(f'<tr><td>{a}</td><td>{b:.2f}</td><td>{c:.1f}</td></tr>' for a, b, c in V20) + '</table>'
S.append(qslide('apk', '2 of 2', 'Explanatory and response variables', 'VCAA 2020 Exam 2 Q4bi',
    'The age, in years, body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 men aged 23 to 25 years are shown in the table below.<br>'
    'A least squares line is to be fitted to the data with the aim of predicting body density from weight.<br>Name the explanatory variable for this least squares line.',
    'Predict <b>RV</b> from <b>EV</b>', ['We predict the RV (body density) <b>from</b> the EV.', 'The variable we predict from: weight.'],
    '<i>weight</i>', ED12 + ', 6A Q16 (VCAA 2020 Further Mathematics Exam 2 Core Q4bi; original wording); % from the examiner report.',
    fig=BT, figw='.8fr', marks=1, vcaa=78, watch='‘predicting A from B’: B is the explanatory variable.'))

keyslide('2D–2E',
    [('Scatterplot', 'a plot of paired numerical data: EV on the horizontal (x) axis, RV on the vertical (y) axis; one point per case'),
     ('Direction', 'positive (RV tends to increase as EV increases), negative (RV tends to decrease) or none'),
     ('Form', 'linear (points follow a straight line) or non-linear (a curve)'),
     ('Strength', 'strong, moderate or weak: how tightly the points cluster about a trend line'),
     ('Outlier', 'a point that does not fit the pattern of the rest')],
    [('Describe an association', 'Direction · Form · Strength, + any outliers, then a sentence in context'),
     ('Sentence template', 'There is a <i>strong, positive, linear</i> association between RV and EV (e.g. ‘taller players tend to be heavier’)')],
    CG + ', 2D pp. 130–131, 2E pp. 134–138')

# ---- the scatterplot
PT_ = '<table class="ztab zsm2"><tr><th>Participation rate (%)</th>' + ''.join(f'<td>{x}</td>' for x, _ in PART) + '</tr><tr><th>Hours worked</th>' + ''.join(f'<td>{y}</td>' for _, y in PART) + '</tr></table>'
S.append(nl_slide('The scatterplot',
    'Two numerical variables → a <b>scatterplot</b>: each point is <b>one case</b> (here, one country); EV on the <b>horizontal (x) axis</b>, RV on the <b>vertical (y) axis</b>. <span class="hint">Click to plot.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col">' + PT_
    + st('<b>1</b> Axes: <i>participation rate</i> (EV) across, <i>hours worked</i> (RV) up.', cls='stp') + st('<b>2</b> One point for each country.', do='sx:lps', cls='stp')
    + st('Read the question: the variable you predict FROM is the EV and goes on the x-axis.', cls='stp ztest') + '</div><div class="col zc">'
    + scat('lps', PART, (0, 60, 10), (30, 55, 5), 'Participation rate (%)', 'Hours worked', build=True, w=520, h=360, r=6) + '</div></div>',
    CG + ', 2D pp. 130–131 (9 countries)'))
TP = '<table class="ztab"><tr><th>Test 1</th>' + ''.join(f'<td>{x}</td>' for x in TEST1) + '</tr><tr><th>Test 2</th>' + ''.join(f'<td>{x}</td>' for x in TEST2) + '</tr></table>'
S.append(qslide('cas', '', 'Constructing a scatterplot', 'Cambridge · 2D CAS 1',
    'Construct a scatterplot for the set of test scores given below. Treat test 1 as the explanatory (i.e. x) variable.' + TP,
    'EV in the x list, RV in the y list', ['Enter the lists <b>test1</b> and <b>test2</b>.', 'Plot test2 against test1.'],
    'test1 on the x-axis, test2 on the y-axis: 9 points, a positive association.', CG + ', 2D CAS 1 (pp. 131–132). CAS steps: planner CAS guide (scatterplot).',
    fig=casbox('scatterplot'), figw='1.2fr'))
CT_ = '<table class="ztab zsm2"><tr><th><i>time</i> (s)</th>' + ''.join(f'<td>{t}</td>' for t, _ in CROSS) + '</tr><tr><th><i>points</i></th>' + ''.join(f'<td>{p}</td>' for _, p in CROSS) + '</tr></table>'
S.append(qslide('yt', 'CAS', 'Constructing a scatterplot on CAS', 'Edrolo 2C WE3',
    '10 students were competing in the school cross-country. Each student’s house would be awarded <i>points</i> based on their placing in the race. The <i>time</i> that it took each student to complete the race and the number of house <i>points</i> they received were recorded.'
    + CT_ + 'With a calculator, use the data in the table to construct a scatterplot.',
    'EV in the x list, RV in the y list', ['Name a list ‘time’ and another list ‘points’ and enter the data.', 'Points are awarded based on time: RV <i>points</i>, EV <i>time</i>.',
                                         ('Plot with the EV on the x-axis.', 'sx:ycs')],
    'Scatterplot of <i>points</i> (y) against <i>time</i> (x), opposite.', ED + ', 2C Worked example 3 (pp. 133–134). Working by teacher.',
    fig=scat('ycs', CROSS, (680, 940, 40), (0, 11, 1), 'time (seconds)', 'points', build=True, w=500, h=340), figw='.9fr', ans_do='sx:ycs'))

# ---- direction
FBP = [(173, 68), (174, 75), (175, 71), (176, 73), (176, 76), (178, 68), (178, 73), (179, 77), (180, 79), (181, 81), (182, 78), (183, 85), (184, 80), (185, 87), (185, 89), (186, 78), (187, 75), (188, 83), (191, 87), (192, 80), (193, 86), (194, 83), (195, 85), (195, 90), (196, 83), (197, 92), (201, 96), (206, 100)]
HWP = [(0, 49), (4, 51), (6, 48), (7, 48.5), (20, 42), (21, 39), (22, 42.5), (26, 39), (27, 38.5), (27, 35), (27, 34.5), (31, 40), (36, 38.5), (37, 36.5), (55, 35)]
S.append(nl_slide('Direction of an association',
    'First: is there a clear pattern? No pattern (a random scatter) → <b>no association</b>. A clear pattern → describe its <b>direction</b>. <span class="hint">Click to reveal.</span>',
    '<div class="zrow2"><div>' + scat('ld1', FBP, (170, 210, 10), (60, 100, 10), 'Height (cm)', 'Weight (kg)', seg=((172, 70), (206, 98)), w=440, h=300, r=4) + 'positive</div><div>'
    + scat('ld2', HWP, (0, 60, 10), (30, 50, 5), 'Participation rate (%)', 'Hours worked', seg=((0, 49.5), (56, 34)), w=440, h=300, r=4) + 'negative</div></div>'
    + st('<b>Positive</b>: points trend <b>upwards</b> left to right (RV tends to increase as EV increases).', do='sl:ld1', cls='stp')
    + st('<b>Negative</b>: points trend <b>downwards</b> left to right. Always say what it means in context: ‘taller players tend to be heavier’.', do='sl:ld1 sl:ld2', cls='stp'),
    CG + ', 2E pp. 134–135 (footballers; 15 countries)'))
KI_DIR = 'Upwards left to right → <b>positive</b>; downwards → <b>negative</b><div class="kn">no pattern → no association</div>'
S.append(qslide('ex', 13, 'Direction of association', 'Cambridge · Example 13',
    'Classify each of the following scatterplots as exhibiting positive, negative or no association. Where there is an association, describe the direction of the association in terms of the variables in the scatterplot and what it means in terms of the variables involved.',
    KI_DIR, [('<b>a</b> The points trend downwards from left to right. The direction of the association is negative. Reaction times tend to decrease as the drug dose increases.', 'sl:w13a'),
             '<b>b</b> There is no pattern in the scatterplot of diameter against age. There is no association between diameter and age.',
             ('<b>c</b> The points trend upwards from left to right. The direction of the association is positive. Taller mothers tend to have taller daughters.', 'sl:w13a sl:w13c')],
    '<b>a</b> negative · <b>b</b> no association · <b>c</b> positive', CG + ', 2E Example 13 (pp. 135–136; scatterplots redrawn)', ans_do='sl:w13a sl:w13c',
    fig='<div class="zrow3"><div>a' + scat('w13a', E13A, (0, 6, 1), (0, 70, 10), 'Dose (mg)', 'Reaction time (min)', seg=((0, 62), (5.5, 8)), w=320, h=250, r=4) + '</div>'
        + '<div>b' + scat('w13b', E13B, (20, 36, 4), (0, 25, 5), 'Age (years)', 'Diameter (cm)', w=320, h=250, r=4) + '</div>'
        + '<div>c' + scat('w13c', E13C, (145, 180, 5), (145, 180, 5), 'Height mother', 'Height daughter', seg=((148, 156), (178, 180)), w=320, h=250, r=4) + '</div></div>',
    stack=True, cls='tight zs16'))
S.append(qslide('yt', 13, 'Interpreting the direction of an association', 'Edrolo U1&amp;2 6B WE3',
    'The relationship between customer satisfaction and burger patty size at a fast food restaurant is shown in the following scatterplot.<br>Interpret the correlation between <i>burger patty diameter</i> and <i>customer satisfaction level</i>.',
    KI_DIR, [('The values follow an upward trend from left to right: positive.', 'sl:y13s'), 'In context: an increase in the EV goes with an increase in the RV.'],
    'An increase in <i>burger patty diameter</i> is associated with an increase in <i>customer satisfaction level</i>.', ED12 + ', 6B Worked example 3 (p. 329; scatterplot redrawn). Working by teacher.',
    fig=scat('y13s', W3, (0, 20, 5), (0, 20, 5), 'burger patty diameter (cm)', 'customer satisfaction level (0–20)', seg=((0, 1), (19, 20.2)), w=500, h=360, r=4), figw='1fr'))

# ---- form
PF = [(x, round(5 * (1 - 2.718 ** (-x / 2.2)), 2)) for x in [0.3, 0.8, 1.2, 1.8, 2.4, 3, 3.6, 4.4, 5, 6, 7, 8, 9, 10]]
VEL = [(0, 1), (0.5, 3.5), (1, 5.5), (1.5, 8), (2, 11), (2.5, 13), (3, 15.5), (3.5, 17), (4, 21), (4.5, 22), (5, 25.5)]
S.append(nl_slide('Form of an association',
    'Linear or non-linear? Imagine a line through the points: if a curve fits better, the form is non-linear. <span class="hint">Click to reveal.</span>',
    '<div class="zrow2"><div>' + scat('lf1', VEL, (0, 5, 1), (0, 30, 5), 'Time (s)', 'Velocity (m/s)', seg=((0, 1), (5, 25.5)), w=440, h=300, r=4) + 'linear</div><div>'
    + scat('lf2', PF, (0, 10, 2), (0, 5, 1), 'Time spent practising', 'Performance level', curve=[(x / 4, 5 * (1 - 2.718 ** (-x / 8.8))) for x in range(0, 41)], w=440, h=300, r=4) + 'non-linear</div></div>'
    + st('<b>Linear</b>: the points tend to follow a <b>straight line</b>.', do='sl:lf1', cls='stp')
    + st('<b>Non-linear</b>: the points tend to follow a <b>curved line</b>. For now we analyse linear associations; non-linear data can often be made linear later.', do='sl:lf1 sl:lf2', cls='stp'),
    CG + ', 2E pp. 136–137'))
KI_FORM = 'Straight line → <b>linear</b>; curve → <b>non-linear</b>'
S.append(qslide('ex', 14, 'Form of an association', 'Cambridge · Example 14',
    'Classify the form of the association in each of scatterplot as linear or non-linear.', KI_FORM, [], None, CG + ', 2E Example 14 (p. 137; scatterplots redrawn)',
    parts=[('a', '', [], 'There is a clear pattern. The points can be imagined to be scattered around a straight line. The association is linear.', 'sl:w14a'),
           ('b', '', [], 'There is a clear pattern. The points can be imagined to be scattered around a curved line rather than a straight line. The association is non-linear.', 'sl:w14a sl:w14b')],
    fig='<div class="zrow2"><div>a' + scat('w14a', E13C, (145, 180, 5), (145, 180, 5), 'Height mother', 'Height daughter', seg=((148, 156), (178, 180)), w=420, h=280, r=4) + '</div>'
        + '<div>b' + scat('w14b', E14B, (1, 7, 1), (0, 14, 2), 'Number of weeks on a diet', 'Weight loss (kg)', curve=[(1.8 + k * 0.13, 12.6 * (1 - 2.718 ** (-(1.8 + k * 0.13 - 1.75) / 1.9))) for k in range(40)], w=420, h=280, r=4) + '</div></div>',
    stack=True))
S.append(qslide('yt', 14, 'Describing strength, direction and form', 'Edrolo U1&amp;2 6B WE1',
    'Consider the following scatterplot.<br>Describe the relationship in terms of strength, direction and form.', KI_DFS,
    [('Strength: a distinct trend, but the points are more spread out: moderate.', None), ('Direction: <i>y</i> tends to increase as <i>x</i> increases: positive.', None),
     ('Form: the trend resembles a straight line: linear.', 'sl:y14s')],
    'Moderate, positive, linear relationship', ED12 + ', 6B Worked example 1 (p. 327; scatterplot redrawn). Working by teacher.',
    fig=scat('y14s', W1, (0, 12, 2), (0, 15, 3), 'x', 'y', seg=((0, 1.5), (11.2, 13.5)), w=500, h=340, r=4), figw='1fr'))

# ---- strength
def cloud(sd, seed, neg=False):
    r = random.Random(seed); return [(x, (10 - x if neg else x) + r.gauss(0, sd)) for x in [r.uniform(0.5, 9.5) for _ in range(16)]]
ROWS = [('Strong', 0.5), ('Moderate', 1.5), ('Weak', 3)]
GRID = '<div class="zgrid6">' + ''.join(f'<div>{scat(f"m{k}{int(ng)}", cloud(sd, k * 7 + (3 if ng else 1), ng), (0, 10, 10), (-3, 13, 16), "", "", w=220, h=170, r=4, grid=False, ticks=False)}<b>{n.lower()} {"negative" if ng else "positive"}</b></div>' for k, (n, sd) in enumerate(ROWS) for ng in (False, True)) + '</div>'
S.append(nl_slide('Strength of an association',
    'How much scatter about a trend line? <b>strong</b>: tightly clustered · <b>moderate</b>: broadly clustered · <b>weak</b>: loosely clustered · no pattern: <b>no association</b>. <span class="hint">Click to reveal.</span>',
    GRID + st('Describe in the order direction, form, strength, then outliers: ‘a strong, negative, linear association’.', cls='stp ztest'),
    CG + ', 2E pp. 137–138 (example plots redrawn)'))
KI_STR = 'Tightly clustered → <b>strong</b>; broadly → <b>moderate</b>; loosely → <b>weak</b>'
S.append(qslide('ex', 15, 'Strength of an association', 'Cambridge · Example 15',
    'Classify the <b>strength</b> of the association in each of the following scatterplots.', KI_STR, [], None, CG + ', 2E Example 15 (p. 138; scatterplots redrawn, points approximate)',
    parts=[('a', '', [], 'The points are loosely clustered. The association is weak.'), ('b', '', [], 'The points are tightly clustered. The association is strong.', 'sl:w15b')],
    fig='<div class="zrow2"><div>a' + scat('w15a', E15A, (5, 25, 5), (5, 45, 10), 'X', 'Y', w=420, h=280, r=3.5) + '</div>'
        + '<div>b' + scat('w15b', E15B, (0, 20, 5), (5, 25, 5), 'X', 'Y', seg=((2, 6.9), (20, 24)), w=420, h=280, r=3.5) + '</div></div>',
    stack=True))
S.append(qslide('yt', 15, 'Strength, direction, form and outliers', 'Edrolo 2C WE4',
    'An investigation into the association between sleep and work performance was conducted. The following scatterplot displays the collected data.<br>Describe the relationship in terms of strength, direction, form and potential outliers.',
    KI_DFS, [('Strength: all points appear very close to the underlying trend: strong.', None), ('Direction: as the EV increases, the RV decreases: negative.', None),
             ('Form: the data best resembles a straight line: linear.', 'sl:y15s'), 'Outliers: no points clearly lie outside the trend.'],
    'The scatterplot displays a strong, negative, linear relationship, with no visible outliers.', ED + ', 2C Worked example 4 (p. 136; scatterplot redrawn). Working by teacher.',
    fig=scat('y15s', SLEEP, (0, 10, 2), (0, 12, 2), 'amount of sleep (hours)', 'number of basic errors', seg=((0, 10.8), (10, 0.3)), w=500, h=340, r=6), figw='1fr'))

# ---- exits
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2018 Exam 2 Q2b',
    'The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>This is called the percentage congestion level.<br>'
    'The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.<br>'
    'A least squares line is to be fitted to the data with the aim of predicting evening congestion level from morning congestion level.<br>The equation of this line is<br>'
    '<i>evening congestion level</i> = 8.48 + 0.922 × <i>morning congestion level</i><br>Name the response variable in this equation.',
    'The RV is the one being <b>predicted</b><div class="kn">left-hand side of the equation; vertical axis</div>',
    ['We predict evening congestion level from morning congestion level.', 'The RV is on the left of the equation, on the y-axis.'],
    '<i>evening congestion level</i>', ED + ', 2C Q15 (VCAA 2018 Further Mathematics Exam 2 Core Q2b; original wording; scatterplot redrawn); % from the examiner report.',
    fig=scat('x1s', V18, (35, 70, 5), (35, 75, 5), 'morning congestion level (%)', 'evening congestion level (%)', w=460, h=320, r=4.5), figw='.9fr', marks=1, vcaa=90, cls='tight',
    watch='name the variable exactly as given: <i>evening congestion level</i>.'))
TT = ('<table class="ztab zxs2"><tr><th>Apparent temperature (°C)</th>' + ''.join(f'<td>{b}</td>' for a, b in V16) + '</tr><tr><th>Actual temperature (°C)</th>' + ''.join(f'<td>{a}</td>' for a, b in V16) + '</tr></table>')
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2016 Exam 2 Q3a',
    'The data in the table below shows a sample of actual temperatures and apparent temperatures recorded at the weather station. A scatterplot of the data is also shown.<br>'
    'The data will be used to investigate the association between the variables <i>apparent temperature</i> and <i>actual temperature</i>.' + TT
    + 'Use the scatterplot to describe the association between <i>apparent temperature</i> and <i>actual temperature</i> in terms of strength, direction and form.',
    KI_DFS, ['Strength: points tightly clustered: strong.', 'Direction: trend upwards: positive.', 'Form: follows a straight line: linear.'],
    'The association is <b>strong, positive and linear</b>.', ED + ', 2C Q16 (VCAA 2016 Further Mathematics Exam 2 Core Q3a; original wording); % from the examiner report.',
    fig='<div class="zfigc">' + scat('x2s', V16, (20, 29, 1), (16, 26, 1), 'actual temperature (°C)', 'apparent temperature (°C)', w=460, h=320, r=4.5) + '<span><i>n</i> = 13 · <i>r</i>² = 0.97</span></div>',
    figw='.9fr', marks=1, vcaa=78, cls='tight', watch='‘positively skewed’ describes one distribution, not an association. Use strength, direction and form.'))

checkin(SC)
coursework('2D–2E', 'Coursework · Exercises 2D and 2E', [('Cambridge Exercise 2D', 'Q1–6'), ('Cambridge Exercise 2E', 'Q1–2'), ('Practice booklet', '2D section (Insight)')],
           'Exercise 2D: Two numerical variables', CG + ', Exercises 2D and 2E; Chapter 2 workbook practice questions', fit=False)

LESSON_CSS = r'''
.slide.zs16 .zw .st.zs,.slide.zs16 .zw .zpq{font-size:15.5px!important;line-height:1.3!important;margin:2px 0!important}

.ztab.zsm2{font-size:14px}.ztab.zsm2 td,.ztab.zsm2 th{padding:1px 5px}
.ztab.zxs2{font-size:12px}.ztab.zxs2 td,.ztab.zxs2 th{padding:1px 3px}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:12px!important}
.zsocs{font-size:16px;line-height:1.4;padding:8px 12px;width:100%;box-sizing:border-box}
.zsocs .zsr{display:flex;gap:8px;align-items:baseline;margin:2px 0}.zsocs .zsr>b{min-width:78px}
.zgrid6{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;text-align:center;font-size:15px;margin:10px 0}
'''
build('S8-slides.html', '12MAG S8 · Investigating associations between two numerical variables · Slides', css=LESSON_CSS)
