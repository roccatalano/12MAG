r"""12MAG S1 (1A Types of data, 1B Categorical data) rebuilt in the 10MA slide house style.
Built on the slide library tools/deck/z10/lib (rules: tools/deck/z10/HOWTO.md).
python3 tools/deck/z10/s1_build.py  ->  lessons/S1-slides.html
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.cat import *
lesson('1A Types of data · 1B Categorical data')
# S1 = 1A Types of data + 1B Categorical data. Content sources (verbatim, already cited): tools/deck/s1/build.py (old S1 deck, in git history),
# planner/unit-plan.json card gm12-u3-s1, planner/cas-skills.json 'stats-list'. % correct as in the old deck (examiner reports).
EDR12 = 'Edrolo General Mathematics Units 1&amp;2'
title_slide('Types of data and categorical data', ['1A Types of data', '1B Displaying and describing the distributions of categorical variables'])
LI = ['To be able to classify data as categorical or numerical.', 'To be able to further classify categorical data as nominal or ordinal.',
      'To be able to further classify numerical data as discrete or continuous.', 'To be able to construct frequency and percentage frequency tables for categorical data.',
      'To be able to construct bar charts and percentage bar charts from frequency tables.', 'To be able to interpret and describe frequency tables and bar charts.',
      'To be able to answer statistical questions about a categorical variable.']
SC = ['I can identify types of data.', 'I can construct a frequency table for categorical data.', 'I can construct a bar chart from a frequency table.',
      'I can construct a percentage segmented bar chart from a frequency table.', 'I can describe the distribution of a categorical variable.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Types of variable · Example 1', 'Sort it', 'CAS: setting up the statistics app',
       'Frequency tables · Example 2', 'Bar charts · Example 3', 'Segmented bar charts · Example 4', 'Describing the distribution · Example 5', 'Exit tasks', 'Check-in and coursework']
overview('1A–1B', LI, SC, SEQ, CG + ", 1A and 1B Learning intentions; success criteria: one per worked example", cols='1.1fr 1fr .9fr')

# APK 1: Cambridge U1&2 2A #1
KI_TYPES = 'Categorical: <b>nominal</b> (names only) or <b>ordinal</b> (names and orders)<div class="kn">Numerical: <b>discrete</b> (counted) or <b>continuous</b> (measured)</div>'
S.append(qslide('apk', '1 of 3', 'Year 11 skills: types of data', 'Cambridge U1&amp;2 · 2A #1',
    'Classify the following data as nominal, ordinal, discrete or continuous:', KI_TYPES, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2A #1. Working by teacher.',
    parts=[('a', 'The time between people arriving at the coffee shop.', [], '<b>Continuous</b>: time is measured.'),
           ('b', 'The number of people in the queue at the coffee shop.', [], '<b>Discrete</b>: people are counted.'),
           ('c', 'Customer’s coffee preference (latte, cappuccino, black).', [], '<b>Nominal</b>: the categories only name the coffee.'),
           ('d', 'Customer’s rating of the coffee (excellent, quite good, not that good).', [], '<b>Ordinal</b>: the ratings have a natural order.')], cls='tight'))
# APK 2: VCAA 2021 E1 Q1 (Edrolo U1&2 1A Q13)
OPTDIST['2 of 3'] = [70, 3, 21, 4, 2]
S.append(qslide('apk', '2 of 3', 'A real VCAA question you can already do', 'VCAA 2021 Exam 1 Q1',
    'The percentage segmented bar chart provided shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).'
    '<br>The variables <i>age</i> (under 55 years, 55 years and over) and <i>preferred travel destination</i> (domestic, international) are',
    KI_TYPES, ['<i>age</i> is recorded in two groups (under 55, 55 and over), not as a number of years: categorical.',
               '<i>preferred travel destination</i>: domestic or international names a group: categorical.'],
    'both categorical variables.', EDR12 + ', 1A Q13 (VCAA 2021 Exam 1 Data analysis Q1); % from the examiner report. Chart redrawn.',
    fig=schart('a2s', [('under 55', [65, 35]), ('55 and over', [45, 55])], ['domestic', 'international'], 100, 20, 'percentage', 'age', full=True, w=520),
    figw='1.35fr', marks=1, vcaa=70, opts=[('A', 'both categorical variables.'), ('B', 'both numerical variables.'), ('C', 'a numerical variable and a categorical variable respectively.'),
    ('D', 'a categorical variable and a numerical variable respectively.'), ('E', 'a discrete variable and a continuous variable respectively.')], key='A'))
# APK 3: VCAA 2020 E1 Q10 (Edrolo U1&2 1A Q14)
NT = ('<table class="ztab"><tr><th></th><th colspan="2"><i>snores</i></th><th></th></tr><tr><th><i>frequency of nightmares</i></th><th>no</th><th>yes</th><th>total</th></tr>'
      '<tr><td>low</td><td>80</td><td>58</td><td>138</td></tr><tr><td>high</td><td>11</td><td>12</td><td>23</td></tr><tr><td>total</td><td>91</td><td>70</td><td>161</td></tr></table>')
OPTDIST['3 of 3'] = [57, 5, 3, 24, 11]
S.append(qslide('apk', '3 of 3', 'And another', 'VCAA 2020 Exam 1 Q10',
    'The data in the table shown was collected in a study of the association between the variables <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes).'
    + NT + 'The variables in this study, <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes), are',
    KI_TYPES, ['<i>frequency of nightmares</i>: low and high have a natural order: ordinal.', '<i>snores</i>: no and yes only name a group: nominal.'],
    'ordinal and nominal respectively.', EDR12 + ', 1A Q14 (VCAA 2020 Exam 1 Data analysis Q10); % from the examiner report.',
    figw='1.15fr', marks=1, vcaa=57, opts=[('A', 'ordinal and nominal respectively.'), ('B', 'nominal and ordinal respectively.'), ('C', 'both numerical.'), ('D', 'both ordinal.'), ('E', 'both nominal.')], key='A'))

# Key ideas
KD = [('Categorical variable', 'names a quality or group: <b>nominal</b> (names only) or <b>ordinal</b> (names and orders)'),
      ('Numerical variable', 'a quantity: <b>discrete</b> (counted, ‘How many?’) or <b>continuous</b> (measured, ‘How much?’)'),
      ('Frequency table', 'lists each category and how often it occurs: as a number and as a percentage'),
      ('Bar chart', 'one bar per category, with gaps; height = frequency'),
      ('Percentage segmented bar chart', 'one 100% bar, a segment per category, with a legend'),
      ('Mode (modal category)', 'the category that occurs most often: the tallest bar or longest segment')]
KF = [('Percentage frequency', r'$\dfrac{\text{number in the category}}{\text{total}} \times 100\%$'),
      ('Number from a percentage', r'$\text{number} = \dfrac{\text{percentage}}{100} \times \text{total}$'),
      ('Segmented bar', 'each segment ends at the previous end + its %'),
      ('Majority', 'only when the mode is more than 50%; otherwise ‘the most common’')]
S.append(f'<section class="slide z kif">{bar("1A–1B", "Key ideas")}<div class="cols" style="grid-template-columns:1.1fr .9fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1A pp. 2–4 and 1B pp. 7–10")}</section>')

# NL: types of variable (tree, top-down, one branch at a time)
def tb(t, sub, pos, c=''): return st(f'<b>{t}</b><i class="zsub">{sub}</i>', cls=f'ztb {c}" style="grid-area:{pos}')
TREE = ('<div class="ztree"><div class="ztb ztop" style="grid-area:1/1/2/5"><b>Variable</b></div>'
        + tb('Categorical', 'names a quality or group', '2/1/3/3', 'zcat') + tb('Nominal', 'names only · e.g. eye colour', '3/1/4/2', 'zcat') + tb('Ordinal', 'names <i>and</i> orders · e.g. fitness level', '3/2/4/3', 'zcat')
        + tb('Numerical', 'a quantity: counted or measured', '2/3/3/5', 'znum') + tb('Discrete', '‘How many?’ counted · e.g. cars', '3/3/4/4', 'znum') + tb('Continuous', '‘How much?’ measured · e.g. weight', '3/4/4/5', 'znum') + '</div>')
S.append(nl_slide('Types of variable',
    'Categorical data put people into groups. Numerical data are quantities you can do arithmetic with. <span class="hint">Click to build the tree.</span>',
    TREE + st('<b>Not sure? Two tests.</b> 1 · Does an average make sense? (average weight ✓ numerical; average house number ✗ categorical) &nbsp; 2 · How was it recorded? (weight in kg: numerical; ‘underweight’, ‘normal’, ‘overweight’: categorical)', True, cls='ztest'),
    CG + ', 1A pp. 2–4'))

def split2(h):
    # two working columns: everything from the part marked <span class="cbk"> goes in the right column
    i = h.index('<div class="zw">') + len('<div class="zw">'); j = h.rfind('<div class="zpq', 0, h.index('cbk')); e = h.index('</div></div><div class="foot"')
    return h[:i] + '<div class="zc2"><div>' + h[i:j] + '</div><div>' + h[j:e].replace(' sep"', '"', 1) + '</div></div>' + h[e:]
# Example 1
S.append(split2(qslide('ex', 1, 'Types of data', 'Cambridge · Example 1',
    'Classify the following data as nominal, ordinal, discrete or continuous.', KI_TYPES, [], None, CG + ', 1A Example 1 (p. 4)',
    parts=[('a', 'The number of chocolate chips in each of 10 cookies is counted.', [], '<b>Discrete</b>: the number of chips can only be a whole number.'),
           ('b', 'The time taken for 20 students to complete a puzzle is recorded in seconds.', [], '<b>Continuous</b>: time can take any value, limited only by how accurately it is measured.'),
           ('c', 'Member of a football club were asked to rate how they felt about the current coach, 1 = Very satisfied, 2 = Satisfied, 3 = Indifferent, 4 = Dissatisfied, 5 = Very dissatisfied.', [], '<b>Ordinal</b>: the numbers are not quantities; they rank how much each person approves of the coach.'),
           ('d', '<span class="cbk"></span>Students are asked to each choose their preferred colour from the list 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow.', [], '<b>Nominal</b>: the numbers are not quantities; they just name colours.'),
           ('e', 'Students weights were classified as ‘less than 60kg’, ‘60kg - 80kg’ or ‘more than 80kg’.', [], '<b>Ordinal</b>: weight was recorded in three groups that can be ordered.')], cls='tight ex1x')))
# You try 1: Edrolo 1A WE1-3
S.append(split2(qslide('yt', 1, 'Types of data', 'Edrolo 1A WE1, WE2, WE3',
    'Three short questions. Classify each variable.', KI_TYPES, [], None, ED + ', 1A Worked examples 1, 2 and 3 (pp. 2–4). Working by teacher.',
    parts=[('1', 'Classify the following variables as either categorical or numerical.<br><b>a.</b> <i>type of pasta</i> &nbsp; <b>b.</b> <i>number of candles</i>', ['a. grouped into pasta types · b. candles are counted'], '<b>a.</b> Categorical &nbsp; <b>b.</b> Numerical'),
           ('2', 'Classify the following categorical variables as either nominal or ordinal.<br><b>a.</b> <i>type of shoe</i> (runners, boots, sandals, slides) &nbsp; <b>b.</b> <i>shirt size</i> (small, medium, large)', ['a. no natural order · b. small → medium → large'], '<b>a.</b> Nominal &nbsp; <b>b.</b> Ordinal'),
           ('3', '<span class="cbk"></span>Classify the following numerical variables as either discrete or continuous.<br><b>a.</b> <i>length</i> (m) &nbsp; <b>b.</b> <i>number of tennis racquets</i>', ['a. measured · b. counted'], '<b>a.</b> Continuous &nbsp; <b>b.</b> Discrete')], cls='tight')))
# Sort it (interactive): the APK and You try items, verbatim
SORT = [('<i>type of pasta</i>', 'Nominal'), ('<i>number of candles</i>', 'Discrete'), ('<i>type of shoe</i> (runners, boots, sandals, slides)', 'Nominal'),
        ('<i>shirt size</i> (small, medium, large)', 'Ordinal'), ('<i>length</i> (m)', 'Continuous'), ('<i>number of tennis racquets</i>', 'Discrete'),
        ('The time between people arriving at the coffee shop.', 'Continuous'), ('The number of people in the queue at the coffee shop.', 'Discrete'),
        ('Customer’s coffee preference (latte, cappuccino, black).', 'Nominal'), ('Customer’s rating of the coffee (excellent, quite good, not that good).', 'Ordinal'),
        ('<i>frequency of nightmares</i> (low, high)', 'Ordinal'), ('<i>snores</i> (no, yes)', 'Nominal')]
CARDS = ''.join(f'<div class="card ix" data-a="{a}"><div class="ct">{t}</div><div class="cb">' + ''.join(f'<button data-v="{v}">{v}</button>' for v in ('Nominal', 'Ordinal', 'Discrete', 'Continuous')) + '</div></div>' for t, a in SORT)
S.append(f'<section class="slide z nl sort">{bar("New learning", "Sort it: what type of data?")}'
         '<p class="lead zlead">Every variable from today’s questions so far. Click the type for each card: green = right, red = try again. <span class="score ix">Correct: <b>0</b> / 12 <button class="reset">↺ Reset</button></span></p>'
         f'<div class="cards c12">{CARDS}</div>{foot("Items verbatim from Cambridge U1&amp;2 2A #1, " + ED + " 1A Worked examples 1–3 and VCAA 2020 Exam 1 Q10")}</section>')

# CAS: setting up the statistics app (planner/cas-skills.json: stats-list)
CS = [x for x in json.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if x['id'] == 'stats-list'][0]
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CS["ti"])}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CS["classpad"])}</ol></div></div>').replace('class="zcas2"','class="zcas2 zsm"')
SURV = table_hl('surv', [('Height (cm)', '173 179 167 195 173 184 175 140'.split()), ('Weight (kg)', '57 58 62 84 64 74 60 50'.split()), ('Age (years)', '18 19 18 18 18 22 19 34'.split()),
                         ('Study mode', 'C C C O C O O C'.split()), ('Fitness level', '2 2 1 1 3 3 3 3'.split()), ('Pulse rate (beats/min)', '86 82 96 71 90 78 88 70'.split())], 'ztab zsm2')
S.append(qslide('cas', '', 'Setting up the statistics app', 'Cambridge · 1A survey data',
    'A university survey of eight students (Study mode: C = on-campus, O = online; Fitness level: 1 = high, 2 = medium, 3 = low).' + SURV
    + 'Enter the <i>height</i> data into a list named <b>height</b>.',
    'Only <b>numerical</b> variables go into a list you calculate with.<div class="kn">Check: rows filled = number of data values.</div>',
    [('Name the list <i>height</i> (top cell).', 'tc:surv:0,1,2,3,4,5,6,7'), 'Enter the 8 heights down the list.', 'Check: 8 rows filled = 8 students.'],
    'The list <b>height</b> holds 8 values, ready for one-variable statistics (1D onwards).',
    CG + ', 1A p. 2 (survey data); the task is the teacher’s. CAS steps: planner CAS guide (stats-list).', fig=TABS, figw='1fr'))

# NL: raw data -> frequency table (study mode of 60 students)
STUDY = 'O O C O O O C O C C C O C O O O C C C O C O C O C C C O C O C O C O O O C O C O C O O O O O O C C O C O O O C O C C C O'.split()
SM = [('on-campus', 27, '45.0'), ('online', 33, '55.0')]
S.append(nl_slide('From raw data to a frequency table',
    'A <b>frequency table</b> lists each category and how often it occurs: as a number and as a percentage. Here: the <i>study mode</i> (C = on-campus, O = online) of 60 students. <span class="hint">Click to build the table.</span>',
    '<div class="cols" style="grid-template-columns:1.2fr 1fr"><div class="col">' + chips('sm', STUDY) + '</div><div class="col">' + freq_table('smt', '<i>study mode</i>', SM, (60, '100.0'), '%')
    + st('Count the C’s: <b>27</b> on-campus', do='hv:sm:C:hb tf:smt:n0', cls='stp') + st('Count the O’s: <b>33</b> online', do='hv:sm:O:hy tf:smt:n1', cls='stp')
    + st('Total: 27 + 33 = <b>60</b>', do='tf:smt:nT', cls='stp') + st(r'% on-campus $= \dfrac{27}{60} \times 100\% = 45.0\%$', do='tf:smt:p0', cls='stp')
    + st(r'% online $= \dfrac{33}{60} \times 100\% = 55.0\%$', do='tf:smt:p1', cls='stp') + st('Check: 45.0 + 55.0 = <b>100.0%</b>', do='tf:smt:pT', cls='stp') + '</div></div>',
    CG + ', 1B p. 7 (study mode of 60 students)', 'eng'))
# Example 2
ICE = 'C V V C C V C C C V V'.split()
S.append(qslide('ex', 2, 'Constructing a frequency table for a categorical variable', 'Cambridge · Example 2',
    'A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):' + chips('ice', ICE) + 'Construct a frequency table (including percentage frequencies) to display the data.',
    r'Percentage frequency $= \dfrac{\text{number}}{\text{total}} \times 100\%$',
    [('Count chocolate: 6', 'hv:ice:C:hb tf:ict:n0'), ('Count vanilla: 5', 'hv:ice:V:hy tf:ict:n1'), ('Total: 6 + 5 = 11', 'tf:ict:nT'),
     (r'% chocolate $= \dfrac{6}{11} \times 100\% = 54.5\%$', 'tf:ict:p0'), (r'% vanilla $= \dfrac{5}{11} \times 100\% = 45.5\%$', 'tf:ict:p1'), ('Check: 54.5 + 45.5 = 100.0', 'tf:ict:pT')],
    'The completed table (opposite).', CG + ', 1B Example 2 (p. 7)', cls='tight',
    fig=freq_table('ict', 'Flavour', [('chocolate', 6, '54.5'), ('vanilla', 5, '45.5')], (11, '100.0')), figw='1fr'))
# You try 2: Edrolo 1B WE1
TH = 'average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'.split()
S.append(qslide('yt', 2, 'Constructing a frequency table', 'Edrolo 1B WE1',
    'The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:<br>'
    + chips('th', TH) + 'Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.',
    r'Percentage frequency $= \dfrac{\text{number}}{\text{total}} \times 100\%$',
    [('short: 6 · average: 10 · tall: 8', 'hv:th:short:hy hv:th:average:hb hv:th:tall:hg tf:tht:n0,n1,n2'), ('Total: 6 + 10 + 8 = 24', 'tf:tht:nT'),
     (r'$\dfrac{6}{24} \times 100 = 25.0$, $\dfrac{10}{24} \times 100 = 41.7$, $\dfrac{8}{24} \times 100 = 33.3$', 'tf:tht:p0,p1,p2'), ('Check: 25.0 + 41.7 + 33.3 = 100.0', 'tf:tht:pT')],
    'The completed table (opposite).', ED + ', 1B Worked example 1 (pp. 9–10). Working by teacher.',
    fig=freq_table('tht', 'teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), '%'), figw='.8fr', cls='tight'))

# NL: frequency table -> bar chart
S.append(nl_slide('The bar chart: frequency table → graph',
    'One bar per category, gaps between the bars, height = frequency. <span class="hint">Click to draw it.</span>',
    '<div class="cols" style="grid-template-columns:.8fr 1.2fr"><div class="col">' + freq_table('bct', '<i>study mode</i>', SM, (60, '100.0'), '%', blank=False)
    + st('<b>1</b> Axes: <i>study mode</i> across, <i>Frequency</i> up (to 35).', do='ax:bc', cls='stp') + st('<b>2</b> on-campus: a bar 27 high.', do='hr:bct:0 bg:bc:0', cls='stp')
    + st('<b>3</b> online: a bar 33 high, with a gap.', do='hr:bct:1 bg:bc:1', cls='stp') + '</div><div class="col zc">'
    + bchart('bc', ['on-campus', 'online'], [27, 33], 35, 5, 'study mode', 'Frequency') + '</div></div>', CG + ', 1B pp. 7–8 (study mode of 60 students)'))
# Example 3
CLIMR = [('Cold', 3, '13.0'), ('Mild', 14, '60.9'), ('Hot', 6, '26.1')]
S.append(qslide('ex', 3, 'Constructing a bar chart from a frequency table', 'Cambridge · Example 3',
    'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.',
    'One bar per category, <b>gaps</b> between bars<div class="kn">label both axes</div>', [], None, CG + ', 1B Example 3 (p. 8)',
    parts=[('a', 'What is the level of measurement of the variable <i>climate type</i>?', ['cold, mild, hot can be put in a natural order of ‘warmth’.'], '<b>Ordinal</b>'),
           ('b', 'Construct a frequency bar chart to display this information.', [('Axes: <i>Climate type</i> across; <i>Frequency</i> up, scaled to 15.', 'ax:e3'),
             ('Cold 3, Mild 14, Hot 6: one bar each, with gaps.', 'hr:e3t:0,1,2 bg:e3:0,1,2')], 'The bar chart opposite.', 'ax:e3 bg:e3:0,1,2')],
    fig='<div class="zrowc">' + freq_table('e3t', 'Climate type', CLIMR, (23, '100.0'), blank=False) + bchart('e3', ['Cold', 'Mild', 'Hot'], [3, 14, 6], 15, 5, 'Climate type', 'Frequency', h=320) + '</div>', figw='1.6fr', cls='tight'))
# You try 3: Edrolo 1B WE2
THR = [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')]
S.append(qslide('yt', 3, 'Constructing a bar chart', 'Edrolo 1B WE2',
    '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.<br>Use the frequency table to construct a frequency bar chart.',
    'One bar per category, <b>gaps</b> between bars<div class="kn">label both axes</div>',
    [('Axes: <i>teacher’s height</i> across; <i>frequency</i> up to 10.', 'ax:y3'), ('short 6, average 10, tall 8: one bar each, with gaps.', 'hr:y3t:0,1,2 bg:y3:0,1,2')],
    'The bar chart opposite.', ED + ', 1B Worked example 2 (p. 11). Working by teacher.',
    fig='<div class="zrowc">' + freq_table('y3t', 'teacher’s height', THR, (24, '100.0'), '%', blank=False) + bchart('y3', ['short', 'average', 'tall'], [6, 10, 8], 10, 2, 'teacher’s height', 'frequency', h=320) + '</div>', figw='1.6fr', ans_do='ax:y3 bg:y3:0,1,2'))

# NL: segmented bar chart, modelled as a transformation (bars -> one stacked bar -> 100% bar)
S.append(nl_slide('From a bar chart to a percentage segmented bar chart',
    'Start with the bar chart. Stack the bars into <b>one bar</b>, then change to percentages so the bar is exactly 100% tall. <span class="hint">Click to transform.</span>',
    '<div class="cols zmo2" style="grid-template-columns:.85fr 1.15fr"><div class="col">' + freq_table('sgt', 'Climate type', CLIMR, (23, '100.0'), blank=False)
    + st('<b>1</b> Stack into one bar: Cold at the bottom, then Mild, then Hot. Total 3 + 14 + 6 = 23.', do='mo:sgm:1', cls='stp')
    + st('<b>2</b> Axis to percentage: 23 becomes 100%. Cold 13.0%, Mild 60.9%, Hot 26.1%.', do='mo:sgm:2', cls='stp')
    + st('<b>3</b> Segments end at 13.0, 13.0 + 60.9 = 73.9 and 100. Add a legend.', do='mo:sgm:3', cls='stp')
    + st('<b>4</b> The longest segment is the mode: Mild.', do='mo:sgm:3 hr:sgt:1', cls='stp') + '</div><div class="col zc">'
    + morph_svg('sgm', ['Cold', 'Mild', 'Hot'], [3, 14, 6], 24, 4, 'Climate type') + '</div></div>', CG + ', 1B pp. 8–9 (climate data, Example 3)'))
# Example 4
S.append(qslide('ex', 4, 'Constructing a percentage segmented bar chart', 'Cambridge · Example 4',
    'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’.<br>Construct a percentage frequency segmented bar chart to display this information.',
    'Each segment ends at the <b>previous end + its %</b><div class="kn">the bar is 100% tall; add a legend</div>',
    [('Axes: vertical axis <i>Percentage</i>, 0 to 100 in tens.', 'ax:e4'), ('Cold: from 0 to 13.0%', 'hr:e4t:0 bg:e4:0'), ('Mild: from 13.0 to 13.0 + 60.9 = 73.9%', 'hr:e4t:1 bg:e4:1'),
     ('Hot: from 73.9 to 100%; add the legend', 'hr:e4t:2 bg:e4:2 lg:e4')],
    'The percentage segmented bar chart opposite.', CG + ', 1B Example 4 (p. 9)',
    fig='<div class="zrowc">' + freq_table('e4t', 'Climate type', CLIMR, (23, '100.0'), blank=False) + schart('e4', [('', [13.0, 60.9, 26.1])], ['Cold', 'Mild', 'Hot'], 100, 10, 'Percentage', w=330, h=340) + '</div>', figw='1.6fr'))
# You try 4: Edrolo 1B WE3, three columns: question + table | part a + chart a | part b + chart b
_n4 = ['short', 'average', 'tall']
_y4a = [W('Axes: <i>frequency</i> 0 to 24.', 'ax:y4a'), W('short: 0 to 6', 'ax:y4a bg:y4a:0'), W('average: 6 to 6 + 10 = 16', 'ax:y4a bg:y4a:0,1'),
        W('tall: 16 to 16 + 8 = 24', 'ax:y4a bg:y4a:0,1,2'), W('Add the legend.', 'ax:y4a bg:y4a:0,1,2 lg:y4a')]
_y4b = [W('Axes: <i>percentage</i> 0 to 100.', 'ax:y4b'), W('short: 0 to 25%', 'ax:y4b bg:y4b:0'), W('average: 25 to 25 + 41.7 = 66.7%', 'ax:y4b bg:y4b:0,1'),
        W('tall: 66.7 to 66.7 + 33.3 = 100%', 'ax:y4b bg:y4b:0,1,2'), W('Add the legend.', 'ax:y4b bg:y4b:0,1,2 lg:y4b')]
S.append('<section class="slide z ex yt k-yt yt4">'
    + '<div class="bar ytb"><span class="tag">You try 4</span><h1>Constructing segmented bar charts</h1><span class="sub zpill">Edrolo 1B WE3</span></div>'
    + '<div class="zb" style="grid-template-columns:.9fr 1fr 1fr">'
    + '<div class="zw y4q"><div class="q">24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.</div>'
    + freq_table('y4t', 'teacher’s height', THR, (24, '100.0'), '%', blank=False)
    + ki('Key idea', 'Each segment ends at the <b>previous end + its value</b><div class="kn">add a legend</div>') + '</div>'
    + '<div class="zw y4p"><div class="zpq"><b>a</b> Use the frequency table to construct a segmented bar chart.</div>' + ''.join(_y4a)
    + st('<span class="zok">✓ Answer</span> Segmented bar chart: short 0–6, average 6–16, tall 16–24, with a legend', True, do='ax:y4a bg:y4a:0,1,2 lg:y4a', cls='zpa')
    + schart_big('y4a', [6, 10, 8], _n4, 24, 4, 'frequency', ['6', '16', '24']) + '</div>'
    + '<div class="zw y4p"><div class="zpq"><b>b</b> Use the frequency table to construct a percentage segmented bar chart.</div>' + ''.join(_y4b)
    + st('<span class="zok">✓ Answer</span> Percentage segmented bar chart: short 0–25%, average 25–66.7%, tall 66.7–100%, with a legend', True, do='ax:y4b bg:y4b:0,1,2 lg:y4b', cls='zpa')
    + schart_big('y4b', [25, 41.7, 33.3], _n4, 100, 20, 'percentage (%)', ['25%', '66.7%', '100%']) + '</div>'
    + '</div>' + foot(ED + ', 1B Worked example 3 (pp. 12–13). Working by teacher.') + '</section>')

# NL: describing the distribution
SREP = report('srep', ['The ', ('a0', '<i>study mode</i>'), ' of ', ('a1', '60'), ' students were classified as being ', ('a2', '‘on-campus’ or ‘online’'), '. The ', ('b0', 'majority'),
                       ' of the students, ', ('b1', '55.0%'), ', were found to ', ('b2', 'study online'), '. Of the remaining students, ', ('c0', '45.0%'), ' were found to ', ('c1', 'study on-campus'), '.'])
S.append(nl_slide('Describing the distribution of a categorical variable',
    'A report gives <b>1</b> the context and how many, <b>2</b> the modal category with its %, <b>3</b> the percentages for the others. <span class="hint">Click to fill the report.</span>',
    '<div class="cols" style="grid-template-columns:.75fr 1.25fr"><div class="col">' + freq_table('drt', '<i>study mode</i>', SM, (60, '100.0'), '%', blank=False)
    + '<p class="zsc" style="font-size:19px">‘Majority’ only when the mode is more than 50%; otherwise ‘the most common’.</p></div><div class="col">' + SREP
    + st('<b>1</b> Context: 60 students, on-campus or online.', do='tf:srep:a0,a1,a2 hr:drt:2', cls='stp') + st('<b>2</b> Mode: online, 55.0%: more than 50%, so ‘the majority’.', do='tf:srep:b0,b1,b2 hr:drt:1', cls='stp')
    + st('<b>3</b> The others: on-campus 45.0%.', do='tf:srep:c0,c1 hr:drt:0', cls='stp') + '</div></div>', CG + ', 1B pp. 9–10 (report guidelines; study mode data p. 7)'))
# Example 5
WREP = report('e5r', ['The ', ('a0', 'climate types'), ' of ', ('a1', '23'), ' countries were classified as being ', ('a2', '‘cold’, ‘mild’ or ‘hot’'), '. The ', ('b0', 'majority'), ' of the countries, ', ('b1', '60.9%'),
                      ', were found to ', ('b2', 'have a mild climate'), '. Of the remaining countries, ', ('c0', '26.1%'), ' were found to ', ('c1', 'have a hot climate'), ', while ', ('c2', '13.0%'), ' were found to ', ('c3', 'have a cold climate'), '.'])
S.append(qslide('ex', 5, 'Describing the distribution of a categorical variable', 'Cambridge · Example 5',
    'In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages.<br>Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.',
    'Context → mode with its % → the others<div class="kn">‘majority’ only if the mode is over 50%</div>',
    [('Context: 23 countries; cold, mild or hot.', 'hr:e5t:3 tf:e5r:a0,a1,a2'), ('Mode: Mild, 60.9%: more than 50%, so ‘the majority’.', 'hr:e5t:1 tf:e5r:b0,b1,b2'),
     ('The others: hot 26.1%, cold 13.0%.', 'hr:e5t:0,2 tf:e5r:c0,c1,c2,c3')],
    'The report opposite.', CG + ', 1B Example 5 (pp. 10–11, report verbatim)',
    fig=freq_table('e5t', 'Climate type', CLIMR, (23, '100.0'), '%', blank=False) + WREP, figw='1.1fr'))
# You try 5: Edrolo 1B WE4
YREP = report('y5r', [('a0', '24'), ' ', ('a1', 'prep students'), ' were surveyed on ', ('a2', 'how tall they thought their teacher was'), '. The ', ('b0', 'most common'), ' response was ', ('b1', 'average'),
                      ', accounting for ', ('b2', '41.7%'), ' of responses, while ', ('c0', '25%'), ' said their teacher was ', ('c1', 'short'), ', and ', ('c2', '33.3%'), ' said their teacher was ', ('c3', 'tall'), '.'])
S.append(qslide('yt', 5, 'Describing the distribution', 'Edrolo 1B WE4',
    '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.',
    'The mode is the <b>longest segment</b><div class="kn">‘most common’ when it is under 50%</div>', [], None, ED + ', 1B Worked example 4 (p. 14). Working by teacher.',
    parts=[('a', 'Find the modal category of the data set.', ['Longest segment: average, 41.7% (short 25%, tall 33.3%).'], '<b>Average</b>'),
           ('b', 'Describe the distribution of the data set.', [('Context, then mode: average 41.7% is under 50%, so ‘the most common’.', 'tf:y5r:a0,a1,a2,b0,b1,b2'), ('The others: short 25%, tall 33.3%.', 'tf:y5r:c0,c1,c2,c3')],
            'The report under the chart.', 'tf:y5r:a0,a1,a2,b0,b1,b2,c0,c1,c2,c3')],
    fig=schart('y5s', [('', [25, 41.7, 33.3])], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', 'teacher’s height', full=True, w=340, h=280) + YREP, figw='1.1fr', cls='tight'))

# Exits
TMP = [12.7, 11.8, 10.7, 9.0, 6.0, 7.0, 4.1, 4.8, 9.2, 6.7, 7.5, 8.0, 8.6, 9.8, 7.7]
TT1 = (table_hl('x1a', [('<i>day number</i>', [str(d) for d in range(1, 9)]), ('<i>minimum temperature</i> (°C)', [str(t) for t in TMP[:8]])], 'ztab zsm2')
       + table_hl('x1b', [('<i>day number</i>', [str(d) for d in range(9, 16)]), ('<i>minimum temperature</i> (°C)', [str(t) for t in TMP[8:]])], 'ztab zsm2'))
S.append(qslide('exit', '1 of 3', 'Show what you know', 'VCAA 2019 Exam 2 Q1a',
    'The table shows the <i>day number</i> and the <i>minimum temperature</i>, in degrees Celsius, for 15 consecutive days in May 2017.' + TT1
    + 'Which of the two variables in this data set is an ordinal variable?', KI_TYPES,
    ['<i>minimum temperature</i> is measured in °C: numerical.', '<i>day number</i> labels each day and puts the days in order; you wouldn’t average it: categorical, ordinal.'],
    '<i>day number</i> is the ordinal variable.', ED + ', 1A Q14 (VCAA 2019 Exam 2 Data analysis Q1a); % from the examiner report.',
    marks=1, vcaa=83, figw='1.2fr', watch='a variable written as numbers is not automatically numerical. Ask what the numbers do: <i>day number</i> only puts the days in order. <span class="zsc">(teacher note)</span>'))
HEP = [(1, 1.76, 15.34, 41.22), (2, 1.79, 16.96, 42.41), (3, 1.83, 13.87, 46.53), (4, 1.82, 14.23, 40.53), (5, 1.87, 13.78, 40.62), (6, 1.73, 14.50, 45.62), (7, 1.68, 15.08, 42.33), (8, 1.82, 13.13, 40.88),
       (9, 1.83, 14.22, 39.22), (10, 1.87, 13.62, 42.51), (11, 1.87, 12.01, 42.75), (12, 1.80, 12.88, 38.12), (13, 1.83, 12.68, 42.65), (14, 1.87, 12.45, 41.32), (15, 1.78, 11.31, 42.88)]
HT = lambda rows: ('<table class="ztab zhep"><tr><th><i>athlete number</i></th><th><i>high jump</i> (metres)</th><th><i>shot-put</i> (metres)</th><th><i>javelin</i> (metres)</th></tr>'
                   + ''.join(f'<tr><td>{a}</td><td>{b:.2f}</td><td>{c:.2f}</td><td>{d:.2f}</td></tr>' for a, b, c, d in rows) + '</table>')
S.append(qslide('exit', '2 of 3', 'Show what you know', 'VCAA 2021 Exam 2 Q1a',
    'In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.'
    + f'<div class="zrowc">{HT(HEP[:8])}{HT(HEP[8:])}</div>Write down the number of numerical variables in the table.', KI_TYPES,
    ['<i>high jump</i>, <i>shot-put</i> and <i>javelin</i> are measured in metres: numerical.', '<i>athlete number</i> only names each athlete: categorical.'],
    '<b>3</b> numerical variables', ED + ', 1A Q16 (VCAA 2021 Exam 2 Data analysis Q1a); % and common error from the examiner report.',
    marks=1, vcaa=52, figw='1.35fr', watch='count the <b>variables</b> (columns), not the values. The examiners noted a common error was counting the 45 values.'))
OPTDIST['3 of 3'] = [21, 76, 2, 1, 1]
S.append(qslide('exit', '3 of 3', 'Show what you know', 'VCAA 2017 Exam 1 Q5 (adapted)',
    'A study was conducted that investigated the <i>number of moths</i> caught in a sugar moth trap (less than 250, 250–500, more than 500). The results are summarised in the percentage segmented bar chart shown.<br>There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to',
    r'$\text{number} = \dfrac{\text{percentage}}{100} \times \text{total}$',
    ['Read: the ‘less than 250’ segment runs from 0 to 30%.', r'$\dfrac{30}{100} \times 300 = 90$'],
    '90', ED + ', 1B Q13 · Adapted from VCAA 2017 Exam 1 Data analysis Q5; % from the examiner report for the original question.',
    fig=schart('x3', [('', [30, 46, 24])], ['less than 250', '250–500', 'more than 500'], 100, 10, 'frequency (%)', 'number of moths', full=True, w=400, h=260),
    figw='1.15fr', marks=1, vcaa=76, opts=[('A', '30'), ('B', '90'), ('C', '250'), ('D', '300'), ('E', '500')], key='B'))

checkin(SC, "Success criteria: one per worked example")
coursework('1A–1B', 'Coursework · Exercises 1A and 1B', [('Cambridge Exercise 1A', 'Q1–6'), ('Cambridge Exercise 1B', 'Q1–9'), ('Practice booklet', '1A and 1B sections')],
           'Exercise 1A: Types of data', CG + ", Exercises 1A and 1B; Chapter 1 practice booklet", fit=False)



# ---- lesson-only CSS / JS (everything shared lives in lib/)
LESSON_CSS = r'''
#sm .zc{min-width:30px;text-align:center;font-size:20px}
.ztree{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 18px;margin:16px 0}
.ztree .ztb,.ztree .st.ztb{border:3px solid #000;padding:8px 10px;text-align:center;font-size:22px!important;color:#000!important;box-shadow:4px 4px 0 #bbb;margin:0!important;white-space:normal}
.ztree .ztop{width:300px;justify-self:center}.ztree .zcat{border-color:#1f9e74!important}.ztree .znum{border-color:#2f6fdf!important}
.ztree i.zsub{display:block;font-style:normal;font-size:16px;color:#444}
.slide.z .st.ztest{font-size:20px!important;color:#000}
.slide.ex1x .zpq{font-size:17px;margin-bottom:5px}.slide.ex1x .st.zs{font-size:18px!important}.slide.ex1x .zb>div{padding-top:10px}
.ztab.zhep{font-size:13px}.ztab.zhep td,.ztab.zhep th{padding:1px 5px}
.slide.sort .score{float:right;font-weight:bold}.slide.sort .cards{margin-top:10px}.slide.sort .card{font-size:16px}.slide.sort .card .cb{flex-wrap:wrap;gap:4px}.slide.sort .card button{font-size:13px;padding:3px 6px}
.slide.yt4 .zb{flex:1;min-height:0}
.slide.yt4 .zw{padding:10px 14px!important;overflow:hidden;border-right:1.5px solid #000}.slide.yt4 .zw:last-child{border-right:none}
.slide.yt4 .y4q .q{font-size:19px;line-height:1.35;margin-bottom:8px}.slide.yt4 .y4q .ztab.zft{font-size:19px;margin:6px 0 10px}.slide.yt4 .y4q .ki{font-size:17px;width:auto!important;max-width:100%!important;box-sizing:border-box}
.slide.yt4 .y4p .st.zs{font-size:18px;margin:2px 0!important;line-height:1.3}.slide.yt4 .zpq{font-size:18px;margin-bottom:4px}
.slide.yt4 .y4p .st.zpa{font-size:16px;margin-top:4px!important}
.slide.yt4 svg.zch.zbig{flex:1 1 0;min-height:0;width:100%;max-height:none!important;margin-top:4px}
'''

build('S1-slides.html', '12MAG S1 · Types of data and categorical data · Slides', css=LESSON_CSS)
