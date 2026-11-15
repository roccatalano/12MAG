"""Crop CFAT 1.4.1/1.4.2 figures from Edrolo U3&4 2023 (300 dpi renders H-<page>.png). Boxes in px of an 850x1100 preview of the page."""
import sys
from PIL import Image
S=sys.argv[1]
C={'3D_Q1':(207,88,395,305,570),'3D_Q2a':(207,92,700,355,930),'3D_Q2b':(207,445,700,722,930),
   '3D_Q3a':(208,130,105,360,275),'3D_Q3b':(208,130,315,360,483),'3D_Q3c':(208,130,612,360,782),
   '3E_Q7':(223,455,66,770,298)}
for k,(p,a,b,c,d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((round(a*2481/850),round(b*3508/1100),round(c*2481/850),round(d*3508/1100))).save(f'fig/{k}.png')
