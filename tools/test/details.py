"""Writes planner/tests.json: per chapter test, marks + question breakdown, read from tools/test/ch*/build.py (MC, SA lists).
Shown on the planner's chapter test cards ('Test details'). Re-run after changing a test: python3 tools/test/details.py"""
import os, re, sys, json, glob, importlib.util, html
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def txt(h): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
def short(h, n=110):
    t = txt(h); return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'
out = {}
for f in sorted(glob.glob(os.path.join(R, 'tools/test/ch*/build.py'))):
    ch = int(re.search(r'ch(\d+)', f).group(1))
    sp = importlib.util.spec_from_file_location(f'test{ch}', f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    doc = (m.__doc__ or '').strip().splitlines()
    qs, n = [], 0
    for src, stem, opts, k in m.MC:
        n += 1; qs.append(dict(q=str(n), type='MC', marks=1, src=src, text=short(stem), answer='ABCDE'[k]))
    for src, stem, parts in m.SA:
        n += 1
        for lab, ptxt, mk, *_ in parts:
            qs.append(dict(q=f'{n}{lab}', type='SA', marks=mk, src=src, text=short(ptxt or stem)))
    by = {}
    for q in qs:
        code = q['src'].split('·')[-1].strip(); b = by.setdefault(code, dict(lesson=code, marks=0, qs=[])); b['marks'] += q['marks']
        if q['q'].rstrip('abcdefghi') not in [x.rstrip('abcdefghi') for x in b['qs']]: b['qs'].append(q['q'])
    out[str(ch)] = dict(chapter=ch, total=sum(q['marks'] for q in qs), mc=len(m.MC), sa=len(m.SA),
                        about=' '.join(doc[1:3]).strip(), byLesson=list(by.values()), questions=qs)
json.dump(out, open(os.path.join(R, 'planner/tests.json'), 'w'), indent=1, ensure_ascii=False)
print({k: (v['total'], len(v['questions'])) for k, v in out.items()})
