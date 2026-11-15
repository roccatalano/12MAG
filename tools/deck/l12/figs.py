"""Data for lesson l12 (4A). Values read off the source figures/tables (VCAA scatterplots redrawn; points read off the grid)."""
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f9', os.path.join(H, '..', 'l09', 'figs.py')); _f9 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f9)
scat, W_, corr, lsq = _f9.scat, _f9.W_, _f9.corr, _f9.lsq

# VCAA 2024 NHT Exam 1 Q9-10 (life expectancy, income; 42 countries; read off the grid at 160 dpi: pixel -> value)
_PX = [(101,530),(121,525),(225,481),(240,339),(252,458),(266,181),(268,480),(269,503),(269,529),(281,429),(279,494),(311,411),(315,512),(319,482),
       (325,482),(325,520),(336,523),(341,544),(368,313),(373,432),(383,485),(384,365),(385,357),(389,170),(392,475),(424,511),(427,432),(440,333),
       (443,432),(457,341),(482,511),(489,473),(498,411),(530,461),(544,476),(560,511),(584,396),(593,420),(711,62),(824,218),(847,84),(860,303)]
LIFE = [(round(55 + (x - 83) / 39.35, 1), round((576 - y) / 566 * 14000, -1)) for x, y in _PX]
LIFE_TL = ((55, 870), (75, 8380))   # printed least squares line (end points read off)
# VCAA 2024 NHT Exam 2 Q4 (LLT, HHT in m; 31 days of July 2021; read off the grid)
TIDE = [(0.22,2.02),(0.22,1.98),(0.25,1.90),(0.27,2.01),(0.31,1.78),(0.35,1.96),(0.38,1.64),(0.40,1.81),(0.41,1.84),(0.41,1.76),(0.42,1.85),
        (0.42,1.39),(0.43,1.68),(0.44,1.84),(0.45,1.58),(0.45,1.40),(0.46,1.77),(0.47,1.57),(0.48,1.81),(0.49,1.87),(0.49,1.66),(0.52,1.50),
        (0.54,1.77),(0.54,1.60),(0.58,1.47),(0.58,1.41),(0.60,1.71),(0.61,1.46),(0.62,1.65),(0.62,1.59),(0.62,1.52)]
# Cambridge U3&4 4A Example 1 / CAS 1 (base jumper: time s, height m)
TIME = list(range(11)); JUMP = [1560, 1555, 1540, 1516, 1482, 1438, 1383, 1320, 1246, 1163, 1070]
# Cambridge U3&4 4A Example 2 (fertiliser mL, yield^2 read off the transformed plot; close approximation)
FERT = list(range(11)); YLD2 = [4.5, 6.0, 10.0, 11.5, 13.0, 16.0, 19.0, 21.5, 20.5, 27.0, 27.0]
YLD = [round(v ** 0.5, 2) for v in YLD2]
# Edrolo U3&4 3D Worked example 2
EX = [3, 4, 5, 6, 7]; EY = [8, 17, 24, 33, 52]
# Edrolo U3&4 3E Worked example 1 (week, distance km)
WEEK = list(range(1, 11)); DIST = [0.8, 3.2, 4.5, 5.2, 5.9, 6.4, 7, 7.4, 7.6, 7.7]
