"""Lesson l12 (4A) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l12/build.py
(Do Now and CFAT are not on the worksheet; l12 has no exit tasks).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 9 checklist 9C #4; APK 2 = 9A #1 (solutions worked for 12MAG).
Examples 1-2 = Cambridge U3&4 4A pp. 212-214. You trys: Edrolo U3&4 3D WE2 (p. 193); Edrolo U3&4 3E WE1a (p. 207).
Output: lessons/4A worksheet(.html/.pdf) + lessons/4A worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l12/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#000', tl_hid=False, **k) + '</div>'
def SPr(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#d00', tl_hid=False, **k) + '</div>'

P = [title('4A', 'The squared transformation')]
P.append(lis(['To be able to apply a squared transformation to either x or y.', 'To be able to fit a least squares regression line to the transformed data.',
              'To be able to use the least squares regression line fitted to the transformed data for prediction.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Complete the following table giving an <i>x</i>² transformation, and check that this linearises the data.')
  + table([['<b><i>x</i></b>', '1', '2', '5'], ['<b><i>x</i>²</b>', a('1'), a('4'), a('25')], ['<b><i>y</i></b>', '12', '27', '132']], head=False, cls='t')
  + space(14, 'slope (27 − 12) ÷ (4 − 1) = 5; (132 − 27) ÷ (25 − 4) = 5: same slope, so y against x² is linear (y = 7 + 5x²).')))
P.append(box('Question 2', q('The distance (<i>d</i>) travelled by a vehicle is directly proportional to the time (<i>t</i>) taken. Using the information in the following table, find the constant of variation.')
  + table([['<b>Time (<i>t</i>)</b>', '1', '2', '3'], ['<b>Distance (<i>d</i>)</b>', '95', '190', '285']], head=False, cls='t')
  + space(12, 'd = kt, so k = d ÷ t = 95 ÷ 1 = 95')))
# ---------------------------------------------------------------- 4A
P.append(sect('4A The squared transformation', 'Example, then you try'))
ja, jb = lsq([t * t for t in TIME], JUMP)
P.append(exyt('Example 1 · Applying the x-squared transformation',
  q('A base jumper leaps from the top of a cliff, 1560 metres above the valley floor. The scatterplot below shows the height (in metres) of the base jumper above the valley floor every second, for the first 10 seconds of the jump.')
  + SP(list(zip(TIME, JUMP)), (0, 10), (1000, 1600), 1, 100, 'Time (seconds)', 'Height (metres)', 70)
  + q('A scatterplot shows that there is a strong negative association between the height of the base jumper above the ground and time.')
  + q('a. Apply a squared transformation to the variable time, and determine the least squares regression line for the transformed data.')
  + table([['<b>time</b>'] + TIME, ['<b>time²</b>'] + [a(t * t) for t in TIME]], head=False, cls='t tiny')
  + q('<i>height</i> = ' + a('1560') + ' − ' + a('4.90') + ' × ' + a('<i>time</i>²'))
  + q('b. Use the least squares equation to predict to the nearest metre the height of the base jumper after 3.4 seconds.')
  + q('<i>height</i> = ' + a('1560 − 4.90 × 3.4² = 1503 m')),
  'You try 1', q('A scatterplot was constructed from the following data.')
  + T([['<b><i>x</i></b>'] + EX, ['<b><i>y</i></b>'] + EY])
  + q('Apply an <i>x</i>-squared transformation and plot the transformed data.')
  + space(62, 'x² = 9, 16, 25, 36, 49' + SPr([(x * x, y) for x, y in zip(EX, EY)], (0, 50), (0, 60), 10, 10, 'x²', 'y', 62))))
P.append(exyt('Example 2 · Applying the y-squared transformation',
  q('In a study of the effectiveness of fertiliser on the yield of strawberry plants, differing amounts of liquid fertiliser (in mL) were given to groups of plants, and their average yield (in kg) measured.')
  + SP(list(zip(FERT, YLD)), (0, 10), (2, 6), 2, 1, 'fertiliser (ml)', 'yield (kg)', 66)
  + q('A scatterplot shows that there is a strong positive association between the fertiliser and yield.')
  + q('a. Apply a squared transformation to the variable yield, and determine the least squares regression line for the transformed data.')
  + q('<i>yield</i>² = ' + a('4.45') + ' + ' + a('2.29') + ' × <i>fertiliser</i>')
  + q('b. Use the least squares equation to predict the yield of a plant given 6.5 mL of fertiliser, giving your answer to 1 decimal place.')
  + q('<i>yield</i>² = ' + a('4.45 + 2.29 × 6.5 = 19.34'))
  + q('<i>yield</i> = √' + a('19.34') + ' = ' + a('4.4 kg (positive root only)')),
  'You try 2', q('Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <i>distance</i>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.')
  + T([['<b>week</b>'] + WEEK, ['<b>distance (km)</b>'] + DIST])
  + SP(list(zip(WEEK, DIST)), (0, 10), (0, 8), 1, 1, 'week', 'distance (km)', 62)
  + q('a. Apply a squared transformation to the variable <i>distance</i> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.')
  + space(30, 'distsq = dist²; Linear Reg: XList week, YList distsq<br>(distance)² = −1.361 + 6.697 × week')))
SC = ['I can apply the x² transformation.', 'I can apply the y² transformation.']
P.append(close(SC, [('4A', 'Q1–10')], ['4A']))
build('l12', '4A', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l12-worksheet', '4A worksheet'), ('l12-worksheet-solutions', '4A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
