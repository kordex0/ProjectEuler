
def isTriangleWord(s):
    s = s.lower()
    value = 0
    for c in s:
        value += (ord(c) - 96)
    
    value *= 2
    sqrt = int(value ** 0.5)
    return value == sqrt * (sqrt+1)

def problem042():
    ans = 0
    words = open("problem042_words.txt").readline()[:-1].split(",")
    for word in words:
        word = word[1:-1]
        if isTriangleWord(word):
            ans += 1
    return ans

print(problem042())

