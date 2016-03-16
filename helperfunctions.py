
import sys

def _import_module(name):
    __import__(name)
    return sys.modules[name]

# make sure to always use the iterator range
def range(*args, **kwargs):
    if sys.version_info[0] == 2:
        module = _import_module("__builtin__")
        return getattr(module, "xrange")(*args,**kwargs)
    else:
        module = _import_module("builtins")
        return getattr(module, "range")(*args,**kwargs)  

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
    limit1 = limit-1
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    primes[4:limit:2] = [False]*((limit1//2)-1)
    primes[9:limit:3] = [False]*((limit1//3)-2)
    
    for i in range(5, int(limit**0.5)+1, 6):
        if primes[i]:
            primes[i*i:limit:i] = [False]*((limit1//i)-i+1)
        if primes[i+2]:
            primes[(i+2)*(i+2):limit:(i+2)] = [False]*((limit1//(i+2))-i-1)
    
    return [i for i in range(limit) if primes[i]]
    
def factors(n):
    l = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    return l

def primeFactorsDict(n):
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

def primeFactorsList(n):
    l = []
    if n < 2:
        return l
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

def properFactors(n):
    f = factors(n)
    if n in f:
        f.remove(n)
    return f
    

