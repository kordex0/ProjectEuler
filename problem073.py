
from fractions import Fraction

def problem073():
    n = 12000
    ans = 0
    a = 1
    b = 3
    for d in range(n, 2, -1):
        c = (a * d + 1) // b
        if a * d + 1 == b * c:
            break
    
    while(c != 1 and d != 2):
        tmp = (n + b)//d
        e = tmp * c - a
        f = tmp * d - b
        a = c
        b = d
        c = e
        d = f
        ans += 1
        
    return ans

print(problem073())

