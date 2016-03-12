
def problem048():
    ans = 0
    for i in range(1, 1001):
        ans += pow(i, i, 10**10)
    
    return ans % 10**10

print(problem048())

