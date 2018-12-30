import numpy as np
import time

count = 0
for i in range(3,1001):
    if i%2==0:
        count += i*(i-2)
    else:
        count += i*(i-1)

print(count)
