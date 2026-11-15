"""Data + time series plot helper for lesson l17 (5B moving means). ts() copied from l16 with overlays= (smoothed series with gaps, hidden until shown)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f9', os.path.join(H, '..', 'l09', 'figs.py')); _f9 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f9)
scat, W_, corr, FOOT, lsq = _f9.scat, _f9.W_, _f9.corr, _f9.FOOT, _f9.lsq


def _n(v):
    return str(int(v)) if abs(v - round(v)) < 1e-9 else f'{v:g}'


def ts(ys, xs=None, yr=(0, 10), yt=1, xl='', yl='', W=560, H=280, fs=13, xlab=None, xtick=1, xr=None, sid='', ink='#1f4fb0', r=3.5,
       hidpts=False, hidline=False, tls=(), grid=True, ax=True, lw=2.2, vmarks=(), extra=(), hidfrom=None, overlays=()):
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
    for oys, col, nm, dash in overlays:  # smoothed series: None = no value (lost at the ends); hidden until data-show="#sid|nm"
        pts = [(x, y) for x, y in zip(xs, oys) if y is not None]
        dd = ' '.join(('M' if k == 0 else 'L') + f'{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(pts))
        s.append(f'<g data-i="{nm}" class="hid0"><path d="{dd}" fill="none" stroke="{col}" stroke-width="{lw+0.6}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'
                 + ''.join(f'<rect x="{X(x)-r:.1f}" y="{Y(y)-r:.1f}" width="{2*r:.1f}" height="{2*r:.1f}" fill="{col}"/>' for x, y in pts) + '</g>')
    s.append('</svg>')
    return ''.join(s)



def mm(ys, n):
    """n-moving mean (n odd), None where there is no value"""
    h = n // 2
    return [None if k < h or k >= len(ys) - h else round(sum(ys[k - h:k + h + 1]) / n, 1) for k in range(len(ys))]

# Cambridge U3&4 Example 7 (p. 268): 9 a.m. temperature for a week
E7_D = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']; E7_T = [18.1, 24.8, 26.4, 13.9, 12.7, 14.2, 24.9]
# Cambridge U3&4 Example 8 (p. 269): births per month in a country hospital
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
E8_B = [10, 12, 6, 5, 22, 18, 13, 7, 9, 10, 8, 15]
# Edrolo U3&4 4B Worked example 1 (p. 234): Dunedin daily rainfall (mm)
WE1_DAY = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']; WE1_R = [2, 3, 5, 5, 1, 0, 2]
# Edrolo U3&4 4B Worked example 3 (p. 243): Rubik's cube time taken (s), days 1-14, and Tobias's five-mean smoothed values
WE3_T = [120, 88, 112, 110, 83, 95, 101, 75, 91, 72, 108, 90, 65, 82]
WE3_S = [None, None, 102.6, 97.6, 100.2, 92.8, 89.0, 86.8, 89.4, 87.2, 85.2, 83.4, None, None]
# Exit 1: VCAA 2019 Exam 1 Q15-16 stem: monthly rainfall 2017 (read off the plot)
RAIN19 = [70, 132, 75, 135, 73, 53, 96, 120, 109, 111, 82, 247]
# Do Now 1: VCAA 2024 Exam 1 Q11-12 table
PAIRS = [320, 250, 225, 208, 190, 180, 170, 165, 160, 158, 155, 150]
# Do Now 2: VCAA 2026 NHT Exam 1 Q10 (read off the plot)
HEALTH = [(10, 200), (12, 250), (15, 350), (25, 800), (35, 1700), (45, 2500), (60, 4300), (65, 5200), (80, 7300), (95, 12300)]
# Do Now 3: VCAA 2023 Exam 2 Q4 (read off the plot), months 1-36
ICE = [0.168, 0.177, 0.173, 0.180, 0.192, 0.206, 0.173, 0.137, 0.127, 0.121, 0.135, 0.141, 0.156, 0.150, 0.158, 0.180, 0.200, 0.210, 0.183, 0.172, 0.162,
       0.145, 0.134, 0.154, 0.146, 0.170, 0.178, 0.197, 0.207, 0.224, 0.218, 0.190, 0.176, 0.154, 0.142, 0.135]
# Do Now 4: VCAA 2024 NHT Exam 2 Q4 (LLT, HHT) read off the scatterplot
TIDE = [(0.22, 2.02), (0.22, 1.98), (0.25, 1.90), (0.27, 2.01), (0.31, 1.78), (0.35, 1.96), (0.38, 1.64), (0.40, 1.81), (0.41, 1.84), (0.41, 1.76), (0.42, 1.85),
        (0.42, 1.39), (0.43, 1.68), (0.44, 1.84), (0.45, 1.58), (0.45, 1.40), (0.46, 1.77), (0.47, 1.57), (0.48, 1.81), (0.49, 1.87), (0.49, 1.66), (0.52, 1.50),
        (0.54, 1.77), (0.54, 1.60), (0.58, 1.47), (0.58, 1.41), (0.60, 1.71), (0.61, 1.46), (0.62, 1.65), (0.62, 1.59), (0.62, 1.52)]
# APK: VCAA 2017 Exam 1 Q3 (forearm circumference, cm)
ARM = ['26.0', '27.8', '28.4', '25.9', '28.3', '31.5', '28.2', '25.9', '27.9', '27.8']
