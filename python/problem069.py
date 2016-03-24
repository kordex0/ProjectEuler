
from helperfunctions import primeFactorsSet

def p(n):
    ans = n
    for p in primeFactorsSet(n):
        ans *= (1 - (1/p))
    
    return int(ans)

def problem069():
    ans = 0
    
    for i in range(1, 10**6 + 1):
        print(i)
        ans = max(ans, i/p(i))
    
    return ans

print(problem069())

