# Random Forest Tree Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, -1].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X[:, 0] = label_encoder.fit_transform(X[:, 0])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fitting Random Forest Tree Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)

# Calculating Accuracy
cal_accuracy = r2_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)

# Visualising the Random Forest Tree Regression Training data set
X_grid = np.arange(min(X_train), max(X_train), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X_train, y_train, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Random Forest Tree Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualising the Random Forest Tree Regression Test set
X_grid_test = np.arange(min(X_test), max(X_test), 0.01)
X_grid_test = X_grid_test.reshape((len(X_grid_test), 1))

plt.scatter(X_test, y_test, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Random Forest Tree Regression')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
