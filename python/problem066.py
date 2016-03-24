
from continuedfractions import convergentsIterator, sqrtPartialDenominators

def problem066():
    maxx = 0
    ans = 0
    for d in range(2,1001):
        if int(d**0.5)**2 == d:
            continue
        for x, y in convergentsIterator(sqrtPartialDenominators(d)):
            a = x**2 - d * (y**2)
            if a == 1:
                if x > maxx:
                    maxx = x
                    ans = d
                break
            else:
                x += 1
                continue
    return ans

print(problem066())
