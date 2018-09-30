#!/usr/bin/python
from difflib import SequenceMatcher as SM

def sim(queryNama):
	import mkList
	mkList = mkList.matkuls
	maxprob = 0
	mkData = range(3)
	for data in mkList:
		data = list(data)
		name = data[1]
		prob = SM(None, queryNama, name).ratio()
		if(prob > maxprob):
			maxprob = prob
			if maxprob > 0.6:
				mkData[0] = data[0]
				mkData[1] = name
				mkData[2] = maxprob
	if(maxprob<=0.6):
	    return False
	else:
	    return mkData
	