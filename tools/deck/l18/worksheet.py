"""Lesson l18 (5B, centring) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l18/build.py
(Do Now is not on the worksheet, as in l16-l17).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = VCAA 2020 Exam 2 Q4aii (= Edrolo U1&2 1E Q12, original wording and data).
Example 9 / You try 1 = Cambridge U3&4 Example 9 (p. 271) / Edrolo U3&4 4B WE2a-b (pp. 240-241).
Example 10 / You try 2 = Cambridge Example 10 (pp. 272-273) / Edrolo 4B WE2c (p. 242).
Example 11 / You try 3 = Cambridge Example 11 (p. 273) / Edrolo 4B WE2d (pp. 242-243).
Exits = Edrolo U3&4 4B Q16 (VCAA 2017 Exam 1 Q15), Q18 (VCAA 2016 Exam 2 Q4b).
Output: lessons/5B centring worksheet(.html/.pdf) + lessons/5B centring worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l18/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
f1 = lambda v: '–' if v is None else f'{v:.1f}'
def g(v): return '–' if v is None else f'{v:.3f}'.rstrip('0').rstrip('.')
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
TEMP = T([['<b>Day</b>'] + DAYS, ['<b>Temp. (°C)</b>'] + E7_T])

P = [title('5B', 'Moving means with centring')]
P.append(lis(['To be able to know when and how to use centring when smoothing.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 12 · mean'))
P.append(box('Question 1 · VCAA 2020 Exam 2 Q4aii', q('The age, in years, body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 men aged 23 to 25 years are shown in the table below.')
  + T([['<b>Age (years)</b>'] + AGE, ['<b>Body density (kg/litre)</b>'] + DENS, ['<b>Weight (kg)</b>'] + WT])
  + parts([('a', 'For these 12 men, determine<br>ii. the mean of their body density, in kilograms per litre.', '1.065 (CAS one-variable statistics; not rounded)', 12)]), '1 mark'))
# ---------------------------------------------------------------- 5B
P.append(sect('5B Moving means with centring', 'Example, then you try'))
DIST = lambda extra: ''.join(T([['<b>month</b>'] + MON[j:j + 6], ['<b>distance run (km)</b>'] + WE2_D[j:j + 6]] + [[f'<b>{h}</b>'] + ['–' if v is None else a(f1(v)) for v in vals[j:j + 6]] for h, vals in extra]) for j in (0, 6))
P.append(exyt('Example 9 · Two-moving mean smoothing with centring',
  q('The temperatures (°C) recorded at a weather station at 9 a.m. each day for a week are displayed in the table.') + TEMP
  + parts([('', 'Calculate the two-moving mean smoothed temperature with centring for Tuesday.', 'mean 1 = (18.1 + 24.8) ÷ 2 = 21.45; mean 2 = (24.8 + 26.4) ÷ 2 = 25.60; centred = (21.45 + 25.60) ÷ 2 = 23.525 → 23.5 °C', 24)]),
  'You try 1', q('Amelia recorded the distance, in km, she ran each month for a year.')
  + DIST([('two-mean smoothed distance run with centring (km)', WE2_2)])
  + parts([('a', 'Find the two-mean smoothed distance run for July.', 'mean 1 = (35 + 36) ÷ 2 = 35.5; mean 2 = (36 + 28) ÷ 2 = 32; (35.5 + 32) ÷ 2 = 33.75 km', 14),
           ('b', 'Find the two-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.', 'In the table.', 6)])))
P.append(exyt('Example 10 · Four- and six-moving mean smoothing with centring',
  q('The table below gives the temperature (°C) recorded at a weather station at 9.00 a.m. each day for a week.') + TEMP
  + parts([('a', 'Calculate the four-moving mean smoothed temperature with centring for Thursday.', 'mean 1 = 19.45, mean 2 = 16.8; (19.45 + 16.8) ÷ 2 = 18.125 → 18.1 °C', 18),
           ('b', 'Calculate the six-moving mean smoothed temperature with centring for Thursday.', 'mean 1 = 18.35, mean 2 = 19.483…; centred = 18.917 → 18.9 °C', 18)]),
  'You try 2', q('Amelia recorded the distance, in km, she ran each month for a year.') + DIST([])
  + parts([('c', 'Find the four-mean smoothed distance run for July.', 'mean 1 = (37 + 35 + 36 + 28) ÷ 4 = 34; mean 2 = (35 + 36 + 28 + 31) ÷ 4 = 32.5; (34 + 32.5) ÷ 2 = 33.25 km', 30)])))
c4 = mmc(E8_B, 4)
NC = ['', '8.25', '11.25', '12.75', '14.5', '15', '11.75', '9.75', '8.5', '10.5', '', '']
P.append(exyt('Example 11 · Smoothing a time series using four-mean smoothing with centring',
  q('The following table gives the number of births per month over a calendar year in a country hospital. Use the four moving mean with centring method to complete the table.')
  + table([['Month', 'Number of births', '4-moving mean', '4-moving mean with centring']] + [[m, str(b), a(n) if n else '', '–' if c is None else a(g(c))] for m, b, n, c in zip(MON, E8_B, NC, c4)], cls='t fill tiny'),
  'You try 3', q('Amelia recorded the distance, in km, she ran each month for a year.')
  + DIST([('four-mean smoothed distance run with centring (km)', WE2_4)])
  + parts([('d', 'Find the four-mean smoothed values, correct to one decimal place, for the entire time series and fill in the table.', 'In the table (CAS: C3 = (b1+2b2+2b3+2b4+b5)/8, copied down).', 10)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q15', q('The wind speed at a city location is measured throughout the day.<br>The table below shows the daily maximum wind speed, in kilometres per hour, for the days in week 2.')
  + T([['<b>Day</b>'] + WIND_D, ['<b>Maximum wind speed (km/h)</b>'] + WIND])
  + q('A four-point moving mean with centring is used to smooth the time series data above.<br>The smoothed maximum wind speed, in kilometres per hour, for day 11 is closest to')
  + mc(['22', '24', '26', '28', '30'], 'D', cols=5) + why('mean 1 = 26.5, mean 2 = 30.25; centred = 28.375.'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2016 Exam 2 Q4b', q('The maximum daily rainfall each month was also recorded at the weather station.<br>The table below shows the maximum daily rainfall each month for a period of one year.')
  + T([['<b>Month</b>', 'Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'], ['<b>Month number</b>'] + list(range(1, 13)), ['<b>Maximum daily rainfall (mm)</b>'] + RAIN16])
  + q('The data in the table has been used to plot maximum daily rainfall against month number in the time series plot below.')
  + '<div style="max-width:95mm;margin:1mm auto">' + ts(RAIN16, yr=(0, 250), yt=50, xl='month number', yl='maximum daily rainfall (mm)', xr=(0, 13), W=480, H=210, ink='#000', fs=12, r=3,
        overlays=[(mmc(RAIN16, 2), '#000', 'c2', '5 4')]).replace('class="hid0"', '') + '</div>'
  + q('Two-mean smoothing with centring has been used to smooth the time series plot above.<br>The smoothed values are marked with crosses (×).<br>Using the data given in the table, show that the two-mean smoothed rainfall centred on October is 157.25 mm.')
  + parts([('b', '', 'M1 = (124 + 140) ÷ 2 = 132; M2 = (140 + 225) ÷ 2 = 182.5; (132 + 182.5) ÷ 2 = 157.25 mm', 22)]), '2 marks'))
SC = ['I can smooth a time series using moving mean smoothing with centring.']
P.append(close(SC, [('5B', 'Q6–14')], ['5B']))
build('l18', '5B', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l18-worksheet', '5B centring worksheet'), ('l18-worksheet-solutions', '5B centring worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
