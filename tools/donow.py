import re,csv,collections,json
ORDER=['1A','1B','1C','1D','1E','1F','1G','1H','1I','2A','2B','2C','2D','2E','2F','2G','2H','2I','3A','3B','3C','4A','4B','4C','4D','5A','5B','5C','5D','5E']
LES=[('s1',['1A','1B']),('s2',['1C','1D','1E']),('s3',['1F']),('s4',['1G']),('s5',['1H','1I']),('l03',['2A','2B']),('l04',['2C','2D']),('l05',['2E']),('l06',['2F']),('l07',['2G','2H','2I']),('l09',['3A']),('l10',['3B']),('l11',['3B','3C']),('l12',['4A']),('l13',['4B']),('l14',['4C']),('l15',['4D']),('l16',['5A']),('l17',['5B']),('l18',['5B']),('l19',['5C']),('l20',['5D']),('l21',['5D']),('l22',['5E'])]
KW=[('1A',r'nominal|ordinal|discrete|continuous|categorical variable|numerical variable|type of variable'),
('1B',r'bar chart|percentage frequency|frequency table|mode'),
('1C',r'histogram|skew|symmetric|shape of the distribution'),
('1D',r'stem plot|dot plot'),
('1E',r'log scale|logarithmic scale|log\s*10\s*\(|log10'),
('1F',r'\bmean\b|median|standard deviation|range|interquartile|IQR|quartile'),
('1G',r'boxplot|five-number|outlier|fence'),
('1H',r'normal(ly)? distribut|68|95%|99\.7'),
('1I',r'z-?score|standardised|standard score|percentile'),
('2A',r'explanatory|response variable|two-way|segmented'),
('2C',r'parallel boxplot|back-to-back|parallel dot'),
('2E',r'scatterplot|direction|strength of the|linear association|form '),
('2F',r'correlation coefficient|\br\s*=|Pearson'),
('2G',r'coefficient of determination|r\s*2|variation in'),
('2H',r'caus|confound|common response|lurking'),
('3A',r'least squares line|equation of the least squares|regression line'),
('3B',r'slope|intercept|predict|extrapolat|interpolat'),
('3C',r'residual'),
('4A',r'squared transformation|\(\w+\)\s*2 |x2 transformation|square transformation'),
('4B',r'logarithmic \(base 10\) transformation|log\s*10\s*transformation|log transformation|log10\(?\w*\)? transformation|logarithmic transformation'),
('4C',r'reciprocal'),
('4D',r'transformation|linearis'),
('5A',r'time series|trend|seasonal(ity)?|cyclic|irregular|structural change'),
('5B',r'moving mean|smooth|centr'),
('5C',r'moving median|median smoothing'),
('5D',r'seasonal ind|deseasonal|re-?seasonal'),
('5E',r'trend line|forecast')]
def tag(txt):
    q=txt.split('||')[-1]
    for t in (q,txt):
        hits=[s for s,r in KW if re.search(r,t,re.I)]
        if {'4A','4B','4C'}&set(hits): hits=[h for h in hits if h!='4D']
        if hits: return max(hits,key=ORDER.index)
    return None
items=[]
for r in csv.DictReader(open('/home/claude/vcaa_cur_data.csv')):
    if r['exam']=='Exam 1': items.append(dict(ex=1,paper=r['paper'],q='Q'+r['q'],marks=1,sec=tag(r['ctx'])))
for r in csv.DictReader(open('/home/claude/vcaa_cur_ex2parts.csv')):
    m=int(r['marks'] or 1)
    if m<=2: items.append(dict(ex=2,paper=r['paper'],q='Q'+r['q'],marks=m,sec=tag(r['ctx'])))
OVR={('2025 NHT','Q7',1):'5A'}
for i in items:
    i['sec']=OVR.get((i['paper'],i['q'],i['ex']),i['sec'])
items=[i for i in items if i['sec']]
print(len(items),collections.Counter((i['ex'],i['sec'][0]) for i in items))
used=set();out={};taught=[]
for lid,secs in LES:
    pool=lambda ex:[i for i in items if i['ex']==ex and i['sec'] in taught and (i['paper'],i['q'],ex) not in used]
    pick=[]
    for ex in (1,2):
        cand=pool(ex)
        # spread: favour sections least recently used, oldest first, alternating
        cand.sort(key=lambda i:(sum(1 for v in out.values() for x in v if x['sec']==i['sec']),-ORDER.index(i['sec']) if len(pick)%2 else ORDER.index(i['sec'])))
        got=[]
        for c in cand:
            if len(got)==2: break
            if any(g['sec']==c['sec'] for g in got): continue
            got.append(c)
        for c in got: used.add((c['paper'],c['q'],ex))
        pick+=got
    out[lid]=pick; taught+=secs
for k,v in out.items(): print(k,[f"{x['paper']} E{x['ex']} {x['q']}({x['sec']})" for x in v])
json.dump(out,open('/home/claude/donow.json','w'))
