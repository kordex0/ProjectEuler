
from helperfunctions import primes

def countPrimeFamily(p, indeces, primes):
    count = 0
    l = list(p)
    if 0 in indeces:
        start = 1
    else:
        start = 0
    for i in range(start, 10):
        for j in indeces:
            l[j] = str(i)
        if int("".join(l)) in primes:
            count += 1
    return count

def countPrimeFamilies(p, c, primes):
    ans = 0
    p = str(p)
    c = str(c)
    indeces = [p.find(c)]
    while p.find(c, indeces[-1]+1) != -1:
        indeces.append(p.find(c, indeces[-1]+1))
        
    for x in range(1, 2**len(indeces)):
        tmpindeces = []
        for i in range(0, len(indeces)):
            if x % 2 == 1:
                tmpindeces.append(indeces[i])
            x //= 2
        ans = max(ans, countPrimeFamily(p, tmpindeces, primes))
        
    return ans

def problem051():
    primelist = primes(1000000)
    primeset = set(primelist)
    
    for p in primelist:
        p = str(p)
        if p.count("0") >= 2:
            if countPrimeFamilies(p, 0, primeset) == 8:
                return p
        if p.count("1") >= 2:
            if countPrimeFamilies(p, 1, primeset) == 8:
                return p
        if p.count("2") >= 2:
            if countPrimeFamilies(p, 2, primeset) == 8:
                return p
                

print(problem051())

