"""Crop Insight figures (scanned pages rendered at 220 dpi; boxes given in 110-dpi px) -> crops/*.png.
Usage: python3 crop.py <folder with g1-NN.png / g2-NN.png at 220 dpi>.
g1 = GM1 U3 Data Analysis pdf pages 25-30 (printed 22-27); g2 = GM2 pdf pages 35-42 (questions), 60-62 (worked solutions)."""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
BOX = {  # key: (file, x0, x1, y0, y1)
 'g1q1': ('g1-25', 455, 830, 210, 470), 'g1q5': ('g1-26', 505, 870, 735, 925), 'g1q14': ('g1-28', 485, 850, 335, 545),
 'g1q16': ('g1-29', 85, 430, 160, 335), 'g1q17': ('g1-29', 85, 430, 760, 1100), 'g1q20': ('g1-30', 140, 475, 755, 945),
 'g2q1': ('g2-35', 140, 720, 345, 655), 'g2q2': ('g2-36', 160, 610, 340, 605), 'g2q3': ('g2-37', 80, 750, 375, 690),
 'g2q4': ('g2-39', 220, 640, 160, 410), 'g2q6': ('g2-41', 80, 800, 275, 660),
 's2a': ('g2-60', 160, 490, 205, 410), 's3d': ('g2-61', 80, 400, 140, 390), 's4a': ('g2-61', 80, 410, 945, 1145),
 's6a': ('g2-62', 495, 800, 140, 740),
}
for k, (f, x0, x1, y0, y1) in BOX.items():
    im = Image.open(f'{SRC}/{f}.png').convert('RGB').crop((x0*2, y0*2, x1*2, y1*2))
    g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0)
    bb = g.getbbox()
    if bb: im = im.crop((max(bb[0]-8, 0), max(bb[1]-8, 0), min(bb[2]+8, im.width), min(bb[3]+8, im.height)))
    im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
