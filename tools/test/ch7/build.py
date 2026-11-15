"""Chapter 7 test (7A-7F, recursion: depreciation and interest) + solutions, HTML + PDF in the CFAT 1.x layout. Model: tools/test/ch5/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4, 'Chapter 5 - Depreciation and interest' (Mathspace's numbering),
'Chapter 5 - Topic assessment.pdf' + '5. Depreciation and interest - topicanswerkey.pdf' (02 Sources\\Textbooks\\Mathspace\\Chapter 5 - Depreciation and interest). All 20 items, marks as printed (/39). No figures.
Answers = Mathspace answer key, checked with numpy (Q17c 35 284 - 4291 x age; Q17d -7626 with rounded coefficients, 7087; Q8 6.17%, Q14 5.09%, Q15c 45, Q19 9).
Run: python3 tools/test/ch7/build.py lessons -> 'Ch7 test.html/.pdf' + 'Ch7 test solutions.html/.pdf'
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
TA = 'Mathspace Ch 5 (depreciation and interest) topic assessment'
def R(s):
    import re
    s = re.sub(r'([uVB])_\{?(n\+1|n|0|1|2|3|4)\}?', lambda m: f'<i>{m.group(1)}</i><sub>{m.group(2).replace("n", "<i>n</i>")}</sub>', s)
    return s
MC = [
 (TA + ' Q1 · 5.01', 'Which of these is a correct recurrence relation for a sequence that starts at 400 and decreases by 25 each term?',
  [R('u_0 = 25, u_n+1 = u_n − 400'), R('u_0 = 400, u_n+1 = u_n − 25'), R('u_0 = 400, u_n+1 = u_n + 25'), R('u_0 = 400, u_n+1 = 0.25u_n')], 1),
 (TA + ' Q2 · 5.02', R('For the recurrence relation u_0 = 1000, u_n+1 = 0.8u_n + 50, what is the value of u_2?'), ['850', '810', '690', '730'], 3),
 (TA + ' Q3 · 5.03', R('A car is purchased for $24 000 and depreciates by $3000 per year using flat-rate (simple) depreciation. Which recurrence relation models the value of the car, V_n, after <i>n</i> years?'),
  [R('V_0 = 24 000, V_n+1 = 0.875V_n'), R('V_0 = 3000, V_n+1 = V_n − 24 000'), R('V_0 = 24 000, V_n+1 = V_n − 3000'), R('V_0 = 24 000, V_n+1 = V_n + 3000')], 2),
 (TA + ' Q4 · 5.04', 'A machine worth $50 000 depreciates at 10% per year using reducing balance depreciation. What is its value after 3 years?', ['$40 500', '$45 000', '$35 000', '$36 450'], 3),
 (TA + ' Q5 · 5.06', 'An investment of $5000 earns compound interest at 6% per annum, compounded annually. Which recurrence relation correctly models this?',
  [R('V_0 = 5000, V_n+1 = V_n + 300'), R('V_0 = 5000, V_n+1 = 0.94V_n'), R('V_0 = 5000, V_n+1 = 1.06V_n'), R('V_0 = 5000, V_n+1 = 1.6V_n')], 2),
 (TA + ' Q6 · 5.04', 'A laptop is purchased for $2000 and depreciates at 20% per year using reducing balance depreciation. Which recurrence relation models its value?',
  [R('V_0 = 2000, V_n+1 = 0.8V_n'), R('V_0 = 2000, V_n+1 = 0.2V_n'), R('V_0 = 2000, V_n+1 = 1.2V_n'), R('V_0 = 2000, V_n+1 = V_n − 400')], 0),
 (TA + ' Q7 · 5.06', 'An investment of $10 000 earns compound interest at 4% per annum, compounded quarterly. What is the interest rate per compounding period?', ['2%', '1%', '4%', '0.5%'], 1),
 (TA + ' Q8 · 5.08', 'A nominal interest rate of 6% per annum is compounded monthly. What is the effective annual interest rate, rounded to two decimal places?', ['6.14%', '6.17%', '6.00%', '6.09%'], 1),
 (TA + ' Q9 · 5.05', 'An investment of $6000 earns simple interest at 4% per annum. How much interest is earned after 3 years?', ['$720', '$180', '$240', '$960'], 0),
]
SOLV = T([['Variable', 'Value'], ['N', '36'], ['I%', '4.2'], ['PV', '−12 000'], ['PMT', '0'], ['FV', '13 608.39'], ['P/Y', '12'], ['C/Y', '12']], True)
CAR = T([['Age (years)', 'Value ($)'], ['0', '36 000.00'], ['1', '30 600.00'], ['2', '26 010.00'], ['3', '22 108.50'], ['4', '18 792.23']], True)
STMT = T([['Date', 'Description', 'Amount ($)', 'Balance ($)'], ['1 Jul', 'Opening deposit', '8000.00', '8000.00'], ['31 Jul', 'Interest', '26.67', '8026.67'], ['31 Aug', 'Interest', '26.76', '8053.43'], ['30 Sep', 'Interest', '26.84', '8080.27']], True)
SA = [
 (TA + ' Q10 · 5.01', 'Write a recurrence relation to model a sequence that starts at 750, and each term is found by multiplying the previous term by 0.95 and then adding 40.',
  [('', '', 1, R('u_0 = 750, u_n+1 = 0.95u_n + 40'), 14)]),
 (TA + ' Q11 · 5.02', R('For the recurrence relation u_0 = 600, u_n+1 = 1.06u_n − 25, calculate the values of u_1, u_2, and u_3, rounded to two decimal places.'),
  [('', '', 2, R('u_1 = 611.00, u_2 = 622.66, u_3 = 635.02'), 20)]),
 (TA + ' Q12 · 5.04', 'A piece of equipment worth $18 000 depreciates at 15% per year using reducing balance depreciation. Write a recurrence relation to model its value and calculate its value after 4 years, to the nearest dollar.',
  [('', '', 2, R('V_0 = 18 000, V_n+1 = 0.85V_n; V_4 = $9396'), 20)]),
 (TA + ' Q13 · 5.05', R('A savings account pays simple interest. The value of the account is modelled by V_n = 4000 + 180<i>n</i>, where V_n is the value in dollars after <i>n</i> years. Calculate the annual simple interest rate as a percentage.'),
  [('', '', 1, '4.5% per annum', 14)]),
 (TA + ' Q14 · 5.08', 'A nominal interest rate of 5% per annum is compounded quarterly. Calculate the effective annual interest rate, rounded to two decimal places.',
  [('', '', 2, '<i>r</i><sub>eff</sub> = 5.09%', 18)]),
 (TA + ' Q15 · 5.07', 'Mia invested $12 000 in a term deposit. She used the finance solver on her calculator to find the value of the investment at the end of the term. The solver screen is shown below.' + SOLV,
  [('a', 'State how often interest is compounded and the length of the term in years.', 1, 'Interest is compounded monthly and the term is 3 years.', 12),
   ('b', 'Determine the total interest Mia earns over the term.', 1, '$1608.39', 12),
   ('c', 'Mia wants the value of her investment to be more than $14 000. At the same interest rate, determine the minimum number of whole months the investment must stay in the account.', 2, '45 months', 18)]),
 (TA + ' Q16 · 5.03', 'A courier company buys a delivery van for $52 000. The van is depreciated using unit cost depreciation at a rate of $0.24 per kilometre travelled. The van travels 35 000 km each year.',
  [('a', 'Calculate the depreciation of the van in one year.', 1, '$8400', 12),
   ('b', R('Write a recurrence relation for V_n, the value of the van in dollars after <i>n</i> years.'), 1, R('V_0 = 52 000, V_n+1 = V_n − 8400'), 12),
   ('c', 'The company sells the van as soon as its value falls below $12 000. Determine after how many years the van is sold.', 1, '5 years', 14)]),
 (TA + ' Q17 · 5.04', 'A family in Ballarat bought a new car. The table shows the value of the car, in dollars, at each age of the car, in years.' + CAR,
  [('a', 'Show that the car is depreciating by reducing balance depreciation, and state the annual rate of depreciation.', 1, 'Each value is 0.85 times the previous value (a constant ratio), so the rate is 15% per year.', 16),
   ('b', R('Write a recurrence relation for V_n, the value of the car in dollars after <i>n</i> years.'), 1, R('V_0 = 36 000, V_n+1 = 0.85V_n'), 12),
   ('c', 'A financial planner fits a least squares regression line to the data in the table, with age as the explanatory variable. Use technology to find the equation of this line, with its coefficients rounded to the nearest whole number.', 1, 'value = 35 284 − 4291 × age', 12),
   ('d', 'Use the regression line from part c and the recurrence relation from part b to predict the value of the car when it is 10 years old. Give both values to the nearest dollar.', 1, 'Regression line: −$7626. Recurrence relation: $7087.', 16),
   ('e', 'Which of the two predictions is more reasonable? Give a reason based on the data and the predictions.', 2, 'The recurrence relation prediction of $7087. The regression line gives a negative value, which is impossible, and the data fall by a constant percentage, not a constant amount, so a linear model does not suit them.', 20)]),
 (TA + ' Q18 · 5.08', 'Sam opened a savings account with $8000 on 1 July. Interest is compounded monthly, and Sam makes no further deposits or withdrawals. Part of his account statement is shown below.' + STMT,
  [('a', 'Determine the annual interest rate for this account.', 1, '4% per annum', 12),
   ('b', R('Write a recurrence relation for B_n, the balance of the account in dollars after <i>n</i> months.'), 1, R('B_0 = 8000, B_n+1 = (1 + 0.04/12) B_n'), 12),
   ('c', 'Determine the balance of the account after 12 months, to the nearest cent.', 1, '$8325.93', 12),
   ('d', 'Calculate the effective annual interest rate for this account, rounded to two decimal places.', 1, '4.07%', 12),
   ('e', 'Another bank offers Sam an account paying 4.05% per annum, compounding annually. Should Sam move his money to the other bank? Give a reason.', 2, 'No. His current account has an effective annual rate of 4.07%, which is higher than the 4.05% effective rate of the other account (annual compounding), so Sam earns more by staying.', 20)]),
 (TA + ' Q19 · 5.07', R('A recurrence relation is given by V_0 = 25 000, V_n+1 = 1.06V_n. Using technology, determine after how many full years the investment will first exceed $40 000.'),
  [('', '', 2, '9 years', 18)]),
 (TA + ' Q20 · 5.05', 'A loan of $7200 charges simple interest. The total interest paid after 4 years is $1296. Determine the annual simple interest rate as a percentage.',
  [('', '', 1, '4.5% per annum', 14)]),
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
    out = [f'<div class="title"><div class="code">Ch 7<br>test</div><h1>Modelling growth and decay using recursion<div style="font-size:10pt;font-weight:normal;margin-top:1mm">7A–7F · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch7 test' + (' solutions' if sol else '')
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
