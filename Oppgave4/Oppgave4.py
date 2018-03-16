from util import make_a


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


y_e = [correct(x/10) for x in range(2, 21, 2)]

print()