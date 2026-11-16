from .deck import *
from . import deck as _d
_d.use("boxplot")
"""Boxplot engine (S4): parts appear with bx:id:p,p (bx1 = only this band), bxo colours outliers, bdx marks dot-plot extremes."""
def fmt(v, dec=0):
    s = f'{v:.{dec}f}' if dec else (str(int(v)) if float(v).is_integer() else str(v))
    return s.replace('-', '−')

def bplot(id_, lo, hi, step, lab, f5, out=(), xl='', build=False, hide=(), fences=(), marks=(), bands=(), W=640, caps=False, dec=0, col='#fff', T=None):
    """Boxplot SVG. f5 = (lower whisker end, Q1, M, Q3, upper whisker end). Parts (data-p): axis, box, med, wl, wu, out,
    plus named fences (p, x, label[, lv]), marks (p, x, label[, colour, lv]) and bands (p, a, b, label).
    Fences / marks / bands start hidden; build=True also hides the plot itself. Steps show parts with bx:id:p,p (bx1 = only this band)."""
    lw, q1, m, q3, uw = f5
    lv_max = max([0] + [f[3] if len(f) > 3 else 0 for f in fences] + [k[4] if len(k) > 4 else 0 for k in marks])
    T = T if T is not None else (34 + 22 * lv_max if (fences or marks or bands) else 12)
    px = lambda x: 30 + (x - lo) / (hi - lo) * (W - 60)
    bt, bb = T + 8, T + 62; cy = (bt + bb) / 2; ay = bb + 26
    H = ay + (54 if xl else 32)
    g = lambda p, s: f'<g data-p="{p}">{s}</g>'
    ax = f'<line x1="{px(lo)-8}" y1="{ay}" x2="{px(hi)+8}" y2="{ay}" stroke="#000" stroke-width="2"/>'
    k = 0; x = lo
    while x <= hi + 1e-9:
        big = abs(((x - lo) / lab) - round((x - lo) / lab)) < 1e-6
        ax += f'<line x1="{px(x):.1f}" y1="{ay-(7 if big else 4)}" x2="{px(x):.1f}" y2="{ay+(7 if big else 4)}" stroke="#000" stroke-width="{1.6 if big else 1}"/>'
        if big: ax += f'<text x="{px(x):.1f}" y="{ay+25}" font-size="17" text-anchor="middle">{fmt(round(x, 6), dec)}</text>'
        k += 1; x = lo + k * step
    if xl: ax += f'<text x="{W/2}" y="{ay+48}" font-size="17" text-anchor="middle">{xl}</text>'
    s = g('axis', ax)
    for p, a, b, t in bands:
        s += g(p, f'<rect x="{px(a):.1f}" y="{bt-6}" width="{px(b)-px(a):.1f}" height="{bb-bt+12}" fill="rgba(31,95,191,.16)" stroke="#1f5fbf" stroke-width="2" stroke-dasharray="5 4"/>'
                  f'<text x="{(px(a)+px(b))/2:.1f}" y="{bt-12}" font-size="18" font-weight="bold" fill="#1f5fbf" text-anchor="middle">{t}</text>')
    s += g('box', f'<rect x="{px(q1):.1f}" y="{bt}" width="{px(q3)-px(q1):.1f}" height="{bb-bt}" fill="{col}" stroke="#000" stroke-width="2.5"/>')
    s += g('med', f'<line x1="{px(m):.1f}" y1="{bt}" x2="{px(m):.1f}" y2="{bb}" stroke="#000" stroke-width="4"/>')
    cap = lambda x: f'<line x1="{px(x):.1f}" y1="{cy-12}" x2="{px(x):.1f}" y2="{cy+12}" stroke="#000" stroke-width="2.5"/>' if caps else ''
    s += g('wl', f'<line x1="{px(lw):.1f}" y1="{cy}" x2="{px(q1):.1f}" y2="{cy}" stroke="#000" stroke-width="2.5"/>' + cap(lw))
    s += g('wu', f'<line x1="{px(q3):.1f}" y1="{cy}" x2="{px(uw):.1f}" y2="{cy}" stroke="#000" stroke-width="2.5"/>' + cap(uw))
    s += g('out', ''.join(f'<circle class="bo" cx="{px(o):.1f}" cy="{cy}" r="6.5" fill="#fff" stroke="#000" stroke-width="2.5"/>' for o in out))
    for f in fences:
        p, xx, t = f[:3]; lv = f[3] if len(f) > 3 else 0
        s += g(p, f'<line x1="{px(xx):.1f}" y1="{T-4-22*lv}" x2="{px(xx):.1f}" y2="{ay}" stroke="#1f5fbf" stroke-width="2.5" stroke-dasharray="7 5"/>'
                  f'<text x="{px(xx):.1f}" y="{T-10-22*lv}" font-size="17" font-weight="bold" fill="#1f5fbf" text-anchor="middle">{t}</text>')
    for mk in marks:
        p, xx, t = mk[:3]; c = mk[3] if len(mk) > 3 else '#d00000'; lv = mk[4] if len(mk) > 4 else 0
        s += g(p, f'<text x="{px(xx):.1f}" y="{T-8-22*lv}" font-size="18" font-weight="bold" fill="{c}" text-anchor="middle">{t}</text>'
                  f'<line x1="{px(xx):.1f}" y1="{T-4-22*lv}" x2="{px(xx):.1f}" y2="{bt-2}" stroke="{c}" stroke-width="1.5"/>')
    hid = [f[0] for f in fences] + [mk[0] for mk in marks] + [b[0] for b in bands] + list(hide)
    if build: hid += ['axis', 'box', 'med', 'wl', 'wu', 'out']
    return f'<svg class="zbx" id="{id_}" data-hide="{",".join(hid)}" viewBox="0 0 {W} {H}">{s}</svg>'


def rowtab(id_, head, vals):
    return table_hl(id_, [(head, vals)], 'ztab zinq')
