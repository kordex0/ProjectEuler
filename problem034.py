
import math

def checkNum(n):
    ans = 0
    for c in str(n):
        ans += math.factorial(int(c))
    return ans == n

def problem034():
    ans = 0
    for i in range(10, 100000):
        if checkNum(i):
            ans += i
    return ans

print(problem034())

