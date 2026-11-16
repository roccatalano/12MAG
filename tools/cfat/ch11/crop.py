"""Crop CFAT 3.11.x question images from Edrolo U3&4 2023 (300 dpi renders H-<pdfpage>.png, 2481x3508).
Boxes in px of a 1/3-scale preview (827x1169). Matrices/diagrams are cropped, not retyped, so the wording stays verbatim.
Run: python3 crop.py <dir with H-*.png>  (pdftoppm -f P -l P -r 300 -png <edrolo pdf> H-P -singlefile)"""
import sys, os
from PIL import Image
S = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
C = {'7G_Q1': (496, 105, 160, 610, 352), '7G_Q2': (496, 105, 370, 660, 555), '7G_Q4': (496, 105, 903, 745, 1022), '7G_Q5': (497, 86, 75, 640, 170), '7I_Q1': (516, 105, 160, 770, 340), '7I_Q2': (516, 105, 365, 770, 670), '7H_Q1': (506, 105, 160, 770, 222), '7H_Q4': (506, 105, 510, 660, 632), '7H_Q5': (506, 105, 688, 660, 850), '7I_Q7': (518, 105, 105, 420, 228), '7I_Q8': (518, 105, 255, 560, 375), '7G_Q10': (498, 105, 70, 660, 205), '7G_Q12': (498, 105, 575, 620, 1016), '7G_Q13': (499, 86, 75, 640, 212)}
for k, (p, a, b, c, d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((a*3, b*3, c*3, d*3)).save(os.path.join(HERE, 'fig', k + '.png'))
