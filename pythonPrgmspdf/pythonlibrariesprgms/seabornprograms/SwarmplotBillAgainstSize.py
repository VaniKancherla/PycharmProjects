import seaborn as sb
from matplotlib import pyplot as plt

data = sb.load_dataset('tips')
sb.swarmplot(x='total_bill', y='size', data=data)
plt.show()
