
import math

def problem009():
    for a in range(2, 999):
        for b in range(2, 1000-a):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                return int(a*b*c)

print(problem009())

