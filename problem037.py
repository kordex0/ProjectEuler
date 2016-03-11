
from helperfunctions import primes

def isTruncatable(p, primess):
    s = str(p)
    for i in range(1, len(s)):
        if int(s[i:]) not in primess:
            return False
        if int(s[:-i]) not in primess:
            return False
    return True

def problem037():
    primesl = primes(1000000)
    primess = set(primesl)
    ans = 0
    for p in primesl[4:]:
        if isTruncatable(p, primess):
            ans += p
    return ans

print(problem037())
