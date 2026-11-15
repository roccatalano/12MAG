"""Lesson l22 (5E, fitting a trend line and forecasting) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as tools/deck/l22/build.py (Do Now is not on the worksheet, as in l16-l21; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 5 skills checklist 5F #10 (card's 7E #10 burnt in l10: dropped), VCAA 2014 Exam 1 G&R Q4 (Edrolo U1&2 4D Q13), VCAA 2016 Exam 1 G&R Q2 (Edrolo U1&2 4E Q16).
Example 20 / You try 1 = Cambridge U3&4 Example 20 (pp. 295-296) / Edrolo U3&4 4E WE1a (pp. 280-281).
Example 21 / You try 2 = Cambridge Example 21 (p. 296) / Edrolo 4E WE1b, c (p. 281).
Example 22 / You try 3 = Cambridge Example 22 (p. 297) / Edrolo 4E WE2a (pp. 282-284).
Example 23 / You try 4 = Cambridge Example 23 (pp. 297-298) / Edrolo 4E WE2b, c (pp. 283-284).
Exit = Edrolo U3&4 4E Q12 (VCAA 2018 Exam 2 Q3bii, biii, d; original wording).
Output: lessons/5E worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/l22/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
nn = lambda v: f'{v:,}'.replace(',', ' ')
A = lambda v: ans(v)
B = lambda xs: [f'<b>{x}</b>' for x in xs]

P = [title('5E', 'Fitting a trend line and forecasting')]
P.append(lis(['To be able to use the method of least squares to fit a trend line to a time series.', 'To be able to use the trend line to make predictions.',
              'To be able to use seasonal indices to add seasonality to predicted values as appropriate.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('Find the equation of the line that goes through the points (3, −1) and (−2, 7).') + space(14, 'slope = (7 − (−1)) ÷ (−2 − 3) = −1.6; −1 = a − 1.6 × 3 → a = 3.8: y = 3.8 − 1.6x'), ''))
P.append(box('Question 2 · VCAA 2014 Exam 1 Q4', q('A line passes through the points (−1, 1) and (3, 5). Another point that lies on this line is')
  + mc(['(0, 1)', '(1, 3)', '(2, 6)', '(3, 4)', '(4, 7)'], 'B', cols=5) + why('slope 1, y = 2 + x: (1, 3) fits'), ''))
P.append(box('Question 3 · VCAA 2016 Exam 1 Q2', q('A phone company charges a fixed, monthly line rental fee of $28 and $0.25 per call.<br>Let <i>n</i> be the number of calls that are made in a month.<br>Let <i>C</i> be the monthly phone bill, in dollars.<br>The equation for the relationship between the monthly phone bill, in dollars, and the number of calls is')
  + mc(['C = 28 + 0.25n', 'C = 28n + 0.25', 'C = n + 28.25', 'C = 28(n + 0.25)', 'C = 0.25(n + 28)'], 'A', cols=3) + why('$28 fixed = intercept; $0.25 per call = slope'), ''))
P.append(sect('5E Fitting a trend line and forecasting', 'Example, then you try'))
P.append(exyt('Example 20 · Fitting a trend line',
  q('The table below shows the number of female students in Victoria enrolled in at least one subject in the Mathematics learning area at year 12 over the period 2010–18. Fit a trend line to the data, and interpret the slope.')
  + T([B(['Year'] + FEM_X[:5]), ['<b>Number</b>'] + [nn(v) for v in FEM[:5]]]) + T([B(['Year'] + FEM_X[5:]), ['<b>Number</b>'] + [nn(v) for v in FEM[5:]]])
  + q('Trend line: number of female students = ' + A('−1 633 580 + 851.017 × year')) + q('Slope = ' + A('851'))
  + q('Interpretation: ' + A('Over 2010–2018 on average the number of female students … increased by 851 per year.')),
  'You try 1', q('A public library introduced a record collection to their catalogue. The number of visitors to the library each day following its introduction was recorded.<br>The day that the record collection was introduced is noted as day 0 and the first day after the introduction is day 1.')
  + T([B(['day'] + list(range(1, 8))), ['<b>number of visitors</b>'] + LIB])
  + parts([('a', 'Determine the equation of the least squares regression line for the data. Give values correct to two decimal places where necessary.', 'number of visitors = 68.29 + 21.18 × day', 18)])))
P.append(exyt('Example 21 · Forecasting',
  q('How many female students in Victoria do we predict being enrolled in at least one subject in the Mathematics learning area at year 12 in 2026 if the same increasing trend continues? Give your answer rounded to the nearest whole number.')
  + q('number = −1 633 580 + 851.017 × ' + A('2026') + ' = ' + A('90 580')) + q('Caution: ' + A('2026 is well beyond the data (extrapolation)')),
  'You try 2', q('Use the rounded regression equation from You try 1.')
  + parts([('b', 'Use the rounded regression equation to estimate the number of visitors on the 8th day after the introduction. Round to the nearest whole number.', '68.29 + 21.18 × 8 = 237.73 → 238 visitors', 18),
           ('c', 'Use the regression equation to estimate the number of visitors to the library on the day that the record collection was introduced. Round to the nearest whole number.', 'day 0 = intercept 68.29 → 68 visitors', 18)])))
P.append(exyt('Example 22 · Fitting a trend line (seasonality)',
  q('The deseasonalised quarterly sales data from Mikki’s shop are shown below.')
  + T([B(['Quarter'] + list(range(1, 7))), ['<b>Sales</b>'] + MDS[:6]]) + T([B(['Quarter'] + list(range(7, 13))), ['<b>Sales</b>'] + MDS[6:]])
  + q('Fit a trend line and interpret the slope.') + q('Trend line: sales = ' + A('838.0 + 32.07 × quarter'))
  + q('Interpretation: ' + A('on average sales increased by 32.07 sales per quarter')),
  'You try 3', q('The sales of NRL jerseys at a merchandise store are seasonal. The sales for the first six months of 2022 are shown in the following table.')
  + T([B(['month'] + MON[:6]), ['<b>sales</b>'] + JER]) + q('The long-term seasonal index for each month is also provided.')
  + T([B(['month'] + MON[:6]), ['<b>seasonal index</b>'] + JSI[:6]]) + T([B(['month'] + MON[6:]), ['<b>seasonal index</b>'] + JSI[6:]])
  + parts([('a', 'Determine the equation of the least squares regression line to predict the deseasonalised sales for a month. Give values correct to one decimal place.<br>Note: When deseasonalising sales, round values correct to one decimal place.',
            'deseasonalised: 870.9, 814.3, 805.0, 738.8, 720.7, 673.9<br>deseasonalised sales = 903.8 − 38.1 × month', 20)])))
P.append(exyt('Example 23 · Forecasting (seasonality)',
  q('What sales do we predict for Mikki’s shop in the winter of year 4? (Because many items have to be ordered well in advance, retailers often need to make such decisions.)')
  + T([['', '<b>Summer</b>', '<b>Autumn</b>', '<b>Winter</b>', '<b>Spring</b>'], ['<b>SI</b>', '1.03', '1.15', '1.30', '0.52']])
  + q('Winter year 4 = quarter ' + A('15')) + q('Deseasonalised = 838.0 + 32.07 × 15 = ' + A('1319.05'))
  + q('Actual = ' + A('1319.05 × 1.30 = 1714.765 → 1715')),
  'You try 4', q('Use the rounded regression equation and seasonal indices from You try 3.')
  + parts([('b', 'Use the rounded regression equation to predict the sales, correct to the nearest whole number, for October 2022.', '903.8 − 38.1 × 10 = 522.8; × 0.58 = 303.224 → 303 sales', 14),
           ('c', 'Interpret the slope of the rounded regression line in terms of the change in deseasonalised sales each month.', 'On average, deseasonalised sales decrease by 38.1 each month.', 12)])))
P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q3bii, biii, d', q('Table 3 shows the yearly average traffic congestion levels in two cities, Melbourne and Sydney, during the period 2008 to 2016.<br><b>Table 3</b> · Congestion level (%)')
  + T([B(['Year'] + YRS), ['<b>Melbourne</b>'] + MEL, ['<b>Sydney</b>'] + SYD])
  + parts([('b', 'A least squares line is used to model the trend in the time series plot for Sydney. The equation is<br><i>congestion level</i> = –2280 + 1.15 × <i>year</i><br>'
            'ii. Use the equation of the least squares line to determine the average rate of increase in percentage congestion level for the period 2008 to 2016 in Sydney. ________ % per year', '1.15 % per year', 8),
           ('', 'iii. Use the least squares line to predict when the percentage congestion level in Sydney will be 43%.', '(43 + 2280) ÷ 1.15 = 2020', 12),
           ('d', 'The yearly average traffic congestion level data for Melbourne is repeated in Table 4 below.<br><b>Table 4</b>' + T([B(['Year'] + YRS), ['<b>Melbourne</b>'] + MEL]) + 'Use the data in Table 4 to determine the equation of the least squares line that can be used to model the trend in the data for Melbourne. The variable <i>year</i> is the explanatory variable.<br>Write the values of the intercept and the slope of this least squares line in the boxes provided below. Round both values to four significant figures.<br>'
            '<i>congestion level</i> = ' + A('−1515') + ' &nbsp;+&nbsp; ' + A('0.7667') + ' × <i>year</i>', '', 6)]), '4 marks'))
SC = ['I can fit a trend line to a time series plot.', 'I can use a trend line to forecast a future value (no seasonality).',
      'I can fit a trend line to a time series plot with seasonality.', 'I can use a trend line to forecast a future value (with seasonality).']
P.append(close(SC, [('5E', 'Q1–8')], ['5E']))
build('l22', '5E', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l22-worksheet', '5E worksheet'), ('l22-worksheet-solutions', '5E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
