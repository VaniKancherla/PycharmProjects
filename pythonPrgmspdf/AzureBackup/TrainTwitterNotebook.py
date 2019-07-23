# Databricks notebook source
import pandas as pd
import ast
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pickle
from azure.datalake.store import core, lib, multithread
import numpy as np

#Load TrainTwitter CSV File
lookup_data = dbutils.widgets.get("traintwitterpath")

#Converting str to dictionary
dic_data = ast.literal_eval(lookup_data)
valueList = []
for i in range(0, len(dic_data['value']), 1):
  valueList.append(dic_data['value'][i])

data_set = pd.DataFrame(valueList)
# print(data_set)

# Cleaning the text
nltk.download('stopwords')
corpus = []
for i in range(0, len(data_set)):
  review = data_set.iloc[:, 2]
  review = re.sub('[^a-zA-Z]', ' ', review[i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus.append(review)

# Creating the Bag of words model
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
y = data_set.iloc[:, 1]
# Splitting the data set into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Fitting Naive Bayes to the Training set
classifierNLP = GaussianNB()
classifierNLP.fit(X_train, y_train)

# Predicting the Test set results
y_predict = classifierNLP.predict(X_test)

# Calculating Accuracy
cal_accuracy = accuracy_score(y_test, y_predict)
print("Accuracy for linear: ", accuracy_score(y_test, y_predict))

#Saving Pickle file in Azure Lake Storage
localFileName = 'TwitterClassifierNLP.pkl'
pickle.dump(classifierNLP, open(localFileName, 'wb'))

token = lib.auth(tenant_id = '524b0e96-35a3-46ef-ade3-a76c1936a890', client_secret = 'Q:Zb3@Crk*X:S57iYKx0j0J-G=-1bOMf', client_id = '50af3e84-daae-4cd6-baca-d9900b9dada2')
adlsFileSystemClient = core.AzureDLFileSystem(token, store_name='vanidatalakestorage')
adlsFileSystemClient.put(localFileName, 'twitterhistoricaldata/TwitterClassifierNLP.pkl')
print("TwitterClassifierNLP pickle file saved in Azure Data Lake Storage")

#Load pickle file from Data Lake Storage
adlsFileSystemClient.get('twitterhistoricaldata/TwitterClassifierNLP.pkl', 'TwitterClassifierNLP.pkl')
pkl_file = open('TwitterClassifierNLP.pkl', 'rb')
model= pickle.load(pkl_file)

# Get csv file from azure data lake storage
adlsFileSystemClient.get('twitterhistoricaldata/twitter_test.csv', 'twitter_test.csv')
Twitter_TestFile_csv = open('twitter_test.csv', 'rb')
test_dataset = pd.read_csv(Twitter_TestFile_csv)
# print("Read csv from data lake: ",test_dataset)

# Cleaning the text
nltk.download('stopwords')
test_corpus = []
for i in range(0, len(test_dataset)):
  test_review = test_dataset.iloc[:, 2]
  test_review = re.sub('[^a-zA-Z]', ' ', test_review[i])
  test_review = test_review.lower()
  test_review = test_review.split()
  ps = PorterStemmer()
  test_review = [ps.stem(word) for word in test_review if not word in set(stopwords.words('english'))]
  test_review = ' '.join(test_review)
  test_corpus.append(test_review)

# print("test_corpus data: ",test_corpus)  
# Creating the Bag of words model
cv1 = CountVectorizer(max_features=1500)
x_testData = cv1.fit_transform(test_corpus).toarray()
# print("x_testData shape: ", x_testData)
y_test_index= test_dataset.columns.get_loc("Sentiment")
y_test = test_dataset.iloc[:,y_test_index:(y_test_index+1)]
# print("y_test",y_test)

# Predicting the Test set results
y_test_predict = model.predict(x_testData)
# print("y_test_predict shape: ", y_test_predict.shape)
# print("y_test_predict data: ", y_test_predict)

#Calculating Accuracy
accuracy_testPickle = accuracy_score(y_test, y_test_predict)
print("Accuracy for test model: ", accuracy_testPickle)

vv = pd.DataFrame.from_records(x_testData)
print("vv data: ", vv)
# x_testData_df = pd.DataFrame(x_testData)
# print("x_testData_df data: ",x_testData_df)

x_testData_df = pd.DataFrame(test_corpus, columns=['xtest_df'])
# print(x_testData_df)
y_predict_df = pd.DataFrame(y_test_predict, columns=['y_predict_df'])
# print("y_test_predict data: ", y_predict_df)
result_df = pd.concat([x_testData_df, y_predict_df], axis=1)
# print(result_df)

# Save dataframe to cosmosDB
writeConfig = {
"Endpoint" : "https://vanicosmosdb.documents.azure.com:443/",
"Masterkey" : "i5ZNuO1GEWHhnwtzESYfkhEZUa9EvcNso3IiGoIlWe5c2JdHAoZ3TjxkQezfGYqpZzH6LmLZqgrcYiTNuyqrJg==",
"Database" : "ToDoList",
"Collection" : "twittercontainer",
"Upsert" : "true"
}

spark_df = spark.createDataFrame(result_df)
spark_df.write.format("com.microsoft.azure.cosmosdb.spark").mode('overwrite').options(**writeConfig).save()


# COMMAND ----------


