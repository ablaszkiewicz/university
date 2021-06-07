import numpy as np

def find_interpolated_y(data, wanted_x):
    x = data[:, 0]
    y = data[:, 1]
    m = len(x)
    n = m - 1

    yp = 0
    for i in range(n+1):
        p = 1
        for j in range(n+1):
            if j != i:
                p *= (wanted_x - x[j]) / (x[i] - x[j])
        yp += y[i]*p

    # print('For x = ', wanted_x, 'Y =', yp)
    return yp

def interpolate_data(original_data, defective_data):
    interpolated_data = np.array([original_data[i] for i in range(original_data.shape[0])])
    interpolated_data[:, 1] = 0

    for i in range(interpolated_data.shape[0]):
        interpolated_data[i][1] = find_interpolated_y(defective_data, interpolated_data[i][0])

    return interpolated_data