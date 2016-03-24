

def primeFactorSiev(limit): # still need to find factors
    if limit < 2:
        return []
    primes = [True]*limit
    primes[0] = primes[1] = False
    factors = [None]*limit
    
    def partialSiev(p, primes, factors):
        for i in range(2*p, limit, p):
            primes[i] = False
            tmp = i
            while i % p == 0:
                i /= p
                # factors[i].append(p)
                
    partialSiev(2, primes, factors)
    partialSiev(3, primes, factors)
    
    for i in range(5, limit, 6):
        if primes[i]:
            partialSiev(i, primes, factors)
        if primes[i+2]:
            partialSiev(i+2, primes, factors)
    
    return [i for i in range(limit) if primes[i]]
    
#print(S(10000))

def problem549():
    primeFactorSiev(10**8)
    return 0

print(problem549())
