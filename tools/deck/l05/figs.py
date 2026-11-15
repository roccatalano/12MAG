"""Figures for lesson l05 (2D, 2E): scatterplots (slides + worksheet).
All redrawn from the source figures (point values read off them; Example 15 and Edrolo 6B WE1/WE3 point clouds are close approximations).
data-i keys: every point 'p' (and 'p<k>' for point k); trend line 'tl' (hidden until shown when tl_hid=True)."""
import random

def _n(v): return ('%g' % v)

def scat(pts, xr, yr, xt, yt, xl='', yl='', W=520, H=380, r=5, fs=15, tl=None, tl_hid=True, grid=True, ink='#1f4fb0',
         hid=False, ticks=True, curve=None, sid=''):
    """pts [(x,y)]; xr/yr (lo,hi); xt/yt tick step; tl ((x1,y1),(x2,y2)) dashed trend line; curve = list of (x,y) for a dashed curve."""
    L, R, T, B = (58 if yl else 40), 16, 12, (50 if xl else 30)
    pw, ph = W - L - R, H - T - B
    X = lambda x: L + (x - xr[0]) / (xr[1] - xr[0]) * pw
    Y = lambda y: T + ph - (y - yr[0]) / (yr[1] - yr[0]) * ph
    s = [f'<svg{" id="+chr(34)+sid+chr(34) if sid else ""} viewBox="0 0 {W} {H}" width="100%" style="display:block">']
    v = xr[0]
    while v <= xr[1] + 1e-9:
        if grid: s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{T}" y2="{T+ph}" stroke="#e3e6ee"/>')
        if ticks: s.append(f'<text x="{X(v):.1f}" y="{T+ph+19}" text-anchor="middle" font-size="{fs-1}">{_n(v)}</text>')
        v += xt
    v = yr[0]
    while v <= yr[1] + 1e-9:
        if grid: s.append(f'<line x1="{L}" x2="{L+pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#e3e6ee"/>')
        if ticks: s.append(f'<text x="{L-7}" y="{Y(v)+5:.1f}" text-anchor="end" font-size="{fs-1}">{_n(v)}</text>')
        v += yt
    s.append(f'<line x1="{L}" x2="{L+pw}" y1="{T+ph}" y2="{T+ph}" stroke="#333" stroke-width="2"/><line x1="{L}" x2="{L}" y1="{T}" y2="{T+ph}" stroke="#333" stroke-width="2"/>')
    if xl: s.append(f'<text x="{L+pw/2:.1f}" y="{H-8}" text-anchor="middle" font-size="{fs}" font-weight="600" font-style="italic">{xl}</text>')
    if yl: s.append(f'<text x="15" y="{T+ph/2:.1f}" text-anchor="middle" font-size="{fs}" font-weight="600" font-style="italic" transform="rotate(-90 15 {T+ph/2:.1f})">{yl}</text>')
    h = ' class="hid0"' if tl_hid else ''
    if tl:
        (a, b), (c, d) = tl
        s.append(f'<line data-i="tl"{h} x1="{X(a):.1f}" y1="{Y(b):.1f}" x2="{X(c):.1f}" y2="{Y(d):.1f}" stroke="#d2475b" stroke-width="3" stroke-dasharray="9 6"/>')
    if curve:
        dd = ' '.join(('M' if k == 0 else 'L') + f'{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(curve))
        s.append(f'<path data-i="tl"{h} d="{dd}" fill="none" stroke="#d2475b" stroke-width="3" stroke-dasharray="9 6"/>')
    hp = ' class="hid0"' if hid else ''
    for k, (x, y) in enumerate(pts):
        s.append(f'<g data-i="p"{hp}><circle data-i="p{k}" cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{r}" fill="{ink}"/></g>')
    s.append('</svg>')
    return ''.join(s)

def W_(px, inner): return f'<div style="width:{px}px;max-width:100%">{inner}</div>'

# ---------------- data (read off the source figures) ----------------
# VCAA 2018 Further Exam 2 Core Q2: morning vs evening congestion level, 19 cities
V18 = [(37,41),(41,48),(44,51),(46,51),(47,50),(48,52),(49,54),(50,62),(51,53),(52,50),(55,64),(56,56),(57,64),(57,60),(61,60),(62,67),(64,68),(65,68),(69,74)]
# VCAA 2016 Further Exam 2 Core Q3: (actual, apparent) temperature, from the table
V16 = [(28.5,24.7),(27.6,24.3),(27.7,24.9),(26.9,23.2),(26.6,24.2),(25.5,22.6),(24.4,21.5),(23.8,20.6),(22.3,19.4),(22.1,18.4),(20.9,17.6),(21.2,18.7),(20.5,18.2)]
# VCAA 2020 Exam 2 Q4 table (age, body density, weight)
V20 = [(23,1.07,70.1),(23,1.07,90.4),(23,1.08,73.2),(23,1.08,85.0),(24,1.03,84.3),(24,1.05,95.6),(24,1.07,71.7),(24,1.06,95.0),(25,1.07,80.2),(25,1.09,87.4),(25,1.02,94.9),(25,1.09,65.3)]
# Cambridge U1&2 Ch 7 checklist #2/#3: (height, foot length)
FOOT = [(172,24),(172,22),(177,28),(165,20),(176,28),(155,25),(166,22),(166,30),(182,32),(160,26),(153,22),(177,28),(172,26),(173,25),(185,40),(159,24)]
# Cambridge 2D CAS 1 test scores
TEST1 = [10,18,13,6,8,5,12,15,15]; TEST2 = [12,20,11,9,6,6,12,13,17]
# Cambridge 2D: participation rate vs hours worked (9 countries)
PART = [(26,35),(20,43),(36,38),(1,50),(25,40),(9,50),(30,40),(3,53),(55,35)]
# Cambridge Example 13
E13A = [(0.1,70),(0.3,64),(0.5,48),(1,35),(1.9,20),(2.4,24),(3.6,18),(4,16),(5,11),(5.3,11)]
E13B = [(21,6.5),(22,12.5),(23.5,11.5),(23.5,22.5),(23.5,7.5),(25,7.5),(27.5,11),(28.5,10),(29,13.5),(29.5,7),(30,10),(31.5,5.5),(33,15),(34,9)]
E13C = [(150,160),(155,164),(158,152),(160,175),(163,163),(165,172),(167,168),(170,178),(173,178),(176,169)]
# Cambridge Example 14b
E14B = [(2,0.5),(2,2.3),(2,4.2),(2.5,3.5),(3,4.3),(3,5.3),(3,6.3),(3.5,8.2),(4,8.2),(4,9.3),(5,10.1),(6,10.1),(6.2,11.7),(6.8,11.7)]
# Cambridge Example 15 (approximate point clouds: a = weak, b = strong)
_r = random.Random(15)
E15A = [(round(_r.uniform(9, 22), 1), round(min(44, max(9, 0.9 * x + 13 + _r.gauss(0, 7))), 1)) for x in [_r.uniform(9, 22) for _ in range(45)]]
E15A = [(x, round(min(44, max(9, 0.9 * x + 13 + _r.gauss(0, 6.5))), 1)) for x, _ in E15A] + [(8.5, 9.5), (21.5, 43), (25, 27)]
E15B = [(x, round(0.95 * x + 5 + _r.gauss(0, 0.9), 1)) for x in [round(_r.uniform(3, 16), 1) for _ in range(45)]] + [(3.2, 5.6), (17, 22), (20, 24)]
# Edrolo U3&4 2C WE4: sleep (hours) vs basic errors
SLEEP = [(0,11),(1,8),(2,10),(3,9),(4,7),(5,4),(6,3),(7,2),(8,0),(9,1),(10,2)]
# Edrolo U3&4 2C WE3: time (s) vs points
CROSS = [(903,1),(916,2),(873,3),(892,4),(845,5),(823,6),(794,7),(702,8),(740,9),(715,10)]
# Edrolo U1&2 6B WE1 (approximate)
W1 = [(0,4.5),(0.3,1),(0.3,0),(0.4,4.2),(0.9,0),(1.1,2.8),(1.1,0.1),(1.2,0.3),(1.6,4.6),(1.9,1.8),(1.9,5.2),(1.9,0),(2.1,1.2),(2.2,3.8),(2.9,3.6),(3,8.1),
      (3.5,5.4),(3.6,6.8),(4,3.4),(4,3.1),(4.2,6.1),(4.5,8.2),(4.7,2.6),(4.8,2),(5,7.2),(5,5.9),(5.2,5),(5.5,8.7),(5.9,10.5),(5.9,5.7),(6.1,10.2),(6.2,7.4),
      (6.3,10.3),(6.3,11),(6.3,6),(6.5,9.7),(6.5,6.3),(6.6,11.9),(6.7,7.2),(6.9,10.9),(7,6.8),(7,4.4),(7.1,12.1),(7.1,9.9),(7.1,5.7),(7.5,12.2),(7.6,7.6),
      (8.4,7.9),(8.6,9.9),(9.1,13.4),(9.2,11.8),(9.3,10.2),(9.5,6.8),(9.6,14.8),(10,13.8),(10.1,9.4),(10.8,10.8),(10.9,12.1),(11,8.2),(11.1,13.1)]
# Edrolo U1&2 6B WE3: burger patty diameter vs satisfaction (approximate)
W3 = [(x, round(min(19.9, max(0.8, 1.02 * x + 1 + _r.gauss(0, 0.35))), 1)) for x in [round(0.1 + k * 0.32, 2) for k in range(58)]]
