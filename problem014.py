
chain = {}

def chainLength(n):
    if n == 1:
        return 1
    elif n in chain:
        return chain[n]
    else:
        if n % 2 == 0:
            m = int(n/2)
        else:
            m = 3*n + 1
        l = chainLength(m) + 1
        chain[n] = l
        return l

def problem014():
    l = 0
    n = 0
    for i in range(1, 1000000):
        if chainLength(i) > l:
            l = chainLength(i)
            n = i
    return n
    
print(problem014())

