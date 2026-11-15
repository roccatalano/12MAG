"""Lesson 2 (1C-1E) guided worksheet, S1/S4 house style. Question text copied verbatim from lessons/S2-slides.html (which copied it from the sources).
Run: python3 tools/deck/s2/worksheet.py -> lessons/S2-worksheet(.html/.pdf) + lessons/S2-worksheet-solutions(.html/.pdf)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from wslib import *

P = [title('1C–1E', 'Displaying and describing numerical data; log scales', 'Chapter 1 · 1C, 1D, 1E')]
P.append(lis(['To be able to construct frequency tables for discrete numerical data.', 'To be able to construct frequency tables for grouped numerical data (discrete and continuous).',
  'To be able to construct a histogram from a frequency table for numerical data.', 'To be able to construct a histogram from numerical data using a CAS calculator.',
  'To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.',
  'To be able to construct a dot plot for numerical data.', 'To be able to construct a stem plot for numerical data.',
  'To be able to revise the concept of log<sub>10</sub> <i>x</i>.', 'To be able to investigate the effect of the logarithmic scale on the features of a distribution.']))

# ---- APK
AFL = '266 259 238 227 210 160 160 159 155 145 133<br>99 91 80 80 75 73 58 42 36 32 25<br>32 25 25 21 17 13 10 9 9 4 2'
PARTY = '19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29'
apk = (item('1', q('The following data gives the number of games played in total by each member of an AFL club:') + f'<div class="data">{AFL}</div>'
          + q('<b>1. a</b> Use a CAS calculator to construct a histogram starting at 0 with column width 20.') + q('<b>b</b> Describe the shape of the histogram of the number of games played (above).')
          + lines(2, 'Positively skewed: most players have played fewer than 100 games; the tail runs out to the right.'),
          hist(0, 20, [7, 7, 2, 2, 4, 0, 1, 3, 2, 0, 1, 2, 1, 1], 8, 2, 'number of games played', draw=False, lab=2), sep=False)
       + cite(f'{CAM12} · Chapter 2 skills checklist, 2C #6 / 2D #7')
       + item('2', q('<b>2.</b> Construct a stem plot of the ages of a group of people at a party:') + f'<div class="data">{PARTY}</div>',
          stemfill([('1', [7, 9, 9, 9]), ('2', [0, 0, 1, 1, 2, 3, 6, 7, 8, 9]), ('3', [4, 4, 7]), ('4', [5]), ('5', [6]), ('6', [6])], 'Key: 1 | 7 = 17', 'age (years)'))
       + cite(f'{CAM12} · Chapter 2 skills checklist, 2D #9')
       + item('3', parts([('3. a', 'Find the log of 592 to two decimal places.', 'log<sub>10</sub>(592) = 2.772… → 2.77'),
                          ('b', 'What is the order of magnitude of 478 000?', '478 000 = 4.78 × 10<sup>5</sup> → 5')], cols=2))
       + cite(f'{CAM12} · Chapter 9 skills checklist, 9D #6, #7'))
P.append(box('Activating prior knowledge', apk, 'Year 11', cls='split'))

# ---- 1C frequency tables
FT = lambda hd, rows, tot: table([hd] + [[a] + fillrow([b, c]) for a, b, c in rows] + [['<b>Total</b>'] + fillrow(tot)])
P.append(pair('Example 6 · Frequency table, discrete data',
  q('The number of bedrooms in each of the 24 properties sold in a certain area over a one month period are as follows:') + '<div class="data">2 3 4 3 3 4 3 4 4 1 3 2 1 2 2 2 4 5 3 4 4 5 3 4</div>'
  + q('Construct a table for these data showing both frequency and percentage frequency, giving the values of the percentage frequency rounded to one decimal place.')
  + FT(['Number of bedrooms', 'Number', '%'], [('1', '2', '8.3'), ('2', '5', '20.8'), ('3', '7', '29.2'), ('4', '8', '33.3'), ('5', '2', '8.3')], ['24', '99.9']) + cite(f'{CAM} · Example 6'),
  'You try · Edrolo 1C WE4',
  q('The height (cm) of 20 plants in a Year 6 science experiment were recorded.') + '<div class="data">32.0 40.2 40.5 45.1 47.0 49.1 50.1 53.7 54.2 55.3<br>56.9 57.2 58.2 67.2 68.9 69.0 72.3 77.6 82.1 88.5</div>'
  + q('Construct a grouped frequency table with intervals of 10.')
  + table([['height (cm)', 'number', '%']] + [fillrow(r) for r in [('30−&lt;40', '1', '5'), ('40−&lt;50', '5', '25'), ('50−&lt;60', '7', '35'), ('60−&lt;70', '3', '15'), ('70−&lt;80', '2', '10'), ('80−&lt;90', '2', '10')]] + [['<b>total</b>'] + fillrow(['20', '100'])])
  + cite(f'{EDR} · 1C Worked example 4')))
P.append(box('Example 7 · Constructing a grouped frequency table',
  '<div class="row"><div style="flex:1">' + q('The data below give the average hours worked per week in 23 countries.') + '<div class="data">35.0 48.0 45.0 43.0 38.2 50.0 39.8 40.7 40.0 50.0 35.4 38.8<br>40.2 45.0 45.0 40.0 43.0 48.8 43.3 53.1 35.6 44.1 34.8</div>'
  + q('Construct a grouped frequency table with five intervals.') + '</div><div style="flex:1">'
  + table([['Average hours worked', 'Number', 'Percentage']] + [fillrow(r) for r in [('30.0−34.9', '1', '4.3'), ('35.0−39.9', '6', '26.1'), ('40.0−44.9', '8', '34.8'), ('45.0−49.9', '5', '21.7'), ('50.0−54.9', '3', '13.0')]] + [['<b>Total</b>'] + fillrow(['23', '99.9'])])
  + '</div></div>' + cite(f'{CAM} · Example 7')))

# ---- histograms
PLANT = table([['height (cm)', 'number', '%'], ['30−&lt;40', '1', '5'], ['40−&lt;50', '5', '25'], ['50−&lt;60', '7', '35'], ['60−&lt;70', '3', '15'], ['70−&lt;80', '2', '10'], ['80−&lt;90', '2', '10'], ['<b>total</b>', '20', '100']], style='font-size:8.5pt')
P.append(pair('Example 8 · Constructing a histogram from a frequency table',
  q('Construct a histogram for the frequency table opposite.') + table([['Average hours worked', 'Frequency'], ['30.0–34.9', '1'], ['35.0–39.9', '6'], ['40.0–44.9', '8'], ['45.0–49.9', '5'], ['50.0–54.9', '3'], ['<b>Total</b>', '23']], style='font-size:8.5pt')
  + hist(25, 5, [0, 1, 6, 8, 5, 3, 0], 9, 1, 'Average hours worked', 'Frequency', draw=False) + cite(f'{CAM} · Example 8'),
  'You try · Edrolo 1C WE5',
  q('The height (cm) of 20 plants in a Year 6 science experiment was recorded in the following grouped frequency table.') + PLANT
  + q('<b>a.</b> Construct a histogram to display this data.') + hist(30, 10, [1, 5, 7, 3, 2, 2], 8, 1, 'height (cm)', draw=False)
  + q('<b>b.</b> What percentage of plants were shorter than 60 cm?') + lines(1, '1 + 5 + 7 = 13; 13 ÷ 20 = 0.65 → 65%') + cite(f'{EDR} · 1C Worked example 5')))
P.append(box('CAS 1 · Histogram from raw data',
  '<div class="row"><div style="flex:1.1">' + q('Display the following set of 27 marks in the form of a histogram (column width 4, starting point 2):') + '<div class="data">16 11 4 25 15 7 14 13 14 12 15 13 16 14<br>15 12 18 22 17 18 23 15 13 17 18 22 23</div>'
  + '<p class="q"><b>TI-Nspire:</b> Lists &amp; Spreadsheet → Data &amp; Statistics → Plot Type › Histogram → Bin Settings: width 4, alignment 2.<br><b>ClassPad:</b> Statistics → SetGraph: Histogram → Set Interval: HStart 2, HStep 4.</p></div>'
  + f'<div class="fig">{hist(2, 4, [1, 1, 6, 11, 3, 5], 12, 2, "marks", draw=False)}</div></div>' + cite(f'{CAM}, 1C pp. 16–20 (CAS 1)')))

# ---- describing
TPL = lambda: (f'<div class="tpl"><b>Shape:</b> {blank("negatively skewed, with a long lower tail", 70)}<br><b>Centre:</b> around {blank("38–39 weeks", 26)}<br>'
               f'<b>Spread:</b> from {blank("25", 10)} to {blank("42 weeks", 18)}; most values in the range {blank("36–41 weeks", 24)}<br><b>Outliers:</b> {blank("values below 34 weeks seem small; outliers can’t be identified from a histogram", 80)}</div>')
P.append(box('Example 9 · Describing the features of a distribution from a histogram',
  '<div class="row"><div style="flex:1">' + q('The histogram shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe this histogram in terms of shape, centre, spread and outliers.') + TPL() + '</div>'
  + f'<div class="fig">{hist(25, 1, [2, 2, 2, 2, 2, 2, 2, 4, 6, 10, 16, 34, 95, 233, 302, 207, 86, 4], 300, 100, "Gestation period (weeks)", "Frequency", lab=2)}</div></div>' + cite(f'{CAM} · Example 9')))

# ---- 1D dot and stem plots
P.append(pair('Example 10 · Constructing a dot plot',
  q('The ages (in years) of the 13 members of a cricket team are:') + '<div class="data">22 19 18 19 23 25 22 29 18 22 23 24 22</div>' + q('Construct a dot plot.')
  + axis_svg(17, 30, 1, 1, 'Age (years)', body=lambda s, y: '<g class="solfig">' + ''.join(f'<circle cx="{s(v):.1f}" cy="{y-5-k*9}" r="4" fill="none" stroke="#c00"/>' for v, f in {18: 2, 19: 2, 22: 4, 23: 2, 24: 1, 25: 1, 29: 1}.items() for k in range(f)) + '</g>', top=12)
  + cite(f'{CAM} · Example 10'),
  'You try · Edrolo 1C WE1',
  q('Sophie surveyed 12 of the families living on her street. She asked for the number of pets each of them owned and the results were recorded.') + '<div class="data">3 2 0 1 1 3 0 5 2 1 1 2</div>'
  + q('<b>a.</b> Construct a dot plot to display this data.')
  + axis_svg(0, 5, 1, 1, 'number of pets', body=lambda s, y: '<g class="solfig">' + ''.join(f'<circle cx="{s(v):.1f}" cy="{y-5-k*9}" r="4" fill="none" stroke="#c00"/>' for v, f in {0: 2, 1: 4, 2: 3, 3: 2, 5: 1}.items() for k in range(f)) + '</g>', top=12)
  + q('<b>b.</b> What was the modal number of pets owned by families that Sophie surveyed?') + lines(1, '1 pet (the most dots)') + cite(f'{EDR} · 1C Worked example 1')))
P.append(pair('Example 11 · Constructing a stem plot',
  q('University participation rates (%) in 23 countries are given below.') + '<div class="data">26 3 12 20 36 1 25 26 13 9 26 27<br>15 21 7 8 22 3 37 17 55 30 1</div>' + q('Display the data in the form of a stem plot.')
  + stemfill([('0', [1, 1, 3, 3, 7, 8, 9]), ('1', [2, 3, 5, 7]), ('2', [0, 1, 2, 5, 6, 6, 6, 7]), ('3', [0, 6, 7]), ('4', []), ('5', [5])], 'Key: 1 | 2 = 12', 'rate (%)') + cite(f'{CAM} · Example 11'),
  'You try · Edrolo 1C WE2',
  q('Ms Smyth’s maths class of 25 students sat their end-of-year exam. Their results (%) were recorded.') + '<div class="data">55 68 76 90 83 89 75 66 59 84 48 62 58<br>95 80 77 61 92 99 63 84 65 70 81 96</div>'
  + q('<b>a.</b> Construct a stem plot to display this data.') + stemfill([('4', [8]), ('5', [5, 8, 9]), ('6', [1, 2, 3, 5, 6, 8]), ('7', [0, 5, 6, 7]), ('8', [0, 1, 3, 4, 4, 9]), ('9', [0, 2, 5, 6, 9])], 'Key: 4 | 8 = 48%', 'exam result (%)')
  + q('<b>b.</b> How many students scored above 70% on the exam?') + lines(1, '7 | 5 6 7 and every leaf on stems 8 and 9: 14 students') + cite(f'{EDR} · 1C Worked example 2')))

# ---- 1E logs
P.append(pair('Example 12 · Using a CAS calculator to find logs',
  parts([('a', 'Find the log of 45, correct to two significant figures.', 'log 45 = 1.65… = 1.7'), ('b', 'Find the number with log equal to 2.7125, correct to the nearest whole number.', '10<sup>2.7125</sup> = 515.82… = 516')]) + cite(f'{CAM} · Example 12'),
  'You try · Edrolo 1D WE1',
  q('Use log<sub>10</sub> for the following calculations.') + parts([('a.', 'Calculate the log of 23, correct to two decimal places.', 'log<sub>10</sub>(23) = 1.361… → 1.36'), ('b.', 'If the log of a number is 5, what is the number?', '10<sup>5</sup> = 100 000')]) + cite(f'{EDR} · 1D Worked example 1')))
P.append(pair('Example 13 · Interpreting a histogram with a log scale',
  q('The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.') + hist(-2, 1, [3.7, 7.4, 18.5, 25.9, 25.9, 11.1, 7.4], 28, 4, 'log(body weight)', 'Percentage', pct=True)
  + parts([('a', 'What body weight (in kg) is represented by the number 4 on the log scale?', '10<sup>4</sup> = 10 000 kg'), ('b', 'How many of these animals have body weights more than 10 000 kg?', 'bars above 4: two animals'),
           ('c', 'The weight of a cat is 3.3 kg. Use your calculator to determine the log of its weight correct to two significant figures.', 'log 3.3 = 0.518… = 0.52'),
           ('d', 'Determine the weight (in kg) of the animal with a log(body weight) of 3.4 (the elephant). Write your answer correct to the nearest whole number.', '10<sup>3.4</sup> = 2511.88… = 2512 kg')]) + cite(f'{CAM} · Example 13'),
  'You try · Edrolo 1D WE3',
  q('A class of twenty students were asked about the <i>distance</i>, in kilometres, from their home to the school. The results were summarised in a histogram using a log<sub>10</sub> scale.')
  + hist(-1, .5, [2, 3, 3, 5, 6, 1], 8, 2, 'log₁₀(distance)', dec=1)
  + parts([('a.', 'Jane was away the day of the survey. It is known that she lives 9.5 km away from school. Which interval on the histogram reflects this?', 'log<sub>10</sub>(9.5) = 0.977… → 0.5–&lt;1.0'),
           ('b.', 'How many students live more than 10 km away from school?', 'log<sub>10</sub>(10) = 1; columns above 1: 6 + 1 = 7 students')]) + cite(f'{EDR} · 1D Worked example 3')))

# ---- exits
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
nv = [k for k, f in neck.items() for _ in range(f)]
temp = stem([('2', [2, 4, 4]), ('2', [5, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]), ('3', [1, 2, 3, 3, 4, 4, 4]), ('3', [5, 6, 7, 7, 7, 7]), ('4', [1])], 'Key: 2 | 2 = 2.2 °C')
ex = (item('1', q('<b>1.</b> The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.') + q('Write down the modal <i>neck size</i>, in centimetres, for these 250 men. <i>(1 mark)</i>') + lines(1, '38 cm'),
           dotplot(30, 45, nv, 'neck size (cm)', r=1.15, W=300), sep=False)
      + guess('93%', mcq=False) + cite(f'{EDR} · 1C Q16 · VCAA 2020 Exam 2 Data analysis Q2a')
      + item('2', q('<b>2.</b> The following stem plot displays 30 temperatures recorded at a weather station.') + q('The modal temperature is') + mc(['2.8 °C', '2.9 °C', '3.7 °C', '8.0 °C', '9.0 °C'], cols=3) + ans('A: the leaf 8 appears six times on a 2 stem.'), temp)
      + guess('87% · B') + cite(f'{EDR} · 1C Q18 · VCAA 2016 Exam 1 Data analysis Q3')
      + item('3', q('<b>3.</b> The following histogram shows the <i>population size</i> for 48 countries plotted on a log<sub>10</sub> scale.') + q('Based on this histogram, the number of countries with a <i>population size</i> that is less than 100 000 people is')
             + mc(['1', '5', '7', '8', '48'], cols=5) + ans('D: 100 000 = 10<sup>5</sup>, so 5 on the log scale. Columns below 5: 1 + 7 = 8.'),
             hist(0, 1, [0, 0, 1, 0, 7, 5, 21, 13, 1, 0], 25, 5, 'log₁₀(population size)'))
      + guess('71% · none stands out') + cite(f'{EDR} · 1D Q13 · VCAA 2019 Exam 1 Data analysis Q3'))
P.append(box('Exit tasks', ex, 'Show what you know', cls='split'))

P.append(checklist(['I can construct a frequency table for discrete numerical data.', 'I can construct a grouped frequency table.', 'I can construct a histogram from a grouped frequency table.',
  'I can describe the features of a distribution from a histogram.', 'I can construct a dot plot.', 'I can construct a stem plot.', 'I can use a CAS calculator to find logs.', 'I can interpret a histogram with a log scale.']))
P.append(coursework([('Exercise 1C', 'Q1–2 · Q3 · Q4 · Q5–6<br>Q7–8 <i>(CAS)</i> · Q9–10<br>Q11–12 <i>(Exam 1 style)</i>'), ('Exercise 1D', 'Q1–5 · Q6 · Q7 · Q8–9<br>Q10–11 <i>(Exam 1 style)</i>'), ('Exercise 1E', 'Q1 · Q2 · Q3 · Q4<br>Q5–6 <i>(Exam 1 style)</i>')], '1C, 1D and 1E sections'))
build('1C–1E', 'Displaying and describing numerical data; log scales', P, 'S2')
