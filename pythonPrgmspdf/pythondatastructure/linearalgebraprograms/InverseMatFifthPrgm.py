from numpy.linalg import inv
import numpy as np

x = np.array([[12, 7, 3],
              [4, 5, 6],
              [7, 8, 9]])
x_inv = np.linalg.inv(x)
# matinv = inv(np.matrix(x))
print(x_inv)


