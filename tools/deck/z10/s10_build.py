r"""12MAG S10 (2G The coefficient of determination, 2H Correlation and causality) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l07/build.py (planner card gm12-u3-l07; same items, same order). Data: tools/deck/l07/figs.py, l06/figs.py.
python3 tools/deck/z10/s10_build.py  ->  lessons/S10-slides.html
Sources (verbatim; read from the PDFs on G: 15 Nov 2026):
- APK: Cambridge U1&2 Ch 7 skills checklist 7C #6 (umbrellas; solution written for 12MAG) · VCAA 2019 Further Exam 2 Q4a (Edrolo U1&2 6A Q15; original wording; 84%).
- New learning: Cambridge U3&4 2G pp. 146-148, 2H pp. 151-154 (own words; diagrams redrawn).
- CAS: planner/cas-skills.json 'r-and-r2'; data Cambridge 2F CAS 2 (income / CO2): r = 0.818, r² = 0.669.
- Examples: Cambridge U3&4 Examples 17-21 (pp. 146-148; Example 21 scatterplot drawn for 12MAG with r = -0.7218).
- You trys: Edrolo U3&4 3C WE1a, 1b (p. 179) · YT-2G-19/20/21 (planner/written-youtrys.json, written for 12MAG) · 2H: Edrolo U3&4 2D WE2 (p. 148).
- Exits: Edrolo U3&4 2D Q13 = VCAA 2017 Further Exam 1 Q12 (D 81%; A 2, B 6, C 10, E 2) · 2D Q14 = VCAA 2019 Further Exam 2 Q4c (r = 0.871; 76%).
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'l06'))
from lib.deck import *
from lib.cat import *
from lib.assoc import *
from figs import INC, CO2, corr, rcloud
H9 = [100, 99, 95, 63, 81, 94, 96, 81, 73, 53, 57, 77, 51, 41]
H3 = [87, 75, 67, 57, 57, 74, 71, 62, 53, 54, 36, 39, 30, 32]
YTW = {y['id']: y for y in json.load(open(os.path.join(ROOT, 'planner', 'written-youtrys.json')))['items']}
lesson('2G Coefficient of determination · 2H Correlation and causality')

title_slide('The coefficient of determination · Correlation and causality',
            ['2G The coefficient of determination (pp. 146–150)', '2H Correlation and causality (pp. 151–155)'])
LI = ['To be able to calculate the value of the coefficient of determination.',
      'To be able to use the coefficient of determination to assess the strength of the association in terms of the explained variation.',
      'To be able to define and differentiate the concepts of association and causation.']
SC = ['I can calculate the value of the coefficient of determination.',
      'I can use the coefficient of determination to assess the strength of the association in terms of the explained variation.',
      'I understand that correlation does not imply causation.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'The coefficient of determination · Example 17', 'Interpreting r² · Examples 18–20', 'CAS: r and r²',
       'From r² back to r · Example 21', 'Correlation and causality', 'Exit tasks', 'Check-in and coursework']
overview('2G–2H', LI, SC, SEQ, CG + ', 2G and 2H Learning intentions; success criteria from the planner card', cols='1.15fr 1fr .85fr')

S.append(qslide('apk', '1 of 2', 'Correlation does not imply causation', 'Cambridge U1&amp;2 · 7C #6',
    'There is a strong positive correlation between sales of umbrellas and traffic accidents. Can we conclude that decreasing the sales of umbrellas will help decrease the number of traffic accidents?',
    'An association shows the variables move together<div class="kn">not that one causes the other</div>',
    ['A correlation shows the variables move together, not that one causes the other.', 'Third variable: rain. On rainy days more umbrellas are sold <b>and</b> roads are wet, so there are more accidents.'],
    'No. The association is most likely a common response to rain; it does not show that umbrella sales cause traffic accidents.',
    CG12 + ', Chapter 7 skills checklist 7C #6. Working by teacher.'))
HT = lambda id_: (f'<table class="ztab zsm2" id="{id_}"><tr><th rowspan="2">Relative humidity (%)</th><th>9 am</th>' + ''.join(f'<td>{v}</td>' for v in H9) + '</tr><tr><th>3 pm</th>' + ''.join(f'<td>{v}</td>' for v in H3) + '</tr></table>')
HQ = ('The relative humidity (%) at 9 am and 3 pm on 14 days in November 2017 is shown in Table 3 below.<br><b>Table 3</b>{T}<span class="zsmall">Data: Australian Government, Bureau of Meteorology, &lt;www.bom.gov.au/&gt;</span><br>'
      'A least squares line is to be fitted to the data with the aim of predicting the relative humidity at 3 pm (<i>humidity 3 pm</i>) from the relative humidity at 9 am (<i>humidity 9 am</i>).<br>')
S.append(qslide('apk', '2 of 2', 'Explanatory and response variables', 'VCAA 2019 Exam 2 Q4a',
    HQ.format(T=HT('a2t')) + 'Name the explanatory variable.', 'Predict <b>RV</b> from <b>EV</b>',
    ['We predict <i>humidity 3 pm</i> (RV) <b>from</b> <i>humidity 9 am</i> (EV).'], '<i>humidity 9 am</i>',
    ED12 + ', 6A Q15 (VCAA 2019 Further Mathematics Exam 2 Core Q4a; original wording); % from the examiner report.', marks=1, vcaa=84, figw='1fr',
    watch='‘predicting A from B’: B is the explanatory variable.'))

keyslide('2G–2H',
    [('Coefficient of determination', '<i>r</i>²: how well the EV predicts the RV, written as a percentage'),
     ('Interpretation', '<i>r</i>²% of the variation in the RV is explained by the variation in the EV'),
     ('Causation', 'only an experiment (EV changed on purpose, everything else constant) can show it'),
     ('Non-causal explanations', '<b>common response</b> (a third variable drives both) · <b>confounding</b> (another possible cause can’t be separated) · <b>coincidence</b>')],
    [('Coefficient of determination', r'$r^2 = (r)^2$, $0 \le r^2 \le 1$'), ('From r² back to r', r'$r = \pm\sqrt{r^2}$: the sign comes from the scatterplot'),
     ('Sentence', '__% of the variation in <i>RV</i> can be explained by the variation in <i>EV</i>')],
    CG + ', 2G pp. 146–148, 2H pp. 151–154')

def expl(id_, pct, rv='the RV', ev='the EV', ex=''):
    return (f'<div class="zexpl" id="{id_}"><div class="zebar"><div class="zein" style="width:{pct}%"><b>{pct}%</b> explained by the variation in {ev}</div><div class="zeout">{100-pct}% not explained {ex}</div></div></div>')
S.append(nl_slide('The coefficient of determination, r²',
    'Square <i>r</i>. The coefficient of determination tells us how well the EV <b>predicts</b> the RV: 0 ≤ <i>r</i>² ≤ 1, written as a percentage. <span class="hint">Click to reveal.</span>',
    '<div class="zlead2">Weight (RV) and height (EV): <i>r</i> = 0.8 → <i>r</i>² = 0.64 = 64%</div>' + expl('lb1', 64, ev='height', ex='(diet, lifestyle, build …)')
    + st('<i>r</i> = ±1: <i>r</i>² = 100%, an exact prediction · <i>r</i> ≈ 0: <i>r</i>² ≈ 0, no better than guessing.', cls='stp')
    + st('<i>r</i>² is always positive: it has no direction. Square <i>r</i>, don’t square the percentage.', cls='stp')
    + st('<b>Sentence</b>: <b>__ %</b> of the variation in <b>the RV</b> can be explained by the variation in <b>the EV</b>. Name the variables in context: never write ‘the RV’ or ‘x’ and ‘y’ in an answer.', cls='stp'),
    CG + ', 2G pp. 146–148 (bar drawn for 12MAG)'))
KI_R2 = r'$r^2 = (r)^2$, then × 100 for a %<div class="kn">__% of the variation in RV is explained by the variation in EV</div>'
S.append(qslide('ex', 17, 'Calculating the coefficient of determination', 'Cambridge · Example 17',
    'If the correlation between weight and height is <i>r</i> = 0.8, find the value of the coefficient of determination. Express your answer as a percentage.', KI_R2,
    [r'$r^2 = 0.8^2 = 0.64$', '0.64 × 100 = 64%'], 'The coefficient of determination = <i>r</i>² = 0.8² = 0.64 = <b>64%</b>', CG + ', 2G Example 17 (p. 146)'))
VG = 'A study was conducted to explore the effect of the time in minutes spent playing <i>video games</i> on time spent <i>studying</i> in minutes. It was determined that the correlation coefficient, <i>r</i>, for the data collected during the study is 0.6584.'
S.append(qslide('yt', 17, 'Calculating the coefficient of determination', 'Edrolo 3C WE1a',
    VG + '<br><b>a.</b> Determine the coefficient of determination, <i>r</i>², correct to four decimal places.', KI_R2, [r'$r^2 = 0.6584^2 = 0.43349\ldots$'], '<i>r</i>² = <b>0.4335</b>',
    ED + ', 3C Worked example 1a (p. 179). Working by teacher.'))
S.append(qslide('ex', 18, 'Interpreting the coefficient of determination', 'Cambridge · Example 18',
    'In the previous example we found the coefficient of determination between height and weight to be 0.64 (or 64%). Interpret this value in terms of the variables weight and height.', KI_R2,
    ['Weight depends on height: RV weight, EV height.', 'Fill the sentence: 64% · weight · height.'],
    'The coefficient of determination tells us that <b>64%</b> of the variation in people’s weight is explained by the variation in their height.', CG + ', 2G Example 18 (p. 147)'))
S.append(qslide('yt', 18, 'Interpreting the coefficient of determination', 'Edrolo 3C WE1b',
    VG + '<br><b>b.</b> Interpret the coefficient of determination in terms of time spent studying and time spent playing video games.', KI_R2,
    ['Studying is affected by video games: EV video games, RV studying.', '0.4335 × 100 = 43.35'],
    '43.35% of the variation in the time spent studying can be explained by the variation in the time spent playing video games.', ED + ', 3C Worked example 1b (p. 179). Working by teacher.'))

def we_interp(n, text, r_, rv, ev, pct, ans):
    S.append(qslide('ex', n, 'Calculating and interpreting the coefficient of determination', f'Cambridge · Example {n}', text, KI_R2,
        [f'$r^2 = ({r_})^2 = {float(r_)**2:.4f}$', f'{float(r_)**2:.4f} × 100 = {pct}% (1 d.p.)', f'RV {rv} · EV {ev}'], ans, CG + f', 2G Example {n} (pp. 147–148)'))
def yt_w(n, id_, r_, rv, ev):
    y = YTW[id_]; a = y['answer'].split('; ', 1)
    S.append(qslide('yt', n, 'Calculating and interpreting the coefficient of determination', 'Written for 12MAG',
        y['text'].replace('r = ', '<i>r</i> = '), KI_R2, [f'$r^2 = ({r_})^2 = {float(r_)**2:.4f}$', f'RV {rv} · EV {ev}'],
        a[0].replace('r² = ', '<i>r</i>² = ') + '<br>' + a[1][0].upper() + a[1][1:], f'{id_}: written for 12MAG, modelled on {CG} Example {n} (no Edrolo match; planner/written-youtrys.json).'))
we_interp(19, 'The level of carbon monoxide (CO) in the air measured at the roadside, and the traffic volume at the same location are linearly related, with <i>r</i> = +0.985. Determine the value of the coefficient of determination, write it in percentage terms and interpret. In this relationship, traffic volume is the explanatory variable.',
          '0.985', 'carbon monoxide level', 'traffic volume', '97.0', 'Therefore, <b>97.0%</b> of the variation in carbon monoxide levels in the air can be explained by the variation in traffic volume.')
yt_w(19, 'YT-2G-19', '0.912', 'bottles of sunscreen sold', 'daily maximum temperature')
we_interp(20, 'Scores on tests of verbal and mathematical ability are linearly related with correlation coefficient <i>r</i> = +0.275. Determine the value of the coefficient of determination, write it in percentage terms, and interpret. In this relationship, verbal ability is the explanatory variable.',
          '0.275', 'mathematical ability score', 'verbal ability score', '7.6', 'Therefore, only <b>7.6%</b> of the variation observed in scores on the mathematical ability test can be explained by the variation in scores obtained on the verbal ability test.')
yt_w(20, 'YT-2G-20', '0.342', 'spelling ability score', 'reading speed score')

# ---- CAS
r = corr(INC, CO2)
IT = ('<table class="ztab zsm2"><tr><th>Income ($’000)</th>' + ''.join(f'<td>{x}</td>' for x in INC) + '</tr><tr><th>CO<sub>2</sub> (tonnes)</th>' + ''.join(f'<td>{x}</td>' for x in CO2) + '</tr></table>')
S.append(qslide('cas', '', 'Finding r and r²', 'Data: Cambridge · 2F CAS 2',
    'The following data show the per capita income (in $’000) and the per capita carbon dioxide emissions (in tonnes) of 11 countries.' + IT
    + 'Find <i>r</i> and the coefficient of determination, <i>r</i>², with income as the EV.', 'Linear Regression gives <i>r</i> and <i>r</i>²',
    ['Enter <b>income</b> (x) and <b>co2</b> (y).', 'Linear Regression (a + bx) → read <i>r</i> and <i>r</i>².'],
    f'<i>r</i> = {r:.4f}… · <i>r</i>² = {r*r:.4f}… → <b>66.9%</b> of the variation in CO<sub>2</sub> emissions is explained by the variation in income.',
    CG + ', 2F CAS 2 data (pp. 142–143). CAS steps: planner CAS guide (r-and-r2).', fig=casbox('r-and-r2'), figw='1.2fr'))

# ---- Example 21 / You try 21
KI_BACK = r'$r = \pm\sqrt{r^2}$<div class="kn">the <b>sign</b> comes from the direction of the scatterplot</div>'
S.append(qslide('ex', 21, 'Calculating the correlation coefficient from the coefficient of determination', 'Cambridge · Example 21',
    'For the relationship described by this scatterplot, the coefficient of determination = 0.5210.<br>Determine the value of the correlation coefficient, <i>r</i>, rounded to four decimal places.',
    KI_BACK, [r'$r = \pm\sqrt{0.5210} = \pm 0.7218$', 'Direction: the points trend downwards: negative.'], '<i>r</i> = <b>−0.7218</b>', CG + ', 2G Example 21 (p. 148; scatterplot drawn for 12MAG)',
    fig=scat('s21', rcloud(-0.7218, 26, 21), (-2.6, 2.6, 9), (-2.6, 2.6, 9), '', '', w=440, h=320, r=4.5, grid=False, ticks=False), figw='.9fr'))
y21 = YTW['YT-2G-21']
S.append(qslide('yt', 21, 'Calculating the correlation coefficient from the coefficient of determination', 'Written for 12MAG',
    y21['text'].replace('r, ', '<i>r</i>, ').replace('r²', '<i>r</i>²'), KI_BACK, [r'$r = \pm\sqrt{0.6384} = \pm 0.7990$', 'Direction: the points trend upwards: positive.'],
    '<i>r</i> = <b>+0.7990</b>', f'YT-2G-21: written for 12MAG, modelled on {CG} Example 21 (no Edrolo match; planner/written-youtrys.json).',
    fig=scat('s24', rcloud(0.7990, 26, 24), (-2.6, 2.6, 9), (-2.6, 2.6, 9), '', '', w=440, h=320, r=4.5, grid=False, ticks=False), figw='.9fr'))

# ---- 2H
S.append(nl_slide('Correlation does not imply causality',
    'A correlation tells you the <b>strength</b> of an association, but nothing about its <b>cause</b>. Countries with more IKEA stores win more Nobel prizes (<i>r</i> = 0.82): building IKEAs won’t win prizes. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr">' + st('<b>Observation</b><br>record data as it happens<br>→ shows an <b>association</b> only', cls='stp zcard')
    + st('<b>Experiment</b><br>change the EV on purpose, keep every other variable the same (random groups, same conditions), then measure the RV<br>→ can show <b>causation</b>', cls='stp zcard') + '</div>'
    + st('However strong the association, observational data alone never proves cause.', cls='stp ztest'), CG + ', 2H pp. 151–152'))
TRI = lambda top, a, b, q='': (f'<div class="ztri"><div class="zt0">{top}</div><div class="zt1"><span>↙</span><span>↘</span></div><div class="zt2"><span>{a}</span><span class="zta">⟷{q}</span><span>{b}</span></div></div>')
S.append(nl_slide('Possible non-causal explanations',
    'In an answer: name the third variable and say how it affects <b>both</b> variables. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr 1fr">'
    + st('<b>Common response</b><br>both variables respond to a third variable' + TRI('Temperature', 'Sunscreen sales', 'Fainting'), cls='stp zcard')
    + st('<b>Confounding</b><br>another possible cause that can’t be separated from the EV' + TRI('Economy', 'Unemployment', 'Crime', ' ?'), cls='stp zcard')
    + st('<b>Coincidence</b><br>chance: margarine eaten and divorces in Maine, <i>r</i> = 0.99', cls='stp zcard') + '</div>',
    CG + ', 2H pp. 153–154 (diagrams redrawn)'))
S.append(qslide('yt', 22, 'Correlation and causation', 'Edrolo 2D WE2',
    'Gunther runs a cafe and collects data throughout the year on the daily number of <i>hot chocolates purchased</i>. He finds that there is a negative association between the daily number of <i>hot chocolates purchased</i> and the number of <i>daylight hours</i> on a particular day.',
    'Name the <b>third variable</b> and how it affects <b>both</b>', [], None, ED + ', 2D Worked example 2 (p. 148; no Cambridge Example for 2H). Working by teacher.',
    parts=[('a', 'Identify a potential third variable that could have caused this association.', ['Colder seasons: fewer daylight hours <b>and</b> more hot chocolates.'], 'A potential third variable is the <b>season</b>.'),
           ('b', 'Has Gunther conducted an appropriate experiment to determine causation? Why or why not?', ['All external variables must stay constant to determine causation.'],
            'No. The variable <b>season</b> does not remain constant across the experiment.')]))

# ---- exits
OPTDIST['1 of 2'] = [2, 6, 10, 81, 2]
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2017 Exam 1 Q12',
    'Data collected over a period of 10 years indicated a strong, positive association between the number of stray cats and the number of stray dogs reported each year (<i>r</i> = 0.87) in a large, regional city.<br>'
    'A positive association was also found between the population of the city and both the number of stray cats (<i>r</i> = 0.61) and the number of stray dogs (<i>r</i> = 0.72).<br>'
    'During the time that the data was collected, the population of the city grew from 34 564 to 51 055.<br>From this information, we can conclude that',
    'Look for a <b>third variable</b> linked to both', ['Population is associated with both cats and dogs.', 'Population growth → more stray cats and more stray dogs: a common response.'],
    'a common response to the growing population.', ED + ', 2D Q13 (VCAA 2017 Further Mathematics Exam 1 Q12; original wording); % from the examiner report.',
    figw='1.6fr', marks=1, vcaa=81, cls='x1s',
    opts=[('A', 'if cat owners paid more attention to keeping dogs off their property, the number of stray cats reported would decrease.'),
          ('B', 'the association between the number of stray cats and stray dogs reported cannot be causal because only a correlation of +1 or –1 shows causal relationships.'),
          ('C', 'there is no logical explanation for the association between the number of stray cats and stray dogs reported in the city so it must be a chance occurrence.'),
          ('D', 'because larger populations tend to have both a larger number of stray cats and stray dogs, the association between the number of stray cats and the number of stray dogs can be explained by a common response to a third variable, which is the increasing population size of the city.'),
          ('E', 'more stray cats were reported because people are no longer as careful about keeping their cats properly contained on their property as they were in the past.')], key='D'))
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2019 Exam 2 Q4c',
    HQ.format(T=HT('x2t')) + 'Determine the value of the correlation coefficient for this data set.<br>Round your answer to three decimal places.',
    'CAS: Linear Regression → <i>r</i>', ['X: humidity 9 am (EV), Y: humidity 3 pm (RV) → Linear Regression.', f'Read off: <i>r</i> = {corr(H9, H3):.4f}…'],
    '<i>r</i> = <b>0.871</b>', ED + ', 2D Q14 (VCAA 2019 Further Mathematics Exam 2 Core Q4c; original wording); % from the examiner report.', marks=1, vcaa=76, figw='1fr',
    watch='round to <b>three</b> decimal places, as asked.'))

checkin(SC)
coursework('2G–2H', 'Coursework · Exercises 2G and 2H', [('Cambridge Exercise 2G', 'Q1–8'), ('Cambridge Exercise 2H', 'Q1–8'), ('Practice booklet', '2G and 2H sections (Insight)')],
           'Exercise 2G: The coefficient of determination', CG + ', Exercises 2G and 2H; Chapter 2 workbook practice questions', fit=False)

LESSON_CSS = r'''
.slide.z .st.zcard{align-self:start}
.ztab.zsm2{font-size:14px}.ztab.zsm2 td,.ztab.zsm2 th{padding:1px 5px}
.zsmall{font-size:13px;color:#555}
.slide.z .st.zcard{border:2.5px solid #000;padding:10px 12px;box-shadow:4px 4px 0 #bbb;font-size:20px;color:#000;margin:0!important}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:14px!important}
.zlead2{font-size:22px;text-align:center;margin:8px 0}
.zexpl{margin:10px 0 14px}.zebar{display:flex;border:2.5px solid #000;height:64px;font-size:18px}
.zein{background:#a8dca8;display:flex;align-items:center;justify-content:center;border-right:2.5px solid #000;text-align:center;padding:0 6px}
.zeout{flex:1;background:#eee;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 6px}
.ztri{margin-top:10px;text-align:center;font-size:17px}.ztri .zt0{border:2px solid #000;display:inline-block;padding:4px 10px;font-weight:bold}
.ztri .zt1{display:flex;justify-content:space-around;font-size:28px}.ztri .zt2{display:flex;justify-content:space-between;align-items:center;gap:4px}
.ztri .zt2>span:not(.zta){border:2px solid #000;padding:4px 8px}.ztri .zta{color:#d00000;font-weight:bold}
.slide.x1s .zmc>div{font-size:15px}
'''
build('S10-slides.html', '12MAG S10 · The coefficient of determination · Correlation and causality · Slides', css=LESSON_CSS)
