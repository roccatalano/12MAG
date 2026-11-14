"""One-off: write planner/unit-plan.json (the Unit plan: AoS -> chapters -> lessons, no dates).
Ch 1-5 and 7-8 come from the dashboard JSON that tools/build_plan.py wrote (teaching-dashboard-2027/classes/general-maths-12.json).
Unit 4 chapters are shells from the Cambridge sample planner (00 Admin/Study Design/Sample-planner-and-timeline.docx).
After this first draft, planner/unit-plan.json is the source of truth: edit it, don't re-run this.
Usage: python tools/make_unit_plan.py <path to general-maths-12.json>"""
import json, re, sys, os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(sys.argv[1], encoding='utf-8'))

CH = {1: 'Investigating data distributions', 2: 'Investigating associations between two variables',
      3: 'Investigating and modelling linear associations', 4: 'Data transformation',
      5: 'Investigating and modelling time series', 7: 'Modelling growth and decay using recursion',
      8: 'Reducing balance loans, annuities and investments', 10: 'Matrices',
      11: 'Transition matrices and Leslie matrices', 13: 'Graphs, networks and trees: travelling and connecting problems',
      14: 'Flow, matching and scheduling'}
AOS = [dict(id='aos1', n=1, unit=3, title='Data analysis', chapters=[1, 2, 3, 4, 5], revision='Ch 6 (revision, practice only)'),
       dict(id='aos2', n=2, unit=3, title='Recursion and financial modelling', chapters=[7, 8], revision='Ch 9 (revision)'),
       dict(id='aos3', n=3, unit=4, title='Matrices', chapters=[10, 11], revision='Ch 12 (revision)'),
       dict(id='aos4', n=4, unit=4, title='Networks and decision mathematics', chapters=[13, 14], revision='Ch 15 (revision)')]

def subs(section):
    """'1C–1E' -> ['1C','1D','1E']; '7B, 7D' -> ['7B','7D']"""
    out = []
    for part in re.split(r',\s*', section):
        m = re.fullmatch(r'(\d+)([A-Z])[–-](\d+)?([A-Z])', part.strip())
        if m:
            out += [m.group(1) + chr(c) for c in range(ord(m.group(2)), ord(m.group(4)) + 1)]
        elif part.strip():
            out.append(part.strip())
    return out

def fix_paths(x):
    """dashboard paths lessons/gm12/X -> this repo's lessons/X"""
    return json.loads(json.dumps(x).replace('lessons/gm12/', 'lessons/'))

CARD = ['learningObjectives', 'successCriteria', 'studyDesign', 'keyVocab', 'weDo', 'apk', 'doNow', 'exit', 'cas', 'cfats', 'materials']
chapters = {n: [] for n in CH}
seen_sub = {}
hol_cfats = []
for l in D['lessons']:
    if l['type'] == 'holiday':
        hol_cfats = l.get('cfats', [])
        continue
    if l['type'] == 'lesson':
        ss = subs(l['section'])
        ch = int(re.match(r'\d+', ss[0]).group())
        if ch not in chapters:
            continue
        # a subchapter split over two lessons -> "5B (part 1)", "5B (part 2)"
        key = tuple(ss)
        seen_sub[key] = seen_sub.get(key, 0) + 1
        les = dict(id=l['id'], kind='lesson', subchapters=ss, title=l['title'])
        les['card'] = fix_paths({k: l[k] for k in CARD if l.get(k)})
        chapters[ch].append(les)
    elif l['type'] == 'sac' and re.fullmatch(r'\d+', l['section']):
        ch = int(l['section'])
        if ch in chapters:
            les = dict(id=l['id'], kind='check', subchapters=[], title=f'Chapter {ch} coursework check + test')
            les['card'] = fix_paths({k: l[k] for k in CARD if l.get(k)})
            chapters[ch].append(les)

# label split subchapters
for ch, ls in chapters.items():
    count = {}
    for les in ls:
        k = tuple(les['subchapters'])
        if les['kind'] == 'lesson' and seen_sub.get(k, 0) > 1:
            count[k] = count.get(k, 0) + 1
            les['part'] = count[k]

# CFAT 1.1.3 was set as summer holiday work: keep it with the Ch 1 check lesson
for les in chapters[1]:
    if les['kind'] == 'check' and hol_cfats:
        les['card'].setdefault('cfats', [])
        les['card']['cfats'] = [dict(c, note='Set as summer holiday work in 2026–27') for c in hol_cfats] + les['card']['cfats']

# Unit 4 shells (Cambridge sample planner savings: 10A–10C in one lesson; 13A+13B and 13D+13E in one lesson)
SHELL = {10: [['10A', '10B', '10C'], ['10D'], ['10E'], ['10F'], ['10G']],
         11: [['11A'], ['11B'], ['11C'], ['11D'], ['11E']],
         13: [['13A', '13B'], ['13C'], ['13D', '13E'], ['13F']],
         14: [['14A'], ['14B'], ['14C'], ['14D'], ['14E']]}
for ch, groups in SHELL.items():
    chapters[ch] = [dict(id=f'gm12-u4-{"".join(g).lower()}', kind='lesson', subchapters=g, title='', card={}, shell=True) for g in groups]

# every chapter ends with exactly one coursework check + test lesson
for ch, ls in chapters.items():
    if not any(x['kind'] == 'check' for x in ls):
        ls.append(dict(id=f'gm12-ch{ch}-test', kind='check', subchapters=[], title=f'Chapter {ch} coursework check + test', card={}, shell=True))
    ls.sort(key=lambda x: x['kind'] == 'check')

out = dict(subject='VCE General Mathematics Units 3&4', code='12MAG', textbook='Cambridge General Mathematics VCE Units 3&4 (2nd ed., 2023)',
           note='Content only, no dates. Lessons are lists of Cambridge subchapters; plan one chapter at a time. Year plans flow these lessons into dated slots.',
           aos=[dict(a, chapters=[dict(n=n, title=CH[n], lessons=chapters[n]) for n in a['chapters']]) for a in AOS])
os.makedirs(os.path.join(R, 'planner', 'years'), exist_ok=True)
json.dump(out, open(os.path.join(R, 'planner', 'unit-plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for a in out['aos']:
    for c in a['chapters']:
        print(a['n'], c['n'], [('+'.join(l['subchapters']) or 'TEST') + (f" p{l['part']}" if l.get('part') else '') for l in c['lessons']])
