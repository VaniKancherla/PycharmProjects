import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('FinancialData.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()
