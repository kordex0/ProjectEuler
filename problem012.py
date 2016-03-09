
from helperfunctions import factors

def problem012():
    i = 1
    while True:
        n = int((i*(i+1))/2)
        if len(factors(n)) > 500:
            return n
        i += 1
    
print(problem012())

