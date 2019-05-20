# Random Forest Tree Regression

# Importing the libraries
import pandas as pd
from sklearn.metrics import r2_score

# Importing the dataset
dataset = pd.read_csv('bike_sharing.csv')

x1 = dataset.columns.get_loc("temp")
x2 = dataset.columns.get_loc("hr")
x3 = dataset.columns.get_loc("atemp")
x = dataset.iloc[:, [x2, x1, x3]]
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

# Fitting Random Forest Tree Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)

# Calculating Accuracy
cal_accuracy = r2_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)
