"""Prefill the Chapter 10 lesson cards (gm12-u4-10a10b, -10c, -10d, -10e, -10f10g) - queue task AoS3 #2, 16 Nov 2026 (runner).
Learning intentions, success criteria, Study Design points and coursework were set by tools/plan_ch10.py (AoS3 #1) and are kept.
Sources checked: Cambridge U3&4 2023 Ch 10 (Examples 1-32, pp. 474-541, chapter skills checklist), Edrolo U3&4 2023 Ch 7
worked examples (7A WE1-4, 7B WE1-3, 7C WE1-4, 7D WE1-3, 7E WE1-3, 7F WE1-2) and exam practice (7A-7F),
Edrolo U1&2 2023 Ch 5 worked examples (5A-5F) and exam practice, tools/y11_cambridge_skills_checklist.csv (Cambridge U1&2 Ch 4),
tools/vcaa_current_index.csv, tools/ledger*.csv (burnt; read from origin 16 Nov 01:45).
No Edrolo (U3&4 or U1&2) WE matches Cambridge Ex 8 (credit card -> matrix), 10 (interpreting a road-network matrix),
15 (zero matrix), 16 (processing sales data), 19 (row x column by hand), 24 (showing two matrices are inverses),
30 (inverse of a permutation matrix) -> written You trys YT-10B-8, YT-10B-10, YT-10C-15, YT-10C-16, YT-10D-19, YT-10E-24, YT-10F-30.
Exit / APK duplicates of the same VCAA original across books were avoided (e.g. 2018 E1 Matrices Q1 = Edrolo U3&4 7D Q15
= U1&2 5E Q14; 2020 E2 Matrices Q2 = U3&4 7D Q16 = U1&2 5E Q15; 2018 E1 Matrices Q2 = U3&4 7C Q18 = U1&2 5C Q18).
Do Now: current-design items only from content already taught (AoS 1 + earlier Ch 10 subchapters); AoS 2 (Ch 7-8) items left
for the AoS 2 runner.
"""
import json, csv
P='planner/unit-plan.json'; d=json.load(open(P))
L={}
for a in d['aos']:
    for ch in a['chapters']:
        for l in ch['lessons']: L[l['id']]=l

def dn(*items): return [{'exam':e,'ref':r,'sec':s} for e,r,s in items]
def we(n,sub,title,yt): return {'n':n,'sub':sub,'title':title,'youTry':yt,'video':f'Cambridge GO · {sub} Resources'}
def sk(sec,n,text): return {'kind':'Skill','ref':f'Cambridge U1&2 {sec} checklist #{n}','text':text}
def ex(ref,src): return {'ref':ref,'src':src}
W=lambda n,sub: f'Written (modelled on Cambridge Ex {n}) · YT-{sub}-{n}'

C={}
C['gm12-u4-10a10b']=dict(
 keyVocab=['Matrix: a rectangular array of numbers (elements) in rows and columns',
   'Order: rows × columns (a 2 × 3 matrix has 2 rows and 3 columns)',
   'aᵢⱼ: the element in row i, column j',
   'Row, column, square, zero, identity (I), diagonal, symmetric, upper/lower triangular matrices',
   'Transpose Aᵀ: rows become columns'],
 weDo=[we(1,'10A','The order of a matrix','Edrolo 7A WE1a'),
   we(2,'10A','The transpose of a matrix','Edrolo 7B WE3'),
   we(3,'10A','Matrix facts (row, column, square)','Edrolo U1&2 5A WE2'),
   we(4,'10A','Types of matrices','Edrolo 7A WE2'),
   we(5,'10A','Identifying the elements in a matrix','Edrolo 7A WE1b'),
   we(6,'10A','Constructing a matrix given a rule for its ijth term','Edrolo 7A WE4'),
   we(7,'10B','Representing information in a table by a matrix','Edrolo 7A WE3a–b'),
   we(8,'10B','Entering a credit card number into a matrix',W(8,'10B')),
   we(9,'10B','Representing a network diagram by a matrix','Edrolo U1&2 5D WE3a'),
   we(10,'10B','Interpreting a matrix representing a network diagram',W(10,'10B'))],
 apk=[sk('4A',1,'I can state the order of a given matrix.'),
   sk('4A',2,'I can describe the location of an element in a matrix.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5A Q13','text':'VCAA 2020 Exam 1 Matrices Q6 (adapted by Edrolo; 73%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q2','1F'),('Exam 1','VCAA 2024 Exam 1 Q15','5B'),
   ('Exam 2','VCAA 2024 Exam 2 Q2a','1C'),('Exam 2','VCAA 2026 Exam 2 Q3a','1H')),
 exit=[ex('Edrolo U3&4 7A Q12','VCAA 2018 Exam 2 Matrices Q1'),ex('Edrolo U3&4 7B Q15','VCAA 2017 Exam 1 Matrices Q6')],
 cas=['matrix-entry'], casYouTry='Cambridge CAS 1 (entering a matrix) with the Example 4 matrices',
 note='Edrolo 7A WE3c (interpreting a sum) is a spare You try for Example 10d–e.')

C['gm12-u4-10c']=dict(
 keyVocab=['Equal matrices: same order and every pair of corresponding elements equal',
   'A + B and A − B are only defined when A and B have the same order: add/subtract corresponding elements',
   'Scalar multiplication kA: multiply every element by k',
   'Zero matrix O: every element is 0 (A + O = A, A − A = O)'],
 weDo=[we(11,'10C','Equality of two matrices','Edrolo U1&2 5B WE3'),
   we(12,'10C','Adding two matrices','Edrolo U1&2 5B WE2'),
   we(13,'10C','Subtracting two matrices','Edrolo 7B WE1 (defined? then A − B)'),
   we(14,'10C','Scalar multiplication','Edrolo 7B WE2'),
   we(15,'10C','The zero matrix',W(15,'10C')),
   we(16,'10C','Processing data using addition, subtraction and scalar multiplication',W(16,'10C'))],
 apk=[sk('4B',3,'I can add and subtract matrices.'),
   sk('4C',6,'I can apply scalar multiplication with addition and subtraction of matrices.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5B Q15','text':'VCAA 2021 Exam 2 Matrices Q1b (adapted by Edrolo; 50%)'}],
 doNow=dn(('Exam 1','VCAA 2023 Exam 1 Q29','10A'),('Exam 1','VCAA 2025 Exam 1 Q8','2I'),
   ('Exam 2','VCAA 2024 Exam 2 Q9a','10A'),('Exam 2','VCAA 2025 Exam 2 Q4e','2E')),
 exit=[ex('Edrolo U3&4 7B Q13','VCAA 2019 Exam 1 Matrices Q1'),ex('Edrolo U3&4 7B Q14','VCAA 2016 Exam 1 Matrices Q1')],
 cas=['matrix-operations'], casYouTry='Edrolo 7B WE2 Method 2 (3C on CAS)',
 note='Edrolo U1&2 5B WE1 (is A + B defined?) and WE5 (find a in a scalar matrix equation) are spare You trys for Examples 12 and 11.')

C['gm12-u4-10d']=dict(
 keyVocab=['AB is defined when columns of A = rows of B; the order of AB is (rows of A) × (columns of B)',
   'Multiply row by column: multiply matching elements and add',
   'Order matters: AB ≠ BA in general',
   'Summing matrix: a row or column matrix of 1s; A × column of 1s sums the rows, row of 1s × A sums the columns',
   'Powers: A² = A × A (A must be square)'],
 weDo=[we(17,'10D','Is a matrix product defined?','Edrolo 7C WE1'),
   we(18,'10D','Determining the order of a matrix product','Edrolo U1&2 5C WE1'),
   we(19,'10D','Multiplying a row matrix by a column matrix (by hand)',W(19,'10D')),
   we(20,'10D','Multiplying a rectangular matrix by a column matrix (by hand)','Edrolo 7C WE2'),
   we(21,'10D','Using matrix multiplication to sum the rows and columns of a matrix','Edrolo 7C WE3'),
   we(22,'10D','A practical application of matrix multiplication','Edrolo U1&2 5D WE1'),
   we(23,'10D','Evaluating matrix expressions involving powers','Edrolo 7C WE4')],
 apk=[sk('4D',7,'I can determine if matrix multiplication is possible for two matrices.'),
   sk('4D',9,'I can perform matrix multiplication by hand.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5C Q16','text':'VCAA 2020 Exam 1 Matrices Q2 (79%)'}],
 doNow=dn(('Exam 1','VCAA 2024 Exam 1 Q26','10C'),('Exam 1','VCAA 2024 Exam 1 Q8','3A'),
   ('Exam 2','VCAA 2024 Exam 2 Q9c','10C'),('Exam 2','VCAA 2026 Exam 2 Q5b','3B')),
 exit=[ex('Edrolo U3&4 7C Q17','VCAA 2017 Exam 2 Matrices Q1a'),ex('Edrolo U3&4 7C Q18','VCAA 2018 Exam 1 Matrices Q2')],
 cas=['matrix-operations'], casYouTry='Edrolo 7C WE2 Method 2 (PQ on CAS)',
 note='Edrolo U1&2 5C WE2 (XY by hand), 5C WE3 (B²) and 5D WE2 (carnival snacks) are spare You trys for Examples 20, 23 and 22.')

C['gm12-u4-10e']=dict(
 keyVocab=['Identity matrix I: 1s on the leading diagonal, 0s elsewhere; AI = IA = A',
   'A and B are inverses if AB = BA = I; the inverse of A is A⁻¹',
   'Determinant of [a b; c d] = ad − bc',
   'det(A) = 0 → A is singular: no inverse',
   'AX = B → X = A⁻¹B (pre-multiply); XA = B → X = BA⁻¹ (post-multiply)'],
 weDo=[we(24,'10E','Demonstrating that two matrices are inverses',W(24,'10E')),
   we(25,'10E','Finding the determinant of a 2 × 2 matrix','Edrolo 7D WE1a'),
   we(26,'10E','Using the rule to find the inverse of a 2 × 2 matrix','Edrolo 7D WE2'),
   we(27,'10E','Solving matrix equations','Edrolo U1&2 5F WE1')],
 apk=[sk('4D',11,'I can identify and construct an identity matrix of a given size.'),
   sk('4E',12,'I can find the inverse of a matrix.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5F Q15','text':'VCAA 2017 Exam 2 Matrices Q1ci (60%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q26','10D'),('Exam 1','VCAA 2026 Exam 1 Q1','1F'),
   ('Exam 2','VCAA 2023 Exam 2 Q9b','10D'),('Exam 2','VCAA 2025 Exam 2 Q6a','5A')),
 exit=[ex('Edrolo U3&4 7D Q15','VCAA 2018 Exam 1 Matrices Q1'),ex('Edrolo U3&4 7D Q16','VCAA 2020 Exam 2 Matrices Q2'),
   ex('Edrolo U3&4 7D Q17','VCAA 2016 Exam 1 Matrices Q3')],
 cas=['matrix-det-inverse'], casYouTry='Edrolo 7D WE1b (determinant on CAS)',
 note='Edrolo 7D WE3 (simultaneous equations with matrices) and U1&2 5F WE2 (AX = B) are spare You trys for Example 27. U1&2 5E WE1–3 are spares for Examples 25–26.')

C['gm12-u4-10f10g']=dict(
 keyVocab=['Binary matrix: every element is 0 or 1',
   'Permutation matrix: a square binary matrix with exactly one 1 in each row and column; PA reorders the rows of A, AP the columns',
   'P⁻¹ = Pᵀ for a permutation matrix',
   'Communication matrix: 1 = a one-step (direct) link; C² counts two-step links; C + C² = one- and two-step links',
   'Dominance matrix: 1 = row player dominates column player; rank by row sums of D (then D + D² if tied)'],
 weDo=[we(28,'10F','Applying a permutation matrix','Edrolo 7E WE1'),
   we(29,'10F','Finding a permutation matrix','Edrolo 7E WE3'),
   we(30,'10F','The inverse of a permutation matrix',W(30,'10F')),
   we(31,'10F','Constructing a communication matrix','Edrolo 7F WE1'),
   we(32,'10G','Determining dominance','Edrolo 7F WE2')],
 apk=[sk('4F',14,'I can represent a road network in a matrix.'),
   sk('4F',15,'I can summarise relationships in a network in a matrix.'),
   {'kind':'Exam','ref':'Edrolo U1&2 5D Q14','text':'VCAA 2019 Exam 1 Matrices Q7 (adapted by Edrolo; 54%)'}],
 doNow=dn(('Exam 1','VCAA 2025 Exam 1 Q27','10E'),('Exam 1','VCAA 2024 Exam 1 Q13','5C'),
   ('Exam 2','VCAA 2025 NHT Exam 2 Q11b','10E'),('Exam 2','VCAA 2023 Exam 2 Q1bi','1F')),
 exit=[ex('Edrolo U3&4 7E Q9','VCAA 2018 Exam 1 Matrices Q4'),ex('Edrolo U3&4 7E Q10','VCAA 2020 Exam 1 Matrices Q3'),
   ex('Edrolo U3&4 7F Q12','VCAA 2017 Exam 1 Matrices Q5'),ex('Edrolo U3&4 7F Q13','VCAA 2021 Exam 2 Matrices Q2')],
 cas=['matrix-operations'], casYouTry='Edrolo 7F WE1b (C + C² on CAS)',
 note='Edrolo 7E WE2 (row permutation) and U1&2 5D WE3 are spare You trys for Examples 28 and 31. Spare exits (not reserved): Edrolo 7E Q8 (VCAA 2016 E1 Matrices Q2), 7E Q11 (VCAA 2019 E2 Matrices Q2d, 20%).')

for i,c in C.items():
    card=L[i]['card']
    for k in ['keyVocab','weDo','apk','doNow','exit','cas']: card[k]=c[k]
    for k in ['casYouTry','note']:
        if k in c: card[k]=c[k]
json.dump(d,open(P,'w'),indent=1,ensure_ascii=False)

# written You trys
WY='planner/written-youtrys.json'; w=json.load(open(WY))
lab=lambda n:f'Written for 12MAG (Claude, modelled on Cambridge Example {n})'
new=[
 {'id':'YT-10B-8','pairs':'Cambridge U3&4 Example 8','sub':'10B','label':lab(8),
  'text':'Convert the 16-digit credit card number: 5213 7046 9381 2750 into a 2 × 8 matrix, listing the digits in pairs, one under the other. Ignore the spaces.',
  'answer':'[5 1 7 4 9 8 2 5; 2 3 0 6 3 1 7 0]'},
 {'id':'YT-10B-10','pairs':'Cambridge U3&4 Example 10','sub':'10B','label':lab(10),
  'text':'The roads connecting four towns, town P, town Q, town R and town S, have been represented by a 4 × 4 matrix, M. The elements show the number of roads between each pair of towns. M = [0 2 1 0; 2 0 0 1; 1 0 0 3; 0 1 3 0] (rows and columns in the order P, Q, R, S). a In the matrix M, m₁₄ = 0. What does this tell us? b In the matrix M, m₃₄ = 3. What does this tell us? c What is the sum of the elements in row 2 of matrix M and what does this tell us? d What is the sum of all the elements of matrix M and what does this tell us?',
  'answer':'a There is no road between town P and town S. b There are three roads between town R and town S. c 3: the total number of roads between town Q and the other towns in the network. d 14: the total number of different ways you can travel between towns.'},
 {'id':'YT-10C-15','pairs':'Cambridge U3&4 Example 15','sub':'10C','label':lab(15),
  'text':'G = [4 0; −2 6], H = [6 0; −3 9]. Show that 3G − 2H = O.',
  'answer':'3G − 2H = [12 0; −6 18] − [12 0; −6 18] = [0 0; 0 0], so 3G − 2H = O.'},
 {'id':'YT-10C-16','pairs':'Cambridge U3&4 Example 16','sub':'10C','label':lab(16),
  'text':'The bread sales (small, medium, large loaves) for two bakeries are displayed below. 2024: Corner Bake 18, 25, 9; Daily Loaf 27, 22, 14. 2025: Corner Bake 22, 30, 12; Daily Loaf 28, 26, 16. a Construct two matrices, A and B, to represent the sales data for 2024 and 2025 separately. b Construct a new matrix C = A + B. What does this matrix represent? c Construct a new matrix, D = B − A. What does this matrix represent? d Both bakeries want to increase their 2025 sales by 50% by 2026. Construct a new matrix E = 1.5B. Explain why this matrix represents the planned sales figures for 2026.',
  'answer':'a A = [18 25 9; 27 22 14], B = [22 30 12; 28 26 16]. b C = [40 55 21; 55 48 30]: the total sales for 2024 and 2025 for the two bakeries. c D = [4 5 3; 1 4 2]: the increase in sales from 2024 to 2025 for the two bakeries. d E = [33 45 18; 42 39 24]: each 2025 figure is multiplied by 1.5 (a 50% increase), giving the planned 2026 sales.'},
 {'id':'YT-10D-19','pairs':'Cambridge U3&4 Example 19','sub':'10D','label':lab(19),
  'text':'Evaluate the matrix product AB, where A = [2 1 3] and B = [5; 2; 4].',
  'answer':'1 × 3 times 3 × 1: defined, order 1 × 1. AB = [2 × 5 + 1 × 2 + 3 × 4] = [24].'},
 {'id':'YT-10E-24','pairs':'Cambridge U3&4 Example 24','sub':'10E','label':lab(24),
  'text':'Show that the matrices A = [3 5; 1 2] and B = [2 −5; −1 3] are inverses.',
  'answer':'AB = [3×2 + 5×(−1)  3×(−5) + 5×3; 1×2 + 2×(−1)  1×(−5) + 2×3] = [1 0; 0 1] = I and BA = [2×3 + (−5)×1  2×5 + (−5)×2; −1×3 + 3×1  −1×5 + 3×2] = [1 0; 0 1] = I, so A and B are inverses.'},
 {'id':'YT-10F-30','pairs':'Cambridge U3&4 Example 30','sub':'10F','label':lab(30),
  'text':'A 4 × 4 permutation matrix P = [0 1 0 0; 0 0 0 1; 1 0 0 0; 0 0 1 0] applied to a 4 × 1 column matrix A gives the column matrix [K; L; M; N]. Determine the matrix A.',
  'answer':'PA = [K; L; M; N], so A = P⁻¹[K; L; M; N] = Pᵀ[K; L; M; N] = [M; K; N; L].'},
]
ids={x['id'] for x in w['items']}
w['items']+=[x for x in new if x['id'] not in ids]
json.dump(w,open(WY,'w'),indent=1,ensure_ascii=False)

# CAS skills (new for Ch 10; Draft)
CS='planner/cas-skills.json'; cs=json.load(open(CS)); S=cs['skills']
have={k['id'] for k in S}
NEW=[
 {'id':'matrix-entry','skill':'Entering and storing a matrix (and its transpose)','subs':['10A','10B'],
  'ti':['Calculator page: press the template key (beside 9) and choose the m × n matrix template; enter the number of rows and columns; OK.',
        'Type the elements, using tab to move between them.',
        'Store it: press ctrl var (sto→), type a letter (e.g. a) and press enter.',
        'Transpose: type a then Menu › Matrix & Vector › Transpose (shows aᵀ) and press enter.'],
  'classpad':['Main application: open the Keyboard › Math2 tab and tap the matrix template; tap the add-row / add-column buttons until the order is right.',
        'Type the elements, tapping each cell.',
        'Store it: tap ⇒ and type a letter (e.g. A), then EXE.',
        'Transpose: Action › Matrix › Create › trn, type trn(A) and press EXE.'],
  'tip':'Check the order (rows × columns) on screen before storing; a stored letter keeps its matrix until you overwrite it.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 10A CAS 1 + Edrolo 7B WE3 (Draft, check against 02 Sources\\CAS guides)'},
 {'id':'matrix-operations','skill':'Matrix arithmetic: sum, difference, scalar multiple, product and power','subs':['10C','10D','10F','10G'],
  'ti':['Enter and store each matrix (see Entering and storing a matrix).',
        'Type the calculation with the stored letters, e.g. a+b, a−b, 3·a, a·b (use ×) or a^2, and press enter.',
        '"Error: Dimension" means the operation is not defined for those orders.'],
  'classpad':['Enter and store each matrix (see Entering and storing a matrix).',
        'Type the calculation with the stored letters, e.g. A+B, A−B, 3A, A×B or A^2, and press EXE.',
        '"Dimension ERROR" means the operation is not defined for those orders.'],
  'tip':'Order matters for products: a·b and b·a are usually different (or one is not defined).',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 10C CAS 2, 10D CAS 3-4 + Edrolo 7B WE2, 7C WE2 Method 2 (Draft, check against 02 Sources\\CAS guides)'},
 {'id':'matrix-det-inverse','skill':'Determinant and inverse of a matrix; solving AX = B','subs':['10E'],
  'ti':['Enter and store the matrix (e.g. as a).',
        'Determinant: Menu › Matrix & Vector › Determinant, type det(a) and press enter.',
        'Inverse: type a^-1 and press enter ("Singular matrix" means det = 0, no inverse).',
        'Solve AX = B: type a^-1·b (pre-multiply); for XA = B type b·a^-1.'],
  'classpad':['Enter and store the matrix (e.g. as A).',
        'Determinant: Action › Matrix › Calculation › det, type det(A) and press EXE.',
        'Inverse: type A^-1 and press EXE (an error means det = 0, no inverse).',
        'Solve AX = B: type A^-1×B (pre-multiply); for XA = B type B×A^-1.'],
  'tip':'Find det first: if it is 0 the matrix has no inverse.',
  'videos':{'ti':[],'classpad':[]},'checked':'Cambridge U3&4 10E CAS 5 + Edrolo 7D WE1b, WE2 (Draft, check against 02 Sources\\CAS guides)'},
]
S+=[k for k in NEW if k['id'] not in have]
json.dump(cs,open(CS,'w'),indent=1,ensure_ascii=False)

V='planner/videos.json'; v=json.load(open(V))
have={x['sub'] for x in v['videos']}
for s,t in [('10A','What is a matrix?'),('10B','Using matrices to represent information'),
            ('10C','Matrix arithmetic: addition, subtraction and scalar multiplication'),('10D','Matrix arithmetic: the product of two matrices'),
            ('10E','Matrix inverse, the determinant and matrix equations'),('10F','Binary, permutation and communication matrices'),
            ('10G','Dominance matrices')]:
    if s not in have: v['videos'].append({'sub':s,'title':t,'channel':'MaffsGuru (Darren Smyth)','url':'','length':'','page':'','status':'draft','note':'find the matching MaffsGuru General Maths U3&4 video (link not checked yet)'})
json.dump(v,open(V,'w'),indent=1,ensure_ascii=False)

# reserve exam items (ledger_manual.csv): Do Now + exits + APK exam items + Cambridge APK skills
rows=[]
for i,c in C.items():
    for x in c['doNow']: rows.append((x['ref'].replace('Exam ','E'),'','Do Now',i))
    for x in c['exit']: rows.append((x['src'].replace('Exam ','E'),x['ref'],'exit',i))
    for x in c['apk']:
        if x['kind']=='Exam': rows.append((x['text'].split(' (')[0].replace('Exam ','E'),x['ref'],'APK',i))
        else:
            sec,num=x['ref'].split()[2],x['ref'].split()[-1]
            rows.append((f'Cambridge U1&2 skills checklist {sec} {num}','','APK',i))
M='tools/ledger_manual.csv'
old=open(M).read()
items_old={l.split(',')[0] for l in old.splitlines()}
with open(M,'a',newline='') as f:
    if not old.endswith('\n'): f.write('\n')
    wr=csv.writer(f)
    for item,via,role,where in rows:
        if item in items_old: print('ALREADY IN LEDGER:',item); continue
        wr.writerow([item,via,role,'yes',where,'2026-11-16','reserved by AoS3 prefill'])
print('ok', len(rows))
