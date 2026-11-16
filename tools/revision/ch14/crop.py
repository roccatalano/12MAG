"""Crop the Ch 14 Insight questions (verbatim scans) -> crops/*.png.
Usage: python3 crop.py <folder with h1-NN.png (GM1 Unit 4 pdf pages) and h2-NN.png (GM2 Unit 4 pdf pages) at 220 dpi>.
Segments are (page, column, y0, y1) in 220-dpi px; column L/R (GM1 two-column pages) or W (full width).
A question that runs over a column/page break has several segments, saved as key, key_2, key_3."""
import sys
from PIL import Image, ImageOps
COL = {'L': (110, 905), 'R': (895, 1790), 'W': (90, 1790)}
SHIFT = {'L': (150, 995), 'R': (1000, 1790)}
SHIFTP = {'h1-24', 'h1-26', 'h1-28', 'h1-30'}
F = 2365  # footer line
SEG = {
    # GM1 Unit 4: undirected section Q19 (allocation, printed p.23 = pdf 24); directed section Q1-26 (printed pp.24-30 = pdf 25-31)
    'u19': [('h1-24', 'L', 120, F)],
    'd1': [('h1-25', 'L', 400, 1060)], 'd2': [('h1-25', 'L', 1060, F)], 'd3': [('h1-25', 'R', 120, 900)],
    'd5': [('h1-25', 'R', 1660, F), ('h1-26', 'L', 110, 530)],
    'i6': [('h1-26', 'L', 530, 1075)], 'd6': [('h1-26', 'L', 1075, 1790)], 'd7': [('h1-26', 'L', 1790, F)],
    'i8': [('h1-26', 'R', 120, 800)], 'd8': [('h1-26', 'R', 800, 1240)], 'd9': [('h1-26', 'R', 1240, 1680)], 'd10': [('h1-26', 'R', 1680, F)],
    'i11': [('h1-27', 'L', 120, 778)], 'd11': [('h1-27', 'L', 778, 1250)], 'd12': [('h1-27', 'L', 1250, 1660)], 'd13': [('h1-27', 'L', 1660, F)],
    'i14': [('h1-27', 'R', 120, 640)], 'd14': [('h1-27', 'R', 640, 1088)], 'd15': [('h1-27', 'R', 1088, 1495)], 'd16': [('h1-27', 'R', 1495, F)],
    'i17': [('h1-28', 'L', 130, 677)], 'd17': [('h1-28', 'L', 677, F), ('h1-28', 'R', 110, 700)], 'd18': [('h1-28', 'R', 700, 1368)],
    'i19': [('h1-28', 'R', 1368, 1836)], 'd19': [('h1-28', 'R', 1836, F)],
    'd20': [('h1-29', 'L', 120, 605)], 'd21': [('h1-29', 'L', 605, F)], 'd22': [('h1-29', 'R', 120, 858)], 'd23': [('h1-29', 'R', 858, F)],
    'd24': [('h1-30', 'L', 120, F), ('h1-30', 'R', 110, 1050)], 'd25': [('h1-30', 'R', 1050, F)], 'd26': [('h1-31', 'L', 110, 1200)],
    # GM2 Unit 4: directed section Q1-13 (printed pp.29-39 = pdf 30-40), with Insight's own answer lines
    'g1': [('h2-30', 'W', 345, 1570)], 'g2': [('h2-30', 'W', 1570, F + 20), ('h2-31', 'W', 110, 432)], 'g3': [('h2-31', 'W', 432, F + 20)],
    'g4': [('h2-32', 'W', 150, F + 20)], 'g5': [('h2-33', 'W', 110, 1785)], 'g6': [('h2-33', 'W', 1785, F), ('h2-34', 'W', 110, 1700)],
    'g7': [('h2-34', 'W', 1700, 2385), ('h2-35', 'W', 110, 648)], 'g8': [('h2-35', 'W', 648, F + 20)],
    'g9': [('h2-36', 'W', 150, 1605)], 'g10': [('h2-36', 'W', 1605, F + 20), ('h2-37', 'W', 110, 1240)], 'g11': [('h2-37', 'W', 1240, F + 20)],
    'g12': [('h2-38', 'W', 140, F + 10), ('h2-39', 'W', 110, 990)], 'g13': [('h2-39', 'W', 990, F + 5), ('h2-40', 'W', 110, 1400)],
}
if __name__ == '__main__':
    SRC = sys.argv[1]
    for k, segs in SEG.items():
        for i, (f, c, y0, y1) in enumerate(segs):
            im = Image.open(f'{SRC}/{f}.png').convert('RGB')
            x0, x1 = COL[c] if c == 'W' or f not in SHIFTP else SHIFT[c]
            im = im.crop((x0, y0, x1, min(y1, im.height)))
            g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 60 else 0)
            bb = g.getbbox()
            if bb: im = im.crop((max(bb[0] - 8, 0), max(bb[1] - 8, 0), min(bb[2] + 8, im.width), min(bb[3] + 8, im.height)))
            name = k if i == 0 else f'{k}_{i + 1}'
            im.save(f'crops/{name}.png', optimize=True); print(name, im.size)
