"""CONTENT for CFAT 1.3.1 (Cambridge 3A-3B: fitting and interpreting the least squares line) and
CFAT 1.3.2 (Cambridge 3B-3C: residuals and regression analysis). Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no VCAA reprints / exam practice). Wording copied verbatim
from Edrolo (PDF pp. 170-173, 180-182, 194-196); answers from the Edrolo answer pages (PDF pp. 676-680 =
printed 669-673). Figures cropped by crop.py from the Edrolo PDF (pp. 171, 181, 195). Edrolo 3C Q1-2 are
already burnt (CFAT 1.2.3). Marks for parts set by Claude (Edrolo prints none).

CFAT 1.3.1 (15 marks): MC Edrolo 3A Q1, 3A Q2, 3A Q6, 3B Q1, 3B Q4; SA 3A Q3, 3A Q8, 3B Q2a-b, 3B Q7a-d.
CFAT 1.3.2 (15 marks): MC Edrolo 3A Q11, 3A Q4, 3C Q3; SA 3C Q4a-b, 3C Q6a-c, 3C Q8a-c.
Note: 3C Q4b answer is Edrolo's (57.26, -3.26: unrounded coefficients); with the rounded equation it is 57.20, -3.20.

Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

CFATS = [
 dict(id='CFAT 1.3.1', subs='3A-3B', title='Fitting and interpreting the least squares regression line',
  layout=[([0],[1]),([2],[3]),('full',4)],
  mc=[
   dict(src='Edrolo 3A Q1', stem='Consider the following table.',
        table=[['number of beaches','1','3','4','4','4','5','5','7','7','8'],['number of surf shops','2','3','4','18','5','6','6','7','9','10']],
        stem2='A least squares regression line would not be appropriate for this data because',
        opts=['the data is categorical.','there are not enough data points.','both variables are numerical.','there is a clear outlier.'], ans=3),
   dict(src='Edrolo 3A Q2', stem='Consider the following table.',
        table=[['number of shops','8','12','15','19','20','21','25','27','30','34'],['population (000’s)','4.7','6.9','8.4','7.8','10.8','8.1','13.0','11.6','19.0','16.2']],
        stem2='A least squares line is fitted to the data, with the aim of predicting population from number of shops.\nWhich of the following statements is true?',
        opts=['a = 0.91 and b = 0.82','a = 0.49 and b = 0.24','a = 0.24 and b = 0.49','a = 0.82 and b = 0.91'], ans=2),
   dict(src='Edrolo 3A Q6', stem='Consider the following summary statistics for a set of bivariate data involving the variables x and y.\nr = −0.96, x̄ = 15.3, ȳ = 43.8, s_x = 12.2, s_y = 13.0\nThe equation of the least squares regression line that allows y to be predicted from x, with values given correct to 3 significant figures, is closest to',
        opts=['y = 59.5 + 1.02x','y = 1.02 + 59.5x','y = 59.5 − 1.02x','y = 1.02 − 59.5x'], ans=2),
   dict(src='Edrolo 3B Q1', stem='The following regression equation shows the relationship between the number of bedrooms and price ($000’s) of houses in Melbourne:\nprice = 593.2 + 98.4 × number of bedrooms\nBy how much, on average, do house prices increase as the number of bedrooms increases?',
        opts=['$98.40','$593.20','$98 400.00','$593 200.00'], ans=2),
   dict(src='Edrolo 3B Q4', stem='The relationship between the daily maximum temperature (°C) and the daily minimum temperature (°C) is given by the following least squares regression line:\nmaximum temperature = 10.42 + 0.89 × minimum temperature\nWhat is the expected maximum temperature on Tuesday if the minimum temperature is 18 °C?',
        opts=['16.02 °C','25.29 °C','26.44 °C','28.42 °C'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 3A Q3', stem='A group of students were asked how many hours they had slept the night before a General Mathematics exam.\nTheir number of hours slept and result (%) are shown in the table.',
        table=[['number of hours slept','7.2','7.8','8.3','5.3','6','9','2.3','6.8','7.7','8','8.6','9.2'],['result (%)','88','79','83','67','70','92','56','74','63','84','98','85']],
        parts=[('','A least squares regression line has been fitted to the data to predict result, from number of hours slept.\nWrite the equation of the regression line, giving values correct to three decimal places.',2,'result = 41.250 + 5.151 × number of hours slept  (1 mark intercept, 1 mark slope)')]),
   dict(src='Edrolo 3A Q8', stem='Joe the farmer wants to investigate the relationship between time (days) and the height (cm) of his growing wheat crops. Joe hires a data analyst, who is able to provide certain statistics based on the data gathered from a patch of growing wheat crops.\nx̄ = 55.0, ȳ = 63.8, s_x = 30.3, s_y = 37.4, r = 0.99',
        parts=[('','Joe wants to model a least squares regression line to his data, so that he can predict the height of any given wheat plant based on the amount of time that has passed. Determine the equation of this line, giving values correct to one decimal place.',2,'b = 0.99 × 37.4 ÷ 30.3 = 1.2;  a = 63.8 − 1.22… × 55.0 = −3.4\nheight = −3.4 + 1.2 × time  (1 mark each)')]),
   dict(src='Edrolo 3B Q2', stem='The price ($) of a second-hand car depends on its age (years).\nAn approximate relationship between the car’s price and age is given in the following equation.\nprice = 24 000 − 3500 × age',
        parts=[('a.','What was the price of the car when it was brand new?',1,'$24 000'),
               ('b.','By how much does the car’s value decrease each year?',1,'$3500')]),
   dict(src='Edrolo 3B Q7', stem='The manager of a swimming pool investigated the effect that the temperature has on attendance at his pool. He recorded the weather and the number of people that attended the pool for two weeks.\nThe results are displayed in the scatterplot.\nThe regression equation that allows attendance to be predicted from temperature (°C) is as follows.\nattendance = −88.53 + 5.7 × temperature',
        fig='3B_Q7', w=7.2,
        parts=[('a.','Use the regression equation to predict the number of people that will attend the pool if the temperature is 31 °C. Round to the nearest whole number.',1,'88 people'),
               ('b.','Is the prediction from part a reliable? Explain briefly.',1,'Yes, the prediction is reliable because it is an example of interpolation.'),
               ('c.','Use the regression equation to predict the number of people that will attend the pool if the temperature is 16 °C. Round to the nearest whole number.',1,'3 people'),
               ('d.','Is the prediction from part c reliable? Explain briefly.',1,'No, it may not be reliable because the prediction is an example of extrapolation.')]),
  ]),
 dict(id='CFAT 1.3.2', subs='3B-3C', title='Residuals, residual plots and regression analysis',
  layout=[([0],[1]),('full',2)],
  mc=[
   dict(src='Edrolo 3A Q11', stem='Which of the following statements regarding the least squares regression line is false?',
        opts=['A least squares regression line minimises the sum of the squares of the residuals.','A least squares regression line is not appropriate if there is a clear outlier.','A least squares regression line is generally written in the form y = a + bx.','A least squares regression line can be fitted to the variables day of the week and hours spent watching TV.'], ans=3),
   dict(src='Edrolo 3A Q4', stem='The least squares line fitted to the scatterplot shown is of the form y = a + bx.\nWhich of the following statements is false?',
        fig='3A_Q4', w=4.6, opts=['The value of a is positive.','The value of b is positive.','x is the explanatory variable.','y is the response variable.'], ans=1),
   dict(src='Edrolo 3C Q3', stem='Rachel’s Health and Human Development class is studying the average growth in the height of children and young teenagers. They determine the following least squares regression equation, which can be used to predict height (cm) from age (years).\nheight = 47.32 + 7.13 × age\nRachel is 14 years old and 152 cm tall. What is the residual value when her height is predicted from the least squares regression equation, correct to two decimal places?',
        opts=['−4.86','0.68','4.86','152.00'], ans=2),
  ],
  sa=[
   dict(src='Edrolo 3C Q4', stem='A group of scientists collected the IQ of 5 participants. The scientists then determined a least squares regression equation that can be used to predict test score on a particular intelligence test from IQ. The predicted test scores were calculated and recorded.\nThe participants then completed the intelligence test and the scientists recorded their actual test scores, before calculating the residual values of each participant. However, they lost the predicted test score and residual value for the participant with an IQ of 91.',
        table=[['IQ','101','87','94','106','91'],['actual test score (%)','76','54','60','80','54'],['predicted test score (%)','72.90','50.92','61.91','80.75',''],['residual value (%)','3.10','3.08','−1.91','−0.75','']],
        parts=[('a.','Find the regression equation used by the scientists. Round values to two decimal places.',2,'predicted test score = −85.67 + 1.57 × IQ  (fit IQ against predicted test score)'),
               ('b.','Use the regression equation from part a to find the predicted test score and residual value for the participant with an IQ of 91.',2,'predicted test score = 57.26, residual = −3.26  (Edrolo; 57.20 and −3.20 from the rounded equation also accepted)')]),
   dict(src='Edrolo 3C Q6', stem='For each of the following residual plots, determine whether the assumption of linearity is supported.',
        parts=[('a.','',1,'The residual plot does not support the assumption of linearity.','3C_Q6a',5.6),
               ('b.','',1,'The residual plot supports the assumption of linearity.','3C_Q6b',5.6),
               ('c.','',1,'The residual plot does not support the assumption of linearity.','3C_Q6c',5.6)]),
   dict(src='Edrolo 3C Q8', stem='A Year 10 Maths class recently completed a statistics test and a calculus test. Six students recorded their results from both tests. They are displayed in the following table.',
        table=[['','Sophie','Isaac','Mayu','Deanne','Selby','Emily'],['statistics test result (%)','75','61','88','43','94','64'],['calculus test result (%)','64','53','95','40','92','59']],
        stem2='The students calculated the following least squares regression equation that could predict a calculus test result from a statistics test result.\ncalculus test result = −12.66 + 1.13 × statistics test result',
        parts=[('a.','Use the least squares regression equation to determine each student’s predicted calculus test result (%), correct to one decimal place.',2,'Sophie 72.1, Isaac 56.3, Mayu 86.8, Deanne 35.9, Selby 93.6, Emily 59.7'),
               ('b.','Using the rounded answers from part a, calculate the residual values when the calculus test result (%) is predicted from the least squares regression equation. Give values correct to one decimal place.',2,'Sophie −8.1, Isaac −3.3, Mayu 8.2, Deanne 4.1, Selby −1.6, Emily −0.7'),
               ('c.','Which student(s) didn’t perform as well as was predicted on the calculus test?',1,'Sophie, Isaac, Selby and Emily (negative residuals)')]),
  ]),
]
