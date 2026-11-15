"""Data for lesson l10 (3B). Values read off the source figures/tables (VCAA and Edrolo scatterplots redrawn; points read off the grid)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f9', os.path.join(H, '..', 'l09', 'figs.py')); _f9 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f9)
scat, W_, corr, ICE, FOOT, FEM, lsq = _f9.scat, _f9.W_, _f9.corr, _f9.ICE, _f9.FOOT, _f9.FEM, _f9.lsq
_s = importlib.util.spec_from_file_location('f5', os.path.join(H, '..', 'l05', 'figs.py')); _f5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f5)
CONG = _f5.V18   # VCAA 2018 Further Exam 2 Q2 (morning, evening congestion level %, 19 cities)
# VCAA 2023 Exam 1 Q7-8 (test 1 mark, test 2 mark; 15 students, whole numbers)
TESTS = [(16, 18), (19, 27), (20, 20), (21, 23), (22, 30), (22, 22), (23, 28), (24, 36), (28, 40), (29, 39), (30, 37), (31, 41), (33, 47), (33, 41), (36, 49)]
# VCAA 2018 Further Exam 1 Q7-9 (time spent exercising h/week, resting pulse rate; 16 students)
PULSE = [(2, 67), (2, 66), (2, 65), (3, 66), (3, 65), (3, 64), (4, 63), (5, 64), (6, 63), (6, 62), (7, 61), (7, 60), (8, 60), (8, 59), (9, 58), (10, 57)]
# VCAA 2019 Further Exam 2 Q5 (pressure 9 am, pressure 3 pm, hPa; 23 days)
PRESS = [(1013, 1015), (1013.8, 1013), (1014.4, 1013.4), (1014.5, 1014.4), (1014.6, 1014.8), (1015.6, 1013.9), (1015.6, 1013.4), (1016.8, 1016.4),
         (1017.8, 1016.6), (1018.4, 1015.4), (1018.7, 1017), (1018.8, 1017.8), (1019, 1016.5), (1020.4, 1017.7), (1022, 1018.9), (1022, 1021.4),
         (1022.8, 1020.2), (1023.4, 1021.4), (1024.6, 1022.1), (1025.6, 1023.6), (1026.5, 1026.3), (1026.6, 1025.3), (1027.2, 1025.7)]
# Edrolo U3&4 3B Worked example 1 (age years, height cm; approximate)
KIDS = [(1, 62), (1, 75), (1.2, 74), (1.6, 67), (1.6, 83), (1.8, 80), (2, 73), (2.2, 84), (2.4, 81), (2.7, 78), (2.8, 91), (3, 90), (3, 86), (3.3, 99),
        (3.8, 94), (4, 109), (4, 90), (4.3, 102), (4.4, 105), (4.6, 110), (4.8, 108), (5, 112), (5.1, 116), (5.3, 118), (5.4, 105), (5.5, 115), (5.8, 113)]
# Edrolo U3&4 3B Worked example 2 (snowfall cm, number of customers; line through (0, 14) and (10, 87))
SKI = [(1, 28), (2, 29), (3, 34), (3.8, 35), (4, 41), (4.3, 39), (5.2, 43), (5.9, 61), (6, 67), (7, 68), (7.6, 75), (8, 67), (8.3, 79), (9, 82), (9, 75)]
# Cambridge U3&4 3B (pp. 179-180): age (years), price ($) of 15 second-hand cars
CARS = [(1, 32500), (1, 30500), (2, 25600), (3, 20000), (3, 24300), (3, 22000), (4, 22000), (4, 23000), (4, 19200), (5, 16000), (5, 18400),
        (6, 6500), (7, 6400), (7, 8500), (8, 4200)]
