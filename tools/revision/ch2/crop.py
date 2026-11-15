"""Crop Insight figures (scanned pages rendered at 220 dpi; boxes given in 110-dpi px) -> crops/*.png"""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
BOX = {  # name: (file, x0, x1, y0, y1)
 'g1q1': ('c1-15', 455, 782, 283, 386), 'g1q6': ('c1-17', 466, 800, 868, 1068), 'g1q9': ('c1-18', 130, 480, 775, 988),
 'g1q12': ('c1-19', 85, 436, 708, 942), 'g1q24': ('c1-22', 110, 490, 200, 410),
 'g2q1': ('c2-17', 200, 636, 210, 422), 'g2q2': ('c2-17', 300, 818, 745, 1065), 'g2q3': ('c2-19', 165, 700, 600, 915),
 'g2q4': ('c2-20', 135, 655, 175, 500), 'g2q5': ('c2-21', 220, 636, 530, 838), 'g2q6': ('c2-23', 225, 630, 158, 500),
 'g2q14': ('c2-33', 40, 786, 150, 510)}
for k, (f, x0, x1, y0, y1) in BOX.items():
    im = Image.open(f'{SRC}/{f}.png').convert('RGB').crop((x0*2, y0*2, x1*2, y1*2))
    g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0)
    bb = g.getbbox()
    if bb: im = im.crop((max(bb[0]-8, 0), max(bb[1]-8, 0), min(bb[2]+8, im.width), min(bb[3]+8, im.height)))
    im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
