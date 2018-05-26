'''
Created on 27-Nov-2016

@author: timmy
'''
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

# Boilerplate Spark stuff:
conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc = SparkContext(conf=conf)


# Some functions that convert our CSV input data into numerical
# features for each job candidate
def binary(YN):
    if (YN == 'Y'):
        return 1
    else:
        return 0


def mapEmpLen(empLen):
    if (empLen == '< 1 year'):
        return 0
    elif (empLen == '1 year'):
        return 1
    elif (empLen == '2 years'):
        return 2
    elif (empLen == '3 years'):
        return 3
    elif (empLen == '4 years'):
        return 4
    elif (empLen == '5 years'):
        return 5
    elif (empLen == '6 years'):
        return 6
    elif (empLen == '7 years'):
        return 7
    elif (empLen == '8 years'):
        return 8
    elif (empLen == '9 years'):
        return 9
    elif (empLen == '10+ years'):
        return 10
    else:
        return 11


def mapTitle(title):
    if (title == 'Debt consolidation'):
        return 1
    elif (title == 'Business'):
        return 2
    elif (title == 'Car financing'):
        return 3
    elif (title == 'Credit card refinancing'):
        return 4
    elif (title == 'Green loan'):
        return 5
    elif (title == 'Home buying'):
        return 6
    elif (title == 'Home improvement'):
        return 7
    elif (title == 'Major purchase'):
        return 8
    elif (title == 'Medical expenses'):
        return 9
    elif (title == 'Moving and relocation'):
        return 10
    elif (title == 'Vacation'):
        return 11
    else:
        return 0


# Convert a list of raw fields from our CSV file to a
# LabeledPoint that MLLib can use. All data must be numerical...
# loantitle,employmentlength,dti,amountrequested,zipcode,state,status
def createLabeledPoints(fields):
    loantitle = mapTitle(fields[0])
    employmentlength = mapEmpLen(fields[1])
    dti = float(fields[2])
    amountrequested = float(fields[3])
    # zipcode = (fields[4])
    # state = binary(fields[5])
    status = fields[6]

    return LabeledPoint(status, array([loantitle, employmentlength,
                                       dti, amountrequested]))


def createNpArr(fields):
    loantitle = mapTitle(fields[0])
    employmentlength = mapEmpLen(fields[1])
    dti = float(fields[2])
    amountrequested = float(fields[3])
    # zipcode = (fields[4])
    # state = binary(fields[5])
    # status = fields[6]

    return array([loantitle, employmentlength,
                  dti, amountrequested])


# Load up our CSV file, and filter out the header line with the column names
rawData = sc.textFile("../data/preproc_loan.csv")
# header = rawData.first()
# rawData = rawData.filter(lambda x:x != header)

# Split each line into a list based on the comma delimiters
csvData = rawData.map(lambda x: x.split(","))

# Convert these lists to LabeledPoints
test_1, train_1 = csvData.randomSplit(weights=[0.01, 0.99], seed=1)

test = test_1.map(createNpArr)
test_original = test_1.map(lambda x: float(x[6]))

print test_original.count()
print test_original.take(10)

train = train_1.map(createLabeledPoints)
# Build the model
model = DecisionTree.trainClassifier(train, numClasses=2,
                                     categoricalFeaturesInfo={0: 12, 1: 12},
                                     impurity='gini', maxDepth=5, maxBins=32)

predictions = model.predict(test)
# print ('Storing prediction:')
# print type(test)
# print type(predictions)
# print test.count()
# print predictions.count()
# print predictions.take(10)
# print type(array(predictions))
# results = [array(predictions)]
# for result in results:
#    print result


# predictions.saveAsTextFile('output')

# We can also print out the decision tree itself:
print('Learned classification tree model:')
print(model.toDebugString())

predictionAndLabels = test_original.zip(predictions)

print predictionAndLabels.take(10)


def evaluate(predictionAndLabels):
    tn = predictionAndLabels.filter(lambda (predicted, actual): actual == 0 and predicted == 0).count()
    fp = predictionAndLabels.filter(lambda (predicted, actual): actual == 0 and predicted == 1).count()
    fn = predictionAndLabels.filter(lambda (predicted, actual): actual == 1 and predicted == 0).count()
    tp = predictionAndLabels.filter(lambda (predicted, actual): actual == 1 and predicted == 1).count()

    print 'tn ', tn
    print 'fp ', fp
    print 'fn ', fn
    print 'tp ', tp

    # Closer to 1 is better
    tpr = float(tp) / (tp + fn)

    # Closer to 0 is better
    fpr = float(fp) / (fp + tn)

    # accuracy = (tp+fp)/(tp+fp+fn+tn)
    return tpr, fpr


print 'Accuracy (tpr, fpr) : ', evaluate(predictionAndLabels)
