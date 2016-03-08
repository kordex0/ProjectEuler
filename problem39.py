
maxn = 0
p = 0

for i in range(3, 1000):
    n = 0
    for a in range(1, i // 2):
        for b in range(1, a):
            c = i - (a + b)
            if a*a + b*b == c*c:
                n += 1
    if n > maxn:
        maxn = n
        p = i
    
print(p)
