"""Lesson l16 (5A) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l16/build.py
(Do Now and CFAT are not on the worksheet, as in l07/l09).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 7 checklist 7D #7 (replaces 7B #3, burnt in l05); APK 2 = Cambridge U1&2 Ch 5 checklist 5J #14; APK 3 = VCAA 2019 Exam 1 Q9 (= Edrolo U1&2 9B Q21, original wording).
Examples 1-6 = Cambridge U3&4 pp. 254-262 (plots redrawn, values read off). You trys: Edrolo U3&4 4A WE1a (p. 223); YT-5A-2, YT-5A-3; Edrolo 4A WE2 (p. 227); YT-5A-5; YT-5A-6.
Exits = Edrolo U3&4 4A Q11 (VCAA 2018 Exam 2 Q3a), Q12 (VCAA 2016 Exam 1 Q13), Q13 (VCAA 2021 Exam 1 Q12).
Output: lessons/5A worksheet(.html/.pdf) + lessons/5A worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l16/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def FIG(svg, mm): return f'<div style="max-width:{mm}mm;margin:1mm auto">{svg}</div>'
K = dict(ink='#000', fs=13, r=3)
RED = dict(ink='#c00', fs=13, r=3)

P = [title('5A', 'Time series data')]
P.append(lis(['To be able to recognise time series data.', 'To be able to construct a time series plot.',
              'To be able to recognise features in the plot such as trend, seasonality and irregular fluctuations.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Determine the equation of the line fitted by eye to the scatterplot, below, which shows the association between the age of a group of cars, in years, (<i>age of car</i>) and the number of kilometres they have travelled (<i>kms</i>).')
  + FIG(scat(CARS, (0, 10), (0, 80000), 1, 10000, 'Age of car (years)', 'Kms', W=480, H=230, r=4, fs=13, ink='#000', tl=((0, 10000), (10, 62000)), tl_hid=False), 85)
  + space(14, 'Points (0, 10 000) and (10, 62 000): slope = 52 000 ÷ 10 = 5200. kms = 10 000 + 5200 × age of car')))
P.append(box('Question 2', q('A car park is open for 10 hours a day. The cost, <i>C</i>, for the time, <i>t</i>, is given by the following piecewise equation.<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>C</i> = 12<i>t</i> &nbsp;&nbsp;&nbsp;&nbsp;(0 ≤ <i>t</i> &lt; 4)<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>C</i> = 8 + 10<i>t</i> &nbsp;(4 ≤ <i>t</i> ≤ 10)<br>Find the cost for parking your car for 8 hours.')
  + space(10, 'C = 8 + 10 × 8 = $88')))
P.append(box('Question 3 · VCAA 2019 Exam 1 Q9', q('A least squares line is used to model the relationship between the monthly <i>average temperature</i> and <i>latitude</i> recorded at seven different weather stations. The equation of the least squares line is found to be<br>&nbsp;&nbsp;&nbsp;&nbsp;<i>average temperature</i> = 42.9842 – 0.877447 × <i>latitude</i>')
  + q('When the numbers in this equation are correctly rounded to three significant figures, the equation will be')
  + mc(['<i>average temperature</i> = 42.984 – 0.877 × <i>latitude</i>', '<i>average temperature</i> = 42.984 – 0.878 × <i>latitude</i>', '<i>average temperature</i> = 43.0 – 0.878 × <i>latitude</i>',
        '<i>average temperature</i> = 42.9 – 0.878 × <i>latitude</i>', '<i>average temperature</i> = 43.0 – 0.877 × <i>latitude</i>'], 'E')
  + why('42.9842 → 43.0 (three significant figures); 0.877447 → 0.877.'), '1 mark'))
# ---------------------------------------------------------------- 5A
P.append(sect('5A Time series data', 'Example, then you try'))
DL = {k + 1: d for k, d in enumerate(E1_DAYS)}
P.append(exyt('Example 1 · Constructing a time series plot',
  q('Maximum temperature was recorded each day for a week in a certain town. Construct a time series plot of the data.')
  + T([['<b>Day</b>'] + E1_DAYS, ['<b>Temperature (°C)</b>'] + E1_T])
  + f'<div style="position:relative;max-width:80mm;margin:1mm auto">{ts([None]*7, yr=(15, 40), yt=5, xl="Day", yl="Temp (°C)", xlab=DL, W=420, H=230, **K)}'
  + f'<div class="ans" style="position:absolute;inset:0">{ts(E1_T, yr=(15, 40), yt=5, xl="Day", yl="Temp (°C)", xlab=DL, W=420, H=230, **RED)}</div></div>',
  'You try 1', q('The <i>number of deaths and serious injuries</i> caused by road accidents in the UK for each month from October 1982 until the end of 1983 are shown in a table.')
  + T([['<b>month</b>'] + [m.replace('<br>', ' ') for m in WE1_M[:8]], ['<b>deaths and serious injuries</b>'] + WE1_D[:8]])
  + T([['<b>month</b>'] + [m.replace('<br>', ' ') for m in WE1_M[8:]], ['<b>deaths and serious injuries</b>'] + WE1_D[8:]])
  + q('a. Use the table to construct a time series plot.')
  + solfig(55, 'Code the months 1–15.' + FIG(ts(WE1_D, yr=(1000, 2200), yt=200, xl='month', yl='deaths and serious injuries', W=440, H=230, xtick=2, xr=(0, 16), **RED), 78))))
P.append(exyt('Example 2 · Identifying trends',
  q('Consider the time series plot of the Australian annual birth rates over the years from 1931 to 1990, shown below. Comment on the trend shown in the plot.')
  + FIG(ts(BIRTH, BIRTH_Y, yr=(1.6, 3.6), yt=0.4, xl='Year', yl='Birth rate', W=440, H=210, xtick=10, xr=(1930, 2000), ink='#000', fs=13, r=2), 80)
  + space(24, 'Three distinct trends: a rapid increase from 1940 to 1961 (‘Baby Boom’); a very rapid decrease from about 1962 to 1980 (‘Baby Bust’); a slow decrease during the 1980s and beyond.'),
  'You try 2', q('Consider the time series plot of the number of visitors (in thousands) to a national park each year from 2008 to 2022, constructed from the data below. Comment on the trend shown in the plot.')
  + T([['<b>Year</b>'] + list(range(2008, 2016)), ['<b>Visitors (’000)</b>'] + YT2[:8]]) + T([['<b>Year</b>'] + list(range(2016, 2023)), ['<b>Visitors (’000)</b>'] + YT2[8:]])
  + FIG(ts(YT2, list(range(2008, 2023)), yr=(30, 70), yt=10, xl='year', yl='visitors (’000)', W=440, H=200, xtick=2, xr=(2007, 2023), **K), 78)
  + space(22, 'Two trends: 2008–2014 increasing steadily (41 000 to 62 000); 2014–2022 decreasing steadily (62 000 to 38 000).')))
P.append(exyt('Example 3 · Identifying cycles',
  q('Sunspots are darker, cooler area on the surface of the sun. The following plot shows the sunspot activity for the period 1945 to 2016. Comment on the cycles shown in the plot.')
  + FIG(ts(SUN, SUN_Y, yr=(0, 200), yt=50, xl='Year', yl='Sunspots', W=440, H=200, xtick=10, xr=(1940, 2020), ink='#000', fs=13, r=2), 80)
  + space(18, 'Cycles: recurrent peaks and troughs. Lowest activity about 1954, 1964, 1975, 1986, 1996, 2008.'),
  'You try 3', q('The following plot shows the number of mice caught each year on a farm for the period 2000 to 2023, constructed from the data below. Comment on the cycles shown in the plot.')
  + ''.join(T([['<b>Year</b>'] + list(range(2000 + j, 2008 + j)), ['<b>Mice</b>'] + YT3[j:j + 8]]) for j in (0, 8, 16))
  + FIG(ts(YT3, list(range(2000, 2024)), yr=(0, 100), yt=20, xl='year', yl='mice caught', W=440, H=200, xtick=4, xr=(1999, 2024), **K), 78)
  + space(18, 'Cycles (peaks and troughs over more than a year); highest about 2002, 2008, 2014, 2020: about every 6 years.')))
HL = {k: v.replace('<br>', '<br>') for k, v in HOTEL_LAB.items()}
P.append(exyt('Example 4 · Identifying seasonality',
  q('The plot below shows the total percentage of hotel rooms occupied in Australia by quarter, over the years 2012–2016. Comment on the seasonality shown in the plot.')
  + FIG(ts(HOTEL, yr=(67, 75), yt=1, xl='Quarter', yl='Room occupancy rate (%)', W=460, H=230, xlab=HL, ink='#000', fs=11, r=3), 82)
  + space(22, 'Seasonality: lowest in the June quarter, highest in the December quarter each year. Also an increasing trend.'),
  'You try 4', q('The number of <i>deaths and serious injuries</i> caused by road accidents in the UK for each month over a four-year period, from September 1980 until September 1984, are shown in the time series plot.<br>Note that seat belt use became mandatory by law in the UK in February 1983.')
  + FIG(ts(WE2, yr=(1000, 2100), yt=100, xl='month', yl='deaths and serious injuries', W=460, H=220, xtick=5, xr=(0, 50), ink='#000', fs=11, r=2), 82)
  + q('Describe any patterns present in the time series plot.')
  + space(22, 'No obvious trend. Seasonality with a period of 12 months, peaking every December. Structural change between month 29 and month 31 (seat belt laws, February 1983).')))
P.append(exyt('Example 5 · Identifying structural change',
  q('The time series plot below shows the power bill for a rental house (in kWh) for the 12 months of a year. Comment on any structural change in the plot.')
  + FIG(ts(POWER, yr=(0, 350), yt=50, xl='Month', yl='Electricity use (kWh)', W=440, H=210, xlab={k + 1: m for k, m in enumerate(MONTHS)}, ink='#000', fs=12, r=3), 78)
  + space(22, 'Abrupt change from June to July: from around 300 kWh per month to around 175 kWh (e.g. a family replaced by one person).'),
  'You try 5', q('The time series plot below shows the water use for a house (in kL) for the 12 months of a year, constructed from the data below. Comment on any structural change in the plot.')
  + T([['<b>Month</b>'] + MONTHS, ['<b>kL</b>'] + YT5])
  + FIG(ts(YT5, yr=(0, 45), yt=5, xl='Month', yl='Water use (kL)', W=440, H=200, xlab={k + 1: m for k, m in enumerate(MONTHS)}, ink='#000', fs=12, r=3), 78)
  + space(18, 'Abrupt increase from June to July: from around 21 kL to around 38 kL per month (e.g. more people moving in).')))
P.append(exyt('Example 6 · Identifying outliers',
  q('The time series plot below shows the daily power bill for a house (in kWh) for a fortnight. Comment on any outliers in the plot.')
  + FIG(ts(DAILY, yr=(0, 12), yt=2, xl='Day', yl='Electricity use (kWh)', W=440, H=210, xr=(0, 15), **K), 78)
  + space(18, 'Day 4 is a clear outlier: less than 2 kWh against about 10 kWh on other days (power out for 18 hours in a storm).'),
  'You try 6', q('The time series plot below shows the number of coffees sold each day at a café for a fortnight, constructed from the data below. Comment on any outliers in the plot.')
  + T([['<b>Day</b>'] + list(range(1, 15)), ['<b>Coffees</b>'] + YT6])
  + FIG(ts(YT6, yr=(0, 160), yt=20, xl='Day', yl='Coffees sold', W=440, H=200, xr=(0, 15), **K), 78)
  + space(16, 'Day 9 is an outlier: 150 coffees against about 80–86 on other days.')))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
YR = list(range(2008, 2017))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q3a', q('The following table shows the yearly average traffic congestion levels in two cities, Melbourne and Sydney, during the period 2008 to 2016. Also shown is a time series plot of the same data. The time series plot for Melbourne is incomplete.')
  + T([['<b>year</b>'] + YR, ['<b>Melbourne</b>'] + MEL, ['<b>Sydney</b>'] + SYD])
  + f'<div style="position:relative;max-width:90mm;margin:1mm auto">{ts(MEL[:6] + [None]*3, YR, yr=(20, 45), yt=5, xl="year", yl="congestion level (%)", W=460, H=220, xr=(2008, 2016), extra=[(SYD, "#000", "")], ink="#000", fs=13, r=3)}'
  + f'<div class="ans" style="position:absolute;inset:0">{ts([None]*5 + MEL[5:], YR, yr=(20, 45), yt=5, xl="", yl="", W=460, H=220, xr=(2008, 2016), grid=False, **RED).replace("<text", "<text fill-opacity=0 ")}</div></div>'
  + q('Upper line: Sydney · lower line: Melbourne (to 2013). Use the data in the table to complete the time series plot for Melbourne.'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2016 Exam 1 Q13', '<div style="display:flex;gap:4mm"><div style="flex:1">' + q('Consider the time series plot.<br>The pattern in the time series plot shown is best described as having')
  + mc(['irregular fluctuations only.', 'an increasing trend with irregular fluctuations.', 'seasonality with irregular fluctuations.', 'seasonality with an increasing trend and irregular fluctuations.', 'seasonality with a decreasing trend and irregular fluctuations.'], 'C')
  + why('Peaks every 12 months (seasonality); the peaks do not keep rising (no trend).') + '</div><div style="flex:1">'
  + FIG(ts(TEMP16, list(range(0, 49)), yr=(0, 30), yt=5, xl='month number', yl='mean temperature', W=440, H=220, xtick=12, xr=(0, 48), ink='#000', fs=13, r=2.5), 85) + '</div></div>', '1 mark'))
P.append(box('Exit task 3 · VCAA 2021 Exam 1 Q12', '<div style="display:flex;gap:4mm"><div style="flex:1">' + q('The time series plot shows the quarterly <i>sales</i>, in thousands of dollars, of a small business for the years 2010 to 2020.<br>The time series plot is best described as having')
  + mc(['seasonality only.', 'irregular fluctuations only.', 'seasonality with irregular fluctuations.', 'a decreasing trend with irregular fluctuations.', 'a decreasing trend with seasonality and irregular fluctuations.'], 'D')
  + why('Sales drift down (decreasing trend); peaks are not in the same quarter each year (no seasonality).') + '</div><div style="flex:1">'
  + FIG(ts(SALES21, [2010 + k / 4 for k in range(41)], yr=(0, 700), yt=100, xl='year', yl='sales ($000’s)', W=440, H=220, xtick=2, xr=(2010, 2020), ink='#000', fs=13, r=2.5), 85) + '</div></div>', '1 mark'))
SC = [x for x in ['I can construct a time series plot.', 'I can identify trend in a time series plot.', 'I can identify cycles in a time series plot.',
                  'I can identify seasonality in a time series plot.', 'I can identify structural change in a time series plot.', 'I can identify outliers in a time series plot.']]
P.append(close(SC, [('5A', 'Q1–15')], ['5A']))
build('l16', '5A', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l16-worksheet', '5A worksheet'), ('l16-worksheet-solutions', '5A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
