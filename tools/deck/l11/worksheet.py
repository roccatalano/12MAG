"""Lesson l11 (3C) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l11/build.py
(Do Now is not on the worksheet, as in l07/l09/l10).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1-2 = Cambridge U1&2 Ch 5 checklist 5A #1, 5E #8 (answers p. 820); APK 3 = VCAA 2017 Exam 1 Q8 (= Edrolo U1&2 6D Q14, original wording);
APK 4 = VCAA 2016 Exam 2 Q3bii (Edrolo U1&2 6D Q15 adapted wording).
Examples 6-8 = Cambridge U3&4 pp. 184-188. You trys: Edrolo U3&4 3C WE2 (pp. 181-183), WE3 (p. 185); YT-3B-8 (written for 12MAG).
Exits = Edrolo U3&4 3C Q11 (VCAA 2018 Exam 2 Q2e), Q13 (VCAA 2019 Exam 2 Q5fi-ii), Q14 (VCAA 2021 Exam 2 Q3b, original wording).
Output: lessons/3C worksheet(.html/.pdf) + lessons/3C worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l11/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#000', tl_hid=False, **k) + '</div>'
def RP(pts, xr, yr, xt, yt, xl, yl, mm, W=420, H=200):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + resid(pts, xr, yr, xt, yt, xl, yl, W=W, H=H, r=4, fs=13, ink='#000') + '</div>'
YT8 = {y['id']: y for y in json.load(open(os.path.join(ws2.ROOT, 'planner', 'written-youtrys.json')))['items']}['YT-3B-8']
cx, cy = zip(*CARS); ca, cb = lsq(cx, cy); CRES = [(x, y - (ca + cb * x)) for x, y in CARS]
ma, mb = lsq(MAGE, MPR); MRES = [(x, y - (ma + mb * x)) for x, y in zip(MAGE, MPR)]
PRED = [7 + 29 * p for p in PPL]; RES = [c - p for c, p in zip(COST, PRED)]

P = [title('3B–3C', 'Residual analysis and regression analysis')]
P.append(lis(['To be able to use a residual plot to investigate the linearity assumption.', 'To be able to report a regression analysis.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('The cost, <i>C</i>, of hiring a trailer is <i>C</i> = 10<i>t</i> + 50, where <i>t</i> is the time in hours.<br>How much will it cost to hire the trailer for 6 hours?')
  + space(10, '<i>C</i> = 10 × 6 + 50 = $110')))
P.append(box('Question 2', q('What is the <i>y</i>-intercept and the slope of the straight line <i>y</i> = −7 + 2<i>x</i>?') + space(10, '<i>y</i>-intercept = −7, slope = 2')))
P.append(box('Question 3 · VCAA 2017 Exam 1 Q8', q('The scatterplot below shows the <i>wrist</i> circumference and <i>ankle</i> circumference, both in centimetres, of 13 people. A least squares line has been fitted to the scatterplot with <i>ankle</i> circumference as the explanatory variable.')
  + SP(WRIST, (21, 26), (16, 20), 1, 1, 'ankle circumference (cm)', 'wrist circumference (cm)', 52, tl=((21, 10.2 + 0.342 * 21), (26, 10.2 + 0.342 * 26)))
  + q('The equation of the least squares line is closest to')
  + mc(['<i>ankle</i> = 10.2 + 0.342 × <i>wrist</i>', '<i>wrist</i> = 10.2 + 0.342 × <i>ankle</i>', '<i>ankle</i> = 17.4 + 0.342 × <i>wrist</i>', '<i>wrist</i> = 17.4 + 0.342 × <i>ankle</i>', '<i>wrist</i> = 17.4 + 0.731 × <i>ankle</i>'], 'B')
  + why('ankle is the EV; slope ≈ 1.7 ÷ 5 ≈ 0.34; the axis starts at 21, so 17.4 is not the intercept: 17.4 − 0.342 × 21 ≈ 10.2'), '1 mark'))
P.append(box('Question 4 · VCAA 2016 Exam 2 Q3bii (adapted)', q('The data in the following scatterplot shows a sample of actual temperatures and apparent temperatures recorded at a weather station.')
  + SP(list(zip(ACT, APP)), (20, 29), (16, 26), 1, 2, 'actual temperature (°C)', 'apparent temperature (°C)', 50)
  + q('A line of good fit has the equation &nbsp; <i>apparent temperature</i> = −1.7 + 0.94 × <i>actual temperature</i><br>Interpret the intercept of the line of good fit in terms of the variables <i>apparent temperature</i> and <i>actual temperature</i>.')
  + space(14, 'On average, when the actual temperature is 0 °C, the apparent temperature is −1.7 °C.'), '1 mark'))
# ---------------------------------------------------------------- 3B residuals
P.append(sect('3B Residuals, residual plots and reports', 'Example, then you try'))
RT = lambda pred, res: T([['<b>number of people</b>'] + PPL, ['<b>actual total cost ($)</b>'] + COST, ['<b>predicted total cost ($)</b>'] + pred, ['<b>residual value ($)</b>'] + res])
P.append(exyt('Example 6 · Calculating a residual',
  q('The actual price of the 6-year-old car is $6500. Calculate the residual when its price is predicted using the regression equation: <i>price</i> = 35100 − 3940 × <i>age</i>')
  + q('Actual price: ' + a('$6500')) + q('Predicted price = 35 100 − 3940 × 6 = ' + a('$11 460')) + q('Residual = actual − predicted = $6500 − $11 460 = ' + a('−$4960')),
  'You try 6', q('A least squares regression equation has been used to predict the <i>total cost</i> ($) of a table bill at a restaurant from the <i>number of people</i> eating together on the table, such that <i>total cost</i> = 7 + 29 × <i>number of people</i>')
  + parts([('a', 'If the actual <i>total cost</i> for a table of six people is $166, calculate the residual value when the <i>total cost</i> is predicted using the regression equation.', '7 + 29 × 6 = 181; residual = 166 − 181 = −15', 14),
           ('b', 'There were 8 other groups of people at the restaurant. The <i>number of people</i> at each table and the <i>total cost</i> for each group were recorded and displayed in a table.'
            + RT([a(v) for v in PRED], [a(v) for v in RES]) + 'Use the regression equation to complete the table by filling in the predicted <i>total cost</i> and residual values.', '', 2),
           ('c', 'Construct a residual plot for this data set.', RP(list(zip(PPL, RES)), (0, 7), (-10, 10), 1, 5, 'number of people', 'residual value', 60), 40)])))
EX7 = {k: v for k, v in EX7.items()}
RPS = lambda k: f'<div><div style="text-align:center;font-weight:700">{k}</div>' + RP(EX7[k], (0, 12), (-1, 1), 2, 0.5, 'x', 'Residual', 44, H=170) + '</div>'
P.append(exyt('Example 7 · Interpreting a residual plot',
  q('Which of the following residual plots would call into question the assumption of linearity in a regression analysis? Give reasons for your answers.')
  + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:1mm">' + RPS('A') + RPS('B') + RPS('C') + RPS('D') + '</div>'
  + q('Plot A – residuals look random, so linearity assumption ' + a('is met') + '.<br>Plot B – there is a clear ' + a('curve') + ' in the residuals, the linearity assumption ' + a('is not met') + '.<br>Plot C – residuals look random, so linearity assumption ' + a('is met') + '.<br>Plot D – there is a clear ' + a('curve') + ' in the residuals, the linearity assumption ' + a('is not met') + '.'),
  'You try 7', q('Determine if the following residual plots support the assumption of linearity.')
  + parts([('a', RP(EW3['a'], (0, 8), (-4, 4), 2, 2, 'x', 'residual', 52, H=180), 'The residual plot does not support the assumption of linearity (clear curved pattern).', 14),
           ('b', RP(EW3['b'], (0, 10), (-4, 4), 2, 2, 'x', 'residual', 52, H=180), 'The residual plot supports the assumption of linearity (random, no pattern).', 14)])))
P.append(exyt('Example 8 · Reporting the results of a regression analysis',
  q('Construct a report to describe the association between the price and age of secondhand cars.')
  + SP(CARS, (0, 10), (0, 40000), 1, 10000, 'Age (years)', 'Price (dollars)', 55, tl=((0, 35100), (8.9, 35100 - 3940 * 8.9)))
  + RP(CRES, (0, 9), (-6000, 4000), 1, 2000, 'Age (years)', 'Residual', 55, H=170)
  + q('<i>r</i> = −0.964 · <i>price</i> = 35 100 − 3940 × <i>age</i> · <i>r</i>² = 0.930')
  + report(['From the scatterplot we see that there is a ', ('strength', 'strong'), ' ', ('direction', 'negative'), ', ', ('form', 'linear'), ' association between the price of a second hand car and its age, <i>r</i> = ', ('r', '−0.964'), '. There are ', ('outliers', 'no obvious outliers'), '. '
            'The equation of the least squares regression line is: <i>price</i> = ', ('equation', '35 100 − 3940 × age'), '. The slope of the regression line predicts that, on average, the price of these second-hand cars ', ('slope', 'decreased by $3940'), ' each year. '
            'The intercept predicts that, on average, the price of these cars when new was ', ('intercept', '$35 100'), '. The coefficient of determination indicates that ', ('r²', '93%'), ' of the variation in the price of these second-hand cars is explained by the variation in their age. '
            'The ', ('residual plot', 'lack of a clear pattern'), ' in the residual plot confirms the assumption of a linear association between the price and the age of these second-hand cars.']),
  'You try 8', q('Construct a report to describe the association between the price and age of secondhand motorbikes.')
  + T([['<b>age (years)</b>'] + MAGE[:5], ['<b>price ($)</b>'] + MPR[:5], ['<b>age (years)</b>'] + MAGE[5:], ['<b>price ($)</b>'] + MPR[5:]])
  + SP(list(zip(MAGE, MPR)), (0, 9), (6000, 16000), 1, 2000, 'age (years)', 'price ($)', 55, tl=((0, ma), (9, ma + mb * 9)))
  + RP(MRES, (0, 9), (-600, 600), 1, 300, 'age (years)', 'residual', 55, H=170)
  + space(60, YT8['answer'])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q2e', q('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods). This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.')
  + SP(CONG, (35, 70), (35, 75), 5, 5, 'morning congestion level (%)', 'evening congestion level (%)', 48)
  + q('e. The value of the correlation coefficient <i>r</i> is 0.92<br>What percentage of the variation in the evening congestion level can be explained by the variation in the morning congestion level?<br>Round your answer to the nearest whole number.')
  + space(10, '0.92² = 0.8464 → 85%'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2019 Exam 2 Q5f', q('The scatterplot shows the atmospheric pressure, in hectopascals (hPa), at 3 pm (<i>pressure 3 pm</i>) plotted against the atmospheric pressure, in hectopascals, at 9 am (<i>pressure 9 am</i>) for 23 days in November 2017 at a particular weather station. The equation of the least squares line is <i>pressure 3 pm</i> = 111.4 + 0.8894 × <i>pressure 9 am</i><br>f. The residual plot associated with the least squares line is shown below.')
  + RP(PRES, (1010, 1030), (-3, 3), 5, 1, 'pressure 9 am (hPa)', 'residual (hPa)', 60)
  + parts([('i', 'The residual plot above can be used to test one of the assumptions about the nature of the association between the atmospheric pressure at 3 pm and the atmospheric pressure at 9 am. What is this assumption?', 'Linearity (the association is linear).', 'L'),
           ('ii', 'The residual plot above does not support this assumption. Explain why.', 'The residuals have a clear pattern (a curve): they are not randomly scattered.', 12)]), '2 marks'))
P.append(box('Exit task 3 · VCAA 2021 Exam 2 Q3b', q('The time series plot below shows the <i>winning time</i>, in seconds, for the women’s 100 m freestyle swim plotted against <i>year</i>, for each year that the Olympic Games were held during the period 1956 to 2016. A least squares line has been fitted to the plot to model the decreasing trend in the <i>winning time</i> over this period.')
  + f'<div style="max-width:60mm;margin:1mm auto">' + ts(SWIM, (1952, 2016), (52, 64), 8, 2, 'year', 'winning time (seconds)', W=420, H=230, r=4, fs=13, ink='#000', tl=((1952, 357.1 - 0.1515 * 1952), (2016, 357.1 - 0.1515 * 2016)), tl_hid=False) + '</div>'
  + q('The equation of the least squares line is <i>winning time</i> = 357.1 – 0.1515 × <i>year</i><br>The coefficient of determination is 0.8794<br>b. Determine the value of the correlation coefficient (<i>r</i>). Round your answer to three decimal places.')
  + space(10, '√0.8794 = 0.938; the slope is negative, so r = −0.938'), '1 mark'))
SC = ['I can calculate residual values.', 'I can interpret a residual plot.', 'I can write a report based on a regression analysis.', 'I can use a CAS calculator to generate all of the analyses required for a regression analysis.']
P.append(close(SC, [('3B', 'Q8–20'), ('3C', 'Q1–3')], ['3B', '3C']))
build('l11', '3C', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l11-worksheet', '3C worksheet'), ('l11-worksheet-solutions', '3C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
