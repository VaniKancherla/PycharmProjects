# Databricks notebook source
import pandas as pd
import json as js
from pandas.compat import StringIO
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pyspark
import pickle

# COMMAND ----------

# Load pickle model to predict data
pkl_file = open('ClassificationDFPickle', 'rb')
model = pickle.load(pkl_file)

# COMMAND ----------

#Getting Train data set from Storage Account
dbutils.widgets.text("testpath", "","")
dbutils.widgets.get("testpath")
testdatafromStorage = getArgument("testpath")
inputdata = js.loads(testdatafromStorage)
inputdata = inputdata["Response"]

# COMMAND ----------

# Importing the data set
test_dataSet = pd.read_csv(StringIO(inputdata),header=0,delimiter=',',skipinitialspace=True)
x_testData = test_dataSet.iloc[:, [2, 3]].values
y_testData = test_dataSet.iloc[:, 4].values

# COMMAND ----------

# Predicting the Test set results
y_predict = model.predict(x_testData)

#Calculating Accuracy
accuracy_testPickle = accuracy_score(y_testData, y_predict)
print("Accuracy for test model: ", accuracy_testPickle)

# COMMAND ----------

#Converting x_testData, y_predict to DataFrame and concating these two fields
x_test_df = pd.DataFrame(x_testData, columns=['Age', 'EstimatedSalary'])
y_predict_df = pd.DataFrame(y_predict, columns=['y_predict_df'])
result_df = pd.concat([x_test_df, y_predict_df], axis=1)

# Save dataframe to cosmosDB
writeConfig = {
"Endpoint" : "https://vanicosmosdb.documents.azure.com:443/",
"Masterkey" : "i5ZNuO1GEWHhnwtzESYfkhEZUa9EvcNso3IiGoIlWe5c2JdHAoZ3TjxkQezfGYqpZzH6LmLZqgrcYiTNuyqrJg==",
"Database" : "ToDoList",
"Collection" : "Items",
"Upsert" : "true"
}

spark_df = spark.createDataFrame(result_df)
spark_df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(**writeConfig).save()

# COMMAND ----------


