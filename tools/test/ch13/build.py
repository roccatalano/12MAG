"""Chapter 13 test (13A-13F, graphs, networks and trees) + solutions, HTML + PDF in the CFAT layout. Model: tools/test/ch7/build.py.
Source (rule 9), copied verbatim: Mathspace General Maths 3&4 'Chapter 8 - Graphs and networks' topic assessment + answer key (all 20 Qs),
plus the Ch 13 (shortest path / Dijkstra) items of 'Chapter 9 - Applications of graphs and networks' topic assessment: Q3, Q4, Q5, Q10.
(02 Sources\\Textbooks\\Mathspace). Figures cropped from the PDFs (crop: see AoS4 #10 run); Q3 matrix and Q18b A^2 retyped as tables.
Answers = Mathspace answer keys (MSTs, Prim, Dijkstra values checked by hand). Ch 9 Q13 (cutting) and the rest of Ch 9 are left for the Ch 14 test.
Run: python3 tools/test/ch13/build.py lessons
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

A = 'Mathspace Ch 8 (graphs and networks) topic assessment'
B = 'Mathspace Ch 9 (applications of graphs and networks) topic assessment'
def ar(s): return s.replace('->', ' → ')
def MAT(rows, labs):
    return T([[''] + labs] + [[labs[i]] + r for i, r in enumerate(rows)], True)
Q3M = MAT([['0','1','1','0'],['1','0','2','1'],['1','2','0','0'],['0','1','0','0']], list('ABCD'))
MC = [
 (A + ' Q1 · 8.01', 'A simple graph has 5 vertices with degrees 1, 2, 3, 3, 3. How many edges does this graph have?', ['12', '6', '7', '5'], 1),
 (A + ' Q2 · 8.01', 'Which of the following best describes a directed graph (digraph)?', ['A graph where every vertex has the same degree.', 'A graph that can be drawn without any edges crossing.', 'A graph where every vertex is connected to every other vertex.', 'A graph where edges have a specified direction of travel.'], 3),
 (A + ' Q3 · 8.02', 'The adjacency matrix below represents an undirected graph. What is the degree of vertex <i>B</i>?' + Q3M, ['3', '5', '2', '4'], 3),
 (A + ' Q4 · 8.03', 'Two graphs are isomorphic if they have the same number of vertices and edges, and the same degree sequence. Which degree sequence would make two graphs potentially isomorphic to a graph with degree sequence {1, 2, 2, 3}?', ['{1, 2, 2, 3}', '{2, 2, 2, 2}', '{1, 2, 3, 3}', '{1, 1, 3, 3}'], 0),
 (A + ' Q5 · 8.04', 'A connected planar graph has 9 vertices and 14 edges. How many faces does it have?', ['8', '7', '6', '5'], 1),
 (A + ' Q6 · 8.06', 'Consider the graph shown. Which of the following is a valid walk from <i>A</i> to <i>D</i>?' + IMG('q6.png', 32), [ar('A->C->D'), ar('A->D->B'), ar('A->E->B->D'), ar('A->C->E->D')], 3),
 (A + ' Q7 · 8.09', 'Which of the following is a property of a tree?', ['A tree with <i>n</i> vertices has exactly <i>n</i> edges.', 'A tree is a connected graph with no cycles.', 'A tree must have at least one vertex of degree greater than two.', 'A tree is a connected graph with exactly one cycle.'], 1),
 (A + ' Q8 · 8.10', 'A weighted graph has the following edges and weights: <i>AB</i> = 4, <i>AC</i> = 7, <i>BC</i> = 2, <i>BD</i> = 5, <i>CD</i> = 3. What is the total weight of the minimum spanning tree?', ['11', '14', '21', '9'], 3),
 (A + ' Q9 · 8.05', 'The complete graph <i>K</i><sub>5</sub> has 5 vertices. How many edges does it have?', ['20', '12', '10', '8'], 2),
 (B + ' Q3 · 9.03', 'The weighted graph below shows travel times in minutes between suburbs. By inspection, what is the shortest travel time from <i>A</i> to <i>D</i>?' + IMG('n3.png', 34), ['13', '9', '10', '7'], 1),
 (B + ' Q4 · 9.04', "In Dijkstra's algorithm, when a node is finalised (permanently labelled), it means:", ['The node is the sink of the network', 'The shortest path to that node has been determined and will not change', 'All edges from that node have been removed from the graph', 'The node has been visited but may be updated later'], 1),
 (B + ' Q5 · 9.04', "Using Dijkstra's algorithm on the network shown, what is the shortest distance from <i>A</i> to <i>D</i>?" + IMG('n5.png', 30), ['10', '9', '12', '7'], 1),
]
SQ = '<span style="display:inline-grid;grid-template-columns:repeat(5,7mm);border-left:1px solid #000;border-right:1px solid #000;padding:0 1mm;text-align:center">' + ''.join(f'<span>{x}</span>' for x in '3 1 3 1 2 1 3 1 3 2 3 1 3 1 2 1 3 1 3 2 2 2 2 2 4'.split()) + '</span>'
SA = [
 (A + ' Q10 · 8.02', 'Construct the adjacency matrix for the undirected graph shown.' + IMG('q10.png', 40),
  [('', '', 2, MAT([['0','1','0','1'],['1','0','1','2'],['0','1','0','1'],['1','2','1','0']], list('ABCD')), 34)]),
 (A + ' Q11 · 8.03', 'Determine whether the two graphs shown are isomorphic. Justify your answer.' + IMG('q11.png', 50),
  [('', '', 2, 'Yes, the graphs are isomorphic. The mapping A → Q, B → P, C → S, D → R sends every edge of the first graph to an edge of the second.', 22)]),
 (A + ' Q12 · 8.04', "A connected planar graph has <i>v</i> = 7 vertices and <i>f</i> = 6 faces. Use Euler's formula to find the number of edges.",
  [('', '', 2, '<i>v</i> − <i>e</i> + <i>f</i> = 2 → 7 − <i>e</i> + 6 = 2 → <i>e</i> = 11', 18)]),
 (A + ' Q13 · 8.09', 'Determine whether the graph below is a tree. Give a reason for your answer.' + IMG('q13.png', 40),
  [('', '', 1, 'No, the graph is not a tree because it contains a cycle (B → C → D → B).', 14)]),
 (A + ' Q14 · 8.07', 'A graph has 4 vertices each of degree 3. Determine whether this graph has an Eulerian circuit, an Eulerian trail, or neither.',
  [('', '', 1, 'Neither. All four vertices have odd degree (3), giving 4 odd-degree vertices.', 14)]),
 (A + ' Q15 · 8.10', 'The weighted graph below shows distances (in km) between five towns. By inspection, identify the minimum spanning tree and state its total weight.' + IMG('q15.png', 36),
  [('', '', 3, 'Minimum spanning tree edges: D–E (2), B–C (3), A–C (4), C–D (5). Total weight 14 km.', 24)]),
 (A + ' Q16 · 8.05', 'The network shows the walking tracks between six locations, <i>P</i>, <i>Q</i>, <i>R</i>, <i>S</i>, <i>T</i> and <i>U</i>, in a national park.' + IMG('q16.png', 45),
  [('a', 'Rangers would like every pair of locations to be joined directly by a track. How many additional tracks would be needed?', 1, '9', 12),
   ('b', 'Identify the two bridges in the network.', 2, 'R–T and T–U', 12),
   ('c', 'Track <i>T</i>–<i>U</i> is closed after a storm. Explain the effect of this closure on walkers in the park.', 1, 'Location U can no longer be reached from any other location; because T–U is a bridge, the network becomes disconnected.', 14)]),
 (A + ' Q17 · 8.11', 'A Mildura vineyard will lay irrigation pipes from its pump, <i>P</i>, to five blocks, <i>A</i>, <i>B</i>, <i>C</i>, <i>D</i> and <i>E</i>. The network shows the possible pipe routes and their lengths, in metres.' + IMG('q17.png', 50),
  [('a', "Using Prim's algorithm, starting at <i>P</i>, list the pipes in the order they are added to the minimum spanning tree.", 2, 'P–A, A–C, C–B, C–D, C–E', 16),
   ('b', 'State the minimum total length of pipe needed.', 1, '590 m', 10),
   ('c', 'Pipe costs $38 per metre to lay. Calculate the cost of laying the pipes in the minimum spanning tree.', 1, '$22 420', 10),
   ('d', 'The owner decides that the pipe <i>P</i>–<i>C</i> must be included. Determine the minimum total length of pipe now needed.', 1, '640 m', 12),
   ('e', 'Explain why every spanning tree for this network has exactly five pipes.', 1, 'The network has 6 vertices and a tree with n vertices has n − 1 edges; a sixth pipe would create a cycle.', 14)]),
 (A + ' Q18 · 8.08', 'A tourist staying at a hotel (<i>H</i>) in the Yarra Valley plans to visit a winery (<i>W</i>), a lake (<i>L</i>), a gallery (<i>G</i>) and a market (<i>M</i>). The network shows the roads between these places and the travel times, in minutes.' + IMG('q18.png', 45),
  [('a', 'Write the adjacency matrix for this network, with rows and columns in the order <i>H</i>, <i>W</i>, <i>L</i>, <i>G</i>, <i>M</i>.', 1, MAT([['0','1','0','1','1'],['1','0','1','0','1'],['0','1','0','1','1'],['1','0','1','0','1'],['1','1','1','1','0']], list('HWLGM')), 40),
   ('b', 'The square of the adjacency matrix, calculated with a CAS, is shown below.<br>' + SQ + '<br>State the number of two-step routes from the hotel to the lake.', 1, '3', 10),
   ('c', 'Explain why the tourist cannot travel along every road exactly once.', 1, 'Four vertices (H, W, L and G) have odd degree, but an Eulerian trail needs exactly 0 or 2 vertices of odd degree.', 14),
   ('d', 'Write a Hamiltonian cycle that starts and finishes at the hotel.', 1, 'For example, H → W → L → G → M → H', 10),
   ('e', 'Find the Hamiltonian cycle that starts and finishes at the hotel and has the shortest total travel time, and state this time.', 1, 'H → W → M → L → G → H (or the reverse), 75 minutes', 12),
   ('f', 'The tourist says that the cycle in part e uses every road in the network. Decide whether the tourist is correct. Give a reason.', 1, 'Not correct. A Hamiltonian cycle visits every vertex once, not every road; it uses only 5 of the 8 roads.', 14)]),
 (A + ' Q19 · 8.06', 'State whether each of the following walks on the graph below is a trail, a path, or neither. The graph has edges: <i>A</i>–<i>B</i>, <i>B</i>–<i>C</i>, <i>C</i>–<i>D</i>, <i>D</i>–<i>A</i>, <i>A</i>–<i>C</i>.',
  [('a', ar('A->B->C->A->D'), 1, 'Trail (no edge repeated, but vertex A is repeated, so it is not a path).', 10),
   ('b', ar('A->C->B->A->D'), 1, 'Trail (no edge repeated, but vertex A is repeated, so it is not a path).', 10)]),
 (A + ' Q20 · 8.08', 'Consider the graph shown. Determine whether a Hamiltonian cycle exists. If it does, state one such cycle.' + IMG('q20.png', 36),
  [('', '', 2, 'Yes, a Hamiltonian cycle exists. One example is A → B → C → D → E → A.', 16)]),
 (B + ' Q10 · 9.03', 'The network below shows distances in kilometres between locations in regional Victoria. By inspection, find a shortest path from <i>A</i> to <i>F</i> and state its length.' + IMG('n10.png', 40),
  [('', '', 2, 'The shortest length is 14 km. Each of A → B → D → F, A → B → E → F and A → C → E → F has this length.', 16)]),
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
    out = [f'<div class="title"><div class="code">Ch 13<br>test</div><h1>Graphs, networks and trees<div style="font-size:10pt;font-weight:normal;margin-top:1mm">13A–13F · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{tot}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(MC)} marks</span></div>']
    for i in range(0, len(MC), 2):
        out.append('<div class="qgrid" style="margin-bottom:3mm">' + mcbox(i + 1, MC[i]) + (mcbox(i + 2, MC[i + 1]) if i + 1 < len(MC) else '') + '</div>')
    out.append(f'<div class="secthd">Section B · Short answer<span>Show your working. {tot - len(MC)} marks</span></div>')
    for j, q in enumerate(SA): out.append(sabox(len(MC) + 1 + j, q))
    t = 'Ch13 test' + (' solutions' if sol else '')
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
