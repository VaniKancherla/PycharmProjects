import numpy as np

# 9th program
org_ary = [10, 20, 30]
print(np.append(org_ary, [10, 20, 30, 40, 50, 60, 70, 80, 90]))

# 10th program
exmp = [1.00000000+0.j, 0+1j]
for i in exmp:
    x = np.sqrt(i)
    print("Real part: ", i.real)
    print("Img part: ", i.imag)


x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ", x)
print("Original array:y ", y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)

