# Chapter 8 revision booklet: Insight GM1 (MC) + GM2 (SA), Unit 3 Recursion and Financial Modelling, second and third
# sections: 'Reducing balance loans, annuities, perpetuities, amortisation tables' (GM1 Q1-21, printed pp.7-11 = pdf 10-14;
# GM2 Q1-3, printed pp.11-13 = pdf 14-16) and 'Using the finance solver' (GM1 Q1-12, printed pp.11-13 = pdf 14-16;
# GM2 Q1-8, printed pp.14-17 = pdf 17-20). The first section was used in the Ch 7 booklet.
# Questions are scans of the Insight pages (crop.py -> crops/*.png), verbatim; GM2 crops keep Insight's own answer lines.
# Answers from Insight's explanatory notes / worked solutions (GM1 pp.17-25, GM2 pp.24-31). Insight is never burnt.
# Insight print glitches kept as printed: GM1 Q10 reads 'V_{n+1} = 1.5V_0 + 100' (V_n meant; Insight's answer uses V_n);
# GM1 multiplication signs print as '´'.
A = 'Insight GM1 U3 Recursion and Financial Modelling, ‘Reducing balance loans…’'
F = 'Insight GM1 U3 Recursion and Financial Modelling, ‘Using the finance solver’'
S = 'Insight GM2 U3 Recursion and Financial Modelling, ‘Reducing balance loans…’'
T = 'Insight GM2 U3 Recursion and Financial Modelling, ‘Using the finance solver’'


def MC(key, sub, page, a, why, info=None, shared=None):
    sec, n = (A, key[1:]) if key[0] == 'a' else (F, key[1:])
    stem = (f'[[{info}]]' if info else '') + f'[[{key}]]'
    return dict(kind='mc', n=n, sub=sub, stem=stem, opts=None, a='ABCDE'.index(a), why=why, src=f'{sec} p.{page} Q{n}', shared=shared)


def SX(key, sub, page, marks, ans):
    sec = S if key[0] == 's' else T
    segs = f'[[{key}]]' + ('[[t5_2]]' if key == 't5' else '')
    return dict(kind='sx', n=key[1:], sub=sub, marks=marks, stem=segs, ans=ans, src=f'{sec} p.{page} Q{key[1:]}')


SUBS = [('8A', 'Compound interest investments with regular additions'), ('8B', 'Reducing balance loans and annuities (recurrence relations)'),
        ('8C', 'Amortisation tables'), ('8D', 'Analysing financial situations with amortisation tables'),
        ('8E', 'Finance solver: balance and final payment'), ('8F', 'Finance solver: interest rate, time and payment'),
        ('8G', 'Harder financial problems'), ('8H', 'Interest-only loans'), ('8I', 'Perpetuities')]
EMPTY = {}

Q = [
 # 8A
 MC('a7', '8A', 8, 'D', '3.8 ÷ 12 = 0.317% per month, so R = 1.00317; the $250 is added: V<sub>n+1</sub> = 1.00317 × V<sub>n</sub> + 250.'),
 MC('a10', '8A', 9, 'D', 'Starts at 1000 and grows by ×1.5 then +100 each year: 1000, 1600, 2500, 3850, …: graph D (Insight prints V<sub>0</sub> on the right for V<sub>n</sub>).'),
 SX('t4', '8A', 15, 4, '<b>a</b> 450 × 12 = $5400<br><b>b</b> 0.38% × 12 = 4.56%<br><b>c i</b> $30 544 (after 10 months)<br><b>c ii</b> 10 + 21 = 31 months'),
 # 8B
 MC('a1', '8B', 7, 'E', 'Apply the rule four times: 31 791, 31 578.24, 31 361.65, 31 141.16.'),
 MC('a3', '8B', 7, 'E', '1.00238 = 1 + (r/12)/100, so r = 0.238 × 12 = 2.856 ≈ 2.86%.', info='ia3', shared='Q3–4'),
 MC('a4', '8B', 7, 'C', 'Six steps of the recurrence relation on CAS: $45 889.6 ≈ $45 890.', info='ia3', shared='Q3–4'),
 MC('a5', '8B', 7, 'E', 'A loan: interest is added (R &gt; 1) and the payment is subtracted: R<sub>n+1</sub> = 1.004 × R<sub>n</sub> − 1250.'),
 MC('a11', '8B', 9, 'C', 'Five steps of the recurrence relation on CAS: $2245.', info='ia11', shared='Q11–12'),
 MC('a12', '8B', 9, 'D', 'Interest is added (R = 1.062) and $200 is taken out each period, and 200 is more than the interest: an annuity with regular withdrawals of $200.', info='ia11', shared='Q11–12'),
 # 8C
 MC('a2', '8C', 7, 'C', 'Interest on payment 3 = 274 724.38 × 0.054 ÷ 12 = 1236.26; principal reduction = 1375 − 1236.26 = $138.74.'),
 MC('a6', '8C', 8, 'C', 'Principal reduction = 346 117.98 − 344 788.03 = 1329.95; interest = 2700 − 1329.95 = $1370.05.'),
 MC('a20', '8C', 11, 'A', 'Interest = 700 000 × 0.033 ÷ 12 = $1925; principal reduction = 3724 − 1925 = $1799; balance = 700 000 − 1799 = $698 201.', info='ia20', shared='Q20–21'),
 # 8D
 MC('a8', '8D', 8, 'A', 'Balance after 32 = balance after 31 + 503.83, so 78 740.33 − 503.83 = $78 236.50.', info='ia8', shared='Q8–9'),
 MC('a9', '8D', 8, 'E', 'Principal addition = 79 753.28 − 79 245.92 = 507.36; interest = 507.36 − 230 = 277.36; 277.36 ÷ 507.36 = 54.7% ≈ 55%.', info='ia8', shared='Q8–9'),
 MC('a13', '8D', 10, 'C', 'Quarterly rate = 1300 ÷ 100 000 = 1.3%; annual rate = 1.3 × 4 = 5.2%.', info='ia13', shared='Q13–14'),
 MC('a14', '8D', 10, 'C', 'Principal reduction = 99 392.17 − 99 184.27 = 207.90; 207.90 ÷ 1500 = 13.86%.', info='ia13', shared='Q13–14'),
 MC('a21', '8D', 11, 'D', 'Principal reduction 1808.91 ÷ 3724 = 48.6%.', info='ia20', shared='Q20–21'),
 SX('s3', '8D', 13, 4, '<b>a</b> 4.1 ÷ 4 = 1.025%<br><b>b</b> 73 687.19 − 2925.31 = $70 761.88<br><b>c</b> interest = 79 628.07 × 0.01025 = 816.19; deposit = 3141.19 − 816.19 = $2325<br><b>d</b> 725.31 ÷ 2925.31 × 100 = 24.8%'),
 # 8E
 MC('a17', '8E', 10, 'D', 'Finance solver, N = 24: Will ≈ $20 892 (PV −10 000, Pmt −400, 4.05%, 12/yr); Linda ≈ $12 936 (N = 52, PV −12 000, 4.02%, 26/yr). Total ≈ $33 828.', info='ia16', shared='Q16–18'),
 MC('f1', '8E', 11, 'C', 'Finance solver: N = 8, I% = 3.25, PV = −4500, Pmt = −500, Ppy = Cpy = 4 → FV = 8916.57. Interest = 8916.57 − 4500 − 8 × 500 = $416.57.'),
 MC('f6', '8E', 12, 'C', 'Finance solver: N = 60, I% = 5.25, PV = 425 000, Pmt = −3100 → FV ≈ −340 089.56. Interest = 60 × 3100 − (425 000 − 340 089.56) = 186 000 − 84 910.44 = $101 090.', info='if6', shared='Q6–7'),
 MC('f10', '8E', 13, 'C', 'Finance solver twice (N = 52, I% = 3.7, PV = −1500, Ppy = Cpy = 26): Pmt −50 and Pmt −20; the difference in FV is about $1618.'),
 SX('t2', '8E', 14, 1, '$841 825.35 (N = 24, I% = 3.82, PV = −780 000, Pmt = 0, 12 per year)'),
 SX('t7', '8E', 16, 2, '<b>a</b> $38 229 (N = 60)<br><b>b</b> first five years 42 060 − 31 771 = 10 289; last five years 42 060 − 38 229 = 3831; difference $6458'),
 # 8F
 MC('a16', '8F', 10, 'C', 'Finance solver: I% = 4.05, PV = −10 000, Pmt = −400, FV = 20 000 → N = 22.1, so 23 months.', info='ia16', shared='Q16–18'),
 MC('f4', '8F', 12, 'C', 'Finance solver: N = 300, I% = 5.85, PV = 425 000, FV = 0 → Pmt = −$2699.44.', info='if4', shared='Q4–5'),
 MC('f5', '8F', 12, 'E', '5.85 ÷ 12 = 0.4875% per month, so R = 1.004875, and the repayment is subtracted.', info='if4', shared='Q4–5'),
 MC('f11', '8F', 13, 'D', 'R = 1.0061 means 0.61% per quarter = 2.44% p.a.; finance solver with PV = −13 800, Pmt = 162.50, FV = 0 → N ≈ 120 quarters.'),
 SX('s2', '8F', 12, 4, '<b>a</b> 5.2% (finance solver: N = 48, PV 650 000, Pmt −4960.35, FV −535 893.37)<br><b>b</b> after 12 months FV = −623 653.76; paid 12 × 4960.35 = 59 524.20; principal repaid 650 000 − 623 653.76 = 26 346.24; interest = 59 524.20 − 26 346.24 = $33 177.96<br>'
    '<b>c</b> G<sub>0</sub> = 535 893.37, G<sub>n+1</sub> = 1.004G<sub>n</sub> − 4327.56'),
 SX('t3', '8F', 14, 3, '<b>a</b> 36 + 18 = 54 months<br><b>b</b> value after 4 years $926 869.57; interest = 926 869.57 − 874 552 − 12 × 1500 = $34 317.60 ≈ $34 318'),
 SX('t6', '8F', 16, 1, '$125 per fortnight (N = 156, I% = 3.56, PV = −7076, FV = 30 482, 26 per year)'),
 # 8G
 MC('f2', '8G', 11, 'E', 'Stage 1 (N = 20, 2.6%, quarterly, PV −75 000, Pmt −1000) gives the new PV; stage 2 (N = 60, 3.2%, monthly, FV 175 000) gives Pmt ≈ −$767.38.'),
 MC('f3', '8G', 12, 'C', 'After 24 months the balance is about $21 884; with Pmt −750, N ≈ 31 months instead of 36 remaining: 5 months saved.'),
 MC('f7', '8G', 12, 'E', 'From $319 256, N = 48 months left (10 years − 6), I% = 4.95 → Pmt ≈ $7345.', info='if6', shared='Q6–7'),
 MC('f8', '8G', 12, 'A', 'Two stages (2 years at $150, then 8 years at $220) vs 10 years at $150: the difference in FV is about $8004.'),
 MC('f9', '8G', 13, 'B', 'Over 10 years (N = 120), compare the interest paid with Pmt −1762 and Pmt −1972 (total paid − principal repaid): about $4299 saved.'),
 MC('f12', '8G', 13, 'D', 'Three one-year stages (N = 26 each, 2.05%, 26 per year) with Pmt −800, −850, −900, each FV becoming the next PV: about $72 552.'),
 SX('s1', '8G', 11, 6, '<b>a</b> $13 992.47<br><b>b</b> $208.50 (N = 84, I% = 4.5, PV 15 000, FV 0)<br><b>c</b> after 24 months owes $11 183.94; paid 24 × 208.50 = 5004; principal repaid 3816.06; interest = $1187.94<br>'
    '<b>d</b> after 3 years owes $9143.44; with Pmt −325, N = 29.8 → 30 months instead of 48: saves 18 months'),
 SX('t1', '8G', 14, 3, '<b>a</b> $41 526.87<br><b>b</b> after 4 years owes $29 478.20; N = 24, FV = 0 → $1322.49 per month'),
 SX('t8', '8G', 17, 3, '<b>a i</b> with Pmt 701, N = 85.2, so 85 full payments; 144 − 85 = 59 months shorter<br><b>a ii</b> balance after 5 years $16 917.04; N = 24, PV −16 917.04, Pmt 701, FV 841 → 4.01%'),
 # 8H
 SX('t5', '8H', 15, 4, '<b>a</b> 3.78%<br><b>b</b> (1590 × 12) − (310 000 − 302 321.97) = $11 402<br><b>c</b> $310 000 (interest-only: the balance does not change)<br><b>d</b> N = 288, PV 310 000, FV 0 → $1629 per month'),
 # 8I
 MC('a15', '8I', 10, 'E', 'Perpetuity payment = interest each month: 80 000 × 0.037 ÷ 12 = $246.67 ≈ $247 (the 7 years does not matter).'),
 MC('a18', '8I', 10, 'D', 'Interest each fortnight = 15 000 × 0.0402 ÷ 26 = $23.19; withdrawing $23 keeps the balance from reducing ($24 would reduce it).', info='ia16', shared='Q16–18'),
 MC('a19', '8I', 11, 'B', 'Monthly interest = 24 000 × 0.0212 ÷ 12 = 42.40; over 120 months = $5088.'),
]
