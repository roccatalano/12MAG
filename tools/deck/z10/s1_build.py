r"""12MAG S1 (1A Types of data, 1B Categorical data) rebuilt in the 10MA slide house style.
Shell (CSS + navigation/tile engine JS) copied from 10MA '10MAG Univariate Statistics - Slides.html'.
python3 s1_build.py  ->  lessons/S1-slides-v2.html
"""
import json, html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SH = os.path.join(HERE, "shell")
OUT = os.path.join(HERE, "..", "..", "..", "lessons", "S1-slides-v2.html")
HEAD = open(os.path.join(SH,'head.html')).read().replace('10MAG Univariate Statistics · Slides', '12MAG S1 · Types of data and categorical data · Slides')
TAIL = open(os.path.join(SH,'tail.html')).read()
CG = 'Cambridge General Mathematics Units 3&amp;4'
ED = 'Edrolo General Mathematics Units 3&amp;4'
SUB = '1A Types of data · 1B Categorical data'
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
def stem(id_, rows, key, head=('Stem', 'Leaf')):
    k = 0; tr = ''
    for s, leaves in rows:
        cells = ''
        for l in leaves.split():
            cells += f'<span class="lv" data-k="{k}">{l}</span>'; k += 1
        tr += f'<tr><td class="zst">{s}</td><td class="zlv">{cells}</td></tr>'
    return f'<div class="zstem" id="{id_}"><table><tr><th>{head[0]}</th><th>{head[1]}</th></tr>{tr}</table><div class="zkey">{key}</div></div>'
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
# S1 = 1A Types of data + 1B Categorical data. Content sources (verbatim, already cited): tools/deck/s1/build.py (old S1 deck),
# planner/unit-plan.json card gm12-u3-s1, planner/cas-skills.json 'stats-list'. % correct as in the old deck (examiner reports).
SUB = '1A Types of data · 1B Categorical data'
EDR12 = 'Edrolo General Mathematics Units 1&amp;2'
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

def ftab(id_, var, rows, total, pcth='Percentage', blank=True):
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

S.append(f'<section class="slide title cover"><h1>Types of data and categorical data</h1>'
         f'<div class="unit">12MAG · Unit 3 · AOS 1 Data analysis</div>'
         f'<div class="pp" style="font-size:22px;margin-top:14px">{CG}</div>'
         f'<ul style="list-style:none;padding:0;margin:10px 0 0;font-size:22px;line-height:1.5;text-align:left"><li>1A Types of data</li><li>1B Displaying and describing the distributions of categorical variables</li></ul><span class="pg" style="display:none"></span></section>')
LI = ['To be able to classify data as categorical or numerical.', 'To be able to further classify categorical data as nominal or ordinal.',
      'To be able to further classify numerical data as discrete or continuous.', 'To be able to construct frequency and percentage frequency tables for categorical data.',
      'To be able to construct bar charts and percentage bar charts from frequency tables.', 'To be able to interpret and describe frequency tables and bar charts.',
      'To be able to answer statistical questions about a categorical variable.']
SC = ['I can identify types of data.', 'I can construct a frequency table for categorical data.', 'I can construct a bar chart from a frequency table.',
      'I can construct a percentage segmented bar chart from a frequency table.', 'I can describe the distribution of a categorical variable.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'Types of variable · Example 1', 'Sort it', 'CAS: setting up the statistics app',
       'Frequency tables · Example 2', 'Bar charts · Example 3', 'Segmented bar charts · Example 4', 'Describing the distribution · Example 5', 'Exit tasks', 'Check-in and coursework']
S.append(f'<section class="slide z li">{bar("1A–1B", "Learning intentions")}<div class="cols" style="grid-template-columns:1.1fr 1fr .9fr">'
         f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
         f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
         f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
         f'{foot(CG + ", 1A and 1B Learning intentions; success criteria: one per worked example")}</section>')

# APK 1: Cambridge U1&2 2A #1
KI_TYPES = 'Categorical: <b>nominal</b> (names only) or <b>ordinal</b> (names and orders)<div class="kn">Numerical: <b>discrete</b> (counted) or <b>continuous</b> (measured)</div>'
S.append(qslide('apk', '1 of 3', 'Year 11 skills: types of data', 'Cambridge U1&amp;2 · 2A #1',
    'Classify the following data as nominal, ordinal, discrete or continuous:', KI_TYPES, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2A #1. Working by teacher.',
    parts=[('a', 'The time between people arriving at the coffee shop.', [], '<b>Continuous</b>: time is measured.'),
           ('b', 'The number of people in the queue at the coffee shop.', [], '<b>Discrete</b>: people are counted.'),
           ('c', 'Customer’s coffee preference (latte, cappuccino, black).', [], '<b>Nominal</b>: the categories only name the coffee.'),
           ('d', 'Customer’s rating of the coffee (excellent, quite good, not that good).', [], '<b>Ordinal</b>: the ratings have a natural order.')], cls='tight'))
# APK 2: VCAA 2021 E1 Q1 (Edrolo U1&2 1A Q13)
OPTDIST['2 of 3'] = [70, 3, 21, 4, 2]
S.append(qslide('apk', '2 of 3', 'A real VCAA question you can already do', 'VCAA 2021 Exam 1 Q1',
    'The percentage segmented bar chart provided shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).'
    '<br>The variables <i>age</i> (under 55 years, 55 years and over) and <i>preferred travel destination</i> (domestic, international) are',
    KI_TYPES, ['<i>age</i> is recorded in two groups (under 55, 55 and over), not as a number of years: categorical.',
               '<i>preferred travel destination</i>: domestic or international names a group: categorical.'],
    'both categorical variables.', EDR12 + ', 1A Q13 (VCAA 2021 Exam 1 Data analysis Q1); % from the examiner report. Chart redrawn.',
    fig=schart('a2s', [('under 55', [65, 35]), ('55 and over', [45, 55])], ['domestic', 'international'], 100, 20, 'percentage', 'age', full=True, w=520),
    figw='1.35fr', marks=1, vcaa=70, opts=[('A', 'both categorical variables.'), ('B', 'both numerical variables.'), ('C', 'a numerical variable and a categorical variable respectively.'),
    ('D', 'a categorical variable and a numerical variable respectively.'), ('E', 'a discrete variable and a continuous variable respectively.')], key='A'))
# APK 3: VCAA 2020 E1 Q10 (Edrolo U1&2 1A Q14)
NT = ('<table class="ztab"><tr><th></th><th colspan="2"><i>snores</i></th><th></th></tr><tr><th><i>frequency of nightmares</i></th><th>no</th><th>yes</th><th>total</th></tr>'
      '<tr><td>low</td><td>80</td><td>58</td><td>138</td></tr><tr><td>high</td><td>11</td><td>12</td><td>23</td></tr><tr><td>total</td><td>91</td><td>70</td><td>161</td></tr></table>')
OPTDIST['3 of 3'] = [57, 5, 3, 24, 11]
S.append(qslide('apk', '3 of 3', 'And another', 'VCAA 2020 Exam 1 Q10',
    'The data in the table shown was collected in a study of the association between the variables <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes).'
    + NT + 'The variables in this study, <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes), are',
    KI_TYPES, ['<i>frequency of nightmares</i>: low and high have a natural order: ordinal.', '<i>snores</i>: no and yes only name a group: nominal.'],
    'ordinal and nominal respectively.', EDR12 + ', 1A Q14 (VCAA 2020 Exam 1 Data analysis Q10); % from the examiner report.',
    figw='1.15fr', marks=1, vcaa=57, opts=[('A', 'ordinal and nominal respectively.'), ('B', 'nominal and ordinal respectively.'), ('C', 'both numerical.'), ('D', 'both ordinal.'), ('E', 'both nominal.')], key='A'))

# Key ideas
KD = [('Categorical variable', 'names a quality or group: <b>nominal</b> (names only) or <b>ordinal</b> (names and orders)'),
      ('Numerical variable', 'a quantity: <b>discrete</b> (counted, ‘How many?’) or <b>continuous</b> (measured, ‘How much?’)'),
      ('Frequency table', 'lists each category and how often it occurs: as a number and as a percentage'),
      ('Bar chart', 'one bar per category, with gaps; height = frequency'),
      ('Percentage segmented bar chart', 'one 100% bar, a segment per category, with a legend'),
      ('Mode (modal category)', 'the category that occurs most often: the tallest bar or longest segment')]
KF = [('Percentage frequency', r'$\dfrac{\text{number in the category}}{\text{total}} \times 100\%$'),
      ('Number from a percentage', r'$\text{number} = \dfrac{\text{percentage}}{100} \times \text{total}$'),
      ('Segmented bar', 'each segment ends at the previous end + its %'),
      ('Majority', 'only when the mode is more than 50%; otherwise ‘the most common’')]
S.append(f'<section class="slide z kif">{bar("1A–1B", "Key ideas")}<div class="cols" style="grid-template-columns:1.1fr .9fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1A pp. 2–4 and 1B pp. 7–10")}</section>')

# NL: types of variable (tree, top-down, one branch at a time)
def tb(t, sub, pos, c=''): return st(f'<b>{t}</b><i class="zsub">{sub}</i>', cls=f'ztb {c}" style="grid-area:{pos}')
TREE = ('<div class="ztree"><div class="ztb ztop" style="grid-area:1/1/2/5"><b>Variable</b></div>'
        + tb('Categorical', 'names a quality or group', '2/1/3/3', 'zcat') + tb('Nominal', 'names only · e.g. eye colour', '3/1/4/2', 'zcat') + tb('Ordinal', 'names <i>and</i> orders · e.g. fitness level', '3/2/4/3', 'zcat')
        + tb('Numerical', 'a quantity: counted or measured', '2/3/3/5', 'znum') + tb('Discrete', '‘How many?’ counted · e.g. cars', '3/3/4/4', 'znum') + tb('Continuous', '‘How much?’ measured · e.g. weight', '3/4/4/5', 'znum') + '</div>')
S.append(nl_slide('Types of variable',
    'Categorical data put people into groups. Numerical data are quantities you can do arithmetic with. <span class="hint">Click to build the tree.</span>',
    TREE + st('<b>Not sure? Two tests.</b> 1 · Does an average make sense? (average weight ✓ numerical; average house number ✗ categorical) &nbsp; 2 · How was it recorded? (weight in kg: numerical; ‘underweight’, ‘normal’, ‘overweight’: categorical)', True, cls='ztest'),
    CG + ', 1A pp. 2–4'))

def split2(h):
    # two working columns: everything from the part marked <span class="cbk"> goes in the right column
    i = h.index('<div class="zw">') + len('<div class="zw">'); j = h.rfind('<div class="zpq', 0, h.index('cbk')); e = h.index('</div></div><div class="foot"')
    return h[:i] + '<div class="zc2"><div>' + h[i:j] + '</div><div>' + h[j:e].replace(' sep"', '"', 1) + '</div></div>' + h[e:]
# Example 1
S.append(split2(qslide('ex', 1, 'Types of data', 'Cambridge · Example 1',
    'Classify the following data as nominal, ordinal, discrete or continuous.', KI_TYPES, [], None, CG + ', 1A Example 1 (p. 4)',
    parts=[('a', 'The number of chocolate chips in each of 10 cookies is counted.', [], '<b>Discrete</b>: the number of chips can only be a whole number.'),
           ('b', 'The time taken for 20 students to complete a puzzle is recorded in seconds.', [], '<b>Continuous</b>: time can take any value, limited only by how accurately it is measured.'),
           ('c', 'Member of a football club were asked to rate how they felt about the current coach, 1 = Very satisfied, 2 = Satisfied, 3 = Indifferent, 4 = Dissatisfied, 5 = Very dissatisfied.', [], '<b>Ordinal</b>: the numbers are not quantities; they rank how much each person approves of the coach.'),
           ('d', '<span class="cbk"></span>Students are asked to each choose their preferred colour from the list 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow.', [], '<b>Nominal</b>: the numbers are not quantities; they just name colours.'),
           ('e', 'Students weights were classified as ‘less than 60kg’, ‘60kg - 80kg’ or ‘more than 80kg’.', [], '<b>Ordinal</b>: weight was recorded in three groups that can be ordered.')], cls='tight ex1x')))
# You try 1: Edrolo 1A WE1-3
S.append(split2(qslide('yt', 1, 'Types of data', 'Edrolo 1A WE1, WE2, WE3',
    'Three short questions. Classify each variable.', KI_TYPES, [], None, ED + ', 1A Worked examples 1, 2 and 3 (pp. 2–4). Working by teacher.',
    parts=[('1', 'Classify the following variables as either categorical or numerical.<br><b>a.</b> <i>type of pasta</i> &nbsp; <b>b.</b> <i>number of candles</i>', ['a. grouped into pasta types · b. candles are counted'], '<b>a.</b> Categorical &nbsp; <b>b.</b> Numerical'),
           ('2', 'Classify the following categorical variables as either nominal or ordinal.<br><b>a.</b> <i>type of shoe</i> (runners, boots, sandals, slides) &nbsp; <b>b.</b> <i>shirt size</i> (small, medium, large)', ['a. no natural order · b. small → medium → large'], '<b>a.</b> Nominal &nbsp; <b>b.</b> Ordinal'),
           ('3', '<span class="cbk"></span>Classify the following numerical variables as either discrete or continuous.<br><b>a.</b> <i>length</i> (m) &nbsp; <b>b.</b> <i>number of tennis racquets</i>', ['a. measured · b. counted'], '<b>a.</b> Continuous &nbsp; <b>b.</b> Discrete')], cls='tight')))
# Sort it (interactive): the APK and You try items, verbatim
SORT = [('<i>type of pasta</i>', 'Nominal'), ('<i>number of candles</i>', 'Discrete'), ('<i>type of shoe</i> (runners, boots, sandals, slides)', 'Nominal'),
        ('<i>shirt size</i> (small, medium, large)', 'Ordinal'), ('<i>length</i> (m)', 'Continuous'), ('<i>number of tennis racquets</i>', 'Discrete'),
        ('The time between people arriving at the coffee shop.', 'Continuous'), ('The number of people in the queue at the coffee shop.', 'Discrete'),
        ('Customer’s coffee preference (latte, cappuccino, black).', 'Nominal'), ('Customer’s rating of the coffee (excellent, quite good, not that good).', 'Ordinal'),
        ('<i>frequency of nightmares</i> (low, high)', 'Ordinal'), ('<i>snores</i> (no, yes)', 'Nominal')]
CARDS = ''.join(f'<div class="card ix" data-a="{a}"><div class="ct">{t}</div><div class="cb">' + ''.join(f'<button data-v="{v}">{v}</button>' for v in ('Nominal', 'Ordinal', 'Discrete', 'Continuous')) + '</div></div>' for t, a in SORT)
S.append(f'<section class="slide z nl sort">{bar("New learning", "Sort it: what type of data?")}'
         '<p class="lead zlead">Every variable from today’s questions so far. Click the type for each card: green = right, red = try again. <span class="score ix">Correct: <b>0</b> / 12 <button class="reset">↺ Reset</button></span></p>'
         f'<div class="cards c12">{CARDS}</div>{foot("Items verbatim from Cambridge U1&amp;2 2A #1, " + ED + " 1A Worked examples 1–3 and VCAA 2020 Exam 1 Q10")}</section>')

# CAS: setting up the statistics app (planner/cas-skills.json: stats-list)
CS = [x for x in json.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if x['id'] == 'stats-list'][0]
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CS["ti"])}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CS["classpad"])}</ol></div></div>').replace('class="zcas2"','class="zcas2 zsm"')
SURV = table_hl('surv', [('Height (cm)', '173 179 167 195 173 184 175 140'.split()), ('Weight (kg)', '57 58 62 84 64 74 60 50'.split()), ('Age (years)', '18 19 18 18 18 22 19 34'.split()),
                         ('Study mode', 'C C C O C O O C'.split()), ('Fitness level', '2 2 1 1 3 3 3 3'.split()), ('Pulse rate (beats/min)', '86 82 96 71 90 78 88 70'.split())], 'ztab zsm2')
S.append(qslide('cas', '', 'Setting up the statistics app', 'Cambridge · 1A survey data',
    'A university survey of eight students (Study mode: C = on-campus, O = online; Fitness level: 1 = high, 2 = medium, 3 = low).' + SURV
    + 'Enter the <i>height</i> data into a list named <b>height</b>.',
    'Only <b>numerical</b> variables go into a list you calculate with.<div class="kn">Check: rows filled = number of data values.</div>',
    [('Name the list <i>height</i> (top cell).', 'tc:surv:0,1,2,3,4,5,6,7'), 'Enter the 8 heights down the list.', 'Check: 8 rows filled = 8 students.'],
    'The list <b>height</b> holds 8 values, ready for one-variable statistics (1D onwards).',
    CG + ', 1A p. 2 (survey data); the task is the teacher’s. CAS steps: planner CAS guide (stats-list).', fig=TABS, figw='1fr'))

# NL: raw data -> frequency table (study mode of 60 students)
STUDY = 'O O C O O O C O C C C O C O O O C C C O C O C O C C C O C O C O C O O O C O C O C O O O O O O C C O C O O O C O C C C O'.split()
SM = [('on-campus', 27, '45.0'), ('online', 33, '55.0')]
S.append(nl_slide('From raw data to a frequency table',
    'A <b>frequency table</b> lists each category and how often it occurs: as a number and as a percentage. Here: the <i>study mode</i> (C = on-campus, O = online) of 60 students. <span class="hint">Click to build the table.</span>',
    '<div class="cols" style="grid-template-columns:1.2fr 1fr"><div class="col">' + chips('sm', STUDY) + '</div><div class="col">' + ftab('smt', '<i>study mode</i>', SM, (60, '100.0'), '%')
    + st('Count the C’s: <b>27</b> on-campus', do='hv:sm:C:hb tf:smt:n0', cls='stp') + st('Count the O’s: <b>33</b> online', do='hv:sm:O:hy tf:smt:n1', cls='stp')
    + st('Total: 27 + 33 = <b>60</b>', do='tf:smt:nT', cls='stp') + st(r'% on-campus $= \dfrac{27}{60} \times 100\% = 45.0\%$', do='tf:smt:p0', cls='stp')
    + st(r'% online $= \dfrac{33}{60} \times 100\% = 55.0\%$', do='tf:smt:p1', cls='stp') + st('Check: 45.0 + 55.0 = <b>100.0%</b>', do='tf:smt:pT', cls='stp') + '</div></div>',
    CG + ', 1B p. 7 (study mode of 60 students)', 'eng'))
# Example 2
ICE = 'C V V C C V C C C V V'.split()
S.append(qslide('ex', 2, 'Constructing a frequency table for a categorical variable', 'Cambridge · Example 2',
    'A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):' + chips('ice', ICE) + 'Construct a frequency table (including percentage frequencies) to display the data.',
    r'Percentage frequency $= \dfrac{\text{number}}{\text{total}} \times 100\%$',
    [('Count chocolate: 6', 'hv:ice:C:hb tf:ict:n0'), ('Count vanilla: 5', 'hv:ice:V:hy tf:ict:n1'), ('Total: 6 + 5 = 11', 'tf:ict:nT'),
     (r'% chocolate $= \dfrac{6}{11} \times 100\% = 54.5\%$', 'tf:ict:p0'), (r'% vanilla $= \dfrac{5}{11} \times 100\% = 45.5\%$', 'tf:ict:p1'), ('Check: 54.5 + 45.5 = 100.0', 'tf:ict:pT')],
    'The completed table (opposite).', CG + ', 1B Example 2 (p. 7)', cls='tight',
    fig=ftab('ict', 'Flavour', [('chocolate', 6, '54.5'), ('vanilla', 5, '45.5')], (11, '100.0')), figw='1fr'))
# You try 2: Edrolo 1B WE1
TH = 'average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'.split()
S.append(qslide('yt', 2, 'Constructing a frequency table', 'Edrolo 1B WE1',
    'The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:<br>'
    + chips('th', TH) + 'Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.',
    r'Percentage frequency $= \dfrac{\text{number}}{\text{total}} \times 100\%$',
    [('short: 6 · average: 10 · tall: 8', 'hv:th:short:hy hv:th:average:hb hv:th:tall:hg tf:tht:n0,n1,n2'), ('Total: 6 + 10 + 8 = 24', 'tf:tht:nT'),
     (r'$\dfrac{6}{24} \times 100 = 25.0$, $\dfrac{10}{24} \times 100 = 41.7$, $\dfrac{8}{24} \times 100 = 33.3$', 'tf:tht:p0,p1,p2'), ('Check: 25.0 + 41.7 + 33.3 = 100.0', 'tf:tht:pT')],
    'The completed table (opposite).', ED + ', 1B Worked example 1 (pp. 9–10). Working by teacher.',
    fig=ftab('tht', 'teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), '%'), figw='.8fr', cls='tight'))

# NL: frequency table -> bar chart
S.append(nl_slide('The bar chart: frequency table → graph',
    'One bar per category, gaps between the bars, height = frequency. <span class="hint">Click to draw it.</span>',
    '<div class="cols" style="grid-template-columns:.8fr 1.2fr"><div class="col">' + ftab('bct', '<i>study mode</i>', SM, (60, '100.0'), '%', blank=False)
    + st('<b>1</b> Axes: <i>study mode</i> across, <i>Frequency</i> up (to 35).', do='ax:bc', cls='stp') + st('<b>2</b> on-campus: a bar 27 high.', do='hr:bct:0 bg:bc:0', cls='stp')
    + st('<b>3</b> online: a bar 33 high, with a gap.', do='hr:bct:1 bg:bc:1', cls='stp') + '</div><div class="col zc">'
    + bchart('bc', ['on-campus', 'online'], [27, 33], 35, 5, 'study mode', 'Frequency') + '</div></div>', CG + ', 1B pp. 7–8 (study mode of 60 students)'))
# Example 3
CLIMR = [('Cold', 3, '13.0'), ('Mild', 14, '60.9'), ('Hot', 6, '26.1')]
S.append(qslide('ex', 3, 'Constructing a bar chart from a frequency table', 'Cambridge · Example 3',
    'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.',
    'One bar per category, <b>gaps</b> between bars<div class="kn">label both axes</div>', [], None, CG + ', 1B Example 3 (p. 8)',
    parts=[('a', 'What is the level of measurement of the variable <i>climate type</i>?', ['cold, mild, hot can be put in a natural order of ‘warmth’.'], '<b>Ordinal</b>'),
           ('b', 'Construct a frequency bar chart to display this information.', [('Axes: <i>Climate type</i> across; <i>Frequency</i> up, scaled to 15.', 'ax:e3'),
             ('Cold 3, Mild 14, Hot 6: one bar each, with gaps.', 'hr:e3t:0,1,2 bg:e3:0,1,2')], 'The bar chart opposite.', 'ax:e3 bg:e3:0,1,2')],
    fig='<div class="zrowc">' + ftab('e3t', 'Climate type', CLIMR, (23, '100.0'), blank=False) + bchart('e3', ['Cold', 'Mild', 'Hot'], [3, 14, 6], 15, 5, 'Climate type', 'Frequency', h=320) + '</div>', figw='1.6fr', cls='tight'))
# You try 3: Edrolo 1B WE2
THR = [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')]
S.append(qslide('yt', 3, 'Constructing a bar chart', 'Edrolo 1B WE2',
    '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.<br>Use the frequency table to construct a frequency bar chart.',
    'One bar per category, <b>gaps</b> between bars<div class="kn">label both axes</div>',
    [('Axes: <i>teacher’s height</i> across; <i>frequency</i> up to 10.', 'ax:y3'), ('short 6, average 10, tall 8: one bar each, with gaps.', 'hr:y3t:0,1,2 bg:y3:0,1,2')],
    'The bar chart opposite.', ED + ', 1B Worked example 2 (p. 11). Working by teacher.',
    fig='<div class="zrowc">' + ftab('y3t', 'teacher’s height', THR, (24, '100.0'), '%', blank=False) + bchart('y3', ['short', 'average', 'tall'], [6, 10, 8], 10, 2, 'teacher’s height', 'frequency', h=320) + '</div>', figw='1.6fr', ans_do='ax:y3 bg:y3:0,1,2'))

# NL: segmented bar chart, modelled as a transformation (bars -> one stacked bar -> 100% bar)
def morph_svg(id_):
    """Three bars (Cold 3, Mild 14, Hot 6) that the JS (op mo:id:stage) slides into one stack, then rescales to 100%."""
    W_, H_ = 600, 520; X0, Y0, Y1 = 92, 450, 40
    t = '<g class="mof">' + ''.join(f'<line x1="{X0-7}" y1="{Y0-y/24*(Y0-Y1):.1f}" x2="{X0}" y2="{Y0-y/24*(Y0-Y1):.1f}" stroke="#000" stroke-width="2"/><text x="{X0-12}" y="{Y0-y/24*(Y0-Y1)+8:.1f}" font-size="22" text-anchor="end">{y}</text>' for y in range(0, 25, 4))
    t += f'<text transform="translate(26 {(Y0+Y1)/2}) rotate(-90)" font-size="24" text-anchor="middle" font-style="italic">Frequency</text></g>'
    t += '<g class="mop">' + ''.join(f'<line x1="{X0-7}" y1="{Y0-y/100*(Y0-Y1):.1f}" x2="{X0}" y2="{Y0-y/100*(Y0-Y1):.1f}" stroke="#000" stroke-width="2"/><text x="{X0-12}" y="{Y0-y/100*(Y0-Y1)+8:.1f}" font-size="22" text-anchor="end">{y}</text>' for y in range(0, 101, 20))
    t += f'<text transform="translate(26 {(Y0+Y1)/2}) rotate(-90)" font-size="24" text-anchor="middle" font-style="italic">Percentage (%)</text></g>'
    ax = f'<line x1="{X0}" y1="{Y0}" x2="{W_-150}" y2="{Y0}" stroke="#000" stroke-width="2.5"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1-10}" stroke="#000" stroke-width="2.5"/>'
    names = ['Cold', 'Mild', 'Hot']
    cl = '<g class="mocat">' + ''.join(f'<text class="moc" data-i="{i}" x="0" y="{Y0+30}" font-size="22" text-anchor="middle">{n}</text>' for i, n in enumerate(names)) + '</g>'
    cl += f'<text class="moxl" x="{(X0+W_-150)/2}" y="{Y0+62}" font-size="22" text-anchor="middle" font-style="italic">Climate type</text>'
    r = ''.join(f'<rect class="mor" data-i="{i}" fill="{COL[i]}" stroke="#000" stroke-width="2.5"/>' for i in range(3))
    lb = ''.join(f'<text class="mol" data-i="{i}" font-size="23" font-weight="bold" text-anchor="middle"></text>' for i in range(3))
    lg = '<g class="molg">' + ''.join(f'<rect x="{W_-120}" y="{Y1+40+k*40}" width="26" height="26" fill="{COL[2-k]}" stroke="#000" stroke-width="2"/><text x="{W_-84}" y="{Y1+62+k*40}" font-size="23">{names[2-k]}</text>' for k in range(3)) + '</g>'
    return f'<svg class="zmorph" id="{id_}" viewBox="0 0 {W_} {H_}" data-g="{X0},{Y0},{Y1},{W_-150}">{t}{ax}{cl}{r}{lb}{lg}</svg>'
S.append(nl_slide('From a bar chart to a percentage segmented bar chart',
    'Start with the bar chart. Stack the bars into <b>one bar</b>, then change to percentages so the bar is exactly 100% tall. <span class="hint">Click to transform.</span>',
    '<div class="cols zmo2" style="grid-template-columns:.85fr 1.15fr"><div class="col">' + ftab('sgt', 'Climate type', CLIMR, (23, '100.0'), blank=False)
    + st('<b>1</b> Stack into one bar: Cold at the bottom, then Mild, then Hot. Total 3 + 14 + 6 = 23.', do='mo:sgm:1', cls='stp')
    + st('<b>2</b> Axis to percentage: 23 becomes 100%. Cold 13.0%, Mild 60.9%, Hot 26.1%.', do='mo:sgm:2', cls='stp')
    + st('<b>3</b> Segments end at 13.0, 13.0 + 60.9 = 73.9 and 100. Add a legend.', do='mo:sgm:3', cls='stp')
    + st('<b>4</b> The longest segment is the mode: Mild.', do='mo:sgm:3 hr:sgt:1', cls='stp') + '</div><div class="col zc">'
    + morph_svg('sgm') + '</div></div>', CG + ', 1B pp. 8–9 (climate data, Example 3)'))
# Example 4
S.append(qslide('ex', 4, 'Constructing a percentage segmented bar chart', 'Cambridge · Example 4',
    'The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’.<br>Construct a percentage frequency segmented bar chart to display this information.',
    'Each segment ends at the <b>previous end + its %</b><div class="kn">the bar is 100% tall; add a legend</div>',
    [('Axes: vertical axis <i>Percentage</i>, 0 to 100 in tens.', 'ax:e4'), ('Cold: from 0 to 13.0%', 'hr:e4t:0 bg:e4:0'), ('Mild: from 13.0 to 13.0 + 60.9 = 73.9%', 'hr:e4t:1 bg:e4:1'),
     ('Hot: from 73.9 to 100%; add the legend', 'hr:e4t:2 bg:e4:2 lg:e4')],
    'The percentage segmented bar chart opposite.', CG + ', 1B Example 4 (p. 9)',
    fig='<div class="zrowc">' + ftab('e4t', 'Climate type', CLIMR, (23, '100.0'), blank=False) + schart('e4', [('', [13.0, 60.9, 26.1])], ['Cold', 'Mild', 'Hot'], 100, 10, 'Percentage', w=330, h=340) + '</div>', figw='1.6fr'))
# You try 4: Edrolo 1B WE3, three columns: question + table | part a + chart a | part b + chart b
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
_n4 = ['short', 'average', 'tall']
_y4a = [W('Axes: <i>frequency</i> 0 to 24.', 'ax:y4a'), W('short: 0 to 6', 'ax:y4a bg:y4a:0'), W('average: 6 to 6 + 10 = 16', 'ax:y4a bg:y4a:0,1'),
        W('tall: 16 to 16 + 8 = 24', 'ax:y4a bg:y4a:0,1,2'), W('Add the legend.', 'ax:y4a bg:y4a:0,1,2 lg:y4a')]
_y4b = [W('Axes: <i>percentage</i> 0 to 100.', 'ax:y4b'), W('short: 0 to 25%', 'ax:y4b bg:y4b:0'), W('average: 25 to 25 + 41.7 = 66.7%', 'ax:y4b bg:y4b:0,1'),
        W('tall: 66.7 to 66.7 + 33.3 = 100%', 'ax:y4b bg:y4b:0,1,2'), W('Add the legend.', 'ax:y4b bg:y4b:0,1,2 lg:y4b')]
S.append('<section class="slide z ex yt k-yt yt4">'
    + '<div class="bar ytb"><span class="tag">You try 4</span><h1>Constructing segmented bar charts</h1><span class="sub zpill">Edrolo 1B WE3</span></div>'
    + '<div class="zb" style="grid-template-columns:.9fr 1fr 1fr">'
    + '<div class="zw y4q"><div class="q">24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.</div>'
    + ftab('y4t', 'teacher’s height', THR, (24, '100.0'), '%', blank=False)
    + ki('Key idea', 'Each segment ends at the <b>previous end + its value</b><div class="kn">add a legend</div>') + '</div>'
    + '<div class="zw y4p"><div class="zpq"><b>a</b> Use the frequency table to construct a segmented bar chart.</div>' + ''.join(_y4a)
    + st('<span class="zok">✓ Answer</span> Segmented bar chart: short 0–6, average 6–16, tall 16–24, with a legend', True, do='ax:y4a bg:y4a:0,1,2 lg:y4a', cls='zpa')
    + schart_big('y4a', [6, 10, 8], _n4, 24, 4, 'frequency', ['6', '16', '24']) + '</div>'
    + '<div class="zw y4p"><div class="zpq"><b>b</b> Use the frequency table to construct a percentage segmented bar chart.</div>' + ''.join(_y4b)
    + st('<span class="zok">✓ Answer</span> Percentage segmented bar chart: short 0–25%, average 25–66.7%, tall 66.7–100%, with a legend', True, do='ax:y4b bg:y4b:0,1,2 lg:y4b', cls='zpa')
    + schart_big('y4b', [25, 41.7, 33.3], _n4, 100, 20, 'percentage (%)', ['25%', '66.7%', '100%']) + '</div>'
    + '</div>' + foot(ED + ', 1B Worked example 3 (pp. 12–13). Working by teacher.') + '</section>')

# NL: describing the distribution
SREP = report('srep', ['The ', ('a0', '<i>study mode</i>'), ' of ', ('a1', '60'), ' students were classified as being ', ('a2', '‘on-campus’ or ‘online’'), '. The ', ('b0', 'majority'),
                       ' of the students, ', ('b1', '55.0%'), ', were found to ', ('b2', 'study online'), '. Of the remaining students, ', ('c0', '45.0%'), ' were found to ', ('c1', 'study on-campus'), '.'])
S.append(nl_slide('Describing the distribution of a categorical variable',
    'A report gives <b>1</b> the context and how many, <b>2</b> the modal category with its %, <b>3</b> the percentages for the others. <span class="hint">Click to fill the report.</span>',
    '<div class="cols" style="grid-template-columns:.75fr 1.25fr"><div class="col">' + ftab('drt', '<i>study mode</i>', SM, (60, '100.0'), '%', blank=False)
    + '<p class="zsc" style="font-size:19px">‘Majority’ only when the mode is more than 50%; otherwise ‘the most common’.</p></div><div class="col">' + SREP
    + st('<b>1</b> Context: 60 students, on-campus or online.', do='tf:srep:a0,a1,a2 hr:drt:2', cls='stp') + st('<b>2</b> Mode: online, 55.0%: more than 50%, so ‘the majority’.', do='tf:srep:b0,b1,b2 hr:drt:1', cls='stp')
    + st('<b>3</b> The others: on-campus 45.0%.', do='tf:srep:c0,c1 hr:drt:0', cls='stp') + '</div></div>', CG + ', 1B pp. 9–10 (report guidelines; study mode data p. 7)'))
# Example 5
WREP = report('e5r', ['The ', ('a0', 'climate types'), ' of ', ('a1', '23'), ' countries were classified as being ', ('a2', '‘cold’, ‘mild’ or ‘hot’'), '. The ', ('b0', 'majority'), ' of the countries, ', ('b1', '60.9%'),
                      ', were found to ', ('b2', 'have a mild climate'), '. Of the remaining countries, ', ('c0', '26.1%'), ' were found to ', ('c1', 'have a hot climate'), ', while ', ('c2', '13.0%'), ' were found to ', ('c3', 'have a cold climate'), '.'])
S.append(qslide('ex', 5, 'Describing the distribution of a categorical variable', 'Cambridge · Example 5',
    'In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages.<br>Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.',
    'Context → mode with its % → the others<div class="kn">‘majority’ only if the mode is over 50%</div>',
    [('Context: 23 countries; cold, mild or hot.', 'hr:e5t:3 tf:e5r:a0,a1,a2'), ('Mode: Mild, 60.9%: more than 50%, so ‘the majority’.', 'hr:e5t:1 tf:e5r:b0,b1,b2'),
     ('The others: hot 26.1%, cold 13.0%.', 'hr:e5t:0,2 tf:e5r:c0,c1,c2,c3')],
    'The report opposite.', CG + ', 1B Example 5 (pp. 10–11, report verbatim)',
    fig=ftab('e5t', 'Climate type', CLIMR, (23, '100.0'), '%', blank=False) + WREP, figw='1.1fr'))
# You try 5: Edrolo 1B WE4
YREP = report('y5r', [('a0', '24'), ' ', ('a1', 'prep students'), ' were surveyed on ', ('a2', 'how tall they thought their teacher was'), '. The ', ('b0', 'most common'), ' response was ', ('b1', 'average'),
                      ', accounting for ', ('b2', '41.7%'), ' of responses, while ', ('c0', '25%'), ' said their teacher was ', ('c1', 'short'), ', and ', ('c2', '33.3%'), ' said their teacher was ', ('c3', 'tall'), '.'])
S.append(qslide('yt', 5, 'Describing the distribution', 'Edrolo 1B WE4',
    '24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.',
    'The mode is the <b>longest segment</b><div class="kn">‘most common’ when it is under 50%</div>', [], None, ED + ', 1B Worked example 4 (p. 14). Working by teacher.',
    parts=[('a', 'Find the modal category of the data set.', ['Longest segment: average, 41.7% (short 25%, tall 33.3%).'], '<b>Average</b>'),
           ('b', 'Describe the distribution of the data set.', [('Context, then mode: average 41.7% is under 50%, so ‘the most common’.', 'tf:y5r:a0,a1,a2,b0,b1,b2'), ('The others: short 25%, tall 33.3%.', 'tf:y5r:c0,c1,c2,c3')],
            'The report under the chart.', 'tf:y5r:a0,a1,a2,b0,b1,b2,c0,c1,c2,c3')],
    fig=schart('y5s', [('', [25, 41.7, 33.3])], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', 'teacher’s height', full=True, w=340, h=280) + YREP, figw='1.1fr', cls='tight'))

# Exits
TMP = [12.7, 11.8, 10.7, 9.0, 6.0, 7.0, 4.1, 4.8, 9.2, 6.7, 7.5, 8.0, 8.6, 9.8, 7.7]
TT1 = (table_hl('x1a', [('<i>day number</i>', [str(d) for d in range(1, 9)]), ('<i>minimum temperature</i> (°C)', [str(t) for t in TMP[:8]])], 'ztab zsm2')
       + table_hl('x1b', [('<i>day number</i>', [str(d) for d in range(9, 16)]), ('<i>minimum temperature</i> (°C)', [str(t) for t in TMP[8:]])], 'ztab zsm2'))
S.append(qslide('exit', '1 of 3', 'Show what you know', 'VCAA 2019 Exam 2 Q1a',
    'The table shows the <i>day number</i> and the <i>minimum temperature</i>, in degrees Celsius, for 15 consecutive days in May 2017.' + TT1
    + 'Which of the two variables in this data set is an ordinal variable?', KI_TYPES,
    ['<i>minimum temperature</i> is measured in °C: numerical.', '<i>day number</i> labels each day and puts the days in order; you wouldn’t average it: categorical, ordinal.'],
    '<i>day number</i> is the ordinal variable.', ED + ', 1A Q14 (VCAA 2019 Exam 2 Data analysis Q1a); % from the examiner report.',
    marks=1, vcaa=83, figw='1.2fr', watch='a variable written as numbers is not automatically numerical. Ask what the numbers do: <i>day number</i> only puts the days in order. <span class="zsc">(teacher note)</span>'))
HEP = [(1, 1.76, 15.34, 41.22), (2, 1.79, 16.96, 42.41), (3, 1.83, 13.87, 46.53), (4, 1.82, 14.23, 40.53), (5, 1.87, 13.78, 40.62), (6, 1.73, 14.50, 45.62), (7, 1.68, 15.08, 42.33), (8, 1.82, 13.13, 40.88),
       (9, 1.83, 14.22, 39.22), (10, 1.87, 13.62, 42.51), (11, 1.87, 12.01, 42.75), (12, 1.80, 12.88, 38.12), (13, 1.83, 12.68, 42.65), (14, 1.87, 12.45, 41.32), (15, 1.78, 11.31, 42.88)]
HT = lambda rows: ('<table class="ztab zhep"><tr><th><i>athlete number</i></th><th><i>high jump</i> (metres)</th><th><i>shot-put</i> (metres)</th><th><i>javelin</i> (metres)</th></tr>'
                   + ''.join(f'<tr><td>{a}</td><td>{b:.2f}</td><td>{c:.2f}</td><td>{d:.2f}</td></tr>' for a, b, c, d in rows) + '</table>')
S.append(qslide('exit', '2 of 3', 'Show what you know', 'VCAA 2021 Exam 2 Q1a',
    'In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.'
    + f'<div class="zrowc">{HT(HEP[:8])}{HT(HEP[8:])}</div>Write down the number of numerical variables in the table.', KI_TYPES,
    ['<i>high jump</i>, <i>shot-put</i> and <i>javelin</i> are measured in metres: numerical.', '<i>athlete number</i> only names each athlete: categorical.'],
    '<b>3</b> numerical variables', ED + ', 1A Q16 (VCAA 2021 Exam 2 Data analysis Q1a); % and common error from the examiner report.',
    marks=1, vcaa=52, figw='1.35fr', watch='count the <b>variables</b> (columns), not the values. The examiners noted a common error was counting the 45 values.'))
OPTDIST['3 of 3'] = [21, 76, 2, 1, 1]
S.append(qslide('exit', '3 of 3', 'Show what you know', 'VCAA 2017 Exam 1 Q5 (adapted)',
    'A study was conducted that investigated the <i>number of moths</i> caught in a sugar moth trap (less than 250, 250–500, more than 500). The results are summarised in the percentage segmented bar chart shown.<br>There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to',
    r'$\text{number} = \dfrac{\text{percentage}}{100} \times \text{total}$',
    ['Read: the ‘less than 250’ segment runs from 0 to 30%.', r'$\dfrac{30}{100} \times 300 = 90$'],
    '90', ED + ', 1B Q13 · Adapted from VCAA 2017 Exam 1 Data analysis Q5; % from the examiner report for the original question.',
    fig=schart('x3', [('', [30, 46, 24])], ['less than 250', '250–500', 'more than 500'], 100, 10, 'frequency (%)', 'number of moths', full=True, w=400, h=260),
    figw='1.15fr', marks=1, vcaa=76, opts=[('A', '30'), ('B', '90'), ('C', '250'), ('D', '300'), ('E', '500')], key='B'))

S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
         f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot("Success criteria: one per worked example")}</section>')
CWR = open(os.path.join(SH, 'cwr.html')).read().replace('>Exercise 9A: Collecting representative data<','>Exercise 1A: Types of data<'); CWL = open(os.path.join(SH, 'cwl.html')).read()
S.append(f'<section class="slide cwk">{bar("1A–1B", "Coursework · Exercises 1A and 1B")}<div class="cwgrid"><div class="cwl2">'
         '<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>'
         '<tr><th>Cambridge Exercise 1A</th><td>Q1–6</td></tr><tr><th>Cambridge Exercise 1B</th><td>Q1–9</td></tr>'
         '<tr><th>Practice booklet</th><td>1A and 1B sections</td></tr></tbody></table>'
         '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
         f'{CWL}</div>{CWR}</div>{foot(CG + ", Exercises 1A and 1B; Chapter 1 practice booklet")}</section>')

# S1 extras: chart / table-fill / chip engines (ops ax, bg, lg, tf, hv, hr), kept inside the slides section
S[-1] += r'''<style>
svg.zch .cax,svg.zch .clg{opacity:0;transition:opacity .4s}svg.zch .cax.on,svg.zch .clg.on,svg.zch.full .cax,svg.zch.full .clg{opacity:1}
svg.zch .cbr{transform:scaleY(0);transform-box:fill-box;transform-origin:bottom;transition:transform .6s}svg.zch .cbr.on,svg.zch.full .cbr{transform:none}
.slide.z .zfig svg.zch{max-height:330px}
.zft td.l{text-align:left}.zft.zbl td{min-width:70px}.zft [data-f]{color:transparent;transition:color .3s}.zft [data-f].on{color:#d00000;font-weight:bold}
.zft.zbl td:not(.l){border-bottom:2px dashed #888}.zft tr.hl td{background:#fff2a8}
.zchips{display:flex;flex-wrap:wrap;gap:5px;justify-content:center;font-size:18px;margin:6px 0}
.zc{border:1.5px solid #000;padding:1px 7px;transition:background .3s}.zc.hb{background:#b9cff3}.zc.hy{background:#fff2a8}.zc.hg{background:#c8ebc8}
#sm .zc{min-width:30px;text-align:center;font-size:20px}
.zrep{font-size:19px;line-height:1.75;border:2px solid #000;padding:8px 12px;margin-top:10px;background:#fff}
.zrb.on{min-width:0!important}.zrb{display:inline-block;min-width:70px;border-bottom:2px dashed #888;color:transparent;transition:color .3s;line-height:1.3}.zrb.on{color:#d00000;font-weight:bold;border-bottom-color:transparent}
.ztree{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 18px;margin:16px 0}
.ztree .ztb,.ztree .st.ztb{border:3px solid #000;padding:8px 10px;text-align:center;font-size:22px!important;color:#000!important;box-shadow:4px 4px 0 #bbb;margin:0!important;white-space:normal}
.ztree .ztop{width:300px;justify-self:center}.ztree .zcat{border-color:#1f9e74!important}.ztree .znum{border-color:#2f6fdf!important}
.ztree i.zsub{display:block;font-style:normal;font-size:16px;color:#444}
.slide.z .st.ztest{font-size:20px!important;color:#000}
.zrowf svg.zch{width:270px!important;max-height:195px!important}.zrowf .ztab.zft{font-size:16px}.zrowf{align-items:center}
.zrowc .ztab.zft{font-size:14px;flex:none}.zrowc .ztab.zft td,.zrowc .ztab.zft th{padding:2px 6px}.zrowc svg.zch{flex:1;min-width:58%}
.slide.ex1x .zpq{font-size:17px;margin-bottom:5px}.slide.ex1x .st.zs{font-size:18px!important}.slide.ex1x .zb>div{padding-top:10px}
.slide.z .zfig .zrep{font-size:17px}
.zc2{display:grid;grid-template-columns:1fr 1fr;gap:28px}.zc2>div+div{border-left:1.5px dashed #bbb;padding-left:20px}
.zrowc{display:flex;gap:14px;justify-content:center;align-items:center;width:100%}.zrowc svg{flex:1;min-width:0}
.ztab.zhep{font-size:13px}.ztab.zhep td,.ztab.zhep th{padding:1px 5px}
.slide.sort .score{float:right;font-weight:bold}.slide.sort .cards{margin-top:10px}.slide.sort .card{font-size:16px}.slide.sort .card .cb{flex-wrap:wrap;gap:4px}.slide.sort .card button{font-size:13px;padding:3px 6px}
.zmcq svg.zch{min-height:150px!important}
.slide.z .st.stp{overflow:visible;line-height:1.5;margin-bottom:6px!important;font-size:21px}
.slide.c2w .zw{display:block!important;column-count:2;column-fill:auto;column-gap:30px;column-rule:1.5px dashed #bbb}.slide.c2w .zw>*{break-inside:avoid}.slide.c2w .zpq{break-after:avoid}.slide.c2w .zpq.sep{border-top:none;padding-top:0}.slide.c2w .zpq:has(.cbk){break-before:column}
.zcas2.zsm .zcas{font-size:14px!important}.zcas2.zsm{gap:4px}
.top>.q .ztab.zft{font-size:16px;margin:4px 0}.top>.q .zchips{justify-content:flex-start}
</style><script>
(function(){function zs1(sl){sl.querySelectorAll('svg.zch:not(.full) .cax,svg.zch:not(.full) .cbr,svg.zch:not(.full) .clg,[data-f]').forEach(e=>e.classList.remove('on'));
 sl.querySelectorAll('.zc').forEach(c=>c.classList.remove('hb','hy','hg'));sl.querySelectorAll('tr.hl').forEach(r=>r.classList.remove('hl'));
 sl.querySelectorAll('.st[data-do].show').forEach(s=>s.dataset.do.split(' ').forEach(a=>{const [op,id,x,y]=a.split(':');const el=document.getElementById(id);if(!el)return;
  if(op==='ax')el.querySelector('.cax')?.classList.add('on');if(op==='lg')el.querySelector('.clg')?.classList.add('on');
  if(op==='bg')x.split(',').forEach(i=>el.querySelector(`.cbr[data-i="${i}"]`)?.classList.add('on'));
  if(op==='tf')x.split(',').forEach(k=>el.querySelector(`[data-f="${k}"]`)?.classList.add('on'));
  if(op==='hv')el.querySelectorAll(`.zc[data-v="${x}"]`).forEach(c=>c.classList.add(y));
  if(op==='hr')x.split(',').forEach(r=>el.querySelector(`tr[data-r="${r}"]`)?.classList.add('hl'))}))}
 document.querySelectorAll('.slide.z').forEach(zs1);
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide.z');if(sl&&!seen.has(sl)){seen.add(sl);zs1(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});})();
</script>'''


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


/* S1: bar chart -> percentage segmented bar morph; You try 4 three columns */
.zmo2{flex:1;min-height:0}.zmo2 .col.zc{display:flex;align-items:center;justify-content:center}

.zmo2 .st.stp{font-size:19px!important;margin-bottom:4px!important}.zmo2 .ztab{font-size:17px}
svg.zmorph{width:100%;height:100%;max-height:520px}
svg.zmorph .mof,svg.zmorph .mop,svg.zmorph .molg,svg.zmorph .mocat,svg.zmorph .moxl{transition:opacity .6s}
.slide.yt4 .zb{flex:1;min-height:0}
.slide.yt4 .zw{padding:10px 14px!important;overflow:hidden;border-right:1.5px solid #000}.slide.yt4 .zw:last-child{border-right:none}
.slide.yt4 .y4q .q{font-size:19px;line-height:1.35;margin-bottom:8px}.slide.yt4 .y4q .ztab.zft{font-size:19px;margin:6px 0 10px}.slide.yt4 .y4q .ki{font-size:17px;width:auto!important;max-width:100%!important;box-sizing:border-box}
.slide.yt4 .y4p .st.zs{font-size:18px;margin:2px 0!important;line-height:1.3}.slide.yt4 .zpq{font-size:18px;margin-bottom:4px}
.slide.yt4 .y4p .st.zpa{font-size:16px;margin-top:4px!important}
.slide.yt4 svg.zch.zbig{flex:1 1 0;min-height:0;width:100%;max-height:none!important;margin-top:4px}
svg.zch.zbig g.cbr{transform:scaleY(0);transform-box:fill-box;transform-origin:bottom;transition:transform .6s}svg.zch.zbig g.cbr.on{transform:none}
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

// S1 morph: bars -> one stacked bar (total 23) -> 100% bar. Stage = highest mo:id:k among shown steps.
(function(){const V=[3,14,6],T=23,P=V.map(v=>v/T*100),LP=['13.0%','60.9%','26.1%'];
 function geom(sv,s){const [X0,Y0,Y1,XE]=sv.dataset.g.split(',').map(Number),H=Y0-Y1,bw=110;const g=[];
  if(s===0){const sl=(XE-X0)/3;V.forEach((v,i)=>g.push({x:X0+sl*(i+.5)-bw/2,y:Y0-v/24*H,h:v/24*H}))}
  else{const xc=X0+(XE-X0)/2-bw/2;let b=0;const u=s===1?V.map(v=>v/24*H):P.map(p=>p/100*H);u.forEach(h=>{g.push({x:xc,y:Y0-b-h,h});b+=h})}
  return {g,bw}}
 function draw(sv,G,s){sv.querySelectorAll('.mor').forEach((r,i)=>{const q=G.g[i];r.setAttribute('x',q.x);r.setAttribute('y',q.y);r.setAttribute('width',G.bw);r.setAttribute('height',Math.max(0,q.h))});
  sv.querySelectorAll('.mol').forEach((t,i)=>{const q=G.g[i];t.setAttribute('x',q.x+G.bw/2);t.setAttribute('y',q.y+q.h/2+8);t.textContent=s>=2?LP[i]:V[i];if(s===0){t.setAttribute('y',q.y-10)}});
  sv.querySelectorAll('.moc').forEach((t,i)=>{const q=G.g[i];t.setAttribute('x',q.x+G.bw/2)})}
 function set(sv,s){const from=sv._s??0;sv._s=s;const A=geom(sv,from),B=geom(sv,s);
  sv.querySelector('.mof').style.opacity=s>=2?0:1;sv.querySelector('.mop').style.opacity=s>=2?1:0;sv.querySelector('.molg').style.opacity=s>=3?1:0;
  sv.querySelector('.mocat').style.opacity=s===0?1:0;sv.querySelector('.moxl').style.opacity=s===0?1:0;
  if(sv._raf)cancelAnimationFrame(sv._raf);if(from===s){draw(sv,B,s);return}
  const t0=performance.now(),D=1100,e=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
  const step=now=>{const k=e(Math.min(1,(now-t0)/D));const G={bw:B.bw,g:A.g.map((a,i)=>({x:a.x+(B.g[i].x-a.x)*k,y:a.y+(B.g[i].y-a.y)*k,h:a.h+(B.g[i].h-a.h)*k}))};
   draw(sv,G,k<1?Math.min(from,s)+(k>.5&&s>from?s-from:0):s);if(k<1)sv._raf=requestAnimationFrame(step)};sv._raf=requestAnimationFrame(step)}
 function upd(sl){sl.querySelectorAll('svg.zmorph').forEach(sv=>{let s=0;sl.querySelectorAll('.st.show[data-do]').forEach(st=>st.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');if(op==='mo'&&id===sv.id)s=Math.max(s,+x)}));if(s!==sv._s)set(sv,s)})}
 document.querySelectorAll('svg.zmorph').forEach(sv=>{sv._s=0;set(sv,0)});
 new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)&&sl.querySelector('svg.zmorph')){seen.add(sl);upd(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});})();
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
