
from itertools import permutations

def problem043():
    ans = 0
    s = ""
    for i in range(0, 10):
        s += str(i)
    
    for perm in permutations(s):
        p = "".join(perm)
        i = p[1:4]
        if not int(i) % 2 == 0:
            continue
        i = p[2:5]
        if not int(i) % 3 == 0:
            continue
        i = p[3:6]
        if not int(i) % 5 == 0:
            continue
        i = p[4:7]
        if not int(i) % 7 == 0:
            continue
        i = p[5:8]
        if not int(i) % 11 == 0:
            continue
        i = p[6:9]
        if not int(i) % 13 == 0:
            continue
        i = p[7:10]
        if not int(i) % 17 == 0:
            continue
        ans += int(p)
    return ans

print(problem043())

