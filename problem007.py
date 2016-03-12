
import math

from helperfunctions import isPrime

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

