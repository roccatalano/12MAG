r"""12MAG S<n> (<subchapters>) slides: STARTER. Copy to s<n>_build.py, fill in, run:
    python3 tools/deck/z10/s<n>_build.py  ->  lessons/S<n>-slides.html
Rules: tools/deck/z10/HOWTO.md (the slide standard). Never write questions: copy verbatim, cite in the footer.
Sources (keep the real ones here): planner card gm12-u3-s<n>; Cambridge U3&4 Examples ...; Edrolo ... You trys; exits ...
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
# from lib.num import *        # numerical build-ups: histograms bar by bar, dot plots, stem leaves, SOCS template
# from lib.cat import *        # categorical: bar / segmented bar charts, frequency tables, reports, bar -> 100% morph
# from lib.boxplot import *    # boxplots, fences, outliers
# from lib.normal import *     # normal curve, 68-95-99.7 shading, z-scores
lesson('1X Subchapter title')                                   # right-hand text in every title bar

# ---- title, then learning intentions | success criteria | lesson sequence
title_slide('Formal topic title', ['1X Subchapter title (pp. 1–9)', '1Y Next subchapter (pp. 10–19)'])
LI = ['To be able to ...']                                       # Cambridge learning intentions
SC = ['I can ...']                                               # one per worked example
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Topic · Example 1', 'Exit task', 'Check-in and coursework']
overview('1X', LI, SC, SEQ, CG + ', 1X Learning intentions (p. 1); success criteria: one per worked example')

# ---- APK (Cambridge U1&2 skills checklist / Edrolo U1&2 VCAA questions)
S.append(qslide('apk', '1 of 1', 'Year 11 skills: ...', 'Cambridge U1&amp;2 · 2A #1',
    'Question context, verbatim.', 'Key idea text',
    [], None, CG12 + ', Chapter 2 skills checklist 2A #1. Working by teacher.',
    parts=[('a', 'Part a, verbatim.', ['step 1', 'step 2'], 'answer a'),
           ('b', 'Part b, verbatim.', ['step 1'], 'answer b')]))

# ---- New learning, then Example / You try pairs
S.append(nl_slide('Idea title', 'One-line lead. <span class="hint">Click to reveal.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col">' + st('<b>1</b> first idea', cls='stp') + '</div>'
    '<div class="col">' + stem('nl1', [('1', '2 5 8'), ('2', '0 3')], 'Key: 1 | 2 = 12', build=True) + '</div></div>',
    CG + ', 1X p. 2'))
S.append(qslide('ex', 1, 'Example title', 'Cambridge · Example 1',
    'Question, verbatim.', KI_MED,
    ['one idea per click', ('a step that animates the figure', 'lm:e1:2')],
    '<b>answer with units</b>', CG + ', 1X Example 1 (p. 3)',
    fig=stem('e1', [('1', '2 5 8'), ('2', '0 3')], 'Key: 1 | 2 = 12')))
S.append(qslide('yt', 1, 'Example title', 'Edrolo 1X WE1',
    'Question, verbatim.', KI_MED, ['step'], '<b>answer</b>', ED + ', 1X Worked example 1 (p. 5). Working by teacher.'))

# ---- exit task (past-design VCAA, via Edrolo U3&4); MC: OPTDIST + opts + key
OPTDIST['1'] = [10, 70, 10, 5, 5]                                # % choosing A–E, from the examiner report
S.append(qslide('exit', '1', 'Exit task', 'VCAA 2019 Exam 1 Q1',
    'Question, verbatim.', 'Key idea', [], 'why B', ED + ', 1X Q10 (VCAA 2019 Exam 1 Q1)',
    vcaa=70, opts=[('A', '...'), ('B', '...'), ('C', '...'), ('D', '...'), ('E', '...')], key='B'))

# ---- check-in, coursework (example page heading = this lesson's own exercise)
checkin(SC)
coursework('1X', 'Coursework · Exercise 1X', [('Cambridge Exercise 1X', 'Q1–10'), ('Practice booklet', '1X section')],
           'Exercise 1X: Subchapter title', CG + ', Exercise 1X')

LESSON_CSS = r'''
'''
LESSON_JS = r'''
'''
build('SX-slides.html', '12MAG SX · Formal topic title · Slides', css=LESSON_CSS, js=LESSON_JS)
