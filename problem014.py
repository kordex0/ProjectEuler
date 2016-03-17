
from helperfunctions import range

def chainLength(n, chain):
    if n == 1:
        return 1
    elif n in chain:
        return chain[n]
    else:
        if n % 2 == 0:
            l = chainLength(n//2, chain) + 1
        else:
            m = (3*n + 1)//2
            l = 2
            while m % 2 == 0:
                m //= 2
                l += 1
            l += chainLength(m, chain)
        chain[n] = l
        return l

def problem014():
    chain = {1:1}
    l = 0
    n = 0
    for i in range(1, 1000000):
        if chainLength(i, chain) > l:
            l = chain[i]
            n = i
    return n
    
print(problem014())

import timeit

print(timeit.timeit("problem014()", setup="from __main__ import problem014", number=2))

