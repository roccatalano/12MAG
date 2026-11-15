"""CONTENT for CFAT 1.5.1 (Cambridge 5A-5C: time series plots, moving means, moving medians) and
CFAT 1.5.2 (Cambridge 5D-5E: seasonal indices, deseasonalising, forecasting). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no VCAA reprints / exam practice). Edrolo calls the chapter 4
(time series = Cambridge Ch 5). Wording copied verbatim from Edrolo 4A-4E (PDF pp. 236-237, 253, 255, 268, 271,
281-282, 284, 293-295 = printed 229-230, 246, 248, 261, 264, 273-274, 277, 286-288); answers from the Edrolo
answer pages (PDF pp. 687-694 = printed 680-687), checked by hand. Figures cropped by crop.py from the Edrolo PDF
(pp. 236, 237, 268, 271). Marks for parts set by Claude (Edrolo prints none).

CFAT 1.5.1 (14 marks, start of the first seasonal indices lesson l20): MC Edrolo 4A Q1, 4A Q5, 4B Q1, 4B Q6, 4C Q1, 4C Q9;
  SA 4A Q6a-b, 4B Q2a-b, 4C Q10a-d.
CFAT 1.5.2 (17 marks, last 20 min of the 5E lesson l22): MC Edrolo 4D Q1, 4D Q3, 4D Q5, 4D Q6, 4D Q10, 4E Q6;
  SA 4D Q2a-b, 4D Q15a-c, 4E Q4a-c, 4E Q7.
Not used (plot-drawing answers, whole-series tables or long): 4A Q2-4, Q7-10; 4B Q3-5, Q7-14 (Q7 left out so the CFAT fits on 2 pages); 4C Q2-8, Q11-12;
  4D Q4, Q7-9, Q11-14, Q16; 4E Q1-3, Q5, Q8-11.

Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

CFATS = [
 dict(id='CFAT 1.5.1', subs='5A-5C', title='Time series plots and smoothing',
  layout=[([0],[1]),([2],[3]),([4],[5])],
  mc=[
   dict(src='Edrolo 4A Q1', stem='Consider the following time series showing the number of tickets sold to Melbourne Zoo’s hippopotamus show ‘Hypnotic Hippos’ each month this year. The month data has been represented by a time code, so that January is 1, February is 2, etc.\nHow many tickets were sold in June?',
        fig='4A_Q1', w=4.6, opts=['320 tickets','345 tickets','550 tickets','910 tickets'], ans=2),
   dict(src='Edrolo 4A Q5', stem='Identify which one of the following features is present in the time series plot.',
        fig='4A_Q5', w=5.0, opts=['Structural change','Outlier','Seasonality','A decreasing trend'], ans=0),
   dict(src='Edrolo 4B Q1', stem='Consider the following table.',
        table=[['month','1','2','3','4','5','6'],['value','75','83','104','97','71','64']],
        stem2='The three-mean smoothed value for month 4 is closest to', opts=['91','92','93','94'], ans=0),
   dict(src='Edrolo 4B Q6', stem='Consider the following table.',
        table=[['year','2016','2017','2018','2019','2020','2021','2022'],['sales','203','226','241','188','203','261','250']],
        stem2='The two-mean smoothed sales for 2020 is closest to', opts=['214','217','224','232'], ans=0),
   dict(src='Edrolo 4C Q1', stem='Consider the following time series.\nThe three-median smoothed time spent on homework for Friday is',
        fig='4C_Q1', w=6.0, opts=['20 minutes','35 minutes','45 minutes','80 minutes'], ans=1),
   dict(src='Edrolo 4C Q9', stem='Jae is a small business owner. She recorded her daily income over the 28 days of February. Jae then smoothed the data using moving median smoothing in order to see any underlying trends. The smoothed data consisted of 22 smoothed data values.\nThe smoothing Jae has used is',
        opts=['three-moving median smoothing.','five-moving median smoothing.','seven-moving median smoothing.','nine-moving median smoothing.'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 4A Q6', stem='Identify two features that are present in each of the following time series plots.',
        parts=[('a.','',1,'Increasing trend including an outlier','4A_Q6a',4.4),
               ('b.','',1,'Seasonality and structural change','4A_Q6b',4.4)]),
   dict(src='Edrolo 4B Q2', stem='Alexia recorded the time taken, in minutes, to travel to school over a period of two weeks. She displayed the data in the following table.',
        table=[['day','Mon 1st Oct','Tue 2nd Oct','Wed 3rd Oct','Thu 4th Oct','Fri 5th Oct','Mon 8th Oct','Tue 9th Oct','Wed 10th Oct','Thu 11th Oct','Fri 12th Oct'],
               ['time taken (mins)','37','33','44','40','45','31','38','41','37','50']],
        parts=[('a.','Calculate the three-mean smoothed time taken for Tuesday 2nd October.',1,'(37 + 33 + 44) ÷ 3 = 38 minutes'),
               ('b.','Calculate the five-mean smoothed time taken for Wednesday 10th October.',1,'(31 + 38 + 41 + 37 + 50) ÷ 5 = 39.4 minutes')]),
   dict(src='Edrolo 4C Q10', stem='The daily snowfall (mm) on Mount Buller was recorded over a two-week period. The results are shown in the following time series plot.',
        fig='4C_Q10', w=6.4,
        parts=[('a.','Using three-median smoothing, find the smoothed daily snowfall for day 4.',1,'days 3–5: 22, 21, 25 → median 22 mm'),
               ('b.','Using five-median smoothing, find the smoothed daily snowfall for day 7.',1,'days 5–9: 25, 17, 15, 18, 21 → median 18 mm'),
               ('c.','Using seven-median smoothing, find the smoothed daily snowfall for day 11.',1,'days 8–14: 18, 21, 14, 23, 22, 20, 17 → median 20 mm'),
               ('d.','Using nine-median smoothing, find the smoothed daily snowfall for day 8.',1,'days 4–12: 21, 25, 17, 15, 18, 21, 14, 23, 22 → median 21 mm')]),
  ]),
 dict(id='CFAT 1.5.2', subs='5D-5E', title='Seasonal indices and forecasting',
  layout=[([0],[1]),([2],[3]),([4],[5])],
  mc=[
   dict(src='Edrolo 4D Q1', stem='The seasonal index for sales in June is 0.73.\nWhich statement is correct?',
        opts=['On average, sales in June are 73% less than the monthly average.','On average, sales in June are 27% less than the monthly average.','On average, sales in June are 27% more than the monthly average.','On average, sales in June are 73% more than the monthly average.'], ans=1),
   dict(src='Edrolo 4D Q3', stem='Consider the following table.',
        table=[['','summer','autumn','winter','spring'],['seasonal index','0.65','1.15','','0.80']],
        stem2='What is the seasonal index for winter?', opts=['0.87','1.20','1.25','1.40'], ans=3),
   dict(src='Edrolo 4D Q5', stem='Consider the following table.',
        table=[['','Mon','Tue','Wed','Thu','Fri','Sat','Sun'],['seasonal index','0.87','0.94','0.91','0.85','0.96','1.26','1.21'],['value','603','665','509','670','702','931','950']],
        stem2='The deseasonalised value for Thursday is closest to', opts=['570','583','771','788'], ans=3),
   dict(src='Edrolo 4D Q6', stem='The number of weddings held in the Botanical Gardens is seasonal, with the number of weddings in spring having a seasonal index of 1.32. If there were 58 weddings held in the Botanical Gardens this spring, the deseasonalised number of weddings is closest to',
        opts=['39','43','44','77'], ans=2),
   dict(src='Edrolo 4D Q10', stem='The deseasonalised value for a particular season is 927. If the seasonal index is 0.75, the actual value is closest to',
        opts=['695','864','927','1236'], ans=0),
   dict(src='Edrolo 4E Q6', stem='A regression equation has predicted the deseasonalised value in September to be 3750. If September has a long-term seasonal index of 1.09, the actual predicted value for September is closest to',
        opts=['3413','3440','4088','4121'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 4D Q2', stem='The quarterly sales ($000’s) of a canine clothing shop are displayed in the following table.',
        table=[['','quarter 1','quarter 2','quarter 3','quarter 4'],['sales ($000’s)','33.5','61.3','52.0','43.4']],
        parts=[('a.','Calculate the seasonal index for quarter 1, correct to two decimal places.',1,'mean = (33.5 + 61.3 + 52.0 + 43.4) ÷ 4 = 47.55\nSI = 33.5 ÷ 47.55 = 0.70'),
               ('b.','What does the rounded seasonal index for quarter 1 mean in terms of the amount of sales in quarter 1 compared to the average quarter?',1,'On average, sales in quarter 1 are 70% of, or 30% less than, the average quarter.')]),
   dict(src='Edrolo 4D Q15', stem='The sales ($000’s) for a churro company are seasonal, with the sales for 2020, 2021, and 2022 shown in the following table. The season index for autumn is 1.06 and the seasonal index for winter is 1.32.',
        table=[['year','summer','autumn','winter','spring'],['2020','2050','3650','4300','3125'],['2021','1900','3075','4150','3300'],['2022','1625','3300','4050','3250']],
        parts=[('a.','Calculate the average seasonal indices of sales for summer and spring. Give values correct to two decimal places.',2,'summer: 0.59, spring: 1.03\n(SI for each year = value ÷ that year’s mean, then average the three years)'),
               ('b.','What does the seasonal index for autumn tell us about the amount of sales in autumn compared to the average season?',1,'On average, sales in autumn are 6% greater than the average season.'),
               ('c.','Fill in the gap in the following sentence, giving the value correct to the nearest percent.\nTo correct for seasonality, the amount of sales in winter should be decreased by ____%.',1,'1 ÷ 1.32 = 0.758 → decreased by 24%')]),
   dict(src='Edrolo 4E Q4', stem='Leonard conducted research into the number of alien sightings from 1975 to 2015 in the northern and southern hemispheres. He then used this data to construct regression equations to predict the number of alien sightings in each hemisphere for any given year.\nNote: Leonard has used year = 0 to represent 1975.\nThe least squares regression equations are:\nSouthern hemisphere: alien sightings = 208 + 23.4 × year\nNorthern hemisphere: alien sightings = 361 + 41.2 × year',
        parts=[('a.','Estimate the difference between the number of alien sightings in each hemisphere in the year 2030, correct to the nearest whole number.',1,'year = 55: N = 361 + 41.2 × 55 = 2627, S = 208 + 23.4 × 55 = 1495\ndifference = 1132 alien sightings'),
               ('b.','Explain why this prediction may be of limited reliability, even if Leonard’s original data was correct.',1,'The prediction is an example of extrapolation since it is outside the range of recorded data.'),
               ('c.','Interpret the slope of the regression line in terms of the change in the number of alien sightings in the northern hemisphere each year.',1,'On average, the number of alien sightings in the northern hemisphere increases by 41.2 each year.')]),
   dict(src='Edrolo 4E Q7', stem='The following equation can be used to forecast the deseasonalised sales ($) of a small business.\ndeseasonalised sales = 20 005 + 15 000 × quarter number\nquarter number = 1 in quarter 1 of 2014 and quarter number = 2 in quarter 2 of 2014.\nThe seasonal index for the third quarter of each year is 0.65.',
        parts=[('','What is the actual value of sales in the third quarter of 2015?',2,'quarter number = 7: deseasonalised sales = 20 005 + 15 000 × 7 = 125 005\nactual = 125 005 × 0.65 = $81 253.25')]),
  ]),
]
