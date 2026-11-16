"""Lesson gm12-u4-11d (11D) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4H #19 (p. 293; matrices from 4H #18), solution worked for 12MAG.
Example 8 = Cambridge U3&4 pp. 570-571 (diagram cropped, fig/ex8.png). You try = Edrolo U3&4 7I WE3 (pp. 506-507).
Exit = VCAA 2017 Further E1 Matrices Q7 (Edrolo U3&4 7I Q15).
Output: lessons/11D worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-11d/worksheet.py"""
import os, sys, json, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:6mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def LT(m, top, side): return f'<span style="display:inline-flex;flex-direction:column;align-items:center"><i style="font-size:9pt">{top}</i>{m}</span><i style="font-size:9pt">{side}</i>'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-11d')
S_ = lambda n: f'<span style="white-space:nowrap"><i>S</i><sub>{n}</sub></span>'
def IMG(f, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{mm}mm;max-width:100%;display:block;margin:1mm auto">'
P = [title('11D', 'Transition matrices: using the rule S<sub>n+1</sub> = TS<sub>n</sub> + B')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skill'))
P.append(box('Question 1', q('Consider the following matrices: one defining the initial populations in Geelong and Ballarat and the other, a transition matrix defining the proportion of the population moving between the two cities each year. Assume Geelong is listed first.')
  + row(S_(0) + ' = ' + M([['250 000'], ['110 000']]), '<i>T</i> = ' + M([[0.9, 0.15], [0.1, 0.85]]))
  + q('In the example of Geelong and Ballarat above, how many people are expected to be in Geelong in the long term?')
  + space(16, '<i>T</i><sup>50</sup>' + S_(0) + ' = <i>T</i><sup>51</sup>' + S_(0) + ' = (216 000, 144 000): about 216 000 people in Geelong')))

P.append(sect('11D Transition matrices – using the rule Sₙ₊₁ = TSₙ + B', 'Example, then you try'))
EX = (Q('A rental starts with 90 cars, 50 located at Bendigo and 40 located at Colac.<br>Cars are usually rented and returned in the same town. However, a small percentage of cars rented in Bendigo are returned in Colac and vice versa. The transition diagram opposite gives these percentages.')
  + IMG('ex8.png', 50)
  + Q('To increase the number of cars, two extra cars are added to the rental fleet at each location each week. The recurrence relation that can be used to model this situation is:')
  + row(S_(0) + ' = ' + M([[50], [40]]) + ', ' + S_('<i>n</i>+1') + ' = <i>T</i>' + S_('<i>n</i>') + ' + <i>B</i>', 'where <i>T</i> = ' + M([[0.8, 0.1], [0.2, 0.9]]), 'and <i>B</i> = ' + M([[2], [2]]))
  + Q('Determine the number of cars at Bendigo and Colac after:')
  + parts([('a', '1 week', S_(1) + ' = <i>T</i>' + S_(0) + ' + <i>B</i> = (44, 46) + (2, 2) = (46, 48): 46 cars in Bendigo and 48 in Colac', 18),
           ('b', '2 weeks.', S_(2) + ' = <i>T</i>' + S_(1) + ' + <i>B</i> = (41.6, 52.4) + (2, 2) = (43.6, 54.4): 43.6 cars in Bendigo and 54.4 in Colac', 18)]))
T3 = [['0.73', '0.07', '0.11', '0'], ['0.10', '0.71', '0.04', '0'], ['0.06', '0.08', '0.72', '0'], ['0.11', '0.14', '0.13', '1']]
YT = (Q('Eddortsford High School runs an optional extra-curricular arts program. Each year, students can choose from Music (<i>M</i>), Drama (<i>D</i>), Visual Arts (<i>V</i>), or to opt out (<i>O</i>) of the program. The movement of students from one year to the next is summarised in the transition matrix, <i>T</i>.')
  + row('<i>T</i> = ' + LT(M(T3, cl=list('MDVO'), rl=list('MDVO'), side=True), 'this year', 'next year'))
  + Q('The matrix ' + S_(0) + ' represents the number of students enrolled in each course at the beginning of 2023.') + row(S_(0) + ' = ' + M([[73], [36], [52], [0]], rl=list('MDVO'), side=True))
  + Q('As the program expands, 30 new students are added to the program each year. 13 of these students are expected to be added to the music course, 6 to the drama course and 11 to the visual arts course.')
  + parts([('a', 'Construct matrix <i>B</i> to represent the predicted new enrolments and their preferences.', '<i>B</i> = ' + M([[13], [6], [11], [0]], rl=list('MDVO'), side=True), 20),
           ('b', 'How many students are expected to be enrolled in the music course at the beginning of 2025? Round to the nearest whole number.', S_(1) + ' = <i>T</i>' + S_(0) + ' + <i>B</i> = (74.53, 40.94, 55.70, 19.83); ' + S_(2) + ' = <i>T</i>' + S_(1) + ' + <i>B</i> = (76.3997, 44.7484, 58.8510, 41.0009): 76 students', 22)]))
P.append(exyt('Example 8 · Sₙ₊₁ = TSₙ + B', EX, 'You try 1', YT))

P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 1 Q7', q('At a fish farm:<br>• young fish (<i>Y</i>) may eventually grow into juveniles (<i>J</i>) or they may die (<i>D</i>)<br>• juveniles (<i>J</i>) may eventually grow into adults (<i>A</i>) or they may die (<i>D</i>)<br>• adults (<i>A</i>) eventually die (<i>D</i>).<br>The initial state of this population, <i>F</i><sub>0</sub>, is shown below.')
  + row('<i>F</i><sub>0</sub> = ' + M([['50 000'], ['10 000'], ['7 000'], ['0']], rl=list('YJAD'), side=True))
  + q('Every month, fish are either sold or bought so that the number of young, juvenile and adult fish in the farm remains constant.<br>The population of fish in the fish farm after <i>n</i> months, <i>F</i><sub><i>n</i></sub>, can be determined by the recurrence rule')
  + row('<i>F</i><sub><i>n</i>+1</sub> = ' + M([['0.65', 0, 0, 0], ['0.25', '0.75', 0, 0], [0, '0.20', '0.95', 0], ['0.10', '0.05', '0.05', 1]]) + ' <i>F</i><sub><i>n</i></sub> + <i>B</i>')
  + q('where <i>B</i> is a column matrix that shows the number of young, juvenile and adult fish bought or sold each month and the number of dead fish that are removed.<br>Each month, the fish farm will')
  + mc(['sell 1650 adult fish.', 'buy 1750 adult fish.', 'sell 17 500 young fish.', 'buy 50 000 young fish.', 'buy 10 000 juvenile fish.'], 'A', cols=1)
  + space(14, '<i>F</i><sub>1</sub> = <i>F</i><sub>0</sub>, so <i>B</i> = <i>F</i><sub>0</sub> − <i>TF</i><sub>0</sub> = (17 500, −10 000, −1650, −5850): A is −1650, so sell 1650 adult fish'), '1 mark'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('11D', 'Q1–4')], ['11D']))
build('gm12-u4-11d', '11D', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-11d-worksheet', '11D worksheet'), ('gm12-u4-11d-worksheet-solutions', '11D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
