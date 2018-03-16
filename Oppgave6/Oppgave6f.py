import numpy as np

from util import displacement

w = 0.3
d = 0.03
p_1 = 480
p_2 = 100
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0


def f(x):
    return - p_1 * w * d * g - p_2 * g * np.sin(np.pi * x / L)


def correct(x):
    return -p_1 * w * d * g / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2) - g * p_2 * L / (
            E * I * np.pi) * (
                   L ** 3 / (np.pi ** 3) * np.sin(np.pi * x / L) - x ** 3 / 6 + L * x ** 2 / 2 - L ** 2 * x / (
                   np.pi ** 2))


c = correct(L)

minE = 1000
minN = 0
for n in range(20, 10 * 2 ** 11, 20):
    disp = displacement(n, L, E, I, f=f)[-1]
    e = abs(disp - c)
    if e < minE:
        minE = e
        minN = n

print('Minste feil er', minE, 'på n =', minN)  # n=1660 e=3.830370687296636e-09
