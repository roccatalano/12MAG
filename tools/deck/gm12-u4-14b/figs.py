"""Figures for lesson gm12-u4-14b (14B Matching and allocation problems).
VCAA figures are cropped verbatim from the papers (fig/*.png, 200 dpi). Bipartite graphs from the textbooks are redrawn
with bip() (same vertices and edges as the source); cost matrices are typeset with cm() (covering lines shown as shaded rows /
columns, allocations circled)."""
import os, base64

H = os.path.dirname(os.path.abspath(__file__))
INK = '#1f4fb0'; RED = '#d2475b'; HL = '#d9b100'


def img(name, w='100%'):
    b = base64.b64encode(open(os.path.join(H, 'fig', name), 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{w};max-width:100%;display:block;margin:4px auto">'


def bip(L, R, E, hl=(), W=360, gap=44, fs=17, ink=INK, hcol=HL, lw=110, rw=110, heads=None):
    """Bipartite graph: L, R = vertex names (left / right column); E = [(l, r)]; hl = edges drawn thick in hcol."""
    n = max(len(L), len(R)); top = 26 if heads else 8
    Hh = top + (n - 1) * gap + 16
    yl = {v: top + i * gap * (n - 1) / max(len(L) - 1, 1) for i, v in enumerate(L)} if len(L) > 1 else {L[0]: top}
    yr = {v: top + i * gap * (n - 1) / max(len(R) - 1, 1) for i, v in enumerate(R)} if len(R) > 1 else {R[0]: top}
    xl, xr = lw, W - rw
    s = [f'<svg viewBox="0 0 {W} {Hh}" width="100%" style="display:block;max-width:{W}px;margin:2px auto;font-family:inherit">']
    if heads:
        s.append(f'<text x="{xl}" y="12" font-size="{fs-2}" font-weight="700" text-anchor="middle" fill="#333">{heads[0]}</text>'
                 f'<text x="{xr}" y="12" font-size="{fs-2}" font-weight="700" text-anchor="middle" fill="#333">{heads[1]}</text>')
    for a, b in E:
        h = (a, b) in hl
        s.append(f'<line x1="{xl}" y1="{yl[a]}" x2="{xr}" y2="{yr[b]}" stroke="{hcol if h else ink}" stroke-width="{5 if h else 2.2}"/>')
    for v, y in yl.items():
        s.append(f'<circle cx="{xl}" cy="{y}" r="5" fill="{ink}"/><text x="{xl-10}" y="{y+5}" font-size="{fs}" text-anchor="end" fill="#222">{v}</text>')
    for v, y in yr.items():
        s.append(f'<circle cx="{xr}" cy="{y}" r="5" fill="{ink}"/><text x="{xr+10}" y="{y+5}" font-size="{fs}" fill="#222">{v}</text>')
    return ''.join(s) + '</svg>'


def cm(cols, rows, cover_r=(), cover_c=(), circ=(), fs=15, extra=None, xh='', hi=(), col='#fde9a8'):
    """Cost matrix table. rows = [(name, [values])]. cover_r / cover_c: indexes of covered rows / columns (shaded = a line).
    circ: {(r, c)} circled (allocations). extra: list of values for an extra right-hand column headed xh. hi: {(r, c)} bold."""
    t = [f'<table class="cmx" style="border-collapse:collapse;margin:3px auto;font-size:{fs}px">'
         '<tr><th></th>' + ''.join(f'<th style="padding:1px 6px;color:#0a7a8a">{c}</th>' for c in cols) + (f'<th style="padding:1px 6px;color:#888;font-size:.8em">{xh}</th>' if extra else '') + '</tr>']
    for i, (nm, vals) in enumerate(rows):
        t.append(f'<tr><th style="text-align:left;padding:1px 6px;color:#0a7a8a">{nm}</th>')
        for k, v in enumerate(vals):
            bg = ''
            if i in cover_r and k in cover_c: bg = 'background:#f6c453;'
            elif i in cover_r or k in cover_c: bg = f'background:{col};'
            inner = f'<span style="border:2.5px solid {RED};border-radius:50%;padding:0 5px">{v}</span>' if (i, k) in circ else (f'<b>{v}</b>' if (i, k) in hi else v)
            t.append(f'<td style="{bg}border:1px solid #bbb;padding:1px 7px;text-align:center">{inner}</td>')
        if extra: t.append(f'<td style="padding:1px 6px;color:#888;text-align:center">{extra[i]}</td>')
        t.append('</tr>')
    return ''.join(t) + '</table>'
