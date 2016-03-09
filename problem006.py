def problem006():
    s = 0
    for i in range(1, 101):
        s += i ** 2
    return int((100*101)/2)**2 - s
    
print(problem006())
