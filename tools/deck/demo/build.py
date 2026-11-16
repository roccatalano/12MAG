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
   ('n = 12: order, find M (line between the middle two)',tsort('qe')+' '+tmed('qe',label='M = 8.5',line=True)),('Split into halves of 6: M stays',b1),('Q₁',b2),('Q₃',b3)])+'</div>',SRC))
# 2b even-n median line + quartile lines inside even halves (n = 8: halves of 4)
e8=[14,9,21,11,17,6,19,12]; c1,c2,c3=tquart('e8',8,'Q₁ = 10','Q₃ = 18',line=True)
S.append(islide('Learn · tiles','Even n: the median sits between two values',
  '<div class="row2"><div>'+tiles('e8',e8)+'</div>'+isteps([('Order (n = 8)',tsort('e8')),('Cross off pairs: M = (12 + 14) ÷ 2 = 13',tmed('e8',label='M = 13',line=True)),
   ('Split into halves of 4',c1),('Q₁ = (9 + 11) ÷ 2 = 10',c2),('Q₃ = (17 + 19) ÷ 2 = 18',c3)])+'</div>',SRC))
# 3 fences slider
hp=[620,680,700,720,750,780,820,800]
S.append(islide('Learn · slider','Outliers and fences <span class="i-hint">DRAG THE SLIDER</span>',
  '<p class="i-sm" style="font-size:20px;color:var(--ink)">Eight house sale prices ($ thousands, demo data). One owner knocks the house down or builds a mansion. When is that price an <b>outlier</b>?</p>'+
  fence_slider('fs',hp,max=3000,min=0,k=7,step=10,lo=100,hi=3000,tick=100,lab=500,xl='sale price ($ thousands)',dec=1,name='Price',lt='Knocked down',rt='Mansion',pre='$',post='k',mm=True)+
  isteps([('A mansion: $2500k',fset('fs',2500)),('Knocked down: $150k',fset('fs',150))]),SRC))
fd=[3,5,6,6,7,8,8,9,10,11,12]
S.append(islide('Learn · slider','Fences on a dot plot <span class="i-hint">DRAG THE SLIDER</span>',
  fence_slider('fs2',fd,max=30,xl='number of ducks (demo data)',tick=1,lab=5,name='Largest')+isteps([('Move the largest value to 25',fset('fs2',25)),('Back to 12',fset('fs2',12))]),SRC))
# 4 box plot slider
bd=[12,14,15,15,16,17,18,18,19,20,21,22,24]
S.append(islide('Learn · slider','Box plot: whisker or outlier? <span class="i-hint">DRAG THE SLIDER</span>',
  box_slider('bs',bd,max=45,k=12,lab=5,xl='walking time (minutes, demo data)',name='Time',lt='Next door',rt='Very far',post=' min')+
  isteps([('Very far: 40 min is beyond UF, so it is an outlier dot; the whisker stops at 22',fset('bs',40)),('Next door: 2 min is below LF',fset('bs',2))]),SRC))
# 5 card sort
items=[('Hair colour','Categorical/Nominal'),('Shoe size','Numerical/Discrete'),('Time to run 100 m','Numerical/Continuous'),('Level of satisfaction (low, medium, high)','Categorical/Ordinal'),
  ('Number of pets','Numerical/Discrete'),('Postcode','Categorical/Nominal'),('Height of a tree','Numerical/Continuous'),('Year level (7–12) as a label','Categorical/Ordinal'),
  ('Mass of a shell','Numerical/Continuous'),('Rating: good, satisfactory, poor','Categorical/Ordinal'),('Colour of a car','Categorical/Nominal'),('Number of computers at home','Numerical/Discrete')]
S.append(islide('Learn · card sort','Sort it: what type of data? <span class="i-hint">STEP 1: CATEGORICAL OR NUMERICAL? STEP 2: WHICH KIND?</span>',card_sort('cs1',items),SRC,frags=sort_steps('cs1')))
S.append(islide('Learn · card sort','Sort it, one card per click',card_sort('cs2',items[:8]),SRC,frags=sort_steps('cs2',per_card=True,n=8)))
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
# 10 new widgets: two tests · plinko · rounder · normal curve brackets
S.append(islide('Learn · slider','Which test went better? <span class="i-hint">DRAG EACH SLIDER</span>',
  ztwo('zt',('Maths',60,10,75),('English',70,5,74))+isteps([('Maths 75 (z = 1.5) vs English 74 (z = 0.8): better in Maths',''),('English 80: z = 2, now English is relatively better',ztset('zt',None,80))]),SRC))
S.append(islide('Learn · plinko','Why a bell shape? <span class="i-hint">DROP SOME BALLS</span>',plinko('pk'),SRC,frags=ifr(pdrop('pk',50),pdrop('pk',150))))
S.append(islide('Learn · rounding','Decimal places vs significant figures <span class="i-hint">CHOOSE A MODE AND A COUNT</span>',
  rounder('rd','0.0047386',mode='dp',n=2)+isteps([('3 decimal places',rset('rd','dp',3)),('2 significant figures: leading zeros do not count',rset('rd','sf',2))]),SRC))
S.append(islide('Learn · rounding','Rounding a big number','<div class="row2">'+rounder('rd2','3456.789',mode='sf',n=2)+isteps([('2 significant figures: 3500 (zeros hold the place)',''),('1 decimal place: 3456.8',rset('rd2','dp',1)),('0 decimal places: 3457',rset('rd2','dp',0))])+'</div>',SRC))
S.append(islide('Learn · normal','68–95–99.7% brackets (always on)',norm('nb',{"m":100,"s":15,"rows":['x','z'],"xl":"IQ score (demo)","W":1300,"h":330,"fs":19,"br":True}),SRC))
S.append(islide('Learn · normal','68–95–99.7% brackets, one per click',norm('nb2',{"m":0,"s":1,"rows":['z'],"W":1300,"h":300,"fs":19,"br":True,"brhide":True}),SRC,frags=ifr(nbr('nb2','1'),nbr('nb2','2'),nbr('nb2','3'))))
S.append(islide('Learn · normal','Small curve: % labels never touch the curve','<div class="row2">'+norm('nb3',{"m":0,"s":1,"rows":[],"W":420,"h":110,"T":14,"fs":12})+norm('nb4',{"m":0,"s":1,"rows":['z'],"W":620,"h":220,"fs":15,"T":64,"br":True})+'</div>',SRC))
# 9 inside a template: qslide with tiles in its working steps
S.append(qslide('we','Worked example · tiles in a qslide','Median inside the question template',
  ('Find the median of these values.',tiles('qw',[8,3,11,5,9,2,7],fs=24),''),
  [('Order','n = 7',tsort('qw')),('Cross off','three pairs; the 4th value is left',tmed('qw',label='M = 7'))],'The median is <b>7</b>.',SRC))
n=assemble(S,'12MAG · interactive features demo',OUT); print(n,'slides ->',OUT)
