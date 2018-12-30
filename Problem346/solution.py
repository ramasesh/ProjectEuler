from __future__ import division
import time
import timeit

#variables to look at the time of this program
dictionaryTimeCount = 0
startTime = time.time()

N = 1000000000

sum_repunits = 1
repunits = {}
repunits[1]=True

for i in xrange(2,N):
    number = 1+i+i*i
    while number < N:
        time1 = time.time()
        repeated = number in repunits
        time2 = time.time()
        dictionaryTimeCount += time2-time1

        if not repeated:
            repunits[number]=True
            sum_repunits += number
        number = i * number + 1

print sum_repunits

elapsedTime = time.time() - startTime
print elapsedTime
print dictionaryTimeCount/elapsedTime

