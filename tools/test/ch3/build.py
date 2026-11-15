"""Chapter 3 test (3A-3C) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css). Model: tools/test/ch2/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4, Chapter 3 - Model linear associations, 'Chapter 3 - Topic assessment.pdf' + answer key
(02 Sources\\Textbooks\\Mathspace\\Chapter 3 - Model linear associations). Kept 3.01-3.04 items: MC 1, 2, 5, 7, 8; SA 9-16, 20 (renumbered).
Left out for the Ch 4 test (transformations 3.05-3.07): MC 3, 4, 6; SA 17, 18, 19. Q15b residual plot redrawn from the same points.
Answers checked with numpy (Q10 -45.84 + 4.04x; Q16 r = 0.986, 39.92 + 2.60x, residual 0.9; Q15 residuals 1.93, -0.21, -1.55, -1.69, -0.63, 2.23).
Run: python3 tools/test/ch3/build.py lessons -> 'Ch3 test.html/.pdf' + 'Ch3 test solutions.html/.pdf'
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
.secthd{font-weight:bold;border-bottom:2px solid #000;margin:2mm 0;display:flex;justify-content:space-between}
"""
E = html.escape
SRC = 'Mathspace Ch 3 topic assessment'
def RPLOT():
    W,H,L,B=230,150,34,124
    X=lambda w:L+w*12.5; Y=lambda r:70-r*17
    g=''.join(f'<line x1="{X(w)}" y1="{Y(3)}" x2="{X(w)}" y2="{Y(-3)}" stroke="#ddd"/>' for w in range(0,15,2))
    g+=''.join(f'<line x1="{X(0)}" y1="{Y(r)}" x2="{X(14)}" y2="{Y(r)}" stroke="#ddd"/><text x="{X(0)-5}" y="{Y(r)+3}" font-size="9" text-anchor="end">{str(r).replace("-","−")}</text>' for r in range(-3,4))
    g+=''.join(f'<text x="{X(w)}" y="{Y(-3)+11}" font-size="9" text-anchor="middle">{w}</text>' for w in range(0,15,2))
    g+=f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(14)}" y2="{Y(0)}" stroke="#000" stroke-dasharray="4 3"/><line x1="{X(0)}" y1="{Y(3)}" x2="{X(0)}" y2="{Y(-3)}" stroke="#000"/><line x1="{X(0)}" y1="{Y(-3)}" x2="{X(14)}" y2="{Y(-3)}" stroke="#000"/>'
    g+=''.join(f'<rect x="{X(w)-3}" y="{Y(r)-3}" width="6" height="6" transform="rotate(45 {X(w)} {Y(r)})" fill="#000"/>' for w,r in [(2,1.93),(4,-0.21),(6,-1.55),(10,-0.63),(12,2.23)])
    g+=f'<text x="{X(7)}" y="{Y(-3)+23}" font-size="10" text-anchor="middle">Week</text><text x="10" y="{Y(0)}" font-size="10" transform="rotate(-90 10 {Y(0)})" text-anchor="middle">Residual</text>'
    return f'<div style="text-align:center"><svg width="{W}" height="{H+15}" viewBox="0 0 {W} {H+15}">{g}</svg></div>'
def T(rows, head=True):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{E(c)}</th>' if (head and i == 0) else f'<td>{E(c)}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
MC = [
 ('3.01', 'The least-squares regression line for a data set is y = 3.2x + 7.5. What is the gradient of this line?', ['7.5', '3.2', '−3.2', '10.7'], 1),
 ('3.03', 'A residual value is calculated as:', ['predicted value ÷ actual value', 'actual value ÷ predicted value', 'predicted value − actual value', 'actual value − predicted value'], 3),
 ('3.01', 'The means of a data set are x̄ = 5 and ȳ = 14. The standard deviations are sₓ = 2 and s_y = 6, and the correlation coefficient is r = 0.9. Using the formula b = r × s_y ÷ sₓ, the gradient of the least-squares regression line is:', ['0.3', '1.8', '2.7', '0.6'], 2),
 ('3.02', 'A least-squares regression line was fitted to data on the height and age of eucalyptus saplings aged from 3 to 12 years. Using this line to predict the height of a sapling of which age would be an extrapolation?', ['3.5 years', '7 years', '11.5 years', '15 years'], 3),
 ('3.03', 'The residual plot for a least-squares regression line shows a clear curved pattern. Which of the following conclusions is most appropriate?', ['The linear model is appropriate because the residuals are both positive and negative', 'The association is non-linear, so a linear model is not appropriate', 'The association is linear, but the correlation is weak', 'The data must contain an outlier'], 1),
]
SA = [
 ('3.02', 'The least-squares regression line for a data set is Weight = 3.8 × Age + 12.5, where weight is in kilograms and age is in months. Interpret the gradient and the y-intercept in the context of this model.',
  [('', '', 2, 'The gradient of 3.8 means that for each additional month of age, the weight is predicted to increase by 3.8 kg. The y-intercept of 12.5 means that at birth (age 0 months), the predicted weight is 12.5 kg.', 22)]),
 ('3.01', 'The following data was collected on the temperature (°C) and the number of ice creams sold at a Sydney beach kiosk.'
  + T([['Temperature (°C)', '22', '25', '28', '30', '33', '35'], ['Ice creams sold', '45', '52', '68', '74', '89', '95']], head=False)
  + 'Use technology to determine the equation of the least-squares regression line for ice creams sold (y) in terms of temperature (x). Round values to two decimal places.',
  [('', '', 2, 'y = −45.84 + 4.04x', 14)]),
 ('3.03', 'A regression line y = 5.6x + 22.3 is fitted to data. Calculate the residual for the data point (4, 43).',
  [('', '', 2, 'Predicted y = 5.6 × 4 + 22.3 = 44.7\nResidual = 43 − 44.7 = −1.7', 14)]),
 ('3.02', 'For adults at a Bendigo gym, resting heart rate, in beats per minute, can be predicted from the number of hours of exercise per week using the equation heart rate = 78.4 − 0.65 × hours. Predict the resting heart rate of an adult who exercises for 14 hours per week.',
  [('', '', 1, '78.4 − 0.65 × 14 = 69.3 beats per minute', 10)]),
 ('3.01', 'For a bivariate data set, x̄ = 12 and ȳ = 40. The least-squares regression line y = a + bx has a gradient of b = 2.5. Calculate the value of a.',
  [('', '', 1, 'a = ȳ − b x̄ = 40 − 2.5 × 12 = 10', 10)]),
 ('3.02', 'A least-squares regression line was fitted to data on the age, in years, and the price, in dollars, of used hatchbacks advertised in Melbourne. Age is the explanatory variable. The CAS output is shown below, where the line has the form y = a + bx.'
  + T([['a', '27 850'], ['b', '−2140'], ['r²', '0.8836'], ['r', '−0.94']], head=False),
  [('a', 'Write the equation of the least-squares regression line in terms of the variables price and age.', 1, 'price = 27 850 − 2140 × age', 8),
   ('b', 'Interpret the gradient of the line in the context of this data.', 1, 'On average, the price of a used hatchback decreases by $2140 for each additional year of age.', 12),
   ('c', 'Interpret the coefficient of determination in the context of this data.', 1, '88.36% of the variation in price can be explained by the variation in age.', 12),
   ('d', 'Predict the price of a 4-year-old hatchback.', 1, '27 850 − 2140 × 4 = $19 290', 9)]),
 ('3.03', 'The height of a tomato seedling, in centimetres, was recorded every two weeks after planting. The data are shown below.'
  + T([['Week', '2', '4', '6', '8', '10', '12'], ['Height (cm)', '9.4', '10.1', '11.6', '14.3', '18.2', '23.9']], head=False)
  + 'The least-squares regression line is height = 4.63 + 1.42 × week, with r² = 0.908.',
  [('a', 'Calculate the residual for week 8.', 1, 'Predicted = 4.63 + 1.42 × 8 = 15.99\nResidual = 14.3 − 15.99 = −1.69', 12),
   ('b', 'The residual plot, with the point for week 8 not yet plotted, is shown below. With reference to the residual plot, comment on whether a linear model is appropriate for this data.', 2,
    'A linear model is not appropriate. The residuals form a clear curved (U-shaped) pattern, so the association is non-linear, even though the coefficient of determination is high.', 18)]),
 ('3.04', 'The average number of hours spent studying each week and the final score out of 100 were recorded for 10 Year 12 students. The data are shown below.'
  + T([['Study (hours)', '3', '5', '6', '8', '9', '10', '12', '14', '15', '18'], ['Score', '48', '55', '52', '61', '66', '63', '72', '75', '81', '86']], head=False),
  [('a', "Use technology to determine the value of Pearson's correlation coefficient, r, rounded to three decimal places, and describe the strength and direction of the association.", 1, 'r = 0.986, strong and positive', 10),
   ('b', 'Use technology to find the equation of the least-squares regression line that can be used to predict score from study hours. Write the values rounded to two decimal places.', 2, 'score = 39.92 + 2.60 × study hours', 12),
   ('c', 'Interpret the gradient of the regression line in the context of this data.', 1, 'On average, the final score increases by 2.60 for each additional hour of study per week.', 12),
   ('d', 'Using your equation from part b, calculate the residual for the student who studied for 12 hours, rounded to one decimal place.', 1, 'Predicted = 39.92 + 2.60 × 12 = 71.12\nResidual = 72 − 71.12 = 0.9', 12),
   ('e', 'Determine whether the equation can reliably predict the score of a student who studies for 30 hours per week. Justify your answer.', 1, 'No. This is an extrapolation well beyond the data (3 to 18 hours) and it predicts a score above 100, which is not possible.', 14)]),
 ('3.04', "A full regression analysis was carried out on the age, in years, and the annual maintenance cost, in dollars, of 12 ride-on mowers at a Geelong council depot. The mowers were aged from 1 to 9 years. The least-squares regression line is cost = 180 + 95 × age, Pearson's correlation coefficient is r = 0.96 and the residual plot shows no clear pattern. Predict the annual maintenance cost of a 6-year-old mower and state whether this prediction is reliable. Give a reason for your answer.",
  [('', '', 2, '180 + 95 × 6 = $750. The prediction is reliable: it is an interpolation (within 1 to 9 years), the association is strong and linear and the residual plot supports a linear model.', 22)]),
]

def mk(n): return f'{n} mark{"s" if n > 1 else ""}'
def mcbox(n, q):
    les, stem, opts, a = q
    o = ''.join(f'<div><b>{"ABCD"[i]}</b>{E(x)} {"<span class=ok>✓</span>" if i == a else ""}</div>' for i, x in enumerate(opts))
    cls = 'mc2' if max(map(len, opts)) < 25 else 'mcl'
    return f'<div class="box"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><p class="q">{E(stem)}</p><div class="{cls}">{o}</div><div class="cite">{SRC} · {les}</div></div></div>'
def sabox(n, q):
    les, stem, parts = q
    tot = sum(p[2] for p in parts)
    ps = ''
    for lab, txt, m, ans, h in parts:
        head = f'<div class="pq"><b>{lab}</b>{E(txt)} <span class="mk">({mk(m)})</span></div>' if lab else ''
        if lab == 'b' and 'residual plot' in txt: head += RPLOT()
        ps += f'<div class="part">{head}<div class="sp" style="--h:{h}mm"><div class="ans">{ans}</div></div></div>'
    return f'<div class="box"><div class="hd">Question {n}<span>{mk(tot)}</span></div><div class="bd"><p class="q">{stem}</p>{ps}<div class="cite">{SRC} · {les}</div></div></div>'

def page(sol):
    tot = len(MC) + sum(p[2] for q in SA for p in q[2])
    out = [f'<div class="title"><div class="code">Ch 3<br>test</div><h1>Fitting a linear model to numerical data<div style="font-size:10pt;font-weight:normal;margin-top:1mm">3A–3C · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch3 test' + (' solutions' if sol else '')
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
