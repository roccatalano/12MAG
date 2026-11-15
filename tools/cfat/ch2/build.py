"""CFAT 1.2.1 (Cambridge 2A-2B) and CFAT 1.2.2 (Cambridge 2C-2D), Word layout per the 12mag-cfat-word skill.

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no VCAA reprints). Rebuilt from scratch 15 Nov 2026
(queue Ch2 #2, Rocco's answer to Q1). Wording copied from Edrolo; stems shortened only where the skill allows
(all information kept). Answers from the Edrolo answer pages (PDF pp. 669-673).
Figures cropped by crop.py from the Edrolo PDF (pp. 119-121, 132-135, 147).

CFAT 1.2.1 (17 marks): Edrolo 2C Q1, 2A Q1a, 2A Q1b, 2A Q5, 2A Q7 (MC); 2C Q2a-d, 2A Q2, 2A Q8, 2A Q9a-b.
CFAT 1.2.2 (16 marks): Edrolo 2B Q3a, 2C Q10, 2B Q3b, 2B Q5, 2B Q7a (MC); 2B Q1, 2B Q8a-b, 2C Q11a-b.

Run: python3 build.py <outdir>  -> CFAT 1.2.x (2A-2B).docx + solutions .docx
"""
import sys, os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')
RED = RGBColor(0xC0, 0, 0)
GREY = RGBColor(0x77, 0x77, 0x77)

# ---------------- content ----------------
CFATS = [
 dict(id='CFAT 1.2.1', subs='2A-2B', title='Response and explanatory variables · associations between two categorical variables',
  layout=[([0,2],[1]),('full',3),('full',4)],
  mc=[
   dict(src='Edrolo 2C Q1', stem='Fill in the blanks for the following statement.\nThe ______ variable is used to predict the changes observed in the ______ variable. When representing the variables on a scatterplot, the response variable is positioned on the ______ axis and the explanatory variable is positioned on the ______ axis.',
        opts=['response, explanatory, horizontal, vertical','response, explanatory, vertical, horizontal','explanatory, response, horizontal, vertical','explanatory, response, vertical, horizontal'], ans=3),
   dict(src='Edrolo 2A Q1a', stem='A group of people were surveyed on commute time from home to school. Their responses were classified as ‘less than an hour’ or ‘an hour or more’. They were also grouped by the location of their home as either ‘urban’ or ‘rural’. The results were displayed in the two-way percentage frequency table.\nWhat percentage of respondents living in an ‘urban’ location are ‘less than an hour’ away from their school?',
        fig='2A_Q1', w=3.6, opts=['3%','38%','62%','97%'], ans=3),
   dict(src='Edrolo 2A Q1b', stem='Use the table in Question 2.\nWhat percentage of respondents living in a ‘rural’ location are ‘less than an hour’ away from their school?',
        opts=['3%','38%','62%','97%'], ans=2),
   dict(src='Edrolo 2A Q5', stem='A scientific experiment was conducted to determine if there is a relationship between light intensity (dark, bright) and respiration rate (low, medium, high) for a small sample of spinach leaves. The results were displayed in a percentage segmented bar chart.\nWhich of the following statements is correct?',
        fig='2A_Q5', w=3.4, opts=['25% of spinach leaves subjected to a bright light intensity had a low respiration rate.','55% of spinach leaves subjected to a dark light intensity had a low respiration rate.','35% of spinach leaves subjected to a dark light intensity had a medium respiration rate.','55% of spinach leaves subjected to a bright light intensity had a high respiration rate.'], ans=3),
   dict(src='Edrolo 2A Q7', full=True, stem='Each morning at the Edrolo office, a team member volunteers to do a coffee run. Everyone is able to choose either ‘cappuccino’, ‘flat white’ or ‘latte’. Their coffee preference has been recorded alongside their employment duration (less than three years, three years or more) in a two-way percentage frequency table.\nThe data displayed supports the contention that there is no obvious association between coffee preference and employment duration because',
        fig='2A_Q7', w=6.0, opts=['the coffee preferences between employment duration differ by a significant amount.','23.7% of team members who have been working for less than 3 years prefer a flat white.','63.2% of team members who have been working for less than 3 years prefer a latte and 64.7% of those who have been working for 3 or more years prefer a latte.','63.2% of team members who have been working for less than 3 years prefer a latte and 11.7% of those who have been working for 3 or more years prefer a cappuccino.'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 2C Q2', stem='Identify the response variable, RV, and the explanatory variable, EV, in each of the following questions.',
        parts=[('a.','Can the number of umbrellas sold on a day be predicted from the amount of rainfall?',1,'RV: number of umbrellas sold   EV: amount of rainfall'),
               ('b.','Can the age of a second-hand TV predict its selling price?',1,'RV: selling price   EV: age'),
               ('c.','Does the price of a watermelon depend on the season?',1,'RV: price   EV: season'),
               ('d.','Do years of experience affect an individual’s salary?',1,'RV: salary   EV: years of experience')]),
   dict(src='Edrolo 2A Q2', stem='A survey was conducted on people’s preferences for reusable cup brands (frank green, KeepCup, other) and their coffee consumption (often, rarely). The results were displayed in a two-way percentage frequency table, but some values are missing.',
        fig='2A_Q2', w=4.6,
        parts=[('a.','Fill in the table with the missing values.',2,'KeepCup / often = 40%;  other / rarely = 72%  (1 mark each)'),
               ('b.','What percentage of people who often drink coffee prefer to use a KeepCup?',1,'40%')]),
   dict(src='Edrolo 2A Q8', stem='A study was conducted to see if individuals had a cryptocurrency investment (yes, no). Participants also had their age (under 45, 45 and over) recorded. The results have been displayed in a percentage segmented bar chart.',
        fig='2A_Q8', w=3.6,
        parts=[('','Is there an association between age and cryptocurrency investment? Ensure to quote appropriate percentages.',2,'Yes, there is an association between cryptocurrency investment and age (1). The percentage of those with a cryptocurrency investment increases with age, from 15% of participants aged under 45 to 75% of participants aged 45 and over (1).')]),
   dict(src='Edrolo 2A Q9', stem='Mark wants to see if there is an association between the number of hours studied (0 to 9 hours, 10 to 19 hours, 20 to 29 hours, 30 or more hours) for an assessment and the test score (low, medium, high) that his students get.',
        parts=[('a.','Which variable is most likely to be plotted on the horizontal axis of a percentage segmented bar chart?',1,'hours studied'),
               ('b.','Mark fills out a table with the data he gathered from the test. However, Mark spilled his coffee on his paper on his drive to work, leaving a couple of stains. Fill out the rest of the table.',2,'0 to 9 hours: low = 80%;  10 to 19 hours: medium = 60%;  20 to 29 hours: medium = 50%  (2 marks; −1 per error)','2A_Q9',9.0)]),
  ]),
 dict(id='CFAT 1.2.2', subs='2C-2D', title='Numerical vs categorical variables · scatterplots',
  layout=[([0],[1]),('full',2),('full',3),('full',4)],
  mc=[
   dict(src='Edrolo 2B Q3a', stem='The number of minutes spent in the shower by each participant at band camp was recorded correct to the nearest 30 seconds. The participants were then categorised by age into two groups: ‘11–14 years’ and ‘15–18 years’.\nIn this circumstance, age is classified as what kind of variable?',
        opts=['Discrete numerical variable','Nominal categorical variable','Continuous numerical variable','Ordinal categorical variable'], ans=3),
   dict(src='Edrolo 2C Q10', stem='The relationship in the scatterplot shown can be described as',
        fig='2C_Q10', w=4.0, opts=['weak, positive and linear.','strong, positive and linear.','weak, negative and linear.','strong, negative and linear.'], ans=1),
   dict(src='Edrolo 2B Q3b', stem='The results from Question 1 are displayed in the following dot plots.\nWhich of these statements is not true?',
        fig='2B_Q3', w=5.5, opts=['The median number of minutes spent in the shower increases as age increases from 11–14 years to 15–18 years.','The modal number of minutes spent in the shower for 11–14 year olds is 6 minutes.','The middle 50% of data for 15–18 year olds is less variable than the middle 50% of data for 11–14 year olds.','The number of minutes spent in the shower is more variable for 15–18 year olds than for 11–14 year olds.'], ans=3),
   dict(src='Edrolo 2B Q5', stem='A Unit 3&4 General Mathematics teacher monitored the results of her class in the Edrolo AOS tests. At the end of the week, the teacher was expected to present the data to the Head of Mathematics. In her report, she displayed the data using parallel boxplots.\nWhich of the following statements relating to this data is not correct?',
        fig='2B_Q5', w=3.6, opts=['The median chapter 2 result was higher than the median chapter 1 result.','The lowest 25% of results in the chapter 2 test was better than the lowest 25% of results in the chapter 1 test.','The IQR for the chapter 1 test was greater than the IQR for the chapter 2 test.','The range for the chapter 1 test was the same as the range for the chapter 2 test.'], ans=2),
   dict(src='Edrolo 2B Q7a', full=True, stem='The average pay rate ($/hour) of workers from 50 countries were tracked in the years ‘1980’, ‘1990’ and ‘2000’. The results are displayed in the following parallel boxplots.\nWhich of the following statements is not true?',
        fig='2B_Q7', w=8.0, opts=['In 1980, over 75% of countries had an average pay rate lower than the median average pay rate in 1990.','In 1990, 75% of the countries had an average pay rate lower than the median average pay rate in 2000.','In 1990, there was more variation in average pay rate in the middle 50% of countries than the middle 50% of countries in 1980.','In 2000, the top 50% of countries had an average pay rate higher than any of the countries in 1980.'], ans=1),
  ],
  sa=[
   dict(src='Edrolo 2B Q1', stem='A popular local bakery has recently reduced the size of its workforce, and as such needs to reduce their menu. They are deciding between removing either ‘muffins’ or ‘scones’ from their selection based on the number of sales for each. They have recorded the number of sales each day for the month of June in the back-to-back stem plot.',
        fig='2B_Q1', w=6.5,
        parts=[('','Use the stem plot to fill in the gaps in the following sentences.\n\nThe median number of ‘scones’ sold per day is __________ while the median number of ‘muffins’ sold per day is __________. In order to maximise revenue, the bakery should remove __________ from their selection.',3,'29;  38;  scones  (1 mark each)')]),
   dict(src='Edrolo 2B Q8', stem='Charlotte is a long distance runner. Her coach formulated an intense training program to prepare her for a big competition next year. In order to see if the training program was effective, Charlotte tracked the time it took her to run 10 km (correct to the nearest minute) before and after she completed the program. Her results are shown in the following parallel dot plots.',
        fig='2B_Q8', w=4.8,
        parts=[('a.','Did the training program improve Charlotte’s running time? Write a brief explanation, referencing centre.',2,'Yes (1). Her median running time decreased from 48.5 minutes before the program to 43 minutes after it (1).'),
               ('b.','Did the training program improve Charlotte’s consistency? Write a brief explanation, referencing spread.',2,'Yes (1). The range decreased from 9 minutes to 6 minutes and the IQR decreased from 4 minutes to 1.5 minutes (1).')]),
   dict(src='Edrolo 2C Q11', stem='For each of the following scatterplots, describe the association between the variables in terms of strength, direction, form and potential outliers.',
        parts=[('a.','',2,'Strong, positive and linear with no visible outliers  (2 marks; −1 per missing/wrong feature, max −2)','2C_Q11a',3.8),
               ('b.','',2,'Strong, negative and linear with one visible outlier at (30, 60)  (2 marks)','2C_Q11b',3.8)]),
  ]),
]

# ---------------- docx helpers ----------------
def shade(cell, hexcol):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), hexcol); tcPr.append(s)

def fix(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(int(sum(widths) * 567))); w.set(qn('w:type'), 'dxa'); tblPr.append(w)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = table._tbl.tblGrid
    for gc, wd in zip(grid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(wd * 567)))
    for row in table.rows:
        for c, wd in zip(row.cells, widths): c.width = Cm(wd)

def cant_split(row):
    trPr = row._tr.get_or_add_trPr(); e = OxmlElement('w:cantSplit'); trPr.append(e)

def borders(table):
    tbl = table._tbl; tblPr = tbl.tblPr; b = OxmlElement('w:tblBorders')
    for side in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'6'); e.set(qn('w:color'),'000000'); b.append(e)
    tblPr.append(b)

def para(cell, text='', bold=False, size=10, color=None, italic=False, first=False, align=None, space=2):
    p = cell.paragraphs[0] if first else cell.add_paragraph()
    p.paragraph_format.space_after = Pt(space); p.paragraph_format.space_before = Pt(0)
    if align: p.alignment = align
    if text:
        r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p

def heading(cell, n, src, marks=None, first=True):
    p = para(cell, first=first)
    r = p.add_run(f'Question {n}' + (f' ({marks} mark{"s" if marks>1 else ""})' if marks else '')); r.bold = True; r.font.size = Pt(10.5)
    r = p.add_run(f'   {src}'); r.font.size = Pt(7.5); r.font.color.rgb = GREY

def pic(cell, key, w):
    p = para(cell, align=WD_ALIGN_PARAGRAPH.CENTER); p.add_run().add_picture(FIG(key), width=Cm(w))

def mc_cell(cell, n, q, sol, cw, first=True):
    heading(cell, n, q['src'], first=first)
    for line in q['stem'].split('\n'): para(cell, line, bold=True, size=9.5)
    target = cell
    if q.get('fig'):
        fw = q['w']; nt = cell.add_table(rows=1, cols=2); fix(nt, [cw - fw - 0.4, fw + 0.2])
        target = nt.rows[0].cells[0]; fc = nt.rows[0].cells[1]
        p = fc.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.add_run().add_picture(FIG(q['fig']), width=Cm(fw))
    for i, o in enumerate(q['opts']):
        p = para(target, space=1, first=(i == 0 and target is not cell)); p.paragraph_format.left_indent = Cm(0.5); p.paragraph_format.first_line_indent = Cm(-0.5)
        right = sol and i == q['ans']
        r = p.add_run(f'{"abcd"[i]}.  {o}' + ('  ✓' if right else '')); r.font.size = Pt(9.5)
        if right: r.font.color.rgb = RED; r.bold = True
    p = para(cell, '', space=0); p.paragraph_format.line_spacing = Pt(4)

def build(c, sol, outdir):
    d = Document(); s = d.sections[0]
    s.page_height, s.page_width = Cm(29.7), Cm(21.0)
    s.left_margin = s.right_margin = Cm(1.3); s.top_margin = s.bottom_margin = Cm(1.1)
    st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10); st.paragraph_format.space_after = Pt(0); st.paragraph_format.line_spacing = 1.0
    W = 18.4
    total = len(c['mc']) + sum(p[2] for q in c['sa'] for p in q['parts'])
    # header
    t = d.add_table(rows=1, cols=3); borders(t); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    a, b, cc = t.rows[0].cells
    fix(t, [9.4, 6.0, 3.0])
    p = para(a, f"{c['id']} ({c['subs'].replace('-', '–')})" + ('  SOLUTIONS' if sol else ''), bold=True, size=13, first=True, color=RED if sol else None)
    para(a, c['title'], size=8.5, color=GREY)
    para(a, 'About 20 min · individual · CAS and bound reference allowed', size=8, color=GREY)
    para(b, 'Name:', bold=True, first=True); para(cc, 'Score', bold=True, first=True)
    para(cc, f'      / {total}', size=12)
    d.add_paragraph().paragraph_format.space_after = Pt(0)
    # MC grid
    p = d.add_paragraph(); r = p.add_run('Section A · Multiple choice (1 mark each) — circle one answer'); r.bold = True; r.font.size = Pt(10.5)
    p.paragraph_format.space_after = Pt(2)
    lay = c['layout']
    t = d.add_table(rows=len(lay), cols=2); borders(t); fix(t, [W/2, W/2])
    for ri, row_l in enumerate(lay):
        row = t.rows[ri]; cant_split(row)
        if row_l[0] == 'full':
            m = row.cells[0].merge(row.cells[1]); mc_cell(m, row_l[1] + 1, c['mc'][row_l[1]], sol, W - 0.3)
        else:
            for j in range(2):
                for k, qi in enumerate(row_l[j]):
                    cell = row.cells[j]
                    if k: para(cell, '', space=4)
                    mc_cell(cell, qi + 1, c['mc'][qi], sol, W/2 - 0.3, first=(k == 0))
    n = len(c['mc']) + 1
    # SA
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(2)
    r = p.add_run('Section B · Short answer — show working where needed'); r.bold = True; r.font.size = Pt(10.5)
    p.paragraph_format.page_break_before = True
    for q in c['sa']:
        marks = sum(x[2] for x in q['parts'])
        t = d.add_table(rows=len(q['parts']), cols=2); borders(t); fix(t, [8.2, W-8.2])
        left = t.cell(0, 0)
        if len(q['parts']) > 1: left = left.merge(t.cell(len(q['parts']) - 1, 0))
        left.width = Cm(8.2)
        heading(left, n, q['src'], marks)
        for line in q['stem'].split('\n'): para(left, line, size=9.5)
        if q.get('fig'): pic(left, q['fig'], min(q['w'], 7.6))
        for i, part in enumerate(q['parts']):
            row = t.rows[i]; cant_split(row); cell = row.cells[1]; cell.width = Cm(W - 8.2)
            lab, txt, mk, ans = part[:4]
            p = para(cell, first=True)
            r = p.add_run(f'{lab} ' if lab else ''); r.bold = True; r.font.size = Pt(9.5)
            for k2, line in enumerate(txt.split('\n')):
                if k2: p = para(cell)
                r = p.add_run(line); r.font.size = Pt(9.5)
            r = p.add_run(f'  ({mk} mark{"s" if mk > 1 else ""})'); r.font.size = Pt(8); r.font.color.rgb = GREY
            if len(part) > 4: pic(cell, part[4], part[5])
            if sol: para(cell, ans, size=9.5, color=RED, bold=True)
            else:
                for _ in range(mk): para(cell, '')
        d.add_paragraph().paragraph_format.space_after = Pt(0)
        n += 1
    name = f"{c['id']} ({c['subs']})" + (' solutions' if sol else '') + '.docx'
    d.save(os.path.join(outdir, name)); return name

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out, exist_ok=True)
    for c in CFATS:
        for sol in (False, True): print(build(c, sol, out))
