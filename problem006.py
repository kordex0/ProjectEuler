
def problem006(n):
    s = 0
    return ((n*(n+1))//2)**2 - ((n*(n+1)*(2*n+1))//6)
    
print(problem006(100))

