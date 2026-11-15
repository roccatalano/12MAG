"""Lesson l06 (2F) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l06/build.py.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1-2 = Cambridge U1&2 Ch 7 skills checklist 7C #4, #5 (height/foot length data of 7B #2, p. 457; solutions written for 12MAG);
APK 3 = VCAA 2016 Further Exam 1 Q12 (Edrolo U1&2 6B Q15, original wording). Example 16 = Cambridge U3&4 Example 16 (p. 144).
You try 16 = Edrolo U3&4 2D Worked example 1 (pp. 146-148). Exit = Edrolo U3&4 2C Q17 (VCAA 2020 Exam 2 Core Q6b).
Output: lessons/2F worksheet(.html/.pdf) + lessons/2F worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l06/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *

def SP(pts, xr, yr, xt, yt, xl, yl, mm, W=420, H=300, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=W, H=H, r=4, fs=14, ink='#000', tl_hid=False, **k) + '</div>'
def side(left, f, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{f}</div></div>'
STR = [('0.75 ≤ <i>r</i> ≤ 1', 'strong positive'), ('0.5 ≤ <i>r</i> &lt; 0.75', 'moderate positive'), ('0.25 ≤ <i>r</i> &lt; 0.5', 'weak positive'), ('−0.25 &lt; <i>r</i> &lt; 0.25', 'no association'),
       ('−0.5 &lt; <i>r</i> ≤ −0.25', 'weak negative'), ('−0.75 &lt; <i>r</i> ≤ −0.5', 'moderate negative'), ('−1 ≤ <i>r</i> ≤ −0.75', 'strong negative')]
STRT = table([['<i>r</i>', 'linear association']] + [list(x) for x in STR], cls='t tiny')
rf = corr(*zip(*FOOT))

P = [title('2F', 'Strength of a linear relationship: the correlation coefficient')]
P.append(lis([x for x in ['To introduce Pearson’s correlation coefficient r as a measure of the strength of a linear association between two variables.',
  'To be able to use technology to determine the value of Pearson’s correlation coefficient r.',
  'To be able to classify the strength of a linear association as weak, moderate or strong based on the value of Pearson’s correlation coefficient r.']]))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
FT = table([['<b>height</b>'] + [str(h) for h, _ in FOOT[:8]], ['<b>foot length</b>'] + [str(f) for _, f in FOOT[:8]], ['<b>height</b>'] + [str(h) for h, _ in FOOT[8:]], ['<b>foot length</b>'] + [str(f) for _, f in FOOT[8:]]], head=False, cls='t tiny')
P.append(box('Questions 1 and 2', q('Height (<i>height</i>) and foot length (<i>foot length</i>) of 16 students, in centimetres:')
  + side(FT, SP(FOOT, (150, 190), (15, 45), 5, 5, 'height (cm)', 'foot length (cm)', 62, H=260), 64)
  + '<b>Question 1</b>' + q('Estimate the value of the correlation coefficient, <i>r</i>, between height and foot length by comparing the scatterplot to those on page 420, and then use your calculator to find its exact value. Give your answer rounded to three decimal places.')
  + space(12, f'estimate r ≈ 0.7 (positive, more scattered than r = 0.9) · CAS: r = {rf:.3f}') + QSEP
  + '<b>Question 2</b>' + side(q('Use the table on page 428 to classify the value of the correlation coefficient, <i>r</i>, between height and foot length as weak, moderate or strong.')
  + space(10, f'0.5 ≤ {rf:.3f} &lt; 0.75 → moderate'), STRT, 62)))
P.append(box('Question 3 · VCAA 2016 Exam 1 Q12', q('There is a strong positive association between a country’s Human Development Index and its carbon dioxide emissions.<br>From this information, it can be concluded that')
  + mc(['increasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.', 'decreasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.',
        'this association must be a chance occurrence and can be safely ignored.', 'countries that have higher human development indices tend to have higher levels of carbon dioxide emissions.',
        'countries that have higher human development indices tend to have lower levels of carbon dioxide emissions.'], 'D')
  + why('A positive association: higher HDI goes with higher CO₂. An association does not show cause (A, B).'), '1 mark'))

# ---------------------------------------------------------------- 2F
P.append(sect('2F Strength of a linear relationship: the correlation coefficient', 'Example, then you try'))
P.append(exyt('Example 16 · Classifying the strength of a linear association',
  q('Classify the strength of each of the following linear associations using the previous table:') + STRT
  + parts([('a', '<i>r</i> = 0.35', 'weak, positive', 'L'), ('b', '<i>r</i> = −0.507', 'moderate, negative', 'L'),
           ('c', '<i>r</i> = 0.992', 'strong, positive', 'L'), ('d', '<i>r</i> = −0.159', 'no association', 'L')], cols=2),
  'You try 16', q('A survey followed the study habits of a group of first-year uni students with the aim of predicting their <i>grade</i>, as a percentage, from the number of <i>lectures attended</i>. The results are shown in the following table.')
  + table([['<i>grade</i> (%)'] + [str(g) for g in GRADE], ['<i>lectures attended</i>'] + [str(l) for l in LECT]], head=False, cls='t tiny')
  + parts([('a', 'Is the Pearson correlation coefficient, <i>r</i>, an appropriate statistic for this data set?', 'Yes, the Pearson correlation coefficient is an appropriate statistic for this data set (numeric, linear, no outliers).', 14),
           ('b', 'Determine the value of the correlation coefficient. Give the value correct to two decimal places.', 'r = 0.85', 8),
           ('c', 'If possible, describe the association between the variables in terms of strength, direction, and form.', 'Strong, positive, linear association', 10)])))

# ---------------------------------------------------------------- exit
P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2020 Exam 2 Q6b', q('The table below shows the <i>mean age</i>, in years, and the <i>mean height</i>, in centimetres, of 648 women from seven different age groups.')
  + table([['', *AGEGRP], ['<i>Mean age</i> (years)', *map(str, AGE)], ['<i>Mean height</i> (cm)', *map(str, HT)]], cls='t tiny')
  + side(q('A scatterplot displaying this data shows an association between the <i>mean height</i> and the <i>mean age</i> of these women. In an initial analysis of the data, a line is fitted to the data by eye, as shown.')
         + q('b. Describe this association in terms of strength and direction.') + space(12, 'strong, negative'),
         SP(list(zip(AGE, HT)), (20, 90), (155, 170), 10, 5, 'mean age (years)', 'mean height (cm)', 74, H=250, tl=((19, 168.2), (91, 155.9))), 76), '1 mark'))

SC = ['I can use technology to determine the value of the correlation coefficient r.', 'I can classify the strength of a linear association as weak, moderate or strong based on the value of the correlation coefficient r.']
P.append(close(SC, [('2F', 'Q1–4')], ['2F']))
build('l06', '2F', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l06-worksheet', '2F worksheet'), ('l06-worksheet-solutions', '2F worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
