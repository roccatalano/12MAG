"""Lesson gm12-u4-14d (14D Scheduling problems and critical path analysis) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/14D slides.html      Run: python3 tools/deck/gm12-u4-14d/build.py      Screenshots: python3 tools/deck/gm12-u4-14d/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; figures cropped from the sources by crop.py, fig/*.png):
- No CFAT at the start (CFAT 4.14.1 sits on 14C, 4.14.2 on 14E).
- Do Now: VCAA 2023 Exam 1 Q38 (D, 60%) · VCAA 2025 Exam 1 Q13 (C, 76%) · VCAA 2023 Exam 2 Q14 stem + Q14a (C, G; 73%) ·
          VCAA 2023 Exam 2 Q9 stem + Q9c (I-H-E-G-F; 68%). Q9c replaces the card's Q9d: the 2023 E2 report says Q9d was invalidated (error in the stimulus).
- APK: VCAA 2021 Further Exam 2 N&DM Q2 stem + Q2a (original wording; = Edrolo U1&2 7E Q13, adapted there; 86 km, 85%).
- Learn: Cambridge U3&4 14D pp. 692-699 (own words) · Edrolo U3&4 8I pp. 623-628 (forward/backward scanning diagrams cropped from pp. 624, 626).
- Worked examples: Cambridge U3&4 Example 10 (p. 699), Example 11 (pp. 700-702; Cambridge's part d solution misprints 'EST' for 'LST').
  You trys: Edrolo U3&4 8I Worked examples 1 + 2 (pp. 623-625), 3 + 4 (pp. 626-628).
- No CAS (card: none).
- Exits: VCAA 2020 Further Exam 1 N&DM Q6 (E, 61%) · VCAA 2018 Further Exam 2 N&DM Q3a-d (10 64%, B-E-G-H-J 76%, A and C 45%, E to J 25%) ·
         VCAA 2021 Further Exam 1 N&DM Q6 (B, 46%). Original VCAA wording; % from the examiner reports (Edrolo prints 45% for Q3d; the 2018 report says 25%).
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
CAM = 'Cambridge General Mathematics Units 3&amp;4'; EDR = 'Edrolo General Mathematics Units 3&amp;4'; EDR12 = 'Edrolo General Mathematics Units 1&amp;2'
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-14d')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'
def side(a, txt, w=280): return f'<div style="display:flex;gap:18px;align-items:center;justify-content:center">{a}<div style="font-size:19px;width:{w}px">{txt}</div></div>'

EX10 = [('A', 6, '–'), ('B', 9, '–'), ('C', 8, 'A, B'), ('D', 7, 'A, B'), ('E', 10, 'D'), ('F', 12, 'C, E')]
EX11 = [('A', 3, '–'), ('B', 5, '–'), ('C', 12, '–'), ('D', 4, 'A'), ('E', 7, 'A'), ('F', 5, 'B, D'), ('G', 6, 'E, F'), ('H', 2, 'C')]
S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .R .wk li{font-size:15px}'
     '.L .q ul li{font-size:inherit!important;line-height:1.3!important}</style>']
S.append(title('14D', 'Scheduling problems and critical path analysis', f'{CAM} · 14D Scheduling problems', 'gm12-u4-14d'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 14D', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>14D')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· one Year 11 question', 'var(--apk)'),
  ('Forward scanning: EST', '', None), ('Worked example 10', '→ You try', None), ('Backward scanning: LST, float, critical path', '', None),
  ('Worked example 11', '→ You try', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'), ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Earliest start time (EST)', 'the earliest an activity can start'), ('Minimum completion time', 'EST at the finish = the longest path'),
  ('Latest start time (LST)', 'the latest an activity can start without delaying the project'), ('Float time', 'how long an activity can be delayed'),
  ('Critical path', 'the activities with zero float; a delay here delays the project'), ('Shortest path (Year 11)', 'smallest total weight from one vertex to another')],
  [('EST', 'EST = EST of predecessor + its duration', 'forward scan: take the LARGEST'),
   ('LST', 'LST = LST of following activity − duration', 'backward scan: take the SMALLEST'),
   ('Float', 'float = LST − EST', 'critical ⇔ float = 0')],
  f'{CAM}, 14D pp. 692–699; {EDR}, 8I pp. 623–628; Study Design: forward and backward scanning to determine EST and LST; critical path and float times'))

# ================= Do Now
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2023 Exam 1 Q38', 'Review of 14C (activity networks)',
  '<div style="font-size:15px">A particular building project has ten activities that must be completed.<br>These activities and their immediate predecessor(s) are shown in the table below.'
  + Wd(170, img('dn1t.png')) + 'A directed graph that could represent this project is</div>',
  [('Dummy?', '<i>G</i> needs <i>C</i>, <i>F</i>; <i>H</i> needs only <i>F</i>: a dummy from the end of <i>F</i>'),
   ('Direction', 'it runs from the end of <i>F</i> into the start of <i>G</i> (with <i>C</i>)'), ('Check', '<i>I</i> after <i>D</i>, <i>E</i>; <i>J</i> after <i>H</i>, <i>I</i>')],
  'Graph <b>D</b> represents the project.', 'VCAA 2023 General Mathematics Exam 1 Q38 (examiner report: 60% correct)',
  mc=[Wd(320, img(f'dn1{k}.png')) for k in 'ABCDE'], key='D', stat=('mc', 60), dis=('A', 'A (13%) has no dummy: <i>H</i> would then need <i>C</i> as well.')))
sm(extra='sm xs')
S[-1] = S[-1].replace('class="mc"', 'class="mc" style="display:grid;grid-template-columns:1fr 1fr;gap:2px"', 1)
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2025 Exam 1 Q13', 'Review of 5C (median smoothing)',
  ('<div style="font-size:18px">The following time series graph shows the <i>margin</i>, in points, for a team winning all of its games in the first 18 weeks of a season. The team plays one game per week.</div>',
   Wd(400, img('dn2.png')), '<div style="font-size:18px">The time series graph is smoothed using five-median smoothing.<br>The smoothed value for the <i>margin</i> in <i>week</i> 8, in points, is</div>'),
  [('Five values', 'weeks 6 to 10: 50, 38, 32, 35, 41'), ('Order', '32, 35, <b>38</b>, 41, 50: the middle one')],
  'The smoothed value is 38: <b>C</b>.', 'VCAA 2025 General Mathematics Exam 1 Q13 (examiner report: 76% correct)',
  mc=['32', '35', '38', '41'], key='C', stat=('mc', 76), dis=('A', 'A (10%) is the actual week 8 value, not the median of five.')))
sm()
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2023 Exam 2 Q14a', 'Review of 14C (immediate predecessors)',
  ('<div style="font-size:15px">One of the landmarks in state <i>A</i> requires a renovation project.<br>This project involves 12 activities, <i>A</i> to <i>L</i>. The directed network below shows these activities and their completion times, in days.</div>',
   '<div style="font-size:15px">The table below shows the 12 activities that need to be completed for the renovation project.<br>It also shows the earliest start time (EST), the duration, and the immediate predecessors for the activities.<br>The immediate predecessor(s) for activity <i>I</i> and the EST for activity <i>J</i> are missing.</div>'
   + f'<div style="display:flex;gap:8px;align-items:center">{Wd(430, img("dn3n.png"))}{Wd(240, img("dn3t.png"))}</div>',
   '<div style="font-size:16px">a. Write down the immediate predecessor(s) for activity <i>I</i>. <span class="muted">(1 mark)</span></div>'),
  [('Into I', '<i>G</i> ends where <i>I</i> starts'), ('Dummy', 'brings <i>C</i> to the same vertex')],
  'The immediate predecessors of <i>I</i> are <b><i>C</i> and <i>G</i></b>.', 'VCAA 2023 General Mathematics Exam 2 Q14 stem and Q14a (examiner report: average 0.7/1, 73%)',
  stat=('avg', 73), cmd=('Write down', 1, 'count the dummy’s activity')))
sm(extra='sm xs')
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2023 Exam 2 Q9c', 'Review of 10F (permutation matrices)',
  ('<div style="font-size:18px">The circus is held at five different locations, <i>E</i>, <i>F</i>, <i>G</i>, <i>H</i> and <i>I</i>. …<br>The circus moves from one location to the next each month. It rotates through each of the five locations, before starting the cycle again.<br>The following matrix displays the movement between the five locations.</div>',
   Wd(400, img('dn4.png')), '<div style="font-size:18px">c. The circus started in town <i>I</i>.<br>What is the order in which the circus will visit the five towns? <span class="muted">(1 mark)</span></div>'),
  [('Read a column', 'column = this month, the 1 shows next month'), ('From I', '<i>I</i> → <i>H</i> → <i>E</i> → <i>G</i> → <i>F</i>')],
  'The order is <b><i>I</i> – <i>H</i> – <i>E</i> – <i>G</i> – <i>F</i></b>.', 'VCAA 2023 General Mathematics Exam 2 Q9 stem (part) and Q9c (examiner report: average 0.7/1, 68%)',
  stat=('avg', 68), cmd=('What', 1, 'the five towns in order')))
sm()

# ================= APK
S.append(qslide('apk', 'APK · VCAA 2021 Exam 2 Q2a', 'Shortest path (Year 11)',
  ('<div style="font-size:19px">George lives in Town <i>G</i> and Maggie lives in Town <i>M</i>.<br>The diagram below shows the network of main roads between Town <i>G</i> and Town <i>M</i>.<br>The vertices <i>G</i>, <i>H</i>, <i>I</i>, <i>J</i>, <i>K</i>, <i>L</i>, <i>M</i>, <i>N</i> and <i>O</i> represent towns.<br>The edges represent the main roads. The numbers on the edges indicate the distances, in kilometres, between adjacent towns.</div>',
   Wd(460, img('apk.png')), '<div style="font-size:19px">a. What is the shortest distance, in kilometres, between Town <i>G</i> and Town <i>M</i>? <span class="muted">(1 mark)</span></div>'),
  [('Try routes', 'G–J–K–L–M: 30 + 15 + 25 + 30 = 100'), ('Better', 'G–J–N–M: 30 + 50 + 16 = 96'),
   ('Shortest', 'G–O–N–M: 28 + 42 + 16 = 86')],
  'The shortest distance is <b>86 km</b>.', f'VCAA 2021 Further Mathematics Exam 2 Networks and decision mathematics Q2 stem and Q2a (examiner report: 85%) · {EDR12} 7E Q13 (adapted there)',
  stat=('avg', 85), cmd=('What', 1, 'a distance in km')))
sm()

# ================= Learn 1: forward scan
S.append(learn('Learn · 14D', 'Forward scanning: EST',
  '<h4>Work from start to finish</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>draw a two-cell box at the start of each activity and at the finish</li><li>activities leaving the start: <b>EST = 0</b></li>'
  '<li>EST = EST of predecessor + its duration</li><li>several arrows in: take the <b>largest</b> (everything before must be done)</li>'
  '<li>EST at the finish = <b>minimum completion time</b> (the longest path)</li></ul>',
  side(Wd(470, img('lrn1.png')), frag('<i>D</i> and <i>E</i>: 0 + 3 = 3 (dummy adds 0)') + frag('Finish: largest of 3 + 2, 3 + 3, 2 + 2 = 6 hours')),
  'Critical path = LONGEST path, not shortest.', f'{CAM}, 14D pp. 692–695 (own words) · {EDR}, 8I p. 624 (diagram)',
  cards=(kcard('EST', 'largest in'), kcard('Minimum completion time', 'EST at finish'))))
S.append(qslide('we', 'Worked example 10 · 14D', 'Finding the critical path from a precedence table',
  ('<div style="font-size:17px">A project has six activities as shown in the precedence table and the associated activity network is shown below.' + wtab(EX10, fs=14) + '</div>',
   Wd(380, img('cam10q.png')), plist([('a', '<b>Complete</b> the critical path analysis to calculate the EST and LST for each activity.'), ('b', 'Write down the critical path of this project.'), ('c', 'What is the minimum time required to complete the project?')])),
  [('EST', '<i>A</i>, <i>B</i>: 0. <i>C</i>, <i>D</i>: largest of 0 + 6, 0 + 9 = 9 (dummy)'), ('EST', '<i>E</i>: 9 + 7 = 16. <i>F</i>: largest of 9 + 8, 16 + 10 = 26. Finish 26 + 12 = 38'),
   ('LST', 'back from 38: <i>F</i> 26, <i>E</i> 16, <i>C</i> 26 − 8 = 18, <i>D</i> 9, <i>B</i> 9 − 9 = 0, <i>A</i> 9 − 6 = 3'), ('Critical', 'EST = LST: <i>B</i>, <i>D</i>, <i>E</i>, <i>F</i>')],
  '', f'{CAM} · Example 10 (p. 699)', video='Cambridge GO · Example 10 (14D Resources)', cmd=('Complete', None, 'EST forwards, LST backwards'),
  parts=[('a', Wd(440, img('cam10a.png'))), ('b', '<i>B</i> → <i>D</i> → <i>E</i> → <i>F</i> (the dummy is not part of the path)'), ('c', '38 days')]))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8I WE1', 'Activity network from a weighted table',
  ('<div style="font-size:19px"><b>Construct</b> an activity network based on the following weighted precedence table.</div>', Wd(330, img('edr1t.png')), ''),
  [('Start', '<i>A</i> leaves start; <i>B</i>, <i>C</i>, <i>D</i> after <i>A</i>'), ('Chains', '<i>E</i> after <i>D</i>, <i>F</i> after <i>E</i>; <i>G</i> after <i>B</i>'),
   ('Dummy', '<i>H</i> needs <i>B</i>, <i>C</i>, <i>F</i>: dummy from the end of <i>B</i>')],
  '', f'{EDR} · 8I Worked example 1 (p. 623)', cmd=('Construct', None, 'label each edge activity, duration'), afig=Wd(360, img('edr1a.png'))))
S.append(qslide('yt', 'You try · Edrolo 8I WE2', 'Forward scanning',
  ('<div style="font-size:19px">Consider the following activity network. The estimated completion times are in hours.</div>', Wd(380, img('edr2q.png')),
   plist([('a', '<b>Find</b> the earliest start time of activity <i>H</i>.'), ('b', '<b>Find</b> the minimum completion time of the project.')])),
  [('Start', '<i>A</i>: 0; <i>B</i>, <i>C</i>, <i>D</i>: 0 + 4 = 4'), ('Next', '<i>E</i>: 4 + 6 = 10; <i>F</i>: 10 + 2 = 12; <i>G</i>: 4 + 11 = 15'),
   ('H', 'largest of 15 (dummy), 4 + 5 = 9, 12 + 3 = 15'), ('Finish', 'largest of 15 + 4 = 19, 15 + 9 = 24')],
  '', f'{EDR} · 8I Worked example 2 (pp. 624–625)', cmd=('Find', None, 'largest value in'),
  parts=[('a', '15 hours'), ('b', '24 hours ' + Wd(300, img('edr2a.png')))]))
sm()

# ================= Learn 2: backward scan
S.append(learn('Learn · 14D', 'Backward scanning: LST, float, critical path',
  '<h4>Work from finish to start</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>finish: LST = EST (the minimum completion time)</li><li>LST = LST of the following activity − its own duration</li>'
  '<li>several arrows out: take the <b>smallest</b></li><li><b>float = LST − EST</b>; float 0 → <b>critical</b></li>'
  '<li>critical path: start to finish using only critical activities (there can be more than one)</li></ul>',
  side(Wd(470, img('lrn2.png')), frag('<i>C</i>: LST 4 − 2 = 2, float 2 − 0 = 2 hours') + frag('Critical path: <i>B</i>–<i>E</i> (EST = LST all the way)')),
  'A dummy is never written in the critical path.', f'{CAM}, 14D pp. 695–699 (own words) · {EDR}, 8I pp. 626–627 (diagram)',
  cards=(kcard('LST', 'smallest out'), kcard('Float', 'LST − EST'))))
S.append(qslide('we', 'Worked example 11 · 14D (a–b)', 'Finding the critical path',
  ('<div style="font-size:17px">A project has eight activities as shown in the precedence table.' + wtab(EX11, fs=13, unit='weeks') + '</div>', '',
   plist([('a', '<b>Draw</b> an activity network for this project.'), ('b', '<b>Complete</b> the critical path analysis to calculate the EST and LST for each activity.')])),
  [('Draw', '<i>A</i>, <i>B</i>, <i>C</i> leave start; <i>F</i> after <i>B</i> and <i>D</i>; <i>G</i> after <i>E</i>, <i>F</i>'),
   ('Forward', '<i>D</i>, <i>E</i>: 3. <i>F</i>: largest of 5, 3 + 4 = 7. <i>G</i>: largest of 3 + 7, 7 + 5 = 12. <i>H</i>: 12. Finish 18'),
   ('Backward', '<i>G</i> 12, <i>H</i> 16, <i>F</i> 7, <i>E</i> 12 − 7 = 5, <i>D</i> 3, <i>A</i> smallest of 3 − 3, 5 − 3 = 0, <i>B</i> 2, <i>C</i> 4')],
  '', f'{CAM} · Example 11 (pp. 700–701)', video='Cambridge GO · Example 11 (14D Resources)', cmd=('Complete', None, 'two cells per box'),
  parts=[('a', Wd(300, img('cam11a.png'))), ('b', Wd(300, img('cam11d.png')))]))
sm(extra='sm xs')
S.append(qslide('we', 'Worked example 11 · 14D (c–h)', 'Float and the critical path',
  ('<div style="font-size:16px">(Example 11 continued: the completed network.)</div>', Wd(330, img('cam11d.png')),
   plist([('c', 'What is the earliest starting time for activity H?'), ('d', 'What is the latest starting time for activity H?'), ('e', 'What is the float time of activity H?'),
          ('f', 'Write down the critical path of this project.'), ('g', 'What is the minimum time required to complete the project?'),
          ('h', 'The person responsible for completing activity E falls sick three weeks into the project. If he will be away from work for two weeks, will this cause the entire project to be delayed?')])),
  [('Read H', 'box at the start of <i>H</i>: 12 | 16'), ('Float', 'H: 16 − 12 = 4. Zero float: <i>A</i>, <i>D</i>, <i>F</i>, <i>G</i>'), ('E', 'EST 3, LST 5: float 2 weeks = the 2-week delay')],
  '', f'{CAM} · Example 11 (pp. 701–702; Cambridge’s part d misprints “EST” for LST)', cmd=('What', None, 'read the boxes'),
  parts=[('c', '12 weeks'), ('d', '16 weeks'), ('e', 'float = 16 − 12 = 4 weeks'), ('f', '<i>A</i> – <i>D</i> – <i>F</i> – <i>G</i>'), ('g', '18 weeks'),
         ('h', 'No: <i>E</i> has a float of 2 weeks, equal to the delay, so the project is not delayed.')]))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8I WE3', 'Backward scanning',
  ('<div style="font-size:19px">Consider the following activity network with the earliest start time for each activity filled in. The estimated completion times are in hours.</div>',
   Wd(390, img('edr3q.png')), '<div style="font-size:19px"><b>Find</b> the latest start time of activity <i>B</i>.</div>'),
  [('Finish', 'LST = EST = 24'), ('G, H', '<i>G</i>: 24 − 4 = 20; <i>H</i>: 24 − 9 = 15'), ('B', 'smallest of 15 − 0 − 11 = 4 (dummy to <i>H</i>), 20 − 11 = 9')],
  'The latest start time of activity <i>B</i> is <b>4 hours</b>.', f'{EDR} · 8I Worked example 3 (pp. 626–627)', cmd=('Find', None, 'smallest value out')))
S.append(qslide('yt', 'You try · Edrolo 8I WE4', 'Critical paths and float',
  ('<div style="font-size:19px">Consider the following activity network with the earliest and latest starting time for each activity shown. The estimated completion times are in hours.</div>',
   Wd(390, img('edr4q.png')), plist([('a', '<b>Determine</b> the critical path(s) of the project.'), ('b', '<b>Determine</b> the float time of activity <i>C</i>.')])),
  [('Critical', 'EST = LST: <i>A</i>, <i>B</i>, <i>D</i>, <i>E</i>, <i>F</i>, <i>H</i>'), ('Paths', 'two routes use only these'), ('C', 'LST 10, EST 4')],
  '', f'{EDR} · 8I Worked example 4 (p. 628)', cmd=('Determine', None, 'EST = LST'),
  parts=[('a', '<i>A</i>–<i>B</i>–<i>H</i> and <i>A</i>–<i>D</i>–<i>E</i>–<i>F</i>–<i>H</i>' + Wd(260, img('edr4a.png'))), ('b', 'float = 10 − 4 = 6 hours')]))
sm()

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2020 Exam 1 Q6', 'Show what you know',
  ('<div style="font-size:19px">The activity network below shows the sequence of activities required to complete a project.<br>The number next to each activity in the network is the time it takes to complete that activity, in days.</div>',
   Wd(400, img('ex1.png')), '<div style="font-size:19px">The minimum completion time for this project, in days, is</div>'),
  [('Forward', '<i>C</i>, <i>D</i>: 4. <i>E</i>, <i>F</i>: 7. <i>H</i>, <i>I</i>: largest of 4 + 6, 7 + 4 = 11'), ('Next', '<i>K</i>: largest of 6 + 9, 11 + 3 = 15. <i>L</i>, <i>J</i>: 14'),
   ('Finish', '<i>M</i>: largest of 17, 15 = 17. Finish: largest of 20, 20, 22 = 22')],
  'The minimum completion time is 22 days: <b>E</b>.', f'VCAA 2020 Further Mathematics Exam 1 Networks and decision mathematics Q6 (examiner report: 61% correct) · {EDR} 8I Q15',
  mc=['18', '19', '20', '21', '22'], key='E', stat=('mc', 61), dis=('A', 'A (16%) takes the smallest value in at a vertex: always take the largest.')))
sm()
ZEN = '<div style="font-size:16px">At the Zenith Post Office all computer systems are to be upgraded.<br>This project involves 10 activities, <i>A</i> to <i>J</i>.<br>The directed network below shows these activities and their completion times, in hours.</div>'
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2018 Exam 2 Q3a–c', 'Show what you know',
  (ZEN, Wd(330, img('ex2.png')),
   plist([('a', 'Determine the earliest starting time, in hours, for activity <i>I</i>. <span class="muted">(1 mark)</span>'),
          ('b', 'The minimum completion time for the project is 15 hours.<br>Write down the critical path. <span class="muted">(1 mark)</span>'),
          ('c', 'Two of the activities have a float time of two hours.<br>Write down these two activities. <span class="muted">(1 mark)</span>')])),
  [('Forward', '<i>C</i>: 3; <i>D</i>, <i>E</i>: 2; <i>F</i>: largest of 7, 8 = 8; <i>G</i>: 5; <i>H</i>, <i>I</i>: largest of 9, 10 = 10'),
   ('Backward', 'finish 15: <i>J</i> 13, <i>H</i> 10, <i>I</i> 11 → <i>G</i> 5, <i>F</i> 9, <i>C</i> 5, <i>A</i> 2, <i>D</i> 3, <i>E</i> 2, <i>B</i> 0'),
   ('Float', '<i>A</i>: 2 − 0 = 2, <i>C</i>: 5 − 3 = 2')],
  '', f'VCAA 2018 Further Mathematics Exam 2 Networks and decision mathematics Q3 stem and Q3a–c (examiner report: a 64%, b 76%, c 45%) · {EDR} 8I Q16',
  stat=('avg', 62), cmd=('Write down', None, 'one answer per part'),
  parts=[('a', '10 hours'), ('b', '<i>B</i>–<i>E</i>–<i>G</i>–<i>H</i>–<i>J</i>'), ('c', '<i>A</i> and <i>C</i>')]))
sm()
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2018 Exam 2 Q3d', 'Show what you know',
  (ZEN, Wd(330, img('ex2.png')),
   '<div style="font-size:17px">d. For the next upgrade, the same project will be repeated but one extra activity will be added.<br>This activity has a duration of one hour, an earliest starting time of five hours and a latest starting time of 12 hours.<br>'
   '<b>Complete</b> the following sentence by filling in the boxes provided. <span class="muted">(1 mark)</span><br>The extra activity could be represented on the network above by a directed edge from the end of activity ☐ to the start of activity ☐.</div>'),
  [('Start', 'EST 5: only <i>E</i> finishes at 5 (2 + 3)'), ('Finish', 'LST 12 + 1 = 13 = LST of <i>J</i>')],
  'From the end of activity <b><i>E</i></b> to the start of activity <b><i>J</i></b>.', f'VCAA 2018 Further Mathematics Exam 2 Networks and decision mathematics Q3d (examiner report: 25%; Edrolo prints 45%) · {EDR} 8I Q16',
  stat=('avg', 25), cmd=('Complete', 1, 'two activity letters')))
sm()
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2021 Exam 1 Q6', 'Show what you know',
  ('<div style="font-size:19px">The directed graph below shows the sequence of activities required to complete a project.<br>The time taken to complete each activity, in hours, is also shown.</div>',
   Wd(440, img('ex3.png')), '<div style="font-size:19px">The minimum completion time for this project is 18 hours.<br>The time taken to complete activity <i>E</i> is labelled <i>x</i>.<br>The maximum value of <i>x</i> is</div>'),
  [('J', 'finish 18 → <i>J</i> must start by 18 − 7 = 11'), ('E start', 'EST of <i>E</i>: largest of 5 (<i>B</i>), 4 + 3 + 1 = 8 (<i>C</i>, <i>G</i>, <i>F</i>) = 8'),
   ('x', '8 + <i>x</i> ≤ 11 → <i>x</i> ≤ 3')],
  'The maximum value of <i>x</i> is 3: <b>B</b>.', f'VCAA 2021 Further Mathematics Exam 1 Networks and decision mathematics Q6 (examiner report: 46% correct) · {EDR} 8I Q17',
  mc=['2', '3', '4', '5', '6'], key='B', stat=('mc', 46), dis=('E', 'E (31%) uses EST of <i>E</i> = 5 from <i>B</i> only: the path through <i>C</i>, <i>G</i>, <i>F</i> is longer.')))
sm()

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 14 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '14D' and v.get('url')]))
n = assemble(S, '12MAG · 14D · Scheduling problems and critical path analysis', os.path.join(ROOT, 'lessons', '14D slides.html'))
print(n - 1, 'slides')
