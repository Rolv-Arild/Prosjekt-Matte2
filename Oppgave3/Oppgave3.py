import numpy as np

from util import displacement

w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0
n = 10000


def f(x):
    return - p * w * d * g


print(displacement(n, L, E, I, f=f)[n // 10])

# Should be y(x) = (f/24EI)x^2(x^2-4Lx+6L^2) = -0.000201231x^2(x^2-8x+24)
#   {-0.000180625, -0.000674848, -0.00141699, -0.00234909, -0.00342093,
#    -0.00459, -0.00582153, -0.00708848, -0.00837153, -0.00965909}
