
from helperfunctions import primeFactorsSet

def problem003(n):
    return max(primeFactorsSet(n))
    
print(problem003(600851475143))

