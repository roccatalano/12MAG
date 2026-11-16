"""CONTENT for CFAT 4.14.1 (Cambridge 14A-14B), CFAT 4.14.2 (14C-14D), CFAT 4.14.3 (14E). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no exam practice / VCAA reprints). Edrolo Ch 8 -> Cambridge Ch 14:
8E -> 14A, 8G -> 14B, 8H -> 14C, 8I -> 14D, 8J -> 14E (tools/y12_edrolo_exercise_questions.csv).
Graphs/tables/options CROPPED from the Edrolo PDF by crop.py (PDF pp. 585-587, 609-610, 621-622, 637-638, 647-649 =
printed 578-642); stems/part text typed verbatim. Answers from the Edrolo answer pages (PDF pp. 737, 739-741, 743, 746 =
printed 730-739). Marks set by Claude. 8E Q5 and 8E Q9 use parts a-b only; 8H Q4 uses part a only (stems unchanged).

CFAT 4.14.1 (13 marks, start of lesson gm12-u4-14c): MC 8E Q1, 8E Q4, 8E Q7, 8G Q1, 8G Q4; SA 8E Q5ab, 8E Q9ab, 8G Q2.
CFAT 4.14.2 (12 marks, start of lesson gm12-u4-14e): MC 8H Q1, 8H Q3, 8I Q7; SA 8H Q2, 8H Q4a, 8I Q3, 8I Q4, 8I Q8.
CFAT 4.14.3 (10 marks, start of the Ch 14 test lesson gm12-ch14-test): MC 8J Q1, 8J Q4; SA 8J Q3, 8J Q6, 8J Q7.
Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

def mc(src, fig, w, ans): return dict(src='Edrolo ' + src, fig=fig, w=w, ans=ans)

CFATS = [
 dict(id='CFAT 4.14.1', subs='14A-14B', title='Flow problems and matching problems',
  layout=[('full', 0), ('full', 1), ('full', 2), ('full', 3), ('full', 4)],
  mc=[mc('8E Q1', '8E_Q1', 11, 1), mc('8E Q4', '8E_Q4', 10.5, 1), mc('8E Q7', '8E_Q7', 9, 0), mc('8G Q1', '8G_Q1', 11.5, 0), mc('8G Q4', '8G_Q4', 10.5, 3)],
  sa=[
   dict(src='Edrolo 8E Q5 (parts a–b)', stem='Calculate the capacity of each of the following cuts.', fig='8E_Q5', w=12,
        parts=[('a.', '', 1, '15'), ('b.', '', 1, '17')]),
   dict(src='Edrolo 8E Q9', stem='Find the maximum flow from source to sink for each of the following networks.', fig='8E_Q9', w=12,
        parts=[('a.', '', 1, '11'), ('b.', '', 1, '18')]),
   dict(src='Edrolo 8G Q2', stem='Miki, Ramsha, Joy, and Kat are trying to set up a study group for each of their Year 12 subjects. The bipartite graph shows which subjects the students have in common.', fig='8G_Q2', w=5.5,
        parts=[('a.', 'How many of the students study English?', 1, '3 students'), ('b.', 'Which subject has the most students studying it?', 1, 'General Maths'),
               ('c.', 'The students want to set up a study group only for subjects that three or more of them are studying. How many study groups will they have?', 1, '3 study groups'),
               ('d.', 'Which study groups will Miki and Ramsha be in together?', 1, 'English and General Maths')]),
  ]),
 dict(id='CFAT 4.14.2', subs='14C-14D', title='Activity networks, precedence tables and critical path analysis',
  layout=[('full', 0), ('full', 1), ('full', 2)],
  mc=[mc('8H Q1', '8H_Q1', 13, 1), mc('8H Q3', '8H_Q3', 13, 3), dict(mc('8I Q7', '8I_Q7', 11.5, 4), n=5)],
  sa=[
   dict(src='Edrolo 8H Q2', stem='Hannah created a precedence table for a DIY project she wanted to complete.\nWhich activities must be completed before activity H can commence?', fig='8H_Q2', w=4.5,
        parts=[('', '', 1, 'A, B, C, D, E')]),
   dict(src='Edrolo 8H Q4 (part a)', stem='Construct a precedence table for each of the following activity networks.', fig='8H_Q4a', w=6.5,
        parts=[('a.', '', 1, 'activity: immediate predecessor(s)\nA: –   B: A   C: A\nD: A   E: B   F: D')]),
   dict(src='Edrolo 8I Q3', stem='Consider the following activity network.', fig='8I_Q3', w=6.5,
        parts=[('a.', 'The EST of activity B is\nA. 3     B. 4     C. 6     D. 7', 1, 'B'), ('b.', 'Determine the EST of activity E.', 1, '7'),
               ('c.', 'Determine the minimum completion time of the project.', 1, '17')]),
   dict(src='Edrolo 8I Q4', stem='The following activity network displays the time in minutes taken for each of the steps of a DIY craft project.', fig='8I_Q4', w=6.5,
        parts=[('a.', 'What is the earliest start time after the beginning of the project that activity E can start?', 1, '14 minutes'),
               ('b.', 'What is the minimum amount of time that it would take to finish the DIY craft project?', 1, '30 minutes')]),
   dict(src='Edrolo 8I Q8', stem='Consider the following activity network.', fig='8I_Q8', w=7,
        parts=[('a.', 'Find the critical path(s) of the activity network.', 1, 'A–D–H–I'), ('b.', 'What is the float time of activity J?', 1, '5')]),
  ]),
 dict(id='CFAT 4.14.3', subs='14E', title='Crashing an activity network',
  layout=[('full', 0), ('full', 1)],
  mc=[mc('8J Q1', '8J_Q1', 14, 2), mc('8J Q4', '8J_Q4', 14, 3)],
  sa=[
   dict(src='Edrolo 8J Q3', stem='In order to be more efficient, Alyssa, a Year 12 student, has timed all of her activities as she gets ready for school in the morning. She is able to multitask by doing numerous activities at once. The activity network for her morning activities is shown. All values are in minutes.', fig='8J_Q3', w=9,
        parts=[('a.', 'Find the critical path(s).', 1, 'A–B–E–G and A–D–H'),
               ('b.', 'Alyssa is able to cut down the time it takes to complete activity B. She can reduce its duration by 2 minutes.\nWill Alyssa be able to get ready for school faster? If not, explain why. If so, how much time has she saved?', 1, 'No. Reducing the duration of activity B will not reduce the total duration of the critical path A–D–H.'),
               ('c.', 'What is the new float time of activity B?', 1, '2 minutes'), ('d.', 'Find the new critical path(s).', 1, 'A–D–H')]),
   dict(src='Edrolo 8J Q6', stem='The following activity network shows the steps required to build an automatic farm on Minecraft.', fig='8J_Q6', w=7.5,
        stem2='The current minimum completion time is 19 minutes.\nActivities A and B can each be reduced for 9 emeralds per minute.\nActivities C and D can each be reduced for 7 emeralds per minute.\nEach activity can be reduced by a maximum of 2 minutes.',
        parts=[('', 'What is the minimum additional cost of completing the automatic farm in 16 minutes?', 1, '41 emeralds')]),
   dict(src='Edrolo 8J Q7', stem='There are plans for a new basketball court to be built in West Melbourne. Nine activities have been identified for this project. The following activity network shows the activities and their completion times in weeks.', fig='8J_Q7', w=9,
        stem2='The builders are able to speed up the project. Activities A, C, E, F and G can be reduced in completion time at an additional cost. The maximum reduction in time for each of the five activities is 2 weeks.',
        parts=[('a.', 'Which of these activities, if their durations were reduced individually, would not result in an earlier completion of the project?', 1, 'A, E and G'),
               ('b.', 'Determine the minimum time, in weeks, that the project can be completed now that certain activities can be reduced in duration.', 1, '15 weeks'),
               ('c.', 'The cost of reducing the time of each activity is $5000 per week. Determine the minimum additional cost for completing the project in this reduced time.', 1, '$25 000')]),
  ]),
]
