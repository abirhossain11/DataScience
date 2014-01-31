# -*- coding: utf-8 -*-
"""
RemainingLifetimes.py
Excercise 2.2 from ThinkStats2

Created on Mon Jan 27 13:59:14 2014
~ 45 min

@author: rlouie
"""

import thinkstats2
import pyplot

def RemainingLifetimes(pmf, age):
    """
    Inputs:
        
        pmf:  Probability Mass Function Object of lifetimes
        age: age (a integer in years)
    
    Outputs: 
        
        
    """
    
    copy = pmf.Copy()
    
    # leave remaining lifetime years (remove ages younger than current) 
    for val in copy.Values():
        if val <= age:
            pmf.Remove(val)

    pmf.Normalize()
    
    return pmf

if __name__ == '__main__':    
    pmf = thinkstats2.MakePmfFromList([1, 2, 2, 3, 4, 5])
    rl_pmf = RemainingLifetimes(pmf, 2)
    pyplot.bar
    
        
    
    
    
