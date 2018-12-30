# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
import numpy as np
import fractions


totDen = 1000001
greatest = 0
greatestNum = 0
greatestDen = 0


for i in range(totDen):
    if i == 0 or i == 7:
        continue
    largestPossible = numpy.floor(i*3/7)
    #print i, largestPossible
    if largestPossible < greatest:
        continue
    den = i
    num = largestPossible
    while not fractions.gcd(num,den)==1:
        num = num-1
    if num/den > greatest:
        greatest = num/den
        greatestNum = num
        greatestDen = den
        
print greatestNum, greatestDen
    
    
    


