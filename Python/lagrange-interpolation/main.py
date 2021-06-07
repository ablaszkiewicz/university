import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lagrange as lagrange
import splines as splines


def initialize_data(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    return df.to_numpy()


def plot_data(original_data, interpolated_data, reference_points):
    fig, axs = plt.subplots()

    plt.title("Lagrange interpolation")
    plt.ylim(500, 800)

    plt.plot(original_data[:, 0], original_data[:, 1], label="Original data")
    plt.plot(interpolated_data[:, 0], interpolated_data[:, 1], label="Interpolated data")
    plt.scatter(reference_points[:, 0], reference_points[:, 1], label="Reference points", color="hotpink")

    axs.legend()
    plt.show()


def discretize_data(data, step):
    discretized_data = np.array([data[i] for i in range(0, data.shape[0], step)])
    return discretized_data


def interpolate_lagrange(data, step):
    defective_data = discretize_data(data, step)
    interpolated_data = lagrange.interpolate_data(data, defective_data)
    plot_data(data, interpolated_data, defective_data)


def interpolate_splines(data, step):
    defective_data = discretize_data(data, step)
    interpolated_data = splines.interpolate_data(data, defective_data)
    plot_data(data, interpolated_data, defective_data)


original_data = initialize_data("data/uluru.csv")
#interpolate_lagrange(original_data, 25)
interpolate_splines(original_data, 40)
