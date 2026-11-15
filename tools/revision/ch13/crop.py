"""Crop the Ch 13 Insight questions (verbatim scans) -> crops/*.png.
Usage: python3 crop.py <folder with h1-NN.png (GM1 Unit 4 pdf pages) and h2-NN.png (GM2 Unit 4 pdf pages) at 220 dpi>.
Boxes are (page, x0, y0, x1, y1) in 110-dpi px (half the 220-dpi size). GM2 boxes were read off 0.8-scaled two-page
spreads: B2(left/right, x0, y0, x1, y1) converts them."""
import sys
from PIL import Image, ImageOps
SRC = sys.argv[1]


def B2(page, side, x0, y0, x1, y1):
    o = 727 if side == 'R' else 0
    return (page, (x0 - o) / .8, y0 / .8, (x1 - o) / .8, y1 / .8)


L, R = (60, 455), (450, 880)
L20, R20 = (60, 505), (495, 880)
BOX = {
    # GM1 Unit 4, 'Undirected graphs and networks' (printed pp.18-23 = pdf 19-24) + directed section Q4 (pdf 25)
    'g1q1': ('h1-19', R[0], 247, R[1], 675), 'g1q2': ('h1-19', R[0], 730, R[1], 1175),
    'g1q3': ('h1-20', L20[0], 110, L20[1], 545), 'g1q4': ('h1-20', L20[0], 590, L20[1], 940), 'g1q5': ('h1-20', R20[0], 110, R20[1], 1060),
    'g1q6': ('h1-21', L[0], 100, L[1], 300), 'g1q7': ('h1-21', L[0], 330, L[1], 700), 'g1q8': ('h1-21', L[0], 750, L[1], 1130),
    'g1q9': ('h1-21', R[0], 100, R[1], 285), 'g1q10': ('h1-21', R[0], 335, R[1], 690), 'g1q11': ('h1-21', R[0], 730, R[1], 1165),
    'g1q12': ('h1-22', L[0], 100, L[1], 385), 'g1q13': ('h1-22', L[0], 430, L[1], 745), 'g1q14': ('h1-22', 482, 100, R[1], 810),
    'g1q15': ('h1-22', R[0], 860, R[1], 1065),
    'g1q16': ('h1-23', L[0], 85, L[1], 460), 'g1q17': ('h1-23', L[0], 515, L[1], 870), 'g1q18': ('h1-23', R[0], 85, R[1], 1100),
    'g1q20': ('h1-24', R20[0], 85, R20[1], 440), 'g1q21': ('h1-24', R20[0], 475, R20[1], 850), 'g1q22': ('h1-24', R20[0], 890, R20[1], 1115),
    'g1d4': ('h1-25', 450, 475, 900, 815),
    # GM2 Unit 4, 'Undirected graphs and networks' (printed pp.21-28 = pdf 22-29)
    'g2q1': B2('h2-22', 'L', 100, 125, 665, 378), 'g2q1a': B2('h2-22', 'L', 100, 377, 665, 397), 'g2q1b': B2('h2-22', 'L', 100, 448, 665, 497),
    'g2q1c': B2('h2-22', 'L', 100, 553, 665, 570), 'g2q1d': B2('h2-22', 'L', 100, 680, 665, 712),
    'g2q2': B2('h2-23', 'R', 790, 55, 1420, 255), 'g2q2a': B2('h2-23', 'R', 790, 258, 1345, 325), 'g2q2b': B2('h2-23', 'R', 790, 432, 1345, 500),
    'g2q2c': B2('h2-23', 'R', 790, 610, 1345, 815), 'g2q2cii': B2('h2-23', 'R', 790, 820, 1345, 837),
    'g2q3': B2('h2-24', 'L', 100, 65, 665, 228), 'g2q3a': B2('h2-24', 'L', 100, 232, 665, 250), 'g2q3b': B2('h2-24', 'L', 100, 330, 665, 426),
    'g2q3c': B2('h2-24', 'L', 100, 498, 665, 662),
    'g2q4': B2('h2-25', 'R', 790, 65, 1345, 222), 'g2q4a': B2('h2-25', 'R', 790, 225, 1345, 243), 'g2q4b': B2('h2-25', 'R', 790, 350, 1345, 602),
    'g2q5': B2('h2-26', 'L', 100, 65, 665, 315), 'g2q5a': B2('h2-26', 'L', 100, 320, 665, 337), 'g2q5bi': B2('h2-26', 'L', 100, 420, 665, 482),
    'g2q5bii': B2('h2-26', 'L', 100, 595, 665, 628), 'g2q5biii': B2('h2-26', 'L', 100, 695, 665, 925),
    'g2q6': B2('h2-27', 'R', 790, 62, 1420, 300), 'g2q6a': B2('h2-27', 'R', 790, 345, 1345, 362), 'g2q6b': B2('h2-27', 'R', 790, 415, 1345, 442),
    'g2q6c': B2('h2-27', 'R', 790, 530, 1345, 787), 'g2q6d': B2('h2-27', 'R', 790, 805, 1345, 852),
    'g2q7': B2('h2-28', 'L', 100, 65, 665, 300), 'g2q7a': B2('h2-28', 'L', 100, 310, 665, 327), 'g2q7b': B2('h2-28', 'L', 100, 385, 665, 432),
    'g2q7c': B2('h2-28', 'L', 100, 495, 665, 752),
    'g2q7d': B2('h2-29', 'R', 790, 60, 1345, 307), 'g2q8': B2('h2-29', 'R', 790, 365, 1345, 905),
}
if __name__ == '__main__':
    for k, (f, x0, y0, x1, y1) in BOX.items():
        im = Image.open(f'{SRC}/{f}.png').convert('RGB')
        im = im.crop((int(x0 * 2), int(y0 * 2), min(int(x1 * 2), im.width), min(int(y1 * 2), im.height)))
        g = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 60 else 0)
        bb = g.getbbox()
        if bb: im = im.crop((max(bb[0] - 8, 0), max(bb[1] - 8, 0), min(bb[2] + 8, im.width), min(bb[3] + 8, im.height)))
        im.save(f'crops/{k}.png', optimize=True); print(k, im.size)
