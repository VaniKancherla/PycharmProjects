import numpy as np

exp_array = np.array([1, 2, 3], dtype=np.int)
print(exp_array)
print("Size of the array: ", exp_array.size)
print("Length of one array element in bytes: ", exp_array.itemsize)
print("Total bytes consumed by the elements of the array: ", exp_array.nbytes)