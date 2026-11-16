"""Crop the figures for 14D from the source PDFs (200 dpi). Boxes in 100-dpi page pixels (x0, y0, x1, y1).
Run with the sources staged under /mnt/user-data/uploads/12MAG Course Planner/02 Sources."""
import os, subprocess
from PIL import Image
SRC = '/mnt/user-data/uploads/12MAG Course Planner/02 Sources/'; H = os.path.dirname(os.path.abspath(__file__)); T = '/tmp/claude-0/crop'
os.makedirs(T, exist_ok=True)
C = 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf'; E = 'Textbooks/Edrolo U3&4/2023-edrolo-units-3-4.pdf'
J = [('dn1t', 'VCAA current/2023/2023 E1.pdf', 23, (76, 156, 378, 454)),
     ('dn1A', 'VCAA current/2023/2023 E1.pdf', 23, (105, 508, 522, 617)), ('dn1B', 'VCAA current/2023/2023 E1.pdf', 23, (105, 626, 522, 736)),
     ('dn1C', 'VCAA current/2023/2023 E1.pdf', 23, (105, 746, 522, 856)), ('dn1D', 'VCAA current/2023/2023 E1.pdf', 23, (105, 865, 522, 976)),
     ('dn1E', 'VCAA current/2023/2023 E1.pdf', 23, (105, 984, 522, 1093)),
     ('dn2', 'VCAA current/2025/2025 E1.pdf', 8, (115, 165, 670, 562)),
     ('dn3n', 'VCAA current/2023/2023 E2.pdf', 24, (110, 155, 735, 412)), ('dn3t', 'VCAA current/2023/2023 E2.pdf', 24, (66, 530, 545, 992)),
     ('dn4', 'VCAA current/2023/2023 E2.pdf', 16, (180, 120, 470, 287)),
     ('apk', 'VCAA past/2021/2021 E2.pdf', 23, (150, 543, 727, 727)),
     ('ex1', 'VCAA past/2020/2020 E1.pdf', 27, (180, 158, 640, 387)),
     ('ex2', 'VCAA past/2018/2018 E2.pdf', 24, (190, 158, 652, 412)),
     ('ex3', 'VCAA past/2021/2021 E1.pdf', 25, (100, 158, 705, 357)),
     ('cam10q', C, 711, (195, 330, 600, 462)), ('cam10a', C, 711, (140, 500, 645, 668)),
     ('cam11a', C, 712, (405, 490, 665, 605)), ('cam11b', C, 712, (405, 620, 665, 768)),
     ('cam11c', C, 713, (400, 85, 665, 245)), ('cam11d', C, 713, (400, 325, 665, 490)), ('cam11f', C, 713, (400, 645, 670, 812)),
     ('edr1t', E, 630, (78, 115, 356, 349)), ('edr1a', E, 630, (75, 910, 375, 1040)),
     ('edr2q', E, 631, (455, 700, 752, 832)), ('edr2a', E, 632, (148, 768, 425, 936)),
     ('lrn1', E, 631, (60, 465, 460, 642)), ('lrn2', E, 633, (60, 450, 460, 627)),
     ('edr3q', E, 633, (455, 685, 757, 857)), ('edr3a', E, 634, (113, 180, 420, 352)),
     ('edr4q', E, 635, (55, 140, 352, 305)), ('edr4a', E, 635, (93, 440, 405, 607))]
for n, f, p, b in J:
    o = f'{T}/{n}'
    subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(p), '-l', str(p), SRC + f, o], check=True, stderr=subprocess.DEVNULL)
    Image.open(o + '.png').crop(tuple(2 * v for v in b)).save(f'{H}/fig/{n}.png')
print(len(J), 'figures')
