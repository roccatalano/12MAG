"""Lesson l09 (3A) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l09/build.py
(Do Now and CFAT are not on the worksheet, as in l07).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 7 checklist 7D #8 (data 7A #2; solution worked for 12MAG); APK 2 = Cambridge U1&2 Ch 5 checklist 5E #7;
APK 3 = Edrolo U1&2 6C Q11 (adapted from VCAA 2017 Exam 2 Q4cii); APK 4 = VCAA 2021 Exam 2 Q3eii (= Edrolo U1&2 6C Q12; original wording, stem shortened).
Examples 1-2 = Cambridge U3&4 pp. 171-173. You trys: Edrolo U3&4 3A WE3 (p. 161); YT-3A-2 (written for 12MAG); CAS You try = Edrolo 3A WE1 (p. 157).
Exits = Edrolo U3&4 3A Q13 (VCAA 2018 Exam 1 Q13), Q14 (VCAA 2021 Exam 1 Q11), Q15 (VCAA 2017 Exam 2 Q3a, bi).
Output: lessons/3A worksheet(.html/.pdf) + lessons/3A worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l09/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def ST(cols, rows): return table([[''] + cols] + [list(r) for r in rows], cls='t')
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#000', tl_hid=False, **k) + '</div>'

P = [title('3A', 'Fitting a least squares regression line')]
P.append(lis(['To be able to define linear regression.', 'To be able to define a residual.', 'To introduce the least squares line of best fit.',
              'To be able to find the equation of the least squares line using summary statistics.', 'To be able to find the equation of the least squares line using technology.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
fa_, fb_ = lsq([p[0] for p in FOOT], [p[1] for p in FOOT])
P.append(box('Question 1', q('In order to predict the length of a person’s foot from their height, a group of 16 students collected the following data set, which gives height (<i>height</i>) and the length of their foot (<i>foot length</i>) in centimetres.')
  + T([['<b>height</b>'] + [h for h, _ in FOOT], ['<b>foot length</b>'] + [f for _, f in FOOT]])
  + q('Find the equation of the least squares line which would enable foot length to be predicted from height. Give the values of the intercept and slope, rounded to two decimal places.')
  + space(12, f'EV height, RV foot length. foot length = {fa_:.2f} + {fb_:.2f} × height')))
P.append(box('Question 2', q('Find the slope of the line that goes through the points (1, 8) and (4, 2).') + space(10, 'slope = (2 − 8) ÷ (4 − 1) = −6 ÷ 3 = −2')))
P.append(box('Question 3 · VCAA 2017 Exam 2 Q4cii (adapted)', q('A large colony of ants grows in size each year. The association between the <i>population</i> of the colony and <i>year</i> is approximately linear. The data is shown in the following table.')
  + T([['<b>year</b>'] + list(range(2014, 2023)), ['<b>population (mil)</b>', '18.2', '19.0', '19.9', '20.8', '22.0', '22.8', '23.2', '23.8', '25.3']])
  + q('The line of good fit predicts that the population of the ant colony by the year 2026 will be approximately 28.5 million.<br>Give a reason why this prediction may have limited reliability.')
  + space(12, 'Extrapolation: 2026 is beyond the range of the data (2014–2022).'), '1 mark'))
P.append(box('Question 4 · VCAA 2021 Exam 2 Q3eii', q('Data on the winning time, in seconds, for the women’s 100 m freestyle swim, for each year that the Olympic Games were held during the period 1956 to 2016, was used to model the decreasing trend in the winning time over this period.')
  + q('e. The following equation can be used to predict the winning time for the women’s 100 m freestyle in the future.<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>winning time</i> = 357.1 – 0.1515 × <i>year</i>')
  + q('ii. What assumption is being made when this equation is used to predict the winning time for the women’s 100 m freestyle in 2032?')
  + space(12, 'The same decreasing trend continues in the future.'), '1 mark'))
# ---------------------------------------------------------------- 3A
P.append(sect('3A Fitting a least squares regression line', 'Example, then you try'))
P.append(exyt('Example 1 · Least squares line from summary statistics',
  q('The height and weight of 11 people have been recorded, and the values of the following statistics determined:')
  + ST(['height', 'weight'], [('mean', '173.3 cm', '65.45 kg'), ('standard deviation', '7.444 cm', '7.594 kg')]) + q('correlation coefficient <i>r</i> = 0.8502')
  + q('Use the formula to determine the equation of the least squares regression line that enables weight to be predicted from height. Calculate the values of the slope and intercept rounded to two decimal places.')
  + q('EV: ' + a('height (x)') + ' &nbsp; RV: ' + a('weight (y)'))
  + q('<i>b</i> = <i>r s<sub>y</sub></i> / <i>s<sub>x</sub></i> = ' + a('0.8502 × 7.594 ÷ 7.444 = 0.87'))
  + q('<i>a</i> = <i>ȳ</i> − <i>b x̄</i> = ' + a('65.45 − 0.8673… × 173.3 = −84.86'))
  + q('<i>weight</i> = ' + a('−84.86') + ' + ' + a('0.87') + ' × <i>height</i>'),
  'You try 1', q('Consider the following summary statistics for a set of bivariate data involving the variables <i>x</i> and <i>y</i>.<br><i>r</i> = 0.845, <i>x̄</i> = 11.0, <i>ȳ</i> = 29.2, <i>s<sub>x</sub></i> = 6.06, <i>s<sub>y</sub></i> = 16.8')
  + q('Find the equation of the least squares regression line that allows <i>y</i> to be predicted from <i>x</i>. Give all values correct to three significant figures.')
  + space(40, 'b = 0.845 × 16.8 ÷ 6.06 = 2.342…<br>a = 29.2 − 2.342… × 11.0 = 3.431…<br>y = 3.43 + 2.34x')))
P.append(exyt('Example 2 · The correlation coefficient from the slope',
  q('Use the following information to find the value of the correlation coefficient <i>r</i>, rounded to three decimal places.')
  + ST(['hours studied', 'exam score'], [('mean', '5.87', '68.3'), ('standard deviation', '1.34', '5.42')]) + q('least squares equation: <i>exam score</i> = 52.7 + 2.45 × <i>hours studied</i>')
  + q('EV: ' + a('hours studied (x)') + ' &nbsp; RV: ' + a('exam score (y)'))
  + q('<i>r</i> = <i>b s<sub>x</sub></i> / <i>s<sub>y</sub></i> = ' + a('2.45 × 1.34 ÷ 5.42 = 0.606')),
  'You try 2', q('Use the following information to find the value of the correlation coefficient <i>r</i>, rounded to three decimal places.')
  + ST(['hours of sleep', 'reaction test score'], [('mean', '7.42', '61.8'), ('standard deviation', '2.05', '9.42')]) + q('least squares equation: <i>reaction test score</i> = 38.2 + 3.18 × <i>hours of sleep</i>')
  + space(18, 'EV hours of sleep, RV reaction test score. r = 3.18 × 2.05 ÷ 9.42 = 0.692')))
P.append(box('You try 3 · CAS', q('The following table gives the heights, in cm, of fathers and their sons when they were the same age.')
  + T([['<b>height of father (cm)</b>'] + FATH, ['<b>height of son (cm)</b>'] + SON])
  + q('Determine the equation of the least squares regression line that will allow the <i>height of son</i> to be predicted from the <i>height of father</i>. Give values correct to three significant figures.')
  + space(12, 'height of son = 23.2 + 0.857 × height of father')))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q13', q('The statistical analysis of a set of bivariate data involving variables <i>x</i> and <i>y</i> resulted in the information displayed in the table below.')
  + table([['Mean', '<i>x̄</i> = 27.8', '<i>ȳ</i> = 33.4'], ['Standard deviation', '<i>s<sub>x</sub></i> = 2.33', '<i>s<sub>y</sub></i> = 3.24'], ['Equation of the least squares line', '<i>y</i> = –2.84 + 1.31<i>x</i>', '']], head=False)
  + q('Using this information, the value of the correlation coefficient <i>r</i> for this set of bivariate data is closest to')
  + mc(['0.88', '0.89', '0.92', '0.94', '0.97'], 'D', 5) + why('r = b s<sub>x</sub> / s<sub>y</sub> = 1.31 × 2.33 ÷ 3.24 = 0.942'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q11', q('The table below shows the weight, in kilograms, and the height, in centimetres, of 10 adults.')
  + T([['<b>Weight (kg)</b>'] + WT, ['<b>Height (cm)</b>'] + HTC])
  + q('A least squares line is fitted to the data.<br>The least squares line enables an adult’s weight to be predicted from their height.<br>The number of times that the predicted value of an adult’s weight is greater than the actual value of their weight is')
  + mc(['3', '4', '5', '6', '7'], 'D', 5) + why('weight = −83.5 + 0.842 × height; 6 points lie below the line (predicted &gt; actual).'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2017 Exam 2 Q3a, bi', q('The <i>number of male moths</i> caught in a trap set in a forest and the <i>egg density</i> (eggs per square metre) in the forest are shown in the table below.')
  + T([['<b>Number of male moths</b>'] + MALE, ['<b>Egg density (eggs per m²)</b>'] + EGG])
  + parts([('a', 'Determine the equation of the least squares line that can be used to predict the <i>egg density</i> in the forest from the <i>number of male moths</i> caught in the trap. Round your answers to one decimal place.<br><i>egg density</i> = ______ + ______ × <i>number of male moths</i> (2 marks)', 'egg density = −46.8 + 18.9 × number of male moths', 10),
           ('b', 'The <i>number of female moths</i> caught in a trap set in a forest and the <i>egg density</i> (eggs per square metre) in the forest can also be examined. A scatterplot of the data is shown below.<br>The equation of the least squares line is <i>egg density</i> = 191 + 31.3 × <i>number of female moths</i><br>i. Draw the graph of this least squares line on the scatterplot below. (1 mark)'
            + SP(FEM, (10, 60), (0, 2500), 5, 500, 'number of female moths', 'egg density', 70, tl=None), 'Line through (10, 504) and (60, 2069).' + SP(FEM, (10, 60), (0, 2500), 5, 500, '', '', 60, tl=((10, 504), (60, 2069))), 40)]), '3 marks'))
SC = ['I can determine the equation of the least squares regression line using the formulas.', 'I can determine the correlation coefficient from the slope of the least squares regression line using the formula.',
      'I can determine the equation of the least squares regression line using a CAS calculator.']
P.append(close(SC, [('3A', 'Q1–16')], ['3A']))
build('l09', '3A', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l09-worksheet', '3A worksheet'), ('l09-worksheet-solutions', '3A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
