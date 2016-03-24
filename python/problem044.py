
def pentagonal(n):
    l = []
    for i in range(1, n):
        l.append((i*(3*i-1))/2)
    return l

def problem044():
    pentl = pentagonal(10000)
    pents = set(pentl)
    
    s = set()
    
    for i, a in enumerate(pentl):
        for b in pentl[:i]:
            if (a-b) in pents and (a+b) in pents:
                s.add(a-b)
    return min(s)

print(problem044())

