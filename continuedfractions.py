
from fractions import Fraction
import math

# x = a0 +        1
#          -------------
#          a1 +    1
#               --------
#               a2 + ...

def convergentsIterator(it):
    A = []
    B = []
    i = 0
    for a in it:
        if i == 0:
            A.append(a)
            B.append(1)
        elif i == 1:
            A.append(a*A[i-1] + 1)
            B.append(a*B[i-1])
        else:
            A.append(a*A[i-1] + A[i-2])
            B.append(a*B[i-1] + B[i-2])
        
        f = Fraction(A[i], B[i])
        yield (f.numerator, f.denominator)
        i += 1

def sqrtPartialDenominators(n):
    m = [0]
    d = [1]
    a = [int(math.sqrt(n))]
    i = 0
    while True:
        yield a[i]
        i += 1
        m.append(d[i-1]*a[i-1]-m[i-1])
        d.append(int((n-m[i]**2)/d[i-1]))
        a.append(int((a[0]+m[i])/(d[i])))
        

