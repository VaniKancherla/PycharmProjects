# Data Preprocessing Template

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')

# prints the first 5 rows from Salary_Data.csv
print(dataset.head())
# prints the shape of Salary_Data.csv (rows, columns)
print(dataset.shape)
# prints range of index of Salary_Data.csv
print(dataset.index)
# prints the columns heading names
print(dataset.columns)
# Checking for the missing values in the Salary_Data.csv
print("Checking for the missing values: ", dataset.isnull().sum())


mean_SalaryData = dataset['YearsExperience'].mean()
print("mean: ", mean_SalaryData)

median_SalaryData = dataset['YearsExperience'].median()
print("median: ", median_SalaryData)

mode_SalaryData = dataset['YearsExperience'].mode()
print("mode: ", mode_SalaryData)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Taking care of missing data
# Replace the all NaN with mean, median or mode
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 0:1])
X[:, 0:1] = imputer.transform(X[:, 0:1])

# Splitting the dataset into the Training set and Test set
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

cal_accuracy = r2_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)

# Visualising the Training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color='green')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
