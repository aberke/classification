# build_featuresADV.py
# Compile a featuresADV.dat file from a given training corpus

import sys, operator
from vecrep_util import parse, tokenize, create_stopwords_set

import searchio  # import our own optimized I/O module

# creates dictionary mapping pageID to class it was classified in to make training data easier to work with
# input: training_filename
# output: dictionary mapping pageID to class for each document in training set file {pageID: class for pageID in training-set}
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

# input: <stopWords filename>, <pagesCollection filename>, <training filename>, <features output filename to be built>
# output: a feature list based on term popularity in the collection, by category
def main(stopwords_filename, pagesCollection_filename, training_filename, output_filename):
	# obtain the stopwords in a set for quick checking
	stopWords_set = create_stopwords_set(stopwords_filename)

	# obtain dictionary mapping pageID's to list of title and text words, ie collection = {pageID: textString}
	(collection, maxID) = parse(pagesCollection_filename)
	
	# load in the training categories
	training = create_training(training_filename)
	
	# create some structures to hold the terms
	terms = set()
	termsByCategory = {
		0: {},
		1: {},
		2: {},
		3: {},
		4: {},
		5: {},
		6: {},
		7: {},
		8: {},
		9: {},
		10: {}
	}
	termCountByCategory = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0,
		10: 0
	}
	termWeights = {
		0: {},
		1: {},
		2: {},
		3: {},
		4: {},
		5: {},
		6: {},
		7: {},
		8: {},
		9: {},
		10: {}
	}
	
	# create a set to hold the result
	result = set()
	
	# iterate over training data
	for pageID in training:
		if not pageID in collection:
			print(str(pageID)+' not in collection!!')
			#continue
			return ####
		
		# tokenize the document
		textString = collection[pageID]
		token_list = searchio.tokenize(stopWords_set, textString, False)
		category = training[pageID]
		
		# increment token counts
		for token in token_list:
			terms.add(token)
			termCountByCategory[category] += 1
			
			if not token in termsByCategory[category]:
				termsByCategory[category][token] = 0
			
			termsByCategory[category][token] += 1
	
	# weight all of the terms
	for category in termsByCategory:
		categoryTerms = termsByCategory[category]
		for term in categoryTerms:
			termAvg = 0
			for otherCategory in termsByCategory:
				if category != otherCategory and term in termsByCategory[otherCategory]:
					termAvg += termsByCategory[otherCategory][term]
			
			termAvg /= 10
			
			# a term's weight is the frequency in the category minus the average frequency in other categories
			termWeights[category][term] = categoryTerms[term] - termAvg
	
	# for each category, sort terms by weight, and take up to 10000 of them
	for category in termWeights:
		weighted = sorted(termWeights[category].iteritems(), key=operator.itemgetter(1))
		result |= set(t for (t, w) in weighted[:10000])
	
	# output the result
	f = open(output_filename, 'w')
	for term in result:
		f.write(term + '\n')
	f.close()
				
main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
