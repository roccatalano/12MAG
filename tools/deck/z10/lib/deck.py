r"""12MAG slide library (10MA house style, 'z10'). THE slide standard: see tools/deck/z10/HOWTO.md.

A lesson script is content only:

    import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/deck/z10
    from lib.deck import *          # S (slide list), qslide, nl_slide, figures, title/overview/check-in/coursework slides
    from lib.num import *           # optional modules: num (numerical build-ups), cat (categorical charts),
                                    # boxplot, normal. Importing a module adds its CSS + JS to the deck.
    lesson('1F Measures of centre and spread')            # subchapter line in every title bar
    title_slide('Measures of centre and spread', ['1F Using summary statistics ... (pp. 44–54)'])
    ...  S.append(qslide(...)) ...
    build('S3-slides.html', '12MAG S3 · Measures of centre and spread · Slides', css=LESSON_CSS, js=LESSON_JS)

Files: core.css / core.js (shared shell additions: question template, tiles, stem plot standard, dot plots, histograms,
count badges, key-as-step, check-in, coursework) + <module>.css / <module>.js. The 10MA shell itself is ../shell/.
"""
import json, os, re

LIB = os.path.dirname(os.path.abspath(__file__))
Z10 = os.path.dirname(LIB)
SH = os.path.join(Z10, 'shell')
ROOT = os.path.abspath(os.path.join(Z10, '..', '..', '..'))
LESSONS = os.path.join(ROOT, 'lessons')

CG = 'Cambridge General Mathematics Units 3&amp;4'
ED = 'Edrolo General Mathematics Units 3&amp;4'
CG12 = 'Cambridge General Mathematics Units 1&amp;2'
ED12 = 'Edrolo General Mathematics Units 1&amp;2'

S = []                 # the slides, in order (lesson scripts append to it)
OPTDIST = {}           # multiple choice: OPTDIST[num or title] = [% choosing A, B, C, ...] (examiner report)
_L = {'sub': ''}
_MODS = []             # library modules in use (added when lib.<module> is imported)


def lesson(sub):
    """Set the subchapter line shown at the right of every title bar, e.g. '1F Measures of centre and spread'."""
    _L['sub'] = sub


def use(mod):
    """Add lib/<mod>.css and lib/<mod>.js to the deck (done for you by `from lib.<mod> import *`)."""
    if mod not in _MODS:
        _MODS.append(mod)


def _read(name):
    p = os.path.join(LIB, name)
    return open(p).read() if os.path.exists(p) else ''


# ---------------- small parts ----------------
def bar(tag, h1, yt=False):
    return f'<div class="bar{" ytb" if yt else ""}"><span class="tag">{tag}</span><h1>{h1}</h1><span class="sub">{_L["sub"]}</span></div>'
def foot(src): return f'<div class="foot"><span>{src}</span><span class="pg"></span></div>'
TILEOPS = ('sort', 'cross', 'mid', 'clr', 'band')
def st(t, final=False, do=None, cls=''):
    """One click-step. do = space-separated step actions (see HOWTO.md); tile actions go to the 10MA tile engine."""
    a = ''
    if do:
        ta = [x for x in do.split() if x.split(':')[0] in TILEOPS]; za = [x for x in do.split() if x.split(':')[0] not in TILEOPS]
        if ta: a += f' data-act="{" ".join(ta)}"'
        a += f' data-do="{" ".join(za)}"'
    return f'<div class="st zs{" final" if final else ""} {cls}"{a}>{t}</div>'
def stat(): return '<div class="zstat">VCAA: <b>?%</b> of students answered correctly</div>'
def sumtiles(id_, vals, unit='', label='running total'):
    t = ''.join(f'<span class="zt" data-k="{k}">{v}</span>' for k, v in enumerate(vals))
    return f'<div class="zsumw" id="{id_}"><div class="ztiles">{t}</div><div class="zrun"><span>{label}</span><b data-u="{unit}">0</b></div></div>'
def table_hl(id_, rows, cls='ztab'):
    """rows: list of (header, [cells]); cells get data-k numbered per row r*100+c"""
    h = ''
    for r, (hd, cells) in enumerate(rows):
        h += f'<tr><th>{hd}</th>' + ''.join(f'<td data-k="{r*100+c}">{v}</td>' for c, v in enumerate(cells)) + '</tr>'
    return f'<table class="{cls}" id="{id_}">{h}</table>'
def mc(opts, dist):
    return '<div class="zmc">' + ''.join(f'<div data-o="{L}"><span class="pb"></span><b>{L}.</b> {o}<span class="pc">{d}%</span></div>' for (L, o), d in zip(opts, dist)) + '</div>'
def ki(head, body): return f'<div class="ki"><div class="kh">{head}</div><div class="kb">{body}</div></div>'
def J2(xs): return ','.join(str(x) for x in xs)

# ---------------- figures ----------------
def dotplot(id_, vals, lo, hi, xl=''):
    return f'<svg class="zdp" id="{id_}" data-v="{json.dumps(sorted(vals))}" data-lo="{lo}" data-hi="{hi}" data-xl="{xl}" viewBox="0 0 640 262"></svg>'
def hist(id_, start, w, v, ymax, ystep, xl='', yl='Frequency'):
    cfg = dict(start=start, w=w, v=v, ymax=ymax, ystep=ystep, xl=xl, yl=yl)
    return f"<svg class=\"zhg\" id=\"{id_}\" data-cfg='{json.dumps(cfg)}' viewBox=\"0 0 600 330\"></svg>"
def stem(id_, rows, key, head=('Stem', 'Leaf'), build=False):
    """Stem plot (the stem plot standard: zstemfit sizes it as big as the figure box allows; fixed cells, highlights never resize).
    build=True hides the key until a step with sk:id (writing the key is its own step)."""
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
def tilerow(lab, t, d):
    return f'<div class="ztr"><span class="lab">{lab}</span>{tiles(t, d)}</div>' if lab else tiles(t, d)
def five(id_, vals):
    hd = ''.join(f'<th>{h}</th>' for h in ['min', '$Q_1$', '$M$', '$Q_3$', 'max'])
    return f'<table class="z5 zfill" id="{id_}"><tr>{hd}</tr><tr>' + ''.join(f'<td data-k="{k}">{v}</td>' for k, v in enumerate(vals)) + '</tr></table>'

# SOCS answer (describe a distribution): one line per letter, in this order
SOCS = lambda s, o, c, sp: (f'The distribution is {s}.<br>There {o}.<br>The distribution is centred at {c}, the median.<br>{sp}')

# CAS steps come from planner/cas-skills.json (fix a step there, never in a deck)
CASJ = {x['id']: x for x in json.load(open(os.path.join(ROOT, 'planner', 'cas-skills.json')))['skills']}
def casbox(cid, ti_note=None):
    """TI-Nspire and ClassPad steps side by side for skill `cid`."""
    c = CASJ[cid]
    cp = c['classpad'] or ['ClassPad cannot make dot plots: draw them by hand.']
    return ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in c["ti"])}</ol></div>'
            '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{x}</li>" for x in cp)}</ol></div></div>')

# ================= ONE TEMPLATE FOR EVERY QUESTION SLIDE =================
# bar [tag | title | source pill]; top: question (+ marks) | Key idea (+ VCAA % badge for exam questions);
# body: figure / data / MC options | working, one idea per click -> green ✓ Answer (-> % bars for MC, Watch out for short answer)
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
    m = re.search(r'<br><b>([a-z])\.</b> (.*)$', q)
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
    if vcaa is not None:   # exam layout: question + data (+ options) left; badge, key idea, working right
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

KI_MED = r'Median position $= \dfrac{n + 1}{2}$th value<div class="kn">n even: average the two middle values</div>'
KI_MEDH = r'Median position $= \dfrac{n + 1}{2}$th value<div class="kn">histogram: add the frequencies until you pass that position</div>'
KI_RANGE = r'$\text{range} = \text{largest} - \text{smallest}$'
KI_IQR = r'$\text{IQR} = Q_3 - Q_1$<div class="kn">$Q_1$ = median of the lower half, $Q_3$ = median of the upper half (n odd: leave the median out)</div>'
KI_MEAN = r'$\bar{x} = \dfrac{\Sigma x}{n}$<div class="kn">add the values, divide by how many</div>'
KI_CAS = r'One-Variable Statistics gives $\bar{x}$, $s_x$, $n$ and the five-number summary.<div class="kn">Use $s_x$, not $\sigma_x$. Check $n$.</div>'

# ================= STANDARD SLIDES =================
def title_slide(title, subs, unit='12MAG · Unit 3 · AOS 1 Data analysis', book=CG):
    """Title page: formal topic, unit line, the textbook on its own row, the subchapters as a vertical list
    (with page ranges). No big S#, no 'Lesson N'."""
    li = ''.join(f'<li>{x}</li>' for x in subs)
    S.append(f'<section class="slide title cover"><h1>{title}</h1>'
             f'<div class="unit">{unit}</div>'
             f'<div class="pp" style="font-size:22px;margin-top:14px">{book}</div>'
             f'<ul style="list-style:none;padding:0;margin:10px 0 0;font-size:22px;line-height:1.5;text-align:left">{li}</ul><span class="pg" style="display:none"></span></section>')

def overview(code, LI, SC, SEQ, src, cols='1.05fr 1.05fr .9fr', cls=''):
    """Learning intentions | success criteria (tick boxes) | lesson sequence. code = '1F', '1A–1B' (bar tag)."""
    S.append(f'<section class="slide z li{(" " + cls) if cls else ""}">{bar(code, "Learning intentions")}<div class="cols" style="grid-template-columns:{cols}">'
             f'<div class="col"><h2>Learning intentions</h2><ul class="zul">{"".join(f"<li>{x}</li>" for x in LI)}</ul></div>'
             f'<div class="col"><h2>Success criteria</h2><ul class="zul ck">{"".join(f"<li>☐ {x}</li>" for x in SC)}</ul></div>'
             f'<div class="col"><h2>Lesson sequence</h2><ol class="zseq">{"".join(f"<li>{x}</li>" for x in SEQ)}</ol></div></div>'
             f'{foot(src)}</section>')

def checkin(SC, src='Success criteria: one per worked example'):
    """One tick box per success criterion (click = green tick)."""
    S.append(f'<section class="slide z chk">{bar("Check-in", "How did you go?")}<p class="lead zlead">Read each one. If you can do it, tick it on your worksheet. <span class="hint">Click a box to tick it.</span></p>'
             f'<div class="zchk">{"".join(f"<div class=zci><span class=\"zcb ix\"></span>{x}</div>" for x in SC)}</div>{foot(src)}</section>')

def coursework(code, heading, rows, example, src, fit=True):
    """10MA coursework slide: short table (rows = [(Do, Questions), ...]), margin rules, and the example A4 page whose
    heading shows THIS lesson's own exercise (example = 'Exercise 1F: Using summary statistics').
    fit=True squeezes a long example heading to the page width."""
    attr = ' textLength="344" lengthAdjust="spacingAndGlyphs"' if fit else ''
    cwr = open(os.path.join(SH, 'cwr.html')).read().replace('>Exercise 9A: Collecting representative data<', f'{attr}>{example}<')
    cwl = open(os.path.join(SH, 'cwl.html')).read()
    tr = ''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in rows)
    S.append(f'<section class="slide cwk">{bar(code, heading)}<div class="cwgrid"><div class="cwl2">'
             f'<table class="cw"><thead><tr><th>Do</th><th>Questions</th></tr></thead><tbody>{tr}</tbody></table>'
             '<p class="note">Your teacher will tell you which questions to start with. Tick them off on your worksheet.</p>'
             f'{cwl}</div>{cwr}</div>{foot(src)}</section>')

# ================= BUILD =================
def _cfu_of(x):
    h = x[:120]
    if 'k-exam' in h: return 'mc'
    if 'k-exit' in h or 'k-yt' in h or 'k-apk' in h: return 'qw'
    if 'k-ex' in h or 'k-cas' in h: return 'cold'
    if ' nl' in h: return 'disc'
    if ' chk' in h: return 'tps'
    return ''

def build(out, page_title, css='', js='', css_first=False):
    """Write the deck. out = file name in lessons/ (e.g. 'S3-slides.html') or a path. css/js = lesson-only extras
    (plain CSS / JS text, no tags), added after the core and module files. css_first=True puts the module + lesson CSS
    BEFORE core.css, so core rules win ties (S4 was built that way; new decks leave it False)."""
    head = open(os.path.join(SH, 'head.html')).read().replace('10MAG Univariate Statistics · Slides', page_title)
    tail = open(os.path.join(SH, 'tail.html')).read()
    extra = ''.join(_read(m + '.css') for m in _MODS) + css
    C = (extra + _read('core.css')) if css_first else (_read('core.css') + extra)
    J = _read('core.js').replace('__CFU__', open(os.path.join(SH, 'cfu.json')).read()) + ''.join(_read(m + '.js') for m in _MODS) + js
    sl = [x.replace('<section class="slide', '<section data-cfu="%s" class="slide' % _cfu_of(x), 1) if _cfu_of(x) else x for x in S]
    html = head.replace('</head>', '<style>' + C + '</style></head>') + '\n'.join(sl) + tail.replace('</body>', '<script>' + J + '</script></body>')
    path = out if os.path.isabs(out) or os.sep in out else os.path.join(LESSONS, out)
    open(path, 'w').write(html)
    print(len(S), 'slides ->', os.path.relpath(path, ROOT), len(html))
    return path
