# -*- coding: utf-8 -*-
"""
risk.py

Data Science Course
ThinkStats2 Ex 2.3

Created on Mon Jan 27 20:11:39 2014

@author: rlouie
"""

import thinkstats2

def ProbOverRange(pmf, vals):
    """
    inputs:
        pmf: probability mass function object
        vals: list of values for which probability will be calculated
    return:
        sum of probabilities for values defined by vals
    """
    totalProb = 0
    for val in vals:
        totalProb += pmf.Prob(val)
        
    return totalProb
    
def ProbEarly(pmf):
    """
    inputs:
        pmf: probability mass function object
    outpus:
        fraction of births that are considered "early"
    """
    minWeek = min(pmf.Values())
    return ProbOverRange(pmf, range(minWeek,38))

def ProbOnTime(pmf):
    """
    inputs:
        pmf: probability mass function object
    outpus:
        fraction of births that are considered "On Time"
    """
    return ProbOverRange(pmf, range(38,41))

def ProbLate(pmf):
    """
    inputs:
        pmf: probability mass function object
    outpus:
        fraction of births that are considered "late"
    """
    maxWeek = max(pmf.Values())
    return ProbOverRange(pmf, range(41, maxWeek+1))


        

