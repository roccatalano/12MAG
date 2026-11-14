"""Build classes/general-maths-12.json: Unit 3 lesson order (names only).
Sources: VCE Mathematics Study Design 2023-2027, Cambridge General Mathematics VCE Units 3&4
(2nd ed.) curriculum grid and sample planner. Run from the repo root."""
import csv as _csv, os as _os
import json
A1=('U3 AoS1','Data analysis'); A2=('U3 AoS2','Recursion and financial modelling')
# (block, weekLabel, termLabel, aos, [(type, section, title), ...])
W=[
 ('su','Step-up week 1','Nov–Dec 2026',A1,[('lesson','1A–1B','Types of data; categorical data'),('lesson','1C–1E','Histograms, dot plots and stem plots; log scales')]),
 ('su','Step-up week 2','Nov–Dec 2026',A1,[('lesson','1F','Centre and spread: median, quartiles, IQR, mean and standard deviation'),('lesson','1G','Five-number summary, boxplots and outliers'),('lesson','1H–1I','Normal distribution, z-scores; populations and samples')]),
 ('hol','Summer holidays','Dec 2026 – Jan 2027',A1,[('holiday','','Summer holiday work','gm12-u3-holiday')]),
 ('t1','Week 1','Term 1 · short week',A1,[('sac','1','Chapter 1 coursework check + test','gm12-u3-ch1-test'),('lesson','2A–2B','Response and explanatory variables; two-way tables','gm12-u3-l03')]),
 ('t1','Week 2','Term 1',A1,[('lesson','2C','Numerical vs categorical: parallel boxplots, back-to-back stem plots','gm12-u3-l04'),('lesson','2D–2E','Scatterplots: direction, form and strength','gm12-u3-l05'),('lesson','2F','Correlation coefficient, $r$','gm12-u3-l06')]),
 ('t1','Week 3','Term 1',A1,[('lesson','2G–2H','Coefficient of determination; correlation and causation','gm12-u3-l07'),('lesson','2I','Which graph?','gm12-u3-l08'),('sac','2','Chapter 2 coursework check + test','gm12-u3-ch2-test')]),
 ('t1','Week 4','Term 1',A1,[('lesson','3A','Least squares regression line','gm12-u3-l09'),('lesson','3B','Interpreting slope and intercept; predictions','gm12-u3-l10'),('lesson','3C','Residual analysis and regression analysis','gm12-u3-l11')]),
 ('t1','Week 5','Term 1',A1,[('sac','3','Chapter 3 coursework check + test','gm12-u3-ch3-test'),('lesson','4A','Squared transformation','gm12-u3-l12'),('lesson','4B','Log transformation','gm12-u3-l13')]),
 ('t1','Week 6','Term 1',A1,[('lesson','4C','Reciprocal transformation','gm12-u3-l14'),('lesson','4D','Choosing and applying a transformation','gm12-u3-l15'),('sac','4','Chapter 4 coursework check + test','gm12-u3-ch4-test')]),
 ('t1','Week 7','Term 1 · Labour Day Mon 8 Mar',A1,[('lesson','5A','Time series data: features of time series plots','gm12-u3-l16'),('lesson','5B','Smoothing with moving means','gm12-u3-l17'),('lesson','5B','Centring moving means','gm12-u3-l18')]),
 ('t1','Week 8','Term 1',A1,[('lesson','5C','Smoothing with moving medians','gm12-u3-l19'),('lesson','5D','Seasonal indices','gm12-u3-l20'),('lesson','5D','Deseasonalising and reseasonalising','gm12-u3-l21')]),
 ('t1','Week 9','Term 1',A1,[('lesson','5E','Trend lines and forecasting','gm12-u3-l22'),('sac','5','Chapter 5 coursework check + test','gm12-u3-ch5-test'),('review','SAC 1','SAC 1 practice application task','gm12-u3-l25')]),
 ('t2','Week 1','Term 2',A2,[('review','SAC 1','SAC 1 refresher (before Part 1, Wed 14 Apr after school)'),('review','SAC 1','SAC 1 revision'),('sac','SAC 1','SAC 1 Part 2: in class (10 min reading + 60 min)')]),
 ('t2','Week 2','Term 2',A2,[('review','SAC 1','SAC 1 revision (before Part 3, Wed 21 Apr after school)'),('lesson','7A','Sequences and recurrence relations (after SAC 1 Part 3)'),('lesson','7B, 7D','Linear and geometric growth and decay')]),
 ('t2','Week 3','Term 2',A2,[('lesson','7C, 7E','Explicit rules for linear and geometric growth and decay'),('lesson','7F','Interest rates over different periods; effective interest rates'),('review','SAC 1','SAC 1 feedback')]),
 ('t2','Week 4','Term 2',A2,[('sac','7','Chapter 7 coursework check + test'),('lesson','8A','Compound interest investments with regular additions'),('lesson','8B','Reducing balance loans and annuities')]),
 ('t2','Week 5','Term 2',A2,[('lesson','8C','Amortisation tables'),('lesson','8D','Analysing financial situations with amortisation tables'),('lesson','8E','Finance solver: balance and final payment')]),
 ('t2','Week 6','Term 2',A2,[('lesson','8F','Finance solver: interest rate, time and payment'),('lesson','8G','Harder financial problems'),('lesson','8H','Interest-only loans')]),
 ('t2','Week 7','Term 2',A2,[('lesson','8I','Perpetuities'),('sac','8','Chapter 8 coursework check + test'),('review','9','Review: recursion and financial modelling')]),
 ('t2','Week 8','Term 2',A2,[('review','SAC 2','SAC 2 revision (Part 1, Wed 2 Jun after school)'),('review','Exam','Unit 3 exam revision'),('review','Exam','Unit 3 exam revision')]),
 ('t2','Week 9','Term 2 · trial exam week',A2,[('sac','Exam','Unit 3 trial exams')]),
 ('t2','Week 10','Term 2',A2,[('tbc','','To be planned'),('tbc','','To be planned'),('tbc','','To be planned')]),
 ('t2','Week 11','Term 2',A2,[('tbc','','To be planned'),('tbc','','To be planned'),('tbc','','To be planned')]),
]
TASKS={'holiday':['Holiday pack ready','Set before the last step-up lesson'],'tbc':[],'lesson':['Slides ready','Guided sheet ready','Exit ticket'],'review':['Review set ready'],'sac':['Task ready','Marking scheme ready']}
L=[];n=0;s=0
for wi,(blk,wl,tl,(aos,at),ls) in enumerate(W,1):
  for typ,sec,title,*fix in ls:
    if blk=='hol': num='H'
    elif blk=='su': s+=1;num=f'S{s}'
    else: n+=1;num=n
    # IDs: an explicit id keeps a lesson's data (Do Now, APK, exits, CFATs, ticks) attached when lessons move.
    L.append(dict(type=typ,section=sec,title=title,aos=aos,aosTitle=at,unit=3,week=wi,weekLabel=wl,termLabel=tl,lesson=num,
      id=(fix[0] if fix else f'gm12-u3-{num if blk=="su" else "l%02d"%num}').lower(),keyKnowledge=[],questions=[],tasks=[dict(text=t,done=False) for t in TASKS[typ]]))
# Chapter-end lessons: coursework check (CFATs, bound reference, guided notes, homework) + chapter test.
for l in L:
  if l['title'].endswith('coursework check + test'):
    l['tasks']=[dict(text=t,done=False) for t in ['Coursework checklist ready (CFATs, bound reference, guided notes, homework)','Chapter test ready','Marking scheme ready']]
import datetime as dt
START={'t1':dt.date(2027,1,25),'t2':dt.date(2027,4,12)}; END={'t1':dt.date(2027,3,25)}
def rng(blk,wl):
  if blk not in START: return ''
  mon=START[blk]+dt.timedelta(weeks=int(wl.split()[1])-1)
  a=max(mon,dt.date(2027,1,28)); b=min(mon+dt.timedelta(days=4),END.get(blk,dt.date(2099,1,1)))
  f=lambda d:f"{d.day} {d.strftime('%b')}"
  return f"{a.day}–{f(b)}" if a.month==b.month else f"{f(a)} – {f(b)}"
for blk,wl,tl,_,_ in W:
  for l in L:
    if l['weekLabel']==wl and l['termLabel']==tl: l['dates']=rng(blk,wl)
for l in L:
  if l['title'] in ('Unit 3 trial exams','Summer holiday work'): l['span']=3
# CFATs (from Planning\Topics\1. Data Analysis\README.md + HANDOFF.md). ~20 min each, on lighter lessons.
FMT='About 20 min · individual · CAS and single bound reference allowed'
SRC='Edrolo GM U3&4 2023 exercise questions (CFAT-only)'
DIR='1. Data Analysis\\CFATs\\Chapter 1\\'
CF={
 'gm12-u3-s3':[dict(id='CFAT 1.1.1',title='Types of data, displays, log scales',covers=['1A','1B','1C','1D','1E'],format=FMT,file=DIR+'CFAT 1.1.1 [1A, 1B, 1C, 1D, 1E].docx',status='Written (10 Nov 2026)',
   plan='Start of Step-up lesson 3. Covers step-up week 1 (1A–1E).',sources=[SRC+': 1A Q15, Q17 · 1B Q8, Q9 · 1C Q6, Q17 · 1D Q9, Q12, Q14'])],
 'gm12-u3-s5':[dict(id='CFAT 1.1.2',title='Describing numerical data: median, IQR, boxplots, SOCS',covers=['1F (median, IQR)','1G'],format=FMT,file=DIR+'CFAT 1.1.2 [1F, 1G].docx',status='Written (10 Nov 2026)',
   plan='Start of Step-up lesson 5. Covers Step-up lessons 3–4 (1F, 1G).',sources=[SRC+': 1E Q1, Q8, Q11, Q14, Q17, Q18 · 1F Q12, Q16, Q18, Q19'])],
 'gm12-u3-s5b':[dict(id='CFAT 1.1.3',title='Mean and SD, the normal distribution, z-scores',covers=['1F (mean, SD)','1H','1I'],format=FMT,file=DIR+'CFAT 1.1.3 [1H, 1F, 1I].docx',status='Written (10 Nov 2026)',marks=16,
   plan='Summer holiday work: set in Step-up lesson 5, gone over in the Chapter 1 coursework check + test lesson.',sources=[SRC+': 1G Q4 · 1H Q8, Q11, Q13 · 1I Q1, Q4, Q9, Q12, Q15'])],
}
CF['gm12-u3-holiday']=CF.pop('gm12-u3-s5b')
for l in L:
  if l['id'] in CF: l['cfats']=CF[l['id']]
# Step-up lesson details. LOs: Cambridge learning intentions (verbatim). SC: Cambridge Chapter 1 skills checklist (verbatim).
# Study Design: VCE Mathematics Study Design 2023-2027, GM U3 AoS1 'Investigating data distributions' (verbatim).
# Vocab: terms from the Chapter 1 'Key ideas and chapter summary'; short definitions in our own words.
SDT=['types of data',
 'representation, display and description of the distributions of categorical variables: data tables, two-way frequency tables and their associated segmented bar charts',
 'representation, display and description of the distributions of numerical variables: dot plots, stem plots, histograms; the use of a logarithmic (base 10) scale to display data ranging over several orders of magnitude and their interpretation in terms of powers of ten',
 'use of the distribution(s) of one or more categorical or numerical variables to answer statistical questions',
 'summary of the distributions of numerical variables; the five-number summary and boxplots (including the use of the lower fence (Q1 – 1.5 × IQR) and upper fence (Q3 + 1.5 × IQR) to identify and display possible outliers); the sample mean and standard deviation and their use in comparing data distributions in terms of centre and spread',
 'the normal model for bell-shaped distributions and the use of the 68–95–99.7% rule to estimate percentages and to give meaning to the standard deviation; standardised values (z-scores) and their use in comparing data values across distributions']
LOS={'1A':['To be able to classify data as categorical or numerical.','To be able to further classify categorical data as nominal or ordinal.','To be able to further classify numerical data as discrete or continuous.'],
 '1B':['To be able to construct frequency and percentage frequency tables for categorical data.','To be able to construct bar charts and percentage bar charts from frequency tables.','To be able to interpret and describe frequency tables and bar charts.','To be able to answer statistical questions about a categorical variable.'],
 '1C':['To be able to construct frequency tables for discrete numerical data.','To be able to construct frequency tables for grouped numerical data (discrete and continuous).','To be able to construct a histogram from a frequency table for numerical data.','To be able to construct a histogram from numerical data using a CAS calculator.','To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.'],
 '1D':['To be able to construct a dot plot for numerical data.','To be able to construct a stem plot for numerical data.'],
 '1E':['To be able to revise the concept of log10 x.','To be able to investigate the effect of the logarithmic scale on the features of a distribution.'],
 '1F':['To be able to understand the mean and the median as measures of centre.','To be able to understand the range, interquartile range and standard deviation as measures of spread.'],
 '1G':['To be able to construct the boxplot for displaying the distribution of a numerical data.','To be able to define and identify outliers.','To be able to construct both simple boxplots and boxplots with outliers.','To be able to determine the features of a distribution from a boxplot.','To be able to use a CAS calculator to construct a boxplot.'],
 '1H':['To be able to introduce the normal model for bell-shaped distributions.','To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.','To be able to calculate standardised scores and use them to compare values across distributions.'],
 '1I':['No learning intentions found for 1I in the printed textbook (not assessed in the CFATs).']}
SC={'1A':['I can identify types of data.'],
 '1B':['I can construct a frequency table for categorical data.','I can construct a bar chart from a frequency table.','I can construct a percentage segmented bar chart from a frequency table.','I can describe the distribution of a categorical variable.'],
 '1C':['I can construct a frequency table for discrete numerical data.','I can construct a grouped frequency table.','I can construct a histogram from a grouped frequency table.','I can describe the features of a distribution from a histogram.'],
 '1D':['I can construct a dot plot.','I can construct a stem plot.'],
 '1E':['I can use a CAS calculator to find logs.','I can interpret a histogram with a log scale.'],
 '1F':['I can find the median value in a data set.','I can find the median value from a dot plot.','I can find the median value from a stem plot.','I can find the range from a stem plot.','I can find the IQR from a stem plot when n is even.','I can find the IQR from a stem plot when n is odd.','I can calculate the mean using the formula.','I can calculate the mean and standard deviation using the CAS calculator.'],
 '1G':['I can construct a boxplot from a five number summary.','I can construct a boxplot with outliers from data using the CAS calculator.','I can read values from a boxplot.','I estimate percentages from a boxplot.','I can use boxplots for describe a distribution without outliers.','I can use boxplots to describe a distribution with outliers.','I can use boxplots to answer statistical questions.'],
 '1H':['I can apply the 68-95-99.7% rule.','I can calculate standardised scores.','I can use standardised scores to make comparisons.','I can use standard scores to determine percentages.','I can convert standardised scores into actual scores.','I can solve for the values of the mean and standard deviation.'],
 '1I':[]}
V=dict(
 cat=['Categorical variable: describes a quality or category, not a quantity','Nominal: categories with no natural order (e.g. eye colour)','Ordinal: categories with a natural order (e.g. shirt size)','Numerical variable: values are quantities','Discrete: counted, whole-number values','Continuous: measured, any value in a range','Frequency table: lists each value and how often it occurs (count and %)','Bar chart: a bar for each category, bars separated by gaps','Segmented bar chart: one bar split into segments, one per category','Mode (modal category): the most common value or category'],
 num=['Histogram: columns showing the frequency of numerical data in class intervals; bars touch','Dot plot: one dot per data value above a number line','Stem plot: each value split into a stem (leading digits) and a leaf (last digit), with a key','Shape: symmetric, positively skewed or negatively skewed','Outlier: a value that stands out from the rest of the data','Log scale: an axis in powers of 10, for data spanning several orders of magnitude'],
 cen=['Summary statistics: numbers that describe features of a distribution, such as centre and spread','Mean (x̄): the sum of the values divided by n','Median (M): the middle value of the ordered data','Range: largest value minus smallest value','Quartiles (Q1, Q3): split the ordered data into four equal groups','Interquartile range (IQR): Q3 − Q1, the spread of the middle 50%','Standard deviation (s): spread of the data around the mean'],
 box=['Five-number summary: min, Q1, median, Q3, max','Boxplot: a display of the five-number summary, with outliers shown separately','Lower fence: Q1 − 1.5 × IQR','Upper fence: Q3 + 1.5 × IQR','Outlier: a value below the lower fence or above the upper fence'],
 nor=['Normal distribution: a bell-shaped model for symmetric data','68–95–99.7% rule: about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean','Standardised score (z-score): how many standard deviations a value is above or below the mean','Population: every member of the group being studied','Sample: a subset of the population'])
DET={'gm12-u3-s1':(['1A','1B'],[0,1,3],V['cat']),'gm12-u3-s2':(['1C','1D','1E'],[2,3],V['num']),'gm12-u3-s3':(['1F'],[4,3],V['cen']),
 'gm12-u3-s4':(['1G'],[4,3],V['box']),'gm12-u3-s5':(['1H','1I'],[5],V['nor'])}
for l in L:
  if l['id'] in DET:
    subs,sd,voc=DET[l['id']]
    l['learningObjectives']=[dict(sub=x,items=LOS[x]) for x in subs]
    l['successCriteria']=[dict(sub=x,items=SC[x]) for x in subs if SC[x]]
    l['studyDesign']=[SDT[i] for i in sd]
    l['keyVocab']=voc
# We Do: Cambridge Examples (titles from the Chapter 1 skills checklist / example headings) paired with the
# Edrolo You Try map agreed with Rocco (Planning\Topics\1. Data Analysis\HANDOFF.md). Edrolo chapter letters differ from Cambridge.

_VP=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'cambridge_go_videos.csv')
VIDS={(int(r['chapter']),int(r['example'])):r for r in _csv.DictReader(open(_VP,encoding='utf-8')) if r['example']}
def _vid(ch,n):
    r=VIDS.get((ch,n)); return f"Cambridge GO · {r['subchapter']} Resources" if r else None
EX={1:('1A','Types of data','Edrolo 1A Q11 a–e'),
 2:('1B','Constructing a frequency table for categorical data','Edrolo 1B WE1'),3:('1B','Constructing a bar chart from a frequency table','Edrolo 1B WE2'),
 4:('1B','Constructing a percentage segmented bar chart','Edrolo 1B WE3'),5:('1B','Describing the distribution of a categorical variable','Edrolo 1B WE4'),
 6:('1C','Constructing a frequency table for discrete numerical data',None),7:('1C','Constructing a grouped frequency table','Edrolo 1C WE4'),
 8:('1C','Constructing a histogram from a frequency table','Edrolo 1C WE5'),9:('1C','Describing the features of a distribution from a histogram',None),
 10:('1D','Constructing a dot plot','Edrolo 1C WE1'),11:('1D','Constructing a stem plot','Edrolo 1C WE2'),
 12:('1E','Using a CAS calculator to find logs','Edrolo 1D WE1'),13:('1E','Interpreting a histogram with a log scale','Edrolo 1D WE3'),
 14:('1F','Finding the median value in a data set','Edrolo 1E WE1'),15:('1F','Finding the median value from a dot plot','Edrolo 1F WE2'),
 16:('1F','Finding the median value from a stem plot','Edrolo 1F WE3'),17:('1F','Finding the range from a stem plot','Edrolo 1E WE2a'),
 18:('1F','Finding the IQR from an ordered stem plot when n is even','Edrolo 1E WE2b'),19:('1F','Finding the IQR from a stem plot when n is odd',None),
 20:('1F','Finding the median and quartiles from a histogram','Edrolo 1F WE1'),21:('1F','Calculating the mean using the formula','Edrolo 1G WE1'),
 22:('1G','Constructing a boxplot from a five-number summary','Edrolo 1E WE4'),23:('1G','Reading values from a boxplot','Edrolo 1E WE6'),
 24:('1G','Estimating percentages from a boxplot',None),25:('1G','Using a boxplot to describe a distribution without outliers','Edrolo 1F WE5'),
 26:('1G','Using a boxplot to describe a distribution with outliers',None),27:('1G','Using a boxplot to answer statistical questions',None),
 28:('1H','Applying the 68–95–99.7% rule','Edrolo 1H WE1'),29:('1H','Calculating standard scores','Edrolo 1I WE1'),
 30:('1H','Using standardised scores to make comparisons','Edrolo 1I WE3'),31:('1H','Using standardised scores to find percentages','Edrolo 1H WE2a'),
 32:('1H','Converting standardised scores into actual scores','Edrolo 1I WE2'),33:('1H','Finding the standard deviation given the mean and one percentage',None),
 34:('1H','Finding the mean and standard deviation','Edrolo 1H WE3a')}
WEDO={'gm12-u3-s1':range(1,6),'gm12-u3-s2':range(6,14),'gm12-u3-s3':range(14,22),'gm12-u3-s4':range(22,28),'gm12-u3-s5':range(28,35)}
for l in L:
  if l['id'] in WEDO:
    l['weDo']=[dict(n=n,sub=EX[n][0],title=EX[n][1],youTry=EX[n][2],video=_vid(1,n)) for n in WEDO[l['id']]]
    if l['id']=='gm12-u3-s5': l['weDoNote']='1I is online-only in Cambridge: no printed Examples.'
# CAS videos: links from 12MAG 2027\CAS Videos (Casio ClassPad and TI-nspire support-video lists for VCE GM 3&4).
def yt(t,u): return dict(title=t,url=u)
CP={'stat':yt('ClassPad Help 400 – Statistics: basic settings and actions','https://www.youtube.com/watch?v=Qqg8vWK3SE8'),
 'pie':yt('ClassPad Help 520 – Pie chart','https://www.youtube.com/watch?v=PKbqBLbW9DI'),
 'hl':yt('ClassPad Help 406 – Create a histogram from a list','https://www.youtube.com/watch?v=2YuJoKS4XvM'),
 'hf':yt('ClassPad Help 407 – Create a histogram from a frequency table','https://www.youtube.com/watch?v=E3JIz_SDywE'),
 'hc':yt('ClassPad Help 440 – Histogram class intervals','https://www.youtube.com/watch?v=nnJtqIB6yWM'),
 'sl':yt('ClassPad Help 401 – Statistical calcs from a list','https://www.youtube.com/watch?v=K93TBJP-uaA'),
 'sf':yt('ClassPad Help 402 – Statistical calcs from a frequency table','https://www.youtube.com/watch?v=GjbQKBD9f00'),
 'bl':yt('ClassPad Help 403 – Create a boxplot from a list','https://www.youtube.com/watch?v=HBS1g3cja2g'),
 'bf':yt('ClassPad Help 404 – Create a boxplot from a frequency table','https://www.youtube.com/watch?v=sw2xy8_x1k0'),
 'bm':yt('ClassPad Help 405 – Create multiple boxplots','https://www.youtube.com/watch?v=NCoE4Z-irZ0'),
 'calc':yt('ClassPad Help 007 – Simple calculations in Main','https://www.youtube.com/watch?v=Zb9V3RwXVLA'),
 'n80':yt('ClassPad Help 80 – Normal probability calculations','https://www.youtube.com/watch?v=OGBTcuB7S8E'),
 'n470':yt('ClassPad Help 470 – Normal probability calculations','https://www.youtube.com/watch?v=awgngSed02c'),
 'n81':yt('ClassPad Help 81 – Inverse normal probability calculations','https://www.youtube.com/watch?v=3VFcgs8Mp40')}
TI={'bar':yt('Bar & pie graphs | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=Wt0QZBrRzDA'),
 'lists':yt('Analysing data | Getting Started Series – Lists & Spreadsheets','https://www.youtube.com/watch?v=qDZRQeUvC0I'),
 'hist':yt('Creating histograms | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=YrluejAQRK4'),
 'dotbox':yt('Dot plots & box plots | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=73Ymuvv-BU8'),
 'long':yt('Data analysis: box-plots, dot-plots and histograms (long walkthrough)','https://www.youtube.com/watch?v=wCb6z1IbVy8&t=965s'),
 'uni':yt('Data analysis – univariate data (long walkthrough)','https://www.youtube.com/watch?v=lqml9PBBhV0&t=630s'),
 'z':yt('Calculating and understanding z-scores with TI-nspire','https://www.youtube.com/watch?v=yrR9IALJD6g'),
 'calc':yt('Settings and calculations | Getting Started Series – Calculator','https://www.youtube.com/watch?v=35RcQzXqj6o')}
SK=lambda name,cp,ti:dict(skill=name,classpad=[CP[k] for k in cp],ti=[TI[k] for k in ti])
CASV={'gm12-u3-s1':[SK('Setting up the statistics app',['stat'],['lists'])],
 'gm12-u3-s2':[SK('Creating a histogram',['hl','hf'],['hist']),SK('Setting histogram class intervals',['hc'],[]),
   SK('Creating a dot plot',[],['dotbox']),SK('Finding logs (base 10)',['calc'],['calc']),SK('Full walkthrough: dot plots, boxplots and histograms',[],['long'])],
 'gm12-u3-s3':[SK('Calculating summary statistics (mean, median, standard deviation)',['sl','sf'],['lists','uni'])],
 'gm12-u3-s4':[SK('Creating a boxplot',['bl','bf'],['dotbox','long']),SK('Creating parallel boxplots',['bm'],[])],
 'gm12-u3-s5':[SK('Calculating z-scores',['calc'],['z']),SK('Normal probability calculations',['n80','n470','n81'],[])]}
for l in L:
  if l['id'] in CASV: l['cas']=CASV[l['id']]
# ---- AoS1 Chapters 2-5 lesson details (appended) ----
SDA=['response and explanatory variables and their role in investigating associations between variables',
 'contingency (two-way) frequency tables, their associated bar charts (including percentage segmented bar charts) and their use in identifying and describing associations between two categorical variables',
 'back-to-back stem plots, parallel dot plots and boxplots and their use in identifying and describing associations between a numerical variable and a categorical variable',
 'scatterplots and their use in identifying and qualitatively describing the association between two numerical variables in terms of direction (positive/negative), form (linear/non-linear) and strength (strong/moderate/weak)',
 'answering statistical questions that require a knowledge of the associations between pairs of variables',
 'Pearson correlation coefficient, r, and its calculation and interpretation',
 'cause and effect; the difference between observation and experimentation when collecting data and the need for experimentation to definitively determine cause and effect']
SDM=['least squares line of best fit y = a + bx, where x represents the explanatory variable, and y represents the response variable; the determination of the coefficients a and b using technology, and the formulas b = r × s_y / s_x and a = ȳ − b x̄',
 'modelling linear association between two numerical variables, including the: identification of the explanatory and response variables; use of the least squares method to fit a linear model to the data',
 'interpretation of the slope and intercepts of the least squares line in the context of the situation being modelled, including: use of the rule of the fitted line to make predictions being aware of the limitations of extrapolation',
 'use of the coefficient of determination, r², to assess the strength of the association in terms of explained variation',
 'use of residual analysis to check quality of fit',
 'data transformation and its use in transforming some forms of non-linear data to linearity using a square, logarithmic (base 10) or reciprocal transformation (applied to one axis only)',
 'interpretation and use of the equation of the least squares line fitted to the transformed data to make predictions']
SDT2=['qualitative features of time series plots; recognition of features such as trend (long-term direction), seasonality (systematic, calendar related movements) and irregular fluctuations (unsystematic, short-term fluctuations); possible outliers and their sources, including one-off real-world events, and signs of structural change such as a discontinuity in the time series',
 'numerical smoothing of time series data using moving means with consideration of the number of terms required (using centring when appropriate) to help identify trends in time series plot with large fluctuations',
 'graphical smoothing of time series plots using moving medians (involving an odd number of points only) to help identify long-term trends in time series with large fluctuations',
 'seasonal adjustment including the use and interpretation of seasonal indices and their calculation using seasonal and yearly means',
 'modelling trend by fitting a least squares line to a time series with time as the explanatory variable (data de-seasonalised where necessary), and the use of the model to make forecasts (with re-seasonalisation where necessary) including consideration of the possible limitations of fitting a linear model and the limitations of extending into the future']
NOLI='No learning intentions for this subchapter in the printed textbook.'
LOS.update({
 '2A':['To introduce bivariate data.','To be able to classify data as categorical or numerical.','To be able to identify explanatory and response variables.'],
 '2B':['To be able to summarise data from two categorical variables using two-way frequency tables.','To be able to appropriately percentage two-way frequency tables.','To be able to use a percentaged two-way frequency table to identify and describe an association between two categorical variables.'],
 '2C':['To be able to use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable for small data sets.','To be able to use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable for small data sets.','To be able to use parallel boxplots to display the association between a numerical variable and a categorical variable which can take two or more values.'],
 '2D':['To be able to introduce the scatterplot for displaying data from two numerical variables.','To be able to construct a scatterplot using a CAS calculator.'],
 '2E':['To be able to use a scatterplot to identify an association between two variables.','From the the scatterplot, be able to classify an association according to: direction, which may be positive or negative; form, which may be linear or non-linear; strength, which may be weak, moderate or strong.'],
 '2F':['To introduce Pearson’s correlation coefficient r as a measure of the strength of a linear association between two variables.','To be able to use technology to determine the value of Pearson’s correlation coefficient r.','To be able to classify the strength of a linear association as weak, moderate or strong based on the value of Pearson’s correlation coefficient r.'],
 '2G':['To be able to calculate the value of the coefficient of determination.','To be able to use the coefficient of determination to assess the strength of the association in terms of the explained variation.'],
 '2H':['To be able to define and differentiate the concepts of association and causation.'],
 '2I':[NOLI],
 '3A':['To be able to define linear regression.','To be able to define a residual.','To introduce the least squares line of best fit.','To be able to find the equation of the least squares line using summary statistics.','To be able to find the equation of the least squares line using technology.'],
 '3B':['To be able to interpret the intercept and slope of the least squares line.','To be able to use the equation of the least squares line to make predictions.','To be able to use the coefficient of determination in a regression analysis.','To be able to use a residual plot to investigate the linearity assumption.','To be able to report a regression analysis.'],
 '3C':[NOLI],
 '4A':['To be able to apply a squared transformation to either x or y.','To be able to fit a least squares regression line to the transformed data.','To be able to use the least squares regression line fitted to the transformed data for prediction.'],
 '4B':['To be able to apply a log10 transformation to either x or y.','To be able to fit a least squares regression line to the transformed data.','To be able to use the least squares regression line fitted to the transformed data for prediction.'],
 '4C':['To be able to apply a reciprocal transformation to either x or y.','To be able to fit a least squares regression line to the transformed data.','To be able to use the least squares regression line fitted to the transformed data for prediction.'],
 '4D':['To be able to use the circle of transformations to determine which transformations may help linearise a non-linear association.','To be able to use a residual plot to assess the effectiveness of a data transformation.','To be able to use the coefficient of determination to assess the effectiveness of a data transformation.'],
 '5A':['To be able to recognise time series data.','To be able to construct a time series plot.','To be able to recognise features in the plot such as trend, seasonality and irregular fluctuations.'],
 '5B':['To be able to smooth a time series plot using moving means.','To be able to know when and how to use centring when smoothing.'],
 '5C':['To be able to locate the median of a data set graphically.','To be able to smooth a time series plot using moving medians.'],
 '5D':['To be able to interpret the meaning of seasonal indices.','To be able to seasonally adjust data using seasonal indices.','To be able to calculate seasonal indices from time series data.'],
 '5E':['To be able to use the method of least squares to fit a trend line to a time series.','To be able to use the trend line to make predictions.','To be able to use seasonal indices to add seasonality to predicted values as appropriate.']})
SC.update({
 '2A':['I can identify categorical and numerical variables in bivariate data.','I can identify explanatory and response variables.'],
 '2B':['I can construct a two-way frequency table.','I can percentage a two-way frequency table.','I can describe an association from a percentaged two-way frequency table.','I can construct a segmented bar chart from a percentaged two-way frequency table.','I can describe an association from a percentaged segmented bar chart.'],
 '2C':['I can use parallel dot plots to identify and describe the association between a numerical variable and a categorical variable.','I can use back-to-back stem plots to display and describe the association between a numerical variable and a categorical variable.','I can use parallel boxplots to display and describe the association between a numerical variable and a categorical variable.'],
 '2D':['I can construct a scatterplot using a CAS calculator.'],
 '2E':['I can classify the direction, form and strength of an association from a scatterplot.'],
 '2F':['I can use technology to determine the value of the correlation coefficient r.','I can classify the strength of a linear association as weak, moderate or strong based on the value of the correlation coefficient r.'],
 '2G':['I can calculate the value of the coefficient of determination.','I can use the coefficient of determination to assess the strength of the association in terms of the the explained variation.'],
 '2H':['I understand that correlation does not imply causation.'],'2I':[],
 '3A':['I can determine the equation of the least squares regression line using the formulas.','I can determine the correlation coefficient from the slope of the least squares regression line using the formula.','I can determine the equation of the least squares regression line using a CAS calculator.'],
 '3B':['I can interpret the slope and intercept of a regression line.','I can use the regression line to make predictions.','I can use the coefficient of determination to compare associations.','I can calculate residual values.','I can interpret a residual plot.','I can write a report based on a regression analysis.'],
 '3C':['I can use a CAS calculator to generate all of the analyses required for a regression analysis.'],
 '4A':['I can apply the x² transformation.','I can apply the y² transformation.'],'4B':['I can apply the log x transformation.','I can apply the log y transformation.'],
 '4C':['I can apply the reciprocal (1/x) transformation.','I can apply the reciprocal (1/y) transformation.'],'4D':['I can choose the best transformation to apply.'],
 '5A':['I can construct a time series plot.','I can identify trend in a time series plot.','I can identify cycles in a time series plot.','I can identify seasonality in a time series plot.','I can identify structural change in a time series plot.','I can identify outliers in a time series plot.'],
 '5B':['I can smooth a time series using moving mean smoothing.','I can smooth a time series using moving mean smoothing with centring.'],
 '5C':['I can smooth a time series using moving median smoothing.'],
 '5D':['I can interpret seasonal indices.','I can use seasonal indices to deseasonalise and reseasonalise data.','I can use seasonal indices to determine percentage change required to correct for seasonality.','I can calculate seasonal indices from 1 year of data.','I can calculate seasonal indices from several years of data.','I can use seasonal indices to deseasonalise a time series.'],
 '5E':['I can fit a trend line to a time series plot.','I can use a trend line to forecast a future value (no seasonality).','I can fit a trend line to a time series plot with seasonality.','I can use a trend line to forecast a future value (with seasonality).']})
EX2={2:{1:('2A','Identifying associations as categorical or numerical'),2:('2A','Identifying the response and explanatory variables'),3:('2A','Identifying the response and explanatory variables'),
 4:('2B','Constructing a two-way frequency table'),5:('2B','Identifying and describing an association from a percentaged two-way table (2 × 2)'),6:('2B','Identifying and describing associations from a percentaged two-way table (3 × 3)'),
 7:('2B','Constructing a segmented bar chart'),8:('2B','Identifying and describing associations from a segmented bar chart'),9:('2C','Using a parallel dot plot to identify and describe associations'),
 10:('2C','Using a back-to-back stem plot to identify and describe associations'),11:('2C','Comparing distributions across two groups using parallel boxplots'),12:('2C','Comparing distributions across more than two groups using parallel boxplots'),
 13:('2E','Direction of association'),14:('2E','Form of an association'),15:('2E','Strength of an association'),16:('2F','Classifying the strength of a linear association'),
 17:('2G','Calculating the coefficient of determination'),18:('2G','Interpreting the coefficient of determination'),19:('2G','Calculating and interpreting the coefficient of determination'),
 20:('2G','Calculating and interpreting the coefficient of determination'),21:('2G','Calculating the correlation coefficient from the coefficient of determination')},
 3:{1:('3A','Determining the equation of the least squares regression line using summary statistics and the correlation coefficient'),2:('3A','Determining the correlation coefficient using the slope of the least squares regression line'),
 3:('3B','Interpreting the slope and intercept of a regression line'),4:('3B','Using the regression line to make predictions'),5:('3B','Using the coefficient of determination to compare associations'),
 6:('3B','Calculating a residual'),7:('3B','Interpreting a residual plot'),8:('3B','Reporting the results of a regression analysis')},
 4:{1:('4A','Applying the x-squared transformation'),2:('4A','Applying the y-squared transformation'),3:('4B','Applying the log x transformation'),4:('4B','Applying the log y transformation'),
 5:('4C','Applying the reciprocal (1/x) transformation'),6:('4C','Applying the reciprocal (1/y) transformation'),7:('4D','Choosing the best transformation')},
 5:{1:('5A','Constructing a time series plot'),2:('5A','Identifying trends'),3:('5A','Identifying cycles'),4:('5A','Identifying seasonality'),5:('5A','Identifying structural change'),6:('5A','Identifying outliers'),
 7:('5B','Three- and five-moving mean smoothing'),8:('5B','Three- and five-moving mean smoothing of a time series'),9:('5B','Two-moving mean smoothing with centring'),10:('5B','Four- and six-moving mean smoothing with centring'),
 11:('5B','Smoothing of a time series using four-mean smoothing with centring'),12:('5C','Three-moving median smoothing using a graphical approach'),13:('5C','Five-moving median smoothing using a graphical approach'),
 14:('5D','Interpreting seasonal indices'),15:('5D','Using seasonal indices'),16:('5D','Using seasonal indices to determine percentage change required to correct for seasonality'),
 17:('5D','Calculating seasonal indices (1 year’s data)'),18:('5D','Calculating seasonal indices (several years’ data)'),19:('5D','Deseasonalising a time series'),
 20:('5E','Fitting a trend line'),21:('5E','Forecasting'),22:('5E','Fitting a trend line (seasonality)'),23:('5E','Forecasting (seasonality)')}}
YT2={(2,4):'Edrolo 2A WE1',(2,5):'Edrolo 2A WE4',(2,7):'Edrolo 2A WE3',(2,8):'Edrolo 2A WE5'}
CP.update({'sr':yt('ClassPad Help 411 – Scatterplot and regression','https://www.youtube.com/watch?v=EShk1ze8Cpw'),
 'pr':yt('ClassPad Help 441 – Prediction from regression line','https://www.youtube.com/watch?v=hr_53Cu1xSs'),
 'res':yt('ClassPad Help 442 – Residuals and residual plots','https://www.youtube.com/watch?v=q5mm9-QHhlE'),
 'ts':yt('ClassPad Help 412 – xyLine time series','https://www.youtube.com/watch?v=g8HfR10oVtY'),
 'sm':yt('ClassPad Help 545 – Smoothing time series','https://www.youtube.com/watch?v=tzfG4MilCQ4'),
 'mav':yt('ClassPad Help 945 – Smoothing time series using mavII','https://www.youtube.com/watch?v=WMEW4LykEgA')})
TI.update({'sc':yt('Scatterplots | Getting Started Series – Lists & Spreadsheets','https://www.youtube.com/watch?v=AMH-Dj-VYm8'),
 'asc':yt('Analysing scatterplots | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=97ptJ2fbafM'),
 'biv':yt('Statistical plots & bivariate data | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=5ZrJDq4RqD4&t=364s'),
 'lr':yt('How to perform linear regression with TI-nspire','https://www.youtube.com/watch?v=Xse7Aqb0fLI')})
VB=dict(
 biv=['Bivariate data: two variables recorded for each individual','Explanatory variable (EV): the variable that may explain or predict changes in the other variable','Response variable (RV): the variable that responds to changes in the EV','Two-way frequency table: counts of two categorical variables, cross-tabulated','Percentaged two-way table: percentages calculated within each category of the EV','Association: knowing the value of one variable helps predict the value of the other','Segmented bar chart: one bar per EV category, split by the RV'],
 numcat=['Parallel dot plots: dot plots for each group on a common scale','Back-to-back stem plot: two groups sharing one stem','Parallel boxplots: a boxplot for each group on a common scale','Comparing groups: compare shape, centre (median), spread (IQR) and outliers'],
 sca=['Scatterplot: a plot of paired numerical data, EV on the horizontal axis','Direction: positive or negative','Form: linear or non-linear','Strength: weak, moderate or strong','Outlier: a point that does not fit the pattern of the rest'],
 r=['Pearson’s correlation coefficient (r): measures the strength and direction of a linear association, from −1 to 1','Strength guide: |r| ≥ 0.75 strong · 0.5 to 0.75 moderate · 0.25 to 0.5 weak · below 0.25 no association','Only use r when the association is linear, with no clear outliers'],
 r2=['Coefficient of determination (r²): the percentage of the variation in the RV that is explained by the variation in the EV','Causation: one variable directly causes a change in the other','Confounding variable: another variable that affects both variables','Common response: both variables respond to a third variable','Coincidence: an association that happens by chance','Experiment: needed to show cause and effect; an observational study is not enough'],
 lsrl=['Least squares regression line: y = a + bx, the line that makes the sum of squared residuals as small as possible','Slope (b) = r × s_y / s_x','Intercept (a) = ȳ − b x̄','Residual: actual value − predicted value'],
 interp=['Slope interpretation: on average, the RV changes by b for each 1-unit increase in the EV','Intercept interpretation: the predicted RV when the EV is 0','Interpolation: predicting within the range of the data (reliable)','Extrapolation: predicting outside the range of the data (unreliable)'],
 resid=['Residual plot: residuals plotted against the EV','Random scatter: supports the linearity assumption','Clear pattern (e.g. a curve): the association is not linear','Regression analysis report: direction, form, strength, equation, slope, r² and residual check'],
 tr=['Data transformation: applying a function to one axis to linearise the data','Squared transformation: x² or y²','Log transformation: log x or log y (base 10)','Reciprocal transformation: 1/x or 1/y','Circle of transformations: shows which transformations may linearise each shape of curve','Choosing the best transformation: compare residual plots and r²'],
 ts=['Time series data: values recorded at regular time intervals','Trend: the long-term increase or decrease','Seasonality: a regular calendar-related pattern','Cycles: up-and-down movement over periods longer than a year','Irregular fluctuations: unpredictable, short-term changes','Structural change: a sudden change in the level or pattern','Outlier: a value that does not fit the pattern'],
 mm=['Moving mean smoothing: replacing each value by the mean of it and its neighbours','Centring: needed when smoothing over an even number of points'],
 med=['Moving median smoothing: replacing each value by the median of it and its neighbours, done graphically','Uses an odd number of points'],
 si=['Seasonal index: actual value ÷ seasonal average','Seasonal indices add up to the number of seasons (and average to 1)','Deseasonalise: actual value ÷ seasonal index','Reseasonalise: deseasonalised value × seasonal index'],
 trend=['Trend line: a least squares line fitted with time as the EV','Forecasting: using the trend line to predict future values','Limitations: forecasts further into the future are less reliable'])
def subs_items(D,pairs): return [dict(sub=s,items=D[s][a:b]) for s,a,b in pairs if D[s][a:b]]
def exs(ch,ns): return [dict(n=n,sub=EX2[ch][n][0],title=EX2[ch][n][1],youTry=YT2.get((ch,n),'TBM'),video=_vid(ch,n)) for n in ns]
F=lambda s:(s,0,None)
A2={
 'gm12-u3-l03':([F('2A'),F('2B')],[F('2A'),F('2B')],[SDA[0],SDA[1]],VB['biv'],[],exs(2,range(1,9))),
 'gm12-u3-l04':([F('2C')],[F('2C')],[SDA[2],SDA[4]],VB['numcat'],[SK('Creating parallel boxplots',['bm'],['dotbox','long'])],exs(2,range(9,13))),
 'gm12-u3-l05':([F('2D'),F('2E')],[F('2D'),F('2E')],[SDA[3]],VB['sca'],[SK('Creating a scatterplot',['sr'],['sc','asc','biv'])],exs(2,range(13,16))),
 'gm12-u3-l06':([F('2F')],[F('2F')],[SDA[5]],VB['r'],[SK('Finding the correlation coefficient r',['sr'],['lr'])],exs(2,[16])),
 'gm12-u3-l07':([F('2G'),F('2H')],[F('2G'),F('2H')],[SDM[3],SDA[6]],VB['r2'],[SK('Finding r and r²',['sr'],['lr'])],exs(2,range(17,22))),
 'gm12-u3-l08':([F('2I')],[],[SDA[4]],[],[],[]),
 'gm12-u3-l09':([F('3A')],[F('3A')],[SDM[0],SDM[1]],VB['lsrl'],[SK('Finding the least squares regression line',['sr'],['lr'])],exs(3,[1,2])),
 'gm12-u3-l10':([('3B',0,3)],[('3B',0,3)],[SDM[2],SDM[3]],VB['interp'],[SK('Making predictions from the regression line',['pr'],['lr'])],exs(3,[3,4,5])),
 'gm12-u3-l11':([('3B',3,5),F('3C')],[('3B',3,6),F('3C')],[SDM[4]],VB['resid'],[SK('Residuals and residual plots',['res'],['asc']),SK('Full regression analysis',['sr','res'],['lr'])],exs(3,[6,7,8])),
 'gm12-u3-l12':([F('4A')],[F('4A')],[SDM[5],SDM[6]],VB['tr'][:2],[SK('Fitting a regression line to transformed data',['sr'],['lr'])],exs(4,[1,2])),
 'gm12-u3-l13':([F('4B')],[F('4B')],[SDM[5],SDM[6]],[VB['tr'][0],VB['tr'][2]],[SK('Fitting a regression line to transformed data',['sr'],['lr'])],exs(4,[3,4])),
 'gm12-u3-l14':([F('4C')],[F('4C')],[SDM[5],SDM[6]],[VB['tr'][0],VB['tr'][3]],[SK('Fitting a regression line to transformed data',['sr'],['lr'])],exs(4,[5,6])),
 'gm12-u3-l15':([F('4D')],[F('4D')],[SDM[5],SDM[4]],VB['tr'],[SK('Checking a transformation: residual plot and r²',['res','sr'],['lr','asc'])],exs(4,[7])),
 'gm12-u3-l16':([F('5A')],[F('5A')],[SDT2[0]],VB['ts'],[SK('Plotting a time series',['ts'],[])],exs(5,range(1,7))),
 'gm12-u3-l17':([('5B',0,1)],[('5B',0,1)],[SDT2[1]],VB['mm'][:1],[SK('Smoothing a time series (moving means)',['sm','mav'],[])],exs(5,[7,8])),
 'gm12-u3-l18':([('5B',1,2)],[('5B',1,2)],[SDT2[1]],VB['mm'],[SK('Smoothing a time series (moving means)',['sm','mav'],[])],exs(5,[9,10,11])),
 'gm12-u3-l19':([F('5C')],[F('5C')],[SDT2[2]],VB['med'],[],exs(5,[12,13])),
 'gm12-u3-l20':([('5D',0,2)],[('5D',0,3)],[SDT2[3]],VB['si'],[],exs(5,[14,15,16])),
 'gm12-u3-l21':([('5D',2,3)],[('5D',3,6)],[SDT2[3]],VB['si'],[],exs(5,[17,18,19])),
 'gm12-u3-l22':([F('5E')],[F('5E')],[SDT2[4]],VB['trend'],[SK('Fitting a trend line (least squares)',['sr','pr'],['lr'])],exs(5,range(20,24)))}
for l in L:
  if l['id'] in A2:
    lo,sc,sd,voc,cas,we=A2[l['id']]
    l['learningObjectives']=subs_items(LOS,lo); l['successCriteria']=subs_items(SC,sc)
    l['studyDesign']=sd; l['keyVocab']=voc
    if cas: l['cas']=cas
    if we: l['weDo']=we
# CFATs for Chapters 2-5: about 20 min, start of a lighter lesson after the content is taught. No CFATs in review lessons.
D2='1. Data Analysis\\\\CFATs\\\\Chapter '
def cf(i,t,cov,lid,plan,st='Planned',fn=None,src=None,marks=None):
  c=dict(id=i,title=t,covers=cov,format=FMT,status=st,plan=plan)
  if fn:c['file']=fn
  if src:c['sources']=src
  if marks:c['marks']=marks
  return lid,c
CF2=[cf('CFAT 1.2.1','Bivariate data and associations between categorical variables',['2A','2B'],'gm12-u3-l04','Start of the 2C lesson.','Written (11 Nov 2026)',D2+'2\\\\CFAT 1.2.1 [2A, 2B].docx',['Edrolo GM U3&4 2023 exercise questions (CFAT-only): 2A Q1b, Q2, Q5, Q8, Q12 · 2B Q3a, Q5, Q11, Q12 · 2C Q2b, Q2c'],14),
 cf('CFAT 1.2.2','Numerical vs categorical; scatterplots',['2C','2D'],'gm12-u3-l06','Start of the 2F lesson (one subchapter).','Written',D2+'2\\\\CFAT 1.2.2 [2C, 2D].docx'),
 cf('CFAT 1.2.3','Direction, form, strength, r, r² and causation',['2E','2F','2G','2H'],'gm12-u3-l09','Start of the 3A lesson (the Chapter 2 review lesson stays CFAT-free).'),
 cf('CFAT 1.3.1','Fitting and interpreting the least squares line',['3A','3B (slope, intercept, predictions, r²)'],'gm12-u3-l11','Start of the residuals and regression analysis lesson.'),
 cf('CFAT 1.3.2','Residuals and regression analysis',['3B (residuals, reporting)','3C'],'gm12-u3-l12','Start of the 4A lesson.'),
 cf('CFAT 1.4.1','Applying transformations',['4A','4B','4C'],'gm12-u3-l15','Start of the 4D lesson (one subchapter).'),
 cf('CFAT 1.4.2','Choosing and using a transformation',['4D'],'gm12-u3-l16','Start of the 5A lesson (features of time series plots, a lighter lesson).'),
 cf('CFAT 1.5.1','Time series and smoothing',['5A','5B','5C'],'gm12-u3-l20','Start of the first seasonal indices lesson.'),
 cf('CFAT 1.5.2','Seasonal indices and forecasting',['5D','5E'],'gm12-u3-l22','Last 20 min of the 5E lesson: the lessons after it are all review or SAC 1 preparation.')]
for lid,c in CF2:
  for l in L:
    if l['id']==lid: l.setdefault('cfats',[]).append(c)

ids={l['title']:l for l in L}
def when(t):l=ids[t];return dict(id=l['id'],week=l['week'],lesson=l['lesson'])
SD='VCE Mathematics Study Design 2023–2027'
d=dict(id='general-maths-12',name='Year 12 General Maths',unitLabel='Unit 3',
 scope='Unit 3 only · lesson order only (details to come) · step-up before summer, then Term 1 and Term 2 Weeks 1–11 · SAC sittings after school on Wednesdays',
 summary='Step-up 5 lessons · Term 1: 26 lessons · Term 2 Weeks 1–8: 24 lessons, Week 9 trial exams · Weeks 10–11 to be planned · 3 lessons a week (2 in Step-up week 1 and the Term 1 short week)',
 textbook='Cambridge Senior Mathematics General Mathematics VCE Units 3&4 (2nd ed.)',
 lessonsPerWeek=3,lessonMinutes=None,lessons=L,
 assessment=dict(rulesTitle=SD,
  rules=['Unit 3 School-assessed Coursework contributes 24 per cent to the study score (60 marks).',
   'Application task (Data analysis): 4–6 hours over 1–2 weeks. Outcome 1: 10, Outcome 2: 20, Outcome 3: 10 marks.',
   'Modelling or problem-solving task 1 (Recursion and financial modelling): 2–3 hours over 1 week. Outcome 1: 5, Outcome 2: 10, Outcome 3: 5 marks.',
   'Examinations 1 and 2 each contribute 30 per cent.',
   'School arrangement: SAC sittings run after school on Wednesdays (up to 100 minutes), so they do not use lesson time.'],
  suitableTasks=['Application task: a guided investigation of a given data set with several variables, with three components of increasing complexity: data plots (including smoothed plots for time series); summary statistics (including seasonal indices); modelling linear associations or trends (including data transformation).'],
  aos=[dict(aos='SAC 1',title='Application task: Data analysis',when=when('SAC 1 Part 2: in class (10 min reading + 60 min)'),outcome='Outcomes 1–3 (40 of 60 marks)',task='Guided investigation of a given multivariate data set, in three parts: Part 1 after school Wed 14 Apr (10 min reading + 90 min), Part 2 in class in Term 2 Week 1 (10 min reading + 60 min). No new content until Part 3 is done; Chapter 7 starts after it., Part 3 after school Wed 21 Apr (10 min reading + 90 min). Total 4 h 30 min (4 h working time) over 7 days.',taskType='Application task, 4–6 hours over 1–2 weeks',gaps=['Check lessons are at least 70 minutes long, for Part 2.','Part 2 must fall between the two Wednesday sittings (Thu 15 Apr – Tue 20 Apr).','Confirm the Wednesday dates against the school calendar.'],practice=[],actual=[],redemption=[],models=[]),
       dict(aos='SAC 2',title='Modelling or problem-solving task 1: Recursion and financial modelling',when=when('SAC 2 revision (Part 1, Wed 2 Jun after school)'),outcome='Outcomes 1–3 (20 of 60 marks)',task='Modelling or problem-solving task on recursion and financial modelling, in two parts after school: Part 1 Wed 2 Jun (Week 8), Part 2 Wed 9 Jun (Week 9, trial exam week). Feedback in Week 10. Keep the total at 2–3 hours, e.g. 2 × (10 min reading + 80 min).',taskType='Modelling or problem-solving task, 2–3 hours over 1 week',gaps=['Part 2 falls in trial exam week: confirm, or move it to Wed 16 Jun (Week 10).','Week 10 lessons are not planned yet (Unit 4 starts there); SAC 2 feedback needs a slot.','Two full 100-minute sittings would be 3 h 20 min, over the 3-hour maximum. Cap each sitting.','Confirm the Wednesday dates against the school calendar.'],practice=[],actual=[],redemption=[],models=[])],
  exams=[dict(name='Unit 3 trial exams',covers='Unit 3: Data analysis; Recursion and financial modelling',when='Term 2 Week 9 (trial exam week, no classes)',practice=[],actual=[])]))

# ---- APK (activating prior knowledge): Year 11 prerequisites ----
# CL = Cambridge General Mathematics VCE Units 1&2 (2nd ed.) chapter skills checklist item (section, #, skill).
# ED = Edrolo General Mathematics Units 1&2 exam practice question (lesson, Q, VCAA source).
CL={('2A',1):'Classify data as nominal, ordinal, discrete or continuous',('2B',5):'Interpret and describe a frequency table and bar chart',
 ('2A',2):'Construct a frequency table and a percentage frequency table',('2D',7):'Recognise symmetric, positively and negatively skewed distributions',
 ('2D',9):'Construct a stem plot from raw data',('2E',10):'Determine the median and mean as measures of centre',('2F',11):'Determine the quartiles and IQR',
 ('2F',12):'Find the standard deviation of a data set',('2G',13):'Use the 68–95–99.7% rule',('2H',14):'Produce a five-number summary and construct a boxplot',
 ('2H',15):'Determine the values of any outliers',('2I',16):'Compare distributions with a back-to-back stem plot or boxplot',
 ('7B',3):'Use a scatterplot to describe an association (direction, form, strength)',('7C',4):'Estimate and calculate the correlation coefficient r',
 ('7C',5):'Classify the strength of r',('7C',6):'Recognise that correlation does not imply causation',('7D',8):'Find the equation of the least squares line',
 ('7E',9):'Interpret the slope and intercept of a linear model',('7E',10):'Make predictions: interpolation and extrapolation',
 ('5A',1):'Substitute values into linear equations and formulas',('5E',7):'Find the slope of a line from two points',('5F',10):'Find the equation of a line from two points',
 ('5J',14):'Use piecewise linear graphs to model a practical situation',('9A',1):'Find k in direct variation',('9A',2):'Find k in inverse variation',
 ('9B',3):'Decide direct or inverse variation from a graph',('9C',4):'Use the squared transformation',('9C',5):'Use the reciprocal transformation',
 ('9D',6):'Evaluate logarithms',('9D',7):'State the order of magnitude of a number',('9D',10):'Use the log transformation',('9E',11):'Model non-linear data with a transformation',
 ('1A',2):'Convert decimals to percentages',('1B',6):'Increase or decrease a value by a percentage',('1D',11):'Express quantities as a ratio',('1F',14):'Use the unitary method'}
ED={('1A',13):'VCAA 2021 Exam 1 Q1',('1A',14):'VCAA 2020 Exam 1 Q10',('1C',15):'adapted from VCAA 2017 Exam 2 Q2b',('1C',16):'VCAA 2019 Exam 2 Q1b',('1C',17):'adapted from VCAA 2016 Exam 2 Q1d',
 ('1G',13):'adapted from VCAA 2017 Exam 2 Q1bi',('1E',12):'adapted from VCAA 2020 Exam 2 Q4aii',('1D',17):'adapted from VCAA 2020 Exam 2 Q3b',('1D',18):'VCAA 2017 Exam 2 Q1ai',('1D',19):'VCAA 2018 Exam 2 Q2a',('1E',11):'adapted from VCAA 2017 Exam 1 Q3',('1E',13):'adapted from VCAA 2021 Exam 2 Q1b',
 ('1F',16):'adapted from VCAA 2017 Exam 1 Q2',('1G',12):'adapted from VCAA 2019 Exam 1 Q6',('1G',14):'adapted from VCAA 2020 Exam 2 Q2bi',('1H',16):'VCAA 2019 Exam 2 Q2aii',('1H',17):'adapted from VCAA 2021 Exam 1 Q4',
 ('6A',14):'adapted from VCAA 2018 Exam 2 Q2b',('6A',15):'adapted from VCAA 2019 Exam 2 Q4a',('6A',16):'adapted from VCAA 2020 Exam 2 Q4bi',('6B',14):'adapted from VCAA 2016 Exam 2 Q3a',
 ('6B',15):'adapted from VCAA 2016 Exam 1 Q12',('6B',16):'adapted from VCAA 2020 Exam 2 Q6b',('6C',11):'adapted from VCAA 2017 Exam 2 Q4cii',('6C',12):'adapted from VCAA 2021 Exam 2 Q3eii',
 ('6D',12):'adapted from VCAA 2018 Exam 1 Q8',('6D',13):'adapted from VCAA 2019 Exam 2 Q5a',('6D',14):'adapted from VCAA 2017 Exam 1 Q8',('6D',15):'adapted from VCAA 2016 Exam 2 Q3bii',
 ('8D',14):'adapted from VCAA 2017 Exam 1 Q4',('9B',21):'adapted from VCAA 2019 Exam 1 Q9',('9B',22):'adapted from VCAA 2021 Exam 2 Q2a',('4D',13):'VCAA 2014 Exam 1 Q4',('4E',16):'VCAA 2016 Exam 1 Q2'}
APK={'gm12-u3-s1':([('2A',1),('2B',5)],[('1A',13),('1A',14)]),
 'gm12-u3-s2':([('2D',7),('2D',9),('9D',7)],[('1C',15),('1C',17)]),
 'gm12-u3-s3':([('2E',10),('2F',11)],[('1D',18)]),
 'gm12-u3-s4':([('2H',14),('2H',15)],[('1F',16)]),
 'gm12-u3-s5':([('2F',12),('2G',13)],[('1G',13),('1G',14)]),
 'gm12-u3-l03':([('2A',2),('1A',2)],[]),
 'gm12-u3-l04':([('2I',16),('2H',14)],[('1H',16),('1H',17)]),
 'gm12-u3-l05':([('7B',3)],[('6A',16)]),
 'gm12-u3-l06':([('7C',4),('7C',5)],[('6B',15)]),
 'gm12-u3-l07':([('7C',6),('7C',5)],[('6A',15)]),
 'gm12-u3-l09':([('7D',8),('5E',7)],[('6C',11),('6C',12)]),
 'gm12-u3-l10':([('7E',9),('7E',10)],[('6D',12),('6D',13)]),
 'gm12-u3-l11':([('7E',10),('5A',1)],[('6D',14),('6D',15)]),
 'gm12-u3-l12':([('9C',4),('9A',1)],[]),
 'gm12-u3-l13':([('9D',6),('9D',10)],[('8D',14)]),
 'gm12-u3-l14':([('9C',5),('9A',2)],[]),
 'gm12-u3-l15':([('9E',11),('9B',3)],[('9B',22)]),
 'gm12-u3-l16':([('7B',3),('5J',14)],[('9B',21)]),
 'gm12-u3-l17':([('2E',10)],[('1E',11)]),
 'gm12-u3-l18':([('2E',10)],[('1E',12)]),
 'gm12-u3-l19':([('2E',10)],[('1D',17)]),
 'gm12-u3-l20':([('1A',2),('1D',11)],[('1D',19)]),
 'gm12-u3-l21':([('1B',6),('1F',14)],[]),
 'gm12-u3-l22':([('5F',10),('7E',10)],[('4D',13),('4E',16)])}
for l in L:
    if l.get('id') in APK:
        cl,ed=APK[l['id']]
        l['apk']=[dict(kind='Skill',ref=f'Cambridge U1&2 {s} checklist #{n}',text=CL[(s,n)]) for s,n in cl]+\
                 [dict(kind='Exam',ref=f'Edrolo U1&2 {s} Q{n}',text=ED[(s,n)]) for s,n in ed]


# ---- Exit tasks: Edrolo General Mathematics Units 3&4 exam practice (VCAA) questions ----
import re as _re, csv as _c2
_EP={(r['edrolo_lesson'],int(r['q'])):_re.sub(r'\s*Data analysis','',r['source']) for r in _c2.DictReader(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'y12_edrolo_exam_practice.csv'),encoding='utf-8'))}
EXIT={'gm12-u3-s1':[('1A',14),('1A',16),('1B',13)],'gm12-u3-s2':[('1C',16),('1C',18),('1D',13)],
 'gm12-u3-s3':[('1G',11)],'gm12-u3-s4':[('1E',19),('1E',20)],'gm12-u3-s5':[('1H',12),('1I',13)],
 'gm12-u3-l03':[('2A',11),('2A',13)],'gm12-u3-l04':[('2B',11),('2B',12),('2B',13)],
 'gm12-u3-l05':[('2C',15),('2C',16)],'gm12-u3-l06':[('2C',17)],'gm12-u3-l07':[('2D',13),('2D',14)],
 'gm12-u3-l09':[('3A',13),('3A',14),('3A',15)],'gm12-u3-l10':[('3B',11),('3B',12),('3B',13)],
 'gm12-u3-l11':[('3C',11),('3C',13),('3C',14)],'gm12-u3-l13':[('3E',10),('3E',12)],
 'gm12-u3-l14':[('3E',11)],'gm12-u3-l15':[('3D',14),('3E',13)],
 'gm12-u3-l16':[('4A',11),('4A',12),('4A',13)],'gm12-u3-l17':[('4B',16),('4B',17)],
 'gm12-u3-l18':[('4B',15),('4B',18)],'gm12-u3-l19':[('4C',13),('4C',14),('4C',15)],
 'gm12-u3-l20':[('4D',19),('4D',17)],'gm12-u3-l21':[('4D',18)],'gm12-u3-l22':[('4E',12)]}
for l in L:
    if l.get('id') in EXIT:
        l['exit']=[dict(ref=f'Edrolo U3&4 {s} Q{n}',src=_EP[(s,n)]) for s,n in EXIT[l['id']]]


# ---- Do Now: current Study Design VCAA (2023-26 incl. NHT); built by tools/gm12/donow.py ----
_DN=json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'vcaa_donow_aos1.json'),encoding='utf-8'))
for l in L:
    k=(l.get('id') or '').replace('gm12-u3-','')
    if _DN.get(k):
        l['doNow']=[dict(exam=f"Exam {x['ex']}",ref=f"VCAA {x['paper']} Exam {x['ex']} {x['q']}",sec=x['sec']) for x in _DN[k]]


# ---- CFAT details: per-question breakdown (marks, skill, Study Design, Cambridge subchapter, success criterion) ----
# skill = own words. sc = success criterion copied from the lesson cards. fu = follow-up question for students who miss it (to find later).
import json as _json
_SD=_json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'sd.json'),encoding='utf-8'))
TY='Types of data'; SEG='Segmented bar charts'; HIS='Histograms'; LOG='Log scales'; STEM='Stem plots'
def q(n,m,typ,skill,sd,sub,sc,src,fu=''): return dict(q=n,marks=m,type=typ,skill=skill,sd=sd,sub=sub,sc=sc,src=src,fu=fu)
QMAP={
 'CFAT 1.1.1':[
  q(1,1,'MC','Classify two variables as nominal or ordinal',['DA-1.1','DA-K1'],'1A','I can identify types of data.','Edrolo 1A Q17'),
  q(2,1,'MC','Count the discrete variables in a list',['DA-1.1','DA-K1'],'1A','I can identify types of data.','Edrolo 1A Q15'),
  q(3,1,'MC','Read a percentage segmented bar chart and scale to a count',['DA-1.2','DA-K2','DA-S1'],'1B','I can describe the distribution of a categorical variable.','Edrolo 1B Q9'),
  q(4,1,'MC','Read frequencies from a histogram over an interval',['DA-1.3','DA-K2','DA-S3'],'1C','I can describe the features of a distribution from a histogram.','Edrolo 1C Q17'),
  q(5,1,'MC','Convert a value to log10 and find a percentage from a log histogram',['DA-1.3','DA-K3'],'1E','I can interpret a histogram with a log scale.','Edrolo 1D Q12'),
  q(6,1,'MC','Find the modal interval on a log histogram and convert back from log10',['DA-1.3','DA-K3'],'1E','I can interpret a histogram with a log scale.','Edrolo 1D Q14'),
  q('7a',2,'SA','Write a report on a categorical distribution, naming the mode',['DA-1.2','DA-1.4','DA-S1','DA-S2'],'1B','I can describe the distribution of a categorical variable.','Edrolo 1B Q8'),
  q('8a',1,'SA','Count values in an interval from a stem plot',['DA-1.3','DA-S3'],'1D','I can construct a stem plot.','Edrolo 1C Q6'),
  q('8b',1,'SA','Count values above a cut-off from a stem plot',['DA-1.3','DA-S4'],'1D','I can construct a stem plot.','Edrolo 1C Q6'),
  q('8c',1,'SA','Find the mode from a stem plot',['DA-1.3','DA-S3'],'1D','I can construct a stem plot.','Edrolo 1C Q6'),
  q('9a',1,'SA','Convert a log10 value back to the actual value',['DA-1.3','DA-K3'],'1E','I can use a CAS calculator to find logs.','Edrolo 1D Q9'),
  q('9b',1,'SA','Find the log10 interval a value is plotted in',['DA-1.3','DA-K3'],'1E','I can interpret a histogram with a log scale.','Edrolo 1D Q9')],
 'CFAT 1.1.2':[
  q(1,1,'MC','Find Q3 of an unordered data set',['DA-1.5','DA-K4','DA-S3'],'1F','I can find the median value in a data set.','Edrolo 1E Q1'),
  q(2,1,'MC','Find the IQR from a stem plot (n odd)',['DA-1.5','DA-K4','DA-S3'],'1F','I can find the IQR from a stem plot when n is odd.','Edrolo 1E Q17'),
  q(3,1,'MC','Calculate the lower fence from a five-number summary',['DA-1.5','DA-K4'],'1G','I can use boxplots to describe a distribution with outliers.','Edrolo 1E Q8'),
  q(4,1,'MC','Read the five-number summary from a boxplot',['DA-1.5','DA-K4'],'1G','I can read values from a boxplot.','Edrolo 1E Q11'),
  q(5,1,'MC','Decide shape and outliers from a five-number summary',['DA-1.5','DA-K4','DA-S3'],'1G','I can use boxplots to describe a distribution with outliers.','Edrolo 1F Q19'),
  q(6,1,'MC','Describe the features of a negatively skewed boxplot',['DA-1.5','DA-S3'],'1G','I can use boxplots for describe a distribution without outliers.','Edrolo 1F Q12'),
  q('7a',1,'SA','Calculate the upper fence from a boxplot',['DA-1.5','DA-K4'],'1G','I can read values from a boxplot.','Edrolo 1E Q18'),
  q('7b',1,'SA','Describe and compare the shapes of two boxplots, including outliers',['DA-1.5','DA-S3','DA-S4'],'1G','I can use boxplots to describe a distribution with outliers.','Edrolo 1E Q18'),
  q('8a',1,'SA','Find the five-number summary from raw data (CAS)',['DA-1.5','DA-K4','DA-S3'],'1G','I can construct a boxplot with outliers from data using the CAS calculator.','Edrolo 1E Q14'),
  q('8b',1,'SA','Calculate the IQR',['DA-1.5','DA-K4'],'1F','I can find the median value in a data set.','Edrolo 1E Q14'),
  q('8c',1,'SA','Use the fences to identify outliers, with working',['DA-1.5','DA-K4'],'1G','I can construct a boxplot with outliers from data using the CAS calculator.','Edrolo 1E Q14'),
  q('8d',1,'SA','Draw a boxplot with an outlier on a given scale',['DA-1.5','DA-S3'],'1G','I can construct a boxplot from a five number summary.','Edrolo 1E Q14'),
  q('9a',1,'SA','Describe the shape of a distribution from a stem plot',['DA-1.3','DA-S3'],'1C','I can describe the features of a distribution from a histogram.','Edrolo 1F Q18'),
  q('9b',1,'SA','Find the median from a stem plot (n even)',['DA-1.5','DA-S3'],'1F','I can find the median value from a stem plot.','Edrolo 1F Q18')],
 'CFAT 1.1.3':[
  q(1,1,'MC','Find the mean and sample SD of raw data (CAS)',['DA-1.5','DA-K5'],'1F','I can calculate the mean and standard deviation using the CAS calculator.','Edrolo 1G Q4'),
  q(2,1,'MC','Interpret a negative z-score',['DA-1.6','DA-K6'],'1H','I can calculate standardised scores.','Edrolo 1I Q1'),
  q(3,1,'MC','Know that z = 0 is the mean',['DA-1.6','DA-K6'],'1H','I can convert standardised scores into actual scores.','Edrolo 1I Q4'),
  q(4,1,'MC','Use the 68–95–99.7% rule across two intervals',['DA-1.6','DA-K6','DA-S5'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q11'),
  q(5,1,'MC','Convert a z-score to an actual score',['DA-1.6','DA-K6','DA-S5'],'1H','I can convert standardised scores into actual scores.','Edrolo 1I Q12'),
  q(6,1,'MC','Calculate a z-score with a negative value',['DA-1.6','DA-K6','DA-S5'],'1H','I can calculate standardised scores.','Edrolo 1I Q15'),
  q('7a',1,'SA','68–95–99.7% rule: percentage above one SD below the mean',['DA-1.6','DA-S5'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q13'),
  q('7b',1,'SA','68–95–99.7% rule: turn a percentage into a count',['DA-1.6','DA-S5'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q13'),
  q('8a',1,'SA','Label the normal curve: values and percentages',['DA-1.6','DA-K6'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q8'),
  q('8b',1,'SA','Percentage between the mean and one SD below',['DA-1.6','DA-S5'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q8'),
  q('8c',1,'SA','Percentage between two and three SDs below',['DA-1.6','DA-S5'],'1H','I can apply the 68-95-99.7% rule.','Edrolo 1H Q8'),
  q('8d',1,'SA','Turn a tail percentage into a count',['DA-1.6','DA-S5'],'1H','I can use standard scores to determine percentages.','Edrolo 1H Q8'),
  q('8e',1,'SA','Find the value that cuts off the bottom 2.5%',['DA-1.6','DA-S5'],'1H','I can convert standardised scores into actual scores.','Edrolo 1H Q8'),
  q('9a',1,'SA','Calculate z-scores for three distributions',['DA-1.6','DA-K6','DA-S5'],'1H','I can calculate standardised scores.','Edrolo 1I Q9'),
  q('9b',1,'SA','Use z-scores to compare performance (lower time is better)',['DA-1.6','DA-S5'],'1H','I can use standardised scores to make comparisons.','Edrolo 1I Q9')],
}
for l in L:
    for c in l.get('cfats',[]):
        Q=QMAP.get(c['id'])
        if not Q: continue
        c['questions']=Q
        c['marks']=sum(x['marks'] for x in Q)
        c['mcMarks']=sum(x['marks'] for x in Q if x['type']=='MC'); c['saMarks']=c['marks']-c['mcMarks']
        subs={}
        for x in Q: subs.setdefault(x['sub'],[0,[]]); subs[x['sub']][0]+=x['marks']; (x['sc'] in subs[x['sub']][1]) or subs[x['sub']][1].append(x['sc'])
        c['bySub']=[dict(sub=k,marks=v[0],sc=v[1]) for k,v in sorted(subs.items())]
        codes={}
        for x in Q:
            for k in x['sd']: codes.setdefault(k,[0,[]]); codes[k][0]+=x['marks']; codes[k][1].append(str(x['q']))
        order=lambda k:(0 if k[3].isdigit() else 1 if k[3]=='K' else 2, float(k.split('-')[1].lstrip('KS')))
        c['bySd']=[dict(code=k,text=_SD.get(k,''),marks=v[0],qs=v[1]) for k,v in sorted(codes.items(),key=lambda kv:order(kv[0]))]
        c['status']='Ready (14 Nov 2026): worksheet house style, on the dashboard'
        c['file']=dict(zip(['CFAT 1.1.1','CFAT 1.1.2','CFAT 1.1.3'],['lessons/gm12/CFAT-1.1.1.html','lessons/gm12/CFAT-1.1.2.html','lessons/gm12/CFAT-1.1.3.html']))[c['id']]


# Guard: an exit task must never repeat a CFAT question (CFAT items come from QMAP sources).
import re as _re2
_CF_ITEMS={(m.group(1),int(m.group(2))) for qs in QMAP.values() for x in qs for m in [_re2.match(r'Edrolo (\w+) Q(\d+)',x['src'])] if m}
for _lid,_qs in EXIT.items():
    _bad=[q for q in _qs if q in _CF_ITEMS]
    assert not _bad, f'Exit tasks for {_lid} repeat CFAT questions: {_bad}'

# ---- Lesson materials (placeholders; status 'todo' | 'draft' | 'ready'; file = path when made) ----
MAT_KINDS=[('Guided slides','Teach the new content and project every question: Do Now, APK, worked examples, you trys, exit tasks.'),
           ('Guided worksheet','Student companion to the slides, in the same order, with space to answer. Max 2 double-sided pages.'),
           ('Bound reference entry','One A4 sheet: key ideas, key formulas, simple how-tos and examples.')]
MAT_LESSONS=['gm12-u3-s1','gm12-u3-s2','gm12-u3-s3','gm12-u3-s4','gm12-u3-s5']
for l in L:
    if l.get('id') in MAT_LESSONS:
        l['materials']=[dict(kind=k,desc=d,status='todo',file='') for k,d in MAT_KINDS]
# CFAT as a lesson resource (lesson id -> CFAT code); same status/file system as the other materials.
CFAT_LESSONS={'gm12-u3-s3':['1.1.1'],'gm12-u3-s5':['1.1.2'],'gm12-u3-holiday':['1.1.3']}
HOL_KINDS=[('Holiday revision pack','Chapter 1 revision over summer, so students come back ready for the Chapter 1 coursework check + test.')]
for l in L:
    if l.get('id')=='gm12-u3-holiday': l['materials']=[dict(kind=k,desc=d,status='todo',file='') for k,d in HOL_KINDS]
for l in L:
    if l.get('id') in CFAT_LESSONS:
        for code in CFAT_LESSONS[l['id']]: l['materials'].append(dict(kind=f'CFAT {code}',desc=f"CFAT {code}: student copy, worksheet style. Solutions by hand.",status='todo',file=''))
# Chapter-end lessons: materials = coursework check (double-sided A4) + chapter test.
TEST_KINDS=[('Coursework check','Double-sided A4. Front: students tick the coursework they have (guided notes, bound reference entries, CFATs, homework); teacher signs off. Back: chapter success criteria, ticked by the teacher when marking the test (Test Q column = which question tests it).'),
            ('Chapter test','Formal chapter test. Each question maps to the success criteria on the back of the coursework check.')]
for l in L:
    if l['title'].endswith('coursework check + test'):
        l['materials']=[dict(kind=k,desc=d,status='todo',file='') for k,d in TEST_KINDS]
# Made materials: (lesson id, kind) -> (status, html file, pdf file), paths relative to the site root.
MAT_FILES={
    ('gm12-u3-s1','Guided slides'):('ready','lessons/gm12/S1-slides.html','lessons/gm12/S1-slides.pdf'),
    ('gm12-u3-s1','Guided worksheet'):('draft','lessons/gm12/S1-worksheet.html','lessons/gm12/S1-worksheet.pdf'),
    ('gm12-u3-s2','Guided slides'):('draft','lessons/gm12/S2-slides.html','lessons/gm12/S2-slides.pdf'),
    ('gm12-u3-s3','Guided slides'):('draft','lessons/gm12/S3-slides.html','lessons/gm12/S3-slides.pdf'),
    ('gm12-u3-ch1-test','Coursework check'):('draft','lessons/gm12/Ch1-coursework-check.html','lessons/gm12/Ch1-coursework-check.pdf'),
    ('gm12-u3-s3','CFAT 1.1.1'):('ready','lessons/gm12/CFAT-1.1.1.html','lessons/gm12/CFAT-1.1.1.pdf'),
    ('gm12-u3-s5','CFAT 1.1.2'):('ready','lessons/gm12/CFAT-1.1.2.html','lessons/gm12/CFAT-1.1.2.pdf'),
    ('gm12-u3-holiday','CFAT 1.1.3'):('ready','lessons/gm12/CFAT-1.1.3.html','lessons/gm12/CFAT-1.1.3.pdf'),
}
for l in L:
    for m in l.get('materials',[]):
        f=MAT_FILES.get((l.get('id'),m['kind']))
        if f: m['status'],m['file'],m['pdf']=f

json.dump(d,open('classes/general-maths-12.json','w'),ensure_ascii=False,indent=1)
print(len(L),'entries')
