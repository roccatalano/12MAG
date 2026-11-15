# Chapter 4 revision booklet: Insight GM1 (MC) + GM2 (SA), "Investigating associations between two variables and
# modelling linear associations": the data-transformation questions the Ch 2 and Ch 3 booklets left out
# (GM1 Q5, 15, 16, 21, 22, 26, 27, 31, 32; GM2 Q12, Q15). Text verbatim from Insight (scanned books; read off the page
# images, GM1 pp.14, 17-21; GM2 pp.27, 31); answers and explanations from Insight's worked solutions (GM1 pp.36-42,
# GM2 pp.54-56), checked on the data with numpy. Figures are crops of the Insight pages (crop.py).
# Shared stems are repeated inside each box. Insight is never burnt.
G1 = 'Insight GM1 U3 Data Analysis'
G2 = 'Insight GM2 U3 Data Analysis'

def tbl(head, rows, cls='t'):
    h = '<tr>' + ''.join(f'<th>{c}</th>' for c in head) + '</tr>'
    return f'<table class="{cls}">' + h + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'

def across(labels, cols, cls='t sm'):
    return f'<table class="{cls}">' + ''.join('<tr><th>' + l + '</th>' + ''.join(f'<td>{c[i]}</td>' for c in cols) + '</tr>' for i, l in enumerate(labels)) + '</table>'

_H = [4, 5, 6, 1, 2, 2, 2.5, 3.6, 4, 7, 8, 9.8, 3.4, 5.6, 7.8, 6.2, 3.1, 1.5, 6.3, 7.2, 3.5, 6.7, 8.4, 6.7, 8.4, 6.7, 5.5]
_E = [18, 30, 38, 25, 22, 24, 28, 22, 20, 52, 65, 98, 23, 32, 67, 42, 22, 28, 42, 51, 23, 52, 67, 52, 67, 51, 34]
STUDY = ('<p class="q">The table below gives the exam results and number of hours spent studying for a different group of students.</p>'
         '<p class="q">A non-linear scatterplot for this data is also shown.</p>'
         + ''.join(across(['No. of hours studied', 'Exam result'], list(zip(_H[k:k + 9], _E[k:k + 9]))) for k in (0, 9, 18))  # same data, three rows of 9 to fit the box
         + '[[g1q5]]')
JAXON = ('<p class="q">Jaxon uses the following data to generate the scatterplot below.</p>'
         + across(['<i>x</i>', '<i>y</i>'], list(zip(range(1, 11), [250, 241, 232, 212, 189, 148, 101, 49, 22, 14])))
         + '[[g1q15]]<p class="q">The scatterplot shows that the data is non-linear.</p>')
SEED = ('<p class="q">The heights of seedlings are measured weekly to track their progress. The data is shown below.</p>'
        + across(['<i>Age</i> (weeks)', '<i>Average height</i> (cm)'], list(zip(range(9), [6.1, 6.4, 7.5, 9.6, '12.0', 18.2, 29.4, 46.1, 61.2]))))
FREEZE = ('<p class="q">Data on the cooling of an object in a laboratory freezer was recorded.</p><p class="q">These times are shown in the table below.</p>'
          + across(['<i>Time</i> (min)', '<i>Temperature</i> (°C)'], list(zip(range(1, 11), [210, 114, 61, 45, 32, 12, 8, 5, 1.3, 0.2]))))
POOL = ('<p class="q">The data below shows the <i>temperature</i> and the <i>number of visitors</i> to a local pool each day over a 10-day period.</p>'
        + ''.join(across(['Temperature (°C)', 'Number of visitors'], list(zip([17, 23, 27, 31, 33, 32, 38, 24, 18, 17], [63, 211, 294, 312, 233, 260, 251, 205, 77, 53]))[k:k + 5]) for k in (0, 5)) + '[[g1q30]]'  # same data, two rows of 5
        + '<p class="q">A reciprocal transformation is applied to the <i>temperature</i> in order to attempt to linearise the data.</p>'
        '<p class="q">The equation of the least squares line for the transformed data is</p>'
        '<p class="q" style="text-align:center"><i>number of visitors</i> = 494.7 − 7191 × <span class="fr"><i>1</i><i>temperature</i></span></p>')
FR = lambda n, d: f'<span class="fr"><i>{n}</i><i>{d}</i></span>'

def MC(n, sub, page, stem_, opts, a, why, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)

Q = [
 # ---- 4A: squared transformation
 MC(5, '4A', 14, STUDY + '<p class="q">A <b>squared transformation</b> will be applied to the variable <i>No. of hours studied</i> and can be used to linearise the scatterplot.</p>'
    '<p class="q">The equation of the least squares regression line for this squared transformation is closest to</p>',
    ['(<i>exam result</i>)<sup>2</sup> = 15.4 + 0.76 × <i>no. hours studied</i>', '<i>exam result</i> = 0.76 + 15.4 × (<i>no. of hours studied</i>)<sup>2</sup>',
     '<i>exam result</i> = 15.4 + 0.76 × <i>no. of hours studied</i>', '(<i>No. of hours studied</i>)<sup>2</sup> = 15.4 + 0.76 × <i>exam result</i>',
     '<i>exam result</i> = 15.4 + 0.76 × (<i>no. hours studied</i>)<sup>2</sup>'],
    'E', 'CAS with x = (hours studied)², y = exam result: a = 15.4, b = 0.76. Only the explanatory variable is squared.'),
 MC(16, '4A', 17, JAXON + '<p class="q">Jaxon performs the squared transformation to the variable <i>y</i>.</p><p class="q">He then fits a least squares line to the transformed data, with <i>x</i> as the explanatory variable.</p>'
    '<p class="q">Using this line, the predicted value for <i>y</i> when <i>x</i> is equal to 5 is closest to</p>',
    ['16&#8239;852', '361', '230', '182', '118'], 'D', 'y² = 73&#8239;661.5 − 8115.6x; y² = 73&#8239;661.5 − 8115.6 × 5, so y = √33&#8239;083.5 = 181.89 ≈ 182', shared='Q15–16'),
 MC(22, '4A', 18, SEED + '<p class="q">A squared transformation of <i>age</i> is performed. The equation of the least squares regression line for the transformed data is</p>'
    '<p class="q" style="text-align:center"><i>Average height</i> = 2.43 + 0.856 × (<i>age</i>)<sup>2</sup></p>'
    '<p class="q">At approximately what <i>age</i> were the plants when the <i>average height</i> was 20 cm?</p>',
    ['4.4 weeks', '4.5 weeks', '19.6 weeks', '20.5 weeks', '345 weeks'], 'B', '20 = 2.43 + 0.856 × age² → age² = 20.53 → age = 4.5 weeks', shared='Q21–22'),
 # ---- 4B: log transformation
 MC(27, '4B', 20, FREEZE + '<p class="q">A logarithmic transformation of the explanatory variable is performed.</p><p class="q">The equation of the least squares line for the transformed data is</p>',
    ['<i>temperature</i> = 182.26 − 203.38 × <i>time</i>', 'log(<i>time</i>) = 182.26 + 203.38 × <i>temperature</i>', '<i>temperature</i> = 182.26 + 203.38 × log(<i>time</i>)',
     'log(<i>temperature</i>) = 182.26 − 203.38 × log(<i>time</i>)', '<i>temperature</i> = 182.26 − 203.38 × log(<i>time</i>)'],
    'E', 'CAS with x = log(time), y = temperature: a = 182.26, b = −203.38 (negative: temperature falls).', shared='Q26–27'),
 # ---- 4C: reciprocal transformation
 MC(21, '4C', 18, SEED + '<p class="q">A reciprocal transformation of <i>average height</i> is performed.</p><p class="q">The equation of the least squares regression line for the transformed data is</p>',
    [f'{FR(1, "Age")} = 0.168 − 0.021 × <i>average height</i>', f'{FR(1, "Age")} = −4.293 + 6.532 × <i>average height</i>', f'{FR(1, "Average height")} = −4.293 + 6.532 × <i>age</i>',
     f'{FR(1, "Average height")} = 47.098 − 296.072 × <i>age</i>', f'{FR(1, "Average height")} = 0.168 − 0.021 × <i>age</i>'],
    'E', 'CAS with x = age, y = 1/average height: a = 0.168, b = −0.021.', shared='Q21–22'),
 MC(31, '4C', 21, POOL + '<p class="q">Which one of the following changes has occurred after the transformation?</p>',
    ['The correlation coefficient has become weaker from 0.830 to −0.917', 'The correlation coefficient has become stronger from 0.830 to −0.917',
     'The coefficient of determination has increased from 0.670 to 0.955', 'The coefficient of determination has decreased from 0.841 to 0.690',
     'The coefficient of determination has decreased from 0.841 to 0.670'],
    'B', 'Before: r = 0.830; after (x = 1/temperature): r = −0.917. |r| is larger, so the association is stronger (r² rises from 0.690 to 0.841).', shared='Q30–32'),
 MC(32, '4C', 21, POOL + '<p class="q">The equation of the least squares line for the transformed data is used to predict the <i>number of visitors</i>.</p>'
    '<p class="q">The <i>number of visitors</i> predicted when the <i>temperature</i> is 30 °C is closest to</p>',
    ['15', '182', '255', '402', '759'], 'C', '494.7 − 7191 × 1/30 = 494.7 − 239.7 = 255', shared='Q30–32'),
 # ---- 4D: choosing a transformation
 MC(15, '4D', 17, JAXON + '<p class="q">To linearise the data, Jaxon could apply which of the following sets of transformations?</p>',
    [f'<i>x</i><sup>2</sup> or {FR(1, "y")}', '<i>x</i><sup>2</sup> or <i>y</i><sup>2</sup>', '<i>x</i><sup>2</sup> or log <i>y</i>', '<i>y</i><sup>2</sup> or log <i>x</i>', f'<i>y</i><sup>2</sup> or {FR(1, "x")}'],
    'B', 'Decreasing and curving down (concave down): the circle of transformations gives x² or y². These are the only ones that could linearise the data.', shared='Q15–16'),
 MC(26, '4D', 19, FREEZE + '<p class="q">Which one of the following transformations would be appropriate in order to linearise this data?</p>',
    [f'{FR(1, "time")}, {FR(1, "temp")}, log(<i>time</i>), log(<i>temp</i>)', f'{FR(1, "temp")}, log(<i>temp</i>), <i>time</i><sup>2</sup>', 'log(<i>time</i>), <i>time</i><sup>2</sup>, <i>temp</i><sup>2</sup>',
     f'{FR(1, "time")}, log(<i>time</i>), <i>temp</i><sup>2</sup>', f'{FR(1, "time")}, {FR(1, "temp")}, log(<i>temp</i>), <i>time</i><sup>2</sup>'],
    'A', 'Decreasing and curving up (concave up): the circle of transformations gives log x, 1/x, log y or 1/y.', shared='Q26–27'),
]

def SA(n, sub, page, stem_, parts, why=None, note=None, long=False):
    return dict(long=long, kind='sa', n=n, sub=sub, marks=sum(p[4] for p in parts), stem=stem_, parts=parts, why=why, note=note, src=f'{G2} p.{page} Q{n}')

STAFF = ('<p class="q">The number of staff rostered on for restocking at the supermarket is measured against the number of items restocked. The data is shown below.</p>'
         + ''.join(across(['Number of staff', 'Units restocked'], list(zip([4, 5, 12, 5, 4, 6, 9, 15, 8, 8], [220, 960, 1920, 520, 190, 1470, 1790, 1990, 1840, 1760]))[k:k + 5]) for k in (0, 5)))  # two rows of 5

Q += [
 # ---- 4B
 SA(15, '4B', 31, STAFF + '<p class="q">In order to linearise the data, a log<sub>10</sub> transformation is applied and a least squares line is fitted to the transformed equation.</p>',
    [('a', 'Complete an appropriate log<sub>10</sub> transformation and write down the equation of the least squares line.<br>Round the values to four significant figures.',
      'A log transformation of the explanatory variable (<i>number of staff</i>):<br><i>units restocked</i> = −1551 + 3355 × log<sub>10</sub>(<i>number of staff</i>)', 14, 2)],
    note='Part a. Part b is in the 4C section.'),
 # ---- 4C
 SA(12, '4C', 27, '<p class="q">A reciprocal transformation of the response variable of a data set was performed, and the results are shown below.</p>'
    + ''.join(across(['<i>x</i>', '<i>y</i>', FR(1, 'y')], list(zip(range(8), [1, 4, 25, 80, 200, 1000, 4000, '25&#8239;000'],
             [1, 0.25, '<u>0.04</u>', 0.0125, '<u>0.005</u>', 0.001, 0.00025, '0.00004']))[k:k + 4], 't sm') for k in (0, 4))  # two rows of 4
    + '<p class="q">The equation of the least squares line for the transformed data is</p><p class="q" style="text-align:center">' + FR(1, 'y') + ' = 0.512 − 0.10<i>x</i></p>',
    [('a', 'In the table above, complete the missing values for the transformed values of <i>y</i>.', '1/25 = 0.04, 1/200 = 0.005', 3, 1),
     ('b', 'The equation is used to predict that, for a particular value of <i>x</i>, <i>y</i> = 1.587.<br>Is the prediction considered reliable? Use calculations to justify your response.',
      '1/1.587 = 0.512 − 0.1<i>x</i> → <i>x</i> = −1.2<br>This is extrapolation (−1.2 is outside the range of the data, 0 to 7), so the prediction is unreliable.', 14, 2)]),
 SA(15, '4C', 31, STAFF + f'<p class="q">A reciprocal transformation is also applied to the data.</p><p class="q">The equation of the least squares line fitted to this transformed data is</p>'
    f'<p class="q" style="text-align:center"><i>units restocked</i> = 2942 − 10&#8239;623 × {FR(1, "number of staff")}</p>',
    [('b i', 'What is the predicted number of units restocked when 16 staff are rostered on? Round your answer to the nearest whole number.', '2942 − 10&#8239;623 × 1/16 = 2278', 10, 1),
     ('b ii', 'Explain why this prediction may have limited reliability.', 'The value of 16 is outside the range of data provided (4 to 15); therefore it is extrapolation, which may be less reliable.', 8, 1)],
    note='Part b. Part a is in the 4B section.'),
]

SUBS = [('4A', 'Squared transformations'), ('4B', 'Log transformations'), ('4C', 'Reciprocal transformations'),
        ('4D', 'Choosing and applying the right transformation')]
