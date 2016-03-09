
from helperfunctions import isPrime

def problem027():
    bestn = 0
    bestprod = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while isPrime(n**2 + a * n + b):
                n += 1
            if n > bestn:
                bestn = n
                bestprod = a*b
    return bestprod

print(problem027())
