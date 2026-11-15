"""Data + time series plot helper for lesson l16 (5A). Values read off the source figures (plots redrawn; points approximate where read off a plot)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f9', os.path.join(H, '..', 'l09', 'figs.py')); _f9 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f9)
scat, W_, corr, FOOT, lsq = _f9.scat, _f9.W_, _f9.corr, _f9.FOOT, _f9.lsq


def _n(v):
    return str(int(v)) if abs(v - round(v)) < 1e-9 else f'{v:g}'


def ts(ys, xs=None, yr=(0, 10), yt=1, xl='', yl='', W=560, H=280, fs=13, xlab=None, xtick=1, xr=None, sid='', ink='#1f4fb0', r=3.5,
       hidpts=False, hidline=False, tls=(), grid=True, ax=True, lw=2.2, vmarks=(), extra=(), hidfrom=None):
    """Time series plot. ys values; xs times (default 1..n); xlab: {x: label} for category ticks (else numeric every xtick).
    Points data-i="p{k}" (+ "p"), segments data-i="s{k}" (+ "s"), trend lines tls = [((x1,y1),(x2,y2),name)] data-i=name (hidden until shown).
    hidpts/hidline: start hidden (revealed with data-show)."""
    xs = xs or list(range(1, len(ys) + 1))
    xr = xr or (min(xs) - (1 if not xlab else .5), max(xs) + (1 if not xlab else .5))
    L, R, T, B = (58 if yl else 40), 14, 10, (48 if xl else 28)
    if xlab and any('<br>' in str(v) for v in xlab.values()): B += 16
    pw, ph = W - L - R, H - T - B
    X = lambda x: L + (x - xr[0]) / (xr[1] - xr[0]) * pw
    Y = lambda y: T + ph - (y - yr[0]) / (yr[1] - yr[0]) * ph
    s = [f'<svg{" id=" + chr(34) + sid + chr(34) if sid else ""} viewBox="0 0 {W} {H}" width="100%" style="display:block">']
    v = yr[0]
    while v <= yr[1] + 1e-9:
        if grid: s.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#e3e6ee"/>')
        s.append(f'<text x="{L-6}" y="{Y(v)+4.5:.1f}" text-anchor="end" font-size="{fs-1}">{_n(v)}</text>')
        v += yt
    if xlab:
        for x, lab in xlab.items():
            parts = str(lab).split('<br>')
            for j, p in enumerate(parts):
                s.append(f'<text x="{X(x):.1f}" y="{T+ph+17+j*15}" text-anchor="middle" font-size="{fs-1}">{p}</text>')
            s.append(f'<line x1="{X(x):.1f}" x2="{X(x):.1f}" y1="{T+ph}" y2="{T+ph+4}" stroke="#333"/>')
    else:
        v = xr[0] if xr[0] % xtick == 0 else xr[0] + (xtick - xr[0] % xtick)
        while v <= xr[1] + 1e-9:
            if grid: s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{T}" y2="{T+ph}" stroke="#eef0f5"/>')
            s.append(f'<text x="{X(v):.1f}" y="{T+ph+17}" text-anchor="middle" font-size="{fs-1}">{_n(v)}</text>')
            v += xtick
    s.append(f'<line x1="{L}" x2="{L+pw}" y1="{T+ph}" y2="{T+ph}" stroke="#333" stroke-width="2"/><line x1="{L}" x2="{L}" y1="{T}" y2="{T+ph}" stroke="#333" stroke-width="2"/>')
    if xl: s.append(f'<text x="{L+pw/2:.1f}" y="{H-6}" text-anchor="middle" font-size="{fs}" font-weight="600" font-style="italic">{xl}</text>')
    if yl: s.append(f'<text x="14" y="{T+ph/2:.1f}" text-anchor="middle" font-size="{fs}" font-weight="600" font-style="italic" transform="rotate(-90 14 {T+ph/2:.1f})">{yl}</text>')
    for x, lab in vmarks:
        s.append(f'<g data-i="vm" class="hid0"><line x1="{X(x):.1f}" x2="{X(x):.1f}" y1="{T}" y2="{T+ph}" stroke="#d2475b" stroke-width="2" stroke-dasharray="6 4"/>'
                 f'<text x="{X(x)+4:.1f}" y="{T+12}" font-size="{fs-1}" fill="#d2475b" font-weight="700">{lab}</text></g>')
    for ey, col, dash in extra:
        dd = ' '.join(('M' if k == 0 else 'L') + f'{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(zip(xs, ey)))
        s.append(f'<path d="{dd}" fill="none" stroke="{col}" stroke-width="{lw}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')
    for k in range(len(ys) - 1):
        if ys[k] is None or ys[k + 1] is None: continue
        hl = ' class="hid0"' if hidline or (hidfrom is not None and k + 1 >= hidfrom) else ''
        s.append(f'<line data-i="s{k}"{hl} x1="{X(xs[k]):.1f}" y1="{Y(ys[k]):.1f}" x2="{X(xs[k+1]):.1f}" y2="{Y(ys[k+1]):.1f}" stroke="{ink}" stroke-width="{lw}"/>')
    for k, (x, y) in enumerate(zip(xs, ys)):
        if y is None: continue
        hp = ' class="hid0"' if hidpts or (hidfrom is not None and k >= hidfrom) else ''
        s.append(f'<g data-i="p"><circle data-i="p{k}"{hp} cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{r}" fill="{ink}"/></g>')
    for (a, b), (c, d), nm in tls:
        s.append(f'<line data-i="{nm}" class="hid0" x1="{X(a):.1f}" y1="{Y(b):.1f}" x2="{X(c):.1f}" y2="{Y(d):.1f}" stroke="#d2475b" stroke-width="3" stroke-dasharray="9 6"/>')
    s.append('</svg>')
    return ''.join(s)


# ---------------- data ----------------
# Cambridge U3&4 Example 1 (p. 254): maximum temperature for a week
E1_DAYS = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']; E1_T = [20, 21, 25, 36, 34, 25, 26]
# Edrolo U3&4 4A Worked example 1 (p. 223): UK deaths and serious injuries, Oct 1982 - Dec 1983 (table)
WE1_M = ['Oct<br>1982', 'Nov<br>1982', 'Dec<br>1982', 'Jan<br>1983', 'Feb<br>1983', 'Mar<br>1983', 'Apr<br>1983', 'May<br>1983', 'Jun<br>1983', 'Jul<br>1983',
         'Aug<br>1983', 'Sep<br>1983', 'Oct<br>1983', 'Nov<br>1983', 'Dec<br>1983']
WE1_D = [1850, 1998, 2079, 1494, 1057, 1218, 1168, 1236, 1076, 1174, 1139, 1427, 1487, 1483, 1513]
# Cambridge Example 2 (p. 258): Australian birth rate 1932-1989 (read off the plot)
BIRTH = [2.08, 1.94, 1.90, 1.85, 1.86, 1.90, 1.95, 1.94, 1.97, 2.07, 2.18, 2.20, 2.30, 2.37, 2.55, 2.80, 2.87, 2.78, 2.78, 2.87, 2.85, 2.97, 3.00, 3.05,
         3.12, 3.15, 3.25, 3.27, 3.28, 3.40, 3.30, 3.20, 3.00, 2.82, 2.75, 2.72, 2.75, 2.75, 2.72, 2.82, 2.60, 2.40, 2.25, 2.10, 1.98, 1.90, 1.85, 1.82,
         1.80, 1.81, 1.82, 1.78, 1.84, 1.80, 1.78, 1.80, 1.78, 1.75]
BIRTH_Y = list(range(1932, 1932 + len(BIRTH)))
# Cambridge Example 3 (p. 259): sunspots 1945-2016 (read off the plot)
SUN = [31, 100, 170, 165, 172, 103, 67, 30, 12, 4, 34, 122, 166, 170, 143, 100, 45, 29, 20, 6, 11, 38, 85, 93, 102, 105, 66, 66, 37, 31, 13, 12, 25, 87,
       142, 146, 144, 113, 64, 43, 15, 11, 28, 100, 160, 142, 141, 94, 54, 30, 18, 8, 20, 58, 96, 121, 121, 107, 64, 41, 30, 15, 7, 3, 3, 14, 48, 53, 58, 72, 46, 24]
SUN_Y = list(range(1945, 1945 + len(SUN)))
# Cambridge Example 4 (p. 260): hotel room occupancy rate (%), Mar 2012 - Jun 2016 (read off the plot)
HOTEL = [72.0, 68.4, 72.4, 72.2, 71.5, 67.6, 72.0, 73.0, 72.0, 68.3, 72.7, 73.5, 72.0, 69.0, 73.2, 73.7, 72.4, 70.5]
HOTEL_LAB = {k + 1: ['Mar', 'Jun', 'Sep', 'Dec'][k % 4] + ('<br>' + str(2012 + k // 4) if k % 4 == 1 else '') for k in range(18)}
# Cambridge Example 5 (p. 261): electricity use (kWh) by month (read off the plot)
POWER = [290, 250, 330, 295, 310, 300, 170, 160, 170, 155, 145, 158]
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Cambridge Example 6 (p. 261): daily electricity use (kWh) for a fortnight (read off the plot)
DAILY = [9.6, 10.5, 10.7, 1.6, 10.4, 10.1, 11.1, 9.8, 8.6, 10.7, 10.7, 10.3, 10.0, 11.2]
# Edrolo U3&4 4A Worked example 2 (p. 227): deaths and serious injuries, Sep 1980 - Sep 1984 (months 1-49, read off the plot)
WE2 = [1550, 1830, 1740, 1950, 1880, 1450, 1530, 1400, 1520, 1390, 1630, 1500, 1680, 1900, 1890, 1960, 1870, 1720, 1460, 1450, 1460, 1360, 1490, 1560,
       1490, 1680, 1780, 2080, 2000, 1490, 1050, 1220, 1180, 1230, 1080, 1170, 1140, 1420, 1480, 1500, 1480, 1360, 1170, 1290, 1110, 1300, 1200, 1280, 1400]
# Written You trys (planner/written-youtrys.json)
YT2 = [41, 44, 48, 51, 55, 58, 62, 60, 57, 53, 50, 46, 44, 41, 38]
YT3 = [20, 45, 90, 60, 30, 15, 25, 55, 95, 70, 35, 20, 15, 40, 85, 65, 30, 20, 30, 60, 100, 70, 35, 20]
YT5 = [22, 21, 23, 22, 20, 21, 38, 37, 39, 38, 40, 39]
YT6 = [82, 85, 80, 84, 83, 81, 86, 84, 150, 83, 82, 85, 80, 84]
# Exits (Edrolo U3&4 4A Exam practice, p. 232)
MEL = [25, 26, 26, 27, 28, 28, 28, 29, 33]; SYD = [28, 30, 32, 33, 34, 34, 35, 36, 39]   # VCAA 2018 Exam 2 Q3a (table)
TEMP16 = [21.3, 20, 17.5, 16.2, 11.2, 10.7, 9.3, 12.6, 14.4, 16.6, 20, 20.8, 22, 23.3, 23.3, 19, 17.3, 11.9, 10, 9.9, 10.3, 13.8, 16.5, 19.6, 22, 25.2,
          26.2, 23.2, 16.6, 13.6, 11, 11.4, 11.4, 15.6, 14.9, 18.1, 21.5, 22.4, 20.8, 19.2, 15.5, 12.6, 10.3, 8.6, 9.4, 13.8, 21.1, 19.7, 22.3]  # VCAA 2016 E1 Q13, months 0-48
SALES21 = [200, 585, 385, 125, 410, 315, 525, 355, 280, 108, 300, 460, 100, 270, 480, 255, 335, 428, 400, 260, 85, 380, 485, 245, 80, 205, 450, 280,
           165, 345, 415, 365, 50, 430, 340, 205, 88, 75, 335, 350, 128]  # VCAA 2021 E1 Q12, quarterly 2010-2020
# Do Now 4: VCAA 2025 NHT Exam 2 Q4 (father's height, son's height in m; read off the scatterplot)
FS = [(1.63, 1.73), (1.63, 1.68), (1.65, 1.69), (1.68, 1.78), (1.68, 1.67), (1.69, 1.78), (1.69, 1.74), (1.70, 1.73), (1.71, 1.77), (1.71, 1.75),
      (1.73, 1.73), (1.73, 1.70), (1.73, 1.68), (1.74, 1.85), (1.74, 1.73), (1.75, 1.83), (1.75, 1.77), (1.75, 1.75), (1.78, 1.91), (1.78, 1.83),
      (1.78, 1.78), (1.78, 1.65), (1.79, 1.78), (1.79, 1.75), (1.79, 1.74), (1.80, 1.83), (1.80, 1.75), (1.83, 1.82), (1.85, 1.80), (1.85, 1.70)]
# VCAA 2024 Exam 2 Q3 Table 2
OLY_Y = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
WGOLD = ['1.92', '1.93', '1.97', '2.02', '2.03', '2.02', '2.05', '2.01', '2.06', '2.05', '2.05', '1.97', '2.04']
WBEST = ['1.94', '1.96', '1.98', '2.07', '2.07', '2.05', '2.05', '2.02', '2.06', '2.06', '2.05', '2.01', '2.05']


def keys_(pre, n): return ','.join(f'{pre}{k}' for k in range(n))
# Cambridge U1&2 Ch 7 skills checklist 7D #7 (age of car, kms; read off the scatterplot); fitted line (0, 10 000) to (10, 62 000)
CARS = [(1, 3000), (1, 4000), (1, 8000), (1, 1000), (2, 28000), (2, 29000), (2, 24000), (2, 20000), (3, 51000), (4, 25000), (4, 16000), (4, 13000),
        (5, 45000), (5, 33000), (5, 16000), (6, 60000), (6, 19000), (6, 5000), (7, 54000), (7, 45000), (8, 80000), (8, 45000), (8, 42000), (9, 40000), (10, 58000)]
