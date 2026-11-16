from .deck import *
from . import deck as _d
_d.use("normal")
"""Normal curve engine (S5): nx/nz/np rows, ns shaded region (sh()), nm mark (mk()), ncl clear, smp samples."""
import json
def ncurve(id_, m=None, s=None, xl='', dec=0, z=True, x=True, small=False):
    """Normal curve (teacher illustration). x row = mean ± k·s (shown by the nx step), z row (nz), section % (np)."""
    cfg = dict(m=m, s=s, xl=xl, dec=dec, z=z, x=(x and m is not None))
    return f"<svg class=\"zn{' zns' if small else ''}\" id=\"{id_}\" data-cfg='{json.dumps(cfg)}' viewBox=\"0 0 700 300\"></svg>"
def sh(id_, a, b, lab='', col='b'): return f'ns:{id_}:{a}:{b}:{col}:{lab.replace(" ", "_")}'
def mk(id_, zv, lab, col='r'): return f'nm:{id_}:{zv}:{col}:{lab.replace(" ", "_")}'
