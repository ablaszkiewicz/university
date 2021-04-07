import random
intervals = [0]*6
F = [0, 0.2, 0.6, 0.8, 0.95, 1]

def getXFromY(y):
    for i in range(6):
        if y <= F[i]:
            return i

for i in range(100000):
    intervals[int(getXFromY(random.random()))] += 1

print(intervals)
