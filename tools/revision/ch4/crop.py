"""Crop Insight figures (scanned pages rendered at 220 dpi; boxes given in 110-dpi px) -> crops/*.png.
g1q30 (pool scatterplot) is copied from ../ch3/crops."""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
BOX = {'g1q5': ('c1-17', 75, 410, 540, 778), 'g1q15': ('c1-20', 115, 495, 762, 1040)}
for k, (f, x0, x1, y0, y1) in BOX.items():
    im = Image.open(f'{SRC}/{f}.png').convert('RGB').crop((x0*2, y0*2, x1*2, y1*2))
    g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0)
    bb = g.getbbox()
    if bb: im = im.crop((max(bb[0]-8, 0), max(bb[1]-8, 0), min(bb[2]+8, im.width), min(bb[3]+8, im.height)))
    im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
