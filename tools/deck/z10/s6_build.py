r"""12MAG S6 (2A Bivariate data, 2B Associations between two categorical variables) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l03/build.py (planner card gm12-u3-l03; same items, same order).
python3 tools/deck/z10/s6_build.py  ->  lessons/S6-slides.html
Sources (verbatim; read from the PDFs on G: 15 Nov 2026):
- APK: Cambridge U1&2 Chapter 2 skills checklist 2A #2 (canteen ratings) · Chapter 1 checklist 1A #2 (0.67 as a %)
- New learning: Cambridge U3&4 2A pp. 104-106, 2B pp. 108-117 (gun control, smoking tables; report wording)
- Examples: Cambridge U3&4 Examples 1-8 (pp. 105-117)
- You try: Edrolo U1&2 1A WE1 (p. 2) · Edrolo U3&4 2C WE1, WE2 (p. 132) · 2A WE1 (pp. 106-107), WE4 (p. 110), WE2 (pp. 107-108), WE3 (p. 109), WE5 (pp. 110-111)
- Exits: Edrolo U3&4 2A Q11 = VCAA 2018 Exam 2 (Further) Core Q1d (report: average 1.9/2 = 94%)
         Edrolo U3&4 2A Q13 = VCAA 2021 Exam 1 (Further) Core Q3 (report: A 50%, B 13, C 28, D 1, E 8)
Do Now and videos are not slides (z10 rule: Rocco attaches them to Google Classroom).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.cat import *
from lib.assoc import *
lesson('2A Bivariate data · 2B Two categorical variables')

title_slide('Investigating associations between two categorical variables',
            ['2A Bivariate data – Classifying the variables (pp. 104–107)', '2B Investigating associations between categorical variables (pp. 108–119)'])
LI = ['To introduce bivariate data.', 'To be able to classify data as categorical or numerical.', 'To be able to identify explanatory and response variables.',
      'To be able to summarise data from two categorical variables using two-way frequency tables.', 'To be able to appropriately percentage two-way frequency tables.',
      'To be able to use a percentaged two-way frequency table to identify and describe an association between two categorical variables.']
SC = ['I can identify categorical and numerical variables in bivariate data.', 'I can identify explanatory and response variables.', 'I can construct a two-way frequency table.',
      'I can percentage a two-way frequency table.', 'I can describe an association from a percentaged two-way frequency table.',
      'I can construct a segmented bar chart from a percentaged two-way frequency table.', 'I can describe an association from a percentaged segmented bar chart.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Bivariate data · Example 1', 'Explanatory and response variables · Examples 2, 3',
       'Two-way frequency tables · Example 4', 'Percentaged tables and associations · Examples 5, 6', 'Segmented bar charts · Examples 7, 8', 'Exit tasks', 'Check-in and coursework']
overview('2A–2B', LI, SC, SEQ, CG + ', 2A and 2B Learning intentions; success criteria: one per worked example', cols='1.1fr 1fr .9fr')

# ---- APK 1: Cambridge U1&2 2A #2
CN = 'bad, bad, ok, ok, good, bad, good, ok, ok, ok, bad, ok, bad, good, good, good, good, bad, ok, ok'.split(', ')
S.append(qslide('apk', '1 of 2', 'What do you remember?', 'Cambridge U1&amp;2 · 2A #2',
    'Twenty students rated their school canteen as bad, ok or good, giving the following data:' + chips('cn', CN) + 'Construct a percentage frequency table.',
    r'Percentage frequency $= \dfrac{\text{count}}{\text{total}} \times 100\%$',
    [('Count bad: 6', 'hv:cn:bad:hy tf:cnt:n0'), ('Count ok: 8', 'hv:cn:ok:hb tf:cnt:n1'), ('Count good: 6', 'hv:cn:good:hg tf:cnt:n2'), ('Total: 20', 'tf:cnt:nT'),
     (r'bad: $\dfrac{6}{20} \times 100\% = 30\%$; ok: 40%; good: 30%', 'tf:cnt:p0,p1,p2,pT')],
    'The completed table (opposite).', CG12 + ', Chapter 2 skills checklist 2A #2. Working by teacher.',
    fig=freq_table('cnt', 'Rating', [('bad', 6, '30'), ('ok', 8, '40'), ('good', 6, '30')], (20, '100'), '%'), figw='.8fr'))
# ---- APK 2: Cambridge U1&2 1A #2
S.append(qslide('apk', '2 of 2', 'Decimals to percentages', 'Cambridge U1&amp;2 · 1A #2',
    'What is 0.67 as a percentage?', 'To change a decimal to a percentage, multiply by 100.', ['0.67 × 100 = 67'], '0.67 = <b>67%</b>',
    CG12 + ', Chapter 1 skills checklist 1A #2. Working by teacher.'))

# ---- Key ideas
keyslide('2A–2B',
    [('Bivariate data', 'two variables recorded for each individual (subject)'),
     ('Explanatory variable (EV)', 'the variable we expect to explain or predict the other one'),
     ('Response variable (RV)', 'the variable whose value we explain or predict'),
     ('Two-way frequency table', 'counts for two categorical variables: EV labels the columns, RV labels the rows'),
     ('Association', 'the percentages differ across the EV categories: knowing the EV helps predict the RV'),
     ('Segmented bar chart', 'one 100% bar per EV category, split into segments for the RV')],
    [('Column percentage', r'$\dfrac{\text{cell frequency}}{\text{column total}} \times 100\%$'),
     ('Placing the variables', 'EV → columns (horizontal axis) · RV → rows (segments)'),
     ('Check', 'each column of a percentaged table adds to 100%')],
    CG + ', 2A pp. 105–106, 2B pp. 109–116')

# ---- NL: bivariate data
S.append(nl_slide('Bivariate data: what kind of association?',
    'Two variables are recorded for each person or thing, so we can ask whether they <b>vary together</b> (are associated). First step: classify each variable as categorical or numerical. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr 1fr">'
    + st('<b>Categorical + numerical</b><br>Does the new headache treatment work more quickly than the old one?<br><i class="zsub">type of treatment (new, old) · time taken (minutes)</i>', cls='stp zcard')
    + st('<b>Two categorical</b><br>Are city voters more likely to vote Greens than country voters?<br><i class="zsub">place of residence (city, country) · vote for the Greens (yes, no)</i>', cls='stp zcard')
    + st('<b>Two numerical</b><br>Can we predict a test score (%) from hours spent studying?<br><i class="zsub">test score · time spent studying</i>', cls='stp zcard') + '</div>'
    + st('A variable with number codes (1 = light, 2 = moderate …) or a postcode is still categorical: the numbers are labels.', cls='stp ztest'),
    CG + ', 2A pp. 104–105'))
KI_BIV = 'Counted or measured → <b>numerical</b><div class="kn">sorted into groups (even with number codes) → <b>categorical</b></div>'
S.append(qslide('ex', 1, 'Identifying associations as categorical or numerical', 'Cambridge · Example 1',
    'For each of the following questions, determine if they involve investigating associations between<br>■ one numerical variable and one categorical variable or<br>■ two categorical variables or<br>■ two numerical variables.',
    KI_BIV, [], None, CG + ', 2A Example 1 (p. 105)',
    parts=[('a', 'Are younger people (age measured in years) more likely to believe in astrology (measured as ‘yes’ or ‘no’) than older people?',
            [], '<i>age</i> numerical, <i>belief in astrology</i> categorical: <b>one numerical variable and one categorical variable</b>'),
           ('b', 'Do people who weigh more (weight measured in kg) tend to have higher blood pressure (blood pressure measured in mmHg)?',
            [], 'both measured: <b>two numerical variables</b>'),
           ('c', 'Are people who have a driver’s licence (measured as ‘yes’ or ‘no’) more likely to be in favour of lowering the driving age (measured as ‘yes’ or ‘no’)?',
            [], 'both yes/no: <b>two categorical variables</b>')], cls='tight'))
S.append(qslide('yt', 1, 'Categorical or numerical?', 'Edrolo U1&amp;2 1A WE1',
    'Is the variable <i>hair colour</i> an example of categorical or numerical data?', KI_BIV,
    ['<i>hair colour</i> can’t be counted or measured; it is sorted into groups (brown, black, red …).'], '<i>hair colour</i> is <b>categorical</b>.',
    ED12 + ', 1A Worked example 1 (p. 2). Working by teacher.'))

# ---- NL: EV and RV
S.append(nl_slide('Explanatory and response variables',
    'The <b>explanatory variable (EV)</b> is the one we expect to explain or predict the value of the <b>response variable (RV)</b>. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr">'
    + st('<b>‘Are city voters more likely to vote Greens than country voters?’</b><br>Knowing where someone lives might help explain how they vote, not the other way round.<br><br><b>EV:</b> <i>place of residence</i><br><b>RV:</b> <i>vote for the Greens</i>', cls='stp zcard')
    + st('<b>Read the question</b><br>‘Can we predict <b>RV</b> from <b>EV</b>?’ · ‘Does <b>RV</b> depend on <b>EV</b>?’<br><br>If there is no obvious EV, the way the question is asked decides.<br><i class="zsub">Also called the independent (IV) and dependent (DV) variables.</i>', cls='stp zcard') + '</div>'
    + st('On a graph or table the EV goes on the horizontal axis / across the columns.', cls='stp ztest'),
    CG + ', 2A pp. 105–106'))
KI_EV = '‘Does <b>RV</b> depend on <b>EV</b>?’ · ‘Predict <b>RV</b> from <b>EV</b>’<div class="kn">the EV explains; the RV responds</div>'
S.append(qslide('ex', 2, 'Identifying the response and explanatory variables', 'Cambridge · Example 2',
    'We wish to investigate the question, ‘Does the time it takes a student to get to school depend on their mode of transport?’ The variables here are <i>time</i> and <i>mode of transport</i>. Which is the response variable (RV) and which is the explanatory variable (EV)?',
    KI_EV, ['Read the question: ‘does the <i>time</i> … depend on their <i>mode of transport</i>?’', 'A student’s mode of transport might explain the differences in the time it takes to get to school.'],
    'EV: <i>mode of transport</i> &nbsp; RV: <i>time</i>', CG + ', 2A Example 2 (p. 106)'))
S.append(qslide('yt', 2, 'Identifying the response and explanatory variables', 'Edrolo 2C WE1',
    'The following question was posed: ‘Can the <i>number of ice creams sold</i> be predicted from the <i>temperature</i>?’<br>Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.',
    KI_EV, ['The number of ice creams sold is being predicted from changes in temperature.'], 'RV: <i>number of ice creams sold</i> &nbsp; EV: <i>temperature</i>',
    ED + ', 2C Worked example 1 (p. 132). Working by teacher.'))
S.append(qslide('ex', 3, 'Identifying the response and explanatory variables', 'Cambridge · Example 3',
    'Can we predict people’s height (in cm) from their wrist measurement? The variables in this investigation are <i>height</i> and <i>wrist measurement</i>. Which is the response variable (RV) and which is the explanatory variable (EV)?',
    KI_EV, ['Read the question: ‘predict … <i>height</i> from their <i>wrist measurement</i>’', 'We use wrist measurement as the predictor (explanatory) variable; height is then the response.'],
    'EV: <i>wrist measurement</i> &nbsp; RV: <i>height</i>', CG + ', 2A Example 3 (p. 106)'))
SP = [(0, 98), (1, 90), (2, 110), (3, 122), (4, 125), (5, 130), (6, 137), (7, 145), (8, 166), (9, 192), (10, 188)]
S.append(qslide('yt', 3, 'Identifying the response and explanatory variables', 'Edrolo 2C WE2',
    'A study was conducted on the association between <i>daily sugar intake</i> and the <i>number of soft drinks consumed per week</i>. The following scatterplot displays the data that was collected.<br>Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.',
    'On a scatterplot: <b>EV</b> on the horizontal axis, <b>RV</b> on the vertical axis', ['Read the axes: horizontal = EV, vertical = RV.'],
    'RV: <i>daily sugar intake</i> &nbsp; EV: <i>number of soft drinks consumed per week</i>', ED + ', 2C Worked example 2 (p. 132; scatterplot redrawn). Working by teacher.',
    fig=scat('y3s', SP, (0, 10, 2), (0, 200, 50), 'number of soft drinks consumed per week', 'daily sugar intake (g)', w=500, h=340), figw='1fr'))

# ---- NL: two-way frequency table
GT = twoway('gt', 'Attitude to gun control', 'Residence', ['Country', 'City'], [('For', [('a', '32'), ('b', '30')]), ('Against', [('c', '26'), ('d', '12')])],
            total=[('g', '58'), ('h', '42'), ('i', '100')], totcol=[('e', '62'), ('f', '38')])
S.append(nl_slide('Constructing a two-way frequency table',
    '100 people were asked where they live and their attitude to gun control. <span class="hint">Click to build the table.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1.1fr"><div class="col">'
    + '<ul class="zul"><li>32 country people are for gun control</li><li>30 city people are for gun control</li><li>26 country people are against gun control</li><li>12 city people are against gun control</li></ul>'
    + st('<b>1</b> EV: <i>residence</i> → labels the <b>columns</b>. RV: <i>attitude to gun control</i> → labels the <b>rows</b>.', cls='stp')
    + st('<b>2</b> The four counts go in the <b>cells</b>.', do='tf:gt:a,b,c,d', cls='stp')
    + st('<b>3</b> Row sums: 62 for, 38 against.', do='tf:gt:e,f', cls='stp')
    + st('<b>4</b> Column sums: 58 country, 42 city. Check: 62 + 38 = 58 + 42 = 100.', do='tf:gt:g,h,i', cls='stp')
    + '</div><div class="col zc">' + GT + '</div></div>', CG + ', 2B pp. 109–110'))
ST = [('Female', 'Yes'), ('Male', 'Yes'), ('Female', 'No'), ('Female', 'Yes'), ('Male', 'No'), ('Male', 'Yes'), ('Female', 'Yes'), ('Male', 'No'), ('Female', 'No'), ('Female', 'Yes')]
STT = lambda rng: '<table class="ztab zsm2"><tr><th>Student</th><th><i>Gender</i></th><th><i>University</i></th></tr>' + ''.join(f'<tr><td>{i+1}</td><td>{ST[i][0]}</td><td>{ST[i][1]}</td></tr>' for i in rng) + '</table>'
W4 = twoway('w4', 'University', 'Gender', ['Male', 'Female'], [('Yes', [('a', '2'), ('b', '4')]), ('No', [('c', '2'), ('d', '2')])],
            total=[('g', '4'), ('h', '6'), ('i', '10')], totcol=[('e', '6'), ('f', '4')])
S.append(qslide('ex', 4, 'Constructing a two-way frequency table', 'Cambridge · Example 4',
    'The following data were obtained when a sample of ten Year 9 students were asked if they intended to go to university (<i>university</i>). The gender of the student was also recorded.'
    + f'<div class="zrowc">{STT(range(5))}{STT(range(5, 10))}</div>Create a two-way frequency table from these data.',
    'EV labels the <b>columns</b>, RV the <b>rows</b><div class="kn">row and column sums both add to the sample size</div>',
    ['Intention to go to university may depend on gender: <i>gender</i> = EV (columns), <i>university</i> = RV (rows).',
     ('Males: Yes 2 · No 2', 'tf:w4:a,c'), ('Females: Yes 4 · No 2', 'tf:w4:b,d'), ('Sums: rows 6, 4 · columns 4, 6 · total 10 = the number of students', 'tf:w4:e,f,g,h,i')],
    'The two-way table opposite.', CG + ', 2B Example 4 (pp. 110–111)', fig=W4, figw='.85fr', cls='tight'))
Y1 = twoway('y1', 'opinion', 'studying status', ['studying', '%', 'not studying', '%'],
            [('for', ['20', ('a', '55.56%'), '5', ('c', '25.00%')]), ('against', ['16', ('b', '44.44%'), '15', ('d', '75.00%')])], total=['36', '100%', '20', '100%'])
S.append(qslide('yt', 4, 'Completing a percentaged two-way table', 'Edrolo 2A WE1',
    'A group of people were surveyed on their opinion towards offering a student discount for public transport. Their <i>studying status</i> was recorded as ‘studying’ or ‘not studying’ along with their <i>opinion</i> ‘for’ or ‘against’ the student discount.<br>Complete the percentage frequency table by filling out the missing columns with the percentage frequency of each category, rounded to two decimal places.',
    r'Column % $= \dfrac{\text{cell}}{\text{column total}} \times 100$<div class="kn">each column adds to 100%</div>',
    [(r'studying, for: $\dfrac{20}{36} \times 100 = 55.56\%$', 'tc:y1:0,900 tf:y1:a'), ('studying, against: 16/36 × 100 = 44.44%', 'tc:y1:100,900 tf:y1:b'),
     ('not studying: 5/20 × 100 = 25.00% · 15/20 × 100 = 75.00%', 'tc:y1:2,102,902 tf:y1:c,d')],
    'The completed table (opposite).', ED + ', 2A Worked example 1 (pp. 106–107). Working by teacher.', fig=Y1, figw='.9fr', cls='tight'))

# ---- NL: percentaged tables and associations
PT = twoway('pt', 'Attitude to gun control', 'Residence', ['Country', 'City'], [('For', [('a', '55.2%'), ('b', '71.4%')]), ('Against', [('c', '44.8%'), ('d', '28.6%')])], total=['100.0%', '100.0%'])
LREP = report('lrep', ['In this sample of 100 people, a higher percentage of ', ('r1', 'city people'), ' were for gun control than ', ('r2', 'country people'), ': ', ('r3', '71.4%'), ' to ', ('r4', '55.2%'), '. '
                       'This indicates that a person’s ', ('r5', 'attitude to gun control'), ' ', ('r6', 'is'), ' associated with their ', ('r7', 'place of residence'), '.'])
S.append(nl_slide('Percentaged two-way tables: is there an association?',
    'More country people (32) than city people (30) are for gun control, but there are more country people in the sample. Compare <b>percentages</b> within each EV category. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:.9fr 1.1fr"><div class="col">' + PT
    + st('<b>1</b> Country column: 32/58 = 55.2% for, 44.8% against.', do='tf:pt:a,c', cls='stp') + st('<b>2</b> City column: 30/42 = 71.4% for, 28.6% against.', do='tf:pt:b,d', cls='stp')
    + st('<b>Associated</b> if the % in one row differ clearly across the columns. <b>Not associated</b> if they are about the same (Year 10 vs Year 12 ban phones: 87.9% vs 86.8%).', cls='stp')
    + '</div><div class="col">' + LREP + st('<b>3</b> Report: the context and the two % compared, from one row.', do='hr:pt:0 tf:lrep:r1,r2,r3,r4', cls='stp')
    + st('<b>4</b> The conclusion: associated or not.', do='tf:lrep:r5,r6,r7', cls='stp') + '</div></div>',
    CG + ', 2B pp. 112–113 (column percentages and both reports)'))
W5 = twoway('w5', 'University', 'Gender', ['Male', 'Female'], [('Yes', ['50', '54']), ('No', ['55', '41'])], total=['105', '95', '200'], totcol=['104', '96'])
W5P = twoway('w5p', 'University', 'Gender (%)', ['Male', 'Female'], [('Yes', [('a', '47.6%'), ('b', '56.8%')]), ('No', [('c', '52.4%'), ('d', '43.2%')])], total=['100.0%', '100.0%'])
KI_ASSOC = 'Percentage down each <b>EV column</b>, then compare <b>one row</b><div class="kn">clearly different % → associated</div>'
S.append(qslide('ex', 5, 'Describing an association from a percentaged table (2 × 2)', 'Cambridge · Example 5',
    'Are males and females in Year 9 equally likely to indicate an intention to go to university? Data from interviews with 200 Year 9 students are summarised in the following table. Write a brief report addressing this question and quoting appropriate percentages.',
    KI_ASSOC, [(r'Male column: $\dfrac{50}{105} \times 100\% = 47.6\%$, 52.4%', 'tc:w5:0,100,900 tf:w5p:a,c'), ('Female column: 54/95 → 56.8% · 41/95 → 43.2%', 'tc:w5:1,101,901 tf:w5p:b,d'),
                ('Compare one row: Yes: 56.8% of females vs 47.6% of males: clearly different, so associated.', 'hr:w5p:0')],
    'In this sample of 200 Year 9 students, a greater proportion of females than males (56.8% compared with 47.6%) were intending to go to university. There is an association between gender and intention to go to university.',
    CG + ', 2B Example 5 (p. 114, report verbatim)', fig='<div class="zfigc">' + W5 + W5P + '</div>', figw='.8fr', cls='tight', ans_do='tf:w5p:a,b,c,d hr:w5p:0'))
Y4 = twoway('y4', 'preference', 'age', ['under 20', '%', '20 and over', '%'], [('hardcopy', ['20', '56%', '15', '75%']), ('digital', ['16', '44%', '5', '25%'])], total=['36', '100%', '20', '100%'])
Y4R = report('y4r', ['Yes, there is an association between ', ('a', '<i>preference</i> and <i>age</i>'), '. The percentage of people that prefer hardcopy books differs depending on their age, since only ',
                     ('b', '56%'), ' of those ', ('c', 'under 20'), ' prefer it while ', ('d', '75%'), ' of those ', ('e', 'aged 20 years and over'), ' do.'])
S.append(qslide('yt', 5, 'Describing an association from a percentaged two-way table', 'Edrolo 2A WE4',
    'A group of people were surveyed on their <i>preference</i> towards reading hardcopy or digital books. Their <i>age</i> (under 20, 20 and over) was recorded along with their book <i>preference</i> (hardcopy, digital).<br>The results were displayed in a two-way percentage frequency table.<br>Is there an association between <i>age</i> and <i>preference</i>? Justify your answer by quoting appropriate percentages.',
    KI_ASSOC, [('Compare one row: hardcopy: 56% (under 20) vs 75% (20 and over): a 19% difference.', 'tc:y4:1,3 tf:y4r:a'), ('Quote both percentages, with their categories.', 'tf:y4r:b,c,d,e')],
    'The report opposite.', ED + ', 2A Worked example 4 (p. 110). Working by teacher.', fig='<div class="zfigc">' + Y4 + Y4R + '</div>', figw='1.1fr', cls='tight'))
W6 = lambda id_: twoway(id_, 'Interest in sport', 'Age group (%)', ['Under 18 years', '19–25 years', '26–35 years', '36–50 years'],
                        [('High', ['56.5', '50.2', '40.7', '35.0']), ('Medium', ['30.1', '34.4', '36.8', '44.7']), ('Low', ['13.4', '15.4', '22.5', '20.3'])], total=['100.0'] * 4, cls='zsm')
S.append(qslide('ex', 6, 'Describing associations from a percentaged table (3 × 3)', 'Cambridge · Example 6',
    'A survey was conducted with 1000 males under 50 years old. As part of this survey, they were asked to rate their interest in sport as ‘high’, ‘medium’, or ‘low’. Their age group was also recorded as ‘under 18’, ‘19–25’, ‘26–35’ and ‘36–50’. The results are displayed in the table.',
    KI_ASSOC, [], None, CG + ', 2B Example 6 (pp. 115–116)',
    parts=[('a', 'Which is the explanatory variable, <i>interest in sport</i> or <i>age group</i>?', ['Age could explain interest in sport, but interest in sport cannot explain age.'], '<i>Age group</i> is the EV.'),
           ('b', 'Is there an association between <i>interest in sport</i> and <i>age group</i>? Write a brief response quoting appropriate percentages.',
            [('The % differ for each age group in every row: associated. Choose one row: High.', 'hr:w6:0')],
            'There is an association between the level of interest in sport and age. A high level of interest in sport is seen to decrease steadily across the age categories from 56.5% for under 18 years, 50.2% for 19–25 years, 40.7% for 26–35 years to, at its lowest, 35% for 36–50 years.', 'hr:w6:0')],
    fig=W6('w6'), figw='1fr', cls='tight zs16'))
CF = [[22, 16, 10, 2], [5, 10, 14, 17], [3, 4, 6, 11]]
CT = twoway('y2t', 'caffeine intake', 'age', ['20–29', '30–39', '40–49', '50–59'], [(n, [str(x) for x in CF[j]]) for j, n in enumerate(['low', 'medium', 'high'])], cls='zsm')
S.append(qslide('yt', 6, 'Constructing a grouped bar chart', 'Edrolo 2A WE2',
    'A group of individuals between the ages of 20 and 59 were asked how much coffee they drink a day. Their <i>caffeine intake</i> was categorised as ‘low’, ‘medium’ and ‘high’. Their <i>age</i> was also recorded and grouped as ‘20–29’, ‘30–39’, ‘40–49’ and ‘50–59’. The results are displayed in a two-way frequency table.<br>Use the frequency table to construct a grouped bar chart.',
    'EV across the horizontal axis; one bar per RV category in each group<div class="kn">add a legend</div>',
    ['<i>age</i> is more likely to dictate <i>caffeine intake</i>: age goes on the horizontal axis.', ('Axes: frequency up, to at least 22 (the largest value); the four age groups across.', 'ax:y2g'),
     ('20–29: bars 22, 5, 3 (low, medium, high)', 'tc:y2t:0,100,200 bg:y2g:0,1,2'), ('30–39: 16, 10, 4', 'tc:y2t:1,101,201 bg:y2g:10,11,12'),
     ('40–49: 10, 14, 6 · 50–59: 2, 17, 11; add a legend', 'tc:y2t:2,102,202,3,103,203 bg:y2g:20,21,22,30,31,32 lg:y2g')],
    'The grouped bar chart opposite.', ED + ', 2A Worked example 2 (pp. 107–108). Working by teacher.',
    fig='<div class="zfigc">' + CT + gbar('y2g', ['20–29', '30–39', '40–49', '50–59'], ['low', 'medium', 'high'], CF, 25, 5, 'age', 'frequency', w=560, h=300) + '</div>',
    figw='1.15fr', cls='tight', ans_do='ax:y2g bg:y2g:0,1,2,10,11,12,20,21,22,30,31,32 lg:y2g'))

# ---- NL: segmented bar chart, then Examples 7, 8
SM = twoway('smt', 'Smoking status', 'Education level (%)', ['Year 9 or less', 'Year 10 or 11', 'Year 12', 'University'],
            [('Smoker', ['34.0', '31.7', '26.5', '18.4']), ('Past smoker', ['36.0', '33.8', '30.9', '28.0']), ('Never smoked', ['30.0', '34.5', '42.6', '53.6'])], total=['100.0'] * 4, cls='zsm')
SMG = schart('smg', [('Yr 9 or less', [34.0, 36.0, 30.0]), ('Yr 10 or 11', [31.7, 33.8, 34.5]), ('Yr 12', [26.5, 30.9, 42.6]), ('University', [18.4, 28.0, 53.6])],
             ['Smoker', 'Past smoker', 'Never smoked'], 100, 20, 'Percentage', 'Level of education', w=760, h=360)
S.append(nl_slide('The segmented bar chart: table → bars',
    'One bar for each <b>EV</b> category (each column of the table); each bar is 100%, split into <b>RV</b> segments; same colour for the same RV category in every bar, plus a key. <span class="hint">Click to draw it.</span>',
    '<div class="cols" style="grid-template-columns:.9fr 1.1fr"><div class="col">' + SM
    + st('<b>1</b> Axes: <i>level of education</i> across, <i>Percentage</i> 0 to 100 up.', do='ax:smg', cls='stp')
    + st('<b>2</b> Year 9 or less: 34.0, 36.0, 30.0', do='tc:smt:0,100,200 bg:smg:0,1,2', cls='stp')
    + st('<b>3</b> Year 10 or 11 and Year 12', do='tc:smt:1,101,201,2,102,202 bg:smg:10,11,12,20,21,22', cls='stp')
    + st('<b>4</b> University, then the key', do='tc:smt:3,103,203 bg:smg:30,31,32 lg:smg', cls='stp')
    + st('Look across one segment: smokers fall from 34.0% to 18.4% as education level rises, so smoking status is associated with education level.', do='hr:smt:0', cls='stp')
    + '</div><div class="col zc">' + SMG + '</div></div>', CG + ', 2B pp. 115–116 (smoking table and chart)'))
S.append(qslide('ex', 7, 'Constructing a segmented bar chart', 'Cambridge · Example 7',
    'Construct a segmented bar chart to display the association <i>interest in sport</i> and <i>age group</i> displayed in the table in Example 6.',
    'One 100% bar per <b>EV</b> category<div class="kn">segments = RV; add a key</div>',
    [('<i>age group</i> is the EV: horizontal axis. Vertical axis 0% to 100%, in intervals of 10%.', 'ax:w7g'), ('under 18: High to 56.5 · Medium to 86.6 · Low to 100', 'tc:w7:0,100,200 bg:w7g:0,1,2'),
     ('19–25: 50.2 · 84.6 · 100', 'tc:w7:1,101,201 bg:w7g:10,11,12'), ('26–35: 40.7 · 77.5 · 100 &nbsp;|&nbsp; 36–50: 35.0 · 79.7 · 100; add the key', 'tc:w7:2,102,202,3,103,203 bg:w7g:20,21,22,30,31,32 lg:w7g')],
    'The segmented bar chart opposite.', CG + ', 2B Example 7 (pp. 116–117)',
    fig='<div class="zfigc">' + W6('w7') + schart('w7g', [('under 18', [56.5, 30.1, 13.4]), ('19–25', [50.2, 34.4, 15.4]), ('26–35', [40.7, 36.8, 22.5]), ('36–50', [35.0, 44.7, 20.3])],
        ['High', 'Medium', 'Low'], 100, 10, 'Interest in sport (%)', 'Age group (years)', w=720, h=330) + '</div>', figw='1.3fr', cls='tight', ans_do='ax:w7g bg:w7g:0,1,2,10,11,12,20,21,22,30,31,32 lg:w7g'))
HT_ = twoway('y3t', 'height', 'year level', ['Year 11', 'Year 12'], [('short', ['15%', '20%']), ('average', ['20%', '30%']), ('tall', ['65%', '50%'])], total=['100%', '100%'])
S.append(qslide('yt', 7, 'Constructing a percentage segmented bar chart', 'Edrolo 2A WE3',
    'A group of students in Year 11 and Year 12 were asked to describe their <i>height</i> as ‘short’, ‘average’ or ‘tall’. Their responses, as well as their <i>year level</i>, were recorded in the following percentage frequency table.<br>Use the frequency table to construct a percentage segmented bar chart.',
    'One 100% bar per <b>EV</b> category<div class="kn">each segment ends at the previous end + its %</div>',
    [('<i>year level</i> is more likely to dictate <i>height</i>: horizontal axis. Vertical axis 0 to 100%.', 'ax:y3g'),
     ('Year 11: short ends at 15 · average at 15 + 20 = 35 · tall at 35 + 65 = 100', 'tc:y3t:0,100,200 bg:y3g:0,1,2'),
     ('Year 12: 20 · 20 + 30 = 50 · 50 + 50 = 100; add a legend', 'tc:y3t:1,101,201 bg:y3g:10,11,12 lg:y3g')],
    'The percentage segmented bar chart opposite.', ED + ', 2A Worked example 3 (p. 109). Working by teacher.',
    fig='<div class="zfigc">' + HT_ + schart('y3g', [('Year 11', [15, 20, 65]), ('Year 12', [20, 30, 50])], ['short', 'average', 'tall'], 100, 10, 'frequency (%)', 'year level', w=480, h=330) + '</div>',
    figw='1fr', ans_do='ax:y3g bg:y3g:0,1,2,10,11,12 lg:y3g'))
S.append(qslide('ex', 8, 'Identifying and describing associations from a segmented bar chart', 'Cambridge · Example 8',
    'The percentaged segmented bar chart below shows the association between <i>preferred holiday</i> (country or coast) and <i>age group</i> (under 40, 40 or over) for a sample of 800 visitors to a travel website.<br>Does the percentaged segmented bar chart support the contention there is an association between <i>preferred holiday</i> and <i>age group</i>?',
    'Look <b>across</b> one segment<div class="kn">heights differ → associated; quote the two %</div>',
    ['The segment heights (percentages) differ for each age group: associated.', 'Choose one segment: coast: 75% (under 40) vs 60% (40 and over).'],
    'There is an association between the holiday preference and age. Those aged under forty are more likely to choose a coastal holiday (75%) than those aged forty or over (60%).', CG + ', 2B Example 8 (p. 117)',
    fig=schart('w8g', [('under 40', [75, 25]), ('40 and over', [60, 40])], ['coast', 'country'], 100, 10, 'Preferred holiday (%)', 'Age group', full=True, w=480, h=330), figw='.9fr'))
S.append(qslide('yt', 8, 'Describing an association from a percentage segmented bar chart', 'Edrolo 2A WE5',
    'A large group of people between the ages of 18 and 25 were asked what their current <i>employment status</i> was. They were classified as either ‘employed’ or ‘unemployed’. Their <i>age</i> was also recorded and classified as ‘18–21’ or ‘22–25’.<br>The results have been displayed in a percentage segmented bar chart.<br>Is there an association between <i>employment status</i> and <i>age</i>? Justify your answer by quoting appropriate percentages.',
    'Look <b>across</b> one segment<div class="kn">heights differ → associated; quote the two %</div>',
    ['Compare one segment: employed: 40% (18–21) vs 75% (22–25): a 35% difference.', 'Quote both percentages, with their age groups.'],
    'Yes, there is an association between <i>employment status</i> and <i>age</i>. The percentage of people that are employed tends to increase with age, with 40% of 18–21 year olds employed and 75% of 22–25 year olds employed.',
    ED + ', 2A Worked example 5 (pp. 110–111). Working by teacher.',
    fig=schart('y5g', [('18–21', [40, 60]), ('22–25', [75, 25])], ['employed', 'unemployed'], 100, 10, 'frequency (%)', 'age', full=True, w=480, h=330), figw='.9fr'))

# ---- Exits
UK = [('Belfast', 'high', 'small', 52), ('Edinburgh', 'high', 'small', 43), ('London', 'high', 'large', 40), ('Manchester', 'high', 'large', 44), ('Brighton and Hove', 'high', 'small', 35), ('Bournemouth', 'high', 'small', 36),
      ('Sheffield', 'medium', 'small', 36), ('Hull', 'medium', 'small', 40), ('Bristol', 'medium', 'small', 39), ('Newcastle-Sunderland', 'medium', 'large', 34), ('Leicester', 'medium', 'small', 36), ('Liverpool', 'medium', 'large', 29),
      ('Swansea', 'low', 'small', 30), ('Glasgow', 'low', 'large', 34), ('Cardiff', 'low', 'small', 31), ('Nottingham', 'low', 'small', 31), ('Birmingham-Wolverhampton', 'low', 'large', 29), ('Leeds-Bradford', 'low', 'large', 31),
      ('Portsmouth', 'low', 'small', 27), ('Southampton', 'low', 'small', 30), ('Reading', 'low', 'small', 31), ('Coventry', 'low', 'small', 30), ('Stoke-on-Trent', 'low', 'small', 29)]
UKT = lambda rng: ('<table class="ztab zuk"><tr><th><i>City</i></th><th><i>Congestion level</i></th><th><i>Size</i></th><th><i>Increase in travel time</i> (minutes per day)</th></tr>'
                   + ''.join(f'<tr><td>{UK[i][0]}</td><td>{UK[i][1]}</td><td>{UK[i][2]}</td><td>{UK[i][3]}</td></tr>' for i in rng) + '</table>')
X1 = twoway('x1t', 'Congestion level', 'City size', ['Small', 'Large'], [('high', ['4', ('a', '2')]), ('medium', [('b', '4'), ('c', '2')]), ('low', [('d', '8'), ('e', '3')])], total=['16', ('f', '7')])
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2018 Exam 2 Q1d',
    '<span class="zsmq">The data in Table 1 relates to the impact of traffic congestion in 2016 on travel times in 23 cities in the United Kingdom (UK). The four variables in this data set are: <i>city</i> – name of city · <i>congestion level</i> – traffic congestion level (high, medium, low) · <i>size</i> – size of city (large, small) · <i>increase in travel time</i> – increase in travel time due to traffic congestion (minutes per day).</span>'
    + f'<div class="zrowc">{UKT(range(12))}{UKT(range(12, 23))}</div>Use the data in Table 1 to complete the following two-way frequency table, Table 2.',
    'Count each <b>pair</b> of categories<div class="kn">check: the total = the number of cities</div>',
    [('High, large: London, Manchester: 2', 'tf:x1t:a'), ('Medium: small 4 · large 2', 'tf:x1t:b,c'), ('Low: small 8 · large 3', 'tf:x1t:d,e'), ('Total large: 2 + 2 + 3 = 7 · check: 16 + 7 = 23 cities', 'tf:x1t:f')],
    'Table 2 completed (opposite).', ED + ', 2A Q11 (VCAA 2018 Further Mathematics Exam 2 Core Q1d); % = average 1.9 out of 2 from the examiner report.',
    fig='<div class="zfigc"><b>Table 2</b>' + X1 + '</div>', figw='1.6fr', marks=2, vcaa=94, cls='tight x1s',
    watch='count from the table, row by row: tick each city as you count it so none is missed or counted twice.'))
OT = lambda d, i, t: (f'<table class="ztab zot"><tr><th></th><th>Under 55</th><th>55 and over</th></tr><tr><td>domestic</td><td>{d[0]}</td><td>{d[1]}</td></tr>'
                      f'<tr><td>international</td><td>{i[0]}</td><td>{i[1]}</td></tr><tr><td><b>Total</b></td><td>{t[0]}</td><td>{t[1]}</td></tr></table>')
OPTDIST['2 of 2'] = [50, 13, 28, 1, 8]
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2021 Exam 1 Q3',
    'The percentaged segmented bar chart below shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).<br>The results could also be summarised in a two-way frequency table.<br>Which one of the following frequency tables could match the percentaged segmented bar chart?',
    'Work out the column % of each table<div class="kn">and compare with the chart</div>',
    ['Read the chart: under 55: 65% domestic, 35% international · 55 and over: 45% domestic, 55% international.', 'A: 91/140 = 65%, 49/140 = 35%, 90/200 = 45%, 110/200 = 55% ✓'],
    'Table A gives the same percentages as the chart.', ED + ', 2A Q13 (VCAA 2021 Further Mathematics Exam 1 Core Q3); % from the examiner report.',
    fig=schart('x2g', [('under 55 years', [65, 35]), ('55 years and over', [45, 55])], ['domestic', 'international'], 100, 10, 'percentage', 'age (years)', full=True, w=480, h=260),
    figw='1.7fr', marks=1, vcaa=50, cls='x2s',
    opts=[('A', OT((91, 90), (49, 110), (140, 200))), ('B', OT((65, 35), (45, 55), (110, 90))), ('C', OT((35, 55), (65, 45), (100, 100))), ('D', OT((50, 70), (100, 50), (150, 120))), ('E', OT((71, 39), (29, 61), (100, 100)))], key='A'))

checkin(SC)
coursework('2A–2B', 'Coursework · Exercises 2A and 2B', [('Cambridge Exercise 2A', 'Q1–6'), ('Cambridge Exercise 2B', 'Q1–12'), ('Practice booklet', '2B section (Insight + skill sheet)')],
           'Exercise 2A: Bivariate data', CG + ', Exercises 2A and 2B; Chapter 2 workbook practice questions', fit=False)

LESSON_CSS = r'''
.slide.z .st.zcard{align-self:start}
.slide.zs16 .zw .st.zs,.slide.zs16 .zw .zpq{font-size:15.5px!important;line-height:1.3!important;margin:2px 0!important}

#cn .zc{min-width:44px;text-align:center;font-size:18px}
.slide.z .st.zcard{border:2.5px solid #000;padding:10px 12px;box-shadow:4px 4px 0 #bbb;font-size:20px;color:#000;margin:0!important}
.slide.z .st.zcard i.zsub{display:block;font-style:normal;font-size:16px;color:#444;margin-top:6px}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:14px!important}
.ztab.zsm2{font-size:15px}.ztab.zsm2 td,.ztab.zsm2 th{padding:1px 6px}
.ztab.zuk{font-size:11px;line-height:1.05}.ztab.zuk td,.ztab.zuk th{padding:0 4px}
.zsmq{font-size:15px;line-height:1.25;display:block}
.slide.x1s .zq{font-size:15px}
.ztab.zot{font-size:11px;margin:0}.ztab.zot td,.ztab.zot th{padding:0 4px}
.slide.x2s .zmc>div{display:flex;align-items:flex-start;gap:4px;padding:2px 34px 2px 4px}
.slide.x2s .zmc{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px}
.zfigc svg.zch{width:100%!important;max-height:340px!important;min-width:0}
.zfigc .zrep{font-size:17px}
'''
build('S6-slides.html', '12MAG S6 · Investigating associations between two categorical variables · Slides', css=LESSON_CSS)
