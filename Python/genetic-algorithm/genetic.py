import numpy as np
from helper import fitness


class Genetic:
    def __init__(self, coords, population_size=100, elitist_factor=10, mutation_rate=0.01):
        self.coords = coords
        self.population_size = population_size
        self.elitist_factor = elitist_factor
        self.mutation_rate = mutation_rate

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            # 1/fitness -> change to maximization problem
            population_fitness[i] = 1/fitness(self.coords, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(self.coords))
            population.append(solution)

        return population

    def selection(self, population):
        selected = []
        population_fitness = self.population_fitness(population)
        probability = {}
        sum_fitness = sum(population_fitness.values())
        probability_previous = 0.0

        for i in range(self.elitist_factor):
            selected.append(population[list(population_fitness.items())[i][0]])

        for key, value in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True):
            probability[key] = probability_previous + (value / sum_fitness)
            probability_previous = probability[key]

        for i in range(self.elitist_factor, len(population)):
            rand = np.random.rand()
            for key, value in probability.items():
                if rand <= value:
                    selected.append(population[key])
                    break

        return selected

    def crossover_population(self, population):
        children = []
        while len(children) < self.population_size:
            left_parent = population[np.random.randint(0, len(population))]
            right_parent = population[np.random.randint(0, len(population))]

            slice_len = np.random.randint(1, len(left_parent) / 2)
            random_from = np.random.randint(0, len(left_parent) - slice_len - 1)
            slice_from_parent = left_parent[random_from:random_from + slice_len]

            child = np.array(right_parent)

            for element in slice_from_parent:
                child = child[child != element]

            child = list(child[:random_from]) + list(slice_from_parent) + list(child[random_from:])

            children.append(child)  # child

        return children

    def mutate_population(self, population):
        population_fitness = self.population_fitness(population)
        mutated_population = []
        for i in range(self.elitist_factor):
            mutated_population.append(population[list(population_fitness.items())[i][0]])

        for subject in population:
            for i in range(self.elitist_factor, len(subject)):
                random = np.random.uniform()
                if random <= self.mutation_rate:
                    new_index = np.random.randint(0, len(subject))
                    subject[i], subject[new_index] = subject[new_index], subject[i]
            mutated_population.append(subject)

        return population

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
