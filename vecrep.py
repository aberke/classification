#vecrep.py file
# file 1 for classification project
import sys
from vecrep_util import parse, tokenize, create_stopwords_set, create_features_dict

import searchio  # import our own optimized I/O module

			
# helper to createIndex: after the index is created, must print it to the ii_filename file
# input: filename of index (ii_filename)
#		 total number of docs (N)
#		 index to represent on disk (index)
# index is built in form {'term': [df, [[pageID, wf, [position for position in page]] for each pageID]]}
# write out index in format:  term*df&pageID_0%wf% pos_0 pos_1&pageID_1%wf% pos_0 pos_1 pos2&pageID_2%wf% pos_0
# 		--> print one line for each word in index
def printIndex(ii_filename, N, index):
	searchio.createIndex(ii_filename, N, index)

# input: <stopWords filename>, <pagesCollection filename>, <features filename>, <vecRep output filename to be built>
# output: write to the files
def main(stopwords_filename, pagesCollection_filename, features_filename, output_filename):
	# open up output file for writing
	output_file = open(output_filename, 'w')

	# obtain the stopwords in a set for quick checking
	stopWords_set = create_stopwords_set(stopwords_filename)
	# obtain features in a dictionary {feature: featureIndex for feature in features_filename} to allow both quick checking and mapping feature to its index
	features_dict = create_features_dict(features_filename)
	# initialize empty index with structure {docID: (occurances, {})}
	index = {}

	# obtain dictionary mapping pageID's to list of title and text words, ie collection = {pageID: [list of tokens]}
	(collection, maxID) = parse(pagesCollection_filename)

	# iterate over keys (pageID's) to fill the index
	for i in range(maxID+1):
		if not i in collection:
			continue
		# otherwise increment total number of documents and process page
		N += 1 # increment total documents

		curr_page_index = {}  # build up temporary dictionary mapping {"term_t": [tf_t, [position for position in page]] for term_t in page}

		pageID = i
		collection[i]
		
		# tokenize titleString
		token_list = searchio.tokenize(stopWords_set, textString, False)
		
		# add to index:
		position = 0
		for t in range(len(token_list)):
			token = token_list[t]

			# now put token in curr_page_index dict which has structure {"term_t": [tf_t, [position for position in page]] for term_t in page}
			if not token in curr_page_index:
				# create new temp_postings entry
				curr_page_index[token] = [0,[]] # page_postings entry initialized to [tf=0, positions=[]]

			curr_page_index[token][0] += 1 # increment tf
			curr_page_index[token][1].append(position) #append position to postings list
			# now just adjust position
			position += 1


		# now curr_page_index built --> need to calculate wf and insert [pageID, wf, [positions]] into index
		# first calculate length of document vector:
		curr_norm = docVecNorm(curr_page_index)
		# now calculate wf for each term in document and insert [pageID, wf, [positions]] into index
		for term in curr_page_index:
			# create new post to insert into index
			new_post = formPost(pageID, curr_page_index[term], curr_norm)

			# insert new post into index
			if not term in index:
				# create new postings entry
				index[term] = [0, []] # postings initialized to [df=0, postings=[]]
			# append post to postings
			index[term][0] += 1 # increment df
			index[term][1].append(new_post) # append post to postings list

	# now the index is built in form {'term': [df, [[pageID, wf, [position for position in page]] for each pageID]]}
	titleIndex_file.close() # done writing to titleIndex
	printIndex(ii_filename, N, index)
	return index
				
main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])