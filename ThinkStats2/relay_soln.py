"""Ryan Louie - relay_soln.py
Excercise 3.2 from ThinkStats2 by Allen Downey
"""

import thinkstats2
from relay import *

def BiasPmf(pmf, speed):
	"""
	pmf: Pmf object
	speed: speed of running observer

	returns: Pmf representing distribution of runners' speeds as seen
	by observer

	"""

	new_pmf = pmf.Copy()
	
	for x, p in pmf.Items():
		new_pmf.Mult(x,abs(x-speed))

	new_pmf.Normalize()

	return new_pmf

def main():

    results = ReadResults()
    speeds = GetSpeeds(results)

    speeds = BinData(speeds, 3, 12, 50)

    pmf = thinkstats2.MakePmfFromList(speeds, 'speeds')
    
    speed_observer = 7.5

    bimodalpmf = BiasPmf(pmf, speed_observer)

    thinkplot.Hist(bimodalpmf)
    thinkplot.Show(title='PMF of running speed (relative to observer speed = 7.5 MPH)',
               xlabel='speed (mph)',
               ylabel='probability')


if __name__ == '__main__':
    main()