"""Lesson 3 (1F) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S3-slides.html
Run: python3 tools/deck/s3/build.py

Sources (all question text verbatim, copied from the previous S3 deck which copied it from the sources):
- CFAT 1.1.1 (1A-1E) at the start.
- Do Now: removed from the deck (Rocco, 16 Nov); the planner card list is unchanged.
- APK: Cambridge U1&2 Ch 2 skills checklist 2E #10, 2F #11 · Edrolo U1&2 1D Q18 = VCAA 2017 E2 Q1ai (87%).
- Examples 14-21 (Cambridge U3&4 1F) · You trys: Edrolo U3&4 1E WE1, 1F WE2a, 1F WE3a, 1E WE2a, 1E WE2b, (none for Ex 19), 1F WE1a, 1G WE1; CAS You try 1G WE2.
- Exit: Edrolo U3&4 1G Q11 = adapted from VCAA 2020 E2 Q4aii (Edrolo: 77%), checked verbatim against the Edrolo PDF (printed p. 86).
  The old second exit (VCAA 2026 NHT E2 Q1b, d: current design, 1G content, not on the card) is removed. The only unburnt Edrolo 1F
  exam-practice item is 1F Q17 = VCAA 2019 E1 Data analysis Q2 (86%), but it tests histogram shape (1C), so it was not added."""
import os, sys, json
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
import tpl as TPL
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'; EDR12='Edrolo General Mathematics Units 1&amp;2'
def G(pre,fig,post=''):
    return f'<div>{pre}</div><div style="margin:14px 0;display:flex;justify-content:center">{fig}</div>'+(f'<div>{post}</div>' if post else '')
def B(cls,val,ph='&nbsp;'): return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def seq(rid,vals,fs=24,gaps=()):
    out=''
    for k,v in enumerate(vals):
        if k in gaps: out+='<span class="gap"></span>'
        out+=f'<span data-i="{k}">{v}</span>'
    return f'<div class="seqrow" id="{rid}" style="font-size:{fs}px">{out}</div>'
def data(vals,fs=24): return f'<span class="data" style="font-size:{fs}px;word-spacing:.35em">{vals}</span>'
def vid(n): return f'Cambridge GO · Example {n} (1F Resources)'
SB='<div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 22px;display:inline-block">{}</div>'
FPOS=F('position = ',FR(['<i>n</i> + 1'],['2'])); FMED=F('M = ',FR(['first middle + second middle'],['2']))
FRNG=F('range = largest − smallest'); FIQR=F('IQR = Q<sub>3</sub> − Q<sub>1</sub>'); FMEAN=F('<i>x̄</i> = ',FR(['Σ<i>x</i>'],['<i>n</i>']))
FSD=F('<i>s</i> = √',FR(['Σ(<i>x</i> − <i>x̄</i>)²'],['<i>n</i> − 1']))
S=[]
def FIVE(*v):
    """five-number summary as a 2-row × 5-column table (Rocco, 16 Nov: use this style for every five-number summary)"""
    h=['min','Q<sub>1</sub>','M','Q<sub>3</sub>','max']
    return ('<table class="t" style="font-size:22px;margin-top:8px;text-align:center"><tr>'+''.join(f'<th style="text-align:center">{x}</th>' for x in h)+'</tr><tr>'
            +''.join(f'<td style="min-width:64px"><b>{x}</b></td>' for x in v)+'</tr></table>')
# ================= opening
S.append(title(3,'Measures of centre and spread','Cambridge General Mathematics Units 3&amp;4 · 1F Using summary statistics to describe numerical distributions: median, quartiles, IQR, mean and standard deviation','S3',
  flow=('CFAT','APK','Learn','Worked examples','You try','Exit tasks')))
LI=['To be able to understand the mean and the median as measures of centre.',
    'To be able to understand the range, interquartile range and standard deviation as measures of spread.',
    'To be able to know whether to use the median and interquartile range, or the mean and standard deviation, for a particular distribution.',
    'To be able to use a CAS calculator to calculate these summary statistics.']
SC=['I can find the median value in a data set.','I can find the median value from a dot plot.','I can find the median value from a stem plot.','I can find the range from a stem plot.',
    'I can find the IQR from a stem plot when n is even.','I can find the IQR from a stem plot when n is odd.','I can calculate the mean using the formula.','I can calculate the mean and standard deviation using the CAS calculator.']
S.append(today(LI,SC,[('CFAT 1.1.1','· 20 minutes, 1A–1E','#00838F'),('APK','· Year 11 skills, one VCAA question','var(--apk)'),
  ('The median','→ WE 14, 15, 16',None),('Range, quartiles and IQR','→ WE 17, 18, 19, 20',None),('The mean','→ WE 21',None),('Mean or median? Standard deviation','· CAS',None),
  ('Exit task','· one VCAA question','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(keys([
  ('Median (M)','the middle value of the ordered data'),('Mean (<i>x̄</i>)','the sum of the values divided by <i>n</i>: the balance point'),
  ('Range','largest value minus smallest value'),('Quartiles (Q<sub>1</sub>, Q<sub>3</sub>)','split the ordered data into four equal groups; Q<sub>1</sub> = median of the lower half, Q<sub>3</sub> = median of the upper half'),
  ('IQR','the spread of the middle 50% of the data'),('Standard deviation (<i>s</i>)','the spread of the data around the mean; on CAS it is <b>s<sub>x</sub></b>')],
  [('Median position',FPOS),('Median, n even',FMED),('Range',FRNG),('Interquartile range',FIQR),('Mean',FMEAN),('Standard deviation',FSD,'use CAS: s<sub>x</sub>, not σ<sub>x</sub>')],
  'Cambridge General Mathematics Units 3&amp;4, 1F pp. 44–52'))
S.append(cfat('CFAT 1.1.1','types of data, displays, log scales','1A–1E',13,'CFAT 1.1.1 (1A-1E): student copy and solutions on the planner'))
# ================= APK
PARTY=[('1',[7,9,9,9]),('2',[0,0,1,1,2,3,6,7,8,9]),('3',[4,4,7]),('4',[5]),('5',[6]),('6',[6])]
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2E #10, 2F #11','What do you remember?',
  '<div style="display:flex;gap:24px;align-items:center"><div style="flex:1">The ages of a group of people at a party:<div style="margin:8px 0">'+data('19 21 22 56 34 19 27 28 34 17<br>66 37 20 20 21 45 26 19 23 29',22)+'</div></div>'+SB.format(stem('apks',PARTY,'Key: 1 | 7 = 17',20))+'</div>'
  +plist([('a','Determine the mean and median of the ages of the people at the party. Which is the preferred measure of centre?'),
     ('b','Determine the quartiles and hence the IQR of the ages of the people at the party.')]),
  [fx('Mean','<i>x̄</i>',F(FR([V('Σ<i>x</i>','583')],[V('<i>n</i>','20')])),'29.15','data-pk="0"'),
   ('Median','n = 20: average the 10th and 11th, (23 + 26) ÷ 2 = 24.5','data-pk="0" data-mark="#apks|9,10|mid"'),
   ('Which?','outliers (56, 66) and a skewed shape pull the mean up: use the median.','data-pk="0"'),
   ('ANS','<b>a</b> &nbsp;<i>x̄</i> = 29.15, M = 24.5. The <b>median</b> is preferred (skewed, outliers 56 and 66).','data-pk="0"'),
   ('Quartiles','Q<sub>1</sub> = (20 + 20) ÷ 2 = 20 · Q<sub>3</sub> = (34 + 34) ÷ 2 = 34','data-pk="1" data-mark="#apks|4,5,14,15|q1m"'),
   fx('Interquartile range','IQR',F(V('Q<sub>3</sub>','34'),' − ',V('Q<sub>1</sub>','20')),'14','data-pk="1"'),
   ('ANS','<b>b</b> &nbsp;Q<sub>1</sub> = 20, Q<sub>3</sub> = 34, <b>IQR = 14</b>','data-pk="1"')],
  '','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2E #10, 2F #11 (teacher solutions)',cmd=('Determine',None,'values, then a choice')))
EGGS=[172,192,159,125,197,135,140,140,138,166,136,131]
S.append(qslide('apk','APK · VCAA 2017 Exam 2 Q1ai','A real VCAA question you can already do',
  'The number of eggs counted in a sample of 12 clusters of moth eggs is recorded in the following table.'
  f'<table class="t" id="egg" style="font-size:20px;margin:14px 0;width:100%"><tr><th class="l"><em class="v">number of eggs</em></th>'+''.join(f'<td><span data-i="{i}">{x}</span></td>' for i,x in enumerate(EGGS))+'</tr></table>'
  'From the information given, determine the range. <span class="muted">(1 mark)</span>',
  [('Extremes','largest = 197, smallest = 125','data-hi="#egg|4,3|hy"'),fx('Range','range',F(V('largest','197'),' − ',V('smallest','125')),'72')],
  'The range is <b>72</b> eggs.',f'{EDR12} · 1D Q18 · VCAA 2017 Exam 2 Data analysis Q1ai',stat=('mc',87),cmd=('determine',1,'one value')))
# ================= Learn: overview
S.append(learn('Learn · 1F','Two questions about any distribution',
  '<h4>Where is the centre? How spread out is it?</h4><p><b style="color:#d2475b">Centre:</b> median M (the middle value) · mean <i>x̄</i> (the balance point)<br><b style="color:#6a3fc7">Spread:</b> range · IQR (the middle 50%) · standard deviation <i>s</i> (spread around the mean)</p>',
  '<div class="row" style="gap:30px;justify-content:center;font-size:26px"><div class="key frag" style="flex:1;text-align:center"><b>median</b> goes with <b>IQR</b><br><small>resistant: outliers barely move them</small></div><div class="key frag" style="flex:1;text-align:center"><b>mean</b> goes with <b>standard deviation</b><br><small>use when symmetric, no outliers</small></div></div>',
  '<b>They come in pairs:</b> median with IQR · mean with standard deviation. In a SOCS answer, C and S use the same pair.',
  'Cambridge General Mathematics Units 3&amp;4, 1F pp. 44, 50–52',cards=[kcard('Median position',FPOS),kcard('Mean',FMEAN)]))
# The median (Rocco, 16 Nov: like the 10MA 'Finding the median step by step' slide, with the (n + 1)/2 position step)
MO=[19,3,26,12,34,1,24,15,30,21,27]; ME=[9,3,12,5,10,2,14,6,11,4]
def _mcol(h,t,steps,k0):
    return f'<div style="flex:1;min-width:0"><p style="font-size:21px;margin:0 0 6px"><b>{h}</b></p>{t}<div style="margin-top:34px">{isteps(steps,k0)}</div></div>'
S.append(islide('Learn · 1F','The median: the middle value',
  '<p style="font-size:22px;margin:0 0 12px">The median is the middle value in an ordered data set. For <i>n</i> data values it is at the '+F(FR(['<i>n</i> + 1'],['2']))+'th position.</p>'
  '<div class="row" style="gap:36px;align-items:flex-start">'
  +_mcol('Odd number of values',tiles('mo',MO,fs=20),[('Write the data in order. Count them: <i>n</i> = 11',tsort('mo')),
      ('Position: (11 + 1) ÷ 2 = <b>6th</b> value',''),('Cross off the smallest and the largest, again and again: one value is left. <b>M = 21</b>',tmed('mo',label='M = 21'))],1)
  +_mcol('Even number of values',tiles('me',ME,fs=20),[('Write the data in order. Count them: <i>n</i> = 10',tsort('me')),
      ('Position: (10 + 1) ÷ 2 = <b>5.5th</b>: halfway between the 5th and 6th values',''),
      ('Cross off pairs: two values are left, 6 and 9. The median sits on the line between them: <b>M = (6 + 9) ÷ 2 = 7.5</b>',tmed('me',label='M = 7.5',line=True))],4)
  +'</div>',
  'Rule: Cambridge General Mathematics Units 3&amp;4, 1F p. 44 · Data and steps: teacher example (as in the 10MA deck)'))
# ================= WE14 / YT
A14=[2,9,1,8,3,5,3,8,1]; B14=[10,1,3,4,8,6,10,1,2,9]
S.append(qslide('we','Worked example 14 · 1F','Finding the median value in a data set',
  'Order each of the following data sets, locate the median, and then write down its value.'+plist([('a','<div style="width:540px">'+tiles('w14a',A14,fs=24)+'</div>'),('b','<div style="width:540px">'+tiles('w14b',B14,fs=24)+'</div>')]),
  [('Order','n = 9 (odd)','data-pk="0" '+tsort('w14a')),fx('Median position',None,F(FR([V('<i>n</i>','9'),' + 1'],['2'])),'5th value','data-pk="0"'),
   ('Cross off','four pairs from the ends: the 5th value is left','data-pk="0" '+tmed('w14a',label='M = 3')),
   ('ANS','<b>a</b> &nbsp;M = <b>3</b>','data-pk="0"'),
   ('Order','n = 10 (even)','data-pk="1" '+tsort('w14b')),fx('Median position',None,F(FR([V('<i>n</i>','10'),' + 1'],['2'])),'5.5th: average the 5th and 6th','data-pk="1"'),
   ('Cross off','four pairs from the ends: 4 and 6 are left; the median sits on the line between them','data-pk="1" '+tmed('w14b',label='M = 5',line=True)),
   fx('Median, n even','M',F(FR([V('5th','4'),' + ',V('6th','6')],['2'])),'5','data-pk="1"'),
   ('ANS','<b>b</b> &nbsp;M = <b>5</b>','data-pk="1"')],
  '',f'{CAM} · Example 14',video=vid(14),cmd=('locate',None,'order first, then count in')))
D1E=[3,5,1,10,8,9,6,3,8,6]; YQ=tquart('y14',10,'Q₁ = 3','Q₃ = 8')
S.append(qslide('yt','You try · Edrolo 1E WE1','Finding the median value in a data set',
  'Construct a five-number summary for the following data.<div style="margin:12px 0">'+tiles('y14',D1E,fs=26)+'</div>',
  [('Order','n = 10; min = 1, max = 10',tsort('y14')),
   ('Median','(10 + 1) ÷ 2 = 5.5th position: (6 + 6) ÷ 2 = 6',tmed('y14',label='M = 6',line=True)),
   ('Halves','n is even: five values in each half',YQ[0]),
   ('Q₁','median of the lower half = 3',YQ[1]),('Q₃','median of the upper half = 8',YQ[2])],
  'Five-number summary:'+FIVE(1,3,6,8,10),f'{EDR} · 1E Worked example 1',cmd=('Construct',None,'min, Q₁, M, Q₃, max')))
CRIC=[18,18,19,19,22,22,22,22,23,23,24,25,29]
S.append(qslide('we','Worked example 15 · 1F','Finding the median value from a dot plot',
  G('The dot plot opposite displays the age distribution (in years) of the 13 members of a local cricket team.','<div style="width:600px">'+dot('w15d',{"min":17,"max":30,"vals":CRIC,"xl":"Age (years)","W":760,"h":230,"r":12})+'</div>',
    'Determine the median age of these cricketers and mark its location on the dot plot.'),
  [('Count','13 dots'),fx('Median position',None,F(FR([V('<i>n</i>','13'),' + 1'],['2'])),'7th value'),
   ('Locate','count in from the left: 18, 18, 19, 19, 22, 22, <b>22</b>','data-dotmark="#w15d|6"')],
  'The median age is <b>22 years</b> (marked on the plot).',f'{CAM} · Example 15',video=vid(15),cmd=('Determine',None,'the value, marked on the plot')))
ED2=[23]+[24]*2+[25]*4+[26]*4+[27]*7+[28]*5+[29]*3+[30,31]
S.append(qslide('yt','You try · Edrolo 1F WE2a','Finding the median value from a dot plot',
  G('Consider the dot plot.','<div style="width:600px">'+dot('y15d',{"min":22,"max":31,"vals":ED2,"W":760,"h":290,"r":11})+'</div>','<b>a.</b> Determine the median.'),
  [('Count','28 data points'),fx('Median position',None,F(FR([V('<i>n</i>','28'),' + 1'],['2'])),'14.5th: average the 14th and 15th',ra='data-dsplit="#y15d|13|14.5th"'),
   fx('Median, n even','M',F(FR([V('14th','27'),' + ',V('15th','27')],['2'])),'27',ra='data-dotmark="#y15d|13,14|#d98a1f"')],
  'The median is <b>27</b>.',f'{EDR} · 1F Worked example 2a',cmd=('Determine',None,'one value')))
W16=[('1',[8,9,9]),('2',[0,2,5,7,8,9,9]),('3',[1,3])]
S.append(qslide('we','Worked example 16 · 1F','Finding the median value from a stem plot',
  G('The stem plot opposite displays the maximum temperature (in °C) for 12 days in January.',SB.format(stem('w16s',W16,'Key: 0|8 = 8°C',28)),'Determine the median maximum temperature for these 12 days.'),
  [fx('Median position',None,F(FR([V('<i>n</i>','12'),' + 1'],['2'])),'6.5th: average the 6th and 7th'),
   ('Locate','count in from both ends: 25 and 27','data-count="#w16s"'),fx('Median, n even','M',F(FR([V('6th','25'),' + ',V('7th','27')],['2'])),'26')],
  'The median maximum temperature is <b>26°C</b>.',f'{CAM} · Example 16',video=vid(16),cmd=('Determine',None,'one value')))
E3=[('40',[7]),('41',[]),('42',[]),('43',[]),('44',[4,6]),('45',[1,3,3]),('46',[2,6,7]),('47',[4,7,8,9]),('48',[0,0,4,5,6,8]),('49',[1,2,5,5,5,9]),('50',[3,4,4,7,8,8,9,9])]
S.append(qslide('yt','You try · Edrolo 1F WE3a','Finding the median value from a stem plot',
  '<div style="display:flex;gap:24px;align-items:flex-start"><div style="flex:1">Consider the stem plot.<br><br><b>a.</b> Calculate the median.</div>'+SB.format(stem('y16s',E3,'Key: 40 | 7 = 407',20))+'</div>',
  [('Count','33 data points'),fx('Median position',None,F(FR([V('<i>n</i>','33'),' + 1'],['2'])),'17th'),('Locate','count in 16 from each end','data-count="#y16s"')],
  'The median is <b>485</b>.',f'{EDR} · 1F Worked example 3a',cmd=('Calculate',None,'one value')))
# ================= Learn: quartiles
S.append(TPL._frame('learn','Learn · 1F','Quartiles cut the ordered data into quarters',
  '<script>/* Rocco, 16 Nov: the middle-50% cut lines. n odd: through Q1 (5) and Q3 (14) tiles (6 values inside, 5 outside);\nn even: between 5|7 and 14|16 (6 inside, 6 outside) */\nfunction qCut(){const box=document.getElementById(\'qx\');if(!box||!box._g)return;const {W,G}=box._g;\n  box.querySelectorAll(\'.band\').forEach((b,ri)=>{const cs=[...box.querySelectorAll(`.chip3[data-r="${ri}"]`)];if(!cs.length)return;\n    const x=k=>parseFloat(cs[k].style.left);let L,R;\n    if(ri===0){L=x(2)+W/2;R=x(8)+W/2}else{L=x(3)-G/2;R=x(9)-G/2}\n    b.style.left=L+\'px\';b.style.width=(R-L)+\'px\';b.style.zIndex=3;b.style.pointerEvents=\'none\';b.style.borderRadius=\'0\';\n    b.style.background=\'rgba(47,111,223,.10)\';b.style.borderTop=b.style.borderBottom=\'none\';b.style.borderLeft=b.style.borderRight=\'3px dashed var(--we)\';\n    b.style.top=(parseFloat(cs[0].style.top)-14)+\'px\';b.style.height=\'80px\'})}\nwindow.addEventListener(\'load\',qCut);window.addEventListener(\'resize\',()=>setTimeout(qCut,50));</script><div class="xp" id="qx" style="height:400px"></div><span class="frag" data-act="q-0-m"></span><span class="frag" data-act="q-0-q"></span><span class="frag" data-act="q-0-band"></span><span class="frag" data-act="q-1-show"></span><span class="frag" data-act="q-1-m"></span><span class="frag" data-act="q-1-q"></span><span class="frag" data-act="q-1-band"></span>'
  '<div class="row" style="gap:20px;margin-top:12px">'+kcard('Range',FRNG).replace('class="kf"','class="kf frag"')+kcard('Interquartile range',FIQR,'Q<sub>1</sub> = median of lower half · Q<sub>3</sub> = median of upper half (n odd: leave the median out)').replace('class="kf"','class="kf frag"')+'</div>',
  'Cambridge General Mathematics Units 3&amp;4, 1F pp. 46–47 · Animation data: teacher example',cfu='disc'))
S.append(qslide('we','Worked example 17 · 1F','Finding the range from a stem plot',
  G('The stem plot opposite displays the maximum temperature (in °C) for 12 days in January.',SB.format(stem('w17s',W16,'Key: 0|8 = 8°C',28)),'Determine the temperature range over these 12 days.'),
  [('Extremes','lowest = 18, highest = 33','data-mark="#w17s|0,11|ext"'),fx('Range','R',F(V('largest','33'),' − ',V('smallest','18')),'15')],
  'The temperature range is <b>15°C</b>.',f'{CAM} · Example 17',video=vid(17),cmd=('Determine',None,'one value with units')))
NET=[('2',[2,3,5,7,9]),('3',[0,1,3,5,7,7,8]),('4',[0,1,2,2])]
S.append(qslide('yt','You try · Edrolo 1E WE2a','Finding the range from a stem plot',
  G('The following stem plot displays the number of <em class="v">goals scored</em> by 16 netball teams over a season.',SB.format(stem('y17s',NET,'Key: 2 | 2 = 22 goals',28)),'<b>a.</b> Calculate the range of <em class="v">goals scored</em>.'),
  [('Extremes','minimum = 22, maximum = 42','data-mark="#y17s|0,15|ext"'),fx('Range','range',F(V('max','42'),' − ',V('min','22')),'20')],
  'The range is <b>20 goals</b>.',f'{EDR} · 1E Worked example 2a',cmd=('Calculate',None,'one value')))
CATS=[('1',[9]),('2',[1,3,5,8]),('3',[0,0,4,9,9]),('4',[0,4,5,8]),('5',[0,3]),('6',[3,4])]
S.append(qslide('we','Worked example 18 · 1F','Finding the IQR from an ordered stem plot when n is even',
  G('Find the interquartile range of the weights of the 18 cats whose weights are displayed in the ordered stem plot below.',
    SB.format('<div style="font-weight:700;font-size:18px">Weight (kg)</div>'+stem('w18s',CATS,'1 | 2 represents 1.2 kg',26))),
  [('Split','18 values: nine in the lower ‘half’, nine in the upper ‘half’.'),
   ('Q₁','lower half 1.9 2.1 2.3 2.5 <b>2.8</b> 3.0 3.0 3.4 3.9: Q<sub>1</sub> = 2.8','data-count="#w18s|0|8|q1m"'),
   ('Q₃','upper half 3.9 4.0 4.4 4.5 <b>4.8</b> 5.0 5.3 6.3 6.4: Q<sub>3</sub> = 4.8','data-count="#w18s|9|17|q1m"'),
   fx('Interquartile range','IQR',F(V('Q<sub>3</sub>','4.8'),' − ',V('Q<sub>1</sub>','2.8')),'2.0')],
  'The IQR is <b>2.0 kg</b>.',f'{CAM} · Example 18',video=vid(18),cmd=('Find',None,'Q₁, Q₃, then IQR')))
S.append(qslide('yt','You try · Edrolo 1E WE2b','Finding the IQR from an ordered stem plot when n is even',
  G('The following stem plot displays the number of <em class="v">goals scored</em> by 16 netball teams over a season.',SB.format(stem('y18s',NET,'Key: 2 | 2 = 22 goals',28)),'<b>b.</b> Calculate the IQR of <em class="v">goals scored</em>.'),
  [('Split','n = 16: median position (16 + 1) ÷ 2 = 8.5, so 8 values in each half.'),
   ('Q₁','22 23 25 27 29 30 31 33: Q<sub>1</sub> = (27 + 29) ÷ 2 = 28','data-count="#y18s|0|7|q1m"'),
   ('Q₃','35 37 37 38 40 41 42 42: Q<sub>3</sub> = (38 + 40) ÷ 2 = 39','data-count="#y18s|8|15|q1m"'),
   fx('Interquartile range','IQR',F(V('Q<sub>3</sub>','39'),' − ',V('Q<sub>1</sub>','28')),'11')],
  'The IQR is <b>11 goals</b>.',f'{EDR} · 1E Worked example 2b',cmd=('Calculate',None,'Q₁, Q₃, then IQR')))
LIFE=[('5',[2]),('5',[5,6]),('6',[4]),('6',[6,6,7,9]),('7',[1,2,2,3,3,4,4,4,4]),('7',[5,5,6,6,7,7])]
S.append(qslide('we','Worked example 19 · 1F','Finding the IQR from an ordered stem plot when n is odd',
  G('The stem plot shows the life expectancy (in years) for 23 countries. Find the IQR for life expectancies.',SB.format(stem('w19s',LIFE,'Stem: 5|2 = 52 years',24))),
  [('Median','23 values: the 12th value from either end, 73','data-count="#w19s"'),('Leave it out','n is odd: 11 values below the median, 11 above it.'),
   ('Q₁','midpoint of the bottom 11 = 66','data-count="#w19s|0|10|q1m"'),('Q₃','midpoint of the top 11 = 75','data-count="#w19s|12|22|q1m"'),
   fx('Interquartile range','IQR',F(V('Q<sub>3</sub>','75'),' − ',V('Q<sub>1</sub>','66')),'9')],
  'The IQR is <b>9 years</b>.',f'{CAM} · Example 19 (no matching Edrolo worked example, so no You try)',video=vid(19),cmd=('Find',None,'Q₁, Q₃, then IQR')))
CQ=tquart('tcat',18,'Q₁ = 2.8','Q₃ = 4.8'); LQ=tquart('tlife',23,'Q₁ = 66','Q₃ = 75')
S.append(islide('Learn · 1F','Quartiles are medians of the halves: n even vs n odd',
  '<p style="font-size:20px;margin:0 0 4px"><b>Example 18</b> · 18 cat weights (kg)</p>'+tiles('tcat',[f'{x:.1f}' for x in [1.9, 2.1, 2.3, 2.5, 2.8, 3.0, 3.0, 3.4, 3.9, 3.9, 4.0, 4.4, 4.5, 4.8, 5.0, 5.3, 6.3, 6.4]],fs=19)
  +'<p style="font-size:20px;margin:10px 0 4px"><b>Example 19</b> · 23 life expectancies (years)</p>'+tiles('tlife',[52, 55, 56, 64, 66, 66, 67, 69, 71, 72, 72, 73, 73, 74, 74, 74, 74, 75, 75, 76, 76, 77, 77],fs=19)
  +'<div class="row2" style="margin-top:8px">'+isteps([('n = 18: cross off pairs, M = (3.9 + 3.9) ÷ 2 = 3.9',tmed('tcat',label='M = 3.9')),('Split: 9 in each half',CQ[0]),('Q₁ = 2.8',CQ[1]),('Q₃ = 4.8 · IQR = 2.0',CQ[2])])
  +isteps([('n = 23: cross off pairs, M = 73 (12th)',tmed('tlife',label='M = 73')),('Split: leave the median out, 11 each side',LQ[0]),('Q₁ = 66',LQ[1]),('Q₃ = 75 · IQR = 9',LQ[2])],5)+'</div>'
  +'<div class="tip" style="font-size:21px;margin-top:10px"><b>Tip:</b> for small data sets it is usually a lot easier to get Q<sub>1</sub> and Q<sub>3</sub> from CAS (One-Variable Statistics) than by hand. Use the halves to check.</div>',
  f'{CAM} · Examples 18 and 19 (data from the stem plots, already ordered)'))
S.append(qslide('we','Worked example 20 · 1F','Finding the median and quartiles from a histogram',
  G('The histogram shows the average number of hours per week a group of 23 people spent on the internet. Find possible values for the median and quartiles of this distribution.',
    '<div style="width:560px">'+hist('w20h',{"start":10,"w":10,"v":[1,0,0,2,4,5,3,6,2],"ymax":7,"ystep":1,"xl":"internet hours per week","yl":"Frequency","h":340,"W":600,"fs":16})+'</div>'),
  [fx('Median position',None,F(FR([V('<i>n</i>','23'),' + 1'],['2'])),'12th value'),
   ('Running totals','add the frequencies from left to right: 1, 3, 7, 12, …','data-cum="#w20h"'),
   ('Median','12th value from the bottom: the 60–70 interval','data-hlbar="#w20h|5|#d2475b"'),
   ('Q₁','11 values below the median: (11 + 1) ÷ 2 = 6th value from the bottom: the 50–60 interval','data-hlbar="#w20h|4|#7b4fd6"'),
   ('Q₃','6th value from the top (2 + 6): the 80–90 interval','data-hlbar="#w20h|7|#7b4fd6"')],
  'Median: 60–70 hours · Q<sub>1</sub>: 50–60 hours · Q<sub>3</sub>: 80–90 hours.',f'{CAM} · Example 20',video=vid(20),cmd=('Find',None,'an interval for each')))
S.append(qslide('yt','You try · Edrolo 1F WE1a','Finding the median and quartiles from a histogram',
  G('Consider the histogram.','<div style="width:560px">'+hist('y20h',{"start":1,"w":1,"v":[3,15,12,13,9,5,2],"ymax":16,"ystep":4,"yl":"frequency","h":340,"W":580,"fs":16})+'</div>','<b>a.</b> Estimate the median.'),
  [('Count','3 + 15 + 12 + 13 + 9 + 5 + 2 = 59 data points'),fx('Median position',None,F(FR([V('<i>n</i>','59'),' + 1'],['2'])),'30th value'),
   ('Running totals','3, 18, 30, …: the 30th data point is in the 3–&lt;4 interval','data-cum="#y20h"'),
   ('Estimate','the middle of the interval: (3 + 4) ÷ 2 = 3.5','data-hlbar="#y20h|2|#d98a1f"')],
  'The median is approximately <b>3.5</b>.',f'{EDR} · 1F Worked example 1a',cmd=('Estimate',None,'one value')))
# ================= Learn: mean
RT='38 36 35 43 46 64 48 25'
S.append(qslide('we','Worked example 21 · 1F','Calculating the mean from the formula',
  'The following is a set of reaction times (in milliseconds):<div style="margin:12px 0">'+data(RT)+'</div>Write down the values of the following, correct to one decimal place.'
  +plist([('a','<i>n</i>'),('b','Σ<i>x</i>'),('c','<i>x̄</i>')]),
  [('Count','<i>n</i> = the number of data values','data-pk="0"'),('ANS','<b>a</b> &nbsp;<i>n</i> = <b>8</b>','data-pk="0"'),
   ('Add','38 + 36 + 35 + 43 + 46 + 64 + 48 + 25','data-pk="1"'),('ANS','<b>b</b> &nbsp;Σ<i>x</i> = <b>335</b>','data-pk="1"'),
   fx('Mean','<i>x̄</i>',F(FR([V('Σ<i>x</i>','335')],[V('<i>n</i>','8')])),'41.875 → 41.9','data-pk="2"'),('ANS','<b>c</b> &nbsp;<i>x̄</i> = <b>41.9</b>','data-pk="2"')],
  '',f'{CAM} · Example 21',video=vid(21),cmd=('Write down',None,'three values')))
S.append(qslide('yt','You try · Edrolo 1G WE1','Calculating the mean from the formula',
  'The amount of money spent, in dollars, of 10 customers at a supermarket is shown. Calculate the mean amount of money spent.<div style="margin:12px 0">'+data('11.60 55.50 7.95 42.15 17.10 2.00 82.55 26.85 5.40 21.90',22)+'</div>',
  [('Add','11.60 + 55.50 + 7.95 + … + 21.90'),('ANS','Σ<i>x</i> = <b>273</b>'),('Count','the number of customers'),('ANS','<i>n</i> = <b>10</b>'),
   fx('Mean','<i>x̄</i>',F(FR([V('Σ<i>x</i>','273')],[V('<i>n</i>','10')])),'27.3'),('ANS','The mean amount spent is <b>$27.30</b>.')],
  '',f'{EDR} · 1G Worked example 1',cmd=('Calculate',None,'one value in dollars')))
S.append(learn('Learn · 1F','Mean or median?',
  '<h4>Choosing between the mean and the median</h4><p style="font-size:21px">The mean and the median are both measures of the centre of a distribution. If the distribution is:</p><ul class="bul" style="font-size:21px"><li>symmetric and there are no outliers, either the mean or the median can be used to indicate the centre of the distribution</li><li>clearly skewed and/or there are outliers, it is more appropriate to use the median to indicate the centre of the distribution.</li></ul>',
  '<div class="row" style="gap:24px"><div class="key frag" style="flex:1"><h4>Symmetric, no outliers</h4>'+hist('mm1',{"start":0,"w":1,"v":[1,2,4,7,9,7,4,2,1],"ymax":10,"ystep":5,"nox":True,"noy":True,"h":170,"W":520,"vline":4.5})+'<p style="font-size:20px">mean ≈ median: <b>either</b> can be used</p></div>'
  '<div class="key frag" style="flex:1"><h4>Clearly skewed and/or outliers</h4>'+hist('mm2',{"start":0,"w":1,"v":[9,8,5,3,2,1,0,0,1],"ymax":10,"ystep":5,"nox":True,"noy":True,"h":170,"W":520,"vline":2.6})+'<p style="font-size:20px">the tail drags the mean: use the <b>median</b></p></div></div>',
  '<b>SOCS:</b> the C line names the measure you chose (‘centred at …, the median’), and the S line uses its partner (IQR with the median).',
  'Key box: Cambridge General Mathematics Units 3&amp;4, 1F p. 52 · Sketches: teacher illustration (dashed line = mean)'))
S.append(TPL._frame('learn','Learn · 1F','Standard deviation: spread around the mean',
  '<div class="row" style="gap:24px;align-items:center">'+kcard('Standard deviation',FSD)+'<p style="flex:1;font-size:22px;line-height:1.4">Roughly, the typical distance of the data values from the mean. On CAS it is <b>s<sub>x</sub></b>. Same mean, different spread:</p></div>'
  '<div class="xp" id="sdx" style="margin-top:12px"></div><span class="frag" data-act="sd-a"></span><span class="frag" data-act="sd-ad"></span><span class="frag" data-act="sd-b"></span><span class="frag" data-act="sd-bd"></span><span class="frag" data-act="sd-s"></span>',
  'Formula: Cambridge General Mathematics Units 3&amp;4, 1F p. 52 · Animation data: teacher example',cfu='disc'))
# ================= CAS (planner/cas-skills.json: one-var-stats)
CS=[x for x in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills'] if x['id']=='one-var-stats'][0]
yid=lambda u:u.split('v=')[1].split('&')[0]
VIDS=[yt(v['title'],yid(v['url'])) for v in CS['videos']['ti'][:1]+CS['videos']['classpad']]
S.append(cas('CAS · 1F','Mean and standard deviation from a list',
  'The following are the heights (in cm) of a group of women.<div style="margin:10px 0">'+data('176 160 163 157 168 172 173 169',22)+'</div>Determine the mean and standard deviation of the women’s heights. Give your answers correct to two decimal places.'
  f'<p class="muted" style="font-size:18px;margin-top:12px"><b>Tip:</b> {CS["tip"]}</p>',
  CS['ti'],CS['classpad'],'<i>x̄</i> = <b>167.25 cm</b> · s<sub>x</sub> = <b>6.67 cm</b>',
  'Cambridge General Mathematics Units 3&amp;4, 1F pp. 53–54 · Steps: CAS guide (planner)',videos=VIDS))
S.append(cas('CAS · 1F','Summary statistics from a frequency table',
  'When values repeat (a dot plot or frequency table), enter each value once and its frequency in a second list. Check with the cricket team from Example 15:'
  '<table class="t" style="font-size:22px;margin:12px 0"><tr><th>age</th><td>18</td><td>19</td><td>22</td><td>23</td><td>24</td><td>25</td><td>29</td></tr><tr><th>freq</th><td>2</td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>1</td></tr></table>'
  '<p class="muted" style="font-size:18px"><b>Check n.</b> If n is not the total frequency, the frequency list was not selected.</p>',
  CS['ti'],CS['classpad'],'<i>n</i> = 13 · <i>x̄</i> = 22 · s<sub>x</sub> = 3.08 · median = 22 ✓',
  'Steps: CAS guide (planner) · ClassPad Help 402 · Data: Cambridge Example 15'))
S.append(qslide('yt','You try · Edrolo 1G WE2','Calculating the mean and standard deviation using the CAS calculator',
  'The <em class="v">weight</em>, in kilograms, of a sample of 10 rugby players are shown. Determine the mean and standard deviation of the rugby players’ <em class="v">weight</em>, rounded to two decimal places.<div style="margin:12px 0">'+data('80 95 85 91 102 93 87 78 84 90')+'</div>',
  [('CAS','One-Variable Statistics on the list <b>weight</b>'),('Mean','<i>x̄</i> = 88.5 → 88.50'),('SD','s<sub>x</sub> = 7.230… → 7.23')],
  'mean = <b>88.50 kg</b>, standard deviation = <b>7.23 kg</b>',f'{EDR} · 1G Worked example 2',cmd=('Determine',None,'two values, 2 d.p.')))
# ================= Exit
DENS=[1.07,1.07,1.08,1.08,1.03,1.05,1.07,1.06,1.07,1.09,1.02,1.09]; WT=[70.1,90.4,73.2,85.0,84.3,95.6,71.7,95.0,80.2,87.4,94.9,65.3]
OT=('<table class="t" id="ex1t" style="font-size:16px;width:100%"><tr><th class="l"><em class="v">body density</em> (kg/litre)</th>'+''.join(f'<td style="padding:2px 6px"><span data-i="{i}">{x:.2f}</span></td>' for i,x in enumerate(DENS))+'</tr>'
    '<tr><th class="l"><em class="v">weight</em> (kg)</th>'+''.join(f'<td style="padding:2px 6px">{x:.1f}</td>' for x in WT)+'</tr></table>')
S.append(qslide('ex','Exit task · VCAA 2020 Exam 2 Q4aii (adapted)','Show what you know',
  G('The <em class="v">body density</em>, in kilograms per litre, and <em class="v">weight</em>, in kilograms, of a sample of 12 orangutans are shown in the table.',OT,
    'For these 12 orangutans, determine the mean of their <em class="v">body density</em>, in kilograms per litre. <span class="muted">(1 mark)</span>'),
  [('Row','only the <em>body density</em> row','data-hi="#ex1t|0,1,2,3,4,5,6,7,8,9,10,11|hy"'),('CAS','One-Variable Statistics on the 12 densities (or add them: Σ<i>x</i> = 12.78)'),
   fx('Mean','<i>x̄</i>',F(FR([V('Σ<i>x</i>','12.78')],[V('<i>n</i>','12')])),'1.065','data-hi="#ex1t||"'),
   ('No rounding','the examiners wanted 1.065: 1.07 was not accepted.')],
  'The mean body density is <b>1.065 kg/litre</b>.',f'{EDR} · 1G Q11 · Adapted from VCAA 2020 Exam 2 Data analysis Q4aii (77% of students answered this type of question correctly)',
  stat=('mc',77),cmd=('determine',1,'one value, not rounded')))
# ================= close
S.append(checkin(SC))
S.append(coursework([('Cambridge · Exercise 1F (part 1)','',['Median from data · Q1–2','Median from a dot plot · Q3','Median and range from a stem plot · Q4','Median and quartiles from a dot plot · Q5',
    'Median and quartiles from a stem plot · Q6–9','Median and quartiles from a histogram · Q10–11']),
  ('Cambridge · Exercise 1F (part 2)','',['Mean, median and mode from data · Q12–17','The concept of standard deviation · Q18–20','Mean and standard deviation on CAS · Q21–22','Exam 1 style questions · Q23–26']),
  ('Practice booklet','The 1F section',[])]))
V=[x for x in json.load(open(os.path.join(ROOT,'planner','videos.json')))['videos'] if x['sub']=='1F']
S.append(videos([yt(f'1F · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V]))
n=assemble(S,'12MAG · S3 · Measures of centre and spread',os.path.join(ROOT,'lessons','S3-slides.html'))
print('slides',n)
