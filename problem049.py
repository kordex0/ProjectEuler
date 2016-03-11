
from helperfunctions import isPrime

def isPerm(a, b):
    a = str(a)
    b = str(b)
    for c in a:
        if c in b:
            p = b.index(c)
            b = b[:p] + b[(p+1):]
        else:
            return False
    return True

def problem049():
    for i in range(1000, 3339):
        if i == 1487:
            continue
        for j in range(0, 3):
            if not isPerm(i, i + 3330*j) or not isPrime(i + 3330*j):
                break
        else:
            return int(str(i) + str(i+3330) + str(i+6660))

print(problem049())
