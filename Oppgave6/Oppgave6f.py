import numpy as np
import scipy.sparse.linalg as ssl

from util import displacement, make_a

bestI = 0
bestC = 0
for i in range(10, 10 * 2 ** 11):
    a = make_a(i)
    cond = ssl.norm(a) * ssl.norm(a.inverse())


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
for n in range(1, 11):
    x = 10 * 2 ** n
    disp = displacement(x, L, E, I, f=f)[0][-1]
    e = abs(disp - c)
    if e < minE:
        minE = e
        minN = x

print('Minste feil er', minE, 'på n =', minN)  # n=1660 e=3.830370687296636e-09
