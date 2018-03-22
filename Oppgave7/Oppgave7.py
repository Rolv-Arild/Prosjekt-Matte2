import matplotlib.pyplot as pl

from util import displacement

w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0
dw = 50
df = 0.3


def s_2(x):
    if L - df <= x <= L:
        return -g * dw / df
    else:
        return 0


def f(x):
    return - p * w * d * g + s_2(x)


disp = displacement(1280, L, E, I, f)

print("y(L) =", disp[-1])

plotx = [L * i / len(disp) for i in range(1, len(disp) + 1)]

pl.plot(plotx, disp, label='$y_c$(x)')

pl.legend(loc='best')
pl.ylabel('y')
pl.xlabel('n')
pl.axis('scaled')
pl.show()
