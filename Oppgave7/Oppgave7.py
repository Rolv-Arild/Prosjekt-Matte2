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
