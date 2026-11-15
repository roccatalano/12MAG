"""Data for lesson l14 (4C). Values copied from the source tables; where only a plot is printed, points are read off the source figure (close approximation)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f12', os.path.join(H, '..', 'l12', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
scat, W_, corr, lsq, WEEK, DIST = _f.scat, _f.W_, _f.corr, _f.lsq, _f.WEEK, _f.DIST
# VCAA 2024 Exam 1 Q11-12 stem (year, pairs)
YR = list(range(1, 13)); PAIRS = [320, 250, 225, 208, 190, 180, 170, 165, 160, 158, 155, 150]
# VCAA 2025 Exam 1 Q11-12 stem (doctors per 1000, life years)
DOC = [0.21, 0.42, 0.59, 0.79, 1.12, 1.42, 1.72, 1.77, 1.94, 2.05]; LIFE = [64.6, 64.4, 64.7, 65.1, 65.9, 66.7, 68.6, 70.9, 73.8, 79.1]
# VCAA 2026 Exam 2 Q5g (happiness index, log10 income)
HAP = [4.3, 7.1, 4.9, 7.6, 7.2, 5.8, 5.3, 5.5, 7.2, 3.0]; LINC = [3.16, 3.85, 3.32, 4.30, 4.29, 3.53, 3.10, 3.74, 4.24, 3.00]
# VCAA 2024 Exam 2 Q3 Table 2 (Wgold, Wbest)
OYR = list(range(1972, 2021, 4))
WGOLD = [1.92, 1.93, 1.97, 2.02, 2.03, 2.02, 2.05, 2.01, 2.06, 2.05, 2.05, 1.97, 2.04]
WBEST = [1.94, 1.96, 1.98, 2.07, 2.07, 2.05, 2.05, 2.02, 2.06, 2.06, 2.05, 2.01, 2.05]
# Cambridge U3&4 4C Example 5 (week, weekly weight loss kg): read off the scatterplot p. 231 (close approximation)
BWK = list(range(1, 11)); LOSS = [5.35, 2.3, 2.0, 1.0, 0.9, 0.4, 1.55, 1.8, 0.4, 0.35]
# Cambridge U3&4 4C Example 6 / CAS 3 (sticky labels, cm)
LEN = [6.8, 5.6, 4.6, 4.2, 3.5, 4.0, 5.0, 5.5]; WID = [1.8, 2.0, 2.5, 3.0, 3.5, 2.6, 2.0, 1.9]
# Edrolo U3&4 3D Worked example 4 (hours studied, questions incorrect)
HRS = [1, 2, 2.5, 3, 4, 4, 5, 6, 6.5, 7]; QI = [63, 32, 23, 17, 16, 14, 8, 7, 5, 5]
# VCAA 2018 Exam 1 Q11 (Edrolo 3E Q11)
FX = list(range(1, 11)); FY = [105, 48, 35, 23, 18, 16, 12, 12, 9, 9]
