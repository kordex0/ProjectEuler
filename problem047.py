
from helperfunctions import primeFactorsSet, primeFactorsList

def problem047():
    count = 0
    i = 1
    while True:
        if len(primeFactorsSet(i)) == 4:
            count += 1
        else:
            count = 0
        if count == 4:
            return i - 3
        i += 1

print(problem047())
