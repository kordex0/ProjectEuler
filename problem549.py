
from helperfunctions import primeFactorsDict

factors = {2: {2: 1}}

def add_dict(a, b):
    for k, v in b.items():
        a[k] = a.get(k, 0) + v
    return a

def smaller_dict(a, b):
    for k, v in a.items():
        if v > b.get(k,0):
            return False
    return True

def S(n):
    f = 2
    fpf = primeFactorsDict(f)
    factprimefactors = {2: fpf}
    ans = 0
    f = 2
    fpf = primeFactorsDict(f)
    for i in range(2, n+1):
        f = 2
        fpf = factprimefactors[2]
        ipf = primeFactorsDict(i)
        while not smaller_dict(ipf, fpf):
            f += 1
            if f not in factprimefactors:
                factprimefactors[f] = add_dict(primeFactorsDict(f), fpf)
            fpf = factprimefactors[f]
        ans += f
    return ans
    
#print(S(10000))

def problem549():
    for i in range(2, 10**8):
        for k, v in primeFactorsDict(i).items():
            pass
    

print(problem549())
