import numpy as np

from util import displacement

w = 0.3
d = 0.03
p_1 = 480
p_2 = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0


def correct(x):
    return -p_1 * w * d * g / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2) - g * p_2 * L / (
            E * I * np.pi) * (
                   L ** 3 / (np.pi ** 3) * np.sin(np.pi * x / L) - x ** 3 / 6 + L * x ** 2 / 2 - L ** 2 * x / (
                   np.pi ** 2))


def error_margin(): return [
    abs(displacement(n, L, E, I, f=lambda x: - p_1 * w * d * g - p_2 * g * np.sin(np.pi * x / L))[-1] - correct(L))
    for n in range(20, 10 * 2 ** 11, 20)
]


e = error_margin()
print(max(e))
