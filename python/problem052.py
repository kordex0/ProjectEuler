
def hasSameDigits(a, b):
    a = str(a)
    b = str(b)
    
    for c in a:
        if c not in b:
            return False
        i = b.find(c)
        b = b[:i] + b[i+1:]
    return True

def problem052():
    i = 0
    cur = 1
    while True:
        for j in range(1, 7):
            if not hasSameDigits(cur, cur*j):
                break
        else:
            return cur
            
        if cur * 6 > 10**(i+1):
            i +=1
            cur = 10**i
        else:
            cur += 1

print(problem052())
