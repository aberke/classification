TEAM_NAME: Alex and Matt

FULL_NAME: Matt Patenaude (SUBMITTER)
CS_LOGIN: pettarin
EMAIL_ADDRESS: pettarin@cs.brown.edu

FULL_NAME: Alexandra Berke (TEAM-MATE)
CS_LOGIN: aberke
EMAIL_ADDRESS: alexandra_berke@brown.edu

################ Notes ##################

questions:




potential optimizations:

	in classify_MNB:
		condprob has structure {t_i: {c_i:P(t_i|c_i) for c_i in categories} for t_i in features-list} , however each t_i and c_i is just an index ---> should this be a tuple?
			might not matter since number of t_i's and c_i's is relatively small
