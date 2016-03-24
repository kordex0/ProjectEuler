
import math

def problem053():

    s = set()
    
    ans = 0
    for r in range(1, 101):
        tmp = 1
        for n in range(r+1, 101):
            tmp *= n
            tmp //= (n-r)
            if tmp > 10**6:
                ans += (101 - n)
                break
    return ans
            

print(problem053())
