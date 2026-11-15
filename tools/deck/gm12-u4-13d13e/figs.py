"""Graphs for lesson gm12-u4-13d13e (13D weighted graphs / shortest path by inspection, 13E Dijkstra's algorithm).
Every graph is redrawn from the source figure with the same vertices, edges and weights (tools/deck/tpl/net.py); layouts follow the source.
Dijkstra labels (Cambridge graphical method) are hidden orange labels + red circles revealed with data-show;
Edrolo's table method uses dtable() (cells r{row}_{col}, hidden until data-show, boxed with data-hi ... |hy)."""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'tpl')); sys.path.insert(0, os.path.join(H, '..', 'gm12-u4-13c'))
from net import net, amat

RED = '#d2475b'; ORG = '#c0632b'
def img(name, w='100%', d=None):
    p = os.path.join(d or H, 'fig', name)
    b = base64.b64encode(open(p, 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'

def E_(a, b, w, i=None, **o):
    d = {'w': w, **o}
    if i: d['i'] = i
    return (a, b, d)

def ring(V, k, nm, R=17, col=RED):
    x, y = V[k][:2]
    return f'<circle data-i="{nm}" class="hid0" cx="{x}" cy="{y}" r="{R}" fill="none" stroke="{col}" stroke-width="2.6"/>'
def lab(x, y, t, nm, fs=20, col=ORG, strike=False):
    s = f'<text data-i="{nm}" class="hid0" x="{x}" y="{y}" text-anchor="middle" font-size="{fs}" font-weight="800" fill="{col}">{t}</text>'
    if strike: s += f'<line data-i="{nm}x" class="hid0" x1="{x-9}" y1="{y-6}" x2="{x+9}" y2="{y-6}" stroke="{col}" stroke-width="2.5"/>'
    return s

# ---- Cambridge 13D p. 633 / Example 9 (p. 634): Croghon network
CR_V = {'Croghon': (120, 20, 'n'), 'Melville': (280, 100, 'n'), 'Kenton': (525, 125, 'e'), 'Bartow': (18, 143, 'w'),
        'Stratmoore': (130, 240, 's'), 'Osburn': (365, 235, 's')}
CR_E = [E_('Bartow', 'Croghon', 12, 'bc', bend=10), E_('Croghon', 'Melville', 6, 'cm', via=[(150, 90), (230, 110)]),
        E_('Melville', 'Kenton', 13, 'mk', via=[(400, 75), (520, 60)]), E_('Bartow', 'Stratmoore', 7, 'bs', bend=10),
        E_('Croghon', 'Osburn', 20, 'co', via=[(160, 160), (260, 225)]), E_('Melville', 'Stratmoore', 8, 'ms'),
        E_('Melville', 'Osburn', 5, 'mo'), E_('Stratmoore', 'Osburn', 9, 'so'), E_('Osburn', 'Kenton', 11, 'ok', bend=22)]
def crog(sid='', **k): return net(CR_V, CR_E, sid=sid, W=540, H=250, pad=30, padx=60, fs=20, **k)

# ---- Edrolo U3&4 8F Worked example 1 (p. 585): train stations
TR_V = {'Beachmore': (140, 82, 'n'), 'Halville': (436, 66, 'e'), 'Daylington': (14, 166, 'se'), 'Tesburn': (266, 158, 'n'),
        'Eastborough': (544, 194, 's'), 'Marron': (142, 282, 'e')}
TR_E = [E_('Daylington', 'Halville', 11, 'dh', via=[(90, 40), (250, 0), (400, 20)]), E_('Beachmore', 'Halville', 6, 'bh'),
        E_('Daylington', 'Beachmore', 3, 'db'), E_('Halville', 'Eastborough', 4, 'he'), E_('Tesburn', 'Eastborough', 7, 'te'),
        E_('Daylington', 'Marron', 8, 'dm'), E_('Marron', 'Tesburn', 9, 'mt'), E_('Marron', 'Eastborough', 10, 'me', via=[(330, 330), (500, 270)])]
def trains(sid='', **k): return net(TR_V, TR_E, sid=sid, W=560, H=300, pad=26, padx=70, fs=20, **k)

# ---- Cambridge Example 10 (p. 638): A to F
X10_V = {'A': (24, 75, 'w'), 'B': (210, 36, 'n'), 'E': (495, 36, 'n'), 'F': (585, 201, 'e'), 'C': (111, 300, 's'), 'D': (381, 303, 's')}
X10_E = [E_('A', 'B', 2, 'ab'), E_('B', 'E', 2, 'be'), E_('A', 'C', 6, 'ac'), E_('B', 'C', 2, 'bc'), E_('B', 'D', 3, 'bd'),
         E_('E', 'D', 2, 'ed'), E_('E', 'F', 3, 'ef'), E_('C', 'D', 1, 'cd'), E_('D', 'F', 5, 'df')]
def ex10(sid='', labels=True, ink=None, fs=22, **k):
    kk = dict(k)
    if ink: kk['ink'] = ink
    ex = ''
    if labels:
        ex = (''.join(ring(X10_V, v, 'k' + v) for v in 'ABCDEF')
              + lab(4, 58, '0', 'lA') + lab(240, 22, '2', 'lB') + lab(66, 296, '6', 'lC6', strike=True) + lab(86, 296, '4', 'lC4')
              + lab(470, 18, '4', 'lE') + lab(410, 330, '5', 'lD') + lab(612, 228, '7', 'lF'))
    return net(X10_V, X10_E, sid=sid, W=610, H=320, pad=34, fs=fs, extra=ex, **kk)

# ---- Edrolo 8F theory (p. 586): A to D, table method
ET_V = {'B': (15, 12, 'w'), 'D': (397, 12, 'e'), 'C': (205, 118, 'n'), 'A': (15, 212, 'w'), 'E': (397, 212, 'e')}
ET_E = [E_('B', 'D', 8, 'bd', bend=-14), E_('A', 'B', 8, 'ab', bend=-10), E_('B', 'C', 5, 'bc'), E_('C', 'A', 4, 'ca'),
        E_('C', 'D', 15, 'cd'), E_('C', 'E', 16, 'ce', via=[(260, 205), (330, 225)]), E_('D', 'E', 7, 'de')]
def etheory(sid='', **k): return net(ET_V, ET_E, sid=sid, W=415, H=225, pad=22, fs=20, **k)

# ---- Edrolo 8F Worked example 2 (p. 588): school
SC_V = {'General': (18, 158, 'w'), 'Chemistry': (310, 108, 'n'), 'English': (608, 65, 'n'), 'Methods': (310, 278, 's'),
        'Biology': (613, 323, 's'), 'Physics': (173, 410, 's')}
SC_E = [E_('General', 'English', 9, 'ge', via=[(200, 40), (420, 10)]), E_('General', 'Chemistry', 7, 'gc'), E_('Chemistry', 'English', 3, 'ce'),
        E_('General', 'Methods', 4, 'gm'), E_('Chemistry', 'Methods', 2, 'cm'), E_('Methods', 'English', 5, 'me'), E_('English', 'Biology', 2, 'eb'),
        E_('Methods', 'Biology', 1, 'mb'), E_('General', 'Physics', 1, 'gp'), E_('Physics', 'Biology', 6, 'pb')]
def school(sid='', **k): return net(SC_V, SC_E, sid=sid, W=640, H=430, pad=34, padx=70, fs=22, **k)

def dtable(tid, rows, cols, vals, hidden=True, fs=20):
    """Edrolo Dijkstra table: rows = row vertices, cols = column vertices, vals[r][c] text ('' = empty). Cells data-i r{r}_{c}."""
    h = f'<tr><th></th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    b = ''.join(f'<tr><th>{r}</th>' + ''.join(f'<td data-i="r{i}_{k}"><span data-i="s{i}_{k}"{" class=" + chr(34) + "hid0" + chr(34) if hidden else ""}>{v}</span></td>'
                                             for k, v in enumerate(vals[i])) + '</tr>' for i, r in enumerate(rows))
    st = ('<style>.dtab{border-collapse:collapse;margin:6px auto}.dtab td,.dtab th{border:2px solid #c9d3e6;padding:3px 12px;text-align:center;min-width:1.6em}'
          '.dtab th{background:#eef3fb}.dtab td.hy{outline:3px solid #d9b100;outline-offset:-5px;background:#fff7cc}</style>')
    return st + f'<table class="dtab" id="{tid}" style="font-size:{fs}px">{h}{b}</table>'

# ---- APK 1: Cambridge U1&2 Ch 8 checklist #14 (p. 542): Home to School
HS_V = {'Home': (21, 141, 'w'), '_a': (189, 90), '_T': (441, 24), '_c': (300, 135), '_L': (174, 249), '_B': (441, 249), '_b': (570, 249),
        '_m': (570, 129), 'School': (711, 249, 'e')}
HS_E = [E_('Home', '_a', 3, 'ha'), E_('_a', '_T', 7, 'at'), E_('_a', '_c', 5, 'ac'), E_('Home', '_c', 8, 'hc'), E_('Home', '_L', 5, 'hl'),
        E_('_L', '_c', 2, 'lc'), E_('_c', '_T', 2, 'ct'), E_('_c', '_B', 9, 'cb'), E_('_T', '_B', 6, 'tb'), E_('_T', '_m', 4, 'tm'),
        E_('_m', 'School', 4, 'ms'), E_('_L', '_B', 13, 'lb'), E_('_B', '_b', 2, 'bb'), E_('_b', 'School', 1, 'bs')]
def hschool(sid='', **k): return net(HS_V, HS_E, sid=sid, W=730, H=270, pad=26, padx=70, fs=24, **k)

# ---- APK 2: VCAA 2020 Exam 2 N&DM Q3 (fitness park)
FP_V = {'S': (108, 29, 'w'), 'T': (280, 27, 'ne'), 'M': (459, 17, 'n'), 'N': (519, 94, 'n'), 'U': (265, 150, 'n'), 'R': (15, 157, 'w'),
        'V': (388, 206, 'n'), 'O': (664, 174, 'se'), 'Q': (80, 286, 's'), 'P': (420, 298, 's')}
FP_E = [E_('S', 'M', 1.8, 'sm', via=[(250, -20), (400, -10)]), E_('S', 'T', 0.6, 'st', bend=-4), E_('T', 'U', 1.2, 'tu', via=[(285, 90)]),
        E_('S', 'R', 1.0, 'sr', via=[(40, 110)]), E_('U', 'N', 0.7, 'un', bend=-4), E_('N', 'O', 0.9, 'no'), E_('M', 'O', 1.5, 'mo', bend=-14),
        E_('U', 'V', 0.6, 'uv', bend=-6), E_('V', 'O', 0.8, 'vo', bend=-6), E_('R', 'Q', 1.2, 'rq', via=[(40, 260)]), E_('Q', 'U', 0.8, 'qu', bend=-14),
        E_('Q', 'V', 1.2, 'qv', bend=-6), E_('Q', 'P', 0.8, 'qp', bend=4), E_('V', 'P', 0.4, 'vp', bend=-6), E_('P', 'O', 1.4, 'po', bend=10)]
def fpark(sid='', **k): return net(FP_V, FP_E, sid=sid, W=690, H=310, pad=26, fs=22, **k)

# ---- Do Now 1: VCAA 2025 Exam 1 Q34 (unlabelled; bridges)
B1_V = {'_1': (30, 80), '_2': (102, 15), '_3': (198, 9), '_4': (280, 79), '_5': (252, 120), '_6': (313, 120), '_7': (8, 170), '_8': (112, 223),
        '_9': (107, 137), '_10': (180, 163)}
B1_E = [('_1', '_2', {'i': 'b12'}), ('_2', '_3', {'i': 'b23'}), ('_3', '_4', {'i': 'b34'}), ('_4', '_5'), ('_5', '_6'), ('_4', '_6'),
        ('_1', '_7'), ('_7', '_8'), ('_1', '_8'), ('_8', '_9'), ('_9', '_10'), ('_8', '_10')]
# ---- Do Now 4: VCAA 2023 Exam 2 Q12 (states)
ST_V = {'A': (100, 15, 'n'), 'B': (40, 75, 'w'), 'C': (158, 75, 'ne'), 'E': (265, 75, 'e'), 'D': (100, 135, 's')}
ST_E = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

# ---- Exit 1: VCAA 2018 Exam 1 N&DM Q2 (Niko)
NK_V = {'home': (22, 103, 'w'), 'A': (220, 103, 'n'), 'B': (444, 26, 'n'), 'D': (414, 180, 's'), 'university': (642, 202, 'e'),
        'C': (106, 237, 's'), 'E': (352, 312, 's')}
NK_E = [E_('home', 'A', 2), E_('home', 'C', 3), E_('A', 'C', 2), E_('A', 'B', 4), E_('A', 'D', 2), E_('B', 'D', 2), E_('B', 'university', 2),
        E_('D', 'university', 3), E_('C', 'E', 1), E_('E', 'university', 5)]
def niko(sid='', **k): return net(NK_V, NK_E, sid=sid, W=660, H=320, pad=28, padx=150, fs=24, **k)
# ---- Exit 2: VCAA 2017 Exam 2 N&DM Q1 (bus routes)
BU_V = {'O': (165, 13, 'n'), 'N': (16, 210, 'w'), 'P': (258, 219, 'ne'), 'R': (507, 214, 'n'), 'S': (721, 213, 'e'), 'Q': (126, 430, 's')}
BU_E = [E_('N', 'O', 15, 'no'), E_('O', 'P', 20, 'op'), E_('O', 'R', 75, 'or'), E_('O', 'S', 105, 'os'), E_('N', 'P', 30, 'np'), E_('P', 'R', 40, 'pr'),
        E_('R', 'S', 30, 'rs'), E_('N', 'Q', 30, 'nq'), E_('P', 'Q', 55, 'pq'), E_('Q', 'R', 20, 'qr'), E_('Q', 'S', 60, 'qs')]
def bus(sid='', **k): return net(BU_V, BU_E, sid=sid, W=740, H=440, pad=30, fs=26, **k)
