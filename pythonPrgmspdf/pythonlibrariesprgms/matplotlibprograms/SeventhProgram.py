import matplotlib.pyplot as plt

x = [10, 20, 30]
y = [30, 25, 10]

x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('Two or more lines with different styles')
plt.plot(x, y)
plt.plot(x1, y1, color='green', linewidth=2,  label='line1-width-2', linestyle='dotted')
plt.plot(x2, y2, color='blue', linewidth=3,  label='line1-width-3', linestyle='dashed')
plt.legend()
plt.show()



















