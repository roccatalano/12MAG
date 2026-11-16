"""CONTENT for CFAT 3.11.1 (Cambridge 11A-11B) and CFAT 3.11.2 (11C-11E). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no exam practice / VCAA reprints). Edrolo 7G-7I = Cambridge Ch 11:
7G (state/transition matrices -> 11A, calculating state matrices -> 11C, Leslie -> 11E), 7H (equilibrium -> 11C),
7I Q1-6 (transition diagrams -> 11B), 7I Q7-11 ('culling and restocking', S(n+1) = T S(n) + B -> 11D; the exercise index
maps them to 11B, but the Edrolo section heading is 11D's content).
Questions (and matrices/diagrams) are CROPPED from the Edrolo PDF by crop.py (PDF pp. 496-499, 506, 516, 518 = printed
489-492, 499, 509, 511), so the wording is verbatim; part wording typed only where the part sits under a cropped stem.
Answers from the Edrolo answer pages (PDF pp. 724, 725, 727, 728 = printed 717, 718, 720, 721), checked with numpy
(7H Q4's answer was on a page not rendered: worked with numpy, T^60 S0). Marks set by Claude.

CFAT 3.11.1 (13 marks, start of lesson gm12-u4-11c): MC 7G Q1, 7I Q1, 7G Q4; SA 7G Q2, 7G Q5, 7I Q2.
CFAT 3.11.2 (14 marks, start of the Ch 11 test lesson gm12-ch11-test): MC 7H Q1, 7H Q5, 7I Q7; SA 7G Q10, 7H Q4, 7I Q8, 7G Q12, 7G Q13.
Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

def mc(src, fig, w, ans): return dict(src='Edrolo ' + src, fig=fig, w=w, ans=ans)

CFATS = [
 dict(id='CFAT 3.11.1', subs='11A-11B', title='Transition matrices and transition diagrams',
  layout=[([0], [1]), ('full', 2)],
  mc=[mc('7G Q1', '7G_Q1', 8.5, 0), mc('7I Q1', '7I_Q1', 9.5, 2), mc('7G Q4', '7G_Q4', 12.5, 3)],
  sa=[
   dict(src='Edrolo 7G Q2', stem='', fig='7G_Q2', w=11.5,
        parts=[('a.', 'How many people rode ‘The Devastator’ as their first ride of the day?', 1, '57 people'),
               ('b.', 'How many people attended the carnival on the given day?', 1, '198 people'),
               ('c.', 'What percentage of people chose not to take a ride at all when attending the carnival, rounded to the nearest percent?', 1, '24/198 × 100 ≈ 12%')]),
   dict(src='Edrolo 7G Q5', stem='', fig='7G_Q5', w=12.5,
        parts=[('a.', 'What percentage of people who fold their paper for recycling this time are expected to scrunch next time?', 1, '9%'),
               ('b.', 'What percentage of people who scrunch their paper for recycling this time are expected to fold next time?', 1, '23%'),
               ('c.', 'What percentage of people who fold their paper for recycling this time are expected to fold again next time?', 1, '91%'),
               ('d.', 'What percentage of people who scrunch their paper for recycling this time are expected to scrunch again next time?', 1, '77%')]),
   dict(src='Edrolo 7I Q2', stem='', fig='7I_Q2', w=11,
        parts=[('a.', '', 1, '[0.23  0.38] A\n[0.77  0.62] B'),
               ('b.', '', 1, '[0.93  0.25] X\n[0.07  0.75] Y'),
               ('c.', '', 1, '[0.87  0] A\n[0.13  1] B')]),
  ]),
 dict(id='CFAT 3.11.2', subs='11C-11E', title='State matrices, steady state, culling/restocking and Leslie matrices',
  layout=[('full', 0), ([1], [2])],
  mc=[mc('7H Q1', '7H_Q1', 13, 3), mc('7H Q5', '7H_Q5', 9, 1), mc('7I Q7', '7I_Q7', 7.5, 2)],
  sa=[
   dict(src='Edrolo 7G Q10', stem='', fig='7G_Q10', w=12.5,
        parts=[('a.', 'How many participants are predicted to eat the red gummy in the third hour?', 1, '23 participants'),
               ('b.', 'How many participants are predicted to eat the blue gummy in the sixth hour?', 1, '27 participants')]),
   dict(src='Edrolo 7H Q4', stem='', fig='7H_Q4', w=10.5,
        parts=[('', '', 1, 'S = [69 eat, 31 stay]ᵀ')]),
   dict(src='Edrolo 7I Q8', stem='', fig='7I_Q8', w=9,
        parts=[('a.', '', 1, 'S₃ = [72.8]\n        [47.2]'), ('b.', '', 1, 'S₃ = [36.3]\n        [41.7]'), ('c.', '', 1, 'S₃ = [88.6]\n        [28.4]')]),
   dict(src='Edrolo 7G Q12', stem='', fig='7G_Q12', w=7.5,
        parts=[('a.', 'Write A, B, C or D.', 1, 'D'), ('b.', 'Write A, B, C or D.', 1, 'B')]),
   dict(src='Edrolo 7G Q13', stem='', fig='7G_Q13', w=10,
        parts=[('a.', 'Using a matrix recurrence relation, determine the expected female population after 2 years.', 1, 'S₂ = L²S₀ = [49.2  19.2]ᵀ → 68 females'),
               ('b.', 'Determine the state matrix that represents the expected female population after 10 years.', 1, 'S₁₀ = [64 (age 0), 25 (age 1)]ᵀ'),
               ('c.', 'Has the female population of the critically endangered species increased after 10 years? If so, by how much?', 1, 'Yes; by 24 females (89 − 65)')]),
  ]),
]
