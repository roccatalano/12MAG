r"""12MAG S11 (2I Which graph?) in the z10 slide standard.
Converted 21 Nov 2026 from the old deck tools/deck/l08/build.py (planner card gm12-u3-l08; same content, same order).
python3 tools/deck/z10/s11_build.py  ->  lessons/S11-slides.html
Sources: Cambridge U3&4 2I p. 155 (guideline table; own words; flowchart drawn for 12MAG). Examples of variable pairs: Exercise 2I Q1.
Learning intention / success criteria written for 12MAG (the textbook prints none for 2I). No APK and no exit task on the planner card (Rocco, 15 Nov).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.assoc import *
lesson('2I Which graph?')

title_slide('Which graph?', ['2I Which graph? (pp. 155–156)'])
LI = ['To choose an appropriate graph to display the association between two variables.']
SC = ['I can classify each variable as categorical or numerical.', 'I can identify the explanatory and response variables.', 'I can choose an appropriate graph for two variables from their types.']
SEQ = ['Key ideas', 'Before you draw: two questions', 'Which graph?', 'Summary table', 'Check-in and coursework']
overview('2I', LI, SC, SEQ, 'Learning intention and success criteria written for 12MAG (the textbook prints none for 2I)')

keyslide('2I',
    [('Categorical variable', 'data that are labels or groups (e.g. sex, school type, yes/no)'),
     ('Numerical variable', 'data that are counts or measurements (e.g. height, income)'),
     ('Explanatory variable (EV)', 'the variable we expect to explain or predict the RV'),
     ('Response variable (RV)', 'the variable that responds: the one we want to predict')],
    [('Two categorical', 'segmented bar chart (from a percentaged two-way table)'),
     ('Numerical RV, categorical EV', 'parallel boxplots · parallel dot plots; two categories: back-to-back stem plot too'),
     ('Two numerical', 'scatterplot (EV on the horizontal axis)')],
    CG + ', 2I p. 155')

S.append(nl_slide('Before you draw: two questions',
    'Ask first: <b>1</b> Is each variable <b>categorical</b> or <b>numerical</b>? <b>2</b> Which is the <b>RV</b> and which is the <b>EV</b>? <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr 1fr">' + st('<b>Both categorical</b><br>vegetarian (yes, no) and sex (male, female)', cls='stp zcard')
    + st('<b>One of each</b><br>hours at the beach and state of residence', cls='stp zcard') + st('<b>Both numerical</b><br>test mark and hours spent studying', cls='stp zcard') + '</div>'
    + st('The type of variable, not the topic, decides the graph.', cls='stp ztest'),
    CG + ', 2I p. 155 (examples from Exercise 2I Q1 variable pairs)'))
FC = ('<div class="zfc"><div class="znd zq2">What types are the RV and EV?</div><div class="zfr">'
      '<div class="zbr">' + st('both categorical', cls='zlab') + st('Segmented bar chart', cls='znd zgr') + st('from a percentaged two-way table', cls='zlab') + '</div>'
      '<div class="zbr">' + st('RV numerical · EV categorical', cls='zlab') + st('How many categories?', cls='znd zq2')
      + st('two: back-to-back stem plot, parallel dot plots or parallel boxplots', cls='znd zgr') + st('three or more: parallel boxplots, parallel dot plots', cls='znd zgr') + '</div>'
      '<div class="zbr">' + st('both numerical', cls='zlab') + st('Scatterplot', cls='znd zgr') + st('EV on the horizontal axis', cls='zlab') + '</div></div></div>')
S.append(nl_slide('Which graph?',
    'Match the graph to the types of variables. They are guidelines only: sometimes more than one graph is suitable. <span class="hint">Click to build the flowchart.</span>',
    FC + st('A histogram, a single dot plot or a single stem plot shows ONE variable: never the answer for an association.', cls='stp ztest'),
    CG + ', 2I p. 155 (table redrawn as a flowchart)'))
TB = ('<table class="ztab zbig"><tr><th>Response variable</th><th>Explanatory variable</th><th>Graph</th></tr>'
      '<tr data-r="0"><td>Categorical</td><td>Categorical</td><td>Segmented bar chart</td></tr>'
      '<tr data-r="1"><td>Numerical</td><td>Categorical</td><td>Parallel boxplots, parallel dot plots</td></tr>'
      '<tr data-r="2"><td>Numerical</td><td>Categorical (two categories only)</td><td>Back-to-back stem plot, parallel dot plots or parallel boxplots</td></tr>'
      '<tr data-r="3"><td>Numerical</td><td>Numerical</td><td>Scatterplot</td></tr></table>')
S.append(nl_slide('Summary: type of variables → graph',
    'Chapter 2 in one table: every display from 2A–2F fits one row.',
    '<div class="zc">' + TB + '</div>' + st('Exam tip: back-to-back stem plots need exactly two categories (e.g. sex, licence type).', cls='stp ztest'),
    CG + ', 2I p. 155'))

checkin(SC)
coursework('2I', 'Coursework · Exercise 2I', [('Cambridge Exercise 2I', 'Q1–3'), ('Practice booklet', '2I section (Insight)')],
           'Exercise 2I: Which graph?', CG + ', Exercise 2I; Chapter 2 workbook practice questions')

LESSON_CSS = r'''
.slide.z .st.zcard{align-self:start}
.slide.z .st.zcard{border:2.5px solid #000;padding:12px 14px;box-shadow:4px 4px 0 #bbb;font-size:22px;color:#000;margin:0!important}
.slide.z .st.ztest{font-size:19px;color:#000;margin-top:16px!important}
.zfc{display:flex;flex-direction:column;align-items:center;gap:12px;margin-top:8px}
.zfc .zfr{display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:18px;width:100%}
.zfc .zbr{display:flex;flex-direction:column;align-items:center;gap:8px}
.zfc .znd{border:2.5px solid #000;padding:8px 14px;font-weight:bold;text-align:center;font-size:19px;box-shadow:3px 3px 0 #bbb;margin:0!important}
.zfc .zq2{background:#fff2a8}.zfc .zgr{background:#d7f0d7}
.zfc .zlab{font-size:17px;color:#333;text-align:center;margin:0!important}
.ztab.zbig{font-size:20px;margin:10px auto}.ztab.zbig td,.ztab.zbig th{padding:8px 14px}
'''
build('S11-slides.html', '12MAG S11 · Which graph? · Slides', css=LESSON_CSS)
