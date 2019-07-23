# Databricks notebook source
import pandas as pd
import json as js
from pandas.compat import StringIO
from sklearn.model_selection import train_test_split
import pickle
from azure.storage.blob import BlockBlobService
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# COMMAND ----------

dbutils.widgets.text("classificationpath", "","")
dbutils.widgets.get("classificationpath")
datafromDb = getArgument("classificationpath")
inputdata = js.loads(datafromDb)
inputdata = inputdata["Response"]
print(inputdata)

# Importing the data set
dataset = pd.read_csv(StringIO(inputdata),header=0,delimiter=',',skipinitialspace=True)

# COMMAND ----------

dataset.info()

# COMMAND ----------

dataset.describe()

# COMMAND ----------

dataset.isnull().sum()

# COMMAND ----------

x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# COMMAND ----------

# Splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Fitting Decision Tree Classification to the Training set
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# COMMAND ----------

# Calculating Accuracy
cal_accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", cal_accuracy)

# COMMAND ----------

# Storing Classification model pickle file into vanistorageacct account
StorageAccountName = 'vanistorageacct'
StorageAccountKey = 'RUK6/w9IYpZpCtAcD+LWNCqfnes+p9rqgJbQcnr/rQdiF6BTvWPUTB9E1jO7Lkyp0dGvr3aWOkC9CMAp2+YIFw=='
ContainerName = 'blobcontainer'
LocalFileName = 'ClassificationDFPickle'
pickle.dump(classifier, open(LocalFileName, 'wb'))
output_blob_service = BlockBlobService(account_name=StorageAccountName,account_key=StorageAccountKey)
output_blob_service.create_blob_from_path(ContainerName,'ClassificationDFPickle'+'.pkl',LocalFileName)
print("classifier model saved to blob")
