"""Chapter 2 test (2A-2I) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css).
Source (rule 9: chapter tests = Mathspace topic assessments), copied verbatim:
  Mathspace, General Maths 3&4, Chapter 2 - Investigate associations, 'Chapter 2 - Topic assessment.pdf'
  + 'Chapter 2 - Topic assessment answer key.pdf' (02 Sources\\Textbooks\\Mathspace\\Chapter 2 - Investigate associations).
Answers checked with numpy (Q17: r = -0.981, mean 27.12, s 2.99, z = -1.6). Mathspace lesson codes (2.01 ...) kept per question.
Run: python3 tools/test/ch2/build.py lessons  -> 'Ch2 test.html/.pdf' + 'Ch2 test solutions.html/.pdf'
"""
import sys, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, '../../cfat/ch2/cfat.css')).read() + """
body{font-size:9.6pt;line-height:1.25}
.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:3mm} .qgrid .box{margin-bottom:0}
.mcl div{margin:.6mm 0} .mcl b{display:inline-block;width:5mm}
.mc2{display:grid;grid-template-columns:1fr 1fr;gap:.5mm 3mm}
.ans{color:#c00;display:none;white-space:pre-wrap} .sol .ans{display:block}
.ok{color:#c00;font-weight:bold;display:none} .sol .ok{display:inline}
.part{border-top:1px dashed #000;padding:1mm 0 0;margin-top:1mm} .part .pq b{margin-right:2mm}
.sp{min-height:var(--h)} .mk{color:#555;font-size:8.5pt}
table.t{border-collapse:collapse;margin:1mm 0} table.t td,table.t th{border:1px solid #000;padding:.5mm 2mm;text-align:center}
.cite{font-size:7.5pt;color:#555;margin-top:1mm}
.stem3 td{border:none!important;padding:0 2mm!important;font-family:monospace;font-size:10pt} .stem3 td.s{border-left:1px solid #000!important;border-right:1px solid #000!important}
.secthd{font-weight:bold;border-bottom:2px solid #000;margin:2mm 0;display:flex;justify-content:space-between}
"""
E = html.escape
SRC = 'Mathspace Ch 2 topic assessment'
MC = [  # (lesson, stem, options, correct index)
 ('2.01', 'In a study investigating whether daily screen time affects sleep duration, which variable is the response variable?',
  ['Daily screen time', 'Age of the participant', 'Sleep duration', 'Type of device used'], 2),
 ('2.02', 'A segmented bar chart shows the proportion of students who prefer sport, music, or art, split by gender. The chart is used to investigate whether gender is associated with activity preference. Which of the following is the explanatory variable?',
  ['Gender', 'Proportion', 'Activity preference', 'Number of students'], 0),
 ('2.03', 'A back-to-back stem plot is used to compare the heights (in cm) of players from two basketball teams. The stem 17 row for Team A shows leaves 2, 5, 8 and for Team B shows leaves 0, 3, 6, 9. How many players from Team B have a height in the 170s?',
  ['3', '7', '2', '4'], 3),
 ('2.04', 'Parallel boxplots are used to compare the distribution of weekly wages (in AUD) for full-time and part-time workers. The median for full-time workers is $1200 and for part-time workers is $480. The IQR for full-time workers is $350 and for part-time workers is $180. Which statement is best supported by these statistics?',
  ['Full-time workers typically earn more and have more variable wages in the middle 50%.', 'Part-time workers earn more on average and have more variable wages.',
   'Full-time and part-time workers have similar wage distributions.', 'Part-time workers have a higher maximum wage than full-time workers.'], 0),
 ('2.05', 'A scatterplot is drawn with "number of hours studied" on the horizontal axis and "exam score" on the vertical axis. The points trend upward from left to right. Which description best matches this scatterplot?',
  ['A strong negative linear association', 'A positive linear association', 'No association', 'A non-linear association'], 1),
 ('2.06', "A scatterplot shows the relationship between daily temperature (°C) and the number of visitors to a beach. The association is described as strong and positive. Which value of Pearson's correlation coefficient, r, is most consistent with this description?",
  ['r = −0.92', 'r = 0.05', 'r = −0.45', 'r = 0.88'], 3),
 ('2.07', "The Pearson's correlation coefficient between two variables is r = 0.6. What is the coefficient of determination?",
  ['0.36', '0.6', '0.77', '0.4'], 0),
 ('2.08', 'A study finds a strong positive correlation (r = 0.91) between the number of fire trucks sent to a fire and the amount of damage caused. Which of the following conclusions is most appropriate?',
  ['The correlation proves that fire trucks are ineffective.', 'There is a strong association, but this does not imply that fire trucks cause the damage.',
   'The number of fire trucks is the response variable.', 'Sending more fire trucks causes more damage.'], 1),
]
def T(rows, head=True):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{E(c)}</th>' if (head and i == 0) else f'<td>{E(c)}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
def STEM(rows, kl, kr):
    return ('<table class="stem3">' + ''.join(f'<tr><td style="text-align:right">{E(a)}</td><td class="s">{E(s)}</td><td>{E(b)}</td></tr>' for a, s, b in rows)
            + f'</table><p class="q">{E(kl)} &nbsp;&nbsp;&nbsp; {E(kr)}</p>')
ANS11 = STEM([('Group A', 'Stem', 'Group B'), ('8 4', '1', '0 5 9'), ('7 5 1', '2', '2 6 8'), ('8 5 3 0', '3', '1 6'), ('2', '4', '0 5')], 'Key 5|2 = 25 push-ups', 'Key 2|2 = 22 push-ups')
SA = [  # (lesson, stem html, [(label, text, marks, answer html, space mm)])
 ('2.01', 'A study investigates whether the number of hours of sleep a student gets affects their reaction time (in milliseconds). Identify the explanatory variable and the response variable for this study.',
  [('', '', 1, 'Explanatory variable: Number of hours of sleep. Response variable: Reaction time (in milliseconds).', 12)]),
 ('2.02', 'A survey asked 150 Melbourne residents whether they preferred coffee or tea, and recorded their age group (Under 30, 30-60, Over 60). The results are shown in the two-way frequency table below.'
  + T([['Age group', 'Coffee', 'Tea', 'Total'], ['Under 30', '48', '12', '60'], ['30 − 60', '35', '25', '60'], ['Over 60', '12', '18', '30'], ['Total', '95', '55', '150']])
  + 'Calculate the percentage of people aged Over 60 who prefer coffee. Round your answer to one decimal place.',
  [('', '', 2, '12 ÷ 30 × 100 = 40.0%', 14)]),
 ('2.03', 'The following data shows the number of push-ups completed by students in two fitness groups, Group A and Group B.<br>Group A: 14, 18, 21, 25, 27, 30, 33, 35, 38, 42<br>Group B: 10, 15, 19, 22, 26, 28, 31, 36, 40, 45<br>Construct an ordered back-to-back stem plot for the data. Include a key.',
  [('', '', 2, ANS11, 34)]),
 ('2.05', 'A scatterplot is drawn to investigate the relationship between the number of hours of rainfall per week and the number of visitors to an outdoor market in Brisbane. Describe what a negative association between these two variables would look like on a scatterplot, and explain what it means in context.',
  [('', '', 2, 'A negative association would appear as points trending downward from left to right on the scatterplot. In context, this means that as the number of hours of rainfall per week increases, the number of visitors to the outdoor market tends to decrease.', 20)]),
 ('2.08', 'Across Victorian towns, the number of cafés in a town is strongly positively associated with the number of car accidents in the town each year. Suggest a possible confounding variable that could explain this association.',
  [('', '', 1, 'The population of the town', 10)]),
 ('2.07', 'The average daily temperature, in °C, and the daily electricity usage, in kWh, of a household in Ballarat were recorded on 10 winter days. The CAS output for the correlation between the two variables is shown below.'
  + T([['n', '10'], ['r', '−0.9120'], ['r²', '0.8317']], head=False),
  [('a', 'Identify the explanatory variable.', 1, 'Average daily temperature', 8),
   ('b', 'Describe the strength and direction of the linear association between the two variables.', 1, 'Strong and negative', 8),
   ('c', 'Write the coefficient of determination as a percentage, rounded to one decimal place, and interpret it in the context of this study.', 2,
    '83.2%. About 83.2% of the variation in daily electricity usage can be explained by the variation in average daily temperature.', 16)]),
 ('2.04', 'A group of students recorded their commute time to school, in minutes, and whether they travel by tram or by car. The five-number summaries are shown below.'
  + T([['Transport', 'Minimum', 'Q1', 'Median', 'Q3', 'Maximum'], ['Tram', '12', '26', '34', '41', '58'], ['Car', '8', '16', '22', '29', '47']]),
  [('a', 'Calculate the interquartile range (IQR) of the commute times for each group.', 1, 'Tram 15 minutes, car 13 minutes', 10),
   ('b', 'Do the data support the claim that commute time is associated with the mode of transport? Justify your answer by quoting appropriate statistics.', 2,
    'Yes. The median commute time for students who travel by tram (34 minutes) is higher than for students who travel by car (22 minutes).', 18)]),
 ('2.02', 'In a survey, 200 Victorian adults were asked their preferred news source and their age group. The results are shown in the two-way frequency table below.'
  + T([['News source', '18-34', '35 and over', 'Total'], ['Online', '78', '28', '106'], ['Television', '30', '36', '66'], ['Print', '12', '16', '28'], ['Total', '120', '80', '200']]),
  [('a', 'Identify the explanatory variable.', 1, 'Age group', 7), ('b', 'Calculate the percentage of respondents aged 18 to 34 who prefer online news.', 1, '65%', 9),
   ('c', 'Calculate the percentage of respondents aged 35 and over who prefer television news.', 1, '45%', 9),
   ('d', 'Does the data support the view that preferred news source is associated with age group? Justify your answer by quoting appropriate percentages.', 2,
    'Yes. 65% of respondents aged 18 to 34 prefer online news compared with 35% of respondents aged 35 and over.', 18),
   ('e', 'Calculate the percentage of all respondents who prefer print news.', 1, '14%', 9)]),
 ('2.06', 'The number of hours spent training each week and the time taken to complete a 5 km parkrun, in minutes, were recorded for 10 runners in Melbourne. The data are shown below.'
  + T([['Training (hours)', '2', '3', '4', '5', '5', '6', '7', '8', '9', '10'], ['Time (minutes)', '31.5', '30.2', '29.8', '27.6', '28.9', '26.4', '25.8', '24.1', '24.6', '22.3']], head=False),
  [('a', "Use technology to determine the value of Pearson's correlation coefficient, r, rounded to three decimal places.", 1, 'r = −0.981', 8),
   ('b', 'Describe the strength and direction of the linear association between training time and parkrun time.', 1, 'Strong and negative', 8),
   ('c', 'Use technology to find the mean and standard deviation of the parkrun times, rounded to two decimal places. Hence, calculate the standardised score of the runner with a time of 22.3 minutes, rounded to one decimal place.', 2,
    'Mean 27.12 minutes, standard deviation 2.99 minutes, standardised score −1.6', 16),
   ('d', "A coach claims that these data prove that training more causes faster parkrun times. Comment on the coach's claim.", 2,
    'The claim is not justified. A strong association alone does not prove causation, since other variables, such as age or running experience, may also affect parkrun times.', 18)]),
 ('2.06', "The Pearson's correlation coefficient between the number of hours spent gardening per week and the number of plants in a household is calculated to be r = 0.84.",
  [('a', 'Describe the strength and direction of the linear association between these two variables.', 1, 'The association is strong and positive.', 8),
   ('b', 'Calculate the coefficient of determination and interpret it in the context of this study.', 1,
    'r² = 0.7056. Approximately 70.6% of the variation in the number of plants in a household is explained by the number of hours spent gardening per week.', 14)]),
 ('2.08', 'A study finds that the number of swimming pools in a suburb is strongly positively correlated with the rate of skin cancer in that suburb. A health reporter claims that swimming pools cause skin cancer. Explain why this conclusion may not be valid, and suggest a possible confounding variable.',
  [('', '', 2, 'Correlation does not imply causation. The association may be explained by a confounding variable such as the amount of sunshine in the suburb — sunnier suburbs tend to have more pools and also higher rates of sun exposure, which increases skin cancer risk.', 20)]),
 ('2.03', 'The travel times to work, in minutes, of 11 workers who live in the inner suburbs of Melbourne and 11 workers who live in the outer suburbs of Melbourne are shown in the back-to-back stem plot below.'
  + STEM([('Inner suburbs', 'Stem', 'Outer suburbs'), ('8 5 2', '1', '9'), ('9 6 4 2 1', '2', '7'), ('5 1', '3', '3 6 8'), ('3', '4', '1 4 7'), ('', '5', '2 5'), ('', '6', '1')],
         'Key 4|2 = 24 minutes', 'Key 2|7 = 27 minutes')
  + 'Do the data support the view that travel time to work is associated with where the workers live? Justify your answer by quoting the values of an appropriate statistic.',
  [('', '', 2, 'Yes. The median travel time for workers in the outer suburbs (41 minutes) is higher than for workers in the inner suburbs (24 minutes).', 20)]),
]

def mk(n): return f'{n} mark{"s" if n > 1 else ""}'
def mcbox(n, q):
    les, stem, opts, a = q
    o = ''.join(f'<div><b>{"ABCD"[i]}</b>{E(x)} {"<span class=ok>✓</span>" if i == a else ""}</div>' for i, x in enumerate(opts))
    cls = 'mc2' if max(map(len, opts)) < 25 else 'mcl'
    return f'<div class="box"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><p class="q">{E(stem)}</p><div class="{cls}">{o}</div><div class="cite">{SRC} · {les}</div></div></div>'
def sabox(n, q):
    les, stem, parts = q
    tot = sum(p[2] for p in parts)
    ps = ''
    for lab, txt, m, ans, h in parts:
        head = f'<div class="pq"><b>{lab}</b>{E(txt)} <span class="mk">({mk(m)})</span></div>' if lab else ''
        ps += f'<div class="part">{head}<div class="sp" style="--h:{h}mm"><div class="ans">{ans}</div></div></div>'
    return f'<div class="box"><div class="hd">Question {n}<span>{mk(tot)}</span></div><div class="bd"><p class="q">{stem}</p>{ps}<div class="cite">{SRC} · {les}</div></div></div>'

def page(sol):
    tot = len(MC) + sum(p[2] for q in SA for p in q[2])
    out = [f'<div class="title"><div class="code">Ch 2<br>test</div><h1>Investigating associations between two variables<div style="font-size:10pt;font-weight:normal;margin-top:1mm">2A–2I · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + mcbox(i + 2, MC[i + 1]) + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch2 test' + (' solutions' if sol else '')
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{t}</title><style>{CSS}</style>'
            f'<script src="a4view.js"></script><script src="paged.polyfill.min.js"></script></head><body class="{"sol" if sol else ""}">\n' + '\n'.join(out) + '\n</body></html>'), t

if __name__ == '__main__':
    od = sys.argv[1]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for sol in (False, True):
            h, t = page(sol); f = os.path.join(od, t + '.html'); open(f, 'w').write(h)
            pg = b.new_page(); pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(2500)
            pg.pdf(path=os.path.join(od, t + '.pdf'), prefer_css_page_size=True, print_background=True); pg.close(); print(t)
        b.close()
