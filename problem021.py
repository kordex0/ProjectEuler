
from helperfunctions import properFactors

def problem021():
    ans = 0
    for i in range(1, 10000):
        a = sum(properFactors(i))
        if a != i and i == sum(properFactors(a)):
            ans += i
    return ans

print(problem021())

