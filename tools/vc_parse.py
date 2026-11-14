import re,glob,os,csv
def paper(n):
    y=re.search(r'20\d\d',n).group(); nht='NHT' if re.search('nht',n,re.I) else ''
    e='1' if re.search(r'(math1|Maths1|GM1|generalmaths1)',n,re.I) else '2'
    return y,nht,e
K=[(5,r'time series|seasonal|deseason|moving (mean|median)|smooth|trend line|quarter'),
   (4,r'transformation|linearis|log\s*10|log10|reciprocal|squared|\^2|x2\b'),
   (3,r'least squares|regression|residual|slope|intercept|predict|extrapolat|interpolat'),
   (2,r'scatterplot|correlation|association|segmented|two-way|explanatory|response variable|parallel box|back-to-back|coefficient of determination|causal'),
   (1,r'histogram|boxplot|stem plot|dot plot|median|mean|standard deviation|normal|z-score|standardised|quartile|interquartile|IQR|outlier|five-number|percentile|nominal|ordinal|discrete|continuous|categorical|numerical|range|skew|frequency|log scale')]
rows=[]
for f in sorted(glob.glob('/tmp/vc/*.txt')):
    n=os.path.basename(f)[:-4]; y,nht,e=paper(n); t=open(f).read()
    i=re.search(r'Recursion and financial',t,re.I); t=t[:i.start()] if i else t
    parts=re.split(r'\n\s*Question\s+(\d+)\b',t)
    for k in range(1,len(parts),2):
        q=int(parts[k]); body=parts[k+1]
        if e=='1' and q>20: continue
        prev=parts[k-1][-700:] if k>1 else parts[0][-700:]
        txt=re.sub(r'\s+',' ',prev+' || '+body)
        ch=next((c for c,r in K if re.search(r,txt,re.I)),0)
        sub=sorted(set(re.findall(r'\n\s*([a-f])\.\s',body))) if e=='2' else []
        marks=re.search(r'\((\d+)\s*marks?\)',body)
        rows.append([y+(' NHT' if nht else ''),'Exam '+e,q,ch,','.join(sub),marks.group(1) if marks else '',txt[txt.find('||')+3:][:110],txt[:900]])
w=csv.writer(open('/home/claude/vcaa_cur_data.csv','w',newline=''));w.writerow(['paper','exam','q','ch','parts','marks','stem','ctx']);w.writerows(rows)
import collections;print(len(rows),collections.Counter((r[1],r[3]) for r in rows))

# Exam 2 parts
rows2=[]
for f in sorted(glob.glob('/tmp/vc/*.txt')):
    n=os.path.basename(f)[:-4]; y,nht,e=paper(n)
    if e!='2': continue
    t=open(f).read(); i=re.search(r'Recursion and financial',t,re.I); t=t[:i.start()] if i else t
    parts=re.split(r'\n\s*Question\s+(\d+)\b',t)
    for k in range(1,len(parts),2):
        q=int(parts[k]); body=parts[k+1]
        sp=re.split(r'\n\s*([a-h])\.\s+',body)
        stem=re.sub(r'\s+',' ',sp[0])
        for j in range(1,len(sp),2):
            p=sp[j]; pb=sp[j+1]
            subs=re.split(r'\n\s*(i{1,3}|iv)\.\s+',pb)
            items=[(p,subs[0])] if len(subs)==1 else [(p+subs[x],subs[x+1]) for x in range(1,len(subs),2)]
            for lab,txt in items:
                tx=re.sub(r'\s+',' ',txt); m=re.search(r'(\d)\s*marks?',tx)
                ch=next((c for c,r in K if re.search(r,tx,re.I)),0) or next((c for c,r in K if re.search(r,stem,re.I)),0)
                rows2.append([y+(' NHT' if nht else ''),'Exam 2',f'{q}{lab}',ch,m.group(1) if m else '',tx[:110],(stem[-500:]+' || '+tx)[:900]])
w=csv.writer(open('/home/claude/vcaa_cur_ex2parts.csv','w',newline=''));w.writerow(['paper','exam','q','ch','marks','text','ctx']);w.writerows(rows2)
print('parts',len(rows2),collections.Counter(r[3] for r in rows2),collections.Counter(r[4] for r in rows2))
