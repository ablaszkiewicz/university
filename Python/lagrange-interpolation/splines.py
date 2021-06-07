import numpy as np


def interpolate_data(original_data, defective_data):
    interpolated_data = np.array([original_data[i] for i in range(original_data.shape[0])])
    interpolated_data[:, 1] = 0

    coefficients = spline_coefficients(defective_data)
    step_length = defective_data[1, 0]
    step_counter = 0
    max_steps = defective_data.shape[0]

    for i in range(interpolated_data.shape[0]):
        x = interpolated_data[i][0]
        temp_coefficients = (coefficients[step_counter * 4], coefficients[step_counter*4 + 1],
                             coefficients[step_counter*4 + 2], coefficients[step_counter*4 + 3])

        interpolated_data[i, 1] = find_interpolated_y(temp_coefficients, x - step_length * step_counter)

        if x > (step_counter+1) * step_length and step_counter < max_steps - 2:
            step_counter += 1

    return interpolated_data


def find_interpolated_y(coefficients, wanted_x):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = coefficients[3]

    return (a * wanted_x**0) + (b * wanted_x**1) + (c * wanted_x**2) + (d * wanted_x**3)


def spline_coefficients(data):
    x = data[:, 0]
    y = data[:, 1]
    m = len(x)
    n = m - 1

    data = list(zip(x, y))
    h = float(data[1][0]) - float(data[0][0])

    A = np.zeros((4 * n, 4 * n))
    b = np.zeros((4 * n))

    for i in range(n):
        A[i][4 * i] = float(1)
        b[i] = float(data[i][1])

    for i in range(n):
        A[n + i][4 * i] = float(1)
        A[n + i][4 * i + 1] = h
        A[n + i][4 * i + 2] = h ** 2
        A[n + i][4 * i + 3] = h ** 3
        b[n + i] = float(data[i + 1][1])

    for i in range(n - 1):
        A[2 * n + i][4 * i + 1] = float(1)
        A[2 * n + i][4 * i + 2] = 2 * h
        A[2 * n + i][4 * i + 3] = 3 * h ** 2
        A[2 * n + i][4 * i + 5] = (-1)
        b[2 * n + i] = float(0)

    for i in range((n - 1)):
        A[2 * n + (n - 1) + i][4 * i + 2] = float(2)
        A[2 * n + (n - 1) + i][4 * i + 3] = 6 * h
        A[2 * n + (n - 1) + i][4 * i + 6] = -2
        b[2 * n + (n - 1) + i] = float(0)

    A[2 * n + (n - 1) + i + 1][2] = float(1)
    A[2 * n + (n - 1) + i + 2][4 * n - 2] = float(2)
    A[2 * n + (n - 1) + i + 2][4 * n - 1] = 6 * h

    vect_x = pivoting(A, b)

    return vect_x


def pivoting(A, b):

    N, n = np.shape(A)
    L = np.eye(n)
    P = np.eye(n)
    U = A

    for i in range(n-1):

        best = np.absolute(U[i][0])
        ind = 0

        for j in range(i, n):
            if np.absolute(U[j][i]) > best:
                best = np.absolute(U[j][i])
                ind = j

        for k in range(i, n):
            U[ind][k], U[i][k] = U[i][k],  U[ind][k]

        for k in range(i):
            L[ind][k], L[i][k] = L[i][k], L[ind][k]

        for k in range(n):
            P[ind][k], P[i][k] = P[i][k], P[ind][k]

        for j in range(i+1, n):
            L[j][i] = U[j][i]/U[i][i]
            for k in range(i, n):
                U[j][k] = U[j][k] - L[j][i] * U[i][k]

    y = np.ones(n)
    b = np.dot(P, b)

    for i in range(n):
        val = b[i]
        for j in range(i):
            if j != i:
                val -= L[i][j] * y[j]
        y[i] = val / L[i][i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        val = y[i]
        for j in range(i, n):
            if j != i:
                val -= U[i][j] * x[j]
        x[i] = val / U[i][i]

    return x


