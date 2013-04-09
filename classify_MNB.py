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






# input: 5 arguments:
#				1) list of features
#				2) vector representation of the pages in dictionary form
#				3) filename of training set
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(features_filename, vecrep, training_filename, toClassify_filename, results_filename):
	# get total number of documents











TRAINMULTINOMIALNB(C,D)
1 V ← EXTRACTVOCABULARY(D)
2 N ← COUNTDOCS(D)
3 for each c ∈ C
4 do Nc ← COUNTDOCSINCLASS(D, c)
5 prior[c] ← Nc/N
6 textc ← CONCATENATETEXTOFALLDOCSINCLASS(D, c)
7 for each t ∈ V
8 do Tct ← COUNTTOKENSOFTERM(textc, t)
9 for each t ∈ V
10 do condprob[t][c] ← Tct+1
∑t
′(Tct′+1)
11 return V, prior, condprob

APPLYMULTINOMIALNB(C,V, prior, condprob,d)
1 W ← EXTRACTTOKENSFROMDOC(V,d)
2 for each c ∈ C
3 do score[c] ← log prior[c]
4 for each t ∈ W
5 do score[c] += logcondprob[t][c]
6 return arg maxc∈C
score[c