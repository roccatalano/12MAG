"""Lesson 3 (1F) guided worksheet, S1/S4 house style. Question text copied verbatim from lessons/S3-slides.html (which copied it from the sources).
Run: python3 tools/deck/s3/worksheet.py -> lessons/S3-worksheet(.html/.pdf) + lessons/S3-worksheet-solutions(.html/.pdf)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from wslib import *

P = [title('1F', 'Measures of centre and spread: median, quartiles, IQR, mean and standard deviation', 'Chapter 1 · 1F')]
P.append(lis(['To be able to understand the mean and the median as measures of centre.', 'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
  'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.', 'To be able to use a CAS calculator to calculate these summary statistics.']))

PARTY = '19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29'
party_stem = stem([('1', [7, 9, 9, 9]), ('2', [0, 0, 1, 1, 2, 3, 6, 7, 8, 9]), ('3', [4, 4, 7]), ('4', [5]), ('5', [6]), ('6', [6])], 'Key: 1 | 7 = 17')
apk = (item('1', q('The ages of a group of people at a party:') + f'<div class="data">{PARTY}</div>'
          + parts([('1. a', 'Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?', 'x̄ = 583 ÷ 20 = 29.15; M = (23 + 26) ÷ 2 = 24.5. Median: skewed, with outliers (56, 66).'),
                   ('b', 'Determine the quartiles and hence the IQR of the ages of the people at the party.', 'Q<sub>1</sub> = 20, Q<sub>3</sub> = 34, IQR = 14')]), party_stem, sep=False)
       + cite(f'{CAM12} · Chapter 2 skills checklist, 2E #10, 2F #11')
       + item('2', q('<b>2.</b> The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.')
              + table([['number of eggs', '172', '192', '159', '125', '197', '135', '140', '140', '138', '166', '136', '131']], head=False)
              + q('From the information given, determine the range. <i>(1 mark)</i>') + lines(1, '197 − 125 = 72 eggs'))
       + guess('87%', mcq=False) + cite(f'{EDR12} · 1D Q18 · VCAA 2017 Exam 2 Data analysis Q1ai'))
P.append(box('Activating prior knowledge', apk, 'Year 11', cls='split'))

P.append(box('Key ideas', '<div class="row"><div style="flex:1">' + q('<b>Centre:</b> median M (the middle value) · mean x̄ (the balance point)<br><b>Spread:</b> range = largest − smallest · IQR = Q<sub>3</sub> − Q<sub>1</sub> · standard deviation s')
  + q('<b>Median:</b> for <i>n</i> data values the median is located at the (<i>n</i> + 1) ÷ 2 th position (ordered data). n odd: the middle value; n even: the average of the two middle values.') + '</div><div style="flex:1">'
  + q('<b>Q<sub>1</sub></b> = median of the lower half · <b>Q<sub>3</sub></b> = median of the upper half (n odd: leave the median out).') + q('<b>Mean:</b> x̄ = Σx ÷ n') + q('They come in pairs: median with IQR · mean with standard deviation.') + '</div></div>'
  + cite(f'{CAM}, 1F pp. 44–52')))

P.append(pair('Example 14 · Finding the median value in a data set',
  q('Order each of the following data sets, locate the median, and then write down its value.')
  + parts([('a', '2 9 1 8 3 5 3 8 1', '1 1 2 3 <b>3</b> 5 8 8 9 → n = 9, 5th value: M = 3'), ('b', '10 1 3 4 8 6 10 1 2 9', '1 1 2 3 <b>4 6</b> 8 9 10 10 → M = (4 + 6) ÷ 2 = 5')]) + cite(f'{CAM} · Example 14'),
  'You try · Edrolo 1E WE1',
  q('Construct a five-number summary for the following data.') + '<div class="data">3 5 1 10 8 9 6 3 8 6</div>' + lines(2, 'In order: 1 3 3 5 6 6 8 8 9 10 · M = (6 + 6) ÷ 2 = 6 · Q<sub>1</sub> = 3 · Q<sub>3</sub> = 8')
  + five(['1', '3', '6', '8', '10']) + cite(f'{EDR} · 1E Worked example 1')))
P.append(pair('Example 15 · Finding the median value from a dot plot',
  q('The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team.') + dotplot(17, 30, [18, 18, 19, 19, 22, 22, 22, 22, 23, 23, 24, 25, 29], 'Age (years)', r=3.5)
  + q('Determine the median age of these cricketers and mark its location on the dot plot.') + lines(1, 'n = 13: (13 + 1) ÷ 2 = 7th value → median = 22 years') + cite(f'{CAM} · Example 15'),
  'You try · Edrolo 1F WE2',
  q('Consider the dot plot.') + dotplot(22, 31, [23, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29, 29, 30, 31], '', r=3)
  + q('<b>a.</b> Determine the median.') + lines(1, '28 data points: (28 + 1) ÷ 2 = 14.5 → average of the 14th and 15th: (27 + 27) ÷ 2 = 27') + cite(f'{EDR} · 1F Worked example 2a')))
TEMP = [('1', [8, 9, 9]), ('2', [0, 2, 5, 7, 8, 9, 9]), ('3', [1, 3])]
P.append(pair('Examples 16 + 17 · Median and range from a stem plot',
  q('The stem plot opposite displays the maximum temperature (in °C) for 12 days in January.') + stem(TEMP, 'Key: 0|8 = 8°C')
  + parts([('16', 'Determine the median maximum temperature for these 12 days.', 'the 6th and 7th values are 25 and 27: M = (25 + 27) ÷ 2 = 26°C'), ('17', 'Determine the temperature range over these 12 days.', '33 − 18 = 15°C')]) + cite(f'{CAM} · Examples 16, 17'),
  'You try · Edrolo 1F WE3',
  q('Consider the stem plot.') + stem([('40', [7]), ('41', []), ('42', []), ('43', []), ('44', [4, 6]), ('45', [1, 3, 3]), ('46', [2, 6, 7]), ('47', [4, 7, 8, 9]), ('48', [0, 0, 4, 5, 6, 8]), ('49', [1, 2, 5, 5, 5, 9]), ('50', [3, 4, 4, 7, 8, 8, 9, 9])], 'Key: 40 | 7 = 407')
  + q('<b>a.</b> Calculate the median.') + lines(1, '33 data points: (33 + 1) ÷ 2 = 17th → median = 485') + cite(f'{EDR} · 1F Worked example 3a')))
NET = stem([('2', [2, 3, 5, 7, 9]), ('3', [0, 1, 3, 5, 7, 7, 8]), ('4', [0, 1, 2, 2])], 'Key: 2 | 2 = 22 goals')
P.append(pair('Example 18 · IQR from a stem plot, n even',
  q('Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.')
  + stem([('1', [9]), ('2', [1, 3, 5, 8]), ('3', [0, 0, 4, 9, 9]), ('4', [0, 4, 5, 8]), ('5', [0, 3]), ('6', [3, 4])], 'Weight (kg) · 1 | 2 represents 1.2 kg')
  + lines(3, 'Lower 9: 1.9 2.1 2.3 2.5 <b>2.8</b> 3.0 3.0 3.4 3.9 → Q<sub>1</sub> = 2.8<br>Upper 9: 3.9 4.0 4.4 4.5 <b>4.8</b> 5.0 5.3 6.3 6.4 → Q<sub>3</sub> = 4.8<br>IQR = 4.8 − 2.8 = 2.0') + cite(f'{CAM} · Example 18'),
  'You try · Edrolo 1E WE2',
  q('The following stem plot displays the <i>number of goals scored</i> by 16 netball teams over a season.') + NET
  + parts([('a.', 'Calculate the range of <i>goals scored</i>.', '42 − 22 = 20 goals'), ('b.', 'Calculate the IQR of <i>goals scored</i>.', 'Q<sub>1</sub> = (27 + 29) ÷ 2 = 28, Q<sub>3</sub> = (38 + 40) ÷ 2 = 39, IQR = 11 goals')]) + cite(f'{EDR} · 1E Worked example 2')))
P.append(pair('Example 19 · IQR from a stem plot, n odd',
  q('The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.')
  + stem([('5', [2]), ('5', [5, 6]), ('6', [4]), ('6', [6, 6, 7, 9]), ('7', [1, 2, 2, 3, 3, 4, 4, 4, 4]), ('7', [5, 5, 6, 6, 7, 7])], 'Stem: 5|2 = 52 years')
  + lines(3, 'M = 12th value = 73; leave it out: 11 below, 11 above<br>Q<sub>1</sub> = 6th value = 66 · Q<sub>3</sub> = 18th value = 75 · IQR = 75 − 66 = 9') + cite(f'{CAM} · Example 19 (no matching Edrolo worked example)'),
  'Example 20 · Median and quartiles from a histogram',
  q('The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.')
  + hist(10, 10, [1, 0, 0, 2, 4, 5, 3, 6, 2], 7, 1, 'internet hours per week', 'Frequency')
  + lines(3, 'M = 12th value: 60–70 · Q<sub>1</sub> = 6th from the bottom: 50–60 · Q<sub>3</sub> = 6th from the top: 80–90') + cite(f'{CAM} · Example 20')))
P.append(pair('You try · Edrolo 1F WE1',
  q('Consider the histogram.') + hist(1, 1, [3, 15, 12, 13, 9, 5, 2], 16, 4, '', 'frequency')
  + q('<b>a.</b> Estimate the median.') + lines(2, '59 data points; median at the 30th. Cumulative: 3, 18, 30 → in 3–&lt;4: approximately 3.5') + cite(f'{EDR} · 1F Worked example 1a'),
  'Example 21 · Calculating the mean from the formula',
  q('The following is a set of reaction times (in milliseconds):') + '<div class="data">38 36 35 43 46 64 48 25</div>' + q('Write down the values of the following, correct to one decimal place.')
  + parts([('a', '<i>n</i>', '8'), ('b', 'Σ<i>x</i>', '335'), ('c', 'x̄', '335 ÷ 8 = 41.875 → 41.9')], cols=3) + cite(f'{CAM} · Example 21')))
P.append(pair('You try · Edrolo 1G WE1',
  q('The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.') + '<div class="data">11.60 55.50 7.95 42.15 17.10 2.00 82.55 26.85 5.40 21.90</div>'
  + lines(2, 'Σx = 273, n = 10 · x̄ = 273 ÷ 10 = 27.3 → $27.30') + cite(f'{EDR} · 1G Worked example 1'),
  'Mean or median?',
  q('The mean and the median are both measures of the centre of a distribution. If the distribution is:') + q('• symmetric and there are no outliers, either the mean or the median can be used to indicate the centre of the distribution<br>• clearly skewed and/or there are outliers, it is more appropriate to use the median to indicate the centre of the distribution.')
  + q('<b>Standard deviation</b> s: roughly the typical distance of the data values from the mean. On CAS it is <b>s<sub>x</sub></b>.') + cite(f'{CAM}, 1F p. 52')))
P.append(pair('CAS 3 · Mean and standard deviation from a list',
  q('The following are the heights (in cm) of a group of women.') + '<div class="data">176 160 163 157 168 172 173 169</div>' + q('Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.')
  + q('<b>TI-Nspire:</b> Lists &amp; Spreadsheet → Calculator › Menu › Statistics › Stat Calculations › One-Variable Statistics.<br><b>ClassPad:</b> Statistics app → Calc › One-Variable.')
  + lines(1, 'x̄ = 167.25 cm · s = 6.67 cm (use s<sub>x</sub>, not σ<sub>x</sub>)') + cite(f'{CAM}, 1F pp. 53–54 (CAS 3)'),
  'You try · Edrolo 1G WE2 (CAS)',
  q('The <i>weight</i>, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ <i>weight</i>, rounded to two decimal places.') + '<div class="data">80 95 85 91 102 93 87 78 84 90</div>'
  + lines(2, 'x̄ = 88.50 kg · s<sub>x</sub> = 7.230… → 7.23 kg') + cite(f'{EDR} · 1G Worked example 2')))

MAM = [('okapi', '250'), ('gorilla', '210'), ('pig', '190'), ('Brazilian tapir', '160'), ('jaguar', '100'), ('grey seal', '85'), ('giant armadillo', '60'), ('sheep', '56'), ('chimpanzee', '52'), ('kangaroo', '35'), ('goat', '28'), ('roedeer', '15'), ('baboon', '11'), ('rhesus monkey', '6.8'), ('raccoon', '4.3'), ('red fox', '4.2'), ('cat', '3.3'), ('echidna', '3.0'), ('rabbit', '2.5')]
mt = table([['Mammal', 'Body weight (kg)']] + [list(r) for r in MAM], cls='t tiny')
ORANG = table([['body density (kg/litre)', '1.07', '1.07', '1.08', '1.08', '1.03', '1.05', '1.07', '1.06', '1.07', '1.09', '1.02', '1.09'], ['weight (kg)', '70.1', '90.4', '73.2', '85.0', '84.3', '95.6', '71.7', '95.0', '80.2', '87.4', '94.9', '65.3']], head=False, style='font-size:8pt')
ex = (q('<b>1.</b> The <i>body density</i>, in kilograms per litre, and <i>weight</i>, in kilograms, of a sample of 12 orangutans are shown in the table.') + ORANG
      + q('For these 12 orangutans, determine the mean of their <i>body density</i>, in kilograms per litre. <i>(1 mark)</i>') + lines(1, '12.78 ÷ 12 = 1.065 kg/litre (rounding did not apply: 1.07 was not accepted)')
      + guess('77%', mcq=False) + cite(f'{EDR} · 1G Q11 · Adapted from VCAA 2020 Exam 2 Data analysis Q4aii')
      + item('2', q('<b>2.</b> The table below displays the typical body weight, in kilograms, for a sample of 19 different mammals.')
             + q('<b>b.</b> Complete the five-number summary in the table below for the variable <i>body weight</i>, in kilograms, by writing in the values for the minimum and the median. <i>(2 marks)</i>')
             + table([['Minimum', 'Q<sub>1</sub>', 'Median', 'Q<sub>3</sub>', 'Maximum'], fillrow(['2.5']) + ['4.3'] + fillrow(['35']) + ['100', '250']])
             + q('<b>d.</b> The mean body weight is 67 kg, rounded to the nearest whole number.<br>Explain why the median is a better measure of the centre of the body weight data than the mean. <i>(1 mark)</i>')
             + lines(3, 'The data is (positively) skewed and/or has an outlier, so the mean is pulled above most values; the median is not affected.'), mt)
      + guess('NHT: answers only', mcq=False) + cite('VCAA 2026 NHT General Mathematics Exam 2 Q1b, Q1d'))
P.append(box('Exit tasks', ex, 'Show what you know', cls='split'))
P.append(checklist(['I can find the median value in a data set.', 'I can find the median value from a dot plot.', 'I can find the median value from a stem plot.', 'I can find the range from a stem plot.',
  'I can find the IQR from a stem plot when n is even.', 'I can find the IQR from a stem plot when n is odd.', 'I can calculate the mean using the formula.', 'I can calculate the mean and standard deviation using the CAS calculator.']))
P.append(coursework([('Exercise 1F (part 1)', 'Q1–2 · Q3 · Q4 · Q5<br>Q6–9 · Q10–11'), ('Exercise 1F (part 2)', 'Q12–17 · Q18–20<br>Q21–22 <i>(CAS)</i><br>Q23–26 <i>(Exam 1 style)</i>')], '1F section'))
build('1F', 'Measures of centre and spread', P, 'S3')
