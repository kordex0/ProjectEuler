
from helperfunctions import isPrime



def problem058():
    i = 1
    total = 0
    primes = 0
    a = 1
    b = 1
    c = 1
    while True:
        a += (i*8) - 6
        b += (i*8) - 4
        c += (i*8) - 2
        total += 4
        if isPrime(a):
            primes += 1
        if isPrime(b):
            primes += 1
        if isPrime(c):
            primes += 1
        if primes / float(total) <= 0.1:
            return i*2 + 1
        
        i += 1

print(problem058())
