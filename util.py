import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve


def make_a(n):
    """
    Creates a matrix that can be used to solve Euler-Bernoulli beam equations EIy''''=f(x)

    |16        -9        8/3       -1/4                                 |
    |          1         -4        6         -4        1                |
    |             ...       ...       ...       ...       ...           |
    |                    1         -4        6         -4        1      |
    |                              16/17     -60/17    72/17     -28/17 |
    |                              -12/17    96/17     -156/17   72/17  |


    :param n: the length of the matrix
    :return: a matrix with the necessary values to solve Euler-Bernoulli beam equations
    """
    e = sp.ones(n)
    A = spdiags([e, -4 * e, 6 * e, -4 * e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    B = csr_matrix([[16, -9, 8 / 3, -1 / 4],
                    [16 / 17, -60 / 17, 72 / 17, -28 / 17],
                    [-12 / 17, 96 / 17, -156 / 17, 72 / 17]])
    A[0, 0:4] = B[0, :]
    A[n - 2, n - 4:n] = B[1, :]
    A[n - 1, n - 4:n] = B[2, :]
    return A.tocsr()


def displacement(n: int, L: float, E: float, I: float, f: staticmethod) -> list:
    """
    A method for calculating the displacement of a beam

    :param n: number of steps
    :param L: length
    :param E: Young modulus
    :param f: weight function with weight of beam included
    :return: the displacement at each step
    """
    A = make_a(n)

    h = L / n

    b = [f(x) * h ** 4 / (E * I) for x in np.arange(n, L + n, h)]  # L+n is excluded, so last is L

    y = spsolve(A, b)

    return y
