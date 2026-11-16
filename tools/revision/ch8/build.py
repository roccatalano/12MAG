"""Build the Ch8 revision booklet (copied from ch14/build.py) from qdata.py. Writes student + solutions HTML.
Figures: crops of the Insight pages (crop.py -> crops/*.png)."""
import json, re, base64, sys, os
A4VIEW = '--print' not in sys.argv  # screen copies get the A4 page view; --print builds the plain copy used for PDFs
sys.path.insert(0, '.')
from qdata import Q, SUBS, EMPTY

os.chdir(os.path.dirname(os.path.abspath(__file__)))
LOADER = ("document.addEventListener('DOMContentLoaded',()=>{if(!matchMedia('screen').matches)return;const d=document.createElement('div');d.id='a4load';"
          "d.style.cssText='position:fixed;inset:0;z-index:99999;background:#6b6b6b;color:#fff;font:600 16px Arial;display:flex;align-items:center;justify-content:center';"
          "d.textContent='Loading A4 pages…';document.documentElement.appendChild(d)});"
          "window.__a4done=()=>{const d=document.getElementById('a4load');if(d)d.remove()};")

WID = {'a10': 58, 'ia20': 92}

def subfigs(html, sol, small=False):
    def r(m):
        k = m.group(1)
        b = base64.b64encode(open(f'crops/{k}.png', 'rb').read()).decode()
        from PIL import Image
        w = WID.get(k) or Image.open(f'crops/{k}.png').width / 220 * 25.4 * 0.92
        return f'<div class="fig"><img src="data:image/png;base64,{b}" style="width:{w:.0f}mm;max-width:100%"></div>'
    return re.sub(r'\[\[(\w+)\]\]', r, html)

EXTRA = """
.sxa{visibility:hidden;color:#c00;font-size:9.5pt;margin-top:1mm;line-height:1.4} .sol .sxa{visibility:visible}
.box.long .bd .fig{break-inside:avoid}
.stp{border-collapse:collapse;margin:1mm auto;font-family:"Times New Roman",serif;font-size:10.5pt}
.stp td{padding:0 2mm;line-height:1.35} .stp td.s{border-right:1px solid #000;text-align:right} .stp td.l{letter-spacing:1.2mm}
.stk{display:flex;justify-content:space-between;font-size:9.5pt;margin:1mm 4mm 0}
.b2b{border-collapse:collapse;margin:1mm auto;font-family:"Times New Roman",serif;font-size:10pt}
.b2b td,.b2b th{padding:0 2mm;line-height:1.3} .b2b th{border-bottom:1px solid #000;font-weight:normal}
.b2b .lf{text-align:right;letter-spacing:1mm} .b2b .rt{letter-spacing:1mm} .b2b .st{border-left:1px solid #000;border-right:1px solid #000;text-align:center;font-weight:bold}
table.t.sm{font-size:9pt} table.t.sm td,table.t.sm th{padding:.3mm 2mm}
table.t{margin:1mm auto}
ul.q{margin:0 0 1.5mm;padding-left:6mm} ul.q li{margin:.2mm 0}
.fillin{margin:1.5mm 0;line-height:2} .bx{display:inline-block;border:1.2px solid #000;min-width:22mm;height:7mm;vertical-align:middle;text-align:center;line-height:7mm}
u{text-decoration:none;color:#c00;visibility:hidden} .sol u{visibility:visible}
table.fill td{height:6mm}
.mc .ok{display:none} .sol .mc .right .ok{display:inline;color:#c00;font-weight:bold}
.sol .mc .right span{color:#c00}
.why{visibility:hidden;color:#c00;font-size:9pt;margin-top:1mm} .sol .why{visibility:visible}
.sa .part .ans{margin-top:1mm}
.fill{font-size:9pt;width:100%} .fill th,.fill td{padding:.4mm 1mm!important;min-width:0!important}
.qgrid table.t{font-size:8.5pt} .qgrid table.t th,.qgrid table.t td{padding:.4mm 1.2mm}
.secthd{break-after:avoid} .box{break-inside:avoid} .box.long{break-inside:auto} .box.long .part{break-inside:avoid}
.subhd{display:flex;align-items:center;gap:4mm;border:2px solid #000;padding:1.5mm 4mm;margin:0 0 3mm;background:#eee;break-after:avoid}
.subhd .c{font-size:18pt;font-weight:bold;border-right:2px solid #000;padding-right:4mm}
.subhd h2{font-size:13pt;margin:0;flex:1}
.subhd .dn{font-size:9.5pt;white-space:nowrap;display:flex;gap:3mm;align-items:center}
.subhd .dn i{display:inline-block;border-bottom:1px solid #000;width:24mm;height:4mm}
.subhd .dn .tick{margin:0}
.qgrid.one{grid-template-columns:1fr}
.mcfig{display:grid;grid-template-columns:repeat(3,1fr);gap:1mm 3mm}
.mcfig div{display:flex;gap:1mm;align-items:flex-start}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.9em;line-height:1.1}.fr i:first-child{border-bottom:1px solid #000;padding:0 1mm}
.cover td{padding:1.2mm 3mm}
.sol .stu{display:none}
.sa{grid-template-columns:1fr} .sa>.stem{border-right:none;border-bottom:1.2px solid #000} .sa .part{break-inside:avoid}
.box.long>.hd{break-after:avoid} .sa>.stem{break-inside:avoid}
"""

def mc_box(q, num, sol):
    opts = q['opts']
    if opts is None:  # whole question (stem + options) is a crop of the Insight page
        return (f'<div class="box"><div class="hd">Question {num}<span>1 mark</span></div><div class="bd">'
                f'{subfigs(q["stem"], sol)}<div class="why"><b>Answer: {"ABCDE"[q["a"]]}.</b> {q["why"]}</div>'
                f'<div class="cite">{q["src"]}</div></div></div>')
    figopts = bool(opts) and opts[0].startswith('[[')
    if figopts:
        inner = '<div class="mc mcfig">' + ''.join(
            f'<div class="{"right" if i == q["a"] else ""}"><b>{"ABCDE"[i]}.</b>{subfigs(o, sol)}<span class="ok">✓</span></div>' for i, o in enumerate(opts)) + '</div>'
    else:
        inner = '<div class="mc">' + ''.join(
            f'<div class="{"right" if i == q["a"] else ""}"><b>{"ABCDE"[i]}.</b><span>{o}</span><span class="ok">&nbsp;✓</span></div>' for i, o in enumerate(opts)) + '</div>'
    sh = f' · shares information with Insight {q["shared"]}' if q.get('shared') else ''
    return (f'<div class="box"><div class="hd">Question {num}<span>1 mark</span></div><div class="bd">'
            f'{subfigs(q["stem"], sol)}{inner}<div class="why">{q["why"]}</div>'
            f'<div class="cite">{q["src"]}{sh}</div></div></div>')

def sa_box(q, num, sol):
    parts = ''
    for lab, txt, ans, sp, mk in q['parts']:
        labh = f'<b>{lab}</b>' if lab else ''
        a = f'<div class="ans">{subfigs(ans, sol)}</div>' if ans else ''
        parts += (f'<div class="part" style="flex:{max(sp,4)}"><div class="pq">{labh}<span>{subfigs(txt, sol)}</span>'
                  f'<span style="margin-left:auto;white-space:nowrap;font-size:8.5pt;color:#444">{mk} mark{"s" if mk > 1 else ""}</span></div>'
                  f'<div class="blank" style="min-height:{sp*1.5:.0f}mm">{a}</div></div>')  # answer sits inside the blank space, so both copies have the same page count
    why = f'<div class="why">{q["why"]}</div>' if q.get('why') else ''
    if q.get('note'): why += f'<div class="cite" style="font-style:italic">{q["note"]}</div>'
    m = q['marks']
    return (f'<div class="box{" long" if q.get("long") else ""}"><div class="hd">Question {num}<span>{m} mark{"s" if m > 1 else ""}</span></div><div class="sa">'
            f'<div class="stem">{subfigs(q["stem"], sol)}{why}<div class="cite">{q["src"]}</div></div>'
            f'<div class="parts">{parts}</div></div></div>')


def sx_box(q, num, sol):
    m = q['marks']
    return (f'<div class="box long"><div class="hd">Question {num}<span>{m} mark{"s" if m > 1 else ""}</span></div><div class="bd">'
            f'{subfigs(q["stem"], sol)}<div class="sxa"><b>Answers.</b> {q["ans"]}</div><div class="cite">{q["src"]}</div></div></div>')


def build(sol):
    css = open('cfat.css').read() + EXTRA
    body = ''
    # cover / title block
    body += ('<div class="title"><div class="code">Ch 8<br>REV</div><h1>Reducing balance loans, annuities and investments'
             f'<div style="font-size:10pt;font-weight:normal;margin-top:1mm">Revision booklet{" · <b style=\"color:#c00\">WORKED SOLUTIONS</b>" if sol else ""} · 8A–8I · CAS and bound reference allowed</div></h1>'
             '<div class="who"><div><b>Name</b> <i></i></div></div></div>')
    rows = ''
    num = 0
    order = []
    for code, name in SUBS:
        qs = [q for q in Q if q['sub'] == code]
        mcs = [q for q in qs if q['kind'] == 'mc']; sas = [q for q in qs if q['kind'] in ('sa', 'sx')]
        order.append((code, name, mcs, sas))
    for code, name, mcs, sas in order:
        marks = len(mcs) + sum(q['marks'] for q in sas)
        qs_ = (f'{len(mcs)} MC' if mcs else '') + (' + ' if mcs and sas else '') + (f'{len(sas)} short answer' if sas else '')
        if not (mcs or sas):
            rows += f'<tr><td><b>{code}</b></td><td>{name}</td><td colspan="3" style="font-size:9pt">{EMPTY[code]}</td></tr>'; continue
        rows += f'<tr><td><b>{code}</b></td><td>{name}</td><td>{qs_}</td><td>{marks}</td><td><div class="tick"></div></td></tr>'
    body += ('<div class="box"><div class="hd">How to use this booklet<span></span></div><div class="bd">'
             '<p class="q">One section per Cambridge subchapter. After each lesson, do the section for that subchapter: answer every question, check against the worked solutions, and correct in a different colour. Tick the box when the section is done and corrected.</p>'
             '<p class="q">Questions are copied from Insight Publications, <i>General Maths 1 – Unit 3 – Recursion and financial modelling</i> (multiple choice) and <i>General Maths 2 – Unit 3 – Recursion and financial modelling</i> (short answer), sections ‘Reducing balance loans, annuities, perpetuities, amortisation tables’ and ‘Using the finance solver’, © Insight Publications 2022, reproduced as scans of the page. Each question shows its Insight section, page and number; answer on the lines in each question. Where Insight lets several questions share information, that information is repeated in each box. Short-answer questions that mix several subchapters sit in the section of the last subchapter they need.</p>'
             '<table class="t cover" style="width:100%"><tr><th>Sub</th><th class="l">Topic</th><th>Questions</th><th>Marks</th><th>Done</th></tr>' + rows + '</table></div></div>')
    for code, name, mcs, sas in order:
        if not (mcs or sas): continue
        body += (f'<div class="brk"></div><div class="subhd"><div class="c">{code}</div><h2>{name}</h2>'
                 '<div class="dn">Done <div class="tick"></div> Date <i></i></div></div>')
        if mcs:
            body += f'<div class="secthd">Multiple choice<span>Circle one answer. {len(mcs)} mark{"s" if len(mcs) > 1 else ""}</span></div>'
            for i in range(0, len(mcs), 2):
                pair = mcs[i:i + 2]
                cls = 'qgrid one' if any((q['opts'] or ['x'])[0].startswith('[[') for q in pair) else 'qgrid'
                if cls == 'qgrid one':
                    for q in pair:
                        num += 1; body += f'<div class="qgrid one">{mc_box(q, num, sol)}</div>'
                    continue
                body += '<div class="qgrid">'
                for q in pair:
                    num += 1; body += mc_box(q, num, sol)
                body += '</div>'
        if sas:
            body += f'<div class="secthd">Short answer<span>Show your working. {sum(q["marks"] for q in sas)} marks</span></div>'
            for q in sas:
                num += 1; body += '' + (sx_box if q['kind'] == 'sx' else sa_box)(q, num, sol)
    title = 'Ch8 revision booklet' + (' solutions' if sol else '')
    L = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'lessons')
    js = ''.join(f'<script>{open(os.path.join(L, f)).read()}</script>' for f in ('a4view.js', 'paged.polyfill.min.js')) if A4VIEW else ''
    if A4VIEW:  # cover the page with a grey 'Loading A4 pages' screen until Paged.js has finished laying out the pages
        js = js.replace('<script>', '<script>' + LOADER + '</script><script>', 1).replace('document.head.appendChild(s);}', 'document.head.appendChild(s);window.__a4done&&window.__a4done();}', 1)
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style>{js}</head><body class="{"sol" if sol else ""}">{body}</body></html>'

os.makedirs('out', exist_ok=True)
for sol in (0, 1):
    open(f'out/Ch8-revision-booklet{"-solutions" if sol else ""}.html', 'w').write(build(sol))
print('ok')
