"""Data for lesson l15 (4D): shared helpers and data from l14/l12 figs (values copied from the source tables)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f14', os.path.join(H, '..', 'l14', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
scat, W_, WEEK, DIST, DOC, LIFE = _f.scat, _f.W_, _f.WEEK, _f.DIST, _f.DOC, _f.LIFE
