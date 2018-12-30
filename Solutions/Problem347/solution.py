##
# Project Euler problem 347
##

import numpy as np

def prime_numbers(limit=1000000):                                                                          
   '''Prime number generator. Yields the series
      2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...    
      using Sieve of Eratosthenes.
   '''
   yield 2
   sub_limit = int(limit**0.5) 
   flags = [False, False] + [True] * (limit - 2)   
   
   for i in range(3, limit, 2):
       if flags[i] == False:
           continue
       yield i
       if i <= sub_limit:
           for j in range(i*3, limit, i<<1):
               flags[j] = False

primes_sol = set(prime_numbers(limit = 10000000))

def twoprimeFactors(n):
    #returns the prime factors of a number 'n', as a dictionary with the keys as the prime factors and the values as the power that appears in the division.
    number_to_factor = n
   
    if n in primes_sol:
        return False

    for ind,p in enumerate(primes_sol):
        if n % p == 0:
            number_to_factor = n
            while(number_to_factor % p) == 0:
                number_to_factor = number_to_factor // p
            break
    if number_to_factor == 1:
        return False

    new_n = number_to_factor

    for p2 in primes_sol:
        if new_n % p2 == 0:
            number_to_factor = new_n
            while(number_to_factor % p2) == 0:
                number_to_factor = number_to_factor // p2
            break
    if number_to_factor == 1:
        return (p, p2)
    else:
        return False
