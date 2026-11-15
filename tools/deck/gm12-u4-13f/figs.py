"""Graphs for lesson gm12-u4-13f (13F trees, spanning trees, Prim's algorithm, minimum connector problems).
Every graph is redrawn from the source figure with the same vertices, edges and weights (tools/deck/tpl/net.py); layouts follow the source.
Each figure function takes sid (for data-hi on slides) and **k passed to net(); tree=True draws the answer tree in red (worksheet solutions).
Prim / spanning-tree steps on slides: data-hi="#sid|e1,e2|hc" (orange = chosen edges), removed edges |hv (dashed, faded)."""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'tpl'))
from net import net

RED = '#d2475b'


def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'


def _E(L, tree=(), ink=None):
    """L = [(a, b, w, id, extra-opts)] -> net edges; edges whose id is in tree are red when tree is given."""
    out = []
    for t in L:
        a, b, w, i = t[:4]; o = dict(t[4]) if len(t) > 4 else {}
        if w is not None: o['w'] = w
        o['i'] = i
        if i in tree: o['col'] = RED
        out.append((a, b, o))
    return out


def _g(V, L, sid, tree, W, H_, **k):
    """vertices with label position '' are drawn unlabelled (net.py: name starting '_')"""
    nm = {a: ('_' + a if len(v) > 2 and v[2] == '' else a) for a, v in V.items()}
    V2 = {nm[a]: (v[:2] if nm[a] != a else v) for a, v in V.items()}
    L2 = [(nm[t[0]], nm[t[1]]) + tuple(t[2:]) for t in L]
    return net(V2, _E(L2, tree), sid=sid, W=W, H=H_, **k)


# ---- Cambridge 13F p. 641: a tree with seven vertices
TR_V = {'A': (0, 100, 'w'), 'B': (84, 32, 'n'), 'F': (156, 36, 'n'), 'G': (238, 0, 'ne'), 'E': (238, 102, 'e'), 'C': (110, 128, 's'), 'D': (238, 172, 'e')}
TR_L = [('A', 'B', None, 'ab'), ('B', 'F', None, 'bf'), ('F', 'G', None, 'fg'), ('A', 'C', None, 'ac'), ('C', 'E', None, 'ce'), ('C', 'D', None, 'cd')]
def tree7(sid='', **k): return _g(TR_V, TR_L, sid, (), 240, 172, pad=22, padx=26, fs=20, **k)

# ---- Cambridge Example 11 (p. 641): 9 vertices, 13 edges (spanning tree removes 1-2, 5-4, 4-7, 6-7, 8-6)
X11_V = {'1': (186, 127, ''), '2': (344, 120, ''), '3': (455, 195, ''), '4': (270, 195, ''), '5': (72, 218, ''),
         '6': (184, 290, ''), '7': (375, 292, ''), '8': (84, 352, ''), '9': (304, 362, '')}
X11_V = {k: (v[0], v[1], '') for k, v in X11_V.items()}
X11_L = [('1', '2', 3, 'a12'), ('2', '3', 4, 'a23'), ('1', '5', 2, 'a15'), ('1', '4', 1, 'a14'), ('5', '4', 6, 'a54'), ('4', '3', 3, 'a43'),
         ('4', '6', 4, 'a46'), ('4', '7', 2, 'a47'), ('6', '7', 7, 'a67'), ('5', '8', 5, 'a58'), ('8', '6', 2, 'a86'), ('6', '9', 5, 'a69'), ('9', '7', 2, 'a97')]
X11_KEEP = ['a15', 'a14', 'a46', 'a43', 'a23', 'a58', 'a69', 'a97']
X11_DROP = ['a12', 'a54', 'a47', 'a67', 'a86']
def ex11(sid='', tree=(), **k):
    V = {kk: (v[0] - 60, v[1] - 110, '') for kk, v in X11_V.items()}
    return _g(V, X11_L, sid, tree, 400, 260, pad=16, fs=20, **k)

# ---- Cambridge Example 12 (p. 643): A-F, MST A-B, A-D, D-C, C-E, E-F = 17
X12_V = {'A': (0, 141, 'w'), 'B': (90, 72, 'nw'), 'C': (237, 0, 'n'), 'D': (229, 162, 'ne'), 'E': (338, 218, 'e'), 'F': (223, 304, 's')}
X12_L = [('A', 'B', 2, 'ab'), ('B', 'C', 8, 'bc'), ('B', 'D', 6, 'bd'), ('A', 'D', 5, 'ad'), ('A', 'F', 6, 'af'), ('C', 'D', 3, 'cd'),
         ('C', 'E', 5, 'ce'), ('D', 'E', 6, 'de'), ('D', 'F', 7, 'df'), ('F', 'E', 2, 'fe')]
X12_T = ['ab', 'ad', 'cd', 'ce', 'fe']
def ex12(sid='', tree=(), **k): return _g(X12_V, X12_L, sid, tree, 340, 304, pad=26, padx=26, fs=20, **k)

# ---- Cambridge Example 13 (pp. 644-645): water tank and outlets, MST = 44 m
X13_V = {'Outlet A': (111, 0, 'n'), 'Outlet B': (346, 0, 'n'), 'Outlet C': (288, 50, 'n'), 'Tank': (216, 58, 'w'), 'Outlet G': (126, 63, 'sw'),
         'Outlet F': (0, 86, 'w'), 'Outlet E': (108, 161, 's'), 'Outlet D': (248, 161, 's')}
X13_L = [('Outlet A', 'Outlet B', 13, 'ab'), ('Outlet A', 'Outlet F', 12, 'af'), ('Outlet A', 'Outlet G', 6, 'ag'), ('Outlet A', 'Tank', 11, 'at'),
         ('Outlet B', 'Outlet C', 6, 'bc'), ('Outlet B', 'Outlet D', 11, 'bd'), ('Outlet C', 'Tank', 2, 'ct'), ('Tank', 'Outlet D', 5, 'td'),
         ('Tank', 'Outlet E', 8, 'te'), ('Outlet G', 'Outlet E', 10, 'ge'), ('Outlet F', 'Outlet E', 7, 'fe'), ('Outlet E', 'Outlet D', 9, 'ed')]
X13_T = ['ct', 'td', 'bc', 'te', 'fe', 'ge', 'ag']
def ex13(sid='', tree=(), **k):
    V = {a: (v[0] * 1.6, v[1] * 1.6, v[2]) for a, v in X13_V.items()}
    s = _g(V, X13_L, sid, tree, 554, 258, pad=30, padx=80, fs=19, **k)
    x, y = V['Tank'][:2]
    return s.replace('</svg>', f'<circle cx="{x}" cy="{y}" r="7" fill="#d2242b"/></svg>')

# ---- Edrolo U3&4 8D Worked example 1 (p. 563): 8 vertices, 9 edges (remove 30 top and 60)
W1_V = {'t': (131, 0), 'b': (76, 61), 'l': (0, 132), 'o': (104, 170), 'k': (172, 177), 'm': (196, 121), 'r1': (216, 30), 'r2': (339, 104)}
W1_V = {k: (v[0], v[1], '') for k, v in W1_V.items()}
W1_L = [('l', 'b', 40, 'lb'), ('b', 't', 30, 'bt'), ('b', 'o', 40, 'bo'), ('t', 'o', 70, 'to'), ('o', 'r1', 90, 'or'), ('r1', 'r2', 60, 'rr'),
        ('r2', 'm', 50, 'rm'), ('m', 'k', 20, 'mk'), ('o', 'k', 30, 'ok')]
W1_DROP = ['bt', 'rr']
def we1(sid='', tree=(), **k): return _g(W1_V, W1_L, sid, tree, 339, 177, pad=18, fs=20, **k)

# ---- Edrolo U3&4 8D Worked example 2 (p. 564): A-F with a loop at C; MST from A = 25
W2_V = {'A': (0, 83, 'w'), 'B': (88, 23, 'nw'), 'C': (119, 145, 's'), 'D': (201, 56, 'n'), 'E': (325, 0, 'ne'), 'F': (300, 110, 'se')}
W2_L = [('A', 'B', 6, 'ab'), ('A', 'C', 6, 'ac'), ('B', 'E', 8, 'be'), ('B', 'D', 7, 'bd'), ('C', 'D', 5, 'cd'), ('D', 'F', 3, 'df'),
        ('E', 'F', 6, 'ef'), ('C', 'F', 4, 'cf'), ('C', 'C', 1, 'cc', {'loop': 90, 'size': 17})]
W2_T = ['ab', 'ac', 'cf', 'df', 'ef']
def we2(sid='', tree=(), **k):
    V = dict(W2_V); V['C'] = (119, 145, 'nw')
    L = [t if t[3] != 'cc' else ('C', 'C', None, 'cc', t[4]) for t in W2_L]
    s = _g(V, L, sid, tree, 325, 175, pad=26, padx=26, fs=20, **k)
    return s.replace('</svg>', '<text x="146" y="178" text-anchor="middle" font-size="18" fill="#222">1</text></svg>')

# ---- Edrolo U1&2 7F Worked example 2 (p. 419): A-H, MST from A = 38
U2_V = {'A': (0, 19, 'w'), 'C': (79, 0, 'n'), 'G': (160, 41, 'ne'), 'B': (20, 100, 'sw'), 'D': (98, 79, 'sw'), 'F': (151, 131, 'e'),
        'E': (122, 182, 's'), 'H': (326, 135, 'e')}
U2_L = [('A', 'C', 7, 'ac'), ('A', 'B', 5, 'ab'), ('C', 'D', 3, 'cd'), ('C', 'G', 9, 'cg'), ('B', 'D', 2, 'bd'), ('D', 'G', 8, 'dg'),
        ('D', 'F', 8, 'df'), ('G', 'F', 6, 'gf'), ('G', 'H', 10, 'gh'), ('B', 'E', 11, 'be'), ('F', 'E', 4, 'fe'), ('E', 'H', 10, 'eh')]
U2_T = ['ab', 'bd', 'cd', 'dg', 'gf', 'fe', 'gh']
def u12we2(sid='', tree=(), **k): return _g(U2_V, U2_L, sid, tree, 326, 182, pad=26, padx=26, fs=20, **k)

# ---- VCAA 2017 Exam 2 N&DM Q3 (theme park, = Edrolo U1&2 7F Q18 / U3&4 8D Q13): MST = 1500 m
TP_V = {'tl': (46, 4), 'tm': (133, 0), 'tr': (201, 15), 'ml': (46, 82), 'c': (140, 64), 'r': (243, 97), 'fr': (311, 59), 'bl': (46, 155), 'bb': (0, 204)}
TP_V = {k: (v[0], v[1], '') for k, v in TP_V.items()}
TP_L = [('tl', 'tm', 350, 'p1'), ('tm', 'tr', 200, 'p2'), ('tl', 'ml', 300, 'p3'), ('ml', 'tm', 100, 'p4'), ('tm', 'c', 100, 'p5'), ('c', 'tr', 50, 'p6'),
        ('ml', 'c', 150, 'p7'), ('tr', 'r', 500, 'p8'), ('c', 'r', 450, 'p9'), ('ml', 'bl', 200, 'p10'), ('bl', 'c', 500, 'p11'), ('bl', 'r', 400, 'p12'),
        ('r', 'fr', 200, 'p13'), ('bl', 'bb', 150, 'p14')]
TP_T = ['p6', 'p4', 'p5', 'p14', 'p10', 'p13', 'p3', 'p12']
def park(sid='', tree=(), dash=False, **k):
    L = [t + ({'dash': True},) if dash else t for t in TP_L]
    return _g(TP_V, L, sid, tree, 311, 204, pad=18, fs=18, **k)

# ---- Do Now: VCAA 2024 Exam 1 Q34 (Eulerian trail)
Q34_V = {'A': (0, 58, 'w'), 'B': (42, 14, 'n'), 'C': (42, 87, 's'), 'D': (99, 57, 'n'), 'E': (142, 0, 'e'), 'F': (142, 102, 's')}
Q34_L = [('A', 'B', None, 'ab'), ('A', 'C', None, 'ac'), ('B', 'C', None, 'bc'), ('B', 'D', None, 'bd'), ('C', 'D', None, 'cd'),
         ('C', 'F', None, 'cf'), ('D', 'E', None, 'de'), ('D', 'F', None, 'df'), ('E', 'F', None, 'ef')]
def q34(sid='', **k): return _g(Q34_V, Q34_L, sid, (), 142, 102, pad=20, padx=20, fs=16, **k)

# ---- Do Now: VCAA 2025 Exam 1 Q38 (Sofia, home to school): shortest 3700 m
SF_V = {'home': (0, 71, 'w'), 'P': (72, 0, ''), 'Q': (262, -10, ''), 'school': (345, 36, 'e'), 'M': (167, 70, ''), 'L': (60, 130, ''),
        'K': (119, 112, ''), 'BL': (72, 191, ''), 'BR': (212, 181, ''), 'R': (302, 126, '')}
SF_V = {k: (v[0], v[1] + 10, v[2] if len(v) > 2 else '') for k, v in SF_V.items()}
SF_L = [('home', 'P', 1500, 'hp'), ('P', 'Q', 1600, 'pq'), ('Q', 'school', 700, 'qs'), ('P', 'M', 500, 'pm'), ('home', 'M', 1900, 'hm'),
        ('M', 'school', 3300, 'ms'), ('home', 'L', 900, 'hl'), ('L', 'K', 500, 'lk'), ('K', 'M', 400, 'km'), ('L', 'M', 1000, 'lm', {'via': [(120, 158)]}),
        ('home', 'BL', 1200, 'hb'), ('BL', 'BR', 1600, 'bb'), ('M', 'BR', 800, 'mb'), ('BR', 'R', 900, 'br'), ('R', 'school', 300, 'rs'),
        ('BR', 'school', 1100, 'bs', {'via': [(268, 200), (330, 130)]})]
def sofia(sid='', **k): return _g(SF_V, SF_L, sid, (), 345, 205, pad=20, padx=60, fs=15, **k)

# ---- Do Now: VCAA 2025 Exam 2 Q15 (Frances)
FR_V = {'coffee shop': (79, 0, 'n'), 'supermarket': (199, 0, 'n'), 'gym': (0, 40, 'w'), 'pet shop': (79, 82, 's'), 'home': (199, 82, 's')}
FR_L = [('coffee shop', 'gym', None, 'cg'), ('gym', 'pet shop', None, 'gp'), ('coffee shop', 'pet shop', None, 'cp'), ('coffee shop', 'supermarket', None, 'cs'),
        ('coffee shop', 'home', None, 'ch'), ('pet shop', 'home', None, 'ph'), ('supermarket', 'home', None, 'sh')]
def frances(sid='', **k): return _g(FR_V, FR_L, sid, (), 199, 82, pad=28, padx=50, fs=15, **k)

# ---- Exit 1: VCAA 2018 Exam 1 N&DM Q1 (five isolated vertices)
def iso5(sid='', ink='#1f4fb0', add=False):
    P = [(18, 12), (75, 0), (168, 20), (83, 60), (0, 92)]
    s = f'<svg class="net" id="{sid}" viewBox="-14 -14 196 120" width="100%" style="display:block">'
    if add:
        for k, (a, b) in enumerate([(4, 0), (0, 1), (1, 3), (3, 2)]):
            s += f'<line data-i="t{k}" class="hid0" x1="{P[a][0]}" y1="{P[a][1]}" x2="{P[b][0]}" y2="{P[b][1]}" stroke="#c0632b" stroke-width="4"/>'
    s += ''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="{ink}"/>' for x, y in P)
    return s + '</svg>'

# ---- Exit 2: VCAA 2020 Exam 1 N&DM Q3 (which is not a spanning tree?)
SP_V = {'1': (0, 46, 'n'), '2': (47, 0, 'n'), '3': (96, 62, 'n'), '4': (160, 14, 'n'), '5': (225, 54, 'n'), '6': (128, 122, 's')}
SP_L = [('1', '2', None, 's12'), ('2', '3', None, 's23'), ('1', '6', None, 's16'), ('3', '4', None, 's34'), ('4', '5', None, 's45'), ('3', '6', None, 's36'), ('5', '6', None, 's56')]
SP_OPT = {'A': [('1', '6'), ('2', '3'), ('3', '6'), ('3', '4'), ('5', '6')], 'B': [('1', '6'), ('2', '3'), ('3', '6'), ('3', '4'), ('3', '5')],
          'C': [('1', '2'), ('1', '6'), ('3', '6'), ('3', '4'), ('5', '6')], 'D': [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('3', '6')],
          'E': [('1', '2'), ('2', '3'), ('3', '4'), ('3', '6'), ('6', '5')]}
def sp(sid='', **k): return _g(SP_V, SP_L, sid, (), 225, 122, pad=22, padx=12, fs=16, **k)
def spopt(L, sid='', fs=22, **k): return net(SP_V, [(a, b, {'i': f'o{a}{b}'}) for a, b in L], sid=sid, W=225, H=122, pad=30, padx=14, fs=fs, **k)
