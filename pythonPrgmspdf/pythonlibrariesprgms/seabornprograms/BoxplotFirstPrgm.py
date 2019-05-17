import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
sb.boxplot(x='lifeExp', y='continent', data=data)
plt.show()
