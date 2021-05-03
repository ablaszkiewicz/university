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

b = np.fromfunction(lambda i, j: np.sin(j*(f+1)), (1, N))

# -------- TASK B GAUSS --------

def gauss(A, b, min_norm):
    iter = 0

    x = np.zeros((b.size, 1))
    L = np.tril(A)
    U = A - L

    current_norm = np.inf
    while current_norm > min_norm:
        x = np.linalg.inv(L)@(b - U@x)
        current_norm = np.linalg.norm(np.matmul(A, x) - b)
        iter += 1

        assert not np.isnan(current_norm), "Norm is nan"
        assert not np.isinf(current_norm), "Norm is inf"
    return x, iter


result, iter = gauss(A, b, 10 ** -6)
print("Iteracje gauss:", iter)

# -------- TASK B JACOBI --------

def jacobi(A, b, min_norm):
    iter = 0

    x = np.zeros((b.size, 1))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(A)

    fst = -(L + U) / D
    snd = b / D

    current_norm = np.inf
    while current_norm > min_norm:
        x = fst@x + snd
        current_norm = np.linalg.norm(np.matmul(A, x) - b)
        iter += 1

        assert not np.isnan(current_norm), "Norm is nan"
        assert not np.isinf(current_norm), "Norm is inf"
    return x, iter


result, iter = jacobi(A, b, 10 ** -6)
print("Iteracje jacobi:", iter)

# -------- TASK C --------

# Wywołałem powyższy kod dla wartości a1=3 i dla obydwu metod wyrzuca
# assert np.isinf(current_norm), więc metody nie zbiegają się

# -------- TASK D --------