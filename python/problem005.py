
from helperfunctions import primeFactorsDict
        
def mergeMaxDicts(a, b):
    for k in b:
        a[k] = max(a.get(k,0), b[k])
    return a

def problem005():
    d = {}
    num = 1
    for i in range(2, 20):
        d = mergeMaxDicts(d, primeFactorsDict(i))
    for k in d:
        num *= k ** d[k]
    return num

print(problem005())

