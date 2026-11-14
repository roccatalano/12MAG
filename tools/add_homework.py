"""Add card.homework to every lesson in planner/unit-plan.json.
Lessons with a slide deck: copied from the deck's Homework slide (Cambridge exercises, skill rows, question ranges; Revision book line).
Other lessons: the Cambridge exercise for each subchapter, breakdown to come when the slides are made (rule 9: homework = Cambridge exercises).
Re-run after making a deck."""
import json,re,html,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(R,'planner','unit-plan.json'); U=json.load(open(P,encoding='utf-8'))
clean=lambda s:re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s))).strip()
def from_deck(path):
    t=open(os.path.join(R,path),encoding='utf-8').read()
    secs=[s for s in re.findall(r'<section\b.*?</section>',t,re.S) if re.search(r'class="pill"[^>]*>\s*Homework',s)]
    if not secs: return None
    out=[]
    for blk in re.findall(r'<div class="key hw"[^>]*>(.*?)</div>',secs[-1],re.S):
        h=clean(re.search(r'<h4>(.*?)</h4>',blk,re.S).group(1))
        rows=[[clean(c) for c in re.findall(r'<td>(.*?)</td>',r,re.S)] for r in re.findall(r'<tr>(.*?)</tr>',blk,re.S)]
        note=clean(re.search(r'<p[^>]*>(.*?)</p>',blk,re.S).group(1)) if '<p' in blk else ''
        out.append(dict(title=h,items=[dict(skill=a,q=b) for a,b in rows],note=note))
    return out
n=0
for a in U['aos']:
    for c in a['chapters']:
        for l in c['lessons']:
            if l['kind']!='lesson': continue
            k=l.setdefault('card',{})
            deck=next((m['file'] for m in k.get('materials',[]) if m.get('kind')=='Guided slides' and m.get('file')),None)
            hw=from_deck(deck) if deck else None
            if hw: k['homework']=dict(source='slides',sets=hw); n+=1
            else:
                k['homework']=dict(source='default',sets=[dict(title=f'Cambridge · Exercise {s}',items=[],note='All questions'+(f' (shared with the other {s} lesson)' if l.get('part') else '')+'. Skill-by-skill breakdown added when the slides are made.') for s in l['subchapters']])
json.dump(U,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(n,'lessons with homework from slides')
