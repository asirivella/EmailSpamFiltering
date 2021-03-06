import csv
import random
import math
import sklearn
from sklearn import datasets
from sklearn import svm

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main ():
	splitRatio = 0.6
	filename = 'spambase.data'
	dataset = loadCsv(filename)
	trainSet,testSet = splitDataset(dataset, splitRatio)
	trainLabel = [row[57] for row in trainSet]
	print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainSet), len(testSet))
	model = svm.SVC(probability = True)
	model.fit(trainSet, trainLabel)
	predicted = clf.predict(testSet)
	accuracy = getAccuracy(testSet, predicted)
	print('Accuracy: ' + repr(accuracy) + '%')

import time
start_time = time.time();
main()
print("%s seconds" % (time.time() - start_time))