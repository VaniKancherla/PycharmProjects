#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import findspark
from pyspark import SparkContext, SparkConf
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# In[2]:


findspark.init("/home/vaninewVM/spark-2.4.3-bin-hadoop2.7")


# In[3]:


# Importing Train data set
pydf_Train = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('hdfs://localhost:9000/Myhadoopfolder/Google_Stock_Price_Train.csv')
pydf_Train=pydf_Train.toPandas()


# In[11]:


# Importing Test data set
pydf_Test = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('hdfs://localhost:9000/Myhadoopfolder/Google_Stock_Price_Test.csv')
pydf_Test = pydf_Test.toPandas()


# In[5]:


x_train = pydf_Train.iloc[:, 2:3]
y_train = pydf_Train.iloc[:, 1]


# In[12]:


x_test = pydf_Test.iloc[:, 2:3]
y_test = pydf_Test.iloc[:, 1]


# In[6]:


# Taking care of missing data
# Replace the all NaN with mean
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(x_train)
x_train = imp.transform(x_train)


# In[7]:


x_train = pd.DataFrame(x_train)


# In[18]:


# # Feature Scaling
# sc_X = StandardScaler()
# sc_y = StandardScaler()
# x_train = sc_X.fit_transform(x_train)
# y_train = np.array(y_train).reshape((len(y_train), 1))
# y_train = sc_y.fit_transform(y_train)
# # print(x_train)
# print(y_train)


# In[8]:


pd_df = pd.concat([x_train,y_train], axis=1)
spark_train_df = spark.createDataFrame(pd_df)
spark_train_df.write.csv("hdfs://localhost:9000/PreproStockPrice")


# In[9]:


# Fitting Simple Linear Regression to the Training set
smlireg = LinearRegression()
smlireg.fit(x_train, y_train)


# In[13]:


# Predicting the Test set results
y_predict = smlireg.predict(x_test)


# In[14]:


# Calculating the accuracy
cal_accuracy = r2_score(y_test, y_predict)
print(cal_accuracy)

