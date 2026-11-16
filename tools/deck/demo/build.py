"""Demo of the interactive slide features (tpl.py 'Interactive features' helpers; JS tpl/ia.js, CSS tpl/ia.css).
NOT lesson material: every data set here is demo data. Output: /tmp/demo.html (or argv[1]).
Run: python3 tools/deck/demo/build.py [/tmp/demo.html]"""
import os, sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
OUT=sys.argv[1] if len(sys.argv)>1 else '/tmp/demo.html'
SRC='Demo data (feature test, not lesson material)'
S=[title('D','Interactive slide features','Demo deck · tpl.py interactive helpers','DEMO')]

# 1 median: odd and even (decimals)
odd=[23,17,31,21,12,40,19,28,21,15,26]; even=[6.5,9,4.2,7,12.1,3,9.8,6,11,5]
S.append(islide('Learn · tiles','Median: order, cross off, middle',
  '<div class="row2"><div>'+tiles('mo',odd)+tiles('me',even)+'</div>'+isteps([
   ('Order the data (n = 11)',tsort('mo')),('Cross off smallest + largest, again and again',tmed('mo',label='M = 21')),
   ('Even n = 10: order the data',tsort('me')),('Two values are left: M = (6.5 + 7) ÷ 2 = 6.75',tmed('me',label='M = 6.75'))])+'</div>',SRC))
# 2 quartiles: odd n=9, even n=12
qo=[7,2,9,4,5,1,8,3,6]; qe=[12,4,7,9,3,15,6,10,5,8,11,14]
a1,a2,a3=tquart('qo',9,'Q₁ = 2.5','Q₃ = 7.5'); b1,b2,b3=tquart('qe',12,'Q₁ = 5.5','Q₃ = 11.5')
S.append(islide('Learn · tiles','Quartiles are medians of the halves',
  '<div class="row2"><div>'+tiles('qo',qo,fs=24)+tiles('qe',qe,fs=24)+'</div>'+isteps([
   ('Order, find M (n = 9)',tsort('qo')+' '+tmed('qo',label='M = 5')),('Split: leave the median out',a1),('Q₁ = median of lower half',a2),('Q₃ = median of upper half',a3),
   ('n = 12: order, find M',tsort('qe')+' '+tmed('qe',label='M = 8.5')),('Split into halves of 6',b1),('Q₁',b2),('Q₃',b3)])+'</div>',SRC))
# 3 fences slider
fd=[3,5,6,6,7,8,8,9,10,11,12]
S.append(islide('Learn · slider','Outliers and fences <span class="i-hint">DRAG THE ORANGE DOT</span>',
  fence_slider('fs',fd,max=30,xl='number of ducks (demo data)',tick=1,lab=5)+isteps([('Move the largest value to 25',fset('fs',25)),('Back to 12',fset('fs',12)),('Now 22: an outlier again',fset('fs',22))]),SRC))
# 4 box plot slider
bd=[4,6,7,7,8,9,10,10,11,12,13,14,16]
S.append(islide('Learn · slider','Box plot: whisker or outlier? <span class="i-hint">DRAG THE HANDLE</span>',
  box_slider('bs',bd,max=40,lab=5,xl='walking time (minutes, demo data)')+isteps([('Max = 30: beyond UF, so an outlier dot; the whisker stops at 14',fset('bs',30))]),SRC))
# 5 card sort
items=[('Hair colour','Categorical/Nominal'),('Shoe size','Numerical/Discrete'),('Time to run 100 m','Numerical/Continuous'),('Level of satisfaction (low, medium, high)','Categorical/Ordinal'),
  ('Number of pets','Numerical/Discrete'),('Postcode','Categorical/Nominal'),('Height of a tree','Numerical/Continuous'),('Year level (7–12) as a label','Categorical/Ordinal')]
S.append(islide('Learn · card sort','Sort it: what type of data? <span class="i-hint">CLICK A CARD, THEN A BUCKET (OR DRAG)</span>',card_sort('cs1',items),SRC,frags=sort_steps('cs1')))
# 6 stem plot leaf by leaf
sv=[34,27,45,31,38,52,29,41,36,33,47,25]
S.append(islide('Learn · stem plot','Stem plot, leaf by leaf',
  '<div class="row2">'+stem_fly('sp',sv,key='Key: 3 | 4 = 34')+isteps([('First four values',leaf('sp','0-3')),('The rest',leaf('sp','4-11')),('Order each row',lsort('sp'))])+'</div>',SRC))
# 6b decimals, split stems
S.append(islide('Learn · stem plot','Split stems, decimals',
  '<div class="row2">'+stem_fly('sp2',[4.7,5.2,4.1,5.8,4.9,5.5,4.3],unit=0.1,split=True,key='Key: 4 | 7 = 4.7')+isteps([('All leaves',leaf('sp2')),('Order',lsort('sp2'))])+'</div>',SRC))
# 7 tally → table → histogram
tv=[12,25,7,18,33,21,15,9,27,22,14,31,19,24,16,11]
ch,tb=tally_set('tc','tt',tv,[0,10,20,30,40])
hc=hist('th',{"start":0,"w":10,"v":[2,7,5,2],"ymax":7,"ystep":1,"xl":"score (demo)","yl":"frequency","h":330,"W":560,"fs":17},'data-stepped="1"')
S.append(islide('Learn · display','Data → frequency table → histogram',
  ch+'<div class="row2" style="grid-template-columns:.8fr 1.2fr 1fr"><div>'+tb+'</div><div>'+hc+'</div>'+isteps([(f'Class {k}',ftally('tc','tt',k,'th')) for k in range(4)]+[('Total = 16',ftot('tt'))])+'</div>',SRC))
# 8 normal z slider · log slider · shape slider
S.append(islide('Learn · slider','z-scores and the 68–95–99.7% rule <span class="i-hint">DRAG</span>',z_slider('zs',60,5,x0=65,xl='score (demo)')+isteps([('x = 70',fset('zs',70)),('x = 52.5',fset('zs',52.5))]),SRC))
S.append(islide('Learn · slider','Log scale <span class="i-hint">DRAG</span>',log_slider('ls',0,6,x0=1000,xl='price ($)')+isteps([('x = 250 000',fset('ls',250000))]),SRC))
S.append(islide('Learn · slider','Shape: mean vs median <span class="i-hint">DRAG</span>',shape_slider('sh')+isteps([('Positive skew',shset('sh',0.8)),('Negative skew',shset('sh',-0.7))]),SRC))
# 9 inside a template: qslide with tiles in its working steps
S.append(qslide('we','Worked example · tiles in a qslide','Median inside the question template',
  ('Find the median of these values.',tiles('qw',[8,3,11,5,9,2,7],fs=24),''),
  [('Order','n = 7',tsort('qw')),('Cross off','three pairs; the 4th value is left',tmed('qw',label='M = 7'))],'The median is <b>7</b>.',SRC))
n=assemble(S,'12MAG · interactive features demo',OUT); print(n,'slides ->',OUT)
