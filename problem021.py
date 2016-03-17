
import math
from helperfunctions import primes, primeFactorsList

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
    
def problem021(n):
    ans = 0
    primesl = primes(int(math.sqrt(n))+1)
    factorsum = [0]*n
    for i in range(2, n):
        factorsum[i] = divisorsSum(primeFactorsList(i, primesl)) - i
        if factorsum[i] < i and i == factorsum[factorsum[i]]:
            ans += factorsum[i]
            ans += i
    return ans

print(problem021(10**4))

