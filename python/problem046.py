
from helperfunctions import primes

def hasSum(n, primess):
    for i in range(1, int(n**0.5)):
        if (n - 2*i*i) in primess:
            return True
    
    return False

def problem046():
    primesl = primes(10000)
    primess = set(primesl)
    
    for i in range(3, 10000, 2):
        if i not in primess:
            if not hasSum(i, primess):
                return i

print(problem046())

