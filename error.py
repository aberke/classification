# checks for error differences in validate and results files

import sys


# prints out % number of times that results line matched validate line
def percent_classified(results_filename, validate_filename):
	f_results = open(results_filename, 'r')
	f_validate = open(validate_filename, 'r')

	total_classified = 0
	correct = 0
	# compare line by line
	line_results = f_results.readline()
	line_validate = f_validate.readline()
	while line_validate and line_results:
		total_classified += 1
		if line_results == line_validate:
			correct += 1
		else:
			print('****** line '+str(total_classified)+ ' differed: *******')
			print('results: '+line_results)
			print('validate: '+line_validate)
		line_results = f_results.readline()
		line_validate = f_validate.readline()
	f_results.close()
	f_validate.close()
	print('percent classified: '+str(float(correct)/total_classified))
	return


percent_classified(sys.argv[1], sys.argv[2])