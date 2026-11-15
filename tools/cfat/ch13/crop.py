"""Crop CFAT 4.13.x question images from Edrolo U3&4 2023 (300 dpi renders H-<pdfpage>.png).
Boxes in px of the 100 dpi render (827x1170) of each page; graphs/options are cropped, not redrawn, so they stay verbatim.
Run: python3 crop.py <dir with H-*.png>  (pdftoppm -f P -l P -r 300 -png <edrolo pdf> H-P -singlefile)"""
import sys, os
from PIL import Image
S = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
C = {'8A_Q1':(533,85,160,760,290), '8A_Q5':(533,85,880,760,1005), '8A_Q11':(535,85,272,600,392), '8A_Q3':(533,555,468,755,582),
     '8B_Q1':(546,105,375,600,585), '8B_Q2':(546,105,635,770,800), '8B_Q4':(547,565,70,755,237),
     '8C_Q1':(562,85,160,775,340), '8C_Q4':(563,85,105,760,225), '8C_Q8':(564,100,105,775,230), '8C_Q6':(563,495,658,752,808),
     '8F_Q1':(597,85,690,610,1027), '8F_Q6':(599,85,800,620,1037), '8F_Q3':(598,485,520,772,702), '8F_Q8':(600,458,352,777,552),
     '8D_Q1':(574,100,160,720,440), '8D_Q5':(575,85,415,660,852), '8D_Q2':(574,100,488,300,627), '8D_Q3':(574,100,755,420,1000),
     '8D_Q6':(575,85,890,262,1042), '8D_Q7':(576,100,72,600,458), '8D_Q8':(576,100,518,445,748)}
for k, (p, a, b, c, d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((a*3, b*3, c*3, d*3)).save(os.path.join(HERE, 'fig', k + '.png'))
