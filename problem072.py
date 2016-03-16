
def problem072():
    ans = 0
    p = range(0, 10**6+1)
    
    for i in range(2, 10**6+1):
        if p[i] == i:
            for j in range(i, 10**6+1, i):
                p[j] = p[j] - (p[j]/i)
        ans += p[i]
    return ans
    
print(problem072())

