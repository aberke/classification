# implements MNB (multinomial naive bayes algorithm) for classify



# helper to Train: creates count of number of categories -- it's just the number of lines of the categories file


# helper to Train: creates initial condprob dictionary which will have structure {t_i: {c_i:P(t_i|c_i) for c_i in categories} for t_i in features-list} 
#					where t_i and c_i are indecies of their corresponding feature terms and categories, respectively
#		--> Initializes condprob to: {t_i:{c_i: 1 for c_i in categories} for t_i in features-list}
#
# input: file name of list of features (features_filename)
#		 number of categories (C)
# output: condprob dictionary
def create_condprob(features_filename, C):
	# open up file for reading and instantiate dictionary
	f = open(features_filename, 'r')
	condprob = {}

	# each line of the file is a feature and its line is its index
	t = 0
	line = f.readline()
	while line:
		condprob[t] = {}
		for c in range(C):
			condprob[t][c] = 1
		t += 1
		line = f.readline()
	f.close()
	return condprob


# helper to train --> builds classToDocs dictionary 
# input: 1) dictionary mapping docIDs to their tuple (sum_d, feature vector) {docID: (sum_d, {f_i:occ_i for feature in features})} 
#		 2) dictionary mapping docID in training set to its class {pageID: class for pageID in training-set}
# output: dictionary mapping class to document tuples {c_i: {docID: (sum_d, feature-vector}) for c_i in categories}
def create_classToDocs(vecrep, training):
	classToDocs = {}
	for docID in training:
		c = training[docID]
		if not c in classToDocs:
			classToDocs[c] = {}
		doc_tuple = vecrep[docID]
		classToDocs[c][docID] = doc_tuple
	return classToDocs

# input: 3 arguments:
#				1) # of features V -- ie size of 'vocabulary'
#				2) vector representation of the pages in dictionary form {docID: (sum_d, {f_i:occ_i for feature in features})} 
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
# output: tuple (prior, condprob)
#				1) prior = dictionary mapping category c to P(c) --> {c_i: P(c_i) for c_i in categories}
#				2) condprob = dictionary mapping (t_i,c_i) to P(t_i|c_i) --> {t_i: {c_i: P(t_i|c_i) for c_i in categories} for t_i in features}
def train(V, vecrep, training):
	# have vecrep dict
	# have training dict
	# get total number of documents in training set
	N = len(training)
	# build classToDocs {c_i: {docID: (sum_d, feature-vector})}
	classToDocs = create_classToDocs()
	# build prior {c_i: P(c_i)=N_ci/N} where N_ci = #docs of class c_i in training set, N = total #docs in training set
	# build classToVec {c_i: (sum_c, feature-vector = sum of feature-vectors for docs of class c_i) for c_i in categories}
	# initialize condprob
	# populate condprob {t_i: {c_i: (T_ci_ti + 1)/SUM(T_ci_t' + 1) for c_i in categories} for t_i in features}
	return (prior,condprob)



# TRAINMULTINOMIALNB(C,D)
# 1 V <-- EXTRACTVOCABULARY(D)
# 2 N <-- COUNTDOCS(D)
# 3 for each c in C
# 4 do Nc <-- COUNTDOCSINCLASS(D, c)
# 5 prior[c] <-- Nc/N
# 6 textc <-- CONCATENATETEXTOFALLDOCSINCLASS(D, c)
# 7 for each t in V
# 8 do Tct <-- COUNTTOKENSOFTERM(textc, t)
# 9 for each t in V
# 10 do condprob[t][c] <-- Tct+1
# sum(t'(Tct'+1)
# 11 return V, prior, condprob

# input: 5 arguments:
#				1) # of features V -- ie size of 'vocabulary'
#				2) vector representation of the pages in dictionary form
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(V, vecrep, training, toClassify_filename, results_filename):
	# train
	prior, condprob = train(V, vecrep, training)
	# classify
	print('TODO')
	pass
	









# APPLYMULTINOMIALNB(C,V, prior, condprob,d)
# 1 W <-- EXTRACTTOKENSFROMDOC(V,d)
# 2 for each c in C
# 3 do score[c] <-- log prior[c]
# 4 for each t in W
# 5 do score[c] += logcondprob[t][c]
# 6 return arg maxc in C
# score[c