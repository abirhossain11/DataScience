import thinkstats2
import PmfMean

def PmfVar(pmf):
	"""
	inputs:
		pmf: probability mass function
	outputs:
		var: variance
	"""

	var = 0
	mean = PmfMean(pmf)

	for val, freq in pmf.Items():
		var += freq*(mean - val)**2

	return var

