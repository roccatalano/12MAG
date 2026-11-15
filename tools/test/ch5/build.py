"""Chapter 5 test (5A-5E, time series) + solutions, HTML + PDF in the CFAT 1.x layout (tools/cfat/ch2/cfat.css). Model: tools/test/ch4/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4, 'Chapter 4 - Time series data' (Mathspace's numbering),
'Chapter 4 - Topic assessment.pdf' + answer key (02 Sources\\Textbooks\\Mathspace\\Chapter 4 - Time series data). All 20 items, marks as printed (/47).
Q9 and Q13 graphs cropped from the PDF (q9.png, q13.png). Answers = Mathspace answer key, checked with numpy
(Q16 8.39 + 2.69t, 2027 = 37.99; Q20 seasonal indices sum 12, Year 2 deseasonalised regression 44.26 + 0.05t, Mar Y3 45.61 with rounded b; all others by hand).
Run: python3 tools/test/ch5/build.py lessons -> 'Ch5 test.html/.pdf' + 'Ch5 test solutions.html/.pdf'
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
import base64
def IMG(f, w=150): return f'<img src="data:image/png;base64,{base64.b64encode(open(os.path.join(HERE, f), "rb").read()).decode()}" style="width:{w}mm;display:block;margin:1mm 0">'
def T(rows, head=False):
    return '<table class="t">' + ''.join('<tr>' + ''.join((f'<th>{c}</th>' if (head and i == 0) else f'<td>{c}</td>') for c in r) + '</tr>' for i, r in enumerate(rows)) + '</table>'
TA = 'Mathspace Ch 4 (time series) topic assessment'
MC = [
 (TA + ' Q1 · 4.01', 'A time series graph shows sales data that rises steadily over several years, with regular peaks each December and troughs each June. Which components of a time series are present?',
  ['Seasonality and irregular fluctuations only', 'Trend, seasonality, and irregular fluctuations', 'Trend and seasonality only', 'Trend and irregular fluctuations only'], 2),
 (TA + ' Q2 · 4.02', 'A time series of monthly café revenue shows a sudden, sharp spike in April due to a one-off food festival held near the café. In all other months the revenue follows its usual pattern. This spike is best described as:',
  ['A structural change', 'A seasonal variation', 'An upward trend', 'An outlier'], 3),
 (TA + ' Q3 · 4.03', 'The data below shows the number of visitors to a museum over 5 consecutive months: 120, 135, 128, 142, 131. What is the 3-point moving mean for Month 3?',
  ['128.33', '135.00', '127.67', '133.67'], 1),
 (TA + ' Q4 · 4.04', 'The following data values are recorded over 7 time periods: 10, 14, 9, 16, 11, 18, 13. What is the 5-point median smooth value for Time Period 3?',
  ['11', '14', '9', '12'], 0),
 (TA + ' Q5 · 4.05', 'The seasonal indices for four quarters of a year are: Q1 1.20, Q2 0.85, Q3 0.75, Q4 <i>X</i>. What is the value of <i>X</i>?',
  ['1.00', '1.10', '1.20', '0.80'], 2),
 (TA + ' Q6 · 4.07', 'A least-squares regression line fitted to deseasonalised quarterly sales data is deseasonalised sales = 520 + 12<i>t</i>, where <i>t</i> = 1 represents Quarter 1 of 2024. The seasonal index for Quarter 3 is 0.8. The predicted actual sales for Quarter 3 of 2026 are:',
  ['521.6', '531.2', '652', '815'], 0),
 (TA + ' Q7 · 4.03', 'The values of a time series for the first five months are 20, 26, 31, 23, 28. The 4-point moving mean with centring for month 3 is:',
  ['25', '25.6', '26', '27'], 2),
 (TA + ' Q8 · 4.06', 'The seasonal index for summer sales at a surf shop is 1.25. To deseasonalise a summer sales figure, the actual sales should be:',
  ['increased by 25%', 'decreased by 25%', 'decreased by 20%', 'increased by 20%'], 2),
]
SA = [
 (TA + ' Q9 · 4.01', 'This time series graph shows the monthly number of new home loan approvals (in thousands) in a major Australian city over two years:' + IMG('q9.png') + 'Describe the trend and seasonal pattern visible in the graph.',
  [('', '', 2, 'The overall trend is increasing over the two-year period. There is a clear seasonal pattern with a cycle of approximately 12 months, with peaks around months 3 and 15, and troughs around months 7 and 19.', 22)]),
 (TA + ' Q10 · 4.04', 'Apply a 3-point median smooth to the following data and state the smoothed values for Time Periods 2, 3, 4, and 5:'
  + T([['Time period', '1', '2', '3', '4', '5', '6', '7'], ['Value', '14', '22', '11', '28', '17', '35', '20']]),
  [('', '', 2, 'Period 2: 14, Period 3: 22, Period 4: 17, Period 5: 28.', 22)]),
 (TA + ' Q11 · 4.06', 'The seasonal indices for the four quarters of a year are given below. The actual sales for Q2 were 3600 units.'
  + T([['Quarter', 'Q1', 'Q2', 'Q3', 'Q4'], ['Seasonal index', '1.25', '0.90', '0.75', '1.10']]) + 'Calculate the deseasonalised sales for Q2.',
  [('', '', 1, '3600 ÷ 0.90 = 4000 units.', 14)]),
 (TA + ' Q12 · 4.05', 'The seasonal indices for three of the four seasons at a ski resort are: Summer 0.55, Autumn 0.80, Winter 1.95. Calculate the seasonal index for Spring.',
  [('', '', 1, '4 − (0.55 + 0.80 + 1.95) = 0.70', 14)]),
 (TA + ' Q13 · 4.02', 'This time series graph shows the weekly number of deliveries made by a courier company. Identify whether the unusual data point at Week 8 is an outlier or a structural change, and justify your answer.' + IMG('q13.png'),
  [('', '', 2, 'The data point at Week 8 is an outlier. After the spike, the data returns to its previous pattern of approximately 200 deliveries per week. A structural change would result in the data settling at a new level permanently.', 22)]),
 (TA + ' Q14 · 4.05', 'The number of visitors to a wildlife park on Phillip Island in each quarter of 2025 is shown below.'
  + T([['Quarter', '1', '2', '3', '4'], ['Visitors', '5400', '3000', '2400', '4200']]),
  [('a', 'Calculate the seasonal index for Quarter 1.', 2, 'Quarterly mean = (5400 + 3000 + 2400 + 4200) ÷ 4 = 3750\nSI = 5400 ÷ 3750 = 1.44', 20),
   ('b', 'The seasonal index for Quarter 3 is 0.64. Interpret this seasonal index in the context of this data.', 1, 'The number of visitors in Quarter 3 is typically 36% below the quarterly average.', 14),
   ('c', 'In Quarter 3 of 2026, the park had 2720 visitors. Calculate the deseasonalised number of visitors for this quarter.', 1, '2720 ÷ 0.64 = 4250', 14)]),
 (TA + ' Q15 · 4.07', 'A Melbourne retailer fitted a least-squares regression line of the form <i>y</i> = <i>a</i> + <i>bt</i> to its deseasonalised monthly bicycle sales, where <i>t</i> = 1 represents January 2024. The CAS output is shown below.'
  + T([['<i>a</i>', '1286.4'], ['<i>b</i>', '14.62'], ['<i>r</i><sup>2</sup>', '0.8123']]),
  [('a', 'Interpret the value of <i>b</i> in the context of this data.', 1, 'On average, deseasonalised bicycle sales increase by 14.62 bicycles per month.', 14),
   ('b', 'Predict the deseasonalised sales for December 2026.', 1, 't = 36: 1286.4 + 14.62 × 36 = 1812.72 bicycles', 14),
   ('c', 'The seasonal index for December is 1.18. Predict the actual number of bicycles sold in December 2026, rounded to the nearest whole number.', 1, '1812.72 × 1.18 = 2139.0 → 2139 bicycles', 14)]),
 (TA + ' Q16 · 4.07', 'The number of electric vehicles registered each year in a regional Victorian city, in hundreds, is shown below.'
  + T([['Year', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'], ['<i>t</i>', '1', '2', '3', '4', '5', '6', '7', '8'], ['Registrations (hundreds)', '12', '15', '14', '19', '23', '22', '28', '31']]),
  [('a', 'Calculate the 3-point moving mean for 2019.', 1, '(15 + 14 + 19) ÷ 3 = 16 hundred', 12),
   ('b', 'Use technology to find the equation of the least-squares regression line for registrations, in hundreds, against <i>t</i>. Write the values rounded to two decimal places.', 2, 'registrations = 8.39 + 2.69t', 14),
   ('c', 'Interpret the gradient of the regression line in the context of this data.', 1, 'On average, electric vehicle registrations increase by 269 each year.', 12),
   ('d', 'Use your equation to predict the number of registrations, in hundreds, in 2027, rounded to one decimal place.', 1, 't = 11: 8.39 + 2.69 × 11 = 37.98 → 38.0 hundred', 12),
   ('e', 'Comment on the reliability of the prediction for 2027.', 1, 'It is of limited reliability. It is an extrapolation 3 years beyond the data and assumes the trend continues unchanged.', 14)]),
 (TA + ' Q17 · 4.06', 'The number of guests, in hundreds, staying at a caravan park at Lakes Entrance each quarter for two years is shown below, with the seasonal index for each quarter.'
  + T([['Quarter', 'Year 1', 'Year 2', 'Seasonal index'], ['1', '85', '92', '1.42'], ['2', '47', '50', '0.78'], ['3', '37', '40', '0.60'], ['4', '71', '77', '<i>k</i>']], True),
  [('a', 'Calculate the value of <i>k</i>.', 1, 'k = 4 − (1.42 + 0.78 + 0.60) = 1.20', 12),
   ('b', 'Calculate the deseasonalised number of guests, in hundreds, for Quarter 3 of Year 2, rounded to two decimal places.', 1, '40 ÷ 0.60 = 66.67 hundred', 12),
   ('c', "The manager claims that Quarter 1 of Year 2 was the park's best performing quarter that year. Use deseasonalised figures for Quarters 1 and 3 of Year 2 to comment on this claim.", 2, 'The claim is not supported. The deseasonalised figure for Quarter 1 is 92 ÷ 1.42 = 64.79 hundred, which is lower than 66.67 hundred for Quarter 3, so once seasonal effects are removed, Quarter 3 performed better.', 20),
   ('d', 'A least-squares regression line fitted to the deseasonalised data is deseasonalised guests = 58.56 + 0.89<i>t</i>, where <i>t</i> = 1 represents Quarter 1 of Year 1. Predict the actual number of guests for Quarter 4 of Year 3, rounded to the nearest whole number of guests.', 2, 't = 12: 58.56 + 0.89 × 12 = 69.24 hundred (deseasonalised)\nActual = 69.24 × 1.20 = 83.088 hundred → 8309 guests', 20)]),
 (TA + ' Q18 · 4.03', 'The 5-point moving means for a time series are: 24.2, 25.6, 27.0, 28.4, 29.8 for Time Periods 3 through 7. Describe what the moving means reveal about the underlying trend of the data.',
  [('', '', 1, 'The moving means are increasing by a constant amount of 1.4 each period, indicating a steady upward linear trend in the underlying data.', 14)]),
 (TA + ' Q19 · 4.07', 'The regression equation <i>y</i> = 95.4 + 2.1<i>t</i> is fitted to deseasonalised data, where <i>t</i> = 1 represents the first time period. Calculate the predicted deseasonalised value for <i>t</i> = 20. Round to two decimal places.',
  [('', '', 1, '95.4 + 2.1 × 20 = 137.40', 12)]),
 (TA + ' Q20 · 4.06', 'A regional airline tracks the number of passengers (in hundreds) on its Sydney-Canberra route each month. The data for two years and the corresponding seasonal indices are given below:'
  + T([['Month', 'Year 1 passengers', 'Year 2 passengers', 'Seasonal index']] + [r.split() for r in ['Jan 48 54 1.20', 'Feb 44 50 1.15', 'Mar 40 46 1.00', 'Apr 36 42 0.95', 'May 32 38 0.85', 'Jun 28 34 0.70', 'Jul 30 36 0.80', 'Aug 34 40 0.90', 'Sep 38 44 0.95', 'Oct 42 48 1.05', 'Nov 46 52 1.15', 'Dec 52 58 1.30']], True),
  [('a', 'Deseasonalise the Year 2 data for January, June, and December. Round to two decimal places.', 2, 'January: 54 ÷ 1.20 = 45.00, June: 34 ÷ 0.70 = 48.57, December: 58 ÷ 1.30 = 44.62 hundred passengers.', 16),
   ('b', 'Using a CAS calculator, deseasonalise all Year 2 data and fit a least-squares regression line to the deseasonalised Year 2 values, where <i>t</i> = 13 represents January of Year 2. Give the equation in the form <i>y</i> = <i>a</i> + <i>bt</i>, rounding to two decimal places.', 3, 'y = 44.26 + 0.05t', 20),
   ('c', 'Use the regression equation to predict the deseasonalised number of passengers for March of Year 3 (Month 27). Round to two decimal places.', 1, '44.26 + 0.05 × 27 = 45.61 hundred passengers', 12),
   ('d', 'Reseasonalise the forecast for March of Year 3 to obtain the actual predicted number of passengers. Round to the nearest whole number.', 2, '45.61 × 1.00 = 45.61 → 46 hundred passengers', 14),
   ('e', 'Evaluate the reliability of the prediction for March of Year 3, referring specifically to how far the forecast extends beyond the available data.', 2, "The prediction for March of Year 3 is reasonably reliable. It is only 3 months beyond the last data point (December of Year 2), which is well within one seasonal cycle (12 months). This short-term extrapolation is generally considered reliable, provided no major structural changes occur in the airline's operations or passenger demand.", 22)]),
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
    out = [f'<div class="title"><div class="code">Ch 5<br>test</div><h1>Investigating and modelling time series data<div style="font-size:10pt;font-weight:normal;margin-top:1mm">5A–5E · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch5 test' + (' solutions' if sol else '')
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
