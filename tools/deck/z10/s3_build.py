r"""12MAG S3 (1F Measures of centre and spread) rebuilt in the 10MA slide house style.
Shell (CSS + navigation/tile engine JS) copied from 10MA '10MAG Univariate Statistics - Slides.html'.
python3 build.py  ->  12MAG S3 - Slides (10MA style).html
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
S.append(f'<section class="slide title cover"><h1>Measures of centre and spread</h1>'
         f'<div class="unit">12MAG · Unit 3 · AOS 1 Data analysis</div>'
         f'<div class="pp" style="font-size:22px;margin-top:14px">{CG}</div>'
         f'<ul style="list-style:none;padding:0;margin:10px 0 0;font-size:22px;line-height:1.5;text-align:left"><li>1F Using summary statistics to describe numerical distributions (pp. 44–54)</li></ul><span class="pg" style="display:none"></span></section>')
LI = ['To be able to understand the mean and the median as measures of centre.',
      'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
      'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.',
      'To be able to use a CAS calculator to calculate these summary statistics.']
SC = ['I can find the median value in a data set.', 'I can find the median value from a dot plot.', 'I can find the median value from a stem plot.',
      'I can find the range from a stem plot.', 'I can find the IQR from a stem plot when n is even.', 'I can find the IQR from a stem plot when n is odd.',
      'I can calculate the mean using the formula.', 'I can calculate the mean and standard deviation using the CAS calculator.']
SEQ = ['CFAT 1.1.1 (20 minutes, 1A–1E)', 'Activating prior knowledge', 'Key ideas and formulas',
       'The median · Examples 14–16', 'Quartiles, range and IQR · Examples 17–20', 'Exam practice: median from a histogram', 'The mean · Example 21',
       'Exam practice: working back from a mean', 'Mean or median? Standard deviation', 'Mean and standard deviation on CAS', 'Exit task', 'Check-in and coursework']
S.append(f'<section class="slide z li">{bar("1F", "Learning intentions")}<div class="cols" style="grid-template-columns:1.05fr 1.05fr .9fr">'
         f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
         f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
         f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
         f'{foot(CG + ", 1F Learning intentions (p. 44); success criteria: one per worked example")}</section>')
S.append(f'<section class="slide z cfat">{bar("CFAT 1.1.1", "Types of data, displays, log scales")}'
         '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
         '<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · 13 marks</li>'
         '<li>Covers 1A–1E</li><li>Pens down when the timer ends</li></ul></div>'
         '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
         '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
         f'{foot("CFAT 1.1.1 (1A–1E): student copy and solutions on the planner")}</section>')

# APK 1
ages = stem('apk', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17')
APKQ = ('The ages of a group of people at a party:<br>19 21 22 56 34 19 27 28 34 17 66 37 20 20 21 45 26 19 23 29<br>')
S.append(qslide('apk', '1 of 3', 'Year 11 skills: centre', 'Cambridge U1&amp;2 · 2E #10',
    APKQ, KI_MED, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2E #10. Working by teacher.',
    parts=[('a', 'Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?',
      [r'$\bar{x} = \dfrac{583}{20} = 29.15$', (r'$n = 20$: average the 10th and 11th values', 'ln:apk:0:11 lm:apk:9,10'),
       (r'$M = \dfrac{23 + 26}{2} = 24.5$', 'ln:apk:0:11 lm:apk:9,10'), ('Outliers (56, 66) and a skewed shape pull the mean up.', 'ln:apk:0:11 lm:apk:9,10')],
      r'$\bar{x} = 29.15$, $M = 24.5$: the <b>median</b> is preferred.', 'ln:apk:0:11 lm:apk:9,10')],
    fig=stem('apk', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17'), figw='.9fr', cmd='<b>DETERMINE</b> · values, then a choice'))
S.append(qslide('apk', '2 of 3', 'Year 11 skills: spread', 'Cambridge U1&amp;2 · 2F #11',
    APKQ, KI_IQR, [], None,
    'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2F #11. Working by teacher.',
    parts=[('b', 'Determine the quartiles and hence the IQR of the ages of the people at the party.', [('$n = 20$: ten values in each half, split on the median line', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi'),
             (r'$Q_1 = \dfrac{20 + 20}{2} = 20$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5'),
             (r'$Q_3 = \dfrac{34 + 34}{2} = 34$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5,14,15')],
    r'$Q_1 = 20$, $Q_3 = 34$, $\boldsymbol{\text{IQR} = 14}$', 'lm:apk2:9,10 lb:apk2:0:9:lo lb:apk2:10:19:hi lq:apk2:4,5,14,15')],
    fig=stem('apk2', [('1', '7 9 9 9'), ('2', '0 0 1 1 2 3 6 7 8 9'), ('3', '4 4 7'), ('4', '5'), ('5', '6'), ('6', '6')], 'Key: 1 | 7 = 17'), figw='.9fr', cmd='<b>DETERMINE</b> · quartiles, then IQR'))
# APK 2 (exam short answer)
S.append(qslide('apk', '3 of 3', 'A real VCAA question you can already do', 'VCAA 2017 Exam 2 Q1ai',
    'The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.'
    + table_hl('egg', [('number of eggs', ['172', '192', '159', '125', '197', '135']), ('', ['140', '140', '138', '166', '136', '131'])], 'ztab zv zinq zbig')
    + 'From the information given, determine the range.',
    KI_RANGE, [('Scan the table for the extremes: largest = 197, smallest = 125', 'tc:egg:4,3'), (r'$\text{range} = 197 - 125$', 'tc:egg:4,3')],
    r'$\boldsymbol{\text{range} = 72 \text{ eggs}}$',
    'Edrolo General Mathematics Units 1&amp;2, 1D Q18 (VCAA 2017 Exam 2 Data analysis Q1ai). Working by teacher.',
    marks=1, cmd='<b>DETERMINE</b> · one value', vcaa=87, figw='1.1fr', ans_do='tc:egg:4,3', watch='the range is one number (72), not “125 to 197”.'))

# Key ideas
KD = [('Median ($M$)', 'the middle value of the ordered data'), (r'Mean ($\bar{x}$)', 'the sum of the values divided by $n$: the balance point'),
      ('Range', 'largest value minus smallest value'),
      ('Quartiles ($Q_1$, $Q_3$)', 'split the ordered data into four equal groups; $Q_1$ = median of the lower half, $Q_3$ = median of the upper half'),
      ('IQR', 'the spread of the middle 50% of the data'), ('Standard deviation ($s$)', 'the spread of the data around the mean; on CAS it is $s_x$')]
KF = [('Median position', r'$\text{position} = \dfrac{n + 1}{2}$'), ('Median, $n$ even', r'$M = \dfrac{\text{first middle} + \text{second middle}}{2}$'),
      ('Range', r'$\text{range} = \text{largest} - \text{smallest}$'), ('Interquartile range', r'$\text{IQR} = Q_3 - Q_1$'),
      ('Mean', r'$\bar{x} = \dfrac{\Sigma x}{n}$'), ('Standard deviation', r'$s = \sqrt{\dfrac{\Sigma (x - \bar{x})^2}{n - 1}}$ &nbsp;<span class="zn">use CAS: $s_x$, not $\sigma_x$</span>')]
S.append(f'<section class="slide z kif">{bar("1F", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1F Key ideas (pp. 44–52)")}</section>')

# NL: pairs
S.append(nl_slide('Two questions about any distribution',
    'Where is the <b>centre</b>? How <b>spread out</b> is it? <span class="hint">Click to reveal the pairs.</span>',
    r'<div class="zpair"><div class="zpc"><div class="zpt">Centre</div><div class="zbox" id="pM">median $M$<i class="zsub">the middle value</i></div><div class="zbox" id="pX">mean $\bar{x}$<i class="zsub">the balance point</i></div></div>'
    '<div class="zpm">' + st('<span class="zarr">median ⟷ IQR</span><br>resistant: outliers barely move them', do='pair:pM:pI') + st('<span class="zarr">mean ⟷ standard deviation</span><br>use when symmetric, no outliers', do='pair:pM:pI pair2:pX:pS') + '</div>'
    r'<div class="zpc"><div class="zpt">Spread</div><div class="zbox">range<i class="zsub">largest − smallest</i></div><div class="zbox" id="pI">IQR<i class="zsub">the middle 50%</i></div><div class="zbox" id="pS">standard deviation $s$<i class="zsub">spread around the mean</i></div></div></div>'
    + st('<b>They come in pairs.</b> In a SOCS answer, the C and the S lines use the same pair.', True, cls='zctr', do='pair:pM:pI pair2:pX:pS'),
    CG + ', 1F pp. 44, 50–52'))

def nl_median():
    o = [19, 3, 26, 12, 34, 1, 24, 15, 30, 21, 27]; e = [9, 3, 12, 5, 10, 2, 14, 6, 11, 4]
    col = lambda h, t, d, n, last: (f'<div class="col"><h2>{h}</h2>{tiles(t, d)}'
        f'<div class="st stp" data-act="sort:{t}"><b>Step 1</b> Write the data in order. Count them: $n = {n}$</div>'
        f'<div class="st stp" data-do="tn:{t}:0:{6}"><b>Step 2</b> Median position $= \\tfrac{{{n} + 1}}{{2}} = $ {"6th" if n == 11 else "5.5th"}. Count along to it.</div>'
        f'<div class="st stp" data-act="mid:{t}:0:{n-1}:mid">{last}</div>'
        '</div>')
    return nl_slide('The median: the middle value',
        'The <b>median</b> is the middle value in an ordered data set. <span class="hint">Click to find the median.</span>',
        '<div class="cols" style="grid-template-columns:1fr 1fr">' + col('Odd number of values', 'o', o, 11, '<b>Step 3</b> The 6th value is the median. <b>Median $= 21$</b>')
        + col('Even number of values', 'e', e, 10, '<b>Step 3</b> 5.5th: halfway between the 5th and 6th values, $6$ and $9$. <b>Median $= \\tfrac{6 + 9}{2} = 7.5$</b>') + '</div>',
        CG + ', 1F p. 44. Data and steps by teacher (as in the 10MA deck).', 'eng')
S.append(nl_median())

# Example 14 (tiles are the data)
a14 = [2, 9, 1, 8, 3, 5, 3, 8, 1]; b14 = [10, 1, 3, 4, 8, 6, 10, 1, 2, 9]
S.append(qslide('ex', 14, 'Finding the median value in a data set', 'Cambridge · Example 14',
    'Order each of the following data sets, locate the median, and then write down its value.', KI_MED, [], None,
    CG + ', 1F Example 14 (p. 45); cross-off steps by teacher',
    parts=[('a', '2 &nbsp;9 &nbsp;1 &nbsp;8 &nbsp;3 &nbsp;5 &nbsp;3 &nbsp;8 &nbsp;1', [('Order: $n = 9$ (odd)', 'sort:a'), (r'Median position $= \dfrac{9 + 1}{2} = $ 5th value', 'sort:a'),
             ('Count along to the 5th value.', 'sort:a tn:a:0:5 mid:a:0:8:mid')], r'$\boldsymbol{M = 3}$', 'sort:a tn:a:0:5 mid:a:0:8:mid'),
           ('b', '10 &nbsp;1 &nbsp;3 &nbsp;4 &nbsp;8 &nbsp;6 &nbsp;10 &nbsp;1 &nbsp;2 &nbsp;9', [('Order: $n = 10$ (even)', 'sort:b'), (r'Median position $= \dfrac{10 + 1}{2} = $ 5.5th: average the 5th and 6th', 'sort:b'),
             ('Count along to the 5th and 6th values: $4$ and $6$', 'sort:b tn:b:0:6 mid:b:0:9:mid')], r'$\boldsymbol{M = \dfrac{4 + 6}{2} = 5}$', 'sort:b tn:b:0:6 mid:b:0:9:mid')],
    fig=tilerow('a', 'a', a14) + tilerow('b', 'b', b14), cmd='<b>LOCATE</b> · order first, then count in', cls='eng', stack=True))
# You try 14: adapted, median only
y14 = [3, 5, 1, 10, 8, 9, 6, 3, 8, 6]
S.append(qslide('yt', 14, 'Finding the median value in a data set', 'Edrolo 1E WE1 data (adapted)',
    'Order the following data set, locate the median, and then write down its value.', KI_MED,
    [('Order: $n = 10$ (even)', 'sort:y'), (r'Median position $= \dfrac{10 + 1}{2} = $ 5.5th: average the 5th and 6th', 'sort:y'),
     ('Count along to the 5th and 6th values: $6$ and $6$', 'sort:y tn:y:0:6 mid:y:0:9:mid')],
    r'$\boldsymbol{M = \dfrac{6 + 6}{2} = 6}$',
    ED + ', 1E Worked example 1 data; question adapted (median only) to match Example 14. The full five-number summary comes after quartiles.',
    fig=tiles('y', y14), figw='1fr', cmd='<b>LOCATE</b> · order first, then count in', cls='eng'))

# Example 15 / You try 15: dot plots
cr = [18, 18, 19, 19, 22, 22, 22, 22, 23, 23, 24, 25, 29]
S.append(qslide('ex', 15, 'Finding the median value from a dot plot', 'Cambridge · Example 15',
    'The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team. Determine the median age of these cricketers and mark its location on the dot plot.',
    KI_MED, ['Count: $n = 13$ dots', r'Median position $= \dfrac{13 + 1}{2} = $ 7th value',
             ('Count in from the left (each column bottom to top): 18, 18, 19, 19, 22, 22, <b>22</b>', 'dn:d15:7')],
    'The median age is <b>22 years</b> (marked on the plot).', CG + ', 1F Example 15 (p. 45)',
    fig=dotplot('d15', cr, 17, 30, 'Age (years)'), figw='1.2fr', cmd='<b>DETERMINE</b> · the value, marked on the plot', ans_do='dn:d15:7 dm:d15:6'))
yd = [23, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29, 29, 30, 31]
S.append(qslide('yt', 15, 'Finding the median value from a dot plot', 'Edrolo 1F WE2a',
    'Consider the dot plot.<br><b>a.</b> Determine the median.', KI_MED,
    ['Count: $n = 28$ data points', (r'Median position $= \dfrac{28 + 1}{2} = $ 14.5th: average the 14th and 15th', 'dn:y15:15'),
     (r'$M = \dfrac{27 + 27}{2}$', 'dn:y15:15 dm:y15:13,14')],
    r'$\boldsymbol{M = 27}$', ED + ', 1F Worked example 2a. Working by teacher.',
    fig=dotplot('y15', yd, 22, 31), figw='1.2fr', cmd='<b>DETERMINE</b> · one value', ans_do='dn:y15:15 dm:y15:13,14'))

# Example 16 / You try 16: stem plots
temp = [('1', '8 9 9'), ('2', '0 2 5 7 8 9 9'), ('3', '1 3')]
S.append(qslide('ex', 16, 'Finding the median value from a stem plot', 'Cambridge · Example 16',
    'The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the median maximum temperature for these 12 days.',
    KI_MED, [r'Median position $= \dfrac{12 + 1}{2} = $ 6.5th: average the 6th and 7th',
             ('Count to the 6th and 7th values: 25 and 27', 'ln:s16:0:7 lm:s16:5,6'), (r'$M = \dfrac{25 + 27}{2}$', 'ln:s16:0:7 lm:s16:5,6')],
    r'$\boldsymbol{M = 26^\circ\text{C}}$', CG + ', 1F Example 16 (p. 46)',
    fig=stem('s16', temp, 'Key: 0 | 8 = 8°C'), figw='.85fr', cmd='<b>DETERMINE</b> · one value', ans_do='ln:s16:0:7 lm:s16:5,6'))
ed = [('40', '7'), ('41', ''), ('42', ''), ('43', ''), ('44', '4 6'), ('45', '1 3 3'), ('46', '2 6 7'), ('47', '4 7 8 9'), ('48', '0 0 4 5 6 8'), ('49', '1 2 5 5 5 9'), ('50', '3 4 4 7 8 8 9 9')]
S.append(qslide('yt', 16, 'Finding the median value from a stem plot', 'Edrolo 1F WE3a',
    'Consider the stem plot.<br><b>a.</b> Calculate the median.', KI_MED,
    ['Count: $n = 33$ data points', r'Median position $= \dfrac{33 + 1}{2} = $ 17th', ('Count along to the 17th value', 'ln:y16:0:17 lm:y16:16')],
    r'$\boldsymbol{M = 485}$', ED + ', 1F Worked example 3a. Working by teacher.',
    fig=stem('y16', ed, 'Key: 40 | 7 = 407'), figw='1.15fr', cmd='<b>CALCULATE</b> · one value', ans_do='ln:y16:0:17 lm:y16:16'))

# NL quartiles
def nl_q():
    def col(h, t, d, steps):
        return f'<div class="col"><h2>{h}</h2>{tiles(t, d)}' + ''.join(st(x, do=a or None, cls='stp').replace('st zs','st') for a, x in steps) + '</div>'
    A = [6, 2, 9, 1, 5, 7, 2, 6, 3]; B = [8, 3, 9, 2, 9, 4, 7, 3, 9, 8]
    ca = col('Odd number of values', 'a', A, [('sort:a', '<b>1</b> Order the data. $n = 9$'), ('tn:a:0:5 mid:a:0:8:mid', '<b>2</b> Median: count to the 5th value. <b>$M = 5$</b>'),
        ('tclr:a clr:a band:a:0:3:lo band:a:5:8:hi mid:a:4:4:mid', '<b>3</b> Split into halves. With an odd $n$, <b>leave the median out</b>.'),
        ('tn:a:0:3 mid:a:0:3:q', '<b>4</b> Lower half (4 values): 2.5th position. <b>$Q_1 = \\tfrac{2 + 2}{2} = 2$</b>'), ('tclr:a tn:a:5:3 mid:a:5:8:q', '<b>5</b> Upper half: 2.5th position. <b>$Q_3 = \\tfrac{6 + 7}{2} = 6.5$</b>'), ('', '<b>$\\text{IQR} = 6.5 - 2 = 4.5$</b>')])
    cb = col('Even number of values', 'b', B, [('sort:b', '<b>1</b> Order the data. $n = 10$'), ('tn:b:0:6 mid:b:0:9:mid', '<b>2</b> Median: count to the 5.5th position. <b>$M = \\tfrac{7 + 8}{2} = 7.5$</b>'),
        ('tclr:b clr:b band:b:0:4:lo band:b:5:9:hi mid:b:0:9:mid', '<b>3</b> Split into halves (5 values each), on the median line.'),
        ('tn:b:0:3 mid:b:0:4:q', '<b>4</b> Lower half (5 values): 3rd position. <b>$Q_1 = 3$</b>'), ('tclr:b tn:b:5:3 mid:b:5:9:q', '<b>5</b> Upper half: 3rd position. <b>$Q_3 = 9$</b>'), ('', '<b>$\\text{IQR} = 9 - 3 = 6$</b>')])
    return nl_slide('Quartiles cut the ordered data into quarters',
        r'Quartiles are just <b>medians of each half</b>. $\text{IQR} = Q_3 - Q_1$ is the spread of the middle 50%. <span class="hint">Click to find each quartile.</span>',
        f'<div class="cols" style="grid-template-columns:1fr 1fr">{ca}{cb}</div>', CG + ', 1F pp. 46–47. Data and steps by teacher (as in the 10MA deck).', 'eng')
S.append(nl_q())
# You try: full five-number summary (Edrolo 1E WE1), now after quartiles
S.append(qslide('yt', '', 'Five-number summary', 'Edrolo 1E WE1',
    'Construct a five-number summary for the following data.', KI_IQR,
    [('Order: $n = 10$; min $= 1$, max $= 10$', 'sort:f fill:f5:0 fill:f5:4'),
     (r'Median: 5.5th position, $M = \dfrac{6 + 6}{2} = 6$', 'sort:f tn:f:0:6 mid:f:0:9:mid fill:f5:0 fill:f5:4 fill:f5:2'),
     ('$n$ is even: five values in each half', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid fill:f5:0 fill:f5:4 fill:f5:2'),
     ('$Q_1$: 3rd value of the lower half $= 3$', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid tn:f:0:3 mid:f:0:4:q fill:f5:0 fill:f5:4 fill:f5:2 fill:f5:1'),
     ('$Q_3$: 3rd value of the upper half $= 8$', 'sort:f band:f:0:4:lo band:f:5:9:hi mid:f:0:9:mid mid:f:0:4:q tn:f:5:3 mid:f:5:9:q fill:f5:0 fill:f5:4 fill:f5:2 fill:f5:1 fill:f5:3')],
    '<b>1, 3, 6, 8, 10</b> (min, $Q_1$, $M$, $Q_3$, max)', ED + ', 1E Worked example 1. Working by teacher.',
    fig=tiles('f', y14) + five('f5', [1, 3, 6, 8, 10]), figw='1fr', cmd='<b>CONSTRUCT</b> · min, $Q_1$, $M$, $Q_3$, max', cls='eng'))

# Example 17 / You try 17
S.append(qslide('ex', 17, 'Finding the range from a stem plot', 'Cambridge · Example 17',
    'The stem plot opposite displays the maximum temperature (in °C) for 12 days in January. Determine the temperature range over these 12 days.',
    KI_RANGE, [('Lowest = 18, highest = 33', 'lx:s17:0,11'), (r'$R = 33 - 18$', 'lx:s17:0,11')],
    r'$\boldsymbol{R = 15^\circ\text{C}}$', CG + ', 1F Example 17 (p. 46)',
    fig=stem('s17', temp, 'Key: 0 | 8 = 8°C'), figw='.85fr', cmd='<b>DETERMINE</b> · one value with units', ans_do='lx:s17:0,11'))
nb = [('2', '2 3 5 7 9'), ('3', '0 1 3 5 7 7 8'), ('4', '0 1 2 2')]
S.append(qslide('yt', 17, 'Finding the range from a stem plot', 'Edrolo 1E WE2a',
    'The following stem plot displays the number of goals scored by 16 netball teams over a season.<br><b>a.</b> Calculate the range of goals scored.',
    KI_RANGE, [('Lowest = 22, highest = 42', 'lx:y17:0,15'), (r'$R = 42 - 22$', 'lx:y17:0,15')],
    r'$\boldsymbol{R = 20 \text{ goals}}$', ED + ', 1E Worked example 2a. Working by teacher.',
    fig=stem('y17', nb, 'Key: 2 | 2 = 22 goals'), figw='.85fr', cmd='<b>CALCULATE</b> · one value', ans_do='lx:y17:0,15'))

# Example 18 / You try 18 / Example 19
cats = [('1', '9'), ('2', '1 3 5 8'), ('3', '0 0 4 9 9'), ('4', '0 4 5 8'), ('5', '0 3'), ('6', '3 4')]
H18 = 'lm:s18:8,9 lb:s18:0:8:lo lb:s18:9:17:hi'
S.append(qslide('ex', 18, 'Finding the IQR from an ordered stem plot when n is even', 'Cambridge · Example 18',
    'Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.', KI_IQR,
    [('18 values: split on the median line, nine in each half', H18), ('Lower half: 5th value', H18 + ' lq:s18:4'),
     ('$Q_1 = 2.8$', H18 + ' lq:s18:4'), ('Upper half: 5th value', H18 + ' lq:s18:4,13'), ('$Q_3 = 4.8$', H18 + ' lq:s18:4,13'), (r'$\text{IQR} = 4.8 - 2.8$', H18 + ' lq:s18:4,13')],
    r'$\boldsymbol{\text{IQR} = 2.0 \text{ kg}}$', CG + ', 1F Example 18 (p. 47)',
    fig=stem('s18', cats, 'Weight (kg) · 1 | 2 represents 1.2 kg'), figw='.85fr', cmd='<b>FIND</b> · $Q_1$, $Q_3$, then IQR', ans_do=H18 + ' lq:s18:4,13'))
H18y = 'lm:y18:7,8 lb:y18:0:7:lo lb:y18:8:15:hi'
S.append(qslide('yt', 18, 'Finding the IQR from an ordered stem plot when n is even', 'Edrolo 1E WE2b',
    'The following stem plot displays the number of goals scored by 16 netball teams over a season.<br><b>b.</b> Calculate the IQR of goals scored.', KI_IQR,
    [('16 values: split on the median line, eight in each half', H18y), (r'$Q_1 = \dfrac{27 + 29}{2} = 28$', H18y + ' lq:y18:3,4'),
     (r'$Q_3 = \dfrac{38 + 40}{2} = 39$', H18y + ' lq:y18:3,4,11,12'), (r'$\text{IQR} = 39 - 28$', H18y + ' lq:y18:3,4,11,12')],
    r'$\boldsymbol{\text{IQR} = 11 \text{ goals}}$', ED + ', 1E Worked example 2b. Working by teacher.',
    fig=stem('y18', nb, 'Key: 2 | 2 = 22 goals'), figw='.85fr', cmd='<b>CALCULATE</b> · $Q_1$, $Q_3$, then IQR', ans_do=H18y + ' lq:y18:3,4,11,12'))
life = [('5', '2'), ('5', '5 6'), ('6', '4'), ('6', '6 6 7 9'), ('7', '1 2 2 3 3 4 4 4 4'), ('7', '5 5 6 6 7 7')]
H19 = 'lm:s19:11 lb:s19:0:10:lo lb:s19:12:22:hi'
S.append(qslide('ex', 19, 'Finding the IQR from an ordered stem plot when n is odd', 'Cambridge · Example 19',
    'The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.', KI_IQR,
    [('23 values: median position 12th. Count to it: 73', 'ln:s19:0:12 lm:s19:11'), ('$n$ is odd: leave the median out. 11 values below, 11 above.', H19),
     ('$Q_1$ = middle (6th) of the bottom 11 $= 66$', H19 + ' lq:s19:5'), ('$Q_3$ = middle (6th) of the top 11 $= 75$', H19 + ' lq:s19:5,17'),
     (r'$\text{IQR} = 75 - 66$', H19 + ' lq:s19:5,17')],
    r'$\boldsymbol{\text{IQR} = 9 \text{ years}}$', CG + ', 1F Example 19 (p. 48). No matching Edrolo worked example, so no You try.',
    fig=stem('s19', life, 'Stem: 5 | 2 = 52 years'), figw='.85fr', cmd='<b>FIND</b> · $Q_1$, $Q_3$, then IQR', ans_do=H19 + ' lq:s19:5,17'))

# Example 20 / You try 20 / exam MC
S.append(qslide('ex', 20, 'Finding the median and quartiles from a histogram', 'Cambridge · Example 20',
    'The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.', KI_MEDH,
    [r'Median position $= \dfrac{23 + 1}{2} = $ 12th value', ('Running totals from the left: 1, 3, 7, 12, …', 'hc:h20'),
     ('Median: the 12th value is in the 60–70 interval', 'hc:h20 hm:h20:5'),
     (r'$Q_1$: 11 values below the median, $\tfrac{11 + 1}{2} = $ 6th from the bottom: 50–60', 'hc:h20 hm:h20:5 hq:h20:4'),
     ('$Q_3$: 6th value from the top (2 + 6 = 8, so it is in the 80–90 interval)', 'hc:h20 hm:h20:5 hq:h20:4,7')],
    'Median 60–70 hours · $Q_1$ 50–60 hours · $Q_3$ 80–90 hours', CG + ', 1F Example 20 (p. 49)',
    fig=hist('h20', 10, 10, [1, 0, 0, 2, 4, 5, 3, 6, 2], 7, 1, 'internet hours per week'), figw='1.1fr', cmd='<b>FIND</b> · an interval for each'))
S.append(qslide('yt', 20, 'Finding the median and quartiles from a histogram', 'Edrolo 1F WE1a',
    'Consider the histogram.<br><b>a.</b> Estimate the median.', KI_MEDH,
    [r'Count: $3 + 15 + 12 + 13 + 9 + 5 + 2 = 59$', r'Median position $= \dfrac{59 + 1}{2} = $ 30th value',
     ('Running totals 3, 18, 30: the 30th value is in the 3–&lt;4 interval', 'hc:y20 hm:y20:2'), (r'Estimate the middle of the interval: $\dfrac{3 + 4}{2}$', 'hc:y20 hm:y20:2')],
    r'$\boldsymbol{M \approx 3.5}$', ED + ', 1F Worked example 1a. Working by teacher.',
    fig=hist('y20', 1, 1, [3, 15, 12, 13, 9, 5, 2], 16, 4, '', 'frequency'), figw='1.1fr', cmd='<b>ESTIMATE</b> · one value'))
OPTDIST['VCAA 2024 Exam 1 Q3'] = [18, 5, 7, 71]
S.append(qslide('exam', '', 'VCAA 2024 Exam 1 Q3', 'Median from a histogram',
    'The histogram below displays the population density, in people per km<sup>2</sup>, of the 27 countries in the European Union in 2021. The histogram has a logarithmic (base 10) scale.<br>The median value occurs in a column with a frequency of',
    KI_MEDH, [r'27 values: median position $= \dfrac{27 + 1}{2} = $ 14th value', ('Running totals: 2, 4, 6, 12, 21', 'hc:m3'),
              ('The 14th value is in the 2.0–2.2 column', 'hc:m3 hm:m3:5')],
    'frequency 9', 'VCAA 2024 General Mathematics Exam 1 Q3–4 stem and Q3; % from the examiner report. Histogram redrawn.',
    fig=hist('m3', 1.0, 0.2, [0, 2, 2, 2, 6, 9, 3, 1, 1, 0, 0, 1, 0], 10, 2, 'log<tspan baseline-shift="sub" font-size="11">10</tspan> (population density)', 'frequency'),
    figw='1.15fr', marks=1, cmd='<b>CHOOSE</b> · one option', vcaa=71, opts=[('A', '2'), ('B', '3'), ('C', '6'), ('D', '9')], key='D',
    dis=('A', '18% chose 2, the median of the <b>column heights</b> (1, 1, 1, 2, 2, 2, 3, 6, 9), not of the 27 <b>data values</b>. <span class="zsc">(likely reason: teacher comment)</span>')))

# Example 21 / You try 21 / exam MC
S.append(qslide('ex', 21, 'Calculating the mean from the formula', 'Cambridge · Example 21',
    'The following is a set of reaction times (in milliseconds). Write down the values of the following, correct to one decimal place.', KI_MEAN, [], None,
    CG + ', 1F Example 21 (p. 50)',
    parts=[('a', '$n$', [('Count the data values.', 'cnt:r21')], r'$\boldsymbol{n = 8}$', 'cnt:r21'),
           ('b', r'$\Sigma x$', [('Add them up.', 'cnt:r21 sum:r21')], r'$\boldsymbol{\Sigma x = 335}$', 'cnt:r21 sum:r21'),
           ('c', r'$\bar{x}$', [(r'$\bar{x} = \dfrac{\Sigma x}{n} = \dfrac{335}{8} = 41.875$', 'cnt:r21 sum:r21 bal:r21:41.875')], r'$\boldsymbol{\bar{x} = 41.9}$', 'cnt:r21 sum:r21 bal:r21:41.875')],
    fig=sumtiles("r21", [38, 36, 35, 43, 46, 64, 48, 25]), figw=".62fr", cmd='<b>WRITE DOWN</b> · three values', cls='tight'))
S.append(qslide('yt', 21, 'Calculating the mean from the formula', 'Edrolo 1G WE1',
    'The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.', KI_MEAN,
    [('Add the 10 amounts: $\\Sigma x = 273$', 'sum:y21'), ('Count: $n = 10$ customers', 'sum:y21 cnt:y21'), (r'$\bar{x} = \dfrac{273}{10} = 27.3$', 'sum:y21 cnt:y21 bal:y21:27.30')],
    'The mean amount spent is <b><span class="nomath">$</span>27.30</b>.', ED + ', 1G Worked example 1. Working by teacher.',
    fig=sumtiles('y21', ['11.60', '55.50', '7.95', '42.15', '17.10', '2.00', '82.55', '26.85', '5.40', '21.90']), figw='1fr',
    cmd='<b>CALCULATE</b> · one value in dollars', ans_do='sum:y21 cnt:y21 bal:y21:27.30'))
OPTDIST['VCAA 2024 Exam 1 Q14'] = [15, 68, 12, 5]
S.append(qslide('exam', '', 'VCAA 2024 Exam 1 Q14', 'Working back from a mean',
    'A school runs an orientation program for new staff each January. The time series plot below shows the number of new staff, <i>new</i>, for each year, <i>year</i>, from 2011 to 2022 (inclusive).'
    '<br>The number of new staff in 2023 is added to the total number of new staff from the previous 12 years. For these 13 years, the mean number of new staff is 11.<br>The number of new staff in 2023 is',
    KI_MEAN, [r'Total for 13 years $= 11 \times 13 = 143$', ('Total for 12 years $= 14 + 11 + 7 + \\cdots + 10 = 127$', 'tc:t14:' + ','.join(str(100 + c) for c in range(12))),
              r'2023 $= 143 - 127 = 16$'],
    '16 new staff',
    'VCAA 2024 General Mathematics Exam 1 Q13–14 stem and Q14; % and distractor from the examiner report. Time series plot shown as a table of its values (as in 12MAG 3A).',
    fig=table_hl('t14', [('<i>year</i>', [str(y) for y in range(2011, 2023)]), ('<i>new</i>', ['14', '11', '7', '6', '11', '13', '12', '6', '10', '15', '12', '10'])], 'ztab zsm2') + '<div class="zsc">(values read off the time series plot)</div>',
    figw='1.15fr', marks=1, cmd='<b>CHOOSE</b> · one option', vcaa=68, opts=[('A', '11'), ('B', '16'), ('C', '17'), ('D', '19')], key='B',
    dis=('A', '15% chose the mean itself, 11: the new value has to pull the total up to 143.')))

# NL house prices
S.append(f'<section class="slide z nl house">{bar("New learning", "Mean or median? House prices")}'
    '<div class="ctx">Eight houses sold in a suburb this year. Then one owner either <b>knocks the house down</b> and sells the empty block cheaply, '
    'or <b>builds a mansion</b> and sells it for millions. Drag the slider (or tap a button) to change that one sale price (the white dot). Which measure of centre still describes a <b>typical</b> house?</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>House sale prices ($ thousands)</h2>'
    '<svg class="zhs ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>Knocked down</span><input type="range" min="50" max="3000" step="10" value="760"><span>Mansion</span></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-v="120">Knock it down ($120k)</button><button data-v="760">Typical ($760k)</button><button data-v="1000">Renovated ($1m)</button><button data-v="2800">Mansion ($2.8m)</button></div></div>'
    '<div class="col"><h2>Live summary</h2><div class="zhso"></div>'
    '<div class="zrule">If the distribution is <b>symmetric and there are no outliers</b>, either the mean or the median can be used. '
    'If it is <b>clearly skewed and/or there are outliers</b>, it is more appropriate to use the <b>median</b>.</div></div></div>'
    f'{foot(CG + ", 1F p. 52 (rule). Fences: VCAA formula sheet. Prices made up by the teacher (as in the 10MA deck).")}</section>')
# NL SD
S.append(nl_slide('Standard deviation: spread around the mean',
    r'$s = \sqrt{\dfrac{\Sigma (x - \bar{x})^2}{n - 1}}$ &nbsp; roughly the typical distance of the values from the mean. <span class="hint">Drag to spread the data. The mean stays at 50.</span>',
    '<div class="cols" style="grid-template-columns:1.35fr .65fr"><div class="col"><h2>Eight test scores, mean 50</h2>'
    '<svg class="zsd ix" viewBox="0 0 700 260" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span>bunched</span><input type="range" min="0" max="100" value="35"><span>spread out</span></div></div>'
    '<div class="col"><h2>Live</h2><div class="zsdo"></div></div></div>',
    CG + ', 1F p. 52 (formula). Scores made up by the teacher.', 'sdx'))

# CAS
TI = ('Lists &amp; Spreadsheet: name a list, enter the data.', 'Add Calculator › Menu › Statistics › Stat Calculations › One-Variable Statistics.',
      'Num of Lists: 1. X1 List: the list (Frequency List: 1, or the frequency column). OK.', r'Read $\bar{x}$, $s_x$, $n$, MinX, Q₁X, MedianX, Q₃X, MaxX.')
CP = ('Statistics app: name a list, enter the data.', 'Calc › One-Variable.', r'XList: main\list; Freq: 1 (or the frequency list). OK.', r'Read $\bar{x}$, $s_x$, $n$; scroll for minX, Q₁, Med, Q₃, maxX.')
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in TI)}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in CP)}</ol></div></div>')
S.append(qslide('cas', '', 'Mean and standard deviation from a list', 'Cambridge · 1F CAS',
    'The following are the heights (in cm) of a group of women.<br>176 &nbsp;160 &nbsp;163 &nbsp;157 &nbsp;168 &nbsp;172 &nbsp;173 &nbsp;169<br>Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.',
    KI_CAS, ['Enter the 8 heights in one list.', 'One-Variable Statistics. Check $n = 8$.', r'$\bar{x} = 167.25$'],
    r'$\boldsymbol{\bar{x} = 167.25 \text{ cm},\ s_x = 6.67 \text{ cm}}$', CG + ', 1F pp. 53–54. CAS steps: planner CAS guide.',
    fig=TABS, figw='1fr', cmd='<b>DETERMINE</b> · two values, 2 d.p.'))
S.append(qslide('cas', '', 'Summary statistics from a frequency table', 'Data: Cambridge Example 15',
    'When values repeat (a dot plot or frequency table), enter each value once and its frequency in a second list. Check with the cricket team from Example 15:'
    '<table class="ztab z5b"><tr><th>age</th><td>18</td><td>19</td><td>22</td><td>23</td><td>24</td><td>25</td><td>29</td></tr><tr><th>freq</th><td>2</td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>1</td></tr></table>',
    KI_CAS, ['List 1: ages · list 2: frequencies', 'Select the frequency list in One-Variable Statistics.', 'Check $n = 13$ (the total frequency).', r'$\bar{x} = 22$, median $= 22$'],
    r'$\boldsymbol{s_x = 3.08}$', 'Data: ' + CG + ', 1F Example 15. CAS steps: planner CAS guide · ClassPad Help 402.',
    fig=TABS, figw='1fr', cmd='<b>CHECK</b> · $n$, $\\bar{x}$, $s_x$'))
S.append(qslide('yt', '', 'Mean and standard deviation on CAS', 'Edrolo 1G WE2',
    'The weight, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ weight, rounded to two decimal places.',
    KI_CAS, [('CAS: One-Variable Statistics on the list <i>weight</i>. Check $n = 10$.', 'cnt:rug'), (r'$\bar{x} = 88.5 \to 88.50$', 'cnt:rug sum:rug bal:rug:88.5'), r'$s_x = 7.230\ldots \to 7.23$'],
    r'mean $= \boldsymbol{88.50}$ kg, standard deviation $= \boldsymbol{7.23}$ kg', ED + ', 1G Worked example 2. Working by teacher.',
    fig=sumtiles('rug', [80, 95, 85, 91, 102, 93, 87, 78, 84, 90], '', 'check by hand: Σx'), figw='1fr', cmd='<b>DETERMINE</b> · two values, 2 d.p.'))

# Exit task: exam short answer
S.append(qslide('exit', '', 'Show what you know', 'VCAA 2020 Exam 2 Q4aii (adapted)',
    'The body density, in kilograms per litre, and weight, in kilograms, of a sample of 12 orangutans are shown in the table.'
    + table_hl('ora', [('body density (kg/litre)', '1.07 1.07 1.08 1.08 1.03 1.05 1.07 1.06 1.07 1.09 1.02 1.09'.split()), ('weight (kg)', '70.1 90.4 73.2 85.0 84.3 95.6 71.7 95.0 80.2 87.4 94.9 65.3'.split())], 'ztab zv zora zinq')
    + 'For these 12 orangutans, determine the mean of their body density, in kilograms per litre.',
    KI_MEAN, [('Use only the <i>body density</i> row.', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1'),
              (r'CAS One-Variable Statistics, or $\Sigma x = 12.78$', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1'),
              (r'$\bar{x} = \dfrac{12.78}{12}$', 'tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1')],
    r'$\boldsymbol{\bar{x} = 1.065 \text{ kg/litre}}$',
    ED + ', 1G Q11 · Adapted from VCAA 2020 Exam 2 Data analysis Q4aii (77% answered this type of question correctly). Working by teacher.',
    marks=1, cmd='<b>DETERMINE</b> · one value, not rounded', vcaa=77, figw='1.15fr', ans_do='tc:ora:' + ','.join(str(c) for c in range(12)) + ' dim:ora:1',
    watch='1.07 was not accepted. The examiners wanted 1.065: no rounding instruction means no rounding.'))

S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
         f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot("Success criteria: one per worked example")}</section>')
CWR=open(os.path.join(SH,'cwr.html')).read().replace('>Exercise 9A: Collecting representative data<',' textLength="344" lengthAdjust="spacingAndGlyphs">Exercise 1F: Using summary statistics<');CWL=open(os.path.join(SH,'cwl.html')).read()
S.append(f'<section class="slide cwk">{bar("1F", "Coursework · Exercise 1F")}<div class="cwgrid"><div class="cwl2">'
         '<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>'
         '<tr><th>Cambridge Exercise 1F</th><td>Q1–26</td></tr>'
         '<tr><th>Practice booklet</th><td>1F section</td></tr></tbody></table>'
         '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
         f'{CWL}</div>{CWR}</div>{foot(CG + ", Exercise 1F")}</section>')

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
