
def ispandigital(n):
    if len(sum) != 9:
        return False
    s = set()
    for c in n:
        if c in s:
            return False
        s.add(c)
    if '0' in s:
        return False
    return len(s) == 9

l = []
for i in range(1, 10000):
    sum = ""
    for n in range(1, 1000):
        sum += str(n * i)
        if len(sum) > 9:
            break
        if len(sum) < 9:
            continue
        if n == 1:
            continue
        if ispandigital(sum):
            l.append(sum)

print(l[-1])
