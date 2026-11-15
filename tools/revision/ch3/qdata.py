# Chapter 3 revision booklet: Insight GM1 (MC) + GM2 (SA), "Investigating associations between two variables and
# modelling linear associations" (GM1 pp.12-22 Q1-34; GM2 pp.14-31 Q1-15). Uses the regression questions/parts the
# Ch 2 booklet left out (Cambridge 3A-3C). Transformation questions (GM1 Q5, 15, 16, 21, 22, 26, 27, 31, 32; GM2 Q12,
# Q15) are left for the Ch 4 booklet. Text verbatim from Insight (scanned books; read off the page images); answers and
# explanations from Insight's worked solutions (GM1 pp.36-42, GM2 pp.47-55), checked on the data with numpy.
# Figures are crops of the Insight pages (crop.py). Shared stems are repeated inside each box.
import os, importlib.util
_sp = importlib.util.spec_from_file_location('ch2q', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ch2', 'qdata.py'))
_c2 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_c2)
tbl, across, TRIAL79, BABY, CAFE = _c2.tbl, _c2.across, _c2.TRIAL79.replace('are 0.916', 'is 0.916'), _c2.BABY, _c2.CAFE
_T, _P = [17, 26, 25, 22, 29, 22, 27, 14, 16, 15, 16, 24], [226, 128, 162, 187, 107, 156, 139, 210, 198, 185, 173, 139]
GYM = ''.join(across(['Day number', 'Maximum daily temperature (°C)', 'Number of patrons'], list(zip(range(k + 1, k + 7), _T[k:k + 6], _P[k:k + 6]))) for k in (0, 6))  # same data, two rows of 6 to fit the box
_PR = ['11.40', '18.20', '10.30', '12.40', '13.50', '16.00', '13.00', '14.75', '16.80', '16.70', '18.20', '25.00', '17.25', '15.80', '20.16', '21.15', '22.60', '18.00', '20.50', '17.25', '18.90', '17.10', '18.00']
_HW = [5, 10, 4, 12, 5, 10, 9, 8, 10, 8, 9, 19, 10, 14, 12, 16, 18, 14, 15, 16, 21, 18, 20]
PAY = ''.join(across(['<i>Hourly pay rate</i> ($)', '<i>Hours worked</i>'], list(zip(_PR[k:k + 6], _HW[k:k + 6]))) for k in (0, 6, 12, 18))  # same data, four rows of 6 to fit the box  # same Insight stems as the Ch 2 booklet

G1 = 'Insight GM1 U3 Data Analysis'
G2 = 'Insight GM2 U3 Data Analysis'

EXAM = ('<p class="q">The scatterplot below shows the exam results as a percentage (<i>exam result</i>) plotted against the number of hours spent studying in the week immediately preceding the exam (<i>No. of hours studied</i>).</p>'
        '<p class="q">A least squares regression line has been fitted to the data.</p>[[g1q2]]'
        '<p class="q">The equation for this least squares regression line is</p><p class="q" style="text-align:center"><i>exam result</i> = 36.8 + 5.7 × <i>No. of hours studied</i></p>'
        '<p class="q">Pearson’s correlation coefficient is <i>r</i> = 0.7883.</p>')
CAR = ('<p class="q">The relationship between the age and price of a car is shown by the equation</p>'
       '<p class="q" style="text-align:center">Price ($) = 61&#8239;591 − 4164 × age (years)</p><p class="q">The correlation coefficient is −0.9978.</p>')
POOL = ('<p class="q">The data below shows the <i>temperature</i> and the <i>number of visitors</i> to a local pool each day over a 10-day period.</p>'
        + across(['Temperature (°C)', 'Number of visitors'], list(zip([17, 23, 27, 31, 33, 32, 38, 24, 18, 17], [63, 211, 294, 312, 233, 260, 251, 205, 77, 53]))) + '[[g1q30]]')

def MC(n, sub, page, stem_, opts, a, why, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)

Q = [
 # ---- 3A: the least squares line
 MC(7, '3A', 15, TRIAL79 + '<p class="q">The least squares regression equation for the relationship between <i>first trial exam</i> and <i>final trial exam</i> is</p>',
    ['<i>final trial exam</i> = 4.760 − 1.007 × <i>first trial exam</i>', '<i>first trial exam</i> = 4.760 + 1.007 × <i>final trial exam</i>',
     '<i>final trial exam</i> = 1.007 + 4.760 × <i>first trial exam</i>', '<i>final trial exam</i> = 4.760 + 1.007 × <i>first trial exam</i>',
     '<i>final trial exam</i> = −0.404 + 0.832 × <i>first trial exam</i>'],
    'D', 'CAS with x = first trial exam, y = final trial exam: a = 4.760, b = 1.007.', shared='Q7–9'),
 MC(11, '3A', 16, BABY + '<p class="q">The equation of the least squares line is closest to</p>',
    ['<i>mother’s weight</i> = −1.1203 + 0.063 × <i>birth weight</i>', '<i>mother’s weight</i> = −1.1203 − 0.063 × <i>birth weight</i>',
     '<i>birth weight</i> = −1.1203 − 0.063 × <i>mother’s weight</i>', '<i>birth weight</i> = 1.1203 + 0.063 × <i>mother’s weight</i>',
     '<i>birth weight</i> = −1.1203 + 0.063 × <i>mother’s weight</i>'],
    'E', 'Birth weight is the response variable (vertical axis); the line has a positive slope and crosses below 0 at mother’s weight = 0.', shared='Q10–13'),
 MC(14, '3A', 17, '<p class="q">The statistical analysis of a set of bivariate data involving variables <i>x</i> and <i>y</i> resulted in the information displayed in the table below.</p>'
    + tbl(['', '', ''], [['<b>Mean</b>', 'x̄ = 8', 'ȳ = 50.53'], ['<b>Standard deviation</b>', '<i>s<sub>x</sub></i> = 4.47', '<i>s<sub>y</sub></i> = 18.77'], ['<b>Correlation coefficient</b>', '<i>r</i> = 0.98', '']]).replace('<tr><th></th><th></th><th></th></tr>', '')
    + '<p class="q">Using this information, the equation of the least squares line in the form <i>y</i> = <i>a</i> + <i>bx</i> is</p>',
    ['<i>y</i> = −200.18 + 4.1<i>x</i>', '<i>y</i> = 48.66 + 0.23<i>x</i>', '<i>y</i> = 17.6 − 4.1<i>x</i>', '<i>y</i> = 4.1 + 17.6<i>x</i>', '<i>y</i> = 17.6 + 4.1<i>x</i>'],
    'E', 'b = 0.98 × 18.77 ÷ 4.47 = 4.1; a = 50.53 − 4.115 × 8 = 17.6'),
 MC(18, '3A', 18, '<p class="q">A scatterplot showing the relationship between variables is shown below.</p>[[g1q18]]<p class="q">The equation of the least squares regression line is best represented by</p>',
    ['<i>y</i> = 1.42 + 0.84<i>x</i>', '<i>y</i> = 1.42 − 0.84<i>x</i>', '<i>y</i> = 2.26 + 1.42<i>x</i>', '<i>y</i> = 0.84 − 2.26<i>x</i>', '<i>y</i> = 2.26 − 1.42<i>x</i>'],
    'A', 'Positive slope; the line rises about 0.84 per unit of x (e.g. from 3 at x = 3 to 7.3 at x = 8).'),
 MC(25, '3A', 19, CAFE + '<p class="q">The <i>y</i>-intercept, <i>a</i>, of the least squares line is best calculated by which one of the following?</p>',
    ['0.9453 × 2082.3 ÷ 35.4', '4595 − 55.60 × 82.4', '55.60 × 2082.3 ÷ 35.4', '0.9453 × 35.4 ÷ 2082.3', '82.4 − 55.60 × 4595'],
    'B', 'b = 0.9453 × 2082.3 ÷ 35.4 = 55.60, then a = ȳ − b x̄ = 4595 − 55.60 × 82.4', shared='Q23–25'),
 MC(29, '3A', 20, '<p class="q">The scatterplot below shows a least squares line fitted to a scatterplot.</p>[[g1q29]]'
    '<p class="q">The statistics for the set of data above are shown in the table below.</p>'
    + tbl(['x̄', 'ȳ', '<i>s<sub>x</sub></i>', '<i>s<sub>y</sub></i>', '<i>r</i>'], [['23.2', '12.8', '2.7', '0.46', '0.9351']])
    + '<p class="q">The equation of the least squares line is</p>',
    ['<i>y</i> = 5.5 − 114.5<i>x</i>', '<i>y</i> = 0.16 + 9.10<i>x</i>', '<i>y</i> = −114.5 + 5.5<i>x</i>', '<i>y</i> = 0.16 − 9.10<i>x</i>', '<i>y</i> = 9.10 + 0.16<i>x</i>'],
    'E', 'b = 0.9351 × 0.46 ÷ 2.7 = 0.16; a = 12.8 − 0.159 × 23.2 = 9.10'),
 # ---- 3B: interpreting, predicting, residuals
 MC(2, '3B', '12–13', EXAM + '<p class="q">Given the information above, which of the following statements is <b>not</b> true?</p>',
    ['The value of the coefficient of determination is close to 0.62', 'On average, as the number of hours studied increases by 1, the exam result increases by 5.7%.',
     '78.8% of the variation in exam result can be explained by the variation in number of hours studied.',
     'Ignoring any outliers, the association between number of hours studied and exam result can be described as strong, positive and linear.',
     'On average, when a student has studied for 0 hours in the week preceding their exam, they will receive an exam result of 36.8%.'],
    'C', 'r² = 0.7883² = 0.62, so 62% (not 78.8%) of the variation is explained.', shared='Q2–4'),
 MC(3, '3B', '12–13', EXAM + '<p class="q">Belinda studied for a total of 7.6 hours in the week preceding her exam and achieved an exam result of 75%. Using the least squares line, the residual value for Belinda’s exam result is closest to</p>',
    ['−389', '−5', '5', '80', '389'], 'B', 'Predicted = 36.8 + 5.7 × 7.6 = 80.1; residual = 75 − 80.1 = −5.1', shared='Q2–4'),
 MC(4, '3B', '12–13', EXAM + '<p class="q">Which of the following could be the residual plot for the relationship between number of hours studied and exam result scores?</p>',
    ['[[g1q4a]]', '[[g1q4b]]', '[[g1q4c]]', '[[g1q4d]]', '[[g1q4e]]'],
    'D', 'Residuals match the vertical distances from the line: the two points near 1 hour lie about 15 below it, the point at 2 hours (79%) about 30 above it.', shared='Q2–4'),
 MC(8, '3B', 15, TRIAL79 + '<p class="q">Which of the following statements is <b>incorrect</b>?</p>',
    ['On average, as <i>first trial exam</i> score increases by 1 mark, the <i>final trial exam</i> score decreases by 1.007 marks.',
     'A student who achieved a score of 0 marks on their <i>first trial exam</i> would achieve a score of approximately 5 marks on their <i>final trial exam</i>.',
     '83.85% of the variation in <i>final trial exam</i> score can be explained by the variation in <i>first trial exam</i> score.',
     'There is a strong, positive, linear relationship between <i>first trial exam</i> score and <i>final trial exam</i> score for this cohort of Year 12 students.',
     'On average, as <i>first trial exam</i> score increases by 1 mark, the <i>final trial exam</i> score increases by 1.007 marks.'],
    'A', 'The slope (1.007) is positive, so the final trial exam score increases, not decreases.', shared='Q7–9'),
 MC(10, '3B', 16, BABY + '<p class="q">Using the least squares line, the predicted value for <i>birth weight</i>, when <i>mother’s weight</i> is 60 kilograms, is approximately</p>',
    ['2.6', '3.2', '3.4', '3.6', '4.0'], 'A', 'Read up from 60 kg to the line, then across: about 2.6 kg.', shared='Q10–13'),
 MC(13, '3B', 16, BABY + '<p class="q">Using this least squares line to model the association between <i>mother’s weight</i> and <i>birth weight</i>, the residual value for a baby that is born to a mother weighing 92 kilograms is closest to</p>',
    ['−2.0 kg', '−1.0 kg', '−0.30 kg', '0.30 kg', '2.0 kg'], 'B', 'Predicted = −1.1203 + 0.063 × 92 = 4.7 kg; actual ≈ 3.7 kg; residual ≈ 3.7 − 4.7 = −1.0 kg', shared='Q10–13'),
 MC(19, '3B', 18, CAR + '<p class="q">Which one of the following statements is <b>not</b> true?</p>',
    ['The car was bought for $61&#8239;591 when it was new.', '99.78% of the variation in price can be explained by the variation in age.',
     'The car depreciates by $4164 for every additional year it ages.', 'There is a strong negative association between the car’s age and price.',
     'When the car is 10 years old, its price will be $19&#8239;951.'],
    'B', 'r² = (−0.9978)² = 0.9956, so 99.56% (not 99.78%) of the variation is explained.', shared='Q19–20'),
 MC(20, '3B', 18, CAR + '<p class="q">Jose paid $18&#8239;000 when the car was 12 years old.<br>The residual value is</p>',
    ['−$6377', '$6377', '−$11&#8239;623', '$11&#8239;623', '$18&#8239;000'], 'B', 'Predicted = 61&#8239;591 − 4164 × 12 = 11&#8239;623; residual = 18&#8239;000 − 11&#8239;623 = $6377', shared='Q19–20'),
 MC(23, '3B', 19, CAFE + '<p class="q">Using the least squares line, when the revenue is at least $200 higher than predicted, the staff receive a small bonus.</p><p class="q">How many days did staff receive a bonus over the ten days?</p>',
    ['1', '2', '3', '4', '5'], 'C', 'The line gives the predicted revenue: 3 points lie at least $200 above it.', shared='Q23–25'),
 MC(30, '3B', 21, POOL + '<p class="q">The residual plot that matches the data is</p>',
    ['[[g1q30a]]', '[[g1q30b]]', '[[g1q30c]]', '[[g1q30d]]', '[[g1q30e]]'],
    'C', 'Least squares line: visitors = −85.9 + 10.84 × temperature. Residuals: 17 °C → −35, −45; 18 → −32; 23 → 48; 24 → 31; 27 → 87; 31 → 62; 32 → −1; 33 → −39; 38 → −75.'),
]

def SA(n, sub, page, stem_, parts, why=None, note=None, long=False):
    return dict(long=long, kind='sa', n=n, sub=sub, marks=sum(p[4] for p in parts), stem=stem_, parts=parts, why=why, note=note, src=f'{G2} p.{page} Q{n}')

_TS, _NP = [15, 35, 45, 12, 8, 18, 12, 34, 40, 38, 19, 20, 36, ''], [12, 27, 38, 8, 6, 22, 15, 28, 46, 32, 25, 23, 33, 23]
PAGES = ('<p class="q">The data from the scatterplot is shown in the table below.</p>' + ''.join(
    '<table class="t sm"><tr><th><i>Time spent reading</i> (minutes)</th>' + ''.join(f'<td>{v}</td>' for v in _TS[k:k + 7]) + '</tr>'
    '<tr><th><i>Number of pages read</i></th>' + ''.join(f'<td>{v}</td>' for v in _NP[k:k + 7]) + '</tr></table>' for k in (0, 7)))  # same data, two rows of 7
DONE2 = 'Insight’s other parts of this question are in the Chapter 2 booklet.'

Q += [
 # ---- 3A
 SA(10, '3A', 25, '<p class="q">A research study is conducted on 2300 babies from birth until they are 12 months old. Of these babies, 1100 were girls and 1200 were boys.</p>'
    '<p class="q">The data on the weight of the babies at six months of age for both boys and girls is shown below.</p>'
    + tbl(['<i>Weight at six months</i> (kg)', 'Min.', '<i>Q</i><sub>1</sub>', 'Median', '<i>Q</i><sub>3</sub>', 'Max.'], [['girls', '6.7', '7.0', '7.3', '7.7', '8.2'], ['boys', '6.8', '7.7', '7.9', '8.2', '8.8']])
    + '[[g2q10]]<p class="q">It is found that the average weight for boys at birth is 3.25 kg and at 12 months is 9.49 kg. The Pearson correlation coefficient is 0.9364.</p>'
    '<p class="q">A least squares line is fitted to the data.</p>',
    [('a', 'What percentage of the variation in weight can be explained by the variation in age?<br>Round your answer to one decimal place.', '<i>r</i>² = 0.9364² = 0.8768 → 87.7%', 8, 1),
     ('b', 'Write the equation of the least squares line below, using the variables <i>age</i> and <i>weight</i>.',
      'Intercept = weight at age 0 = 3.25; slope = (9.49 − 3.25) ÷ (12 − 0) = 0.52<br><i>weight</i> = 3.25 + 0.52 × <i>age</i>', 14, 2)]),
 SA(7, '3A', 21, '<p class="q">The maximum daily temperature (°C) and number of patrons attending the gym on the first 12 days of April 2019 are shown in Table 1 below.</p>'
    '<p class="q" style="text-align:center"><b>Table 1</b></p>' + GYM
    + '<p class="q">A least squares line is to be fitted to the data, using the maximum daily temperature as the explanatory variable.</p>',
    [('b', 'Determine the equation of this least squares line.<br>Round the values for the slope and intercept to three significant figures.',
      'CAS (x = maximum daily temperature, y = number of patrons): <i>number of patrons</i> = 291 − 5.84 × <i>maximum daily temperature</i>', 12, 1)],
    note='Part b. ' + DONE2),
 SA(2, '3A', '14–16', '<p class="q">A small group of train travellers were surveyed on the morning train. Those who specified that they were in the 18–24 years age group were also asked what their <i>hourly pay rate</i> was, with the intention of identifying an association between <i>hours worked</i> and <i>hourly pay rate</i>.</p>'
    '<p class="q">The data are shown in the table below and are also displayed as a scatterplot.</p>' + PAY + '[[g2q2]]',
    [('c', 'Determine the equation of the least squares regression line that can be used to predict the number of <i>hours worked</i> from the <i>hourly pay rate</i>.<br>Round the values for the slope and intercept to two significant figures.',
      'CAS: <i>hours worked</i> = −4.857… + 1.004… × <i>hourly pay rate</i> → <i>hours worked</i> = −4.9 + 1.0 × <i>hourly pay rate</i>', 12, 2),
     ('d', 'Interpret the <b>slope</b> of the least squares regression line in terms of the variables <i>hourly pay rate</i> and <i>hours worked</i>.',
      'On average, as the hourly pay rate increases by one dollar, the number of hours worked increases by one hour.', 10, 1),
     ('e', 'The value of the coefficient of determination for the association between the variables <i>hourly pay rate</i> and <i>hours worked</i> is 0.5159.<br>Interpret the coefficient of determination in terms of these variables.',
      '51.59% of the variation in hours worked can be explained by the variation in hourly pay rate.', 10, 1),
     ('f', 'A residual plot was obtained when the least squares regression line was fitted to the data. This is shown below.[[g2q2r]]'
      '<b>i.</b> Does the residual plot support the assumption that there is a linear association between <i>hourly pay rate</i> and <i>hours worked</i>?<br>Explain your answer.',
      'Yes: the residual plot shows no clear pattern (random scatter), so it supports the assumption of linearity.', 10, 2),
     ('f ii', 'Find the residual value for a train passenger who is paid $25.00 per hour, and works 17 hours in a week.<br>Round your answer to one decimal place.',
      'Predicted = −4.9 + 1.0 × 25 = 20.1; residual = 17 − 20.1 = −3.1', 10, 1)],
    note='Parts c–f. ' + DONE2),
 # ---- 3B
 SA(4, '3B', '17–18', '<p class="q">The teacher became concerned about the amount of homework her students were completing, and so began an investigation into the association between <i>hours of homework per week</i> and the <i>distance from school</i> for her students. A scatterplot of the data that the teacher gathered is shown below.</p>[[g2q4]]'
    '<p class="q">The equation of the least squares regression line is</p><p class="q" style="text-align:center"><i>hours of homework per week</i> = 7.46 − 0.0977 × <i>distance from school</i></p>',
    [('a', 'On the scatterplot above, draw the least squares regression line.', 'Line through (0, 7.46) and (30, 4.53) (drawn with a ruler).', 4, 2),
     ('c', 'Interpret the slope of the regression line in terms of the variables <i>hours of homework per week</i> and <i>distance from school</i>.',
      'On average, as the distance from school increases by one kilometre, the hours of homework per week decrease by 0.0977 hours.', 10, 1),
     ('e', 'The <i>hours of homework per week</i> is 3 when the <i>distance from school</i> is 8 km.<br>Determine the residual value if the least squares line is used to predict the hours of homework per week for this distance. Round your answer to two decimal places.',
      'Predicted = 7.46 − 0.0977 × 8 = 6.6784; residual = 3 − 6.6784 = −3.68', 10, 1),
     ('f i', 'The teacher has a new student in her class who lives 11 kilometres away from school.<br>Predict the number of hours of homework per week that this student can complete, correct to one decimal place.',
      '7.46 − 0.0977 × 11 = 6.3853 → 6.4 hours', 8, 1),
     ('f ii', 'Explain why this is an appropriate prediction.', 'It is interpolation: 11 km is within the range of the data.', 8, 1)],
    note='Parts a, c, e and f. ' + DONE2),
 SA(5, '3B', '18–19', '<p class="q">During October 2018, there was only one scheduled flight between Melbourne and Darwin per day.</p>'
    '<p class="q">The minutes delayed and the wind speed (km/h) at 9 am in Melbourne for each day in October are plotted on the scatterplot below.</p>[[g2q5]]'
    '<p class="q">A least squares line is to be fitted to the data with the aim of predicting the number of minutes delayed from the wind speed on a particular day in Melbourne.</p>'
    '<p class="q">The equation of this line is</p><p class="q"><i>minutes delayed</i> = −10.745 + 18.051 × <i>wind speed</i></p>',
    [('b', 'Interpret the slope of the least squares regression line in terms of the variables <i>wind speed</i> and <i>minutes delayed</i>.',
      'As the wind speed increases by one kilometre per hour, the minutes delayed can be expected to increase by 18.051 minutes, on average.', 10, 1),
     ('c', 'Draw the line for the least squares regression equation on the scatterplot.<br><i>(Answer on the scatterplot.)</i>', 'Line through (1, 7) and (25, 441) (drawn with a ruler).', 4, 1),
     ('d', 'Using the equation of the least squares regression line, show that the number of minutes delayed is 242 minutes when wind speed is 14 km/h.',
      '−10.745 + 18.051 × 14 = 241.969 ≈ 242 minutes', 10, 2),
     ('e', 'On a particular day in October, the wind speed was 15 km/h and the flight from Melbourne to Darwin was delayed by 196 minutes.<br>Determine the residual value when the equation of the least squares line is used to predict the minutes delayed when the wind speed is 15 km/h.<br>Round your answer to one decimal place.',
      'Predicted = −10.745 + 18.051 × 15 = 260.0; residual = 196 − 260.0 = −64.0', 12, 2)],
    note='Parts b–e. ' + DONE2),
 SA(11, '3B', 26, '<p class="q">The average amount of rainfall and the average growth in a crop of plants is recorded for ten weeks.</p>[[g2q11]]'
    + ''.join(tbl(['Week'] + [str(i) for i in range(k + 1, k + 6)], [['<b><i>rainfall</i> (mm)</b>'] + [70, 15, 80, 120, 150, 135, 10, 0, 25, 0][k:k + 5], ['<b><i>average growth</i> (mm)</b>'] + [14, 13, 30, 46, 48, 33, 9, 7, 18, 8][k:k + 5]], 't sm') for k in (0, 5))  # same data, two rows of 5
    + '<p class="q">The equation of the least squares line for the data shown is</p><p class="q" style="text-align:center"><i>average growth</i> = 7.6 + 0.25 × <i>rainfall</i></p>',
    [('a', 'Determine the residual for a day when the average amount of rainfall was 10 mm.', 'Predicted = 7.6 + 0.25 × 10 = 10.1; actual = 9 (week 7); residual = 9 − 10.1 = −1.1', 12, 2),
     ('b', 'Explain what a residual of 3.2 means in the context of this scenario.', 'The actual growth of the crop was 3.2 mm more than the growth predicted by the least squares line.', 8, 1),
     ('c', 'Interpret the intercept of the least squares line in terms of the variables <i>average growth</i> and <i>rainfall</i>.', 'On average, when the rainfall is 0 mm, the average growth is 7.6 mm.', 8, 1)]),
 SA(14, '3B', '30–31', '<p class="q">Farah reads novels during her lunch and rest breaks. The amount of <i>time spent reading</i> by Farah, in minutes, and the <i>number of pages read</i> is shown on the scatterplot below.</p>[[g2q14]]'
    '<p class="q">A least squares line is fitted to the scatterplot. The equation of this line is</p><p class="q" style="text-align:center"><i>number of pages read</i> = 2.44 + 0.85 × <i>time spent reading</i></p>',
    [('a', 'Interpret the slope of the least squares line in terms of the <i>number of pages read</i> and <i>time spent reading</i>.', 'For every extra 1 minute spent reading, 0.85 more pages are read (on average).', 8, 1),
     ('b', PAGES + 'A value is missing from the table and the scatterplot. The corresponding residual for this value is −0.69<br>Determine the missing value.',
      'residual = actual − predicted: −0.69 = 23 − predicted → predicted = 23.69<br>23.69 = 2.44 + 0.85 × <i>time</i> → <i>time</i> = 25 minutes', 14, 2)],
    note='Parts a and b. ' + DONE2),
 # ---- 3C: a full regression analysis
 SA(8, '3C', '22–23', '<p class="q">The scatterplot below shows the <i>number of participants</i> in the morning weights class plotted against the <i>predicted maximum daily temperature</i> (°C) on each day during February 2020.</p>[[g2q8]]'
    '<p class="q">A least squares equation has been fitted to the scatterplot.</p><p class="q">The least squares equation is</p>'
    '<p class="q" style="text-align:center"><i>number of participants</i> = −0.7296 + 1.077 × <i>predicted maximum temperature</i></p>',
    [('a', 'On the scatterplot above, sketch the least squares line using the equation given.', 'Line through (6, 5.7) and (23, 24.0).', 3, 1),
     ('b', 'Interpret the slope of this least squares line in terms of the <i>predicted maximum temperature</i> and the <i>number of participants</i>.',
      'On average, for every 1 °C increase in the predicted maximum temperature, the number of participants increases by 1.077.', 6, 1),
     ('c', 'Use the equation of the least squares line to find the <i>predicted maximum temperature</i> when the <i>number of participants</i> is 20.<br>Round your answer to the nearest degree.',
      '20 = −0.7296 + 1.077 × <i>x</i> → <i>x</i> = 19.2 → 19 °C', 5, 1),
     ('d', 'Show that the residual value is −7 when the <i>predicted maximum temperature</i> is 18 °C.',
      'Actual (from the scatterplot) = 12; predicted = −0.7296 + 1.077 × 18 = 18.66 ≈ 19; residual = 12 − 19 = −7', 6, 1),
     ('e', 'The value of the coefficient of determination for the relationship between the <i>predicted maximum temperature</i> and the <i>predicted number of participants</i> is 0.4143.<br>Determine the value of the correlation coefficient, <i>r</i>.<br>Round your answer to two decimal places.',
      '<i>r</i> = √0.4143 = 0.64 (positive slope)', 4, 1),
     ('f', 'The mean for <i>predicted maximum temperature</i> is 14.97 °C.<br>Show that the mean for the <i>number of participants</i>, rounded to one decimal place, is 15.4 °C.',
      '<i>a</i> = ȳ − <i>b</i>x̄: −0.7296 = ȳ − 1.077 × 14.97 → ȳ = 15.39 → 15.4', 6, 1),
     ('g', 'The residual plot associated with the least squares line is shown below.[[g2q8r]]'
      '<b>i.</b> Using the equation for the least squares line and the scatterplot for the relationship, complete the residual plot for a <i>predicted maximum temperature</i> of 8 °C and 21 °C.',
      '8 °C: 10 − 7.89 = +2.1; 21 °C: 25 − 21.89 = +3.1 (plotted at (8, 2.1) and (21, 3.1)).', 3, 1),
     ('g ii', 'Does the residual plot confirm the assumption of linearity for the relationship between the <i>predicted maximum temperature</i> and the <i>predicted number of participants</i>?<br>Give a reason for your answer.',
      'Yes: the residual plot shows no clear pattern (the points are randomly scattered), so it confirms the assumption of linearity.', 5, 1)], long=True),
]

SUBS = [('3A', 'Least squares regression line'), ('3B', 'Performing a regression analysis'),
        ('3C', 'Conducting a regression analysis using raw data')]
