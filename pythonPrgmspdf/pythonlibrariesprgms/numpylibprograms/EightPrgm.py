import numpy as np

list1 = [1, 2, 3, 4, 5, 6, 7]
print("List to array: ")
print(np.array(list1))

print("tuple to array for (1, 2, 3, 4, 5, 6, 7) : ")
tuple1 = (1, 2, 3, 4, 5, 6, 7)
print(np.asarray(tuple1))
print("tuple to array for ([8, 4, 6], [1, 2, 3]) : ")
my_tuple = ([8, 4, 6], [1, 2, 3])
print(np.asanyarray(my_tuple))


A = np.matrix(np.ones((3, 3)))
print(A)
np.array(A)[2] = 2
print(A)







