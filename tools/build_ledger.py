"""Build tools/ledger.csv: every item already used, keyed by a canonical id.
VCAA reprints (Edrolo exam practice) are keyed by their ORIGINAL VCAA question (rule 10).
Sources: the burnt table in 04 Archive/Planning/Topics/1. Data Analysis/HANDOFF.md (pass its path)
and the src citations in lessons/*.html. Re-run after adding lessons; add manual rows to tools/ledger_manual.csv."""
import re,csv,html,glob,os,sys
T=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(T)
BURNS={'Do Now','APK','Exit','CFAT','Booklet','Test','Do Now/Exit','Exam practice'}
# Edrolo lesson+Q -> VCAA citation, from the step-1 indexes
ED={}
for book,f in (('U1&2','y11_edrolo_exam_practice.csv'),('U3&4','y12_edrolo_exam_practice.csv')):
    for r in csv.DictReader(open(os.path.join(T,f))): ED[(book,r['edrolo_lesson'],int(r['q']))]=r['source']
def vcaa_id(s):
    s=re.sub(r'\s+',' ',s.replace('Adapted from','')).strip()
    m=re.search(r'VCAA (\d{4})( NHT)?(?: General Mathematics)? Exam ([12])(?: (.*?))? ?Q\s?(\d+[a-z]*(?:\s?i{1,3}v?)?)',s)
    if not m: return None
    y,nht,ex,sec,q=m.groups(); q=q.replace(' ','')
    if int(y)>=2023 and not (y=='2023' and nht): return f'VCAA {y}{nht or ""} E{ex} Q{q}'
    sec=(sec or '').lower(); S='Core'
    for k,v in (('matri','Matrices'),('network','Networks'),('geometr','Geometry'),('graph','Graphs'),('business','Business'),('number pattern','Number patterns')):
        if k in sec: S=v
    return f'VCAA {y}{nht or ""} E{ex} {S} Q{q}'
def ids_from_cite(c):
    """one citation string -> (canonical id, book ref)"""
    c=re.sub(r'\s+',' ',html.unescape(c)).strip()
    if c.startswith('Data:') or c.startswith('Survey data'): return None
    book='U1&2' if 'Units 1&2' in c else 'U3&4'
    m=re.search(r'Edrolo.*?(\d[A-Z]) (Q\d+|Worked example \d+)',c)
    if m and m.group(2).startswith('Q'):
        q=int(m.group(2)[1:]); v=ED.get((book,m.group(1),q))
        ref=f'Edrolo {book} {m.group(1)} Q{q}'
        return (vcaa_id(v) if v else ref), ref
    if m: return f'Edrolo {book} {m.group(1)} WE{m.group(2).split()[-1]}', ''
    v=vcaa_id(c)
    if v: return v,''
    m=re.search(r'Example (\d+)',c)
    if 'Cambridge' in c and m and 'Exercise' not in c: return f'Cambridge {book} Example {m.group(1)}',''
    m=re.search(r'skills checklist, (\w+ #\d+)',c)
    if m: return f'Cambridge U1&2 skills checklist {m.group(1)}',''
    m=re.search(r'Exercise (\d[A-Z])\b.*?(Q[\d–-]+)',c)
    if m: return f'Cambridge {book} Ex {m.group(1)} {m.group(2)}',''
    return None  # page refs, notes, data credits: not items
ROLE={'do now':'Do Now','apk':'APK','exit task':'Exit','you try':'You try','worked example':'Example','check-in':'Check-in','homework':'Homework','skills check':'Skills check'}
rows=[]
def add(id_,ref,role,where,date,note=''):
    rows.append(dict(item=id_,via=ref,role=role,burnt='yes' if role in BURNS else 'no',where=where,date=date,note=note))
# 1. lessons: the role comes from each slide's own class (dn, apk, we, yt, ex, cfat) or its pill label
CLS={'dn':'Do Now','apk':'APK','ex':'Exit','we':'Example','yt':'You try','cfat':'CFAT'}
PILL=[('Do Now','Do Now'),('APK','APK'),('Exit','Exit'),('Worked example','Example'),('You try','You try'),('CFAT','CFAT'),('Homework','Homework'),('CAS','CAS')]
for f in sorted(glob.glob(os.path.join(R,'lessons','*.html'))):
    t=open(f,encoding='utf-8').read(); name=os.path.basename(f)[:-5]
    for sec in re.findall(r'<section\b.*?</section>',t,re.S):
        cls=(re.match(r'<section[^>]*class="([^"]*)"',sec) or [None,''])[1].split()
        pill=html.unescape(re.sub(r'<[^>]+>','',(re.search(r'class="pill"[^>]*>(.*?)</div>',sec,re.S) or [None,''])[1])).strip()
        role=next((CLS[c] for c in cls if c in CLS),None) or next((r for k,r in PILL if pill.startswith(k)),'Other')
        for m in re.finditer(r'class="src"[^>]*>(.*?)</',sec,re.S):
            cite=html.unescape(re.sub(r'<[^>]+>','',m.group(1)))
            # one src can name two parts (e.g. "Q1b, Q1d"): split them
            for c in ([re.sub(r'Q(\d+)([a-z]), Q\1([a-z])',lambda x:'Q'+x.group(1)+x.group(2),cite),re.sub(r'Q(\d+)([a-z]), Q\1([a-z])',lambda x:'Q'+x.group(1)+x.group(3),cite)] if re.search(r'Q\d+[a-z], Q\d+[a-z]',cite) else [cite]):
                if 'skills checklist' in c:
                    items=[];cur=None
                    for sub,num in re.findall(r'(\d[A-Z])? ?#(\d+)',c.split('checklist',1)[1]):
                        cur=sub or cur; items.append(f'{cur} #{num}')
                    for it in items: add(f'Cambridge U1&2 skills checklist {it}','',role,name.split('-')[0],'',name)
                    continue
                r=ids_from_cite(c)
                if r: add(r[0],r[1],role,name.split('-')[0],'',name)
# 2. HANDOFF burnt table
if len(sys.argv)>1:
    on=False
    for l in open(sys.argv[1],encoding='utf-8'):
        if l.startswith('## '): on=l.lower().startswith('## burnt')
        if not on: continue
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        if len(c)!=4 or c[0] in ('Use','---') or c[0].startswith('-'): continue
        use,src,paper,qs=c
        if 'Insight' in src: continue
        if use.startswith('Lesson handout') or use.startswith('Exam Q ('): continue  # Rocco 15 Nov: old handout/exam-Q rows are freed (never used in class)  # Rocco 14 Nov: nothing from Insight is ever burnt (rejected CFAT 1.1)
        u=use+' '+qs
        role=('Do Now/Exit' if use.startswith('Deck') else 'Do Now' if 'Do Now' in use else 'Exit' if ('Exit' in use or use.startswith('Exam Q'))
              else 'APK' if 'APK' in u else 'CFAT' if use.startswith('CFAT') else 'You try' if 'You' in u else 'Example' if ('Example' in u or 'WE' in use)
              else 'Rapid practice' if use.startswith('Rapid') else 'Exam practice' if src.startswith('VCAA') else 'Skills check/homework')
        note='HANDOFF burnt list'+('; Insight CFAT 1.1 was rejected (4 Nov), un-burn still open' if 'Insight' in src else '')
        where=re.sub(r'\s*\(.*\)','',use) if use.startswith('CFAT') else use
        qlist=[q.strip() for q in re.split(r',\s*(?=Q)',re.sub(r'\s*\(.*?\)','',qs))]
        for q in qlist:
            if src.startswith('VCAA'):
                y=paper.replace(' Exam ',' E')
                cur=re.match(r'(\d{4})',y) and int(y[:4])>=2023 and 'current' in src
                m=re.fullmatch(r'(Q\d+)([a-z])–([a-z])',q)
                for qq in ([m.group(1)+chr(c) for c in range(ord(m.group(2)),ord(m.group(3))+1)] if m else [q]):
                    id_=f'VCAA {y} {qq}' if cur else vcaa_id(f'VCAA {paper} Data analysis {qq}')
                    add(id_,'',role,where,'',note)
            elif src=='Edrolo' and q.startswith('Q'):
                m=re.fullmatch(r'Q(\d+)–(\d+)',q)
                nums=range(int(m.group(1)),int(m.group(2))+1) if m else [int(re.match(r'Q(\d+)',q).group(1))]
                tail='' if m else q[len(re.match(r'Q\d+',q).group(0)):]
                for n in nums:
                    v=ED.get(('U3&4',paper,n))
                    add(vcaa_id(v) if v else f'Edrolo U3&4 {paper} Q{n}{tail}', f'Edrolo U3&4 {paper} Q{n}' if v else '',role,where,'',note)
            elif 'checklist' in paper:
                for it in re.findall(r'\d[A-Z] #\d+',q): add(f'Cambridge U1&2 skills checklist {it}','',role,where,'',note)
            else: add(f'{src} {paper} {q}','',role,where,'',note)
man=os.path.join(T,'ledger_manual.csv')
if os.path.exists(man): rows+=list(csv.DictReader(open(man)))
seen=set(); out=[]
for r in rows:
    k=(r['item'],r['role'],r['where'])
    if k in seen: continue
    seen.add(k); out.append(r)
out.sort(key=lambda r:(r['burnt']!='yes',r['item']))
w=csv.DictWriter(open(os.path.join(T,'ledger.csv'),'w',newline='',encoding='utf-8'),fieldnames=['item','via','role','burnt','where','date','note']); w.writeheader(); w.writerows(out)
print(len(out),'rows,',sum(r['burnt']=='yes' for r in out),'burnt')
