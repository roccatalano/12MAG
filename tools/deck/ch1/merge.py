"""Merge the Chapter 1 lesson decks (S1–S5) into one deck: lessons/Ch1 slides.html (+ PDF).

Rocco, 16 Nov 2026: Do Now slides are off the decks (Do Now lists stay on the planner cards);
one merged Chapter 1 deck for testing, the per-lesson decks stay linked to their lessons.
Run after rebuilding the lesson decks:  python3 tools/deck/ch1/merge.py [--pdf]
"""
import os, re, sys, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, f'{ROOT}/tools/deck/tpl')
import tpl

DECKS = ['S1', 'S2', 'S3', 'S4', 'S5']
OUT = f'{ROOT}/lessons/Ch1 slides.html'

tpl.assemble([], 'X', '/tmp/_empty_engine.html')
E = open('/tmp/_empty_engine.html', encoding='utf-8').read()

def segment(path):
    f = re.sub(r'<title>.*?</title>', '<title>X</title>', open(path, encoding='utf-8').read(), count=1)
    i = 0
    while i < len(E) and f[i] == E[i]: i += 1
    j = 0
    while j < len(E) - i and f[-1 - j] == E[-1 - j]: j += 1
    assert i + j == len(E), f'{path}: not built on the current engine (rebuild it first)'
    return f[i:len(f) - j]

seen, parts = set(), []
for d in DECKS:
    g = segment(f'{ROOT}/lessons/{d}-slides.html')
    ids = set(re.findall(r'\bid="([^"]+)"', g))
    for x in sorted(ids & seen):          # same id in an earlier deck: give this deck's copy a prefix
        if x == 'cfatT': continue          # CFAT timer: handled by the patch below
        y = f'{d.lower()}-{x}'
        g = re.sub(rf'\bid="{re.escape(x)}"', f'id="{y}"', g)
        g = re.sub(rf'#{re.escape(x)}(?=[|;"\'\s,)\]])', f'#{y}', g)
    seen |= ids
    parts.append(g)

h = E.replace('<title>X</title>', '<title>12MAG Chapter 1 · Investigating data distributions · slides</title>', 1)
cut = len(E) - len(E.split('<!--SLIDES-->')[-1]) if '<!--SLIDES-->' in E else None
# the empty engine is head + tail; find the join with the S1 file
s1 = open(f'{ROOT}/lessons/S1-slides.html', encoding='utf-8').read()
s1 = re.sub(r'<title>.*?</title>', '<title>X</title>', s1, count=1)
i = 0
while s1[i] == E[i]: i += 1
head, tail = h[:i + (len(h) - len(E))], h[i + (len(h) - len(E)):]
# CFAT timer: several CFAT slides now share one deck, so look inside the slide on screen
tail = tail.replace("document.getElementById('cfatT')", "(document.querySelector('.slide.on #cfatT')||document.getElementById('cfatT'))")
open(OUT, 'w', encoding='utf-8').write(head + '\n'.join(parts) + tail)
n = sum(len(re.findall(r'<section|class="slide[ "]', p)) for p in parts)
print('wrote', OUT)
if '--pdf' in sys.argv:
    subprocess.run(['python3', f'{ROOT}/tools/deck/pdf.py', OUT, OUT[:-5] + '.pdf'], check=True)
