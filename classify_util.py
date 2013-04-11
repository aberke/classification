# utility procedures relevant to both MNB and Rocchio

from math import sqrt

# counts features because there is a feature index f_i for each feature, and we only care about that index
# input:  features filename
# output: feature count (V)
def feature_count(features_filename):
	# open file for reading each line and initialize count (V)
    f = open(features_filename, 'r')
    V = 0

    w = f.readline()
    while w != '' and w != '\n': # read to EOF
        V += 1
        w = f.readline()
    f.close()
    return V

# helper to create_classToDocs -- normalizes the given document vector
# input:  tuple (sum_d, document-vector) where sum_d is the sum of the square of the occurances of features in the document vector
# output: normalized document-vector
def tuple_to_normalizedVector(docTuple):
	# unpack tuple and initialize normalized document-vector, calculate norm
	(sum_d, document_vector) = doc_tuple
	normalized_document_vector = {}
	norm = sqrt(sum_d)
	# now fill in normalized-vector
	for t in document_vector:
		normalized_document_vector[t] = document_vector[t]/norm
	return normalized_document_vector

# helper to train for both MNB and Rocchio--> builds classToDocs dictionary which turns training set into dictionary mapping class to (docID, document vector tuple)
# input: 1) dictionary mapping docIDs to their tuple (sum_d, feature vector) {docID: (sum_d, {f_i:occ_i for feature in features})} 
#		 2) dictionary mapping docID in training set to its class {pageID: class for pageID in training-set}
#		 3) boolean that's true if process should also normalize each document vector, false if it should not normalize them
# output: dictionary mapping class to document tuples {c_i: {docID: (sum_d, feature-vector}) for c_i in categories}
def create_classToDocs(vecrep, training, normalize_bool):
	# first we'll just map class to dictionary of document tuples (sum_d, document-vector)
	classToDocTuple = {}
	for docID in training:
		c = training[docID]
		if not c in classToDocTuple:
			classToDocTuple[c] = {}
		doc_tuple = vecrep[docID]
		classToDocTuple[c][docID] = doc_tuple
	
	# now use classToDocTuple to map each class to its document-vectors (normalized or not normalized based on boolean argument)
	classToDocs = {}
	for c in classToDocTuple:
		classToDocs[c] = {}
		for docID in classToDocTuple[c]:
			if normalize_bool:
				classToDocs[c][docID] = tuple_to_normalizedVector(classToDocTuple[c][docID])
			else:
				classToDocs[c][docID] = classToDocTuple[c][docID][1]
	return classToDocs

# combines all the document vectors corresponding to a given class to one vector representing the feature vector of that class
# input:  1) classToDocs dictionary {c_i: {docID: feature-vector}}
#		  2) number of features (V) so that feature indecies are range of V
# output: classToVec dictionary {c_i: SUM(feature-vectors) for c_i in categories}
def create_classToVec(classToDocs, V):
	classToVec = {}
	for c in classToDocs:
		feature_vec = {}
		for f in range(V):
			feature_vec[f] = 0
			for docID in classToDocs[c]:
				doc_vec = classToDocs[c][docID]
				if f in doc_vec:
					feature_vec[f] += doc_vec[f]
		classToVec[c] = feature_vec
	return classToVec

# helper to create_classToCentroid: 
def normalize_classToDocs(classToDocs):


def create_classToCentroid(classToDocs, V):
	# will utilize create_classToVec's, but first needs to normalize each document vector since u_i = (1/D_i)SUM(v(d) for d in D_i) and v(d) is a normalized vector
	normalized_classToDocs = normalize_classToDocs(classToDocs)




