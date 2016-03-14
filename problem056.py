
def digitSum(n):
    n = str(n)
    ans = 0
    for c in n:
        ans += int(c)
    return ans

def problem056():
    
    ans = 0
    for a in range(1, 101):
        for b in range(1, 101):
            ans = max(ans, digitSum(a**b))
    
    return ans

print(problem056())
