"""Crop CFAT 3.10.x question images from Edrolo U3&4 2023 (300 dpi renders H-<pdfpage>.png).
Boxes in px of an 850x1100 preview of the page. Matrices are cropped, not retyped, so the wording stays verbatim.
Run: python3 crop.py <dir with H-*.png>  (pdftoppm -f P -l P -r 300 -png <edrolo pdf> H-P -singlefile)"""
import sys, os
from PIL import Image
S = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
C = {'7A_Q1':(432,105,150,792,235), '7A_Q2':(432,105,256,420,332), '7A_Q4':(432,105,603,430,677),
     '7B_Q1':(441,88,150,762,274), '7B_Q4':(441,88,918,762,1013), '7B_Q5':(442,108,66,800,188), '7B_Q7':(442,108,486,800,574),
     '7C_Q1':(453,88,150,762,236), '7C_Q4':(453,88,578,762,667), '7C_Q6':(453,88,845,700,942),
     '7C_Q12':(455,88,176,762,237), '7C_Q14':(455,88,388,762,463),
     '7D_Q1':(463,88,434,762,507), '7D_Q5':(463,88,841,762,950), '7D_Q9':(464,108,400,800,497), '7D_Q11':(464,108,644,800,697),
     '7E_Q1':(472,108,150,800,214), '7E_Q4':(472,108,610,800,762),
     '7F_Q1':(482,108,150,800,347), '7F_Q3':(482,108,750,620,860), '7F_Q6':(483,88,710,762,920), '7F_Q8':(484,108,231,700,379)}
for k, (p, a, b, c, d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((round(a*2481/850), round(b*3508/1100), round(c*2481/850), round(d*3508/1100))).save(os.path.join(HERE, 'fig', k + '.png'))
