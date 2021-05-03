import numpy as np

# -------- TASK A --------
INDEX = 175715
c = int(str(INDEX)[-2])
d = int(str(INDEX)[-1])
e = int(str(INDEX)[3])
f = int(str(INDEX)[2])

a1 = 5 + e
a2 = -1
a3 = -1
N = 9*c*d

A = np.zeros((N, N))
i, j = np.indices(A.shape)
A[i == j+2] = a3
A[i == j+1] = a2
A[i == j] = a1
A[i == j-1] = a2
A[i == j-2] = a3

b = np.fromfunction(lambda i, j: np.sin(j*(f+1)), (1, N));

# -------- TASK B1 --------

