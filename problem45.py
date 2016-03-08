

tnums = set()
maxtnum = 0
maxtn = 0

pnums = set()
maxpnum = 0
maxpn = 0

hnums = set()
maxhnum = 0
maxhn = 0

def istrianglenum(n):
    global maxtnum
    global maxtn
    global tnums
    if n > maxtnum:
        while maxtnum < n:
            maxtn += 1
            maxtnum = (maxtn * (maxtn + 1)) / 2
            tnums.add(maxtnum)
    return n in tnums

def ispentagonalnum(n):
    global maxpnum
    global maxpn
    global pnums
    if n > maxpnum:
        while maxpnum < n:
            maxpn += 1
            maxpnum = (maxpn * (3 * maxpn - 1)) / 2
            pnums.add(maxpnum)
    return n in pnums

def ishexagonalnum(n):
    global maxhnum
    global maxhn
    global hnums
    if n > maxhnum:
        while maxhnum < n:
            maxhn += 1
            maxhnum = maxhn * (2*maxhn - 1)
            hnums.add(maxhnum)
    return n in hnums
    
n = 286

while True:
    num = (n * (n + 1)) / 2
    if ispentagonalnum(num) and ishexagonalnum(num):
        print(num)
        break
    n += 1
    
    
