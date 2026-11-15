"""Lesson 1 (1A-1B) guided worksheet, S1/S4 house style. Question text copied verbatim from tools/deck/s1/build.py (verbatim-checked against the sources 15 Nov).
Order = the slides (no Do Now in Lesson 1).
Run: python3 tools/deck/s1/worksheet.py -> lessons/S1-worksheet(.html/.pdf) + lessons/S1-worksheet-solutions(.html/.pdf)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from wslib import *

SHADE = ['#fff', '#bbb', '#555']
def grid_svg(W, H, L, T, B, ymax, ystep, yl, xl, pct=False):
    y0 = H - B; k = (H - T - B) / ymax; o = []
    y = 0
    while y <= ymax + 1e-9:
        yy = y0 - y * k
        o.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{W-8}" y2="{yy:.1f}" stroke="#ccc" stroke-width=".5"/><text x="{L-4}" y="{yy+3:.1f}" font-size="8.5" text-anchor="end">{y:g}{"%" if pct else ""}</text>')
        y += ystep
    o.append(f'<line x1="{L}" y1="{y0}" x2="{W-8}" y2="{y0}" stroke="#000"/><line x1="{L}" y1="{y0}" x2="{L}" y2="{T-2}" stroke="#000"/>')
    if xl: o.append(f'<text x="{(L+W-8)/2}" y="{H-3}" font-size="9" text-anchor="middle">{xl}</text>')
    if yl: o.append(f'<text x="9" y="{(T+y0)/2}" font-size="9" text-anchor="middle" transform="rotate(-90 9 {(T+y0)/2})">{yl}</text>')
    return o, y0, k

def barchart(cats, v, ymax, ystep, xl, yl, draw=True, W=260, H=120, labels=True):
    """Bar chart on a grid. draw=False: grid only for students (bars + category labels in red on the solutions copy)."""
    L, T, B = 34, 8, 30
    o, y0, k = grid_svg(W, H, L, T, B, ymax, ystep, yl, xl)
    n = len(cats); slot = (W - 8 - L) / n; bw = slot * .6
    c = '#000' if draw else RED; cls = '' if draw else ' class="solfig"'
    o.append(f'<g{cls}>' + ''.join(f'<rect x="{L+i*slot+(slot-bw)/2:.1f}" y="{y0-f*k:.1f}" width="{bw:.1f}" height="{f*k:.1f}" fill="{"#d9d9d9" if draw else "none"}" stroke="{c}"/>' for i, f in enumerate(v))
             + ('' if labels or draw else ''.join(f'<text x="{L+(i+.5)*slot:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle" fill="{RED}">{t}</text>' for i, t in enumerate(cats))) + '</g>')
    if labels: o += [f'<text x="{L+(i+.5)*slot:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle">{t}</text>' for i, t in enumerate(cats)]
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}</svg>'

def segbar(v, names, ymax, ystep, yl, xl='', draw=True, W=210, H=125, pct=True):
    """One segmented bar + legend. draw=False: grid only for students (segments + legend in red on the solutions copy)."""
    L, T, B = 34, 8, 22
    o, y0, k = grid_svg(W, H, L, T, B, ymax, ystep, yl, xl, pct=False)
    x = L + 14; bw = 46; c = '#000' if draw else RED; cls = '' if draw else ' class="solfig"'
    g = []; s = 0
    for i, f in enumerate(v):
        g.append(f'<rect x="{x}" y="{y0-(s+f)*k:.1f}" width="{bw}" height="{f*k:.1f}" fill="{SHADE[i] if draw else "none"}" stroke="{c}"/>')
        if not draw: g.append(f'<text x="{x+bw/2}" y="{y0-(s+f/2)*k+3:.1f}" font-size="8" text-anchor="middle" fill="{RED}">{names[i]}</text>')
        s += f
    if draw:
        lx = x + bw + 14
        for j, i in enumerate(reversed(range(len(v)))):
            ly = T + 6 + j * 14
            g.append(f'<rect x="{lx}" y="{ly}" width="9" height="9" fill="{SHADE[i]}" stroke="#000"/><text x="{lx+13}" y="{ly+8}" font-size="8.5">{names[i]}</text>')
    o.append(f'<g{cls}>' + ''.join(g) + '</g>')
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}</svg>'

def ftab(var, rows, total, blank=True, pcth='Percentage (%)'):
    """Frequency table. blank=True: number/% cells are answers (red on solutions, empty for students)."""
    f = (lambda x: f'<span class="ans in">{x}</span>') if blank else (lambda x: x)
    body = [[var, 'Number', pcth]] + [[a, f(b), f(c)] for a, b, c in rows] + [['<b>Total</b>', f(f'<b>{total[0]}</b>'), f(f'<b>{total[1]}</b>')]]
    return table(body, cls='t fill')

def report(toks):
    """Report template: text with blanks (red on the solutions copy)."""
    return '<p class="tpl">' + ''.join(t if isinstance(t, str) else f'<span class="s"><u>{t[1]}</u><i>{t[0]}</i></span>' for t in toks) + '</p>'

def mc(opts, cols=1, extra=''):
    if cols == 1 and extra: opts = opts[:-1] + [opts[-1] + ' &nbsp; ' + extra]; extra = ''
    return f'<div class="mc" style="grid-template-columns:repeat({cols},auto)">' + ''.join(f'<div><b>{"ABCDE"[i]}.</b>{o}</div>' for i, o in enumerate(opts)) + (f'<div>{extra}</div>' if extra else '') + '</div>'
def iparts(items, cols=1):
    # parts with the answer blank at the end of the line (saves a ruled line per part)
    return f'<div class="parts" style="grid-template-columns:repeat({cols},minmax(0,1fr))">' + ''.join(f'<div class="pt"><b>{k}</b><div>{t} <span class="blank" style="display:inline-block;min-width:20mm;border-bottom:1px solid #999">{ans(a, True)}&nbsp;</span></div></div>' for k, t, a in items) + '</div>'
# ---------------------------------------------------------------- page 1
P = ['<style>@page{margin:8mm 10mm 9mm 10mm}body{font-size:9pt;line-height:1.2}.title{margin-bottom:2mm}.ki li{margin:0;font-size:8.5pt}.ki{column-count:2}.box,.pair{margin-bottom:2mm}.lines div{height:6.3mm}.box>.bd,.pair .bd{padding:1.5mm 2.5mm}.sig .stamp{height:14mm}.sig{margin-top:1.5mm}.guess{margin-top:1mm;padding:.8mm 2mm}.sc{padding:.6mm 2mm}.hwg>div{padding:1mm}.tpl{line-height:1.8}.pt{padding:.3mm 0}.pl{min-height:4.6mm}table.fill td{height:5mm}table.t th,table.t td{padding:.3mm 2mm}.scg .sc{border-right:none!important;border-bottom:1px solid #000}.row .box>.hd span{font-size:8pt}</style>', title('1A–1B', 'Types of data and categorical data', 'Chapter 1 · 1A, 1B')]
P.append(lis(['To be able to classify data as categorical or numerical.', 'To be able to further classify categorical data as nominal or ordinal.',
  'To be able to further classify numerical data as discrete or continuous.', 'To be able to construct frequency and percentage frequency tables for categorical data.',
  'To be able to construct bar charts and percentage bar charts from frequency tables.', 'To be able to interpret and describe frequency tables and bar charts.',
  'To be able to answer statistical questions about a categorical variable.']))

apk = (item('1', q('<b>1.</b> Classify the following data as nominal, ordinal, discrete or continuous:')
          + iparts([('a', 'The time between people arriving at the coffee shop.', 'continuous'), ('b', 'The number of people in the queue at the coffee shop.', 'discrete'),
                   ('c', 'Customer’s coffee preference (latte, cappuccino, black).', 'nominal'), ('d', 'Customer’s rating of the coffee (excellent, quite good, not that good).', 'ordinal')], cols=2), sep=False)
       + cite(f'{CAM12} · Chapter 2 skills checklist, 2A #1')
       + item('2', q('<b>2.</b> The percentage segmented bar chart provided shows the <i>age</i> (under 55 years, 55 years and over) of visitors at a travel convention, segmented by <i>preferred travel destination</i> (domestic, international).')
              + q('The variables <i>age</i> (under 55 years, 55 years and over) and <i>preferred travel destination</i> (domestic, international) are')
              + mc(['both categorical variables.', 'both numerical variables.', 'a numerical variable and a categorical variable respectively.', 'a categorical variable and a numerical variable respectively.', 'a discrete variable and a continuous variable respectively.'], extra=ans('→ A (age is in groups)', True)),
              '<svg viewBox="0 0 230 150" width="100%" style="max-width:60mm">' + ''.join(
                  [f'<line x1="34" y1="{120-p*1.1:.1f}" x2="200" y2="{120-p*1.1:.1f}" stroke="#ccc" stroke-width=".5"/><text x="30" y="{123-p*1.1:.1f}" font-size="8" text-anchor="end">{p}</text>' for p in range(0, 101, 20)]
                  + [f'<rect x="{x}" y="{120-(a+b)*1.1:.1f}" width="40" height="{b*1.1:.1f}" fill="{f}" stroke="#000"/>' for x, segs in ((50, (65, 35)), (115, (45, 55))) for a, b, f in ((0, segs[0], '#fff'), (segs[0], segs[1], '#999'))]
                  + ['<line x1="34" y1="120" x2="165" y2="120" stroke="#000"/><line x1="34" y1="120" x2="34" y2="8" stroke="#000"/>',
                     '<text x="70" y="131" font-size="8" text-anchor="middle">under 55</text><text x="135" y="131" font-size="8" text-anchor="middle">55 and over</text><text x="100" y="145" font-size="8.5" text-anchor="middle">age</text>',
                     '<text x="9" y="64" font-size="8.5" text-anchor="middle" transform="rotate(-90 9 64)">percentage</text>',
                     '<rect x="166" y="14" width="8" height="8" fill="#999" stroke="#000"/><text x="177" y="21" font-size="7.5">inter-</text><text x="177" y="29" font-size="7.5">national</text>',
                     '<rect x="166" y="38" width="8" height="8" fill="#fff" stroke="#000"/><text x="177" y="45" font-size="7.5">domestic</text>']) + '</svg>')
       + guess('70% · C (21%)') + cite(f'{EDR12} · 1A Q13 · VCAA 2021 Exam 1 Data analysis Q1')
       + item('3', q('<b>3.</b> The data in the table shown was collected in a study of the association between the variables <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes).')
              + q('The variables in this study, <i>frequency of nightmares</i> (low, high) and <i>snores</i> (no, yes), are')
              + mc(['ordinal and nominal respectively.', 'nominal and ordinal respectively.', 'both numerical.', 'both ordinal.', 'both nominal.'], cols=2, extra=ans('A: low/high has an order (ordinal); no/yes only names a group (nominal).', True)),
              '<table class="t" style="font-size:8.5pt"><tr><th></th><th colspan="2"><i>snores</i></th><th></th></tr><tr><th><i>frequency of nightmares</i></th><th>no</th><th>yes</th><th>total</th></tr>'
              '<tr><td class="l">low</td><td>80</td><td>58</td><td>138</td></tr><tr><td class="l">high</td><td>11</td><td>12</td><td>23</td></tr><tr><td class="l">total</td><td>91</td><td>70</td><td>161</td></tr></table>')
       + guess('57% · D (24%)') + cite(f'{EDR12} · 1A Q14 · VCAA 2020 Exam 1 Data analysis Q10'))
P.append(box('Activating prior knowledge', apk, 'Year 11', cls='split'))

P.append(pair('Example 1 · Types of data',
  q('Classify the following data as nominal, ordinal, discrete or continuous.')
  + iparts([('a', 'The number of chocolate chips in each of 10 cookies is counted.', 'discrete'), ('b', 'The time taken for 20 students to complete a puzzle is recorded in seconds.', 'continuous'),
           ('c', 'Member of a football club were asked to rate how they felt about the current coach, 1 = Very satisfied, 2 = Satisfied, 3 = Indifferent, 4 = Dissatisfied, 5 = Very dissatisfied.', 'ordinal'),
           ('d', 'Students are asked to each choose their preferred colour from the list 1 = Blue, 2 = Green, 3 = Red, 4 = Yellow.', 'nominal'),
           ('e', 'Students weights were classified as ‘less than 60kg’, ‘60kg - 80kg’ or ‘more than 80kg’.', 'ordinal')]) + cite(f'{CAM} · Example 1 (p. 4)'),
  'You try · Edrolo 1A WE1, WE2, WE3',
  q('<b>1</b> Classify the following variables as either categorical or numerical.') + iparts([('a.', '<i>type of pasta</i>', 'categorical'), ('b.', '<i>number of candles</i>', 'numerical')], cols=2)
  + q('<b>2</b> Classify the following categorical variables as either nominal or ordinal.') + iparts([('a.', '<i>type of shoe</i> (runners, boots, sandals, slides)', 'nominal'), ('b.', '<i>shirt size</i> (small, medium, large)', 'ordinal')])
  + q('<b>3</b> Classify the following numerical variables as either discrete or continuous.') + iparts([('a.', '<i>length</i> (m)', 'continuous'), ('b.', '<i>number of tennis racquets</i>', 'discrete')], cols=2)
  + cite(f'{EDR} · 1A Worked examples 1, 2 and 3 (pp. 2–4)')))

# ---------------------------------------------------------------- 1B
ICE = 'C V V C C V C C C V V'
TH = 'average short tall tall short short average average tall short average short average average average tall tall short average tall tall average average tall'
P.append(pair('Example 2 · Frequency table for a categorical variable',
  q('A group of 11 preschool children were asked to choose between chocolate and vanilla ice-cream (C = chocolate, V = vanilla):') + f'<div class="data">{ICE}</div>'
  + q('Construct a frequency table (including percentage frequencies) to display the data.')
  + ftab('Flavour', [('chocolate', 6, '54.5'), ('vanilla', 5, '45.5')], (11, '100.0')) + cite(f'{CAM} · Example 2 (p. 7)'),
  'You try · Edrolo 1B WE1',
  q('The students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses were as follows:')
  + f'<div class="data" style="font-size:8.5pt;font-family:inherit">{TH}</div>'
  + q('Use this data to create a frequency table displaying both frequency and percentage frequency, correct to the nearest decimal place.')
  + ftab('teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), pcth='%') + cite(f'{EDR} · 1B Worked example 1 (pp. 9–10)')))

CLIM = ftab('Climate type', [('Cold', 3, '13.0'), ('Mild', 14, '60.9'), ('Hot', 6, '26.1')], (23, '100.0'), blank=False)
THT = ftab('teacher’s height', [('short', 6, '25.0'), ('average', 10, '41.7'), ('tall', 8, '33.3')], (24, '100.0'), blank=False, pcth='%')
P.append(pair('Example 3 · Constructing a bar chart from a frequency table',
  q('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. The results are summarised in the table opposite.') + CLIM
  + q('<b>a</b> What is the level of measurement of the variable <i>climate type</i>?') + lines(1, 'Ordinal: cold, mild, hot have a natural order of warmth.')
  + q('<b>b</b> Construct a frequency bar chart to display this information.') + barchart(['Cold', 'Mild', 'Hot'], [3, 14, 6], 15, 5, 'Climate type', 'Frequency', draw=False, labels=False)
  + cite(f'{CAM} · Example 3 (p. 8)'),
  'You try · Edrolo 1B WE2',
  q('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown.') + THT
  + q('Use the frequency table to construct a frequency bar chart.') + barchart(['short', 'average', 'tall'], [6, 10, 8], 10, 2, 'teacher’s height', 'frequency', draw=False, labels=False)
  + cite(f'{EDR} · 1B Worked example 2 (p. 11)')))

P.append(pair('Example 4 · Constructing a percentage segmented bar chart',
  q('The climate type of 23 countries is classified as ‘cold’, ‘mild’ or ‘hot’. <i>(Table: see Example 3.)</i>')
  + q('Construct a percentage frequency segmented bar chart to display this information.')
  + '<div class="row"><div style="flex:1">' + segbar([13.0, 60.9, 26.1], ['Cold', 'Mild', 'Hot'], 100, 10, 'Percentage', draw=False, W=200, H=160) + '</div><div style="flex:1">'
  + ans('Cold 0 to 13.0<br>Mild 13.0 to 13.0 + 60.9 = 73.9<br>Hot 73.9 to 100') + '</div></div>' + cite(f'{CAM} · Example 4 (p. 9)'),
  'You try · Edrolo 1B WE3',
  q('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are recorded in the frequency table shown. <i>(Table: see You try 1B WE2.)</i>') + q('<b>a.</b> Use the frequency table to construct a segmented bar chart.<br><b>b.</b> Use the frequency table to construct a percentage segmented bar chart.')
  + '<div class="row"><div style="flex:1"><b>a.</b>' + segbar([6, 10, 8], ['short', 'average', 'tall'], 24, 4, 'frequency', draw=False, W=150, H=110) + '</div><div style="flex:1"><b>b.</b>'
  + segbar([25, 41.7, 33.3], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', draw=False, W=150, H=110) + '</div></div>' + cite(f'{EDR} · 1B Worked example 3 (pp. 12–13)')))

P.append(pair('Example 5 · Describing the distribution',
  q('In an investigation of the variation of climate type across countries, the climate types of 23 countries were classified as ‘cold’, ‘mild’ or ‘hot’. The data are displayed in a frequency table to show the percentages.')
  + q('<i>(Table: see Example 3.)</i> Use the information in the frequency table to write a concise report on the distribution of climate types across these 23 countries.')
  + report(['The ', ('variable', 'climate types'), ' of ', ('number', '23'), ' ', ('individuals', 'countries'), ' were classified as being ', ('categories', '‘cold’, ‘mild’ or ‘hot’'), '. The ', ('majority / most', 'majority'), ' of the countries, ',
            ('%', '60.9%'), ', were found to ', ('modal category', 'have a mild climate'), '. Of the remaining countries, ', ('%', '26.1%'), ' were found to have a ', ('category', 'hot'), ' climate, while ', ('%', '13.0%'), ' were found to have a ', ('category', 'cold'), ' climate.'])
  + cite(f'{CAM} · Example 5 (pp. 10–11)'),
  'You try · Edrolo 1B WE4',
  '<div class="row"><div style="flex:1.4">' + q('24 students in a prep class were asked the question, ‘Would you describe your teacher’s height as short, average or tall?’. Their responses are shown in the given percentage segmented bar chart.')
  + '</div><div style="flex:1">' + segbar([25, 41.7, 33.3], ['short', 'average', 'tall'], 100, 20, 'frequency (%)', W=170, H=130) + '</div></div>'
  + q('<b>a.</b> Find the modal category of the data set.') + lines(1, 'Average')
  + q('<b>b.</b> Describe the distribution of the data set.')
  + report([('number', '24'), ' ', ('individuals', 'prep students'), ' were surveyed on ', ('question', 'how tall they thought their teacher was'), '. The ', ('most common / majority', 'most common'), ' response was ', ('modal category', 'average'),
            ', accounting for ', ('%', '41.7%'), ' of responses, while ', ('%', '25%'), ' said ', ('category', 'short'), ', and ', ('%', '33.3%'), ' said ', ('category', 'tall'), '.'])
  + cite(f'{EDR} · 1B Worked example 4 (p. 14)')))

# ---------------------------------------------------------------- exits
DAY = list(range(1, 16)); TMP = [12.7, 11.8, 10.7, 9.0, 6.0, 7.0, 4.1, 4.8, 9.2, 6.7, 7.5, 8.0, 8.6, 9.8, 7.7]
TT = table([['<i>day number</i>'] + DAY, ['<i>minimum temperature</i> (°C)'] + TMP], head=False, style='font-size:7.8pt')
HEP = [(1, 1.76, 15.34, 41.22), (2, 1.79, 16.96, 42.41), (3, 1.83, 13.87, 46.53), (4, 1.82, 14.23, 40.53), (5, 1.87, 13.78, 40.62), (6, 1.73, 14.50, 45.62), (7, 1.68, 15.08, 42.33), (8, 1.82, 13.13, 40.88),
       (9, 1.83, 14.22, 39.22), (10, 1.87, 13.62, 42.51), (11, 1.87, 12.01, 42.75), (12, 1.80, 12.88, 38.12), (13, 1.83, 12.68, 42.65), (14, 1.87, 12.45, 41.32), (15, 1.78, 11.31, 42.88)]
HT = lambda rows: table([['<i>athlete number</i>', '<i>high jump</i> (metres)', '<i>shot-put</i> (metres)', '<i>javelin</i> (metres)']] + [[a, f'{b:.2f}', f'{c:.2f}', f'{d:.2f}'] for a, b, c, d in rows], cls='t tiny')
ex = (q('<b>1.</b> The table shows the <i>day number</i> and the <i>minimum temperature</i>, in degrees Celsius, for 15 consecutive days in May 2017.') + TT
      + q('Which of the two variables in this data set is an ordinal variable? <i>(1 mark)</i>') + lines(1, '<i>day number</i>')
      + guess('83%', mcq=False) + cite(f'{EDR} · 1A Q14 · VCAA 2019 Exam 2 Data analysis Q1a')
      + item('2', q('<b>2.</b> In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>Their results for three of the heptathlon events – high jump, shot-put and javelin – are shown in the table.')
             + table([['<i>athlete number</i>']+[h[0] for h in HEP]]+[[n]+[f'{h[k]:.2f}' for h in HEP] for k,n in ((1,'<i>high jump</i> (metres)'),(2,'<i>shot-put</i> (metres)'),(3,'<i>javelin</i> (metres)'))], cls='t tiny', style='')
             + q('Write down the number of numerical variables in the table. <i>(1 mark)</i>') + lines(1, '3 (athlete number is a label)'))
      + guess('52%', mcq=False) + cite(f'{EDR} · 1A Q16 · VCAA 2021 Exam 2 Data analysis Q1a (table rows and columns swapped to fit)')
      + item('3', q('<b>3.</b> A study was conducted that investigated the <i>number of moths</i> caught in a sugar moth trap (less than 250, 250–500, more than 500). The results are summarised in the percentage segmented bar chart shown.')
             + q('There were 300 sugar traps.<br>The number of sugar traps that caught less than 250 moths is closest to') + mc(['30', '90', '250', '300', '500'], cols=5, extra=ans('B: 30 ÷ 100 × 300 = 90', True)),
             segbar([30, 46, 24], ['less than 250', '250–500', 'more than 500'], 100, 10, 'frequency (%)', 'number of moths', W=220, H=115))
      + guess('76% · A (21%)') + cite(f'{EDR} · 1B Q13 · Adapted from VCAA 2017 Exam 1 Data analysis Q5'))
P.append(box('Exit tasks', ex, 'Show what you know', cls='split'))
CK=checklist(['I can identify types of data.', 'I can construct a frequency table for categorical data.', 'I can construct a bar chart from a frequency table.',
  'I can construct a percentage segmented bar chart from a frequency table.', 'I can describe the distribution of a categorical variable.'])
CW=coursework([('Exercise 1A', 'Q1 · Q2 · Q3<br>Q4–6 <i>(Exam 1 style)</i>'), ('Exercise 1B', 'Q1–3 · Q4–5<br>Q6–8 · Q9 <i>(Exam 1 style)</i>')], 'Chapter 1 revision booklet: 1A and 1B sections')
P.append(f'<div class="row" style="gap:2mm;align-items:stretch"><div style="flex:.8">{CK.replace("class=\"scg\"","class=\"scg\" style=\"grid-template-columns:1fr\"")}</div><div style="flex:1.2">{CW}</div></div>')
build('1A–1B', 'Types of data and categorical data', P, 'S1')
