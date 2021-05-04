import numpy as np
import time
import matplotlib.pyplot as plt

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


def lu(A):
    n = A.shape[0]

    U = A.copy()
    L = np.eye(n, dtype=np.double)

    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return L, U


def forward_substitution(L, b):
    n = L.shape[0]

    y = np.zeros_like(b, dtype=np.double);

    y[0] = b[0] / L[0, 0]

    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    return y


def back_substitution(U, y):
    n = U.shape[0]

    x = np.zeros_like(y, dtype=np.double);

    x[-1] = y[-1] / U[-1, -1]

    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i:], x[i:])) / U[i, i]

    return x


def lu_solve(A, b):
    L, U = lu(A)
    b = np.squeeze(b)
    y = forward_substitution(L, b)

    return back_substitution(U, y)

a1 = 3
x_test = lu_solve(A, b)
print("Norma z residuum dla LU:", np.linalg.norm(np.matmul(A, x_test) - b))

# -------- TASK E --------

a1 = 5 + e
Ns = [100, 500, 1000, 2000, 3000]
czasy_gauss = []
czasy_jacobi = []
czasy_lu = []

for i in Ns:
    N = i

    A = np.zeros((N, N))
    i, j = np.indices(A.shape)
    A[i == j + 2] = a3
    A[i == j + 1] = a2
    A[i == j] = a1
    A[i == j - 1] = a2
    A[i == j - 2] = a3

    b = np.fromfunction(lambda i, j: np.sin(j * (f + 1)), (1, N))

    start = time.time()
    gauss(A, b, 10 ** -6)
    end = time.time()
    czasy_gauss.append(end - start)

    start = time.time()
    jacobi(A, b, 10 ** -6)
    end = time.time()
    czasy_jacobi.append(end - start)

    start = time.time()
    lu_solve(A, b)
    end = time.time()
    czasy_lu.append(end - start)


fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(Ns, czasy_gauss, label="Gauss")
ax.plot(Ns, czasy_jacobi, label="Jacobi")
ax.plot(Ns, czasy_lu, label="LU")

plt.xlabel("Matrix size")
plt.ylabel("Time [ms]")
plt.title("Linear equations")
plt.legend(loc="upper right")
plt.show()
