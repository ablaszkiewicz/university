import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.best_fitness = math.inf
        self.best_x = 0
        self.best_y = 0

    def fitness(self):
        return self.x ** 2 + self.y ** 2

    def distance(self, other):
        delta_x = math.fabs(other.x - self.x)
        delta_y = math.fabs(other.y - self.y)
        return math.fabs(delta_x ** 2 + delta_y ** 2)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def calculate_self_best_position(self):
        if(self.fitness() < self.best_fitness):
            self.best_x = self.x
            self.best_y = self.y

