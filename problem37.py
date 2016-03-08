primes = set()

def isprime(n):
    if n <= 1:
        return False
    if n in primes:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    primes.add(n)
    return True
    
def checktruncate(n):
    if not isprime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not isprime(int(n[i:])):
            return False
        if not isprime(int(n[:-i])):
            return False
    return True
    
sum = 0
for i in range(10, 739398):
    if checktruncate(i):
        sum += i

print(sum)
