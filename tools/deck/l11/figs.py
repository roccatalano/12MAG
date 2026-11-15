"""Data for lesson l11 (3C). Values read off the source figures/tables (VCAA, Cambridge and Edrolo plots redrawn; points read off the grid)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f10', os.path.join(H, '..', 'l10', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
scat, W_, corr, lsq, CARS, PRESS, CONG = _f.scat, _f.W_, _f.corr, _f.lsq, _f.CARS, _f.PRESS, _f.CONG
_s = importlib.util.spec_from_file_location('f7', os.path.join(H, '..', 'l07', 'figs.py')); _g = importlib.util.module_from_spec(_s); _s.loader.exec_module(_g)
WYR, WGOLD, WBEST = _g.WYR, _g.WGOLD, _g.WBEST

def line(svg, pts, xr, yr, xl, yl, W, H, col='#1f4fb0'):
    """Add a solid line joining pts (time series) to an svg made by scat with the same xr, yr, xl, yl, W, H."""
    L, R, T, B = (58 if yl else 40), 16, 12, (50 if xl else 30); pw, ph = W - L - R, H - T - B
    X = lambda x: L + (x - xr[0]) / (xr[1] - xr[0]) * pw; Y = lambda y: T + ph - (y - yr[0]) / (yr[1] - yr[0]) * ph
    d = ' '.join(('M' if k == 0 else 'L') + f'{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(pts))
    return svg.replace('</svg>', f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2"/></svg>', 1)
def ts(pts, xr, yr, xt, yt, xl, yl, W=440, H=240, **k): return line(scat(pts, xr, yr, xt, yt, xl, yl, W=W, H=H, **k), pts, xr, yr, xl, yl, W, H)
def resid(pts, xr, yr, xt, yt, xl='', yl='residual', **k): return scat(pts, xr, yr, xt, yt, xl, yl, tl=((xr[0], 0), (xr[1], 0)), tl_hid=False, **k)

# VCAA 2026 NHT Exam 1 Q9 (day, minimum temperature)
MINT = [(1, 8), (2, 10), (3, 7), (4, 9), (5, 8)]
# VCAA 2017 Further Exam 1 Q8-10 (ankle, wrist circumference cm; 13 people)
WRIST = [(21.5, 17.7), (21.9, 17.1), (22.8, 18.2), (22.9, 17.7), (23.2, 18.8), (23.4, 18.2), (23.7, 18.8), (23.8, 18.2), (24, 17.7), (25, 19.2), (25.2, 18.5), (25.6, 18.8), (25.9, 19.0)]
# VCAA 2016 Further Exam 2 Q3 (actual, apparent temperature; table)
APP = [24.7, 24.3, 24.9, 23.2, 24.2, 22.6, 21.5, 20.6, 19.4, 18.4, 17.6, 18.7, 18.2]; ACT = [28.5, 27.6, 27.7, 26.9, 26.6, 25.5, 24.4, 23.8, 22.3, 22.1, 20.9, 21.2, 20.5]
# Cambridge U3&4 Example 7 residual plots A-D
EX7 = {'A': [(0.5, -.75), (.8, .55), (1.2, .1), (3, -.4), (4.5, -.13), (5, .35), (5.5, -.65), (6.7, .17), (6.8, .55), (7.2, -.17), (9, -.38), (10.8, .55), (11, -.62), (11.2, 0)],
       'B': [(1, .25), (2.5, -.22), (3.3, -.42), (4.3, -.08), (4.6, -.26), (5.4, .22), (6.6, .07), (6.8, .37), (9, .62), (9.2, .32), (11, .35), (11.7, 0)],
       'C': [(1.8, -.22), (2.6, .24), (3.4, .46), (4, -.42), (4.1, .22), (5, -.03), (6, .25), (6.6, -.42), (7, .01), (8, .4), (8, -.13), (8, -.5)],
       'D': [(1.3, -.13), (1.6, .18), (2.9, .25), (3.1, -.13), (3.9, .08), (5, .14), (5.3, -.03), (6.9, .03), (7.3, -.3), (7.8, -.12), (8.9, -.75), (9.1, -.4)]}
# Edrolo U3&4 3C Worked example 3 residual plots a, b
EW3 = {'a': [(1, -2.5), (1.3, -1.6), (1.5, -.8), (2, 1.7), (3.4, 3.4), (4.8, 4.1), (5.8, 2.3), (6.1, .5), (6.3, -.3), (6.6, -1.9), (6.9, -3)],
       'b': [(1.2, -1), (1.5, 2), (2.3, -2.4), (3.6, 2.2), (4.5, -1.8), (5, 1.8), (6.3, .5), (6.7, -1.9), (7.1, 1.3), (8, -1.4), (9, 1)]}
# Edrolo U3&4 3C Worked example 2 (number of people, total cost $)
PPL = [3, 4, 1, 6, 5, 2, 2, 4]; COST = [90, 133, 29, 174, 154, 73, 62, 129]
# VCAA 2019 Further Exam 2 Q5f residual plot (pressure 9 am, residual hPa; 23 days)
PRES = [(1013.2, 2.45), (1013.8, -.05), (1014.4, -.15), (1014.5, .85), (1014.6, 1.05), (1015.7, -.75), (1015.7, -1.25), (1016.8, .7), (1017.8, 0), (1018.4, -1.75),
        (1018.7, -.4), (1018.8, .3), (1019.1, -1.25), (1020.4, -1.25), (1021.9, -1.25), (1022, 1.05), (1022.9, -.95), (1023.4, -.3), (1024.6, -.65), (1025.7, -.1),
        (1026.5, 1.95), (1026.6, .85), (1027.2, .75)]
# VCAA 2021 Further Exam 2 Q3 (year, women's 100 m freestyle winning time s)
SWIM = list(zip(range(1956, 2017, 4), [62.0, 61.2, 59.5, 60.0, 58.6, 55.65, 54.8, 55.9, 55.0, 54.65, 54.5, 53.83, 53.84, 53.1, 53.0, 52.7]))
# Cambridge U3&4 3C CAS 2 (birth rate per 1000, life expectancy years; 10 countries)
BIRTH = [30, 38, 38, 43, 34, 42, 31, 32, 26, 34]; LIFE = [66, 54, 43, 42, 49, 45, 64, 61, 61, 66]
# YT-3B-8 (written for 12MAG): motorbikes
MAGE = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]; MPR = [14800, 13900, 13100, 12600, 11200, 10500, 9800, 9300, 8100, 7400]
