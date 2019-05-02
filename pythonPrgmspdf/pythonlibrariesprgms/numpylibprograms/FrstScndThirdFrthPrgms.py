import numpy as np
# 1st program
py_arr = [12.23, 13.32, 100, 36.32]
numpy_arr = np.array([12.23, 13.32, 100, 36.32])
print("list of numeric values: ", py_arr)
print("One-dimensional NumPy array: ", numpy_arr)

# 2nd program
create_matrix = np.arange(2, 11).reshape(3, 3)
print("Creating 3*3 matrix: ", create_matrix)

# 3rd program
zero_array = np.zeros(10)
print("A null vector of size 10: ", zero_array)
zero_array[6] = 11
print("Update sixth value to 11: ", zero_array)

# 4th program
org_array = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
print("Reverse of an array:", np.flip(org_array))



