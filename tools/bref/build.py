"""Bound reference entries: one card per subchapter (half or full A4), cut lines, colour.
Writes lessons/<sub> bound reference.html for each sub + a combined file for each lesson.
Usage: python3 tools/bref/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cards import CARDS, LESSONS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'lessons')
CSS = open(os.path.join(os.path.dirname(__file__), 'bref.css')).read()
MJ = ('<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]],displayMath:[["\\\\[","\\\\]"]]},svg:{fontCache:"global"}};</script>'
      '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>')


READY = "<script>addEventListener('load',()=>setTimeout(()=>document.body.dataset.fit=1,800))</script>"

def card(sub):
    c = CARDS[sub]
    return (f'<div class="slot {c["size"]}"><div class="cut"><span class="sc">&#9986;</span>'
            f'<div class="card"><div class="hd"><span class="code">{sub}</span><span class="tt">{c["title"]}</span>'
            f'<span class="sd">{c["sd"]}</span></div><div class="bd">{c["body"]}</div>'
            f'<div class="ft">{c["cite"]}</div></div></div></div>')

def pages(subs):
    out, half = [], None
    for s in subs:
        if CARDS[s]['size'] == 'full':
            out.append([s])
        elif half is None:
            half = [s]; out.append(half)
        else:
            half.append(s); half = None
    return ''.join('<div class="page">' + ''.join(card(s) for s in p) + '</div>' for p in out)

def doc(title, subs):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style>{MJ}{READY}</head><body>{pages(subs)}</body></html>')

def write(name, html):
    with open(os.path.join(OUT, name), 'w') as f: f.write(html)
    print('wrote', name)

if __name__ == '__main__':
    for s in CARDS:
        write(f'{s} bound reference.html', doc(f'{s} bound reference', [s]))
    for name, subs in LESSONS.items():
        write(f'{name} bound reference.html', doc(f'{name} bound reference', subs))
