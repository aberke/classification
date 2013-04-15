# produces a confusion matrix for the differences between two files

import sys

def confusion(results_filename, expected_filename):
	f_results = open(results_filename, 'r')
	f_expected = open(expected_filename, 'r')
	
	mat = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	]
	
	# compare line by line
	line_results = f_results.readline()
	line_expected = f_expected.readline()
	while line_expected and line_results:
		desired = int(line_expected.split(' ')[1])
		actual = int(line_results.split(' ')[1])
		
		mat[actual][desired] += 1
		
		line_results = f_results.readline()
		line_expected = f_expected.readline()
	
	f_results.close()
	f_expected.close()
	print "\n".join(["\t".join(map(str, r)) for r in mat])
	return

confusion(sys.argv[1], sys.argv[2])