"""Data for lesson l20 (5D seasonal indices). Values read off the source figures/tables (VCAA plots redrawn).
ts/tsm/mmed/MON come from tools/deck/l19/figs.py; scat + the 2018 congestion data (V18) from tools/deck/l05/figs.py."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def _load(n, p):
    s = importlib.util.spec_from_file_location(n, os.path.join(H, '..', p, 'figs.py')); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
_f19 = _load('f19', 'l19'); _f5 = _load('f5', 'l05')
ts, tsm, mmed, MON = _f19.ts, _f19.tsm, _f19.mmed, _f19.MON
scat, CONG = _f5.scat, _f5.V18   # VCAA 2018 Further Exam 2 Q2 (morning, evening congestion level %, 19 cities)

# Do Now 1: VCAA 2023 Exam 1 Q13-14 stem: women's 800 m winning time (s), 2000-2022 (read off the plot; seven-median for 2006 = 116.8 as in the report)
W800_X = list(range(2000, 2023))
W800 = [116.4, 118.3, 115.2, 117.9, 116.4, 116.8, 117.2, 116.0, 116.0, 117.6, 118.0, 118.3, 117.6, 118.0, 117.6, 116.8, 117.6, 115.6, 114.4,
        118.2, 117.6, 115.2, 116.4]
# Do Now 2: VCAA 2026 NHT Exam 1 Q2-3 stem: shoe sizes of 46 adults (dot plot counts 5:2, 6:4, 7:7, 8:12, 9:9, 10:6, 11:3, 12:2, 13:1)
SHOE = sum(([s] * c for s, c in zip(range(5, 14), (2, 4, 7, 12, 9, 6, 3, 2, 1))), [])
# Do Now 3: VCAA 2024 Exam 2 Q4: Wgold (m), Olympic years 1952-1988 (read off the plot; five-medians 1.82, 1.85 printed for 1960, 1964)
OLY = list(range(1952, 1989, 4))
WG = [1.67, 1.76, 1.85, 1.90, 1.82, 1.92, 1.93, 1.97, 2.02, 2.01]
# Learn 1: Cambridge U3&4 5D p. 284 hypothetical unemployment seasonal indices
UNEMP = [1.1, 1.2, 1.1, 1.0, 0.95, 0.95, 0.9, 0.9, 0.85, 0.85, 1.1, 1.1]
UMON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
# Exit 2: VCAA 2020 Further Exam 1 Q17-18 Table 4 (monthly rainfall 2019, mm, and seasonal indices)
RAIN = [18.4, 17.6, 46.8, 23.6, 92.6, 77.2, 80.0, 86.8, 93.8, 55.2, 97.3, 69.4]
RSI = [0.728, 0.734, 0.741, 0.934, 1.222, 0.973, 1.024, 1.121, 1.159, 1.156, 1.138, 1.072]
RMON = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
