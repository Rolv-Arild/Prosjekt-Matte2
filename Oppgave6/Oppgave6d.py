import matplotlib.pyplot as pl
import numpy as np

from util import displacement, make_a, cond

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
plotx = []
plot1 = []
plot2 = []
plot3 = []
for n in range(1, 12):
    x = 10 * 2 ** n
    disp = displacement(x, L, E, I, f=f)[-1]
    con = cond(make_a(x))
    e = abs(disp - c)
    plotx.append(x)
    plot1.append(e)
    plot2.append(2 ** -52 * con)
    plot3.append((L / x) ** 2)
    if e > maxE:
        maxE = e
        maxN = x

# pl.plot([1, 2, 3, 4])
pl.loglog(plotx, plot1, label='error(L)')
pl.loglog(plotx, plot2, label='$\epsilon_{mach}$cond(A)')
pl.loglog(plotx, plot3, label='$h^2$')

pl.legend(loc='best')
pl.ylabel('y')
pl.xlabel('n')
pl.show()
