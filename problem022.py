
def score(s):
    score = 0
    for c in s:
        score += (ord(c) - 64)
    return score

def problem022():
    names = open("problem022_names.txt", "r").readline()[:-1].split(",")
    names = sorted(names)
    ans = 0
    for i, name in enumerate(names):
        name = name[1:-1]
        ans += (i+1) * score(name)
    return ans

print(score("COLIN"))

print(problem022())
