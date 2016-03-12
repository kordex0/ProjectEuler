
import math

def problem020():
    ans = 0
    for c in str(math.factorial(100)):
        ans += int(c)
    return ans

print(problem020())

