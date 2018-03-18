import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from util import make_a, displacement


w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * d ** 3 / 12
E = 1.3E10
L = 2.0
n = 10


def f(x):
    return - p * w * d * g


def correct(x):
    return f(x) / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2)


A = make_a(n)

# Oppgave4c
y_e = csr_matrix([correct(x/n) for x in range(2, 21, 2)])
Ay_e = (1/(0.2**4)) * (A.dot(y_e.T))

# Oppgave 4d
y4_e = csr_matrix([f(1)/(E*I) for x in range(0, n)]).T


# Oppgave 4e
y_c = csr_matrix(displacement(n, L, E, I, f)[0])
print(np.max(abs(y_c - y_e)))


# Cond A
condA = sp.sparse.linalg.norm(A) * sp.sparse.linalg.norm(sp.sparse.linalg.inv(A))
print(condA)
