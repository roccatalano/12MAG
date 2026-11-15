"""Chapter 1 test (1A-1I) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css). Same layout as tools/test/ch2/build.py.
Source (rule 9: chapter tests = Mathspace topic assessments), copied verbatim:
  Mathspace, General Maths 3&4, Chapter 1 - Investigate data distributions, 'Chapter 1 - Topic assessment.pdf'
  + 'Chapter 1 - Topic assessment answer key.pdf' (02 Sources\\Textbooks\\Mathspace\\Chapter 1 - Investigate data distributions).
Mathspace lessons 1.01-1.11 (types of data ... standardised values) all sit in Cambridge 1A-1H. Mathspace lesson codes kept per question.
Left out: Mathspace Q8 (1.09 Compare data sets: comparing two boxplots = Cambridge Ch 2 (2D), not Ch 1). Mathspace Q9-Q20 renumbered 8-19.
Adapted: Q11 (Mathspace Q12) bar chart: the answer key shows no chart, so the solutions chart is drawn for 12MAG from the table.
Figures (dot plot, histogram, bar chart) are crops of the Mathspace PDF (q2.png, q3.png, q9.png).
Answers checked with numpy (mean 7.14; dot plot n=18 median 4; Q20 hours median 10, Q1 8, Q3 13, IQR 5, UF 20.5, mean 11.13) and by hand (z-scores, 68-95-99.7%).
Run: python3 tools/test/ch1/build.py lessons  -> 'Ch1 test.html/.pdf' + 'Ch1 test solutions.html/.pdf'
"""
import sys, os, html, base64
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, '../../cfat/ch2/cfat.css')).read() + """
body{font-size:9.6pt;line-height:1.25}
.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:3mm} .qgrid .box{margin-bottom:0}
.mcl div{margin:.6mm 0} .mcl b{display:inline-block;width:5mm}
.mc2{display:grid;grid-template-columns:1fr 1fr;gap:.5mm 3mm}
.ans{color:#c00;display:none;white-space:pre-wrap} .sol .ans{display:block}
.ok{color:#c00;font-weight:bold;display:none} .sol .ok{display:inline}
.part{border-top:1px dashed #000;padding:1mm 0 0;margin-top:1mm} .part .pq b{margin-right:2mm}
.sp{min-height:var(--h)} .mk{color:#555;font-size:8.5pt}
table.t{border-collapse:collapse;margin:1mm 0} table.t td,table.t th{border:1px solid #000;padding:.5mm 2mm;text-align:center}
.cite{font-size:7.5pt;color:#555;margin-top:1mm}
.stem3 td{border:none!important;padding:0 2mm!important;font-family:monospace;font-size:10pt} .stem3 td.s{border-left:1px solid #000!important;border-right:1px solid #000!important}
.secthd{font-weight:bold;border-bottom:2px solid #000;margin:2mm 0;display:flex;justify-content:space-between}
"""
E = html.escape
SRC = 'Mathspace Ch 1 topic assessment'
def IMG(f, w):
    b = base64.b64encode(open(os.path.join(HERE, f), 'rb').read()).decode()
    return f'<div style="text-align:center;margin:1mm 0"><img src="data:image/png;base64,{b}" style="width:{w}mm"></div>'
MC = [  # (lesson, stem html, options, correct index)
 ('Q1 · 1.01', 'Which of the following is an example of numerical discrete data?',
  ['The number of goals scored in a match', 'The colour of cars in a car park', 'The height of students in a class', 'The temperature recorded each hour'], 0),
 ('Q2 · 1.03', 'The dot plot below shows the number of books read by students over a school term. What is the median number of books read?' + IMG('q2.png', 48),
  ['3', '4', '4.5', '5'], 1),
 ('Q3 · 1.04', 'The histogram below shows the distribution of times (in minutes) taken by students to complete a puzzle. Which description best matches the shape of the distribution?' + IMG('q3.png', 42),
  ['Positively skewed', 'Approximately symmetric', 'Negatively skewed', 'Uniform'], 1),
 ('Q4 · 1.05', 'The masses of a group of animals range from 0.01 kg to 10 000 kg. Which type of scale is most appropriate for displaying this data?',
  ['A linear scale from 0 to 10 000', 'A logarithmic scale', 'A percentage scale', 'A frequency scale'], 1),
 ('Q5 · 1.06', 'The data set 3, 5, 7, 7, 8, 9, 11 has a mean of:', ['7', '7.14', '8', '7.5'], 1),
 ('Q6 · 1.07', 'For the data set 4, 6, 8, 10, 12, 14, 16, the interquartile range (IQR) is:', ['6', '10', '8', '12'], 2),
 ('Q7 · 1.08', 'A boxplot shows: minimum 10, <i>Q</i><sub>1</sub> = 18, median 24, <i>Q</i><sub>3</sub> = 30, maximum 40. What is the IQR?', ['12', '6', '14', '30'], 0),
 ('Q9 · 1.02', 'The bar chart below shows the number of students who chose each sport as their favourite. How many students chose swimming or tennis?' + IMG('q9.png', 80),
  ['14', '16', '21', '26'], 1),
 ('Q10 · 1.11', "A student scores 72 on a test where the mean is 60 and the standard deviation is 8. The student's standardised score (z-score) is:", ['1.5', '2', '0.67', '1.2'], 0),
 ('Q11 · 1.10', 'Which of the following features is characteristic of a normal distribution?',
  ['The mean is always greater than the median', 'The distribution is skewed to the right', 'The mean, median, and mode are all equal', 'The total area under the curve is greater than 1'], 2),
]
def T(rows, head=True):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{E(c)}</th>' if (head and i == 0) else f'<td>{E(c)}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']; CUS = [45, 38, 52, 41, 67, 89, 73]
def BAR():
    W, H, x0, y0 = 170, 62, 14, 52; sc = 44 / 100; bw = 18
    s = f'<svg viewBox="0 0 {W} {H}" style="width:150mm" font-size="3" fill="#c00" stroke="#c00">'
    s += f'<text x="{W/2}" y="4" text-anchor="middle" stroke="none" font-weight="bold">Number of customers visiting a café each day</text>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="6" stroke-width=".3"/><line x1="{x0}" y1="{y0}" x2="{W-2}" y2="{y0}" stroke-width=".3"/>'
    for v in range(0, 101, 20):
        y = y0 - v * sc; s += f'<line x1="{x0-1}" y1="{y}" x2="{x0}" y2="{y}" stroke-width=".3"/><text x="{x0-1.5}" y="{y+1}" text-anchor="end" stroke="none">{v}</text>'
    for i, (d, c) in enumerate(zip(DAYS, CUS)):
        x = x0 + 3 + i * 22; s += f'<rect x="{x}" y="{y0-c*sc}" width="{bw}" height="{c*sc}" fill="none" stroke-width=".4"/>'
        s += f'<text x="{x+bw/2}" y="{y0-c*sc-1}" text-anchor="middle" stroke="none">{c}</text><text x="{x+bw/2}" y="{y0+4}" text-anchor="middle" stroke="none">{d}</text>'
    s += f'<text x="{W/2}" y="{H-1}" text-anchor="middle" stroke="none">Day</text><text transform="translate(4 {y0/2+4}) rotate(-90)" text-anchor="middle" stroke="none">Customers</text></svg>'
    return s
STATS = T([['x̄', '6.84'], ['s<sub>x</sub>', '4.12'], ['n', '25'], ['minX', '0'], ['Q<sub>1</sub>', '3'], ['Median', '6'], ['Q<sub>3</sub>', '9'], ['maxX', '21']], head=False).replace('&lt;sub&gt;', '<sub>').replace('&lt;/sub&gt;', '</sub>')
SA = [  # (lesson, stem html, [(label, text, marks, answer html, space mm)])
 ('Q12 · 1.02', 'The table below shows the number of customers who visited a café on each day of the week.' + T([['Day'] + DAYS, ['Customers'] + [str(c) for c in CUS]])
  + 'Construct a bar chart to display this data, clearly labelling the axes and title.',
  [('', '', 2, BAR(), 62)]),
 ('Q13 · 1.07', 'The number of minutes late was recorded for 25 V/Line trains arriving at Southern Cross Station. The summary statistics from a CAS calculator are shown below.' + STATS
  + 'State the range and the interquartile range (IQR) of the number of minutes late.',
  [('', '', 2, 'Range = 21 minutes, IQR = 6 minutes', 12)]),
 ('Q14 · 1.11', "Scores on a reading speed test have a mean of 240 words per minute and a standard deviation of 35 words per minute. Ella's standardised score on the test is −1.6. Calculate Ella's reading speed, in words per minute.",
  [('', '', 2, '240 − 1.6 × 35 = 184 words per minute', 16)]),
 ('Q15 · 1.10', 'The wingspans of adult wedge-tailed eagles are approximately normally distributed with a mean of 2.10 m and a standard deviation of 0.12 m. Using the 68 − 95 − 99.7% rule, determine the percentage of adult wedge-tailed eagles with a wingspan greater than 2.34 m.',
  [('', '', 1, '2.34 = 2.10 + 2 × 0.12, so 2.5%', 14)]),
 ('Q16 · 1.06', 'The mean of a set of 9 test scores is 14. A tenth score of 24 is added to the set. Calculate the mean of the 10 scores.',
  [('', '', 1, '(9 × 14 + 24) ÷ 10 = 150 ÷ 10 = 15', 12)]),
 ('Q17 · 1.11', "Liam's results in two Year 12 subjects, together with the mean and standard deviation of the scores for his cohort, are shown in the table below."
  + T([['Subject', 'Score', 'Cohort mean', 'Cohort standard deviation'], ['General Mathematics', '71', '62', '6'], ['English', '78', '70', '10']]),
  [('a', "Calculate Liam's standardised score in General Mathematics.", 1, '(71 − 62) ÷ 6 = 1.5', 9),
   ('b', "Calculate Liam's standardised score in English.", 1, '(78 − 70) ÷ 10 = 0.8', 9),
   ('c', 'Relative to his cohort, in which subject did Liam perform better? Justify your answer.', 2,
    'General Mathematics. His standardised score in General Mathematics (1.5) is higher than his standardised score in English (0.8).', 14)]),
 ('Q18 · 1.10', 'The masses of packets of rice crackers filled by a machine at a factory in Dandenong are approximately normally distributed with a mean of 250 g and a standard deviation of 4 g. Use the 68 − 95 − 99.7% rule to answer the following.',
  [('a', 'Determine the percentage of packets with a mass between 242 g and 254 g.', 1, '242 = μ − 2σ, 254 = μ + σ: 47.5% + 34% = 81.5%', 10),
   ('b', 'In a batch of 2000 packets, how many packets would be expected to have a mass less than 246 g?', 1, '246 = μ − σ: 16% × 2000 = 320', 10),
   ('c', 'Packets with a mass less than 238 g are rejected. How many of the 2000 packets would be expected to be rejected?', 1, '238 = μ − 3σ: 0.15% × 2000 = 3', 10)]),
 ('Q19 · 1.10', 'The times taken by commuters to cycle to work in Melbourne are approximately normally distributed. Of these commuters, 16% take longer than 38 minutes and 2.5% take less than 20 minutes.',
  [('a', 'Determine the mean and the standard deviation of the cycling times.', 3,
    'μ + σ = 38 and μ − 2σ = 20, so 3σ = 18<br>Mean = 32 minutes, standard deviation = 6 minutes', 22),
   ('b', 'Calculate the standardised score of a commuter who takes 41 minutes to cycle to work.', 1, '(41 − 32) ÷ 6 = 1.5', 9),
   ('c', 'Sam says that a cycling time of 50 minutes would be very unusual for these commuters. Use the 68 − 95 − 99.7% rule to decide whether Sam is correct.', 2,
    'Sam is correct. A time of 50 minutes is three standard deviations above the mean, so only about 0.15% of commuters take longer than this.', 16)]),
 ('Q20 · 1.08', 'The number of hours of part-time work completed in one week by 15 Year 12 students at a school in Geelong is shown below.'
  + T([['Hours worked', '4', '6', '7', '8', '8', '9', '10', '10', '11', '12', '12', '13', '14', '15', '28']], head=False),
  [('a', 'Determine the median and the interquartile range (IQR) of the number of hours worked.', 2, 'Median = 10 hours, IQR = 13 − 8 = 5 hours', 16),
   ('b', 'Show that the student who worked 28 hours is an outlier.', 1, 'The upper fence is 13 + 1.5 × 5 = 20.5 hours and 28 > 20.5, so 28 hours is an outlier.', 12),
   ('c', 'Describe the shape of the distribution.', 1, 'Positively skewed', 8),
   ('d', 'The mean number of hours worked is 11.13, rounded to two decimal places. Is the mean or the median the better measure of the centre of this data? Explain your answer.', 2,
    'The median. The distribution is positively skewed with an outlier, which increases the mean, whereas the median is not affected by the outlier.', 16)]),
]

def mk(n): return f'{n} mark{"s" if n > 1 else ""}'
def mcbox(n, q):
    les, stem, opts, a = q
    o = ''.join(f'<div><b>{"ABCD"[i]}</b>{E(x)} {"<span class=ok>✓</span>" if i == a else ""}</div>' for i, x in enumerate(opts))
    cls = 'mc2' if max(map(len, opts)) < 25 else 'mcl'
    return f'<div class="box"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><p class="q">{stem}</p><div class="{cls}">{o}</div><div class="cite">{SRC} · {les}</div></div></div>'
def sabox(n, q):
    les, stem, parts = q
    tot = sum(p[2] for p in parts)
    ps = ''
    for lab, txt, m, ans, h in parts:
        head = f'<div class="pq"><b>{lab}</b>{E(txt)} <span class="mk">({mk(m)})</span></div>' if lab else ''
        ps += f'<div class="part">{head}<div class="sp" style="--h:{h}mm"><div class="ans">{ans}</div></div></div>'
    return f'<div class="box"><div class="hd">Question {n}<span>{mk(tot)}</span></div><div class="bd"><p class="q">{stem}</p>{ps}<div class="cite">{SRC} · {les}</div></div></div>'

def page(sol):
    tot = len(MC) + sum(p[2] for q in SA for p in q[2])
    out = [f'<div class="title"><div class="code">Ch 1<br>test</div><h1>Investigating data distributions<div style="font-size:10pt;font-weight:normal;margin-top:1mm">1A–1I · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + mcbox(i + 2, MC[i + 1]) + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch1 test' + (' solutions' if sol else '')
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{t}</title><style>{CSS}</style>'
            f'<script src="a4view.js"></script><script src="paged.polyfill.min.js"></script></head><body class="{"sol" if sol else ""}">\n' + '\n'.join(out) + '\n</body></html>'), t

if __name__ == '__main__':
    od = sys.argv[1]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for sol in (False, True):
            h, t = page(sol); f = os.path.join(od, t + '.html'); open(f, 'w').write(h)
            pg = b.new_page(); pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(2500)
            pg.pdf(path=os.path.join(od, t + '.pdf'), prefer_css_page_size=True, print_background=True); pg.close(); print(t)
        b.close()
