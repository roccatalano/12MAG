"""Lesson 1 (1A-1B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim from tools/deck/s1/build.py (verbatim-checked 15 Nov).
Sources (not printed, Rocco 15 Nov: only exam questions show their source): APK 1 = Cambridge U1&2 Ch 2 skills checklist 2A #1; APK 2 = Edrolo U1&2 1A Q13; APK 3 = Edrolo U1&2 1A Q14;
Examples 1-5 = Cambridge U3&4 Examples 1-5; You try 1 = Edrolo U3&4 1A WE1-3; You try 2-5 = Edrolo U3&4 1B WE1-4; exits = Edrolo U3&4 1A Q14, 1A Q16, 1B Q13.
Run: python3 tools/deck/s1/worksheet.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *

P = [title('1A–1B', 'Types of data and categorical data')]
P.append(lis(['To be able to classify data as categorical or numerical.', 'To be able to further classify categorical data as nominal or ordinal.',
  'To be able to further classify numerical data as discrete or continuous.', 'To be able to construct frequency and percentage frequency tables for categorical data.',
  'To be able to construct bar charts and percentage bar charts from frequency tables.', 'To be able to interpret and describe frequency tables and bar charts.',
  'To be able to answer statistical questions about a categorical variable.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Classify the following data as nominal, ordinal, discrete or continuous:')
  + parts([('a', 'The time between people arriving at the coffee shop.', 'continuous', 4), ('b', 'The number of people in the queue at the coffee shop.', 'discrete', 6),
           ('c', 'Customer’s coffee preference (latte, cappuccino, black).', 'nominal', 6), ('d', 'Customer’s rating of the coffee (excellent, quite good, not that good).', 'ordinal', 6)], cols=4)))
TRAVEL = segbar(None, ['domestic', 'international'], 100, 20, 'percentage', 'age', bars=[('under 55', [65, 35]), ('55 and over', [45, 55])], W=230, H=140, mm=58)
NIGHT = ('<table class="t"><tr><th></th><th colspan="2"><i>snores</i></th><th></th></tr><tr><th><i>frequency of nightmares</i></th><th>no</th><th>yes</th><th>total</th></tr>'
         '<tr><td class="l">low</td><td>80</td><td>58</td><td>138</td></tr><tr><td class="l">high</td><td>11</td><td>12</td><td>23</td></tr><tr><td class="l">total</td><td>91</td><td>70</td><td>161</td></tr></table>')
def side(left, fig, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{fig}</div></div>'
P.append(box('Question 2', side(q('The percentage segmented bar chart provided shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).')
      + q('The variables <i>age</i> (under 55 years, 55 years and over) and <i>preferred travel destination</i> (domestic, international) are')
      + mc(['both categorical variables.', 'both numerical variables.', 'a numerical variable and a categorical variable respectively.', 'a categorical variable and a numerical variable respectively.', 'a discrete variable and a continuous variable respectively.'], 'A')
      + why('Age is recorded in two groups, not as a number of years, so it is categorical.'), TRAVEL, 58) + guess('70% · C (21%)') + src('VCAA 2021 Exam 1 Q1'), '1 mark'))
P.append(box('Question 3', side(q('The data in the table shown was collected in a study of the association between the variables <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes).')
      + q('The variables in this study, <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes), are')
      + mc(['ordinal and nominal respectively.', 'nominal and ordinal respectively.', 'both numerical.', 'both ordinal.', 'both nominal.'], 'A', cols=2)
      + why('Low and high have a natural order (ordinal); no and yes only name a group (nominal).'), NIGHT, 62) + guess('57% · D (24%)') + src('VCAA 2020 Exam 1 Q10'), '1 mark'))

# ---------------------------------------------------------------- 1A
P.append(sect('1A Types of data', 'Example, then you try'))
P.append(box('Example 1 · Types of data', q('Classify the following data as nominal, ordinal, discrete or continuous.')
      + parts([('a', 'The number of chocolate chips in each of 10 cookies is counted.', 'discrete', 5), ('b', 'The time taken for 20 students to complete a puzzle is recorded in seconds.', 'continuous', 5),
               ('c', 'Member of a football club were asked to rate how they felt about the current coach, 1 = Very satisfied, 2 = Satisfied, 3 = Indifferent, 4 = Dissatisfied, 5 = Very dissatisfied.', 'ordinal', 5),
               ('d', 'Students are asked to each choose their preferred colour from the list 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow.', 'nominal', 5),
               ('e', 'Students weights were classified as ‘less than 60kg’, ‘60kg - 80kg’ or ‘more than 80kg’.', 'ordinal', 5)], cols=2)))
G3 = lambda n, t, items: f'<div><p class="q"><b>{n}</b> {t}</p>' + parts(items) + '</div>'
P.append(box('You try 1', '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4mm">'
      + G3(1, 'Classify the following variables as either categorical or numerical.', [('a.', '<i>type of pasta</i>', 'categorical', 5), ('b.', '<i>number of candles</i>', 'numerical', 5)])
      + G3(2, 'Classify the following categorical variables as either nominal or ordinal.', [('a.', '<i>type of shoe</i> (runners, boots, sandals, slides)', 'nominal', 5), ('b.', '<i>shirt size</i> (small, medium, large)', 'ordinal', 5)])
      + G3(3, 'Classify the following numerical variables as either discrete or continuous.', [('a.', '<i>length</i> (m)', 'continuous', 5), ('b.', '<i>number of tennis racquets</i>', 'discrete', 5)]) + '</div>'))

# ---------------------------------------------------------------- 1B
P.append(sect('1B Displaying and describing categorical data', 'Example, then you try'))
TH = 'average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'
P.append(pair(
  box('Example 2 · Frequency table for a categorical variable', q('A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):')
      + '<div class="data">C V V C C V C C C V V</div>' + q('Construct a frequency table (including percentage frequencies) to display the data.')
      + ftab('Flavour', [('chocolate', 6, '54.5'), ('vanilla', 5, '45.5')], (11, '100.0'))),
  box('You try 2', q('The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:')
      + f'<div class="data" style="font-family:inherit;font-size:8.8pt">{TH}</div>'
      + q('Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.')
      + ftab('teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), pcth='%'))))

CLIM = ftab('Climate type', [('Cold', 3, '13.0'), ('Mild', 14, '60.9'), ('Hot', 6, '26.1')], (23, '100.0'), blank=False)
THT = ftab('teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), blank=False, pcth='%')
TQ = '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.'
P.append(pair(
  box('Example 3 · Constructing a bar chart from a frequency table', q('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.') + CLIM
      + parts([('a', 'What is the level of measurement of the variable <i>climate type</i>?', 'Ordinal: cold, mild, hot have a natural order of warmth.', 7),
               ('b', 'Construct a frequency bar chart to display this information.' + barchart(['Cold', 'Mild', 'Hot'], [3, 14, 6], 15, 5, 'Climate type', 'Frequency', draw=False, H=100, mm=56), '', 0)])),
  box('You try 3', q(TQ) + THT + q('Use the frequency table to construct a frequency bar chart.')
      + barchart(['short', 'average', 'tall'], [6, 10, 8], 10, 2, 'teacher’s height', 'frequency', draw=False, H=100, mm=56))))

P.append(pair(
  box('Example 4 · Constructing a percentage segmented bar chart', q('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. <i>(Table: see Example 3.)</i>')
      + q('Construct a percentage frequency segmented bar chart to display this information.')
      + '<div class="row"><div style="flex:1">' + segbar([13.0, 60.9, 26.1], ['Cold', 'Mild', 'Hot'], 100, 10, 'Percentage', draw=False, W=180, H=165, mm=48) + '</div>'
      + '<div style="flex:1">' + space(30, 'Cold: 0 to 13.0<br>Mild: 13.0 to 13.0 + 60.9 = 73.9<br>Hot: 73.9 to 100') + '</div></div>'),
  box('You try 4', q(TQ + ' <i>(Table: see You try 3.)</i>')
      + parts([('a.', 'Use the frequency table to construct a segmented bar chart.', '', 0), ('b.', 'Use the frequency table to construct a percentage segmented bar chart.', '', 0)])
      + '<div class="row"><div style="flex:1"><b>a.</b>' + segbar([6, 10, 8], ['short', 'average', 'tall'], 24, 4, 'frequency', draw=False, W=150, H=115, mm=38) + '</div>'
      + '<div style="flex:1"><b>b.</b>' + segbar([25, 41.7, 33.3], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', draw=False, W=150, H=115, mm=38) + '</div></div>')))

P.append(pair(
  box('Example 5 · Describing the distribution of a categorical variable', q('In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages. <i>(Table: see Example 3.)</i>')
      + q('Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.')
      + report(['The ', ('variable', 'climate types'), ' of ', ('number', '23'), ' ', ('individuals', 'countries'), ' were classified as being ', ('categories', '‘cold’, ‘mild’ or ‘hot’'), '. The ', ('majority / most', 'majority'), ' of the countries, ',
                ('%', '60.9%'), ', were found to ', ('modal category', 'have a mild climate'), '. Of the remaining countries, ', ('%', '26.1%'), ' were found to have a ', ('category', 'hot'), ' climate, while ', ('%', '13.0%'), ' were found to have a ', ('category', 'cold'), ' climate.'])),
  box('You try 5', '<div class="row"><div style="flex:1.3">' + q('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.')
      + '</div><div style="flex:1">' + segbar([25, 41.7, 33.3], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', 'teacher’s height', W=175, H=120, mm=40) + '</div></div>'
      + parts([('a.', 'Find the modal category of the data set.', 'average', 7), ('b.', 'Describe the distribution of the data set.', '', 0)])
      + report([('number', '24'), ' ', ('individuals', 'prep students'), ' were surveyed on ', ('question', 'how tall they thought their teacher was'), '. The ', ('most common / majority', 'most common'), ' response was ', ('modal category', 'average'),
                ', accounting for ', ('%', '41.7%'), ' of responses, while ', ('%', '25%'), ' said their teacher was ', ('category', 'short'), ', and ', ('%', '33.3%'), ' said their teacher was ', ('category', 'tall'), '.']))))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
DAY = list(range(1, 16)); TMP = [12.7, 11.8, 10.7, 9.0, 6.0, 7.0, 4.1, 4.8, 9.2, 6.7, 7.5, 8.0, 8.6, 9.8, 7.7]
P.append(box('Exit task 1', q('The table shows the <i>day number</i> and the <i>minimum temperature</i>, in degrees Celsius, for 15 consecutive days in May 2017.')
  + table([['<i>day number</i>'] + DAY, ['<i>minimum temperature</i> (°C)'] + TMP], head=False, style='font-size:8pt')
  + q('Which of the two variables in this data set is an ordinal variable?') + space(8, '<i>day number</i>') + guess('83%', mcq=False) + src('VCAA 2019 Exam 2 Q1a'), '1 mark'))
HEP = [(1, 1.76, 15.34, 41.22), (2, 1.79, 16.96, 42.41), (3, 1.83, 13.87, 46.53), (4, 1.82, 14.23, 40.53), (5, 1.87, 13.78, 40.62), (6, 1.73, 14.50, 45.62), (7, 1.68, 15.08, 42.33), (8, 1.82, 13.13, 40.88),
       (9, 1.83, 14.22, 39.22), (10, 1.87, 13.62, 42.51), (11, 1.87, 12.01, 42.75), (12, 1.80, 12.88, 38.12), (13, 1.83, 12.68, 42.65), (14, 1.87, 12.45, 41.32), (15, 1.78, 11.31, 42.88)]
HT = lambda rows: table([['<i>athlete number</i>', '<i>high jump</i> (metres)', '<i>shot-put</i> (metres)', '<i>javelin</i> (metres)']] + [[x, f'{b:.2f}', f'{c:.2f}', f'{d:.2f}'] for x, b, c, d in rows], cls='t tiny')
P.append(box('Exit task 2', q('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.')
  + table([['<i>athlete number</i>'] + [h[0] for h in HEP]] + [[n] + [f'{h[k]:.2f}' for h in HEP] for k, n in ((1, '<i>high jump</i> (metres)'), (2, '<i>shot-put</i> (metres)'), (3, '<i>javelin</i> (metres)'))], cls='t tiny')
  + q('Write down the number of numerical variables in the table.') + space(8, '3 (<i>athlete number</i> is a label)') + guess('52%', mcq=False) + src('VCAA 2021 Exam 2 Q1a (table turned to fit)'), '1 mark'))
P.append(box('Exit task 3', '<div class="row"><div style="flex:1">' + q('A study was conducted that investigated the <i>number of moths</i> caught in a sugar moth trap (less than 250, 250–500, more than 500). The results are summarised in the percentage segmented bar chart shown.')
  + q('There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to') + mc(['30', '90', '250', '300', '500'], 'B', cols=5)
  + why('30% of 300 = 30 ÷ 100 × 300 = 90') + guess('76% · A (21%)') + '</div><div style="flex:none;width:62mm">'
  + segbar([30, 46, 24], ['less than 250', '250–500', 'more than 500'], 100, 10, 'frequency (%)', 'number of moths', W=230, H=150, mm=62) + '</div></div>'
  + src('VCAA 2017 Exam 1 Q5 (adapted)'), '1 mark'))

P.append(close(['I can identify types of data.', 'I can construct a frequency table for categorical data.', 'I can construct a bar chart from a frequency table.',
  'I can construct a percentage segmented bar chart from a frequency table.', 'I can describe the distribution of a categorical variable.'],
  [('Exercise 1A', 'Q1 · Q2 · Q3<br>Q4–6 <i>(Exam 1 style)</i>'), ('Exercise 1B', 'Q1–3 · Q4–5<br>Q6–8 · Q9 <i>(Exam 1 style)</i>')], '1A and 1B sections'))
build('S1', '1A–1B', 'AoS 1 · Data analysis', P)
