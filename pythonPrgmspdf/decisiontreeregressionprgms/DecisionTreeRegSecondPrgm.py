import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from matplotlib import pyplot as plt

bikes = pd.read_csv('bike_sharing.csv')
regressor = DecisionTreeRegressor(max_depth=2)
regressor.fit(bikes[['temp', 'hum']], bikes['cnt'])

DecisionTreeRegressor(criterion='mse', max_depth=2, max_features=None,
           max_leaf_nodes=None, min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, presort=False, random_state=None, splitter='best')

nx = 40
ny = 40
# creating a grid of points%matplotlib inline
# min temperature -5, max 40
x_temperature = np.linspace(0, 1, nx)
# min humidity 20, max 80
y_humidity = np.linspace(0, 1, ny)
xx, yy = np.meshgrid(x_temperature, y_humidity)
# evaluating the regressor on all the points
z_bikes = regressor.predict(np.array([xx.flatten(), yy.flatten()]).T)
zz = np.reshape(z_bikes, (nx, ny))


fig = plt.figure(figsize=(8, 8))
# plotting the predictions
plt.pcolormesh(x_temperature, y_humidity, zz, cmap=plt.cm.YlOrRd)
# add a color bar on the right
plt.colorbar(label='bikes predicted')
# plotting also the observations
plt.scatter(bikes['temp'], bikes['hum'], s=bikes['cnt']/25.0, c='g')
# setting the limit for each axis
plt.xlim(np.min(x_temperature), np.max(x_temperature))
plt.ylim(np.min(y_humidity), np.max(y_humidity))
plt.xlabel('temperature')
plt.ylabel('humidity')
plt.show()
