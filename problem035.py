
from helperfunctions import primes

def isCircular(p, primess):
    s = str(p)
    if len(s) == 1:
        return p in primess
    for i in range(len(s)):
        s = s[1:] + s[0]
        if int(s) not in primess:
            return False
    return True

def problem035():
    primesl = primes(1000000)
    primess = set(primesl)
    circularprimes = set()
    for p in primesl:
        if isCircular(p, primess):
            circularprimes.add(p)
    return len(circularprimes)

print(problem035())

