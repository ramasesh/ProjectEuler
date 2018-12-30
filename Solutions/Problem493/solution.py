import numpy as np
import scipy.special

def f(a,b):
    if a==3 and b==2:
        return 3
    elif a==b:
        return scipy.special.binom(a*10,20) - sum([f(a,x) for x in range(2,a)])
    else:
        return scipy.special.binom(a,b)*f(b,b)

