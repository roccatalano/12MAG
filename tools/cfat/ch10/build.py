"""CONTENT for CFAT 3.10.1 (Cambridge 10A-10C), CFAT 3.10.2 (10D-10E), CFAT 3.10.3 (10F-10G). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no exam practice / VCAA reprints). Edrolo Ch 7 (Matrices) = Cambridge Ch 10
(7A -> 10A-10B, 7B -> 10C, 7C -> 10D, 7D -> 10E, 7E + 7F Q1-5 -> 10F, 7F Q6-10 -> 10G; tools/y12_edrolo_exercise_questions.csv).
Edrolo has no separate 10B exercise (7A covers 10A-10B). Matrices are not retyped: each question (or its stem) is CROPPED
from the Edrolo PDF by crop.py (PDF pp. 432, 441-442, 453, 455, 463-464, 472, 482-484 = printed 425, 434-435, 446, 448,
456-457, 465, 475-477), so the wording is verbatim. Answers from the Edrolo answer pages (PDF pp. 716-723 = printed 709-716),
checked by hand (7D Q9/Q11 and 7F Q6/Q8 worked by hand: their answer page was not rendered). Marks set by Claude.

CFAT 3.10.1 (15 marks, start of lesson gm12-u4-10d): MC 7A Q1, 7B Q1, 7B Q4, 7B Q7; SA 7A Q2, 7A Q4, 7B Q5.
CFAT 3.10.2 (15 marks, start of lesson gm12-u4-10f10g): MC 7C Q1, 7C Q4, 7C Q12, 7D Q1, 7D Q5, 7D Q9; SA 7C Q6, 7C Q14 (a-b... all parts), 7D Q11.
CFAT 3.10.3 (13 marks, start of the Ch 10 test lesson gm12-ch10-test): MC 7E Q4, 7F Q1, 7F Q6, SA 7E Q1, 7F Q3, 7F Q8.
Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

def mc(src, fig, w, ans): return dict(src='Edrolo ' + src, fig=fig, w=w, ans=ans)

CFATS = [
 dict(id='CFAT 3.10.1', subs='10A-10C', title='Matrices: types, addition, scalars and transpose',
  layout=[('full', 0), ('full', 1), ('full', 2), ('full', 3)],
  mc=[mc('7A Q1', '7A_Q1', 15, 0), mc('7B Q1', '7B_Q1', 14, 2), mc('7B Q4', '7B_Q4', 14, 3), mc('7B Q7', '7B_Q7', 15, 0)],
  sa=[
   dict(src='Edrolo 7A Q2', stem='', fig='7A_Q2', w=6.5,
        parts=[('a.', 'How many rows and columns can be found in B?', 1, '4 rows and 2 columns'),
               ('b.', 'What is the order of B?', 1, '4 × 2'),
               ('c.', 'What entry corresponds with b₃₁?', 1, '8')]),
   dict(src='Edrolo 7A Q4', stem='', fig='7A_Q4', w=6.5,
        parts=[('a.', 'What entry corresponds to d₂₃?', 1, '46'), ('b.', 'What entry corresponds to d₃₅?', 1, '47'),
               ('c.', 'What entry corresponds to d₁₅?', 1, '111'), ('d.', 'Which entry corresponds to d₂₄?', 1, '53')]),
   dict(src='Edrolo 7B Q5', stem='', fig='7B_Q5', w=14,
        parts=[('a.', '', 1, '[6  12  2  18  10]'), ('b.', '', 1, '[ 8  20  −24 ]\n[−12  4  16 ]'),
               ('c.', '', 1, '[−36  21  12  −27  −24  −33]ᵀ (a 6 × 1 column matrix)'),
               ('d.', '', 1, '[ 9  15  7.5 ]\n[ 6  −4.5  −30 ]\n[ −1.5  12  3 ]')]),
  ]),
 dict(id='CFAT 3.10.2', subs='10D-10E', title='Matrix products, powers, determinants and inverses',
  layout=[('full', 0), ('full', 1), ('full', 2), ('full', 3), ('full', 4), ('full', 5)],
  mc=[mc('7C Q1', '7C_Q1', 14, 2), mc('7C Q4', '7C_Q4', 14, 3), mc('7C Q12', '7C_Q12', 14, 2),
      mc('7D Q1', '7D_Q1', 14, 0), mc('7D Q5', '7D_Q5', 14, 1), mc('7D Q9', '7D_Q9', 14, 1)],
  sa=[
   dict(src='Edrolo 7C Q6', stem='', fig='7C_Q6', w=12.5,
        parts=[('a.', 'Calculate GH.', 1, 'GH = [26]\n        [19]'), ('b.', 'What does the matrix GH represent?', 1, 'The total number of points received in the tournament by each team.'),
               ('c.', 'Which team had the most points at the end of the tournament and how many points did they have?', 1, 'Soccerolo; 26 points')]),
   dict(src='Edrolo 7C Q14', stem='', fig='7C_Q14', w=13.5,
        parts=[('a.', '', 1, '[0  1]\n[1  0]'), ('b.', '', 1, '[3  −6]\n[5  −2]'), ('c.', '', 1, '[−3  −6]\n[−1  −2]')]),
   dict(src='Edrolo 7D Q11', stem='', fig='7D_Q11', w=13.5,
        parts=[('a.', '', 1, 'x = 2, y = 6'), ('b.', '', 1, 'x = −8, y = 5'), ('c.', '', 1, 'x = 1, y = 5')]),
  ]),
 dict(id='CFAT 3.10.3', subs='10F-10G', title='Binary, permutation, communication and dominance matrices',
  layout=[('full', 0), ('full', 1), ('full', 2)],
  mc=[mc('7E Q4', '7E_Q4', 14, 2), mc('7F Q1', '7F_Q1', 14, 0), mc('7F Q6', '7F_Q6', 11, 1)],
  sa=[
   dict(src='Edrolo 7E Q1', stem='', fig='7E_Q1', w=13.5,
        parts=[('a.', 'Which of these are binary matrices?', 1, 'B, C, D and E'), ('b.', 'Which of these are permutation matrices?', 1, 'C and E')]),
   dict(src='Edrolo 7F Q3', stem='', fig='7F_Q3', w=9,
        parts=[('a.', 'Interpret c₁₃.', 1, 'P1 and P3 cannot communicate with each other.'), ('b.', 'Which aeroplane(s) can P4 directly communicate with?', 1, 'P2 and P3'),
               ('c.', 'Is this a directed or undirected communication matrix?', 1, 'Undirected')]),
   dict(src='Edrolo 7F Q8', stem='', fig='7F_Q8', w=10,
        parts=[('a.', 'Interpret d₂₃.', 1, 'rainbowmuffin defeated xthundercatx.'), ('b.', 'Which player(s) did ai.zhao999 lose to?', 1, 'rainbowmuffin and felipe.sanchez.'),
               ('c.', 'Who is the top-ranking player according to one-step dominances?', 1, 'rainbowmuffin (3 one-step dominances)')]),
  ]),
]
