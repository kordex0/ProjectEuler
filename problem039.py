
def problem039():
    ans = 0
    maxn = 0
    for i in range(1001):
        n = 0
        for a in range(1, i // 2):
            b = int(((i-2*a)*i)/(2*i-2*a))
            c = i - (a + b)
            if a*a + b*b == c*c:
                n += 1
        if n > maxn:
            maxn = n
            ans = i
    return ans

print(problem039())
