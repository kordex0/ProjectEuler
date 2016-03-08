
import time

ends89 = set([89])
ends1 = set([1])

def checkchain(n):
    global ends89
    global ends1
    partial = set()
    
    while True:
        if n in ends89:
            if len(partial) > 0:
                ends89 = ends89.union(partial)
            return True
        elif n in ends1:
            if len(partial) > 0:
                ends1 = ends1.union(partial)
            return False
        partial.add(n)
        n = sum(int(c)**2 for c in str(n))
        
def checkchain2(n):
    n = sum(int(c)**2 for c in str(n))
    
    if n in ends89:
        return True
    elif n in ends1:
        return False
    

total = 0
for i in range(1,10000000):
    if(i < 1000):
        if checkchain(i):
            total += 1
    else:
        if checkchain2(i):
            total += 1
    
print(total)
