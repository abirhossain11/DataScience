import thinkstats2

def PmfMean(pmf):
	"""
	pmf: prob mass function object
	"""
	mean = 0
	
	for val, freq in pmf.Items():
		mean += freq*val

	return mean

v = [1,1,2,3,4]
pmf = thinkstats2.MakePmfFromList(v)
print "Mean = ", PmfMean(pmf)
