"""Graphs for lesson gm12-u4-13a13b (13A graphs and networks, 13B adjacency matrices).
Every graph is redrawn from the source figure with the same vertices and edges (tools/deck/tpl/net.py); layouts follow the source.
Two VCAA figures that are not graphs (a floor plan and a road map) are cropped from the papers (fig/), so they stay verbatim."""
import os, sys, base64
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'tpl'))
from net import net, amat

def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'

def bend(k): return {'bend': k}

# ---- Cambridge U3&4 13A p. 609: the social media graph (Learn)
SOC_V = {'Anna': (60, 70, 'w'), 'Brett': (200, 70, 'n'), 'Frances': (330, 25, 'n'), 'Ethan': (115, 140, 's'), 'Cora': (215, 135, 's'), 'Dario': (340, 160, 's')}
SOC_E = [('Anna', 'Brett', {'i': 'ab'}), ('Anna', 'Ethan', {'i': 'ae'}), ('Anna', 'Frances', {'i': 'af', 'bend': -12}), ('Brett', 'Cora', {'i': 'bc'}),
         ('Brett', 'Frances', {'i': 'bf'}), ('Cora', 'Dario', {'i': 'cd'}), ('Cora', 'Ethan', {'i': 'ce'}), ('Frances', 'Dario', {'i': 'fd', 'bend': -14}),
         ('Ethan', 'Ethan', {'i': 'el', 'loop': 215, 'hid': True, 'col': '#c0632b'})]
def soc(sid, **k): return net(SOC_V, SOC_E, sid=sid, W=400, H=190, fs=15, pad=34, **k)

# ---- Cambridge Example 1 (p. 612)
EX1_V = {'A': (60, 45, 'n'), 'B': (65, 140, 'e'), 'C': (170, 85, 'n'), 'D': (250, 35, 'n'), 'E': (240, 180, 's'), 'F': (305, 125, 's')}
EX1_E = [('A', 'B', {'i': 'ab1', 'bend': 18}), ('A', 'B', {'i': 'ab2', 'bend': -6}), ('B', 'B', {'i': 'bl', 'loop': 100, 'size': 17}), ('A', 'C', {'i': 'ac'}),
         ('C', 'D', {'i': 'cd', 'bend': 14}), ('C', 'F', {'i': 'cf', 'bend': 8}), ('C', 'E', {'i': 'ce', 'bend': 20}), ('D', 'F', {'i': 'df', 'bend': -12}),
         ('E', 'F', {'i': 'ef', 'bend': 10}), ('F', 'F', {'i': 'fl', 'loop': 0, 'size': 17})]
def ex1(sid, **k): return net(EX1_V, EX1_E, sid=sid, W=360, H=200, pad=14, **k)
def ex1sub(sid='', **k):  # Cambridge's first answer: A-C, A-B
    return net({'A': (30, 30, 'w'), 'C': (110, 20, 'n'), 'B': (60, 90, 's')}, [('A', 'C'), ('A', 'B', bend(-8))], sid=sid, W=150, H=110, pad=10, **{'ink': '#1f9e74', **k})

# ---- Edrolo U3&4 8A Worked example 1 (p. 520)
Y1_V = {'A': (25, 210, 'e'), 'B': (85, 75, 'w'), 'C': (175, 160, 'ne'), 'D': (215, 22, 's'), 'E': (330, 45, 'n'), 'F': (330, 140, 's')}
Y1_E = [('A', 'B', {'i': 'ab'}), ('A', 'C', {'i': 'ac', 'bend': 14}), ('B', 'C', {'i': 'bc', 'bend': 16}), ('C', 'C', {'i': 'cl', 'loop': 95, 'size': 17}),
        ('C', 'D', {'i': 'cd', 'via': [(140, 80)]}), ('D', 'E', {'i': 'de'}), ('D', 'F', {'i': 'df', 'bend': 25}), ('E', 'F', {'i': 'ef'})]
Y1_F = [('f₁', 120, 30, '_f1'), ('f₂', 105, 150, '_f2'), ('f₃', 175, 205, '_f3'), ('f₄', 285, 70, '_f4')]
def y1(sid, faces=False, **k): return net(Y1_V, Y1_E, sid=sid, W=360, H=230, pad=12, faces=Y1_F if faces else (), **k)

# ---- Cambridge Example 2 (p. 613)
EX2_V = {'A': (40, 100, 'w'), 'B': (120, 40, 'n'), 'C': (230, 40, 'n'), 'D': (310, 100, 'e'), 'F': (120, 160, 's'), 'E': (230, 160, 's')}
EX2_E = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'F'), ('F', 'E'), ('E', 'D'), ('A', 'D', {'i': 'ad'}), ('C', 'E', {'i': 'ce'}),
         ('C', 'E', {'i': 'ce2', 'via': [(320, 20), (375, 100), (320, 180)], 'hid': True, 'col': '#1f9e74'})]
def ex2(sid, **k): return net(EX2_V, EX2_E, sid=sid, W=390, H=200, pad=12, **k)

# ---- Edrolo 8A Worked example 2 (p. 523)
Y2_V = {'A': (30, 120, 's'), 'B': (100, 35, 'n'), 'C': (230, 30, 'e'), 'D': (380, 40, 'n'), 'E': (300, 175, 'e')}
Y2_E = [('A', 'B'), ('A', 'C', {'i': 'ac'}), ('A', 'D', {'i': 'ad'}), ('B', 'E', {'i': 'be'}), ('C', 'E', {'i': 'ce'}), ('D', 'E')]
Y2_P = [('A', 'B'), ('B', 'E'), ('C', 'E'), ('D', 'E'), ('A', 'D', {'via': [(120, 225), (320, 225), (400, 120)], 'col': '#1f9e74'}),
        ('A', 'C', {'via': [(20, 40), (110, 5), (200, 8)], 'col': '#1f9e74'})]
def y2(sid, planar=False, **k): return net(Y2_V, Y2_P if planar else Y2_E, sid=sid, W=420, H=230, pad=12, **k)

# ---- Cambridge Example 3 (p. 614)
EX3_V = {'B': (110, 35, 'n'), 'C': (260, 35, 'n'), 'A': (110, 150, 's'), 'D': (260, 150, 's'), 'E': (30, 90, 'n')}
EX3_E = [('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'B'), ('B', 'D', {'i': 'bd'}), ('A', 'C', {'i': 'ac'}), ('E', 'A'),
         ('A', 'C', {'i': 'ac2', 'via': [(200, 205), (310, 195), (325, 100)], 'hid': True, 'col': '#1f9e74'})]
EX3_F = [('f₁', 150, 65, '_f1'), ('f₂', 215, 120, '_f2'), ('f₃', 285, 160, '_f3'), ('f₄', 60, 160, '_f4')]
def ex3(sid, faces=False, **k): return net(EX3_V, EX3_E, sid=sid, W=360, H=210, pad=12, faces=EX3_F if faces else (), **k)

# ---- Cambridge Example 4 (p. 615) answer
EX4_V = {'B': (40, 70, 'w'), 'C': (110, 30, 'n'), 'D': (190, 22, 'n'), 'E': (260, 42, 'ne'), 'F': (315, 85, 'e'), 'A': (175, 195, 's')}
EX4_E = [('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F')]
EX4_F = [('f₁', 115, 95, 'f1'), ('f₂', 160, 70, 'f2'), ('f₃', 205, 70, 'f3'), ('f₄', 245, 95, 'f4'), ('f₅', 300, 170, 'f5')]
def ex4(sid='', **k): return net(EX4_V, EX4_E, sid=sid, W=350, H=215, pad=10, faces=EX4_F, **k)

# ---- Edrolo 8A Worked example 3a (p. 524)
Y3_V = {'A': (40, 20, 'n'), 'D': (190, 25, 'n'), 'B': (30, 130, 'w'), 'C': (165, 165, 'n')}
Y3_E = [('A', 'D'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('B', 'D', {'via': [(90, 225), (240, 205), (255, 70)]})]
Y3_F = [('f₁', 100, 85, '_f1'), ('f₂', 180, 175, '_f2'), ('f₃', 270, 210, '_f3')]
def y3(sid, faces=False, **k): return net(Y3_V, Y3_E, sid=sid, W=300, H=230, pad=12, faces=Y3_F if faces else (), **k)

# ---- Cambridge 13B p. 619 (Learn) graph + matrix
LB_V = {'A': (30, 90, 'w'), 'B': (130, 25, 'n'), 'C': (290, 90, 'e'), 'D': (175, 150, 's'), 'E': (100, 190, 's')}
LB_E = [('A', 'B', {'i': 'ab'}), ('A', 'C', {'i': 'ac'}), ('A', 'E', {'i': 'ae'}), ('B', 'C', {'i': 'bc1'}), ('B', 'C', {'i': 'bc2', 'bend': -22}), ('B', 'D', {'i': 'bd'})]
LB_M = [[0, 1, 1, 0, 1], [1, 0, 2, 1, 0], [1, 2, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]

# ---- Cambridge Example 5 (p. 619): matrix -> graph
EX5_M = [[0, 0, 2, 0, 1], [0, 0, 2, 1, 0], [2, 2, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 0, 0, 0]]
EX5_V = {'A': (40, 85, 'w'), 'B': (215, 30, 'n'), 'D': (330, 55, 'n'), 'C': (220, 160, 's'), 'E': (110, 195, 's')}
EX5_E = [('A', 'C', {'i': 'ac1', 'bend': 14, 'hid': True}), ('A', 'C', {'i': 'ac2', 'bend': -14, 'hid': True}), ('A', 'E', {'i': 'ae', 'hid': True}),
         ('B', 'C', {'i': 'bc1', 'bend': 12, 'hid': True}), ('B', 'C', {'i': 'bc2', 'bend': -12, 'hid': True}), ('B', 'D', {'i': 'bd', 'hid': True}),
         ('C', 'D', {'i': 'cd', 'hid': True}), ('D', 'D', {'i': 'dl', 'loop': 0, 'size': 16, 'hid': True})]
def ex5(sid, **k): return net(EX5_V, EX5_E, sid=sid, W=380, H=215, pad=10, **k)

# ---- Edrolo 8B Worked example 2 (p. 534): matrix -> graph
Y5_M = [[0, 1, 2, 0, 1], [1, 0, 0, 1, 0], [2, 0, 1, 1, 0], [0, 1, 1, 1, 2], [1, 0, 0, 2, 0]]
Y5_V = {'A': (30, 110, 'w'), 'B': (150, 30, 'n'), 'C': (300, 110, 'n'), 'D': (235, 195, 'w'), 'E': (90, 195, 's')}
Y5_E = [('A', 'B'), ('A', 'C'), ('A', 'C', {'via': [(80, 30), (165, 0), (270, 30)]}), ('A', 'E'), ('B', 'D'), ('C', 'C', {'loop': 0, 'size': 15}),
        ('C', 'D'), ('D', 'D', {'loop': 60, 'size': 14}), ('D', 'E', {'bend': 12}), ('D', 'E', {'bend': -12})]
def y5(sid='', **k): return net(Y5_V, Y5_E, sid=sid, W=360, H=225, pad=10, **k)

# ---- Cambridge Example 6 (p. 620): houses and utilities
EX6_V = {'A': (50, 30, 'n'), 'B': (190, 30, 'n'), 'C': (330, 30, 'n'), 'G': (50, 160, 's'), 'W': (190, 160, 's'), 'E': (330, 160, 's')}
EX6_E = [(h, u, {'i': h + u}) for h in 'ABC' for u in 'GWE']
EX6_M = [[0, 0, 0, 1, 1, 1]] * 3 + [[1, 1, 1, 0, 0, 0]] * 3

# ---- Edrolo 8B Worked example 1 (p. 532): graph -> matrix
Y6_V = {'A': (45, 85, 'n'), 'B': (150, 160, 's'), 'C': (175, 20, 'n'), 'D': (235, 200, 's'), 'E': (275, 70, 'n')}
Y6_E = [('A', 'A', {'i': 'al', 'loop': 180, 'size': 15}), ('A', 'B', {'i': 'ab1', 'bend': 14}), ('A', 'B', {'i': 'ab2', 'bend': -14}), ('A', 'C', {'i': 'ac'}),
        ('B', 'C', {'i': 'bc'}), ('B', 'D', {'i': 'bd'}), ('C', 'D', {'i': 'cd'}), ('D', 'E', {'i': 'de'})]
Y6_M = [[1, 2, 1, 0, 0], [2, 0, 1, 1, 0], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [0, 0, 0, 1, 0]]

# ---- APK: Cambridge U1&2 Ch 8 skills checklist #1-2 (p. 540) and #6-8 (p. 541)
K1_V = {'A': (30, 60, 'w'), 'B': (140, 20, 'n'), 'C': (250, 65, 'w'), 'D': (205, 170, 's'), 'E': (90, 170, 'sw')}
K1_E = [('A', 'B', {'i': 'ab'}), ('A', 'E', {'i': 'ae'}), ('B', 'E', {'i': 'be'}), ('B', 'D', {'i': 'bd'}), ('E', 'D', {'i': 'ed'}), ('D', 'C', {'i': 'dc'}),
        ('C', 'C', {'i': 'cl', 'loop': 0, 'size': 17}), ('E', 'E', {'i': 'el', 'loop': 100, 'size': 17})]
K2_V = {'_1': (40, 50), '_2': (250, 50), '_3': (150, 170)}
K2_E = [('_1', '_2'), ('_1', '_3'), ('_2', '_3'), ('_1', '_3', {'via': [(150, 15), (320, 20), (290, 100)]}), ('_1', '_2', {'via': [(45, 170), (150, 230), (260, 160)]})]

# ---- APK: VCAA 2017 Exam 1 N&DM Q2 (Graph 1 = 4 vertices, 6 edges; Graph 2 = hexagon)
def apk3():
    g1 = net({'_1': (45, 20), '_2': (110, 55), '_3': (15, 105), '_4': (100, 130)}, [('_1', '_2'), ('_1', '_3'), ('_1', '_4'), ('_2', '_3'), ('_2', '_4'), ('_3', '_4')],
             W=130, H=150, pad=8, r=5, sid='g1')
    g2 = net({'_1': (60, 15), '_2': (160, 15), '_3': (205, 75), '_4': (160, 135), '_5': (60, 135), '_6': (15, 75)},
             [('_1', '_2'), ('_2', '_3'), ('_3', '_4'), ('_4', '_5'), ('_5', '_6'), ('_6', '_1')], W=220, H=150, pad=8, r=5, sid='g2')
    return ('<div style="display:flex;gap:40px;justify-content:center;align-items:flex-end"><div style="width:150px">' + g1 +
            '<div style="text-align:center;font-weight:700">Graph 1</div></div><div style="width:240px">' + g2 + '<div style="text-align:center;font-weight:700">Graph 2</div></div></div>')

# ---- Exit: VCAA 2021 Exam 2 N&DM Q1 graph (rooms A-E, outside F); A-B is the missing edge
X1_V = {'A': (60, 40, 'w'), 'F': (195, 25, 'e'), 'E': (265, 85, 'n'), 'B': (20, 140, 'w'), 'C': (120, 205, 's'), 'D': (225, 205, 's')}
X1_E = [('A', 'F', {'bend': 14}), ('A', 'F', {'bend': -8}), ('F', 'C', {'via': [(190, 90)]}), ('B', 'C', {'bend': -6}), ('C', 'D'),
        ('B', 'E', {'via': [(30, 230), (150, 260), (285, 210)]}), ('D', 'E', {'bend': -10}),
        ('A', 'B', {'i': 'miss', 'hid': True, 'col': '#d2475b', 'bend': 6})]
def x1(sid, **k): return net(X1_V, X1_E, sid=sid, W=320, H=265, pad=10, **k)
# ---- Exit: VCAA 2021 Exam 1 N&DM Q3 (4 unlabelled vertices, 6 edges, two cross)
X2_V = {'_1': (25, 95), '_2': (150, 20), '_3': (290, 60), '_4': (135, 175)}
X2_E = [('_1', '_2'), ('_2', '_3'), ('_3', '_4'), ('_4', '_1'), ('_1', '_3', {'i': 'x13'}), ('_2', '_4'),
        ('_1', '_3', {'i': 'r13', 'via': [(80, 5), (210, -10), (305, 20)], 'hid': True, 'col': '#1f9e74'})]
X2_F = [('f₁', 90, 70, '_f1'), ('f₂', 200, 65, '_f2'), ('f₃', 140, 120, '_f3'), ('f₄', 260, 140, '_f4')]

# ---- Do Now 1 (VCAA 2024 Exam 1 Q30) option matrices
DN1_OPTS = [[['0', '1.8', '0'], ['0.7', '0', '1.2'], ['0', '0.6', '0']], [['0', '1.8', '1.2'], ['0.7', '0', '0'], ['0', '0.6', '0']],
            [['0', '1.8', '1.2'], ['0.7', '0.6', '0'], ['0', '0', '0']], [['2100', '6400', '4260'], ['0', '1.8', '1.2'], ['0.7', '0.6', '0']]]
# ---- Exit 3 (VCAA 2019 Exam 1 N&DM Q6) option matrices, rows/cols P Q R S T
X3_OPTS = [[[1, 3, 0, 2, 2], [3, 0, 1, 1, 1], [0, 1, 0, 1, 0], [2, 1, 1, 0, 2], [2, 1, 0, 2, 0]],
           [[1, 2, 0, 2, 2], [2, 0, 1, 1, 1], [0, 1, 0, 1, 0], [2, 1, 1, 0, 2], [2, 1, 0, 2, 0]],
           [[0, 3, 0, 2, 2], [3, 0, 1, 1, 1], [0, 1, 0, 1, 0], [2, 1, 1, 0, 2], [2, 1, 0, 2, 0]],
           [[0, 2, 0, 2, 2], [2, 0, 1, 1, 1], [0, 1, 0, 1, 0], [2, 1, 1, 1, 2], [2, 1, 0, 2, 0]],
           [[1, 2, 0, 2, 2], [2, 0, 1, 1, 1], [0, 1, 0, 1, 0], [2, 1, 1, 1, 1], [2, 1, 0, 1, 0]]]
