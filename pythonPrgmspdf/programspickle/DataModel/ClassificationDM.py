import collections


class ClassificationDM:
    classificationmodel = collections.namedtuple('Data', ['xTrain', 'xTest', 'yTrain', 'yTest'])

