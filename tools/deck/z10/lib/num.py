from .deck import *
from . import deck as _d
_d.use("num")
"""Numerical displays that build up (S2): histogram bars one per click (xb) with the table row highlighted (fill/xs),
dot plots (xd, xm), stem leaves (xl), key as its own step (sk), SOCS template fill (bf, bok)."""
def dlist(id_, vals, cols, cls='ztab zdl2'):
    """data list in a grid; cell for value i has data-k = (i//cols)*100 + i%cols"""
    rows = [vals[i:i + cols] for i in range(0, len(vals), cols)]
    h = ''.join('<tr>' + ''.join(f'<td data-k="{r*100+c}">{v}</td>' for c, v in enumerate(row)) + '</tr>' for r, row in enumerate(rows))
    return f'<table class="{cls}" id="{id_}">{h}</table>'
def dk(cols, idxs): return ','.join(str((i // cols) * 100 + i % cols) for i in idxs)
def where(vals, test): return [i for i, v in enumerate(vals) if test(v)]
def sk(vals, test): return J2([i for i, v in enumerate(sorted(vals)) if test(v)])  # dot index (sorted order)
def ftab(id_, head, rows):
    """frequency table that fills in: every cell starts blank, cell (r, c) has data-k = r*10 + c"""
    hd = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td data-k="{r*10+c}">{v}</td>' for c, v in enumerate(row)) + '</tr>' for r, row in enumerate(rows))
    return f'<table class="zft zfill" id="{id_}"><tr>{hd}</tr>{tr}</table>'
def fills(id_, cells): return ' '.join(f'fill:{id_}:{k}' for k in cells)
def rowk(r, ncol): return [r * 10 + c for c in range(ncol)]
def bars(id_, idxs): return f'xb:{id_}:{J2(idxs)}'
def stemmap(vals, stems, ordered):
    """rows for stem() + map data index -> leaf k"""
    rows, mp, k = [], {}, 0
    for s in stems:
        ix = [i for i, v in enumerate(vals) if v // 10 == s]
        if ordered: ix = sorted(ix, key=lambda i: vals[i])
        for i in ix: mp[i] = k; k += 1
        rows.append((str(s), ' '.join(str(vals[i] % 10) for i in ix)))
    return rows, mp
def bigdot(id_, vals, lo, hi, xl, H=330, W=640):
    """dot plot for large n (the zdp engine is sized for small n)"""
    cnt, s = {}, ''
    mx = max(vals.count(v) for v in set(vals)); step = min(22, (H - 80) / mx); r = min(9, step / 2 - .4)
    px = lambda x: 40 + (x - lo) / (hi - lo) * (W - 80); Y = H - 60
    s += f'<line x1="20" y1="{Y}" x2="{W-20}" y2="{Y}" stroke="#000" stroke-width="2"/>'
    for x in range(lo, hi + 1):
        s += f'<line x1="{px(x)}" y1="{Y-6}" x2="{px(x)}" y2="{Y+6}" stroke="#000"/><text x="{px(x)}" y="{Y+26}" font-size="17" text-anchor="middle">{x}</text>'
    for k, v in enumerate(sorted(vals)):
        cnt[v] = cnt.get(v, 0) + 1
        s += f'<circle class="dot" data-k="{k}" cx="{px(v):.1f}" cy="{Y - step*cnt[v] + step/2 - 2:.1f}" r="{r:.2f}" fill="#555"/>'
    s += f'<text x="{W/2}" y="{H-8}" font-size="17" text-anchor="middle">{xl}</text>'
    return f'<svg class="zbd" id="{id_}" viewBox="0 0 {W} {H}">{s}</svg>'


def hist_build(*a, **k):
    """hist() whose bars start hidden: show them one per click with xb:id:i (and highlight the matching
    frequency-table row in the same step, e.g. 'xb:h1:0 xs:t1:1' or fill:t1:k for a filling table)."""
    return hist(*a, **k).replace('class="zhg"', 'class="zhg zbuild"')


def socs_tpl(id_, shape, outliers, centre, spread):
    """SOCS answer template (describe a distribution): shown first with blank lines, one line per letter; fill it line by
    line with bf:id:0 .. bf:id:3 (several: bf:id:0-3), then bok:id turns it green. Put it in qslide steps as a plain
    string (it starts with <div class="zpart" so it is not wrapped as a step). Wording follows CLAUDE.md SOCS."""
    b = lambda k, v: f'<span class="s2b" data-b="{k}">{v}</span>'
    return (f'<div class="zpart s2tpl" id="{id_}"><span class="zok">✓ Answer</span> '
            f'<b>S</b> The distribution is {b(0, shape)}.<br><b>O</b> There {b(1, outliers)}.<br>'
            f'<b>C</b> The distribution is centred at {b(2, centre)}.<br><b>S</b> {b(3, spread)}.</div>')
