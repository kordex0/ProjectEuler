
def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0:
            return False
        if n % (i+2) == 0:
            return False
            
    return True

def primes(limit):
    if limit < 2:
        return []
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    for j in range(4, limit, 2):
        primes[j] = False
    
    if limit < 9:
        return [i for i in range(limit) if primes[i]]
    
    for j in range(9, limit, 3):
        primes[j] = False
    
    for i in range(5, int(limit**0.5)+1, 6):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False
        if primes[i+2]:
            for j in range((i+2)*(i+2), limit, i+2):
                primes[j] = False
    
    return [i for i in range(limit) if primes[i]]
    
def factors(n):
    l = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != int(n/i):
                l.append(int(n/i))
    return l

def primeFactorsDict(n):
    if n < 2:
        return {}
    d = {}
    while n % 2 == 0:
        d[2] = d.get(2, 0) + 1
        n /= 2
    i = 3
    while i <= n:
        while n % i == 0:
            d[i] = d.get(i, 0) + 1
            n /= i
        i += 2
    return d

def primeFactorsList(n):
    if n < 2:
        return []
    l = []
    while n % 2 == 0:
        l.append(2)
        n /= 2
    i = 3
    while i <= n:
        while n % i == 0:
            l.append(i)
            n /= i
        i += 2
    return l

def primeFactorsSet(n):
    if n < 2:
        return set()
    s = set()
    while n % 2 == 0:
        s.add(2)
        n /= 2
    i = 3
    while i <= n:
        while n % i == 0:
            s.add(i)
            n /= i
        i += 2
    return s

def properFactors(n):
    f = factors(n)
    if n in f:
        f.remove(n)
    return f
    

