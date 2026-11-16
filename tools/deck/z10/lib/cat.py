from .deck import *
from . import deck as _d
_d.use("cat")
"""Categorical charts (S1): bar charts and segmented bar charts that build one bar/segment per click (ax, bg, lg),
frequency tables and reports that fill in (tf), chips and row highlights (hv, hr), bar -> stacked -> 100% morph (mo)."""
COL = ['#9ec5f0', '#f6c27a', '#a8dca8', '#e7a9d6']

def bchart(id_, cats, vals, ymax, ystep, xl, yl, full=False, w=520, h=340):
    X0, X1, Y0, Y1 = 70, w - 20, h - 60, 20; n = len(cats); slot = (X1 - X0) / n; bw = slot * 0.55
    py = lambda y: Y0 - y / ymax * (Y0 - Y1)
    ax = ''.join(f'<line x1="{X0}" y1="{py(y)}" x2="{X1}" y2="{py(y)}" stroke="#ddd"/><text x="{X0-8}" y="{py(y)+5}" font-size="15" text-anchor="end">{y}</text>' for y in range(0, ymax + 1, ystep))
    ax += ''.join(f'<text x="{X0+slot*(i+.5)}" y="{Y0+22}" font-size="16" text-anchor="middle">{c}</text>' for i, c in enumerate(cats))
    ax += f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="#000" stroke-width="2"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="#000" stroke-width="2"/>'
    ax += f'<text x="{(X0+X1)/2}" y="{Y0+48}" font-size="16" text-anchor="middle" font-style="italic">{xl}</text><text transform="translate(20 {(Y0+Y1)/2}) rotate(-90)" font-size="16" text-anchor="middle" font-style="italic">{yl}</text>'
    bars = ''.join(f'<rect class="cbr" data-i="{i}" x="{X0+slot*(i+.5)-bw/2}" y="{py(v)}" width="{bw}" height="{Y0-py(v)}" fill="{COL[0]}" stroke="#000" stroke-width="2"/>' for i, v in enumerate(vals))
    return f'<svg class="zch{" full" if full else ""}" id="{id_}" viewBox="0 0 {w} {h}"><g class="cax">{ax}</g>{bars}</svg>'

def schart(id_, bars, names, scale, tick, yl, xl='', full=False, w=420, h=340):
    """bars: [(label, [segment values bottom->top])]; segments data-i = bar*10 + seg"""
    X0, Y0, Y1 = 70, h - 50, 20; n = len(bars); slot = 140; bw = 90; X1 = X0 + slot * n + 10
    py = lambda y: Y0 - y / scale * (Y0 - Y1)
    ax = ''.join(f'<line x1="{X0-5}" y1="{py(y)}" x2="{X0}" y2="{py(y)}" stroke="#000"/><text x="{X0-8}" y="{py(y)+5}" font-size="14" text-anchor="end">{y}</text>' for y in range(0, scale + 1, tick))
    ax += f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="#000" stroke-width="2"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="#000" stroke-width="2"/>'
    ax += f'<text transform="translate(18 {(Y0+Y1)/2}) rotate(-90)" font-size="15" text-anchor="middle" font-style="italic">{yl}</text>'
    if xl: ax += f'<text x="{(X0+X1)/2}" y="{Y0+42}" font-size="15" text-anchor="middle" font-style="italic">{xl}</text>'
    segs = ''
    for b, (lab, vs) in enumerate(bars):
        x = X0 + 20 + b * slot; base = 0
        if lab: ax += f'<text x="{x+bw/2}" y="{Y0+20}" font-size="15" text-anchor="middle">{lab}</text>'
        for s, v in enumerate(vs):
            segs += f'<rect class="cbr" data-i="{b*10+s}" x="{x}" y="{py(base+v)}" width="{bw}" height="{py(base)-py(base+v)}" fill="{COL[s]}" stroke="#000" stroke-width="2"/>'
            base += v
    lx = X1 + 14; lg = ''
    for k, nm in enumerate(reversed(names)):
        s = len(names) - 1 - k
        lg += f'<rect x="{lx}" y="{Y1+10+k*28}" width="18" height="18" fill="{COL[s]}" stroke="#000"/><text x="{lx+26}" y="{Y1+24+k*28}" font-size="15">{nm}</text>'
    return f'<svg class="zch{" full" if full else ""}" id="{id_}" viewBox="0 0 {w} {h}"><g class="cax">{ax}</g>{segs}<g class="clg">{lg}</g></svg>'

def freq_table(id_, var, rows, total, pcth='Percentage', blank=True):
    """Cambridge-style frequency table. blank=True: numbers/percentages hidden until tf:id:n0,p0,nT,pT"""
    f = (lambda k, v: f'<span data-f="{k}">{v}</span>') if blank else (lambda k, v: str(v))
    tr = ''.join(f'<tr data-r="{i}"><td class="l">{a}</td><td>{f("n%d" % i, b)}</td><td>{f("p%d" % i, c)}</td></tr>' for i, (a, b, c) in enumerate(rows))
    return (f'<table class="ztab zft{" zbl" if blank else ""}" id="{id_}"><tr><th rowspan="2">{var}</th><th colspan="2">Frequency</th></tr><tr><th>Number</th><th>{pcth}</th></tr>{tr}'
            f'<tr data-r="{len(rows)}"><td class="l"><b>Total</b></td><td><b>{f("nT", total[0])}</b></td><td><b>{f("pT", total[1])}</b></td></tr></table>')

def chips(id_, vals, lab=None):
    return f'<div class="zchips" id="{id_}">' + ''.join(f'<span class="zc" data-v="{v}">{lab(v) if lab else v}</span>' for v in vals) + '</div>'

def report(id_, toks):
    """toks: text or (key, filled text). Blanks show as dashed lines until tf fills them."""
    return f'<div class="zrep" id="{id_}">' + ''.join(t if isinstance(t, str) else f'<span class="zrb" data-f="{t[0]}">{t[1]}</span>' for t in toks) + '</div>'


def schart_big(id_, vals, names, scale, tick, yl, fmt):
    """One segmented bar, large text. Segments data-i 0,1,2 (bottom->top), boundary labels appear with each segment."""
    W_, H_, X0, Y0, Y1, bw = 440, 400, 84, 360, 22, 120
    py = lambda y: Y0 - y / scale * (Y0 - Y1)
    ax = ''.join(f'<line x1="{X0-7}" y1="{py(y):.1f}" x2="{X0}" y2="{py(y):.1f}" stroke="#000" stroke-width="2"/><text x="{X0-11}" y="{py(y)+7:.1f}" font-size="20" text-anchor="end">{y}</text>' for y in range(0, scale + 1, tick))
    ax += f'<line x1="{X0}" y1="{Y0}" x2="{X0+bw+60}" y2="{Y0}" stroke="#000" stroke-width="2.5"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1-8}" stroke="#000" stroke-width="2.5"/>'
    ax += f'<text transform="translate(22 {(Y0+Y1)/2}) rotate(-90)" font-size="21" text-anchor="middle" font-style="italic">{yl}</text>'
    segs = ''; base = 0; x = X0 + 30
    for i, v in enumerate(vals):
        top = base + v
        segs += (f'<g class="cbr" data-i="{i}"><rect x="{x}" y="{py(top):.1f}" width="{bw}" height="{py(base)-py(top):.1f}" fill="{COL[i]}" stroke="#000" stroke-width="2.5"/>'
                 f'<line x1="{x+bw}" y1="{py(top):.1f}" x2="{x+bw+14}" y2="{py(top):.1f}" stroke="#d00000" stroke-width="2"/>'
                 f'<text x="{x+bw+18}" y="{py(top)+7:.1f}" font-size="20" font-weight="bold" fill="#d00000">{fmt[i]}</text></g>')
        base = top
    lx = X0 + bw + 130; lg = ''
    for k in range(len(names)):
        s_ = len(names) - 1 - k
        lg += f'<rect x="{lx}" y="{Y1+20+k*36}" width="24" height="24" fill="{COL[s_]}" stroke="#000" stroke-width="2"/><text x="{lx+32}" y="{Y1+40+k*36}" font-size="21">{names[s_]}</text>'
    return f'<svg class="zch zbig" id="{id_}" viewBox="0 0 {W_} {H_}"><g class="cax">{ax}</g>{segs}<g class="clg">{lg}</g></svg>'

def morph_svg(id_, names, vals, ymax, tick, xl, yl='Frequency'):
    """Bar chart that the JS (op mo:id:stage) slides into one stacked bar (stage 1), rescales to 100% (stage 2)
    and adds the legend (stage 3). vals = frequencies; ymax = frequency axis max (>= total); tick = frequency axis step."""
    n = len(vals); W_, H_ = 600, 520; X0, Y0, Y1 = 92, 450, 40
    t = '<g class="mof">' + ''.join(f'<line x1="{X0-7}" y1="{Y0-y/ymax*(Y0-Y1):.1f}" x2="{X0}" y2="{Y0-y/ymax*(Y0-Y1):.1f}" stroke="#000" stroke-width="2"/><text x="{X0-12}" y="{Y0-y/ymax*(Y0-Y1)+8:.1f}" font-size="22" text-anchor="end">{y}</text>' for y in range(0, ymax + 1, tick))
    t += f'<text transform="translate(26 {(Y0+Y1)/2}) rotate(-90)" font-size="24" text-anchor="middle" font-style="italic">{yl}</text></g>'
    t += '<g class="mop">' + ''.join(f'<line x1="{X0-7}" y1="{Y0-y/100*(Y0-Y1):.1f}" x2="{X0}" y2="{Y0-y/100*(Y0-Y1):.1f}" stroke="#000" stroke-width="2"/><text x="{X0-12}" y="{Y0-y/100*(Y0-Y1)+8:.1f}" font-size="22" text-anchor="end">{y}</text>' for y in range(0, 101, 20))
    t += f'<text transform="translate(26 {(Y0+Y1)/2}) rotate(-90)" font-size="24" text-anchor="middle" font-style="italic">Percentage (%)</text></g>'
    ax = f'<line x1="{X0}" y1="{Y0}" x2="{W_-150}" y2="{Y0}" stroke="#000" stroke-width="2.5"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1-10}" stroke="#000" stroke-width="2.5"/>'
    cl = '<g class="mocat">' + ''.join(f'<text class="moc" data-i="{i}" x="0" y="{Y0+30}" font-size="22" text-anchor="middle">{nm}</text>' for i, nm in enumerate(names)) + '</g>'
    cl += f'<text class="moxl" x="{(X0+W_-150)/2}" y="{Y0+62}" font-size="22" text-anchor="middle" font-style="italic">{xl}</text>'
    r = ''.join(f'<rect class="mor" data-i="{i}" fill="{COL[i]}" stroke="#000" stroke-width="2.5"/>' for i in range(n))
    lb = ''.join(f'<text class="mol" data-i="{i}" font-size="23" font-weight="bold" text-anchor="middle"></text>' for i in range(n))
    lg = '<g class="molg">' + ''.join(f'<rect x="{W_-120}" y="{Y1+40+k*40}" width="26" height="26" fill="{COL[n-1-k]}" stroke="#000" stroke-width="2"/><text x="{W_-84}" y="{Y1+62+k*40}" font-size="23">{names[n-1-k]}</text>' for k in range(n)) + '</g>'
    return (f'<svg class="zmorph" id="{id_}" viewBox="0 0 {W_} {H_}" data-g="{X0},{Y0},{Y1},{W_-150}" data-v="{",".join(str(v) for v in vals)}" data-ymax="{ymax}">'
            f'{t}{ax}{cl}{r}{lb}{lg}</svg>')
