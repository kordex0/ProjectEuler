
def problem071():

    s = set()
    
    for d in range(10**6, 1, -1):
        if d % 7 == 0:
            return ((d//7)*3)-1

print(problem071())

