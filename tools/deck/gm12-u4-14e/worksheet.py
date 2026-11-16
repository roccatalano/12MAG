"""Lesson gm12-u4-14e (14E Crashing) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py).
Questions verbatim, same items and order as build.py (Do Now and CFAT are not on the worksheet; no APK and no CAS for 14E).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
Examples 12-13 = Cambridge U3&4 pp. 709-712. You try 1-2 = Edrolo U3&4 8J WE1 (p. 637), WE2 (pp. 638-639).
Exits = VCAA 2017 Exam 2 N&DM Q4ci,ii (Edrolo 8J Q9) · VCAA 2020 Exam 1 N&DM Q10 (Edrolo 8J Q10) · VCAA 2021 Exam 2 N&DM Q4c (Edrolo 8J Q11).
Output: lessons/14E worksheet(.html/.pdf) + ... solutions.   Run: python3 tools/deck/gm12-u4-14e/worksheet.py"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..')); sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, H)
from ws2 import *
import ws2
from figs import img
def G(html, mm): return f'<div style="width:{mm}mm;max-width:100%;margin:1mm auto">{html}</div>'
def I(name, mm): return G(img(name), mm)
def sol(html): return f'<div class="solonly">{html}</div>'
def stu(mm): return f'<div class="stuonly"><div style="min-height:{mm}mm"></div></div>'
def red(t): return f'<div class="solonly" style="color:#c00;font-weight:700;font-size:10pt">{t}</div>'
def ans(mm, t): return stu(mm) + red(t)
HR = '<hr class="dash">'

P = [title('14E', 'Crashing')]
P.append(lis(['To be able to use crashing to reduce the completion time of a project.',
              'To be able to minimise the cost of crashing activities to achieve the maximum reduction in completion time of a project.']))
P.append(sect('14E Crashing', 'Example, then you try'))
P.append(exyt('Example 12 · Crashing one activity with cost',
  q('The directed network below shows the sequence of 8 activities that are needed to complete a project. The time, in days, that it takes to complete each activity is also shown.') + I('cam12.png', 70)
  + q('a. Write down the critical path for this project.') + ans(10, '<i>C</i> – <i>F</i> – <i>G</i> (paths: <i>A</i>–<i>D</i>–<i>H</i> 14, <i>B</i>–<i>E</i>–<i>G</i> 13, <i>C</i>–<i>F</i>–<i>G</i> 16)') + HR
  + q('b. What is the minimum completion time for the project?') + ans(6, '16 days') + HR
  + q('Activity <i>F</i> can be reduced by a maximum of 3 days at a cost of $100 per day.<br>c. What is the new minimum completion time for the project?') + ans(8, '14 days (<i>A</i>–<i>D</i>–<i>H</i> becomes critical)') + HR
  + q('d. What is the minimum cost that will achieve the greatest reduction in time taken to complete the project?') + ans(8, '$200 (reduce <i>F</i> by 2 days only)'),
  'You try 1', q('Claire is part of a study group that is planning to create revision notes on chapter 8 of this textbook. The activity network shows all the lessons within chapter 8. All values are in hours.') + I('edr1q.png', 70)
  + q('Claire asks her friend Klare to help the study group. With Klare’s assistance, the study group can reduce the time it will take to complete revision notes for lesson <i>C</i> by 2 hours and lessons <i>B</i>, <i>G</i> and <i>I</i> by 3 hours.')
  + q('a. What is the minimum amount of time it will take the group to complete revision notes for chapter 8 with Klare’s help?') + stu(40) + sol(I('edr1a.png', 65)) + red('19 hours') + HR
  + q('b. What is the critical path of the project?') + stu(40) + sol(I('edr1b.png', 65)) + red('<i>A</i>–<i>B</i>–<i>C</i>–<i>D</i>–<i>E</i>')))
P.append(exyt('Example 13 · Crashing multiple activities with cost',
  q('The directed network below shows the sequence of 9 activities that are needed to complete a project. The time, in days, that it takes to complete each activity is also shown.') + I('cam13.png', 70)
  + q('The minimum completion time for the project is 28 days. It is possible to reduce the completion time for activities <i>B</i>, <i>E</i>, <i>G</i>, <i>H</i> and <i>I</i>. The completion time for each of these five activities can be reduced by a maximum of two days.')
  + q('a. What is the new minimum completion time, in days, that the project could take?') + ans(22, 'Paths: <i>A</i>–<i>C</i>–<i>E</i> 27 → 25, <i>A</i>–<i>F</i>–<i>H</i> 19 → 17, <i>B</i>–<i>D</i>–<i>F</i>–<i>H</i> 28 → 24, <i>B</i>–<i>G</i>–<i>I</i> 28 → 22<br>25 days') + HR
  + '<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">' + q('The reduction in completion time for each of these five activities will incur an additional cost. The table opposite shows the five activities that can have their completion times reduced and the associated daily cost, in dollars.<br>b. What is the minimum cost that will achieve the greatest reduction in time taken to complete the project?') + '</div>' + I('cam13t.png', 30) + '</div>'
  + ans(30, '<i>E</i> by 2, <i>B</i> by 2, <i>H</i> by 1, <i>G</i> by 1<br>2000 × 2 + 1500 × 2 + 900 + 700 = $8600'),
  'You try 2', q('A landscaping company is preparing to renovate and landscape a garden. The activities that must be completed for the project are represented in the following activity network. All values are in days.') + I('edr2q.png', 75)
  + q('The manager is willing to employ more staff in order to speed up the completion of the project.<br>The completion times of activities <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i> can each be reduced by $150 per day, for up to two days.')
  + q('a. What is the minimum cost of reducing the minimum completion time by as much as possible?') + stu(40) + sol(I('edr2a.png', 70)) + red('<i>A</i>, <i>C</i>, <i>D</i> by 2 days, <i>B</i> (or <i>E</i>) by 1 day: 7 × $150 = $1050') + HR
  + q('b. On top of the current reductions, the manager may also be able to further reduce either the duration of activity <i>A</i> by 1 day for $140, the duration of activity <i>G</i> by 1 day for $175 or the duration of activity <i>I</i> by 1 day for $225. Which activity should the manager reduce the duration of?')
  + stu(30) + red('Activity <i>G</i>: <i>G</i> and <i>I</i> are on both critical paths (<i>A</i>–<i>C</i>–<i>D</i>–<i>G</i>–<i>I</i>, <i>B</i>–<i>E</i>–<i>G</i>–<i>I</i>); <i>G</i> is cheaper')))
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2017 Exam 2 Q4c', q('The rides at the theme park are set up at the beginning of each holiday season.<br>This project involves activities <i>A</i> to <i>O</i>.<br>The directed network below shows these activities and their completion times in days.')
  + I('ex1.png', 85) + q('[The minimum completion time for the project is 19 days.]<br>c. The project could finish earlier if some activities were crashed.<br>Six activities, <i>B</i>, <i>D</i>, <i>G</i>, <i>I</i>, <i>J</i> and <i>L</i>, can all be reduced by one day.<br>The cost of this crashing is $1000 per activity.')
  + q('i. What is the minimum number of days in which the project could now be completed?') + space(10, '17 days') + HR
  + q('ii. What is the minimum cost of completing the project in this time?') + space(10, '$4000 (reduce <i>G</i>, <i>I</i>, <i>J</i> and <i>L</i>)'), '2 marks'))
P.append(box('Exit task 2 · VCAA 2020 Exam 1 Q10', q('The directed network below shows the sequence of activities, <i>A</i> to <i>I</i>, that is required to complete an office renovation.<br>The time taken to complete each activity, in weeks, is also shown.') + I('ex2.png', 110)
  + q('The project manager would like to complete the office renovation in less time.<br>The project manager asks all the workers assigned to activity <i>H</i> to also work on activity <i>F</i>.<br>This will reduce the completion time of activity <i>F</i> to three weeks.<br>The workers assigned to activity <i>H</i> cannot work on both activity <i>H</i> and activity <i>F</i> at the same time.<br>No other activity times will be changed.<br>This change to the network will result in a change to the completion time of the office renovation.<br>Which one of the following is correct?')
  + mc(['The completion time will be reduced by one week if activity <i>F</i> is completed before activity <i>H</i> is started.', 'The completion time will be reduced by three weeks if activity <i>F</i> is completed before activity <i>H</i> is started.',
        'The completion time will be reduced by one week if activity <i>H</i> is completed before activity <i>F</i> is started.', 'The completion time will be reduced by three weeks if activity <i>H</i> is completed before activity <i>F</i> is started.',
        'The completion time will be increased by three weeks if activity <i>H</i> is completed before activity <i>F</i> is started.'], 'A')
  + why('25 weeks now; with <i>F</i> first, <i>A</i>–<i>C</i>–<i>E</i>–<i>F</i>–dummy–<i>H</i>–<i>I</i> = 24 weeks'), '1 mark'))
P.append(box('Exit task 3 · VCAA 2021 Exam 2 Q4c', q('Roadworks planned by the local council require 13 activities to be completed.<br>The network below shows these 13 activities and their completion times in weeks.') + I('ex3.png', 100)
  + '<div style="display:flex;gap:4mm;align-items:center"><div style="flex:1">' + q('c. It is possible to reduce the completion time for activities <i>A</i>, <i>E</i>, <i>F</i>, <i>L</i> and <i>K</i>.<br>The reduction in completion time for each of these five activities will incur an additional cost.<br>The table below shows the five activities that can have their completion time reduced and the associated weekly cost, in dollars.') + '</div>' + I('ex3t.png', 38) + '</div>'
  + q('The completion time for each of these five activities can be reduced by a maximum of two weeks.<br>The overall completion time for the roadworks can be reduced to 16 weeks.<br>What is the minimum cost, in dollars, of this change in completion time?')
  + space(14, '<i>L</i> by 2 weeks, <i>A</i> by 1 week: 2 × 120 000 + 140 000 = $380 000'), '1 mark'))
SC = ['I can crash an activity network.', 'I can crash an activity network with restrictions (cost).']
P.append(close(SC, [('14E', 'Q1–11')], ['14E']))
P[0] = ('<style>.solonly{display:none}.sol .solonly{display:block}.sol .stuonly{display:none}.box svg{max-width:100%}'
        'hr.dash{border:0;border-top:1px dashed #999;margin:2mm 0}</style>') + P[0]
build('gm12-u4-14e', '14E', 'AoS 4 · Networks and decision mathematics', P)
RD = os.path.join(ws2.ROOT, 'lessons')
for x, y in (('gm12-u4-14e-worksheet', '14E worksheet'), ('gm12-u4-14e-worksheet-solutions', '14E worksheet solutions')):
    for ext in ('.html', '.pdf'): os.replace(f'{RD}/{x}{ext}', f'{RD}/{y}{ext}')
