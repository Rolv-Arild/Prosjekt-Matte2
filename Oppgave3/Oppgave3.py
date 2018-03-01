from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix

A = csr_matrix([[2, 3, 5],  # Example matrix
                [7, 11, 13],
                [17, 19, 23]])
b = [1, 2, 3]

y = spsolve(A, b)

print(y)
