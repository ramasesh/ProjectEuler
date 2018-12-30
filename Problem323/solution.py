import numpy as np

def f(x):
    a = 1-1.0/(2**(x-1))
    b = a**32
    c = 1-b
    return c

ans = f(1)
found = 0
i = 2

while not found:
    oldAns = ans
    ans = ans+f(i)
    i+=1
    diff = ans-oldAns
    if abs(diff) <= 1e-11:
        found = 1


