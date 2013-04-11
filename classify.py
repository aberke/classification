# classify.py main file

import sys

from classify_util import feature_count

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
		pageID = int(lineList[0])
		sum_d = int(lineList[1])
		feature_vector = {}
		for i in range(2, len(lineList)):
			(f_i, occ_i) = lineList[i].split(':')
			feature_vector[int(f_i)] = int(occ_i)
		vecrep[pageID] = (sum_d, feature_vector)

		lineString = f.readline()
	f.close()
	return vecrep


# creates dictionary mapping pageID to class it was classified in to make training data easier to work with
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
		training[int(pageID)] = int(c)
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
	# create features count (V) since then we can use its range as f_i indecies which is all we care about
	V = feature_count(features_filename)
	# recreate vecrep that was created and written to file in vecrep.py {docID: (sum_d, {f_i:occ_i for feature in features})} 
	vecrep = recreate_vecrep(vecrep_filename)
	# turn training data file into dictionary form
	training = create_training(training_filename)
	# determine if using bayes or rocchio algorithm
	if classification_method == '-mnb':
		return MNB(V, vecrep, training, toClassify_filename, results_filename)
	elif classification_method == '-r':
		return rocchio(V, vecrep, training, toClassify_filename, results_filename)
	else:
		print("Must specify algorithm as MNB (flag '-mnb') or Rocchio (flag '-r')")
		return









main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])




