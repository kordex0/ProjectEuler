
from continuedfractions import convergentsIterator, sqrtPartialDenominators

def countDigits(n):
    return len(str(n))

def problem057():
    ans = 0
    for i, (num, den) in enumerate(convergentsIterator(sqrtPartialDenominators(2))):
        if countDigits(num) > countDigits(den):
            ans += 1
        if i == 1000:
            return ans

print(problem057())
