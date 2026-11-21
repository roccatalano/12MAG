"""Lesson l05 (2D, 2E) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l05/build.py.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 7 skills checklist 7B #3 (data from #2, p. 457; solution written for 12MAG); APK 2 = VCAA 2020 Further Exam 2 Core Q4bi (Edrolo U1&2 6A Q16).
CAS You try = Edrolo U3&4 2C WE3. Examples 13-15 = Cambridge U3&4 Examples 13-15 (pp. 135-138). You try 13-15 = Edrolo U1&2 6B WE3, 6B WE1, Edrolo U3&4 2C WE4.
Exits = Edrolo U3&4 2C Q15 (VCAA 2018 Exam 2 Core Q2b), Q16 (VCAA 2016 Exam 2 Core Q3a).
Figures redrawn (values in tools/deck/l05/figs.py). Output: lessons/2D-2E worksheet(.html/.pdf) + lessons/2D-2E worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l05/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *

def SP(pts, xr, yr, xt, yt, xl, yl, mm, red=False, W=420, H=300, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=W, H=H, r=4, fs=14, ink=RED if red else '#000', tl_hid=False, **k) + '</div>'
def side(left, f, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{f}</div></div>'
def htab(rows, cls='t tiny'): return table(rows, head=False, cls=cls)
DFSR = lambda d, f, s, o=None: report(['Direction: ', ('positive / negative', d), ' · Form: ', ('linear / non-linear', f), ' · Strength: ', ('weak / moderate / strong', s)] + ([' · Outliers: ', ('any?', o)] if o else []))

P = [title('2D–2E', 'Investigating associations between two numerical variables · How to interpret a scatterplot')]
P.append(lis(['To be able to introduce the scatterplot for displaying data from two numerical variables.', 'To be able to construct a scatterplot using a CAS calculator.',
  'To be able to use a scatterplot to identify an association between two variables.',
  'From the the scatterplot, be able to classify an association according to: direction, which may be positive or negative; form, which may be linear or non-linear; strength, which may be weak, moderate or strong.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
FT = htab([['<b>height</b>'] + [str(h) for h, _ in FOOT[:8]], ['<b>foot length</b>'] + [str(f) for _, f in FOOT[:8]], ['<b>height</b>'] + [str(h) for h, _ in FOOT[8:]], ['<b>foot length</b>'] + [str(f) for _, f in FOOT[8:]]])
P.append(pair(
  box('Question 1', q('In order to predict the length of a person’s foot from their height, a group of 16 students collected the following data set, which gives height (<i>height</i>) and the length of their foot (<i>foot length</i>) in centimetres.')
      + FT + SP(FOOT, (150, 190), (15, 45), 5, 5, 'height (cm)', 'foot length (cm)', 62)
      + q('Describe the association in the previous scatterplot between height and foot length in terms of direction, form and strength.')
      + space(16, 'There is a moderate, positive, linear association between foot length and height: taller students tend to have longer feet. (Possible outlier: 185 cm, 40 cm.)')),
  box('Question 2 · VCAA 2020 Exam 2 Q4bi', q('The age, in years, body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 men aged 23 to 25 years are shown in the table below.')
      + table([['<i>Age</i> (years)', '<i>Body density</i> (kg/litre)', '<i>Weight</i> (kg)']] + [[str(x), f'{y:.2f}', f'{z:.1f}'] for x, y, z in V20], cls='t tiny')
      + q('A least squares line is to be fitted to the data with the aim of predicting body density from weight.<br>i. Name the explanatory variable for this least squares line.')
      + space(8, 'weight'), '1 mark')))

# ---------------------------------------------------------------- 2D
P.append(sect('2D Investigating associations between two numerical variables', 'You try (CAS)'))
P.append(box('You try · CAS', q('10 students were competing in the school cross-country. Each student’s house would be awarded <i>points</i> based on their placing in the race. The <i>time</i> that it took each student to complete the race and the number of house <i>points</i> they received were recorded.')
  + table([['<i>time</i> (seconds)'] + [str(t) for t, _ in CROSS], ['<i>points</i>'] + [str(p) for _, p in CROSS]], head=False, cls='t tiny')
  + q('With a calculator, use the data in the table to construct a scatterplot.')
  + solfig(50, SP(CROSS, (680, 940), (0, 11), 40, 1, 'time (seconds)', 'points', 80, red=True, H=260))))

# ---------------------------------------------------------------- 2E
P.append(sect('2E How to interpret a scatterplot', 'Example, then you try'))
m = lambda pts, xr, yr, xt, yt, xl, yl, **k: SP(pts, xr, yr, xt, yt, xl, yl, 30, W=230, H=190, **k)
P.append(exyt('Example 13 · Direction of association',
  q('Classify each of the following scatterplots as exhibiting positive, negative or no association. Where there is an association, describe the direction of the association in terms of the variables in the scatterplot and what it means in terms of the variables involved.')
  + '<div class="row" style="gap:1mm">' + m(E13A, (0, 6), (0, 70), 1, 10, 'Dose (mg)', 'Reaction time (min)') + m(E13B, (20, 36), (0, 25), 4, 5, 'Age (years)', 'Diameter (cm)') + m(E13C, (145, 180), (145, 180), 5, 5, 'Height mother', 'Height daughter') + '</div>'
  + parts([('a', report(['The direction of the association is ', ('positive / negative / none', 'negative'), '. Reaction times tend to ', ('increase / decrease', 'decrease'), ' as the drug dose increases.']), '', 0),
           ('b', report(['There ', ('is / is no', 'is no'), ' association between diameter and age.']), '', 0),
           ('c', report(['The direction of the association is ', ('positive / negative / none', 'positive'), '. Taller mothers tend to have ', ('taller / shorter', 'taller'), ' daughters.']), '', 0)]),
  'You try 13', q('The relationship between customer satisfaction and burger patty size at a fast food restaurant is shown in the following scatterplot.')
  + SP(W3, (0, 20), (0, 20), 5, 5, 'burger patty diameter (cm)', 'customer satisfaction level (0–20)', 66)
  + q('Interpret the correlation between <i>burger patty diameter</i> and <i>customer satisfaction level</i>.')
  + space(16, 'An increase in burger patty diameter is associated with an increase in customer satisfaction level.')))
P.append(exyt('Example 14 · Form of an association', q('Classify the form of the association in each of scatterplot as linear or non-linear.')
  + '<div class="row" style="gap:2mm">' + SP(E13C, (145, 180), (145, 180), 5, 5, 'Height mother', 'Height daughter', 42, W=320, H=250) + SP(E14B, (1, 7), (0, 14), 1, 2, 'Number of weeks on a diet', 'Weight loss (kg)', 42, W=320, H=250) + '</div>'
  + parts([('a', report(['The association is ', ('linear / non-linear', 'linear'), '.']), '', 0), ('b', report(['The association is ', ('linear / non-linear', 'non-linear'), '.']), '', 0)]),
  'You try 14', q('Consider the following scatterplot.') + SP(W1, (0, 11.5), (0, 15), 2, 2, 'x', 'y', 66)
  + q('Describe the relationship in terms of strength, direction and form.') + space(12, 'Moderate, positive, linear relationship')))
P.append(exyt('Example 15 · Strength of an association', q('Classify the <b>strength</b> of the association in each of the following scatterplots.')
  + '<div class="row" style="gap:2mm">' + SP(E15A, (5, 25), (5, 45), 5, 10, 'X', 'Y', 42, W=320, H=250) + SP(E15B, (0, 20), (5, 25), 5, 5, 'X', 'Y', 42, W=320, H=250) + '</div>'
  + parts([('a', report(['The association is ', ('weak / moderate / strong', 'weak'), '.']), '', 0), ('b', report(['The association is ', ('weak / moderate / strong', 'strong'), '.']), '', 0)]),
  'You try 15', q('An investigation into the association between sleep and work performance was conducted. The following scatterplot displays the collected data.')
  + SP(SLEEP, (0, 10), (0, 12), 2, 2, 'amount of sleep (hours)', 'number of basic errors', 62)
  + q('Describe the relationship in terms of strength, direction, form and potential outliers.')
  + space(14, 'The scatterplot displays a strong, negative, linear relationship, with no visible outliers.')))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q2b', side(q('The congestion level in a city can also be recorded as the percentage increase in travel time due to traffic congestion in peak periods (compared to non-peak periods).<br>This is called the percentage congestion level.<br>The percentage congestion levels for the morning and evening peak periods for 19 large cities are plotted on the scatterplot below.')
  + q('A least squares line is to be fitted to the data with the aim of predicting evening congestion level from morning congestion level.<br>The equation of this line is<br><i>evening congestion level</i> = 8.48 + 0.922 × <i>morning congestion level</i>')
  + q('Name the response variable in this equation.') + space(8, 'evening congestion level'),
  SP(V18, (35, 70), (35, 75), 5, 5, 'morning congestion level (%)', 'evening congestion level (%)', 66), 68), '1 mark'))
P.append(box('Exit task 2 · VCAA 2016 Exam 2 Q3a', q('The data in the table below shows a sample of actual temperatures and apparent temperatures recorded at the weather station. A scatterplot of the data is also shown.<br>The data will be used to investigate the association between the variables <i>apparent temperature</i> and <i>actual temperature</i>.')
  + side(table([['Apparent temperature (°C)', 'Actual temperature (°C)']] + [[str(b), str(a_)] for a_, b in V16], cls='t tiny'),
         '<div style="position:relative">' + SP(V16, (20, 29), (16, 26), 1, 1, 'actual temperature (°C)', 'apparent temperature (°C)', 72) + '<div style="position:absolute;right:6mm;bottom:14mm;font-size:8pt"><i>n</i> = 13<br><i>r</i>² = 0.97</div></div>', 76)
  + q('a. Use the scatterplot to describe the association between <i>apparent temperature</i> and <i>actual temperature</i> in terms of strength, direction and form.')
  + space(10, 'strong, positive, linear'), '1 mark'))

SC = ['I can construct a scatterplot using a CAS calculator.', 'I can classify the direction, form and strength of an association from a scatterplot.']
P.append(close(SC, [('2D', 'Q1–6'), ('2E', 'Q1–2')], ['2D', '2E']))
if WB: P.append(practice(['2D', '2E']))  # workbook edition only: practice sections (Insight + Cambridge skill sheets) flow on after the exits
build('l05', '2D–2E', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (() if WB else (('l05-worksheet', '2D-2E worksheet'), ('l05-worksheet-solutions', '2D-2E worksheet solutions'))):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
