import random

intervals = [0] * 10

def getXFromY(y):
    x = y
    x *= 100
    x += 50
    return x


for i in range(100000):
    intervals[int(getXFromY(random.random())%10)] += 1

print(intervals)

