import matplotlib.pyplot as plt
from numpy.random import random

colors = ['b', 'c', 'y', 'm', 'r']
a = plt.scatter(random(10), random(10), marker='x', color=colors[0])
b = plt.scatter(random(10), random(10), marker='+', color=colors[2])
c = plt.scatter(random(10), random(10), marker='o', color=colors[1])
plt.legend((a, b, c), ('a', 'b', 'c'), scatterpoints=1, loc='upper right', ncol=3, fontsize=8)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
