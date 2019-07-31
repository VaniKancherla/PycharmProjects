import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Importing the data set
data_setX = pd.read_csv('Google_Stock_Price_Train.csv')
data_setX.drop_duplicates()
x = data_setX.iloc[:, 2:3].values
y = data_setX.iloc[:, 1].values

test_data = pd.read_csv('Google_Stock_Price_Test.csv')
X_test = test_data.iloc[:, 2:3].values
y_test = test_data.iloc[:, 1].values

# Taking care of missing data
# Replace the all NaN with mean
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(x[:, 0:1])
x[:, 0:1] = imp.transform(x[:, 0:1])

# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
x = sc_X.fit_transform(x)
y = np.array(y).reshape((len(y), 1))
y = sc_y.fit_transform(y)
train_csv = np.savetxt('final_train.csv', x, fmt='%.8f', delimiter=',')
a = open("final_train.csv", 'r')
print("the file contains:")
print(a.read())

# Fitting Simple Linear Regression to the Training set
slr = LinearRegression()
slr.fit(x, y)

# Predicting the Test set results
y_predict = slr.predict(X_test)

# Calculating the accuracy
cal_accuracy = r2_score(y_test, y_predict)
print(cal_accuracy)
