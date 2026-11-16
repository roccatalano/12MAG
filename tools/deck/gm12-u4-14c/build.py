"""Lesson gm12-u4-14c (14C Precedence tables and activity networks) slides, built from the slide templates (tools/deck/tpl/tpl.py).
Output: lessons/14C slides.html      Run: python3 tools/deck/gm12-u4-14c/build.py      Screenshots: python3 tools/deck/gm12-u4-14c/shoot.py

Sources (read from the PDFs on G: 16 Nov 2026; question text verbatim; figures cropped from the sources by crop.py, fig/*.png):
- CFAT 4.14.1 (14A-14B) at the start (card).
- Do Now: VCAA 2025 Exam 1 Q39 (B, 71%) · VCAA 2024 Exam 1 Q28 (C, 84%) · VCAA 2024 NHT Exam 2 Q14 stem + Q14a (Ben; NHT report: no %) ·
          VCAA 2025 Exam 2 Q8 stem + Q8b (20%; average 0.7/1, 70%).
- APK: VCAA 2018 Further Exam 1 N&DM Q4 (original wording; = Edrolo U1&2 7D Q12, adapted there; D, 88% from the 2018 E1 report).
- Learn: Cambridge U3&4 14C pp. 685-688 (own words; Cambridge's dummy diagram p. 687) · Edrolo U3&4 8H pp. 608-612.
- Worked examples: Cambridge U3&4 Examples 7 (pp. 685-686), 8 (pp. 687-688), 9 (p. 688).
  You trys: Edrolo U3&4 8H Worked examples 2 (pp. 609-610), 4 (pp. 612-613; parts a and b), 3 (pp. 610-611).
- No CAS (card: none).
- Exits: VCAA 2017 Further Exam 2 N&DM Q4 stem + Q4a (= Edrolo 8H Q14; D and E; 67%) ·
         VCAA 2020 Further Exam 2 N&DM Q5 stem + Q5a (= Edrolo 8H Q15; B to C; 26%). Original VCAA wording; % from the examiner reports.
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
CARD = _card(json.load(open(os.path.join(ROOT, 'planner', 'unit-plan.json'))), 'gm12-u4-14c')
def Wd(px, inner): return f'<div style="width:{px}px;max-width:100%;margin:0 auto">{inner}</div>'
def sm(i=-1, extra='sm'): S[i] = S[i].replace('<section class="slide T ', f'<section class="slide T {extra} ', 1)
def frag(t, a=''): return f'<div class="frag" style="font-size:20px;text-align:center;line-height:1.3" {a}>{t}</div>'
def side(tab, txt, w=260): return f'<div style="display:flex;gap:18px;align-items:center;justify-content:center">{tab}<div style="font-size:19px;width:{w}px">{txt}</div></div>'

EX7 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'C'), ('G', 'D'), ('H', 'E, F, G')]
EX8 = [('A', '–'), ('B', '–'), ('C', 'A'), ('D', 'B'), ('E', 'C, D'), ('F', 'C'), ('G', 'E, F')]
EX9 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'C'), ('F', 'D, C'), ('G', 'D, C'), ('H', 'E, F'), ('I', 'G'), ('J', 'G, H')]
WE2 = [('A', '–'), ('B', '–'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'B'), ('G', 'D, E'), ('H', 'C, G'), ('I', 'F, H')]
WE3 = [('A', '–'), ('B', '–'), ('C', '–'), ('D', 'B'), ('E', 'A, D'), ('F', 'B'), ('G', 'C'), ('H', 'E'), ('I', 'F, G')]
WE4 = [('A', '–'), ('B', 'A'), ('C', 'A'), ('D', 'A'), ('E', 'B'), ('F', 'C'), ('G', 'D'), ('H', 'E, F'), ('I', 'C, G')]
DUM = [('A', '–'), ('B', '–'), ('C', '–'), ('D', 'A, B'), ('E', 'B, C')]
CR = [('A', '0', '2', '–'), ('B', '0', '5', '–'), ('C', '5', '', 'A, B'), ('D', '7', '7', 'C'), ('E', '7', '9', 'C'), ('F', '5', '3', 'B'), ('G', '14', '4', 'D'), ('H', '8', '9', 'F'), ('I', '18', '2', 'E, G, H')]
S = ['<style>.sm .L .q{font-size:18px}.sm .L .mc>div{font-size:16px;padding-top:1px;padding-bottom:1px}.xs .R .wk li{font-size:15px}'
     '.L .q ul li{font-size:inherit!important;line-height:1.3!important}.cmx td,.cmx th{line-height:1.25}</style>']
S.append(title('14C', 'Precedence tables and activity networks', f'{CAM} · 14C Precedence tables and activity networks', 'gm12-u4-14c'))
S[-1] = S[-1].replace('Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson 14C', 'Unit 4<i></i>AOS 4 Networks and decision mathematics<i></i>14C')
LI = [x for g_ in CARD['learningObjectives'] for x in g_['items']]
SC_ = [x for g_ in CARD['successCriteria'] for x in g_['items']]
S.append(today(LI, SC_, [('CFAT 4.14.1', '· 14A–14B', 'var(--muted)'), ('Do Now', '· four VCAA questions', '#00838F'), ('APK', '· one Year 11 question', 'var(--apk)'),
  ('Activity networks', '', None), ('Worked example 7', '→ You try', None), ('Dummy activities', '', None), ('Worked example 8', '→ You try', None),
  ('Worked example 9', '→ You try', None), ('Exit tasks', '· two VCAA questions', 'var(--exit)'), ('Check-in and coursework', '', 'var(--muted)')]))
S.append(keys([
  ('Immediate predecessor', 'an activity that must be finished just before another can start'), ('Precedence table', 'each activity and its immediate predecessors'),
  ('Activity network', 'directed graph: edges = activities, vertices = where they start and finish'), ('Start / finish', 'the only labelled vertices; one of each'),
  ('Dummy activity', 'dashed edge, takes no time; not a real activity'), ('Path', 'a walk with no repeated vertices or edges (Year 11)')],
  [('Start', 'no immediate predecessors → leave the start vertex', 'read the “–” rows'),
   ('Finish', 'not an immediate predecessor of anything → go to finish', 'missing from column 2'),
   ('Dummy', 'two activities share SOME (not all) predecessors', 'from the end of the shared one → to the start of the one with extra')],
  f'{CAM}, 14C pp. 685–688; {EDR}, 8H pp. 608–612; Study Design: construction of an activity network from a precedence table (or equivalent) including the use of dummy activities where necessary'))
S.append(cfat('CFAT 4.14.1', 'Flow problems and matching problems', '14A–14B', 13, 'Start of the 14C lesson · about 20 min · CAS and bound reference allowed'))

# ================= Do Now
def site(rows): return cm(['Site 1', 'Site 2', 'Site 3', 'Site 4'], rows, fs=13)
def cm(cols, rows, fs=15):
    return (f'<table class="cmx" style="border-collapse:collapse;margin:2px auto;font-size:{fs}px"><tr><th></th>' + ''.join(f'<th style="padding:0 6px;color:#0a7a8a">{c}</th>' for c in cols) + '</tr>'
            + ''.join(f'<tr><th style="padding:0 6px;color:#0a7a8a">{n}</th>' + ''.join(f'<td style="border:1px solid #bbb;padding:0 6px;text-align:center">{v}</td>' for v in vs) + '</tr>' for n, vs in rows) + '</table>')
OPT = [[('P', ['5800', '0', '13 150', '8700']), ('Q', ['4500', '0', '15 000', '9450']), ('R', ['8600', '0', '16 900', '12 200']), ('S', ['10 438', '0', '14 150', '9000'])],
       [('P', ['1300', '0', '0', '0']), ('Q', ['0', '0', '1850', '750']), ('R', ['4100', '0', '3750', '3500']), ('S', ['5938', '0', '1000', '300'])],
       [('P', ['900', '600', '0', '300']), ('Q', ['0', '1000', '2250', '1450']), ('R', ['6500', '3400', '6550', '6600']), ('S', ['4938', '0', '400', '0'])],
       [('P', ['900', '600', '0', '300']), ('Q', ['0', '1000', '2250', '1450']), ('R', ['3100', '0', '3150', '3200']), ('S', ['4938', '0', '400', '0'])]]
S.append(qslide('dn', 'Do Now 1 of 4 · VCAA 2025 Exam 1 Q39', 'Review of 14B (Hungarian algorithm)',
  '<div style="font-size:14px">Four contractors, P, Q, R and S, have been hired to complete work at one of four sites.<br>Each contractor will be allocated to a different site.<br>The cost for each contractor to complete the works, in dollars ($), is shown in the table below.'
  + cm(['Site 1', 'Site 2', 'Site 3', 'Site 4'], [('P', ['15 400', '9600', '22 750', '18 300']), ('Q', ['14 500', '10 000', '25 000', '19 450']), ('R', ['21 000', '12 400', '29 300', '24 600']), ('S', ['19 438', '9000', '23 150', '18 000'])], fs=13)
  + 'The Hungarian algorithm is used to determine the minimum cost to complete the works.<br>Martha, the project manager, completes two steps of the Hungarian algorithm, as follows.'
  '<ul style="margin-left:20px"><li>First, she subtracts the minimum entry in each row from each element in that row to obtain a new table of values.</li>'
  '<li>Then, using this new table, she subtracts the minimum entry in each column from each element in that column.</li></ul>'
  'Which one of the following tables correctly displays the results after these two steps are completed?</div>',
  [('Rows', 'subtract 9600, 10 000, 12 400, 9000: Site 2 column becomes all 0'),
   ('Columns', 'column minimums 4500, 0, 13 150, 8700'), ('Check P', '5800 − 4500 = 1300, 13 150 − 13 150 = 0, 8700 − 8700 = 0')],
  'The table is option <b>B</b>.', 'VCAA 2025 General Mathematics Exam 1 Q39 (examiner report: 71% correct)',
  mc=[site(o) for o in OPT], key='B', stat=('mc', 71), dis=('A', 'A stops after the row step: the column step is still to come.')))
sm(extra='sm xs')
S[-1] = S[-1].replace('class="mc"', 'class="mc" style="display:grid;grid-template-columns:1fr 1fr;gap:2px"', 1)
S.append(qslide('dn', 'Do Now 2 of 4 · VCAA 2024 Exam 1 Q28', 'Review of 10D (matrix multiplication)',
  '<div style="font-size:20px">A primary school is hosting a sports day.<br>Students represent one of four teams: blue (<i>B</i>), green (<i>G</i>), red (<i>R</i>) or yellow (<i>Y</i>).<br>'
  'Students compete in one of three sports: football (<i>F</i>), netball (<i>N</i>) or tennis (<i>T</i>).<br>Matrix <i>W</i> shows the number of students competing in each sport and the team they represent.'
  '<div style="text-align:center;margin:6px">' + cm(['<i>B</i>', '<i>G</i>', '<i>R</i>', '<i>Y</i>'], [('<i>F</i>', [85, 60, 64, 71]), ('<i>N</i>', [62, 74, 80, 64]), ('<i>T</i>', [63, 76, 66, 75])], fs=18).replace('<th></th>', '<th><i>W</i> =</th>', 1) + '</div>'
  'Matrix <i>W</i> is multiplied by the matrix [1 1 1 1]<sup>T</sup> (a column of four 1s) to produce matrix <i>X</i>.<br>Element <i>x</i><sub>31</sub> indicates that</div>',
  [('Order', '(3 × 4)(4 × 1) = 3 × 1: one total per sport'), ('Row 3', 'tennis: 63 + 76 + 66 + 75 = 280')],
  '280 students compete in tennis: <b>C</b>.', 'VCAA 2024 General Mathematics Exam 1 Q28 (examiner report: 84% correct; the column matrix is printed upright in the paper)',
  mc=['210 students represent the blue team.', '210 students compete in netball.', '280 students compete in tennis.', '280 students compete in football.'], key='C', stat=('mc', 84),
  dis=('D', 'row 3 is tennis, not football: x<sub>31</sub> = row 3, column 1.')))
sm()
S.append(qslide('dn', 'Do Now 3 of 4 · VCAA 2024 NHT Exam 2 Q14a', 'Review of 14B (bipartite graphs)',
  ('<div style="font-size:18px">Andrea, Ben, Cathy, Delani and Elliot are a group of friends.<br>They are visiting a theme park that has six attractions: a Carousel, a Ferris wheel, a Mini-coaster, a Tilt-A-Whirl, Bumper cars and a Roller-coaster.<br>'
   'The following bipartite graph illustrates the attractions each friend plans to visit.</div>', Wd(420, img('dn3.png')),
   '<div style="font-size:18px">a. Which friend plans to visit the most attractions? <span class="muted">(1 mark)</span></div>'),
  [('Count edges', 'Andrea 1 · Ben 3 · Cathy 1 · Delani 2 · Elliot 2')],
  '<b>Ben</b> plans to visit the most attractions (3).', 'VCAA 2024 (NHT) General Mathematics Exam 2 Q14 stem and Q14a (NHT report: no % given)', cmd=('Which', 1, 'name the friend')))
sm()
S.append(qslide('dn', 'Do Now 4 of 4 · VCAA 2025 Exam 2 Q8b', 'Review of 7B (flat rate depreciation)',
  ('<div style="font-size:18px">Declan depreciates the value of his lighting equipment using flat rate depreciation.<br>The graph below shows the value, in dollars, of the lighting equipment, <i>V<sub>n</sub></i>, after <i>n</i> years.</div>',
   Wd(380, img('dn4.png')), '<div style="font-size:18px">b. What is the annual flat rate depreciation percentage applied to the lighting equipment? <span class="muted">(1 mark)</span></div>'),
  [('Each year', '$40 000 → $32 000: falls $8000'), ('Percentage', '8000 ÷ 40 000 × 100 = 20%')],
  'The flat rate depreciation is <b>20%</b> of the initial value per year.', 'VCAA 2025 General Mathematics Exam 2 Q8 stem and Q8b (examiner report: average 0.7/1)', stat=('avg', 70), cmd=('What', 1, 'a percentage of the initial value')))
sm()

# ================= APK
S.append(qslide('apk', 'APK · VCAA 2018 Exam 1 Q4', 'Paths (Year 11)',
  ('<div style="font-size:21px">Consider the graph below.</div>', Wd(330, img('apk.png')), '<div style="font-size:21px">Which one of the following is <b>not</b> a path for this graph?</div>'),
  [('Path', 'every step must use an edge; no vertex repeated'), ('Check D', 'P–T ✓, T–Q ✓, Q–S ✓, S–R: no edge')],
  '<i>PTQSR</i> is not a path: <b>D</b>.', f'VCAA 2018 Further Mathematics Exam 1 Networks and decision mathematics Q4 (examiner report: 88% correct) · {EDR12} 7D Q12 (adapted there)',
  mc=['<i>PRQTS</i>', '<i>PQRTS</i>', '<i>PRTSQ</i>', '<i>PTQSR</i>', '<i>PTRQS</i>'], key='D', stat=('mc', 88)))
sm()

# ================= Learn 1
S.append(learn('Learn · 14C', 'Precedence tables and activity networks',
  '<h4>Edges are activities</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li><b>immediate predecessor</b>: must be finished just before the next activity starts</li><li><b>precedence table</b>: each activity and its immediate predecessors</li>'
  '<li>in the <b>activity network</b> each activity is a directed edge; only start and finish are labelled</li>'
  '<li>“–” activities leave the start; activities that are nobody’s predecessor go to the finish</li></ul>',
  side(ptab(EX7, fs=13), frag('Read each row as: <i>H</i> can start once <i>E</i>, <i>F</i> and <i>G</i> are all finished') + frag('So <i>E</i>, <i>F</i>, <i>G</i> all end at the vertex where <i>H</i> starts')),
  'Work from the finish backwards, or from the start forwards: both work.', f'{CAM}, 14C pp. 685–686 (own words) · {EDR}, 8H pp. 608–609',
  cards=(kcard('Immediate predecessor', 'finished just before'), kcard('Activity network', 'edges = activities'))))
S.append(qslide('we', 'Worked example 7 · 14C', 'Drawing an activity network',
  '<div style="font-size:20px"><b>Draw</b> an activity network from the precedence table shown below.' + ptab(EX7, fs=17) + '</div>',
  [('Finish', '<i>H</i> is no one’s predecessor → <i>H</i> leads to finish'), ('Into H', '<i>E</i>, <i>F</i>, <i>G</i> all end where <i>H</i> starts'),
   ('Paths', '<i>A</i>–<i>B</i>–<i>E</i>, <i>A</i>–<i>C</i>–<i>F</i>, <i>A</i>–<i>D</i>–<i>G</i>'), ('Start', '<i>A</i> has no predecessor → leaves start')],
  '', f'{CAM} · Example 7 (pp. 685–686)', video='Cambridge GO · Example 7 (14C Resources)', cmd=('Draw', None, 'one edge per activity'), afig=Wd(330, img('cam7.png'))))
S.append(qslide('yt', 'You try · Edrolo 8H WE2', 'Constructing an activity network',
  '<div style="font-size:20px"><b>Construct</b> an activity network from the following precedence table.' + ptab(WE2, fs=17, head=('activity', 'immediate predecessor(s)')) + '</div>',
  [('Start', '<i>A</i>, <i>B</i> have no predecessors'), ('Next', '<i>C</i>, <i>D</i> after <i>A</i>; <i>E</i>, <i>F</i> after <i>B</i>'),
   ('Meet', '<i>D</i>, <i>E</i> meet → <i>G</i>; <i>C</i>, <i>G</i> meet → <i>H</i>; <i>F</i>, <i>H</i> meet → <i>I</i> → finish')],
  '', f'{EDR} · 8H Worked example 2 (pp. 609–610)', cmd=('Construct', None, 'one edge per activity'), afig=Wd(360, img('edr2.png'))))

# ================= Learn 2: dummies
S.append(learn('Learn · 14C', 'Dummy activities',
  '<h4>Some, but not all, the same</h4><ul class="bul" style="font-size:19px;line-height:1.5;margin-left:22px">'
  '<li>when two activities share <b>some, but not all</b>, of their immediate predecessors, one edge can’t show both</li>'
  '<li>draw a <b>dummy</b>: a dashed edge, zero time, not a real activity</li>'
  '<li>it runs <b>from the end</b> of the shared predecessor <b>to the start</b> of the activity with the extra predecessor</li></ul>',
  side(ptab(DUM, fs=16, hi=('D', 'E')), Wd(340, img('camdum.png')) + frag('<i>D</i> needs <i>A</i> and <i>B</i>; <i>E</i> needs <i>B</i> and <i>C</i>: two dummies from the end of <i>B</i>'), w=380),
  'A dummy is never written as a predecessor in the table.', f'{CAM}, 14C pp. 686–687 (own words; Cambridge’s diagram) · {EDR}, 8H pp. 611–612',
  cards=(kcard('Dummy activity', 'dashed, zero time'), kcard('Direction', 'end of shared → start of extra'))))
S.append(qslide('we', 'Worked example 8 · 14C', 'Using a dummy activity',
  '<div style="font-size:20px"><b>Draw</b> an activity network from the precedence table shown below.' + ptab(EX8, fs=17) + '</div>',
  [('Start / finish', '<i>A</i>, <i>B</i> leave start; <i>G</i> goes to finish'), ('Shared', '<i>F</i> needs <i>C</i>; <i>E</i> needs <i>C</i> AND <i>D</i>'),
   ('Dummy', 'from the end of <i>C</i> (shared) to the start of <i>E</i> (extra predecessor)')],
  '', f'{CAM} · Example 8 (pp. 687–688)', video='Cambridge GO · Example 8 (14C Resources)', cmd=('Draw', None, 'add a dummy where needed'), afig=Wd(360, img('cam8.png'))))
S.append(qslide('yt', 'You try · Edrolo 8H WE4', 'Activity networks with a dummy',
  '<div style="font-size:18px">Consider the following precedence table.' + ptab(WE4, fs=16, head=('activity', 'immediate predecessor(s)'))
  + '<div style="margin-top:6px">a. Complete the following sentence.<br><span style="margin-left:18px">A dummy activity needs to be drawn from the end of activity _ to the start of activity _.</span></div>'
  '<div style="margin-top:6px">b. <b>Construct</b> an activity network from the precedence table.</div></div>',
  [('Shared', '<i>F</i> needs <i>C</i>; <i>I</i> needs <i>C</i> and <i>G</i>'), ('Draw', '<i>A</i>, then <i>B</i>, <i>C</i>, <i>D</i>; <i>I</i> after <i>G</i>; then the dummy')],
  '', f'{EDR} · 8H Worked example 4 (pp. 612–613)', cmd=('Construct', None, 'one edge per activity, plus the dummy'),
  parts=[('a', 'from the end of activity <b><i>C</i></b> to the start of activity <b><i>I</i></b>'), ('b', Wd(330, img('edr4.png')))]))
sm()
S.append(qslide('we', 'Worked example 9 · 14C', 'Precedence table from a network',
  ('<div style="font-size:20px"><b>Write down</b> a precedence table for the activity network shown below.</div>', Wd(470, img('cam9.png')), ''),
  [('Rows', 'one row per activity (not the dummies)'), ('Read', 'what ends at the start of each edge'),
   ('Dummies', '<i>C</i> also comes before <i>F</i> and <i>G</i>; <i>G</i> also before <i>J</i>')],
  '', f'{CAM} · Example 9 (p. 688)', video='Cambridge GO · Example 9 (14C Resources)', cmd=('Write down', None, 'every edge ending at its start'), afig=ptab(EX9, fs=14)))
sm()
S.append(qslide('yt', 'You try · Edrolo 8H WE3', 'Precedence table from a network',
  ('<div style="font-size:20px"><b>Construct</b> a precedence table from the following activity network.</div>', Wd(400, img('edr3.png')), ''),
  [('Start', '<i>A</i>, <i>B</i>, <i>C</i> leave start: “–”'), ('Read', 'what ends where each activity starts')],
  '', f'{EDR} · 8H Worked example 3 (pp. 610–611)', cmd=('Construct', None, 'a row per activity'), afig=ptab(WE3, fs=14, head=('activity', 'immediate predecessor(s)'))))
sm()

# ================= Exits
S.append(qslide('ex', 'Exit task 1 of 2 · VCAA 2017 Exam 2 Q4a', 'Show what you know',
  ('<div style="font-size:17px">The rides at the theme park are set up at the beginning of each holiday season.<br>This project involves activities <i>A</i> to <i>O</i>.<br>'
   'The directed network below shows these activities and their completion times in days.</div>', Wd(470, img('ex1.png')),
   '<div style="font-size:18px">a. Write down the two immediate predecessors of activity <i>I</i>. <span class="muted">(1 mark)</span></div>'),
  [('Into I', '<i>D</i> ends where <i>I</i> starts'), ('Dummy', 'the dummy brings <i>E</i> to that vertex too: count <i>E</i>, not “dummy”')],
  'The immediate predecessors of <i>I</i> are <b><i>D</i> and <i>E</i></b>.', f'VCAA 2017 Further Mathematics Exam 2 Networks and decision mathematics Q4 stem and Q4a (examiner report: 67%) · {EDR} 8H Q14 (adapted there)',
  stat=('avg', 67), cmd=('Write down', 1, 'two activities')))
sm()
S.append(qslide('ex', 'Exit task 2 of 2 · VCAA 2020 Exam 2 Q5a', 'Show what you know',
  '<div style="font-size:15px">The Sunny Coast cricket clubroom is undergoing a major works project.<br>This project involves nine activities: A to I.<br>'
  'The table below shows the earliest start time (EST) and duration, in months, for each activity.<br>The immediate predecessor(s) is also shown.<br>The duration for activity C is missing.'
  '<table class="t" style="margin:4px auto;font-size:14px"><tr><th>Activity</th><th>EST</th><th>Duration</th><th>Immediate predecessor(s)</th></tr>'
  + ''.join(f'<tr><td style="text-align:center">{a}</td><td style="text-align:center">{e}</td><td style="text-align:center">{d}</td><td style="text-align:center">{p}</td></tr>' for a, e, d, p in CR) + '</table>'
  'The information in the table above can be used to complete a directed network.<br>This network will require a dummy activity.<br>'
  'a. <b>Complete</b> the following sentence by filling in the boxes provided. <span class="muted">(1 mark)</span><br>This dummy activity could be drawn as a directed edge from the end of activity ☐ to the start of activity ☐.</div>',
  [('Shared', '<i>F</i> needs only <i>B</i>; <i>C</i> needs <i>A</i> AND <i>B</i>'), ('Dummy', 'from the end of <i>B</i> (shared) to the start of <i>C</i> (extra predecessor)')],
  'From the end of activity <b>B</b> to the start of activity <b>C</b>.', f'VCAA 2020 Further Mathematics Exam 2 Networks and decision mathematics Q5 stem and Q5a (examiner report: 26%) · {EDR} 8H Q15 (adapted there)',
  stat=('avg', 26), cmd=('Complete', 1, 'two activity letters')))
sm(extra='sm xs')

# ================= closing
S.append(checkin(SC_))
CW = CARD['homework']['sets']
S.append(coursework([(st_['title'].replace('Revision book', 'Chapter 14 revision booklet'), st_.get('note') or '', ['<span style="display:flex;justify-content:space-between;gap:12px"><span>' + it['skill'] + '</span><b>' + it['q'] + '</b></span>' for it in st_['items']]) for st_ in CW]))
Vd = json.load(open(os.path.join(ROOT, 'planner', 'videos.json'))); Vd = Vd if isinstance(Vd, list) else Vd.get('videos', [])
yid = lambda u: u.split('v=')[1].split('&')[0] if 'v=' in u else u.rstrip('/').split('/')[-1]
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})', yid(v['url'])) for v in Vd if v['sub'] == '14C' and v.get('url')]))
n = assemble(S, '12MAG · 14C · Precedence tables and activity networks', os.path.join(ROOT, 'lessons', '14C slides.html'))
print(n - 1, 'slides')
