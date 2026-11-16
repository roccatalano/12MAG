"""Build the Ch11 revision booklet (Transition matrices and Leslie matrices: 11A-11E) + solutions.
Source: Insight GM1 Unit 4 (MCQ) 'Matrices - Transition matrices' Q1-14 (printed pp.13-18 = pdf 14-19; answers printed
pp.37-40) + 'Matrices and their applications' Q24, Q29 (transition questions held back from the Ch10 booklet; answers p.36),
and Insight GM2 Unit 4 (Short Answer) 'Matrices - Transition matrices' Q1-11 (printed pp.10-20 = pdf 11-21; worked solutions
printed pp.43-46). (C) Insight Publications 2022. Insight is never burnt.
Questions are crops of the scanned Insight pages (verbatim). Crops: seg.py (tesseract finds 'Question n' headers and
'Use the following information' stems; seg_g1.json / seg_g2.json) + mk.py. Shared stems are shown once, before their group,
and the group is kept in one section (so GM1 Q4 sits in 11D with Q5, and Q9-Q10 in 11D with Q11).
Answers: Insight's answers; the one-line 'why' is condensed from Insight's explanatory notes / worked solutions."""
import base64, os, sys, json
from PIL import Image, ImageOps
os.chdir(os.path.dirname(os.path.abspath(__file__)))
A4VIEW = '--print' not in sys.argv
G1 = 'Insight GM1 Unit 4 (Transition matrices)'
G1M = 'Insight GM1 Unit 4 (Matrices and their applications)'
G2 = 'Insight GM2 Unit 4 (Transition matrices)'
SUBS = [('11A', 'Introduction to transition matrices'), ('11B', 'Interpreting transition matrices and diagrams'),
        ('11C', 'Using transition matrices to model change: Sn+1 = TSn'), ('11D', 'Transition matrices with additions and removals: Sn+1 = TSn + B'),
        ('11E', 'Leslie matrices')]
S1 = json.load(open('seg_g1.json')); S2 = json.load(open('seg_g2.json'))
def pg(seg, n): return seg[str(n)][0][0] - 1   # pdf page -> printed page
# GM1 MC: (crop tag, n, sub, printed page, answer, why, stem)
MC = [
 ('g1t', 1, '11A', 'D', 'Each column of a transition matrix must add to 1 (no one leaves the system); only D does.', None),
 ('g1t', 6, '11A', 'D', 'Each column adds to 1, so A→A = 1 − 0.45 − 0.20 = 0.35, B→B = 1 − 0.30 − 0.50 = 0.20, C→C = 1 − 0.65 − 0.10 = 0.25.', None),
 ('g1t', 13, '11A', 'A', 'Fill the missing values from the diagram (columns add to 1): only A has every value in the right place.', None),
 ('g1t', 12, '11B', 'A', '0.35x = 320 gives x = 914 at PB in week 1; 0.35 × 914 + 0.72y = 1220 gives y = 1250; total 2164, so a = 2164 − 1220 = 944.', None),
 ('g1t', 2, '11C', 'C', 'S₃ = T²S₁ = [206.9, 142.3, 100.8]: juice ≈ 142.', 'S1'),
 ('g1t', 3, '11C', 'A', 'Steady state: T³⁰S₁ = T³¹S₁ = [208.7, 140.4, 100.9]: iced tea ≈ 209.', None),
 ('g1t', 7, '11C', 'A', 'G₃ = T⁻¹G₄ = [2.28, 2.00, 11.55, 5.91, 6.25]: 2 students received a B.', 'S3'),
 ('g1t', 8, '11C', 'C', 'Steady state: T³⁰G₄ = T³¹G₄, A ≈ 5.4, so 5 students.', None),
 ('g1t', 14, '11C', 'D', 'First Sunday = T⁻²S₃ = [111.3, 316.9, 71.8]: Masterchess ≈ 317.', None),
 ('g1m', 24, '11C', 'E', 'S₁ = T⁻¹S₂ = [381.3, 246.4, 137.3].', None),
 ('g1m', 29, '11C', 'E', 'Roster A, C, B, D repeats: week 1 A C B D A, week 2 C B D A C, week 3 B D A C B, week 4 D A C B D. B\'s fifth day is Thursday of week 4, not Friday of week 3.', None),
 ('g1t', 4, '11D', 'B', 'August 2019 = T²A₂₀₁₇: adults ≈ 13.7, so 14.', 'S2'),
 ('g1t', 5, '11D', 'C', 'TA₂₀₁₇ leaves 4 puppies of the 25, so 21 new puppies are needed each year.', None),
 ('g1t', 9, '11D', 'D', 'Term 1 Year 11 = S₁, so Term 3 Year 12 = S₇ = T⁶S₁ = [111.6, 67.9, 17.3, 33.2].', 'S4'),
 ('g1t', 10, '11D', 'C', 'T⁴S₁ gives Maths C = 19.06 < 20 (T³S₁ = 20.2): S₅ = Term 1 Year 12.', None),
 ('g1t', 11, '11D', 'D', 'S₂ = TS₁ + B = [117.4, 71.4, 23.1, 15.1]; S₃ = TS₂ + B = [115.1, 72.2, 21.5, 15.2].', None),
]
# GM2 SA: (n, sub, marks, [answers])
SA = [
 (9, '11B', 2, ['a i. 0.06 × 5 + 0.24 × 12 + 0.76 × 21 = 19', 'a ii. Did not change: 0.92×5 + 0.62×12 + 0.76×21 = 28, so 38 − 28 = 10 changed.']),
 (2, '11C', 3, ['a. 100% − 72% = 28', 'b. 0.23×51 + 0.09×73 + 0.65×101 ≈ 12 + 7 + 66 = 85', 'c. 0.55 × 51 ≈ 28, then 0.55 × 28 ≈ 15']),
 (3, '11C', 5, ['a. (0.18 + 0.32)×120 + (0.34 + 0.22)×120 + (0.12 + 0.11)×120 = 154.8 ≈ 155',
               'b. M₃ = T²M₁ = [91; 62; 146; 60] (F, H, S, L)', 'c. M₅ = T⁴M₁: S ≈ 129',
               'd. 2025 = M₈ = T⁷M₁: H ≈ 36, which is 36/120 = 30% of 2018. Not below 25%, so the manager is not correct.']),
 (4, '11C', 5, ['a. 20%', 'b. 0.10×3500 + 0.12×3500 + 0.86×3500 + 0.05×3500 = 3955', 'c. S₁ = TS₀ = [3605; 3115; 3955; 3325]',
               'd. S₃ = T³S₀: B ≈ 2630 g', 'e. S₃₀ = S₃₁: D ≈ 2619.28; 2619.28 ÷ 14000 × 100 ≈ 18.7%']),
 (6, '11C', 5, ['a. 1650', 'b. V₁ = TV₀ = [1540; 1865; 1595]', 'c. 0.45×1650 + 0.35×1850 = 1390; 1390 ÷ 1540 × 100 ≈ 90%',
               'd i. V₂₉ = V₃₀ = [1543.91; 1798.87; 1657.22]', 'd ii. 1657']),
 (1, '11D', 8, ['a. f = 132 (S₁ = TS₀ = [152.5; 132; 133.75; 181.75])', 'b. 0.13×250 + 0.11×125 + 0.62×125 + 0.10×100 = 133.75 ≈ 134',
               'c i. 68%', 'c ii. 0.32 × 100 = 32', 'd. S₅₀ = S₅₁ = [110.183; 115.693; 134.297; 239.827]: 110 customers',
               'e. F₂₀₁₇ = TJ₂₀₁₇ + B = [287.1; 297.1; 331.65; 389.15]; M₂₀₁₇ = TF₂₀₁₇ + B: Burton ≈ 345']),
 (5, '11D', 2, ['a. 4000 g', 'b. R₁ must equal R₀: TR₀ = [3900; 3440; 4420; 2240], so G = [100; 560; −420; −240]']),
 (7, '11D', 3, ['a. No child does the same activity two hours in a row.', 'b. K × L₀: W = 126, X = 135, Y = 189, Z = 150',
               'c. B = [24; 15; −39; 0]']),
 (8, '11D', 5, ['a. 0.05 × 20 = 1', 'b. S₄ = T⁴S₀: N ≈ 23', 'c. S₅₀ = S₅₁ ≈ [22.5; 30.2; 19.3]: fiction 2 staff, nonfiction 3, other 2',
               'd. [0.85 0.08 0.05; 0.1 0.9 0.04; 0.05 0.02 0.91] × [20; 18; 34] + [2; 0; −1] = [22.14; 19.56; 31.3]']),
 (10, '11D', 3, ['a. Four additional backpackers will need a dormitory room.',
                 'b. S₁ = TS₀ + B = [7.01; 9.85; 23.14]; S₂ = TS₁ + B ≈ [9; …; 24]: 9 people for 8 single rooms and 24 for 22 dormitory rooms, so not all can be accommodated.']),
 (11, '11E', 3, ['a i. LS₀ = [2800; 350; 150]', 'a ii. 3300 − 1500 = 1800', 'b. L²S₀ = [1660; 1960; 105]: 1960']),
]
STEMS = {'S1': 'Questions 2 and 3', 'S2': 'Questions 4 and 5', 'S3': 'Questions 7 and 8', 'S4': 'Questions 9–11'}


def trim_header(path):
    """Drop Insight's 'Question n' header line (first text band) and return a PNG data URI + width in px."""
    im = Image.open(path).convert('L')
    g = ImageOps.invert(im).point(lambda v: 255 if v > 60 else 0)
    rows = [g.crop((0, y, g.width, y + 1)).getbbox() is not None for y in range(min(g.height, 200))]
    y = 0
    while y < len(rows) and not rows[y]: y += 1
    while y < len(rows) and rows[y]: y += 1   # end of header band
    im = im.crop((0, y, im.width, im.height))
    bb = ImageOps.invert(im).point(lambda v: 255 if v > 60 else 0).getbbox()
    if bb: im = im.crop((max(bb[0] - 6, 0), max(bb[1] - 6, 0), min(bb[2] + 6, im.width), min(bb[3] + 6, im.height)))
    import io
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode(), im.width


MM = 25.4 / 220  # crop px -> mm at print size


def img(path, scale):
    uri, w = trim_header(path)
    return f'<div class="fig"><img src="{uri}" style="width:{w * MM * scale:.1f}mm;max-width:100%"></div>'


EXTRA = """
.fig{text-align:left;margin:1mm 0} .fig img{display:block}
.secthd{break-after:avoid} .box{break-inside:avoid}
.subhd{display:flex;align-items:center;gap:4mm;border:2px solid #000;padding:1.5mm 4mm;margin:0 0 3mm;background:#eee;break-after:avoid}
.subhd .c{font-size:18pt;font-weight:bold;border-right:2px solid #000;padding-right:4mm}
.subhd h2{font-size:13pt;margin:0;flex:1}
.subhd .dn{font-size:9.5pt;white-space:nowrap;display:flex;gap:3mm;align-items:center}
.subhd .dn i{display:inline-block;border-bottom:1px solid #000;width:24mm;height:4mm}
.subhd .dn .tick{margin:0}
.qgrid.one{grid-template-columns:1fr}
.cover td{padding:1.2mm 3mm}
.ans{display:block;color:#c00;font-size:9.5pt;border-top:1px dashed #999;margin-top:1.5mm;padding-top:1mm;visibility:hidden}
.sol .ans{visibility:visible}
.mccols{column-count:2;column-gap:3mm} .mccols .box{display:inline-block;width:100%}
.subhd{margin-top:4mm}
.box.sab{break-inside:auto} .box.sab .fig{break-inside:avoid}
.ans p{margin:.4mm 0}
"""


def img_split(path, scale, gap=40):
    """Like img() but cut the crop at wide white bands so a long question can run over a page break."""
    import io
    uri, w = trim_header(path)
    im = Image.open(io.BytesIO(base64.b64decode(uri.split(',', 1)[1]))).convert('L')
    g = ImageOps.invert(im).point(lambda v: 255 if v > 60 else 0)
    blank = [g.crop((0, y, g.width, y + 1)).getbbox() is None for y in range(im.height)]
    cuts, run = [0], 0
    for y, b in enumerate(blank):
        run = run + 1 if b else 0
        if run == gap and y - cuts[-1] > 300: cuts.append(y - gap // 2)
    cuts.append(im.height)
    out = ''
    for a, b in zip(cuts, cuts[1:]):
        piece = im.crop((0, a, im.width, b)); bio = io.BytesIO(); piece.save(bio, 'PNG', optimize=True)
        out += (f'<div class="fig"><img src="data:image/png;base64,{base64.b64encode(bio.getvalue()).decode()}" '
                f'style="width:{w * MM * scale:.1f}mm;max-width:100%"></div>')
    return out


def stem_box(k):
    return (f'<div class="box"><div class="hd">Use the following information<span></span></div><div class="bd">'
            f'{img(f"crops/g1tq{k}.png", 0.82)}'
            f'<div class="cite">{G1} p.{pg(S1, k)}</div></div></div>')


def mc_box(tag, n, sub, a, why, stem, num):
    if tag == 'g1m':
        src, page = G1M, {24: 11, 29: 12}[n]
    else:
        src, page = G1, pg(S1, n)
    return (f'<div class="box"><div class="hd">Question {num}<span>1 mark</span></div><div class="bd">'
            f'{img(f"crops/{tag}q{n}.png", 0.82)}'
            f'<div class="ans"><b>{a}</b> ✓ {why}</div>'
            f'<div class="cite">{src} p.{page} Q{n}</div></div></div>')


def sa_box(n, sub, marks, ans, num):
    page = pg(S2, n)
    a = ''.join(f'<p>{x}</p>' for x in ans)
    return (f'<div class="box sab"><div class="hd">Question {num}<span>{marks} marks</span></div><div class="bd">'
            f'{img_split(f"crops/g2tq{n}.png", 0.8)}'
            f'<div class="ans">{a}</div>'
            f'<div class="cite">{G2} p.{page} Q{n} · write your answers on the lines</div></div></div>')


def build(sol):
    css = open('cfat.css').read() + EXTRA
    body = ('<div class="title"><div class="code">Ch 11<br>REV</div><h1>Transition and Leslie matrices'
            f'<div style="font-size:10pt;font-weight:normal;margin-top:1mm">Revision booklet{" · <b style=\"color:#c00\">WORKED SOLUTIONS</b>" if sol else ""} · 11A–11E · CAS and bound reference allowed</div></h1>'
            '<div class="who"><div><b>Name</b> <i></i></div></div></div>')
    rows = ''
    for code, name in SUBS:
        m = [q for q in MC if (q[2] if len(q) == 6 else q[1]) == code]; s = [q for q in SA if (q[2] if len(q) == 6 else q[1]) == code]
        qs = (f'{len(m)} MC' if m else '') + (' + ' if m and s else '') + (f'{len(s)} short answer' if s else '')
        rows += f'<tr><td><b>{code}</b></td><td>{name}</td><td>{qs}</td><td>{len(m) + sum(q[2] for q in s)}</td><td><div class="tick"></div></td></tr>'
    body += ('<div class="box"><div class="hd">How to use this booklet<span></span></div><div class="bd">'
             '<p class="q">One section per Cambridge subchapter. After each lesson, do the section for that subchapter: answer every question, check against the worked solutions, and correct in a different colour. Tick the box when the section is done and corrected.</p>'
             '<p class="q">Questions are copied from Insight Publications, <i>General Maths 1 – Unit 4</i> (multiple choice) and <i>General Maths 2 – Unit 4</i> (short answer), section ‘Matrices — Transition matrices’ (plus two transition questions from ‘Matrices and their applications’), © Insight Publications 2022. Each question shows its Insight page and number.</p>'
             '<table class="t cover" style="width:100%"><tr><th>Sub</th><th class="l">Topic</th><th>Questions</th><th>Marks</th><th>Done</th></tr>' + rows + '</table></div></div>')
    num = 0
    for code, name in SUBS:
        m = [q for q in MC if (q[2] if len(q) == 6 else q[1]) == code]; s = [q for q in SA if (q[2] if len(q) == 6 else q[1]) == code]
        body += (f'<div class="subhd"><div class="c">{code}</div><h2>{name}</h2>'
                 '<div class="dn">Done <div class="tick"></div> Date <i></i></div></div>')
        if m:
            body += f'<div class="secthd">Multiple choice<span>Circle one answer. {len(m)} mark{"s" if len(m) > 1 else ""}</span></div>'
            body += '<div class="mccols">'
            for q in m:
                if q[5]: body += stem_box(q[5])
                num += 1; body += mc_box(*q, num)
            body += '</div>'
        if s:
            body += f'<div class="secthd">Short answer<span>Show your working. {sum(q[2] for q in s)} marks</span></div>'
            for q in s:
                num += 1; body += sa_box(*q, num)
    title = 'Ch11 revision booklet' + (' solutions' if sol else '')
    L = os.path.join('..', '..', '..', 'lessons')
    js = ''
    if A4VIEW:
        js = ''.join(f'<script>{open(os.path.join(L, f)).read()}</script>' for f in ('a4view.js', 'paged.polyfill.min.js'))
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style>{js}</head><body class="{"sol" if sol else ""}">{body}</body></html>'


os.makedirs('out', exist_ok=True)
for sol in (0, 1):
    open(f'out/Ch11-revision-booklet{"-solutions" if sol else ""}.html', 'w').write(build(sol))
print('ok')
