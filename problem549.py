
import pytest-benchmark

factors = {2: {2: 1}}

def add_dict(a, b):
    for k, v in b.items():
        a[k] = a.get(k, 0) + v
    return a

def prime_factors(n, cur=None):
    realn = n
    f = {}
    if n % 2 == 0:
        f[2] = 1
        n //= 2
    else:
        i = 3
        while i <= n:
            if n % i == 0:
                n //= i
                f[i] = 1
                break
            i += 2
    if n != 1:
        f = add_dict(f, factors[n])
    factors[realn] = f.copy()
    return f if cur is None else add_dict(cur, f)

def smaller_dict(a, b):
    for k, v in a.items():
        if v > b.get(k,0):
            return False
    return True

def S(n):
    f = 2
    fpf = prime_factors(f)
    factprimefactors = {2: fpf}
    ans = 0
    f = 2
    fpf = prime_factors(f)
    for i in range(2, n+1):
        f = 2
        fpf = factprimefactors[2]
        ipf = prime_factors(i)
        while not smaller_dict(ipf, fpf):
            f += 1
            if f not in factprimefactors:
                factprimefactors[f] = prime_factors(f, fpf.copy())
            fpf = factprimefactors[f]
        ans += f
    return ans
    
benchmark(S, 10000)
