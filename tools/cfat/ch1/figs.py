"""Red solution figures for CFAT 1.1.2 Q8d (boxplot on the student grid) and CFAT 1.1.3 Q8a (filled normal curve).
Base images are taken from the student HTML (lessons/CFAT-1.1.x.html); writes fig/*.png."""
import os, re, base64, io
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(HERE, '..', '..', '..', 'lessons')
def imgs(f): return [Image.open(io.BytesIO(base64.b64decode(b))).convert('RGB') for b in re.findall(r'data:image/png;base64,([^"]+)', open(os.path.join(L, f)).read())]
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
RED = (204, 0, 0)
def boxplot():
    im = imgs('CFAT-1.1.2.html')[4]; d = ImageDraw.Draw(im)
    X = lambda v: 137 + (v - 40) * (1422 - 137) / 70
    y0, y1, ym = 70, 175, 122
    d.rectangle([X(45.5), y0, X(62.5), y1], outline=RED, width=5)
    d.line([X(51.5), y0, X(51.5), y1], fill=RED, width=5)
    d.line([X(40), ym, X(45.5), ym], fill=RED, width=5); d.line([X(62.5), ym, X(76), ym], fill=RED, width=5)
    for v in (40, 76): d.line([X(v), ym - 18, X(v), ym + 18], fill=RED, width=5)
    d.ellipse([X(109) - 11, ym - 11, X(109) + 11, ym + 11], outline=RED, width=5)
    im.save(os.path.join(HERE, 'fig', 'q112_8d.png'))
def normal():
    im = imgs('CFAT-1.1.3.html')[0]; d = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, 34)
    tops = [((36, 432, 165, 498), '0.15'), ((86, 276, 214, 343), '2.35'), ((234, 119, 362, 186), '13.5'), ((512, 304, 627, 371), '34'),
            ((676, 304, 792, 371), '34'), ((941, 119, 1070, 186), '13.5'), ((1089, 276, 1218, 343), '2.35'), ((1139, 432, 1267, 498), '0.15')]
    for (a, b, c, e), t in tops: d.text(((a + c) / 2, (b + e) / 2), t, fill=RED, font=f, anchor='mm')
    for x, v in zip((158, 322, 487, 652, 816, 980, 1145), (104, 116, 128, 140, 152, 164, 176)):
        d.text((x, 677), str(v), fill=RED, font=ImageFont.truetype(FONT, 40), anchor='mm')
    im.save(os.path.join(HERE, 'fig', 'q113_8a.png'))
if __name__ == '__main__': boxplot(); normal()
