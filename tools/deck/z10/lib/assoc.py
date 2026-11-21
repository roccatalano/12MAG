from .deck import *
from . import deck as _d
import re
_d.use("assoc")
"""Associations (Chapter 2): two-way tables that fill in (tf) with row (hr) and cell (tc) highlights, grouped bar charts
(ax / bg / lg, same engine as lib/cat.py: import cat too), scatterplots (sx:id points appear, sl:id line appears),
back-to-back stem plots, parallel dot plots and parallel boxplots (static figures)."""
COLS = ['#9ec5f0', '#f6c27a', '#a8dca8', '#e7a9d6']


def twoway(id_, rv, ev, cats, rows, total=None, totcol=None, tothead='Total', cls=''):
    """Two-way table: EV labels the columns, RV the rows. rows = [(RV category, [cells])]. A cell is text or (key, text):
    a (key, text) cell is blank until a step with tf:id:key. Cells have data-k = 100*row + col (tc:id:k), rows data-r (hr:id:r);
    the total row is row 9."""
    def c(x, k):
        if isinstance(x, tuple): return f'<td data-k="{k}"><span data-f="{x[0]}">{x[1]}</span></td>'
        return f'<td data-k="{k}">{x}</td>'
    n = len(cats) + (1 if totcol else 0)
    h = (f'<tr><th class="zcorner"></th><th colspan="{len(cats)}"><i>{ev}</i></th>' + ('<th class="zcorner"></th>' if totcol else '') + '</tr>'
         f'<tr><th><i>{rv}</i></th>' + ''.join(f'<th>{x}</th>' for x in cats) + (f'<th>{tothead}</th>' if totcol else '') + '</tr>')
    for r, (lab, cells) in enumerate(rows):
        cc = list(cells) + ([totcol[r]] if totcol else [])
        h += f'<tr data-r="{r}"><td class="l">{lab}</td>' + ''.join(c(x, 100 * r + j) for j, x in enumerate(cc)) + '</tr>'
    if total:
        h += '<tr data-r="9" class="ztot"><td class="l"><b>Total</b></td>' + ''.join(c(x, 900 + j) for j, x in enumerate(total)) + '</tr>'
    return f'<table class="ztab ztw {cls}" id="{id_}">{h}</table>'


def gbar(id_, cats, names, vals, ymax, ystep, xl, yl, w=560, h=330, full=False):
    """Grouped bar chart: one group per EV category (cats), one bar per RV category (names); vals[j][i] = names[j] in cats[i].
    Bars data-i = 10*group + bar (bg:id:0,1,2 grows group 0)."""
    X0, X1, Y0, Y1 = 66, w - 140, h - 58, 16
    py = lambda y: Y0 - y / ymax * (Y0 - Y1)
    ax = ''.join(f'<line x1="{X0}" y1="{py(y):.1f}" x2="{X1}" y2="{py(y):.1f}" stroke="#ddd"/><text x="{X0-8}" y="{py(y)+5:.1f}" font-size="15" text-anchor="end">{y}</text>' for y in range(0, ymax + 1, ystep))
    gw = (X1 - X0) / len(cats); bw = gw * 0.8 / len(names); bars = ''
    for i, c in enumerate(cats):
        ax += f'<text x="{X0+gw*(i+.5):.1f}" y="{Y0+22}" font-size="15" text-anchor="middle">{c}</text>'
        for j in range(len(names)):
            v = vals[j][i]; x = X0 + i * gw + gw * 0.1 + j * bw
            bars += f'<rect class="cbr" data-i="{10*i+j}" x="{x:.1f}" y="{py(v):.1f}" width="{bw:.1f}" height="{Y0-py(v):.1f}" fill="{COLS[j]}" stroke="#000" stroke-width="1.5"/>'
    ax += (f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="#000" stroke-width="2"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="#000" stroke-width="2"/>'
           f'<text x="{(X0+X1)/2}" y="{Y0+48}" font-size="16" text-anchor="middle" font-style="italic">{xl}</text>'
           f'<text transform="translate(18 {(Y0+Y1)/2}) rotate(-90)" font-size="16" text-anchor="middle" font-style="italic">{yl}</text>')
    lg = ''.join(f'<rect x="{X1+18}" y="{Y1+10+j*28}" width="18" height="18" fill="{COLS[j]}" stroke="#000"/><text x="{X1+44}" y="{Y1+24+j*28}" font-size="15">{n}</text>' for j, n in enumerate(names))
    return f'<svg class="zch zgb{" full" if full else ""}" id="{id_}" viewBox="0 0 {w} {h}"><g class="cax">{ax}</g>{bars}<g class="clg">{lg}</g></svg>'


def _ticks(lo, hi, step):
    out = []; k = 0
    while lo + k * step <= hi + 1e-9: out.append(round(lo + k * step, 6)); k += 1
    return out


def _f(v):
    return str(int(v)) if float(v).is_integer() else str(v)


def scat(id_, pts, xr, yr, xl, yl, line=None, w=520, h=360, build=False, grid=True, r=5, curve=None, seg=None, ticks=True, shown=False):
    """Scatterplot. xr / yr = (lo, hi, step). line = (a, b) for y = a + b x, hidden until sl:id. build=True: points hidden until sx:id."""
    X0, X1, Y0, Y1 = 74, w - 16, h - 56, 14
    px = lambda x: X0 + (x - xr[0]) / (xr[1] - xr[0]) * (X1 - X0)
    py = lambda y: Y0 - (y - yr[0]) / (yr[1] - yr[0]) * (Y0 - Y1)
    s = ''
    for x in _ticks(*xr):
        if grid: s += f'<line x1="{px(x):.1f}" y1="{Y0}" x2="{px(x):.1f}" y2="{Y1}" stroke="#e5e5e5"/>'
        s += f'<text x="{px(x):.1f}" y="{Y0+20}" font-size="14" text-anchor="middle">{_f(x)}</text>'
    for y in _ticks(*yr):
        if grid: s += f'<line x1="{X0}" y1="{py(y):.1f}" x2="{X1}" y2="{py(y):.1f}" stroke="#e5e5e5"/>'
        s += f'<text x="{X0-7}" y="{py(y)+5:.1f}" font-size="14" text-anchor="end">{_f(y)}</text>'
    s += (f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="#000" stroke-width="2"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="#000" stroke-width="2"/>'
          f'<text x="{(X0+X1)/2}" y="{h-10}" font-size="15" text-anchor="middle" font-style="italic">{xl}</text>'
          f'<text transform="translate(18 {(Y0+Y1)/2}) rotate(-90)" font-size="15" text-anchor="middle" font-style="italic">{yl}</text>')
    s += '<g class="zsp">' + ''.join(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="{r}" fill="#000"/>' for x, y in pts) + '</g>'
    if line:
        a, b = line; x0, x1 = xr[0], xr[1]
        y0, y1 = a + b * x0, a + b * x1
        # clip to the y range
        if y0 < yr[0] or y0 > yr[1]: yy = yr[0] if y0 < yr[0] else yr[1]; x0 = (yy - a) / b; y0 = yy
        if y1 < yr[0] or y1 > yr[1]: yy = yr[0] if y1 < yr[0] else yr[1]; x1 = (yy - a) / b; y1 = yy
        s += f'<line class="zsl" x1="{px(x0):.1f}" y1="{py(y0):.1f}" x2="{px(x1):.1f}" y2="{py(y1):.1f}" stroke="#d00000" stroke-width="3"/>'
    if curve:  # [(x, y), ...] drawn as a red curve, hidden until sl:id
        s += '<polyline class="zsl" fill="none" stroke="#d00000" stroke-width="3" points="' + ' '.join(f'{px(x):.1f},{py(y):.1f}' for x, y in curve) + '"/>'
    if seg:  # ((x1, y1), (x2, y2)) red trend line segment, hidden until sl:id
        (a1, b1), (a2, b2) = seg
        s += f'<line class="zsl" x1="{px(a1):.1f}" y1="{py(b1):.1f}" x2="{px(a2):.1f}" y2="{py(b2):.1f}" stroke="#d00000" stroke-width="3"/>'
    if not ticks: s = re.sub(r'<text[^>]*>[^<]*</text>', '', s)
    return f'<svg class="zsc{" zbuild" if build else ""}{" zshown" if shown else ""}" id="{id_}" viewBox="0 0 {w} {h}">{s}</svg>'


def b2b(id_, left, right, stems, lab=('', ''), key=''):
    """Back-to-back stem plot. left / right = {stem: 'leaves'} or lists (one per stem row) (left leaves written as they appear, reading outwards
    from the stem, i.e. already reversed)."""
    g = lambda d, i, s: d[i] if isinstance(d, (list, tuple)) else d.get(s, '')   # lists: one entry per stem row (repeated stems allowed)
    tr = ''.join(f'<tr><td class="zbl">{g(left, i, s)}</td><td class="zbs">{s}</td><td class="zbr">{g(right, i, s)}</td></tr>' for i, s in enumerate(stems))
    return (f'<div class="zb2b" id="{id_}"><div class="zb2k">{key}</div><table><tr><th class="zbl">{lab[0]}</th><th></th><th class="zbr">{lab[1]}</th></tr>{tr}</table></div>')


def pdots(id_, groups, lo, hi, step, xl, w=600, row=70, lab_w=110):
    """Parallel dot plots. groups = [(label, [values])], drawn top to bottom."""
    X0, X1 = lab_w, w - 20
    px = lambda x: X0 + (x - lo) / (hi - lo) * (X1 - X0)
    h = row * len(groups) + 60; s = ''
    for g, (lab, vals) in enumerate(groups):
        base = 20 + row * (g + 1) - 12
        s += f'<text x="{X0-12}" y="{base}" font-size="16" text-anchor="end">{lab}</text><line x1="{X0}" y1="{base+4}" x2="{X1}" y2="{base+4}" stroke="#999"/>'
        cnt = {}
        for v in sorted(vals):
            k = cnt.get(v, 0); cnt[v] = k + 1
            s += f'<circle cx="{px(v):.1f}" cy="{base-5-k*11}" r="5" fill="#000"/>'
    ay = h - 40
    s += f'<line x1="{X0}" y1="{ay}" x2="{X1}" y2="{ay}" stroke="#000" stroke-width="2"/>'
    for x in _ticks(lo, hi, step):
        s += f'<line x1="{px(x):.1f}" y1="{ay}" x2="{px(x):.1f}" y2="{ay+6}" stroke="#000"/><text x="{px(x):.1f}" y="{ay+22}" font-size="14" text-anchor="middle">{_f(x)}</text>'
    s += f'<text x="{(X0+X1)/2}" y="{h-2}" font-size="15" text-anchor="middle" font-style="italic">{xl}</text>'
    return f'<svg class="zpd" id="{id_}" viewBox="0 0 {w} {h}">{s}</svg>'


def pbox(*a, w=600, row=64, lab_w=130, out=None, minor=None, id_=''):
    """pbox([id,] groups, lo, hi, step, xl): parallel boxplots. groups = [(label, (min-or-whisker, Q1, M, Q3, max-or-whisker), [outliers])], top to bottom."""
    if isinstance(a[0], str): id_, a = a[0], a[1:]
    groups, lo, hi, step, xl = a
    X0, X1 = lab_w, w - 20
    px = lambda x: X0 + (x - lo) / (hi - lo) * (X1 - X0)
    h = row * len(groups) + 56; s = ''
    for g, gr in enumerate(groups):
        lab, (a, q1, m, q3, b) = gr[0], gr[1]; outs = gr[2] if len(gr) > 2 else []
        cy = 12 + row * g + row / 2; t, bt = cy - row * 0.28, cy + row * 0.28
        s += (f'<text x="{X0-12}" y="{cy+5}" font-size="16" text-anchor="end">{lab}</text>'
              f'<line x1="{px(a):.1f}" y1="{cy}" x2="{px(q1):.1f}" y2="{cy}" stroke="#000" stroke-width="2"/><line x1="{px(q3):.1f}" y1="{cy}" x2="{px(b):.1f}" y2="{cy}" stroke="#000" stroke-width="2"/>'
              f'<rect x="{px(q1):.1f}" y="{t:.1f}" width="{px(q3)-px(q1):.1f}" height="{bt-t:.1f}" fill="#fff" stroke="#000" stroke-width="2"/>'
              f'<line x1="{px(m):.1f}" y1="{t:.1f}" x2="{px(m):.1f}" y2="{bt:.1f}" stroke="#000" stroke-width="3.5"/>'
              + ''.join(f'<circle cx="{px(o):.1f}" cy="{cy}" r="5" fill="#fff" stroke="#000" stroke-width="2"/>' for o in outs))
    ay = h - 40
    s += f'<line x1="{X0}" y1="{ay}" x2="{X1}" y2="{ay}" stroke="#000" stroke-width="2"/>'
    for x in _ticks(lo, hi, minor or step):
        big = abs((x - lo) / step - round((x - lo) / step)) < 1e-6
        s += f'<line x1="{px(x):.1f}" y1="{ay}" x2="{px(x):.1f}" y2="{ay+(7 if big else 4)}" stroke="#000"/>'
        if big: s += f'<text x="{px(x):.1f}" y="{ay+22}" font-size="14" text-anchor="middle">{_f(x)}</text>'
    s += f'<text x="{(X0+X1)/2}" y="{h-2}" font-size="15" text-anchor="middle" font-style="italic">{xl}</text>'
    return f'<svg class="zpb" id="{id_}" viewBox="0 0 {w} {h}">{s}</svg>'


def keyslide(code, KD, KF, src):
    """Key ideas slide (as Chapter 1): key definitions | key formulas."""
    S.append(f'<section class="slide z kif">{bar(code, "Key ideas")}<div class="cols" style="grid-template-columns:1.1fr .9fr">'
             f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
             f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
             f'{foot(src)}</section>')
