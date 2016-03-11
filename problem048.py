
def expLast10(a, b):
    ans = 1
    for i in range(b):
        ans *= a
        ans %= 10000000000
    return ans

def problem048():
    ans = 0
    for i in range(1, 1001):
        ans += expLast10(i,i)
        ans %= 10000000000
    
    return ans

print(problem048())
