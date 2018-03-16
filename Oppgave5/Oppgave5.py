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
    return abs(displacement(n, L, E, I, f=f)[-1] - c)


maxE = 0
maxN = 0
for n in range(20, 10 * 2 ** 11, 20):
    e = error_margin(n)
    if e > maxE:
        maxE = e
        maxN = n

print(maxN, maxE)  # 18900 0.00033555218550867724
