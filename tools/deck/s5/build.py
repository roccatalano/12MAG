"""Lesson 5 (1H–1I) slides, built from the slide templates (tools/deck/tpl/tpl.py). Output: lessons/S5-slides.html
Run: python3 tools/deck/s5/build.py
Planner card: gm12-u3-s5 (coursework + CAS steps read from planner/unit-plan.json and planner/cas-skills.json; videos from planner/videos.json).
1I populations and samples: no Example or worked example exists in Cambridge U3&4 (1I is Interactive Textbook only) or Edrolo U3&4
(checked 16 Nov), so 1I is a Learn slide only (own words) — no question written."""
import os, sys, json
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
import tpl as TPL
def G(pre,fig,post=''):
    # question text, figure, question line: stacked with normal spacing (no stretched gap), as in S1
    return f'<div>{pre}</div>'+(f'<div style="margin:14px 0;display:flex;justify-content:center">{fig}</div>' if fig else '')+(f'<div>{post}</div>' if post else '')
def qslide(*a,**k):
    a=list(a)
    if isinstance(a[3],tuple) and 'data-chart="norm"' not in a[3][1] and 'data-chart="hist"' not in a[3][1]: a[3]=G(*a[3])  # curves/histograms keep the figure zone
    return TPL.qslide(*a,**k)
S=[]
# ================= opening
S.append(title(5,'The normal distribution and standardised scores','Cambridge General Mathematics Units 3&amp;4 · 1H The normal distribution and the 68–95–99.7% rule · 1I Populations and samples','S5',
  flow=('CFAT','APK','Learn','Worked examples','You try','Exit tasks')))
LI=['To be able to introduce the normal model for bell-shaped distributions.',
    'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.',
    'To be able to calculate standardised scores and use them to compare values across distributions.']
SC=['I can apply the 68-95-99.7% rule.','I can calculate standardised scores.','I can use standardised scores to make comparisons.',
    'I can use standard scores to determine percentages.','I can convert standardised scores into actual scores.','I can solve for the values of the mean and standard deviation.',
    'I can explain the difference between a population and a sample.']
S.append(today(LI,SC,[('CFAT 1.1.2','· 20 minutes','#00838F'),('APK','· Year 11 normal distribution','var(--apk)'),
  ('The 68–95–99.7% rule','· Galton board → WE 28',None),('Standardised scores','· two tests → WE 29, 30 · CAS',None),('From z to percentages','→ WE 31',None),
  ('Actual scores; finding x̄ and s','→ WE 32, 33, 34',None),('Populations and samples','· 1I',None),('Exit tasks','· two VCAA questions','var(--exit)'),('Check-in and coursework','','var(--muted)')]))
S.append(cfat('CFAT 1.1.2','median, IQR, boxplots, SOCS','1F–1G',14,'CFAT 1.1.2 (lessons/CFAT-1.1.2) · Edrolo U3&amp;4 exercise questions'))
# ---------- key definitions and formulas
kn=lambda rid,c:norm(rid,dict({"W":420,"h":110,"T":14,"fs":12,"rows":[]},**c))
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
S.append(qslide('apk','APK · VCAA 2020 Exam 2 Q2b.i (adapted)','A real VCAA question you can already do',
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
  norm('l1',{"m":0,"s":1,"rows":['z'],"hide":['z','pct'],"W":1300,"h":330,"fs":19,"br":True}),
  '<b>Use the symmetry:</b> 68% in the middle leaves 32% for the two tails, so 16% in each tail. 95% leaves 2.5% in each tail; 99.7% leaves 0.15%.',
  'Cambridge General Mathematics Units 3&amp;4, 1H pp. 76–78 · Curve: teacher illustration',
  frags=('<span class="frag" data-nshow="#l1|z"></span>'
         f'<span class="frag" {sh("l1",-1,1,"68%")}></span><span class="frag" {sh("l1",-2,2,"95%")}></span><span class="frag" {sh("l1",-3,3,"99.7%")}></span>'
         f'<span class="frag" data-nclear="#l1" data-nshow="#l1|pct"></span>'),
  cards=[kcard('68–95–99.7% rule','within 1, 2, 3 SDs of the mean: 68%, 95%, 99.7%'),kcard('Tail percentages','16% · 2.5% · 0.15% in each tail')]))
# ================= Learn: plinko (Galton board): why a bell shape (own words)
S.append(islide('Learn · 1H · interactive','Why is the normal distribution bell shaped? <span class="i-hint">DROP THE BALLS</span>',
  plinko('pk',note='Each ball bounces left or right at every peg. Most end up near the middle (the average); fewer and fewer land further out. Many real data sets (heights, test marks, delivery times) build up the same way: most values are near the mean, extreme values are rare.'),
  'Cambridge General Mathematics Units 3&amp;4, 1H p. 76 (the normal distribution; explained in own words) · Galton board: teacher illustration',
  frags=ifr(pdrop('pk',50))+ifr(pdrop('pk',150))))
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
  '<style>.T .y13 ol.parts{gap:6px;justify-content:flex-start} .T .y13 ol.parts li{font-size:18px!important;line-height:1.25!important}</style><div class="y13" style="font-size:.9em">'+HAIR+
   plist([('a.','What percentage of hair lengths donated were between 16 cm and 32 cm?'),
          ('b.','Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?'),
          ('c.','If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?'),
          ('d.','How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?')])+'</div>',
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
# ================= Interactive: two tests (Cambridge Example 30 data)
S.append(islide('Learn · 1H · interactive','Which test went relatively better? Compare z-scores <span class="i-hint">SLIDE EACH SCORE</span>',
  ztwo('zt',('Psychology',65,10,75),('Statistics',60,5,70))+isteps([
   ('Psychology 75 → <i>z</i> = 1 · Statistics 70 → <i>z</i> = 2: relatively better in Statistics',ztset('zt',75,70)),
   ('Both 55 → <i>z</i> = −1 in each: equally well (Example 30)',ztset('zt',55,55))]),
  'Values: Cambridge General Mathematics Units 3&amp;4, 1H Example 30 (Psychology mean 65, SD 10, mark 75; Statistics mean 60, SD 5, mark 70)'))
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
CS=[x for x in json.load(open(os.path.join(ROOT,'planner','cas-skills.json')))['skills'] if x['id']=='z-score'][0]
yid=lambda u:u.split('v=')[1].split('&')[0]
S.append(cas('CAS · 1H','Standardised scores on CAS',
  'Calculate the standardised score of a woman who is 172 cm tall, when the heights have a mean of 160 cm and a standard deviation of 8 cm (Example 29a).<div class="data" style="font-size:24px"><i>z</i> = (172 − 160) ÷ 8</div>'+CS['tip'],
  CS['ti'],CS['classpad'],'<i>z</i> = 1.5','Cambridge General Mathematics Units 3&amp;4, 1H p. 80 (Example 29a) · Steps: CAS guide (planner)',
  videos=[yt(v['title'],yid(v['url'])) for v in CS['videos']['ti']+CS['videos']['classpad']]))
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
   '',
   plist([('a.','A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.'),
          ('b.','Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.')])),
  [],'',f'{EDR} · 1I Worked example 3',cmd=('Use',None,'z-scores and the rule'),made=norm('y30',{"rows":['z'],"hide":['pct'],"W":780,"h":200,"fs":15,"T":60}),
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
  [('Percentages','label each section of the curve.','data-nshow="#w31|pct"'),
   fx('Standardised score','<i>z</i>₁',zf('39','42','3'),'−1',ra='data-nmark="#w31|-1|z₁_=_−1"'),
   fx('Standardised score','<i>z</i>₂',zf('48','42','3'),'2',ra='data-nmark="#w31|2|z₂_=_2|#1f4fb0"')],'',f'{CAM} · Example 31',video='Cambridge GO · Example 31 (1H Resources)',cmd=('Find',None,'a percentage'),
  parts=[('a','16% of the distribution is below <i>z</i> = −1, so the percentage above <i>z</i> = −1 is <b>84%</b>.',sh('w31',-1,3.6,'84%')+' data-nmark="#w31|-1|z_=_−1"'),
         ('b','<i>z</i>₁ = −1 and <i>z</i>₂ = 2. The percentage between <i>z</i>₁ = −1 and <i>z</i>₂ = 2 is 34 + 34 + 13.5 = <b>81.5%</b>.',sh('w31',-1,2,'81.5%'))]))
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
S.append(qslide('ex','Exit task 1 of 2 · VCAA 2019 Exam 2 Q2b','Show what you know',
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
S.append(qslide('ex','Exit task 2 of 2 · VCAA 2021 Exam 2 Q1c','Show what you know',
  ('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.',
   SP,'Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place. <span class="muted">(1 mark)</span>'),
  [('Write down',f'{X} = 14.50, {XB} = 13.74, {SD} = 1.43'),fx('Standardised score',Z,zf('14.50','13.74','1.43'),'0.531…'),('Round','to one decimal place: 0.5.')],
  'Jamilia’s standardised score is <b><i>z</i> = 0.5</b>.',f'{EDR} · 1I Q13 · VCAA 2021 Exam 2 Data analysis Q1c (examiner report)',stat=('mark',78),cmd=('Calculate',1,'working, then round')))
# ================= close
S.append(checkin(SC))
def _card(o):
    if isinstance(o,dict):
        if o.get('id')=='gm12-u3-s5': return o['card']
        for v in o.values():
            r=_card(v)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=_card(v)
            if r: return r
CW=_card(json.load(open(os.path.join(ROOT,'planner','unit-plan.json'))))['homework']['sets']
S.append(coursework([(st['title'].replace('Revision book','Chapter 1 practice booklet'),st.get('note') or '',['<span style="display:flex;justify-content:space-between;gap:12px"><span>'+it['skill']+'</span><b>'+it['q']+'</b></span>' for it in st['items']]) for st in CW]))
V=json.load(open(os.path.join(ROOT,'planner','videos.json'))); V=V if isinstance(V,list) else V.get('videos',[])
S.append(videos([yt(f'{v["sub"]} · {v["title"]} ({v["channel"].split(" (")[0]})',yid(v['url'])) for v in V if v['sub'] in ('1H','1I') and v.get('url')]))
n=assemble(S,'12MAG · S5 · The normal distribution and standardised scores',f'{ROOT}/lessons/S5-slides.html')
print('slides',n)
