"""Chapter 8 test (8A-8I, reducing balance loans, annuities and investments) + solutions, HTML + PDF in the CFAT 1.x layout. Model: tools/test/ch7/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4, 'Chapter 6 - Loans and investments' (Mathspace's numbering),
'Chapter 6 - Topic assessment.pdf' + 'Chapter 6 - Topic assessment answer key.pdf' (02 Sources\\Textbooks\\Mathspace\\Chapter 6 - Loans and investments). All 20 items, marks as printed (/40). No figures.
Answers = Mathspace answer key. PV/PMT in the PDF are printed 'P V', 'P M T' (spacing only, joined here).
Run: python3 tools/test/ch8/build.py lessons -> 'Ch8 test.html/.pdf' + 'Ch8 test solutions.html/.pdf'
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
TA = 'Mathspace Ch 6 (loans and investments) topic assessment'
def R(s):
    import re
    s = re.sub(r'([uVB])_\{?(n\+1|n|0|1|2|3|4)\}?', lambda m: f'<i>{m.group(1)}</i><sub>{m.group(2).replace("n", "<i>n</i>")}</sub>', s)
    return s

MC = [
 (TA + ' Q1 · 6.01', 'A reducing balance loan of $20 000 charges interest at 6% per annum, compounded monthly. The monthly interest charged in the first month is closest to:', ['$120.00', '$83.33', '$100.00', '$1200.00'], 2),
 (TA + ' Q2 · 6.01', 'A loan of $15 000 is taken out at 8.4% per annum, compounded monthly. The monthly repayment is $350. The balance after the first repayment is:', ['$14 752.55', '$14 650.00', '$14 755.00', '$15 910.00'], 2),
 (TA + ' Q3 · 6.02', 'A home loan of $480 000 is taken at 5.4% per annum, compounded monthly, with monthly repayments of $2900. Using a financial solver, the number of months to repay the loan is closest to:', ['264', '300', '240', '288'], 1),
 (TA + ' Q4 · 6.03', 'Two loans of $30 000 are offered. Loan P charges 7.2% per annum compounded monthly with monthly repayments of $600. Loan Q charges 6.6% per annum compounded fortnightly with fortnightly repayments of $280. Which statement is correct?',
  ['Loan P has a shorter loan term.', 'Loan Q has a lower total repayment amount.', 'Both loans have the same total repayment amount.', 'Loan P has a lower total repayment amount.'], 1),
 (TA + ' Q5 · 6.04', 'An annuity of $200 000 earns 5% per annum compounded annually. Annual withdrawals of $15 000 are made. The balance after the first withdrawal is:', ['$196 000', '$185 000', '$194 250', '$195 000'], 3),
 (TA + ' Q6 · 6.04', 'An annuity of $200 000 earns 5% per annum compounded annually. Annual withdrawals of $15 000 are made. The balance after the first withdrawal is $195 000. The interest earned in the second year is:', ['$10 000', '$9750', '$10 250', '$9500'], 1),
 (TA + ' Q7 · 6.02', "A reducing balance loan has a principal of $50 000, an interest rate of 9% per annum compounded monthly, and monthly repayments of $1000. From the borrower's perspective, the correct sign convention in a financial solver for <i>PV</i> and <i>PMT</i> is:",
  ['<i>PV</i> is negative, <i>PMT</i> is positive.', '<i>PV</i> is positive, <i>PMT</i> is negative.', 'Both <i>PV</i> and <i>PMT</i> are positive.', 'Both <i>PV</i> and <i>PMT</i> are negative.'], 1),
 (TA + ' Q8 · 6.07', 'An investor deposits $800 per month into an account earning 4.8% per annum compounded monthly, starting with no initial balance. After 5 years, the balance is closest to:', ['$53 891', '$54 128', '$48 000', '$55 000'], 1),
 (TA + ' Q9 · 6.05', 'Two annuities each start with $150 000. Annuity X earns 5% per annum compounded annually with annual withdrawals of $12 000. Annuity Y earns 5% per annum compounded monthly with monthly withdrawals of $1000. Which annuity lasts longer?',
  ['Annuity Y lasts longer.', 'Both annuities last the same length of time.', 'Neither annuity will ever be depleted.', 'Annuity X lasts longer.'], 3),
]
SOLV = T([['Variable', 'Value'], ['N', '205.655'], ['I%', '4.8'], ['PV', '−420 000'], ['PMT', '3000'], ['FV', '0'], ['P/Y', '12'], ['C/Y', '12']], True)
AMORT = T([['Repayment number', 'Repayment ($)', 'Interest ($)', 'Principal reduction ($)', 'Balance ($)'], ['0', '0.00', '0.00', '0.00', '520 000.00'],
           ['1', '3400.00', '2652.00', '748.00', '519 252.00'], ['2', '3400.00', '<i>a</i>', '751.81', '<i>b</i>'], ['3', '3400.00', '2644.35', '755.65', '517 744.54']], True)
SA = [
 (TA + ' Q10 · 6.01', R('A reducing balance loan of $12 000 charges interest at 9% per annum, compounded monthly. The monthly repayment is $380.<br>Using the recurrence relation V_n+1 = 1.0075 × V_n − 380, calculate the balance of the loan after the first two repayments.'),
  [('', '', 2, 'After first repayment: $11 710.00. After second repayment: $11 417.83.', 16)]),
 (TA + ' Q11 · 6.02', 'A loan of $35 000 is taken at 6.6% per annum compounded monthly. Monthly repayments of $700 are made. Use a financial solver to determine how many full months it takes to repay the loan.',
  [('', '', 2, '59 months (the loan is fully repaid in month 59, with a smaller final repayment).', 16)]),
 (TA + ' Q12 · 6.04', 'An annuity of $180 000 earns 4.5% per annum compounded annually. Annual withdrawals of $13 500 are made at the end of each year.<br>Using the recurrence relation <i>A</i><sub><i>n</i>+1</sub> = 1.045 × <i>A</i><sub><i>n</i></sub> − 13 500, calculate the balance of the annuity after the first two withdrawals.',
  [('', '', 2, 'After first withdrawal: $174 600. After second withdrawal: $168 957.', 16)]),
 (TA + ' Q13 · 6.08', 'A charity establishes a perpetuity to fund an annual scholarship of $8000. The fund earns 3.2% per annum. Determine the amount that must be invested to establish this perpetuity.',
  [('', '', 1, '$250 000', 14)]),
 (TA + ' Q14 · 6.08', 'A fund of $750 000 earns 4.2% per annum compounded monthly. Determine the maximum monthly payment that can be made from this fund as a perpetuity.',
  [('', '', 1, '$2625', 14)]),
 (TA + ' Q15 · 6.05', 'Two annuities each start with $280 000. Annuity A earns 5.4% per annum compounded annually with annual withdrawals of $22 000. Annuity B earns 5.4% per annum compounded monthly with monthly withdrawals of $1833.33. Withdrawals continue until each annuity is exhausted, with a smaller final withdrawal. Use a financial solver to determine when the final withdrawal from each annuity is made, and hence which annuity lasts longer and by how many months.',
  [('', '', 3, 'Annuity A: final withdrawal at the end of year 23 (month 276). Annuity B: final withdrawal at month 259. Annuity A lasts 17 months longer.', 22)]),
 (TA + ' Q16 · 6.06', 'Graham, a retiree from Geelong, invests $420 000 in an annuity that earns interest at 4.8% per annum, compounding monthly. He receives a withdrawal of $3000 at the end of each month. Graham used a finance solver to find how long the annuity will last. The solver screen is shown below.' + SOLV,
  [('a', 'State the number of full withdrawals of $3000 that Graham will receive.', 1, '205', 12),
   ('b', "Graham's final withdrawal is smaller than $3000. Determine the value of the final withdrawal, to the nearest cent.", 2, '$1967.42', 22),
   ('c', 'Graham would like the annuity to last exactly 20 years instead. Determine the monthly withdrawal he could receive, to the nearest cent.', 1, '$2725.62', 14)]),
 (TA + ' Q17 · 6.06', 'Leila is retiring and will invest $600 000 in an annuity that is to last exactly 25 years, after which the balance will be zero. She is offered two options.<br>Option A: 5.4% per annum, compounding monthly, with a payment to Leila at the end of each month.<br>Option B: 5.5% per annum, compounding annually, with a payment to Leila at the end of each year.',
  [('a', 'Calculate the effective annual interest rate for Option A, rounded to two decimal places.', 1, '5.54%', 12),
   ('b', 'Determine the monthly payment Leila would receive under Option A, to the nearest cent.', 1, '$3648.78', 12),
   ('c', 'Determine the annual payment Leila would receive under Option B, to the nearest cent.', 1, '$44 729.61', 12),
   ('d', 'Under Option A, determine the balance of the annuity after 10 years, to the nearest dollar.', 1, '$449 475', 12),
   ('e', 'Leila wants the option with the higher effective annual interest rate. Recommend an option for Leila, and justify your recommendation.', 2, 'Option A. Its effective annual rate of 5.54% is higher than the effective annual rate of Option B, which is 5.50% because it compounds annually.', 20)]),
 (TA + ' Q18 · 6.03', 'Ryan and Jess borrow $520 000 to buy a house in Bendigo. Interest is charged at 6.12% per annum, compounding monthly, and they make repayments of $3400 at the end of each month. Part of the amortisation table for the loan is shown below, with two values, <i>a</i> and <i>b</i>, missing.' + AMORT,
  [('a', 'Find the values of <i>a</i> and <i>b</i>.', 2, '<i>a</i> = 2648.19, <i>b</i> = 518 500.19', 18),
   ('b', 'Use a finance solver to determine the total number of monthly repayments needed to repay the loan.', 1, '298 repayments (the final repayment is smaller)', 12),
   ('c', 'Determine the balance of the loan after 5 years, to the nearest cent.', 1, '$467 650.75', 12),
   ('d', 'After 5 years, Ryan and Jess refinance the balance with a loan charging 5.64% per annum, compounding monthly. They keep making repayments of $3400 per month. Determine how many fewer repayments they make than they would have made with the original loan.', 1, '16', 14),
   ('e', 'Refinancing costs a one-off fee of $4000. Decide whether refinancing was worthwhile for Ryan and Jess. Give a reason.', 1, 'Yes. Their total repayments fall by about $54 062, far more than the $4000 fee.', 16)]),
 (TA + ' Q19 · 6.07', 'Priya wants to save $20 000 for a car in 2 years. Her savings account earns 3.6% per annum compounded monthly. Use a financial solver to determine how much Priya must deposit each month, rounded to the nearest cent.',
  [('', '', 2, '$804.94', 18)]),
 (TA + ' Q20 · 6.06', 'A retiree invests $350 000 in an annuity earning 5.2% per annum compounded monthly. The retiree wants the annuity to last exactly 20 years. Use a financial solver to determine the maximum monthly withdrawal, rounded to the nearest cent.',
  [('', '', 2, '$2348.69', 18)]),
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
    out = [f'<div class="title"><div class="code">Ch 8<br>test</div><h1>Reducing balance loans, annuities and investments<div style="font-size:10pt;font-weight:normal;margin-top:1mm">8A–8I · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch8 test' + (' solutions' if sol else '')
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
