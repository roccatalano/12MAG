"""Graphs for lesson gm12-u4-13c (13C exploring and travelling).
Every graph is redrawn from the source figure with the same vertices and edges (tools/deck/tpl/net.py); layouts follow the source.
Walks given in a question (red arrows in the source) are drawn as red arrowed edges with walk().
Figures that are not graphs (the Example 8 road map, a floor plan, a life-cycle diagram) are cropped from the PDFs (fig/), so they stay verbatim."""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'tpl'))
from net import net, amat

RED = '#d2475b'
def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'

def walk(seq, col=RED, pre='w', hid=False, bend=7, start=1):
    """Arrowed edges for a walk A-B-C ...; repeated edges alternate their bend so both show. ids w1, w2 ..."""
    seen = {}; out = []
    for k in range(len(seq) - 1):
        a, b = seq[k], seq[k + 1]; key = frozenset((a, b)); n = seen.get(key, 0); seen[key] = n + 1
        bd = bend * (1 + 1.6 * n) * (1 if a < b else -1)
        out.append((a, b, {'i': f'{pre}{k + start}', 'arrow': True, 'col': col, 'bend': bd, 'hid': hid}))
    return out

# ---- Cambridge 13C p. 624: the house-shaped graph used for walks, trails, paths, circuits, cycles (Learn)
HS_V = {'A': (160, 18, 'n'), 'B': (40, 85, 'w'), 'C': (160, 85, 'nw'), 'D': (290, 85, 'e'), 'E': (40, 175, 'sw'), 'F': (160, 175, 's'), 'G': (290, 175, 'se')}
HS_E = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('C', 'D'), ('B', 'E'), ('C', 'F'), ('D', 'G'), ('E', 'F'), ('F', 'G')]
HS_W = {'walk': 'ACADG', 'trail': 'BEFCBA', 'path': 'ADCFEB', 'circuit': 'ACFGDCBA', 'cycle': 'FEBCF'}
def house(sid, kind=None, wcol=RED, **k):
    E = HS_E + (walk(HS_W[kind], pre=kind, col=wcol) if kind else [])
    return net(HS_V, E, sid=sid, W=330, H=195, pad=18, fs=24, **k)

# ---- Cambridge Example 7 (p. 626): one graph, four walks
E7_V = {'A': (25, 85, 'w'), 'B': (120, 15, 'n'), 'C': (110, 80, 'sw'), 'D': (215, 72, 'e'), 'E': (95, 160, 's'), 'F': (180, 130, 'se')}
E7_E = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D'), ('B', 'C'), ('C', 'E'), ('A', 'E'), ('A', 'E', {'bend': -26}), ('D', 'E'), ('D', 'F'), ('E', 'F')]
E7_W = {'a': 'DBCAECD', 'b': 'AECDBA', 'c': 'BCABDF', 'd': 'DECAECB'}
E7_SE = {'a': ('D', 'D'), 'b': ('A', 'A'), 'c': ('B', 'F'), 'd': ('D', 'B')}
def ex7(p, sid='', ink=None, wcol=RED, **k):
    kk = dict(k);
    if ink: kk['ink'] = ink
    return net(E7_V, E7_E + walk(E7_W[p], col=wcol, bend=6), sid=sid, W=245, H=175, pad=14, fs=19, r=4, **kk)

# ---- Edrolo 8C Worked example 1 (pp. 549-550): one graph, four walks
Y1_V = {'B': (20, 20, 'w'), 'C': (220, 15, 'e'), 'D': (115, 60, 'n'), 'A': (15, 100, 'w'), 'E': (175, 100, 'se'), 'F': (110, 175, 's')}
Y1_E = [('B', 'C'), ('B', 'D'), ('D', 'E'), ('A', 'D'), ('D', 'C'), ('A', 'E'), ('A', 'F'), ('F', 'E'), ('E', 'C')]
Y1_W = {'a': 'FECDAF', 'b': 'AEDBC', 'c': 'DAFEDBC', 'd': 'BCEDADB'}
def ey1(p, sid='', ink=None, wcol=RED, **k):
    kk = dict(k)
    if ink: kk['ink'] = ink
    return net(Y1_V, Y1_E + walk(Y1_W[p], col=wcol, bend=6), sid=sid, W=240, H=185, pad=14, fs=19, r=4, **kk)

# ---- Cambridge Example 8 (p. 628) answer graph: towns
T_V = {'Kinglake': (110, 20, 'n'), 'Toolangi': (330, 25, 'n'), 'St Andrews': (20, 100, 's'), 'Yarra Glen': (170, 160, 's'), 'Healesville': (340, 165, 's')}
T_E = [('St Andrews', 'Kinglake', {'i': 'sk'}), ('St Andrews', 'Yarra Glen', {'i': 'sy'}), ('Kinglake', 'Yarra Glen', {'i': 'ky'}), ('Kinglake', 'Toolangi', {'i': 'kt'}),
       ('Yarra Glen', 'Toolangi', {'i': 'yt'}), ('Yarra Glen', 'Healesville', {'i': 'yh'}), ('Healesville', 'Toolangi', {'i': 'ht'})]
def towns(sid='', hid=False, **k):
    return net(T_V, [(a, b, {**o, 'hid': hid}) for a, b, o in T_E], sid=sid, W=360, H=180, pad=30, padx=80, fs=22, **k)

# ---- Edrolo 8C Worked example 2 (p. 551): Dandenong walking track
DR_V = {'A': (205, 40, 'nw'), 'B': (340, 90, 'e'), 'C': (260, 130, 'sw'), 'E': (70, 230, 'w'), 'D': (205, 250, 's')}
DR_E = [('A', 'B', {'i': 'ab1', 'via': [(260, -10), (360, 0), (370, 60)]}), ('A', 'B', {'i': 'ab2', 'via': [(280, 40), (310, 45)]}),
        ('A', 'E', {'i': 'ae', 'via': [(195, 120), (110, 160)]}), ('A', 'D', {'i': 'ad', 'via': [(100, 120), (20, 150), (30, 240), (130, 255)]}),
        ('B', 'E', {'i': 'be', 'via': [(220, 105), (175, 200)]}), ('B', 'C', {'i': 'bc', 'via': [(345, 150), (300, 150)]}), ('C', 'D', {'i': 'cd', 'via': [(225, 150), (225, 210)]})]
def dandy(sid='', extra=(), **k): return net(DR_V, DR_E + list(extra), sid=sid, W=390, H=265, pad=14, **k)

# ---- Edrolo 8C Worked example 3 (p. 553): Max the mailman
MX_V = {'PO': (20, 75, 'n'), '2': (120, 35, 'n'), '3': (225, 55, 'n'), '4': (275, 15, 'n'), '6': (310, 105, 'ne'), '1': (95, 165, 's'), '5': (285, 210, 's')}
MX_E = [('PO', '2', {'i': 'p2'}), ('PO', '1', {'i': 'p1', 'via': [(0, 140), (40, 170)]}), ('1', '2', {'i': 'a12'}), ('2', '3', {'i': 'a23'}),
        ('2', '4', {'i': 'a24', 'via': [(185, -20), (255, -5)]}), ('3', '4', {'i': 'a34'}), ('3', '6', {'i': 'a36'}), ('1', '6', {'i': 'a16'}), ('1', '5', {'i': 'a15'}),
        ('5', '6', {'i': 'a56', 'via': [(340, 160)]})]
def maxg(sid='', extra=(), **k): return net(MX_V, MX_E + list(extra), sid=sid, W=345, H=225, pad=16, **k)

# ---- APK: Cambridge U1&2 Ch 8 checklist #1/#3 graph (p. 540) and #9 graph (p. 541)
K1_V = {'A': (30, 60, 'w'), 'B': (140, 20, 'n'), 'C': (250, 65, 'w'), 'D': (205, 170, 's'), 'E': (90, 170, 'sw')}
K1_E = [('A', 'B', {'i': 'ab'}), ('A', 'E', {'i': 'ae'}), ('B', 'E', {'i': 'be'}), ('B', 'D', {'i': 'bd'}), ('E', 'D', {'i': 'ed'}), ('D', 'C', {'i': 'dc'}),
        ('C', 'C', {'i': 'cl', 'loop': 0, 'size': 17}), ('E', 'E', {'i': 'el', 'loop': 100, 'size': 17})]
K9_V = {'N': (130, 15, 'n'), 'M': (20, 60, 'w'), 'O': (200, 60, 'ne'), 'P': (265, 105, 'e'), 'R': (115, 105, 's'), 'S': (20, 150, 's'), 'Q': (195, 150, 's')}
K9_E = [('M', 'N', {'i': 'mn'}), ('N', 'O', {'i': 'no'}), ('O', 'P', {'i': 'op'}), ('P', 'Q', {'i': 'pq'}), ('Q', 'R', {'i': 'qr'}), ('R', 'M', {'i': 'rm'}),
        ('O', 'R', {'i': 'or'}), ('R', 'S', {'i': 'rs'}), ('M', 'S', {'i': 'ms'})]
# ---- APK: Edrolo U1&2 7D Q11 (adapted from VCAA 2019 Exam 2 N&DM Q1bii): hiking trail
HK_V = {'Sunset Lookout': (60, 40, 'w'), 'Waterfall Way': (215, 20, 'n'), 'Point Kangaroo': (185, 110, 'ne'), 'Snake Point': (185, 205, 's'),
        'Mount Cockatoo': (110, 240, 'w'), 'Feather Mountain': (300, 280, 's')}
HK_E = [('Sunset Lookout', 'Waterfall Way', {'bend': -12}), ('Waterfall Way', 'Feather Mountain', {'via': [(330, 110), (340, 220)]}), ('Sunset Lookout', 'Point Kangaroo', {'bend': -12}),
        ('Sunset Lookout', 'Mount Cockatoo', {'via': [(50, 100), (110, 180)]}), ('Point Kangaroo', 'Snake Point'), ('Point Kangaroo', 'Mount Cockatoo', {'bend': 18}),
        ('Snake Point', 'Mount Cockatoo'), ('Point Kangaroo', 'Feather Mountain', {'bend': -8}), ('Mount Cockatoo', 'Feather Mountain', {'via': [(160, 310), (260, 310)]})]
def hike(sid='', extra=(), **k): return net(HK_V, HK_E + list(extra), sid=sid, W=360, H=300, pad=30, padx=150, fs=22, **k)

# ---- Do Now 1: VCAA 2024 Exam 1 Q33 (unlabelled; isolated vertex, loop)
D1_V = {'_i': (40, 10), '_l': (10, 75), '_t': (115, 20), '_m': (88, 72), '_b': (130, 120), '_r': (170, 92)}
D1_E = [('_l', '_t', {'i': 'lt'}), ('_t', '_m', {'i': 'tm'}), ('_t', '_r', {'i': 'tr'}), ('_m', '_b', {'i': 'mb'}), ('_b', '_r', {'i': 'br'}), ('_r', '_r', {'i': 'rl', 'loop': 0, 'size': 20})]
# ---- Do Now 3: VCAA 2024 Exam 2 Q13 graph (incomplete; P and its edges hidden)
D3_V = {'D': (40, 20, 'nw'), 'F': (40, 130, 's'), 'G': (110, 85, 'n'), 'B': (190, 10, 'e'), 'P': (190, 140, 'e')}
D3_E = [('D', 'F'), ('D', 'G'), ('F', 'G'), ('G', 'B'), ('P', 'G', {'i': 'pg', 'hid': True, 'col': RED}), ('P', 'F', {'i': 'pf', 'hid': True, 'col': RED})]
def d3(sid='', **k): return net(D3_V, D3_E, sid=sid, W=230, H=150, pad=16, **k).replace('<circle data-i="vP"', '<circle data-i="vP" class="hid0"').replace('<text data-i="tP"', '<text data-i="tP" class="hid0"')

# ---- Exit 1: VCAA 2019 Exam 2 N&DM Q1 (Fencedale High School)
FH_V = {'office': (150, 20, 'n'), 'library': (255, 65, 'e'), 'science laboratories': (50, 115, 'w'), 'computer rooms': (215, 115, 'se'),
        'mathematics classrooms': (80, 200, 'sw'), 'gymnasium': (255, 215, 'se')}
FH_E = [('office', 'science laboratories', {'via': [(60, 40)]}), ('science laboratories', 'mathematics classrooms', {'bend': 10}), ('office', 'mathematics classrooms', {'bend': -8}),
        ('office', 'library', {'bend': 6}), ('office', 'computer rooms', {'via': [(290, 30), (335, 70)]}), ('office', 'gymnasium', {'via': [(320, 10), (385, 60), (320, 170)]}),
        ('library', 'mathematics classrooms', {'bend': 10}), ('library', 'computer rooms'), ('computer rooms', 'gymnasium', {'via': [(195, 175)]}), ('mathematics classrooms', 'gymnasium', {'bend': 10})]
def fence(sid='', extra=(), **k): return net(FH_V, FH_E + list(extra), sid=sid, W=380, H=230, pad=30, padx=175, fs=22, **k)
# ---- Exit 2: VCAA 2019 Exam 1 N&DM Q2 (6 unlabelled vertices)
X2_V = {'_1': (10, 40), '_2': (100, 10), '_3': (190, 20), '_4': (230, 75), '_5': (150, 110), '_6': (25, 120)}
X2_E = [('_1', '_2'), ('_2', '_3'), ('_3', '_4'), ('_4', '_5'), ('_5', '_6'), ('_6', '_1'), ('_1', '_5'), ('_2', '_5'), ('_3', '_5')]
# ---- Exit 3: VCAA 2018 Exam 2 N&DM Q2c (Zenith)
ZN_V = {'A': (40, 50, 'nw'), 'B': (130, 30, 'n'), 'C': (190, 5, 'e'), 'D': (120, 85, 'sw'), 'E': (10, 160, 'w'), 'F': (85, 145, 'nw'), 'G': (170, 140, 'e'),
        'H': (25, 215, 's'), 'I': (100, 205, 's'), 'J': (185, 200, 's')}
ZN_E = [('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'D'), ('A', 'E'), ('D', 'F'), ('D', 'G'), ('E', 'F'), ('F', 'G'), ('E', 'H'), ('F', 'I'), ('G', 'J'), ('H', 'I'), ('I', 'J')]
def zen(sid='', dash=False, extra=(), **k): return net(ZN_V, [(a, b, {'dash': dash}) for a, b in ZN_E] + list(extra), sid=sid, W=210, H=225, pad=16, fs=15, **k)
