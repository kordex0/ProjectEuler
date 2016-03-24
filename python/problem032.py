
def isPandigital(i, j):
    s = str(i) + str(j) + str(i * j)
    if len(s) != 9:
        return False
    for i in "123456789":
        if not i in s:
            return False
    return True

def problem032():
    ans = set()
    for i in range(9876):
        for j in range(10 * (4-len(str(i))), 10 * (8-len(str(i)))):
            if isPandigital(i, j):
                ans.add(i*j)
    return sum(ans)

print(problem032())

