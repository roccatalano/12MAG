"""Lesson gm12-u4-14c (14C Precedence tables and activity networks) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now and CFAT are not on the worksheet; no CAS for 14C).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = VCAA 2018 Exam 1 N&DM Q4 (Edrolo U1&2 7D Q12). Examples 7-9 = Cambridge U3&4 pp. 685-688.
You try 1-3 = Edrolo U3&4 8H WE2 (pp. 609-610), WE4 (pp. 612-613), WE3 (pp. 610-611).
Exits = VCAA 2017 Exam 2 N&DM Q4a (Edrolo 8H Q14) · VCAA 2020 Exam 2 N&DM Q5a (Edrolo 8H Q15).
Output: lessons/14C worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-14c/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import img, ptab
def G(html, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{html}</div>'
def I(name, mm): return G(img(name), mm)
def sol(html): return f'<div class="solonly">{html}</div>'
def stu(mm): return f'<div class="stuonly"><div style="min-height:{mm}mm"></div></div>'
def pt(rows, **k): k.setdefault('fs', 11); return ptab(rows, **k)
EX7 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'C'), ('G', 'D'), ('H', 'E, F, G')]
EX8 = [('A', '–'), ('B', '–'), ('C', 'A'), ('D', 'B'), ('E', 'C, D'), ('F', 'C'), ('G', 'E, F')]
EX9 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'C'), ('F', 'D, C'), ('G', 'D, C'), ('H', 'E, F'), ('I', 'G'), ('J', 'G, H')]
WE2 = [('A', '–'), ('B', '–'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'B'), ('G', 'D, E'), ('H', 'C, G'), ('I', 'F, H')]
WE3 = [('A', '–'), ('B', '–'), ('C', '–'), ('D', 'B'), ('E', 'A, D'), ('F', 'B'), ('G', 'C'), ('H', 'E'), ('I', 'F, G')]
WE4 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'C'), ('G', 'D'), ('H', 'E, F'), ('I', 'C, G')]
AH = ('activity', 'immediate predecessor(s)')
CR = [['Activity', 'EST', 'Duration', 'Immediate predecessor(s)'], ['A', '0', '2', '–'], ['B', '0', '5', '–'], ['C', '5', '', 'A, B'], ['D', '7', '7', 'C'], ['E', '7', '9', 'C'],
      ['F', '5', '3', 'B'], ['G', '14', '4', 'D'], ['H', '8', '9', 'F'], ['I', '18', '2', 'E, G, H']]
def bl(x): return f'<span style="display:inline-block;min-width:14mm;border:1px solid #444;text-align:center;margin:0 1mm"><span class="blk" style="color:#c00;font-weight:700">{x}</span></span>'
def side(l, r): return f'<div style="display:flex;gap:4mm;align-items:flex-start"><div style="flex:1">{l}</div><div>{r}</div></div>'

P = [title('14C', 'Precedence tables and activity networks')]
P.append(lis(['To be able to identify activities in a project.', 'To be able to understand the precedence that some activities have over others in a project.',
              'To be able to identify immediate predecessors of activities from an activity network.', 'To be able to draw an activity network from a precedence table.',
              'To be able to understand and explain the need for dummy activities in projects.', 'To be able to include dummy activities in activity networks as required.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1 · VCAA 2018 Exam 1 Q4', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('Consider the graph below.')
  + q('Which one of the following is <b>not</b> a path for this graph?') + mc(['<i>PRQTS</i>', '<i>PQRTS</i>', '<i>PRTSQ</i>', '<i>PTQSR</i>', '<i>PTRQS</i>'], 'D')
  + why('there is no edge from S to R') + '</div>' + I('apk.png', 60) + '</div>', '1 mark'))
P.append(sect('14C Precedence tables and activity networks', 'Example, then you try'))
P.append(exyt('Example 7 · Drawing an activity network',
  q('Draw an activity network from the precedence table shown on the right.') + pt(EX7) + stu(30) + sol(I('cam7.png', 70)),
  'You try 1', q('Construct an activity network from the following precedence table.') + pt(WE2, head=AH) + stu(30) + sol(I('edr2.png', 75))))
P.append(exyt('Example 8 · Using a dummy activity',
  q('Draw an activity network from the precedence table shown on the right.') + pt(EX8) + stu(30) + sol(I('cam8.png', 75)),
  'You try 2', q('Consider the following precedence table.') + pt(WE4, head=AH)
  + q('a. Complete the following sentence.<br>A dummy activity needs to be drawn from the end of activity ' + bl('C') + ' to the start of activity ' + bl('I') + '.')
  + '<hr class="dash">' + q('b. Construct an activity network from the precedence table.') + stu(28) + sol(I('edr4.png', 70))))
P.append(exyt('Example 9 · Creating a precedence table from an activity network',
  q('Write down a precedence table for the activity network shown below.') + I('cam9.png', 80) + '<div class="stuonly">' + pt(EX9, blank=True) + '</div>' + sol(pt(EX9, red=True)),
  'You try 3', q('Construct a precedence table from the following activity network.') + I('edr3.png', 72) + '<div class="stuonly">' + pt(WE3, head=AH, blank=True) + '</div>' + sol(pt(WE3, head=AH, red=True))))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 2 Q4a', q('The rides at the theme park are set up at the beginning of each holiday season.<br>This project involves activities <i>A</i> to <i>O</i>.<br>The directed network below shows these activities and their completion times in days.')
  + I('ex1.png', 110) + q('a. Write down the two immediate predecessors of activity <i>I</i>.') + space(10, '<i>D</i> and <i>E</i> (the dummy carries <i>E</i>)'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2020 Exam 2 Q5a', q('The Sunny Coast cricket clubroom is undergoing a major works project.<br>This project involves nine activities: A to I.<br>The table below shows the earliest start time (EST) and duration, in months, for each activity.<br>The immediate predecessor(s) is also shown.<br>The duration for activity C is missing.')
  + table(CR) + q('The information in the table above can be used to complete a directed network.<br>This network will require a dummy activity.')
  + q('a. Complete the following sentence by filling in the boxes provided.<br>This dummy activity could be drawn as a directed edge from the end of activity ' + bl('B') + ' to the start of activity ' + bl('C') + '.'), '1 mark'))
SC = ['I can create an activity network from a precedence table.', 'I can write down a precedence table from an activity network.', 'I can decide when to use dummy activities in an activity network.']
P.append(close(SC, [('14C', 'Q1–10')], ['14C']))
P[0] = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
        '.blk{visibility:hidden}.sol .blk{visibility:visible}hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}</style>') + P[0]
build('gm12-u4-14c', '14C', 'AoS 4 · Networks and decision mathematics', P)
RD = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-14c-worksheet', '14C worksheet'), ('gm12-u4-14c-worksheet-solutions', '14C worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{RD}/{x}{ext}', f'{RD}/{y}{ext}')
