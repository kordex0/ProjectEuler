
def getDays(n, y):
    if n in [1,3,5,7,8,10,12]:
        return 31
    elif n == 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 30
            

def problem019():
    days = 1
    sundays = 0
    for i in range(1,13):
        days += getDays(i, 1900)
    if days % 7 == 0:
        sundays += 1
    
    for i in range(1901, 2001):
        for j in range(1, 13):
            days += getDays(j, i)
            if days % 7 == 0:
                sundays += 1
    return sundays
            

print(problem019())

