
from helperfunctions import nprimes

def problem007(n):
    return nprimes(n)[n-1]
    
print(problem007(10001))

