# Databricks notebook source
import pandas as pd
import json as js
from pandas.compat import StringIO
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
from azure.storage.blob import BlockBlobService
from datetime import datetime 

dbutils.widgets.text("inputpath", "","")
dbutils.widgets.get("inputpath")
datafromDb = getArgument("inputpath")
inputdata = js.loads(datafromDb)
inputdata = inputdata["Response"]
# print(inputdata)

# Importing the data set
dataset = pd.read_csv(StringIO(inputdata),header=0,delimiter=',',skipinitialspace=True)
# print(dataset)
x = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Calculating Accuracy
cal_accuracy = r2_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)
print(regressor)

StorageAccountName = 'vanistorageacct'
StorageAccountKey = 'RUK6/w9IYpZpCtAcD+LWNCqfnes+p9rqgJbQcnr/rQdiF6BTvWPUTB9E1jO7Lkyp0dGvr3aWOkC9CMAp2+YIFw=='
ContainerName = 'blobcontainer'
LocalFileName = 'SimpleLinearDFPickle'
pickle.dump(regressor, open(LocalFileName, 'wb'))
output_blob_service = BlockBlobService(account_name=StorageAccountName,account_key=StorageAccountKey)
output_blob_service.create_blob_from_path(ContainerName,'SimpleLinearDFPickle'+'.pkl',LocalFileName)
print("regressor model saved to blob")

