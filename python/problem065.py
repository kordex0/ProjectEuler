
from continuedfractions import convergentsIterator

def ePartialDenominators():
    i = 1
    while True:
        if i == 1:
            yield 2
        elif i % 3 == 0:
            yield int(i/3) * 2
        else:
            yield 1
        i += 1

def problem065():
    i = 1
    for x, y in convergentsIterator(ePartialDenominators()):
        if i == 100:
            return sum(map(int,str(x)))
        i += 1

print(problem065())
