import numpy as np
from scipy.sparse import csr_matrix
from util import make_a, displacement


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


n = 10

y_e = csr_matrix([correct(x/n) for x in range(2, 21, 2)])

Ay_e = (1/(0.2**4)) * (make_a(n).dot(y_e.T))


y4_e = csr_matrix([f(1)/(E*I) for x in range(0, n)]).T


y_c = csr_matrix(displacement(n, L, E, I, f))
print(np.max(abs(y_c - y_e)))

