
from helperfunctions import properFactors

def isAbundant(n):
    return sum(properFactors(n)) > n

def problem023():
    abundant = []
    for i in range(28124):
        if isAbundant(i):
            abundant.append(i)
    
    nums = [True]*28124
    
    print(len(abundant))
    
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            tmp = abundant[i]+abundant[j]
            if tmp >= 28124:
                break
            nums[tmp] = False
    return sum([i for i in range(28124) if nums[i]])
    

print(problem023())

