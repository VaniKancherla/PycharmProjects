# Databricks notebook source
import pandas as pd
import json as js
from pandas.compat import StringIO
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import pyspark

# Load pickle model to predict data
pkl_file = open('SimpleLinearDFPickle', 'rb')
model = pickle.load(pkl_file)
print(model)

#Getting Train data set from Storage Account
dbutils.widgets.text("sltestpath", "","")
dbutils.widgets.get("sltestpath")
testdatafromStorage = getArgument("sltestpath")
inputdata = js.loads(testdatafromStorage)
inputdata = inputdata["Response"]

test_dataSet = pd.read_csv(StringIO(inputdata),header=0,delimiter=',',skipinitialspace=True)
x_testData = test_dataSet.iloc[:, 2:3].values
y_testData = test_dataSet.iloc[:, 1].values

# Predicting the Test set results
y_predict = model.predict(x_testData)

#Calculating Accuracy
accuracy_testPickle = r2_score(y_testData, y_predict)
print("Accuracy for test model: ", accuracy_testPickle)

#Converting x_testData, y_predict to DataFrame and concating these two fields
x_test_df = pd.DataFrame(x_testData, columns=['x_test_df'])
y_predict_df = pd.DataFrame(y_predict, columns=['y_predict_df'])
result_df = pd.concat([x_test_df, y_predict_df], axis=1)
print(result_df)

# Save dataframe to cosmosDB
writeConfig = {
"Endpoint" : "https://vanicosmosdb.documents.azure.com:443/",
"Masterkey" : "i5ZNuO1GEWHhnwtzESYfkhEZUa9EvcNso3IiGoIlWe5c2JdHAoZ3TjxkQezfGYqpZzH6LmLZqgrcYiTNuyqrJg==",
"Database" : "ToDoList",
"Collection" : "Items",
"Upsert" : "true"
}

spark_df = spark.createDataFrame(result_df)
print(type(spark_df))
spark_df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(**writeConfig).save()


# COMMAND ----------


