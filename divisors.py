
from helperfunctions import range

def divisors(n):
    l = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    return l

def properDivisors(n):
    f = factors(n)
    if n in f:
        f.remove(n)
    return f

