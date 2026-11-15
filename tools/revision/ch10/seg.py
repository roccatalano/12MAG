import sys,subprocess,csv,io,json,re
from PIL import Image
pre,p0,p1,ncol,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]
regions=[]  # (page,x0,x1,y0,y1, headers[(y,n)])
for p in range(p0,p1+1):
    f=f'{pre}-{p:02d}.png'; im=Image.open(f); W,H=im.size
    t=subprocess.run(['tesseract',f,'-','--psm','3','tsv'],capture_output=True,text=True).stdout
    rows=list(csv.DictReader(io.StringIO(t),delimiter='\t',quoting=csv.QUOTE_NONE))
    words=[r for r in rows if r['text'] and r['text'].strip()]
    hd=[];stop=None
    for i,w in enumerate(words):
        if w['text']=='Question' and i+1<len(words):
            m=re.match(r'^(\d+)',words[i+1]['text'])
            if m and abs(int(words[i+1]['top'])-int(w['top']))<15: hd.append((int(w['left']),int(w['top']),int(m.group(1))))
        if 'Transition' in w['text']: stop=(int(w['left']),int(w['top']))
    sp=(1005 if p%2==0 else 900)
    cols=[(0,W)] if ncol==1 else [(0,sp),(sp,W)]
    for (x0,x1) in cols:
        y1=int(H*0.915)
        if stop and x0<=stop[0]<x1: y1=stop[1]-20
        regions.append(dict(p=p,x0=x0,x1=x1,y0=int(H*0.05),y1=y1,h=sorted([(y,n) for x,y,n in hd if x0<=x<x1])))
qs={};cur=None
for r in regions:
    y=r['y0']
    for (hy,n) in r["h"]:
        if n in qs and n!=cur: break
        if cur is not None and hy-10>y: qs[cur].append((r['p'],r['x0'],y,r['x1'],hy-10))
        cur=n;qs[cur]=[];y=hy-10
    if cur is not None and r['y1']>y: qs[cur].append((r['p'],r['x0'],y,r['x1'],r['y1']))
json.dump(qs,open(out,'w'));print({k:len(v) for k,v in qs.items()})
