"""
mode.py
author: ryan louie
date: 1/26/2014

Citations:
Allen Downey for the tip on passing operator.itemgetter as a key to sorted
"""

import thinkstats2
import operator

def mode(hist):
	""" 
	returns the statistical mode(s) of a historgram

	hist: Hist object 
	"""
	modeVal = []
	modeFreq = 0
	
	for val in hist.Values():
		
		if hist.Freq(val) == modeFreq:
			modeVal.append(val)
		
		else:
			if hist.Freq(val) > modeFreq:
				modeVal = [val]
				modeFreq = hist.Freq(val)

	return modeVal

def AllModes(hist):
	"""
	returns a sorted, decending list of (val, freq) pairs by frequency

	hist: Hist object
	"""
	
	return sorted(hist.Items(), key=operator.itemgetter, reverse=True)


hist = thinkstats2.MakeHistFromList([1, 2, 2, 2, 3, 3, 3])
print mode(hist)
print AllModes(hist)

