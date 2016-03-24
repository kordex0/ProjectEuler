
import math
from fractions import gcd

def problem009b(s): # from projecteuler
    s2 = s // 2
    mlimit = int(math.sqrt(s2))
    for m in range(2, mlimit):
        if s2 % m == 0:
            sm = s2 // m
            while sm % 2 == 0:
                sm //= 2
            k = m + 2 if m % 2 == 1  else m+1
            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2//(k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    return a*b*c
                k += 2

print(problem009(1000))

