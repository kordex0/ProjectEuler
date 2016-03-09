
import math

def isPrime(n):
    sqrt = int(math.sqrt(n))
    if n % 2 == 0:
        return False
    i = 3
    while i <= sqrt:
        if n % i == 0:
            return False
        i += 1
    return True

def problem007():
    count = 1
    n = 3
    while True:
        if isPrime(n):
            count += 1
            if count == 10001:
                return n
        n += 2
    
print(problem007())
