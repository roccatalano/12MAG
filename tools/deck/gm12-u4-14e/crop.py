"""Crop the figures for 14E from the source PDFs (200 dpi). Boxes in 100-dpi page pixels (x0, y0, x1, y1).
Run with the sources staged under /mnt/user-data/uploads/12MAG Course Planner/02 Sources."""
import os, subprocess
from PIL import Image
SRC = '/mnt/user-data/uploads/12MAG Course Planner/02 Sources/'; H = os.path.dirname(os.path.abspath(__file__)); T = '/tmp/claude-0/crop'
os.makedirs(T, exist_ok=True)
C = 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf'; E = 'Textbooks/Edrolo U3&4/2023-edrolo-units-3-4.pdf'
J = [('dn2', 'VCAA current/2023/2023 E1.pdf', 18, (190, 818, 320, 895)),
     ('dn3', 'VCAA current/2024/2024 E2.pdf', 25, (105, 195, 745, 432)),
     ('ex1', 'VCAA past/2017/2017 E2.pdf', 22, (150, 162, 700, 498)),
     ('ex2', 'VCAA past/2020/2020 E1.pdf', 30, (80, 172, 735, 342)),
     ('ex3', 'VCAA past/2021/2021 E2.pdf', 25, (135, 128, 725, 358)), ('ex3t', 'VCAA past/2021/2021 E2.pdf', 25, (105, 642, 322, 858)),
     ('lrn', C, 721, (380, 180, 668, 332)),
     ('cam12', C, 721, (245, 795, 545, 922)),
     ('cam13', C, 723, (245, 298, 548, 437)), ('cam13t', C, 723, (490, 556, 665, 690)),
     ('edr1q', E, 644, (72, 138, 375, 252)), ('edr1a', E, 644, (430, 458, 730, 602)), ('edr1b', E, 644, (95, 848, 425, 1015)),
     ('edr2q', E, 645, (52, 288, 412, 392)), ('edr2a', E, 645, (85, 718, 402, 848)), ('edr2b', E, 646, (85, 205, 442, 338))]
for n, f, p, b in J:
    o = f'{T}/{n}'
    subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(p), '-l', str(p), SRC + f, o], check=True, stderr=subprocess.DEVNULL)
    Image.open(o + '.png').crop(tuple(2 * v for v in b)).save(f'{H}/fig/{n}.png')
print(len(J), 'figures')
