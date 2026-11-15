"""Data for lesson l18 (5B, centring). Plot helpers ts()/scat()/mm() come from tools/deck/l17/figs.py."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f17', os.path.join(H, '..', 'l17', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
ts, scat, mm, MON, E7_D, E7_T, E8_B = _f.ts, _f.scat, _f.mm, _f.MON, _f.E7_D, _f.E7_T, _f.E8_B


def mmc(ys, n):
    """n-moving mean with centring (n even): mean of the two n-means either side; None where there is no value (unrounded)"""
    h = n // 2
    out = []
    for k in range(len(ys)):
        if k < h or k >= len(ys) - h: out.append(None); continue
        a = sum(ys[k - h:k + h]) / n; b = sum(ys[k - h + 1:k + h + 1]) / n
        out.append((a + b) / 2)
    return out

# Edrolo U3&4 4B Worked example 2 (pp. 239-243): Amelia's distance run (km) per month, with Edrolo's answers (1 d.p.)
WE2_D = [42, 47, 39, 41, 37, 35, 36, 28, 31, 28, 35, 41]
WE2_2 = [None, 43.8, 41.5, 39.5, 37.5, 35.8, 33.8, 30.8, 29.5, 30.5, 34.8, None]
WE2_4 = [None, None, 41.6, 39.5, 37.6, 35.6, 33.3, 31.6, 30.6, 32.1, None, None]
# Do Now 1: VCAA 2026 NHT Exam 1 Q13-14 stem, closing share price days 1-10 (read off the plot; agrees with the report's working)
SHARE = [5.50, 5.70, 5.60, 5.70, 5.80, 6.00, 6.20, 5.90, 6.50, 5.60]
# Do Now 2: VCAA 2024 NHT Exam 1 Q11-12 stem table
BIRTH = [27.18, 26.78, 25.21, 26.44, 26.14, 20.60, 17.55, 18.24, 15.69, 11.35, 8.15, 7.72]
INCOME = [2460, 5211, 9846, 12706, 15176, 16304, 17402, 20463, 20615, 23285, 23926, 24364]
# Do Now 3: VCAA 2025 Exam 2 Q4 scatterplot (distance km, sale price $), read off the plot
HOUSE = [(5.1, 880000), (5.15, 920000), (5.2, 980000), (5.25, 1870000), (5.7, 1170000), (5.8, 1130000), (6.5, 1380000), (6.5, 1280000), (7.3, 1740000),
         (7.5, 1760000), (7.5, 1550000), (7.3, 1150000), (7.9, 1000000), (8.2, 1530000), (8.4, 2350000), (9.2, 1560000), (9.7, 2320000), (10.1, 1410000),
         (13.1, 1360000), (13.8, 950000), (14.2, 950000), (14.3, 2260000), (14.3, 1500000), (15.5, 1250000)]
# Do Now 4: VCAA 2024 Exam 2 Q4, women's high jump gold height (m), 1952-1988 (read off the plot)
YEARS = list(range(1952, 1989, 4)); WGOLD = [1.67, 1.76, 1.85, 1.90, 1.82, 1.92, 1.93, 1.97, 2.02, 2.01]
# APK: VCAA 2020 Exam 2 Q4 table (age, body density, weight)
AGE = [23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25]
DENS = ['1.07', '1.07', '1.08', '1.08', '1.03', '1.05', '1.07', '1.06', '1.07', '1.09', '1.02', '1.09']
WT = ['70.1', '90.4', '73.2', '85.0', '84.3', '95.6', '71.7', '95.0', '80.2', '87.4', '94.9', '65.3']
# Exit 1: VCAA 2017 Exam 1 Q15, max wind speed week 2 (days 8-14)
WIND_D = list(range(8, 15)); WIND = [22, 22, 19, 22, 43, 37, 33]
# Exit 2: VCAA 2016 Exam 2 Q4b table, maximum daily rainfall (mm) per month
RAIN16 = [79, 123, 100, 156, 174, 186, 149, 162, 124, 140, 225, 119]
