# Chapter 5 revision booklet: Insight GM1 (MC) + GM2 (SA), "Investigating and modelling time series data"
# (GM1 Q1-22, pp.22-27; GM2 Q1-6, pp.32-39). Text verbatim from Insight (scanned books; read off the page images).
# Answers and explanations from Insight's worked solutions (GM1 pp.43-46, GM2 pp.56-60), checked by hand.
# Figures are crops of the Insight pages (crop.py). Shared stems are repeated in each box. Insight is never burnt.
# Print glitches restored: GM1 Q3 options print '¸' for ÷ (as in Insight's own solution). GM1 Q16 prints the Q18
# seasonal-index table under Q16: it is placed with Q18 here. GM2 Q2c says "this equation" but the equation is
# missing from the question: it is added from Insight's worked solution (labelled adapted). GM2 Q3e says 'Table 4'
# (Insight's typo for Table 2): kept verbatim with a note.
G1 = 'Insight GM1 U3 Data Analysis'
G2 = 'Insight GM2 U3 Data Analysis'

def across(labels, cols, cls='t sm'):
    return f'<table class="{cls}">' + ''.join('<tr><th>' + l + '</th>' + ''.join(f'<td>{c[i]}</td>' for c in cols) + '</tr>' for i, l in enumerate(labels)) + '</table>'

def P(t): return f'<p class="q">{t}</p>'
def C(t): return f'<p class="q" style="text-align:center">{t}</p>'

MONS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
COFFEE = (C('<i>Use the following information to answer Questions 2–4.</i>')
          + P('The table below shows the long-term average number of customers utilising a drive-through coffee booth for each day of the week.')
          + P('Also shown are the seasonal indices for Monday, Wednesday, Friday, Saturday and Sunday.')
          + across(['Day of the week', 'Long-term average', 'Seasonal index'],
                   list(zip(['Mon.', 'Tues.', 'Wed.', 'Thur.', 'Fri.', 'Sat.', 'Sun.'], [1820, 1700, 1467, 1476, 1765, 1239, 1348],
                            ['1.18', '', '0.95', '', '1.14', '0.80', '0.87']))))
TEMPS = (C('<i>Use the following information to answer Questions 5 and 6.</i>')
         + P('The graph below shows the maximum daily temperature for October, the month leading up to the mathematics exam, between 2000 and 2016.') + '[[g1q5]]')
MINT = (C('<i>Use the following information to answer Questions 7 and 8.</i>')
        + P('A student considered the average minimum temperature for each month within 2017. These are given in the table below:')
        + across(['<i>Month</i>', '<i>Min temp</i> (°C)'], list(zip(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], [28, 31, 26, 22, 18, 16])))
        + across(['<i>Month</i>', '<i>Min temp</i> (°C)'], list(zip(['July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], [15, 17, 23, 27, 30, 32]))))
CARSI = (C('<i>Use the following information to answer Questions 11 and 12.</i>')
         + P('The seasonal indices for the number of cars sold by the car dealership are shown below.')
         + across(['Month', 'Seasonal index'], list(zip(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], ['1.29', '1.17', '', '0.77', '0.70', '0.92'])))
         + across(['Month', 'Seasonal index'], list(zip(['July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'], ['1.24', '1.08', '0.99', '0.80', '0.95', '1.22']))))
STORE = (C('<i>Use the following information to answer Questions 17 and 18.</i>')
         + P('The sales figures for a store are shown in the time series plot below.') + '[[g1q17]]')

def MC(n, sub, page, stem_, opts, a, why, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)

Q = [
 # ---- 5A: features of time series plots
 MC(1, '5A', 22, P('Consider the time series plot below.') + '[[g1q1]]' + P('The pattern in the time series plot shown above can be best described as having'),
    ['irregular fluctuations only.', 'an increasing trend with seasonality.', 'an increasing trend with irregular fluctuations.', 'an increasing trend with cycles evident.', 'structural change.'],
    'C', 'No pattern repeats within a year (no seasonality) or over a longer regular period (no cycles); sales rise over time with random fluctuations.'),
 MC(5, '5A', 23, TEMPS + P('The time series is best described as having'),
    ['seasonality only.', 'irregular fluctuations only.', 'seasonality with irregular fluctuations.', 'a decreasing trend with irregular fluctuations.', 'an increasing trend with irregular fluctuations.'],
    'E', 'No pattern repeats within a year, so no seasonality (A, C wrong). Values do not decline (D wrong); they increase over time.', shared='Q5–6'),
 MC(16, '5A', 26, P('The number of koalas observed in a reserve was recorded once a week over the course of 12 weeks. This data is shown in the graph below.') + '[[g1q16]]'
    + P('After the sixth week, a bushfire destroyed a section of the reserve.') + P('The impact on the data could best be described as'),
    ['a decreasing trend.', 'a discontinuity.', 'seasonality.', 'smoothed data.', 'an outlier.'],
    'B', 'A discontinuity (structural change) is a sudden break in the data: the shift from week 6 to week 7.'),
 # ---- 5B: moving means and centring
 MC(10, '5B', 24, P('The number of cars sold monthly by a local car dealership in 2017 are displayed in the table below.')
    + across(['Month', 'Number of cars'], list(zip(['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June'], [125, 114, 86, 75, 68, 89])))
    + across(['Month', 'Number of cars'], list(zip(['July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'], [120, 105, 95, 78, 92, 118])))
    + P('Using three-mean smoothing, the smoothed number of cars sold in July is closest to'),
    ['89', '95', '104', '105', '120'], 'D', '(89 + 120 + 105) ÷ 3 = 104.67 ≈ 105'),
 MC(8, '5B', 24, MINT + P('The four-point moving mean with centring is used to smooth the time series data. The smoothed value for August 2017 is closest to'),
    ['18', '19', '20', '21', '22'], 'B', '(16 + 15 + 17 + 23) ÷ 4 = 17.75; (15 + 17 + 23 + 27) ÷ 4 = 20.5; centred: (17.75 + 20.5) ÷ 2 = 19.125 ≈ 19', shared='Q7–8'),
 MC(13, '5B', 25, P('The table below shows the sales of cakes over 10 days.')
    + across(['Day', 'Sales'], list(zip(range(1, 6), [15, 13, 17, '', 21]))) + across(['Day', 'Sales'], list(zip(range(6, 11), [24, 23, 18, 17, 15])))
    + P('A two-point moving mean with centring is used to smooth the time series data above.')
    + P('If the smoothed sales figure for Day 4 was 19.5, what was the actual sales figure for Day 4?'),
    ['18', '19', '20', '22', '38'], 'C', '½ × ((17 + x) ÷ 2 + (x + 21) ÷ 2) = 19.5 → (38 + 2x) ÷ 4 = 19.5 → x = 20 (check: 18.5, 20.5, centred 19.5)'),
 MC(19, '5B', 27, P('The table below shows the average temperature, in degrees Celsius, for each month in a year.')
    + across(['', ''], list(zip(['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June'], [29, 28, 23, 20, 19, 10]))).replace('<tr><th></th>', '<tr><th>Month</th>', 1).replace('<tr><th></th>', '<tr><th>°C</th>', 1)
    + across(['', ''], list(zip(['July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'], [7, 9, 11, 16, 24, 30]))).replace('<tr><th></th>', '<tr><th>Month</th>', 1).replace('<tr><th></th>', '<tr><th>°C</th>', 1)
    + P('The two-mean smoothed average temperature with centring for August is'),
    ['8', '9', '10', '11', '20'], 'B', '(7 + 9) ÷ 2 = 8; (9 + 11) ÷ 2 = 10; centring: (8 + 10) ÷ 2 = 9'),
 # ---- 5C: moving medians
 MC(6, '5C', 24, TEMPS + P('The five-median smoothed value for 2011 is closest to'),
    ['26', '27', '28', '31', '36'], 'C', 'Insight: the median of the five points centred on 2011 (graphically, the median x and median y lines cross at (2011, 28)).', shared='Q5–6'),
 MC(14, '5C', 25, P('A time series plot is shown below.') + '[[g1q14]]' + P('If five-median smoothing is completed, how many months have a smoothed value of 2?'),
    ['1', '2', '3', '4', '5'], 'E', 'Smooth Mar to Oct (median of each five consecutive months): five of these smoothed values are 2.'),
 MC(17, '5C', 26, STORE + P('Three-median smoothing has been performed; however, there are some errors.') + P('Which months have errors in the smoothed result?'),
    ['May, October', 'January, October, December', 'January, May, October, December', 'January, May, December', 'May, October, December'],
    'C', 'January and December cannot have three-median values (no neighbour on one side). May and October are also plotted at the wrong values.', shared='Q17–18'),
 MC(20, '5C', 27, P('The online sales for a bookstore over 12 days are shown in the time series plot below.') + '[[g1q20]]'
    + P('The seven-median smoothed <i>number of sales</i> value for day 8 is closest to'),
    ['19', '29', '39', '48', '51'], 'B', 'Days 5–11: 48, 51, 16, 19, 29, 15, 39. In order: 15, 16, 19, <b>29</b>, 39, 48, 51. Median = 29'),
 # ---- 5D: seasonal indices, deseasonalising
 MC(2, '5D', 23, COFFEE + P('The seasonal index for Sunday is 0.87') + P('This tells us that, on average, the number of coffees sold on a Sunday is'),
    ['87% of the coffee sales for the week.', '87% less than the daily average for coffee sales.', '87% more than the daily average for coffee sales.',
     '13% more than the daily average for coffee sales.', '13% less than the daily average for coffee sales.'],
    'E', '1 − 0.87 = 0.13: Sunday sales are 13% below the daily average.', shared='Q2–4'),
 MC(3, '5D', 23, COFFEE + P('The seasonal index for Tuesday is missing.') + P('The correct calculation to find the seasonal index for Tuesday is'),
    ['1&#8239;545 ÷ 1700', '1700 ÷ 1&#8239;545', '(7 − (1.18 − 0.95 − 1.14 − 0.80 − 0.87)) ÷ 2', '1&#8239;700 ÷ 10&#8239;815', '1&#8239;700 ÷ 7'],
    'B', 'Weekly average = (1820 + 1700 + 1467 + 1476 + 1765 + 1239 + 1348) ÷ 7 = 1545. SI = 1700 ÷ 1545 = 1.10', shared='Q2–4'),
 MC(4, '5D', 23, COFFEE + P('In the final week of the school term the actual sales for coffee on a Friday were 1825.')
    + P('The deseasonalised number of coffee sales for the last Friday of the term was closest to'),
    ['247', '1600', '1765', '2011', '12&#8239;600'], 'B', 'deseasonalised = actual ÷ SI = 1825 ÷ 1.14 = 1600', shared='Q2–4'),
 MC(7, '5D', 24, MINT + P('The seasonal index for the month of May, correct to two decimal places, is closest to'),
    ['1.80', '1.32', '1.00', '0.76', '0.69'], 'D', 'Yearly average = 285 ÷ 12 = 23.75. SI(May) = 18 ÷ 23.75 = 0.7579 ≈ 0.76', shared='Q7–8'),
 MC(11, '5D', 25, CARSI + P('The seasonal index for March is'),
    ['0.13', '0.67', '0.87', '0.93', '2.09'], 'C', 'Twelve seasons: indices add to 12. 12 − (sum of the other eleven = 11.13) = 0.87', shared='Q11–12'),
 MC(12, '5D', 25, CARSI + P('If the deseasonalised predicted value for car sales in July 2019 is 99, the actual value for July 2019 is closest to'),
    ['79', '80', '87', '122', '123'], 'E', 'actual = deseasonalised × SI = 99 × 1.24 = 122.76 ≈ 123', shared='Q11–12'),
 MC(15, '5D', 25, P('The sales figures of plants in a shop were recorded each month. When the seasonal index for the sales in May was calculated, it was determined that the actual sales needed to be increased by 25% in order to correct for seasonality.')
    + P('What was the seasonal index for May?'),
    ['0.25', '0.75', '0.80', '1.25', '4.00'], 'C', '1 ÷ SI = 1.25 → SI = 0.8'),
 MC(21, '5D', 27, P('The table below shows two of the seasonal indices for the quarterly sales figures of a business.')
    + across(['', 'Seasonal index'], list(zip(['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'], ['1.07', '1.03', '', '']))).replace('<tr><th></th>', '<tr><th>Quarter</th>', 1)
    + P('Which one of the following is <b>not</b> true about this data?'),
    ['The sales in Quarter 1 are 7% above the average sales.', 'The mean seasonal index for Quarter 3 and Quarter 4 is 0.95', 'The seasonal index for Quarter 3 could be 0.98',
     'The seasonal index for Quarter 4 could be 1.06', 'The sales for the year are 400% above the average sales.'],
    'E', 'Indices add to 4, so Q3 + Q4 = 1.90 (mean 0.95; 0.98 + 0.92 or 0.84 + 1.06 both work). Adding to 4 (400%) does not mean sales are 400% above average.'),
 MC(22, '5D', 27, P('A business has a seasonal index of 1.20 for Quarter 1.') + P('To correct for seasonality, its sales for Quarter 1 would need to be'),
    ['decreased by 20%', 'decreased by 17%', 'decreased by 13%', 'increased by 17%', 'increased by 13%'], 'B', '1 ÷ 1.20 = 0.833 = 83.3%: decrease by 100 − 83 = 17%'),
 # ---- 5E: trend lines and forecasting
 MC(9, '5E', 24, P('The average minimum temperature was gathered for the first 10 months of 2018, in order to make predictions around the possible temperature for future Year 12 examinations.')
    + P('The regression equation for the deseasonalised data for January to October 2018 is') + C('deseasonalised = 25.558 − 0.027 × month')
    + P('where January 2018 is month 1.') + P('The seasonal index for November is 1.26.') + P('The average minimum temperature for November 2018 is'),
    ['24', '25', '30', '31', '32'], 'E', 'November = month 11: 25.558 − 0.027 × 11 = 25.261 (deseasonalised). Reseasonalise: 25.261 × 1.26 = 31.83 ≈ 32'),
 MC(18, '5E', 26, STORE + P('The seasonal indices for sales data of the store are shown below.')
    + across(['', 'Seasonal index'], list(zip(['Q1', 'Q2', 'Q3', 'Q4'], ['0.82', '1.04', '', '0.96']))).replace('<tr><th></th>', '<tr><th></th>', 1)
    + P('The equation of the least squares line fitted to the deseasonalised sales data is') + C('<i>deseasonalised sales</i> ($’000) = 13.9 + 1.08 × <i>quarter number</i>')
    + P('The actual sales figure for Quarter 3 is closest to'),
    ['$14&#8239;525', '$17&#8239;140', '$20&#8239;225', '$23&#8239;355', '$26&#8239;075'],
    'C', 'SI(Q3) = 4 − (0.82 + 1.04 + 0.96) = 1.18. Deseasonalised = 13.9 + 1.08 × 3 = 17.14 ($17&#8239;140). Actual = 1.18 × 17&#8239;140 = $20&#8239;225.20', shared='Q17–18'),
]

def SA(n, sub, page, stem_, parts, why=None, note=None, long=False):
    return dict(long=long, kind='sa', n=n, sub=sub, marks=sum(p[4] for p in parts), stem=stem_, parts=parts, why=why, note=note, src=f'{G2} pp.{page} Q{n}')

TS3 = across(['', 'Month', 'Number of delays'], list(zip(range(1, 14), ["Oct '17", "Nov '17", "Dec '17", "Jan '18", "Feb '18", "Mar '18", "Apr '18", "May '18", "June '18", "July '18", "Aug '18", "Sept '18", "Oct '18"],
                                                         [45, 52, 68, 85, 35, 40, 62, 42, 73, 58, 38, 78, 49])))
T2 = across(['', '<i>Month</i>', '<i>Number of delays</i>', '<i>Three-mean smoothing</i>'],
            list(zip(range(1, 14), ["Oct '17", "Nov '17", "Dec '17", "Jan '18", "Feb '18", "Mar '18", "Apr '18", "May '18", "June '18", "July '18", "Aug '18", "Sept '18", "Oct '18"],
                     [45, 52, 68, 85, 35, 40, 62, 42, 73, 58, 38, 78, 49], ['■', 55, 68, 63, 53, 46, 48, 59, 58, 56, 58, '', '■'])))
BOXES = ('<div class="fillin"><i>number of delays</i> = <span class="bx"><u>59</u></span> + <span class="bx"><u>−0.35</u></span> × <i>month</i></div>')

Q += [
 # ---- 5D
 SA(5, '5D', '37', P('The amount of screen time Amina had each day over one week is shown below.')
    + across(['Day', '<i>Screen time</i> (hours)'], list(zip(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], [3.3, 2.1, 3.2, 1.5, 2.4, 4.5, 6.1]))),
    [('a', 'Using the data provided, show that the two-point centred moving mean for Thursday is 2.15.',
      '(3.2 + 1.5) ÷ 2 = 2.35; (1.5 + 2.4) ÷ 2 = 1.95; centring: (2.35 + 1.95) ÷ 2 = 2.15', 14, 2),
     ('b', 'The long-term average number of hours of screen time for each day is shown below.'
      + across(['Day', '<i>Screen time</i> (hours)', 'Seasonal index'], list(zip(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Weekly average'],
               [3.1, 2.7, 3.8, 2.6, 2.5, 4.4, 6.3, 3.628], ['0.85', '0.74', '<u>1.05</u>', '<u>0.72</u>', '0.69', '1.21', '1.74', ''])))
      + 'Complete the missing seasonal indices in the table above.', 'SI = actual ÷ average: Wed 3.8 ÷ 3.628 = 1.05; Thu 2.6 ÷ 3.628 = 0.72', 4, 1)]),
 SA(6, '5D', '38–39', P('The total number of cars in a carpark is recorded over each day for a week. The results are shown below.')
    + across(['Day', 'Number of cars'], list(zip(['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'], [593, 272, 208, 730, 345, 425, 894])))
    + P('The data is smoothed using both a three-moving median and three-point moving mean method of smoothing.')
    + P('Part of the smoothing for both methods has been graphed onto the time series plot below.') + '[[g2q6]]',
    [('a i', 'Complete the three-point moving median smoothing and the three-point moving mean smoothing on the <b>time series plot above</b>.<br><i>(Answer on the time series plot above.)</i>',
      'Medians: Wed 345, Thu 425 (Mon 272, Tue 272, Fri 425 given). Means: Wed 427.7, Thu 500 (Mon 357.7, Tue 403.3, Fri 554.7 given).[[s6a]]', 44, 2),
     ('ii', 'Explain a limitation of using a moving-mean method to smooth data compared to using a moving-median method.',
      'The moving mean is affected by outliers or extreme values; the moving median is not.', 8, 1),
     ('b i', 'The average number of cars parked each month in the carpark for a year is shown in the table below.'
      + across(['Month', 'Number of cars'], list(zip(['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.', '<b>Average</b>'],
               ['22&#8239;100', '19&#8239;700', '16&#8239;400', '18&#8239;400', '12&#8239;500', '12&#8239;900', '18&#8239;800', '20&#8239;300', '21&#8239;500', '19&#8239;700', '32&#8239;400', '48&#8239;200', '<b>21&#8239;908</b>'])))
      + 'Show that the calculation to determine the seasonal index for May is 0.57', 'SI = 12&#8239;500 ÷ 21&#8239;908 = 0.57', 8, 1),
     ('ii', 'In May the following year, the average number of cars was 14&#8239;300.<br>What is the deseasonalised value?<br>Round your answer to three significant figures.',
      '14&#8239;300 ÷ 0.57 = 25&#8239;087.7 ≈ 25&#8239;100', 10, 1)], long=True),
 # ---- 5E
 SA(1, '5E', '32', P('A Year 12 student recorded the amount of sleep that she had in the months leading up to her November exams.')
    + P('The data she recorded, shown to the nearest hour, are given in the table below.') + P('A time series graph has also been produced.')
    + across(['Month', '<i>Month number</i>', '<i>Sleep per month (hours)</i>'], list(zip(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'], range(1, 11),
             [282, 252, 265, 257, 262, 224, 218, 198, 172, 165]))) + '[[g2q1]]',
    [('a', 'Describe the time series plot above.', 'A decreasing trend only (a mention of random variation is also accepted).', 6, 1),
     ('b', 'Find the equation for the least squares trend line for this time series data, using the variables <i>sleep per month</i> and <i>month number</i>.<br>Round your coefficients correct to one decimal place.',
      '<i>sleep</i> = 299.6 − 12.7 × <i>month</i>', 6, 1),
     ('c', 'Explain why it would <b>not</b> be appropriate to use this trend line to predict the hours for <i>sleep</i> for this student in January of the following year.',
      'It would be extrapolating; also the data is only for her final year of school: the pattern would not continue after exams finish.', 8, 1),
     ('d', 'Using the data provided, show that the seasonal index for July (Month 7) is 0.95.',
      'Average = (282 + 252 + … + 165) ÷ 10 = 2295 ÷ 10 = 229.5; SI = actual ÷ average = 218 ÷ 229.5 = 0.9499 ≈ 0.95', 12, 2)], long=True),
 SA(2, '5E', '33', P('The following table shows the average temperature (°C) of the mathematics classroom, as recorded by the teacher, in the 12 months leading up to the students’ final mathematics SAC.')
    + P('The teacher was concerned that the room may be too hot for the students.')
    + across(['Time', 'Month no.', 'Temp (°C)'], list(zip(['Oct 2017', 'Nov 2017', 'Dec 2017', 'Jan 2018', 'Feb 2018', 'Mar 2018', 'Apr 2018', 'May 2018', 'Jun 2018', 'Jul 2018', 'Aug 2018', 'Sept 2018'],
             range(1, 13), [27, 29, 28, 31, 32, 25, 21, 17, 16, 15, 18, 23])))
    + P('The data is also displayed graphically below.') + '[[g2q2]]',
    [('a', 'The graph above shows both the original data for <i>average temperature</i> and the three- median smoothed data. The three-median smoothed value for August 2018 is missing.<br>Complete the graph for three-median smoothing above.',
      'Median of 15, 18, 23 is 18: plot (11, 18) and join it to the line.[[s2a]]', 28, 1),
     ('b', 'The table below shows the seasonal indices (SI) for each month:'
      + across(['Time', 'SI'], list(zip(['Oct 2017', 'Nov 2017', 'Dec 2017', 'Jan 2018', 'Feb 2018', 'Mar 2018', 'Apr 2018', 'May 2018', 'Jun 2018', 'Jul 2018', 'Aug 2018', 'Sept 2018'],
               ['1.13', '1.23', '1.19', '1.33', '1.35', '1.08', '0.89', '0.74', '0.68', '0.64', '0.79', '0.98'])))
      + 'Calculate the deseasonalised value for June 2018, correct to one decimal place.', 'deseasonalised = actual ÷ SI = 16 ÷ 0.68 = 23.5', 6, 1),
     ('c', '<span style="color:#555">[Adapted: the equation is missing from Insight’s printed question; it is taken from Insight’s worked solution.] '
      '<i>deseasonalised temperature</i> = 23.71 + 0.457 × <i>month</i></span><br>'
      'Use this equation to predict the temperature in the mathematics classroom on the day of the students’ last mathematics SAC, which will occur in October 2018. Round your answer to the nearest whole degree.',
      'October 2018 = month 13: 23.71 + 0.457 × 13 = 29.651 (deseasonalised). Reseasonalise with SI(Oct) = 1.13: 29.651 × 1.13 = 33.5 ≈ 34 °C', 10, 2)], long=True),
 SA(3, '5E', '34–35', P('Airsetter Airlines wants to investigate the relationship between month and number of delays.')
    + P('Table 1 shows the number of delays recorded for each month, from October 2017 to October 2018, for the flight from Melbourne to Sydney.') + P('<b>Table 1</b>') + TS3
    + P('This data is shown on the time series plot below, along with an incomplete graph for the data that has been smoothed using three-mean smoothing.') + '[[g2q3]]',
    [('a', 'Describe a feature of the time series plot for the original data.', 'Random variation only (possibly an increasing trend).', 6, 1),
     ('b i', 'A least squares line is used to model the trend in the time series plot for the original data.<br>The equation is'
      '<div style="text-align:center"><i>number of delays</i> = 54.58 + 0.17 × <i>month</i></div>'
      'Use the equation of the least squares line to find the month and year in which it is predicted there will be 58 delays.',
      '58 = 54.58 + 0.17 × month → month = 20.1: month 20 = May 2019', 6, 1),
     ('ii', 'The correlation coefficient, <i>r</i>, for this least squares regression line is 0.04062.<br>Using the <i>r</i>-value, explain why the prediction in <b>part b.i.</b> would not be reliable.',
      'r = 0.04062 means little or no correlation: the least squares line is not suited to this data.', 6, 1),
     ('c', 'Table 2 shows the three-mean smoothed values for this time series plot.<br>This table is incomplete.<br><b>Table 2</b>' + T2
      + 'Calculate the three-mean smoothed value for September 2018.', '(38 + 78 + 49) ÷ 3 = 55', 6, 1),
     ('d', 'Plot your answer from <b>part c.</b> on the <b>time series plot.</b><br><i>(Answer on the time series plot.)</i>', 'Plot (12, 55) and join it to the smoothed line.[[s3d]]', 31, 1),
     ('e', 'When a least squares line is used to model the three-mean smoothed data, the <i>y</i>-intercept for this line is approximately 58.69.<br>'
      'Use the data in Table 4 to determine the equation of the least squares line that can be used to model the trend for the smoothed data for the number of delays for the flight between Melbourne and Sydney airports.<br>'
      'Write you answer in the appropriate boxes provided below.<br>Round the values for slope and intercept to two significant figures.' + BOXES,
      'Intercept 58.69 → 59. CAS on the smoothed values (Table 2) gives slope −0.345455 → −0.35: <i>number of delays</i> = 59 − 0.35 × <i>month</i>', 14, 1)],
    note='Part e: ‘Table 4’ is Insight’s typo for Table 2.', long=True),
 SA(4, '5E', '36', P('The gym allows non-members to attend for a casual fee of $12 per visit. The income received through these casual fees for each of the four seasons in 2017 and 2018 is shown in the time series plot below. Some of the data is missing.')
    + '[[g2q4]]' + P('Table 1 below shows the completed data for 2017 and 2018.') + P('<b>Table 1</b> · Total income ($)')
    + across(['Year', '2017', '2018'], [('Summer', '17&#8239;064', '17&#8239;976'), ('Autumn', '13&#8239;236', '14&#8239;256'), ('Winter', '10&#8239;548', '11&#8239;064'), ('Spring', '15&#8239;732', '15&#8239;876')]),
    [('a', 'Complete the time series plot above using the data from Table 1.', 'Plot quarters 7 (11&#8239;064) and 8 (15&#8239;876) and join them.[[s4a]]', 24, 1),
     ('b', 'The seasonal indices for the four quarters are shown in Table 2 below.<br><b>Table 2</b>'
      + across(['', 'Seasonal index'], list(zip(['Summer', 'Autumn', 'Winter', 'Spring'], ['1.21', '0.95', '0.75', '1.09'])))
      + 'Table 3 shows the values for Seasons 1–5, which have already been deseasonalised.<br><b>Table 3</b>'
      + across(['Season', 'Deseasonalised data'], list(zip(range(1, 9), ['14&#8239;102.48', '13&#8239;932.63', '14&#8239;064.00', '14&#8239;433.03', '14&#8239;856.20',
               '<u>15&#8239;006.32</u>', '<u>14&#8239;752.00</u>', '<u>14&#8239;565.14</u>'])))
      + 'Deseasonalise the values for Seasons 6–8, and use the values in Table 3 to find the linear equation for the deseasonalised income received by the gym through casual fees.<br>Round the values for the slope and intercept to two decimal places.',
      '14&#8239;256 ÷ 0.95 = 15&#8239;006.32; 11&#8239;064 ÷ 0.75 = 14&#8239;752; 15&#8239;876 ÷ 1.09 = 14&#8239;565.14. CAS (season 1–8): '
      '<i>deseasonalised income</i> = 13&#8239;896.89 + 126.02 × <i>season number</i>', 10, 2)], long=True),
]

SUBS = [('5A', 'Time series data: features of time series plots'), ('5B', 'Smoothing with moving means (and centring)'),
        ('5C', 'Smoothing with moving medians'), ('5D', 'Seasonal indices, deseasonalising and reseasonalising'),
        ('5E', 'Trend lines and forecasting')]
