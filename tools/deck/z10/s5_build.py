r"""12MAG S5 (1H normal distribution, z-scores · 1I populations and samples) built in the 10MA slide house style.
Built on the slide library tools/deck/z10/lib (rules: tools/deck/z10/HOWTO.md).
python3 tools/deck/z10/s5_build.py  ->  lessons/S5-slides.html
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib.deck import *
from lib.normal import *
lesson('1H The normal distribution · 1I Populations and samples')
# ---------------- slides ----------------
# S5 = 1H The normal distribution and the 68–95–99.7% rule (+ standardised scores) · 1I Populations and samples.
# Content from the planner card gm12-u3-s5 and the old deck (git history) tools/deck/s5/build.py (questions there are verbatim and cited).
# 1I: Cambridge 1I is Interactive Textbook only and Edrolo has no worked example, so 1I is a New learning slide only (no question written).
KI_RULE = r'about <b>68%</b>, <b>95%</b>, <b>99.7%</b> of values lie within <b>1, 2, 3</b> standard deviations of the mean<div class="kn">tails: 16% · 2.5% · 0.15% on each side</div>'
KI_Z = r'$z = \dfrac{x - \bar{x}}{s}$<div class="kn">+ above the mean · 0 at the mean · − below the mean</div>'
KI_X = r'$x = \bar{x} + z \times s$<div class="kn">start at the mean, step $z$ standard deviations</div>'
KI_ZP = r'Convert to $z$-scores, then add the sections<div class="kn">34 · 13.5 · 2.35 · 0.15 (% on each side of the mean)</div>'


title_slide('The normal distribution and standardised scores', ['1H The normal distribution and the 68–95–99.7% rule (pp. 76–84)', '1I Populations and samples (Interactive Textbook)'])
LI = ['To be able to introduce the normal model for bell-shaped distributions.',
      'To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.',
      'To be able to calculate standardised scores and use them to compare values across distributions.']
SC = ['I can apply the 68-95-99.7% rule.', 'I can calculate standardised scores.', 'I can use standardised scores to make comparisons.',
      'I can use standard scores to determine percentages.', 'I can convert standardised scores into actual scores.',
      'I can solve for the values of the mean and standard deviation.', 'I can explain the difference between a population and a sample.']
SEQ = ['CFAT 1.1.2 (20 minutes, 1F–1G)', 'Activating prior knowledge', 'Key ideas and formulas', 'The 68–95–99.7% rule · Example 28',
       'Standardised scores · Example 29 · CAS', 'Comparing with z-scores · Example 30', 'z-scores to percentages · Example 31',
       'Actual scores · Example 32', 'Finding $s$ and $\\bar{x}$ · Examples 33–34', 'Populations and samples (1I)', 'Exit tasks', 'Check-in and coursework']
overview('1H–1I', LI, SC, SEQ, CG + ", 1H Learning intentions (p. 76); 1I has none in the printed book. Success criteria: planner card", cols='1.05fr 1.05fr .9fr')
S.append(f'<section class="slide z cfat">{bar("CFAT 1.1.2", "Median, IQR, boxplots, SOCS")}'
         '<div class="cols" style="grid-template-columns:1fr 1fr"><div class="col"><h2>How it runs</h2><ul class="zul">'
         '<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · 14 marks</li>'
         '<li>Covers 1F–1G</li><li>Pens down when the timer ends</li></ul></div>'
         '<div class="col zc"><h2>Time remaining</h2><div class="ztime ix" data-s="1200">20:00</div>'
         '<div class="ix zbtns"><button data-a="go">▶ Start</button><button data-a="pause">❚❚ Pause</button><button data-a="reset">↺ Reset</button></div></div></div>'
         f'{foot("CFAT 1.1.2 (1F–1G): student copy and solutions on the planner")}</section>')

# APK 1: Cambridge U1&2 2G #13
S.append(qslide('apk', '1 of 2', 'Year 11 skills: the 68–95–99.7% rule', 'Cambridge U1&amp;2 · 2G #13',
    'Suppose the distribution of weights for a type of cat is approximately symmetric and bell shaped with a mean of 3.5 kg and a standard deviation of 0.5 kg.'
    '<br><b>a.</b> Approximately what percentage of cats weigh between 2 kg and 5 kg?', KI_RULE,
    [('Scale the curve: 3.5 ± 0.5, 1.0, 1.5 kg → 2.0 … 5.0 kg', 'nx:a1'),
     ('$2 = 3.5 - 3 \\times 0.5$ and $5 = 3.5 + 3 \\times 0.5$: within <b>three</b> standard deviations', 'nx:a1 ' + sh('a1', -3, 3, '99.7%'))],
    'approximately <b>99.7%</b> of cats', 'Cambridge General Mathematics Units 1&amp;2, Chapter 2 skills checklist 2G #13. Working by teacher.',
    fig=ncurve('a1', 3.5, 0.5, 'weight (kg)', 1, z=False), figw='1.15fr', ans_do='nx:a1 ' + sh('a1', -3, 3, '99.7%')))
# APK 2: Edrolo U1&2 1G Q14 = VCAA 2020 E2 Q2bi (adapted by Edrolo)
A2 = 'nx:a2 ' + sh('a2', -3.6, -3, '', 'o') + ' ' + sh('a2', 3, 3.6, '0.3%', 'o')
S.append(qslide('apk', '2 of 2', 'A real VCAA question you can already do', 'VCAA 2020 Exam 2 Q2bi (adapted)',
    'A sample of 250 bonobos has been drawn at random from a population of bonobos whose <i>neck size</i> is normally distributed with a mean of 38 cm and a standard deviation of 2.3 cm.<br>'
    'How many of these 250 bonobos are expected to have a <i>neck size</i> that is more than three standard deviations above or below the mean? Round to the nearest whole number.',
    KI_RULE, [('Within three standard deviations: 99.7%', 'nx:a2 ' + sh('a2', -3, 3, '99.7%')),
              ('More than three away: $100\\% - 99.7\\% = 0.3\\%$', A2),
              ('$0.3\\% \\times 250 = 0.003 \\times 250 = 0.75$', A2)],
    '$0.75 \\to$ <b>1 bonobo</b>',
    'Edrolo General Mathematics Units 1&amp;2, 1G Q14 (adapted by Edrolo from VCAA 2020 Exam 2 Data analysis Q2bi); % from the examiner report. Working by teacher.',
    marks=1, vcaa=40, figw='1.15fr', fig=ncurve('a2', 38, 2.3, 'neck size (cm)', 1, z=False, small=True), ans_do=A2, watch='0.75 is not a number of bonobos. Round to the nearest whole number, as the question asks. <span class="zsc">(teacher note)</span>'))

# Key ideas
KD = [('Normal distribution', 'a symmetric, bell-shaped model: mean = median, in the centre'),
      ('68–95–99.7% rule', 'about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean'),
      ('Standardised score ($z$-score)', 'how many standard deviations a value is above (+) or below (−) the mean'),
      ('Population', 'every member of the group being studied'), ('Sample', 'a subset of the population')]
KF = [('Within 1 SD', r'$\bar{x} - s$ to $\bar{x} + s$: ≈ 68%'), ('Within 2 SDs', r'$\bar{x} - 2s$ to $\bar{x} + 2s$: ≈ 95%'),
      ('Within 3 SDs', r'$\bar{x} - 3s$ to $\bar{x} + 3s$: ≈ 99.7%'), ('Standardised score', r'$z = \dfrac{x - \bar{x}}{s}$'),
      ('Actual score', r'$x = \bar{x} + z \times s$'), ('Tails (each side)', 'beyond 1 SD: 16% · 2 SD: 2.5% · 3 SD: 0.15%')]
S.append(f'<section class="slide z kif">{bar("1H–1I", "Key ideas")}<div class="cols" style="grid-template-columns:1fr 1fr">'
         f'<div class="col"><h2>Key definitions</h2>{"".join(f"<div class=zkd><span><b>{a}</b>: {b}</span></div>" for a, b in KD)}</div>'
         f'<div class="col"><h2>Key formulas</h2>{"".join(f"<div class=zkd><span class=zkn>{a}</span><span>{b}</span></div>" for a, b in KF)}</div></div>'
         f'{foot(CG + ", 1H Key ideas (pp. 76–84); 1I definitions in own words")}</section>')

# NL: the rule
S.append(nl_slide('The normal distribution and the 68–95–99.7% rule',
    'A <b>normal</b> distribution is bell shaped and symmetric: the mean is in the middle and the standard deviation sets the width. <span class="hint">Click to build the rule.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l1', None, None, '', 0) + '</div><div class="col">'
    + st('Within <b>1</b> SD of the mean: about <b>68%</b>', do=sh('l1', -1, 1, '68%'), cls='stp')
    + st('Within <b>2</b> SDs: about <b>95%</b>', do=sh('l1', -2, 2, '95%'), cls='stp')
    + st('Within <b>3</b> SDs: about <b>99.7%</b>', do=sh('l1', -3, 3, '99.7%'), cls='stp')
    + st('Halve the leftovers for each tail: <b>16%</b>, <b>2.5%</b>, <b>0.15%</b>', do='ncl:l1 np:l1', cls='stp')
    + st('Every section: 34, 13.5, 2.35, 0.15 on each side. They add to 100%.', True, do='ncl:l1 np:l1', cls='stp') + '</div></div>',
    CG + ', 1H pp. 76–78. Curve: teacher illustration.'))

# Example 28 / You try (Edrolo 1H WE1)
S.append(qslide('ex', 28, 'Applying the 68–95–99.7% rule', 'Cambridge · Example 28',
    'The distribution of delivery times for pizzas made by House of Pizza is approximately normal, with a mean of 25 minutes and a standard deviation of 5 minutes.', KI_RULE, [], None,
    CG + ', 1H Example 28 (p. 78). Part c is as typed in the old deck (“Approximately many”): check against the book.',
    parts=[('a', 'What percentage of pizzas have delivery times of between 15 and 35 minutes?',
            [('$15 = 25 - 2 \\times 5$, $35 = 25 + 2 \\times 5$: within 2 SDs', 'nx:w28 ' + sh('w28', -2, 2, '95%'))], '<b>95%</b>', 'nx:w28 ' + sh('w28', -2, 2, '95%')),
           ('b', 'What percentage of pizzas have delivery times of greater than 30 minutes?',
            [('$30 = 25 + 1 \\times 5$: more than 1 SD above', 'nx:w28 ncl:w28 ' + sh('w28', 1, 3.6, '16%'))], '<b>16%</b>', 'nx:w28 ncl:w28 ' + sh('w28', 1, 3.6, '16%')),
           ('c', 'In 1 month, House of Pizza delivers 2000 pizzas. Approximately many of these pizzas are delivered in less than 10 minutes?',
            [('$10 = 25 - 3 \\times 5$: 0.15% below. $0.0015 \\times 2000$', 'nx:w28 ncl:w28 ' + sh('w28', -3.6, -3, '0.15%', 'o'))],
            '<b>3 pizzas</b>', 'nx:w28 ncl:w28 ' + sh('w28', -3.6, -3, '0.15%', 'o'))],
    fig=ncurve('w28', 25, 5, 'delivery time (minutes)'), figw='.72fr', cls='tight tt'))
HAIR = ('An entire girl’s basketball club decided to shave their heads to raise money for cancer. They also donated their hair to be made into wigs for those undergoing treatment. '
        'The <i>length of hair donated</i> was approximately normally distributed with a mean of 20 cm and a standard deviation of 4 cm.')
S.append(qslide('yt', '28 (a, b)', 'Applying the 68–95–99.7% rule', 'Edrolo 1H WE1', HAIR, KI_RULE, [], None,
    ED + ', 1H Worked example 1 (parts a–b; c–d on the next slide). Working by teacher.',
    parts=[('a.', 'What percentage of hair lengths donated were between 16 cm and 32 cm?',
            [('16 cm is 1 SD below, 32 cm is 3 SDs above', 'nx:y1 np:y1 ' + sh('y1', -1, 3, '')), ('$34 + 34 + 13.5 + 2.35$', 'nx:y1 np:y1 ' + sh('y1', -1, 3, ''))], '<b>83.85%</b>', 'nx:y1 np:y1 ' + sh('y1', -1, 3, '')),
           ('b.', 'Donated hair lengths greater than 24 cm are highly sought after as they can be customised for a diverse range of hairstyles. What percentage of the girl’s basketball club donated hair greater than 24 cm?',
            [('24 cm is 1 SD above: $13.5 + 2.35 + 0.15$', 'nx:y1 np:y1 ncl:y1 ' + sh('y1', 1, 3.6, ''))], '<b>16%</b>', 'nx:y1 np:y1 ncl:y1 ' + sh('y1', 1, 3.6, ''))],
    fig=ncurve('y1', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))
S.append(qslide('yt', '28 (c, d)', 'Applying the 68–95–99.7% rule', 'Edrolo 1H WE1', HAIR, KI_RULE, [], None,
    ED + ', 1H Worked example 1 (parts c–d). Working by teacher.',
    parts=[('c.', 'If there are 30 girls at the basketball club, how many of them are expected to have donated hair lengths longer than 24 cm, rounded to the nearest person?',
            [('Longer than 24 cm: 16% (part b)', 'nx:y1b np:y1b ' + sh('y1b', 1, 3.6, '')), '$0.16 \\times 30 = 4.8$'], '<b>5 girls</b>', 'nx:y1b np:y1b ' + sh('y1b', 1, 3.6, '')),
           ('d.', 'How many girls are expected to have donated hair lengths that were either less than 16 cm or greater than 28 cm, rounded to the nearest person?',
            [('Below 16 cm: 16% · above 28 cm: 2.5%', 'nx:y1b np:y1b ncl:y1b ' + sh('y1b', -3.6, -1, '', 'o') + ' ' + sh('y1b', 2, 3.6, '', 'o')),
             '$16\\% + 2.5\\% = 18.5\\%$; $0.185 \\times 30 = 5.55$'], '<b>6 girls</b>',
            'nx:y1b np:y1b ncl:y1b ' + sh('y1b', -3.6, -1, '', 'o') + ' ' + sh('y1b', 2, 3.6, '', 'o'))],
    fig=ncurve('y1b', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))

# NL: z-scores
S.append(nl_slide('Standardised scores ($z$-scores)',
    r'A $z$-score counts how many standard deviations a value is from the mean: $z = \dfrac{x - \bar{x}}{s}$. <span class="hint">IQ scores: mean 100, standard deviation 15. Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l2', 100, 15, 'IQ score', 0) + '</div><div class="col">'
    + st('Each standard deviation is one step on the $z$ row.', do='nx:l2 nz:l2', cls='stp')
    + st(r'IQ 115: $z = \dfrac{115 - 100}{15} = 1$', do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1'), cls='stp')
    + st(r'IQ 70: $z = \dfrac{70 - 100}{15} = -2$', do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1') + ' ' + mk('l2', -2, 'z = −2', 'b'), cls='stp')
    + st('Check the sign: below the mean gives a <b>negative</b> $z$.', True, do='nx:l2 nz:l2 ' + mk('l2', 1, 'z = 1') + ' ' + mk('l2', -2, 'z = −2', 'b'), cls='stp') + '</div></div>',
    CG + ', 1H p. 80 (IQ illustration). Curve: teacher illustration.'))

# Example 29
S.append(qslide('ex', 29, 'Calculating standard scores', 'Cambridge · Example 29',
    r'The heights of a group of young women have a mean of $\bar{x} = 160$ cm and a standard deviation of $s = 8$ cm. Determine the standard or z-scores of a woman who is:', KI_Z, [], None,
    CG + ', 1H Example 29 (p. 80)',
    parts=[('a', '172 cm tall', [(r'$z = \dfrac{172 - 160}{8}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172'))], '$\\boldsymbol{z = 1.5}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172')),
           ('b', '150 cm tall', [(r'$z = \dfrac{150 - 160}{8}$', 'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b'))], '$\\boldsymbol{z = -1.25}$',
            'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b')),
           ('c', '160 cm tall.', [(r'$z = \dfrac{160 - 160}{8}$', None)], '$\\boldsymbol{z = 0}$ (at the mean)',
            'nx:w29 nz:w29 ' + mk('w29', 1.5, '172') + ' ' + mk('w29', -1.25, '150', 'b') + ' ' + mk('w29', 0, '160', 'g'))],
    fig=ncurve('w29', 160, 8, 'height (cm)'), figw='.75fr', cls='tight tt'))

# CAS (steps from planner/cas-skills.json, skill z-score)
CSK = [x for x in json.load(open(os.path.join(HERE, '..', '..', '..', 'planner', 'cas-skills.json')))['skills'] if x['id'] == 'z-score'][0]
amp = lambda t: t.replace('& ', '&amp; ')
TABS = ('<div class="zcas2"><div><div class="zch3">TI-Nspire</div>' f'<ol class="zcas">{"".join(f"<li>{amp(x)}</li>" for x in CSK["ti"])}</ol></div>'
        '<div><div class="zch3">ClassPad</div>' f'<ol class="zcas">{"".join(f"<li>{amp(x)}</li>" for x in CSK["classpad"])}</ol></div>'
        f'<div class="zrule" style="margin-top:0">{CSK["tip"]}</div></div>')
S.append(qslide('cas', '', 'Standardised scores on CAS', 'Cambridge · Example 29a',
    'The heights of a group of young women have a mean of $\\bar{x} = 160$ cm and a standard deviation of $s = 8$ cm. Determine the standard or z-scores of a woman who is:<br><b>a.</b> 172 cm tall',
    KI_Z, ['Type the whole rule with brackets: $(172 - 160) \\div 8$', 'Without brackets: $172 - 160 \\div 8 = 152$. Wrong!'],
    '$\\boldsymbol{z = 1.5}$', CG + ', 1H Example 29a (p. 80). CAS steps: planner CAS guide (z-score).',
    fig=TABS, figw='1.1fr'))

S.append(qslide('yt', 29, 'Calculating standardised (z) scores', 'Edrolo 1I WE1',
    'The weights of puppies within a litter are approximately normally distributed with a mean of 4 kg and a standard deviation of 0.3 kg. Determine the z-score of a puppy that weighs 4.6 kg.',
    KI_Z, [(r'$z = \dfrac{4.6 - 4}{0.3} = \dfrac{0.6}{0.3}$', 'nx:y29 nz:y29 ' + mk('y29', 2, '4.6 kg'))], '$\\boldsymbol{z = 2}$',
    ED + ', 1I Worked example 1. Working by teacher.', fig=ncurve('y29', 4, 0.3, 'weight (kg)', 1), figw='1.1fr', ans_do='nx:y29 nz:y29 ' + mk('y29', 2, '4.6 kg')))

# Interactive: which test went better? (Example 30 means and SDs)
S.append(f'<section class="slide z nl ztwo">{bar("New learning", "Which test went better? Use z-scores")}'
    '<div class="ctx">A student sits two tests. <b>Psychology</b>: mean 65, standard deviation 10. <b>Statistics</b>: mean 60, standard deviation 5. '
    'Drag each mark. The raw marks can mislead: the <b>higher $z$-score</b> is the better result <b>relative to the class</b>.</div>'
    '<div class="cols" style="grid-template-columns:1.45fr .75fr;margin-top:4px"><div class="col"><h2>Both marks on the $z$ scale</h2>'
    '<svg class="zts ix" viewBox="0 0 700 250" style="width:100%;flex:1;min-height:0"></svg>'
    '<div class="ix zsl"><span style="width:150px;color:#d00000"><b>Psychology</b></span><input data-k="p" type="range" min="35" max="95" step="1" value="75"><b class="zv" data-k="p">75</b></div>'
    '<div class="ix zsl"><span style="width:150px;color:#1f5fbf"><b>Statistics</b></span><input data-k="s" type="range" min="45" max="75" step="1" value="70"><b class="zv" data-k="s">70</b></div>'
    '<div class="ix zbtns" style="justify-content:flex-start"><button data-p="75" data-s="70">Student 1 (75, 70)</button><button data-p="55" data-s="55">Student 2 (55, 55)</button><button data-p="85" data-s="65">85 and 65</button></div></div>'
    '<div class="col"><h2>Live</h2><div class="ztso"></div></div></div>'
    f'{foot("Means, standard deviations and the two students: " + CG + ", 1H Example 30 (p. 81). Interactive by teacher.")}</section>')

# Example 30
S.append(qslide('ex', 30, 'Using standardised scores to make comparisons', 'Cambridge · Example 30',
    'Another student studying the same two subjects obtained a mark of 55 for both Psychology and Statistics. Does this mean that she performed equally well in both subjects? Use standardised marks to help you arrive at your conclusion.',
    KI_Z, [(r'Psychology: $z = \dfrac{55 - 65}{10} = -1$', 'tc:ps:101,102'), (r'Statistics: $z = \dfrac{55 - 60}{5} = -1$', 'tc:ps:101,102,201,202'),
           ('Below $z = -1$: the bottom 16% in each', 'tc:ps:101,102,201,202 ' + sh('w30', -3.6, -1, '16%') + ' ' + mk('w30', -1, 'z = −1'))],
    'Yes, her standardised score, $z = -1$, was the same for both subjects. In both subjects she finished in the bottom 16%.',
    CG + ', 1H Example 30 (p. 81); table of marks, means and standard deviations from the book.',
    fig=table_hl('ps', [('Subject', ['Mark', 'Mean', 'SD']), ('Psychology', ['75', '65', '10']), ('Statistics', ['70', '60', '5'])], 'ztab') + ncurve('w30', None, None, '', 0, small=True),
    figw='1fr', ans_do='tc:ps:101,102,201,202 ' + sh('w30', -3.6, -1, '16%') + ' ' + mk('w30', -1, 'z = −1')))
# You try (Edrolo 1I WE3)
Y30a = sh('y30', 2, 3.6, '2.5%') + ' ' + mk('y30', 2, 'Chem') + ' ' + sh('y30', -3.6, -3, '0.15%', 'o') + ' ' + mk('y30', -3, 'Phys', 'b')
S.append(qslide('yt', 30, 'Using standardised (z) scores to interpret data', 'Edrolo 1I WE3',
    'The results for a Chemistry exam were approximately normally distributed, with a mean of 71 and a standard deviation of 3. The results for a Physics exam were also approximately normally distributed, with a mean of 95 and a standard deviation of 6.',
    KI_Z, [], None, ED + ', 1I Worked example 3. Answer wording from the worked solution.',
    parts=[('a.', 'A student taking both Chemistry and Physics scored 77 in her final exam for both subjects. Did she do equally well in both exams in relation to her peers? Use standardised scores and the 68–95–99.7% rule to justify your answer.',
            [(r'Chemistry $z = \dfrac{77 - 71}{3} = 2$ · Physics $z = \dfrac{77 - 95}{6} = -3$', Y30a)],
            'No. Chemistry $z = 2$: top 2.5% of students. Physics $z = -3$: bottom 0.15%. She did not do equally well in both exams when compared to her peers.', Y30a),
           ('b.', 'Another student scores 66 on his Chemistry exam. Use standardised scores and the 68–95–99.7% rule to compare this student’s score relative to the class.',
            [(r'$z = \dfrac{66 - 71}{3} = -1.67$', 'ncl:y30 ' + sh('y30', -3.6, -1, '16%') + ' ' + mk('y30', -1.67, '66'))],
            '$z = -1.67$ places him in the bottom 16% of students.', 'ncl:y30 ' + sh('y30', -3.6, -1, '16%') + ' ' + mk('y30', -1.67, '66'))],
    fig=ncurve('y30', None, None, '', 0), figw='.62fr', cls='tight tt'))

# NL: z to percentages
S.append(nl_slide('Using standardised scores to find percentages',
    'On the $z$ scale every normal distribution looks the same. Convert values to $z$-scores, then <b>add the sections</b>. <span class="hint">Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l3', None, None, '', 0) + '</div><div class="col">'
    + st('The sections: 34, 13.5, 2.35, 0.15 on each side', do='np:l3', cls='stp')
    + st('Below $z = -1$: $13.5 + 2.35 + 0.15 = 16\\%$', do='np:l3 ' + sh('l3', -3.6, -1, '16%', 'o') + ' ' + mk('l3', -1, 'z = −1'), cls='stp')
    + st('So above $z = -1$: $100\\% - 16\\% = 84\\%$', do='np:l3 ncl:l3 ' + sh('l3', -1, 3.6, '84%') + ' ' + mk('l3', -1, 'z = −1'), cls='stp')
    + st('Read the question twice: <b>above</b> or <b>below</b>?', True, do='np:l3 ncl:l3 ' + sh('l3', -1, 3.6, '84%') + ' ' + mk('l3', -1, 'z = −1'), cls='stp') + '</div></div>',
    CG + ', 1H p. 82. Curve: teacher illustration.'))
# Example 31
S.append(qslide('ex', 31, 'Using standard scores to determine percentages', 'Cambridge · Example 31',
    'Suppose the weight of a certain species of bird is normally distributed with a mean of 42 grams with a standard deviation of 3 grams.', KI_ZP, [], None,
    CG + ', 1H Example 31 (p. 82)',
    parts=[('a', 'If a bird selected at random from this population has a standardised weight of $z = -1$, what percentage of birds in this population weigh more than this bird?',
            [('Below $z = -1$: 16%', 'nx:w31 nz:w31 np:w31 ' + mk('w31', -1, 'z = −1')), ('Above: $100\\% - 16\\%$', 'nx:w31 nz:w31 np:w31 ' + sh('w31', -1, 3.6, '84%') + ' ' + mk('w31', -1, 'z = −1'))],
            '<b>84%</b>', 'nx:w31 nz:w31 np:w31 ' + sh('w31', -1, 3.6, '84%') + ' ' + mk('w31', -1, 'z = −1')),
           ('b', 'Approximately what percentage of birds would weigh between 39 and 48 grams?',
            [(r'$z_1 = \dfrac{39 - 42}{3} = -1$, $z_2 = \dfrac{48 - 42}{3} = 2$', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b')),
             ('$34 + 34 + 13.5$', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + sh('w31', -1, 2, '') + ' ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b'))],
            '<b>81.5%</b>', 'nx:w31 nz:w31 np:w31 ncl:w31 ' + sh('w31', -1, 2, '') + ' ' + mk('w31', -1, 'z₁') + ' ' + mk('w31', 2, 'z₂', 'b'))],
    fig=ncurve('w31', 42, 3, 'weight (grams)'), figw='1.05fr', cls='tight'))
# You try (Edrolo 1H WE2)
S.append(qslide('yt', 31, 'Calculating values in normal distributions', 'Edrolo 1H WE2', HAIR, KI_ZP, [], None,
    ED + ', 1H Worked example 2. Working by teacher.',
    parts=[('a.', '97.35% of the hair lengths will fall within 12 cm and which other value?',
            [('12 cm is 2 SDs below. $13.5 + 34 + 34 + 13.5 + 2.35 = 97.35$: up to 3 SDs above', 'nx:y31 np:y31 ' + sh('y31', -2, 3, ''))], '<b>32 cm</b>', 'nx:y31 np:y31 ' + sh('y31', -2, 3, '')),
           ('b.', '2.5% of hair donated by the team will be disposed of, as it falls below a required minimum length. What is this required minimum length?',
            [('$0.15 + 2.35 = 2.5$: everything below 2 SDs under the mean', 'nx:y31 np:y31 ncl:y31 ' + sh('y31', -3.6, -2, '', 'o'))], '<b>12 cm</b>', 'nx:y31 np:y31 ncl:y31 ' + sh('y31', -3.6, -2, '', 'o'))],
    fig=ncurve('y31', 20, 4, 'length of hair donated (cm)'), figw='.8fr', cls='tight tt'))

# NL: actual scores
S.append(nl_slide('Converting standardised scores into actual scores',
    r'Make $x$ the subject: $x = \bar{x} + z \times s$. Start at the mean, step $z$ standard deviations. <span class="hint">Test marks: mean 50, standard deviation 10. Click.</span>',
    '<div class="cols" style="grid-template-columns:1.5fr .8fr"><div class="col zc">' + ncurve('l4', 50, 10, 'test mark', 0) + '</div><div class="col">'
    + st(r'$z = 1.5$: $x = 50 + 1.5 \times 10 = 65$', do='nx:l4 nz:l4 ' + mk('l4', 1.5, '65'), cls='stp')
    + st(r'$z = -2$: $x = 50 + (-2) \times 10 = 30$', do='nx:l4 nz:l4 ' + mk('l4', 1.5, '65') + ' ' + mk('l4', -2, '30', 'b'), cls='stp')
    + st('A tail % gives $z$: 16% above → $z = 1$ · 2.5% above → $z = 2$ · 0.15% above → $z = 3$ (negative below the mean)', do='nx:l4 nz:l4 ncl:l4 np:l4', cls='stp')
    + st('With $z$ and one value you can solve for $s$ or $\\bar{x}$.', True, do='nx:l4 nz:l4 ncl:l4 np:l4', cls='stp') + '</div></div>',
    CG + ', 1H pp. 83–84. Marks made up by the teacher; curve: teacher illustration.'))
S.append(qslide('ex', 32, 'Converting standard scores into actual scores', 'Cambridge · Example 32',
    r'A class test (out of 50) has a mean mark of $\bar{x} = 34$ and a standard deviation of $s = 4$. Joe’s standardised test mark was $z = -1.5$. What was Joe’s actual mark?',
    KI_X, [r'$x = \bar{x} + z \times s$', (r'$x = 34 + (-1.5) \times 4 = 34 - 6$', 'nx:w32 nz:w32 ' + mk('w32', -1.5, '28'))],
    '<b>28</b>', CG + ', 1H Example 32 (p. 83). ',
    fig=ncurve('w32', 34, 4, 'test mark'), figw='1.1fr', ans_do='nx:w32 nz:w32 ' + mk('w32', -1.5, '28')))
S.append(qslide('yt', 32, 'Calculating actual scores from standardised (z) scores', 'Edrolo 1I WE2',
    'The number of black stripes on tigers at the Royal Melbourne Zoo is known to be normally distributed with a mean of 55 and a standard deviation of 2. One of the tigers has a standardised number of stripes of $z = -2.5$. How many stripes does the tiger actually have?',
    KI_X, [r'$x = \bar{x} + z \times s$', (r'$x = 55 + (-2.5) \times 2 = 55 - 5$', 'nx:y32 nz:y32 ' + mk('y32', -2.5, '50'))],
    '<b>50 stripes</b>', ED + ', 1I Worked example 2. Working by teacher.',
    fig=ncurve('y32', 55, 2, 'number of stripes'), figw='1.1fr', ans_do='nx:y32 nz:y32 ' + mk('y32', -2.5, '50')))

# Example 33 (no You try: no matching Edrolo worked example)
W33 = 'np:w33 ' + sh('w33', 2, 3.6, '', 'o') + ' ' + mk('w33', 2, '11.4 m (2.5% above)')
S.append(qslide('ex', 33, 'Finding the standard deviation given the mean and one percentage', 'Cambridge · Example 33',
    'Suppose the heights of red flowering gum trees have a mean of 10.2 metres, and 2.5% of these trees grow to more than 11.4 metres tall. Assuming that the heights of these trees are approximately normally distributed, what is the standard deviation of the height of the red flowering gum trees?',
    KI_X, [('2.5% above, so 11.4 m is at $z = 2$', W33), (r'$x = \bar{x} + z \times s$: $11.4 = 10.2 + 2 \times s$', W33), (r'$2s = 1.2$, so $s = 0.6$', W33)],
    '<b>0.6 metres</b>', CG + ', 1H Example 33 (p. 84). No matching Edrolo worked example, so no You try.',
    fig=ncurve('w33', None, None, '', 0), figw='1fr', ans_do=W33))
# Example 34
W34a = 'np:w34 ' + sh('w34', -3.6, -2, '2.5%', 'o') + ' ' + mk('w34', -2, '20', 'b')
W34 = W34a + ' ' + sh('w34', 1, 3.6, '16%') + ' ' + mk('w34', 1, '80')
S.append(qslide('ex', 34, 'Finding the mean and standard deviation', 'Cambridge · Example 34',
    'The marks scored in an examination are known to be approximately normally distributed. If 16% of students score more than 80 marks, and 2.5% of students score less than 20 marks, estimate the mean and standard deviation of this distribution.',
    KI_X, [('2.5% below 20, so 20 is at $z = -2$: $\\bar{x} - 2s = 20$ (1)', W34a), ('16% above 80, so 80 is at $z = 1$: $\\bar{x} + s = 80$ (2)', W34),
           ('(2) − (1): $3s = 60$, so $s = 20$', W34), (r'Substitute: $\bar{x} - 2 \times 20 = 20$, so $\bar{x} = 60$', W34)],
    r'$\boldsymbol{\bar{x} = 60}$ marks, $\boldsymbol{s = 20}$ marks', CG + ', 1H Example 34 (p. 84). Working by teacher, following the book.',
    fig=ncurve('w34', None, None, '', 0), figw='1fr', ans_do=W34, cls='tight'))
# You try (Edrolo 1H WE3)
S.append(qslide('yt', 34, 'Determining the mean and standard deviation of a normal distribution', 'Edrolo 1H WE3',
    'Duncan’s light bulb factory produces light bulbs.<br>The <i>lifetime</i> of their light bulbs are approximately normally distributed. It is known that approximately 95% of the light bulbs have a <i>lifetime</i> ranging from 800 hours to 1600 hours.',
    KI_X, [], None, ED + ', 1H Worked example 3. Working by teacher.',
    parts=[('a.', 'Calculate the standard deviation for the <i>lifetime</i> of a light bulb.',
            [('95%: 800 h is at $z = -2$, 1600 h at $z = 2$, four SDs apart', sh('y34', -2, 2, '95%') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600')),
             ('$1600 - 800 = 800 = 4s$', None)], '$s = 800 \\div 4 =$ <b>200 hours</b>', sh('y34', -2, 2, '95%') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600')),
           ('b.', 'Calculate the mean <i>lifetime</i> of a light bulb.',
            [('The mean is in the middle: $800 + 2 \\times 200$', sh('y34', -2, 2, '') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600') + ' ' + mk('y34', 0, '1200', 'g'))],
            '<b>1200 hours</b>', sh('y34', -2, 2, '') + ' ' + mk('y34', -2, '800', 'b') + ' ' + mk('y34', 2, '1600') + ' ' + mk('y34', 0, '1200', 'g'))],
    fig=ncurve('y34', None, None, '', 0), figw='.75fr', cls='tight'))

# NL: 1I populations and samples
SMP = (3, 8, 17, 22, 29, 36, 41, 48, 52, 57)
dots = ''.join(f'<circle cx="{40 + (k % 15) * 56}" cy="{36 + (k // 15) * 50}" r="15" fill="#c9d6f2"/>' for k in range(60))
sdots = ''.join(f'<circle cx="{40 + (k % 15) * 56}" cy="{36 + (k // 15) * 50}" r="17" fill="#d98a1f" stroke="#000" stroke-width="2"/>' for k in SMP)
S.append(nl_slide('1I Populations and samples',
    'The <b>population</b> is every member of the group we want to know about. Measuring them all is usually too slow or costly, so we measure a <b>sample</b>: a subset of the population. <span class="hint">Click.</span>',
    '<div class="cols" style="grid-template-columns:1.4fr .9fr"><div class="col zc"><svg class="zpop" viewBox="0 0 880 230" style="width:100%">'
    f'<rect x="4" y="4" width="872" height="200" rx="18" fill="none" stroke="#1f5fbf" stroke-width="3"/>{dots}<g class="zsmp" style="opacity:0;transition:opacity .4s">{sdots}</g>'
    '<text x="440" y="226" text-anchor="middle" font-size="18" font-weight="bold" fill="#1f5fbf">population: all 60 members</text></svg></div><div class="col">'
    + st('Pick a sample <b>at random</b>: every member has the same chance of being chosen.', do='smp:on', cls='stp')
    + st('The sample mean $\\bar{x}$ and standard deviation $s$ are used to <b>estimate</b> the population values.', do='smp:on', cls='stp')
    + st('A different random sample gives slightly different statistics.', do='smp:on', cls='stp')
    + st('Population = everyone · sample = the ones we measure.', True, do='smp:on', cls='stp') + '</div></div>',
    CG + ', 1I Populations and samples (Interactive Textbook only), summarised in own words. Picture: teacher illustration.'))

# Exit tasks (short-answer exam questions)
E1 = 'nx:e1 ' + mk('e1', 0, '9.4') + ' ' + sh('e1', 0, 3.6, '50%')
S.append(qslide('exit', '1 of 2', 'Show what you know', 'VCAA 2019 Exam 2 Q2b',
    'The <i>temperature difference</i> between the <i>minimum daily temperature</i> and the <i>maximum daily temperature</i> in November 2017 at a location is approximately normally distributed with a mean of 9.4 °C and a standard deviation of 3.2 °C.'
    '<br>Determine the number of days in November 2017 for which this <i>temperature difference</i> is expected to be greater than 9.4 °C.',
    KI_RULE, [('9.4 °C is the mean: half of the days are above it', E1), ('November has 30 days: $50\\% \\times 30$', E1)],
    '<b>15 days</b>', ED + ', 1H Q12 (VCAA 2019 Exam 2 Data analysis Q2b); % and comment from the examiner report. Working by teacher.',
    marks=1, vcaa=58, figw='1.15fr', fig=ncurve('e1', 9.4, 3.2, 'temperature difference (°C)', 1, z=False, small=True), ans_do=E1, watch='Some gave the percentage of 50% rather than the number of days. <span class="zsc">(examiner report)</span>'))
S.append(qslide('exit', '2 of 2', 'Show what you know', 'VCAA 2021 Exam 2 Q1c',
    'In the sport of heptathlon, athletes compete in seven events.<br>These events are the 100 m hurdles, high jump, shot-put, javelin, 200 m run, 800 m run and long jump.<br>'
    'In shot-put, athletes throw a heavy spherical ball (a shot) as far as they can.<br>Fifteen female athletes competed to qualify for the heptathlon at the Olympic Games.<br>'
    'For shot-put, athlete number six, Jamilia, threw the shot 14.50 m.<br>The table shows the mean and standard deviation of the shot-put results for the 15 athletes.'
    + table_hl('sp', [('statistic', ['<i>shot-put</i> (metres)']), ('mean', ['13.74']), ('standard deviation', ['1.43'])], 'ztab zsm')
    + 'Calculate Jamilia’s standardised score (<i>z</i>).<br>Round your answer to one decimal place.',
    KI_Z, [('$x = 14.50$, $\\bar{x} = 13.74$, $s = 1.43$', 'tc:sp:100,200'), (r'$z = \dfrac{14.50 - 13.74}{1.43} = 0.531\ldots$', 'tc:sp:100,200')],
    '$\\boldsymbol{z = 0.5}$', ED + ', 1I Q13 (VCAA 2021 Exam 2 Data analysis Q1c); % from the examiner report. Working by teacher.',
    marks=1, vcaa=78, figw='1.25fr', ans_do='tc:sp:100,200', watch='Round only at the end, to one decimal place: 0.531… → 0.5. <span class="zsc">(teacher note)</span>'))

checkin(SC, "Success criteria: planner card")
coursework('1H–1I', 'Coursework · Exercises 1H, 1I', [('Cambridge Exercise 1H', 'Q1–23'), ('Cambridge Exercise 1I', 'Interactive Textbook (Cambridge GO)'), ('Practice booklet', '1H section')],
           'Exercise 1H: The normal distribution and the 68–95–99.7% rule', CG + ", Exercises 1H and 1I")



# ---- lesson-only CSS / JS (everything shared lives in lib/)
LESSON_CSS = r'''
.ztso{font-size:21px;line-height:1.55}.ztso .v{font-size:17px;border:2px solid #000;background:#fff7d6;padding:8px 10px;margin-top:10px;line-height:1.35}
.slide.tt .st.zs{font-size:18px!important;margin-bottom:4px!important}.slide.tt .zpq{font-size:17px;margin-bottom:4px}.slide.tt .top>.q{font-size:19px;line-height:1.3}.slide.tt .st.zs .katex{font-size:1.02em}
.zv{width:42px;text-align:right;font-size:22px}
.slide.nl .stp{white-space:normal;font-size:21px;line-height:1.35;color:#000;margin:0 0 14px!important}
.slide.nl .stp.final{color:#d00000}
'''
LESSON_JS = r'''
(function(){const {PX,PY,BASE,mark}=window.ZN;
// two tests: Psychology (mean 65, sd 10) vs Statistics (mean 60, sd 5)
const BELOW={'-3':0.15,'-2':2.5,'-1':16,'0':50,'1':84,'2':97.5,'3':99.85};
const below=z=>{if(Number.isInteger(z))return `${BELOW[z]}% of the class scored lower`;const lo=Math.floor(z),hi=Math.ceil(z);return `between ${BELOW[lo]}% and ${BELOW[hi]}% of the class scored lower`};
document.querySelectorAll('.slide.ztwo').forEach(sl=>{const sv=sl.querySelector('svg.zts'),O=sl.querySelector('.ztso'),I={};sl.querySelectorAll('input').forEach(i=>I[i.dataset.k]=i);
  const go=()=>{const p=+I.p.value,s=+I.s.value,zp=Math.round((p-65)/10*100)/100,zs=Math.round((s-60)/5*100)/100;
    sl.querySelectorAll('.zv').forEach(v=>v.textContent=I[v.dataset.k].value);
    let g='';for(let k=-3;k<=3;k++)g+=`<line x1="${PX(k)}" y1="${PY(k)}" x2="${PX(k)}" y2="${BASE}" stroke="#999" stroke-dasharray="4 4"/><text x="${PX(k)}" y="${BASE+22}" font-size="16" fill="#1f5fbf" text-anchor="middle">${k}</text>`;
    let d='';for(let z=-3.6;z<=3.601;z+=0.05)d+=(d?'L':'M')+PX(z).toFixed(1)+' '+PY(z).toFixed(1);
    g+=`<path d="${d}" fill="none" stroke="#000" stroke-width="3"/><line x1="20" y1="${BASE}" x2="680" y2="${BASE}" stroke="#000" stroke-width="2"/><text x="16" y="${BASE+22}" font-size="16" font-weight="bold" fill="#1f5fbf">z</text>`;
    const same=Math.abs(zp-zs)<1e-9;g+=mark(zp,'r','Psych'+(same?' = Stats':''));if(!same)g+=mark(zs,'b','Stats');sv.setAttribute('viewBox','0 0 700 250');sv.innerHTML=g;
    const f=z=>(z>0?'+':'')+(+z.toFixed(2));
    O.innerHTML=`<b style="color:#d00000">Psychology</b> ${p}: $z = \\dfrac{${p} - 65}{10} = ${f(zp)}$<br><span style="font-size:16px">${below(zp)}</span><br>`+
      `<b style="color:#1f5fbf">Statistics</b> ${s}: $z = \\dfrac{${s} - 60}{5} = ${f(zs)}$<br><span style="font-size:16px">${below(zs)}</span>`+
      `<div class="v">${same?'<b>Equal z-scores:</b> equally well in both, relative to each class.':(zp>zs?'<b>Psychology</b> was the better result relative to the class'+(p<s?' (even though the raw mark is lower).':'.'):'<b>Statistics</b> was the better result relative to the class'+(s<p?' (even though the raw mark is lower).':'.'))}</div>`;
    O.innerHTML=O.innerHTML.replace(/−/g,'-');if(window.renderMathInElement)renderMathInElement(O,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false})};
  Object.values(I).forEach(i=>{i.oninput=go;i.onclick=e=>e.stopPropagation()});
  sl.querySelectorAll('.zbtns button').forEach(b=>b.onclick=e=>{e.stopPropagation();I.p.value=b.dataset.p;I.s.value=b.dataset.s;go()});
  if(document.readyState==='complete')go();else window.addEventListener('load',go)});
})();
'''

build('S5-slides.html', '12MAG S5 · The normal distribution and standardised scores · Slides', css=LESSON_CSS, js=LESSON_JS)
