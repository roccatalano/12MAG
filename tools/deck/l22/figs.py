"""Data for lesson l22 (5E, trend lines and forecasting). Values from the source tables (no plots read off).
ts comes from tools/deck/l16/figs.py (via l19)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f19', os.path.join(H, '..', 'l19', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
ts = _f.ts
# Cambridge U3&4 Example 20 (p. 295-296): female Year 12 maths students, Victoria 2010-18
FEM_X = list(range(2010, 2019)); FEM = [76260, 78707, 79797, 79952, 78237, 80858, 81587, 83820, 84069]
# Cambridge Example 22 (p. 297): Mikki's deseasonalised sales, quarters 1-12; SIs from Example 18
MDS = [893, 943, 955, 858, 1005, 1026, 1043, 1040, 1261, 1151, 1115, 1267]
# Edrolo U3&4 4E WE1 (p. 280): library visitors, days 1-7
LIB = [94, 114, 120, 153, 178, 191, 221]
# Edrolo 4E WE2 (pp. 282-284): NRL jersey sales Jan-Jun 2022 + seasonal indices Jan-Dec
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
JER = [479, 513, 1127, 894, 800, 802]
JSI = ['0.55', '0.63', '1.40', '1.21', '1.11', '1.19', '1.23', '1.19', '1.25', '0.58', '0.52', '1.14']
JDS = ['870.9', '814.3', '805.0', '738.8', '720.7', '673.9']
# Do Now 2: VCAA 2026 Exam 1 Q10-11 stem table (likes per day)
LIKES = [51, 55, 65, 72, 95, 121, 226, 341, 535, 841]
# Do Now 3: VCAA 2023 Exam 2 Q4c Table 4 (ice cream, litres/person, 2011)
ICE = ['0.156', '0.150', '0.158', '0.180', '0.200', '0.210', '0.183', '0.172', '0.162', '0.145', '0.134', '0.154']
# Do Now 4: VCAA 2026 Exam 2 Q1 table (happiness index 2022)
HAPPY = [('Finland', '7.82'), ('Denmark', '7.64'), ('Iceland', '7.56'), ('Switzerland', '7.51'), ('Netherlands', '7.42'), ('Luxembourg', '7.40'),
         ('Sweden', '7.38'), ('Norway', '7.37'), ('Israel', '7.36'), ('New Zealand', '7.20'), ('Austria', '7.16'), ('Australia', '7.16')]
# Exit: VCAA 2018 Further Exam 2 Q3 Table 3 (congestion level %, 2008-16)
YRS = list(range(2008, 2017)); MEL = [25, 26, 26, 27, 28, 28, 28, 29, 33]; SYD = [28, 30, 32, 33, 34, 34, 35, 36, 39]
