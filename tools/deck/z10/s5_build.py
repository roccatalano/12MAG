r"""12MAG S5 (1H normal distribution, z-scores · 1I populations and samples) built in the 10MA slide house style.
Shell (CSS + navigation/tile engine JS) copied from 10MA '10MAG Univariate Statistics - Slides.html'.
python3 build.py  ->  12MAG S3 - Slides (10MA style).html
"""
import json, html, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SH = os.path.join(HERE, "shell")
OUT = os.path.join(HERE, "..", "..", "..", "lessons", "S5-slides-v2.html")
HEAD = open(os.path.join(SH,'head.html')).read().replace('10MAG Univariate Statistics · Slides', '12MAG S3 · Measures of centre and spread · Slides')
TAIL = open(os.path.join(SH,'tail.html')).read()
CG = 'Cambridge General Mathematics Units 3&amp;4'
ED = 'Edrolo General Mathematics Units 3&amp;4'
SUB = '1H–1I'
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
# S5 = 1H The normal distribution and the 68–95–99.7% rule (+ standardised scores) · 1I Populations and samples.
# Content from the planner card gm12-u3-s5 and the old deck tools/deck/s5/build.py (questions there are verbatim and cited).
# 1I: Cambridge 1I is Interactive Textbook only and Edrolo has no worked example, so 1I is a New learning slide only (no question written).
SUB = '1H The normal distribution · 1I Populations and samples'
HEAD = HEAD.replace('12MAG S3 · Measures of centre and spread · Slides', '12MAG S5 · The normal distribution and standardised scores · Slides')
KI_RULE = r'about <b>68%</b>, <b>95%</b>, <b>99.7%</b> of values lie within <b>1, 2, 3</b> standard deviations of the mean<div class="kn">tails: 16% · 2.5% · 0.15% on each side</div>'
KI_Z = r'$z = \dfrac{x - \bar{x}}{s}$<div class="kn">+ above the mean · 0 at the mean · − below the mean</div>'
KI_X = r'$x = \bar{x} + z \times s$<div class="kn">start at the mean, step $z$ standard deviations</div>'
KI_ZP = r'Convert to $z$-scores, then add the sections<div class="kn">34 · 13.5 · 2.35 · 0.15 (% on each side of the mean)</div>'

def ncurve(id_, m=None, s=None, xl='', dec=0, z=True, x=True, small=False):
    """Normal curve (teacher illustration). x row = mean ± k·s (shown by the nx step), z row (nz), section % (np)."""
    cfg = dict(m=m, s=s, xl=xl, dec=dec, z=z, x=(x and m is not None))
    return f"<svg class=\"zn{' zns' if small else ''}\" id=\"{id_}\" data-cfg='{json.dumps(cfg)}' viewBox=\"0 0 700 300\"></svg>"
def sh(id_, a, b, lab='', col='b'): return f'ns:{id_}:{a}:{b}:{col}:{lab.replace(" ", "_")}'
def mk(id_, zv, lab, col='r'): return f'nm:{id_}:{zv}:{col}:{lab.replace(" ", "_")}'

S.append(f'<section class="slide title cover"><div class="code">S5</div><h1>The normal distribution and standardised scores</h1>'
         f'<div class="unit">12MAG · Unit 3 · AOS 1 Data analysis · Lesson 5</div>'
         f'<div class="pp">{CG} · 1H The normal distribution and the 68–95–99.7% rule (pp. 76–84) · 1I Populations and samples (Interactive Textbook)</div><span class="pg" style="display:none"></span></section>')
LI = ['To be able to introduce the normal model for bell-shaped distributions.',
      'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.',
      'To be able to calculate standardised scores and use them to compare values across distributions.']
SC = ['I can apply the 68-95-99.7% rule.', 'I can calculate standardised scores.', 'I can use standardised scores to make comparisons.',
      'I can use standard scores to determine percentages.', 'I can convert standardised scores into actual scores.',
      'I can solve for the values of the mean and standard deviation.', 'I can explain the difference between a population and a sample.']
SEQ = ['CFAT 1.1.2 (20 minutes, 1F–1G)', 'Activating prior knowledge', 'Key ideas and formulas', 'The 68–95–99.7% rule · Example 28',
       'Standardised scores · Example 29 · CAS', 'Comparing with z-scores · Example 30', 'z-scores to percentages · Example 31',
       'Actual scores · Example 32', 'Finding $s$ and $\\bar{x}$ · Examples 33–34', 'Populations and samples (1I)', 'Exit tasks', 'Check-in and coursework']
S.append(f'<section class="slide z li">{bar("1H–1I", "Learning intentions")}<div class="cols" style="grid-template-columns:1.05fr 1.05fr .9fr">'
         f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
         f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
         f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
         f'{foot(CG + ", 1H Learning intentions (p. 76); 1I has none in the printed book. Success criteria: planner card")}</section>')
S.append(f'<section class="slide z cfat">{bar("CFAT 1.1.2", "Median, IQR, boxplots, SOCS")}'
         '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
         '<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · 14 marks</li>'
         '<li>Covers 1F–1G</li><li>Pens down when the timer ends</li></ul></div>'
         '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
         '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
         f'{foot("CFAT 1.1.2 (1F–1G): student copy and solutions on the planner")}</section>')

# APK 1: Cambridge U1&2 2G #13
S.append(qslide('apk', '1 of 2', 'Year 11 skills: the 68–95–99.7% rule', 'Cambridge U1&amp;2 · 2G #13',
    'Suppose the distribution of weights for a type of cat is approximately symmetric and bell shaped with a mean of 3.5 kg and a standard deviation of 0.5 kg.'
    '<br><b>a.</b> Approximately what percentage of cats weigh between 2 kg and 5 kg?', KI_RULE,
    [('Scale the curve: 3.5 ± 0.5, 1.0, 1.5 kg → 2.0 … 5.0 kg', 'nx:a1'),
     ('$2 = 3.5 - 3 \\times 0.5$ and $5 = 3.5 + 3 \\times 0.5$: within <b>three</b> standard deviations', 'nx:a1 ' + sh('a1', -3, 3, '99.7%'))],
    'approximately <b>99.7%</b> of cats', 'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2G #13. Working by teacher.',
    fig=ncurve('a1', 3.5, 0.5, 'weight (kg)', 1, z=False), figw='1.15fr', ans_do='nx:a1 ' + sh('a1', -3, 3, '99.7%')))
# APK 2: Edrolo U1&2 1G Q14 = VCAA 2020 E2 Q2bi (adapted by Edrolo)
A2 = 'nx:a2 ' + sh('a2', -3.6, -3, '', 'o') + ' ' + sh('a2', 3, 3.6, '0.3%', 'o')
S.append(qslide('apk', '2 of 2', 'A real VCAA question you can already do', 'VCAA 2020 Exam 2 Q2bi (adapted)',
    'A sample of 250 bonobos has been drawn at random from a population of bonobos whose <i>neck size</i> is normally distributed with a mean of 38 cm and a standard deviation of 2.3 cm.<br>'
    'How many of these 250 bonobos are expected to have a <i>neck size</i> that is more than three standard deviations above or below the mean? Round to the nearest whole number.',
    KI_RULE, [('Within three standard deviations: 99.7%', 'nx:a2 ' + sh('a2', -3, 3, '99.7%')),
              ('More than three away: $100\\% - 99.7\\% = 0.3\\%$', A2),
              ('$0.3\\% \\times 250 = 0.003 \\times 250 = 0.75$', A2)],
    '$0.75 \\to$ <b>1 bonobo</b>',
    'Edrolo General Mathematics Units 1&amp;2, 1G Q14 (adapted by Edrolo from VCAA 2020 Exam 2 Data analysis Q2bi); % from the examiner report. Working by teacher.',
    marks=1, vcaa=40, figw='1.15fr', fig=ncurve('a2', 38, 2.3, 'neck size (cm)', 1, z=False, small=True), ans_do=A2, watch='0.75 is not a number of bonobos. Round to the nearest whole number, as the question asks. <span class="zsc">(teacher note)</span>'))

# Key ideas
KD = [('Normal distribution', 'a symmetric, bell-shaped model: mean = median, in the centre'),
      ('68–95–99.7% rule', 'about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean'),
      ('Standardised score ($z$-score)', 'how many standard deviations a value is above (+) or below (−) the mean'),
      ('Population', 'every member of the group being studied'), ('Sample', 'a subset of the population')]
KF = [('Within 1 SD', r'$\bar{x} - s$ to $\bar{x} + s$: ≈ 68%'), ('Within 2 SDs', r'$\bar{x} - 2s$ to $\bar{x} + 2s$: ≈ 95%'),
      ('Within 3 SDs', r'$\bar{x} - 3s$ to $\bar{x} + 3s$: ≈ 99.7%'), ('Standardised score', r'$z = \dfrac{x - \bar{x}}{s}$'),
      ('Actual score', r'$x = \bar{x} + z \times s$'), ('Tails (each side)', 'beyond 1 SD: 16% · 2 SD: 2.5% · 3 SD: 0.15%')]
S.append(f'<section class="slide z kif">{bar("1H–1I", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1H Key ideas (pp. 76–84); 1I definitions in own words")}</section>')

# NL: the rule
S.append(nl_slide('The normal distribution and the 68–95–99.7% rule',
    'A <b>normal</b> distribution is bell shaped and symmetric: the mean is in the middle and the standard deviation sets the width. <span class="hint">Click to build the rule.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l1', None, None, '', 0) + '</div><div class="col">'
    + st('Within <b>1</b> SD of the mean: about <b>68%</b>', do=sh('l1', -1, 1, '68%'), cls='stp')
    + st('Within <b>2</b> SDs: about <b>95%</b>', do=sh('l1', -2, 2, '95%'), cls='stp')
    + st('Within <b>3</b> SDs: about <b>99.7%</b>', do=sh('l1', -3, 3, '99.7%'), cls='stp')
    + st('Halve the leftovers for each tail: <b>16%</b>, <b>2.5%</b>, <b>0.15%</b>', do='ncl:l1 np:l1', cls='stp')
    + st('Every section: 34, 13.5, 2.35, 0.15 on each side. They add to 100%.', True, do='ncl:l1 np:l1', cls='stp') + '</div></div>',
    CG + ', 1H pp. 76–78. Curve: teacher illustration.'))

# Example 28 / You try (Edrolo 1H WE1)
S.append(qslide('ex', 28, 'Applying the 68–95–99.7% rule', 'Cambridge · Example 28',
    'The distribution of delivery times for pizzas made by House of Pizza is approximately normal, with a mean of 25 minutes and a standard deviation of 5 minutes.', KI_RULE, [], None,
    CG + ', 1H Example 28 (p. 78). Part c is as typed in the old deck (“Approximately many”): check against the book.',
    parts=[('a', 'What percentage of pizzas have delivery times of between 15 and 35 minutes?',
            [('$15 = 25 - 2 \\times 5$, $35 = 25 + 2 \\times 5$: within 2 SDs', 'nx:w28 ' + sh('w28', -2, 2, '95%'))], '<b>95%</b>', 'nx:w28 ' + sh('w28', -2, 2, '95%')),
           ('b', 'What percentage of pizzas have delivery times of greater than 30 minutes?',
            [('$30 = 25 + 1 \\times 5$: more than 1 SD above', 'nx:w28 ncl:w28 ' + sh('w28', 1, 3.6, '16%'))], '<b>16%</b>', 'nx:w28 ncl:w28 ' + sh('w28', 1, 3.6, '16%')),
           ('c', 'In 1 month, House of Pizza delivers 2000 pizzas. Approximately many of these pizzas are delivered in less than 10 minutes?',
            [('$10 = 25 - 3 \\times 5$: 0.15% below. $0.0015 \\times 2000$', 'nx:w28 ncl:w28 ' + sh('w28', -3.6, -3, '0.15%', 'o'))],
            '<b>3 pizzas</b>', 'nx:w28 ncl:w28 ' + sh('w28', -3.6, -3, '0.15%', 'o'))],
    fig=ncurve('w28', 25, 5, 'delivery time (minutes)'), figw='.72fr', cls='tight tt'))
HAIR = ('An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. '
        'The <i>length of hair donated</i> was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.')
S.append(qslide('yt', '28 (a, b)', 'Applying the 68–95–99.7% rule', 'Edrolo 1H WE1', HAIR, KI_RULE, [], None,
    ED + ', 1H Worked example 1 (parts a–b; c–d on the next slide). Working by teacher.',
    parts=[('a.', 'What percentage of hair lengths donated were between 16 cm and 32 cm?',
            [('16 cm is 1 SD below, 32 cm is 3 SDs above', 'nx:y1 np:y1 ' + sh('y1', -1, 3, '')), ('$34 + 34 + 13.5 + 2.35$', 'nx:y1 np:y1 ' + sh('y1', -1, 3, ''))], '<b>83.85%</b>', 'nx:y1 np:y1 ' + sh('y1', -1, 3, '')),
           ('b.', 'Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?',
            [('24 cm is 1 SD above: $13.5 + 2.35 + 0.15$', 'nx:y1 np:y1 ncl:y1 ' + sh('y1', 1, 3.6, ''))], '<b>16%</b>', 'nx:y1 np:y1 ncl:y1 ' + sh('y1', 1, 3.6, ''))],
    fig=ncurve('y1', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))
S.append(qslide('yt', '28 (c, d)', 'Applying the 68–95–99.7% rule', 'Edrolo 1H WE1', HAIR, KI_RULE, [], None,
    ED + ', 1H Worked example 1 (parts c–d). Working by teacher.',
    parts=[('c.', 'If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?',
            [('Longer than 24 cm: 16% (part b)', 'nx:y1b np:y1b ' + sh('y1b', 1, 3.6, '')), '$0.16 \\times 30 = 4.8$'], '<b>5 girls</b>', 'nx:y1b np:y1b ' + sh('y1b', 1, 3.6, '')),
           ('d.', 'How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?',
            [('Below 16 cm: 16% · above 28 cm: 2.5%', 'nx:y1b np:y1b ncl:y1b ' + sh('y1b', -3.6, -1, '', 'o') + ' ' + sh('y1b', 2, 3.6, '', 'o')),
             '$16\\% + 2.5\\% = 18.5\\%$; $0.185 \\times 30 = 5.55$'], '<b>6 girls</b>',
            'nx:y1b np:y1b ncl:y1b ' + sh('y1b', -3.6, -1, '', 'o') + ' ' + sh('y1b', 2, 3.6, '', 'o'))],
    fig=ncurve('y1b', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))

# NL: z-scores
S.append(nl_slide('Standardised scores ($z$-scores)',
    r'A $z$-score counts how many standard deviations a value is from the mean: $z = \dfrac{x - \bar{x}}{s}$. <span class="hint">IQ scores: mean 100, standard deviation 15. Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l2', 100, 15, 'IQ score', 0) + '</div><div class="col">'
    + st('Each standard deviation is one step on the $z$ row.', do='nx:l2 nz:l2', cls='stp')
    + st(r'IQ 115: $z = \dfrac{115 - 100}{15} = 1$', do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1'), cls='stp')
    + st(r'IQ 70: $z = \dfrac{70 - 100}{15} = -2$', do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1') + ' ' + mk('l2', -2, 'z = −2', 'b'), cls='stp')
    + st('Check the sign: below the mean gives a <b>negative</b> $z$.', True, do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1') + ' ' + mk('l2', -2, 'z = −2', 'b'), cls='stp') + '</div></div>',
    CG + ', 1H p. 80 (IQ illustration). Curve: teacher illustration.'))

# Example 29
S.append(qslide('ex', 29, 'Calculating standard scores', 'Cambridge · Example 29',
    r'The heights of a group of young women have a mean of $\bar{x} = 160$ cm and a standard deviation of $s = 8$ cm. Determine the standard or z-scores of a woman who is:', KI_Z, [], None,
    CG + ', 1H Example 29 (p. 80)',
    parts=[('a', '172 cm tall', [(r'$z = \dfrac{172 - 160}{8}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172'))], '$\\boldsymbol{z = 1.5}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172')),
           ('b', '150 cm tall', [(r'$z = \dfrac{150 - 160}{8}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b'))], '$\\boldsymbol{z = -1.25}$',
            'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b')),
           ('c', '160 cm tall.', [(r'$z = \dfrac{160 - 160}{8}$', None)], '$\\boldsymbol{z = 0}$ (at the mean)',
            'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b') + ' ' + mk('w29', 0, '160', 'g'))],
    fig=ncurve('w29', 160, 8, 'height (cm)'), figw='.75fr', cls='tight tt'))

# CAS (steps from planner/cas-skills.json, skill z-score)
CSK = [x for x in json.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if x['id'] == 'z-score'][0]
amp = lambda t: t.replace('& ', '&amp; ')
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{amp(x)}</li>" for x in CSK["ti"])}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{amp(x)}</li>" for x in CSK["classpad"])}</ol></div>'
        f'<div class="zrule" style="margin-top:0">{CSK["tip"]}</div></div>')
S.append(qslide('cas', '', 'Standardised scores on CAS', 'Cambridge · Example 29a',
    'The heights of a group of young women have a mean of $\\bar{x} = 160$ cm and a standard deviation of $s = 8$ cm. Determine the standard or z-scores of a woman who is:<br><b>a.</b> 172 cm tall',
    KI_Z, ['Type the whole rule with brackets: $(172 - 160) \\div 8$', 'Without brackets: $172 - 160 \\div 8 = 152$. Wrong!'],
    '$\\boldsymbol{z = 1.5}$', CG + ', 1H Example 29a (p. 80). CAS steps: planner CAS guide (z-score).',
    fig=TABS, figw='1.1fr'))

S.append(qslide('yt', 29, 'Calculating standardised (z) scores', 'Edrolo 1I WE1',
    'The weights of puppies within a litter are approximately normally distributed with a mean of 4 kg and a standard deviation of 0.3 kg. Determine the z-score of a puppy that weighs 4.6 kg.',
    KI_Z, [(r'$z = \dfrac{4.6 - 4}{0.3} = \dfrac{0.6}{0.3}$', 'nx:y29 nz:y29 ' + mk('y29', 2, '4.6 kg'))], '$\\boldsymbol{z = 2}$',
    ED + ', 1I Worked example 1. Working by teacher.', fig=ncurve('y29', 4, 0.3, 'weight (kg)', 1), figw='1.1fr', ans_do='nx:y29 nz:y29 ' + mk('y29', 2, '4.6 kg')))

# Interactive: which test went better? (Example 30 means and SDs)
S.append(f'<section class="slide z nl ztwo">{bar("New learning", "Which test went better? Use z-scores")}'
    '<div class="ctx">A student sits two tests. <b>Psychology</b>: mean 65, standard deviation 10. <b>Statistics</b>: mean 60, standard deviation 5. '
    'Drag each mark. The raw marks can mislead: the <b>higher $z$-score</b> is the better result <b>relative to the class</b>.</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>Both marks on the $z$ scale</h2>'
    '<svg class="zts ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span style="width:150px;color:#d00000"><b>Psychology</b></span><input data-k="p" type="range" min="35" max="95" step="1" value="75"><b class="zv" data-k="p">75</b></div>'
    '<div class="ix zsl"><span style="width:150px;color:#1f5fbf"><b>Statistics</b></span><input data-k="s" type="range" min="45" max="75" step="1" value="70"><b class="zv" data-k="s">70</b></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-p="75" data-s="70">Student 1 (75, 70)</button><button data-p="55" data-s="55">Student 2 (55, 55)</button><button data-p="85" data-s="65">85 and 65</button></div></div>'
    '<div class="col"><h2>Live</h2><div class="ztso"></div></div></div>'
    f'{foot("Means, standard deviations and the two students: " + CG + ", 1H Example 30 (p. 81). Interactive by teacher.")}</section>')

# Example 30
S.append(qslide('ex', 30, 'Using standardised scores to make comparisons', 'Cambridge · Example 30',
    'Another student studying the same two subjects obtained a mark of 55 for both Psychology and Statistics. Does this mean that she performed equally well in both subjects? Use standardised marks to help you arrive at your conclusion.',
    KI_Z, [(r'Psychology: $z = \dfrac{55 - 65}{10} = -1$', 'tc:ps:101,102'), (r'Statistics: $z = \dfrac{55 - 60}{5} = -1$', 'tc:ps:101,102,201,202'),
           ('Below $z = -1$: the bottom 16% in each', 'tc:ps:101,102,201,202 ' + sh('w30', -3.6, -1, '16%') + ' ' + mk('w30', -1, 'z = −1'))],
    'Yes, her standardised score, $z = -1$, was the same for both subjects. In both subjects she finished in the bottom 16%.',
    CG + ', 1H Example 30 (p. 81); table of marks, means and standard deviations from the book.',
    fig=table_hl('ps', [('Subject', ['Mark', 'Mean', 'SD']), ('Psychology', ['75', '65', '10']), ('Statistics', ['70', '60', '5'])], 'ztab') + ncurve('w30', None, None, '', 0, small=True),
    figw='1fr', ans_do='tc:ps:101,102,201,202 ' + sh('w30', -3.6, -1, '16%') + ' ' + mk('w30', -1, 'z = −1')))
# You try (Edrolo 1I WE3)
Y30a = sh('y30', 2, 3.6, '2.5%') + ' ' + mk('y30', 2, 'Chem') + ' ' + sh('y30', -3.6, -3, '0.15%', 'o') + ' ' + mk('y30', -3, 'Phys', 'b')
S.append(qslide('yt', 30, 'Using standardised (z) scores to interpret data', 'Edrolo 1I WE3',
    'The results for a Chemistry exam were approximately normally distributed, with a mean of 71 and a standard deviation of 3. The results for a Physics exam were also approximately normally distributed, with a mean of 95 and a standard deviation of 6.',
    KI_Z, [], None, ED + ', 1I Worked example 3. Answer wording from the worked solution.',
    parts=[('a.', 'A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.',
            [(r'Chemistry $z = \dfrac{77 - 71}{3} = 2$ · Physics $z = \dfrac{77 - 95}{6} = -3$', Y30a)],
            'No. Chemistry $z = 2$: top 2.5% of students. Physics $z = -3$: bottom 0.15%. She did not do equally well in both exams when compared to her peers.', Y30a),
           ('b.', 'Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.',
            [(r'$z = \dfrac{66 - 71}{3} = -1.67$', 'ncl:y30 ' + sh('y30', -3.6, -1, '16%') + ' ' + mk('y30', -1.67, '66'))],
            '$z = -1.67$ places him in the bottom 16% of students.', 'ncl:y30 ' + sh('y30', -3.6, -1, '16%') + ' ' + mk('y30', -1.67, '66'))],
    fig=ncurve('y30', None, None, '', 0), figw='.62fr', cls='tight tt'))

# NL: z to percentages
S.append(nl_slide('Using standardised scores to find percentages',
    'On the $z$ scale every normal distribution looks the same. Convert values to $z$-scores, then <b>add the sections</b>. <span class="hint">Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l3', None, None, '', 0) + '</div><div class="col">'
    + st('The sections: 34, 13.5, 2.35, 0.15 on each side', do='np:l3', cls='stp')
    + st('Below $z = -1$: $13.5 + 2.35 + 0.15 = 16\\%$', do='np:l3 ' + sh('l3', -3.6, -1, '16%', 'o') + ' ' + mk('l3', -1, 'z = −1'), cls='stp')
    + st('So above $z = -1$: $100\\% - 16\\% = 84\\%$', do='np:l3 ncl:l3 ' + sh('l3', -1, 3.6, '84%') + ' ' + mk('l3', -1, 'z = −1'), cls='stp')
    + st('Read the question twice: <b>above</b> or <b>below</b>?', True, do='np:l3 ncl:l3 ' + sh('l3', -1, 3.6, '84%') + ' ' + mk('l3', -1, 'z = −1'), cls='stp') + '</div></div>',
    CG + ', 1H p. 82. Curve: teacher illustration.'))
# Example 31
S.append(qslide('ex', 31, 'Using standard scores to determine percentages', 'Cambridge · Example 31',
    'Suppose the weight of a certain species of bird is normally distributed with a mean of 42 grams with a standard deviation of 3 grams.', KI_ZP, [], None,
    CG + ', 1H Example 31 (p. 82)',
    parts=[('a', 'If a bird selected at random from this population has a standardised weight of $z = -1$, what percentage of birds in this population weigh more than this bird?',
            [('Below $z = -1$: 16%', 'nx:w31 nz:w31 np:w31 ' + mk('w31', -1, 'z = −1')), ('Above: $100\\% - 16\\%$', 'nx:w31 nz:w31 np:w31 ' + sh('w31', -1, 3.6, '84%') + ' ' + mk('w31', -1, 'z = −1'))],
            '<b>84%</b>', 'nx:w31 nz:w31 np:w31 ' + sh('w31', -1, 3.6, '84%') + ' ' + mk('w31', -1, 'z = −1')),
           ('b', 'Approximately what percentage of birds would weigh between 39 and 48 grams?',
            [(r'$z_1 = \dfrac{39 - 42}{3} = -1$, $z_2 = \dfrac{48 - 42}{3} = 2$', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b')),
             ('$34 + 34 + 13.5$', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + sh('w31', -1, 2, '') + ' ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b'))],
            '<b>81.5%</b>', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + sh('w31', -1, 2, '') + ' ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b'))],
    fig=ncurve('w31', 42, 3, 'weight (grams)'), figw='1.05fr', cls='tight'))
# You try (Edrolo 1H WE2)
S.append(qslide('yt', 31, 'Calculating values in normal distributions', 'Edrolo 1H WE2', HAIR, KI_ZP, [], None,
    ED + ', 1H Worked example 2. Working by teacher.',
    parts=[('a.', '97.35% of the hair lengths will fall within 12 cm and which other value?',
            [('12 cm is 2 SDs below. $13.5 + 34 + 34 + 13.5 + 2.35 = 97.35$: up to 3 SDs above', 'nx:y31 np:y31 ' + sh('y31', -2, 3, ''))], '<b>32 cm</b>', 'nx:y31 np:y31 ' + sh('y31', -2, 3, '')),
           ('b.', '2.5% of hair donated by the team will be disposed of, as it falls below a required minimum length. What is this required minimum length?',
            [('$0.15 + 2.35 = 2.5$: everything below 2 SDs under the mean', 'nx:y31 np:y31 ncl:y31 ' + sh('y31', -3.6, -2, '', 'o'))], '<b>12 cm</b>', 'nx:y31 np:y31 ncl:y31 ' + sh('y31', -3.6, -2, '', 'o'))],
    fig=ncurve('y31', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))

# NL: actual scores
S.append(nl_slide('Converting standardised scores into actual scores',
    r'Make $x$ the subject: $x = \bar{x} + z \times s$. Start at the mean, step $z$ standard deviations. <span class="hint">Test marks: mean 50, standard deviation 10. Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l4', 50, 10, 'test mark', 0) + '</div><div class="col">'
    + st(r'$z = 1.5$: $x = 50 + 1.5 \times 10 = 65$', do='nx:l4 nz:l4 ' + mk('l4', 1.5, '65'), cls='stp')
    + st(r'$z = -2$: $x = 50 + (-2) \times 10 = 30$', do='nx:l4 nz:l4 ' + mk('l4', 1.5, '65') + ' ' + mk('l4', -2, '30', 'b'), cls='stp')
    + st('A tail % gives $z$: 16% above → $z = 1$ · 2.5% above → $z = 2$ · 0.15% above → $z = 3$ (negative below the mean)', do='nx:l4 nz:l4 ncl:l4 np:l4', cls='stp')
    + st('With $z$ and one value you can solve for $s$ or $\\bar{x}$.', True, do='nx:l4 nz:l4 ncl:l4 np:l4', cls='stp') + '</div></div>',
    CG + ', 1H pp. 83–84. Marks made up by the teacher; curve: teacher illustration.'))
S.append(qslide('ex', 32, 'Converting standard scores into actual scores', 'Cambridge · Example 32',
    r'A class test (out of 50) has a mean mark of $\bar{x} = 34$ and a standard deviation of $s = 4$. Joe’s standardised test mark was $z = -1.5$. What was Joe’s actual mark?',
    KI_X, [r'$x = \bar{x} + z \times s$', (r'$x = 34 + (-1.5) \times 4 = 34 - 6$', 'nx:w32 nz:w32 ' + mk('w32', -1.5, '28'))],
    '<b>28</b>', CG + ', 1H Example 32 (p. 83). ',
    fig=ncurve('w32', 34, 4, 'test mark'), figw='1.1fr', ans_do='nx:w32 nz:w32 ' + mk('w32', -1.5, '28')))
S.append(qslide('yt', 32, 'Calculating actual scores from standardised (z) scores', 'Edrolo 1I WE2',
    'The number of black stripes on tigers at the Royal Melbourne Zoo is known to be normally distributed with a mean of 55 and a standard deviation of 2. One of the tigers has a standardised number of stripes of $z = -2.5$. How many stripes does the tiger actually have?',
    KI_X, [r'$x = \bar{x} + z \times s$', (r'$x = 55 + (-2.5) \times 2 = 55 - 5$', 'nx:y32 nz:y32 ' + mk('y32', -2.5, '50'))],
    '<b>50 stripes</b>', ED + ', 1I Worked example 2. Working by teacher.',
    fig=ncurve('y32', 55, 2, 'number of stripes'), figw='1.1fr', ans_do='nx:y32 nz:y32 ' + mk('y32', -2.5, '50')))

# Example 33 (no You try: no matching Edrolo worked example)
W33 = 'np:w33 ' + sh('w33', 2, 3.6, '', 'o') + ' ' + mk('w33', 2, '11.4 m (2.5% above)')
S.append(qslide('ex', 33, 'Finding the standard deviation given the mean and one percentage', 'Cambridge · Example 33',
    'Suppose the heights of red flowering gum trees have a mean of 10.2 metres, and 2.5% of these trees grow to more than 11.4 metres tall. Assuming that the heights of these trees are approximately normally distributed, what is the standard deviation of the height of the red flowering gum trees?',
    KI_X, [('2.5% above, so 11.4 m is at $z = 2$', W33), (r'$x = \bar{x} + z \times s$: $11.4 = 10.2 + 2 \times s$', W33), (r'$2s = 1.2$, so $s = 0.6$', W33)],
    '<b>0.6 metres</b>', CG + ', 1H Example 33 (p. 84). No matching Edrolo worked example, so no You try.',
    fig=ncurve('w33', None, None, '', 0), figw='1fr', ans_do=W33))
# Example 34
W34a = 'np:w34 ' + sh('w34', -3.6, -2, '2.5%', 'o') + ' ' + mk('w34', -2, '20', 'b')
W34 = W34a + ' ' + sh('w34', 1, 3.6, '16%') + ' ' + mk('w34', 1, '80')
S.append(qslide('ex', 34, 'Finding the mean and standard deviation', 'Cambridge · Example 34',
    'The marks scored in an examination are known to be approximately normally distributed. If 16% of students score more than 80 marks, and 2.5% of students score less than 20 marks, estimate the mean and standard deviation of this distribution.',
    KI_X, [('2.5% below 20, so 20 is at $z = -2$: $\\bar{x} - 2s = 20$ (1)', W34a), ('16% above 80, so 80 is at $z = 1$: $\\bar{x} + s = 80$ (2)', W34),
           ('(2) − (1): $3s = 60$, so $s = 20$', W34), (r'Substitute: $\bar{x} - 2 \times 20 = 20$, so $\bar{x} = 60$', W34)],
    r'$\boldsymbol{\bar{x} = 60}$ marks, $\boldsymbol{s = 20}$ marks', CG + ', 1H Example 34 (p. 84). Working by teacher, following the book.',
    fig=ncurve('w34', None, None, '', 0), figw='1fr', ans_do=W34, cls='tight'))
# You try (Edrolo 1H WE3)
S.append(qslide('yt', 34, 'Determining the mean and standard deviation of a normal distribution', 'Edrolo 1H WE3',
    'Duncan’s light bulb factory produces light bulbs.<br>The <i>lifetime</i> of their light bulbs are approximately normally distributed. It is known that approximately 95% of the light bulbs have a <i>lifetime</i> ranging from 800 hours to 1600 hours.',
    KI_X, [], None, ED + ', 1H Worked example 3. Working by teacher.',
    parts=[('a.', 'Calculate the standard deviation for the <i>lifetime</i> of a light bulb.',
            [('95%: 800 h is at $z = -2$, 1600 h at $z = 2$, four SDs apart', sh('y34', -2, 2, '95%') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600')),
             ('$1600 - 800 = 800 = 4s$', None)], '$s = 800 \\div 4 =$ <b>200 hours</b>', sh('y34', -2, 2, '95%') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600')),
           ('b.', 'Calculate the mean <i>lifetime</i> of a light bulb.',
            [('The mean is in the middle: $800 + 2 \\times 200$', sh('y34', -2, 2, '') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600') + ' ' + mk('y34', 0, '1200', 'g'))],
            '<b>1200 hours</b>', sh('y34', -2, 2, '') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600') + ' ' + mk('y34', 0, '1200', 'g'))],
    fig=ncurve('y34', None, None, '', 0), figw='.75fr', cls='tight'))

# NL: 1I populations and samples
SMP = (3, 8, 17, 22, 29, 36, 41, 48, 52, 57)
dots = ''.join(f'<circle cx="{40 + (k % 15) * 56}" cy="{36 + (k // 15) * 50}" r="15" fill="#c9d6f2"/>' for k in range(60))
sdots = ''.join(f'<circle cx="{40 + (k % 15) * 56}" cy="{36 + (k // 15) * 50}" r="17" fill="#d98a1f" stroke="#000" stroke-width="2"/>' for k in SMP)
S.append(nl_slide('1I Populations and samples',
    'The <b>population</b> is every member of the group we want to know about. Measuring them all is usually too slow or costly, so we measure a <b>sample</b>: a subset of the population. <span class="hint">Click.</span>',
    '<div class="cols" style="grid-template-columns:1.4fr .9fr"><div class="col zc"><svg class="zpop" viewBox="0 0 880 230" style="width:100%">'
    f'<rect x="4" y="4" width="872" height="200" rx="18" fill="none" stroke="#1f5fbf" stroke-width="3"/>{dots}<g class="zsmp" style="opacity:0;transition:opacity .4s">{sdots}</g>'
    '<text x="440" y="226" text-anchor="middle" font-size="18" font-weight="bold" fill="#1f5fbf">population: all 60 members</text></svg></div><div class="col">'
    + st('Pick a sample <b>at random</b>: every member has the same chance of being chosen.', do='smp:on', cls='stp')
    + st('The sample mean $\\bar{x}$ and standard deviation $s$ are used to <b>estimate</b> the population values.', do='smp:on', cls='stp')
    + st('A different random sample gives slightly different statistics.', do='smp:on', cls='stp')
    + st('Population = everyone · sample = the ones we measure.', True, do='smp:on', cls='stp') + '</div></div>',
    CG + ', 1I Populations and samples (Interactive Textbook only), summarised in own words. Picture: teacher illustration.'))

# Exit tasks (short-answer exam questions)
E1 = 'nx:e1 ' + mk('e1', 0, '9.4') + ' ' + sh('e1', 0, 3.6, '50%')
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2019 Exam 2 Q2b',
    'The <i>temperature difference</i> between the <i>minimum daily temperature</i> and the <i>maximum daily temperature</i> in November 2017 at a location is approximately normally distributed with a mean of 9.4 °C and a standard deviation of 3.2 °C.'
    '<br>Determine the number of days in November 2017 for which this <i>temperature difference</i> is expected to be greater than 9.4 °C.',
    KI_RULE, [('9.4 °C is the mean: half of the days are above it', E1), ('November has 30 days: $50\\% \\times 30$', E1)],
    '<b>15 days</b>', ED + ', 1H Q12 (VCAA 2019 Exam 2 Data analysis Q2b); % and comment from the examiner report. Working by teacher.',
    marks=1, vcaa=58, figw='1.15fr', fig=ncurve('e1', 9.4, 3.2, 'temperature difference (°C)', 1, z=False, small=True), ans_do=E1, watch='Some gave the percentage of 50% rather than the number of days. <span class="zsc">(examiner report)</span>'))
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2021 Exam 2 Q1c',
    'In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>'
    'In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>'
    'For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.'
    + table_hl('sp', [('statistic', ['<i>shot-put</i> (metres)']), ('mean', ['13.74']), ('standard deviation', ['1.43'])], 'ztab zsm')
    + 'Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place.',
    KI_Z, [('$x = 14.50$, $\\bar{x} = 13.74$, $s = 1.43$', 'tc:sp:100,200'), (r'$z = \dfrac{14.50 - 13.74}{1.43} = 0.531\ldots$', 'tc:sp:100,200')],
    '$\\boldsymbol{z = 0.5}$', ED + ', 1I Q13 (VCAA 2021 Exam 2 Data analysis Q1c); % from the examiner report. Working by teacher.',
    marks=1, vcaa=78, figw='1.25fr', ans_do='tc:sp:100,200', watch='Round only at the end, to one decimal place: 0.531… → 0.5. <span class="zsc">(teacher note)</span>'))

S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
         f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot("Success criteria: planner card")}</section>')
CWR = open(os.path.join(SH, 'cwr.html')).read(); CWL = open(os.path.join(SH, 'cwl.html')).read()
S.append(f'<section class="slide cwk">{bar("1H–1I", "Coursework · Exercises 1H, 1I")}<div class="cwgrid"><div class="cwl2">'
         '<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>'
         '<tr><th>Cambridge Exercise 1H</th><td>Q1–23</td></tr>'
         '<tr><th>Cambridge Exercise 1I</th><td>Interactive Textbook (Cambridge GO)</td></tr>'
         '<tr><th>Practice booklet</th><td>1H section</td></tr></tbody></table>'
         '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
         f'{CWL}</div>{CWR}</div>{foot(CG + ", Exercises 1H and 1I")}</section>')

# ---- S5 extras: normal-curve engine, two-tests interactive (CSS + JS ride along after the last slide)
S.append(r'''<style>
svg.zn{width:100%;max-height:330px}.slide.z .zfig svg.zn{max-height:330px}
.slide.z .top>.q svg.zn.zns,.slide.z .zq svg.zn.zns{display:block;max-height:190px;margin:6px auto}
.slide.z .zfig svg.zn.zns{max-height:220px}
.slide.nl .stp{white-space:normal;font-size:21px;line-height:1.35;color:#000;margin:0 0 14px!important}
.slide.nl .stp.final{color:#d00000}
.ztso{font-size:21px;line-height:1.55}.ztso .v{font-size:17px;border:2px solid #000;background:#fff7d6;padding:8px 10px;margin-top:10px;line-height:1.35}
.slide.tt .st.zs{font-size:18px!important;margin-bottom:4px!important}.slide.tt .zpq{font-size:17px;margin-bottom:4px}.slide.tt .top>.q{font-size:19px;line-height:1.3}.slide.tt .st.zs .katex{font-size:1.02em}
.zv{width:42px;text-align:right;font-size:22px}
</style>
<script>
(function(){
const N=x=>Math.exp(-x*x/2),PX=z=>40+(z+3.6)/7.2*620,BASE=215,H=160,PY=z=>BASE-H*N(z);
const PCT=[[-3.3,'0.15'],[-2.5,'2.35'],[-1.5,'13.5'],[-0.5,'34'],[0.5,'34'],[1.5,'13.5'],[2.5,'2.35'],[3.3,'0.15']];
function fmt(v,d){return (+v.toFixed(d)).toFixed(d)}
function draw(sv){const c=JSON.parse(sv.dataset.cfg);let s='';
  for(let k=-3;k<=3;k++)s+=`<line x1="${PX(k)}" y1="${PY(k)}" x2="${PX(k)}" y2="${BASE}" stroke="#999" stroke-width="1.2" stroke-dasharray="4 4"/>`;
  s+='<g class="sh"></g>';let d='';for(let z=-3.6;z<=3.601;z+=0.05)d+=(d?'L':'M')+PX(z).toFixed(1)+' '+PY(z).toFixed(1);
  s+=`<path d="${d}" fill="none" stroke="#000" stroke-width="3"/><line x1="20" y1="${BASE}" x2="680" y2="${BASE}" stroke="#000" stroke-width="2"/>`;
  let y=BASE+24;
  if(c.x){s+='<g class="rx" opacity="0">';for(let k=-3;k<=3;k++)s+=`<text x="${PX(k)}" y="${y}" font-size="17" text-anchor="middle">${fmt(c.m+k*c.s,c.dec)}</text>`;s+='</g>';y+=24}
  if(c.z){s+=`<g class="rz" opacity="${c.x?0:1}">`;for(let k=-3;k<=3;k++)s+=`<text x="${PX(k)}" y="${y}" font-size="16" fill="#1f5fbf" text-anchor="middle">${k}</text>`;s+=`<text x="16" y="${y}" font-size="16" font-weight="bold" fill="#1f5fbf">z</text></g>`;y+=22}
  if(c.xl)s+=`<text x="350" y="${y+2}" font-size="16" text-anchor="middle">${c.xl}</text>`;
  s+='<g class="rp" opacity="0">'+PCT.map(([z,t])=>{const tail=Math.abs(z)>3;return `<text x="${PX(z)}" y="${tail?BASE-12:Math.max(PY(z)+((Math.abs(z)>2)?-8:30),40)}" font-size="${tail?12:16}" font-weight="bold" text-anchor="middle">${t}%</text>`}).join('')+'</g><g class="nmk"></g>';
  sv.setAttribute('viewBox','0 0 700 '+(y+12));sv.innerHTML=s}
document.querySelectorAll('svg.zn').forEach(draw);
function region(a,b,col,lab){a=+a;b=+b;let d=`M${PX(a)} ${BASE}`;for(let z=a;z<=b+1e-9;z+=0.05)d+=`L${PX(z).toFixed(1)} ${PY(z).toFixed(1)}`;d+=`L${PX(b)} ${PY(b)}L${PX(b)} ${BASE}Z`;
  const f=col==='o'?'#e8892b':'#1f5fbf';let s=`<path d="${d}" fill="${f}" fill-opacity="${col==='o'?.55:.32}"/>`;
  if(lab){const zc=Math.max(-3.2,Math.min(3.2,(Math.max(a,-3.4)+Math.min(b,3.4))/2));const yy=Math.max(22,PY(zc)-40);
    s+=`<line x1="${PX(zc)}" y1="${yy+4}" x2="${PX(zc)}" y2="${PY(zc)+12}" stroke="${col==='o'?'#a04a00':'#d00000'}" stroke-width="1.5"/><text x="${PX(zc)}" y="${yy}" font-size="22" font-weight="bold" fill="${col==='o'?'#a04a00':'#d00000'}" text-anchor="middle" stroke="#fff" stroke-width="5" paint-order="stroke">${lab}</text>`}return s}
function mark(z,col,lab){z=+z;const f={r:'#d00000',b:'#1f5fbf',g:'#1a7f1a'}[col]||'#d00000';
  return `<line x1="${PX(z)}" y1="${PY(z)-26}" x2="${PX(z)}" y2="${BASE}" stroke="${f}" stroke-width="3.5"/><circle cx="${PX(z)}" cy="${BASE}" r="6" fill="${f}"/><text x="${PX(z)}" y="${PY(z)-32}" font-size="18" font-weight="bold" fill="${f}" text-anchor="middle" stroke="#fff" stroke-width="5" paint-order="stroke">${lab}</text>`}
function apply(sl){sl.querySelectorAll('svg.zn').forEach(sv=>{sv.querySelector('.sh').innerHTML='';sv.querySelector('.nmk').innerHTML='';['rx','rp'].forEach(c=>sv.querySelector('.'+c)?.setAttribute('opacity',0));
    const c=JSON.parse(sv.dataset.cfg);if(c.x&&c.z)sv.querySelector('.rz').setAttribute('opacity',0)});
  sl.querySelectorAll('.zsmp').forEach(g=>g.style.opacity=0);
  [...sl.querySelectorAll('.st[data-do].show')].forEach(st=>st.dataset.do.split(' ').forEach(a=>{const p=a.split(':'),op=p[0];
    if(op==='smp'){sl.querySelectorAll('.zsmp').forEach(g=>g.style.opacity=1);return}
    const sv=document.getElementById(p[1]);if(!sv||!sv.classList.contains('zn'))return;
    if(op==='nx')sv.querySelector('.rx')?.setAttribute('opacity',1);
    if(op==='nz')sv.querySelector('.rz')?.setAttribute('opacity',1);
    if(op==='np')sv.querySelector('.rp').setAttribute('opacity',1);
    if(op==='ncl'){sv.querySelector('.sh').innerHTML='';sv.querySelector('.nmk').innerHTML=''}
    if(op==='ns')sv.querySelector('.sh').insertAdjacentHTML('beforeend',region(p[2],p[3],p[4],(p[5]||'').replace(/_/g,' ')));
    if(op==='nm')sv.querySelector('.nmk').insertAdjacentHTML('beforeend',mark(p[2],p[3],(p[4]||'').replace(/_/g,' ')));
  }))}
new MutationObserver(ms=>{const seen=new Set();ms.forEach(m=>{const t=m.target;if(t.classList&&t.classList.contains('st')){const sl=t.closest('.slide');if(sl&&!seen.has(sl)&&sl.querySelector('svg.zn,.zsmp')){seen.add(sl);apply(sl)}}})}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class']});
// two tests: Psychology (mean 65, sd 10) vs Statistics (mean 60, sd 5)
const BELOW={'-3':0.15,'-2':2.5,'-1':16,'0':50,'1':84,'2':97.5,'3':99.85};
const below=z=>{if(Number.isInteger(z))return `${BELOW[z]}% of the class scored lower`;const lo=Math.floor(z),hi=Math.ceil(z);return `between ${BELOW[lo]}% and ${BELOW[hi]}% of the class scored lower`};
document.querySelectorAll('.slide.ztwo').forEach(sl=>{const sv=sl.querySelector('svg.zts'),O=sl.querySelector('.ztso'),I={};sl.querySelectorAll('input').forEach(i=>I[i.dataset.k]=i);
  const go=()=>{const p=+I.p.value,s=+I.s.value,zp=Math.round((p-65)/10*100)/100,zs=Math.round((s-60)/5*100)/100;
    sl.querySelectorAll('.zv').forEach(v=>v.textContent=I[v.dataset.k].value);
    let g='';for(let k=-3;k<=3;k++)g+=`<line x1="${PX(k)}" y1="${PY(k)}" x2="${PX(k)}" y2="${BASE}" stroke="#999" stroke-dasharray="4 4"/><text x="${PX(k)}" y="${BASE+22}" font-size="16" fill="#1f5fbf" text-anchor="middle">${k}</text>`;
    let d='';for(let z=-3.6;z<=3.601;z+=0.05)d+=(d?'L':'M')+PX(z).toFixed(1)+' '+PY(z).toFixed(1);
    g+=`<path d="${d}" fill="none" stroke="#000" stroke-width="3"/><line x1="20" y1="${BASE}" x2="680" y2="${BASE}" stroke="#000" stroke-width="2"/><text x="16" y="${BASE+22}" font-size="16" font-weight="bold" fill="#1f5fbf">z</text>`;
    const same=Math.abs(zp-zs)<1e-9;g+=mark(zp,'r','Psych'+(same?' = Stats':''));if(!same)g+=mark(zs,'b','Stats');sv.setAttribute('viewBox','0 0 700 250');sv.innerHTML=g;
    const f=z=>(z>0?'+':'')+(+z.toFixed(2));
    O.innerHTML=`<b style="color:#d00000">Psychology</b> ${p}: $z = \\dfrac{${p} - 65}{10} = ${f(zp)}$<br><span style="font-size:16px">${below(zp)}</span><br>`+
      `<b style="color:#1f5fbf">Statistics</b> ${s}: $z = \\dfrac{${s} - 60}{5} = ${f(zs)}$<br><span style="font-size:16px">${below(zs)}</span>`+
      `<div class="v">${same?'<b>Equal z-scores:</b> equally well in both, relative to each class.':(zp>zs?'<b>Psychology</b> was the better result relative to the class'+(p<s?' (even though the raw mark is lower).':'.'):'<b>Statistics</b> was the better result relative to the class'+(s<p?' (even though the raw mark is lower).':'.'))}</div>`;
    O.innerHTML=O.innerHTML.replace(/−/g,'-');if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};
  Object.values(I).forEach(i=>{i.oninput=go;i.onclick=e=>e.stopPropagation()});
  sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();I.p.value=b.dataset.p;I.s.value=b.dataset.s;go()});
  if(document.readyState==='complete')go();else window.addEventListener('load',go)});
})();
</script>''')


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
