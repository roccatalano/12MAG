"""Segment Insight 'Matrices - Transition matrices' questions. args: prefix p0 p1 ncol out
Starts at the 'Transition' section header, stops at the next section header ('Networks')."""
import sys,subprocess,csv,io,json,re
from PIL import Image
pre,p0,p1,ncol,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
regions=[];started=False
for p in range(p0,p1+1):
    f=f'{pre}-{p:02d}.png'; im=Image.open(f); W,H=im.size
    t=subprocess.run(['tesseract',f,'-','--psm','3','tsv'],capture_output=True,text=True).stdout
    words=[r for r in csv.DictReader(io.StringIO(t),delimiter='\t',quoting=csv.QUOTE_NONE) if r['text'] and r['text'].strip()]
    hd=[];start=None;stop=None
    for i,w in enumerate(words):
        if w['text']=='Question' and i+1<len(words):
            m=re.match(r'^(\d+)',words[i+1]['text'])
            if m and abs(int(words[i+1]['top'])-int(w['top']))<15: hd.append((int(w['left']),int(w['top']),int(m.group(1))))
        if w['text']=='Use' and i+2<len(words) and words[i+1]['text']=='the' and words[i+2]['text'].startswith('follow'): hd.append((int(w['left']),int(w['top'])+10,'S'))
        if 'Transition' in w['text'] and 'Matrices' in words[i-1]['text']+w['text']: start=(int(w['left']),int(w['top']))
        if w['text']=='Networks': stop=(int(w['left']),int(w['top']))
    sp=(1005 if p%2==0 else 900)
    cols=[(0,W)] if ncol==1 else [(0,sp),(sp,W)]
    for (x0,x1) in cols:
        y0=int(H*0.05);y1=int(H*0.915)
        if start and x0<=start[0]<x1: started=True;y0=start[1]+60
        if not started: continue
        if stop and x0<=stop[0]<x1: y1=stop[1]-20
        if stop and x0>stop[0]: continue
        regions.append(dict(p=p,x0=x0,x1=x1,y0=y0,y1=y1,h=sorted([(y,n) for x,y,n in hd if x0<=x<x1 and y0<y<y1])))
        if stop and x0<=stop[0]<x1: break
    if stop: break
qs={};cur=None;ns=0
for r in regions:
    y=r['y0']
    for (hy,n) in r["h"]:
        if n=='S': ns+=1;n=f'S{ns}'
        if cur is not None and hy-10>y: qs[cur].append((r['p'],r['x0'],y,r['x1'],hy-10))
        cur=n;qs[cur]=[];y=hy-10
    if cur is not None and r['y1']>y: qs[cur].append((r['p'],r['x0'],y,r['x1'],r['y1']))
json.dump(qs,open(out,'w'));print({k:len(v) for k,v in qs.items()})
