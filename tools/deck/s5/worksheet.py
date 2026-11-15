"""Lesson 5 (1H-1I) guided worksheet, S1/S4 house style. Question text copied verbatim from lessons/S5-slides.html (which copied it from the sources).
Run: python3 tools/deck/s5/worksheet.py -> lessons/S5-worksheet(.html/.pdf) + lessons/S5-worksheet-solutions(.html/.pdf)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from wslib import *

P = [title('1H–1I', 'The normal distribution and standardised scores; populations and samples', 'Chapter 1 · 1H, 1I')]
P.append(lis(['To be able to introduce the normal model for bell-shaped distributions.', 'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.', 'To be able to calculate standardised scores and use them to compare values across distributions.']))

apk = (item('1', q('<b>1.</b> Suppose the distribution of weights for a type of cat is approximately symmetric and bell shaped with a mean of 3.5 kg and a standard deviation of 0.5 kg.')
            + q('Approximately what percentage of cats weigh between 2 kg and 5 kg?') + lines(2, '2 = 3.5 − 3 × 0.5 and 5 = 3.5 + 3 × 0.5: within three SDs → approximately 99.7%'),
            ncurve(3.5, .5, 'weight (kg)', dec=1, zrow=False, fill_x=True), sep=False)
       + cite(f'{CAM12} · Chapter 2 skills checklist, 2G #13')
       + item('2', q('<b>2.</b> A sample of 250 bonobos has been drawn at random from a population of bonobos whose neck size is normally distributed with a mean of 38 cm and a standard deviation of 2.3 cm.')
              + q('How many of these 250 bonobos are expected to have a neck size that is more than three standard deviations above or below the mean? Round to the nearest whole number. <i>(1 mark)</i>')
              + lines(2, '100% − 99.7% = 0.3%; 0.3% × 250 = 0.75 → 1 bonobo'))
       + guess('40%', mcq=False) + cite(f'{EDR12} · 1G Q14 · Adapted from VCAA 2020 Exam 2 Data analysis Q2b.i'))
P.append(box('Activating prior knowledge', apk, 'Year 11', cls='split'))

P.append(box('Key ideas · the 68–95–99.7% rule and standardised scores',
  '<div class="row"><div style="flex:1">' + q('In a normal distribution approximately <b>68%</b>, <b>95%</b> and <b>99.7%</b> of values lie within <b>one, two and three</b> standard deviations of the mean. Label the percentage in each section:')
  + ncurve(fill_pct=True) + '</div><div style="flex:1">'
  + q('<b>Standardised score:</b> z = (x − x̄) ÷ s &nbsp;&nbsp; <b>Actual score:</b> x = x̄ + z × s')
  + q('<b>Tails:</b> above z = 1: 16% · above z = 2: 2.5% · above z = 3: 0.15% (the same below −1, −2, −3).')
  + q('<b>Population:</b> every member of the group being studied. <b>Sample:</b> a subset of the population that is measured. Choose the sample at random.') + '</div></div>'
  + cite(f'{CAM}, 1H pp. 76–84; 1I (Interactive Textbook, own words)')))

P.append(pair('Example 28 · Applying the 68–95–99.7% rule',
  q('The distribution of delivery times for pizzas made by House of Pizza is approximately normal, with a mean of 25 minutes and a standard deviation of 5 minutes.') + ncurve(25, 5, 'Delivery time', zrow=False, fill_x=True)
  + parts([('a', 'What percentage of pizzas have delivery times of between 15 and 35 minutes?', '95%'), ('b', 'What percentage of pizzas have delivery times of greater than 30 minutes?', '16%'),
           ('c', 'In 1 month, House of Pizza delivers 2000 pizzas. Approximately many of these pizzas are delivered in less than 10 minutes?', '0.15% × 2000 = 3 pizzas')]) + cite(f'{CAM} · Example 28'),
  'You try · Edrolo 1H WE1',
  q('An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. The length of hair donated was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.')
  + ncurve(20, 4, '', zrow=False, fill_x=True)
  + parts([('a.', 'What percentage of hair lengths donated were between 16 cm and 32 cm?', '34 + 34 + 13.5 + 2.35 = 83.85%'),
           ('b.', 'Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?', '13.5 + 2.35 + 0.15 = 16%'),
           ('c.', 'If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?', '0.16 × 30 = 4.8 → 5 girls'),
           ('d.', 'How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?', '16% + 2.5% = 18.5%; 0.185 × 30 = 5.55 → 6 girls')]) + cite(f'{EDR} · 1H Worked example 1')))
P.append(pair('Example 29 · Calculating standard scores',
  q('The heights of a group of young women have a mean of x̄ = 160 cm and a standard deviation of s = 8 cm. Determine the standard or z-scores of a woman who is:')
  + parts([('a', '172 cm tall', 'z = (172 − 160) ÷ 8 = 1.5'), ('b', '150 cm tall', 'z = (150 − 160) ÷ 8 = −1.25'), ('c', '160 cm tall.', 'z = 0 (at the mean)')])
  + q('<b>CAS:</b> type (172−160)/8 with the brackets.') + cite(f'{CAM} · Example 29'),
  'You try · Edrolo 1I WE1',
  q('The weights of puppies within a litter are approximately normally distributed with a mean of 4 kg and a standard deviation of 0.3 kg.') + q('Determine the z-score of a puppy that weighs 4.6 kg.')
  + lines(2, 'z = (4.6 − 4) ÷ 0.3 = 2') + cite(f'{EDR} · 1I Worked example 1')))
P.append(pair('Example 30 · Using standardised scores to make comparisons',
  q('A student’s marks in Psychology and Statistics, with the mean and standard deviation for each subject:') + table([['Subject', 'Mark', 'Mean', 'Standard deviation'], ['Psychology', '75', '65', '10'], ['Statistics', '70', '60', '5']])
  + q('Another student studying the same two subjects obtained a mark of 55 for both Psychology and Statistics. Does this mean that she performed equally well in both subjects? Use standardised marks to help you arrive at your conclusion.')
  + lines(4, 'Psychology z = (55 − 65) ÷ 10 = −1 · Statistics z = (55 − 60) ÷ 5 = −1<br>Yes, her standardised score, z = −1, was the same for both subjects. In both subjects she finished in the bottom 16%.') + cite(f'{CAM} · Example 30'),
  'You try · Edrolo 1I WE3',
  q('The results for a Chemistry exam were approximately normally distributed, with a mean of 71 and a standard deviation of 3. The results for a Physics exam were also approximately normally distributed, with a mean of 95 and a standard deviation of 6.')
  + parts([('a.', 'A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.',
            'Chemistry z = (77 − 71) ÷ 3 = 2: top 2.5%. Physics z = (77 − 95) ÷ 6 = −3: bottom 0.15%. She did not do equally well.'),
           ('b.', 'Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.', 'z = (66 − 71) ÷ 3 = −1.67: in the bottom 16% of students.')]) + cite(f'{EDR} · 1I Worked example 3')))
P.append(pair('Example 31 · Using standard scores to determine percentages',
  q('Suppose the weight of a certain species of bird is normally distributed with a mean of 42 grams with a standard deviation of 3 grams.') + ncurve(42, 3, 'weight (grams)', fill_x=True)
  + parts([('a', 'If a bird selected at random from this population has a standardised weight of z = −1, what percentage of birds in this population weigh more than this bird?', '100% − 16% = 84%'),
           ('b', 'Approximately what percentage of birds would weigh between 39 and 48 grams?', 'z = −1 to z = 2: 34 + 34 + 13.5 = 81.5%')]) + cite(f'{CAM} · Example 31'),
  'You try · Edrolo 1H WE2',
  q('The length of hair donated was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm (basketball club, above).')
  + parts([('a.', '97.35% of the hair lengths will fall within 12 cm and which other value?', '13.5 + 34 + 34 + 13.5 + 2.35 = 97.35% → 32 cm'),
           ('b.', '2.5% of hair donated by the team will be disposed of, as it falls below a required minimum length. What is this required minimum length?', '0.15 + 2.35 = 2.5% → 12 cm')]) + cite(f'{EDR} · 1H Worked example 2')))
P.append(pair('Example 32 · Converting standard scores into actual scores',
  q('A class test (out of 50) has a mean mark of x̄ = 34 and a standard deviation of s = 4. Joe’s standardised test mark was z = −1.5.') + q('What was Joe’s actual mark?')
  + lines(2, 'x = 34 + (−1.5) × 4 = 28') + cite(f'{CAM} · Example 32'),
  'You try · Edrolo 1I WE2',
  q('The number of black stripes on tigers at the Royal Melbourne Zoo is known to be normally distributed with a mean of 55 and a standard deviation of 2. One of the tigers has a standardised number of stripes of z = −2.5.') + q('How many stripes does the tiger actually have?')
  + lines(2, 'x = 55 + (−2.5) × 2 = 50 stripes') + cite(f'{EDR} · 1I Worked example 2')))
P.append(pair('Examples 33 + 34 · Finding the mean and standard deviation',
  q('<b>33</b> Suppose the heights of red flowering gum trees have a mean of 10.2 metres, and 2.5% of these trees grow to more than 11.4 metres tall. Assuming that the heights of these trees are approximately normally distributed, what is the standard deviation of the height of the red flowering gum trees?')
  + lines(2, '11.4 is at z = 2: 11.4 = 10.2 + 2s → s = 0.6 metres')
  + q('<b>34</b> The marks scored in an examination are known to be approximately normally distributed. If 16% of students score more than 80 marks, and 2.5% of students score less than 20 marks, estimate the mean and standard deviation of this distribution.')
  + lines(3, 'x̄ − 2s = 20 and x̄ + s = 80 → 3s = 60, s = 20 · x̄ = 60') + cite(f'{CAM} · Examples 33, 34'),
  'You try · Edrolo 1H WE3',
  q('Duncan’s light bulb factory produces light bulbs.<br>The lifetime of their light bulbs are approximately normally distributed. It is known that approximately 95% of the light bulbs have a lifetime ranging from 800 hours to 1600 hours.')
  + parts([('a.', 'Calculate the standard deviation for the lifetime of a light bulb.', 'four SDs = 1600 − 800 = 800 → s = 200 hours'), ('b.', 'Calculate the mean lifetime of a light bulb.', '800 + 2 × 200 = 1200 hours')]) + cite(f'{EDR} · 1H Worked example 3')))

ex = (q('<b>1.</b> The <i>temperature difference</i> between the <i>minimum daily temperature</i> and the <i>maximum daily temperature</i> in November 2017 at a location is approximately normally distributed with a mean of 9.4 °C and a standard deviation of 3.2 °C.')
      + q('Determine the number of days in November 2017 for which this <i>temperature difference</i> is expected to be greater than 9.4 °C. <i>(1 mark)</i>') + lines(1, '50% of 30 days = 15 days')
      + guess('58%', mcq=False) + cite(f'{EDR} · 1H Q12 · VCAA 2019 Exam 2 Data analysis Q2b')
      + item('2', q('<b>2.</b> In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.')
             + q('Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place. <i>(1 mark)</i>') + lines(2, 'z = (14.50 − 13.74) ÷ 1.43 = 0.531… → 0.5'),
             table([['statistic', 'shot-put (metres)'], ['mean', '13.74'], ['standard deviation', '1.43']]))
      + guess('78%', mcq=False) + cite(f'{EDR} · 1I Q13 · VCAA 2021 Exam 2 Data analysis Q1c'))
P.append(box('Exit tasks', ex, 'Show what you know', cls='split'))
P.append(checklist(['I can apply the 68-95-99.7% rule.', 'I can calculate standardised scores.', 'I can use standardised scores to make comparisons.', 'I can use standard scores to determine percentages.', 'I can convert standardised scores into actual scores.', 'I can solve for the values of the mean and standard deviation.', 'I can explain the difference between a population and a sample.']))
P.append(coursework([('Exercise 1H', 'Q1–5 · Q6–7 · Q8 · Q9–10<br>Q11 · Q12–15 · Q16–18<br>Q19–23 <i>(Exam 1 style)</i>'), ('Exercise 1I', 'Interactive Textbook<br>(Cambridge GO)')], '1H section'))
build('1H–1I', 'The normal distribution and standardised scores; populations and samples', P, 'S5')
