numA = 1
numB = 1
numC = 1
numD = 1
total = 1
primes = 0

def isprime(n):
    i = 2
    if n < 2:
        return False
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

i = 0
while True:
    numA += (i*8) + 2
    numB += (i*8) + 4
    numC += (i*8) + 6
    total += 4
    if(isprime(numA)):
        primes += 1
    if(isprime(numB)):
        primes += 1
    if(isprime(numC)):
        primes += 1
    if primes / total < 0.1:
        print(i)
        break
    i += 1
    
