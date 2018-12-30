# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:51:04 2016

@author: qnl
"""
from __future__ import division
import numpy as np
import fractions

count = 0

for i in xrange(4,12001):
    start = np.floor(i/3)+1
    end = np.ceil(i/2)-1   
    for j in xrange(int(start), int(end)+1):
        if fractions.gcd(i,j)==1:
            count += 1
            
print count