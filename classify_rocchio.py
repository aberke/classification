# implements Rocchio algorithm for classify

import heapq # used to return argmin ||u_j - v(d)||


# APPLY({u_1, u_2,..., u_k}, d):
# 1 return arg minj ||µj − v(d)||
##########################################
# input:  1) classToCentroid dictionary {c_i: u_i} where u_i of form {t_i:occ_i for t_i in features(V)} and u_i = (1/|D_i|)SUM(v(d) for d in D_i)
#		  2) vector representation of the pages (normalized) in dictionary form {docID: {f_i:occ_i for feature in features})} 
#		  3) docID of docment to classify
# output: classification of document docID
def applRocchio(classToCentroid, vecrep, docID):
	doc_vec = vecrep[docID]
	min_tup = (float("inf"), None) # keep tuple of min (score_c, c)
	for c_i in classToCentroid:
		u_i = classToCentroid[c_i]
		norm_sq = 0
		for t in u_i:
			if t in doc_vec:
				norm_sq += (u_i[t] - doc_vec[t])**2
			else:
				norm_sq += u_i[t]**2
		if norm_sq < min_tup[0]:
			min_tup = (norm_sq, c_i)
	return min_tup[c_i]

# input:  filename of docID's to classify and all the necessary components for apply to classify with
# output: list classified = [(docID, class) for docID in toClassify_filename]
def classifyRocchio(classToCentroid, vecrep, toClassify_filename):
	# open toClassify and initialize classified list
	f_toClassify = open(toClassify_filename, 'r')
	classified = []
	# for each docID, classify it and add tuple (docID, class) to classified
	line = f_toClassify.readline()
	while (line and line != '\n'):
		docID = int(line.split()[0])
		c = applyRocchio(classToCentroid, vecrep, docID)
		classified.append((docID,c))
		line = f_toClassify.readline()
	f_toClassify.close()
	return classified	

# combines all the document-vectors that a class maps to into their centroid
# input:  1) # of features V -- ie size of 'vocabulary'
#		  2) classToDocs dictionary mapping class to (normalized) documents in that class {c_i: {docID: feature-vector} for c_i in categories}
# output: dictionary mapping class to centroid {c_i: u_i} where u_i of form {t_i:occ_i for t_i in features(V)} and u_i = (1/|D_i|)SUM(v(d) for d in D_i)
def classToCentroid(V, classToDocs):
	# initalize empty classToCentroid dictionary 
	classToCentroid = {}
	for c_i in classToDocs:
		docs_i = classToDocs[c_i]
		# retrieve D_i = number of documents mapped to c_i
		D_i = len(docs_i)
		# initialize empty centroid u and then fill it in with sum
		u = {}
		for t in range(V):
			sum_t = 0
			for docID in docs:
				if t in docs_i[docID]:
					sum_t += docs_i[docID][t]
			u[t] = float(sum_t)/D_i
		classToCentroid[c_i] = u
	return classToCentroid

# TRAINROCHIO(C,D):
# 1   for each c_j in C:
# 2		  do D_j = {d: <d, c_j> in D}
# 3		  u_j = 1/|D_j|SUM(v(d) for d in D_j)
# 4	  return {u_1, u_2,...., u_k}
##########################################
# input:  1) # of features V -- ie size of 'vocabulary'
#		  2) vector representation of the pages (normalized) in dictionary form {docID: {f_i:occ_i for feature in features})} 
#		  3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
# output: dictionary mapping class to centroid {c_i: u_i for each c_i in categories} where u_i of form {t_i:occ_i for t_i in features(V)}
def train(V, vecrep_normalized, training):
	# creat classToDocs dictionary mapping class to (normalized) documents in that class {c_i: {docID: feature-vector} for c_i in categories}
	classToDocs = create_classToDocs(vecrep_normalized, training)
	# combine all the document-vectors that a class maps to into their centroid
	classToCentroid = create_classToCentroid(V, classToDocs)
	return classToCentroid


# input: 5 arguments:
#				1) # of features V -- ie size of 'vocabulary'
#				2) vector representation of the pages (normalized) in dictionary form {docID: {f_i:occ_i for feature in features})} 
#				3) training set as dictionary mapping pageID to class, ie {pageID: class for pageID in training set}
#				4) filename containing list of documents to be classified
#				5) filename of classification results to be generated
def main(V, vecrep_normalized, training, toClassify_filename, results_filename):
	# train
	classToCentroid = train(V, vecrep_normalized, training)
	# classify each document in toClassify and store (docID, class) tuples in classified list --> get classified = [(docID, class) for docID in toClassify_filename]
	classified = classifyRocchio(classToCentroid, vecrep, toClassify_filename)
	# print results to results_filename with 'docID class' entry on each line
	print_classified(classified, results_filename)
	return