"""Lesson l03 (2A-2B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Questions verbatim, same items and order as tools/deck/l03/build.py.
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 2 skills checklist 2A #2; APK 2 = Cambridge U1&2 Ch 1 skills checklist 1A #2.
Examples 1-8 = Cambridge U3&4 Examples 1-8 (pp. 105-117). You try 1 = Edrolo U1&2 1A WE1; You try 2, 3 = Edrolo U3&4 2C WE1, WE2;
You try 4-8 = Edrolo U3&4 2A WE1, WE4, WE2, WE3, WE5. Exits = Edrolo U3&4 2A Q11 (VCAA 2018 Exam 2 Core Q1d), 2A Q13 (VCAA 2021 Exam 1 Core Q3).
Output: lessons/2A-2B worksheet(.html/.pdf) + lessons/2A-2B worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l03/worksheet.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *
import ws2

def tw(rv, ev, cats, rows, total=None, totcol=None, style=''):
    """two-way table: EV across the columns, RV down the rows. Cells may be a(...) (blank for students, red on solutions)."""
    n = len(cats)
    h = f'<tr><th style="background:none;border:none"></th><th colspan="{n}"><i>{ev}</i></th>' + ('<th style="background:none;border:none"></th>' if totcol else '') + '</tr>'
    h += f'<tr><th class="l"><i>{rv}</i></th>' + ''.join(f'<th>{c}</th>' for c in cats) + ('<th>Total</th>' if totcol else '') + '</tr>'
    tr = ''.join(f'<tr><td class="l">{lab}</td>' + ''.join(f'<td>{x}</td>' for x in cells + ([totcol[r]] if totcol else [])) + '</tr>' for r, (lab, cells) in enumerate(rows))
    if total: tr += '<tr><td class="l"><b>Total</b></td>' + ''.join(f'<td><b>{x}</b></td>' for x in total) + '</tr>'
    return f'<table class="t fill" style="{style}">{h}{tr}</table>'
def side(left, fig, w): return f'<div class="row"><div style="flex:1">{left}</div><div style="flex:none;width:{w}mm">{fig}</div></div>'
def gbar(cats, names, vals, ymax, ystep, xl, yl, W=250, H=125, mm=66):
    L, T, B = 34, 8, 26
    o, y0, k = ws2._grid(W, H, L, T, B, ymax, ystep, yl, xl)
    slot = (W - 70 - L) / len(cats); bw = slot * .8 / len(names); g = []
    for i, c in enumerate(cats):
        for j in range(len(names)):
            v = vals[j][i]; g.append(f'<rect x="{L+i*slot+slot*.1+j*bw:.1f}" y="{y0-v*k:.1f}" width="{bw:.1f}" height="{v*k:.1f}" fill="none" stroke="{RED}"/>')
        g.append(f'<text x="{L+(i+.5)*slot:.1f}" y="{y0+10}" font-size="8" text-anchor="middle" fill="{RED}">{c}</text>')
    for j, n in enumerate(names): g.append(f'<text x="{W-62}" y="{T+10+j*12}" font-size="8" fill="{RED}">{j+1} = {n}</text>')
    o.append('<g>' + ''.join(g) + '</g>')
    return ws2._svg(W, H, o, mm)
def scat(pts, W=230, H=150, mm=58):
    L, T, B = 34, 8, 26
    o, y0, k = ws2._grid(W, H, L, T, B, 200, 50, 'daily sugar intake (g)', 'number of soft drinks consumed per week')
    sx = lambda x: L + x / 10 * (W - 8 - L)
    o += [f'<text x="{sx(x):.1f}" y="{y0+10}" font-size="8" text-anchor="middle">{x}</text>' for x in range(0, 11, 2)]
    o += [f'<circle cx="{sx(x):.1f}" cy="{y0-y*k:.1f}" r="2.6" fill="#000"/>' for x, y in pts]
    return ws2._svg(W, H, o, mm)

P = [title('2A–2B', 'Investigating associations between two categorical variables')]
P.append(lis(['To introduce bivariate data.', 'To be able to classify data as categorical or numerical.', 'To be able to identify explanatory and response variables.',
  'To be able to summarise data from two categorical variables using two-way frequency tables.', 'To be able to appropriately percentage two-way frequency tables.',
  'To be able to use a percentaged two-way frequency table to identify and describe an association between two categorical variables.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
CN = 'bad, bad, ok, ok, good, bad, good, ok, ok, ok, bad, ok, bad, good, good, good, good, bad, ok, ok'
P.append(pair(box('Question 1', q(f'Twenty students rated their school canteen as bad, ok or good, giving the following data: {CN}.') + q('Construct a percentage frequency table.')
      + space(30, table([['Rating', 'Frequency', '%'], ['bad', 6, 30], ['ok', 8, 40], ['good', 6, 30], ['<b>Total</b>', '<b>20</b>', '<b>100</b>']]), grow=True)),
  box('Question 2', q('What is 0.67 as a percentage?') + space(10, '0.67 × 100 = 67%', grow=True))))

# ---------------------------------------------------------------- 2A
P.append(sect('2A Bivariate data – Classifying the variables', 'Example, then you try'))
P.append(exyt('Example 1 · Categorical or numerical', q('For each of the following questions, determine if they involve investigating associations between<br>■ one numerical variable and one categorical variable or<br>■ two categorical variables or<br>■ two numerical variables.')
      + parts([('a', 'Are younger people (age measured in years) more likely to believe in astrology (measured as ‘yes’ or ‘no’) than older people?', 'One numerical variable (<i>age</i>) and one categorical variable (<i>belief in astrology</i>)', 'L'),
               ('b', 'Do people who weigh more (weight measured in kg) tend to have higher blood pressure (blood pressure measured in mmHg)?', 'Two numerical variables (<i>weight</i> and <i>blood pressure</i>)', 'L'),
               ('c', 'Are people who have a driver’s licence (measured as ‘yes’ or ‘no’) more likely to be in favour of lowering the driving age (measured as ‘yes’ or ‘no’)?', 'Two categorical variables (<i>have a driver’s licence</i> and <i>support for lowering the driving age</i>)', 'L')]),
  'You try 1', q('Is the variable <i>hair colour</i> an example of categorical or numerical data?') + space(12, 'Categorical: it can’t be counted or measured; it is sorted into groups.', grow=True)))
P.append(exyt('Example 2 · Response and explanatory variables', q('We wish to investigate the question, ‘Does the time it takes a student to get to school depend on their mode of transport?’ The variables here are <i>time</i> and <i>mode of transport</i>. Which is the response variable (RV) and which is the explanatory variable (EV)?')
      + parts([('EV', '', '<i>mode of transport</i>', 'L'), ('RV', '', '<i>time</i>', 'L')]),
  'You try 2', q('The following question was posed: ‘Can the <i>number of ice creams sold</i> be predicted from the <i>temperature</i>?’<br>Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.')
      + space(16, 'RV: <i>number of ice creams sold</i><br>EV: <i>temperature</i>', grow=True)))
SP = [(0, 98), (1, 90), (2, 110), (3, 122), (4, 125), (5, 130), (6, 137), (7, 145), (8, 166), (9, 192), (10, 188)]
P.append(exyt('Example 3 · Response and explanatory variables', q('Can we predict people’s height (in cm) from their wrist measurement? The variables in this investigation are <i>height</i> and <i>wrist measurement</i>. Which is the response variable (RV) and which is the explanatory variable (EV)?')
      + parts([('EV', '', '<i>wrist measurement</i>', 'L'), ('RV', '', '<i>height</i>', 'L')]),
  'You try 3', q('A study was conducted on the association between <i>daily sugar intake</i> and the <i>number of soft drinks consumed per week</i>. The following scatterplot displays the data that was collected.')
      + scat(SP) + q('Identify the response variable, <i>RV</i>, and the explanatory variable, <i>EV</i>.')
      + space(14, 'RV: <i>daily sugar intake</i> (vertical axis)<br>EV: <i>number of soft drinks consumed per week</i> (horizontal axis)', grow=True)))

# ---------------------------------------------------------------- 2B
P.append(sect('2B Investigating associations between categorical variables', 'Example, then you try'))
ST = [('Female', 'Yes'), ('Male', 'Yes'), ('Female', 'No'), ('Female', 'Yes'), ('Male', 'No'), ('Male', 'Yes'), ('Female', 'Yes'), ('Male', 'No'), ('Female', 'No'), ('Female', 'Yes')]
STT = '<div class="row" style="justify-content:center">' + ''.join(table([['Student', '<i>Gender</i>', '<i>University</i>']] + [[i + 1, *ST[i]] for i in rng], cls='t tiny', style='font-size:8pt;margin:1mm 0') for rng in (range(5), range(5, 10))) + '</div>'
E1 = tw('opinion', 'studying status', ['studying', '', 'not studying', ''], [('for', ['20', a('55.56%'), '5', a('25.00%')]), ('against', ['16', a('44.44%'), '15', a('75.00%')])], total=['36', '100%', '20', '100%'])
P.append(exyt('Example 4 · Constructing a two-way frequency table', q('The following data were obtained when a sample of ten Year 9 students were asked if they intended to go to university (<i>university</i>). The gender of the student was also recorded.')
      + STT + q('Create a two-way frequency table from these data.')
      + tw('University', 'Gender', ['Male', 'Female'], [('Yes', [a(2), a(4)]), ('No', [a(2), a(2)])], total=[a(4), a(6), a(10)], totcol=[a(6), a(4)]),
  'You try 4', q('A group of people were surveyed on their opinion towards offering a student discount for public transport. Their <i>studying status</i> was recorded as ‘studying’ or ‘not studying’ along with their <i>opinion</i> ‘for’ or ‘against’ the student discount.')
      + q('Complete the percentage frequency table by filling out the missing columns with the percentage frequency of each category, rounded to two decimal places.') + E1
      + space(10, '20/36 × 100 ≈ 55.56% · 16/36 × 100 ≈ 44.44% · 5/20 × 100 = 25.00% · 15/20 × 100 = 75.00%', grow=True)))
Y4 = tw('preference', 'age', ['under 20', '', '20 and over', ''], [('hardcopy', ['20', '56%', '15', '75%']), ('digital', ['16', '44%', '5', '25%'])], total=['36', '100%', '20', '100%'])
P.append(exyt('Example 5 · Association from a percentaged table (2 × 2)', q('Are males and females in Year 9 equally likely to indicate an intention to go to university? Data from interviews with 200 Year 9 students are summarised in the following table. Write a brief report addressing this question and quoting appropriate percentages.')
      + '<div class="row" style="justify-content:space-between">' + tw('University', 'Gender', ['Male', 'Female'], [('Yes', ['50', '54']), ('No', ['55', '41'])], total=['105', '95', '200'], totcol=['104', '96'], style='font-size:8pt;margin:1mm 0').replace('class="t fill"', 'class="t tiny"')
      + tw('University', 'Gender', ['Male', 'Female'], [('Yes', [a('47.6%'), a('56.8%')]), ('No', [a('52.4%'), a('43.2%')])], total=['100.0%', '100.0%'], style='font-size:8pt;margin:1mm 0').replace('class="t fill"', 'class="t tiny"') + '</div>'
      + report(['In this sample of 200 Year 9 students, a greater proportion of ', ('category', 'females'), ' than ', ('category', 'males'), ' (', ('%', '56.8%'), ' compared with ', ('%', '47.6%'),
                ') were intending to go to university. There ', ('is / is not', 'is'), ' an association between ', ('EV', 'gender'), ' and ', ('RV', 'intention to go to university'), '.']),
  'You try 5', q('A group of people were surveyed on their <i>preference</i> towards reading hardcopy or digital books. Their <i>age</i> (under 20, 20 and over) was recorded along with their book <i>preference</i> (hardcopy, digital).<br>The results were displayed in a two-way percentage frequency table.')
      + Y4 + q('Is there an association between <i>age</i> and <i>preference</i>? Justify your answer by quoting appropriate percentages.')
      + space(30, 'Yes, there is an association between <i>preference</i> and <i>age</i>. The percentage of people that prefer hardcopy books differs depending on their age, since only 56% of those under 20 prefer it while 75% of those aged 20 years and over do.', grow=True)))
SPORT = tw('Interest in sport', 'Age group (%)', ['Under 18 years', '19–25 years', '26–35 years', '36–50 years'], [('High', ['56.5', '50.2', '40.7', '35.0']), ('Medium', ['30.1', '34.4', '36.8', '44.7']), ('Low', ['13.4', '15.4', '22.5', '20.3'])], total=['100.0'] * 4, style='font-size:8.4pt')
CF = [[22, 16, 10, 2], [5, 10, 14, 17], [3, 4, 6, 11]]
P.append(exyt('Example 6 · Association from a percentaged table (3 × 3)', q('A survey was conducted with 1000 males under 50 years old. As part of this survey, they were asked to rate their interest in sport as ‘high’, ‘medium’, or ‘low’. Their age group was also recorded as ‘under 18’, ‘19–25’, ‘26–35’ and ‘36–50’. The results are displayed in the table.')
      + SPORT + parts([('a', 'Which is the explanatory variable, <i>interest in sport</i> or <i>age group</i>?', '<i>Age group</i> is the EV.', 'L'),
                       ('b', 'Is there an association between <i>interest in sport</i> and <i>age group</i>? Write a brief response quoting appropriate percentages.',
                        'There is an association between the level of interest in sport and age. A high level of interest in sport is seen to decrease steadily across the age categories from 56.5% for under 18 years, 50.2% for 19–25 years, 40.7% for 26–35 years to, at its lowest, 35% for 36–50 years.', 26)]),
  'You try 6', q('A group of individuals between the ages of 20 and 59 were asked how much coffee they drink a day. Their <i>caffeine intake</i> was categorised as ‘low’, ‘medium’ and ‘high’. Their <i>age</i> was also recorded and grouped as ‘20–29’, ‘30–39’, ‘40–49’ and ‘50–59’. The results are displayed in a two-way frequency table.')
      + tw('caffeine intake', 'age', ['20–29', '30–39', '40–49', '50–59'], [('low', CF[0]), ('medium', CF[1]), ('high', CF[2])])
      + q('Use the frequency table to construct a grouped bar chart.') + space(36, gbar(['20–29', '30–39', '40–49', '50–59'], ['low', 'medium', 'high'], CF, 25, 5, 'age', 'frequency', W=260, H=130, mm=72), grow=True)))
HT = tw('height', 'year level', ['Year 11', 'Year 12'], [('short', ['15%', '20%']), ('average', ['20%', '30%']), ('tall', ['65%', '50%'])], total=['100%', '100%'])
P.append(exyt('Example 7 · Constructing a segmented bar chart', q('Construct a segmented bar chart to display the association <i>interest in sport</i> and <i>age group</i> displayed in the table in Example 6.')
      + segbar(None, ['High', 'Medium', 'Low'], 100, 10, 'Interest in sport (%)', 'Age group (years)', draw=False, W=320, H=170, mm=78,
               bars=[('under 18', [56.5, 30.1, 13.4]), ('19–25', [50.2, 34.4, 15.4]), ('26–35', [40.7, 36.8, 22.5]), ('36–50', [35.0, 44.7, 20.3])]),
  'You try 7', q('A group of students in Year 11 and Year 12 were asked to describe their <i>height</i> as ‘short’, ‘average’ or ‘tall’. Their responses, as well as their <i>year level</i>, were recorded in the following percentage frequency table.')
      + HT + q('Use the frequency table to construct a percentage segmented bar chart.')
      + space(40, segbar(None, ['short', 'average', 'tall'], 100, 20, 'frequency (%)', 'year level', draw=False, W=220, H=140, mm=56, bars=[('Year 11', [15, 20, 65]), ('Year 12', [20, 30, 50])]), grow=True)))
HOL = segbar(None, ['coast', 'country'], 100, 20, 'Preferred holiday (%)', 'Age group', W=230, H=125, mm=56, bars=[('under 40', [75, 25]), ('40 and over', [60, 40])])
EMP = segbar(None, ['employed', 'unemployed'], 100, 20, 'frequency (%)', 'age', W=240, H=125, mm=58, bars=[('18–21', [40, 60]), ('22–25', [75, 25])])
P.append(exyt('Example 8 · Association from a segmented bar chart', q('The percentaged segmented bar chart below shows the association between <i>preferred holiday</i> (country or coast) and <i>age group</i> (under 40, 40 or over) for a sample of 800 visitors to a travel website.')
      + HOL + q('Does the percentaged segmented bar chart support the contention there is an association between <i>preferred holiday</i> and <i>age group</i>?')
      + report(['There ', ('is / is not', 'is'), ' an association between the ', ('RV', 'holiday preference'), ' and ', ('EV', 'age'), '. Those aged under forty are more likely to choose a coastal holiday (', ('%', '75%'), ') than those aged forty or over (', ('%', '60%'), ').']),
  'You try 8', q('A large group of people between the ages of 18 and 25 were asked what their current <i>employment status</i> was. They were classified as either ‘employed’ or ‘unemployed’. Their <i>age</i> was also recorded and classified as ‘18–21’ or ‘22–25’.<br>The results have been displayed in a percentage segmented bar chart.')
      + EMP + q('Is there an association between <i>employment status</i> and <i>age</i>? Justify your answer by quoting appropriate percentages.')
      + space(26, 'Yes, there is an association between <i>employment status</i> and <i>age</i>. The percentage of people that are employed tends to increase with age, with 40% of 18–21 year olds employed and 75% of 22–25 year olds employed.', grow=True)))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
UK = [('Belfast', 'high', 'small', 52), ('Edinburgh', 'high', 'small', 43), ('London', 'high', 'large', 40), ('Manchester', 'high', 'large', 44), ('Brighton and Hove', 'high', 'small', 35), ('Bournemouth', 'high', 'small', 36),
      ('Sheffield', 'medium', 'small', 36), ('Hull', 'medium', 'small', 40), ('Bristol', 'medium', 'small', 39), ('Newcastle-Sunderland', 'medium', 'large', 34), ('Leicester', 'medium', 'small', 36), ('Liverpool', 'medium', 'large', 29),
      ('Swansea', 'low', 'small', 30), ('Glasgow', 'low', 'large', 34), ('Cardiff', 'low', 'small', 31), ('Nottingham', 'low', 'small', 31), ('Birmingham-Wolverhampton', 'low', 'large', 29), ('Leeds-Bradford', 'low', 'large', 31),
      ('Portsmouth', 'low', 'small', 27), ('Southampton', 'low', 'small', 30), ('Reading', 'low', 'small', 31), ('Coventry', 'low', 'small', 30), ('Stoke-on-Trent', 'low', 'small', 29)]
HD = ['City', 'Congestion level', 'Size', 'Increase in travel time (minutes per day)']
UKT = lambda r: table([HD] + [list(u) for u in UK[r]], cls='t tiny')
T2 = '<div style="font-weight:bold;font-size:9pt">Table 2</div>' + tw('Congestion level', 'City size', ['Small', 'Large'], [('high', ['4', a(2)]), ('medium', [a(4), a(2)]), ('low', [a(8), a(3)])], total=['16', a(7)])
P.append(box('Exit task 1 · VCAA 2018 Exam 2 Q1d', q('<b>Table 1</b> &nbsp;The data in Table 1 relates to the impact of traffic congestion in 2016 on travel times in 23 cities in the United Kingdom (UK).')
  + f'<div class="row" style="justify-content:center">{UKT(slice(0, 12))}{UKT(slice(12, 23))}</div>'
  + q('The four variables in this data set are:<br>• <i>city</i> – name of city<br>• <i>congestion level</i> – traffic congestion level (high, medium, low)<br>• <i>size</i> – size of city (large, small)<br>• <i>increase in travel time</i> – increase in travel time due to traffic congestion (minutes per day).')
  + side(q('Use the data in Table 1 to complete the following two-way frequency table, Table 2.'), T2, 70), '2 marks'))
def ot(d, i, t): return table([['', 'Under 55 years', '55 years and over'], ['domestic', *d], ['international', *i], ['<b>Total</b>', *t]], cls='t tiny')
TRAVEL = segbar(None, ['international', 'domestic'], 100, 10, 'percentage', 'age (years)', bars=[('under 55', [35, 65]), ('55 and over', [55, 45])], W=250, H=150, mm=62)
P.append(box('Exit task 2 · VCAA 2021 Exam 1 Q3', side(q('The percentaged segmented bar chart below shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).')
      + q('The results could also be summarised in a two-way frequency table.<br>Which one of the following frequency tables could match the percentaged segmented bar chart?'), TRAVEL, 60)
  + mc([ot((91, 90), (49, 110), (140, 200)), ot((65, 35), (45, 55), (110, 90)), ot((35, 55), (65, 45), (100, 100)), ot((50, 70), (100, 50), (150, 120)), ot((71, 39), (29, 61), (100, 100))], 'A', cols=3)
  + why('A: 91/140 = 65%, 49/140 = 35%, 90/200 = 45%, 110/200 = 55%: the same percentages as the chart.'), '1 mark'))

SC = ['I can identify categorical and numerical variables in bivariate data.', 'I can identify explanatory and response variables.', 'I can construct a two-way frequency table.',
      'I can percentage a two-way frequency table.', 'I can describe an association from a percentaged two-way frequency table.',
      'I can construct a segmented bar chart from a percentaged two-way frequency table.', 'I can describe an association from a percentaged segmented bar chart.']
P.append(close(SC, [('2A', 'Q1–6'), ('2B', 'Q1–12')], ['2A', '2B']))
build('l03', '2A–2B', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('l03-worksheet', '2A-2B worksheet'), ('l03-worksheet-solutions', '2A-2B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
