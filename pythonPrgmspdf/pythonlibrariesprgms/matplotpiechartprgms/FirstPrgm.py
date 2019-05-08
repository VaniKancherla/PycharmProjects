import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['green', 'blue', 'yellow', 'cyan', 'red', '#8c564b']
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(popularity, explode=explode, labels=languages, colors=colors, autopct='%1.2f%%', shadow=True, startangle=120)

plt.show()
