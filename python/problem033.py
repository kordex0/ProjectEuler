
from fractions import Fraction

def cancels(a, b):
    al = int(a / 10)
    ar = a % 10
    bl = int(b / 10)
    br = b % 10

    if al == br and ar != 0 and Fraction(a, ar) == Fraction(b, bl):
        return True
    if ar == bl and br != 0 and Fraction(a, al) == Fraction(b, br):
        return True
    return False

def problem033():
    top = 1
    bottom = 1
    for a in range(10, 100) :
        for b in range(a + 1, 100):
            if cancels(a, b):
                top *= a
                bottom *= b
    return Fraction(top, bottom).denominator

print(problem033())

