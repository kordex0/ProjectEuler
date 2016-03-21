
def primeFactorDict(n):
    d = {}
    if n < 2:
        return d
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

def primeFactorList(n, primes=None):
    l = []
    if n < 2:
        return l
    
    if primes is None:
        while n % 2 == 0:
            l.append(2)
            n //= 2
        i = 3
        while i <= n:
            while n % i == 0:
                l.append(i)
                n //= i
            i += 2
    else:
        for p in primes:
            if p*p > n:
                l.append(n)
                break
            while n % p == 0:
                l.append(p)
                n //= p
            if n == 1:
                break
    return l

def primeFactorSet(n):
    s = set()
    if n < 2:
        return s
    if n % 2 == 0:
        s.add(2)
        n /= 2
        while n % 2 == 0:
            n /= 2
    if n % 3 == 0:
        s.add(3)
        n /= 3
        while n % 3 == 0:
            n /= 3
    i = 5
    while i <= n:
        if n % i == 0:
            s.add(i)
            n /= i
            while n % i == 0:
                n /= i
        if n % (i+2) == 0:
            s.add(i+2)
            n /= (i+2)
            while n % (i+2) == 0:
                n /= (i+2)
        i += 6
    return s

