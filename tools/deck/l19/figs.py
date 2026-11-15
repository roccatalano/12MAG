"""Data + plot helpers for lesson l19 (5C moving medians). ts()/scat() come from tools/deck/l17/figs.py.
tsm(): a ts() plot plus, for each smoothed time k, hidden guide lines (data-i="g{k}": vertical dashed at the middle time,
horizontal dashed at the median value) and a hidden red cross (data-i="m{k}"), and the joined smoothed line (data-i="ml")."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f17', os.path.join(H, '..', 'l17', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
ts, scat, MON, E8_B = _f.ts, _f.scat, _f.MON, _f.E8_B
_s2 = importlib.util.spec_from_file_location('f11', os.path.join(H, '..', 'l11', 'figs.py')); _g = importlib.util.module_from_spec(_s2); _s2.loader.exec_module(_g)
SC, WYR, WGOLD, WBEST = _g.scat, _g.WYR, _g.WGOLD, _g.WBEST


def mmed(ys, n):
    """n-moving median (n odd); None where there is no value"""
    h = n // 2
    return [None if k < h or k >= len(ys) - h else sorted(ys[k - h:k + h + 1])[h] for k in range(len(ys))]


def tsm(ys, meds=None, xs=None, guides=True, col='#d2475b', show=False, **kw):
    """ts() + median crosses. meds: list like mmed() output (None = no value). show=True: crosses and line visible (static, e.g. worksheet)."""
    svg = ts(ys, xs=xs, **kw)
    if meds is None: return svg
    xs = xs or list(range(1, len(ys) + 1))
    W, Hh, yr, xl, yl, xlab = kw.get('W', 560), kw.get('H', 280), kw.get('yr', (0, 10)), kw.get('xl', ''), kw.get('yl', ''), kw.get('xlab')
    xr = kw.get('xr') or (min(xs) - (1 if not xlab else .5), max(xs) + (1 if not xlab else .5))
    L, R, T, B = (58 if yl else 40), 14, 10, (48 if xl else 28)
    if xlab and any('<br>' in str(v) for v in xlab.values()): B += 16
    pw, ph = W - L - R, Hh - T - B
    X = lambda x: L + (x - xr[0]) / (xr[1] - xr[0]) * pw
    Y = lambda y: T + ph - (y - yr[0]) / (yr[1] - yr[0]) * ph
    hid = '' if show else ' class="hid0"'
    out = []
    pts = [(x, m) for x, m in zip(xs, meds) if m is not None]
    dd = ' '.join(('M' if k == 0 else 'L') + f'{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(pts))
    out.append(f'<path data-i="ml"{hid} d="{dd}" fill="none" stroke="{col}" stroke-width="2.6"/>')
    c = 6
    for k, (x, m) in enumerate(zip(xs, meds)):
        if m is None: continue
        if guides and not show:
            out.append(f'<g data-i="g{k}" class="hid0"><line x1="{X(x):.1f}" x2="{X(x):.1f}" y1="{T}" y2="{T+ph}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>'
                       f'<line x1="{L}" x2="{L+pw}" y1="{Y(m):.1f}" y2="{Y(m):.1f}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/></g>')
        out.append(f'<g data-i="m{k}"{hid}><path d="M{X(x)-c:.1f},{Y(m)-c:.1f}L{X(x)+c:.1f},{Y(m)+c:.1f}M{X(x)-c:.1f},{Y(m)+c:.1f}L{X(x)+c:.1f},{Y(m)-c:.1f}" stroke="{col}" stroke-width="3"/></g>')
    return svg.replace('</svg>', ''.join(out) + '</svg>')


# Learn: Cambridge U3&4 5C p. 278 'Locating medians graphically': points (1, 3), (3, 1), (4, 4) -> median point (3, 3)
LOC_X, LOC_Y = [1, 3, 4], [3, 1, 4]
# Cambridge Examples 12, 13 (pp. 278-280): births per month = Example 8/11 data (E8_B)
# Edrolo U3&4 4C Worked example 1 (pp. 254-256): Bailey's screen time (mins), days 1-7 (days 1-4 and 6 given in the text; 5, 7 read off the plot)
SCREEN = [82, 55, 70, 107, 81, 102, 113]
# Edrolo U3&4 4C Worked example 2 (pp. 257-259): Emanuel's goals saved, months 1-10 (months 1-6 in the text; rest read off, agree with the WE's medians)
GOALS = [18, 10, 17, 18, 25, 13, 11, 15, 7, 12]
# Do Now 1: VCAA 2024 NHT Exam 1 Q14 table (fruit drinks)
DRINK = [65, 84, 123, 154, 129, 187, 179, 71, 89, 131, 147, 141, 190, 185]
# Exit 1: VCAA 2021 Further Exam 1 Q13, points scored over 40 games (read off the plot; games 6-14 give the report's answer 110)
PTS = [110, 138, 128, 107, 121.5, 109.5, 108.5, 96.5, 110, 118, 102, 118, 134, 112, 113, 113, 101, 116, 107, 97.5, 96.5, 107.5, 114.5, 137,
       117.5, 114, 115, 105.5, 112.5, 98.5, 100, 124.5, 96.5, 102.5, 117.5, 105.5, 120, 105.5, 128.5, 140.5]
# Exit 2: VCAA 2016 Further Exam 2 Q4a, minimum rainfall (mm) per month (read off the plot; first four five-medians 53, 53, 59, 61 as printed)
RMIN = [14, 53, 36, 59, 95, 50, 83, 61, 74, 48, 67, 53]
# Exit 3: VCAA 2019 Further Exam 1 Q13-14 stem table: Liv's run times (min), days 1-9
LIV = [22, 40, 28, 51, 19, 60, 33, 37, 46]
# APK: VCAA 2020 Further Exam 2 Q3 table (BMI by neck size)
BMI = [('below average', 50, 18.1, 20.6, 21.6, 23.2, 26.8), ('average', 124, 19.8, 23.4, 24.6, 26.0, 33.9), ('above average', 76, 23.1, 26.25, 28.1, 29.95, 39.1)]
