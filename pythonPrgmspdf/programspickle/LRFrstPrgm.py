from programspickle.BasePickleFile import *
import os
from sklearn.linear_model import LinearRegression
from programspickle.DataModel.ClassificationDM import *
from sklearn.metrics import r2_score


class LinearRegressionAlgoritham(BasePickleFile):
    def __init__(self):
        """
        LinearRegressionAlgoritham is Child class Derived from BaseBC Class
        """
        # Passing Model To Parent Class
        BasePickleFile.__init__(self, ClassificationDM.classificationmodel)

    def _DisplayGraph(self):
        """
        :return: Displays Graph
        """
        list = []
        objregression = LinearRegression()
        csv_file_path = BasePickleFile._UserInput(self)
        processed_file = BasePickleFile._datapreprocessing(self, csv_file_path)
        list = BasePickleFile._Traindataset(self, objregression, processed_file)
        if list[0] >= 0.5:
            file_name = os.path.basename(__file__).split(".")[0]
            dir_name = os.path.dirname(file_name)
            BasePickleFile._SaveModel(self, objregression, file_name, dir_name)

        else:
            BasePickleFile._Traindataset(self, objregression, csv_file_path)

        """
        # TODO
        assign specific values/description for labels and title dynamically Based Of Graph Type 
        """
        # Region To Get Values From List
        xTrainvalue = list[1].xTrain
        yTrainvalue = list[1].yTrain
        xTestvalue = list[1].xTest
        yTestvalue = list[1].yTest
        title = "prediction"
        xlable= "X-axis"
        ylable= "Y-axis"

        # End Region

        # Region Ploting Graph
        # BaseBC._DistributionGraph(self, xTrainvalue, yTrainvalue, objregression, title, xlable, ylable)
        BasePickleFile._GrphPloting(self, xTrainvalue, yTrainvalue, objregression, title, xlable, ylable)
        # Plotting Test Data
        BasePickleFile._GrphPloting(self, xTestvalue, yTestvalue, objregression, "TestPrediction", xlable, ylable)

        # EndRegion

        # Region TestModel
        pkl_file_name = input("Enter Pickle File Path")
        test_data = input("Enter TestData File Path")
        BasePickleFile.test_model(self, pkl_file_name, test_data)

        # End Region


objlinearRegression = LinearRegressionAlgoritham()
# objlinearRegression._DisplayGraph()
