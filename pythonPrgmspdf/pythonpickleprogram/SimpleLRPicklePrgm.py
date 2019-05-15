import pickle
import pandas as pd
# Scikit-learn method to split the dataset into train and test dataset
from sklearn.model_selection import train_test_split
# Scikit-learn method to implement the decsion tree classifier
from sklearn.tree import DecisionTreeClassifier


# Load the dataset
balance_scale_data = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data', sep=',', header=None)
print("Dataset Length:: ", len(balance_scale_data))
print("Dataset Shape:: ", balance_scale_data.shape)

# Split the dataset into train and test dataset
X = balance_scale_data.values[:, 1:5]
Y = balance_scale_data.values[:, 0]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

# Decision model with Gini index critiria
decision_tree_model = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
decision_tree_model.fit(X_train, y_train)
y_pred = decision_tree_model.predict(X_test)
print(y_pred)


# Dump the trained decision tree classifier with Pickle
decision_tree_pkl_filename = 'decision_tree_classifier_20170212.pkl'
# Open the file to save as pkl file
decision_tree_model_pkl = open(decision_tree_pkl_filename, 'wb')
pickle.dump(decision_tree_model, decision_tree_model_pkl)
# Close the pickle instances
decision_tree_model_pkl.close()

# Loading the saved decision tree model pickle
decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
decision_tree_model = pickle.load(decision_tree_model_pkl)

y_pred = decision_tree_model.predict(X_test)
print(y_pred)

