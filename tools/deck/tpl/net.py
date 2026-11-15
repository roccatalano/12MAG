"""Reusable graph / network drawing helper (Chapter 13-14, AoS 4). Static SVG, same look on slides and worksheets.
Graphs are redrawn from the source figure with the same vertices and edges (layout follows the source).

net(V, E, ...) where
  V = {'A': (x, y), ...} or {'A': (x, y, 'ne')}   label position: n ne e se s sw w nw (default 'n'); label '' = unlabelled vertex
  E = list of edges, each a tuple (a, b) or (a, b, opts) with opts a dict:
      bend: perpendicular offset of a curved edge (px, + = left of a->b) · loop: direction in degrees for a loop (a == b)
      i: data-i name (default e<k>) · hid: start hidden (reveal with data-show="#sid|e3") · dash: dashed · col: colour
      w: weight label (networks) · arrow: True for a directed edge a->b · via: [(x, y), ...] a smooth path through points
Edges and vertices can be highlighted with data-hi="#sid|e1,e2|hy" (hy hb hg hc) and vertices by data-i="vA".
faces: [(text, x, y, name)] small italic labels (hidden: name starts with '_' -> data-i=name[1:] and class hid0).
"""
import math

INK = '#1f4fb0'
CSS = ('<style>.net path.hy,.net line.hy{stroke:#d9b100!important;stroke-width:6!important}'
       '.net path.hb{stroke:#2f6fdf!important;stroke-width:6!important}.net path.hg{stroke:#1f9e74!important;stroke-width:6!important}'
       '.net path.hc{stroke:#c0632b!important;stroke-width:6!important}.net text.hy{fill:#b08a00;font-weight:800}'
       '.net .hy,.net .hb,.net .hg,.net .hc,.net .hv{outline:none!important;background:none!important}.net path.hv,.net path.hx{stroke-dasharray:6 6;opacity:.3}</style>')
_OFF = {'n': (0, -1), 'ne': (.75, -.75), 'e': (1, 0), 'se': (.75, .85), 's': (0, 1.1), 'sw': (-.75, .85), 'w': (-1, 0), 'nw': (-.75, -.75)}


def net(V, E, sid='', W=360, H=240, fs=18, r=5, ink=INK, lw=2.6, faces=(), mm=None, extra='', pad=0, padx=None):
    px = pad if padx is None else padx
    s = [f'<svg class="net"{" id=" + chr(34) + sid + chr(34) if sid else ""} viewBox="{-px} {-pad} {W+2*px} {H+2*pad}" width="100%" '
         f'style="display:block;{"max-width:" + str(mm) + "mm;margin:1mm auto;" if mm else ""}">{CSS}'
         '<defs>' + ''.join(f'<marker id="ah{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in sorted({ink} | {(e[2].get('col') or ink) for e in E if len(e) > 2 and e[2].get('arrow')})) + '</defs>']
    P = {k: v[:2] for k, v in V.items()}
    for k, e in enumerate(E):
        a, b = e[0], e[1]; o = e[2] if len(e) > 2 else {}
        col = o.get('col', ink)
        att = f'data-i="{o.get("i", "e" + str(k))}"' + (' class="hid0"' if o.get('hid') else '')
        st = f'fill="none" stroke="{col}" stroke-width="{lw}"' + (' stroke-dasharray="7 6"' if o.get('dash') else '') + (f' marker-end="url(#ah{col[1:]})"' if o.get('arrow') else '')
        (x1, y1), (x2, y2) = P[a], P[b]
        if a == b:
            ang = math.radians(o.get('loop', -90)); R = o.get('size', 16)
            cx, cy = x1 + R * math.cos(ang), y1 + R * math.sin(ang)
            s.append(f'<path {att} d="M{x1:.1f},{y1:.1f} a{R},{R} 0 1,1 {2*(cx-x1):.2f},{2*(cy-y1):.2f} a{R},{R} 0 1,1 {-2*(cx-x1):.2f},{-2*(cy-y1):.2f}" {st}/>')
            mx, my = cx, cy
        elif o.get('via'):
            pts = [P[a]] + list(o['via']) + [P[b]]
            d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
            for j in range(1, len(pts)):  # Catmull-Rom -> cubic Bezier
                p0 = pts[max(j - 2, 0)]; p1 = pts[j - 1]; p2 = pts[j]; p3 = pts[min(j + 1, len(pts) - 1)]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                d += f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
            s.append(f'<path {att} d="{d}" {st}/>'); mx, my = pts[len(pts) // 2]
        else:
            bd = o.get('bend', 0); L = math.hypot(x2 - x1, y2 - y1) or 1
            nx, ny = (y1 - y2) / L, (x2 - x1) / L
            cx, cy = (x1 + x2) / 2 + 2 * bd * nx, (y1 + y2) / 2 + 2 * bd * ny
            if o.get('arrow'):  # stop short of the vertex
                tx, ty = x2 - cx, y2 - cy; tl = math.hypot(tx, ty) or 1; x2, y2 = x2 - tx / tl * (r + 2), y2 - ty / tl * (r + 2)
            s.append(f'<path {att} d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" {st}/>')
            mx, my = (x1 + x2) / 2 + bd * nx, (y1 + y2) / 2 + bd * ny
        if 'w' in o:
            s.append(f'<text x="{mx:.1f}" y="{my-6:.1f}" text-anchor="middle" font-size="{fs-2}" fill="#222" paint-order="stroke" stroke="#fff" stroke-width="4">{o["w"]}</text>')
    for t, x, y, nm in faces:
        hid = nm.startswith('_'); nm = nm.lstrip('_')
        s.append(f'<text data-i="{nm}"{" class=" + chr(34) + "hid0" + chr(34) if hid else ""} x="{x}" y="{y}" text-anchor="middle" font-size="{fs-2}" font-style="italic" fill="#c0632b" font-weight="700">{t}</text>')
    for k, v in V.items():
        x, y = v[:2]; pos = v[2] if len(v) > 2 else 'n'
        s.append(f'<circle data-i="v{k}" cx="{x}" cy="{y}" r="{r}" fill="#111"/>')
        if k and not k.startswith('_'):
            dx, dy = _OFF[pos]
            ex = (len(k) - 1) * fs * .27 if dy == 0 or abs(dx) > .5 else 0
            s.append(f'<text data-i="t{k}" x="{x + dx*(fs*.85 + ex):.1f}" y="{y + dy*(fs*.85) + fs*.35:.1f}" text-anchor="middle" font-size="{fs}" font-style="italic" font-family="Times New Roman,serif">{k}</text>')
    s.append(extra + '</svg>')
    return ''.join(s)


def amat(labels, rows, fs=18, tid='', blank=False, cols=None, cls=''):
    """Adjacency matrix as a bracketed table with row and column labels. Cells data-i="c{r}_{k}" (for data-hi / data-show).
    blank=True: cells start hidden (hid0) for filling step by step with data-show."""
    cols = cols or labels
    hd = '<tr><th></th>' + ''.join(f'<th class="ml">{c}</th>' for c in cols) + '<th></th></tr>'
    body = ''
    n = len(rows)
    for i, (lab, r) in enumerate(zip(labels, rows)):
        body += f'<tr><th class="ml">{lab}</th>' + ''.join(
            f'<td data-i="c{i}_{k}"><span data-i="v{i}_{k}"{" class=" + chr(34) + "hid0" + chr(34) if blank else ""}>{v}</span></td>' for k, v in enumerate(r))
        body += '<td></td></tr>'
    st = ('<style>.amat{border-collapse:collapse;margin:6px auto}.amat td,.amat th{padding:1px .5em!important;text-align:center;min-width:1.2em;font-size:inherit!important}'
          '.amat th.ml{color:#0a7a8a;font-style:italic;font-weight:600}.amat tr:not(:first-child) td:nth-child(2){border-left:2px solid #222}'
          '.amat tr:not(:first-child) td:nth-last-child(2){border-right:2px solid #222}</style>')
    return st + f'<table class="amat {cls}"{" id=" + chr(34) + tid + chr(34) if tid else ""} style="font-size:{fs}px">{hd}{body}</table>'
