"""Lesson gm12-u4-11b (11B) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4G #17 (p. 293; solution worked for 12MAG).
Example 3 = Cambridge U3&4 Example 3 (pp. 555-556; diagram cropped). You try = Edrolo U3&4 7G WE3 (p. 483).
Exit = VCAA 2019 Further Exam 1 Matrices Q8 (Edrolo U3&4 7I Q16; diagram cropped from the paper).
Output: lessons/11B worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-11b/worksheet.py"""
import os, sys, json, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def IMG(f, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{mm}mm;max-width:100%;display:block;margin:1mm auto">'
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-11b')
P = [title('11B', 'Interpreting transition matrices')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('The following transition matrix, <i>T</i>, can be used to describe whether customers bring their shopping bags to the supermarket (<i>S</i>) or leave them at home (<i>H</i>), based on their behaviour last week.')
  + row('<i>T</i> = ' + LT(M([['0.8', '0.3'], ['0.2', '0.7']], cl=['S', 'H'], rl=['S', 'H'], side=True), 'This week', 'Next week'))
  + q('If 150 people took their bags for their weekly shop, and 90 people left their bags at home this week, how many people do you expect to bring their own shopping bags next week?')
  + space(18, '0.8 × 150 + 0.3 × 90 = 120 + 27 = 147 people')))

P.append(sect('11B Interpreting transition matrices', 'Example, then you try'))
EX = (Q('The following transition matrix, <i>T</i>, and its transition diagram can be used to describe the weekly pattern of rental car returns in three locations: Albury, Wodonga and Benalla.')
  + row('<i>T</i> = ' + LT(M([[0.7, 0.05, 0.12], [0.1, 0.8, 0.11], [0.2, 0.15, 0.77]], cl=['A', 'W', 'B'], rl=['A', 'W', 'B'], side=True), '', 'Returned to'))
  + IMG('ex3.png', 55) + Q('Use the transition matrix <i>T</i> and its transition diagram to answer the following questions.')
  + parts([('a', 'What percentage of cars rented in Wodonga each week are predicted to be returned to:<br>i Albury? &nbsp; ii Benalla? &nbsp; iii Wodonga?', 'i 5% &nbsp; ii 15% &nbsp; iii 80%', 'L'),
           ('b', 'Two hundred cars were rented in Albury this week. How many of these cars do we expect to be returned to:<br>i Albury? &nbsp; ii Benalla? &nbsp; iii Wodonga?', 'i 0.70 × 200 = 140 &nbsp; ii 0.20 × 200 = 40 &nbsp; iii 0.10 × 200 = 20', 'L'),
           ('c', 'What percentage of cars rented in Benalla each week are <i>not</i> expected to be returned to Benalla?', '11 + 12 = 23% (or 100 − 77)', 'L'),
           ('d', 'One hundred and sixty cars were rented in Albury this week. How many of these cars are expected to be returned to either Benalla or Wodonga?', '20% of 160 + 10% of 160 = 48 cars', 'L')]))
YT = (Q('The transition matrix, <i>T</i>, is used to predict the number of people who drive, bus, or train to work on a day-to-day basis.')
  + row('<i>T</i> = ' + LT(M([['0.68', '0.34', '0.58'], ['0.22', '0.17', '0.36'], ['0.10', '0.49', '0.06']], cl=['drive', 'bus', 'train'], rl=['drive', 'bus', 'train'], side=True), 'today', 'tomorrow'))
  + Q('What percentage of people who caught the train today will choose to drive tomorrow?')
  + space(30, 'train today = column 3, drive tomorrow = row 1: 0.58 = 58%'))
P.append(exyt('Example 3 · Interpreting a transition matrix', EX, 'You try 1', YT))

P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 1 Q8', q('An airline parks all of its planes at Sydney airport or Melbourne airport overnight.<br>The transition diagram below shows the change in the location of the planes from night to night.')
  + IMG('exit1.png', 95)
  + q('There are always <i>m</i> planes parked at Melbourne airport.<br>There are always <i>s</i> planes parked at Sydney airport.<br>Of the planes parked at Melbourne airport on Tuesday night, 12 had been parked at Sydney airport on Monday night.<br>How many planes does the airline have?')
  + mc(['25', '37', '62', '65', '85'], 'E', cols=5) + space(16, '0.48<i>s</i> = 12 → <i>s</i> = 25; 12 also go Melbourne → Sydney: 0.2<i>m</i> = 12 → <i>m</i> = 60; 60 + 25 = 85') , '1 mark'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('11B', 'Q1–6')], ['11B']))
build('gm12-u4-11b', '11B', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-11b-worksheet', '11B worksheet'), ('gm12-u4-11b-worksheet-solutions', '11B worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
