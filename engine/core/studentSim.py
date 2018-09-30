#!/usr/bin/python
from difflib import SequenceMatcher as SM

def sim(queryNama):
	import studentList
	students = studentList.students
	maxprob = 0
	studentNim = range(3)
	for data in students:
		data = list(data)
		name = data[1]
		prob = SM(None, queryNama, name).ratio()
		if(prob > maxprob):
			maxprob = prob
			if maxprob > 0.6:
				studentNim[0] = data[0]
				studentNim[1] = name
				studentNim[2] = maxprob
	if(maxprob<=0.6):
	    return False
	else:
	    return studentNim