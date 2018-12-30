# -*- coding: utf-8 -*-
"""
Created on Fri May 20 23:03:29 2016

@author: Vinay

Clocks, Max and Sam's

"""
import numpy as np


d0 = '0b1110111'
d1 = '0b0010010'
d2 = '0b1011101'
d3 = '0b1011011'
d4 = '0b0111010'
d5 = '0b1101011'
d6 = '0b1101111'
d7 = '0b1110010'
d8 = '0b1111111'
d9 = '0b1111011'

digits = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9] #Would a dictionary be better here?

# make array to hold the number of segments contained in each letter
litCount = np.zeros(len(digits))

for i in range(len(digits)):
    digit_string = digits[i]
    litCountTemp = 0
    for char in digit_string:
        if char=='1':
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

def digitsum(n):
    #works as long as n is less than 10^8
    sum = 0
    for i in range(10):
        sum += n%10
        n /= 10
    return sum
    
def transitMax(a,b):
    #this is for the guy that does things Smartly
    #assumes a > b, as it will be in the relevant case where b is the digit sum of a
    numTransits = 0
    while b>0:
        numTransits += changeCount[b%10][a%10]
        b = b/10
        a = a/10
    while a>0:
        numTransits += litCount[a%10]
        a = a/10
    return numTransits

def totalMax(a):
    count = 0
    tempA = a
    while tempA>0:
        count += litCount[tempA%10]
        tempA /= 10
    b = digitsum(a)
    while not a == b:
        count += transitMax(a,b)
        temp = digitsum(b)
        a = b
        b = temp
    count += litCount[b]
    return count
    
def transitSam(a):
    count = 0
    while a > 0:
        count += litCount[a%10]
        a /= 10
    count *= 2
    return count
    
def totalSam(a):
    count = transitSam(a)    
    while not a / 10 == 0:
        a = digitsum(a)        
        count += transitSam(a)
    
    return count
    
    
    
    
def prime_numbers(limit=20000000):
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
    
diff = 0
prime = prime_numbers()
for i in prime:
    if i<10000000:
        continue
    diff += totalMax(i) - totalSam(i)
print(diff)
    
