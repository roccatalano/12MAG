r"""12MAG S4 (1G The five-number summary and the boxplot) built in the 10MA slide house style.
Shell (CSS + navigation/tile engine JS) copied from 10MA '10MAG Univariate Statistics - Slides.html'.
python3 s4_build.py  ->  lessons/S4-slides-v2.html (copy of s3_build.py; only the slides section differs)
"""
import json, html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SH = os.path.join(HERE, "shell")
OUT = os.path.join(HERE, "..", "..", "..", "lessons", "S3-slides-v2.html")
HEAD = open(os.path.join(SH,'head.html')).read().replace('10MAG Univariate Statistics · Slides', '12MAG S3 · Measures of centre and spread · Slides')
TAIL = open(os.path.join(SH,'tail.html')).read()
CG = 'Cambridge General Mathematics Units 3&amp;4'
ED = 'Edrolo General Mathematics Units 3&amp;4'
SUB = '1F Measures of centre and spread'
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
# S4 = 1G The five-number summary and the boxplot. Content from the planner card gm12-u3-s4 and the old deck
# tools/deck/s4/build.py (questions there are verbatim and cited). Boxplot helper + engine defined here.
OUT = os.path.join(HERE, "..", "..", "..", "lessons", "S4-slides-v2.html")
SUB = '1G Boxplots'
HEAD = HEAD.replace('12MAG S3 · Measures of centre and spread · Slides', '12MAG S4 · The five-number summary and the boxplot · Slides')
CG1 = 'Cambridge General Mathematics Units 1&amp;2'
ED1 = 'Edrolo General Mathematics Units 1&amp;2'

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

def bigdot(id_, counts, lo, hi, xl, W=640, r=3.4, gap=7):
    """Dot plot for large n (one dot per value, stacked)."""
    mx = max(counts.values()); ay = 30 + mx * gap; px = lambda x: 30 + (x - lo) / (hi - lo) * (W - 60)
    s = f'<line x1="14" y1="{ay}" x2="{W-14}" y2="{ay}" stroke="#000" stroke-width="2"/>'
    for x in range(lo, hi + 1):
        s += f'<line x1="{px(x)}" y1="{ay-5}" x2="{px(x)}" y2="{ay+5}" stroke="#000"/><text x="{px(x)}" y="{ay+24}" font-size="17" text-anchor="middle">{x}</text>'
    first, last = min(counts), max(counts)
    for x, c in counts.items():
        for j in range(c):
            e = ' data-e="1"' if (x in (first, last)) else ''
            s += f'<circle cx="{px(x)}" cy="{ay-6-j*gap}" r="{r}" fill="#333"{e}/>'
    s += f'<text x="{W/2}" y="{ay+48}" font-size="17" text-anchor="middle">{xl}</text>'
    return f'<svg class="zbd" id="{id_}" viewBox="0 0 {W} {ay+56}">{s}</svg>'

def rowtab(id_, head, vals):
    return table_hl(id_, [(head, vals)], 'ztab zinq')

KI_5 = r'Five-number summary: min, $Q_1$, $M$, $Q_3$, max<div class="kn">the box runs $Q_1$ to $Q_3$; line at $M$; whiskers to the ends</div>'
KI_F = r'$\text{LF} = Q_1 - 1.5 \times \text{IQR}$<br>$\text{UF} = Q_3 + 1.5 \times \text{IQR}$<div class="kn">below LF or above UF → outlier (a dot)</div>'
KI_P = r'Each of the four sections holds about <b>25%</b> of the data.<div class="kn">below $Q_1$: 25% · below $M$: 50% · below $Q_3$: 75%</div>'
KI_S = r'SOCS: <b>S</b>hape · <b>O</b>utliers · <b>C</b>entre (median) · <b>S</b>pread (IQR, range)'
SOCS = lambda s, o, c, sp: (f'The distribution is {s}.<br>There {o}.<br>The distribution is centred at {c}, the median.<br>{sp}')

S.append(f'<section class="slide title cover"><h1>The five-number summary and the boxplot</h1>'
         f'<div class="unit">12MAG · Unit 3 · AOS 1 Data analysis</div>'
         f'<div class="pp" style="font-size:22px;margin-top:14px">{CG}</div>'
         f'<ul style="list-style:none;padding:0;margin:10px 0 0;font-size:22px;line-height:1.5;text-align:left"><li>1G The five-number summary and the boxplot (pp. 61–69)</li></ul><span class="pg" style="display:none"></span></section>')
LI = ['To be able to construct the boxplot for displaying the distribution of a numerical data.', 'To be able to define and identify outliers.',
      'To be able to construct both simple boxplots and boxplots with outliers.', 'To be able to determine the features of a distribution from a boxplot.',
      'To be able to use a CAS calculator to construct a boxplot.']
SC = ['I can construct a boxplot from a five-number summary.', 'I can construct a boxplot with outliers from data using the CAS calculator.',
      'I can read values from a boxplot.', 'I can estimate percentages from a boxplot.', 'I can use boxplots to describe a distribution without outliers.',
      'I can use boxplots to describe a distribution with outliers.', 'I can use boxplots to answer statistical questions.']
SEQ = ['Activating prior knowledge', 'Key ideas and formulas', 'The boxplot · Example 22', 'Outliers and the fences', 'Boxplots on CAS',
       'Reading a boxplot · Examples 23–24', 'Shape from a boxplot · Examples 25–27', 'Exit tasks', 'Check-in and coursework']
S.append(f'<section class="slide z li">{bar("1G", "Learning intentions")}<div class="cols" style="grid-template-columns:1.05fr 1.05fr .9fr">'
         f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
         f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
         f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
         f'{foot(CG + ", 1G Learning intentions (p. 61); success criteria: one per worked example")}</section>')

# ---- APK 1 + 2: party ages (Cambridge U1&2 2H #14, #15)
PARTY = [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')]
APKQ = 'The ages of a group of people at a party:<br>19 21 22 56 34 19 27 28 34 17 66 37 20 20 21 45 26 19 23 29<br>'
S.append(qslide('apk', '1 of 3', 'Year 11 skills: five-number summary and boxplot', 'Cambridge U1&amp;2 · 2H #14',
    APKQ + 'Complete the five-number summary for the ages of the people who attended the party (from above) and use it to construct a boxplot (without outliers).',
    KI_5, [('$n = 20$: min $= 17$, max $= 66$', 'lx:pa:0,19'),
           (r'Median position $= \dfrac{20 + 1}{2} = $ 10.5th. Count to the 10th and 11th: $M = \dfrac{23 + 26}{2} = 24.5$', 'ln:pa:0:11 lm:pa:9,10'),
           (r'Ten in each half: $Q_1 = \dfrac{20 + 20}{2} = 20$, $Q_3 = \dfrac{34 + 34}{2} = 34$', 'lm:pa:9,10 lq:pa:4,5,14,15'),
           ('Scale 15 to 70. Box from 20 to 34, line at 24.5', 'lm:pa:9,10 lq:pa:4,5,14,15 bx:pab:axis,box,med'),
           ('Whiskers out to 17 and 66', 'lm:pa:9,10 lq:pa:4,5,14,15 bx:pab:wl,wu')],
    '<b>17, 20, 24.5, 34, 66</b>; boxplot drawn', CG1 + ', Chapter 2 skills checklist 2H #14 (data in a stem plot by the teacher). Working by teacher.',
    fig=stem('pa', PARTY, 'Key: 1 | 7 = 17') + bplot('pab', 15, 70, 5, 10, (17, 20, 24.5, 34, 66), xl='age (years)', build=True), figw='1.45fr', cls='tight apkb apks'))
S.append(qslide('apk', '2 of 3', 'Year 11 skills: outliers from the fences', 'Cambridge U1&amp;2 · 2H #15',
    APKQ + 'Calculate the values of the upper and lower fences, and use these to find any outliers in the ages of the people who attended the party (from above).',
    KI_F, [(r'$\text{IQR} = 34 - 20 = 14$', 'lq:pb:4,5,14,15'),
           (r'$\text{LF} = 20 - 1.5 \times 14 = -1$', 'lq:pb:4,5,14,15 bx:pbb:fl'),
           (r'$\text{UF} = 34 + 1.5 \times 14 = 55$', 'lq:pb:4,5,14,15 bx:pbb:fl,fu'),
           ('$56 > 55$ and $66 > 55$: outliers. Nothing is below $-1$.', 'lq:pb:4,5,14,15 lx:pb:18,19 bx:pbb:fl,fu,out'),
           ('Upper whisker stops at 45, the largest value that is not an outlier', 'lq:pb:4,5,14,15 lx:pb:18,19 bx:pbb:fl,fu,out,wu')],
    'LF $= -1$, UF $= 55$. The outliers are <b>56 and 66</b>.', CG1 + ', Chapter 2 skills checklist 2H #15. Working by teacher.',
    fig=stem('pb', PARTY, 'Key: 1 | 7 = 17') + bplot('pbb', -5, 70, 5, 10, (17, 20, 24.5, 34, 45), out=(56, 66), xl='age (years)', hide=('out', 'wu'),
        fences=(('fl', -1, 'LF = −1'), ('fu', 55, 'UF = 55'))), figw='1.75fr', cls='tight apkb apks'))
OPTDIST['3 of 3'] = [None] * 5
S.append(qslide('apk', '3 of 3', 'A real VCAA question you can already do', 'VCAA 2017 Exam 1 Q2 (adapted)',
    'The boxplot shows the distribution of the <i>reaction time</i> (milliseconds), of 256 firefighters.'
    + bplot('fir', 0, 260, 10, 50, (122, 130, 140, 152, 179), out=(70, 90, 255), xl='reaction time (milliseconds)', caps=True,
            marks=(('m1', 70, 'min', '#d00000'), ('m2', 255, 'max', '#d00000'))) +
    'The five-number summary for the <i>reaction time</i> of these 256 firefighters is closest to',
    r'Outliers are real data values.<div class="kn">min and max are the outer dots, not the whisker ends</div>',
    [('The dots are data: smallest value $= 70$, largest $= 255$', 'bx:fir:m1,m2 bxo:fir'), ('Box: $Q_1 = 130$, $M = 140$, $Q_3 = 152$', 'bx:fir:m1,m2 bxo:fir')],
    '70, 130, 140, 152, 255',
    ED1 + ', 1F Q16 · adapted by Edrolo from VCAA 2017 Exam 1 Data analysis Q2; 58% correct (examiner report, original question). Boxplot redrawn.',
    marks=1, vcaa=58, opts=[('A', '70, 130, 140, 152, 179'), ('B', '70, 130, 140, 152, 255'), ('C', '122, 130, 140, 152, 179'), ('D', '122, 130, 140, 152, 245'), ('E', '122, 130, 140, 152, 265')],
    key='B', figw='1.15fr').replace('zmc"', 'zmc zmc1"').replace('How did students answer? Bars show the % choosing each option.', '58% chose B (examiner report). The report’s % for each other option is not in the repo.')
    .replace('pct stat:58', 'stat:58'))

# ---- Key ideas
KD = [('Five-number summary', 'minimum, $Q_1$, median, $Q_3$, maximum'), ('Boxplot', 'a picture of the five-number summary; the box holds the middle 50%'),
      ('Whiskers', 'run from the box to the smallest and largest values that are not outliers'), ('Outlier', 'a value below the lower fence or above the upper fence, drawn as a dot')]
KF = [('Median position', r'$\dfrac{n + 1}{2}$th value'), ('Interquartile range', r'$\text{IQR} = Q_3 - Q_1$'), ('Range', r'$\text{range} = \text{max} - \text{min}$'),
      ('Lower fence', r'$\text{LF} = Q_1 - 1.5 \times \text{IQR}$ &nbsp;<span class="zn">$x < \text{LF}$ → outlier</span>'),
      ('Upper fence', r'$\text{UF} = Q_3 + 1.5 \times \text{IQR}$ &nbsp;<span class="zn">$x > \text{UF}$ → outlier</span>')]
S.append(f'<section class="slide z kif">{bar("1G", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1F pp. 44–47 and 1G pp. 61–64. Fences: VCAA formula sheet.")}</section>')

# ---- NL: the boxplot
S.append(nl_slide('Five numbers, one picture',
    'A <b>boxplot</b> draws the five-number summary. <span class="hint">Click to build it.</span>',
    '<div class="zbig">' + bplot('nl1', 0, 100, 5, 10, (12, 35, 50, 62, 95), build=True, W=900,
        marks=(('k0', 12, 'min', '#8a4d00'), ('k1', 35, 'Q₁', '#1f5fbf'), ('k2', 50, 'M', '#d00000'), ('k3', 62, 'Q₃', '#1f5fbf'), ('k4', 95, 'max', '#8a4d00')),
        bands=(('p1', 12, 35, '25%'), ('p2', 35, 50, '25%'), ('p3', 50, 62, '25%'), ('p4', 62, 95, '25%'))) + '</div>'
    + '<div class="zrow3">' + st('<b>1</b> Scaled number line; mark the five numbers.', do='bx:nl1:axis,k0,k1,k2,k3,k4')
    + st('<b>2</b> Box from $Q_1$ to $Q_3$, line at the median.', do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med')
    + st('<b>3</b> Whiskers out to the min and the max.', do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med,wl,wu')
    + st('<b>Each section holds about 25% of the data</b>, however long it looks.', True, do='bx:nl1:axis,k0,k1,k2,k3,k4,box,med,wl,wu,p1,p2,p3,p4') + '</div>',
    CG + ', 1G pp. 61–62. Boxplot: teacher illustration.'))

# ---- Example 22 / You try 22
life = [('5', '2'), ('5', '5 6'), ('6', '4'), ('6', '6 6 7 9'), ('7', '1 2 2 3 3 4 4 4 4'), ('7', '5 5 6 6 7 7')]
S.append(qslide('ex', 22, 'Constructing a boxplot from a five-number summary', 'Cambridge · Example 22',
    'The stem plot shows the distribution of life expectancies (in years) in 23 countries. The five-number summary for these data is:'
    + '<table class="ztab zinq zh5"><tr><th>minimum</th><th>first quartile ($Q_1$)</th><th>median ($M$)</th><th>third quartile ($Q_3$)</th><th>maximum</th></tr><tr><td>52</td><td>66</td><td>73</td><td>75</td><td>77</td></tr></table>'
    + 'Use the five-number summary to construct a boxplot.', KI_5,
    [('The five numbers on the stem plot: 52, 66, 73, 75, 77', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11'),
     ('Number line 50 to 80, labelled and scaled', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis'),
     ('Box from $Q_1 = 66$ to $Q_3 = 75$; line at $M = 73$', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis,box,med'),
     ('Whiskers out to 52 and 77', 'lx:s22:0,22 lq:s22:5,17 lm:s22:11 bx:b22:axis,box,med,wl,wu')],
    'Boxplot drawn (52, 66, 73, 75, 77)', CG + ', 1G Example 22',
    fig=stem('s22', life, 'Key: 5 | 2 = 52 years') + bplot('b22', 50, 80, 1, 5, (52, 66, 73, 75, 77), xl='Life expectancy (years)', build=True), figw='1.75fr', cls='tight apkb apks'))
w4 = [('0', '1 2 3 5 5 9'), ('1', '0 0 1 5 8 9'), ('2', '1 2 3 3 5'), ('3', '3 7 9')]
S.append(qslide('yt', 22, 'Constructing a boxplot from a five-number summary', 'Edrolo 1E WE4',
    'The five-number summary for the following stem plot is: 1, 7, 16.5, 23, 39<br>Construct a boxplot using the data.', KI_5,
    [('Number line 0 to 40', 'bx:b4:axis'), ('Box from 7 to 23; line at 16.5', 'bx:b4:axis,box,med'),
     (r'Check for outliers: $\text{IQR} = 16$, fences $-17$ and $47$. 1 and 39 are inside.', 'bx:b4:axis,box,med'),
     ('Whiskers out to 1 and 39', 'bx:b4:axis,box,med,wl,wu')],
    'Boxplot drawn; no outliers', ED + ', 1E Worked example 4. Working by teacher.',
    fig=stem('y22', w4, 'Key: 1 | 2 = 12') + bplot('b4', 0, 40, 1, 5, (1, 7, 16.5, 23, 39), build=True), figw='1fr', cls='tight apkb'))

# ---- NL: outliers and fences (Cambridge CAS 4 data)
S.append(nl_slide('Outliers: the 1.5 × IQR fences',
    'An <b>outlier</b> is more than 1.5 IQRs below $Q_1$ or above $Q_3$. It is drawn as a dot; the whisker stops at the last value inside the fence. <span class="hint">19 marks: $Q_1 = 23$, $M = 30$, $Q_3 = 35$.</span>',
    '<div class="zbig">' + bplot('nl2', 0, 55, 1, 5, (21, 23, 30, 35, 48), out=(3,), xl='marks', W=900, hide=('wl', 'wu', 'out'),
        bands=(('iq', 23, 35, 'IQR = 12'),), fences=(('fl', 5, 'LF = 5'), ('fu', 53, 'UF = 53'))) + '</div>'
    + '<div class="zrow3">' + st(r'<b>1</b> $\text{IQR} = 35 - 23 = 12$', do='bx:nl2:iq')
    + st(r'<b>2</b> $\text{LF} = 23 - 18 = 5$, $\text{UF} = 35 + 18 = 53$', do='bx:nl2:iq,fl,fu')
    + st('<b>3</b> $3 < 5$: <b>3 is an outlier</b> (a dot). Nothing is above 53.', do='bx:nl2:iq,fl,fu,out')
    + st('Whiskers: down to 21 (smallest non-outlier), up to 48 (the max).', True, do='bx:nl2:iq,fl,fu,out,wl,wu') + '</div>',
    CG + ', 1G pp. 63–64. Data: CAS 4 (p. 64).'))

# ---- interactive: party ages fence slider
S.append(f'<section class="slide z nl zfx">{bar("New learning", "When is an age an outlier?")}'
    '<div class="ctx">Back to the party. The oldest guest was 66. Drag the slider (or tap a button) to change that one guest’s age. The quartiles, fences and boxplot update. When does that guest become an <b>outlier</b>?</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>Party ages (years)</h2>'
    '<svg class="zfxs ix" viewBox="0 0 700 230" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>15</span><input type="range" min="15" max="90" step="1" value="66"><span>90</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-v="45">45</button><button data-v="55">55</button><button data-v="56">56</button><button data-v="66">66</button><button data-v="90">90</button></div></div>'
    '<div class="col"><h2>Live summary</h2><div class="zfxo"></div>'
    '<div class="zrule">$x$ is an outlier if $x < Q_1 - 1.5 \\times \\text{IQR}$ or $x > Q_3 + 1.5 \\times \\text{IQR}$. Exactly on a fence is <b>not</b> an outlier.</div></div></div>'
    f'{foot("Data: " + CG1 + ", Chapter 2 skills checklist 2H #14–15 (party ages). Interactive by teacher.")}</section>')

# ---- CAS
def castabs(sid):
    import json as _j
    sk = [x for x in _j.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if isinstance(x, dict) and x.get('id') == sid][0]
    return ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in sk["ti"])}</ol></div>'
            '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in sk["classpad"])}</ol></div></div>')
S.append(qslide('cas', '', 'Boxplot with outliers on CAS', 'Cambridge · 1G CAS 4',
    'Display the following set of 19 marks in the form of a boxplot with outliers.<br>28 &nbsp;21 &nbsp;21 &nbsp;3 &nbsp;22 &nbsp;31 &nbsp;35 &nbsp;26 &nbsp;27 &nbsp;33 &nbsp;43 &nbsp;31 &nbsp;30 &nbsp;34 &nbsp;48 &nbsp;36 &nbsp;35 &nbsp;23 &nbsp;24',
    r'CAS draws outliers as dots automatically.<div class="kn">Trace gives min, $Q_1$, $M$, $Q_3$, max</div>',
    ['Enter the 19 marks in one list.', 'Draw the box plot (outliers on).', 'Trace: min $= 3$ (a dot), $Q_1 = 23$, $M = 30$, $Q_3 = 35$, max $= 48$',
     ('3 shows as a dot; the whisker starts at 21', 'bx:cb:out')],
    'The boxplot has one outlier, <b>3</b>', CG + ', 1G pp. 64–66 (CAS 4). CAS steps: planner CAS guide.',
    fig=castabs('boxplot') + bplot('cb', 0, 50, 1, 10, (21, 23, 30, 35, 48), out=(3,), xl='marks', W=560), figw='1.05fr', cls='tight apkb'))
S.append(qslide('yt', '', 'Constructing a boxplot with outliers using CAS', 'Edrolo 1E WE5',
    'Construct a boxplot for the following data set.<br>2 &nbsp;4 &nbsp;4 &nbsp;5 &nbsp;5 &nbsp;5 &nbsp;7 &nbsp;6 &nbsp;5 &nbsp;4 &nbsp;6 &nbsp;5 &nbsp;6 &nbsp;7 &nbsp;8 &nbsp;12 &nbsp;3 &nbsp;5', KI_F,
    ['CAS one-variable statistics: 2, 4, 5, 6, 12', r'$\text{IQR} = 6 - 4 = 2$', r'$\text{LF} = 4 - 3 = 1$, $\text{UF} = 6 + 3 = 9$',
     ('$12 > 9$: outlier. $2 > 1$: not an outlier.', 'bx:b5:axis,box,med,fl,fu,out'), ('Whiskers to 2 and 8 (largest non-outlier)', 'bx:b5:axis,box,med,fl,fu,out,wl,wu')],
    'Boxplot drawn, with <b>12 as an outlier</b>', ED + ', 1E Worked example 5. Working by teacher.',
    fig=bplot('b5', 0, 13, 1, 1, (2, 4, 5, 6, 8), out=(12,), xl='value', build=True, fences=(('fl', 1, 'LF = 1'), ('fu', 9, 'UF = 9'))), figw='1fr'))
S.append(f'<section class="slide z cas">{bar("CAS", "Parallel boxplots on CAS")}<p class="lead zlead">Two or more groups on the same scale (used again in 2C). Steps from the planner CAS guide.</p>'
         f'<div class="zb" style="grid-template-columns:1fr;margin-top:6px"><div class="zfig">{castabs("parallel-boxplots").replace("zcas2", "zcas2 zh")}</div></div>'
         f'{foot("CAS steps: planner CAS guide (parallel-boxplots) · ClassPad Help 405")}</section>')

# ---- Example 23 / You try 23
S.append(qslide('ex', 23, 'Reading values from a boxplot', 'Cambridge · Example 23',
    'For the boxplot shown, write down the values of:', r'Fences: $Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$', [], None, CG + ', 1G Example 23',
    parts=[('a', 'the median', [], '$M = 36$', 'bx:b23:mm'),
           ('b', 'the quartiles $Q_1$ and $Q_3$', [], '$Q_1 = 30$, $Q_3 = 44$', 'bx:b23:mm,mq,mq3'),
           ('c', 'the interquartile range (IQR)', [], r'$\text{IQR} = 44 - 30 = 14$', 'bx:b23:mm,mq,mq3'),
           ('d', 'the minimum and maximum values', [], 'min $= 4$, max $= 92$', 'bx:b23:mm,mq,mq3'),
           ('e', 'the values of any possible outliers', [], '4, 70, 84 and 92', 'bx:b23:mm,mq,mq3 bxo:b23'),
           ('f', 'the smallest value in the upper end of the data set that will be classified as an outlier', [], r'$\text{UF} = 44 + 1.5 \times 14 = 65$: values above 65', 'bx:b23:mm,mq,mq3,fu bxo:b23'),
           ('g', 'the largest value in the lower end of the data set that will be classified as an outlier.', [], r'$\text{LF} = 30 - 1.5 \times 14 = 9$: values below 9', 'bx:b23:mm,mq,mq3,fu,fl bxo:b23')],
    fig=bplot('b23', 0, 100, 2, 10, (10, 30, 36, 44, 60), out=(4, 70, 84, 92), W=900,
        marks=(('mm', 36, 'M', '#d00000', 1), ('mq', 30, 'Q₁', '#1f5fbf'), ('mq3', 44, 'Q₃', '#1f5fbf')),
        fences=(('fl', 9, 'LF 9'), ('fu', 65, 'UF 65'))), stack=True, cls='tight p7'))
S.append(qslide('yt', 23, 'Reading values from a boxplot', 'Edrolo 1E WE6',
    'The <i>number of runs scored</i> by the leading batsman at a local cricket club is represented by the following boxplot. It is known that data was collected from 20 separate innings.',
    KI_P, [], None, ED + ', 1E Worked example 6. Working by teacher.',
    parts=[('a.', 'Determine the five-number summary for the data and identify any outliers.', [], '30, 50, 70, 80, 90; no outliers', None),
           ('b.', 'Between which two values does the middle 50% of data lie?', [], '50 and 80 runs', 'bx1:b6:h1'),
           ('c.', 'In approximately what percentage of innings did they score more than 80 runs?', [], '25%', 'bx1:b6:h2'),
           ('d.', 'In approximately how many innings did they score at least 50 runs, but fall short of 100?', [], r'75% of 20 $= 15$ innings', 'bx1:b6:h3')],
    fig=bplot('b6', 0, 100, 5, 10, (30, 50, 70, 80, 90), caps=True, xl='number of runs scored', W=900,
        bands=(('h1', 50, 80, 'middle 50%'), ('h2', 80, 90, '25%'), ('h3', 50, 90, '75%'))), stack=True, cls='tight'))

# ---- Example 24
S.append(qslide('ex', 24, 'Estimating percentages from a boxplot', 'Cambridge · Example 24',
    'For the boxplot shown, estimate the percentage of values:', KI_P, [], None,
    CG + ', 1G Example 24. Boxplot redrawn; the outlier dots are placed by eye from the textbook figure. No matching Edrolo worked example, so no You try.',
    parts=[('a', 'less than 54', [], '54 is $Q_1$: <b>25%</b>', 'bx1:b24:ba'), ('b', 'less than 55', [], '55 is $M$: <b>50%</b>', 'bx1:b24:bb'),
           ('c', 'less than 59', [], '59 is $Q_3$: <b>75%</b>', 'bx1:b24:bc'), ('d', 'greater than 59', [], '100% − 75% = <b>25%</b>', 'bx1:b24:bd'),
           ('e', 'between 54 and 59', [], '75% − 25% = <b>50%</b>', 'bx1:b24:be'), ('f', 'between 54 and 86.', [], '100% − 25% = <b>75%</b>', 'bx1:b24:bf')],
    fig=bplot('b24', 45, 85, 1, 5, (50, 54, 55, 59, 65), out=(70, 81), W=900,
        bands=(('ba', 50, 54, '25%'), ('bb', 50, 55, '50%'), ('bc', 50, 59, '75%'), ('bd', 59, 81, '25%'), ('be', 54, 59, '50%'), ('bf', 54, 81, '75%'))), stack=True, cls='tight'))

# ---- NL: shape
def mini(id_, f5, out=()):
    return bplot(id_, 0, 20, 1, 100, f5, out=out, W=420, T=4)
S.append(nl_slide('Reading shape from a boxplot',
    'Where does the median sit in the box? Which whisker is longer? The long side is the <b>tail</b>. <span class="hint">Click for each shape.</span>',
    '<div class="zsh4">' + st('<h3>Symmetric</h3>' + mini('h1', (2, 7, 10, 13, 18)) + 'Median near the middle; whiskers about equal.')
    + st('<h3>Positively skewed</h3>' + mini('h2', (1, 3, 4.5, 8, 19)) + 'Median to the <b>left</b> of the box; long <b>right</b> whisker.')
    + st('<h3>Negatively skewed</h3>' + mini('h3', (1, 12, 15.5, 17, 19)) + 'Median to the <b>right</b>; long <b>left</b> whisker.')
    + st('<h3>With outliers</h3>' + mini('h4', (8, 10, 11, 12, 14), out=(2, 19)) + 'Dots separated from the whiskers.') + '</div>'
    + st('<b>Describe with SOCS, like a sock:</b> Shape · Outliers · Centre (the median) · Spread (IQR and range).', True, cls='zctr'),
    CG + ', 1G pp. 68–69. Sketches: teacher illustration.'))

# ---- Example 25 / You try 25 / Examples 26, 27
S.append(qslide('ex', 25, 'Using a boxplot to describe a distribution without outliers', 'Cambridge · Example 25',
    'Describe the distribution represented by the boxplot in terms of shape, centre and spread. Give appropriate values.', KI_S,
    [('<b>S</b> Median left of centre, long right whisker', 'bx:b25:mm'), ('<b>O</b> No dots', 'bx:b25:mm'),
     ('<b>C</b> $M = 10$', 'bx:b25:mm'), (r'<b>S</b> $\text{IQR} = 21 - 5 = 16$, range $= 45 - 0 = 45$', 'bx:b25:mm,q1,q3,mx')],
    SOCS('positively skewed', 'are no outliers', '10', 'The IQR is 16 and the range is 45.'),
    CG + ', 1G Example 25 (solution set out in SOCS order)',
    fig=bplot('b25', 0, 50, 1, 5, (0, 5, 10, 21, 45), W=640, col='#fde7a6',
        marks=(('mm', 10, 'M = 10', '#d00000', 1), ('q1', 5, 'Q₁ = 5', '#1f5fbf'), ('q3', 21, 'Q₃ = 21', '#1f5fbf'), ('mx', 45, 'max = 45', '#8a4d00'))), figw='1fr'))
S.append(qslide('yt', 25, 'Using a boxplot to describe a distribution without outliers', 'Edrolo 1F WE5',
    'Consider the boxplot.<br>Describe the distribution in terms of shape, centre, spread and outliers.', KI_S,
    [('<b>S</b> Median towards the right of the box; tail to the left', 'bx:b25y:mm'), ('<b>O</b> No dots', 'bx:b25y:mm'),
     ('<b>C</b> $M = 18$', 'bx:b25y:mm'), (r'<b>S</b> range $= 20 - 12 = 8$', 'bx:b25y:mm')],
    SOCS('negatively skewed', 'are no outliers', '18', 'The range is 8.'),
    ED + ', 1F Worked example 5 (solution set out in SOCS order)',
    fig=bplot('b25y', 12, 20, 0.5, 2, (12, 15, 18, 19, 20), caps=True, W=640, col='#ddd3f3', marks=(('mm', 18, 'M = 18', '#d00000'),)), figw='1fr'))
S.append(qslide('ex', 26, 'Using a boxplot to describe a distribution with outliers', 'Cambridge · Example 26',
    'Describe the distributions represented by the boxplot in terms of shape and outliers, centre and spread. Give appropriate values.', KI_S,
    [('<b>S</b> Box and whiskers symmetric', 'bx:b26:mm'), ('<b>O</b> Four dots: 10, 15, 20, 25', 'bx:b26:mm bxo:b26'),
     ('<b>C</b> $M = 41$', 'bx:b26:mm bxo:b26'), (r'<b>S</b> $\text{IQR} = 44.25 - 38.75 = 5.5$, range $= 47 - 10 = 37$', 'bx:b26:mm bxo:b26')],
    SOCS('symmetric', 'are outliers at 10, 15, 20 and 25', '41', 'The IQR is 5.5 and the range is 37.'),
    CG + ', 1G Example 26 (solution set out in SOCS order). No matching Edrolo worked example, so no You try.',
    fig=bplot('b26', 0, 50, 1, 5, (34, 38.75, 41, 44.25, 47), out=(10, 15, 20, 25), W=640, col='#e9c6ea', marks=(('mm', 41, 'M = 41', '#d00000'),)), figw='1fr'))
S.append(qslide('ex', 27, 'Using a boxplot to answer statistical questions', 'Cambridge · Example 27',
    'The boxplot shows the gestation period (completed weeks) for a sample for 1000 babies born in Australia one year. Describe the distribution of gestation period in terms of shape, centre, spread and outliers.', KI_S,
    [('<b>S</b> Long tail of dots to the left', 'bx:b27:mm'), ('<b>O</b> Dots at 25 to 34 weeks', 'bx:b27:mm bxo:b27'),
     ('<b>C</b> $M = 39$ weeks', 'bx:b27:mm bxo:b27'), (r'<b>S</b> $\text{IQR} = 40 - 38 = 2$, range $= 42 - 25 = 17$', 'bx:b27:mm bxo:b27')],
    SOCS('negatively skewed', 'are outliers at 25, 26, 27, 28, 29, 30, 31, 32, 33 and 34 weeks', '39 weeks', 'The IQR is only 2 weeks, but the range is 17 weeks.'),
    CG + ', 1G Example 27 (solution set out in SOCS order). No matching Edrolo worked example, so no You try.',
    fig=bplot('b27', 25, 43, 1, 1, (35, 38, 39, 40, 42), out=tuple(range(25, 35)), xl='Gestation period (weeks)', W=640, col='#bcd6f2', marks=(('mm', 39, 'M = 39', '#d00000'),)), figw='1fr', cls='tight'))

# ---- Exit 1: VCAA 2020 E2 Q2c (Edrolo 1E Q19)
neck = {31: 1, 32: 1, 33: 3, 34: 11, 35: 19, 36: 32, 37: 34, 38: 48, 39: 39, 40: 18, 41: 28, 42: 12, 43: 3, 44: 1}
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2020 Exam 2 Q2c',
    'The <i>neck size</i>, in centimetres, of 250 men was recorded and displayed in the following dot plot.' + bigdot('nk', neck, 30, 45, 'neck size (cm)')
    + 'The five-number summary for this sample of neck sizes, in centimetres, is given in the following table.'
    + table_hl('nk5', [('minimum', ['31']), ('first quartile ($Q_1$)', ['36']), ('median', ['38']), ('third quartile ($Q_3$)', ['39']), ('maximum', ['44'])], 'ztab zinq zh5')
    + 'Use the five-number summary to construct a boxplot, showing any outliers if appropriate.', KI_F,
    [r'$\text{IQR} = 39 - 36 = 3$', r'$\text{LF} = 36 - 4.5 = 31.5$, $\text{UF} = 39 + 4.5 = 43.5$',
     ('$31 < 31.5$ and $44 > 43.5$: both are outliers', 'bdx:nk'), ('Whiskers stop at the last values inside the fences: 32 and 43', 'bdx:nk')],
    bplot('nkb', 30, 45, 0.5, 1, (32, 36, 38, 39, 43), out=(31, 44), xl='neck size (cm)', W=560),
    ED + ', 1E Q19 · VCAA 2020 Exam 2 Data analysis Q2c; average 1.1/2 marks (55%), examiner report. Dot plot redrawn. Working by teacher.',
    marks=2, vcaa=55, figw='1.05fr', ans_do='bdx:nk', cls='tight',
    watch='Teacher tip: the whiskers end at 32 and 43 (real values), not at the fences 31.5 and 43.5.'))
# ---- Exit 2: VCAA 2021 E2 Q1e (Edrolo 1E Q20)
hep = [('1.76', '15.34', '41.22'), ('1.79', '16.96', '42.41'), ('1.83', '13.87', '46.53'), ('1.82', '14.23', '40.53'), ('1.87', '13.78', '40.62'), ('1.73', '14.50', '45.62'),
       ('1.68', '15.08', '42.33'), ('1.82', '13.13', '40.88'), ('1.83', '14.22', '39.22'), ('1.87', '13.62', '42.51'), ('1.87', '12.01', '42.75'), ('1.80', '12.88', '38.12'),
       ('1.83', '12.68', '42.65'), ('1.87', '12.45', '41.32'), ('1.78', '11.31', '42.88')]
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2021 Exam 2 Q1e',
    'In the sport of heptathlon, athletes compete in seven events. These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump. '
    'Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games. Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.'
    + table_hl('hp', [('athlete number', [str(i) for i in range(1, 16)]), ('high jump (metres)', [h[0] for h in hep]), ('shot-put (metres)', [h[1] for h in hep]), ('javelin (metres)', [h[2] for h in hep])], 'ztab zinq zhep')
    + 'The following boxplot was constructed to show the distribution of high jump heights for all 15 athletes in the qualifying competition.'
    + bplot('hj', 1.68, 1.88, 0.01, 0.04, (1.68, 1.78, 1.82, 1.87, 1.87), caps=True, xl='high jump (metres)', dec=2, W=600, marks=(('q3', 1.87, 'Q₃ = max = 1.87', '#d00000'),))
    + 'Explain why the boxplot has no whisker at its upper end.', KI_5,
    [('Only the high jump row matters', 'dim:hp:2 dim:hp:3'),
     (r'$n = 15$: $Q_3$ is the middle (4th) of the top 7 values $= 1.87$', 'dim:hp:2 dim:hp:3 bx:hj:q3'),
     ('The largest jump is also 1.87 (four athletes)', 'dim:hp:2 dim:hp:3 bx:hj:q3 tc:hp:104,109,110,113')],
    '$Q_3$ and the maximum are both 1.87 m, so there is nothing for an upper whisker to cover.',
    ED + ', 1E Q20 · VCAA 2021 Exam 2 Data analysis Q1e; average 0.5/1 (50%), examiner report. Table transposed to fit (adapted layout); boxplot redrawn.',
    marks=1, vcaa=50, figw='1.25fr', ans_do='dim:hp:2 dim:hp:3 bx:hj:q3 tc:hp:104,109,110,113', cls='tight',
    watch='Teacher tip: name both values. “$Q_3$ = maximum = 1.87 m” is the reason; “there are no data above the box” on its own does not say why.'))

# ---- check-in, coursework
S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
         f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot("Success criteria: one per worked example")}</section>')
CWR = open(os.path.join(SH, 'cwr.html')).read().replace('>Exercise 9A: Collecting representative data<',' textLength="344" lengthAdjust="spacingAndGlyphs">Exercise 1G: The five-number summary and the boxplot<'); CWL = open(os.path.join(SH, 'cwl.html')).read()
S.append(f'<section class="slide cwk">{bar("1G", "Coursework · Exercise 1G")}<div class="cwgrid"><div class="cwl2">'
         '<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>'
         '<tr><th>Cambridge Exercise 1G (part 1)</th><td>Q1–10</td></tr>'
         '<tr><th>Cambridge Exercise 1G (part 2)</th><td>Q11–20</td></tr>'
         '<tr><th>Practice booklet</th><td>1G section</td></tr></tbody></table>'
         '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
         f'{CWL}</div>{CWR}</div>{foot(CG + ", Exercise 1G")}</section>')

# ---- S4 extras: boxplot engine, big dot plot marks, party slider (appended to the shell)
HEAD = HEAD.replace('</head>', r'''<style>
svg.zbx{width:100%;overflow:visible}svg.zbx [data-p]{transition:opacity .35s}
svg.zbx .bo.on{fill:#f39c12}
.slide.z .zfig svg.zbx{max-height:230px}
.slide.z.stack .zfig svg.zbx,.slide.z .zb.stack .zfig svg.zbx{max-height:250px}
.slide.apkb .zfig{flex-direction:column;gap:2px;justify-content:flex-start!important;padding-top:22px!important}.slide.apkb .zstem table{font-size:19px!important}.slide.apkb .zstem .zkey{font-size:15px;margin-top:2px}.slide.apkb .zfig svg.zbx{max-height:112px;flex:none}.slide.apkb .zcas2 .zcas{font-size:15px!important}.slide.apkb .zstem td{padding-top:0!important;padding-bottom:0!important}
.zw.c2 .zpq.brk{break-before:auto!important;border-top:2px dotted #888!important;padding-top:6px!important}.zw.c2 .zpq.brk:first-child{border-top:none!important}
.slide.tight .zw.c2{column-count:3}
.slide.tight .zw.c2 .st.zs{font-size:18px!important;margin-bottom:4px!important}.slide.tight .zw.c2 .zpq{font-size:17px;margin-bottom:2px}.slide.z .zb.stack .zfig svg.zbx{max-height:165px!important}.slide.z .zb.stack>.zfig{padding:4px 22px!important}.zw.c2 .zpq{break-after:avoid}.slide.p7 .zb.stack .zfig svg.zbx{max-height:135px!important}.slide.p7 .zw.c2 .st.zs{font-size:16px!important}.slide.p7 .zw.c2 .zpq{font-size:16px}.slide.p7 .top>.q{font-size:20px}
.slide.exam .st.final svg.zbx{max-height:105px!important}.slide.exam.tight .st.zs{font-size:17px!important;margin-bottom:4px!important}.slide.exam .zw .ki{margin-bottom:6px}
.slide.z .zfig .zstem+svg.zbx{margin-top:4px}
svg.zbd circle{transition:fill .3s}svg.zbd circle.on{fill:#d00000}
.zbig{display:flex;justify-content:center;margin:14px 0 6px}.zbig svg.zbx{max-height:290px}
.zrow3{display:grid;grid-template-columns:1fr 1fr 1fr 1.3fr;gap:16px;margin-top:6px}
.zrow3 .st{font-size:21px!important;white-space:normal}
.zsh4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;margin:14px 0}
.zsh4 .st{border:2px solid #000;padding:10px;font-size:19px!important;white-space:normal;box-shadow:4px 4px 0 #bbb}
.zsh4 h3{margin:0 0 6px;font-size:22px}
.ztab.zh5{font-size:16px}.ztab.zhep{font-size:12px}.ztab.zhep th,.ztab.zhep td{padding:1px 3px}
.zmc1 .pc{display:none}
.zcas2.zh{flex-direction:row}.zcas2.zh>div{flex:1}.zcas2.zh .zcas{font-size:22px!important}
.zfxo{font-size:20px;line-height:1.55}.zfxo .ol{color:#d00000;font-weight:bold}
.slide.z .st.final svg.zbx{max-height:170px;display:block;margin-top:4px;background:#fff}
</style></head>''')
TAIL = TAIL.replace('</body>', r'''<script>
function bxApply(sl){const V=new Map();sl.querySelectorAll('svg.zbx').forEach(sv=>V.set(sv.id,{s:new Set(),o:false}));
  sl.querySelectorAll('svg.zbd circle').forEach(c=>c.classList.remove('on'));
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const one={};s.dataset.do.split(' ').forEach(a=>{const [op,id,x]=a.split(':');const v=V.get(id);
    if(op==='bdx'){sl.querySelectorAll('#'+id+' circle[data-e]').forEach(c=>c.classList.add('on'));return}
    if(!v)return;if(op==='bx')x.split(',').forEach(p=>v.s.add(p));if(op==='bxo')v.o=true;
    if(op==='bx1'){(v.b1||[]).forEach(p=>v.s.delete(p));v.b1=x.split(',');v.b1.forEach(p=>v.s.add(p))}})});
  V.forEach((v,id)=>{const sv=document.getElementById(id);const H=new Set((sv.dataset.hide||'').split(',').filter(Boolean));
    sv.querySelectorAll('[data-p]').forEach(g=>g.style.opacity=(!H.has(g.dataset.p)||v.s.has(g.dataset.p))?1:0);
    sv.querySelectorAll('.bo').forEach(c=>c.classList.toggle('on',v.o))})}
document.querySelectorAll('.slide').forEach(bxApply);
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)){seen.add(sl);bxApply(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// party ages: one guest's age changes; quartiles by the halves method (n = 20)
document.querySelectorAll('.slide.zfx').forEach(sl=>{const sv=sl.querySelector('svg.zfxs'),r=sl.querySelector('input'),O=sl.querySelector('.zfxo');
  const base=[19,21,22,56,34,19,27,28,34,17,37,20,20,21,45,26,19,23,29];
  const md=a=>{const n=a.length,h=Math.floor(n/2);return n%2?a[h]:(a[h-1]+a[h])/2};
  const draw=()=>{const X=+r.value,d=[...base,X].sort((a,b)=>a-b),n=d.length,h=Math.floor(n/2),M=md(d),Q1=md(d.slice(0,h)),Q3=md(d.slice(n-h)),I=Q3-Q1,LF=Q1-1.5*I,UF=Q3+1.5*I;
    const ins=d.filter(v=>v>=LF&&v<=UF),wl=Math.min(...ins),wu=Math.max(...ins),outs=d.filter(v=>v<LF||v>UF);
    const lo=-10,hi=100,px=v=>30+(v-lo)/(hi-lo)*640,cy=110;let s='';
    s+=`<line x1="20" y1="185" x2="690" y2="185" stroke="#000" stroke-width="2"/>`;for(let v=-10;v<=100;v+=10)s+=`<line x1="${px(v)}" y1="179" x2="${px(v)}" y2="191" stroke="#000"/><text x="${px(v)}" y="210" font-size="15" text-anchor="middle">${v<0?'−'+(-v):v}</text>`;
    [[LF,'LF'],[UF,'UF']].forEach(([v,l])=>{s+=`<line x1="${px(v)}" y1="40" x2="${px(v)}" y2="185" stroke="#1f5fbf" stroke-width="2.5" stroke-dasharray="7 5"/><text x="${px(v)}" y="32" font-size="15" font-weight="bold" fill="#1f5fbf" text-anchor="middle">${l} = ${+v.toFixed(2)}</text>`});
    s+=`<line x1="${px(wl)}" y1="${cy}" x2="${px(Q1)}" y2="${cy}" stroke="#000" stroke-width="2.5"/><line x1="${px(Q3)}" y1="${cy}" x2="${px(wu)}" y2="${cy}" stroke="#000" stroke-width="2.5"/>`;
    s+=`<rect x="${px(Q1)}" y="${cy-28}" width="${px(Q3)-px(Q1)}" height="56" fill="#fff" stroke="#000" stroke-width="2.5"/><line x1="${px(M)}" y1="${cy-28}" x2="${px(M)}" y2="${cy+28}" stroke="#000" stroke-width="4"/>`;
    outs.forEach(v=>{s+=`<circle cx="${px(v)}" cy="${cy}" r="7" fill="#fff" stroke="#000" stroke-width="2.5"/>`});
    const xo=X<LF||X>UF;s+=`<path d="M${px(X)} ${cy+38} l-8 14 h16z" fill="${xo?'#d00000':'#555'}"/><text x="${px(X)}" y="${cy+66}" font-size="14" font-weight="bold" text-anchor="middle" fill="${xo?'#d00000':'#555'}">${X}</text>`;
    sv.innerHTML=s;const f=v=>+v.toFixed(2);
    O.innerHTML=`Changed guest: <b>${X}</b><br>$Q_1$ = <b>${f(Q1)}</b>, $M$ = <b>${f(M)}</b>, $Q_3$ = <b>${f(Q3)}</b><br>IQR = <b>${f(I)}</b><br>Fences: <b>${f(LF)}</b> and <b>${f(UF)}</b><br>Outliers: <b>${outs.length?outs.join(', '):'none'}</b><br>`+
      (xo?`<span class="ol">${X} is an outlier: it is ${X>UF?'above the upper':'below the lower'} fence.</span>`:(X===UF||X===LF?`<b style="color:#a06b00">${X} is exactly on the fence: not an outlier.</b>`:`<b>${X} is inside the fences: not an outlier.</b>`));
    if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};
  r.oninput=draw;sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();r.value=b.dataset.v;draw()});draw()});
</script></body>''')

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
  sl.querySelectorAll('.lv').forEach(l=>l.className='lv');sl.querySelectorAll('.zkey.zkh').forEach(k=>k.classList.remove('on'));
  [...sl.querySelectorAll('.st[data-do].show')].forEach(s=>{const last=s===anim;s.dataset.do.split(' ').forEach(a=>{const [op,id,x,y,c]=a.split(':');const el=document.getElementById(id);if(!el)return;
    const L=[...el.querySelectorAll('.lv')],ks=(x||'').split(',').map(Number);
    if(op==='dn'){const n=+x;for(let k=0;k<n;k++){const go=()=>{el.querySelector(`.dot[data-k="${k}"]`).setAttribute('fill','#1f5fbf');el.querySelector(`.dn[data-k="${k}"]`).setAttribute('opacity',1)};last?setTimeout(T(go),k*(1600/n)):go()}}
    if(op==='dm'){ks.forEach(k=>{const d=el.querySelector(`.dot[data-k="${k}"]`);d.setAttribute('fill','#d00000');d.setAttribute('stroke','#000');d.setAttribute('stroke-width',2)});
      const m=ks.reduce((t,k)=>t+el._v[k],0)/ks.length,X=el._px(m);el.querySelector('.mk').innerHTML=`<line x1="${X}" y1="10" x2="${X}" y2="200" stroke="#d00000" stroke-width="3" stroke-dasharray="7 5"/><text x="${X+8}" y="24" fill="#d00000" font-size="18" font-weight="bold">M = ${m}</text>`}
    if(op==='hc'){el.querySelectorAll('.cu').forEach((t,i)=>{const go=()=>t.setAttribute('opacity',1);last?setTimeout(T(go),i*260):go()})}
    if(op==='hm'||op==='hq')ks.forEach(i=>el.querySelector(`rect.b[data-i="${i}"]`).setAttribute('fill',op==='hm'?'#f6b3b3':'#b9cff3'));
    if(op==='lb')L.slice(+x,+y+1).forEach(l=>l.classList.add(c));
    if(op==='sk')el.querySelector('.zkey').classList.add('on');
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
// ---- stem plot standard: biggest font (same for stems and leaves) that fits the figure box; key scales with it
function zstemfit(){document.querySelectorAll('.st[data-do]').forEach(t=>t.dataset.do.split(' ').forEach(a=>{const [op,id]=a.split(':');if(op==='ln'){const z=document.getElementById(id);if(z&&z.classList.contains('zstem'))z.classList.add('zcnt')}}));document.querySelectorAll('.slide.z').forEach(sl=>{const st=[...sl.querySelectorAll('.zstem')];if(!st.length)return;const was=sl.classList.contains('on');sl.classList.add('on');
  st.forEach(z=>{const fg=z.closest('.zfig')||z.parentNode;let f=z.dataset.max?+z.dataset.max:48;const bx=fg.querySelector('svg.zbx');const row=getComputedStyle(fg).flexDirection==='row';const ok=()=>(!bx||(row?bx.getBoundingClientRect().width>=300:bx.getBoundingClientRect().height>=110))&&fg.scrollHeight<=fg.clientHeight+1&&z.scrollWidth<=fg.clientWidth-8&&z.offsetWidth<=fg.clientWidth-8;
    z.style.setProperty('--zsf',f+'px');while(!ok()&&f>16){f-=1;z.style.setProperty('--zsf',f+'px')}});
  if(!was)sl.classList.remove('on')})}
document.fonts.ready.then(()=>setTimeout(zstemfit,900));
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
