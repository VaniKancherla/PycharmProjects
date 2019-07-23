#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import findspark
from pyspark import SparkContext, SparkConf
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# In[2]:


# findspark.init("/home/vaninewVM/spark-2.4.3-bin-hadoop2.7")


# In[4]:


# Importing iris data set
pydf_Train = sqlContext.read.format('com.databricks.spark.csv').options(header='true').load('hdfs://localhost:9000//Applying-Linear-Regression-on-Iris-Dataset/iris-dataset.csv')
print(type(pydf_Train))
pydf_Train=pydf_Train.toPandas()
print(type(pydf_Train))


# In[5]:


x = pydf_Train.iloc[:, 2:3] # C column
# print(x)
y= pydf_Train.iloc[:, 1:2] # B column
# print(y)


# In[6]:


# Taking care of missing data
# Replace the all NaN with mean
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp = imp.fit(x)
x = imp.transform(x)
# print(x)


# In[7]:


x = pd.DataFrame(x)
# print(x)


# In[8]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# In[9]:


# Fitting Simple Linear Regression to the Training set
smlireg = LinearRegression()
smlireg.fit(x_train, y_train)


# In[10]:


# Predicting the Test set results
y_predict = smlireg.predict(x_test)
# print(y_predict)
# print(x_test)


# In[11]:


#calculating accuracy
accuracy = r2_score(y_test, y_predict)
print(accuracy)


# In[13]:


df_xtest = pd.DataFrame(x_test)
df_ypredict = pd.DataFrame(y_predict)
# print(df_xtest)
# print(df_ypredict)


# In[15]:


#uploading the Preprocessing iris data set to hdfs
uploadiris1 = pd.concat([x_train, y_train], axis=1)
spark_df1 = spark.createDataFrame(uploadiris1)
spark_df1.write.csv("hdfs://localhost:9000/PreprocessingIris")


# In[ ]:




