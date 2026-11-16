r"""12MAG S2 (1C-1E Displaying and describing numerical data) rebuilt in the 10MA slide house style.
Shell (CSS + navigation/tile engine JS) copied from 10MA '10MAG Univariate Statistics - Slides.html'.
python3 build.py  ->  lessons/S2-slides-v2.html
"""
import json, html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SH = os.path.join(HERE, "shell")
OUT = os.path.join(HERE, "..", "..", "..", "lessons", "S2-slides-v2.html")
HEAD = open(os.path.join(SH,'head.html')).read().replace('10MAG Univariate Statistics · Slides', '12MAG S2 · Displaying and describing numerical data · Slides')
TAIL = open(os.path.join(SH,'tail.html')).read()
CG = 'Cambridge General Mathematics Units 3&amp;4'
ED = 'Edrolo General Mathematics Units 3&amp;4'
SUB = '1C–1E Displaying numerical data'
S = []

def bar(tag, h1, yt=False):
    return f'<div class="bar{" ytb" if yt else ""}"><span class="tag">{tag}</span><h1>{h1}</h1><span class="sub">{SUB}</span></div>'
def foot(src): return f'<div class="foot"><span>{src}</span><span class="pg"></span></div>'
TILEOPS=('sort','cross','mid','clr','band')
def st(t, final=False, do=None, cls=''):
    a = ''
    if do:
        ta=[x for x in do.split() if x.split(':')[0] in TILEOPS]; za=[x for x in do.split() if x.split(':')[0] not in TILEOPS]
        if ta: a += f' data-act="{" ".join(ta)}"'
        a += f' data-do="{" ".join(za)}"'
    return f'<div class="st zs{" final" if final else ""} {cls}"{a}>{t}</div>'
def stat(): return '<div class="zstat">VCAA: <b>?%</b> of students answered correctly</div>'
def sumtiles(id_, vals, unit='', label='running total'):
    t=''.join(f'<span class="zt" data-k="{k}">{v}</span>' for k,v in enumerate(vals))
    return f'<div class="zsumw" id="{id_}"><div class="ztiles">{t}</div><div class="zrun"><span>{label}</span><b data-u="{unit}">0</b></div></div>'
def table_hl(id_, rows, cls='ztab'):
    """rows: list of (header, [cells]); cells get data-k numbered per row r*100+c"""
    h=''
    for r,(hd,cells) in enumerate(rows):
        h+=f'<tr><th>{hd}</th>'+''.join(f'<td data-k="{r*100+c}">{v}</td>' for c,v in enumerate(cells))+'</tr>'
    return f'<table class="{cls}" id="{id_}">{h}</table>'
def mc(opts, dist):
    return '<div class="zmc">'+''.join(f'<div data-o="{L}"><span class="pb"></span><b>{L}.</b> {o}<span class="pc">{d}%</span></div>' for (L,o),d in zip(opts,dist))+'</div>'
def ki(head, body): return f'<div class="ki"><div class="kh">{head}</div><div class="kb">{body}</div></div>'

# ---------- figures ----------
def dotplot(id_, vals, lo, hi, xl=''):
    return f'<svg class="zdp" id="{id_}" data-v="{json.dumps(sorted(vals))}" data-lo="{lo}" data-hi="{hi}" data-xl="{xl}" viewBox="0 0 640 262"></svg>'
def hist(id_, start, w, v, ymax, ystep, xl='', yl='Frequency'):
    cfg = dict(start=start, w=w, v=v, ymax=ymax, ystep=ystep, xl=xl, yl=yl)
    return f"<svg class=\"zhg\" id=\"{id_}\" data-cfg='{json.dumps(cfg)}' viewBox=\"0 0 600 330\"></svg>"
def stem(id_, rows, key, head=('Stem', 'Leaf'), build=False):
    k = 0; tr = ''
    for s, leaves in rows:
        cells = ''
        for l in leaves.split():
            cells += f'<span class="lv" data-k="{k}">{l}</span>'; k += 1
        tr += f'<tr><td class="zst">{s}</td><td class="zlv">{cells}</td></tr>'
    return f'<div class="zstem" id="{id_}"><table><tr><th>{head[0]}</th><th>{head[1]}</th></tr>{tr}</table><div class="zkey' + (' zkh' if build else '') + f'">{key}</div></div>'
def tiles(t, orig):
    srt = sorted(orig, key=float)
    return '<div class="tl" data-t="%s">%s</div>' % (t, ''.join(f'<span class="mtile" data-o="{o}" data-s="{s}">{o}</span>' for o, s in zip(orig, srt)))

# ---------- slide shells ----------

# ================= ONE TEMPLATE FOR EVERY QUESTION SLIDE =================
# Layout (always): bar [tag | title | source pill]
#   top:  question (+ marks)            | side: VCAA % badge (exam only), command chip, Key idea (always)
#   body: figure / data / MC options    | working: one idea per click (red) -> ✓ Answer (bold)
#         -> exam MC: What's the distractor? -> % bars      exam short answer: Watch out
TAGS = {'ex': 'Example', 'yt': 'You try', 'apk': 'APK', 'exam': 'Exam practice', 'exit': 'Exit task', 'cas': 'CAS example'}

def W(t, do=None):
    return st(t, do=do)

def part(lab):
    return f'<div class="zpart">{lab}</div>'

def qslide(kind, num, title, pill, q, kib, steps, answer, src, fig='', figw='1fr', marks=None, cmd=None,
           vcaa=None, opts=None, key=None, dis=None, watch=None, ans_do='', cls='', stack=False, parts=None):
    yt = kind in ('yt',)
    tag = TAGS[kind] + (f' {num}' if num else '')
    mk = f' <span class="zmk">({marks} mark{"s" if marks and marks > 1 else ""})</span>' if marks else ''
    side = (stat() if vcaa is not None else '') + '' + ki('Key idea', kib)
    body = ''.join(W(*s) if isinstance(s, tuple) else (s if s.startswith('<div class="zpart') else W(s)) for s in steps)
    import re as _re
    m = _re.search(r'<br><b>([a-z])\.</b> (.*)$', q)
    if m and not parts and vcaa is None:   # single lettered part: ask it in the working box
        parts = [(m.group(1) + '.', m.group(2), steps, answer, ans_do or None)]; q = q[:m.start()]
        body = ''
    if parts:  # context on top; each part asked, worked and answered in the working box
        body = ''
        for k, pt in enumerate(parts):
            lab, txt, stp, ans = pt[:4]; pdo = pt[4] if len(pt) > 4 else None
            body += f'<div class="zpq{" brk" if k and stack else ""}{" sep" if k else ""}"><b>{lab}</b> {txt}</div>'
            body += ''.join(W(*x) if isinstance(x, tuple) else W(x) for x in stp)
            body += st(f'<span class="zok">✓ Answer</span> {ans}', True, do=pdo, cls='zpa')
    elif opts:  # multiple choice exam question
        body += st(f'<span class="zok">✓ Answer</span> <b>{key}</b>' + (f' · {answer}' if answer else ''), True, do=f'key:{key}')
        body += st('<span class="zsc">How did students answer? Bars show the % choosing each option.</span>',
                   do=f'key:{key} pct stat:{vcaa}' + (f' dis:{dis[0]}' if dis else ''))
    if parts: pass
    elif not opts:
        sd = (ans_do + (f' stat:{vcaa}' if vcaa is not None else '')).strip() or None
        body += st(f'<span class="zok">✓ Answer</span> {answer}', True, do=sd)
        if watch:
            body += st(f'<span class="zdl zw2">Watch out</span> {watch}', cls='zdis')
    figcol = fig + (mc(opts, OPTDIST[num or title]) if opts else '')
    grid = f'grid-template-columns:{figw} 1fr' if figcol else 'grid-template-columns:1fr'
    figh = f'<div class="zfig zcol">{figcol}</div>' if figcol else ''
    head = f'<div class="bar{" ytb" if yt else ""}"><span class="tag">{tag}</span><h1>{title}</h1><span class="sub zpill">{pill}</span></div>'
    if vcaa is not None:   # exam layout: question + data (+ options) left; badge, command, key idea, working right
        return (f'<section class="slide z ex k-{kind} exam {cls}">{head}'
                f'<div class="zb" style="grid-template-columns:{figw} 1fr;margin-top:14px"><div class="zfig zcol zmcq"><div class="zq">{q}{mk}</div>{figcol}</div>'
                f'<div class="zw"><div class="zside zrow2">{stat()}</div>{ki("Key idea", kib)}{body}</div></div>{foot(src)}</section>')
    if stack:
        return (f'<section class="slide z ex{" yt" if yt else ""} k-{kind} {cls}">{head}'
                f'<div class="top"><div class="q">{q}{mk}</div><div class="zside">{side}</div></div>'
                f'<div class="zb stack"><div class="zfig zrowf">{figcol}</div><div class="zw c2">{body}</div></div>{foot(src)}</section>')
    return (f'<section class="slide z ex{" yt" if yt else ""} k-{kind} {cls}">'
            f'<div class="bar{" ytb" if yt else ""}"><span class="tag">{tag}</span><h1>{title}</h1><span class="sub zpill">{pill}</span></div>'
            f'<div class="top"><div class="q">{q}{mk}</div><div class="zside">{side}</div></div>'
            f'<div class="zb" style="{grid}">{figh}<div class="zw">{body}</div></div>{foot(src)}</section>')

def nl_slide(title, lead, body, src, cls=''):
    return (f'<section class="slide z nl {cls}">{bar("New learning", title)}'
            f'<p class="lead zlead">{lead}</p>{body}{foot(src)}</section>')

OPTDIST = {}
KI_MED = r'Median position $= \dfrac{n + 1}{2}$th value<div class="kn">n even: average the two middle values</div>'
KI_MEDH = r'Median position $= \dfrac{n + 1}{2}$th value<div class="kn">histogram: add the frequencies until you pass that position</div>'
KI_RANGE = r'$\text{range} = \text{largest} - \text{smallest}$'
KI_IQR = r'$\text{IQR} = Q_3 - Q_1$<div class="kn">$Q_1$ = median of the lower half, $Q_3$ = median of the upper half (n odd: leave the median out)</div>'
KI_MEAN = r'$\bar{x} = \dfrac{\Sigma x}{n}$<div class="kn">add the values, divide by how many</div>'
KI_CAS = r'One-Variable Statistics gives $\bar{x}$, $s_x$, $n$ and the five-number summary.<div class="kn">Use $s_x$, not $\sigma_x$. Check $n$.</div>'

def tilerow(lab, t, d):
    return f'<div class="ztr"><span class="lab">{lab}</span>{tiles(t, d)}</div>' if lab else tiles(t, d)

def five(id_, vals):
    hd = ''.join(f'<th>{h}</th>' for h in ['min', '$Q_1$', '$M$', '$Q_3$', 'max'])
    return f'<table class="z5 zfill" id="{id_}"><tr>{hd}</tr><tr>' + ''.join(f'<td data-k="{k}">{v}</td>' for k, v in enumerate(vals)) + '</tr></table>'

# ---------------- slides ----------------
# S2 = 1C-1E (planner card gm12-u3-s2). Content and verbatim questions from the old deck tools/deck/s2/build.py
# (sources checked against the PDFs on G: 15 Nov 2026). Ledger: every APK/exit item is burnt by S2 only.
#   APK: Cambridge U1&2 Ch 2 skills checklist 2C #6, 2D #7, 2D #9; Ch 9 checklist 9D #6, #7;
#        Edrolo U1&2 1C Q17 (adapted from VCAA 2016 Exam 2 Q1d, report: 52%), 1C Q15 (adapted from VCAA 2017 Exam 2 Q2b, report: 87%).
#   Examples: Cambridge U3&4 Examples 6-13. You trys: Edrolo U3&4 1C WE4, WE5, WE1, WE2; 1D WE1, WE3 (none for Examples 6 and 9).
#   CAS: planner/cas-skills.json histogram, dotplot (TI-Nspire only), logs.
#   Exits: Edrolo U3&4 1C Q16 = VCAA 2020 Exam 2 Q2a (93%), 1C Q18 = VCAA 2016 Exam 1 Q3 (87/9/1/2/1),
#          1D Q13 = VCAA 2019 Exam 1 Q3 (7/6/7/71/9). Original VCAA wording.
import math
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CG12 = 'Cambridge General Mathematics Units 1&amp;2'
ED12 = 'Edrolo General Mathematics Units 1&amp;2'
CASJ = {x['id']: x for x in json.load(open(os.path.join(ROOT, 'planner', 'cas-skills.json')))['skills']}

def J2(xs): return ','.join(str(x) for x in xs)
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
def casbox(cid, ti_note=None):
    c = CASJ[cid]
    cp = c['classpad'] or ['ClassPad cannot make dot plots: draw them by hand.']
    return ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in c["ti"])}</ol></div>'
            '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in cp)}</ol></div></div>')

KI_PCT = r'$\text{percentage frequency} = \dfrac{\text{count}}{\text{total}} \times 100\%$'
KI_INT = 'Intervals: no gaps, no overlaps, about 5 to 15 of them, starting at an exact value.'
KI_HIST = 'Bars <b>touch</b>. Each bar is one interval; its height is the frequency.'
KI_SOCS = '<b>SOCS</b>: Shape · Outliers · Centre · Spread, one sentence each.'
KI_DOT = 'One dot per value on a scaled, labelled number line. Equal values <b>stack</b>.'
KI_STEM = 'Stem = leading digits, leaf = last digit. Order the leaves. <b>Always a key.</b>'
KI_MODE = 'Mode = the value that occurs most often (the tallest stack, the most repeated leaf).'
KI_LOG = r'$\log_{10} x = b \iff 10^{b} = x$<div class="kn">undo a log: $x = 10^{\text{log}}$</div>'
KI_LOGH = r'A value $v$ on a $\log_{10}$ scale stands for the number $10^{v}$.'

# ---- title + lesson overview
S.append(f'<section class="slide title cover"><h1>Displaying and describing numerical data</h1>'
         f'<div class="unit">12MAG · Unit 3 · AOS 1 Data analysis</div>'
         f'<div class="pp" style="font-size:22px;margin-top:14px">{CG}</div>'
         f'<ul style="list-style:none;padding:0;margin:10px 0 0;font-size:22px;line-height:1.5;text-align:left"><li>1C Displaying and describing numerical data (pp. 14–27)</li><li>1D Dot plots and stem plots (pp. 28–33)</li><li>1E Using a logarithmic (base 10) scale to display data (pp. 34–40)</li></ul><span class="pg" style="display:none"></span></section>')
LI = ['To be able to construct frequency tables for discrete numerical data.', 'To be able to construct frequency tables for grouped numerical data (discrete and continuous).',
      'To be able to construct a histogram from a frequency table for numerical data.', 'To be able to construct a histogram from numerical data using a CAS calculator.',
      'To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.',
      'To be able to construct a dot plot for numerical data.', 'To be able to construct a stem plot for numerical data.',
      'To be able to revise the concept of log<sub>10</sub> <i>x</i>.', 'To be able to investigate the effect of the logarithmic scale on the features of a distribution.']
SC = ['I can construct a frequency table for discrete numerical data.', 'I can construct a grouped frequency table.', 'I can construct a histogram from a grouped frequency table.',
      'I can describe the features of a distribution from a histogram.', 'I can construct a dot plot.', 'I can construct a stem plot.',
      'I can use a CAS calculator to find logs.', 'I can interpret a histogram with a log scale.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Frequency tables · Examples 6–7', 'Histograms · Example 8 · CAS',
       'Shape and SOCS · Example 9', 'Dot plots · Example 10 · CAS', 'Stem plots · Example 11', 'Logs · Example 12 · CAS',
       'Log scales · Example 13', 'Exit tasks', 'Check-in and coursework']
S.append(f'<section class="slide z li s2li">{bar("1C–1E", "Learning intentions")}<div class="cols" style="grid-template-columns:1.15fr 1fr .8fr">'
         f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
         f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
         f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
         f'{foot(CG + ", 1C, 1D, 1E Learning intentions; success criteria: one per worked example")}</section>')

# ---- APK 1: Cambridge U1&2 2C #6 + 2D #7 (AFL games)
AFL = [266, 259, 238, 227, 210, 160, 160, 159, 155, 145, 133, 99, 91, 80, 80, 75, 73, 58, 42, 36, 32, 25, 32, 25, 25, 21, 17, 13, 10, 9, 9, 4, 2]
AV = [sum(1 for v in AFL if 20 * b <= v < 20 * b + 20) for b in range(14)]
nz = [i for i, f in enumerate(AV) if f]
S.append(qslide('apk', '1 of 5', 'Year 11 skills: histogram and shape', 'Cambridge U1&amp;2 · 2C #6, 2D #7',
    'The following data gives the number of games played in total by each member of an AFL club:' + dlist('afl', AFL, 11, 'ztab zdl2 zsm3'),
    KI_HIST, [], None,
    CG12 + ', Chapter 2 skills checklist 2C #6 and 2D #7. Working by teacher.',
    parts=[('a', 'Use a CAS calculator to construct a histogram starting at 0 with column width 20.',
            [('CAS: Histogram, column width 20, start 0. Copy the bars.', bars('afh', nz))], 'Histogram (left): width 20, starting at 0.', bars('afh', nz)),
           ('b', 'Describe the shape of the histogram of the number of games played (above).',
            [('Most players have under 100 games; a long tail runs out to the right.', bars('afh', nz) + ' hq:afh:0,1')],
            'The distribution is <b>positively skewed</b>.', bars('afh', nz) + ' hq:afh:0,1')],
    fig=hist('afh', 0, 20, AV, 8, 2, 'number of games played', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1fr', cls='tight'))

# ---- APK 2: Cambridge U1&2 2D #9 (party ages, stem plot)
PA = [19, 21, 22, 56, 34, 19, 27, 28, 34, 17, 66, 37, 20, 20, 21, 45, 26, 19, 23, 29]
prow, pmp = stemmap(PA, range(1, 7), True)
pst = lambda test: J2(sorted(pmp[i] for i in where(PA, test)))
S.append(qslide('apk', '2 of 5', 'Year 11 skills: a stem plot', 'Cambridge U1&amp;2 · 2D #9',
    'Construct a stem plot of the ages of a group of people at a party:' + dlist('pa', PA, 10),
    KI_STEM,
    ['Ages run from 17 to 66: the tens digits 1 to 6 are the stems.',
     ('Teens: leaves 7, 9, 9, 9', f'tc:pa:{dk(10, where(PA, lambda v: v < 20))} xl:pas:{pst(lambda v: v < 20)}'),
     ('Twenties: leaves 0 0 1 1 2 3 6 7 8 9', f'tc:pa:{dk(10, where(PA, lambda v: v < 30))} xl:pas:{pst(lambda v: v < 30)}'),
     ('Thirties to sixties: 4 4 7 · 5 · 6 · 6', f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)}'),
     ('Write the key: 1 | 7 = 17, <i>age</i> (years)', f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)} sk:pas')],
    'Ordered stem plot (left) with the key <b>1 | 7 = 17</b>.',
    CG12 + ', Chapter 2 skills checklist 2D #9. Working by teacher.',
    fig=stem('pas', prow, 'Key: 1 | 7 = 17 &nbsp; <i>age</i> (years)', build=True).replace('class="zstem"', 'class="zstem zbuild"'), figw='.9fr',
    ans_do=f'tc:pa:{dk(10, range(20))} xl:pas:{pst(lambda v: True)} sk:pas', cls=''))

# ---- APK 3: Cambridge U1&2 9D #6, #7 (logs)
S.append(qslide('apk', '3 of 5', 'Year 11 skills: logs and powers of ten', 'Cambridge U1&amp;2 · 9D #6, #7',
    'Answer each part.', KI_LOG, [], None, CG12 + ', Chapter 9 skills checklist 9D #6 and #7. Working by teacher.',
    parts=[('a', 'Find the log of 592 to two decimal places.', [r'CAS: $\log_{10}(592) = 2.7723\ldots$'], r'$\boldsymbol{2.77}$'),
           ('b', 'What is the order of magnitude of 478 000?', [r'$478\,000 = 4.78 \times 10^{5}$'], 'order of magnitude <b>5</b>')]))

# ---- APK 4: Edrolo U1&2 1C Q17 (adapted from VCAA 2016 E2 Q1d)
GL = [0] * 16 + [0.3, 0.6, 1.2, 1.6, 1.6, 2.2, 2.6, 3.2, 6.4, 7.2, 7.8, 12.4, 16.8, 17.8]
GB = [sum(1 for v in GL if 2 * b <= v < 2 * b + 2) for b in range(9)]
GO = 'xb:goh:0'
S.append(qslide('apk', '4 of 5', 'A real VCAA question you can already do', 'VCAA 2016 Exam 2 Q1d (adapted)',
    'The following dot plot shows the average number of goals scored per season by each player within a soccer club.<br>'
    'Use the grid to construct a histogram that displays the distribution of the average number of goals scored per season at the soccer club. Use interval widths of two with the first interval starting at 0.',
    KI_HIST,
    [('0 to &lt;2: <b>21</b> (16 at 0, 5 more)', f'xb:goh:0'),
     ('2 to &lt;4: <b>3</b> · 4 to &lt;6: <b>0</b> · 6 to &lt;8: <b>3</b>', f'xb:goh:0,1,3'),
     ('12 to &lt;14: <b>1</b> · 16 to &lt;18: <b>2</b> · total 30 ✓', f'xb:goh:0,1,3,6,8')],
    'Histogram (left, lower): frequencies 21, 3, 0, 3, 0, 0, 1, 0, 2.',
    ED12 + ', 1C Q17 (adapted from VCAA 2016 Exam 2 Data analysis Q1d; % from the examiner report, original question). Working by teacher.',
    fig=f'<svg class="zdp" id="gd" data-v="{json.dumps(GL)}" data-lo="0" data-hi="19" data-xl="average goals scored" viewBox="0 0 640 262"></svg>'
        + hist('goh', 0, 2, GB, 22, 2, 'average goals scored', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'),
    marks=2, vcaa=52, figw='1.6fr', ans_do=f'xb:goh:0,1,3,6,8',
    watch='widths of <b>two</b> from 0: the examiners reported many students drew widths of one.'))

# ---- APK 5: Edrolo U1&2 1C Q15 (adapted from VCAA 2017 E2 Q2b)
MR = [('1', '8'), ('2', '2 2 4 4 4'), ('2', '5 5 9'), ('3', '0 0 1 2 3 4'), ('3', '6 8'), ('4', '0 3')]
S.append(qslide('apk', '5 of 5', 'And another', 'VCAA 2017 Exam 2 Q2b (adapted)',
    'The following stem plot displays the <i>wingspan</i>, in millimetres, of 19 moths that were captured.<br>Write down the modal <i>wingspan</i>, in millimetres, of the moths captured.',
    KI_MODE,
    [('Leaf 4 appears three times on the first 2 stem. No other value appears more than twice.', 'lx:mo:3,4,5'), ('Key: 2 | 4 = 24 mm', 'lx:mo:3,4,5')],
    'The modal wingspan is <b>24 mm</b>.',
    ED12 + ', 1C Q15 (adapted from VCAA 2017 Exam 2 Data analysis Q2b; % from the examiner report, original question). Working by teacher.',
    fig=stem('mo', MR, 'Key: 1 | 2 = 12 &nbsp; <i>wingspan</i> (mm)'), marks=1, vcaa=87, figw='1fr', ans_do='lx:mo:3,4,5',
    watch='the mode is the <b>value</b> (24 mm), not how many times it occurs (3). <span class="zsc">(teacher note)</span>'))

# ---- Key ideas
KD = [('Histogram', 'columns that touch; each column is an interval, its height the frequency'),
      ('Dot plot', 'a number line with a dot for each value; equal values stack'),
      ('Stem plot', 'each value split into a stem (leading digits) and a leaf (last digit), with a key'),
      ('Shape', 'symmetric, positively skewed (long upper tail) or negatively skewed (long lower tail)'),
      ('Outlier', 'a value that stands out from the rest of the data'),
      ('Log scale', 'an axis in powers of 10, for data ranging over several orders of magnitude')]
KF = [('Percentage frequency', r'$\dfrac{\text{count}}{\text{total}} \times 100\%$ &nbsp;<span class="zn">count = number of values in the interval</span>'),
      ('Log of a number', r'$\log_{10} x = b \iff 10^{b} = x$ &nbsp;<span class="zn">$\log_{10} 100 = 2$, since $10^2 = 100$</span>'),
      ('Number from its log', r'$\text{number} = 10^{\text{log}}$ &nbsp;<span class="zn">log 3.4 → $10^{3.4}$</span>'),
      ('Describe: SOCS', 'Shape · Outliers · Centre · Spread')]
S.append(f'<section class="slide z kif">{bar("1C–1E", "Key ideas")}<div class="cols" style="grid-template-columns:1.1fr .9fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1C pp. 14–23, 1D pp. 28–31, 1E pp. 34–36")}</section>')

# ---- NL: grouped frequency table (27 marks, Cambridge 1C CAS 1 data)
MK = [16, 11, 4, 25, 15, 7, 14, 13, 14, 12, 15, 13, 16, 14, 15, 12, 18, 22, 17, 18, 23, 15, 13, 17, 18, 22, 23]
MI = ['2–5', '6–9', '10–13', '14–17', '18–21', '22–25']; MN = [sum(1 for v in MK if 2 + 4 * b <= v <= 5 + 4 * b) for b in range(6)]
def mstep(b, tid, extra=''):
    ix = where(MK, lambda v: 2 <= v <= 5 + 4 * b)
    return f'tc:mk{tid}:{dk(9, ix)} ' + fills('mt' + tid, [k for r in range(b + 1) for k in rowk(r, 2)]) + extra
S.append(nl_slide('Grouped frequency tables',
    'Many different values, or continuous data? Group them into <b>intervals</b>. <span class="hint">Click to count the 27 marks into the table.</span>',
    '<div class="cols" style="grid-template-columns:1fr .75fr 1fr"><div class="col"><h2>Data: “the following set of 27 marks” (Cambridge 1C CAS 1)</h2>' + dlist('mk1', MK, 9) +
    '<ul class="zul s2rules"><li>every value in exactly one interval: no gaps, no overlaps</li><li>about 5 to 15 intervals</li><li>start on an exact value</li><li><b>2–5</b> (whole marks) = 2, 3, 4 or 5 · <b>30.0–34.9</b> = 30.0 up to 34.9</li></ul></div>'
    '<div class="col">' + ftab('mt1', ['<i>marks</i>', 'Frequency'], [(a, f) for a, f in zip(MI, MN)] + [('<b>Total</b>', '<b>27</b>')]) + '</div><div class="col">'
    + st('<b>1</b> Width 4, starting at 2: 2–5, 6–9, …, 22–25', do=fills('mt1', [r * 10 for r in range(6)]))
    + st('<b>2</b> 2–5: <b>1</b> · 6–9: <b>1</b> · 10–13: <b>6</b>', do=mstep(2, '1'))
    + st('<b>3</b> 14–17: <b>11</b> · 18–21: <b>3</b> · 22–25: <b>5</b>', do=mstep(5, '1'))
    + st('<b>4</b> Total: 1 + 1 + 6 + 11 + 3 + 5 = <b>27</b> ✓', do=mstep(5, '1', ' ' + fills('mt1', rowk(6, 2))))
    + '</div></div>', CG + ', 1C pp. 14–16 (27 marks: CAS 1, p. 16)'))

# ---- Example 6 (Cambridge)
BED = [2, 3, 4, 3, 3, 4, 3, 4, 4, 1, 3, 2, 1, 2, 2, 2, 4, 5, 3, 4, 4, 5, 3, 4]
bc = [BED.count(v) for v in range(1, 6)]; bp = [f'{100 * c / 24:.1f}' for c in bc]
B6 = [(str(v), bc[v - 1], bp[v - 1]) for v in range(1, 6)] + [('<b>Total</b>', '<b>24</b>', '<b>99.9</b>')]
F6a = fills('t6', [r * 10 for r in range(6)])
F6b = F6a + ' ' + fills('t6', [r * 10 + 1 for r in range(6)])
S.append(qslide('ex', 6, 'Constructing a frequency table for discrete numerical data', 'Cambridge · Example 6',
    'The number of bedrooms in each of the 24 properties sold in a certain area over a one month period are as follows:' + dlist('bd', BED, 12) +
    'Construct a table for these data showing both frequency and percentage frequency, giving the values of the percentage frequency rounded to one decimal place.',
    KI_PCT,
    [('Smallest 1, largest 5: one row for each of 1, 2, 3, 4, 5.', F6a),
     ('Count each value: 2, 5, 7, 8, 2 · total 24', F6b + f' tc:bd:{dk(12, range(24))}'),
     (r'Percentage for 1 bedroom: $\dfrac{2}{24} \times 100\% = 8.3\%$', F6b + ' fill:t6:2'),
     ('The rest: 20.8, 29.2, 33.3, 8.3 · total 99.9 (rounding)', F6b + ' ' + fills('t6', [r * 10 + 2 for r in range(6)]))],
    'The frequency table (left).', CG + ', 1C Example 6 (p. 14)',
    fig=ftab('t6', ['Number of bedrooms', 'Number', '%'], B6), figw='1fr', cls='tight',
    ans_do=F6b + ' ' + fills('t6', [r * 10 + 2 for r in range(6)])))

# ---- Example 7 (Cambridge)
HRS = [35.0, 48.0, 45.0, 43.0, 38.2, 50.0, 39.8, 40.7, 40.0, 50.0, 35.4, 38.8, 40.2, 45.0, 45.0, 40.0, 43.0, 48.8, 43.3, 53.1, 35.6, 44.1, 34.8]
HI = ['30.0–34.9', '35.0–39.9', '40.0–44.9', '45.0–49.9', '50.0–54.9']; hk = lambda v: int((v - 30) // 5)
HN = [sum(1 for v in HRS if hk(v) == b) for b in range(5)]; HP = [f'{100 * n / 23:.1f}' for n in HN]
F7a = fills('t7', [r * 10 for r in range(6)])
F7b = F7a + ' ' + fills('t7', [r * 10 + 1 for r in range(6)])
S.append(qslide('ex', 7, 'Constructing a grouped frequency table', 'Cambridge · Example 7',
    'The data below give the average hours worked per week in 23 countries.' + dlist('hr', [f'{v:.1f}' for v in HRS], 8) + 'Construct a grouped frequency table with five intervals.',
    KI_INT,
    [('Smallest 34.8, largest 53.1: five intervals of width 5, from 30.0–34.9 to 50.0–54.9', F7a),
     ('Count 30.0–34.9 and 35.0–39.9: 1 · 6', F7a + ' ' + fills('t7', [1, 11]) + f' tc:hr:{dk(8, where(HRS, lambda v: hk(v) <= 1))}'),
     ('Count the rest: 8 · 5 · 3 · total 23', F7b + f' tc:hr:{dk(8, range(23))}'),
     (r'Percentages: $\dfrac{1}{23} \times 100\% = 4.3\%$, then 26.1, 34.8, 21.7, 13.0', F7b + ' ' + fills('t7', [r * 10 + 2 for r in range(6)]))],
    'The grouped frequency table (left).', CG + ', 1C Example 7 (p. 15)',
    fig=ftab('t7', ['Average hours worked', 'Number', '%'], [(a, n, p) for a, n, p in zip(HI, HN, HP)] + [('<b>Total</b>', '<b>23</b>', '<b>99.9</b>')]), figw='.9fr',
    ans_do=F7b + ' ' + fills('t7', [r * 10 + 2 for r in range(6)])))

# ---- You try 7: Edrolo 1C WE4
PL = [32.0, 40.2, 40.5, 45.1, 47.0, 49.1, 50.1, 53.7, 54.2, 55.3, 56.9, 57.2, 58.2, 67.2, 68.9, 69.0, 72.3, 77.6, 82.1, 88.5]
PI = ['30.0–39.9', '40.0–49.9', '50.0–59.9', '60.0–69.9', '70.0–79.9', '80.0–89.9']; pk = lambda v: int((v - 30) // 10)
PN = [sum(1 for v in PL if pk(v) == b) for b in range(6)]; PP = [str(5 * n) for n in PN]
FYa = fills('ty7', [r * 10 for r in range(7)]); FYb = FYa + ' ' + fills('ty7', [r * 10 + 1 for r in range(7)])
S.append(qslide('yt', 7, 'Constructing a grouped frequency table', 'Edrolo 1C WE4',
    'The <i>height</i> (cm) of 20 plants in a Year 6 science experiment were recorded.' + dlist('pl', [f'{v:.1f}' for v in PL], 7) + 'Construct a grouped frequency table with intervals of 10.',
    KI_INT,
    [('Smallest 32.0 → start at 30.0 · largest 88.5 → last interval 80.0–89.9: six intervals', FYa),
     ('Count: 1 · 5 · 7 · 3 · 2 · 2 · total 20', FYb + f' tc:pl:{dk(7, range(20))}'),
     (r'Percentages: $\dfrac{1}{20} \times 100\% = 5\%$, then 25, 35, 15, 10, 10', FYb + ' ' + fills('ty7', [r * 10 + 2 for r in range(7)]))],
    'The grouped frequency table (left).', ED + ', 1C Worked example 4 (intervals written Cambridge style). Working by teacher.',
    fig=ftab('ty7', ['<i>height</i> (cm)', 'number', '%'], [(a, n, p) for a, n, p in zip(PI, PN, PP)] + [('<b>total</b>', '<b>20</b>', '<b>100</b>')]), figw='.9fr',
    ans_do=FYb + ' ' + fills('ty7', [r * 10 + 2 for r in range(7)])))

# ---- NL: the histogram (same 27 marks)
S.append(nl_slide('The histogram: table → graph',
    'A <b>histogram</b> shows a grouped frequency table. The bars <b>touch</b> because the scale is continuous. <span class="hint">Click to grow the bars.</span>',
    '<div class="cols" style="grid-template-columns:.68fr 1.1fr 1.15fr"><div class="col">' + ftab('mt2', ['<i>marks</i>', 'Frequency'], [(a, f) for a, f in zip(MI, MN)] + [('<b>Total</b>', '<b>27</b>')]).replace('zft zfill', 'zft ztab') +
    '</div><div class="col">' + hist('mh2', 2, 4, MN, 12, 2, 'marks', 'frequency').replace('class="zhg"', 'class="zhg zbuild"') + '</div><div class="col">'
    + st('<b>1</b> Axes: <i>marks</i> across (2, 6, 10, …); frequency up, to 12.')
    + ''.join(st(f'<b>{i + 2}</b> {MI[i]}: frequency {MN[i]} → bar from {2 + 4 * i} to {6 + 4 * i}, height {MN[i]}', do=f'xb:mh2:{J2(range(i + 1))} tc:mt2:{dk(10, [i * 10, i * 10 + 1])}'.replace(dk(10,[i*10,i*10+1]), f'{i*10},{i*10+1}')) for i in range(6))
    + st('<b>Check:</b> heights add to 27 ✓', True, do='xb:mh2:0,1,2,3,4,5')
    + '</div></div>', CG + ', 1C pp. 15–16 (27 marks: CAS 1, p. 16)', 's2hg'))

# ---- Example 8 (Cambridge)
HV = [1, 6, 8, 5, 3]
S.append(qslide('ex', 8, 'Constructing a histogram from a frequency table', 'Cambridge · Example 8',
    'Construct a histogram for the frequency table opposite.' + table_hl('t8', [('Average hours worked', HI), ('Frequency', [str(x) for x in HV])], 'ztab zinq'),
    KI_HIST,
    ['Axes: <i>Average hours worked</i> across (30, 35, …); <i>Frequency</i> up, to at least 8.',
     *[(f'{HI[i]}: frequency {HV[i]} → bar {30 + 5 * i} to {35 + 5 * i}, height {HV[i]}', f'xb:h8:{J2(range(i + 1))} tc:t8:{i},{100 + i}') for i in range(5)]],
    'The histogram (left): bars touch, both axes labelled.', CG + ', 1C Example 8 (p. 16)',
    fig=hist('h8', 30, 5, HV, 9, 1, 'Average hours worked', 'Frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1.1fr',
    ans_do='xb:h8:0,1,2,3,4'))

# ---- You try 8: Edrolo 1C WE5 (a and b on two slides, as Example 13)
YT8Q = ('The <i>height</i> (cm) of 20 plants in a Year 6 science experiment was recorded in the following grouped frequency table.'
    + table_hl('ty8', [('<i>height</i> (cm)', PI), ('number', [str(x) for x in PN]), ('%', PP)], 'ztab zinq zsm2'))
S.append(qslide('yt', '8 (a)', 'Constructing a histogram from a frequency table', 'Edrolo 1C WE5',
    YT8Q, KI_HIST, [], None, ED + ', 1C Worked example 5 a (intervals written Cambridge style). Working by teacher.',
    parts=[('a.', 'Construct a histogram to display this data.',
            [(f'{PI[i]}: {PN[i]} → bar {30 + 10 * i} to {40 + 10 * i}, height {PN[i]}', f'xb:yh8:{J2(range(i + 1))} tc:ty8:{i},{100 + i}') for i in range(6)],
            'Histogram (left).', 'xb:yh8:0,1,2,3,4,5')],
    fig=hist('yh8', 30, 10, PN, 8, 1, 'height (cm)', 'frequency').replace('class="zhg"', 'class="zhg zbuild"'), figw='1.1fr', cls='tight'))
S.append(qslide('yt', '8 (b)', 'Constructing a histogram from a frequency table', 'Edrolo 1C WE5',
    YT8Q.replace("'ty8'", "'ty8b'").replace('id="ty8"', 'id="ty8b"'), KI_HIST, [], None, ED + ', 1C Worked example 5 b. Working by teacher.',
    parts=[('b.', 'What percentage of plants were shorter than 60 cm?',
            [('Shorter than 60 cm: the first three intervals.', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2'),
             ('Add their percentages: 5 + 25 + 35', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2,200,201,202')],
            '<b>65%</b> of plants were shorter than 60 cm.', 'hq:yh8b:0,1,2 tc:ty8b:0,1,2,200,201,202')],
    fig=hist('yh8b', 30, 10, PN, 8, 1, 'height (cm)', 'frequency'), figw='1.1fr', cls='tight'))

# ---- CAS: histogram (Cambridge 1C CAS 1, 27 marks)
S.append(qslide('cas', '', 'Constructing a histogram from raw data', 'Cambridge · 1C CAS 1',
    'Display the following set of 27 marks in the form of a histogram.' + dlist('mk3', MK, 14, 'ztab zdl2 zsm3') +
    'Enter the data into a list named <b>marks</b>, then change the column (bin) width to <b>4</b> and the starting point to <b>2</b>.',
    'Set the <b>width</b> and the <b>start</b> yourself: the calculator’s default bins are rarely the ones asked for.',
    ['Enter the 27 marks in a list named <i>marks</i>.', 'Draw the histogram, then set width 4, start 2.',
     'Read each bar (hover or trace): 1, 1, 6, 11, 3, 5'],
    'Same histogram as the table → graph slide: 2–5 has 1, …, 14–17 has 11, 22–25 has 5.', CG + ', 1C pp. 16–20 (CAS 1). CAS steps: planner CAS guide.',
    fig=casbox('histogram'), figw='1.15fr', cls='s2cas'))

# ---- NL: shape
def mini(id_, v, ym=10):
    return hist(id_, 0, 1, v, ym, 5, '', '').replace('class="zhg"', 'class="zhg zmini"')
SHP = [('Symmetric', 'tails off evenly on either side of the peak', [1, 2, 4, 7, 9, 7, 4, 2, 1]),
       ('Positively skewed', 'long <b>upper</b> tail, to the right', [3, 9, 8, 6, 4, 3, 2, 1, 1]),
       ('Negatively skewed', 'long <b>lower</b> tail, to the left', [1, 1, 2, 3, 4, 6, 8, 9, 3]),
       ('With an outlier', 'a value well away from the rest', [0, 3, 7, 9, 6, 2, 0, 0, 1])]
MM = ['mean ≈ median', '<b>mean &gt; median</b> (the tail pulls the mean up)', '<b>mean &lt; median</b>', 'the mean is pulled towards the outlier, and the median barely moves']
S.append(nl_slide('Shape: which way is the tail?',
    'Look at the <b>tail</b>: it names the skew. <span class="hint">Click to reveal each shape.</span>',
    '<div class="s2shp">' + ''.join(f'<div class="zpc">' + st(f'<div class="zpt">{a}</div>' + mini(f'shp{k}', v) + f'<div class="s2c">{b}</div><div style="font-size:24px;line-height:1.25;margin-top:10px;padding-top:8px;border-top:2px dotted #999">{MM[k]}</div>') + '</div>' for k, (a, b, v) in enumerate(SHP)) + '</div>'
    + st('Salaries and house prices are usually positively skewed. Age at death is negatively skewed.', True, cls='zctr'),
    CG + ', 1C p. 21 (shapes and mean/median notes by the teacher)'))

# ---- NL: SOCS
SOCSL = [('S', 'Shape', 'The distribution is symmetric / positively skewed / negatively skewed.'),
         ('O', 'Outliers', 'There are no outliers / is an outlier at … / are outliers at …'),
         ('C', 'Centre', 'The distribution is centred at <i>value</i>, the median / mean / mode.'),
         ('S', 'Spread', 'The range / IQR is <i>value</i>. Most values lie between <i>a</i> and <i>b</i>.')]
S.append(nl_slide('Describing a distribution: SOCS, like a sock',
    'Describe numerical data in this order, one sentence for each letter. <span class="hint">Click for each line.</span>',
    '<div class="s2socs">' + ''.join(st(f'<span class="s2L">{l}</span><b>{n}</b> &nbsp; {t}') for l, n, t in SOCSL) + '</div>'
    + st('Skewed, or outliers? Give the <b>median</b> and the <b>IQR</b>: outliers don’t affect them. From a histogram, the centre and spread are only estimates.', True, cls='zctr'),
    CG + ', 1C pp. 21–23 (SOCS order: class convention)'))

# ---- Example 9 (Cambridge)
GV = [2, 2, 2, 2, 2, 2, 2, 4, 6, 10, 16, 34, 95, 233, 300, 207, 86, 4]
S.append(qslide('ex', 9, 'Describing the features of a distribution from a histogram', 'Cambridge · Example 9',
    'The histogram shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe this histogram in terms of shape, centre, spread and outliers.',
    KI_SOCS,
    ['<div class="zpart s2tpl" id="tp9"><span class="zok">✓ Answer</span> The distribution is <span class="s2b" data-b="0">negatively</span> skewed. There are <span class="s2b" data-b="1">possible outliers below 34 weeks</span>. It is centred at around <span class="s2b" data-b="2">38–39 weeks</span>, the median. The values range from <span class="s2b" data-b="3">25</span> to <span class="s2b" data-b="3">42</span> weeks; most lie between <span class="s2b" data-b="3">36</span> and <span class="s2b" data-b="3">41</span> weeks.</div>',
     ('<b>S</b> The bars tail off to the left: a long lower tail.', 'bf:tp9:0 hq:h9:0,1,2,3,4,5,6,7,8,9,10'),
     ('<b>O</b> Bars below 34 weeks are tiny next to the rest.', 'bf:tp9:0,1 hq:h9:0,1,2,3,4,5,6,7,8'),
     ('<b>C</b> The middle (500th baby) falls in 38–39 weeks.', 'bf:tp9:0-2 hm:h9:13,14'),
     ('<b>S</b> Lowest bar 25, highest 42; the tall bars 36 to 41.', 'bf:tp9:0-3 hq:h9:11,12,13,14,15,16')],
    '', 
    CG + ', 1C Example 9 (pp. 23–24); Cambridge’s solution set out in SOCS order; histogram redrawn',
    fig=hist('h9', 25, 1, GV, 300, 50, 'Gestation period (weeks)', 'Frequency'), figw='1.15fr', cls='tight', ans_do='bf:tp9:0-3 hq:h9:11,12,13,14,15,16 bok:tp9').replace('<span class="zok">✓ Answer</span> </div>', '</div>').replace('class="st zs final "', 'class="st zs final s2hid"'))

# ---- NL: dot plots and stem plots
DPV = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7]
S.append(nl_slide('Dot plots and stem plots',
    'Two quick, by-hand displays for small data sets. Both show <b>every</b> data value. <span class="hint">Click for each display.</span>',
    '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>Dot plot</h2>'
    + f'<svg class="zdp zbuild" id="nld" data-v="{json.dumps(sorted(DPV))}" data-lo="1" data-hi="8" data-xl="board games owned" viewBox="0 0 640 262"></svg>'
    + st('A number line with one dot per value. Equal values <b>stack</b>. Best for small, discrete data sets.', do='xd:nld:0-10') + '</div>'
    '<div class="col"><h2>Stem plot</h2>' + stem('nls', [('4', '3 5 5 5 7'), ('5', '1 3 6 8'), ('6', '7 9'), ('7', '1'), ('8', '0 1 3 9 9'), ('9', '1 4')], 'Key: 4 | 3 = 43', build=True).replace('class="zstem"', 'class="zstem zbuild"')
    + st('Stem = leading digits, leaf = last digit. Leaves in order, empty stems kept.', do='xl:nls:0-18') + st('<b>Always a key</b>: 4 | 3 = 43.', do='xl:nls:0-18 sk:nls') + '</div></div>',
    CG + ', 1D pp. 28–31 · ' + ED + ', 1C (example plots)'))

# ---- Example 10 (Cambridge)
CR = [22, 19, 18, 19, 23, 25, 22, 29, 18, 22, 23, 24, 22]
S.append(qslide('ex', 10, 'Constructing a dot plot', 'Cambridge · Example 10',
    'The ages (in years) of the 13 members of a cricket team are:' + dlist('cr', CR, 13) + 'Construct a dot plot.',
    KI_DOT,
    ['Draw a number line scaled to include all values (17 to 30); label it <i>Age (years)</i>.',
     ('18 and 19: two dots each, stacked', f'xd:d10:{sk(CR, lambda v: v <= 19)} tc:cr:{dk(13, where(CR, lambda v: v <= 19))}'),
     ('22: four dots · 23: two dots', f'xd:d10:{sk(CR, lambda v: v <= 23)} tc:cr:{dk(13, where(CR, lambda v: v <= 23))}'),
     ('24, 25, 29: one dot each · check: 13 dots', f'xd:d10:{sk(CR, lambda v: True)} tc:cr:{dk(13, range(13))}')],
    'The dot plot (left).', CG + ', 1D Example 10 (p. 29)',
    fig=f'<svg class="zdp zbuild" id="d10" data-v="{json.dumps(sorted(CR))}" data-lo="17" data-hi="30" data-xl="Age (years)" viewBox="0 0 640 262"></svg>', figw='1.2fr',
    ans_do=f'xd:d10:{sk(CR, lambda v: True)} tc:cr:{dk(13, range(13))}'))

# ---- You try 10: Edrolo 1C WE1
PET = [3, 2, 0, 1, 1, 3, 0, 5, 2, 1, 1, 2]
ALLP = f'xd:y10:{sk(PET, lambda v: True)} tc:pt:{dk(12, range(12))}'
S.append(qslide('yt', 10, 'Constructing a dot plot', 'Edrolo 1C WE1',
    'Sophie surveyed 12 of the families living on her street. She asked for the number of pets each of them owned and the results were recorded.' + dlist('pt', PET, 12),
    KI_DOT, [], None, ED + ', 1C Worked example 1. Working by teacher.',
    parts=[('a.', 'Construct a dot plot to display this data.',
            ['Number line 0 to 5, labelled <i>number of pets</i>.',
             ('Dots: 0→2 · 1→4 · 2→3 · 3→2 · 5→1', ALLP)], 'Dot plot (left).', ALLP),
           ('b.', 'What was the modal number of pets owned by families that Sophie surveyed?',
            [('The tallest stack: 4 families own 1 pet.', ALLP + f' xm:y10:{sk(PET, lambda v: v == 1)}')], '<b>1 pet</b>', ALLP + f' xm:y10:{sk(PET, lambda v: v == 1)}')],
    fig=f'<svg class="zdp zbuild" id="y10" data-v="{json.dumps(sorted(PET))}" data-lo="0" data-hi="6" data-xl="number of pets" viewBox="0 0 640 262"></svg>', figw='1.1fr'))

# ---- CAS: dot plot (TI-Nspire only)
S.append(qslide('cas', '', 'Constructing a dot plot (TI-Nspire)', 'Data: Cambridge Example 10',
    'The ages (in years) of the 13 members of a cricket team are: 22 &nbsp;19 &nbsp;18 &nbsp;19 &nbsp;23 &nbsp;25 &nbsp;22 &nbsp;29 &nbsp;18 &nbsp;22 &nbsp;23 &nbsp;24 &nbsp;22<br>Enter the ages into a list named <b>age</b> and display them as a dot plot.',
    'Check the number of dots equals $n$. ClassPad has no dot plot: draw it by hand.',
    ['Enter the 13 ages in a list named <i>age</i>.', 'Data &amp; Statistics: add <i>age</i> on the x-axis.', ('A dot plot appears: 13 dots', f'xd:cd:{sk(CR, lambda v: True)}')],
    'Same dot plot as Example 10: 22 has four dots, the most of any age.', 'Data: ' + CG + ', 1D Example 10 (p. 29). CAS steps: planner CAS guide (TI-Nspire only).',
    fig=casbox('dotplot') + f'<svg class="zdp zbuild" id="cd" data-v="{json.dumps(sorted(CR))}" data-lo="17" data-hi="30" data-xl="age" viewBox="0 0 640 262"></svg>', figw='1.15fr', cls='s2cas',
    ans_do=f'xd:cd:{sk(CR, lambda v: True)}'))

# ---- Example 11 (Cambridge): unordered, then ordered
UR = [26, 3, 12, 20, 36, 1, 25, 26, 13, 9, 26, 27, 15, 21, 7, 8, 22, 3, 37, 17, 55, 30, 1]
urow, ump = stemmap(UR, range(6), False); orow, omp = stemmap(UR, range(6), True)
uk = lambda ix: J2(sorted(ump[i] for i in ix))
S.append(qslide('ex', 11, 'Constructing a stem plot', 'Cambridge · Example 11',
    'University participation rates (%) in 23 countries are given below.' + dlist('ur', UR, 12) + 'Display the data in the form of a stem plot.',
    KI_STEM,
    ['Values run from 1 to 55: stems 0 to 5 (units, tens, …, fifties).',
     ('First values, in the order given: 26 → stem 2, leaf 6 · 3 → stem 0, leaf 3 …', f'xl:u11:{uk(range(8))} tc:ur:{dk(12, range(8))}'),
     ('Every value gets a leaf on its stem; stem 4 stays empty.', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))}'),
     ('Order the leaves on each stem, smallest first.', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22'),
     ('Write the key and variable: 1 | 2 = 12, <i>rate</i> (%)', f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22 sk:o11')],
    'The ordered stem plot (right), key 1 | 2 = 12%.', CG + ', 1D Example 11 (p. 30)',
    fig='<div class="s2two"><div><div class="zsc">unordered</div>' + stem('u11', urow, '&nbsp;').replace('class="zstem"', 'class="zstem zbuild" data-max="30"').replace('<div class="zkey">&nbsp;</div>', '<div class="zkey" style="visibility:hidden">&nbsp;</div>')
        + '</div><div><div class="zsc">ordered</div>' + stem('o11', orow, 'Key: 1 | 2 = 12 &nbsp; <i>rate</i> (%)', build=True).replace('class="zstem"', 'class="zstem zbuild" data-max="30"') + '</div></div>',
    figw='1.15fr', ans_do=f'xl:u11:{uk(range(23))} tc:ur:{dk(12, range(23))} xl:o11:0-22 sk:o11'))

# ---- You try 11: Edrolo 1C WE2
EX = [55, 68, 76, 90, 83, 89, 75, 66, 59, 84, 48, 62, 58, 95, 80, 77, 61, 92, 99, 63, 84, 65, 70, 81, 96]
erow, emp = stemmap(EX, range(4, 10), True)
EALL = f'xl:y11:0-24 tc:ex:{dk(13, range(25))}'
above = J2(sorted(emp[i] for i in where(EX, lambda v: v > 70)))
S.append(qslide('yt', 11, 'Constructing a stem plot', 'Edrolo 1C WE2',
    'Ms Smyth’s maths class of 25 students sat their end-of-year exam. Their results (%) were recorded.' + dlist('ex', EX, 13),
    KI_STEM, [], None, ED + ', 1C Worked example 2. Working by teacher.',
    parts=[('a.', 'Construct a stem plot to display this data.',
            ['Values from 48 to 99: stems 4 to 9 (tens), leaves = ones.', ('Place each leaf, then order each stem.', EALL), ('Write the key: 4 | 8 = 48%', EALL + ' sk:y11')],
            'Ordered stem plot (left).', EALL + ' sk:y11'),
           ('b.', 'How many students scored above 70% on the exam?',
            [('Leaves 5, 6, 7 on stem 7, and stems 8 and 9: 3 + 6 + 5', EALL + f' sk:y11 lx:y11:{above}')],
            '<b>14 students</b>', EALL + f' sk:y11 lx:y11:{above}')],
    fig=stem('y11', erow, 'Key: 4 | 8 = 48%', build=True).replace('class="zstem"', 'class="zstem zbuild"'), figw='.95fr', cls='tight'))

# ---- NL: logs are powers of ten
S.append(nl_slide('Logs are just powers of 10',
    r'The log of a number is the power of 10 that makes it: $\log_{10} 1000 = 3$, since $10^3 = 1000$. <span class="hint">Click to fill the rows.</span>',
    '<table class="zft s2lt" id="lgt"><tr><th>number</th>' + ''.join(f'<td>{x}</td>' for x in ['0.01', '0.1', '1', '10', '100', '1000', '1 000 000']) + '</tr>'
    '<tr><th>power of 10</th>' + ''.join(f'<td class="s2h" data-k="1{c}">$10^{{{p}}}$</td>' for c, p in enumerate(['-2', '-1', '0', '1', '2', '3', '6'])) + '</tr>'
    '<tr><th>log</th>' + ''.join(f'<td class="s2h" data-k="2{c}"><b>{p}</b></td>' for c, p in enumerate(['−2', '−1', '0', '1', '2', '3', '6'])) + '</tr></table>'
    + st('Write each number as a power of 10.', do='xs:lgt:1')
    + st('The log is the power.', do='xs:lgt:1 xs:lgt:2')
    + st('Number above 1 → positive log · between 0 and 1 → negative log · 0 → no log. Each step of 1 on a log scale multiplies by 10.', True, do='xs:lgt:1 xs:lgt:2'),
    CG + ', 1E pp. 34–35'))

# ---- NL interactive: animal weights on a log scale (Cambridge 1E Example 13 context)
S.append(f'<section class="slide z nl logx">{bar("New learning", "Why a log scale? Animal body weights")}'
    '<div class="ctx">Animals range from a 0.02 kg mouse to a 2500 kg elephant. On an ordinary scale, almost every animal is squashed against 0. '
    'On a <b>log scale</b>, each step of 1 is ten times heavier. Drag the slider (or tap an animal) to move the white dot.</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>The same weight on two scales</h2>'
    '<svg class="zlg ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>log −2</span><input type="range" min="-200" max="400" step="1" value="52"><span>log 4</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-w="0.02">Mouse (0.02 kg)</button><button data-w="3.3">Cat (3.3 kg)</button><button data-w="70">Person (70 kg)</button><button data-w="2512">Elephant (log 3.4)</button><button data-w="10000">log 4</button></div></div>'
    '<div class="col"><h2>Live</h2><div class="zlgo"></div>'
    r'<div class="zrule">$\log_{10}(\text{weight}) = b \iff \text{weight} = 10^{b}$. A positively skewed set of weights often looks roughly symmetric on a log scale.</div></div></div>'
    f'{foot(CG + ", 1E pp. 34–38 (cat 3.3 kg, elephant log 3.4: Example 13). Mouse and person weights made up by the teacher.")}</section>')

# ---- Example 12 (Cambridge)
S.append(qslide('ex', 12, 'Using a CAS calculator to find logs', 'Cambridge · Example 12',
    'Answer each part.', KI_LOG, [], None, CG + ', 1E Example 12 (pp. 36–37)',
    parts=[('a', 'Find the log of 45, correct to two significant figures.', [r'CAS: $\log(45) = 1.653\ldots$', '2 significant figures: count from the first non-zero digit.'],
            r'$\log 45 = \boldsymbol{1.7}$'),
           ('b', 'Find the number with log equal to 2.7125, correct to the nearest whole number.', [r'Undo the log: the number is $10^{2.7125}$', r'CAS: $10^{2.7125} = 515.82\ldots$'],
            r'$\boldsymbol{516}$')]))

# ---- CAS: logs
S.append(qslide('cas', '', 'Finding a log, and undoing it', 'Cambridge · Example 12',
    'a Find the log of 45, correct to two significant figures.<br>b Find the number with log equal to 2.7125, correct to the nearest whole number.',
    'log( ) gives the power of 10. 10^ undoes it.',
    [r'Type log(45): $1.65321\ldots$', r'Type 10^2.7125: $515.822\ldots$', 'Round as each part asks.'],
    'a 1.7 &nbsp;·&nbsp; b 516', CG + ', 1E Example 12 (p. 37). CAS steps: planner CAS guide.',
    fig=casbox('logs'), figw='1fr', cls='s2cas'))

# ---- You try 12: Edrolo 1D WE1
S.append(qslide('yt', 12, 'Using a CAS calculator to find logs', 'Edrolo 1D WE1',
    'Use log<sub>10</sub> for the following calculations.', KI_LOG, [], None, ED + ', 1D Worked example 1. Working by teacher.',
    parts=[('a.', 'Calculate the log of 23, correct to two decimal places.', [r'CAS: $\log_{10}(23) = 1.3617\ldots$'], r'$\boldsymbol{1.36}$'),
           ('b.', 'If the log of a number is 5, what is the number?', [r'$\log_{10}(x) = 5$, so $x = 10^{5}$'], r'$\boldsymbol{100\,000}$')]))

# ---- Example 13 (Cambridge)
AW = [3.7, 7.4, 18.5, 25.9, 25.9, 11.1, 7.4]
H13 = lambda id_: hist(id_, -2, 1, AW, 28, 4, 'log(body weight)', 'Percentage')
S.append(qslide('ex', '13 (a, b)', 'Interpreting a histogram with a log scale', 'Cambridge · Example 13',
    'The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.', KI_LOGH, [], None,
    CG + ', 1E Example 13 a–b (pp. 37–38); histogram redrawn from the CAS 2 data (p. 38)',
    parts=[('a', 'What body weight (in kg) is represented by the number 4 on the log scale?', [r'4 on the log scale stands for $10^{4}$.'], r'$10^{4} = \boldsymbol{10\,000}$ kg'),
           ('b', 'How many of these animals have body weights more than 10 000 kg?', [('10 000 kg is 4 on the log scale. One bar above 4: 7.4% of 27 animals', 'hq:h13:6'), (r'$0.074 \times 27 = 1.998 \approx 2$', 'hq:h13:6')], '<b>Two animals</b>', 'hq:h13:6')],
    fig=H13('h13'), figw='1fr'))
S.append(qslide('ex', '13 (c, d)', 'Interpreting a histogram with a log scale', 'Cambridge · Example 13',
    'The histogram shows the distribution of the weights of 27 animal species plotted on a log scale.', KI_LOG, [], None,
    CG + ', 1E Example 13 c–d (pp. 37–38); histogram redrawn from the CAS 2 data (p. 38)',
    parts=[('c', 'The weight of a cat is 3.3 kg. Use your calculator to determine the log of its weight correct to two significant figures.', [r'CAS: $\log(3.3) = 0.5185\ldots$'], r'$\boldsymbol{0.52}$', 'hq:h13b:2'),
           ('d', 'Determine the weight (in kg) of the animal with a log(<i>body weight</i>) of 3.4 (the elephant). Write your answer correct to the nearest whole number.', [r'Undo the log: $10^{3.4} = 2511.88\ldots$'], r'$\boldsymbol{2512}$ kg', 'hq:h13b:2,5')],
    fig=H13('h13b'), figw='.9fr'))

# ---- You try 13: Edrolo 1D WE3
DV = [2, 3, 3, 5, 6, 1]
S.append(qslide('yt', 13, 'Interpreting a histogram with a log scale', 'Edrolo 1D WE3',
    'A class of twenty students were asked about the <i>distance</i>, in kilometres, from their home to the school. The results were summarised in a histogram using a log<sub>10</sub> scale.',
    KI_LOGH, [], None, ED + ', 1D Worked example 3. Working by teacher.',
    parts=[('a.', 'Jane was away the day of the survey. It is known that she lives 9.5 km away from school. Which interval on the histogram reflects this?',
            [(r'$\log_{10}(9.5) = 0.9777\ldots$: between 0.5 and 1.0', 'hm:yh13:3')], '<b>0.5 – &lt;1.0</b>', 'hm:yh13:3'),
           ('b.', 'How many students live more than 10 km away from school?',
            [(r'$\log_{10}(10) = 1$: add the columns above 1', 'hm:yh13:3 hq:yh13:4,5')], '6 + 1 = <b>7 students</b>', 'hm:yh13:3 hq:yh13:4,5')],
    fig=hist('yh13', -1, 0.5, DV, 8, 2, 'log<tspan baseline-shift="sub" font-size="11">10</tspan>(distance)', 'frequency'), figw='1fr'))

# ---- Exit tasks
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
NV = [k for k, f in neck.items() for _ in range(f)]
S.append(qslide('exit', '1 of 3', 'Show what you know', 'VCAA 2020 Exam 2 Q2a',
    'The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the dot plot below.<br>Write down the modal <i>neck size</i>, in centimetres, for these 250 men.',
    KI_MODE, [('The tallest stack of dots: 48 dots at 38.', f'xm:e1:{sk(NV, lambda v: v == 38)}')],
    'The modal neck size is <b>38 cm</b>.', ED + ', 1C Q16 · VCAA 2020 Exam 2 Data analysis Q2a (% from the examiner report). Dot plot redrawn.',
    fig=bigdot('e1', NV, 30, 45, 'neck size (cm)', H=520), marks=1, vcaa=93, figw='1.2fr', ans_do=f'xm:e1:{sk(NV, lambda v: v == 38)}',
    watch='write the <b>value</b> (38 cm), not the number of men (48). <span class="zsc">(teacher note)</span>'))
TR = [('2', '2 2 4 4'), ('2', '5 7 8 8 8 8 8 8 9 9 9 9'), ('3', '1 2 3 3 4 4 4'), ('3', '5 6 7 7 7 7'), ('4', '1')]
OPTDIST['2 of 3'] = [87, 9, 1, 2, 1]
S.append(qslide('exit', '2 of 3', 'Show what you know', 'VCAA 2016 Exam 1 Q3',
    'The stem plot below displays 30 temperatures recorded at a weather station.<br>The modal temperature is',
    KI_MODE, [('2 | 8 has six leaves: more than any other value.', 'lx:e2:6,7,8,9,10,11'), ('Read the key: 2 | 8 = 2.8 °C', 'lx:e2:6,7,8,9,10,11')],
    '2.8 °C', ED + ', 1C Q18 · VCAA 2016 Exam 1 Data analysis Q3 (% from the examiner report)',
    fig=stem('e2', TR, 'key: 2 | 2 = 2.2 °C &nbsp; <i>temperature</i>').replace('class="zstem"', 'class="zstem zsm"'), marks=1, vcaa=87, figw='1.1fr',
    opts=[('A', '2.8 °C'), ('B', '2.9 °C'), ('C', '3.7 °C'), ('D', '8.0 °C'), ('E', '9.0 °C')], key='A'))
PV = [0, 0, 1, 0, 7, 5, 21, 13, 1, 0]
OPTDIST['3 of 3'] = [7, 6, 7, 71, 9]
S.append(qslide('exit', '3 of 3', 'Show what you know', 'VCAA 2019 Exam 1 Q3',
    'The histogram below shows the population size for these 48 countries plotted on a log<sub>10</sub> scale.<br>Based on this histogram, the number of countries with a population size that is less than 100 000 people is',
    KI_LOGH, [r'$100\,000 = 10^{5}$: that is 5 on the log scale.', ('Columns below 5: 1 + 7', 'hq:e3:2,4')],
    '8', ED + ', 1D Q13 · VCAA 2019 Exam 1 Data analysis Q3 (% from the examiner report). Histogram redrawn; data: Worldometers.',
    fig=hist('e3', 0, 1, PV, 25, 5, 'log<tspan baseline-shift="sub" font-size="11">10</tspan> (population size)', 'frequency'), marks=1, vcaa=71, figw='1.1fr',
    opts=[('A', '1'), ('B', '5'), ('C', '7'), ('D', '8'), ('E', '48')], key='D'))

# ---- check-in + coursework
S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
         f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot("Success criteria: one per worked example")}</section>')
CWR = open(os.path.join(SH, 'cwr.html')).read().replace('>Exercise 9A: Collecting representative data<',' textLength="344" lengthAdjust="spacingAndGlyphs">Exercise 1C: Displaying and describing numerical data<'); CWL = open(os.path.join(SH, 'cwl.html')).read()
S.append(f'<section class="slide cwk">{bar("1C–1E", "Coursework · Exercises 1C, 1D, 1E")}<div class="cwgrid"><div class="cwl2">'
         '<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>'
         '<tr><th>Cambridge Exercise 1C</th><td>Q1–12</td></tr>'
         '<tr><th>Cambridge Exercise 1D</th><td>Q1–11</td></tr>'
         '<tr><th>Cambridge Exercise 1E</th><td>Q1–6</td></tr>'
         '<tr><th>Practice booklet</th><td>1C, 1D, 1E sections</td></tr></tbody></table>'
         '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
         f'{CWL}</div>{CWR}</div>{foot(CG + ", Exercises 1C, 1D, 1E")}</section>')

# ---- S2 extras: build-up figures (xb bars, xd dots, xl leaves, xm mode dots, xs table rows) + the log-scale interactive
S2CSS = r'''<style>
.zhg.zbuild rect.b{opacity:0;transition:opacity .35s}.zhg.zbuild rect.b.xon{opacity:1}
.zdp.zbuild .dot{opacity:0;transition:opacity .3s}.zdp.zbuild .dot.xon{opacity:1}
.zstem.zbuild .lv{visibility:hidden}.zstem.zbuild .lv.xon{visibility:visible}
.zdp .dot.xm,.zbd .dot.xm{fill:#d00000!important}
.ztab.zdl2{font-size:20px;margin:8px 0}.ztab.zdl2 td{padding:2px 9px}.ztab.zsm3{font-size:16px}.ztab.zsm3 td{padding:1px 6px}
table.zft{border-collapse:collapse;font-size:21px;margin:auto}
table.zft th,table.zft td{border:1.5px solid #000;padding:4px 14px;text-align:center}table.zft th{background:#eee}
table.zft.zfill th{border-color:#d00000!important}
.zstem.zsm table{font-size:22px!important}.s2two .zstem td.zlv{min-width:0}.s2two>div{flex:1;min-width:0}#u11,#o11{--zsf:27px!important}#o11 .zkey{white-space:nowrap}.s2two .lv{min-width:14px;margin-right:4px}.zstem.zsm .zkey{font-size:16px}
.s2two{display:flex;gap:14px;align-items:flex-start;justify-content:center}
.s2shp{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;margin:12px 0}
.s2shp .zpc .st{text-align:center;font-size:18px!important;color:#000;white-space:normal}.s2shp svg{width:100%;height:170px}
.zhg.zmini text{display:none}.s2c{font-size:18px;margin-top:4px}
.s2socs{display:flex;flex-direction:column;gap:14px;margin:18px 0;flex:1}
.s2socs .st{font-size:25px!important;border:2px solid #000;padding:12px 16px;white-space:normal;color:#000}
.s2L{display:inline-block;width:42px;height:42px;line-height:42px;text-align:center;background:#000;color:#fff;font-weight:bold;margin-right:12px}
.s2rules{font-size:17px!important;margin-top:12px!important}.s2rules li{margin-bottom:5px!important}
table.s2lt{font-size:26px;margin:22px auto}table.s2lt td.s2h{color:transparent;transition:color .3s}table.s2lt tr.on td.s2h{color:#d00000}
.slide.s2li .zul li{margin-bottom:6px;font-size:17px}.slide.s2li .zseq li{margin-bottom:5px;font-size:18px}
.slide.s2cas .zfig{flex-direction:column;justify-content:flex-start!important;gap:8px}.slide.s2cas .zfig svg{max-height:260px}
.zlgo{font-size:21px;line-height:1.6}
.zmcq svg.zbd{max-height:410px!important}
.slide.tight table.zft td,.slide.tight table.zft th{padding:2px 12px}
.slide.tight .zb>div.zfig{padding:8px 14px}
.s2tpl{border:2px dashed #999;padding:8px 12px;font-size:21px;line-height:1.55;margin-bottom:6px;transition:all .3s}
.s2tpl .s2b{display:inline-block;min-width:70px;border-bottom:2px solid #333;text-align:center;color:transparent}
.s2tpl .s2b.xon{color:#d00000;font-weight:bold}
.s2tpl.xon{border:3px solid #1a7f1a;background:#eaf6ea}.s2tpl .zok{visibility:hidden}.s2tpl.xon .zok{visibility:visible}
.st.s2hid{display:none!important;height:0!important;min-height:0!important;margin:0!important;padding:0!important;border:0!important;overflow:hidden}

/* ==== STEM PLOT STANDARD (17 Nov): fixed cells, same font for stems+leaves, highlights never change size ==== */
.zstem{display:flex;flex-direction:column;align-items:center}
.zstem.zstem.zstem.zstem table,.zstem.zstem.zstem.zstem table{border-collapse:collapse;font-size:var(--zsf,44px)!important;font-variant-numeric:tabular-nums;line-height:1}
.zstem th,.zstem.zstem.zstem.zstem th{font-size:.42em!important;font-weight:bold;padding:0 .5em .25em!important;border-bottom:3px solid #000;text-align:left}
.zstem th:first-child{text-align:right}
.zstem td,.zstem.zstem.zstem.zstem td{padding:.06em 0!important;height:1.3em;vertical-align:middle}
.zstem td.zst,.zstem.zstem.zstem.zstem td.zst{font-weight:bold;text-align:right;padding:0 .35em 0 .2em!important;border-right:3px solid #000;width:auto}
.zstem td.zlv,.zstem.zstem.zstem.zstem td.zlv{padding:0 .2em 0 .3em!important;min-width:0!important;white-space:nowrap;text-align:left}
.zstem .lv,.zstem.zstem.zstem.zstem .lv{display:inline-block;box-sizing:border-box;width:.95em!important;min-width:0!important;height:1.2em;line-height:1.2em;margin:0 .07em 0 0!important;padding:0!important;text-align:center;vertical-align:middle;
  border-radius:.14em;transform:none!important;font-size:1em!important;transition:background-color .3s,color .3s,opacity .3s;position:relative}
.zstem .lv.mid,.zstem .lv.q{transform:none!important;color:#fff!important;opacity:1!important;text-decoration:none!important}.zstem .lv.mid{background:#d00000!important}.zstem .lv.q{background:#1f5fbf!important}
.zstem .lv.ex{outline:.07em solid #d00000;outline-offset:-.07em}
.zstem .lv.mid+.lv.mid::before,.zstem .lv.q+.lv.q::before{left:calc(-.035em - 1.5px)!important;width:3px!important;top:-.12em!important;bottom:-.12em!important;border-radius:0!important}
.zstem .lv[data-c]::after{font-size:max(10px,.3em)!important;width:auto!important;min-width:1.25em;padding:0 .2em;box-sizing:border-box;height:1.2em!important;line-height:1.2em!important;border-radius:.6em!important;top:auto!important;bottom:calc(100% + 1px)!important;left:50%!important;right:auto!important;transform:translateX(-50%);z-index:2}
.zstem .zkey,.zstem.zstem.zstem.zstem .zkey{font-size:max(20px,calc(var(--zsf,44px)*.55))!important;margin-top:.35em!important;color:#000;font-weight:bold;border:2px solid #000;border-radius:6px;padding:.1em .6em;background:#fff;transition:opacity .3s}
.slide.apkb .zfig svg.zbx{flex:1 1 0!important;min-height:0!important;max-height:210px!important}
.zstem.zcnt td{height:1.5em!important;vertical-align:bottom!important}.zstem.zcnt td.zst{padding-bottom:.08em!important}.zstem.zcnt .lv{margin-bottom:.06em!important}
.slide.apks .zfig{flex-direction:row!important;align-items:center!important;gap:18px;padding-top:6px!important;justify-content:center!important}.slide.apks .zfig .zstem{flex:none}.slide.apks .zw .st.zs{font-size:19px!important;margin:3px 0!important;line-height:1.55}.slide.apks .zfig svg.zbx{flex:1 1 0!important;min-width:0;max-height:none!important;width:auto}
.zstem .zkey.zkh{opacity:0}.zstem .zkey.zkh.on{opacity:1}
.zstem .zkey.zkh.on{animation:zkp .6s}@keyframes zkp{0%{background:#fff3a8}100%{background:#fff}}
.slide.z.s2hg .col .st.zs{flex-shrink:0!important;height:auto!important;font-size:20px!important;margin:0 0 4px!important;padding:3px 8px!important;line-height:1.3!important}
.s2hg svg.zhg{width:100%!important;height:auto!important;max-height:none!important}
.s2hg .col{justify-content:flex-start!important;gap:4px!important}
.slide.z.s2hg .col .st.zs.final{margin-top:8px!important}
</style>'''
S2JS = r'''<script>
window.addEventListener('load',()=>{
 const rng=s=>{const o=[];(s||'').split(',').forEach(p=>{if(p==='')return;if(p.includes('-')&&!p.startsWith('-')){const [a,b]=p.split('-').map(Number);for(let i=a;i<=b;i++)o.push(i)}else o.push(+p)});return o};
 function x2(sl){sl.querySelectorAll('.zkey.zkh.on').forEach(e=>e.classList.remove('on'));sl.querySelectorAll('.xon').forEach(e=>e.classList.remove('xon'));sl.querySelectorAll('.xm').forEach(e=>e.classList.remove('xm'));sl.querySelectorAll('table.s2lt tr.on').forEach(e=>e.classList.remove('on'));
  sl.querySelectorAll('.st[data-do].show').forEach(s=>s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');const el=document.getElementById(id);if(!el)return;
   if(op==='xb')rng(x).forEach(i=>el.querySelector(`rect.b[data-i="${i}"]`)?.classList.add('xon'));
   if(op==='xd')rng(x).forEach(k=>el.querySelector(`.dot[data-k="${k}"]`)?.classList.add('xon'));
   if(op==='xm')rng(x).forEach(k=>el.querySelector(`.dot[data-k="${k}"]`)?.classList.add('xm'));
   if(op==='xl'){const L=[...el.querySelectorAll('.lv')];rng(x).forEach(k=>L[k]?.classList.add('xon'))}
   if(op==='xs')el.querySelectorAll('tr')[+x]?.classList.add('on');
   if(op==='sk')el.querySelector('.zkey')?.classList.add('on');
   if(op==='bf')rng(x).forEach(k=>el.querySelectorAll(`[data-b="${k}"]`).forEach(e=>e.classList.add('xon')));
   if(op==='bok')el.classList.add('xon');
  }))}
 document.querySelectorAll('.slide.z').forEach(x2);
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);x2(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
 // log-scale interactive: one weight shown on an ordinary scale (0 to 10 000 kg) and on a log scale (-2 to 4)
 document.querySelectorAll('.slide.logx').forEach(sl=>{const sv=sl.querySelector('svg.zlg'),r=sl.querySelector('input'),O=sl.querySelector('.zlgo');
  const A=[['mouse',0.02],['cat',3.3],['person',70],['elephant',2512]];
  const fmt=w=>w>=100?Math.round(w).toLocaleString('en-AU'):(w>=1?w.toFixed(1):w.toPrecision(2));
  const draw=()=>{const b=+r.value/100,w=Math.pow(10,b),pl=v=>40+v/10000*620,pg=v=>40+(v+2)/6*620;
   let s='<text x="20" y="22" font-size="16" font-weight="bold">Ordinary scale (kg)</text><line x1="30" y1="80" x2="670" y2="80" stroke="#000" stroke-width="2"/>';
   for(let v=0;v<=10000;v+=2000)s+=`<line x1="${pl(v)}" y1="74" x2="${pl(v)}" y2="86" stroke="#000"/><text x="${pl(v)}" y="106" font-size="15" text-anchor="middle">${v.toLocaleString('en-AU')}</text>`;
   s+='<text x="20" y="152" font-size="16" font-weight="bold">Log scale: log₁₀(weight)</text><line x1="30" y1="210" x2="670" y2="210" stroke="#000" stroke-width="2"/>';
   for(let v=-2;v<=4;v++)s+=`<line x1="${pg(v)}" y1="204" x2="${pg(v)}" y2="216" stroke="#000"/><text x="${pg(v)}" y="236" font-size="15" text-anchor="middle">${v<0?'−'+(-v):v}</text>`;
   A.forEach(([n,v])=>{s+=`<circle cx="${pl(v)}" cy="64" r="6" fill="#555"/><circle cx="${pg(Math.log10(v))}" cy="194" r="6" fill="#555"/><text x="${pg(Math.log10(v))}" y="180" font-size="13" text-anchor="middle">${n}</text>`});
   s+=`<circle cx="${pl(w)}" cy="58" r="10" fill="#fff" stroke="#d00000" stroke-width="3"/><circle cx="${pg(b)}" cy="188" r="10" fill="#fff" stroke="#d00000" stroke-width="3"/>`;
   sv.innerHTML=s;
   O.innerHTML=`Weight = <b>${fmt(w)} kg</b><br>log₁₀(weight) = <b style="color:#d00000">${b.toFixed(2)}</b><br>Check: 10<sup>${b.toFixed(2)}</sup> = ${fmt(w)}<br><span style="font-size:17px">On the ordinary scale the mouse, cat and person all sit on top of each other at 0. On the log scale they spread out.</span>`};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(x=>x.onclick=e=>{e.stopPropagation();r.value=Math.round(Math.log10(+x.dataset.w)*100);draw()});draw()});
});
// ---- stem plot standard: biggest font (same for stems and leaves) that fits the figure box; key scales with it
function zstemfit(){document.querySelectorAll('.st[data-do]').forEach(t=>t.dataset.do.split(' ').forEach(a=>{const [op,id]=a.split(':');if(op==='ln'){const z=document.getElementById(id);if(z&&z.classList.contains('zstem'))z.classList.add('zcnt')}}));document.querySelectorAll('.slide.z').forEach(sl=>{const st=[...sl.querySelectorAll('.zstem')];if(!st.length)return;const was=sl.classList.contains('on');sl.classList.add('on');
  st.forEach(z=>{const fg=z.closest('.zfig')||z.parentNode;let f=z.dataset.max?+z.dataset.max:48;const bx=fg.querySelector('svg.zbx');const row=getComputedStyle(fg).flexDirection==='row';const ok=()=>(!bx||(row?bx.getBoundingClientRect().width>=300:bx.getBoundingClientRect().height>=110))&&fg.scrollHeight<=fg.clientHeight+1&&z.scrollWidth<=fg.clientWidth-8&&z.offsetWidth<=fg.clientWidth-8;
    z.style.setProperty('--zsf',f+'px');while(!ok()&&f>16){f-=1;z.style.setProperty('--zsf',f+'px')}});
  if(!was)sl.classList.remove('on')})}
document.fonts.ready.then(()=>setTimeout(zstemfit,900));
</script>'''
S[-1] = S[-1][:-len('</section>')] + S2CSS + S2JS + '</section>'

CSS = r'''<style>
/* ---- S3 additions (namespaced .z) ---- */
.slide.z .bar.ytb{background:#d9d9d9}
.slide.z .zb{flex:1;display:grid;border:1.5px solid #000;min-height:0}
.slide.z .zb>div{padding:12px 18px;min-width:0;overflow:hidden}
.slide.z .zb>div+div{border-left:1.5px solid #000}
.slide.z .zfig{display:flex;align-items:center;justify-content:center}
.slide.z .zfig svg{width:100%;max-height:420px}
.slide.z .zw{display:flex;flex-direction:column}
.slide.z .st.zs{white-space:normal;font-size:23px;line-height:1.35;margin:0 0 9px!important}
.slide.z .st.zs .katex{font-size:1.08em}
.slide.z .top>.q{font-size:22px;line-height:1.38}
.slide.z .zlead{font-size:21px;margin:12px 4px 2px}
.slide.z .zul{margin:4px 0 0;padding-left:22px}.slide.z .zul li{margin-bottom:12px}
.slide.z .zul.ck{list-style:none;padding-left:0}
.slide.z .zseq{margin:4px 0 0;padding-left:26px}.slide.z .zseq li{margin-bottom:8px}
.slide.z .zkd{border-bottom:1.5px dashed #888;padding:7px 0;display:flex;gap:14px;align-items:center;flex:1}
.slide.z .zkd .zkn{width:190px;flex:none;font-weight:bold}
.slide.z .zn{font-size:16px;color:#555}
.zstem table{border-collapse:collapse;font-size:32px}
.zstem th{font-size:16px;padding:2px 14px;border-bottom:3px solid #000}
.zstem td.zst{border-right:3px solid #000;text-align:right;padding:2px 16px;font-weight:bold}
.zstem td.zlv{padding:2px 12px;min-width:250px;white-space:nowrap}
.slide.apk .zstem table{font-size:24px}.slide.apk .lv{margin-right:2px;min-width:18px}.zstem .zkey{font-size:16px;margin-top:8px;color:#333}
.lv{display:inline-block;min-width:24px;text-align:center;margin-right:6px;border-radius:5px;padding:0 3px;transition:all .3s;position:relative}
.lv.x{opacity:.2;text-decoration:line-through}
.lv.mid{background:#d00000;color:#fff;opacity:1;text-decoration:none;transform:scale(1.15)}
.lv.q{background:#1f5fbf;color:#fff;opacity:1;text-decoration:none;transform:scale(1.15)}
.lv.lo{background:#dbe7fb}.lv.hi{background:#fde9cf}
.lv.ex{outline:3px solid #d00000}
.slide.z .zrow{display:flex;gap:22px;align-items:flex-start;margin-top:6px}
.slide.apk .qtxt{font-size:20px;padding:0;margin:0 0 10px}.zsk{font-size:15px;color:#555}
.slide.apk .skill{padding:0 0 6px}
.slide.apk .st.zs{font-size:20px}
.ztab{border-collapse:collapse;margin:8px 0;font-size:19px}
.ztab th,.ztab td{border:1.5px solid #000;padding:3px 10px;text-align:center}
.ztab th{background:#eee}
.ztab.zsm{font-size:16px}.ztab.zsm th{text-align:left}
table.z5{border-collapse:collapse;color:#d00000;font-size:22px;margin-top:6px}
table.z5 th,table.z5 td{border:1.5px solid currentColor;padding:3px 16px;text-align:center}
.slide.z .z3{display:grid;grid-template-columns:repeat(3,1fr);gap:0;flex:1}
.slide.z .z3>div{padding:0 14px}.slide.z .z3>div+div{border-left:1.5px solid #000}
.slide.z .lab{font-weight:bold;margin-right:10px;font-size:24px}
.slide.z .qq{font-size:24px;margin-bottom:6px}
.zpair{display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:24px;flex:1;align-items:center;margin:14px 0}
.zpc{border:3px solid #000;padding:12px;display:flex;flex-direction:column;gap:10px}
.zpt{font-weight:bold;font-size:26px;text-align:center}
.zbox{border:2px solid #000;padding:8px 12px;font-size:24px;font-weight:bold;box-shadow:4px 4px 0 #bbb}
.zbox i.zsub{display:block;font-style:normal;font-size:16px;font-weight:normal;color:#444}
.zpm .st{text-align:center;font-size:19px;color:#000;margin-bottom:26px!important;white-space:normal}
.zarr{font-size:28px;font-weight:bold;color:#d00000}
.zctr{text-align:center;font-size:22px!important}
.ztime{font-size:150px;font-weight:bold;text-align:center;font-variant-numeric:tabular-nums;margin:20px 0}
.ztime.low{color:#d00000}
.zbtns,.ztabs{display:flex;gap:10px;justify-content:center}
.zbtns button,.ztabs button{font:inherit;font-size:20px;border:2px solid #000;background:#fff;padding:6px 16px;cursor:pointer;box-shadow:3px 3px 0 #bbb}
.ztabs{justify-content:flex-start;margin-bottom:10px}
.ztabs button.on{background:#000;color:#fff}
.zcas{font-size:20px;line-height:1.4;padding-left:26px}.zcas li{margin-bottom:8px}
.zsl{display:flex;gap:14px;align-items:center;font-size:18px;margin-top:8px}.zsl input{flex:1;height:30px}
.slide.sdx .zlead{font-size:18px}.zmmo,.zsdo{font-size:22px;line-height:1.6}
.zrule{margin-top:auto;border:2px solid #000;background:#fff7d6;padding:10px 12px;font-size:17px;line-height:1.35}
.zchk{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1.5px solid #000;margin-top:12px;flex:1}
.zci{display:flex;gap:16px;align-items:center;padding:10px 18px;font-size:22px;border-bottom:1.5px dashed #888}
.zcb{width:40px;height:40px;border:2px solid #000;flex:none;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:bold;cursor:pointer}
.zcb.s1{background:#e3f5e3;color:#1a7f1a}.zcb.s1::after{content:'✓'}
.zcb.s2{background:#fff3cd;color:#a06b00}.zcb.s2::after{content:'~'}
.zcb.s3{background:#fde2e2;color:#d00000}.zcb.s3::after{content:'✗'}
.zcw{width:100%;border-collapse:collapse;font-size:21px}
.zcw th{background:#eee;text-align:left;padding:6px 10px;border:1.5px solid #000}
.zcw td{border:1.5px solid #000;padding:7px 10px}.zcw td:last-child{width:110px;text-align:center;font-weight:bold}
.slide.z .note{font-size:19px;margin-top:16px}
.zdp .dot,.zhg rect.b{transition:fill .3s,stroke .3s}
/* ---- round 2 ---- */
.slide.z .zside{display:flex;flex-direction:column;gap:8px;align-items:flex-end;flex:none}
.zstat{font-size:17px;font-weight:600;color:#555;border:2px solid #000;border-radius:999px;padding:4px 14px;background:#fff;white-space:nowrap}
.zstat b{font-size:22px;color:#000;transition:color .3s}
.zstat.done{background:#e3f5e3;border-color:#1a7f1a}.zstat.done b{color:#1a7f1a}
.zcmd{font-size:16px;border:2px solid #000;padding:3px 12px;background:#fff7d6}
.zmk{font-size:16px;color:#666}
.zdl{display:inline-block;font-size:13px;font-weight:bold;text-transform:uppercase;letter-spacing:.5px;background:#6b3fc9;color:#fff;padding:1px 8px;margin-right:6px;vertical-align:2px}
.slide.z .st.zdis,.slide.z .st.ztrap{color:#3d2380;background:#f1ebfd;border:2px solid #6b3fc9;padding:6px 10px;font-size:19px!important;line-height:1.35}
.slide.z .st.ztrap{margin-top:auto!important}
.zsc{font-size:16px;color:#555}
.zmc{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;margin-top:10px;width:100%}
.zmc>div{position:relative;border:2px solid #000;padding:6px 60px 6px 10px;font-size:22px;background:#fff;transition:background .3s}
.zmc>div>*{position:relative;z-index:1}
.zmc .pb{position:absolute!important;left:0;top:0;bottom:0;width:0;background:rgba(80,90,110,.16);transition:width .9s ease;z-index:0}
.zmc .pc{position:absolute!important;right:10px;top:50%;transform:translateY(-50%);font-weight:bold;color:#555;opacity:0;transition:opacity .4s}
.zmc.pct .pc{opacity:1}
.zmc>div.right{background:#e3f5e3;border-color:#1a7f1a;font-weight:bold}.zmc>div.right .pb{background:rgba(26,127,26,.25)}
.zmc>div.dis{background:#f1ebfd;border-color:#6b3fc9}.zmc>div.dis .pb{background:rgba(107,63,201,.25)}
.zfig.zcol{flex-direction:column;justify-content:center}
.ztab td.hl{background:#fff2a8;font-weight:bold;outline:2px solid #d00000}
.ztab tr.dim{opacity:.25;transition:opacity .4s}
.ztab.zbig{font-size:26px}.ztab.zv{border-collapse:collapse}
.ztab.zora{font-size:17px}.ztab.zsm2{font-size:15px}
.zsumw{width:100%}
.ztiles{display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
.zt{position:relative;font-size:28px;border:2px solid #000;min-width:62px;text-align:center;padding:6px 8px;transition:all .3s}
.zt.on{background:#fde2e2;border-color:#d00000}
.zt[data-c]::after{content:attr(data-c);position:absolute;top:-11px;right:-9px;background:#1f5fbf;color:#fff;font-size:13px;font-weight:bold;border-radius:50%;width:22px;height:22px;line-height:22px;text-align:center}
.zrun{margin:22px auto 0;text-align:center;font-size:18px;color:#555}
.zrun b{display:block;font-size:56px;color:#d00000;font-variant-numeric:tabular-nums}
.zrun i{display:block;font-style:normal;font-size:22px;color:#000;margin-top:6px}
.zab{margin-bottom:10px}
/* n even: a line between the two middle values */
.mtile,.lv{position:relative}
.mtile.mid+.mtile.mid::before,.lv.mid+.lv.mid::before{content:'';position:absolute;left:-7px;top:-12px;bottom:-12px;width:4px;background:#d00000;border-radius:2px}
.mtile.q+.mtile.q::before,.lv.q+.lv.q::before{content:'';position:absolute;left:-7px;top:-12px;bottom:-12px;width:4px;background:#1f5fbf;border-radius:2px}
.mtile.x.mid+.mtile.x.mid::before{opacity:1}
/* less dead space, less bunching */
.slide.z .st.zs{font-size:26px;line-height:1.45;margin:0 0 15px!important}
.slide.z .zb>div{padding:16px 22px}
.slide.z .top>.q{font-size:23px}
.zstem table{font-size:38px}.zstem th{font-size:18px}.zstem .zkey{font-size:19px}
.slide.z .zfig svg{max-height:470px}
.zcfu{display:inline-flex;gap:10px;margin-left:auto;margin-right:18px;align-items:center}
.zcfu span{display:flex;align-items:center;gap:5px;font-size:13px;color:#777;font-weight:600}
.zcfu img{width:26px;height:26px;opacity:.85}
.slide.z .foot{align-items:center}
.zhso{font-size:20px;line-height:1.55}
.zhso .ol{color:#d00000;font-weight:bold}
.zbtns button{font-size:17px}
.slide.cwk .zcw{font-size:25px}.slide.cwk .zcw td{padding:12px 12px}
.slide.cas .zcas{font-size:22px}

.slide.apk .zstem table{font-size:24px!important}.slide.apk .st.zs{font-size:22px}
.slide.z.eng .stp{font-size:24px;margin-bottom:14px}
.slide.z.eng .tl .mtile{font-size:28px;min-width:48px}

.st.zmeasure{opacity:1}
.zmcq{justify-content:flex-start!important;align-items:stretch!important}.zmcq .zq{font-size:20px;line-height:1.35;margin-bottom:8px}.zmcq svg{max-height:260px!important}
.zside.zrow2{flex-direction:row;justify-content:flex-start;align-items:center;margin-bottom:14px;flex-wrap:wrap}
.slide.z .zw>*,.slide.z .zab>*{flex:none}
.slide.z .zw .st.zs{overflow:visible}
/* ---- round 3: one template ---- */
.zpill{font-size:15px!important;border:1.5px solid #000;padding:2px 10px;background:#fff;white-space:nowrap}
.zpart{font-weight:bold;font-size:20px;color:#000;border-bottom:1.5px dashed #888;margin:4px 0 8px;padding-bottom:2px}
.zok{display:inline-block;font-size:15px;font-weight:bold;background:#1a7f1a;color:#fff;padding:1px 8px;margin-right:6px;vertical-align:3px}
.slide.z .st.final{border-top:2px solid #d00000;padding-top:8px}
.zdl.zw2{background:#c46a00}
.ztab.zinq{margin:8px 0;font-size:18px}
.ztr{display:flex;align-items:center;gap:10px;margin-bottom:14px}.ztr .tl{margin:0}
.slide.z .zfig.zcol{align-items:center}
table.zfill td{color:transparent;transition:color .3s}table.zfill td.on{color:#d00000;font-weight:bold}
table.z5b{font-size:18px;margin:6px 0}
.zbox.pa{background:#fde2e2;border-color:#d00000}.zbox.pb2{background:#dbe7fb;border-color:#1f5fbf}
.zchk2{display:grid;border:1.5px solid #000;margin-top:10px;flex:1;grid-auto-rows:1fr}
.zch{display:grid;grid-template-columns:1fr 90px 90px 90px;align-items:center;border-bottom:1.5px dashed #888;padding:0 14px;font-size:20px}
.zch.h{font-weight:bold;background:#eee;font-size:16px;text-transform:uppercase}
.zch.h span:not(:first-child){text-align:center}
.zct{font:inherit;font-size:22px;font-weight:bold;width:64px;height:40px;justify-self:center;border:2px solid #000;background:#fff;cursor:pointer}
.zct.g{color:#1a7f1a}.zct.m{color:#a06b00}.zct.n{color:#d00000}
.zmc>div.right::after{content:'✓ correct';position:absolute;right:62px;top:50%;transform:translateY(-50%);font-size:14px;color:#1a7f1a;z-index:1}
.zmc>div.dis::after{content:'distractor';position:absolute;right:62px;top:50%;transform:translateY(-50%);font-size:14px;color:#6b3fc9;z-index:1}
.lv.lo::after,.lv.hi::after{content:'';position:absolute;left:0;right:0;bottom:-3px;height:3px;background:currentColor;opacity:.0}

.slide.z .st.zs{font-size:24px}
.zb.stack{grid-template-columns:1fr!important;grid-template-rows:auto minmax(0,1fr)}
.zb.stack>div+div{border-left:none!important;border-top:1.5px solid #000}
.zfig.zrowf{display:flex!important;flex-direction:row!important;gap:40px;justify-content:center;flex-wrap:wrap}
.zw.c2{display:block!important;column-count:2;column-gap:34px;column-rule:1.5px dashed #bbb}
.zw.c2 .zpart.brk{break-before:column}
.zw.c2 .st.final{column-span:all;margin-top:8px!important}
.zw.c2>*{break-inside:avoid}
.slide.exam .zw .ki{width:auto;margin:0 0 12px;font-size:15px}
.slide.exam .zw .ki .kn{font-size:13px}
.zstem table{font-size:34px}

.zpq{font-size:21px;line-height:1.35;color:#000;margin:0 0 10px;white-space:normal;flex:none}
.zpq b{display:inline-block;min-width:26px;font-size:22px}
.zpq.sep{border-top:2px dotted #888;padding-top:12px;margin-top:6px}
.zw.c2 .zpq.brk{break-before:column;border-top:none;padding-top:0;margin-top:0}
.slide.z .st.final.zpa{border-top:none;padding-top:0;margin-bottom:10px!important}
.zw.c2 .st.final.zpa{column-span:none}

/* tiles: one row, thin centred median line */
.slide .tl{flex-wrap:nowrap!important;gap:8px!important}
.slide .tl .mtile{flex:1 1 0!important;min-width:0!important;max-width:58px;font-size:24px!important;padding:5px 0!important}
.slide.nl .tl .mtile{font-size:22px!important}
.mtile.mid+.mtile.mid::before,.mtile.q+.mtile.q::before{left:-5px!important;width:2px!important;top:-10px!important;bottom:-10px!important;border-radius:0!important}
.lv{margin-right:6px}
.lv.mid+.lv.mid::before,.lv.q+.lv.q::before{left:-4px!important;width:2px!important;top:-6px!important;bottom:-6px!important;border-radius:0!important}
.mtile.mid,.mtile.q,.lv.mid,.lv.q{transform:none!important}

.mtile[data-c]::after,.lv[data-c]::after{content:attr(data-c);position:absolute;top:-13px;right:-8px;background:#1f5fbf;color:#fff;font-size:12px;font-weight:bold;border-radius:50%;width:20px;height:20px;line-height:20px;text-align:center;font-family:Arial,sans-serif;text-decoration:none;opacity:1}
.lv[data-c]::after{top:-10px;right:-7px;width:17px;height:17px;line-height:17px;font-size:10px}
.slide .tl{margin-top:16px!important}

.zcas2{display:flex;flex-direction:column;gap:12px;width:100%;align-self:stretch}
.zch3{font-weight:bold;font-size:15px;text-transform:uppercase;background:#eee;border:1.5px solid #000;padding:2px 10px}
.slide .zcas2 .zcas{font-size:17px!important;line-height:1.3;margin:6px 0 0;padding-left:24px}.zcas2 .zcas li{margin-bottom:3px}

.ztr{flex:1;min-width:0}.ztr .tl{flex:1}
.zfig .tl{width:100%;align-self:stretch}
.zfig.zrowf{flex-wrap:nowrap!important}
.zstem .lv{margin-right:10px}.zstem .lv.mid+.lv.mid::before,.zstem .lv.q+.lv.q::before{left:-6px!important}
.slide.tight .st.zs{font-size:20px!important;margin-bottom:6px!important}.slide.tight .zpq{margin-bottom:4px;font-size:19px}.slide.tight .zpq.sep{padding-top:6px}

.zcmd{display:none!important}
.slide.z .st.final{border:2px solid #1a7f1a!important;background:#e9f7e9;padding:6px 12px!important;margin-top:6px!important;white-space:normal}
.slide.z .st.final.zpa{border:2px solid #1a7f1a!important;padding:4px 10px!important}
.zok{background:#1a7f1a;font-size:15px}
.slide.z .st.zdis{margin-top:10px!important}

table.zfill th,table.zfill td{border:1.5px solid #d00000!important;min-width:56px;height:34px}

</style>'''

JS = r'''<script>
// ---- S3 engines: dot plots, histograms, stem plots driven by .st[data-do]; sliders; timer; tabs; check-in
const NS='http://www.w3.org/2000/svg';
function drawDot(sv){const v=JSON.parse(sv.dataset.v),lo=+sv.dataset.lo,hi=+sv.dataset.hi,W=640,px=x=>40+(x-lo)/(hi-lo)*(W-80),cnt={};
  let s=`<line x1="20" y1="200" x2="${W-20}" y2="200" stroke="#000" stroke-width="2"/>`;
  for(let x=lo;x<=hi;x++)s+=`<line x1="${px(x)}" y1="194" x2="${px(x)}" y2="206" stroke="#000"/><text x="${px(x)}" y="228" font-size="18" text-anchor="middle">${x}</text>`;
  const step=Math.min(26,170/Math.max(...Object.values(v.reduce((a,x)=>(a[x]=(a[x]||0)+1,a),{}))));
  v.forEach((x,k)=>{cnt[x]=(cnt[x]||0)+1;const cy=200-step*cnt[x]+step/2-4;s+=`<circle class="dot" data-k="${k}" cx="${px(x)}" cy="${cy}" r="${Math.min(11,step/2-1)}" fill="#555"/><text class="dn" data-k="${k}" x="${px(x)}" y="${cy+5}" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle" opacity="0">${k+1}</text>`});
  if(sv.dataset.xl)s+=`<text x="${W/2}" y="250" font-size="17" text-anchor="middle">${sv.dataset.xl}</text>`;
  s+=`<g class="mk"></g>`;sv.innerHTML=s;sv._px=px;sv._v=v}
function drawHist(sv){const c=JSON.parse(sv.dataset.cfg),n=c.v.length,X0=70,X1=580,Y0=280,Y1=20,bw=(X1-X0)/n,py=y=>Y0-(y/c.ymax)*(Y0-Y1);
  let s='';for(let y=0;y<=c.ymax;y+=c.ystep)s+=`<line x1="${X0}" y1="${py(y)}" x2="${X1}" y2="${py(y)}" stroke="#ddd"/><text x="${X0-8}" y="${py(y)+5}" font-size="15" text-anchor="end">${y}</text>`;
  let cum=0;c.v.forEach((f,i)=>{cum+=f;s+=`<rect class="b" data-i="${i}" x="${X0+i*bw}" y="${py(f)}" width="${bw}" height="${Y0-py(f)}" fill="#fff" stroke="#000" stroke-width="2"/>`+
    (f?`<text class="cu" data-i="${i}" x="${X0+i*bw+bw/2}" y="${py(f)-8}" font-size="17" font-weight="bold" fill="#d00000" text-anchor="middle" opacity="0">${cum}</text>`:'')});
  for(let i=0;i<=n;i++){const x=c.start+i*c.w;s+=`<text x="${X0+i*bw}" y="${Y0+20}" font-size="15" text-anchor="middle">${c.w<1?x.toFixed(1):+x.toFixed(2)}</text>`}
  s+=`<line x1="${X0}" y1="${Y0}" x2="${X1}" y2="${Y0}" stroke="#000" stroke-width="2"/><line x1="${X0}" y1="${Y0}" x2="${X0}" y2="${Y1}" stroke="#000" stroke-width="2"/>`;
  if(c.xl)s+=`<text x="${(X0+X1)/2}" y="${Y0+44}" font-size="16" text-anchor="middle">${c.xl}</text>`;
  s+=`<text transform="translate(18 ${(Y0+Y1)/2}) rotate(-90)" font-size="16" text-anchor="middle">${c.yl}</text>`;
  sv.setAttribute('viewBox','0 0 600 '+(c.xl?335:310));sv.innerHTML=s}
document.querySelectorAll('svg.zdp').forEach(drawDot);document.querySelectorAll('svg.zhg').forEach(drawHist);
function zApply(sl,anim){const tok=sl._zt=(sl._zt||0)+1;const T=f=>()=>{if(sl._zt===tok)f()};
  sl.querySelectorAll('svg.zdp').forEach(sv=>{sv.querySelectorAll('.dot').forEach(d=>{d.setAttribute('fill','#555');d.removeAttribute('stroke')});sv.querySelectorAll('.dn').forEach(t=>t.setAttribute('opacity',0));sv.querySelector('.mk').innerHTML=''});
  sl.querySelectorAll('svg.zhg').forEach(sv=>{sv.querySelectorAll('rect.b').forEach(r=>r.setAttribute('fill','#fff'));sv.querySelectorAll('.cu').forEach(t=>t.setAttribute('opacity',0))});
  sl.querySelectorAll('.lv').forEach(l=>l.className='lv');
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const last=s===anim;s.dataset.do.split(' ').forEach(a=>{const [op,id,x,y,c]=a.split(':');const el=document.getElementById(id);if(!el)return;
    const L=[...el.querySelectorAll('.lv')],ks=(x||'').split(',').map(Number);
    if(op==='dn'){const n=+x;for(let k=0;k<n;k++){const go=()=>{el.querySelector(`.dot[data-k="${k}"]`).setAttribute('fill','#1f5fbf');el.querySelector(`.dn[data-k="${k}"]`).setAttribute('opacity',1)};last?setTimeout(T(go),k*(1600/n)):go()}}
    if(op==='dm'){ks.forEach(k=>{const d=el.querySelector(`.dot[data-k="${k}"]`);d.setAttribute('fill','#d00000');d.setAttribute('stroke','#000');d.setAttribute('stroke-width',2)});
      const m=ks.reduce((t,k)=>t+el._v[k],0)/ks.length,X=el._px(m);el.querySelector('.mk').innerHTML=`<line x1="${X}" y1="10" x2="${X}" y2="200" stroke="#d00000" stroke-width="3" stroke-dasharray="7 5"/><text x="${X+8}" y="24" fill="#d00000" font-size="18" font-weight="bold">M = ${m}</text>`}
    if(op==='hc'){el.querySelectorAll('.cu').forEach((t,i)=>{const go=()=>t.setAttribute('opacity',1);last?setTimeout(T(go),i*260):go()})}
    if(op==='hm'||op==='hq')ks.forEach(i=>el.querySelector(`rect.b[data-i="${i}"]`).setAttribute('fill',op==='hm'?'#f6b3b3':'#b9cff3'));
    if(op==='lb')L.slice(+x,+y+1).forEach(l=>l.classList.add(c));
    if(op==='lq')ks.forEach(k=>L[k].classList.add('q'));
    if(op==='lm')ks.forEach(k=>L[k].classList.add('mid'));
    if(op==='lx')ks.forEach(k=>L[k].classList.add('ex'));
    if(op==='lc'){let i=+x,j=+y,k=0;while(j-i>=2){[i,j].forEach(q=>{const go=()=>L[q].classList.add('x');last?setTimeout(T(go),k*140):go()});i++;j--;k++}}
  })})}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')&&t.dataset.do!==undefined){const sl=t.closest('.slide');if(!seen.has(sl)){seen.add(sl);zApply(sl,t.classList.contains('show')?t:null)}}
  else if(t.classList&&t.classList.contains('st')&&t.closest('.slide.z')){const sl=t.closest('.slide');if(sl.querySelector('[data-do]')&&!seen.has(sl)){seen.add(sl);zApply(sl,null)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// standard deviation
document.querySelectorAll('.slide.sdx').forEach(sl=>{const sv=sl.querySelector('svg.zsd'),r=sl.querySelector('input'),O=sl.querySelector('.zsdo'),D=[-1,-.75,-.45,-.15,.15,.45,.75,1];
  const draw=()=>{const k=+r.value/100*40,d=D.map(z=>50+Math.sign(z)*Math.round(Math.abs(z)*k)),m=d.reduce((s,v)=>s+v,0)/8,sd=Math.sqrt(d.reduce((s,v)=>s+(v-m)**2,0)/7),px=v=>30+v/100*640;
    let s=`<line x1="20" y1="230" x2="690" y2="230" stroke="#000" stroke-width="2"/>`;for(let v=0;v<=100;v+=10)s+=`<line x1="${px(v)}" y1="224" x2="${px(v)}" y2="236" stroke="#000"/><text x="${px(v)}" y="254" font-size="15" text-anchor="middle">${v}</text>`;
    s+=`<rect x="${px(m-sd)}" y="10" width="${px(m+sd)-px(m-sd)}" height="215" fill="#1f5fbf" fill-opacity=".08"/><line x1="${px(m)}" y1="10" x2="${px(m)}" y2="228" stroke="#d00000" stroke-width="3" stroke-dasharray="7 5"/>`;
    d.forEach((v,i)=>{const y=30+i*24;s+=`<line x1="${px(m)}" y1="${y}" x2="${px(v)}" y2="${y}" stroke="#1f5fbf" stroke-width="3"/><circle cx="${px(v)}" cy="${y}" r="8" fill="#555"/>`});
    sv.innerHTML=s;O.innerHTML=`Scores: ${d.join(', ')}<br>Mean $\\bar{x}$ = <b>${m.toFixed(1)}</b><br>Standard deviation $s$ = <b style="color:#1f5fbf">${sd.toFixed(2)}</b><br><span style="font-size:17px">Blue lines = distance of each score from the mean. Shaded band = mean ± one standard deviation.</span>`;
    if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};r.oninput=draw;draw()});

// ---- round 2: slide-level state (VCAA %, MC key/distractor/% bars, table highlights, running sums)
const CFU=__CFU__;
document.querySelectorAll('.slide[data-cfu]').forEach(sl=>{const f=sl.querySelector('.foot');if(!f)return;const w=document.createElement('span');w.className='zcfu';
  sl.dataset.cfu.split(' ').forEach(c=>{if(CFU[c])w.insertAdjacentHTML('beforeend',`<span><img src="${CFU[c][0]}" alt="">${CFU[c][1]}</span>`)});f.insertBefore(w,f.querySelector('.pg'))});
function z2(sl,anim){const tok=sl._z2=(sl._z2||0)+1;const T=f=>()=>{if(sl._z2===tok)f()};
  sl.querySelectorAll('.mtile[data-c],.lv[data-c]').forEach(t=>delete t.dataset.c);sl.querySelectorAll('.zfill td').forEach(t=>t.classList.remove('on'));sl.querySelectorAll('.zbox').forEach(b=>b.classList.remove('pa','pb2'));
  const S=sl.querySelector('.zstat');if(S){S.classList.remove('done');S.querySelector('b').textContent='?%'}
  const M=sl.querySelector('.zmc');if(M){M.classList.remove('pct');M.querySelectorAll('div[data-o]').forEach(o=>{o.classList.remove('right','dis');o.querySelector('.pb').style.width=0})}
  sl.querySelectorAll('.ztab td.hl').forEach(t=>t.classList.remove('hl'));sl.querySelectorAll('.ztab tr.dim').forEach(t=>t.classList.remove('dim'));
  sl.querySelectorAll('.zsumw').forEach(w=>{w.querySelectorAll('.zt').forEach(t=>{t.classList.remove('on');delete t.dataset.c});const b=w.querySelector('.zrun b');b.textContent='0';w.querySelector('.zrun i')?.remove()});
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const last=s===anim;s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');
    if(op==='stat'&&S){S.querySelector('b').textContent=id+'%';S.classList.add('done')}
    if(op==='key'&&M)M.querySelector(`[data-o="${id}"]`).classList.add('right');
    if(op==='dis'&&M)M.querySelector(`[data-o="${id}"]`).classList.add('dis');
    if(op==='tn'||op==='tclr'){const tt=[...sl.querySelectorAll(`.tl[data-t="${id}"] .mtile`)];if(op==='tclr'){tt.forEach(t=>delete t.dataset.c)}else{const st0=+x,K=+a.split(':')[3];for(let k=0;k<K;k++){const t=tt[st0+k];if(!t)continue;const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*(1500/K)):go()}}}
    if(op==='ln'){const L=[...document.getElementById(id).querySelectorAll('.lv')],st0=+x,K=+a.split(':')[3];for(let k=0;k<K;k++){const t=L[st0+k];if(!t)continue;const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*(1500/K)):go()}}
    if(op==='pair'||op==='pair2'){[id,x].forEach(q=>document.getElementById(q)?.classList.add(op==='pair'?'pa':'pb2'))}
    if(op==='pct'&&M){M.classList.add('pct');M.querySelectorAll('div[data-o]').forEach(o=>{o.querySelector('.pb').style.width=parseFloat(o.querySelector('.pc').textContent)+'%'})}
    const el=document.getElementById(id);if(!el)return;
    if(op==='fill')el.querySelector(`td[data-k="${x}"]`)?.classList.add('on');
    if(op==='tc')x.split(',').forEach(k=>el.querySelector(`td[data-k="${k}"]`)?.classList.add('hl'));
    if(op==='dim')el.querySelectorAll('tr')[+x].classList.add('dim');
    if(op==='cnt')el.querySelectorAll('.zt').forEach((t,k)=>{const go=()=>t.dataset.c=k+1;last?setTimeout(T(go),k*180):go()});
    if(op==='sum'){const TT=[...el.querySelectorAll('.zt')],b=el.querySelector('.zrun b');let run=0;const dp=Math.max(...TT.map(t=>(t.textContent.split('.')[1]||'').length));
      TT.forEach((t,k)=>{const go=()=>{t.classList.add('on');run+=parseFloat(t.textContent);b.textContent=run.toFixed(dp)};last?setTimeout(T(go),k*(1800/TT.length)):go()})}
    if(op==='bal'){const go=()=>{el.querySelector('.zrun i')?.remove();el.querySelector('.zrun').insertAdjacentHTML('beforeend',`<i>÷ ${el.querySelectorAll('.zt').length} = <b style="display:inline;font-size:30px">${x}</b></i>`)};last?setTimeout(T(go),1900):go()}
  })})}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);z2(sl,t.classList.contains('show')?t:null)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// house prices: mean or median
document.querySelectorAll('.slide.house').forEach(sl=>{const sv=sl.querySelector('svg.zhs'),r=sl.querySelector('input'),O=sl.querySelector('.zhso');
  const md=a=>{const n=a.length,h=Math.floor(n/2);return n%2?a[h]:(a[h-1]+a[h])/2};
  const draw=()=>{const X=+r.value,base=[620,680,700,720,740,780,820],d=[...base,X].sort((a,b)=>a-b),med=md(d),q1=md(d.slice(0,4)),q3=md(d.slice(4)),iqr=q3-q1,lo=q1-1.5*iqr,hi=q3+1.5*iqr,mean=d.reduce((t,v)=>t+v,0)/8;
    const top=X>900?3000:1000,stp=top>1500?500:100,px=v=>30+v/top*640;let s=`<line x1="20" y1="190" x2="690" y2="190" stroke="#000" stroke-width="2"/>`;
    for(let v=0;v<=top;v+=stp)s+=`<line x1="${px(v)}" y1="184" x2="${px(v)}" y2="196" stroke="#000"/><text x="${px(v)}" y="216" font-size="15" text-anchor="middle">${v}</text>`;
    s+=`<rect x="${px(Math.max(lo,0))}" y="60" width="${px(hi)-px(Math.max(lo,0))}" height="125" fill="#1f5fbf" fill-opacity=".06"/>`;
    [[lo,'lower fence'],[hi,'upper fence']].forEach(([v,l],k)=>{if(v<0)return;s+=`<line x1="${px(v)}" y1="52" x2="${px(v)}" y2="190" stroke="#1f5fbf" stroke-width="2" stroke-dasharray="6 5"/><text x="${px(v)+(k?4:-4)}" y="246" font-size="13" fill="#1f5fbf" text-anchor="${k?'start':'end'}">${l} ${Math.round(v)}</text>`});
    d.forEach(v=>{const o=v<lo||v>hi,me=v===X;s+=`<circle cx="${px(v)}" cy="${me?145:170}" r="${me?11:8}" fill="${o?'#d00000':(me?'#fff':'#555')}" stroke="${me?'#d00000':'none'}" stroke-width="3"/>`});
    s+=`<line x1="${px(med)}" y1="30" x2="${px(med)}" y2="185" stroke="#000" stroke-width="4"/><text x="${px(med)}" y="22" font-size="16" font-weight="bold" text-anchor="middle">median</text>`;
    s+=`<line x1="${px(mean)}" y1="48" x2="${px(mean)}" y2="185" stroke="#d00000" stroke-width="4" stroke-dasharray="8 5"/><text x="${px(mean)+(mean>=med?8:-8)}" y="44" font-size="16" font-weight="bold" fill="#d00000" text-anchor="${mean>=med?'start':'end'}">mean</text>`;
    if(Math.abs(mean-med)>15)s+=`<line x1="${px(med)}" y1="100" x2="${px(mean)}" y2="100" stroke="#d00000" stroke-width="2.5" marker-end="url(#zar)"/>`;
    sv.innerHTML=`<defs><marker id="zar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#d00000"/></marker></defs>`+s;
    const out=X<lo||X>hi,fmt=v=>'$'+Math.round(v)+'k';
    O.innerHTML=`Changed sale: <b>${fmt(X)}</b><br><span style="border-top:4px solid #000;display:inline-block;width:28px;vertical-align:middle"></span> Median = <b>${fmt(med)}</b><br><span style="border-top:4px dashed #d00000;display:inline-block;width:28px;vertical-align:middle"></span> Mean = <b style="color:#d00000">${fmt(mean)}</b> <span style="font-size:16px">(${mean>=med?'+':'−'}${fmt(Math.abs(mean-med)).slice(1)} from the median)</span><br>`+
      `Fences: <b>${fmt(Math.max(lo,0))}</b> to <b>${fmt(hi)}</b><br>`+(out?`<span class="ol">${fmt(X)} is an outlier: use the median.</span>`:(Math.abs(mean-med)>=25?`<b style="color:#a06b00">No outlier yet, but the data are skewed and the mean is being pulled. The median is safer.</b>`:`<b>Symmetric, no outlier: mean ≈ median, either can be used.</b>`));
    O.innerHTML=O.innerHTML.replace(/\$(\d)/g,'&#36;$1')};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();r.value=b.dataset.v;draw()});draw()});


// ---- fit: working columns never overflow, tables and stem plots fit their box
function zfit(){document.querySelectorAll('.slide.z').forEach(sl=>{const was=sl.classList.contains('on');sl.classList.add('on');const hid=[...sl.querySelectorAll('.st:not(.show)')];hid.forEach(x=>x.style.opacity=0);sl.querySelectorAll('.st').forEach(x=>x.classList.add('zmeasure'));
  const ov=e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2;
  sl.querySelectorAll('.zw').forEach(w=>{let g=0;const L=[...w.querySelectorAll('.st.zs')];while(ov(w)&&g<40){g++;L.forEach(q=>{const f=parseFloat(getComputedStyle(q).fontSize);if(f>19)q.style.fontSize=(f*0.96)+'px'})}});
  sl.querySelectorAll('.zfig').forEach(fg=>{fg.querySelectorAll('table').forEach(t=>{let g=0;const fs=()=>parseFloat(getComputedStyle(t).fontSize);while(((t.offsetWidth>fg.clientWidth-8&&fs()>10)||(!fg.classList.contains('zmcq')&&fg.scrollHeight>fg.clientHeight+2&&fs()>16))&&g<60){g++;t.style.fontSize=(fs()*0.94)+'px'}})});
  sl.querySelectorAll('.zmcq').forEach(fg=>{let g=0;const q=fg.querySelector('.zq');while(fg.scrollHeight>fg.clientHeight+2&&g<20){g++;q.style.fontSize=(parseFloat(getComputedStyle(q).fontSize)*0.95)+'px';fg.querySelectorAll('svg').forEach(v=>v.style.maxHeight=(v.getBoundingClientRect().height*0.94)+'px')}});
  sl.querySelectorAll('.top>.q').forEach(q=>{q.querySelectorAll('table').forEach(t=>{let g=0;while(t.offsetWidth>q.clientWidth&&g<30){g++;t.style.fontSize=(parseFloat(getComputedStyle(t).fontSize)*0.94)+'px'}})});
  sl.querySelectorAll('.st').forEach(x=>x.classList.remove('zmeasure'));hid.forEach(x=>x.style.opacity='');if(!was)sl.classList.remove('on')})}
document.fonts.ready.then(()=>setTimeout(zfit,700));

// check-in ticks
document.querySelectorAll('.zcb').forEach(b=>b.onclick=e=>{e.stopPropagation();b.classList.toggle('s1')});
document.querySelectorAll('.zct').forEach(b=>{b.onclick=e=>{e.stopPropagation();b.textContent=+b.textContent+1};b.oncontextmenu=e=>{e.preventDefault();e.stopPropagation();b.textContent=Math.max(0,+b.textContent-1)}});
// timer
document.querySelectorAll('.ztime').forEach(t=>{let left=+t.dataset.s,h=null;const sh=()=>{t.textContent=String(Math.floor(left/60)).padStart(2,'0')+':'+String(left%60).padStart(2,'0');t.classList.toggle('low',left<=120)};
  t.parentNode.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();const a=b.dataset.a;clearInterval(h);h=null;
    if(a==='go')h=setInterval(()=>{left=Math.max(0,left-1);sh();if(!left)clearInterval(h)},1000);if(a==='reset'){left=+t.dataset.s;sh()}})});
// CAS tabs
document.querySelectorAll('.ztabs').forEach(tb=>tb.querySelectorAll('button').forEach(b=>b.onclick=e=>{e.stopPropagation();tb.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));
  tb.parentNode.querySelectorAll('.zcas').forEach(o=>o.hidden=o.dataset.c!==b.dataset.c)}));
</script>'''

import re
CFUD=open(os.path.join(SH,'cfu.json')).read()
JS=JS.replace('__CFU__',CFUD)
def cfu_of(x):
    h=x[:120]
    if 'k-exam' in h: return 'mc'
    if 'k-exit' in h or 'k-yt' in h or 'k-apk' in h: return 'qw'
    if 'k-ex' in h or 'k-cas' in h: return 'cold'
    if ' nl' in h: return 'disc'
    if ' chk' in h: return 'tps'
    return ''
S=[x.replace('<section class="slide','<section data-cfu="%s" class="slide' % cfu_of(x),1) if cfu_of(x) else x for x in S]
out = HEAD.replace('</head>', CSS + '</head>') + '\n'.join(S) + TAIL.replace('</body>', JS + '</body>')
open(OUT, 'w').write(out)
print(len(S), 'slides', len(out))
