# implements MNB (multinomial naive bayes algorithm) for classify

import heapq # using heap to store max P(c|d) in apply
from math import log


from classify_util import create_classToDocs, create_classToVec, create_categories, print_classified



# input: 1) classToDocs dictionary {c_i: {docID: (sum_d, feature-vector)} for c_i in categories}
#		 2) total number of documents in training set (N)
# output: prior dictionary that maps class to its prior probability, ie {c_i: P(c_i)=N_ci/N} where N_ci = #docs of class c_i in training set, N = total #docs in training set
def create_prior(classToDocs, N):
	prior = {}
	for c in classToDocs:
		prior[c] = (float(len(classToDocs[c]))/N)
	return prior

# helper to create conditional probability, which needs to SUM(T_c_t for each T in V)
# input:  feature-vector for given class (should come from classToVec)
# output: sum of all occurances in that feature-vector
def create_sumOccurances(feature_vec):
	sum_occ = 0
	for f in feature_vec: # for each term in vocabulary
		sum_occ += feature_vec[f] # SUM += T_c_t  since T = feature_vec[f]
	return sum_occ

# helper to create_condprob, this dictionary mapping each class c to SUM(T_c_t for each t in vocabulary (V or feature set)) which are parts of denominators of P(t|c)'s
# input:  classToVec dictionary which maps classes to their feature vectors
# output: dictionary mapping each class c to SUM(T_c_t for each t in vocabulary (V or feature set))
def create_classToSumOccurances(classToVec):
	classToSumOccurances = {}
	for c in classToVec:
		feature_vec = classToVec[c]
		classToSumOccurances[c] = create_sumOccurances(feature_vec)
	return classToSumOccurances

# input:  1) classToVec dictionary mapping class to its feature-vector {c_i: feature-vector = sum of feature-vectors for docs of class c_i) for c_i in categories}
# 		  2) number of features (V) so that set of features indecies can be range(V)
# output: dictionary of conditional probabilities {t_i: {c_i: P(t_i|c_i) for c_i in categories} for t_i in V}
def create_condprob(classToVec, V):
	condprob = {}
	# for demonitors of P(t|c) we need SUM(T_c_t for each t in vocabulary (V or feature set)) but we use these same values again and again, so just make dictionary upfront:
	classToSumOccurances = create_classToSumOccurances(classToVec)
	for t in range(V):
		condprob[t] = {}
		for c in classToVec:
			if not t in classToVec[c]:
				numerator = 1 # <-- +1 for Laplace smoothing
			else:
				numerator = classToVec[c][t] + 1 # <-- +1 for Laplace smoothing
			denominator = classToSumOccurances[c] + V
			condprob[t][c] = float(numerator)/denominator
	return condprob


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
###############################
# input: 3 arguments:
#				1) # of features V -- ie size of 'vocabulary'
#				2) vector representation of the pages (unnormalized) in dictionary form {docID: {f_i:occ_i for feature in features})} 
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
# output: tuple (prior, condprob)
#				1) prior = dictionary mapping category c to P(c) --> {c_i: P(c_i) for c_i in categories}
#				2) condprob = dictionary mapping (t_i,c_i) to P(t_i|c_i) --> {t_i: {c_i: P(t_i|c_i) for c_i in categories} for t_i in features}
def train(V, vecrep, training):
	# get total number of documents in training set
	N = len(training)
	# build classToDocs {c_i: {docID: feature-vector}}
	classToDocs = create_classToDocs(vecrep, training)
	# build prior {c_i: P(c_i)=N_ci/N} where N_ci = #docs of class c_i in training set, N = total #docs in training set
	prior = create_prior(classToDocs, N)
	# build classToVec {c_i: feature-vector = sum of feature-vectors for docs of class c_i) for c_i in categories}
	classToVec = create_classToVec(classToDocs, V)
	# build condprob dictionary of conditional probabilities {t_i: {c_i: P(t_i|c_i) for c_i in categories} for t_i in V}
	condprob = create_condprob(classToVec, V)
	# also get set of categories so it can be used in apply
	return (prior,condprob)

# test prior real quick
def test_prior(prior):
	prior_sum = 0
	for p in prior:
		prior_sum += prior[p]
	print('prior_sum = '+str(prior_sum))
	return


# APPLYMULTINOMIALNB(C,V, prior, condprob,d)
# 1 W <-- EXTRACTTOKENSFROMDOC(V,d)
# 2 for each c in C
# 3 do score[c] <-- log prior[c]
# 4 for each t in W
# 5 do score[c] += logcondprob[t][c]
# 6 return arg maxc in C
# score[c]	
############################################
# input: implicit: categories set is keys of prior
#		 1) # of features V -- ie size of 'vocabulary' --> set if feature indecies is range(V)
#		 2) vector representation of the pages in dictionary form {docID: (sum_d, {f_i:occ_i for feature in features})} 
#		 3) prior dictionary mapping classes c to P(c) --> {c_i: P(c_i)=N_ci/N} where N_ci = #docs of class c_i in training set, N = total #docs in training set
#		 4) condprob dictionary of conditional probabilities {t_i: {c_i: P(t_i|c_i) for c_i in categories} for t_i in V}
#		 5) docID to find most probable class c of
# output: best c to map docID to
def applyMNB(V, vecrep, prior, condprob, docID):
	(sum_d, d_vector) = vecrep[docID]
	c_heap = []  # uses min-heap turned into max-heap by storing negative values to store P(c|d)'s and retrieve max

	for c in prior:
		score = log(prior[c])
		for t_i in d_vector:
			T_i = d_vector[t_i]
			score += T_i*(log(condprob[t_i][c])) # score will be negative since P(t|c) < 1
		entry = ((-1)*score, c)
		heapq.heappush(c_heap, entry)
	# pop off c with highest probability
	print('heap: ')
	print(c_heap)
	maxc = heapq.heappop(c_heap)[1]
	return maxc

# input:  filename of docID's to classify and all the necessary components for apply to classify with
# output: list classified = [(docID, class) for docID in toClassify_filename]
def classifyMNB(V, vecrep, prior, condprob, toClassify_filename):
	# open toClassify and initialize classified list
	f_toClassify = open(toClassify_filename, 'r')
	classified = []
	# for each docID, classify it and add tuple (docID, class) to classified
	line = f_toClassify.readline()
	while (line and line != '\n'):
		docID = int(line.split()[0])
		print('to Classify: '+str(docID))
		c = applyMNB(V, vecrep, prior, condprob, docID)
		classified.append((docID,c))
		line = f_toClassify.readline()
	f_toClassify.close()
	return classified


# input: 5 arguments:
#				1) # of features V -- ie size of 'vocabulary'
#				2) vector representation of the pages (unnormalized) in dictionary form {docID: {f_i:occ_i for feature in features})} 
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(V, vecrep, training, toClassify_filename, results_filename):
	# train
	print('to train')
	prior, condprob = train(V, vecrep, training)
	print('trained')
	# classify each document in toClassify and store (docID, class) tuples in classified list --> get classified = [(docID, class) for docID in toClassify_filename]
	classified = classifyMNB(V, vecrep, prior, condprob, toClassify_filename)
	print('classified')
	# print results to results_filename with 'docID class' entry on each line
	print_classified(classified, results_filename)
	print('done')
	return





