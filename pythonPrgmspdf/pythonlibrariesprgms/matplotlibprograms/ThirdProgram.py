import matplotlib.pyplot as plt
import csv
x = []
y = []
with open('test.txt', 'r') as f:
    plots = csv.reader(f, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
