
from helperfunctions import primes

def problem050():
    primesl = primes(1000000)
    primess = set(primesl)
    ans = 0
    maxn = 0
    for i in range(len(primesl)):
        tmpsum = 0
        j = 0
        while tmpsum < 1000000 and (i+j) < len(primesl):
            tmpsum += primesl[i+j]
            j += 1
            if tmpsum in primess:
                if j > maxn:
                    maxn = j
                    ans = tmpsum
    return ans

print(problem050())
