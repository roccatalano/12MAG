"""Chapter 4 test (4A-4D, data transformations) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css). Model: tools/test/ch3/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4 has no transformations chapter; its transformation lessons are 3.05-3.07 in
'Chapter 3 - Model linear associations' (02 Sources\\Textbooks\\Mathspace). Used:
 - 'Chapter 3 - Topic assessment.pdf' + answer key: MC 3, 4, 6; SA 17, 18, 19 (the items the Ch 3 test leaves out; marks as printed).
 - 'Chapter 3 review - Question worksheet.pdf' + worked solutions: Q8-Q13 (3.05-3.07). Review Qs print no marks: marks assigned for 12MAG.
   Review Q15, Q16 (VCAA 2023 E1 Q11-12, 2024 E1 Q11) left out: current-design VCAA = Do Now pool (rule 4/10).
Answers checked with numpy (TA17 0.57 + 24.03/v, r2 0.9997; R8 -2.1 + 3.1x2, r 0.9994; R9 24.76 - 0.78x2; R10 2.2 + 3.0x, 4.82;
R11a 0.32 + 2.68 log x, r2 0.9867; R11b 0.35 + 100.18/x, r2 0.9991; R13 r2 0.6057 / 0.99996 / 0.7686, -0.49 + 17.98 log x, 20.7).
Run: python3 tools/test/ch4/build.py lessons -> 'Ch4 test.html/.pdf' + 'Ch4 test solutions.html/.pdf'
"""
import sys, os, html
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
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.9em;line-height:1.05}.fr span:first-child{border-bottom:1px solid #000;padding:0 1px}
.mc2 b{display:inline-block;width:5mm}
.blk{display:inline-block;min-width:9mm;height:4mm;text-align:center;line-height:4mm;border:1px solid #000;vertical-align:middle}
.secthd{font-weight:bold;border-bottom:2px solid #000;margin:2mm 0;display:flex;justify-content:space-between}
"""
E = html.escape

def F(a, b): return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'
TA = 'Mathspace Ch 3 topic assessment'
RV = 'Mathspace Chapter 3 review'
def T(rows, head=False):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{c}</th>' if (head and i == 0) else f'<td>{c}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
BL = '<span class="blk"></span>'
def blanktab(lab, xs, top=True):  # student copy: blank cells; solutions copy: red values
    return xs
MC = [
 (TA + ' Q3 · 3.05', 'The following data set has an upward-curving (parabolic) shape when plotted. Which transformation is most likely to linearise the data?'
  + T([['x', '1', '2', '3', '4', '5'], ['y', '2.1', '8.3', '18.5', '32.2', '50.1']]),
  [F(1, 'y') + ' transformation', 'x² transformation', F(1, 'x') + ' transformation', 'log(x) transformation'], 1),
 (TA + ' Q4 · 3.06', 'A data set shows a non-linear relationship where y decreases rapidly as x increases. Which transformation is most likely to linearise this data?',
  ['log(x) transformation', 'y² transformation', 'x² transformation', F(1, 'x') + ' transformation'], 3),
 (TA + ' Q6 · 3.07', 'A scatterplot of data on the population of bacteria (y) over time in hours (x) shows an upward-curving shape. After applying a log(y) transformation, the data appears linear. The regression equation on the transformed data is log(y) = 0.5 + 0.3x. What is the predicted value of y when x = 4?',
  ['50.1', '5.01', '1.7', '501'], 0),
]
def tab2(r1, r2, sol_vals):
    """r1 = top row (label + values); r2 label; sol_vals shown in red in the solutions copy only."""
    return T([r1, [r2[0]] + [BL] * (len(r1) - 1)])
SQ = '<table class="t"><tr><td>x²</td>' + ''.join(f'<td><span class="blk"><span class="ok">{v}</span></span></td>' for v in [1, 4, 9, 16, 25, 36]) + '</tr><tr><td>y</td>' + ''.join(f'<td>{v}</td>' for v in [3, 10, 25, 45, 75, 110]) + '</tr></table>'
SQA = '<table class="t" style="color:#c00"><tr><td>x²</td>' + ''.join(f'<td>{v}</td>' for v in [1, 4, 9, 16, 25, 36]) + '</tr><tr><td>y</td>' + ''.join(f'<td>{v}</td>' for v in [3, 10, 25, 45, 75, 110]) + '</tr></table>'
Y2 = '<table class="t"><tr><td>x</td>' + ''.join(f'<td>{v}</td>' for v in [1, 2, 3, 5, 8, 10]) + '</tr><tr><td>y²</td>' + ''.join(f'<td><span class="blk"><span class="ok">{v}</span></span></td>' for v in ['5.29', '7.84', '11.56', '16.00', '27.04', '31.36']) + '</tr></table>'
Y2A = '<table class="t" style="color:#c00"><tr><td>x</td>' + ''.join(f'<td>{v}</td>' for v in [1, 2, 3, 5, 8, 10]) + '</tr><tr><td>y²</td>' + ''.join(f'<td>{v}</td>' for v in ['5.29', '7.84', '11.56', '16.00', '27.04', '31.36']) + '</tr></table>'
FV = F(1, 'volunteers')
SA = [
 (TA + ' Q17 · 3.07', 'After a storm in Gippsland, teams of volunteers cleared fallen branches from sections of walking track of equal length. The number of volunteers in each team and the time taken, in hours, are shown below.'
  + T([['Volunteers', '1', '2', '3', '4', '5', '6', '8'], ['Time (hours)', '24.5', '12.8', '8.6', '6.7', '5.3', '4.6', '3.4']])
  + f'A reciprocal transformation is applied to the number of volunteers, so that time is modelled against {FV}.',
  [('a', f'Use technology to find the equation of the least-squares regression line for time against {FV}. Write the values rounded to two decimal places.', 2, f'time = 0.57 + 24.03 × {FV}', 14),
   ('b', 'Write the value of r² for the transformed data, rounded to four decimal places, and comment on how well the model fits.', 1, 'r² = 0.9997. The model fits the transformed data very well.', 12),
   ('c', 'Use the rounded equation from part (a) to predict the time taken by a team of 7 volunteers, rounded to two decimal places.', 1, f'time = 0.57 + 24.03 × {F(1, 7)} = 4.00 hours', 12),
   ('d', 'Use the model to find the minimum number of volunteers needed to clear a section in 2 hours or less, and comment on the reliability of this prediction.', 2, f'2 = 0.57 + 24.03 × {FV} → volunteers = 24.03 ÷ 1.43 ≈ 16.8, so 17 volunteers.\nThe prediction is unreliable because it is an extrapolation beyond the data (1 to 8 volunteers).', 20)]),
 (TA + ' Q18 · 3.07', 'A data set shows a non-linear relationship. After applying an x² transformation, the regression equation is y = 2.4 + 0.85x². Predict the value of y when x = 5. State whether this prediction is an interpolation or extrapolation, given the original data had x values between 1 and 6.',
  [('', '', 2, 'y = 2.4 + 0.85 × 5² = 23.65\nThis is an interpolation since x = 5 is within the original data range.', 18)]),
 (TA + ' Q19 · 3.07', 'For Victorian towns with populations between 2000 and 80 000, a logarithmic transformation was used to linearise the relationship between the number of cafés in a town and the town\'s population. The equation of the least-squares regression line is cafés = −21.4 + 9.6 × log<sub>10</sub>(population).',
  [('a', 'Use this equation to predict the number of cafés in a town with a population of 25 000. Round your answer to the nearest whole number.', 1, 'cafés = −21.4 + 9.6 × log<sub>10</sub>(25 000) = 20.8 → 21 cafés', 12),
   ('b', 'Explain why the equation should not be used to predict the number of cafés in a town with a population of 100.', 1, 'It predicts a negative number of cafés (−2.2), which is impossible; this is an extrapolation well outside the population range of the data.', 14)]),
 (RV + ' Q8 · 3.05', 'The table shows a non-linear relationship between variables x and y:' + T([['x', '1', '2', '3', '4', '5', '6'], ['y', '3', '10', '25', '45', '75', '110']]),
  [('a', 'Complete the transformation of the x-values by completing the table:' + SQ, 1, '', 2),
   ('b', 'Determine the equation of the least-squares regression line for the transformed data set. Give the answer in the form y = a + bx², where a and b are rounded to one decimal place.', 2, 'y = −2.1 + 3.1x²', 14),
   ('c', 'Using technology, determine the value of the correlation coefficient, r, for the transformed data. Round the answer to four decimal places.', 1, 'r = 0.9994', 10)]),
 (RV + ' Q9 · 3.05', 'A data set has been collected, and the scatterplot shows a curved shape:' + T([['x', '0.5', '1.5', '2.5', '3.5', '4.5', '5.5'], ['y', '25.1', '23.2', '19.5', '14.8', '8.3', '1.7']]),
  [('a', f'Use technology to create a scatterplot. Which transformation is most suitable to linearise the data?<div class="mc2" style="grid-template-columns:repeat(4,1fr);margin-top:1mm"><div><b>A</b> {F(1, "x")}</div><div><b>B</b> x²</div><div><b>C</b> log<sub>10</sub>(x)</div><div><b>D</b> log<sub>10</sub>(y)</div></div>', 1, 'B (x²): it gives the highest r² (0.9967; 1/x 0.483, log<sub>10</sub>(x) 0.754, log<sub>10</sub>(y) 0.777).', 8),
   ('b', 'Determine the equation of the least-squares regression line for the transformed data. Give the answer in the form y = a + bx², where a and b are rounded to two decimal places.', 2, 'y = 24.76 − 0.78x²', 14)]),
 (RV + ' Q10 · 3.05', 'Consider the data set, where all y-values are positive:' + T([['x', '1', '2', '3', '5', '8', '10'], ['y', '2.3', '2.8', '3.4', '4.0', '5.2', '5.6']]),
  [('a', 'Transform the data by applying a squared transformation to the y-values. Complete the table, rounding y² values to two decimal places:' + Y2, 1, '', 2),
   ('b', 'Determine the equation of the least-squares regression line for the transformed data. Give the answer in the form y² = a + bx, where a and b are rounded to one decimal place.', 2, 'y² = 2.2 + 3.0x', 14),
   ('c', 'Predict the value of y when x = 7. Round the answer to two decimal places.', 1, 'y² = 2.2 + 3.0 × 7 = 23.2\ny = √23.2 ≈ 4.82', 14),
   ('d', 'Comment on the reliability of this prediction.', 1, 'Reliable: it is an interpolation (x = 7 is within 1 to 10) and the transformed model is strong (r ≈ 0.997).', 12)]),
 (RV + ' Q11 · 3.06', 'For each of the data sets, a scatterplot reveals a non-linear relationship. Apply an appropriate logarithmic or reciprocal transformation to linearise the data:'
  + '<div style="margin:1mm 0 0 4mm"><b>i</b>&nbsp; Based on the shape of the data, identify the most appropriate transformation to apply.<br><b>ii</b>&nbsp; State the coefficient of determination, r², for the transformed data, to four decimal places.<br><b>iii</b> Determine the equation of the least-squares regression line for the transformed data. Round coefficients as specified.</div>',
  [('a', 'A biologist observes that the relationship between the age of a tree (in years) and its height (in metres) is non-linear:' + T([['Age (x)', '1', '2', '5', '10', '20', '30'], ['Height (y)', '0.5', '1.1', '2.0', '2.8', '3.8', '4.5']]), 3,
    'i log<sub>10</sub>(x) (increasing curve that flattens out)\nii r² = 0.9867\niii y = 0.32 + 2.68 log<sub>10</sub>(x)', 26),
   ('b', 'The relationship between the pressure (P in kPa) and volume (V in L) of a gas is non-linear:' + T([['Volume (x)', '1', '2', '4', '5', '8', '10'], ['Pressure (y)', '100', '52', '24', '21', '13', '10']]), 3,
    f'i {F(1, "x")} (decreasing curve that drops sharply then flattens out)\nii r² = 0.9991\niii y = 0.35 + 100.18 × {F(1, "x")}', 26)]),
 (RV + ' Q12 · 3.07', 'The value of a piece of industrial machinery is modelled using a log<sub>10</sub>(y) transformation, where y is the value in dollars and x is the age in years. The least-squares regression line for the transformed data is: log<sub>10</sub>(y) = 4.8 − 0.05x. The original data for the age (x) was collected for machinery aged between 1 and 8 years. The coefficient of determination for this model was r² = 0.96:',
  [('a', 'Predict the value of the machinery (y) when it is 5 years old. Round the answer to the nearest dollar.', 1, 'log<sub>10</sub>(y) = 4.8 − 0.05 × 5 = 4.55\ny = 10<sup>4.55</sup> ≈ $35 481', 16),
   ('b', 'Choose the description which best describes the reliability of this prediction.<div class="mcl" style="margin-top:1mm"><div><b>A</b>Unreliable, as it is an extrapolation.</div><div><b>B</b>Reliable, as it is an interpolation and the model is a strong fit.</div><div><b>C</b>Unreliable, because the r² value is too low.</div><div><b>D</b>Reliable, even though it is an extrapolation, because the correlation is strong.</div></div>', 1, 'B: x = 5 is within 1 to 8 years (interpolation) and r² = 0.96 is a strong fit.', 6)]),
 (RV + ' Q13 · 3.07', 'The table shows data collected on the relationship between the dosage of a medication (in mg) and the reduction in blood pressure (in mmHg). A scatterplot of the data reveals a non-linear relationship:'
  + T([['Dosage (mg), x', '2', '5', '10', '20', '50', '100'], ['Reduction (mmHg), y', '5.0', '12.0', '17.5', '22.8', '30.1', '35.5']]),
  [('a', f'To pick the best model, a researcher tests three transformations: x², log<sub>10</sub>(x), and {F(1, "x")}. Determine the coefficient of determination (r²) for each transformation and identify which one is the most appropriate.', 2,
    f'x²: r² ≈ 0.6057; log<sub>10</sub>(x): r² ≈ 0.99996; {F(1, "x")}: r² ≈ 0.7686\nlog<sub>10</sub>(x) is the most appropriate (highest r²).', 18),
   ('b', 'Using the best transformation from part (a), state the equation of the least-squares regression line. Round coefficients to two decimal places.', 2, 'y = −0.49 + 17.98 log<sub>10</sub>(x)', 12),
   ('c', 'Use the model to predict the reduction in blood pressure for a dosage of 15 mg. Round the answer to one decimal place.', 1, 'y = −0.49 + 17.98 × log<sub>10</sub>(15) ≈ 20.7 mmHg', 12),
   ('d', 'Comment on the reliability of the prediction.', 1, 'Reliable: the model is an extremely strong fit (r² ≈ 1.000) and 15 mg is within 2 to 100 mg (interpolation).', 12)]),
]
def mk(n): return f'{n} mark{"s" if n > 1 else ""}'
def mcbox(n, q):
    les, stem, opts, a = q
    o = ''.join(f'<div><b>{"ABCD"[i]}</b>{x} {"<span class=ok>✓</span>" if i == a else ""}</div>' for i, x in enumerate(opts))
    cls = 'mc2' if max(map(len, opts)) < 25 else 'mcl'
    return f'<div class="box"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><p class="q">{stem}</p><div class="{cls}">{o}</div><div class="cite">{les}</div></div></div>'
def sabox(n, q):
    les, stem, parts = q
    tot = sum(p[2] for p in parts)
    ps = ''
    for lab, txt, m, ans, h in parts:
        head = f'<div class="pq"><b>{lab}</b>{txt} <span class="mk">({mk(m)})</span></div>' if lab else ''
        ps += f'<div class="part">{head}<div class="sp" style="--h:{h}mm"><div class="ans">{ans}</div></div></div>'
    return f'<div class="box"><div class="hd">Question {n}<span>{mk(tot)}</span></div><div class="bd"><p class="q">{stem}</p>{ps}<div class="cite">{les}</div></div></div>'

def page(sol):
    tot = len(MC) + sum(p[2] for q in SA for p in q[2])
    out = [f'<div class="title"><div class="code">Ch 4<br>test</div><h1>Data transformations<div style="font-size:10pt;font-weight:normal;margin-top:1mm">4A–4D · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch4 test' + (' solutions' if sol else '')
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
