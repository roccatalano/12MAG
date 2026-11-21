"""Lesson l04 (2C) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l04/build.py.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 2I Now try this 27 (skills checklist 2I #16); APK 2 = VCAA 2019 Further Exam 2 Core Q2aii (Edrolo U1&2 1H Q16);
APK 3 = VCAA 2021 Further Exam 1 Core Q4 (Edrolo U1&2 1H Q17). Examples 9-12 = Cambridge U3&4 Examples 9-12 (pp. 123-127).
You try 9-12 = Edrolo U3&4 2B WE2, WE1, WE3, WE4. Exits = Edrolo U3&4 2B Q11 (VCAA 2016 Exam 1 Core Q8), Q12 (VCAA 2019 Exam 2 Core Q3), Q13 (VCAA 2017 Exam 2 Core Q2e).
Figures redrawn (values in tools/deck/l04/figs.py). Output: lessons/2C worksheet(.html/.pdf) + lessons/2C worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l04/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import pbox, pdot, EX9, EX10, EX11, EX12, YT1, YT2, YT3, YT4, NT27, V19Q2, V21Q4, V19Q3, V17

def fig(svg, mm): return f'<div style="max-width:{mm}mm;margin:1mm auto">{svg}</div>'
def BX(rows, lo, hi, step, xl, mm, W=520, rowH=40, lab=90, red=False, **k):
    return fig(pbox(rows, lo, hi, step, xl, W=W, rowH=rowH, fs=13, lab=lab, ink=RED if red else '#000', fill='none' if red else '#e6e6e6', sw=1.4, out_r=4, **k), mm)
def DT(groups, lo, hi, step, xl, mm, W=520, gh=56, red=False):
    return fig(pdot(groups, lo, hi, step, xl, W=W, gh=gh, fs=13, r=4.5, ink=RED if red else '#000'), mm)
def BB(stems, left, right, lh, rh, kl='', kr='', title='', red=False):
    c = f' style="color:{RED}"' if red else ''
    tr = ''.join(f'<tr><td style="text-align:right;padding:0 2mm">{" ".join(left[i])}</td><td style="border-left:1px solid #000;border-right:1px solid #000;padding:0 1.5mm;font-weight:bold">{s}</td><td style="padding:0 2mm">{" ".join(right[i])}</td></tr>' for i, s in enumerate(stems))
    cap = (f'<div style="text-align:center;font-style:italic">{title}</div>' if title else '') + (f'<div style="display:flex;justify-content:space-between;font-size:8pt"><span>{kl}</span><span>{kr}</span></div>' if kl or kr else '')
    return f'<div{c} style="display:table;margin:1mm auto;font-size:9.5pt{";color:"+RED if red else ""}">{cap}<table style="border-collapse:collapse;margin:0 auto"><tr><th style="text-align:right;padding:0 2mm">{lh}</th><th></th><th style="text-align:left;padding:0 2mm">{rh}</th></tr>{tr}</table></div>'
def side(left, f, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{f}</div></div>'

P = [title('2C', 'Investigating the association between a numerical and a categorical variable')]
P.append(lis(['To be able to use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable for small data sets.',
  'To be able to use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable for small data sets.',
  'To be able to use parallel boxplots to display the association between a numerical variable and a categorical variable which can take two or more values.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
st, l, r = NT27
P.append(box('Question 1', side(q('The following back-to-back stem plot displays the distributions of the number of hours per week spent relaxing by a group of 17 males and 16 females.')
      + q('Use the back-to-back stem plot and the summary statistics provided to compare these distributions in terms of centre and spread, and draw an appropriate conclusion.'),
      BB(st, l, r, 'Males', 'Females', '1|2 = 21 hours', '1|6 = 16 hours', 'Number of hours per week spent relaxing')
      + '<div style="display:flex;justify-content:space-around;font-size:8.5pt"><span>M = 30 hours<br>IQR = 14.5 hours</span><span>M = 24.5 hours<br>IQR = 19 hours</span></div>', 80)
  + space(22, 'The median time spent relaxing for males (M = 30 hours) was higher than for females (M = 24.5 hours). The spread for males (IQR = 14.5 hours) was lower than for females (IQR = 19 hours). In conclusion, the males spent more time relaxing than the females, and their times were less variable.')))
P.append(pair(
  box('Question 2 · VCAA 2019 Exam 2 Q2aii', q('The parallel boxplots below show the <i>maximum daily temperature</i> and <i>minimum daily temperature</i>, in degrees Celsius, for 30 days in November 2017.')
      + BX([('', *V19Q2[0][1:])], 6, 30, 2, 'maximum daily temperature (°C)', 78, lab=10, rowH=34) + BX([('', *V19Q2[1][1:])], 6, 30, 2, 'minimum daily temperature (°C)', 78, lab=10, rowH=34)
      + q('Use the information in the boxplots to complete the following sentence.<br>For November 2017, the median value for <i>maximum daily temperature</i> was ______ °C higher than the median value for <i>minimum daily temperature</i>.')
      + space(8, '25 − 15 = 10 °C'), '1 mark'),
  box('Question 3 · VCAA 2021 Exam 1 Q4', q('The boxplots below show the distribution of the length of fish caught in two different ponds, Pond A and Pond B.')
      + BX(V21Q4, 0, 12, 0.5, 'length', 62, lab=60, rowH=34, ticks=False, grid=True) + q('Based on the boxplots above, it can be said that')
      + mc(['50% of the fish caught in Pond A are the same length as the fish caught in Pond B.', '50% of the fish caught in Pond B are longer than all of the fish caught in Pond A.',
            '50% of the fish caught in Pond B are shorter than all of the fish caught in Pond A.', '75% of the fish caught in Pond A are shorter than all of the fish caught in Pond B.',
            '75% of the fish caught in Pond B are longer than all of the fish caught in Pond A.'], 'B')
      + why('Pond B’s median is beyond Pond A’s maximum, so the top 50% of Pond B are longer than every fish in Pond A.'), '1 mark')))

# ---------------------------------------------------------------- 2C
P.append(sect('2C Investigating the association between a numerical and a categorical variable', 'Example, then you try'))
P.append(exyt('Example 9 · Parallel dot plots', q('The parallel dot plots below display the distribution of the number of sit-ups performed by 15 people before and after they had completed a gym program.')
      + DT([('Number of sit-ups before gym program', EX9[0][1]), ('Number of sit-ups after gym program', EX9[1][1])], 22, 54, 2, '', 88, gh=60)
      + q('Do the parallel dot plots support the contention that the number of sit-ups performed is associated with completing the gym program? Write a brief explanation that compares the distributions.')
      + report(['Centre: The median number of sit-ups performed after attending the gym program (M = ', ('median', '32'), ') is ', ('higher / lower', 'higher'), ' than the median number of sit-ups performed before attending the gym program (M = ', ('median', '26'), '). ',
                'Spread: The variability in the number of sit-ups has also ', ('increased / decreased', 'increased'), ' from IQR = ', ('IQR', '6'), ' to IQR = ', ('IQR', '10'), '. ',
                'Thus we can conclude that the number of sit-ups performed ', ('is / is not', 'is'), ' associated with completing the gym program.']),
  'You try 9', q('A grade 5/6 class took a maths test on fractions. The <i>number of marks</i>, by grade, was recorded.<br>Grade 5: &nbsp;2 &nbsp;4 &nbsp;5 &nbsp;5 &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;7 &nbsp;9<br>Grade 6: &nbsp;5 &nbsp;6 &nbsp;6 &nbsp;7 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;8 &nbsp;9 &nbsp;9 &nbsp;9 &nbsp;10')
      + parts([('a', 'Construct parallel dot plots to display this data.', DT(YT2, 2, 10, 1, 'number of marks', 70, gh=50, red=True), 42),
               ('b', 'Which grade has a larger range of <i>number of marks</i>?', 'Grade 5 (9 − 2 = 7 marks; Grade 6: 10 − 5 = 5 marks)', 'L')])))
st, l, r = EX10; st2, l2, r2 = YT1
P.append(exyt('Example 10 · Back-to-back stem plots', q('The back-to-back stem plot below displays the distribution of life expectancy (in years) for the same 13 countries in 1970 and 2010.')
      + BB(st, l, r, '1970', '2010', '2|5 = 52 years', '6|7 = 67 years')
      + q('Do the back-to-back stem plots support the contention that life expectancy has changed between these two time periods?')
      + report(['Centre: The median life expectancy has increased between 1970 and 2010, from M = ', ('median', '67'), ' years to M = ', ('median', '76'), ' years. ',
                'Spread: Over the same period life expectancy has also become ', ('more / less', 'less'), ' variable (IQR in 1970 = ', ('IQR', '12.5'), ' years; IQR in 2010 = ', ('IQR', '8'), ' years). ',
                'There ', ('is / is not', 'is'), ' an association between year and life expectancy.']),
  'You try 10', q('The ‘Abbotsford Avengers’ soccer team beat the ‘East Melbourne Eagles’ in the final. In order for the ‘East Melbourne Eagles’ to see what they needed to improve on, they collected the <i>successful passes</i> (%) for each member of both teams.<br>Abbotsford Avengers: &nbsp;64 &nbsp;68 &nbsp;70 &nbsp;53 &nbsp;57 &nbsp;62 &nbsp;74 &nbsp;77 &nbsp;36 &nbsp;41 &nbsp;66<br>East Melbourne Eagles: &nbsp;59 &nbsp;90 &nbsp;83 &nbsp;87 &nbsp;88 &nbsp;76 &nbsp;82 &nbsp;83 &nbsp;91 &nbsp;78 &nbsp;75')
      + parts([('a', 'Construct a back-to-back stem plot to display this data, with the ‘Abbotsford Avengers’ on the left.', BB(st2, l2, r2, 'Abbotsford Avengers', 'East Melbourne Eagles', 'Key: 5 | 9 = 59%', '', red=True), 40),
               ('b', 'Which team had a higher median <i>successful passes</i>?', 'East Melbourne Eagles (83%, Avengers 64%)', 'L')])))
P.append(exyt('Example 11 · Parallel boxplots, two groups', q('Use the following parallel boxplots to compare the pulse rates (in beats/minute) for a group of 70 male students and 90 female students.')
      + BX(EX11, 40, 120, 10, 'Resting pulse rate', 86, lab=60, rowH=36, minor=5)
      + report(['Shape: The distributions of resting pulse rates for both male and female students were approximately ', ('shape', 'symmetric'), '. ',
                'Outliers: One male was found to have an extremely low pulse rate of ', ('value', '40'), ', while another had an extremely high pulse rate of ', ('value', '120'), '. ',
                'Centre: On average, the resting pulse rate for males is lower (median: male = ', ('M', '65'), ', female = ', ('M', '72'), ') ',
                'Spread: and less variable than that for females (IQR: male = ', ('IQR', '10'), ', female = ', ('IQR', '15'), '). ',
                'There ', ('is / is not', 'is'), ' an association between resting pulse rate and gender.']),
  'You try 11', q('Daniel went to his local cafe every Sunday for a year and counted the number of people wearing Salomon shoes and the number of people wearing Crocs. The five-number summaries for both shoe brands are recorded.<br>Salomons: 2, 4, 5, 9, 15<br>Crocs: 0, 2, 4, 7, 8')
      + parts([('a', 'Construct parallel boxplots to display this data.', BX(YT3, 0, 15, 1, 'number of people', 74, lab=70, rowH=36, red=True), 34),
               ('b', 'For which shoe brand was the <i>number of people</i> positively skewed?', 'Salomons', 'L')])))
P.append(exyt('Example 12 · Parallel boxplots, more than two groups', q('Use the parallel boxplots below to compare the salary distribution for workers in a certain industry across four different age groups: 20–29 years, 30–39 years, 40–49 years and 50–65 years.')
      + BX(EX12, 40, 140, 10, 'Salary ($’000)', 86, lab=105, rowH=30, minor=2)
      + report(['Shape: The shape of the distribution of salaries changes with age group, from ', ('shape', 'symmetric'), ' for 20−29-year-olds, to progressively more ', ('shape', 'positively skewed'), ' as age increases. ',
                'Outliers: There are no outliers in the 20-29 and 30-39 age group. Outliers also begin to appear at ', ('value', '$110 000'), ' for the 40-49 age group, and at ', ('values', '$119 000, $126 000 and $140 000'), ' for the 50-65 age group. ',
                'Centre: The median salaries increase across the age groups, from ', ('median', '$64 000'), ' for 20−29 year-olds to ', ('median', '$72 000'), ' for 50−65 year-olds. ',
                'Spread: The salaries also became more variable, with the IQR increasing from around ', ('IQR', '$12 000'), ' for 20−29-year-olds to around ', ('IQR', '$20 000'), ' for 50−65-year-olds. ',
                'In this industry there ', ('is / is not', 'is'), ' an association between salary and age group.']),
  'You try 12', q('The following parallel boxplots display the distribution of prices for a 3-bedroom house in three different locations in NSW: ‘rural’, ‘outer suburbs’ and ‘inner suburbs’.')
      + BX(YT4, 0, 2.4, 0.2, 'price ($000 000’s)', 86, lab=115, rowH=32, minor=0.1)
      + q('Identify the association between <i>price</i> and <i>location</i>.<br>Write a report referencing shape, centre and spread.')
      + space(48, 'The parallel boxplots show that price and location are associated. The closer a 3-bedroom house is to a city in NSW, the higher the price of the house. In relation to shape, the distribution of price is positively skewed in locations further from a city in NSW and approximately symmetrical in the inner suburbs. In relation to centre, the median price increases as the location is closer to a city in NSW. In relation to spread, the range and IQR of price tends to be larger in locations closer to a city in NSW.', grow=True)))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2016 Exam 1 Q8', q('Parallel boxplots would be an appropriate graphical tool to investigate the association between the monthly median rainfall, in millimetres, and the')
  + mc(['monthly median wind speed, in kilometres per hour.', 'monthly median temperature, in degrees Celsius.', 'month of the year (January, February, March, etc.).', 'monthly sunshine time, in hours.', 'annual rainfall, in millimetres.'], 'C')
  + why('Rainfall is numerical, so the other variable must be categorical: only month of the year is.'), '1 mark'))
T2 = table([['<i>Month</i>', 'Minimum', 'Q<sub>1</sub>', 'Median', 'Q<sub>3</sub>', 'Maximum'], ['February', '5.9', '9.5', '10.9', '13.9', '22.2'], ['May', '3.3', '6.0', '7.5', '9.8', '12.7'], ['July', '1.6', '3.7', '5.0', '5.9', '7.7']], cls='t tiny')
P.append(box('Exit task 2 · VCAA 2019 Exam 2 Q3', q('The five-number summary for the distribution of <i>minimum daily temperature</i> for the months of February, May and July in 2017 is shown in Table 2.<br>The associated boxplots are shown below the table.')
  + side('<div style="font-size:8.5pt;font-weight:bold">Table 2. Five-number summary for <i>minimum daily temperature</i></div>' + T2, BX(V19Q3, 0, 24, 4, 'minimum daily temperature (°C)', 84, lab=80, rowH=28), 86)
  + q('Explain why the information given above supports the contention that <i>minimum daily temperature</i> is associated with the <i>month</i>. Refer to the values of an appropriate statistic in your response.')
  + space(20, 'The median minimum daily temperature decreases from February (10.9 °C) to May (7.5 °C) to July (5.0 °C). Because the median changes with the month, minimum daily temperature is associated with month.'), '2 marks'))
st, l, r = V17
P.append(box('Exit task 3 · VCAA 2017 Exam 2 Q2e', side(q('The back-to-back stem plot below displays the <i>wingspan</i>, in millimetres, of 32 moths and their <i>place of capture</i> (forest or grassland).')
      + q('The back-to-back stem plot suggests that <i>wingspan</i> is associated with <i>place of capture</i>.<br>Explain why, quoting the values of an appropriate statistic.'),
      BB(st, l, r, 'forest (<i>n</i> = 13)', 'grassland (<i>n</i> = 19)', 'key: 1|8 = 18', '', '<i>wingspan</i> (mm)'), 72)
  + space(18, 'The median wingspan of moths captured in the grassland (30 mm) is higher than that of moths captured in the forest (21 mm). The medians differ, so wingspan is associated with place of capture.'), '2 marks'))

SC = ['I can use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable.',
      'I can use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable.',
      'I can use parallel boxplots to display and describe the association between a numerical variable and a categorical variable.']
P.append(close(SC, [('2C', 'Q1–10')], ['2C']))
if WB: P.append(practice(['2C']))  # workbook edition only: practice sections (Insight + Cambridge skill sheets) flow on after the exits
build('l04', '2C', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (() if WB else (('l04-worksheet', '2C worksheet'), ('l04-worksheet-solutions', '2C worksheet solutions'))):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
