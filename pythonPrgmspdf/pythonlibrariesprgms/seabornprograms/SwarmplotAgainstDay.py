import seaborn as sb
from matplotlib import pyplot as plt

data = sb.load_dataset('tips')
sb.swarmplot(x='total_bill', y='day', data=data)
plt.show()
