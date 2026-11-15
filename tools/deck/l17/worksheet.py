"""Lesson l17 (5B, moving means) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l17/build.py
(Do Now is not on the worksheet, as in l16).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = VCAA 2017 Exam 1 Q3 (= Edrolo U1&2 1E Q11, original wording and data).
Example 7 / You try 1 = Cambridge U3&4 Example 7 (p. 268) / Edrolo U3&4 4B WE1 (p. 234). Example 8 / You try 2 = Cambridge Example 8 (p. 269) / Edrolo 4B WE3 (p. 243).
Exits = Edrolo U3&4 4B Q15 (VCAA 2019 Exam 1 Q16), Q17 (VCAA 2021 Exam 1 Q14).
Output: lessons/5B moving means worksheet(.html/.pdf) + lessons/5B moving means worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l17/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def FIG(svg, mm): return f'<div style="max-width:{mm}mm;margin:1mm auto">{svg}</div>'
K = dict(ink='#000', fs=13, r=3)
f1 = lambda v: '–' if v is None else f'{v:.1f}'
MONL = {k + 1: m for k, m in enumerate(MON)}

P = [title('5B', 'Smoothing with moving means')]
P.append(lis(['To be able to smooth a time series plot using moving means.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1 · VCAA 2017 Exam 1 Q3', q('The table below shows the forearm circumference, in centimetres, of a sample of 10 people selected from this group of 252 people.')
  + T([['<b>Circumference</b>'] + ARM])
  + q('The mean, <i>x̄</i>, and the standard deviation, <i>s<sub>x</sub></i>, of the forearm circumference for this sample of people are closest to')
  + mc(['<i>x̄</i> = 1.58 &nbsp; <i>s<sub>x</sub></i> = 27.8', '<i>x̄</i> = 1.66 &nbsp; <i>s<sub>x</sub></i> = 27.8', '<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 1.58',
        '<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 1.66', '<i>x̄</i> = 27.8 &nbsp; <i>s<sub>x</sub></i> = 2.30'], 'D', cols=2)
  + why('CAS one-variable statistics: x̄ = 27.77, sₓ = 1.664 (C is σₓ, the population value).'), '1 mark'))
# ---------------------------------------------------------------- 5B
P.append(sect('5B Smoothing with moving means', 'Example, then you try'))
r3 = mm(WE1_R, 3); r5 = mm(WE1_R, 5)
P.append(exyt('Example 7 · Three- and five-moving mean smoothing',
  q('The table below gives the temperature (°C) recorded at a weather station at 9.00 a.m. each day for a week.')
  + T([['<b>Day</b>', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], ['<b>Temp.</b>'] + E7_T])
  + parts([('a', 'Calculate the three-moving mean smoothed temperature for Tuesday.', '(18.1 + 24.8 + 26.4) ÷ 3 = 23.1 °C', 16),
           ('b', 'Calculate the five-moving mean smoothed temperature for Thursday.', '(24.8 + 26.4 + 13.9 + 12.7 + 14.2) ÷ 5 = 18.4 °C', 16)]),
  'You try 1', q('The following table shows the daily <i>rainfall</i> in Dunedin for a week.')
  + T([['<b>day</b>'] + WE1_DAY, ['<b>rainfall (mm)</b>'] + WE1_R,
       ['<b>three-mean smoothed rainfall</b>'] + ['–' if v is None else a(f1(v)) for v in r3],
       ['<b>five-mean smoothed rainfall</b>'] + ['–' if v is None else a(f1(v)) for v in r5]])
  + parts([('a', 'Find the three-mean smoothed rainfall for Wednesday, correct to one decimal place.', '(3 + 5 + 5) ÷ 3 = 4.3 mm', 10),
           ('b', 'Find the three-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.', 'In the table.', 6),
           ('c', 'Find the five-mean smoothed rainfall for Wednesday.', '(2 + 3 + 5 + 5 + 1) ÷ 5 = 3.2 mm', 10),
           ('d', 'Find the five-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.', 'In the table.', 6)])))
b3 = mm(E8_B, 3); b5 = mm(E8_B, 5)
P.append(exyt('Example 8 · Three- and five-moving mean smoothing of a time series',
  q('The following table gives the number of births per month over a calendar year in a country hospital. Use the three-moving mean and the five-moving mean methods, rounded to one decimal place, to complete the table.')
  + table([['Month', 'Number of births', '3-moving mean', '5-moving mean']] + [[m, str(b), '–' if x is None else a(f1(x)), '–' if y is None else a(f1(y))] for m, b, x, y in zip(MON, E8_B, b3, b5)], cls='t fill tiny'),
  'You try 2', q('Tobias wants to get faster at solving his Rubik’s Cube. He solves it once a day and records the <i>time taken</i> in seconds. The data taken over two weeks is shown in the following table. Tobias has also calculated the five-mean smoothed values for the data set, correct to one decimal place.')
  + ''.join(T([['<b>day</b>'] + list(range(1 + j, 8 + j)), ['<b>time taken (s)</b>'] + WE3_T[j:j + 7], ['<b>five-mean smoothed</b>'] + [f1(v) for v in WE3_S[j:j + 7]]]) for j in (0, 7))
  + q('Tobias has constructed the following graph to display the <i>time taken</i>.')
  + f'<div style="position:relative;max-width:82mm;margin:1mm auto">{ts(WE3_T, yr=(50, 120), yt=10, xl="day", yl="time taken (s)", xr=(0, 14), W=440, H=220, **K)}'
  + f'<div class="ans" style="position:absolute;inset:0">{ts([None]*14, yr=(50, 120), yt=10, xl="", yl="", xr=(0, 14), W=440, H=220, grid=False, overlays=[(WE3_S, "#c00", "m", "")], ink="#c00", fs=13, r=3).replace("<text", "<text fill-opacity=0 ").replace(chr(39)+"hid0"+chr(39), "").replace(chr(34)+"hid0"+chr(34), chr(34)+chr(34))}</div></div>'
  + parts([('a', 'Plot the five-mean smoothed values onto the same graph.', 'Plotted in red (days 3–12).', 'L'),
           ('b', 'What, if any, trend can be seen from the five-mean smoothed data?', 'A decreasing trend in time taken.', 12)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 1 Q16', '<div style="display:flex;gap:4mm"><div style="flex:1">'
  + q('The time series plot below shows the <i>monthly rainfall</i> at a weather station, in millimetres, for each <i>month</i> in 2017.<br>If seven-mean smoothing is used to smooth this time series plot, the number of smoothed data points would be')
  + mc(['3', '5', '6', '8', '10'], 'C') + why('Seven-mean loses 3 points at each end: 12 − 6 = 6.') + '</div><div style="flex:1">'
  + FIG(ts(RAIN19, yr=(0, 300), yt=50, xl='month', yl='monthly rainfall (mm)', xlab=MONL, W=440, H=220, ink='#000', fs=12, r=3), 85) + '</div></div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q14', q('A garden centre sells garden soil.<br>The table below shows the daily quantity of garden soil sold, in cubic metres, over a one-week period.')
  + T([['<b>Day</b>', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ['<b>Quantity (m<sup>3</sup>)</b>', '234', '186', '', '', '', '346', '346']])
  + q('The quantity of garden soil sold on Wednesday, Thursday and Friday is not shown.<br>The five-mean smoothed quantity of garden soil sold on Thursday is 206 m<sup>3</sup>.<br>The three-mean smoothed quantity of garden soil sold on Thursday, in cubic metres, is')
  + mc(['143', '166', '206', '239', '403'], 'B', cols=5) + why('Wed + Thu + Fri = 5 × 206 − 186 − 346 = 498; 498 ÷ 3 = 166.'), '1 mark'))
SC = ['I can smooth a time series using moving mean smoothing.']
P.append(close(SC, [('5B', 'Q1–5')], ['5B']))
build('l17', '5B', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l17-worksheet', '5B moving means worksheet'), ('l17-worksheet-solutions', '5B moving means worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
