"""Build the Ch10 revision booklet (Matrices: 10A-10G) + solutions.
Source: Insight GM1 Unit 4 (MCQ) 'Matrices - Matrices and their applications' Q1-30 (printed pp.4-13 = pdf 5-14;
answers/explanatory notes printed pp.32-37) and Insight GM2 Unit 4 (Short Answer) same section Q1-9 (printed pp.4-9 =
pdf 5-10; worked solutions printed pp.41-42). (C) Insight Publications 2022. Insight is never burnt.
Questions are shown as crops of the Insight pages (scanned books; matrices are not retyped), so they are verbatim.
Crops made by seg.py (finds 'Question n' headers with tesseract) + mk.py (stitches fragments that run over a column/page);
the Insight 'Question n' header line is trimmed off here (the booklet numbers its own boxes and cites the Insight number).
Left out: GM1 Q24 and Q29 (transition matrices: Chapter 11); the 'Transition matrices' sections of both books (Chapter 11).
Answers: Insight's answers; the one-line 'why' is condensed from Insight's explanatory notes / worked solutions."""
import base64, os, sys
from PIL import Image, ImageOps
os.chdir(os.path.dirname(os.path.abspath(__file__)))
A4VIEW = '--print' not in sys.argv
G1 = 'Insight GM1 Unit 4 (Matrices and their applications)'
G2 = 'Insight GM2 Unit 4 (Matrices and their applications)'
SUBS = [('10A', 'Matrix basics'), ('10B', 'Using matrices to represent information'),
        ('10C', 'Matrix addition, subtraction and scalar multiplication'), ('10D', 'The product of two matrices'),
        ('10E', 'Matrix inverse, the determinant and matrix equations'), ('10F', 'Binary, permutation and communication matrices'),
        ('10G', 'Dominance matrices')]
# GM1 MC: n, sub, printed page, answer, why
MC = [
 (1, '10A', 4, 'C', 'The transpose swaps rows and columns: row 1 becomes column 1.'),
 (19, '10A', 9, 'B', 'Triangular, square, permutation and identity matrices must be square; a binary matrix can be any order.'),
 (25, '10A', 11, 'D', 'm<sub>21</sub> = row 2, column 1 = 23.'),
 (3, '10B', 5, 'D', 'n<sub>ij</sub> = 2j + i: row 1 = 3, 5; row 2 = 4, 6; row 3 = 5, 7.'),
 (5, '10B', 5, 'B', 'Monday: 2865 customers ÷ 8 hours = 358.125 ≈ 358.'),
 (11, '10B', 7, 'E', 'Add the evening (E) column: 13 + 21 + 8 = 42.'),
 (21, '10B', 10, 'D', 'a<sub>ij</sub> = 2i − j gives a 1×4 row 1, 0, −1, −2: the last element should be −2, not −4.'),
 (9, '10C', 6, 'B', 'g<sub>ij</sub> = −2i + j gives [−1 0; −3 −2; −5 −4]; then multiply every element by 2.'),
 (28, '10C', 12, 'A', '3M = [1 −2 22; 25 39 12] − 2N = [3 −6 12; 21 33 0], so M = ⅓ × that = [1 −2 4; 7 11 0].'),
 (2, '10D', 4, 'E', 'A total needs a 1×1 matrix: (1×4 costs) × (4×1 numbers sold) = 3.50×65 + 2.50×156 + 4.00×105 + 1.75×256 = $1485.50.'),
 (8, '10D', 6, 'C', 'Bath mat: 22.45 − 17.51 = 4.94, which is 22% of 22.45, so c = 1 − 0.22 = 0.78.'),
 (14, '10D', 8, 'D', '(1×6 numbers) × (6×1 prices) is the only 1×1 product: $147.78.'),
 (16, '10D', 8, 'E', '(4×2) × (2×1) = 4×1: one total revenue per farm. A, B, D are not defined; C gives 4×2.'),
 (17, '10D', 9, 'E', 'A² defined → A square; A + B defined → same order; ABC is 4×2 → A 4×4, B 4×4, C 4×2.'),
 (20, '10D', 10, 'C', 'A total needs 1×1: (1×3 prices) × (3×1 numbers of people). A, B, E give 3×3; D has the numbers in the wrong order.'),
 (22, '10D', 10, 'C', '2b and 2d use row 1 of the first matrix: 3 × 2b − 1 × 2d, not 3 × 2b − 2 × 2d.'),
 (26, '10D', 11, 'B', 'E<sup>T</sup> is 3×2 and 2F is 2×4, so E<sup>T</sup> × 2F is 3×4.'),
 (30, '10D', 13, 'D', 'Diagonal matrices keep the international and domestic costs apart and pair each quantity with its own rate.'),
 (7, '10E', 6, 'D', 'B is not square. det A = 15, det C = 342, det D = 18 (all non-zero), so 3 inverses.'),
 (10, '10E', 6, 'D', 'R × [2 3; 1 2] = [4 7; −1 3] − [1 2; −2 1] = [3 5; 1 2], so R = [3 5; 1 2] × [2 3; 1 2]<sup>−1</sup> = [1 1; 0 1].'),
 (12, '10E', 7, 'C', 'det A = −20, det B = −7; C and D are not square (no determinant), so 2.'),
 (15, '10E', 8, 'B', 'det = 4×2 − 3×3 = −1, so inverse = −1 × [2 −3; −3 4] = [−2 3; 3 −4].'),
 (27, '10E', 12, 'B', 'det K = 3×(−4) − 2×(−6) = 0, so K has no inverse.'),
 (6, '10F', 5, 'E', 'Following the matrix from Monday, only option E (pork Monday) gives fish on Friday.'),
 (13, '10F', 7, 'B', 'Add row B (Brad): 0 + 0 + 0 + 0 + 1 = 1.'),
 (4, '10G', 5, 'B', 'One-step + two-step dominance: A 2, B 8, C 3, D 6, E 7, so Benjamin wins.'),
 (18, '10G', 9, 'A', 'John lost only to Fred, so beat Gloria, Harriet and Ingrid; Gloria won none; Harriet beat Fred, Gloria and Ingrid.'),
 (23, '10G', 11, 'B', 'One-step + two-step totals: A 2, B 4, C 3, D 5, so Daphne, Bruce, Cristiano, Alia.'),
]
# GM2 SA: n, sub, printed page, marks, [answers per part], space (mm) for the answer strip
SA = [
 (2, '10B', 4, 2, ['a. 107 + 95 + 52 = 254', 'b. The number of occasional (O) memberships taken in February (52).']),
 (1, '10D', 4, 4, ['a. 4 × 1', 'b i. M = [4 5.60 7.20 9] × P = [3637]',
                   'b ii. The total amount (dollars) the company charged for all parcels delivered in January 2016.',
                   'b iii. The number of columns of P (1) equals the number of rows of C (1).']),
 (3, '10D', 5, 3, ['a. $9.78', 'b. 3 × 1', 'c. B = [1 0 2]']),
 (4, '10D', 5, 2, ['a. 25 − 10% × 25 = 22.5 ≈ 23 m²', 'b. D = [0.9 0 0; 0 0.9 0; 0 0 0.9]']),
 (5, '10D', 6, 4, ['a. 3 × 3', 'b. 35 + 22 + 28 = 85', 'c. 87×3.80 + 22×4.50 + 35×6.00 = $639.60', 'd. (48 + 35 + 44) × 6 = 762']),
 (6, '10D', 7, 3, ['a. 3 × 2', 'b. 10 spaces in carpark A for visitors with prams.', 'c. [1 1 1] × S = [170 92]']),
 (7, '10D', 7, 2, ['a. F = [11.45; 9.98] (column)', 'b. N × F = [12 16] × [11.45; 9.98] = $297.08']),
 (8, '10D', 8, 4, ['a. 1 + 2 = 3', 'b. T = [1 1 0 1]',
                   'c. (1/9) × [1 2 12 6] × [9; 14; 2; 4] = 85/9 ≈ 9.4, so 10 toilets (round up to have at least one per nine people).']),
 (9, '10G', 9, 3, ['a i. Team B', 'a ii. Team D beat Teams C and E.']),
]


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
.ans{color:#c00;font-size:9.5pt;border-top:1px dashed #999;margin-top:1.5mm;padding-top:1mm;visibility:hidden}
.sol .ans{visibility:visible}
.mccols{column-count:2;column-gap:3mm} .mccols .box{display:inline-block;width:100%}
.subhd{margin-top:4mm}
.ans p{margin:.4mm 0}
"""


def mc_box(n, sub, page, a, why, num):
    return (f'<div class="box"><div class="hd">Question {num}<span>1 mark</span></div><div class="bd">'
            f'{img(f"crops/g1q{n}.png", 0.82)}'
            f'<div class="ans"><b>{a}</b> ✓ {why}</div>'
            f'<div class="cite">{G1} p.{page} Q{n}</div></div></div>')


def sa_box(n, sub, page, marks, ans, num):
    a = ''.join(f'<p>{x}</p>' for x in ans)
    return (f'<div class="box"><div class="hd">Question {num}<span>{marks} marks</span></div><div class="bd">'
            f'{img(f"crops/g2q{n}.png", 0.8)}'
            f'<div class="ans">{a}</div>'
            f'<div class="cite">{G2} p.{page} Q{n} · write your answers on the lines</div></div></div>')


def build(sol):
    css = open('cfat.css').read() + EXTRA
    body = ('<div class="title"><div class="code">Ch 10<br>REV</div><h1>Matrices'
            f'<div style="font-size:10pt;font-weight:normal;margin-top:1mm">Revision booklet{" · <b style=\"color:#c00\">WORKED SOLUTIONS</b>" if sol else ""} · 10A–10G · CAS and bound reference allowed</div></h1>'
            '<div class="who"><div><b>Name</b> <i></i></div></div></div>')
    rows = ''
    for code, name in SUBS:
        m = [q for q in MC if q[1] == code]; s = [q for q in SA if q[1] == code]
        qs = (f'{len(m)} MC' if m else '') + (' + ' if m and s else '') + (f'{len(s)} short answer' if s else '')
        rows += f'<tr><td><b>{code}</b></td><td>{name}</td><td>{qs}</td><td>{len(m) + sum(q[3] for q in s)}</td><td><div class="tick"></div></td></tr>'
    body += ('<div class="box"><div class="hd">How to use this booklet<span></span></div><div class="bd">'
             '<p class="q">One section per Cambridge subchapter. After each lesson, do the section for that subchapter: answer every question, check against the worked solutions, and correct in a different colour. Tick the box when the section is done and corrected.</p>'
             '<p class="q">Questions are copied from Insight Publications, <i>General Maths 1 – Unit 4</i> (multiple choice) and <i>General Maths 2 – Unit 4</i> (short answer), section ‘Matrices — Matrices and their applications’, © Insight Publications 2022. Each question shows its Insight page and number. Transition matrix questions are in the Chapter 11 booklet.</p>'
             '<table class="t cover" style="width:100%"><tr><th>Sub</th><th class="l">Topic</th><th>Questions</th><th>Marks</th><th>Done</th></tr>' + rows + '</table></div></div>')
    num = 0
    for code, name in SUBS:
        m = [q for q in MC if q[1] == code]; s = [q for q in SA if q[1] == code]
        body += (f'<div class="subhd"><div class="c">{code}</div><h2>{name}</h2>'
                 '<div class="dn">Done <div class="tick"></div> Date <i></i></div></div>')
        if m:
            body += f'<div class="secthd">Multiple choice<span>Circle one answer. {len(m)} mark{"s" if len(m) > 1 else ""}</span></div>'
            body += '<div class="mccols">'
            for q in m:
                num += 1; body += mc_box(*q, num)
            body += '</div>'
        if s:
            body += f'<div class="secthd">Short answer<span>Show your working. {sum(q[3] for q in s)} marks</span></div>'
            for q in s:
                num += 1; body += sa_box(*q, num)
    title = 'Ch10 revision booklet' + (' solutions' if sol else '')
    L = os.path.join('..', '..', '..', 'lessons')
    js = ''
    if A4VIEW:
        js = ''.join(f'<script>{open(os.path.join(L, f)).read()}</script>' for f in ('a4view.js', 'paged.polyfill.min.js'))
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style>{js}</head><body class="{"sol" if sol else ""}">{body}</body></html>'


os.makedirs('out', exist_ok=True)
for sol in (0, 1):
    open(f'out/Ch10-revision-booklet{"-solutions" if sol else ""}.html', 'w').write(build(sol))
print('ok')
