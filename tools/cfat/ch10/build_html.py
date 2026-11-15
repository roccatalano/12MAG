"""HTML + PDF versions of CFAT 3.10.1-3.10.3 (copied from tools/cfat/ch5; MC questions are whole cropped images with the options inside), same layout and CSS as CFAT 1.1.x (Rocco, 15 Nov: CFATs are
HTML + PDF, not Word). Content (questions, answers, sources) comes from build.py's CFATS list.
Run: python3 build_html.py <lessons dir>  -> CFAT 1.5.x (5X-5Y).html/.pdf + solutions .html/.pdf
"""
import sys, os, base64, html
from build import CFATS, FIG
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'cfat.css')).read() + """
.mc .ok{color:#c00;font-weight:bold;display:none} .sol .mc div.right .ok{display:inline}
body{font-size:9pt;line-height:1.2} .title{padding:1.5mm 3mm} .title h1{font-size:13pt} .box>.hd{padding:.6mm 3mm} .box>.bd{padding:1.5mm 2.5mm} .q{margin:0 0 1mm}
.sol .mc div.right span{color:#c00;font-weight:bold}
.colstack{display:flex;flex-direction:column;gap:2.5mm} .colstack .box{flex:1}
.sa .part .ans{margin-top:1mm}
table.ct th,table.ct td{padding:.4mm .6mm} table.ct th{width:24%}
.mcl .ok{display:none} .sol .mcl .right{color:#c00;border:1.5px solid #c00;border-radius:50%;padding:0 1.2mm} .sol .mcl .right .ok{display:inline}
.box>.bd .fig img{max-width:100%}
.sa{grid-template-columns:minmax(0,1fr)} .sa>.stem{border-right:none;border-bottom:1.2px solid #000;padding:1.5mm 3mm} .sa>.stem .fig{text-align:left}
.sa>.parts{display:grid;grid-template-columns:1fr 1fr} .sa .part{border-bottom:1px dashed #bbb!important} .sa .part:nth-child(odd){border-right:1px dashed #bbb}
"""
E = html.escape
def img(k, mm): return f'<img src="data:image/png;base64,{base64.b64encode(open(FIG(k),"rb").read()).decode()}" style="width:{mm}mm">'
def tbl(rows): return '<table class="t ct" style="font-size:7.8pt;width:100%;table-layout:fixed">' + ''.join('<tr>' + ''.join((f'<th class="l">{E(c)}</th>' if j == 0 else f'<td>{E(c)}</td>') for j, c in enumerate(r)) + '</tr>' for r in rows) + '</table>'
def paras(t): return ''.join(f'<p class="q">{E(l)}</p>' for l in t.split('\n')) if t else ''
def mm(cm): return round(cm * 10 * 0.85)

def mcbox(n, q, half=False):
    letters = ''.join(f'<span style="margin-right:9mm;" class="{"right" if i == q["ans"] else ""}"><b>{"ABCD"[i]}</b><i class="ok"> ✓</i></span>' for i in range(4))
    src = q['src'].replace('Edrolo ', 'Edrolo U3&amp;4 ')
    return (f'<div class="box" style="break-inside:avoid"><div class="hd">Question {n}<span>1 mark</span></div><div class="bd"><div class="fig">{img(q["fig"], mm(q["w"]))}</div>'
            f'<div class="mcl" style="margin-top:1mm">Circle: {letters}</div><div class="cite">{src}</div></div></div>')

def sabox(n, q):
    marks = sum(p[2] for p in q['parts'])
    stem = ''.join(f'<p class="q">{E(l)}</p>' for l in q['stem'].split('\n'))
    if q.get('fig'): stem += f'<div class="fig">{img(q["fig"], mm(q["w"]))}</div>'
    if q.get('table'): stem += tbl(q['table'])
    stem += paras(q.get('stem2'))
    src = q['src'].replace('Edrolo ', 'Edrolo U3&amp;4 ')
    parts = ''
    for p in q['parts']:
        lab, txt, mk, ans = p[:4]
        t = '<br>'.join(E(x) for x in txt.split('\n')) if txt else ''
        fig = (tbl(p[4]) if isinstance(p[4], list) else f'<div class="fig">{img(p[4], mm(p[5]))}</div>') if len(p) > 4 else ''
        parts += (f'<div class="part" style="flex:{mk}"><div class="pq"><b>{E(lab.rstrip("."))}</b><span>{t} <span style="color:#555;font-size:8.5pt">({mk} mark{"s" if mk > 1 else ""})</span></span></div>'
                  f'{fig}<div class="blank" style="min-height:{3 + 2.5 * mk}mm"><div class="ans">{'<br>'.join(E(x) for x in ans.split(chr(10)))}</div></div></div>')
    return (f'<div class="box"><div class="hd">Question {n}<span>{marks} mark{"s" if marks > 1 else ""}</span></div>'
            f'<div class="sa"><div class="stem">{stem}<div class="cite">{src}</div></div><div class="parts">{parts}</div></div></div>')

def page(c, sol):
    mcs = c['mc']; total = len(mcs) + sum(p[2] for q in c['sa'] for p in q['parts'])
    subs = c['subs'].replace('-', '–')
    out = [f'<div class="title"><div class="code">CFAT<br>{c["id"][5:]}</div><h1>{E(c["title"])}<div style="font-size:10pt;font-weight:normal;margin-top:1mm">{subs} · CAS and bound reference allowed{" · <b style=color:#c00>SOLUTIONS</b>" if sol else ""}</div></h1><div class="who"><div><b>Name</b> <i></i></div><div class="sc">/{total}</div></div></div>',
           f'<div class="secthd">Section A · Multiple choice<span>Circle one answer. {len(mcs)} marks</span></div>']
    for row in c['layout']:
        if row[0] == 'full': out.append(mcbox(row[1] + 1, mcs[row[1]]))
        else:
            cols = ['<div class="colstack">' + ''.join(mcbox(i + 1, mcs[i], True) for i in col) + '</div>' for col in row]
            out.append('<div class="qgrid">' + ''.join(cols) + '</div>')
    secB=(f'<div class="secthd" style="margin-top:2mm">Section B · Short answer<span>Show your working. {total - len(mcs)} marks</span></div>')
    n = len(mcs) + 1
    for i, q in enumerate(c['sa']):
        out.append(('<div style="break-inside:avoid">' + secB + sabox(n, q) + '</div>') if i == 0 else sabox(n, q)); n += 1
    out = [o.replace('s_x', 's<sub>x</sub>').replace('s_y', 's<sub>y</sub>') for o in out]
    t = f'{c["id"]} ({c["subs"]})' + (' solutions' if sol else '')
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{t}</title><style>{CSS}</style>'
            f'<script src="a4view.js"></script><script src="paged.polyfill.min.js"></script></head><body class="{"sol" if sol else ""}">\n'
            + '\n'.join(out) + '\n</body></html>'), t

if __name__ == '__main__':
    out = sys.argv[1]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for c in CFATS:
            for sol in (False, True):
                h, t = page(c, sol)
                f = os.path.join(out, t + '.html'); open(f, 'w').write(h)
                pg = b.new_page(); pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(2500)
                pg.pdf(path=os.path.join(out, t + '.pdf'), prefer_css_page_size=True, print_background=True)
                pg.close(); print(t)
        b.close()
