
def problem016():
    n = 2**1000
    s = 0 
    for i in str(n):
        s += int(i)
    return s

print(problem016())

