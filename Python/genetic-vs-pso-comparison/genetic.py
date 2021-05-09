import matplotlib.pyplot as plt
from random import *
import helper

# Configuration
iterations = 10

# Population
population_size = 10

# Function
function_min = -100
function_max = 100

# Genetic variables
mutation_rate = 0.1
elite_size = 2
best_distances = []



def random_in_range():
    return float("%.1f" % uniform(function_min, function_max))


def iter_plot():
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    axs[0].scatter(x_values, y_values)
    plt.pause(0.1)


def random_population():
    return [helper.Point(random_in_range(), random_in_range()) for _ in range(population_size)]


def fitness(population):
    rating = {}
    minimum = min([point.fitness() for point in population])
    for point in population:
        if point.fitness() == minimum:
            rating[point] = 1
        else:
            rating[point] = 1 / abs(point.fitness() - minimum)

    return {key: value for key, value in sorted(rating.items(), key=lambda item: item[1], reverse=True)}


def selection(population):
    selected = []
    population_fitness = fitness(population)
    probability = {}
    sum_fitness = sum(population_fitness.values())

    probability_prev = 0
    for key, val in population_fitness.items():
        probability[key] = probability_prev + (val / sum_fitness)
        probability_prev = probability[key]

    for i in range(elite_size):
        selected.append(list(population_fitness.keys())[i])

    for i in range(elite_size, len(population)):
        rand = random()
        for key, val in probability.items():
            if rand <= val:
                selected.append(key)
                break

    return selected


def crossover(population):
    new_population = []

    for i in range(population_size):
        parent1 = population[randint(0, len(population) - 1)]
        parent2 = population[randint(0, len(population) - 1)]

        new_population.append(helper.Point(uniform(parent1.x, parent2.x), uniform(parent1.y, parent2.y)))

    return new_population


def mutation(population):
    new_population = []
    population_fitness = fitness(population)

    for i in range(elite_size):
        new_population.append(list(population_fitness.keys())[i])

    for i in range(elite_size, len(population)):
        population[i].x *= uniform(1 - mutation_rate, 1 + mutation_rate)
        population[i].y *= uniform(1 - mutation_rate, 1 + mutation_rate)
        new_population.append(helper.Point(population[i].x, population[i].y))

    return new_population


def next_generation(population):
    population = selection(population)
    population = crossover(population)
    population = mutation(population)

    return population


def calculate_best_distances(population):
    zero_point = helper.Point(0, 0)
    return sorted(points, key=lambda x: x.fitness())[0].distance(zero_point)


points = random_population()
fig, axs = plt.subplots(1, 2)
axs[0].set_title("Punkty")

for _ in range(iterations):
    points = next_generation(points)
    best_distances.append(calculate_best_distances(points))
    iter_plot()


axs[1].plot(list(range(iterations)), best_distances)
axs[1].set_title("Najlepszy fitness (0 = najlepszy)")
plt.show()
