"""Lesson gm12-u4-11a (11A) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py), matrices from tools/deck/mx.py.
Questions verbatim, same items and order as build.py (Do Now not on the worksheet; no CAS steps).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = Cambridge U1&2 Ch 4 review skills checklist 4G #16 (p. 293; solution worked for 12MAG); VCAA 2019 Exam 2 Matrices Q2b and Q3a (Edrolo U1&2 5G Q11).
Examples 1-2 = Cambridge U3&4 Examples 1-2 (pp. 552-553; Example 1 diagram cropped).
You trys = Edrolo U3&4 7I WE2a (p. 505, diagram cropped), 7G WE4 (pp. 483-484).
Exit = VCAA 2017 Exam 2 Matrices Q2a,b (Edrolo U3&4 7I Q14; diagram cropped from the paper).
Output: lessons/11A worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-11a/worksheet.py"""
import os, sys, json, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..'))
from ws2 import *
import ws2
from mx import mat
A = lambda v: ans(v)
def M(r, **k): return mat(r, fs=12, pad='0 4px', **k)
def Q(t): return '<div class="q">' + t + '</div>'
def row(*xs): return '<div style="display:flex;gap:4mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:1.5mm 0">' + ''.join('<span style="display:inline-flex;align-items:center;gap:1mm">' + x + '</span>' for x in xs) + '</div>'
def IMG(f, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(H,"fig",f),"rb").read()).decode()}" style="width:{mm}mm;max-width:100%;display:block;margin:1mm auto">'
def TT(labels, rows, top, side, blank=True):
    """labelled transition matrix scaffold: column heading on top, row heading on the right; values red on the solutions copy"""
    v = [[A(x) if blank else x for x in r] for r in rows]
    return row(f'<i>T</i> = <span style="display:inline-flex;flex-direction:column;align-items:center"><i style="font-size:9pt">{top}</i>' + M(v, cl=labels, rl=labels) + '</span>' + f'<i style="font-size:9pt">{side}</i>')
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
CARD = _card(json.load(open(os.path.join(ws2.ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-11a')
P = [title('11A', 'Transition matrices: setting up a transition matrix')]
P.append(lis([x for g in CARD['learningObjectives'] for x in g['items']]))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1', q('A charity sends out a monthly letter asking for donations. They notice that 60% of patrons who donated last month will donate this month, while 30% of patrons who did not donate last month will donate this month. Construct a transition matrix that describes how the behaviour of patrons who donate (<i>D</i>) or do not donate (<i>N</i>) changes from month to month.')
  + space(26, TT(['D', 'N'], [['0.6', '0.3'], ['0.4', '0.7']], 'last month', 'this month', blank=False))))
T19 = M([[0.1, 0.2, 0.1, 0.2], [0.3, 0.4, 0.6, 0.3], [0.1, 0.2, 0.2, 0.1], [0.5, 0.2, 0.1, 0.4]], cl=['A', 'F', 'G', 'W'], rl=['A', 'F', 'G', 'W'], side=True)
P.append(box('Question 2 · VCAA 2019 Exam 2 Q2b', q('The theme park has four locations, Air World (<i>A</i>), Food World (<i>F</i>), Ground World (<i>G</i>) and Water World (<i>W</i>). The number of visitors at each of the four locations is counted every hour.')
  + q('Let <i>S</i><sub><i>n</i></sub> be the state matrix that shows the number of visitors expected at each location <i>n</i> hours after 10 am on Saturday. The number of visitors expected at each location <i>n</i> hours after 10 am on Saturday can be determined by the matrix recurrence relation below.')
  + row('<i>S</i><sub>0</sub> = ' + M([[600], [600], [400], [400]]), ', <i>S</i><sub><i>n</i>+1</sub> = <i>T</i> × <i>S</i><sub><i>n</i></sub> &nbsp; where &nbsp;<i>T</i> = ' + T19, '<i style="font-size:9pt">this hour → next hour</i>')
  + q('b. Complete the state matrix, <i>S</i><sub>1</sub>, below to show the number of visitors expected at each location at 11 am on Saturday.')
  + space(4) + row('<i>S</i><sub>1</sub> = ' + M([[A('300')], [A('780')], ['300'], [A('620')]], rl=['A', 'F', 'G', 'W'], side=True)), '1 mark'))
P.append(box('Question 3 · VCAA 2019 Exam 2 Q3a', q('On Sunday, matrix <i>V</i> is used when calculating the expected number of visitors at each location every hour after 10 am. It is assumed that the park will be at its capacity of 2000 visitors for all of Sunday.')
  + q('Let <i>L</i><sub>0</sub> be the state matrix that shows the number of visitors at each location at 10 am on Sunday. The number of visitors expected at each location at 11 am on Sunday can be determined by the matrix product')
  + row('<i>V</i> × <i>L</i><sub>0</sub> &nbsp; where &nbsp;<i>L</i><sub>0</sub> = ' + M([[500], [600], [500], [400]], rl=['A', 'F', 'G', 'W'], side=True), 'and &nbsp;<i>V</i> = ' + M([[0.3, 0.4, 0.6, 0.3], [0.1, 0.2, 0.1, 0.2], [0.1, 0.2, 0.2, 0.1], [0.5, 0.2, 0.1, 0.4]], cl=['A', 'F', 'G', 'W'], rl=['A', 'F', 'G', 'W'], side=True))
  + q('a. Safety restrictions require that all four locations have a maximum of 600 visitors. Which location is expected to have more than 600 visitors at 11 am on Sunday?')
  + space(16, 'Air World: 0.3 × 500 + 0.4 × 600 + 0.6 × 500 + 0.3 × 400 = 810 &gt; 600'), '1 mark'))

P.append(sect('11A Setting up a transition matrix', 'Example, then you try'))
P.append(exyt('Example 1 · Setting up a transition matrix',
  Q('The diagram gives the weekly return rates of rental cars at three locations: Albury, Wodonga and Benalla. Construct a transition matrix that describes the week-by-week return rates at each of the three locations. Convert the percentages to proportions.')
  + IMG('ex1.png', 62) + TT(['A', 'W', 'B'], [['0.7', '0.05', '0.12'], ['0.1', '0.8', '0.11'], ['0.2', '0.15', '0.77']], 'Rented in', 'Returned to')
  + q('Check: each column adds to ' + A('1') + '.'),
  'You try 1', Q('Complete the following conversions.<br>a. Convert the following transition diagram into a transition matrix.') + IMG('yt1.png', 62)
  + space(34, row('<i>T</i> = ' + M([['0.00', '0.05', '0.50'], ['0.80', '0.20', '0.00'], ['0.20', '0.75', '0.50']], cl=['R', 'S', 'T'], rl=['R', 'S', 'T'], side=True)))))
P.append(exyt('Example 2 · Setting up a transition matrix',
  Q('A factory has a large number of machines. Machines can be in one of two states: operating or broken. Broken machines are repaired and come back into operation, and vice versa. On a given day:'
    '<ul style="margin:1mm 0 1mm 5mm;padding:0"><li>85% of machines that are operational stay operating</li><li>15% of machines that are operating break down</li><li>5% of machines that are broken are repaired and start operating again</li><li>95% of machines that are broken stay broken.</li></ul>'
    'Construct a transition matrix to describe this situation. Use the columns to define the situation at the ‘Start’ of the day and the rows to describe the situation at the ‘End’ of the day.')
  + TT(['O', 'B'], [['0.85', '0.05'], ['0.15', '0.95']], 'Start', 'End'),
  'You try 2', Q('Johnny is an avid fan of fish, and has two different ponds (A and B) for his Koi fish. The number of Koi fish in each pond can change on a daily basis.'
    '<ul style="margin:1mm 0 1mm 5mm;padding:0"><li>10% of the Koi fish in pond A today will remain in pond A tomorrow.</li><li>15% of the Koi fish in pond B today will be moved to pond A tomorrow.</li></ul>'
    'Construct a transition matrix, <i>T</i>, to represent the movement of Koi fish in each pond from one day to the next.')
  + space(34, row('<i>T</i> = ' + M([['0.10', '0.15'], ['0.90', '0.85']], cl=['A', 'B'], rl=['A', 'B'], side=True) + ' (today → tomorrow)'))))

P.append(sect('Exit task', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 2 Q2a, b', q('Junior students at this school must choose one elective activity in each of the four terms in 2018.<br>Students can choose from the areas of performance (<i>P</i>), sport (<i>S</i>) and technology (<i>T</i>).<br>'
  'The transition diagram below shows the way in which junior students are expected to change their choice of elective activity from term to term.') + IMG('exit1.png', 58)
  + parts([('a', 'Of the junior students who choose performance (<i>P</i>) in one term, what percentage are expected to choose sport (<i>S</i>) the next term? (1 mark)', '40%', 'L'),
           ('b', 'Matrix <i>J</i><sub>1</sub> lists the number of junior students who will be in each elective activity in Term 1.' + row('<i>J</i><sub>1</sub> = ' + M([[300], [240], [210]], rl=['P', 'S', 'T'], side=True))
            + '306 junior students are expected to choose sport (<i>S</i>) in Term 2.<br>Complete the calculation below to show this. (1 mark)'
            + row('300 × <span style="display:inline-block;min-width:16mm;border:1px solid #333;padding:1mm;text-align:center">' + A('0.4') + '</span> + 240 × <span style="display:inline-block;min-width:16mm;border:1px solid #333;padding:1mm;text-align:center">' + A('0.6') + '</span> + 210 × <span style="display:inline-block;min-width:16mm;border:1px solid #333;padding:1mm;text-align:center">' + A('0.2') + '</span> = 306'), '', 2)]), '2 marks'))
P.append(close([x for g in CARD['successCriteria'] for x in g['items']], [('11A', 'Q1–4')], ['11A']))
build('gm12-u4-11a', '11A', 'AoS 3 · Matrices', P)
R = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-11a-worksheet', '11A worksheet'), ('gm12-u4-11a-worksheet-solutions', '11A worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{R}/{x}{ext}', f'{R}/{y}{ext}')
