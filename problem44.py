
nums = set()
maxnum = 0
maxn = 0

def ispentagonalnum(n):
    global maxnum
    global maxn
    global nums
    if n > maxnum:
        while maxnum < n:
            maxn += 1
            maxnum = (maxn * (3 * maxn - 1)) / 2
            nums.add(maxnum)
    return n in nums

for i in range(2, 9999):
    for j in range(1, i):
        num = (j * (3 * j - 1)) / 2
        num2 = (i * (3 * i - 1)) / 2
        if ispentagonalnum(num + num2) and ispentagonalnum(num2 - num):
            print(num2 - num)
