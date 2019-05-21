# Support Vector Regression
# Importing the libraries
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 2].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X[:, 0] = label_encoder.fit_transform(X[:, 0])

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
# y = y.reshape(-1, 1)
y = np.array(y).reshape((len(y), 1))
y = sc_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# RBF model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(X_train, y_train)
ypred = svr_rbf.predict(X_test)
print("acc for rbf: ", r2_score(y_test, ypred))

# Linear model
svr_lin = SVR(kernel='linear', C=1e3)
svr_lin.fit(X_train, y_train)
ypred = svr_lin.predict(X_test)
print("acc for linear: ", r2_score(y_test, ypred))

# Polynomial model
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
svr_poly.fit(X_train, y_train)
ypred = svr_poly.predict(X_test)
print("acc for poly: ", r2_score(y_test, ypred))

# Visualising the SVR results (for higher resolution and smoother curve) for Train data set
X_grid = np.arange(min(X_train), max(X_train), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_train, y_train, color='black')
plt.plot(X_grid, svr_rbf.predict(X_grid), color='red', label='Radial Basis')
plt.plot(X_grid, svr_lin.predict(X_grid), color='blue', linestyle='-', label='Linear Model')
plt.plot(X_grid, svr_poly.predict(X_grid), color='green', linestyle='--', label='Poly')
plt.title('Position vs Salary (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve) for Test data set
X_grid = np.arange(min(X_test), max(X_test), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, y_test, color='red')
plt.plot(X_grid, svr_rbf.predict(X_grid), color='red')
plt.plot(X_grid, svr_lin.predict(X_grid), color='blue')
plt.plot(X_grid, svr_poly.predict(X_grid), color='green')
plt.title('Position vs Salary (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
