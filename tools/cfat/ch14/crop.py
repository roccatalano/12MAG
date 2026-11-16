"""Crop CFAT 4.14.x question images from Edrolo U3&4 2023 (300 dpi renders H-<pdfpage>.png).
Boxes in px of the 100 dpi render (827x1170); graphs/options cropped, not redrawn, so they stay verbatim.
Run: python3 crop.py <dir with H-*.png>  (pdftoppm -f P -l P -r 300 -png <edrolo pdf> H-P -singlefile)"""
import sys, os
from PIL import Image
S = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
C = {'8E_Q1':(585,85,160,760,345), '8E_Q4':(586,105,105,770,365), '8E_Q7':(587,85,105,700,290),
     '8G_Q1':(609,85,160,750,615), '8G_Q4':(610,105,105,640,365),
     '8E_Q5':(586,105,410,775,585), '8E_Q9':(587,85,725,770,825), '8G_Q2':(609,455,640,755,820),
     '8H_Q1':(621,85,405,760,615), '8H_Q3':(621,85,960,760,1080), '8I_Q7':(638,95,630,680,785),
     '8H_Q2':(621,525,645,750,900), '8H_Q4a':(622,105,95,440,180), '8I_Q3':(637,410,860,750,975),
     '8I_Q4':(638,430,70,775,190), '8I_Q8':(638,105,830,475,985),
     '8J_Q1':(647,85,565,760,805), '8J_Q4':(648,95,590,760,865), '8J_Q3':(648,100,235,530,375),
     '8J_Q6':(649,85,280,430,430), '8J_Q7':(649,85,650,560,800)}
for k, (p, a, b, c, d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((a*3, b*3, c*3, d*3)).save(os.path.join(HERE, 'fig', k + '.png'))
