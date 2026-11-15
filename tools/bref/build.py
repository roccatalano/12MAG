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

DL = ('<style>.dl{position:fixed;top:10px;right:14px;z-index:9;font:700 13px Inter,Arial,sans-serif;background:#2f6fdf;color:#fff;'
      'text-decoration:none;padding:7px 12px;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.25)}@media print{.dl{display:none}}</style>')

def doc(title, subs):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style>{DL}{MJ}{READY}</head><body><a class="dl" href="{title}.pdf" download>Download PDF ⬇</a>{pages(subs)}</body></html>')

def write(name, html):
    with open(os.path.join(OUT, name), 'w') as f: f.write(html)
    print('wrote', name)

def pdfs(names):
    """Print each html to an A4 PDF next to it (waits for MathJax: body[data-fit])."""
    import asyncio
    from playwright.async_api import async_playwright
    async def run():
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
            pg = await b.new_page()
            for n in names:
                await pg.goto('file://' + os.path.join(OUT, n + '.html'))
                await pg.wait_for_selector('body[data-fit]', timeout=30000)
                await pg.pdf(path=os.path.join(OUT, n + '.pdf'), format='A4', prefer_css_page_size=True, print_background=True)
                print('pdf', n)
            await b.close()
    asyncio.run(run())

if __name__ == '__main__':
    names = []
    for s in CARDS:
        write(f'{s} bound reference.html', doc(f'{s} bound reference', [s])); names.append(f'{s} bound reference')
    for name, subs in LESSONS.items():
        write(f'{name} bound reference.html', doc(f'{name} bound reference', subs)); names.append(f'{name} bound reference')
    if '--no-pdf' not in sys.argv:
        pdfs(names)
