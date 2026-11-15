"""Data for lesson l07 (2G-2H). Values read off the source figures/tables (VCAA scatterplots redrawn; points read off the grid)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f6', os.path.join(H, '..', 'l06', 'figs.py')); _f6 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f6)
scat, W_, rcloud, corr, INC, CO2 = _f6.scat, _f6.W_, _f6.rcloud, _f6.corr, _f6.INC, _f6.CO2

# VCAA 2025 Exam 1 Q9-10 (goals against, games won; 12 A-League teams; read off the grid)
GOALS = [(27, 11), (32, 16), (33, 7), (34, 8), (35, 13), (39, 11), (45, 9), (45, 8), (46, 11), (46, 7), (47, 9), (48, 7)]
# VCAA 2024 Exam 2 Q1 Table 1 (year, Mgold m)
MGOLD = [(1928, 1.94), (1932, 1.97), (1936, 2.03), (1948, 1.98), (1952, 2.04), (1956, 2.12), (1960, 2.16), (1964, 2.18), (1968, 2.24), (1972, 2.23), (1976, 2.25),
         (1980, 2.36), (1984, 2.35), (1988, 2.38), (1992, 2.34), (1996, 2.39), (2000, 2.35), (2004, 2.36), (2008, 2.36), (2012, 2.33), (2016, 2.38), (2020, 2.37)]
# VCAA 2024 Exam 2 Q3 Table 2 (year, Wgold, Wbest)
WYR = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
WGOLD = [1.92, 1.93, 1.97, 2.02, 2.03, 2.02, 2.05, 2.01, 2.06, 2.05, 2.05, 1.97, 2.04]
WBEST = [1.94, 1.96, 1.98, 2.07, 2.07, 2.05, 2.05, 2.02, 2.06, 2.06, 2.05, 2.01, 2.05]
# VCAA 2019 Further Exam 2 Q4 Table 3 (relative humidity %, 9 am / 3 pm)
H9 = [100, 99, 95, 63, 81, 94, 96, 81, 73, 53, 57, 77, 51, 41]
H3 = [87, 75, 67, 57, 57, 74, 71, 62, 53, 54, 36, 39, 30, 32]
