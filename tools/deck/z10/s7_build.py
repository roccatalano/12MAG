r"""12MAG S7 (2C Numerical and categorical variables) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l04/build.py (planner card gm12-u3-l04; same items, same order). Figure values: tools/deck/l04/figs.py.
python3 tools/deck/z10/s7_build.py  ->  lessons/S7-slides.html
Sources (verbatim; read from the PDFs on G: 15 Nov 2026; figures redrawn, values read off the source figures):
- CFAT 1.2.1 (2A-2B) at the start (planner card).
- APK: Cambridge U1&2 2I Now try this 27 (p. 114; skills checklist 2I #16; solution written for 12MAG in the Example 27 pattern)
       VCAA 2019 Further Exam 2 Core Q2aii (Edrolo U1&2 1H Q16; report 87%) · VCAA 2021 Further Exam 1 Core Q4 (Edrolo U1&2 1H Q17; report B 60%, A 4, C 10, D 11, E 15)
- New learning: Cambridge U3&4 2C pp. 123-126. Examples 9-12 (pp. 123-127); reports set out in SOCS order, then the conclusion.
- You try: Edrolo U3&4 2B WE2 (pp. 121-122), WE1 (pp. 120-121), WE3 (pp. 122-123), WE4 (p. 124).
- CAS: planner/cas-skills.json 'parallel-boxplots' (data: Cambridge Example 9).
- Exits: Edrolo U3&4 2B Q11 = VCAA 2016 Further Exam 1 Core Q8 (C 45%, A 4, B 21, D 4, E 25) · 2B Q12 = VCAA 2019 Further Exam 2 Core Q3 (36% full marks;
         boxplots redrawn horizontally) · 2B Q13 = VCAA 2017 Further Exam 2 Core Q2e (43% full marks).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'l04'))
from lib.deck import *
from lib.cat import *
from lib.assoc import *
from figs import EX9, EX10, EX11, EX12, YT1, YT2, YT3, YT4, NT27, V19Q2, V21Q4, V19Q3, V17
lesson('2C Numerical and categorical variables')


def b2(id_, data, lab, key=''):
    st_, l, r = data
    return b2b(id_, [' '.join(x) for x in l], [' '.join(x) for x in r], st_, lab, key)


def cfat(code, topic, covers, marks):
    S.append(f'<section class="slide z cfat">{bar(code, topic)}'
             '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
             f'<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · {marks} marks</li>'
             f'<li>Covers {covers}</li><li>Pens down when the timer ends</li></ul></div>'
             '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
             '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
             f'{foot(code + " (" + covers + "): student copy and solutions on the planner")}</section>')




title_slide('Investigating the association between a numerical and a categorical variable',
            ['2C Investigating the association between a numerical and a categorical variable (pp. 123–131)'])
LI = ['To be able to use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable for small data sets.',
      'To be able to use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable for small data sets.',
      'To be able to use parallel boxplots to display the association between a numerical variable and a categorical variable which can take two or more values.']
SC = ['I can use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable.',
      'I can use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable.',
      'I can use parallel boxplots to display and describe the association between a numerical variable and a categorical variable.']
SEQ = ['CFAT 1.2.1 (20 minutes, 2A–2B)', 'Activating prior knowledge', 'Key ideas and formulas', 'Comparing groups with SOCS', 'Parallel dot plots · Example 9',
       'Back-to-back stem plots · Example 10', 'Parallel boxplots · Examples 11, 12', 'CAS: parallel boxplots', 'Exit tasks', 'Check-in and coursework']
overview('2C', LI, SC, SEQ, CG + ', 2C Learning intentions; success criteria: one per display', cols='1.15fr 1.05fr .8fr')
cfat('CFAT 1.2.1', 'Explanatory and response variables, two-way tables', '2A–2B', 17)

# ---- APK
KI_CS = 'Compare <b>centre</b> (medians) and <b>spread</b> (IQRs)<div class="kn">quote the value for every group, then conclude</div>'
S.append(qslide('apk', '1 of 3', 'Comparing two groups with a stem plot', 'Cambridge U1&amp;2 · 2I #16',
    'The following back-to-back stem plot displays the distributions of the number of hours per week spent relaxing by a group of 17 males and 16 females.<br>'
    'Use the back-to-back stem plot and the summary statistics provided to compare these distributions in terms of centre and spread, and draw an appropriate conclusion.',
    KI_CS, ['Centre: compare the medians: males 30 hours, females 24.5 hours.', 'Spread: compare the IQRs: males 14.5 hours, females 19 hours.'],
    'The median time spent relaxing for males (M = 30 hours) was higher than for females (M = 24.5 hours). The spread for males (IQR = 14.5 hours) was lower than for females (IQR = 19 hours). In conclusion, the males spent more time relaxing than the females, and their times were less variable.',
    CG12 + ', 2I Now try this 27 (p. 114), skills checklist 2I #16. Solution written for 12MAG in the Example 27 pattern.',
    fig='<div class="zfigc">' + b2('a1s', NT27, ('Males', 'Females'), '1|2 = 21 hours (males) · 1|6 = 16 hours (females)')
        + '<div class="zrowc" style="gap:40px;font-size:18px"><span>Males: M = 30 hours<br>IQR = 14.5 hours</span><span>Females: M = 24.5 hours<br>IQR = 19 hours</span></div></div>', figw='.9fr', cls='tight'))
S.append(qslide('apk', '2 of 3', 'Reading parallel boxplots', 'VCAA 2019 Exam 2 Q2aii',
    'The parallel boxplots below show the <i>maximum daily temperature</i> and <i>minimum daily temperature</i>, in degrees Celsius, for 30 days in November 2017.<br>'
    'Use the information in the boxplots to complete the following sentence.<br>For November 2017, the median value for <i>maximum daily temperature</i> was ☐ °C higher than the median value for <i>minimum daily temperature</i>.',
    'The <b>median</b> is the line inside the box', ['Median, maximum: 25 °C', 'Median, minimum: 15 °C', '25 − 15 = 10'],
    '<b>10</b> °C', ED12 + ', 1H Q16 (VCAA 2019 Further Mathematics Exam 2 Core Q2aii); % from the examiner report. Boxplots redrawn.',
    fig=pbox([('maximum', V19Q2[0][1], V19Q2[0][2]), ('minimum', V19Q2[1][1], V19Q2[1][2])], 6, 30, 2, 'daily temperature (°C)', w=620, lab_w=110),
    figw='1.1fr', marks=1, vcaa=87, watch='read the scale carefully: each tick is 2 °C.'))
OPTDIST['3 of 3'] = [4, 60, 10, 11, 15]
S.append(qslide('apk', '3 of 3', 'Reading parallel boxplots', 'VCAA 2021 Exam 1 Q4',
    'The boxplots below show the distribution of the length of fish caught in two different ponds, Pond A and Pond B.<br>Based on the boxplots above, it can be said that',
    'Each whisker and each half of the box holds about <b>25%</b> of the data',
    ['Pond B’s median is to the right of Pond A’s maximum: the top 50% of Pond B are longer than every fish in Pond A.'],
    '50% of the fish in Pond B are longer than all of the fish in Pond A.', ED12 + ', 1H Q17 (VCAA 2021 Further Mathematics Exam 1 Core Q4; original wording); % from the examiner report. Boxplots redrawn.',
    fig=pbox(V21Q4, 0, 12, 1, 'length', w=520, lab_w=80, minor=0.5), figw='.9fr', marks=1, vcaa=60, cls='tight',
    opts=[('A', '50% of the fish caught in Pond A are the same length as the fish caught in Pond B.'), ('B', '50% of the fish caught in Pond B are longer than all of the fish caught in Pond A.'),
          ('C', '50% of the fish caught in Pond B are shorter than all of the fish caught in Pond A.'), ('D', '75% of the fish caught in Pond A are shorter than all of the fish caught in Pond B.'),
          ('E', '75% of the fish caught in Pond B are longer than all of the fish caught in Pond A.')], key='B'))

keyslide('2C',
    [('Parallel dot plots', 'a dot plot for each group, one above the other, on the same scale'),
     ('Back-to-back stem plot', 'two groups share one stem: leaves to the left for one group, to the right for the other'),
     ('Parallel boxplots', 'a boxplot for each group on the same scale (any number of groups)'),
     ('Association (numerical + categorical)', 'the distribution of the numerical variable (RV) changes from group to group of the categorical variable (EV)')],
    [('Compare with SOCS', 'Shape · Outliers · Centre (median) · Spread (IQR): quote the value for EVERY group'),
     ('Interquartile range', r'$\text{IQR} = Q_3 - Q_1$'),
     ('Outlier fences', r'below $Q_1 - 1.5 \times \text{IQR}$ or above $Q_3 + 1.5 \times \text{IQR}$')],
    CG + ', 2C pp. 123–126')

S.append(nl_slide('Comparing a numerical variable across groups',
    'Does <i>test score</i> (numerical) depend on <i>attended revision class</i> (yes / no, categorical)? Draw one display per group <b>on the same scale</b>, then compare. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1.15fr"><div class="col"><h2>Which display?</h2>'
    + st('Small data sets: <b>parallel dot plots</b> or a <b>back-to-back stem plot</b>', cls='stp') + st('Any size, two or more groups: <b>parallel boxplots</b>', cls='stp')
    + '</div><div class="col"><h2>Compare the groups with SOCS</h2>'
    + st('<b>S</b>hape: symmetric / skewed, for each group (hard to see in small data sets)', cls='stp') + st('<b>O</b>utliers: any, and where', cls='stp')
    + st('<b>C</b>entre: <b>medians</b>: higher or lower?', cls='stp') + st('<b>S</b>pread: <b>IQRs</b>: more or less variable?', cls='stp')
    + st('<b>Conclude</b>: noticeably different → the variables <b>are associated</b>; much the same → <b>no association</b>', cls='stp') + '</div></div>'
    + st('Quote the value for every group (‘M = 26 before, M = 32 after’). Use medians and IQRs, not means: they are not affected by outliers.', cls='stp ztest'),
    CG + ', 2C pp. 123–125 (SOCS order for 12MAG)'))

# ---- Examples 9-12 and You trys
D = '<span>$</span>'   # a dollar sign KaTeX leaves alone
def rep(lines, concl):
    """SOCS comparison report as working steps: one verbatim line per letter (None = skip), then the conclusion is the answer."""
    lab = ['<b>S</b>hape', '<b>O</b>utliers', '<b>C</b>entre', '<b>S</b>pread']
    return [f'{l}: {x}' for l, x in zip(lab, lines) if x], concl
KI_SOCSC = 'Compare with <b>SOCS</b>: medians and IQRs for every group<div class="kn">differences → associated</div>'
st9, a9 = rep([None, None, 'The median number of sit-ups performed after attending the gym program (M = 32) is higher than the median number of sit-ups performed before attending the gym program (M = 26).',
               'The variability in the number of sit-ups has also increased from IQR = 6 to IQR = 10.'], 'Thus we can conclude that the number of sit-ups performed is associated with completing the gym program.')
S.append(qslide('ex', 9, 'Using a parallel dot plot to identify and describe associations', 'Cambridge · Example 9',
    'The parallel dot plots below display the distribution of the number of sit-ups performed by 15 people before and after they had completed a gym program.<br>'
    'Do the parallel dot plots support the contention that the number of sit-ups performed is associated with completing the gym program? Write a brief explanation that compares the distributions.',
    KI_SOCSC, ['RV: <i>sit-ups</i> · EV: <i>gym program</i>. 15 values: M = 8th dot, Q<sub>1</sub> = 4th, Q<sub>3</sub> = 12th. Before: M = 26, IQR = 30 − 24 = 6; after: M = 32, IQR = 36 − 26 = 10.'] + st9,
    a9, CG + ', 2C Example 9 (pp. 123–124; dot plots redrawn; report in SOCS order)',
    fig=pdots('w9d', [('Before', EX9[0][1]), ('After', EX9[1][1])], 22, 54, 2, 'number of sit-ups', w=600, row=110, lab_w=80), figw='1fr', cls='tight zs16'))
S.append(qslide('yt', 9, 'Constructing parallel dot plots', 'Edrolo 2B WE2',
    'A grade 5/6 class took a maths test on fractions. The <i>number of marks</i>, by grade, was recorded.<br>Grade 5: &nbsp;2 &nbsp;4 &nbsp;5 &nbsp;5 &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;9<br>Grade 6: &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;9 &nbsp;9 &nbsp;9 &nbsp;10',
    'One dot plot per group on the <b>same scale</b><div class="kn">stack repeated values</div>', [], None, ED + ', 2B Worked example 2 (pp. 121–122). Working by teacher.',
    parts=[('a', 'Construct parallel dot plots to display this data.', ['Two identical axes, 2 to 10; a dot for each value, stacking repeats.'], 'The parallel dot plots opposite.', 'tf:y9f:a'),
           ('b', 'Which grade has a larger range of <i>number of marks</i>?', ['Grade 5: 9 − 2 = 7 marks · Grade 6: 10 − 5 = 5 marks'], 'Grade 5')],
    fig='<div class="zrep zhid" id="y9f"><span class="zrb" data-f="a">' + pdots('y9d', [('Grade 5', YT2[0][1]), ('Grade 6', YT2[1][1])], 2, 10, 1, 'number of marks', w=560, row=110, lab_w=90) + '</span></div>', figw='1fr'))
st10, a10 = rep([None, None, 'The median life expectancy has increased between 1970 and 2010, from M = 67 years to M = 76 years.',
                 'Over the same period life expectancy has also become less variable (IQR in 1970 = 12.5 years; IQR in 2010 = 8 years).'], 'There is an association between year and life expectancy.')
S.append(qslide('ex', 10, 'Using a back-to-back stem plot to identify and describe associations', 'Cambridge · Example 10',
    'The back-to-back stem plot below displays the distribution of life expectancy (in years) for the same 13 countries in 1970 and 2010.<br>Do the back-to-back stem plots support the contention that life expectancy has changed between these two time periods?',
    KI_SOCSC, ['RV: <i>life expectancy</i> · EV: <i>year</i> (two values: treated as categorical). 13 values: M = 7th. 1970: M = 67, IQR = 12.5 · 2010: M = 76, IQR = 8.'] + st10,
    a10, CG + ', 2C Example 10 (pp. 124–125; report in SOCS order)', fig=b2('w10s', EX10, ('1970', '2010'), '2|5 = 52 years · 6|7 = 67 years'), figw='.8fr', cls='tight'))
S.append(qslide('yt', 10, 'Constructing a back-to-back stem plot', 'Edrolo 2B WE1',
    'The ‘Abbotsford Avengers’ soccer team beat the ‘East Melbourne Eagles’ in the final. In order for the ‘East Melbourne Eagles’ to see what they needed to improve on, they collected the <i>successful passes</i> (%) for each member of both teams.<br>'
    'Abbotsford Avengers: 64 68 70 53 57 62 74 77 36 41 66<br>East Melbourne Eagles: 59 90 83 87 88 76 82 83 91 78 75',
    'Shared stems in the middle<div class="kn">leaves increase moving <b>away</b> from the stem; add a key</div>', [], None, ED + ', 2B Worked example 1 (pp. 120–121). Working by teacher.',
    parts=[('a', 'Construct a back-to-back stem plot to display this data, with the ‘Abbotsford Avengers’ on the left.',
            ['Stems 3 to 9; Avengers left, Eagles right; key 5 | 9 = 59%.'], 'The back-to-back stem plot opposite.', 'tf:y10f:a'),
           ('b', 'Which team had a higher median <i>successful passes</i>?', ['11 players: the 6th value. Avengers 64% · Eagles 83%'], 'East Melbourne Eagles')],
    fig='<div class="zrep zhid" id="y10f"><span class="zrb" data-f="a">' + b2('y10s', YT1, ('Abbotsford Avengers', 'East Melbourne Eagles'), 'Key: 5 | 9 = 59%') + '</span></div>', figw='.9fr'))

# ---- parallel boxplots
S.append(nl_slide('Using parallel boxplots to compare groups',
    'One boxplot for each category of the EV, all on the <b>same axis</b>: the most common display for a numerical RV and a categorical EV. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1.2fr .8fr"><div class="col zc">' + pbox(EX11, 40, 120, 10, 'Resting pulse rate', w=640, row=84, lab_w=90, minor=5)
    + '</div><div class="col"><h2>Read off each group</h2>' + st('<b>Centre</b>: the median line', cls='stp') + st('<b>Spread</b>: box length = IQR', cls='stp')
    + st('<b>Shape</b>: whiskers and median position', cls='stp') + st('<b>Outliers</b>: the separate dots', cls='stp')
    + st('Each section (whisker, half-box) holds about 25% of the group. Compare with SOCS, then say whether the variables are associated.', cls='stp') + '</div></div>',
    CG + ', 2C p. 125 (pulse-rate boxplots, Example 11)'))
st11, a11 = rep(['The distributions of resting pulse rates for both male and female students were approximately symmetric.', 'One male was found to have an extremely low pulse rate of 40, while another had an extremely high pulse rate of 120.',
                 'On average, the resting pulse rate for males is lower (median: male = 65, female = 72)', 'and less variable than that for females (IQR: male = 10, female = 15).'],
                'There is an association between resting pulse rate and gender.')
S.append(qslide('ex', 11, 'Comparing distributions across two groups using parallel boxplots', 'Cambridge · Example 11',
    'Use the following parallel boxplots to compare the pulse rates (in beats/minute) for a group of 70 male students and 90 female students.',
    KI_SOCSC, st11, a11, CG + ', 2C Example 11 (pp. 125–126; boxplots redrawn; report in SOCS order)',
    fig=pbox(EX11, 40, 120, 10, 'Resting pulse rate', w=620, row=90, lab_w=90, minor=5), figw='1fr', cls='tight zs16'))
S.append(qslide('yt', 11, 'Constructing parallel boxplots', 'Edrolo 2B WE3',
    'Daniel went to his local cafe every Sunday for a year and counted the number of people wearing Salomon shoes and the number of people wearing Crocs. The five-number summaries for both shoe brands are recorded.<br>Salomons: 2, 4, 5, 9, 15<br>Crocs: 0, 2, 4, 7, 8',
    'One axis for every group<div class="kn">box Q₁ to Q₃, median line, whiskers to min and max</div>', [], None, ED + ', 2B Worked example 3 (pp. 122–123). Working by teacher.',
    parts=[('a', 'Construct parallel boxplots to display this data.', ['One axis, 0 to 15. Salomons: box 4 to 9, median 5, whiskers 2 and 15. Crocs: box 2 to 7, median 4, whiskers 0 and 8.'],
            'The parallel boxplots opposite.', 'tf:y11f:a'),
           ('b', 'For which shoe brand was the <i>number of people</i> positively skewed?', ['Long right whisker, median near Q₁.'], 'Salomons')],
    fig='<div class="zrep zhid" id="y11f"><span class="zrb" data-f="a">' + pbox(YT3, 0, 15, 1, 'number of people', w=560, row=90, lab_w=100) + '</span></div>', figw='1fr', cls='tight zs16'))
st12, a12 = rep(['The shape of the distribution of salaries changes with age group, from symmetric for 20−29-year-olds, to progressively more positively skewed as age increases.',
                 f'There are no outliers in the 20-29 and 30-39 age group. Outliers also begin to appear at {D}110 000 for the 40-49 age group, and at {D}119 000, {D}126 000 and {D}140 000 for the 50-65 age group.',
                 f'The median salaries increase across the age groups, from {D}64 000 for 20−29 year-olds to {D}72 000 for 50−65 year-olds.',
                 f'The salaries also became more variable, with the IQR increasing from around {D}12 000 for 20−29-year-olds to around {D}20 000 for 50−65-year-olds.'],
                'In this industry there is an association between salary and age group.')
S.append(qslide('ex', 12, 'Comparing distributions across more than two groups using parallel boxplots', 'Cambridge · Example 12',
    'Use the parallel boxplots below to compare the salary distribution for workers in a certain industry across four different age groups: 20–29 years, 30–39 years, 40–49 years and 50–65 years.',
    KI_SOCSC, st12, a12, CG + ', 2C Example 12 (pp. 126–127; boxplots redrawn; report in SOCS order)',
    fig=pbox(EX12, 40, 140, 10, 'Salary ($’000)', w=620, row=70, lab_w=110, minor=2), figw='1fr', cls='tight zs16'))
st12y, a12y = rep(['In relation to shape, the distribution of price is positively skewed in locations further from a city in NSW and approximately symmetrical in the inner suburbs.', None,
                   'In relation to centre, the median price increases as the location is closer to a city in NSW.', 'In relation to spread, the range and IQR of price tends to be larger in locations closer to a city in NSW.'],
                  'The parallel boxplots show that price and location are associated. The closer a 3-bedroom house is to a city in NSW, the higher the price of the house.')
S.append(qslide('yt', 12, 'Writing a report from parallel boxplots', 'Edrolo 2B WE4',
    'The following parallel boxplots display the distribution of prices for a 3-bedroom house in three different locations in NSW: ‘rural’, ‘outer suburbs’ and ‘inner suburbs’.<br>Identify the association between <i>price</i> and <i>location</i>.<br>Write a report referencing shape, centre and spread.',
    KI_SOCSC, st12y, a12y, ED + ', 2B Worked example 4 (p. 124; boxplots redrawn; report in SOCS order). Working by teacher.',
    fig=pbox(YT4, 0, 2.4, 0.4, 'price ($000 000’s)', w=620, row=80, lab_w=130, minor=0.2), figw='1fr', cls='tight zs16'))
# ---- CAS
S.append(qslide('cas', '', 'Creating parallel boxplots', 'Data: Cambridge Example 9',
    'Use your CAS to draw parallel boxplots of the sit-ups data from Example 9, and read off each five-number summary.<br>Before: 22, 22, 23, 24, 25, 26, 26, 26, 28, 29, 29, 30, 31, 34, 46<br>After: 24, 25, 25, 26, 28, 30, 30, 32, 33, 34, 35, 36, 43, 50, 54',
    'TI-Nspire: one list <b>situps</b> (all 30 values), one list <b>program</b>. ClassPad: <b>list1</b> = before, <b>list2</b> = after.',
    ['Enter the data, then draw the boxplots.', 'Read each five-number summary (Trace).'], 'Before: 22, 24, 26, 30, 34, outlier 46 · After: 24, 26, 32, 36, 50, outlier 54',
    CG + ', 2C Example 9 (data). CAS steps: planner CAS guide (parallel-boxplots).', fig=casbox('parallel-boxplots'), figw='1.2fr'))

# ---- Exits
OPTDIST['1 of 3'] = [4, 21, 45, 4, 25]
S.append(qslide('exit', '1 of 3', 'Show what you know', 'VCAA 2016 Exam 1 Q8',
    'Parallel boxplots would be an appropriate graphical tool to investigate the association between the monthly median rainfall, in millimetres, and the',
    'Parallel boxplots: one <b>numerical</b> and one <b>categorical</b> variable', ['Monthly median rainfall is numerical, so the other variable must be categorical.', 'Only month of the year is categorical.'],
    'month of the year', ED + ', 2B Q11 (VCAA 2016 Further Mathematics Exam 1 Core Q8); % from the examiner report.', figw='1fr', marks=1, vcaa=45,
    opts=[('A', 'monthly median wind speed, in kilometres per hour.'), ('B', 'monthly median temperature, in degrees Celsius.'), ('C', 'month of the year (January, February, March, etc.).'),
          ('D', 'monthly sunshine time, in hours.'), ('E', 'annual rainfall, in millimetres.')], key='C'))
T2 = ('<table class="ztab zsm2"><tr><th><i>Month</i></th><th>Minimum</th><th>Q<sub>1</sub></th><th>Median</th><th>Q<sub>3</sub></th><th>Maximum</th></tr>'
      '<tr><td>February</td><td>5.9</td><td>9.5</td><td>10.9</td><td>13.9</td><td>22.2</td></tr><tr><td>May</td><td>3.3</td><td>6.0</td><td>7.5</td><td>9.8</td><td>12.7</td></tr>'
      '<tr><td>July</td><td>1.6</td><td>3.7</td><td>5.0</td><td>5.9</td><td>7.7</td></tr></table>')
S.append(qslide('exit', '2 of 3', 'Show what you know', 'VCAA 2019 Exam 2 Q3',
    'The five-number summary for the distribution of <i>minimum daily temperature</i> for the months of February, May and July in 2017 is shown in Table 2.<br>The associated boxplots are shown below the table.'
    + '<div class="zfigc"><b style="font-size:15px">Table 2. Five-number summary for <i>minimum daily temperature</i></b>' + T2 + '</div>'
    + 'Explain why the information given above supports the contention that <i>minimum daily temperature</i> is associated with the <i>month</i>. Refer to the values of an appropriate statistic in your response.',
    'Quote <b>one statistic</b> (the median) for <b>every</b> group<div class="kn">say how it changes</div>',
    ['Use the median, for all three months.', 'It decreases from month to month: that change signals an association.'],
    'The median <i>minimum daily temperature</i> decreases from February (10.9 °C) to May (7.5 °C) to July (5.0 °C), so <i>minimum daily temperature</i> is associated with <i>month</i>.',
    ED + ', 2B Q12 (VCAA 2019 Further Mathematics Exam 2 Core Q3); % = full marks, from the examiner report. Boxplots redrawn horizontally.',
    fig=pbox(V19Q3, 0, 24, 2, 'minimum daily temperature (°C)', w=560, row=50, lab_w=100), figw='.9fr', marks=2, vcaa=36, cls='tight',
    watch='quote the statistic for <b>every</b> month; one or two values, or no values, lost marks.'))
S.append(qslide('exit', '3 of 3', 'Show what you know', 'VCAA 2017 Exam 2 Q2e',
    'The back-to-back stem plot below displays the <i>wingspan</i>, in millimetres, of 32 moths and their <i>place of capture</i> (forest or grassland).<br>'
    'The back-to-back stem plot suggests that <i>wingspan</i> is associated with <i>place of capture</i>.<br>Explain why, quoting the values of an appropriate statistic.',
    'Use the <b>median</b> (not the mean: there is an outlier)<div class="kn">quote both values</div>',
    ['Forest median: 13 moths, the 7th value = 21 mm', 'Grassland median: 19 moths, the 10th value = 30 mm'],
    'The median <i>wingspan</i> of moths captured in the grassland (30 mm) is higher than that of moths captured in the forest (21 mm). The medians differ, so <i>wingspan</i> is associated with <i>place of capture</i>.',
    ED + ', 2B Q13 (VCAA 2017 Further Mathematics Exam 2 Core Q2e); % = full marks, from the examiner report.',
    fig=b2('x3s', V17, ('forest (n = 13)', 'grassland (n = 19)'), 'key: 1|8 = 18 · wingspan (mm)'), figw='.85fr', marks=2, vcaa=43,
    watch='the mean is not suitable here: the forest moth with a 52 mm wingspan is an outlier.'))

checkin(SC)
coursework('2C', 'Coursework · Exercise 2C', [('Cambridge Exercise 2C', 'Q1–10'), ('Practice booklet', '2C section (Insight + skill sheet)')],
           'Exercise 2C: Numerical and categorical', CG + ', Exercise 2C; Chapter 2 workbook practice questions')

LESSON_CSS = r'''
.slide.zs16 .zw .st.zs,.slide.zs16 .zw .zpq{font-size:15.5px!important;line-height:1.3!important;margin:2px 0!important}

.ztab.zsm2{font-size:15px}.ztab.zsm2 td,.ztab.zsm2 th{padding:1px 6px}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:14px!important}
.zsocs{font-size:16px;line-height:1.4;padding:8px 12px;width:100%;box-sizing:border-box}
.zsocs .zsr{display:flex;gap:8px;align-items:baseline;margin:2px 0}.zsocs .zsr>b{min-width:16px}
.slide.w12s .zsocs{font-size:13.5px;line-height:1.3}
.zrep.zhid{border:none;padding:0;background:none;width:100%}.zrep.zhid .zrb{border:none;display:block;width:100%}
.zrep.zhid .zrb>*{opacity:0;transition:opacity .4s}.zrep.zhid .zrb.on>*{opacity:1}
.zb2b{font-size:22px}
'''
build('S7-slides.html', '12MAG S7 · Investigating the association between a numerical and a categorical variable · Slides', css=LESSON_CSS)
