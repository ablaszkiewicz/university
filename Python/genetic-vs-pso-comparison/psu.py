import matplotlib.pyplot as plt
import random
import helper

# Configuration
iterations = 100

# Population
population_size = 10

# Function
function_min = -5
function_max = 5

# PSO variables

w = 0.7 # interia
c1 = 1.5 # cognitive (self)
c2 = 1.5 # social (swarm)
swarm_best_position = helper.Point(0, 0)


def random_in_range():
    return float("%.1f" % random.uniform(function_min, function_max))


def show_plot():
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    plt.scatter(x_values, y_values)
    plt.pause(0.1)


def random_population():
    return [helper.Point(random_in_range(), random_in_range()) for _ in range(population_size)]


def calculate_new_velocities(points):
    for point in points:
        # learning part
        learning_part_x = w * point.x_velocity
        learning_part_y = w * point.y_velocity

        # social part
        social_part_x = random.random() * c2 * (swarm_best_position.x - point.x)
        social_part_y = random.random() * c2 * (swarm_best_position.y - point.y)

        point.x_velocity = learning_part_x + social_part_x
        point.y_velocity = learning_part_y + social_part_y


def move_points(points):
    for point in points:
        point.move()


def calculate_best_position(points):
    for point in points:
        if point.fitness() > swarm_best_position.fitness():
            swarm_best_position.x = point.x
            swarm_best_position.y = point.y


points = random_population()

for _ in range(iterations):
    show_plot()
    calculate_new_velocities(points)
    move_points(points)

