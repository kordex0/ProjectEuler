import itertools

def isprime(n):
    n = int(n)
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    

tmp = []
for i in range(1, 10):
    tmp.append(str(i))
    for perm in itertools.permutations(tmp):
        p = "".join(perm)
        if isprime(p):
            ans = p
        
    
print(ans)
