# Chapter 1 revision booklet: Insight GM1 (MC) + GM2 (SA), "Investigating data distributions".
# Text verbatim from Insight; shared "Use the following information" stems are repeated inside each box.
def stem(rows, key=None, left=None):
    h = '<table class="stp">' + ''.join(f'<tr><td class="s">{s}</td><td class="l">{l}</td></tr>' for s, l in rows) + '</table>'
    return h

def tbl(head, rows, cls='t'):
    h = f'<table class="{cls}"><tr>' + ''.join(f'<th>{x}</th>' for x in head) + '</tr>'
    for r in rows:
        h += '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>'
    return h + '</table>'

G1 = 'Insight GM1 U3 Data Analysis'
G2 = 'Insight GM2 U3 Data Analysis'

LUNCH = ('<p class="q">The canteen manager at a secondary school collected students’ preferred lunch choices prior to the school Athletics carnival.</p>'
         '<p class="q">The number of students from each sporting house (Yellow, Green, Blue and Purple) who selected each lunch option is shown in the two-way table below.</p>'
         '<table class="t"><tr><th rowspan="2">Lunch<br>choice</th><th colspan="4">Sporting house</th></tr><tr><th>Yellow</th><th>Green</th><th>Blue</th><th>Purple</th></tr>'
         '<tr><td>pizza</td><td>82</td><td>76</td><td>52</td><td>51</td></tr><tr><td>pie</td><td>76</td><td>64</td><td>47</td><td>49</td></tr>'
         '<tr><td>salad roll</td><td>63</td><td>58</td><td>54</td><td>43</td></tr><tr><td>sushi</td><td>71</td><td>63</td><td>61</td><td>48</td></tr>'
         '<tr class="tot"><td>Total</td><td>292</td><td>261</td><td>214</td><td>191</td></tr></table>')
Y9 = '<p class="q">The weights of female students in Year 9 at a particular secondary school are approximately normally distributed with a mean of 54.6 kg and a standard deviation of 6.2 kg.</p>'
TRIAL = '<p class="q">The teacher of the Year 12 students analysed the results, recorded as a total out of sixty, for the final extended-response trial exam completed by the students. He found the scores to be approximately symmetric with a mean of 43 and a standard deviation of 3.</p>'
MCT = ('<p class="q">The Year 12 teacher continued to perform statistical analysis on the scores of his Year 12 students. This time the teacher considered the score out of forty on the students’ first multiple-choice trial exam and the score achieved on the final multiple-choice trial exam. The teacher does not give half marks for this exam.</p>'
       '<p class="q">These results are represented in the parallel boxplots below.</p>[[m12]]')
BABY = ('<p class="q">The stem plot below displays the <i>weight,</i> in kilograms, of the first 25 babies born at a local hospital in 2019.</p>'
        '<div class="stk"><i>birth weight</i><span>key: 0 | 1 = 0.1</span></div>'
        + stem([('0', ''), ('1', '7 9'), ('2', '2 4 6 7 8'), ('3', '1 2 3 3 4 5 5 6 6 7 9'), ('4', '2 3 3 5 7 8'), ('5', '1')]))
VIC = '<p class="q">The birth weight of Victorian babies, born at 39 weeks or later, according to 2018 statistics, is approximately normally distributed with a mean of 3.3 kilograms and a standard deviation of 300 grams.</p>'
TEST = ('<p class="q">The stem plot below shows the distribution of mathematics <i>test scores</i> for a class of 15 students.</p>'
        '<div class="stk"><span>key: 1|2 = 12</span><span><i>n</i> = 15</span></div>'
        + stem([('0', '5 6'), ('1', '0 1 3'), ('2', '3 3 4 5'), ('3', '2 5 6'), ('4', '9'), ('5', '0 0')]))
RACE = '<p class="q">The results of a 400 metre race show a mean time of 138 seconds and a standard deviation of 6 seconds.</p>'
INC = ('<p class="q">The annual income of a sample of Australians was recorded and is shown in the table below.</p>'
       '<table class="t inc"><tr><th><i>Annual income</i> ($)</th></tr>' + ''.join(f'<tr><td>{x}</td></tr>' for x in
       ['9550', '17&#8239;500', '27&#8239;000', '34&#8239;800', '45&#8239;400', '53&#8239;100', '55&#8239;750', '68&#8239;350', '102&#8239;300', '128&#8239;000', '198&#8239;000', '212&#8239;200', '542&#8239;000', '2&#8239;304&#8239;000']) + '</table>')
SCH = ('<p class="q">An exam was undertaken at five schools, with the results normally distributed at each school.</p>'
       + tbl(['', 'Number of students', 'Mean (<i>x̄</i>)', 'Standard deviation (<i>s<sub>x</sub></i>)'],
             [['<b>School A</b>', 120, 64, 4], ['<b>School B</b>', 165, 70, 3], ['<b>School C</b>', 112, 65, 6], ['<b>School D</b>', 90, 72, 5], ['<b>School E</b>', 105, 70, 5]]))

def MC(n, sub, stem_, opts, a, why, fig=None, wide=False, shared=None):
    return dict(kind='mc', n=n, sub=sub, stem=stem_, opts=opts, a='ABCDE'.index(a), why=why, fig=fig, wide=wide,
                src=f'{G1} p.{[4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,11][n-1]} Q{n}', shared=shared)

Q = []
Q += [
 MC(1, '1B', LUNCH + '<p class="q">The <b>percentage</b> of students in Green house who selected a salad roll for their lunch is closest to</p>',
    ['5%', '20%', '21%', '22%', '25%'], 'D', '58 ÷ 261 × 100 = 22.2%', shared='Q1–3'),
 MC(2, '1A', LUNCH + '<p class="q">The variables <i>Sporting house</i> (Yellow, Green, Blue, Purple) and <i>Lunch choice</i> (pizza, pie, salad roll, sushi) are</p>',
    ['both nominal variables.', 'both ordinal variables.', 'a nominal variable and an ordinal variable respectively.', 'an ordinal variable and a nominal variable respectively.', 'an ordinal variable and a discrete variable respectively.'],
    'A', 'Both are categorical with no natural order: both nominal.', shared='Q1–3'),
 MC(3, '1B', LUNCH + '<p class="q">The most suitable graphical tool to display the data shown in the two-way table would be a</p>',
    ['back-to-back stem plot.', 'histogram.', 'dot plot.', 'scatterplot.', 'segmented bar chart.'], 'E', 'Two categorical variables: segmented bar chart.', shared='Q1–3'),
 MC(4, '1F', '<p class="q">The stem plot below displays the amount of money spent at the school canteen, per week, by a sample of 34 students.</p>'
    '<div class="stk"><b>money spent</b><b>Key: 3|5 = $3.50</b></div>' + stem([('3', '2 3 3 4 4 4'), ('3', '5 5 6 7'), ('4', ''), ('4', '6 6 6 7 9'), ('5', '1 2 2 3 4'), ('5', '5 5 7 9 9'), ('6', '0 1 1 2 4'), ('6', '7 7 9'), ('7', '2')])
    + '<p class="q">The median amount of money spent at the canteen per week is</p>', ['$2.00', '$2.20', '$4.60', '$5.20', '$5.25'], 'D', 'n = 34: median is between the 17th and 18th values, 5.2 and 5.2 → $5.20'),
 MC(5, '1H', Y9 + '<p class="q">There are 186 Year 9 females at the secondary school.</p><p class="q">The expected number of Year 9 females with weights between 42.2 kg and 73.2 kg is closest to</p>',
    ['97', '126', '177', '181', '185'], 'D', '42.2 = <i>z</i> −2, 73.2 = <i>z</i> +3: 47.5% + 49.85% = 97.35%; 0.9735 × 186 = 181', shared='Q5–6'),
 MC(6, '1H', Y9 + '<p class="q">A particular Year 9 student, Caterina, has a standardised weight of <i>z</i> = −1.24. Her actual weight, rounded to the nearest kg, is</p>',
    ['46 kg', '47 kg', '50 kg', '53 kg', '56 kg'], 'B', '<i>x</i> = 54.6 − 1.24 × 6.2 = 46.9 ≈ 47 kg', shared='Q5–6'),
 MC(7, '1E', '<p class="q">The histogram below shows the distribution of a data set that has been plotted on a <b>log<sub>10</sub></b> scale.</p>[[m7]]<p class="q">Based on the histogram, the percentage of data values less than 0.01 is closest to</p>',
    ['3%', '10%', '43%', '86%', '96%'], 'B', '0.01 = 10<sup>−2</sup>: bars below −2 hold 1 + 2 = 3 of 30 values = 10%'),
 MC(8, '1F', '<p class="q">The histogram below shows the <i>number of trial exams completed</i> by a class of Year 12 students in the final month before their Further Maths exam.</p>[[m8]]<p class="q">The median <i>number of trial exams</i> completed lies within the interval</p>',
    ['0–5', '5–10', '10–15', '15–20', '20–25'], 'C', 'Cumulative %: 7.5, 30.5, 53.5 → the 50% mark is in 10–15'),
 MC(9, '1F', '<p class="q">The Year 12 teacher ran a revision session at lunchtime, once a week, leading up to the exams. The table below shows the number of students who attended the study session over an 8 week period.</p>'
    + tbl(['Week', '1', '2', '3', '4', '5', '6', '7', '8'], [['<b><i>No. of students attending</i></b>', 13, 15, 7, 12, '<i>x</i>', 16, 17, 21]])
    + '<p class="q">If the mean number of students attending the study sessions is 14.0, the value of <i>x</i> is:</p>', ['3', '11', '12', '13', '14'], 'B', '8 × 14 = 112; 112 − 101 = 11', wide=False),
 MC(10, '1H', TRIAL + '<p class="q">The percentage of students who achieved a result, out of sixty, between 37 and 52 is:</p>', ['2.65%', '68%', '95%', '97.35%', '99.7%'], 'D', '37 is <i>z</i> = −2, 52 is <i>z</i> = 3: 47.5% + 49.85% = 97.35%', shared='Q10–11'),
 MC(11, '1H', TRIAL + '<p class="q">One of the Year 12 students received a score on his final trial exam that resulted in a standardised score, <i>z</i>-score, of −1.3.</p><p class="q">The score that this student achieved out of sixty, correct to the nearest whole number, was:</p>',
    ['33', '39', '41', '47', '56'], 'B', '43 − 1.3 × 3 = 39.1 ≈ 39', shared='Q10–11'),
 MC(12, '1A', MCT + '<p class="q">The variable <i>score out of forty</i> can be classified as</p>', ['categorical data.', 'numerical, continuous data.', 'categorical, nominal data.', 'numerical, discrete data.', 'numerical, ordinal data.'], 'D', 'Whole-number scores (no half marks): numerical, discrete.', shared='Q12–14'),
 MC(13, '1G', MCT + '<p class="q">The median <i>score out of forty</i> for the Year 12 students’ first trial exam is</p>', ['12', '17', '22', '26', '37'], 'C', 'Line inside the shaded box: 22', shared='Q12–14'),
 MC(14, '1G', MCT + '<p class="q">The IQR of the boxplot for the Year 12 students’ final trial exam is</p>', ['4.5', '5', '10', '11.5', '25'], 'C', 'IQR = 32 − 22 = 10', shared='Q12–14'),
 MC(15, '1D', BABY + '<p class="q">The percentage of babies born with a <i>weight</i> between 2.0 and 4.0 kilograms is</p>', ['4%', '8%', '36%', '64%', '66%'], 'D', '5 + 11 = 16 of 25 = 64%', shared='Q15–16'),
 MC(16, '1F', BABY + '<p class="q">The median <i>weight</i> of the newborn babies, in kilograms, is</p>', ['3.3', '3.4', '3.5', '3.6', '5.0'], 'C', 'n = 25: 13th value = 3.5', shared='Q15–16'),
 MC(17, '1C', '<p class="q">The percentage frequency histogram below displays the <i>weight</i>, in kilograms, of the next 25 babies born at the local hospital in 2019.</p>[[m17]]<p class="q">The percentage of babies born who are above the state average of 3.5 kilograms at birth is</p>',
    ['38%', '40%', '50%', '60%', '62%'], 'D', '24 + 20 + 12 + 4 = 60%'),
 MC(18, '1H', VIC + '<p class="q">A baby selected at random from the sample used has a standardised birth weight of <i>z</i> = 0.8.</p><p class="q">The baby’s actual birth weight, in kilograms, is</p>', ['0.75', '2.64', '3.06', '3.50', '3.54'], 'E', '3.3 + 0.8 × 0.3 = 3.54 kg', shared='Q18–20'),
 MC(19, '1H', VIC + '<p class="q">What percentage of babies born in Victoria can be expected to weigh between 2.7 and 3.9 kilograms at birth?</p>', ['64.0%', '66.5%', '81.5%', '95.0%', '99.7%'], 'D', '2.7 and 3.9 are <i>z</i> = ±2: 95%', shared='Q18–20'),
 MC(20, '1H', VIC + '<p class="q">A sample of 150 babies was chosen for closer studies.</p><p class="q">The predicted number of these babies with a birth weight less than 3.0 kilograms or greater than 3.9 kilograms is closest to</p>', ['16', '17', '26', '27', '28'], 'E', '&lt; 3.0 (<i>z</i> &lt; −1): 16%; &gt; 3.9 (<i>z</i> &gt; 2): 2.5%; 18.5% × 150 = 27.75 ≈ 28', shared='Q18–20'),
 MC(21, '1D', TEST + '<p class="q">The percentage of <i>test scores</i> that are below 25 is closest to</p>', ['8%', '9%', '15%', '53%', '60%'], 'D', '8 of 15 scores = 53%', shared='Q21–22'),
 MC(22, '1F', TEST + '<p class="q">An extra score was added. As a result, the lower quartile (<i>Q</i><sub>1</sub>) increased from 11 to 12, the median increased from 24 to 24.5 and the upper quartile (<i>Q</i><sub>3</sub>) decreased from 36 to 35.5.</p><p class="q">The score that was added could be</p>', ['7', '10', '24', '32', '48'], 'D', 'Adding 32: <i>Q</i><sub>1</sub> = (11+13)/2 = 12, median = (24+25)/2 = 24.5, <i>Q</i><sub>3</sub> = (35+36)/2 = 35.5', shared='Q21–22'),
 MC(23, '1F', '<p class="q">The histogram below shows the <i>number of hours per week</i> that students participate in cocurricular activities, in a school of 800 students.</p>[[m23]]<p class="q">The upper quartile (<i>Q</i><sub>3</sub>) falls into which interval?</p>',
    ['2 – &lt; 4 hours', '4 – &lt; 6 hours', '6 – &lt; 8 hours', '8 – &lt; 10 hours', '10 – &lt; 12 hours'], 'B', 'Cumulative %: 30, 65, 81 → the 75% mark is in 4 – &lt; 6'),
 MC(24, '1E', '<p class="q">The following scores are represented in a histogram with a log scale on the <i>x</i>-axis.</p><p class="q" style="text-align:center;word-spacing:2mm">3 7 10 25 87 112 250 812 970 1102</p><p class="q">Which one of the log histograms below best represents the data?</p>',
    ['[[m24A]]', '[[m24B]]', '[[m24C]]', '[[m24D]]', '[[m24E]]'], 'A', 'Logs: 0.5, 0.8 | 1.0, 1.4, 1.9 | 2.05, 2.4, 2.9, 2.99 | 3.04 → 2, 3, 4, 1'),
 MC(25, '1H', RACE + '<p class="q">Given that Janet’s time was 130 seconds, it can be concluded that</p>',
    ['she performed in the top 50% but not the top 16%.', 'she performed in the top 16% but not the top 2.5%.', 'she performed in the top 2.5% but not the top 0.15%.', 'she performed in the bottom 50% but not the bottom 16%.', 'she performed in the bottom 16% but not the bottom 2.5%.'],
    'B', '<i>z</i> = (130 − 138) ÷ 6 = −1.33; a lower time is better, so top 16% but not top 2.5%', shared='Q25–26'),
 MC(26, '1H', RACE + '<p class="q">Another student achieved a standardised score of 2.4.</p><p class="q">What was their actual time?</p>', ['23.0 seconds', '93.0 seconds', '123.6 seconds', '138.0 seconds', '152.4 seconds'], 'E', '138 + 2.4 × 6 = 152.4 s', shared='Q25–26'),
 MC(27, '1G', '<p class="q">An outlier test was conducted on a dataset. An upper fence of 63 was calculated.</p><p class="q">If the upper quartile (<i>Q</i><sub>3</sub>) is 45, the value of the lower fence is</p>', ['12', '15', '18', '33', '39'], 'B', '63 = 45 + 1.5 × IQR → IQR = 12, <i>Q</i><sub>1</sub> = 33; LF = 33 − 18 = 15'),
 MC(28, '1A', '<p class="q">Information relating to the following seven variables was asked for in a questionnaire:</p><ul class="q"><li><i>name</i></li><li><i>street address</i></li><li><i>postcode</i></li><li><i>occupation</i></li><li><i>place of birth</i></li><li><i>number of children</i></li><li><i>height</i></li></ul><p class="q">The number of these variables that are discrete numerical variables is</p>',
    ['0', '1', '2', '3', '4'], 'B', 'Only <i>number of children</i> (postcode is a label; height is continuous).'),
 MC(29, '1G', INC + '<p class="q">The upper fence is</p>', ['−210&#8239;000', '163&#8239;200', '198&#8239;000', '210&#8239;000', '442&#8239;800'], 'E', '<i>Q</i><sub>1</sub> = 34&#8239;800, <i>Q</i><sub>3</sub> = 198&#8239;000, IQR = 163&#8239;200; UF = 198&#8239;000 + 244&#8239;800 = 442&#8239;800', shared='Q29–30'),
 MC(30, '1E', INC + '<p class="q">Which one of the following would be the best way to represent the data?</p>', ['boxplot', 'segmented bar chart', 'two-way frequency table', 'log scale histogram', 'stem plot'], 'D', 'Values range over several powers of 10: use a log scale.', shared='Q29–30'),
 MC(31, '1G', '[[m31]]<p class="q">The interquartile range for the data represented by the boxplot above is</p>', ['2', '3.5', '5.5', '8.5', '10.5'], 'C', 'IQR = 16 − 10.5 = 5.5'),
 MC(32, '1F', '<p class="q">The distance, in kilometres, that 18 students travel to school from home is recorded and the following summary statistics are calculated.</p>'
    + tbl(['Min', '(<i>Q</i><sub>1</sub>)', 'Median', '(<i>Q</i><sub>3</sub>)', 'Max', 'Mean', 'Standard deviation'], [['0.9', '3.2', '4.7', '7.9', '12.7', '5.4', '3.5']])
    + '<p class="q">One student moves house, which changes her distance travelled from 4.3 km to 4.6 km.</p><p class="q">What impact will this have on the statistics shown above?</p>',
    ['The range will increase.', 'The mean will increase.', 'The interquartile range (IQR) will increase.', 'The median will increase.', 'The standard deviation will increase.'], 'B', 'The total increases, so the mean increases; 4.3 → 4.6 stays below the median 4.7.'),
 MC(33, '1D', '<p class="q">The stem plot below represents the number of students enrolled in Year 7 over 20 years at a local high school.</p><div class="stk"><span>key: 9|6 = 96</span><span>n = 20</span></div>'
    + stem([('9', '6'), ('10', '4'), ('11', '2 5 8'), ('12', '3 6 7 7 8'), ('13', '2 4 4 6 6 6 9'), ('14', '3 5 5')]) + '<p class="q">The distribution of this data is best described as</p>',
    ['symmetric.', 'a positive association.', 'a negative association.', 'positively skewed.', 'negatively skewed.'], 'E', 'Tail towards the low values: negatively skewed.'),
 MC(34, '1A', '<p class="q">Shoppers were asked to rate the customer service at a store. They were asked to rate the <i>speed of service</i> (1 = fast, 2 = average, 3 = slow) and their <i>likelihood of returning</i> to the store (yes, no).</p><p class="q">These variables are</p>',
    ['a numerical and ordinal variable respectively.', 'an ordinal and nominal variable respectively.', 'a nominal and ordinal variable respectively.', 'both ordinal variables.', 'both nominal variables.'], 'B', 'Speed has an order; yes/no does not.'),
 MC(35, '1H', SCH + '<p class="q">Mostyn achieved a score of 73 and was informed he was in the top 2.5% of students who undertook the exam in his school.</p><p class="q">The school Mostyn attends is</p>', ['School A.', 'School B.', 'School C.', 'School D.', 'School E.'], 'A', 'Top 2.5% means <i>z</i> ≥ 2. School A: 64 + 2 × 4 = 72 ≤ 73', shared='Q35–36'),
 MC(36, '1H', SCH + '<p class="q">76 students from one school achieved a standardised score within one standard deviation of the school mean.</p><p class="q">The school they attend is</p>', ['School A.', 'School B.', 'School C.', 'School D.', 'School E.'], 'C', '76 ÷ 0.68 = 111.8 ≈ 112 students: School C', shared='Q35–36'),
]

def SA(n, sub, page, marks, stem_, parts, why=None, fig=None):
    return dict(kind='sa', n=n, sub=sub, marks=marks, stem=stem_, parts=parts, why=why, src=f'{G2} {page} Q{n}')
# part: (label, text, answer, space_mm)
Q += [
 SA(1, '1G', 'p.4', 5, '<p class="q">A sample of travellers on an evening train were asked how many hours (to the nearest hour) they work in a week. The data were sorted into two categories, based on their age.</p>'
    '<div class="stk" style="justify-content:flex-end"><b>Key: 1|0 = 10 hours</b></div>'
    '<table class="b2b"><tr><th><i>18 – 24 years</i></th><th>Stem</th><th><i>25 – 30 years</i></th></tr>'
    + ''.join(f'<tr><td class="lf">{a}</td><td class="st">{s}</td><td class="rt">{b}</td></tr>' for a, s, b in [
        ('4 4 3 3', '0', ''), ('9 9 8 8 8 6 6 5', '0', ''), ('4 4 2 2 2 0 0', '1', '0 1 2 2'), ('9 9 9 8 8 7 6 5', '1', '8 9'), ('3 3 2 1 1', '2', '2 3 4'),
        ('7 7 6 5 5 5 5 5', '2', '5 5 6 8 9'), ('2 2 1', '3', '1 3 3 4'), ('', '3', '5 5 6 7 8 8'), ('', '4', '0 0 2 2 4 4'), ('5', '4', '5 5 6 7 8'), ('', '5', '2 2 3 3 4'), ('', '5', '8')])
    + '</table><p class="q">The results of this survey are shown in the back-to-back stem plot below.</p>',
    [('a', 'What type of data is the variable <i>hours worked</i>?', 'Numerical, discrete.', 10, 1),
     ('b', 'What percentage of 18–24-year-olds work more than 20 hours a week?<br>Round your answer to one decimal place.', '17 ÷ 44 × 100 = 38.6%', 14, 1),
     ('c', 'Find the median for the data gathered on <i>hours worked</i> for those in the 18–24 years category.', 'n = 44: (17 + 18) ÷ 2 = 17.5 hours', 12, 1),
     ('d', 'The statistician conducting the survey suspects that the data for the 18–24 years age group contain an outlier at 45 hours.<br>Is the statistician correct?<br>Explain your answer, showing a calculation to support your argument.',
      'IQR = 25 − 9 = 16. Upper fence = 25 + 1.5 × 16 = 49. 45 &lt; 49, so 45 is not an outlier: the statistician is not correct.', 30, 2)]),
 SA(2, '1G', 'p.5', 3, '<p class="q">A boxplot has been drawn for the <i>hours worked</i> data gathered. These boxplots are shown below.</p>[[s2]]',
    [('a', 'Describe the boxplot for the 25–30 years age group, in terms of shape, centre and spread.', 'Approximately symmetric, median about 35 hours, IQR = 45 − 25 = 20 hours (range 48 also accepted).', 18, 1),
     ('b', 'Which measure of centre, <b>mean</b> or <b>median</b>, would be most appropriate for a boxplot showing a positive skew?<br>Explain your answer.', 'The median: it is not pulled towards the long tail (extreme values), as the mean is.', 20, 2)],
    why='Boxplots redrawn from the Q1 stem plot. Insight reads the median as 35; the stem plot gives 36.'),
 SA(3, '1B', 'p.5', 2, '<p class="q">A mathematics teacher surveyed the 25 students in her Year 12 mathematics class to investigate their favourite topic studied in mathematics.</p><p class="q">The graph below displays the information she gathered, with the data for matrices missing.</p>[[s3]]',
    [('a', 'What percentage of the Year 12 students selected geometry as their favourite topic?', '3 ÷ 25 × 100 = 12%', 14, 1),
     ('b', 'Complete the graph above by drawing the bar for the number of students who selected matrices as their favourite topic.', '25 − (8 + 3 + 6 + 3) = 5: bar of height 5 (shown on the graph).', 14, 1)]),
 SA(4, '1F', 'p.6', 3, '<p class="q">The mathematics teacher continued her survey by asking the students to rate their effort in mathematics in previous years of study on a scale from 1 to 10.</p><p class="q">The information obtained from the students is displayed in the dot plot below.</p>[[s4]]',
    [('a', 'Find the median <i>effort rating</i> given by the students.', 'n = 25: 13th value = 5', 12, 1),
     ('b', 'Complete the following statement.<div class="fillin"><span class="bx"><u>36</u></span> per cent of students gave an <i>effort rating</i> between 3 and 7.</div>', 'Ratings 4, 5, 6: 4 + 3 + 2 = 9 students; 9 ÷ 25 × 100 = 36%', 4, 1),
     ('c', 'Is the variable <i>effort rating</i> numerical discrete or numerical continuous?', 'Numerical discrete.', 10, 1)]),
 SA(5, '1G', 'pp.6–7', 5, '<p class="q">End of year results for the Year 11 mathematics exam were recorded by the teacher as a score out of 50. The teacher was interested in determining whether <i>gender</i> is related to <i>end of year result.</i></p><p class="q">The students’ Year 11 mathematics results are shown in the graph below.</p>[[s5]]',
    [('a', 'Describe the shape of the boxplot for <b>female</b> <i>end of year result.</i>', 'Positively skewed.', 10, 1),
     ('b', 'Complete the following five-number summary for <b>male</b> <i>end of year result.</i>'
      '<table class="t fill"><tr><th rowspan="2"><i>Gender</i></th><th colspan="5"><i>End of year result</i></th></tr><tr><th>min</th><th><i>Q</i><sub>1</sub></th><th><i>M</i></th><th><i>Q</i><sub>3</sub></th><th>max</th></tr>'
      '<tr><td>Male</td><td><u>3</u></td><td>26</td><td>32</td><td><u>41</u></td><td>50</td></tr><tr><td>Female</td><td>15</td><td>17.5</td><td>26</td><td>42.5</td><td>49</td></tr></table>', 'The outlier 3 is still the minimum; <i>Q</i><sub>3</sub> = 41.', 2, 2),
     ('c', 'Show that the male student who received a result of 3 out of 50 for his end-of-year examination is an outlier.', 'IQR = 41 − 26 = 15. Lower fence = 26 − 1.5 × 15 = 3.5. 3 &lt; 3.5, so 3 is an outlier.', 28, 2)]),
 SA(6, '1G', 'pp.7–8', 9, '<p class="q"><b>Table 1</b></p>' + tbl(['<i>Destination</i>', '<i>Flights per month</i>', '<i>Flights delayed &gt;5 min</i>', '<i>Minutes delayed</i>'],
        [['Sydney', 186, 49, 85], ['Perth', 124, 31, 55], ['Brisbane', 155, 41, 65], ['Adelaide', 65, 17, 27], ['Hobart', 94, 24, 126], ['Cairns', 65, 15, 285], ['Darwin', 31, 10, 314], ['Townsville', 54, 14, 384], ['Launceston', 42, 12, 235], ['Uluru', 80, 21, 155], ['Ballina (Byron)', 110, 28, 43], ['Sunshine Coast', 125, 33, 62]], 't sm')
    + '<p class="q">The data in Table 1 shows a range of scheduled flights, departing from Melbourne airport, run by a local airline, Airsetter Airlines.</p><p class="q">The four variables in this data set are:</p><ul class="q"><li><i>destination</i> – name of city</li><li><i>flights per month</i> – total number of flights</li><li><i>flights delayed &gt;5 min</i> – total number of flights delayed more than 5 minutes</li><li><i>minutes delayed</i> – average minutes delayed in October 2018.</li></ul><p class="q">A flight is classified as ‘delayed’ if the departure time is greater than 5 minutes after the scheduled time.</p>',
    [('a', 'How many variables are numerical, discrete variables?', '3 (Insight’s answer; <i>destination</i> is not numerical).', 8, 1),
     ('b', 'What percentage of flights from Melbourne to Townsville were classified as delayed flights?<br>Round your answer to one decimal place.', '14 ÷ 54 × 100 = 25.9%', 10, 1),
     ('c', 'Complete the following five-number summary for the variable <i>minutes delayed.</i><br><b>Table 2</b><table class="t fill"><tr><th>Min</th><th><i>Q</i><sub>1</sub></th><th>Median</th><th><i>Q</i><sub>3</sub></th><th>Max</th></tr><tr><td>27</td><td>58.5</td><td><u>105.5</u></td><td>260</td><td><u>384</u></td></tr></table>', 'Median = (85 + 126) ÷ 2 = 105.5; maximum = 384', 2, 1),
     ('d', 'Using the five-number summary, sketch the boxplot for the variable <i>minutes delayed</i> on the scale provided below.[[s6d]]', '', 0, 2),
     ('e', 'Describe the shape of the distribution of the total minutes delayed for the airline.', 'Positively skewed.', 8, 1),
     ('f', 'Complete the following sentence by writing the correct numerical values in the appropriate boxes provided below.<div class="fillin">For the distribution of <i>minutes delayed</i>, the middle 50% of the data lies between <span class="bx"><u>58.5</u></span> and <span class="bx"><u>260</u></span> minutes.</div>', '', 2, 1),
     ('g', 'Write down a calculation to show that the value 27 is not an outlier for this data set.', 'Lower fence = 58.5 − 1.5 × (260 − 58.5) = −243.75. 27 &gt; −243.75, so 27 is not an outlier.', 22, 2)]),
 SA(7, '1G', 'p.9', 4, '<p class="q">Table 1 shows the <i>day number</i> and the <i>number of calories burned</i> by <i>Gym patron 1</i> during each 1.5 hour workout for the first 13 days of April 2019.</p><p class="q"><b>Table 1</b></p>'
    + tbl(['<i>Day number</i>', '<i>Number of calories burned</i>', '<i>Day number</i>', '<i>Number of calories burned</i>'], [[1, 630, 8, 910], [2, 726, 9, 879], [3, 905, 10, 637], [4, 558, 11, 716], [5, 672, 12, 847], [6, 775, 13, 690], [7, 821, '', '']], 't sm'),
    [('a', 'What type of data is the variable <i>number of calories burned</i>?', 'Numerical, discrete.', 8, 1),
     ('b', 'Using Table 2, complete the five-number summary for the data, <i>number of calories burned,</i> given in Table 1.<br>Round your answers to the nearest whole number.<br><b>Table 2</b><table class="t fill"><tr><th>Min</th><th><i>Q</i><sub>1</sub></th><th>Median</th><th><i>Q</i><sub>3</sub></th><th>Max</th></tr><tr><td>558</td><td><u>655</u></td><td>726</td><td>863</td><td><u>910</u></td></tr></table>', '<i>Q</i><sub>1</sub> = (637 + 672) ÷ 2 = 654.5 ≈ 655', 8, 2),
     ('c', 'Calculate the percentage of days on which <i>Gym Patron 1</i> burned less than 700 calories.<br>Round your answer to one decimal place.', '5 ÷ 13 × 100 = 38.5%', 12, 1)]),
 SA(8, '1H', 'p.9', 2, '<p class="q">For a particular cycle class, the <i>number of calories burned</i> by each gym patron who participates in the class is approximately normally distributed with a mean of 375 calories and a standard deviation of 3 calories.</p>',
    [('a', 'Determine the percentage of patrons who will burn less than 369 calories.', '369 = 375 − 2 × 3 (<i>z</i> = −2): 2.5%', 14, 1),
     ('b', '500 patrons participate in the cycle class over a period of one week.<br>How many of these people can be expected to burn between 375 and 381 calories during the cycle class?', '<i>z</i> = 0 to 2: 47.5%; 0.475 × 500 = 237.5 ≈ 238 patrons', 18, 1)]),
 SA(9, '1H', 'p.10', 4, '<p class="q">The number of fish caught by 15 people at a holiday destination was recorded and displayed in the dot plot below.</p>[[s9]]',
    [('a', 'Determine the median <i>number of fish caught</i>.', 'n = 15: 8th value = 2 fish', 8, 1),
     ('b', 'If everyone caught an extra three fish, by how much would the standard deviation increase?', 'By zero: the spread does not change.', 8, 1),
     ('c i', 'Assume that, at another holiday destination, the mean weight of fish caught annually by 2000 visitors was normally distributed. The mean weight of fish caught per person was 1.8 kg, with a standard deviation of 0.4 kg.<br>Determine<br>the number of visitors who caught fish weighing between 1 kg and 3 kg.', '1 kg is <i>z</i> = −2, 3 kg is <i>z</i> = 3: 47.5% + 49.85% = 97.35%; 0.9735 × 2000 = 1947 visitors', 14, 1),
     ('ii', 'the actual weight of a fish caught if its standardised weight is −0.75.', '1.8 − 0.75 × 0.4 = 1.5 kg', 12, 1)]),
 SA(10, '1G', 'p.11', 4, '<p class="q">A research study is conducted on 2300 babies from birth until they are 12 months old. Of these babies, 1100 were girls and 1200 were boys.</p><p class="q">The data on the weight of the babies at six months of age for both boys and girls is shown below.</p>'
    + tbl(['<i>Weight at six months</i> (kg)', 'Min.', '<i>Q</i><sub>1</sub>', 'Median', '<i>Q</i><sub>3</sub>', 'Max.'], [['girls', 6.7, '7.0', 7.3, 7.7, 8.2], ['boys', 6.8, 7.7, 7.9, 8.2, 8.8]], 't sm') + '[[s10]]',
    [('a i', 'How many babies weighed<br>more than 8.2 kg?', '25% of the boys: 0.25 × 1200 = 300 babies', 12, 1),
     ('ii', 'less than 7.7 kg?', '75% of girls + 25% of boys: 825 + 300 = 1125 babies', 14, 1),
     ('b', 'It is realised that the boxplot for boys has ignored outliers in the data.<br>Show that 6.8 is an outlier.', 'IQR = 8.2 − 7.7 = 0.5. Lower fence = 7.7 − 1.5 × 0.5 = 6.95. 6.8 &lt; 6.95, so 6.8 is an outlier.', 22, 2)]),
 SA(11, '1H', 'pp.12–13', 6, '<p class="q">Farah gets a job at a supermarket.</p><p class="q">The table below shows the sales information for each hour of trade on a particular day at the supermarket. The store was open for 14 hours.</p>'
    + tbl(['Hour number', 'No. of customers', 'Hourly total sales ($)'], [[1, 51, 520], [2, 82, 4815], [3, 176, 9740], [4, 194, '15&#8239;600'], [5, 92, 6025], [6, 34, 4010], [7, 120, '12&#8239;985'], [8, 105, 6630], [9, 82, 5325], [10, 134, 6210], [11, 176, 6510], [12, 86, 4025], [13, 55, 2750], [14, 42, 2110], ['<b>Total</b>', '<b>1429</b>', '<b>87&#8239;255</b>']], 't sm'),
    [('a i', 'In which hour did the store have the most customers?', 'Hour 4 (194 customers)', 8, 1),
     ('ii', 'What was the average sales per customer?<br>Round your answer to the nearest dollar.', '87&#8239;255 ÷ 1429 = 61.06 ≈ $61', 10, 1),
     ('b', 'The manager examines the hourly total sales and checks if any values should be considered outliers.<br>Determine if the sales figure of $520 is an outlier, showing calculations to justify your answer.', '<i>Q</i><sub>1</sub> = 4010, <i>Q</i><sub>3</sub> = 6630, IQR = 2620. Lower fence = 4010 − 1.5 × 2620 = 80. 520 &gt; 80, so $520 is not an outlier.', 26, 2),
     ('c', 'The age of the 38 permanent staff at the supermarket is normally distributed. The mean age is 34 years and the standard deviation is 4.6 years.<br>The age of the 52 casual staff is also normally distributed. The mean age is 19 years and the standard deviation is 1.2 years.<br>Farah’s friend Toni is 25 years old. Using the 68–95–99.7% rule, Toni is in the youngest 16% of the permanent staff and oldest 0.15% of the casual staff.<br>Farah is 21 years old.<br>Using the 68–95–99.7% rule, describe her age, referring to the relevant percentages, in relation to both the permanent and casual members of staff.',
      'Permanent: 20.2 (−3<i>s</i>) &lt; 21 &lt; 24.8 (−2<i>s</i>) → youngest 2.5%. Casual: 20.2 (+1<i>s</i>) &lt; 21 &lt; 21.4 (+2<i>s</i>) → oldest 16%.', 26, 2)]),
 SA(12, '1E', 'p.13', 1, '<p class="q">After work, Farah visits a homewares store next to the supermarket.</p><p class="q">The histogram below shows the distribution of <i>sales per hour</i> ($) on a particular day at the homewares store. The histogram has been plotted on a log<sub>10</sub> scale.</p>[[s12]]'
    '<p class="q">There were 7 hours during this day in which the <i>sales per hour</i> were between $100 and $10&#8239;000.</p>',
    [('', 'Draw a bar on the <b>histogram</b> to represent the missing information accurately.<br><i>(Answer on the histogram.)</i>', '$100 to $10&#8239;000 is log 2 to 4; the 2–3 bar has 2, so the 3–4 bar has 7 − 2 = 5.', 4, 1)]),
]

SUBS = [('1A', 'Types of data'), ('1B', 'Displaying and describing categorical data'), ('1C', 'Displaying numerical data: histograms'),
        ('1D', 'Dot plots and stem plots'), ('1E', 'Using a log scale to display data'), ('1F', 'Summarising numerical data: centre and spread'),
        ('1G', 'Boxplots and outliers'), ('1H', 'The normal model and standardised scores')]
