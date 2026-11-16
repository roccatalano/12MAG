"""Figures for lesson gm12-u4-14c (14C Precedence tables and activity networks).
All networks and graphs are cropped verbatim from the source PDFs (fig/*.png, 200 dpi; crop.py). Precedence tables are typeset with ptab()."""
import os, base64
H = os.path.dirname(os.path.abspath(__file__))
def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'
def ptab(rows, fs=17, head=('Activity', 'Immediate predecessors'), blank=False, red=False, hi=()):
    """Precedence table. rows = [(activity, predecessors)]; blank: leave the predecessor column empty; red: predecessors in red; hi: activities bolded."""
    c = 'color:#d2475b;font-weight:700;' if red else ''
    t = [f'<table class="t" style="margin:4px auto;font-size:{fs}px"><tr><th>{head[0]}</th><th>{head[1]}</th></tr>']
    for a, p in rows:
        b = 'background:#fde9a8;' if a in hi else ''
        t.append(f'<tr><td style="text-align:center;{b}"><i>{a}</i></td><td style="text-align:center;min-width:110px;{c}{b}">{"" if blank else ("<i>" + p + "</i>" if p != "–" else p)}</td></tr>')
    return ''.join(t) + '</table>'
def wtab(rows, fs=16, unit='days', head=None):
    """Weighted precedence table: rows = [(activity, duration, predecessors)]."""
    h = head or ('Activity', f'Duration ({unit})', 'Immediate predecessors')
    t = [f'<table class="t" style="margin:4px auto;font-size:{fs}px"><tr>' + ''.join(f'<th>{x}</th>' for x in h) + '</tr>']
    for a, d, p in rows:
        t.append(f'<tr><td style="text-align:center"><i>{a}</i></td><td style="text-align:center">{d}</td><td style="text-align:center">{"<i>" + p + "</i>" if p != "–" else p}</td></tr>')
    return ''.join(t) + '</table>'
