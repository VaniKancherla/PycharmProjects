import seaborn as sb
from matplotlib import pyplot as plt

data = sb.load_dataset('https://github.com/mwaskom/seaborn-data/blob/master/iris.csv')
sb.violinplot(x='species', y='sepal_length', data=data)
plt.show()
