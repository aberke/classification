# implements MNB (multinomial naive bayes algorithm) for classify



# input: 5 arguments:
#				1) list of features
#				2) vector representation of the pages
#				3) filename of training set
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(features_filename, vecrep_filename, training_filename, toClassify_filename, results_filename):
	










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