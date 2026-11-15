"""Crop CFAT 1.3.1/1.3.2 figures from Edrolo U3&4 2023 (300 dpi renders H-<page>.png). Boxes in 100-dpi px."""
import sys
from PIL import Image
S=sys.argv[1]
C={'3A_Q4':(171,478,282,752,528),'3B_Q7':(181,400,742,745,992),'3C_Q6a':(195,95,128,395,262),'3C_Q6b':(195,440,128,725,262),'3C_Q6c':(195,95,280,395,465)}
for k,(p,a,b,c,d) in C.items():
    Image.open(f'{S}/H-{p}.png').crop((a*3,b*3,c*3,d*3)).save(f'fig/{k}.png')
