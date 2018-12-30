##
# Project Euler problem 504
##

import numpy as np
#NOT importing division from the future

def primeFactors(n):
    #returns the prime factors of a number 'n', as a dictionary with the keys as the prime factors and the values as the power that appears in the division.
    number_to_factor = n
    primeFactors = {}
    for i in xrange(2,int(np.sqrt(n))):
        count = 0
        while number_to_factor % i == 0:
            #get all the powers of i out of the number
            count += 1
            number_to_factor = number_to_factor / i  #integer division
        if count > 0:
            primeFactors[i] = count
    return primeFactors

def smallestDivisor(n, m):
    #given a prime number n, and a power m, determines the smallest integer k such that k factorial divides n^m



