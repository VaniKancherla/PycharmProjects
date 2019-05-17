import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd

data = sb.load_dataset('tips')
# sb.boxplot(x=data["day"])
sb.boxplot(x='day', y='tip', data=data)
plt.show()
