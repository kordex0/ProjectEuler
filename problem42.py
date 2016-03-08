
nums = set()
maxnum = 0
maxn = 0

def istrianglenum(n):
    global maxnum
    global maxn
    global nums
    if n > maxnum:
        while maxnum < n:
            maxn += 1
            maxnum = (maxn * (maxn + 1)) / 2
            nums.add(maxnum)
    return n in nums

def istriangleword(w):
    w = w.lower()
    sum = 0
    for c in w:
        sum += (ord(c) - 96)
    return istrianglenum(sum)
    
def parsefile(f):
    count = 0
    for l in f:
        strs = l.split(",")
        for s in strs:
            s = s[1:-1]
            if istriangleword(s):
                count += 1
    return count
            

f = open("words.txt")
print(parsefile(f))


