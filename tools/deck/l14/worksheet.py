"""Lesson l14 (4C) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l14/build.py
(Do Now is not on the worksheet).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 9 checklist 9C #5; APK 2 = 9A #2 (solutions worked for 12MAG).
Examples 5-6 = Cambridge U3&4 4C pp. 231-233. You trys: Edrolo U3&4 3E Worked example 1c (p. 210); Edrolo U3&4 3D Worked example 4 (pp. 198-199).
Exit: Edrolo U3&4 3E Q11 (VCAA 2018 Exam 1 Q11).
Output: lessons/4C worksheet(.html/.pdf) + lessons/4C worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l14/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, **{'ink':'#000','tl_hid':False,**k}) + '</div>'
FR = lambda n, d: f'<sup>{n}</sup>&frasl;<sub>{d}</sub>'

P = [title('4C', 'The reciprocal transformation')]
P.append(lis(['To be able to apply a reciprocal transformation to either x or y.', 'To be able to fit a least squares regression line to the transformed data.',
              'To be able to use the least squares regression line fitted to the transformed data for prediction.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Complete the following table giving a 1/<i>x</i> transformation, and check that this linearises the data.')
  + table([['<b><i>x</i></b>', '0.5', '0.2', '0.1'], ['<b>1/<i>x</i></b>', a('2'), a('5'), a('10')], ['<b><i>y</i></b>', '5', '35', '85']], head=False, cls='t')
  + space(12, 'slopes: 30 ÷ 3 = 10 and 50 ÷ 5 = 10: same slope, so y against 1/x is linear (y = −15 + 10 × 1/x).')))
P.append(box('Question 2', q('If <i>F</i> is inversely proportional to <i>d</i>, use the following table to find the constant of variation.')
  + table([['<b><i>d</i></b>', '10', '20', '50'], ['<b><i>F</i></b>', '10', '5', '2']], head=False, cls='t')
  + space(10, 'k = F × d = 10 × 10 = 100 (F = 100/d)')))
# ---------------------------------------------------------------- 4C
P.append(sect('4C The reciprocal transformation', 'Example, then you try'))
P.append(exyt('Example 5 · Applying the reciprocal (1/x) transformation',
  q('After embarking on a new healthy eating and exercise plan, Ben recorded his weekly weight loss over a 10 week. The association is not linear, as can be seen in the scatterplot below which plots <i>weekly weight loss</i> in kg against <i>length of diet</i> in weeks.')
  + SP(list(zip(BWK, LOSS)), (0, 10), (0, 6), 2, 1, 'length of diet (weeks)', 'weekly weight loss (kg)', 66)
  + q('The scatterplot shows that there is a strong negative association between <i>weekly weight loss</i> and <i>length of diet</i>.')
  + q('a. Apply a reciprocal transformation to the variable <i>length of diet</i>, and determine the least squares regression line for the transformed data.')
  + q('<i>weekly weight loss</i> = ' + a('0.13') + ' + ' + a('5.09') + ' × ' + a('1/<i>length of diet</i>'))
  + q('b. Use the least squares equation to predict the <i>weekly weight loss</i> in week 11, giving your answer to one decimal place.')
  + q('<i>weekly weight loss</i> = ' + a('0.13 + 5.09 ÷ 11 = 0.6 kg')),
  'You try 1', q('Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <i>distance</i>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.')
  + T([['<b>week</b>'] + WEEK, ['<b>distance (km)</b>'] + DIST])
  + SP(list(zip(WEEK, DIST)), (0, 10), (0, 8), 1, 1, 'week', 'distance (km)', 62)
  + q('c. Apply a reciprocal transformation to the variable <i>week</i> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.')
  + space(30, 'weekrec = 1/week; Linear Reg: XList weekrec, YList dist<br>distance = 7.826 − 7.701 × 1/week')))
P.append(exyt('Example 6 · Applying the reciprocal (1/y) transformation',
  q('A homeware company makes rectangular sticky labels with a variety of lengths and widths.<br>The scatterplot below displays the width (in cm) and length (in cm) of eight of the sticky labels.')
  + SP(list(zip(LEN, WID)), (3.5, 7), (1.5, 3.5), 0.5, 0.5, 'Length (cm)', 'Width (cm)', 66)
  + q('The scatterplot shows that there is a strong negative association between the width of the sticky labels and their lengths, but it is clearly non-linear.')
  + q('a. Apply a reciprocal transformation to the variable width, and determine the least squares regression line for the transformed data.')
  + q('1/<i>width</i> = ' + a('0.015') + ' + ' + a('0.086') + ' × <i>length</i>')
  + q('b. Use the least squares equation to predict the width of a sticky label which is 5 cm long, giving your answer to two decimal places.')
  + q('1/<i>width</i> = ' + a('0.015 + 0.086 × 5 = 0.445'))
  + q('<i>width</i> = 1 ÷ ' + a('0.445') + ' = ' + a('2.25 cm')),
  'You try 2', q('A class of ten students recorded the time they spent studying for their psychology test. The number of questions they got incorrect are shown in the table.')
  + T([['<b>hours studied</b>'] + HRS, ['<b>questions incorrect</b>'] + QI])
  + q('Apply a <i>y</i>-reciprocal transformation (1/<i>y</i>) and plot the transformed data.')
  + space(60, 'quesrec = 1/ques: 0.016, 0.031, 0.043, 0.059, 0.063, 0.071, 0.125, 0.143, 0.2, 0.2'
          + SP([(h, 1 / v) for h, v in zip(HRS, QI)], (0, 7.5), (0, 0.22), 1, 0.04, 'hours', 'quesrec', 60, ink='#c00'))))
# ---------------------------------------------------------------- exit
P.append(sect('Exit task', 'VCAA'))
P.append(box('Exit task 1 · VCAA 2018 Exam 1 Q11', q('Freya uses the following data to generate the scatterplot below.')
  + T([['<b><i>x</i></b>'] + FX, ['<b><i>y</i></b>'] + FY])
  + SP(list(zip(FX, FY)), (0, 10), (0, 120), 1, 20, 'x', 'y', 70)
  + q('The scatterplot shows that the data is non-linear.<br>To linearise the data, Freya applies a reciprocal transformation to the variable <i>y</i>.<br>She then fits a least squares line to the transformed data.<br>With <i>x</i> as the explanatory variable, the equation of this least squares line is closest to')
  + mc(['1/<i>y</i> = −0.0039 + 0.012<i>x</i>', '1/<i>y</i> = −0.025 + 1.1<i>x</i>', '1/<i>y</i> = 7.8 − 0.082<i>x</i>', '<i>y</i> = 45.3 + 59.7 × 1/<i>x</i>', '<i>y</i> = 59.7 + 45.3 × 1/<i>x</i>'], 'A', cols=2)
  + why('1/y against x on CAS: a = −0.00395, b = 0.0118')))
SC = ['I can apply the reciprocal (1/x) transformation.', 'I can apply the reciprocal (1/y) transformation.']
P.append(close(SC, [('4C', 'Q1–9')], ['4C']))
build('l14', '4C', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l14-worksheet', '4C worksheet'), ('l14-worksheet-solutions', '4C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
