import matplotlib.pyplot as pl

from util import displacement

w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0


def s_2(x):
    if L - 0.3 <= x <= L:
        return -g * 50 / 0.3
    else:
        return 0


def f(x):
    return - p * w * d * g + s_2(x)


print(displacement(20000, L, E, I, f)[-1])

plot1 = []
plot2 = []
for n in range(1, 12):
    x = 10 * 2 ** n
    disp = displacement(x, L, E, I, f=f)[-1]
    plot1.append(disp)
    plot2.append(x)

pl.plot(plot2, plot1, label='$y_c$(L)')

pl.legend(loc='best')
pl.ylabel('y')
pl.xlabel('n')
pl.show()
