import numpy as np
from scipy.sparse.linalg import spsolve

from Oppgave2.Oppgave2 import make_a


def displacement(n, L, w, d, p, E, g=-9.81, f=None):
    """
    A method for calculating the displacement of a beam

    :param n: number of steps
    :param L: length
    :param w: width
    :param d: thickness
    :param p: density
    :param E: Young modulus
    :param g: gravitational constant
    :param f: weight function
    :return: the displacement at each step
    """
    A = make_a(n)

    if f is None:
        def f(x): return p * w * d * g

    h = L / n
    I = w * d ** 3 / 12

    b = [f(x) * h ** 4 / (E * I) for x in np.arange(n, L + n, h)]

    y = spsolve(A, b)

    return y


print(displacement(10, 2.0, 0.3, 0.03, 480, 1.3E10))

# Should be y(x) = (f/24EI)x^2(x^2-4Lx+6L^2) = -0.000201231x^2(x^2-8x+24)
#   {-0.000180625, -0.000674848, -0.00141699, -0.00234909, -0.00342093,
#    -0.00459, -0.00582153, -0.00708848, -0.00837153, -0.00965909}
