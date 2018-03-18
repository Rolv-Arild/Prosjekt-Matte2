from util import displacement

w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0


def f(x):
    return - p * w * d * g


def correct(x):
    return -p * w * d * g / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2)


c = correct(L)


def error_margin(n):
    return abs(displacement(n, L, E, I, f=f)[0][-1] - c)


maxE = 0
maxN = 0
errs = []
plot2 = []
for n in range(1, 11):
    x = 10 * 2 ** n
    e = error_margin(x)
    errs.append(e)
    plot2.append(x)
    if e > maxE:
        maxE = e
        maxN = x

print('Største feil er', maxE, 'på n =', maxN)  # n=18900 e=0.00033555218550867724
print(errs)
