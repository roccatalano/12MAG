"""Lesson l20 (5D, seasonal indices: interpreting and using) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as tools/deck/l20/build.py (Do Now is not on the worksheet, as in l16-l19).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 1 skills checklist 1B #6 (replaces 1A #2, burnt in l03), 1D #11; VCAA 2018 Exam 2 Q2a (= Edrolo U1&2 1D Q19, original wording).
Example 14 / You try 1 = Cambridge U3&4 Example 14 (p. 284) / Edrolo U3&4 4D WE1b (p. 269).
Example 15 / You try 2 = Cambridge Example 15 (p. 285) / Edrolo 4D WE5 (p. 271).
Example 16 / You try 3 = Cambridge Example 16 (p. 286) / Edrolo 4D WE4 (p. 271).
Exits = Edrolo U3&4 4D Q19 (VCAA 2017 Exam 1 Q16), 4D Q17 (VCAA 2020 Exam 1 Q17, Table 4 in two halves).
Output: lessons/5D seasonal indices worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/l20/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
SEAS = ['<b>Summer</b>', '<b>Autumn</b>', '<b>Winter</b>', '<b>Spring</b>']

P = [title('5D', 'Seasonal indices: interpreting and using')]
P.append(lis(['To be able to interpret the meaning of seasonal indices.', 'To be able to seasonally adjust data using seasonal indices.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11 skills · Year 12 · medians'))
P.append(box('Question 1', q('Decrease $150 by 20%.') + space(10, '150 × 0.8 = $120'), ''))
P.append(box('Question 2', q('In a class there are ten students who are 16 years old and twenty students who are 17 years old. Express the ratio of the number of 16-year-olds to 17-year-olds.') + space(10, '10 : 20 = 1 : 2'), ''))
P.append(box('Question 3 · VCAA 2018 Exam 2 Q2a', q('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>'
  'This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.')
  + f'<div style="max-width:78mm;margin:1mm auto">{scat(CONG, (35, 70), (35, 75), 5, 5, "morning congestion level (%)", "evening congestion level (%)", W=420, H=300, r=4.5, fs=12, ink="#000")}</div>'
  + q('a. Determine the median percentage congestion level for the morning peak period and the evening peak period.<br>Write your answers in the appropriate boxes provided below.')
  + q('Median percentage congestion level for morning peak period &nbsp;<span style="display:inline-block;border:1px solid #000;min-width:16mm;text-align:center">' + ans('52') + '</span> %<br><br>'
      'Median percentage congestion level for evening peak period &nbsp;&nbsp;<span style="display:inline-block;border:1px solid #000;min-width:16mm;text-align:center">' + ans('56') + '</span> %')
  + why('19 points → 10th value: 10th from the left = 52; 10th from the bottom = 56 (a different point).'), '2 marks'))
# ---------------------------------------------------------------- 5D
P.append(sect('5D Seasonal indices', 'Example, then you try'))
P.append(exyt('Example 14 · Interpreting seasonal indices',
  q('Suppose that the seasonal indices (SI) for electricity usage in Esse’s home are as shown in the table:') + T([SEAS, ['1.16', '0.94', '1.26', '0.64']])
  + parts([('a', 'What does the seasonal index for Winter tell us?', 'Esse’s electricity usage in Winter is typically 26% higher than the average season.', 14),
           ('b', 'What does the seasonal index for Spring tell us?', 'Esse’s electricity usage in Spring is typically 36% lower than the average season.', 14)]),
  'You try 1', q('Consider the following table.') + T([['', '<b>summer</b>', '<b>autumn</b>', '<b>winter</b>', '<b>spring</b>'], ['<b>umbrella sales</b>', 205, 377, 528, 442]])
  + q('<i>Part a: the seasonal index for umbrella sales in summer, correct to two decimal places, is 0.53.</i>')
  + parts([('b', 'What does the rounded seasonal index for summer mean in terms of the <i>umbrella sales</i> in summer compared to the average season?',
            'On average, the number of umbrella sales in summer is 53% of, or 47% less than, the average season.', 20)])))
P.append(exyt('Example 15 · Using seasonal indices',
  q('The seasonal indices (SI) for cold drink sales for Imogen’s kiosk are as shown in the table:') + T([SEAS, ['1.75', '0.66', '0.46', '1.13']])
  + parts([('a', 'If the actual cold drink sales last summer totalled $21 653, what is the deseasonalised sales figure for that time period?', '21 653 ÷ 1.75 = $12 373.14', 12),
           ('b', 'If the deseasonalised cold drink sales last spring totalled $10 870, what were the actual sales for that time period?', '10 870 × 1.13 = $12 283.10', 12)]),
  'You try 2', q('The seasonal index for Australian <i>Oodie sales</i> in January is 0.65.<br>Last January, a store in Sydney sold a deseasonalised number of 540 Oodies.<br>How many Oodies did the store actually sell in January?')
  + space(24, 'actual = 0.65 × 540 = 351 Oodies')))
P.append(exyt('Example 16 · Using seasonal indices to determine percentage change required to correct for seasonality',
  q('Consider the table below which gives the seasonal indices for heater sales at a discount store:') + T([SEAS, ['0.65', '1.25', '1.35', '0.75']])
  + parts([('a', 'By what percentage should the sales in summer be increased or decreased in order to deseasonalise the data? Give your answer as a percentage rounded to one decimal place.',
            '1 ÷ 0.65 = 1.538 → actual sales should be increased by 53.8%', 14),
           ('b', 'By what percentage should the sales in winter be increased or decreased in order to deseasonalise the data? Give your answer as a percentage rounded to one decimal place.',
            '1 ÷ 1.35 = 0.741 → actual sales should be decreased by 25.9%', 14)]),
  'You try 3', q('The seasonal index for January is 0.8. How should data for this season be adjusted to correct for seasonality?')
  + space(24, '1 ÷ 0.8 = 1.25 → the data from January should be increased by 25% to correct for seasonality.')))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q16', q('The seasonal index for the sales of cold drinks in a shop in January is 1.6<br>To correct the January sales of cold drinks for seasonality, the actual sales should be')
  + mc(['reduced by 37.5%', 'reduced by 40%', 'reduced by 62.5%', 'increased by 60%', 'increased by 62.5%'], 'A', cols=3) + why('1 ÷ 1.6 = 0.625 = 62.5% → reduce by 37.5%.'), '1 mark'))
def half(ks): return T([[''] + [f'<b>{RMON[k]}</b>' for k in ks], ['<b>Monthly rainfall (mm)</b>'] + [f'{RAIN[k]:.1f}' for k in ks], ['<b>Seasonal index</b>'] + [f'{RSI[k]:.3f}' for k in ks]])
P.append(box('Exit task 2 · VCAA 2020 Exam 1 Q17', q('Table 4 below shows the monthly rainfall for 2019, in millimetres, recorded at a weather station, and the associated long-term seasonal indices for each month of the year.<br><b>Table 4</b>')
  + half(range(6)) + half(range(6, 12)) + q('The deseasonalised rainfall for May 2019 is closest to')
  + mc(['71.3 mm', '75.8 mm', '86.1 mm', '88.1 mm', '113.0 mm'], 'B', cols=5) + why('92.6 ÷ 1.222 = 75.78 mm.'), '1 mark'))
SC = ['I can interpret seasonal indices.', 'I can use seasonal indices to deseasonalise and reseasonalise data.', 'I can use seasonal indices to determine percentage change required to correct for seasonality.']
P.append(close(SC, [('5D', 'Q1–5, Q13–15')], ['5D']))
build('l20', '5D', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l20-worksheet', '5D seasonal indices worksheet'), ('l20-worksheet-solutions', '5D seasonal indices worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
