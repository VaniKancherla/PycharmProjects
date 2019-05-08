import matplotlib.pyplot as plt
from pylab import randn

x = randn(200)
y = randn(200)
plt.scatter(x, y, color=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
