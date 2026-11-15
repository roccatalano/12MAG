# Chapter 2 revision booklet: Insight GM1 (MC) + GM2 (SA), "Investigating associations between two variables and
# modelling linear associations" (GM1 pp.12-22 Q1-34; GM2 pp.14-31 Q1-15). Only the association questions/parts
# (Cambridge 2A-2I) are used; the regression parts (3A-3D) are left for the Ch 3 booklet.
# Text verbatim from Insight (scanned books; read off the page images). Figures are crops of the Insight pages
# (crop.py). Shared "Use the following information" stems are repeated inside each box.
def tbl(head, rows, cls='t'):
    h = f'<table class="{cls}"><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
    return h + '</table>'

def across(lab, cols):  # a long two/three-column table laid out across the page (same data)
    h = '<table class="t sm">'
    for i, l in enumerate(lab):
        h += f'<tr><th>{l}</th>' + ''.join(f'<td>{c[i]}</td>' for c in cols) + '</tr>'
    return h + '</table>'

G1 = 'Insight GM1 U3 Data Analysis'
G2 = 'Insight GM2 U3 Data Analysis'

A6 = [18,12,22,13,22,14,14,21,26,20,23,37,19,19,23,15,27,24,21,27,16,28,32,24,31,25]
B6 = [22,15,25,16,25,16,20,30,31,28,25,40,22,29,32,21,32,34,24,29,20,36,37,25,34,33]
TRIAL_T = ''.join(across(['Student', 'Score on <i>first trial exam</i>', 'Score on <i>final trial exam</i>'],
                         [(i + 1, A6[i], B6[i]) for i in range(k, k + 13)]) for k in (0, 13))
TRIAL6 = ('<p class="q">The Year 12 teacher continued to perform statistical analysis on the scores of his Year 12 students. This time the teacher considered the score out of forty on the students’ first multiple-choice trial exam and the score achieved on the final multiple-choice trial exam. The teacher does not give half marks for this exam.</p>'
          '<p class="q">These results are represented in the parallel boxplots below.</p>' + TRIAL_T + '[[g1q6]]')
TRIAL79 = ('<p class="q">The Year 12 teacher continued his analysis of the students’ trial exams by considering whether an association exists between the students’ <i>first trial exam</i> and their <i>final trial exam</i>.</p>'
           '<p class="q">In order to assist with this, the teacher recorded the data in a table as well as plotting this on a scatterplot. The value of Pearson’s correlation coefficient, <i>r</i>, for the scatterplot are 0.916.</p>'
           '<p class="q">Both the table and scatterplot are shown below.</p>' + TRIAL_T + '[[g1q9]]')
BABY = ('<p class="q">The scatterplot below displays the <i>birth weight</i>, in kilograms, of newborn babies, and weight, in kilograms, of the mother at 39 weeks pregnant. A least squares line has been fitted to the data.</p>[[g1q12]]')
CAFE = ('<p class="q">The <i>number of customers</i> at a café and the <i>revenue</i> received each day is recorded for ten days and displayed in the scatterplot below.</p>'
        '<p class="q">A least squares line has been fitted to the data.</p>[[g1q24]]'
        + tbl(['', '<i>Number of customers</i>', '<i>Revenue</i> ($)'], [['<b>Mean</b>', '82.4', '4595'], ['<b>Standard deviation</b>', '35.4', '2082.3'], ['<b>Correlation coefficient <i>r</i></b>', '0.9453', '']]).replace('<td>0.9453</td><td></td>', '<td colspan="2">0.9453</td>'))
VEG = ('<p class="q">The <i>average number of servings of vegetables</i> eaten per day by a sample of people is shown below.</p>'
       '<p class="q">The back-to-back stem plot below compares the data for those <i>under 18 years</i> and those <i>18 years or older</i>.</p>'
       '<div class="stk"><span>key: 3|1 = 3.1</span></div>'
       '<table class="b2b"><tr><th><i>under 18 years</i></th><th></th><th><i>18 years or older</i></th></tr>'
       + ''.join(f'<tr><td class="lf">{a}</td><td class="st">{s}</td><td class="rt">{b}</td></tr>' for a, s, b in [
           ('3', '0', ''), ('8 5 3 3', '1', '7 8 8'), ('9 5 5 3 1 1', '2', '3 4 4 6 8'), ('8 7 4 4', '3', '4 7 7 7 8 9 9'), ('5 2', '4', '1 3 5 8 8 8'), ('7', '5', '3 7')])
       + '</table>')

def MC(n, sub, page, stem_, opts, a, why, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)

Q = [
 MC(1, '2C', 12, '<p class="q">The following boxplots show the weights of male students in both Year 8 (red) and 9 (yellow).</p>[[g1q1]]'
    '<p class="q">Which of the following statements is <b>not</b> true with regard to the weights of Year 8 and 9 male students?</p>',
    ['Less than 75% of male Year 9 students weigh more than the heaviest male student in Year 8.',
     'The distribution of Year 9 male students is negatively skewed with an outlier.',
     'The variation in weights for Year 8 male students has a similar variance to the distribution of Year 9 male students.',
     'The mean would be an appropriate measure of centre for the distribution of Year 8 students due to the fact that the distribution does not contain an outlier.',
     'The distribution for Year 8 male students is positively skewed, with a median at 58 kg.'],
    'D', 'Year 8 is positively skewed, so the mean is not a suitable measure of centre (the lower box is Year 8; the scan is in grey).'),
 MC(6, '2C', '14–15', TRIAL6 + '<p class="q">The data displayed in the parallel boxplots supports the contention that, on average, there is an improvement in the students’ <i>score out of forty</i> between their first trial exam and their final trial exam because</p>',
    ['the maximum score for the first trial exam is higher than the median score for the final trial exam.',
     'the range of the distribution of <i>scores out of forty</i> increases from 20 for the first trial exam to 25 for the final trial exam.',
     'the distribution of <i>scores out of forty</i> for the first trial exam is approximately symmetric, compared to the distribution for the final trial exam, which is positively skewed.',
     'the interquartile range for the <i>scores out of forty</i> in the first trial exam is greater than that for the final trial exam.',
     'the median <i>score out of forty</i> has increased from 22 in the first trial exam to 26.5 in the final trial exam.'],
    'E', '“On average” → compare medians: 22 → 26.5.'),
 MC(33, '2C', 22, VEG + '<p class="q">The percentage of the sample for which the <i>average number of servings of vegetables</i> eaten per day was at least 3.5 is closest to</p>',
    ['19%', '22%', '41%', '46%', '54%'], 'D', '19 of the 41 values are 3.5 or more: 19 ÷ 41 × 100 = 46%', shared='Q33–34'),
 MC(34, '2C', 22, VEG + '<p class="q">How much higher is the median for <i>18 years or older</i> compared to <i>under 18 years</i>?</p>',
    ['1.2', '1.6', '2.5', '3.7', '12'], 'A', 'Medians: under 18 = 2.5 (n = 18), 18 or older = 3.7 (n = 23); 3.7 − 2.5 = 1.2', shared='Q33–34'),
 MC(28, '2D', 20, '<p class="q">Which of the following would <b>not</b> represent a positive association?</p>',
    ['temperature and number of heaters sold', 'population and number of hospitals', 'time spent exercising and calories burned',
     'number of cars on the road and levels of sound pollution', 'hours of study and test results'],
    'A', 'As temperature increases, fewer heaters are sold: a negative association.'),
 MC(12, '2G', 16, BABY + '<p class="q">If the coefficient of determination is 0.6877, the correlation coefficient, <i>r</i>, is closest to</p>',
    ['−0.829', '−0.688', '−0.473', '0.473', '0.829'], 'E', 'r = √0.6877 = 0.829; the association is positive, so r is positive.'),
 MC(24, '2G', 19, CAFE + '<p class="q">What is the coefficient of determination, as a percentage, to three significant figures?</p>',
    ['0.894%', '0.945%', '89.3%', '89.4%', '94.5%'], 'D', 'r² = 0.9453² = 0.8936 → 89.4%'),
 MC(9, '2H', '15–16', TRIAL79 + '<p class="q">The Year 12 teacher would like to draw a conclusion from the regression analysis, regarding the correlation between his students’ <i>first trial exam</i> score and their <i>final trial exam</i> score.</p><p class="q">Which of the following statements is <b>correct</b>?</p>',
    ['If a student achieves a score over 20 marks for their <i>first trial exam</i>, they will always achieve a high score in their <i>final trial exam</i>.',
     'A high score in the <i>first trial exam</i> will cause a student to get a high score in their <i>final trial exam</i>.',
     'Students who studied a lot between exams improved their scores.',
     'On average, there was always an increase in scores between <i>first trial exam</i> and <i>final trial exam</i>.',
     'There is a correlation between <i>first trial exam</i> and <i>final trial exam</i>. On average, as the <i>first trial exam</i> score increased, so did the <i>final trial exam</i> score. This suggests that a student with a higher <i>first trial exam</i> score will also have a higher <i>final trial exam</i> score.'],
    'E', 'Correlation does not imply causation (B), and “always” cannot be claimed (A, D); there is no data on study (C).'),
 MC(17, '2I', 17, '<p class="q">Percentaged segmented bar charts would be an appropriate graphical tool to investigate the association between which of the following pairs of variables?</p>',
    ['height (in cm) and weight (in kg) of 18-year-old males', 'height of 18-year-old males (in cm) and country of birth (Australia, China and Germany)',
     'fitness levels (below average, average, above average) of 18-year-old males and country of birth (Australia, China and Germany)',
     'fitness levels (below average, average, above average) and weight (in kg) of 18-year-old males', 'weight (in kg) of 18-year-old males and country of birth (Australia, China and Germany)'],
    'C', 'Segmented bar charts need two categorical variables.'),
]

def SA(n, sub, page, stem_, parts, why=None, note=None):
    return dict(kind='sa', n=n, sub=sub, marks=sum(p[4] for p in parts), stem=stem_, parts=parts, why=why, note=note, src=f'{G2} p.{page} Q{n}')

def segbar(sol):
    # Insight GM2 Q13a chart (redrawn): male column given (45/58 = 77.6% under 5 km); female column drawn in the solutions.
    W, H, x0, y0, h = 330, 200, 50, 10, 160
    s = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H + 30}" font-family="Arial" font-size="10">'
    for p in range(0, 101, 10):
        y = y0 + h - h * p / 100
        s += f'<line x1="{x0}" x2="{x0 + 200}" y1="{y}" y2="{y}" stroke="#ccc"/><text x="{x0 - 4}" y="{y + 3}" text-anchor="end">{p}%</text>'
    def col(x, f, col):
        yy = y0 + h - h * f
        return (f'<rect x="{x}" y="{yy}" width="50" height="{h * f}" fill="{col}" stroke="#000"/>'
                f'<rect x="{x}" y="{y0}" width="50" height="{yy - y0}" fill="#fff" stroke="#000"/>')
    s += col(x0 + 25, 45 / 58, '#999')
    if sol: s += col(x0 + 125, 62 / 97, '#e8a0a0').replace('stroke="#000"', 'stroke="#c00"')
    s += (f'<text x="{x0 + 50}" y="{y0 + h + 14}" text-anchor="middle" font-size="11">male</text><text x="{x0 + 150}" y="{y0 + h + 14}" text-anchor="middle" font-size="11">female</text>'
          f'<text x="{x0 + 100}" y="{y0 + h + 28}" text-anchor="middle" font-style="italic">sex</text>'
          f'<rect x="{x0 + 215}" y="70" width="9" height="9" fill="#fff" stroke="#000"/><text x="{x0 + 228}" y="78">over 5 km</text>'
          f'<rect x="{x0 + 215}" y="88" width="9" height="9" fill="#999" stroke="#000"/><text x="{x0 + 228}" y="96">under 5 km</text>'
          f'<text transform="translate(10,{y0 + h / 2}) rotate(-90)" text-anchor="middle" font-style="italic">frequency (%)</text></svg>')
    return s

PAY = across(['<i>Hourly pay rate</i> ($)', '<i>Hours worked</i>'], list(zip(
    ['11.40', '18.20', '10.30', '12.40', '13.50', '16.00', '13.00', '14.75', '16.80', '16.70', '18.20', '25.00', '17.25', '15.80', '20.16', '21.15', '22.60', '18.00', '20.50', '17.25', '18.90', '17.10', '18.00'],
    [5, 10, 4, 12, 5, 10, 9, 8, 10, 8, 9, 19, 10, 14, 12, 16, 18, 14, 15, 16, 21, 18, 20])))
GYM = across(['Day number', 'Maximum daily temperature (°C)', 'Number of patrons'],
             list(zip(range(1, 13), [17, 26, 25, 22, 29, 22, 27, 14, 16, 15, 16, 24], [226, 128, 162, 187, 107, 156, 139, 210, 198, 185, 173, 139])))
REST = 'Insight’s other parts of this question (least squares line, residuals) are in the Chapter 3 booklet.'

Q += [
 SA(1, '2C', 14, '<p class="q">A boxplot has been drawn for the <i>hours worked</i> data gathered. These boxplots are shown below.</p>[[g2q1]]',
    [('', 'Is there a correlation between the variables <i>age group</i> and <i>hours worked</i>?<br>Quote appropriate statistics in your explanation.',
      'Yes. As age group increases from 18–24 to 25–30, the median hours worked increases from 17.5 to 35 hours (and the IQR from 16 to 20 hours).', 26, 2)],
    why='Insight’s Ch 1 questions describe the same train survey of hours worked (18–24 and 25–30 years).'),
 SA(3, '2C', 16, '<p class="q">End of year results for a Year 11 mathematics exam were recorded by the teacher as a score out of 50. The teacher was interested in determining whether <i>gender</i> is related to <i>end of year result</i>.</p>'
    '<p class="q">The students’ Year 11 mathematics results are shown in the graph below.</p>[[g2q3]]',
    [('', 'The data shown in the boxplots above suggest that <i>end of year result</i> is associated with <i>gender</i>.<br>Explain why, quoting the values of an appropriate statistic.',
      'The median end of year result differs: 32 for males compared with 26 for females. The median is higher for males, so result is associated with gender.', 26, 2)]),
 SA(6, '2C', 20, '<p class="q">The parallel boxplots below show the <i>number of calories burned</i> by <i>Gym patron 1</i> and <i>Gym patron 2</i> for the same 13-day period.</p>[[g2q6]]',
    [('a', 'What is the minimum number of calories burned by <i>Gym patron 2</i>?', 'About 275 calories (270–280).', 8, 1),
     ('b', 'On approximately how many days over the 13-day period did <i>Gym patron 2</i> burn less calories than the minimum number of calories burned by <i>Gym patron 1</i>?',
      'Patron 1’s minimum (about 558) is near Patron 2’s median, so about 50% of 13 days = 6.5 → about 7 days.', 12, 1),
     ('c', 'On a particular day, <i>Gym patron 2</i> burned 275 calories.<br>Explain why this value is an outlier for the data set.',
      'IQR ≈ 125. LF = <i>Q</i><sub>1</sub> − 1.5 × IQR = 490 − 1.5 × 125 = 302.5. 275 &lt; 302.5 = LF → outlier.', 22, 2)]),
 SA(9, '2C', 24, '<p class="q">The median income ($) for males and females in three age groups is shown in the table below.</p>'
    + tbl(['Age (years)', 'Male', 'Female'], [['35–44', '80&#8239;800', '52&#8239;410'], ['45–54', '82&#8239;805', '54&#8239;470'], ['55–64', '72&#8239;330', '50&#8239;555']]),
    [('a', 'Which of the two variables shown, <i>sex</i> or <i>age</i>, is an ordinal variable?', 'Age: here it is categorical ordinal (ordered groups 35–44, 45–54, 55–64).', 8, 1),
     ('b', 'Does the data shown support the assumption that the median income is associated with sex? Refer to the values of an appropriate statistic in your response.',
      'Yes. The median income differs with sex: e.g. for 35–44 year olds it is $80&#8239;800 for males compared with $52&#8239;410 for females.', 22, 2)]),
 SA(13, '2B', '27–28', '<p class="q">After work, Farah visits a homewares store next to the supermarket.</p>'
    '<p class="q">The homewares store records the postcode and sex of its customers over a week.<br>This information was used to construct the two-way frequency table below.</p>'
    '<table class="t"><tr><th></th><th colspan="3">Sex</th></tr><tr><th>Distance from store</th><th>Male</th><th>Female</th><th>Total</th></tr>'
    '<tr><td><b>Under 5 km</b></td><td>45</td><td>62</td><td>107</td></tr><tr><td><b>Over 5 km</b></td><td>13</td><td>35</td><td>48</td></tr>'
    '<tr><td><b>Total</b></td><td>58</td><td>97</td><td>155</td></tr></table>'
    '<p class="q">The information from the two-way frequency table is converted into a percentaged segmented bar chart.<br>The data for males has been completed.</p>[[SEGBAR]]',
    [('a', 'Draw the missing column for females on the <b>percentaged segmented bar chart above</b>.<br><i>(Answer on the percentaged segmented bar chart above.)</i>',
      'Under 5 km: 62 ÷ 97 = 64%; over 5 km: 35 ÷ 97 = 36% (drawn above).', 4, 2)],
    note='Part a only (the log histogram before it and part b are Ch 1 content). Chart redrawn from the table.'),
 SA(2, '2F', '14–15', '<p class="q">A small group of train travellers were surveyed on the morning train. Those who specified that they were in the 18–24 years age group were also asked what their <i>hourly pay rate</i> was, with the intention of identifying an association between <i>hours worked</i> and <i>hourly pay rate</i>.</p>'
    '<p class="q">The data are shown in the table below and are also displayed as a scatterplot.</p>' + PAY + '[[g2q2]]',
    [('a', 'Use the scatterplot to describe the relationship between <i>hourly pay rate</i> and <i>hours worked</i> in terms of strength, direction and form.', 'Moderate, positive, linear.', 10, 1),
     ('b', 'Find the value of Pearson’s correlation coefficient, rounding your answer to two decimal places.', 'CAS (x = hourly pay rate, y = hours worked): <i>r</i> = 0.718… = 0.72', 10, 1)],
    note='Parts a and b. ' + REST),
 SA(4, '2G', 17, '<p class="q">The teacher became concerned about the amount of homework her students were completing, and so began an investigation into the association between <i>hours of homework per week</i> and the <i>distance from school</i> for her students. A scatterplot of the data that the teacher gathered is shown below.</p>[[g2q4]]'
    '<p class="q">The equation of the least squares regression line is</p><p class="q" style="text-align:center"><i>hours of homework per week</i> = 7.46 − 0.0977 × <i>distance from school</i></p>',
    [('b', 'Describe the scatterplot in relation to its strength, direction and form.', 'Moderate (or weak), negative, linear.', 10, 1),
     ('d', 'The value of the coefficient of determination for the scatterplot is 0.1117.<br>Find the value of Pearson’s correlation coefficient, correct to three decimal places.',
      '√0.1117 = 0.334; the association is negative (negative slope), so <i>r</i> = −0.334', 12, 1)],
    note='Parts b and d. ' + REST),
 SA(5, '2G', '18–19', '<p class="q">During October 2018, there was only one scheduled flight between Melbourne and Darwin per day.</p>'
    '<p class="q">The minutes delayed and the wind speed (km/h) at 9 am in Melbourne for each day in October are plotted on the scatterplot below.</p>[[g2q5]]'
    '<p class="q">A least squares line is to be fitted to the data with the aim of predicting the number of minutes delayed from the wind speed on a particular day in Melbourne.</p>'
    '<p class="q">The equation of this line is</p><p class="q"><i>minutes delayed</i> = −10.745 + 18.051 × <i>wind speed</i></p>',
    [('a', 'Name the explanatory variable in this equation.', '<i>wind speed</i>', 8, 1),
     ('f', 'The value of the correlation coefficient <i>r</i> is 0.747.<br>Describe the strength of the relationship between <i>wind speed</i> and <i>minutes delayed</i>.', 'Strong (moderate also accepted).', 8, 1),
     ('g', 'What percentage of the variation in the number of minutes delayed for flights from Melbourne to Darwin can be explained by the variation in wind speed in Melbourne?<br>Round your answer to the nearest whole number.',
      '<i>r</i>² = 0.747² = 0.558 → 56%', 10, 1)],
    note='Parts a, f and g. ' + REST),
 SA(7, '2G', 21, '<p class="q">The maximum daily temperature (°C) and number of patrons attending the gym on the first 12 days of April 2019 are shown in Table 1 below.</p>'
    '<p class="q" style="text-align:center"><b>Table 1</b></p>' + GYM
    + '<p class="q">A least squares line is to be fitted to the data, using the maximum daily temperature as the explanatory variable.</p>',
    [('a', 'Complete the following sentence.<br>A least squares line is fitted to the data with the aim of predicting the ______________________ from the ______________________.',
      'number of patrons; maximum daily temperature', 6, 1),
     ('c', 'What percentage of the variation in number of patrons is explained by the variation in maximum daily temperature?<br>Round your answer to one decimal place.',
      'CAS: <i>r</i>² = 0.74371 → 74.4%', 10, 1)],
    note='Parts a and c. ' + REST),
 SA(14, '2G', '30–31', '<p class="q">Farah reads novels during her lunch and rest breaks. The amount of <i>time spent reading</i> by Farah, in minutes, and the <i>number of pages read</i> is shown on the scatterplot below.</p>[[g2q14]]'
    '<p class="q">A least squares line is fitted to the scatterplot. The equation of this line is</p><p class="q" style="text-align:center"><i>number of pages read</i> = 2.44 + 0.85 × <i>time spent reading</i></p>'
    '<p class="q">The correlation coefficient for the <i>time spent reading</i> and <i>number of pages read</i> is 0.9170</p>',
    [('c', 'Interpret the coefficient of determination in terms of the variables <i>time spent reading</i> and <i>number of pages read</i>.<br>Round the percentage to the nearest whole number.',
      '<i>r</i>² = 0.9170² = 0.84: 84% of the variation in <i>number of pages read</i> can be explained by the variation in <i>time spent reading</i>.', 16, 1)],
    note='Part c. ' + REST),
]

SUBS = [('2A', 'Response and explanatory variables'), ('2B', 'Investigating associations between two categorical variables'),
        ('2C', 'Investigating the association between a numerical and a categorical variable'), ('2D', 'Investigating associations between two numerical variables'),
        ('2E', 'How to interpret a scatterplot'), ('2F', 'Strength of a linear relationship: the correlation coefficient'),
        ('2G', 'The coefficient of determination'), ('2H', 'Correlation and causality'), ('2I', 'Which graph?')]
