"""Matrix helper for Ch 10-11 slides and worksheets (AoS 3). Pure inline-styled HTML, so it works in the slide engine and in ws2.py.
mat(rows, name='A', rl=['M','F'], cl=['W','A','F'], tid='m1', fs=22)
- rows: list of rows (numbers or strings); cells get data-i="c{r}_{k}" so slide steps can highlight them (data-hi="#m1|c0_1|hy").
- name: shown as 'name =' in front · rl/cl: row/column labels (Cambridge style: row labels left, column labels on top)
- side: put the row labels on the right (Edrolo style) · sup: superscript after the right bracket (e.g. 'T')."""
def _c(v): return str(v).replace('-', '−') if isinstance(v, (int, float)) or (isinstance(v, str) and v.startswith('-')) else str(v)
def mat(rows, name=None, rl=None, cl=None, tid='', fs=None, side=False, sup='', pad='1px 7px', col='currentColor'):
    n = len(rows); m = max(len(r) for r in rows)
    st = f'font-size:{fs}px;' if fs else ''
    br = lambda s: f'<td rowspan="{n}" style="width:5px;padding:0;border:2px solid {col};border-{s}:none"></td>'
    lab = lambda t: f'<td style="padding:{pad};font-style:italic;opacity:.8">{t}</td>'
    t = f'<table{" id=" + chr(34) + tid + chr(34) if tid else ""} style="border-collapse:collapse;display:inline-table;width:auto;margin:0;vertical-align:middle;{st}line-height:1.25">'
    if cl:
        t += '<tr>' + ('<td></td>' if rl and not side else '') + '<td></td>' + ''.join(lab(x) for x in cl) + '<td></td></tr>'
    for r, row in enumerate(rows):
        t += '<tr>' + (lab(rl[r]) if rl and not side else '') + (br('right') if r == 0 else '')
        t += ''.join(f'<td data-i="c{r}_{k}" style="padding:{pad};text-align:center">{_c(v)}</td>' for k, v in enumerate(row))
        t += (br('left') if r == 0 else '') + (lab(rl[r]) if rl and side else '') + '</tr>'
    t += '</table>'
    if sup: t = f'<span style="display:inline-flex;align-items:flex-start;vertical-align:middle">{t}<sup style="font-size:.7em">{sup}</sup></span>'
    return (f'<span style="display:inline-flex;align-items:center;gap:6px;vertical-align:middle;{st}"><i>{name}</i>&nbsp;=&nbsp;{t}</span>' if name else t)
def cells(r0, r1, k0, k1): return ','.join(f'c{r}_{k}' for r in range(r0, r1) for k in range(k0, k1))
