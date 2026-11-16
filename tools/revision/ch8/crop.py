"""Crop the Ch 8 Insight questions (verbatim scans) -> crops/*.png.
Usage: python3 crop.py <folder with h1-NN.png (GM1 U3 Recursion and Financial Modelling pdf pages 10-16) and h2-NN.png
(GM2 U3 Recursion and Financial Modelling pdf pages 14-20) at 220 dpi>.
Segments are (page, column, y0, y1) in 220-dpi px. Keys: a = GM1 'Reducing balance loans, annuities, perpetuities,
amortisation tables' section, f = GM1 'Using the finance solver' section, i* = shared information blocks,
s = GM2 reducing balance section, t = GM2 finance solver section."""
import sys
from PIL import Image, ImageOps
EVEN = {'h1-10', 'h1-12', 'h1-14', 'h1-16'}  # pages with the wide left margin
def cols(f, c):
    if c == 'W': return (90, 1790)
    if c == 'T': return (70, 1000)
    if f in EVEN: return {'L': (230, 1000), 'R': (1000, 1800)}[c]
    return {'L': (110, 895), 'R': (895, 1770)}[c]
F = 2370; G = 2390
SEG = {
    'a1': [('h1-10', 'L', 400, 1045)], 'a2': [('h1-10', 'L', 1045, F)],
    'ia3': [('h1-10', 'R', 140, 440)], 'a3': [('h1-10', 'R', 440, 880)], 'a4': [('h1-10', 'R', 880, 1322)], 'a5': [('h1-10', 'R', 1322, F)],
    'a6': [('h1-11', 'L', 140, 1245)], 'a7': [('h1-11', 'L', 1245, F)],
    'ia8': [('h1-11', 'R', 140, 972)], 'a8': [('h1-11', 'R', 972, 1415)], 'a9': [('h1-11', 'R', 1415, F)],
    'a10': [('h1-12', 'L', 145, F)], 'ia11': [('h1-12', 'R', 140, 382)], 'a11': [('h1-12', 'R', 382, 790)], 'a12': [('h1-12', 'R', 790, F)],
    'ia13': [('h1-13', 'L', 140, 1062)], 'a13': [('h1-13', 'L', 1062, 1452)], 'a14': [('h1-13', 'L', 1452, 1880)], 'a15': [('h1-13', 'L', 1880, F)],
    'ia16': [('h1-13', 'R', 140, 528)], 'a16': [('h1-13', 'R', 528, 972)], 'a17': [('h1-13', 'R', 972, 1415)], 'a18': [('h1-13', 'R', 1415, F)],
    'a19': [('h1-14', 'L', 140, 638)], 'ia20': [('h1-14', 'T', 638, 1290)], 'a20': [('h1-14', 'L', 1290, 1732)], 'a21': [('h1-14', 'L', 1732, F)],
    'f1': [('h1-14', 'R', 340, 995)], 'f2': [('h1-14', 'R', 995, F)],
    'f3': [('h1-15', 'L', 140, 880)], 'if4': [('h1-15', 'L', 880, 1162)], 'f4': [('h1-15', 'L', 1162, 1605)], 'f5': [('h1-15', 'L', 1605, F)],
    'if6': [('h1-15', 'R', 140, 548)], 'f6': [('h1-15', 'R', 548, 992)], 'f7': [('h1-15', 'R', 992, 1597)], 'f8': [('h1-15', 'R', 1597, F)],
    'f9': [('h1-16', 'L', 145, 890)], 'f10': [('h1-16', 'L', 890, 1632)], 'f11': [('h1-16', 'L', 1632, F)], 'f12': [('h1-16', 'R', 145, 1000)],
    's1': [('h2-14', 'W', 340, G)], 's2': [('h2-15', 'W', 170, G)], 's3': [('h2-16', 'W', 175, G)],
    't1': [('h2-17', 'W', 270, 1188)], 't2': [('h2-17', 'W', 1188, 1682)], 't3': [('h2-17', 'W', 1682, G)],
    't4': [('h2-18', 'W', 175, 1518)], 't5': [('h2-18', 'W', 1518, G), ('h2-19', 'W', 110, 638)],
    't6': [('h2-19', 'W', 638, 1245)], 't7': [('h2-19', 'W', 1245, G)], 't8': [('h2-20', 'W', 180, G)],
}
if __name__ == '__main__':
    SRC = sys.argv[1]
    for k, segs in SEG.items():
        for i, (f, c, y0, y1) in enumerate(segs):
            im = Image.open(f'{SRC}/{f}.png').convert('RGB')
            x0, x1 = cols(f, c)
            im = im.crop((x0, y0, x1, min(y1, im.height)))
            g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 60 else 0)
            bb = g.getbbox()
            if bb: im = im.crop((max(bb[0] - 8, 0), max(bb[1] - 8, 0), min(bb[2] + 8, im.width), min(bb[3] + 8, im.height)))
            name = k if i == 0 else f'{k}_{i + 1}'
            im.save(f'crops/{name}.png', optimize=True); print(name, im.size)
