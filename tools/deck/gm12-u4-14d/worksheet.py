"""Lesson gm12-u4-14d (14D Scheduling problems and critical path analysis) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now is not on the worksheet; no CAS for 14D).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK = VCAA 2021 Exam 2 N&DM Q2a (Edrolo U1&2 7E Q13). Examples 10-11 = Cambridge U3&4 pp. 699-702.
You try 1-4 = Edrolo U3&4 8I WE1 (p. 623), WE2 (pp. 624-625), WE3 (pp. 626-627), WE4 (p. 628).
Exits = VCAA 2020 Exam 1 N&DM Q6 (Edrolo 8I Q15) · VCAA 2018 Exam 2 N&DM Q3a-d (Edrolo 8I Q16) · VCAA 2021 Exam 1 N&DM Q6 (Edrolo 8I Q17).
Output: lessons/14D worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-14d/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import img, wtab
def G(html, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{html}</div>'
def I(name, mm): return G(img(name), mm)
def sol(html): return f'<div class="solonly">{html}</div>'
def stu(mm): return f'<div class="stuonly"><div style="min-height:{mm}mm"></div></div>'
def red(t): return f'<div class="solonly" style="color:#c00;font-weight:700;font-size:10pt">{t}</div>'
def ans(mm, t): return stu(mm) + red(t)
HR = '<hr class="dash">'
EX10 = [('A', 6, '–'), ('B', 9, '–'), ('C', 8, 'A, B'), ('D', 7, 'A, B'), ('E', 10, 'D'), ('F', 12, 'C, E')]
EX11 = [('A', 3, '–'), ('B', 5, '–'), ('C', 12, '–'), ('D', 4, 'A'), ('E', 7, 'A'), ('F', 5, 'B, D'), ('G', 6, 'E, F'), ('H', 2, 'C')]
def bl(x): return f'<span style="display:inline-block;min-width:14mm;border:1px solid #444;text-align:center;margin:0 1mm"><span class="blk" style="color:#c00;font-weight:700">{x}</span></span>'

P = [title('14D', 'Scheduling problems and critical path analysis')]
P.append(lis(['To be able to understand activity networks that include weights (durations) of each activity.', 'To be able to determine the EST for activities using forward scanning.',
              'To be able to determine the LST for activities using backward scanning.', 'To be able to calculate and understand the existence of float times for some activities.',
              'To be able to identify the critical path and completion time of a project.']))
P.append(sect('Activating prior knowledge', 'Year 11 skills'))
P.append(box('Question 1 · VCAA 2021 Exam 2 Q2a', q('George lives in Town <i>G</i> and Maggie lives in Town <i>M</i>.<br>The diagram below shows the network of main roads between Town <i>G</i> and Town <i>M</i>.<br>The vertices <i>G</i>, <i>H</i>, <i>I</i>, <i>J</i>, <i>K</i>, <i>L</i>, <i>M</i>, <i>N</i> and <i>O</i> represent towns.<br>The edges represent the main roads. The numbers on the edges indicate the distances, in kilometres, between adjacent towns.')
  + I('apk.png', 100) + q('a. What is the shortest distance, in kilometres, between Town <i>G</i> and Town <i>M</i>?') + space(10, '86 km (<i>G</i>–<i>O</i>–<i>N</i>–<i>M</i>: 28 + 42 + 16)'), '1 mark'))
P.append(sect('14D Scheduling problems', 'Example, then you try'))
P.append(exyt('Example 10 · Finding the critical path from a precedence table',
  q('A project has six activities as shown in the precedence table and the associated activity network is shown below.') + wtab(EX10, fs=10) + I('cam10q.png', 75)
  + q('a. Complete the critical path analysis to calculate the EST and LST for each activity.') + sol(I('cam10a.png', 80)) + stu(4) + HR
  + q('b. Write down the critical path of this project.') + ans(8, '<i>B</i> → <i>D</i> → <i>E</i> → <i>F</i>') + HR
  + q('c. What is the minimum time required to complete the project?') + ans(8, '38 days'),
  'You try 1', q('Construct an activity network based on the following weighted precedence table.') + I('edr1t.png', 55) + stu(45) + sol(I('edr1a.png', 70))))
P.append(exyt('You try 2 · Forward scanning',
  q('Consider the following activity network. The estimated completion times are in hours.') + I('edr2q.png', 70)
  + q('a. Find the earliest start time of activity <i>H</i>.') + ans(14, '15 hours (largest of 4 + 11 + 0, 4 + 5, 12 + 3)') + HR
  + q('b. Find the minimum completion time of the project.') + ans(14, '24 hours (largest of 15 + 4, 15 + 9)'),
  'You try 3 · Backward scanning', q('Consider the following activity network with the earliest start time for each activity filled in. The estimated completion times are in hours.') + I('edr3q.png', 70)
  + q('Find the latest start time of activity <i>B</i>.') + ans(30, 'LST <i>H</i> = 24 − 9 = 15, <i>G</i> = 24 − 4 = 20<br><i>B</i>: smallest of 15 − 0 − 11 = 4, 20 − 11 = 9 → 4 hours')))
P.append(exyt('Example 11 · Finding the critical path',
  q('A project has eight activities as shown in the precedence table.') + wtab(EX11, fs=10, unit='weeks')
  + q('a. Draw an activity network for this project.') + stu(32) + sol(I('cam11a.png', 70)) + HR
  + q('b. Complete the critical path analysis to calculate the EST and LST for each activity.') + stu(32) + sol(I('cam11d.png', 75)) + HR
  + q('c. What is the earliest starting time for activity H?') + ans(5, '12 weeks') + q('d. What is the latest starting time for activity H?') + ans(5, '16 weeks')
  + q('e. What is the float time of activity H?') + ans(5, '16 − 12 = 4 weeks') + q('f. Write down the critical path of this project.') + ans(5, '<i>A</i> – <i>D</i> – <i>F</i> – <i>G</i>')
  + q('g. What is the minimum time required to complete the project?') + ans(5, '18 weeks')
  + q('h. The person responsible for completing activity E falls sick three weeks into the project. If he will be away from work for two weeks, will this cause the entire project to be delayed?') + ans(12, 'No: the float of <i>E</i> is 5 − 3 = 2 weeks, equal to the delay.'),
  'You try 4', q('Consider the following activity network with the earliest and latest starting time for each activity shown. The estimated completion times are in hours.') + I('edr4q.png', 70)
  + q('a. Determine the critical path(s) of the project.') + ans(30, '<i>A</i>–<i>B</i>–<i>H</i> and <i>A</i>–<i>D</i>–<i>E</i>–<i>F</i>–<i>H</i>') + HR
  + q('b. Determine the float time of activity <i>C</i>.') + ans(30, 'float = 10 − 4 = 6 hours')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2020 Exam 1 Q6', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('The activity network below shows the sequence of activities required to complete a project.<br>The number next to each activity in the network is the time it takes to complete that activity, in days.')
  + q('The minimum completion time for this project, in days, is') + mc(['18', '19', '20', '21', '22'], 'E') + why('the longest path: largest EST at every vertex gives 22') + '</div>' + I('ex1.png', 85) + '</div>', '1 mark'))
P.append(box('Exit task 2 · VCAA 2018 Exam 2 Q3', q('At the Zenith Post Office all computer systems are to be upgraded.<br>This project involves 10 activities, <i>A</i> to <i>J</i>.<br>The directed network below shows these activities and their completion times, in hours.')
  + I('ex2.png', 80) + q('a. Determine the earliest starting time, in hours, for activity <i>I</i>.') + space(8, '10 hours') + HR
  + q('b. The minimum completion time for the project is 15 hours.<br>Write down the critical path.') + space(8, '<i>B</i>–<i>E</i>–<i>G</i>–<i>H</i>–<i>J</i>') + HR
  + q('c. Two of the activities have a float time of two hours.<br>Write down these two activities.') + space(8, '<i>A</i> and <i>C</i>') + HR
  + q('d. For the next upgrade, the same project will be repeated but one extra activity will be added.<br>This activity has a duration of one hour, an earliest starting time of five hours and a latest starting time of 12 hours.<br>Complete the following sentence by filling in the boxes provided.<br>The extra activity could be represented on the network above by a directed edge from the<br>end of activity ' + bl('E') + ' to the start of activity ' + bl('J') + '.'), '4 marks'))
P.append(box('Exit task 3 · VCAA 2021 Exam 1 Q6', '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">'
  + q('The directed graph below shows the sequence of activities required to complete a project.<br>The time taken to complete each activity, in hours, is also shown.')
  + q('The minimum completion time for this project is 18 hours.<br>The time taken to complete activity <i>E</i> is labelled <i>x</i>.<br>The maximum value of <i>x</i> is') + mc(['2', '3', '4', '5', '6'], 'B')
  + why('<i>E</i> starts at 8 (via <i>C</i>, <i>G</i>, <i>F</i>) and must end by 18 − 7 = 11') + '</div>' + I('ex3.png', 95) + '</div>', '1 mark'))
SC = ['I can use forward scanning to determine the earliest starting time of activities in an activity network.', 'I can use backward scanning to determine the latest starting time of activities in an activity network.',
      'I can determine the float time for activities in an activity network.', 'I can determine the overall minimum completion time for a project using critical path analysis.', 'I can determine the critical path for an activity network.']
P.append(close(SC, [('14D', 'Q1–18')], ['14D']))
P[0] = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
        '.blk{visibility:hidden}.sol .blk{visibility:visible}hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}</style>') + P[0]
build('gm12-u4-14d', '14D', 'AoS 4 · Networks and decision mathematics', P)
RD = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-14d-worksheet', '14D worksheet'), ('gm12-u4-14d-worksheet-solutions', '14D worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{RD}/{x}{ext}', f'{RD}/{y}{ext}')
