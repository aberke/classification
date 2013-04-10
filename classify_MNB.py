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




def train(vecrep, training):
	# get total number of documents in training set
	N = len(training)



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
#				1) list of features
#				2) vector representation of the pages in dictionary form
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(features_filename, vecrep, training, toClassify_filename, results_filename):
	# train
	V, prior, condprob = train(vecrep, training)
	# classify
	









# APPLYMULTINOMIALNB(C,V, prior, condprob,d)
# 1 W <-- EXTRACTTOKENSFROMDOC(V,d)
# 2 for each c in C
# 3 do score[c] <-- log prior[c]
# 4 for each t in W
# 5 do score[c] += logcondprob[t][c]
# 6 return arg maxc in C
# score[c