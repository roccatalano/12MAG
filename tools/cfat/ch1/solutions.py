"""Solutions copies for CFAT 1.1.1-1.1.3 (Chapter 1). The questions are NOT rebuilt: the student copies
(lessons/CFAT 1.1.x (..).html = copies of the 14 Nov CFAT-1.1.x.html files, left as they are per Rocco) are read and the answers injected in red.
Answers: Edrolo GM U3&4 2023 worked solutions (Answers, pdf pp. 655-700), each checked by hand.
1.1.2 Q7b (shapes for July and May) has no Edrolo answer (Edrolo 1E Q18 has only the fence part): own answer.
Run: python3 solutions.py  -> lessons/CFAT 1.1.x (..) solutions.html/.pdf
"""
import os, re, base64
HERE = os.path.dirname(os.path.abspath(__file__)); L = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'lessons'))
FIG = lambda k: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(HERE, 'fig', k), 'rb').read()).decode()
C = {
 '1.1.1': ('CFAT 1.1.1 (1A-1E)', {
   1: ('E', 'Ordered groups, then unordered labels.'),
   2: ('A', 'Only number of wings is counted (discrete).'),
   3: ('A', '45% = 36, so n = 80; 10% of 80 = 8.'),
   4: ('B', '11 + 4 + 2 = 17.'),
   5: ('E', 'Below log 4: (3 + 2 + 12)/20 = 85%.'),
   6: ('E', 'Modes 2–3 and 4–5 → 10<sup>2</sup>–10<sup>3</sup>, 10<sup>4</sup>–10<sup>5</sup>.')},
   ['The most common brand was Toyota (the modal category), 60% of cars. Holden made up 30% and Ford the remaining 10%.',
    '7 (21, 24, 25, 25, 26, 27, 29)', '13 students (26, 27, 29 + six in the 30s + three in the 40s + 52)', '38 minutes',
    '10<sup>3.6</sup> ≈ 3981 kg', 'log<sub>10</sub>(3750) ≈ 3.57, so the 3.4–&lt;3.6 interval'], None),
 '1.1.2': ('CFAT 1.1.2 (1F-1G)', {
   1: ('C', 'Upper half 6 7 8 9 10 → Q<sub>3</sub> = 8.'),
   2: ('C', '75 − 57 = 18.'),
   3: ('A', '50 − 1.5 × 180 = −220.'),
   4: ('A', 'Whisker ends 1, 10; box 3, 4, 8.'),
   5: ('C', 'Positive skew; 1380 > UF = 645.'),
   6: ('B', 'Long tail on the left.')},
   ['IQR = 11 − 8 = 3; UF = 11 + 1.5 × 3 = 15.5 °C',
    'July: positively skewed with an outlier (about 15.8 °C). May: approximately symmetric with no outliers.',
    '40, 45.5, 51.5, 62.5, 109', 'IQR = 62.5 − 45.5 = 17',
    'LF = 45.5 − 25.5 = 20, UF = 62.5 + 25.5 = 88; 109 > 88, so 109 is an outlier (no low outliers).',
    None, 'Positively skewed', 'n = 32: median = (24.5 + 24.6) ÷ 2 = 24.55 kg'], ('IMGIDX', 4, 'q112_8d.png')),
 '1.1.3': ('CFAT 1.1.3 (1F-1I)', {
   1: ('B', 'CAS: x̄ = 58.88, s<sub>x</sub> = 25.40.'),
   2: ('D', '2.4 SDs below the mean.'),
   3: ('C', 'z = 0 at the mean.'),
   4: ('D', 'x̄ − 2s to x̄ + s: 47.5 + 34.'),
   5: ('A', '69 − 2.5 × 4 = 59.'),
   6: ('B', '(−4.3 − 3.5) ÷ 3 = −2.6.')},
   ['140 = x̄ − s: 34 + 50 = 84%', '215 = x̄ + 2s: 97.5% × 1000 = 975 clusters',
    '128 = x̄ − s to 140 = x̄: 34%', '104 = x̄ − 3s to 116 = x̄ − 2s: 2.35%', '176 = x̄ + 3s: 0.15% × 2000 = 3 plants',
    '116 cm (x̄ − 2s)',
    '2017: z = (10.55 − 10.43)/0.09 = 1.33<br>2018: z = (10.12 − 10.17)/0.23 = −0.22<br>2019: z = (9.97 − 9.91)/0.10 = 0.60',
    '2018: lowest z (−0.22), i.e. faster than the mean time; in 100 m a lower time is better.'], ('IMGIDX', 0, 'q113_8a.png')),
}
CSS = ('<style>.sol .mc div.right > span{color:#c00;font-weight:bold} .why{display:none}'
       ' .sol .qgrid .cite{display:flex;justify-content:space-between;gap:2mm} .sol .why{display:inline;color:#c00;font-style:normal;font-size:8pt;text-align:left}'
       ' .sol .blank .ans{font-size:9.2pt;line-height:1.25}</style>')
def build(code):
    name, mc, sa, fig = C[code]
    s = open(os.path.join(L, f'{name}.html')).read()
    if fig:
        i = [0]
        def rep(m):
            k = i[0]; i[0] += 1
            return FIG(fig[2]) if k == fig[1] else m.group(0)
        s = re.sub(r'data:image/png;base64,[^"]+', rep, s)
    boxes = s.split('<div class="box"><div class="hd">Question ')
    for j in range(1, len(boxes)):
        n = int(re.match(r'\d+', boxes[j]).group()); b = boxes[j]
        if n in mc:
            let, why = mc[n]
            b = re.sub(rf'<div><b>{let}\.</b><span>(.*?)</span></div>', lambda m: f'<div class="right"><b>{let}.</b><span>{m.group(1)} ✓</span></div>', b, count=1)
            b = re.sub(r'<div class="cite">', f'<div class="cite"><span class="why">{why}</span>', b, count=1)
        boxes[j] = b
    s = '<div class="box"><div class="hd">Question '.join(boxes)
    it = iter(sa)
    def blank(m):
        a = next(it)
        return m.group(0) if a is None else m.group(0)[:-6] + f'<div class="ans">{a}</div></div>'
    s = re.sub(r'<div class="blank"( style="[^"]*")?></div>', blank, s)
    assert next(it, 'END') == 'END', code
    s = s.replace('</head><body>', CSS + '</head><body class="sol">', 1)
    s = s.replace('<div><b>Name</b> <i></i></div>', '<div><b style="color:#c00;font-weight:bold">SOLUTIONS</b></div>', 1)
    s = re.sub(r'<title>.*?</title>', f'<title>{name} solutions</title>', s, count=1)
    f = os.path.join(L, f'{name} solutions.html'); open(f, 'w').write(s); return f
if __name__ == '__main__':
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for code in C:
            f = build(code); pg = b.new_page(); pg.goto('file://' + f); pg.wait_for_timeout(2500)
            pg.pdf(path=f[:-5] + '.pdf', prefer_css_page_size=True, print_background=True); pg.close(); print(f)
        b.close()
