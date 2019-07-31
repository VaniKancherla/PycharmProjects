import pandas as pd
import os
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as mat
from programspickle.DataModel.ClassificationDM import *
from sklearn.metrics import r2_score
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer


class BasePickleFile(object):
    # BaseBC is Define As Parent Class
    def __init__(self, classificationmodel):  # Constructor of BaseBC
        """
         Initializing __init__ with given param
        :param classificationmodel:
         Returns:  Model with given properties
        """
        self.classificationmodel = classificationmodel

    def _CreateClassificationModel(self, csv_file_path):  # Data Pre-processing Method
        """
        :param none:
        :return:Prepared Model with all assigned Values
        """
        try:
            data_set = pd.read_csv(csv_file_path)
            variables = input("Enter Comma Separated Variables you want to select")
            x1, y1 = [word for word in variables.split(",")]
            x = data_set.loc[:, [x1.strip()]].values
            y = data_set.loc[:, [y1.strip()]].values
            classificationmodel = train_test_split(x, y, test_size=1/3, random_state=0)
            return classificationmodel

        except:
            print("File Extention should be .csv")

    def _UserInput(self):

        userInput = input("Enter File Path: ")  # Take User Input as file path
        if not userInput.endswith('.csv'):  # Check file Extention is .csv
            raise ValueError("File format invalid")
        if not os.path.isfile(userInput):
            raise FileNotFoundError("File does not exist at path:")
        return userInput

    def _SplitDataFiles(self, userInput):
        """
        :param userInput:
        :return: Two Files TRain And Test
        """
        try:
            df = pd.read_csv(userInput)
            count = df.count()[0]
            train_count = int(0.8 * count)
            # test_count = 0.2 * count
            train_frame, test_frame = df.iloc[:train_count, :], df.iloc[train_count:, :]
            dir_name = os.path.dirname(userInput)
            file_name = os.path.basename(userInput).split(".")[0]
            train_file = BasePickleFile._create_file(self, file_name, "_train")
            test_file = BasePickleFile._create_file(self, file_name, "_test")
            train_file_path = BasePickleFile._make_csv_file(self, train_frame, dir_name, "train", train_file)
            BasePickleFile._make_csv_file(self, test_frame, dir_name, "test", test_file)
            return train_file_path
        except:
            print("directory Not Created")

    def _create_file(self, file_name, suffix):
        extension = ".csv"
        f_name = file_name + suffix + extension
        return f_name

    def _make_csv_file(self, data_frame, dir_path, dir_name, file_name):
        final_dir = os.path.join(dir_path, dir_name)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
        file_name = os.path.join(final_dir, file_name)
        data_frame.to_csv(file_name, header=True, index=False)
        return file_name

    def _DistributionGraph(self, classification, x_data, y_data):  # plotting graph
        """
             :param regression:Is a Prepared Model object of Regression
             :param x_data: Values you want to show on X-Axis
             :param y_data:Values you want to show on Y-Axis
             :return:Displays Graph
        """
        mat.scatter(x_data, y_data, color='Red')
        mat.plot(x_data, classification.predict(x_data), color='blue')
        mat.title("Salary Vs Experience")
        mat.xlabel("Years Of Experience")
        mat.ylabel("Salary")
        mat.show()

    def _SaveModel(self, regression_model, file_name, dir_name):
        """
        :arg:
        :param regression_model: Model which you want to save to directory
        :param file_name: name of file you want to save pickle file
        :param dir_name: directory to which you want to save your model
        :return:none
        object of Model in
        """
        new_dir_name = "classificationmodel"
        final_dir_path = os.path.join(dir_name, new_dir_name)
        if not os.path.exists(final_dir_path):
            os.makedirs(final_dir_path)
        new_file_name = file_name + ".pkl"
        final_path = os.path.join(final_dir_path, new_file_name)
        classification_pkl = open(final_path, 'wb')
        pickle.dump(regression_model, classification_pkl)
        classification_pkl.close()

    def _Traindataset(self, objregression, processed_file):
        """
        :param objregression: its an object of alogoritham module
        :param csv_file_path: file on which dataset you want to train dataset
        :return: list object that contains "accuracy", created "reggression_model","csv_file_path"
        """
        # Calling Parent Class Method To Get Train And Test Separated Data
        dataparam=[]
        train_path = BasePickleFile._SplitDataFiles(self, processed_file)

        # call for Data Pre processing function

        classification_model = BasePickleFile._CreateClassificationModel(self, train_path)
        """
        *dataset is used to get all Key Fields of Model or from namedtuple
        """
        classification_model = ClassificationDM.classificationmodel(*classification_model)
        objregression.fit(classification_model.xTrain, classification_model.yTrain)
        y_predict = objregression.predict(classification_model.xTest)
        #finding Accuracy
        accuracy = r2_score(classification_model.yTest, y_predict)
        # end region
        dataparam.append(accuracy)
        dataparam.append(classification_model)
        dataparam.append(processed_file)
        dataparam.append(y_predict)
        return dataparam

    def _GrphPloting(self, xvalue, yvalue, objregression, title, xlable, ylable ):
        X_grid = np.arange(min(xvalue), max(xvalue), 0.01)
        X_grid = X_grid.reshape((len(X_grid), 1))
        mat.scatter(xvalue, yvalue, color='red')
        # plot predicted data
        mat.plot(X_grid, objregression.predict(X_grid), color='blue')
        # specify title
        mat.title(title)
        # specify X axis label
        mat.xlabel(xlable)
        # specify Y axis label
        mat.ylabel(ylable)
        # show the plot
        mat.show()

    def _DistributionGraph(self, xvalue, yvalue, objregression, title, xlable, ylable ):  # plotting graph
        """
             :param regression:Is a Prepared Model object of Regression
             :param x_data: Values you want to show on X-Axis
             :param y_data:Values you want to show on Y-Axis
             :return:Displays Graph
        """
        mat.scatter(xvalue, yvalue, color='Red')
        mat.plot(xvalue, objregression.predict(xvalue), color='blue')
        mat.title(title)
        mat.xlabel(xlable)
        mat.ylabel(ylable)
        mat.show()

    # def _LogisticRegression(self, xvalue, yvalue, objregression, title, xlable, ylable):

    def load_model(self, pickleFilePath):
            trained_model_pkl = open(pickleFilePath, 'rb')
            trained_model = pickle.load(trained_model_pkl)
            return trained_model

    def test_model(self, pickleFilePath, userTestFile):
        data_set = pd.read_csv(userTestFile)
        x_data = data_set.iloc[:, :-1].values
        model = self.load_model(pickleFilePath)
        y_predict = model.predict(x_data)
        print(y_predict)

    def _datapreprocessing(self, csv_file_path):
        """""
        :return: Clean Data set after applying necessary pre-processing steps on data
        """
        """
        imputation fills in the missing value with some number. 
        The imputed value won't be exactly right in most cases, 
        but it usually gives more accurate models than dropping the column entirely.     
        The default behavior fills in the mean value for imputation.
        """
        missing_values = ["n/a", "na", "-"]
        df = pd.read_csv(csv_file_path, na_values=missing_values)
        # Check For missing Data and null

        if df.isnull().sum().sum() > 0:
            df_1 = pd.DataFrame((df).astype('category'))
            imp = SimpleImputer(strategy="most_frequent")
            imp = imp.fit_transform(df_1)
            new_dataframe = pd.DataFrame(imp)
        else:
                new_dataframe= df
