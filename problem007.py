
import math, sys

from helperfunctions import primes

def problem007(n):
    x = int(2**(math.log(n)//math.log(2)))
    if (x > 5395):
        epsilon = -1
    else:
        epsilon = 2
    while x / (math.log(x)+epsilon) < n:
        x *= 2
    primel = primes(x)
    
    return primel[n-1]
    
print(problem007(10001))

import timeit

print(timeit.timeit("problem007(10001)", setup="from __main__ import problem007", number=100))

