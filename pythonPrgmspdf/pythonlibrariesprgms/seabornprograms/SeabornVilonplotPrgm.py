import seaborn as sb
from matplotlib import pyplot as plt

data = sb.load_dataset('tips')
sb.violinplot(x='sex', y='total_bill', data=data)
plt.show()
