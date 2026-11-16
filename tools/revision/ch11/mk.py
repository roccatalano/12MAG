import json,sys
from PIL import Image,ImageOps
pre,seg,tag,od=sys.argv[1:5]
import os;os.makedirs(od,exist_ok=True)
for n,fr in json.load(open(seg)).items():
    parts=[]
    for p,x0,y0,x1,y1 in fr:
        im=Image.open(f'{pre}-{p:02d}.png').convert('L').crop((x0,y0,x1,y1))
        g=ImageOps.invert(im).point(lambda v:255 if v>60 else 0); bb=g.getbbox()
        if not bb or bb[3]-bb[1]<12: continue
        parts.append(im.crop((max(bb[0]-10,0),max(bb[1]-10,0),min(bb[2]+10,im.width),min(bb[3]+10,im.height))))
    W=max(i.width for i in parts);H=sum(i.height for i in parts)+20*(len(parts)-1)
    c=Image.new('L',(W,H),255);y=0
    for i in parts:c.paste(i,(0,y));y+=i.height+20
    c.save(f'{od}/{tag}q{n}.png',optimize=True);print(n,len(parts),c.size)
