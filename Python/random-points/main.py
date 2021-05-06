import random
# 0.2, 0.4, 0.3, 0.1
# 0.2, 0.6, 0.9, 1.0
x_probabilities = [0.2, 0.6, 0.9, 1.0]
y_probabilities = [[0.0, 0.0, 0.5, 1.0],
                   [0.5, 0.5, 0.5, 1.0],
                   [0.0, 0.0, 1.0, 1.0],
                   [0.0, 0.5, 0.5, 1.0]]

points = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(100000):
    x = random.random()
    for j in range(len(x_probabilities)):
        if x < x_probabilities[j]:
            y = random.random()
            for k in range(len(y_probabilities[j])):
                if y < y_probabilities[j][k]:
                    points[j][k] += 1
                    break
            break

for i in range(len(points)):
    for j in range(len(points[i])):
        print(points[i][j], "\t\t\t", end='')
    print()
