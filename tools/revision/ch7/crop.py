"""Crop Insight figures (pages rendered at 220 dpi; boxes given in 110-dpi px) -> crops/*.png.
Usage: python3 crop.py <folder with h1-NN.png at 220 dpi>. h1 = GM1 U3 Recursion and Financial Modelling pdf pages."""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
BOX = {'g1q5': ('h1-07', 450, 815, 658, 900), 'g1q7': ('h1-08', 145, 455, 455, 700), 'g1q12': ('h1-09', 80, 420, 165, 345)}
for k, (f, x0, x1, y0, y1) in BOX.items():
    im = Image.open(f'{SRC}/{f}.png').convert('RGB').crop((x0*2, y0*2, x1*2, y1*2))
    g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0)
    bb = g.getbbox()
    if bb: im = im.crop((max(bb[0]-8, 0), max(bb[1]-8, 0), min(bb[2]+8, im.width), min(bb[3]+8, im.height)))
    im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
