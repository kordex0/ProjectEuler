
# (x - n)(y - n) = n^2

# n^2 = 2^4 3^4 5^2 7^2 11^2 13^2 
# n = 2^2 3^2 5^1 7^1 11^1 13^1 = 180180

import math
from helperfunctions import factors

def problem108():
    i = 4
    while True:
        f = len(factors(i*i))
        print(f)
        if f > 2000:
            return i
        i += 1

print(problem108())

