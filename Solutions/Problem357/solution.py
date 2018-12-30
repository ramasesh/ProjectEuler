import numpy as np
import time


start_time = time.time()
primes_to_check = {}
success = []

count  = 0

for prime in testSieveEratosthenes.prime_numbers(100000000):
    testNumber = prime-1
    primes_to_check[prime] = True
    for i in xrange(2,int(np.sqrt(testNumber))):
        if testNumber % i == 0:
            if (i + testNumber/i) not in primes_to_check:
                break
    else:
        count += testNumber
        success.append(testNumber)

elapsed_time = time.time() - start_time
