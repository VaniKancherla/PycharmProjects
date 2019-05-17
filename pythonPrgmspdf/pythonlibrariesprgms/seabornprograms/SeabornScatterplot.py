import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('tips')
sb.scatterplot(x="sex", y="total_bill", data=df)
plt.show()
