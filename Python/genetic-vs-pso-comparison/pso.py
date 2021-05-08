import matplotlib.pyplot as plt
import random
import helper

# Configuration
iterations = 30

# Population
population_size = 10

# Function
function_min = 100
function_max = -100

# PSO variables

w = 0.7 # interia
cognitive_coefficient = 1.5 # cognitive (self)
social_coefficient = 1.5 # social (swarm)
swarm_best_position = helper.Point(function_min, function_max)

# Plot variables

distances_to_best_point = []


def random_in_range():
    return float("%.1f" % random.uniform(function_min, function_max))


def iter_plot():
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    axs[0].scatter(x_values, y_values)
    plt.pause(0.1)


def random_population():
    return [helper.Point(random_in_range(), random_in_range()) for _ in range(population_size)]


def calculate_new_velocities(points):
    for point in points:
        # learning part
        learning_part_x = w * point.x_velocity
        learning_part_y = w * point.y_velocity

        # cognitive part (self learning)
        cognitive_part_x = cognitive_coefficient * random.random() * (point.best_x - point.x)
        cognitive_part_y = cognitive_coefficient * random.random() * (point.best_y - point.y)

        # social part
        social_part_x = random.random() * social_coefficient * (swarm_best_position.x - point.x)
        social_part_y = random.random() * social_coefficient * (swarm_best_position.y - point.y)

        point.x_velocity = learning_part_x + cognitive_part_x + social_part_x
        point.y_velocity = learning_part_y + cognitive_part_y + social_part_y


def move_points(points):
    for point in points:
        point.move()


def calculate_best_position(points):
    for point in points:
        if point.fitness() < swarm_best_position.fitness():
            swarm_best_position.x = point.x
            swarm_best_position.y = point.y


def calculate_self_best_positions(points):
    for point in points:
        point.calculate_self_best_position()


points = random_population()
fig, axs = plt.subplots(1, 2)
axs[0].set_title("Punkty")

for _ in range(iterations):
    iter_plot()
    calculate_best_position(points)
    calculate_new_velocities(points)
    move_points(points)
    distances_to_best_point.append(swarm_best_position.distance(helper.Point(0, 0)))
    print(swarm_best_position.x, swarm_best_position.y)


axs[1].plot(list(range(iterations)), distances_to_best_point)
axs[1].set_title("Najlepszy dystans")
plt.show()


