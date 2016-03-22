
from factors import primeFactorSet

def problem003(n):
    return max(primeFactorSet(n))
    
print(problem003(600851475143))

