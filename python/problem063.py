
def countDigits(n):
    return len(str(n))

def problem063():
    ans = 0
    for b in range(1, 100):
        for a in range(1, 100):
            i = countDigits(a**b)
            if i == b:
                ans += 1
            elif i > b:
                break
    return ans
            
print(problem063())
