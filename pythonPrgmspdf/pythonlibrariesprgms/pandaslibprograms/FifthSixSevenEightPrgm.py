import pandas as pd
import numpy as np

# 5th prgm

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
# 6th prgm
print(df)
print("Info: ", df.info())

# 7th prgm
print("First three rows of the data frame:")
print(df.iloc[:3])

# 8th prgm
# print("to select the 'name' and 'score': ")
print(df['name'])
print(df['score'])











