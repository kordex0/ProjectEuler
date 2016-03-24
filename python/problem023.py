
import math
from primes import primes
from factors import primeFactorsList
from helperfunctions import properFactors, primes, primeFactorsList

def isAbundant(n):
    return sum(properFactors(n)) > n

def problem023():
    primesl = primes(int(math.sqrt(28124)))
    abundant = []
    for i in range(28124):
        if isAbundant(i):
            abundant.append(i)
    
    nums = [True]*28124
    
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            tmp = abundant[i]+abundant[j]
            if tmp >= 28124:
                break
            nums[tmp] = False
    return sum([i for i in range(28124) if nums[i]])

def divisorsSum(factors):
    if len(factors) == 0:
        return 1
    base = factors[0]
    i = 1
    while i < len(factors) and factors[i] == base:
        i += 1
    partialSum = divisorsSum(factors[i:])
    fullSum = partialSum
    for power in range(i):
        fullSum *= base
        fullSum += partialSum
    return fullSum

def isAbundantb(n, primes):
    return divisorsSum(primeFactorsList(n, primes)) > 2*n

def problem023b():
    primesl = primes(int(math.sqrt(28124)))
    abundant = []
    for i in range(1,28124):
        if isAbundantb(i, primesl):
            abundant.append(i)
    
    nums = [True]*28124
    
    for i, a in enumerate(abundant):
        for b in abundant[i:]:
            tmp = a+b
            if tmp >= 28124:
                break
            nums[tmp] = False
    return sum([i for i in range(28124) if nums[i]])
    

print(problem023())
print(problem023b())

import timeit

print(timeit.timeit("problem023()", setup="from __main__ import problem023", number=1))

print(timeit.timeit("problem023b()", setup="from __main__ import problem023b", number=1))

