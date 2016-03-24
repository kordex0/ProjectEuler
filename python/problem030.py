
def problem030():
    ans = 0
    for i in range(10, 1000000):
        s = str(i)
        tmp = 0
        for c in s:
            tmp += int(c)**5
        if tmp == i:
            ans += i
    return ans

print(problem030())

