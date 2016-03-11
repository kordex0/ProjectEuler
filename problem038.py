
def checkPandigital(n):
    s = ""
    for i in range(1, 1000):
        s += str(i*n)
        if len(s) > 9:
            return 0
        for i in range(1, 10):
            if str(i) not in s:
                break
        else:
            return int(s)
        
def problem038():
    s = set()
    for i in range(10000):
        j = checkPandigital(i)
        if j != 0:
            s.add(j)
    return max(s)

print(problem038())
