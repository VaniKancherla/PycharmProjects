import matplotlib.pyplot as plt
from pylab import randn

x = randn(50)
y = randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
