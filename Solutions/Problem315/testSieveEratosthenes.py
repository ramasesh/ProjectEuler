# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:14:23 2016

@author: qnl
"""
import time
import numpy

def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True
    sublimit = int(numpy.sqrt(limit))    
    
    for i in primes:
        if i<sublimit:
            factors = range(i,limitn, i)
            for f in factors[1:]:
                primes[f] = False
    return [i for i in primes if primes[i]==True]

def prime_numbers(limit=1000000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...    
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit**0.5) 
    flags = [False, False] + [True] * (limit - 2)   
    # Step through all the odd numbers
    for i in range(3, limit, 2):       
        if flags[i] is False:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*3, limit, i<<1):
                flags[j] = False
#                flags[j] = True

start_time = time.time()

#a = primes_sieve1(20000000)
a = prime_numbers(2000000000000000)                
                
print("--- %s seconds ---" % (time.time() - start_time))
