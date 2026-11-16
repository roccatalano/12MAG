"""Lesson 5 (1H-1I) guided worksheet, CFAT / revision-booklet style (tools/deck/ws2.py; model tools/deck/s1/worksheet.py).
Questions verbatim from tools/deck/s5/build.py (which copied them from the sources).
Sources (not printed, Rocco 15 Nov: only exam questions show their source):
APK 1 = Cambridge U1&2 Ch 2 skills checklist 2G #13; APK 2 = Edrolo U1&2 1G Q14 (adapted from VCAA 2020 E2 Q2b.i);
Examples 28-34 = Cambridge U3&4 Examples 28-34; You trys = Edrolo U3&4 1H WE1, 1I WE1, 1I WE3, 1H WE2, 1I WE2, 1H WE3;
exits = Edrolo U3&4 1H Q12 (VCAA 2019 E2 Q2b), 1I Q13 (VCAA 2021 E2 Q1c).
1I populations and samples: no Example / worked example in Cambridge or Edrolo, so no question here (the slides have a Learn slide).
Run: python3 tools/deck/s5/worksheet.py"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from ws2 import *

R = '#c00'
def ncurve(m=None, s=None, xl='', W=320, H=118, dec=0, zrow=True, fill_x=False, fill_pct=False, pct=True, mm=86):
    """Normal curve with section lines. fill_x / fill_pct: blank for students, red on the solutions copy (class 'a')."""
    x0, x1 = 12, W - 12; yb = H - (10 + (12 if m is not None else 0) + (12 if zrow else 0) + (12 if xl else 0)); top = 8
    X = lambda z: x0 + (z + 3.6) / 7.2 * (x1 - x0); Y = lambda z: yb - (yb - top) * math.exp(-z * z / 2)
    o = [f'<polyline points="{" ".join(f"{X(z):.1f},{Y(z):.1f}" for z in [-3.6 + i * .05 for i in range(145)])}" fill="none" stroke="#000" stroke-width="1.2"/>',
         f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#000"/>']
    o += [f'<line x1="{X(z):.1f}" y1="{Y(z):.1f}" x2="{X(z):.1f}" y2="{yb+3}" stroke="#777" stroke-width=".6"/>' for z in range(-3, 4)]
    hid = lambda f: ' class="wsa"' if f else ''
    if pct:
        for z, p in [(-3.3, '0.15'), (-2.5, '2.35'), (-1.5, '13.5'), (-.5, '34'), (.5, '34'), (1.5, '13.5'), (2.5, '2.35'), (3.3, '0.15')]:
            yy = min(Y(z) + 13, yb - 3) if abs(z) < 2 else yb - 3
            o.append(f'<text{hid(fill_pct)} x="{X(z):.1f}" y="{yy:.1f}" font-size="{7.5 if abs(z)<2 else 6.2}" text-anchor="middle">{p}%</text>')
    yy = yb + 10
    if m is not None:
        o += [f'<text{hid(fill_x and z)} x="{X(z):.1f}" y="{yy}" font-size="8" text-anchor="middle">{m+z*s:.{dec}f}</text>' for z in range(-3, 4)]
        yy += 12
    if zrow:
        o += [f'<text x="{X(z):.1f}" y="{yy}" font-size="7.5" fill="#555" text-anchor="middle">{"z = " if z==-3 else ""}{z}</text>' for z in range(-3, 4)]; yy += 12
    if xl: o.append(f'<text x="{W/2}" y="{yy}" font-size="8.5" text-anchor="middle">{xl}</text>')
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{mm}mm;display:block;margin:1mm auto">{"".join(o)}</svg>'
STY = f'<style>svg text.wsa{{visibility:hidden}} .sol svg text.wsa{{visibility:visible;fill:{R}}}</style>'

P = [STY, title('1H–1I', 'The normal distribution and standardised scores; populations and samples')]
P.append(lis(['To be able to introduce the normal model for bell-shaped distributions.',
  'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.',
  'To be able to calculate standardised scores and use them to compare values across distributions.']))

# ---------------------------------------------------------------- APK
P.append(sect('Activating prior knowledge', 'Year 11'))
P.append(box('Question 1', q('Suppose the distribution of weights for a type of cat is approximately symmetric and bell shaped with a mean of 3.5 kg and a standard deviation of 0.5 kg.')
  + ncurve(3.5, .5, 'weight (kg)', dec=1, zrow=False, fill_x=True, mm=80)
  + q('Approximately what percentage of cats weigh between 2 kg and 5 kg?') + space(12, '2 = 3.5 − 3 × 0.5 and 5 = 3.5 + 3 × 0.5: within three standard deviations → approximately 99.7%')))
P.append(box('Question 2 · VCAA 2020 Exam 2 Q2b.i (adapted)', q('A sample of 250 bonobos has been drawn at random from a population of bonobos whose <i>neck size</i> is normally distributed with a mean of 38 cm and a standard deviation of 2.3 cm.')
  + q('How many of these 250 bonobos are expected to have a <i>neck size</i> that is more than three standard deviations above or below the mean? Round to the nearest whole number.')
  + space(16, '100% − 99.7% = 0.3%; 0.3% × 250 = 0.75 → 1 bonobo'), '1 mark'))

# ---------------------------------------------------------------- 1H
P.append(sect('1H The normal distribution and the 68–95–99.7% rule', 'Example, then you try'))
P.append(exyt('Example 28 · Applying the 68–95–99.7% rule',
  q('The distribution of delivery times for pizzas made by House of Pizza is approximately normal, with a mean of 25 minutes and a standard deviation of 5 minutes.')
  + ncurve(25, 5, 'Delivery time', zrow=False, fill_x=True, fill_pct=True, mm=80)
  + parts([('a', 'What percentage of pizzas have delivery times of between 15 and 35 minutes?', '15 = 25 − 2 × 5, 35 = 25 + 2 × 5: within two SDs → 95%', 12),
           ('b', 'What percentage of pizzas have delivery times of greater than 30 minutes?', '30 = 25 + 1 × 5 → 16%', 12),
           ('c', 'In 1 month, House of Pizza delivers 2000 pizzas. Approximately many of these pizzas are delivered in less than 10 minutes?', '10 = 25 − 3 × 5: 0.15% × 2000 = 3 pizzas', 14)]),
  'You try 1',
  q('An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. The <i>length of hair donated</i> was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.')
  + parts([('a.', 'What percentage of hair lengths donated were between 16 cm and 32 cm?', '34 + 34 + 13.5 + 2.35 = 83.85%', 14),
           ('b.', 'Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?', '13.5 + 2.35 + 0.15 = 16%', 14),
           ('c.', 'If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?', '0.16 × 30 = 4.8 → 5 girls', 14),
           ('d.', 'How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?', '0.15 + 2.35 + 13.5 + 2.35 + 0.15 = 18.5%; 0.185 × 30 = 5.55 → 6 girls', 14)])))

P.append(exyt('Example 29 · Calculating standard scores',
  q('The heights of a group of young women have a mean of <i>x̄</i> = 160 cm and a standard deviation of <i>s</i> = 8 cm. Determine the standard or z-scores of a woman who is:')
  + parts([('a', '172 cm tall', 'z = (172 − 160) ÷ 8 = 1.5', 12), ('b', '150 cm tall', 'z = (150 − 160) ÷ 8 = −1.25', 12), ('c', '160 cm tall.', 'z = (160 − 160) ÷ 8 = 0 (at the mean)', 12)]),
  'You try 2',
  q('The weights of puppies within a litter are approximately normally distributed with a mean of 4 kg and a standard deviation of 0.3 kg.')
  + q('Determine the z-score of a puppy that weighs 4.6 kg.') + space(24, 'z = (4.6 − 4) ÷ 0.3 = 2')))

PS = table([['Subject', 'Mark', 'Mean', 'Standard deviation'], ['Psychology', '75', '65', '10'], ['Statistics', '70', '60', '5']])
P.append(exyt('Example 30 · Using standardised scores to make comparisons',
  q('A student’s marks in Psychology and Statistics, with the mean and standard deviation for each subject:') + PS
  + q('Another student studying the same two subjects obtained a mark of 55 for both Psychology and Statistics. Does this mean that she performed equally well in both subjects? Use standardised marks to help you arrive at your conclusion.')
  + space(34, 'Psychology: z = (55 − 65) ÷ 10 = −1<br>Statistics: z = (55 − 60) ÷ 5 = −1<br>Yes, her standardised score, z = −1, was the same for both subjects. In both subjects she finished in the bottom 16%.'),
  'You try 3',
  q('The results for a Chemistry exam were approximately normally distributed, with a mean of 71 and a standard deviation of 3. The results for a Physics exam were also approximately normally distributed, with a mean of 95 and a standard deviation of 6.')
  + parts([('a.', 'A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.',
            'Chemistry: z = (77 − 71) ÷ 3 = 2 · Physics: z = (77 − 95) ÷ 6 = −3<br>In Chemistry, z = 2 places her in the top 2.5% of students. In Physics, z = −3 places her in the bottom 0.15%. She did not do equally well in both exams compared to her peers.', 34),
           ('b.', 'Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.',
            'z = (66 − 71) ÷ 3 = −1.67, placing him in the bottom 16% of students.', 22)])))

P.append(exyt('Example 31 · Using standard scores to determine percentages',
  q('Suppose the weight of a certain species of bird is normally distributed with a mean of 42 grams with a standard deviation of 3 grams.')
  + ncurve(42, 3, 'weight (grams)', fill_x=True, fill_pct=True, mm=80)
  + parts([('a', 'If a bird selected at random from this population has a standardised weight of <i>z</i> = −1, what percentage of birds in this population weigh more than this bird?', '16% are below z = −1, so 100% − 16% = 84%', 14),
           ('b', 'Approximately what percentage of birds would weigh between 39 and 48 grams?', 'z = (39 − 42) ÷ 3 = −1 · z = (48 − 42) ÷ 3 = 2<br>34 + 34 + 13.5 = 81.5%', 18)]),
  'You try 4',
  q('An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. The <i>length of hair donated</i> was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.')
  + parts([('a.', '97.35% of the hair lengths will fall within 12 cm and which other value?', '12 cm is two SDs below: 13.5 + 34 + 34 + 13.5 + 2.35 = 97.35% ends three SDs above → 32 cm', 22),
           ('b.', '2.5% of hair donated by the team will be disposed of, as it falls below a required minimum length. What is this required minimum length?', '0.15 + 2.35 = 2.5% lies below two SDs under the mean → 12 cm', 22)])))

P.append(exyt('Example 32 · Converting standard scores into actual scores',
  q('A class test (out of 50) has a mean mark of <i>x̄</i> = 34 and a standard deviation of <i>s</i> = 4. Joe’s standardised test mark was <i>z</i> = −1.5.')
  + q('What was Joe’s actual mark?') + space(20, 'x = x̄ + z × s = 34 + (−1.5) × 4 = 28'),
  'You try 5',
  q('The number of black stripes on tigers at the Royal Melbourne Zoo is known to be normally distributed with a mean of 55 and a standard deviation of 2. One of the tigers has a standardised number of stripes of <i>z</i> = −2.5.')
  + q('How many stripes does the tiger actually have?') + space(20, 'x = 55 + (−2.5) × 2 = 50 stripes')))

P.append(exyt('Example 33 · Finding the standard deviation given the mean and one percentage',
  q('Suppose the heights of red flowering gum trees have a mean of 10.2 metres, and 2.5% of these trees grow to more than 11.4 metres tall. Assuming that the heights of these trees are approximately normally distributed, what is the standard deviation of the height of the red flowering gum trees?')
  + ncurve(zrow=True, pct=True, mm=70) + space(18, '2.5% above → 11.4 m is at z = 2: 11.4 = 10.2 + 2 × s → 2s = 1.2 → s = 0.6 metres'),
  'Example 34 · Finding the mean and standard deviation',
  q('The marks scored in an examination are known to be approximately normally distributed. If 16% of students score more than 80 marks, and 2.5% of students score less than 20 marks, estimate the mean and standard deviation of this distribution.')
  + ncurve(zrow=True, pct=True, mm=70) + space(18, '20 at z = −2: x̄ − 2s = 20 · 80 at z = 1: x̄ + s = 80<br>Subtract: 3s = 60 → s = 20 · x̄ = 20 + 40 = 60')))
P.append(box('You try 6',
  q('Duncan’s light bulb factory produces light bulbs.<br>The <i>lifetime</i> of their light bulbs are approximately normally distributed. It is known that approximately 95% of the light bulbs have a <i>lifetime</i> ranging from 800 hours to 1600 hours.')
  + parts([('a.', 'Calculate the standard deviation for the <i>lifetime</i> of a light bulb.', '95% lies within two SDs each side: four SDs = 1600 − 800 = 800 → s = 800 ÷ 4 = 200 hours', 16),
           ('b.', 'Calculate the mean <i>lifetime</i> of a light bulb.', '800 + 2 × 200 = 1200 hours', 12)], cols=2)))

# ---------------------------------------------------------------- exits
P.append(sect('Exit tasks', 'Show what you know'))
P.append(box('Exit task 1 · VCAA 2019 Exam 2 Q2b', q('The <i>temperature difference</i> between the <i>minimum daily temperature</i> and the <i>maximum daily temperature</i> in November 2017 at a location is approximately normally distributed with a mean of 9.4 °C and a standard deviation of 3.2 °C.')
  + q('Determine the number of days in November 2017 for which this <i>temperature difference</i> is expected to be greater than 9.4 °C.')
  + space(16, '9.4 °C is the mean: 50% of days are above it. 50% × 30 = 15 days'), '1 mark'))
P.append(box('Exit task 2 · VCAA 2021 Exam 2 Q1c', '<div class="row"><div style="flex:1">'
  + q('In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.')
  + '</div><div style="flex:none;width:55mm">' + table([['statistic', '<i>shot-put</i> (metres)'], ['mean', '13.74'], ['standard deviation', '1.43']]) + '</div></div>'
  + q('Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place.')
  + space(16, 'z = (14.50 − 13.74) ÷ 1.43 = 0.531… → z = 0.5'), '1 mark'))

P.append(close(['I can apply the 68-95-99.7% rule.', 'I can calculate standardised scores.', 'I can use standardised scores to make comparisons.',
  'I can use standard scores to determine percentages.', 'I can convert standardised scores into actual scores.', 'I can solve for the values of the mean and standard deviation.',
  'I can explain the difference between a population and a sample.'],
  [('1H', 'Q1–10'), ('1H', 'Q11–23'), ('1I', 'Interactive Textbook (Cambridge GO)')], ['1H']))
build('S5', '1H–1I', 'AoS 1 · Data analysis', P)
