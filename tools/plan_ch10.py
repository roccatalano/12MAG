"""AoS3 #1: plan Chapter 10 (Matrices) lessons in planner/unit-plan.json.
Split (16 Nov runner): 10A+10B+10C (16 Examples) was too much for one lesson, and 10G
(1 Example) too little: lessons are now 10A-10B · 10C · 10D · 10E · 10F-10G (still 5).
Learning intentions = Cambridge U3&4 (2023) subchapter 'Learning intentions';
success criteria = Cambridge Chapter 10 skills checklist (items 1-33, 10G item added from the textbook checklist);
coursework = Cambridge exercises by section heading (pp. 478-541)."""
import json
P='planner/unit-plan.json'
LI={
'10A':["To be able to state the order of a given matrix.","To be able to describe the location of an element in a matrix.","To be able to determine the transpose of a matrix.","To be able to define and recognise diagonal, symmetric and triangular matrices.","To be able to define and recognise identity matrices."],
'10B':["To be able to represent data given in a table by a matrix.","To be able to represent a network diagram with a matrix."],
'10C':["To be able to establish when two matrices are equal.","To be able to recognise when matrix addition and subtraction are defined and to perform these operations.","To be able to undertake scalar multiplication.","To be able to identify zero matrices.","To be able to undertake addition, subtraction and multiplication by a scalar with a CAS calculator.","To be able to use the operations of addition, subtraction and scalar multiplication of matrices in practical situations."],
'10D':["To be able to establish when multiplication of two matrices can be undertaken.","To be able to undertake the multiplication of matrices.","To be able to understand that the order of multiplication of matrices is important.","To be able to apply multiplication of matrices to practical problems.","To be able to use your CAS calculator to undertake multiplication of matrices.","To be able to understand the role of 'summing matrices'.","To be able to work with calculations involving powers of matrices."],
'10E':["To be able to determine by multiplication when two matrices are inverses.","To be able to determine the determinant of a 2 × 2 matrix.","To be able to determine the inverse of a 2 × 2 matrix.","To be able to use a CAS calculator to determine the inverse and determinant of an n × n matrix.","To be able to solve simple matrix equations."],
'10F':["To be able to identify and work with binary matrices, permutation matrices and communication matrices."],
'10G':["To be able to construct and interpret dominance matrices."]}
SC={
'10A':["I can state the order of a given matrix.","I can find the transpose of a matrix.","I can identify a matrix as being a square, column or row matrix.","I can identify a square matrix as being an identity or diagonal or symmetric or upper/lower triangular matrix.","I can identify the aij term in a matrix A.","I can construct a matrix given a rule for aij.","I can enter a matrix into a CAS calculator."],
'10B':["I can enter information from a table into a matrix.","I can represent a network diagram by a matrix.","I can interpret a matrix representing a network diagram."],
'10C':["I can recognise when two matrices are equal and use this to solve problems.","I can add two matrices of the same order together.","I can subtract one matrix from another when they have the same order.","I can multiply a matrix by a scalar.","I recognise the role of the zero matrix and can undertake operations using the zero matrix.","I can use addition, subtraction and scalar multiplication to process data."],
'10D':["I can determine if the product of two given matrices is defined.","I can determine the order of a matrix product.","I can multiply a row matrix by a column matrix by hand.","I can multiply a rectangular matrix by a column matrix by hand.","I can use summing matrices to sum the rows or columns of a matrix.","I can undertake multiplications of matrices to solve practical problems.","I can evaluate matrix expressions involving powers."],
'10E':["I can recognise that two matrices are inverses if their product is the identity matrix.","I can evaluate the determinant of a 2 × 2 matrix by hand.","I can calculate the inverse of a 2 × 2 matrix by hand.","I can calculate the inverse and determinant of an n × n matrix using CAS.","I can solve simple matrix equations."],
'10F':["I can use a permutation matrix to rearrange the elements of a column or row matrix.","I can construct a permutation matrix to rearrange the elements of a column or row matrix in a given order.","I can find the inverse of a permutation matrix.","I can construct a communication matrix from information given in written form or a diagram."],
'10G':["I can construct a dominance matrix from information given in written form or a diagram."]}
CW={
'10A':[("Order of a matrix","Q1–4"),("The transpose of a matrix","Q5"),("Types of matrices and their elements","Q6–14"),("Exam 1 style questions","Q15–19")],
'10B':[("Representing a table of data in matrix form","Q1–6"),("Representing a network diagram by a matrix","Q7–10"),("Exam 1 style questions","Q11–12")],
'10C':[("Equality of two matrices","Q1"),("Matrix addition, subtraction and scalar multiplication","Q2–6"),("Applications of matrix addition, subtraction and scalar multiplication","Q7–9"),("Exam 1 style questions","Q10–11")],
'10D':[("Matrix multiplication","Q1–7"),("Practical applications of matrix multiplication","Q8–13"),("Powers of matrices","Q14–17"),("Exam 1 style questions","Q18–20")],
'10E':[("Review of the properties of the identity matrix","Q1–2"),("Calculating the determinant of a matrix","Q3"),("Calculating the inverse of a matrix","Q4"),("Solving matrix equations","Q5–11"),("Exam 1 style questions","Q12–14")],
'10F':[("Permutation matrices","Q1–3"),("Inverses of permutation matrices","Q4"),("Communication matrices","Q5–7"),("Exam 1 style questions","Q8–9")],
'10G':[("Dominance matrices","Q1–9"),("Exam 1 style questions","Q10–12")]}
SD={'10A':["MX-1.1","MX-1.3"],'10B':["MX-1.3"],'10C':["MX-1.1"],'10D':["MX-1.1"],'10E':["MX-1.2"],'10F':["MX-1.4","MX-1.5"],'10G':["MX-1.5"]}
LESSONS=[('gm12-u4-10a10b',['10A','10B'],'What is a matrix? Representing information'),
 ('gm12-u4-10c',['10C'],'Matrix addition, subtraction and scalar multiplication'),
 ('gm12-u4-10d',['10D'],'The product of two matrices'),
 ('gm12-u4-10e',['10E'],'Matrix inverse, the determinant and matrix equations'),
 ('gm12-u4-10f10g',['10F','10G'],'Binary, permutation, communication and dominance matrices')]
sd=json.load(open('tools/sd.json'))
d=json.load(open(P))
ch=[c for A in d['aos'] for c in A['chapters'] if c['n']==10][0]
check=[l for l in ch['lessons'] if l['kind']=='check']
new=[]
for lid,subs,title in LESSONS:
  sdp=[]
  for s in subs:
    for k in SD[s]:
      if sd[k] not in sdp: sdp.append(sd[k])
  sets=[{"title":f"Cambridge · Exercise {s}","items":[{"skill":a,"q":b} for a,b in CW[s]],"note":""} for s in subs]
  sets.append({"title":"Revision book","items":[],"note":"The "+" and ".join(subs)+" section"+("s" if len(subs)>1 else "")})
  new.append({"id":lid,"kind":"lesson","subchapters":subs,"title":title,"card":{
    "learningObjectives":[{"sub":s,"items":LI[s]} for s in subs],
    "successCriteria":[{"sub":s,"items":SC[s]} for s in subs],
    "studyDesign":sdp,
    "homework":{"source":"prefill","sets":sets}}})
for c in check: c.pop('shell',None)
ch['lessons']=new+check
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
