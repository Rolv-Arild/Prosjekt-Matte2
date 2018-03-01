import scipy as sp
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix


def make_a(n):
    e = sp.ones(n)
    A = spdiags([e, -4*e, 6*e, -4*e, e], [-2, -1, 0, 1, 2], n, n)
    A = lil_matrix(A)
    B = csr_matrix([[1, 2, 3, 4],  # Example matrix
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
    A[0, 0:4] = B[0, :]
    A[n-2, n-4:n] = B[1, :]
    A[n-1, n-4:n] = B[2, :]
    return A
