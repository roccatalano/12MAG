"""Figures for lesson gm12-u4-14a (14A Flow problems).
Source figures are cropped verbatim from the PDFs (fig/*.png, 200 dpi). The two written You trys (YT-14A-4, YT-14A-5,
planner/written-youtrys.json) have no source figure, so they are drawn with tools/deck/tpl/net.py (arrow=True)."""
import os, sys, base64, itertools
_N = itertools.count()
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'tpl'))
from net import net

RED = '#d2475b'


def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'


def _E(L, flow=None):
    out = []
    for a, b, w, i in L:
        o = {'w': w, 'i': i, 'arrow': True}
        if flow and i in flow: o['col'] = RED
        out.append((a, b, o))
    return out


# YT-14A-4: wildlife park, A (source) to G (sink); max flow 36 (checked with networkx)
Y4_V = {'A': (0, 110, 'w'), 'B': (120, 0, 'n'), 'C': (250, 30, 'ne'), 'D': (150, 110, 'ne'), 'E': (50, 220, 's'), 'F': (190, 220, 's'), 'G': (330, 140, 'e')}
Y4_L = [('A', 'B', 14, 'ab'), ('A', 'D', 18, 'ad'), ('A', 'E', 7, 'ae'), ('B', 'C', 9, 'bc'), ('B', 'D', 6, 'bd'), ('C', 'G', 11, 'cg'),
        ('D', 'C', 4, 'dc'), ('D', 'G', 10, 'dg'), ('D', 'F', 8, 'df'), ('E', 'F', 12, 'ef'), ('F', 'G', 20, 'fg')]
Y4_CUT = ['cg', 'dg', 'df', 'ae']        # minimum cut 11 + 10 + 8 + 7 = 36
def _u(s):
    """unique arrow-marker ids per svg (a marker defined on a hidden slide does not render elsewhere)"""
    n = next(_N); return s.replace('markerWidth="7" markerHeight="7"', 'markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14"').replace('id="ah', f'id="ah{n}_').replace('url(#ah', f'url(#ah{n}_')
def yt4(sid='', **k): return _u(net(Y4_V, _E(Y4_L, k.pop('flow', None)), sid=sid, W=330, H=220, pad=26, padx=30, fs=19, **k))

# YT-14A-5: two sources, two outlets; Outlet 1 max 600, Outlet 2 max 650 (checked with networkx)
Y5_V = {'Source 1': (0, 0, 'w'), 'Source 2': (0, 220, 'w'), 'P': (170, 0, 'n'), 'Q': (170, 110, 'ne'), 'R': (170, 220, 's'), 'Outlet 1': (360, 50, 'e'), 'Outlet 2': (360, 180, 'e')}
Y5_L = [('Source 1', 'P', 500, 'sp'), ('Source 1', 'Q', 300, 'sq'), ('Source 2', 'Q', 200, 'tq'), ('Source 2', 'R', 400, 'tr'), ('P', 'Outlet 1', 350, 'po'),
        ('P', 'Q', 150, 'pq'), ('Q', 'Outlet 1', 250, 'qo'), ('Q', 'R', 100, 'qr'), ('Q', 'Outlet 2', 200, 'qp'), ('R', 'Outlet 2', 450, 'ro')]
def yt5(sid='', **k):
    s = net(Y5_V, _E(Y5_L, k.pop('flow', None)), sid=sid, W=360, H=220, pad=30, padx=95, fs=17, **k)
    for a, b in (('>S1<', '>Source 1<'), ('>S2<', '>Source 2<'), ('>O1<', '>Outlet 1<'), ('>O2<', '>Outlet 2<')): s = s.replace(a, b)
    return _u(s)
