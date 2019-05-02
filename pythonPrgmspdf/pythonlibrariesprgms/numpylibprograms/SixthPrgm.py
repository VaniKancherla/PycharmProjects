import numpy as np

border_array = np.ones((3, 3))
print("Original array: ", border_array)
print("Border filled with 0's around an existing array: ")
border_array = np.pad(border_array, pad_width=1, mode='constant', constant_values=0)
print(border_array)
