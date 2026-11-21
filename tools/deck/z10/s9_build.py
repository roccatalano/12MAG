r"""12MAG S9 (2F The correlation coefficient r) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l06/build.py (planner card gm12-u3-l06; same items, same order). Figure values: tools/deck/l06/figs.py, l05/figs.py (FOOT).
python3 tools/deck/z10/s9_build.py  ->  lessons/S9-slides.html
Sources (verbatim; read from the PDFs on G: 15 Nov 2026):
- CFAT 1.2.2 (2C-2D) at the start (planner card).
- APK: Cambridge U1&2 Ch 7 skills checklist 7C #4 and #5 (data of 7B #2, p. 457; no printed answers: solutions written for 12MAG, r = 0.657 -> moderate)
       VCAA 2016 Further Exam 1 Q12 (Edrolo U1&2 6B Q15; original wording; report D 67%, A 11, B 8, C 3, E 11).
- New learning: Cambridge U3&4 2F pp. 140-144 (properties of r, strength table, warning). Example 16 (p. 144).
- CAS: planner/cas-skills.json 'correlation-r'; Cambridge 2F CAS 2 (income / CO2; r = 0.818: the TI page's 0.8342 is a misprint, checked on the data).
- You try: Edrolo U3&4 2D Worked example 1 (pp. 146-148). Exit: Edrolo U3&4 2C Q17 = VCAA 2020 Further Exam 2 Core Q6b (average 0.5/1 = 50%).
"""
import os, sys, math, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'l06'))
from lib.deck import *
from lib.cat import *
from lib.assoc import *
from figs import INC, CO2, GRADE, LECT, AGEGRP, AGE, HT, corr, rcloud
FOOT = [(172, 24), (172, 22), (177, 28), (165, 20), (176, 28), (155, 25), (166, 22), (166, 30), (182, 32), (160, 26), (153, 22), (177, 28), (172, 26), (173, 25), (185, 40), (159, 24)]
lesson('2F The correlation coefficient r')


def cfat(code, topic, covers, marks):
    S.append(f'<section class="slide z cfat">{bar(code, topic)}'
             '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
             f'<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · {marks} marks</li>'
             f'<li>Covers {covers}</li><li>Pens down when the timer ends</li></ul></div>'
             '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
             '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
             f'{foot(code + " (" + covers + "): student copy and solutions on the planner")}</section>')


STR = [('0.75 ≤ <i>r</i> ≤ 1', 'strong positive'), ('0.5 ≤ <i>r</i> &lt; 0.75', 'moderate positive'), ('0.25 ≤ <i>r</i> &lt; 0.5', 'weak positive'), ('−0.25 &lt; <i>r</i> &lt; 0.25', 'no association'),
       ('−0.5 &lt; <i>r</i> ≤ −0.25', 'weak negative'), ('−0.75 &lt; <i>r</i> ≤ −0.5', 'moderate negative'), ('−1 ≤ <i>r</i> ≤ −0.75', 'strong negative')]
strt = lambda id_: f'<table class="ztab zstr" id="{id_}"><tr><th><i>r</i></th><th>linear association</th></tr>' + ''.join(f'<tr data-r="{k}"><td>{a}</td><td>{b}</td></tr>' for k, (a, b) in enumerate(STR)) + '</table>'
mini = lambda r, s, w=200, h=160: scat(f'm{abs(int(r*100))}{s}', rcloud(r, 30, s), (-2.6, 2.6, 9), (-2.6, 2.6, 9), '', '', w=w, h=h, r=3.5, grid=False, ticks=False)
r_foot = corr(*zip(*FOOT))

title_slide('Strength of a linear relationship: the correlation coefficient', ['2F Strength of a linear relationship: the correlation coefficient (pp. 140–146)'])
LI = ['To introduce Pearson’s correlation coefficient r as a measure of the strength of a linear association between two variables.',
      'To be able to use technology to determine the value of Pearson’s correlation coefficient r.',
      'To be able to classify the strength of a linear association as weak, moderate or strong based on the value of Pearson’s correlation coefficient r.']
SC = ['I can use technology to determine the value of the correlation coefficient r.',
      'I can classify the strength of a linear association as weak, moderate or strong based on the value of the correlation coefficient r.']
SEQ = ['CFAT 1.2.2 (20 minutes, 2C–2D)', 'Activating prior knowledge', 'Key ideas and formulas', 'What r measures', 'Classifying r · Example 16', 'CAS: finding r', 'Exit task', 'Check-in and coursework']
overview('2F', LI, SC, SEQ, CG + ', 2F Learning intentions; success criteria from the planner card', cols='1.15fr 1fr .85fr')
cfat('CFAT 1.2.2', 'Numerical vs categorical variables, scatterplots', '2C–2D', 16)

# ---- APK
FS = scat('a1s', FOOT, (150, 190, 10), (15, 45, 5), 'height (cm)', 'foot length (cm)', w=440, h=300, r=5)
GAL = '<div class="zgal4">' + ''.join(f'<div>{mini(r, 7 + k)}<i>r</i> = {r}</div>' for k, r in enumerate([0.3, 0.5, 0.7, 0.9])) + '</div>'
S.append(qslide('apk', '1 of 3', 'Estimating and calculating r', 'Cambridge U1&amp;2 · 7C #4',
    'Height (<i>height</i>) and foot length (<i>foot length</i>) of 16 students, in centimetres (data from 7B #2).<br>'
    'Estimate the value of the correlation coefficient, <i>r</i>, between height and foot length by comparing the scatterplot to those on page 420, and then use your calculator to find its exact value. Give your answer rounded to three decimal places.',
    '<i>r</i> close to ±1: points close to a line<div class="kn">sign = direction</div>',
    ['Estimate: positive, more scattered than <i>r</i> = 0.9, about like <i>r</i> = 0.7: <i>r</i> ≈ 0.6 to 0.7.', 'CAS: lists height (EV) and foot (RV) → Linear Regression → <i>r</i> = 0.6567…'],
    f'<i>r</i> ≈ 0.7 (estimate); <i>r</i> = <b>{r_foot:.3f}</b>', CG12 + ', Chapter 7 skills checklist 7C #4 (data from 7B #2, p. 457; plots drawn for 12MAG; ‘page 420’ = the <i>r</i> gallery in Cambridge U1&amp;2). Working by teacher.',
    fig='<div class="zrowc" style="align-items:center">' + FS + GAL + '</div>', figw='1.5fr', cls='tight'))
S.append(qslide('apk', '2 of 3', 'Classifying the strength of r', 'Cambridge U1&amp;2 · 7C #5',
    'Use the table on page 428 to classify the value of the correlation coefficient, <i>r</i>, between height and foot length as weak, moderate or strong.',
    'Find where <i>r</i> sits in the table', [(f'<i>r</i> = {r_foot:.3f}: 0.5 ≤ {r_foot:.3f} &lt; 0.75', 'hr:a2t:1')],
    f'<i>r</i> = {r_foot:.3f}: a <b>moderate</b> positive linear association.', CG12 + ', Chapter 7 skills checklist 7C #5 (‘page 428’ = the strength table, as Cambridge U3&amp;4 p. 143). Working by teacher.',
    fig=strt('a2t'), figw='.8fr'))
OPTDIST['3 of 3'] = [11, 8, 3, 67, 11]
S.append(qslide('apk', '3 of 3', 'Interpreting an association', 'VCAA 2016 Exam 1 Q12',
    'There is a strong positive association between a country’s Human Development Index and its carbon dioxide emissions.<br>From this information, it can be concluded that',
    'Positive: higher values go with higher values<div class="kn">association is not cause</div>',
    ['Positive: higher values of one variable go with higher values of the other.', 'An association does not tell us that changing one variable changes the other: A and B ✗'],
    'countries with higher HDI tend to have higher CO₂ emissions.', ED12 + ', 6B Q15 (VCAA 2016 Further Mathematics Exam 1 Q12; original wording); % from the examiner report.',
    figw='1fr', marks=1, vcaa=67,
    opts=[('A', 'increasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.'), ('B', 'decreasing a country’s carbon dioxide emissions will increase the Human Development Index of the country.'),
          ('C', 'this association must be a chance occurrence and can be safely ignored.'), ('D', 'countries that have higher human development indices tend to have higher levels of carbon dioxide emissions.'),
          ('E', 'countries that have higher human development indices tend to have lower levels of carbon dioxide emissions.')], key='D'))

keyslide('2F',
    [('Pearson’s correlation coefficient <i>r</i>', 'one number for the strength and direction of a <b>linear</b> association'),
     ('Sign of <i>r</i>', 'the direction: positive or negative'),
     ('Size of <i>r</i>', 'the strength: closer to ±1 → points closer to a straight line'),
     ('Use <i>r</i> only when', 'both variables are numerical, the association is linear and there are no outliers')],
    [('Range', r'$-1 \le r \le +1$'), ('Perfect / none', r'$r = \pm 1$ perfect · $r \approx 0$ no linear association'),
     ('Strength guide', r'$|r| \ge 0.75$ strong · $0.5$ to $0.75$ moderate · $0.25$ to $0.5$ weak · below $0.25$ none')],
    CG + ', 2F pp. 140–144')

ROW = '<div class="zgal7">' + ''.join(st(f'{mini(r, 11 + k, 170, 140)}<i>r</i> = {r:+g}'.replace('= +0<', '= 0<'), cls='stp zgi') for k, r in enumerate([-1, -0.7, -0.3, 0, 0.5, 0.9, 1])) + '</div>'
S.append(nl_slide('Pearson’s correlation coefficient, r',
    'One number for a linear association: −1 ≤ <i>r</i> ≤ +1. The <b>sign</b> gives the direction; the <b>size</b> gives the strength. <span class="hint">Click to reveal.</span>',
    ROW + st('<i>r</i> = ±1: a perfect linear association · <i>r</i> ≈ 0: no linear association. Read the sign for direction, then the size for strength.', cls='stp ztest'),
    CG + ', 2F pp. 140–141 (plots drawn for 12MAG)'))
S.append(nl_slide('Classifying the strength of a linear association',
    'Find where <i>r</i> sits in the table. Watch the ends: 0.75 is <b>strong</b>, 0.5 is <b>moderate</b>, 0.25 is <b>weak</b>. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col zc">' + strt('lst') + '</div><div class="col">'
    + st('<b>1</b> Positive: strong, moderate, weak', do='hr:lst:0,1,2', cls='stp') + st('<b>2</b> Close to 0: no association', do='hr:lst:3', cls='stp')
    + st('<b>3</b> Negative: weak, moderate, strong', do='hr:lst:4,5,6', cls='stp')
    + st('<b>Warning</b>: only use <i>r</i> when 1 · the variables are numerical, 2 · the association is linear, 3 · there are no outliers. Look at the scatterplot first.', cls='stp') + '</div></div>',
    CG + ', 2F pp. 143–144'))
S.append(qslide('ex', 16, 'Classifying the strength of a linear association', 'Cambridge · Example 16',
    'Classify the strength of each of the following linear associations using the previous table:', 'Find where <i>r</i> sits in the table', [], None, CG + ', 2F Example 16 (p. 144)',
    parts=[('a', '<i>r</i> = 0.35', ['The value 0.35 is more than 0.25 and less than 0.5. That is, 0.25 ≤ <i>r</i> &lt; 0.5'], 'weak, positive', 'hr:w16:2'),
           ('b', '<i>r</i> = −0.507', ['The value −0.507 is more than −0.75 and less than −0.5. That is, −0.75 &lt; <i>r</i> ≤ −0.5'], 'moderate, negative', 'hr:w16:5'),
           ('c', '<i>r</i> = 0.992', ['The value 0.992 is more than 0.75 and less than 1. That is, 0.75 ≤ <i>r</i> ≤ 1'], 'strong, positive', 'hr:w16:0'),
           ('d', '<i>r</i> = −0.159', ['The value −0.159 is more than −0.25 and less than 0.25. That is, −0.25 &lt; <i>r</i> &lt; 0.25'], 'no association', 'hr:w16:3')],
    fig=strt('w16'), figw='.75fr', cls='tight zs16'))
YT = ('<table class="ztab zsm2"><tr><th><i>grade</i> (%)</th>' + ''.join(f'<td>{g}</td>' for g in GRADE) + '</tr><tr><th><i>lectures attended</i></th>' + ''.join(f'<td>{l}</td>' for l in LECT) + '</tr></table>')
S.append(qslide('yt', 16, 'Calculating and interpreting r', 'Edrolo 2D WE1',
    'A survey followed the study habits of a group of first-year uni students with the aim of predicting their <i>grade</i>, as a percentage, from the number of <i>lectures attended</i>. The results are shown in the following table.' + YT,
    'Check: numerical, linear, no outliers → then use <i>r</i>', [], None, ED + ', 2D Worked example 1 (pp. 146–148). Working by teacher.',
    parts=[('a', 'Is the Pearson correlation coefficient, <i>r</i>, an appropriate statistic for this data set?', ['RV <i>grade</i>, EV <i>lectures attended</i>; the scatterplot shows no curve: linear and numerical.'],
            'Yes, the Pearson correlation coefficient is an appropriate statistic for this data set.'),
           ('b', 'Determine the value of the correlation coefficient. Give the value correct to two decimal places.', [f'CAS (X: lectures, Y: grade): <i>r</i> = {corr(LECT, GRADE):.4f}…'], '<i>r</i> = 0.85'),
           ('c', 'If possible, describe the association between the variables in terms of strength, direction, and form.', [], 'Strong, positive, linear association (0.75 ≤ 0.85 ≤ 1; 0.85 is positive)')],
    fig=scat('y16s', list(zip(LECT, GRADE)), (0, 12, 2), (40, 100, 10), 'lectures attended', 'grade (%)', w=440, h=300, r=5), figw='.85fr', cls='tight zs16'))

# ---- CAS
IT = ('<table class="ztab zsm2"><tr><th>Income ($’000)</th>' + ''.join(f'<td>{x}</td>' for x in INC) + '</tr><tr><th>CO<sub>2</sub> (tonnes)</th>' + ''.join(f'<td>{x}</td>' for x in CO2) + '</tr></table>')
S.append(qslide('cas', '', 'Finding the correlation coefficient r', 'Cambridge · 2F CAS 2',
    'The following data show the per capita income (in $’000) and the per capita carbon dioxide emissions (in tonnes) of 11 countries.' + IT
    + 'Determine the value of Pearson’s correlation coefficient rounded to two decimal places.',
    'Linear Regression gives <i>r</i> (and <i>r</i>²)', ['Enter <b>income</b> (x) and <b>co2</b> (y).', 'Linear Regression (a + bx) → read <i>r</i>.'],
    f'<i>r</i> = {corr(INC, CO2):.4f}… = <b>0.82</b> (2 d.p.): a strong positive linear association.', CG + ', 2F CAS 2 (pp. 142–143). CAS steps: planner CAS guide (correlation-r).',
    fig=casbox('correlation-r'), figw='1.2fr'))

# ---- exit
EX = ('<table class="ztab zsm2"><tr><th></th>' + ''.join(f'<th>{g}</th>' for g in AGEGRP) + '</tr><tr><th><i>Mean age</i> (years)</th>' + ''.join(f'<td>{a}</td>' for a in AGE)
      + '</tr><tr><th><i>Mean height</i> (cm)</th>' + ''.join(f'<td>{h}</td>' for h in HT) + '</tr></table>')
S.append(qslide('exit', '1 of 1', 'Show what you know', 'VCAA 2020 Exam 2 Q6b',
    'The table below shows the <i>mean age</i>, in years, and the <i>mean height</i>, in centimetres, of 648 women from seven different age groups.' + EX
    + 'A scatterplot displaying this data shows an association between the <i>mean height</i> and the <i>mean age</i> of these women. In an initial analysis of the data, a line is fitted to the data by eye, as shown.<br>'
    'Describe this association in terms of strength and direction.',
    'Strength and direction <b>only</b>', ['Strength: the points lie very close to the line: strong.', 'Direction: mean height decreases as mean age increases: negative.'],
    'The association is <b>strong</b> and <b>negative</b>.', ED + ', 2C Q17 (VCAA 2020 Further Mathematics Exam 2 Core Q6b; original wording; scatterplot redrawn); % = average mark, from the examiner report.',
    fig=scat('x1s', list(zip(AGE, HT)), (20, 90, 10), (155, 170, 5), 'mean age (years)', 'mean height (cm)', seg=((20, 168.0), (90, 156.0)), shown=True, w=460, h=300, r=4.5),
    figw='.9fr', marks=1, vcaa=50, cls='tight', watch='answer only what is asked: extra information that is wrong (e.g. ‘non-linear’) loses the mark.'))

checkin(SC)
coursework('2F', 'Coursework · Exercise 2F', [('Cambridge Exercise 2F', 'Q1–4'), ('Practice booklet', '2F section (Insight + skill sheet)')],
           'Exercise 2F: The correlation coefficient', CG + ', Exercise 2F; Chapter 2 workbook practice questions')

LESSON_CSS = r'''
.slide.zs16 .zw .st.zs,.slide.zs16 .zw .zpq{font-size:15.5px!important;line-height:1.3!important;margin:2px 0!important}

.ztab.zsm2{font-size:14px}.ztab.zsm2 td,.ztab.zsm2 th{padding:1px 5px}
.ztab.zstr{font-size:18px}.ztab.zstr tr.hl td{background:#fff2a8;font-weight:bold}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:12px!important}
.zgal4{display:grid;grid-template-columns:1fr 1fr;gap:4px 10px;text-align:center;font-size:15px;width:330px}
.zgal7{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin:14px 0}
.slide.z .st.zgi{text-align:center;font-size:17px;margin:0!important}
'''
build('S9-slides.html', '12MAG S9 · Strength of a linear relationship: the correlation coefficient · Slides', css=LESSON_CSS)
