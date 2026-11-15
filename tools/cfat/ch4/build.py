"""CONTENT for CFAT 1.4.1 (Cambridge 4A-4B: squared and log transformations) and
CFAT 1.4.2 (Cambridge 4C-4D: reciprocal transformation, choosing and applying a transformation).
Output: build_html.py (HTML + PDF).

Rule 8: Edrolo U3&4 (2023) exercise questions ONLY (no VCAA reprints / exam practice). Wording copied verbatim
from Edrolo 3D/3E (PDF pp. 207-210, 222-223 = printed 200-203, 215-216); answers from the Edrolo answer pages
(PDF pp. 681-684 = printed 674-677), checked by regression in Python. Figures cropped by crop.py from the Edrolo
PDF (pp. 207, 208, 223). Marks for parts set by Claude (Edrolo prints none). 3D Q3 a-c are three MC items.

CFAT 1.4.1 (11 marks, start of the 4C lesson l14): MC Edrolo 3D Q4, 3E Q1, 3D Q7, 3E Q6; SA 3D Q2a-b, 3E Q7a-b, 3E Q2.
CFAT 1.4.2 (16 marks, start of the 5A lesson l16): MC Edrolo 3D Q10, 3E Q5, 3D Q1, 3D Q3a-c; SA 3E Q3, 3E Q8a-b, 3E Q4a-c.
Not used (graph-plotting answers or very long): 3D Q5, Q6, Q8, Q9, Q11, Q12, Q13; 3E Q9.

Run: python3 build_html.py <lessons dir>
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = lambda k: os.path.join(HERE, 'fig', k + '.png')

Q3STEM = 'Determine the transformations that could be used to linearise the data in each of the following scatterplots.'

CFATS = [
 dict(id='CFAT 1.4.1', subs='4A-4B', title='Squared and log transformations',
  layout=[([0],[1]),([2],[3])],
  mc=[
   dict(src='Edrolo 3D Q4', stem='An x-squared transformation was applied to a data set, but one value is missing.',
        table=[['x','1','3','6','8','12'],['y','3','12','32','81','132'],['x²','1','9','36','','144']],
        stem2='What is the missing value?', opts=['8','9','64','81'], ans=2),
   dict(src='Edrolo 3E Q1', stem='An x-squared transformation was applied to the data in the following table, and a least squares regression line was fitted.',
        table=[['x','5','9','14','20','24'],['y','22','23','25','30','35']],
        stem2='The equation of the least squares regression line is closest to',
        opts=['y = 17.269 + 0.676x²','y = 20.975 + 0.024x²','y = 206.701 + 37.910x²','y = −880.917 + 43.093x²'], ans=1),
   dict(src='Edrolo 3D Q7', stem='A log₁₀ y transformation was applied to a data set, but one value is missing.',
        table=[['x','10','20','30','40','50'],['y','10','84','732','5045','38 720'],['log₁₀ y','1','1.92','2.86','3.70','']],
        stem2='What is the missing value?', opts=['4.59','5.34','7.81','10.56'], ans=0),
   dict(src='Edrolo 3E Q6', stem='The relationship between the value ($) and age (years) of an antique vase has been linearised using a log₁₀ transformation. A least squares regression line is fitted to the transformed data and its equation is\nvalue = 37 000 + 13 000 × log₁₀(age)\nIf the value of the vase is $49 400, its age is closest to',
        opts=['1 year','5 years','8 years','9 years'], ans=3),
  ],
  sa=[
   dict(src='Edrolo 3D Q2', stem='Which square transformation(s) can be used to linearise each data set?',
        parts=[('a.','',1,'x-squared transformation','3D_Q2a',5.4),
               ('b.','',1,'x-squared and y-squared transformation','3D_Q2b',5.4)]),
   dict(src='Edrolo 3E Q7', stem='A group of medicine students went camping with a limited amount of mosquito repellent. The number of mosquito repellent sprays and the number of mosquito bites received for each student is shown in the scatterplot.\nA squared transformation was applied to the variable mosquito bites to linearise the data. A least squares regression line was then fitted to the transformed data and its equation is\n(mosquito bites)² = 282 − 49 × mosquito repellent sprays',
        fig='3E_Q7', w=6.0,
        parts=[('a.','Using the equation, estimate the number of mosquito repellent sprays a student would have applied if they received 6 mosquito bites. Round your answer to the nearest whole number.',2,'6² = 282 − 49 × sprays → sprays = (282 − 36) ÷ 49 = 5.02…\n5 sprays'),
               ('b.','Is the estimate in part a reliable? Justify your answer.',1,'Yes. The estimate is reliable because it is an interpolation.')]),
   dict(src='Edrolo 3E Q2', stem='Apply a log₁₀ y transformation to the data in the following table, and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to three decimal places.',
        table=[['x','2','4','5','8','10','14','15','17','19','20'],['y','32','34','38','53','67','102','118','134','168','182']],
        parts=[('','',2,'log₁₀(y) = 1.379 + 0.045x  (1 mark intercept, 1 mark slope)')]),
  ]),
 dict(id='CFAT 1.4.2', subs='4C-4D', title='Reciprocal transformation; choosing and applying a transformation',
  layout=[([0],[1]),('full',2),([3],[4]),('full',5)],
  mc=[
   dict(src='Edrolo 3D Q10', stem='An x-reciprocal transformation was applied to a data set, but one value is missing.',
        table=[['x','12','16','20','24','28'],['y','43','94','111','118','120'],['1/x','0.0833','0.0625','0.0500','','0.0357']],
        stem2='What is the missing value?', opts=['0.0042','0.0085','0.0406','0.0417'], ans=3),
   dict(src='Edrolo 3E Q5', stem='An x-reciprocal transformation was used to linearise a set of non-linear bivariate data. A least squares line was then fitted to the transformed data. The equation of this least squares line is\ny = 843 − 165 × 1/x\nThis equation is used to predict the value of y when x = 5.\nThe value of y is',
        opts=['0','18','810','876'], ans=2),
   dict(src='Edrolo 3D Q1', stem='Which transformations could be used to linearise the data in the scatterplot?', fig='3D_Q1', w=4.4,
        opts=['log x, x-reciprocal and y-squared','x-squared and y-squared','log x, x-reciprocal, log y and y-reciprocal','x-squared, log y and y-reciprocal'], ans=2),
   dict(src='Edrolo 3D Q3a', stem=Q3STEM + '\na.', fig='3D_Q3a', w=4.6,
        opts=['lifespan²','log₁₀(cost)','1/cost','All of the above'], ans=3),
   dict(src='Edrolo 3D Q3b', stem='b.', fig='3D_Q3b', w=4.6,
        opts=['age² and (bone density)²','1/bone density, log₁₀(bone density), 1/age and log₁₀(age)','age², log₁₀(bone density) and 1/age','(bone density)², log₁₀(age) and 1/bone density'], ans=1),
   dict(src='Edrolo 3D Q3c', stem='c.', fig='3D_Q3c', w=4.6,
        opts=['time²','log₁₀(points scored)','1/points scored','All of the above'], ans=3),
  ],
  sa=[
   dict(src='Edrolo 3E Q3', stem='Loki uploads soccer videos to Youtube daily. The number of new views on his latest video, on each day in the first week after uploading, are shown in the table.',
        table=[['day','1','2','3','4','5','6','7'],['views','321','113','54','36','28','24','21']],
        stem2='Apply a reciprocal transformation to the variable views, and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to four decimal places.',
        parts=[('','',2,'1/views = −0.0047 + 0.0077 × day  (1 mark intercept, 1 mark slope)')]),
   dict(src='Edrolo 3E Q8', stem='In an attempt to investigate claims that the sea levels are rising, a climate scientist decides to measure the increase in the depth of the sea just off a remote island every year, for ten years. Her results are shown in the following table.',
        table=[['year','1','2','3','4','5','6','7','8','9','10'],['sea level rise (cm)','0.21','0.10','0.13','0.25','0.12','0.20','0.19','0.27','0.20','0.42']],
        stem2='A reciprocal transformation was applied to the variable sea level rise to linearise the data. A least squares regression line was then fitted to the transformed data and its equation is\n1/sea level rise = 8.14 − 0.46 × year',
        parts=[('a.','Fill out the following table using the equation to predict the sea level rise in each of the next five years. Round each estimate to two decimal places.',2,'0.32, 0.38, 0.46, 0.59, 0.81',[['year','11','12','13','14','15'],['estimated sea level rise (cm)','','','','','']]),
               ('b.','Are the predictions in part a reliable? Justify your answer.',1,'No. The predictions may be of limited reliability because they are extrapolations.')]),
   dict(src='Edrolo 3E Q4', stem='Amanda competed in a 400 m swimming race. Her time for each lap of the 50-metre pool was recorded and the results are shown in the table.',
        table=[['lap','1','2','3','4','5','6','7','8'],['time (seconds)','31','40','44','50','53','55','58','60']],
        parts=[('a.','Apply a log transformation to the variable lap and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to one decimal place.',2,'time = 30.3 + 32.3 × log₁₀(lap)'),
               ('b.','Apply a squared transformation to the variable time and calculate the equation of the least squares regression line for the transformed data. Round the values of the intercept and slope to one decimal place.',2,'(time)² = 820.7 + 367.5 × lap'),
               ('c.','Which transformation is the best fit for the data set?',1,'time = 30.3 + 32.3 × log₁₀(lap)  (r² = 0.994 vs 0.975 for the squared transformation)')]),
  ]),
]
