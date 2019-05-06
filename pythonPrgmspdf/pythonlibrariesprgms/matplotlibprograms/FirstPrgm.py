import matplotlib.pyplot as plt

x = range(1, 20)
print("Values of x: ", x)
print(*range(1, 20))
y = [value * 2 for value in x]
print("Values of Y (thrice of X):", y)
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line")
plt.show()
