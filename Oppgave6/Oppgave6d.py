import matplotlib.pyplot as pl
import numpy as np
from scipy.sparse.linalg import norm

from util import displacement, make_a

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

maxE = 0
maxN = 0
plot1 = []
plot2 = []
plot3 = []
plot4 = []
for n in range(20, 10 * 2 ** 11, 20):
    disp = displacement(n, L, E, I, f=f)[-1]
    e = abs(disp - c)
    plot2.append(n)
    plot1.append(e)
    a = make_a(n)
    plot3.append(2 ** -52 * norm(a) * norm(a.transpose()))
    plot4.append((L / n) ** 2)
    if e > maxE:
        maxE = e
        maxN = n

# pl.plot([1, 2, 3, 4])
pl.plot(np.log10(plot2), np.log10(plot1), label='error(L)')
pl.plot(np.log10(plot2), np.log10(plot3), label='$\epsilon_{mach}$cond(A)')
pl.plot(np.log10(plot2), np.log10(plot4), label='$h^2$')

pl.legend(loc='best')
pl.ylabel('$log_{10}$(y)')
pl.xlabel('$log_{10}$(n)')
pl.show()
