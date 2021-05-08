import matplotlib.pyplot as plt
import random

# Configuration
iterations = 100

# Population
population_size = 10

# Function
function_min = -5
function_max = 5


def fitness():
    ...


def random_in_range():
    return float("%.1f" % random.uniform(function_min, function_max))


def show_plot():
    x_values = [pair[0] for pair in points]
    y_values = [pair[1] for pair in points]
    plt.scatter(x_values, y_values)
    plt.pause(2)

def new_generation():
    ...

for _ in range(iterations):
    points = [(random_in_range(), random_in_range()) for _ in range(population_size)]
    show_plot()
