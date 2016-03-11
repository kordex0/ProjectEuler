
# 1000000 < 9*1 + 90*2 + 900*3 + 9000*4 + 90000*5 + 100000*6

def problem040():
    ans = 1
    s = ""
    for i in range(1, 200000):
        s += str(i)
    for i in range(7):
        ans *= int(s[(10**i)-1])
    return ans

print(problem040())
