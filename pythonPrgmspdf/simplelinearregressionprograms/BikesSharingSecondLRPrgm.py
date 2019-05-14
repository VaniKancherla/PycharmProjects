# Data Preprocessing Template

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Bike_Sharing.csv')
x = dataset.iloc[:, [10]].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=1/2, random_state=0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Bikes getting shared based on the temperature of the day (Training set)')
plt.xlabel('Temperature')
plt.ylabel('Bikes Shared')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color='green')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Bikes getting shared based on the temperature of the day (Test set)')
plt.xlabel('Temperature')
plt.ylabel('Bikes Shared')
plt.show()
