"""Lesson l10 (3B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l10/build.py
(Do Now is not on the worksheet, as in l07/l09).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1-2 = Cambridge U1&2 Ch 7 checklist 7E #9, #10 (data 7A #2; solutions worked for 12MAG); APK 3 = VCAA 2018 Exam 1 Q8 (= Edrolo U1&2 6D Q12);
APK 4 = VCAA 2019 Exam 2 Q5a (= Edrolo U1&2 6D Q13).
Examples 3-5 = Cambridge U3&4 pp. 181-184. You trys: Edrolo U3&4 3B WE1 (pp. 169-170), WE2 (p. 171); YT-3B-5 (written for 12MAG).
Exits = Edrolo U3&4 3B Q11 (adapted from VCAA 2019 Exam 2 Q5c), Q12 (VCAA 2018 Exam 2 Q2c), Q13 (VCAA 2017 Exam 2 Q3bii).
Output: lessons/3B worksheet(.html/.pdf) + lessons/3B worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l10/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#000', tl_hid=False, **k) + '</div>'
PL = ((1010.4, 111.4 + 0.8894 * 1010.4), (1030, 111.4 + 0.8894 * 1030))
fa, fb = lsq([p[0] for p in FOOT], [p[1] for p in FOOT])

P = [title('3B', 'Using the least squares regression line to model a relationship')]
P.append(lis(['To be able to interpret the intercept and slope of the least squares line.', 'To be able to use the equation of the least squares line to make predictions.',
              'To be able to use the coefficient of determination in a regression analysis.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Height (<i>height</i>) and foot length (<i>foot length</i>) of 16 students, in centimetres:')
  + T([['<b>height</b>'] + [h for h, _ in FOOT], ['<b>foot length</b>'] + [f for _, f in FOOT]])
  + q(f'Least squares line: <i>foot length</i> = {fa:.2f} + {fb:.2f} × <i>height</i>')
  + q('Interpret the intercept and slope of the regression line relating height and foot length in terms of these variables.')
  + space(18, f'Slope: on average, foot length increases by {fb:.2f} cm for each 1 cm increase in height.<br>Intercept: on average, a person of height 0 cm would have a foot length of {fa:.2f} cm: no practical meaning (0 cm is far outside the data).')))
P.append(box('Question 2', q(f'Use the linear model line relating height and foot length to predict the foot length of people with the following heights, indicating in each whether you are interpolating or extrapolating. Give your answers rounded to one decimal place.')
  + parts([('a', '160 cm tall', f'{fa+fb*160:.1f} cm, interpolating (160 is inside 153–185)', 10), ('b', '100 cm tall', f'{fa+fb*100:.1f} cm, extrapolating (100 is outside 153–185)', 10)])))
P.append(box('Question 3 · VCAA 2018 Exam 1 Q8', q('The scatterplot below displays the <i>resting pulse rate</i>, in beats per minute, and the <i>time spent exercising</i>, in hours per week, of 16 students. A least squares line has been fitted to the data.')
  + SP(PULSE, (1, 11), (56, 68), 1, 1, 'time spent exercising (hours per week)', 'resting pulse rate', 52, tl=((1, 67.2), (11, 56.2)))
  + q('The equation of this least squares line is closest to')
  + mc(['<i>resting pulse rate</i> = 67.2 – 0.91 × <i>time spent exercising</i>', '<i>resting pulse rate</i> = 67.2 – 1.10 × <i>time spent exercising</i>', '<i>resting pulse rate</i> = 68.3 – 0.91 × <i>time spent exercising</i>',
        '<i>resting pulse rate</i> = 68.3 – 1.10 × <i>time spent exercising</i>', '<i>resting pulse rate</i> = 67.2 + 1.10 × <i>time spent exercising</i>'], 'D')
  + why('slope = −11 ÷ 10 = −1.10; the axis starts at 1, so the intercept is 67.2 + 1.10 = 68.3'), '1 mark'))
P.append(box('Question 4 · VCAA 2019 Exam 2 Q5a', q('The scatterplot below shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<i>pressure 3 pm</i>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<i>pressure 9 am</i>) for 23 days in November 2017 at a particular weather station.')
  + SP(PRESS, (1010, 1030), (1010, 1030), 5, 5, 'pressure 9 am (hPa)', 'pressure 3 pm (hPa)', 48, tl=PL)
  + q('A least squares line has been fitted to the scatterplot as shown.<br>The equation of this line is &nbsp; <i>pressure 3 pm</i> = 111.4 + 0.8894 × <i>pressure 9 am</i>')
  + q('a. Interpret the slope of this least squares line in terms of the atmospheric pressure at this weather station at 9 am and at 3 pm.')
  + space(14, 'On average, pressure at 3 pm increases by 0.8894 hPa for each one unit (hPa) increase in pressure at 9 am.'), '1 mark'))
# ---------------------------------------------------------------- 3B
P.append(sect('3B Using the least squares regression line', 'Example, then you try'))
P.append(exyt('Example 3 · Interpreting the slope and intercept',
  q('The equation of a regression line that enables the price of a second-hand car to be predicted from its age is:<br><i>price</i> = 35 100 − 3940 × <i>age</i>')
  + q('a Interpret the slope in terms of the variables price and age.') + q('On average, for each additional year of age the price of these cars ' + a('decreases by $3940') + '.')
  + q('b Interpret the intercept in terms of the variables price and age.') + q('On average, the price of these cars ' + a('when new was $35 100') + '.'),
  'You try 3', q('The heights of a group of children aged between one and six years old were measured. The scatterplot and regression equation show the relationship between <i>height</i> (cm) and <i>age</i> (years).')
  + SP(KIDS, (0, 7), (50, 130), 1, 10, 'age (years)', 'height (cm)', 52, tl=((0, 58.22), (6.9, 58.22 + 10.46 * 6.9)))
  + q('Based on the regression equation, <i>height</i> = 58.22 + 10.46 × <i>age</i>')
  + parts([('a', 'How much on average does a child grow each year, correct to two decimal places?', 'On average, a child grows 10.46 cm each year.', 12),
           ('b', 'Interpret the <i>y</i>-intercept in this regression equation.', 'On average, the height of children when they are born is 58.22 cm.', 12)])))
P.append(exyt('Example 4 · Using the regression line to make predictions',
  q('The equation of a regression line that enables the price of a second-hand car to be predicted from its age is:<br><i>price</i> = 35 100 − 3940 × <i>age</i>')
  + q('Use this equation to predict the price of a car that is 5.5 years old.')
  + q('<i>price</i> = 35 100 − 3940 × ' + a('5.5')) + q('= ' + a('$13 430')),
  'You try 4', q('A ski hire shop has recorded the daily <i>snowfall</i> (cm) and the corresponding <i>number of customers</i> that hire from them. The relationship between <i>number of customers</i> and <i>snowfall</i> is displayed on the scatterplot.')
  + SP(SKI, (0, 10), (0, 90), 1, 10, 'snowfall (cm)', 'number of customers', 52, tl=((0, 14), (10, 87)))
  + parts([('a', 'What is the predicted <i>number of customers</i> when there is 5 cm of <i>snowfall</i>? Is this interpolation or extrapolation?', '50 customers; interpolation (5 cm is inside 1–9 cm)', 12),
           ('b', 'How many customers are expected to hire from the ski hire shop when there is no snowfall?', 'About 14 customers (the y-intercept)', 10)])))
P.append(exyt('Example 5 · Using r² to compare associations',
  q('In a recent study across a number of countries the correlation between educational attainment and the amount spent on education was found to be 0.26, whilst the correlation between educational attainment and the student : teacher ratio was found to be −0.38.')
  + q('a Find the values of the coefficient of determination between educational attainment and the amount spent on education, and student : teacher ratio respectively.')
  + q('amount spent: <i>r</i>² = ' + a('0.26² = 6.8%') + ' &nbsp; student : teacher ratio: <i>r</i>² = ' + a('(−0.38)² = 14.4%'))
  + q('b Which of the variables, amount spent on education or student : teacher ratio is more important in explaining the variation in educational attainment?')
  + q(a('Student : teacher ratio') + ': it explains ' + a('14.4%') + ' of the variation in educational attainment, compared with only ' + a('6.8%') + '.'),
  'You try 5', q('In a recent study of a group of schools the correlation between Year 12 study score and hours of paid work per week was found to be −0.45, whilst the correlation between Year 12 study score and hours of sleep per night was found to be 0.31.')
  + parts([('a', 'Find the values of the coefficient of determination between Year 12 study score and hours of paid work per week, and hours of sleep per night respectively.', 'paid work: (−0.45)² = 20.3% · sleep: 0.31² = 9.6%', 14),
           ('b', 'Which of the variables, hours of paid work per week or hours of sleep per night, is more important in explaining the variation in Year 12 study score?', 'Hours of paid work per week: it explains 20.3% of the variation, compared with 9.6%.', 14)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 2 Q5c (adapted)', q('The scatterplot provided shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<i>pressure 3 pm</i>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<i>pressure 9 am</i>) for 23 days in November 2017 at a particular weather station. A least squares line has been fitted to the scatterplot as shown.')
  + SP(PRESS, (1010, 1030), (1010, 1030), 5, 5, 'pressure 9 am (hPa)', 'pressure 3 pm (hPa)', 48, tl=PL)
  + q('The equation of this line is <i>pressure 3 pm</i> = 111.4 + 0.8894 × <i>pressure 9 am</i><br>The equation of the least squares line is used to predict the atmospheric pressure at 3 pm when the atmospheric pressure at 9 am is 1025 hPa.<br>Is this prediction an example of extrapolation or interpolation?')
  + space(10, 'Interpolation: 1025 hPa is within the range of the pressure 9 am data (about 1013–1027 hPa).'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2018 Exam 2 Q2c', q('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods). This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.')
  + SP(CONG, (35, 70), (35, 75), 5, 5, 'morning congestion level (%)', 'evening congestion level (%)', 48)
  + q('A least squares line is to be fitted to the data with the aim of predicting evening congestion level from morning congestion level.<br>The equation of this line is &nbsp; <i>evening congestion level</i> = 8.48 + 0.922 × <i>morning congestion level</i>')
  + q('c. Use the equation of the least squares line to predict the evening congestion level when the morning congestion level is 60%.')
  + space(10, '8.48 + 0.922 × 60 = 63.8%'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2017 Exam 2 Q3bii', q('The <i>number of female moths</i> caught in a trap set in a forest and the <i>egg density</i> (eggs per square metre) in the forest can also be examined. A scatterplot of the data is shown below.')
  + SP(FEM, (10, 60), (0, 2500), 5, 500, 'number of female moths', 'egg density', 48)
  + q('The equation of the least squares line is <i>egg density</i> = 191 + 31.3 × <i>number of female moths</i>')
  + q('ii. Interpret the slope of the regression line in terms of the variables egg density and number of female moths caught in the trap.')
  + space(14, 'On average, egg density increases by 31.3 eggs/m² for each additional female moth caught.'), '1 mark'))
SC = ['I can interpret the slope and intercept of a regression line.', 'I can use the regression line to make predictions.', 'I can use the coefficient of determination to compare associations.']
P.append(close(SC, [('3B', 'Q1–7')], ['3B']))
build('l10', '3B', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l10-worksheet', '3B worksheet'), ('l10-worksheet-solutions', '3B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
