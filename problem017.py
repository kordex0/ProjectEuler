# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
first20 = [4,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]

#0,10,20,30,40,50,60,70,80,90
tens = [4,3,6,6,5,5,5,7,6,6]

def countLetters(n):
    s = str(n)
    if n < 20:
        return first20[n]
    elif n < 100:
        l = tens[int(s[0])]
        if s[1] != "0":
            l += countLetters(int(s[1]))
        return l
    elif n < 1000:
        l = first20[int(s[0])] + 7
        if s[1] != "0" or s[2] != "0":
            l += countLetters(int(s[1:])) + 3
        return l
    elif n == 1000:
        return 11

def problem017():
    ans = 0
    for i in range(1,1001):
        ans += countLetters(i)
    return ans
    
print(problem017())
