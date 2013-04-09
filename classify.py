# classify.py main file

from classify_MNB import main as MNB
from classify_rocchio import main as rocchio


# helper to main for both MNB and Rocchio: recreates the vecrep dictionary from file that was created in vecrep.py
# input: filename of vector representation of the pages -- written out in format pageID sum_d f_i:occ_i ........
# output: vecrep dictionary that maps pageID to tuple (sum of sq of occurances, feature-vector), 
#			ie vecrep has structure {pageID: (sum_d, {f_i:occ_i for feature in features}) for each pageID}
def recreate_vecrep(vecrep_filename):
	# open file for reading and instantiate vecrep dictionary
    f = open(vecrep_filename, 'r')
	vecrep = {}

	lineString = f.readline()
	while lineString:
		lineList =  lineString.split()
		pageID = lineList[0]
		sum_d = lineList[1]
		feature_vector = {}
		for i in range(2, len(lineList)):
			(f_i, occ_i) = lineList[i].split(':')
			feature_vector[f_i] = occ_i
		vecrep[pageID] = (sum_d, feature_vector)

		lineString = f.readline()
	f.close()
	return vecrep

## ***** Matt to rewrite? : ******

# ....I think having the training data in dictionary form right off the bat will make it easier to work with
# creates dictionary mapping pageID to class it was classified in
#	ie {pageID: class for pageID in training-set}
# input: training_filename
# output: dictionary mapping pageID to class for each document in training set file
def create_training(training_filename):
	# open file for reading and instantiate empty dictionary
	f = open(training_filename, 'r')
	training = {}

	line = f.readline()
	while line:
		(pageID, c) = line.split()
		training[pageID] = c
		line = f.readline()
	f.close()
	return training





# input: 6 arguments:
#				1) classification method to be used (-mnb for MNB and -r for Rocchio)
#				2) list of features
#				3) vector representation of the pages written to file
#				4) filename of training set
#				5) filename containing list of documents to be classified
#				6) filename of classification results to be generated
def main(classification_method, features_filename, vecrep_filename, training_filename, toClassify_filename, results_filename):
	# recreate vecrep that was created and written to file in vecrep.py
	vecrep = recreate_vecrep(vecrep_filename)













