"""Lesson l08 (2I) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py). Same order as tools/deck/l08/build.py.
The l08 card has no APK, no Examples / You trys and no exits (Rocco, 15 Nov: Q2), so the worksheet is: learning intentions →
'Which graph?' table to complete (Cambridge U3&4 2I p. 155 guideline table, Graph column blank; red on the solutions copy) → skills checklist + coursework.
Output: lessons/2I worksheet(.html/.pdf) + lessons/2I worksheet solutions(.html/.pdf).   Run: python3 tools/deck/l08/worksheet.py"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2

def _card(o, i):
    if isinstance(o, dict):
        if o.get('id') == i: return o['card']
        for v in o.values():
            r = _card(v, i)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = _card(v, i)
            if r: return r
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u3-l08')
SC = [x for g in CARD['successCriteria'] for x in g['items']]

P = [title('2I', 'Which graph?')]
P.append(lis(['To be able to choose an appropriate graph to display the association between two variables.']))
P.append(sect('2I Which graph?', 'Complete the table'))
rows = [['Response variable', 'Explanatory variable', 'Graph'],
        ['Categorical', 'Categorical', a('Segmented bar chart')],
        ['Numerical', 'Categorical', a('Parallel boxplots, parallel dot plots')],
        ['Numerical', 'Categorical (two categories only)', a('Back-to-back stem plot, parallel dot plots or parallel boxplots')],
        ['Numerical', 'Numerical', a('Scatterplot')]]
P.append(box('Which graph?', table(rows, cls='t fill', style='width:100%') ))
P.append(close(SC, [('2I', 'Q1–3')], ['2I']))
if WB: P.append(practice(['2I']))  # workbook edition only: practice sections (Insight + Cambridge skill sheets) flow on after the exits
build('l08', '2I', 'AoS 1 · Data analysis', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (() if WB else (('l08-worksheet', '2I worksheet'), ('l08-worksheet-solutions', '2I worksheet solutions'))):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
