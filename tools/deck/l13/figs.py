"""Data for lesson l13 (4B). Values copied from the source tables; where only a plot is printed, points are read off the source figure (close approximation)."""
import os, importlib.util, math
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f12', os.path.join(H, '..', 'l12', 'figs.py')); _f = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f)
scat, W_, corr, lsq, LIFE, LIFE_TL, TIDE, WEEK, DIST = _f.scat, _f.W_, _f.corr, _f.lsq, _f.LIFE, _f.LIFE_TL, _f.TIDE, _f.WEEK, _f.DIST
lg = lambda v: math.log10(v)
# Cambridge U3&4 4B CAS 2 table (lifespan years, GDP dollars; 12 countries). Example 3's scatterplot (13 countries) is drawn from this table.
LIFESPAN = [80.4, 79.8, 79.2, 77.4, 78.8, 81.5, 74.9, 72.0, 77.9, 70.3, 73.0, 68.6]
GDP = [36032, 34484, 26664, 41890, 26893, 25592, 7454, 1713, 7073, 1192, 631, 1302]
# Cambridge U3&4 4B Example 4: log(cases) read off the transformed plot (p. 223); cases = 10^log
DAY = list(range(1, 13)); LCASES = [1.30, 1.45, 1.73, 1.80, 2.40, 2.55, 2.48, 2.90, 3.13, 3.18, 3.52, 3.84]
CASES = [round(10 ** v) for v in LCASES]
# planner/written-youtrys.json YT-4B-4 (written for 12MAG)
FWEEK = list(range(1, 11)); FOLL = [15, 22, 36, 51, 80, 118, 190, 276, 440, 650]
# Edrolo U3&4 3E Q12 (VCAA 2017 Exam 2 Q4): year, area (hectares)
YEAR = list(range(1900, 1981, 10)); AREA = [66, 80, 100, 120, 160, 190, 210, 240, 340]
# Edrolo U1&2 8D Q14 (adapted from VCAA 2017 Exam 1 Q4): histogram frequencies for log10(population) bins 0-1 ... 4-5
POPF = [1, 3, 3, 2, 3]
