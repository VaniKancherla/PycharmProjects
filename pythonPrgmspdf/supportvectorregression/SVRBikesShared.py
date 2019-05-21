# Random Forest Tree Regression

# Importing the libraries
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Importing the dataset
dataset = pd.read_csv('bike_sharing.csv')
x1 = dataset.columns.get_loc("temp")
x2 = dataset.columns.get_loc("hr")
x3 = dataset.columns.get_loc("atemp")
x = dataset.iloc[:, [x2, x1, x3]]
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Fitting Random Forest Tree Regression to the dataset
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
