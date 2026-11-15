"""Figures for lesson l04 (2C): parallel boxplots, parallel dot plots, back-to-back stem plots.
Used by both the slides (build.py) and the guided worksheet (worksheet.py). All redrawn from the source figures (values read off them).
data-i keys (for data-hi / data-show on slides): boxplot row r -> 'r' (whole row), 'rb' box, 'rm' median, 'rw' whiskers, 'ro' outliers;
dot plot group g, k-th smallest value -> 'g.k'; stem plot leaves -> 'L<row>.<k>' / 'R<row>.<k>'."""

def _num(x): return ('%g' % x)

def pbox(rows, lo, hi, step, xl='', W=900, rowH=70, fs=17, lab=130, minor=None, ink='#1f3b73', fill='#dbe6fb', hid=False,
         ticks=True, grid=False, sw=2.4, out_r=6, tick_every=1, top=8):
    """rows: [(label, (min, q1, med, q3, max), [outliers])]. Drawn top to bottom in list order."""
    L, R = lab, 24; T = top; ph = rowH * len(rows); B = 30 + (24 if xl else 0)
    H = T + ph + B; pw = W - L - R
    X = lambda v: L + (v - lo) / (hi - lo) * pw
    h0 = ' class="hid0"' if hid else ''
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block">']
    if grid:
        v = lo
        while v <= hi + 1e-9:
            s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{T}" y2="{T+ph}" stroke="#d7dde8" stroke-width="1"/>'); v += step
    for r, (name, (mn, q1, m, q3, mx), outs) in enumerate(rows):
        cy = T + r * rowH + rowH / 2; bh = rowH * .46
        s.append(f'<text x="{L-12}" y="{cy+fs*.35:.1f}" text-anchor="end" font-size="{fs}" font-weight="600">{name}</text>')
        g = f'<g data-i="{r}"{h0}>'
        g += (f'<line data-i="{r}w" x1="{X(mn):.1f}" x2="{X(q1):.1f}" y1="{cy}" y2="{cy}" stroke="{ink}" stroke-width="{sw}"/>'
              f'<line data-i="{r}w" x1="{X(q3):.1f}" x2="{X(mx):.1f}" y1="{cy}" y2="{cy}" stroke="{ink}" stroke-width="{sw}"/>'
              f'<line data-i="{r}w" x1="{X(mn):.1f}" x2="{X(mn):.1f}" y1="{cy-bh/4:.1f}" y2="{cy+bh/4:.1f}" stroke="{ink}" stroke-width="{sw}"/>'
              f'<line data-i="{r}w" x1="{X(mx):.1f}" x2="{X(mx):.1f}" y1="{cy-bh/4:.1f}" y2="{cy+bh/4:.1f}" stroke="{ink}" stroke-width="{sw}"/>'
              f'<rect data-i="{r}b" x="{X(q1):.1f}" y="{cy-bh/2:.1f}" width="{X(q3)-X(q1):.1f}" height="{bh:.1f}" fill="{fill}" stroke="{ink}" stroke-width="{sw}"/>'
              f'<line data-i="{r}m" x1="{X(m):.1f}" x2="{X(m):.1f}" y1="{cy-bh/2:.1f}" y2="{cy+bh/2:.1f}" stroke="{ink}" stroke-width="{sw*1.6:.1f}"/>')
        for o in outs: g += f'<circle data-i="{r}o" cx="{X(o):.1f}" cy="{cy}" r="{out_r}" fill="#fff" stroke="{ink}" stroke-width="{sw*.8:.1f}"/>'
        s.append(g + '</g>')
    y0 = T + ph + 4
    s.append(f'<line x1="{L}" x2="{L+pw}" y1="{y0}" y2="{y0}" stroke="#333" stroke-width="1.6"/>')
    if minor:
        v = lo
        while v <= hi + 1e-9:
            s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{y0}" y2="{y0+4}" stroke="#333"/>'); v += minor
    if ticks:
        v = lo; k = 0
        while v <= hi + 1e-9:
            s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{y0}" y2="{y0+8}" stroke="#333" stroke-width="1.4"/>')
            if k % tick_every == 0: s.append(f'<text x="{X(v):.1f}" y="{y0+8+fs}" text-anchor="middle" font-size="{fs-1}">{_num(round(v, 6))}</text>')
            v += step; k += 1
    if xl: s.append(f'<text x="{L+pw/2:.1f}" y="{H-6}" text-anchor="middle" font-size="{fs}" font-style="italic" font-weight="600">{xl}</text>')
    return ''.join(s) + '</svg>'

def pbox_keys(r): return f'{r},{r}b,{r}m,{r}w,{r}o'

def pdot(groups, lo, hi, step=1, xl='', W=900, gh=110, fs=17, r=7, ink='#2f6fdf', hid=False, lab_every=1, label_side='top'):
    """groups: [(label, [values])]. One dot plot per group, same scale. Equal values stack."""
    L, R = 30, 24; pw = W - L - R; B = 40 + (22 if xl else 0)
    H = len(groups) * (gh + 46) + 4
    X = lambda v: L + (v - lo) / (hi - lo) * pw
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="display:block">']
    h0 = ' class="hid0"' if hid else ''
    for g, (name, vals) in enumerate(groups):
        y0 = g * (gh + 46) + gh
        s.append(f'<text x="{L}" y="{y0-gh+fs}" font-size="{fs}" font-weight="700">{name}</text>')
        cnt = {}
        for k, v in enumerate(sorted(vals)):
            c = cnt.get(v, 0); cnt[v] = c + 1
            s.append(f'<circle data-i="{g}.{k}"{h0} cx="{X(v):.1f}" cy="{y0-r-2-c*(2*r+2):.1f}" r="{r}" fill="{ink}"/>')
        s.append(f'<line x1="{L}" x2="{L+pw}" y1="{y0}" y2="{y0}" stroke="#333" stroke-width="1.6"/>')
        v = lo; k = 0
        while v <= hi + 1e-9:
            s.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{y0}" y2="{y0+6}" stroke="#333"/>')
            if k % lab_every == 0: s.append(f'<text x="{X(v):.1f}" y="{y0+8+fs}" text-anchor="middle" font-size="{fs-1}">{_num(v)}</text>')
            v += step; k += 1
        if xl: s.append(f'<text x="{L+pw/2:.1f}" y="{y0+30+fs}" text-anchor="middle" font-size="{fs-1}" font-style="italic">{xl}</text>')
    return ''.join(s) + '</svg>'

def pdot_keys(g, n): return ','.join(f'{g}.{k}' for k in range(n))

def bbstem(rid, stems, left, right, lhead, rhead, keyl='', keyr='', title='', fs=22, hid=False, cls='bbs'):
    """back-to-back stem plot. left[i]/right[i] = leaves for stems[i] (left leaves written as printed, i.e. largest nearest... as given)."""
    h0 = ' hid0' if hid else ''
    def lv(side, i, xs): return ''.join(f'<span class="lf2{h0}" data-i="{side}{i}.{k}">{x}</span>' for k, x in enumerate(xs))
    tr = ''.join(f'<tr><td class="lv l">{lv("L", i, left[i])}</td><td class="st">{s}</td><td class="lv r">{lv("R", i, right[i])}</td></tr>' for i, s in enumerate(stems))
    hd = f'<tr><th class="lv l">{lhead}</th><th></th><th class="lv r">{rhead}</th></tr>'
    cap = (f'<div class="bbcap">{title}</div>' if title else '') + (f'<div class="bbkey"><span>{keyl}</span><span>{keyr}</span></div>' if keyl or keyr else '')
    return f'<div class="{cls}">{cap}<table class="bb" id="{rid}" style="font-size:{fs}px">{hd}{tr}</table></div>'

BBCSS = ('<style>.bbs{display:inline-block}.bbs .bbcap{text-align:center;font-style:italic;font-weight:600;margin-bottom:2px}'
         '.bbs .bbkey{display:flex;justify-content:space-between;gap:40px;font-size:.8em;margin-bottom:2px}'
         'table.bb{border-collapse:collapse;margin:0 auto}table.bb td,table.bb th{padding:1px 4px}table.bb th{font-weight:700;background:none}'
         'table.bb td.st{border-left:2px solid #333;border-right:2px solid #333;font-weight:700;text-align:center;min-width:1.4em}'
         'table.bb td.l,table.bb th.l{text-align:right}table.bb td.r,table.bb th.r{text-align:left}table.bb .lf2{display:inline-block;min-width:1.05em;text-align:center}'
         '.T line.hy{stroke:#d9b100!important;stroke-width:6}.T line.hb{stroke:#2f6fdf!important;stroke-width:6}.T line.hg{stroke:#1f9e74!important;stroke-width:6}'
         '.T circle.hc{fill:#c0632b!important}.T g.hy rect{fill:#fff3c4}</style>')

# ---------------- data (read off the source figures; see build.py docstring)
EX9 = [('Before', [22, 22, 23, 24, 25, 26, 26, 26, 28, 29, 29, 30, 31, 34, 46]), ('After', [24, 25, 25, 26, 28, 30, 30, 32, 33, 34, 35, 36, 43, 50, 54])]
EX10 = ([3, 4, 5, 6, 7, 8], [['8'], [], ['9', '4', '2'], ['9', '9', '9', '8', '7', '7', '1', '0'], ['4'], []],
        [[], [], ['8'], ['9'], ['1', '2', '4', '4', '6', '8', '9', '9'], ['0', '0', '0']])
EX11 = [('Female', (50, 65, 72, 80, 100), []), ('Male', (50, 60, 65, 70, 82), [40, 120])]
EX12 = [('50–65 years', (68, 70, 72, 89.5, 109), [119, 126, 140]), ('40–49 years', (62.5, 66, 70.5, 83.5, 100), [110]),
        ('30–39 years', (57.5, 61, 68, 75, 89.5), []), ('20–29 years', (54, 58, 64, 70, 73), [])]
YT2 = [('Grade 5', [2, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 9]), ('Grade 6', [5, 6, 6, 7, 8, 8, 8, 8, 9, 9, 9, 10])]
YT1A = [64, 68, 70, 53, 57, 62, 74, 77, 36, 41, 66]; YT1E = [59, 90, 83, 87, 88, 76, 82, 83, 91, 78, 75]
YT1 = ([3, 4, 5, 6, 7, 8, 9], [['6'], ['1'], ['7', '3'], ['8', '6', '4', '2'], ['7', '4', '0'], [], []],
       [[], [], ['9'], [], ['5', '6', '8'], ['2', '3', '3', '7', '8'], ['0', '1']])
YT3 = [('Salomons', (2, 4, 5, 9, 15), []), ('Crocs', (0, 2, 4, 7, 8), [])]
YT4 = [('rural', (0.4, 0.5, 0.6, 0.7, 1.0), []), ('outer suburbs', (0.6, 0.8, 1.1, 1.5, 1.9), [2.2]), ('inner suburbs', (0.9, 1.2, 1.6, 2.0, 2.4), [])]
NT27 = ([0, 1, 2, 3, 4], [['9', '7'], ['8', '1'], ['5', '3', '1', '1'], ['9', '5', '3', '1', '1', '0', '0'], ['5', '4']],
        [['1', '8', '9'], ['4', '7'], ['3', '4', '4', '5'], ['0', '1', '2', '7', '8', '9'], ['7']])
V19Q2 = [('maximum daily temperature (°C)', (19, 22, 25, 27, 30), [14]), ('minimum daily temperature (°C)', (7, 12, 15, 17, 21), [])]
V21Q4 = [('Pond A', (1, 2.2, 4.3, 6.3, 7.3), []), ('Pond B', (5.4, 6.6, 7.6, 8.6, 10.5), [])]
V19Q3 = [('February', (5.9, 9.5, 10.9, 13.9, 19.1), [22.2]), ('May', (3.3, 6.0, 7.5, 9.8, 12.7), []), ('July', (1.6, 3.7, 5.0, 5.9, 7.7), [])]
V17 = ([1, 2, 2, 3, 3, 4, 4, 5], [['6'], ['2', '1', '1', '0', '0', '0', '0'], ['7'], ['4', '0'], ['5'], [], [], ['2']],
       [['8'], ['2', '2', '4', '4'], ['5', '5', '9'], ['0', '0', '1', '2', '3', '4'], ['6', '8'], ['0', '3'], ['5'], []])
