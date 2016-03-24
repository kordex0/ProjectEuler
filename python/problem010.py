
from helperfunctions import primes

def problem010(n):
    return sum(primes(n))
    
print(problem010(2*10**6))

