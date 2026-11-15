"""Lesson 5 (1H–1I) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S5-slides.html
Run: python3 tools/deck/s5/build.py"""
import os, sys
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,'..','..','..'))
sys.path.insert(0,os.path.join(H,'..','tpl'))
from tpl import *
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
XB='<i>x̄</i>'; X='<i>x</i>'; Z='<i>z</i>'; SD='<i>s</i>'
GT='&gt;'; LT='&lt;'
SH='rgba(79,132,230,.45)'; OR='rgba(217,138,31,.5)'
def zf(x,m,s): return F(FR([V(X,x),' − ',V(XB,m)],[V(SD,s)]))           # z = (x − x̄)/s with values
def xf(m,z,s): return F(V(XB,m),' + ',V(Z,z),' × ',V(SD,s))               # x = x̄ + z × s with values
def shs(rid,regs,clear=True):
    """several shaded regions in one click: regs = [(a,b,label,col)]"""
    sp=' '.join(f'#{rid}|{a},{b}|{col}|{lab}' for a,b,lab,col in regs)
    return (f'data-nclear="#{rid}" ' if clear else '')+f'data-nshade="{sp}"'
def sh(rid,a,b,lab='',col=SH,clear=True): return (f'data-nclear="#{rid}" ' if clear else '')+f'data-nshade="#{rid}|{a},{b}|{col}|{lab}"'
S=[]
# ================= opening
S.append(title(5,'The normal distribution and standardised scores','Cambridge General Mathematics Units 3&amp;4 · 1H The normal distribution and the 68–95–99.7% rule · 1I Populations and samples','S5',
  flow=('CFAT','Do Now','APK','Learn','Worked examples','You try','Exit tasks')))
LI=['To be able to introduce the normal model for bell-shaped distributions.',
    'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.',
    'To be able to calculate standardised scores and use them to compare values across distributions.']
SC=['I can apply the 68-95-99.7% rule.','I can calculate standardised scores.','I can use standardised scores to make comparisons.',
    'I can use standard scores to determine percentages.','I can convert standardised scores into actual scores.','I can solve for the values of the mean and standard deviation.',
    'I can explain the difference between a population and a sample.']
S.append(today(LI,SC,[('CFAT 1.1.2','· 20 minutes','#00838F'),('Do Now','· four current VCAA questions','#00838F'),('APK','· Year 11 normal distribution','var(--apk)'),
  ('The 68–95–99.7% rule','→ WE 28',None),('Standardised scores','→ WE 29, 30 · CAS',None),('From z to percentages','→ WE 31',None),
  ('Actual scores; finding x̄ and s','→ WE 32, 33, 34',None),('Populations and samples','· 1I',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.1.2','median, IQR, boxplots, SOCS','1F–1G',14,'CFAT 1.1.2 (lessons/CFAT-1.1.2) · Edrolo U3&amp;4 exercise questions'))
# ---------- key definitions and formulas
kn=lambda rid,c:norm(rid,dict({"W":420,"h":150,"T":18,"fs":13,"rows":[]},**c))
FZ=F(Z,' = ',FR([X,' − ',XB],[SD])); FX=F(X,' = ',XB,' + ',Z,' × ',SD)
S.append(keys([
  ('Normal distribution','a symmetric, bell-shaped model: mean = median, at the centre',kn('k1',{})),
  ('68–95–99.7% rule','about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean',
     kn('k2',{"sh":[[-3,3,'rgba(79,132,230,.15)'],[-2,2,'rgba(79,132,230,.3)'],[-1,1,'rgba(79,132,230,.5)']]})),
  ('Standardised score (z-score)','how many standard deviations a value is above (+) or below (−) the mean'),
  ('Population · sample','every member of the group being studied · a subset of the population that is measured')],
  [('Within 1 SD',F('(',XB,' − ',SD,', ',XB,' + ',SD,')'),'≈ 68% of values'),
   ('Within 2 SDs',F('(',XB,' − 2',SD,', ',XB,' + 2',SD,')'),'≈ 95% of values'),
   ('Within 3 SDs',F('(',XB,' − 3',SD,', ',XB,' + 3',SD,')'),'≈ 99.7% of values'),
   ('Standardised score',FZ),('Actual score',FX),
   ('Tail percentages','above +1 SD: 16% · above +2 SD: 2.5% · above +3 SD: 0.15%','the same below −1, −2, −3 SD')],
  'Cambridge General Mathematics Units 3&amp;4, 1H pp. 76–83 · Curves: teacher illustrations'))
# ================= Do Now 1: VCAA 2025 E1 Q1
S.append(qslide('dn','Do Now 1 of 4 · VCAA 2025 Exam 1 Q1','Review of 1F',
  ('At a fruit shop, customers can buy avocados in bags.<br>The bag size ranges from one to six avocados per bag.<br>The histogram below shows the number of customers who bought each bag size on a particular day.',
   hist('d1',{"start":0.5,"w":1,"v":[4,11,3,9,5,7],"xmin":0.5,"xmax":6.5,"nox":1,"clab":["1","2","3","4","5","6"],"ymax":12,"ystep":2,"xl":"bag size (number of avocados)","yl":"number of customers","h":330,"W":640,"fs":17,"L":84,"col":"#a9a9a9"}),
   'The median bag size bought by customers on the day was'),
  [('Count','running totals across the columns: 4, 15, 18, 27, 32, 39 → n = 39 customers.','data-cum="#d1"'),
   fx('Median position',None,F(FR([V('<i>n</i>','39'),' + 1'],['2'])),'20th'),
   ('Find','the 20th customer: 18 are in bag sizes 1–3, and 27 in bag sizes 1–4, so the 20th bought a bag of 4.','data-hlbar="#d1|3|#d98a1f"')],
  'The median bag size is <b>4</b> avocados.','VCAA 2025 General Mathematics Exam 1 Q1 (examiner report)',
  stat=('mc',75),mc=['2','3','3.5','4'],key='D',dist=[4,5,17,75],
  dis=('C','3.5 is the middle of the bag sizes 1 to 6, not the middle customer. The median counts the 39 customers.')))
# ================= Do Now 2: VCAA 2024 E1 Q4
S.append(qslide('dn','Do Now 2 of 4 · VCAA 2024 Exam 1 Q4','Review of 1E',
  ('The histogram below displays the population density, in people per km<sup>2</sup>, of the 27 countries in the European Union in 2021. The histogram has a logarithmic (base 10) scale.',
   hist('d2',{"start":1.0,"w":0.2,"v":[0,2,2,2,6,9,3,1,1,0,0,1,0],"xmax":3.6,"tick":0.2,"dec":1,"ymax":10,"ystep":2,"xl":"log10 (population density)","yl":"frequency","h":320,"W":700,"fs":15,"col":"#333"}),
   'There is one outlier at the upper end of the histogram.<br>This value could be'),
  [('Outlier','the column on its own is from 3.2 to 3.4 on the log<sub>10</sub> scale.','data-hlbar="#d2|11|#d98a1f"'),
   ('Convert','log<sub>10</sub>(330) = 2.52 · log<sub>10</sub>(1330) = 3.12 · log<sub>10</sub>(<b>2030</b>) = <b>3.31</b> · log<sub>10</sub>(2730) = 3.44'),
   ('Check','only 3.31 is from 3.2 up to 3.4.')],
  'The outlier could be <b>2030</b> people per km<sup>2</sup>.','VCAA 2024 General Mathematics Exam 1 Q4 (examiner report) · Data: Adapted from &lt;https://ec.europa.eu/eurostat&gt;',
  stat=('mc',68),mc=['330','1330','2030','2730'],key='C',dist=[11,14,68,6],
  dis=('B','log<sub>10</sub>(1330) = 3.12 is in the empty 3.0–3.2 column, not the outlier’s column.')))
# ================= Do Now 3 / 4: VCAA 2025 E2 Q1ci, Q1cii
apt=['350 000','490 000','500 000','620 000','720 000','830 000','875 000','995 000','1 100 000','1 520 000']
hou=['800 000','840 000','920 000','920 000','1 010 000','1 263 000','1 398 000','1 460 000','1 540 000','1 540 000']
def t1(rid):
    tb=lambda rows,o:'<table class="t tight" style="font-size:12px;line-height:1.05"><tr><th>Price ($)</th><th>Type</th></tr>'+''.join(f'<tr><td style="text-align:right"><span data-i="{o+k}" style="padding:0 4px;border-radius:5px;border:1.5px solid transparent">{p}</span></td><td>{t}</td></tr>' for k,(p,t) in enumerate(rows))+'</table>'
    return f'<div class="tbl1" id="{rid}" style="justify-content:center;display:flex;gap:18px">{tb([(p,"apartment") for p in apt],0)}{tb([(p,"house") for p in hou],10)}</div>'
def t2(v,hl=False):
    st=' style="background:#fff3b0;font-weight:700"' if hl else ''
    return ('<div style="margin-top:8px"><b>Table 2</b><table class="t" style="font-size:16px;margin-top:4px"><tr><th>Type of home</th><th>Standard deviation of sale price ($)</th></tr>'
            f'<tr><td>house</td><td>300 911</td></tr><tr><td>apartment</td><td{st}>{v}</td></tr></table></div>')
INTRO='Table 1, below, shows the prices in dollars, <em class="v">price</em>, for a sample of 20 homes sold in an inner Melbourne suburb during 2017.<br>The type of home sold is either an apartment or a house.'
DSRC='Data: Adapted from &lt;www.kaggle.com/datasets/anthonypino/melbourne-housing-market&gt;'
S.append(qslide('dn','Do Now 3 of 4 · VCAA 2025 Exam 2 Q1c.i','Review of 1F',
  (INTRO,t1('d3'),f'<b>c.</b> i. Complete the table below by finding the standard deviation, to the nearest whole number, for the sale price of apartments in the sample. <span class="muted">(1 mark)</span>{t2("&nbsp;")}'),
  [('CAS','enter the 10 apartment prices in a list. Don’t calculate the SD by hand.','data-mark="#d3|0,1,2,3,4,5,6,7,8,9|mid"'),
   ('CAS','One-variable statistics → <i>s<sub>x</sub></i> = 346 466.29'),
   ('Round','to the nearest whole number: 346 466.')],
  'The standard deviation for apartments is <b>$346 466</b>.',f'VCAA 2025 General Mathematics Exam 2 Q1ci (examiner report) · {DSRC}',
  stat=('mark',69),cmd=('Complete',1,'fill in the value, from CAS')))
S.append(qslide('dn','Do Now 4 of 4 · VCAA 2025 Exam 2 Q1c.ii','Review of 1F',
  (INTRO+'<br>Table 2 gives the standard deviation of the sale prices for each type of home (apartment value from part c.i).',t2('346 466'),
   'ii. Using the information in Table 2, comment on the relative spread in the distribution of the sale prices of houses compared with apartments in this sample. <span class="muted">(1 mark)</span>'),
  [('Compare','300 911 (houses) &lt; 346 466 (apartments).'),
   ('Meaning','a smaller standard deviation means the values sit closer to the mean: less spread.'),
   ('Use Table 2','the question says to use Table 2, so use the SD only, not the range or IQR.')],
  'House sale prices have a lower spread than apartment sale prices, as shown by the lower standard deviation.',f'VCAA 2025 General Mathematics Exam 2 Q1cii (examiner report) · {DSRC}',
  stat=('mark',47),cmd=('Comment',1,'a comparison, using the given statistic')))
# ================= APK 1: Cambridge U1&2 2G #13
S.append(qslide('apk','APK · Year 11 · Cambridge U1&amp;2 2G #13','The 68–95–99.7% rule',
  ('Suppose the distribution of weights for a type of cat is approximately symmetric and bell shaped with a mean of 3.5 kg and a standard deviation of 0.5 kg.',
   norm('a1',{"m":3.5,"s":0.5,"rows":['x'],"hide":['x'],"dec":1,"xl":"weight (kg)","W":820,"h":300}),
   'Approximately what percentage of cats weigh between 2 kg and 5 kg?'),
  [('Scale','mean 3.5 kg, one SD = 0.5 kg: 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0.','data-nshow="#a1|x"'),
   ('SDs','2 = 3.5 − 3 × 0.5 and 5 = 3.5 + 3 × 0.5: within three standard deviations.',sh('a1',-3,3,'99.7%'))],
  'Approximately <b>99.7%</b> of cats weigh between 2 kg and 5 kg.','Cambridge General Mathematics Units 1&amp;2 · Chapter 2 skills checklist, 2G #13 (teacher solution)',
  cmd=('Find',None,'a percentage from the rule')))
# ================= APK 2: Edrolo U1&2 1G Q14 (adapted from VCAA 2020 E2 Q2bi)
S.append(qslide('apk','APK · Edrolo U1&amp;2 1G Q14','A real VCAA question you can already do',
  ('A sample of 250 bonobos has been drawn at random from a population of bonobos whose <em class="v">neck size</em> is normally distributed with a mean of 38 cm and a standard deviation of 2.3 cm.',
   norm('a2',{"m":38,"s":2.3,"rows":['x'],"hide":['x'],"dec":1,"xl":"neck size (cm)","W":820,"h":300}),
   'How many of these 250 bonobos are expected to have a <em class="v">neck size</em> that is more than three standard deviations above or below the mean? Round to the nearest whole number. <span class="muted">(1 mark)</span>'),
  [('Within 3 SDs','99.7% of neck sizes are within three standard deviations of the mean.','data-nshow="#a2|x" '+sh('a2',-3,3,'99.7%','rgba(79,132,230,.25)')),
   ('Outside','100% − 99.7% = 0.3%: 0.15% in each tail.',shs('a2',[(-3.6,-3,'',OR),(3,3.6,'',OR)],False)),
   fx('Expected number',None,F(V('%','0.3%'),' × ',V('<i>n</i>','250')),'0.75'),
   ('Round','0.75 rounds to 1. A number of bonobos must be a whole number.')],
  'About <b>1</b> bonobo is expected to have a neck size more than three standard deviations from the mean.',
  'Edrolo General Mathematics Units 1&amp;2 · 1G Q14 · Adapted from VCAA 2020 Exam 2 Data analysis Q2b.i (40%, examiner report)',
  stat=('mark',40),cmd=('Round',1,'a whole number of bonobos')))
# ================= Learn 1: the normal distribution and the rule
S.append(learn('Learn · 1H','The normal distribution and the 68–95–99.7% rule',
  '<h4>Normal distribution</h4><p>A bell-shaped, symmetric model. The mean sits in the middle, and the standard deviation sets the width: approximately 68%, 95% and 99.7% of values lie within one, two and three standard deviations of the mean.</p>',
  norm('l1',{"m":0,"s":1,"rows":['z'],"hide":['z','pct'],"W":1300,"h":330,"fs":19}),
  '<b>Use the symmetry:</b> 68% in the middle leaves 32% for the two tails, so 16% in each tail. 95% leaves 2.5% in each tail; 99.7% leaves 0.15%.',
  'Cambridge General Mathematics Units 3&amp;4, 1H pp. 76–78 · Curve: teacher illustration',
  frags=('<span class="frag" data-nshow="#l1|z"></span>'
         f'<span class="frag" {sh("l1",-1,1,"68%")}></span><span class="frag" {sh("l1",-2,2,"95%")}></span><span class="frag" {sh("l1",-3,3,"99.7%")}></span>'
         f'<span class="frag" data-nclear="#l1" data-nshow="#l1|pct"></span>'),
  cards=[kcard('68–95–99.7% rule','within 1, 2, 3 SDs of the mean: 68%, 95%, 99.7%'),kcard('Tail percentages','16% · 2.5% · 0.15% in each tail')]))
# ================= WE28
S.append(qslide('we','Worked example 28 · 1H','Applying the 68–95–99.7% rule',
  ('The distribution of delivery times for pizzas made by House of Pizza is approximately normal, with a mean of 25 minutes and a standard deviation of 5 minutes.',
   norm('w28',{"m":25,"s":5,"rows":['x'],"hide":['x','pct'],"xl":"Delivery time","W":820,"h":290}),
   plist([('a','What percentage of pizzas have delivery times of between 15 and 35 minutes?'),('b','What percentage of pizzas have delivery times of greater than 30 minutes?'),
          ('c','In 1 month, House of Pizza delivers 2000 pizzas. Approximately many of these pizzas are delivered in less than 10 minutes?')])),
  [('Sketch','scale the curve: mean = 25, SD = 5 → 10, 15, 20, 25, 30, 35, 40.','data-nshow="#w28|x"'),('Percentages','label each section.','data-nshow="#w28|pct"')],'',
  f'{CAM} · Example 28',video='Cambridge GO · Example 28 (1H Resources)',cmd=('Find',None,'a percentage or a number'),
  parts=[('a','15 = 25 − 2 × 5 and 35 = 25 + 2 × 5: within two SDs. <b>95%</b> of pizzas will have delivery times of between 15 and 35 minutes.',sh('w28',-2,2,'95%')),
         ('b','30 = 25 + 1 × 5: more than one SD above the mean. <b>16%</b> of pizzas will have delivery times of greater than 30 minutes.',sh('w28',1,3.6,'16%')),
         ('c','10 = 25 − 3 × 5: 0.15% are below it. '+fx('n','number',F(V('%','0.15%'),' × ',V('<i>n</i>','2000')),'3',ra=sh('w28',-3.6,-3,'0.15%',OR))[1]+' pizzas')]))
# ================= YT Edrolo 1H WE1
HAIR='An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. The <em class="v">length of hair donated</em> was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.'
S.append(qslide('yt','You try · Edrolo 1H WE1','Applying the 68–95–99.7% rule',
  (HAIR,'',
   plist([('a.','What percentage of hair lengths donated were between 16 cm and 32 cm?'),
          ('b.','Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?'),
          ('c.','If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?'),
          ('d.','How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?')])),
  [('Label','8, 12, 16, 20, 24, 28, 32 cm and the section percentages.','data-nshow="#y1|x,pct"')],'',
  f'{EDR} · 1H Worked example 1',cmd=('Find',None,'add the sections'),made=norm('y1',{"m":20,"s":4,"rows":['x'],"hide":['x','pct'],"W":820,"h":250,"fs":17,"T":60}),
  parts=[('a.','34 + 34 + 13.5 + 2.35 = <b>83.85%</b>',sh('y1',-1,3,'83.85%')),
         ('b.','13.5 + 2.35 + 0.15 = <b>16%</b>',sh('y1',1,3.6,'16%')),
         ('c.',fx('n','number',F(V('%','0.16'),' × ',V('<i>n</i>','30')),'4.8')[1]+' → <b>5 girls</b>'),
         ('d.','0.15 + 2.35 + 13.5 + 2.35 + 0.15 = 18.5%; 0.185 × 30 = 5.55 → <b>6 girls</b>',shs('y1',[(-3.6,-1,'',OR),(2,3.6,'',OR)]))]))
# ================= Learn 2: standardised scores
S.append(learn('Learn · 1H','Standardised scores (z-scores)',
  '<h4>Standardised score</h4><p>A z-score counts how many standard deviations a value is from the mean. Subtract the mean, then divide by the standard deviation. Positive: above the mean · zero: at the mean · negative: below the mean.</p>',
  norm('l2',{"m":100,"s":15,"rows":['x','z'],"hide":['z'],"xl":"IQ score (mean 100, SD 15)","W":1300,"h":330,"fs":19}),
  '<b>Check the sign:</b> a value below the mean must give a negative z-score. IQ 115 is one SD above 100, so <i>z</i> = (115 − 100) ÷ 15 = 1.',
  'Cambridge General Mathematics Units 3&amp;4, 1H p. 80 (IQ illustration) · Curve: teacher illustration',
  frags='<span class="frag" data-nshow="#l2|z"></span><span class="frag" data-nmark="#l2|1|115:_z_=_1"></span><span class="frag" data-nmark="#l2|-2|70:_z_=_−2|#1f4fb0"></span>',
  cards=[kcard('Standardised score',FZ)]))
# ================= WE29
S.append(qslide('we','Worked example 29 · 1H','Calculating standard scores',
  ('The heights of a group of young women have a mean of <i>x̄</i> = 160 cm and a standard deviation of <i>s</i> = 8 cm. Determine the standard or z-scores of a woman who is:',
   norm('w29',{"m":160,"s":8,"rows":['x','z'],"hide":['z'],"xl":"height (cm)","W":820,"h":300}),
   plist([('a','172 cm tall'),('b','150 cm tall'),('c','160 cm tall.')])),
  [('Write down',f'{XB} = 160, {SD} = 8, and each value of {X}.')],'',f'{CAM} · Example 29',video='Cambridge GO · Example 29 (1H Resources)',cmd=('Determine',None,'formula, substitute, evaluate'),
  parts=[('a',fx('z',Z,zf('172','160','8'),'1.5',ra='data-nshow="#w29|z" data-nmark="#w29|1.5|172"')[1]),
         ('b',fx('z',Z,zf('150','160','8'),'−1.25',ra='data-nmark="#w29|-1.25|150|#1f4fb0"')[1]),
         ('c',fx('z',Z,zf('160','160','8'),'0',ra='data-nmark="#w29|0|160|#137a59"')[1]+'&nbsp;: at the mean')]))
# ================= CAS
S.append(cas('CAS · 1H','Standardised scores on CAS',
  'Calculate the standardised score of a woman who is 172 cm tall, when the heights have a mean of 160 cm and a standard deviation of 8 cm (Example 29a).<div class="data" style="font-size:24px"><i>z</i> = (172 − 160) ÷ 8</div>Brackets matter: without them the CAS divides 160 by 8 first.',
  ['New document → <b>Calculator</b>.','Type <b>(172−160)/8</b> with the brackets.','Press <b>enter</b>.','Many values: in <b>Lists &amp; Spreadsheet</b>, use a column formula <b>=(a[]−160)/8</b>.'],
  ['Open the <b>Main</b> app.','Type <b>(172−160)÷8</b> with the brackets.','Press <b>EXE</b>.','Many values: in <b>Statistics</b>, put the list in list1 and type <b>(list1−160)÷8</b> into list2’s Cal row.'],
  '<i>z</i> = 1.5','Cambridge General Mathematics Units 3&amp;4, 1H p. 80 (Example 29a)',
  videos=[yt('Calculating and understanding z-scores with TI-nspire','yrR9IALJD6g'),yt('ClassPad Help 007 – Simple calculations in Main','Zb9V3RwXVLA')]))
# ================= YT Edrolo 1I WE1
S.append(qslide('yt','You try · Edrolo 1I WE1','Calculating standardised (z) scores',
  ('The weights of puppies within a litter are approximately normally distributed with a mean of 4 kg and a standard deviation of 0.3 kg.',
   norm('y29',{"m":4,"s":0.3,"rows":['x','z'],"hide":['z'],"dec":1,"xl":"weight (kg)","W":820,"h":300}),'Determine the z-score of a puppy that weighs 4.6 kg.'),
  [('Write down',f'{XB} = 4, {SD} = 0.3, {X} = 4.6'),fx('Standardised score',Z,zf('4.6','4','0.3'),'2',ra='data-nshow="#y29|z" data-nmark="#y29|2|4.6"')],
  'The puppy’s z-score is <b>2</b>.',f'{EDR} · 1I Worked example 1',cmd=('Determine',None,'formula, substitute, evaluate')))
# ================= WE30
PS='<table class="t" style="font-size:18px"><tr><th>Subject</th><th>Mark</th><th>Mean</th><th>Standard deviation</th></tr><tr><td>Psychology</td><td>75</td><td>65</td><td>10</td></tr><tr><td>Statistics</td><td>70</td><td>60</td><td>5</td></tr></table>'
S.append(qslide('we','Worked example 30 · 1H','Using standardised scores to make comparisons',
  ('A student’s marks in Psychology and Statistics, with the mean and standard deviation for each subject:',PS,
   'Another student studying the same two subjects obtained a mark of 55 for both Psychology and Statistics. Does this mean that she performed equally well in both subjects? Use standardised marks to help you arrive at your conclusion.'),
  [fx('Psychology',Z,zf('55','65','10'),'−1'),fx('Statistics',Z,zf('55','60','5'),'−1'),
   ('Locate','<i>z</i> = −1 in both: 16% of students are below it.',sh('w30',-3.6,-1,'16%')+' data-nmark="#w30|-1|z_=_−1"')],
  'Yes, her standardised score, <i>z</i> = −1, was the same for both subjects. In both subjects she finished in the bottom 16%.',
  f'{CAM} · Example 30 (table from p. 81)',video='Cambridge GO · Example 30 (1H Resources)',cmd=('Use',None,'z-scores, then a conclusion'),
  made=norm('w30',{"rows":['z'],"W":620,"h":220,"fs":15,"T":64})))
# ================= YT Edrolo 1I WE3
S.append(qslide('yt','You try · Edrolo 1I WE3','Using standardised (z) scores to interpret data',
  ('The results for a Chemistry exam were approximately normally distributed, with a mean of 71 and a standard deviation of 3. The results for a Physics exam were also approximately normally distributed, with a mean of 95 and a standard deviation of 6.',
   norm('y30',{"rows":['z'],"hide":['pct'],"W":780,"h":230,"fs":16,"T":44}),
   plist([('a.','A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.'),
          ('b.','Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.')])),
  [],'',f'{EDR} · 1I Worked example 3',cmd=('Use',None,'z-scores and the rule'),
  parts=[('a.','Chemistry: '+fx('z',Z,zf('77','71','3'),'2',ra=sh('y30',2,3.6,'2.5%')+' data-nmark="#y30|2|Chem"')[1]+' · Physics: '+fx('z',Z,zf('77','95','6'),'−3',ra=sh('y30',-3.6,-3,'0.15%',OR,False)+' data-nmark="#y30|-3|Phys|#1f4fb0"')[1]
          +'<br>In Chemistry, the student’s standardised score was <i>z</i> = 2 placing her in the top 2.5% of students. In Physics, the student’s standardised score was <i>z</i> = −3 placing her in the bottom 0.15% of students. Therefore, she did not do equally well in both exams when compared to her peers.'),
         ('b.',fx('z',Z,zf('66','71','3'),'−1.67',ra=sh('y30',-3.6,-1,'16%')+' data-nmark="#y30|-1.67|66"')[1]+'<br>In Chemistry, the student’s standardised score was <i>z</i> = −1.67 placing him in the bottom 16% of students.')]))
# ================= Learn 3: z-scores to percentages
S.append(learn('Learn · 1H','Using standardised scores to find percentages',
  '<h4>z-scores and percentages</h4><p>On a z-score scale every normal distribution looks the same: the mean is at <i>z</i> = 0 and each section between whole z-scores holds a fixed percentage. Convert the values to z-scores, then add up the sections.</p>',
  norm('l3',{"rows":['z'],"hide":['pct'],"W":1300,"h":330,"fs":19}),
  '<b>Above or below?</b> Read the question twice. Below <i>z</i> = −1 is 16%, so above <i>z</i> = −1 is 100% − 16% = 84%.',
  'Cambridge General Mathematics Units 3&amp;4, 1H p. 82 · Curve: teacher illustration',
  frags=f'<span class="frag" data-nshow="#l3|pct"></span><span class="frag" {sh("l3",-1,3.6,"84%")} data-nmark="#l3|-1|z_=_−1"></span><span class="frag" {sh("l3",-1,2,"81.5%")}></span>',
  cards=[kcard('Standardised score',FZ),kcard('Tail percentages','16% · 2.5% · 0.15% in each tail')]))
# ================= WE31
S.append(qslide('we','Worked example 31 · 1H','Using standard scores to determine percentages',
  ('Suppose the weight of a certain species of bird is normally distributed with a mean of 42 grams with a standard deviation of 3 grams.',
   norm('w31',{"m":42,"s":3,"rows":['x','z'],"hide":['pct'],"xl":"weight (grams)","W":820,"h":320}),
   plist([('a','If a bird selected at random from this population has a standardised weight of <i>z</i> = −1, what percentage of birds in this population weigh more than this bird?'),
          ('b','Approximately what percentage of birds would weigh between 39 and 48 grams?')])),
  [('Percentages','label each section of the curve.','data-nshow="#w31|pct"')],'',f'{CAM} · Example 31',video='Cambridge GO · Example 31 (1H Resources)',cmd=('Find',None,'a percentage'),
  parts=[('a','16% of the distribution is below <i>z</i> = −1, so the percentage above <i>z</i> = −1 is <b>84%</b>.',sh('w31',-1,3.6,'84%')+' data-nmark="#w31|-1|z_=_−1"'),
         ('b',fx('z',Z,zf('39','42','3'),'−1')[1]+' · '+fx('z',Z,zf('48','42','3'),'2')[1]+'<br>The percentage between <i>z</i> = −1 and <i>z</i> = 2 is 34 + 34 + 13.5 = <b>81.5%</b>.',sh('w31',-1,2,'81.5%'))]))
# ================= YT Edrolo 1H WE2
S.append(qslide('yt','You try · Edrolo 1H WE2','Calculating values in normal distributions',
  (HAIR,norm('y31',{"m":20,"s":4,"rows":['x','z'],"hide":['pct'],"W":820,"h":300}),
   plist([('a.','97.35% of the hair lengths will fall within 12 cm and which other value?'),
          ('b.','2.5% of hair donated by the team will be disposed of, as it falls below a required minimum length. What is this required minimum length?')])),
  [('Percentages','label each section of the curve.','data-nshow="#y31|pct"')],'',f'{EDR} · 1H Worked example 2',cmd=('Find',None,'a boundary value'),
  parts=[('a.','12 cm is two SDs below the mean. Add sections from 12 cm: 13.5 + 34 + 34 + 13.5 + 2.35 = 97.35%, which ends three SDs above the mean: <b>32 cm</b>.',sh('y31',-2,3,'97.35%')),
         ('b.','0.15 + 2.35 = 2.5%, so 2.5% of hair lengths are below 12 cm: <b>12 cm</b>.',sh('y31',-3.6,-2,'2.5%',OR))]))
# ================= Learn 4: actual scores, working backwards
S.append(learn('Learn · 1H','Converting standardised scores into actual scores',
  f'<h4>Actual score</h4><p>Make {X} the subject of the z-score rule: start at the mean and step {Z} standard deviations. A percentage in a tail tells you {Z}, so with one known value you can solve for the mean or the standard deviation.</p>',
  norm('l4',{"m":50,"s":10,"rows":['x','z'],"W":1300,"h":330,"fs":19}),
  '<b>Tail → z:</b> 16% above → <i>z</i> = 1 · 2.5% above → <i>z</i> = 2 · 0.15% above → <i>z</i> = 3 (negative for tails below the mean).',
  'Cambridge General Mathematics Units 3&amp;4, 1H pp. 83–84 · Curve: teacher illustration',
  frags=f'<span class="frag" data-nmark="#l4|1.5|z_=_1.5_→_x_=_50_+_1.5_×_10_=_65"></span><span class="frag" data-nclear="#l4" {sh("l4",2,3.6,"2.5%",OR,False)} data-nmark="#l4|2|z_=_2"></span>',
  cards=[kcard('Actual score',FX)]))
# ================= WE32
S.append(qslide('we','Worked example 32 · 1H','Converting standard scores into actual scores',
  ('A class test (out of 50) has a mean mark of <i>x̄</i> = 34 and a standard deviation of <i>s</i> = 4. Joe’s standardised test mark was <i>z</i> = −1.5.',
   norm('w32',{"m":34,"s":4,"rows":['x','z'],"xl":"test mark","W":820,"h":300}),'What was Joe’s actual mark?'),
  [('Write down',f'{XB} = 34, {SD} = 4, {Z} = −1.5'),fx('Actual score',X,xf('34','(−1.5)','4'),'28',ra='data-nmark="#w32|-1.5|28"')],
  'Joe’s actual mark was <b>28</b>.',f'{CAM} · Example 32',video='Cambridge GO · Example 32 (1H Resources)',cmd=('Find',None,'formula, substitute, evaluate')))
# ================= YT Edrolo 1I WE2
S.append(qslide('yt','You try · Edrolo 1I WE2','Calculating actual scores from standardised (z) scores',
  ('The number of black stripes on tigers at the Royal Melbourne Zoo is known to be normally distributed with a mean of 55 and a standard deviation of 2. One of the tigers has a standardised number of stripes of <i>z</i> = −2.5.',
   norm('y32',{"m":55,"s":2,"rows":['x','z'],"xl":"number of stripes","W":820,"h":300}),'How many stripes does the tiger actually have?'),
  [('Write down',f'{XB} = 55, {SD} = 2, {Z} = −2.5'),fx('Actual score',X,xf('55','(−2.5)','2'),'50',ra='data-nmark="#y32|-2.5|50"')],
  'The tiger has <b>50</b> stripes.',f'{EDR} · 1I Worked example 2',cmd=('Find',None,'formula, substitute, evaluate')))
# ================= WE33
S.append(qslide('we','Worked example 33 · 1H','Finding the standard deviation given the mean and one percentage',
  ('Suppose the heights of red flowering gum trees have a mean of 10.2 metres, and 2.5% of these trees grow to more than 11.4 metres tall. Assuming that the heights of these trees are approximately normally distributed, what is the standard deviation of the height of the red flowering gum trees?',
   norm('w33',{"rows":['z'],"W":820,"h":280}),''),
  [('Tail → z','2.5% are taller than 11.4 m, so 11.4 m is at <i>z</i> = 2.',sh('w33',2,3.6,'2.5%',OR)+' data-nmark="#w33|2|11.4_m"'),
   ('Actual score',f'<span class="fx">{X} = {XB} + {Z} × {SD} → 11.4 = 10.2 + 2 × {SD}</span>'),
   ('Solve',f'2 × {SD} = 11.4 − 10.2 = 1.2, so {SD} = 0.6')],
  'The standard deviation of the heights is <b>0.6 metres</b>.',f'{CAM} · Example 33 (no matching Edrolo worked example, so no You try)',video='Cambridge GO · Example 33 (1H Resources)',
  cmd=('Find',None,'the standard deviation')))
# ================= WE34
S.append(qslide('we','Worked example 34 · 1H','Finding the mean and standard deviation given two percentages',
  ('The marks scored in an examination are known to be approximately normally distributed. If 16% of students score more than 80 marks, and 2.5% of students score less than 20 marks, estimate the mean and standard deviation of this distribution.',
   norm('w34',{"rows":['z'],"W":820,"h":280}),''),
  [('Tail → z','2.5% score less than 20, so 20 is at <i>z</i> = −2: '+f'{XB} − 2 × {SD} = 20 (1)',sh('w34',-3.6,-2,'2.5%',OR)+' data-nmark="#w34|-2|20"'),
   ('Tail → z','16% score more than 80, so 80 is at <i>z</i> = 1: '+f'{XB} + 1 × {SD} = 80 (2)',sh('w34',1,3.6,'16%',SH,False)+' data-nmark="#w34|1|80"'),
   ('Subtract',f'(2) − (1): 3 × {SD} = 60, so {SD} = 20'),
   ('Substitute',f'{XB} − 2 × 20 = 20, so {XB} = 60')],
  f'The mean is {XB} = <b>60</b> marks and the standard deviation is {SD} = <b>20</b> marks.',f'{CAM} · Example 34 (the book writes (1) − (2); (2) − (1) is the subtraction that gives 3s = 60)',
  video='Cambridge GO · Example 34 (1H Resources)',cmd=('Estimate',None,'two equations, then solve')))
# ================= YT Edrolo 1H WE3
S.append(qslide('yt','You try · Edrolo 1H WE3','Determining the mean and standard deviation of a normal distribution',
  ('Duncan’s light bulb factory produces light bulbs.<br>The <em class="v">lifetime</em> of their light bulbs are approximately normally distributed. It is known that approximately 95% of the light bulbs have a <em class="v">lifetime</em> ranging from 800 hours to 1600 hours.',
   norm('y34',{"rows":['z'],"W":820,"h":280,"sh":[[-2,2,'rgba(79,132,230,.3)','95%']]}),
   plist([('a.','Calculate the standard deviation for the <em class="v">lifetime</em> of a light bulb.'),('b.','Calculate the mean <em class="v">lifetime</em> of a light bulb.')])),
  [('SDs','95% lies within two SDs either side of the mean: 800 h is at <i>z</i> = −2 and 1600 h at <i>z</i> = 2, a total of four SDs.','data-nmark="#y34|-2|800 #y34|2|1600"')],'',
  f'{EDR} · 1H Worked example 3',cmd=('Calculate',None,'working, then the value'),
  parts=[('a.','four SDs = 1600 − 800 = 800, so one SD = 800 ÷ 4 = <b>200 hours</b>'),
         ('b.','two SDs above the lower boundary: 800 + 2 × 200 = <b>1200 hours</b>','data-nmark="#y34|0|1200"')]))
# ================= Learn 5: 1I populations and samples
SMP=(3,8,17,22,29,36,41,48,52,57)
dots=''.join(f'<circle cx="{40+(k%15)*56}" cy="{36+(k//15)*52}" r="15" fill="#c9d6f2"/>' for k in range(60))
dots+='<g class="frag">'+''.join(f'<circle cx="{40+(k%15)*56}" cy="{36+(k//15)*52}" r="17" fill="#d98a1f" stroke="#9a5a00" stroke-width="2"/>' for k in SMP)+'</g>'
POP=(f'<svg viewBox="0 0 880 260" width="100%" style="max-width:1000px;display:block;margin:0 auto">'
     f'<rect x="4" y="4" width="872" height="230" rx="18" fill="none" stroke="#1f4fb0" stroke-width="3"/>{dots}'
     '<text x="440" y="256" text-anchor="middle" font-size="20" font-weight="700" fill="#1f4fb0">population: every member · orange: a random sample of 10</text></svg>')
S.append(learn('Learn · 1I','Populations and samples',
  '<h4>Population and sample</h4><p>The <b>population</b> is every member of the group we want to know about. Measuring them all is usually too slow or costly, so we measure a <b>sample</b>: a subset of the population. The sample’s mean and standard deviation are used to estimate the population’s.</p>',
  f'<div id="pp">{POP}</div>',
  '<b>Choose the sample at random</b> so every member has the same chance of being picked; then the sample statistics give fair estimates of the population values.',
  'Cambridge General Mathematics Units 3&amp;4, 1I Populations and samples (Interactive Textbook only; summarised in own words) · Picture: teacher illustration',
  cards=[kcard('Population','every member of the group being studied'),kcard('Sample','a subset of the population')]))
# ================= Exit 1: Edrolo 1H Q12 (VCAA 2019 E2 Q2b)
S.append(qslide('ex','Exit task 1 of 2 · Edrolo 1H Q12 · VCAA 2019 Exam 2 Q2b','Show what you know',
  ('The <em class="v">temperature difference</em> between the <em class="v">minimum daily temperature</em> and the <em class="v">maximum daily temperature</em> in November 2017 at a location is approximately normally distributed with a mean of 9.4 °C and a standard deviation of 3.2 °C.',
   norm('e1',{"m":9.4,"s":3.2,"rows":['x'],"hide":['x'],"dec":1,"xl":"temperature difference (°C)","W":820,"h":300}),
   'Determine the number of days in November 2017 for which this <em class="v">temperature difference</em> is expected to be greater than 9.4 °C. <span class="muted">(1 mark)</span>'),
  [('Locate','9.4 °C is the mean (<i>z</i> = 0).','data-nshow="#e1|x" data-nmark="#e1|0|9.4"'),
   ('Percentage','a normal distribution is symmetric: 50% of days are above the mean.',sh('e1',0,3.6,'50%')),
   fx('Number of days',None,F(V('%','50%'),' × ',V('days','30')),'15'),
   ('Watch out','the question asks for a number of days, not a percentage.')],
  'The temperature difference is expected to be greater than 9.4 °C on <b>15 days</b>.',f'{EDR} · 1H Q12 · VCAA 2019 Exam 2 Data analysis Q2b (examiner report: “Some gave the percentage of 50% rather than the number of days.”)',
  stat=('mark',58),cmd=('Determine',1,'a number of days')))
# ================= Exit 2: Edrolo 1I Q13 (VCAA 2021 E2 Q1c)
SP='<table class="t" style="font-size:18px"><tr><th>statistic</th><th><em class="v">shot-put</em> (metres)</th></tr><tr><td>mean</td><td>13.74</td></tr><tr><td>standard deviation</td><td>1.43</td></tr></table>'
S.append(qslide('ex','Exit task 2 of 2 · Edrolo 1I Q13 · VCAA 2021 Exam 2 Q1c','Show what you know',
  ('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.',
   SP,'Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place. <span class="muted">(1 mark)</span>'),
  [('Write down',f'{X} = 14.50, {XB} = 13.74, {SD} = 1.43'),fx('Standardised score',Z,zf('14.50','13.74','1.43'),'0.531…'),('Round','to one decimal place: 0.5.')],
  'Jamilia’s standardised score is <b><i>z</i> = 0.5</b>.',f'{EDR} · 1I Q13 · VCAA 2021 Exam 2 Data analysis Q1c (examiner report)',stat=('mark',78),cmd=('Calculate',1,'working, then round')))
# ================= close
S.append(checkin(SC))
S.append(coursework([('1H The normal distribution and the 68–95–99.7% rule','Cambridge Exercise 1H: Questions 1–23',
  ['Q1–5 the 68–95–99.7% rule · Q6–7 standardised scores · Q8 comparisons · Q9–10 percentages from z-scores · Q11 actual scores · Q12–15 finding the mean and SD · Q16–18 applications · Q19–23 Exam 1 style',
   'Revision book: the 1H section']),
  ('1I Populations and samples','Cambridge Exercise 1I (Interactive Textbook)',['1I is online only: open it in Cambridge GO'])]))
S.append(videos())
n=assemble(S,'12MAG · S5 · The normal distribution and standardised scores',f'{ROOT}/lessons/S5-slides.html')
print('slides',n)
