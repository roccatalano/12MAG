# Chapter 14 revision booklet: Insight GM1 Unit 4 (MC) + GM2 Unit 4 (SA), section 'Networks and decision mathematics—
# Directed graphs: flow, matching and critical path analysis' (GM1 Q1-26 except Q4, printed pp.24-30 = pdf 25-31;
# GM2 Q1-13, printed pp.29-39 = pdf 30-40), plus GM1 undirected-section Q19 (allocation, printed p.23) left over from Ch 13.
# GM1 Q4 (shortest path) was used in the Ch 13 booklet. Questions are scans of the Insight pages (crop.py -> crops/*.png),
# verbatim; GM2 crops keep Insight's own answer lines and boxes. Answers from Insight's explanatory notes / worked
# solutions (GM1 pp.44-49, GM2 pp.50-56). Insight is never burnt.
G1 = 'Insight GM1 Unit 4'
G2 = 'Insight GM2 Unit 4'
NSEG = {'d5': 2, 'd17': 2, 'd24': 2, 'g2': 2, 'g6': 2, 'g7': 2, 'g10': 2, 'g12': 2, 'g13': 2}


def segs(k):
    return ''.join(f'[[{k if i == 0 else f"{k}_{i + 1}"}]]' for i in range(NSEG.get(k, 1)))


def MC(n, sub, page, a, why, info=None, key=None, shared=None):
    key = key or f'd{n}'
    stem = (segs(info) if info else '') + segs(key)
    return dict(kind='mc', n=n, sub=sub, stem=stem, opts=None, a='ABCDE'.index(a), why=why, src=f'{G1} p.{page} Q{n}', shared=shared)


def SX(n, sub, page, marks, ans):
    """Whole short-answer question as Insight prints it (with its answer lines); ans = worked answers per part (solutions copy)."""
    return dict(kind='sx', n=n, sub=sub, marks=marks, stem=segs(f'g{n}'), ans=ans, src=f'{G2} p.{page} Q{n}')


SUBS = [('14A', 'Flow problems'), ('14B', 'Matching and allocation problems'), ('14C', 'Precedence tables and activity networks'),
        ('14D', 'Critical path analysis'), ('14E', 'Crashing')]
EMPTY = {}
I67, I810, I1113, I1415, I1718, I1920 = ('Q6–7', 'Q8–10', 'Q11–13', 'Q14–15', 'Q17–18', 'Q19–20')

Q = [
 # 14A flow (and directed-graph reachability)
 MC(1, '14A', 24, 'B', 'The minimum cut (or tracking the flow through the network) gives a maximum flow of 14.'),
 MC(2, '14A', 24, 'A', 'Maximum flow = capacity of the minimum cut = 12 (Insight shows it by tracking the flow).'),
 MC(3, '14A', 24, 'C', 'Tracking the flow through the graph gives 15; a cut of capacity 15 confirms it.'),
 MC(14, '14A', 26, 'B', 'Cut A: 4 + 9 = 13; Cut B: 4 + 3 + 1 + 4 = 12 (2 is a double cut); Cut C: 6 + 3 + 1 + 4 = 14; Cut D: 5 + 4 + 3 = 12; Cut E: 10 + 3 = 13. One cut of 14.', info='i14', shared=I1415),
 MC(15, '14A', 26, 'B', 'The minimum cut has capacity 4 + 4 + 3 = 11 litres per minute.', info='i14', shared=I1415),
 MC(22, '14A', 28, 'D', 'A: C–D–G–B–A; B: D–G–B; C: G–B–C–E; D: no path reaches I from F (not possible); E: B–D–G.'),
 MC(23, '14A', 28, 'A', 'Minimum cut = 8 cars per minute, so the maximum flow is 8.'),
 SX(1, '14A', 29, 1, '118 children (minimum cut / tracking through the network; Insight GM2 p.50).'),
 SX(2, '14A', 29, 2, '<b>a</b> 23 + 26 + 36 + 42 = 127 (the backwards edge, 16, is not counted)<br><b>b</b> 70 litres per hour'),
 SX(9, '14A', 35, 3, '<b>a</b> 7 routes<br><b>b</b> 4 + 3 + 2 + 5 + 6 = 20 people<br><b>c</b> 7 people per minute (minimum cut 2 + 2 + 3)'),
 # 14B matching / Hungarian algorithm
 MC(19, '14B', 23, 'A', 'Row reduction then column reduction gives E 2 0 0 2 / R 2 1 0 0 / M 0 4 2 1 / L 1 0 2 0: E does task 2 or 3, R 3 or 4, M 1, L 2 or 4. Allocations I and II both work (33 days).', key='u19'),
 MC(5, '14B', 24, 'A', 'Hungarian algorithm (row, then column reduction, cover the zeros, adjust): in both optimal allocations Adam does Job 1.'),
 MC(16, '14B', 26, 'B', 'Row then column reduction and allocating with the zeros: Andy Task 1, Daisy Task 3, Callum Task 2, Bertha Task 4.'),
 MC(24, '14B', 29, 'C', 'Reduce the columns (subtract the lowest value in each column), cover the zeros and allocate: Merindah 1, Yvonne 3, Jackie 2, Ryder 4.', key='d24'),
 SX(3, '14B', 30, 3, '<b>a</b> After row and column reduction: Al 0 5 7 0 / Br 2 0 0 0 / Ch 1 7 7 0 / Da 1 0 1 0 (4 lines cover the zeros)<br>'
    '<b>b</b> Alistair Addressing, Brianna Packaging, Christine Sorting, Danielle Weighing: 22 + 32 + 16 + 30 = 100 minutes'),
 SX(7, '14B', 33, 3, '<b>a</b> Package remaining goods for sale the next day (Adriano: ovens, Tiana: floors, Vish: surfaces)<br>'
    '<b>b</b> Jess (24) and Adriano (26) work at the same time; then Vish disinfects (36), then Tiana sweeps (43): 26 + 36 + 43 = 105 minutes'),
 SX(11, '14B', 36, 1, 'A Jamal · B Campbell · C Brooke · D Leith'),
 # 14C precedence tables, activity networks, dummies
 MC(6, '14C', 25, 'B', 'The dummy shows that activity J needs both E and F, while activity H needs only E.', info='i6', shared=I67),
 MC(11, '14C', 26, 'D', 'Activities A, B, C and E all occur before activity H; activity D has no effect on H.', info='i11', shared=I1113),
 MC(17, '14C', 27, 'D', 'An immediate predecessor of M is C, so C must be joined to the start of L and M: the dummy connects the end of C and the start of K.', info='i17', key='d17', shared=I1718),
 # 14D critical path analysis
 MC(8, '14D', 25, 'C', 'Forward scanning: the earliest start time for G is 14 days.', info='i8', shared=I810),
 MC(9, '14D', 25, 'E', 'Longest path through the network: 29 days.', info='i8', shared=I810),
 MC(10, '14D', 25, 'D', 'Float times: B = 3, C = 11, F = 2, H = 5, I = 10, J = 5: activity I has the greatest float.', info='i8', shared=I810),
 MC(12, '14D', 26, 'E', 'Backward scanning gives the latest start time of D as 12.', info='i11', shared=I1113),
 MC(13, '14D', 26, 'D', 'The critical path is C–F–I–J; minimum completion time 28 days.', info='i11', shared=I1113),
 MC(18, '14D', 27, 'C', 'Critical path B–G–K–L–N–O, 23 weeks, so A and B are true. If M increases to 8, 13 + 8 = 21: not on the critical path (D true). F has float 7 − 5 = 2 weeks, so A can be delayed 2 weeks (E true). The latest start of F is 13 − 3 = 10, not 13.', info='i17', shared=I1718),
 MC(19, '14D', 27, 'E', 'Critical path B–D–I–J takes 15 days.', info='i19', shared=I1920),
 MC(21, '14D', 28, 'B', 'Activity F starts at 6 days at the latest and lasts 4 days, so it must finish after 10 days.'),
 MC(25, '14D', 29, 'B', 'Float times of activities off the critical path: 2, 4 and 6 weeks, and activity M has a float of 3: x = 3.'),
 MC(26, '14D', 30, 'D', 'Paths: A–D–F–J–M 18, A–C–I–J–M 13, A–C–H–J–M 13, B–E–G–J–M 17, B–E–K–M 12. G must increase by 4 days to make 21 days: 3 + 4 = 7.'),
 SX(6, '14D', 32, 5, '<b>a</b> 20 days<br><b>b</b> C – E – H – K – L<br><b>c</b> 4 activities<br><b>d</b> Draw X (3 days) from the end of activity G (EST 13) to the finish so that its LST is 24 (Insight GM2 p.53 draws it)<br><b>e</b> 34 days'),
 SX(8, '14D', 34, 5, '<b>a</b> 28 weeks<br><b>b</b> 6 activities (B, C, E, F, G, I)<br><b>c</b> 9 weeks<br><b>d i</b> Draw L, 4 so that it can start after 8 weeks and finish by 26 (Insight GM2 p.54 draws it)<br><b>d ii</b> No change: 28 weeks'),
 SX(12, '14D', 37, 4, '<b>a</b> I, K and L<br><b>b</b> A – E – I – K – L drawn on the diagram<br><b>c</b> 17 days (the dummy does not change the minimum completion time)<br>'
    '<b>d</b> Friday 18 January (EST of G = 3 days, LST = 4 days)'),
 # 14E crashing
 MC(7, '14E', 25, 'D', 'With F reduced to 12 days, the longest path through the network (the critical path) is 34 days (Insight GM1 p.46).', info='i6', shared=I67),
 MC(20, '14E', 28, 'C', 'Only reducing activities on every 15-day path brings the project to 12 days: reduce I by 3 days (BDIJ and BCFIJ both go to 12).', info='i19', shared=I1920),
 SX(4, '14E', 31, 5, '<b>a</b> 4 days<br><b>b</b> A – E – I – K, 37 days<br><b>c</b> B and F<br>'
    '<b>d</b> Activities E, F and G are all predecessors of one activity, but only E and F are required for activity J: the dummy shows this.<br>'
    '<b>e</b> $8000 (crash E and J; the project then takes 35 days)'),
 SX(5, '14E', 32, 6, '<b>a</b> A, B, C, E and F<br><b>b</b> A – E – G – K, 27 days<br><b>c</b> 17 − 8 = 9 days<br>'
    '<b>d i</b> 23 days (crash E and G by 2 days each, and F by 1 day)<br><b>d ii</b> 4000 + 4000 + 2000 = $10 000'),
 SX(10, '14E', 35, 5, '<b>a</b> B – G – H – J – M<br><b>b</b> 9 − 6 = 3 weeks<br><b>c</b> C (C – F – K – M becomes 20 weeks)<br>'
    '<b>d</b> H, J and K are reduced (or E and K): new minimum completion time 17 weeks'),
 SX(13, '14E', 38, 2, '<b>a</b> 15 days (reduce J, K and L)<br><b>b</b> 200 + 2 × 150 + 2 × 250 = $1000'),
]
