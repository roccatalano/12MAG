r"""Chapter deck: one HTML file with a tab per lesson deck (lessons/Ch<n>-slides.html), plus a combined PDF.

    python3 tools/deck/z10/chapter.py 1 S1 S2 S3 S4 S5          # -> lessons/Ch1-slides.html (+ Ch1-slides.pdf)
    python3 tools/deck/z10/chapter.py 2 S6 S7 S8 --no-pdf

Each lesson deck (lessons/<S#>-slides.html) is embedded whole and LAZY-LOADED: its iframe gets the deck only when its
tab is first shown. Never load them all at once: the decks' fit scripts (zstemfit, zfit, ...) measure the slides and
give wrong sizes inside a hidden iframe. The PDF is the lesson PDFs (lessons/<S#>-slides.pdf, vector prints from pdf.py) joined in order.
Rebuild the lesson decks (and their PDFs) first.
"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
LESSONS = os.path.join(ROOT, 'lessons')


def chapter(n, lessons, pdf=True):
    decks = [open(os.path.join(LESSONS, f'{s}-slides.html'), encoding='utf-8').read() for s in lessons]
    data = json.dumps(decks).replace('</', '<\\/')          # safe inside <script>
    btn = ''.join(f'<button onclick="show({i})" id="b{i}">{s}</button>' for i, s in enumerate(lessons))
    fr = ''.join(f'<iframe id="f{i}" title="{s} slides"></iframe>' for i, s in enumerate(lessons))
    html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>12MAG Chapter {n} slides</title>\n'
            '<style>body{margin:0;font-family:Arial,sans-serif;display:flex;flex-direction:column;height:100vh}\n'
            'nav{display:flex;gap:6px;padding:6px;background:#222}nav button{padding:6px 16px;font-size:15px;border:0;border-radius:4px;cursor:pointer}\n'
            'nav button.on{background:#2e7d32;color:#fff}iframe{flex:1;border:0;width:100%;display:none}nav span{color:#ccc;align-self:center;margin-left:auto;font-size:13px}</style></head>\n'
            f'<body><nav><b style="color:#fff;align-self:center;margin:0 8px">Chapter {n}</b>{btn}<span>Click inside a deck, then use the arrow keys</span></nav>{fr}\n'
            f'<script>const D={data};\n'
            'function show(n){for(let i=0;i<D.length;i++){document.getElementById("f"+i).style.display=i==n?"block":"none";document.getElementById("b"+i).className=i==n?"on":""}\n'
            ' const f=document.getElementById("f"+n);if(!f.srcdoc)f.srcdoc=D[n];f.focus();history.replaceState(null,"","#"+(n+1))}\n'
            'show(Math.max(0,Math.min(D.length-1,(+location.hash.slice(1)||1)-1)))</script></body></html>')
    out = os.path.join(LESSONS, f'Ch{n}-slides.html')
    open(out, 'w', encoding='utf-8').write(html)
    print(len(lessons), 'decks ->', os.path.relpath(out, ROOT), len(html))
    if pdf:
        from pypdf import PdfWriter, PdfReader
        w = PdfWriter(); k = 0
        for s in lessons:
            p = os.path.join(LESSONS, f'{s}-slides.pdf')
            for pg in PdfReader(p).pages: w.add_page(pg); k += 1
        w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)   # shared fonts once
        w.write(os.path.join(LESSONS, f'Ch{n}-slides.pdf'))
        print(k, 'pages ->', f'lessons/Ch{n}-slides.pdf')


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    if len(a) < 2:
        sys.exit(__doc__)
    chapter(a[0], a[1:], pdf='--no-pdf' not in sys.argv)
