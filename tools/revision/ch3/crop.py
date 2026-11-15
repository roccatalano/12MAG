"""Crop Insight figures (scanned pages rendered at 220 dpi; boxes given in 110-dpi px) -> crops/*.png.
g1q9, g1q12, g1q24, g2q4, g2q5, g2q14 are copied from ../ch2/crops."""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]
BOX = {  # name: (file, x0, x1, y0, y1)
 'g1q2': ('c1-15', 460, 815, 950, 1185),
 'g1q4a': ('c1-16', 525, 800, 188, 348), 'g1q4b': ('c1-16', 525, 800, 353, 502), 'g1q4c': ('c1-16', 525, 800, 503, 657),
 'g1q4d': ('c1-16', 525, 800, 668, 837), 'g1q4e': ('c1-16', 525, 800, 843, 1007),
 'g1q18': ('c1-21', 85, 425, 148, 318), 'g1q29': ('c1-23', 72, 432, 648, 852), 'g1q30': ('c1-23', 420, 842, 520, 718),
 'g1q30a': ('c1-24', 160, 492, 112, 242), 'g1q30b': ('c1-24', 160, 492, 266, 408), 'g1q30c': ('c1-24', 160, 492, 426, 562),
 'g1q30d': ('c1-24', 160, 492, 593, 732), 'g1q30e': ('c1-24', 160, 492, 758, 897),
 'g2q2': ('c2-17', 300, 818, 745, 1065), 'g2q2r': ('c2-18', 290, 672, 912, 1132),
 'g2q8': ('c2-25', 198, 652, 158, 512), 'g2q8r': ('c2-26', 268, 702, 458, 792),
 'g2q10': ('c2-28', 138, 852, 328, 582), 'g2q11': ('c2-29', 138, 722, 148, 478)}
for k, (f, x0, x1, y0, y1) in BOX.items():
    im = Image.open(f'{SRC}/{f}.png').convert('RGB').crop((x0*2, y0*2, x1*2, y1*2))
    g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0)
    bb = g.getbbox()
    if bb: im = im.crop((max(bb[0]-8, 0), max(bb[1]-8, 0), min(bb[2]+8, im.width), min(bb[3]+8, im.height)))
    im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
