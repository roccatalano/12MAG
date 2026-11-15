"""Crop CFAT 1.5.1 figures from Edrolo U3&4 2023 (300 dpi renders H-<page>.png). Boxes in px of an 850x1100 preview of the page."""
import sys
from PIL import Image
S=sys.argv[1]
C={'4A_Q1':(236,505,152,785,318),'4A_Q5':(237,420,462,772,612),'4A_Q6a':(237,108,662,402,835),'4A_Q6b':(237,438,662,772,835),
   '4C_Q1':(268,100,702,672,935),'4C_Q10':(271,415,528,772,728)}
for k,(p,a,b,c,d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((round(a*2481/850),round(b*3508/1100),round(c*2481/850),round(d*3508/1100))).save(f'fig/{k}.png')
