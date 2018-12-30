import numpy as np

#make a list of all the prime numbers below 1e14

#generate list of Harshad numbers below n

def isHarshad(n):
    return n%sumOfDigits(n)==0

def sumOfDigits(n):
    if n==0:
        return 0
    else:
        return n%10+sumOfDigits(n/10)

def isPrime(n):
    if n==2:
        return True
    for i in range(2,int(np.ceil(np.sqrt(n)))+1):
        if n%i == 0:
            return False
    return True

def prime_numbers(limit=int(1e14)):
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

harshad = []
strongharshad = []

#generate all the right truncatable Harshad numbers
for i in xrange(10,100):
    if isHarshad(i):
        harshad.append(i)

for i in harshad:
    for j in range(10):
        test = i*10+j
        if isHarshad(test):
            harshad.append(test)
    if i > 1e14:
        break

