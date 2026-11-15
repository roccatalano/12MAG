"""Data for lesson l09 (3A). Values read off the source figures/tables (VCAA scatterplots redrawn; points read off the grid)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f6', os.path.join(H, '..', 'l06', 'figs.py')); _f6 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f6)
scat, W_, corr, ICE, FOOT = _f6.scat, _f6.W_, _f6.corr, _f6.ICE, _f6.FOOT

# VCAA 2026 Exam 1 Q7-8 (doctors per 10 000, TV sets per 1000; 20 countries; read off the grid); printed LSRL from (0, 113) to (50, 348)
DOC = [(2.5, 52), (5, 111), (7.7, 158), (12, 44), (13.5, 158), (14, 318), (15.8, 333), (16, 126), (20, 242), (21.5, 97), (23.3, 350), (25, 276),
       (27.8, 251), (32, 386), (33.5, 318), (34.7, 261), (35.3, 20), (36.2, 339), (47.2, 418), (48, 231)]
# VCAA 2024 Exam 1 Q13-14 time series (new staff 2011-2022)
NEWST = [14, 11, 7, 6, 11, 13, 12, 6, 10, 15, 12, 10]
# VCAA 2017 Further Exam 2 Q3 (male moths table; female moths scatterplot read off the grid)
MALE = [35, 37, 45, 49, 65, 74, 77, 86, 95]; EGG = [471, 635, 664, 997, 1350, 1100, 2010, 1640, 1350]
FEM = [(15, 500), (16, 680), (22, 1100), (29, 740), (30, 1280), (35, 1420), (45, 1820), (49, 2010), (55, 1500)]
# VCAA 2021 Further Exam 1 Q11 (weight kg, height cm)
WT = [59, 67, 69, 84, 64, 74, 76, 56, 58, 66]; HTC = [173, 180, 184, 195, 173, 180, 192, 169, 164, 180]
# Edrolo U3&4 3A Worked example 1 (fathers and sons, cm)
FATH = [182, 187, 174, 177, 162, 171, 188, 165, 170, 185]; SON = [184, 179, 176, 168, 161, 173, 187, 163, 170, 181]
# Cambridge U3&4 3A CAS 1 (height cm, weight kg, 11 people)
CH = [177, 182, 167, 178, 173, 184, 162, 169, 164, 170, 180]; CW = [74, 75, 62, 63, 64, 74, 57, 55, 56, 68, 72]


def lsq(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return my - b * mx, b
