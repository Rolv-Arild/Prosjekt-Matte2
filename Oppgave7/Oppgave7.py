import matplotlib.pyplot as pl

from util import displacement, make_a, cond

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


print(displacement(1280, L, E, I, f)[-1])

plotx = []
plot1 = []
for n in range(1, 12):
    x = 10 * 2 ** n
    disp = displacement(x, L, E, I, f=f)[-1]
    plot1.append(disp)
    plotx.append(x)

pl.plot(plotx, plot1, label='$y_c$(L)')

pl.legend(loc='best')
pl.ylabel('y')
pl.xlabel('n')
pl.show()

m = 10000
mN = 0
for n in range(1, 11):
    x = 10 * 2 ** n
    con = cond(make_a(x))
    v = 2 ** -52 * con + (L / x) ** 2
    if v < m:
        m = v
        mN = x
print("Optimal n =", mN, "med verdi:", m)
