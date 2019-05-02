import numpy as np

border_array = np.ones((5, 5))
print("Original array:")
print(border_array)
print("1 on the border and 0 inside in the array")
border_array[1:-1, 1:-1] = 0
print(border_array)

