"""Lesson l13 (4B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l13/build.py
(Do Now is not on the worksheet).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 9 checklist 9D #9; APK 2 = 9D #10 (solutions worked for 12MAG); APK 3 = Edrolo U1&2 8D Q14 (p. 473), adapted by Edrolo from VCAA 2017 Exam 1 Q4.
Examples 3-4 = Cambridge U3&4 4B pp. 221-223. You trys: Edrolo U3&4 3E Worked example 1b (pp. 208-209); YT-4B-4 written for 12MAG (planner/written-youtrys.json).
Exits: Edrolo U3&4 3E Q10 (VCAA 2020 Exam 1 Q14); Edrolo U3&4 3E Q12a-b (VCAA 2017 Exam 2 Q4b, Q4ci).
Output: lessons/4B worksheet(.html/.pdf) + lessons/4B worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l13/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import *
def T(rows, cls='t tiny'): return table([[str(c) for c in r] for r in rows], head=False, cls=cls)
def SP(pts, xr, yr, xt, yt, xl, yl, mm, **k):
    return f'<div style="max-width:{mm}mm;margin:1mm auto">' + scat(pts, xr, yr, xt, yt, xl, yl, W=420, H=230, r=4, fs=13, ink='#000', tl_hid=False, **k) + '</div>'

P = [title('4B', 'The log transformation')]
P.append(lis(['To be able to apply a log10 transformation to either x or y.', 'To be able to fit a least squares regression line to the transformed data.',
              'To be able to use the least squares regression line fitted to the transformed data for prediction.']))
# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Find the number whose logarithm is 2.1567 to one decimal place.') + space(12, '10<sup>2.1567</sup> = 143.4')))
P.append(box('Question 2', q('Complete the following table giving a log<sub>10</sub>(<i>x</i>) transformation, and check that this linearises the data.')
  + table([['<b><i>x</i></b>', '10', '100', '1000'], ['<b>log<sub>10</sub>(<i>x</i>)</b>', a('1'), a('2'), a('3')], ['<b><i>y</i></b>', '3', '6', '9']], head=False, cls='t')
  + space(12, 'each increase of 1 in log x adds 3 to y: same slope, so y against log x is linear (y = 3 log x).')))
P.append(box('Question 3 · VCAA 2017 Exam 1 Q4 (adapted)', q('The following histogram shows the distribution of log<sub>10</sub>(<i>population</i>) of 12 towns.')
  + barchart(['0–1', '1–2', '2–3', '3–4', '4–5'], POPF, 3, 1, 'log10(population)', 'frequency', mm=70)
  + q('The median population of these towns is between')
  + mc(['2 and 3', '3 and 4', '100 and 1000', '1000 and 10 000', '10 000 and 100 000'], 'C', cols=3)
  + why('6th and 7th towns are in the 2–3 column; 10² = 100, 10³ = 1000.')))
# ---------------------------------------------------------------- 4B
P.append(sect('4B The log transformation', 'Example, then you try'))
P.append(exyt('Example 3 · Applying the log x transformation',
  q('The general wealth of a country, often measured by its Gross Domestic Product (GDP), is one of several variables associated with lifespan in different countries. However, the association is not linear, as can be seen in the scatterplot below which plots lifespan (in years) against GDP per person (in dollars) for 13 different countries.')
  + SP(list(zip(GDP, LIFESPAN)), (0, 50000), (67, 83), 10000, 2, 'GDP', 'Lifespan (years)', 70)
  + q('The scatterplot shows that there is a strong positive association between the lifespan and GDP.')
  + q('a. Apply a log transformation to the variable GDP, and determine the least squares regression line for the transformed data.')
  + q('<i>lifespan</i> = ' + a('54.3') + ' + ' + a('5.59') + ' × ' + a('log(<i>GDP</i>)'))
  + q('b. Use the least squares equation to predict the lifespan of a country with a GDP of $20 000 per person, giving your answer rounded to one decimal place.')
  + q('<i>lifespan</i> = ' + a('54.3 + 5.59 × log 20 000 = 78.3 years')),
  'You try 1', q('Akin is training for an Ironman Triathlon. Each Sunday, for ten weeks, he woke up early and ran ten kilometres.<br>He recorded the <i>distance</i>, in kilometres, he ran before his first break. The results are shown in the following table and scatterplot.')
  + T([['<b>week</b>'] + WEEK, ['<b>distance (km)</b>'] + DIST])
  + SP(list(zip(WEEK, DIST)), (0, 10), (0, 8), 1, 1, 'week', 'distance (km)', 62)
  + q('b. Apply a log transformation to the variable <i>week</i> and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.')
  + space(30, 'logweek = log(week); Linear Reg: XList logweek, YList dist<br>distance = 0.997 + 6.971 × log<sub>10</sub>(week)')))
P.append(exyt('Example 4 · Applying the log y transformation',
  q('The numbers of cases of a very infectious disease were recorded over a 12 day period. The association is not linear, as can be seen in the scatterplot below which plots cases against days.')
  + SP(list(zip(DAY, CASES)), (0, 12), (0, 7000), 2, 1000, 'day', 'cases', 66)
  + q('The scatterplot shows that there is a strong positive association between the number of case and day.')
  + q('a. Apply a log transformation to the variable cases, and determine the least squares regression line for the transformed data.')
  + q('log(<i>cases</i>) = ' + a('1.046') + ' + ' + a('0.227') + ' × <i>day</i>')
  + q('b. Use the least squares equation to predict the cases on day 13.')
  + q('log(<i>cases</i>) = ' + a('1.046 + 0.227 × 13 = 3.997'))
  + q('<i>cases</i> = 10<sup>' + a('3.997') + '</sup> = ' + a('9931 cases')),
  'You try 2', q('The number of followers of a new social media account was recorded over a 10 week period. The association is not linear.')
  + T([['<b>week</b>'] + FWEEK, ['<b>followers</b>'] + FOLL])
  + parts([('a', 'Apply a log transformation to the variable followers, and determine the least squares regression line for the transformed data.', 'log(followers) = 0.989 + 0.183 × week', 26),
           ('b', 'Use the least squares equation to predict the followers in week 11.', 'log(followers) = 0.989 + 0.183 × 11 = 3.002; 10<sup>3.002</sup> = 1005 followers', 26)])))
# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'VCAA'))
P.append(box('Exit task 1 · VCAA 2020 Exam 1 Q14', q('In a study, the association between the <i>number of tasks</i> completed on a test and the <i>time</i> allowed for the test, in hours, was found to be non-linear.<br>'
  'The data can be linearised using a log<sub>10</sub> transformation applied to the variable <i>number of tasks</i>.<br>The equation of the least squares line for the transformed data is')
  + q('<span style="display:block;text-align:center">log<sub>10</sub>(<i>number of tasks</i>) = 1.160 + 0.03617 × <i>time</i></span>')
  + q('This equation predicts that the <i>number of tasks</i> completed when the <i>time</i> allowed for the test is three hours is closest to')
  + mc(['13', '16', '19', '25', '26'], 'C', cols=5) + why('1.160 + 0.03617 × 3 = 1.2685; 10<sup>1.2685</sup> = 18.6 ≈ 19')))
P.append(box('Exit task 2 · VCAA 2017 Exam 2 Q4b, Q4ci', q('The following time series plot shows the total area, in hectares, of forest eaten by the caterpillars in a rural area during the period 1900 to 1980. The data used to generate this plot is also given.')
  + SP(list(zip(YEAR, AREA)), (1890, 1990), (0, 400), 20, 50, 'year', 'area (hectares)', 72)
  + T([['<b>year</b>'] + YEAR, ['<b>area (hectares)</b>'] + AREA])
  + q('The association between <i>area</i> of forest eaten by the caterpillars and <i>year</i> is non-linear.<br>A log<sub>10</sub> transformation can be applied to the variable <i>area</i> to linearise the data.')
  + parts([('a', 'Perform the log<sub>10</sub> transformation to the variable <i>area</i> and determine the equation of the least squares line that can be used to predict log<sub>10</sub>(<i>area</i>) from <i>year</i>. Round the values of the intercept and slope to three significant figures. (2 marks)', 'log<sub>10</sub>(area) = −14.4 + 0.00854 × year', 22),
           ('b', 'The least squares line predicts that the log<sub>10</sub>(<i>area</i>) of forest eaten by the caterpillars by the year 2020 will be approximately 2.85. Using this value of 2.85, calculate the expected area of forest that will be eaten by the caterpillars by the year 2020. Round your answer to the nearest hectare. (1 mark)', '10<sup>2.85</sup> = 707.9… ≈ 708 hectares', 16)])))
SC = ['I can apply the log x transformation.', 'I can apply the log y transformation.']
P.append(close(SC, [('4B', 'Q1–10')], ['4B']))
build('l13', '4B', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l13-worksheet', '4B worksheet'), ('l13-worksheet-solutions', '4B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
