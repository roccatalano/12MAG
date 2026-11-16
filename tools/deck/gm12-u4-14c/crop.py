"""Crop the figures for 14C from the source PDFs (200 dpi). Boxes in 100-dpi page pixels (x0, y0, x1, y1).
Run with the sources staged under /mnt/user-data/uploads/12MAG Course Planner/02 Sources."""
import os, subprocess, sys
from PIL import Image
SRC = '/mnt/user-data/uploads/12MAG Course Planner/02 Sources/'; H = os.path.dirname(os.path.abspath(__file__)); T = '/tmp/claude-0/crop'
os.makedirs(T, exist_ok=True)
J = [('dn3', 'VCAA current/2024/2024 NHT E2.pdf', 21, (250, 255, 612, 476)),
     ('dn4', 'VCAA current/2025/2025 E2.pdf', 12, (140, 168, 572, 442)),
     ('apk', 'VCAA past/2018/2018 E1.pdf', 23, (195, 338, 528, 582)),
     ('ex1', 'VCAA past/2017/2017 E2.pdf', 22, (150, 163, 702, 500)),
     ('cam7', 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf', 698, (402, 232, 668, 336)),
     ('camdum', 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf', 699, (425, 383, 672, 490)),
     ('cam8', 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf', 700, (352, 110, 668, 236)),
     ('cam9', 'Textbooks/Cambridge U3&4/2023-cambridge-units-3-4.pdf', 700, (316, 380, 668, 502)),
     ('edr2', 'Textbooks/Edrolo U3&4/2023-edrolo-units-3-4.pdf', 617, (55, 666, 378, 787)),
     ('edr3', 'Textbooks/Edrolo U3&4/2023-edrolo-units-3-4.pdf', 617, (55, 873, 342, 992)),
     ('edr4', 'Textbooks/Edrolo U3&4/2023-edrolo-units-3-4.pdf', 620, (92, 498, 362, 597))]
for n, f, p, b in J:
    o = f'{T}/{n}'
    subprocess.run(['pdftoppm', '-r', '200', '-png', '-singlefile', '-f', str(p), '-l', str(p), SRC + f, o], check=True, stderr=subprocess.DEVNULL)
    Image.open(o + '.png').crop(tuple(2 * v for v in b)).save(f'{H}/fig/{n}.png')
    print(n)
