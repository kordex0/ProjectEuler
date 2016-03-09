
def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
        i += 2
    return True

def primes(limit):
    if limit < 2:
        return []
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    for i in range(2, limit):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False
    
    return [i for i in range(limit) if primes[i]]
    
def factors(n):
    l = []
    for i in range(1,int(n**0.5)):
        if n % i == 0:
            l.append(i)
            l.append(int(n/i))
    return l

