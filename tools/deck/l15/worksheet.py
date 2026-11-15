"""Lesson l15 (4D) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l15/build.py
(Do Now is not on the worksheet).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 9 checklist 9E #11; APK 2 = 9B #3 (graph redrawn); APK 3 = Edrolo U1&2 9B Q22 (adapted from VCAA 2021 Exam 2 Q2a).
Example 7 = Cambridge U3&4 4D pp. 240-242 (figures cropped from the textbook). You try: Edrolo U3&4 3E Worked example 1d (pp. 207-211).
Exits: Edrolo U3&4 3D Q14 (VCAA 2009 Exam 1 Q12); Edrolo U3&4 3E Q13 (VCAA 2020 Exam 2 Q6d, original wording).
Output: lessons/4D worksheet(.html/.pdf) + lessons/4D worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l15/worksheet.py"""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, **{'ink':'#000','tl_hid':False,**k}) + '</div>'
def IMG(f, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"img",f),"rb").read()).decode()}" style="width:{mm}mm;display:block;margin:1mm auto">'
HYP = ''.join(f'{"M" if i==0 else "L"}{40+i*4},{int(200-170/(1+i*0.18))}' for i in range(60))
GR = (f'<svg viewBox="0 0 300 230" style="width:55mm;display:block;margin:1mm auto"><line x1="30" y1="10" x2="30" y2="210" stroke="#000" stroke-width="2"/><line x1="30" y1="210" x2="290" y2="210" stroke="#000" stroke-width="2"/>'
      f'<text x="16" y="20" font-size="14" font-style="italic">y</text><text x="282" y="226" font-size="14" font-style="italic">x</text><text x="18" y="226" font-size="13">0</text><path d="{HYP}" fill="none" stroke="#000" stroke-width="2.5"/></svg>')
MA = [26.3, 35.2, 45.2, 55.3, 65.1, 74.8, 83.1]; MH = [167.1, 164.9, 164.8, 163.4, 161.2, 158.4, 156.7]
RES = [-0.334, -0.959, 0.709, 1.096, 0.629, -0.455, -0.687]

P = [title('4D', 'Choosing and applying the appropriate transformation')]
P.append(lis(['To be able to use the circle of transformations to determine which transformations may help linearise a non-linear association.',
              'To be able to use a residual plot to assess the effectiveness of a data transformation.',
              'To be able to use the coefficient of determination to assess the effectiveness of a data transformation.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Find a rule connecting the variables <i>x</i> and <i>y</i> if the data in the given table has undergone an <i>x</i>² transformation.')
  + table([['<b><i>x</i></b>', '1', '5', '10', '15'], ['<b><i>x</i>²</b>', '1', '25', '100', '225'], ['<b><i>y</i></b>', '23', '95', '320', '695']], head=False, cls='t')
  + space(14, 'slope = (95 − 23) ÷ (25 − 1) = 3; 23 = 3 × 1 + c, c = 20<br>y = 3x² + 20')))
P.append(box('Question 2', q('Does the following graph show direct or inverse variation?') + GR + space(8, 'inverse variation (y decreases as x increases: y = k/x)')))
P.append(box('Question 3 · adapted from VCAA 2021 Exam 2 Q2a', q('The two running events in the heptathlon are the 200 m run and the 800 m run. The times taken by the athletes in these two events, <i>time200</i> and <i>time800</i>, are linearly related.')
  + q('When a line of good fit is fitted to the data, the equation of this line is found to be')
  + q('<span style="display:block;text-align:center"><i>time800</i> = 0.03921 + 5.2756 × <i>time200</i></span>')
  + q('Round the values for the intercept and the slope to three significant figures.<br>Write your answers in the boxes provided.')
  + q('<span style="display:block;text-align:center"><i>time800</i> = ' + a('0.0392') + ' + ' + a('5.28') + ' × <i>time200</i></span>')))
# ---------------------------------------------------------------- 4D
P.append(sect('4D Choosing and applying the appropriate transformation', 'Example, then you try'))
P.append(exyt('Example 7 · Choosing the best transformation',
  q('The scatterplot shows the age (in years) and diameter at a height of 1.5 metre (in cm) for a sample of 19 trees of the same species. Use an appropriate transformation to find a regression model which allows the age of this species of tree to be predicted from its diameter.')
  + IMG('ex7.png', 55)
  + q('Possible transformations (circle of transformations): ' + a('x², 1/y, log y'))
  + table([['<b>Transformation</b>', '<b>Residual plot</b>', '<b>r²</b>'], ['<i>x</i>²', a('no clear pattern'), a('92.7%')], ['1/<i>y</i>', a('still curved'), a('75.7%')], ['log <i>y</i>', a('no clear pattern'), a('90.2%')]], head=False, cls='t')
  + q('Best: ' + a('x² (similar r² to log y, easier to interpret)'))
  + q('<i>age</i> = ' + a('5.098') + ' + ' + a('0.091') + ' × ' + a('diameter²')),
  'You try', q('Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <i>distance</i>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.')
  + T([['<b>week</b>'] + WEEK, ['<b>distance (km)</b>'] + DIST])
  + SP(list(zip(WEEK, DIST)), (0, 10), (0, 8), 1, 1, 'week', 'distance (km)', 62)
  + q('Parts a–c: (distance)² against week · distance against log<sub>10</sub>(week) · distance against 1/week')
  + q('d. Determine which transformation is the best fit for the data set.')
  + space(40, 'r²: (distance)² 0.9732 · log<sub>10</sub>(week) 0.9959 · 1/week 0.9221<br>Largest r² = 0.9959: the log transformation on week<br>distance = 0.997 + 6.971 × log<sub>10</sub>(week)')))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'VCAA'))
P.append(box('Exit task 1 · VCAA 2009 Exam 1 Q12', q('The <i>mathematics achievement</i> level (TIMSS score) for grade 8 students and the general rate of <i>internet use</i> (%) for 10 countries are displayed in the following scatterplot.')
  + IMG('timss.png', 70) + q('To linearise the data, it would be best to plot')
  + mc(['<i>mathematics achievement</i> against <i>internet use</i>.', 'log<sub>10</sub>(<i>mathematics achievement</i>) against <i>internet use</i>.', '<i>mathematics achievement</i> against log<sub>10</sub>(<i>internet use</i>).',
        '<i>mathematics achievement</i> against (<i>internet use</i>)².', '1/<i>mathematics achievement</i> against <i>internet use</i>.'], 'C')
  + why('increasing, curving over (top-left quarter): y², log x or 1/x; only log x is offered')))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q6d', q('The table below shows the mean age, in years, and the mean height, in centimetres, of 648 women from seven different age groups.')
  + T([['<b>Mean age (years)</b>'] + MA, ['<b>Mean height (cm)</b>'] + MH])
  + q('d. In a further analysis of the data, a least squares line was fitted.<br>The associated residual plot that was generated is shown below.')
  + SP(list(zip(MA, RES)), (20, 90), (-1, 1), 10, 0.5, 'mean age (years)', 'residual', 70)
  + q('The residual plot indicates that the association between the mean height and the mean age of women is non-linear.<br>The data … can be linearised by applying an appropriate transformation to the variable <i>mean age</i>.')
  + q('Apply an appropriate transformation to the variable <i>mean age</i> to linearise the data. Fit a least squares line to the transformed data and write its equation below.<br>Round the values of the intercept and the slope to four significant figures. (2 marks)')
  + space(22, 'x² transformation on mean age: Linear Reg XList age², YList height<br>mean height = 167.9 − 0.001621 × (mean age)²')))
SC = ['I can choose the best transformation to apply.']
P.append(close(SC, [('4D', 'Q1–4')], ['4D']))
build('l15', '4D', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l15-worksheet', '4D worksheet'), ('l15-worksheet-solutions', '4D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
