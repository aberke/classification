# classify.py main file

from classify_MNB import main as MNB
from classify_rocchio import main as rocchio


# input: 6 arguments:
#				1) classification method to be used (-mnb for MNB and -r for Rocchio)
#				2) list of features
#				3) vector representation of the pages
#				4) filename of training set
#				5) filename containing list of documents to be classified
#				6) filename of classification results to be generated
def main(classification_method, features_filename, vecrep_filename, training_filename, toClassify_filename, results_filename):












