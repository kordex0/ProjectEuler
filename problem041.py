
from itertools import permutations
from helperfunctions import isPrime

def problem041():
    ans = 0
    s = ""
    for i in range(1, 8):
        s += str(i)
    for p in permutations(s):
        p = int("".join(p))
        if isPrime(p):
            ans = p
    return ans

print(problem041())

