"""Data for lesson l21 (5D, calculating seasonal indices and deseasonalising). Values from the source tables; VCAA plots redrawn (values read off).
ts/tsm come from tools/deck/l19/figs.py (l16 ts), scat from tools/deck/l05/figs.py."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def _load(n, p):
    s = importlib.util.spec_from_file_location(n, os.path.join(H, '..', p, 'figs.py')); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
_f19 = _load('f19', 'l19'); _f5 = _load('f5', 'l05')
ts, tsm, mmed = _f19.ts, _f19.tsm, _f19.mmed
scat = _f5.scat
# Do Now 2: VCAA 2024 NHT Exam 1 Q13: men's 1500 m winning time (s), 2004-2016 (read off the plot, grid 0.2 s)
M15_X = list(range(2004, 2017))
M15 = [207.4, 209.4, 209.0, 210.6, 211.4, 210.0, 209.2, 210.4, 208.8, 207.8, 207.4, 207.8, 209.0]
# Do Now 3: VCAA 2026 NHT Exam 2 Q4b table (mean monthly sunspot numbers, month 1 = March 1990)
SUN = [200.6, 198.7, 196.1, 192.9, 191.7, 192.7, 194.6, 195.1, 193.3, 197.1, 203.8, 207.6, 201.2, 203.4, 200.3, 202.9, 203.0, 205.7]
# Do Now 4: VCAA 2024 Exam 2 Q3 (Table 2); residuals from Wbest = 0.300 + 0.860 x Wgold (match the printed residual plot)
WG = [1.92, 1.93, 1.97, 2.02, 2.03, 2.02, 2.05, 2.01, 2.06, 2.05, 2.05, 1.97, 2.04]
WB = [1.94, 1.96, 1.98, 2.07, 2.07, 2.05, 2.05, 2.02, 2.06, 2.06, 2.05, 2.01, 2.05]
RES = [(x, round(y - (0.3 + 0.86 * x), 4)) for k, (x, y) in enumerate(zip(WG, WB)) if k != 3]   # 1984 point (part f) missing
# Cambridge Examples 17-19: Mikki's shop (customers per quarter, 3 years)
MIK = [[920, 1085, 1241, 446], [1035, 1180, 1356, 541], [1299, 1324, 1450, 659]]
MSI = ['1.03', '1.15', '1.30', '0.52']
MDES = [[893, 943, 955, 858], [1005, 1026, 1043, 1040], [1261, 1151, 1115, 1267]]
# Edrolo 4D WE2 / WE3
E2 = [[45, 30, 22, 51], [53, 29, 26, 60], [54, 41, 29, 72]]
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
E3SI = ['0.70', '1.35', '0.80', '0.75', '1.20', '1.70', '0.50']
E3N = ['7500', '14 000', '6000', '8000', '13 000', '17 000', '4000']
E3D = ['10 714', '10 370', '7500', '10 667', '10 833', '10 000', '8000']
