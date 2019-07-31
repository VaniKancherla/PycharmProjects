import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import numpy as np

# Importing the dataset
dataCSV = pd.read_csv('Google_Stock_Price_Train.csv')

df_training = dataCSV.sample(frac=0.8)
df_test = pd.concat([dataCSV, df_training]).drop_duplicates(keep=False)

df_training.to_csv('/home/admin1/PycharmProjects/pythonPrgmspdf/inputFiles/training_data.csv', header=True, index=None)
df_test.to_csv('/home/admin1/PycharmProjects/pythonPrgmspdf/inputFiles/test_data.csv', header=True, index=None)

train_dataSet = pd.read_csv('/home/admin1/PycharmProjects/pythonPrgmspdf/inputFiles/training_data.csv')
x = train_dataSet.iloc[:, 2:3].values
y = train_dataSet.iloc[:, 1].values

# Splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

cal_accuracy = r2_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)

print(regressor)

file_name = '/home/admin1/PycharmProjects/pythonPrgmspdf/simplelinearregressionprograms/slDatafactory.pkl'
pkl_file = open(file_name, 'wb')
model = pickle.dump(regressor, pkl_file)
pkl_file.close()

# Load pickle model to predict data
pkl_file = open(file_name, 'rb')
model = pickle.load(pkl_file)
test_dataSet = pd.read_csv('/home/admin1/PycharmProjects/pythonPrgmspdf/inputFiles/test_data.csv')
x_testData = test_dataSet.iloc[:, 2:3].values
y_testData = test_dataSet.iloc[:, 1].values

y_predict = model.predict(x_testData)
accuracy_testPickle = r2_score(y_testData, y_predict)
print("Accuracy for test model: ", accuracy_testPickle)

x_test_df = pd.DataFrame(x_testData)
y_predict_df = pd.DataFrame(y_predict)
result_df = pd.concat([x_test_df, y_predict_df], axis=1)
print(result_df)
