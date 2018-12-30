import numpy as np

def gcdVinay(a,b):
    if a==b:
        return a
    elif a==0:
        return b
    elif b==0:
        return a
    elif a < b:
        return gcdVinay(a,b%a)
    else:
        return gcdVinay(b,a%b)

def totient(n):
    count = 0
    for i in range(1,n):
        if gcdVinay(i,n)==1:
            count += 1
    return count

maxRat = 0
nMaxRat = 0
for i in range(2,1000001):
    a = i/float(totient(i))
    if a > maxRat:
        maxRat = a
        nMaxRat = i

