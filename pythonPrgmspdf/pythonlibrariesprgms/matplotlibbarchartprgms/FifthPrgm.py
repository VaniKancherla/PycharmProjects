import matplotlib.pyplot as plt


x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
n = len(x)
x_pos = range(n)

fig, ax = plt.subplots()

dis = plt.bar(x_pos, popularity, color=[[1.0, 0.4, 0.6, 1.0], [0.4, 0.6, 0.8, 1.0], 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')


def display_test_label(dis):

    for rect in dis:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, 1.0 * height, '%f' % float(height), ha='center', va='bottom')


display_test_label(dis)
plt.show()

