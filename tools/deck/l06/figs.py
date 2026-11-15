"""Data for lesson l06 (2F). Values read off the source figures/tables (VCAA scatterplots redrawn; points approximate where read off a plot)."""
import os, random, math, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('f5', os.path.join(H, '..', 'l05', 'figs.py')); _f5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(_f5)
scat, W_, FOOT = _f5.scat, _f5.W_, _f5.FOOT  # FOOT = Cambridge U1&2 7B #2 height/foot length data

# VCAA 2025 NHT Exam 1 Q8-9 (study time vs test scores; read off the scatterplot)
STUDY = [(0, 35), (0, 28), (0.5, 53), (0.5, 48), (0.5, 35), (1, 60), (1, 57), (1, 53), (1, 48), (1, 42), (1, 35), (1.5, 77), (1.5, 71), (1.5, 65),
         (1.5, 61), (1.5, 58), (1.5, 55), (1.5, 49), (1.5, 44), (2, 79), (2, 73), (2, 69), (2, 60), (2, 50), (2.5, 80), (2.5, 66), (4, 98)]
# VCAA 2024 Exam 1 Q5 (siblings, 2 rows of 12)
SIB = [[2, 1, 3, 2, 1, 1, 1, 4, 1, 1, 1, 1], [1, 2, 1, 2, 2, 1, 3, 4, 2, 2, 3, 1]]
# VCAA 2023 Exam 2 Q3 (temperature, consumption; read off the scatterplot)
ICE = [(-4.5, .121), (-3.3, .141), (-2.2, .135), (0, .156), (0, .127), (4.5, .150), (5, .183), (6.7, .162), (8.5, .136), (12.7, .158), (14, .172),
       (15, .177), (16, .155), (17.3, .180), (17.3, .186), (18.4, .170), (19.5, .183), (20, .201), (20.7, .192), (22.2, .210), (22.2, .200)]
# Cambridge U3&4 2F CAS 2 (income $'000, CO2 tonnes)
INC = [8.9, 23.0, 7.5, 8.0, 18.0, 16.7, 5.2, 12.8, 19.1, 16.4, 21.7]
CO2 = [7.5, 12.0, 6.0, 1.8, 7.7, 5.7, 3.8, 5.7, 11.0, 9.7, 9.9]
# Edrolo U3&4 2D WE1 (grade %, lectures attended)
GRADE = [75, 61, 92, 53, 47, 86, 74]; LECT = [11, 6, 10, 5, 2, 8, 9]
# VCAA 2020 Exam 2 Q6 (mean age, mean height of women)
AGEGRP = ['Twenties', 'Thirties', 'Forties', 'Fifties', 'Sixties', 'Seventies', 'Eighties']
AGE = [26.3, 35.2, 45.2, 55.3, 65.1, 74.8, 83.1]; HT = [167.1, 164.9, 164.8, 163.4, 161.2, 158.4, 156.7]


def rcloud(r, n=40, seed=1):
    """points with sample correlation exactly r (for the 'what r looks like' gallery)"""
    g = random.Random(seed)
    x = [g.gauss(0, 1) for _ in range(n)]; e = [g.gauss(0, 1) for _ in range(n)]
    def z(v):
        m = sum(v) / len(v); s = math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)); return [(a - m) / s for a in v]
    x = z(x); e = z(e)
    b = sum(a * c for a, c in zip(x, e)) / (n - 1); e = z([c - b * a for a, c in zip(x, e)])  # make e uncorrelated with x
    y = [r * a + math.sqrt(max(0, 1 - r * r)) * c for a, c in zip(x, e)]
    return list(zip(x, y))


def corr(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    sab = sum((x - ma) * (y - mb) for x, y in zip(a, b)); sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return sab / (sa * sb)
