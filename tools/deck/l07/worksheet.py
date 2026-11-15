"""Lesson l07 (2G-2H) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l07/build.py.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 7 skills checklist 7C #6 (solution written for 12MAG); APK 2 = VCAA 2019 Further Exam 2 Q4a (Edrolo U1&2 6A Q15, original wording).
Examples 17-21 = Cambridge U3&4 pp. 146-148. You trys: Edrolo U3&4 3C WE1a, 1b (p. 179); YT-2G-19/20/21 (planner/written-youtrys.json, written for 12MAG);
2H You try = Edrolo U3&4 2D WE2 (p. 148). Exits = Edrolo U3&4 2D Q13 (VCAA 2017 Exam 1 Q12), 2D Q14 (VCAA 2019 Exam 2 Q4c).
Output: lessons/2G-2H worksheet(.html/.pdf) + lessons/2G-2H worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l07/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
YTW = {y['id']: y for y in json.load(open(os.path.join(ws2.ROOT, 'planner', 'written-youtrys.json')))['items']}
def SP(pts, mm, W=360, H=230, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, (-2.6, 2.6), (-2.6, 2.6), 9, 9, W=W, H=H, r=4, fs=14, ink='#000', tl_hid=False, grid=False, ticks=False, **k) + '</div>'
def side(left, f, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{f}</div></div>'
HT = table([['<b>Relative humidity (%)</b>', '<b>9 am</b>'] + [str(v) for v in H9], ['', '<b>3 pm</b>'] + [str(v) for v in H3]], head=False, cls='t tiny')
HSTEM = (q('The relative humidity (%) at 9 am and 3 pm on 14 days in November 2017 is shown in Table 3 below.') + '<b>Table 3</b>' + HT
         + q('A least squares line is to be fitted to the data with the aim of predicting the relative humidity at 3 pm (<i>humidity 3 pm</i>) from the relative humidity at 9 am (<i>humidity 9 am</i>).'))

P = [title('2G–2H', 'The coefficient of determination · Correlation and causality')]
P.append(lis(['To be able to calculate the value of the coefficient of determination.',
  'To be able to use the coefficient of determination to assess the strength of the association in terms of the explained variation.',
  'To be able to define and differentiate the concepts of association and causation.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('There is a strong positive correlation between sales of umbrellas and traffic accidents. Can we conclude that decreasing the sales of umbrellas will help decrease the number of traffic accidents?')
  + space(16, 'No. Most likely a common response to rain (more umbrellas sold and wet roads); an association does not show cause.')))
P.append(box('Question 2 · VCAA 2019 Exam 2 Q4a', HSTEM + q('a. Name the explanatory variable.') + space(8, '<i>humidity 9 am</i>'), '1 mark'))
# ---------------------------------------------------------------- 2G
P.append(sect('2G The coefficient of determination', 'Example, then you try'))
VG = 'A study was conducted to explore the effect of the time in minutes spent playing <i>video games</i> on time spent <i>studying</i> in minutes. It was determined that the correlation coefficient, <i>r</i>, for the data collected during the study is 0.6584.'
P.append(exyt('Example 17 · Calculating the coefficient of determination',
  q('If the correlation between weight and height is <i>r</i> = 0.8, find the value of the coefficient of determination. Express your answer as a percentage.') + space(14, 'r² = 0.8² = 0.64 = 64%'),
  'You try 17', q(VG) + q('a. Determine the coefficient of determination, <i>r</i>², correct to four decimal places.') + space(10, '0.6584² = 0.4335')))
P.append(exyt('Example 18 · Interpreting the coefficient of determination',
  q('In the previous example we found the coefficient of determination between height and weight to be 0.64 (or 64%). Interpret this value in terms of the variables weight and height.')
  + report([('%', a('64')), '% of the variation in ', ('RV', a('people’s weight')), ' is explained by the variation in ', ('EV', a('their height')), '.']),
  'You try 18', q(VG) + q('b. Interpret the coefficient of determination in terms of time spent studying and time spent playing video games.')
  + space(16, '43.35% of the variation in the time spent studying can be explained by the variation in the time spent playing video games.')))
for n, tx, ans_ex, yid_ in ((19, 'The level of carbon monoxide (CO) in the air measured at the roadside, and the traffic volume at the same location are linearly related, with <i>r</i> = +0.985. Determine the value of the coefficient of determination, write it in percentage terms and interpret. In this relationship, traffic volume is the explanatory variable.',
                             'r² = (0.985)² = 0.9702 = 97.0%. 97.0% of the variation in carbon monoxide levels in the air can be explained by the variation in traffic volume.', 'YT-2G-19'),
                            (20, 'Scores on tests of verbal and mathematical ability are linearly related with correlation coefficient <i>r</i> = +0.275. Determine the value of the coefficient of determination, write it in percentage terms, and interpret. In this relationship, verbal ability is the explanatory variable.',
                             'r² = (0.275)² = 0.0756 = 7.6%. Only 7.6% of the variation in scores on the mathematical ability test can be explained by the variation in scores on the verbal ability test.', 'YT-2G-20')):
    y = YTW[yid_]
    P.append(exyt(f'Example {n} · Calculating and interpreting the coefficient of determination',
      q(tx) + space(8, ans_ex.split('. ')[0]) + report([('%', a(ans_ex.split(' = ')[-1].split('.')[0] + '.' + ans_ex.split('.')[1][:1] if False else ans_ex.split('= ')[3].split('%')[0])), '% of the variation in ', ('RV', a(ans_ex.split('variation in ')[1].split(' can')[0])), ' can be explained by the variation in ', ('EV', a(ans_ex.split('variation in ')[2].rstrip('.'))), '.']),
      f'You try {n}', q(y['text'].replace('r = ', '<i>r</i> = ')) + space(26, y['answer'])))
P.append(exyt('Example 21 · Calculating r from the coefficient of determination',
  q('For the relationship described by this scatterplot, the coefficient of determination = 0.5210.<br>Determine the value of the correlation coefficient, <i>r</i>, rounded to four decimal places.') + SP(rcloud(-0.7218, 26, 21), 50) + space(12, 'r = ±√0.5210 = ±0.7218; negative association → r = −0.7218'),
  'You try 21', q('For the relationship described by this scatterplot, the coefficient of determination = 0.6384.<br>Determine the value of the correlation coefficient, <i>r</i>, rounded to four decimal places.') + SP(rcloud(0.7990, 26, 24), 50) + space(12, YTW['YT-2G-21']['answer'])))
# ---------------------------------------------------------------- 2H
P.append(sect('2H Correlation and causality', 'You try'))
P.append(box('You try 22', q('Gunther runs a cafe and collects data throughout the year on the daily number of <i>hot chocolates purchased</i>. He finds that there is a negative association between the daily number of <i>hot chocolates purchased</i> and the number of <i>daylight hours</i> on a particular day.')
  + parts([('a', 'Identify a potential third variable that could have caused this association.', 'season', 10),
           ('b', 'Has Gunther conducted an appropriate experiment to determine causation? Why or why not?', 'No. The variable season does not remain constant across the experiment.', 14)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q12', q('Data collected over a period of 10 years indicated a strong, positive association between the number of stray cats and the number of stray dogs reported each year (<i>r</i> = 0.87) in a large, regional city.<br>A positive association was also found between the population of the city and both the number of stray cats (<i>r</i> = 0.61) and the number of stray dogs (<i>r</i> = 0.72).<br>During the time that the data was collected, the population of the city grew from 34 564 to 51 055.<br>From this information, we can conclude that')
  + mc(['if cat owners paid more attention to keeping dogs off their property, the number of stray cats reported would decrease.', 'the association between the number of stray cats and stray dogs reported cannot be causal because only a correlation of +1 or –1 shows causal relationships.',
        'there is no logical explanation for the association between the number of stray cats and stray dogs reported in the city so it must be a chance occurrence.',
        'because larger populations tend to have both a larger number of stray cats and stray dogs, the association between the number of stray cats and the number of stray dogs can be explained by a common response to a third variable, which is the increasing population size of the city.',
        'more stray cats were reported because people are no longer as careful about keeping their cats properly contained on their property as they were in the past.'], 'D')
  + why('Population is associated with both: a common response.'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2019 Exam 2 Q4c', HSTEM + q('c. Determine the value of the correlation coefficient for this data set.<br>Round your answer to three decimal places.') + space(10, 'r = 0.871'), '1 mark'))

SC = ['I can calculate the value of the coefficient of determination.', 'I can use the coefficient of determination to assess the strength of the association in terms of the explained variation.', 'I understand that correlation does not imply causation.']
P.append(close(SC, [('2G', 'Q1–8'), ('2H', 'Q1–8')], ['2G', '2H']))
build('l07', '2G–2H', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l07-worksheet', '2G-2H worksheet'), ('l07-worksheet-solutions', '2G-2H worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
