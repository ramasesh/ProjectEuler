# -*- coding: utf-8 -*-
"""
Created on Fri May 20 23:03:29 2016

@author: qnl

Clocks, Max and Sam's

"""
import numpy as np


d0 = '0b1110111'
d1 = '0b0010010'
d2 = '0b1011101'
d3 = '0b0000000'
d4 = '0b0000000'
d5 = '0b0000000'
d6 = '0b0000000'
d7 = '0b0000000'
d8 = '0b1111111'
d9 = '0b1111011'

digits = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9] #Would a dictionary be better here?

# make array to hold the number of segments contained in each letter
litCount = np.zeros(len(digits))

for i in range(len(digits)):
    digit_string = digits[i]
    litCountTemp = 0
    for char in digit_string:
        if char==1:
            litCountTemp += 1
    litCount[i] = litCountTemp

#now make a 2D array to hold the number of changes needed to make to go from one digit to another 
changeCount = np.zeros([len(digits),len(digits)])

for i in range(len(digits)):
    for j in range(len(digits)):
        digitString1 = digits[i]
        digitString2 = digits[j]
        changeCountTemp = 0
        for charIndex in range(len(digitString1)):
            if not digitString1[charIndex]==digitString2[charIndex]:
                changeCountTemp += 1
        changeCount[i][j] = changeCountTemp


    