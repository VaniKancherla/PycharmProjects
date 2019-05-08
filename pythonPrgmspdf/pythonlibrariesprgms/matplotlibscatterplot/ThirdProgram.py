import math
import random
import matplotlib.pyplot as plt

no_of_balls = 20
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
colors = [random.randint(1, 8) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_balls)]
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.2, 0.0, 1.2])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
