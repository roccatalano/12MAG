"""Lesson l19 (5C, moving medians) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l19/build.py
(Do Now is not on the worksheet, as in l16-l18).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = VCAA 2020 Exam 2 Q3b (= Edrolo U1&2 1D Q17, original wording and data).
Example 12 / You try 1 = Cambridge U3&4 Example 12 (pp. 278-279) / Edrolo U3&4 4C WE1 (pp. 254-256).
Example 13 / You try 2 = Cambridge Example 13 (pp. 279-280) / Edrolo 4C WE2 (pp. 257-259).
Exits = Edrolo U3&4 4C Q13 (VCAA 2021 Exam 1 Q13), Q14 (VCAA 2016 Exam 2 Q4a), Q15 (VCAA 2019 Exam 1 Q13).
Output: lessons/5C worksheet(.html/.pdf) + lessons/5C worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l19/worksheet.py"""
import os, sys, re
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
MONL = {k + 1: m for k, m in enumerate(MON)}
EX12 = [10, 12.5, 6, 5, 22, 19.5, 14, 7.5, 8.5, 10, 8, 15]


def plot(ys, meds=None, given=None, mm=88, **kw):
    """Black plot for students; red crosses + joined line (meds) only on the solutions copy. given: crosses printed in the question (black)."""
    kw = dict(dict(ink='#000', fs=12, r=3), **kw)
    base = ts(ys, **kw)
    if given: base = tsm(ys, given, show=True, col='#000', **kw).replace('<path data-i="ml"', '<path data-i="ml" style="display:none"')
    over = ''
    if meds:
        full = tsm(ys, meds, show=True, col='#c00', guides=False, **kw)
        b0 = ts(ys, **kw)
        head = re.match(r'<svg[^>]*>', b0).group(0)
        over = f'<div class="ans" style="position:absolute;inset:0">{head}{full[len(b0) - 6:]}</div>'
    return f'<div style="position:relative;max-width:{mm}mm;margin:1mm auto">{base}{over}</div>'


P = [title('5C', 'Smoothing a time series plot using moving medians')]
P.append(lis(['To be able to locate the median of a data set graphically.', 'To be able to smooth a time series plot using moving medians.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 12 · median and IQR'))
P.append(box('Question 1 · VCAA 2020 Exam 2 Q3b', q('In a study of the association between BMI and neck size, 250 men were grouped by neck size (below average, average and above average) and their BMI recorded.<br>Five-number summaries describing the distribution of BMI for each group are displayed in the table below along with the group size.')
  + table([['Neck size', 'Group size', 'Min.', 'Q<sub>1</sub>', 'Median', 'Q<sub>3</sub>', 'Max.']] + [[str(c) for c in r] for r in BMI], cls='t tiny')
  + parts([('b', 'What is the interquartile range (IQR) of BMI for the men with an average neck size?', 'IQR = 26.0 − 23.4 = 2.6', 12)]), '1 mark'))
# ---------------------------------------------------------------- 5C
P.append(sect('5C Smoothing with moving medians', 'Example, then you try'))
P.append(exyt('Example 12 · Three-moving median smoothing using a graphical approach',
  q('Construct a three-median smoothed plot of the time series plot shown opposite.')
  + plot(EX12, mmed(EX12, 3), yr=(0, 25), yt=5, xl='month', yl='number of births', xlab=MONL, W=440, H=230)
  + why('Median of each three months, marked × at the middle month; joined (Feb–Nov).'),
  'You try 1', q('Bailey recorded their screen time, in minutes, on their phone over the past week. Their data is presented in the following time series plot.')
  + plot(SCREEN, mmed(SCREEN, 3), yr=(40, 120), yt=10, xl='day', yl='screen time (mins)', W=440, H=220)
  + parts([('a', 'Determine the three-median smoothed <i>screen time</i> for day 5.', 'median of 107, 81, 102 = 102 minutes', 12),
           ('b', 'Construct a three-median smoothed plot for the entire time series.', 'On the plot (days 2–6: 70, 70, 81, 102, 102).', 'L'),
           ('c', 'What, if any, trend can be seen from the three-median smoothed time series?', 'The three-median smoothed data shows an increasing trend in Bailey’s screen time over the week.', 14)])))
P.append(exyt('Example 13 · Five-moving median smoothing using a graphical approach',
  q('Construct a five-median smoothed plot of the time series plot shown opposite.')
  + plot(EX12, mmed(EX12, 5), yr=(0, 25), yt=5, xl='month', yl='number of births', xlab=MONL, W=440, H=230)
  + why('Median of each five months, marked × at the middle month; joined (Mar–Oct). Smoother than the three-median plot.'),
  'You try 2', q('Emanuel is the goalkeeper for his soccer team and has recorded the <i>number of goals saved</i> each month for the past ten months. His data has been presented in the following time series plot.')
  + plot(GOALS, mmed(GOALS, 5), yr=(0, 30), yt=5, xl='month', yl='number of goals saved', W=440, H=220)
  + parts([('a', 'Determine the five-median smoothed <i>number of goals saved</i> for month 8.', 'median of 13, 11, 15, 7, 12 = 12', 10),
           ('b', 'Determine the nine-median smoothed <i>number of goals saved</i> for month 5.', 'months 1–9: 5th value of 7, 10, 11, 13, 15, 17, 18, 18, 25 = 15', 10),
           ('c', 'Construct a five-median smoothed plot for the entire time series.', 'On the plot (months 3–8: 18, 17, 17, 15, 13, 12).', 'L'),
           ('d', 'What, if any, trend can be seen from the five-median smoothed time series?', 'The five-median smoothed data shows a decreasing trend in number of goals saved.', 12)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2021 Exam 1 Q13', q('The time series plot below shows the <i>points scored</i> by a basketball team over 40 games.')
  + plot(PTS, None, yr=(90, 150), yt=10, xl='game number', yl='points scored', W=560, H=230, xr=(0, 40), xtick=5, mm=120)
  + q('The nine-median smoothed <i>points scored</i> for game number 10 is closest to')
  + mc(['102', '108', '110', '112', '117'], 'C', cols=5) + why('Games 6–14 in order: 96.5, 102, 108.5, 109.5, 110, … → 5th value = 110.'), '1 mark'))
RM = mmed(RMIN, 5)
P.append(box('Exit task 2 · VCAA 2016 Exam 2 Q4a', q('The time series plot below shows the <i>minimum rainfall</i> recorded at the weather station each month plotted against the <i>month number</i> (1 = January, 2 = February, and so on).<br>Rainfall is recorded in millimetres.<br>The data was collected over a period of one year.')
  + plot(RMIN, [None] * 6 + RM[6:], given=RM[:6] + [None] * 6, yr=(0, 100), yt=10, xl='month number', yl='minimum rainfall (mm)', W=480, H=230, xr=(0, 13), mm=88)
  + q('Five-median smoothing has been used to smooth the time series plot above.<br>The first four smoothed points are shown as crosses (×).<br>Complete the five-median smoothing by marking smoothed values with crosses (×) on the time series plot above.')
  + why('Crosses at (7, 74), (8, 61), (9, 67), (10, 61).'), '2 marks'))
P.append(box('Exit task 3 · VCAA 2019 Exam 1 Q13', q('The time, in minutes, that Liv ran each day was recorded for nine days.<br>These times are shown in the table below.')
  + T([['<b>Day number</b>'] + list(range(1, 10)), ['<b>Time (minutes)</b>'] + LIV])
  + q('The time series plot below was generated from this data.')
  + plot(LIV, None, yr=(0, 70), yt=10, xl='day number', yl='time (minutes)', W=420, H=210, xr=(0, 10), mm=68)
  + q('Both three-median smoothing and five-median smoothing are being considered for this data.<br>Both of these methods result in the same smoothed value on <i>day number</i>')
  + mc(['3', '4', '5', '6', '7'], 'E', cols=5) + why('Day 7: three-median of 60, 33, 37 = 37; five-median of 19, 60, 33, 37, 46 = 37.'), '1 mark'))
SC = ['I can smooth a time series using moving median smoothing.']
P.append(close(SC, [('5C', 'Q1–10')], ['5C']))
build('l19', '5C', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l19-worksheet', '5C worksheet'), ('l19-worksheet-solutions', '5C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
