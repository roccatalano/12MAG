"""Prefill the Chapter 5 lesson cards (l16-l22) - queue task Ch5 #1, 15 Nov 2026 (runner).
Sources checked: Cambridge U3&4 2023 Ch 5 (Examples 1-23, CAS 1 time series plot, Exercises 5A-5E),
Edrolo U3&4 2023 Ch 4 worked examples (4A WE1-2, 4B WE1-3, 4C WE1-2, 4D WE1-6, 4E WE1-2),
tools/vcaa_current_index.csv (Do Now tags: index wins), tools/ledger*.csv (burnt).
Edrolo U1&2 has no time series chapter (not in the U1&2 study design), so Ex 2, 3, 5, 6 get written You trys.
"""
import json
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for ch in d['aos'][0]['chapters']:
    for l in ch['lessons']: L[l['id']]=l
def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
DN={
'gm12-u3-l16':dn(('Exam 1','VCAA 2023 Exam 1 Q12','4B'),('Exam 1','VCAA 2026 Exam 1 Q11','4C'),('Exam 2','VCAA 2024 Exam 2 Q3a','2A'),('Exam 2','VCAA 2025 NHT Exam 2 Q4d','2E')),
'gm12-u3-l17':dn(('Exam 1','VCAA 2024 Exam 1 Q12','4D'),('Exam 1','VCAA 2026 NHT Exam 1 Q10','4D'),('Exam 2','VCAA 2023 Exam 2 Q4a','5A'),('Exam 2','VCAA 2024 NHT Exam 2 Q4b','2G')),
'gm12-u3-l18':dn(('Exam 1','VCAA 2023 Exam 1 Q15','5B'),('Exam 1','VCAA 2024 NHT Exam 1 Q12','4D'),('Exam 2','VCAA 2025 Exam 2 Q4c','3B'),('Exam 2','VCAA 2024 Exam 2 Q4b','5A')),
'gm12-u3-l19':dn(('Exam 1','VCAA 2024 NHT Exam 1 Q14','5B'),('Exam 1','VCAA 2024 NHT Exam 1 Q5','1H'),('Exam 2','VCAA 2025 Exam 2 Q4d','3B'),('Exam 2','VCAA 2024 Exam 2 Q3b','3A')),
'gm12-u3-l20':dn(('Exam 1','VCAA 2023 Exam 1 Q13','5C'),('Exam 1','VCAA 2026 NHT Exam 1 Q3','1F'),('Exam 2','VCAA 2024 Exam 2 Q4a','5C'),('Exam 2','VCAA 2023 Exam 2 Q3d','3B')),
'gm12-u3-l21':dn(('Exam 1','VCAA 2023 Exam 1 Q16','5D'),('Exam 1','VCAA 2024 NHT Exam 1 Q13','5C'),('Exam 2','VCAA 2026 NHT Exam 2 Q4bi','5B'),('Exam 2','VCAA 2024 Exam 2 Q3gi','3C')),
'gm12-u3-l22':dn(('Exam 1','VCAA 2024 NHT Exam 1 Q15','5D'),('Exam 1','VCAA 2026 Exam 1 Q10','4B'),('Exam 2','VCAA 2023 Exam 2 Q4c','5D'),('Exam 2','VCAA 2026 Exam 2 Q1b','1B')),
}
YT={1:'Edrolo 4A WE1',2:'Written (modelled on Cambridge Ex 2) · YT-5A-2',3:'Written (modelled on Cambridge Ex 3) · YT-5A-3',
    4:'Edrolo 4A WE2',5:'Written (modelled on Cambridge Ex 5) · YT-5A-5',6:'Written (modelled on Cambridge Ex 6) · YT-5A-6',
    7:'Edrolo 4B WE1',8:'Edrolo 4B WE3',9:'Edrolo 4B WE2a–b',10:'Edrolo 4B WE2c',11:'Edrolo 4B WE2d',
    12:'Edrolo 4C WE1',13:'Edrolo 4C WE2',
    14:'Edrolo 4D WE1b',15:'Edrolo 4D WE5',16:'Edrolo 4D WE4',
    17:'Edrolo 4D WE1a',18:'Edrolo 4D WE2',19:'Edrolo 4D WE3',
    20:'Edrolo 4E WE1a',21:'Edrolo 4E WE1b–c',22:'Edrolo 4E WE2a',23:'Edrolo 4E WE2b–c'}
def hw(sub,items): return {'title':f'Cambridge · Exercise {sub}','items':[{'skill':s,'q':q} for s,q in items],'note':''}
HW={
'gm12-u3-l16':[hw('5A',[('Constructing a time series plot','Q1–3'),('Identifying key features in a time series plot','Q4–7'),('Describing time series plots','Q8–13'),('Exam 1 style questions','Q14–15')])],
'gm12-u3-l17':[hw('5B',[('Calculating the smoothed values of an odd number of points','Q1–3'),('Smoothing and plotting a time series plot (odd number of points)','Q4–5')])],
'gm12-u3-l18':[hw('5B',[('Calculating the smoothed values of an even number of points','Q6–8'),('Smoothing and plotting a time series plot (even number of points)','Q9–10'),('Exam 1 style questions','Q11–14')])],
'gm12-u3-l19':[hw('5C',[('Locating the median of a set of data points graphically','Q1'),('Smoothing a time series graphically','Q2–7'),('Exam 1 style questions','Q8–10')])],
'gm12-u3-l20':[hw('5D',[('Basic skills and interpretation','Q1–5'),('Exam 1 style questions','Q13–15')])],
'gm12-u3-l21':[hw('5D',[('Deseasonalising a time series','Q6–7'),('Calculating seasonal indices','Q8–12'),('Exam 1 style questions','Q16–17')])],
'gm12-u3-l22':[hw('5E',[('Fitting a least squares line to a time series plot (no seasonality)','Q1–4'),('Fitting a least squares line to a time series with seasonality','Q5–6'),('Exam 1 style questions','Q7–8')])],
}
CAS={'gm12-u3-l16':['time-series-plot'],'gm12-u3-l17':['moving-means'],'gm12-u3-l18':['moving-means'],'gm12-u3-l19':[],
     'gm12-u3-l20':[],'gm12-u3-l21':[],'gm12-u3-l22':['trend-line']}
NOTE={'gm12-u3-l16':'Edrolo 4A WE2 (seasonality + structural change, seat-belt law) pairs with Example 4; it also fits Example 5.',
      'gm12-u3-l21':'Edrolo 4D WE6 (plot deseasonalised data, identify the trend) is a spare You try for Example 19.'}
for i in DN:
    c=L[i]['card']; c['doNow']=DN[i]
    for w in c.get('weDo',[]): w['youTry']=YT.get(w['n'])
    subs=sorted({s['title'][-2:] for s in HW[i]})
    c['homework']={'source':'prefill','sets':HW[i]+[{'title':'Revision book','items':[],'note':'The '+', '.join(subs)+' section'+('s' if len(subs)>1 else '')}]}
    c['cas']=CAS[i]
    if i in NOTE: c['note']=NOTE[i]
L['gm12-u3-l16']['card']['casYouTry']='Edrolo 4A WE1 (time series plot on CAS)'
L['gm12-u3-l22']['card']['casYouTry']='Edrolo 4E WE1a (trend line on CAS)'
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# written You trys
W='planner/written-youtrys.json'; w=json.load(open(W))
new=[
 {'id':'YT-5A-2','pairs':'Cambridge U3&4 Example 2','sub':'5A','label':'Written for 12MAG (Claude, modelled on Cambridge Example 2)',
  'text':'Consider the time series plot of the number of visitors (in thousands) to a national park each year from 2008 to 2022, constructed from the data below. Comment on the trend shown in the plot. Year: 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022; Visitors (\'000): 41 44 48 51 55 58 62 60 57 53 50 46 44 41 38',
  'answer':'There are two distinct trends. Trend 1: from 2008 to 2014 the number of visitors increased steadily (from 41 000 to 62 000). Trend 2: from 2014 to 2022 the number of visitors decreased steadily (from 62 000 to 38 000).'},
 {'id':'YT-5A-3','pairs':'Cambridge U3&4 Example 3','sub':'5A','label':'Written for 12MAG (Claude, modelled on Cambridge Example 3)',
  'text':'The following plot shows the number of mice caught each year on a farm for the period 2000 to 2023, constructed from the data below. Comment on the cycles shown in the plot. Year 2000–2023; Mice caught: 20 45 90 60 30 15 25 55 95 70 35 20 15 40 85 65 30 20 30 60 100 70 35 20',
  'answer':'There is a recurrent pattern of peaks and troughs lasting longer than a year, so the plot shows cycles. The years of highest numbers of mice caught are approximately 2002, 2008, 2014 and 2020, so the cycle repeats about every 6 years.'},
 {'id':'YT-5A-5','pairs':'Cambridge U3&4 Example 5','sub':'5A','label':'Written for 12MAG (Claude, modelled on Cambridge Example 5)',
  'text':'The time series plot below shows the water use for a house (in kL) for the 12 months of a year, constructed from the data below. Comment on any structural change in the plot. Month: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec; Water use (kL): 22 21 23 22 20 21 38 37 39 38 40 39',
  'answer':'The plot reveals an abrupt change in water use from June to July. Monthly water use suddenly increases from around 21 kL per month from January to June to around 38 kL for the rest of the year. This is an example of structural change that can probably be explained by a change in circumstances, for example, more people moving into the house.'},
 {'id':'YT-5A-6','pairs':'Cambridge U3&4 Example 6','sub':'5A','label':'Written for 12MAG (Claude, modelled on Cambridge Example 6)',
  'text':'The time series plot below shows the number of coffees sold each day at a café for a fortnight, constructed from the data below. Comment on any outliers in the plot. Day 1–14; Coffees sold: 82 85 80 84 83 81 86 84 150 83 82 85 80 84',
  'answer':'The number of coffees sold is around 80–86 each day, except on day 9 when 150 coffees were sold. This value stands out from the rest of the data, so day 9 is an outlier (perhaps there was a special event nearby that day).'},
]
ids={x['id'] for x in w['items']}
w['items']+=[x for x in new if x['id'] not in ids]
json.dump(w,open(W,'w'),indent=1,ensure_ascii=False)

# CAS steps (time series plot, trend line); moving-means left for first use (l17)
C='planner/cas-skills.json'; cs=json.load(open(C)); S=cs if isinstance(cs,list) else cs['skills']
for k in S:
    if k['id']=='time-series-plot' and not k['ti']:
        k['ti']=['Lists & Spreadsheet: enter the time (coded 1, 2, 3 … if needed) and the values in named lists (e.g. year, birth).',
                 'Add Data & Statistics: time on the horizontal axis, values on the vertical axis.',
                 'Menu › Plot Properties › Connect Data Points to join the points into a time series plot.']
        k['classpad']=['Statistics app: enter the time (coded 1, 2, 3 … if needed) in list1 and the values in list2 (or name the columns).',
                       'SetGraph › Setting: Type = xyLine, XList = time, YList = values; Set.',
                       'Tap the graph icon to draw the time series plot.']
        k['tip']='Time is always the explanatory variable (horizontal axis). Code months or quarters as 1, 2, 3 … first.'
        k['checked']='Cambridge U3&4 5A CAS 1 + Edrolo 4A WE1 (Draft, check against 02 Sources\\CAS guides)'
    if k['id']=='trend-line' and not k['ti']:
        k['ti']=['Lists & Spreadsheet: enter the time (coded 1, 2, 3 …) and the (deseasonalised) values in named lists.',
                 'Menu › Statistics › Stat Calculations › Linear Regression (a+bx): X List = time, Y List = values; OK.',
                 'Write the trend line in the variable names, e.g. deseasonalised sales = 903.8 − 38.1 × month.']
        k['classpad']=['Statistics app: time in list1, (deseasonalised) values in list2 (or name the columns).',
                       'Calc › Regression › Linear Reg; form y = a + b·x; XList = time, YList = values; OK.',
                       'Write the trend line in the variable names, e.g. deseasonalised sales = 903.8 − 38.1 × month.']
        k['tip']='With seasonal data, fit the line to the DESEASONALISED values, then reseasonalise the forecast (× seasonal index).'
        k['checked']='Cambridge U3&4 5E + Edrolo 4E WE2a (Draft, check against 02 Sources\\CAS guides)'
json.dump(cs,open(C,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('5A','Time series data and their features'),('5B','Smoothing with moving means (and centring)'),('5C','Moving median smoothing'),('5D','Seasonal indices, deseasonalising and reseasonalising'),('5E','Fitting a trend line and forecasting')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)
print('ok')
