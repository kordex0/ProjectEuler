def primeFactors(n):
    i = 2
    d = {}
    while n % i == 0:
        d[i] = d.get(i, 0) + 1
        n /= i
    i = 3
    while i <= n:
        while n % i == 0:
            d[i] = d.get(i, 0) + 1
            n /= i
        i += 2
    
    return d
        
def mergeMaxDicts(a, b):
    for k in b:
        a[k] = max(a.get(k,0), b[k])
    return a

def problem005():
    d = {}
    num = 1
    for i in range(2, 20):
        d = mergeMaxDicts(d, primeFactors(i))
    for k in d:
        num *= k ** d[k]
    return num

print(problem005())
