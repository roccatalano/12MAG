import json,csv,re,collections
I=json.load(open('/root/work/edq.json'))
LES={'1A':'1A','1B':'1B','1C':'1C','1D':'1E','1E':'1G','1F':'1F','1G':'1F','1H':'1H','1I':'1H',
'2A':'2B','2B':'2C','2C':'2E','2D':'2F','3A':'3A','3B':'3B','3C':'3C','3D':'4D','3E':'4D',
'4A':'5A','4B':'5B','4C':'5C','4D':'5D','4E':'5E','5A':'7A','5B':'7B','5C':'7D','5D':'7C','5E':'7B','5F':'7D','5G':'7F',
'6A':'8C','6B':'8B','6C':'8H','6D':'8B','6E':'8I','6F':'8A',
'7A':'10A','7B':'10C','7C':'10D','7D':'10E','7E':'10F','7F':'10F','7G':'11A','7H':'11C','7I':'11B',
'8A':'13A','8B':'13B','8C':'13C','8D':'13F','8E':'14A','8F':'13E','8G':'14B','8H':'14C','8I':'14D','8J':'14E'}
HEAD={'Displaying data using dot plots':'1D','Displaying data using stem plots':'1D','Calculating the range and interquartile range':'1F',
'Describing the distribution of histograms':'1C','Describing the distribution of dot plots and stem plots':'1D','Describing the distribution of boxplots':'1G',
'Identifying the response and explanatory variables':'2A','Using technology to construct scatterplots':'2D',
'Distinguishing between correlation and causation':'2H','Calculating and interpreting the coefficient of determination':'2G',
'Applying a squared transformation':'4A','Applying a log transformation':'4B','Applying a reciprocal transformation':'4C',
'Creating and using a rule for reducing balance depreciation':'7E','Modelling simple interest using a rule':'7C',
'Using financial applications of technology':'8E','Using amortisation tables to solve problems involving reducing balance loans':'8C',
'Using amortisation tables to solve problems involving amortising annuities':'8C','Interpreting and constructing dominance matrices':'10G',
'Calculating state matrices':'11C','Using Leslie matrices in applied scenarios':'11E','Determining the shortest path by inspection':'13D'}
BURNT={'CFAT 1.1.1':'1A Q15, Q17 · 1B Q8, Q9 · 1C Q6, Q17 · 1D Q9, Q12, Q14','CFAT 1.1.2':'1E Q1, Q8, Q11, Q14, Q17, Q18 · 1F Q12, Q16, Q18, Q19','CFAT 1.1.3':'1G Q4 · 1H Q8, Q11, Q13 · 1I Q1, Q4, Q9, Q12, Q15'}
used={}
for c,s in BURNT.items():
    for part in s.split('·'):
        les,*qs=part.split(); 
        for q in ' '.join(qs).replace(',',' ').split(): used[(les,int(q[1:]))]=c
rows=[];vflag=[]
for i in I:
    if i['section']=='exam':
        if (i['lesson'],i['q']) in used: vflag.append((i['lesson'],i['q'],used[(i['lesson'],i['q'])]))
        continue
    if i['vcaa']: continue
    sub='' if i['section']=='multi' else HEAD.get(i['heading'],LES[i['lesson']])
    rows.append(dict(edrolo_lesson=i['lesson'],q=i['q'],section={'skill':'skill','joining':'joining it all together','multi':'questions from multiple lessons'}[i['section']],
        skill_heading='' if i['section']!='skill' else (i['heading'] or ''),cambridge_sub=sub,pdf_page=i['pdf_page'],printed_page=i['pdf_page']-7,
        type='MC' if i['mc'] else 'short answer',parts=i['parts'] or '',used_in=used.get((i['lesson'],i['q']),''),stem_start=i['stem']))
w=csv.DictWriter(open('/home/claude/12mag/tools/y12_edrolo_exercise_questions.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows),collections.Counter(r['section'] for r in rows)); print('burnt',sum(1 for r in rows if r['used_in'])); print('VCAA reprints used in CFATs',vflag)
print(collections.Counter(r['type'] for r in rows))
