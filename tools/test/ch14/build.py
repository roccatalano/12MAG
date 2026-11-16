"""Chapter 14 test (14A-14E, flow, matching, critical path) + solutions, HTML + PDF in the CFAT layout. Model: tools/test/ch13/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4 'Chapter 9 - Applications of graphs and networks' topic assessment + answer key,
every question the Ch13 test does not use: Q1, 2, 6, 7, 8, 9 (MC) and Q11-20 (short response). (Q3, 4, 5, 10 = shortest path, in the Ch13 test.)
(02 Sources\\Textbooks\\Mathspace). Figures (Q13, Q16, Q17, Q18 and the Q11 answer network) cropped from the PDFs at 300 dpi; tables retyped.
Answers = Mathspace answer key (checked by hand).
Run: python3 tools/test/ch14/build.py lessons
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

A = 'Mathspace Ch 9 (applications of graphs and networks) topic assessment'
I = lambda s: '<i>' + s + '</i>'
MC = [
 (A + ' Q1 · 9.01', 'In a flow network, which of the following best describes a source node?', ['A node with no edges', 'A node with only outgoing edges', 'A node with only incoming edges', 'A node with both incoming and outgoing edges'], 1),
 (A + ' Q2 · 9.01', 'A flow network has the following edges and capacities: <i>S</i> → <i>A</i> = 12, <i>S</i> → <i>B</i> = 8, <i>A</i> → <i>T</i> = 10, <i>B</i> → <i>T</i> = 6. What is the maximum flow from <i>S</i> to <i>T</i>?', ['16', '20', '36', '14'], 0),
 (A + ' Q6 · 9.09', 'In a project network, an activity has an earliest start time (EST) of 8 and a latest start time (LST) of 11. What is the float time for this activity?', ['11', '19', '3', '8'], 2),
 (A + ' Q7 · 9.07', 'A project network has the following activities and immediate predecessors. Which activity must be completed before activity <i>D</i> can begin?' + T([['Activity', 'Duration (days)', 'Immediate predecessor'], ['A', '3', '—'], ['B', '5', '—'], ['C', '4', 'A'], ['D', '6', 'B, C'], ['E', '2', 'D']], True), ['Activity A only', 'Activities A and B only', 'Activities A, B, and C', 'Activities B and C'], 3),
 (A + ' Q8 · 9.10', 'A project has a critical path duration of 20 days. Activity <i>P</i> is on the critical path and can be crashed by up to 3 days at a cost of $400 per day. Activity <i>Q</i> is not on the critical path and has a float of 2 days. To reduce the project duration by 2 days at minimum cost, which activity should be crashed?', ['Both P and Q equally', 'Neither activity, as the project cannot be shortened', 'Activity Q only, as it is cheaper', 'Activity P only, as it is on the critical path'], 3),
 (A + ' Q9 · 9.05', 'Which of the following correctly describes a bipartite graph?', ['A graph whose vertices can be divided into two disjoint sets where edges only connect vertices from different sets', 'A graph where every vertex is connected to every other vertex', 'A directed graph with exactly one source and one sink', 'A graph where all edges have equal weight'], 0),
]
CL = ['Cleaner', 'P', 'Q', 'R', 'S']
SA = [
 (A + ' Q11 · 9.07', 'A construction project has the following activities, durations, and predecessors.' + T([['Activity', 'Duration (days)', 'Predecessor'], ['A', '4', '—'], ['B', '6', '—'], ['C', '3', 'A'], ['D', '5', 'B'], ['E', '2', 'C, D']], True) + 'Draw a project network diagram for this project.',
  [('', '', 2, IMG('a11.png', 95), 50)]),
 (A + ' Q12 · 9.09', 'A project network has been fully scanned. The EST and LST values are shown below.' + T([['Vertex', 'EST', 'LST'], ['Start', '0', '0'], ['<i>V</i><sub>1</sub>', '7', '7'], ['<i>V</i><sub>2</sub>', '4', '9'], ['<i>V</i><sub>3</sub>', '13', '13'], ['Finish', '20', '20']], True) + 'Identify all vertices on the critical path and state the project duration.',
  [('', '', 2, 'Critical path vertices (where EST = LST): Start, <i>V</i><sub>1</sub>, <i>V</i><sub>3</sub>, Finish. Project duration 20 days.', 18)]),
 (A + ' Q13 · 9.02', 'The flow network shows the capacities of pipes, in litres per second, from the source <i>S</i> to the sink <i>T</i>. Determine the capacity of the cut shown.' + IMG('q13.png', 55),
  [('', '', 1, '13', 14)]),
 (A + ' Q14 · 9.08', 'In a project network, activities <i>P</i> and <i>Q</i> both end at vertex <i>V</i>, and activity <i>R</i> starts at vertex <i>V</i>. Activity <i>P</i> has an earliest start time of 9 days and a duration of 5 days. Activity <i>Q</i> has an earliest start time of 6 days and a duration of 7 days. Determine the earliest start time of activity <i>R</i>.',
  [('', '', 1, '14 days', 14)]),
 (A + ' Q15 · 9.06', 'A cleaning company must assign four cleaners, Ava, Ben, Cara and Dev, to four offices, <i>P</i>, <i>Q</i>, <i>R</i> and <i>S</i>, one cleaner to each office. The table shows the time, in minutes, each cleaner takes to clean each office.'
  + T([CL, ['Ava', '44', '22', '34', '22'], ['Ben', '54', '28', '38', '46'], ['Cara', '28', '54', '26', '56'], ['Dev', '38', '54', '30', '26']], True)
  + 'The manager used a spreadsheet to carry out the row reduction and column reduction steps of the Hungarian algorithm. The spreadsheet output is shown below.'
  + T([CL, ['Ava', '20', '0', '12', '0'], ['Ben', '24', '0', '10', '18'], ['Cara', '0', '28', '0', '30'], ['Dev', '10', '28', '4', '0']], True),
  [('a', 'Explain why an optimal allocation cannot yet be made from the spreadsheet output.', 1, 'All the zeros can be covered by 3 lines (the Cara row and the Q and S columns), which is fewer than 4.', 16),
   ('b', 'Complete the Hungarian algorithm to find the allocation of cleaners to offices that minimises the total cleaning time.', 2, 'Ava S, Ben Q, Cara P, Dev R', 40),
   ('c', 'State the minimum total cleaning time.', 1, '108 minutes', 10)]),
 (A + ' Q16 · 9.05', 'Four volunteers, Kai, Lena, Mo and Nia, are each to be given a different job at a Geelong fun run: registration, water station, first aid or timing. The bipartite graph shows the jobs each volunteer is able to do.' + IMG('q16.png', 55),
  [('a', 'Which job must Mo be given?', 1, 'First aid', 10),
   ('b', 'List the two possible complete allocations of volunteers to jobs.', 1, 'Mo first aid, Lena water station, Nia registration, Kai timing; or Mo first aid, Lena water station, Nia timing, Kai registration', 18),
   ('c', 'Nia later finds that she cannot do timing. State the allocation that must be used, and explain why.', 1, 'Mo first aid, Lena water station, Nia registration, Kai timing. Lena must take the water station, so registration is Nia\'s only job left and Kai must do timing.', 18)]),
 (A + ' Q17 · 9.08', 'A school in Shepparton is building a new outdoor learning area. The activities, their durations and their immediate predecessors are shown in the table.'
  + T([['Activity', 'Duration (days)', 'Immediate predecessors'], ['A', '4', 'none'], ['B', '6', 'none'], ['C', '3', 'A'], ['D', '5', 'A'], ['E', '7', 'B, C'], ['F', '4', 'D'], ['G', '2', 'E, F'], ['H', '3', 'D']], True)
  + 'The project network for this project is shown below.' + IMG('q17.png', 85),
  [('a', 'Determine the earliest start time of activity <i>E</i>.', 1, '7 days', 10),
   ('b', 'Determine the minimum time needed to complete the project.', 1, '16 days', 10),
   ('c', 'State the critical path.', 1, 'A → C → E → G', 10),
   ('d', 'Determine the latest start time of activity <i>D</i>.', 1, '5 days', 10),
   ('e', 'Determine the float time of activity <i>H</i>.', 1, '4 days', 10),
   ('f', 'Activity <i>B</i> is delayed by 3 days. Decide whether this delays the project, and if so, by how long. Give a reason.', 1, 'Yes, by 2 days (to 18 days). Activity B has a float of only 1 day, so a 3 day delay exceeds its float by 2 days.', 16)]),
 (A + ' Q18 · 9.02', 'Water is pumped from a reservoir, <i>S</i>, to a town, <i>T</i>, through the network of pipes shown. The capacity of each pipe is in kilolitres per hour.' + IMG('q18.png', 55),
  [('a', 'Determine the capacity of the cut that separates <i>S</i> and <i>A</i> from <i>B</i>, <i>C</i> and <i>T</i>.', 1, '24', 12),
   ('b', 'Determine the maximum flow from the reservoir to the town, and identify the minimum cut.', 2, '22 kilolitres per hour; the minimum cut passes through pipes B → T and C → T.', 18),
   ('c', 'The council increases the capacity of pipe <i>C</i> → <i>T</i> by 5 kilolitres per hour. Determine the new maximum flow, and explain why the maximum flow does not increase by 5.', 1, '23 kilolitres per hour. The cut through A → C, B → C and B → T, with capacity 23, now becomes the minimum cut.', 18),
   ('d', 'An inspector wants to walk along every pipe exactly once, ignoring the direction of flow. Explain why the inspector cannot finish where they started, and state the two vertices where the walk must start and finish.', 2, 'Exactly two vertices, A and C, have odd degree (3), so an Eulerian trail exists but not an Eulerian circuit. The walk must start at A and finish at C, or the reverse.', 18)]),
 (A + ' Q19 · 9.06', 'Three delivery drivers (<i>D</i><sub>1</sub>, <i>D</i><sub>2</sub>, <i>D</i><sub>3</sub>) are to be assigned to three delivery zones (<i>Z</i><sub>1</sub>, <i>Z</i><sub>2</sub>, <i>Z</i><sub>3</sub>). The cost matrix (in dollars) is shown below. Apply the first step of the Hungarian algorithm (row reduction) and write the resulting matrix.'
  + T([['', 'Z1', 'Z2', 'Z3'], ['D1', '10', '14', '8'], ['D2', '6', '9', '12'], ['D3', '11', '7', '5']], True),
  [('', '', 2, 'Row minima: D1 8, D2 6, D3 5. Row-reduced matrix (rows D1 to D3, columns Z1 to Z3):' + T([['', 'Z1', 'Z2', 'Z3'], ['D1', '2', '6', '0'], ['D2', '0', '3', '6'], ['D3', '6', '2', '0']], True), 34)]),
 (A + ' Q20 · 9.10', 'A project network has activities with the following details.'
  + T([['Activity', 'Duration (days)', 'Predecessor', 'Crash cost per day ($)'], ['A', '8', '—', '200'], ['B', '5', '—', '150'], ['C', '6', 'A', '300'], ['D', '4', 'B', '250']], True)
  + 'The critical path is <i>A</i> → <i>C</i> with duration 14 days. The non-critical path <i>B</i> → <i>D</i> takes 9 days. Determine the cheapest way to reduce the project duration by 1 day and state the cost.',
  [('', '', 2, 'Crash activity A by 1 day at a cost of $200.', 16)]),
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
    out = [f'<div class="title"><div class="code">Ch 14<br>test</div><h1>Flow, matching and scheduling problems<div style="font-size:10pt;font-weight:normal;margin-top:1mm">14A–14E · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch14 test' + (' solutions' if sol else '')
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
