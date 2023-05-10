#
# mandelbrotlib.py

import numpy as np

np.warnings.filterwarnings("ignore")


def complex_matrix(xmin, xmax, ymin, ymax, density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def stability(z, c, niterations):
    for _ in range(niterations):
        z = z**2 + c
    return abs(z)


def calculate(xmin, xmax, ymin, ymax, density, niterations, z):
    print("************")
    c = complex_matrix(xmin, xmax, ymin, ymax, density)
    return stability(z, c, niterations)
