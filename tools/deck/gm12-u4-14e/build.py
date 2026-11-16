"""Lesson gm12-u4-14e (14E Crashing) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/14E slides.html      Run: python3 tools/deck/gm12-u4-14e/build.py      Screenshots: python3 tools/deck/gm12-u4-14e/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; figures cropped from the sources by crop.py, fig/*.png):
- CFAT 4.14.2 (14C-14D) at the start (card).
- Do Now: VCAA 2024 NHT Exam 1 Q40 (A; NHT report gives no %) · VCAA 2023 Exam 1 Q31 (C, 74%) ·
          VCAA 2024 Exam 2 Q15 stem + Q15a (A-C-H-J; 65% full marks, average 0.7) · VCAA 2024 Exam 2 Q6 stem + Q6a (4.95%; 51%, average 0.5).
- No APK (card: crashing has no Units 1&2 prerequisite).
- Learn: Cambridge U3&4 14E pp. 708-709 (own words; 'simple crashing example' diagram cropped from p. 709) · Edrolo U3&4 8J pp. 636-638.
- Worked examples: Cambridge U3&4 Example 12 (pp. 709-711), Example 13 (pp. 711-712).
  You trys: Edrolo U3&4 8J Worked example 1 (p. 637), Worked example 2 (pp. 638-639).
- No CAS (card: none).
- Exits: VCAA 2017 Further Exam 2 N&DM Q4 stem + Q4ci,ii (17 days 35%, $4000 15%) · VCAA 2020 Further Exam 1 N&DM Q10 (A, 24%) ·
         VCAA 2021 Further Exam 2 N&DM Q4 stem + Q4c ($380 000, 9%). = Edrolo 8J Q9, Q10, Q11. Original VCAA wording; % from the examiner reports.
"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from tpl import *
from figs import *
CAM = 'Cambridge General Mathematics Units 3&amp;4'; EDR = 'Edrolo General Mathematics Units 3&amp;4'
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-14e')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'
def side(a, txt, w=280): return f'<div style="display:flex;gap:18px;align-items:center;justify-content:center">{a}<div style="font-size:19px;width:{w}px">{txt}</div></div>'
def ptbl(rows, head=('Path', 'Duration (days)'), fs=15):
    t = [f'<table class="t" style="margin:4px auto;font-size:{fs}px"><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr>']
    for r in rows: t.append('<tr>' + ''.join(f'<td style="text-align:center">{c}</td>' for c in r) + '</tr>')
    return ''.join(t) + '</table>'
NHT40 = [('A', '–'), ('B', '–'), ('C', 'A'), ('D', 'B'), ('E', 'B'), ('F', 'D'), ('G', 'D, E'), ('H', 'C, F'), ('I', 'E'), ('J', 'G, H')]

S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .R .wk li{font-size:15px}'
     '.L .q ul li{font-size:inherit!important;line-height:1.3!important}</style>']
S.append(title('14E', 'Crashing', f'{CAM} · 14E Crashing', 'gm12-u4-14e'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 14E', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>14E')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('CFAT 4.14.2', '· 14C–14D', 'var(--muted)'), ('Do Now', '· four VCAA questions', '#00838F'),
  ('Crashing', '', None), ('Worked example 12', '→ You try', None), ('Crashing with cost', '', None),
  ('Worked example 13', '→ You try', None), ('Exit tasks', '· three VCAA questions', 'var(--exit)'), ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Crashing', 'reducing the duration of activities to reduce the completion time of a project'),
  ('Critical path', 'the longest path; only crashing critical activities shortens the project'),
  ('New critical path', 'another path can become just as long: then it must be crashed too'),
  ('Minimum cost', 'crash the cheapest activities that shorten ALL critical paths')],
  [('Path length', 'path length = sum of its durations', 'list every path start → finish'),
   ('Completion time', 'minimum completion time = longest path', 'after crashing: recheck every path'),
   ('Crash cost', 'cost = Σ (days reduced × cost per day)', 'stop crashing once it no longer helps')],
  f'{CAM}, 14E pp. 708–712; {EDR}, 8J pp. 636–639; Study Design: use of crashing to reduce the completion time of the project or task being modelled'))
S.append(cfat('CFAT 4.14.2', 'Activity networks, precedence tables and critical path analysis', '14C–14D', 12, 'Start of the 14E lesson · about 20 min · CAS and bound reference allowed'))

# ================= Do Now
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2024 NHT Exam 1 Q40', 'Review of 14C–14D (precedence and EST)',
  ('<div style="font-size:16px">A project has 10 activities, labelled <i>A</i> to <i>J</i>. The table below shows the immediate predecessor(s) for each activity. Each activity has a duration of at least one day.</div>',
   ptab(NHT40, fs=13, head=('Activity', 'Immediate predecessor(s)')), '<div style="font-size:16px">Which one of the following statements about this project is <b>not</b> true?</div>'),
  [('H needs', '<i>C</i> (after <i>A</i>) and <i>F</i> (after <i>D</i>, after <i>B</i>)'), ('At least', '<i>B</i>, <i>D</i>, <i>F</i> take at least 1 day each: EST of <i>H</i> ≥ 3'),
   ('So', 'two days is impossible')],
  'Statement <b>A</b> is not true.', 'VCAA 2024 NHT General Mathematics Exam 1 Q40 (the NHT report gives no % correct)',
  mc=['The earliest starting time of activity <i>H</i> could be two days.', 'In the network for this project, there would be a dummy activity from the end of activity <i>D</i> to the start of activity <i>G</i>.',
      'One of the paths through the network of this project is <i>BDGJ</i>.', 'The latest starting time of activity <i>E</i> could be three days.', 'The network for this project would require two dummy activities.'],
  key='A', cmd=('Which', 1, 'NOT true')))
sm(extra='sm xs')
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2023 Exam 1 Q31', 'Review of 11E (Leslie matrices)',
  ('<div style="font-size:18px">A species of bird has a life span of three years.<br>The females in this species do not reproduce in their first year but produce an average of four female offspring in their second year, and three in their third year.<br>The Leslie matrix, <i>L</i>, below is used to model the female population distribution of this species of bird.</div>',
   Wd(220, img('dn2.png')), '<div style="font-size:18px">The element in the second row, first column states that on average 20% of this population will</div>'),
  [('Row 2', 'the sub-diagonal holds survival rates'), ('Column 1 → row 2', 'from year 1 into year 2')],
  'On average 20% survive into their second year: <b>C</b>.', 'VCAA 2023 General Mathematics Exam 1 Q31 (examiner report: 74% correct)',
  mc=['be female.', 'never reproduce.', 'survive into their second year.', 'produce offspring in their first year.', 'live for the entire lifespan of three years.'],
  key='C', stat=('mc', 74), dis=('D', 'D (10%) reads the first column as reproduction: births sit in the FIRST ROW.')))
sm()
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2024 Exam 2 Q15a', 'Review of 14D (critical path)',
  ('<div style="font-size:17px">An upgrade to the supermarket requires the completion of 11 activities, <i>A</i> to <i>K</i>.<br>The directed network below shows these activities and their completion time, in weeks.<br>The minimum completion time for the project is 29 weeks.</div>',
   Wd(470, img('dn3.png')), '<div style="font-size:17px">a. Write down the critical path. <span class="muted">(1 mark)</span></div>'),
  [('Paths', '<i>A</i>–<i>C</i>–<i>G</i> 28 · <i>A</i>–<i>D</i>–<i>I</i>–<i>J</i> 28 · <i>B</i>–<i>F</i>–<i>K</i> 27 · <i>B</i>–<i>E</i>–<i>I</i>–<i>J</i> 26'),
   ('29 weeks', '<i>A</i>–<i>C</i>–<i>H</i>–<i>J</i>: 9 + 7 + 8 + 5 = 29')],
  'The critical path is <b><i>A</i>–<i>C</i>–<i>H</i>–<i>J</i></b>.', 'VCAA 2024 General Mathematics Exam 2 Q15 stem and Q15a (examiner report: 65% full marks, average 0.7)',
  stat=('avg', 65), cmd=('Write down', 1, 'the longest path')))
sm()
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2024 Exam 2 Q6a', 'Review of 7F (effective interest rates)',
  ('<div style="font-size:19px">Emi invested profits of $10 000 into a savings account that earns interest compounding fortnightly, for one year.<br>The effective interest rate, rounded to two decimal places, is 5.07%.<br>Assume that there are exactly 26 fortnights in a year.</div>', '',
   '<div style="font-size:19px">a. What is the nominal percentage rate of interest for the account?<br>Round your answer to two decimal places. <span class="muted">(1 mark)</span></div>'),
  [('Formula', 'r<sub>eff</sub> = ((1 + r/(100 × 26))<sup>26</sup> − 1) × 100'), ('Solve on CAS', '5.07 = ((1 + r/2600)<sup>26</sup> − 1) × 100 → r = 4.950…')],
  'The nominal rate is <b>4.95%</b> per annum.', 'VCAA 2024 General Mathematics Exam 2 Q6 stem and Q6a (examiner report: 51% full marks, average 0.5)',
  stat=('avg', 51), cmd=('What', 1, 'a percentage, 2 d.p.')))
sm()

# ================= Learn 1
S.append(learn('Learn · 14E', 'Crashing',
  '<h4>Shorten the critical path</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>crashing</b> = reducing activity times (more staff, better equipment) to finish sooner</li>'
  '<li>only <b>critical</b> activities matter: others already have float</li>'
  '<li>list every path and its length; the longest is critical</li>'
  '<li>crash, then <b>recheck every path</b>: another path may become critical</li></ul>',
  side(Wd(420, img('lrn.png')), frag('Critical path <i>D</i>–<i>E</i>: 13 hours') + frag('Crash <i>D</i> to 4 hours → 11 hours') + frag('Crashing <i>A</i>, <i>B</i> or <i>C</i>: no change')),
  'Crashing past the float of another path only moves the problem.', f'{CAM}, 14E pp. 708–709 (own words, diagram p. 709) · {EDR}, 8J p. 636',
  cards=(kcard('Completion time', 'longest path'), kcard('New critical path', 'recheck every path'))))
S.append(qslide('we', 'Worked example 12 · 14E', 'Crashing one activity with cost',
  ('<div style="font-size:17px">The directed network below shows the sequence of 8 activities that are needed to complete a project. The time, in days, that it takes to complete each activity is also shown.</div>',
   Wd(360, img('cam12.png')), plist([('a', 'Write down the critical path for this project.'), ('b', 'What is the minimum completion time for the project?'),
     ('c', 'Activity <i>F</i> can be reduced by a maximum of 3 days at a cost of $100 per day.<br>What is the new minimum completion time for the project?'),
     ('d', 'What is the minimum cost that will achieve the greatest reduction in time taken to complete the project?')])),
  [('Paths', '<i>A</i>–<i>D</i>–<i>H</i> 14 · <i>B</i>–<i>E</i>–<i>G</i> 13 · <i>C</i>–<i>F</i>–<i>G</i> 16'),
   ('Crash F by 3', '<i>C</i>–<i>F</i>–<i>G</i> → 13, but <i>A</i>–<i>D</i>–<i>H</i> is still 14'),
   ('Only 2 needed', 'crash <i>F</i> by 2: two critical paths of 14 days; 2 × $100')],
  '', f'{CAM} · Example 12 (pp. 709–711)', video='Cambridge GO · Example 12 (14E Resources)', cmd=('Write down', None, 'list every path'),
  parts=[('a', '<i>C</i> – <i>F</i> – <i>G</i>'), ('b', '16 days'), ('c', '14 days'), ('d', '$200 (reduce <i>F</i> by 2 days)')]))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8J WE1', 'Crashing an activity network',
  ('<div style="font-size:16px">Claire is part of a study group that is planning to create revision notes on chapter 8 of this textbook. The activity network shows all the lessons within chapter 8. All values are in hours.</div>',
   Wd(360, img('edr1q.png')), '<div style="font-size:16px">Claire asks her friend Klare to help the study group. With Klare’s assistance, the study group can reduce the time it will take to complete revision notes for lesson <i>C</i> by 2 hours and lessons <i>B</i>, <i>G</i> and <i>I</i> by 3 hours.</div>'
   + plist([('a', 'What is the minimum amount of time it will take the group to complete revision notes for chapter 8 with Klare’s help?'), ('b', 'What is the critical path of the project?')])),
  [('Reduce', '<i>B</i>: 4 − 3 = 1 · <i>C</i>: 3 − 2 = 1 · <i>G</i>: 9 − 3 = 6 · <i>I</i>: 11 − 3 = 8'), ('Forward scan', 'EST at finish = 19'),
   ('Backward scan', 'EST = LST along <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i>, <i>E</i>')],
  '', f'{EDR} · 8J Worked example 1 (p. 637)', cmd=('What', None, 'reduce, then rescan'),
  parts=[('a', '19 hours ' + Wd(300, img('edr1a.png'))), ('b', '<i>A</i>–<i>B</i>–<i>C</i>–<i>D</i>–<i>E</i> ' + Wd(300, img('edr1b.png')))]))
sm(extra='sm xs')

# ================= Learn 2
S.append(learn('Learn · 14E', 'Crashing with cost',
  '<h4>Most time saved for the least money</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>crash everything allowed by the maximum: find the <b>new</b> minimum time</li>'
  '<li>then undo what isn’t needed: every path only has to get down to that time</li>'
  '<li>prefer the <b>cheaper</b> activity; an activity on two long paths can be worth more</li>'
  '<li>cost = days reduced × cost per day, added up</li></ul>',
  side(Wd(360, img('cam12.png')), frag('<i>F</i> by 3 days: 16 → 13, but <i>A</i>–<i>D</i>–<i>H</i> is 14') + frag('so only 2 days are worth paying for: $200'), w=300),
  'Never pay to shorten a path below the new critical path.', f'{CAM}, 14E pp. 709–712 (own words) · {EDR}, 8J p. 638',
  cards=(kcard('Crash cost', 'days × cost'), kcard('Minimum cost', 'cheapest that helps'))))
S.append(qslide('we', 'Worked example 13 · 14E', 'Crashing multiple activities with cost',
  ('<div style="font-size:15px">The directed network below shows the sequence of 9 activities that are needed to complete a project. The time, in days, that it takes to complete each activity is also shown.</div>',
   f'<div style="display:flex;gap:10px;align-items:center">{Wd(330, img("cam13.png"))}{Wd(140, img("cam13t.png"))}</div>',
   '<div style="font-size:15px">The minimum completion time for the project is 28 days. It is possible to reduce the completion time for activities <i>B</i>, <i>E</i>, <i>G</i>, <i>H</i> and <i>I</i>. The completion time for each of these five activities can be reduced by a maximum of two days.</div>'
   + plist([('a', 'What is the new minimum completion time, in days, that the project could take?'),
            ('b', 'The reduction in completion time for each of these five activities will incur an additional cost. The table opposite shows the five activities that can have their completion times reduced and the associated daily cost, in dollars.<br>What is the minimum cost that will achieve the greatest reduction in time taken to complete the project?')])),
  [('Paths', ptbl([('A–C–E', 27, 25), ('A–F–H', 19, 17), ('B–D–F–H', 28, 24), ('B–G–I', 28, 22)], ('Path', 'Days', 'Max crash'), 13)),
   ('A–C–E', 'only <i>E</i> can shorten it: <i>E</i> by 2 → 25 days'),
   ('B–D–F–H', '28 → 25: <i>B</i> by 2 (also helps <i>B</i>–<i>G</i>–<i>I</i>), <i>H</i> by 1'), ('B–G–I', '28 − 2 = 26: cheaper of <i>G</i>, <i>I</i>: <i>G</i> by 1')],
  '', f'{CAM} · Example 13 (pp. 711–712)', video='Cambridge GO · Example 13 (14E Resources)', cmd=('What', None, 'crash to the new critical path'),
  parts=[('a', '25 days (new critical path <i>A</i>–<i>C</i>–<i>E</i>)'), ('b', '2000 × 2 + 1500 × 2 + 900 + 700 = <b>$8600</b>')]))
sm(extra='sm xs')
S.append(qslide('yt', 'You try · Edrolo 8J WE2', 'Crashing with restrictions',
  ('<div style="font-size:16px">A landscaping company is preparing to renovate and landscape a garden. The activities that must be completed for the project are represented in the following activity network. All values are in days.</div>',
   Wd(380, img('edr2q.png')), '<div style="font-size:16px">The manager is willing to employ more staff in order to speed up the completion of the project.<br>The completion times of activities <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i> can each be reduced by $150 per day, for up to two days.</div>'
   + plist([('a', 'What is the minimum cost of reducing the minimum completion time by as much as possible?'),
            ('b', 'On top of the current reductions, the manager may also be able to further reduce either the duration of activity <i>A</i> by 1 day for $140, the duration of activity <i>G</i> by 1 day for $175 or the duration of activity <i>I</i> by 1 day for $225. Which activity should the manager reduce the duration of?')])),
  [('Reduce all by 2', 'scan: finish 27; <i>A</i>, <i>C</i>, <i>D</i> float 0, <i>B</i> and <i>E</i> float 3'), ('Undo', '<i>B</i> + <i>E</i> only need 1 day between them'),
   ('Cost', '<i>A</i>, <i>C</i>, <i>D</i> by 2 + <i>B</i> by 1 = 7 days × $150'), ('b', 'critical paths <i>A</i>–<i>C</i>–<i>D</i>–<i>G</i>–<i>I</i> and <i>B</i>–<i>E</i>–<i>G</i>–<i>I</i>: <i>G</i>, <i>I</i> on both; <i>G</i> cheaper')],
  '', f'{EDR} · 8J Worked example 2 (pp. 638–639)', cmd=('What', None, 'pay only for days that help'),
  parts=[('a', '$1050 ' + Wd(300, img('edr2a.png'))), ('b', 'Activity <i>G</i> ' + Wd(300, img('edr2b.png')))]))
sm(extra='sm xs')

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 3 · VCAA 2017 Exam 2 Q4c', 'Show what you know',
  ('<div style="font-size:16px">The rides at the theme park are set up at the beginning of each holiday season.<br>This project involves activities <i>A</i> to <i>O</i>.<br>The directed network below shows these activities and their completion times in days.</div>',
   Wd(330, img('ex1.png')), '<div style="font-size:16px">[The minimum completion time for the project is 19 days.]<br>c. The project could finish earlier if some activities were crashed.<br>Six activities, <i>B</i>, <i>D</i>, <i>G</i>, <i>I</i>, <i>J</i> and <i>L</i>, can all be reduced by one day.<br>The cost of this crashing is $1000 per activity.</div>'
   + plist([('i', 'What is the minimum number of days in which the project could now be completed? <span class="muted">(1 mark)</span>'), ('ii', 'What is the minimum cost of completing the project in this time? <span class="muted">(1 mark)</span>')])),
  [('Critical', '<i>A</i>–<i>E</i>–<i>J</i>–<i>L</i>–<i>N</i> and <i>A</i>–<i>E</i>–<i>I</i>–<i>L</i>–<i>N</i> (dummy): 19'),
   ('Crash', '<i>L</i>, <i>J</i>, <i>I</i>: both → 17'), ('New 18s', '<i>A</i>–<i>C</i>–<i>G</i>–<i>N</i> 18 → crash <i>G</i>: 17 · <i>A</i>–<i>E</i>–<i>J</i>–<i>O</i> 18 − 1 (<i>J</i>) = 17')],
  '', f'VCAA 2017 Further Mathematics Exam 2 Networks and decision mathematics Q4 stem and Q4ci, ii (examiner report: i 35%, ii 15%) · {EDR} 8J Q9',
  stat=('avg', 25), cmd=('What', None, 'recheck every path'),
  parts=[('i', '17 days'), ('ii', '<i>G</i>, <i>I</i>, <i>J</i>, <i>L</i>: 4 × $1000 = $4000')]))
sm(extra='sm xs')
S.append(qslide('ex', 'Exit task 2 of 3 · VCAA 2020 Exam 1 Q10', 'Show what you know',
  ('<div style="font-size:15px">The directed network below shows the sequence of activities, <i>A</i> to <i>I</i>, that is required to complete an office renovation.<br>The time taken to complete each activity, in weeks, is also shown.</div>',
   Wd(400, img('ex2.png')), '<div style="font-size:15px">The project manager would like to complete the office renovation in less time.<br>The project manager asks all the workers assigned to activity <i>H</i> to also work on activity <i>F</i>.<br>This will reduce the completion time of activity <i>F</i> to three weeks.<br>The workers assigned to activity <i>H</i> cannot work on both activity <i>H</i> and activity <i>F</i> at the same time.<br>No other activity times will be changed.<br>This change to the network will result in a change to the completion time of the office renovation.<br>Which one of the following is correct?</div>'),
  [('Now', 'critical <i>A</i>–<i>C</i>–<i>E</i>–<i>F</i>–<i>G</i>–<i>I</i>: 25 weeks'), ('F first', '<i>H</i> must wait for <i>F</i>: <i>A</i>–<i>C</i>–<i>E</i>–<i>F</i>–dummy–<i>H</i>–<i>I</i> = 2 + 5 + 3 + 3 + 6 + 5 = 24'),
   ('H first', '<i>F</i> waits for <i>H</i>: longer, not shorter')],
  'The completion time is reduced by one week if <i>F</i> is completed first: <b>A</b>.', f'VCAA 2020 Further Mathematics Exam 1 Networks and decision mathematics Q10 (examiner report: 24% correct) · {EDR} 8J Q10',
  mc=['The completion time will be reduced by one week if activity <i>F</i> is completed before activity <i>H</i> is started.', 'The completion time will be reduced by three weeks if activity <i>F</i> is completed before activity <i>H</i> is started.',
      'The completion time will be reduced by one week if activity <i>H</i> is completed before activity <i>F</i> is started.', 'The completion time will be reduced by three weeks if activity <i>H</i> is completed before activity <i>F</i> is started.',
      'The completion time will be increased by three weeks if activity <i>H</i> is completed before activity <i>F</i> is started.'],
  key='A', stat=('mc', 24), dis=('B', 'B (36%) subtracts the full 3 weeks saved on <i>F</i>: <i>H</i> now has to follow <i>F</i>.')))
sm(extra='sm xs')
S.append(qslide('ex', 'Exit task 3 of 3 · VCAA 2021 Exam 2 Q4c', 'Show what you know',
  ('<div style="font-size:15px">Roadworks planned by the local council require 13 activities to be completed.<br>The network below shows these 13 activities and their completion times in weeks.</div>',
   f'<div style="display:flex;gap:10px;align-items:center">{Wd(360, img("ex3.png"))}{Wd(130, img("ex3t.png"))}</div>', f'<div><div style="font-size:15px">c. It is possible to reduce the completion time for activities <i>A</i>, <i>E</i>, <i>F</i>, <i>L</i> and <i>K</i>.<br>The reduction in completion time for each of these five activities will incur an additional cost.<br>The table below shows the five activities that can have their completion time reduced and the associated weekly cost, in dollars.<br>The completion time for each of these five activities can be reduced by a maximum of two weeks.<br>The overall completion time for the roadworks can be reduced to 16 weeks.<br>What is the minimum cost, in dollars, of this change in completion time? <span class="muted">(1 mark)</span></div></div>'),
  [('Paths', '<i>A</i>–<i>E</i>–<i>H</i>–<i>L</i>–<i>M</i>, <i>A</i>–<i>D</i>–<i>G</i>–<i>L</i>–<i>M</i>: 19 · <i>B</i>–<i>C</i>–… : 18 · <i>A</i>–<i>E</i>–<i>J</i>–<i>K</i>: 17'),
   ('L by 2', 'both 19s → 17; the <i>B</i>–<i>C</i> paths → 16'), ('A by 1', 'every <i>A</i> path → 16 (incl. <i>A</i>–<i>E</i>–<i>J</i>–<i>K</i>)'),
   ('Cost', '2 × 120 000 + 140 000')],
  'The minimum cost is <b>$380 000</b>.', f'VCAA 2021 Further Mathematics Exam 2 Networks and decision mathematics Q4 stem and Q4c (examiner report: 9%) · {EDR} 8J Q11',
  stat=('avg', 9), cmd=('What', 1, 'a cost in dollars')))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 14 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '14E' and v.get('url')]))
n = assemble(S, '12MAG · 14E · Crashing', os.path.join(ROOT, 'lessons', '14E slides.html'))
print(n - 1, 'slides')
