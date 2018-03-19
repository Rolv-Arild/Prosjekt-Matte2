import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import norm, inv
from util import make_a, displacement


w = 0.3
d = 0.03
p = 480
g = 9.81
I = w * (d ** 3) / 12
E = 1.3E10
L = 2.0
n = 10


def f(x):  # constant f(x)
    return - p * w * d * g


def correct(x):  # The correct y(x) for constant f(x)=f
    return f(x) / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2)


A = make_a(n)  # A matrix
condA = norm(A) * norm(inv(A))  # Cond A

# Oppgave4c
y_e = (csr_matrix([correct(x/n) for x in range(2, 21, 2)])).T
Ay_e = csr_matrix((1/((L/n)**4)) * (A.dot(y_e)))

print("Oppgave 4c:")
print(Ay_e)


# Oppgave 4d
y4_e = csr_matrix([f(x)/(E*I) for x in range(0, n)]).T
FE = norm(abs(y4_e - Ay_e), 1)  # Forward Error
RFE = norm(abs(Ay_e - y4_e), sp.inf) / norm(abs(y4_e), sp.inf)  # Relative Forward Error
RBE = 2**-52  # Relative Backwards Error (Given in assignment)
ErrMag = RFE/RBE  # Error Magnification Factor

print("\n\nOppgave 4d:")
print("Forward error: ", FE, " or ", FE / (2**-52), " machineeps")
print("Relative Forward error: ", RFE, " or ", RFE / (2**-52), " machineeps")
print("Relative Backward error: ", RBE, " or ", RBE / (2**-52), " machineeps")
print("Error Magnification Factor: ", ErrMag)
print("Condition Number of A: ", condA)


# Oppgave 4e
y_c = (csr_matrix(displacement(n, L, E, I, f))).T
FE = norm(abs(y_c-y_e), 1)

print("\n\nOppgave 4e:")
print("Forward error: ", FE / (2**-52), " machineeps")

