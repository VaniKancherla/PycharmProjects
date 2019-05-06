import numpy as np

arry1 = np.array([10, 20, 30, 40])
arry2 = np.array([20, 40, 12, 6, 8, 1])

print("Intersect: ")
print(np.intersect1d(arry1, arry2))
print("Union: ")
print(np.union1d(arry1, arry2))
print("Value exits or not: prints True/False")
print(np.in1d(arry1, arry2))

# 13th prgm
array_diff = np.array([0, 10, 20, 40, 60, 80])
array_diff2 = np.array([10, 30, 40, 50, 70, 90])
print("Difference: ")
print(np.setdiff1d(array_diff, array_diff2))

# 14th prgm
array_exor = np.array([0, 10, 20, 40, 60, 80])
array_exor2 = np.array([10, 30, 40, 50, 90])
print("Exclusive OR: ")
print(np.setxor1d(array_exor, array_exor2))

# 15th prgm
cmpary = np.array([1, 2, 8, 12])
cmpary2 = np.array([4, 5, 6, 12])
print("Comparing to sets: ")
print(cmpary > cmpary2)
print(cmpary >= cmpary2)
print(cmpary < cmpary2)
print(cmpary <= cmpary2)




